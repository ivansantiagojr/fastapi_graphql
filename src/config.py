from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    HOST: str
    PORT: int

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
