# Good Design Principles Ontology (GDPO)

![version](https://img.shields.io/badge/version-4.0.3-blue)
![BFO](https://img.shields.io/badge/BFO-2020-green)
![CCO](https://img.shields.io/badge/CCO-2.0%20%282024%29-green)
![OWL](https://img.shields.io/badge/OWL-2%20DL-orange)

An applied ontology for representing Dieter Rams' *Ten Principles of Good Design* as normative information content, artifact-side target expressions, prescription components, evaluation methods, and evidence-bearing evaluation records.

## Quick Start

**Current version:** [`ontology/gdpo-4.0.3.ttl`](ontology/gdpo-4.0.3.ttl)

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .

<http://example.org/my-design-review-ontology>
  owl:imports <https://www.ramsprinciplesofgooddesign.com/GoodDesignPrinciplesOntology> .
```

For local editing in Protege or other OWL tools, use [`ontology/catalog-v001.xml`](ontology/catalog-v001.xml) to resolve BFO 2020 and the stable CCO 2.0 imports.

For a compact review path, start with [`docs/reviewer-guide.md`](docs/reviewer-guide.md).

---

## Principles Are Not Properties

The **Good Design Principles Ontology (GDPO)** is a BFO 2020 and CCO 2.0 aligned ontology for representing Rams' ten principles as **prescriptive information content entities**, not as qualities, functions, or dispositions inhering in artifacts.

The core modeling problem is not whether normative design principles can be represented realistically. Rams' statements, copies of those statements, design processes, evaluation processes, evaluation records, methods, scores, artifacts, qualities, functions, dispositions, and material bases all have ordinary ontological places. The challenge is to connect them without collapsing a directive principle into the artifact-side entities it concerns.

GDPO addresses that challenge by distinguishing:

* principle categories and canonical principle-statement individuals
* artifact-side qualities, functions, dispositions, material bases, processes, and communication content
* design process prescriptions and their lifecycle or temporal applicability
* evaluation methods and evaluation records
* explicit evaluation criteria and method-derived relevance

---

## Why GDPO Matters for Evaluation

Design teams, reviewers, and governance processes routinely ask whether an artifact is useful, honest, durable, minimal, environmentally responsible, or thorough. Without a formal representation, these judgments remain trapped in narrative reports, loosely structured rubrics, or checklist spreadsheets.

**GDPO provides the missing bridge:**

* **Normative Design Guidance**  
  Represents Rams' principles as directive information content entities while keeping them distinct from artifact-side qualities, functions, and dispositions.

* **Prescription Traceability**  
  Connects principle categories to explicit `design process prescription` components, including prescribed process types and lifecycle-stage or temporal qualifiers.

* **Structured Design Evaluation**  
  Represents evaluations as information content entities about an evaluated artifact, against an explicit principle criterion, using an optional method, during a BFO temporal region, with optional score components.

* **Method-Derived Relevance**  
  Distinguishes principles explicitly selected as evaluation criteria from principles made relevant by a method that operationalizes them.

* **Modality-Specific Evaluation**  
  Supports specializations such as `design communicative honesty evaluation`, where the assessment concerns manuals, labels, advertisements, product descriptions, interface messages, or other communication content.

---

## Contribution

GDPO is not an automated theory of design quality and does not decide by itself whether an artifact is good design. Its contribution is a reusable ontology pattern for connecting normative design principles to target expressions, prescribed processes, evaluation methods, and evidence-bearing records.

The ontology implements three primary patterns from the accompanying manuscript:

* **Prescription-component pattern**  
  Separates what a principle concerns on the artifact side from what it prescribes at the process level.

* **Criterion-method relevance pattern**  
  Separates explicit criterion selection from broader method-derived evaluative relevance.

* **Modality-specific evaluation pattern**  
  Refines principle-keyed evaluation classes by subject matter or evidence modality.

These patterns build on an About-the-Unreal-style class-expression strategy for representing possible, future, or not-yet-instantiated targets without introducing dummy target individuals or punned proxy instances.

---

## Ontology Overview

The Good Design Principles Ontology represents Rams' ten principles using BFO 2020 and the Common Core Ontologies 2.0.

### Modeling Approach

* Each Rams principle category is represented as a class under `design principle`, a subclass of CCO `Prescriptive Information Content Entity`.
* Principle target content is represented through `aims at artifact-side target only TargetClassExpression`, where the filler is an OWL class expression.
* No punned class-as-individual target proxies and no `owl:hasValue` target restrictions are used.
* Prescriptive force is represented separately through `design process prescription` components.
* Lifecycle-stage applicability is represented using stage process types such as sourcing, manufacturing, distribution, use/maintenance, and end-of-life handling.
* The ten canonical Rams statements are represented as named individuals typed under their corresponding principle categories.
* Evaluation results are represented as `design evaluation record` individuals, not as qualities inhering in the artifact and not as the evaluation process itself.
* Scores are represented preferably as reified `design evaluation score` components with a value, principle, and score scale.
* `has material bearer` is included only as lightweight material-bearer provenance for information content entities; it is not a replacement for the full BFO concretization pattern.

### The Ten Principles

Each Rams principle is represented as a principle category class with a canonical statement individual.

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

### 1. Target-Expression Pattern

Principles are related to their artifact-side or communication-side targets through universal restrictions over class expressions.

```text
principle of honesty
  SubClassOf:
    aims at artifact-side target only
      (
        design material honesty
        or design functional honesty
      )
```

The target expression constrains the kinds of entities the principle concerns. It does not assert that any particular artifact already bears the relevant quality, function, disposition, material basis, process, or communication content.

### 2. Prescription Component Pattern

Principles carry prescriptive process content through explicit prescription components.

```text
principle of usefulness
  SubClassOf:
    has prescription component some
      (
        design process prescription
        and prescribes only design use process
        and applies during lifecycle stage only design use and maintenance process
      )
```

For multi-stage applicability, GDPO uses a union filler rather than repeated `only` restrictions.

### 3. Evaluation Record Pattern

Evaluation records capture assessments with explicit criterion, time, method, artifact, and score structure.

```text
design evaluation record
  EquivalentTo:
    information content entity
    and is about evaluated artifact some material entity
    and against principle some design principle
    and assessed during temporal region some BFO temporal region
```

Optional relations add method use, score components, communication content, material bearer provenance, and evaluation-process provenance.

### 4. Criterion-Method Relevance Pattern

GDPO distinguishes explicit criterion selection from method-derived relevance.

```text
is about using method o operationalizes principle
  SubPropertyOf:
    has evaluation-relevant principle
```

An evaluation can be explicitly against one principle while using a method that operationalizes additional principles.

### 5. Modality-Specific Evaluation Pattern

`design communicative honesty evaluation` is defined as a kind of `design honesty evaluation` that is about communication content.

```text
design communicative honesty evaluation
  EquivalentTo:
    design honesty evaluation
    and is about communication content some design communication content entity
```

This supports assessments involving manuals, labels, advertisements, product descriptions, interface messages, or other communicated claims.

---

## Class and Property Inventory

GDPO 4.0.3 contains:

* 56 named classes
* 22 named object properties
* 3 named datatype properties
* 1 local annotation property
* 21 named individuals

### Core Classes

| Class | Description |
|-------|-------------|
| `design principle` | Directive ICE that prescribes constraints or aims concerning artifact-side targets or design processes |
| `principle specification` | Directive ICE organizing one or more principle components |
| `rams ten principles specification` | Principle specification containing the ten Rams principle categories |
| `design process prescription` | Directive ICE specifying prescribed process types and optional applicability qualifiers |
| `evaluation method specification` | Prescriptive ICE specifying a procedure, rubric, or protocol for evaluation |
| `design evaluation process` | Process in which an agent assesses an artifact and produces an evaluation record |
| `design evaluation record` | ICE recording an assessment against one or more design principles |
| `design evaluation score` | Reified score component with value, principle, and scale |
| `evaluation score scale specification` | ICE defining how score values should be interpreted |

### Artifact-Side Target Classes

| Kind | Classes |
|------|---------|
| Qualities | `design innovativeness`, `design aesthetic quality`, `design unobtrusiveness quality`, `design thoroughness quality`, `design environmental friendliness`, `design minimalism quality` |
| Function | `design usefulness` |
| Dispositions | `design understandability`, `design honesty`, `design durability`, `design material honesty`, `design functional honesty` |
| Material bases | `design honesty basis`, `design material honesty basis`, `design functional honesty basis` |

### Process Classes

| Class | Role |
|-------|------|
| `design innovation process` | Process producing novel or non-trivial design change |
| `design use process` | Agent operation of an artifact in context |
| `design comprehension process` | Agent formation of understanding about an artifact |
| `design interaction process` | Agent-artifact interaction involving controls, signals, and affordances |
| `design endurance process` | Process involving loads, stresses, or environmental conditions over time |
| `design aesthetic development process` | Development or refinement of perceptual form |
| `design contextual integration process` | Integration of artifact salience with setting |
| `design thoroughness assurance process` | Ensuring completeness and fit across parts and ecosystem |
| `design reduction process` | Eliminating superfluous elements |
| `design communication process` | Producing or displaying claims, documentation, labels, or advertisements |

### Lifecycle Stage Process Classes

| Class | Stage |
|-------|-------|
| `design sourcing process` | Sourcing |
| `design manufacturing process` | Manufacturing |
| `design distribution process` | Distribution |
| `design use and maintenance process` | Use and maintenance |
| `design end-of-life handling process` | End-of-life handling |

### Key Object Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `aims at artifact-side target` | CCO Prescriptive ICE | no declared OWL range | Used in universal restrictions over target class expressions |
| `has prescription component` | design principle | design process prescription | Links a principle to prescriptive components |
| `applies during lifecycle stage` | design process prescription | design lifecycle stage process | Coarse lifecycle applicability qualifier |
| `applies during temporal region` | design process prescription | BFO temporal region | Fine-grained temporal applicability qualifier |
| `is about evaluated artifact` | design evaluation record | BFO material entity | Evaluated artifact |
| `against principle` | design evaluation record | design principle | Explicit evaluation criterion |
| `is about using method` | design evaluation record | evaluation method specification | Method used |
| `operationalizes principle` | evaluation method specification | design principle | Principle measured or operationalized by a method |
| `has evaluation-relevant principle` | design evaluation record | design principle | Explicit or method-derived relevant principle |
| `is about communication content` | design evaluation record | design communication content entity | Communication content under assessment |
| `assessed during temporal region` | design evaluation record | BFO temporal region | BFO-style temporal indexing |
| `has score component` | design evaluation record | design evaluation score | Reified score component |
| `score for principle` | design evaluation score | design principle | Criterion scored |
| `has score scale` | design evaluation score | evaluation score scale specification | Score interpretation context |
| `has material bearer` | information content entity | BFO material entity | Lightweight material-bearer provenance |

---

## Competency Questions

### About Principles and Prescriptions

1. Which target class expressions are associated with each principle?
2. Which process types are prescribed through prescription components?
3. Which prescriptions apply during a given lifecycle stage?
4. Which principles are part of the Rams ten principles specification?
5. How does the ontology distinguish a principle from the artifact-side quality, function, or disposition it concerns?

### About Evaluations

6. What artifacts have been the subject of design evaluation records?
7. Which principles was a particular artifact evaluated against?
8. During which temporal region was an evaluation conducted?
9. Which evaluation method specification was used in a given evaluation?
10. What score components, score values, and score scales are associated with an evaluation?

### About Methods

11. Which evaluation method specifications operationalize which principles?
12. Which principles are evaluation-relevant by method use?
13. Which principles were explicitly selected as criteria, and which were method-derived?

### About Honesty and Communication

14. Which evaluations are honesty evaluations?
15. Which evaluations are communicative honesty evaluations?
16. Which communication content entities were assessed?
17. Which artifacts have material or functional honesty dispositions asserted in instance data?

### About Provenance

18. Which evaluation process produced a given evaluation record?
19. Which agent carried out a design evaluation process?
20. Which information content entities have lightweight material-bearer provenance?

---

## SPARQL Queries

The queries below are representative examples. For the manuscript versions, see Appendix A2.

### CQ1: Retrieve principle target expressions

```sparql
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT DISTINCT ?principleClass ?principleLabel ?targetExpression WHERE {
  ?principleClass rdfs:subClassOf gdpo:GDPO0000003 .
  FILTER(?principleClass != gdpo:GDPO0000003)

  ?principleClass rdfs:subClassOf ?restriction .
  ?restriction owl:onProperty gdpo:GDPO0000454 ;
               owl:allValuesFrom ?targetExpression .

  OPTIONAL { ?principleClass rdfs:label ?principleLabel . }
}
ORDER BY ?principleLabel
```

### CQ2: Retrieve prescribed process types from prescription components

```sparql
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX cco:  <https://www.commoncoreontologies.org/>

SELECT DISTINCT ?principleClass ?principleLabel ?processType ?processLabel WHERE {
  ?principleClass rdfs:subClassOf gdpo:GDPO0000003 .
  FILTER(?principleClass != gdpo:GDPO0000003)

  ?principleClass rdfs:subClassOf ?restriction .
  ?restriction owl:onProperty gdpo:GDPO0000062 ;
               owl:someValuesFrom ?pcExpr .

  ?pcExpr owl:intersectionOf/rdf:rest*/rdf:first ?prescribesPart .
  ?prescribesPart owl:onProperty cco:ont00001942 ;
                  owl:allValuesFrom ?processType .

  OPTIONAL { ?principleClass rdfs:label ?principleLabel . }
  OPTIONAL { ?processType rdfs:label ?processLabel . }
}
ORDER BY ?principleLabel ?processLabel
```

### CQ7: Which principles was a particular artifact evaluated against?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact ;
              gdpo:GDPO0000046 ?principle .
  OPTIONAL { ?principle rdfs:label ?principleLabel . }
}
```

### CQ8: Which method was used in a given evaluation?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?method ?methodLabel WHERE {
  ?evaluation rdfs:label "SK4 durability evaluation record (2024-06-15)"@en .
  ?evaluation gdpo:GDPO0000048 ?method .
  OPTIONAL { ?method rdfs:label ?methodLabel . }
}
```

### CQ9: Retrieve score components

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?scoreComp ?principle ?scoreValue ?scale WHERE {
  ?evaluation gdpo:GDPO0000457 ?scoreComp .
  OPTIONAL { ?scoreComp gdpo:GDPO0000458 ?principle . }
  OPTIONAL { ?scoreComp gdpo:GDPO0000459 ?scoreValue . }
  OPTIONAL { ?scoreComp gdpo:GDPO0000460 ?scale . }
}
```

### CQ11: During which temporal region was an evaluation conducted?

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT ?evaluation ?artifact ?temporalRegion WHERE {
  ?evaluation a gdpo:GDPO0000044 ;
              gdpo:GDPO0000045 ?artifact ;
              gdpo:GDPO0000468 ?temporalRegion .
}
```

### CQ15: Retrieve communicative honesty evaluations

```sparql
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT DISTINCT ?eval ?artifact ?content ?principleToken WHERE {
  ?eval a gdpo:GDPO0000044 ;
        gdpo:GDPO0000045 ?artifact ;
        gdpo:GDPO0000450 ?content ;
        gdpo:GDPO0000046 ?principleToken .

  ?principleToken a gdpo:GDPO0000025 .
}
```

---

## Validation

The current validation baseline is:

* parse `ontology/gdpo-4.0.3.ttl` as Turtle
* load `ontology/catalog-v001.xml` as a well-formed XML catalog
* verify there are no `owl:hasValue` target restrictions
* classify the communicative-honesty example under OWL-RL
* run the paper-aligned SK4 fixture, seven SPARQL templates, and two reported
  entailment checks from `supplement/manuscript-validation/`
* verify no GDPO entity is both an `owl:Class` and an `owl:NamedIndividual`
* verify named prescription component individuals do not use process-type classes as ABox object-property values
* verify CCO imports resolve to the stable CCO 2.0 release tag

Example local checks:

```bash
python3 -c "import rdflib; rdflib.Graph().parse('ontology/gdpo-4.0.3.ttl', format='turtle')"
xmllint --noout ontology/catalog-v001.xml
```

---

## Files in This Repository

Current repository layout:

| File/Folder | Description |
|-------------|-------------|
| `ontology/gdpo-4.0.3.ttl` | Current ontology release |
| `ontology/catalog-v001.xml` | XML catalog pinning imports to BFO 2020 and stable CCO 2.0 |
| `ontology/gdpo-4.0.3.properties` | Ontology metadata/properties file |
| `paper/` | Current manuscript file for *Principles Are Not Properties* |
| `docs/reviewer-guide.md` | Short reviewer path through the repository |
| `docs/imports-and-versioning.md` | Import pinning and version policy notes |
| `docs/design-patterns.md` | Design-pattern explanation for readers and reviewers |
| `docs/competency-questions.md` | Competency questions mapped to ontology elements |
| `queries/sparql-templates.md` | Reusable SPARQL query templates |
| `examples/gdpo-example-abox.ttl` | Minimal paper-aligned ABox example |
| `validation/` | Baseline validation checks and manuscript-alignment notes |
| `supplement/manuscript-validation/` | Reproducible article fixture, queries, entailment checks, and expected output |
| `legacy/` | Historical ontology files retained for provenance only |
| `CHANGELOG.md` | Release history and breaking changes |
| `CITATION.cff` | Repository citation metadata |
| `README.md` | This file |

---

## Interoperability

GDPO imports and reuses BFO 2020 and the Common Core Ontologies 2.0 rather than introducing local substitutes for core upper-level categories.

**Imports:**

* BFO 2020: `http://purl.obolibrary.org/obo/bfo/2020/bfo.owl`
* CCO Agent Ontology 2.0: `https://www.commoncoreontologies.org/2024-11-05/AgentOntology`
* CCO Artifact Ontology 2.0: `https://www.commoncoreontologies.org/2024-11-06/ArtifactOntology`

The local XML catalog resolves CCO imports through the stable GitHub tag:

```text
CommonCoreOntology/CommonCoreOntologies v2.0-2024-11-06
```

---

## License

GDPO is released under the Creative Commons Attribution 4.0 International License
([CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)).

---

## Citation

If you use GDPO in academic work, please cite:

> Coleman, T. W. (2026). *Principles Are Not Properties: A BFO-Grounded Ontology for Normative Design Guidance and Evaluation Traceability*. Manuscript in preparation.

---

## Contact

Timothy W. Coleman  
[GitHub Issues](https://github.com/TimothyWColeman/GoodDesignPrinciplesOntology/issues)
