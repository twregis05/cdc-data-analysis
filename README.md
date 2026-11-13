# cdc-data-analysis

**Goal:** an end-to-end data science project (clean, explore, visualize, test, model, report) published as a static website.
**Question:** TODO (one sentence). See `docs/questions.md`.
Progress: `CHECKLIST.md`.

## Folder layout
| Path | Purpose |
|------|---------|
| `data/raw/` | Original data, never edited, contents git-ignored (see its README) |
| `data/clean/` | `base.csv`, produced only by `cleaning/base_clean.ipynb` |
| `data/derived/` | `<question-name>.csv`, per-question datasets |
| `cleaning/` | Shared base clean notebook and `cleaning_log.md` |
| `analysis/python/`, `analysis/r/` | Each person's exploration and question-specific cleaning (Python notebooks; R may use scripts or Rmd/Quarto-free notebooks) |
| `tests/hypothesis/` | One `.md` per hypothesis test (template included) |
| `model/` | The single modeling pipeline, in a notebook (language TBD) |
| `feature_check/` | Exploration patterns vs. model importance |
| `export/` | Script that writes figures/tables into `site/` |
| `site/` | Static report (HTML/CSS/JS) |
| `docs/` | Question tracker |

## Environment setup
**Python** (use `uv` if installed, otherwise `venv`):
```sh
# with uv
uv venv && uv pip install -r requirements.txt
# without uv
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```
**R:** install R, open it in the project root, then run `source("setup_r.R")` (first time only).
On another machine: `renv::restore()`.

## Workflow
1. Raw data goes in `data/raw/`, never edited.
2. `cleaning/base_clean.ipynb` writes `data/clean/base.csv` (only fixes valid for every question); decisions go in `cleaning/cleaning_log.md`.
3. Each person explores and cleans per question in their own folder, reading `base.csv` and writing `data/derived/<question-name>.csv`.
4. Hypothesis tests live with the questions they answer (`tests/hypothesis/`). The model is one pipeline in one language, with a seeded split and preprocessing fit on training data only.
5. `feature_check/` compares top model features to exploration patterns.
6. `export/export_site.py` writes every figure and table to `site/figures` and `site/data`; report pages only read from there.

Main charts are built by hand in Tableau Public from the cleaned CSVs.

**Rule:** `data/raw/` and `base.csv` change only through the base clean notebook (and the raw data never at all).

## Make targets
`make base-clean`, `make export`, `make serve` (http://localhost:8000), `make all`.

## Git conventions
- One branch per person; small commits; review each other's changes before merging to `main`.
- Work in notebooks, but notebooks diff badly: strip outputs before committing (`pip install nbstripout`, then `nbstripout --install` once per clone) and avoid both of you editing the same notebook at once.

## Publishing (GitHub Pages)
Run `make export`, commit, push. In the GitHub repo: Settings > Pages > deploy from branch `main`, folder `/site` if offered
(otherwise use a `gh-pages` branch or GitHub Actions to publish `site/`). TODO: confirm once the repo is on GitHub.
