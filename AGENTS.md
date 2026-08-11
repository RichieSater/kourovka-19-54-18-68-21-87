# Repository rules

This repository is a public-safe research workspace for Kourovka Problems
19.54, 18.68, and 21.87.

## Current boundary

The initial setup is complete. Do not begin computational reconnaissance or
proof development until a later explicit task resumes the attack order in
`ATTACK-ORDER.md`.

## Milestone tracking

- Follow `docs/SOLUTION-REVIEW-WORKFLOW.md`: one initial solution candidate,
  then four revision/referee pairs.
- Update `tracker/portfolio.json`, `TRACKER.md`, and the problem's
  `REVIEW-PLAN.md` together.
- Freeze the exact candidate commit before every referee pass.
- Preserve referee reports historically; answer them in a new revision file.
- Internal passes never count as external specialist peer review.

## Rigor

1. Label statements as **proved**, **published input**, **computationally
   certified**, **experimental**, **conjectural**, or **unchecked**.
2. A positive universal verdict requires exhaustive coverage. A single
   negative witness may refute a universal property, but it must include enough
   data to be independently reproduced.
3. Never infer a property of sections, quotients, socles, or extensions until
   the relevant inheritance lemma is proved or cited.
4. Character-table, subgroup-lattice, and GAP computations are discovery or
   finite verification. Connect them to a published exhaustive classification
   before using them in an infinite-family proof.
5. Do not claim novelty or current openness without a dedicated, dated
   literature search.
6. Keep correspondence, private messages, and recipient-specific drafts out of
   the repository.

## Finite-group notation (hard rule)

- In every group-theory project, manuscript, research note, review, generated
  artifact, and final response, conform notation to standard conventions in
  modern finite group theory.
- Write the index of a subgroup `M` in `G` as `|G:M|` (in LaTeX,
  `\lvert G:M\rvert`), never with square delimiters.
- Normalize imported or adapted prose before circulation. Preserve the original
  notation only inside a clearly marked verbatim quotation.
- Treat violations as blocking style-check failures, not discretionary edits.

## Reuse of earlier work

- Consult `docs/PREVIOUS-WORK-AUDIT.md` before copying a reduction or script.
- Reuse code only when its license permits it, preserve provenance, and add
  tests for the new predicate.
- Do not assume the quotient behavior from Problem 10.34 or 19.57/19.58 also
  holds here.

## Reproducibility

- Pin GAP and package versions before committing generated certificates.
- Generated data must name its producer command and exact environment.
- Fail closed on missing subgroup or character-table data.
- Run `make check` before every commit.

## Git attribution

Every commit must use:

```text
Richie Sater <15129476+RichieSater@users.noreply.github.com>
```

Verify `git config user.name` and `git config user.email` before committing.
