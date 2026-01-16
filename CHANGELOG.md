# Changelog

All notable changes to the Good Design Principles Ontology (GDPO) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.0] - 2026-01-16

### Added

#### Named Individuals for Canonical Rams Statements
- `GDPO0000065` - rams ten principles specification 001 (canonical instance)
- `GDPO0000066` - principle of innovativeness 001 ("Good design is innovative.")
- `GDPO0000067` - principle of usefulness 001 ("Good design makes a product useful.")
- `GDPO0000068` - principle of aesthetics 001 ("Good design is aesthetic.")
- `GDPO0000069` - principle of understandability 001 ("Good design makes a product understandable.")
- `GDPO0000070` - principle of unobtrusiveness 001 ("Good design is unobtrusive.")
- `GDPO0000071` - principle of honesty 001 ("Good design is honest.")
- `GDPO0000072` - principle of durability 001 ("Good design is long-lasting.")
- `GDPO0000073` - principle of thoroughness 001 ("Good design is thorough down to the last detail.")
- `GDPO0000074` - principle of environmental friendliness 001 ("Good design is environmentally friendly.")
- `GDPO0000075` - principle of minimalism 001 ("Good design is as little design as possible.")

#### Annotation Properties
- `GDPO0000453` - has canonical statement text (relates principle statement ICE to Rams' original wording)

#### Design Communication Content Classes
- `GDPO0000446` - design communication content entity (parent class for communicated claims/disclosures)
- `GDPO0000447` - product manual content
- `GDPO0000448` - product label content
- `GDPO0000449` - product advertisement content

#### Communicative Honesty Evaluation
- `GDPO0000452` - design communicative honesty evaluation (evaluates communication artifacts against honesty principle)
- `GDPO0000450` - is about communication content (links evaluation to communication artifact)

#### Reified Prescription Architecture
- `GDPO0000061` - design process prescription (reified directive for what processes principles prescribe)
- `GDPO0000062` - has prescription component (links principle to its prescription components)
- `GDPO0000063` - applies during lifecycle stage (temporal/lifecycle qualifier for prescriptions)
- `GDPO0000064` - prescribes via prescription component (property chain for derived prescriptive semantics)

#### Honesty Basis Classes
- `GDPO0000056` - design honesty basis (material entity grounding honesty dispositions)
- `GDPO0000057` - design material honesty basis
- `GDPO0000058` - design functional honesty basis

#### Derived Properties
- `GDPO0000059` - has evaluation-relevant principle (property chain: evaluation → method → principle)
- `GDPO0000445` - used in evaluation (inverse of is about using method)

### Changed

#### Modeling Architecture
- Principle categories are now represented as classes; canonical Rams statements are named individuals with provenance
- Prescriptive semantics moved from direct `cco:prescribes` assertions to reified `design process prescription` components
- Universal ('only') restrictions replace existential restrictions where appropriate to avoid unwarranted commitments
- `GDPO0000064` intentionally not a subproperty of `cco:prescribes` to avoid non-regular role hierarchy (HermiT compatibility)

#### Honesty Modeling
- Communicative honesty now modeled via evaluation records of communication artifacts, not as product-borne disposition
- Material and functional honesty remain as dispositions inhering in artifacts
- Added `BFO_0000218` (has basis) axioms linking honesty dispositions to their structural grounds

#### Design Evaluation
- `GDPO0000044` now has full equivalent class definition with required properties
- Added `owl:AllDifferent` assertion for the ten principle statement individuals

#### Editorial Notes
- Extensive updates to `skos:editorialNote` across all principle and quality classes
- Added modeling notes explaining prescription component architecture
- Clarified scope notes for lifecycle stage processes

### Deprecated
- Direct use of `cco:prescribes` on principle classes (use prescription components instead)
- Communicative honesty as a disposition class (use communicative honesty evaluation instead)

### Fixed
- Property chain in `GDPO0000064` structured to avoid OWL 2 DL reasoning failures
- Lifecycle stage process disjointness axioms properly scoped

## [3.0.0] - 2026-01-15

### Changed
- Major restructuring of principle-to-process relationships
- Updated CCO alignment to 2024-11 release

## [1.5.1] - 2025-12-29

### Added
- Initial lifecycle stage process classes
- Evaluation method specification class

## [1.4.9] - 2025-08-21

### Added
- Design evaluation record class
- Evaluation properties (against principle, has score, assessed on)

## [1.4.7] - 2025-08-21

### Changed
- Refined honesty disposition subclasses

## [1.4.6] - 2025-08-21

### Added
- Material and functional honesty disposition classes

## [1.4] - 2025-08-21

### Added
- Initial design process types
- Quality and disposition classes for artifacts

## [1.3] - 2025-08-21

### Changed
- Principle class hierarchy refinements

## [1.2] - 2025-08-21

### Added
- Initial ten principle classes

## [1.0] - 2025-08-18

### Added
- Initial ontology release
- BFO 2020 and CCO 2.0 imports
- Core design principle class
- Rams ten principles specification class

---

## Version Numbering

GDPO uses semantic versioning:
- **Major** (X.0.0): Breaking changes to class IRIs, property semantics, or modeling patterns
- **Minor** (0.X.0): New classes/properties that don't break existing usage
- **Patch** (0.0.X): Bug fixes, annotation updates, editorial clarifications
