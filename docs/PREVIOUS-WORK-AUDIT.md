# Previous group-theory work audit

## Purpose

The three new problems were selected because they overlap with completed work
on maximal subgroups, maximal chains, subgroup products, and nonabelian socles.
This document records what is actually reusable and what must be reproved.

## `kourovka-10-34`

### Reusable assets

- The minimal-counterexample workflow: quotient inheritance first, then the
  soluble radical, uniqueness of a minimal normal subgroup, a socle \(S^k\),
  coordinate transitivity, and an ambient wreath product.
- The separation between exploratory GAP, proof-path certificates, independent
  arithmetic checkers, formal coverage, and external classification inputs.
- Fail-closed manifests and source maps:
  `CLASSIFICATION-MANIFEST.json`, `LIE-SOURCE-MAP.csv`,
  `MAXIMALITY-SOURCE-MAP.csv`, `ORDER-FORMULA-SOURCE-MAP.csv`, and
  `EXCEPTION-MANIFEST.json`.
- The proof-engineering lesson that product-type "novelty" maximals can appear
  after outer automorphisms fuse simple-group maximal classes.
- Uniform CFSG family organization and finite exception routing.

### Do not import blindly

- Property 10.34 passes to quotients; that fact is specific to the subgroup
  product condition and does not establish inheritance for any new property.
- Its normalizer/divisibility obstruction depends on exact subgroup-product
  orders. It is an analogy, not a ready-made lemma for 19.54, 18.68, or 21.87.
- The historical workspace `../Math/kourovka-10.34` contains superseded
  exploratory claims. Prefer the public `../kourovka-10-34` release when
  citing a result.

## `kourovka-19-57-19-58`

### Reusable assets

- A compact, tested pattern for scanning every listed maximal character table
  and refusing to interpret missing `Maxes` data as a negative result.
- Separation of one-witness exclusions from positive rows requiring exhaustive
  maximal-subgroup classification.
- Family-by-family proof obligations for alternating, sporadic, classical,
  and exceptional simple groups.
- The use of exact software versions, deterministic TSVs, producer commands,
  and regression tests.
- A mature claim-audit culture in `notes/11-proof-obligations.md` and the
  successive referee reports.

### Do not import blindly

- Character tables can test normal subgroup orders but cannot recover the full
  subgroup-overgroup geometry required by Problem 19.54.
- A maximal subgroup being simple or \(p\)-nilpotent is a property of one
  subgroup. Having a complement is an existential factorization inside its
  ambient group and needs different data.
- The published simple-factor classification for 19.57/19.58 does not imply
  either of the new classifications.

## `monotone-maximal-chains`

### Reusable assets

- The representation of an unrefinable subgroup chain by cover relations and
  index-labelled edges.
- Recursive, witness-producing search over conjugacy classes of maximal
  subgroups (`src/mmc.g`).
- The use of nested maximal-index spectra and explicit negative controls.
- A concise claim ledger linking each mathematical statement to an independent
  computational check.

### Do not import blindly

- `MMCLast` tracks the least possible final index of a monotone chain; it does
  not decide whether every 2-maximal subgroup is strict.
- Problem 19.54 requires all maximal overgroups of each weak second-maximal
  subgroup. A class representative without fusion/embedding information may
  be insufficient.
- The monotone-chain counterexample is soluble and does not directly constrain
  nonabelian chief factors.

## Reuse matrix

| Asset | 19.54 | 18.68 | 21.87 |
|---|---:|---:|---:|
| subgroup cover graph | high | low | low |
| maximal-class exhaustive audit | high | high | medium |
| subgroup-product/factorization checks | low | high | low |
| index arithmetic | medium | medium | high |
| minimal-counterexample/socle template | high | high | high |
| CFSG family/source maps | high | high | medium |
| extension/cohomology machinery | medium | high | medium |
| crown/generation theory | low | low | high |

## Architectural conclusion

One umbrella repository is appropriate because provenance, software pinning,
simple-group inventories, and evidence schemas can be shared. Separate problem
directories are mandatory because the mathematical predicates and their
inheritance behavior are different. A shared executable predicate is expressly
out of scope.
