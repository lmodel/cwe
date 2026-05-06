#!/usr/bin/env python3
"""Post-process the gen-python output to fix issues that cannot be addressed
in the schema.

Fixes applied
-------------
1. Python reserved keyword ``class`` - see project.justfile fix-python-keywords.
   (That is done by sed; this script handles the remaining issues.)

2. _normalize_inlined_as_list for enum-keyed slots - linkml_runtime's
   _normalize_inlined_as_list cannot compare an enum instance against the raw
   YAML string used as the dict key.  Replace with a plain list comprehension
   that calls the range type constructor via **as_dict(v).
"""

from __future__ import annotations

import sys
from pathlib import Path


ENUM_KEYED_SLOTS: list[tuple[str, str, str]] = [
    # (slot_name, slot_type, key_name)
    # All keyed=False inlined-as-list slots: linkml_runtime's
    # _normalize_inlined_as_list has a bug where single-field dict entries
    # are passed as slot_type(dict) (positional) instead of slot_type(**dict).
    # Replace every such call with a safe list comprehension.
    ("notes", "Note", "type"),
    ("references", "CWEReference", "external_reference_id"),
    ("taxonomy_mappings", "TaxonomyMapping", "taxonomy_name"),
    ("related_weaknesses", "RelatedWeakness", "nature"),
    ("weakness_ordinalities", "WeaknessOrdinality", "ordinality"),
    ("alternate_terms", "AlternateTerm", "term"),
    ("modes_of_introduction", "ModeOfIntroduction", "phase"),
    ("common_consequences", "CommonConsequence", "scopes"),
    ("detection_methods", "DetectionMethod", "method"),
    ("potential_mitigations", "PotentialMitigation", "description"),
    ("demonstrative_examples", "DemonstrativeExample", "intro_text"),
    ("observed_examples", "ObservedExample", "reference"),
    ("audience", "Audience", "type"),
    ("members", "CatalogMember", "cwe_id"),
    ("languages", "LanguagePlatform", "prevalence"),
    ("operating_systems", "OSPlatform", "prevalence"),
    ("architectures", "ArchitecturePlatform", "prevalence"),
    ("technologies", "TechnologyPlatform", "prevalence"),
    ("example_codes", "ExampleCode", "nature"),
    ("suggestions", "MappingSuggestion", "cwe_id"),
    ("member_of", "CatalogMember", "cwe_id"),
    ("has_member", "CatalogMember", "cwe_id"),
    ("modifications", "Modification", "modification_date"),
    ("contributions", "Contribution", "contribution_date"),
    ("previous_entry_names", "PreviousEntryName", "name"),
]


def fix(path: Path) -> None:
    src = path.read_text()

    for slot_name, slot_type, key_name in ENUM_KEYED_SLOTS:
        # Match both keyed=True and keyed=False variants
        for keyed in ("True", "False"):
            old = (
                f'self._normalize_inlined_as_list(slot_name="{slot_name}", '
                f'slot_type={slot_type}, key_name="{key_name}", keyed={keyed})'
            )
            new = (
                f"if not isinstance(self.{slot_name}, list):\n"
                f"            self.{slot_name} = [self.{slot_name}] if self.{slot_name} is not None else []\n"
                f"        self.{slot_name} = [v if isinstance(v, {slot_type}) else {slot_type}(**as_dict(v)) for v in self.{slot_name}]"
            )
            count = src.count(old)
            if count:
                src = src.replace(old, new)
                print(f"Patched {count} occurrence(s) of '{slot_name}' (keyed={keyed})")

    path.write_text(src)


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src/cwe/datamodel/cwe.py")
    fix(target)
    print(f"Done: {target}")
