"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
import json
import keyword
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
SOURCE_DIR = ROOT / "src" / "cwe" / "schema"
COPY = ROOT / ".lokf" / "cwe.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/attack v0.1.1, schema-v0.1.1-attack.yaml
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/cve v0.1.0, schema-v0.1.0-cve.yaml
    "cve.yaml": "33e6086a81ac8e4cdc1e6143598cfcc961cbc1864ad9268773da9e863c652a73",
    # lmodel/kev-catalog v0.1.0, schema-v0.1.0-kev-catalog.yaml
    "kev-catalog.yaml": "76bdff7d02cc34ac6a14314692e316b005649a34f442eaf54c2846b1dac5396c",
    # lmodel/nist-nvd v0.1.0, schema-v0.1.0-nist-nvd.yaml
    "nist-nvd.yaml": "69dc8a9b34cc6646cf44515c121c8924c4e07232a9699e31065fb8930ed8be40",
    # lmodel/capec, .lokf/capec.yaml on feat/first-release, since capec has no release
    # yet. Move this to schema-v0.1.0-capec.yaml once it has one.
    "capec.yaml": "3f99bbb793ceac4240e016c62756052afb4bd4ddcd815d6b077763d3feba14a2",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour. The keys here begin with a capital, as the
# XSD writes them, and the neighbours' begin with a small letter, so only the
# capitalised keys of a neighbour could overlap. A new overlap fails this test. No
# class, enum or type is shared, since each carries the Cwe or cwe_ prefix.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}

# lmodel/capec is the exception. MITRE writes both XSDs in one style, so the two copies
# share these keys, and a composite of the two is the plan's risk of keys shared across
# copies until lokf's adapt can rename what a neighbour copy defines (lokf #169).
SHARED_WITH_NEIGHBOURS["capec.yaml"] = {
    "Abstraction",
    "Alternate_Terms",
    "Audience",
    "Author",
    "CAPEC_ID",
    "CWE_ID",
    "Consequence_ID",
    "Content_History",
    "Contribution",
    "Contribution_Comment",
    "Contribution_Date",
    "Contribution_Name",
    "Contribution_Organization",
    "Date",
    "Description",
    "Edition",
    "Entry_ID",
    "Entry_Name",
    "Extended_Description",
    "External_Reference_ID",
    "External_References",
    "Filter",
    "Has_Member",
    "Impact",
    "Likelihood",
    "Mapping_Fit",
    "Member_Of",
    "Members",
    "Modification",
    "Modification_Comment",
    "Modification_Date",
    "Modification_Importance",
    "Modification_Name",
    "Modification_Organization",
    "Name",
    "Nature",
    "Note",
    "Notes",
    "Phase",
    "Previous_Entry_Name",
    "Publication",
    "Publication_Day",
    "Publication_Month",
    "Publication_Year",
    "Publisher",
    "References",
    "Related_Attack_Patterns",
    "Related_Weaknesses",
    "Relationships",
    "Scope",
    "Section",
    "Status",
    "Submission",
    "Submission_Comment",
    "Submission_Date",
    "Submission_Name",
    "Submission_Organization",
    "Taxonomy_Mappings",
    "Taxonomy_Name",
    "Term",
    "Type",
    "URL",
    "URL_Date",
    "Value",
    "Version",
    "Views",
}

# The classes `just lokf-adapt` re-roots on Concept, and the four a concept can name,
# which the README lists for the plugins' Known LOKF types setting.
ROOTS = {"CweEntry", "CweExternalReference"}
CONCEPT_TYPES = {"CweWeakness", "CweGrouping", "CweView", "CweExternalReference"}

# What the copy folds into LOKF's slots, so that a concept writes its own title and
# description, and the identifiers it drops for LOKF's id.
FOLDED = {
    ("CweEntry", "Name"): "title",
    ("CweExternalReference", "Title"): "title",
    ("CweWeakness", "Description"): "description",
    ("CweGrouping", "Summary"): "description",
    ("CweView", "Objective"): "description",
}
DROPPED = {("CweEntry", "ID"), ("CweExternalReference", "Reference_ID")}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _load(path):
    return yaml.safe_load(path.read_text())


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _terms(doc):
    """The IRI of every class, slot, attribute, enum and type a schema file
    declares, each its own URI or the default prefix and its name."""
    expand = _expander(doc)
    default = doc.get("default_prefix")
    terms = set()
    for kind, uri_key in (
        ("classes", "class_uri"),
        ("slots", "slot_uri"),
        ("enums", "enum_uri"),
        ("types", "uri"),
    ):
        for name, element in (doc.get(kind) or {}).items():
            terms.add(expand((element or {}).get(uri_key) or f"{default}:{name}"))
    for cls in (doc.get("classes") or {}).values():
        for name, slot in ((cls or {}).get("attributes") or {}).items():
            terms.add(expand((slot or {}).get("slot_uri") or f"{default}:{name}"))
    return terms


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the file pinned above."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def _source():
    """The three modules of the source, merged by element kind."""
    merged = {"classes": {}, "slots": {}, "prefixes": {}, "enums": {}, "types": {}}
    for path in sorted(SOURCE_DIR.glob("*.yaml")):
        doc = _load(path)
        for kind, elements in merged.items():
            elements.update(doc.get(kind) or {})
    return merged


def test_the_copy_drops_and_folds_only_what_is_named():
    """Each class of the copy keeps the source's attributes, but for the identifiers
    it drops for LOKF's id and the keys it folds into LOKF's title and description."""
    source, copy = _source(), _load(COPY)
    assert set(copy["classes"]) == set(source["classes"])
    assert set(copy.get("slots") or {}) == set(source["slots"])
    for name, cls in source["classes"].items():
        kept = set(cls.get("attributes") or {})
        kept -= {key for owner, key in FOLDED if owner == name}
        kept -= {key for owner, key in DROPPED if owner == name}
        assert set(copy["classes"][name].get("attributes") or {}) == kept, name


def test_each_fold_leaves_the_slot_on_the_class():
    """A concept of a class with a fold carries LOKF's slot, required as the XSD
    requires the key it stands for."""
    copy = _load(COPY)
    for (owner, _), slot in FOLDED.items():
        cls = copy["classes"][owner]
        assert slot in cls["slots"], owner
        assert cls["slot_usage"][slot]["required"] is True, owner


def test_no_key_of_the_source_is_a_slot_of_lokf():
    """adapt renames a top-level slot and never an attribute, so an attribute named
    like one of LOKF's slots would keep that name in the copy. A key here begins with
    a capital, and LOKF's do not."""
    source = _source()
    lokf_slots = set(_load(LOKF)["slots"])
    for name, cls in source["classes"].items():
        assert not set(cls.get("attributes") or {}) & lokf_slots, name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the classes with an identifier on Concept, keeps the
    three kinds of entry under the base, leaves the tree root out of the concept types,
    and imports nothing but the LinkML types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    for name in ("CweWeakness", "CweGrouping", "CweView"):
        assert doc["classes"][name]["is_a"] == "CweEntry", name
    assert doc["imports"] == ["linkml:types", "lokf"]
    assert not doc["classes"]["CweWeaknessCatalog"].get("tree_root")


def test_the_readme_lists_the_concept_types():
    """The README's Known LOKF types block names each class a concept may use."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in CONCEPT_TYPES:
        assert name in readme, name


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_each_mapping_into_a_neighbour_names_a_term_it_declares():
    """A mapping into a released neighbour's own namespace names a term its copy
    declares. tests/test_mappings.py checks the rest against their files."""
    doc = _load(COPY)
    expand = _expander(doc)
    namespaces = {}
    for name in NEIGHBOURS:
        theirs = _load(NEIGHBOUR_DIR / name)
        default = theirs.get("default_prefix")
        namespace = (theirs.get("prefixes") or {}).get(default)
        if namespace:
            namespaces[namespace] = (name, _terms(theirs))
    mapped_into = 0
    for mapping in _mappings(doc):
        iri = expand(mapping)
        for namespace, (name, terms) in namespaces.items():
            if iri.startswith(namespace):
                assert iri in terms, (mapping, name)
                mapped_into += 1
    assert mapped_into >= 2


def _page_names(source):
    """The name of each page gen-doc writes for an element of the source."""
    names = set(source["classes"]) | set(source["enums"]) | set(source["slots"])
    names |= {
        "".join(part.title() for part in name.split("_")) for name in source["types"]
    }
    for cls in source["classes"].values():
        names |= set(cls.get("attributes") or {})
    return names


def test_no_two_pages_differ_only_by_case():
    """gen-doc writes a page per element, and two names that differ only by case
    are one file on a case-insensitive disk. A slot keeps the upstream's key and every
    class, enum and type carries a prefix of this schema's, so no two can."""
    source = _source()
    lowered = {}
    for name in _page_names(source):
        lowered.setdefault(name.lower(), set()).add(name)
    assert not {key: found for key, found in lowered.items() if len(found) > 1}


def test_the_one_page_that_collides_is_date():
    """The key Date and the Date type of LinkML share a page name exactly, and a
    schema can rename neither. So docs/elements/Date.md describes only one of them,
    and each class page still describes its own key."""
    linkml_types = {
        "Boolean", "Curie", "Date", "DateOrDatetime", "Datetime", "Decimal", "Double",
        "Float", "Integer", "Jsonpath", "Jsonpointer", "Ncname", "Nodeidentifier",
        "Objectidentifier", "Sparqlpath", "String", "Time", "Uri", "Uriorcurie",
    }  # fmt: skip
    assert _page_names(_source()) & linkml_types == {"Date"}


def test_no_page_overwrites_the_index():
    """A slot named index would overwrite the docs site's index page."""
    assert "index" not in {name.lower() for name in _page_names(_source())}


def test_no_slot_is_a_python_keyword():
    """A slot named after a Python keyword breaks the generated dataclasses."""
    source = _source()
    slots = set(source["slots"])
    for cls in source["classes"].values():
        slots |= set(cls.get("attributes") or {})
    assert not {name for name in slots if keyword.iskeyword(name)}


def _concept_schema():
    """The JSON Schema of the adapt copy, as `lokf validate` reads it beside LOKF."""
    generator = JsonSchemaGenerator(str(COPY), mergeimports=True)
    return json.loads(generator.serialize())["$defs"]


# What a concept of each type holds beside the example it comes from: the keys adapt
# drops or folds go, and LOKF's stand for them.
_CONCEPT_EXAMPLES = {
    "CweWeakness": ("CweWeakness-smallest", ("ID", "Name", "Description")),
    "CweGrouping": ("CweGrouping-smallest", ("ID", "Name", "Summary")),
    "CweView": ("CweView-smallest", ("ID", "Name", "Objective")),
    "CweExternalReference": (
        "CweExternalReference-smallest",
        ("Reference_ID", "Title"),
    ),
}


def test_a_concept_of_each_type_validates_against_the_copy():
    """Each class a concept may name admits a real example, in the copy's keys."""
    definitions = _concept_schema()
    for class_name, (example, moved) in _CONCEPT_EXAMPLES.items():
        data = _load(ROOT / "tests" / "data" / "valid" / f"{example}.yaml")
        concept = {key: value for key, value in data.items() if key not in moved}
        concept.update(
            type=class_name,
            id=f"https://example.org/knowledge/{class_name}",
            title="A title",
            description="A description.",
        )
        schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions}
        validator = jsonschema.validators.validator_for(schema)(schema)
        errors = [e.message[:160] for e in validator.iter_errors(concept)]
        assert not errors, (class_name, errors)
        concept.pop("title")
        assert list(validator.iter_errors(concept)), (class_name, "needs a title")


def test_the_pen_refuses_a_status_key_on_create():
    """KTL v0.61.0's pen compares a key with its reserved names without regard to
    case, so a concept of a kind of entry, which this schema requires to hold
    `Status`, cannot be created through it. Only CweExternalReference can. This test
    fails when a KTL sync brings a pen that compares exact case: then the bundle's
    example can move to a CweWeakness, and the README's note can go."""
    pen = (ROOT / ".lokf" / "scripts" / "knowledge-apply.py").read_text(
        encoding="utf-8"
    )
    assert "k.lower() in DENIED_CREATE" in pen
