from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from src.main import app
from src.domain.user import UserCreate
from src.infrastructure.db.database import get_db
from src.application.user_service import create_user
@app.post('/users')
async def create_user(user: UserCreate, db:Session = Depends(get_db)):
    user = create_user(db, user)
    return user
