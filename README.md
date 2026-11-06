<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# cwe

Common Weakness Enumeration (CWE) List 5.0 and Schema 8.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/cwe](https://lmodel.github.io/cwe)

## What it models

The schema renders the [CWE List](https://cwe.mitre.org/data/index.html), version 5.0 of 28 October 2026, through its XML Schema, version 8.0: weaknesses, the groupings that used to be called categories, views and external references. It keeps the XML Schema's own names and values, so the whole catalogue validates with both unchanged, after `scripts/cwec_to_json.py` has turned its XML into JSON.

`upstream/` holds both files, pinned by hash, and `tests/test_coverage.py` holds the schema to the XML Schema in both directions. All 984 weaknesses, 431 groupings, 62 views and 1081 external references validate with no departure. A weekly workflow opens an issue when a new edition appears, a pinned file changes, or the Terms of Use change. [docs/index.md](docs/index.md) says how to validate a catalogue, and [docs/about.md](docs/about.md) what the conversion does and which of MITRE's two schema files this is.

## Mappings

The schema is the one home for mappings. The hand-kept SSSOM file that sat under `src/cwe/mappings/` is gone, since no source confirmed its rows.

* **[SEPSES](https://www.sepses.org/vocab/ref/cwe/) CWE ontology**: `close_mappings` on the classes and `exact_mappings` on the keys its conversion reads from the same XML. `tests/test_mappings.py` checks each against the term list from its pinned file.
* **[SKOS](https://www.w3.org/TR/skos-reference/), [schema.org](https://schema.org/) and [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)**: `close_mappings` for a weakness as a concept and a defined term, the catalogue as a scheme, a grouping as a collection and the fields of a citation, and `related_mappings` for a view as a scheme. `tests/test_mappings.py` checks each against the term list from their pinned files.
* **[lmodel/cve](https://github.com/lmodel/cve), [lmodel/kev-catalog](https://github.com/lmodel/kev-catalog) and [lmodel/nist-nvd](https://github.com/lmodel/nist-nvd)**: `related_mappings` to the fields that name a weakness in a vulnerability record. `tests/test_mappings.py` checks each against its released copy.
* **[lmodel/capec](https://github.com/lmodel/capec)**: `related_mappings` from the link to an attack pattern and its number, and `close_mappings` on an external reference. `tests/test_schema_rules.py` checks them against capec's copy, and `tests/test_catalogue.py` holds the 1212 pairs both catalogues name.
* **[SPDX](https://spdx.github.io/spdx-spec/v3.0.1/) 3.0.1 Core**: `related_mappings` on a weakness to `ExternalRefType/cwe`. `tests/test_mappings.py` checks it against lmodel/spdx's released copy.
* **[Wikidata](https://www.wikidata.org/wiki/Q2682392)**: `close_mappings` on the ID to the property P3624, and `related_mappings` on the catalogue to Q2682392. The term list names the two by hand, as read on 4 November 2026.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the conversion from XML, the upstream watch and the mapping term extractor
* [src/cwe/schema/](src/cwe/schema): the LinkML schema, `cwe.yaml`, `cwe_entries.yaml` and `cwe_core.yaml` (edit these)
* [src/cwe/datamodel/](src/cwe/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), the term list in [upstream/](tests/upstream) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the catalogue and its XML Schema at the pinned edition, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/cwe.yaml`, is the copy `just lokf-adapt` writes from `src/cwe/schema/cwe.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-cwe.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `CweEntry` and `CweExternalReference` on `Concept`, so a concept may be an entry of any kind or a source. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CweWeakness, CweGrouping, CweView, CweExternalReference
```

The copy drops `ID` and `Reference_ID` for LOKF's `id`. It folds `Name` and `Title` into LOKF's `title`, and `Description`, `Summary` and `Objective` into its `description`. Every other key keeps its capital, so no key is LOKF's. `tests/test_schema_rules.py` holds all this.

No key is another released copy's, but lmodel/capec's copy shares 66, such as `Status`. A host importing both validates each class against its own lists, while the shared keys project under one prefix, `cwe:`, until `lokf adapt` can rename what a neighbour copy defines (lokf #169).

KTL v0.61.0's librarian pen compares a key with its reserved names without regard to case, so it refuses the key `Status` that a weakness, a grouping or a view must hold. Until that changes, write such a concept by hand and let `just lokf-validate` check it. The bundle's own typed example is a `CweExternalReference`, which has no such key.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The CWE List and its XML Schema are under the CWE Terms of Use, and `upstream/` reproduces MITRE's designation and licence as those terms ask: see [NOTICE](NOTICE). This is not a project of the CWE Program or MITRE, and its use implies no endorsement by either. CWE is a trademark of The MITRE Corporation.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
