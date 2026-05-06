"""Tests for CWE CSV files in tests/data/cwe/.

699.csv  - Software Development view
1000.csv - Research Concepts view
1194.csv - Hardware Design view
"""
import csv
import pytest
from pathlib import Path

VIEWS_DIR = Path(__file__).parent / "data" / "cwe"

VIEW_FILES = {
    699:  VIEWS_DIR / "699.csv",
    1000: VIEWS_DIR / "1000.csv",
    1194: VIEWS_DIR / "1194.csv",
}

EXPECTED_HEADERS = [
    "CWE-ID",
    "Name",
    "Weakness Abstraction",
    "Status",
    "Description",
    "Extended Description",
    "Related Weaknesses",
    "Weakness Ordinalities",
    "Applicable Platforms",
    "Background Details",
    "Alternate Terms",
    "Modes Of Introduction",
    "Exploitation Factors",
    "Likelihood of Exploit",
    "Common Consequences",
    "Detection Methods",
    "Potential Mitigations",
    "Observed Examples",
    "Functional Areas",
    "Affected Resources",
    "Taxonomy Mappings",
    "Related Attack Patterns",
    "Notes",
]

VALID_ABSTRACTIONS = {"Pillar", "Class", "Base", "Variant", "Compound"}
VALID_STATUSES = {"Stable", "Draft", "Incomplete", "Deprecated", "Obsolete"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_rows(view_id: int) -> list[dict]:
    path = VIEW_FILES[view_id]
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------------------
# Existence
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("view_id,path", list(VIEW_FILES.items()))
def test_file_exists(view_id, path):
    """Each vendor CSV file must be present on disk."""
    assert path.is_file(), f"Missing vendor CSV for view {view_id}: {path}"


# ---------------------------------------------------------------------------
# Structure - shared across all three files
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_headers_match_expected(view_id):
    """CSV headers must exactly match the canonical CWE export format."""
    with VIEW_FILES[view_id].open(newline="", encoding="utf-8") as fh:
        headers = next(csv.reader(fh))
    assert headers == EXPECTED_HEADERS, (
        f"View {view_id}: unexpected CSV headers.\n"
        f"  Expected: {EXPECTED_HEADERS}\n"
        f"  Got:      {headers}"
    )


@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_cwe_ids_are_positive_integers(view_id):
    """Every CWE-ID cell must be parseable as a positive integer."""
    for row in _load_rows(view_id):
        raw = row["CWE-ID"]
        assert raw.isdigit(), f"View {view_id}: non-numeric CWE-ID '{raw}'"
        assert int(raw) > 0, f"View {view_id}: non-positive CWE-ID {raw}"


@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_no_duplicate_cwe_ids(view_id):
    """Each CWE-ID must appear at most once within a view CSV."""
    ids = [row["CWE-ID"] for row in _load_rows(view_id)]
    duplicates = {i for i in ids if ids.count(i) > 1}
    assert not duplicates, f"View {view_id}: duplicate CWE-IDs found: {duplicates}"


@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_abstraction_values_are_valid(view_id):
    """Weakness Abstraction column must only contain recognised CWE terms."""
    found = {row["Weakness Abstraction"] for row in _load_rows(view_id)}
    invalid = found - VALID_ABSTRACTIONS
    assert not invalid, (
        f"View {view_id}: unknown Weakness Abstraction values: {invalid}"
    )


@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_status_values_are_valid(view_id):
    """Status column must only contain recognised CWE lifecycle terms."""
    found = {row["Status"] for row in _load_rows(view_id)}
    invalid = found - VALID_STATUSES
    assert not invalid, f"View {view_id}: unknown Status values: {invalid}"


@pytest.mark.parametrize("view_id", list(VIEW_FILES))
def test_name_and_description_non_empty(view_id):
    """Every row must have a non-blank Name and Description."""
    for row in _load_rows(view_id):
        cid = row["CWE-ID"]
        assert row["Name"].strip(), f"View {view_id}, CWE-{cid}: empty Name"
        assert row["Description"].strip(), f"View {view_id}, CWE-{cid}: empty Description"


@pytest.mark.parametrize("view_id,expected_min", [
    (699, 300),
    (1000, 800),
    (1194, 80),
])
def test_row_count_above_minimum(view_id, expected_min):
    """Each file should contain at least the historically observed minimum."""
    rows = _load_rows(view_id)
    assert len(rows) >= expected_min, (
        f"View {view_id}: expected >= {expected_min} rows, got {len(rows)}"
    )


# ---------------------------------------------------------------------------
# View 699 - Software Development
# ---------------------------------------------------------------------------

class TestSoftwareDevelopmentView699:
    """Spot-checks for the Software Development view (699)."""

    def test_contains_sql_injection(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(699)}
        assert 89 in ids, "View 699 must include CWE-89 (SQL Injection)"

    def test_contains_xss(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(699)}
        assert 79 in ids, "View 699 must include CWE-79 (XSS)"

    def test_contains_os_command_injection(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(699)}
        assert 78 in ids, "View 699 must include CWE-78 (OS Command Injection)"

    def test_contains_path_traversal(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(699)}
        assert 22 in ids, "View 699 must include CWE-22 (Path Traversal)"

    def test_no_hardware_jtag_entries(self):
        """JTAG debug interface weakness is hardware-specific and must not appear."""
        ids = {int(r["CWE-ID"]) for r in _load_rows(699)}
        assert 1191 not in ids, (
            "View 699 should not include CWE-1191 (On-Chip Debug Interface)"
        )

    def test_abstractions_exclude_pillar_and_compound(self):
        """Software Development view uses Base/Class/Variant only."""
        found = {r["Weakness Abstraction"] for r in _load_rows(699)}
        assert "Pillar" not in found, "View 699 should not contain Pillar abstractions"
        assert "Compound" not in found, "View 699 should not contain Compound abstractions"


# ---------------------------------------------------------------------------
# View 1000 - Research Concepts
# ---------------------------------------------------------------------------

class TestResearchConceptsView1000:
    """Spot-checks for the Research Concepts view (1000)."""

    def test_contains_improper_input_validation(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1000)}
        assert 20 in ids, "View 1000 must include CWE-20 (Improper Input Validation)"

    def test_contains_classic_buffer_overflow(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1000)}
        assert 120 in ids, "View 1000 must include CWE-120 (Classic Buffer Overflow)"

    def test_contains_path_traversal(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1000)}
        assert 22 in ids, "View 1000 must include CWE-22 (Path Traversal)"

    def test_contains_pillar_abstractions(self):
        """Research Concepts is the comprehensive tree and must include Pillar entries."""
        found = {r["Weakness Abstraction"] for r in _load_rows(1000)}
        assert "Pillar" in found, "View 1000 should include at least one Pillar abstraction"

    def test_contains_compound_abstractions(self):
        found = {r["Weakness Abstraction"] for r in _load_rows(1000)}
        assert "Compound" in found, "View 1000 should include at least one Compound abstraction"

    def test_is_larger_than_specialised_views(self):
        """Research Concepts covers more entries than either specialised view."""
        n_1000 = len(_load_rows(1000))
        assert n_1000 > len(_load_rows(699)), "View 1000 should have more rows than view 699"
        assert n_1000 > len(_load_rows(1194)), "View 1000 should have more rows than view 1194"


# ---------------------------------------------------------------------------
# View 1194 - Hardware Design
# ---------------------------------------------------------------------------

class TestHardwareDesignView1194:
    """Spot-checks for the Hardware Design view (1194)."""

    def test_contains_jtag_debug_interface(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1194)}
        assert 1191 in ids, "View 1194 must include CWE-1191 (On-Chip Debug Interface)"

    def test_contains_cleartext_transmission(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1194)}
        assert 319 in ids, "View 1194 must include CWE-319 (Cleartext Transmission)"

    def test_contains_insufficient_access_control_granularity(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1194)}
        assert 1220 in ids, (
            "View 1194 must include CWE-1220 (Insufficient Granularity of Access Control)"
        )

    def test_contains_dma_enabled_too_early(self):
        ids = {int(r["CWE-ID"]) for r in _load_rows(1194)}
        assert 1190 in ids, "View 1194 must include CWE-1190 (DMA Device Enabled Too Early)"

    def test_no_j2ee_misconfiguration(self):
        """J2EE misconfigurations are Java/software-specific and must not appear."""
        ids = {int(r["CWE-ID"]) for r in _load_rows(1194)}
        assert 5 not in ids, (
            "View 1194 should not include CWE-5 (J2EE Misconfiguration)"
        )

    def test_abstractions_exclude_pillar_and_compound(self):
        """Hardware Design view uses Base/Class/Variant only."""
        found = {r["Weakness Abstraction"] for r in _load_rows(1194)}
        assert "Pillar" not in found, "View 1194 should not contain Pillar abstractions"
        assert "Compound" not in found, "View 1194 should not contain Compound abstractions"
