---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/references-and-identifiers
genre: explanation
title: References and identifiers
description: "Why `ID`, `CWE_ID` and `View_ID` are digit strings that range over the class they name, why `Reference_ID` has no pattern, and why `tests/cwe_rules.py` checks over a whole catalogue what a generated JSON Schema cannot: that a reference resolves to an entry of the right kind."
about:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/entry
  - https://w3id.org/lmodel/cwe/knowledge/datasets/entries-module
sources:
  - id: cwe_core.yaml
    resource: src/cwe/schema/cwe_core.yaml
    title: cwe_entry_id and cwe_reference_id
  - id: cwe_entries.yaml
    resource: src/cwe/schema/cwe_entries.yaml
    title: CweRelatedWeakness and CweMember
  - id: cwe_rules.py
    resource: tests/cwe_rules.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# References and identifiers

The XML holds text, and the numbers stay text here. LinkML's RDF dumper needs an identifier it can expand, and an integer would gain nothing.[^cwe_core.yaml]

A `CWE_ID` ranges over `CweWeakness` in a related weakness and a suggestion, and over `CweEntry` in a member, since a member can be a grouping.[^cwe_entries.yaml]

JSON Schema looks at one value at a time, so it cannot tell whether a value names an entry that exists. `tests/cwe_rules.py` checks that, with the uniqueness the XSD states.[^cwe_rules.py]

The XSD types `Reference_ID` as a string, and CWE 5.0 writes REF and a number on all sources but one, whose identifier is the bare number 1300. So the schema states no pattern for it.[^cwe_core.yaml]

[^cwe_core.yaml]: src/cwe/schema/cwe_core.yaml, cwe_entry_id and cwe_reference_id
[^cwe_entries.yaml]: src/cwe/schema/cwe_entries.yaml, CweRelatedWeakness and CweMember
[^cwe_rules.py]: tests/cwe_rules.py, the docstring
