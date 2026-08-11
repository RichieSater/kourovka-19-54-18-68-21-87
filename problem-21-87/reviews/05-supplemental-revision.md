# Supplemental post-protocol revision — referee preflight

- **Base release candidate:**
  `9c92e55278b045e8667264e8fbb40b74fa6a8ed1`
- **Corrected candidate:** pending freeze
- **Date:** 2026-08-11
- **Scope:** editorial precision and bibliographic fidelity only
- **Protocol status:** supplemental; not a fifth required revision round

## Preflight findings and dispositions

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| S5-R01 | P3 | The theorem quantified (d\geq0) without explicitly saying that (d) is an integer. | The theorem now says “Let (d) be a nonnegative integer.” |
| S5-R02 | P3 | The introduction called the (d+1) bound sharp but gave no witness. | Added the elementary (S_3) witness: cyclic subgroups of orders (2) and (3) have indices (3) and (2), while (d(S_3)=2). |
| S5-R03 | P3 | The Detomi--Lucchini title in the local bibliography and source manifest used the grammatically natural singular “subgroup,” but the publisher and Crossref records print “subgroups.” | Restored the official published title verbatim in both metadata files. |

None of these items changes the proof, its hypotheses, the crown count, or any
evidence classification.  The supplemental referee pass must start from the
frozen corrected candidate and recheck the complete paper rather than only
these three changes.
