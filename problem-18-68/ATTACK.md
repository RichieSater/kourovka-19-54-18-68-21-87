# Planned attack

This plan refines Stage 2 of the root attack order. None of the tasks has been
executed.

## Deliverable A — exact property and fixtures

- Read Levchuk--Likharev and the Maslova/Revin papers in full.
- Fix the complement convention and identify any equivalent factorization
  test.
- Implement a maximal-class loop that returns an explicit complement for every
  positive class or one maximal subgroup with a certified failure.
- Validate the simple positive groups
  \(L_2(7),L_2(11),L_5(2)\) and source-backed negative simple controls.

**Gate A:** exact source pinpoints, tested product/intersection witnesses, and
fail-closed behavior when a subgroup search is incomplete.

## Deliverable B — inheritance audit

Treat separately:

1. quotients by arbitrary normal subgroups;
2. quotients by subgroups inside the Frattini subgroup;
3. normal subgroups and arbitrary sections;
4. direct products;
5. split and nonsplit extensions.

Every positive inheritance statement needs a construction of the required
complement; every failure needs a smallest practical counterexample.

**Gate B:** only after this audit may a least-order counterexample or
composition-factor reduction be formulated.

## Deliverable C — bounded reconnaissance

- Scan a declared SmallGroups/perfect-groups range.
- Scan a declared set of primitive groups with abelian and nonabelian socles.
- Record `CMP`, maximal-class witnesses, composition factors, socle, soluble
  radical, and primitive action type.
- Test the three-factor conjecture and actively search for an extension that
  violates it.

Positive verdicts require exhaustive maximal-class coverage and exhaustive
complement search within the declared group. Negative verdicts require one
verified maximal subgroup with no complement, plus a transparent completeness
argument for the candidate complement orders/classes.

## Deliverable D — primitive/monolithic reduction

- Use the inheritance audit to choose the correct minimal object.
- Separate affine primitive groups from groups with socle \(S^k\).
- For nonabelian socle, classify maximal subgroups by top, product, and
  diagonal behavior only after checking whether the 10.34 trichotomy applies
  to the exact ambient group.
- Track how an arbitrary nonabelian composition factor appears through the
  normal series; do not replace composition-factor control with socle control.

## Deliverable E — extension and cohomology layer

- Identify the precise complement theorem required in each primitive case.
- If using \(H^1\), specify module, acting group, and whether the result proves
  existence, conjugacy, or counts complements.
- Treat nonsplit extensions explicitly; a scan of split semidirect products is
  not exhaustive evidence.

## Deliverable F — classification closeout

If the working conjecture survives, produce a section-safe proof that every
nonabelian composition factor is one of the three simple groups. If it fails,
record the smallest explicit counterexample and revise the target before any
CFSG-wide campaign.
