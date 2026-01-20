import redis.asyncio as redis
from src.core.config import settings


class RedisClient:
    def __init__(self):
        self.client = redis.from_url(settings.redis_url)

    async def get(self, key: str) -> str | None:
        return await self.client.get(key)

    async def set(self, key: str, value: str, ex: int | None = None):
        await self.client.set(key, value, ex=ex)

    async def incr(self, key: str) -> int:
        return await self.client.incr(key)

    async def expire(self, key: str, seconds: int):
        await self.client.expire(key, seconds)
