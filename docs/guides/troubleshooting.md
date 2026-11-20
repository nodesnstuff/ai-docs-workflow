# Troubleshooting

## Requests time out

Parcelo waits 10 seconds for the API to respond before it gives up. On a slow connection, raise the limit with `PARCELO_TIMEOUT`:

```bash
export PARCELO_TIMEOUT=60
```

By default, Parcelo automatically retries failed requests up to 3 times with exponential backoff. You can configure the maximum retries with `PARCELO_MAX_RETRIES` or set it to `0` to disable retries:

```bash
export PARCELO_MAX_RETRIES=5
```

## "No parcel with tracking ID"

The tracking ID does not exist. Tracking IDs are case-sensitive and start with `PCL-`. The command exits with code `2`.

## "PARCELO_PAGE_SIZE must be between 1 and 100"

Set `PARCELO_PAGE_SIZE` to a value in the allowed range, or unset it to use the default.

## "PARCELO_MAX_RETRIES must be between 0 and 10"

Set `PARCELO_MAX_RETRIES` to a value in the allowed range, or unset it to use the default.
