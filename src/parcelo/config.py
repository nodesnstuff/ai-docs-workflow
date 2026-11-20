"""Runtime configuration for the Parcelo client.

Every setting is read from an environment variable and falls back to the
default defined in this module.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_API_URL = "https://api.parcelo.example/v1"
DEFAULT_TIMEOUT_SECONDS = 10
DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100
DEFAULT_MAX_RETRIES = 3
MAX_RETRIES_LIMIT = 10


@dataclass(frozen=True)
class Settings:
    """Resolved client settings."""

    api_url: str
    api_key: str | None
    timeout_seconds: int
    page_size: int
    max_retries: int


def load_settings(env: dict[str, str] | None = None) -> Settings:
    """Build Settings from environment variables.

    PARCELO_API_URL   Base URL of the Parcelo API.
    PARCELO_API_KEY   API key sent in the X-Parcelo-Key header.
    PARCELO_TIMEOUT   Request timeout in seconds.
    PARCELO_PAGE_SIZE Number of parcels returned per page (1-100).
    PARCELO_MAX_RETRIES Times a failed request is retried (0-10). 0 disables retries.
    """
    env = dict(os.environ) if env is None else env

    page_size = int(env.get("PARCELO_PAGE_SIZE", DEFAULT_PAGE_SIZE))
    if not 1 <= page_size <= MAX_PAGE_SIZE:
        raise ValueError(f"PARCELO_PAGE_SIZE must be between 1 and {MAX_PAGE_SIZE}")

    max_retries = int(env.get("PARCELO_MAX_RETRIES", DEFAULT_MAX_RETRIES))
    if not 0 <= max_retries <= MAX_RETRIES_LIMIT:
        raise ValueError(f"PARCELO_MAX_RETRIES must be between 0 and {MAX_RETRIES_LIMIT}")

    return Settings(
        api_url=env.get("PARCELO_API_URL", DEFAULT_API_URL).rstrip("/"),
        api_key=env.get("PARCELO_API_KEY"),
        timeout_seconds=int(env.get("PARCELO_TIMEOUT", DEFAULT_TIMEOUT_SECONDS)),
        page_size=page_size,
        max_retries=max_retries,
    )
