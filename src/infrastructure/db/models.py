from enum import StrEnum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UUID, DateTime, Enum as SQLEnum
import uuid

from src.domain.user.user import User, UserRole
from src.infrastructure.db.database import Base


class EventStatus(StrEnum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    SOLD_OUT = "sold_out"


class OrderStatus(StrEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    EXPIRED = "expired"
    FAILED = "failed"


class UserORM(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)

    @classmethod
    def from_entity(cls, entity: User):
        return cls(id=entity.id,
            username=entity.username,
            email=entity.email,
            hashed_password=entity.hashed_password,
            role=entity.role,
            created_at=entity.created_at,
        )


""" class Event(Base):
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
    idempotency_key = Column(String) """
