from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.api.v1.schemas.user import UserCreate
from src.application.user_service import authenticate_user, create_user
from src.domain.user.user import User, UserRole
from src.infrastructure.db.dependencies import db_dependency


router = APIRouter()


@router.get("/auth", )
def create_user_api(user: UserCreate, db: db_dependency):
    user = create_user(user, db)
    return "ok"

@router.post("/token", )
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
          db: db_dependency):
    user = authenticate_user(
        form_data.username, form_data.password, db)
    if not user:
        return 'Failed Authentication'
    return 'Sucess Authentication'

