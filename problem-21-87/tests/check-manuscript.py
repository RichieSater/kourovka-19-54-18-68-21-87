#!/usr/bin/env python3
"""Fail-closed static checks for the Problem 21.87 proof bundle."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "paper" / "main.tex"
BIBLIOGRAPHY = ROOT / "paper" / "references.bib"
SOURCES = ROOT / "references" / "SOURCES.csv"

CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}")
BIB_RE = re.compile(r"@\w+\{([^,]+),")
SHA_RE = re.compile(r"[0-9a-f]{64}")

REQUIRED_CITATIONS = {
    "BurnessGuralnick2024",
    "DallaVoltaLucchini1998",
    "DetomiLucchini2013",
    "Gruenberg1976",
    "Guralnick1986",
    "KovacsSim1991",
    "kourovka21",
    "Lucchini1990",
    "Lucchini1992",
    "Lucchini2000",
    "Roggenkamp1979",
}
REQUIRED_LABELS = {
    "thm:main",
    "lem:quotient",
    "lem:sylow-coverage",
    "lem:sylow-transport",
    "lem:simple-centralizer",
    "lem:monolithic-centralizer",
    "eq:lower-k",
    "eq:upper-k",
}
REQUIRED_SOURCES = {
    "notebook-21",
    "lucchini-1990",
    "lucchini-1992",
    "roggenkamp-1979",
    "dalla-volta-lucchini-1998",
    "detomi-lucchini-2013",
    "guralnick-1986",
    "burness-guralnick-2024",
}
ALLOWED_BLANK_HASHES = {
    "detomi-lucchini-2013",
    "guralnick-1986",
    "roggenkamp-1979",
}


def parse_sources(text: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(text)))


def validate(manuscript: str, bibliography: str, rows: list[dict[str, str]]) -> list[str]:
    failures: list[str] = []

    bib_key_list = BIB_RE.findall(bibliography)
    bib_keys = set(bib_key_list)
    duplicate_bib_keys = sorted(
        {key for key in bib_key_list if bib_key_list.count(key) > 1}
    )
    if duplicate_bib_keys:
        failures.append(
            "duplicate bibliography keys: " + ", ".join(duplicate_bib_keys)
        )
    cited: set[str] = set()
    for group in CITE_RE.findall(manuscript):
        cited.update(key.strip() for key in group.split(","))

    missing_bib = sorted(cited - bib_keys)
    if missing_bib:
        failures.append("undefined bibliography keys: " + ", ".join(missing_bib))
    unused_bib = sorted(bib_keys - cited)
    if unused_bib:
        failures.append("uncited bibliography keys: " + ", ".join(unused_bib))
    missing_citations = sorted(REQUIRED_CITATIONS - cited)
    if missing_citations:
        failures.append(
            "required sources not cited: " + ", ".join(missing_citations)
        )

    labels = set(re.findall(r"\\label\{([^}]+)\}", manuscript))
    missing_labels = sorted(REQUIRED_LABELS - labels)
    if missing_labels:
        failures.append("required proof labels missing: " + ", ".join(missing_labels))

    lower = " ".join(manuscript.lower().split())
    if "no computer calculation enters it" not in lower:
        failures.append("manuscript does not state the computational evidence boundary")
    if "external specialist" not in lower:
        failures.append("manuscript does not state the external-review boundary")

    fieldnames = {
        "id",
        "citation_or_description",
        "url",
        "retrieved",
        "sha256",
        "proof_role",
        "access_note",
    }
    if not rows:
        failures.append("source manifest is empty")
        return failures
    if set(rows[0]) != fieldnames:
        failures.append("source manifest columns do not match the required schema")

    ids = [row.get("id", "") for row in rows]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        failures.append("duplicate source ids: " + ", ".join(duplicates))
    missing_sources = sorted(REQUIRED_SOURCES - set(ids))
    if missing_sources:
        failures.append("required source rows missing: " + ", ".join(missing_sources))

    for row in rows:
        source_id = row.get("id", "")
        url = row.get("url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            failures.append(f"{source_id}: source URL must be absolute HTTPS")
        if row.get("retrieved") != "2026-08-11":
            failures.append(f"{source_id}: unexpected or missing retrieval date")
        sha = row.get("sha256", "")
        if not sha and source_id not in ALLOWED_BLANK_HASHES:
            failures.append(f"{source_id}: missing SHA-256")
        if sha and not SHA_RE.fullmatch(sha):
            failures.append(f"{source_id}: malformed SHA-256")
        if not row.get("proof_role"):
            failures.append(f"{source_id}: missing proof role")
        if not row.get("access_note"):
            failures.append(f"{source_id}: missing access note")

    return failures


def run_self_test(
    manuscript: str, bibliography: str, rows: list[dict[str, str]]
) -> list[str]:
    failures: list[str] = []

    bad_citation = manuscript + "\n\\cite{deliberately_missing_key}\n"
    if not any(
        "undefined bibliography keys" in item
        for item in validate(bad_citation, bibliography, rows)
    ):
        failures.append("citation mutation was not rejected")

    bad_rows = copy.deepcopy(rows)
    target = next(row for row in bad_rows if row["id"] == "notebook-21")
    target["sha256"] = target["sha256"][:-1]
    if not any(
        "malformed SHA-256" in item
        for item in validate(manuscript, bibliography, bad_rows)
    ):
        failures.append("checksum mutation was not rejected")

    missing_rows = [row for row in rows if row["id"] != "guralnick-1986"]
    if not any(
        "required source rows missing" in item
        for item in validate(manuscript, bibliography, missing_rows)
    ):
        failures.append("source-omission mutation was not rejected")

    return failures


def cited_keys(manuscript: str) -> set[str]:
    keys: set[str] = set()
    for group in CITE_RE.findall(manuscript):
        keys.update(key.strip() for key in group.split(","))
    return keys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    bibliography = BIBLIOGRAPHY.read_text(encoding="utf-8")
    rows = parse_sources(SOURCES.read_text(encoding="utf-8"))

    failures = validate(manuscript, bibliography, rows)
    if args.self_test and not failures:
        failures.extend(run_self_test(manuscript, bibliography, rows))

    if failures:
        print("PROBLEM 21.87 PROOF-BUNDLE CHECK FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    suffix = " and 3 mutation controls" if args.self_test else ""
    print(
        f"PROBLEM 21.87 PROOF BUNDLE OK: {len(rows)} source rows, "
        f"{len(cited_keys(manuscript))} cited keys{suffix}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
