"""Configuration settings for the uPay API."""

from typing import List, Literal, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    Attributes:
        app_name: Name of the application.
        debug: Debug mode flag.
        environment: Current environment (dev, test, prod).
        database_url: Database connection string.
        posting_key: Authentication key for validating uPay requests.
        allowed_origins: List of allowed origins for CORS in production.
        connection_pool_size: Size of the database connection pool.
        connection_pool_max_overflow: Maximum overflow of the connection pool.
    """

    app_name: str = "uPay API"
    debug: bool = False
    environment: Literal["dev", "test", "prod"] = "dev"
    database_url: str = Field(
        default="sqlite:///./upay.db", description="Database connection string"
    )
    posting_key: str = Field(
        default="", description="Authentication key for validating uPay requests"
    )
    allowed_origins: List[str] = Field(
        default=["http://localhost:8000"],
        description="List of allowed origins for CORS in production",
    )
    connection_pool_size: int = Field(
        default=5, description="Size of the database connection pool"
    )
    connection_pool_max_overflow: int = Field(
        default=10, description="Maximum overflow of the connection pool"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    @field_validator("environment")
    def validate_environment(cls, v: str) -> str:
        """Validate the environment value.

        Args:
            v: The environment value.

        Returns:
            The validated environment value.

        Raises:
            ValueError: If the environment value is invalid.
        """
        if v not in ["dev", "test", "prod"]:
            raise ValueError("Environment must be one of: dev, test, prod")
        return v


def get_settings(env: Optional[Literal["dev", "test", "prod"]] = None) -> Settings:
    """Get settings for the specified environment.

    Args:
        env: The environment to get settings for. If None, uses the value from environment variables.

    Returns:
        Settings instance for the specified environment.
    """
    settings_instance = Settings()

    if env:
        settings_instance.environment = env

        # Configure debug mode based on environment
        if env in ["dev", "test"]:
            settings_instance.debug = True
        else:
            settings_instance.debug = False

    return settings_instance


# Create settings instance
settings = get_settings()
