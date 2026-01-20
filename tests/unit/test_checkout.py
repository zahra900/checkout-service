import pytest
from src.domain.order import Order, OrderStatus


def test_order_confirm():
    order = Order(
        id=1,
        user_id="user123",
        event_id=1,
        quantity=2,
        status=OrderStatus.PENDING,
        idempotency_key="key123",
    )
    order.confirm()
    assert order.status == OrderStatus.CONFIRMED


def test_order_cancel():
    order = Order(
        id=1,
        user_id="user123",
        event_id=1,
        quantity=2,
        status=OrderStatus.PENDING,
        idempotency_key="key123",
    )
    order.cancel()
    assert order.status == OrderStatus.CANCELLED


def test_order_expire():
    order = Order(
        id=1,
        user_id="user123",
        event_id=1,
        quantity=2,
        status=OrderStatus.PENDING,
        idempotency_key="key123",
    )
    order.expire()
    assert order.status == OrderStatus.EXPIRED
