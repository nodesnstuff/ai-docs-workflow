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

## Get JSON or CSV output

Add `--output json` or `--output csv` before the subcommand to get machine-readable output:

```bash
parcelo --output json list --limit 2
```

Parcelo supports three output formats: `table` (the default), `json`, and `csv`. You can also use `-o` as a short flag for `--output`.

## Next steps

- Change the defaults in the [configuration reference](../reference/configuration.md).
- See every flag in the [CLI reference](../reference/cli.md).
