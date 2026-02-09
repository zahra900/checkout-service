from src.infrastructure.cache.redis import RedisClient


class IdempotencyCache:
    """Optional fast-path cache for idempotency (non-authoritative)."""

    def __init__(self, redis_client: RedisClient):
        self.redis = redis_client

    async def get_cached_response(self, idempotency_key: str) -> str | None:
        return await self.redis.get(f"idempotency:{idempotency_key}")

    async def cache_response(
        self, idempotency_key: str, response: str, ttl: int = 3600
    ):
        await self.redis.set(f"idempotency:{idempotency_key}", response, ex=ttl)
