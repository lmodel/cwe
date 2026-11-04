---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/compound
title: Chain and composite
description: "A compound weakness, which is a chain or a composite: a chain is several weaknesses reached one after another, and a composite is several that must occur together. CWE 5.0 has three chains and four composites."
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/related-nature
sources:
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_compound_weaknesses_use_their_natures
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Chain and composite

A chain says where it starts with the nature `StartsWith`, and a composite what it needs with `Requires`. CWE 5.0 has 3 chains and 4 composites.[^test_catalogue.py]

[^test_catalogue.py]: tests/test_catalogue.py, test_the_compound_weaknesses_use_their_natures
