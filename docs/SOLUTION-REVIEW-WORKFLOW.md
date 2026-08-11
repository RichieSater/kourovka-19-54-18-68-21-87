# Initial solution and four-round review workflow

This protocol applies to every tracked problem. Problems 19.57 and 19.58 share
one manuscript and therefore share review artifacts, but retain separate rows
in the portfolio tracker.

## Roles and independence

- **Solution author:** develops the initial theorem, proof, computations, and
  manuscript.
- **Revision author:** answers every open referee item without rewriting the
  historical report.
- **Referee:** starts from the frozen candidate, checks the full theorem rather
  than only the response, and issues an independent verdict.

One person or system may perform multiple roles at different times, but every
referee pass must use a fresh checklist and must not treat prior agreement as
evidence. External specialist peer review is tracked separately and can never
be replaced by these internal passes.

## Milestone states

Allowed tracker states are:

- `not_started`
- `in_progress`
- `revision_required`
- `blocked`
- `complete`
- `complete_legacy`

Each milestone transition must name a commit and an artifact. `blocked` must
name the missing source, theorem, computation, or external action.

## Milestone 0 — initial solution candidate

### Instructions

1. Freeze the exact problem statement, notation, and claimed scope.
2. Repeat the literature/priority search and record queries and limits.
3. State the answer as a theorem or an explicit counterexample.
4. Build a dependency graph from elementary reductions through every external
   classification input.
5. Put every nontrivial assertion in the claim ledger with an evidence label.
6. Separate published inputs, prose proofs, finite certificates, exploratory
   computation, and conjecture.
7. Supply a complete manuscript draft, source ledger, assumptions ledger,
   reproducibility instructions, and all proof-path tests.
8. Run the documented suite from the development tree and record results.
9. Freeze a candidate commit before starting round 1.

### Exit gate

- The result is complete at proof-draft level; no known step is intentionally
  deferred.
- Every positive classification has an exhaustive source or proof.
- Every negative family has a valid uniform obstruction or complete finite
  certificate.
- The README and abstract state the same scope and confidence level.

Use [`templates/INITIAL-SOLUTION.md`](../templates/INITIAL-SOLUTION.md).

## Round 1 — logical and structural revision, then referee pass

### Revision 1 instructions

- Reprove definition equivalences and audit all quantifiers.
- Attack quotient, section, subgroup, direct-product, and extension claims.
- Stress-test the minimal-counterexample reduction and socle transition.
- Search for small counterexamples to every inheritance lemma.
- Remove circular uses of the target theorem and implicit CFSG assumptions.
- Produce a response matrix even if the initial author found no issue.

### Referee pass 1 instructions

- Read the frozen candidate as a hostile but fair correctness referee.
- Check the theorem statement against the Notebook and the proof against the
  claim ledger.
- Reconstruct all structural reductions independently.
- Validate named counterexamples/witnesses and sample edge cases.
- Issue one verdict: `reject`, `major revision`, `minor revision`, or `pass`.
- Assign stable issue IDs with severity `P0` (fatal), `P1` (acceptance-level),
  `P2` (important), or `P3` (editorial).

**Pass gate:** no open P0/P1 logical or structural issue.

## Round 2 — classification and source revision, then referee pass

### Revision 2 instructions

- Audit the completeness of every simple-group, maximal-subgroup, module, or
  primitive-group classification used.
- Replace broad citations with theorem/table/page pinpoints.
- Separate positive exhaustive burdens from one-witness negative burdens.
- Route low parameters, exceptional isomorphisms, Zsigmondy exceptions, and
  outer-automorphism fusion explicitly.
- Verify credit, chronology, and dependence on prior authors' results.

### Referee pass 2 instructions

- Repeat the family inventory without trusting the author's partition.
- Inspect the original source text for every acceptance-critical quantifier.
- Check that all exceptions land in a proved finite case.
- Repeat a current ten-angle literature/citation search.
- Recheck the full revised theorem, not only the response to pass 1.

**Pass gate:** no missing family, source-scope mismatch, unhandled exception,
or unsupported novelty statement.

## Round 3 — computational and reproducibility revision, then referee pass

### Revision 3 instructions

- Pin software, package, database, and source versions with hashes.
- Make all property checks fail closed on missing data.
- Separate discovery output from proof certificates.
- Add independent parsers/checkers, negative controls, and mutation tests.
- Bind every manuscript finite claim to a certificate row and producer.
- Provide quick and full verification commands and a clean-environment recipe.

### Referee pass 3 instructions

- Reproduce the proof-path suite from a fresh clone and isolated environment.
- Confirm committed outputs match regenerated outputs.
- Audit group inventories and coverage counts independently.
- Deliberately corrupt representative inputs and verify failure detection.
- Check the interfaces between prose, GAP, Python, and any formal proof layer.

**Pass gate:** clean reproduction succeeds, omissions fail closed, and no
machine result is asked to prove more than its declared scope.

## Round 4 — hard-final revision, then referee pass

### Revision 4 instructions

- Resolve every remaining issue from passes 1--3 in an itemized disposition.
- Perform a theorem-by-theorem consistency and notation audit.
- Tighten abstract, title, README, credit, AI disclosure, limitations, and
  publication-status language.
- Recheck bibliography, source checksums, manifests, links, PDF rendering, and
  release metadata.
- Freeze the exact release candidate and rerun the full suite.

### Referee pass 4 instructions

- Start from the release candidate, not the working tree used for revision.
- Recheck every acceptance-critical theorem and every previously closed P0/P1
  issue.
- Perform a final source-scope, exception-routing, clean-run, and manuscript-
  certificate audit.
- State explicitly what was not checked and what remains trusted.
- Recommend one of: `do not circulate`, `major revision`, `minor corrections`,
  or `circulate for external specialist review`.

**Pass gate:** no open P0/P1 issue, all tests and release checks pass, and the
status language distinguishes a claimed complete solution from an externally
established theorem.

## Required artifact names

Each active problem's `reviews/` directory should contain, when created:

```text
00-initial-solution.md
01-revision.md
01-referee.md
02-revision.md
02-referee.md
03-revision.md
03-referee.md
04-revision.md
04-referee.md
```

Reports are append-only historical records. Later revisions may supersede a
verdict, but must not silently edit the old report to make it favorable.
