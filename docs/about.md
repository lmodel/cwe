# About cwe

This page is for anyone reading the schema's elements: it says how the classes fit together, how the XML becomes JSON and what the model leaves out.

## How the catalogue is shaped

A release of the CWE List is one `CweWeaknessCatalog`, which holds four lists: `Weaknesses`, `Groupings`, `Views` and `External_References`. The CWE glossary calls any item with a unique identifier an [entry](https://cwe.mitre.org/documents/glossary/index.html#Entry), so the three kinds of entry share an abstract class, `CweEntry`, which holds what the XSD gives all three: the `ID`, the `Name`, the `Status`, the `References`, the `Mapping_Notes`, the `Notes` and the `Content_History`. An `ID` is unique across all three kinds.

A weakness has an `Abstraction` and a `Structure`. `Pillar`, `Class`, `Base` and `Variant` run from the most general to the most specific. `Compound` is the abstraction of a chain or a composite, and a rule in the schema holds the two keys to each other. Entries link in three ways:

- a weakness names other weaknesses in `Related_Weaknesses`, each link with a `Nature` and the view it holds in;
- a grouping names its members in `Relationships`, and a view in `Members`, each through a `CweMember`;
- `Mapping_Notes` says whether a real vulnerability may be mapped to the entry, and `Suggestions` names better choices.

These references are typed: `CWE_ID` ranges over the class it names and `External_Reference_ID` over `CweExternalReference`. A generated JSON Schema cannot check that such a value names something that exists, so `tests/cwe_rules.py` does, over a whole catalogue.

The list writes most links in one direction. CWE 5.0 uses `ChildOf`, `CanPrecede` and `Requires` and never their inverses, so a reader who wants `ParentOf` computes it. Most `PeerOf` links, and all `Overlaps` links, also appear from one side only, although the CWE Program calls both natures symmetric.

## Keys

The keys and values are the XSD's own, such as `Related_Weaknesses`, `CWE_ID` and `Automated Static Analysis - Source Code`, and the classes and enums carry a `Cwe` prefix. Each class and enum names the XSD type it renders in an `xsd_type` annotation.

## From XML to JSON

LinkML validates JSON and YAML, and MITRE publishes XML, so `scripts/cwec_to_json.py` is the one step between them. It keeps every name and every value, and it reads what repeats from the XSD.

- An attribute becomes a key of the same name.
- A wrapper, an element whose only content is one repeating child, becomes a list under the wrapper's name. So `Related_Weaknesses` holds a list and `Related_Weakness` is not a key.
- Any other element with children becomes an object, and a child that may repeat is always a list. So `Applicable_Platforms` holds `Language`, `Technology` and the others.
- An element with text and attributes becomes an object with its text under `Value`, the word the CWE REST API uses.
- Text that may hold XHTML (`cwe_structured_text`) becomes a string holding the fragment, without the namespace prefix and with its special characters escaped. A consumer that shows it as HTML must sanitize it first, since many entries quote attack strings.
- The repeating choice of `Body_Text` and `Example_Code` in a worked example becomes `Entries`, a list of objects with exactly one of the two, because the prose and the code are written to be read in order. `Entries` is the REST API's name, and the one key here that the XSD does not give.
- Every value stays a string, the numbers that identify entries among them, as the XML has them.

## Which file is the schema

The XML of CWE 5.0 names `cwe_schema_v8.0.xsd` as its schema, and validates against it with no error. That is the file this schema renders. The file behind the `cwe_schema_latest.xsd` link on MITRE's downloads page is an earlier copy of version 8.0, made 32 minutes before it. The catalogue breaks that copy in 69 places, since it lacks the keys `Rationale`, `Alt_URL`, `Alt_URL_Date`, `Media_Type` and `Access_Restrictions` and two values. The upstream watch pins both files, and reports when the second changes.

The CWE-CAPEC REST API working group publishes the same content as JSON, with other keys, in an API and in a repository. Its JSON schemas date from 2024 and its keys are not consistent, such as `CweID` beside `CWE_ID`, so this project does not render them.

## RDF

An entry's number is its identifier, so the JSON-LD route works: apply `project/jsonld/cwe.context.jsonld` to the catalogue with `https://w3id.org/lmodel/cwe/` as the base, and CWE-79 is `cwe:79`, with each link an IRI. LinkML's own RDF dumper, `linkml-convert -t rdf`, fails on an identifier that is not a CURIE, with `Unknown CURIE prefix: @base`, and `tests/test_datamodel.py` holds this sentence to it.

A key that means different things on different classes, such as `Type` or `Name`, has one IRI, because the IRI names the XSD's key. `gen-owl` warns of each one when it runs.

## What is left out

XSD 8.0 still declares `CategoryType` and a `Categories` element beside `GroupingType` and `Groupings`. CWE 5.0 holds no category, and the CWE Program says `Grouping` replaced `Category`, so the schema has no such class, and `tests/test_coverage.py` names this as its one exclusion.

The CWE Program keeps a parallel 4.x line under schema 7.x for consumers who have not moved, of which CWE 4.21 is the newest. This schema does not render it.

The schema says nothing about whether what an entry claims is true.
