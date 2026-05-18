"""
Database configuration.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/identity_core"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """
    SQLAlchemy declarative base.
    """
