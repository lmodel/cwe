---
type: CweExternalReference
id: https://w3id.org/lmodel/cwe/knowledge/datasets/example-external-reference
genre: reference
title: A Catalog of Security Architecture Weaknesses.
description: The external reference REF-9 of CWE 5.0, written as a concept of type `CweExternalReference` in the adapt copy's keys. It shows that the domain schema admits a source as a concept, with its other address and its access restriction.
resource: tests/data/valid/CweExternalReference-alternate-address.yaml
derivedFrom:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/upstream-copy
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: cweexternalreference-alternate-address.yaml
    resource: tests/data/valid/CweExternalReference-alternate-address.yaml
Author:
  - Santos, J. C. S.
  - Tarrit, K.
  - Mirakhorli, M.
Publication: 2017 IEEE International Conference on Software Architecture (ICSA)
Publication_Year: "2017"
URL: https://ieeexplore.ieee.org/document/7958491
URL_Date: "2026-10-23"
Alt_URL: https://joannacss.com/preprints/icsaw17-preprint.pdf
Alt_URL_Date: "2026-10-23"
Access_Restrictions: Proprietary-Subscription
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:18:44Z"
status: draft
---

# A Catalog of Security Architecture Weaknesses

This concept shows how a host writes a source in its bundle: REF-9 of CWE 5.0, in the adapt copy's keys. Its type is `CweExternalReference`, and `lokf validate` checks it against `.lokf/schema/cwe.yaml`.[^readme.md]

Its `title` is the source's `Title`, which the copy folds into LOKF's key, and LOKF's `id` stands for its `Reference_ID`. Its other keys are as `tests/data/valid/CweExternalReference-alternate-address.yaml` holds them.[^cweexternalreference-alternate-address.yaml]

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^cweexternalreference-alternate-address.yaml]: tests/data/valid/CweExternalReference-alternate-address.yaml
