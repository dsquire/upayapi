"""Database configuration for the uPay API."""

import logging
from contextlib import contextmanager
from typing import Any, Dict, Generator

from sqlalchemy import create_engine, event, exc, text
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.pool import QueuePool

from upayapi.config import settings

# Configure logger
logger = logging.getLogger("upayapi.database")


def get_engine_args() -> Dict[str, Any]:
    """Get SQLAlchemy engine arguments based on database type.

    Returns:
        Dictionary of engine arguments.
    """
    # Default engine arguments
    engine_args = {
        "echo": settings.debug,
    }

    # Add connection pooling configuration for non-SQLite databases in production
    if (
        not settings.database_url.startswith("sqlite")
        and settings.environment == "prod"
    ):
        engine_args.update(
            {
                "poolclass": QueuePool,
                "pool_size": settings.connection_pool_size,
                "max_overflow": settings.connection_pool_max_overflow,
                "pool_timeout": 30,  # 30 seconds
                "pool_recycle": 1800,  # 30 minutes
                "pool_pre_ping": True,
            }
        )

    # Add connect_args based on database type
    if settings.database_url.startswith("sqlite"):
        engine_args["connect_args"] = {"check_same_thread": False}

    return engine_args


# Create SQLAlchemy engine with appropriate configuration
try:
    engine_args = get_engine_args()
    engine = create_engine(settings.database_url, **engine_args)
    logger.info(f"Database engine created for {settings.database_url}")
except Exception as e:
    logger.error(f"Failed to create database engine: {str(e)}")
    raise


# Add event listeners for connection pool
@event.listens_for(engine, "connect")
def connect(dbapi_connection, connection_record):
    """Log when a connection is created."""
    logger.debug("Database connection established")


@event.listens_for(engine, "checkout")
def checkout(dbapi_connection, connection_record, connection_proxy):
    """Verify that the connection is still alive on checkout."""
    try:
        # For PostgreSQL
        if hasattr(dbapi_connection, "ping"):
            dbapi_connection.ping(reconnect=True)
        # For SQLite and others
        else:
            cursor = dbapi_connection.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
    except Exception:
        # Disconnect the invalid connection
        connection_record.invalidate()
        logger.warning("Invalid connection detected and invalidated")
        raise


# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Get database session.

    Yields:
        Database session.

    Raises:
        Exception: If there's an error with the database connection.
    """
    db = SessionLocal()
    try:
        yield db
    except exc.SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error: {str(e)}")
        raise
    finally:
        db.close()


@contextmanager
def db_transaction() -> Generator[Session, None, None]:
    """Context manager for database transactions.

    Yields:
        Database session.

    Raises:
        Exception: If there's an error with the database transaction.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Transaction error: {str(e)}")
        raise
    finally:
        db.close()


def check_database_connection() -> Dict[str, Any]:
    """Check the database connection health.

    Returns:
        Dictionary with database health status.

    Raises:
        Exception: If there's an error with the database connection.
    """
    try:
        with db_transaction() as db:
            # Execute a simple query to check the connection
            db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": settings.database_url.split("://")[0],
            "details": "Database connection is healthy",
        }
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "database": settings.database_url.split("://")[0],
            "details": str(e),
        }
