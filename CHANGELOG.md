# Changelog

All notable changes to the Good Design Principles Ontology are documented here.

## [4.0.3] - 2026-05-11

### Changed

- Reworked GDPO around the manuscript framing that principles are directive information content entities, not artifact properties.
- Replaced punned artifact-side target individuals and `owl:hasValue` target restrictions with universal class-expression restrictions.
- Represented Rams' ten canonical principle statements as named information-content individuals under their corresponding principle categories.
- Added prescription-component modeling for prescribed design process types and lifecycle-stage applicability.
- Added evaluation-record, evaluation-method, score-component, and criterion-method relevance patterns.
- Added modality-specific support for communicative honesty evaluation.
- Pinned Common Core Ontologies imports to stable CCO 2.0 release IRIs from 2024 rather than the development branch.
- Clarified `has material bearer` as optional lightweight material-bearer provenance, not a replacement for the full BFO concretization pattern.

### Repository

- Moved the current ontology release into `ontology/gdpo-4.0.3.ttl`.
- Moved the XML catalog into `ontology/catalog-v001.xml`.
- Moved the manuscript into `paper/`.
- Archived historical TTL files under `legacy/` for provenance.
- Added validation notes in `validation/README.md`.

## Historical Versions

Earlier ontology snapshots and releases are retained under `legacy/` for reference only. They do not represent the current manuscript-aligned modeling pattern.
