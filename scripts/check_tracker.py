#!/usr/bin/env python3
"""Validate the portfolio milestone schema and sequencing."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "tracker" / "portfolio.json"

EXPECTED_PROBLEMS = {"10.34", "18.68", "19.54", "19.57", "19.58", "21.87"}
EXPECTED_MILESTONES = [
    "initial_solution",
    "revision_1",
    "referee_1",
    "revision_2",
    "referee_2",
    "revision_3",
    "referee_3",
    "revision_4",
    "referee_4",
]
ALLOWED_STATES = {
    "not_started",
    "in_progress",
    "revision_required",
    "blocked",
    "complete",
    "complete_legacy",
}
COMPLETE_STATES = {"complete", "complete_legacy"}
ACTIVE_PROBLEMS = {"18.68", "19.54", "21.87"}


def main() -> int:
    failures: list[str] = []
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    if data.get("schema_version") != 1:
        failures.append("schema_version must be 1")
    if data.get("milestone_order") != EXPECTED_MILESTONES:
        failures.append("milestone_order does not match the nine-stage protocol")

    projects = data.get("projects")
    if not isinstance(projects, list):
        failures.append("projects must be a list")
        projects = []

    identifiers = [project.get("problem") for project in projects]
    if set(identifiers) != EXPECTED_PROBLEMS or len(identifiers) != len(
        EXPECTED_PROBLEMS
    ):
        failures.append(
            "tracker must contain exactly 10.34, 18.68, 19.54, 19.57, "
            "19.58, and 21.87"
        )

    in_progress: list[str] = []
    for project in projects:
        problem = project.get("problem", "<missing>")
        milestones = project.get("milestones", {})
        if list(milestones) != EXPECTED_MILESTONES:
            failures.append(f"{problem}: milestone keys/order are invalid")
            continue

        earlier_complete = True
        for name in EXPECTED_MILESTONES:
            record = milestones[name]
            if not isinstance(record, dict):
                failures.append(f"{problem}/{name}: record must be an object")
                earlier_complete = False
                continue
            state = record.get("status")
            evidence = record.get("evidence")
            if state not in ALLOWED_STATES:
                failures.append(f"{problem}/{name}: invalid status {state!r}")
            if not isinstance(evidence, str) or not evidence.strip():
                failures.append(f"{problem}/{name}: evidence field is required")
            if state != "not_started" and not earlier_complete:
                failures.append(
                    f"{problem}/{name}: started before every earlier milestone completed"
                )
            if state == "in_progress":
                in_progress.append(f"{problem}/{name}")
            if state in COMPLETE_STATES and not earlier_complete:
                failures.append(
                    f"{problem}/{name}: completed after an incomplete earlier milestone"
                )
            earlier_complete = earlier_complete and state in COMPLETE_STATES

        publication = project.get("publication_status")
        artifacts = project.get("public_artifacts")
        if publication != "none" and not artifacts:
            failures.append(f"{problem}: public status requires a public artifact")

    active_in_progress = [
        item for item in in_progress if item.split("/", 1)[0] in ACTIVE_PROBLEMS
    ]
    if len(active_in_progress) > 1:
        failures.append(
            "only one open-problem milestone may be in progress: "
            + ", ".join(active_in_progress)
        )

    dashboard = (ROOT / "TRACKER.md").read_text(encoding="utf-8")
    for problem in EXPECTED_PROBLEMS:
        if f"**{problem}**" not in dashboard:
            failures.append(f"TRACKER.md has no dashboard row for {problem}")

    for problem in ACTIVE_PROBLEMS:
        path = ROOT / f"problem-{problem.replace('.', '-')}" / "REVIEW-PLAN.md"
        if not path.is_file():
            failures.append(f"missing active review plan: {path.relative_to(ROOT)}")

    workstreams = {
        project["problem"]: project.get("workstream") for project in projects
    }
    if workstreams.get("19.57") != workstreams.get("19.58"):
        failures.append("19.57 and 19.58 must share their joint review workstream")

    if failures:
        print("TRACKER CHECK FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    complete = sum(
        record["status"] in COMPLETE_STATES
        for project in projects
        for record in project["milestones"].values()
    )
    total = len(projects) * len(EXPECTED_MILESTONES)
    print(
        f"TRACKER OK: {len(projects)} problem rows, {total} milestones, "
        f"{complete} complete/legacy-complete, {len(in_progress)} in progress."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
