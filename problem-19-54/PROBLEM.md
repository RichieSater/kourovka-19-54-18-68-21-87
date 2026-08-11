# Exact problem and terminology

## Notebook statement

> **19.54.** What are the chief factors of a finite group in which every
> 2-maximal subgroup is not \(m\)-maximal for any \(m\geq 3\)?

The Notebook defines \(H\leq G\) to be \(m\)-maximal when there is a chain

\[
H=H_0 < H_1 < \cdots < H_{m-1}<H_m=G
\]

in which \(H_i\) is maximal in \(H_{i+1}\) for every \(i\).

Source: 21st Kourovka Notebook, PDF/printed page 137. See the root source
ledger for the retrieved-file hash.

## Equivalent terminology to verify and use

For a proper subgroup \(H<G\), let
\(\operatorname{Max}(G,H)\) be the maximal subgroups of \(G\) containing
\(H\).

- `weak second maximal`: \(H\) is maximal in at least one member of
  \(\operatorname{Max}(G,H)\);
- `second maximal` / `strictly 2-maximal`: \(H\) is maximal in every member of
  \(\operatorname{Max}(G,H)\).

Monakhov--Sokhor state that the Notebook hypothesis is equivalent to

\[
\operatorname{Max}_2(G)=\operatorname{Max}_2^\star(G),
\]

so this workspace uses **WSM-group** for a group satisfying the hypothesis.
The equivalence is a published input to be pinpointed and regression-tested,
not merely a naming convention.

## Chief-factor target

A chief factor is a section \(A/B\) with
\(B\lhd G\), \(A\lhd G\), and no normal subgroup of \(G\) strictly between
\(B\) and \(A\). The problem asks which such factors can occur; it does not
directly ask for a classification of all WSM-groups.

The attack must distinguish:

- Frattini and non-Frattini chief factors;
- abelian factors (including their induced module action) and nonabelian
  factors;
- factors of \(G\) from factors of subgroups or covers;
- abstract isomorphism type from the action of \(G/C_G(A/B)\).

## Published footholds

1. For **soluble** \(G\), Meng--Guo prove that \(G\) is a WSM-group if and
   only if every non-Frattini chief factor, as a \(G\)-module, is strongly
   irreducible.
2. Every supersoluble group satisfies the condition.
3. Published examples outside the supersoluble class include
   \(C_3^2:C_8\), \(U_3(2)\), and the simple groups \(U_3(3)\) and
   \(L_2(17)\).

These are starting fixtures, not a general classification.

## Questions that must be settled before a reduction

- Does the WSM property pass to quotients? If not without qualification, what
  local statement about a chief factor survives?
- What does the property do under direct products and subdirect products?
- Can a least-order nonsoluble WSM-group be forced to be monolithic,
  primitive, or almost simple?
- Is the relevant object the abstract chief factor \(S^k\), its induced outer
  action, or both?
- Are \(U_3(3)\) and \(L_2(17)\) the only nonabelian simple WSM-groups?

All five questions are currently **unchecked** in this repository.
