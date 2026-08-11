#!/usr/bin/env python3
"""Reject square-delimited subgroup-index notation in reviewable text."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".g", ".md", ".py", ".rst", ".tex", ".txt"}

# Match square-delimited mathematical indices, including subscripted terms and
# quotient expressions. Ordinary prose and Markdown labels containing spaces
# are intentionally outside this narrow check. The repository rule still
# governs cases not caught here.
FORBIDDEN_INDEX = re.compile(
    r"\[\s*"
    r"[A-Za-z\\][A-Za-z0-9_{}^\\()/.-]*"
    r"\s*:\s*"
    r"[A-Za-z\\][A-Za-z0-9_{}^\\()/.-]*"
    r"\s*\]"
)


def candidate_files() -> list[Path]:
    completed = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = completed.stdout.decode("utf-8", errors="surrogateescape").split("\0")
    return [ROOT / name for name in paths if name and Path(name).suffix in TEXT_SUFFIXES]


def main() -> int:
    failures: list[str] = []
    for path in candidate_files():
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: unreadable text file: {exc}")
            continue
        for line_number, line in enumerate(lines, start=1):
            match = FORBIDDEN_INDEX.search(line)
            if match:
                failures.append(
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    f"replace {match.group(0)!r} by vertical-bar index notation"
                )

    if failures:
        print("Finite-group notation check failed:", file=sys.stderr)
        print("\n".join(f"  {failure}" for failure in failures), file=sys.stderr)
        return 1

    print("Finite-group notation check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
