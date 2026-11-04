"""Walks the CWE XSD beside the schema, in both directions.

Starting at the root element, each XSD type is compared with the class whose
xsd_type annotation names it: the keys, which are required, which repeat and what
range each has. Every enumeration is compared with its enum. A key, class or value
the XSD does not declare fails, and so does anything the XSD declares that the
schema leaves out, except for the named exclusions below.
"""

from collections import defaultdict
from functools import cache
from pathlib import Path

import pytest
from linkml_runtime import SchemaView

from tests import conversion

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cwe" / "schema" / "cwe.yaml"

# The XSD's Categories element and CategoryType, which schema 8.0 keeps beside
# Groupings and GroupingType. CWE 5.0 holds no category, and the CWE Program's news
# article of 2026-10-28 says Grouping replaced Category.
EXCLUDED_KEYS = {("Weakness_Catalog", "Categories")}
EXCLUDED_SHAPES = {"CategoryType"}

# How an XSD simple type is written in the schema, where a class does not stand for
# it. An identifier the XSD types as an integer ranges over the class it names, or
# stays a digit string.
SIMPLE_RANGES = {
    "xs:string": {"string", "cwe_reference_id"},
    "xs:integer": {"cwe_entry_id", "cwe_capec_id"},
    "xs:date": {"date"},
    "xs:anyURI": {"uri"},
    "xs:gYear": {"cwe_publication_year"},
    "xs:gMonth": {"cwe_publication_month"},
    "xs:gDay": {"cwe_publication_day"},
    "StructuredTextType": {"cwe_structured_text"},
}
# The identifier classes a reference may range over, by the key that names them.
REFERENCE_RANGES = {
    "CWE_ID": {"CweWeakness", "CweEntry"},
    "Chain_ID": {"CweWeakness"},
    "View_ID": {"CweView"},
    "External_Reference_ID": {"CweExternalReference"},
}


@cache
def view():
    return SchemaView(str(SCHEMA))


@cache
def slots_of(class_name):
    return {s.name: s for s in view().class_induced_slots(class_name)}


@cache
def class_by_xsd():
    """Each class, by the XSD type or types its annotation names."""
    found = {}
    for name, cls in view().all_classes().items():
        annotation = cls.annotations.get("xsd_type")
        assert annotation, f"{name} names no XSD type"
        for token in annotation.value.split():
            if not cls.abstract:
                assert token not in found, token
                found[token] = name
    return found


@cache
def enum_by_xsd():
    found = {}
    for name, enum in view().all_enums().items():
        annotation = enum.annotations.get("xsd_type")
        assert annotation, f"{name} names no XSD type"
        assert annotation.value not in found, annotation.value
        found[annotation.value] = name
    return found


def _check_range(where, xsd_type, slot):
    """That a slot's range renders an XSD type."""
    data = conversion.xsd()
    if xsd_type in data.enumerations:
        assert slot.range == enum_by_xsd()[xsd_type], where
    elif xsd_type in data.unions:
        members = {enum_by_xsd()[m] for m in data.unions[xsd_type]}
        assert {e.range for e in slot.any_of} == members, where
    elif xsd_type in data.shapes and not _is_plain_text(xsd_type):
        assert slot.range == class_by_xsd()[xsd_type], where
    elif slot.name in REFERENCE_RANGES:
        assert slot.range in REFERENCE_RANGES[slot.name], where
    else:
        assert slot.range in SIMPLE_RANGES[xsd_type], (where, slot.range)


def _is_plain_text(xsd_type):
    shape = conversion.xsd().shapes.get(xsd_type)
    return bool(shape and shape.structured and not shape.attributes)


@cache
def walk():
    """Each pair of an XSD type and a class that the walk from the root reaches,
    with a list of what disagrees."""
    data = conversion.xsd()
    seen, wrong = {}, []

    def check(shape, class_name):
        if shape.name in seen:
            return
        seen[shape.name] = class_name
        expected = {}
        for attribute in shape.attributes.values():
            expected[attribute.name] = (attribute.type, attribute.required, False)
        for child in shape.children.values():
            if (shape.name, child.name) in EXCLUDED_KEYS:
                continue
            if child.name in shape.ordered_choice:
                continue
            inner = data.shapes.get(child.type)
            if inner is not None and inner.wrapped:
                expected[child.name] = (inner.wrapped.type, child.required, True)
            else:
                expected[child.name] = (child.type, child.required, child.repeated)
        if shape.text or (shape.structured and shape.attributes):
            text_type = shape.text or "StructuredTextType"
            expected["Value"] = (text_type, None, False)
        slots = slots_of(class_name)
        if shape.ordered_choice:
            expected["Entries"] = (None, False, True)
            entry = slots_of("CweExampleEntry")
            if set(entry) != set(shape.ordered_choice):
                wrong.append((shape.name, sorted(entry), shape.ordered_choice))
            for name in shape.ordered_choice:
                child = shape.children[name]
                _check_range(f"{shape.name}/{name}", child.type, entry[name])
                if not _is_plain_text(child.type):
                    check(data.shapes[child.type], entry[name].range)
        if expected.keys() != slots.keys():
            wrong.append((shape.name, sorted(expected.keys() ^ slots.keys())))
        for key in expected.keys() & slots.keys():
            xsd_type, required, repeated = expected[key]
            slot = slots[key]
            where = f"{shape.name}/{key}"
            if bool(slot.multivalued) != repeated:
                wrong.append((where, "multivalued", slot.multivalued, repeated))
            if required is not None and not slot.identifier:
                if bool(slot.required) != required:
                    wrong.append((where, "required", slot.required, required))
            if xsd_type is None:
                continue
            try:
                _check_range(where, xsd_type, slot)
            except AssertionError as err:
                wrong.append((where, "range", xsd_type, slot.range, str(err)))
            inner = data.shapes.get(xsd_type)
            if inner is not None and not _is_plain_text(xsd_type):
                check(inner, slot.range)

    check(data.shapes["Weakness_Catalog"], "CweWeaknessCatalog")
    return seen, wrong


def test_the_schema_and_the_xsd_agree():
    """Keys, required, repeating and ranges, for every type the walk reaches."""
    _, wrong = walk()
    assert not wrong, wrong


def test_every_type_is_reached_but_the_named_exclusions():
    """Every XSD type with keys is a class, or is a wrapper the JSON form drops, or
    is plain text, or is one of the exclusions."""
    data = conversion.xsd()
    seen, _ = walk()
    left = {
        name
        for name, shape in data.shapes.items()
        if name not in seen and not shape.wrapped and not _is_plain_text(name)
    }
    assert left == EXCLUDED_SHAPES


def test_every_class_is_reached():
    """Every class renders a type the walk reached, or is one of the two the JSON
    form adds: the abstract base and the entry of a repeating choice."""
    seen, _ = walk()
    reached = set(seen.values())
    assert set(view().all_classes()) - reached == {"CweEntry", "CweExampleEntry"}


def test_the_base_class_holds_what_all_three_entries_share():
    """Each key on CweEntry is declared by all three XSD types it names, and every
    key all three share is on it."""
    data = conversion.xsd()
    shapes = [data.shapes[n] for n in ("WeaknessType", "GroupingType", "ViewType")]
    keys = [set(s.children) | set(s.attributes) for s in shapes]
    shared = set.intersection(*keys)
    assert shared == set(slots_of("CweEntry"))


@cache
def enums_by_type():
    found = defaultdict(list)
    for name, enum in view().all_enums().items():
        found[enum.annotations["xsd_type"].value].append(name)
    return found


def test_every_xsd_enumeration_is_an_enum():
    """Both ways: each enumeration has its enum, and each enum its enumeration."""
    assert set(conversion.xsd().enumerations) == set(enums_by_type())


@pytest.mark.parametrize("xsd_type", sorted(conversion.xsd().enumerations))
def test_each_enum_lists_the_xsds_values(xsd_type):
    """The same values in the same order, spelled as the XSD spells them."""
    enum = view().get_enum(enum_by_xsd()[xsd_type])
    assert list(enum.permissible_values) == conversion.xsd().enumerations[xsd_type]


def test_the_custom_phase_rules_list_the_two_enums():
    """The rules repeat the two lists, since JSON Schema's generator drops a range
    in a rule's condition, so they are held equal here."""
    rules = view().get_class("CweCustomPhase").rules
    by_domain = {
        rule.preconditions.slot_conditions[
            "Domain"
        ].equals_string: rule.postconditions.slot_conditions["Value"].equals_string_in
        for rule in rules
    }
    assert by_domain["AI"] == list(view().get_enum("CweAiPhase").permissible_values)
    assert by_domain["Hardware"] == list(
        view().get_enum("CweHardwarePhase").permissible_values
    )
