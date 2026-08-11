# GAP workspace

Reserved for complement tests and bounded group scans for Problem 18.68.

A future property function must return structured evidence, not a bare Boolean:

- group and maximal-class identifiers;
- complement subgroup generators/order for a positive class;
- product and trivial-intersection checks;
- an explicit `UNKNOWN` state if completeness of the complement search is not
  established.

Character tables alone cannot certify complement existence.
