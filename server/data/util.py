from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from server.config import Settings

settings = Settings()
engine = create_engine(settings.DATABASE_URL)
DatabaseSession = sessionmaker(engine)