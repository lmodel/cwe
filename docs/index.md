# cwe

This project is a LinkML model of the Common Weakness Enumeration (CWE) List, version 5.0, and of the XML Schema (XSD) version 8.0 it is written in. It keeps the XSD's own element names and values, so the whole catalogue validates with both unchanged, once one fixed step has turned its XML into JSON.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together, how the XML becomes JSON and what the model leaves out
- [`cwe.yaml`](schema/cwe.yaml): the schema, with its modules merged

## Validating a catalogue

```bash
uv run scripts/cwec_to_json.py upstream/cwec_v5.0.xml.zip -o tmp/cwec_v5.0.json
uv run linkml-validate -s src/cwe/schema/cwe.yaml -C CweWeaknessCatalog tmp/cwec_v5.0.json
```

The first command needs only Python's standard library. `project/jsonschema/cwe.schema.json` is the same schema for anyone without LinkML. JSON Schema looks at one value at a time, so a consumer that wants every rule also runs `tests/cwe_rules.py`, which checks that a reference names an entry of the right kind, and that no two entries or sources share an identifier.

## What was checked

All 984 weaknesses, 431 groupings, 62 views and 1081 external references of CWE 5.0 pass the committed JSON Schema and those rules with no departure, and load into the generated dataclasses and Pydantic models. `tests/test_catalogue.py` shows that the conversion loses nothing, and `tests/test_coverage.py` walks the XSD beside the classes and fails on anything missing, added or of another cardinality.
