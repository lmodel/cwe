---
type: Reference
id: https://w3id.org/lmodel/cwe/knowledge/references/cwe-list
genre: reference
title: CWE List
description: The Common Weakness Enumeration list of software and hardware weakness types, which The MITRE Corporation publishes for the CWE Program. The schema renders version 5.0 of 28 October 2026, which holds 984 weaknesses, 431 groupings, 62 views and 1081 external references.
resource: https://cwe.mitre.org/data/index.html
references:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_catalogue_is_the_pinned_edition
  - id: about.md
    resource: docs/about.md
    title: What is left out
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# CWE List

The list is one XML file in a ZIP. The schema renders version 5.0 of 28 October 2026.[^check_upstream_release.py]

That release holds 984 weaknesses, 431 groupings, 62 views and 1081 external references.[^test_catalogue.py]

The CWE Program also publishes a parallel 4.x line under schema 7.x, of which 4.21 is the newest.[^about.md]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the pins
[^test_catalogue.py]: tests/test_catalogue.py, test_the_catalogue_is_the_pinned_edition
[^about.md]: docs/about.md, What is left out
