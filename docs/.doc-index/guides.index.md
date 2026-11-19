# GUIDES Documentation Index

## Overview
The `guides` documentation area provides operational, integration, and troubleshooting instructions for developers and users interacting with Parcelo. It covers diagnosing common API and CLI execution errors, configuring behavior using environment variables, and establishing HTTPS webhooks for real-time parcel updates.

## Files Summary
* `guides/troubleshooting.md`: Outlines common runtime errors and resolution steps, including timeout adjustments via environment variables, tracking ID validation rules, and page size constraints.
* `guides/webhooks.md`: Details how to integrate with Parcelo's webhook notification system, including endpoint security requirements, JSON payload structures, and response acknowledgement criteria.

## Code Changes That Would Require Documentation Updates
* **Timeout and Retry Policies**: Adjusting the default 30-second API request timeout, modifying request retry behavior, or changing the `PARCELO_TIMEOUT` environment variable name.
* **Tracking ID Formatting and Validation**: Modifying the tracking ID pattern (e.g., prefix changing from `PCL-`), changing case-sensitivity constraints, or altering the CLI exit code (code `2`) for non-existent tracking IDs.
* **Pagination Constraints**: Changing the minimum/maximum bounds for pagination (currently 1 to 100), altering default page sizes, or modifying the `PARCELO_PAGE_SIZE` environment variable name.
* **Webhook Registration & Protocol Requirements**: Changes to how webhook endpoints are registered (e.g., introducing self-service APIs) or changing protocol requirements (e.g., HTTPS enforcement).
* **Webhook Event Schema**: Adding, removing, or changing payload fields (`event`, `tracking_id`, `status`), modifying event naming conventions (e.g., `parcel.status_changed`), or altering the JSON structure.
* **Webhook Delivery & Acknowledgement Logic**: Altering the expected acknowledgement HTTP status codes (currently any `2xx`) or changing the 5-second response timeout window before a webhook attempt is considered failed.

## Key Technical Concepts
* `PARCELO_TIMEOUT`: Environment variable for configuring API request timeout in seconds (default: 30).
* `PARCELO_PAGE_SIZE`: Environment variable for configuring API pagination size (valid range: 1–100).
* `PCL-` tracking ID: Case-sensitive identifier format starting with the `PCL-` prefix.
* Exit Code `2`: CLI exit status returned when a tracking ID is not found.
* Webhook Event `parcel.status_changed`: Notification event triggered when a parcel's delivery status updates.
* Webhook Payload Schema: JSON object containing `event`, `tracking_id`, and `status`.
* Webhook Acknowledgement: Requirement to respond with a `2xx` HTTP status code within a 5-second window.

## Related Components
* **CLI Engine / Error Handler**: Manages command execution, exit codes (e.g., code `2`), and console error messaging.
* **API Client / HTTP Transport**: Handles outbound network calls, timeout limits (`PARCELO_TIMEOUT`), and pagination parameters (`PARCELO_PAGE_SIZE`).
* **Parcel Tracking & ID Service**: Validates, parses, and looks up tracking IDs by prefix and case.
* **Webhook Event Dispatcher**: Emits status change events, formats JSON payloads, and handles HTTP POST deliveries and response timeouts.