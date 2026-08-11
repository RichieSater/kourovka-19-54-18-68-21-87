# Referee pass 1 — logical and structural correctness

- **Frozen candidate reviewed:** 671b5c45d2bed165a9efb8ec58167b0c8f834fdd
- **Review date:** 2026-08-11
- **Role boundary:** internal adversarial review; not external specialist peer
  review
- **Verdict:** **pass**

## Scope

This pass checked the theorem against the Notebook statement, reconstructed
the elementary reductions, followed every quantifier in the
minimal-counterexample argument, and audited the two coordinate-orbit claims.
The CFSG-dependent source theorems were treated as stated published inputs;
their source scope is the focus of Referee 2.

## Independent reconstruction

1. The gcd condition gives, for every \(p\mid |G|\), an
   at-most-\(d\)-generated subgroup containing a Sylow \(p\)-subgroup.
2. Images in \(G/N\) remain at most \(d\)-generated and their indices divide
   the original indices, so the same hypothesis holds with the same \(d\).
3. For a least counterexample and \(m=d+1\), every proper quotient is
   \(m\)-generated. The augmentation-ideal bound forces positive presentation
   rank; Gruenberg's result eliminates nontrivial soluble normal subgroups.
4. The critical crown therefore has nonabelian socle and its monolithic base
   \(L\) is a proper quotient, so \(m\geq d(L)\).
5. The exact crown formula and conditional probability bound give the stated
   lower bound for \(k\).
6. If two coordinate tuples were in one \(\Gamma_{L,A}\)-orbit, the induced
   coordinate identity would hold for every word in the generators of \(H\).
   A nonidentity element supported in one coordinate of
   \(T\cap A^k\leq H\) contradicts it.
7. Tuple stabilizers fix the projected Sylow \(2\)-subgroups pointwise. The
   monolithic centralizer estimate therefore gives the orbit-size lower bound
   and the incompatible upper bound for \(k\).

## Edge and mutation checks

- \(d=0\): nonemptiness of the family forces every member to be trivial, and
  gcd one forces \(G=1\).
- Replacing “divides” by “is divisible by” in the quotient-index step breaks
  the gcd implication; the manuscript has the correct direction.
- Allowing the coordinate automorphism to depend on a word would break the
  orbit argument; the manuscript fixes one \(\alpha\) for the generating
  tuples, so the word extension is valid.
- Omitting \(T\leq H\) would break the supported-element argument; that
  containment is supplied by Sylow coverage and stated explicitly.
- If the socle were abelian, the orbit count would not apply; the proof
  excludes that branch before the count.

## Issues

| ID | Severity | Observation | Status |
|---|---|---|---|
| F1-01 | P3 | The proof relies on standard Sylow transport under a normal subgroup and quotient. | Closed by the explicit Lemma 2.3 in Revision 1. |
| F1-02 | P3 | The exact source scope of the Detomi--Lucchini probability bound must be rechecked in the source round. | Deferred to Revision/Referee 2; not a logical defect in the stated deduction. |
| F1-03 | P3 | The full Lucchini 2000 proof is unavailable. | Not acceptance-critical because only its historical \(d+2\) result is cited. |

No P0 or P1 logical or structural issue remains.

## Verdict rationale

The conclusion follows from the five declared published inputs with no
quantifier shift, circular use of the target theorem, or unsupported
inheritance step. The logical/structural pass gate is satisfied. This verdict
does not certify the CFSG inputs, priority search, typesetting, or external
acceptance.
