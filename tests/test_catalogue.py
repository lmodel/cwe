"""Holds the schema to the whole catalogue, and records what the catalogue shows.

The first group of tests is the proof the schema is for: CWE 5.0, unchanged but for
the conversion, passes the committed JSON Schema and the rules on a whole catalogue,
and the conversion loses nothing. The second group records facts about CWE 5.0 that
no upstream text states. They are not rules of the schema, so a later edition may
break them, and each one then asks a person to look.
"""

import json
import xml.etree.ElementTree as ET
from collections import Counter
from functools import cache
from pathlib import Path
from xml.sax.saxutils import unescape

import jsonschema
import pytest

from tests import conversion
from tests.cwe_rules import rule_errors

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "cwe.schema.json"
XHTML = "{http://www.w3.org/1999/xhtml}"
SCHEMA_INSTANCE = "{http://www.w3.org/2001/XMLSchema-instance}"
ENTRY_LISTS = ("Weaknesses", "Groupings", "Views")
# Two empty elements of CWE 5.0, which the XSD allows.
EMPTY_AUTHOR = ["REF-1466"]
EMPTY_NOTE = ["1470"]


@cache
def document():
    return conversion.catalogue()


def _entries():
    for key in ENTRY_LISTS:
        yield from document()[key]


def test_the_catalogue_is_the_pinned_edition():
    assert document()["Name"] == "CWE"
    assert document()["Version"] == "5.0"
    assert document()["Date"] == "2026-10-28"
    assert Counter({k: len(document()[k]) for k in ENTRY_LISTS}) == Counter(
        Weaknesses=984, Groupings=431, Views=62
    )
    assert len(document()["External_References"]) == 1081


def test_the_catalogue_names_the_xsd_this_schema_renders():
    """The file's own schemaLocation is the versioned XSD held in upstream/."""
    location = conversion.xml_root().get(SCHEMA_INSTANCE + "schemaLocation")
    assert location.split() == [
        "http://cwe.mitre.org/cwe-8",
        "http://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd",
    ]


def test_the_whole_catalogue_passes_the_committed_json_schema():
    """Every key and value of every entry, with no departure."""
    schema = json.loads(COMMITTED.read_text(encoding="utf-8"))
    validator = jsonschema.validators.validator_for(schema)(schema)
    errors = list(validator.iter_errors(document()))
    assert not errors, [
        ("/".join(map(str, e.absolute_path)), e.message[:160]) for e in errors[:20]
    ]


def test_the_whole_catalogue_keeps_the_rules_json_schema_cannot_state():
    """Every reference resolves to an entry of the right kind, and no two entries
    or sources share an identifier."""
    assert not rule_errors(document())


def _xml_values(element):
    """Each attribute value and each stretch of text of the catalogue's XML."""
    for key, value in element.attrib.items():
        if not key.startswith(SCHEMA_INSTANCE):
            yield value
    if len(element) == 0 or any(c.tag.startswith(XHTML) for c in element):
        text = "".join(element.itertext()).strip()
        if text or not element.attrib:
            yield text
        return
    for child in element:
        yield from _xml_values(child)


def _json_values(node):
    if isinstance(node, dict):
        for value in node.values():
            yield from _json_values(value)
    elif isinstance(node, list):
        for value in node:
            yield from _json_values(value)
    else:
        yield node


def _plain(text):
    """A string of the JSON form as text, whether a fragment of XHTML or not."""
    try:
        return "".join(ET.fromstring(f"<r>{text}</r>").itertext()).strip()
    except ET.ParseError:
        return unescape(text).strip()


def test_the_conversion_loses_nothing():
    """Every attribute value and text of the XML is in the JSON form, as many times
    as the XML has it, and nothing else is."""
    xml = Counter(" ".join(v.split()) for v in _xml_values(conversion.xml_root()) if v)
    converted = Counter(" ".join(_plain(v).split()) for v in _json_values(document()))
    converted.pop("", None)
    assert not xml - converted, list((xml - converted).items())[:10]
    assert not converted - xml, list((converted - xml).items())[:10]


def test_a_structured_text_is_a_well_formed_fragment():
    """Each fragment parses, and carries no namespace prefix."""
    weakness = next(w for w in document()["Weaknesses"] if w["ID"] == "79")
    example = weakness["Demonstrative_Examples"][0]
    code = example["Entries"][0]["Example_Code"]
    assert code["Nature"] == "Bad"
    assert code["Language"] == "PHP"
    ET.fromstring(f"<r>{code['Value']}</r>")
    assert "xhtml:" not in code["Value"]
    assert "&lt;div" in code["Value"]


def test_the_entries_keep_their_order():
    """A worked example's prose and code stay in the order the XML gives them."""
    namespace = "{http://cwe.mitre.org/cwe-8}"
    weakness = next(
        w
        for w in conversion.xml_root().iter(namespace + "Weakness")
        if w.get("ID") == "79"
    )
    element = weakness.find(f"{namespace}Demonstrative_Examples").find(
        f"{namespace}Demonstrative_Example"
    )
    tags = [
        c.tag.removeprefix(namespace)
        for c in element
        if c.tag.removeprefix(namespace) in ("Body_Text", "Example_Code")
    ]
    converted = next(w for w in document()["Weaknesses"] if w["ID"] == "79")
    entries = converted["Demonstrative_Examples"][0]["Entries"]
    assert [next(iter(e)) for e in entries] == tags
    assert len(set(tags)) == 2


def test_the_converter_stops_on_what_the_xsd_does_not_declare():
    """A key from outside the XSD is a departure to notice, not to carry."""
    namespace = "http://cwe.mitre.org/cwe-8"
    root = ET.fromstring(
        f'<Weakness_Catalog xmlns="{namespace}" Name="CWE" Version="5.0" '
        f'Date="2026-10-28"><Not_A_Key/></Weakness_Catalog>'
    )
    with pytest.raises(ValueError, match="declares no element Not_A_Key"):
        conversion.CONVERTER.convert(root, conversion.xsd())
    root = ET.fromstring(
        f'<Weakness_Catalog xmlns="{namespace}" Name="CWE" Version="5.0" '
        f'Date="2026-10-28" Not_A_Key="x"/>'
    )
    with pytest.raises(ValueError, match="declares no attribute Not_A_Key"):
        conversion.CONVERTER.convert(root, conversion.xsd())


def test_the_converter_writes_what_it_is_asked_to(tmp_path):
    """The command line takes the ZIP and writes the same document as the function."""
    output = tmp_path / "deeper" / "catalogue.json"
    code = conversion.CONVERTER.main(
        [
            str(conversion.CATALOGUE_FILE),
            "--xsd",
            str(conversion.XSD_FILE),
            "-o",
            str(output),
        ]
    )
    assert code == 0
    assert json.loads(output.read_text(encoding="utf-8")) == document()


# What CWE 5.0 shows and no upstream text states. Each of these is a fact about one
# edition.


def test_a_deprecated_entry_is_named_so_and_barred_from_mapping():
    """Every deprecated entry's name starts DEPRECATED: and its usage is Prohibited,
    and no other entry's name starts so."""
    kinds = Counter()
    for entry in _entries():
        deprecated = entry["Status"] == "Deprecated"
        assert deprecated == entry["Name"].startswith("DEPRECATED:"), entry["ID"]
        if deprecated:
            kinds[entry["Mapping_Notes"]["Usage"]] += 1
    assert kinds == Counter(Prohibited=67)


@pytest.mark.parametrize("key", ["Groupings", "Views"])
def test_groupings_and_views_are_barred_from_mapping(key):
    """No grouping or view may be used to map a real vulnerability."""
    assert {e["Mapping_Notes"]["Usage"] for e in document()[key]} == {"Prohibited"}


def test_the_compound_weaknesses_use_their_natures():
    """A chain says where it starts and a composite what it requires, in CWE 5.0
    three chains and four composites."""
    found = Counter()
    for weakness in document()["Weaknesses"]:
        natures = {r["Nature"] for r in weakness.get("Related_Weaknesses", [])}
        if weakness["Structure"] == "Chain":
            assert "StartsWith" in natures, weakness["ID"]
        elif weakness["Structure"] == "Composite":
            assert "Requires" in natures, weakness["ID"]
        else:
            assert not natures & {"StartsWith", "Requires"}, weakness["ID"]
        found[weakness["Structure"]] += 1
    assert found == Counter(Simple=977, Composite=4, Chain=3)


def test_each_link_is_written_in_one_direction_only():
    """The list writes ChildOf and never ParentOf, CanPrecede and never CanFollow,
    and Requires and never RequiredBy, so a reader computes the inverse."""
    natures = Counter(
        link["Nature"]
        for weakness in document()["Weaknesses"]
        for link in weakness.get("Related_Weaknesses", [])
    )
    assert natures == Counter(
        ChildOf=1324,
        CanPrecede=148,
        PeerOf=103,
        CanAlsoBe=28,
        Requires=13,
        Overlaps=3,
        StartsWith=3,
    )


def test_a_symmetric_nature_is_not_written_both_ways():
    """The news article of 2026-10-28 calls PeerOf and Overlaps symmetric, but the
    list mostly writes one direction: 14 of 103 PeerOf links and no Overlaps link
    has its reverse."""
    for nature, total, reciprocal in (("PeerOf", 103, 14), ("Overlaps", 3, 0)):
        links = {
            (weakness["ID"], link["CWE_ID"], link["View_ID"])
            for weakness in document()["Weaknesses"]
            for link in weakness.get("Related_Weaknesses", [])
            if link["Nature"] == nature
        }
        assert len(links) == total
        assert sum((b, a, v) in links for a, b, v in links) == reciprocal


def test_only_weaknesses_and_groupings_are_members():
    """No view holds a view, in CWE 5.0."""
    weaknesses = {w["ID"] for w in document()["Weaknesses"]}
    groupings = {g["ID"] for g in document()["Groupings"]}
    kinds = Counter()
    for entry in _entries():
        holder = entry.get("Relationships") or entry.get("Members") or {}
        for member in holder.get("Has_Member", []):
            kinds["weakness" if member["CWE_ID"] in weaknesses else "other"] += 1
            kinds["grouping"] += member["CWE_ID"] in groupings
    assert kinds == Counter(weakness=4733, other=430, grouping=430)


def test_a_view_of_each_kind_holds_what_its_type_says():
    """An implicit view has a filter and no members. All but two of the rest name
    their members: CWE-630, an explicit slice, and CWE-631, a graph, have none, and
    both are deprecated."""
    kinds = Counter(
        (v["Type"], "Members" in v, "Filter" in v) for v in document()["Views"]
    )
    assert kinds == Counter(
        {
            ("Graph", True, False): 38,
            ("Implicit", False, True): 17,
            ("Explicit", True, False): 5,
            ("Explicit", False, False): 1,
            ("Graph", False, False): 1,
        }
    )


def test_name_or_class_gives_a_platform_with_one_exception():
    """The XSD leaves both optional, so the schema does too. In CWE 5.0 exactly one of
    the two holds on every platform but one Technology in CWE-1259, which gives both."""
    both, neither = [], []
    for weakness in document()["Weaknesses"]:
        platforms = weakness.get("Applicable_Platforms", {})
        for kind, items in platforms.items():
            for item in items:
                if "Name" in item and "Class" in item:
                    both.append((weakness["ID"], kind))
                elif "Name" not in item and "Class" not in item:
                    neither.append((weakness["ID"], kind))
    assert both == [("1259", "Technology")]
    assert not neither


def test_the_known_oddities_of_cwe_5_0():
    """One source has the bare number 1300 for an identifier, and one has the word
    Original for an address. A correction upstream fails this test on purpose."""
    sources = document()["External_References"]
    assert [
        s["Reference_ID"] for s in sources if not s["Reference_ID"].startswith("REF-")
    ] == ["1300"]
    assert [s["Reference_ID"] for s in sources if s.get("URL") == "Original"] == [
        "REF-1068"
    ]
    assert [
        s["Reference_ID"] for s in sources if "" in s.get("Author", [])
    ] == EMPTY_AUTHOR
    assert [
        weakness["ID"]
        for weakness in document()["Weaknesses"]
        for mode in weakness.get("Modes_Of_Introduction", [])
        if mode.get("Note") == ""
    ] == EMPTY_NOTE


def test_the_attack_pattern_links_are_the_ones_capec_names():
    """CWE 5.0 and CAPEC 3.9 each hold this link from their own side, and they agree."""
    pairs = ROOT / "tests" / "upstream" / "capec-3.9-weakness-pairs.txt"
    theirs = {
        tuple(line.split())
        for line in pairs.read_text().splitlines()
        if not line.startswith("#")
    }
    ours = {
        (weakness["ID"], link["CAPEC_ID"])
        for weakness in document()["Weaknesses"]
        for link in weakness.get("Related_Attack_Patterns", [])
    }
    assert len(ours) == 1212
    assert ours == theirs
