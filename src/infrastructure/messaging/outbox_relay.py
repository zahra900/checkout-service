import asyncio

from src.infrastructure.messaging.broker import MessageBroker


class OutboxRelay:
    """Polls outbox table and publishes to message broker."""

    def __init__(self, broker: MessageBroker):
        self.broker = broker

    async def run(self):
        """Poll NEW messages, publish, mark SENT."""
        while True:
            # TODO: Fetch NEW outbox messages
            # TODO: Publish to broker
            # TODO: Mark as SENT
            await asyncio.sleep(1)


if __name__ == "__main__":
    # relay = OutboxRelay(broker=MessageBroker())
    # asyncio.run(relay.run())
    pass
