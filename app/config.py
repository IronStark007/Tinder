from ast import Str
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tinder API"
    version: str
    url_prefix: str
    api_key: str
    auth_domain: str
    database_url: str
    project_id: str
    storage_bucket: str
    messaging_sender_id: str
    app_id: str
    measurement_id: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_config():
    return Settings()
