"""The catalogue as the schema describes it, for the tests that read it.

scripts/cwec_to_json.py is not a package, so it is loaded by its path. The whole
catalogue takes about a second to convert, so each test module shares one copy and
must not change it.
"""

import importlib.util
import sys
from functools import cache
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "cwec_to_json.py"
XSD_FILE = ROOT / "upstream" / "cwe_schema_v8.0.xsd"
CATALOGUE_FILE = ROOT / "upstream" / "cwec_v5.0.xml.zip"


def _load():
    spec = importlib.util.spec_from_file_location("cwec_to_json", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    # The dataclasses in the script read their module from this table.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONVERTER = _load()


@cache
def xsd():
    """The XSD's types, read once."""
    return CONVERTER.read_xsd(XSD_FILE)


@cache
def xml_root():
    """The catalogue's parsed XML, read once."""
    return CONVERTER.read_xml(CATALOGUE_FILE)


@cache
def catalogue():
    """The whole catalogue in the JSON form, converted once."""
    return CONVERTER.convert(xml_root(), xsd())
