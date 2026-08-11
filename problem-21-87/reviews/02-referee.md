# Referee pass 2 — classification and source scope

- **Frozen candidate reviewed:** ec734ae960cfe1b408b625f6ecf05e738c793d40
- **Review date:** 2026-08-11
- **Role boundary:** internal source audit; not external specialist peer review
- **Verdict:** **pass**

## Independent source inventory

The proof has five acceptance-critical published inputs:

1. Lucchini's augmentation-ideal bound.
2. Gruenberg's soluble-normal-subgroup theorem at positive presentation rank.
3. Dalla Volta--Lucchini's critical crown reduction and exact multiplicity.
4. Detomi--Lucchini's uniform conditional generation bound.
5. Guralnick's Sylow \(2\)-subgroup plus involution theorem.

No other classification, primitive-group list, character table, maximal
subgroup table, or computational database is used.

## Original-source checks

- **Lucchini 1992:** Theorem 2 has the family-of-indices hypothesis at the
  augmentation-ideal level; Proposition 2 supplies the one-prime local step.
  A \(d\)-generated subgroup has a \(d\)-generated augmentation ideal, so the
  manuscript's use matches the source.
- **Lucchini 1990 / Gruenberg 1976:** item 2.1 says precisely that if
  \(N\unlhd G\) is soluble and \(\operatorname{pr}(G)>0\), then
  \(d(G)=d(G/N)\).
- **Dalla Volta--Lucchini 1998:** Theorem 1.4 permits \(m=2\), uses
  \(d(X/N)\leq m\), and yields the stated critical crown. Theorem 2.7 permits
  \(m=d(L)\). In the nonabelian branch its Eulerian-function formula becomes
  the manuscript's probability formula after multiplication by \(|A|^m\).
- **Detomi--Lucchini 2013:** the official abstract states
  \(P_{L,A}(m)\geq1/2\) when \(m\geq d(L)\). The public author slides give the
  stronger nonabelian-socle bound \(53/90\), so the manuscript does not
  overstate the accessible record.
- **Guralnick 1986:** Burness--Guralnick 2024 explicitly records the exact
  formulation used. Conjugacy of Sylow subgroups permits the chosen
  \(P\), rather than only one unspecified Sylow subgroup.

## Exhaustiveness audit

The critical-crown theorem is itself exhaustive for the
minimal-counterexample hypothesis. Its socle alternatives are abelian
complemented or nonabelian. The first is eliminated because \(A^k\) would be
a nontrivial soluble normal subgroup. A nonabelian minimal normal subgroup is
a direct product of isomorphic nonabelian simple groups, and the centralizer
lemma applies uniformly to every simple factor. Thus there is no unhandled
O'Nan--Scott type or CFSG family.

## Literature refresh

Exact-problem, exact-title, structural-phrase, author, and forward-citation
queries were repeated. The July 2026 Notebook still states the problem;
OpenAlex and Google Scholar citation lists exposed no paper claiming the
conclusion. This remains a limited negative search and is not evidence of
priority.

## Issues

| ID | Severity | Observation | Status |
|---|---|---|---|
| F2-01 | P1 | The 1998 formula could be misnormalized when translated from \(\phi_L\) to \(P_{L,A}\). | Closed: Revision 2 prints both formulas and the substitution. |
| F2-02 | P2 | Full access to the Detomi--Lucchini version of record was unavailable. | Accepted as a transparent trust boundary: the exact theorem is in the official abstract and a stronger form is in public author slides. |
| F2-03 | P2 | A secondary citation alone must not silently replace Guralnick's original credit. | Closed: the manuscript cites the original and uses the later paper only to corroborate the formulation. |
| F2-04 | P3 | Search results cannot support a novelty claim. | Closed: no such claim is made. |

No missing family, source-scope mismatch, unhandled parameter, or open P0/P1
issue remains.

## Verdict rationale

The classification and source pass gate is satisfied. The deduction uses each
published result within its stated quantifiers, and the access limitations are
disclosed rather than hidden. The referee does not independently reprove the
CFSG-dependent published theorems.
