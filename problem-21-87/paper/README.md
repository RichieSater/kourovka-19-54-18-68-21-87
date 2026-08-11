# Manuscript build

`main.tex` is the peer-review draft answering Kourovka Problem 21.87.
The exact internally reviewed source is frozen at
[`ada5993f83e2c5e19e91a8bf4669eb702de0e45f`](https://github.com/RichieSater/kourovka-19-54-18-68-21-87/tree/ada5993f83e2c5e19e91a8bf4669eb702de0e45f/problem-21-87/paper).

Build from this directory with the pinned wrapper used for the candidate:

```sh
./build.sh
```

The proof is prose-only and uses no computer calculation. The PDF is a build
artifact and is not committed; reviewers should regenerate it from the source.
The wrapper requires Tectonic 0.17.0, rejects LaTeX diagnostics, and confirms
that the generated PDF has a readable, nonzero page count.
