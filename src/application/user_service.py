import uuid
from datetime import datetime

from datetime import timezone
from dataclasses import asdict

from src.application.dtos import UserCreateDTO
from src.application.exceptions import AuthenticationFailed, UserNotFound
from src.domain.user.user import User
from src.domain.user.user_repository import UserRepository
from src.security.password_hasher import hash_password, verify_password
from src.security.token_provider import create_access_token


def create_user(user_dto: UserCreateDTO, user_repo: UserRepository):
    existing = user_repo.get_by_email(user_dto.email)
    if existing:
        raise ValueError("Email already registered")
    print()
    hashed_password = hash_password(user_dto.password)
    print("***********************************************************************")
    print(asdict(user_dto))
    new_user = User(
        id=str(uuid.uuid4()),
        email=user_dto.email,
        username=user_dto.username,
        hashed_password=hash_password(user_dto.password),
        role=user_dto.role,
        created_at=datetime.now(timezone.utc),
    )
    return user_repo.add(new_user)


def authenticate_user(username: str, password: str, user_repo: UserRepository):
    user = user_repo.get_by_username(username)
    if not user:
        raise UserNotFound()
    if not verify_password(password, user.hashed_password):
        raise AuthenticationFailed()
    token = create_access_token(user.username, user.id)
    return token
