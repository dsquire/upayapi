"""Configuration settings for the uPay API."""

import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    Attributes:
        app_name: Name of the application.
        debug: Debug mode flag.
        database_url: Database connection string.
        posting_key: Authentication key for validating uPay requests.
    """

    app_name: str = "uPay API"
    debug: bool = False
    database_url: str = Field(
        default="sqlite:///./upay.db", 
        description="Database connection string"
    )
    posting_key: str = Field(
        default="", 
        description="Authentication key for validating uPay requests"
    )

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        case_sensitive=False
    )


# Create settings instance
settings = Settings()