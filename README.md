# Good Design Principles Ontology (GDPO)

[![Version](https://img.shields.io/badge/version-4.0.0-blue.svg)](releases/v4.0.0/)
[![BFO](https://img.shields.io/badge/BFO-2020-green.svg)](http://purl.obolibrary.org/obo/bfo.owl)
[![CCO](https://img.shields.io/badge/CCO-2024--11-green.svg)](https://www.commoncoreontologies.org/)
[![OWL](https://img.shields.io/badge/OWL-2%20DL-orange.svg)](https://www.w3.org/TR/owl2-overview/)

An applied ontology that formalizes Dieter Rams' *Ten Principles of Good Design* within a rigorous semantic framework (BFO 2020, CCO 2.0).

## Quick Start

**Current version:** [`current/gdpo.ttl`](current/gdpo.ttl)

```turtle
@prefix gdpo: <https://www.ramsprinciplesofgooddesign.com/> .

# Import the ontology
owl:imports gdpo:GoodDesignPrinciplesOntology20260116v4.0.0 .
```

## Overview

Rams' philosophy has shaped generations of products—from Braun's SK4 record player to Apple's iPhone—but until now it has remained a human-readable philosophy rather than a machine-interpretable framework.

**GDPO changes that**, turning "good design" into structured, computable data that can be embedded directly into design workflows.

### Key Features

| Feature | Description |
|---------|-------------|
| **BFO 2020 Conformant** | Full alignment with Basic Formal Ontology |
| **CCO Integration** | Uses Common Core Ontologies for agents and artifacts |
| **OWL 2 DL** | Compatible with standard reasoners (HermiT, Pellet, ELK) |
| **Evaluation Framework** | Model assessments with scores, methods, and provenance |
| **Lifecycle Coverage** | Sourcing → Manufacturing → Distribution → Use → End-of-life |

### The Ten Principles

Each principle is modeled as a directive information content entity (DICE) with:
- A **class** representing the principle category
- A **named individual** capturing Rams' canonical statement
- Links to **artifact-side qualities, functions, or dispositions**

| # | Principle | Artifact Target |
|---|-----------|-----------------|
| 1 | Innovativeness | Quality (relational) |
| 2 | Usefulness | Function |
| 3 | Aesthetics | Quality |
| 4 | Understandability | Disposition |
| 5 | Unobtrusiveness | Quality |
| 6 | Honesty | Disposition |
| 7 | Durability | Disposition |
| 8 | Thoroughness | Quality |
| 9 | Environmental Friendliness | Quality |
| 10 | Minimalism | Quality |

## Repository Structure

```
GoodDesignPrinciplesOntology/
├── README.md                 # This file
├── CHANGELOG.md              # Version history
├── current/
│   └── gdpo.ttl              # Canonical current version
├── releases/
│   └── v4.0.0/
│       ├── GoodDesignPrinciplesOntology-v4.0.0.ttl
│       └── RELEASE_NOTES_v4.0.0.md
├── docs/
│   └── competency-questions.md
└── examples/
    └── sparql-queries.md
```

## Documentation

- **[CHANGELOG.md](CHANGELOG.md)** — Full version history with migration notes
- **[Competency Questions](docs/competency-questions.md)** — 20 questions GDPO answers
- **[Design Pattern Diagrams](docs/design-pattern-diagrams.md)** — Mermaid visualizations for each CQ
- **[SPARQL Examples](examples/sparql-queries.md)** — Ready-to-use queries

## Use Cases

### Design Evaluation
Capture structured assessments of products against Rams' principles:

```turtle
:iPhone14Evaluation a gdpo:DesignEvaluation ;
    gdpo:is_about_evaluated_artifact :iPhone14 ;
    gdpo:against_principle gdpo:GDPO0000029 ;  # minimalism
    gdpo:has_score "0.85"^^xsd:decimal ;
    gdpo:assessed_on "2026-01-15T10:00:00Z"^^xsd:dateTime .
```

### Lifecycle Integration
Link principles to lifecycle stages for sustainability analysis:

```turtle
gdpo:GDPO0000028  # principle of environmental friendliness
    gdpo:has_prescription_component [
        a gdpo:DesignProcessPrescription ;
        cco:prescribes gdpo:GDPO0000040 ;  # end-of-life handling
        gdpo:applies_during_lifecycle_stage gdpo:GDPO0000040
    ] .
```

### Communicative Honesty Assessment
Evaluate marketing claims against actual product properties:

```turtle
:AdEvaluation a gdpo:DesignCommunicativeHonestyEvaluation ;
    gdpo:is_about_evaluated_artifact :ProductX ;
    gdpo:is_about_communication_content :ProductXAdCampaign ;
    gdpo:against_principle gdpo:GDPO0000025 .  # honesty
```

## Dependencies

| Ontology | Version | IRI |
|----------|---------|-----|
| BFO | 2020 | `http://purl.obolibrary.org/obo/bfo/2020/bfo.owl` |
| CCO AgentOntology | 2024-11-05 | `https://www.commoncoreontologies.org/2024-11-05/AgentOntology` |
| CCO ArtifactOntology | 2024-11-06 | `https://www.commoncoreontologies.org/2024-11-06/ArtifactOntology` |

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

## License

[To be determined]

## Acknowledgments

GDPO formalizes the design philosophy of Dieter Rams. Thanks to the BFO and CCO communities for foundational ontological infrastructure.

---

*"Less, but better." — Dieter Rams*
