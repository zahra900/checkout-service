from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.domain.user.user import UserRole


class UserBase(BaseModel):
    email: str
    username: str
    role: UserRole


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserBase):
    hashed_password: str
