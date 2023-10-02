from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from server.config import Settings

settings = Settings()
url = f"postgresql+psycopg2://{settings.DATABASE_DICT.get('username')}:{settings.DATABASE_DICT.get('password')}@{settings.DATABASE_DICT.get('host')}:{settings.DATABASE_DICT.get('port')}/{settings.DATABASE_DICT.get('database')}"
engine = create_engine(url)
DatabaseSession = sessionmaker(engine)