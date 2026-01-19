# Good Design Principles Ontology (GDPO)

![version](https://img.shields.io/badge/version-4.0.3-blue)
![BFO](https://img.shields.io/badge/BFO-2020-green)
![CCO](https://img.shields.io/badge/CCO-2024--11-green)
![OWL](https://img.shields.io/badge/OWL-2%20DL-orange)

An applied ontology that formalizes Dieter Rams' *Ten Principles of Good Design* within a rigorous semantic framework (BFO 2020, CCO 2.0).

## Quick Start

**Current version:** [`current/gdpo.ttl`](current/gdpo.ttl)

```turtle
@prefix gdpo: <https://www.ramsprinciplesofgooddesign.com/> .

# Import the ontology
owl:imports <https://www.ramsprinciplesofgooddesign.com/GoodDesignPrinciplesOntology20260116v4.0.3> .
```

---

## Making Rams' Philosophy Actionable

The **Good Design Principles Ontology (GDPO)** is an applied ontology that formalizes Dieter Rams' *Ten Principles of Good Design* within a rigorous semantic framework (**BFO 2020, CCO 2.0**).

Rams' philosophy has shaped generations of products—from Braun's SK4 record player to Apple's iPhone—but until now it has remained a human-readable philosophy rather than a machine-interpretable framework.

**GDPO changes that**, turning "good design" into structured, computable data that can be embedded directly into the workflows of design-driven companies.

---

## Why GDPO Matters for Industry

Leading firms such as **Apple, IDEO, and Braun** already anchor their design culture in principles like *honesty*, *minimalism*, and *usefulness*. But today's design teams operate in complex product lifecycle environments:

* Global supply chains
* Sustainability reporting
* Regulatory compliance
* Digital twin ecosystems

Rams' principles, in their original narrative form, cannot be measured, audited, or integrated into these systems.

**GDPO provides the missing bridge:**

* **Structured Design Evaluation**  
  Captures who reviewed a design, when, using which method, against which principle, and with what score.  
  → Evaluations become traceable, auditable, and comparable.

* **Lifecycle & Sustainability Integration**  
  Principles like durability and environmental friendliness are tied to lifecycle processes (*sourcing, manufacturing, use, end-of-life*).  
  → Links Rams' ideals to ESG dashboards, supply chain ethics, and circular economy metrics.

* **Design Toolchain Embedding**  
  Works inside tools designers already use (Figma, CAD/PLM, generative design).  
  → Dashboards can flag violations (e.g., minimalism, durability) or auto-score prototypes.

---

## Innovation Potential

GDPO is not just a compliance framework—it's an **innovation enabler**:

* **AI-Assisted Design**  
  Serves as a constraint layer for generative design tools, ensuring outputs respect Rams' principles.  
  → Imagine AI prototypes that are honest, minimal, and durable by default.

* **Cross-Company Benchmarking**  
  Formalized principles allow companies to benchmark design quality across portfolios and industries.

* **Future-Proofing Brand Integrity**  
  Enforces timeless principles in a world dominated by speed and novelty.  
  → Transforms Rams' motto *"Less, but better"* into a living rule across development stages.

---

## Value Proposition

* **For Apple**: Extend Jony Ive's Rams-inspired legacy by embedding "good design" into AI-assisted prototyping and lifecycle compliance.
* **For IDEO**: Strengthen human-centered design methodologies with computable principles, creating new opportunities for scalable, principle-driven innovation.
* **For Braun**: Reconnect with Rams' origins by auditing and evolving products against the very ideals the company introduced.

---

## Ontology Overview

The Good Design Principles Ontology (GDPO) formally represents Rams' Ten Principles of Good Design as a hierarchy of classes within the framework of Basic Formal Ontology (BFO 2020) and aligned with the Common Core Ontologies (CCO 2.0).

### Modeling Approach

* Each of Rams' principles is represented as a class under `design principle` (a directive information content entity).
* Every principle prescribes one or more design process types via reified `design process prescription` components.
* Process classes are occurrents that have participants: an Agent and a Material Entity (the designed artifact).
* Realizable entities are modeled on the artifact side: functions and dispositions *inhere in* a material entity and are *realized in* the appropriate process types; qualities (e.g., aesthetic, unobtrusiveness, minimalism, thoroughness) *inhere in* a material entity (qualities are not realized).
* The ten canonical Rams statements are represented as named individuals (ICEs) with provenance and canonical statement text.
* Evaluation results (conformance/nonconformance) are represented in evaluation records rather than baked into process definitions.

### The Ten Principles

Each of Rams' ten principles is represented as a distinct class under `design principle`:

| # | Principle Class | Canonical Statement |
|---|-----------------|---------------------|
| 1 | `principle of innovativeness` | Good design is innovative |
| 2 | `principle of usefulness` | Good design makes a product useful |
| 3 | `principle of aesthetics` | Good design is aesthetic |
| 4 | `principle of understandability` | Good design makes a product understandable |
| 5 | `principle of unobtrusiveness` | Good design is unobtrusive |
| 6 | `principle of honesty` | Good design is honest |
| 7 | `principle of durability` | Good design is long-lasting |
| 8 | `principle of thoroughness` | Good design is thorough down to the last detail |
| 9 | `principle of environmental friendliness` | Good design is environmentally friendly |
| 10 | `principle of minimalism` | Good design is as little design as possible |

---

## Key Design Patterns

### 1. Prescription Component Pattern

Principles prescribe processes via reified prescription components:

```
principle of usefulness
  └─ has prescription component → design process prescription
       ├─ cco:prescribes → design use process
       └─ applies during lifecycle stage → design use and maintenance process
```

### 2. Evaluation Record Pattern

Evaluation records capture assessments with full provenance:

```
design evaluation record
  ├─ is about evaluated artifact → material entity
  ├─ against principle → design principle
  ├─ is about using method → evaluation method specification
  ├─ has score component → design evaluation score
  │     ├─ score value → xsd:decimal
  │     ├─ score for principle → design principle
  │     └─ has score scale → evaluation score scale specification
  └─ assessed during temporal region → BFO:temporal region
```

### 3. Temporal Region Indexing Pattern (v4.0.2)

GDPO v4.0.2 introduces BFO 2020–compliant temporal indexing:

**For Evaluation Records:**
* `assessed_on` (GDPO0000050): Legacy xsd:dateTime literal for lightweight timestamping
* `assessed during temporal region` (GDPO0000468): BFO temporal region for full ontological modeling

**For Prescriptions:**
* `applies during lifecycle stage` (GDPO0000063): Coarse lifecycle-stage qualifier
* `applies during temporal region` (GDPO0000467): Fine-grained BFO temporal region

Use temporal regions when you need:
- Integration with time ontologies (e.g., OWL-Time)
- Interval-based reasoning (evaluations spanning periods)
- Full BFO 2020 continuant–occurrent discipline

### 4. Aims-At Pattern (v4.0.2)

The `aims at artifact-side target` property links principles to their intended targets (quality/function/disposition types) using OWL2 punning:

```
principle of aesthetics
  └─ aims at artifact-side target → design aesthetic quality (as punned individual)
```

**Note:** OWL range restrictions are intentionally omitted to avoid treating punned targets as instances. Validate via SHACL (see `gdpo-shapes.ttl`).

---

## Class and Property Inventory (v4.0.2)

### Core Classes

| Class | Description |
|-------|-------------|
| `design principle` | Directive ICE prescribing constraints or aims for artifacts/processes |
| `design process prescription` | Directive ICE specifying prescribed process types with applicability conditions |
| `design evaluation record` | ICE recording an assessment against one or more principles |
| `design evaluation process` | Process producing evaluation records |
| `evaluation method specification` | ICE specifying evaluation procedures/rubrics |
| `design evaluation score` | Reified score component with value, principle, and scale |
| `evaluation score scale specification` | ICE defining score interpretation (bounds, units) |

### Process Classes

| Class | Lifecycle Stage |
|-------|-----------------|
| `design sourcing process` | Sourcing |
| `design manufacturing process` | Manufacturing |
| `design distribution process` | Distribution |
| `design use and maintenance process` | Use/Maintenance |
| `design end-of-life handling process` | End-of-Life |
| `design innovation process` | Cross-cutting |
| `design interaction process` | Use (agent–artifact interaction) |
| `design comprehension process` | Use (cognitive uptake) |
| `design communication process` | Cross-cutting (claims, docs, ads) |

### Key Object Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `has prescription component` | design principle | design process prescription | Links principle to its prescriptive clauses |
| `applies during lifecycle stage` | design process prescription | design lifecycle stage process | Lifecycle-stage qualifier |
| `applies during temporal region` | design process prescription | BFO:temporal region | Temporal scope (v4.0.2) |
| `against principle` | design evaluation record | design principle | Evaluation criterion |
| `is about evaluated artifact` | design evaluation record | BFO:material entity | Evaluated artifact |
| `assessed during temporal region` | design evaluation record | BFO:temporal region | When assessed (v4.0.2) |
| `has score component` | design evaluation record | design evaluation score | Reified score |
| `aims at artifact-side target` | directive ICE | (punned class) | Principle's intended target |

---

## Competency Questions

### About Principles and Processes

1. Which design processes does the principle of innovativeness prescribe?
2. Which principle of good design prescribes a design use process?
3. Which design evaluation methods operationalize the principle of minimalism?
4. Which design principles apply to a given design lifecycle process?
5. Which qualities or dispositions are linked to a specific design principle?

### About Evaluations

6. What artifacts (material entities) have been the subject of a design evaluation?
7. Which principles was a particular artifact evaluated against?
8. Which evaluation method specification was used in a given design evaluation?
9. What numeric score was assigned to an artifact in its last design evaluation?
10. On what date was an artifact last assessed for conformity to Rams' principles?
11. During which temporal region was an evaluation conducted? *(v4.0.2)*
12. What are all evaluations conducted within a specified temporal interval? *(v4.0.2)*

### About Methods

13. Which evaluation method specification prescribes a design evaluation process?
14. Which principles does a given evaluation method specification operationalize?
15. Are there multiple methods used to evaluate the same principle?
16. Which principle is most frequently associated with evaluation methods?

### About Qualities and Dispositions

17. Which qualities (e.g., aesthetic quality, minimalism quality) inhere in a given artifact?
18. Which dispositions (e.g., honesty, durability) of an artifact are realized in which processes?
19. Which aspects of honesty (material, functional, communicative) does a given artifact exhibit?

### About Prescriptions and Temporal Scope

20. Which principles are part of the Rams ten principles specification?
21. How does the ontology distinguish between qualities and principles?
22. Which agents carried out a design evaluation process for a given artifact?
23. Which prescriptions apply during a specified temporal region? *(v4.0.2)*
24. What is the temporal scope of a design process prescription? *(v4.0.2)*

---

## SPARQL Queries

### CQ1: Which design processes does the principle of innovativeness prescribe?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX cco: <https://www.commoncoreontologies.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?process ?processLabel WHERE {
  ?principle rdfs:label "principle of innovativeness"@en .
  ?principle gdpo:GDPO0000062 ?prescription .
  ?prescription cco:ont00001942 ?process .
  ?process rdfs:label ?processLabel .
}
```

### CQ7: Which principles was a particular artifact evaluated against?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label ?principleLabel .
}
```

### CQ8: Which evaluation method was used in a given design evaluation?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?method ?methodLabel WHERE {
  ?evaluation rdfs:label "SK4 evaluation 1970"@en .
  ?evaluation gdpo:GDPO0000048 ?method .
  ?method rdfs:label ?methodLabel .
}
```

### CQ9: What numeric score was assigned to an artifact? (Legacy dateTime)

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?date ?score WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000050 ?date .
  ?evaluation gdpo:GDPO0000047 ?score .
}
ORDER BY DESC(?date)
LIMIT 1
```

### CQ9b: Reified score pattern with principle and scale

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?artifact ?principle ?scoreValue ?scaleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000457 ?scoreComponent .
  ?scoreComponent gdpo:GDPO0000459 ?scoreValue .
  ?scoreComponent gdpo:GDPO0000458 ?principle .
  ?principle rdfs:label ?principleLabel .
  OPTIONAL {
    ?scoreComponent gdpo:GDPO0000460 ?scale .
    ?scale rdfs:label ?scaleLabel .
  }
}
```

### CQ11: During which temporal region was an evaluation conducted? (v4.0.2)

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?artifact ?temporalRegion WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000468 ?temporalRegion .
}
```

### CQ12: All evaluations within a temporal interval (v4.0.2)

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT ?evaluation ?artifact ?principleLabel WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label ?principleLabel .
  ?evaluation gdpo:GDPO0000468 ?tempRegion .
  # Filter by interval if using OWL-Time integration
  # ?tempRegion time:inXSDDateTimeStamp ?ts .
  # FILTER(?ts >= "2025-01-01T00:00:00Z"^^xsd:dateTime)
}
```

### CQ23: Which prescriptions apply during a specified temporal region? (v4.0.2)

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?prescription ?prescriptionLabel ?temporalRegion WHERE {
  ?prescription a gdpo:GDPO0000061 .
  ?prescription rdfs:label ?prescriptionLabel .
  ?prescription gdpo:GDPO0000467 ?temporalRegion .
}
```

### CQ20: Which agents carried out a design evaluation process?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?process ?agent ?agentLabel ?artifact WHERE {
  ?process a gdpo:GDPO0000055 .
  ?process gdpo:GDPO0000051 ?agent .
  ?agent rdfs:label ?agentLabel .
  ?process gdpo:GDPO0000465 ?artifact .
}
```

---

## Validation

GDPO includes SHACL shapes for validation. See `gdpo-shapes.ttl` for:

* Evaluation record completeness (artifact, principle, temporal region)
* Score component structure (value, principle, scale)
* Aims-at target constraints (must be a class, subclass of quality/function/disposition)

---

## Files in This Repository

| File | Description |
|------|-------------|
| `GoodDesignPrinciplesOntology20260116v4_0_2.ttl` | Current release (v4.0.2) |
| `gdpo-shapes.ttl` | SHACL validation shapes |
| `gdpo-example-abox.ttl` | Example instance data |
| `CHANGELOG.md` | Version history |
| `README.md` | This file |

---

## Interoperability

All assertions use BFO 2020 relations and CCO classes for agents and artifacts, ensuring compatibility with adjacent ontologies and data pipelines.

**Imports:**
* BFO 2020 (`http://purl.obolibrary.org/obo/bfo/2020/bfo.owl`)
* CCO Agent Ontology (`https://www.commoncoreontologies.org/2024-11-05/AgentOntology`)
* CCO Artifact Ontology (`https://www.commoncoreontologies.org/2024-11-06/ArtifactOntology`)

---

## License

[To be specified]

---

## Citation

If you use GDPO in academic work, please cite:

> Coleman, T. W. (2026). The Good Design Principles Ontology (GDPO): A BFO 2020–conformant ontology of Rams' principles, prescriptions, and evaluation records. *Applied Ontology* [forthcoming].

---

## Contact

Timothy W. Coleman  
[GitHub Issues](https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/issues)
