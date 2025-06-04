"""uPay posting endpoint routes."""

from typing import Annotated, Dict, Any

from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.responses import JSONResponse

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
) -> Dict[str, Any]:
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
        transaction_data = {
            "posting_key": posting_key,
            "tpg_trans_id": tpg_trans_id,
            "session_identifier": session_identifier,
            "pmt_status": pmt_status,
            "pmt_amt": pmt_amt,
            "pmt_date": pmt_date,
            "name_on_acct": name_on_acct,
        }
        result = transaction_service.process_transaction(transaction_data)
        return result
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log the error (in a production environment)
        # logger.error(f"Error processing uPay posting: {str(e)}")

        # Return a generic error response
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing the transaction",
        )
