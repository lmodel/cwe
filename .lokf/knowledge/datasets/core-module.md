---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/core-module
genre: reference
title: Core module
description: "`src/cwe/schema/cwe_core.yaml`, the module with the schema's types, its enums of the XSD's value lists, and the value classes every entry shares: `CweExternalReference`, `CweReference`, `CweNote`, `CweDimension`, `CweCustomPhase`, `CweTaxonomyMapping` and the content history."
resource: src/cwe/schema/cwe_core.yaml
isPartOf:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: cwe_core.yaml
    resource: src/cwe/schema/cwe_core.yaml
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_each_enum_lists_the_xsds_values
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Core module

The module imports only the LinkML types.[^cwe_core.yaml]

Each enum renders one XSD enumeration, and its `xsd_type` annotation names which.[^cwe_core.yaml] `tests/test_coverage.py` compares the values with the XSD's, in order.[^test_coverage.py]

`CweCustomPhase` holds a stage from an AI or a hardware life cycle. Two rules tie the stage to the `Domain`, which the XSD's own comment says XML Schema could not do.[^cwe_core.yaml]

[^cwe_core.yaml]: src/cwe/schema/cwe_core.yaml
[^test_coverage.py]: tests/test_coverage.py, test_each_enum_lists_the_xsds_values
