from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "postgresql+asyncpg://chirag:CHIRAG@localhost/pos_app"

engine = create_async_engine(database_url, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
