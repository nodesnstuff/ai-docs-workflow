#!/usr/bin/env bash
# Opens a pull request that changes code but not docs, so Code-to-Docs has
# something to find. Run from the repository root after the first push to main.
# Needs git and the GitHub CLI (gh auth login).
set -euo pipefail

BRANCH="feature/retries-and-output-flag"

git checkout main
git pull --ff-only
git checkout -b "$BRANCH"
git apply demo/retries-and-output-flag.patch
git add src
git commit -m "Add request retries, CSV output, and a shorter default timeout"
git push -u origin "$BRANCH"

gh pr create \
  --base main \
  --title "Add request retries, CSV output, and a shorter default timeout" \
  --body "Code-only change for the Code-to-Docs pilot. The docs are intentionally left out of date.

- New \`PARCELO_MAX_RETRIES\` setting (default 3, range 0-10) with exponential backoff
- Default timeout lowered from 30 to 10 seconds
- \`--format\` renamed to \`--output\` / \`-o\`, with a new \`csv\` format"

echo
echo "Pull request opened. Comment [review-docs] on it to run the reviewer."
