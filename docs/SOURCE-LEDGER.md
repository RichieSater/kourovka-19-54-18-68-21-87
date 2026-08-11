# Source ledger

This ledger records sources used to establish the repository's starting point.
It does not certify that the problems remain open after the search date; see
[`LITERATURE-SEARCH.md`](LITERATURE-SEARCH.md) for the limits of that check.

## Canonical Notebook

| Field | Value |
|---|---|
| Source | *The Kourovka Notebook: Unsolved Problems in Group Theory*, 21st issue |
| File | [July 2026 PDF](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21tkt.pdf) |
| Retrieved | 2026-08-11 |
| PDF creation metadata | 2026-07-03 |
| Pages | 302 |
| SHA-256 | `301b0cdcc53abc88b57cc0732cad73bf8fbe1c9ba0de5a0a794070398e3395fe` |

Problem locations in that PDF:

- Problem 18.68: PDF/printed page 123.
- Problem 19.54: PDF/printed page 137.
- Problem 21.87: PDF/printed page 177.

The exact statements are transcribed in the respective `PROBLEM.md` files.

## Problem 19.54

1. H. Meng and X. Guo, "Weak second maximal subgroups in solvable
   groups," *Journal of Algebra* 517 (2019), 112--118,
   [arXiv:1808.02309](https://arxiv.org/abs/1808.02309),
   [DOI 10.1016/j.jalgebra.2018.09.029](https://doi.org/10.1016/j.jalgebra.2018.09.029).
   Published input: the soluble WSM characterization by strongly irreducible
   non-Frattini chief factors.
2. V. S. Monakhov and I. L. Sokhor, "On strictly 2-maximal subgroups of
   finite groups," [arXiv:2010.05714](https://arxiv.org/abs/2010.05714).
   Terminology, equivalence with the Notebook condition, and examples.
3. M. N. Konovalova, V. S. Monakhov, and I. L. Sokhor, "On strictly
   2-maximal subgroups of finite groups," *Problems of Physics, Mathematics
   and Technics* 4(49) (2021), 95--100,
   [MathNet record](https://www.mathnet.ru/eng/pfmt817),
   [DOI 10.54341/20778708_2021_4_49_95](https://doi.org/10.54341/20778708_2021_4_49_95).
   Published examples and related structural statements.

## Problem 18.68

1. V. M. Levchuk and A. G. Likharev, "Finite simple groups with
   complemented maximal subgroups," *Siberian Mathematical Journal* 47(4)
   (2006), 659--668,
   [MathNet record](https://www.mathnet.ru/eng/smj896),
   [DOI 10.1007/s11202-006-0077-7](https://doi.org/10.1007/s11202-006-0077-7).
   Published input: the simple-group list stated in the Notebook.
2. N. V. Maslova, work cited by the Notebook in *Siberian Mathematical
   Journal* 53(5) (2012), 853--861. Published input quoted by the Notebook:
   the Hall-maximal composition-factor classification.
3. N. V. Maslova and D. O. Revin, "On the normal structure of a finite group
   with restrictions on the maximal subgroups," *Siberian Advances in
   Mathematics* 23(3) (2013), 196--209. Published input quoted by the
   Notebook: Hall maximal subgroups have complements.

Items 2 and 3 need edition-level source capture and pinpoint theorem numbers
before they are used in a proof.

## Problem 21.87

1. L. G. Kovacs and H.-S. Sim, "Generating finite soluble groups,"
   *Indagationes Mathematicae* 2 (1991), 229--232. Published input quoted by
   the Notebook: the soluble \(d+1\) bound.
2. A. Lucchini, "On groups with d-generator subgroups of coprime index,"
   *Communications in Algebra* 28(4) (2000), 1875--1880,
   [publisher record](https://www.tandfonline.com/doi/abs/10.1080/00927870008826932),
   [DOI 10.1080/00927870008826932](https://doi.org/10.1080/00927870008826932).
   Published input quoted by the Notebook: the arbitrary finite-group
   \(d+2\) bound.
3. A. Lucchini, "Generating the augmentation ideal," *Rend. Sem. Mat.
   Univ. Padova* 88 (1992), 145--149,
   [Numdam PDF](https://www.numdam.org/item/RSMUP_1992__88__145_0.pdf).
   Published input: \(d_G(I_G)\leq d+1\).
4. F. Dalla Volta and A. Lucchini, "Finite groups that need more generators
   than any proper quotient," *J. Austral. Math. Soc. Ser. A* 64 (1998),
   82--91,
   [DOI 10.1017/S1446788700001312](https://doi.org/10.1017/S1446788700001312).
   Published input: critical crown reduction and exact multiplicity formula.
5. E. Detomi and A. Lucchini, "Probabilistic generation of finite groups
   with a unique minimal normal subgroups," *J. Lond. Math. Soc.* 87 (2013),
   689--706,
   [official repository record](https://www.research.unipd.it/handle/11577/2528913),
   [DOI 10.1112/jlms/jds076](https://doi.org/10.1112/jlms/jds076).
   Published input: \(P_{L,A}(m)\geq1/2\) for \(m\geq d(L)\).
6. R. M. Guralnick, "Generation of simple groups," *J. Algebra* 103 (1986),
   381--401,
   [DOI 10.1016/0021-8693(86)90194-8](https://doi.org/10.1016/0021-8693(86)90194-8).
   Published input: generation by a Sylow \(2\)-subgroup and an involution.

The proof-path retrieval hashes and access boundaries are recorded in
`problem-21-87/references/SOURCES.csv`. The full Lucchini 2000 article was
not openly accessible, but the new proof does not invoke it; it is used only
for the historical baseline recorded by the current Notebook.

## Local prior-work sources

The setup read local checked-out copies rather than web mirrors:

- `../kourovka-10-34/README.md` and
  `../kourovka-10-34/supporting-materials/README.md`.
- `../kourovka-19-57-19-58/README.md`, `AGENTS.md`, `gap/properties.g`,
  `notes/00-reduction.md`, `notes/03-roadmap.md`, and the paper structure.
- `../monotone-maximal-chains/README.md`, `notes/problem.md`,
  `proofs/claim-ledger.md`, `proofs/counterexample.md`, and `src/mmc.g`.
- Historical exploratory notes in `../Math/kourovka-10.34/`.
