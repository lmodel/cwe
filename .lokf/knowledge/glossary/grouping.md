---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/grouping
title: Grouping
description: "A grouping: a set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category, and `CweGrouping` models it."
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/explanations/grouping-not-category
sources:
  - id: cwe_entries.yaml
    resource: src/cwe/schema/cwe_entries.yaml
    title: CweGrouping
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Grouping

A grouping names its members under `Relationships`. Schema 8.0 changed the word to stop people confusing a category with a class.[^cwe_entries.yaml]

[^cwe_entries.yaml]: src/cwe/schema/cwe_entries.yaml, CweGrouping
