from fastapi import APIRouter, FastAPI

from src.api.v1.auth import router as auth_router
from src.logger import get_logger

app = FastAPI(title="Checkout service", version="1.0.0", debug=True)

api_v1 = APIRouter(prefix="/api/v1")

api_v1.include_router(auth_router, tags=["auth"])

app.include_router(api_v1)

logger = get_logger(__name__)

logger.info("Starting application...")


@app.get("/")
def root():
    return {"message": "Welcome to the checkout service"}
