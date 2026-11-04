---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/cwe.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CweEntry` and `CweExternalReference`, with `ID` and `Reference_ID` dropped for LOKF's `id`, and five keys folded into LOKF's `title` and `description`."
resource: .lokf/cwe.yaml
derivedFrom:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
about:
  - https://w3id.org/lmodel/cwe/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: FOLDED and DROPPED
  - resource: .lokf/cwe.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/cwe.yaml` from `src/cwe/schema/cwe.yaml`, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

A concept may name `CweWeakness`, `CweGrouping`, `CweView` or `CweExternalReference` as its `type`.[^readme.md]

The copy folds `Name` and `Title` into `title`, and `Description`, `Summary` and `Objective` into `description`. Every other key keeps its capital, so none is LOKF's.[^test_schema_rules.py]

A release attaches the copy as `schema-<tag>-cwe.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, FOLDED and DROPPED
