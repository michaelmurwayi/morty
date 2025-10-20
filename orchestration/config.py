# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    ENV: str = "production"
    DATABASE_URL: str = "sqlite+aiosqlite:///./agents.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    API_KEY: str = "changeme"
    WORKER_CONCURRENCY: int = 4
    TASK_FETCH_TIMEOUT: int = 5
    TASK_DEFAULT_TIMEOUT: int = 60
    MAX_RETRIES: int = 3
    LOG_LEVEL: str = "INFO"
    PROMETHEUS_METRICS: bool = True

    # ✅ new-style config for Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
