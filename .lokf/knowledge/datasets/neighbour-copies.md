---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The adapt copies of eleven released lmodel repositories and of lmodel/capec's branch in `tests/neighbours/`, among them cve, kev-catalog, nist-nvd, spdx and stix, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and SHARED_WITH_NEIGHBOURS
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: neighbour_iris
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-04T03:04:31Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum, except `capec.yaml`, which comes from lmodel/capec's branch until that repository has a release.[^test_schema_rules.py]

The test fails on any shared class, enum or type, and on a shared key it does not list. It lists none for eleven of the copies, because the keys here begin with a capital and theirs do not. It lists 66 for lmodel/capec, whose XSD MITRE writes in the same style.[^test_schema_rules.py]

`tests/test_mappings.py` also reads these copies, to hold the mappings to cve, kev-catalog, nist-nvd, capec and SPDX.[^test_mappings.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
[^test_mappings.py]: tests/test_mappings.py, neighbour_iris
