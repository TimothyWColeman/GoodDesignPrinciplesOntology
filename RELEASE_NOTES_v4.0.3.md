# GDPO v4.0.3

This release reworks the Good Design Principles Ontology around the manuscript
framing in *Principles Are Not Properties: A BFO-Grounded Ontology for
Normative Design Guidance and Evaluation Traceability*.

## Highlights

- Represents Rams' principles as directive information content entities, not as artifact properties.
- Replaces punned artifact-side target individuals and `owl:hasValue` target restrictions with universal class-expression restrictions.
- Represents the ten canonical Rams statements as named information-content individuals under their corresponding principle categories.
- Adds prescription-component modeling for prescribed design process types and lifecycle-stage applicability.
- Adds evaluation-record, evaluation-method, score-component, and criterion-method relevance patterns.
- Adds modality-specific support for communicative honesty evaluation.
- Pins Common Core Ontologies imports to stable CCO 2.0 release IRIs from 2024.
- Clarifies `has material bearer` as optional lightweight material-bearer provenance.

## Repository Changes

- Current ontology release: `ontology/gdpo-4.0.3.ttl`
- XML catalog: `ontology/catalog-v001.xml`
- Manuscript folder: `paper/`
- Historical TTL archive: `legacy/`
- Validation notes: `validation/README.md`
- License: CC-BY-4.0

## Validation

The release was checked by:

```bash
python3 -c "import rdflib; rdflib.Graph().parse('ontology/gdpo-4.0.3.ttl', format='turtle')"
xmllint --noout ontology/catalog-v001.xml
ruby -e "require 'yaml'; YAML.load_file('CITATION.cff')"
```
