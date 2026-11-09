# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.62.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.61.0...v0.62.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-librarian.sh`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-sync.sh`, `.lokf/justfile` and `website/scripts/sync.mjs` here.

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `cwe.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-04

### Added

- **A LinkML rendering of the Common Weakness Enumeration (CWE) List 5.0 and its XML Schema 8.0**, as an umbrella over `cwe_core` and `cwe_entries`. Keys and values are the XSD's own, every description is this project's, and the abstract `CweEntry` holds what a weakness, a grouping and a view share.
- **`scripts/cwec_to_json.py`**, the one fixed step from MITRE's XML to the JSON the schema describes, which stops on anything the XSD does not declare.
- **The upstream's rules**: compound weaknesses and their structure, a custom phase's value and its domain, and a platform's name or class. What JSON Schema cannot state, that a reference resolves and that an identifier is unique, `tests/cwe_rules.py` checks.
- **A test that walks the XSD beside the classes**, and fails on anything missing, added or of another cardinality, and a test that the whole catalogue validates and that the conversion loses nothing.
- **A weekly upstream watch** that reports a new edition, a changed XSD, a change behind the `cwe_schema_latest.xsd` link, a newer schema on the archive page, or changed Terms of Use.
- **Mappings to the SEPSES CWE ontology, SKOS, schema.org, Dublin Core, SPDX 3.0.1, Wikidata, lmodel/cve, lmodel/kev-catalog and lmodel/nist-nvd**, each held by a test to a pinned term list or a released copy.
- **`.lokf/cwe.yaml`, the schema's `lokf adapt` copy, rooted on `CweEntry` and `CweExternalReference`.** The knowledge release attaches it as `schema-<tag>-cwe.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The schema moves from CWE 4.19.1 and XSD 7.3 to CWE 5.0 and XSD 8.0**, so `Category` becomes `Grouping`, and technical nuance, dimensions, custom phases, the `Overlaps` nature and the keys that describe a citation arrive.
- **Keys and values take the XSD's spelling**, such as `Related_Weaknesses` and `ChildOf`, in place of snake_case slots and upper-case values, and classes and enums take the `Cwe` prefix. An identifier is a digit string that ranges over the class it names.
- **The template moves to linkml-project-copier v0.5.0**, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `cwe-linkml`. PyPI publishing stays off.

### Removed

- **`NVDWeaknessObservation`, `WeaknessSource`, the slots `tags` and `source`, and the subsets**, which render nothing in the XSD. lmodel/nist-nvd models what NVD says.
- **The Wikidata mapping to Q429785**, which is a poster.
- **The hand-kept SSSOM file under `src/cwe/mappings/`.** No source confirmed its rows, and the schema is now the one home for mappings.
- **CWE 4.19.1's XML and CSV files, the script that derived test data from them, the patched generator script, and the mkdocs site.** The knowledge website replaces the site.
