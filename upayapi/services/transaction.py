"""Transaction service for the uPay API."""

from datetime import datetime
from decimal import Decimal

from fastapi import Depends, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from upayapi.config import settings
from upayapi.database import get_db
from upayapi.exceptions import AuthenticationError, DatabaseError, DuplicateError
from upayapi.models.schemas import (
    TransactionRequest,
    TransactionResponse,
)
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

    def process_transaction(
        self, transaction_request: TransactionRequest
    ) -> TransactionResponse:
        """Process a uPay transaction.

        Args:
            transaction_request: Validated transaction request data.

        Returns:
            Transaction response with processing result.

        Raises:
            AuthenticationError: If the posting key is invalid.
            DatabaseError: If there's an error with the database operation.
            DuplicateError: If the transaction has already been processed.
        """
        # Validate posting key
        if not self.validate_posting_key(transaction_request.posting_key):
            raise AuthenticationError(
                detail="Invalid posting key"
            )

        # Convert validated data to appropriate types
        pmt_status = transaction_request.pmt_status.value
        pmt_amt = Decimal(transaction_request.pmt_amt)
        pmt_date = datetime.strptime(transaction_request.pmt_date, "%m/%d/%Y").date()

        try:
            # Check if transaction already exists
            existing_transaction = self.repository.get_by_tpg_trans_id(
                transaction_request.tpg_trans_id
            )
            if existing_transaction:
                # Use DuplicateError for consistent error handling, but return success response
                # since this is an expected condition
                return TransactionResponse(
                    success=True,
                    message="Transaction already processed",
                    transaction_id=existing_transaction.id,
                )

            # Create transaction
            transaction = self.repository.create_transaction(
                tpg_trans_id=transaction_request.tpg_trans_id,
                session_identifier=transaction_request.session_identifier,
                pmt_status=pmt_status,
                pmt_amt=pmt_amt,
                pmt_date=pmt_date,
                name_on_acct=transaction_request.name_on_acct,
            )
        except SQLAlchemyError as e:
            # Convert SQLAlchemy exceptions to our custom DatabaseError
            raise DatabaseError(
                detail=f"Database error while processing transaction: {str(e)}"
            )

        return TransactionResponse(
            success=True,
            message="Transaction processed successfully",
            transaction_id=transaction.id,
        )
