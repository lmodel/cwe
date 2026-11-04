---
type: Service
id: https://w3id.org/lmodel/cwe/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/cwe`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
resource: website
dependsOn:
  - https://w3id.org/lmodel/cwe/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/cwe/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: REPO, SITE, BASE and REDIRECTS
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:42:50Z"
status: draft
---

# Documentation site

`website/` holds an Astro Starlight site with a page per concept, a health page, a graph, the schema's pages and the docs.[^website-readme.md]

`REDIRECTS` keeps the retired mkdocs site's addresses: each old element page goes to its successor where it has one, and otherwise to the schema's index.[^site.config.mjs]

[^website-readme.md]: website/README.md
[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE and REDIRECTS
