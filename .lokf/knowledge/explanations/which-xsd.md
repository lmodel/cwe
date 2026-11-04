---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/which-xsd
genre: explanation
title: Which file is the schema
description: "Why the schema renders `cwe_schema_v8.0.xsd` and not `cwe_schema_latest.xsd`: CWE 5.0 names the versioned file and validates against it, while the file behind the latest link is an earlier copy of 8.0 that the catalogue breaks in 69 places."
about:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
references:
  - https://w3id.org/lmodel/cwe/knowledge/workflows/upstream-watch
sources:
  - id: about.md
    resource: docs/about.md
    title: Which file is the schema
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: PINNED_LATEST_XSD_BLOB
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Which file is the schema

The XML of CWE 5.0 names `cwe_schema_v8.0.xsd` in its `schemaLocation`, and validates against it with no error.[^about.md]

The file behind the `cwe_schema_latest.xsd` link is an earlier copy of 8.0. It lacks the keys `Rationale`, `Alt_URL`, `Alt_URL_Date`, `Media_Type` and `Access_Restrictions`, and two values.[^about.md]

The watch pins both files. When the second changes, the run fails and asks a person to look.[^check_upstream_release.py]

[^about.md]: docs/about.md, Which file is the schema
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_LATEST_XSD_BLOB
