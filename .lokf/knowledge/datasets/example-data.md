---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: a valid example of each class, most of them real pieces of the CWE List, a counter-example for each constraint, and counter-examples for the rules on a whole catalogue that JSON Schema cannot state."
resource: tests/data
references:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: data-readme.md
    resource: tests/data/README.md
  - id: test_data.py
    resource: tests/test_data.py
    title: test_every_concrete_class_has_an_example
  - resource: tests/cwe_rules.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Example data

`tests/data/valid/` holds an example of each class. `tests/data/invalid/` holds a counter-example for each constraint, whose first line names the one place it fails. `tests/data/problem/invalid/` holds a counter-example for each rule that `tests/cwe_rules.py` checks.[^data-readme.md]

The real pieces name the entry they come from, and carry MITRE's designation.[^data-readme.md]

`tests/test_data.py` runs them all and fails when a class has no example.[^test_data.py]

[^data-readme.md]: tests/data/README.md
[^test_data.py]: tests/test_data.py, test_every_concrete_class_has_an_example
