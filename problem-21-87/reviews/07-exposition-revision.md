# Response to English and exposition report

- **Base candidate:**
  `dec0db6701228d2e9db8ec3065f4e0b1fdd98d38`
- **Referee report:** `reviews/07-exposition-referee.md`
- **Date:** 2026-08-11
- **Scope:** surgical English and proof-navigation changes only
- **Revision status:** all requested changes implemented; the validated
  manuscript is to be frozen in a new candidate commit recorded in the
  tracker

## Response matrix

| ID | Disposition |
|---|---|
| ER7-01 | **Implemented.** The introduction now gives the exact nonempty-family, at-most-\(d\)-generated, greatest-common-divisor-\(1\) formulation and states the requested inequality \(d(G)\leq d+1\). |
| ER7-02 | **Implemented.** The coordinatewise quotient map \(\rho:L^d\to(L/A)^d\) is defined before its common fiber \(\Omega\), whose cardinality and componentwise \(\Gamma_{L,A}\)-action are stated. |
| ER7-03 | **Implemented.** A generic \(h\in H\) is written as \(h=(x_1,\ldots,x_k)\).  The relation and supported-coordinate contradiction now use \(x_r,x_s\), not generator notation. |
| ER7-04 | **Implemented.** The coordinate image \(H_j=\langle h_{1j},\ldots,h_{dj}\rangle\) is named, and both pointwise fixation and \(T_j\leq H_j\) are explicit. |
| ER7-05 | **Implemented.** The presentation-rank sentence now says directly that any counterexample must have positive presentation rank. |
| ER7-06 | **Implemented.** The Dalla Volta--Lucchini summary now states their characterization by critical crown-based powers and their exact critical multiplicity. |
| ER7-07 | **Implemented.** The automorphism-centralizer notation is defined elementwise. |
| ER7-08 | **Implemented.** The disclosure now uses the requested mathematical no-computation wording, retains the CFSG, priority, and specialist-review boundaries, and gives the concise AI and author-responsibility statements.  The fail-closed checker was synchronized with that wording. |
| ER7-09 | **Preserved as instructed.** The Detomi--Lucchini title remains exactly as recorded by the journal. |

## Mathematical-change boundary

No theorem, hypothesis, published-input scope, inequality, crown
normalization, centralizer estimate, or orbit count changed.  The additions
name maps, coordinates, and subgroups already present in the proof and make
two containments explicit.

## Verification

The revised manuscript and its supporting proof map and fail-closed checker
were tested together in a clean candidate overlay:

- `make check` passed, including the repository structure, tracker,
  finite-group-notation, proof-bundle, mutation-control, and whitespace
  checks;
- the proof-bundle self-test passed with 12 source rows, 11 cited keys, and
  all three mutation controls;
- Tectonic 0.17.0 produced a seven-page PDF with no warnings, underfull or
  overfull boxes, undefined references, or other review-blocking diagnostics;
  and
- all seven rendered pages were inspected for clipping, collisions, broken
  references, and malformed equations, with none found.
