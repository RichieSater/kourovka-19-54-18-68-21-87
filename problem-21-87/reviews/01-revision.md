# Revision 1 — logical and structural audit

- **Base candidate:** \(b3b07ccf0c4517cdd2aece4364f906c948e238f5\)
- **Revision candidate:** pending freeze
- **Date:** 2026-08-11
- **Scope:** definitions, quantifiers, quotients, Sylow transport, minimality,
  and the coordinate-orbit argument

## Audit method

The proof was reconstructed from the exact theorem statement without using
the prose proof map. Every change of group was checked for preservation of
the same parameter \(d\), and every use of a Sylow subgroup under intersection
or projection was isolated.

## Response matrix

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| R1-01 | P2 | The initial manuscript used without an explicit lemma that a Sylow subgroup intersects a normal subgroup in a Sylow subgroup and maps onto a Sylow subgroup of a quotient. | Added Lemma 2.3 with the order calculation and cited it at both uses. |
| R1-02 | P3 | The minimal-counterexample sentence should say that \(d\) remains fixed. | The proof now selects a least-order counterexample for the fixed value of \(d\). |
| R1-03 | P3 | The arbitrary family should be reduced to a finite subfamily before invoking Lucchini's theorem. | The finite-gcd paragraph now explicitly authorizes that application. |
| R1-04 | P3 | The \(d=0\) edge case requires the family to be nonempty. | The theorem already says nonempty; the case proof was rechecked and retained. |
| R1-05 | P2 | A coordinate relation must hold for all elements of \(H\), not just the displayed generators. | Rechecked: applying the same word in each coordinate and using that \(\alpha\) is an automorphism proves the assertion. No text change needed. |
| R1-06 | P2 | The supported element must actually lie in \(H\). | Rechecked: it lies in \(T\cap A^k\), and \(T\leq H\). No text change needed. |

## Quantifier and inheritance audit

- The family is nonempty.
- The same \(d\) is used for \(G\), every image \(HN/N\), and every proper
  quotient in the minimality argument.
- No subgroup- or section-inheritance statement is used.
- The abelian-socle branch is excluded because \(A^k\) would itself be a
  nontrivial soluble normal subgroup.
- The crown coordinate projections are surjective because they contain the
  diagonal copy of \(L\).

## Verification

- Manuscript build: Tectonic 0.17.0, successful.
- LaTeX log scan: no warnings, undefined references, or overfull boxes.
- Repository check: make check, successful.
- Finite-group notation: all subgroup indices use vertical bars.

## Open items

No P0 or P1 issue was found in this author-side revision. The revised
candidate still requires a separately recorded referee pass.
