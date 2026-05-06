#!/usr/bin/env python3
"""Derive a small, schema-compliant WeaknessCatalog YAML from the CWE XML catalog.

Usage:
    python tests/data/cwe/derive_test_data.py [XML_INPUT] [YAML_OUTPUT]

Defaults:
    XML_INPUT  = tests/data/cwe/cwec_v4.19.1.xml
    YAML_OUTPUT = tests/data/valid/WeaknessCatalog-001.yaml

The script extracts the first N_WEAKNESSES weaknesses, the first N_CATEGORIES
categories, the first N_VIEWS views, and all ExternalReferences that are
referenced by those entries.  All XML enum values are mapped to the
UPPER_SNAKE_CASE permissible-value keys used in the LinkML schema.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import yaml

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

NS = "http://cwe.mitre.org/cwe-7"
XHTML_NS = "http://www.w3.org/1999/xhtml"

# ---------------------------------------------------------------------------
# Enum value maps  (XML value -> schema UPPER_SNAKE_CASE key)
# ---------------------------------------------------------------------------

ABSTRACTION_MAP = {
    "Pillar": "PILLAR", "Class": "CLASS", "Base": "BASE",
    "Variant": "VARIANT", "Compound": "COMPOUND",
}
STRUCTURE_MAP = {"Chain": "CHAIN", "Composite": "COMPOSITE", "Simple": "SIMPLE"}
STATUS_MAP = {
    "Deprecated": "DEPRECATED", "Draft": "DRAFT", "Incomplete": "INCOMPLETE",
    "Obsolete": "OBSOLETE", "Stable": "STABLE", "Usable": "USABLE",
}
LIKELIHOOD_MAP = {"High": "HIGH", "Medium": "MEDIUM", "Low": "LOW", "Unknown": "UNKNOWN"}
ORDINAL_MAP = {"Primary": "PRIMARY"}
ORDINALITY_MAP = {"Indirect": "INDIRECT", "Primary": "PRIMARY", "Resultant": "RESULTANT"}
NATURE_MAP = {
    "ChildOf": "CHILD_OF", "ParentOf": "PARENT_OF", "StartsWith": "STARTS_WITH",
    "CanFollow": "CAN_FOLLOW", "CanPrecede": "CAN_PRECEDE", "RequiredBy": "REQUIRED_BY",
    "Requires": "REQUIRES", "CanAlsoBe": "CAN_ALSO_BE", "PeerOf": "PEER_OF",
}
PREVALENCE_MAP = {
    "Often": "OFTEN", "Sometimes": "SOMETIMES", "Rarely": "RARELY", "Undetermined": "UNDETERMINED",
}
LANGUAGE_CLASS_MAP = {
    "Assembly": "ASSEMBLY", "Compiled": "COMPILED",
    "Hardware Description Language": "HARDWARE_DESCRIPTION_LANGUAGE",
    "Interpreted": "INTERPRETED", "Object-Oriented": "OBJECT_ORIENTED",
    "Memory-Unsafe": "MEMORY_UNSAFE", "Not Language-Specific": "NOT_LANGUAGE_SPECIFIC",
}
LANGUAGE_NAME_MAP = {
    "Ada": "ADA", "ARM Assembly": "ARM_ASSEMBLY", "ASP": "ASP", "ASP.NET": "ASP_DOT_NET",
    "Basic": "BASIC", "C": "C", "C++": "C_PLUS_PLUS", "C#": "C_SHARP", "COBOL": "COBOL",
    "Fortran": "FORTRAN", "F#": "F_SHARP", "Go": "GO", "HTML": "HTML", "Java": "JAVA",
    "JavaScript": "JAVASCRIPT", "JSON": "JSON", "JSP": "JSP", "Objective-C": "OBJECTIVE_C",
    "Pascal": "PASCAL", "Perl": "PERL", "PHP": "PHP", "Pseudocode": "PSEUDOCODE",
    "Python": "PYTHON", "Ruby": "RUBY", "Rust": "RUST", "Shell": "SHELL", "SQL": "SQL",
    "Swift": "SWIFT", "VB.NET": "VB_DOT_NET", "Verilog": "VERILOG", "VHDL": "VHDL",
    "XML": "XML", "x86 Assembly": "X86_ASSEMBLY", "Other": "OTHER",
}
OS_CLASS_MAP = {
    "Linux": "LINUX", "macOS": "MACOS", "Unix": "UNIX", "Windows": "WINDOWS",
    "Not OS-Specific": "NOT_OS_SPECIFIC",
}
OS_NAME_MAP = {
    "AIX": "AIX", "Android": "ANDROID", "BlackBerry OS": "BLACKBERRY_OS",
    "Chrome OS": "CHROME_OS", "Darwin": "DARWIN", "FreeBSD": "FREEBSD", "iOS": "IOS",
    "macOS": "MACOS", "NetBSD": "NETBSD", "OpenBSD": "OPENBSD", "Red Hat": "RED_HAT",
    "Solaris": "SOLARIS", "SUSE": "SUSE", "tvOS": "TVOS", "Ubuntu": "UBUNTU",
    "watchOS": "WATCHOS", "Windows 9x": "WINDOWS_9X", "Windows Embedded": "WINDOWS_EMBEDDED",
    "Windows NT": "WINDOWS_NT",
}
ARCH_CLASS_MAP = {
    "Embedded": "EMBEDDED", "Microcomputer": "MICROCOMPUTER", "Workstation": "WORKSTATION",
    "Not Architecture-Specific": "NOT_ARCHITECTURE_SPECIFIC",
}
ARCH_NAME_MAP = {
    "Alpha": "ALPHA", "ARM": "ARM", "Itanium": "ITANIUM",
    "Power Architecture": "POWER_ARCHITECTURE", "SPARC": "SPARC", "x86": "X86", "Other": "OTHER",
}
TECH_CLASS_MAP = {
    "Client Server": "CLIENT_SERVER", "Cloud Computing": "CLOUD_COMPUTING", "ICS/OT": "ICS_OT",
    "Mainframe": "MAINFRAME", "Mobile": "MOBILE", "N-Tier": "N_TIER", "SOA": "SOA",
    "System on Chip": "SYSTEM_ON_CHIP", "Web Based": "WEB_BASED",
    "Not Technology-Specific": "NOT_TECHNOLOGY_SPECIFIC",
}
TECH_NAME_MAP = {
    "AI/ML": "AI_ML", "Web Server": "WEB_SERVER", "Database Server": "DATABASE_SERVER",
    "Accelerator Hardware": "ACCELERATOR_HARDWARE",
    "Analog and Mixed Signal Hardware": "ANALOG_AND_MIXED_SIGNAL_HARDWARE",
    "Audio/Video Hardware": "AUDIO_VIDEO_HARDWARE", "Bus/Interface Hardware": "BUS_INTERFACE_HARDWARE",
    "Clock/Counter Hardware": "CLOCK_COUNTER_HARDWARE", "Communication Hardware": "COMMUNICATION_HARDWARE",
    "Controller Hardware": "CONTROLLER_HARDWARE", "Memory Hardware": "MEMORY_HARDWARE",
    "Microcontroller Hardware": "MICROCONTROLLER_HARDWARE",
    "Network on Chip Hardware": "NETWORK_ON_CHIP_HARDWARE",
    "Power Management Hardware": "POWER_MANAGEMENT_HARDWARE", "Processor Hardware": "PROCESSOR_HARDWARE",
    "Security Hardware": "SECURITY_HARDWARE", "Sensor Hardware": "SENSOR_HARDWARE",
    "Storage Hardware": "STORAGE_HARDWARE", "Test/Debug Hardware": "TEST_DEBUG_HARDWARE",
    "Other": "OTHER",
}
PHASE_MAP = {
    "Policy": "POLICY", "Requirements": "REQUIREMENTS",
    "Architecture and Design": "ARCHITECTURE_AND_DESIGN", "Implementation": "IMPLEMENTATION",
    "Build and Compilation": "BUILD_AND_COMPILATION", "Testing": "TESTING",
    "Documentation": "DOCUMENTATION", "Bundling": "BUNDLING", "Distribution": "DISTRIBUTION",
    "Installation": "INSTALLATION", "System Configuration": "SYSTEM_CONFIGURATION",
    "Operation": "OPERATION", "Patching and Maintenance": "PATCHING_AND_MAINTENANCE",
    "Porting": "PORTING", "Integration": "INTEGRATION", "Manufacturing": "MANUFACTURING",
    "Decommissioning and End-of-Life": "DECOMMISSIONING_AND_END_OF_LIFE",
}
STRATEGY_MAP = {
    "Attack Surface Reduction": "ATTACK_SURFACE_REDUCTION",
    "Compilation or Build Hardening": "COMPILATION_OR_BUILD_HARDENING",
    "Enforcement by Conversion": "ENFORCEMENT_BY_CONVERSION",
    "Environment Hardening": "ENVIRONMENT_HARDENING", "Firewall": "FIREWALL",
    "Input Validation": "INPUT_VALIDATION", "Language Selection": "LANGUAGE_SELECTION",
    "Libraries or Frameworks": "LIBRARIES_OR_FRAMEWORKS",
    "Resource Limitation": "RESOURCE_LIMITATION", "Output Encoding": "OUTPUT_ENCODING",
    "Parameterization": "PARAMETERIZATION", "Refactoring": "REFACTORING",
    "Sandbox or Jail": "SANDBOX_OR_JAIL", "Separation of Privilege": "SEPARATION_OF_PRIVILEGE",
}
EFFECTIVENESS_MAP = {
    "High": "HIGH", "Moderate": "MODERATE", "Limited": "LIMITED",
    "Incidental": "INCIDENTAL", "Discouraged Common Practice": "DISCOURAGED_COMMON_PRACTICE",
    "Defense in Depth": "DEFENSE_IN_DEPTH", "None": "NONE",
}
DETECTION_METHOD_MAP = {
    "Automated Analysis": "AUTOMATED_ANALYSIS",
    "Automated Dynamic Analysis": "AUTOMATED_DYNAMIC_ANALYSIS",
    "Automated Static Analysis": "AUTOMATED_STATIC_ANALYSIS",
    "Automated Static Analysis - Source Code": "AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE",
    "Automated Static Analysis - Binary or Bytecode": "AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
    "Fuzzing": "FUZZING", "Manual Analysis": "MANUAL_ANALYSIS",
    "Manual Dynamic Analysis": "MANUAL_DYNAMIC_ANALYSIS",
    "Manual Static Analysis": "MANUAL_STATIC_ANALYSIS",
    "Manual Static Analysis - Source Code": "MANUAL_STATIC_ANALYSIS_SOURCE_CODE",
    "Manual Static Analysis - Binary or Bytecode": "MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
    "White Box": "WHITE_BOX", "Black Box": "BLACK_BOX",
    "Architecture or Design Review": "ARCHITECTURE_OR_DESIGN_REVIEW",
    "Dynamic Analysis with Manual Results Interpretation": "DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION",
    "Dynamic Analysis with Automated Results Interpretation": "DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION",
    "Formal Verification": "FORMAL_VERIFICATION", "Simulation / Emulation": "SIMULATION_EMULATION",
    "Other": "OTHER",
}
DETECT_EFFECT_MAP = {
    "High": "HIGH", "Moderate": "MODERATE", "SOAR Partial": "SOAR_PARTIAL",
    "Opportunistic": "OPPORTUNISTIC", "Limited": "LIMITED", "None": "NONE",
}
SCOPE_MAP = {
    "Confidentiality": "CONFIDENTIALITY", "Integrity": "INTEGRITY",
    "Availability": "AVAILABILITY", "Access Control": "ACCESS_CONTROL",
    "Accountability": "ACCOUNTABILITY", "Authentication": "AUTHENTICATION",
    "Authorization": "AUTHORIZATION", "Non-Repudiation": "NON_REPUDIATION", "Other": "OTHER",
}
TECH_IMPACT_MAP = {
    "Modify Memory": "MODIFY_MEMORY", "Read Memory": "READ_MEMORY",
    "Modify Files or Directories": "MODIFY_FILES_OR_DIRECTORIES",
    "Read Files or Directories": "READ_FILES_OR_DIRECTORIES",
    "Modify Application Data": "MODIFY_APPLICATION_DATA",
    "Read Application Data": "READ_APPLICATION_DATA",
    "DoS: Crash, Exit, or Restart": "DOS_CRASH_EXIT_OR_RESTART",
    "DoS: Amplification": "DOS_AMPLIFICATION", "DoS: Instability": "DOS_INSTABILITY",
    "DoS: Resource Consumption (CPU)": "DOS_RESOURCE_CONSUMPTION_CPU",
    "DoS: Resource Consumption (Memory)": "DOS_RESOURCE_CONSUMPTION_MEMORY",
    "DoS: Resource Consumption (Other)": "DOS_RESOURCE_CONSUMPTION_OTHER",
    "Execute Unauthorized Code or Commands": "EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS",
    "Gain Privileges or Assume Identity": "GAIN_PRIVILEGES_OR_ASSUME_IDENTITY",
    "Bypass Protection Mechanism": "BYPASS_PROTECTION_MECHANISM",
    "Hide Activities": "HIDE_ACTIVITIES", "Alter Execution Logic": "ALTER_EXECUTION_LOGIC",
    "Quality Degradation": "QUALITY_DEGRADATION", "Unexpected State": "UNEXPECTED_STATE",
    "Varies by Context": "VARIES_BY_CONTEXT",
    "Increase Analytical Complexity": "INCREASE_ANALYTICAL_COMPLEXITY",
    "Reduce Maintainability": "REDUCE_MAINTAINABILITY",
    "Reduce Performance": "REDUCE_PERFORMANCE", "Reduce Reliability": "REDUCE_RELIABILITY",
    "Other": "OTHER",
}
FUNC_AREA_MAP = {
    "Authentication": "AUTHENTICATION", "Authorization": "AUTHORIZATION",
    "Code Libraries": "CODE_LIBRARIES", "Counters": "COUNTERS", "Cryptography": "CRYPTOGRAPHY",
    "Error Handling": "ERROR_HANDLING", "Interprocess Communication": "INTERPROCESS_COMMUNICATION",
    "File Processing": "FILE_PROCESSING", "Logging": "LOGGING",
    "Memory Management": "MEMORY_MANAGEMENT", "Networking": "NETWORKING",
    "Number Processing": "NUMBER_PROCESSING", "Program Invocation": "PROGRAM_INVOCATION",
    "Protection Mechanism": "PROTECTION_MECHANISM", "Session Management": "SESSION_MANAGEMENT",
    "Signals": "SIGNALS", "String Processing": "STRING_PROCESSING",
    "Not Functional-Area-Specific": "NOT_FUNCTIONAL_AREA_SPECIFIC",
    "Power": "POWER", "Clock": "CLOCK",
}
RESOURCE_MAP = {
    "CPU": "CPU", "File or Directory": "FILE_OR_DIRECTORY", "Memory": "MEMORY",
    "System Process": "SYSTEM_PROCESS", "Other": "OTHER",
}
NOTE_TYPE_MAP = {
    "Applicable Platform": "APPLICABLE_PLATFORM", "Maintenance": "MAINTENANCE",
    "Relationship": "RELATIONSHIP", "Research Gap": "RESEARCH_GAP",
    "Terminology": "TERMINOLOGY", "Theoretical": "THEORETICAL", "Other": "OTHER",
}
STAKEHOLDER_MAP = {
    "Academic Researchers": "ACADEMIC_RESEARCHERS", "Applied Researchers": "APPLIED_RESEARCHERS",
    "Assessment Teams": "ASSESSMENT_TEAMS", "Assessment Tool Vendors": "ASSESSMENT_TOOL_VENDORS",
    "CWE Team": "CWE_TEAM", "Educators": "EDUCATORS", "Hardware Designers": "HARDWARE_DESIGNERS",
    "Information Providers": "INFORMATION_PROVIDERS", "Product Customers": "PRODUCT_CUSTOMERS",
    "Product Vendors": "PRODUCT_VENDORS", "Software Developers": "SOFTWARE_DEVELOPERS",
    "Vulnerability Analysts": "VULNERABILITY_ANALYSTS", "Other": "OTHER",
}
IMPORTANCE_MAP = {"Normal": "NORMAL", "Critical": "CRITICAL"}
TAXONOMY_FIT_MAP = {
    "Exact": "EXACT", "CWE More Abstract": "CWE_MORE_ABSTRACT",
    "CWE More Specific": "CWE_MORE_SPECIFIC", "Imprecise": "IMPRECISE", "Perspective": "PERSPECTIVE",
}
TAXONOMY_NAME_MAP = {
    "7 Pernicious Kingdoms": "SEVEN_PERNICIOUS_KINGDOMS",
    "19 Deadly Sins": "NINETEEN_DEADLY_SINS", "Aslam": "ASLAM", "Bishop": "BISHOP",
    "CERT C Secure Coding": "CERT_C_SECURE_CODING",
    "CERT C++ Secure Coding": "CERT_C_PLUS_PLUS_SECURE_CODING",
    "The CERT Oracle Secure Coding Standard for Java (2011)": "THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011",
    "CLASP": "CLASP", "ISA/IEC 62443": "ISA_IEC_62443", "Landwehr": "LANDWEHR",
    "OMG ASCSM": "OMG_ASCSM", "OMG ASCRM": "OMG_ASCRM", "OMG ASCMM": "OMG_ASCMM",
    "OMG ASCPEM": "OMG_ASCPEM", "OWASP Top Ten 2004": "OWASP_TOP_TEN_2004",
    "OWASP Top Ten 2007": "OWASP_TOP_TEN_2007", "OWASP Top Ten": "OWASP_TOP_TEN",
    "PLOVER": "PLOVER", "Protection Analysis": "PROTECTION_ANALYSIS", "RISOS": "RISOS",
    "SEI CERT C Coding Standard": "SEI_CERT_C_CODING_STANDARD",
    "SEI CERT C++ Coding Standard": "SEI_CERT_C_PLUS_PLUS_CODING_STANDARD",
    "SEI CERT Oracle Coding Standard for Java": "SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA",
    "SEI CERT Perl Coding Standard": "SEI_CERT_PERL_CODING_STANDARD",
    "Software Fault Patterns": "SOFTWARE_FAULT_PATTERNS",
    "Weber, Karger, Paradkar": "WEBER_KARGER_PARADKAR", "WASC": "WASC",
}
USAGE_MAP = {
    "Discouraged": "DISCOURAGED", "Prohibited": "PROHIBITED",
    "Allowed": "ALLOWED", "Allowed-with-Review": "ALLOWED_WITH_REVIEW",
}
VIEW_TYPE_MAP = {"Implicit": "IMPLICIT", "Explicit": "EXPLICIT", "Graph": "GRAPH"}
REASON_MAP = {
    "Abstraction": "ABSTRACTION", "Category": "CATEGORY", "View": "VIEW",
    "Deprecated": "DEPRECATED", "Potential Deprecation": "POTENTIAL_DEPRECATION",
    "Frequent Misuse": "FREQUENT_MISUSE", "Frequent Misinterpretation": "FREQUENT_MISINTERPRETATION",
    "Multiple Use": "MULTIPLE_USE", "CWE Overlap": "CWE_OVERLAP",
    "Acceptable-Use": "ACCEPTABLE_USE", "Potential Major Changes": "POTENTIAL_MAJOR_CHANGES",
    "Other": "OTHER",
}
CODE_NATURE_MAP = {
    "Attack": "ATTACK", "Bad": "BAD", "Good": "GOOD",
    "Informative": "INFORMATIVE", "Mitigation": "MITIGATION", "Result": "RESULT",
}
CONTRIBUTION_TYPE_MAP = {"Content": "CONTENT", "Feedback": "FEEDBACK"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _tag(local: str) -> str:
    return f"{{{NS}}}{local}"


def _text(el: ET.Element | None, strip_xhtml: bool = True) -> str | None:
    if el is None:
        return None
    # Collect all text within the element (including XHTML children)
    text_parts: list[str] = []
    for part in el.itertext():
        text_parts.append(part)
    raw = "".join(text_parts).strip()
    if strip_xhtml:
        # Collapse whitespace
        raw = re.sub(r"\s+", " ", raw)
    return raw or None


def _child_text(parent: ET.Element, local: str) -> str | None:
    el = parent.find(_tag(local))
    return _text(el)


def _map(value: str | None, mapping: dict[str, str], field: str = "") -> str | None:
    if value is None:
        return None
    result = mapping.get(value)
    if result is None:
        print(f"  WARNING: unmapped {field!r} value {value!r}", file=sys.stderr)
        # Fall back to uppercased slug
        result = re.sub(r"[^A-Z0-9]+", "_", value.upper()).strip("_")
    return result


def _map_list(values: list[str], mapping: dict[str, str], field: str = "") -> list[str]:
    return [_map(v, mapping, field) for v in values if v is not None]  # type: ignore[misc]


def _children_text(parent: ET.Element, local: str) -> list[str]:
    return [_text(el) for el in parent.findall(_tag(local)) if _text(el)]  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Parsers for sub-structures
# ---------------------------------------------------------------------------

def _parse_content_history(ch: ET.Element) -> dict[str, Any]:
    result: dict[str, Any] = {}
    sub = ch.find(_tag("Submission"))
    if sub is not None:
        s: dict[str, Any] = {}
        for field, local in [
            ("submission_name", "Submission_Name"),
            ("submission_organization", "Submission_Organization"),
            ("submission_version", "Submission_Version"),
            ("submission_comment", "Submission_Comment"),
        ]:
            v = _child_text(sub, local)
            if v:
                s[field] = v
        sd = _child_text(sub, "Submission_Date")
        srd = _child_text(sub, "Submission_ReleaseDate")
        sv = _child_text(sub, "Submission_Version")
        if sd:
            s["submission_date"] = sd
        if srd:
            s["submission_release_date"] = srd
        if sv:
            s["submission_version"] = sv
        result["submission"] = s

    mods = []
    for m in ch.findall(_tag("Modification")):
        mod: dict[str, Any] = {}
        for field, local in [
            ("modification_name", "Modification_Name"),
            ("modification_organization", "Modification_Organization"),
            ("modification_version", "Modification_Version"),
            ("modification_comment", "Modification_Comment"),
        ]:
            v = _child_text(m, local)
            if v:
                mod[field] = v
        md = _child_text(m, "Modification_Date")
        mrd = _child_text(m, "Modification_ReleaseDate")
        mi = _child_text(m, "Modification_Importance")
        if md:
            mod["modification_date"] = md
        if mrd:
            mod["modification_release_date"] = mrd
        if mi:
            mod["modification_importance"] = _map(mi, IMPORTANCE_MAP, "Modification_Importance")
        if mod:
            mods.append(mod)
    if mods:
        result["modifications"] = mods

    contribs = []
    for c in ch.findall(_tag("Contribution")):
        contrib: dict[str, Any] = {}
        ct = c.get("Type")
        if ct:
            contrib["type"] = _map(ct, CONTRIBUTION_TYPE_MAP, "Contribution.Type")
        for field, local in [
            ("contribution_name", "Contribution_Name"),
            ("contribution_organization", "Contribution_Organization"),
            ("contribution_version", "Contribution_Version"),
            ("contribution_comment", "Contribution_Comment"),
        ]:
            v = _child_text(c, local)
            if v:
                contrib[field] = v
        cd = _child_text(c, "Contribution_Date")
        crd = _child_text(c, "Contribution_ReleaseDate")
        if cd:
            contrib["contribution_date"] = cd
        if crd:
            contrib["contribution_release_date"] = crd
        if contrib:
            contribs.append(contrib)
    if contribs:
        result["contributions"] = contribs

    prev_names = []
    for p in ch.findall(_tag("Previous_Entry_Name")):
        pn: dict[str, Any] = {}
        pn_text = _text(p)
        pn_date = p.get("Date")
        pn_version = p.get("Version")
        if pn_text:
            pn["name"] = pn_text
        if pn_date:
            pn["date"] = pn_date
        if pn_version:
            pn["version"] = pn_version
        if pn:
            prev_names.append(pn)
    if prev_names:
        result["previous_entry_names"] = prev_names

    return result


def _parse_mapping_notes(mn: ET.Element) -> dict[str, Any]:
    result: dict[str, Any] = {}
    usage = _child_text(mn, "Usage")
    if usage:
        result["usage"] = _map(usage, USAGE_MAP, "Usage")
    rationale = _child_text(mn, "Rationale")
    if rationale:
        result["rationale"] = rationale
    comments = _child_text(mn, "Comments")
    if comments:
        result["comments"] = comments
    reasons_el = mn.find(_tag("Reasons"))
    if reasons_el is not None:
        reasons = []
        for r in reasons_el.findall(_tag("Reason")):
            rt = r.get("Type")
            if rt:
                mapped = _map(rt, REASON_MAP, "Reason.Type")
                if mapped:
                    reasons.append(mapped)
        if reasons:
            result["reasons"] = reasons
    suggestions = []
    for s in mn.findall(_tag("Suggestion")):
        sug: dict[str, Any] = {}
        cwe_id = s.get("CWE_ID") or _child_text(s, "CWE_ID")
        comment = _child_text(s, "Comment")
        if cwe_id:
            sug["cwe_id"] = int(cwe_id)
        if comment:
            sug["comment"] = comment
        if sug:
            suggestions.append(sug)
    if suggestions:
        result["suggestions"] = suggestions
    return result


def _parse_weakness(w: ET.Element, used_refs: set[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": int(w.get("ID", "0")),
        "name": w.get("Name", ""),
        "abstraction": _map(w.get("Abstraction"), ABSTRACTION_MAP, "Abstraction"),
        "structure": _map(w.get("Structure"), STRUCTURE_MAP, "Structure"),
        "status": _map(w.get("Status"), STATUS_MAP, "Status"),
    }

    desc = _child_text(w, "Description")
    if desc:
        result["description"] = desc

    ext_desc = w.find(_tag("Extended_Description"))
    if ext_desc is not None:
        t = _text(ext_desc)
        if t:
            result["extended_description"] = t

    # Related weaknesses
    rw_el = w.find(_tag("Related_Weaknesses"))
    if rw_el is not None:
        rws = []
        for rw in rw_el.findall(_tag("Related_Weakness")):
            entry: dict[str, Any] = {
                "nature": _map(rw.get("Nature"), NATURE_MAP, "Nature"),
                "cwe_id": int(rw.get("CWE_ID", "0")),
                "view_id": int(rw.get("View_ID", "0")),
            }
            ordinal = rw.get("Ordinal")
            if ordinal:
                entry["ordinal"] = _map(ordinal, ORDINAL_MAP, "Ordinal")
            chain_id = rw.get("Chain_ID")
            if chain_id:
                entry["chain_id"] = int(chain_id)
            rws.append(entry)
        if rws:
            result["related_weaknesses"] = rws

    # Weakness ordinalities
    wo_el = w.find(_tag("Weakness_Ordinalities"))
    if wo_el is not None:
        wos = []
        for wo in wo_el.findall(_tag("Weakness_Ordinality")):
            entry = {}
            ord_val = _child_text(wo, "Ordinality")
            if ord_val:
                entry["ordinality"] = _map(ord_val, ORDINALITY_MAP, "Ordinality")
            desc_val = _child_text(wo, "Description")
            if desc_val:
                entry["description"] = desc_val
            if entry:
                wos.append(entry)
        if wos:
            result["weakness_ordinalities"] = wos

    # Applicable platforms
    ap_el = w.find(_tag("Applicable_Platforms"))
    if ap_el is not None:
        ap: dict[str, Any] = {}
        langs = []
        for lang in ap_el.findall(_tag("Language")):
            lp: dict[str, Any] = {"prevalence": _map(lang.get("Prevalence"), PREVALENCE_MAP, "Prevalence")}
            lc = lang.get("Class")
            ln = lang.get("Name")
            if lc:
                lp["class_"] = _map(lc, LANGUAGE_CLASS_MAP, "Language.Class")
            if ln:
                lp["name"] = _map(ln, LANGUAGE_NAME_MAP, "Language.Name")
            langs.append(lp)
        if langs:
            ap["languages"] = langs
        oss = []
        for os_el in ap_el.findall(_tag("Operating_System")):
            osp: dict[str, Any] = {"prevalence": _map(os_el.get("Prevalence"), PREVALENCE_MAP, "Prevalence")}
            oc = os_el.get("Class")
            on = os_el.get("Name")
            ov = os_el.get("Version")
            if oc:
                osp["class_"] = _map(oc, OS_CLASS_MAP, "OS.Class")
            if on:
                osp["name"] = _map(on, OS_NAME_MAP, "OS.Name")
            if ov:
                osp["version"] = ov
            oss.append(osp)
        if oss:
            ap["operating_systems"] = oss
        archs = []
        for arch in ap_el.findall(_tag("Architecture")):
            archp: dict[str, Any] = {"prevalence": _map(arch.get("Prevalence"), PREVALENCE_MAP, "Prevalence")}
            ac = arch.get("Class")
            an = arch.get("Name")
            if ac:
                archp["class_"] = _map(ac, ARCH_CLASS_MAP, "Arch.Class")
            if an:
                archp["name"] = _map(an, ARCH_NAME_MAP, "Arch.Name")
            archs.append(archp)
        if archs:
            ap["architectures"] = archs
        techs = []
        for tech in ap_el.findall(_tag("Technology")):
            tp: dict[str, Any] = {"prevalence": _map(tech.get("Prevalence"), PREVALENCE_MAP, "Prevalence")}
            tc = tech.get("Class")
            tn = tech.get("Name")
            if tc:
                tp["class_"] = _map(tc, TECH_CLASS_MAP, "Tech.Class")
            if tn:
                tp["name"] = _map(tn, TECH_NAME_MAP, "Tech.Name")
            techs.append(tp)
        if techs:
            ap["technologies"] = techs
        if ap:
            result["applicable_platforms"] = ap

    # Background details
    bg_el = w.find(_tag("Background_Details"))
    if bg_el is not None:
        bgs = _children_text(bg_el, "Background_Detail")
        if bgs:
            result["background_details"] = bgs

    # Alternate terms
    at_el = w.find(_tag("Alternate_Terms"))
    if at_el is not None:
        ats = []
        for at in at_el.findall(_tag("Alternate_Term")):
            aterm: dict[str, Any] = {}
            term = _child_text(at, "Term")
            desc_t = _child_text(at, "Description")
            if term:
                aterm["term"] = term
            if desc_t:
                aterm["description"] = desc_t
            if aterm:
                ats.append(aterm)
        if ats:
            result["alternate_terms"] = ats

    # Modes of introduction
    moi_el = w.find(_tag("Modes_Of_Introduction"))
    if moi_el is not None:
        intros = []
        for intro in moi_el.findall(_tag("Introduction")):
            phase = _child_text(intro, "Phase")
            note = _child_text(intro, "Note")
            entry: dict[str, Any] = {}
            if phase:
                entry["phase"] = _map(phase, PHASE_MAP, "Phase")
            if note:
                entry["note"] = note
            if entry:
                intros.append(entry)
        if intros:
            result["modes_of_introduction"] = intros

    # Likelihood of exploit
    loe = _child_text(w, "Likelihood_Of_Exploit")
    if loe:
        result["likelihood_of_exploit"] = _map(loe, LIKELIHOOD_MAP, "Likelihood_Of_Exploit")

    # Common consequences
    cc_el = w.find(_tag("Common_Consequences"))
    if cc_el is not None:
        cons = []
        for c in cc_el.findall(_tag("Consequence")):
            centry: dict[str, Any] = {}
            cid = c.get("Consequence_ID")
            if cid:
                centry["consequence_id"] = cid
            scopes = _map_list(_children_text(c, "Scope"), SCOPE_MAP, "Scope")
            impacts = _map_list(_children_text(c, "Impact"), TECH_IMPACT_MAP, "Impact")
            if scopes:
                centry["scopes"] = scopes
            if impacts:
                centry["impacts"] = impacts
            lk = _child_text(c, "Likelihood")
            if lk:
                centry["likelihood"] = _map(lk, LIKELIHOOD_MAP, "Likelihood")
            note = _child_text(c, "Note")
            if note:
                centry["note"] = note
            if centry:
                cons.append(centry)
        if cons:
            result["common_consequences"] = cons

    # Detection methods
    dm_el = w.find(_tag("Detection_Methods"))
    if dm_el is not None:
        dms = []
        for dm in dm_el.findall(_tag("Detection_Method")):
            dentry: dict[str, Any] = {}
            dmid = dm.get("Detection_Method_ID")
            if dmid:
                dentry["detection_method_id"] = dmid
            method = _child_text(dm, "Method")
            if method:
                dentry["method"] = _map(method, DETECTION_METHOD_MAP, "Method")
            desc_d = _child_text(dm, "Description")
            if desc_d:
                dentry["description"] = desc_d
            eff = _child_text(dm, "Effectiveness")
            if eff:
                dentry["effectiveness"] = _map(eff, DETECT_EFFECT_MAP, "Detection Effectiveness")
            eff_notes = _child_text(dm, "Effectiveness_Notes")
            if eff_notes:
                dentry["effectiveness_notes"] = eff_notes
            if dentry:
                dms.append(dentry)
        if dms:
            result["detection_methods"] = dms

    # Potential mitigations
    pm_el = w.find(_tag("Potential_Mitigations"))
    if pm_el is not None:
        mits = []
        for m in pm_el.findall(_tag("Mitigation")):
            mentry: dict[str, Any] = {}
            mid = m.get("Mitigation_ID")
            if mid:
                mentry["mitigation_id"] = mid
            phases = _map_list(_children_text(m, "Phase"), PHASE_MAP, "Phase")
            if phases:
                mentry["phases"] = phases
            strategy = _child_text(m, "Strategy")
            if strategy:
                mentry["strategy"] = _map(strategy, STRATEGY_MAP, "Strategy")
            desc_m = _child_text(m, "Description")
            if desc_m:
                mentry["description"] = desc_m
            eff = _child_text(m, "Effectiveness")
            if eff:
                mentry["effectiveness"] = _map(eff, EFFECTIVENESS_MAP, "Effectiveness")
            eff_notes = _child_text(m, "Effectiveness_Notes")
            if eff_notes:
                mentry["effectiveness_notes"] = eff_notes
            if mentry:
                mits.append(mentry)
        if mits:
            result["potential_mitigations"] = mits

    # Demonstrative examples
    de_el = w.find(_tag("Demonstrative_Examples"))
    if de_el is not None:
        des = []
        for de in de_el.findall(_tag("Demonstrative_Example")):
            dentry: dict[str, Any] = {}
            deid = de.get("Demonstrative_Example_ID")
            if deid:
                dentry["demonstrative_example_id"] = deid
            title = _child_text(de, "Title_Text")
            if title:
                dentry["title_text"] = title
            intro = _child_text(de, "Intro_Text")
            if intro:
                dentry["intro_text"] = intro
            bodies = _children_text(de, "Body_Text")
            if bodies:
                dentry["body_texts"] = bodies
            codes = []
            for ec in de.findall(_tag("Example_Code")):
                nature = ec.get("Nature")
                lang = ec.get("Language")
                content = _text(ec)
                centry: dict[str, Any] = {}
                if nature:
                    centry["nature"] = _map(nature, CODE_NATURE_MAP, "Code Nature")
                if lang:
                    centry["language"] = _map(lang, LANGUAGE_NAME_MAP, "Language.Name")
                if content:
                    centry["content"] = content
                if centry:
                    codes.append(centry)
            if codes:
                dentry["example_codes"] = codes
            if dentry:
                des.append(dentry)
        if des:
            result["demonstrative_examples"] = des

    # Observed examples
    oe_el = w.find(_tag("Observed_Examples"))
    if oe_el is not None:
        oes = []
        for oe in oe_el.findall(_tag("Observed_Example")):
            ref = _child_text(oe, "Reference")
            desc_o = _child_text(oe, "Description")
            link = _child_text(oe, "Link")
            oentry: dict[str, Any] = {}
            if ref:
                oentry["reference"] = ref
            if desc_o:
                oentry["description"] = desc_o
            if link:
                oentry["link"] = link
            if oentry:
                oes.append(oentry)
        if oes:
            result["observed_examples"] = oes

    # Functional areas
    fa_el = w.find(_tag("Functional_Areas"))
    if fa_el is not None:
        fas = _map_list(_children_text(fa_el, "Functional_Area"), FUNC_AREA_MAP, "Functional_Area")
        if fas:
            result["functional_areas"] = fas

    # Affected resources
    ar_el = w.find(_tag("Affected_Resources"))
    if ar_el is not None:
        ars = _map_list(_children_text(ar_el, "Affected_Resource"), RESOURCE_MAP, "Affected_Resource")
        if ars:
            result["affected_resources"] = ars

    # Related attack patterns
    rap_el = w.find(_tag("Related_Attack_Patterns"))
    if rap_el is not None:
        raps = []
        for rap in rap_el.findall(_tag("Related_Attack_Pattern")):
            capec_id = rap.get("CAPEC_ID")
            if capec_id:
                raps.append(int(capec_id))
        if raps:
            result["related_attack_patterns"] = raps

    # Taxonomy mappings
    tm_el = w.find(_tag("Taxonomy_Mappings"))
    if tm_el is not None:
        tms = []
        for tm in tm_el.findall(_tag("Taxonomy_Mapping")):
            tentry: dict[str, Any] = {}
            tname = tm.get("Taxonomy_Name")
            if tname:
                tentry["taxonomy_name"] = _map(tname, TAXONOMY_NAME_MAP, "Taxonomy_Name")
            eid = _child_text(tm, "Entry_ID")
            if eid:
                tentry["entry_id"] = eid
            en = _child_text(tm, "Entry_Name")
            if en:
                tentry["entry_name"] = en
            fit = _child_text(tm, "Mapping_Fit")
            if fit:
                tentry["mapping_fit"] = _map(fit, TAXONOMY_FIT_MAP, "Mapping_Fit")
            if tentry:
                tms.append(tentry)
        if tms:
            result["taxonomy_mappings"] = tms

    # Notes
    notes_el = w.find(_tag("Notes"))
    if notes_el is not None:
        notes = []
        for n in notes_el.findall(_tag("Note")):
            ntype = n.get("Type")
            content = _text(n)
            nentry: dict[str, Any] = {}
            if ntype:
                nentry["type"] = _map(ntype, NOTE_TYPE_MAP, "Note.Type")
            if content:
                nentry["content"] = content
            if nentry:
                notes.append(nentry)
        if notes:
            result["notes"] = notes

    # References
    refs_el = w.find(_tag("References"))
    if refs_el is not None:
        refs = []
        for r in refs_el.findall(_tag("Reference")):
            ref_id = r.get("External_Reference_ID")
            section = r.get("Section") or _child_text(r, "Section")
            rentry: dict[str, Any] = {}
            if ref_id:
                rentry["external_reference_id"] = ref_id
                used_refs.add(ref_id)
            if section:
                rentry["section"] = section
            if rentry:
                refs.append(rentry)
        if refs:
            result["references"] = refs

    # Mapping notes
    mn_el = w.find(_tag("Mapping_Notes"))
    if mn_el is not None:
        result["mapping_notes"] = _parse_mapping_notes(mn_el)
    else:
        # Provide required defaults
        result["mapping_notes"] = {
            "usage": "ALLOWED",
            "rationale": "No mapping notes provided.",
            "comments": "No mapping notes provided.",
            "reasons": ["ACCEPTABLE_USE"],
        }

    # Content history
    ch_el = w.find(_tag("Content_History"))
    if ch_el is not None:
        result["content_history"] = _parse_content_history(ch_el)
    else:
        result["content_history"] = {
            "submission": {
                "submission_date": "2006-07-19",
                "submission_version": "Draft 3",
                "submission_release_date": "2006-07-19",
            }
        }

    return result


def _parse_category(c: ET.Element, used_refs: set[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": int(c.get("ID", "0")),
        "name": c.get("Name", ""),
        "status": _map(c.get("Status"), STATUS_MAP, "Status"),
    }

    summary = _child_text(c, "Summary")
    if summary:
        result["summary"] = summary

    # Relationships
    rels_el = c.find(_tag("Relationships"))
    if rels_el is not None:
        rels: dict[str, Any] = {}
        member_of = []
        for m in rels_el.findall(_tag("Member_Of")):
            mentry: dict[str, Any] = {
                "cwe_id": int(m.get("CWE_ID", "0")),
                "view_id": int(m.get("View_ID", "0")),
            }
            member_of.append(mentry)
        if member_of:
            rels["member_of"] = member_of
        has_member = []
        for m in rels_el.findall(_tag("Has_Member")):
            mentry = {
                "cwe_id": int(m.get("CWE_ID", "0")),
                "view_id": int(m.get("View_ID", "0")),
            }
            has_member.append(mentry)
        if has_member:
            rels["has_member"] = has_member
        if rels:
            result["relationships"] = rels

    # Notes
    notes_el = c.find(_tag("Notes"))
    if notes_el is not None:
        notes = []
        for n in notes_el.findall(_tag("Note")):
            ntype = n.get("Type")
            content = _text(n)
            nentry: dict[str, Any] = {}
            if ntype:
                nentry["type"] = _map(ntype, NOTE_TYPE_MAP, "Note.Type")
            if content:
                nentry["content"] = content
            if nentry:
                notes.append(nentry)
        if notes:
            result["notes"] = notes

    # References
    refs_el = c.find(_tag("References"))
    if refs_el is not None:
        refs = []
        for r in refs_el.findall(_tag("Reference")):
            ref_id = r.get("External_Reference_ID")
            section = r.get("Section") or _child_text(r, "Section")
            rentry: dict[str, Any] = {}
            if ref_id:
                rentry["external_reference_id"] = ref_id
                used_refs.add(ref_id)
            if section:
                rentry["section"] = section
            if rentry:
                refs.append(rentry)
        if refs:
            result["references"] = refs

    # Taxonomy mappings
    tm_el = c.find(_tag("Taxonomy_Mappings"))
    if tm_el is not None:
        tms = []
        for tm in tm_el.findall(_tag("Taxonomy_Mapping")):
            tentry: dict[str, Any] = {}
            tname = tm.get("Taxonomy_Name")
            if tname:
                tentry["taxonomy_name"] = _map(tname, TAXONOMY_NAME_MAP, "Taxonomy_Name")
            eid = _child_text(tm, "Entry_ID")
            if eid:
                tentry["entry_id"] = eid
            en = _child_text(tm, "Entry_Name")
            if en:
                tentry["entry_name"] = en
            fit = _child_text(tm, "Mapping_Fit")
            if fit:
                tentry["mapping_fit"] = _map(fit, TAXONOMY_FIT_MAP, "Mapping_Fit")
            if tentry:
                tms.append(tentry)
        if tms:
            result["taxonomy_mappings"] = tms

    # Mapping notes
    mn_el = c.find(_tag("Mapping_Notes"))
    if mn_el is not None:
        result["mapping_notes"] = _parse_mapping_notes(mn_el)
    else:
        result["mapping_notes"] = {
            "usage": "PROHIBITED",
            "rationale": "Category entry.",
            "comments": "Categories should not be used for mapping.",
            "reasons": ["CATEGORY"],
        }

    # Content history
    ch_el = c.find(_tag("Content_History"))
    if ch_el is not None:
        result["content_history"] = _parse_content_history(ch_el)
    else:
        result["content_history"] = {
            "submission": {
                "submission_date": "2006-07-19",
                "submission_version": "Draft 3",
                "submission_release_date": "2006-07-19",
            }
        }

    return result


def _parse_view(v: ET.Element, used_refs: set[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": int(v.get("ID", "0")),
        "name": v.get("Name", ""),
        "type": _map(v.get("Type"), VIEW_TYPE_MAP, "View.Type"),
        "status": _map(v.get("Status"), STATUS_MAP, "Status"),
    }

    obj = _child_text(v, "Objective")
    if obj:
        result["objective"] = obj

    # Audience
    aud_el = v.find(_tag("Audience"))
    if aud_el is not None:
        stakeholders = []
        for s in aud_el.findall(_tag("Stakeholder")):
            stype = _child_text(s, "Type")
            sdesc = _child_text(s, "Description")
            sentry: dict[str, Any] = {}
            if stype:
                sentry["type"] = _map(stype, STAKEHOLDER_MAP, "Stakeholder.Type")
            if sdesc:
                sentry["description"] = sdesc
            if sentry:
                stakeholders.append(sentry)
        if stakeholders:
            result["audience"] = stakeholders

    # Members
    members_el = v.find(_tag("Members"))
    if members_el is not None:
        members = []
        for m in members_el.findall(_tag("Has_Member")):
            mentry = {
                "cwe_id": int(m.get("CWE_ID", "0")),
                "view_id": int(m.get("View_ID", "0")),
            }
            members.append(mentry)
        if members:
            result["members"] = members

    # Filter
    filt = _child_text(v, "Filter")
    if filt:
        result["filter"] = filt

    # Notes
    notes_el = v.find(_tag("Notes"))
    if notes_el is not None:
        notes = []
        for n in notes_el.findall(_tag("Note")):
            ntype = n.get("Type")
            content = _text(n)
            nentry: dict[str, Any] = {}
            if ntype:
                nentry["type"] = _map(ntype, NOTE_TYPE_MAP, "Note.Type")
            if content:
                nentry["content"] = content
            if nentry:
                notes.append(nentry)
        if notes:
            result["notes"] = notes

    # References
    refs_el = v.find(_tag("References"))
    if refs_el is not None:
        refs = []
        for r in refs_el.findall(_tag("Reference")):
            ref_id = r.get("External_Reference_ID")
            section = r.get("Section") or _child_text(r, "Section")
            rentry: dict[str, Any] = {}
            if ref_id:
                rentry["external_reference_id"] = ref_id
                used_refs.add(ref_id)
            if section:
                rentry["section"] = section
            if rentry:
                refs.append(rentry)
        if refs:
            result["references"] = refs

    # Mapping notes
    mn_el = v.find(_tag("Mapping_Notes"))
    if mn_el is not None:
        result["mapping_notes"] = _parse_mapping_notes(mn_el)
    else:
        result["mapping_notes"] = {
            "usage": "PROHIBITED",
            "rationale": "View entry.",
            "comments": "Views should not be used for mapping.",
            "reasons": ["VIEW"],
        }

    # Content history
    ch_el = v.find(_tag("Content_History"))
    if ch_el is not None:
        result["content_history"] = _parse_content_history(ch_el)
    else:
        result["content_history"] = {
            "submission": {
                "submission_date": "2006-07-19",
                "submission_version": "Draft 3",
                "submission_release_date": "2006-07-19",
            }
        }

    return result


def _parse_external_reference(er: ET.Element) -> dict[str, Any]:
    result: dict[str, Any] = {
        "reference_id": er.get("Reference_ID", ""),
    }
    title = _child_text(er, "Title")
    if title:
        result["title"] = title
    authors = _children_text(er, "Author")
    if authors:
        result["authors"] = authors
    edition = _child_text(er, "Edition")
    if edition:
        result["edition"] = edition
    publication = _child_text(er, "Publication")
    if publication:
        result["publication"] = publication
    pub_year = _child_text(er, "Publication_Year")
    if pub_year:
        result["publication_year"] = pub_year
    pub_month = _child_text(er, "Publication_Month")
    if pub_month:
        result["publication_month"] = pub_month
    pub_day = _child_text(er, "Publication_Day")
    if pub_day:
        result["publication_day"] = pub_day
    publisher = _child_text(er, "Publisher")
    if publisher:
        result["publisher"] = publisher
    url_el = er.find(_tag("URL"))
    if url_el is not None and url_el.text:
        result["url"] = url_el.text.strip()
    url_date = _child_text(er, "URL_Date")
    if url_date:
        result["url_date"] = url_date
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    xml_input = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("tests/data/cwe/cwec_v4.19.1.xml")
    yaml_output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("tests/data/valid/WeaknessCatalog-001.yaml")

    print(f"Reading {xml_input} ...", file=sys.stderr)
    tree = ET.parse(xml_input)
    root = tree.getroot()

    catalog_name = root.get("Name", "CWE")
    catalog_version = root.get("Version", "")
    catalog_date = root.get("Date", "")

    used_refs: set[str] = set()

    # --- Weaknesses ---
    weaknesses_root = root.find(_tag("Weaknesses"))
    weakness_list = []
    if weaknesses_root is not None:
        for w in weaknesses_root.findall(_tag("Weakness")):
            weakness_list.append(_parse_weakness(w, used_refs))
    print(f"Extracted {len(weakness_list)} weakness(es).", file=sys.stderr)

    # --- Categories ---
    categories_root = root.find(_tag("Categories"))
    category_list = []
    if categories_root is not None:
        for c in categories_root.findall(_tag("Category")):
            category_list.append(_parse_category(c, used_refs))
    print(f"Extracted {len(category_list)} category(ies).", file=sys.stderr)

    # --- Views ---
    views_root = root.find(_tag("Views"))
    view_list = []
    if views_root is not None:
        for v in views_root.findall(_tag("View")):
            view_list.append(_parse_view(v, used_refs))
    print(f"Extracted {len(view_list)} view(s).", file=sys.stderr)

    # --- External references (only those actually used) ---
    ext_refs_root = root.find(_tag("External_References"))
    ext_ref_list = []
    if ext_refs_root is not None:
        for er in ext_refs_root.findall(_tag("External_Reference")):
            ref_id = er.get("Reference_ID", "")
            if ref_id in used_refs:
                ext_ref_list.append(_parse_external_reference(er))
    # Sort by reference ID
    ext_ref_list.sort(key=lambda x: x.get("reference_id", ""))
    print(f"Included {len(ext_ref_list)} external reference(s).", file=sys.stderr)

    catalog: dict[str, Any] = {
        "name": catalog_name,
        "version": catalog_version,
        "date": catalog_date,
    }
    if weakness_list:
        catalog["weaknesses"] = weakness_list
    if category_list:
        catalog["categories"] = category_list
    if view_list:
        catalog["views"] = view_list
    if ext_ref_list:
        catalog["external_references"] = ext_ref_list

    yaml_output.parent.mkdir(parents=True, exist_ok=True)
    with yaml_output.open("w", encoding="utf-8") as fh:
        yaml.dump(
            catalog,
            fh,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )
    print(f"Written to {yaml_output}", file=sys.stderr)


if __name__ == "__main__":
    main()
