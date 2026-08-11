# Attack order

## Decision

Work in the following order:

1. **Problem 19.54** as the primary project.
2. **Problem 18.68** after the 19.54 structural baseline is stable.
3. **Problem 21.87** after reconstructing its existing \(d+2\) argument and
   only after the first two projects have reusable monolithic-group tooling.

This order follows mathematical fit, not the numerical order of the Notebook.
Problem 19.54 is closest to the completed maximal-chain project; Problem
18.68 next reuses the maximal-subgroup and simple-factor audit discipline of
Problems 10.34 and 19.57/19.58; Problem 21.87 has the largest amount of new
generation/crown theory.

No phase below has begun. Every item is a planned work package, not a claimed
lemma.

## Stage 0 — common baseline

Complete once, before attacking any problem:

1. Freeze the exact Notebook statement and terminology.
2. Recheck current solution status and prior art with a dated, reproducible
   search; do not infer openness merely from the Notebook.
3. Pin GAP, CTblLib, AtlasRep, and any subgroup-lattice datasets before a
   certificate is promoted beyond exploration.
4. Establish a fail-closed result schema shared only at the metadata level:
   group identifier, software/source version, property verdict, witness or
   exhaustive-coverage receipt, and evidence label.
5. Keep each mathematical property in its own implementation. Shared code may
   handle logging, hashes, and group inventories, but not silently encode a
   problem-specific predicate.

**Gate 0:** the source ledger, definitions, property tests, and known-example
fixtures for the selected problem all pass review.

## Stage 1 — Problem 19.54

### 1A. Normalize the condition

- Reconcile the Notebook's `m`-maximal definition with the weak-second,
  second-maximal, and strictly-2-maximal terminology.
- Prove or cite every equivalence used by the implementation.
- Audit behavior under quotients, direct products, subgroups, and extensions;
  record failures as carefully as positive inheritance results.

### 1B. Reproduce the soluble theorem

- Reconstruct Meng--Guo's characterization of soluble WSM-groups by strongly
  irreducible non-Frattini chief factors.
- Turn the proof into a claim ledger that identifies exactly what remains when
  solubility is removed.
- Validate the definitions against supersoluble groups,
  \(C_3^2:C_8\), \(U_3(2)\), \(U_3(3)\), \(L_2(17)\), and explicit negative
  controls.

### 1C. Build the finite reconnaissance layer

- Enumerate subgroup-conjugacy classes and cover relations, not just maximal
  subgroup orders.
- Produce a positive verdict only after all relevant overgroups of every
  2-maximal class are exhausted.
- Search soluble groups first as a regression suite, then simple and almost
  simple groups within a declared finite range.

### 1D. Structural reduction

- Attempt a minimal nonsoluble/least-order reduction.
- Determine whether the condition passes far enough to force a monolithic or
  primitive quotient and a socle \(S^k\).
- Separate assertions about the group from assertions about an individual
  chief factor.

### 1E. Classification and synthesis

- Classify viable simple and almost-simple sections using published exhaustive
  maximal-subgroup data plus finite certificates.
- Treat alternating, sporadic, classical, and exceptional families in
  separate audit rows.
- State the chief-factor answer only after Frattini and non-Frattini factors,
  abelian and nonabelian factors, and extension effects are all accounted for.

**Exit gate for Stage 1:** either a complete proof with an external-source
map, a rigorous counterexample narrowing the question, or a written blocker
that identifies one precise unresolved family/extension lemma. Do not slide an
unchecked classification table into a theorem.

## Stage 2 — Problem 18.68

### 2A. Property audit

- Fix the complement convention and distinguish it from the Hall-maximal
  property.
- Determine exactly which quotient, extension, and section operations preserve
  "every maximal subgroup has a complement."
- Reproduce the simple-group baseline
  \(L_2(7),L_2(11),L_5(2)\) from the cited classification.

### 2B. Bounded computational test

- Implement a witness-producing complement test for maximal-subgroup classes.
- Scan a declared finite range of nonsoluble groups and primitive groups.
- Record nonabelian composition factors and test, without assuming, the
  candidate containment
  \[
  \operatorname{Comp}_{\rm nab}(G)\subseteq
  \{L_2(7),L_2(11),L_5(2)\}.
  \]

### 2C. Minimal-counterexample and extension analysis

- Reduce to primitive/monolithic configurations only after inheritance is
  proved.
- Split abelian-socle and nonabelian-socle cases.
- Isolate where complement existence or conjugacy is controlled by extension
  theory and \(H^1\); cite the exact theorem used.

### 2D. Simple-factor classification

- Reuse the CFSG family ledger and source-map discipline from Problems 10.34
  and 19.57/19.58.
- Do not replace an extension argument by checking the simple quotient alone.

**Exit gate for Stage 2:** a section-safe reduction plus a complete list, or a
minimal explicit obstruction showing why the three-group conjecture needs
revision.

## Stage 3 — Problem 21.87

### 3A. Reconstruct the known bounds

- Write a self-contained notation layer for \(d(G)\) and the family of
  \(d\)-generated subgroups.
- Reproduce Kovacs--Sim's soluble \(d+1\) theorem and Lucchini's arbitrary
  \(d+2\) theorem from primary sources.
- Locate the exact step at which the extra generator enters.

### 3B. Reformulate the hypothesis

- Compare the gcd-of-indices formulation with prime-by-prime Sylow coverage.
- Prove all quotient and lifting statements before using minimality.
- Specify whether `d-generator` means generated by at most \(d\) elements; do
  not let implementation conventions decide the mathematics.

### 3C. Small and primitive reconnaissance

- Compute \(d(G)\), candidate subgroups, and index gcds for a bounded library
  range.
- Search first for a \(d+2\)-generated counterexample satisfying the
  hypothesis; retain explicit subgroup families as certificates.
- Examine simple, almost-simple, affine primitive, and product-action cases
  separately.

### 3D. Crown/monolithic analysis

- Translate a minimal counterexample into the appropriate crown-based-power or
  unique-minimal-normal framework.
- Reuse only the socle bookkeeping from earlier projects; generation
  probabilities and crown multiplicities require their own proofs.
- Determine whether the remaining one-generator gap is almost-simple or
  genuinely product-action/crown-theoretic.

**Exit gate for Stage 3:** a proof of the \(d+1\) bound, an explicit
counterexample, or a sharp reduction naming the only unresolved primitive
type.

## Scheduling rule

Do not run all three as open-ended searches. Work on one primary stage at a
time. A bounded side experiment is allowed only if its input range, expected
witness, resource limit, and stop condition are written first in that
problem's `notes/` directory.
