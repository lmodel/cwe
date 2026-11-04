---
type: Playbook
id: https://w3id.org/lmodel/cwe/knowledge/playbooks/validate-a-catalogue
genre: how-to
title: Validate a catalogue
description: "How to validate a release of the CWE List: run `scripts/cwec_to_json.py` over MITRE's XML or ZIP, run `linkml-validate` on the result with the class `CweWeaknessCatalog`, and run the rules in `tests/cwe_rules.py` for what JSON Schema cannot state."
references:
  - https://w3id.org/lmodel/cwe/knowledge/explanations/from-xml-to-json
  - https://w3id.org/lmodel/cwe/knowledge/datasets/generated-artefacts
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a catalogue
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Validate a catalogue

1. Turn the XML into JSON with `uv run scripts/cwec_to_json.py upstream/cwec_v5.0.xml.zip -o tmp/cwec_v5.0.json`. It needs only Python's standard library.[^index.md]
2. Validate the result with `uv run linkml-validate -s src/cwe/schema/cwe.yaml -C CweWeaknessCatalog tmp/cwec_v5.0.json`.[^index.md]
3. For the rules JSON Schema cannot state, run `rule_errors` from `tests/cwe_rules.py` on the JSON.[^index.md]

`project/jsonschema/cwe.schema.json` is the same schema for anyone without LinkML.[^index.md]

[^index.md]: docs/index.md, Validating a catalogue
