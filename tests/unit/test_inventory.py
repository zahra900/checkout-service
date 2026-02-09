import pytest

from src.domain.inventory import InsufficientInventoryError, Inventory


def test_reserve_success():
    inv = Inventory(event_id=1, remaining_tickets=10, version=0)
    inv.reserve(5)
    assert inv.remaining_tickets == 5


def test_reserve_insufficient():
    inv = Inventory(event_id=1, remaining_tickets=3, version=0)
    with pytest.raises(InsufficientInventoryError):
        inv.reserve(5)


def test_release():
    inv = Inventory(event_id=1, remaining_tickets=5, version=0)
    inv.release(3)
    assert inv.remaining_tickets == 8
