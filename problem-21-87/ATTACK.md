# Attack record

The user's request explicitly resumed this problem out of the default
portfolio order. The proof-draft attack, all four required internal referee
passes, and a supplemental full re-audit are complete. External specialist
review is the next evidence boundary.

## Deliverable A — reconstruct the two published proofs

- Obtain the primary papers in full where lawfully and publicly accessible;
  record any access boundary and do not rely on an unavailable proof.
- Normalize their notation and hypotheses.
- Write a dependency map for the soluble \(d+1\) proof and the arbitrary
  \(d+2\) proof.
- Identify one exact lemma or case responsible for the additional generator;
  do not begin a search based only on the abstracts.

**Gate A: passed with the disclosed access boundary.** The full Lucchini 2000
paper was unavailable and is used only for historical context; no proof step
depends on it. See `notes/04-source-audit.md`.

## Deliverable B — arithmetic and quotient kernel

- Prove the finite-subfamily reduction for the gcd.
- Prove or correct the prime-by-prime Sylow-coverage reformulation.
- Audit images of the \(d\)-generated subgroups in every quotient.
- Record the effects of Frattini quotients and direct products on both the
  hypothesis and \(d(G)\).

**Gate B: passed.** See Lemmas 2.1 and 2.2 of the manuscript.

## Deliverable C — executable finite predicate

For fixed \(G,d\):

1. enumerate or otherwise certify enough \(d\)-generated subgroup classes;
2. compute their indices and gcd;
3. independently compute or certify \(d(G)\);
4. emit the subgroup family when the hypothesis holds;
5. flag a candidate counterexample only if \(d(G)>d+1\).

The search must distinguish "no qualifying family" from "enumeration
incomplete."

**Gate C: not needed for the theorem.** No computational statement enters the
proof. A bounded pilot remained experimental and was not promoted to
evidence.

## Deliverable D — bounded reconnaissance (experimental only)

- Start with \(d=1\) and \(d=2\) in declared SmallGroups/perfect/primitive
  ranges.
- Stratify results by soluble, almost simple, affine primitive, and
  nonabelian-socle types.
- Search directly for groups requiring \(d+2\) generators while satisfying
  the hypothesis.
- Stop at the declared bounds; do not launch an unbounded enumeration.

## Deliverable E — crown and monolithic reduction

- Translate a minimal counterexample into the appropriate primitive or
  crown-based-power framework.
- Track generator numbers through the socle and quotient exactly.
- For \(N=S^k\), separate coordinate generation, top-group generation, and
  diagonal/crown multiplicity.
- Use probabilistic generation only with explicit bounds strong enough for the
  exact \(d+1\) conclusion.

## Deliverable F — close the one-generator gap

Either:

- repair the precise \(d+2\) proof step and obtain \(d+1\);
- exhibit and independently verify a counterexample; or
- reduce the question to one named primitive/crown configuration with all
  other cases proved.

Any statement weaker than those is a partial result and must be labelled as
such.

**Deliverables E--F: complete at proof-draft level.** The exact crown count,
the Detomi--Lucchini probability bound, and the Sylow-centralizer orbit count
close the gap in `paper/main.tex`.
