---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/entries-module
genre: reference
title: Entries module
description: "`src/cwe/schema/cwe_entries.yaml`, the module with the abstract `CweEntry` and its three kinds, `CweWeakness`, `CweGrouping` and `CweView`, with what a weakness holds: related weaknesses, platforms, modes of introduction, consequences, detection methods, mitigations and worked examples."
resource: src/cwe/schema/cwe_entries.yaml
isPartOf:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
about:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/entry
  - https://w3id.org/lmodel/cwe/knowledge/glossary/weakness
  - https://w3id.org/lmodel/cwe/knowledge/glossary/grouping
  - https://w3id.org/lmodel/cwe/knowledge/glossary/view
sources:
  - id: cwe_entries.yaml
    resource: src/cwe/schema/cwe_entries.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Entries module

`CweEntry` holds the fields the XSD gives all three kinds of entry, with `ID` as the identifier.[^cwe_entries.yaml]

The module also holds the rules that tie `Abstraction` to `Structure`, and the rule that a platform has a `Name` or a `Class`.[^cwe_entries.yaml]

A reference such as `CWE_ID` ranges over the class it names, so it is typed. `CAPEC_ID` stays a digit string, because CAPEC is another catalogue.[^cwe_entries.yaml]

[^cwe_entries.yaml]: src/cwe/schema/cwe_entries.yaml
