"""Exception handling for the uPay API.

This module provides custom exception classes and error handling utilities
for the uPay API. It includes a centralized error handler and structured
error response format.
"""

import logging
import uuid
from typing import Any, Dict, Optional, Type, Union

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError

# Configure logger
logger = logging.getLogger("upayapi.exceptions")


class ErrorDetail(BaseModel):
    """Model for structured error response details.

    Attributes:
        message: Human-readable error message.
        code: Error code for programmatic handling.
        params: Additional parameters related to the error.
    """

    message: str
    code: str = "error"
    params: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    """Model for structured error responses.

    Attributes:
        detail: Error details.
        request_id: Unique identifier for the request for traceability.
        status_code: HTTP status code.
    """

    detail: Union[str, ErrorDetail]
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    status_code: int


# Base exception class for all API exceptions
class APIException(Exception):
    """Base exception class for all API exceptions.

    Attributes:
        detail: Error details.
        status_code: HTTP status code.
    """

    def __init__(
        self,
        detail: Union[str, ErrorDetail],
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        """Initialize the exception.

        Args:
            detail: Error details.
            status_code: HTTP status code.
        """
        self.detail = detail
        self.status_code = status_code
        super().__init__(str(detail))


# Specific exception types
class AuthenticationError(APIException):
    """Exception raised when authentication fails."""

    def __init__(self, detail: Union[str, ErrorDetail] = "Authentication failed"):
        """Initialize the exception.

        Args:
            detail: Error details.
        """
        super().__init__(detail, status.HTTP_401_UNAUTHORIZED)


class ValidationError(APIException):
    """Exception raised when validation fails."""

    def __init__(self, detail: Union[str, ErrorDetail] = "Validation failed"):
        """Initialize the exception.

        Args:
            detail: Error details.
        """
        super().__init__(detail, status.HTTP_422_UNPROCESSABLE_ENTITY)


class DatabaseError(APIException):
    """Exception raised when a database operation fails."""

    def __init__(self, detail: Union[str, ErrorDetail] = "Database operation failed"):
        """Initialize the exception.

        Args:
            detail: Error details.
        """
        super().__init__(detail, status.HTTP_500_INTERNAL_SERVER_ERROR)


class NotFoundError(APIException):
    """Exception raised when a resource is not found."""

    def __init__(self, detail: Union[str, ErrorDetail] = "Resource not found"):
        """Initialize the exception.

        Args:
            detail: Error details.
        """
        super().__init__(detail, status.HTTP_404_NOT_FOUND)


class DuplicateError(APIException):
    """Exception raised when a duplicate resource is detected."""

    def __init__(self, detail: Union[str, ErrorDetail] = "Resource already exists"):
        """Initialize the exception.

        Args:
            detail: Error details.
        """
        super().__init__(detail, status.HTTP_409_CONFLICT)


def register_exception_handlers(app: FastAPI) -> None:
    """Register exception handlers for the application.

    Args:
        app: The FastAPI application.
    """

    @app.middleware("http")
    async def add_request_id(request: Request, call_next):
        """Add a request ID to the request state for traceability.

        Args:
            request: The incoming request.
            call_next: The next middleware or route handler.

        Returns:
            The response from the next middleware or route handler.
        """
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

    @app.exception_handler(APIException)
    async def api_exception_handler(request: Request, exc: APIException):
        """Handle API exceptions.

        Args:
            request: The request that caused the exception.
            exc: The exception that was raised.

        Returns:
            JSON response with error details.
        """
        logger.error(
            f"API Exception: {exc.detail}",
            extra={"request_id": getattr(request.state, "request_id", "unknown")},
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                detail=exc.detail,
                request_id=getattr(request.state, "request_id", str(uuid.uuid4())),
                status_code=exc.status_code,
            ).model_dump(),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle request validation errors.

        Args:
            request: The request that caused the exception.
            exc: The exception that was raised.

        Returns:
            JSON response with validation error details.
        """
        logger.error(
            f"Validation Error: {exc.errors()}",
            extra={"request_id": getattr(request.state, "request_id", "unknown")},
        )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ErrorResponse(
                detail=ErrorDetail(
                    message="Validation error",
                    code="validation_error",
                    params={"errors": exc.errors()},
                ),
                request_id=getattr(request.state, "request_id", str(uuid.uuid4())),
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            ).model_dump(),
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        """Handle SQLAlchemy errors.

        Args:
            request: The request that caused the exception.
            exc: The exception that was raised.

        Returns:
            JSON response with database error details.
        """
        logger.error(
            f"Database Error: {str(exc)}",
            extra={"request_id": getattr(request.state, "request_id", "unknown")},
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ErrorResponse(
                detail=ErrorDetail(
                    message="Database operation failed",
                    code="database_error",
                ),
                request_id=getattr(request.state, "request_id", str(uuid.uuid4())),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        """Handle unhandled exceptions.

        Args:
            request: The request that caused the exception.
            exc: The exception that was raised.

        Returns:
            JSON response with error details.
        """
        logger.error(
            f"Unhandled Exception: {str(exc)}",
            extra={"request_id": getattr(request.state, "request_id", "unknown")},
            exc_info=True,
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ErrorResponse(
                detail=ErrorDetail(
                    message="An internal server error occurred",
                    code="internal_server_error",
                ),
                request_id=getattr(request.state, "request_id", str(uuid.uuid4())),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ).model_dump(),
        )