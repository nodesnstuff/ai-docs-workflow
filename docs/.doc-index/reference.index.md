# REFERENCE Documentation Index

## Overview
The REFERENCE documentation provides technical specification details for using the Parcelo CLI tool and API client. It details API request rate limits and page size constraints, command-line syntax, subcommands, flags, exit codes, and environment variable configuration settings.

## Files Summary
- `reference/api-limits.md`: Documents rate limits (requests per minute) and maximum page size limits enforced by the Parcelo API, along with HTTP 429 error response behavior.
- `reference/cli.md`: Defines the command-line interface syntax, global options, subcommands (`track`, `list`), status filters, output formats, and exit codes for the `parcelo` CLI tool.
- `reference/configuration.md`: Outlines environment variables used to configure the Parcelo client (API URL, authentication key, request timeouts, page size defaults) and validation rules.

## Code Changes That Would Require Documentation Updates
- **API Rate Limiting & Pagination Limits**: Adjusting the default rate limit (e.g., changing 60 requests per minute), altering the maximum page size (e.g., changing max limit of 100), or changing the HTTP response status code for throttled requests.
- **CLI Commands and Options**: Adding, removing, or renaming subcommands (e.g., changing `track` or `list`), adding or changing global options (e.g., changing `--format` options beyond `table` and `json`), or changing command-specific flags (e.g., `--status`, `--limit`).
- **Parcel Status Enum Values**: Adding, removing, or renaming valid parcel statuses used in CLI filtering (`created`, `in_transit`, `out_for_delivery`, `delivered`).
- **CLI Exit Codes**: Changing existing process exit code numbers (`0`, `2`, `64`) or introducing new exit codes for error conditions.
- **Environment Variable Configuration**: Adding, renaming, or removing environment variable names (`PARCELO_API_URL`, `PARCELO_API_KEY`, `PARCELO_TIMEOUT`, `PARCELO_PAGE_SIZE`).
- **Configuration Defaults and Validation**: Modifying default values for configuration options (e.g., default timeout or default page size) or changing validation range boundaries for `PARCELO_PAGE_SIZE`.
- **Authentication Headers**: Changing the HTTP header key used to convey the API key (e.g., modifying `X-Parcelo-Key`).

## Key Technical Concepts
- **Environment Variables**: `PARCELO_API_URL`, `PARCELO_API_KEY`, `PARCELO_TIMEOUT`, `PARCELO_PAGE_SIZE`
- **CLI Subcommands**: `parcelo track <tracking_id>`, `parcelo list`
- **CLI Flags & Options**: `--format` (`table`, `json`), `-h`/`--help`, `--status`, `--limit`
- **Parcel Statuses**: `created`, `in_transit`, `out_for_delivery`, `delivered`
- **CLI Exit Codes**: `0` (Success), `2` (No parcel matches tracking ID), `64` (Invalid usage)
- **API & HTTP Concepts**: HTTP `429 Too Many Requests`, `X-Parcelo-Key` header, 60 requests per minute limit, max page size limit (100)

## Related Components
- **Parcelo CLI Application**: Command-line parser, command handlers, output formatters (`table`, `json`), exit code handlers.
- **Parcelo API Client**: HTTP client, authentication header generator (`X-Parcelo-Key`), timeout handler, rate limit/429 retry logic.
- **Configuration Module**: Environment variable loader, configuration defaults manager, validation logic for page sizes and timeouts.
- **Parcelo API Backend / Gateway**: API rate limiter middleware, parcel tracking service, pagination engine.