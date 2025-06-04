"""Main application module for the uPay API."""

import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from upayapi.config import settings
from upayapi.database import engine, Base
from upayapi.routes import upay

# Import models to ensure they are registered with Base.metadata

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.debug else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("upayapi")

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="API for processing uPay Posting URL parameters",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upay.router)


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
        Health status.
    """
    return {"status": "healthy"}
