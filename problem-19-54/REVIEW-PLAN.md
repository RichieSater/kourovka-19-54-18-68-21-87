# Problem 19.54 solution and review plan

**Current stage:** initial solution not started.
**Generic protocol:**
[`../docs/SOLUTION-REVIEW-WORKFLOW.md`](../docs/SOLUTION-REVIEW-WORKFLOW.md)

## Milestones

| Milestone | Status | Required focus | Artifact |
|---|---|---|---|
| Initial solution | not started | Full chief-factor answer; definitions; soluble baseline; nonsoluble reduction | `reviews/00-initial-solution.md` |
| Revision 1 | not started | Repair definition, quotient, inheritance, and monolithic-reduction gaps | `reviews/01-revision.md` |
| Referee 1 | not started | Independent logical/structural audit | `reviews/01-referee.md` |
| Revision 2 | not started | Complete simple/almost-simple and CFSG source coverage | `reviews/02-revision.md` |
| Referee 2 | not started | Independent family, overgroup, and source audit | `reviews/02-referee.md` |
| Revision 3 | not started | Embedding-aware certificates and reproducibility hardening | `reviews/03-revision.md` |
| Referee 3 | not started | Fresh-clone subgroup-lattice and mutation audit | `reviews/03-referee.md` |
| Revision 4 | not started | Final chief-factor synthesis, exposition, credit, and release candidate | `reviews/04-revision.md` |
| Referee 4 | not started | Hard-final theorem/source/certificate pass | `reviews/04-referee.md` |

## Initial-solution instructions

The candidate must answer the chief-factor question, not merely list simple
WSM-groups. It must reconcile all second-maximal terminology, reproduce the
soluble strongly-irreducible theorem, prove every inheritance step used in a
nonsoluble reduction, and distinguish Frattini/non-Frattini and
abelian/nonabelian factors. Positive simple cases require exhaustive
maximal-overgroup evidence.

## Four review rounds

1. **Structural:** try to destroy quotient inheritance and every path to a
   monolithic socle; search small counterexamples to each lemma.
2. **Classification:** independently rebuild all maximal-overgroup families,
   outer fusions, low exceptions, and positive exhaustive lists.
3. **Computation:** require embedding-aware witnesses, complete positive
   coverage, fresh reproduction, and failure when an overgroup is omitted.
4. **Hard final:** verify that the final theorem really describes all chief
   factors and actions claimed, and that no soluble/nonsoluble interface is
   hidden behind shorthand.

No milestone may move to `complete` solely because GAP agrees on a finite
range.
