import os
from dotenv import load_dotenv
from typing import Optional
from pathlib import Path

class Settings:
    _instance = None
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","gis")
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance
