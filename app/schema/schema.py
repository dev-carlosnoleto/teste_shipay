from pydantic import BaseModel, EmailStr
from datetime import date

# Saída da role
class RoleResponse(BaseModel):
    id: int
    description: str

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    role_id: int                
    password: str | None = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: RoleResponse          
    created_at: date

    class Config:
        from_attributes = True


class ClaimResponse(BaseModel):
    id: int
    description: str
    active: bool

    class Config:
        from_attributes = True
