import os
from dotenv import load_dotenv
from typing import Optional
from pathlib import Path

class Settings:
    _instance = None
    DATABASE_DICT = {
        "host":  os.getenv("POSTGRES_SERVER","localhost"),
        "port": os.getenv("POSTGRES_PORT",5432),
        "database": os.getenv("POSTGRES_DB","gis"),
        "username": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "drivername": 'postgresql',
        'query': {'charset': 'utf8'}
    }

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(Settings, cls).__new__(cls)
            print(f"Database Connection: {cls.DATABASE_DICT}")
        return cls._instance
