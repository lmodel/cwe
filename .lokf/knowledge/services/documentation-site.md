---
type: Service
id: https://w3id.org/lmodel/cwe/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/cwe`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
resource: website
dependsOn:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/cwe/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:31:33Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site with a page per concept, a health page, a graph, the schema's pages and the docs.[^website-readme.md]

`REDIRECTS` keeps the retired mkdocs site's addresses: each old element page goes to its successor where it has one, and otherwise to the schema's index.[^site.toml]

[^website-readme.md]: website/README.md
[^site.toml]: website/site.toml, the site's address, title and redirects
