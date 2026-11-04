---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/cwe/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: cwe Knowledge Bundle
description: Common Weakness Enumeration (CWE) List 5.0 and Schema 8.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/cwe/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# cwe Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for cwe. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/cwe`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Datasets

* [cwe LinkML schema](datasets/cwe-linkml-schema.md) - The LinkML model of the CWE List 5.0 and its XML Schema 8.0, `src/cwe/schema/cwe.yaml` (schema id `https://w3id.org/lmodel/cwe`): an umbrella that holds only the tree root `CweWeaknessCatalog`, over the modules `cwe_core` and `cwe_entries`. Search it for weaknesses, groupings, views and external references.
* [Core module](datasets/core-module.md) - `src/cwe/schema/cwe_core.yaml`, the module with the schema's types, its enums of the XSD's value lists, and the value classes every entry shares: `CweExternalReference`, `CweReference`, `CweNote`, `CweDimension`, `CweCustomPhase`, `CweTaxonomyMapping` and the content history.
* [Entries module](datasets/entries-module.md) - `src/cwe/schema/cwe_entries.yaml`, the module with the abstract `CweEntry` and its three kinds, `CweWeakness`, `CweGrouping` and `CweView`, with what a weakness holds: related weaknesses, platforms, modes of introduction, consequences, detection methods, mitigations and worked examples.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the cwe schema: the projections in `project/`, the Python models in `src/cwe/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: a valid example of each class, most of them real pieces of the CWE List, a counter-example for each constraint, and counter-examples for the rules on a whole catalogue that JSON Schema cannot state.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/`: the CWE List 5.0 as MITRE's ZIP, the XSD 8.0 and the Terms of Use, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and `tests/test_upstream.py` holds the folder to that list.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/cwe.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CweEntry` and `CweExternalReference`, with `ID` and `Reference_ID` dropped for LOKF's `id`, and five keys folded into LOKF's `title` and `description`.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of twelve released lmodel repositories in `tests/neighbours/`, among them capec, cve, kev-catalog, nist-nvd, spdx and stix, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.
* [Mapping term list](datasets/mapping-term-list.md) - `tests/upstream/mapping-terms.txt`, the classes and properties of Dublin Core, schema.org, SKOS and the SEPSES CWE ontology, which `scripts/extract_mapping_terms.py` writes from each vocabulary's pinned file and `tests/test_mappings.py` holds each mapping to.
* [A Catalog of Security Architecture Weaknesses.](datasets/example-external-reference.md) - The external reference REF-9 of CWE 5.0, written as a concept of type `CweExternalReference` in the adapt copy's keys. It shows that the domain schema admits a source as a concept, with its other address and its access restriction.

# Explanations

* [The XSD's keys and values](explanations/keys-and-values.md) - Why slots and permissible values keep the XSD's spelling, such as `Related_Weaknesses`, `CWE_ID` and `Automated Static Analysis - Source Code`, while classes and enums take a `Cwe` prefix: the catalogue must validate with both unchanged, and `.linkmllint.yaml` says so.
* [From XML to JSON](explanations/from-xml-to-json.md) - How `scripts/cwec_to_json.py` turns MITRE's XML into the JSON that the schema describes: wrappers become lists, text beside attributes goes under `Value`, XHTML stays a fragment, and the prose and code of an example stay in order under `Entries`.
* [Which file is the schema](explanations/which-xsd.md) - Why the schema renders `cwe_schema_v8.0.xsd` and not `cwe_schema_latest.xsd`: CWE 5.0 names the versioned file and validates against it, while the file behind the latest link is an earlier copy of 8.0 that the catalogue breaks in 69 places.
* [Grouping, not category](explanations/grouping-not-category.md) - Why the schema has `CweGrouping` and no category class: schema 8.0 renamed Category to Grouping to end the confusion with Class, CWE 5.0 holds no category, and `tests/test_coverage.py` names `CategoryType` as its one exclusion, although the XSD still declares it.
* [References and identifiers](explanations/references-and-identifiers.md) - Why `ID`, `CWE_ID` and `View_ID` are digit strings that range over the class they name, why `Reference_ID` has no pattern, and why `tests/cwe_rules.py` checks over a whole catalogue what a generated JSON Schema cannot: that a reference resolves to an entry of the right kind.
* [What the data shows and the schema does not say](explanations/what-the-data-shows.md) - Facts about CWE 5.0 that no upstream text states, which stay in `tests/test_catalogue.py` and out of the schema: every deprecated entry is named so and barred from mapping, every grouping and view is barred from mapping, and each link is written in one direction only.
* [Mappings](explanations/mappings.md) - How the schema crosses to other vocabularies: `exact_mappings` where SEPSES reads the same XML key, `close_mappings` to SKOS, schema.org and Dublin Core, `related_mappings` to lmodel/cve, lmodel/kev-catalog, lmodel/nist-nvd, lmodel/capec and SPDX. Each is held to a pinned term list or a neighbour copy.
* [RDF through JSON-LD](explanations/rdf-through-json-ld.md) - How to get RDF from the catalogue: apply the generated context `project/jsonld/cwe.context.jsonld` with the schema's namespace as the base, so that CWE-79 is `cwe:79`. LinkML's own `linkml-convert -t rdf` fails on an identifier that is not a CURIE.
* [What the schema does not cover](explanations/scope.md) - What the schema leaves out on purpose: the category kept in XSD 8.0, the parallel CWE 4.x line under schema 7.x, the JSON of the CWE REST API, and any claim about whether what an entry says is true.

# Glossary

* [Entry](glossary/entry.md) - An entry of the CWE List: any item with its own identifier, which is a weakness, a grouping or a view. `CweEntry` is the abstract class of all three.
* [Weakness](glossary/weakness.md) - A weakness: a type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack. `CweWeakness` models it, with its `Abstraction` and `Structure`.
* [Grouping](glossary/grouping.md) - A grouping: a set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category, and `CweGrouping` models it.
* [View](glossary/view.md) - A view: a way of looking at the catalogue, as a subset of its entries from one standpoint. `CweView` models it, and its `Type` is `Graph`, `Explicit` or `Implicit`.
* [Abstraction](glossary/abstraction.md) - The abstraction of a weakness: how far it is described in general terms or tied to a specific product. `CweAbstraction` lists `Pillar`, `Class`, `Base`, `Variant` and `Compound`.
* [Chain and composite](glossary/compound.md) - A compound weakness, which is a chain or a composite: a chain is several weaknesses reached one after another, and a composite is several that must occur together. CWE 5.0 has three chains and four composites.
* [Related nature](glossary/related-nature.md) - The nature of a link between two weaknesses: `ChildOf`, `ParentOf`, `StartsWith`, `CanFollow`, `CanPrecede`, `RequiredBy`, `Requires`, `CanAlsoBe`, `PeerOf` or `Overlaps`. `CweRelatedNature` lists them.
* [Mapping notes](glossary/mapping-notes.md) - Mapping notes: the guidance on whether a real vulnerability may be mapped to an entry as its root cause. `CweMappingNotes` holds the `Usage`, which is `Allowed`, `Allowed-with-Review`, `Discouraged` or `Prohibited`, with the reasons and suggestions.
* [Structured text](glossary/structured-text.md) - Structured text: text that may hold XHTML, as a well-formed fragment without the namespace prefix and with its special characters escaped. `cwe_structured_text` is its type, and a consumer that shows it as HTML must sanitize it first.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.

# Playbooks

* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/cwe/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Validate a catalogue](playbooks/validate-a-catalogue.md) - How to validate a release of the CWE List: run `scripts/cwec_to_json.py` over MITRE's XML or ZIP, run `linkml-validate` on the result with the class `CweWeaknessCatalog`, and run the rules in `tests/cwe_rules.py` for what JSON Schema cannot state.
* [Move to another edition](playbooks/update-upstream-pins.md) - How to move the schema to another edition when the watch reports one: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let `tests/test_coverage.py` show what the new XSD changed.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the XSD says, a rule states only what the upstream states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, the CWE List and its XSD under MITRE's CWE Terms of Use, with the designation and licence those terms ask each copy to reproduce. No endorsement by MITRE or the CWE Program is implied.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in the CWE List or its XSD belongs with the CWE Program.

# References

* [CWE List](references/cwe-list.md) - The Common Weakness Enumeration list of software and hardware weakness types, which The MITRE Corporation publishes for the CWE Program. The schema renders version 5.0 of 28 October 2026, which holds 984 weaknesses, 431 groupings, 62 views and 1081 external references.
* [CWE Schema](references/cwe-schema.md) - The XML Schema of the CWE List, version 8.0 of 28 October 2026, namespace `http://cwe.mitre.org/cwe-8`, at `https://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd`. The schema renders this file, a copy of which `upstream/` holds.
* [CWE Terms of Use](references/cwe-terms-of-use.md) - MITRE's terms for using the CWE: a non-exclusive, royalty-free licence for research, development and commercial purposes, on condition that a copy reproduces MITRE's copyright designation and the licence. `upstream/TERMS.txt` holds the text, and the watch compares it.
* [CWE REST API](references/cwe-rest-api.md) - The CWE-CAPEC REST API working group's JSON form of the CWE, at `cwe-api.mitre.org`, with schemas in the `CWE-CAPEC/REST-API-wg` repository. It is not the source of this schema, because its schemas date from 2024 and its keys are not consistent. `Value` and `Entries` take its names.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another edition of the CWE List, a changed XSD, a change behind the latest link, a newer schema on the archive page or changed Terms of Use fails the run and opens or updates an issue.
