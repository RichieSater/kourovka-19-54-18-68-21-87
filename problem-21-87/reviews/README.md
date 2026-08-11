# Review artifacts

The initial candidate and four sequential internal revision/referee pairs use
the required names:

```text
00-initial-solution.md
01-revision.md  01-referee.md
02-revision.md  02-referee.md
03-revision.md  03-referee.md
04-revision.md  04-referee.md
```

Reports are historical and append-only. Update `REVIEW-PLAN.md`, the root
tracker, and `tracker/portfolio.json` in the same milestone commit.

These are internal adversarial audits. They never count as external
specialist peer review.

After the required four rounds were complete, a direct request for another
full pass produced the supplemental, non-milestone pair
`05-supplemental-revision.md` and `05-supplemental-referee.md`.  The referee
reviewed the frozen corrected candidate `ada5993f` and again recommended
circulation for external specialist review.

Two independently supplied, non-milestone reports follow that internal
audit.  `06-external-referee.md` records a mathematical minor-revision report
on `ada5993f`, with its response in `06-external-revision.md` and changes
frozen at `dec0db6`.  `07-exposition-referee.md` records a subsequent
English/exposition report on `dec0db6`, with its response in
`07-exposition-revision.md` and changes frozen at `517f7d3`.  The latter is
expressly not a finite-group-specialist review.  Neither report closes the
tracked external specialist review requirement.
