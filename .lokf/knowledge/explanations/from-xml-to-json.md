---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/from-xml-to-json
genre: explanation
title: From XML to JSON
description: "How `scripts/cwec_to_json.py` turns MITRE's XML into the JSON that the schema describes: wrappers become lists, text beside attributes goes under `Value`, XHTML stays a fragment, and the prose and code of an example stay in order under `Entries`."
about:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
  - https://w3id.org/lmodel/cwe/knowledge/glossary/structured-text
references:
  - https://w3id.org/lmodel/cwe/knowledge/playbooks/validate-a-catalogue
sources:
  - id: about.md
    resource: docs/about.md
    title: From XML to JSON
  - id: cwec_to_json.py
    resource: scripts/cwec_to_json.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_conversion_loses_nothing
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# From XML to JSON

LinkML validates JSON and YAML, and MITRE publishes XML, so one fixed step stands between them. It keeps every name and value, and it reads what repeats from the XSD.[^about.md]

The step stops on an element or an attribute the XSD does not declare, so a catalogue that leaves its schema is noticed.[^cwec_to_json.py]

`Entries` is the one key the XSD does not give. It keeps the order of `Body_Text` and `Example_Code`, which the prose relies on.[^about.md]

`tests/test_catalogue.py` shows that the conversion loses nothing: every attribute value and text of the XML is in the output as many times as the XML has it, and nothing else is.[^test_catalogue.py]

[^about.md]: docs/about.md, From XML to JSON
[^cwec_to_json.py]: scripts/cwec_to_json.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py, test_the_conversion_loses_nothing
