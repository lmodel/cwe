# Auto generated from cwe.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-07T15:07:42
# Schema: cwe
#
# id: https://w3id.org/lmodel/cwe
# description: MITRE Common Weakness Enumeration (CWE) LinkML Schema.
#
#   Self-contained schema covering the full MITRE CWE XSD: weakness entries,
#   categories, views, external references, and NVD weakness observations (CWE-ID,
#   CWE Name, Source).
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

metamodel_version = "1.7.0"
version = "7.3"

# Namespaces
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
CAPEC = CurieNamespace('capec', 'https://w3id.org/lmodel/capec/')
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
CWE = CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CWE


# Types
class CveId(str):
    """ A CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CveId"
    type_model_uri = CWE.CveId


# Class references
class WeaknessCatalogName(extended_str):
    pass


class WeaknessId(extended_int):
    pass


class CategoryId(extended_int):
    pass


class ViewId(extended_int):
    pass


class ExternalReferenceReferenceId(extended_str):
    pass


class NVDWeaknessObservationObservationId(extended_str):
    pass


@dataclass(repr=False)
class WeaknessCatalog(YAMLRoot):
    """
    Top-level container for a CWE catalog snapshot (Weakness_Catalog in XSD). Holds weakness entries, categories,
    views, external references, and NVD weakness observations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["WeaknessCatalog"]
    class_class_curie: ClassVar[str] = "cwe:WeaknessCatalog"
    class_name: ClassVar[str] = "WeaknessCatalog"
    class_model_uri: ClassVar[URIRef] = CWE.WeaknessCatalog

    name: Union[str, WeaknessCatalogName] = None
    version: str = None
    date: Union[str, XSDDate] = None
    weaknesses: Optional[Union[dict[Union[int, WeaknessId], Union[dict, "Weakness"]], list[Union[dict, "Weakness"]]]] = empty_dict()
    categories: Optional[Union[dict[Union[int, CategoryId], Union[dict, "Category"]], list[Union[dict, "Category"]]]] = empty_dict()
    views: Optional[Union[dict[Union[int, ViewId], Union[dict, "View"]], list[Union[dict, "View"]]]] = empty_dict()
    external_references: Optional[Union[dict[Union[str, ExternalReferenceReferenceId], Union[dict, "ExternalReference"]], list[Union[dict, "ExternalReference"]]]] = empty_dict()
    observations: Optional[Union[dict[Union[str, NVDWeaknessObservationObservationId], Union[dict, "NVDWeaknessObservation"]], list[Union[dict, "NVDWeaknessObservation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, WeaknessCatalogName):
            self.name = WeaknessCatalogName(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        self._normalize_inlined_as_list(slot_name="weaknesses", slot_type=Weakness, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="categories", slot_type=Category, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="views", slot_type=View, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="reference_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=NVDWeaknessObservation, key_name="observation_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Weakness(YAMLRoot):
    """
    Canonical CWE weakness record (WeaknessType in XSD). Describes a specific type of weakness and the full set of
    associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Weakness"]
    class_class_curie: ClassVar[str] = "cwe:Weakness"
    class_name: ClassVar[str] = "Weakness"
    class_model_uri: ClassVar[URIRef] = CWE.Weakness

    id: Union[int, WeaknessId] = None
    name: str = None
    description: str = None
    abstraction: Union[str, "WeaknessAbstraction"] = None
    structure: Union[str, "WeaknessStructure"] = None
    status: Union[str, "WeaknessStatus"] = None
    mapping_notes: Union[dict, "MappingNotes"] = None
    content_history: Union[dict, "ContentHistory"] = None
    extended_description: Optional[str] = None
    diagram: Optional[str] = None
    weakness_ordinalities: Optional[Union[Union[dict, "WeaknessOrdinality"], list[Union[dict, "WeaknessOrdinality"]]]] = empty_list()
    applicable_platforms: Optional[Union[dict, "ApplicablePlatforms"]] = None
    background_details: Optional[Union[str, list[str]]] = empty_list()
    alternate_terms: Optional[Union[Union[dict, "AlternateTerm"], list[Union[dict, "AlternateTerm"]]]] = empty_list()
    modes_of_introduction: Optional[Union[Union[dict, "ModeOfIntroduction"], list[Union[dict, "ModeOfIntroduction"]]]] = empty_list()
    exploitation_factors: Optional[Union[str, list[str]]] = empty_list()
    likelihood_of_exploit: Optional[Union[str, "LikelihoodLevel"]] = None
    common_consequences: Optional[Union[Union[dict, "CommonConsequence"], list[Union[dict, "CommonConsequence"]]]] = empty_list()
    detection_methods: Optional[Union[Union[dict, "DetectionMethod"], list[Union[dict, "DetectionMethod"]]]] = empty_list()
    potential_mitigations: Optional[Union[Union[dict, "PotentialMitigation"], list[Union[dict, "PotentialMitigation"]]]] = empty_list()
    demonstrative_examples: Optional[Union[Union[dict, "DemonstrativeExample"], list[Union[dict, "DemonstrativeExample"]]]] = empty_list()
    observed_examples: Optional[Union[Union[dict, "ObservedExample"], list[Union[dict, "ObservedExample"]]]] = empty_list()
    functional_areas: Optional[Union[Union[str, "FunctionalArea"], list[Union[str, "FunctionalArea"]]]] = empty_list()
    affected_resources: Optional[Union[Union[str, "AffectedResource"], list[Union[str, "AffectedResource"]]]] = empty_list()
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()
    related_attack_patterns: Optional[Union[int, list[int]]] = empty_list()
    related_weaknesses: Optional[Union[Union[dict, "RelatedWeakness"], list[Union[dict, "RelatedWeakness"]]]] = empty_list()
    references: Optional[Union[Union[dict, "CWEReference"], list[Union[dict, "CWEReference"]]]] = empty_list()
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()
    tags: Optional[Union[str, list[str]]] = empty_list()
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WeaknessId):
            self.id = WeaknessId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.abstraction):
            self.MissingRequiredField("abstraction")
        if not isinstance(self.abstraction, WeaknessAbstraction):
            self.abstraction = WeaknessAbstraction(self.abstraction)

        if self._is_empty(self.structure):
            self.MissingRequiredField("structure")
        if not isinstance(self.structure, WeaknessStructure):
            self.structure = WeaknessStructure(self.structure)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, WeaknessStatus):
            self.status = WeaknessStatus(self.status)

        if self._is_empty(self.mapping_notes):
            self.MissingRequiredField("mapping_notes")
        if not isinstance(self.mapping_notes, MappingNotes):
            self.mapping_notes = MappingNotes(**as_dict(self.mapping_notes))

        if self._is_empty(self.content_history):
            self.MissingRequiredField("content_history")
        if not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        if self.extended_description is not None and not isinstance(self.extended_description, str):
            self.extended_description = str(self.extended_description)

        if self.diagram is not None and not isinstance(self.diagram, str):
            self.diagram = str(self.diagram)

        if not isinstance(self.weakness_ordinalities, list):
            self.weakness_ordinalities = [self.weakness_ordinalities] if self.weakness_ordinalities is not None else []
        self.weakness_ordinalities = [v if isinstance(v, WeaknessOrdinality) else WeaknessOrdinality(**as_dict(v)) for v in self.weakness_ordinalities]

        if self.applicable_platforms is not None and not isinstance(self.applicable_platforms, ApplicablePlatforms):
            self.applicable_platforms = ApplicablePlatforms(**as_dict(self.applicable_platforms))

        if not isinstance(self.background_details, list):
            self.background_details = [self.background_details] if self.background_details is not None else []
        self.background_details = [v if isinstance(v, str) else str(v) for v in self.background_details]

        if not isinstance(self.alternate_terms, list):
            self.alternate_terms = [self.alternate_terms] if self.alternate_terms is not None else []
        self.alternate_terms = [v if isinstance(v, AlternateTerm) else AlternateTerm(**as_dict(v)) for v in self.alternate_terms]

        if not isinstance(self.modes_of_introduction, list):
            self.modes_of_introduction = [self.modes_of_introduction] if self.modes_of_introduction is not None else []
        self.modes_of_introduction = [v if isinstance(v, ModeOfIntroduction) else ModeOfIntroduction(**as_dict(v)) for v in self.modes_of_introduction]

        if not isinstance(self.exploitation_factors, list):
            self.exploitation_factors = [self.exploitation_factors] if self.exploitation_factors is not None else []
        self.exploitation_factors = [v if isinstance(v, str) else str(v) for v in self.exploitation_factors]

        if self.likelihood_of_exploit is not None and not isinstance(self.likelihood_of_exploit, LikelihoodLevel):
            self.likelihood_of_exploit = LikelihoodLevel(self.likelihood_of_exploit)

        if not isinstance(self.common_consequences, list):
            self.common_consequences = [self.common_consequences] if self.common_consequences is not None else []
        self.common_consequences = [v if isinstance(v, CommonConsequence) else CommonConsequence(**as_dict(v)) for v in self.common_consequences]

        if not isinstance(self.detection_methods, list):
            self.detection_methods = [self.detection_methods] if self.detection_methods is not None else []
        self.detection_methods = [v if isinstance(v, DetectionMethod) else DetectionMethod(**as_dict(v)) for v in self.detection_methods]

        if not isinstance(self.potential_mitigations, list):
            self.potential_mitigations = [self.potential_mitigations] if self.potential_mitigations is not None else []
        self.potential_mitigations = [v if isinstance(v, PotentialMitigation) else PotentialMitigation(**as_dict(v)) for v in self.potential_mitigations]

        if not isinstance(self.demonstrative_examples, list):
            self.demonstrative_examples = [self.demonstrative_examples] if self.demonstrative_examples is not None else []
        self.demonstrative_examples = [v if isinstance(v, DemonstrativeExample) else DemonstrativeExample(**as_dict(v)) for v in self.demonstrative_examples]

        if not isinstance(self.observed_examples, list):
            self.observed_examples = [self.observed_examples] if self.observed_examples is not None else []
        self.observed_examples = [v if isinstance(v, ObservedExample) else ObservedExample(**as_dict(v)) for v in self.observed_examples]

        if not isinstance(self.functional_areas, list):
            self.functional_areas = [self.functional_areas] if self.functional_areas is not None else []
        self.functional_areas = [v if isinstance(v, FunctionalArea) else FunctionalArea(v) for v in self.functional_areas]

        if not isinstance(self.affected_resources, list):
            self.affected_resources = [self.affected_resources] if self.affected_resources is not None else []
        self.affected_resources = [v if isinstance(v, AffectedResource) else AffectedResource(v) for v in self.affected_resources]

        if not isinstance(self.taxonomy_mappings, list):
            self.taxonomy_mappings = [self.taxonomy_mappings] if self.taxonomy_mappings is not None else []
        self.taxonomy_mappings = [v if isinstance(v, TaxonomyMapping) else TaxonomyMapping(**as_dict(v)) for v in self.taxonomy_mappings]

        if not isinstance(self.related_attack_patterns, list):
            self.related_attack_patterns = [self.related_attack_patterns] if self.related_attack_patterns is not None else []
        self.related_attack_patterns = [v if isinstance(v, int) else int(v) for v in self.related_attack_patterns]

        if not isinstance(self.related_weaknesses, list):
            self.related_weaknesses = [self.related_weaknesses] if self.related_weaknesses is not None else []
        self.related_weaknesses = [v if isinstance(v, RelatedWeakness) else RelatedWeakness(**as_dict(v)) for v in self.related_weaknesses]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, CWEReference) else CWEReference(**as_dict(v)) for v in self.references]

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, Note) else Note(**as_dict(v)) for v in self.notes]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Category(YAMLRoot):
    """
    A collection of weaknesses grouped by a shared characteristic (CategoryType in XSD). Organizational mechanism
    only; not for mapping.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Category"]
    class_class_curie: ClassVar[str] = "cwe:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = CWE.Category

    id: Union[int, CategoryId] = None
    name: str = None
    status: Union[str, "WeaknessStatus"] = None
    summary: str = None
    mapping_notes: Union[dict, "MappingNotes"] = None
    content_history: Union[dict, "ContentHistory"] = None
    relationships: Optional[Union[dict, "Relationship"]] = None
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()
    references: Optional[Union[Union[dict, "CWEReference"], list[Union[dict, "CWEReference"]]]] = empty_list()
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CategoryId):
            self.id = CategoryId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, WeaknessStatus):
            self.status = WeaknessStatus(self.status)

        if self._is_empty(self.summary):
            self.MissingRequiredField("summary")
        if not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self._is_empty(self.mapping_notes):
            self.MissingRequiredField("mapping_notes")
        if not isinstance(self.mapping_notes, MappingNotes):
            self.mapping_notes = MappingNotes(**as_dict(self.mapping_notes))

        if self._is_empty(self.content_history):
            self.MissingRequiredField("content_history")
        if not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        if self.relationships is not None and not isinstance(self.relationships, Relationship):
            self.relationships = Relationship(**as_dict(self.relationships))

        if not isinstance(self.taxonomy_mappings, list):
            self.taxonomy_mappings = [self.taxonomy_mappings] if self.taxonomy_mappings is not None else []
        self.taxonomy_mappings = [v if isinstance(v, TaxonomyMapping) else TaxonomyMapping(**as_dict(v)) for v in self.taxonomy_mappings]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, CWEReference) else CWEReference(**as_dict(v)) for v in self.references]

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, Note) else Note(**as_dict(v)) for v in self.notes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class View(YAMLRoot):
    """
    A perspective from which to look at weaknesses in the catalog (ViewType in XSD). Types: Graph, Explicit slice,
    Implicit slice.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["View"]
    class_class_curie: ClassVar[str] = "cwe:View"
    class_name: ClassVar[str] = "View"
    class_model_uri: ClassVar[URIRef] = CWE.View

    id: Union[int, ViewId] = None
    name: str = None
    type: Union[str, "CWEViewType"] = None
    status: Union[str, "WeaknessStatus"] = None
    objective: str = None
    mapping_notes: Union[dict, "MappingNotes"] = None
    content_history: Union[dict, "ContentHistory"] = None
    audience: Optional[Union[Union[dict, "Audience"], list[Union[dict, "Audience"]]]] = empty_list()
    members: Optional[Union[Union[dict, "CatalogMember"], list[Union[dict, "CatalogMember"]]]] = empty_list()
    filter: Optional[str] = None
    references: Optional[Union[Union[dict, "CWEReference"], list[Union[dict, "CWEReference"]]]] = empty_list()
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ViewId):
            self.id = ViewId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, CWEViewType):
            self.type = CWEViewType(self.type)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, WeaknessStatus):
            self.status = WeaknessStatus(self.status)

        if self._is_empty(self.objective):
            self.MissingRequiredField("objective")
        if not isinstance(self.objective, str):
            self.objective = str(self.objective)

        if self._is_empty(self.mapping_notes):
            self.MissingRequiredField("mapping_notes")
        if not isinstance(self.mapping_notes, MappingNotes):
            self.mapping_notes = MappingNotes(**as_dict(self.mapping_notes))

        if self._is_empty(self.content_history):
            self.MissingRequiredField("content_history")
        if not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        if not isinstance(self.audience, list):
            self.audience = [self.audience] if self.audience is not None else []
        self.audience = [v if isinstance(v, Audience) else Audience(**as_dict(v)) for v in self.audience]

        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, CatalogMember) else CatalogMember(**as_dict(v)) for v in self.members]

        if self.filter is not None and not isinstance(self.filter, str):
            self.filter = str(self.filter)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, CWEReference) else CWEReference(**as_dict(v)) for v in self.references]

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, Note) else Note(**as_dict(v)) for v in self.notes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalReference(YAMLRoot):
    """
    Pointer to external reading material shared across CWE entries (ExternalReferenceType in XSD). Identified by
    Reference_ID (e.g. REF-1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ExternalReference"]
    class_class_curie: ClassVar[str] = "cwe:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = CWE.ExternalReference

    reference_id: Union[str, ExternalReferenceReferenceId] = None
    title: str = None
    authors: Optional[Union[str, list[str]]] = empty_list()
    edition: Optional[str] = None
    publication: Optional[str] = None
    publication_year: Optional[str] = None
    publication_month: Optional[str] = None
    publication_day: Optional[str] = None
    publisher: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    url_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, ExternalReferenceReferenceId):
            self.reference_id = ExternalReferenceReferenceId(self.reference_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.edition is not None and not isinstance(self.edition, str):
            self.edition = str(self.edition)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if self.publication_year is not None and not isinstance(self.publication_year, str):
            self.publication_year = str(self.publication_year)

        if self.publication_month is not None and not isinstance(self.publication_month, str):
            self.publication_month = str(self.publication_month)

        if self.publication_day is not None and not isinstance(self.publication_day, str):
            self.publication_day = str(self.publication_day)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.url_date is not None and not isinstance(self.url_date, XSDDate):
            self.url_date = XSDDate(self.url_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CWEReference(YAMLRoot):
    """
    Link from a CWE entry to an ExternalReference in the catalog (ReferencesType/Reference in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CWEReference"]
    class_class_curie: ClassVar[str] = "cwe:CWEReference"
    class_name: ClassVar[str] = "CWEReference"
    class_model_uri: ClassVar[URIRef] = CWE.CWEReference

    external_reference_id: str = None
    section: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.external_reference_id):
            self.MissingRequiredField("external_reference_id")
        if not isinstance(self.external_reference_id, str):
            self.external_reference_id = str(self.external_reference_id)

        if self.section is not None and not isinstance(self.section, str):
            self.section = str(self.section)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedWeakness(YAMLRoot):
    """
    Typed directional relationship from one CWE entry to another (RelatedWeaknessesType/Related_Weakness in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["RelatedWeakness"]
    class_class_curie: ClassVar[str] = "cwe:RelatedWeakness"
    class_name: ClassVar[str] = "RelatedWeakness"
    class_model_uri: ClassVar[URIRef] = CWE.RelatedWeakness

    nature: Union[str, "WeaknessRelationNature"] = None
    cwe_id: int = None
    view_id: int = None
    chain_id: Optional[int] = None
    ordinal: Optional[Union[str, "OrdinalQualifier"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.nature):
            self.MissingRequiredField("nature")
        if not isinstance(self.nature, WeaknessRelationNature):
            self.nature = WeaknessRelationNature(self.nature)

        if self._is_empty(self.cwe_id):
            self.MissingRequiredField("cwe_id")
        if not isinstance(self.cwe_id, int):
            self.cwe_id = int(self.cwe_id)

        if self._is_empty(self.view_id):
            self.MissingRequiredField("view_id")
        if not isinstance(self.view_id, int):
            self.view_id = int(self.view_id)

        if self.chain_id is not None and not isinstance(self.chain_id, int):
            self.chain_id = int(self.chain_id)

        if self.ordinal is not None and not isinstance(self.ordinal, OrdinalQualifier):
            self.ordinal = OrdinalQualifier(self.ordinal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WeaknessOrdinality(YAMLRoot):
    """
    Potential ordering relationship with other weaknesses (WeaknessOrdinalitiesType/Weakness_Ordinality in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["WeaknessOrdinality"]
    class_class_curie: ClassVar[str] = "cwe:WeaknessOrdinality"
    class_name: ClassVar[str] = "WeaknessOrdinality"
    class_model_uri: ClassVar[URIRef] = CWE.WeaknessOrdinality

    ordinality: Union[str, "WeaknessOrdinalityLevel"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ordinality):
            self.MissingRequiredField("ordinality")
        if not isinstance(self.ordinality, WeaknessOrdinalityLevel):
            self.ordinality = WeaknessOrdinalityLevel(self.ordinality)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApplicablePlatforms(YAMLRoot):
    """
    Languages, operating systems, architectures, and technologies where a weakness could appear
    (ApplicablePlatformsType in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ApplicablePlatforms"]
    class_class_curie: ClassVar[str] = "cwe:ApplicablePlatforms"
    class_name: ClassVar[str] = "ApplicablePlatforms"
    class_model_uri: ClassVar[URIRef] = CWE.ApplicablePlatforms

    languages: Optional[Union[Union[dict, "LanguagePlatform"], list[Union[dict, "LanguagePlatform"]]]] = empty_list()
    operating_systems: Optional[Union[Union[dict, "OSPlatform"], list[Union[dict, "OSPlatform"]]]] = empty_list()
    architectures: Optional[Union[Union[dict, "ArchitecturePlatform"], list[Union[dict, "ArchitecturePlatform"]]]] = empty_list()
    technologies: Optional[Union[Union[dict, "TechnologyPlatform"], list[Union[dict, "TechnologyPlatform"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.languages, list):
            self.languages = [self.languages] if self.languages is not None else []
        self.languages = [v if isinstance(v, LanguagePlatform) else LanguagePlatform(**as_dict(v)) for v in self.languages]

        if not isinstance(self.operating_systems, list):
            self.operating_systems = [self.operating_systems] if self.operating_systems is not None else []
        self.operating_systems = [v if isinstance(v, OSPlatform) else OSPlatform(**as_dict(v)) for v in self.operating_systems]

        if not isinstance(self.architectures, list):
            self.architectures = [self.architectures] if self.architectures is not None else []
        self.architectures = [v if isinstance(v, ArchitecturePlatform) else ArchitecturePlatform(**as_dict(v)) for v in self.architectures]

        if not isinstance(self.technologies, list):
            self.technologies = [self.technologies] if self.technologies is not None else []
        self.technologies = [v if isinstance(v, TechnologyPlatform) else TechnologyPlatform(**as_dict(v)) for v in self.technologies]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LanguagePlatform(YAMLRoot):
    """
    A programming language or language class applicable to a weakness with associated prevalence (Language element in
    ApplicablePlatformsType).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["LanguagePlatform"]
    class_class_curie: ClassVar[str] = "cwe:LanguagePlatform"
    class_name: ClassVar[str] = "LanguagePlatform"
    class_model_uri: ClassVar[URIRef] = CWE.LanguagePlatform

    prevalence: Union[str, "PlatformPrevalence"] = None
    name: Optional[Union[str, "ProgrammingLanguage"]] = None
    class_: Optional[Union[str, "LanguageClass"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prevalence):
            self.MissingRequiredField("prevalence")
        if not isinstance(self.prevalence, PlatformPrevalence):
            self.prevalence = PlatformPrevalence(self.prevalence)

        if self.name is not None and not isinstance(self.name, ProgrammingLanguage):
            self.name = ProgrammingLanguage(self.name)

        if self.class_ is not None and not isinstance(self.class_, LanguageClass):
            self.class_ = LanguageClass(self.class_)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OSPlatform(YAMLRoot):
    """
    An operating system or OS class applicable to a weakness (Operating_System element in ApplicablePlatformsType).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["OSPlatform"]
    class_class_curie: ClassVar[str] = "cwe:OSPlatform"
    class_name: ClassVar[str] = "OSPlatform"
    class_model_uri: ClassVar[URIRef] = CWE.OSPlatform

    prevalence: Union[str, "PlatformPrevalence"] = None
    name: Optional[Union[str, "OperatingSystemName"]] = None
    class_: Optional[Union[str, "OperatingSystemClass"]] = None
    version: Optional[str] = None
    cpe_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prevalence):
            self.MissingRequiredField("prevalence")
        if not isinstance(self.prevalence, PlatformPrevalence):
            self.prevalence = PlatformPrevalence(self.prevalence)

        if self.name is not None and not isinstance(self.name, OperatingSystemName):
            self.name = OperatingSystemName(self.name)

        if self.class_ is not None and not isinstance(self.class_, OperatingSystemClass):
            self.class_ = OperatingSystemClass(self.class_)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.cpe_id is not None and not isinstance(self.cpe_id, str):
            self.cpe_id = str(self.cpe_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ArchitecturePlatform(YAMLRoot):
    """
    A processor architecture or class applicable to a weakness (Architecture element in ApplicablePlatformsType).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ArchitecturePlatform"]
    class_class_curie: ClassVar[str] = "cwe:ArchitecturePlatform"
    class_name: ClassVar[str] = "ArchitecturePlatform"
    class_model_uri: ClassVar[URIRef] = CWE.ArchitecturePlatform

    prevalence: Union[str, "PlatformPrevalence"] = None
    name: Optional[Union[str, "ArchitectureName"]] = None
    class_: Optional[Union[str, "ArchitectureClass"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prevalence):
            self.MissingRequiredField("prevalence")
        if not isinstance(self.prevalence, PlatformPrevalence):
            self.prevalence = PlatformPrevalence(self.prevalence)

        if self.name is not None and not isinstance(self.name, ArchitectureName):
            self.name = ArchitectureName(self.name)

        if self.class_ is not None and not isinstance(self.class_, ArchitectureClass):
            self.class_ = ArchitectureClass(self.class_)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnologyPlatform(YAMLRoot):
    """
    A technology or technology class applicable to a weakness (Technology element in ApplicablePlatformsType).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["TechnologyPlatform"]
    class_class_curie: ClassVar[str] = "cwe:TechnologyPlatform"
    class_name: ClassVar[str] = "TechnologyPlatform"
    class_model_uri: ClassVar[URIRef] = CWE.TechnologyPlatform

    prevalence: Union[str, "PlatformPrevalence"] = None
    name: Optional[Union[str, "TechnologyName"]] = None
    class_: Optional[Union[str, "TechnologyClass"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prevalence):
            self.MissingRequiredField("prevalence")
        if not isinstance(self.prevalence, PlatformPrevalence):
            self.prevalence = PlatformPrevalence(self.prevalence)

        if self.name is not None and not isinstance(self.name, TechnologyName):
            self.name = TechnologyName(self.name)

        if self.class_ is not None and not isinstance(self.class_, TechnologyClass):
            self.class_ = TechnologyClass(self.class_)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternateTerm(YAMLRoot):
    """
    Another name by which this weakness may be known (AlternateTermsType/Alternate_Term in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["AlternateTerm"]
    class_class_curie: ClassVar[str] = "cwe:AlternateTerm"
    class_name: ClassVar[str] = "AlternateTerm"
    class_model_uri: ClassVar[URIRef] = CWE.AlternateTerm

    term: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, str):
            self.term = str(self.term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModeOfIntroduction(YAMLRoot):
    """
    Information about how and when a weakness may be introduced (ModesOfIntroductionType/Introduction in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ModeOfIntroduction"]
    class_class_curie: ClassVar[str] = "cwe:ModeOfIntroduction"
    class_name: ClassVar[str] = "ModeOfIntroduction"
    class_model_uri: ClassVar[URIRef] = CWE.ModeOfIntroduction

    phase: Union[str, "LifecyclePhase"] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.phase):
            self.MissingRequiredField("phase")
        if not isinstance(self.phase, LifecyclePhase):
            self.phase = LifecyclePhase(self.phase)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonConsequence(YAMLRoot):
    """
    Individual consequence associated with a weakness (CommonConsequencesType/Consequence in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CommonConsequence"]
    class_class_curie: ClassVar[str] = "cwe:CommonConsequence"
    class_name: ClassVar[str] = "CommonConsequence"
    class_model_uri: ClassVar[URIRef] = CWE.CommonConsequence

    scopes: Union[Union[str, "SecurityScope"], list[Union[str, "SecurityScope"]]] = None
    impacts: Union[Union[str, "TechnicalImpact"], list[Union[str, "TechnicalImpact"]]] = None
    consequence_id: Optional[str] = None
    likelihood: Optional[Union[str, "LikelihoodLevel"]] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scopes):
            self.MissingRequiredField("scopes")
        if not isinstance(self.scopes, list):
            self.scopes = [self.scopes] if self.scopes is not None else []
        self.scopes = [v if isinstance(v, SecurityScope) else SecurityScope(v) for v in self.scopes]

        if self._is_empty(self.impacts):
            self.MissingRequiredField("impacts")
        if not isinstance(self.impacts, list):
            self.impacts = [self.impacts] if self.impacts is not None else []
        self.impacts = [v if isinstance(v, TechnicalImpact) else TechnicalImpact(v) for v in self.impacts]

        if self.consequence_id is not None and not isinstance(self.consequence_id, str):
            self.consequence_id = str(self.consequence_id)

        if self.likelihood is not None and not isinstance(self.likelihood, LikelihoodLevel):
            self.likelihood = LikelihoodLevel(self.likelihood)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DetectionMethod(YAMLRoot):
    """
    A method that may be employed to detect a weakness, with effectiveness (DetectionMethodsType/Detection_Method in
    XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["DetectionMethod"]
    class_class_curie: ClassVar[str] = "cwe:DetectionMethod"
    class_name: ClassVar[str] = "DetectionMethod"
    class_model_uri: ClassVar[URIRef] = CWE.DetectionMethod

    method: Union[str, "DetectionMethodType"] = None
    description: str = None
    detection_method_id: Optional[str] = None
    effectiveness: Optional[Union[str, "DetectionEffectiveness"]] = None
    effectiveness_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, DetectionMethodType):
            self.method = DetectionMethodType(self.method)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.detection_method_id is not None and not isinstance(self.detection_method_id, str):
            self.detection_method_id = str(self.detection_method_id)

        if self.effectiveness is not None and not isinstance(self.effectiveness, DetectionEffectiveness):
            self.effectiveness = DetectionEffectiveness(self.effectiveness)

        if self.effectiveness_notes is not None and not isinstance(self.effectiveness_notes, str):
            self.effectiveness_notes = str(self.effectiveness_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PotentialMitigation(YAMLRoot):
    """
    A potential mitigation for a weakness (PotentialMitigationsType/Mitigation in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["PotentialMitigation"]
    class_class_curie: ClassVar[str] = "cwe:PotentialMitigation"
    class_name: ClassVar[str] = "PotentialMitigation"
    class_model_uri: ClassVar[URIRef] = CWE.PotentialMitigation

    description: str = None
    mitigation_id: Optional[str] = None
    phases: Optional[Union[Union[str, "LifecyclePhase"], list[Union[str, "LifecyclePhase"]]]] = empty_list()
    strategy: Optional[Union[str, "MitigationStrategy"]] = None
    effectiveness: Optional[Union[str, "MitigationEffectiveness"]] = None
    effectiveness_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.mitigation_id is not None and not isinstance(self.mitigation_id, str):
            self.mitigation_id = str(self.mitigation_id)

        if not isinstance(self.phases, list):
            self.phases = [self.phases] if self.phases is not None else []
        self.phases = [v if isinstance(v, LifecyclePhase) else LifecyclePhase(v) for v in self.phases]

        if self.strategy is not None and not isinstance(self.strategy, MitigationStrategy):
            self.strategy = MitigationStrategy(self.strategy)

        if self.effectiveness is not None and not isinstance(self.effectiveness, MitigationEffectiveness):
            self.effectiveness = MitigationEffectiveness(self.effectiveness)

        if self.effectiveness_notes is not None and not isinstance(self.effectiveness_notes, str):
            self.effectiveness_notes = str(self.effectiveness_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DemonstrativeExample(YAMLRoot):
    """
    A code example illustrating how a weakness may appear (DemonstrativeExamplesType/Demonstrative_Example in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["DemonstrativeExample"]
    class_class_curie: ClassVar[str] = "cwe:DemonstrativeExample"
    class_name: ClassVar[str] = "DemonstrativeExample"
    class_model_uri: ClassVar[URIRef] = CWE.DemonstrativeExample

    intro_text: str = None
    demonstrative_example_id: Optional[str] = None
    title_text: Optional[str] = None
    body_texts: Optional[Union[str, list[str]]] = empty_list()
    example_codes: Optional[Union[Union[dict, "ExampleCode"], list[Union[dict, "ExampleCode"]]]] = empty_list()
    references: Optional[Union[Union[dict, CWEReference], list[Union[dict, CWEReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.intro_text):
            self.MissingRequiredField("intro_text")
        if not isinstance(self.intro_text, str):
            self.intro_text = str(self.intro_text)

        if self.demonstrative_example_id is not None and not isinstance(self.demonstrative_example_id, str):
            self.demonstrative_example_id = str(self.demonstrative_example_id)

        if self.title_text is not None and not isinstance(self.title_text, str):
            self.title_text = str(self.title_text)

        if not isinstance(self.body_texts, list):
            self.body_texts = [self.body_texts] if self.body_texts is not None else []
        self.body_texts = [v if isinstance(v, str) else str(v) for v in self.body_texts]

        if not isinstance(self.example_codes, list):
            self.example_codes = [self.example_codes] if self.example_codes is not None else []
        self.example_codes = [v if isinstance(v, ExampleCode) else ExampleCode(**as_dict(v)) for v in self.example_codes]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, CWEReference) else CWEReference(**as_dict(v)) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExampleCode(YAMLRoot):
    """
    A structured code snippet within a demonstrative example (StructuredCodeType in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ExampleCode"]
    class_class_curie: ClassVar[str] = "cwe:ExampleCode"
    class_name: ClassVar[str] = "ExampleCode"
    class_model_uri: ClassVar[URIRef] = CWE.ExampleCode

    nature: Union[str, "CodeNature"] = None
    language: Optional[Union[str, "ProgrammingLanguage"]] = None
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.nature):
            self.MissingRequiredField("nature")
        if not isinstance(self.nature, CodeNature):
            self.nature = CodeNature(self.nature)

        if self.language is not None and not isinstance(self.language, ProgrammingLanguage):
            self.language = ProgrammingLanguage(self.language)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedExample(YAMLRoot):
    """
    A reference to a real-world instance of a weakness, typically a CVE (ObservedExampleType/Observed_Example in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ObservedExample"]
    class_class_curie: ClassVar[str] = "cwe:ObservedExample"
    class_name: ClassVar[str] = "ObservedExample"
    class_model_uri: ClassVar[URIRef] = CWE.ObservedExample

    reference: str = None
    description: str = None
    link: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.link):
            self.MissingRequiredField("link")
        if not isinstance(self.link, URI):
            self.link = URI(self.link)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomyMapping(YAMLRoot):
    """
    A mapping from a CWE entry to an equivalent entry in an external taxonomy (TaxonomyMappingsType/Taxonomy_Mapping
    in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["TaxonomyMapping"]
    class_class_curie: ClassVar[str] = "cwe:TaxonomyMapping"
    class_name: ClassVar[str] = "TaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CWE.TaxonomyMapping

    taxonomy_name: Union[str, "TaxonomyName"] = None
    entry_id: Optional[str] = None
    entry_name: Optional[str] = None
    mapping_fit: Optional[Union[str, "TaxonomyMappingFit"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomy_name):
            self.MissingRequiredField("taxonomy_name")
        if not isinstance(self.taxonomy_name, TaxonomyName):
            self.taxonomy_name = TaxonomyName(self.taxonomy_name)

        if self.entry_id is not None and not isinstance(self.entry_id, str):
            self.entry_id = str(self.entry_id)

        if self.entry_name is not None and not isinstance(self.entry_name, str):
            self.entry_name = str(self.entry_name)

        if self.mapping_fit is not None and not isinstance(self.mapping_fit, TaxonomyMappingFit):
            self.mapping_fit = TaxonomyMappingFit(self.mapping_fit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogMember(YAMLRoot):
    """
    A Has_Member or Member_Of entry specifying a CWE ID and the View ID in which the membership holds (MemberType in
    XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CatalogMember"]
    class_class_curie: ClassVar[str] = "cwe:CatalogMember"
    class_name: ClassVar[str] = "CatalogMember"
    class_model_uri: ClassVar[URIRef] = CWE.CatalogMember

    cwe_id: int = None
    view_id: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cwe_id):
            self.MissingRequiredField("cwe_id")
        if not isinstance(self.cwe_id, int):
            self.cwe_id = int(self.cwe_id)

        if self._is_empty(self.view_id):
            self.MissingRequiredField("view_id")
        if not isinstance(self.view_id, int):
            self.view_id = int(self.view_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    Container for category membership relationships (RelationshipsType in XSD). Holds Has_Member and optionally
    Member_Of lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Relationship"]
    class_class_curie: ClassVar[str] = "cwe:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = CWE.Relationship

    has_member: Optional[Union[Union[dict, CatalogMember], list[Union[dict, CatalogMember]]]] = empty_list()
    member_of: Optional[Union[Union[dict, CatalogMember], list[Union[dict, CatalogMember]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_member, list):
            self.has_member = [self.has_member] if self.has_member is not None else []
        self.has_member = [v if isinstance(v, CatalogMember) else CatalogMember(**as_dict(v)) for v in self.has_member]

        if not isinstance(self.member_of, list):
            self.member_of = [self.member_of] if self.member_of is not None else []
        self.member_of = [v if isinstance(v, CatalogMember) else CatalogMember(**as_dict(v)) for v in self.member_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Audience(YAMLRoot):
    """
    A target stakeholder group for a CWE view or category (AudienceType/Stakeholder in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Audience"]
    class_class_curie: ClassVar[str] = "cwe:Audience"
    class_name: ClassVar[str] = "Audience"
    class_model_uri: ClassVar[URIRef] = CWE.Audience

    type: Union[str, "StakeholderType"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StakeholderType):
            self.type = StakeholderType(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingNotes(YAMLRoot):
    """
    Guidance for when and whether to map an issue to a CWE entry (MappingNotesType in XSD). Required on every
    Weakness, Category, and View.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["MappingNotes"]
    class_class_curie: ClassVar[str] = "cwe:MappingNotes"
    class_name: ClassVar[str] = "MappingNotes"
    class_model_uri: ClassVar[URIRef] = CWE.MappingNotes

    usage: Union[str, "MappingUsage"] = None
    rationale: str = None
    comments: str = None
    reasons: Union[Union[str, "MappingReason"], list[Union[str, "MappingReason"]]] = None
    suggestions: Optional[Union[Union[dict, "MappingSuggestion"], list[Union[dict, "MappingSuggestion"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.usage):
            self.MissingRequiredField("usage")
        if not isinstance(self.usage, MappingUsage):
            self.usage = MappingUsage(self.usage)

        if self._is_empty(self.rationale):
            self.MissingRequiredField("rationale")
        if not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if self._is_empty(self.comments):
            self.MissingRequiredField("comments")
        if not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self._is_empty(self.reasons):
            self.MissingRequiredField("reasons")
        if not isinstance(self.reasons, list):
            self.reasons = [self.reasons] if self.reasons is not None else []
        self.reasons = [v if isinstance(v, MappingReason) else MappingReason(v) for v in self.reasons]

        if not isinstance(self.suggestions, list):
            self.suggestions = [self.suggestions] if self.suggestions is not None else []
        self.suggestions = [v if isinstance(v, MappingSuggestion) else MappingSuggestion(**as_dict(v)) for v in self.suggestions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingSuggestion(YAMLRoot):
    """
    A suggested alternative CWE entry for mapping purposes (SuggestionsType/Suggestion in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["MappingSuggestion"]
    class_class_curie: ClassVar[str] = "cwe:MappingSuggestion"
    class_name: ClassVar[str] = "MappingSuggestion"
    class_model_uri: ClassVar[URIRef] = CWE.MappingSuggestion

    cwe_id: int = None
    comment: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cwe_id):
            self.MissingRequiredField("cwe_id")
        if not isinstance(self.cwe_id, int):
            self.cwe_id = int(self.cwe_id)

        if self._is_empty(self.comment):
            self.MissingRequiredField("comment")
        if not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Note(YAMLRoot):
    """
    Additional commentary about a CWE entry (NotesType/Note in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Note"]
    class_class_curie: ClassVar[str] = "cwe:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = CWE.Note

    type: Union[str, "NoteType"] = None
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NoteType):
            self.type = NoteType(self.type)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentHistory(YAMLRoot):
    """
    Tracks the original author and subsequent modifications (ContentHistoryType in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["ContentHistory"]
    class_class_curie: ClassVar[str] = "cwe:ContentHistory"
    class_name: ClassVar[str] = "ContentHistory"
    class_model_uri: ClassVar[URIRef] = CWE.ContentHistory

    submission: Union[dict, "Submission"] = None
    modifications: Optional[Union[Union[dict, "Modification"], list[Union[dict, "Modification"]]]] = empty_list()
    contributions: Optional[Union[Union[dict, "Contribution"], list[Union[dict, "Contribution"]]]] = empty_list()
    previous_entry_names: Optional[Union[Union[dict, "PreviousEntryName"], list[Union[dict, "PreviousEntryName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.submission):
            self.MissingRequiredField("submission")
        if not isinstance(self.submission, Submission):
            self.submission = Submission(**as_dict(self.submission))

        if not isinstance(self.modifications, list):
            self.modifications = [self.modifications] if self.modifications is not None else []
        self.modifications = [v if isinstance(v, Modification) else Modification(**as_dict(v)) for v in self.modifications]

        self._normalize_inlined_as_list(slot_name="contributions", slot_type=Contribution, key_name="type", keyed=False)

        if not isinstance(self.previous_entry_names, list):
            self.previous_entry_names = [self.previous_entry_names] if self.previous_entry_names is not None else []
        self.previous_entry_names = [v if isinstance(v, PreviousEntryName) else PreviousEntryName(**as_dict(v)) for v in self.previous_entry_names]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Submission(YAMLRoot):
    """
    Initial submission record for a CWE entry (ContentHistoryType/Submission in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Submission"]
    class_class_curie: ClassVar[str] = "cwe:Submission"
    class_name: ClassVar[str] = "Submission"
    class_model_uri: ClassVar[URIRef] = CWE.Submission

    submission_date: Union[str, XSDDate] = None
    submission_version: str = None
    submission_release_date: Union[str, XSDDate] = None
    submission_name: Optional[str] = None
    submission_organization: Optional[str] = None
    submission_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.submission_date):
            self.MissingRequiredField("submission_date")
        if not isinstance(self.submission_date, XSDDate):
            self.submission_date = XSDDate(self.submission_date)

        if self._is_empty(self.submission_version):
            self.MissingRequiredField("submission_version")
        if not isinstance(self.submission_version, str):
            self.submission_version = str(self.submission_version)

        if self._is_empty(self.submission_release_date):
            self.MissingRequiredField("submission_release_date")
        if not isinstance(self.submission_release_date, XSDDate):
            self.submission_release_date = XSDDate(self.submission_release_date)

        if self.submission_name is not None and not isinstance(self.submission_name, str):
            self.submission_name = str(self.submission_name)

        if self.submission_organization is not None and not isinstance(self.submission_organization, str):
            self.submission_organization = str(self.submission_organization)

        if self.submission_comment is not None and not isinstance(self.submission_comment, str):
            self.submission_comment = str(self.submission_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modification(YAMLRoot):
    """
    A modification record documenting a change to a CWE entry (ContentHistoryType/Modification in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Modification"]
    class_class_curie: ClassVar[str] = "cwe:Modification"
    class_name: ClassVar[str] = "Modification"
    class_model_uri: ClassVar[URIRef] = CWE.Modification

    modification_date: Union[str, XSDDate] = None
    modification_name: Optional[str] = None
    modification_organization: Optional[str] = None
    modification_version: Optional[str] = None
    modification_release_date: Optional[Union[str, XSDDate]] = None
    modification_importance: Optional[Union[str, "ContentImportance"]] = None
    modification_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modification_date):
            self.MissingRequiredField("modification_date")
        if not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.modification_name is not None and not isinstance(self.modification_name, str):
            self.modification_name = str(self.modification_name)

        if self.modification_organization is not None and not isinstance(self.modification_organization, str):
            self.modification_organization = str(self.modification_organization)

        if self.modification_version is not None and not isinstance(self.modification_version, str):
            self.modification_version = str(self.modification_version)

        if self.modification_release_date is not None and not isinstance(self.modification_release_date, XSDDate):
            self.modification_release_date = XSDDate(self.modification_release_date)

        if self.modification_importance is not None and not isinstance(self.modification_importance, ContentImportance):
            self.modification_importance = ContentImportance(self.modification_importance)

        if self.modification_comment is not None and not isinstance(self.modification_comment, str):
            self.modification_comment = str(self.modification_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contribution(YAMLRoot):
    """
    A contribution record documenting donated content or feedback (ContentHistoryType/Contribution in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["Contribution"]
    class_class_curie: ClassVar[str] = "cwe:Contribution"
    class_name: ClassVar[str] = "Contribution"
    class_model_uri: ClassVar[URIRef] = CWE.Contribution

    type: Union[str, "ContributionType"] = None
    contribution_date: Union[str, XSDDate] = None
    contribution_name: Optional[str] = None
    contribution_organization: Optional[str] = None
    contribution_version: Optional[str] = None
    contribution_release_date: Optional[Union[str, XSDDate]] = None
    contribution_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ContributionType):
            self.type = ContributionType(self.type)

        if self._is_empty(self.contribution_date):
            self.MissingRequiredField("contribution_date")
        if not isinstance(self.contribution_date, XSDDate):
            self.contribution_date = XSDDate(self.contribution_date)

        if self.contribution_name is not None and not isinstance(self.contribution_name, str):
            self.contribution_name = str(self.contribution_name)

        if self.contribution_organization is not None and not isinstance(self.contribution_organization, str):
            self.contribution_organization = str(self.contribution_organization)

        if self.contribution_version is not None and not isinstance(self.contribution_version, str):
            self.contribution_version = str(self.contribution_version)

        if self.contribution_release_date is not None and not isinstance(self.contribution_release_date, XSDDate):
            self.contribution_release_date = XSDDate(self.contribution_release_date)

        if self.contribution_comment is not None and not isinstance(self.contribution_comment, str):
            self.contribution_comment = str(self.contribution_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreviousEntryName(YAMLRoot):
    """
    A previous name used for a CWE entry before a substantive rename (ContentHistoryType/Previous_Entry_Name in XSD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["PreviousEntryName"]
    class_class_curie: ClassVar[str] = "cwe:PreviousEntryName"
    class_name: ClassVar[str] = "PreviousEntryName"
    class_model_uri: ClassVar[URIRef] = CWE.PreviousEntryName

    name: str = None
    date: Union[str, XSDDate] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NVDWeaknessObservation(YAMLRoot):
    """
    Weakness observation from an NVD vulnerability detail page.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["NVDWeaknessObservation"]
    class_class_curie: ClassVar[str] = "cwe:NVDWeaknessObservation"
    class_name: ClassVar[str] = "NVDWeaknessObservation"
    class_model_uri: ClassVar[URIRef] = CWE.NVDWeaknessObservation

    observation_id: Union[str, NVDWeaknessObservationObservationId] = None
    observed_in_cve: str = None
    weakness: Union[int, WeaknessId] = None
    reported_by: Union[str, "WeaknessSource"] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_id):
            self.MissingRequiredField("observation_id")
        if not isinstance(self.observation_id, NVDWeaknessObservationObservationId):
            self.observation_id = NVDWeaknessObservationObservationId(self.observation_id)

        if self._is_empty(self.observed_in_cve):
            self.MissingRequiredField("observed_in_cve")
        if not isinstance(self.observed_in_cve, str):
            self.observed_in_cve = str(self.observed_in_cve)

        if self._is_empty(self.weakness):
            self.MissingRequiredField("weakness")
        if not isinstance(self.weakness, WeaknessId):
            self.weakness = WeaknessId(self.weakness)

        if self._is_empty(self.reported_by):
            self.MissingRequiredField("reported_by")
        if not isinstance(self.reported_by, WeaknessSource):
            self.reported_by = WeaknessSource(self.reported_by)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


# Enumerations
class WeaknessSource(EnumDefinitionImpl):
    """
    Source attribution for weakness data in NVD/CVE contexts.
    """
    MITRE = PermissibleValue(
        text="MITRE",
        description="Data sourced from MITRE CWE content.")
    NIST = PermissibleValue(
        text="NIST",
        description="Data produced by NIST/NVD analysis.")
    ASSIGNER = PermissibleValue(
        text="ASSIGNER",
        description="Data provided by the CVE assigner/CNA.")
    CNA = PermissibleValue(
        text="CNA",
        description="Data provided by a CVE Numbering Authority.")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or unspecified source.")

    _defn = EnumDefinition(
        name="WeaknessSource",
        description="Source attribution for weakness data in NVD/CVE contexts.",
    )

class WeaknessAbstraction(EnumDefinitionImpl):
    """
    CWE abstraction layer (AbstractionEnumeration in XSD).
    """
    PILLAR = PermissibleValue(
        text="PILLAR",
        description="Most abstract type; a theme for all class/base/variant weaknesses.")
    CLASS = PermissibleValue(
        text="CLASS",
        description="Abstract, independent of any specific language or technology.")
    BASE = PermissibleValue(
        text="BASE",
        description="Mostly independent of resource or technology; supports detection/prevention.")
    VARIANT = PermissibleValue(
        text="VARIANT",
        description="Linked to a specific language or technology.")
    COMPOUND = PermissibleValue(
        text="COMPOUND",
        description="Meaningful aggregation — Chain or Composite.")

    _defn = EnumDefinition(
        name="WeaknessAbstraction",
        description="CWE abstraction layer (AbstractionEnumeration in XSD).",
    )

class WeaknessStatus(EnumDefinitionImpl):
    """
    Lifecycle status of a CWE entry, category, or view (StatusEnumeration in XSD).
    """
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="Removed from CWE; likely a duplicate or created in error.")
    DRAFT = PermissibleValue(
        text="DRAFT",
        description="All important elements filled; may still have problems or gaps.")
    INCOMPLETE = PermissibleValue(
        text="INCOMPLETE",
        description="Not all important elements filled; quality not guaranteed.")
    OBSOLETE = PermissibleValue(
        text="OBSOLETE",
        description="Still valid but no longer relevant; likely superseded.")
    STABLE = PermissibleValue(
        text="STABLE",
        description="All important elements verified; unlikely to change significantly.")
    USABLE = PermissibleValue(
        text="USABLE",
        description="Has received close extensive review; critical elements verified.")

    _defn = EnumDefinition(
        name="WeaknessStatus",
        description="Lifecycle status of a CWE entry, category, or view (StatusEnumeration in XSD).",
    )

class WeaknessStructure(EnumDefinitionImpl):
    """
    Structural nature of a weakness (StructureEnumeration in XSD).
    """
    SIMPLE = PermissibleValue(
        text="SIMPLE",
        description="Single weakness whose exploitation is not dependent on another weakness.")
    CHAIN = PermissibleValue(
        text="CHAIN",
        description="Set of weaknesses reachable consecutively to produce a vulnerability.")
    COMPOSITE = PermissibleValue(
        text="COMPOSITE",
        description="Set of weaknesses that must all be present simultaneously.")

    _defn = EnumDefinition(
        name="WeaknessStructure",
        description="Structural nature of a weakness (StructureEnumeration in XSD).",
    )

class LikelihoodLevel(EnumDefinitionImpl):
    """
    Likelihood of exploitation or occurrence (LikelihoodEnumeration in XSD).
    """
    HIGH = PermissibleValue(text="HIGH")
    MEDIUM = PermissibleValue(text="MEDIUM")
    LOW = PermissibleValue(text="LOW")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Actual likelihood is not known.")

    _defn = EnumDefinition(
        name="LikelihoodLevel",
        description="Likelihood of exploitation or occurrence (LikelihoodEnumeration in XSD).",
    )

class WeaknessRelationNature(EnumDefinitionImpl):
    """
    Nature of a directional relationship between two CWE entries (RelatedNatureEnumeration in XSD).
    """
    CHILD_OF = PermissibleValue(
        text="CHILD_OF",
        description="Related weakness at a higher level of abstraction.")
    PARENT_OF = PermissibleValue(
        text="PARENT_OF",
        description="Related weakness at a lower level of abstraction.")
    STARTS_WITH = PermissibleValue(
        text="STARTS_WITH",
        description="Chaining; this weakness starts the chain.")
    CAN_FOLLOW = PermissibleValue(
        text="CAN_FOLLOW",
        description="Chaining; this weakness can follow the target.")
    CAN_PRECEDE = PermissibleValue(
        text="CAN_PRECEDE",
        description="Chaining; this weakness can precede the target.")
    REQUIRED_BY = PermissibleValue(
        text="REQUIRED_BY",
        description="Composite; this weakness is required by the target.")
    REQUIRES = PermissibleValue(
        text="REQUIRES",
        description="Composite; this weakness requires the target.")
    CAN_ALSO_BE = PermissibleValue(
        text="CAN_ALSO_BE",
        description="In proper context can also be perceived as the target weakness.")
    PEER_OF = PermissibleValue(
        text="PEER_OF",
        description="Shows similarity with the target; no precise fit elsewhere.")

    _defn = EnumDefinition(
        name="WeaknessRelationNature",
        description="Nature of a directional relationship between two CWE entries (RelatedNatureEnumeration in XSD).",
    )

class WeaknessOrdinalityLevel(EnumDefinitionImpl):
    """
    Potential ordering relationship of a weakness relative to others (OrdinalityEnumeration in XSD).
    """
    PRIMARY = PermissibleValue(
        text="PRIMARY",
        description="Weakness exists independent of other weaknesses.")
    RESULTANT = PermissibleValue(
        text="RESULTANT",
        description="Weakness exists only in the presence of other weaknesses.")
    INDIRECT = PermissibleValue(
        text="INDIRECT",
        description="Does not directly lead to security weaknesses but may facilitate them.")

    _defn = EnumDefinition(
        name="WeaknessOrdinalityLevel",
        description="Potential ordering relationship of a weakness relative to others (OrdinalityEnumeration in XSD).",
    )

class OrdinalQualifier(EnumDefinitionImpl):
    """
    Marks a related-weakness relationship as the primary one for a given <Nature, CWE_ID, View_ID> triple
    (OrdinalEnumeration in XSD).
    """
    PRIMARY = PermissibleValue(
        text="PRIMARY",
        description="Primary ChildOf relationship for this weakness in the given view.")

    _defn = EnumDefinition(
        name="OrdinalQualifier",
        description="""Marks a related-weakness relationship as the primary one for a given <Nature, CWE_ID, View_ID> triple (OrdinalEnumeration in XSD).""",
    )

class SecurityScope(EnumDefinitionImpl):
    """
    Security property area that can be violated by exploiting a weakness (ScopeEnumeration in XSD).
    """
    CONFIDENTIALITY = PermissibleValue(text="CONFIDENTIALITY")
    INTEGRITY = PermissibleValue(text="INTEGRITY")
    AVAILABILITY = PermissibleValue(text="AVAILABILITY")
    ACCESS_CONTROL = PermissibleValue(text="ACCESS_CONTROL")
    ACCOUNTABILITY = PermissibleValue(text="ACCOUNTABILITY")
    AUTHENTICATION = PermissibleValue(text="AUTHENTICATION")
    AUTHORIZATION = PermissibleValue(text="AUTHORIZATION")
    NON_REPUDIATION = PermissibleValue(text="NON_REPUDIATION")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="SecurityScope",
        description="Security property area that can be violated by exploiting a weakness (ScopeEnumeration in XSD).",
    )

class TechnicalImpact(EnumDefinitionImpl):
    """
    Technical impact of successfully exploiting a weakness (TechnicalImpactEnumeration in XSD).
    """
    MODIFY_MEMORY = PermissibleValue(text="MODIFY_MEMORY")
    READ_MEMORY = PermissibleValue(text="READ_MEMORY")
    MODIFY_FILES_OR_DIRECTORIES = PermissibleValue(text="MODIFY_FILES_OR_DIRECTORIES")
    READ_FILES_OR_DIRECTORIES = PermissibleValue(text="READ_FILES_OR_DIRECTORIES")
    MODIFY_APPLICATION_DATA = PermissibleValue(text="MODIFY_APPLICATION_DATA")
    READ_APPLICATION_DATA = PermissibleValue(text="READ_APPLICATION_DATA")
    DOS_CRASH_EXIT_OR_RESTART = PermissibleValue(
        text="DOS_CRASH_EXIT_OR_RESTART",
        description="DoS: Crash, Exit, or Restart")
    DOS_AMPLIFICATION = PermissibleValue(
        text="DOS_AMPLIFICATION",
        description="DoS: Amplification")
    DOS_INSTABILITY = PermissibleValue(
        text="DOS_INSTABILITY",
        description="DoS: Instability")
    DOS_RESOURCE_CONSUMPTION_CPU = PermissibleValue(
        text="DOS_RESOURCE_CONSUMPTION_CPU",
        description="DoS: Resource Consumption (CPU)")
    DOS_RESOURCE_CONSUMPTION_MEMORY = PermissibleValue(
        text="DOS_RESOURCE_CONSUMPTION_MEMORY",
        description="DoS: Resource Consumption (Memory)")
    DOS_RESOURCE_CONSUMPTION_OTHER = PermissibleValue(
        text="DOS_RESOURCE_CONSUMPTION_OTHER",
        description="DoS: Resource Consumption (Other)")
    EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS = PermissibleValue(text="EXECUTE_UNAUTHORIZED_CODE_OR_COMMANDS")
    GAIN_PRIVILEGES_OR_ASSUME_IDENTITY = PermissibleValue(text="GAIN_PRIVILEGES_OR_ASSUME_IDENTITY")
    BYPASS_PROTECTION_MECHANISM = PermissibleValue(text="BYPASS_PROTECTION_MECHANISM")
    HIDE_ACTIVITIES = PermissibleValue(text="HIDE_ACTIVITIES")
    ALTER_EXECUTION_LOGIC = PermissibleValue(text="ALTER_EXECUTION_LOGIC")
    QUALITY_DEGRADATION = PermissibleValue(text="QUALITY_DEGRADATION")
    UNEXPECTED_STATE = PermissibleValue(text="UNEXPECTED_STATE")
    VARIES_BY_CONTEXT = PermissibleValue(text="VARIES_BY_CONTEXT")
    INCREASE_ANALYTICAL_COMPLEXITY = PermissibleValue(
        text="INCREASE_ANALYTICAL_COMPLEXITY",
        description="Makes vulnerability harder to find and fix.")
    REDUCE_MAINTAINABILITY = PermissibleValue(text="REDUCE_MAINTAINABILITY")
    REDUCE_PERFORMANCE = PermissibleValue(text="REDUCE_PERFORMANCE")
    REDUCE_RELIABILITY = PermissibleValue(text="REDUCE_RELIABILITY")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="TechnicalImpact",
        description="Technical impact of successfully exploiting a weakness (TechnicalImpactEnumeration in XSD).",
    )

class LifecyclePhase(EnumDefinitionImpl):
    """
    Phase in the product lifecycle where a weakness may be introduced or a mitigation applied (PhaseEnumeration in
    XSD).
    """
    POLICY = PermissibleValue(text="POLICY")
    REQUIREMENTS = PermissibleValue(text="REQUIREMENTS")
    ARCHITECTURE_AND_DESIGN = PermissibleValue(text="ARCHITECTURE_AND_DESIGN")
    IMPLEMENTATION = PermissibleValue(text="IMPLEMENTATION")
    BUILD_AND_COMPILATION = PermissibleValue(text="BUILD_AND_COMPILATION")
    TESTING = PermissibleValue(text="TESTING")
    DOCUMENTATION = PermissibleValue(text="DOCUMENTATION")
    BUNDLING = PermissibleValue(text="BUNDLING")
    DISTRIBUTION = PermissibleValue(text="DISTRIBUTION")
    INSTALLATION = PermissibleValue(text="INSTALLATION")
    SYSTEM_CONFIGURATION = PermissibleValue(text="SYSTEM_CONFIGURATION")
    OPERATION = PermissibleValue(text="OPERATION")
    PATCHING_AND_MAINTENANCE = PermissibleValue(text="PATCHING_AND_MAINTENANCE")
    PORTING = PermissibleValue(text="PORTING")
    INTEGRATION = PermissibleValue(text="INTEGRATION")
    MANUFACTURING = PermissibleValue(text="MANUFACTURING")
    DECOMMISSIONING_AND_END_OF_LIFE = PermissibleValue(text="DECOMMISSIONING_AND_END_OF_LIFE")

    _defn = EnumDefinition(
        name="LifecyclePhase",
        description="""Phase in the product lifecycle where a weakness may be introduced or a mitigation applied (PhaseEnumeration in XSD).""",
    )

class MitigationStrategy(EnumDefinitionImpl):
    """
    General strategy for protecting a system (MitigationStrategyEnumeration in XSD).
    """
    ATTACK_SURFACE_REDUCTION = PermissibleValue(text="ATTACK_SURFACE_REDUCTION")
    COMPILATION_OR_BUILD_HARDENING = PermissibleValue(text="COMPILATION_OR_BUILD_HARDENING")
    ENFORCEMENT_BY_CONVERSION = PermissibleValue(text="ENFORCEMENT_BY_CONVERSION")
    ENVIRONMENT_HARDENING = PermissibleValue(text="ENVIRONMENT_HARDENING")
    FIREWALL = PermissibleValue(text="FIREWALL")
    INPUT_VALIDATION = PermissibleValue(text="INPUT_VALIDATION")
    LANGUAGE_SELECTION = PermissibleValue(text="LANGUAGE_SELECTION")
    LIBRARIES_OR_FRAMEWORKS = PermissibleValue(text="LIBRARIES_OR_FRAMEWORKS")
    RESOURCE_LIMITATION = PermissibleValue(text="RESOURCE_LIMITATION")
    OUTPUT_ENCODING = PermissibleValue(text="OUTPUT_ENCODING")
    PARAMETERIZATION = PermissibleValue(text="PARAMETERIZATION")
    REFACTORING = PermissibleValue(text="REFACTORING")
    SANDBOX_OR_JAIL = PermissibleValue(text="SANDBOX_OR_JAIL")
    SEPARATION_OF_PRIVILEGE = PermissibleValue(text="SEPARATION_OF_PRIVILEGE")

    _defn = EnumDefinition(
        name="MitigationStrategy",
        description="General strategy for protecting a system (MitigationStrategyEnumeration in XSD).",
    )

class DetectionMethodType(EnumDefinitionImpl):
    """
    Method that may be employed to detect a weakness (DetectionMethodEnumeration in XSD).
    """
    AUTOMATED_ANALYSIS = PermissibleValue(text="AUTOMATED_ANALYSIS")
    AUTOMATED_DYNAMIC_ANALYSIS = PermissibleValue(text="AUTOMATED_DYNAMIC_ANALYSIS")
    AUTOMATED_STATIC_ANALYSIS = PermissibleValue(text="AUTOMATED_STATIC_ANALYSIS")
    AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE = PermissibleValue(
        text="AUTOMATED_STATIC_ANALYSIS_SOURCE_CODE",
        description="Automated Static Analysis - Source Code")
    AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE = PermissibleValue(
        text="AUTOMATED_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
        description="Automated Static Analysis - Binary or Bytecode")
    FUZZING = PermissibleValue(text="FUZZING")
    MANUAL_ANALYSIS = PermissibleValue(text="MANUAL_ANALYSIS")
    MANUAL_DYNAMIC_ANALYSIS = PermissibleValue(text="MANUAL_DYNAMIC_ANALYSIS")
    MANUAL_STATIC_ANALYSIS = PermissibleValue(text="MANUAL_STATIC_ANALYSIS")
    MANUAL_STATIC_ANALYSIS_SOURCE_CODE = PermissibleValue(
        text="MANUAL_STATIC_ANALYSIS_SOURCE_CODE",
        description="Manual Static Analysis - Source Code")
    MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE = PermissibleValue(
        text="MANUAL_STATIC_ANALYSIS_BINARY_OR_BYTECODE",
        description="Manual Static Analysis - Binary or Bytecode")
    WHITE_BOX = PermissibleValue(text="WHITE_BOX")
    BLACK_BOX = PermissibleValue(text="BLACK_BOX")
    ARCHITECTURE_OR_DESIGN_REVIEW = PermissibleValue(text="ARCHITECTURE_OR_DESIGN_REVIEW")
    DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION = PermissibleValue(text="DYNAMIC_ANALYSIS_WITH_MANUAL_RESULTS_INTERPRETATION")
    DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION = PermissibleValue(text="DYNAMIC_ANALYSIS_WITH_AUTOMATED_RESULTS_INTERPRETATION")
    FORMAL_VERIFICATION = PermissibleValue(text="FORMAL_VERIFICATION")
    SIMULATION_EMULATION = PermissibleValue(text="SIMULATION_EMULATION")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="DetectionMethodType",
        description="Method that may be employed to detect a weakness (DetectionMethodEnumeration in XSD).",
    )

class DetectionEffectiveness(EnumDefinitionImpl):
    """
    Effectiveness of a detection method (DetectionEffectivenessEnumeration in XSD).
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Succeeds frequently; few false reports.")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Applicable broadly but may lack complete coverage.")
    SOAR_PARTIAL = PermissibleValue(
        text="SOAR_PARTIAL",
        description="Cost-effective for partial coverage per IATAC SOAR report.")
    OPPORTUNISTIC = PermissibleValue(
        text="OPPORTUNISTIC",
        description="May succeed by chance rather than reliably.")
    LIMITED = PermissibleValue(
        text="LIMITED",
        description="Useful in limited circumstances.")
    NONE = PermissibleValue(
        text="NONE",
        description="Highly unlikely to work.")

    _defn = EnumDefinition(
        name="DetectionEffectiveness",
        description="Effectiveness of a detection method (DetectionEffectivenessEnumeration in XSD).",
    )

class MitigationEffectiveness(EnumDefinitionImpl):
    """
    Effectiveness of a potential mitigation (EffectivenessEnumeration in XSD).
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Frequently eliminates the weakness entirely.")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Prevents multiple forms but lacks complete coverage.")
    LIMITED = PermissibleValue(
        text="LIMITED",
        description="Useful in limited circumstances.")
    INCIDENTAL = PermissibleValue(
        text="INCIDENTAL",
        description="Generally not effective; only protects by chance.")
    DEFENSE_IN_DEPTH = PermissibleValue(
        text="DEFENSE_IN_DEPTH",
        description="Minimizes impact rather than preventing the weakness.")
    DISCOURAGED_COMMON_PRACTICE = PermissibleValue(
        text="DISCOURAGED_COMMON_PRACTICE",
        description="Commonly attempted but known to be ineffective or risky.")
    NONE = PermissibleValue(text="NONE")

    _defn = EnumDefinition(
        name="MitigationEffectiveness",
        description="Effectiveness of a potential mitigation (EffectivenessEnumeration in XSD).",
    )

class NoteType(EnumDefinitionImpl):
    """
    Type of note on a CWE entry (NoteTypeEnumeration in XSD).
    """
    APPLICABLE_PLATFORM = PermissibleValue(text="APPLICABLE_PLATFORM")
    MAINTENANCE = PermissibleValue(text="MAINTENANCE")
    RELATIONSHIP = PermissibleValue(text="RELATIONSHIP")
    RESEARCH_GAP = PermissibleValue(text="RESEARCH_GAP")
    TERMINOLOGY = PermissibleValue(text="TERMINOLOGY")
    THEORETICAL = PermissibleValue(text="THEORETICAL")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="NoteType",
        description="Type of note on a CWE entry (NoteTypeEnumeration in XSD).",
    )

class CWEViewType(EnumDefinitionImpl):
    """
    Type of CWE view (ViewTypeEnumeration in XSD).
    """
    GRAPH = PermissibleValue(
        text="GRAPH",
        description="Hierarchical representation from a specific vantage point.")
    EXPLICIT = PermissibleValue(
        text="EXPLICIT",
        description="Flat list related through an external factor (e.g. Top-N list).")
    IMPLICIT = PermissibleValue(
        text="IMPLICIT",
        description="Subset identified by an XSL filter expression.")

    _defn = EnumDefinition(
        name="CWEViewType",
        description="Type of CWE view (ViewTypeEnumeration in XSD).",
    )

class FunctionalArea(EnumDefinitionImpl):
    """
    Functional area where a weakness is most likely to occur (FunctionalAreaEnumeration in XSD).
    """
    AUTHENTICATION = PermissibleValue(text="AUTHENTICATION")
    AUTHORIZATION = PermissibleValue(text="AUTHORIZATION")
    CODE_LIBRARIES = PermissibleValue(text="CODE_LIBRARIES")
    COUNTERS = PermissibleValue(text="COUNTERS")
    CRYPTOGRAPHY = PermissibleValue(text="CRYPTOGRAPHY")
    ERROR_HANDLING = PermissibleValue(text="ERROR_HANDLING")
    INTERPROCESS_COMMUNICATION = PermissibleValue(text="INTERPROCESS_COMMUNICATION")
    FILE_PROCESSING = PermissibleValue(text="FILE_PROCESSING")
    LOGGING = PermissibleValue(text="LOGGING")
    MEMORY_MANAGEMENT = PermissibleValue(text="MEMORY_MANAGEMENT")
    NETWORKING = PermissibleValue(text="NETWORKING")
    NUMBER_PROCESSING = PermissibleValue(text="NUMBER_PROCESSING")
    PROGRAM_INVOCATION = PermissibleValue(text="PROGRAM_INVOCATION")
    PROTECTION_MECHANISM = PermissibleValue(text="PROTECTION_MECHANISM")
    SESSION_MANAGEMENT = PermissibleValue(text="SESSION_MANAGEMENT")
    SIGNALS = PermissibleValue(text="SIGNALS")
    STRING_PROCESSING = PermissibleValue(text="STRING_PROCESSING")
    NOT_FUNCTIONAL_AREA_SPECIFIC = PermissibleValue(text="NOT_FUNCTIONAL_AREA_SPECIFIC")
    POWER = PermissibleValue(text="POWER")
    CLOCK = PermissibleValue(text="CLOCK")

    _defn = EnumDefinition(
        name="FunctionalArea",
        description="Functional area where a weakness is most likely to occur (FunctionalAreaEnumeration in XSD).",
    )

class AffectedResource(EnumDefinitionImpl):
    """
    System resource that can be affected by exploiting a weakness (ResourceEnumeration in XSD).
    """
    CPU = PermissibleValue(text="CPU")
    FILE_OR_DIRECTORY = PermissibleValue(text="FILE_OR_DIRECTORY")
    MEMORY = PermissibleValue(text="MEMORY")
    SYSTEM_PROCESS = PermissibleValue(text="SYSTEM_PROCESS")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="AffectedResource",
        description="System resource that can be affected by exploiting a weakness (ResourceEnumeration in XSD).",
    )

class PlatformPrevalence(EnumDefinitionImpl):
    """
    Regularity with which a weakness applies to a given platform (PrevalenceEnumeration in XSD).
    """
    OFTEN = PermissibleValue(text="OFTEN")
    SOMETIMES = PermissibleValue(text="SOMETIMES")
    RARELY = PermissibleValue(text="RARELY")
    UNDETERMINED = PermissibleValue(text="UNDETERMINED")

    _defn = EnumDefinition(
        name="PlatformPrevalence",
        description="Regularity with which a weakness applies to a given platform (PrevalenceEnumeration in XSD).",
    )

class ProgrammingLanguage(EnumDefinitionImpl):
    """
    Source code language or data format (LanguageNameEnumeration in XSD).
    """
    ADA = PermissibleValue(text="ADA")
    ARM_ASSEMBLY = PermissibleValue(text="ARM_ASSEMBLY")
    ASP = PermissibleValue(text="ASP")
    ASP_DOT_NET = PermissibleValue(text="ASP_DOT_NET")
    BASIC = PermissibleValue(text="BASIC")
    C = PermissibleValue(text="C")
    C_PLUS_PLUS = PermissibleValue(text="C_PLUS_PLUS")
    C_SHARP = PermissibleValue(text="C_SHARP")
    COBOL = PermissibleValue(text="COBOL")
    FORTRAN = PermissibleValue(text="FORTRAN")
    FSHARP = PermissibleValue(text="FSHARP")
    GO = PermissibleValue(text="GO")
    HTML = PermissibleValue(text="HTML")
    JAVA = PermissibleValue(text="JAVA")
    JAVASCRIPT = PermissibleValue(text="JAVASCRIPT")
    JSON = PermissibleValue(text="JSON")
    JSP = PermissibleValue(text="JSP")
    OBJECTIVE_C = PermissibleValue(text="OBJECTIVE_C")
    PASCAL = PermissibleValue(text="PASCAL")
    PERL = PermissibleValue(text="PERL")
    PHP = PermissibleValue(text="PHP")
    PSEUDOCODE = PermissibleValue(text="PSEUDOCODE")
    PYTHON = PermissibleValue(text="PYTHON")
    RUBY = PermissibleValue(text="RUBY")
    RUST = PermissibleValue(text="RUST")
    SHELL = PermissibleValue(text="SHELL")
    SQL = PermissibleValue(text="SQL")
    SWIFT = PermissibleValue(text="SWIFT")
    VB_DOT_NET = PermissibleValue(text="VB_DOT_NET")
    VERILOG = PermissibleValue(text="VERILOG")
    VHDL = PermissibleValue(text="VHDL")
    XML = PermissibleValue(text="XML")
    X86_ASSEMBLY = PermissibleValue(text="X86_ASSEMBLY")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="ProgrammingLanguage",
        description="Source code language or data format (LanguageNameEnumeration in XSD).",
    )

class LanguageClass(EnumDefinitionImpl):
    """
    Class of programming language (LanguageClassEnumeration in XSD).
    """
    ASSEMBLY = PermissibleValue(text="ASSEMBLY")
    COMPILED = PermissibleValue(text="COMPILED")
    HARDWARE_DESCRIPTION_LANGUAGE = PermissibleValue(text="HARDWARE_DESCRIPTION_LANGUAGE")
    INTERPRETED = PermissibleValue(text="INTERPRETED")
    OBJECT_ORIENTED = PermissibleValue(text="OBJECT_ORIENTED")
    MEMORY_UNSAFE = PermissibleValue(text="MEMORY_UNSAFE")
    NOT_LANGUAGE_SPECIFIC = PermissibleValue(text="NOT_LANGUAGE_SPECIFIC")

    _defn = EnumDefinition(
        name="LanguageClass",
        description="Class of programming language (LanguageClassEnumeration in XSD).",
    )

class ArchitectureName(EnumDefinitionImpl):
    """
    Processor architecture (ArchitectureNameEnumeration in XSD).
    """
    ALPHA = PermissibleValue(text="ALPHA")
    ARM = PermissibleValue(text="ARM")
    ITANIUM = PermissibleValue(text="ITANIUM")
    POWER_ARCHITECTURE = PermissibleValue(text="POWER_ARCHITECTURE")
    SPARC = PermissibleValue(text="SPARC")
    X86 = PermissibleValue(text="X86")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="ArchitectureName",
        description="Processor architecture (ArchitectureNameEnumeration in XSD).",
    )

class ArchitectureClass(EnumDefinitionImpl):
    """
    Class of processor architecture (ArchitectureClassEnumeration in XSD).
    """
    EMBEDDED = PermissibleValue(text="EMBEDDED")
    MICROCOMPUTER = PermissibleValue(text="MICROCOMPUTER")
    WORKSTATION = PermissibleValue(text="WORKSTATION")
    NOT_ARCHITECTURE_SPECIFIC = PermissibleValue(text="NOT_ARCHITECTURE_SPECIFIC")

    _defn = EnumDefinition(
        name="ArchitectureClass",
        description="Class of processor architecture (ArchitectureClassEnumeration in XSD).",
    )

class OperatingSystemName(EnumDefinitionImpl):
    """
    Operating system (OperatingSystemNameEnumeration in XSD).
    """
    AIX = PermissibleValue(text="AIX")
    ANDROID = PermissibleValue(text="ANDROID")
    BLACKBERRY_OS = PermissibleValue(text="BLACKBERRY_OS")
    CHROME_OS = PermissibleValue(text="CHROME_OS")
    DARWIN = PermissibleValue(text="DARWIN")
    FREEBSD = PermissibleValue(text="FREEBSD")
    IOS = PermissibleValue(text="IOS")
    MACOS = PermissibleValue(text="MACOS")
    NETBSD = PermissibleValue(text="NETBSD")
    OPENBSD = PermissibleValue(text="OPENBSD")
    RED_HAT = PermissibleValue(text="RED_HAT")
    SOLARIS = PermissibleValue(text="SOLARIS")
    SUSE = PermissibleValue(text="SUSE")
    TVOS = PermissibleValue(text="TVOS")
    UBUNTU = PermissibleValue(text="UBUNTU")
    WATCHOS = PermissibleValue(text="WATCHOS")
    WINDOWS_9X = PermissibleValue(text="WINDOWS_9X")
    WINDOWS_EMBEDDED = PermissibleValue(text="WINDOWS_EMBEDDED")
    WINDOWS_NT = PermissibleValue(text="WINDOWS_NT")

    _defn = EnumDefinition(
        name="OperatingSystemName",
        description="Operating system (OperatingSystemNameEnumeration in XSD).",
    )

class OperatingSystemClass(EnumDefinitionImpl):
    """
    Class of operating system (OperatingSystemClassEnumeration in XSD).
    """
    LINUX = PermissibleValue(text="LINUX")
    MACOS = PermissibleValue(text="MACOS")
    UNIX = PermissibleValue(text="UNIX")
    WINDOWS = PermissibleValue(text="WINDOWS")
    NOT_OS_SPECIFIC = PermissibleValue(text="NOT_OS_SPECIFIC")

    _defn = EnumDefinition(
        name="OperatingSystemClass",
        description="Class of operating system (OperatingSystemClassEnumeration in XSD).",
    )

class TechnologyName(EnumDefinitionImpl):
    """
    Specific technology applicable to a weakness (TechnologyNameEnumeration in XSD).
    """
    AI_ML = PermissibleValue(text="AI_ML")
    WEB_SERVER = PermissibleValue(text="WEB_SERVER")
    DATABASE_SERVER = PermissibleValue(text="DATABASE_SERVER")
    ACCELERATOR_HARDWARE = PermissibleValue(text="ACCELERATOR_HARDWARE")
    ANALOG_AND_MIXED_SIGNAL_HARDWARE = PermissibleValue(text="ANALOG_AND_MIXED_SIGNAL_HARDWARE")
    AUDIO_VIDEO_HARDWARE = PermissibleValue(text="AUDIO_VIDEO_HARDWARE")
    BUS_INTERFACE_HARDWARE = PermissibleValue(text="BUS_INTERFACE_HARDWARE")
    CLOCK_COUNTER_HARDWARE = PermissibleValue(text="CLOCK_COUNTER_HARDWARE")
    COMMUNICATION_HARDWARE = PermissibleValue(text="COMMUNICATION_HARDWARE")
    CONTROLLER_HARDWARE = PermissibleValue(text="CONTROLLER_HARDWARE")
    MEMORY_HARDWARE = PermissibleValue(text="MEMORY_HARDWARE")
    MICROCONTROLLER_HARDWARE = PermissibleValue(text="MICROCONTROLLER_HARDWARE")
    NETWORK_ON_CHIP_HARDWARE = PermissibleValue(text="NETWORK_ON_CHIP_HARDWARE")
    POWER_MANAGEMENT_HARDWARE = PermissibleValue(text="POWER_MANAGEMENT_HARDWARE")
    PROCESSOR_HARDWARE = PermissibleValue(text="PROCESSOR_HARDWARE")
    SECURITY_HARDWARE = PermissibleValue(text="SECURITY_HARDWARE")
    SENSOR_HARDWARE = PermissibleValue(text="SENSOR_HARDWARE")
    STORAGE_HARDWARE = PermissibleValue(text="STORAGE_HARDWARE")
    TEST_DEBUG_HARDWARE = PermissibleValue(text="TEST_DEBUG_HARDWARE")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="TechnologyName",
        description="Specific technology applicable to a weakness (TechnologyNameEnumeration in XSD).",
    )

class TechnologyClass(EnumDefinitionImpl):
    """
    Class of technology (TechnologyClassEnumeration in XSD).
    """
    CLIENT_SERVER = PermissibleValue(text="CLIENT_SERVER")
    CLOUD_COMPUTING = PermissibleValue(text="CLOUD_COMPUTING")
    ICS_OT = PermissibleValue(text="ICS_OT")
    MAINFRAME = PermissibleValue(text="MAINFRAME")
    MOBILE = PermissibleValue(text="MOBILE")
    N_TIER = PermissibleValue(text="N_TIER")
    SOA = PermissibleValue(text="SOA")
    SYSTEM_ON_CHIP = PermissibleValue(text="SYSTEM_ON_CHIP")
    WEB_BASED = PermissibleValue(text="WEB_BASED")
    NOT_TECHNOLOGY_SPECIFIC = PermissibleValue(text="NOT_TECHNOLOGY_SPECIFIC")

    _defn = EnumDefinition(
        name="TechnologyClass",
        description="Class of technology (TechnologyClassEnumeration in XSD).",
    )

class TaxonomyMappingFit(EnumDefinitionImpl):
    """
    Closeness of a mapping to an external taxonomy (TaxonomyMappingFitEnumeration in XSD).
    """
    EXACT = PermissibleValue(text="EXACT")
    CWE_MORE_ABSTRACT = PermissibleValue(text="CWE_MORE_ABSTRACT")
    CWE_MORE_SPECIFIC = PermissibleValue(text="CWE_MORE_SPECIFIC")
    IMPRECISE = PermissibleValue(text="IMPRECISE")
    PERSPECTIVE = PermissibleValue(text="PERSPECTIVE")

    _defn = EnumDefinition(
        name="TaxonomyMappingFit",
        description="Closeness of a mapping to an external taxonomy (TaxonomyMappingFitEnumeration in XSD).",
    )

class TaxonomyName(EnumDefinitionImpl):
    """
    Known taxonomy that can be mapped to CWE (TaxonomyNameEnumeration in XSD).
    """
    SEVEN_PERNICIOUS_KINGDOMS = PermissibleValue(text="SEVEN_PERNICIOUS_KINGDOMS")
    NINETEEN_DEADLY_SINS = PermissibleValue(text="NINETEEN_DEADLY_SINS")
    ASLAM = PermissibleValue(text="ASLAM")
    BISHOP = PermissibleValue(text="BISHOP")
    CERT_C_SECURE_CODING = PermissibleValue(text="CERT_C_SECURE_CODING")
    CERT_CPP_SECURE_CODING = PermissibleValue(text="CERT_CPP_SECURE_CODING")
    THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011 = PermissibleValue(text="THE_CERT_ORACLE_SECURE_CODING_STANDARD_FOR_JAVA_2011")
    CLASP = PermissibleValue(text="CLASP")
    ISA_IEC_62443 = PermissibleValue(text="ISA_IEC_62443")
    LANDWEHR = PermissibleValue(text="LANDWEHR")
    OMG_ASCSM = PermissibleValue(text="OMG_ASCSM")
    OMG_ASCRM = PermissibleValue(text="OMG_ASCRM")
    OMG_ASCMM = PermissibleValue(text="OMG_ASCMM")
    OMG_ASCPEM = PermissibleValue(text="OMG_ASCPEM")
    OWASP_TOP_TEN_2004 = PermissibleValue(text="OWASP_TOP_TEN_2004")
    OWASP_TOP_TEN_2007 = PermissibleValue(text="OWASP_TOP_TEN_2007")
    OWASP_TOP_TEN = PermissibleValue(text="OWASP_TOP_TEN")
    PLOVER = PermissibleValue(text="PLOVER")
    PROTECTION_ANALYSIS = PermissibleValue(text="PROTECTION_ANALYSIS")
    RISOS = PermissibleValue(text="RISOS")
    SEI_CERT_C_CODING_STANDARD = PermissibleValue(text="SEI_CERT_C_CODING_STANDARD")
    SEI_CERT_CPP_CODING_STANDARD = PermissibleValue(text="SEI_CERT_CPP_CODING_STANDARD")
    SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA = PermissibleValue(text="SEI_CERT_ORACLE_CODING_STANDARD_FOR_JAVA")
    SEI_CERT_PERL_CODING_STANDARD = PermissibleValue(text="SEI_CERT_PERL_CODING_STANDARD")
    SOFTWARE_FAULT_PATTERNS = PermissibleValue(text="SOFTWARE_FAULT_PATTERNS")
    WEBER_KARGER_PARADKAR = PermissibleValue(text="WEBER_KARGER_PARADKAR")
    WASC = PermissibleValue(text="WASC")

    _defn = EnumDefinition(
        name="TaxonomyName",
        description="Known taxonomy that can be mapped to CWE (TaxonomyNameEnumeration in XSD).",
    )

class MappingUsage(EnumDefinitionImpl):
    """
    Whether a CWE entry should be used for mapping (UsageEnumeration in XSD).
    """
    ALLOWED = PermissibleValue(
        text="ALLOWED",
        description="May be used to map to real-world vulnerabilities.")
    ALLOWED_WITH_REVIEW = PermissibleValue(
        text="ALLOWED_WITH_REVIEW",
        description="May be used in limited situations requiring careful review.")
    DISCOURAGED = PermissibleValue(
        text="DISCOURAGED",
        description="Should not be used for mapping.")
    PROHIBITED = PermissibleValue(
        text="PROHIBITED",
        description="Must not be used for mapping.")

    _defn = EnumDefinition(
        name="MappingUsage",
        description="Whether a CWE entry should be used for mapping (UsageEnumeration in XSD).",
    )

class MappingReason(EnumDefinitionImpl):
    """
    Reason why a CWE entry should not be used for mapping (ReasonEnumeration in XSD).
    """
    ABSTRACTION = PermissibleValue(text="ABSTRACTION")
    CATEGORY = PermissibleValue(text="CATEGORY")
    VIEW = PermissibleValue(text="VIEW")
    DEPRECATED = PermissibleValue(text="DEPRECATED")
    POTENTIAL_DEPRECATION = PermissibleValue(text="POTENTIAL_DEPRECATION")
    FREQUENT_MISUSE = PermissibleValue(text="FREQUENT_MISUSE")
    FREQUENT_MISINTERPRETATION = PermissibleValue(text="FREQUENT_MISINTERPRETATION")
    MULTIPLE_USE = PermissibleValue(text="MULTIPLE_USE")
    CWE_OVERLAP = PermissibleValue(text="CWE_OVERLAP")
    ACCEPTABLE_USE = PermissibleValue(text="ACCEPTABLE_USE")
    POTENTIAL_MAJOR_CHANGES = PermissibleValue(text="POTENTIAL_MAJOR_CHANGES")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="MappingReason",
        description="Reason why a CWE entry should not be used for mapping (ReasonEnumeration in XSD).",
    )

class StakeholderType(EnumDefinitionImpl):
    """
    Type of stakeholder in the CWE community (StakeholderEnumeration in XSD).
    """
    ACADEMIC_RESEARCHERS = PermissibleValue(text="ACADEMIC_RESEARCHERS")
    APPLIED_RESEARCHERS = PermissibleValue(text="APPLIED_RESEARCHERS")
    ASSESSMENT_TEAMS = PermissibleValue(text="ASSESSMENT_TEAMS")
    ASSESSMENT_TOOL_VENDORS = PermissibleValue(text="ASSESSMENT_TOOL_VENDORS")
    CWE_TEAM = PermissibleValue(text="CWE_TEAM")
    EDUCATORS = PermissibleValue(text="EDUCATORS")
    HARDWARE_DESIGNERS = PermissibleValue(text="HARDWARE_DESIGNERS")
    INFORMATION_PROVIDERS = PermissibleValue(text="INFORMATION_PROVIDERS")
    PRODUCT_CUSTOMERS = PermissibleValue(text="PRODUCT_CUSTOMERS")
    PRODUCT_VENDORS = PermissibleValue(text="PRODUCT_VENDORS")
    SOFTWARE_DEVELOPERS = PermissibleValue(text="SOFTWARE_DEVELOPERS")
    VULNERABILITY_ANALYSTS = PermissibleValue(text="VULNERABILITY_ANALYSTS")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="StakeholderType",
        description="Type of stakeholder in the CWE community (StakeholderEnumeration in XSD).",
    )

class CodeNature(EnumDefinitionImpl):
    """
    Nature of a code snippet in a demonstrative example (StructuredCodeNatureEnumeration in XSD).
    """
    ATTACK = PermissibleValue(text="ATTACK")
    BAD = PermissibleValue(text="BAD")
    GOOD = PermissibleValue(text="GOOD")
    INFORMATIVE = PermissibleValue(text="INFORMATIVE")
    MITIGATION = PermissibleValue(text="MITIGATION")
    RESULT = PermissibleValue(text="RESULT")

    _defn = EnumDefinition(
        name="CodeNature",
        description="Nature of a code snippet in a demonstrative example (StructuredCodeNatureEnumeration in XSD).",
    )

class ContentImportance(EnumDefinitionImpl):
    """
    Importance level of a content modification (ImportanceEnumeration in XSD).
    """
    NORMAL = PermissibleValue(text="NORMAL")
    CRITICAL = PermissibleValue(
        text="CRITICAL",
        description="Changes the meaning or interpretation of the entry.")

    _defn = EnumDefinition(
        name="ContentImportance",
        description="Importance level of a content modification (ImportanceEnumeration in XSD).",
    )

class ContributionType(EnumDefinitionImpl):
    """
    Whether a contribution was donated content or general feedback.
    """
    CONTENT = PermissibleValue(
        text="CONTENT",
        description="Content donated to the CWE entry.")
    FEEDBACK = PermissibleValue(
        text="FEEDBACK",
        description="General feedback given about the CWE entry.")

    _defn = EnumDefinition(
        name="ContributionType",
        description="Whether a contribution was donated content or general feedback.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DCT.identifier, name="id", curie=DCT.curie('identifier'),
                   model_uri=CWE.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CWE.name, domain=None, range=Optional[str])

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=CWE.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=CWE.description, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=CWE.version, domain=None, range=Optional[str])

slots.date = Slot(uri=DCT.date, name="date", curie=DCT.curie('date'),
                   model_uri=CWE.date, domain=None, range=Optional[Union[str, XSDDate]])

slots.source = Slot(uri=DCT.source, name="source", curie=DCT.curie('source'),
                   model_uri=CWE.source, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=CWE.url, domain=None, range=Optional[Union[str, URI]])

slots.url_date = Slot(uri=CWE.url_date, name="url_date", curie=CWE.curie('url_date'),
                   model_uri=CWE.url_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.summary = Slot(uri=CWE.summary, name="summary", curie=CWE.curie('summary'),
                   model_uri=CWE.summary, domain=None, range=Optional[str])

slots.objective = Slot(uri=CWE.objective, name="objective", curie=CWE.curie('objective'),
                   model_uri=CWE.objective, domain=None, range=Optional[str])

slots.filter = Slot(uri=CWE.filter, name="filter", curie=CWE.curie('filter'),
                   model_uri=CWE.filter, domain=None, range=Optional[str])

slots.comment = Slot(uri=CWE.comment, name="comment", curie=CWE.curie('comment'),
                   model_uri=CWE.comment, domain=None, range=Optional[str])

slots.abstraction = Slot(uri=SKOS.broader, name="abstraction", curie=SKOS.curie('broader'),
                   model_uri=CWE.abstraction, domain=None, range=Optional[Union[str, "WeaknessAbstraction"]])

slots.structure = Slot(uri=CWE.structure, name="structure", curie=CWE.curie('structure'),
                   model_uri=CWE.structure, domain=None, range=Optional[Union[str, "WeaknessStructure"]])

slots.status = Slot(uri=CWE.status, name="status", curie=CWE.curie('status'),
                   model_uri=CWE.status, domain=None, range=Optional[Union[str, "WeaknessStatus"]])

slots.diagram = Slot(uri=CWE.diagram, name="diagram", curie=CWE.curie('diagram'),
                   model_uri=CWE.diagram, domain=None, range=Optional[str])

slots.extended_description = Slot(uri=CWE.extended_description, name="extended_description", curie=CWE.curie('extended_description'),
                   model_uri=CWE.extended_description, domain=None, range=Optional[str])

slots.likelihood_of_exploit = Slot(uri=CWE.likelihood_of_exploit, name="likelihood_of_exploit", curie=CWE.curie('likelihood_of_exploit'),
                   model_uri=CWE.likelihood_of_exploit, domain=None, range=Optional[Union[str, "LikelihoodLevel"]])

slots.tags = Slot(uri=CWE.tags, name="tags", curie=CWE.curie('tags'),
                   model_uri=CWE.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.type = Slot(uri=CWE.type, name="type", curie=CWE.curie('type'),
                   model_uri=CWE.type, domain=None, range=Optional[str])

slots.phase = Slot(uri=CWE.phase, name="phase", curie=CWE.curie('phase'),
                   model_uri=CWE.phase, domain=None, range=Optional[Union[str, "LifecyclePhase"]])

slots.phases = Slot(uri=CWE.phases, name="phases", curie=CWE.curie('phases'),
                   model_uri=CWE.phases, domain=None, range=Optional[Union[Union[str, "LifecyclePhase"], list[Union[str, "LifecyclePhase"]]]])

slots.strategy = Slot(uri=CWE.strategy, name="strategy", curie=CWE.curie('strategy'),
                   model_uri=CWE.strategy, domain=None, range=Optional[Union[str, "MitigationStrategy"]])

slots.effectiveness = Slot(uri=CWE.effectiveness, name="effectiveness", curie=CWE.curie('effectiveness'),
                   model_uri=CWE.effectiveness, domain=None, range=Optional[str])

slots.effectiveness_notes = Slot(uri=CWE.effectiveness_notes, name="effectiveness_notes", curie=CWE.curie('effectiveness_notes'),
                   model_uri=CWE.effectiveness_notes, domain=None, range=Optional[str])

slots.method = Slot(uri=CWE.method, name="method", curie=CWE.curie('method'),
                   model_uri=CWE.method, domain=None, range=Optional[str])

slots.usage = Slot(uri=CWE.usage, name="usage", curie=CWE.curie('usage'),
                   model_uri=CWE.usage, domain=None, range=Optional[Union[str, "MappingUsage"]])

slots.rationale = Slot(uri=CWE.rationale, name="rationale", curie=CWE.curie('rationale'),
                   model_uri=CWE.rationale, domain=None, range=Optional[str])

slots.comments = Slot(uri=CWE.comments, name="comments", curie=CWE.curie('comments'),
                   model_uri=CWE.comments, domain=None, range=Optional[str])

slots.reasons = Slot(uri=CWE.reasons, name="reasons", curie=CWE.curie('reasons'),
                   model_uri=CWE.reasons, domain=None, range=Optional[Union[Union[str, "MappingReason"], list[Union[str, "MappingReason"]]]])

slots.ordinality = Slot(uri=CWE.ordinality, name="ordinality", curie=CWE.curie('ordinality'),
                   model_uri=CWE.ordinality, domain=None, range=Optional[Union[str, "WeaknessOrdinalityLevel"]])

slots.nature = Slot(uri=SKOS.related, name="nature", curie=SKOS.curie('related'),
                   model_uri=CWE.nature, domain=None, range=Optional[str])

slots.class_ = Slot(uri=CWE.class_, name="class_", curie=CWE.curie('class_'),
                   model_uri=CWE.class_, domain=None, range=Optional[str])

slots.prevalence = Slot(uri=CWE.prevalence, name="prevalence", curie=CWE.curie('prevalence'),
                   model_uri=CWE.prevalence, domain=None, range=Optional[Union[str, "PlatformPrevalence"]])

slots.language = Slot(uri=CWE.language, name="language", curie=CWE.curie('language'),
                   model_uri=CWE.language, domain=None, range=Optional[Union[str, "ProgrammingLanguage"]])

slots.cpe_id = Slot(uri=CWE.cpe_id, name="cpe_id", curie=CWE.curie('cpe_id'),
                   model_uri=CWE.cpe_id, domain=None, range=Optional[str])

slots.cwe_id = Slot(uri=CWE.cwe_id, name="cwe_id", curie=CWE.curie('cwe_id'),
                   model_uri=CWE.cwe_id, domain=None, range=Optional[int])

slots.view_id = Slot(uri=CWE.view_id, name="view_id", curie=CWE.curie('view_id'),
                   model_uri=CWE.view_id, domain=None, range=Optional[int])

slots.chain_id = Slot(uri=CWE.chain_id, name="chain_id", curie=CWE.curie('chain_id'),
                   model_uri=CWE.chain_id, domain=None, range=Optional[int])

slots.ordinal = Slot(uri=CWE.ordinal, name="ordinal", curie=CWE.curie('ordinal'),
                   model_uri=CWE.ordinal, domain=None, range=Optional[Union[str, "OrdinalQualifier"]])

slots.scopes = Slot(uri=CWE.scopes, name="scopes", curie=CWE.curie('scopes'),
                   model_uri=CWE.scopes, domain=None, range=Optional[Union[Union[str, "SecurityScope"], list[Union[str, "SecurityScope"]]]])

slots.impacts = Slot(uri=CWE.impacts, name="impacts", curie=CWE.curie('impacts'),
                   model_uri=CWE.impacts, domain=None, range=Optional[Union[Union[str, "TechnicalImpact"], list[Union[str, "TechnicalImpact"]]]])

slots.likelihood = Slot(uri=CWE.likelihood, name="likelihood", curie=CWE.curie('likelihood'),
                   model_uri=CWE.likelihood, domain=None, range=Optional[Union[str, "LikelihoodLevel"]])

slots.note = Slot(uri=CWE.note, name="note", curie=CWE.curie('note'),
                   model_uri=CWE.note, domain=None, range=Optional[str])

slots.content = Slot(uri=CWE.content, name="content", curie=CWE.curie('content'),
                   model_uri=CWE.content, domain=None, range=Optional[str])

slots.term = Slot(uri=CWE.term, name="term", curie=CWE.curie('term'),
                   model_uri=CWE.term, domain=None, range=Optional[str])

slots.detection_method_id = Slot(uri=CWE.detection_method_id, name="detection_method_id", curie=CWE.curie('detection_method_id'),
                   model_uri=CWE.detection_method_id, domain=None, range=Optional[str])

slots.mitigation_id = Slot(uri=CWE.mitigation_id, name="mitigation_id", curie=CWE.curie('mitigation_id'),
                   model_uri=CWE.mitigation_id, domain=None, range=Optional[str])

slots.demonstrative_example_id = Slot(uri=CWE.demonstrative_example_id, name="demonstrative_example_id", curie=CWE.curie('demonstrative_example_id'),
                   model_uri=CWE.demonstrative_example_id, domain=None, range=Optional[str])

slots.title_text = Slot(uri=CWE.title_text, name="title_text", curie=CWE.curie('title_text'),
                   model_uri=CWE.title_text, domain=None, range=Optional[str])

slots.intro_text = Slot(uri=CWE.intro_text, name="intro_text", curie=CWE.curie('intro_text'),
                   model_uri=CWE.intro_text, domain=None, range=Optional[str])

slots.body_texts = Slot(uri=CWE.body_texts, name="body_texts", curie=CWE.curie('body_texts'),
                   model_uri=CWE.body_texts, domain=None, range=Optional[Union[str, list[str]]])

slots.reference = Slot(uri=CWE.reference, name="reference", curie=CWE.curie('reference'),
                   model_uri=CWE.reference, domain=None, range=Optional[str])

slots.link = Slot(uri=CWE.link, name="link", curie=CWE.curie('link'),
                   model_uri=CWE.link, domain=None, range=Optional[Union[str, URI]])

slots.taxonomy_name = Slot(uri=CWE.taxonomy_name, name="taxonomy_name", curie=CWE.curie('taxonomy_name'),
                   model_uri=CWE.taxonomy_name, domain=None, range=Optional[Union[str, "TaxonomyName"]])

slots.entry_id = Slot(uri=CWE.entry_id, name="entry_id", curie=CWE.curie('entry_id'),
                   model_uri=CWE.entry_id, domain=None, range=Optional[str])

slots.entry_name = Slot(uri=CWE.entry_name, name="entry_name", curie=CWE.curie('entry_name'),
                   model_uri=CWE.entry_name, domain=None, range=Optional[str])

slots.mapping_fit = Slot(uri=CWE.mapping_fit, name="mapping_fit", curie=CWE.curie('mapping_fit'),
                   model_uri=CWE.mapping_fit, domain=None, range=Optional[Union[str, "TaxonomyMappingFit"]])

slots.related_attack_patterns = Slot(uri=SKOS.related, name="related_attack_patterns", curie=SKOS.curie('related'),
                   model_uri=CWE.related_attack_patterns, domain=None, range=Optional[Union[int, list[int]]])

slots.functional_areas = Slot(uri=CWE.functional_areas, name="functional_areas", curie=CWE.curie('functional_areas'),
                   model_uri=CWE.functional_areas, domain=None, range=Optional[Union[Union[str, "FunctionalArea"], list[Union[str, "FunctionalArea"]]]])

slots.affected_resources = Slot(uri=CWE.affected_resources, name="affected_resources", curie=CWE.curie('affected_resources'),
                   model_uri=CWE.affected_resources, domain=None, range=Optional[Union[Union[str, "AffectedResource"], list[Union[str, "AffectedResource"]]]])

slots.background_details = Slot(uri=CWE.background_details, name="background_details", curie=CWE.curie('background_details'),
                   model_uri=CWE.background_details, domain=None, range=Optional[Union[str, list[str]]])

slots.exploitation_factors = Slot(uri=CWE.exploitation_factors, name="exploitation_factors", curie=CWE.curie('exploitation_factors'),
                   model_uri=CWE.exploitation_factors, domain=None, range=Optional[Union[str, list[str]]])

slots.reference_id = Slot(uri=DCT.identifier, name="reference_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.reference_id, domain=None, range=URIRef)

slots.authors = Slot(uri=CWE.authors, name="authors", curie=CWE.curie('authors'),
                   model_uri=CWE.authors, domain=None, range=Optional[Union[str, list[str]]])

slots.edition = Slot(uri=CWE.edition, name="edition", curie=CWE.curie('edition'),
                   model_uri=CWE.edition, domain=None, range=Optional[str])

slots.publication = Slot(uri=CWE.publication, name="publication", curie=CWE.curie('publication'),
                   model_uri=CWE.publication, domain=None, range=Optional[str])

slots.publication_year = Slot(uri=CWE.publication_year, name="publication_year", curie=CWE.curie('publication_year'),
                   model_uri=CWE.publication_year, domain=None, range=Optional[str])

slots.publication_month = Slot(uri=CWE.publication_month, name="publication_month", curie=CWE.curie('publication_month'),
                   model_uri=CWE.publication_month, domain=None, range=Optional[str])

slots.publication_day = Slot(uri=CWE.publication_day, name="publication_day", curie=CWE.curie('publication_day'),
                   model_uri=CWE.publication_day, domain=None, range=Optional[str])

slots.publisher = Slot(uri=CWE.publisher, name="publisher", curie=CWE.curie('publisher'),
                   model_uri=CWE.publisher, domain=None, range=Optional[str])

slots.external_reference_id = Slot(uri=CWE.external_reference_id, name="external_reference_id", curie=CWE.curie('external_reference_id'),
                   model_uri=CWE.external_reference_id, domain=None, range=Optional[str])

slots.section = Slot(uri=CWE.section, name="section", curie=CWE.curie('section'),
                   model_uri=CWE.section, domain=None, range=Optional[str])

slots.consequence_id = Slot(uri=CWE.consequence_id, name="consequence_id", curie=CWE.curie('consequence_id'),
                   model_uri=CWE.consequence_id, domain=None, range=Optional[str])

slots.submission_name = Slot(uri=CWE.submission_name, name="submission_name", curie=CWE.curie('submission_name'),
                   model_uri=CWE.submission_name, domain=None, range=Optional[str])

slots.submission_organization = Slot(uri=CWE.submission_organization, name="submission_organization", curie=CWE.curie('submission_organization'),
                   model_uri=CWE.submission_organization, domain=None, range=Optional[str])

slots.submission_date = Slot(uri=CWE.submission_date, name="submission_date", curie=CWE.curie('submission_date'),
                   model_uri=CWE.submission_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.submission_version = Slot(uri=CWE.submission_version, name="submission_version", curie=CWE.curie('submission_version'),
                   model_uri=CWE.submission_version, domain=None, range=Optional[str])

slots.submission_release_date = Slot(uri=CWE.submission_release_date, name="submission_release_date", curie=CWE.curie('submission_release_date'),
                   model_uri=CWE.submission_release_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.submission_comment = Slot(uri=CWE.submission_comment, name="submission_comment", curie=CWE.curie('submission_comment'),
                   model_uri=CWE.submission_comment, domain=None, range=Optional[str])

slots.modification_name = Slot(uri=CWE.modification_name, name="modification_name", curie=CWE.curie('modification_name'),
                   model_uri=CWE.modification_name, domain=None, range=Optional[str])

slots.modification_organization = Slot(uri=CWE.modification_organization, name="modification_organization", curie=CWE.curie('modification_organization'),
                   model_uri=CWE.modification_organization, domain=None, range=Optional[str])

slots.modification_date = Slot(uri=CWE.modification_date, name="modification_date", curie=CWE.curie('modification_date'),
                   model_uri=CWE.modification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modification_version = Slot(uri=CWE.modification_version, name="modification_version", curie=CWE.curie('modification_version'),
                   model_uri=CWE.modification_version, domain=None, range=Optional[str])

slots.modification_release_date = Slot(uri=CWE.modification_release_date, name="modification_release_date", curie=CWE.curie('modification_release_date'),
                   model_uri=CWE.modification_release_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modification_importance = Slot(uri=CWE.modification_importance, name="modification_importance", curie=CWE.curie('modification_importance'),
                   model_uri=CWE.modification_importance, domain=None, range=Optional[Union[str, "ContentImportance"]])

slots.modification_comment = Slot(uri=CWE.modification_comment, name="modification_comment", curie=CWE.curie('modification_comment'),
                   model_uri=CWE.modification_comment, domain=None, range=Optional[str])

slots.contribution_name = Slot(uri=CWE.contribution_name, name="contribution_name", curie=CWE.curie('contribution_name'),
                   model_uri=CWE.contribution_name, domain=None, range=Optional[str])

slots.contribution_organization = Slot(uri=CWE.contribution_organization, name="contribution_organization", curie=CWE.curie('contribution_organization'),
                   model_uri=CWE.contribution_organization, domain=None, range=Optional[str])

slots.contribution_date = Slot(uri=CWE.contribution_date, name="contribution_date", curie=CWE.curie('contribution_date'),
                   model_uri=CWE.contribution_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.contribution_version = Slot(uri=CWE.contribution_version, name="contribution_version", curie=CWE.curie('contribution_version'),
                   model_uri=CWE.contribution_version, domain=None, range=Optional[str])

slots.contribution_release_date = Slot(uri=CWE.contribution_release_date, name="contribution_release_date", curie=CWE.curie('contribution_release_date'),
                   model_uri=CWE.contribution_release_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.contribution_comment = Slot(uri=CWE.contribution_comment, name="contribution_comment", curie=CWE.curie('contribution_comment'),
                   model_uri=CWE.contribution_comment, domain=None, range=Optional[str])

slots.observation_id = Slot(uri=DCT.identifier, name="observation_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.observation_id, domain=None, range=URIRef)

slots.observed_in_cve = Slot(uri=DCT.references, name="observed_in_cve", curie=DCT.curie('references'),
                   model_uri=CWE.observed_in_cve, domain=None, range=Optional[str])

slots.weakness = Slot(uri=SCHEMA.about, name="weakness", curie=SCHEMA.curie('about'),
                   model_uri=CWE.weakness, domain=None, range=Optional[Union[int, WeaknessId]])

slots.reported_by = Slot(uri=DCT.source, name="reported_by", curie=DCT.curie('source'),
                   model_uri=CWE.reported_by, domain=None, range=Optional[Union[str, "WeaknessSource"]])

slots.weaknesses = Slot(uri=CWE.weaknesses, name="weaknesses", curie=CWE.curie('weaknesses'),
                   model_uri=CWE.weaknesses, domain=None, range=Optional[Union[dict[Union[int, WeaknessId], Union[dict, Weakness]], list[Union[dict, Weakness]]]])

slots.categories = Slot(uri=CWE.categories, name="categories", curie=CWE.curie('categories'),
                   model_uri=CWE.categories, domain=None, range=Optional[Union[dict[Union[int, CategoryId], Union[dict, Category]], list[Union[dict, Category]]]])

slots.views = Slot(uri=CWE.views, name="views", curie=CWE.curie('views'),
                   model_uri=CWE.views, domain=None, range=Optional[Union[dict[Union[int, ViewId], Union[dict, View]], list[Union[dict, View]]]])

slots.external_references = Slot(uri=CWE.external_references, name="external_references", curie=CWE.curie('external_references'),
                   model_uri=CWE.external_references, domain=None, range=Optional[Union[dict[Union[str, ExternalReferenceReferenceId], Union[dict, ExternalReference]], list[Union[dict, ExternalReference]]]])

slots.observations = Slot(uri=CWE.observations, name="observations", curie=CWE.curie('observations'),
                   model_uri=CWE.observations, domain=None, range=Optional[Union[dict[Union[str, NVDWeaknessObservationObservationId], Union[dict, NVDWeaknessObservation]], list[Union[dict, NVDWeaknessObservation]]]])

slots.weakness_ordinalities = Slot(uri=CWE.weakness_ordinalities, name="weakness_ordinalities", curie=CWE.curie('weakness_ordinalities'),
                   model_uri=CWE.weakness_ordinalities, domain=None, range=Optional[Union[Union[dict, WeaknessOrdinality], list[Union[dict, WeaknessOrdinality]]]])

slots.applicable_platforms = Slot(uri=CWE.applicable_platforms, name="applicable_platforms", curie=CWE.curie('applicable_platforms'),
                   model_uri=CWE.applicable_platforms, domain=None, range=Optional[Union[dict, ApplicablePlatforms]])

slots.languages = Slot(uri=CWE.languages, name="languages", curie=CWE.curie('languages'),
                   model_uri=CWE.languages, domain=None, range=Optional[Union[Union[dict, LanguagePlatform], list[Union[dict, LanguagePlatform]]]])

slots.operating_systems = Slot(uri=CWE.operating_systems, name="operating_systems", curie=CWE.curie('operating_systems'),
                   model_uri=CWE.operating_systems, domain=None, range=Optional[Union[Union[dict, OSPlatform], list[Union[dict, OSPlatform]]]])

slots.architectures = Slot(uri=CWE.architectures, name="architectures", curie=CWE.curie('architectures'),
                   model_uri=CWE.architectures, domain=None, range=Optional[Union[Union[dict, ArchitecturePlatform], list[Union[dict, ArchitecturePlatform]]]])

slots.technologies = Slot(uri=CWE.technologies, name="technologies", curie=CWE.curie('technologies'),
                   model_uri=CWE.technologies, domain=None, range=Optional[Union[Union[dict, TechnologyPlatform], list[Union[dict, TechnologyPlatform]]]])

slots.alternate_terms = Slot(uri=CWE.alternate_terms, name="alternate_terms", curie=CWE.curie('alternate_terms'),
                   model_uri=CWE.alternate_terms, domain=None, range=Optional[Union[Union[dict, AlternateTerm], list[Union[dict, AlternateTerm]]]])

slots.modes_of_introduction = Slot(uri=CWE.modes_of_introduction, name="modes_of_introduction", curie=CWE.curie('modes_of_introduction'),
                   model_uri=CWE.modes_of_introduction, domain=None, range=Optional[Union[Union[dict, ModeOfIntroduction], list[Union[dict, ModeOfIntroduction]]]])

slots.common_consequences = Slot(uri=CWE.common_consequences, name="common_consequences", curie=CWE.curie('common_consequences'),
                   model_uri=CWE.common_consequences, domain=None, range=Optional[Union[Union[dict, CommonConsequence], list[Union[dict, CommonConsequence]]]])

slots.detection_methods = Slot(uri=CWE.detection_methods, name="detection_methods", curie=CWE.curie('detection_methods'),
                   model_uri=CWE.detection_methods, domain=None, range=Optional[Union[Union[dict, DetectionMethod], list[Union[dict, DetectionMethod]]]])

slots.potential_mitigations = Slot(uri=CWE.potential_mitigations, name="potential_mitigations", curie=CWE.curie('potential_mitigations'),
                   model_uri=CWE.potential_mitigations, domain=None, range=Optional[Union[Union[dict, PotentialMitigation], list[Union[dict, PotentialMitigation]]]])

slots.demonstrative_examples = Slot(uri=CWE.demonstrative_examples, name="demonstrative_examples", curie=CWE.curie('demonstrative_examples'),
                   model_uri=CWE.demonstrative_examples, domain=None, range=Optional[Union[Union[dict, DemonstrativeExample], list[Union[dict, DemonstrativeExample]]]])

slots.example_codes = Slot(uri=CWE.example_codes, name="example_codes", curie=CWE.curie('example_codes'),
                   model_uri=CWE.example_codes, domain=None, range=Optional[Union[Union[dict, ExampleCode], list[Union[dict, ExampleCode]]]])

slots.observed_examples = Slot(uri=CWE.observed_examples, name="observed_examples", curie=CWE.curie('observed_examples'),
                   model_uri=CWE.observed_examples, domain=None, range=Optional[Union[Union[dict, ObservedExample], list[Union[dict, ObservedExample]]]])

slots.taxonomy_mappings = Slot(uri=CWE.taxonomy_mappings, name="taxonomy_mappings", curie=CWE.curie('taxonomy_mappings'),
                   model_uri=CWE.taxonomy_mappings, domain=None, range=Optional[Union[Union[dict, TaxonomyMapping], list[Union[dict, TaxonomyMapping]]]])

slots.related_weaknesses = Slot(uri=CWE.related_weaknesses, name="related_weaknesses", curie=CWE.curie('related_weaknesses'),
                   model_uri=CWE.related_weaknesses, domain=None, range=Optional[Union[Union[dict, RelatedWeakness], list[Union[dict, RelatedWeakness]]]])

slots.references = Slot(uri=CWE.references, name="references", curie=CWE.curie('references'),
                   model_uri=CWE.references, domain=None, range=Optional[Union[Union[dict, CWEReference], list[Union[dict, CWEReference]]]])

slots.mapping_notes = Slot(uri=CWE.mapping_notes, name="mapping_notes", curie=CWE.curie('mapping_notes'),
                   model_uri=CWE.mapping_notes, domain=None, range=Optional[Union[dict, MappingNotes]])

slots.suggestions = Slot(uri=CWE.suggestions, name="suggestions", curie=CWE.curie('suggestions'),
                   model_uri=CWE.suggestions, domain=None, range=Optional[Union[Union[dict, MappingSuggestion], list[Union[dict, MappingSuggestion]]]])

slots.notes = Slot(uri=SKOS.note, name="notes", curie=SKOS.curie('note'),
                   model_uri=CWE.notes, domain=None, range=Optional[Union[Union[dict, Note], list[Union[dict, Note]]]])

slots.content_history = Slot(uri=CWE.content_history, name="content_history", curie=CWE.curie('content_history'),
                   model_uri=CWE.content_history, domain=None, range=Optional[Union[dict, ContentHistory]])

slots.submission = Slot(uri=CWE.submission, name="submission", curie=CWE.curie('submission'),
                   model_uri=CWE.submission, domain=None, range=Optional[Union[dict, Submission]])

slots.modifications = Slot(uri=CWE.modifications, name="modifications", curie=CWE.curie('modifications'),
                   model_uri=CWE.modifications, domain=None, range=Optional[Union[Union[dict, Modification], list[Union[dict, Modification]]]])

slots.contributions = Slot(uri=CWE.contributions, name="contributions", curie=CWE.curie('contributions'),
                   model_uri=CWE.contributions, domain=None, range=Optional[Union[Union[dict, Contribution], list[Union[dict, Contribution]]]])

slots.previous_entry_names = Slot(uri=CWE.previous_entry_names, name="previous_entry_names", curie=CWE.curie('previous_entry_names'),
                   model_uri=CWE.previous_entry_names, domain=None, range=Optional[Union[Union[dict, PreviousEntryName], list[Union[dict, PreviousEntryName]]]])

slots.members = Slot(uri=CWE.members, name="members", curie=CWE.curie('members'),
                   model_uri=CWE.members, domain=None, range=Optional[Union[Union[dict, CatalogMember], list[Union[dict, CatalogMember]]]])

slots.has_member = Slot(uri=CWE.has_member, name="has_member", curie=CWE.curie('has_member'),
                   model_uri=CWE.has_member, domain=None, range=Optional[Union[Union[dict, CatalogMember], list[Union[dict, CatalogMember]]]])

slots.member_of = Slot(uri=CWE.member_of, name="member_of", curie=CWE.curie('member_of'),
                   model_uri=CWE.member_of, domain=None, range=Optional[Union[Union[dict, CatalogMember], list[Union[dict, CatalogMember]]]])

slots.relationships = Slot(uri=CWE.relationships, name="relationships", curie=CWE.curie('relationships'),
                   model_uri=CWE.relationships, domain=None, range=Optional[Union[dict, Relationship]])

slots.audience = Slot(uri=CWE.audience, name="audience", curie=CWE.curie('audience'),
                   model_uri=CWE.audience, domain=None, range=Optional[Union[Union[dict, Audience], list[Union[dict, Audience]]]])

slots.WeaknessCatalog_name = Slot(uri=RDFS.label, name="WeaknessCatalog_name", curie=RDFS.curie('label'),
                   model_uri=CWE.WeaknessCatalog_name, domain=WeaknessCatalog, range=Union[str, WeaknessCatalogName])

slots.WeaknessCatalog_version = Slot(uri=SCHEMA.version, name="WeaknessCatalog_version", curie=SCHEMA.curie('version'),
                   model_uri=CWE.WeaknessCatalog_version, domain=WeaknessCatalog, range=str)

slots.WeaknessCatalog_date = Slot(uri=DCT.date, name="WeaknessCatalog_date", curie=DCT.curie('date'),
                   model_uri=CWE.WeaknessCatalog_date, domain=WeaknessCatalog, range=Union[str, XSDDate])

slots.Weakness_id = Slot(uri=DCT.identifier, name="Weakness_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.Weakness_id, domain=Weakness, range=Union[int, WeaknessId])

slots.Weakness_name = Slot(uri=RDFS.label, name="Weakness_name", curie=RDFS.curie('label'),
                   model_uri=CWE.Weakness_name, domain=Weakness, range=str)

slots.Weakness_description = Slot(uri=DCT.description, name="Weakness_description", curie=DCT.curie('description'),
                   model_uri=CWE.Weakness_description, domain=Weakness, range=str)

slots.Weakness_abstraction = Slot(uri=SKOS.broader, name="Weakness_abstraction", curie=SKOS.curie('broader'),
                   model_uri=CWE.Weakness_abstraction, domain=Weakness, range=Union[str, "WeaknessAbstraction"])

slots.Weakness_structure = Slot(uri=CWE.structure, name="Weakness_structure", curie=CWE.curie('structure'),
                   model_uri=CWE.Weakness_structure, domain=Weakness, range=Union[str, "WeaknessStructure"])

slots.Weakness_status = Slot(uri=CWE.status, name="Weakness_status", curie=CWE.curie('status'),
                   model_uri=CWE.Weakness_status, domain=Weakness, range=Union[str, "WeaknessStatus"])

slots.Weakness_mapping_notes = Slot(uri=CWE.mapping_notes, name="Weakness_mapping_notes", curie=CWE.curie('mapping_notes'),
                   model_uri=CWE.Weakness_mapping_notes, domain=Weakness, range=Union[dict, "MappingNotes"])

slots.Weakness_content_history = Slot(uri=CWE.content_history, name="Weakness_content_history", curie=CWE.curie('content_history'),
                   model_uri=CWE.Weakness_content_history, domain=Weakness, range=Union[dict, "ContentHistory"])

slots.Category_id = Slot(uri=DCT.identifier, name="Category_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.Category_id, domain=Category, range=Union[int, CategoryId])

slots.Category_name = Slot(uri=RDFS.label, name="Category_name", curie=RDFS.curie('label'),
                   model_uri=CWE.Category_name, domain=Category, range=str)

slots.Category_status = Slot(uri=CWE.status, name="Category_status", curie=CWE.curie('status'),
                   model_uri=CWE.Category_status, domain=Category, range=Union[str, "WeaknessStatus"])

slots.Category_summary = Slot(uri=CWE.summary, name="Category_summary", curie=CWE.curie('summary'),
                   model_uri=CWE.Category_summary, domain=Category, range=str)

slots.Category_mapping_notes = Slot(uri=CWE.mapping_notes, name="Category_mapping_notes", curie=CWE.curie('mapping_notes'),
                   model_uri=CWE.Category_mapping_notes, domain=Category, range=Union[dict, "MappingNotes"])

slots.Category_content_history = Slot(uri=CWE.content_history, name="Category_content_history", curie=CWE.curie('content_history'),
                   model_uri=CWE.Category_content_history, domain=Category, range=Union[dict, "ContentHistory"])

slots.View_id = Slot(uri=DCT.identifier, name="View_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.View_id, domain=View, range=Union[int, ViewId])

slots.View_name = Slot(uri=RDFS.label, name="View_name", curie=RDFS.curie('label'),
                   model_uri=CWE.View_name, domain=View, range=str)

slots.View_status = Slot(uri=CWE.status, name="View_status", curie=CWE.curie('status'),
                   model_uri=CWE.View_status, domain=View, range=Union[str, "WeaknessStatus"])

slots.View_objective = Slot(uri=CWE.objective, name="View_objective", curie=CWE.curie('objective'),
                   model_uri=CWE.View_objective, domain=View, range=str)

slots.View_mapping_notes = Slot(uri=CWE.mapping_notes, name="View_mapping_notes", curie=CWE.curie('mapping_notes'),
                   model_uri=CWE.View_mapping_notes, domain=View, range=Union[dict, "MappingNotes"])

slots.View_content_history = Slot(uri=CWE.content_history, name="View_content_history", curie=CWE.curie('content_history'),
                   model_uri=CWE.View_content_history, domain=View, range=Union[dict, "ContentHistory"])

slots.View_type = Slot(uri=CWE.type, name="View_type", curie=CWE.curie('type'),
                   model_uri=CWE.View_type, domain=View, range=Union[str, "CWEViewType"])

slots.ExternalReference_reference_id = Slot(uri=DCT.identifier, name="ExternalReference_reference_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.ExternalReference_reference_id, domain=ExternalReference, range=Union[str, ExternalReferenceReferenceId])

slots.ExternalReference_title = Slot(uri=DCT.title, name="ExternalReference_title", curie=DCT.curie('title'),
                   model_uri=CWE.ExternalReference_title, domain=ExternalReference, range=str)

slots.CWEReference_external_reference_id = Slot(uri=CWE.external_reference_id, name="CWEReference_external_reference_id", curie=CWE.curie('external_reference_id'),
                   model_uri=CWE.CWEReference_external_reference_id, domain=CWEReference, range=str)

slots.RelatedWeakness_nature = Slot(uri=SKOS.related, name="RelatedWeakness_nature", curie=SKOS.curie('related'),
                   model_uri=CWE.RelatedWeakness_nature, domain=RelatedWeakness, range=Union[str, "WeaknessRelationNature"])

slots.RelatedWeakness_cwe_id = Slot(uri=CWE.cwe_id, name="RelatedWeakness_cwe_id", curie=CWE.curie('cwe_id'),
                   model_uri=CWE.RelatedWeakness_cwe_id, domain=RelatedWeakness, range=int)

slots.RelatedWeakness_view_id = Slot(uri=CWE.view_id, name="RelatedWeakness_view_id", curie=CWE.curie('view_id'),
                   model_uri=CWE.RelatedWeakness_view_id, domain=RelatedWeakness, range=int)

slots.RelatedWeakness_chain_id = Slot(uri=CWE.chain_id, name="RelatedWeakness_chain_id", curie=CWE.curie('chain_id'),
                   model_uri=CWE.RelatedWeakness_chain_id, domain=RelatedWeakness, range=Optional[int])

slots.RelatedWeakness_ordinal = Slot(uri=CWE.ordinal, name="RelatedWeakness_ordinal", curie=CWE.curie('ordinal'),
                   model_uri=CWE.RelatedWeakness_ordinal, domain=RelatedWeakness, range=Optional[Union[str, "OrdinalQualifier"]])

slots.WeaknessOrdinality_ordinality = Slot(uri=CWE.ordinality, name="WeaknessOrdinality_ordinality", curie=CWE.curie('ordinality'),
                   model_uri=CWE.WeaknessOrdinality_ordinality, domain=WeaknessOrdinality, range=Union[str, "WeaknessOrdinalityLevel"])

slots.WeaknessOrdinality_description = Slot(uri=DCT.description, name="WeaknessOrdinality_description", curie=DCT.curie('description'),
                   model_uri=CWE.WeaknessOrdinality_description, domain=WeaknessOrdinality, range=Optional[str])

slots.LanguagePlatform_name = Slot(uri=RDFS.label, name="LanguagePlatform_name", curie=RDFS.curie('label'),
                   model_uri=CWE.LanguagePlatform_name, domain=LanguagePlatform, range=Optional[Union[str, "ProgrammingLanguage"]])

slots.LanguagePlatform_class_ = Slot(uri=CWE.class_, name="LanguagePlatform_class_", curie=CWE.curie('class_'),
                   model_uri=CWE.LanguagePlatform_class_, domain=LanguagePlatform, range=Optional[Union[str, "LanguageClass"]])

slots.LanguagePlatform_prevalence = Slot(uri=CWE.prevalence, name="LanguagePlatform_prevalence", curie=CWE.curie('prevalence'),
                   model_uri=CWE.LanguagePlatform_prevalence, domain=LanguagePlatform, range=Union[str, "PlatformPrevalence"])

slots.OSPlatform_name = Slot(uri=RDFS.label, name="OSPlatform_name", curie=RDFS.curie('label'),
                   model_uri=CWE.OSPlatform_name, domain=OSPlatform, range=Optional[Union[str, "OperatingSystemName"]])

slots.OSPlatform_class_ = Slot(uri=CWE.class_, name="OSPlatform_class_", curie=CWE.curie('class_'),
                   model_uri=CWE.OSPlatform_class_, domain=OSPlatform, range=Optional[Union[str, "OperatingSystemClass"]])

slots.OSPlatform_version = Slot(uri=SCHEMA.version, name="OSPlatform_version", curie=SCHEMA.curie('version'),
                   model_uri=CWE.OSPlatform_version, domain=OSPlatform, range=Optional[str])

slots.OSPlatform_cpe_id = Slot(uri=CWE.cpe_id, name="OSPlatform_cpe_id", curie=CWE.curie('cpe_id'),
                   model_uri=CWE.OSPlatform_cpe_id, domain=OSPlatform, range=Optional[str])

slots.OSPlatform_prevalence = Slot(uri=CWE.prevalence, name="OSPlatform_prevalence", curie=CWE.curie('prevalence'),
                   model_uri=CWE.OSPlatform_prevalence, domain=OSPlatform, range=Union[str, "PlatformPrevalence"])

slots.ArchitecturePlatform_name = Slot(uri=RDFS.label, name="ArchitecturePlatform_name", curie=RDFS.curie('label'),
                   model_uri=CWE.ArchitecturePlatform_name, domain=ArchitecturePlatform, range=Optional[Union[str, "ArchitectureName"]])

slots.ArchitecturePlatform_class_ = Slot(uri=CWE.class_, name="ArchitecturePlatform_class_", curie=CWE.curie('class_'),
                   model_uri=CWE.ArchitecturePlatform_class_, domain=ArchitecturePlatform, range=Optional[Union[str, "ArchitectureClass"]])

slots.ArchitecturePlatform_prevalence = Slot(uri=CWE.prevalence, name="ArchitecturePlatform_prevalence", curie=CWE.curie('prevalence'),
                   model_uri=CWE.ArchitecturePlatform_prevalence, domain=ArchitecturePlatform, range=Union[str, "PlatformPrevalence"])

slots.TechnologyPlatform_name = Slot(uri=RDFS.label, name="TechnologyPlatform_name", curie=RDFS.curie('label'),
                   model_uri=CWE.TechnologyPlatform_name, domain=TechnologyPlatform, range=Optional[Union[str, "TechnologyName"]])

slots.TechnologyPlatform_class_ = Slot(uri=CWE.class_, name="TechnologyPlatform_class_", curie=CWE.curie('class_'),
                   model_uri=CWE.TechnologyPlatform_class_, domain=TechnologyPlatform, range=Optional[Union[str, "TechnologyClass"]])

slots.TechnologyPlatform_prevalence = Slot(uri=CWE.prevalence, name="TechnologyPlatform_prevalence", curie=CWE.curie('prevalence'),
                   model_uri=CWE.TechnologyPlatform_prevalence, domain=TechnologyPlatform, range=Union[str, "PlatformPrevalence"])

slots.AlternateTerm_term = Slot(uri=CWE.term, name="AlternateTerm_term", curie=CWE.curie('term'),
                   model_uri=CWE.AlternateTerm_term, domain=AlternateTerm, range=str)

slots.ModeOfIntroduction_phase = Slot(uri=CWE.phase, name="ModeOfIntroduction_phase", curie=CWE.curie('phase'),
                   model_uri=CWE.ModeOfIntroduction_phase, domain=ModeOfIntroduction, range=Union[str, "LifecyclePhase"])

slots.CommonConsequence_scopes = Slot(uri=CWE.scopes, name="CommonConsequence_scopes", curie=CWE.curie('scopes'),
                   model_uri=CWE.CommonConsequence_scopes, domain=CommonConsequence, range=Union[Union[str, "SecurityScope"], list[Union[str, "SecurityScope"]]])

slots.CommonConsequence_impacts = Slot(uri=CWE.impacts, name="CommonConsequence_impacts", curie=CWE.curie('impacts'),
                   model_uri=CWE.CommonConsequence_impacts, domain=CommonConsequence, range=Union[Union[str, "TechnicalImpact"], list[Union[str, "TechnicalImpact"]]])

slots.DetectionMethod_method = Slot(uri=CWE.method, name="DetectionMethod_method", curie=CWE.curie('method'),
                   model_uri=CWE.DetectionMethod_method, domain=DetectionMethod, range=Union[str, "DetectionMethodType"])

slots.DetectionMethod_description = Slot(uri=DCT.description, name="DetectionMethod_description", curie=DCT.curie('description'),
                   model_uri=CWE.DetectionMethod_description, domain=DetectionMethod, range=str)

slots.DetectionMethod_effectiveness = Slot(uri=CWE.effectiveness, name="DetectionMethod_effectiveness", curie=CWE.curie('effectiveness'),
                   model_uri=CWE.DetectionMethod_effectiveness, domain=DetectionMethod, range=Optional[Union[str, "DetectionEffectiveness"]])

slots.PotentialMitigation_description = Slot(uri=DCT.description, name="PotentialMitigation_description", curie=DCT.curie('description'),
                   model_uri=CWE.PotentialMitigation_description, domain=PotentialMitigation, range=str)

slots.PotentialMitigation_effectiveness = Slot(uri=CWE.effectiveness, name="PotentialMitigation_effectiveness", curie=CWE.curie('effectiveness'),
                   model_uri=CWE.PotentialMitigation_effectiveness, domain=PotentialMitigation, range=Optional[Union[str, "MitigationEffectiveness"]])

slots.DemonstrativeExample_intro_text = Slot(uri=CWE.intro_text, name="DemonstrativeExample_intro_text", curie=CWE.curie('intro_text'),
                   model_uri=CWE.DemonstrativeExample_intro_text, domain=DemonstrativeExample, range=str)

slots.ExampleCode_nature = Slot(uri=SKOS.related, name="ExampleCode_nature", curie=SKOS.curie('related'),
                   model_uri=CWE.ExampleCode_nature, domain=ExampleCode, range=Union[str, "CodeNature"])

slots.ExampleCode_language = Slot(uri=CWE.language, name="ExampleCode_language", curie=CWE.curie('language'),
                   model_uri=CWE.ExampleCode_language, domain=ExampleCode, range=Optional[Union[str, "ProgrammingLanguage"]])

slots.ExampleCode_content = Slot(uri=CWE.content, name="ExampleCode_content", curie=CWE.curie('content'),
                   model_uri=CWE.ExampleCode_content, domain=ExampleCode, range=Optional[str])

slots.ObservedExample_reference = Slot(uri=CWE.reference, name="ObservedExample_reference", curie=CWE.curie('reference'),
                   model_uri=CWE.ObservedExample_reference, domain=ObservedExample, range=str)

slots.ObservedExample_description = Slot(uri=DCT.description, name="ObservedExample_description", curie=DCT.curie('description'),
                   model_uri=CWE.ObservedExample_description, domain=ObservedExample, range=str)

slots.ObservedExample_link = Slot(uri=CWE.link, name="ObservedExample_link", curie=CWE.curie('link'),
                   model_uri=CWE.ObservedExample_link, domain=ObservedExample, range=Union[str, URI])

slots.TaxonomyMapping_taxonomy_name = Slot(uri=CWE.taxonomy_name, name="TaxonomyMapping_taxonomy_name", curie=CWE.curie('taxonomy_name'),
                   model_uri=CWE.TaxonomyMapping_taxonomy_name, domain=TaxonomyMapping, range=Union[str, "TaxonomyName"])

slots.CatalogMember_cwe_id = Slot(uri=CWE.cwe_id, name="CatalogMember_cwe_id", curie=CWE.curie('cwe_id'),
                   model_uri=CWE.CatalogMember_cwe_id, domain=CatalogMember, range=int)

slots.CatalogMember_view_id = Slot(uri=CWE.view_id, name="CatalogMember_view_id", curie=CWE.curie('view_id'),
                   model_uri=CWE.CatalogMember_view_id, domain=CatalogMember, range=int)

slots.Audience_type = Slot(uri=CWE.type, name="Audience_type", curie=CWE.curie('type'),
                   model_uri=CWE.Audience_type, domain=Audience, range=Union[str, "StakeholderType"])

slots.MappingNotes_usage = Slot(uri=CWE.usage, name="MappingNotes_usage", curie=CWE.curie('usage'),
                   model_uri=CWE.MappingNotes_usage, domain=MappingNotes, range=Union[str, "MappingUsage"])

slots.MappingNotes_rationale = Slot(uri=CWE.rationale, name="MappingNotes_rationale", curie=CWE.curie('rationale'),
                   model_uri=CWE.MappingNotes_rationale, domain=MappingNotes, range=str)

slots.MappingNotes_comments = Slot(uri=CWE.comments, name="MappingNotes_comments", curie=CWE.curie('comments'),
                   model_uri=CWE.MappingNotes_comments, domain=MappingNotes, range=str)

slots.MappingNotes_reasons = Slot(uri=CWE.reasons, name="MappingNotes_reasons", curie=CWE.curie('reasons'),
                   model_uri=CWE.MappingNotes_reasons, domain=MappingNotes, range=Union[Union[str, "MappingReason"], list[Union[str, "MappingReason"]]])

slots.MappingSuggestion_cwe_id = Slot(uri=CWE.cwe_id, name="MappingSuggestion_cwe_id", curie=CWE.curie('cwe_id'),
                   model_uri=CWE.MappingSuggestion_cwe_id, domain=MappingSuggestion, range=int)

slots.MappingSuggestion_comment = Slot(uri=CWE.comment, name="MappingSuggestion_comment", curie=CWE.curie('comment'),
                   model_uri=CWE.MappingSuggestion_comment, domain=MappingSuggestion, range=str)

slots.Note_type = Slot(uri=CWE.type, name="Note_type", curie=CWE.curie('type'),
                   model_uri=CWE.Note_type, domain=Note, range=Union[str, "NoteType"])

slots.ContentHistory_submission = Slot(uri=CWE.submission, name="ContentHistory_submission", curie=CWE.curie('submission'),
                   model_uri=CWE.ContentHistory_submission, domain=ContentHistory, range=Union[dict, "Submission"])

slots.Submission_submission_date = Slot(uri=CWE.submission_date, name="Submission_submission_date", curie=CWE.curie('submission_date'),
                   model_uri=CWE.Submission_submission_date, domain=Submission, range=Union[str, XSDDate])

slots.Submission_submission_version = Slot(uri=CWE.submission_version, name="Submission_submission_version", curie=CWE.curie('submission_version'),
                   model_uri=CWE.Submission_submission_version, domain=Submission, range=str)

slots.Submission_submission_release_date = Slot(uri=CWE.submission_release_date, name="Submission_submission_release_date", curie=CWE.curie('submission_release_date'),
                   model_uri=CWE.Submission_submission_release_date, domain=Submission, range=Union[str, XSDDate])

slots.Modification_modification_date = Slot(uri=CWE.modification_date, name="Modification_modification_date", curie=CWE.curie('modification_date'),
                   model_uri=CWE.Modification_modification_date, domain=Modification, range=Union[str, XSDDate])

slots.Contribution_contribution_date = Slot(uri=CWE.contribution_date, name="Contribution_contribution_date", curie=CWE.curie('contribution_date'),
                   model_uri=CWE.Contribution_contribution_date, domain=Contribution, range=Union[str, XSDDate])

slots.Contribution_type = Slot(uri=CWE.type, name="Contribution_type", curie=CWE.curie('type'),
                   model_uri=CWE.Contribution_type, domain=Contribution, range=Union[str, "ContributionType"])

slots.PreviousEntryName_name = Slot(uri=RDFS.label, name="PreviousEntryName_name", curie=RDFS.curie('label'),
                   model_uri=CWE.PreviousEntryName_name, domain=PreviousEntryName, range=str)

slots.PreviousEntryName_date = Slot(uri=DCT.date, name="PreviousEntryName_date", curie=DCT.curie('date'),
                   model_uri=CWE.PreviousEntryName_date, domain=PreviousEntryName, range=Union[str, XSDDate])

slots.PreviousEntryName_version = Slot(uri=SCHEMA.version, name="PreviousEntryName_version", curie=SCHEMA.curie('version'),
                   model_uri=CWE.PreviousEntryName_version, domain=PreviousEntryName, range=Optional[str])

slots.NVDWeaknessObservation_observation_id = Slot(uri=DCT.identifier, name="NVDWeaknessObservation_observation_id", curie=DCT.curie('identifier'),
                   model_uri=CWE.NVDWeaknessObservation_observation_id, domain=NVDWeaknessObservation, range=Union[str, NVDWeaknessObservationObservationId])

slots.NVDWeaknessObservation_observed_in_cve = Slot(uri=DCT.references, name="NVDWeaknessObservation_observed_in_cve", curie=DCT.curie('references'),
                   model_uri=CWE.NVDWeaknessObservation_observed_in_cve, domain=NVDWeaknessObservation, range=str)

slots.NVDWeaknessObservation_weakness = Slot(uri=SCHEMA.about, name="NVDWeaknessObservation_weakness", curie=SCHEMA.curie('about'),
                   model_uri=CWE.NVDWeaknessObservation_weakness, domain=NVDWeaknessObservation, range=Union[int, WeaknessId])

slots.NVDWeaknessObservation_reported_by = Slot(uri=DCT.source, name="NVDWeaknessObservation_reported_by", curie=DCT.curie('source'),
                   model_uri=CWE.NVDWeaknessObservation_reported_by, domain=NVDWeaknessObservation, range=Union[str, "WeaknessSource"])
