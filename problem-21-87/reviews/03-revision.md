# Revision 3 — reproducibility and evidence boundary

- **Base candidate:** ec734ae960cfe1b408b625f6ecf05e738c793d40
- **Revision candidate:** `8ba6bc2bc3eaa02ebfb201a1e2e7cd2a8356d192`
- **Date:** 2026-08-11
- **Scope:** clean build, source-manifest validation, negative controls, and
  separation of exploratory computation from proof

## Evidence inventory

The theorem uses prose deductions and published inputs only. It has no
finite-group database row, GAP computation, character table, subgroup
lattice, or generated certificate on its proof path. Consequently the correct
computational audit is to verify that no experimental result is cited as
evidence, rather than to manufacture a finite certificate for an infinite
theorem.

## Response matrix

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| R3-01 | P2 | The manuscript build command documented a version but did not enforce it. | Added paper/build.sh, which requires Tectonic 0.17.0, rejects log diagnostics, and checks the PDF page count. |
| R3-02 | P2 | Bibliography and source-manifest drift could pass the general repository checks. | Added tests/check-manuscript.py and wired it into make check. |
| R3-03 | P2 | A checker without negative controls can pass vacuously. | Added citation-key, checksum, and missing-source mutations; all must be rejected. |
| R3-04 | P2 | The exploratory SmallGroups pilot did not meet its own row-receipt contract. | Kept it explicitly experimental, committed no purported certificate, and stated that the manuscript uses none of it. |
| R3-05 | P3 | Generated PDF and LaTeX intermediates could pollute the review commit. | They remain ignored; reviewers regenerate the PDF from source. |

## Reproduction commands

From the umbrella repository root:

1. Run “make check”.
2. Change to problem-21-87/paper.
3. Run “./build.sh”.

Expected results:

- the structure, tracker, finite-group notation, proof-bundle, mutation, and
  whitespace checks all pass;
- the manuscript compiles with Tectonic 0.17.0;
- the LaTeX diagnostic scan is empty; and
- a nonempty PDF with a readable page count is produced.

## Fail-closed controls

The proof-bundle self-test confirms that each of the following changes makes
the checker fail:

1. adding a citation whose key is absent from the bibliography;
2. shortening a recorded SHA-256 value; and
3. deleting the Guralnick source row.

## Boundary

Passing these checks proves only artifact consistency and reproducibility. It
does not establish the mathematical truth of the published CFSG inputs or
replace external specialist review.
