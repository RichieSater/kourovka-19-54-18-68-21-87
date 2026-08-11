# Problem 10.34 — retrospective lifecycle mapping

## Status boundary

The local `../kourovka-10-34` repository claims a complete negative solution
and publicly releases it as arXiv:2608.02970 and GitHub/Zenodo release
`v1.0.8`. Its README explicitly says that the manuscript is a public preprint,
has not been accepted through journal peer review, and has not received
independent end-to-end certification.

The four rounds below map historical work to the new lifecycle. The old
project did not use these exact round names.

## Initial solution

- `98eb1a2` — paper, GAP certificates, and receipts.
- Outcome: complete claimed theorem at proof-draft level.

## Round 1 — first adversarial correction

- Revision: `2a23897`, addressing v1.0.1 audit findings and two overclaims.
- Pass evidence: `6dd8c5e`, final adversarial-pass fixes and release
  preparation.

## Round 2 — proof-audit and formalization

- Revision: `770399c` and `2b2d5a5`, adversarial fixes, binary gates, Lean
  coverage, and fail-closed evidence.
- Pass evidence: `c9da1c`, closure of proof-audit, literature-priority, and
  clean-room gates under the recorded amendment.

## Round 3 — clean-room assurance

- Revision: `393f70f`, audit-driven manuscript repairs and revised audit
  bundle.
- Pass evidence: `d6b51c8`, clean-room assurance attestation for v1.0.7.

## Round 4 — final reproducibility and language audit

- Revision: `5cf0b27` and `6f61a7c`, reproducibility repairs, submission
  copyedits, and a second-reviewer English audit.
- Pass/release evidence: `35942dc`, immutable public release `v1.0.8` and the
  current explicit review boundary.

## Remaining external gate

External specialist refereeing and journal acceptance remain outstanding. The
tracker must not translate `complete_legacy` into "established theorem."
