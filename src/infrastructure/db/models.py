from sqlalchemy import Column, Integer, String, create_engine
from datetime import datetime
from src.infrastructure.db.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True, nullable=False)
    created_at = Column(datetime, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
