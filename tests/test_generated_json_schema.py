"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/cwe.schema.json is what a consumer without LinkML validates
with. It is read here under the draft it declares, and held to the generator's
settings in .linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "cwe.schema.json"
SCHEMA = ROOT / "src" / "cwe" / "schema" / "cwe.yaml"
DATA = ROOT / "tests" / "data"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def validator():
    return jsonschema.validators.validator_for(schema())(schema())


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_the_catalogue():
    """The file's root takes a whole catalogue, and refuses any other key."""
    assert schema()["title"] == "cwe"
    assert schema()["additionalProperties"] is False
    assert set(schema()["properties"]) == {
        "Name",
        "Version",
        "Date",
        "Weaknesses",
        "Groupings",
        "Views",
        "External_References",
    }
    assert set(schema()["required"]) == {"Name", "Version", "Date"}


def test_every_class_is_closed():
    """A key the XSD does not declare is refused everywhere."""
    for name, definition in schema()["$defs"].items():
        if definition.get("type") == "object":
            assert definition["additionalProperties"] is False, name


@pytest.mark.parametrize(
    "name",
    ["CweWeaknessCatalog-small"],
)
def test_a_catalogue_validates_against_the_file(name):
    assert not list(validator().iter_errors(_load(DATA / "valid" / f"{name}.yaml")))


def test_a_rule_reaches_the_file():
    """A rule in the schema is a condition in the committed file: a compound weakness
    that says it is simple is refused there too, inside a catalogue."""
    catalogue = _load(DATA / "valid" / "CweWeaknessCatalog-small.yaml")
    catalogue["Weaknesses"][0]["Abstraction"] = "Compound"
    assert list(validator().iter_errors(catalogue))
