#!/usr/bin/env python3
"""Entry program for the make.fun competition "news-summary-01".

Reads summary.txt, stored next to this file, and writes its exact
bytes to entry.txt inside the output directory. The output directory
is $MAKEFUN_OUTPUT_DIR when that environment variable is set, and
/output otherwise. The directory is created if it does not exist.

Standard library only, no network access, fully deterministic.
"""

import os
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "summary.txt"
    data = source.read_bytes()

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
