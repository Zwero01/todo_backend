from sqlalchemy import create_engine
from src.core.settings import settings


# Replace USERNAME, PASSWORD, HOST, PORT, and DBNAME with your credentials
engine = create_engine(settings.DATABASE_URI)
