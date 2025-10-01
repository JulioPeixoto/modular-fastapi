from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = ""
    openai_api_key: str = ""
    log_level: str = ""
    origins: str = ""
    debug: str = ""
    environment: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
