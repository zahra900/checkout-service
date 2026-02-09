from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.api.v1.exceptions import UnauthorizedException
from src.security.token_provider import decode_token

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = decode_token(token)
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise UnauthorizedException
        return {"username": username, "id": user_id}
    except JWTError:
        raise UnauthorizedException
