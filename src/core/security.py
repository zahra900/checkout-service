import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.core.config import settings

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Validate RS256 JWT and extract user_id."""
    try:
        # TODO: Fetch public key from JWT_PUBLIC_KEY_URL
        payload = jwt.decode(
            credentials.credentials,
            options={"verify_signature": False},  # Replace with actual verification
            audience=settings.jwt_audience,
            algorithms=[settings.jwt_algorithm],
        )
        return payload.get("sub")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
