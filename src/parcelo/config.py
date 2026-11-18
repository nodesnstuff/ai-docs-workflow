"""Runtime configuration for the Parcelo client.

Every setting is read from an environment variable and falls back to the
default defined in this module.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_API_URL = "https://api.parcelo.example/v1"
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100


@dataclass(frozen=True)
class Settings:
    """Resolved client settings."""

    api_url: str
    api_key: str | None
    timeout_seconds: int
    page_size: int


def load_settings(env: dict[str, str] | None = None) -> Settings:
    """Build Settings from environment variables.

    PARCELO_API_URL   Base URL of the Parcelo API.
    PARCELO_API_KEY   API key sent in the X-Parcelo-Key header.
    PARCELO_TIMEOUT   Request timeout in seconds.
    PARCELO_PAGE_SIZE Number of parcels returned per page (1-100).
    """
    env = dict(os.environ) if env is None else env

    page_size = int(env.get("PARCELO_PAGE_SIZE", DEFAULT_PAGE_SIZE))
    if not 1 <= page_size <= MAX_PAGE_SIZE:
        raise ValueError(f"PARCELO_PAGE_SIZE must be between 1 and {MAX_PAGE_SIZE}")

    return Settings(
        api_url=env.get("PARCELO_API_URL", DEFAULT_API_URL).rstrip("/"),
        api_key=env.get("PARCELO_API_KEY"),
        timeout_seconds=int(env.get("PARCELO_TIMEOUT", DEFAULT_TIMEOUT_SECONDS)),
        page_size=page_size,
    )
