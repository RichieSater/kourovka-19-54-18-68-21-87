# Manuscript build

`main.tex` is the peer-review draft answering Kourovka Problem 21.87.

Build from this directory with the pinned command used for the candidate:

```sh
tectonic --keep-logs --keep-intermediates main.tex
```

The proof is prose-only and uses no computer calculation. The PDF is a build
artifact and is not committed; reviewers should regenerate it from the source.
Tectonic 0.17.0 was used on 2026-08-11.
