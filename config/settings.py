# ------------------------------------------------------------------------------
# settings.py
# ------------------------------------------------------------------------------
# This module manages runtime configuration using Pydantic's BaseSettings class.
#
# Why this exists:
# - Centralizes all application settings in one place.
# - Loads environment variables from .env file or system environment.
# - Prevents hardcoding secrets or environment-specific logic.
# - Ensures type safety and early validation (fail-fast behavior).
#
# This makes your application portable, secure, and production-friendly.
#
# Example usage:
#   from config.settings import get_settings
#   settings = get_settings()
#   api_key = settings.OPENAI_API_KEY
# ------------------------------------------------------------------------------

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # --------------------------------------------------------------------------
    # External Service Keys (load securely via environment)
    # --------------------------------------------------------------------------
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    SERPAPI_API_KEY: str = Field(default="", env="SERPAPI_API_KEY")

    # --------------------------------------------------------------------------
    # Application Environment
    # Helps control behavior in dev vs staging vs prod
    # --------------------------------------------------------------------------
    ENV: str = Field(default="dev", env="ENV")  # Options: "dev", "staging", "prod"

    # --------------------------------------------------------------------------
    # Feature Toggles (e.g. switch between agent modes)
    # --------------------------------------------------------------------------
    USE_LANGCHAIN: bool = Field(default=False, env="USE_LANGCHAIN")

    # --------------------------------------------------------------------------
    # Advanced Config (Optional placeholders for future config flags)
    # --------------------------------------------------------------------------
    DEBUG_MODE: bool = Field(default=True, env="DEBUG_MODE")

    class Config:
        env_file = ".env"         # Default location for local config
        case_sensitive = True     # Make ENV vars case-sensitive

def get_settings():
    """
    Returns a singleton-like settings object that can be imported anywhere.
    """
    return Settings()
