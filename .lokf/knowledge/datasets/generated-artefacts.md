---
type: Dataset
id: https://w3id.org/lmodel/cwe/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the cwe schema: the projections in `project/`, the Python models in `src/cwe/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/cwe-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: the docstring
  - id: test_datamodel.py
    resource: tests/test_datamodel.py
    title: the docstring
  - resource: .linkml/generators.yaml
  - resource: project
  - resource: src/cwe/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/cwe/datamodel/`. `just gen-doc` writes the merged schema to `docs/schema/cwe.yaml` and the element pages to `docs/elements/`, which git ignores.[^justfile]

`project/jsonschema/cwe.schema.json` is what a consumer without LinkML validates with. `tests/test_generated_json_schema.py` holds it to the generator's output.[^test_generated_json_schema.py]

The generated dataclasses and Pydantic models both load the whole catalogue.[^test_datamodel.py]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, the docstring
[^test_datamodel.py]: tests/test_datamodel.py, the docstring
