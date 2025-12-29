from sqlalchemy.orm import Session
from datetime import date
import secrets
from app.models.models import User, Role
from app.schema.schema import UserCreate, UserResponse

def create_user_service(user: UserCreate, db: Session) -> UserResponse:
    # Verifica se o role existe
    role = db.query(Role).filter(Role.id == user.role_id).first()
    if not role:
        raise ValueError("Role não encontrada")

    # Gera senha aleatória se não informada
    password = user.password or secrets.token_hex(8)

    # Cria o usuário
    new_user = User(
        name=user.name,
        email=user.email,
        password=password,
        role_id=user.role_id,
        created_at=date.today()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email,
        role=role.description,
        created_at=new_user.created_at
    )
