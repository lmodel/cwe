# The CWE files this schema renders

This folder holds files of the Common Weakness Enumeration (CWE) as The MITRE Corporation publishes them, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and `tests/test_upstream.py` holds the folder to that list.

| File | What it is | Read from |
| --- | --- | --- |
| `cwe_schema_v8.0.xsd` | The CWE Schema, version 8.0, with its licence header | <https://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd> |
| `cwec_v5.0.xml.zip` | The CWE List, version 5.0 of 2026-10-28 | <https://cwe.mitre.org/data/xml/cwec_latest.xml.zip> |
| `TERMS.txt` | The text of the Terms of Use | <https://cwe.mitre.org/about/termsofuse.html> |

Copyright (c) 2006-2026, The MITRE Corporation. CWE, CWSS, CWRAF, and the CWE logo are trademarks of The MITRE Corporation. The Terms of Use authorise these copies on condition that each reproduces that designation and the licence in `TERMS.txt`. [NOTICE](../NOTICE) says more. MITRE has not endorsed this project.

`scripts/cwec_to_json.py` turns the catalogue into the JSON that the LinkML schema describes.
