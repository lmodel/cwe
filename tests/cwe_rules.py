"""The rules on a whole catalogue that JSON Schema cannot state.

JSON Schema sees one value at a time, so it cannot tell whether an identifier names
an entry that exists, or of the right kind, or whether two entries share a number.
The XSD states the uniqueness in its xs:unique constraints and says what each
reference points at in its documentation. tests/test_catalogue.py runs these rules
over CWE 5.0, and tests/test_data.py holds them to the counter-examples under
tests/data/problem/invalid/.

A consumer that wants the upstream's whole rule set runs ``rule_errors`` beside the
JSON Schema. Each error is a JSON pointer and a sentence.
"""

from __future__ import annotations

ENTRY_LISTS = ("Weaknesses", "Groupings", "Views")


def _entries(document):
    for key in ENTRY_LISTS:
        for index, entry in enumerate(document.get(key) or []):
            yield f"/{key}/{index}", key, entry


def _unique_ids(document):
    seen = set()
    for place, _, entry in _entries(document):
        if entry["ID"] in seen:
            yield f"{place}/ID", f"another entry already has the ID {entry['ID']}"
        seen.add(entry["ID"])
    seen = set()
    for index, source in enumerate(document.get("External_References") or []):
        if source["Reference_ID"] in seen:
            yield (
                f"/External_References/{index}/Reference_ID",
                f"another source already has the ID {source['Reference_ID']}",
            )
        seen.add(source["Reference_ID"])


def _related_weaknesses(place, entry, weaknesses, views):
    primary = set()
    for index, link in enumerate(entry.get("Related_Weaknesses") or []):
        here = f"{place}/Related_Weaknesses/{index}"
        if link["CWE_ID"] not in weaknesses:
            yield f"{here}/CWE_ID", f"no weakness has the ID {link['CWE_ID']}"
        if link["View_ID"] not in views:
            yield f"{here}/View_ID", f"no view has the ID {link['View_ID']}"
        chain = link.get("Chain_ID")
        if chain is not None and chain not in weaknesses:
            yield f"{here}/Chain_ID", f"no weakness has the ID {chain}"
        if link.get("Ordinal") == "Primary":
            key = (link["Nature"], link["View_ID"])
            if key in primary:
                yield (
                    f"{here}/Ordinal",
                    f"this weakness already has a primary {key[0]} link in view {key[1]}",
                )
            primary.add(key)


def _members(place, relationships, all_ids, views):
    for kind in ("Member_Of", "Has_Member"):
        for index, member in enumerate(relationships.get(kind) or []):
            here = f"{place}/{kind}/{index}"
            if member["CWE_ID"] not in all_ids:
                yield f"{here}/CWE_ID", f"no entry has the ID {member['CWE_ID']}"
            if member["View_ID"] not in views:
                yield f"{here}/View_ID", f"no view has the ID {member['View_ID']}"


def rule_errors(document):
    """Each place a catalogue breaks a rule the JSON Schema cannot state."""
    weaknesses = {e["ID"] for e in document.get("Weaknesses") or []}
    groupings = {e["ID"] for e in document.get("Groupings") or []}
    views = {e["ID"] for e in document.get("Views") or []}
    all_ids = weaknesses | groupings | views
    sources = {s["Reference_ID"] for s in document.get("External_References") or []}
    found = list(_unique_ids(document))
    for place, key, entry in _entries(document):
        found += _related_weaknesses(place, entry, weaknesses, views)
        for field in ("Relationships", "Members"):
            if entry.get(field):
                found += _members(f"{place}/{field}", entry[field], all_ids, views)
        suggestions = (entry.get("Mapping_Notes") or {}).get("Suggestions") or []
        for index, suggestion in enumerate(suggestions):
            if suggestion["CWE_ID"] not in weaknesses:
                found.append(
                    (
                        f"{place}/Mapping_Notes/Suggestions/{index}/CWE_ID",
                        f"no weakness has the ID {suggestion['CWE_ID']}",
                    )
                )
        for index, reference in enumerate(entry.get("References") or []):
            if reference["External_Reference_ID"] not in sources:
                found.append(
                    (
                        f"{place}/References/{index}/External_Reference_ID",
                        f"no source has the ID {reference['External_Reference_ID']}",
                    )
                )
    return found
