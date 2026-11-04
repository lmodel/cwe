# Auto generated from cwe.yaml by pythongen.py version: 0.0.1
# Schema: cwe
#
# id: https://w3id.org/lmodel/cwe
# description: A LinkML model of the Common Weakness Enumeration, the catalogue of software and hardware weakness types that The MITRE Corporation publishes for the CWE Program. It renders the catalogue's XML Schema with its own element names and values, so the whole catalogue validates with both unchanged.
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

from linkml_runtime.linkml_model.types import Date, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

metamodel_version = "1.12.0"
version = "5.0"

# Namespaces
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
CWE = CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
KEV_CATALOG = CurieNamespace('kev_catalog', 'https://w3id.org/lmodel/kev-catalog/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_NVD = CurieNamespace('nist_nvd', 'https://w3id.org/lmodel/nist-nvd/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEPSES_CWE = CurieNamespace('sepses_cwe', 'http://w3id.org/sepses/vocab/ref/cwe#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX_CORE = CurieNamespace('spdx_core', 'https://spdx.org/rdf/3.0.1/terms/Core/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
WDT = CurieNamespace('wdt', 'http://www.wikidata.org/prop/direct/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CWE


# Types
class CweEntryId(String):
    """ The number that identifies an entry of the CWE List, written as text, such as 79. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cwe_entry_id"
    type_model_uri = CWE.CweEntryId


class CweCapecId(String):
    """ The number of an attack pattern in the CAPEC list, written as text, such as 63. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cwe_capec_id"
    type_model_uri = CWE.CweCapecId


class CweReferenceId(String):
    """ The identifier of an external reference in the catalogue, such as REF-1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cwe_reference_id"
    type_model_uri = CWE.CweReferenceId


class CweStructuredText(String):
    """ Text that may hold XHTML markup, kept as a well-formed fragment without the namespace prefix and with its special characters escaped. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cwe_structured_text"
    type_model_uri = CWE.CweStructuredText


class CwePublicationYear(String):
    """ A year in XML Schema's form, such as 2021. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "cwe_publication_year"
    type_model_uri = CWE.CwePublicationYear


class CwePublicationMonth(String):
    """ A month in XML Schema's form, two hyphens and two digits, such as --03. """
    type_class_uri = XSD["gMonth"]
    type_class_curie = "xsd:gMonth"
    type_name = "cwe_publication_month"
    type_model_uri = CWE.CwePublicationMonth


class CwePublicationDay(String):
    """ A day of the month in XML Schema's form, three hyphens and two digits, such as ---06. """
    type_class_uri = XSD["gDay"]
    type_class_curie = "xsd:gDay"
    type_name = "cwe_publication_day"
    type_model_uri = CWE.CwePublicationDay


# Class references
class CweExternalReferenceReferenceID(CweReferenceId):
    pass


class CweEntryID(CweEntryId):
    pass


class CweWeaknessID(CweEntryID):
    pass


class CweGroupingID(CweEntryID):
    pass


class CweViewID(CweEntryID):
    pass


@dataclass(repr=False)
class CweWeaknessCatalog(YAMLRoot):
    """
    One release of the CWE List, with all its entries and the sources they cite.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweWeaknessCatalog"]
    class_class_curie: ClassVar[str] = "cwe:CweWeaknessCatalog"
    class_name: ClassVar[str] = "CweWeaknessCatalog"
    class_model_uri: ClassVar[URIRef] = CWE.CweWeaknessCatalog

    Name: str = None
    Version: str = None
    Date: Union[str, XSDDate] = None
    Weaknesses: Optional[Union[dict[Union[str, CweWeaknessID], Union[dict, "CweWeakness"]], list[Union[dict, "CweWeakness"]]]] = empty_dict()
    Groupings: Optional[Union[dict[Union[str, CweGroupingID], Union[dict, "CweGrouping"]], list[Union[dict, "CweGrouping"]]]] = empty_dict()
    Views: Optional[Union[dict[Union[str, CweViewID], Union[dict, "CweView"]], list[Union[dict, "CweView"]]]] = empty_dict()
    External_References: Optional[Union[dict[Union[str, CweExternalReferenceReferenceID], Union[dict, "CweExternalReference"]], list[Union[dict, "CweExternalReference"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Version):
            self.MissingRequiredField("Version")
        if not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self._is_empty(self.Date):
            self.MissingRequiredField("Date")
        if not isinstance(self.Date, XSDDate):
            self.Date = XSDDate(self.Date)

        self._normalize_inlined_as_list(slot_name="Weaknesses", slot_type=CweWeakness, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="Groupings", slot_type=CweGrouping, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="Views", slot_type=CweView, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="External_References", slot_type=CweExternalReference, key_name="Reference_ID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweExternalReference(YAMLRoot):
    """
    A source that entries of the catalogue cite, such as a paper, a book or a web page.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweExternalReference"]
    class_class_curie: ClassVar[str] = "cwe:CweExternalReference"
    class_name: ClassVar[str] = "CweExternalReference"
    class_model_uri: ClassVar[URIRef] = CWE.CweExternalReference

    Reference_ID: Union[str, CweExternalReferenceReferenceID] = None
    Title: str = None
    Author: Optional[Union[str, list[str]]] = empty_list()
    Edition: Optional[str] = None
    Publication: Optional[str] = None
    Publication_Year: Optional[Union[str, CwePublicationYear]] = None
    Publication_Month: Optional[Union[str, CwePublicationMonth]] = None
    Publication_Day: Optional[Union[str, CwePublicationDay]] = None
    Publisher: Optional[str] = None
    URL: Optional[Union[str, URI]] = None
    URL_Date: Optional[Union[str, XSDDate]] = None
    Alt_URL: Optional[Union[str, URI]] = None
    Alt_URL_Date: Optional[Union[str, XSDDate]] = None
    Media_Type: Optional[Union[Union[str, "CweReferenceMediaType"], list[Union[str, "CweReferenceMediaType"]]]] = empty_list()
    Access_Restrictions: Optional[Union[str, "CweReferenceAccessRestriction"]] = None
    Rationale: Optional[Union[Union[str, "CweReferenceRationale"], list[Union[str, "CweReferenceRationale"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Reference_ID):
            self.MissingRequiredField("Reference_ID")
        if not isinstance(self.Reference_ID, CweExternalReferenceReferenceID):
            self.Reference_ID = CweExternalReferenceReferenceID(self.Reference_ID)

        if self._is_empty(self.Title):
            self.MissingRequiredField("Title")
        if not isinstance(self.Title, str):
            self.Title = str(self.Title)

        if not isinstance(self.Author, list):
            self.Author = [self.Author] if self.Author is not None else []
        self.Author = [v if isinstance(v, str) else str(v) for v in self.Author]

        if self.Edition is not None and not isinstance(self.Edition, str):
            self.Edition = str(self.Edition)

        if self.Publication is not None and not isinstance(self.Publication, str):
            self.Publication = str(self.Publication)

        if self.Publication_Year is not None and not isinstance(self.Publication_Year, CwePublicationYear):
            self.Publication_Year = CwePublicationYear(self.Publication_Year)

        if self.Publication_Month is not None and not isinstance(self.Publication_Month, CwePublicationMonth):
            self.Publication_Month = CwePublicationMonth(self.Publication_Month)

        if self.Publication_Day is not None and not isinstance(self.Publication_Day, CwePublicationDay):
            self.Publication_Day = CwePublicationDay(self.Publication_Day)

        if self.Publisher is not None and not isinstance(self.Publisher, str):
            self.Publisher = str(self.Publisher)

        if self.URL is not None and not isinstance(self.URL, URI):
            self.URL = URI(self.URL)

        if self.URL_Date is not None and not isinstance(self.URL_Date, XSDDate):
            self.URL_Date = XSDDate(self.URL_Date)

        if self.Alt_URL is not None and not isinstance(self.Alt_URL, URI):
            self.Alt_URL = URI(self.Alt_URL)

        if self.Alt_URL_Date is not None and not isinstance(self.Alt_URL_Date, XSDDate):
            self.Alt_URL_Date = XSDDate(self.Alt_URL_Date)

        if not isinstance(self.Media_Type, list):
            self.Media_Type = [self.Media_Type] if self.Media_Type is not None else []
        self.Media_Type = [v if isinstance(v, CweReferenceMediaType) else CweReferenceMediaType(v) for v in self.Media_Type]

        if self.Access_Restrictions is not None and not isinstance(self.Access_Restrictions, CweReferenceAccessRestriction):
            self.Access_Restrictions = CweReferenceAccessRestriction(self.Access_Restrictions)

        if not isinstance(self.Rationale, list):
            self.Rationale = [self.Rationale] if self.Rationale is not None else []
        self.Rationale = [v if isinstance(v, CweReferenceRationale) else CweReferenceRationale(v) for v in self.Rationale]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweReference(YAMLRoot):
    """
    A citation of an external reference from an entry or from one of its parts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweReference"]
    class_class_curie: ClassVar[str] = "cwe:CweReference"
    class_name: ClassVar[str] = "CweReference"
    class_model_uri: ClassVar[URIRef] = CWE.CweReference

    External_Reference_ID: Union[str, CweExternalReferenceReferenceID] = None
    Section: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.External_Reference_ID):
            self.MissingRequiredField("External_Reference_ID")
        if not isinstance(self.External_Reference_ID, CweExternalReferenceReferenceID):
            self.External_Reference_ID = CweExternalReferenceReferenceID(self.External_Reference_ID)

        if self.Section is not None and not isinstance(self.Section, str):
            self.Section = str(self.Section)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweDimension(YAMLRoot):
    """
    One aspect of a weakness, or of how two weaknesses differ, named in a word or two.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweDimension"]
    class_class_curie: ClassVar[str] = "cwe:CweDimension"
    class_name: ClassVar[str] = "CweDimension"
    class_model_uri: ClassVar[URIRef] = CWE.CweDimension

    Type: Union[str, "CweDimensionType"] = None
    Value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweDimensionType):
            self.Type = CweDimensionType(self.Type)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, str):
            self.Value = str(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweCustomPhase(YAMLRoot):
    """
    A life cycle stage from a field whose stages differ from those of software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweCustomPhase"]
    class_class_curie: ClassVar[str] = "cwe:CweCustomPhase"
    class_name: ClassVar[str] = "CweCustomPhase"
    class_model_uri: ClassVar[URIRef] = CWE.CweCustomPhase

    Domain: Union[str, "CweCustomPhaseDomain"] = None
    Value: Union[str, "CweAiPhase", "CweHardwarePhase"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Domain):
            self.MissingRequiredField("Domain")
        if not isinstance(self.Domain, CweCustomPhaseDomain):
            self.Domain = CweCustomPhaseDomain(self.Domain)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, (CweAiPhase, CweHardwarePhase)):
            value = self.Value
            for _coerce in (lambda: CweAiPhase(value), lambda: CweHardwarePhase(value)):
                try:
                    self.Value = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[CweAiPhase, CweHardwarePhase] could be constructed from {value!r} for slot Value")

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweNote(YAMLRoot):
    """
    A remark on an entry that fits nowhere else.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweNote"]
    class_class_curie: ClassVar[str] = "cwe:CweNote"
    class_name: ClassVar[str] = "CweNote"
    class_model_uri: ClassVar[URIRef] = CWE.CweNote

    Type: Union[str, "CweNoteType"] = None
    Version: Optional[str] = None
    ReleaseDate: Optional[Union[str, XSDDate]] = None
    Value: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweNoteType):
            self.Type = CweNoteType(self.Type)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self.ReleaseDate is not None and not isinstance(self.ReleaseDate, XSDDate):
            self.ReleaseDate = XSDDate(self.ReleaseDate)

        if self.Value is not None and not isinstance(self.Value, CweStructuredText):
            self.Value = CweStructuredText(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweTaxonomyMapping(YAMLRoot):
    """
    A link from an entry to an entry of another taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweTaxonomyMapping"]
    class_class_curie: ClassVar[str] = "cwe:CweTaxonomyMapping"
    class_name: ClassVar[str] = "CweTaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CWE.CweTaxonomyMapping

    Taxonomy_Name: Union[str, "CweTaxonomyName"] = None
    Entry_ID: Optional[str] = None
    Entry_Name: Optional[str] = None
    Mapping_Fit: Optional[Union[str, "CweMappingFit"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Taxonomy_Name):
            self.MissingRequiredField("Taxonomy_Name")
        if not isinstance(self.Taxonomy_Name, CweTaxonomyName):
            self.Taxonomy_Name = CweTaxonomyName(self.Taxonomy_Name)

        if self.Entry_ID is not None and not isinstance(self.Entry_ID, str):
            self.Entry_ID = str(self.Entry_ID)

        if self.Entry_Name is not None and not isinstance(self.Entry_Name, str):
            self.Entry_Name = str(self.Entry_Name)

        if self.Mapping_Fit is not None and not isinstance(self.Mapping_Fit, CweMappingFit):
            self.Mapping_Fit = CweMappingFit(self.Mapping_Fit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweContentHistory(YAMLRoot):
    """
    The record of who wrote an entry and how it has changed since.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweContentHistory"]
    class_class_curie: ClassVar[str] = "cwe:CweContentHistory"
    class_name: ClassVar[str] = "CweContentHistory"
    class_model_uri: ClassVar[URIRef] = CWE.CweContentHistory

    Submission: Union[Union[dict, "CweSubmission"], list[Union[dict, "CweSubmission"]]] = None
    Modification: Optional[Union[Union[dict, "CweModification"], list[Union[dict, "CweModification"]]]] = empty_list()
    Contribution: Optional[Union[Union[dict, "CweContribution"], list[Union[dict, "CweContribution"]]]] = empty_list()
    Previous_Entry_Name: Optional[Union[Union[dict, "CwePreviousEntryName"], list[Union[dict, "CwePreviousEntryName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Submission):
            self.MissingRequiredField("Submission")
        self._normalize_inlined_as_list(slot_name="Submission", slot_type=CweSubmission, key_name="Submission_Date", keyed=False)

        self._normalize_inlined_as_list(slot_name="Modification", slot_type=CweModification, key_name="Modification_Date", keyed=False)

        self._normalize_inlined_as_list(slot_name="Contribution", slot_type=CweContribution, key_name="Type", keyed=False)

        self._normalize_inlined_as_list(slot_name="Previous_Entry_Name", slot_type=CwePreviousEntryName, key_name="Date", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweSubmission(YAMLRoot):
    """
    Who first submitted an entry, and when it joined the list.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweSubmission"]
    class_class_curie: ClassVar[str] = "cwe:CweSubmission"
    class_name: ClassVar[str] = "CweSubmission"
    class_model_uri: ClassVar[URIRef] = CWE.CweSubmission

    Submission_Date: Union[str, XSDDate] = None
    Submission_Version: str = None
    Submission_ReleaseDate: Union[str, XSDDate] = None
    Submission_Name: Optional[Union[str, list[str]]] = empty_list()
    Submission_Organization: Optional[str] = None
    Submission_Comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Submission_Date):
            self.MissingRequiredField("Submission_Date")
        if not isinstance(self.Submission_Date, XSDDate):
            self.Submission_Date = XSDDate(self.Submission_Date)

        if self._is_empty(self.Submission_Version):
            self.MissingRequiredField("Submission_Version")
        if not isinstance(self.Submission_Version, str):
            self.Submission_Version = str(self.Submission_Version)

        if self._is_empty(self.Submission_ReleaseDate):
            self.MissingRequiredField("Submission_ReleaseDate")
        if not isinstance(self.Submission_ReleaseDate, XSDDate):
            self.Submission_ReleaseDate = XSDDate(self.Submission_ReleaseDate)

        if not isinstance(self.Submission_Name, list):
            self.Submission_Name = [self.Submission_Name] if self.Submission_Name is not None else []
        self.Submission_Name = [v if isinstance(v, str) else str(v) for v in self.Submission_Name]

        if self.Submission_Organization is not None and not isinstance(self.Submission_Organization, str):
            self.Submission_Organization = str(self.Submission_Organization)

        if self.Submission_Comment is not None and not isinstance(self.Submission_Comment, str):
            self.Submission_Comment = str(self.Submission_Comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweModification(YAMLRoot):
    """
    One change made to an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweModification"]
    class_class_curie: ClassVar[str] = "cwe:CweModification"
    class_name: ClassVar[str] = "CweModification"
    class_model_uri: ClassVar[URIRef] = CWE.CweModification

    Modification_Date: Union[str, XSDDate] = None
    Modification_Version: str = None
    Modification_ReleaseDate: Union[str, XSDDate] = None
    Modification_Comment: str = None
    Modification_Name: Optional[str] = None
    Modification_Organization: Optional[str] = None
    Modification_Importance: Optional[Union[str, "CweImportance"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Modification_Date):
            self.MissingRequiredField("Modification_Date")
        if not isinstance(self.Modification_Date, XSDDate):
            self.Modification_Date = XSDDate(self.Modification_Date)

        if self._is_empty(self.Modification_Version):
            self.MissingRequiredField("Modification_Version")
        if not isinstance(self.Modification_Version, str):
            self.Modification_Version = str(self.Modification_Version)

        if self._is_empty(self.Modification_ReleaseDate):
            self.MissingRequiredField("Modification_ReleaseDate")
        if not isinstance(self.Modification_ReleaseDate, XSDDate):
            self.Modification_ReleaseDate = XSDDate(self.Modification_ReleaseDate)

        if self._is_empty(self.Modification_Comment):
            self.MissingRequiredField("Modification_Comment")
        if not isinstance(self.Modification_Comment, str):
            self.Modification_Comment = str(self.Modification_Comment)

        if self.Modification_Name is not None and not isinstance(self.Modification_Name, str):
            self.Modification_Name = str(self.Modification_Name)

        if self.Modification_Organization is not None and not isinstance(self.Modification_Organization, str):
            self.Modification_Organization = str(self.Modification_Organization)

        if self.Modification_Importance is not None and not isinstance(self.Modification_Importance, CweImportance):
            self.Modification_Importance = CweImportance(self.Modification_Importance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweContribution(YAMLRoot):
    """
    Feedback or content that someone gave to an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweContribution"]
    class_class_curie: ClassVar[str] = "cwe:CweContribution"
    class_name: ClassVar[str] = "CweContribution"
    class_model_uri: ClassVar[URIRef] = CWE.CweContribution

    Type: Union[str, "CweContributionType"] = None
    Contribution_Date: Union[str, XSDDate] = None
    Contribution_Version: str = None
    Contribution_ReleaseDate: Union[str, XSDDate] = None
    Contribution_Name: Optional[Union[str, list[str]]] = empty_list()
    Contribution_Organization: Optional[str] = None
    Contribution_Comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweContributionType):
            self.Type = CweContributionType(self.Type)

        if self._is_empty(self.Contribution_Date):
            self.MissingRequiredField("Contribution_Date")
        if not isinstance(self.Contribution_Date, XSDDate):
            self.Contribution_Date = XSDDate(self.Contribution_Date)

        if self._is_empty(self.Contribution_Version):
            self.MissingRequiredField("Contribution_Version")
        if not isinstance(self.Contribution_Version, str):
            self.Contribution_Version = str(self.Contribution_Version)

        if self._is_empty(self.Contribution_ReleaseDate):
            self.MissingRequiredField("Contribution_ReleaseDate")
        if not isinstance(self.Contribution_ReleaseDate, XSDDate):
            self.Contribution_ReleaseDate = XSDDate(self.Contribution_ReleaseDate)

        if not isinstance(self.Contribution_Name, list):
            self.Contribution_Name = [self.Contribution_Name] if self.Contribution_Name is not None else []
        self.Contribution_Name = [v if isinstance(v, str) else str(v) for v in self.Contribution_Name]

        if self.Contribution_Organization is not None and not isinstance(self.Contribution_Organization, str):
            self.Contribution_Organization = str(self.Contribution_Organization)

        if self.Contribution_Comment is not None and not isinstance(self.Contribution_Comment, str):
            self.Contribution_Comment = str(self.Contribution_Comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CwePreviousEntryName(YAMLRoot):
    """
    A name an entry had before.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CwePreviousEntryName"]
    class_class_curie: ClassVar[str] = "cwe:CwePreviousEntryName"
    class_name: ClassVar[str] = "CwePreviousEntryName"
    class_model_uri: ClassVar[URIRef] = CWE.CwePreviousEntryName

    Date: Union[str, XSDDate] = None
    Value: str = None
    Version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Date):
            self.MissingRequiredField("Date")
        if not isinstance(self.Date, XSDDate):
            self.Date = XSDDate(self.Date)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, str):
            self.Value = str(self.Value)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweEntry(YAMLRoot):
    """
    Any item of the CWE List that has an identifier of its own: a weakness, a grouping or a view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweEntry"]
    class_class_curie: ClassVar[str] = "cwe:CweEntry"
    class_name: ClassVar[str] = "CweEntry"
    class_model_uri: ClassVar[URIRef] = CWE.CweEntry

    ID: Union[str, CweEntryID] = None
    Name: str = None
    Status: Union[str, "CweStatus"] = None
    Mapping_Notes: Union[dict, "CweMappingNotes"] = None
    Content_History: Union[dict, CweContentHistory] = None
    References: Optional[Union[Union[dict, CweReference], list[Union[dict, CweReference]]]] = empty_list()
    Notes: Optional[Union[Union[dict, CweNote], list[Union[dict, CweNote]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CweEntryID):
            self.ID = CweEntryID(self.ID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Status):
            self.MissingRequiredField("Status")
        if not isinstance(self.Status, CweStatus):
            self.Status = CweStatus(self.Status)

        if self._is_empty(self.Mapping_Notes):
            self.MissingRequiredField("Mapping_Notes")
        if not isinstance(self.Mapping_Notes, CweMappingNotes):
            self.Mapping_Notes = CweMappingNotes(**as_dict(self.Mapping_Notes))

        if self._is_empty(self.Content_History):
            self.MissingRequiredField("Content_History")
        if not isinstance(self.Content_History, CweContentHistory):
            self.Content_History = CweContentHistory(**as_dict(self.Content_History))

        if not isinstance(self.References, list):
            self.References = [self.References] if self.References is not None else []
        self.References = [v if isinstance(v, CweReference) else CweReference(**as_dict(v)) for v in self.References]

        self._normalize_inlined_as_list(slot_name="Notes", slot_type=CweNote, key_name="Type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweWeakness(CweEntry):
    """
    A type of mistake or condition in software, firmware, hardware or a service that can leave a product open to
    attack.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweWeakness"]
    class_class_curie: ClassVar[str] = "cwe:CweWeakness"
    class_name: ClassVar[str] = "CweWeakness"
    class_model_uri: ClassVar[URIRef] = CWE.CweWeakness

    ID: Union[str, CweWeaknessID] = None
    Name: str = None
    Status: Union[str, "CweStatus"] = None
    Mapping_Notes: Union[dict, "CweMappingNotes"] = None
    Content_History: Union[dict, CweContentHistory] = None
    Abstraction: Union[str, "CweAbstraction"] = None
    Structure: Union[str, "CweStructure"] = None
    Description: str = None
    Diagram: Optional[str] = None
    Extended_Description: Optional[Union[str, CweStructuredText]] = None
    Technical_Nuance: Optional[Union[str, CweStructuredText]] = None
    Dimensions: Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]] = empty_list()
    Related_Weaknesses: Optional[Union[Union[dict, "CweRelatedWeakness"], list[Union[dict, "CweRelatedWeakness"]]]] = empty_list()
    Weakness_Ordinalities: Optional[Union[Union[dict, "CweWeaknessOrdinality"], list[Union[dict, "CweWeaknessOrdinality"]]]] = empty_list()
    Applicable_Platforms: Optional[Union[dict, "CweApplicablePlatforms"]] = None
    Background_Details: Optional[Union[Union[str, CweStructuredText], list[Union[str, CweStructuredText]]]] = empty_list()
    Alternate_Terms: Optional[Union[Union[dict, "CweAlternateTerm"], list[Union[dict, "CweAlternateTerm"]]]] = empty_list()
    Modes_Of_Introduction: Optional[Union[Union[dict, "CweIntroduction"], list[Union[dict, "CweIntroduction"]]]] = empty_list()
    Exploitation_Factors: Optional[Union[Union[str, CweStructuredText], list[Union[str, CweStructuredText]]]] = empty_list()
    Likelihood_Of_Exploit: Optional[Union[str, "CweLikelihood"]] = None
    Common_Consequences: Optional[Union[Union[dict, "CweConsequence"], list[Union[dict, "CweConsequence"]]]] = empty_list()
    Detection_Methods: Optional[Union[Union[dict, "CweDetectionMethod"], list[Union[dict, "CweDetectionMethod"]]]] = empty_list()
    Potential_Mitigations: Optional[Union[Union[dict, "CweMitigation"], list[Union[dict, "CweMitigation"]]]] = empty_list()
    Demonstrative_Examples: Optional[Union[Union[dict, "CweDemonstrativeExample"], list[Union[dict, "CweDemonstrativeExample"]]]] = empty_list()
    Observed_Examples: Optional[Union[Union[dict, "CweObservedExample"], list[Union[dict, "CweObservedExample"]]]] = empty_list()
    Functional_Areas: Optional[Union[Union[str, "CweFunctionalArea"], list[Union[str, "CweFunctionalArea"]]]] = empty_list()
    Affected_Resources: Optional[Union[Union[str, "CweResource"], list[Union[str, "CweResource"]]]] = empty_list()
    Taxonomy_Mappings: Optional[Union[Union[dict, CweTaxonomyMapping], list[Union[dict, CweTaxonomyMapping]]]] = empty_list()
    Related_Attack_Patterns: Optional[Union[Union[dict, "CweRelatedAttackPattern"], list[Union[dict, "CweRelatedAttackPattern"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CweWeaknessID):
            self.ID = CweWeaknessID(self.ID)

        if self._is_empty(self.Abstraction):
            self.MissingRequiredField("Abstraction")
        if not isinstance(self.Abstraction, CweAbstraction):
            self.Abstraction = CweAbstraction(self.Abstraction)

        if self._is_empty(self.Structure):
            self.MissingRequiredField("Structure")
        if not isinstance(self.Structure, CweStructure):
            self.Structure = CweStructure(self.Structure)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if self.Diagram is not None and not isinstance(self.Diagram, str):
            self.Diagram = str(self.Diagram)

        if self.Extended_Description is not None and not isinstance(self.Extended_Description, CweStructuredText):
            self.Extended_Description = CweStructuredText(self.Extended_Description)

        if self.Technical_Nuance is not None and not isinstance(self.Technical_Nuance, CweStructuredText):
            self.Technical_Nuance = CweStructuredText(self.Technical_Nuance)

        self._normalize_inlined_as_list(slot_name="Dimensions", slot_type=CweDimension, key_name="Type", keyed=False)

        self._normalize_inlined_as_list(slot_name="Related_Weaknesses", slot_type=CweRelatedWeakness, key_name="Nature", keyed=False)

        self._normalize_inlined_as_list(slot_name="Weakness_Ordinalities", slot_type=CweWeaknessOrdinality, key_name="Ordinality", keyed=False)

        if self.Applicable_Platforms is not None and not isinstance(self.Applicable_Platforms, CweApplicablePlatforms):
            self.Applicable_Platforms = CweApplicablePlatforms(**as_dict(self.Applicable_Platforms))

        if not isinstance(self.Background_Details, list):
            self.Background_Details = [self.Background_Details] if self.Background_Details is not None else []
        self.Background_Details = [v if isinstance(v, CweStructuredText) else CweStructuredText(v) for v in self.Background_Details]

        self._normalize_inlined_as_list(slot_name="Alternate_Terms", slot_type=CweAlternateTerm, key_name="Term", keyed=False)

        if not isinstance(self.Modes_Of_Introduction, list):
            self.Modes_Of_Introduction = [self.Modes_Of_Introduction] if self.Modes_Of_Introduction is not None else []
        self.Modes_Of_Introduction = [v if isinstance(v, CweIntroduction) else CweIntroduction(**as_dict(v)) for v in self.Modes_Of_Introduction]

        if not isinstance(self.Exploitation_Factors, list):
            self.Exploitation_Factors = [self.Exploitation_Factors] if self.Exploitation_Factors is not None else []
        self.Exploitation_Factors = [v if isinstance(v, CweStructuredText) else CweStructuredText(v) for v in self.Exploitation_Factors]

        if self.Likelihood_Of_Exploit is not None and not isinstance(self.Likelihood_Of_Exploit, CweLikelihood):
            self.Likelihood_Of_Exploit = CweLikelihood(self.Likelihood_Of_Exploit)

        self._normalize_inlined_as_list(slot_name="Common_Consequences", slot_type=CweConsequence, key_name="Scope", keyed=False)

        self._normalize_inlined_as_list(slot_name="Detection_Methods", slot_type=CweDetectionMethod, key_name="Method", keyed=False)

        self._normalize_inlined_as_list(slot_name="Potential_Mitigations", slot_type=CweMitigation, key_name="Description", keyed=False)

        self._normalize_inlined_as_list(slot_name="Demonstrative_Examples", slot_type=CweDemonstrativeExample, key_name="Intro_Text", keyed=False)

        self._normalize_inlined_as_list(slot_name="Observed_Examples", slot_type=CweObservedExample, key_name="Reference", keyed=False)

        if not isinstance(self.Functional_Areas, list):
            self.Functional_Areas = [self.Functional_Areas] if self.Functional_Areas is not None else []
        self.Functional_Areas = [v if isinstance(v, CweFunctionalArea) else CweFunctionalArea(v) for v in self.Functional_Areas]

        if not isinstance(self.Affected_Resources, list):
            self.Affected_Resources = [self.Affected_Resources] if self.Affected_Resources is not None else []
        self.Affected_Resources = [v if isinstance(v, CweResource) else CweResource(v) for v in self.Affected_Resources]

        self._normalize_inlined_as_list(slot_name="Taxonomy_Mappings", slot_type=CweTaxonomyMapping, key_name="Taxonomy_Name", keyed=False)

        self._normalize_inlined_as_list(slot_name="Related_Attack_Patterns", slot_type=CweRelatedAttackPattern, key_name="CAPEC_ID", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweGrouping(CweEntry):
    """
    A set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to.
    Schema versions before 8.0 called it a category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweGrouping"]
    class_class_curie: ClassVar[str] = "cwe:CweGrouping"
    class_name: ClassVar[str] = "CweGrouping"
    class_model_uri: ClassVar[URIRef] = CWE.CweGrouping

    ID: Union[str, CweGroupingID] = None
    Name: str = None
    Status: Union[str, "CweStatus"] = None
    Mapping_Notes: Union[dict, "CweMappingNotes"] = None
    Content_History: Union[dict, CweContentHistory] = None
    Summary: Union[str, CweStructuredText] = None
    Relationships: Optional[Union[dict, "CweRelationships"]] = None
    Taxonomy_Mappings: Optional[Union[Union[dict, CweTaxonomyMapping], list[Union[dict, CweTaxonomyMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CweGroupingID):
            self.ID = CweGroupingID(self.ID)

        if self._is_empty(self.Summary):
            self.MissingRequiredField("Summary")
        if not isinstance(self.Summary, CweStructuredText):
            self.Summary = CweStructuredText(self.Summary)

        if self.Relationships is not None and not isinstance(self.Relationships, CweRelationships):
            self.Relationships = CweRelationships(**as_dict(self.Relationships))

        self._normalize_inlined_as_list(slot_name="Taxonomy_Mappings", slot_type=CweTaxonomyMapping, key_name="Taxonomy_Name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweView(CweEntry):
    """
    A way of looking at the catalogue, as a subset of its entries seen from one standpoint.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweView"]
    class_class_curie: ClassVar[str] = "cwe:CweView"
    class_name: ClassVar[str] = "CweView"
    class_model_uri: ClassVar[URIRef] = CWE.CweView

    ID: Union[str, CweViewID] = None
    Name: str = None
    Status: Union[str, "CweStatus"] = None
    Mapping_Notes: Union[dict, "CweMappingNotes"] = None
    Content_History: Union[dict, CweContentHistory] = None
    Type: Union[str, "CweViewType"] = None
    Objective: Union[str, CweStructuredText] = None
    Audience: Optional[Union[Union[dict, "CweStakeholder"], list[Union[dict, "CweStakeholder"]]]] = empty_list()
    Members: Optional[Union[dict, "CweRelationships"]] = None
    Filter: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CweViewID):
            self.ID = CweViewID(self.ID)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweViewType):
            self.Type = CweViewType(self.Type)

        if self._is_empty(self.Objective):
            self.MissingRequiredField("Objective")
        if not isinstance(self.Objective, CweStructuredText):
            self.Objective = CweStructuredText(self.Objective)

        self._normalize_inlined_as_list(slot_name="Audience", slot_type=CweStakeholder, key_name="Type", keyed=False)

        if self.Members is not None and not isinstance(self.Members, CweRelationships):
            self.Members = CweRelationships(**as_dict(self.Members))

        if self.Filter is not None and not isinstance(self.Filter, str):
            self.Filter = str(self.Filter)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweRelatedWeakness(YAMLRoot):
    """
    A link from a weakness to another weakness, in one view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweRelatedWeakness"]
    class_class_curie: ClassVar[str] = "cwe:CweRelatedWeakness"
    class_name: ClassVar[str] = "CweRelatedWeakness"
    class_model_uri: ClassVar[URIRef] = CWE.CweRelatedWeakness

    Nature: Union[str, "CweRelatedNature"] = None
    CWE_ID: Union[str, CweWeaknessID] = None
    View_ID: Union[str, CweViewID] = None
    Chain_ID: Optional[Union[str, CweWeaknessID]] = None
    Ordinal: Optional[Union[str, "CweOrdinal"]] = None
    Dimensions: Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Nature):
            self.MissingRequiredField("Nature")
        if not isinstance(self.Nature, CweRelatedNature):
            self.Nature = CweRelatedNature(self.Nature)

        if self._is_empty(self.CWE_ID):
            self.MissingRequiredField("CWE_ID")
        if not isinstance(self.CWE_ID, CweWeaknessID):
            self.CWE_ID = CweWeaknessID(self.CWE_ID)

        if self._is_empty(self.View_ID):
            self.MissingRequiredField("View_ID")
        if not isinstance(self.View_ID, CweViewID):
            self.View_ID = CweViewID(self.View_ID)

        if self.Chain_ID is not None and not isinstance(self.Chain_ID, CweWeaknessID):
            self.Chain_ID = CweWeaknessID(self.Chain_ID)

        if self.Ordinal is not None and not isinstance(self.Ordinal, CweOrdinal):
            self.Ordinal = CweOrdinal(self.Ordinal)

        self._normalize_inlined_as_list(slot_name="Dimensions", slot_type=CweDimension, key_name="Type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweWeaknessOrdinality(YAMLRoot):
    """
    Whether a weakness tends to be a first cause or the result of another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweWeaknessOrdinality"]
    class_class_curie: ClassVar[str] = "cwe:CweWeaknessOrdinality"
    class_name: ClassVar[str] = "CweWeaknessOrdinality"
    class_model_uri: ClassVar[URIRef] = CWE.CweWeaknessOrdinality

    Ordinality: Union[str, "CweOrdinality"] = None
    Description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Ordinality):
            self.MissingRequiredField("Ordinality")
        if not isinstance(self.Ordinality, CweOrdinality):
            self.Ordinality = CweOrdinality(self.Ordinality)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweApplicablePlatforms(YAMLRoot):
    """
    The kinds of platform where a weakness can appear.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweApplicablePlatforms"]
    class_class_curie: ClassVar[str] = "cwe:CweApplicablePlatforms"
    class_name: ClassVar[str] = "CweApplicablePlatforms"
    class_model_uri: ClassVar[URIRef] = CWE.CweApplicablePlatforms

    Language: Optional[Union[Union[dict, "CweLanguagePlatform"], list[Union[dict, "CweLanguagePlatform"]]]] = empty_list()
    Operating_System: Optional[Union[Union[dict, "CweOperatingSystemPlatform"], list[Union[dict, "CweOperatingSystemPlatform"]]]] = empty_list()
    Architecture: Optional[Union[Union[dict, "CweArchitecturePlatform"], list[Union[dict, "CweArchitecturePlatform"]]]] = empty_list()
    Technology: Optional[Union[Union[dict, "CweTechnologyPlatform"], list[Union[dict, "CweTechnologyPlatform"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="Language", slot_type=CweLanguagePlatform, key_name="Prevalence", keyed=False)

        self._normalize_inlined_as_list(slot_name="Operating_System", slot_type=CweOperatingSystemPlatform, key_name="Prevalence", keyed=False)

        self._normalize_inlined_as_list(slot_name="Architecture", slot_type=CweArchitecturePlatform, key_name="Prevalence", keyed=False)

        self._normalize_inlined_as_list(slot_name="Technology", slot_type=CweTechnologyPlatform, key_name="Prevalence", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweLanguagePlatform(YAMLRoot):
    """
    A language where a weakness can appear, named or by its family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweLanguagePlatform"]
    class_class_curie: ClassVar[str] = "cwe:CweLanguagePlatform"
    class_name: ClassVar[str] = "CweLanguagePlatform"
    class_model_uri: ClassVar[URIRef] = CWE.CweLanguagePlatform

    Prevalence: Union[str, "CwePrevalence"] = None
    Name: Optional[Union[str, "CweLanguageName"]] = None
    Class: Optional[Union[str, "CweLanguageClass"]] = None
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Prevalence):
            self.MissingRequiredField("Prevalence")
        if not isinstance(self.Prevalence, CwePrevalence):
            self.Prevalence = CwePrevalence(self.Prevalence)

        if self.Name is not None and not isinstance(self.Name, CweLanguageName):
            self.Name = CweLanguageName(self.Name)

        if self.Class is not None and not isinstance(self.Class, CweLanguageClass):
            self.Class = CweLanguageClass(self.Class)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweOperatingSystemPlatform(YAMLRoot):
    """
    An operating system where a weakness can appear, named or by its family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweOperatingSystemPlatform"]
    class_class_curie: ClassVar[str] = "cwe:CweOperatingSystemPlatform"
    class_name: ClassVar[str] = "CweOperatingSystemPlatform"
    class_model_uri: ClassVar[URIRef] = CWE.CweOperatingSystemPlatform

    Prevalence: Union[str, "CwePrevalence"] = None
    Name: Optional[Union[str, "CweOperatingSystemName"]] = None
    Version: Optional[str] = None
    CPE_ID: Optional[str] = None
    Class: Optional[Union[str, "CweOperatingSystemClass"]] = None
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Prevalence):
            self.MissingRequiredField("Prevalence")
        if not isinstance(self.Prevalence, CwePrevalence):
            self.Prevalence = CwePrevalence(self.Prevalence)

        if self.Name is not None and not isinstance(self.Name, CweOperatingSystemName):
            self.Name = CweOperatingSystemName(self.Name)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self.CPE_ID is not None and not isinstance(self.CPE_ID, str):
            self.CPE_ID = str(self.CPE_ID)

        if self.Class is not None and not isinstance(self.Class, CweOperatingSystemClass):
            self.Class = CweOperatingSystemClass(self.Class)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweArchitecturePlatform(YAMLRoot):
    """
    A hardware architecture where a weakness can appear, named or by its family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweArchitecturePlatform"]
    class_class_curie: ClassVar[str] = "cwe:CweArchitecturePlatform"
    class_name: ClassVar[str] = "CweArchitecturePlatform"
    class_model_uri: ClassVar[URIRef] = CWE.CweArchitecturePlatform

    Prevalence: Union[str, "CwePrevalence"] = None
    Name: Optional[Union[str, "CweArchitectureName"]] = None
    Class: Optional[Union[str, "CweArchitectureClass"]] = None
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Prevalence):
            self.MissingRequiredField("Prevalence")
        if not isinstance(self.Prevalence, CwePrevalence):
            self.Prevalence = CwePrevalence(self.Prevalence)

        if self.Name is not None and not isinstance(self.Name, CweArchitectureName):
            self.Name = CweArchitectureName(self.Name)

        if self.Class is not None and not isinstance(self.Class, CweArchitectureClass):
            self.Class = CweArchitectureClass(self.Class)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweTechnologyPlatform(YAMLRoot):
    """
    A technology where a weakness can appear, named or by its family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweTechnologyPlatform"]
    class_class_curie: ClassVar[str] = "cwe:CweTechnologyPlatform"
    class_name: ClassVar[str] = "CweTechnologyPlatform"
    class_model_uri: ClassVar[URIRef] = CWE.CweTechnologyPlatform

    Prevalence: Union[str, "CwePrevalence"] = None
    Name: Optional[Union[str, "CweTechnologyName"]] = None
    Class: Optional[Union[str, "CweTechnologyClass"]] = None
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Prevalence):
            self.MissingRequiredField("Prevalence")
        if not isinstance(self.Prevalence, CwePrevalence):
            self.Prevalence = CwePrevalence(self.Prevalence)

        if self.Name is not None and not isinstance(self.Name, CweTechnologyName):
            self.Name = CweTechnologyName(self.Name)

        if self.Class is not None and not isinstance(self.Class, CweTechnologyClass):
            self.Class = CweTechnologyClass(self.Class)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweAlternateTerm(YAMLRoot):
    """
    Another name people use for a weakness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweAlternateTerm"]
    class_class_curie: ClassVar[str] = "cwe:CweAlternateTerm"
    class_name: ClassVar[str] = "CweAlternateTerm"
    class_model_uri: ClassVar[URIRef] = CWE.CweAlternateTerm

    Term: str = None
    Role: Optional[Union[Union[str, "CweAlternateTermRole"], list[Union[str, "CweAlternateTermRole"]]]] = empty_list()
    Description: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Term):
            self.MissingRequiredField("Term")
        if not isinstance(self.Term, str):
            self.Term = str(self.Term)

        if not isinstance(self.Role, list):
            self.Role = [self.Role] if self.Role is not None else []
        self.Role = [v if isinstance(v, CweAlternateTermRole) else CweAlternateTermRole(v) for v in self.Role]

        if self.Description is not None and not isinstance(self.Description, CweStructuredText):
            self.Description = CweStructuredText(self.Description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweIntroduction(YAMLRoot):
    """
    One way a weakness can get into a product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweIntroduction"]
    class_class_curie: ClassVar[str] = "cwe:CweIntroduction"
    class_name: ClassVar[str] = "CweIntroduction"
    class_model_uri: ClassVar[URIRef] = CWE.CweIntroduction

    Phase: Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]] = empty_list()
    Custom_Phase: Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]] = empty_list()
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.Phase, list):
            self.Phase = [self.Phase] if self.Phase is not None else []
        self.Phase = [v if isinstance(v, CwePhase) else CwePhase(v) for v in self.Phase]

        self._normalize_inlined_as_list(slot_name="Custom_Phase", slot_type=CweCustomPhase, key_name="Domain", keyed=False)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweConsequence(YAMLRoot):
    """
    One thing that can follow when a weakness is exploited.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweConsequence"]
    class_class_curie: ClassVar[str] = "cwe:CweConsequence"
    class_name: ClassVar[str] = "CweConsequence"
    class_model_uri: ClassVar[URIRef] = CWE.CweConsequence

    Scope: Union[Union[str, "CweScope"], list[Union[str, "CweScope"]]] = None
    Impact: Union[Union[str, "CweTechnicalImpact"], list[Union[str, "CweTechnicalImpact"]]] = None
    Consequence_ID: Optional[str] = None
    Likelihood: Optional[Union[str, "CweLikelihood"]] = None
    Note: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Scope):
            self.MissingRequiredField("Scope")
        if not isinstance(self.Scope, list):
            self.Scope = [self.Scope] if self.Scope is not None else []
        self.Scope = [v if isinstance(v, CweScope) else CweScope(v) for v in self.Scope]

        if self._is_empty(self.Impact):
            self.MissingRequiredField("Impact")
        if not isinstance(self.Impact, list):
            self.Impact = [self.Impact] if self.Impact is not None else []
        self.Impact = [v if isinstance(v, CweTechnicalImpact) else CweTechnicalImpact(v) for v in self.Impact]

        if self.Consequence_ID is not None and not isinstance(self.Consequence_ID, str):
            self.Consequence_ID = str(self.Consequence_ID)

        if self.Likelihood is not None and not isinstance(self.Likelihood, CweLikelihood):
            self.Likelihood = CweLikelihood(self.Likelihood)

        if self.Note is not None and not isinstance(self.Note, CweStructuredText):
            self.Note = CweStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweDetectionMethod(YAMLRoot):
    """
    One way of finding a weakness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweDetectionMethod"]
    class_class_curie: ClassVar[str] = "cwe:CweDetectionMethod"
    class_name: ClassVar[str] = "CweDetectionMethod"
    class_model_uri: ClassVar[URIRef] = CWE.CweDetectionMethod

    Method: Union[str, "CweDetectionMethodName"] = None
    Description: Union[str, CweStructuredText] = None
    Detection_Method_ID: Optional[str] = None
    Phase: Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]] = empty_list()
    Custom_Phase: Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]] = empty_list()
    Effectiveness: Optional[Union[str, "CweDetectionEffectiveness"]] = None
    Effectiveness_Notes: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Method):
            self.MissingRequiredField("Method")
        if not isinstance(self.Method, CweDetectionMethodName):
            self.Method = CweDetectionMethodName(self.Method)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CweStructuredText):
            self.Description = CweStructuredText(self.Description)

        if self.Detection_Method_ID is not None and not isinstance(self.Detection_Method_ID, str):
            self.Detection_Method_ID = str(self.Detection_Method_ID)

        if not isinstance(self.Phase, list):
            self.Phase = [self.Phase] if self.Phase is not None else []
        self.Phase = [v if isinstance(v, CwePhase) else CwePhase(v) for v in self.Phase]

        self._normalize_inlined_as_list(slot_name="Custom_Phase", slot_type=CweCustomPhase, key_name="Domain", keyed=False)

        if self.Effectiveness is not None and not isinstance(self.Effectiveness, CweDetectionEffectiveness):
            self.Effectiveness = CweDetectionEffectiveness(self.Effectiveness)

        if self.Effectiveness_Notes is not None and not isinstance(self.Effectiveness_Notes, CweStructuredText):
            self.Effectiveness_Notes = CweStructuredText(self.Effectiveness_Notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweMitigation(YAMLRoot):
    """
    One way of preventing a weakness or reducing what it can do.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweMitigation"]
    class_class_curie: ClassVar[str] = "cwe:CweMitigation"
    class_name: ClassVar[str] = "CweMitigation"
    class_model_uri: ClassVar[URIRef] = CWE.CweMitigation

    Description: Union[str, CweStructuredText] = None
    Mitigation_ID: Optional[str] = None
    Phase: Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]] = empty_list()
    Custom_Phase: Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]] = empty_list()
    Strategy: Optional[Union[str, "CweMitigationStrategy"]] = None
    Effectiveness: Optional[Union[str, "CweEffectiveness"]] = None
    Effectiveness_Notes: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CweStructuredText):
            self.Description = CweStructuredText(self.Description)

        if self.Mitigation_ID is not None and not isinstance(self.Mitigation_ID, str):
            self.Mitigation_ID = str(self.Mitigation_ID)

        if not isinstance(self.Phase, list):
            self.Phase = [self.Phase] if self.Phase is not None else []
        self.Phase = [v if isinstance(v, CwePhase) else CwePhase(v) for v in self.Phase]

        self._normalize_inlined_as_list(slot_name="Custom_Phase", slot_type=CweCustomPhase, key_name="Domain", keyed=False)

        if self.Strategy is not None and not isinstance(self.Strategy, CweMitigationStrategy):
            self.Strategy = CweMitigationStrategy(self.Strategy)

        if self.Effectiveness is not None and not isinstance(self.Effectiveness, CweEffectiveness):
            self.Effectiveness = CweEffectiveness(self.Effectiveness)

        if self.Effectiveness_Notes is not None and not isinstance(self.Effectiveness_Notes, CweStructuredText):
            self.Effectiveness_Notes = CweStructuredText(self.Effectiveness_Notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweDemonstrativeExample(YAMLRoot):
    """
    A worked example of how a weakness looks in code.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweDemonstrativeExample"]
    class_class_curie: ClassVar[str] = "cwe:CweDemonstrativeExample"
    class_name: ClassVar[str] = "CweDemonstrativeExample"
    class_model_uri: ClassVar[URIRef] = CWE.CweDemonstrativeExample

    Intro_Text: Union[str, CweStructuredText] = None
    Demonstrative_Example_ID: Optional[str] = None
    Title_Text: Optional[str] = None
    Entries: Optional[Union[Union[dict, "CweExampleEntry"], list[Union[dict, "CweExampleEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Intro_Text):
            self.MissingRequiredField("Intro_Text")
        if not isinstance(self.Intro_Text, CweStructuredText):
            self.Intro_Text = CweStructuredText(self.Intro_Text)

        if self.Demonstrative_Example_ID is not None and not isinstance(self.Demonstrative_Example_ID, str):
            self.Demonstrative_Example_ID = str(self.Demonstrative_Example_ID)

        if self.Title_Text is not None and not isinstance(self.Title_Text, str):
            self.Title_Text = str(self.Title_Text)

        if not isinstance(self.Entries, list):
            self.Entries = [self.Entries] if self.Entries is not None else []
        self.Entries = [v if isinstance(v, CweExampleEntry) else CweExampleEntry(**as_dict(v)) for v in self.Entries]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweExampleEntry(YAMLRoot):
    """
    One step of a worked example, either some prose or some code.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweExampleEntry"]
    class_class_curie: ClassVar[str] = "cwe:CweExampleEntry"
    class_name: ClassVar[str] = "CweExampleEntry"
    class_model_uri: ClassVar[URIRef] = CWE.CweExampleEntry

    Body_Text: Optional[Union[str, CweStructuredText]] = None
    Example_Code: Optional[Union[dict, "CweExampleCode"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Body_Text is not None and not isinstance(self.Body_Text, CweStructuredText):
            self.Body_Text = CweStructuredText(self.Body_Text)

        if self.Example_Code is not None and not isinstance(self.Example_Code, CweExampleCode):
            self.Example_Code = CweExampleCode(**as_dict(self.Example_Code))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweExampleCode(YAMLRoot):
    """
    A block of code in a worked example.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweExampleCode"]
    class_class_curie: ClassVar[str] = "cwe:CweExampleCode"
    class_name: ClassVar[str] = "CweExampleCode"
    class_model_uri: ClassVar[URIRef] = CWE.CweExampleCode

    Nature: Union[str, "CweCodeNature"] = None
    Language: Optional[Union[str, "CweLanguageName"]] = None
    Value: Optional[Union[str, CweStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Nature):
            self.MissingRequiredField("Nature")
        if not isinstance(self.Nature, CweCodeNature):
            self.Nature = CweCodeNature(self.Nature)

        if self.Language is not None and not isinstance(self.Language, CweLanguageName):
            self.Language = CweLanguageName(self.Language)

        if self.Value is not None and not isinstance(self.Value, CweStructuredText):
            self.Value = CweStructuredText(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweObservedExample(YAMLRoot):
    """
    A real case of a weakness, usually a CVE record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweObservedExample"]
    class_class_curie: ClassVar[str] = "cwe:CweObservedExample"
    class_name: ClassVar[str] = "CweObservedExample"
    class_model_uri: ClassVar[URIRef] = CWE.CweObservedExample

    Reference: str = None
    Description: Union[str, CweStructuredText] = None
    Link: Union[str, URI] = None
    Rationale: Optional[Union[Union[str, "CweObservedExampleRationale"], list[Union[str, "CweObservedExampleRationale"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Reference):
            self.MissingRequiredField("Reference")
        if not isinstance(self.Reference, str):
            self.Reference = str(self.Reference)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CweStructuredText):
            self.Description = CweStructuredText(self.Description)

        if self._is_empty(self.Link):
            self.MissingRequiredField("Link")
        if not isinstance(self.Link, URI):
            self.Link = URI(self.Link)

        if not isinstance(self.Rationale, list):
            self.Rationale = [self.Rationale] if self.Rationale is not None else []
        self.Rationale = [v if isinstance(v, CweObservedExampleRationale) else CweObservedExampleRationale(v) for v in self.Rationale]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweRelatedAttackPattern(YAMLRoot):
    """
    A pointer from a weakness to an attack pattern in the CAPEC list.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweRelatedAttackPattern"]
    class_class_curie: ClassVar[str] = "cwe:CweRelatedAttackPattern"
    class_name: ClassVar[str] = "CweRelatedAttackPattern"
    class_model_uri: ClassVar[URIRef] = CWE.CweRelatedAttackPattern

    CAPEC_ID: Union[str, CweCapecId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CAPEC_ID):
            self.MissingRequiredField("CAPEC_ID")
        if not isinstance(self.CAPEC_ID, CweCapecId):
            self.CAPEC_ID = CweCapecId(self.CAPEC_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweStakeholder(YAMLRoot):
    """
    A group of people who may find a view useful.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweStakeholder"]
    class_class_curie: ClassVar[str] = "cwe:CweStakeholder"
    class_name: ClassVar[str] = "CweStakeholder"
    class_model_uri: ClassVar[URIRef] = CWE.CweStakeholder

    Type: Union[str, "CweStakeholderType"] = None
    Description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweStakeholderType):
            self.Type = CweStakeholderType(self.Type)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweMember(YAMLRoot):
    """
    A link from a grouping or a view to an entry it holds or belongs to, in one view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweMember"]
    class_class_curie: ClassVar[str] = "cwe:CweMember"
    class_name: ClassVar[str] = "CweMember"
    class_model_uri: ClassVar[URIRef] = CWE.CweMember

    CWE_ID: Union[str, CweEntryID] = None
    View_ID: Union[str, CweViewID] = None
    Dimensions: Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CWE_ID):
            self.MissingRequiredField("CWE_ID")
        if not isinstance(self.CWE_ID, CweEntryID):
            self.CWE_ID = CweEntryID(self.CWE_ID)

        if self._is_empty(self.View_ID):
            self.MissingRequiredField("View_ID")
        if not isinstance(self.View_ID, CweViewID):
            self.View_ID = CweViewID(self.View_ID)

        self._normalize_inlined_as_list(slot_name="Dimensions", slot_type=CweDimension, key_name="Type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweRelationships(YAMLRoot):
    """
    The entries that a grouping or a view holds or belongs to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweRelationships"]
    class_class_curie: ClassVar[str] = "cwe:CweRelationships"
    class_name: ClassVar[str] = "CweRelationships"
    class_model_uri: ClassVar[URIRef] = CWE.CweRelationships

    Member_Of: Optional[Union[Union[dict, CweMember], list[Union[dict, CweMember]]]] = empty_list()
    Has_Member: Optional[Union[Union[dict, CweMember], list[Union[dict, CweMember]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.Member_Of, list):
            self.Member_Of = [self.Member_Of] if self.Member_Of is not None else []
        self.Member_Of = [v if isinstance(v, CweMember) else CweMember(**as_dict(v)) for v in self.Member_Of]

        if not isinstance(self.Has_Member, list):
            self.Has_Member = [self.Has_Member] if self.Has_Member is not None else []
        self.Has_Member = [v if isinstance(v, CweMember) else CweMember(**as_dict(v)) for v in self.Has_Member]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweMappingNotes(YAMLRoot):
    """
    Guidance on whether to map a real vulnerability to an entry, and on what to use instead.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweMappingNotes"]
    class_class_curie: ClassVar[str] = "cwe:CweMappingNotes"
    class_name: ClassVar[str] = "CweMappingNotes"
    class_model_uri: ClassVar[URIRef] = CWE.CweMappingNotes

    Usage: Union[str, "CweUsage"] = None
    Rationale: Union[str, CweStructuredText] = None
    Comments: Union[str, CweStructuredText] = None
    Reasons: Union[Union[dict, "CweMappingReason"], list[Union[dict, "CweMappingReason"]]] = None
    Suggestions: Optional[Union[Union[dict, "CweMappingSuggestion"], list[Union[dict, "CweMappingSuggestion"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Usage):
            self.MissingRequiredField("Usage")
        if not isinstance(self.Usage, CweUsage):
            self.Usage = CweUsage(self.Usage)

        if self._is_empty(self.Rationale):
            self.MissingRequiredField("Rationale")
        if not isinstance(self.Rationale, CweStructuredText):
            self.Rationale = CweStructuredText(self.Rationale)

        if self._is_empty(self.Comments):
            self.MissingRequiredField("Comments")
        if not isinstance(self.Comments, CweStructuredText):
            self.Comments = CweStructuredText(self.Comments)

        if self._is_empty(self.Reasons):
            self.MissingRequiredField("Reasons")
        self._normalize_inlined_as_list(slot_name="Reasons", slot_type=CweMappingReason, key_name="Type", keyed=False)

        self._normalize_inlined_as_list(slot_name="Suggestions", slot_type=CweMappingSuggestion, key_name="Comment", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweMappingReason(YAMLRoot):
    """
    One short label that sums up the usage of an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweMappingReason"]
    class_class_curie: ClassVar[str] = "cwe:CweMappingReason"
    class_name: ClassVar[str] = "CweMappingReason"
    class_model_uri: ClassVar[URIRef] = CWE.CweMappingReason

    Type: Union[str, "CweReason"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CweReason):
            self.Type = CweReason(self.Type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CweMappingSuggestion(YAMLRoot):
    """
    A weakness that may suit a mapping better than this entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CWE["CweMappingSuggestion"]
    class_class_curie: ClassVar[str] = "cwe:CweMappingSuggestion"
    class_name: ClassVar[str] = "CweMappingSuggestion"
    class_model_uri: ClassVar[URIRef] = CWE.CweMappingSuggestion

    CWE_ID: Union[str, CweWeaknessID] = None
    Comment: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CWE_ID):
            self.MissingRequiredField("CWE_ID")
        if not isinstance(self.CWE_ID, CweWeaknessID):
            self.CWE_ID = CweWeaknessID(self.CWE_ID)

        if self._is_empty(self.Comment):
            self.MissingRequiredField("Comment")
        if not isinstance(self.Comment, str):
            self.Comment = str(self.Comment)

        super().__post_init__(**kwargs)


# Enumerations
class CweAbstraction(EnumDefinitionImpl):
    """
    How far a weakness is described in general terms or tied to a specific product or resource.
    """
    Pillar = PermissibleValue(
        text="Pillar",
        description="The most general level, a theme that the weaknesses under it share.")
    Class = PermissibleValue(
        text="Class",
        description="A very general weakness, usually independent of any language or technology.")
    Base = PermissibleValue(
        text="Base",
        description="A weakness general enough to apply widely and detailed enough to find or prevent it.")
    Variant = PermissibleValue(
        text="Variant",
        description="A weakness tied to a particular language, technology or kind of product.")
    Compound = PermissibleValue(
        text="Compound",
        description="An entry that ties two or more weaknesses together, as a chain or a composite.")

    _defn = EnumDefinition(
        name="CweAbstraction",
        description="How far a weakness is described in general terms or tied to a specific product or resource.",
    )

class CweAlternateTermRole(EnumDefinitionImpl):
    """
    The part an alternate term plays when people talk about a weakness.
    """
    Abbreviation = PermissibleValue(text="Abbreviation")
    Acronym = PermissibleValue(text="Acronym")
    Discouraged = PermissibleValue(text="Discouraged")
    Legacy = PermissibleValue(text="Legacy")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweAlternateTermRole",
        description="The part an alternate term plays when people talk about a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Alternate-Spelling",
            PermissibleValue(text="Alternate-Spelling"))
        setattr(cls, "Attack-Focused",
            PermissibleValue(text="Attack-Focused"))
        setattr(cls, "Impact-Oriented",
            PermissibleValue(text="Impact-Oriented"))
        setattr(cls, "Multi-Weakness",
            PermissibleValue(text="Multi-Weakness"))
        setattr(cls, "Multiple-Interpretation",
            PermissibleValue(text="Multiple-Interpretation"))
        setattr(cls, "Common-Name",
            PermissibleValue(text="Common-Name"))

class CweArchitectureClass(EnumDefinitionImpl):
    """
    A broad family of hardware architectures.
    """
    Embedded = PermissibleValue(text="Embedded")
    Microcomputer = PermissibleValue(text="Microcomputer")
    Workstation = PermissibleValue(text="Workstation")

    _defn = EnumDefinition(
        name="CweArchitectureClass",
        description="A broad family of hardware architectures.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Architecture-Specific",
            PermissibleValue(
                text="Not Architecture-Specific",
                description="The weakness can appear on many architectures."))

class CweArchitectureName(EnumDefinitionImpl):
    """
    A named hardware architecture.
    """
    Alpha = PermissibleValue(text="Alpha")
    ARM = PermissibleValue(text="ARM")
    Itanium = PermissibleValue(text="Itanium")
    SPARC = PermissibleValue(text="SPARC")
    x86 = PermissibleValue(text="x86")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweArchitectureName",
        description="A named hardware architecture.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Power Architecture",
            PermissibleValue(text="Power Architecture"))

class CweDetectionMethodName(EnumDefinitionImpl):
    """
    A way of finding a weakness.
    """
    Fuzzing = PermissibleValue(text="Fuzzing")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweDetectionMethodName",
        description="A way of finding a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Automated Analysis",
            PermissibleValue(text="Automated Analysis"))
        setattr(cls, "Automated Dynamic Analysis",
            PermissibleValue(text="Automated Dynamic Analysis"))
        setattr(cls, "Automated Static Analysis",
            PermissibleValue(text="Automated Static Analysis"))
        setattr(cls, "Automated Static Analysis - Source Code",
            PermissibleValue(text="Automated Static Analysis - Source Code"))
        setattr(cls, "Automated Static Analysis - Binary or Bytecode",
            PermissibleValue(text="Automated Static Analysis - Binary or Bytecode"))
        setattr(cls, "Manual Analysis",
            PermissibleValue(text="Manual Analysis"))
        setattr(cls, "Manual Dynamic Analysis",
            PermissibleValue(text="Manual Dynamic Analysis"))
        setattr(cls, "Manual Static Analysis",
            PermissibleValue(text="Manual Static Analysis"))
        setattr(cls, "Manual Static Analysis - Source Code",
            PermissibleValue(text="Manual Static Analysis - Source Code"))
        setattr(cls, "Manual Static Analysis - Binary or Bytecode",
            PermissibleValue(text="Manual Static Analysis - Binary or Bytecode"))
        setattr(cls, "White Box",
            PermissibleValue(text="White Box"))
        setattr(cls, "Black Box",
            PermissibleValue(text="Black Box"))
        setattr(cls, "Architecture or Design Review",
            PermissibleValue(text="Architecture or Design Review"))
        setattr(cls, "Dynamic Analysis with Manual Results Interpretation",
            PermissibleValue(text="Dynamic Analysis with Manual Results Interpretation"))
        setattr(cls, "Dynamic Analysis with Automated Results Interpretation",
            PermissibleValue(text="Dynamic Analysis with Automated Results Interpretation"))
        setattr(cls, "Formal Verification",
            PermissibleValue(text="Formal Verification"))
        setattr(cls, "Simulation / Emulation",
            PermissibleValue(text="Simulation / Emulation"))

class CweDetectionEffectiveness(EnumDefinitionImpl):
    """
    How well a detection method finds a weakness.
    """
    High = PermissibleValue(
        text="High",
        description="It finds the weakness often and with few false reports.")
    Moderate = PermissibleValue(
        text="Moderate",
        description="It works in several situations but misses some forms or gives some false reports.")
    Opportunistic = PermissibleValue(
        text="Opportunistic",
        description="It does not aim at this weakness and finds it only by the way.")
    Limited = PermissibleValue(
        text="Limited",
        description="It helps only in some situations.")

    _defn = EnumDefinition(
        name="CweDetectionEffectiveness",
        description="How well a detection method finds a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SOAR Partial",
            PermissibleValue(
                text="SOAR Partial",
                description="The State Of the Art Report rates it as cost-effective for part of the job."))
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="It does not find the weakness."))

class CweEffectiveness(EnumDefinitionImpl):
    """
    How well a mitigation prevents a weakness.
    """
    High = PermissibleValue(
        text="High",
        description="It often removes the weakness altogether.")
    Moderate = PermissibleValue(
        text="Moderate",
        description="It prevents several forms of the weakness but does not cover them all.")
    Limited = PermissibleValue(
        text="Limited",
        description="It helps only in some situations or against some forms of the weakness.")
    Incidental = PermissibleValue(
        text="Incidental",
        description="It protects by chance and cannot be relied on.")

    _defn = EnumDefinition(
        name="CweEffectiveness",
        description="How well a mitigation prevents a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Discouraged Common Practice",
            PermissibleValue(
                text="Discouraged Common Practice",
                description="A habit people often follow that does not work well enough to recommend."))
        setattr(cls, "Defense in Depth",
            PermissibleValue(
                text="Defense in Depth",
                description="It adds a layer of protection and does not remove the weakness by itself."))
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="It does not prevent the weakness."))

class CweFunctionalArea(EnumDefinitionImpl):
    """
    The part of a product where a weakness is most likely to appear.
    """
    Authentication = PermissibleValue(text="Authentication")
    Authorization = PermissibleValue(text="Authorization")
    Counters = PermissibleValue(text="Counters")
    Cryptography = PermissibleValue(text="Cryptography")
    Logging = PermissibleValue(text="Logging")
    Networking = PermissibleValue(text="Networking")
    Signals = PermissibleValue(text="Signals")
    Power = PermissibleValue(text="Power")
    Clock = PermissibleValue(text="Clock")

    _defn = EnumDefinition(
        name="CweFunctionalArea",
        description="The part of a product where a weakness is most likely to appear.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Code Libraries",
            PermissibleValue(text="Code Libraries"))
        setattr(cls, "Error Handling",
            PermissibleValue(text="Error Handling"))
        setattr(cls, "Interprocess Communication",
            PermissibleValue(text="Interprocess Communication"))
        setattr(cls, "File Processing",
            PermissibleValue(text="File Processing"))
        setattr(cls, "Memory Management",
            PermissibleValue(text="Memory Management"))
        setattr(cls, "Number Processing",
            PermissibleValue(text="Number Processing"))
        setattr(cls, "Program Invocation",
            PermissibleValue(text="Program Invocation"))
        setattr(cls, "Protection Mechanism",
            PermissibleValue(text="Protection Mechanism"))
        setattr(cls, "Session Management",
            PermissibleValue(text="Session Management"))
        setattr(cls, "String Processing",
            PermissibleValue(text="String Processing"))
        setattr(cls, "Not Functional-Area-Specific",
            PermissibleValue(text="Not Functional-Area-Specific"))

class CweImportance(EnumDefinitionImpl):
    """
    How much a change to an entry matters to people who already rely on it.
    """
    Normal = PermissibleValue(text="Normal")
    Critical = PermissibleValue(
        text="Critical",
        description="The change alters what the entry means or how it may be read.")

    _defn = EnumDefinition(
        name="CweImportance",
        description="How much a change to an entry matters to people who already rely on it.",
    )

class CweLanguageClass(EnumDefinitionImpl):
    """
    A broad family of programming languages.
    """
    Assembly = PermissibleValue(text="Assembly")
    Compiled = PermissibleValue(text="Compiled")
    Interpreted = PermissibleValue(text="Interpreted")

    _defn = EnumDefinition(
        name="CweLanguageClass",
        description="A broad family of programming languages.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hardware Description Language",
            PermissibleValue(text="Hardware Description Language"))
        setattr(cls, "Object-Oriented",
            PermissibleValue(text="Object-Oriented"))
        setattr(cls, "Memory-Unsafe",
            PermissibleValue(text="Memory-Unsafe"))
        setattr(cls, "Not Language-Specific",
            PermissibleValue(
                text="Not Language-Specific",
                description="The weakness can appear in many languages."))

class CweLanguageName(EnumDefinitionImpl):
    """
    A named programming language or notation.
    """
    Ada = PermissibleValue(text="Ada")
    Algorithm = PermissibleValue(text="Algorithm")
    ASP = PermissibleValue(text="ASP")
    Basic = PermissibleValue(text="Basic")
    C = PermissibleValue(text="C")
    COBOL = PermissibleValue(text="COBOL")
    Fortran = PermissibleValue(text="Fortran")
    Go = PermissibleValue(text="Go")
    HTML = PermissibleValue(text="HTML")
    Java = PermissibleValue(text="Java")
    JavaScript = PermissibleValue(text="JavaScript")
    JSON = PermissibleValue(text="JSON")
    JSP = PermissibleValue(text="JSP")
    Pascal = PermissibleValue(text="Pascal")
    Perl = PermissibleValue(text="Perl")
    PHP = PermissibleValue(text="PHP")
    Pseudocode = PermissibleValue(text="Pseudocode")
    Python = PermissibleValue(text="Python")
    Ruby = PermissibleValue(text="Ruby")
    Rust = PermissibleValue(text="Rust")
    Shell = PermissibleValue(text="Shell")
    SQL = PermissibleValue(text="SQL")
    Swift = PermissibleValue(text="Swift")
    SystemVerilog = PermissibleValue(text="SystemVerilog")
    Verilog = PermissibleValue(text="Verilog")
    VHDL = PermissibleValue(text="VHDL")
    XML = PermissibleValue(text="XML")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweLanguageName",
        description="A named programming language or notation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ARM Assembly",
            PermissibleValue(text="ARM Assembly"))
        setattr(cls, "ASP.NET",
            PermissibleValue(text="ASP.NET"))
        setattr(cls, "C++",
            PermissibleValue(
                text="C++",
                title="C plus plus"))
        setattr(cls, "C#",
            PermissibleValue(
                text="C#",
                title="C sharp"))
        setattr(cls, "F#",
            PermissibleValue(
                text="F#",
                title="F sharp"))
        setattr(cls, "Objective-C",
            PermissibleValue(text="Objective-C"))
        setattr(cls, "VB.NET",
            PermissibleValue(text="VB.NET"))
        setattr(cls, "x86 Assembly",
            PermissibleValue(text="x86 Assembly"))

class CweLikelihood(EnumDefinitionImpl):
    """
    How likely something is to happen.
    """
    High = PermissibleValue(text="High")
    Medium = PermissibleValue(text="Medium")
    Low = PermissibleValue(text="Low")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Nobody knows how likely it is.")

    _defn = EnumDefinition(
        name="CweLikelihood",
        description="How likely something is to happen.",
    )

class CweMitigationStrategy(EnumDefinitionImpl):
    """
    A general approach that a mitigation follows.
    """
    Firewall = PermissibleValue(text="Firewall")
    Parameterization = PermissibleValue(text="Parameterization")
    Refactoring = PermissibleValue(text="Refactoring")

    _defn = EnumDefinition(
        name="CweMitigationStrategy",
        description="A general approach that a mitigation follows.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Attack Surface Reduction",
            PermissibleValue(text="Attack Surface Reduction"))
        setattr(cls, "Compilation or Build Hardening",
            PermissibleValue(text="Compilation or Build Hardening"))
        setattr(cls, "Enforcement by Conversion",
            PermissibleValue(text="Enforcement by Conversion"))
        setattr(cls, "Environment Hardening",
            PermissibleValue(text="Environment Hardening"))
        setattr(cls, "Input Validation",
            PermissibleValue(text="Input Validation"))
        setattr(cls, "Language Selection",
            PermissibleValue(text="Language Selection"))
        setattr(cls, "Libraries or Frameworks",
            PermissibleValue(text="Libraries or Frameworks"))
        setattr(cls, "Resource Limitation",
            PermissibleValue(text="Resource Limitation"))
        setattr(cls, "Output Encoding",
            PermissibleValue(text="Output Encoding"))
        setattr(cls, "Sandbox or Jail",
            PermissibleValue(text="Sandbox or Jail"))
        setattr(cls, "Separation of Privilege",
            PermissibleValue(text="Separation of Privilege"))

class CweNoteType(EnumDefinitionImpl):
    """
    What a note on an entry is about.
    """
    Maintenance = PermissibleValue(
        text="Maintenance",
        description="Work the entry still needs, such as sharper concepts or better relationships.")
    Relationship = PermissibleValue(
        text="Relationship",
        description="More detail on how the entry relates to others.")
    Terminology = PermissibleValue(
        text="Terminology",
        description="A discussion of the words used for the weakness.")
    Theoretical = PermissibleValue(
        text="Theoretical",
        description="The weakness described in the terms of vulnerability theory.")
    Other = PermissibleValue(
        text="Other",
        description="Anything useful that fits no other type.")

    _defn = EnumDefinition(
        name="CweNoteType",
        description="What a note on an entry is about.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Applicable Platform",
            PermissibleValue(
                text="Applicable Platform",
                description="More detail on the platforms the entry lists."))
        setattr(cls, "Research Gap",
            PermissibleValue(
                text="Research Gap",
                description="A topic researchers have not yet explored enough."))

class CweOrdinal(EnumDefinitionImpl):
    """
    Marks the relationship to prefer among several in one view.
    """
    Primary = PermissibleValue(
        text="Primary",
        description="The relationship to follow first in that view.")

    _defn = EnumDefinition(
        name="CweOrdinal",
        description="Marks the relationship to prefer among several in one view.",
    )

class CweOrdinality(EnumDefinitionImpl):
    """
    How a weakness stands to other weaknesses in a sequence of causes.
    """
    Indirect = PermissibleValue(
        text="Indirect",
        description="A quality problem that makes other weaknesses easier to introduce or harder to find.")
    Primary = PermissibleValue(
        text="Primary",
        description="The weakness exists without depending on another one.")
    Resultant = PermissibleValue(
        text="Resultant",
        description="The weakness exists only because another one is present.")

    _defn = EnumDefinition(
        name="CweOrdinality",
        description="How a weakness stands to other weaknesses in a sequence of causes.",
    )

class CweOperatingSystemClass(EnumDefinitionImpl):
    """
    A broad family of operating systems.
    """
    Linux = PermissibleValue(text="Linux")
    macOS = PermissibleValue(text="macOS")
    Unix = PermissibleValue(text="Unix")
    Windows = PermissibleValue(text="Windows")

    _defn = EnumDefinition(
        name="CweOperatingSystemClass",
        description="A broad family of operating systems.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not OS-Specific",
            PermissibleValue(
                text="Not OS-Specific",
                description="The weakness can appear on many operating systems."))

class CweOperatingSystemName(EnumDefinitionImpl):
    """
    A named operating system.
    """
    AIX = PermissibleValue(text="AIX")
    Android = PermissibleValue(text="Android")
    Darwin = PermissibleValue(text="Darwin")
    FreeBSD = PermissibleValue(text="FreeBSD")
    iOS = PermissibleValue(text="iOS")
    macOS = PermissibleValue(text="macOS")
    NetBSD = PermissibleValue(text="NetBSD")
    OpenBSD = PermissibleValue(text="OpenBSD")
    Solaris = PermissibleValue(text="Solaris")
    SUSE = PermissibleValue(text="SUSE")
    tvOS = PermissibleValue(text="tvOS")
    Ubuntu = PermissibleValue(text="Ubuntu")
    watchOS = PermissibleValue(text="watchOS")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweOperatingSystemName",
        description="A named operating system.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "BlackBerry OS",
            PermissibleValue(text="BlackBerry OS"))
        setattr(cls, "Chrome OS",
            PermissibleValue(text="Chrome OS"))
        setattr(cls, "Red Hat",
            PermissibleValue(text="Red Hat"))
        setattr(cls, "Windows 9x",
            PermissibleValue(text="Windows 9x"))
        setattr(cls, "Windows Embedded",
            PermissibleValue(text="Windows Embedded"))
        setattr(cls, "Windows NT",
            PermissibleValue(text="Windows NT"))

class CwePhase(EnumDefinitionImpl):
    """
    A stage of a product life cycle.
    """
    Policy = PermissibleValue(text="Policy")
    Requirements = PermissibleValue(text="Requirements")
    Implementation = PermissibleValue(text="Implementation")
    Testing = PermissibleValue(text="Testing")
    Documentation = PermissibleValue(text="Documentation")
    Bundling = PermissibleValue(text="Bundling")
    Distribution = PermissibleValue(text="Distribution")
    Installation = PermissibleValue(text="Installation")
    Operation = PermissibleValue(text="Operation")
    Porting = PermissibleValue(text="Porting")
    Integration = PermissibleValue(text="Integration")
    Manufacturing = PermissibleValue(text="Manufacturing")

    _defn = EnumDefinition(
        name="CwePhase",
        description="A stage of a product life cycle.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Architecture and Design",
            PermissibleValue(text="Architecture and Design"))
        setattr(cls, "Build and Compilation",
            PermissibleValue(text="Build and Compilation"))
        setattr(cls, "System Configuration",
            PermissibleValue(text="System Configuration"))
        setattr(cls, "Patching and Maintenance",
            PermissibleValue(text="Patching and Maintenance"))
        setattr(cls, "Decommissioning and End-of-Life",
            PermissibleValue(text="Decommissioning and End-of-Life"))

class CweAiPhase(EnumDefinitionImpl):
    """
    A stage of the life cycle of an artificial intelligence system.
    """
    Training = PermissibleValue(text="Training")
    Testing = PermissibleValue(text="Testing")
    Tokenization = PermissibleValue(text="Tokenization")
    Prompting = PermissibleValue(text="Prompting")

    _defn = EnumDefinition(
        name="CweAiPhase",
        description="A stage of the life cycle of an artificial intelligence system.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data Collection",
            PermissibleValue(text="Data Collection"))
        setattr(cls, "Fine-tuning",
            PermissibleValue(text="Fine-tuning"))
        setattr(cls, "Output Processing",
            PermissibleValue(text="Output Processing"))
        setattr(cls, "Component Interaction",
            PermissibleValue(text="Component Interaction"))
        setattr(cls, "Re-training / Feedback",
            PermissibleValue(text="Re-training / Feedback"))

class CweHardwarePhase(EnumDefinitionImpl):
    """
    A stage of the life cycle of a hardware product.
    """
    Reuse = PermissibleValue(text="Reuse")
    Decommissioning = PermissibleValue(text="Decommissioning")

    _defn = EnumDefinition(
        name="CweHardwarePhase",
        description="A stage of the life cycle of a hardware product.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hardware Requirements",
            PermissibleValue(text="Hardware Requirements"))
        setattr(cls, "Hardware Architecture",
            PermissibleValue(text="Hardware Architecture"))
        setattr(cls, "Hardware Microarchitecture",
            PermissibleValue(text="Hardware Microarchitecture"))
        setattr(cls, "Implementation & Physical Design",
            PermissibleValue(text="Implementation & Physical Design"))
        setattr(cls, "Pre-Manufacturing Verification",
            PermissibleValue(text="Pre-Manufacturing Verification"))
        setattr(cls, "Hardware Manufacturing",
            PermissibleValue(text="Hardware Manufacturing"))
        setattr(cls, "Post-Manufacturing Validation",
            PermissibleValue(text="Post-Manufacturing Validation"))
        setattr(cls, "Device Configuration & Personalization",
            PermissibleValue(text="Device Configuration & Personalization"))
        setattr(cls, "Device / System Integration",
            PermissibleValue(text="Device / System Integration"))
        setattr(cls, "Field Operations & Sustainment",
            PermissibleValue(text="Field Operations & Sustainment"))

class CweCustomPhaseDomain(EnumDefinitionImpl):
    """
    The field whose own life cycle a custom phase belongs to.
    """
    AI = PermissibleValue(text="AI")
    Hardware = PermissibleValue(text="Hardware")

    _defn = EnumDefinition(
        name="CweCustomPhaseDomain",
        description="The field whose own life cycle a custom phase belongs to.",
    )

class CweDimensionType(EnumDefinitionImpl):
    """
    The aspect of a weakness that a dimension names, such as a behaviour or a resource.
    """
    Technology = PermissibleValue(text="Technology")
    Framework = PermissibleValue(text="Framework")
    Attack = PermissibleValue(text="Attack")
    Acronym = PermissibleValue(text="Acronym")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweDimensionType",
        description="The aspect of a weakness that a dimension names, such as a behaviour or a resource.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Behavior-Type",
            PermissibleValue(text="Behavior-Type"))
        setattr(cls, "Behavior-Property",
            PermissibleValue(text="Behavior-Property"))
        setattr(cls, "Resource-Type",
            PermissibleValue(text="Resource-Type"))
        setattr(cls, "Resource-Property",
            PermissibleValue(text="Resource-Property"))
        setattr(cls, "Input-Type",
            PermissibleValue(text="Input-Type"))
        setattr(cls, "Input-Property",
            PermissibleValue(text="Input-Property"))
        setattr(cls, "Info-Type",
            PermissibleValue(text="Info-Type"))
        setattr(cls, "Info-Property",
            PermissibleValue(text="Info-Property"))
        setattr(cls, "Code-Type",
            PermissibleValue(text="Code-Type"))
        setattr(cls, "Code-Property",
            PermissibleValue(text="Code-Property"))
        setattr(cls, "Language-Type",
            PermissibleValue(text="Language-Type"))
        setattr(cls, "Language-Property",
            PermissibleValue(text="Language-Property"))
        setattr(cls, "Common-Name",
            PermissibleValue(text="Common-Name"))

class CwePrevalence(EnumDefinitionImpl):
    """
    How regularly a weakness applies to a platform.
    """
    Often = PermissibleValue(text="Often")
    Sometimes = PermissibleValue(text="Sometimes")
    Rarely = PermissibleValue(text="Rarely")
    Undetermined = PermissibleValue(text="Undetermined")

    _defn = EnumDefinition(
        name="CwePrevalence",
        description="How regularly a weakness applies to a platform.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(text="None"))

class CweReason(EnumDefinitionImpl):
    """
    A short label for why an entry may not suit vulnerability mapping.
    """
    Abstraction = PermissibleValue(text="Abstraction")
    Category = PermissibleValue(text="Category")
    Grouping = PermissibleValue(text="Grouping")
    View = PermissibleValue(text="View")
    Deprecated = PermissibleValue(text="Deprecated")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweReason",
        description="A short label for why an entry may not suit vulnerability mapping.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Potential Deprecation",
            PermissibleValue(text="Potential Deprecation"))
        setattr(cls, "Frequent Misuse",
            PermissibleValue(text="Frequent Misuse"))
        setattr(cls, "Frequent Misinterpretation",
            PermissibleValue(text="Frequent Misinterpretation"))
        setattr(cls, "Multiple Use",
            PermissibleValue(text="Multiple Use"))
        setattr(cls, "CWE Overlap",
            PermissibleValue(text="CWE Overlap"))
        setattr(cls, "Acceptable-Use",
            PermissibleValue(text="Acceptable-Use"))
        setattr(cls, "Frequently-Resultant",
            PermissibleValue(text="Frequently-Resultant"))
        setattr(cls, "Potential Major Changes",
            PermissibleValue(text="Potential Major Changes"))

class CweRelatedNature(EnumDefinitionImpl):
    """
    How one weakness relates to another.
    """
    ChildOf = PermissibleValue(
        text="ChildOf",
        description="The related weakness is more general than this one.")
    ParentOf = PermissibleValue(
        text="ParentOf",
        description="The related weakness is more specific than this one.")
    StartsWith = PermissibleValue(
        text="StartsWith",
        description="For a named chain only: the related weakness is where the chain begins.")
    CanFollow = PermissibleValue(
        text="CanFollow",
        description="In a chain, the related weakness can come before this one.")
    CanPrecede = PermissibleValue(
        text="CanPrecede",
        description="In a chain, the related weakness can come after this one.")
    RequiredBy = PermissibleValue(
        text="RequiredBy",
        description="For composites only: the related composite needs this weakness to be present.")
    Requires = PermissibleValue(
        text="Requires",
        description="For composites only: this composite needs the related weakness to be present.")
    CanAlsoBe = PermissibleValue(
        text="CanAlsoBe",
        description="""In some settings this weakness may be seen as the related one, with neither being a parent of the other.""")
    PeerOf = PermissibleValue(
        text="PeerOf",
        description="The two are similar in a way that no other nature fits.")
    Overlaps = PermissibleValue(
        text="Overlaps",
        description="The two weaknesses share some ground, which CWE would rather avoid.")

    _defn = EnumDefinition(
        name="CweRelatedNature",
        description="How one weakness relates to another.",
    )

class CweResource(EnumDefinitionImpl):
    """
    A kind of system resource that exploiting a weakness can affect.
    """
    CPU = PermissibleValue(text="CPU")
    Memory = PermissibleValue(text="Memory")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweResource",
        description="A kind of system resource that exploiting a weakness can affect.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "File or Directory",
            PermissibleValue(text="File or Directory"))
        setattr(cls, "System Process",
            PermissibleValue(text="System Process"))

class CweScope(EnumDefinitionImpl):
    """
    The security property a consequence violates.
    """
    Confidentiality = PermissibleValue(text="Confidentiality")
    Integrity = PermissibleValue(text="Integrity")
    Availability = PermissibleValue(text="Availability")
    Accountability = PermissibleValue(text="Accountability")
    Authentication = PermissibleValue(text="Authentication")
    Authorization = PermissibleValue(text="Authorization")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweScope",
        description="The security property a consequence violates.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Access Control",
            PermissibleValue(text="Access Control"))
        setattr(cls, "Non-Repudiation",
            PermissibleValue(text="Non-Repudiation"))

class CweStatus(EnumDefinitionImpl):
    """
    How far an entry has come in its life and how much it can be trusted.
    """
    Deprecated = PermissibleValue(
        text="Deprecated",
        description="Taken out of CWE, usually because it duplicated another entry or was made by mistake.")
    Draft = PermissibleValue(
        text="Draft",
        description="Its important elements are filled in and readable, though it may still have problems.")
    Incomplete = PermissibleValue(
        text="Incomplete",
        description="Some important elements are missing and its quality is not assured.")
    Obsolete = PermissibleValue(
        text="Obsolete",
        description="Still correct but no longer relevant, usually because a newer entry replaced it.")
    Stable = PermissibleValue(
        text="Stable",
        description="Its important elements have been checked and are not expected to change much.")
    Usable = PermissibleValue(
        text="Usable",
        description="It has had close review and its critical elements have been checked.")

    _defn = EnumDefinition(
        name="CweStatus",
        description="How far an entry has come in its life and how much it can be trusted.",
    )

class CweStakeholderType(EnumDefinitionImpl):
    """
    A group of people who may have a use for a view.
    """
    Educators = PermissibleValue(text="Educators")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweStakeholderType",
        description="A group of people who may have a use for a view.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Academic Researchers",
            PermissibleValue(text="Academic Researchers"))
        setattr(cls, "Applied Researchers",
            PermissibleValue(text="Applied Researchers"))
        setattr(cls, "Assessment Teams",
            PermissibleValue(text="Assessment Teams"))
        setattr(cls, "Assessment Tool Vendors",
            PermissibleValue(text="Assessment Tool Vendors"))
        setattr(cls, "CWE Team",
            PermissibleValue(text="CWE Team"))
        setattr(cls, "Hardware Designers",
            PermissibleValue(text="Hardware Designers"))
        setattr(cls, "Information Providers",
            PermissibleValue(text="Information Providers"))
        setattr(cls, "Product Customers",
            PermissibleValue(text="Product Customers"))
        setattr(cls, "Product Vendors",
            PermissibleValue(text="Product Vendors"))
        setattr(cls, "Software Developers",
            PermissibleValue(text="Software Developers"))
        setattr(cls, "Vulnerability Analysts",
            PermissibleValue(text="Vulnerability Analysts"))

class CweStructure(EnumDefinitionImpl):
    """
    Whether a weakness stands alone or is made up of others.
    """
    Chain = PermissibleValue(
        text="Chain",
        description="Several weaknesses that must be reached one after another to give a vulnerability.")
    Composite = PermissibleValue(
        text="Composite",
        description="Several weaknesses that give a vulnerability only when they occur together.")
    Simple = PermissibleValue(
        text="Simple",
        description="One weakness whose exploitation does not depend on another.")

    _defn = EnumDefinition(
        name="CweStructure",
        description="Whether a weakness stands alone or is made up of others.",
    )

class CweCodeNature(EnumDefinitionImpl):
    """
    What a block of example code shows.
    """
    Attack = PermissibleValue(
        text="Attack",
        description="An attack against the code.")
    Bad = PermissibleValue(
        text="Bad",
        description="Code that has the weakness.")
    Good = PermissibleValue(
        text="Good",
        description="Code that avoids the weakness.")
    Informative = PermissibleValue(
        text="Informative",
        description="Background that shows neither good nor bad code.")
    Mitigation = PermissibleValue(
        text="Mitigation",
        description="A way of addressing the weakness.")
    Result = PermissibleValue(
        text="Result",
        description="What running the code produces.")

    _defn = EnumDefinition(
        name="CweCodeNature",
        description="What a block of example code shows.",
    )

class CweMappingFit(EnumDefinitionImpl):
    """
    How closely a CWE entry matches an entry of another taxonomy.
    """
    Exact = PermissibleValue(text="Exact")
    Imprecise = PermissibleValue(
        text="Imprecise",
        description="The two match only loosely.")
    Perspective = PermissibleValue(
        text="Perspective",
        description="The two look at the same matter from different angles.")

    _defn = EnumDefinition(
        name="CweMappingFit",
        description="How closely a CWE entry matches an entry of another taxonomy.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CWE More Abstract",
            PermissibleValue(
                text="CWE More Abstract",
                description="The CWE entry is more general than the other."))
        setattr(cls, "CWE More Specific",
            PermissibleValue(
                text="CWE More Specific",
                description="The CWE entry is narrower than the other."))

class CweTaxonomyName(EnumDefinitionImpl):
    """
    A taxonomy that CWE entries are mapped to.
    """
    Aslam = PermissibleValue(text="Aslam")
    Bishop = PermissibleValue(text="Bishop")
    CLASP = PermissibleValue(text="CLASP")
    Landwehr = PermissibleValue(text="Landwehr")
    PLOVER = PermissibleValue(text="PLOVER")
    RISOS = PermissibleValue(text="RISOS")
    WASC = PermissibleValue(text="WASC")

    _defn = EnumDefinition(
        name="CweTaxonomyName",
        description="A taxonomy that CWE entries are mapped to.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "7 Pernicious Kingdoms",
            PermissibleValue(
                text="7 Pernicious Kingdoms",
                title="Seven Pernicious Kingdoms"))
        setattr(cls, "19 Deadly Sins",
            PermissibleValue(
                text="19 Deadly Sins",
                title="Nineteen Deadly Sins"))
        setattr(cls, "CERT C Secure Coding",
            PermissibleValue(text="CERT C Secure Coding"))
        setattr(cls, "CERT C++ Secure Coding",
            PermissibleValue(text="CERT C++ Secure Coding"))
        setattr(cls, "The CERT Oracle Secure Coding Standard for Java (2011)",
            PermissibleValue(text="The CERT Oracle Secure Coding Standard for Java (2011)"))
        setattr(cls, "ISA/IEC 62443",
            PermissibleValue(text="ISA/IEC 62443"))
        setattr(cls, "OMG ASCSM",
            PermissibleValue(text="OMG ASCSM"))
        setattr(cls, "OMG ASCRM",
            PermissibleValue(text="OMG ASCRM"))
        setattr(cls, "OMG ASCMM",
            PermissibleValue(text="OMG ASCMM"))
        setattr(cls, "OMG ASCPEM",
            PermissibleValue(text="OMG ASCPEM"))
        setattr(cls, "OpenSSF Secure Coding Guide for Python",
            PermissibleValue(text="OpenSSF Secure Coding Guide for Python"))
        setattr(cls, "OWASP Golang Secure Coding Practices Guide",
            PermissibleValue(text="OWASP Golang Secure Coding Practices Guide"))
        setattr(cls, "OWASP Top Ten 2004",
            PermissibleValue(text="OWASP Top Ten 2004"))
        setattr(cls, "OWASP Top Ten 2007",
            PermissibleValue(text="OWASP Top Ten 2007"))
        setattr(cls, "OWASP Top Ten",
            PermissibleValue(text="OWASP Top Ten"))
        setattr(cls, "PLC Top 20",
            PermissibleValue(text="PLC Top 20"))
        setattr(cls, "Protection Analysis",
            PermissibleValue(text="Protection Analysis"))
        setattr(cls, "SEI CERT C Coding Standard",
            PermissibleValue(text="SEI CERT C Coding Standard"))
        setattr(cls, "SEI CERT C++ Coding Standard",
            PermissibleValue(text="SEI CERT C++ Coding Standard"))
        setattr(cls, "SEI CERT Oracle Coding Standard for Java",
            PermissibleValue(text="SEI CERT Oracle Coding Standard for Java"))
        setattr(cls, "SEI CERT Perl Coding Standard",
            PermissibleValue(text="SEI CERT Perl Coding Standard"))
        setattr(cls, "Software Fault Patterns",
            PermissibleValue(text="Software Fault Patterns"))
        setattr(cls, "Weber, Karger, Paradkar",
            PermissibleValue(text="Weber, Karger, Paradkar"))

class CweTechnicalImpact(EnumDefinitionImpl):
    """
    What an attacker can achieve by exploiting a weakness.
    """
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweTechnicalImpact",
        description="What an attacker can achieve by exploiting a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Modify Memory",
            PermissibleValue(text="Modify Memory"))
        setattr(cls, "Read Memory",
            PermissibleValue(text="Read Memory"))
        setattr(cls, "Modify Files or Directories",
            PermissibleValue(text="Modify Files or Directories"))
        setattr(cls, "Read Files or Directories",
            PermissibleValue(text="Read Files or Directories"))
        setattr(cls, "Modify Application Data",
            PermissibleValue(text="Modify Application Data"))
        setattr(cls, "Read Application Data",
            PermissibleValue(text="Read Application Data"))
        setattr(cls, "DoS: Crash, Exit, or Restart",
            PermissibleValue(text="DoS: Crash, Exit, or Restart"))
        setattr(cls, "DoS: Amplification",
            PermissibleValue(text="DoS: Amplification"))
        setattr(cls, "DoS: Instability",
            PermissibleValue(text="DoS: Instability"))
        setattr(cls, "DoS: Prevent Access",
            PermissibleValue(text="DoS: Prevent Access"))
        setattr(cls, "DoS: Resource Consumption (CPU)",
            PermissibleValue(text="DoS: Resource Consumption (CPU)"))
        setattr(cls, "DoS: Resource Consumption (Memory)",
            PermissibleValue(text="DoS: Resource Consumption (Memory)"))
        setattr(cls, "DoS: Resource Consumption (Other)",
            PermissibleValue(text="DoS: Resource Consumption (Other)"))
        setattr(cls, "DoS: Other",
            PermissibleValue(text="DoS: Other"))
        setattr(cls, "Execute Unauthorized Code or Commands",
            PermissibleValue(text="Execute Unauthorized Code or Commands"))
        setattr(cls, "Gain Privileges or Assume Identity",
            PermissibleValue(text="Gain Privileges or Assume Identity"))
        setattr(cls, "Bypass Protection Mechanism",
            PermissibleValue(text="Bypass Protection Mechanism"))
        setattr(cls, "Hide Activities",
            PermissibleValue(text="Hide Activities"))
        setattr(cls, "Alter Execution Logic",
            PermissibleValue(text="Alter Execution Logic"))
        setattr(cls, "Undefined Behavior",
            PermissibleValue(text="Undefined Behavior"))
        setattr(cls, "Quality Degradation",
            PermissibleValue(text="Quality Degradation"))
        setattr(cls, "Unexpected State",
            PermissibleValue(text="Unexpected State"))
        setattr(cls, "Varies by Context",
            PermissibleValue(text="Varies by Context"))
        setattr(cls, "Increase Analytical Complexity",
            PermissibleValue(text="Increase Analytical Complexity"))
        setattr(cls, "Reduce Maintainability",
            PermissibleValue(text="Reduce Maintainability"))
        setattr(cls, "Reduce Performance",
            PermissibleValue(text="Reduce Performance"))
        setattr(cls, "Reduce Reliability",
            PermissibleValue(text="Reduce Reliability"))

class CweTechnologyClass(EnumDefinitionImpl):
    """
    A broad family of technologies.
    """
    Mainframe = PermissibleValue(text="Mainframe")
    Mobile = PermissibleValue(text="Mobile")
    SOA = PermissibleValue(text="SOA")

    _defn = EnumDefinition(
        name="CweTechnologyClass",
        description="A broad family of technologies.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Client Server",
            PermissibleValue(text="Client Server"))
        setattr(cls, "Cloud Computing",
            PermissibleValue(text="Cloud Computing"))
        setattr(cls, "ICS/OT",
            PermissibleValue(text="ICS/OT"))
        setattr(cls, "N-Tier",
            PermissibleValue(text="N-Tier"))
        setattr(cls, "System on Chip",
            PermissibleValue(text="System on Chip"))
        setattr(cls, "Web Based",
            PermissibleValue(text="Web Based"))
        setattr(cls, "Not Technology-Specific",
            PermissibleValue(
                text="Not Technology-Specific",
                description="The weakness can appear in many technologies."))

class CweTechnologyName(EnumDefinitionImpl):
    """
    A named technology.
    """
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweTechnologyName",
        description="A named technology.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AI/ML",
            PermissibleValue(text="AI/ML"))
        setattr(cls, "Web Server",
            PermissibleValue(text="Web Server"))
        setattr(cls, "Database Server",
            PermissibleValue(text="Database Server"))
        setattr(cls, "Accelerator Hardware",
            PermissibleValue(text="Accelerator Hardware"))
        setattr(cls, "Analog and Mixed Signal Hardware",
            PermissibleValue(text="Analog and Mixed Signal Hardware"))
        setattr(cls, "Audio/Video Hardware",
            PermissibleValue(text="Audio/Video Hardware"))
        setattr(cls, "Bus/Interface Hardware",
            PermissibleValue(text="Bus/Interface Hardware"))
        setattr(cls, "Clock/Counter Hardware",
            PermissibleValue(text="Clock/Counter Hardware"))
        setattr(cls, "Communication Hardware",
            PermissibleValue(text="Communication Hardware"))
        setattr(cls, "Controller Hardware",
            PermissibleValue(text="Controller Hardware"))
        setattr(cls, "Memory Hardware",
            PermissibleValue(text="Memory Hardware"))
        setattr(cls, "Microcontroller Hardware",
            PermissibleValue(text="Microcontroller Hardware"))
        setattr(cls, "Network on Chip Hardware",
            PermissibleValue(text="Network on Chip Hardware"))
        setattr(cls, "Power Management Hardware",
            PermissibleValue(text="Power Management Hardware"))
        setattr(cls, "Processor Hardware",
            PermissibleValue(text="Processor Hardware"))
        setattr(cls, "Security Hardware",
            PermissibleValue(text="Security Hardware"))
        setattr(cls, "Sensor Hardware",
            PermissibleValue(text="Sensor Hardware"))
        setattr(cls, "Storage Hardware",
            PermissibleValue(text="Storage Hardware"))
        setattr(cls, "Test/Debug Hardware",
            PermissibleValue(text="Test/Debug Hardware"))

class CweUsage(EnumDefinitionImpl):
    """
    Whether an entry may be used when mapping a real vulnerability to its root cause.
    """
    Discouraged = PermissibleValue(
        text="Discouraged",
        description="It should not be used for mapping.")
    Prohibited = PermissibleValue(
        text="Prohibited",
        description="It must not be used for mapping.")
    Allowed = PermissibleValue(
        text="Allowed",
        description="It may be used for mapping.")

    _defn = EnumDefinition(
        name="CweUsage",
        description="Whether an entry may be used when mapping a real vulnerability to its root cause.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Allowed-with-Review",
            PermissibleValue(
                text="Allowed-with-Review",
                description="It may be used for mapping only in limited situations and after careful review."))

class CweViewType(EnumDefinitionImpl):
    """
    How a view selects and arranges its entries.
    """
    Implicit = PermissibleValue(
        text="Implicit",
        description="A flat list that a filter selects.")
    Explicit = PermissibleValue(
        text="Explicit",
        description="A flat list whose members are named one by one.")
    Graph = PermissibleValue(
        text="Graph",
        description="A hierarchy of entries from one point of view.")

    _defn = EnumDefinition(
        name="CweViewType",
        description="How a view selects and arranges its entries.",
    )

class CweObservedExampleRationale(EnumDefinitionImpl):
    """
    A hint at why an observed example was chosen for an entry.
    """
    Chain = PermissibleValue(text="Chain")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweObservedExampleRationale",
        description="A hint at why an observed example was chosen for an entry.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Early-Publication",
            PermissibleValue(
                text="Early-Publication",
                description="One of the earliest examples recognised as showing this weakness."))
        setattr(cls, "Influential/Newsworthy",
            PermissibleValue(
                text="Influential/Newsworthy",
                description="An example that drew attention or shaped how people see this weakness."))
        setattr(cls, "Language-Variety",
            PermissibleValue(text="Language-Variety"))
        setattr(cls, "Product-Variety",
            PermissibleValue(text="Product-Variety"))
        setattr(cls, "Attack-Surface",
            PermissibleValue(text="Attack-Surface"))

class CweReferenceAccessRestriction(EnumDefinitionImpl):
    """
    What stands between a reader and a cited source.
    """
    Removed = PermissibleValue(
        text="Removed",
        description="It has been taken down and may have no other copy.")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweReferenceAccessRestriction",
        description="What stands between a reader and a cited source.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="Anybody on the internet can read it for free."))
        setattr(cls, "Proprietary-Subscription",
            PermissibleValue(
                text="Proprietary-Subscription",
                description="Only paying subscribers can read it."))
        setattr(cls, "Minimal-Registration",
            PermissibleValue(
                text="Minimal-Registration",
                description="A reader must register, at no cost, to read it."))

class CweReferenceMediaType(EnumDefinitionImpl):
    """
    The form a cited source takes, which affects how easily people can use it.
    """
    Text = PermissibleValue(
        text="Text",
        description="Plain text or a format that is easy to parse, as HTML with no scripts is.")
    Video = PermissibleValue(
        text="Video",
        description="A recording with pictures, such as a conference talk.")
    Audio = PermissibleValue(
        text="Audio",
        description="A recording with sound and no pictures.")
    Other = PermissibleValue(
        text="Other",
        description="Some other format, which may be harder for some readers to use.")

    _defn = EnumDefinition(
        name="CweReferenceMediaType",
        description="The form a cited source takes, which affects how easily people can use it.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Common-Proprietary-Text",
            PermissibleValue(
                text="Common-Proprietary-Text",
                description="A widely used proprietary format for text, such as PDF or a word processor file."))

class CweReferenceRationale(EnumDefinitionImpl):
    """
    A hint at why a source was cited.
    """
    Example = PermissibleValue(
        text="Example",
        description="It gives more detail on an example in the entry, and may be where the example came from.")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CweReferenceRationale",
        description="A hint at why a source was cited.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Early-Publication",
            PermissibleValue(
                text="Early-Publication",
                description="One of the first publications to explain the weakness or how it is exploited."))
        setattr(cls, "Influential/Newsworthy",
            PermissibleValue(
                text="Influential/Newsworthy",
                description="A publication that drew attention or shaped how people see the weakness."))
        setattr(cls, "Manual/Man Pages",
            PermissibleValue(
                text="Manual/Man Pages",
                description="""Technical reference material that gives background and is not about the weakness itself."""))
        setattr(cls, "Mitigation-Based",
            PermissibleValue(
                text="Mitigation-Based",
                description="It proposes ways to reduce or remove weaknesses across a whole system."))
        setattr(cls, "Secure-Development-Rules",
            PermissibleValue(
                text="Secure-Development-Rules",
                description="It points to formal rules or guides for developing securely."))

class CweContributionType(EnumDefinitionImpl):
    """
    What a contribution to an entry consisted of.
    """
    Content = PermissibleValue(
        text="Content",
        description="Content given to the entry.")
    Feedback = PermissibleValue(
        text="Feedback",
        description="Feedback on the entry.")

    _defn = EnumDefinition(
        name="CweContributionType",
        description="What a contribution to an entry consisted of.",
    )

# Slots
class slots:
    pass

slots.cweWeaknessCatalog__Name = Slot(uri=CWE.Name, name="cweWeaknessCatalog__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweWeaknessCatalog__Name, domain=None, range=str)

slots.cweWeaknessCatalog__Version = Slot(uri=CWE.Version, name="cweWeaknessCatalog__Version", curie=CWE.curie('Version'),
                   model_uri=CWE.cweWeaknessCatalog__Version, domain=None, range=str)

slots.cweWeaknessCatalog__Date = Slot(uri=CWE.Date, name="cweWeaknessCatalog__Date", curie=CWE.curie('Date'),
                   model_uri=CWE.cweWeaknessCatalog__Date, domain=None, range=Union[str, XSDDate])

slots.cweWeaknessCatalog__Weaknesses = Slot(uri=CWE.Weaknesses, name="cweWeaknessCatalog__Weaknesses", curie=CWE.curie('Weaknesses'),
                   model_uri=CWE.cweWeaknessCatalog__Weaknesses, domain=None, range=Optional[Union[dict[Union[str, CweWeaknessID], Union[dict, CweWeakness]], list[Union[dict, CweWeakness]]]])

slots.cweWeaknessCatalog__Groupings = Slot(uri=CWE.Groupings, name="cweWeaknessCatalog__Groupings", curie=CWE.curie('Groupings'),
                   model_uri=CWE.cweWeaknessCatalog__Groupings, domain=None, range=Optional[Union[dict[Union[str, CweGroupingID], Union[dict, CweGrouping]], list[Union[dict, CweGrouping]]]])

slots.cweWeaknessCatalog__Views = Slot(uri=CWE.Views, name="cweWeaknessCatalog__Views", curie=CWE.curie('Views'),
                   model_uri=CWE.cweWeaknessCatalog__Views, domain=None, range=Optional[Union[dict[Union[str, CweViewID], Union[dict, CweView]], list[Union[dict, CweView]]]])

slots.cweWeaknessCatalog__External_References = Slot(uri=CWE.External_References, name="cweWeaknessCatalog__External_References", curie=CWE.curie('External_References'),
                   model_uri=CWE.cweWeaknessCatalog__External_References, domain=None, range=Optional[Union[dict[Union[str, CweExternalReferenceReferenceID], Union[dict, CweExternalReference]], list[Union[dict, CweExternalReference]]]])

slots.cweExternalReference__Reference_ID = Slot(uri=CWE.Reference_ID, name="cweExternalReference__Reference_ID", curie=CWE.curie('Reference_ID'),
                   model_uri=CWE.cweExternalReference__Reference_ID, domain=None, range=URIRef)

slots.cweExternalReference__Author = Slot(uri=CWE.Author, name="cweExternalReference__Author", curie=CWE.curie('Author'),
                   model_uri=CWE.cweExternalReference__Author, domain=None, range=Optional[Union[str, list[str]]])

slots.cweExternalReference__Title = Slot(uri=CWE.Title, name="cweExternalReference__Title", curie=CWE.curie('Title'),
                   model_uri=CWE.cweExternalReference__Title, domain=None, range=str)

slots.cweExternalReference__Edition = Slot(uri=CWE.Edition, name="cweExternalReference__Edition", curie=CWE.curie('Edition'),
                   model_uri=CWE.cweExternalReference__Edition, domain=None, range=Optional[str])

slots.cweExternalReference__Publication = Slot(uri=CWE.Publication, name="cweExternalReference__Publication", curie=CWE.curie('Publication'),
                   model_uri=CWE.cweExternalReference__Publication, domain=None, range=Optional[str])

slots.cweExternalReference__Publication_Year = Slot(uri=CWE.Publication_Year, name="cweExternalReference__Publication_Year", curie=CWE.curie('Publication_Year'),
                   model_uri=CWE.cweExternalReference__Publication_Year, domain=None, range=Optional[Union[str, CwePublicationYear]])

slots.cweExternalReference__Publication_Month = Slot(uri=CWE.Publication_Month, name="cweExternalReference__Publication_Month", curie=CWE.curie('Publication_Month'),
                   model_uri=CWE.cweExternalReference__Publication_Month, domain=None, range=Optional[Union[str, CwePublicationMonth]])

slots.cweExternalReference__Publication_Day = Slot(uri=CWE.Publication_Day, name="cweExternalReference__Publication_Day", curie=CWE.curie('Publication_Day'),
                   model_uri=CWE.cweExternalReference__Publication_Day, domain=None, range=Optional[Union[str, CwePublicationDay]])

slots.cweExternalReference__Publisher = Slot(uri=CWE.Publisher, name="cweExternalReference__Publisher", curie=CWE.curie('Publisher'),
                   model_uri=CWE.cweExternalReference__Publisher, domain=None, range=Optional[str])

slots.cweExternalReference__URL = Slot(uri=CWE.URL, name="cweExternalReference__URL", curie=CWE.curie('URL'),
                   model_uri=CWE.cweExternalReference__URL, domain=None, range=Optional[Union[str, URI]])

slots.cweExternalReference__URL_Date = Slot(uri=CWE.URL_Date, name="cweExternalReference__URL_Date", curie=CWE.curie('URL_Date'),
                   model_uri=CWE.cweExternalReference__URL_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.cweExternalReference__Alt_URL = Slot(uri=CWE.Alt_URL, name="cweExternalReference__Alt_URL", curie=CWE.curie('Alt_URL'),
                   model_uri=CWE.cweExternalReference__Alt_URL, domain=None, range=Optional[Union[str, URI]])

slots.cweExternalReference__Alt_URL_Date = Slot(uri=CWE.Alt_URL_Date, name="cweExternalReference__Alt_URL_Date", curie=CWE.curie('Alt_URL_Date'),
                   model_uri=CWE.cweExternalReference__Alt_URL_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.cweExternalReference__Media_Type = Slot(uri=CWE.Media_Type, name="cweExternalReference__Media_Type", curie=CWE.curie('Media_Type'),
                   model_uri=CWE.cweExternalReference__Media_Type, domain=None, range=Optional[Union[Union[str, "CweReferenceMediaType"], list[Union[str, "CweReferenceMediaType"]]]])

slots.cweExternalReference__Access_Restrictions = Slot(uri=CWE.Access_Restrictions, name="cweExternalReference__Access_Restrictions", curie=CWE.curie('Access_Restrictions'),
                   model_uri=CWE.cweExternalReference__Access_Restrictions, domain=None, range=Optional[Union[str, "CweReferenceAccessRestriction"]])

slots.cweExternalReference__Rationale = Slot(uri=CWE.Rationale, name="cweExternalReference__Rationale", curie=CWE.curie('Rationale'),
                   model_uri=CWE.cweExternalReference__Rationale, domain=None, range=Optional[Union[Union[str, "CweReferenceRationale"], list[Union[str, "CweReferenceRationale"]]]])

slots.cweReference__External_Reference_ID = Slot(uri=CWE.External_Reference_ID, name="cweReference__External_Reference_ID", curie=CWE.curie('External_Reference_ID'),
                   model_uri=CWE.cweReference__External_Reference_ID, domain=None, range=Union[str, CweExternalReferenceReferenceID])

slots.cweReference__Section = Slot(uri=CWE.Section, name="cweReference__Section", curie=CWE.curie('Section'),
                   model_uri=CWE.cweReference__Section, domain=None, range=Optional[str])

slots.cweDimension__Type = Slot(uri=CWE.Type, name="cweDimension__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweDimension__Type, domain=None, range=Union[str, "CweDimensionType"])

slots.cweDimension__Value = Slot(uri=CWE.Value, name="cweDimension__Value", curie=CWE.curie('Value'),
                   model_uri=CWE.cweDimension__Value, domain=None, range=str)

slots.cweCustomPhase__Domain = Slot(uri=CWE.Domain, name="cweCustomPhase__Domain", curie=CWE.curie('Domain'),
                   model_uri=CWE.cweCustomPhase__Domain, domain=None, range=Union[str, "CweCustomPhaseDomain"])

slots.cweCustomPhase__Value = Slot(uri=CWE.Value, name="cweCustomPhase__Value", curie=CWE.curie('Value'),
                   model_uri=CWE.cweCustomPhase__Value, domain=None, range=Union[str, "CweAiPhase", "CweHardwarePhase"])

slots.cweNote__Type = Slot(uri=CWE.Type, name="cweNote__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweNote__Type, domain=None, range=Union[str, "CweNoteType"])

slots.cweNote__Version = Slot(uri=CWE.Version, name="cweNote__Version", curie=CWE.curie('Version'),
                   model_uri=CWE.cweNote__Version, domain=None, range=Optional[str])

slots.cweNote__ReleaseDate = Slot(uri=CWE.ReleaseDate, name="cweNote__ReleaseDate", curie=CWE.curie('ReleaseDate'),
                   model_uri=CWE.cweNote__ReleaseDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.cweNote__Value = Slot(uri=CWE.Value, name="cweNote__Value", curie=CWE.curie('Value'),
                   model_uri=CWE.cweNote__Value, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweTaxonomyMapping__Taxonomy_Name = Slot(uri=CWE.Taxonomy_Name, name="cweTaxonomyMapping__Taxonomy_Name", curie=CWE.curie('Taxonomy_Name'),
                   model_uri=CWE.cweTaxonomyMapping__Taxonomy_Name, domain=None, range=Union[str, "CweTaxonomyName"])

slots.cweTaxonomyMapping__Entry_ID = Slot(uri=CWE.Entry_ID, name="cweTaxonomyMapping__Entry_ID", curie=CWE.curie('Entry_ID'),
                   model_uri=CWE.cweTaxonomyMapping__Entry_ID, domain=None, range=Optional[str])

slots.cweTaxonomyMapping__Entry_Name = Slot(uri=CWE.Entry_Name, name="cweTaxonomyMapping__Entry_Name", curie=CWE.curie('Entry_Name'),
                   model_uri=CWE.cweTaxonomyMapping__Entry_Name, domain=None, range=Optional[str])

slots.cweTaxonomyMapping__Mapping_Fit = Slot(uri=CWE.Mapping_Fit, name="cweTaxonomyMapping__Mapping_Fit", curie=CWE.curie('Mapping_Fit'),
                   model_uri=CWE.cweTaxonomyMapping__Mapping_Fit, domain=None, range=Optional[Union[str, "CweMappingFit"]])

slots.cweContentHistory__Submission = Slot(uri=CWE.Submission, name="cweContentHistory__Submission", curie=CWE.curie('Submission'),
                   model_uri=CWE.cweContentHistory__Submission, domain=None, range=Union[Union[dict, CweSubmission], list[Union[dict, CweSubmission]]])

slots.cweContentHistory__Modification = Slot(uri=CWE.Modification, name="cweContentHistory__Modification", curie=CWE.curie('Modification'),
                   model_uri=CWE.cweContentHistory__Modification, domain=None, range=Optional[Union[Union[dict, CweModification], list[Union[dict, CweModification]]]])

slots.cweContentHistory__Contribution = Slot(uri=CWE.Contribution, name="cweContentHistory__Contribution", curie=CWE.curie('Contribution'),
                   model_uri=CWE.cweContentHistory__Contribution, domain=None, range=Optional[Union[Union[dict, CweContribution], list[Union[dict, CweContribution]]]])

slots.cweContentHistory__Previous_Entry_Name = Slot(uri=CWE.Previous_Entry_Name, name="cweContentHistory__Previous_Entry_Name", curie=CWE.curie('Previous_Entry_Name'),
                   model_uri=CWE.cweContentHistory__Previous_Entry_Name, domain=None, range=Optional[Union[Union[dict, CwePreviousEntryName], list[Union[dict, CwePreviousEntryName]]]])

slots.cweSubmission__Submission_Name = Slot(uri=CWE.Submission_Name, name="cweSubmission__Submission_Name", curie=CWE.curie('Submission_Name'),
                   model_uri=CWE.cweSubmission__Submission_Name, domain=None, range=Optional[Union[str, list[str]]])

slots.cweSubmission__Submission_Organization = Slot(uri=CWE.Submission_Organization, name="cweSubmission__Submission_Organization", curie=CWE.curie('Submission_Organization'),
                   model_uri=CWE.cweSubmission__Submission_Organization, domain=None, range=Optional[str])

slots.cweSubmission__Submission_Date = Slot(uri=CWE.Submission_Date, name="cweSubmission__Submission_Date", curie=CWE.curie('Submission_Date'),
                   model_uri=CWE.cweSubmission__Submission_Date, domain=None, range=Union[str, XSDDate])

slots.cweSubmission__Submission_Version = Slot(uri=CWE.Submission_Version, name="cweSubmission__Submission_Version", curie=CWE.curie('Submission_Version'),
                   model_uri=CWE.cweSubmission__Submission_Version, domain=None, range=str)

slots.cweSubmission__Submission_ReleaseDate = Slot(uri=CWE.Submission_ReleaseDate, name="cweSubmission__Submission_ReleaseDate", curie=CWE.curie('Submission_ReleaseDate'),
                   model_uri=CWE.cweSubmission__Submission_ReleaseDate, domain=None, range=Union[str, XSDDate])

slots.cweSubmission__Submission_Comment = Slot(uri=CWE.Submission_Comment, name="cweSubmission__Submission_Comment", curie=CWE.curie('Submission_Comment'),
                   model_uri=CWE.cweSubmission__Submission_Comment, domain=None, range=Optional[str])

slots.cweModification__Modification_Name = Slot(uri=CWE.Modification_Name, name="cweModification__Modification_Name", curie=CWE.curie('Modification_Name'),
                   model_uri=CWE.cweModification__Modification_Name, domain=None, range=Optional[str])

slots.cweModification__Modification_Organization = Slot(uri=CWE.Modification_Organization, name="cweModification__Modification_Organization", curie=CWE.curie('Modification_Organization'),
                   model_uri=CWE.cweModification__Modification_Organization, domain=None, range=Optional[str])

slots.cweModification__Modification_Date = Slot(uri=CWE.Modification_Date, name="cweModification__Modification_Date", curie=CWE.curie('Modification_Date'),
                   model_uri=CWE.cweModification__Modification_Date, domain=None, range=Union[str, XSDDate])

slots.cweModification__Modification_Version = Slot(uri=CWE.Modification_Version, name="cweModification__Modification_Version", curie=CWE.curie('Modification_Version'),
                   model_uri=CWE.cweModification__Modification_Version, domain=None, range=str)

slots.cweModification__Modification_ReleaseDate = Slot(uri=CWE.Modification_ReleaseDate, name="cweModification__Modification_ReleaseDate", curie=CWE.curie('Modification_ReleaseDate'),
                   model_uri=CWE.cweModification__Modification_ReleaseDate, domain=None, range=Union[str, XSDDate])

slots.cweModification__Modification_Importance = Slot(uri=CWE.Modification_Importance, name="cweModification__Modification_Importance", curie=CWE.curie('Modification_Importance'),
                   model_uri=CWE.cweModification__Modification_Importance, domain=None, range=Optional[Union[str, "CweImportance"]])

slots.cweModification__Modification_Comment = Slot(uri=CWE.Modification_Comment, name="cweModification__Modification_Comment", curie=CWE.curie('Modification_Comment'),
                   model_uri=CWE.cweModification__Modification_Comment, domain=None, range=str)

slots.cweContribution__Type = Slot(uri=CWE.Type, name="cweContribution__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweContribution__Type, domain=None, range=Union[str, "CweContributionType"])

slots.cweContribution__Contribution_Name = Slot(uri=CWE.Contribution_Name, name="cweContribution__Contribution_Name", curie=CWE.curie('Contribution_Name'),
                   model_uri=CWE.cweContribution__Contribution_Name, domain=None, range=Optional[Union[str, list[str]]])

slots.cweContribution__Contribution_Organization = Slot(uri=CWE.Contribution_Organization, name="cweContribution__Contribution_Organization", curie=CWE.curie('Contribution_Organization'),
                   model_uri=CWE.cweContribution__Contribution_Organization, domain=None, range=Optional[str])

slots.cweContribution__Contribution_Date = Slot(uri=CWE.Contribution_Date, name="cweContribution__Contribution_Date", curie=CWE.curie('Contribution_Date'),
                   model_uri=CWE.cweContribution__Contribution_Date, domain=None, range=Union[str, XSDDate])

slots.cweContribution__Contribution_Version = Slot(uri=CWE.Contribution_Version, name="cweContribution__Contribution_Version", curie=CWE.curie('Contribution_Version'),
                   model_uri=CWE.cweContribution__Contribution_Version, domain=None, range=str)

slots.cweContribution__Contribution_ReleaseDate = Slot(uri=CWE.Contribution_ReleaseDate, name="cweContribution__Contribution_ReleaseDate", curie=CWE.curie('Contribution_ReleaseDate'),
                   model_uri=CWE.cweContribution__Contribution_ReleaseDate, domain=None, range=Union[str, XSDDate])

slots.cweContribution__Contribution_Comment = Slot(uri=CWE.Contribution_Comment, name="cweContribution__Contribution_Comment", curie=CWE.curie('Contribution_Comment'),
                   model_uri=CWE.cweContribution__Contribution_Comment, domain=None, range=Optional[str])

slots.cwePreviousEntryName__Date = Slot(uri=CWE.Date, name="cwePreviousEntryName__Date", curie=CWE.curie('Date'),
                   model_uri=CWE.cwePreviousEntryName__Date, domain=None, range=Union[str, XSDDate])

slots.cwePreviousEntryName__Version = Slot(uri=CWE.Version, name="cwePreviousEntryName__Version", curie=CWE.curie('Version'),
                   model_uri=CWE.cwePreviousEntryName__Version, domain=None, range=Optional[str])

slots.cwePreviousEntryName__Value = Slot(uri=CWE.Value, name="cwePreviousEntryName__Value", curie=CWE.curie('Value'),
                   model_uri=CWE.cwePreviousEntryName__Value, domain=None, range=str)

slots.cweEntry__ID = Slot(uri=CWE.ID, name="cweEntry__ID", curie=CWE.curie('ID'),
                   model_uri=CWE.cweEntry__ID, domain=None, range=URIRef)

slots.cweEntry__Name = Slot(uri=CWE.Name, name="cweEntry__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweEntry__Name, domain=None, range=str)

slots.cweEntry__Status = Slot(uri=CWE.Status, name="cweEntry__Status", curie=CWE.curie('Status'),
                   model_uri=CWE.cweEntry__Status, domain=None, range=Union[str, "CweStatus"])

slots.cweEntry__References = Slot(uri=CWE.References, name="cweEntry__References", curie=CWE.curie('References'),
                   model_uri=CWE.cweEntry__References, domain=None, range=Optional[Union[Union[dict, CweReference], list[Union[dict, CweReference]]]])

slots.cweEntry__Mapping_Notes = Slot(uri=CWE.Mapping_Notes, name="cweEntry__Mapping_Notes", curie=CWE.curie('Mapping_Notes'),
                   model_uri=CWE.cweEntry__Mapping_Notes, domain=None, range=Union[dict, CweMappingNotes])

slots.cweEntry__Notes = Slot(uri=CWE.Notes, name="cweEntry__Notes", curie=CWE.curie('Notes'),
                   model_uri=CWE.cweEntry__Notes, domain=None, range=Optional[Union[Union[dict, CweNote], list[Union[dict, CweNote]]]])

slots.cweEntry__Content_History = Slot(uri=CWE.Content_History, name="cweEntry__Content_History", curie=CWE.curie('Content_History'),
                   model_uri=CWE.cweEntry__Content_History, domain=None, range=Union[dict, CweContentHistory])

slots.cweWeakness__Abstraction = Slot(uri=CWE.Abstraction, name="cweWeakness__Abstraction", curie=CWE.curie('Abstraction'),
                   model_uri=CWE.cweWeakness__Abstraction, domain=None, range=Union[str, "CweAbstraction"])

slots.cweWeakness__Structure = Slot(uri=CWE.Structure, name="cweWeakness__Structure", curie=CWE.curie('Structure'),
                   model_uri=CWE.cweWeakness__Structure, domain=None, range=Union[str, "CweStructure"])

slots.cweWeakness__Diagram = Slot(uri=CWE.Diagram, name="cweWeakness__Diagram", curie=CWE.curie('Diagram'),
                   model_uri=CWE.cweWeakness__Diagram, domain=None, range=Optional[str])

slots.cweWeakness__Description = Slot(uri=CWE.Description, name="cweWeakness__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweWeakness__Description, domain=None, range=str)

slots.cweWeakness__Extended_Description = Slot(uri=CWE.Extended_Description, name="cweWeakness__Extended_Description", curie=CWE.curie('Extended_Description'),
                   model_uri=CWE.cweWeakness__Extended_Description, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweWeakness__Technical_Nuance = Slot(uri=CWE.Technical_Nuance, name="cweWeakness__Technical_Nuance", curie=CWE.curie('Technical_Nuance'),
                   model_uri=CWE.cweWeakness__Technical_Nuance, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweWeakness__Dimensions = Slot(uri=CWE.Dimensions, name="cweWeakness__Dimensions", curie=CWE.curie('Dimensions'),
                   model_uri=CWE.cweWeakness__Dimensions, domain=None, range=Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]])

slots.cweWeakness__Related_Weaknesses = Slot(uri=CWE.Related_Weaknesses, name="cweWeakness__Related_Weaknesses", curie=CWE.curie('Related_Weaknesses'),
                   model_uri=CWE.cweWeakness__Related_Weaknesses, domain=None, range=Optional[Union[Union[dict, CweRelatedWeakness], list[Union[dict, CweRelatedWeakness]]]])

slots.cweWeakness__Weakness_Ordinalities = Slot(uri=CWE.Weakness_Ordinalities, name="cweWeakness__Weakness_Ordinalities", curie=CWE.curie('Weakness_Ordinalities'),
                   model_uri=CWE.cweWeakness__Weakness_Ordinalities, domain=None, range=Optional[Union[Union[dict, CweWeaknessOrdinality], list[Union[dict, CweWeaknessOrdinality]]]])

slots.cweWeakness__Applicable_Platforms = Slot(uri=CWE.Applicable_Platforms, name="cweWeakness__Applicable_Platforms", curie=CWE.curie('Applicable_Platforms'),
                   model_uri=CWE.cweWeakness__Applicable_Platforms, domain=None, range=Optional[Union[dict, CweApplicablePlatforms]])

slots.cweWeakness__Background_Details = Slot(uri=CWE.Background_Details, name="cweWeakness__Background_Details", curie=CWE.curie('Background_Details'),
                   model_uri=CWE.cweWeakness__Background_Details, domain=None, range=Optional[Union[Union[str, CweStructuredText], list[Union[str, CweStructuredText]]]])

slots.cweWeakness__Alternate_Terms = Slot(uri=CWE.Alternate_Terms, name="cweWeakness__Alternate_Terms", curie=CWE.curie('Alternate_Terms'),
                   model_uri=CWE.cweWeakness__Alternate_Terms, domain=None, range=Optional[Union[Union[dict, CweAlternateTerm], list[Union[dict, CweAlternateTerm]]]])

slots.cweWeakness__Modes_Of_Introduction = Slot(uri=CWE.Modes_Of_Introduction, name="cweWeakness__Modes_Of_Introduction", curie=CWE.curie('Modes_Of_Introduction'),
                   model_uri=CWE.cweWeakness__Modes_Of_Introduction, domain=None, range=Optional[Union[Union[dict, CweIntroduction], list[Union[dict, CweIntroduction]]]])

slots.cweWeakness__Exploitation_Factors = Slot(uri=CWE.Exploitation_Factors, name="cweWeakness__Exploitation_Factors", curie=CWE.curie('Exploitation_Factors'),
                   model_uri=CWE.cweWeakness__Exploitation_Factors, domain=None, range=Optional[Union[Union[str, CweStructuredText], list[Union[str, CweStructuredText]]]])

slots.cweWeakness__Likelihood_Of_Exploit = Slot(uri=CWE.Likelihood_Of_Exploit, name="cweWeakness__Likelihood_Of_Exploit", curie=CWE.curie('Likelihood_Of_Exploit'),
                   model_uri=CWE.cweWeakness__Likelihood_Of_Exploit, domain=None, range=Optional[Union[str, "CweLikelihood"]])

slots.cweWeakness__Common_Consequences = Slot(uri=CWE.Common_Consequences, name="cweWeakness__Common_Consequences", curie=CWE.curie('Common_Consequences'),
                   model_uri=CWE.cweWeakness__Common_Consequences, domain=None, range=Optional[Union[Union[dict, CweConsequence], list[Union[dict, CweConsequence]]]])

slots.cweWeakness__Detection_Methods = Slot(uri=CWE.Detection_Methods, name="cweWeakness__Detection_Methods", curie=CWE.curie('Detection_Methods'),
                   model_uri=CWE.cweWeakness__Detection_Methods, domain=None, range=Optional[Union[Union[dict, CweDetectionMethod], list[Union[dict, CweDetectionMethod]]]])

slots.cweWeakness__Potential_Mitigations = Slot(uri=CWE.Potential_Mitigations, name="cweWeakness__Potential_Mitigations", curie=CWE.curie('Potential_Mitigations'),
                   model_uri=CWE.cweWeakness__Potential_Mitigations, domain=None, range=Optional[Union[Union[dict, CweMitigation], list[Union[dict, CweMitigation]]]])

slots.cweWeakness__Demonstrative_Examples = Slot(uri=CWE.Demonstrative_Examples, name="cweWeakness__Demonstrative_Examples", curie=CWE.curie('Demonstrative_Examples'),
                   model_uri=CWE.cweWeakness__Demonstrative_Examples, domain=None, range=Optional[Union[Union[dict, CweDemonstrativeExample], list[Union[dict, CweDemonstrativeExample]]]])

slots.cweWeakness__Observed_Examples = Slot(uri=CWE.Observed_Examples, name="cweWeakness__Observed_Examples", curie=CWE.curie('Observed_Examples'),
                   model_uri=CWE.cweWeakness__Observed_Examples, domain=None, range=Optional[Union[Union[dict, CweObservedExample], list[Union[dict, CweObservedExample]]]])

slots.cweWeakness__Functional_Areas = Slot(uri=CWE.Functional_Areas, name="cweWeakness__Functional_Areas", curie=CWE.curie('Functional_Areas'),
                   model_uri=CWE.cweWeakness__Functional_Areas, domain=None, range=Optional[Union[Union[str, "CweFunctionalArea"], list[Union[str, "CweFunctionalArea"]]]])

slots.cweWeakness__Affected_Resources = Slot(uri=CWE.Affected_Resources, name="cweWeakness__Affected_Resources", curie=CWE.curie('Affected_Resources'),
                   model_uri=CWE.cweWeakness__Affected_Resources, domain=None, range=Optional[Union[Union[str, "CweResource"], list[Union[str, "CweResource"]]]])

slots.cweWeakness__Taxonomy_Mappings = Slot(uri=CWE.Taxonomy_Mappings, name="cweWeakness__Taxonomy_Mappings", curie=CWE.curie('Taxonomy_Mappings'),
                   model_uri=CWE.cweWeakness__Taxonomy_Mappings, domain=None, range=Optional[Union[Union[dict, CweTaxonomyMapping], list[Union[dict, CweTaxonomyMapping]]]])

slots.cweWeakness__Related_Attack_Patterns = Slot(uri=CWE.Related_Attack_Patterns, name="cweWeakness__Related_Attack_Patterns", curie=CWE.curie('Related_Attack_Patterns'),
                   model_uri=CWE.cweWeakness__Related_Attack_Patterns, domain=None, range=Optional[Union[Union[dict, CweRelatedAttackPattern], list[Union[dict, CweRelatedAttackPattern]]]])

slots.cweGrouping__Summary = Slot(uri=CWE.Summary, name="cweGrouping__Summary", curie=CWE.curie('Summary'),
                   model_uri=CWE.cweGrouping__Summary, domain=None, range=Union[str, CweStructuredText])

slots.cweGrouping__Relationships = Slot(uri=CWE.Relationships, name="cweGrouping__Relationships", curie=CWE.curie('Relationships'),
                   model_uri=CWE.cweGrouping__Relationships, domain=None, range=Optional[Union[dict, CweRelationships]])

slots.cweGrouping__Taxonomy_Mappings = Slot(uri=CWE.Taxonomy_Mappings, name="cweGrouping__Taxonomy_Mappings", curie=CWE.curie('Taxonomy_Mappings'),
                   model_uri=CWE.cweGrouping__Taxonomy_Mappings, domain=None, range=Optional[Union[Union[dict, CweTaxonomyMapping], list[Union[dict, CweTaxonomyMapping]]]])

slots.cweView__Type = Slot(uri=CWE.Type, name="cweView__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweView__Type, domain=None, range=Union[str, "CweViewType"])

slots.cweView__Objective = Slot(uri=CWE.Objective, name="cweView__Objective", curie=CWE.curie('Objective'),
                   model_uri=CWE.cweView__Objective, domain=None, range=Union[str, CweStructuredText])

slots.cweView__Audience = Slot(uri=CWE.Audience, name="cweView__Audience", curie=CWE.curie('Audience'),
                   model_uri=CWE.cweView__Audience, domain=None, range=Optional[Union[Union[dict, CweStakeholder], list[Union[dict, CweStakeholder]]]])

slots.cweView__Members = Slot(uri=CWE.Members, name="cweView__Members", curie=CWE.curie('Members'),
                   model_uri=CWE.cweView__Members, domain=None, range=Optional[Union[dict, CweRelationships]])

slots.cweView__Filter = Slot(uri=CWE.Filter, name="cweView__Filter", curie=CWE.curie('Filter'),
                   model_uri=CWE.cweView__Filter, domain=None, range=Optional[str])

slots.cweRelatedWeakness__Nature = Slot(uri=CWE.Nature, name="cweRelatedWeakness__Nature", curie=CWE.curie('Nature'),
                   model_uri=CWE.cweRelatedWeakness__Nature, domain=None, range=Union[str, "CweRelatedNature"])

slots.cweRelatedWeakness__CWE_ID = Slot(uri=CWE.CWE_ID, name="cweRelatedWeakness__CWE_ID", curie=CWE.curie('CWE_ID'),
                   model_uri=CWE.cweRelatedWeakness__CWE_ID, domain=None, range=Union[str, CweWeaknessID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweRelatedWeakness__View_ID = Slot(uri=CWE.View_ID, name="cweRelatedWeakness__View_ID", curie=CWE.curie('View_ID'),
                   model_uri=CWE.cweRelatedWeakness__View_ID, domain=None, range=Union[str, CweViewID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweRelatedWeakness__Chain_ID = Slot(uri=CWE.Chain_ID, name="cweRelatedWeakness__Chain_ID", curie=CWE.curie('Chain_ID'),
                   model_uri=CWE.cweRelatedWeakness__Chain_ID, domain=None, range=Optional[Union[str, CweWeaknessID]],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweRelatedWeakness__Ordinal = Slot(uri=CWE.Ordinal, name="cweRelatedWeakness__Ordinal", curie=CWE.curie('Ordinal'),
                   model_uri=CWE.cweRelatedWeakness__Ordinal, domain=None, range=Optional[Union[str, "CweOrdinal"]])

slots.cweRelatedWeakness__Dimensions = Slot(uri=CWE.Dimensions, name="cweRelatedWeakness__Dimensions", curie=CWE.curie('Dimensions'),
                   model_uri=CWE.cweRelatedWeakness__Dimensions, domain=None, range=Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]])

slots.cweWeaknessOrdinality__Ordinality = Slot(uri=CWE.Ordinality, name="cweWeaknessOrdinality__Ordinality", curie=CWE.curie('Ordinality'),
                   model_uri=CWE.cweWeaknessOrdinality__Ordinality, domain=None, range=Union[str, "CweOrdinality"])

slots.cweWeaknessOrdinality__Description = Slot(uri=CWE.Description, name="cweWeaknessOrdinality__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweWeaknessOrdinality__Description, domain=None, range=Optional[str])

slots.cweApplicablePlatforms__Language = Slot(uri=CWE.Language, name="cweApplicablePlatforms__Language", curie=CWE.curie('Language'),
                   model_uri=CWE.cweApplicablePlatforms__Language, domain=None, range=Optional[Union[Union[dict, CweLanguagePlatform], list[Union[dict, CweLanguagePlatform]]]])

slots.cweApplicablePlatforms__Operating_System = Slot(uri=CWE.Operating_System, name="cweApplicablePlatforms__Operating_System", curie=CWE.curie('Operating_System'),
                   model_uri=CWE.cweApplicablePlatforms__Operating_System, domain=None, range=Optional[Union[Union[dict, CweOperatingSystemPlatform], list[Union[dict, CweOperatingSystemPlatform]]]])

slots.cweApplicablePlatforms__Architecture = Slot(uri=CWE.Architecture, name="cweApplicablePlatforms__Architecture", curie=CWE.curie('Architecture'),
                   model_uri=CWE.cweApplicablePlatforms__Architecture, domain=None, range=Optional[Union[Union[dict, CweArchitecturePlatform], list[Union[dict, CweArchitecturePlatform]]]])

slots.cweApplicablePlatforms__Technology = Slot(uri=CWE.Technology, name="cweApplicablePlatforms__Technology", curie=CWE.curie('Technology'),
                   model_uri=CWE.cweApplicablePlatforms__Technology, domain=None, range=Optional[Union[Union[dict, CweTechnologyPlatform], list[Union[dict, CweTechnologyPlatform]]]])

slots.cweLanguagePlatform__Name = Slot(uri=CWE.Name, name="cweLanguagePlatform__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweLanguagePlatform__Name, domain=None, range=Optional[Union[str, "CweLanguageName"]])

slots.cweLanguagePlatform__Class = Slot(uri=CWE.Class, name="cweLanguagePlatform__Class", curie=CWE.curie('Class'),
                   model_uri=CWE.cweLanguagePlatform__Class, domain=None, range=Optional[Union[str, "CweLanguageClass"]])

slots.cweLanguagePlatform__Prevalence = Slot(uri=CWE.Prevalence, name="cweLanguagePlatform__Prevalence", curie=CWE.curie('Prevalence'),
                   model_uri=CWE.cweLanguagePlatform__Prevalence, domain=None, range=Union[str, "CwePrevalence"])

slots.cweLanguagePlatform__Note = Slot(uri=CWE.Note, name="cweLanguagePlatform__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweLanguagePlatform__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweOperatingSystemPlatform__Name = Slot(uri=CWE.Name, name="cweOperatingSystemPlatform__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweOperatingSystemPlatform__Name, domain=None, range=Optional[Union[str, "CweOperatingSystemName"]])

slots.cweOperatingSystemPlatform__Version = Slot(uri=CWE.Version, name="cweOperatingSystemPlatform__Version", curie=CWE.curie('Version'),
                   model_uri=CWE.cweOperatingSystemPlatform__Version, domain=None, range=Optional[str])

slots.cweOperatingSystemPlatform__CPE_ID = Slot(uri=CWE.CPE_ID, name="cweOperatingSystemPlatform__CPE_ID", curie=CWE.curie('CPE_ID'),
                   model_uri=CWE.cweOperatingSystemPlatform__CPE_ID, domain=None, range=Optional[str])

slots.cweOperatingSystemPlatform__Class = Slot(uri=CWE.Class, name="cweOperatingSystemPlatform__Class", curie=CWE.curie('Class'),
                   model_uri=CWE.cweOperatingSystemPlatform__Class, domain=None, range=Optional[Union[str, "CweOperatingSystemClass"]])

slots.cweOperatingSystemPlatform__Prevalence = Slot(uri=CWE.Prevalence, name="cweOperatingSystemPlatform__Prevalence", curie=CWE.curie('Prevalence'),
                   model_uri=CWE.cweOperatingSystemPlatform__Prevalence, domain=None, range=Union[str, "CwePrevalence"])

slots.cweOperatingSystemPlatform__Note = Slot(uri=CWE.Note, name="cweOperatingSystemPlatform__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweOperatingSystemPlatform__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweArchitecturePlatform__Name = Slot(uri=CWE.Name, name="cweArchitecturePlatform__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweArchitecturePlatform__Name, domain=None, range=Optional[Union[str, "CweArchitectureName"]])

slots.cweArchitecturePlatform__Class = Slot(uri=CWE.Class, name="cweArchitecturePlatform__Class", curie=CWE.curie('Class'),
                   model_uri=CWE.cweArchitecturePlatform__Class, domain=None, range=Optional[Union[str, "CweArchitectureClass"]])

slots.cweArchitecturePlatform__Prevalence = Slot(uri=CWE.Prevalence, name="cweArchitecturePlatform__Prevalence", curie=CWE.curie('Prevalence'),
                   model_uri=CWE.cweArchitecturePlatform__Prevalence, domain=None, range=Union[str, "CwePrevalence"])

slots.cweArchitecturePlatform__Note = Slot(uri=CWE.Note, name="cweArchitecturePlatform__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweArchitecturePlatform__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweTechnologyPlatform__Name = Slot(uri=CWE.Name, name="cweTechnologyPlatform__Name", curie=CWE.curie('Name'),
                   model_uri=CWE.cweTechnologyPlatform__Name, domain=None, range=Optional[Union[str, "CweTechnologyName"]])

slots.cweTechnologyPlatform__Class = Slot(uri=CWE.Class, name="cweTechnologyPlatform__Class", curie=CWE.curie('Class'),
                   model_uri=CWE.cweTechnologyPlatform__Class, domain=None, range=Optional[Union[str, "CweTechnologyClass"]])

slots.cweTechnologyPlatform__Prevalence = Slot(uri=CWE.Prevalence, name="cweTechnologyPlatform__Prevalence", curie=CWE.curie('Prevalence'),
                   model_uri=CWE.cweTechnologyPlatform__Prevalence, domain=None, range=Union[str, "CwePrevalence"])

slots.cweTechnologyPlatform__Note = Slot(uri=CWE.Note, name="cweTechnologyPlatform__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweTechnologyPlatform__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweAlternateTerm__Term = Slot(uri=CWE.Term, name="cweAlternateTerm__Term", curie=CWE.curie('Term'),
                   model_uri=CWE.cweAlternateTerm__Term, domain=None, range=str)

slots.cweAlternateTerm__Role = Slot(uri=CWE.Role, name="cweAlternateTerm__Role", curie=CWE.curie('Role'),
                   model_uri=CWE.cweAlternateTerm__Role, domain=None, range=Optional[Union[Union[str, "CweAlternateTermRole"], list[Union[str, "CweAlternateTermRole"]]]])

slots.cweAlternateTerm__Description = Slot(uri=CWE.Description, name="cweAlternateTerm__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweAlternateTerm__Description, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweIntroduction__Phase = Slot(uri=CWE.Phase, name="cweIntroduction__Phase", curie=CWE.curie('Phase'),
                   model_uri=CWE.cweIntroduction__Phase, domain=None, range=Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]])

slots.cweIntroduction__Custom_Phase = Slot(uri=CWE.Custom_Phase, name="cweIntroduction__Custom_Phase", curie=CWE.curie('Custom_Phase'),
                   model_uri=CWE.cweIntroduction__Custom_Phase, domain=None, range=Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]])

slots.cweIntroduction__Note = Slot(uri=CWE.Note, name="cweIntroduction__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweIntroduction__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweConsequence__Consequence_ID = Slot(uri=CWE.Consequence_ID, name="cweConsequence__Consequence_ID", curie=CWE.curie('Consequence_ID'),
                   model_uri=CWE.cweConsequence__Consequence_ID, domain=None, range=Optional[str])

slots.cweConsequence__Scope = Slot(uri=CWE.Scope, name="cweConsequence__Scope", curie=CWE.curie('Scope'),
                   model_uri=CWE.cweConsequence__Scope, domain=None, range=Union[Union[str, "CweScope"], list[Union[str, "CweScope"]]])

slots.cweConsequence__Impact = Slot(uri=CWE.Impact, name="cweConsequence__Impact", curie=CWE.curie('Impact'),
                   model_uri=CWE.cweConsequence__Impact, domain=None, range=Union[Union[str, "CweTechnicalImpact"], list[Union[str, "CweTechnicalImpact"]]])

slots.cweConsequence__Likelihood = Slot(uri=CWE.Likelihood, name="cweConsequence__Likelihood", curie=CWE.curie('Likelihood'),
                   model_uri=CWE.cweConsequence__Likelihood, domain=None, range=Optional[Union[str, "CweLikelihood"]])

slots.cweConsequence__Note = Slot(uri=CWE.Note, name="cweConsequence__Note", curie=CWE.curie('Note'),
                   model_uri=CWE.cweConsequence__Note, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweDetectionMethod__Detection_Method_ID = Slot(uri=CWE.Detection_Method_ID, name="cweDetectionMethod__Detection_Method_ID", curie=CWE.curie('Detection_Method_ID'),
                   model_uri=CWE.cweDetectionMethod__Detection_Method_ID, domain=None, range=Optional[str])

slots.cweDetectionMethod__Method = Slot(uri=CWE.Method, name="cweDetectionMethod__Method", curie=CWE.curie('Method'),
                   model_uri=CWE.cweDetectionMethod__Method, domain=None, range=Union[str, "CweDetectionMethodName"])

slots.cweDetectionMethod__Phase = Slot(uri=CWE.Phase, name="cweDetectionMethod__Phase", curie=CWE.curie('Phase'),
                   model_uri=CWE.cweDetectionMethod__Phase, domain=None, range=Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]])

slots.cweDetectionMethod__Custom_Phase = Slot(uri=CWE.Custom_Phase, name="cweDetectionMethod__Custom_Phase", curie=CWE.curie('Custom_Phase'),
                   model_uri=CWE.cweDetectionMethod__Custom_Phase, domain=None, range=Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]])

slots.cweDetectionMethod__Description = Slot(uri=CWE.Description, name="cweDetectionMethod__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweDetectionMethod__Description, domain=None, range=Union[str, CweStructuredText])

slots.cweDetectionMethod__Effectiveness = Slot(uri=CWE.Effectiveness, name="cweDetectionMethod__Effectiveness", curie=CWE.curie('Effectiveness'),
                   model_uri=CWE.cweDetectionMethod__Effectiveness, domain=None, range=Optional[Union[str, "CweDetectionEffectiveness"]])

slots.cweDetectionMethod__Effectiveness_Notes = Slot(uri=CWE.Effectiveness_Notes, name="cweDetectionMethod__Effectiveness_Notes", curie=CWE.curie('Effectiveness_Notes'),
                   model_uri=CWE.cweDetectionMethod__Effectiveness_Notes, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweMitigation__Mitigation_ID = Slot(uri=CWE.Mitigation_ID, name="cweMitigation__Mitigation_ID", curie=CWE.curie('Mitigation_ID'),
                   model_uri=CWE.cweMitigation__Mitigation_ID, domain=None, range=Optional[str])

slots.cweMitigation__Phase = Slot(uri=CWE.Phase, name="cweMitigation__Phase", curie=CWE.curie('Phase'),
                   model_uri=CWE.cweMitigation__Phase, domain=None, range=Optional[Union[Union[str, "CwePhase"], list[Union[str, "CwePhase"]]]])

slots.cweMitigation__Custom_Phase = Slot(uri=CWE.Custom_Phase, name="cweMitigation__Custom_Phase", curie=CWE.curie('Custom_Phase'),
                   model_uri=CWE.cweMitigation__Custom_Phase, domain=None, range=Optional[Union[Union[dict, CweCustomPhase], list[Union[dict, CweCustomPhase]]]])

slots.cweMitigation__Strategy = Slot(uri=CWE.Strategy, name="cweMitigation__Strategy", curie=CWE.curie('Strategy'),
                   model_uri=CWE.cweMitigation__Strategy, domain=None, range=Optional[Union[str, "CweMitigationStrategy"]])

slots.cweMitigation__Description = Slot(uri=CWE.Description, name="cweMitigation__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweMitigation__Description, domain=None, range=Union[str, CweStructuredText])

slots.cweMitigation__Effectiveness = Slot(uri=CWE.Effectiveness, name="cweMitigation__Effectiveness", curie=CWE.curie('Effectiveness'),
                   model_uri=CWE.cweMitigation__Effectiveness, domain=None, range=Optional[Union[str, "CweEffectiveness"]])

slots.cweMitigation__Effectiveness_Notes = Slot(uri=CWE.Effectiveness_Notes, name="cweMitigation__Effectiveness_Notes", curie=CWE.curie('Effectiveness_Notes'),
                   model_uri=CWE.cweMitigation__Effectiveness_Notes, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweDemonstrativeExample__Demonstrative_Example_ID = Slot(uri=CWE.Demonstrative_Example_ID, name="cweDemonstrativeExample__Demonstrative_Example_ID", curie=CWE.curie('Demonstrative_Example_ID'),
                   model_uri=CWE.cweDemonstrativeExample__Demonstrative_Example_ID, domain=None, range=Optional[str])

slots.cweDemonstrativeExample__Title_Text = Slot(uri=CWE.Title_Text, name="cweDemonstrativeExample__Title_Text", curie=CWE.curie('Title_Text'),
                   model_uri=CWE.cweDemonstrativeExample__Title_Text, domain=None, range=Optional[str])

slots.cweDemonstrativeExample__Intro_Text = Slot(uri=CWE.Intro_Text, name="cweDemonstrativeExample__Intro_Text", curie=CWE.curie('Intro_Text'),
                   model_uri=CWE.cweDemonstrativeExample__Intro_Text, domain=None, range=Union[str, CweStructuredText])

slots.cweDemonstrativeExample__Entries = Slot(uri=CWE.Entries, name="cweDemonstrativeExample__Entries", curie=CWE.curie('Entries'),
                   model_uri=CWE.cweDemonstrativeExample__Entries, domain=None, range=Optional[Union[Union[dict, CweExampleEntry], list[Union[dict, CweExampleEntry]]]])

slots.cweExampleEntry__Body_Text = Slot(uri=CWE.Body_Text, name="cweExampleEntry__Body_Text", curie=CWE.curie('Body_Text'),
                   model_uri=CWE.cweExampleEntry__Body_Text, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweExampleEntry__Example_Code = Slot(uri=CWE.Example_Code, name="cweExampleEntry__Example_Code", curie=CWE.curie('Example_Code'),
                   model_uri=CWE.cweExampleEntry__Example_Code, domain=None, range=Optional[Union[dict, CweExampleCode]])

slots.cweExampleCode__Nature = Slot(uri=CWE.Nature, name="cweExampleCode__Nature", curie=CWE.curie('Nature'),
                   model_uri=CWE.cweExampleCode__Nature, domain=None, range=Union[str, "CweCodeNature"])

slots.cweExampleCode__Language = Slot(uri=CWE.Language, name="cweExampleCode__Language", curie=CWE.curie('Language'),
                   model_uri=CWE.cweExampleCode__Language, domain=None, range=Optional[Union[str, "CweLanguageName"]])

slots.cweExampleCode__Value = Slot(uri=CWE.Value, name="cweExampleCode__Value", curie=CWE.curie('Value'),
                   model_uri=CWE.cweExampleCode__Value, domain=None, range=Optional[Union[str, CweStructuredText]])

slots.cweObservedExample__Reference = Slot(uri=CWE.Reference, name="cweObservedExample__Reference", curie=CWE.curie('Reference'),
                   model_uri=CWE.cweObservedExample__Reference, domain=None, range=str)

slots.cweObservedExample__Description = Slot(uri=CWE.Description, name="cweObservedExample__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweObservedExample__Description, domain=None, range=Union[str, CweStructuredText])

slots.cweObservedExample__Link = Slot(uri=CWE.Link, name="cweObservedExample__Link", curie=CWE.curie('Link'),
                   model_uri=CWE.cweObservedExample__Link, domain=None, range=Union[str, URI])

slots.cweObservedExample__Rationale = Slot(uri=CWE.Rationale, name="cweObservedExample__Rationale", curie=CWE.curie('Rationale'),
                   model_uri=CWE.cweObservedExample__Rationale, domain=None, range=Optional[Union[Union[str, "CweObservedExampleRationale"], list[Union[str, "CweObservedExampleRationale"]]]])

slots.cweRelatedAttackPattern__CAPEC_ID = Slot(uri=CWE.CAPEC_ID, name="cweRelatedAttackPattern__CAPEC_ID", curie=CWE.curie('CAPEC_ID'),
                   model_uri=CWE.cweRelatedAttackPattern__CAPEC_ID, domain=None, range=Union[str, CweCapecId])

slots.cweStakeholder__Type = Slot(uri=CWE.Type, name="cweStakeholder__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweStakeholder__Type, domain=None, range=Union[str, "CweStakeholderType"])

slots.cweStakeholder__Description = Slot(uri=CWE.Description, name="cweStakeholder__Description", curie=CWE.curie('Description'),
                   model_uri=CWE.cweStakeholder__Description, domain=None, range=Optional[str])

slots.cweMember__CWE_ID = Slot(uri=CWE.CWE_ID, name="cweMember__CWE_ID", curie=CWE.curie('CWE_ID'),
                   model_uri=CWE.cweMember__CWE_ID, domain=None, range=Union[str, CweEntryID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweMember__View_ID = Slot(uri=CWE.View_ID, name="cweMember__View_ID", curie=CWE.curie('View_ID'),
                   model_uri=CWE.cweMember__View_ID, domain=None, range=Union[str, CweViewID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweMember__Dimensions = Slot(uri=CWE.Dimensions, name="cweMember__Dimensions", curie=CWE.curie('Dimensions'),
                   model_uri=CWE.cweMember__Dimensions, domain=None, range=Optional[Union[Union[dict, CweDimension], list[Union[dict, CweDimension]]]])

slots.cweRelationships__Member_Of = Slot(uri=CWE.Member_Of, name="cweRelationships__Member_Of", curie=CWE.curie('Member_Of'),
                   model_uri=CWE.cweRelationships__Member_Of, domain=None, range=Optional[Union[Union[dict, CweMember], list[Union[dict, CweMember]]]])

slots.cweRelationships__Has_Member = Slot(uri=CWE.Has_Member, name="cweRelationships__Has_Member", curie=CWE.curie('Has_Member'),
                   model_uri=CWE.cweRelationships__Has_Member, domain=None, range=Optional[Union[Union[dict, CweMember], list[Union[dict, CweMember]]]])

slots.cweMappingNotes__Usage = Slot(uri=CWE.Usage, name="cweMappingNotes__Usage", curie=CWE.curie('Usage'),
                   model_uri=CWE.cweMappingNotes__Usage, domain=None, range=Union[str, "CweUsage"])

slots.cweMappingNotes__Rationale = Slot(uri=CWE.Rationale, name="cweMappingNotes__Rationale", curie=CWE.curie('Rationale'),
                   model_uri=CWE.cweMappingNotes__Rationale, domain=None, range=Union[str, CweStructuredText])

slots.cweMappingNotes__Comments = Slot(uri=CWE.Comments, name="cweMappingNotes__Comments", curie=CWE.curie('Comments'),
                   model_uri=CWE.cweMappingNotes__Comments, domain=None, range=Union[str, CweStructuredText])

slots.cweMappingNotes__Reasons = Slot(uri=CWE.Reasons, name="cweMappingNotes__Reasons", curie=CWE.curie('Reasons'),
                   model_uri=CWE.cweMappingNotes__Reasons, domain=None, range=Union[Union[dict, CweMappingReason], list[Union[dict, CweMappingReason]]])

slots.cweMappingNotes__Suggestions = Slot(uri=CWE.Suggestions, name="cweMappingNotes__Suggestions", curie=CWE.curie('Suggestions'),
                   model_uri=CWE.cweMappingNotes__Suggestions, domain=None, range=Optional[Union[Union[dict, CweMappingSuggestion], list[Union[dict, CweMappingSuggestion]]]])

slots.cweMappingReason__Type = Slot(uri=CWE.Type, name="cweMappingReason__Type", curie=CWE.curie('Type'),
                   model_uri=CWE.cweMappingReason__Type, domain=None, range=Union[str, "CweReason"])

slots.cweMappingSuggestion__CWE_ID = Slot(uri=CWE.CWE_ID, name="cweMappingSuggestion__CWE_ID", curie=CWE.curie('CWE_ID'),
                   model_uri=CWE.cweMappingSuggestion__CWE_ID, domain=None, range=Union[str, CweWeaknessID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.cweMappingSuggestion__Comment = Slot(uri=CWE.Comment, name="cweMappingSuggestion__Comment", curie=CWE.curie('Comment'),
                   model_uri=CWE.cweMappingSuggestion__Comment, domain=None, range=str)
