from sqlalchemy.orm import Session
from app.models.models import Role
from app.schema.schema import RoleResponse

def get_role_service(role_id: int, db: Session) -> RoleResponse:
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise Exception("Role não encontrada")

    return RoleResponse(
        id=role.id,
        description=role.description
    )
