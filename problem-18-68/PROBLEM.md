# Exact problem and terminology

## Notebook statement

> **18.68.** What are the nonabelian composition factors of a finite
> nonsoluble group all of whose maximal subgroups have complements?

Source: 21st Kourovka Notebook, PDF/printed page 123. See the root source
ledger for the retrieved-file hash.

## Complement convention

For \(M\leq G\), a subgroup \(K\leq G\) is a **complement** to \(M\) in
\(G\) when

\[
G=MK\qquad\text{and}\qquad M\cap K=1.
\]

Equivalently, the product formula forces \(|K|=[G:M]\). The first task must
confirm that this is exactly the convention in the cited sources, including
whether trivial edge cases or "weak complements" ever occur in their
terminology.

Let `CMP(G)` abbreviate the property that every maximal subgroup of \(G\) has
a complement in \(G\). This abbreviation is local to the workspace and is not
claimed to be standard.

## Published baseline recorded by the Notebook

1. The nonabelian finite simple groups satisfying `CMP` are, up to
   isomorphism,
   \[
   L_2(7),\qquad L_2(11),\qquad L_5(2).
   \]
2. The same three groups are the simple groups with Hall maximal subgroups and
   the nonabelian composition factors of finite groups all of whose maximal
   subgroups are Hall.
3. In a finite group with Hall maximal subgroups, every maximal subgroup has a
   complement.

The Hall-maximal hypothesis is stronger than the property in the question.
The cited result in item 3 does **not** reverse, so the composition-factor
result in item 2 does not by itself answer Problem 18.68.

## Working conjecture

The initial candidate, to be tested rather than assumed, is

\[
\operatorname{Comp}_{\mathrm{nab}}(G)
\subseteq \{L_2(7),L_2(11),L_5(2)\}
\]

for every finite nonsoluble `CMP` group \(G\).

**Evidence label:** conjectural.

## Structural questions before minimality

- Does `CMP` pass to quotients? If so, how are complements lifted or projected?
- How does `CMP` behave under direct products and Frattini extensions?
- Can a composition factor that is not a subgroup inherit enough of `CMP` to
  invoke the simple classification?
- In a primitive monolithic group, how do complements to maximals meeting the
  socle encode complements to chief factors?
- When are complement existence and complement conjugacy controlled by
  derivations or \(H^1\)?

All of these are currently **unchecked** in this repository.
