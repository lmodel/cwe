---
type: Policy
id: https://w3id.org/lmodel/cwe/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, the CWE List and its XSD under MITRE's CWE Terms of Use, with the designation and licence those terms ask each copy to reproduce. No endorsement by MITRE or the CWE Program is implied."
resource: NOTICE
references:
  - https://w3id.org/lmodel/cwe/knowledge/references/cwe-terms-of-use
sources:
  - id: notice
    resource: NOTICE
  - id: readme.md
    resource: README.md
    title: License
  - resource: LICENSE
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Licence and attribution

The code in this repository is under the Apache License 2.0.[^notice] The knowledge bundle is under CC BY 4.0.[^readme.md]

`upstream/` holds the catalogue and the XSD as MITRE publishes them, and `tests/data/` short excerpts of entries. The Terms of Use allow such copies on condition that each reproduces MITRE's copyright designation and the licence, and `NOTICE` does.[^notice]

CWE is a trademark of The MITRE Corporation, and the project implies no endorsement by it or by the CWE Program.[^notice]

[^notice]: NOTICE
[^readme.md]: README.md, License
