from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.v1.exceptions import UnauthorizedException
from src.api.v1.schemas.user import UserCreate
from src.application.dtos import UserCreateDTO
from src.application.exceptions import AuthenticationFailed, UserNotFound
from src.application.user_service import authenticate_user, create_user
from src.domain.token import Token
from src.infrastructure.db.dependencies import db_dependency
from src.infrastructure.db.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: db_dependency):
    repo = SqlAlchemyUserRepository(db)
    user_dto = UserCreateDTO(**user.model_dump())
    created_user = create_user(user_dto, repo)
    return {"id": created_user.id, "email": created_user.email}


@router.post("/token", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    try:
        repo = SqlAlchemyUserRepository(db)
        token = authenticate_user(form_data.username, form_data.password, repo)
    except (AuthenticationFailed, UserNotFound):
        raise UnauthorizedException from None

    return {"access_token": token, "token_type": "bearer"}
