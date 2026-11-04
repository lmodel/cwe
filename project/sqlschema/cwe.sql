-- # Class: CweWeaknessCatalog Description: One release of the CWE List, with all its entries and the sources they cite.
--     * Slot: id
--     * Slot: Name Description: The name of the catalogue, which is CWE.
--     * Slot: Version Description: The version of this release.
--     * Slot: Date Description: The date of this release.
-- # Class: CweExternalReference Description: A source that entries of the catalogue cite, such as a paper, a book or a web page.
--     * Slot: Reference_ID Description: The identifier entries use to cite this source.
--     * Slot: Title Description: The title of the source.
--     * Slot: Edition Description: The edition of the source.
--     * Slot: Publication Description: The journal, conference or other publication that holds the source.
--     * Slot: Publication_Year Description: The year the source came out.
--     * Slot: Publication_Month Description: The month the source came out.
--     * Slot: Publication_Day Description: The day of the month the source came out.
--     * Slot: Publisher Description: Who published the source.
--     * Slot: URL Description: An address where the source can be read.
--     * Slot: URL_Date Description: The date on which the address was last seen to work.
--     * Slot: Alt_URL Description: Another address of the source, usually one with fewer restrictions.
--     * Slot: Alt_URL_Date Description: The date on which the other address was last seen to work.
--     * Slot: Access_Restrictions Description: What stands between a reader and the source.
--     * Slot: CweWeaknessCatalog_id Description: Autocreated FK slot
-- # Class: CweReference Description: A citation of an external reference from an entry or from one of its parts.
--     * Slot: id
--     * Slot: External_Reference_ID Description: The external reference being cited.
--     * Slot: Section Description: The section or page of the source that this citation means.
--     * Slot: CweEntry_ID Description: Autocreated FK slot
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: CweGrouping_ID Description: Autocreated FK slot
--     * Slot: CweView_ID Description: Autocreated FK slot
-- # Class: CweDimension Description: One aspect of a weakness, or of how two weaknesses differ, named in a word or two.
--     * Slot: id
--     * Slot: Type Description: The kind of aspect, such as a behaviour or a resource.
--     * Slot: Value Description: The aspect itself, such as Generation or Page.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: CweRelatedWeakness_id Description: Autocreated FK slot
--     * Slot: CweMember_id Description: Autocreated FK slot
-- # Class: CweCustomPhase Description: A life cycle stage from a field whose stages differ from those of software.
--     * Slot: id
--     * Slot: Domain Description: The field whose life cycle the stage belongs to.
--     * Slot: Value Description: The stage.
--     * Slot: CweIntroduction_id Description: Autocreated FK slot
--     * Slot: CweDetectionMethod_id Description: Autocreated FK slot
--     * Slot: CweMitigation_id Description: Autocreated FK slot
-- # Class: CweNote Description: A remark on an entry that fits nowhere else.
--     * Slot: id
--     * Slot: Type Description: What the note is about.
--     * Slot: Version Description: The CWE version the note belongs to.
--     * Slot: ReleaseDate Description: The release date of that version.
--     * Slot: Value Description: The text of the note.
--     * Slot: CweEntry_ID Description: Autocreated FK slot
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: CweGrouping_ID Description: Autocreated FK slot
--     * Slot: CweView_ID Description: Autocreated FK slot
-- # Class: CweTaxonomyMapping Description: A link from an entry to an entry of another taxonomy.
--     * Slot: id
--     * Slot: Taxonomy_Name Description: The other taxonomy.
--     * Slot: Entry_ID Description: The identifier of the entry in the other taxonomy.
--     * Slot: Entry_Name Description: The name of the entry in the other taxonomy.
--     * Slot: Mapping_Fit Description: How closely the two entries match.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: CweGrouping_ID Description: Autocreated FK slot
-- # Class: CweContentHistory Description: The record of who wrote an entry and how it has changed since.
--     * Slot: id
-- # Class: CweSubmission Description: Who first submitted an entry, and when it joined the list.
--     * Slot: id
--     * Slot: Submission_Organization Description: The organization the submitter belongs to.
--     * Slot: Submission_Date Description: The date of the submission.
--     * Slot: Submission_Version Description: The first CWE version that held the submission.
--     * Slot: Submission_ReleaseDate Description: The release date of that version.
--     * Slot: Submission_Comment Description: A remark on the submission.
--     * Slot: CweContentHistory_id Description: Autocreated FK slot
-- # Class: CweModification Description: One change made to an entry.
--     * Slot: id
--     * Slot: Modification_Name Description: The person who made or suggested the change.
--     * Slot: Modification_Organization Description: The organization that person belongs to.
--     * Slot: Modification_Date Description: The date of the change.
--     * Slot: Modification_Version Description: The first CWE version that held the change.
--     * Slot: Modification_ReleaseDate Description: The release date of that version.
--     * Slot: Modification_Importance Description: How much the change matters to people who rely on the entry.
--     * Slot: Modification_Comment Description: What changed.
--     * Slot: CweContentHistory_id Description: Autocreated FK slot
-- # Class: CweContribution Description: Feedback or content that someone gave to an entry.
--     * Slot: id
--     * Slot: Type Description: Whether the contribution was feedback or content.
--     * Slot: Contribution_Organization Description: The organization the contributor belongs to.
--     * Slot: Contribution_Date Description: The date of the contribution.
--     * Slot: Contribution_Version Description: The first CWE version that held the contribution.
--     * Slot: Contribution_ReleaseDate Description: The release date of that version.
--     * Slot: Contribution_Comment Description: A remark on the contribution.
--     * Slot: CweContentHistory_id Description: Autocreated FK slot
-- # Class: CwePreviousEntryName Description: A name an entry had before.
--     * Slot: id
--     * Slot: Date Description: The date the name stopped being used.
--     * Slot: Version Description: The CWE version in which the name changed.
--     * Slot: Value Description: The earlier name.
--     * Slot: CweContentHistory_id Description: Autocreated FK slot
-- # Abstract Class: CweEntry Description: Any item of the CWE List that has an identifier of its own: a weakness, a grouping or a view.
--     * Slot: ID Description: The number that identifies the entry across the whole list.
--     * Slot: Name Description: The name of the entry.
--     * Slot: Status Description: How far the entry has come and how much it can be trusted.
--     * Slot: Mapping_Notes_id Description: Guidance on whether to map a real vulnerability to this entry.
--     * Slot: Content_History_id Description: Who wrote the entry and how it has changed since.
-- # Class: CweWeakness Description: A type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack.
--     * Slot: Abstraction Description: How far the weakness is described in general terms or tied to a specific product.
--     * Slot: Structure Description: Whether the weakness stands alone or is made up of others.
--     * Slot: Diagram Description: The path on MITRE's site of a diagram of the weakness.
--     * Slot: Description Description: A sentence or two that define the weakness.
--     * Slot: Extended_Description Description: More about the weakness than its short description gives.
--     * Slot: Technical_Nuance Description: Finer technical detail that helps tell this weakness from close relatives.
--     * Slot: Likelihood_Of_Exploit Description: How likely it is that the weakness gets exploited.
--     * Slot: ID Description: The number that identifies the entry across the whole list.
--     * Slot: Name Description: The name of the entry.
--     * Slot: Status Description: How far the entry has come and how much it can be trusted.
--     * Slot: CweWeaknessCatalog_id Description: Autocreated FK slot
--     * Slot: Applicable_Platforms_id Description: The languages, systems, architectures and technologies where the weakness can appear.
--     * Slot: Mapping_Notes_id Description: Guidance on whether to map a real vulnerability to this entry.
--     * Slot: Content_History_id Description: Who wrote the entry and how it has changed since.
-- # Class: CweGrouping Description: A set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category.
--     * Slot: Summary Description: What the grouped weaknesses have in common.
--     * Slot: ID Description: The number that identifies the entry across the whole list.
--     * Slot: Name Description: The name of the entry.
--     * Slot: Status Description: How far the entry has come and how much it can be trusted.
--     * Slot: CweWeaknessCatalog_id Description: Autocreated FK slot
--     * Slot: Relationships_id Description: The entries this grouping holds.
--     * Slot: Mapping_Notes_id Description: Guidance on whether to map a real vulnerability to this entry.
--     * Slot: Content_History_id Description: Who wrote the entry and how it has changed since.
-- # Class: CweView Description: A way of looking at the catalogue, as a subset of its entries seen from one standpoint.
--     * Slot: Type Description: How the view selects and arranges its entries.
--     * Slot: Objective Description: What the view is for.
--     * Slot: Filter Description: The XPath expression that selects the entries of an implicit slice.
--     * Slot: ID Description: The number that identifies the entry across the whole list.
--     * Slot: Name Description: The name of the entry.
--     * Slot: Status Description: How far the entry has come and how much it can be trusted.
--     * Slot: CweWeaknessCatalog_id Description: Autocreated FK slot
--     * Slot: Members_id Description: The entries a view names one by one, when it is not selected by a filter.
--     * Slot: Mapping_Notes_id Description: Guidance on whether to map a real vulnerability to this entry.
--     * Slot: Content_History_id Description: Who wrote the entry and how it has changed since.
-- # Class: CweRelatedWeakness Description: A link from a weakness to another weakness, in one view.
--     * Slot: id
--     * Slot: Nature Description: How the two weaknesses relate.
--     * Slot: CWE_ID Description: The weakness at the other end of the link.
--     * Slot: View_ID Description: The view in which the link holds.
--     * Slot: Chain_ID Description: The named chain that the link belongs to.
--     * Slot: Ordinal Description: Marks this as the link to prefer in the view.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweWeaknessOrdinality Description: Whether a weakness tends to be a first cause or the result of another.
--     * Slot: id
--     * Slot: Ordinality Description: The position in the sequence of causes.
--     * Slot: Description Description: The setting in which the weakness takes this position.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweApplicablePlatforms Description: The kinds of platform where a weakness can appear.
--     * Slot: id
-- # Class: CweLanguagePlatform Description: A language where a weakness can appear, named or by its family.
--     * Slot: id
--     * Slot: Name Description: The name of the language.
--     * Slot: Class Description: The family of languages.
--     * Slot: Prevalence Description: How regularly the weakness applies here.
--     * Slot: Note Description: A remark on this platform.
--     * Slot: CweApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: CweOperatingSystemPlatform Description: An operating system where a weakness can appear, named or by its family.
--     * Slot: id
--     * Slot: Name Description: The name of the operating system.
--     * Slot: Version Description: The version of the operating system.
--     * Slot: CPE_ID Description: The Common Platform Enumeration name of the operating system.
--     * Slot: Class Description: The family of operating systems.
--     * Slot: Prevalence Description: How regularly the weakness applies here.
--     * Slot: Note Description: A remark on this platform.
--     * Slot: CweApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: CweArchitecturePlatform Description: A hardware architecture where a weakness can appear, named or by its family.
--     * Slot: id
--     * Slot: Name Description: The name of the architecture.
--     * Slot: Class Description: The family of architectures.
--     * Slot: Prevalence Description: How regularly the weakness applies here.
--     * Slot: Note Description: A remark on this platform.
--     * Slot: CweApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: CweTechnologyPlatform Description: A technology where a weakness can appear, named or by its family.
--     * Slot: id
--     * Slot: Name Description: The name of the technology.
--     * Slot: Class Description: The family of technologies.
--     * Slot: Prevalence Description: How regularly the weakness applies here.
--     * Slot: Note Description: A remark on this platform.
--     * Slot: CweApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: CweAlternateTerm Description: Another name people use for a weakness.
--     * Slot: id
--     * Slot: Term Description: The name.
--     * Slot: Description Description: When and how the name is used.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweIntroduction Description: One way a weakness can get into a product.
--     * Slot: id
--     * Slot: Note Description: The usual way this happens.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweConsequence Description: One thing that can follow when a weakness is exploited.
--     * Slot: id
--     * Slot: Consequence_ID Description: An identifier for this consequence.
--     * Slot: Likelihood Description: How likely this consequence is beside the others.
--     * Slot: Note Description: A remark on the consequence.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweDetectionMethod Description: One way of finding a weakness.
--     * Slot: id
--     * Slot: Detection_Method_ID Description: An identifier that lets entries share this text, such as DM-14.
--     * Slot: Method Description: The way of finding the weakness.
--     * Slot: Description Description: How the method applies to this weakness.
--     * Slot: Effectiveness Description: How well the method finds the weakness.
--     * Slot: Effectiveness_Notes Description: The strengths and limits of the method here.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweMitigation Description: One way of preventing a weakness or reducing what it can do.
--     * Slot: id
--     * Slot: Mitigation_ID Description: An identifier that lets entries share this text, such as MIT-5.
--     * Slot: Strategy Description: The general approach the mitigation follows.
--     * Slot: Description Description: What to do, with its strengths and limits.
--     * Slot: Effectiveness Description: How well the mitigation prevents the weakness.
--     * Slot: Effectiveness_Notes Description: The strengths and limits of the mitigation here.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweDemonstrativeExample Description: A worked example of how a weakness looks in code.
--     * Slot: id
--     * Slot: Demonstrative_Example_ID Description: An identifier that lets entries share this example, such as DX-221.
--     * Slot: Title_Text Description: A title for the example.
--     * Slot: Intro_Text Description: The setting of the code, and what it is trying to do.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweExampleEntry Description: One step of a worked example, either some prose or some code.
--     * Slot: id
--     * Slot: Body_Text Description: Prose that explains the code around it.
--     * Slot: CweDemonstrativeExample_id Description: Autocreated FK slot
--     * Slot: Example_Code_id Description: A block of code.
-- # Class: CweExampleCode Description: A block of code in a worked example.
--     * Slot: id
--     * Slot: Nature Description: What the code shows.
--     * Slot: Language Description: The language of the code.
--     * Slot: Value Description: The code, as an XHTML fragment with its special characters escaped.
-- # Class: CweObservedExample Description: A real case of a weakness, usually a CVE record.
--     * Slot: id
--     * Slot: Reference Description: The identifier of the case, such as a CVE identifier.
--     * Slot: Description Description: What went wrong in that case, as it bears on the weakness.
--     * Slot: Link Description: An address with more about the case.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweRelatedAttackPattern Description: A pointer from a weakness to an attack pattern in the CAPEC list.
--     * Slot: id
--     * Slot: CAPEC_ID Description: The number of the attack pattern in the CAPEC list.
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
-- # Class: CweStakeholder Description: A group of people who may find a view useful.
--     * Slot: id
--     * Slot: Type Description: The group.
--     * Slot: Description Description: What in the view this group may find useful.
--     * Slot: CweView_ID Description: Autocreated FK slot
-- # Class: CweMember Description: A link from a grouping or a view to an entry it holds or belongs to, in one view.
--     * Slot: id
--     * Slot: CWE_ID Description: The entry at the other end of the link.
--     * Slot: View_ID Description: The view in which the link holds.
--     * Slot: CweRelationships_id Description: Autocreated FK slot
-- # Class: CweRelationships Description: The entries that a grouping or a view holds or belongs to.
--     * Slot: id
-- # Class: CweMappingNotes Description: Guidance on whether to map a real vulnerability to an entry, and on what to use instead.
--     * Slot: id
--     * Slot: Usage Description: Whether the entry may be used for mapping.
--     * Slot: Rationale Description: Why the entry has that usage.
--     * Slot: Comments Description: More advice for someone mapping to the entry.
-- # Class: CweMappingReason Description: One short label that sums up the usage of an entry.
--     * Slot: id
--     * Slot: Type Description: The label.
--     * Slot: CweMappingNotes_id Description: Autocreated FK slot
-- # Class: CweMappingSuggestion Description: A weakness that may suit a mapping better than this entry.
--     * Slot: id
--     * Slot: CWE_ID Description: The suggested weakness.
--     * Slot: Comment Description: When the suggestion applies.
--     * Slot: CweMappingNotes_id Description: Autocreated FK slot
-- # Class: CweExternalReference_Author
--     * Slot: CweExternalReference_Reference_ID Description: Autocreated FK slot
--     * Slot: Author Description: A person or group who wrote the source.
-- # Class: CweExternalReference_Media_Type
--     * Slot: CweExternalReference_Reference_ID Description: Autocreated FK slot
--     * Slot: Media_Type Description: A form the source takes.
-- # Class: CweExternalReference_Rationale
--     * Slot: CweExternalReference_Reference_ID Description: Autocreated FK slot
--     * Slot: Rationale Description: A hint at why the source was cited.
-- # Class: CweSubmission_Submission_Name
--     * Slot: CweSubmission_id Description: Autocreated FK slot
--     * Slot: Submission_Name Description: A person or group who submitted the entry.
-- # Class: CweContribution_Contribution_Name
--     * Slot: CweContribution_id Description: Autocreated FK slot
--     * Slot: Contribution_Name Description: A person or group who contributed.
-- # Class: CweWeakness_Background_Details
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: Background_Details Description: Background that helps a reader but does not describe the weakness itself.
-- # Class: CweWeakness_Exploitation_Factors
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: Exploitation_Factors Description: Conditions that make exploiting the weakness more likely.
-- # Class: CweWeakness_Functional_Areas
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: Functional_Areas Description: The parts of a product where the weakness tends to appear.
-- # Class: CweWeakness_Affected_Resources
--     * Slot: CweWeakness_ID Description: Autocreated FK slot
--     * Slot: Affected_Resources Description: The system resources that exploiting the weakness can affect.
-- # Class: CweAlternateTerm_Role
--     * Slot: CweAlternateTerm_id Description: Autocreated FK slot
--     * Slot: Role Description: The part the name plays when people talk about the weakness.
-- # Class: CweIntroduction_Phase
--     * Slot: CweIntroduction_id Description: Autocreated FK slot
--     * Slot: Phase Description: A life cycle stage where the weakness can get in.
-- # Class: CweConsequence_Scope
--     * Slot: CweConsequence_id Description: Autocreated FK slot
--     * Slot: Scope Description: A security property the consequence violates.
-- # Class: CweConsequence_Impact
--     * Slot: CweConsequence_id Description: Autocreated FK slot
--     * Slot: Impact Description: What an attacker can achieve.
-- # Class: CweDetectionMethod_Phase
--     * Slot: CweDetectionMethod_id Description: Autocreated FK slot
--     * Slot: Phase Description: A life cycle stage where the method applies.
-- # Class: CweMitigation_Phase
--     * Slot: CweMitigation_id Description: Autocreated FK slot
--     * Slot: Phase Description: A life cycle stage where the mitigation applies.
-- # Class: CweObservedExample_Rationale
--     * Slot: CweObservedExample_id Description: Autocreated FK slot
--     * Slot: Rationale Description: A hint at why this case was chosen.

CREATE TABLE "CweWeaknessCatalog" (
	id INTEGER NOT NULL,
	"Name" TEXT NOT NULL,
	"Version" TEXT NOT NULL,
	"Date" DATE NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweWeaknessCatalog_id" ON "CweWeaknessCatalog" (id);

CREATE TABLE "CweContentHistory" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweContentHistory_id" ON "CweContentHistory" (id);

CREATE TABLE "CweApplicablePlatforms" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweApplicablePlatforms_id" ON "CweApplicablePlatforms" (id);

CREATE TABLE "CweExampleCode" (
	id INTEGER NOT NULL,
	"Nature" VARCHAR(11) NOT NULL,
	"Language" VARCHAR(13),
	"Value" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweExampleCode_id" ON "CweExampleCode" (id);

CREATE TABLE "CweRelationships" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweRelationships_id" ON "CweRelationships" (id);

CREATE TABLE "CweMappingNotes" (
	id INTEGER NOT NULL,
	"Usage" VARCHAR(19) NOT NULL,
	"Rationale" TEXT NOT NULL,
	"Comments" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CweMappingNotes_id" ON "CweMappingNotes" (id);

CREATE TABLE "CweExternalReference" (
	"Reference_ID" TEXT NOT NULL,
	"Title" TEXT NOT NULL,
	"Edition" TEXT,
	"Publication" TEXT,
	"Publication_Year" TEXT,
	"Publication_Month" TEXT,
	"Publication_Day" TEXT,
	"Publisher" TEXT,
	"URL" TEXT,
	"URL_Date" DATE,
	"Alt_URL" TEXT,
	"Alt_URL_Date" DATE,
	"Access_Restrictions" VARCHAR(24),
	"CweWeaknessCatalog_id" INTEGER,
	PRIMARY KEY ("Reference_ID"),
	FOREIGN KEY("CweWeaknessCatalog_id") REFERENCES "CweWeaknessCatalog" (id)
);
CREATE INDEX "ix_CweExternalReference_Reference_ID" ON "CweExternalReference" ("Reference_ID");

CREATE TABLE "CweSubmission" (
	id INTEGER NOT NULL,
	"Submission_Organization" TEXT,
	"Submission_Date" DATE NOT NULL,
	"Submission_Version" TEXT NOT NULL,
	"Submission_ReleaseDate" DATE NOT NULL,
	"Submission_Comment" TEXT,
	"CweContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweContentHistory_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweSubmission_id" ON "CweSubmission" (id);

CREATE TABLE "CweModification" (
	id INTEGER NOT NULL,
	"Modification_Name" TEXT,
	"Modification_Organization" TEXT,
	"Modification_Date" DATE NOT NULL,
	"Modification_Version" TEXT NOT NULL,
	"Modification_ReleaseDate" DATE NOT NULL,
	"Modification_Importance" VARCHAR(8),
	"Modification_Comment" TEXT NOT NULL,
	"CweContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweContentHistory_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweModification_id" ON "CweModification" (id);

CREATE TABLE "CweContribution" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(8) NOT NULL,
	"Contribution_Organization" TEXT,
	"Contribution_Date" DATE NOT NULL,
	"Contribution_Version" TEXT NOT NULL,
	"Contribution_ReleaseDate" DATE NOT NULL,
	"Contribution_Comment" TEXT,
	"CweContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweContentHistory_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweContribution_id" ON "CweContribution" (id);

CREATE TABLE "CwePreviousEntryName" (
	id INTEGER NOT NULL,
	"Date" DATE NOT NULL,
	"Version" TEXT,
	"Value" TEXT NOT NULL,
	"CweContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweContentHistory_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CwePreviousEntryName_id" ON "CwePreviousEntryName" (id);

CREATE TABLE "CweEntry" (
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"Mapping_Notes_id" INTEGER NOT NULL,
	"Content_History_id" INTEGER NOT NULL,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("Mapping_Notes_id") REFERENCES "CweMappingNotes" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweEntry_ID" ON "CweEntry" ("ID");

CREATE TABLE "CweWeakness" (
	"Abstraction" VARCHAR(8) NOT NULL,
	"Structure" VARCHAR(9) NOT NULL,
	"Diagram" TEXT,
	"Description" TEXT NOT NULL,
	"Extended_Description" TEXT,
	"Technical_Nuance" TEXT,
	"Likelihood_Of_Exploit" VARCHAR(7),
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CweWeaknessCatalog_id" INTEGER,
	"Applicable_Platforms_id" INTEGER,
	"Mapping_Notes_id" INTEGER NOT NULL,
	"Content_History_id" INTEGER NOT NULL,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CweWeaknessCatalog_id") REFERENCES "CweWeaknessCatalog" (id),
	FOREIGN KEY("Applicable_Platforms_id") REFERENCES "CweApplicablePlatforms" (id),
	FOREIGN KEY("Mapping_Notes_id") REFERENCES "CweMappingNotes" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweWeakness_ID" ON "CweWeakness" ("ID");

CREATE TABLE "CweGrouping" (
	"Summary" TEXT NOT NULL,
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CweWeaknessCatalog_id" INTEGER,
	"Relationships_id" INTEGER,
	"Mapping_Notes_id" INTEGER NOT NULL,
	"Content_History_id" INTEGER NOT NULL,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CweWeaknessCatalog_id") REFERENCES "CweWeaknessCatalog" (id),
	FOREIGN KEY("Relationships_id") REFERENCES "CweRelationships" (id),
	FOREIGN KEY("Mapping_Notes_id") REFERENCES "CweMappingNotes" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweGrouping_ID" ON "CweGrouping" ("ID");

CREATE TABLE "CweView" (
	"Type" VARCHAR(8) NOT NULL,
	"Objective" TEXT NOT NULL,
	"Filter" TEXT,
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CweWeaknessCatalog_id" INTEGER,
	"Members_id" INTEGER,
	"Mapping_Notes_id" INTEGER NOT NULL,
	"Content_History_id" INTEGER NOT NULL,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CweWeaknessCatalog_id") REFERENCES "CweWeaknessCatalog" (id),
	FOREIGN KEY("Members_id") REFERENCES "CweRelationships" (id),
	FOREIGN KEY("Mapping_Notes_id") REFERENCES "CweMappingNotes" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CweContentHistory" (id)
);
CREATE INDEX "ix_CweView_ID" ON "CweView" ("ID");

CREATE TABLE "CweLanguagePlatform" (
	id INTEGER NOT NULL,
	"Name" VARCHAR(13),
	"Class" VARCHAR(29),
	"Prevalence" VARCHAR(12) NOT NULL,
	"Note" TEXT,
	"CweApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweApplicablePlatforms_id") REFERENCES "CweApplicablePlatforms" (id)
);
CREATE INDEX "ix_CweLanguagePlatform_id" ON "CweLanguagePlatform" (id);

CREATE TABLE "CweOperatingSystemPlatform" (
	id INTEGER NOT NULL,
	"Name" VARCHAR(16),
	"Version" TEXT,
	"CPE_ID" TEXT,
	"Class" VARCHAR(15),
	"Prevalence" VARCHAR(12) NOT NULL,
	"Note" TEXT,
	"CweApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweApplicablePlatforms_id") REFERENCES "CweApplicablePlatforms" (id)
);
CREATE INDEX "ix_CweOperatingSystemPlatform_id" ON "CweOperatingSystemPlatform" (id);

CREATE TABLE "CweArchitecturePlatform" (
	id INTEGER NOT NULL,
	"Name" VARCHAR(18),
	"Class" VARCHAR(25),
	"Prevalence" VARCHAR(12) NOT NULL,
	"Note" TEXT,
	"CweApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweApplicablePlatforms_id") REFERENCES "CweApplicablePlatforms" (id)
);
CREATE INDEX "ix_CweArchitecturePlatform_id" ON "CweArchitecturePlatform" (id);

CREATE TABLE "CweTechnologyPlatform" (
	id INTEGER NOT NULL,
	"Name" VARCHAR(32),
	"Class" VARCHAR(23),
	"Prevalence" VARCHAR(12) NOT NULL,
	"Note" TEXT,
	"CweApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweApplicablePlatforms_id") REFERENCES "CweApplicablePlatforms" (id)
);
CREATE INDEX "ix_CweTechnologyPlatform_id" ON "CweTechnologyPlatform" (id);

CREATE TABLE "CweMappingReason" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(26) NOT NULL,
	"CweMappingNotes_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweMappingNotes_id") REFERENCES "CweMappingNotes" (id)
);
CREATE INDEX "ix_CweMappingReason_id" ON "CweMappingReason" (id);

CREATE TABLE "CweReference" (
	id INTEGER NOT NULL,
	"External_Reference_ID" TEXT NOT NULL,
	"Section" TEXT,
	"CweEntry_ID" TEXT,
	"CweWeakness_ID" TEXT,
	"CweGrouping_ID" TEXT,
	"CweView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("External_Reference_ID") REFERENCES "CweExternalReference" ("Reference_ID"),
	FOREIGN KEY("CweEntry_ID") REFERENCES "CweEntry" ("ID"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweGrouping_ID") REFERENCES "CweGrouping" ("ID"),
	FOREIGN KEY("CweView_ID") REFERENCES "CweView" ("ID")
);
CREATE INDEX "ix_CweReference_id" ON "CweReference" (id);

CREATE TABLE "CweNote" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(19) NOT NULL,
	"Version" TEXT,
	"ReleaseDate" DATE,
	"Value" TEXT,
	"CweEntry_ID" TEXT,
	"CweWeakness_ID" TEXT,
	"CweGrouping_ID" TEXT,
	"CweView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweEntry_ID") REFERENCES "CweEntry" ("ID"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweGrouping_ID") REFERENCES "CweGrouping" ("ID"),
	FOREIGN KEY("CweView_ID") REFERENCES "CweView" ("ID")
);
CREATE INDEX "ix_CweNote_id" ON "CweNote" (id);

CREATE TABLE "CweTaxonomyMapping" (
	id INTEGER NOT NULL,
	"Taxonomy_Name" VARCHAR(54) NOT NULL,
	"Entry_ID" TEXT,
	"Entry_Name" TEXT,
	"Mapping_Fit" VARCHAR(17),
	"CweWeakness_ID" TEXT,
	"CweGrouping_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweGrouping_ID") REFERENCES "CweGrouping" ("ID")
);
CREATE INDEX "ix_CweTaxonomyMapping_id" ON "CweTaxonomyMapping" (id);

CREATE TABLE "CweRelatedWeakness" (
	id INTEGER NOT NULL,
	"Nature" VARCHAR(10) NOT NULL,
	"CWE_ID" TEXT NOT NULL,
	"View_ID" TEXT NOT NULL,
	"Chain_ID" TEXT,
	"Ordinal" VARCHAR(7),
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CWE_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("View_ID") REFERENCES "CweView" ("ID"),
	FOREIGN KEY("Chain_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweRelatedWeakness_id" ON "CweRelatedWeakness" (id);

CREATE TABLE "CweWeaknessOrdinality" (
	id INTEGER NOT NULL,
	"Ordinality" VARCHAR(9) NOT NULL,
	"Description" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweWeaknessOrdinality_id" ON "CweWeaknessOrdinality" (id);

CREATE TABLE "CweAlternateTerm" (
	id INTEGER NOT NULL,
	"Term" TEXT NOT NULL,
	"Description" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweAlternateTerm_id" ON "CweAlternateTerm" (id);

CREATE TABLE "CweIntroduction" (
	id INTEGER NOT NULL,
	"Note" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweIntroduction_id" ON "CweIntroduction" (id);

CREATE TABLE "CweConsequence" (
	id INTEGER NOT NULL,
	"Consequence_ID" TEXT,
	"Likelihood" VARCHAR(7),
	"Note" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweConsequence_id" ON "CweConsequence" (id);

CREATE TABLE "CweDetectionMethod" (
	id INTEGER NOT NULL,
	"Detection_Method_ID" TEXT,
	"Method" VARCHAR(54) NOT NULL,
	"Description" TEXT NOT NULL,
	"Effectiveness" VARCHAR(13),
	"Effectiveness_Notes" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweDetectionMethod_id" ON "CweDetectionMethod" (id);

CREATE TABLE "CweMitigation" (
	id INTEGER NOT NULL,
	"Mitigation_ID" TEXT,
	"Strategy" VARCHAR(30),
	"Description" TEXT NOT NULL,
	"Effectiveness" VARCHAR(27),
	"Effectiveness_Notes" TEXT,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweMitigation_id" ON "CweMitigation" (id);

CREATE TABLE "CweDemonstrativeExample" (
	id INTEGER NOT NULL,
	"Demonstrative_Example_ID" TEXT,
	"Title_Text" TEXT,
	"Intro_Text" TEXT NOT NULL,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweDemonstrativeExample_id" ON "CweDemonstrativeExample" (id);

CREATE TABLE "CweObservedExample" (
	id INTEGER NOT NULL,
	"Reference" TEXT NOT NULL,
	"Description" TEXT NOT NULL,
	"Link" TEXT NOT NULL,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweObservedExample_id" ON "CweObservedExample" (id);

CREATE TABLE "CweRelatedAttackPattern" (
	id INTEGER NOT NULL,
	"CAPEC_ID" TEXT NOT NULL,
	"CweWeakness_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweRelatedAttackPattern_id" ON "CweRelatedAttackPattern" (id);

CREATE TABLE "CweStakeholder" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(23) NOT NULL,
	"Description" TEXT,
	"CweView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CweView_ID") REFERENCES "CweView" ("ID")
);
CREATE INDEX "ix_CweStakeholder_id" ON "CweStakeholder" (id);

CREATE TABLE "CweMember" (
	id INTEGER NOT NULL,
	"CWE_ID" TEXT NOT NULL,
	"View_ID" TEXT NOT NULL,
	"CweRelationships_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CWE_ID") REFERENCES "CweEntry" ("ID"),
	FOREIGN KEY("View_ID") REFERENCES "CweView" ("ID"),
	FOREIGN KEY("CweRelationships_id") REFERENCES "CweRelationships" (id)
);
CREATE INDEX "ix_CweMember_id" ON "CweMember" (id);

CREATE TABLE "CweMappingSuggestion" (
	id INTEGER NOT NULL,
	"CWE_ID" TEXT NOT NULL,
	"Comment" TEXT NOT NULL,
	"CweMappingNotes_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CWE_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweMappingNotes_id") REFERENCES "CweMappingNotes" (id)
);
CREATE INDEX "ix_CweMappingSuggestion_id" ON "CweMappingSuggestion" (id);

CREATE TABLE "CweExternalReference_Author" (
	"CweExternalReference_Reference_ID" TEXT,
	"Author" TEXT,
	PRIMARY KEY ("CweExternalReference_Reference_ID", "Author"),
	FOREIGN KEY("CweExternalReference_Reference_ID") REFERENCES "CweExternalReference" ("Reference_ID")
);
CREATE INDEX "ix_CweExternalReference_Author_Author" ON "CweExternalReference_Author" ("Author");
CREATE INDEX "ix_CweExternalReference_Author_CweExternalReference_Reference_ID" ON "CweExternalReference_Author" ("CweExternalReference_Reference_ID");

CREATE TABLE "CweExternalReference_Media_Type" (
	"CweExternalReference_Reference_ID" TEXT,
	"Media_Type" VARCHAR(23),
	PRIMARY KEY ("CweExternalReference_Reference_ID", "Media_Type"),
	FOREIGN KEY("CweExternalReference_Reference_ID") REFERENCES "CweExternalReference" ("Reference_ID")
);
CREATE INDEX "ix_CweExternalReference_Media_Type_CweExternalReference_Reference_ID" ON "CweExternalReference_Media_Type" ("CweExternalReference_Reference_ID");
CREATE INDEX "ix_CweExternalReference_Media_Type_Media_Type" ON "CweExternalReference_Media_Type" ("Media_Type");

CREATE TABLE "CweExternalReference_Rationale" (
	"CweExternalReference_Reference_ID" TEXT,
	"Rationale" VARCHAR(24),
	PRIMARY KEY ("CweExternalReference_Reference_ID", "Rationale"),
	FOREIGN KEY("CweExternalReference_Reference_ID") REFERENCES "CweExternalReference" ("Reference_ID")
);
CREATE INDEX "ix_CweExternalReference_Rationale_Rationale" ON "CweExternalReference_Rationale" ("Rationale");
CREATE INDEX "ix_CweExternalReference_Rationale_CweExternalReference_Reference_ID" ON "CweExternalReference_Rationale" ("CweExternalReference_Reference_ID");

CREATE TABLE "CweSubmission_Submission_Name" (
	"CweSubmission_id" INTEGER,
	"Submission_Name" TEXT,
	PRIMARY KEY ("CweSubmission_id", "Submission_Name"),
	FOREIGN KEY("CweSubmission_id") REFERENCES "CweSubmission" (id)
);
CREATE INDEX "ix_CweSubmission_Submission_Name_Submission_Name" ON "CweSubmission_Submission_Name" ("Submission_Name");
CREATE INDEX "ix_CweSubmission_Submission_Name_CweSubmission_id" ON "CweSubmission_Submission_Name" ("CweSubmission_id");

CREATE TABLE "CweContribution_Contribution_Name" (
	"CweContribution_id" INTEGER,
	"Contribution_Name" TEXT,
	PRIMARY KEY ("CweContribution_id", "Contribution_Name"),
	FOREIGN KEY("CweContribution_id") REFERENCES "CweContribution" (id)
);
CREATE INDEX "ix_CweContribution_Contribution_Name_CweContribution_id" ON "CweContribution_Contribution_Name" ("CweContribution_id");
CREATE INDEX "ix_CweContribution_Contribution_Name_Contribution_Name" ON "CweContribution_Contribution_Name" ("Contribution_Name");

CREATE TABLE "CweWeakness_Background_Details" (
	"CweWeakness_ID" TEXT,
	"Background_Details" TEXT,
	PRIMARY KEY ("CweWeakness_ID", "Background_Details"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweWeakness_Background_Details_CweWeakness_ID" ON "CweWeakness_Background_Details" ("CweWeakness_ID");
CREATE INDEX "ix_CweWeakness_Background_Details_Background_Details" ON "CweWeakness_Background_Details" ("Background_Details");

CREATE TABLE "CweWeakness_Exploitation_Factors" (
	"CweWeakness_ID" TEXT,
	"Exploitation_Factors" TEXT,
	PRIMARY KEY ("CweWeakness_ID", "Exploitation_Factors"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweWeakness_Exploitation_Factors_CweWeakness_ID" ON "CweWeakness_Exploitation_Factors" ("CweWeakness_ID");
CREATE INDEX "ix_CweWeakness_Exploitation_Factors_Exploitation_Factors" ON "CweWeakness_Exploitation_Factors" ("Exploitation_Factors");

CREATE TABLE "CweWeakness_Functional_Areas" (
	"CweWeakness_ID" TEXT,
	"Functional_Areas" VARCHAR(28),
	PRIMARY KEY ("CweWeakness_ID", "Functional_Areas"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweWeakness_Functional_Areas_CweWeakness_ID" ON "CweWeakness_Functional_Areas" ("CweWeakness_ID");
CREATE INDEX "ix_CweWeakness_Functional_Areas_Functional_Areas" ON "CweWeakness_Functional_Areas" ("Functional_Areas");

CREATE TABLE "CweWeakness_Affected_Resources" (
	"CweWeakness_ID" TEXT,
	"Affected_Resources" VARCHAR(17),
	PRIMARY KEY ("CweWeakness_ID", "Affected_Resources"),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID")
);
CREATE INDEX "ix_CweWeakness_Affected_Resources_CweWeakness_ID" ON "CweWeakness_Affected_Resources" ("CweWeakness_ID");
CREATE INDEX "ix_CweWeakness_Affected_Resources_Affected_Resources" ON "CweWeakness_Affected_Resources" ("Affected_Resources");

CREATE TABLE "CweDimension" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(17) NOT NULL,
	"Value" TEXT NOT NULL,
	"CweWeakness_ID" TEXT,
	"CweRelatedWeakness_id" INTEGER,
	"CweMember_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweWeakness_ID") REFERENCES "CweWeakness" ("ID"),
	FOREIGN KEY("CweRelatedWeakness_id") REFERENCES "CweRelatedWeakness" (id),
	FOREIGN KEY("CweMember_id") REFERENCES "CweMember" (id)
);
CREATE INDEX "ix_CweDimension_id" ON "CweDimension" (id);

CREATE TABLE "CweCustomPhase" (
	id INTEGER NOT NULL,
	"Domain" VARCHAR(8) NOT NULL,
	"Value" TEXT NOT NULL,
	"CweIntroduction_id" INTEGER,
	"CweDetectionMethod_id" INTEGER,
	"CweMitigation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweIntroduction_id") REFERENCES "CweIntroduction" (id),
	FOREIGN KEY("CweDetectionMethod_id") REFERENCES "CweDetectionMethod" (id),
	FOREIGN KEY("CweMitigation_id") REFERENCES "CweMitigation" (id)
);
CREATE INDEX "ix_CweCustomPhase_id" ON "CweCustomPhase" (id);

CREATE TABLE "CweExampleEntry" (
	id INTEGER NOT NULL,
	"Body_Text" TEXT,
	"CweDemonstrativeExample_id" INTEGER,
	"Example_Code_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CweDemonstrativeExample_id") REFERENCES "CweDemonstrativeExample" (id),
	FOREIGN KEY("Example_Code_id") REFERENCES "CweExampleCode" (id)
);
CREATE INDEX "ix_CweExampleEntry_id" ON "CweExampleEntry" (id);

CREATE TABLE "CweAlternateTerm_Role" (
	"CweAlternateTerm_id" INTEGER,
	"Role" VARCHAR(23),
	PRIMARY KEY ("CweAlternateTerm_id", "Role"),
	FOREIGN KEY("CweAlternateTerm_id") REFERENCES "CweAlternateTerm" (id)
);
CREATE INDEX "ix_CweAlternateTerm_Role_Role" ON "CweAlternateTerm_Role" ("Role");
CREATE INDEX "ix_CweAlternateTerm_Role_CweAlternateTerm_id" ON "CweAlternateTerm_Role" ("CweAlternateTerm_id");

CREATE TABLE "CweIntroduction_Phase" (
	"CweIntroduction_id" INTEGER,
	"Phase" VARCHAR(31),
	PRIMARY KEY ("CweIntroduction_id", "Phase"),
	FOREIGN KEY("CweIntroduction_id") REFERENCES "CweIntroduction" (id)
);
CREATE INDEX "ix_CweIntroduction_Phase_Phase" ON "CweIntroduction_Phase" ("Phase");
CREATE INDEX "ix_CweIntroduction_Phase_CweIntroduction_id" ON "CweIntroduction_Phase" ("CweIntroduction_id");

CREATE TABLE "CweConsequence_Scope" (
	"CweConsequence_id" INTEGER,
	"Scope" VARCHAR(15) NOT NULL,
	PRIMARY KEY ("CweConsequence_id", "Scope"),
	FOREIGN KEY("CweConsequence_id") REFERENCES "CweConsequence" (id)
);
CREATE INDEX "ix_CweConsequence_Scope_Scope" ON "CweConsequence_Scope" ("Scope");
CREATE INDEX "ix_CweConsequence_Scope_CweConsequence_id" ON "CweConsequence_Scope" ("CweConsequence_id");

CREATE TABLE "CweConsequence_Impact" (
	"CweConsequence_id" INTEGER,
	"Impact" VARCHAR(37) NOT NULL,
	PRIMARY KEY ("CweConsequence_id", "Impact"),
	FOREIGN KEY("CweConsequence_id") REFERENCES "CweConsequence" (id)
);
CREATE INDEX "ix_CweConsequence_Impact_CweConsequence_id" ON "CweConsequence_Impact" ("CweConsequence_id");
CREATE INDEX "ix_CweConsequence_Impact_Impact" ON "CweConsequence_Impact" ("Impact");

CREATE TABLE "CweDetectionMethod_Phase" (
	"CweDetectionMethod_id" INTEGER,
	"Phase" VARCHAR(31),
	PRIMARY KEY ("CweDetectionMethod_id", "Phase"),
	FOREIGN KEY("CweDetectionMethod_id") REFERENCES "CweDetectionMethod" (id)
);
CREATE INDEX "ix_CweDetectionMethod_Phase_CweDetectionMethod_id" ON "CweDetectionMethod_Phase" ("CweDetectionMethod_id");
CREATE INDEX "ix_CweDetectionMethod_Phase_Phase" ON "CweDetectionMethod_Phase" ("Phase");

CREATE TABLE "CweMitigation_Phase" (
	"CweMitigation_id" INTEGER,
	"Phase" VARCHAR(31),
	PRIMARY KEY ("CweMitigation_id", "Phase"),
	FOREIGN KEY("CweMitigation_id") REFERENCES "CweMitigation" (id)
);
CREATE INDEX "ix_CweMitigation_Phase_Phase" ON "CweMitigation_Phase" ("Phase");
CREATE INDEX "ix_CweMitigation_Phase_CweMitigation_id" ON "CweMitigation_Phase" ("CweMitigation_id");

CREATE TABLE "CweObservedExample_Rationale" (
	"CweObservedExample_id" INTEGER,
	"Rationale" VARCHAR(22),
	PRIMARY KEY ("CweObservedExample_id", "Rationale"),
	FOREIGN KEY("CweObservedExample_id") REFERENCES "CweObservedExample" (id)
);
CREATE INDEX "ix_CweObservedExample_Rationale_CweObservedExample_id" ON "CweObservedExample_Rationale" ("CweObservedExample_id");
CREATE INDEX "ix_CweObservedExample_Rationale_Rationale" ON "CweObservedExample_Rationale" ("Rationale");
