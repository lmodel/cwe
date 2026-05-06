## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Derive schema-compliant test data from the CWE XML catalog
[group('model development')]
gen-cwe-data xml_input="tests/data/cwe/cwec_v4.19.1.xml" yaml_output="tests/data/valid/WeaknessCatalog-001.yaml":
  uv run python tests/data/cwe/derive_test_data.py {{xml_input}} {{yaml_output}}

# Fix Python reserved keyword 'class' generated as an attribute name due to alias.
# This is needed because gen-python emits 'class:' and 'self.class' verbatim
# when the slot alias is 'class', which is a Python keyword.
# Also patches _normalize_inlined_as_list calls for slots whose key field is an
# enum type, which triggers a linkml_runtime comparison bug (enum != TypedNode).
fix-python-keywords:
        sed -i \
                -e 's/\bclass: Optional\b/class_: Optional/g' \
                -e 's/self\.class\b/self.class_/g' \
                -e 's/cwe\.class\b/cwe["class"]/g' \
                -e 's/MITRE_CWE\.class\b/MITRE_CWE["class"]/g' \
                {{pymodel}}/{{schema_name}}.py
        uv run python scripts/fix_gen_python.py {{pymodel}}/{{schema_name}}.py
