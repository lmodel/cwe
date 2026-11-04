"""Checks the copy of the upstream, and that the schema names the same edition.

upstream/ holds the CWE List and its XSD as MITRE publishes them. These tests hold
them to the git object hashes that scripts/check_upstream_release.py pins, and the
schema's headers to the edition that script watches. They run offline.
"""

import importlib.util
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "cwe" / "schema"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
MODULES = {
    path.stem: yaml.safe_load(path.read_text()) for path in SCHEMA_DIR.glob("*.yaml")
}
XS = "{http://www.w3.org/2001/XMLSchema}"
XSD_FILE = UPSTREAM / "cwe_schema_v8.0.xsd"


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PINS = _watch()


def test_upstream_holds_exactly_the_pinned_files():
    """Nothing is added to the copy, and nothing is missing from it."""
    held = {
        p.relative_to(UPSTREAM).as_posix() for p in UPSTREAM.rglob("*") if p.is_file()
    }
    assert held == set(PINS.PINNED_BLOBS)


@pytest.mark.parametrize("name", sorted(PINS.PINNED_BLOBS))
def test_each_copy_is_the_pinned_blob(name):
    """Each file is byte for byte what was read from MITRE's site."""
    assert PINS.blob((UPSTREAM / name).read_bytes()) == PINS.PINNED_BLOBS[name]


def test_the_xml_in_the_zip_is_the_pinned_one():
    attributes, data = PINS.read_catalogue((UPSTREAM / "cwec_v5.0.xml.zip").read_bytes())
    assert PINS.blob(data) == PINS.PINNED_XML_BLOB
    assert attributes["Version"] == PINS.PINNED_EDITION
    assert attributes["Date"] == PINS.PINNED_DATE


def test_every_module_names_the_pinned_edition():
    """Each module's version is the edition the watch pins, and each names the XSD."""
    for name, doc in MODULES.items():
        assert doc["version"] == PINS.PINNED_EDITION, name
        assert doc["source"] == PINS.PINNED_SOURCE, name
        assert doc["license"] == "Apache-2.0", name
        assert doc["annotations"]["xsd_version"] == PINS.PINNED_XSD_VERSION, name
        assert doc["annotations"]["xsd_date"] == PINS.PINNED_DATE, name
        assert doc["annotations"]["xsd_namespace"] == "http://cwe.mitre.org/cwe-8", name


def test_the_xsd_is_the_edition_the_pins_name():
    root = ET.parse(XSD_FILE).getroot()
    assert root.get("targetNamespace") == "http://cwe.mitre.org/cwe-8"
    assert root.get("version") == PINS.PINNED_XSD_VERSION
    info = root.find(f"{XS}annotation/{XS}appinfo")
    assert info.find("version").text == PINS.PINNED_XSD_VERSION
    assert info.find("date").text == "October 28, 2026"
    # The XSD asks that a copy keep this header.
    assert "this license header must be included" in info.find("terms_of_use").text


def test_notice_reproduces_the_designation_and_the_licence():
    """The Terms of Use ask each copy to reproduce them."""
    notice = " ".join((ROOT / "NOTICE").read_text().split())
    terms = " ".join((UPSTREAM / "TERMS.txt").read_text().split())
    assert "Copyright (c) 2006-2026, The MITRE Corporation." in notice
    assert "CWE is a trademark of The MITRE Corporation." in notice
    assert "endorsement" in notice
    grant = (
        "hereby grants you a non-exclusive, royalty-free license to use CWE for "
        "research, development, and commercial purposes. Any copy you make for such "
        "purposes is authorized on the condition that you reproduce"
    )
    assert grant in notice
    assert grant in terms


def _words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def _runs(words, size):
    return {tuple(words[i : i + size]) for i in range(len(words) - size + 1)}


def _texts(node):
    """Every description anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                yield value
            else:
                yield from _texts(value)
    elif isinstance(node, list):
        for item in node:
            yield from _texts(item)


# A run this long cannot arise by chance in a short hint, though a shorter one can,
# such as "of the weakness that the".
RUN = 6


def test_no_description_copies_the_upstreams_text():
    """A description here is this project's own: none shares a run of six words
    with the XSD's documentation."""
    upstream = set()
    for node in ET.parse(XSD_FILE).getroot().iter(XS + "documentation"):
        upstream |= _runs(_words("".join(node.itertext())), RUN)
    assert upstream
    for name, doc in MODULES.items():
        for text in _texts(doc):
            shared = _runs(_words(text), RUN) & upstream
            assert not shared, (name, text, sorted(shared)[:2])
