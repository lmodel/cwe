---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/grouping-not-category
genre: explanation
title: Grouping, not category
description: "Why the schema has `CweGrouping` and no category class: schema 8.0 renamed Category to Grouping to end the confusion with Class, CWE 5.0 holds no category, and `tests/test_coverage.py` names `CategoryType` as its one exclusion, although the XSD still declares it."
about:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/grouping
sources:
  - id: about.md
    resource: docs/about.md
    title: What is left out
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: EXCLUDED_KEYS
  - id: cwe_core.yaml
    resource: src/cwe/schema/cwe_core.yaml
    title: CweReason
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Grouping, not category

XSD 8.0 still declares `CategoryType` and a `Categories` element beside `GroupingType` and `Groupings`.[^about.md]

CWE 5.0 holds no category, and the CWE Program's news article of 28 October 2026 says `Grouping` replaced `Category`.[^test_coverage.py]

So the schema has no such class, and the coverage test names this as its one exclusion. The value `Category` stays in `CweReason`, because the XSD lists it beside `Grouping`.[^cwe_core.yaml]

[^about.md]: docs/about.md, What is left out
[^test_coverage.py]: tests/test_coverage.py, EXCLUDED_KEYS
[^cwe_core.yaml]: src/cwe/schema/cwe_core.yaml, CweReason
