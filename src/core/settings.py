import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    log_level: str = os.getenv("LOG_LEVEL")
    origins: str = os.getenv("ORIGINS")
    debug: str = os.getenv("DEBUG")
    environment: str = os.getenv("ENVIRONMENT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()