---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/what-the-data-shows
genre: explanation
title: What the data shows and the schema does not say
description: "Facts about CWE 5.0 that no upstream text states, which stay in `tests/test_catalogue.py` and out of the schema: every deprecated entry is named so and barred from mapping, every grouping and view is barred from mapping, and each link is written in one direction only."
about:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/mapping-notes
  - https://w3id.org/lmodel/cwe/knowledge/glossary/related-nature
sources:
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: the second group of tests
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:48:39Z"
status: draft
---

# What the data shows and the schema does not say

These hold in CWE 5.0, and a later edition may break them, so a test records each one and the schema states none.[^test_catalogue.py]

- Every deprecated entry's name starts `DEPRECATED:` and its usage is `Prohibited`.[^test_catalogue.py]
- Every grouping and every view has the usage `Prohibited`.[^test_catalogue.py]
- The list writes `ChildOf`, `CanPrecede` and `Requires`, and never their inverses.[^test_catalogue.py]
- The CWE Program calls `PeerOf` and `Overlaps` symmetric, but 14 of 103 `PeerOf` links, and none of 3 `Overlaps` links, have their reverse.[^test_catalogue.py]
- Two deprecated views, an explicit slice and a graph, name no members.[^test_catalogue.py]

[^test_catalogue.py]: tests/test_catalogue.py, the second group of tests
