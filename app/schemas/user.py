from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models.user import AccessRole

class UserAddDTO(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserDTO(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserInfoAddDTO(BaseModel):
    access_role: AccessRole
    user_id: int

class UserInfoDTO(UserInfoAddDTO):
    id: int         
    created_at: datetime

class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str