## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/cwe.yaml` is the copy `lokf adapt` writes from the schema so that it can
# sit beside `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are
# the two classes that carry the schema's identifiers: CweEntry, the abstract base
# of a weakness, a grouping and a view, and CweExternalReference. A concept names
# CweWeakness, CweGrouping, CweView or CweExternalReference as its `type`, and LOKF's
# `id` stands for the number, which adapt drops. The folds put what the XSD calls
# Name, Title, Description, Summary and Objective into the concept's own `title` and
# `description`. The recipes run the `lokf` the sidecar's floor pins (0.9.0 or
# later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root CweEntry --root CweExternalReference --prefix cwe --fold CweEntry.Name=title --fold CweExternalReference.Title=title --fold CweWeakness.Description=description --fold CweGrouping.Summary=description --fold CweView.Objective=description"

# Rewrite .lokf/schema/cwe.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/cwe.yaml

# Fail when .lokf/schema/cwe.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/cwe.yaml --check

# ============ Artefacts gen-project does not write ============

# Write one LinkML YAML with every import merged, as the copier template's recipe does
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# Write the schema as RDF Turtle; gen-project's rdf generator is switched off in LinkML
[group('model development - extended')]
gen-rdf:
  mkdir -p {{dest}}/rdf
  uv run gen-rdf --mergeimports {{source_schema_path}} > {{dest}}/rdf/{{schema_name}}.ttl
