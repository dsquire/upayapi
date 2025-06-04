"""Transaction model for the uPay API."""


from sqlalchemy import Column, Integer, String, Date, Numeric, DateTime
from sqlalchemy.sql import func

from upayapi.database import Base


class Transaction(Base):
    """Transaction model for storing uPay transaction data.

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

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    tpg_trans_id = Column(String, unique=True, index=True, nullable=False)
    session_identifier = Column(String, index=True, nullable=False)
    pmt_status = Column(String, nullable=False)
    pmt_amt = Column(Numeric(precision=10, scale=2), nullable=False)
    pmt_date = Column(Date, nullable=False)
    name_on_acct = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        """Return string representation of the transaction.

        Returns:
            String representation of the transaction.
        """
        return (
            f"Transaction(id={self.id}, "
            f"tpg_trans_id={self.tpg_trans_id}, "
            f"session_identifier={self.session_identifier}, "
            f"pmt_status={self.pmt_status}, "
            f"pmt_amt={self.pmt_amt}, "
            f"pmt_date={self.pmt_date}, "
            f"name_on_acct={self.name_on_acct})"
        )
