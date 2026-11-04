"""Checks what the generated models and the JSON-LD context do with real data.

The Pydantic models and the dataclasses load the whole catalogue. RDF goes through
JSON-LD with the generated context, because LinkML's RDF dumper cannot expand an
identifier that is not a CURIE, and docs/about.md says so. These tests hold both
sentences.
"""

import json
from functools import cache
from pathlib import Path

import pytest
import rdflib
import yaml
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import json_loader
from linkml_runtime.utils.schemaview import SchemaView

from cwe.datamodel import cwe as dataclasses_module
from cwe.datamodel import cwe_pydantic
from tests import conversion

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cwe" / "schema" / "cwe.yaml"
CONTEXT = ROOT / "project" / "jsonld" / "cwe.context.jsonld"
SMALL = ROOT / "tests" / "data" / "valid" / "CweWeaknessCatalog-small.yaml"
NAMESPACE = "https://w3id.org/lmodel/cwe/"


@cache
def small():
    return yaml.safe_load(SMALL.read_text(encoding="utf-8"))


def test_the_whole_catalogue_loads_into_the_pydantic_models():
    model = cwe_pydantic.CweWeaknessCatalog(**conversion.catalogue())
    assert len(model.Weaknesses) == 984
    weakness = next(w for w in model.Weaknesses if w.ID == "79")
    assert weakness.Abstraction == "Base"


def test_the_whole_catalogue_loads_into_the_dataclasses():
    catalogue = json_loader.loads(
        json.dumps(conversion.catalogue()),
        target_class=dataclasses_module.CweWeaknessCatalog,
    )
    assert len(catalogue.Weaknesses) == 984
    assert len(catalogue.External_References) == 1081


def test_a_value_with_punctuation_survives_the_python_enums():
    """A value such as C++ or None keeps its text, whatever name Python gives it."""
    assert cwe_pydantic.CweLanguageName("C++").value == "C++"
    assert cwe_pydantic.CweEffectiveness("None").value == "None"


def _graph(document):
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]
    data = dict(document, **{"@context": context})
    graph = rdflib.Graph()
    graph.parse(data=json.dumps(data), format="json-ld", base=NAMESPACE)
    return graph


def test_json_ld_gives_an_entry_its_iri_and_a_link_its_target():
    """An entry's number becomes its IRI under this schema's namespace, and a
    reference an IRI too, so the links of the catalogue are links in RDF."""
    graph = _graph(small())
    weakness = rdflib.URIRef(f"{NAMESPACE}2")
    name = rdflib.URIRef(f"{NAMESPACE}Name")
    assert str(graph.value(weakness, name)) == "An example of a specific weakness"
    related = graph.value(weakness, rdflib.URIRef(f"{NAMESPACE}Related_Weaknesses"))
    target = graph.value(related, rdflib.URIRef(f"{NAMESPACE}CWE_ID"))
    assert target == rdflib.URIRef(f"{NAMESPACE}1")


def test_linkmls_rdf_dumper_cannot_expand_the_identifiers():
    """The reason for the route above, which a fix in LinkML would make needless. A
    failure here is good news: tell docs/about.md."""
    catalogue = json_loader.loads(
        json.dumps(small()), target_class=dataclasses_module.CweWeaknessCatalog
    )
    with pytest.raises(ValueError, match="Unknown CURIE prefix"):
        rdflib_dumper.dumps(catalogue, schemaview=SchemaView(str(SCHEMA)))
