"""Tests for the uPay API endpoints."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from upayapi.database import Base, get_db
from upayapi.main import app
from upayapi.config import settings


# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency
def override_get_db():
    """Get test database session.

    Yields:
        Database session.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Create test client
client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """Create test database tables before each test and drop them after.

    Yields:
        None
    """
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables
    Base.metadata.drop_all(bind=engine)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the uPay API"}


def test_health():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_upay_posting_missing_params():
    """Test the upay posting endpoint with missing parameters."""
    response = client.post("/upay/posting")
    assert response.status_code == 422  # Unprocessable Entity


def test_upay_posting_invalid_key(test_db, monkeypatch):
    """Test the upay posting endpoint with an invalid posting key."""
    # Set a known posting key for testing
    monkeypatch.setattr(settings, "posting_key", "test_key")

    # Send request with invalid key
    response = client.post(
        "/upay/posting",
        data={
            "posting_key": "invalid_key",
            "tpg_trans_id": "12345",
            "session_identifier": "session123",
            "pmt_status": "success",
            "pmt_amt": "100.00",
            "pmt_date": "01/01/2025",
            "name_on_acct": "John Doe",
        },
    )
    assert response.status_code == 401
    assert "Invalid posting key" in response.json()["detail"]


def test_upay_posting_success(test_db, monkeypatch):
    """Test the upay posting endpoint with valid parameters."""
    # Set a known posting key for testing
    monkeypatch.setattr(settings, "posting_key", "test_key")

    # Send request with valid data
    response = client.post(
        "/upay/posting",
        data={
            "posting_key": "test_key",
            "tpg_trans_id": "12345",
            "session_identifier": "session123",
            "pmt_status": "success",
            "pmt_amt": "100.00",
            "pmt_date": "01/01/2025",
            "name_on_acct": "John Doe",
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "transaction_id" in response.json()

    # Test duplicate transaction
    response = client.post(
        "/upay/posting",
        data={
            "posting_key": "test_key",
            "tpg_trans_id": "12345",  # Same transaction ID
            "session_identifier": "session123",
            "pmt_status": "success",
            "pmt_amt": "100.00",
            "pmt_date": "01/01/2025",
            "name_on_acct": "John Doe",
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Transaction already processed" in response.json()["message"]
