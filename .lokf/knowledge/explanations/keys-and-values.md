---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/keys-and-values
genre: explanation
title: The XSD's keys and values
description: "Why slots and permissible values keep the XSD's spelling, such as `Related_Weaknesses`, `CWE_ID` and `Automated Static Analysis - Source Code`, while classes and enums take a `Cwe` prefix: the catalogue must validate with both unchanged, and `.linkmllint.yaml` says so."
about:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Keys
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_the_one_page_that_collides_is_date
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# The XSD's keys and values

A key or a value in the schema is what the catalogue holds. So the catalogue validates unchanged only if the schema spells them as the XSD does.[^about.md]

`.linkmllint.yaml` relaxes the naming rule for this, with a comment that says why. Class, enum and type names keep the rule's usual form.[^linkmllint.yaml]

A class name never reaches the data, so classes carry a prefix to stay apart from those of other schemas. The one page that collides is `Date`, the key beside the page of LinkML's own type.[^test_schema_rules.py]

[^about.md]: docs/about.md, Keys
[^linkmllint.yaml]: .linkmllint.yaml, the comment
[^test_schema_rules.py]: tests/test_schema_rules.py, test_the_one_page_that_collides_is_date
