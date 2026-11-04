---
type: GlossaryTerm
id: https://w3id.org/lmodel/cwe/knowledge/glossary/related-nature
title: Related nature
description: "The nature of a link between two weaknesses: `ChildOf`, `ParentOf`, `StartsWith`, `CanFollow`, `CanPrecede`, `RequiredBy`, `Requires`, `CanAlsoBe`, `PeerOf` or `Overlaps`. `CweRelatedNature` lists them."
sources:
  - id: cwe_core.yaml
    resource: src/cwe/schema/cwe_core.yaml
    title: CweRelatedNature
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Related nature

Three pairs are inverses: `ChildOf` and `ParentOf`, `CanPrecede` and `CanFollow`, and `Requires` and `RequiredBy`.[^cwe_core.yaml]

The CWE news article of 28 October 2026 calls `PeerOf` and `Overlaps` symmetric. The XSD says `CanAlsoBe` need not be reciprocal.[^cwe_core.yaml]

[^cwe_core.yaml]: src/cwe/schema/cwe_core.yaml, CweRelatedNature
