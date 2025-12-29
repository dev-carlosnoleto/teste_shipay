from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schema.schema import UserCreate, UserResponse, RoleResponse
from app.services.user_service import create_user_service
from app.models.models import Role, User


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db   
    finally:
        db.close() 


@router.post("/users", response_model=UserResponse, tags=["Users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_service(user, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/roles/{role_id}", response_model=RoleResponse, tags=["Roles"])
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role não encontrada")
    return role

@router.get("/users/{user_id}", response_model= UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
