---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/view
title: View
description: "A view: a way of looking at the catalogue, as a subset of its entries from one standpoint. `CweView` models it, and its `Type` is `Graph`, `Explicit` or `Implicit`."
sources:
  - id: cwe_core.yaml
    resource: src/cwe/schema/cwe_core.yaml
    title: CweViewType
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# View

A graph arranges entries as a hierarchy. An explicit slice names its members, and an implicit slice selects them with a `Filter`, an XPath expression.[^cwe_core.yaml]

[^cwe_core.yaml]: src/cwe/schema/cwe_core.yaml, CweViewType
