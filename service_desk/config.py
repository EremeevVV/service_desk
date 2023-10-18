from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    hostname: str
    database: str
    username: str
    password: str
    port: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path('../.env'), env_file_encoding='utf-8', extra='ignore',
                                      env_nested_delimiter='__')
    app_name: str
    db: DBSettings
