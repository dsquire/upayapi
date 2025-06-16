"""uPay posting endpoint routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, Form

from upayapi.exceptions import ValidationError
from upayapi.models.schemas import (
    TransactionRequest,
    TransactionResponse,
)
from upayapi.services.transaction import TransactionService

router = APIRouter(prefix="/upay", tags=["upay"])


@router.post("/posting")
async def upay_posting(
    posting_key: Annotated[str, Form()],
    tpg_trans_id: Annotated[str, Form()],
    session_identifier: Annotated[str, Form()],
    pmt_status: Annotated[str, Form()],
    pmt_amt: Annotated[str, Form()],
    pmt_date: Annotated[str, Form()],
    name_on_acct: Annotated[str, Form()],
    transaction_service: Annotated[TransactionService, Depends()],
) -> TransactionResponse:
    """Process a uPay posting request.

    This endpoint receives transaction data from the TouchNet Marketplace uPay
    payment gateway and processes it.

    Args:
        posting_key: Authentication key for validating requests.
        tpg_trans_id: Transaction reference number assigned by Payment Gateway.
        session_identifier: Unique session identifier code.
        pmt_status: Transaction status ('success' or 'cancelled').
        pmt_amt: Transaction amount (max: $99,999.99).
        pmt_date: Transaction processing date (format: mm/dd/yyyy).
        name_on_acct: Name on payment account.
        transaction_service: Service for processing transactions.

    Returns:
        JSON response with processing result.
    """
    try:
        # Create and validate the transaction request
        transaction_request = TransactionRequest(
            posting_key=posting_key,
            tpg_trans_id=tpg_trans_id,
            session_identifier=session_identifier,
            pmt_status=pmt_status,
            pmt_amt=pmt_amt,
            pmt_date=pmt_date,
            name_on_acct=name_on_acct,
        )
        result = transaction_service.process_transaction(transaction_request)
        return result
    except ValidationError:
        # Re-raise validation errors
        raise
    except Exception as e:
        # Log the error and convert to ValidationError
        # Our global exception handlers will take care of other specific exceptions
        raise ValidationError(
            detail=f"Error validating transaction data: {str(e)}"
        )
