from dataclasses import dataclass
from sqlalchemy import UUID

from src.domain.user.user import UserRole

@dataclass(frozen=True, slots=True)
class UserCreateDTO:
    email: str
    username: str
    role: UserRole
    password: str
    
