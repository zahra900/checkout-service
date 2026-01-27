from fastapi import Depends
from src.api.v1.schemas.user import UserInDB
from src.api.v1.schemas.user import UserCreate
from sqlalchemy.orm import Session
import uuid
from src.infrastructure.db.database import get_db
from src.infrastructure.db.models import User
from src.infrastructure.db.dependencies import db_dependency
from datetime import datetime
from passlib.context import CryptContext
from typing import Annotated

import pytz

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate, db: Session):
    user_id = str(uuid.uuid4())
    create_user = UserInDB(id=user_id, email=user.email, hashed_password=bcrypt_context.hash(user.password), created_at=datetime.now(tz=pytz.UTC))
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return create_user


def authenticate_user(username: str, password:str, db: Session):
    user = db.query(UserInDB).filter(UserInDB.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True
