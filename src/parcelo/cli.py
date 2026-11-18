"""Command-line interface for Parcelo."""

from __future__ import annotations

import argparse
import json
import sys

from .client import VALID_STATUSES, ParcelNotFound, ParceloClient
from .config import load_settings

EXIT_OK = 0
EXIT_NOT_FOUND = 2
EXIT_USAGE = 64


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="parcelo", description="Track and list parcels.")
    parser.add_argument(
        "--format",
        choices=("table", "json"),
        default="table",
        help="Output format (default: table).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    track = sub.add_parser("track", help="Show one parcel by tracking ID.")
    track.add_argument("tracking_id")

    list_cmd = sub.add_parser("list", help="List parcels.")
    list_cmd.add_argument("--status", choices=VALID_STATUSES, help="Filter by status.")
    list_cmd.add_argument("--limit", type=int, help="Maximum number of parcels to show.")

    return parser


def render(rows: list[dict], fmt: str) -> str:
    if fmt == "json":
        return json.dumps(rows, indent=2)
    header = f"{'TRACKING ID':<12} {'STATUS':<17} {'DESTINATION':<12} {'KG':>5}"
    lines = [
        f"{r['tracking_id']:<12} {r['status']:<17} {r['destination']:<12} {r['weight_kg']:>5}"
        for r in rows
    ]
    return "\n".join([header, *lines])


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    client = ParceloClient(load_settings())

    if args.command == "track":
        try:
            rows = [client.track(args.tracking_id)]
        except ParcelNotFound:
            print(f"No parcel with tracking ID {args.tracking_id}", file=sys.stderr)
            return EXIT_NOT_FOUND
    else:
        rows = client.list_parcels(status=args.status, limit=args.limit)

    print(render(rows, args.format))
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
