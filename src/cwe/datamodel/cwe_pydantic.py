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


metamodel_version = "1.7.0"
version = "7.3"


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


linkml_meta = LinkMLMeta({'annotations': {'source_columns': {'tag': 'source_columns',
                                        'value': 'CWE-ID,CWE Name,Source'},
                     'xsd_namespace': {'tag': 'xsd_namespace',
                                       'value': 'http://cwe.mitre.org/cwe-7'},
                     'xsd_schema_version': {'tag': 'xsd_schema_version',
                                            'value': '7.3'}},
     'default_prefix': 'cwe',
     'default_range': 'string',
     'description': 'MITRE Common Weakness Enumeration (CWE) LinkML Schema.\n'
                    '\n'
                    'Self-contained schema covering the full MITRE CWE XSD: '
                    'weakness entries,\n'
                    'categories, views, external references, and NVD weakness '
                    'observations (CWE-ID,\n'
                    'CWE Name, Source).',
     'id': 'https://w3id.org/lmodel/cwe',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'cwe',
     'prefixes': {'WIKIDATA': {'prefix_prefix': 'WIKIDATA',
                               'prefix_reference': 'https://www.wikidata.org/wiki/'},
                  'capec': {'prefix_prefix': 'capec',
                            'prefix_reference': 'https://w3id.org/lmodel/capec/'},
                  'cwe': {'prefix_prefix': 'cwe',
                          'prefix_reference': 'https://w3id.org/lmodel/cwe/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/cwe',
                  'https://cwe.mitre.org/data/index.html',
                  'https://nvd.nist.gov/'],
     'source': 'https://cwe.mitre.org/data/downloads.html',
     'source_file': 'src/cwe/schema/cwe.yaml',
     'subsets': {'cwe_dictionary': {'description': 'Canonical MITRE CWE dictionary '
                                                   'records.',
                                    'from_schema': 'https://w3id.org/lmodel/cwe',
                                    'name': 'cwe_dictionary'},
                 'nvd_weakness_observation': {'description': 'Weakness rows '
                                                             'observed in NVD '
                                                             'vulnerability detail '
                                                             'pages.',
                                              'from_schema': 'https://w3id.org/lmodel/cwe',
                                              'name': 'nvd_weakness_observation'}},
     'title': 'cwe',
     'types': {'CveId': {'base': 'str',
                         'description': 'A CVE identifier assigned by a CVE '
                                        'Numbering Authority (CNA). Format: '
                                        'CVE-YYYY-NNNNN.',
                         'from_schema': 'https://w3id.org/lmodel/cwe',
                         'name': 'CveId',
                         'pattern': '^CVE-[0-9]{4}-[0-9]+$',
                         'uri': 'xsd:string'}}} )

class WeaknessSource(str, Enum):
    """
    Source attribution for weakness data in NVD/CVE contexts.
    """
    MITRE = "MITRE"
    """
    Data sourced from MITRE CWE content.
    """
    NIST = "NIST"
    """
    Data produced by NIST/NVD analysis.
    """
    ASSIGNER = "ASSIGNER"
    """
    Data provided by the CVE assigner/CNA.
    """
    CNA = "CNA"
    """
    Data provided by a CVE Numbering Authority.
    """
    OTHER = "OTHER"
    """
    Other or unspecified source.
    """


class WeaknessAbstraction(str, Enum):
    """
    CWE abstraction layer (AbstractionEnumeration in XSD).
    """
    PILLAR = "PILLAR"
    """
    Most abstract type; a theme for all class/base/variant weaknesses.
    """
    CLASS = "CLASS"
    """
    Abstract, independent of any specific language or technology.
    """
    BASE = "BASE"
    """
    Mostly independent of resource or technology; supports detection/prevention.
    """
    VARIANT = "VARIANT"
    """
    Linked to a specific language or technology.
    """
    COMPOUND = "COMPOUND"
    """
    Meaningful aggregation — Chain or Composite.
    """


class WeaknessStatus(str, Enum):
    """
    Lifecycle status of a CWE entry, category, or view (StatusEnumeration in XSD).
    """
    DEPRECATED = "DEPRECATED"
    """
    Removed from CWE; likely a duplicate or created in error.
    """
    DRAFT = "DRAFT"
    """
    All important elements filled; may still have problems or gaps.
    """
    INCOMPLETE = "INCOMPLETE"
    """
    Not all important elements filled; quality not guaranteed.
    """
    OBSOLETE = "OBSOLETE"
    """
    Still valid but no longer relevant; likely superseded.
    """
    STABLE = "STABLE"
    """
    All important elements verified; unlikely to change significantly.
    """
    USABLE = "USABLE"
    """
    Has received close extensive review; critical elements verified.
    """


class WeaknessStructure(str, Enum):
    """
    Structural nature of a weakness (StructureEnumeration in XSD).
    """
    SIMPLE = "SIMPLE"
    """
    Single weakness whose exploitation is not dependent on another weakness.
    """
    CHAIN = "CHAIN"
    """
    Set of weaknesses reachable consecutively to produce a vulnerability.
    """
    COMPOSITE = "COMPOSITE"
    """
    Set of weaknesses that must all be present simultaneously.
    """


class LikelihoodLevel(str, Enum):
    """
    Likelihood of exploitation or occurrence (LikelihoodEnumeration in XSD).
    """
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"
    """
    Actual likelihood is not known.
    """


class WeaknessRelationNature(str, Enum):
    """
    Nature of a directional relationship between two CWE entries (RelatedNatureEnumeration in XSD).
    """
    CHILD_OF = "CHILD_OF"
    """
    Related weakness at a higher level of abstraction.
    """
    PARENT_OF = "PARENT_OF"
    """
    Related weakness at a lower level of abstraction.
    """
    STARTS_WITH = "STARTS_WITH"
    """
    Chaining; this weakness starts the chain.
    """
    CAN_FOLLOW = "CAN_FOLLOW"
    """
    Chaining; this weakness can follow the target.
    """
    CAN_PRECEDE = "CAN_PRECEDE"
    """
    Chaining; this weakness can precede the target.
    """
    REQUIRED_BY = "REQUIRED_BY"
    """
    Composite; this weakness is required by the target.
    """
    REQUIRES = "REQUIRES"
    """
    Composite; this weakness requires the target.
    """
    CAN_ALSO_BE = "CAN_ALSO_BE"
    """
    In proper context can also be perceived as the target weakness.
    """
    PEER_OF = "PEER_OF"
    """
    Shows similarity with the target; no precise fit elsewhere.
    """


class WeaknessOrdinalityLevel(str, Enum):
    """
    Potential ordering relationship of a weakness relative to others (OrdinalityEnumeration in XSD).
    """
    PRIMARY = "PRIMARY"
    """
    Weakness exists independent of other weaknesses.
    """
    RESULTANT = "RESULTANT"
    """
    Weakness exists only in the presence of other weaknesses.
    """
    INDIRECT = "INDIRECT"
    """
    Does not directly lead to security weaknesses but may facilitate them.
    """


class OrdinalQualifier(str, Enum):
    """
    Marks a related-weakness relationship as the primary one for a given <Nature, CWE_ID, View_ID> triple (OrdinalEnumeration in XSD).
    """
    PRIMARY = "PRIMARY"
    """
    Primary ChildOf relationship for this weakness in the given view.
    """


class SecurityScope(str, Enum):
    """
    Security property area that can be violated by exploiting a weakness (ScopeEnumeration in XSD).
    """
    CONFIDENTIALITY = "CONFIDENTIALITY"
    INTEGRITY = "INTEGRITY"
    AVAILABILITY = "AVAILABILITY"
    ACCESS_CONTROL = "ACCESS_CONTROL"
    ACCOUNTABILITY = "ACCOUNTABILITY"
    AUTHENTICATION = "AUTHENTICATION"
    AUTHORIZATION = "AUTHORIZATION"
    NON_REPUDIATION = "NON_REPUDIATION"
    OTHER = "OTHER"


class TechnicalImpact(str, Enum):
    """
    Technical impact of successfully exploiting a weakness (TechnicalImpactEnumeration in XSD).
    """
    MODIFY_MEMORY = "MODIFY_MEMORY"
    READ_MEMORY = "READ_MEMORY"
    MODIFY_FILES_OR_DIRECTORIES = "MODIFY_FILES_OR_DIRECTORIES"
    READ_FILES_OR_DIRECTORIES = "READ_FILES_OR_DIRECTORIES"
    MODIFY_APPLICATION_DATA = "MODIFY_APPLICATION_DATA"
    READ_APPLICATION_DATA = "READ_APPLICATION_DATA"
    DOS_CRASH_EXIT_OR_RESTART = "DOS_CRASH_EXIT_OR_RESTART"
    """
    DoS: Crash, Exit, or Restart
    """
    DOS_AMPLIFICATION = "DOS_AMPLIFICATION"
    """
    DoS: Amplification
    """
    DOS_INSTABILITY = "DOS_INSTABILITY"
    """
    DoS: Instability
    """
    DOS_RESOURCE_CONSUMPTION_CPU = "DOS_RESOURCE_CONSUMPTION_CPU"
    """
    DoS: Resource Consumption (CPU)
    """
    DOS_RESOURCE_CONSUMPTION_MEMORY = "DOS_RESOURCE_CONSUMPTION_MEMORY"
    """
    DoS: Resource Consumption (Memory)
    """
    DOS_RESOURCE_CONSUMPTION_OTHER = "DOS_RESOURCE_CONSUMPTION_OTHER"
    """
    DoS: Resource Consumption (Other)
    """
    EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS = "EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS"
    GAIN_PRIVILEGES_OR_ASSUME_IDENTITY = "GAIN_PRIVILEGES_OR_ASSUME_IDENTITY"
    BYPASS_PROTECTION_MECHANISM = "BYPASS_PROTECTION_MECHANISM"
    HIDE_ACTIVITIES = "HIDE_ACTIVITIES"
    ALTER_EXECUTION_LOGIC = "ALTER_EXECUTION_LOGIC"
    QUALITY_DEGRADATION = "QUALITY_DEGRADATION"
    UNEXPECTED_STATE = "UNEXPECTED_STATE"
    VARIES_BY_CONTEXT = "VARIES_BY_CONTEXT"
    INCREASE_ANALYTICAL_COMPLEXITY = "INCREASE_ANALYTICAL_COMPLEXITY"
    """
    Makes vulnerability harder to find and fix.
    """
    REDUCE_MAINTAINABILITY = "REDUCE_MAINTAINABILITY"
    REDUCE_PERFORMANCE = "REDUCE_PERFORMANCE"
    REDUCE_RELIABILITY = "REDUCE_RELIABILITY"
    OTHER = "OTHER"


class LifecyclePhase(str, Enum):
    """
    Phase in the product lifecycle where a weakness may be introduced or a mitigation applied (PhaseEnumeration in XSD).
    """
    POLICY = "POLICY"
    REQUIREMENTS = "REQUIREMENTS"
    ARCHITECTURE_AND_DESIGN = "ARCHITECTURE_AND_DESIGN"
    IMPLEMENTATION = "IMPLEMENTATION"
    BUILD_AND_COMPILATION = "BUILD_AND_COMPILATION"
    TESTING = "TESTING"
    DOCUMENTATION = "DOCUMENTATION"
    BUNDLING = "BUNDLING"
    DISTRIBUTION = "DISTRIBUTION"
    INSTALLATION = "INSTALLATION"
    SYSTEM_CONFIGURATION = "SYSTEM_CONFIGURATION"
    OPERATION = "OPERATION"
    PATCHING_AND_MAINTENANCE = "PATCHING_AND_MAINTENANCE"
    PORTING = "PORTING"
    INTEGRATION = "INTEGRATION"
    MANUFACTURING = "MANUFACTURING"
    DECOMMISSIONING_AND_END_OF_LIFE = "DECOMMISSIONING_AND_END_OF_LIFE"


class MitigationStrategy(str, Enum):
    """
    General strategy for protecting a system (MitigationStrategyEnumeration in XSD).
    """
    ATTACK_SURFACE_REDUCTION = "ATTACK_SURFACE_REDUCTION"
    COMPILATION_OR_BUILD_HARDENING = "COMPILATION_OR_BUILD_HARDENING"
    ENFORCEMENT_BY_CONVERSION = "ENFORCEMENT_BY_CONVERSION"
    ENVIRONMENT_HARDENING = "ENVIRONMENT_HARDENING"
    FIREWALL = "FIREWALL"
    INPUT_VALIDATION = "INPUT_VALIDATION"
    LANGUAGE_SELECTION = "LANGUAGE_SELECTION"
    LIBRARIES_OR_FRAMEWORKS = "LIBRARIES_OR_FRAMEWORKS"
    RESOURCE_LIMITATION = "RESOURCE_LIMITATION"
    OUTPUT_ENCODING = "OUTPUT_ENCODING"
    PARAMETERIZATION = "PARAMETERIZATION"
    REFACTORING = "REFACTORING"
    SANDBOX_OR_JAIL = "SANDBOX_OR_JAIL"
    SEPARATION_OF_PRIVILEGE = "SEPARATION_OF_PRIVILEGE"


class DetectionMethodType(str, Enum):
    """
    Method that may be employed to detect a weakness (DetectionMethodEnumeration in XSD).
    """
    AUTOMATED_ANALYSIS = "AUTOMATED_ANALYSIS"
    AUTOMATED_DYNAMIC_ANALYSIS = "AUTOMATED_DYNAMIC_ANALYSIS"
    AUTOMATED_STATIC_ANALYSIS = "AUTOMATED_STATIC_ANALYSIS"
    AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE = "AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE"
    """
    Automated Static Analysis - Source Code
    """
    AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE = "AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE"
    """
    Automated Static Analysis - Binary or Bytecode
    """
    FUZZING = "FUZZING"
    MANUAL_ANALYSIS = "MANUAL_ANALYSIS"
    MANUAL_DYNAMIC_ANALYSIS = "MANUAL_DYNAMIC_ANALYSIS"
    MANUAL_STATIC_ANALYSIS = "MANUAL_STATIC_ANALYSIS"
    MANUAL_STATIC_ANALYSIS_SOURCE_CODE = "MANUAL_STATIC_ANALYSIS_SOURCE_CODE"
    """
    Manual Static Analysis - Source Code
    """
    MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE = "MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE"
    """
    Manual Static Analysis - Binary or Bytecode
    """
    WHITE_BOX = "WHITE_BOX"
    BLACK_BOX = "BLACK_BOX"
    ARCHITECTURE_OR_DESIGN_REVIEW = "ARCHITECTURE_OR_DESIGN_REVIEW"
    DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION = "DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION"
    DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION = "DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION"
    FORMAL_VERIFICATION = "FORMAL_VERIFICATION"
    SIMULATION_EMULATION = "SIMULATION_EMULATION"
    OTHER = "OTHER"


class DetectionEffectiveness(str, Enum):
    """
    Effectiveness of a detection method (DetectionEffectivenessEnumeration in XSD).
    """
    HIGH = "HIGH"
    """
    Succeeds frequently; few false reports.
    """
    MODERATE = "MODERATE"
    """
    Applicable broadly but may lack complete coverage.
    """
    SOAR_PARTIAL = "SOAR_PARTIAL"
    """
    Cost-effective for partial coverage per IATAC SOAR report.
    """
    OPPORTUNISTIC = "OPPORTUNISTIC"
    """
    May succeed by chance rather than reliably.
    """
    LIMITED = "LIMITED"
    """
    Useful in limited circumstances.
    """
    NONE = "NONE"
    """
    Highly unlikely to work.
    """


class MitigationEffectiveness(str, Enum):
    """
    Effectiveness of a potential mitigation (EffectivenessEnumeration in XSD).
    """
    HIGH = "HIGH"
    """
    Frequently eliminates the weakness entirely.
    """
    MODERATE = "MODERATE"
    """
    Prevents multiple forms but lacks complete coverage.
    """
    LIMITED = "LIMITED"
    """
    Useful in limited circumstances.
    """
    INCIDENTAL = "INCIDENTAL"
    """
    Generally not effective; only protects by chance.
    """
    DEFENSE_IN_DEPTH = "DEFENSE_IN_DEPTH"
    """
    Minimizes impact rather than preventing the weakness.
    """
    DISCOURAGED_COMMON_PRACTICE = "DISCOURAGED_COMMON_PRACTICE"
    """
    Commonly attempted but known to be ineffective or risky.
    """
    NONE = "NONE"


class NoteType(str, Enum):
    """
    Type of note on a CWE entry (NoteTypeEnumeration in XSD).
    """
    APPLICABLE_PLATFORM = "APPLICABLE_PLATFORM"
    MAINTENANCE = "MAINTENANCE"
    RELATIONSHIP = "RELATIONSHIP"
    RESEARCH_GAP = "RESEARCH_GAP"
    TERMINOLOGY = "TERMINOLOGY"
    THEORETICAL = "THEORETICAL"
    OTHER = "OTHER"


class CWEViewType(str, Enum):
    """
    Type of CWE view (ViewTypeEnumeration in XSD).
    """
    GRAPH = "GRAPH"
    """
    Hierarchical representation from a specific vantage point.
    """
    EXPLICIT = "EXPLICIT"
    """
    Flat list related through an external factor (e.g. Top-N list).
    """
    IMPLICIT = "IMPLICIT"
    """
    Subset identified by an XSL filter expression.
    """


class FunctionalArea(str, Enum):
    """
    Functional area where a weakness is most likely to occur (FunctionalAreaEnumeration in XSD).
    """
    AUTHENTICATION = "AUTHENTICATION"
    AUTHORIZATION = "AUTHORIZATION"
    CODE_LIBRARIES = "CODE_LIBRARIES"
    COUNTERS = "COUNTERS"
    CRYPTOGRAPHY = "CRYPTOGRAPHY"
    ERROR_HANDLING = "ERROR_HANDLING"
    INTERPROCESS_COMMUNICATION = "INTERPROCESS_COMMUNICATION"
    FILE_PROCESSING = "FILE_PROCESSING"
    LOGGING = "LOGGING"
    MEMORY_MANAGEMENT = "MEMORY_MANAGEMENT"
    NETWORKING = "NETWORKING"
    NUMBER_PROCESSING = "NUMBER_PROCESSING"
    PROGRAM_INVOCATION = "PROGRAM_INVOCATION"
    PROTECTION_MECHANISM = "PROTECTION_MECHANISM"
    SESSION_MANAGEMENT = "SESSION_MANAGEMENT"
    SIGNALS = "SIGNALS"
    STRING_PROCESSING = "STRING_PROCESSING"
    NOT_FUNCTIONAL_AREA_SPECIFIC = "NOT_FUNCTIONAL_AREA_SPECIFIC"
    POWER = "POWER"
    CLOCK = "CLOCK"


class AffectedResource(str, Enum):
    """
    System resource that can be affected by exploiting a weakness (ResourceEnumeration in XSD).
    """
    CPU = "CPU"
    FILE_OR_DIRECTORY = "FILE_OR_DIRECTORY"
    MEMORY = "MEMORY"
    SYSTEM_PROCESS = "SYSTEM_PROCESS"
    OTHER = "OTHER"


class PlatformPrevalence(str, Enum):
    """
    Regularity with which a weakness applies to a given platform (PrevalenceEnumeration in XSD).
    """
    OFTEN = "OFTEN"
    SOMETIMES = "SOMETIMES"
    RARELY = "RARELY"
    UNDETERMINED = "UNDETERMINED"


class ProgrammingLanguage(str, Enum):
    """
    Source code language or data format (LanguageNameEnumeration in XSD).
    """
    ADA = "ADA"
    ARM_ASSEMBLY = "ARM_ASSEMBLY"
    ASP = "ASP"
    ASP_DOT_NET = "ASP_DOT_NET"
    BASIC = "BASIC"
    C = "C"
    C_PLUS_PLUS = "C_PLUS_PLUS"
    C_SHARP = "C_SHARP"
    COBOL = "COBOL"
    FORTRAN = "FORTRAN"
    FSHARP = "FSHARP"
    GO = "GO"
    HTML = "HTML"
    JAVA = "JAVA"
    JAVASCRIPT = "JAVASCRIPT"
    JSON = "JSON"
    JSP = "JSP"
    OBJECTIVE_C = "OBJECTIVE_C"
    PASCAL = "PASCAL"
    PERL = "PERL"
    PHP = "PHP"
    PSEUDOCODE = "PSEUDOCODE"
    PYTHON = "PYTHON"
    RUBY = "RUBY"
    RUST = "RUST"
    SHELL = "SHELL"
    SQL = "SQL"
    SWIFT = "SWIFT"
    VB_DOT_NET = "VB_DOT_NET"
    VERILOG = "VERILOG"
    VHDL = "VHDL"
    XML = "XML"
    X86_ASSEMBLY = "X86_ASSEMBLY"
    OTHER = "OTHER"


class LanguageClass(str, Enum):
    """
    Class of programming language (LanguageClassEnumeration in XSD).
    """
    ASSEMBLY = "ASSEMBLY"
    COMPILED = "COMPILED"
    HARDWARE_DESCRIPTION_LANGUAGE = "HARDWARE_DESCRIPTION_LANGUAGE"
    INTERPRETED = "INTERPRETED"
    OBJECT_ORIENTED = "OBJECT_ORIENTED"
    MEMORY_UNSAFE = "MEMORY_UNSAFE"
    NOT_LANGUAGE_SPECIFIC = "NOT_LANGUAGE_SPECIFIC"


class ArchitectureName(str, Enum):
    """
    Processor architecture (ArchitectureNameEnumeration in XSD).
    """
    ALPHA = "ALPHA"
    ARM = "ARM"
    ITANIUM = "ITANIUM"
    POWER_ARCHITECTURE = "POWER_ARCHITECTURE"
    SPARC = "SPARC"
    X86 = "X86"
    OTHER = "OTHER"


class ArchitectureClass(str, Enum):
    """
    Class of processor architecture (ArchitectureClassEnumeration in XSD).
    """
    EMBEDDED = "EMBEDDED"
    MICROCOMPUTER = "MICROCOMPUTER"
    WORKSTATION = "WORKSTATION"
    NOT_ARCHITECTURE_SPECIFIC = "NOT_ARCHITECTURE_SPECIFIC"


class OperatingSystemName(str, Enum):
    """
    Operating system (OperatingSystemNameEnumeration in XSD).
    """
    AIX = "AIX"
    ANDROID = "ANDROID"
    BLACKBERRY_OS = "BLACKBERRY_OS"
    CHROME_OS = "CHROME_OS"
    DARWIN = "DARWIN"
    FREEBSD = "FREEBSD"
    IOS = "IOS"
    MACOS = "MACOS"
    NETBSD = "NETBSD"
    OPENBSD = "OPENBSD"
    RED_HAT = "RED_HAT"
    SOLARIS = "SOLARIS"
    SUSE = "SUSE"
    TVOS = "TVOS"
    UBUNTU = "UBUNTU"
    WATCHOS = "WATCHOS"
    WINDOWS_9X = "WINDOWS_9X"
    WINDOWS_EMBEDDED = "WINDOWS_EMBEDDED"
    WINDOWS_NT = "WINDOWS_NT"


class OperatingSystemClass(str, Enum):
    """
    Class of operating system (OperatingSystemClassEnumeration in XSD).
    """
    LINUX = "LINUX"
    MACOS = "MACOS"
    UNIX = "UNIX"
    WINDOWS = "WINDOWS"
    NOT_OS_SPECIFIC = "NOT_OS_SPECIFIC"


class TechnologyName(str, Enum):
    """
    Specific technology applicable to a weakness (TechnologyNameEnumeration in XSD).
    """
    AI_ML = "AI_ML"
    WEB_SERVER = "WEB_SERVER"
    DATABASE_SERVER = "DATABASE_SERVER"
    ACCELERATOR_HARDWARE = "ACCELERATOR_HARDWARE"
    ANALOG_AND_MIXED_SIGNAL_HARDWARE = "ANALOG_AND_MIXED_SIGNAL_HARDWARE"
    AUDIO_VIDEO_HARDWARE = "AUDIO_VIDEO_HARDWARE"
    BUS_INTERFACE_HARDWARE = "BUS_INTERFACE_HARDWARE"
    CLOCK_COUNTER_HARDWARE = "CLOCK_COUNTER_HARDWARE"
    COMMUNICATION_HARDWARE = "COMMUNICATION_HARDWARE"
    CONTROLLER_HARDWARE = "CONTROLLER_HARDWARE"
    MEMORY_HARDWARE = "MEMORY_HARDWARE"
    MICROCONTROLLER_HARDWARE = "MICROCONTROLLER_HARDWARE"
    NETWORK_ON_CHIP_HARDWARE = "NETWORK_ON_CHIP_HARDWARE"
    POWER_MANAGEMENT_HARDWARE = "POWER_MANAGEMENT_HARDWARE"
    PROCESSOR_HARDWARE = "PROCESSOR_HARDWARE"
    SECURITY_HARDWARE = "SECURITY_HARDWARE"
    SENSOR_HARDWARE = "SENSOR_HARDWARE"
    STORAGE_HARDWARE = "STORAGE_HARDWARE"
    TEST_DEBUG_HARDWARE = "TEST_DEBUG_HARDWARE"
    OTHER = "OTHER"


class TechnologyClass(str, Enum):
    """
    Class of technology (TechnologyClassEnumeration in XSD).
    """
    CLIENT_SERVER = "CLIENT_SERVER"
    CLOUD_COMPUTING = "CLOUD_COMPUTING"
    ICS_OT = "ICS_OT"
    MAINFRAME = "MAINFRAME"
    MOBILE = "MOBILE"
    N_TIER = "N_TIER"
    SOA = "SOA"
    SYSTEM_ON_CHIP = "SYSTEM_ON_CHIP"
    WEB_BASED = "WEB_BASED"
    NOT_TECHNOLOGY_SPECIFIC = "NOT_TECHNOLOGY_SPECIFIC"


class TaxonomyMappingFit(str, Enum):
    """
    Closeness of a mapping to an external taxonomy (TaxonomyMappingFitEnumeration in XSD).
    """
    EXACT = "EXACT"
    CWE_MORE_ABSTRACT = "CWE_MORE_ABSTRACT"
    CWE_MORE_SPECIFIC = "CWE_MORE_SPECIFIC"
    IMPRECISE = "IMPRECISE"
    PERSPECTIVE = "PERSPECTIVE"


class TaxonomyName(str, Enum):
    """
    Known taxonomy that can be mapped to CWE (TaxonomyNameEnumeration in XSD).
    """
    SEVEN_PERNICIOUS_KINGDOMS = "SEVEN_PERNICIOUS_KINGDOMS"
    NINETEEN_DEADLY_SINS = "NINETEEN_DEADLY_SINS"
    ASLAM = "ASLAM"
    BISHOP = "BISHOP"
    CERT_C_SECURE_CODING = "CERT_C_SECURE_CODING"
    CERT_CPP_SECURE_CODING = "CERT_CPP_SECURE_CODING"
    THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011 = "THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011"
    CLASP = "CLASP"
    ISA_IEC_62443 = "ISA_IEC_62443"
    LANDWEHR = "LANDWEHR"
    OMG_ASCSM = "OMG_ASCSM"
    OMG_ASCRM = "OMG_ASCRM"
    OMG_ASCMM = "OMG_ASCMM"
    OMG_ASCPEM = "OMG_ASCPEM"
    OWASP_TOP_TEN_2004 = "OWASP_TOP_TEN_2004"
    OWASP_TOP_TEN_2007 = "OWASP_TOP_TEN_2007"
    OWASP_TOP_TEN = "OWASP_TOP_TEN"
    PLOVER = "PLOVER"
    PROTECTION_ANALYSIS = "PROTECTION_ANALYSIS"
    RISOS = "RISOS"
    SEI_CERT_C_CODING_STANDARD = "SEI_CERT_C_CODING_STANDARD"
    SEI_CERT_CPP_CODING_STANDARD = "SEI_CERT_CPP_CODING_STANDARD"
    SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA = "SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA"
    SEI_CERT_PERL_CODING_STANDARD = "SEI_CERT_PERL_CODING_STANDARD"
    SOFTWARE_FAULT_PATTERNS = "SOFTWARE_FAULT_PATTERNS"
    WEBER_KARGER_PARADKAR = "WEBER_KARGER_PARADKAR"
    WASC = "WASC"


class MappingUsage(str, Enum):
    """
    Whether a CWE entry should be used for mapping (UsageEnumeration in XSD).
    """
    ALLOWED = "ALLOWED"
    """
    May be used to map to real-world vulnerabilities.
    """
    ALLOWED_WITH_REVIEW = "ALLOWED_WITH_REVIEW"
    """
    May be used in limited situations requiring careful review.
    """
    DISCOURAGED = "DISCOURAGED"
    """
    Should not be used for mapping.
    """
    PROHIBITED = "PROHIBITED"
    """
    Must not be used for mapping.
    """


class MappingReason(str, Enum):
    """
    Reason why a CWE entry should not be used for mapping (ReasonEnumeration in XSD).
    """
    ABSTRACTION = "ABSTRACTION"
    CATEGORY = "CATEGORY"
    VIEW = "VIEW"
    DEPRECATED = "DEPRECATED"
    POTENTIAL_DEPRECATION = "POTENTIAL_DEPRECATION"
    FREQUENT_MISUSE = "FREQUENT_MISUSE"
    FREQUENT_MISINTERPRETATION = "FREQUENT_MISINTERPRETATION"
    MULTIPLE_USE = "MULTIPLE_USE"
    CWE_OVERLAP = "CWE_OVERLAP"
    ACCEPTABLE_USE = "ACCEPTABLE_USE"
    POTENTIAL_MAJOR_CHANGES = "POTENTIAL_MAJOR_CHANGES"
    OTHER = "OTHER"


class StakeholderType(str, Enum):
    """
    Type of stakeholder in the CWE community (StakeholderEnumeration in XSD).
    """
    ACADEMIC_RESEARCHERS = "ACADEMIC_RESEARCHERS"
    APPLIED_RESEARCHERS = "APPLIED_RESEARCHERS"
    ASSESSMENT_TEAMS = "ASSESSMENT_TEAMS"
    ASSESSMENT_TOOL_VENDORS = "ASSESSMENT_TOOL_VENDORS"
    CWE_TEAM = "CWE_TEAM"
    EDUCATORS = "EDUCATORS"
    HARDWARE_DESIGNERS = "HARDWARE_DESIGNERS"
    INFORMATION_PROVIDERS = "INFORMATION_PROVIDERS"
    PRODUCT_CUSTOMERS = "PRODUCT_CUSTOMERS"
    PRODUCT_VENDORS = "PRODUCT_VENDORS"
    SOFTWARE_DEVELOPERS = "SOFTWARE_DEVELOPERS"
    VULNERABILITY_ANALYSTS = "VULNERABILITY_ANALYSTS"
    OTHER = "OTHER"


class CodeNature(str, Enum):
    """
    Nature of a code snippet in a demonstrative example (StructuredCodeNatureEnumeration in XSD).
    """
    ATTACK = "ATTACK"
    BAD = "BAD"
    GOOD = "GOOD"
    INFORMATIVE = "INFORMATIVE"
    MITIGATION = "MITIGATION"
    RESULT = "RESULT"


class ContentImportance(str, Enum):
    """
    Importance level of a content modification (ImportanceEnumeration in XSD).
    """
    NORMAL = "NORMAL"
    CRITICAL = "CRITICAL"
    """
    Changes the meaning or interpretation of the entry.
    """


class ContributionType(str, Enum):
    """
    Whether a contribution was donated content or general feedback.
    """
    CONTENT = "CONTENT"
    """
    Content donated to the CWE entry.
    """
    FEEDBACK = "FEEDBACK"
    """
    General feedback given about the CWE entry.
    """



class WeaknessCatalog(ConfiguredBaseModel):
    """
    Top-level container for a CWE catalog snapshot (Weakness_Catalog in XSD). Holds weakness entries, categories, views, external references, and NVD weakness observations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['cwe_dictionary'],
         'see_also': ['https://cwe.mitre.org/data/downloads.html'],
         'slot_usage': {'date': {'name': 'date', 'required': True},
                        'name': {'identifier': True, 'name': 'name', 'required': True},
                        'version': {'name': 'version', 'required': True}},
         'tree_root': True})

    name: str = Field(default=..., description="""Short human-readable name or title for this entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    version: str = Field(default=..., description="""Version string of the catalog, entry, or submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog', 'OSPlatform', 'PreviousEntryName'],
         'slot_uri': 'schema:version'} })
    date: date = Field(default=..., description="""Date associated with a catalog snapshot or a name-change event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog', 'PreviousEntryName'], 'slot_uri': 'dct:date'} })
    weaknesses: Optional[list[Weakness]] = Field(default=None, description="""Canonical CWE weakness entries in this catalog snapshot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog']} })
    categories: Optional[list[Category]] = Field(default=None, description="""CWE categories grouping weaknesses by a common characteristic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog']} })
    views: Optional[list[View]] = Field(default=None, description="""CWE views providing different perspectives on the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog']} })
    external_references: Optional[list[ExternalReference]] = Field(default=None, description="""External references shared across CWE entries in this catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog']} })
    observations: Optional[list[NVDWeaknessObservation]] = Field(default=None, description="""Weakness observations from NVD vulnerability detail pages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog']} })


class Weakness(ConfiguredBaseModel):
    """
    Canonical CWE weakness record (WeaknessType in XSD). Describes a specific type of weakness and the full set of associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:DefinedTerm'],
         'exact_mappings': ['WIKIDATA:Q429785'],
         'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['cwe_dictionary'],
         'see_also': ['https://cwe.mitre.org/data/index.html'],
         'slot_usage': {'abstraction': {'name': 'abstraction', 'required': True},
                        'content_history': {'name': 'content_history',
                                            'required': True},
                        'description': {'name': 'description', 'required': True},
                        'id': {'identifier': True, 'name': 'id', 'required': True},
                        'mapping_notes': {'name': 'mapping_notes', 'required': True},
                        'name': {'name': 'name', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'structure': {'name': 'structure', 'required': True}}})

    id: int = Field(default=..., description="""Unique numeric identifier for the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'dct:identifier'} })
    name: str = Field(default=..., description="""Short human-readable name or title for this entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    description: str = Field(default=..., description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })
    extended_description: Optional[str] = Field(default=None, description="""Extended description providing additional details beyond the core concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    abstraction: WeaknessAbstraction = Field(default=..., description="""CWE abstraction tier (e.g. Base or Variant).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness'], 'slot_uri': 'skos:broader'} })
    structure: WeaknessStructure = Field(default=..., description="""Structural nature of the weakness (Simple, Chain, or Composite).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    status: WeaknessStatus = Field(default=..., description="""Lifecycle status of the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    diagram: Optional[str] = Field(default=None, description="""Optional diagram filename or reference associated with the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    weakness_ordinalities: Optional[list[WeaknessOrdinality]] = Field(default=None, description="""Potential ordering relationships of this weakness with others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    applicable_platforms: Optional[ApplicablePlatforms] = Field(default=None, description="""Languages, OS, architectures, and technologies where this weakness can appear.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    background_details: Optional[list[str]] = Field(default=None, description="""Background information relevant but not describing the weakness itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    alternate_terms: Optional[list[AlternateTerm]] = Field(default=None, description="""Other names by which this weakness is known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    modes_of_introduction: Optional[list[ModeOfIntroduction]] = Field(default=None, description="""Information about how and when this weakness may be introduced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    exploitation_factors: Optional[list[str]] = Field(default=None, description="""Conditions that could increase the likelihood of exploit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    likelihood_of_exploit: Optional[LikelihoodLevel] = Field(default=None, description="""Qualitative likelihood that the weakness can be exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    common_consequences: Optional[list[CommonConsequence]] = Field(default=None, description="""Individual consequences associated with this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    detection_methods: Optional[list[DetectionMethod]] = Field(default=None, description="""Methods that may be employed to detect this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    potential_mitigations: Optional[list[PotentialMitigation]] = Field(default=None, description="""Potential mitigations associated with this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    demonstrative_examples: Optional[list[DemonstrativeExample]] = Field(default=None, description="""Code examples illustrating how this weakness may appear.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    observed_examples: Optional[list[ObservedExample]] = Field(default=None, description="""Real-world instances of this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    functional_areas: Optional[list[FunctionalArea]] = Field(default=None, description="""Functional areas in which this weakness is most likely to occur.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    affected_resources: Optional[list[AffectedResource]] = Field(default=None, description="""System resources that can be affected by exploiting this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""Mappings to equivalent entries in external taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category']} })
    related_attack_patterns: Optional[list[int]] = Field(default=None, description="""CAPEC identifiers of attack patterns associated with this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness'], 'slot_uri': 'skos:related'} })
    related_weaknesses: Optional[list[RelatedWeakness]] = Field(default=None, description="""Typed relationships to other CWE entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    references: Optional[list[CWEReference]] = Field(default=None, description="""Links to external references defined in the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View', 'DemonstrativeExample']} })
    mapping_notes: MappingNotes = Field(default=..., description="""Guidance for when and whether to map an issue to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments about this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'skos:note'} })
    content_history: ContentHistory = Field(default=..., description="""Tracks the original author and subsequent modifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form tags for grouping and downstream filtering.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness']} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'NVDWeaknessObservation'], 'slot_uri': 'dct:source'} })


class Category(ConfiguredBaseModel):
    """
    A collection of weaknesses grouped by a shared characteristic (CategoryType in XSD). Organizational mechanism only; not for mapping.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['cwe_dictionary'],
         'slot_usage': {'content_history': {'name': 'content_history',
                                            'required': True},
                        'id': {'identifier': True, 'name': 'id', 'required': True},
                        'mapping_notes': {'name': 'mapping_notes', 'required': True},
                        'name': {'name': 'name', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'summary': {'name': 'summary', 'required': True}}})

    id: int = Field(default=..., description="""Unique numeric identifier for the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'dct:identifier'} })
    name: str = Field(default=..., description="""Short human-readable name or title for this entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    status: WeaknessStatus = Field(default=..., description="""Lifecycle status of the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    summary: str = Field(default=..., description="""Key points that define a category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Category']} })
    relationships: Optional[Relationship] = Field(default=None, description="""Membership relationships for a CWE category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Category']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""Mappings to equivalent entries in external taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category']} })
    references: Optional[list[CWEReference]] = Field(default=None, description="""Links to external references defined in the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View', 'DemonstrativeExample']} })
    mapping_notes: MappingNotes = Field(default=..., description="""Guidance for when and whether to map an issue to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments about this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'skos:note'} })
    content_history: ContentHistory = Field(default=..., description="""Tracks the original author and subsequent modifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })


class View(ConfiguredBaseModel):
    """
    A perspective from which to look at weaknesses in the catalog (ViewType in XSD). Types: Graph, Explicit slice, Implicit slice.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['cwe_dictionary'],
         'slot_usage': {'content_history': {'name': 'content_history',
                                            'required': True},
                        'id': {'identifier': True, 'name': 'id', 'required': True},
                        'mapping_notes': {'name': 'mapping_notes', 'required': True},
                        'name': {'name': 'name', 'required': True},
                        'objective': {'name': 'objective', 'required': True},
                        'status': {'name': 'status', 'required': True},
                        'type': {'description': 'Type of view (Graph, Explicit, or '
                                                'Implicit).',
                                 'name': 'type',
                                 'range': 'CWEViewType',
                                 'required': True}}})

    id: int = Field(default=..., description="""Unique numeric identifier for the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'dct:identifier'} })
    name: str = Field(default=..., description="""Short human-readable name or title for this entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    type: CWEViewType = Field(default=..., description="""Type of view (Graph, Explicit, or Implicit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['View', 'Audience', 'Note', 'Contribution']} })
    status: WeaknessStatus = Field(default=..., description="""Lifecycle status of the CWE entry, category, or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    objective: str = Field(default=..., description="""Perspective from which a view has been constructed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View']} })
    audience: Optional[list[Audience]] = Field(default=None, description="""Target stakeholder groups for this view or category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View']} })
    members: Optional[list[CatalogMember]] = Field(default=None, description="""Member entries for a CWE view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View']} })
    filter: Optional[str] = Field(default=None, description="""XSL query identifying members of an implicit slice view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View']} })
    references: Optional[list[CWEReference]] = Field(default=None, description="""Links to external references defined in the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View', 'DemonstrativeExample']} })
    mapping_notes: MappingNotes = Field(default=..., description="""Guidance for when and whether to map an issue to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments about this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View'], 'slot_uri': 'skos:note'} })
    content_history: ContentHistory = Field(default=..., description="""Tracks the original author and subsequent modifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View']} })


class ExternalReference(ConfiguredBaseModel):
    """
    Pointer to external reading material shared across CWE entries (ExternalReferenceType in XSD). Identified by Reference_ID (e.g. REF-1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['cwe_dictionary'],
         'slot_usage': {'reference_id': {'identifier': True,
                                         'name': 'reference_id',
                                         'required': True},
                        'title': {'name': 'title', 'required': True}}})

    reference_id: str = Field(default=..., description="""Globally unique identifier for an external reference (e.g. REF-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference'], 'slot_uri': 'dct:identifier'} })
    title: str = Field(default=..., description="""Descriptive title for a reference or catalog element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference'], 'slot_uri': 'dct:title'} })
    authors: Optional[list[str]] = Field(default=None, description="""Authors of the referenced material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    edition: Optional[str] = Field(default=None, description="""Edition of the material being referenced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    publication: Optional[str] = Field(default=None, description="""Name of the magazine or journal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    publication_year: Optional[str] = Field(default=None, description="""Year of publication in YYYY format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    publication_month: Optional[str] = Field(default=None, description="""Month of publication in --MM format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    publication_day: Optional[str] = Field(default=None, description="""Day of publication in ---DD format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    publisher: Optional[str] = Field(default=None, description="""Publisher of the referenced material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })
    url: Optional[str] = Field(default=None, description="""URL pointing to the reference resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference'], 'slot_uri': 'schema:url'} })
    url_date: Optional[date] = Field(default=None, description="""Date when the URL was last validated to exist.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference']} })


class CWEReference(ConfiguredBaseModel):
    """
    Link from a CWE entry to an ExternalReference in the catalog (ReferencesType/Reference in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'external_reference_id': {'name': 'external_reference_id',
                                                  'required': True}}})

    external_reference_id: str = Field(default=..., description="""Identifier of the ExternalReference being linked to (e.g. REF-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CWEReference']} })
    section: Optional[str] = Field(default=None, description="""Section title or page number specific to this use of the reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CWEReference']} })


class RelatedWeakness(ConfiguredBaseModel):
    """
    Typed directional relationship from one CWE entry to another (RelatedWeaknessesType/Related_Weakness in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'chain_id': {'description': 'ID of a named chain for '
                                                    'CanFollow/CanPrecede '
                                                    'relationships.',
                                     'name': 'chain_id'},
                        'cwe_id': {'description': 'Numeric ID of the target CWE entry.',
                                   'name': 'cwe_id',
                                   'required': True},
                        'nature': {'description': 'Nature of the relationship.',
                                   'name': 'nature',
                                   'range': 'WeaknessRelationNature',
                                   'required': True},
                        'ordinal': {'description': 'Set to "Primary" for the primary '
                                                   'ChildOf relationship in the given '
                                                   'view.',
                                    'name': 'ordinal'},
                        'view_id': {'description': 'View within which this '
                                                   'relationship is relevant.',
                                    'name': 'view_id',
                                    'required': True}}})

    nature: WeaknessRelationNature = Field(default=..., description="""Nature of the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'ExampleCode'], 'slot_uri': 'skos:related'} })
    cwe_id: int = Field(default=..., description="""Numeric ID of the target CWE entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'CatalogMember', 'MappingSuggestion']} })
    view_id: int = Field(default=..., description="""View within which this relationship is relevant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'CatalogMember']} })
    chain_id: Optional[int] = Field(default=None, description="""ID of a named chain for CanFollow/CanPrecede relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness']} })
    ordinal: Optional[OrdinalQualifier] = Field(default=None, description="""Set to \"Primary\" for the primary ChildOf relationship in the given view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness']} })


class WeaknessOrdinality(ConfiguredBaseModel):
    """
    Potential ordering relationship with other weaknesses (WeaknessOrdinalitiesType/Weakness_Ordinality in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'description': {'description': 'Context in which this ordering '
                                                       'relationship exists.',
                                        'name': 'description'},
                        'ordinality': {'description': 'Ordinality level (Primary, '
                                                      'Resultant, or Indirect).',
                                       'name': 'ordinality',
                                       'required': True}}})

    ordinality: WeaknessOrdinalityLevel = Field(default=..., description="""Ordinality level (Primary, Resultant, or Indirect).""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessOrdinality']} })
    description: Optional[str] = Field(default=None, description="""Context in which this ordering relationship exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })


class ApplicablePlatforms(ConfiguredBaseModel):
    """
    Languages, operating systems, architectures, and technologies where a weakness could appear (ApplicablePlatformsType in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe'})

    languages: Optional[list[LanguagePlatform]] = Field(default=None, description="""Programming languages applicable to this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApplicablePlatforms']} })
    operating_systems: Optional[list[OSPlatform]] = Field(default=None, description="""Operating systems applicable to this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApplicablePlatforms']} })
    architectures: Optional[list[ArchitecturePlatform]] = Field(default=None, description="""Processor architectures applicable to this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApplicablePlatforms']} })
    technologies: Optional[list[TechnologyPlatform]] = Field(default=None, description="""Technologies applicable to this weakness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApplicablePlatforms']} })


class LanguagePlatform(ConfiguredBaseModel):
    """
    A programming language or language class applicable to a weakness with associated prevalence (Language element in ApplicablePlatformsType).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'class_': {'description': 'Class of the programming language.',
                                   'name': 'class_',
                                   'range': 'LanguageClass'},
                        'name': {'description': 'Name of the programming language.',
                                 'name': 'name',
                                 'range': 'ProgrammingLanguage'},
                        'prevalence': {'description': 'Regularity with which this '
                                                      'weakness applies to this '
                                                      'language.',
                                       'name': 'prevalence',
                                       'required': True}}})

    name: Optional[ProgrammingLanguage] = Field(default=None, description="""Name of the programming language.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    class_: Optional[LanguageClass] = Field(default=None, description="""Class of the programming language.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })
    prevalence: PlatformPrevalence = Field(default=..., description="""Regularity with which this weakness applies to this language.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })


class OSPlatform(ConfiguredBaseModel):
    """
    An operating system or OS class applicable to a weakness (Operating_System element in ApplicablePlatformsType).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'class_': {'description': 'Class of the operating system.',
                                   'name': 'class_',
                                   'range': 'OperatingSystemClass'},
                        'cpe_id': {'description': 'CPE identifier for this operating '
                                                  'system.',
                                   'name': 'cpe_id'},
                        'name': {'description': 'Name of the operating system.',
                                 'name': 'name',
                                 'range': 'OperatingSystemName'},
                        'prevalence': {'description': 'Regularity with which this '
                                                      'weakness applies to this OS.',
                                       'name': 'prevalence',
                                       'required': True},
                        'version': {'description': 'Version of the operating system.',
                                    'name': 'version'}}})

    name: Optional[OperatingSystemName] = Field(default=None, description="""Name of the operating system.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    class_: Optional[OperatingSystemClass] = Field(default=None, description="""Class of the operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })
    version: Optional[str] = Field(default=None, description="""Version of the operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog', 'OSPlatform', 'PreviousEntryName'],
         'slot_uri': 'schema:version'} })
    cpe_id: Optional[str] = Field(default=None, description="""CPE identifier for this operating system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OSPlatform']} })
    prevalence: PlatformPrevalence = Field(default=..., description="""Regularity with which this weakness applies to this OS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })


class ArchitecturePlatform(ConfiguredBaseModel):
    """
    A processor architecture or class applicable to a weakness (Architecture element in ApplicablePlatformsType).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'class_': {'description': 'Class of the processor '
                                                  'architecture.',
                                   'name': 'class_',
                                   'range': 'ArchitectureClass'},
                        'name': {'description': 'Name of the processor architecture.',
                                 'name': 'name',
                                 'range': 'ArchitectureName'},
                        'prevalence': {'description': 'Regularity with which this '
                                                      'weakness applies to this '
                                                      'architecture.',
                                       'name': 'prevalence',
                                       'required': True}}})

    name: Optional[ArchitectureName] = Field(default=None, description="""Name of the processor architecture.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    class_: Optional[ArchitectureClass] = Field(default=None, description="""Class of the processor architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })
    prevalence: PlatformPrevalence = Field(default=..., description="""Regularity with which this weakness applies to this architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })


class TechnologyPlatform(ConfiguredBaseModel):
    """
    A technology or technology class applicable to a weakness (Technology element in ApplicablePlatformsType).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'class_': {'description': 'Class of the technology.',
                                   'name': 'class_',
                                   'range': 'TechnologyClass'},
                        'name': {'description': 'Name of the technology.',
                                 'name': 'name',
                                 'range': 'TechnologyName'},
                        'prevalence': {'description': 'Regularity with which this '
                                                      'weakness applies to this '
                                                      'technology.',
                                       'name': 'prevalence',
                                       'required': True}}})

    name: Optional[TechnologyName] = Field(default=None, description="""Name of the technology.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    class_: Optional[TechnologyClass] = Field(default=None, description="""Class of the technology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })
    prevalence: PlatformPrevalence = Field(default=..., description="""Regularity with which this weakness applies to this technology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform']} })


class AlternateTerm(ConfiguredBaseModel):
    """
    Another name by which this weakness may be known (AlternateTermsType/Alternate_Term in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'term': {'name': 'term', 'required': True}}})

    term: str = Field(default=..., description="""An alternate term by which this weakness may be known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AlternateTerm']} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })


class ModeOfIntroduction(ConfiguredBaseModel):
    """
    Information about how and when a weakness may be introduced (ModesOfIntroductionType/Introduction in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'phase': {'name': 'phase', 'required': True}}})

    phase: LifecyclePhase = Field(default=..., description="""Lifecycle phase for introduction or mitigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModeOfIntroduction']} })
    note: Optional[str] = Field(default=None, description="""Additional contextual note.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModeOfIntroduction', 'CommonConsequence']} })


class CommonConsequence(ConfiguredBaseModel):
    """
    Individual consequence associated with a weakness (CommonConsequencesType/Consequence in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'impacts': {'name': 'impacts', 'required': True},
                        'scopes': {'name': 'scopes', 'required': True}}})

    consequence_id: Optional[str] = Field(default=None, description="""Unique identifier for a common consequence (e.g. CC-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommonConsequence']} })
    scopes: list[SecurityScope] = Field(default=..., description="""Security properties violated by this consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommonConsequence']} })
    impacts: list[TechnicalImpact] = Field(default=..., description="""Technical impacts that arise if the weakness is exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommonConsequence']} })
    likelihood: Optional[LikelihoodLevel] = Field(default=None, description="""Likelihood of this specific consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CommonConsequence']} })
    note: Optional[str] = Field(default=None, description="""Additional contextual note.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModeOfIntroduction', 'CommonConsequence']} })


class DetectionMethod(ConfiguredBaseModel):
    """
    A method that may be employed to detect a weakness, with effectiveness (DetectionMethodsType/Detection_Method in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'effectiveness': {'name': 'effectiveness',
                                          'range': 'DetectionEffectiveness'},
                        'method': {'name': 'method',
                                   'range': 'DetectionMethodType',
                                   'required': True}}})

    detection_method_id: Optional[str] = Field(default=None, description="""Unique identifier for a detection method entry (e.g. DM-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod']} })
    method: DetectionMethodType = Field(default=..., description="""Detection method (range narrowed per class via slot_usage).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod']} })
    description: str = Field(default=..., description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })
    effectiveness: Optional[DetectionEffectiveness] = Field(default=None, description="""Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod', 'PotentialMitigation']} })
    effectiveness_notes: Optional[str] = Field(default=None, description="""Strengths and shortcomings of this detection or mitigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod', 'PotentialMitigation']} })


class PotentialMitigation(ConfiguredBaseModel):
    """
    A potential mitigation for a weakness (PotentialMitigationsType/Mitigation in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'effectiveness': {'name': 'effectiveness',
                                          'range': 'MitigationEffectiveness'}}})

    mitigation_id: Optional[str] = Field(default=None, description="""Unique identifier for a potential mitigation (e.g. MIT-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PotentialMitigation']} })
    phases: Optional[list[LifecyclePhase]] = Field(default=None, description="""Lifecycle phases during which a mitigation may be applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PotentialMitigation']} })
    strategy: Optional[MitigationStrategy] = Field(default=None, description="""General protection strategy to which a mitigation contributes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PotentialMitigation']} })
    description: str = Field(default=..., description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })
    effectiveness: Optional[MitigationEffectiveness] = Field(default=None, description="""Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod', 'PotentialMitigation']} })
    effectiveness_notes: Optional[str] = Field(default=None, description="""Strengths and shortcomings of this detection or mitigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DetectionMethod', 'PotentialMitigation']} })


class DemonstrativeExample(ConfiguredBaseModel):
    """
    A code example illustrating how a weakness may appear (DemonstrativeExamplesType/Demonstrative_Example in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'intro_text': {'name': 'intro_text', 'required': True}}})

    demonstrative_example_id: Optional[str] = Field(default=None, description="""Unique identifier for a demonstrative example (e.g. DX-1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemonstrativeExample']} })
    title_text: Optional[str] = Field(default=None, description="""Optional title for a demonstrative example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemonstrativeExample']} })
    intro_text: str = Field(default=..., description="""Context and setting for the demonstrative example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemonstrativeExample']} })
    body_texts: Optional[list[str]] = Field(default=None, description="""Interleaved body text paragraphs for a demonstrative example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemonstrativeExample']} })
    example_codes: Optional[list[ExampleCode]] = Field(default=None, description="""Structured code snippets within a demonstrative example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemonstrativeExample']} })
    references: Optional[list[CWEReference]] = Field(default=None, description="""Links to external references defined in the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'Category', 'View', 'DemonstrativeExample']} })


class ExampleCode(ConfiguredBaseModel):
    """
    A structured code snippet within a demonstrative example (StructuredCodeType in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'content': {'description': 'Text content of the code snippet.',
                                    'name': 'content'},
                        'language': {'description': 'Programming language used in this '
                                                    'code example.',
                                     'name': 'language'},
                        'nature': {'description': 'Nature of the code (Bad, Good, '
                                                  'Attack, Mitigation, etc.).',
                                   'name': 'nature',
                                   'range': 'CodeNature',
                                   'required': True}}})

    nature: CodeNature = Field(default=..., description="""Nature of the code (Bad, Good, Attack, Mitigation, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'ExampleCode'], 'slot_uri': 'skos:related'} })
    language: Optional[ProgrammingLanguage] = Field(default=None, description="""Programming language used in this code example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExampleCode']} })
    content: Optional[str] = Field(default=None, description="""Text content of the code snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExampleCode', 'Note']} })


class ObservedExample(ConfiguredBaseModel):
    """
    A reference to a real-world instance of a weakness, typically a CVE (ObservedExampleType/Observed_Example in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'link': {'name': 'link', 'required': True},
                        'reference': {'name': 'reference', 'required': True}}})

    reference: str = Field(default=..., description="""Identifier for a real-world example (e.g. CVE-2005-1951).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedExample']} })
    description: str = Field(default=..., description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })
    link: str = Field(default=..., description="""URL providing more information about the observed example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedExample']} })


class TaxonomyMapping(ConfiguredBaseModel):
    """
    A mapping from a CWE entry to an equivalent entry in an external taxonomy (TaxonomyMappingsType/Taxonomy_Mapping in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'taxonomy_name': {'name': 'taxonomy_name', 'required': True}}})

    taxonomy_name: TaxonomyName = Field(default=..., description="""Name of the external taxonomy to which the mapping is made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaxonomyMapping']} })
    entry_id: Optional[str] = Field(default=None, description="""ID of the entry in the external taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaxonomyMapping']} })
    entry_name: Optional[str] = Field(default=None, description="""Name of the entry in the external taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaxonomyMapping']} })
    mapping_fit: Optional[TaxonomyMappingFit] = Field(default=None, description="""How close the CWE entry is to the mapped taxonomy entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TaxonomyMapping']} })


class CatalogMember(ConfiguredBaseModel):
    """
    A Has_Member or Member_Of entry specifying a CWE ID and the View ID in which the membership holds (MemberType in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'cwe_id': {'name': 'cwe_id', 'required': True},
                        'view_id': {'name': 'view_id', 'required': True}}})

    cwe_id: int = Field(default=..., description="""Numeric CWE ID (foreign key in relationships and members).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'CatalogMember', 'MappingSuggestion']} })
    view_id: int = Field(default=..., description="""View ID within which a relationship or membership is relevant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'CatalogMember']} })


class Relationship(ConfiguredBaseModel):
    """
    Container for category membership relationships (RelationshipsType in XSD). Holds Has_Member and optionally Member_Of lists.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe'})

    has_member: Optional[list[CatalogMember]] = Field(default=None, description="""CWE entries that belong to this category or view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship']} })
    member_of: Optional[list[CatalogMember]] = Field(default=None, description="""Views or categories that this entry belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship']} })


class Audience(ConfiguredBaseModel):
    """
    A target stakeholder group for a CWE view or category (AudienceType/Stakeholder in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'type': {'description': 'Type of stakeholder in the CWE '
                                                'community.',
                                 'name': 'type',
                                 'range': 'StakeholderType',
                                 'required': True}}})

    type: StakeholderType = Field(default=..., description="""Type of stakeholder in the CWE community.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View', 'Audience', 'Note', 'Contribution']} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness',
                       'WeaknessOrdinality',
                       'AlternateTerm',
                       'DetectionMethod',
                       'PotentialMitigation',
                       'ObservedExample',
                       'Audience'],
         'exact_mappings': ['schema:description'],
         'slot_uri': 'dct:description'} })


class MappingNotes(ConfiguredBaseModel):
    """
    Guidance for when and whether to map an issue to a CWE entry (MappingNotesType in XSD). Required on every Weakness, Category, and View.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'comments': {'name': 'comments', 'required': True},
                        'rationale': {'name': 'rationale', 'required': True},
                        'reasons': {'name': 'reasons', 'required': True},
                        'usage': {'name': 'usage', 'required': True}}})

    usage: MappingUsage = Field(default=..., description="""Whether this CWE entry is supported for mapping.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingNotes']} })
    rationale: str = Field(default=..., description="""Context for the mapping usage designation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingNotes']} })
    comments: str = Field(default=..., description="""Further clarification for the mapping notes reader.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingNotes']} })
    reasons: list[MappingReason] = Field(default=..., description="""Vocabulary summary of the mapping usage recommendation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingNotes']} })
    suggestions: Optional[list[MappingSuggestion]] = Field(default=None, description="""Suggested alternative CWE entries for mapping.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingNotes']} })


class MappingSuggestion(ConfiguredBaseModel):
    """
    A suggested alternative CWE entry for mapping purposes (SuggestionsType/Suggestion in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'comment': {'name': 'comment', 'required': True},
                        'cwe_id': {'name': 'cwe_id', 'required': True}}})

    cwe_id: int = Field(default=..., description="""Numeric CWE ID (foreign key in relationships and members).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedWeakness', 'CatalogMember', 'MappingSuggestion']} })
    comment: str = Field(default=..., description="""Explanatory comment (e.g. on a mapping suggestion).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingSuggestion']} })


class Note(ConfiguredBaseModel):
    """
    Additional commentary about a CWE entry (NotesType/Note in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'type': {'description': 'Type of note (Maintenance, '
                                                'Terminology, Research Gap, etc.).',
                                 'name': 'type',
                                 'range': 'NoteType',
                                 'required': True}}})

    type: NoteType = Field(default=..., description="""Type of note (Maintenance, Terminology, Research Gap, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['View', 'Audience', 'Note', 'Contribution']} })
    content: Optional[str] = Field(default=None, description="""Textual content of a note.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExampleCode', 'Note']} })


class ContentHistory(ConfiguredBaseModel):
    """
    Tracks the original author and subsequent modifications (ContentHistoryType in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'submission': {'name': 'submission', 'required': True}}})

    submission: Submission = Field(default=..., description="""Initial submission information for this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentHistory']} })
    modifications: Optional[list[Modification]] = Field(default=None, description="""Ordered list of modifications made to this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentHistory']} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Contribution records for this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentHistory']} })
    previous_entry_names: Optional[list[PreviousEntryName]] = Field(default=None, description="""Previous names used for this entry before a substantive rename.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentHistory']} })


class Submission(ConfiguredBaseModel):
    """
    Initial submission record for a CWE entry (ContentHistoryType/Submission in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'submission_date': {'name': 'submission_date',
                                            'required': True},
                        'submission_release_date': {'name': 'submission_release_date',
                                                    'required': True},
                        'submission_version': {'name': 'submission_version',
                                               'required': True}}})

    submission_name: Optional[str] = Field(default=None, description="""Name of the person who submitted this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })
    submission_organization: Optional[str] = Field(default=None, description="""Organization of the submitter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })
    submission_date: date = Field(default=..., description="""Date on which this entry was submitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })
    submission_version: str = Field(default=..., description="""CWE version in which this entry was first added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })
    submission_release_date: date = Field(default=..., description="""Release date of the CWE version that added this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })
    submission_comment: Optional[str] = Field(default=None, description="""Optional comment related to the submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Submission']} })


class Modification(ConfiguredBaseModel):
    """
    A modification record documenting a change to a CWE entry (ContentHistoryType/Modification in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'modification_date': {'name': 'modification_date',
                                              'required': True}}})

    modification_name: Optional[str] = Field(default=None, description="""Name of the person who made the modification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_organization: Optional[str] = Field(default=None, description="""Organization of the modifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_date: date = Field(default=..., description="""Date on which the modification was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_version: Optional[str] = Field(default=None, description="""CWE version in which the modification first appeared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_release_date: Optional[date] = Field(default=None, description="""Release date of the CWE version containing the modification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_importance: Optional[ContentImportance] = Field(default=None, description="""Importance level of this modification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })
    modification_comment: Optional[str] = Field(default=None, description="""Comment describing what was changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Modification']} })


class Contribution(ConfiguredBaseModel):
    """
    A contribution record documenting donated content or feedback (ContentHistoryType/Contribution in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'contribution_date': {'name': 'contribution_date',
                                              'required': True},
                        'type': {'description': 'Whether the contribution was Content '
                                                'or Feedback.',
                                 'name': 'type',
                                 'range': 'ContributionType',
                                 'required': True}}})

    type: ContributionType = Field(default=..., description="""Whether the contribution was Content or Feedback.""", json_schema_extra = { "linkml_meta": {'domain_of': ['View', 'Audience', 'Note', 'Contribution']} })
    contribution_name: Optional[str] = Field(default=None, description="""Name of the contributor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })
    contribution_organization: Optional[str] = Field(default=None, description="""Organization of the contributor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })
    contribution_date: date = Field(default=..., description="""Date of the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })
    contribution_version: Optional[str] = Field(default=None, description="""CWE version in which the contribution first appeared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })
    contribution_release_date: Optional[date] = Field(default=None, description="""Release date of the CWE version containing the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })
    contribution_comment: Optional[str] = Field(default=None, description="""Comment related to the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution']} })


class PreviousEntryName(ConfiguredBaseModel):
    """
    A previous name used for a CWE entry before a substantive rename (ContentHistoryType/Previous_Entry_Name in XSD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cwe',
         'slot_usage': {'date': {'description': 'Date on which this name was last '
                                                'used.',
                                 'name': 'date',
                                 'required': True},
                        'name': {'description': 'The previous name of this CWE entry.',
                                 'name': 'name',
                                 'required': True},
                        'version': {'description': 'CWE version in which the name '
                                                   'change occurred.',
                                    'name': 'version'}}})

    name: str = Field(default=..., description="""The previous name of this CWE entry.""", json_schema_extra = { "linkml_meta": {'aliases': ['label'],
         'domain_of': ['WeaknessCatalog',
                       'Weakness',
                       'Category',
                       'View',
                       'LanguagePlatform',
                       'OSPlatform',
                       'ArchitecturePlatform',
                       'TechnologyPlatform',
                       'PreviousEntryName'],
         'slot_uri': 'rdfs:label'} })
    date: date = Field(default=..., description="""Date on which this name was last used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog', 'PreviousEntryName'], 'slot_uri': 'dct:date'} })
    version: Optional[str] = Field(default=None, description="""CWE version in which the name change occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaknessCatalog', 'OSPlatform', 'PreviousEntryName'],
         'slot_uri': 'schema:version'} })


class NVDWeaknessObservation(ConfiguredBaseModel):
    """
    Weakness observation from an NVD vulnerability detail page.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Mirrors the per-CVE weakness table rendered on NVD detail '
                      'pages.'],
         'from_schema': 'https://w3id.org/lmodel/cwe',
         'in_subset': ['nvd_weakness_observation'],
         'slot_usage': {'observation_id': {'identifier': True,
                                           'name': 'observation_id',
                                           'required': True},
                        'observed_in_cve': {'name': 'observed_in_cve',
                                            'required': True},
                        'reported_by': {'name': 'reported_by', 'required': True},
                        'weakness': {'name': 'weakness', 'required': True}}})

    observation_id: str = Field(default=..., description="""Identifier for an NVD weakness observation row.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDWeaknessObservation'], 'slot_uri': 'dct:identifier'} })
    observed_in_cve: str = Field(default=..., description="""CVE identifier where this weakness observation appears.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDWeaknessObservation'], 'slot_uri': 'dct:references'} })
    weakness: int = Field(default=..., description="""Referenced CWE entry for this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDWeaknessObservation'], 'slot_uri': 'schema:about'} })
    reported_by: WeaknessSource = Field(default=..., description="""Source label for the weakness row (e.g. NIST, ASSIGNER).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDWeaknessObservation'], 'slot_uri': 'dct:source'} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Weakness', 'NVDWeaknessObservation'], 'slot_uri': 'dct:source'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
WeaknessCatalog.model_rebuild()
Weakness.model_rebuild()
Category.model_rebuild()
View.model_rebuild()
ExternalReference.model_rebuild()
CWEReference.model_rebuild()
RelatedWeakness.model_rebuild()
WeaknessOrdinality.model_rebuild()
ApplicablePlatforms.model_rebuild()
LanguagePlatform.model_rebuild()
OSPlatform.model_rebuild()
ArchitecturePlatform.model_rebuild()
TechnologyPlatform.model_rebuild()
AlternateTerm.model_rebuild()
ModeOfIntroduction.model_rebuild()
CommonConsequence.model_rebuild()
DetectionMethod.model_rebuild()
PotentialMitigation.model_rebuild()
DemonstrativeExample.model_rebuild()
ExampleCode.model_rebuild()
ObservedExample.model_rebuild()
TaxonomyMapping.model_rebuild()
CatalogMember.model_rebuild()
Relationship.model_rebuild()
Audience.model_rebuild()
MappingNotes.model_rebuild()
MappingSuggestion.model_rebuild()
Note.model_rebuild()
ContentHistory.model_rebuild()
Submission.model_rebuild()
Modification.model_rebuild()
Contribution.model_rebuild()
PreviousEntryName.model_rebuild()
NVDWeaknessObservation.model_rebuild()
