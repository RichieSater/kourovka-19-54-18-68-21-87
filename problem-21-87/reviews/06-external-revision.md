# Response to independently supplied referee report

- **Base candidate:**
  `ada5993f83e2c5e19e91a8bf4669eb702de0e45f`
- **Referee report:** `reviews/06-external-referee.md`
- **Revision candidate:**
  `dec0db6701228d2e9db8ec3065f4e0b1fdd98d38`
- **Date:** 2026-08-11
- **Scope:** attribution, one explicit Sylow-conjugacy transport, separation
  of manuscript and repository verification language, and author metadata
- **Revision status:** all requested changes implemented and frozen

## Response matrix

| ID | Disposition |
|---|---|
| ER6-01 | **Implemented.** Proposition 2.4 now contains only Lucchini's augmentation-ideal bound.  A separate proposition credits Roggenkamp's presentation-rank identity and cites Roggenkamp 1979, Theorem 2.1, directly.  The bibliography, source manifest, source audit, proof map, claim ledger, and fail-closed citation checks were synchronized. |
| ER6-02 | **Implemented.** Lemma 3.1 now starts with a generating pair \((P_0,t_0)\) supplied by Guralnick and explicitly conjugates it so that \(P_0\) becomes the already chosen \(P\). |
| ER6-03 | **Implemented.** The manuscript's closing section now states only the deductive and CFSG dependency boundaries, the no-priority-claim limitation, the external-specialist-review boundary, and a concise AI disclosure.  Checksum, theorem-pinpoint, static-checker, and mutation-control details are retained in the repository's paper, source, and test documentation. |
| ER6-04 | **Implemented.** The title block now gives `Independent Researcher, United States`, `richiesater@gmail.com`, and ORCID [`0009-0007-9051-8207`](https://orcid.org/0009-0007-9051-8207), consistent with the author's other current manuscripts and public metadata. |

## Roggenkamp attribution check

Lucchini 1992, p. 146, explicitly calls

\[
  d(G)=d_G(I_G)+\operatorname{pr}(G)
\]

a result of Roggenkamp and cites *Integral Representations and Presentations
of Finite Groups*, Lecture Notes in Mathematics 744.  The
[official Springer chapter record](https://link.springer.com/chapter/10.1007/BFb0063060)
confirms the author, title, 1979 date, pages 145--275, and DOI
`10.1007/BFb0063060`.  The full chapter is access-restricted; the manifest
records that boundary rather than assigning a checksum to an unavailable
file.

## Review classification

The supplied report is independent of the repository's internal review
passes.  Because the repository has no reviewer identity or evidence of
finite-group generation/crown specialization, it is not relabeled as
completed external specialist peer review.  That boundary remains
outstanding while the mathematical verdict and all four requested changes
are preserved historically.

## Verification

The revised bundle passed:

- `make check`, including structure, tracker, finite-group notation, and
  whitespace gates;
- the fail-closed proof-bundle self-test with 12 source rows, 11 cited keys,
  and all three mutation controls;
- the pinned Tectonic 0.17.0 build, producing seven pages with no LaTeX
  warning, undefined-reference, underfull-box, or overfull-box diagnostic; and
- a page-by-page rendering inspection of all seven pages, including the
  revised attribution, Sylow-conjugacy paragraph, closing disclosure,
  bibliography, and author metadata.

No theorem statement, inequality, crown normalization, or final orbit count
changed in this revision.
