from pydantic import BaseModel, Field


class CheckoutRequest(BaseModel):
    event_id: int
    quantity: int = Field(gt=0)
    idempotency_key: str


class CheckoutResponse(BaseModel):
    order_id: int
    status: str
    event_id: int
    quantity: int
