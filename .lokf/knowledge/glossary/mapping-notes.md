---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/mapping-notes
title: Mapping notes
description: "Mapping notes: the guidance on whether a real vulnerability may be mapped to an entry as its root cause. `CweMappingNotes` holds the `Usage`, which is `Allowed`, `Allowed-with-Review`, `Discouraged` or `Prohibited`, with the reasons and suggestions."
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/explanations/what-the-data-shows
sources:
  - id: cwe_entries.yaml
    resource: src/cwe/schema/cwe_entries.yaml
    title: CweMappingNotes
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Mapping notes

Every entry must have them. `Reasons` sums up the `Usage` in short labels, and `Suggestions` names weaknesses that may suit the mapping better.[^cwe_entries.yaml]

[^cwe_entries.yaml]: src/cwe/schema/cwe_entries.yaml, CweMappingNotes
