---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/entry
title: Entry
description: "An entry of the CWE List: any item with its own identifier, which is a weakness, a grouping or a view. `CweEntry` is the abstract class of all three."
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/entries-module
sources:
  - id: about.md
    resource: docs/about.md
    title: How the catalogue is shaped
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Entry

The CWE glossary calls any item with a unique identifier an entry. An `ID` is unique across all three kinds, and `tests/cwe_rules.py` holds this.[^about.md]

[^about.md]: docs/about.md, How the catalogue is shaped
