from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "5.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'xsd_date': {'tag': 'xsd_date', 'value': '2026-10-28'},
                     'xsd_namespace': {'tag': 'xsd_namespace',
                                       'value': 'http://cwe.mitre.org/cwe-8'},
                     'xsd_version': {'tag': 'xsd_version', 'value': '8.0'}},
     'comments': ['The version is the edition of the CWE List that the schema '
                  'renders, which is the first edition under XML Schema 8.0. '
                  'upstream/ holds both files unchanged, tests/test_coverage.py '
                  'holds the schema to the XSD, and '
                  'scripts/check_upstream_release.py reports when either moves.',
                  'The file behind the cwe_schema_latest.xsd link is an earlier '
                  'copy of 8.0, which the catalogue breaks in 69 places. The '
                  'source above is the file the catalogue itself names, and it '
                  'validates with no error.'],
     'default_prefix': 'cwe',
     'default_range': 'string',
     'description': 'A LinkML model of the Common Weakness Enumeration, the '
                    'catalogue of software and hardware weakness types that The '
                    'MITRE Corporation publishes for the CWE Program. It renders '
                    "the catalogue's XML Schema with its own element names and "
                    'values, so the whole catalogue validates with both unchanged.',
     'id': 'https://w3id.org/lmodel/cwe',
     'imports': ['linkml:types', './cwe_core', './cwe_entries'],
     'keywords': ['weakness',
                  'CWE',
                  'root cause mapping',
                  'software weakness',
                  'hardware weakness',
                  'secure coding'],
     'license': 'Apache-2.0',
     'name': 'cwe',
     'prefixes': {'cwe': {'prefix_prefix': 'cwe',
                          'prefix_reference': 'https://w3id.org/lmodel/cwe/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'wd': {'prefix_prefix': 'wd',
                         'prefix_reference': 'http://www.wikidata.org/entity/'}},
     'see_also': ['https://lmodel.github.io/cwe', 'https://cwe.mitre.org/'],
     'source': 'https://cwe.mitre.org/data/xsd/cwe_schema_v8.0.xsd',
     'source_file': 'src/cwe/schema/cwe.yaml',
     'title': 'Common Weakness Enumeration (CWE) List and Schema'} )

class CweAbstraction(str, Enum):
    """
    How far a weakness is described in general terms or tied to a specific product or resource.
    """
    Pillar = "Pillar"
    """
    The most general level, a theme that the weaknesses under it share.
    """
    Class = "Class"
    """
    A very general weakness, usually independent of any language or technology.
    """
    Base = "Base"
    """
    A weakness general enough to apply widely and detailed enough to find or prevent it.
    """
    Variant = "Variant"
    """
    A weakness tied to a particular language, technology or kind of product.
    """
    Compound = "Compound"
    """
    An entry that ties two or more weaknesses together, as a chain or a composite.
    """


class CweAlternateTermRole(str, Enum):
    """
    The part an alternate term plays when people talk about a weakness.
    """
    Abbreviation = "Abbreviation"
    Acronym = "Acronym"
    Alternate_Spelling = "Alternate-Spelling"
    Attack_Focused = "Attack-Focused"
    Impact_Oriented = "Impact-Oriented"
    Multi_Weakness = "Multi-Weakness"
    Multiple_Interpretation = "Multiple-Interpretation"
    Common_Name = "Common-Name"
    Discouraged = "Discouraged"
    Legacy = "Legacy"
    Other = "Other"


class CweArchitectureClass(str, Enum):
    """
    A broad family of hardware architectures.
    """
    Embedded = "Embedded"
    Microcomputer = "Microcomputer"
    Workstation = "Workstation"
    Not_Architecture_Specific = "Not Architecture-Specific"
    """
    The weakness can appear on many architectures.
    """


class CweArchitectureName(str, Enum):
    """
    A named hardware architecture.
    """
    Alpha = "Alpha"
    ARM = "ARM"
    Itanium = "Itanium"
    Power_Architecture = "Power Architecture"
    SPARC = "SPARC"
    x86 = "x86"
    Other = "Other"


class CweDetectionMethodName(str, Enum):
    """
    A way of finding a weakness.
    """
    Automated_Analysis = "Automated Analysis"
    Automated_Dynamic_Analysis = "Automated Dynamic Analysis"
    Automated_Static_Analysis = "Automated Static Analysis"
    Automated_Static_Analysis___Source_Code = "Automated Static Analysis - Source Code"
    Automated_Static_Analysis___Binary_or_Bytecode = "Automated Static Analysis - Binary or Bytecode"
    Fuzzing = "Fuzzing"
    Manual_Analysis = "Manual Analysis"
    Manual_Dynamic_Analysis = "Manual Dynamic Analysis"
    Manual_Static_Analysis = "Manual Static Analysis"
    Manual_Static_Analysis___Source_Code = "Manual Static Analysis - Source Code"
    Manual_Static_Analysis___Binary_or_Bytecode = "Manual Static Analysis - Binary or Bytecode"
    White_Box = "White Box"
    Black_Box = "Black Box"
    Architecture_or_Design_Review = "Architecture or Design Review"
    Dynamic_Analysis_with_Manual_Results_Interpretation = "Dynamic Analysis with Manual Results Interpretation"
    Dynamic_Analysis_with_Automated_Results_Interpretation = "Dynamic Analysis with Automated Results Interpretation"
    Formal_Verification = "Formal Verification"
    Simulation_SOLIDUS_Emulation = "Simulation / Emulation"
    Other = "Other"


class CweDetectionEffectiveness(str, Enum):
    """
    How well a detection method finds a weakness.
    """
    High = "High"
    """
    It finds the weakness often and with few false reports.
    """
    Moderate = "Moderate"
    """
    It works in several situations but misses some forms or gives some false reports.
    """
    SOAR_Partial = "SOAR Partial"
    """
    The State Of the Art Report rates it as cost-effective for part of the job.
    """
    Opportunistic = "Opportunistic"
    """
    It does not aim at this weakness and finds it only by the way.
    """
    Limited = "Limited"
    """
    It helps only in some situations.
    """
    None_ = "None"
    """
    It does not find the weakness.
    """


class CweEffectiveness(str, Enum):
    """
    How well a mitigation prevents a weakness.
    """
    High = "High"
    """
    It often removes the weakness altogether.
    """
    Moderate = "Moderate"
    """
    It prevents several forms of the weakness but does not cover them all.
    """
    Limited = "Limited"
    """
    It helps only in some situations or against some forms of the weakness.
    """
    Incidental = "Incidental"
    """
    It protects by chance and cannot be relied on.
    """
    Discouraged_Common_Practice = "Discouraged Common Practice"
    """
    A habit people often follow that does not work well enough to recommend.
    """
    Defense_in_Depth = "Defense in Depth"
    """
    It adds a layer of protection and does not remove the weakness by itself.
    """
    None_ = "None"
    """
    It does not prevent the weakness.
    """


class CweFunctionalArea(str, Enum):
    """
    The part of a product where a weakness is most likely to appear.
    """
    Authentication = "Authentication"
    Authorization = "Authorization"
    Code_Libraries = "Code Libraries"
    Counters = "Counters"
    Cryptography = "Cryptography"
    Error_Handling = "Error Handling"
    Interprocess_Communication = "Interprocess Communication"
    File_Processing = "File Processing"
    Logging = "Logging"
    Memory_Management = "Memory Management"
    Networking = "Networking"
    Number_Processing = "Number Processing"
    Program_Invocation = "Program Invocation"
    Protection_Mechanism = "Protection Mechanism"
    Session_Management = "Session Management"
    Signals = "Signals"
    String_Processing = "String Processing"
    Not_Functional_Area_Specific = "Not Functional-Area-Specific"
    Power = "Power"
    Clock = "Clock"


class CweImportance(str, Enum):
    """
    How much a change to an entry matters to people who already rely on it.
    """
    Normal = "Normal"
    Critical = "Critical"
    """
    The change alters what the entry means or how it may be read.
    """


class CweLanguageClass(str, Enum):
    """
    A broad family of programming languages.
    """
    Assembly = "Assembly"
    Compiled = "Compiled"
    Hardware_Description_Language = "Hardware Description Language"
    Interpreted = "Interpreted"
    Object_Oriented = "Object-Oriented"
    Memory_Unsafe = "Memory-Unsafe"
    Not_Language_Specific = "Not Language-Specific"
    """
    The weakness can appear in many languages.
    """


class CweLanguageName(str, Enum):
    """
    A named programming language or notation.
    """
    Ada = "Ada"
    Algorithm = "Algorithm"
    ARM_Assembly = "ARM Assembly"
    ASP = "ASP"
    ASPFULL_STOPNET = "ASP.NET"
    Basic = "Basic"
    C = "C"
    C_plus_plus = "C++"
    C_sharp = "C#"
    COBOL = "COBOL"
    Fortran = "Fortran"
    F_sharp = "F#"
    Go = "Go"
    HTML = "HTML"
    Java = "Java"
    JavaScript = "JavaScript"
    JSON = "JSON"
    JSP = "JSP"
    Objective_C = "Objective-C"
    Pascal = "Pascal"
    Perl = "Perl"
    PHP = "PHP"
    Pseudocode = "Pseudocode"
    Python = "Python"
    Ruby = "Ruby"
    Rust = "Rust"
    Shell = "Shell"
    SQL = "SQL"
    Swift = "Swift"
    SystemVerilog = "SystemVerilog"
    VBFULL_STOPNET = "VB.NET"
    Verilog = "Verilog"
    VHDL = "VHDL"
    XML = "XML"
    x86_Assembly = "x86 Assembly"
    Other = "Other"


class CweLikelihood(str, Enum):
    """
    How likely something is to happen.
    """
    High = "High"
    Medium = "Medium"
    Low = "Low"
    Unknown = "Unknown"
    """
    Nobody knows how likely it is.
    """


class CweMitigationStrategy(str, Enum):
    """
    A general approach that a mitigation follows.
    """
    Attack_Surface_Reduction = "Attack Surface Reduction"
    Compilation_or_Build_Hardening = "Compilation or Build Hardening"
    Enforcement_by_Conversion = "Enforcement by Conversion"
    Environment_Hardening = "Environment Hardening"
    Firewall = "Firewall"
    Input_Validation = "Input Validation"
    Language_Selection = "Language Selection"
    Libraries_or_Frameworks = "Libraries or Frameworks"
    Resource_Limitation = "Resource Limitation"
    Output_Encoding = "Output Encoding"
    Parameterization = "Parameterization"
    Refactoring = "Refactoring"
    Sandbox_or_Jail = "Sandbox or Jail"
    Separation_of_Privilege = "Separation of Privilege"


class CweNoteType(str, Enum):
    """
    What a note on an entry is about.
    """
    Applicable_Platform = "Applicable Platform"
    """
    More detail on the platforms the entry lists.
    """
    Maintenance = "Maintenance"
    """
    Work the entry still needs, such as sharper concepts or better relationships.
    """
    Relationship = "Relationship"
    """
    More detail on how the entry relates to others.
    """
    Research_Gap = "Research Gap"
    """
    A topic researchers have not yet explored enough.
    """
    Terminology = "Terminology"
    """
    A discussion of the words used for the weakness.
    """
    Theoretical = "Theoretical"
    """
    The weakness described in the terms of vulnerability theory.
    """
    Other = "Other"
    """
    Anything useful that fits no other type.
    """


class CweOrdinal(str, Enum):
    """
    Marks the relationship to prefer among several in one view.
    """
    Primary = "Primary"
    """
    The relationship to follow first in that view.
    """


class CweOrdinality(str, Enum):
    """
    How a weakness stands to other weaknesses in a sequence of causes.
    """
    Indirect = "Indirect"
    """
    A quality problem that makes other weaknesses easier to introduce or harder to find.
    """
    Primary = "Primary"
    """
    The weakness exists without depending on another one.
    """
    Resultant = "Resultant"
    """
    The weakness exists only because another one is present.
    """


class CweOperatingSystemClass(str, Enum):
    """
    A broad family of operating systems.
    """
    Linux = "Linux"
    macOS = "macOS"
    Unix = "Unix"
    Windows = "Windows"
    Not_OS_Specific = "Not OS-Specific"
    """
    The weakness can appear on many operating systems.
    """


class CweOperatingSystemName(str, Enum):
    """
    A named operating system.
    """
    AIX = "AIX"
    Android = "Android"
    BlackBerry_OS = "BlackBerry OS"
    Chrome_OS = "Chrome OS"
    Darwin = "Darwin"
    FreeBSD = "FreeBSD"
    iOS = "iOS"
    macOS = "macOS"
    NetBSD = "NetBSD"
    OpenBSD = "OpenBSD"
    Red_Hat = "Red Hat"
    Solaris = "Solaris"
    SUSE = "SUSE"
    tvOS = "tvOS"
    Ubuntu = "Ubuntu"
    watchOS = "watchOS"
    Windows_9x = "Windows 9x"
    Windows_Embedded = "Windows Embedded"
    Windows_NT = "Windows NT"
    Other = "Other"


class CwePhase(str, Enum):
    """
    A stage of a product life cycle.
    """
    Policy = "Policy"
    Requirements = "Requirements"
    Architecture_and_Design = "Architecture and Design"
    Implementation = "Implementation"
    Build_and_Compilation = "Build and Compilation"
    Testing = "Testing"
    Documentation = "Documentation"
    Bundling = "Bundling"
    Distribution = "Distribution"
    Installation = "Installation"
    System_Configuration = "System Configuration"
    Operation = "Operation"
    Patching_and_Maintenance = "Patching and Maintenance"
    Porting = "Porting"
    Integration = "Integration"
    Manufacturing = "Manufacturing"
    Decommissioning_and_End_of_Life = "Decommissioning and End-of-Life"


class CweAiPhase(str, Enum):
    """
    A stage of the life cycle of an artificial intelligence system.
    """
    Data_Collection = "Data Collection"
    Training = "Training"
    Fine_tuning = "Fine-tuning"
    Testing = "Testing"
    Tokenization = "Tokenization"
    Prompting = "Prompting"
    Output_Processing = "Output Processing"
    Component_Interaction = "Component Interaction"
    Re_training_SOLIDUS_Feedback = "Re-training / Feedback"


class CweHardwarePhase(str, Enum):
    """
    A stage of the life cycle of a hardware product.
    """
    Hardware_Requirements = "Hardware Requirements"
    Hardware_Architecture = "Hardware Architecture"
    Hardware_Microarchitecture = "Hardware Microarchitecture"
    Implementation_AMPERSAND_Physical_Design = "Implementation & Physical Design"
    Pre_Manufacturing_Verification = "Pre-Manufacturing Verification"
    Hardware_Manufacturing = "Hardware Manufacturing"
    Post_Manufacturing_Validation = "Post-Manufacturing Validation"
    Device_Configuration_AMPERSAND_Personalization = "Device Configuration & Personalization"
    Device_SOLIDUS_System_Integration = "Device / System Integration"
    Field_Operations_AMPERSAND_Sustainment = "Field Operations & Sustainment"
    Reuse = "Reuse"
    Decommissioning = "Decommissioning"


class CweCustomPhaseDomain(str, Enum):
    """
    The field whose own life cycle a custom phase belongs to.
    """
    AI = "AI"
    Hardware = "Hardware"


class CweDimensionType(str, Enum):
    """
    The aspect of a weakness that a dimension names, such as a behaviour or a resource.
    """
    Behavior_Type = "Behavior-Type"
    Behavior_Property = "Behavior-Property"
    Resource_Type = "Resource-Type"
    Resource_Property = "Resource-Property"
    Input_Type = "Input-Type"
    Input_Property = "Input-Property"
    Info_Type = "Info-Type"
    Info_Property = "Info-Property"
    Code_Type = "Code-Type"
    Code_Property = "Code-Property"
    Technology = "Technology"
    Language_Type = "Language-Type"
    Language_Property = "Language-Property"
    Framework = "Framework"
    Common_Name = "Common-Name"
    Attack = "Attack"
    Acronym = "Acronym"
    Other = "Other"


class CwePrevalence(str, Enum):
    """
    How regularly a weakness applies to a platform.
    """
    Often = "Often"
    Sometimes = "Sometimes"
    Rarely = "Rarely"
    Undetermined = "Undetermined"
    None_ = "None"


class CweReason(str, Enum):
    """
    A short label for why an entry may not suit vulnerability mapping.
    """
    Abstraction = "Abstraction"
    Category = "Category"
    Grouping = "Grouping"
    View = "View"
    Deprecated = "Deprecated"
    Potential_Deprecation = "Potential Deprecation"
    Frequent_Misuse = "Frequent Misuse"
    Frequent_Misinterpretation = "Frequent Misinterpretation"
    Multiple_Use = "Multiple Use"
    CWE_Overlap = "CWE Overlap"
    Acceptable_Use = "Acceptable-Use"
    Frequently_Resultant = "Frequently-Resultant"
    Potential_Major_Changes = "Potential Major Changes"
    Other = "Other"


class CweRelatedNature(str, Enum):
    """
    How one weakness relates to another.
    """
    ChildOf = "ChildOf"
    """
    The related weakness is more general than this one.
    """
    ParentOf = "ParentOf"
    """
    The related weakness is more specific than this one.
    """
    StartsWith = "StartsWith"
    """
    For a named chain only: the related weakness is where the chain begins.
    """
    CanFollow = "CanFollow"
    """
    In a chain, the related weakness can come before this one.
    """
    CanPrecede = "CanPrecede"
    """
    In a chain, the related weakness can come after this one.
    """
    RequiredBy = "RequiredBy"
    """
    For composites only: the related composite needs this weakness to be present.
    """
    Requires = "Requires"
    """
    For composites only: this composite needs the related weakness to be present.
    """
    CanAlsoBe = "CanAlsoBe"
    """
    In some settings this weakness may be seen as the related one, with neither being a parent of the other.
    """
    PeerOf = "PeerOf"
    """
    The two are similar in a way that no other nature fits.
    """
    Overlaps = "Overlaps"
    """
    The two weaknesses share some ground, which CWE would rather avoid.
    """


class CweResource(str, Enum):
    """
    A kind of system resource that exploiting a weakness can affect.
    """
    CPU = "CPU"
    File_or_Directory = "File or Directory"
    Memory = "Memory"
    System_Process = "System Process"
    Other = "Other"


class CweScope(str, Enum):
    """
    The security property a consequence violates.
    """
    Confidentiality = "Confidentiality"
    Integrity = "Integrity"
    Availability = "Availability"
    Access_Control = "Access Control"
    Accountability = "Accountability"
    Authentication = "Authentication"
    Authorization = "Authorization"
    Non_Repudiation = "Non-Repudiation"
    Other = "Other"


class CweStatus(str, Enum):
    """
    How far an entry has come in its life and how much it can be trusted.
    """
    Deprecated = "Deprecated"
    """
    Taken out of CWE, usually because it duplicated another entry or was made by mistake.
    """
    Draft = "Draft"
    """
    Its important elements are filled in and readable, though it may still have problems.
    """
    Incomplete = "Incomplete"
    """
    Some important elements are missing and its quality is not assured.
    """
    Obsolete = "Obsolete"
    """
    Still correct but no longer relevant, usually because a newer entry replaced it.
    """
    Stable = "Stable"
    """
    Its important elements have been checked and are not expected to change much.
    """
    Usable = "Usable"
    """
    It has had close review and its critical elements have been checked.
    """


class CweStakeholderType(str, Enum):
    """
    A group of people who may have a use for a view.
    """
    Academic_Researchers = "Academic Researchers"
    Applied_Researchers = "Applied Researchers"
    Assessment_Teams = "Assessment Teams"
    Assessment_Tool_Vendors = "Assessment Tool Vendors"
    CWE_Team = "CWE Team"
    Educators = "Educators"
    Hardware_Designers = "Hardware Designers"
    Information_Providers = "Information Providers"
    Product_Customers = "Product Customers"
    Product_Vendors = "Product Vendors"
    Software_Developers = "Software Developers"
    Vulnerability_Analysts = "Vulnerability Analysts"
    Other = "Other"


class CweStructure(str, Enum):
    """
    Whether a weakness stands alone or is made up of others.
    """
    Chain = "Chain"
    """
    Several weaknesses that must be reached one after another to give a vulnerability.
    """
    Composite = "Composite"
    """
    Several weaknesses that give a vulnerability only when they occur together.
    """
    Simple = "Simple"
    """
    One weakness whose exploitation does not depend on another.
    """


class CweCodeNature(str, Enum):
    """
    What a block of example code shows.
    """
    Attack = "Attack"
    """
    An attack against the code.
    """
    Bad = "Bad"
    """
    Code that has the weakness.
    """
    Good = "Good"
    """
    Code that avoids the weakness.
    """
    Informative = "Informative"
    """
    Background that shows neither good nor bad code.
    """
    Mitigation = "Mitigation"
    """
    A way of addressing the weakness.
    """
    Result = "Result"
    """
    What running the code produces.
    """


class CweMappingFit(str, Enum):
    """
    How closely a CWE entry matches an entry of another taxonomy.
    """
    Exact = "Exact"
    CWE_More_Abstract = "CWE More Abstract"
    """
    The CWE entry is more general than the other.
    """
    CWE_More_Specific = "CWE More Specific"
    """
    The CWE entry is narrower than the other.
    """
    Imprecise = "Imprecise"
    """
    The two match only loosely.
    """
    Perspective = "Perspective"
    """
    The two look at the same matter from different angles.
    """


class CweTaxonomyName(str, Enum):
    """
    A taxonomy that CWE entries are mapped to.
    """
    Seven_Pernicious_Kingdoms = "7 Pernicious Kingdoms"
    Nineteen_Deadly_Sins = "19 Deadly Sins"
    Aslam = "Aslam"
    Bishop = "Bishop"
    CERT_C_Secure_Coding = "CERT C Secure Coding"
    CERT_CPLUS_SIGNPLUS_SIGN_Secure_Coding = "CERT C++ Secure Coding"
    The_CERT_Oracle_Secure_Coding_Standard_for_Java_LEFT_PARENTHESIS2011RIGHT_PARENTHESIS = "The CERT Oracle Secure Coding Standard for Java (2011)"
    CLASP = "CLASP"
    ISASOLIDUSIEC_62443 = "ISA/IEC 62443"
    Landwehr = "Landwehr"
    OMG_ASCSM = "OMG ASCSM"
    OMG_ASCRM = "OMG ASCRM"
    OMG_ASCMM = "OMG ASCMM"
    OMG_ASCPEM = "OMG ASCPEM"
    OpenSSF_Secure_Coding_Guide_for_Python = "OpenSSF Secure Coding Guide for Python"
    OWASP_Golang_Secure_Coding_Practices_Guide = "OWASP Golang Secure Coding Practices Guide"
    OWASP_Top_Ten_2004 = "OWASP Top Ten 2004"
    OWASP_Top_Ten_2007 = "OWASP Top Ten 2007"
    OWASP_Top_Ten = "OWASP Top Ten"
    PLC_Top_20 = "PLC Top 20"
    PLOVER = "PLOVER"
    Protection_Analysis = "Protection Analysis"
    RISOS = "RISOS"
    SEI_CERT_C_Coding_Standard = "SEI CERT C Coding Standard"
    SEI_CERT_CPLUS_SIGNPLUS_SIGN_Coding_Standard = "SEI CERT C++ Coding Standard"
    SEI_CERT_Oracle_Coding_Standard_for_Java = "SEI CERT Oracle Coding Standard for Java"
    SEI_CERT_Perl_Coding_Standard = "SEI CERT Perl Coding Standard"
    Software_Fault_Patterns = "Software Fault Patterns"
    Weber_Karger_Paradkar = "Weber, Karger, Paradkar"
    WASC = "WASC"


class CweTechnicalImpact(str, Enum):
    """
    What an attacker can achieve by exploiting a weakness.
    """
    Modify_Memory = "Modify Memory"
    Read_Memory = "Read Memory"
    Modify_Files_or_Directories = "Modify Files or Directories"
    Read_Files_or_Directories = "Read Files or Directories"
    Modify_Application_Data = "Modify Application Data"
    Read_Application_Data = "Read Application Data"
    DoSCOLON_Crash_Exit_or_Restart = "DoS: Crash, Exit, or Restart"
    DoSCOLON_Amplification = "DoS: Amplification"
    DoSCOLON_Instability = "DoS: Instability"
    DoSCOLON_Prevent_Access = "DoS: Prevent Access"
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISCPURIGHT_PARENTHESIS = "DoS: Resource Consumption (CPU)"
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISMemoryRIGHT_PARENTHESIS = "DoS: Resource Consumption (Memory)"
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISOtherRIGHT_PARENTHESIS = "DoS: Resource Consumption (Other)"
    DoSCOLON_Other = "DoS: Other"
    Execute_Unauthorized_Code_or_Commands = "Execute Unauthorized Code or Commands"
    Gain_Privileges_or_Assume_Identity = "Gain Privileges or Assume Identity"
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism"
    Hide_Activities = "Hide Activities"
    Alter_Execution_Logic = "Alter Execution Logic"
    Undefined_Behavior = "Undefined Behavior"
    Quality_Degradation = "Quality Degradation"
    Unexpected_State = "Unexpected State"
    Varies_by_Context = "Varies by Context"
    Increase_Analytical_Complexity = "Increase Analytical Complexity"
    Reduce_Maintainability = "Reduce Maintainability"
    Reduce_Performance = "Reduce Performance"
    Reduce_Reliability = "Reduce Reliability"
    Other = "Other"


class CweTechnologyClass(str, Enum):
    """
    A broad family of technologies.
    """
    Client_Server = "Client Server"
    Cloud_Computing = "Cloud Computing"
    ICSSOLIDUSOT = "ICS/OT"
    Mainframe = "Mainframe"
    Mobile = "Mobile"
    N_Tier = "N-Tier"
    SOA = "SOA"
    System_on_Chip = "System on Chip"
    Web_Based = "Web Based"
    Not_Technology_Specific = "Not Technology-Specific"
    """
    The weakness can appear in many technologies.
    """


class CweTechnologyName(str, Enum):
    """
    A named technology.
    """
    AISOLIDUSML = "AI/ML"
    Web_Server = "Web Server"
    Database_Server = "Database Server"
    Accelerator_Hardware = "Accelerator Hardware"
    Analog_and_Mixed_Signal_Hardware = "Analog and Mixed Signal Hardware"
    AudioSOLIDUSVideo_Hardware = "Audio/Video Hardware"
    BusSOLIDUSInterface_Hardware = "Bus/Interface Hardware"
    ClockSOLIDUSCounter_Hardware = "Clock/Counter Hardware"
    Communication_Hardware = "Communication Hardware"
    Controller_Hardware = "Controller Hardware"
    Memory_Hardware = "Memory Hardware"
    Microcontroller_Hardware = "Microcontroller Hardware"
    Network_on_Chip_Hardware = "Network on Chip Hardware"
    Power_Management_Hardware = "Power Management Hardware"
    Processor_Hardware = "Processor Hardware"
    Security_Hardware = "Security Hardware"
    Sensor_Hardware = "Sensor Hardware"
    Storage_Hardware = "Storage Hardware"
    TestSOLIDUSDebug_Hardware = "Test/Debug Hardware"
    Other = "Other"


class CweUsage(str, Enum):
    """
    Whether an entry may be used when mapping a real vulnerability to its root cause.
    """
    Discouraged = "Discouraged"
    """
    It should not be used for mapping.
    """
    Prohibited = "Prohibited"
    """
    It must not be used for mapping.
    """
    Allowed = "Allowed"
    """
    It may be used for mapping.
    """
    Allowed_with_Review = "Allowed-with-Review"
    """
    It may be used for mapping only in limited situations and after careful review.
    """


class CweViewType(str, Enum):
    """
    How a view selects and arranges its entries.
    """
    Implicit = "Implicit"
    """
    A flat list that a filter selects.
    """
    Explicit = "Explicit"
    """
    A flat list whose members are named one by one.
    """
    Graph = "Graph"
    """
    A hierarchy of entries from one point of view.
    """


class CweObservedExampleRationale(str, Enum):
    """
    A hint at why an observed example was chosen for an entry.
    """
    Chain = "Chain"
    Early_Publication = "Early-Publication"
    """
    One of the earliest examples recognised as showing this weakness.
    """
    InfluentialSOLIDUSNewsworthy = "Influential/Newsworthy"
    """
    An example that drew attention or shaped how people see this weakness.
    """
    Language_Variety = "Language-Variety"
    Product_Variety = "Product-Variety"
    Attack_Surface = "Attack-Surface"
    Other = "Other"


class CweReferenceAccessRestriction(str, Enum):
    """
    What stands between a reader and a cited source.
    """
    None_ = "None"
    """
    Anybody on the internet can read it for free.
    """
    Proprietary_Subscription = "Proprietary-Subscription"
    """
    Only paying subscribers can read it.
    """
    Minimal_Registration = "Minimal-Registration"
    """
    A reader must register, at no cost, to read it.
    """
    Removed = "Removed"
    """
    It has been taken down and may have no other copy.
    """
    Other = "Other"


class CweReferenceMediaType(str, Enum):
    """
    The form a cited source takes, which affects how easily people can use it.
    """
    Text = "Text"
    """
    Plain text or a format that is easy to parse, as HTML with no scripts is.
    """
    Common_Proprietary_Text = "Common-Proprietary-Text"
    """
    A widely used proprietary format for text, such as PDF or a word processor file.
    """
    Video = "Video"
    """
    A recording with pictures, such as a conference talk.
    """
    Audio = "Audio"
    """
    A recording with sound and no pictures.
    """
    Other = "Other"
    """
    Some other format, which may be harder for some readers to use.
    """


class CweReferenceRationale(str, Enum):
    """
    A hint at why a source was cited.
    """
    Example = "Example"
    """
    It gives more detail on an example in the entry, and may be where the example came from.
    """
    Early_Publication = "Early-Publication"
    """
    One of the first publications to explain the weakness or how it is exploited.
    """
    InfluentialSOLIDUSNewsworthy = "Influential/Newsworthy"
    """
    A publication that drew attention or shaped how people see the weakness.
    """
    ManualSOLIDUSMan_Pages = "Manual/Man Pages"
    """
    Technical reference material that gives background and is not about the weakness itself.
    """
    Mitigation_Based = "Mitigation-Based"
    """
    It proposes ways to reduce or remove weaknesses across a whole system.
    """
    Secure_Development_Rules = "Secure-Development-Rules"
    """
    It points to formal rules or guides for developing securely.
    """
    Other = "Other"


class CweContributionType(str, Enum):
    """
    What a contribution to an entry consisted of.
    """
    Content = "Content"
    """
    Content given to the entry.
    """
    Feedback = "Feedback"
    """
    Feedback on the entry.
    """



class CweExternalReference(ConfiguredBaseModel):
    """
    A source that entries of the catalogue cite, such as a paper, a book or a web page.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExternalReferenceType'}},
         'close_mappings': ['sepses_cwe:Reference', 'capec:CapecExternalReference'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Reference_ID: str = Field(default=..., description="""The identifier entries use to cite this source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Author: Optional[list[str]] = Field(default=None, description="""A person or group who wrote the source.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:creator'],
         'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referenceAuthor']} })
    Title: str = Field(default=..., description="""The title of the source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referenceTitle', 'dcterms:title']} })
    Edition: Optional[str] = Field(default=None, description="""The edition of the source.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:bookEdition'],
         'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referenceEdition']} })
    Publication: Optional[str] = Field(default=None, description="""The journal, conference or other publication that holds the source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Publication_Year: Optional[str] = Field(default=None, description="""The year the source came out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referencePublicationYear']} })
    Publication_Month: Optional[str] = Field(default=None, description="""The month the source came out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referencePublicationMonth']} })
    Publication_Day: Optional[str] = Field(default=None, description="""The day of the month the source came out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referencePublicationDay']} })
    Publisher: Optional[str] = Field(default=None, description="""Who published the source.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:publisher'],
         'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referencePublisher']} })
    URL: Optional[str] = Field(default=None, description="""An address where the source can be read.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:url'],
         'comments': ['One entry of CWE 5.0, REF-1068, holds the word Original here, '
                      "which the XSD's anyURI admits."],
         'domain_of': ['CweExternalReference'],
         'exact_mappings': ['sepses_cwe:referenceUrl']} })
    URL_Date: Optional[date] = Field(default=None, description="""The date on which the address was last seen to work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Alt_URL: Optional[str] = Field(default=None, description="""Another address of the source, usually one with fewer restrictions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Alt_URL_Date: Optional[date] = Field(default=None, description="""The date on which the other address was last seen to work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Media_Type: Optional[list[CweReferenceMediaType]] = Field(default=None, description="""A form the source takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Access_Restrictions: Optional[CweReferenceAccessRestriction] = Field(default=None, description="""What stands between a reader and the source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference']} })
    Rationale: Optional[list[CweReferenceRationale]] = Field(default=None, description="""A hint at why the source was cited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference', 'CweObservedExample', 'CweMappingNotes']} })


class CweReference(ConfiguredBaseModel):
    """
    A citation of an external reference from an entry or from one of its parts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ReferencesType/Reference'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    External_Reference_ID: str = Field(default=..., description="""The external reference being cited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweReference']} })
    Section: Optional[str] = Field(default=None, description="""The section or page of the source that this citation means.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweReference']} })


class CweDimension(ConfiguredBaseModel):
    """
    One aspect of a weakness, or of how two weaknesses differ, named in a word or two.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'DimensionElementType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Type: CweDimensionType = Field(default=..., description="""The kind of aspect, such as a behaviour or a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })
    Value: str = Field(default=..., description="""The aspect itself, such as Generation or Page.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_text_of': {'tag': 'xsd_text_of', 'value': 'xs:string'}},
         'domain_of': ['CweDimension',
                       'CweCustomPhase',
                       'CweNote',
                       'CwePreviousEntryName',
                       'CweExampleCode']} })


class CweCustomPhase(ConfiguredBaseModel):
    """
    A life cycle stage from a field whose stages differ from those of software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'CustomPhaseType'}},
         'comments': ['XML Schema cannot tie the value to the domain, as a comment in '
                      'the XSD regrets, so the XSD takes either list under either '
                      'domain. The rules below state what it means, and '
                      'tests/test_schema_rules.py holds their lists to the two enums.'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core',
         'rules': [{'description': 'A stage in the AI domain comes from the AI list.',
                    'postconditions': {'slot_conditions': {'Value': {'equals_string_in': ['Data '
                                                                                          'Collection',
                                                                                          'Training',
                                                                                          'Fine-tuning',
                                                                                          'Testing',
                                                                                          'Tokenization',
                                                                                          'Prompting',
                                                                                          'Output '
                                                                                          'Processing',
                                                                                          'Component '
                                                                                          'Interaction',
                                                                                          'Re-training '
                                                                                          '/ '
                                                                                          'Feedback'],
                                                                     'name': 'Value'}}},
                    'preconditions': {'slot_conditions': {'Domain': {'equals_string': 'AI',
                                                                     'name': 'Domain'}}}},
                   {'description': 'A stage in the Hardware domain comes from the '
                                   'hardware list.',
                    'postconditions': {'slot_conditions': {'Value': {'equals_string_in': ['Hardware '
                                                                                          'Requirements',
                                                                                          'Hardware '
                                                                                          'Architecture',
                                                                                          'Hardware '
                                                                                          'Microarchitecture',
                                                                                          'Implementation '
                                                                                          '& '
                                                                                          'Physical '
                                                                                          'Design',
                                                                                          'Pre-Manufacturing '
                                                                                          'Verification',
                                                                                          'Hardware '
                                                                                          'Manufacturing',
                                                                                          'Post-Manufacturing '
                                                                                          'Validation',
                                                                                          'Device '
                                                                                          'Configuration '
                                                                                          '& '
                                                                                          'Personalization',
                                                                                          'Device '
                                                                                          '/ '
                                                                                          'System '
                                                                                          'Integration',
                                                                                          'Field '
                                                                                          'Operations '
                                                                                          '& '
                                                                                          'Sustainment',
                                                                                          'Reuse',
                                                                                          'Decommissioning'],
                                                                     'name': 'Value'}}},
                    'preconditions': {'slot_conditions': {'Domain': {'equals_string': 'Hardware',
                                                                     'name': 'Domain'}}}}]})

    Domain: CweCustomPhaseDomain = Field(default=..., description="""The field whose life cycle the stage belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweCustomPhase']} })
    Value: Union[CweAiPhase, CweHardwarePhase] = Field(default=..., description="""The stage.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_text_of': {'tag': 'xsd_text_of',
                                         'value': 'CustomPhaseEnumeration'}},
         'any_of': [{'range': 'CweAiPhase'}, {'range': 'CweHardwarePhase'}],
         'domain_of': ['CweDimension',
                       'CweCustomPhase',
                       'CweNote',
                       'CwePreviousEntryName',
                       'CweExampleCode']} })


class CweNote(ConfiguredBaseModel):
    """
    A remark on an entry that fits nowhere else.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'NotesType/Note'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Type: CweNoteType = Field(default=..., description="""What the note is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })
    Version: Optional[str] = Field(default=None, description="""The CWE version the note belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweNote',
                       'CwePreviousEntryName',
                       'CweOperatingSystemPlatform',
                       'CweWeaknessCatalog']} })
    ReleaseDate: Optional[date] = Field(default=None, description="""The release date of that version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweNote']} })
    Value: Optional[str] = Field(default=None, description="""The text of the note.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_text_of': {'tag': 'xsd_text_of',
                                         'value': 'StructuredTextType'}},
         'domain_of': ['CweDimension',
                       'CweCustomPhase',
                       'CweNote',
                       'CwePreviousEntryName',
                       'CweExampleCode']} })


class CweTaxonomyMapping(ConfiguredBaseModel):
    """
    A link from an entry to an entry of another taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TaxonomyMappingsType/Taxonomy_Mapping'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Taxonomy_Name: CweTaxonomyName = Field(default=..., description="""The other taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweTaxonomyMapping']} })
    Entry_ID: Optional[str] = Field(default=None, description="""The identifier of the entry in the other taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweTaxonomyMapping']} })
    Entry_Name: Optional[str] = Field(default=None, description="""The name of the entry in the other taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweTaxonomyMapping']} })
    Mapping_Fit: Optional[CweMappingFit] = Field(default=None, description="""How closely the two entries match.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweTaxonomyMapping']} })


class CweContentHistory(ConfiguredBaseModel):
    """
    The record of who wrote an entry and how it has changed since.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Submission: list[CweSubmission] = Field(default=..., description="""The original submission of the entry, or each of several.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasSubmissionHistory'],
         'domain_of': ['CweContentHistory']} })
    Modification: Optional[list[CweModification]] = Field(default=None, description="""A change made to the entry.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasModificationHistory', 'skos:changeNote'],
         'domain_of': ['CweContentHistory']} })
    Contribution: Optional[list[CweContribution]] = Field(default=None, description="""Feedback or content that someone gave to the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContentHistory']} })
    Previous_Entry_Name: Optional[list[CwePreviousEntryName]] = Field(default=None, description="""A name the entry used to have.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContentHistory']} })


class CweSubmission(ConfiguredBaseModel):
    """
    Who first submitted an entry, and when it joined the list.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Submission'}},
         'any_of': [{'slot_conditions': {'Submission_Name': {'name': 'Submission_Name',
                                                             'required': True}}},
                    {'slot_conditions': {'Submission_Organization': {'name': 'Submission_Organization',
                                                                     'required': True}}}],
         'close_mappings': ['sepses_cwe:SubmissionHistory'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Submission_Name: Optional[list[str]] = Field(default=None, description="""A person or group who submitted the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission'],
         'exact_mappings': ['sepses_cwe:submissionName']} })
    Submission_Organization: Optional[str] = Field(default=None, description="""The organization the submitter belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission'],
         'exact_mappings': ['sepses_cwe:submissionOrganization']} })
    Submission_Date: date = Field(default=..., description="""The date of the submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission'],
         'exact_mappings': ['sepses_cwe:submissionDate']} })
    Submission_Version: str = Field(default=..., description="""The first CWE version that held the submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission']} })
    Submission_ReleaseDate: date = Field(default=..., description="""The release date of that version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission']} })
    Submission_Comment: Optional[str] = Field(default=None, description="""A remark on the submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweSubmission']} })


class CweModification(ConfiguredBaseModel):
    """
    One change made to an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Modification'}},
         'close_mappings': ['sepses_cwe:ModificationHistory'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Modification_Name: Optional[str] = Field(default=None, description="""The person who made or suggested the change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification'],
         'exact_mappings': ['sepses_cwe:modificationName']} })
    Modification_Organization: Optional[str] = Field(default=None, description="""The organization that person belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification'],
         'exact_mappings': ['sepses_cwe:modificationOrganization']} })
    Modification_Date: date = Field(default=..., description="""The date of the change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification'],
         'exact_mappings': ['sepses_cwe:modificationDate']} })
    Modification_Version: str = Field(default=..., description="""The first CWE version that held the change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification']} })
    Modification_ReleaseDate: date = Field(default=..., description="""The release date of that version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification']} })
    Modification_Importance: Optional[CweImportance] = Field(default=None, description="""How much the change matters to people who rely on the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification']} })
    Modification_Comment: str = Field(default=..., description="""What changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweModification'],
         'exact_mappings': ['sepses_cwe:modificationComment']} })


class CweContribution(ConfiguredBaseModel):
    """
    Feedback or content that someone gave to an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Contribution'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Type: CweContributionType = Field(default=..., description="""Whether the contribution was feedback or content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })
    Contribution_Name: Optional[list[str]] = Field(default=None, description="""A person or group who contributed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })
    Contribution_Organization: Optional[str] = Field(default=None, description="""The organization the contributor belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })
    Contribution_Date: date = Field(default=..., description="""The date of the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })
    Contribution_Version: str = Field(default=..., description="""The first CWE version that held the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })
    Contribution_ReleaseDate: date = Field(default=..., description="""The release date of that version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })
    Contribution_Comment: Optional[str] = Field(default=None, description="""A remark on the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweContribution']} })


class CwePreviousEntryName(ConfiguredBaseModel):
    """
    A name an entry had before.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Previous_Entry_Name'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_core'})

    Date: date = Field(default=..., description="""The date the name stopped being used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CwePreviousEntryName', 'CweWeaknessCatalog']} })
    Version: Optional[str] = Field(default=None, description="""The CWE version in which the name changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweNote',
                       'CwePreviousEntryName',
                       'CweOperatingSystemPlatform',
                       'CweWeaknessCatalog']} })
    Value: str = Field(default=..., description="""The earlier name.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_text_of': {'tag': 'xsd_text_of', 'value': 'xs:string'}},
         'domain_of': ['CweDimension',
                       'CweCustomPhase',
                       'CweNote',
                       'CwePreviousEntryName',
                       'CweExampleCode']} })


class CweEntry(ConfiguredBaseModel):
    """
    Any item of the CWE List that has an identifier of its own: a weakness, a grouping or a view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'WeaknessType GroupingType ViewType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries',
         'see_also': ['https://cwe.mitre.org/documents/glossary/index.html#Entry']})

    ID: str = Field(default=..., description="""The number that identifies the entry across the whole list.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['wdt:P3624', 'schema:termCode'],
         'comments': ["Wikidata's P3624 holds this number for a weakness, without the "
                      "CWE- prefix. lmodel/cve's cweId and lmodel/kev-catalog's cwes "
                      'write the same number with the prefix, as CWE-79, so they are '
                      'related.'],
         'domain_of': ['CweEntry'],
         'related_mappings': ['cve:cweId', 'kev_catalog:cwes']} })
    Name: str = Field(default=..., description="""The name of the entry.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name', 'skos:prefLabel'],
         'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Status: CweStatus = Field(default=..., description="""How far the entry has come and how much it can be trusted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry'], 'exact_mappings': ['sepses_cwe:status']} })
    References: Optional[list[CweReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasReference'], 'domain_of': ['CweEntry']} })
    Mapping_Notes: CweMappingNotes = Field(default=..., description="""Guidance on whether to map a real vulnerability to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })
    Notes: Optional[list[CweNote]] = Field(default=None, description="""Remarks on the entry that fit nowhere else.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:note'], 'domain_of': ['CweEntry']} })
    Content_History: CweContentHistory = Field(default=..., description="""Who wrote the entry and how it has changed since.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })


class CweWeakness(CweEntry):
    """
    A type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'WeaknessType'}},
         'close_mappings': ['sepses_cwe:CWE', 'schema:DefinedTerm', 'skos:Concept'],
         'comments': ['The SPDX external reference type names a weakness as a target '
                      'of a link, and an NVD weakness names one as the cause of a '
                      'vulnerability, so both are related.'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries',
         'related_mappings': ['spdx_core:ExternalRefType/cwe', 'nist_nvd:NvdWeakness'],
         'rules': [{'description': 'A compound weakness is a chain or a composite.',
                    'postconditions': {'slot_conditions': {'Structure': {'name': 'Structure',
                                                                         'none_of': [{'equals_string': 'Simple'}]}}},
                    'preconditions': {'slot_conditions': {'Abstraction': {'equals_string': 'Compound',
                                                                          'name': 'Abstraction'}}}},
                   {'description': 'A chain is a compound weakness.',
                    'postconditions': {'slot_conditions': {'Abstraction': {'equals_string': 'Compound',
                                                                           'name': 'Abstraction'}}},
                    'preconditions': {'slot_conditions': {'Structure': {'equals_string': 'Chain',
                                                                        'name': 'Structure'}}}},
                   {'description': 'A composite is a compound weakness.',
                    'postconditions': {'slot_conditions': {'Abstraction': {'equals_string': 'Compound',
                                                                           'name': 'Abstraction'}}},
                    'preconditions': {'slot_conditions': {'Structure': {'equals_string': 'Composite',
                                                                        'name': 'Structure'}}}}],
         'see_also': ['https://cwe.mitre.org/documents/glossary/index.html#Weakness']})

    Abstraction: CweAbstraction = Field(default=..., description="""How far the weakness is described in general terms or tied to a specific product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness'], 'exact_mappings': ['sepses_cwe:abstraction']} })
    Structure: CweStructure = Field(default=..., description="""Whether the weakness stands alone or is made up of others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness'], 'exact_mappings': ['sepses_cwe:structure']} })
    Diagram: Optional[str] = Field(default=None, description="""The path on MITRE's site of a diagram of the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Description: str = Field(default=..., description="""A sentence or two that define the weakness.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description',
                            'schema:description',
                            'skos:definition'],
         'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder']} })
    Extended_Description: Optional[str] = Field(default=None, description="""More about the weakness than its short description gives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness'],
         'exact_mappings': ['sepses_cwe:extendedDescription']} })
    Technical_Nuance: Optional[str] = Field(default=None, description="""Finer technical detail that helps tell this weakness from close relatives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Dimensions: Optional[list[CweDimension]] = Field(default=None, description="""The aspects of the weakness that this entry centres on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness', 'CweRelatedWeakness', 'CweMember']} })
    Related_Weaknesses: Optional[list[CweRelatedWeakness]] = Field(default=None, description="""How this weakness relates to others in the list.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasRelatedWeakness'],
         'domain_of': ['CweWeakness'],
         'related_mappings': ['skos:semanticRelation']} })
    Weakness_Ordinalities: Optional[list[CweWeaknessOrdinality]] = Field(default=None, description="""Whether the weakness tends to be a first cause or the result of another.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Applicable_Platforms: Optional[CweApplicablePlatforms] = Field(default=None, description="""The languages, systems, architectures and technologies where the weakness can appear.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasApplicablePlatform'],
         'domain_of': ['CweWeakness']} })
    Background_Details: Optional[list[str]] = Field(default=None, description="""Background that helps a reader but does not describe the weakness itself.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:backgroundDetail'],
         'domain_of': ['CweWeakness']} })
    Alternate_Terms: Optional[list[CweAlternateTerm]] = Field(default=None, description="""Other names people use for the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Modes_Of_Introduction: Optional[list[CweIntroduction]] = Field(default=None, description="""How and when the weakness can get into a product.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasModeOfIntroduction'],
         'domain_of': ['CweWeakness']} })
    Exploitation_Factors: Optional[list[str]] = Field(default=None, description="""Conditions that make exploiting the weakness more likely.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Likelihood_Of_Exploit: Optional[CweLikelihood] = Field(default=None, description="""How likely it is that the weakness gets exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness'],
         'exact_mappings': ['sepses_cwe:likelihoodOfExploit']} })
    Common_Consequences: Optional[list[CweConsequence]] = Field(default=None, description="""What can follow when the weakness is exploited.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasCommonConsequence'],
         'domain_of': ['CweWeakness']} })
    Detection_Methods: Optional[list[CweDetectionMethod]] = Field(default=None, description="""Ways of finding the weakness, with what each is good for.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasDetectionMethod'],
         'domain_of': ['CweWeakness']} })
    Potential_Mitigations: Optional[list[CweMitigation]] = Field(default=None, description="""Ways of preventing the weakness or reducing what it can do.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasPotentialMitigation'],
         'domain_of': ['CweWeakness']} })
    Demonstrative_Examples: Optional[list[CweDemonstrativeExample]] = Field(default=None, description="""Worked examples of how the weakness looks in code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Observed_Examples: Optional[list[CweObservedExample]] = Field(default=None, description="""Real cases of the weakness, usually CVE records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Functional_Areas: Optional[list[CweFunctionalArea]] = Field(default=None, description="""The parts of a product where the weakness tends to appear.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Affected_Resources: Optional[list[CweResource]] = Field(default=None, description="""The system resources that exploiting the weakness can affect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness']} })
    Taxonomy_Mappings: Optional[list[CweTaxonomyMapping]] = Field(default=None, description="""Links to entries of other taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness', 'CweGrouping']} })
    Related_Attack_Patterns: Optional[list[CweRelatedAttackPattern]] = Field(default=None, description="""Attack patterns that may apply where the weakness is present.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasCAPEC'], 'domain_of': ['CweWeakness']} })
    ID: str = Field(default=..., description="""The number that identifies the entry across the whole list.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['wdt:P3624', 'schema:termCode'],
         'comments': ["Wikidata's P3624 holds this number for a weakness, without the "
                      "CWE- prefix. lmodel/cve's cweId and lmodel/kev-catalog's cwes "
                      'write the same number with the prefix, as CWE-79, so they are '
                      'related.'],
         'domain_of': ['CweEntry'],
         'related_mappings': ['cve:cweId', 'kev_catalog:cwes']} })
    Name: str = Field(default=..., description="""The name of the entry.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name', 'skos:prefLabel'],
         'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Status: CweStatus = Field(default=..., description="""How far the entry has come and how much it can be trusted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry'], 'exact_mappings': ['sepses_cwe:status']} })
    References: Optional[list[CweReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasReference'], 'domain_of': ['CweEntry']} })
    Mapping_Notes: CweMappingNotes = Field(default=..., description="""Guidance on whether to map a real vulnerability to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })
    Notes: Optional[list[CweNote]] = Field(default=None, description="""Remarks on the entry that fit nowhere else.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:note'], 'domain_of': ['CweEntry']} })
    Content_History: CweContentHistory = Field(default=..., description="""Who wrote the entry and how it has changed since.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })


class CweGrouping(CweEntry):
    """
    A set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'GroupingType'}},
         'close_mappings': ['skos:Collection'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Summary: str = Field(default=..., description="""What the grouped weaknesses have in common.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description'], 'domain_of': ['CweGrouping']} })
    Relationships: Optional[CweRelationships] = Field(default=None, description="""The entries this grouping holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweGrouping']} })
    Taxonomy_Mappings: Optional[list[CweTaxonomyMapping]] = Field(default=None, description="""Links to entries of other taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness', 'CweGrouping']} })
    ID: str = Field(default=..., description="""The number that identifies the entry across the whole list.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['wdt:P3624', 'schema:termCode'],
         'comments': ["Wikidata's P3624 holds this number for a weakness, without the "
                      "CWE- prefix. lmodel/cve's cweId and lmodel/kev-catalog's cwes "
                      'write the same number with the prefix, as CWE-79, so they are '
                      'related.'],
         'domain_of': ['CweEntry'],
         'related_mappings': ['cve:cweId', 'kev_catalog:cwes']} })
    Name: str = Field(default=..., description="""The name of the entry.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name', 'skos:prefLabel'],
         'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Status: CweStatus = Field(default=..., description="""How far the entry has come and how much it can be trusted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry'], 'exact_mappings': ['sepses_cwe:status']} })
    References: Optional[list[CweReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasReference'], 'domain_of': ['CweEntry']} })
    Mapping_Notes: CweMappingNotes = Field(default=..., description="""Guidance on whether to map a real vulnerability to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })
    Notes: Optional[list[CweNote]] = Field(default=None, description="""Remarks on the entry that fit nowhere else.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:note'], 'domain_of': ['CweEntry']} })
    Content_History: CweContentHistory = Field(default=..., description="""Who wrote the entry and how it has changed since.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })


class CweView(CweEntry):
    """
    A way of looking at the catalogue, as a subset of its entries seen from one standpoint.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'ViewType'}},
         'comments': ['A graph view arranges concepts as a scheme does, but a slice is '
                      'a flat list, so the SKOS concept scheme is only related.'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries',
         'related_mappings': ['skos:ConceptScheme'],
         'see_also': ['https://cwe.mitre.org/documents/glossary/index.html#View']})

    Type: CweViewType = Field(default=..., description="""How the view selects and arranges its entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })
    Objective: str = Field(default=..., description="""What the view is for.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description'], 'domain_of': ['CweView']} })
    Audience: Optional[list[CweStakeholder]] = Field(default=None, description="""The people who may find the view useful, and why.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweView']} })
    Members: Optional[CweRelationships] = Field(default=None, description="""The entries a view names one by one, when it is not selected by a filter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweView']} })
    Filter: Optional[str] = Field(default=None, description="""The XPath expression that selects the entries of an implicit slice.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweView']} })
    ID: str = Field(default=..., description="""The number that identifies the entry across the whole list.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['wdt:P3624', 'schema:termCode'],
         'comments': ["Wikidata's P3624 holds this number for a weakness, without the "
                      "CWE- prefix. lmodel/cve's cweId and lmodel/kev-catalog's cwes "
                      'write the same number with the prefix, as CWE-79, so they are '
                      'related.'],
         'domain_of': ['CweEntry'],
         'related_mappings': ['cve:cweId', 'kev_catalog:cwes']} })
    Name: str = Field(default=..., description="""The name of the entry.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name', 'skos:prefLabel'],
         'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Status: CweStatus = Field(default=..., description="""How far the entry has come and how much it can be trusted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry'], 'exact_mappings': ['sepses_cwe:status']} })
    References: Optional[list[CweReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:hasReference'], 'domain_of': ['CweEntry']} })
    Mapping_Notes: CweMappingNotes = Field(default=..., description="""Guidance on whether to map a real vulnerability to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })
    Notes: Optional[list[CweNote]] = Field(default=None, description="""Remarks on the entry that fit nowhere else.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:note'], 'domain_of': ['CweEntry']} })
    Content_History: CweContentHistory = Field(default=..., description="""Who wrote the entry and how it has changed since.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry']} })


class CweRelatedWeakness(ConfiguredBaseModel):
    """
    A link from a weakness to another weakness, in one view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedWeaknessesType/Related_Weakness'}},
         'close_mappings': ['sepses_cwe:RelatedWeakness'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Nature: CweRelatedNature = Field(default=..., description="""How the two weaknesses relate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweExampleCode'],
         'exact_mappings': ['sepses_cwe:relatedWeaknessNature']} })
    CWE_ID: str = Field(default=..., description="""The weakness at the other end of the link.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweMember', 'CweMappingSuggestion'],
         'exact_mappings': ['sepses_cwe:relatedCWE']} })
    View_ID: str = Field(default=..., description="""The view in which the link holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweMember'],
         'exact_mappings': ['sepses_cwe:relatedWeaknessViewId']} })
    Chain_ID: Optional[str] = Field(default=None, description="""The named chain that the link belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness']} })
    Ordinal: Optional[CweOrdinal] = Field(default=None, description="""Marks this as the link to prefer in the view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness'],
         'exact_mappings': ['sepses_cwe:relatedWeaknessOrdinal']} })
    Dimensions: Optional[list[CweDimension]] = Field(default=None, description="""The aspects in which the two weaknesses differ.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness', 'CweRelatedWeakness', 'CweMember']} })

    @field_validator('CWE_ID')
    def pattern_CWE_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CWE_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CWE_ID format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('View_ID')
    def pattern_View_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid View_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid View_ID format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('Chain_ID')
    def pattern_Chain_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid Chain_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid Chain_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CweWeaknessOrdinality(ConfiguredBaseModel):
    """
    Whether a weakness tends to be a first cause or the result of another.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'WeaknessOrdinalitiesType/Weakness_Ordinality'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Ordinality: CweOrdinality = Field(default=..., description="""The position in the sequence of causes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeaknessOrdinality'],
         'exact_mappings': ['sepses_cwe:weaknessOrdinality']} })
    Description: Optional[str] = Field(default=None, description="""The setting in which the weakness takes this position.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder']} })


class CweApplicablePlatforms(ConfiguredBaseModel):
    """
    The kinds of platform where a weakness can appear.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ApplicablePlatformsType'}},
         'close_mappings': ['sepses_cwe:ApplicablePlatform'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Language: Optional[list[CweLanguagePlatform]] = Field(default=None, description="""A programming language, or a family of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweApplicablePlatforms', 'CweExampleCode']} })
    Operating_System: Optional[list[CweOperatingSystemPlatform]] = Field(default=None, description="""An operating system, or a family of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweApplicablePlatforms']} })
    Architecture: Optional[list[CweArchitecturePlatform]] = Field(default=None, description="""A hardware architecture, or a family of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweApplicablePlatforms']} })
    Technology: Optional[list[CweTechnologyPlatform]] = Field(default=None, description="""A technology, or a family of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweApplicablePlatforms']} })


class CweLanguagePlatform(ConfiguredBaseModel):
    """
    A language where a weakness can appear, named or by its family.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ApplicablePlatformsType/Language'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Name: Optional[CweLanguageName] = Field(default=None, description="""The name of the language.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Class: Optional[CweLanguageClass] = Field(default=None, description="""The family of languages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Prevalence: CwePrevalence = Field(default=..., description="""How regularly the weakness applies here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Note: Optional[str] = Field(default=None, description="""A remark on this platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweOperatingSystemPlatform(ConfiguredBaseModel):
    """
    An operating system where a weakness can appear, named or by its family.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ApplicablePlatformsType/Operating_System'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Name: Optional[CweOperatingSystemName] = Field(default=None, description="""The name of the operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Version: Optional[str] = Field(default=None, description="""The version of the operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweNote',
                       'CwePreviousEntryName',
                       'CweOperatingSystemPlatform',
                       'CweWeaknessCatalog']} })
    CPE_ID: Optional[str] = Field(default=None, description="""The Common Platform Enumeration name of the operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweOperatingSystemPlatform']} })
    Class: Optional[CweOperatingSystemClass] = Field(default=None, description="""The family of operating systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Prevalence: CwePrevalence = Field(default=..., description="""How regularly the weakness applies here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Note: Optional[str] = Field(default=None, description="""A remark on this platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweArchitecturePlatform(ConfiguredBaseModel):
    """
    A hardware architecture where a weakness can appear, named or by its family.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ApplicablePlatformsType/Architecture'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Name: Optional[CweArchitectureName] = Field(default=None, description="""The name of the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Class: Optional[CweArchitectureClass] = Field(default=None, description="""The family of architectures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Prevalence: CwePrevalence = Field(default=..., description="""How regularly the weakness applies here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Note: Optional[str] = Field(default=None, description="""A remark on this platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweTechnologyPlatform(ConfiguredBaseModel):
    """
    A technology where a weakness can appear, named or by its family.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ApplicablePlatformsType/Technology'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Name: Optional[CweTechnologyName] = Field(default=None, description="""The name of the technology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Class: Optional[CweTechnologyClass] = Field(default=None, description="""The family of technologies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Prevalence: CwePrevalence = Field(default=..., description="""How regularly the weakness applies here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform']} })
    Note: Optional[str] = Field(default=None, description="""A remark on this platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweAlternateTerm(ConfiguredBaseModel):
    """
    Another name people use for a weakness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AlternateTermsType/Alternate_Term'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Term: str = Field(default=..., description="""The name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:altLabel'], 'domain_of': ['CweAlternateTerm']} })
    Role: Optional[list[CweAlternateTermRole]] = Field(default=None, description="""The part the name plays when people talk about the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweAlternateTerm']} })
    Description: Optional[str] = Field(default=None, description="""When and how the name is used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder']} })


class CweIntroduction(ConfiguredBaseModel):
    """
    One way a weakness can get into a product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ModesOfIntroductionType/Introduction'}},
         'close_mappings': ['sepses_cwe:ModeOfIntroduction'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Phase: Optional[list[CwePhase]] = Field(default=None, description="""A life cycle stage where the weakness can get in.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:modeOfIntroductionPhase'],
         'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Custom_Phase: Optional[list[CweCustomPhase]] = Field(default=None, description="""A stage from the life cycle of a field such as hardware or AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Note: Optional[str] = Field(default=None, description="""The usual way this happens.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:modeOfIntroductionNote'],
         'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweConsequence(ConfiguredBaseModel):
    """
    One thing that can follow when a weakness is exploited.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'CommonConsequencesType/Consequence'}},
         'close_mappings': ['sepses_cwe:CommonConsequence'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Consequence_ID: Optional[str] = Field(default=None, description="""An identifier for this consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweConsequence']} })
    Scope: list[CweScope] = Field(default=..., description="""A security property the consequence violates.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:consequenceScope'],
         'domain_of': ['CweConsequence']} })
    Impact: list[CweTechnicalImpact] = Field(default=..., description="""What an attacker can achieve.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:consequenceImpact'],
         'domain_of': ['CweConsequence']} })
    Likelihood: Optional[CweLikelihood] = Field(default=None, description="""How likely this consequence is beside the others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweConsequence']} })
    Note: Optional[str] = Field(default=None, description="""A remark on the consequence.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:consequenceNote'],
         'domain_of': ['CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweIntroduction',
                       'CweConsequence']} })


class CweDetectionMethod(ConfiguredBaseModel):
    """
    One way of finding a weakness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'DetectionMethodsType/Detection_Method'}},
         'close_mappings': ['sepses_cwe:DetectionMethod'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Detection_Method_ID: Optional[str] = Field(default=None, description="""An identifier that lets entries share this text, such as DM-14.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod']} })
    Method: CweDetectionMethodName = Field(default=..., description="""The way of finding the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod'],
         'exact_mappings': ['sepses_cwe:detectionMethod']} })
    Phase: Optional[list[CwePhase]] = Field(default=None, description="""A life cycle stage where the method applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Custom_Phase: Optional[list[CweCustomPhase]] = Field(default=None, description="""A stage from the life cycle of a field such as hardware or AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Description: str = Field(default=..., description="""How the method applies to this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder'],
         'exact_mappings': ['sepses_cwe:detectionDescription']} })
    Effectiveness: Optional[CweDetectionEffectiveness] = Field(default=None, description="""How well the method finds the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod', 'CweMitigation'],
         'exact_mappings': ['sepses_cwe:detectionEffectiveness']} })
    Effectiveness_Notes: Optional[str] = Field(default=None, description="""The strengths and limits of the method here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod', 'CweMitigation'],
         'exact_mappings': ['sepses_cwe:detectionEffectivenessNote']} })


class CweMitigation(ConfiguredBaseModel):
    """
    One way of preventing a weakness or reducing what it can do.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'PotentialMitigationsType/Mitigation'}},
         'close_mappings': ['sepses_cwe:PotentialMitigation'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Mitigation_ID: Optional[str] = Field(default=None, description="""An identifier that lets entries share this text, such as MIT-5.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMitigation']} })
    Phase: Optional[list[CwePhase]] = Field(default=None, description="""A life cycle stage where the mitigation applies.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cwe:mitigationPhase'],
         'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Custom_Phase: Optional[list[CweCustomPhase]] = Field(default=None, description="""A stage from the life cycle of a field such as hardware or AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweIntroduction', 'CweDetectionMethod', 'CweMitigation']} })
    Strategy: Optional[CweMitigationStrategy] = Field(default=None, description="""The general approach the mitigation follows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMitigation']} })
    Description: str = Field(default=..., description="""What to do, with its strengths and limits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder'],
         'exact_mappings': ['sepses_cwe:mitigationDescription']} })
    Effectiveness: Optional[CweEffectiveness] = Field(default=None, description="""How well the mitigation prevents the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod', 'CweMitigation'],
         'exact_mappings': ['sepses_cwe:mitigationEffectiveness']} })
    Effectiveness_Notes: Optional[str] = Field(default=None, description="""The strengths and limits of the mitigation here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDetectionMethod', 'CweMitigation'],
         'exact_mappings': ['sepses_cwe:mitigationEffectivenessNote']} })


class CweDemonstrativeExample(ConfiguredBaseModel):
    """
    A worked example of how a weakness looks in code.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'DemonstrativeExamplesType/Demonstrative_Example'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Demonstrative_Example_ID: Optional[str] = Field(default=None, description="""An identifier that lets entries share this example, such as DX-221.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDemonstrativeExample']} })
    Title_Text: Optional[str] = Field(default=None, description="""A title for the example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDemonstrativeExample']} })
    Intro_Text: str = Field(default=..., description="""The setting of the code, and what it is trying to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDemonstrativeExample']} })
    Entries: Optional[list[CweExampleEntry]] = Field(default=None, description="""The example's prose and code, in the order they are meant to be read.""", json_schema_extra = { "linkml_meta": {'comments': ['The XSD gives this list no name, because it writes a repeating '
                      'choice of two elements. The name is the one the CWE REST API '
                      'uses, and it is the one key here that is not in the XSD.'],
         'domain_of': ['CweDemonstrativeExample']} })


class CweExampleEntry(ConfiguredBaseModel):
    """
    One step of a worked example, either some prose or some code.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'DemonstrativeExamplesType/Demonstrative_Example#choice'}},
         'exactly_one_of': [{'slot_conditions': {'Body_Text': {'name': 'Body_Text',
                                                               'required': True}}},
                            {'slot_conditions': {'Example_Code': {'name': 'Example_Code',
                                                                  'required': True}}}],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Body_Text: Optional[str] = Field(default=None, description="""Prose that explains the code around it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExampleEntry']} })
    Example_Code: Optional[CweExampleCode] = Field(default=None, description="""A block of code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExampleEntry']} })


class CweExampleCode(ConfiguredBaseModel):
    """
    A block of code in a worked example.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredCodeType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Nature: CweCodeNature = Field(default=..., description="""What the code shows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweExampleCode']} })
    Language: Optional[CweLanguageName] = Field(default=None, description="""The language of the code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweApplicablePlatforms', 'CweExampleCode']} })
    Value: Optional[str] = Field(default=None, description="""The code, as an XHTML fragment with its special characters escaped.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_text_of': {'tag': 'xsd_text_of',
                                         'value': 'StructuredTextType'}},
         'domain_of': ['CweDimension',
                       'CweCustomPhase',
                       'CweNote',
                       'CwePreviousEntryName',
                       'CweExampleCode']} })


class CweObservedExample(ConfiguredBaseModel):
    """
    A real case of a weakness, usually a CVE record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ObservedExampleType/Observed_Example'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Reference: str = Field(default=..., description="""The identifier of the case, such as a CVE identifier.""", json_schema_extra = { "linkml_meta": {'comments': ['In CWE 5.0 it holds a CVE identifier in 3173 of 3183 cases and '
                      'an external reference such as [REF-1100] in the rest, so '
                      "lmodel/cve's cveId is only related."],
         'domain_of': ['CweObservedExample'],
         'related_mappings': ['cve:cveId']} })
    Description: str = Field(default=..., description="""What went wrong in that case, as it bears on the weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder']} })
    Link: str = Field(default=..., description="""An address with more about the case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweObservedExample']} })
    Rationale: Optional[list[CweObservedExampleRationale]] = Field(default=None, description="""A hint at why this case was chosen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference', 'CweObservedExample', 'CweMappingNotes']} })


class CweRelatedAttackPattern(ConfiguredBaseModel):
    """
    A pointer from a weakness to an attack pattern in the CAPEC list.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedAttackPatternsType/Related_Attack_Pattern'}},
         'comments': ['CAPEC holds the same link from its own side. CWE 5.0 and CAPEC '
                      '3.9 each name the same 1212 pairs, which '
                      'tests/test_catalogue.py holds, so the two classes are the two '
                      'ends of one link and the mapping is related.'],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries',
         'related_mappings': ['capec:CapecRelatedWeakness']})

    CAPEC_ID: str = Field(default=..., description="""The number of the attack pattern in the CAPEC list.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedAttackPattern'],
         'related_mappings': ['capec:CapecAttackPattern']} })


class CweStakeholder(ConfiguredBaseModel):
    """
    A group of people who may find a view useful.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AudienceType/Stakeholder'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Type: CweStakeholderType = Field(default=..., description="""The group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })
    Description: Optional[str] = Field(default=None, description="""What in the view this group may find useful.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness',
                       'CweWeaknessOrdinality',
                       'CweAlternateTerm',
                       'CweDetectionMethod',
                       'CweMitigation',
                       'CweObservedExample',
                       'CweStakeholder']} })


class CweMember(ConfiguredBaseModel):
    """
    A link from a grouping or a view to an entry it holds or belongs to, in one view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'MemberType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    CWE_ID: str = Field(default=..., description="""The entry at the other end of the link.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweMember', 'CweMappingSuggestion']} })
    View_ID: str = Field(default=..., description="""The view in which the link holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweMember']} })
    Dimensions: Optional[list[CweDimension]] = Field(default=None, description="""The aspects in which the two entries differ.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeakness', 'CweRelatedWeakness', 'CweMember']} })

    @field_validator('CWE_ID')
    def pattern_CWE_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CWE_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CWE_ID format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('View_ID')
    def pattern_View_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid View_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid View_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CweRelationships(ConfiguredBaseModel):
    """
    The entries that a grouping or a view holds or belongs to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'RelationshipsType'}},
         'any_of': [{'slot_conditions': {'Member_Of': {'name': 'Member_Of',
                                                       'required': True}}},
                    {'slot_conditions': {'Has_Member': {'name': 'Has_Member',
                                                        'required': True}}}],
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Member_Of: Optional[list[CweMember]] = Field(default=None, description="""An entry that holds this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelationships']} })
    Has_Member: Optional[list[CweMember]] = Field(default=None, description="""An entry that this one holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelationships']} })


class CweMappingNotes(ConfiguredBaseModel):
    """
    Guidance on whether to map a real vulnerability to an entry, and on what to use instead.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'MappingNotesType'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Usage: CweUsage = Field(default=..., description="""Whether the entry may be used for mapping.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMappingNotes'],
         'exact_mappings': ['sepses_cwe:mappingUsage']} })
    Rationale: str = Field(default=..., description="""Why the entry has that usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweExternalReference', 'CweObservedExample', 'CweMappingNotes']} })
    Comments: str = Field(default=..., description="""More advice for someone mapping to the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMappingNotes']} })
    Reasons: list[CweMappingReason] = Field(default=..., description="""Short labels that sum up the usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMappingNotes']} })
    Suggestions: Optional[list[CweMappingSuggestion]] = Field(default=None, description="""Other weaknesses that may suit the mapping better.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMappingNotes']} })


class CweMappingReason(ConfiguredBaseModel):
    """
    One short label that sums up the usage of an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ReasonsType/Reason'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    Type: CweReason = Field(default=..., description="""The label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweDimension',
                       'CweNote',
                       'CweContribution',
                       'CweView',
                       'CweStakeholder',
                       'CweMappingReason']} })


class CweMappingSuggestion(ConfiguredBaseModel):
    """
    A weakness that may suit a mapping better than this entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'SuggestionsType/Suggestion'}},
         'from_schema': 'https://w3id.org/lmodel/cwe/cwe_entries'})

    CWE_ID: str = Field(default=..., description="""The suggested weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweRelatedWeakness', 'CweMember', 'CweMappingSuggestion']} })
    Comment: str = Field(default=..., description="""When the suggestion applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweMappingSuggestion']} })

    @field_validator('CWE_ID')
    def pattern_CWE_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CWE_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CWE_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CweWeaknessCatalog(ConfiguredBaseModel):
    """
    One release of the CWE List, with all its entries and the sources they cite.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'Weakness_Catalog'}},
         'close_mappings': ['skos:ConceptScheme', 'schema:DefinedTermSet'],
         'comments': ["Wikidata's item is the catalogue in general and this class is "
                      'one release of it, so the item is related.'],
         'from_schema': 'https://w3id.org/lmodel/cwe',
         'related_mappings': ['wd:Q2682392'],
         'tree_root': True})

    Name: str = Field(default=..., description="""The name of the catalogue, which is CWE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweEntry',
                       'CweLanguagePlatform',
                       'CweOperatingSystemPlatform',
                       'CweArchitecturePlatform',
                       'CweTechnologyPlatform',
                       'CweWeaknessCatalog']} })
    Version: str = Field(default=..., description="""The version of this release.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweNote',
                       'CwePreviousEntryName',
                       'CweOperatingSystemPlatform',
                       'CweWeaknessCatalog']} })
    Date: date = Field(default=..., description="""The date of this release.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CwePreviousEntryName', 'CweWeaknessCatalog']} })
    Weaknesses: Optional[list[CweWeakness]] = Field(default=None, description="""The weakness entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeaknessCatalog']} })
    Groupings: Optional[list[CweGrouping]] = Field(default=None, description="""The grouping entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeaknessCatalog']} })
    Views: Optional[list[CweView]] = Field(default=None, description="""The view entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeaknessCatalog']} })
    External_References: Optional[list[CweExternalReference]] = Field(default=None, description="""The sources that the entries cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CweWeaknessCatalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CweExternalReference.model_rebuild()
CweReference.model_rebuild()
CweDimension.model_rebuild()
CweCustomPhase.model_rebuild()
CweNote.model_rebuild()
CweTaxonomyMapping.model_rebuild()
CweContentHistory.model_rebuild()
CweSubmission.model_rebuild()
CweModification.model_rebuild()
CweContribution.model_rebuild()
CwePreviousEntryName.model_rebuild()
CweEntry.model_rebuild()
CweWeakness.model_rebuild()
CweGrouping.model_rebuild()
CweView.model_rebuild()
CweRelatedWeakness.model_rebuild()
CweWeaknessOrdinality.model_rebuild()
CweApplicablePlatforms.model_rebuild()
CweLanguagePlatform.model_rebuild()
CweOperatingSystemPlatform.model_rebuild()
CweArchitecturePlatform.model_rebuild()
CweTechnologyPlatform.model_rebuild()
CweAlternateTerm.model_rebuild()
CweIntroduction.model_rebuild()
CweConsequence.model_rebuild()
CweDetectionMethod.model_rebuild()
CweMitigation.model_rebuild()
CweDemonstrativeExample.model_rebuild()
CweExampleEntry.model_rebuild()
CweExampleCode.model_rebuild()
CweObservedExample.model_rebuild()
CweRelatedAttackPattern.model_rebuild()
CweStakeholder.model_rebuild()
CweMember.model_rebuild()
CweRelationships.model_rebuild()
CweMappingNotes.model_rebuild()
CweMappingReason.model_rebuild()
CweMappingSuggestion.model_rebuild()
CweWeaknessCatalog.model_rebuild()
