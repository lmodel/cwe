---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "How the schema crosses to other vocabularies: `exact_mappings` where SEPSES reads the same XML key, `close_mappings` to SKOS, schema.org and Dublin Core, `related_mappings` to lmodel/cve, lmodel/kev-catalog, lmodel/nist-nvd, lmodel/capec and SPDX. Each is held to a pinned term list or a neighbour copy."
references:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/mapping-term-list
  - https://w3id.org/lmodel/cwe/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: cwe_entries.yaml
    resource: src/cwe/schema/cwe_entries.yaml
    title: the comments on ID and CweWeakness
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T03:04:31Z"
status: draft
---

# Mappings

The schema is the one home for mappings. The old SSSOM file is gone, since no source confirmed its rows.[^readme.md]

A mapping is `exact` only where the SEPSES conversion reads the same key of the same XML. A class is `close` to its SEPSES class, because their shapes differ.[^cwe_entries.yaml]

A vulnerability record writes a weakness as `CWE-79`, and this schema writes `79`, so the fields in lmodel/cve and lmodel/kev-catalog are `related`.[^cwe_entries.yaml]

CAPEC holds the link between a weakness and an attack pattern from its own side, and CWE 5.0 and CAPEC 3.9 each name the same 1212 pairs. So the two classes are the two ends of one link, and the mapping to lmodel/capec is `related`.[^cwe_entries.yaml]

Each target must be in a pinned term list or a released neighbour copy, and `tests/test_mappings.py` holds this.[^test_mappings.py]

[^readme.md]: README.md, Mappings
[^cwe_entries.yaml]: src/cwe/schema/cwe_entries.yaml, the comments on ID and CweWeakness
[^test_mappings.py]: tests/test_mappings.py, the docstring
