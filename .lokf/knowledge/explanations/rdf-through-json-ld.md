---
type: Explanation
id: https://w3id.org/lmodel/cwe/knowledge/explanations/rdf-through-json-ld
genre: explanation
title: RDF through JSON-LD
description: "How to get RDF from the catalogue: apply the generated context `project/jsonld/cwe.context.jsonld` with the schema's namespace as the base, so that CWE-79 is `cwe:79`. LinkML's own `linkml-convert -t rdf` fails on an identifier that is not a CURIE."
about:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/generated-artefacts
sources:
  - id: about.md
    resource: docs/about.md
    title: RDF
  - id: test_datamodel.py
    resource: tests/test_datamodel.py
    title: test_json_ld_gives_an_entry_its_iri_and_a_link_its_target
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# RDF through JSON-LD

An entry's number is its identifier, so the JSON-LD route gives each entry an IRI under the schema's namespace, and each reference an IRI too.[^about.md]

`linkml-convert -t rdf` fails with `Unknown CURIE prefix: @base`. `tests/test_datamodel.py` holds both statements, so a fix in LinkML shows up there.[^test_datamodel.py]

A key that means different things on different classes, such as `Type`, has one IRI, because the IRI names the XSD's key.[^about.md]

[^about.md]: docs/about.md, RDF
[^test_datamodel.py]: tests/test_datamodel.py, test_json_ld_gives_an_entry_its_iri_and_a_link_its_target
