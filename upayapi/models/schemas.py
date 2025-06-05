"""Pydantic models for request and response validation."""

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, field_validator, ConfigDict


class PaymentStatus(str, Enum):
    """Enum for payment status values."""

    SUCCESS = "success"
    CANCELLED = "cancelled"


class TransactionRequest(BaseModel):
    """Request model for transaction processing.

    Attributes:
        posting_key: Authentication key for validating requests.
        tpg_trans_id: Transaction reference number assigned by Payment Gateway.
        session_identifier: Unique session identifier code.
        pmt_status: Transaction status ('success' or 'cancelled').
        pmt_amt: Transaction amount (max: $99,999.99).
        pmt_date: Transaction processing date (format: mm/dd/yyyy).
        name_on_acct: Name on payment account.
    """

    posting_key: str
    tpg_trans_id: str
    session_identifier: str
    pmt_status: PaymentStatus
    pmt_amt: str
    pmt_date: str
    name_on_acct: str

    @field_validator("pmt_amt", mode="before")
    def validate_payment_amount(cls, v: str) -> str:
        """Validate payment amount.

        Args:
            v: Payment amount as string.

        Returns:
            Validated payment amount string.

        Raises:
            ValueError: If payment amount is invalid.
        """
        try:
            amount = Decimal(v)
            if amount <= 0 or amount > Decimal("99999.99"):
                raise ValueError()
        except (ValueError, TypeError, ArithmeticError):
            raise ValueError(
                "Invalid payment amount. Must be a positive number less than or equal to 99,999.99"
            )
        return v

    @field_validator("pmt_date", mode="before")
    def validate_payment_date(cls, v: str) -> str:
        """Validate payment date format.

        Args:
            v: Payment date as string in mm/dd/yyyy format.

        Returns:
            Validated payment date string.

        Raises:
            ValueError: If payment date format is invalid.
        """
        try:
            datetime.strptime(v, "%m/%d/%Y").date()
        except ValueError:
            raise ValueError("Invalid payment date. Format must be mm/dd/yyyy")
        return v


class TransactionResponse(BaseModel):
    """Response model for transaction processing.

    Attributes:
        success: Whether the transaction was processed successfully.
        message: Message describing the result of the transaction processing.
        transaction_id: ID of the processed transaction.
    """

    success: bool
    message: str
    transaction_id: int


class TransactionModel(BaseModel):
    """Model representing a transaction.

    Attributes:
        id: Primary key.
        tpg_trans_id: Transaction reference number assigned by Payment Gateway.
        session_identifier: Unique session identifier code.
        pmt_status: Transaction status ('success' or 'cancelled').
        pmt_amt: Transaction amount.
        pmt_date: Transaction processing date.
        name_on_acct: Name on payment account.
        created_at: Timestamp when the record was created.
    """

    id: int
    tpg_trans_id: str
    session_identifier: str
    pmt_status: PaymentStatus
    pmt_amt: Decimal
    pmt_date: date
    name_on_acct: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
    """Pydantic model configuration."""
