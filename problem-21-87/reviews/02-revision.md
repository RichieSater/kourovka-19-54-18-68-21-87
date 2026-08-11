# Revision 2 — classification and source audit

- **Base candidate:** 671b5c45d2bed165a9efb8ec58167b0c8f834fdd
- **Revision candidate:** `ec734ae960cfe1b408b625f6ecf05e738c793d40`
- **Date:** 2026-08-11
- **Scope:** crown theorem scope, probability normalization, exhaustive socle
  branches, CFSG dependence, bibliographic identity, and priority boundary

## Source-by-source reconstruction

### Dalla Volta--Lucchini

Theorem 1.4 was inspected on printed p. 85. Its hypotheses are \(m\geq2\),
\(d(X/N)\leq m\) for each nontrivial normal subgroup \(N\), and \(d(X)>m\).
Its conclusion is exactly the critical crown-based power used in the
manuscript. Theorem 2.7 on printed pp. 87--88 gives the nonabelian formula in
terms of Eulerian functions. The manuscript now displays that source formula
and explicitly substitutes the definition of \(P_{L,A}(m)\).

### Detomi--Lucchini

The official publisher abstract and University of Padua record state the
quantifiers \(m\geq d(L)\) and \(P_{L,A}(m)\geq1/2\) for a group with a unique
minimal normal subgroup. Public author slides state the stronger \(53/90\)
bound in the nonabelian-socle case reached in this proof. The paper uses only
\(1/2\).

### Guralnick

The exact “Sylow \(2\)-subgroup and an involution” formulation is explicitly
attributed to Guralnick 1986 in the introduction of Burness--Guralnick 2024.
The argument needs existence for one Sylow \(2\)-subgroup; conjugacy of Sylow
subgroups then gives the statement for the chosen \(P\).

### Presentation rank

Lucchini 1990, item 2.1 on printed p. 209, states the exact soluble-normal
subgroup equality and cites Gruenberg 1976, p. 218. Lucchini 1992 supplies the
augmentation-ideal bound for arbitrary finite groups.

## Response matrix

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| R2-01 | P1 | The manuscript's crown formula uses conditional probability, while the 1998 theorem is printed in terms of Eulerian functions. | Added the printed formula and the exact normalization substitution. |
| R2-02 | P2 | The socle branch inventory must be exhaustive, not inferred from examples. | The text now says explicitly that the abelian and nonabelian branches are the exhaustive alternatives in the crown proposition. |
| R2-03 | P2 | The full Detomi--Lucchini version of record was access-restricted. | Preserved the access boundary; checked the exact statement in two official/author primary records; used only the weaker published abstract bound. |
| R2-04 | P2 | The exact Guralnick formulation required corroboration. | Added Burness--Guralnick 2024 as a precise public source for the original theorem's formulation. |
| R2-05 | P3 | Bibliographic metadata can silently attach the wrong DOI. | Crossref metadata was checked for the Kovacs--Sim, Dalla Volta--Lucchini, Detomi--Lucchini, Guralnick, Lucchini 2000, and Burness--Guralnick entries. |
| R2-06 | P3 | A negative literature search cannot establish novelty. | The manuscript and search note retain an explicit no-priority-claim boundary. |

## Classification completeness

No new classification is asserted. The proof routes a least counterexample
through the exhaustive critical-crown theorem, then eliminates its abelian
socle using a proved soluble-normal-subgroup obstruction. The remaining
nonabelian socle is a direct product of isomorphic finite nonabelian simple
groups. The only simple-group fact used thereafter is Guralnick's uniform
generation theorem; there is no omitted alternating, sporadic, classical, or
exceptional branch in the new argument.

## Verification

- Every cited acceptance-critical quantifier is transcribed in the source
  audit.
- Source PDF hashes and access states are in references/SOURCES.csv.
- Manuscript build and repository checks pass.
- No P0/P1 issue remains in this revision; Referee 2 must independently
  recheck the source-scope claims.
