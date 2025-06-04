"""Transaction service for the uPay API."""

from datetime import date, datetime
from decimal import Decimal
from typing import Dict, Any, Optional

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from upayapi.config import settings
from upayapi.database import get_db
from upayapi.repositories.transaction import TransactionRepository


class TransactionService:
    """Service for handling transaction operations.

    This class provides methods for processing uPay transactions,
    including validation and security checks.
    """

    def __init__(self, db: Session = Depends(get_db)):
        """Initialize the service with a database session.

        Args:
            db: Database session.
        """
        self.repository = TransactionRepository(db)

    def validate_posting_key(self, posting_key: str) -> bool:
        """Validate the posting key to ensure request is authorized.

        Args:
            posting_key: Authentication key for validating requests.

        Returns:
            True if the posting key is valid, False otherwise.
        """
        return posting_key == settings.posting_key

    def process_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a uPay transaction.

        Args:
            transaction_data: Dictionary containing transaction data from uPay.

        Returns:
            Dictionary with processing result.

        Raises:
            HTTPException: If the posting key is invalid or required parameters are missing.
        """
        # Validate posting key
        posting_key = transaction_data.get("posting_key")
        if not posting_key or not self.validate_posting_key(posting_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid posting key",
            )

        # Validate required parameters
        required_params = [
            "tpg_trans_id",
            "session_identifier",
            "pmt_status",
            "pmt_amt",
            "pmt_date",
            "name_on_acct",
        ]
        for param in required_params:
            if param not in transaction_data or not transaction_data[param]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Missing required parameter: {param}",
                )

        # Validate payment status
        pmt_status = transaction_data["pmt_status"]
        if pmt_status not in ["success", "cancelled"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid payment status. Must be 'success' or 'cancelled'",
            )

        # Validate payment amount
        try:
            pmt_amt = Decimal(transaction_data["pmt_amt"])
            if pmt_amt <= 0 or pmt_amt > Decimal("99999.99"):
                raise ValueError()
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid payment amount. Must be a positive number less than or equal to 99,999.99",
            )

        # Validate payment date
        try:
            pmt_date = datetime.strptime(
                transaction_data["pmt_date"], "%m/%d/%Y"
            ).date()
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid payment date. Format must be mm/dd/yyyy",
            )

        # Check if transaction already exists
        existing_transaction = self.repository.get_by_tpg_trans_id(
            transaction_data["tpg_trans_id"]
        )
        if existing_transaction:
            return {
                "success": True,
                "message": "Transaction already processed",
                "transaction_id": existing_transaction.id,
            }

        # Create transaction
        transaction = self.repository.create(
            tpg_trans_id=transaction_data["tpg_trans_id"],
            session_identifier=transaction_data["session_identifier"],
            pmt_status=pmt_status,
            pmt_amt=pmt_amt,
            pmt_date=pmt_date,
            name_on_acct=transaction_data["name_on_acct"],
        )

        return {
            "success": True,
            "message": "Transaction processed successfully",
            "transaction_id": transaction.id,
        }
