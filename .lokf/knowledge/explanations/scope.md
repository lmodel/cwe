---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/scope
genre: explanation
title: What the schema does not cover
description: "What the schema leaves out on purpose: the category kept in XSD 8.0, the parallel CWE 4.x line under schema 7.x, the JSON of the CWE REST API, and any claim about whether what an entry says is true."
about:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: What is left out
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# What the schema does not cover

The schema renders one edition under one XSD. The CWE Program keeps a parallel 4.x line under schema 7.x for consumers who have not moved, and this schema does not render it.[^about.md]

The REST API's JSON has other keys, and its schemas date from 2024, so this project does not render it either.[^about.md]

The schema says nothing about whether what an entry claims is true.[^about.md]

[^about.md]: docs/about.md, What is left out
