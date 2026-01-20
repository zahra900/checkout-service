from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    email: str
    created_at: datetime


class UserInDB(User):
    hashed_password: str