# Planned attack

This plan refines Stage 1 of the root attack order. None of the tasks has been
executed.

## Deliverable A — definition kernel

- Implement two independent predicates on finite groups:
  1. cover-based strictness for every weak second-maximal subgroup;
  2. exclusion of simultaneous 2-maximal and \(m\)-maximal chains.
- Prove their equivalence in prose and make the implementations agree on all
  fixtures.
- Represent subgroup embeddings and overgroups explicitly; abstract subgroup
  isomorphism types alone are insufficient.

**Gate A:** positive fixtures
\(C_3^2:C_8,U_3(2),U_3(3),L_2(17)\) and negative fixtures
\(S_4,L_2(8),A_6\) have source-backed expected behavior. Any correction to
that provisional fixture list must be recorded, not hidden.

## Deliverable B — soluble baseline

- Reconstruct the Meng--Guo theorem and the definition of strongly
  irreducible modules.
- Create small soluble examples covering Frattini chief factors,
  non-Frattini one-dimensional factors, and higher-dimensional irreducible
  factors that restrict reducibly to a maximal subgroup.
- State exactly what the theorem says about chief factors and what it leaves
  unconstrained.

**Gate B:** a written proof map with exact theorem/lemma citations and finite
regression examples.

## Deliverable C — bounded subgroup-lattice scan

- Declare a feasible SmallGroups range and a separate list of simple/almost
  simple groups.
- Enumerate conjugacy classes of subgroups and cover relations with embedding
  information.
- For a negative group, emit \(H<M<G\) together with an alternative maximal
  overgroup \(X\) in which \(H\) is not maximal.
- For a positive group, emit an exhaustive coverage receipt for all weak
  second-maximal classes.

**Gate C:** rerunnable certificates, exact GAP/package versions, independent
checker, and mutation tests for a deliberately omitted overgroup.

## Deliverable D — minimal nonsoluble reduction

Attempt, in this order:

1. quotient behavior;
2. soluble radical and Frattini reductions;
3. number and type of minimal normal subgroups;
4. primitive or monolithic reduction;
5. socle \(S^k\) and induced coordinate action.

Each failed inheritance step becomes a named obstruction with an explicit
example. Do not skip to \(S^k\) merely because that template worked for
Problem 10.34.

## Deliverable E — simple and almost-simple frontier

- Start from published subgroup lattices for low-degree almost-simple groups.
- Seek a reusable local obstruction: one subgroup lying immediately below one
  maximal class but at depth at least two below another.
- Split the CFSG audit into alternating, sporadic/Tits, classical, and
  exceptional families.
- Use computation for discovery and finite cases; require exhaustive published
  maximal-overgroup data for positive classifications.

## Deliverable F — chief-factor synthesis

Combine the soluble module theorem with the nonsoluble reduction. A final
answer must state both allowed abstract chief factors and any required action
conditions. If only nonabelian chief factors are classified, label that as a
partial answer rather than silently dropping the abelian question.
