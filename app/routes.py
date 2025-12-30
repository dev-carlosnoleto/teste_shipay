from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schema.schema import UserCreate, UserResponse, RoleResponse
from app.services.user_service import create_user_service, get_user_service
from app.services.role_service import get_role_service  

router = APIRouter()

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar usuário
@router.post("/users/create", response_model=UserResponse, tags=["Users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_service(user, db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao criar usuário: {str(e)}"
        )

# Rota para buscar role
@router.get("/roles/{role_id}", response_model=RoleResponse, tags=["Roles"])
def get_role(role_id: int, db: Session = Depends(get_db)):
    try:
        return get_role_service(role_id, db)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"Role com ID {role_id} não encontrada"
        )

# Rota para buscar usuário
@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_user_service(user_id, db)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"Usuário com ID {user_id} não encontrado"
        )
