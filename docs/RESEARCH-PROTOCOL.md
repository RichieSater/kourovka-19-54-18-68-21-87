# Research and evidence protocol

## Evidence labels

Every nontrivial entry in a claim ledger must use one of these labels:

- **proved** — a complete argument is present in the repository.
- **published input** — an exact theorem is cited with a pinpoint location.
- **computationally certified** — a finite statement is reproduced by pinned,
  fail-closed code and a committed certificate.
- **experimental** — observed in a search whose coverage is not proof-level.
- **conjectural** — a proposed statement with no complete proof.
- **unchecked** — a task or recollection that has not been validated.

"Known" is not an evidence label.

## Claim workflow

1. Put the statement in the problem's `CLAIM-LEDGER.md` before building on it.
2. State its quantifiers and whether it concerns groups, pairs, subgroup
   classes, embeddings, sections, or families.
3. Attach either a proof path, a primary-source pinpoint, or a producer command.
4. Add an adversarial test or named failure mode.
5. Promote the evidence label only after the attached material is reviewed.

## Computational workflow

1. Start with an explicit finite range and stop condition.
2. Make verdicts witness-producing where possible.
3. A positive universal property must enumerate the entire relevant domain.
4. Missing library data produce `UNKNOWN`/failure, never `false` or `true`.
5. Keep discovery output separate from proof certificates.
6. Record versions, commands, hashes, and expected summary lines.
7. Add mutation or negative-control tests before a certificate becomes
   proof-essential.

## Classification workflow

- Organize simple groups by alternating, sporadic/Tits, classical, and
  exceptional families.
- Record exact maximal-subgroup classification sources and theorem/table rows.
- Distinguish the existence of a useful subgroup from the exhaustiveness of a
  positive list.
- Maintain explicit low-parameter and accidental-isomorphism routing.
- Never promote a character-table observation to a subgroup-lattice theorem
  without a bridge.

## Literature workflow

- Search exact problem number, exact statement, proposers, foundational paper
  titles, citations to those papers, and likely equivalent terminology.
- Record the search date, queries, databases, and access limits.
- Prefer primary papers, publisher records, arXiv, MathNet, and official
  Notebook editions.
- Repeat the search immediately before claiming novelty or submitting a paper.

## Public-repository rule

Tracked files must be safe to publish. Do not commit private correspondence,
access tokens, copyrighted source PDFs without permission, or informal claims
attributed to individuals without a public source.
