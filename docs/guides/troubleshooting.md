# Troubleshooting

## Requests time out

Parcelo waits 30 seconds for the API to respond before it gives up. On a slow connection, raise the limit with `PARCELO_TIMEOUT`:

```bash
export PARCELO_TIMEOUT=60
```

Parcelo does not retry a failed request. Run the command again if a request fails.

## "No parcel with tracking ID"

The tracking ID does not exist. Tracking IDs are case-sensitive and start with `PCL-`. The command exits with code `2`.

## "PARCELO_PAGE_SIZE must be between 1 and 100"

Set `PARCELO_PAGE_SIZE` to a value in the allowed range, or unset it to use the default.
