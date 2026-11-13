"""Export every figure and table the report uses.

Writes to site/figures/ and site/data/. Site pages only read from those folders.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "site" / "figures"
TABLES = ROOT / "site" / "data"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    # TODO: copy/convert figures (PNG/SVG) into FIGURES
    # TODO: write tables (CSV/JSON) into TABLES
    print("export: nothing to export yet (placeholder)")


if __name__ == "__main__":
    main()
