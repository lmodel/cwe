---
type: Playbook
id: https://w3id.org/lmodel/cwe/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition
description: "How to move the schema to another edition when the watch reports one: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let `tests/test_coverage.py` show what the new XSD changed."
references:
  - https://w3id.org/lmodel/cwe/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/cwe/knowledge/datasets/upstream-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_every_module_names_the_pinned_edition
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Move to another edition

1. Read the watch's report and MITRE's list of changes. A person decides whether the schema moves.[^check_upstream_release.py]
2. Put the new ZIP and XSD in `upstream/`, and move the pins in `scripts/check_upstream_release.py`.[^check_upstream_release.py]
3. Move the `version`, `source` and annotations in each schema header. `tests/test_upstream.py` holds them equal to the pins.[^test_upstream.py]
4. Run `just test`. `tests/test_coverage.py` fails on each key, value or cardinality that moved, and `tests/test_catalogue.py` on each recorded fact that a new edition broke.[^test_coverage.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py, test_every_module_names_the_pinned_edition
[^test_coverage.py]: tests/test_coverage.py, the docstring
