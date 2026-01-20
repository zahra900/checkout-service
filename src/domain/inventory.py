from dataclasses import dataclass


@dataclass
class Inventory:
    event_id: int
    remaining_tickets: int
    version: int

    def reserve(self, quantity: int) -> None:
        if self.remaining_tickets < quantity:
            raise InsufficientInventoryError(f"Only {self.remaining_tickets} tickets available")
        self.remaining_tickets -= quantity

    def release(self, quantity: int) -> None:
        self.remaining_tickets += quantity


class InsufficientInventoryError(Exception):
    pass
