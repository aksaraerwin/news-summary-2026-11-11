#!/usr/bin/env python3
"""Entry program for the make.fun competition "news-summary-01".

Reads summary.txt, stored next to this file, and writes its exact
bytes — unmodified, with nothing added or stripped — to entry.txt
inside the output directory. The output directory is
$MAKEFUN_OUTPUT_DIR when that environment variable is set, and
/output otherwise. The directory is created if it does not exist.

Standard library only, no network access, fully deterministic:
running it any number of times produces the same bytes.
"""

import os
from pathlib import Path


def entry_path() -> Path:
    """Return the path of the entry.txt file to write."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    source_path = Path(__file__).resolve().parent / "summary.txt"
    entry_path().write_bytes(source_path.read_bytes())


if __name__ == "__main__":
    main()
