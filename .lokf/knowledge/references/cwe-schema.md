---
type: Reference
id: https://w3id.org/lmodel/cwe/knowledge/references/cwe-schema
genre: reference
title: CWE Schema
description: The XML Schema of the CWE List, version 8.0 of 28 October 2026, namespace `http://cwe.mitre.org/cwe-8`, at `https://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd`. The schema renders this file, a copy of which `upstream/` holds.
resource: https://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd
relatedTo:
  - https://w3id.org/lmodel/cwe/knowledge/explanations/which-xsd
sources:
  - id: about.md
    resource: docs/about.md
    title: Which file is the schema
  - id: cwe_schema_v8.0.xsd
    resource: upstream/cwe_schema_v8.0.xsd
    title: the appinfo
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# CWE Schema

Version 8.0 came with CWE 5.0. It renamed Category to Grouping in the data, and added technical nuance, dimensions, custom life cycle phases for AI and hardware, and the `Overlaps` nature.[^about.md]

The file's own header gives the version, the date and the licence, and asks each copy to keep that header.[^cwe_schema_v8.0.xsd]

The file behind `cwe_schema_latest.xsd` is not this one.[^about.md]

[^about.md]: docs/about.md, Which file is the schema
[^cwe_schema_v8.0.xsd]: upstream/cwe_schema_v8.0.xsd, the appinfo
