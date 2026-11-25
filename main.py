"""Entry for make.fun bounty: The 3 AM Excuse.

Writes a single line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "Not signing at 3 AM: last time I approved a half-asleep thumb, we bought a picture of a yacht and a coin named after soup; wake me when the sun can co-sign."
MAX_CHARS = 200


def write_entry(out_dir: str) -> Path:
    if not LINE or LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("entry must be a single non-empty line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
