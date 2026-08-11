#!/usr/bin/env python3
"""Fail-closed validation for the scaffold-only repository state."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

PROBLEMS = ("problem-19-54", "problem-18-68", "problem-21-87")
PER_PROBLEM_FILES = (
    "README.md",
    "PROBLEM.md",
    "ATTACK.md",
    "CLAIM-LEDGER.md",
    "gap/README.md",
    "data/README.md",
    "notes/README.md",
    "references/README.md",
    "tests/README.md",
)

ROOT_FILES = (
    "README.md",
    "ATTACK-ORDER.md",
    "STATUS.md",
    "AGENTS.md",
    "LICENSE.md",
    "Makefile",
    "docs/SOURCE-LEDGER.md",
    "docs/LITERATURE-SEARCH.md",
    "docs/PREVIOUS-WORK-AUDIT.md",
    "docs/RESEARCH-PROTOCOL.md",
    "docs/DECISION-LOG.md",
    "shared/README.md",
    "shared/gap/README.md",
    "shared/data/README.md",
    "shared/notes/README.md",
    "shared/references/README.md",
    "shared/tests/README.md",
)

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def validate_expected_files(failures: list[str]) -> None:
    expected = [ROOT / path for path in ROOT_FILES]
    for problem in PROBLEMS:
        expected.extend(ROOT / problem / path for path in PER_PROBLEM_FILES)

    for path in expected:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)
        elif path.stat().st_size == 0:
            fail(f"empty required file: {path.relative_to(ROOT)}", failures)


def validate_links(failures: list[str]) -> None:
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if (
                not target
                or target.startswith(("http://", "https://", "mailto:", "#"))
            ):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                fail(
                    f"broken local link in {document.relative_to(ROOT)}: {raw_target}",
                    failures,
                )


def validate_attack_order(failures: list[str]) -> None:
    text = (ROOT / "ATTACK-ORDER.md").read_text(encoding="utf-8")
    markers = (
        "1. **Problem 19.54**",
        "2. **Problem 18.68**",
        "3. **Problem 21.87**",
    )
    positions = [text.find(marker) for marker in markers]
    if any(position < 0 for position in positions):
        fail("ATTACK-ORDER.md is missing the explicit three-problem order", failures)
    elif positions != sorted(positions):
        fail("ATTACK-ORDER.md does not list the intended order", failures)


def validate_scaffold_status(failures: list[str]) -> None:
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8").lower()
    for problem in ("19.54", "18.68", "21.87"):
        if problem not in status:
            fail(f"STATUS.md does not mention Problem {problem}", failures)
    if "claimed result |\n|---" not in status or "| none |" not in status:
        fail("STATUS.md must retain an explicit no-claimed-result table", failures)


def main() -> int:
    failures: list[str] = []
    validate_expected_files(failures)
    validate_links(failures)
    validate_attack_order(failures)
    validate_scaffold_status(failures)

    if failures:
        print("STRUCTURE CHECK FAILED", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    print(
        "STRUCTURE OK: "
        f"{len(PROBLEMS)} isolated problem workspaces, "
        f"{markdown_count} Markdown files, attack order 19.54 -> 18.68 -> 21.87."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
