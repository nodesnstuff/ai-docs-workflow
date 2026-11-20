"""Parcelo API client.

This is a pilot project with dummy data: the "API" is an in-memory list so
the code runs without any network access or real service.
"""

from __future__ import annotations

import time
from dataclasses import asdict, dataclass

from .config import Settings

RATE_LIMIT_PER_MINUTE = 60
RETRY_BACKOFF_SECONDS = 2
VALID_STATUSES = ("created", "in_transit", "out_for_delivery", "delivered")


@dataclass(frozen=True)
class Parcel:
    tracking_id: str
    status: str
    destination: str
    weight_kg: float


_DUMMY_PARCELS = [
    Parcel("PCL-1001", "in_transit", "Gdansk", 2.4),
    Parcel("PCL-1002", "delivered", "Lisbon", 0.8),
    Parcel("PCL-1003", "out_for_delivery", "Rotterdam", 5.1),
    Parcel("PCL-1004", "created", "Vienna", 1.2),
    Parcel("PCL-1005", "in_transit", "Tallinn", 12.0),
]


class ParcelNotFound(Exception):
    """Raised when a tracking ID does not exist."""


class ParceloClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def _with_retries(self, request):
        """Run a request, retrying on ConnectionError or TimeoutError.

        Waits RETRY_BACKOFF_SECONDS, doubling after each attempt, and gives up
        after settings.max_retries retries.
        """
        delay = RETRY_BACKOFF_SECONDS
        for attempt in range(self.settings.max_retries + 1):
            try:
                return request()
            except (ConnectionError, TimeoutError):
                if attempt == self.settings.max_retries:
                    raise
                time.sleep(delay)
                delay *= 2

    def track(self, tracking_id: str) -> dict:
        """Return a single parcel by tracking ID."""

        def request():
            for parcel in _DUMMY_PARCELS:
                if parcel.tracking_id == tracking_id:
                    return asdict(parcel)
            raise ParcelNotFound(tracking_id)

        return self._with_retries(request)

    def list_parcels(self, status: str | None = None, limit: int | None = None) -> list[dict]:
        """Return parcels, optionally filtered by status.

        `limit` defaults to the configured page size.
        """
        if status is not None and status not in VALID_STATUSES:
            raise ValueError(f"Unknown status: {status}")
        limit = self.settings.page_size if limit is None else limit
        parcels = [p for p in _DUMMY_PARCELS if status is None or p.status == status]
        return [asdict(p) for p in parcels[:limit]]
