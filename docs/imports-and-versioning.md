# Imports and Versioning

GDPO 4.0.3 imports BFO 2020 and the stable 2.0 release of the Common Core
Ontologies.

## Imported Ontologies

The ontology imports:

- BFO 2020: `http://purl.obolibrary.org/obo/bfo/2020/bfo.owl`
- CCO Agent Ontology 2.0: `https://www.commoncoreontologies.org/2024-11-05/AgentOntology`
- CCO Artifact Ontology 2.0: `https://www.commoncoreontologies.org/2024-11-06/ArtifactOntology`

The local XML catalog is `../ontology/catalog-v001.xml`.

## Why CCO 2.0 Is Pinned

The accompanying manuscript cites CCO as a 2024 dependency. For that reason,
GDPO 4.0.3 is pinned to CCO 2.0 release IRIs rather than to the CCO development
branch or later CCO 2.1 headers.

This avoids version drift between:

- the ontology imports
- the XML catalog resolution behavior
- the manuscript's dependency language
- reproducible validation by reviewers

## Catalog Resolution

For local editing in Protege or another OWL tool, load the ontology with the XML
catalog in `ontology/catalog-v001.xml`. The catalog resolves CCO imports through
the stable GitHub release tag:

```text
v2.0-2024-11-06
```

## Version Policy

Use the following expectations for future releases:

- Patch releases may fix annotations, documentation, examples, and validation
  artifacts without changing the core modeling pattern.
- Minor releases may add classes, properties, examples, or optional patterns
  while preserving the v4 modeling commitments.
- Major releases may change the modeling commitments, import strategy, or
  alignment assumptions.

If the manuscript is updated to cite a newer CCO release, update the ontology
imports, XML catalog, README, and this file together.
