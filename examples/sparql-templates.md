# GDPO SPARQL Query Templates

Version: 4.0.3  
Last Updated: 2026-01-20

This document provides representative SPARQL query templates for GDPO, corresponding to Appendix A2 of:

> Coleman, T. W. (2026). Principles Are Not Properties: A BFO-Grounded Ontology for Normative Design Guidance and Evaluation Traceability. *Unpublished manuscript*.

---

## Table of Contents

1. [A2.1 Retrieve Rams principle classes and their prescribed design process types (TBox)](#a21-retrieve-rams-principle-classes-and-their-prescribed-design-process-types-tbox-query)
2. [A2.2 Retrieve all evaluation records for a given artifact](#a22-retrieve-all-evaluation-records-for-a-given-artifact)
3. [A2.3 Compare multiple artifacts with respect to a given principle](#a23-compare-multiple-artifacts-with-respect-to-a-given-principle)
4. [A2.4 Retrieve communicative honesty evaluations](#a24-retrieve-communicative-honesty-evaluations)
5. [A2.5 Retrieve dispositions of an artifact and whether they have realizations](#a25-retrieve-dispositions-of-an-artifact-and-whether-they-have-realizations)
6. [A2.6 Retrieve evaluation method specifications and the principles they operationalize](#a26-retrieve-evaluation-method-specifications-and-the-principles-they-operationalize)
7. [A2.7 Retrieve lifecycle-stage applicability qualifiers (TBox)](#a27-retrieve-lifecycle-stage-applicability-qualifiers-for-principle-prescription-components-tbox-query)

---

## Competency Question Coverage

These templates demonstrate coverage of the motivating competency questions:

| CQ | Question | Template |
|----|----------|----------|
| CQ1 | For a given evaluated artifact, which Rams principle statement(s) were used as explicit evaluation criteria? | A2.2 |
| CQ2 | For a given evaluation record, which additional principles are in scope given the evaluation method(s) used? | A2.2 |
| CQ3 | Which evaluation method specifications operationalize which design principles? | A2.6 |
| CQ4 | Which evaluation records concern communicative honesty? | A2.4 |
| CQ5 | For a given prescription component, during which design lifecycle stage process type(s) is it intended to apply? | A2.7 |
| CQ6 | For each Rams principle category, what artifact-side target universal does it aim at, and which process types are prescribed? | A2.1 |

---

## A2.1 Retrieve Rams principle classes and their prescribed design process types (TBox query)

This query extracts (i) the aims-at artifact-side target universal from the `owl:equivalentClass` definition (using `owl:hasValue`) and (ii) the prescribed process type(s) from the principle's `has prescription component` restrictions.

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX cco: <https://www.commoncoreontologies.org/>

SELECT DISTINCT ?principleClass ?principleLabel ?target ?targetLabel ?processType ?processLabel
WHERE {
  ?principleClass rdfs:subClassOf gdpo:GDPO0000003 .
  FILTER(?principleClass != gdpo:GDPO0000003)

  # Target universal proxy from definitional equivalentClass (hasValue)
  ?principleClass owl:equivalentClass ?eq .
  ?eq owl:intersectionOf/rdf:rest*/rdf:first ?eqPart .
  ?eqPart owl:onProperty gdpo:GDPO0000454 ;
          owl:hasValue ?target .

  # Prescribed process types via prescription components
  ?principleClass rdfs:subClassOf ?sc .
  ?sc owl:onProperty gdpo:GDPO0000062 ;
      owl:someValuesFrom ?pcExpr .

  ?pcExpr owl:intersectionOf/rdf:rest*/rdf:first ?pcPart .
  ?pcPart owl:onProperty cco:ont00001942 ;
          owl:allValuesFrom ?processType .

  OPTIONAL { ?principleClass rdfs:label ?principleLabel . }
  OPTIONAL { ?target rdfs:label ?targetLabel . }
  OPTIONAL { ?processType rdfs:label ?processLabel . }
}
ORDER BY ?principleLabel ?processLabel
```

---

## A2.2 Retrieve all evaluation records for a given artifact

This query retrieves all design evaluation records for a given artifact and returns the explicit criterion principle, assessment time (a BFO temporal region), an optional datatype timestamp (`assessed_on`) when asserted, the method used (if asserted), any score components (including their scored principle, value, and scale), and—when an evaluation process is asserted—an evaluator.

The query returns one row per (evaluation record, score component) pair; evaluation records with no score components are still returned with the score variables unbound.

Method-derived evaluation relevance (CQ2) is exposed in two pragmatic ways:
1. Via the property path `gdpo:is about using method / gdpo:operationalizes principle` (which does not require OWL reasoning)
2. Via `gdpo:has evaluation-relevant principle` if a reasoner or ETL pipeline materializes the GDPO property-chain entailment

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX ex: <http://example.org/gdpo-demo/>

SELECT DISTINCT
  ?eval ?artifact ?time ?assessedOn
  ?criterion
  ?method ?methodDerivedPrinciple ?evalRelevantPrinciple
  ?scoreComp ?scoredPrinciple ?scoreValue ?scale
  ?evaluator
WHERE {
  VALUES ?artifact { ex:BraunSK4_001 }

  ?eval a gdpo:GDPO0000044 ;
        gdpo:GDPO0000045 ?artifact ;
        gdpo:GDPO0000468 ?time ;
        gdpo:GDPO0000046 ?criterion .

  OPTIONAL { ?eval gdpo:GDPO0000050 ?assessedOn . }
  OPTIONAL { ?eval gdpo:GDPO0000048 ?method . }

  # Method-derived evaluation relevance without requiring OWL materialization
  OPTIONAL { ?eval gdpo:GDPO0000048/gdpo:GDPO0000054 ?methodDerivedPrinciple . }

  # If a reasoner/ETL materializes the property-chain entailment, query it directly
  OPTIONAL { ?eval gdpo:GDPO0000059 ?evalRelevantPrinciple . }

  OPTIONAL {
    ?eval gdpo:GDPO0000457 ?scoreComp .
    OPTIONAL { ?scoreComp gdpo:GDPO0000458 ?scoredPrinciple . }
    OPTIONAL { ?scoreComp gdpo:GDPO0000459 ?scoreValue . }
    OPTIONAL { ?scoreComp gdpo:GDPO0000460 ?scale . }
  }

  OPTIONAL {
    ?proc gdpo:GDPO0000463 ?eval ;
          gdpo:GDPO0000051 ?evaluator .
  }
}
ORDER BY DESC(?assessedOn)
```

---

## A2.3 Compare multiple artifacts with respect to a given principle

This query compares artifacts with respect to a selected principle by retrieving the most recent score component for that principle per artifact. It assumes `assessed_on` (`xsd:dateTime`) is populated as an optional ordering key; if only BFO temporal regions are asserted, ordering requires an additional time ontology or dataset-specific mapping.

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

# Example: compare artifacts on the durability principle statement (gdpo:GDPO0000072)
SELECT ?artifact ?artifactLabel ?latestTime ?scoreValue
WHERE {
  VALUES ?principleToken { gdpo:GDPO0000072 }

  {
    SELECT ?artifact (MAX(?t) AS ?latestTime)
    WHERE {
      ?eval a gdpo:GDPO0000044 ;
            gdpo:GDPO0000045 ?artifact ;
            gdpo:GDPO0000050 ?t ;
            gdpo:GDPO0000457 ?scoreComp .
      ?scoreComp gdpo:GDPO0000458 ?principleToken .
    }
    GROUP BY ?artifact
  }

  ?eval a gdpo:GDPO0000044 ;
        gdpo:GDPO0000045 ?artifact ;
        gdpo:GDPO0000050 ?latestTime ;
        gdpo:GDPO0000457 ?scoreComp .

  ?scoreComp gdpo:GDPO0000458 ?principleToken ;
             gdpo:GDPO0000459 ?scoreValue .

  OPTIONAL { ?artifact rdfs:label ?artifactLabel . }
}
ORDER BY DESC(?scoreValue)
```

---

## A2.4 Retrieve communicative honesty evaluations

This query retrieves evaluation records that are about communication content and are against a principle of honesty (i.e., communicative honesty evaluations).

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT DISTINCT ?eval ?time ?timeLabel ?artifact ?artifactLabel ?content ?contentLabel
WHERE {
  ?eval a gdpo:GDPO0000044 ;
        gdpo:GDPO0000045 ?artifact ;
        gdpo:GDPO0000450 ?content ;
        gdpo:GDPO0000468 ?time ;
        gdpo:GDPO0000046 ?principleToken .

  # Require that the principle token is an instance of the honesty principle category
  ?principleToken a gdpo:GDPO0000025 .

  OPTIONAL { ?time rdfs:label ?timeLabel . }
  OPTIONAL { ?artifact rdfs:label ?artifactLabel . }
  OPTIONAL { ?content rdfs:label ?contentLabel . }
}
ORDER BY DESC(?timeLabel)
```

---

## A2.5 Retrieve dispositions of an artifact and whether they have realizations

This illustrates the difference between merely inhering dispositions and dispositions for which realization evidence is recorded.

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bfo: <http://purl.obolibrary.org/obo/>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX ex: <http://example.org/gdpo-demo/>

SELECT ?disposition ?dispositionType ?realized ?realizingProcess
WHERE {
  VALUES ?artifact { ex:BraunSK4_001 }

  ?disposition bfo:BFO_0000197 ?artifact ;
               a ?dispositionType .

  ?dispositionType rdfs:subClassOf* bfo:BFO_0000016 .  # disposition

  OPTIONAL { ?disposition bfo:BFO_0000054 ?realizingProcess . }  # realized in
  BIND(BOUND(?realizingProcess) AS ?realized)
}
ORDER BY ?dispositionType
```

---

## A2.6 Retrieve evaluation method specifications and the principles they operationalize

This query lists evaluation method specification individuals and the principle statement individuals (or other design principle tokens) they operationalize.

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT DISTINCT ?method ?methodLabel ?principleToken ?principleLabel
WHERE {
  ?method a gdpo:GDPO0000052 ;
          gdpo:GDPO0000054 ?principleToken .

  OPTIONAL { ?method rdfs:label ?methodLabel . }
  OPTIONAL { ?principleToken rdfs:label ?principleLabel . }
}
ORDER BY ?methodLabel ?principleLabel
```

---

## A2.7 Retrieve lifecycle-stage applicability qualifiers for principle prescription components (TBox query)

This query extracts lifecycle-stage applicability constraints from the OWL class expressions used to model prescription components (`has prescription component some (design process prescription and ... applies during lifecycle stage only ...)`).

To support CQ5 ("for a given prescription component, during which lifecycle stage process type(s) is it intended to apply?"), this version also retrieves the prescribed process type from the same prescription-component expression so stage qualifiers can be interpreted in context.

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX cco: <https://www.commoncoreontologies.org/>

SELECT DISTINCT ?principleClass ?principleLabel ?processType ?processLabel ?stageType ?stageLabel
WHERE {
  ?principleClass rdfs:subClassOf gdpo:GDPO0000003 .
  FILTER(?principleClass != gdpo:GDPO0000003)

  # Traverse the has prescription component restriction
  ?principleClass rdfs:subClassOf ?sc .
  ?sc owl:onProperty gdpo:GDPO0000062 ;
      owl:someValuesFrom ?pcExpr .

  # Extract the prescribed process type from the same prescription-component expression
  ?pcExpr owl:intersectionOf/rdf:rest*/rdf:first ?prescribesPart .
  ?prescribesPart owl:onProperty cco:ont00001942 ;
                  owl:allValuesFrom ?processType .

  # Extract the lifecycle-stage applicability qualifier from the same prescription-component expression
  ?pcExpr owl:intersectionOf/rdf:rest*/rdf:first ?stagePart .
  ?stagePart owl:onProperty gdpo:GDPO0000063 ;
             owl:allValuesFrom ?stageType .

  OPTIONAL { ?principleClass rdfs:label ?principleLabel . }
  OPTIONAL { ?processType rdfs:label ?processLabel . }
  OPTIONAL { ?stageType rdfs:label ?stageLabel . }
}
ORDER BY ?principleLabel ?processLabel ?stageLabel
```

---

## Usage Notes

These templates illustrate the practical consequence of GDPO's modeling commitments: once principles are explicit directive entities, evaluations are explicit information artifacts about artifacts and against principles, and methods are explicit specifications that operationalize principles, datasets can be queried to answer comparative and audit-oriented questions without introducing category errors or ad hoc conventions.

**Namespace assumptions:**
- `gdpo:` = `https://www.ramsprinciplesofgooddesign.com/`
- `ex:` = `http://example.org/gdpo-demo/` (for ABox examples)
- `cco:` = `https://www.commoncoreontologies.org/`
- `bfo:` = `http://purl.obolibrary.org/obo/`

**Running these queries:**
1. Load `gdpo.ttl` (TBox) and `gdpo-example-abox.ttl` (ABox) into a SPARQL endpoint
2. For TBox queries (A2.1, A2.7), only the ontology is required
3. For ABox queries, instance data must be loaded

---

## Version History

| Version | Changes |
|---------|---------|
| v4.0.3 | Initial publication matching manuscript Appendix A2 |
