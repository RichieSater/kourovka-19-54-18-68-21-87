# Referee pass 3 — reproducibility and evidence boundaries

- **Frozen candidate reviewed:** 8ba6bc2bc3eaa02ebfb201a1e2e7cd2a8356d192
- **Review date:** 2026-08-11
- **Role boundary:** internal reproducibility audit; not external specialist
  peer review
- **Verdict:** **pass**

## Clean-environment reproduction

The candidate was checked out by exact hash in a newly created local clone,
not in the revision working tree.  The following environment was recorded:

- Darwin 25.5.0 on arm64;
- Git 2.49.0;
- GNU Make 3.81;
- Python 3.14.6; and
- Tectonic 0.17.0.

From the clone root, `make check` passed the structure, tracker,
finite-group-notation, proof-bundle, mutation-control, and whitespace gates.
From `problem-21-87/paper`, `./build.sh` produced a seven-page PDF and found no
warning, overfull or underfull box, undefined reference, or error.  The build
left the tracked and untracked Git status empty because all generated files
are ignored.  The regenerated PDF had SHA-256
`272376f58fcf25b839752e25092d7c682f62ea4e3748fc3bd9e2660fc67e27f2`;
this is a run receipt, not a committed or claimed reproducible-bitstream hash.

## Evidence-path audit

The theorem has no computational premise and cites no finite enumeration.
The SmallGroups pilot remains labeled experimental and has no route into the
manuscript's dependency graph.  Accordingly, there are no certificate rows,
GAP outputs, group-inventory counts, or generated mathematical claims to
regenerate.  The machine-checked interface is only between the TeX source,
BibTeX database, source manifest, required proof labels, and review-boundary
statements.

## Negative controls

The clean-clone self-test deliberately made each of these in-memory
corruptions and required the validator to reject it:

1. insertion of an undefined citation key;
2. truncation of the Notebook source checksum; and
3. deletion of the Guralnick source-manifest row.

All three corruptions were detected.  The ordinary, unmodified bundle then
passed.  This confirms that the relevant omission and integrity gates do not
pass vacuously.

## Interface and scope checks

- Every acceptance-critical bibliography key used in the manuscript is
  defined and explicitly required by the checker.
- Required structural lemmas and both competing crown bounds retain labels.
- Source rows fail closed on schema, duplicate or absent identifiers, URL,
  retrieval date, proof role, access note, and checksum format.
- Blank checksums are permitted only for the two disclosed access-restricted
  source files; their public corroborating records remain identified.
- The build wrapper fails on a Tectonic version mismatch or a review-blocking
  LaTeX diagnostic.
- No machine result is described as proving the group-theoretic theorem.

## Issues

| ID | Severity | Observation | Status |
|---|---|---|---|
| F3-01 | P2 | The proof has no finite computational claims, so a subgroup-family certificate would be artificial rather than reproducible evidence. | Closed: the bundle tests its actual prose/source interfaces and explicitly excludes the pilot from the proof path. |
| F3-02 | P2 | A consistency checker without mutations could pass vacuously. | Closed: three representative corruptions are required to fail. |
| F3-03 | P3 | A successful local build alone would not demonstrate a clean checkout. | Closed: the exact candidate was rebuilt in a newly created clone with an empty post-build Git status. |

No P0 or P1 issue remains.

## Verdict rationale

The Round 3 pass gate is satisfied: the exact frozen candidate reproduces in
a clean clone, representative omissions fail closed, and computational
artifacts are asked to support no claim beyond consistency of the review
bundle.  This verdict does not validate the mathematical truth of the
published CFSG-dependent inputs and does not replace external specialist
review.
