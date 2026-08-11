# Manuscript build

`main.tex` is the peer-review draft answering Kourovka Problem 21.87.
The revised submission source, incorporating all four items in the
independently supplied minor-revision report, is frozen at
[`dec0db6701228d2e9db8ec3065f4e0b1fdd98d38`](https://github.com/RichieSater/kourovka-19-54-18-68-21-87/tree/dec0db6701228d2e9db8ec3065f4e0b1fdd98d38/problem-21-87/paper).

Build from this directory with the pinned wrapper used for the candidate:

```sh
./build.sh
```

The proof is prose-only and uses no computer calculation. The PDF is a build
artifact and is not committed; reviewers should regenerate it from the source.
The wrapper requires Tectonic 0.17.0, rejects LaTeX diagnostics, and confirms
that the generated PDF has a readable, nonzero page count.

## Repository verification

The manuscript intentionally keeps repository mechanics out of its main
text.  Supporting records are maintained separately:

- source URLs, access notes, and checksums are in
  [`../references/SOURCES.csv`](../references/SOURCES.csv);
- theorem pinpoints and access boundaries are in
  [`../notes/04-source-audit.md`](../notes/04-source-audit.md);
- claim classifications are in
  [`../CLAIM-LEDGER.md`](../CLAIM-LEDGER.md); and
- `python3 ../tests/check-manuscript.py --self-test` checks bibliography and
  manifest consistency, required proof labels, and three mutation controls.
