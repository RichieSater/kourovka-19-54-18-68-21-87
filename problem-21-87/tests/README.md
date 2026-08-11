# Test plan

The final proof is deductive and uses no finite computation.  Its proof-path
test is therefore a fail-closed consistency check rather than a database
certificate:

```sh
python3 check-manuscript.py --self-test
```

The checker verifies that every citation key is defined and unique, every
bibliography entry is cited, all required sources are cited, required proof
labels are present, and the source manifest has the required rows, schema,
retrieval dates, HTTPS URLs, proof roles, access notes, and checksums where a
public source file was available.  It also requires explicit no-computation
and external-review boundaries in the manuscript.

The repository-facing checksum, theorem-pinpoint, and mutation-control detail
is kept here and in the source audit rather than in the journal manuscript.

The self-test applies three negative controls and requires each to fail:

1. an undefined citation key;
2. a malformed source checksum; and
3. omission of the Guralnick source row.

The exploratory SmallGroups pilot described in the notes is not proof-path
evidence.  It produced no committed certificate, so neither this checker nor
the manuscript treats it as exhaustive verification.
