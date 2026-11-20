# Configuration reference

Parcelo reads its configuration from environment variables. Every variable is optional and falls back to the default shown here.

| Variable | Default | Description |
|---|---|---|
| `PARCELO_API_URL` | `https://api.parcelo.example/v1` | Base URL of the Parcelo API. |
| `PARCELO_API_KEY` | not set | API key sent in the `X-Parcelo-Key` header. |
| `PARCELO_TIMEOUT` | `10` | Request timeout in seconds. |
| `PARCELO_PAGE_SIZE` | `25` | Number of parcels returned per page. Must be between 1 and 100. |
| `PARCELO_MAX_RETRIES` | `3` | Times a failed request is retried. Must be between 0 and 10. Set to 0 to disable retries. |

## Example

```bash
export PARCELO_API_KEY="pk_test_123"
export PARCELO_TIMEOUT=10
parcelo list
```

## Validation

Parcelo stops with an error if `PARCELO_PAGE_SIZE` is outside the range 1 to 100 or if `PARCELO_MAX_RETRIES` is outside the range 0 to 10.
