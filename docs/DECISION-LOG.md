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

## 2026-08-11 — solution and review lifecycle

**Decision:** every open problem must produce an initial complete solution
candidate and then pass four explicit revision/referee pairs: structural,
classification/source, computational/reproducibility, and hard-final.

**Reasoning:** the prior projects improved materially under repeated
adversarial and clean-room review. A fixed lifecycle makes those gates visible
before a result is circulated and prevents a successful computation or one
favorable pass from being treated as external validation.

Problems 10.34, 19.57, and 19.58 are included as retrospectively mapped legacy
projects. Their public artifacts are preprints/research releases; external
specialist peer review remains a separate outstanding status.

## 2026-08-11 — Problem 21.87 scheduling exception

**Decision:** activate Problem 21.87 immediately, before Problems 19.54 and
18.68.

**Reasoning:** the user explicitly requested a complete solution to Problem
21.87. This overrides the default attack order for the current work while
leaving the other two projects' mathematical and milestone states unchanged.
