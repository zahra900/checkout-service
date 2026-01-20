from src.infrastructure.cache.redis import RedisClient
from src.core.config import settings


class RateLimiter:
    def __init__(self, redis_client: RedisClient):
        self.redis = redis_client

    async def check_rate_limit(self, user_id: str) -> bool:
        """Sliding window rate limiting."""
        key = f"rate_limit:{user_id}"
        count = await self.redis.incr(key)
        
        if count == 1:
            await self.redis.expire(key, settings.rate_limit_window_seconds)
        
        return count <= settings.rate_limit_per_user
