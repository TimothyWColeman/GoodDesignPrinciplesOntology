# GDPO v4.0.0 Release Notes

**Release Date:** January 16, 2026  
**Prior Version:** v3.0.0 (2026-01-15)

## Overview

Version 4.0.0 represents a significant architectural evolution of the Good Design Principles Ontology. This release introduces named individuals for Rams' canonical principle statements, a reified prescription architecture for improved reasoning, and a comprehensive treatment of communicative honesty via evaluation records.

## Highlights

### 🎯 Canonical Principle Statement Individuals

The ten Rams principles are now represented as **named individuals** (ICEs) with full provenance:

```turtle
gdpo:GDPO0000066 a owl:NamedIndividual, gdpo:GDPO0000020 ;
    rdfs:label "principle of innovativeness 001"@en ;
    dcterms:creator "Dieter Rams"@en ;
    gdpo:GDPO0000453 "Good design is innovative."@en .
```

This separates the **principle category** (class) from the **canonical statement** (individual), enabling:
- Multiple principle specifications from different authors
- Provenance tracking for each formulation
- Historical comparison across design frameworks

### 🔗 Reified Prescription Architecture

Prescriptive semantics are now modeled via **design process prescription** components:

```
principle of usefulness
  → has prescription component → [design process prescription]
      → cco:prescribes → design use process
      → applies during lifecycle stage → design use and maintenance process
```

This avoids non-regular role hierarchies that cause OWL 2 DL reasoners (HermiT) to fail, while preserving full expressivity.

### 📋 Communicative Honesty as Evaluation

**Breaking change:** Communicative honesty is no longer modeled as a product-borne disposition. Instead:

- `design communicative honesty evaluation` assesses whether communication artifacts (manuals, labels, ads) honestly represent a product
- New classes: `design communication content entity`, `product manual content`, `product label content`, `product advertisement content`
- Material and functional honesty remain as artifact dispositions

### 🏗️ Honesty Basis Classes

New classes ground honesty dispositions in material structure via `BFO:has basis`:

- `design honesty basis` — parent class for structural truthmakers
- `design material honesty basis` — features aligning appearance with actual materials
- `design functional honesty basis` — features aligning affordances with actual capabilities

## Breaking Changes

| Change | Migration Path |
|--------|----------------|
| Direct `cco:prescribes` on principles | Use `has prescription component` → prescription → `cco:prescribes` |
| Communicative honesty disposition | Use `design communicative honesty evaluation` records |
| Principle class = canonical statement | Instantiate principle classes; use individuals for specific statements |

## New IRIs

### Classes
- `GDPO0000446` design communication content entity
- `GDPO0000447` product manual content  
- `GDPO0000448` product label content
- `GDPO0000449` product advertisement content
- `GDPO0000452` design communicative honesty evaluation
- `GDPO0000061` design process prescription
- `GDPO0000056` design honesty basis
- `GDPO0000057` design material honesty basis
- `GDPO0000058` design functional honesty basis

### Object Properties
- `GDPO0000062` has prescription component
- `GDPO0000063` applies during lifecycle stage
- `GDPO0000064` prescribes via prescription component
- `GDPO0000059` has evaluation-relevant principle
- `GDPO0000450` is about communication content
- `GDPO0000445` used in evaluation

### Annotation Properties
- `GDPO0000453` has canonical statement text

### Named Individuals
- `GDPO0000065` rams ten principles specification 001
- `GDPO0000066`–`GDPO0000075` (ten principle statement individuals)

## Compatibility

| Dependency | Version |
|------------|---------|
| BFO | 2020 |
| CCO AgentOntology | 2024-11-05 |
| CCO ArtifactOntology | 2024-11-06 |
| OWL Profile | OWL 2 DL |
| Tested Reasoners | HermiT 1.4.x, Pellet, ELK |

## Installation

Download the TTL file and import into your ontology editor:

```turtle
owl:imports <https://www.ramsprinciplesofgooddesign.com/GoodDesignPrinciplesOntology20260116v4.0.0> .
```

Or load directly:
```bash
robot merge --input gdpo-v4.0.0.ttl --output merged.owl
```

## Documentation

- [CHANGELOG.md](CHANGELOG.md) — Full version history
- [docs/competency-questions.md](docs/competency-questions.md) — 20 competency questions
- [examples/sparql-queries.md](examples/sparql-queries.md) — Example SPARQL queries

## Citation

```bibtex
@misc{coleman2026gdpo,
  author = {Coleman, Timothy W.},
  title = {Good Design Principles Ontology (GDPO)},
  version = {4.0.0},
  year = {2026},
  url = {https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology}
}
```

## Acknowledgments

GDPO formalizes the design philosophy of Dieter Rams within the BFO 2020 and CCO frameworks. Thanks to the BFO and CCO communities for foundational work.
