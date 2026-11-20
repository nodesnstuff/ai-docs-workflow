# GETTING-STARTED Documentation Index

## Overview
The `getting-started` documentation provides introductory setup and usage instructions for the Parcelo CLI tool. It guides new users through installation requirements, installing from source, verifying the CLI setup, and running basic parcel tracking and listing commands. It also introduces global output formatting options and directs users to detailed reference documentation.

## Files Summary
- `getting-started/install.md`: Covers system prerequisites (Python 3.10+), instructions for cloning and installing Parcelo from source via `pip`, and steps to verify the binary installation.
- `getting-started/quickstart.md`: Demonstrates core CLI usage including tracking single parcels, listing/filtering parcels, applying output flags (`--format json`, `--limit`), and navigating to further documentation.

## Code Changes That Would Require Documentation Updates
- **Python Version Updates**: Changes to minimum supported Python version requirement (currently Python 3.10+).
- **Installation Method / Packaging**: Changes to the installation process, package management tool (e.g., switching from `pip` to `uv`/`poetry`), repository URL, or binary executable name.
- **CLI Commands & Arguments**: Adding, renaming, or modifying subcommands (e.g., `track`, `list`), subcommand positional arguments (e.g., tracking ID format/syntax), or subcommand flags (e.g., `--status`, `--limit`).
- **Global Options & Formatting**: Changes to global CLI options (e.g., location or naming of `--format`), addition or removal of output formats (currently `table` and `json`), or changes to default format behavior.
- **Output Schema / Fields**: Changes to the fields displayed in parcel outputs (currently `TRACKING ID`, `STATUS`, `DESTINATION`, `KG`) or status enum values (e.g., `in_transit`).
- **Documentation Link Structure**: Moving, renaming, or deleting referenced documentation files like `reference/configuration.md` or `reference/cli.md`.

## Key Technical Concepts
- **Python Runtime Requirement**: Python 3.10+
- **Installation Command**: `pip install -e .` (editable source install)
- **Executable / Entry Point**: `parcelo`
- **CLI Subcommands**: `parcelo track`, `parcelo list`, `parcelo --help`
- **Global Flags**: `--format` (`table`, `json`)
- **Command Flags**: `--status`, `--limit`
- **Parcel Data Attributes**: Tracking ID (e.g., `PCL-1001`), Status (`in_transit`), Destination, Weight (KG)
- **Environment Prerequisites**: Executable `PATH` configuration

## Related Components
- **CLI Module / Entry Point**: CLI parser (e.g., Click/Typer/argparse handler) exposing `parcelo`, `track`, and `list` commands.
- **Output Formatters**: Table rendering and JSON serialization modules for CLI output.
- **Package Setup**: `pyproject.toml` or `setup.py` defining script entry points and dependency requirements.
- **Parcel Data Engine**: Backend services or data models handling parcel tracking, listing, status filtering, and query limits.