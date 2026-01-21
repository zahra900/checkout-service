from src.domain.user import UserCreate
from sqlalchemy.orm import Session
from src.infrastructure.db.models import User

def create_user(user: UserCreate, db: Session):
    create_user = User(id=user.id, email=user.email, hashed_password=user.hashed_password, created_at=user.created_at)
    db.add(create_user)
    db.commit()
    db.refresh(user)
    return user
