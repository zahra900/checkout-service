import aio_pika
from src.core.config import settings


class MessageBroker:
    """RabbitMQ abstraction."""

    async def connect(self):
        self.connection = await aio_pika.connect_robust(settings.rabbitmq_url)
        self.channel = await self.connection.channel()

    async def publish(self, exchange: str, routing_key: str, message: str):
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key,
        )

    async def close(self):
        await self.connection.close()
