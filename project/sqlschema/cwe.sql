-- # Class: WeaknessCatalog Description: Top-level container for a CWE catalog snapshot (Weakness_Catalog in XSD). Holds weakness entries, categories, views, external references, and NVD weakness observations.
--     * Slot: name Description: Short human-readable name or title for this entity.
--     * Slot: version Description: Version string of the catalog, entry, or submission.
--     * Slot: date Description: Date associated with a catalog snapshot or a name-change event.
-- # Class: Weakness Description: Canonical CWE weakness record (WeaknessType in XSD). Describes a specific type of weakness and the full set of associated information.
--     * Slot: id Description: Unique numeric identifier for the CWE entry, category, or view.
--     * Slot: name Description: Short human-readable name or title for this entity.
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: extended_description Description: Extended description providing additional details beyond the core concept.
--     * Slot: abstraction Description: CWE abstraction tier (e.g. Base or Variant).
--     * Slot: structure Description: Structural nature of the weakness (Simple, Chain, or Composite).
--     * Slot: status Description: Lifecycle status of the CWE entry, category, or view.
--     * Slot: diagram Description: Optional diagram filename or reference associated with the entry.
--     * Slot: likelihood_of_exploit Description: Qualitative likelihood that the weakness can be exploited.
--     * Slot: source Description: Source or origin of the data.
--     * Slot: WeaknessCatalog_name Description: Autocreated FK slot
--     * Slot: applicable_platforms_id Description: Languages, OS, architectures, and technologies where this weakness can appear.
--     * Slot: mapping_notes_id Description: Guidance for when and whether to map an issue to this entry.
--     * Slot: content_history_id Description: Tracks the original author and subsequent modifications.
-- # Class: Category Description: A collection of weaknesses grouped by a shared characteristic (CategoryType in XSD). Organizational mechanism only; not for mapping.
--     * Slot: id Description: Unique numeric identifier for the CWE entry, category, or view.
--     * Slot: name Description: Short human-readable name or title for this entity.
--     * Slot: status Description: Lifecycle status of the CWE entry, category, or view.
--     * Slot: summary Description: Key points that define a category.
--     * Slot: WeaknessCatalog_name Description: Autocreated FK slot
--     * Slot: relationships_id Description: Membership relationships for a CWE category.
--     * Slot: mapping_notes_id Description: Guidance for when and whether to map an issue to this entry.
--     * Slot: content_history_id Description: Tracks the original author and subsequent modifications.
-- # Class: View Description: A perspective from which to look at weaknesses in the catalog (ViewType in XSD). Types: Graph, Explicit slice, Implicit slice.
--     * Slot: id Description: Unique numeric identifier for the CWE entry, category, or view.
--     * Slot: name Description: Short human-readable name or title for this entity.
--     * Slot: type Description: Type of view (Graph, Explicit, or Implicit).
--     * Slot: status Description: Lifecycle status of the CWE entry, category, or view.
--     * Slot: objective Description: Perspective from which a view has been constructed.
--     * Slot: filter Description: XSL query identifying members of an implicit slice view.
--     * Slot: WeaknessCatalog_name Description: Autocreated FK slot
--     * Slot: mapping_notes_id Description: Guidance for when and whether to map an issue to this entry.
--     * Slot: content_history_id Description: Tracks the original author and subsequent modifications.
-- # Class: ExternalReference Description: Pointer to external reading material shared across CWE entries (ExternalReferenceType in XSD). Identified by Reference_ID (e.g. REF-1).
--     * Slot: reference_id Description: Globally unique identifier for an external reference (e.g. REF-1).
--     * Slot: title Description: Descriptive title for a reference or catalog element.
--     * Slot: edition Description: Edition of the material being referenced.
--     * Slot: publication Description: Name of the magazine or journal.
--     * Slot: publication_year Description: Year of publication in YYYY format.
--     * Slot: publication_month Description: Month of publication in --MM format.
--     * Slot: publication_day Description: Day of publication in ---DD format.
--     * Slot: publisher Description: Publisher of the referenced material.
--     * Slot: url Description: URL pointing to the reference resource.
--     * Slot: url_date Description: Date when the URL was last validated to exist.
--     * Slot: WeaknessCatalog_name Description: Autocreated FK slot
-- # Class: CWEReference Description: Link from a CWE entry to an ExternalReference in the catalog (ReferencesType/Reference in XSD).
--     * Slot: id
--     * Slot: external_reference_id Description: Identifier of the ExternalReference being linked to (e.g. REF-1).
--     * Slot: section Description: Section title or page number specific to this use of the reference.
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
--     * Slot: View_id Description: Autocreated FK slot
--     * Slot: DemonstrativeExample_id Description: Autocreated FK slot
-- # Class: RelatedWeakness Description: Typed directional relationship from one CWE entry to another (RelatedWeaknessesType/Related_Weakness in XSD).
--     * Slot: id
--     * Slot: nature Description: Nature of the relationship.
--     * Slot: cwe_id Description: Numeric ID of the target CWE entry.
--     * Slot: view_id Description: View within which this relationship is relevant.
--     * Slot: chain_id Description: ID of a named chain for CanFollow/CanPrecede relationships.
--     * Slot: ordinal Description: Set to "Primary" for the primary ChildOf relationship in the given view.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: WeaknessOrdinality Description: Potential ordering relationship with other weaknesses (WeaknessOrdinalitiesType/Weakness_Ordinality in XSD).
--     * Slot: id
--     * Slot: ordinality Description: Ordinality level (Primary, Resultant, or Indirect).
--     * Slot: description Description: Context in which this ordering relationship exists.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: ApplicablePlatforms Description: Languages, operating systems, architectures, and technologies where a weakness could appear (ApplicablePlatformsType in XSD).
--     * Slot: id
-- # Class: LanguagePlatform Description: A programming language or language class applicable to a weakness with associated prevalence (Language element in ApplicablePlatformsType).
--     * Slot: id
--     * Slot: name Description: Name of the programming language.
--     * Slot: class_ Description: Class of the programming language.
--     * Slot: prevalence Description: Regularity with which this weakness applies to this language.
--     * Slot: ApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: OSPlatform Description: An operating system or OS class applicable to a weakness (Operating_System element in ApplicablePlatformsType).
--     * Slot: id
--     * Slot: name Description: Name of the operating system.
--     * Slot: class_ Description: Class of the operating system.
--     * Slot: version Description: Version of the operating system.
--     * Slot: cpe_id Description: CPE identifier for this operating system.
--     * Slot: prevalence Description: Regularity with which this weakness applies to this OS.
--     * Slot: ApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: ArchitecturePlatform Description: A processor architecture or class applicable to a weakness (Architecture element in ApplicablePlatformsType).
--     * Slot: id
--     * Slot: name Description: Name of the processor architecture.
--     * Slot: class_ Description: Class of the processor architecture.
--     * Slot: prevalence Description: Regularity with which this weakness applies to this architecture.
--     * Slot: ApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: TechnologyPlatform Description: A technology or technology class applicable to a weakness (Technology element in ApplicablePlatformsType).
--     * Slot: id
--     * Slot: name Description: Name of the technology.
--     * Slot: class_ Description: Class of the technology.
--     * Slot: prevalence Description: Regularity with which this weakness applies to this technology.
--     * Slot: ApplicablePlatforms_id Description: Autocreated FK slot
-- # Class: AlternateTerm Description: Another name by which this weakness may be known (AlternateTermsType/Alternate_Term in XSD).
--     * Slot: id
--     * Slot: term Description: An alternate term by which this weakness may be known.
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: ModeOfIntroduction Description: Information about how and when a weakness may be introduced (ModesOfIntroductionType/Introduction in XSD).
--     * Slot: id
--     * Slot: phase Description: Lifecycle phase for introduction or mitigation.
--     * Slot: note Description: Additional contextual note.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: CommonConsequence Description: Individual consequence associated with a weakness (CommonConsequencesType/Consequence in XSD).
--     * Slot: id
--     * Slot: consequence_id Description: Unique identifier for a common consequence (e.g. CC-1).
--     * Slot: likelihood Description: Likelihood of this specific consequence.
--     * Slot: note Description: Additional contextual note.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: DetectionMethod Description: A method that may be employed to detect a weakness, with effectiveness (DetectionMethodsType/Detection_Method in XSD).
--     * Slot: id
--     * Slot: detection_method_id Description: Unique identifier for a detection method entry (e.g. DM-1).
--     * Slot: method Description: Detection method (range narrowed per class via slot_usage).
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: effectiveness Description: Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage).
--     * Slot: effectiveness_notes Description: Strengths and shortcomings of this detection or mitigation.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: PotentialMitigation Description: A potential mitigation for a weakness (PotentialMitigationsType/Mitigation in XSD).
--     * Slot: id
--     * Slot: mitigation_id Description: Unique identifier for a potential mitigation (e.g. MIT-1).
--     * Slot: strategy Description: General protection strategy to which a mitigation contributes.
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: effectiveness Description: Effectiveness level (range narrowed to DetectionEffectiveness or MitigationEffectiveness per class via slot_usage).
--     * Slot: effectiveness_notes Description: Strengths and shortcomings of this detection or mitigation.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: DemonstrativeExample Description: A code example illustrating how a weakness may appear (DemonstrativeExamplesType/Demonstrative_Example in XSD).
--     * Slot: id
--     * Slot: demonstrative_example_id Description: Unique identifier for a demonstrative example (e.g. DX-1).
--     * Slot: title_text Description: Optional title for a demonstrative example.
--     * Slot: intro_text Description: Context and setting for the demonstrative example.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: ExampleCode Description: A structured code snippet within a demonstrative example (StructuredCodeType in XSD).
--     * Slot: id
--     * Slot: nature Description: Nature of the code (Bad, Good, Attack, Mitigation, etc.).
--     * Slot: language Description: Programming language used in this code example.
--     * Slot: content Description: Text content of the code snippet.
--     * Slot: DemonstrativeExample_id Description: Autocreated FK slot
-- # Class: ObservedExample Description: A reference to a real-world instance of a weakness, typically a CVE (ObservedExampleType/Observed_Example in XSD).
--     * Slot: id
--     * Slot: reference Description: Identifier for a real-world example (e.g. CVE-2005-1951).
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: link Description: URL providing more information about the observed example.
--     * Slot: Weakness_id Description: Autocreated FK slot
-- # Class: TaxonomyMapping Description: A mapping from a CWE entry to an equivalent entry in an external taxonomy (TaxonomyMappingsType/Taxonomy_Mapping in XSD).
--     * Slot: id
--     * Slot: taxonomy_name Description: Name of the external taxonomy to which the mapping is made.
--     * Slot: entry_id Description: ID of the entry in the external taxonomy.
--     * Slot: entry_name Description: Name of the entry in the external taxonomy.
--     * Slot: mapping_fit Description: How close the CWE entry is to the mapped taxonomy entry.
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
-- # Class: CatalogMember Description: A Has_Member or Member_Of entry specifying a CWE ID and the View ID in which the membership holds (MemberType in XSD).
--     * Slot: id
--     * Slot: cwe_id Description: Numeric CWE ID (foreign key in relationships and members).
--     * Slot: view_id Description: View ID within which a relationship or membership is relevant.
--     * Slot: View_id Description: Autocreated FK slot
--     * Slot: Relationship_id Description: Autocreated FK slot
-- # Class: Relationship Description: Container for category membership relationships (RelationshipsType in XSD). Holds Has_Member and optionally Member_Of lists.
--     * Slot: id
-- # Class: Audience Description: A target stakeholder group for a CWE view or category (AudienceType/Stakeholder in XSD).
--     * Slot: id
--     * Slot: type Description: Type of stakeholder in the CWE community.
--     * Slot: description Description: Narrative description of the entity.
--     * Slot: View_id Description: Autocreated FK slot
-- # Class: MappingNotes Description: Guidance for when and whether to map an issue to a CWE entry (MappingNotesType in XSD). Required on every Weakness, Category, and View.
--     * Slot: id
--     * Slot: usage Description: Whether this CWE entry is supported for mapping.
--     * Slot: rationale Description: Context for the mapping usage designation.
--     * Slot: comments Description: Further clarification for the mapping notes reader.
-- # Class: MappingSuggestion Description: A suggested alternative CWE entry for mapping purposes (SuggestionsType/Suggestion in XSD).
--     * Slot: id
--     * Slot: cwe_id Description: Numeric CWE ID (foreign key in relationships and members).
--     * Slot: comment Description: Explanatory comment (e.g. on a mapping suggestion).
--     * Slot: MappingNotes_id Description: Autocreated FK slot
-- # Class: Note Description: Additional commentary about a CWE entry (NotesType/Note in XSD).
--     * Slot: id
--     * Slot: type Description: Type of note (Maintenance, Terminology, Research Gap, etc.).
--     * Slot: content Description: Textual content of a note.
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
--     * Slot: View_id Description: Autocreated FK slot
-- # Class: ContentHistory Description: Tracks the original author and subsequent modifications (ContentHistoryType in XSD).
--     * Slot: id
--     * Slot: submission_id Description: Initial submission information for this entry.
-- # Class: Submission Description: Initial submission record for a CWE entry (ContentHistoryType/Submission in XSD).
--     * Slot: id
--     * Slot: submission_name Description: Name of the person who submitted this entry.
--     * Slot: submission_organization Description: Organization of the submitter.
--     * Slot: submission_date Description: Date on which this entry was submitted.
--     * Slot: submission_version Description: CWE version in which this entry was first added.
--     * Slot: submission_release_date Description: Release date of the CWE version that added this entry.
--     * Slot: submission_comment Description: Optional comment related to the submission.
-- # Class: Modification Description: A modification record documenting a change to a CWE entry (ContentHistoryType/Modification in XSD).
--     * Slot: id
--     * Slot: modification_name Description: Name of the person who made the modification.
--     * Slot: modification_organization Description: Organization of the modifier.
--     * Slot: modification_date Description: Date on which the modification was made.
--     * Slot: modification_version Description: CWE version in which the modification first appeared.
--     * Slot: modification_release_date Description: Release date of the CWE version containing the modification.
--     * Slot: modification_importance Description: Importance level of this modification.
--     * Slot: modification_comment Description: Comment describing what was changed.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: Contribution Description: A contribution record documenting donated content or feedback (ContentHistoryType/Contribution in XSD).
--     * Slot: id
--     * Slot: type Description: Whether the contribution was Content or Feedback.
--     * Slot: contribution_name Description: Name of the contributor.
--     * Slot: contribution_organization Description: Organization of the contributor.
--     * Slot: contribution_date Description: Date of the contribution.
--     * Slot: contribution_version Description: CWE version in which the contribution first appeared.
--     * Slot: contribution_release_date Description: Release date of the CWE version containing the contribution.
--     * Slot: contribution_comment Description: Comment related to the contribution.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: PreviousEntryName Description: A previous name used for a CWE entry before a substantive rename (ContentHistoryType/Previous_Entry_Name in XSD).
--     * Slot: id
--     * Slot: name Description: The previous name of this CWE entry.
--     * Slot: date Description: Date on which this name was last used.
--     * Slot: version Description: CWE version in which the name change occurred.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: NVDWeaknessObservation Description: Weakness observation from an NVD vulnerability detail page.
--     * Slot: observation_id Description: Identifier for an NVD weakness observation row.
--     * Slot: observed_in_cve Description: CVE identifier where this weakness observation appears.
--     * Slot: weakness Description: Referenced CWE entry for this observation.
--     * Slot: reported_by Description: Source label for the weakness row (e.g. NIST, ASSIGNER).
--     * Slot: source Description: Source or origin of the data.
--     * Slot: WeaknessCatalog_name Description: Autocreated FK slot
-- # Class: Weakness_background_details
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: background_details Description: Background information relevant but not describing the weakness itself.
-- # Class: Weakness_exploitation_factors
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: exploitation_factors Description: Conditions that could increase the likelihood of exploit.
-- # Class: Weakness_functional_areas
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: functional_areas Description: Functional areas in which this weakness is most likely to occur.
-- # Class: Weakness_affected_resources
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: affected_resources Description: System resources that can be affected by exploiting this weakness.
-- # Class: Weakness_related_attack_patterns
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: related_attack_patterns Description: CAPEC identifiers of attack patterns associated with this weakness.
-- # Class: Weakness_tags
--     * Slot: Weakness_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form tags for grouping and downstream filtering.
-- # Class: ExternalReference_authors
--     * Slot: ExternalReference_reference_id Description: Autocreated FK slot
--     * Slot: authors Description: Authors of the referenced material.
-- # Class: CommonConsequence_scopes
--     * Slot: CommonConsequence_id Description: Autocreated FK slot
--     * Slot: scopes Description: Security properties violated by this consequence.
-- # Class: CommonConsequence_impacts
--     * Slot: CommonConsequence_id Description: Autocreated FK slot
--     * Slot: impacts Description: Technical impacts that arise if the weakness is exploited.
-- # Class: PotentialMitigation_phases
--     * Slot: PotentialMitigation_id Description: Autocreated FK slot
--     * Slot: phases Description: Lifecycle phases during which a mitigation may be applied.
-- # Class: DemonstrativeExample_body_texts
--     * Slot: DemonstrativeExample_id Description: Autocreated FK slot
--     * Slot: body_texts Description: Interleaved body text paragraphs for a demonstrative example.
-- # Class: MappingNotes_reasons
--     * Slot: MappingNotes_id Description: Autocreated FK slot
--     * Slot: reasons Description: Vocabulary summary of the mapping usage recommendation.

CREATE TABLE "WeaknessCatalog" (
	name TEXT NOT NULL,
	version TEXT NOT NULL,
	date DATE NOT NULL,
	PRIMARY KEY (name)
);
CREATE INDEX "ix_WeaknessCatalog_name" ON "WeaknessCatalog" (name);

CREATE TABLE "ApplicablePlatforms" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ApplicablePlatforms_id" ON "ApplicablePlatforms" (id);

CREATE TABLE "Relationship" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);

CREATE TABLE "MappingNotes" (
	id INTEGER NOT NULL,
	usage VARCHAR(19) NOT NULL,
	rationale TEXT NOT NULL,
	comments TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MappingNotes_id" ON "MappingNotes" (id);

CREATE TABLE "Submission" (
	id INTEGER NOT NULL,
	submission_name TEXT,
	submission_organization TEXT,
	submission_date DATE NOT NULL,
	submission_version TEXT NOT NULL,
	submission_release_date DATE NOT NULL,
	submission_comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Submission_id" ON "Submission" (id);

CREATE TABLE "ExternalReference" (
	reference_id TEXT NOT NULL,
	title TEXT NOT NULL,
	edition TEXT,
	publication TEXT,
	publication_year TEXT,
	publication_month TEXT,
	publication_day TEXT,
	publisher TEXT,
	url TEXT,
	url_date DATE,
	"WeaknessCatalog_name" TEXT,
	PRIMARY KEY (reference_id),
	FOREIGN KEY("WeaknessCatalog_name") REFERENCES "WeaknessCatalog" (name)
);
CREATE INDEX "ix_ExternalReference_reference_id" ON "ExternalReference" (reference_id);

CREATE TABLE "LanguagePlatform" (
	id INTEGER NOT NULL,
	name VARCHAR(12),
	class_ VARCHAR(29),
	prevalence VARCHAR(12) NOT NULL,
	"ApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ApplicablePlatforms_id") REFERENCES "ApplicablePlatforms" (id)
);
CREATE INDEX "ix_LanguagePlatform_id" ON "LanguagePlatform" (id);

CREATE TABLE "OSPlatform" (
	id INTEGER NOT NULL,
	name VARCHAR(16),
	class_ VARCHAR(15),
	version TEXT,
	cpe_id TEXT,
	prevalence VARCHAR(12) NOT NULL,
	"ApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ApplicablePlatforms_id") REFERENCES "ApplicablePlatforms" (id)
);
CREATE INDEX "ix_OSPlatform_id" ON "OSPlatform" (id);

CREATE TABLE "ArchitecturePlatform" (
	id INTEGER NOT NULL,
	name VARCHAR(18),
	class_ VARCHAR(25),
	prevalence VARCHAR(12) NOT NULL,
	"ApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ApplicablePlatforms_id") REFERENCES "ApplicablePlatforms" (id)
);
CREATE INDEX "ix_ArchitecturePlatform_id" ON "ArchitecturePlatform" (id);

CREATE TABLE "TechnologyPlatform" (
	id INTEGER NOT NULL,
	name VARCHAR(32),
	class_ VARCHAR(23),
	prevalence VARCHAR(12) NOT NULL,
	"ApplicablePlatforms_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ApplicablePlatforms_id") REFERENCES "ApplicablePlatforms" (id)
);
CREATE INDEX "ix_TechnologyPlatform_id" ON "TechnologyPlatform" (id);

CREATE TABLE "MappingSuggestion" (
	id INTEGER NOT NULL,
	cwe_id INTEGER NOT NULL,
	comment TEXT NOT NULL,
	"MappingNotes_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MappingNotes_id") REFERENCES "MappingNotes" (id)
);
CREATE INDEX "ix_MappingSuggestion_id" ON "MappingSuggestion" (id);

CREATE TABLE "ContentHistory" (
	id INTEGER NOT NULL,
	submission_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(submission_id) REFERENCES "Submission" (id)
);
CREATE INDEX "ix_ContentHistory_id" ON "ContentHistory" (id);

CREATE TABLE "MappingNotes_reasons" (
	"MappingNotes_id" INTEGER,
	reasons VARCHAR(26) NOT NULL,
	PRIMARY KEY ("MappingNotes_id", reasons),
	FOREIGN KEY("MappingNotes_id") REFERENCES "MappingNotes" (id)
);
CREATE INDEX "ix_MappingNotes_reasons_reasons" ON "MappingNotes_reasons" (reasons);
CREATE INDEX "ix_MappingNotes_reasons_MappingNotes_id" ON "MappingNotes_reasons" ("MappingNotes_id");

CREATE TABLE "Weakness" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	extended_description TEXT,
	abstraction VARCHAR(8) NOT NULL,
	structure VARCHAR(9) NOT NULL,
	status VARCHAR(10) NOT NULL,
	diagram TEXT,
	likelihood_of_exploit VARCHAR(7),
	source TEXT,
	"WeaknessCatalog_name" TEXT,
	applicable_platforms_id INTEGER,
	mapping_notes_id INTEGER NOT NULL,
	content_history_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("WeaknessCatalog_name") REFERENCES "WeaknessCatalog" (name),
	FOREIGN KEY(applicable_platforms_id) REFERENCES "ApplicablePlatforms" (id),
	FOREIGN KEY(mapping_notes_id) REFERENCES "MappingNotes" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Weakness_id" ON "Weakness" (id);

CREATE TABLE "Category" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	summary TEXT NOT NULL,
	"WeaknessCatalog_name" TEXT,
	relationships_id INTEGER,
	mapping_notes_id INTEGER NOT NULL,
	content_history_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("WeaknessCatalog_name") REFERENCES "WeaknessCatalog" (name),
	FOREIGN KEY(relationships_id) REFERENCES "Relationship" (id),
	FOREIGN KEY(mapping_notes_id) REFERENCES "MappingNotes" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Category_id" ON "Category" (id);

CREATE TABLE "View" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	type VARCHAR(8) NOT NULL,
	status VARCHAR(10) NOT NULL,
	objective TEXT NOT NULL,
	filter TEXT,
	"WeaknessCatalog_name" TEXT,
	mapping_notes_id INTEGER NOT NULL,
	content_history_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("WeaknessCatalog_name") REFERENCES "WeaknessCatalog" (name),
	FOREIGN KEY(mapping_notes_id) REFERENCES "MappingNotes" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_View_id" ON "View" (id);

CREATE TABLE "Modification" (
	id INTEGER NOT NULL,
	modification_name TEXT,
	modification_organization TEXT,
	modification_date DATE NOT NULL,
	modification_version TEXT,
	modification_release_date DATE,
	modification_importance VARCHAR(8),
	modification_comment TEXT,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Modification_id" ON "Modification" (id);

CREATE TABLE "Contribution" (
	id INTEGER NOT NULL,
	type VARCHAR(8) NOT NULL,
	contribution_name TEXT,
	contribution_organization TEXT,
	contribution_date DATE NOT NULL,
	contribution_version TEXT,
	contribution_release_date DATE,
	contribution_comment TEXT,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Contribution_id" ON "Contribution" (id);

CREATE TABLE "PreviousEntryName" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	date DATE NOT NULL,
	version TEXT,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_PreviousEntryName_id" ON "PreviousEntryName" (id);

CREATE TABLE "ExternalReference_authors" (
	"ExternalReference_reference_id" TEXT,
	authors TEXT,
	PRIMARY KEY ("ExternalReference_reference_id", authors),
	FOREIGN KEY("ExternalReference_reference_id") REFERENCES "ExternalReference" (reference_id)
);
CREATE INDEX "ix_ExternalReference_authors_ExternalReference_reference_id" ON "ExternalReference_authors" ("ExternalReference_reference_id");
CREATE INDEX "ix_ExternalReference_authors_authors" ON "ExternalReference_authors" (authors);

CREATE TABLE "RelatedWeakness" (
	id INTEGER NOT NULL,
	nature VARCHAR(11) NOT NULL,
	cwe_id INTEGER NOT NULL,
	view_id INTEGER NOT NULL,
	chain_id INTEGER,
	ordinal VARCHAR(7),
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_RelatedWeakness_id" ON "RelatedWeakness" (id);

CREATE TABLE "WeaknessOrdinality" (
	id INTEGER NOT NULL,
	ordinality VARCHAR(9) NOT NULL,
	description TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_WeaknessOrdinality_id" ON "WeaknessOrdinality" (id);

CREATE TABLE "AlternateTerm" (
	id INTEGER NOT NULL,
	term TEXT NOT NULL,
	description TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_AlternateTerm_id" ON "AlternateTerm" (id);

CREATE TABLE "ModeOfIntroduction" (
	id INTEGER NOT NULL,
	phase VARCHAR(31) NOT NULL,
	note TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_ModeOfIntroduction_id" ON "ModeOfIntroduction" (id);

CREATE TABLE "CommonConsequence" (
	id INTEGER NOT NULL,
	consequence_id TEXT,
	likelihood VARCHAR(7),
	note TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_CommonConsequence_id" ON "CommonConsequence" (id);

CREATE TABLE "DetectionMethod" (
	id INTEGER NOT NULL,
	detection_method_id TEXT,
	method VARCHAR(54) NOT NULL,
	description TEXT NOT NULL,
	effectiveness VARCHAR(13),
	effectiveness_notes TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_DetectionMethod_id" ON "DetectionMethod" (id);

CREATE TABLE "PotentialMitigation" (
	id INTEGER NOT NULL,
	mitigation_id TEXT,
	strategy VARCHAR(30),
	description TEXT NOT NULL,
	effectiveness VARCHAR(27),
	effectiveness_notes TEXT,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_PotentialMitigation_id" ON "PotentialMitigation" (id);

CREATE TABLE "DemonstrativeExample" (
	id INTEGER NOT NULL,
	demonstrative_example_id TEXT,
	title_text TEXT,
	intro_text TEXT NOT NULL,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_DemonstrativeExample_id" ON "DemonstrativeExample" (id);

CREATE TABLE "ObservedExample" (
	id INTEGER NOT NULL,
	reference TEXT NOT NULL,
	description TEXT NOT NULL,
	link TEXT NOT NULL,
	"Weakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_ObservedExample_id" ON "ObservedExample" (id);

CREATE TABLE "TaxonomyMapping" (
	id INTEGER NOT NULL,
	taxonomy_name VARCHAR(52) NOT NULL,
	entry_id TEXT,
	entry_name TEXT,
	mapping_fit VARCHAR(17),
	"Weakness_id" INTEGER,
	"Category_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id)
);
CREATE INDEX "ix_TaxonomyMapping_id" ON "TaxonomyMapping" (id);

CREATE TABLE "CatalogMember" (
	id INTEGER NOT NULL,
	cwe_id INTEGER NOT NULL,
	view_id INTEGER NOT NULL,
	"View_id" INTEGER,
	"Relationship_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id)
);
CREATE INDEX "ix_CatalogMember_id" ON "CatalogMember" (id);

CREATE TABLE "Audience" (
	id INTEGER NOT NULL,
	type VARCHAR(23) NOT NULL,
	description TEXT,
	"View_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id)
);
CREATE INDEX "ix_Audience_id" ON "Audience" (id);

CREATE TABLE "Note" (
	id INTEGER NOT NULL,
	type VARCHAR(19) NOT NULL,
	content TEXT,
	"Weakness_id" INTEGER,
	"Category_id" INTEGER,
	"View_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id)
);
CREATE INDEX "ix_Note_id" ON "Note" (id);

CREATE TABLE "NVDWeaknessObservation" (
	observation_id TEXT NOT NULL,
	observed_in_cve TEXT NOT NULL,
	weakness INTEGER NOT NULL,
	reported_by VARCHAR(8) NOT NULL,
	source TEXT,
	"WeaknessCatalog_name" TEXT,
	PRIMARY KEY (observation_id),
	FOREIGN KEY(weakness) REFERENCES "Weakness" (id),
	FOREIGN KEY("WeaknessCatalog_name") REFERENCES "WeaknessCatalog" (name)
);
CREATE INDEX "ix_NVDWeaknessObservation_observation_id" ON "NVDWeaknessObservation" (observation_id);

CREATE TABLE "Weakness_background_details" (
	"Weakness_id" INTEGER,
	background_details TEXT,
	PRIMARY KEY ("Weakness_id", background_details),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_background_details_background_details" ON "Weakness_background_details" (background_details);
CREATE INDEX "ix_Weakness_background_details_Weakness_id" ON "Weakness_background_details" ("Weakness_id");

CREATE TABLE "Weakness_exploitation_factors" (
	"Weakness_id" INTEGER,
	exploitation_factors TEXT,
	PRIMARY KEY ("Weakness_id", exploitation_factors),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_exploitation_factors_Weakness_id" ON "Weakness_exploitation_factors" ("Weakness_id");
CREATE INDEX "ix_Weakness_exploitation_factors_exploitation_factors" ON "Weakness_exploitation_factors" (exploitation_factors);

CREATE TABLE "Weakness_functional_areas" (
	"Weakness_id" INTEGER,
	functional_areas VARCHAR(28),
	PRIMARY KEY ("Weakness_id", functional_areas),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_functional_areas_functional_areas" ON "Weakness_functional_areas" (functional_areas);
CREATE INDEX "ix_Weakness_functional_areas_Weakness_id" ON "Weakness_functional_areas" ("Weakness_id");

CREATE TABLE "Weakness_affected_resources" (
	"Weakness_id" INTEGER,
	affected_resources VARCHAR(17),
	PRIMARY KEY ("Weakness_id", affected_resources),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_affected_resources_affected_resources" ON "Weakness_affected_resources" (affected_resources);
CREATE INDEX "ix_Weakness_affected_resources_Weakness_id" ON "Weakness_affected_resources" ("Weakness_id");

CREATE TABLE "Weakness_related_attack_patterns" (
	"Weakness_id" INTEGER,
	related_attack_patterns INTEGER,
	PRIMARY KEY ("Weakness_id", related_attack_patterns),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_related_attack_patterns_related_attack_patterns" ON "Weakness_related_attack_patterns" (related_attack_patterns);
CREATE INDEX "ix_Weakness_related_attack_patterns_Weakness_id" ON "Weakness_related_attack_patterns" ("Weakness_id");

CREATE TABLE "Weakness_tags" (
	"Weakness_id" INTEGER,
	tags TEXT,
	PRIMARY KEY ("Weakness_id", tags),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id)
);
CREATE INDEX "ix_Weakness_tags_Weakness_id" ON "Weakness_tags" ("Weakness_id");
CREATE INDEX "ix_Weakness_tags_tags" ON "Weakness_tags" (tags);

CREATE TABLE "CWEReference" (
	id INTEGER NOT NULL,
	external_reference_id TEXT NOT NULL,
	section TEXT,
	"Weakness_id" INTEGER,
	"Category_id" INTEGER,
	"View_id" INTEGER,
	"DemonstrativeExample_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Weakness_id") REFERENCES "Weakness" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id),
	FOREIGN KEY("DemonstrativeExample_id") REFERENCES "DemonstrativeExample" (id)
);
CREATE INDEX "ix_CWEReference_id" ON "CWEReference" (id);

CREATE TABLE "ExampleCode" (
	id INTEGER NOT NULL,
	nature VARCHAR(11) NOT NULL,
	language VARCHAR(12),
	content TEXT,
	"DemonstrativeExample_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("DemonstrativeExample_id") REFERENCES "DemonstrativeExample" (id)
);
CREATE INDEX "ix_ExampleCode_id" ON "ExampleCode" (id);

CREATE TABLE "CommonConsequence_scopes" (
	"CommonConsequence_id" INTEGER,
	scopes VARCHAR(15) NOT NULL,
	PRIMARY KEY ("CommonConsequence_id", scopes),
	FOREIGN KEY("CommonConsequence_id") REFERENCES "CommonConsequence" (id)
);
CREATE INDEX "ix_CommonConsequence_scopes_scopes" ON "CommonConsequence_scopes" (scopes);
CREATE INDEX "ix_CommonConsequence_scopes_CommonConsequence_id" ON "CommonConsequence_scopes" ("CommonConsequence_id");

CREATE TABLE "CommonConsequence_impacts" (
	"CommonConsequence_id" INTEGER,
	impacts VARCHAR(37) NOT NULL,
	PRIMARY KEY ("CommonConsequence_id", impacts),
	FOREIGN KEY("CommonConsequence_id") REFERENCES "CommonConsequence" (id)
);
CREATE INDEX "ix_CommonConsequence_impacts_CommonConsequence_id" ON "CommonConsequence_impacts" ("CommonConsequence_id");
CREATE INDEX "ix_CommonConsequence_impacts_impacts" ON "CommonConsequence_impacts" (impacts);

CREATE TABLE "PotentialMitigation_phases" (
	"PotentialMitigation_id" INTEGER,
	phases VARCHAR(31),
	PRIMARY KEY ("PotentialMitigation_id", phases),
	FOREIGN KEY("PotentialMitigation_id") REFERENCES "PotentialMitigation" (id)
);
CREATE INDEX "ix_PotentialMitigation_phases_PotentialMitigation_id" ON "PotentialMitigation_phases" ("PotentialMitigation_id");
CREATE INDEX "ix_PotentialMitigation_phases_phases" ON "PotentialMitigation_phases" (phases);

CREATE TABLE "DemonstrativeExample_body_texts" (
	"DemonstrativeExample_id" INTEGER,
	body_texts TEXT,
	PRIMARY KEY ("DemonstrativeExample_id", body_texts),
	FOREIGN KEY("DemonstrativeExample_id") REFERENCES "DemonstrativeExample" (id)
);
CREATE INDEX "ix_DemonstrativeExample_body_texts_body_texts" ON "DemonstrativeExample_body_texts" (body_texts);
CREATE INDEX "ix_DemonstrativeExample_body_texts_DemonstrativeExample_id" ON "DemonstrativeExample_body_texts" ("DemonstrativeExample_id");
