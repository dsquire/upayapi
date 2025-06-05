"""Base repository for the uPay API."""

import logging
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from sqlalchemy import asc, desc, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from upayapi.database import Base

# Type variable for the model
T = TypeVar("T", bound=Base)

# Configure logger
logger = logging.getLogger("upayapi.repositories.base")


class BaseRepository(Generic[T]):
    """Base repository with common CRUD operations.

    This class provides common database operations for models.
    It should be subclassed by specific repositories.

    Attributes:
        db: Database session.
        model: SQLAlchemy model class.
        logger: Logger instance.
    """

    def __init__(self, db: Session, model: Type[T]):
        """Initialize the repository with a database session and model.

        Args:
            db: Database session.
            model: SQLAlchemy model class.
        """
        self.db = db
        self.model = model
        self.logger = logging.getLogger(
            f"upayapi.repositories.{model.__name__.lower()}"
        )

    def create(self, **kwargs) -> T:
        """Create a new record.

        Args:
            **kwargs: Fields for the new record.

        Returns:
            The created record.

        Raises:
            SQLAlchemyError: If there's an error creating the record.
        """
        try:
            record = self.model(**kwargs)
            self.db.add(record)
            self.db.commit()
            self.db.refresh(record)
            return record
        except SQLAlchemyError as e:
            self.db.rollback()
            self.logger.error(f"Error creating {self.model.__name__}: {str(e)}")
            raise

    def get_by_id(self, id: Any) -> Optional[T]:
        """Get a record by its ID.

        Args:
            id: Record ID.

        Returns:
            The record if found, None otherwise.

        Raises:
            SQLAlchemyError: If there's an error retrieving the record.
        """
        try:
            return self.db.query(self.model).filter(self.model.id == id).first()
        except SQLAlchemyError as e:
            self.logger.error(f"Error retrieving {self.model.__name__} by ID: {str(e)}")
            raise

    def get_all(
        self,
        skip: int = 0,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        **filters,
    ) -> List[T]:
        """Get all records with pagination, sorting, and filtering.

        Args:
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").
            **filters: Field filters.

        Returns:
            List of records.

        Raises:
            SQLAlchemyError: If there's an error retrieving the records.
            ValueError: If sort_order is invalid.
        """
        try:
            query = self.db.query(self.model)

            # Apply filters
            for field, value in filters.items():
                if hasattr(self.model, field):
                    query = query.filter(getattr(self.model, field) == value)

            # Apply sorting
            if sort_by and hasattr(self.model, sort_by):
                if sort_order.lower() == "asc":
                    query = query.order_by(asc(getattr(self.model, sort_by)))
                elif sort_order.lower() == "desc":
                    query = query.order_by(desc(getattr(self.model, sort_by)))
                else:
                    raise ValueError("sort_order must be 'asc' or 'desc'")

            # Apply pagination
            query = query.offset(skip)
            if limit is not None:
                query = query.limit(limit)

            return query.all()
        except SQLAlchemyError as e:
            self.logger.error(
                f"Error retrieving {self.model.__name__} records: {str(e)}"
            )
            raise

    def count(self, **filters) -> int:
        """Count records with filtering.

        Args:
            **filters: Field filters.

        Returns:
            Number of records.

        Raises:
            SQLAlchemyError: If there's an error counting the records.
        """
        try:
            query = self.db.query(func.count(self.model.id))

            # Apply filters
            for field, value in filters.items():
                if hasattr(self.model, field):
                    query = query.filter(getattr(self.model, field) == value)

            return query.scalar()
        except SQLAlchemyError as e:
            self.logger.error(f"Error counting {self.model.__name__} records: {str(e)}")
            raise

    def update(self, id: Any, **kwargs) -> Optional[T]:
        """Update a record by its ID.

        Args:
            id: Record ID.
            **kwargs: Fields to update.

        Returns:
            The updated record if found, None otherwise.

        Raises:
            SQLAlchemyError: If there's an error updating the record.
        """
        try:
            record = self.get_by_id(id)
            if record:
                for key, value in kwargs.items():
                    if hasattr(record, key):
                        setattr(record, key, value)
                self.db.commit()
                self.db.refresh(record)
            return record
        except SQLAlchemyError as e:
            self.db.rollback()
            self.logger.error(f"Error updating {self.model.__name__}: {str(e)}")
            raise

    def delete(self, id: Any) -> bool:
        """Delete a record by its ID.

        Args:
            id: Record ID.

        Returns:
            True if the record was deleted, False otherwise.

        Raises:
            SQLAlchemyError: If there's an error deleting the record.
        """
        try:
            record = self.get_by_id(id)
            if record:
                self.db.delete(record)
                self.db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.db.rollback()
            self.logger.error(f"Error deleting {self.model.__name__}: {str(e)}")
            raise

    def get_paginated_response(
        self,
        skip: int = 0,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        **filters,
    ) -> Dict[str, Any]:
        """Get paginated response with metadata.

        Args:
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").
            **filters: Field filters.

        Returns:
            Dictionary with items, total count, and pagination metadata.

        Raises:
            SQLAlchemyError: If there's an error retrieving the records.
        """
        items = self.get_all(skip, limit, sort_by, sort_order, **filters)
        total = self.count(**filters)

        return {
            "items": items,
            "total": total,
            "skip": skip,
            "limit": limit,
            "has_more": total > skip + len(items) if limit is not None else False,
        }
