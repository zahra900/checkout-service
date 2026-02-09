from sqlalchemy.orm import Session

from src.domain.user.user import User
from src.domain.user.user_repository import UserRepository
from src.infrastructure.db.models import UserORM


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def add(self, user: User) -> User:
        orm_user= UserORM.from_entity(user)
        self.db.add(orm_user)
        self.db.commit()
        self.db.refresh(orm_user)
        return orm_user

    def get_by_username(self, username: str) -> UserORM | None:
        return self.db.query(UserORM).filter(UserORM.username == username).first()
    
    def get_by_email(self, email: str) -> UserORM | None:
        return self.db.query(UserORM).filter(UserORM.email == email).first()
