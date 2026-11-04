---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/mapping-term-list
genre: reference
title: Mapping term list
description: "`tests/upstream/mapping-terms.txt`, the classes and properties of Dublin Core, schema.org, SKOS and the SEPSES CWE ontology, which `scripts/extract_mapping_terms.py` writes from each vocabulary's pinned file and `tests/test_mappings.py` holds each mapping to."
resource: tests/upstream/mapping-terms.txt
references:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: extract_mapping_terms.py
    resource: scripts/extract_mapping_terms.py
    title: the docstring and the pins
  - id: test_mappings.py
    resource: tests/test_mappings.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Mapping term list

The list holds each class and property that a vocabulary's published file declares in its own namespace, and no label or comment.[^extract_mapping_terms.py]

The script refuses a file unless its SHA-256 is the pinned one. Wikidata's Q2682392 and P3624 are named by hand, since an entity there has no fixed file to pin.[^extract_mapping_terms.py]

`tests/test_mappings.py` pins the list's own checksum, and fails on a mapping whose prefix the module does not bind or whose target neither the list nor a neighbour copy declares.[^test_mappings.py]

[^extract_mapping_terms.py]: scripts/extract_mapping_terms.py, the docstring and the pins
[^test_mappings.py]: tests/test_mappings.py
