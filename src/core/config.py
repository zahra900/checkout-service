from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    rabbitmq_url: str
    
    jwt_public_key_url: str
    jwt_algorithm: str = "RS256"
    jwt_audience: str
    
    order_expiration_seconds: int = 900
    rate_limit_per_user: int = 10
    rate_limit_window_seconds: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
