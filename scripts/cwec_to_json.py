#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Turn the CWE List's XML into the JSON shape the LinkML schema describes.

MITRE publishes the CWE List as one XML file under an XML Schema (XSD), and LinkML
validates JSON and YAML. This script is the one fixed step between them. It keeps
every element and attribute name as a key and every value as its text, and it reads
which elements repeat from the XSD. The rules are:

- The root element's attributes become keys of the top object.
- An attribute becomes a key of the same name.
- A wrapper, an element whose only content is one repeating child, becomes a list
  under the wrapper's own name, so ``Related_Weaknesses`` holds a list and
  ``Related_Weakness`` is not a key.
- Any other element with child elements becomes an object, and a child that may
  repeat is always a list, so ``Applicable_Platforms`` holds ``Language``,
  ``Technology`` and the others as lists.
- An element with text and attributes becomes an object with its text under
  ``Value``, the word the CWE REST API uses for ``Custom_Phase`` and ``Dimension``.
- Text that may hold XHTML (``StructuredTextType``) becomes a string holding the
  XHTML fragment, without the namespace prefix and with the outer whitespace gone.
  Text in such a fragment stays escaped, so the string is always well formed.
- The repeating choice in a ``Demonstrative_Example`` becomes ``Entries``, a list of
  objects with exactly one of ``Body_Text`` and ``Example_Code``, since a list per
  key would lose the order that the prose and the code rely on. ``Entries`` is the
  REST API's name for it and the one key the XSD does not give. The XSD's other
  repeating choices, of ``Phase`` and ``Custom_Phase``, stay a list per key, because
  the order between the two kinds means nothing.
- Every value stays a string, as the XML has it, the identifiers among them.

An element or attribute the XSD does not declare stops the conversion, so a catalogue
that leaves its schema is noticed. CWE 5.0 validates against XSD 8.0 with no departure.
Usage::

    uv run scripts/cwec_to_json.py upstream/cwec_v5.0.xml.zip -o tmp/cwec_v5.0.json

The input is the XML file or the ZIP MITRE publishes it in. Without ``-o`` the JSON
goes to standard output. The script reads only the two files it is given.
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_XSD = ROOT / "upstream" / "cwe_schema_v8.0.xsd"
ROOT_ELEMENT = "Weakness_Catalog"

XS = "{http://www.w3.org/2001/XMLSchema}"
XHTML = "{http://www.w3.org/1999/xhtml}"
# XHTML's own namespace is the mark of structured text, and the XML Schema instance
# attribute on the root names where the XSD lives, so neither becomes a key.
XSI = "{http://www.w3.org/2001/XMLSchema-instance}"

# The most XML the script will take out of a ZIP. CWE 5.0's is about 19 MB.
MAX_XML_BYTES = 200_000_000

# The key the REST API gives text beside attributes, and the key it gives the
# ordered mix of prose and code. Neither is in the XSD.
VALUE_KEY = "Value"
ENTRIES_KEY = "Entries"

# The one type whose repeating choice keeps its order in ENTRIES_KEY.
ORDERED_CHOICE = "DemonstrativeExamplesType/Demonstrative_Example"


@dataclass(frozen=True)
class Child:
    """One child element an XSD type declares."""

    name: str
    type: str
    required: bool
    repeated: bool


@dataclass(frozen=True)
class Attribute:
    """One attribute an XSD type declares."""

    name: str
    type: str
    required: bool


@dataclass
class Shape:
    """What an XSD complex type lets an element hold."""

    name: str
    children: dict[str, Child] = field(default_factory=dict)
    attributes: dict[str, Attribute] = field(default_factory=dict)
    # The type of the element's own text, when it has any.
    text: str | None = None
    # Set on a type that allows XHTML among its text.
    structured: bool = False
    # The children whose relative order the JSON keeps, in the XSD's order.
    ordered_choice: tuple[str, ...] = ()

    @property
    def wrapped(self) -> Child | None:
        """The repeating child, when this type is a wrapper and nothing else."""
        if len(self.children) != 1 or self.attributes or self.text or self.structured:
            return None
        child = next(iter(self.children.values()))
        return child if child.repeated else None


@dataclass
class Xsd:
    """The named and anonymous types of one XSD, by a name of their path."""

    shapes: dict[str, Shape] = field(default_factory=dict)
    enumerations: dict[str, list[str]] = field(default_factory=dict)
    unions: dict[str, list[str]] = field(default_factory=dict)
    restrictions: dict[str, str] = field(default_factory=dict)


def _local(name: str | None) -> str:
    """A type's name without its namespace prefix; XML Schema's own keep theirs."""
    if not name:
        return ""
    prefix, sep, rest = name.partition(":")
    return name if prefix == "xs" or not sep else rest


def _occurs(element: ET.Element, attribute: str) -> int | None:
    value = element.get(attribute, "1")
    return None if value == "unbounded" else int(value)


def _read_simple(node: ET.Element, name: str, xsd: Xsd) -> None:
    restriction = node.find(XS + "restriction")
    union = node.find(XS + "union")
    if restriction is not None:
        values = [e.get("value") for e in restriction.findall(XS + "enumeration")]
        if values:
            xsd.enumerations[name] = values
        else:
            xsd.restrictions[name] = _local(restriction.get("base"))
    elif union is not None:
        xsd.unions[name] = [_local(t) for t in union.get("memberTypes").split()]


def _add_attribute(node: ET.Element, shape: Shape, xsd: Xsd) -> None:
    name = node.get("name")
    type_name = _local(node.get("type"))
    inline = node.find(XS + "simpleType")
    if inline is not None:
        type_name = f"{shape.name}/@{name}"
        _read_simple(inline, type_name, xsd)
    shape.attributes[name] = Attribute(
        name, type_name, node.get("use", "optional") == "required"
    )


def _add_element(
    node: ET.Element, shape: Shape, xsd: Xsd, optional: bool, repeats: bool
) -> None:
    name = node.get("name")
    path = f"{shape.name}/{name}"
    type_name = _local(node.get("type"))
    inline_complex = node.find(XS + "complexType")
    inline_simple = node.find(XS + "simpleType")
    if inline_complex is not None:
        type_name = path
        _read_complex(inline_complex, path, xsd)
    elif inline_simple is not None:
        type_name = path
        _read_simple(inline_simple, path, xsd)
    low, high = _occurs(node, "minOccurs"), _occurs(node, "maxOccurs")
    repeated = repeats or high is None or high > 1
    required = low >= 1 and not optional
    known = shape.children.get(name)
    if known:
        # A name in two branches of a choice is required only where both say so,
        # and repeats where either does.
        repeated = repeated or known.repeated
        required = required and known.required
    shape.children[name] = Child(name, type_name, required, repeated)


def _read_particle(
    node: ET.Element, shape: Shape, xsd: Xsd, optional: bool, repeats: bool = False
) -> None:
    """Add the elements under a sequence or a choice to a shape."""
    for item in node:
        if item.tag == XS + "element":
            _add_element(item, shape, xsd, optional, repeats)
        elif item.tag == XS + "sequence":
            _read_particle(
                item, shape, xsd, optional or item.get("minOccurs") == "0", repeats
            )
        elif item.tag == XS + "choice":
            high = _occurs(item, "maxOccurs")
            many = repeats or high is None or high > 1
            _read_particle(item, shape, xsd, True, many)
            if many and shape.name == ORDERED_CHOICE:
                shape.ordered_choice = tuple(
                    e.get("name") for e in item.findall(XS + "element")
                )
        elif item.tag == XS + "any":
            shape.structured = True


def _read_complex(node: ET.Element, name: str, xsd: Xsd) -> None:
    shape = Shape(name)
    xsd.shapes[name] = shape
    for item in node:
        if item.tag in (XS + "sequence", XS + "choice"):
            wrapper = ET.Element(XS + "sequence")
            wrapper.append(item)
            _read_particle(wrapper, shape, xsd, False)
        elif item.tag == XS + "attribute":
            _add_attribute(item, shape, xsd)
        elif item.tag in (XS + "simpleContent", XS + "complexContent"):
            extension = item.find(XS + "extension")
            shape.text = _local(extension.get("base"))
            for attribute in extension.findall(XS + "attribute"):
                _add_attribute(attribute, shape, xsd)


def read_xsd(path: Path = DEFAULT_XSD) -> Xsd:
    """Read an XSD's types, naming an anonymous type by its path from a named one."""
    xsd = Xsd()
    root = ET.parse(path).getroot()
    for node in root:
        name = node.get("name")
        if node.tag == XS + "complexType":
            _read_complex(node, name, xsd)
        elif node.tag == XS + "simpleType":
            _read_simple(node, name, xsd)
        elif node.tag == XS + "element":
            _read_complex(node.find(XS + "complexType"), name, xsd)
    return xsd


def _local_tag(element: ET.Element) -> str:
    return element.tag.rpartition("}")[2]


def _fragment(element: ET.Element) -> str:
    """The inside of an element as an XHTML fragment with no namespace prefix."""
    parts = [escape(element.text or "")]
    for child in element:
        name = _local_tag(child)
        attributes = "".join(
            f" {key.rpartition('}')[2]}={quoteattr(value)}"
            for key, value in child.attrib.items()
        )
        inside = _fragment(child)
        if inside:
            parts.append(f"<{name}{attributes}>{inside}</{name}>")
        else:
            parts.append(f"<{name}{attributes}/>")
        parts.append(escape(child.tail or ""))
    return "".join(parts)


def _is_structured(type_name: str, xsd: Xsd) -> bool:
    shape = xsd.shapes.get(type_name)
    return bool(shape and shape.structured)


def _value(element: ET.Element, type_name: str, xsd: Xsd):
    """The JSON form of one element of a known type."""
    shape = xsd.shapes.get(type_name)
    if shape is None:
        return (element.text or "").strip()
    if shape.structured and not shape.attributes:
        return _fragment(element).strip()
    if shape.wrapped:
        inner = shape.wrapped
        return [_value(item, inner.type, xsd) for item in element]
    return _object(element, shape, xsd)


def _text_of(element: ET.Element, shape: Shape, xsd: Xsd) -> str | None:
    """The text of an element that holds text beside attributes, if it does."""
    if shape.structured or _is_structured(shape.text or "", xsd):
        return _fragment(element).strip()
    if shape.text:
        return (element.text or "").strip()
    return None


def _object(element: ET.Element, shape: Shape, xsd: Xsd) -> dict:
    """The JSON object of an element that is neither a wrapper nor plain text."""
    found: dict = {}
    for key, value in element.attrib.items():
        if key.startswith(XSI):
            continue
        if key not in shape.attributes:
            raise ValueError(f"{shape.name} declares no attribute {key}")
        found[key] = value
    text = _text_of(element, shape, xsd)
    if text is not None:
        found[VALUE_KEY] = text
        return found
    for child in element:
        name = _local_tag(child)
        declared = shape.children.get(name)
        if declared is None:
            raise ValueError(f"{shape.name} declares no element {name}")
        if name in shape.ordered_choice:
            entry = {name: _value(child, declared.type, xsd)}
            found.setdefault(ENTRIES_KEY, []).append(entry)
        elif declared.repeated:
            found.setdefault(name, []).append(_value(child, declared.type, xsd))
        else:
            found[name] = _value(child, declared.type, xsd)
    return found


def convert(root: ET.Element, xsd: Xsd) -> dict:
    """The JSON object of a parsed catalogue."""
    return _object(root, xsd.shapes[ROOT_ELEMENT], xsd)


def read_xml(path: Path) -> ET.Element:
    """Parse the catalogue from its XML file or the ZIP MITRE publishes it in."""
    if path.suffix != ".zip":
        return ET.parse(path).getroot()
    with zipfile.ZipFile(path) as archive:
        members = [i for i in archive.infolist() if i.filename.endswith(".xml")]
        if len(members) != 1:
            raise ValueError(f"{path} holds {len(members)} XML files, not one")
        if members[0].file_size > MAX_XML_BYTES:
            raise ValueError(f"{members[0].filename} is larger than the script reads")
        with archive.open(members[0]) as handle:
            return ET.parse(handle).getroot()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("catalogue", type=Path, help="the XML file, or its ZIP")
    parser.add_argument("--xsd", type=Path, default=DEFAULT_XSD, help="the XSD")
    parser.add_argument("-o", "--output", type=Path, help="where to write the JSON")
    args = parser.parse_args(argv)
    document = convert(read_xml(args.catalogue), read_xsd(args.xsd))
    text = json.dumps(document, ensure_ascii=False, indent=1) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
