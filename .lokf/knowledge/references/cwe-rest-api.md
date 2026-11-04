---
type: Reference
id: https://w3id.org/lmodel/cwe/knowledge/references/cwe-rest-api
genre: reference
title: CWE REST API
description: The CWE-CAPEC REST API working group's JSON form of the CWE, at `cwe-api.mitre.org`, with schemas in the `CWE-CAPEC/REST-API-wg` repository. It is not the source of this schema, because its schemas date from 2024 and its keys are not consistent. `Value` and `Entries` take its names.
resource: https://github.com/CWE-CAPEC/REST-API-wg
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Which file is the schema
  - id: cwec_to_json.py
    resource: scripts/cwec_to_json.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# CWE REST API

The working group publishes the same content as JSON, with other keys.[^about.md]

The schema takes two words from it: `Value` for text beside attributes, and `Entries` for a worked example's ordered prose and code.[^cwec_to_json.py]

[^about.md]: docs/about.md, Which file is the schema
[^cwec_to_json.py]: scripts/cwec_to_json.py, the docstring
