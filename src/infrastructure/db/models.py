from enum import Enum
from sqlalchemy import UUID, Column, ForeignKey, Integer, String, DateTime, Enum as SAEnum
from src.infrastructure.db.database import Base

class EventStatus(str, Enum):
    SCHEDULED =  "scheduled"
    CANCELLED = "cancelled"
    SOLD_OUT = "sold_out"

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    EXPIRED = "expired"
    FAILED = "failed"

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    created_at = Column(DateTime, unique=True)
    hashed_password = Column(String, nullable=False)
    role =  Column(String, nullable=False)

class Event(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, nullable=False)
    starts_at = Column(DateTime)
    status = Column(SAEnum(EventStatus), nullable=False)
    venue = Column(String, nullable=False)

class Order(Base):
    __tablename__ = 'order'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"))
    quantity = Column(Integer, nullable=False)
    status = Column(SAEnum(OrderStatus), nullable=False)
    expires_at = Column(DateTime)
    idempotency_key = Column(String)


