# Problem 21.87 solution and review plan

**Current stage:** Revision 3 complete; Referee 3 not started.
**Generic protocol:**
[`../docs/SOLUTION-REVIEW-WORKFLOW.md`](../docs/SOLUTION-REVIEW-WORKFLOW.md)

## Milestones

| Milestone | Status | Required focus | Artifact |
|---|---|---|---|
| Initial solution | complete | Exact \(d+1\) proof or explicit counterexample | `reviews/00-initial-solution.md`; `b3b07cc` |
| Revision 1 | complete | Published-proof reconstruction, gcd/Sylow and quotient kernel | `reviews/01-revision.md`; `671b5c4` |
| Referee 1 | complete | Independent logical and generator-bound audit | `reviews/01-referee.md`; pass on `671b5c4` |
| Revision 2 | complete | Primitive, monolithic, and crown-based-power completeness | `reviews/02-revision.md`; `ec734ae` |
| Referee 2 | complete | Independent generation-theory/source audit | `reviews/02-referee.md`; pass on `ec734ae` |
| Revision 3 | complete | Certified subgroup families and \(d(G)\) lower bounds | `reviews/03-revision.md`; `8ba6bc2` |
| Referee 3 | not started | Fresh-clone enumeration and mutation audit | `reviews/03-referee.md` |
| Revision 4 | not started | Exact one-generator-gap closeout and release candidate | `reviews/04-revision.md` |
| Referee 4 | not started | Hard-final theorem/source/certificate pass | `reviews/04-referee.md` |

## Initial-solution instructions

The candidate must reconstruct the Kovacs--Sim \(d+1\) proof and Lucchini
\(d+2\) proof, identify precisely where the extra generator appears, and then
close that step or give a verified counterexample. It must keep the same
parameter \(d\) through all quotients and crowns, prove the gcd/Sylow
reformulation, and distinguish an actual generator lower bound from a failed
search for a smaller generating set.

The manuscript supplies a complete affirmative proof without using the
exploratory computation. Candidate commit `b3b07cc` is frozen for Revision 1.

## Four review rounds

1. **Logical/generation kernel:** attack terminology, prime-by-prime coverage,
   quotient images, and the exact lower-bound argument for \(d(G)\).
2. **Crown/classification:** independently audit all primitive types,
   nonabelian direct powers, crown multiplicity, and probabilistic inputs.
3. **Computation:** require explicit subgroup-family certificates, independent
   gcd arithmetic, certified generator lower bounds, and incomplete-search
   `UNKNOWN` states.
4. **Hard final:** verify that the theorem is exactly \(d+1\) for arbitrary
   finite groups, not \(d+2\), fixed small \(d\), or only a primitive case.

No milestone may move to `complete` because a generator search timed out or
failed to find a smaller set.
