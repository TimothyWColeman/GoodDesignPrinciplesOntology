# Changelog

All notable changes to the Good Design Principles Ontology (GDPO) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [4.0.3] - 2026-01-17

### Changed
- **`is concretized by` (GDPO0000464)**: Renamed to `has material bearer` and restructured as a subproperty of BFO's `generically depends on` for better alignment with BFO 2020 generically dependent continuant modeling.

### Notes
- This change clarifies that the relation links an ICE to its material bearer (the entity that bears a concretization of the information content), consistent with BFO's treatment of generic dependence.

---

## [4.0.2] - 2026-01-17

### Added
- **`assessed during temporal region` (GDPO0000468)**: New object property relating design evaluation records to BFO temporal regions for full BFO 2020–compliant temporal modeling. Complements the legacy `assessed_on` datatype property.
- **`applies during temporal region` (GDPO0000467)**: New object property relating design process prescriptions to BFO temporal regions, enabling fine-grained temporal scoping beyond lifecycle-stage qualifiers.

### Changed
- **`aims at artifact-side target` (GDPO0000454)**: Removed OWL range restrictions to avoid treating punned target classes as instances of BFO categories. Validation of target constraints (must be a class and subclass of quality/function/disposition) is now deferred to SHACL shapes.

### Notes
- These changes support advanced temporal reasoning and integration with time ontologies (e.g., OWL-Time) while maintaining backward compatibility with existing ABox data using `assessed_on` timestamps.

---

## [4.0.1] - 2026-01-16

### Added
- **Truthmaker patch**: Implemented OWL2 punning solution for the "aboutness pattern" to avoid existential commitments generating "phantom entities." Principle classes are now treated as both classes and individuals where needed for definitional structure.

### Fixed
- Resolved reasoner failures caused by non-regular role hierarchies involving `cco:prescribes` and property chains.

---

## [4.0.0] - 2026-01-15

### Added
- **Reified scoring pattern**: New classes `design evaluation score` (GDPO0000456) and `evaluation score scale specification` (GDPO0000461) for multi-criterion, multi-scale evaluation records.
- **Score-related properties**: `has score component` (GDPO0000457), `score for principle` (GDPO0000458), `score value` (GDPO0000459), `has score scale` (GDPO0000460).
- **Process–record linkage**: `has evaluation record output` (GDPO0000463) and inverse `is evaluation record output of` (GDPO0000462) for explicit truthmaker/provenance connections.
- **Evaluated artifact participant**: `has evaluated artifact participant` (GDPO0000465) for design evaluation processes.
- **Concretization property**: `is concretized by` (GDPO0000464) relating ICEs to material bearers.
- **Communicative honesty evaluation**: New class (GDPO0000452) and `is about communication content` property (GDPO0000450) for evaluating manuals, labels, and advertisements.
- **Design interaction honesty evaluation**: New class (GDPO0000455) for artifact-borne honesty assessments.
- **Communication content classes**: `design communication content entity` (GDPO0000446) with subclasses for manuals (GDPO0000447), labels (GDPO0000448), and advertisements (GDPO0000449).

### Changed
- **Principle definitions**: Refactored all ten principle classes to use `aims at artifact-side target` with punned individuals, replacing prior prescriptive-chain-based definitions.
- **Evaluation record definition**: Now uses equivalentClass axiom requiring artifact, principle, and temporal region.
- **Design honesty**: Restructured as parent class for material and functional honesty dispositions; communicative honesty moved to evaluation-based pattern.

### Removed
- Deprecated disposition-based modeling for communicative honesty (bearer participation constraint violations).

---

## [3.0.0] - 2026-01-15

### Added
- **Prescription component pattern**: New class `design process prescription` (GDPO0000061) and properties `has prescription component` (GDPO0000062), `applies during lifecycle stage` (GDPO0000063).
- **Property chain**: `prescribes via prescription component` (GDPO0000064) deriving prescriptive relations through prescription components.
- **Named prescription individuals**: GDPO0000076–GDPO0000085 for each of the ten principles.
- **Canonical statement text**: Annotation property `has canonical statement text` (GDPO0000453).

### Changed
- **Modeling shift**: Moved from direct `cco:prescribes` assertions on principles to reified prescription components, enabling temporal and conditional qualifiers.

---

## [1.5.1] - 2025-12-29

### Added
- **Lifecycle stage processes**: `design sourcing process` (GDPO0000036), `design manufacturing process` (GDPO0000037), `design distribution process` (GDPO0000038), `design use and maintenance process` (GDPO0000039), `design end-of-life handling process` (GDPO0000040).
- **Has principle component**: Property (GDPO0000060) for Rams Ten Principles Specification composition.

### Changed
- Environmental friendliness reclassified from disposition to quality to resolve temporal contradictions.

---

## [1.4.9] - 2025-08-21

### Added
- **Honesty facets**: `design material honesty` (GDPO0000041), `design functional honesty` (GDPO0000042), `design honesty basis` (GDPO0000056) with subclasses.
- **Evaluation method linkage**: `operationalizes principle` (GDPO0000054), `has evaluation-relevant principle` (GDPO0000059) with property chain.

---

## [1.4.7] - 2025-08-21

### Added
- **Evaluation infrastructure**: `design evaluation record` (GDPO0000044), `design evaluation process` (GDPO0000055), `evaluation method specification` (GDPO0000052).
- **Evaluation properties**: `is about evaluated artifact` (GDPO0000045), `against principle` (GDPO0000046), `has score` (GDPO0000047), `is about using method` (GDPO0000048), `assessed_on` (GDPO0000050), `evaluation carried out by` (GDPO0000051).

---

## [1.4.6] - 2025-08-21

### Added
- Initial process classes: `design use process`, `design comprehension process`, `design interaction process`, `design innovation process`, `design communication process`.

---

## [1.4] - 2025-08-21

### Added
- **Rams Ten Principles Specification** class (GDPO0000034) with composition axioms.
- **Principle specification** class (GDPO0000035).
- Named individuals for ten canonical Rams statements (GDPO0000066–GDPO0000075).
- `owl:AllDifferent` assertion for principle statement individuals.

---

## [1.3] - 2025-08-21

### Added
- Artifact-side quality classes: `design aesthetic quality`, `design unobtrusiveness quality`, `design thoroughness quality`, `design minimalism quality`, `design environmental friendliness`.
- Disposition classes: `design understandability`, `design honesty`, `design durability`.
- Function class: `design usefulness`.
- Relational quality: `design innovativeness`.

---

## [1.2] - 2025-08-21

### Added
- Initial ten principle classes under `design principle`.
- Basic ontology metadata and imports.

---

## [1.0] - 2025-08-18

### Added
- Initial ontology structure with BFO 2020 and CCO alignment.
- `design principle` as subclass of `cco:directive information content entity`.

---

[4.0.3]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v4.0.2...v4.0.3
[4.0.2]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v4.0.1...v4.0.2
[4.0.1]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v4.0.0...v4.0.1
[4.0.0]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v3.0.0...v4.0.0
[3.0.0]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.5.1...v3.0.0
[1.5.1]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.4.9...v1.5.1
[1.4.9]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.4.7...v1.4.9
[1.4.7]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.4.6...v1.4.7
[1.4.6]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.4...v1.4.6
[1.4]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.3...v1.4
[1.3]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.2...v1.3
[1.2]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/compare/v1.0...v1.2
[1.0]: https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/releases/tag/v1.0
