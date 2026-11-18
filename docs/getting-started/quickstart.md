# Quickstart

This page walks through the two things most people do with Parcelo: tracking one parcel and listing several.

## Track a parcel

Pass a tracking ID to `parcelo track`:

```bash
parcelo track PCL-1001
```

```text
TRACKING ID  STATUS            DESTINATION     KG
PCL-1001     in_transit        Gdansk         2.4
```

## List parcels

List every parcel, or filter by status:

```bash
parcelo list --status in_transit
```

## Get JSON output

Add `--format json` before the subcommand to get machine-readable output:

```bash
parcelo --format json list --limit 2
```

Parcelo supports two output formats: `table` (the default) and `json`.

## Next steps

- Change the defaults in the [configuration reference](../reference/configuration.md).
- See every flag in the [CLI reference](../reference/cli.md).
