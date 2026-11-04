# Glossary

* [Entry](entry.md) - An entry of the CWE List: any item with its own identifier, which is a weakness, a grouping or a view. `CweEntry` is the abstract class of all three.
* [Weakness](weakness.md) - A weakness: a type of mistake or condition in software, firmware, hardware or a service that can leave a product open to attack. `CweWeakness` models it, with its `Abstraction` and `Structure`.
* [Grouping](grouping.md) - A grouping: a set of weaknesses gathered by something they share, for browsing and not for mapping real vulnerabilities to. Schema versions before 8.0 called it a category, and `CweGrouping` models it.
* [View](view.md) - A view: a way of looking at the catalogue, as a subset of its entries from one standpoint. `CweView` models it, and its `Type` is `Graph`, `Explicit` or `Implicit`.
* [Abstraction](abstraction.md) - The abstraction of a weakness: how far it is described in general terms or tied to a specific product. `CweAbstraction` lists `Pillar`, `Class`, `Base`, `Variant` and `Compound`.
* [Chain and composite](compound.md) - A compound weakness, which is a chain or a composite: a chain is several weaknesses reached one after another, and a composite is several that must occur together. CWE 5.0 has three chains and four composites.
* [Related nature](related-nature.md) - The nature of a link between two weaknesses: `ChildOf`, `ParentOf`, `StartsWith`, `CanFollow`, `CanPrecede`, `RequiredBy`, `Requires`, `CanAlsoBe`, `PeerOf` or `Overlaps`. `CweRelatedNature` lists them.
* [Mapping notes](mapping-notes.md) - Mapping notes: the guidance on whether a real vulnerability may be mapped to an entry as its root cause. `CweMappingNotes` holds the `Usage`, which is `Allowed`, `Allowed-with-Review`, `Discouraged` or `Prohibited`, with the reasons and suggestions.
* [Structured text](structured-text.md) - Structured text: text that may hold XHTML, as a well-formed fragment without the namespace prefix and with its special characters escaped. `cwe_structured_text` is its type, and a consumer that shows it as HTML must sanitize it first.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
