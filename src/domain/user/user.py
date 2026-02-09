from datetime import datetime
from enum import StrEnum
from uuid import UUID


class UserRole(StrEnum):
    ADMIN = "admin"
    USER = "user"


class User:
    def __init__(
        self,
        id: UUID,
        email: str,
        username: str,
        role: UserRole,
        created_at: datetime,
        hashed_password: str,
    ):
        self.id = id
        self.email = email
        self.username = username
        self.role = role
        self.created_at = created_at
        self.hashed_password = hashed_password
    