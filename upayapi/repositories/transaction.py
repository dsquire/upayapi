"""Transaction repository for the uPay API."""

from typing import List, Optional
from datetime import date
from decimal import Decimal

from sqlalchemy.orm import Session

from upayapi.models.transaction import Transaction


class TransactionRepository:
    """Repository for transaction data operations.

    This class provides methods for creating, retrieving, and querying
    transaction data in the database.
    """

    def __init__(self, db: Session):
        """Initialize the repository with a database session.

        Args:
            db: Database session.
        """
        self.db = db

    def create(
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
        """
        transaction = Transaction(
            tpg_trans_id=tpg_trans_id,
            session_identifier=session_identifier,
            pmt_status=pmt_status,
            pmt_amt=pmt_amt,
            pmt_date=pmt_date,
            name_on_acct=name_on_acct,
        )
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_by_tpg_trans_id(self, tpg_trans_id: str) -> Optional[Transaction]:
        """Get a transaction by its tpg_trans_id.

        Args:
            tpg_trans_id: Transaction reference number assigned by Payment Gateway.

        Returns:
            The transaction if found, None otherwise.
        """
        return (
            self.db.query(Transaction)
            .filter(Transaction.tpg_trans_id == tpg_trans_id)
            .first()
        )

    def get_all(self) -> List[Transaction]:
        """Get all transactions.

        Returns:
            List of all transactions.
        """
        return self.db.query(Transaction).all()
