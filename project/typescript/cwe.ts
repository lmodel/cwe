export type WeaknessCatalogName = string;
export type WeaknessId = string;
export type CategoryId = string;
export type ViewId = string;
export type ExternalReferenceReferenceId = string;
export type NVDWeaknessObservationObservationId = string;
/**
* Source attribution for weakness data in NVD/CVE contexts.
*/
export enum WeaknessSource {
    
    /** Data sourced from MITRE CWE content. */
    MITRE = "MITRE",
    /** Data produced by NIST/NVD analysis. */
    NIST = "NIST",
    /** Data provided by the CVE assigner/CNA. */
    ASSIGNER = "ASSIGNER",
    /** Data provided by a CVE Numbering Authority. */
    CNA = "CNA",
    /** Other or unspecified source. */
    OTHER = "OTHER",
};
/**
* CWE abstraction layer (AbstractionEnumeration in XSD).
*/
export enum WeaknessAbstraction {
    
    /** Most abstract type; a theme for all class/base/variant weaknesses. */
    PILLAR = "PILLAR",
    /** Abstract, independent of any specific language or technology. */
    CLASS = "CLASS",
    /** Mostly independent of resource or technology; supports detection/prevention. */
    BASE = "BASE",
    /** Linked to a specific language or technology. */
    VARIANT = "VARIANT",
    /** Meaningful aggregation — Chain or Composite. */
    COMPOUND = "COMPOUND",
};
/**
* Lifecycle status of a CWE entry, category, or view (StatusEnumeration in XSD).
*/
export enum WeaknessStatus {
    
    /** Removed from CWE; likely a duplicate or created in error. */
    DEPRECATED = "DEPRECATED",
    /** All important elements filled; may still have problems or gaps. */
    DRAFT = "DRAFT",
    /** Not all important elements filled; quality not guaranteed. */
    INCOMPLETE = "INCOMPLETE",
    /** Still valid but no longer relevant; likely superseded. */
    OBSOLETE = "OBSOLETE",
    /** All important elements verified; unlikely to change significantly. */
    STABLE = "STABLE",
    /** Has received close extensive review; critical elements verified. */
    USABLE = "USABLE",
};
/**
* Structural nature of a weakness (StructureEnumeration in XSD).
*/
export enum WeaknessStructure {
    
    /** Single weakness whose exploitation is not dependent on another weakness. */
    SIMPLE = "SIMPLE",
    /** Set of weaknesses reachable consecutively to produce a vulnerability. */
    CHAIN = "CHAIN",
    /** Set of weaknesses that must all be present simultaneously. */
    COMPOSITE = "COMPOSITE",
};
/**
* Likelihood of exploitation or occurrence (LikelihoodEnumeration in XSD).
*/
export enum LikelihoodLevel {
    
    HIGH = "HIGH",
    MEDIUM = "MEDIUM",
    LOW = "LOW",
    /** Actual likelihood is not known. */
    UNKNOWN = "UNKNOWN",
};
/**
* Nature of a directional relationship between two CWE entries (RelatedNatureEnumeration in XSD).
*/
export enum WeaknessRelationNature {
    
    /** Related weakness at a higher level of abstraction. */
    CHILD_OF = "CHILD_OF",
    /** Related weakness at a lower level of abstraction. */
    PARENT_OF = "PARENT_OF",
    /** Chaining; this weakness starts the chain. */
    STARTS_WITH = "STARTS_WITH",
    /** Chaining; this weakness can follow the target. */
    CAN_FOLLOW = "CAN_FOLLOW",
    /** Chaining; this weakness can precede the target. */
    CAN_PRECEDE = "CAN_PRECEDE",
    /** Composite; this weakness is required by the target. */
    REQUIRED_BY = "REQUIRED_BY",
    /** Composite; this weakness requires the target. */
    REQUIRES = "REQUIRES",
    /** In proper context can also be perceived as the target weakness. */
    CAN_ALSO_BE = "CAN_ALSO_BE",
    /** Shows similarity with the target; no precise fit elsewhere. */
    PEER_OF = "PEER_OF",
};
/**
* Potential ordering relationship of a weakness relative to others (OrdinalityEnumeration in XSD).
*/
export enum WeaknessOrdinalityLevel {
    
    /** Weakness exists independent of other weaknesses. */
    PRIMARY = "PRIMARY",
    /** Weakness exists only in the presence of other weaknesses. */
    RESULTANT = "RESULTANT",
    /** Does not directly lead to security weaknesses but may facilitate them. */
    INDIRECT = "INDIRECT",
};
/**
* Marks a related-weakness relationship as the primary one for a given <Nature, CWE_ID, View_ID> triple (OrdinalEnumeration in XSD).
*/
export enum OrdinalQualifier {
    
    /** Primary ChildOf relationship for this weakness in the given view. */
    PRIMARY = "PRIMARY",
};
/**
* Security property area that can be violated by exploiting a weakness (ScopeEnumeration in XSD).
*/
export enum SecurityScope {
    
    CONFIDENTIALITY = "CONFIDENTIALITY",
    INTEGRITY = "INTEGRITY",
    AVAILABILITY = "AVAILABILITY",
    ACCESS_CONTROL = "ACCESS_CONTROL",
    ACCOUNTABILITY = "ACCOUNTABILITY",
    AUTHENTICATION = "AUTHENTICATION",
    AUTHORIZATION = "AUTHORIZATION",
    NON_REPUDIATION = "NON_REPUDIATION",
    OTHER = "OTHER",
};
/**
* Technical impact of successfully exploiting a weakness (TechnicalImpactEnumeration in XSD).
*/
export enum TechnicalImpact {
    
    MODIFY_MEMORY = "MODIFY_MEMORY",
    READ_MEMORY = "READ_MEMORY",
    MODIFY_FILES_OR_DIRECTORIES = "MODIFY_FILES_OR_DIRECTORIES",
    READ_FILES_OR_DIRECTORIES = "READ_FILES_OR_DIRECTORIES",
    MODIFY_APPLICATION_DATA = "MODIFY_APPLICATION_DATA",
    READ_APPLICATION_DATA = "READ_APPLICATION_DATA",
    /** DoS: Crash, Exit, or Restart */
    DOS_CRASH_EXIT_OR_RESTART = "DOS_CRASH_EXIT_OR_RESTART",
    /** DoS: Amplification */
    DOS_AMPLIFICATION = "DOS_AMPLIFICATION",
    /** DoS: Instability */
    DOS_INSTABILITY = "DOS_INSTABILITY",
    /** DoS: Resource Consumption (CPU) */
    DOS_RESOURCE_CONSUMPTION_CPU = "DOS_RESOURCE_CONSUMPTION_CPU",
    /** DoS: Resource Consumption (Memory) */
    DOS_RESOURCE_CONSUMPTION_MEMORY = "DOS_RESOURCE_CONSUMPTION_MEMORY",
    /** DoS: Resource Consumption (Other) */
    DOS_RESOURCE_CONSUMPTION_OTHER = "DOS_RESOURCE_CONSUMPTION_OTHER",
    EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS = "EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS",
    GAIN_PRIVILEGES_OR_ASSUME_IDENTITY = "GAIN_PRIVILEGES_OR_ASSUME_IDENTITY",
    BYPASS_PROTECTION_MECHANISM = "BYPASS_PROTECTION_MECHANISM",
    HIDE_ACTIVITIES = "HIDE_ACTIVITIES",
    ALTER_EXECUTION_LOGIC = "ALTER_EXECUTION_LOGIC",
    QUALITY_DEGRADATION = "QUALITY_DEGRADATION",
    UNEXPECTED_STATE = "UNEXPECTED_STATE",
    VARIES_BY_CONTEXT = "VARIES_BY_CONTEXT",
    /** Makes vulnerability harder to find and fix. */
    INCREASE_ANALYTICAL_COMPLEXITY = "INCREASE_ANALYTICAL_COMPLEXITY",
    REDUCE_MAINTAINABILITY = "REDUCE_MAINTAINABILITY",
    REDUCE_PERFORMANCE = "REDUCE_PERFORMANCE",
    REDUCE_RELIABILITY = "REDUCE_RELIABILITY",
    OTHER = "OTHER",
};
/**
* Phase in the product lifecycle where a weakness may be introduced or a mitigation applied (PhaseEnumeration in XSD).
*/
export enum LifecyclePhase {
    
    POLICY = "POLICY",
    REQUIREMENTS = "REQUIREMENTS",
    ARCHITECTURE_AND_DESIGN = "ARCHITECTURE_AND_DESIGN",
    IMPLEMENTATION = "IMPLEMENTATION",
    BUILD_AND_COMPILATION = "BUILD_AND_COMPILATION",
    TESTING = "TESTING",
    DOCUMENTATION = "DOCUMENTATION",
    BUNDLING = "BUNDLING",
    DISTRIBUTION = "DISTRIBUTION",
    INSTALLATION = "INSTALLATION",
    SYSTEM_CONFIGURATION = "SYSTEM_CONFIGURATION",
    OPERATION = "OPERATION",
    PATCHING_AND_MAINTENANCE = "PATCHING_AND_MAINTENANCE",
    PORTING = "PORTING",
    INTEGRATION = "INTEGRATION",
    MANUFACTURING = "MANUFACTURING",
    DECOMMISSIONING_AND_END_OF_LIFE = "DECOMMISSIONING_AND_END_OF_LIFE",
};
/**
* General strategy for protecting a system (MitigationStrategyEnumeration in XSD).
*/
export enum MitigationStrategy {
    
    ATTACK_SURFACE_REDUCTION = "ATTACK_SURFACE_REDUCTION",
    COMPILATION_OR_BUILD_HARDENING = "COMPILATION_OR_BUILD_HARDENING",
    ENFORCEMENT_BY_CONVERSION = "ENFORCEMENT_BY_CONVERSION",
    ENVIRONMENT_HARDENING = "ENVIRONMENT_HARDENING",
    FIREWALL = "FIREWALL",
    INPUT_VALIDATION = "INPUT_VALIDATION",
    LANGUAGE_SELECTION = "LANGUAGE_SELECTION",
    LIBRARIES_OR_FRAMEWORKS = "LIBRARIES_OR_FRAMEWORKS",
    RESOURCE_LIMITATION = "RESOURCE_LIMITATION",
    OUTPUT_ENCODING = "OUTPUT_ENCODING",
    PARAMETERIZATION = "PARAMETERIZATION",
    REFACTORING = "REFACTORING",
    SANDBOX_OR_JAIL = "SANDBOX_OR_JAIL",
    SEPARATION_OF_PRIVILEGE = "SEPARATION_OF_PRIVILEGE",
};
/**
* Method that may be employed to detect a weakness (DetectionMethodEnumeration in XSD).
*/
export enum DetectionMethodType {
    
    AUTOMATED_ANALYSIS = "AUTOMATED_ANALYSIS",
    AUTOMATED_DYNAMIC_ANALYSIS = "AUTOMATED_DYNAMIC_ANALYSIS",
    AUTOMATED_STATIC_ANALYSIS = "AUTOMATED_STATIC_ANALYSIS",
    /** Automated Static Analysis - Source Code */
    AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE = "AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE",
    /** Automated Static Analysis - Binary or Bytecode */
    AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE = "AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
    FUZZING = "FUZZING",
    MANUAL_ANALYSIS = "MANUAL_ANALYSIS",
    MANUAL_DYNAMIC_ANALYSIS = "MANUAL_DYNAMIC_ANALYSIS",
    MANUAL_STATIC_ANALYSIS = "MANUAL_STATIC_ANALYSIS",
    /** Manual Static Analysis - Source Code */
    MANUAL_STATIC_ANALYSIS_SOURCE_CODE = "MANUAL_STATIC_ANALYSIS_SOURCE_CODE",
    /** Manual Static Analysis - Binary or Bytecode */
    MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE = "MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
    WHITE_BOX = "WHITE_BOX",
    BLACK_BOX = "BLACK_BOX",
    ARCHITECTURE_OR_DESIGN_REVIEW = "ARCHITECTURE_OR_DESIGN_REVIEW",
    DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION = "DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION",
    DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION = "DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION",
    FORMAL_VERIFICATION = "FORMAL_VERIFICATION",
    SIMULATION_EMULATION = "SIMULATION_EMULATION",
    OTHER = "OTHER",
};
/**
* Effectiveness of a detection method (DetectionEffectivenessEnumeration in XSD).
*/
export enum DetectionEffectiveness {
    
    /** Succeeds frequently; few false reports. */
    HIGH = "HIGH",
    /** Applicable broadly but may lack complete coverage. */
    MODERATE = "MODERATE",
    /** Cost-effective for partial coverage per IATAC SOAR report. */
    SOAR_PARTIAL = "SOAR_PARTIAL",
    /** May succeed by chance rather than reliably. */
    OPPORTUNISTIC = "OPPORTUNISTIC",
    /** Useful in limited circumstances. */
    LIMITED = "LIMITED",
    /** Highly unlikely to work. */
    NONE = "NONE",
};
/**
* Effectiveness of a potential mitigation (EffectivenessEnumeration in XSD).
*/
export enum MitigationEffectiveness {
    
    /** Frequently eliminates the weakness entirely. */
    HIGH = "HIGH",
    /** Prevents multiple forms but lacks complete coverage. */
    MODERATE = "MODERATE",
    /** Useful in limited circumstances. */
    LIMITED = "LIMITED",
    /** Generally not effective; only protects by chance. */
    INCIDENTAL = "INCIDENTAL",
    /** Minimizes impact rather than preventing the weakness. */
    DEFENSE_IN_DEPTH = "DEFENSE_IN_DEPTH",
    /** Commonly attempted but known to be ineffective or risky. */
    DISCOURAGED_COMMON_PRACTICE = "DISCOURAGED_COMMON_PRACTICE",
    NONE = "NONE",
};
/**
* Type of note on a CWE entry (NoteTypeEnumeration in XSD).
*/
export enum NoteType {
    
    APPLICABLE_PLATFORM = "APPLICABLE_PLATFORM",
    MAINTENANCE = "MAINTENANCE",
    RELATIONSHIP = "RELATIONSHIP",
    RESEARCH_GAP = "RESEARCH_GAP",
    TERMINOLOGY = "TERMINOLOGY",
    THEORETICAL = "THEORETICAL",
    OTHER = "OTHER",
};
/**
* Type of CWE view (ViewTypeEnumeration in XSD).
*/
export enum CWEViewType {
    
    /** Hierarchical representation from a specific vantage point. */
    GRAPH = "GRAPH",
    /** Flat list related through an external factor (e.g. Top-N list). */
    EXPLICIT = "EXPLICIT",
    /** Subset identified by an XSL filter expression. */
    IMPLICIT = "IMPLICIT",
};
/**
* Functional area where a weakness is most likely to occur (FunctionalAreaEnumeration in XSD).
*/
export enum FunctionalArea {
    
    AUTHENTICATION = "AUTHENTICATION",
    AUTHORIZATION = "AUTHORIZATION",
    CODE_LIBRARIES = "CODE_LIBRARIES",
    COUNTERS = "COUNTERS",
    CRYPTOGRAPHY = "CRYPTOGRAPHY",
    ERROR_HANDLING = "ERROR_HANDLING",
    INTERPROCESS_COMMUNICATION = "INTERPROCESS_COMMUNICATION",
    FILE_PROCESSING = "FILE_PROCESSING",
    LOGGING = "LOGGING",
    MEMORY_MANAGEMENT = "MEMORY_MANAGEMENT",
    NETWORKING = "NETWORKING",
    NUMBER_PROCESSING = "NUMBER_PROCESSING",
    PROGRAM_INVOCATION = "PROGRAM_INVOCATION",
    PROTECTION_MECHANISM = "PROTECTION_MECHANISM",
    SESSION_MANAGEMENT = "SESSION_MANAGEMENT",
    SIGNALS = "SIGNALS",
    STRING_PROCESSING = "STRING_PROCESSING",
    NOT_FUNCTIONAL_AREA_SPECIFIC = "NOT_FUNCTIONAL_AREA_SPECIFIC",
    POWER = "POWER",
    CLOCK = "CLOCK",
};
/**
* System resource that can be affected by exploiting a weakness (ResourceEnumeration in XSD).
*/
export enum AffectedResource {
    
    CPU = "CPU",
    FILE_OR_DIRECTORY = "FILE_OR_DIRECTORY",
    MEMORY = "MEMORY",
    SYSTEM_PROCESS = "SYSTEM_PROCESS",
    OTHER = "OTHER",
};
/**
* Regularity with which a weakness applies to a given platform (PrevalenceEnumeration in XSD).
*/
export enum PlatformPrevalence {
    
    OFTEN = "OFTEN",
    SOMETIMES = "SOMETIMES",
    RARELY = "RARELY",
    UNDETERMINED = "UNDETERMINED",
};
/**
* Source code language or data format (LanguageNameEnumeration in XSD).
*/
export enum ProgrammingLanguage {
    
    ADA = "ADA",
    ARM_ASSEMBLY = "ARM_ASSEMBLY",
    ASP = "ASP",
    ASP_DOT_NET = "ASP_DOT_NET",
    BASIC = "BASIC",
    C = "C",
    C_PLUS_PLUS = "C_PLUS_PLUS",
    C_SHARP = "C_SHARP",
    COBOL = "COBOL",
    FORTRAN = "FORTRAN",
    FSHARP = "FSHARP",
    GO = "GO",
    HTML = "HTML",
    JAVA = "JAVA",
    JAVASCRIPT = "JAVASCRIPT",
    JSON = "JSON",
    JSP = "JSP",
    OBJECTIVE_C = "OBJECTIVE_C",
    PASCAL = "PASCAL",
    PERL = "PERL",
    PHP = "PHP",
    PSEUDOCODE = "PSEUDOCODE",
    PYTHON = "PYTHON",
    RUBY = "RUBY",
    RUST = "RUST",
    SHELL = "SHELL",
    SQL = "SQL",
    SWIFT = "SWIFT",
    VB_DOT_NET = "VB_DOT_NET",
    VERILOG = "VERILOG",
    VHDL = "VHDL",
    XML = "XML",
    X86_ASSEMBLY = "X86_ASSEMBLY",
    OTHER = "OTHER",
};
/**
* Class of programming language (LanguageClassEnumeration in XSD).
*/
export enum LanguageClass {
    
    ASSEMBLY = "ASSEMBLY",
    COMPILED = "COMPILED",
    HARDWARE_DESCRIPTION_LANGUAGE = "HARDWARE_DESCRIPTION_LANGUAGE",
    INTERPRETED = "INTERPRETED",
    OBJECT_ORIENTED = "OBJECT_ORIENTED",
    MEMORY_UNSAFE = "MEMORY_UNSAFE",
    NOT_LANGUAGE_SPECIFIC = "NOT_LANGUAGE_SPECIFIC",
};
/**
* Processor architecture (ArchitectureNameEnumeration in XSD).
*/
export enum ArchitectureName {
    
    ALPHA = "ALPHA",
    ARM = "ARM",
    ITANIUM = "ITANIUM",
    POWER_ARCHITECTURE = "POWER_ARCHITECTURE",
    SPARC = "SPARC",
    X86 = "X86",
    OTHER = "OTHER",
};
/**
* Class of processor architecture (ArchitectureClassEnumeration in XSD).
*/
export enum ArchitectureClass {
    
    EMBEDDED = "EMBEDDED",
    MICROCOMPUTER = "MICROCOMPUTER",
    WORKSTATION = "WORKSTATION",
    NOT_ARCHITECTURE_SPECIFIC = "NOT_ARCHITECTURE_SPECIFIC",
};
/**
* Operating system (OperatingSystemNameEnumeration in XSD).
*/
export enum OperatingSystemName {
    
    AIX = "AIX",
    ANDROID = "ANDROID",
    BLACKBERRY_OS = "BLACKBERRY_OS",
    CHROME_OS = "CHROME_OS",
    DARWIN = "DARWIN",
    FREEBSD = "FREEBSD",
    IOS = "IOS",
    MACOS = "MACOS",
    NETBSD = "NETBSD",
    OPENBSD = "OPENBSD",
    RED_HAT = "RED_HAT",
    SOLARIS = "SOLARIS",
    SUSE = "SUSE",
    TVOS = "TVOS",
    UBUNTU = "UBUNTU",
    WATCHOS = "WATCHOS",
    WINDOWS_9X = "WINDOWS_9X",
    WINDOWS_EMBEDDED = "WINDOWS_EMBEDDED",
    WINDOWS_NT = "WINDOWS_NT",
};
/**
* Class of operating system (OperatingSystemClassEnumeration in XSD).
*/
export enum OperatingSystemClass {
    
    LINUX = "LINUX",
    MACOS = "MACOS",
    UNIX = "UNIX",
    WINDOWS = "WINDOWS",
    NOT_OS_SPECIFIC = "NOT_OS_SPECIFIC",
};
/**
* Specific technology applicable to a weakness (TechnologyNameEnumeration in XSD).
*/
export enum TechnologyName {
    
    AI_ML = "AI_ML",
    WEB_SERVER = "WEB_SERVER",
    DATABASE_SERVER = "DATABASE_SERVER",
    ACCELERATOR_HARDWARE = "ACCELERATOR_HARDWARE",
    ANALOG_AND_MIXED_SIGNAL_HARDWARE = "ANALOG_AND_MIXED_SIGNAL_HARDWARE",
    AUDIO_VIDEO_HARDWARE = "AUDIO_VIDEO_HARDWARE",
    BUS_INTERFACE_HARDWARE = "BUS_INTERFACE_HARDWARE",
    CLOCK_COUNTER_HARDWARE = "CLOCK_COUNTER_HARDWARE",
    COMMUNICATION_HARDWARE = "COMMUNICATION_HARDWARE",
    CONTROLLER_HARDWARE = "CONTROLLER_HARDWARE",
    MEMORY_HARDWARE = "MEMORY_HARDWARE",
    MICROCONTROLLER_HARDWARE = "MICROCONTROLLER_HARDWARE",
    NETWORK_ON_CHIP_HARDWARE = "NETWORK_ON_CHIP_HARDWARE",
    POWER_MANAGEMENT_HARDWARE = "POWER_MANAGEMENT_HARDWARE",
    PROCESSOR_HARDWARE = "PROCESSOR_HARDWARE",
    SECURITY_HARDWARE = "SECURITY_HARDWARE",
    SENSOR_HARDWARE = "SENSOR_HARDWARE",
    STORAGE_HARDWARE = "STORAGE_HARDWARE",
    TEST_DEBUG_HARDWARE = "TEST_DEBUG_HARDWARE",
    OTHER = "OTHER",
};
/**
* Class of technology (TechnologyClassEnumeration in XSD).
*/
export enum TechnologyClass {
    
    CLIENT_SERVER = "CLIENT_SERVER",
    CLOUD_COMPUTING = "CLOUD_COMPUTING",
    ICS_OT = "ICS_OT",
    MAINFRAME = "MAINFRAME",
    MOBILE = "MOBILE",
    N_TIER = "N_TIER",
    SOA = "SOA",
    SYSTEM_ON_CHIP = "SYSTEM_ON_CHIP",
    WEB_BASED = "WEB_BASED",
    NOT_TECHNOLOGY_SPECIFIC = "NOT_TECHNOLOGY_SPECIFIC",
};
/**
* Closeness of a mapping to an external taxonomy (TaxonomyMappingFitEnumeration in XSD).
*/
export enum TaxonomyMappingFit {
    
    EXACT = "EXACT",
    CWE_MORE_ABSTRACT = "CWE_MORE_ABSTRACT",
    CWE_MORE_SPECIFIC = "CWE_MORE_SPECIFIC",
    IMPRECISE = "IMPRECISE",
    PERSPECTIVE = "PERSPECTIVE",
};
/**
* Known taxonomy that can be mapped to CWE (TaxonomyNameEnumeration in XSD).
*/
export enum TaxonomyName {
    
    SEVEN_PERNICIOUS_KINGDOMS = "SEVEN_PERNICIOUS_KINGDOMS",
    NINETEEN_DEADLY_SINS = "NINETEEN_DEADLY_SINS",
    ASLAM = "ASLAM",
    BISHOP = "BISHOP",
    CERT_C_SECURE_CODING = "CERT_C_SECURE_CODING",
    CERT_CPP_SECURE_CODING = "CERT_CPP_SECURE_CODING",
    THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011 = "THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011",
    CLASP = "CLASP",
    ISA_IEC_62443 = "ISA_IEC_62443",
    LANDWEHR = "LANDWEHR",
    OMG_ASCSM = "OMG_ASCSM",
    OMG_ASCRM = "OMG_ASCRM",
    OMG_ASCMM = "OMG_ASCMM",
    OMG_ASCPEM = "OMG_ASCPEM",
    OWASP_TOP_TEN_2004 = "OWASP_TOP_TEN_2004",
    OWASP_TOP_TEN_2007 = "OWASP_TOP_TEN_2007",
    OWASP_TOP_TEN = "OWASP_TOP_TEN",
    PLOVER = "PLOVER",
    PROTECTION_ANALYSIS = "PROTECTION_ANALYSIS",
    RISOS = "RISOS",
    SEI_CERT_C_CODING_STANDARD = "SEI_CERT_C_CODING_STANDARD",
    SEI_CERT_CPP_CODING_STANDARD = "SEI_CERT_CPP_CODING_STANDARD",
    SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA = "SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA",
    SEI_CERT_PERL_CODING_STANDARD = "SEI_CERT_PERL_CODING_STANDARD",
    SOFTWARE_FAULT_PATTERNS = "SOFTWARE_FAULT_PATTERNS",
    WEBER_KARGER_PARADKAR = "WEBER_KARGER_PARADKAR",
    WASC = "WASC",
};
/**
* Whether a CWE entry should be used for mapping (UsageEnumeration in XSD).
*/
export enum MappingUsage {
    
    /** May be used to map to real-world vulnerabilities. */
    ALLOWED = "ALLOWED",
    /** May be used in limited situations requiring careful review. */
    ALLOWED_WITH_REVIEW = "ALLOWED_WITH_REVIEW",
    /** Should not be used for mapping. */
    DISCOURAGED = "DISCOURAGED",
    /** Must not be used for mapping. */
    PROHIBITED = "PROHIBITED",
};
/**
* Reason why a CWE entry should not be used for mapping (ReasonEnumeration in XSD).
*/
export enum MappingReason {
    
    ABSTRACTION = "ABSTRACTION",
    CATEGORY = "CATEGORY",
    VIEW = "VIEW",
    DEPRECATED = "DEPRECATED",
    POTENTIAL_DEPRECATION = "POTENTIAL_DEPRECATION",
    FREQUENT_MISUSE = "FREQUENT_MISUSE",
    FREQUENT_MISINTERPRETATION = "FREQUENT_MISINTERPRETATION",
    MULTIPLE_USE = "MULTIPLE_USE",
    CWE_OVERLAP = "CWE_OVERLAP",
    ACCEPTABLE_USE = "ACCEPTABLE_USE",
    POTENTIAL_MAJOR_CHANGES = "POTENTIAL_MAJOR_CHANGES",
    OTHER = "OTHER",
};
/**
* Type of stakeholder in the CWE community (StakeholderEnumeration in XSD).
*/
export enum StakeholderType {
    
    ACADEMIC_RESEARCHERS = "ACADEMIC_RESEARCHERS",
    APPLIED_RESEARCHERS = "APPLIED_RESEARCHERS",
    ASSESSMENT_TEAMS = "ASSESSMENT_TEAMS",
    ASSESSMENT_TOOL_VENDORS = "ASSESSMENT_TOOL_VENDORS",
    CWE_TEAM = "CWE_TEAM",
    EDUCATORS = "EDUCATORS",
    HARDWARE_DESIGNERS = "HARDWARE_DESIGNERS",
    INFORMATION_PROVIDERS = "INFORMATION_PROVIDERS",
    PRODUCT_CUSTOMERS = "PRODUCT_CUSTOMERS",
    PRODUCT_VENDORS = "PRODUCT_VENDORS",
    SOFTWARE_DEVELOPERS = "SOFTWARE_DEVELOPERS",
    VULNERABILITY_ANALYSTS = "VULNERABILITY_ANALYSTS",
    OTHER = "OTHER",
};
/**
* Nature of a code snippet in a demonstrative example (StructuredCodeNatureEnumeration in XSD).
*/
export enum CodeNature {
    
    ATTACK = "ATTACK",
    BAD = "BAD",
    GOOD = "GOOD",
    INFORMATIVE = "INFORMATIVE",
    MITIGATION = "MITIGATION",
    RESULT = "RESULT",
};
/**
* Importance level of a content modification (ImportanceEnumeration in XSD).
*/
export enum ContentImportance {
    
    NORMAL = "NORMAL",
    /** Changes the meaning or interpretation of the entry. */
    CRITICAL = "CRITICAL",
};
/**
* Whether a contribution was donated content or general feedback.
*/
export enum ContributionType {
    
    /** Content donated to the CWE entry. */
    CONTENT = "CONTENT",
    /** General feedback given about the CWE entry. */
    FEEDBACK = "FEEDBACK",
};


/**
 * Top-level container for a CWE catalog snapshot (Weakness_Catalog in XSD). Holds weakness entries, categories, views, external references, and NVD weakness observations.
 */
export interface WeaknessCatalog {
    /** Short human-readable name or title for this entity. */
    name: string,
    /** Version string of the catalog, entry, or submission. */
    version: string,
    /** Date associated with a catalog snapshot or a name-change event. */
    date: date,
    /** Canonical CWE weakness entries in this catalog snapshot. */
    weaknesses?: WeaknessId[],
    /** CWE categories grouping weaknesses by a common characteristic. */
    categories?: Category[],
    /** CWE views providing different perspectives on the catalog. */
    views?: ViewId[],
    /** External references shared across CWE entries in this catalog. */
    external_references?: ExternalReference[],
    /** Weakness observations from NVD vulnerability detail pages. */
    observations?: NVDWeaknessObservationObservationId[],
}


/**
 * Canonical CWE weakness record (WeaknessType in XSD). Describes a specific type of weakness and the full set of associated information.
 */
export interface Weakness {
    /** Unique numeric identifier for the CWE entry, category, or view. */
    id: number,
    /** Short human-readable name or title for this entity. */
    name: string,
    /** Narrative description of the entity. */
    description: string,
    /** Extended description providing additional details beyond the core concept. */
    extended_description?: string,
    /** CWE abstraction tier (e.g. Base or Variant). */
    abstraction: string,
    /** Structural nature of the weakness (Simple, Chain, or Composite). */
    structure: string,
    /** Lifecycle status of the CWE entry, category, or view. */
    status: string,
    /** Optional diagram filename or reference associated with the entry. */
    diagram?: string,
    /** Potential ordering relationships of this weakness with others. */
    weakness_ordinalities?: WeaknessOrdinality[],
    /** Languages, OS, architectures, and technologies where this weakness can appear. */
    applicable_platforms?: ApplicablePlatforms,
    /** Background information relevant but not describing the weakness itself. */
    background_details?: string[],
    /** Other names by which this weakness is known. */
    alternate_terms?: AlternateTerm[],
    /** Information about how and when this weakness may be introduced. */
    modes_of_introduction?: ModeOfIntroduction[],
    /** Conditions that could increase the likelihood of exploit. */
    exploitation_factors?: string[],
    /** Qualitative likelihood that the weakness can be exploited. */
    likelihood_of_exploit?: string,
    /** Individual consequences associated with this weakness. */
    common_consequences?: CommonConsequence[],
    /** Methods that may be employed to detect this weakness. */
    detection_methods?: DetectionMethod[],
    /** Potential mitigations associated with this weakness. */
    potential_mitigations?: PotentialMitigation[],
    /** Code examples illustrating how this weakness may appear. */
    demonstrative_examples?: DemonstrativeExample[],
    /** Real-world instances of this weakness. */
    observed_examples?: ObservedExample[],
    /** Functional areas in which this weakness is most likely to occur. */
    functional_areas?: string,
    /** System resources that can be affected by exploiting this weakness. */
    affected_resources?: string,
    /** Mappings to equivalent entries in external taxonomies. */
    taxonomy_mappings?: TaxonomyMapping[],
    /** CAPEC identifiers of attack patterns associated with this weakness. */
    related_attack_patterns?: number[],
    /** Typed relationships to other CWE entries. */
    related_weaknesses?: RelatedWeakness[],
    /** Links to external references defined in the catalog. */
    references?: CWEReference[],
    /** Guidance for when and whether to map an issue to this entry. */
    mapping_notes: MappingNotes,
    /** Additional comments about this entry. */
    notes?: Note[],
    /** Tracks the original author and subsequent modifications. */
    content_history: ContentHistory,
    /** Free-form tags for grouping and downstream filtering. */
    tags?: string[],
    /** Source or origin of the data. */
    source?: string,
}


/**
 * A collection of weaknesses grouped by a shared characteristic (CategoryType in XSD). Organizational mechanism only; not for mapping.
 */
export interface Category {
    /** Unique numeric identifier for the CWE entry, category, or view. */
    id: number,
    /** Short human-readable name or title for this entity. */
    name: string,
    /** Lifecycle status of the CWE entry, category, or view. */
    status: string,
    /** Key points that define a category. */
    summary: string,
    /** Membership relationships for a CWE category. */
    relationships?: Relationship,
    /** Mappings to equivalent entries in external taxonomies. */
    taxonomy_mappings?: TaxonomyMapping[],
    /** Links to external references defined in the catalog. */
    references?: CWEReference[],
    /** Guidance for when and whether to map an issue to this entry. */
    mapping_notes: MappingNotes,
    /** Additional comments about this entry. */
    notes?: Note[],
    /** Tracks the original author and subsequent modifications. */
    content_history: ContentHistory,
}


/**
 * A perspective from which to look at weaknesses in the catalog (ViewType in XSD). Types: Graph, Explicit slice, Implicit slice.
 */
export interface View {
    /** Unique numeric identifier for the CWE entry, category, or view. */
    id: number,
    /** Short human-readable name or title for this entity. */
    name: string,
    /** Type of view (Graph, Explicit, or Implicit). */
    type: string,
    /** Lifecycle status of the CWE entry, category, or view. */
    status: string,
    /** Perspective from which a view has been constructed. */
    objective: string,
    /** Target stakeholder groups for this view or category. */
    audience?: Audience[],
    /** Member entries for a CWE view. */
    members?: CatalogMember[],
    /** XSL query identifying members of an implicit slice view. */
    filter?: string,
    /** Links to external references defined in the catalog. */
    references?: CWEReference[],
    /** Guidance for when and whether to map an issue to this entry. */
    mapping_notes: MappingNotes,
    /** Additional comments about this entry. */
    notes?: Note[],
    /** Tracks the original author and subsequent modifications. */
    content_history: ContentHistory,
}


/**
 * Pointer to external reading material shared across CWE entries (ExternalReferenceType in XSD). Identified by Reference_ID (e.g. REF-1).
 */
export interface ExternalReference {
    /** Globally unique identifier for an external reference (e.g. REF-1). */
    reference_id: string,
    /** Descriptive title for a reference or catalog element. */
    title: string,
    /** Authors of the referenced material. */
    authors?: string[],
    /** Edition of the material being referenced. */
    edition?: string,
    /** Name of the magazine or journal. */
    publication?: string,
    /** Year of publication in YYYY format. */
    publication_year?: string,
    /** Month of publication in --MM format. */
    publication_month?: string,
    /** Day of publication in ---DD format. */
    publication_day?: string,
    /** Publisher of the referenced material. */
    publisher?: string,
    /** URL pointing to the reference resource. */
    url?: string,
    /** Date when the URL was last validated to exist. */
    url_date?: date,
}


/**
 * Link from a CWE entry to an ExternalReference in the catalog (ReferencesType/Reference in XSD).
 */
export interface CWEReference {
    /** Identifier of the ExternalReference being linked to (e.g. REF-1). */
    external_reference_id: string,
    /** Section title or page number specific to this use of the reference. */
    section?: string,
}


/**
 * Typed directional relationship from one CWE entry to another (RelatedWeaknessesType/Related_Weakness in XSD).
 */
export interface RelatedWeakness {
    /** Nature of the relationship. */
    nature: string,
    /** Numeric ID of the target CWE entry. */
    cwe_id: number,
    /** View within which this relationship is relevant. */
    view_id: number,
    /** ID of a named chain for CanFollow/CanPrecede relationships. */
    chain_id?: number,
    /** Set to "Primary" for the primary ChildOf relationship in the given view. */
    ordinal?: string,
}


/**
 * Potential ordering relationship with other weaknesses (WeaknessOrdinalitiesType/Weakness_Ordinality in XSD).
 */
export interface WeaknessOrdinality {
    /** Ordinality level (Primary, Resultant, or Indirect). */
    ordinality: string,
    /** Context in which this ordering relationship exists. */
    description?: string,
}


/**
 * Languages, operating systems, architectures, and technologies where a weakness could appear (ApplicablePlatformsType in XSD).
 */
export interface ApplicablePlatforms {
    /** Programming languages applicable to this weakness. */
    languages?: LanguagePlatform[],
    /** Operating systems applicable to this weakness. */
    operating_systems?: OSPlatform[],
    /** Processor architectures applicable to this weakness. */
    architectures?: ArchitecturePlatform[],
    /** Technologies applicable to this weakness. */
    technologies?: TechnologyPlatform[],
}


/**
 * A programming language or language class applicable to a weakness with associated prevalence (Language element in ApplicablePlatformsType).
 */
export interface LanguagePlatform {
    /** Name of the programming language. */
    name?: string,
    /** Class of the programming language. */
    class_?: string,
    /** Regularity with which this weakness applies to this language. */
    prevalence: string,
}


/**
 * An operating system or OS class applicable to a weakness (Operating_System element in ApplicablePlatformsType).
 */
export interface OSPlatform {
    /** Name of the operating system. */
    name?: string,
    /** Class of the operating system. */
    class_?: string,
    /** Version of the operating system. */
    version?: string,
    /** CPE identifier for this operating system. */
    cpe_id?: string,
    /** Regularity with which this weakness applies to this OS. */
    prevalence: string,
}


/**
 * A processor architecture or class applicable to a weakness (Architecture element in ApplicablePlatformsType).
 */
export interface ArchitecturePlatform {
    /** Name of the processor architecture. */
    name?: string,
    /** Class of the processor architecture. */
    class_?: string,
    /** Regularity with which this weakness applies to this architecture. */
    prevalence: string,
}


/**
 * A technology or technology class applicable to a weakness (Technology element in ApplicablePlatformsType).
 */
export interface TechnologyPlatform {
    /** Name of the technology. */
    name?: string,
    /** Class of the technology. */
    class_?: string,
    /** Regularity with which this weakness applies to this technology. */
    prevalence: string,
}


/**
 * Another name by which this weakness may be known (AlternateTermsType/Alternate_Term in XSD).
 */
export interface AlternateTerm {
    /** An alternate term by which this weakness may be known. */
    term: string,
    /** Narrative description of the entity. */
    description?: string,
}


/**
 * Information about how and when a weakness may be introduced (ModesOfIntroductionType/Introduction in XSD).
 */
export interface ModeOfIntroduction {
    /** Lifecycle phase for introduction or mitigation. */
    phase: string,
    /** Additional contextual note. */
    note?: string,
}


/**
 * Individual consequence associated with a weakness (CommonConsequencesType/Consequence in XSD).
 */
export interface CommonConsequence {
    /** Unique identifier for a common consequence (e.g. CC-1). */
    consequence_id?: string,
    /** Security properties violated by this consequence. */
    scopes: string,
    /** Technical impacts that arise if the weakness is exploited. */
    impacts: string,
    /** Likelihood of this specific consequence. */
    likelihood?: string,
    /** Additional contextual note. */
    note?: string,
}


/**
 * A method that may be employed to detect a weakness, with effectiveness (DetectionMethodsType/Detection_Method in XSD).
 */
export interface DetectionMethod {
    /** Unique identifier for a detection method entry (e.g. DM-1). */
    detection_method_id?: string,
    /** Detection method (range narrowed per class via slot_usage). */
    method: string,
    /** Narrative description of the entity. */
    description: string,
    /** Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage). */
    effectiveness?: string,
    /** Strengths and shortcomings of this detection or mitigation. */
    effectiveness_notes?: string,
}


/**
 * A potential mitigation for a weakness (PotentialMitigationsType/Mitigation in XSD).
 */
export interface PotentialMitigation {
    /** Unique identifier for a potential mitigation (e.g. MIT-1). */
    mitigation_id?: string,
    /** Lifecycle phases during which a mitigation may be applied. */
    phases?: string,
    /** General protection strategy to which a mitigation contributes. */
    strategy?: string,
    /** Narrative description of the entity. */
    description: string,
    /** Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage). */
    effectiveness?: string,
    /** Strengths and shortcomings of this detection or mitigation. */
    effectiveness_notes?: string,
}


/**
 * A code example illustrating how a weakness may appear (DemonstrativeExamplesType/Demonstrative_Example in XSD).
 */
export interface DemonstrativeExample {
    /** Unique identifier for a demonstrative example (e.g. DX-1). */
    demonstrative_example_id?: string,
    /** Optional title for a demonstrative example. */
    title_text?: string,
    /** Context and setting for the demonstrative example. */
    intro_text: string,
    /** Interleaved body text paragraphs for a demonstrative example. */
    body_texts?: string[],
    /** Structured code snippets within a demonstrative example. */
    example_codes?: ExampleCode[],
    /** Links to external references defined in the catalog. */
    references?: CWEReference[],
}


/**
 * A structured code snippet within a demonstrative example (StructuredCodeType in XSD).
 */
export interface ExampleCode {
    /** Nature of the code (Bad, Good, Attack, Mitigation, etc.). */
    nature: string,
    /** Programming language used in this code example. */
    language?: string,
    /** Text content of the code snippet. */
    content?: string,
}


/**
 * A reference to a real-world instance of a weakness, typically a CVE (ObservedExampleType/Observed_Example in XSD).
 */
export interface ObservedExample {
    /** Identifier for a real-world example (e.g. CVE-2005-1951). */
    reference: string,
    /** Narrative description of the entity. */
    description: string,
    /** URL providing more information about the observed example. */
    link: string,
}


/**
 * A mapping from a CWE entry to an equivalent entry in an external taxonomy (TaxonomyMappingsType/Taxonomy_Mapping in XSD).
 */
export interface TaxonomyMapping {
    /** Name of the external taxonomy to which the mapping is made. */
    taxonomy_name: string,
    /** ID of the entry in the external taxonomy. */
    entry_id?: string,
    /** Name of the entry in the external taxonomy. */
    entry_name?: string,
    /** How close the CWE entry is to the mapped taxonomy entry. */
    mapping_fit?: string,
}


/**
 * A Has_Member or Member_Of entry specifying a CWE ID and the View ID in which the membership holds (MemberType in XSD).
 */
export interface CatalogMember {
    /** Numeric CWE ID (foreign key in relationships and members). */
    cwe_id: number,
    /** View ID within which a relationship or membership is relevant. */
    view_id: number,
}


/**
 * Container for category membership relationships (RelationshipsType in XSD). Holds Has_Member and optionally Member_Of lists.
 */
export interface Relationship {
    /** CWE entries that belong to this category or view. */
    has_member?: CatalogMember[],
    /** Views or categories that this entry belongs to. */
    member_of?: CatalogMember[],
}


/**
 * A target stakeholder group for a CWE view or category (AudienceType/Stakeholder in XSD).
 */
export interface Audience {
    /** Type of stakeholder in the CWE community. */
    type: string,
    /** Narrative description of the entity. */
    description?: string,
}


/**
 * Guidance for when and whether to map an issue to a CWE entry (MappingNotesType in XSD). Required on every Weakness, Category, and View.
 */
export interface MappingNotes {
    /** Whether this CWE entry is supported for mapping. */
    usage: string,
    /** Context for the mapping usage designation. */
    rationale: string,
    /** Further clarification for the mapping notes reader. */
    comments: string,
    /** Vocabulary summary of the mapping usage recommendation. */
    reasons: string,
    /** Suggested alternative CWE entries for mapping. */
    suggestions?: MappingSuggestion[],
}


/**
 * A suggested alternative CWE entry for mapping purposes (SuggestionsType/Suggestion in XSD).
 */
export interface MappingSuggestion {
    /** Numeric CWE ID (foreign key in relationships and members). */
    cwe_id: number,
    /** Explanatory comment (e.g. on a mapping suggestion). */
    comment: string,
}


/**
 * Additional commentary about a CWE entry (NotesType/Note in XSD).
 */
export interface Note {
    /** Type of note (Maintenance, Terminology, Research Gap, etc.). */
    type: string,
    /** Textual content of a note. */
    content?: string,
}


/**
 * Tracks the original author and subsequent modifications (ContentHistoryType in XSD).
 */
export interface ContentHistory {
    /** Initial submission information for this entry. */
    submission: Submission,
    /** Ordered list of modifications made to this entry. */
    modifications?: Modification[],
    /** Contribution records for this entry. */
    contributions?: Contribution[],
    /** Previous names used for this entry before a substantive rename. */
    previous_entry_names?: PreviousEntryName[],
}


/**
 * Initial submission record for a CWE entry (ContentHistoryType/Submission in XSD).
 */
export interface Submission {
    /** Name of the person who submitted this entry. */
    submission_name?: string,
    /** Organization of the submitter. */
    submission_organization?: string,
    /** Date on which this entry was submitted. */
    submission_date: date,
    /** CWE version in which this entry was first added. */
    submission_version: string,
    /** Release date of the CWE version that added this entry. */
    submission_release_date: date,
    /** Optional comment related to the submission. */
    submission_comment?: string,
}


/**
 * A modification record documenting a change to a CWE entry (ContentHistoryType/Modification in XSD).
 */
export interface Modification {
    /** Name of the person who made the modification. */
    modification_name?: string,
    /** Organization of the modifier. */
    modification_organization?: string,
    /** Date on which the modification was made. */
    modification_date: date,
    /** CWE version in which the modification first appeared. */
    modification_version?: string,
    /** Release date of the CWE version containing the modification. */
    modification_release_date?: date,
    /** Importance level of this modification. */
    modification_importance?: string,
    /** Comment describing what was changed. */
    modification_comment?: string,
}


/**
 * A contribution record documenting donated content or feedback (ContentHistoryType/Contribution in XSD).
 */
export interface Contribution {
    /** Whether the contribution was Content or Feedback. */
    type: string,
    /** Name of the contributor. */
    contribution_name?: string,
    /** Organization of the contributor. */
    contribution_organization?: string,
    /** Date of the contribution. */
    contribution_date: date,
    /** CWE version in which the contribution first appeared. */
    contribution_version?: string,
    /** Release date of the CWE version containing the contribution. */
    contribution_release_date?: date,
    /** Comment related to the contribution. */
    contribution_comment?: string,
}


/**
 * A previous name used for a CWE entry before a substantive rename (ContentHistoryType/Previous_Entry_Name in XSD).
 */
export interface PreviousEntryName {
    /** The previous name of this CWE entry. */
    name: string,
    /** Date on which this name was last used. */
    date: date,
    /** CWE version in which the name change occurred. */
    version?: string,
}


/**
 * Weakness observation from an NVD vulnerability detail page.
 */
export interface NVDWeaknessObservation {
    /** Identifier for an NVD weakness observation row. */
    observation_id: string,
    /** CVE identifier where this weakness observation appears. */
    observed_in_cve: string,
    /** Referenced CWE entry for this observation. */
    weakness: WeaknessId,
    /** Source label for the weakness row (e.g. NIST, ASSIGNER). */
    reported_by: string,
    /** Source or origin of the data. */
    source?: string,
}



