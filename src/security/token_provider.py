import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from sqlalchemy import UUID

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not found")

ALGORITHM = os.getenv("ALGORITHM")
if not ALGORITHM:
    raise RuntimeError("ALGORITHM not found")


def create_access_token(username: str, user_id: UUID) -> str:
    encode = {
        "sub": username,
        "id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=20),
    }
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
