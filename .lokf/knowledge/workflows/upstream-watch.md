---
type: Service
id: https://w3id.org/lmodel/cwe/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: another edition of the CWE List, a changed XSD, a change behind the latest link, a newer schema on the archive page or changed Terms of Use fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-list
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-terms-of-use
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script reads MITRE's public pages, compares each file by git object hash and reads at most 20 MB of an answer. It sends no token, follows a redirect only over https to `cwe.mitre.org`, and quotes server text as code on one line.[^check_upstream_release.py]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
