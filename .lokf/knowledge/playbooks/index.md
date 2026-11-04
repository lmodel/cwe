# Playbooks

* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/cwe/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Validate a catalogue](validate-a-catalogue.md) - How to validate a release of the CWE List: run `scripts/cwec_to_json.py` over MITRE's XML or ZIP, run `linkml-validate` on the result with the class `CweWeaknessCatalog`, and run the rules in `tests/cwe_rules.py` for what JSON Schema cannot state.
* [Move to another edition](update-upstream-pins.md) - How to move the schema to another edition when the watch reports one: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let `tests/test_coverage.py` show what the new XSD changed.
* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
