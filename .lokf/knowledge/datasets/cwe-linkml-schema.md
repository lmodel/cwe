---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
genre: reference
title: cwe LinkML schema
description: "The LinkML model of the CWE List 5.0 and its XML Schema 8.0, `src/cwe/schema/cwe.yaml` (schema id `https://w3id.org/lmodel/cwe`): an umbrella that holds only the tree root `CweWeaknessCatalog`, over the modules `cwe_core` and `cwe_entries`. Search it for weaknesses, groupings, views and external references."
resource: src/cwe/schema/cwe.yaml
derivedFrom:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
hasPart:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/core-module
  - https://w3id.org/lmodel/cwe/knowledge/datasets/entries-module
sources:
  - id: schema
    resource: src/cwe/schema
    title: the three files
  - id: cwe.yaml
    resource: src/cwe/schema/cwe.yaml
    title: the header
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: test_the_module_imports_are_the_contract
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# cwe LinkML schema

The schema has three files. `cwe.yaml` holds the tree root, `CweWeaknessCatalog`. `cwe_entries.yaml` holds the entries, and `cwe_core.yaml` holds the types, the value lists and the value classes they share.[^schema]

The header's `version` is the edition of the CWE List, 5.0, and its `source` is the versioned XSD. Annotations give the XSD's version, namespace and date.[^cwe.yaml]

`tests/test_mappings.py` holds the imports: `cwe_core` imports only the LinkML types, and each module loads on its own.[^test_mappings.py]

[^schema]: src/cwe/schema, the three files
[^cwe.yaml]: src/cwe/schema/cwe.yaml, the header
[^test_mappings.py]: tests/test_mappings.py, test_the_module_imports_are_the_contract
