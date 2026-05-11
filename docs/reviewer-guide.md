# Reviewer Guide

This guide is a short path through GDPO 4.0.3 for paper reviewers, ontology
users, and repository visitors.

## Start Here

GDPO represents Dieter Rams' ten principles as directive information content
entities. It does not model the principles themselves as artifact properties.
Instead, principles are linked to artifact-side target expressions, prescribed
design processes, evaluation methods, and evidence-bearing evaluation records.

Core files:

- ontology: `../ontology/gdpo-4.0.3.ttl`
- XML catalog: `../ontology/catalog-v001.xml`
- manuscript: `../paper/`
- example ABox: `../examples/gdpo-example-abox.ttl`
- SPARQL templates: `../queries/sparql-templates.md`
- validation notes: `../validation/README.md`

## What Changed in v4.0.3

- Principles are treated as directive information content entities.
- Artifact-side targets are represented with OWL class expressions.
- Punned class-as-individual target proxies are not used.
- `owl:hasValue` target restrictions are not used.
- Prescription components represent process-level prescriptive force.
- Evaluation records represent assessment outputs, including criteria, methods,
  temporal indexing, scores, and evidence links.
- CCO imports are pinned to the stable CCO 2.0 release from 2024.

## Modeling Commitments to Check

Reviewers should expect the ontology to maintain these commitments:

- A principle is not the quality, function, disposition, material basis, process,
  or communication content it concerns.
- A design evaluation record is an information content entity, not the evaluated
  artifact and not the evaluation process itself.
- Scores should normally be represented as reified score components with a
  principle and score scale.
- Communicative honesty is handled through evaluation records about
  communication content, not as a product-borne disposition.
- `has material bearer` is optional lightweight provenance and does not replace
  the full BFO concretization pattern.

## Fast Validation

From the repository root:

```bash
python3 -c "import rdflib; rdflib.Graph().parse('ontology/gdpo-4.0.3.ttl', format='turtle')"
python3 -c "import rdflib; rdflib.Graph().parse('examples/gdpo-example-abox.ttl', format='turtle')"
xmllint --noout ontology/catalog-v001.xml
```

## Suggested Reading Order

1. `README.md`
2. `docs/design-patterns.md`
3. `docs/competency-questions.md`
4. `queries/sparql-templates.md`
5. `examples/gdpo-example-abox.ttl`
6. `ontology/gdpo-4.0.3.ttl`
