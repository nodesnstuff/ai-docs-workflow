# Parcelo docs pilot

A small sandbox for trying Red Hat's [Code-to-Docs](https://github.com/redhat-community-ai-tools/code-to-docs) AI documentation reviewer. It contains:

- **Dummy code**: `src/parcelo`, a parcel-tracking CLI that runs on made-up data
- **A docs site**: `docs/`, built with MkDocs Material and deployed to GitHub Pages
- **The reviewer**: `.github/workflows/docs-assistant.yml`, which runs Code-to-Docs when you comment on a pull request
- **A prepared code change**: `demo/`, which makes four docs pages out of date

## What it costs

Nothing, as long as the repository is public.

| Piece | Free because |
|-------|--------------|
| Code-to-Docs | Open source (MIT), runs as a GitHub Action |
| GitHub Actions and Pages | Free for public repositories |
| MkDocs Material | Open source |
| Model | Gemini API free tier from Google AI Studio, no card needed |

## Setup

Allow about 15 minutes.

### 1. Create the repository

Create an empty **public** repository on GitHub named `parcelo-docs-pilot`, then push these files:

```bash
cd parcelo-docs-pilot
git init -b main
git add -A
git commit -m "Initial pilot"
git remote add origin https://github.com/YOUR-USERNAME/parcelo-docs-pilot.git
git push -u origin main
```

### 2. Get a free model key

1. Open [Google AI Studio](https://aistudio.google.com/apikey) and create an API key. Do not link a billing account.
2. In the repository, go to **Settings > Secrets and variables > Actions > New repository secret**.
3. Name it `MODEL_API_KEY` and paste the key.

The workflow defaults to the model `gemini-3.6-flash`. If AI Studio lists different free models, set a repository **variable** named `MODEL_NAME` on the same settings page (Variables tab).

### 3. Change two repository settings

- **Settings > Actions > General > Workflow permissions**: select *Read and write permissions* and tick *Allow GitHub Actions to create and approve pull requests*. Code-to-Docs needs this to open its index pull request.
- **Settings > Pages > Build and deployment > Source**: select *GitHub Actions*.

Then run the site workflow once: **Actions > Docs site > Run workflow**. The site appears at `https://YOUR-USERNAME.github.io/parcelo-docs-pilot/`.

### 4. Open the demo pull request

With the [GitHub CLI](https://cli.github.com/) installed:

```bash
bash demo/open-demo-pr.sh
```

Without it, create a branch, run `git apply demo/retries-and-output-flag.patch`, commit, push, and open the pull request in the browser.

## Run the pilot

1. On the pull request, comment `[review-docs]`. After a few minutes the bot replies with a checklist of doc files it wants to update, and why.
2. The first run also opens a separate pull request that adds `docs/.doc-index/`. Merge it. Later runs use this index to find files faster.
3. Untick any file you disagree with.
4. Comment `[update-docs]`. The bot commits the doc changes to the pull request branch.
5. Review the diff as you would any docs change.

To steer the output, add instructions to the comment:

```text
[update-docs] keep changes minimal
cli.md: only update the options table and the synopsis
```

Standing style rules live in `.code-to-docs/style.md`.

## What a good result looks like

The demo change makes exactly four pages wrong. Use this as the answer key.

| Page | What should change |
|------|--------------------|
| `reference/configuration.md` | `PARCELO_TIMEOUT` default becomes `10`; new `PARCELO_MAX_RETRIES` row (default `3`, range 0 to 10); validation section mentions the new range |
| `reference/cli.md` | `--format` becomes `--output` / `-o`; `csv` added to the formats |
| `getting-started/quickstart.md` | `--format json` example and the "two output formats" sentence |
| `guides/troubleshooting.md` | 30-second timeout becomes 10; "does not retry" is no longer true |

These pages should be left alone: `index.md`, `getting-started/install.md`, `guides/webhooks.md`, `reference/api-limits.md`.

Things worth scoring during the pilot:

- **Recall**: how many of the four pages did it find?
- **Precision**: did it flag any page that should be left alone?
- **Accuracy**: are the new defaults and flag names correct, with nothing invented?
- **Restraint**: did it change only the affected lines, and follow `style.md`?
- **Time**: how long from comment to result?

## Limits to know about

- Only repository owners, members, and collaborators can trigger the reviewer. This protects your model quota.
- The workflow runs from the version on `main`, so changes to it take effect only after they are merged.
- Commits pushed by the bot do not trigger the *Docs site* build check. Push an empty commit or re-run the check if you want it.
- Google can use free-tier prompts to improve its products, so keep real code and data out of this repository.
- The free tier has per-minute and per-day request caps. If a run fails with a 429 error, wait and comment again.
- `[review-feature]` (Jira spec-versus-code analysis) is switched off here. It needs a Jira site and extra secrets; see the Code-to-Docs README.

## Use a different model

Code-to-Docs works with any OpenAI-compatible endpoint. Set the repository variables `MODEL_API_BASE` and `MODEL_NAME`, and put the provider's key in the `MODEL_API_KEY` secret.

## Preview the site locally

```bash
pip install -r requirements-docs.txt
mkdocs serve
```
