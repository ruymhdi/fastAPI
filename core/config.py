from os import getenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"


class DbSettings(BaseModel):
	db_url: str = f"sqlite+aiosqlite:///{DB_PATH}"
	db_echo: bool = False


class Settings(BaseSettings):
	api_v1_prefix: str = "/api/v1"
	
	db: DbSettings = DbSettings()

settings = Settings()
