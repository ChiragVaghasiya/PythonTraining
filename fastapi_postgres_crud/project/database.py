import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Base)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://chirag:CHIRAG@localhost/FastAPIOdoo")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
