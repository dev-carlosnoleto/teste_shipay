from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role_id: int


class UserCreate(UserBase):
    password: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: RoleResponse
    created_at: date

    class Config:
        from_attributes = True  


class RoleResponse(BaseModel):
    id: int
    description: str

    class Config:
        from_attributes = True


class ClaimResponse(BaseModel):
    id: int
    description: str
    active: bool

    class Config:
        from_attributes = True
