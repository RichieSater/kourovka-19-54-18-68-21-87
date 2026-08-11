# Bounded reconnaissance contract

**Status:** **experimental** pilot completed; not promoted to certified
evidence.

## Question

Test the following strengthening, which would imply the target conclusion:

> If \(G\) has a family of at-most-\(d\)-generated subgroups whose indices
> have gcd 1, must some at-most-\(d\)-generated subgroup \(H\le G\) have a
> one-element generating supplement, i.e. \(G=\langle H,x\rangle\) for some
> \(x\in G\)?

Failure of this strengthening is not a counterexample to Problem 21.87.

## Declared input range

- GAP SmallGroups library;
- every group of order at most 255 for which the library and complete subgroup
  conjugacy-class enumeration are available;
- parameters \(d=1,2,3\), stopping a row once \(d\ge d(G)\) makes the target
  trivial;
- subgroup generation is checked exactly by exhaustive tuples for these small
  values, never inferred from a timed-out search.

## Required output

For each tested \((G,d)\), record one of:

- `HYPOTHESIS_FALSE` with the exact gcd;
- `SUPPLEMENT_WITNESS` with generators for \(H\), its index, and \(x\);
- `STRENGTHENING_COUNTEREXAMPLE` with the complete subgroup-class receipt;
- `UNKNOWN` if subgroup enumeration or exact generator testing is unavailable.

## Limits and stop condition

- wall-clock limit: 30 minutes;
- no group order above 255;
- stop immediately on the first reproducible counterexample to the
  strengthening, or on any fail-closed `UNKNOWN` caused by missing data;
- results remain discovery evidence and do not certify an infinite theorem.

## Pilot outcome and contract deviation

A GAP 4.15.1 / SmallGrp 1.5.4 pilot completed all SmallGroups of order at
most 255 for \(d=1,2,3\) and found no counterexample to the proposed
strengthening. However, the pilot used GAP's exact
`MinimalGeneratingSet` routine rather than the contract's promised exhaustive
tuple receipt, and it did not emit the required row-by-row witnesses. It
therefore fails the output/certification terms above and is classified only
as experimental reconnaissance. The manuscript uses none of this result.
