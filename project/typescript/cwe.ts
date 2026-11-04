export type CweExternalReferenceReferenceID = string;
export type CweEntryID = string;
export type CweWeaknessID = string;
export type CweGroupingID = string;
export type CweViewID = string;
/**
* How far a weakness is described in general terms or tied to a specific product or resource.
*/
export enum CweAbstraction {
    
    /** The most general level, a theme that the weaknesses under it share. */
    Pillar = "Pillar",
    /** A very general weakness, usually independent of any language or technology. */
    Class = "Class",
    /** A weakness general enough to apply widely and detailed enough to find or prevent it. */
    Base = "Base",
    /** A weakness tied to a particular language, technology or kind of product. */
    Variant = "Variant",
    /** An entry that ties two or more weaknesses together, as a chain or a composite. */
    Compound = "Compound",
};
/**
* The part an alternate term plays when people talk about a weakness.
*/
export enum CweAlternateTermRole {
    
    Abbreviation = "Abbreviation",
    Acronym = "Acronym",
    Alternate_Spelling = "Alternate-Spelling",
    Attack_Focused = "Attack-Focused",
    Impact_Oriented = "Impact-Oriented",
    Multi_Weakness = "Multi-Weakness",
    Multiple_Interpretation = "Multiple-Interpretation",
    Common_Name = "Common-Name",
    Discouraged = "Discouraged",
    Legacy = "Legacy",
    Other = "Other",
};
/**
* A broad family of hardware architectures.
*/
export enum CweArchitectureClass {
    
    Embedded = "Embedded",
    Microcomputer = "Microcomputer",
    Workstation = "Workstation",
    /** The weakness can appear on many architectures. */
    Not_Architecture_Specific = "Not Architecture-Specific",
};
/**
* A named hardware architecture.
*/
export enum CweArchitectureName {
    
    Alpha = "Alpha",
    ARM = "ARM",
    Itanium = "Itanium",
    Power_Architecture = "Power Architecture",
    SPARC = "SPARC",
    x86 = "x86",
    Other = "Other",
};
/**
* A way of finding a weakness.
*/
export enum CweDetectionMethodName {
    
    Automated_Analysis = "Automated Analysis",
    Automated_Dynamic_Analysis = "Automated Dynamic Analysis",
    Automated_Static_Analysis = "Automated Static Analysis",
    Automated_Static_Analysis___Source_Code = "Automated Static Analysis - Source Code",
    Automated_Static_Analysis___Binary_or_Bytecode = "Automated Static Analysis - Binary or Bytecode",
    Fuzzing = "Fuzzing",
    Manual_Analysis = "Manual Analysis",
    Manual_Dynamic_Analysis = "Manual Dynamic Analysis",
    Manual_Static_Analysis = "Manual Static Analysis",
    Manual_Static_Analysis___Source_Code = "Manual Static Analysis - Source Code",
    Manual_Static_Analysis___Binary_or_Bytecode = "Manual Static Analysis - Binary or Bytecode",
    White_Box = "White Box",
    Black_Box = "Black Box",
    Architecture_or_Design_Review = "Architecture or Design Review",
    Dynamic_Analysis_with_Manual_Results_Interpretation = "Dynamic Analysis with Manual Results Interpretation",
    Dynamic_Analysis_with_Automated_Results_Interpretation = "Dynamic Analysis with Automated Results Interpretation",
    Formal_Verification = "Formal Verification",
    Simulation_SOLIDUS_Emulation = "Simulation / Emulation",
    Other = "Other",
};
/**
* How well a detection method finds a weakness.
*/
export enum CweDetectionEffectiveness {
    
    /** It finds the weakness often and with few false reports. */
    High = "High",
    /** It works in several situations but misses some forms or gives some false reports. */
    Moderate = "Moderate",
    /** The State Of the Art Report rates it as cost-effective for part of the job. */
    SOAR_Partial = "SOAR Partial",
    /** It does not aim at this weakness and finds it only by the way. */
    Opportunistic = "Opportunistic",
    /** It helps only in some situations. */
    Limited = "Limited",
    /** It does not find the weakness. */
    None = "None",
};
/**
* How well a mitigation prevents a weakness.
*/
export enum CweEffectiveness {
    
    /** It often removes the weakness altogether. */
    High = "High",
    /** It prevents several forms of the weakness but does not cover them all. */
    Moderate = "Moderate",
    /** It helps only in some situations or against some forms of the weakness. */
    Limited = "Limited",
    /** It protects by chance and cannot be relied on. */
    Incidental = "Incidental",
    /** A habit people often follow that does not work well enough to recommend. */
    Discouraged_Common_Practice = "Discouraged Common Practice",
    /** It adds a layer of protection and does not remove the weakness by itself. */
    Defense_in_Depth = "Defense in Depth",
    /** It does not prevent the weakness. */
    None = "None",
};
/**
* The part of a product where a weakness is most likely to appear.
*/
export enum CweFunctionalArea {
    
    Authentication = "Authentication",
    Authorization = "Authorization",
    Code_Libraries = "Code Libraries",
    Counters = "Counters",
    Cryptography = "Cryptography",
    Error_Handling = "Error Handling",
    Interprocess_Communication = "Interprocess Communication",
    File_Processing = "File Processing",
    Logging = "Logging",
    Memory_Management = "Memory Management",
    Networking = "Networking",
    Number_Processing = "Number Processing",
    Program_Invocation = "Program Invocation",
    Protection_Mechanism = "Protection Mechanism",
    Session_Management = "Session Management",
    Signals = "Signals",
    String_Processing = "String Processing",
    Not_Functional_Area_Specific = "Not Functional-Area-Specific",
    Power = "Power",
    Clock = "Clock",
};
/**
* How much a change to an entry matters to people who already rely on it.
*/
export enum CweImportance {
    
    Normal = "Normal",
    /** The change alters what the entry means or how it may be read. */
    Critical = "Critical",
};
/**
* A broad family of programming languages.
*/
export enum CweLanguageClass {
    
    Assembly = "Assembly",
    Compiled = "Compiled",
    Hardware_Description_Language = "Hardware Description Language",
    Interpreted = "Interpreted",
    Object_Oriented = "Object-Oriented",
    Memory_Unsafe = "Memory-Unsafe",
    /** The weakness can appear in many languages. */
    Not_Language_Specific = "Not Language-Specific",
};
/**
* A named programming language or notation.
*/
export enum CweLanguageName {
    
    Ada = "Ada",
    Algorithm = "Algorithm",
    ARM_Assembly = "ARM Assembly",
    ASP = "ASP",
    ASPFULL_STOPNET = "ASP.NET",
    Basic = "Basic",
    C = "C",
    C_plus_plus = "C++",
    C_sharp = "C#",
    COBOL = "COBOL",
    Fortran = "Fortran",
    F_sharp = "F#",
    Go = "Go",
    HTML = "HTML",
    Java = "Java",
    JavaScript = "JavaScript",
    JSON = "JSON",
    JSP = "JSP",
    Objective_C = "Objective-C",
    Pascal = "Pascal",
    Perl = "Perl",
    PHP = "PHP",
    Pseudocode = "Pseudocode",
    Python = "Python",
    Ruby = "Ruby",
    Rust = "Rust",
    Shell = "Shell",
    SQL = "SQL",
    Swift = "Swift",
    SystemVerilog = "SystemVerilog",
    VBFULL_STOPNET = "VB.NET",
    Verilog = "Verilog",
    VHDL = "VHDL",
    XML = "XML",
    x86_Assembly = "x86 Assembly",
    Other = "Other",
};
/**
* How likely something is to happen.
*/
export enum CweLikelihood {
    
    High = "High",
    Medium = "Medium",
    Low = "Low",
    /** Nobody knows how likely it is. */
    Unknown = "Unknown",
};
/**
* A general approach that a mitigation follows.
*/
export enum CweMitigationStrategy {
    
    Attack_Surface_Reduction = "Attack Surface Reduction",
    Compilation_or_Build_Hardening = "Compilation or Build Hardening",
    Enforcement_by_Conversion = "Enforcement by Conversion",
    Environment_Hardening = "Environment Hardening",
    Firewall = "Firewall",
    Input_Validation = "Input Validation",
    Language_Selection = "Language Selection",
    Libraries_or_Frameworks = "Libraries or Frameworks",
    Resource_Limitation = "Resource Limitation",
    Output_Encoding = "Output Encoding",
    Parameterization = "Parameterization",
    Refactoring = "Refactoring",
    Sandbox_or_Jail = "Sandbox or Jail",
    Separation_of_Privilege = "Separation of Privilege",
};
/**
* What a note on an entry is about.
*/
export enum CweNoteType {
    
    /** More detail on the platforms the entry lists. */
    Applicable_Platform = "Applicable Platform",
    /** Work the entry still needs, such as sharper concepts or better relationships. */
    Maintenance = "Maintenance",
    /** More detail on how the entry relates to others. */
    Relationship = "Relationship",
    /** A topic researchers have not yet explored enough. */
    Research_Gap = "Research Gap",
    /** A discussion of the words used for the weakness. */
    Terminology = "Terminology",
    /** The weakness described in the terms of vulnerability theory. */
    Theoretical = "Theoretical",
    /** Anything useful that fits no other type. */
    Other = "Other",
};
/**
* Marks the relationship to prefer among several in one view.
*/
export enum CweOrdinal {
    
    /** The relationship to follow first in that view. */
    Primary = "Primary",
};
/**
* How a weakness stands to other weaknesses in a sequence of causes.
*/
export enum CweOrdinality {
    
    /** A quality problem that makes other weaknesses easier to introduce or harder to find. */
    Indirect = "Indirect",
    /** The weakness exists without depending on another one. */
    Primary = "Primary",
    /** The weakness exists only because another one is present. */
    Resultant = "Resultant",
};
/**
* A broad family of operating systems.
*/
export enum CweOperatingSystemClass {
    
    Linux = "Linux",
    macOS = "macOS",
    Unix = "Unix",
    Windows = "Windows",
    /** The weakness can appear on many operating systems. */
    Not_OS_Specific = "Not OS-Specific",
};
/**
* A named operating system.
*/
export enum CweOperatingSystemName {
    
    AIX = "AIX",
    Android = "Android",
    BlackBerry_OS = "BlackBerry OS",
    Chrome_OS = "Chrome OS",
    Darwin = "Darwin",
    FreeBSD = "FreeBSD",
    iOS = "iOS",
    macOS = "macOS",
    NetBSD = "NetBSD",
    OpenBSD = "OpenBSD",
    Red_Hat = "Red Hat",
    Solaris = "Solaris",
    SUSE = "SUSE",
    tvOS = "tvOS",
    Ubuntu = "Ubuntu",
    watchOS = "watchOS",
    Windows_9x = "Windows 9x",
    Windows_Embedded = "Windows Embedded",
    Windows_NT = "Windows NT",
    Other = "Other",
};
/**
* A stage of a product life cycle.
*/
export enum CwePhase {
    
    Policy = "Policy",
    Requirements = "Requirements",
    Architecture_and_Design = "Architecture and Design",
    Implementation = "Implementation",
    Build_and_Compilation = "Build and Compilation",
    Testing = "Testing",
    Documentation = "Documentation",
    Bundling = "Bundling",
    Distribution = "Distribution",
    Installation = "Installation",
    System_Configuration = "System Configuration",
    Operation = "Operation",
    Patching_and_Maintenance = "Patching and Maintenance",
    Porting = "Porting",
    Integration = "Integration",
    Manufacturing = "Manufacturing",
    Decommissioning_and_End_of_Life = "Decommissioning and End-of-Life",
};
/**
* A stage of the life cycle of an artificial intelligence system.
*/
export enum CweAiPhase {
    
    Data_Collection = "Data Collection",
    Training = "Training",
    Fine_tuning = "Fine-tuning",
    Testing = "Testing",
    Tokenization = "Tokenization",
    Prompting = "Prompting",
    Output_Processing = "Output Processing",
    Component_Interaction = "Component Interaction",
    Re_training_SOLIDUS_Feedback = "Re-training / Feedback",
};
/**
* A stage of the life cycle of a hardware product.
*/
export enum CweHardwarePhase {
    
    Hardware_Requirements = "Hardware Requirements",
    Hardware_Architecture = "Hardware Architecture",
    Hardware_Microarchitecture = "Hardware Microarchitecture",
    Implementation_AMPERSAND_Physical_Design = "Implementation & Physical Design",
    Pre_Manufacturing_Verification = "Pre-Manufacturing Verification",
    Hardware_Manufacturing = "Hardware Manufacturing",
    Post_Manufacturing_Validation = "Post-Manufacturing Validation",
    Device_Configuration_AMPERSAND_Personalization = "Device Configuration & Personalization",
    Device_SOLIDUS_System_Integration = "Device / System Integration",
    Field_Operations_AMPERSAND_Sustainment = "Field Operations & Sustainment",
    Reuse = "Reuse",
    Decommissioning = "Decommissioning",
};
/**
* The field whose own life cycle a custom phase belongs to.
*/
export enum CweCustomPhaseDomain {
    
    AI = "AI",
    Hardware = "Hardware",
};
/**
* The aspect of a weakness that a dimension names, such as a behaviour or a resource.
*/
export enum CweDimensionType {
    
    Behavior_Type = "Behavior-Type",
    Behavior_Property = "Behavior-Property",
    Resource_Type = "Resource-Type",
    Resource_Property = "Resource-Property",
    Input_Type = "Input-Type",
    Input_Property = "Input-Property",
    Info_Type = "Info-Type",
    Info_Property = "Info-Property",
    Code_Type = "Code-Type",
    Code_Property = "Code-Property",
    Technology = "Technology",
    Language_Type = "Language-Type",
    Language_Property = "Language-Property",
    Framework = "Framework",
    Common_Name = "Common-Name",
    Attack = "Attack",
    Acronym = "Acronym",
    Other = "Other",
};
/**
* How regularly a weakness applies to a platform.
*/
export enum CwePrevalence {
    
    Often = "Often",
    Sometimes = "Sometimes",
    Rarely = "Rarely",
    Undetermined = "Undetermined",
    None = "None",
};
/**
* A short label for why an entry may not suit vulnerability mapping.
*/
export enum CweReason {
    
    Abstraction = "Abstraction",
    Category = "Category",
    Grouping = "Grouping",
    View = "View",
    Deprecated = "Deprecated",
    Potential_Deprecation = "Potential Deprecation",
    Frequent_Misuse = "Frequent Misuse",
    Frequent_Misinterpretation = "Frequent Misinterpretation",
    Multiple_Use = "Multiple Use",
    CWE_Overlap = "CWE Overlap",
    Acceptable_Use = "Acceptable-Use",
    Frequently_Resultant = "Frequently-Resultant",
    Potential_Major_Changes = "Potential Major Changes",
    Other = "Other",
};
/**
* How one weakness relates to another.
*/
export enum CweRelatedNature {
    
    /** The related weakness is more general than this one. */
    ChildOf = "ChildOf",
    /** The related weakness is more specific than this one. */
    ParentOf = "ParentOf",
    /** For a named chain only: the related weakness is where the chain begins. */
    StartsWith = "StartsWith",
    /** In a chain, the related weakness can come before this one. */
    CanFollow = "CanFollow",
    /** In a chain, the related weakness can come after this one. */
    CanPrecede = "CanPrecede",
    /** For composites only: the related composite needs this weakness to be present. */
    RequiredBy = "RequiredBy",
    /** For composites only: this composite needs the related weakness to be present. */
    Requires = "Requires",
    /** In some settings this weakness may be seen as the related one, with neither being a parent of the other. */
    CanAlsoBe = "CanAlsoBe",
    /** The two are similar in a way that no other nature fits. */
    PeerOf = "PeerOf",
    /** The two weaknesses share some ground, which CWE would rather avoid. */
    Overlaps = "Overlaps",
};
/**
* A kind of system resource that exploiting a weakness can affect.
*/
export enum CweResource {
    
    CPU = "CPU",
    File_or_Directory = "File or Directory",
    Memory = "Memory",
    System_Process = "System Process",
    Other = "Other",
};
/**
* The security property a consequence violates.
*/
export enum CweScope {
    
    Confidentiality = "Confidentiality",
    Integrity = "Integrity",
    Availability = "Availability",
    Access_Control = "Access Control",
    Accountability = "Accountability",
    Authentication = "Authentication",
    Authorization = "Authorization",
    Non_Repudiation = "Non-Repudiation",
    Other = "Other",
};
/**
* How far an entry has come in its life and how much it can be trusted.
*/
export enum CweStatus {
    
    /** Taken out of CWE, usually because it duplicated another entry or was made by mistake. */
    Deprecated = "Deprecated",
    /** Its important elements are filled in and readable, though it may still have problems. */
    Draft = "Draft",
    /** Some important elements are missing and its quality is not assured. */
    Incomplete = "Incomplete",
    /** Still correct but no longer relevant, usually because a newer entry replaced it. */
    Obsolete = "Obsolete",
    /** Its important elements have been checked and are not expected to change much. */
    Stable = "Stable",
    /** It has had close review and its critical elements have been checked. */
    Usable = "Usable",
};
/**
* A group of people who may have a use for a view.
*/
export enum CweStakeholderType {
    
    Academic_Researchers = "Academic Researchers",
    Applied_Researchers = "Applied Researchers",
    Assessment_Teams = "Assessment Teams",
    Assessment_Tool_Vendors = "Assessment Tool Vendors",
    CWE_Team = "CWE Team",
    Educators = "Educators",
    Hardware_Designers = "Hardware Designers",
    Information_Providers = "Information Providers",
    Product_Customers = "Product Customers",
    Product_Vendors = "Product Vendors",
    Software_Developers = "Software Developers",
    Vulnerability_Analysts = "Vulnerability Analysts",
    Other = "Other",
};
/**
* Whether a weakness stands alone or is made up of others.
*/
export enum CweStructure {
    
    /** Several weaknesses that must be reached one after another to give a vulnerability. */
    Chain = "Chain",
    /** Several weaknesses that give a vulnerability only when they occur together. */
    Composite = "Composite",
    /** One weakness whose exploitation does not depend on another. */
    Simple = "Simple",
};
/**
* What a block of example code shows.
*/
export enum CweCodeNature {
    
    /** An attack against the code. */
    Attack = "Attack",
    /** Code that has the weakness. */
    Bad = "Bad",
    /** Code that avoids the weakness. */
    Good = "Good",
    /** Background that shows neither good nor bad code. */
    Informative = "Informative",
    /** A way of addressing the weakness. */
    Mitigation = "Mitigation",
    /** What running the code produces. */
    Result = "Result",
};
/**
* How closely a CWE entry matches an entry of another taxonomy.
*/
export enum CweMappingFit {
    
    Exact = "Exact",
    /** The CWE entry is more general than the other. */
    CWE_More_Abstract = "CWE More Abstract",
    /** The CWE entry is narrower than the other. */
    CWE_More_Specific = "CWE More Specific",
    /** The two match only loosely. */
    Imprecise = "Imprecise",
    /** The two look at the same matter from different angles. */
    Perspective = "Perspective",
};
/**
* A taxonomy that CWE entries are mapped to.
*/
export enum CweTaxonomyName {
    
    Seven_Pernicious_Kingdoms = "7 Pernicious Kingdoms",
    Nineteen_Deadly_Sins = "19 Deadly Sins",
    Aslam = "Aslam",
    Bishop = "Bishop",
    CERT_C_Secure_Coding = "CERT C Secure Coding",
    CERT_CPLUS_SIGNPLUS_SIGN_Secure_Coding = "CERT C++ Secure Coding",
    The_CERT_Oracle_Secure_Coding_Standard_for_Java_LEFT_PARENTHESIS2011RIGHT_PARENTHESIS = "The CERT Oracle Secure Coding Standard for Java (2011)",
    CLASP = "CLASP",
    ISASOLIDUSIEC_62443 = "ISA/IEC 62443",
    Landwehr = "Landwehr",
    OMG_ASCSM = "OMG ASCSM",
    OMG_ASCRM = "OMG ASCRM",
    OMG_ASCMM = "OMG ASCMM",
    OMG_ASCPEM = "OMG ASCPEM",
    OpenSSF_Secure_Coding_Guide_for_Python = "OpenSSF Secure Coding Guide for Python",
    OWASP_Golang_Secure_Coding_Practices_Guide = "OWASP Golang Secure Coding Practices Guide",
    OWASP_Top_Ten_2004 = "OWASP Top Ten 2004",
    OWASP_Top_Ten_2007 = "OWASP Top Ten 2007",
    OWASP_Top_Ten = "OWASP Top Ten",
    PLC_Top_20 = "PLC Top 20",
    PLOVER = "PLOVER",
    Protection_Analysis = "Protection Analysis",
    RISOS = "RISOS",
    SEI_CERT_C_Coding_Standard = "SEI CERT C Coding Standard",
    SEI_CERT_CPLUS_SIGNPLUS_SIGN_Coding_Standard = "SEI CERT C++ Coding Standard",
    SEI_CERT_Oracle_Coding_Standard_for_Java = "SEI CERT Oracle Coding Standard for Java",
    SEI_CERT_Perl_Coding_Standard = "SEI CERT Perl Coding Standard",
    Software_Fault_Patterns = "Software Fault Patterns",
    Weber_Karger_Paradkar = "Weber, Karger, Paradkar",
    WASC = "WASC",
};
/**
* What an attacker can achieve by exploiting a weakness.
*/
export enum CweTechnicalImpact {
    
    Modify_Memory = "Modify Memory",
    Read_Memory = "Read Memory",
    Modify_Files_or_Directories = "Modify Files or Directories",
    Read_Files_or_Directories = "Read Files or Directories",
    Modify_Application_Data = "Modify Application Data",
    Read_Application_Data = "Read Application Data",
    DoSCOLON_Crash_Exit_or_Restart = "DoS: Crash, Exit, or Restart",
    DoSCOLON_Amplification = "DoS: Amplification",
    DoSCOLON_Instability = "DoS: Instability",
    DoSCOLON_Prevent_Access = "DoS: Prevent Access",
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISCPURIGHT_PARENTHESIS = "DoS: Resource Consumption (CPU)",
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISMemoryRIGHT_PARENTHESIS = "DoS: Resource Consumption (Memory)",
    DoSCOLON_Resource_Consumption_LEFT_PARENTHESISOtherRIGHT_PARENTHESIS = "DoS: Resource Consumption (Other)",
    DoSCOLON_Other = "DoS: Other",
    Execute_Unauthorized_Code_or_Commands = "Execute Unauthorized Code or Commands",
    Gain_Privileges_or_Assume_Identity = "Gain Privileges or Assume Identity",
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism",
    Hide_Activities = "Hide Activities",
    Alter_Execution_Logic = "Alter Execution Logic",
    Undefined_Behavior = "Undefined Behavior",
    Quality_Degradation = "Quality Degradation",
    Unexpected_State = "Unexpected State",
    Varies_by_Context = "Varies by Context",
    Increase_Analytical_Complexity = "Increase Analytical Complexity",
    Reduce_Maintainability = "Reduce Maintainability",
    Reduce_Performance = "Reduce Performance",
    Reduce_Reliability = "Reduce Reliability",
    Other = "Other",
};
/**
* A broad family of technologies.
*/
export enum CweTechnologyClass {
    
    Client_Server = "Client Server",
    Cloud_Computing = "Cloud Computing",
    ICSSOLIDUSOT = "ICS/OT",
    Mainframe = "Mainframe",
    Mobile = "Mobile",
    N_Tier = "N-Tier",
    SOA = "SOA",
    System_on_Chip = "System on Chip",
    Web_Based = "Web Based",
    /** The weakness can appear in many technologies. */
    Not_Technology_Specific = "Not Technology-Specific",
};
/**
* A named technology.
*/
export enum CweTechnologyName {
    
    AISOLIDUSML = "AI/ML",
    Web_Server = "Web Server",
    Database_Server = "Database Server",
    Accelerator_Hardware = "Accelerator Hardware",
    Analog_and_Mixed_Signal_Hardware = "Analog and Mixed Signal Hardware",
    AudioSOLIDUSVideo_Hardware = "Audio/Video Hardware",
    BusSOLIDUSInterface_Hardware = "Bus/Interface Hardware",
    ClockSOLIDUSCounter_Hardware = "Clock/Counter Hardware",
    Communication_Hardware = "Communication Hardware",
    Controller_Hardware = "Controller Hardware",
    Memory_Hardware = "Memory Hardware",
    Microcontroller_Hardware = "Microcontroller Hardware",
    Network_on_Chip_Hardware = "Network on Chip Hardware",
    Power_Management_Hardware = "Power Management Hardware",
    Processor_Hardware = "Processor Hardware",
    Security_Hardware = "Security Hardware",
    Sensor_Hardware = "Sensor Hardware",
    Storage_Hardware = "Storage Hardware",
    TestSOLIDUSDebug_Hardware = "Test/Debug Hardware",
    Other = "Other",
};
/**
* Whether an entry may be used when mapping a real vulnerability to its root cause.
*/
export enum CweUsage {
    
    /** It should not be used for mapping. */
    Discouraged = "Discouraged",
    /** It must not be used for mapping. */
    Prohibited = "Prohibited",
    /** It may be used for mapping. */
    Allowed = "Allowed",
    /** It may be used for mapping only in limited situations and after careful review. */
    Allowed_with_Review = "Allowed-with-Review",
};
/**
* How a view selects and arranges its entries.
*/
export enum CweViewType {
    
    /** A flat list that a filter selects. */
    Implicit = "Implicit",
    /** A flat list whose members are named one by one. */
    Explicit = "Explicit",
    /** A hierarchy of entries from one point of view. */
    Graph = "Graph",
};
/**
* A hint at why an observed example was chosen for an entry.
*/
export enum CweObservedExampleRationale {
    
    Chain = "Chain",
    /** One of the earliest examples recognised as showing this weakness. */
    Early_Publication = "Early-Publication",
    /** An example that drew attention or shaped how people see this weakness. */
    InfluentialSOLIDUSNewsworthy = "Influential/Newsworthy",
    Language_Variety = "Language-Variety",
    Product_Variety = "Product-Variety",
    Attack_Surface = "Attack-Surface",
    Other = "Other",
};
/**
* What stands between a reader and a cited source.
*/
export enum CweReferenceAccessRestriction {
    
    /** Anybody on the internet can read it for free. */
    None = "None",
    /** Only paying subscribers can read it. */
    Proprietary_Subscription = "Proprietary-Subscription",
    /** A reader must register, at no cost, to read it. */
    Minimal_Registration = "Minimal-Registration",
    /** It has been taken down and may have no other copy. */
    Removed = "Removed",
    Other = "Other",
};
/**
* The form a cited source takes, which affects how easily people can use it.
*/
export enum CweReferenceMediaType {
    
    /** Plain text or a format that is easy to parse, as HTML with no scripts is. */
    Text = "Text",
    /** A widely used proprietary format for text, such as PDF or a word processor file. */
    Common_Proprietary_Text = "Common-Proprietary-Text",
    /** A recording with pictures, such as a conference talk. */
    Video = "Video",
    /** A recording with sound and no pictures. */
    Audio = "Audio",
    /** Some other format, which may be harder for some readers to use. */
    Other = "Other",
};
/**
* A hint at why a source was cited.
*/
export enum CweReferenceRationale {
    
    /** It gives more detail on an example in the entry, and may be where the example came from. */
    Example = "Example",
    /** One of the first publications to explain the weakness or how it is exploited. */
    Early_Publication = "Early-Publication",
    /** A publication that drew attention or shaped how people see the weakness. */
    InfluentialSOLIDUSNewsworthy = "Influential/Newsworthy",
    /** Technical reference material that gives background and is not about the weakness itself. */
    ManualSOLIDUSMan_Pages = "Manual/Man Pages",
    /** It proposes ways to reduce or remove weaknesses across a whole system. */
    Mitigation_Based = "Mitigation-Based",
    /** It points to formal rules or guides for developing securely. */
    Secure_Development_Rules = "Secure-Development-Rules",
    Other = "Other",
};
/**
* What a contribution to an entry consisted of.
*/
export enum CweContributionType {
    
    /** Content given to the entry. */
    Content = "Content",
    /** Feedback on the entry. */
    Feedback = "Feedback",
};


/**
 * A source that entries of the catalogue cite, such as a paper, a book or a web page.
 */
export interface CweExternalReference {
    /** The identifier entries use to cite this source. */
    Reference_ID: string,
    /** A person or group who wrote the source. */
    Author?: string[],
    /** The title of the source. */
    Title: string,
    /** The edition of the source. */
    Edition?: string,
    /** The journal, conference or other publication that holds the source. */
    Publication?: string,
    /** The year the source came out. */
    Publication_Year?: string,
    /** The month the source came out. */
    Publication_Month?: string,
    /** The day of the month the source came out. */
    Publication_Day?: string,
    /** Who published the source. */
    Publisher?: string,
    /** An address where the source can be read. */
    URL?: string,
    /** The date on which the address was last seen to work. */
    URL_Date?: date,
    /** Another address of the source, usually one with fewer restrictions. */
    Alt_URL?: string,
    /** The date on which the other address was last seen to work. */
    Alt_URL_Date?: date,
    /** A form the source takes. */
    Media_Type?: string,
    /** What stands between a reader and the source. */
    Access_Restrictions?: string,
    /** A hint at why the source was cited. */
    Rationale?: string,
}


/**
 * A citation of an external reference from an entry or from one of its parts.
 */
export interface CweReference {
    /** The external reference being cited. */
    External_Reference_ID: CweExternalReferenceReferenceID,
    /** The section or page of the source that this citation means. */
    Section?: string,
}


/**
 * One aspect of a weakness, or of how two weaknesses differ, named in a word or two.
 */
export interface CweDimension {
    /** The kind of aspect, such as a behaviour or a resource. */
    Type: string,
    /** The aspect itself, such as Generation or Page. */
    Value: string,
}


/**
 * A life cycle stage from a field whose stages differ from those of software.
 */
export interface CweCustomPhase {
    /** The field whose life cycle the stage belongs to. */
    Domain: string,
    /** The stage. */
    Value: string,
}


/**
 * A remark on an entry that fits nowhere else.
 */
export interface CweNote {
    /** What the note is about. */
    Type: string,
    /** The CWE version the note belongs to. */
    Version?: string,
    /** The release date of that version. */
    ReleaseDate?: date,
    /** The text of the note. */
    Value?: string,
}


/**
 * A link from an entry to an entry of another taxonomy.
 */
export interface CweTaxonomyMapping {
    /** The other taxonomy. */
    Taxonomy_Name: string,
    /** The identifier of the entry in the other taxonomy. */
    Entry_ID?: string,
    /** The name of the entry in the other taxonomy. */
    Entry_Name?: string,
    /** How closely the two entries match. */
    Mapping_Fit?: string,
}


/**
 * The record of who wrote an entry and how it has changed since.
 */
export interface CweContentHistory {
    /** The original submission of the entry, or each of several. */
    Submission: CweSubmission[],
    /** A change made to the entry. */
    Modification?: CweModification[],
    /** Feedback or content that someone gave to the entry. */
    Contribution?: CweContribution[],
    /** A name the entry used to have. */
    Previous_Entry_Name?: CwePreviousEntryName[],
}


/**
 * Who first submitted an entry, and when it joined the list.
 */
export interface CweSubmission {
    /** A person or group who submitted the entry. */
    Submission_Name?: string[],
    /** The organization the submitter belongs to. */
    Submission_Organization?: string,
    /** The date of the submission. */
    Submission_Date: date,
    /** The first CWE version that held the submission. */
    Submission_Version: string,
    /** The release date of that version. */
    Submission_ReleaseDate: date,
    /** A remark on the submission. */
    Submission_Comment?: string,
}


/**
 * One change made to an entry.
 */
export interface CweModification {
    /** The person who made or suggested the change. */
    Modification_Name?: string,
    /** The organization that person belongs to. */
    Modification_Organization?: string,
    /** The date of the change. */
    Modification_Date: date,
    /** The first CWE version that held the change. */
    Modification_Version: string,
    /** The release date of that version. */
    Modification_ReleaseDate: date,
    /** How much the change matters to people who rely on the entry. */
    Modification_Importance?: string,
    /** What changed. */
    Modification_Comment: string,
}


/**
 * Feedback or content that someone gave to an entry.
 */
export interface CweContribution {
    /** Whether the contribution was feedback or content. */
    Type: string,
    /** A person or group who contributed. */
    Contribution_Name?: string[],
    /** The organization the contributor belongs to. */
    Contribution_Organization?: string,
    /** The date of the contribution. */
    Contribution_Date: date,
    /** The first CWE version that held the contribution. */
    Contribution_Version: string,
    /** The release date of that version. */
    Contribution_ReleaseDate: date,
    /** A remark on the contribution. */
    Contribution_Comment?: string,
}


/**
 * A name an entry had before.
 */
export interface CwePreviousEntryName {
    /** The date the name stopped being used. */
    Date: date,
    /** The CWE version in which the name changed. */
    Version?: string,
    /** The earlier name. */
    Value: string,
}


/**
 * Any item of the CWE List that has an identifier of its own: a weakness, a grouping or a view.
 */
export interface CweEntry {
    /** The number that identifies the entry across the whole list. */
    ID: string,
    /** The name of the entry. */
    Name: string,
    /** How far the entry has come and how much it can be trusted. */
    Status: string,
    /** The external references the entry cites. */
    References?: CweReference[],
    /** Guidance on whether to map a real vulnerability to this entry. */
    Mapping_Notes: CweMappingNotes,
    /** Remarks on the entry that fit nowhere else. */
    Notes?: CweNote[],
    /** Who wrote the entry and how it has changed since. */
    Content_History: CweContentHistory,
}


/**
 * A type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack.
 */
export interface CweWeakness extends CweEntry {
    /** How far the weakness is described in general terms or tied to a specific product. */
    Abstraction: string,
    /** Whether the weakness stands alone or is made up of others. */
    Structure: string,
    /** The path on MITRE's site of a diagram of the weakness. */
    Diagram?: string,
    /** A sentence or two that define the weakness. */
    Description: string,
    /** More about the weakness than its short description gives. */
    Extended_Description?: string,
    /** Finer technical detail that helps tell this weakness from close relatives. */
    Technical_Nuance?: string,
    /** The aspects of the weakness that this entry centres on. */
    Dimensions?: CweDimension[],
    /** How this weakness relates to others in the list. */
    Related_Weaknesses?: CweRelatedWeakness[],
    /** Whether the weakness tends to be a first cause or the result of another. */
    Weakness_Ordinalities?: CweWeaknessOrdinality[],
    /** The languages, systems, architectures and technologies where the weakness can appear. */
    Applicable_Platforms?: CweApplicablePlatforms,
    /** Background that helps a reader but does not describe the weakness itself. */
    Background_Details?: string[],
    /** Other names people use for the weakness. */
    Alternate_Terms?: CweAlternateTerm[],
    /** How and when the weakness can get into a product. */
    Modes_Of_Introduction?: CweIntroduction[],
    /** Conditions that make exploiting the weakness more likely. */
    Exploitation_Factors?: string[],
    /** How likely it is that the weakness gets exploited. */
    Likelihood_Of_Exploit?: string,
    /** What can follow when the weakness is exploited. */
    Common_Consequences?: CweConsequence[],
    /** Ways of finding the weakness, with what each is good for. */
    Detection_Methods?: CweDetectionMethod[],
    /** Ways of preventing the weakness or reducing what it can do. */
    Potential_Mitigations?: CweMitigation[],
    /** Worked examples of how the weakness looks in code. */
    Demonstrative_Examples?: CweDemonstrativeExample[],
    /** Real cases of the weakness, usually CVE records. */
    Observed_Examples?: CweObservedExample[],
    /** The parts of a product where the weakness tends to appear. */
    Functional_Areas?: string,
    /** The system resources that exploiting the weakness can affect. */
    Affected_Resources?: string,
    /** Links to entries of other taxonomies. */
    Taxonomy_Mappings?: CweTaxonomyMapping[],
    /** Attack patterns that may apply where the weakness is present. */
    Related_Attack_Patterns?: CweRelatedAttackPattern[],
}


/**
 * A set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category.
 */
export interface CweGrouping extends CweEntry {
    /** What the grouped weaknesses have in common. */
    Summary: string,
    /** The entries this grouping holds. */
    Relationships?: CweRelationships,
    /** Links to entries of other taxonomies. */
    Taxonomy_Mappings?: CweTaxonomyMapping[],
}


/**
 * A way of looking at the catalogue, as a subset of its entries seen from one standpoint.
 */
export interface CweView extends CweEntry {
    /** How the view selects and arranges its entries. */
    Type: string,
    /** What the view is for. */
    Objective: string,
    /** The people who may find the view useful, and why. */
    Audience?: CweStakeholder[],
    /** The entries a view names one by one, when it is not selected by a filter. */
    Members?: CweRelationships,
    /** The XPath expression that selects the entries of an implicit slice. */
    Filter?: string,
}


/**
 * A link from a weakness to another weakness, in one view.
 */
export interface CweRelatedWeakness {
    /** How the two weaknesses relate. */
    Nature: string,
    /** The weakness at the other end of the link. */
    CWE_ID: CweWeaknessID,
    /** The view in which the link holds. */
    View_ID: CweViewID,
    /** The named chain that the link belongs to. */
    Chain_ID?: CweWeaknessID,
    /** Marks this as the link to prefer in the view. */
    Ordinal?: string,
    /** The aspects in which the two weaknesses differ. */
    Dimensions?: CweDimension[],
}


/**
 * Whether a weakness tends to be a first cause or the result of another.
 */
export interface CweWeaknessOrdinality {
    /** The position in the sequence of causes. */
    Ordinality: string,
    /** The setting in which the weakness takes this position. */
    Description?: string,
}


/**
 * The kinds of platform where a weakness can appear.
 */
export interface CweApplicablePlatforms {
    /** A programming language, or a family of them. */
    Language?: CweLanguagePlatform[],
    /** An operating system, or a family of them. */
    Operating_System?: CweOperatingSystemPlatform[],
    /** A hardware architecture, or a family of them. */
    Architecture?: CweArchitecturePlatform[],
    /** A technology, or a family of them. */
    Technology?: CweTechnologyPlatform[],
}


/**
 * A language where a weakness can appear, named or by its family.
 */
export interface CweLanguagePlatform {
    /** The name of the language. */
    Name?: string,
    /** The family of languages. */
    Class?: string,
    /** How regularly the weakness applies here. */
    Prevalence: string,
    /** A remark on this platform. */
    Note?: string,
}


/**
 * An operating system where a weakness can appear, named or by its family.
 */
export interface CweOperatingSystemPlatform {
    /** The name of the operating system. */
    Name?: string,
    /** The version of the operating system. */
    Version?: string,
    /** The Common Platform Enumeration name of the operating system. */
    CPE_ID?: string,
    /** The family of operating systems. */
    Class?: string,
    /** How regularly the weakness applies here. */
    Prevalence: string,
    /** A remark on this platform. */
    Note?: string,
}


/**
 * A hardware architecture where a weakness can appear, named or by its family.
 */
export interface CweArchitecturePlatform {
    /** The name of the architecture. */
    Name?: string,
    /** The family of architectures. */
    Class?: string,
    /** How regularly the weakness applies here. */
    Prevalence: string,
    /** A remark on this platform. */
    Note?: string,
}


/**
 * A technology where a weakness can appear, named or by its family.
 */
export interface CweTechnologyPlatform {
    /** The name of the technology. */
    Name?: string,
    /** The family of technologies. */
    Class?: string,
    /** How regularly the weakness applies here. */
    Prevalence: string,
    /** A remark on this platform. */
    Note?: string,
}


/**
 * Another name people use for a weakness.
 */
export interface CweAlternateTerm {
    /** The name. */
    Term: string,
    /** The part the name plays when people talk about the weakness. */
    Role?: string,
    /** When and how the name is used. */
    Description?: string,
}


/**
 * One way a weakness can get into a product.
 */
export interface CweIntroduction {
    /** A life cycle stage where the weakness can get in. */
    Phase?: string,
    /** A stage from the life cycle of a field such as hardware or AI. */
    Custom_Phase?: CweCustomPhase[],
    /** The usual way this happens. */
    Note?: string,
}


/**
 * One thing that can follow when a weakness is exploited.
 */
export interface CweConsequence {
    /** An identifier for this consequence. */
    Consequence_ID?: string,
    /** A security property the consequence violates. */
    Scope: string,
    /** What an attacker can achieve. */
    Impact: string,
    /** How likely this consequence is beside the others. */
    Likelihood?: string,
    /** A remark on the consequence. */
    Note?: string,
}


/**
 * One way of finding a weakness.
 */
export interface CweDetectionMethod {
    /** An identifier that lets entries share this text, such as DM-14. */
    Detection_Method_ID?: string,
    /** The way of finding the weakness. */
    Method: string,
    /** A life cycle stage where the method applies. */
    Phase?: string,
    /** A stage from the life cycle of a field such as hardware or AI. */
    Custom_Phase?: CweCustomPhase[],
    /** How the method applies to this weakness. */
    Description: string,
    /** How well the method finds the weakness. */
    Effectiveness?: string,
    /** The strengths and limits of the method here. */
    Effectiveness_Notes?: string,
}


/**
 * One way of preventing a weakness or reducing what it can do.
 */
export interface CweMitigation {
    /** An identifier that lets entries share this text, such as MIT-5. */
    Mitigation_ID?: string,
    /** A life cycle stage where the mitigation applies. */
    Phase?: string,
    /** A stage from the life cycle of a field such as hardware or AI. */
    Custom_Phase?: CweCustomPhase[],
    /** The general approach the mitigation follows. */
    Strategy?: string,
    /** What to do, with its strengths and limits. */
    Description: string,
    /** How well the mitigation prevents the weakness. */
    Effectiveness?: string,
    /** The strengths and limits of the mitigation here. */
    Effectiveness_Notes?: string,
}


/**
 * A worked example of how a weakness looks in code.
 */
export interface CweDemonstrativeExample {
    /** An identifier that lets entries share this example, such as DX-221. */
    Demonstrative_Example_ID?: string,
    /** A title for the example. */
    Title_Text?: string,
    /** The setting of the code, and what it is trying to do. */
    Intro_Text: string,
    /** The example's prose and code, in the order they are meant to be read. */
    Entries?: CweExampleEntry[],
}


/**
 * One step of a worked example, either some prose or some code.
 */
export interface CweExampleEntry {
    /** Prose that explains the code around it. */
    Body_Text?: string,
    /** A block of code. */
    Example_Code?: CweExampleCode,
}


/**
 * A block of code in a worked example.
 */
export interface CweExampleCode {
    /** What the code shows. */
    Nature: string,
    /** The language of the code. */
    Language?: string,
    /** The code, as an XHTML fragment with its special characters escaped. */
    Value?: string,
}


/**
 * A real case of a weakness, usually a CVE record.
 */
export interface CweObservedExample {
    /** The identifier of the case, such as a CVE identifier. */
    Reference: string,
    /** What went wrong in that case, as it bears on the weakness. */
    Description: string,
    /** An address with more about the case. */
    Link: string,
    /** A hint at why this case was chosen. */
    Rationale?: string,
}


/**
 * A pointer from a weakness to an attack pattern in the CAPEC list.
 */
export interface CweRelatedAttackPattern {
    /** The number of the attack pattern in the CAPEC list. */
    CAPEC_ID: string,
}


/**
 * A group of people who may find a view useful.
 */
export interface CweStakeholder {
    /** The group. */
    Type: string,
    /** What in the view this group may find useful. */
    Description?: string,
}


/**
 * A link from a grouping or a view to an entry it holds or belongs to, in one view.
 */
export interface CweMember {
    /** The entry at the other end of the link. */
    CWE_ID: CweEntryID,
    /** The view in which the link holds. */
    View_ID: CweViewID,
    /** The aspects in which the two entries differ. */
    Dimensions?: CweDimension[],
}


/**
 * The entries that a grouping or a view holds or belongs to.
 */
export interface CweRelationships {
    /** An entry that holds this one. */
    Member_Of?: CweMember[],
    /** An entry that this one holds. */
    Has_Member?: CweMember[],
}


/**
 * Guidance on whether to map a real vulnerability to an entry, and on what to use instead.
 */
export interface CweMappingNotes {
    /** Whether the entry may be used for mapping. */
    Usage: string,
    /** Why the entry has that usage. */
    Rationale: string,
    /** More advice for someone mapping to the entry. */
    Comments: string,
    /** Short labels that sum up the usage. */
    Reasons: CweMappingReason[],
    /** Other weaknesses that may suit the mapping better. */
    Suggestions?: CweMappingSuggestion[],
}


/**
 * One short label that sums up the usage of an entry.
 */
export interface CweMappingReason {
    /** The label. */
    Type: string,
}


/**
 * A weakness that may suit a mapping better than this entry.
 */
export interface CweMappingSuggestion {
    /** The suggested weakness. */
    CWE_ID: CweWeaknessID,
    /** When the suggestion applies. */
    Comment: string,
}


/**
 * One release of the CWE List, with all its entries and the sources they cite.
 */
export interface CweWeaknessCatalog {
    /** The name of the catalogue, which is CWE. */
    Name: string,
    /** The version of this release. */
    Version: string,
    /** The date of this release. */
    Date: date,
    /** The weakness entries. */
    Weaknesses?: CweWeakness[],
    /** The grouping entries. */
    Groupings?: CweGrouping[],
    /** The view entries. */
    Views?: CweView[],
    /** The sources that the entries cite. */
    External_References?: CweExternalReference[],
}



