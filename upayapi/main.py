"""Main application module for the uPay API."""

import logging
from typing import Literal, Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from upayapi.config import settings
from upayapi.database import engine, Base
from upayapi.routes import upay

# Import models to ensure they are registered with Base.metadata

# Configure logger
logger = logging.getLogger("upayapi")


def create_app(env: Optional[Literal["dev", "test", "prod"]] = None) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        env: The environment to configure the app for. If None, uses the value from settings.

    Returns:
        Configured FastAPI application.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if settings.debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create FastAPI application
    app = FastAPI(
        title=settings.app_name,
        description="API for processing uPay Posting URL parameters",
        version="0.1.0",
    )

    # Configure the app based on environment
    environment = env or ("dev" if settings.debug else "prod")

    # Add CORS middleware with environment-specific settings
    if environment == "prod":
        # In production, use more restrictive CORS settings
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.allowed_origins,
            allow_credentials=True,
            allow_methods=["GET", "POST"],
            allow_headers=["*"],
        )
    else:
        # In development and testing, use permissive CORS settings
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Register exception handlers
    register_exception_handlers(app)

    # Register routes
    register_routes(app)

    # Register base endpoints
    register_base_endpoints(app)

    return app


def register_exception_handlers(app: FastAPI) -> None:
    """Register exception handlers for the application.

    Args:
        app: The FastAPI application.
    """

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """Global exception handler for unhandled exceptions.

        Args:
            request: The request that caused the exception.
            exc: The exception that was raised.

        Returns:
            JSON response with error details.
        """
        logger.error(f"Unhandled exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred"},
        )


def register_routes(app: FastAPI) -> None:
    """Register routes for the application.

    Args:
        app: The FastAPI application.
    """
    app.include_router(upay.router)


def register_base_endpoints(app: FastAPI) -> None:
    """Register base endpoints for the application.

    Args:
        app: The FastAPI application.
    """

    @app.get("/")
    async def root():
        """Root endpoint.

        Returns:
            Welcome message.
        """
        return {"message": "Welcome to the uPay API"}

    @app.get("/health")
    async def health():
        """Health check endpoint.

        Returns:
            Health status including database connection status.
        """
        from upayapi.database import check_database_connection

        # Check application status
        app_status = {"status": "healthy", "details": "Application is running"}

        # Check database connection
        db_status = check_database_connection()

        # Determine overall status
        overall_status = "healthy" if db_status["status"] == "healthy" else "unhealthy"

        return {
            "status": overall_status,
            "application": app_status,
            "database": db_status,
        }


# Create the application instance
app = create_app()
