"""Database configuration for the uPay API."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from upayapi.config import settings

# Create SQLAlchemy engine
engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_db():
    """Get database session.

    Yields:
        Database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
