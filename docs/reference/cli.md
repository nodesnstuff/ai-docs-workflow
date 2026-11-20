# CLI reference

```text
parcelo [--output {table,json,csv}] <command> [options]
```

## Global options

| Option | Description |
|---|---|
| `-o`, `--output {table,json,csv}` | Output format. Defaults to `table`. |
| `-h`, `--help` | Show help and exit. |

## Commands

### `parcelo track <tracking_id>`

Shows one parcel by tracking ID.

```bash
parcelo track PCL-1003
```

### `parcelo list`

Lists parcels.

| Option | Description |
|---|---|
| `--status` | Filter by status: `created`, `in_transit`, `out_for_delivery`, or `delivered`. |
| `--limit` | Maximum number of parcels to show. Defaults to the configured page size. |

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Success. |
| `2` | No parcel matches the tracking ID. |
| `64` | Invalid usage. |
