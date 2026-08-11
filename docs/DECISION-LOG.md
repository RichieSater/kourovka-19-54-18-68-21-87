# Decision log

## 2026-08-11 — repository grouping

**Decision:** create one umbrella Git repository with three isolated problem
subfolders rather than three independent repositories.

**Reasoning:** all three projects will need the same provenance discipline,
software pinning, simple-group inventories, and minimal-counterexample
vocabulary. Keeping them together reduces duplicated infrastructure. Their
predicates, inheritance lemmas, searches, and certificates remain separated to
avoid invalid cross-problem reuse.

**Rejected for now:**

- A repository per problem: clean isolation, but too much duplication at the
  setup stage.
- One flat research directory: makes it too easy to mix predicates and
  evidence.
- A fourth shared-code repository: premature before genuine common executable
  code exists.

## 2026-08-11 — attack order

**Decision:** 19.54, then 18.68, then 21.87.

**Reasoning:** maximize reuse from the monotone-chain work first, then reuse
the maximal-subgroup/CFSG audit pattern, and defer the project needing the most
new crown and generation theory.

## 2026-08-11 — publication boundary

**Decision:** initialize and commit locally, but do not create a GitHub remote
as part of the scaffold-only task.

**Reasoning:** the user requested repository structure and an attack order,
not publication of an unfinished research program. Remote visibility can be
chosen explicitly later.
