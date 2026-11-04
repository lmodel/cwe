---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/`: the CWE List 5.0 as MITRE's ZIP, the XSD 8.0 and the Terms of Use, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and `tests/test_upstream.py` holds the folder to that list."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-list
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
sources:
  - id: upstream-readme.md
    resource: upstream/README.md
  - id: notice
    resource: NOTICE
    title: The Common Weakness Enumeration
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the docstring
  - resource: upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Copy of the upstream

The folder holds `cwec_v5.0.xml.zip`, `cwe_schema_v8.0.xsd`, `TERMS.txt` and a README.[^upstream-readme.md]

The Terms of Use allow such copies on condition that each reproduces MITRE's designation and the licence.[^notice]

`tests/test_upstream.py` checks each file against its pinned hash, and the XML inside the ZIP as well, since a ZIP can be packed again with no change to what it holds. It runs offline.[^test_upstream.py]

[^upstream-readme.md]: upstream/README.md
[^notice]: NOTICE, The Common Weakness Enumeration
[^test_upstream.py]: tests/test_upstream.py, the docstring
