# uPayAPI Usage Guide

## Table of Contents
- [Introduction](#introduction)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Routes](#routes)
  - [Adding New Routes](#adding-new-routes)
  - [Modifying Existing Routes](#modifying-existing-routes)
- [Services](#services)
  - [Transaction Service](#transaction-service)
  - [Creating New Services](#creating-new-services)
- [Repositories](#repositories)
  - [Transaction Repository](#transaction-repository)
  - [Creating New Repositories](#creating-new-repositories)
- [Models](#models)
  - [Transaction Model](#transaction-model)
  - [Creating New Models](#creating-new-models)
- [Configuration](#configuration)
- [Database](#database)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Deployment](#deployment)

## Introduction

The uPayAPI is a FastAPI-based application designed to process payment transactions from the TouchNet Marketplace uPay payment gateway. This guide provides instructions for developers maintaining and extending the API.

## Architecture Overview

The application follows a layered architecture with clear separation of concerns:

1. **Routes Layer**: Handles HTTP requests and responses
2. **Service Layer**: Contains business logic
3. **Repository Layer**: Manages data access
4. **Model Layer**: Defines data structures

The application uses the repository pattern to abstract database operations and dependency injection for better testability and maintainability.

## Project Structure

```
upayapi/
├── docs/                  # Documentation
├── migrations/            # Database migrations
├── tests/                 # Test files
├── upayapi/
│   ├── models/            # Data models
│   ├── repositories/      # Data access layer
│   ├── routes/            # API endpoints
│   ├── services/          # Business logic
│   ├── config.py          # Configuration settings
│   ├── database.py        # Database connection
│   └── main.py            # Application entry point
├── alembic.ini            # Alembic configuration
├── pyproject.toml         # Project dependencies
└── README.md              # Project overview
```

## Routes

Routes handle HTTP requests and responses. They are defined in the `upayapi/routes/` directory.

### Current Routes

The API currently has the following routes:

- `POST /upay/posting`: Processes uPay posting requests

### Adding New Routes

To add a new route:

1. Create a new route function in a new router file in the `upayapi/routes/` directory.
2. If creating a new router file, follow this pattern:

```python
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/your-prefix", tags=["your-tag"])

@router.post("/your-endpoint")
async def your_endpoint_function(
    # Parameters
    service: YourService = Depends()
):
    """Docstring describing the endpoint.
    
    Args:
        # Document parameters
        
    Returns:
        # Document return values
    """
    # Implementation
    return result
```

3. Register the router in `main.py` if it's a new router file:

```python
from upayapi.routes import your_router

app.include_router(your_router.router)
```

### Best Practices for Routes

1. **Use Dependency Injection**: Inject services using FastAPI's `Depends()`.
2. **Validate Input**: Use Pydantic models or FastAPI's validation for input data.
3. **Document Thoroughly**: Include detailed docstrings for all routes.
4. **Handle Errors**: Use try-except blocks and raise appropriate HTTPExceptions.
5. **Return Consistent Responses**: Maintain a consistent response format.

### Modifying Existing Routes

When modifying existing routes:

1. Maintain backward compatibility when possible.
2. Update documentation to reflect changes.
3. Add appropriate validation for new parameters.
4. Ensure error handling is comprehensive.
5. Update tests to cover the modified functionality.

Example of modifying the existing uPay posting route:

```python
@router.post("/posting")
async def upay_posting(
    posting_key: Annotated[str, Form()],
    tpg_trans_id: Annotated[str, Form()],
    session_identifier: Annotated[str, Form()],
    pmt_status: Annotated[str, Form()],
    pmt_amt: Annotated[str, Form()],
    pmt_date: Annotated[str, Form()],
    name_on_acct: Annotated[str, Form()],
    # Add new parameters here
    new_parameter: Annotated[str, Form()] = None,  # Optional parameter
    transaction_service: Annotated[TransactionService, Depends()],
) -> Dict[str, Any]:
    """Process a uPay posting request.
    
    Args:
        # Existing parameters...
        new_parameter: Description of new parameter.
        
    Returns:
        JSON response with processing result.
    """
    try:
        transaction_data = {
            # Existing fields...
            "new_parameter": new_parameter,
        }
        result = transaction_service.process_transaction(transaction_data)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing the transaction",
        )
```

## Services

Services contain the business logic of the application. They are defined in the `upayapi/services/` directory.

### Transaction Service

The `TransactionService` handles transaction processing logic, including:

- Validating posting keys
- Validating transaction data
- Processing transactions
- Interacting with the repository layer

### Creating New Services

To create a new service:

1. Create a new file in the `upayapi/services/` directory.
2. Define a class that encapsulates the business logic.
3. Use dependency injection to inject dependencies.

Example:

```python
from fastapi import Depends
from sqlalchemy.orm import Session

from upayapi.database import get_db
from upayapi.repositories.your_repository import YourRepository

class YourService:
    def __init__(self, db: Session = Depends(get_db)):
        """Initialize the service with a database session.
        
        Args:
            db: Database session.
        """
        self.repository = YourRepository(db)
        
    def your_method(self, data):
        """Method description.
        
        Args:
            data: Description of data.
            
        Returns:
            Description of return value.
        """
        # Implementation
        return result
```

### Best Practices for Services

1. **Single Responsibility**: Each service should have a single responsibility.
2. **Validation**: Validate input data before processing.
3. **Error Handling**: Use appropriate exceptions for error conditions.
4. **Documentation**: Include detailed docstrings for all methods.
5. **Testability**: Design services to be easily testable.

## Repositories

Repositories handle data access operations. They are defined in the `upayapi/repositories/` directory.

### Transaction Repository

The `TransactionRepository` handles database operations for transactions, including:

- Creating transactions
- Retrieving transactions by ID
- Retrieving all transactions

### Creating New Repositories

To create a new repository:

1. Create a new file in the `upayapi/repositories/` directory.
2. Define a class that encapsulates data access operations.

Example:

```python
from typing import List, Optional
from sqlalchemy.orm import Session

from upayapi.models.your_model import YourModel

class YourRepository:
    def __init__(self, db: Session):
        """Initialize the repository with a database session.
        
        Args:
            db: Database session.
        """
        self.db = db
        
    def create(self, **kwargs):
        """Create a new record.
        
        Args:
            **kwargs: Fields for the new record.
            
        Returns:
            The created record.
        """
        record = YourModel(**kwargs)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record
        
    def get_by_id(self, id: int) -> Optional[YourModel]:
        """Get a record by its ID.
        
        Args:
            id: Record ID.
            
        Returns:
            The record if found, None otherwise.
        """
        return self.db.query(YourModel).filter(YourModel.id == id).first()
        
    def get_all(self) -> List[YourModel]:
        """Get all records.
        
        Returns:
            List of all records.
        """
        return self.db.query(YourModel).all()
```

### Best Practices for Repositories

1. **Database Abstraction**: Repositories should abstract database operations.
2. **Query Encapsulation**: Encapsulate complex queries within repository methods.
3. **Transaction Management**: Handle database transactions appropriately.
4. **Error Handling**: Handle database errors gracefully.
5. **Documentation**: Include detailed docstrings for all methods.

## Models

Models define the data structures of the application. They are defined in the `upayapi/models/` directory.

### Transaction Model

The `Transaction` model represents a payment transaction with fields such as:

- `tpg_trans_id`: Transaction reference number
- `session_identifier`: Session identifier
- `pmt_status`: Payment status
- `pmt_amt`: Payment amount
- `pmt_date`: Payment date
- `name_on_acct`: Name on account

### Creating New Models

To create a new model:

1. Create a new file in the `upayapi/models/` directory.
2. Define a class that inherits from `Base`.

Example:

```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from upayapi.database import Base

class YourModel(Base):
    """Your model description.
    
    Attributes:
        id: Primary key.
        name: Name field.
        description: Description field.
        created_at: Timestamp when the record was created.
    """
    
    __tablename__ = "your_table"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self) -> str:
        """Return string representation of the model.
        
        Returns:
            String representation of the model.
        """
        return f"YourModel(id={self.id}, name={self.name})"
```

3. After creating a new model, create a migration using Alembic:

```bash
alembic revision --autogenerate -m "Add your_table"
alembic upgrade head
```

### Best Practices for Models

1. **Clear Attributes**: Define clear attributes with appropriate types.
2. **Documentation**: Include detailed docstrings for the model and its attributes.
3. **Relationships**: Define relationships between models when appropriate.
4. **Indexes**: Add indexes for frequently queried fields.
5. **String Representation**: Implement `__repr__` method for debugging.

## Configuration

The application configuration is defined in `upayapi/config.py`. It uses Pydantic's `BaseSettings` for environment variable loading and validation.

To add a new configuration setting:

1. Add the setting to the `Settings` class in `config.py`.
2. Provide a default value and description.

Example:

```python
class Settings(BaseSettings):
    # Existing settings...
    
    new_setting: str = Field(
        default="default_value", description="Description of the new setting"
    )
    
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )
```

3. Access the setting in your code using `settings.new_setting`.

## Database

The database configuration is defined in `upayapi/database.py`. It uses SQLAlchemy for database operations.

The application uses SQLite by default, but you can change the database by modifying the `database_url` setting in the configuration.

To work with the database:

1. Use the `get_db` function to get a database session.
2. Use the session for database operations.
3. Close the session when done.

Example:

```python
from upayapi.database import get_db

def your_function(db = Depends(get_db)):
    # Use db for database operations
    result = db.query(YourModel).all()
    return result
```

## Error Handling

The application uses FastAPI's exception handling for error handling. The main error handling is defined in `upayapi/main.py`.

To handle errors in your code:

1. Use try-except blocks to catch exceptions.
2. Raise appropriate HTTPExceptions with status codes and details.

Example:

```python
from fastapi import HTTPException, status

try:
    # Your code
    if error_condition:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error message",
        )
except Exception as e:
    # Log the error
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="An error occurred",
    )
```

## Testing

The application uses pytest for testing. Tests are defined in the `tests/` directory.

To write tests:

1. Create a new file in the `tests/` directory.
2. Define test functions that test specific functionality.
3. Use pytest fixtures for setup and teardown.

Example:

```python
import pytest
from fastapi.testclient import TestClient

from upayapi.main import app

client = TestClient(app)

def test_your_endpoint():
    response = client.post(
        "/your-endpoint",
        json={"key": "value"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": "expected_result"}
```

## Deployment

The application can be deployed using various methods, including:

1. **Docker**: Build a Docker image and deploy it to a container orchestration platform.
2. **Virtual Machine**: Deploy the application to a virtual machine.
3. **Serverless**: Deploy the application to a serverless platform.

For production deployment, consider:

1. Using a production-grade database (PostgreSQL, MySQL, etc.).
2. Setting up proper logging.
3. Configuring CORS for security.
4. Setting up authentication and authorization.
5. Using HTTPS for secure communication.