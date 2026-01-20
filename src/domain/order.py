from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"


@dataclass
class Order:
    id: int | None
    user_id: str
    event_id: int
    quantity: int
    status: OrderStatus
    idempotency_key: str
    expires_at: datetime | None = None

    def confirm(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError("Only PENDING orders can be confirmed")
        self.status = OrderStatus.CONFIRMED

    def cancel(self):
        if self.status in (OrderStatus.CONFIRMED, OrderStatus.EXPIRED):
            raise ValueError(f"Cannot cancel {self.status} order")
        self.status = OrderStatus.CANCELLED

    def expire(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError("Only PENDING orders can expire")
        self.status = OrderStatus.EXPIRED
