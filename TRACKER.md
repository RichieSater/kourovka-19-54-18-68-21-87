# Kourovka research and review tracker

**As of:** 2026-08-11
**Machine-readable mirror:** [`tracker/portfolio.json`](tracker/portfolio.json)
**Lifecycle instructions:**
[`docs/SOLUTION-REVIEW-WORKFLOW.md`](docs/SOLUTION-REVIEW-WORKFLOW.md)

## Status key

- `✅` — completed under the current protocol, or retrospectively evidenced
  legacy work (`†`).
- `🟡` — in progress.
- `↺` — revision required by the latest referee verdict.
- `⛔` — blocked by a named external dependency.
- `⬜` — not started.

`R1/P1` means revision round 1 followed by referee pass 1. Four rounds are
required after the initial solution candidate.

## Portfolio dashboard

| Problem | Mathematical/public status | Initial | R1/P1 | R2/P2 | R3/P3 | R4/P4 | External specialist peer review |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **10.34** | Claimed complete solution; [public arXiv preprint](https://arxiv.org/abs/2608.02970), release `v1.0.8` | ✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | Outstanding |
| **19.57** | Claimed complete solution; joint public proof-audit preprint with 19.58, release `v1.0.1` | ✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | Outstanding |
| **19.58** | Claimed complete solution; joint public proof-audit preprint with 19.57, release `v1.0.1` | ✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | ✅†/✅† | Outstanding |
| **19.54** | Open target; scaffold only | ⬜ | ⬜/⬜ | ⬜/⬜ | ⬜/⬜ | ⬜/⬜ | Not applicable yet |
| **18.68** | Open target; scaffold only | ⬜ | ⬜/⬜ | ⬜/⬜ | ⬜/⬜ | ⬜/⬜ | Not applicable yet |
| **21.87** | Claimed complete solution draft; Revision 1 frozen | ✅ | ✅/⬜ | ⬜/⬜ | ⬜/⬜ | ⬜/⬜ | Outstanding |

`†` Legacy completion is mapped retrospectively from the public repositories'
commit, release, audit, and referee records. It means that an equivalent
substantive stage is evidenced; it does not assert that the historical work
used the exact filenames or order in the new protocol.

## Active work order

1. [Problem 19.54 review plan](problem-19-54/REVIEW-PLAN.md)
2. [Problem 18.68 review plan](problem-18-68/REVIEW-PLAN.md)
3. [Problem 21.87 review plan](problem-21-87/REVIEW-PLAN.md)

Only one open problem should have `initial_solution` or a revision marked
`in_progress` at a time unless a written scheduling exception is added to the
decision log.

The direct user request of 2026-08-11 is the scheduling exception activating
Problem 21.87 before the two earlier portfolio targets.

## Legacy evidence

- [Problem 10.34 lifecycle mapping](tracker/legacy-10-34.md)
- [Problems 19.57/19.58 lifecycle mapping](tracker/legacy-19-57-19-58.md)

The word "public" here means publicly released as a preprint/research
artifact. Neither legacy project claims journal acceptance or completed
external specialist peer review.

## Update rule

1. Update `tracker/portfolio.json` when a milestone changes state.
2. Update this dashboard and the applicable `REVIEW-PLAN.md` in the same
   commit.
3. Link the frozen candidate commit and required artifacts.
4. Run `make check`.
5. A referee may mark a pass complete only by issuing an explicit verdict and
   an itemized report; a successful test run alone is not a referee pass.
