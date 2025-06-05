"""Transaction repository for the uPay API."""

from typing import Any, Dict, Optional
from datetime import date
from decimal import Decimal

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from upayapi.models.transaction import Transaction
from upayapi.repositories.base import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    """Repository for transaction data operations.

    This class provides methods for creating, retrieving, and querying
    transaction data in the database.
    """

    def __init__(self, db: Session):
        """Initialize the repository with a database session.

        Args:
            db: Database session.
        """
        super().__init__(db, Transaction)

    def create_transaction(
        self,
        tpg_trans_id: str,
        session_identifier: str,
        pmt_status: str,
        pmt_amt: Decimal,
        pmt_date: date,
        name_on_acct: str,
    ) -> Transaction:
        """Create a new transaction record.

        Args:
            tpg_trans_id: Transaction reference number assigned by Payment Gateway.
            session_identifier: Unique session identifier code.
            pmt_status: Transaction status ('success' or 'cancelled').
            pmt_amt: Transaction amount.
            pmt_date: Transaction processing date.
            name_on_acct: Name on payment account.

        Returns:
            The created transaction.

        Raises:
            SQLAlchemyError: If there's an error creating the transaction.
        """
        return self.create(
            tpg_trans_id=tpg_trans_id,
            session_identifier=session_identifier,
            pmt_status=pmt_status,
            pmt_amt=pmt_amt,
            pmt_date=pmt_date,
            name_on_acct=name_on_acct,
        )

    def get_by_tpg_trans_id(self, tpg_trans_id: str) -> Optional[Transaction]:
        """Get a transaction by its tpg_trans_id.

        Args:
            tpg_trans_id: Transaction reference number assigned by Payment Gateway.

        Returns:
            The transaction if found, None otherwise.

        Raises:
            SQLAlchemyError: If there's an error retrieving the transaction.
        """
        try:
            return (
                self.db.query(Transaction)
                .filter(Transaction.tpg_trans_id == tpg_trans_id)
                .first()
            )
        except SQLAlchemyError as e:
            self.logger.error(f"Error retrieving transaction by tpg_trans_id: {str(e)}")
            raise

    def get_transactions(
        self,
        skip: int = 0,
        limit: Optional[int] = None,
        sort_by: Optional[str] = "pmt_date",
        sort_order: Optional[str] = "desc",
        pmt_status: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> Dict[str, Any]:
        """Get transactions with pagination, sorting, and filtering.

        Args:
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            sort_by: Field to sort by.
            sort_order: Sort order ("asc" or "desc").
            pmt_status: Filter by payment status.
            start_date: Filter by payment date (start).
            end_date: Filter by payment date (end).

        Returns:
            Dictionary with transactions, total count, and pagination metadata.

        Raises:
            SQLAlchemyError: If there's an error retrieving the transactions.
        """
        try:
            query = self.db.query(Transaction)

            # Apply filters
            if pmt_status:
                query = query.filter(Transaction.pmt_status == pmt_status)

            if start_date:
                query = query.filter(Transaction.pmt_date >= start_date)

            if end_date:
                query = query.filter(Transaction.pmt_date <= end_date)

            # Get total count
            total = query.count()

            # Apply sorting
            if sort_by and hasattr(Transaction, sort_by):
                if sort_order.lower() == "asc":
                    query = query.order_by(getattr(Transaction, sort_by).asc())
                elif sort_order.lower() == "desc":
                    query = query.order_by(getattr(Transaction, sort_by).desc())
                else:
                    raise ValueError("sort_order must be 'asc' or 'desc'")

            # Apply pagination
            query = query.offset(skip)
            if limit is not None:
                query = query.limit(limit)

            items = query.all()

            return {
                "items": items,
                "total": total,
                "skip": skip,
                "limit": limit,
                "has_more": total > skip + len(items) if limit is not None else False,
            }
        except SQLAlchemyError as e:
            self.logger.error(f"Error retrieving transactions: {str(e)}")
            raise
