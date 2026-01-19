# GDPO SPARQL Queries

Version: 4.0.3  
Last Updated: 2026-01-17

This document provides SPARQL queries corresponding to the GDPO competency questions. Each query demonstrates how to retrieve information from GDPO-conformant instance data.

---

## Prefixes

All queries assume the following prefix declarations:

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bfo: <http://purl.obolibrary.org/obo/>
PREFIX cco: <https://www.commoncoreontologies.org/>
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
```

---

## About Principles and Processes

### CQ1: Which design processes does the principle of innovativeness prescribe?

```sparql
SELECT ?process ?processLabel WHERE {
  ?principle rdfs:label "principle of innovativeness"@en .
  ?principle gdpo:GDPO0000062 ?prescription .
  ?prescription cco:ont00001942 ?process .
  ?process rdfs:label ?processLabel .
}
```

### CQ2: Which principle prescribes a design use process?

```sparql
SELECT ?principle ?principleLabel WHERE {
  ?principle gdpo:GDPO0000062 ?prescription .
  ?prescription cco:ont00001942 gdpo:GDPO0000015 .
  ?principle rdfs:label ?principleLabel .
}
```

### CQ3: Which evaluation methods operationalize the principle of minimalism?

```sparql
SELECT ?method ?methodLabel WHERE {
  ?principle rdfs:label "principle of minimalism"@en .
  ?method gdpo:GDPO0000054 ?principle .
  ?method rdfs:label ?methodLabel .
}
```

### CQ5: Which qualities or dispositions are linked to a specific design principle?

```sparql
SELECT ?principle ?principleLabel ?target ?targetLabel WHERE {
  ?principle a gdpo:GDPO0000003 .
  ?principle rdfs:label ?principleLabel .
  ?principle gdpo:GDPO0000454 ?target .
  ?target rdfs:label ?targetLabel .
}
```

---

## About Evaluations

### CQ6: What artifacts have been the subject of a design evaluation?

```sparql
SELECT DISTINCT ?artifact ?artifactLabel WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?artifact rdfs:label ?artifactLabel .
}
```

### CQ7: Which principles was a particular artifact evaluated against?

```sparql
SELECT ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label ?principleLabel .
}
```

### CQ8: Which evaluation method was used in a given design evaluation?

```sparql
SELECT ?method ?methodLabel WHERE {
  ?evaluation rdfs:label "SK4 evaluation 1970"@en .
  ?evaluation gdpo:GDPO0000048 ?method .
  ?method rdfs:label ?methodLabel .
}
```

### CQ9: What numeric score was assigned to an artifact? (Legacy pattern)

```sparql
SELECT ?evaluation ?date ?score WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000050 ?date .
  ?evaluation gdpo:GDPO0000047 ?score .
}
ORDER BY DESC(?date)
LIMIT 1
```

### CQ9b: Reified scores with principle and scale (v4.0.0+)

```sparql
SELECT ?artifact ?principleLabel ?scoreValue ?scaleLabel WHERE {
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

### CQ10: On what date was an artifact last assessed? (Legacy xsd:dateTime)

```sparql
SELECT ?artifact ?date WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000050 ?date .
}
ORDER BY DESC(?date)
LIMIT 1
```

### CQ11: During which temporal region was an evaluation conducted? (v4.0.3)

```sparql
SELECT ?evaluation ?artifact ?temporalRegion ?regionLabel WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000468 ?temporalRegion .
  OPTIONAL { ?temporalRegion rdfs:label ?regionLabel . }
}
```

### CQ12: All evaluations within a specified temporal interval (v4.0.3)

```sparql
SELECT ?evaluation ?artifact ?principleLabel ?temporalRegion WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label ?principleLabel .
  ?evaluation gdpo:GDPO0000468 ?temporalRegion .
  # Add temporal region filter as needed, e.g.:
  # ?temporalRegion rdfs:label "Q4 2025"@en .
}
```

---

## About Methods

### CQ14: Which principles does a method operationalize?

```sparql
SELECT ?method ?methodLabel ?principle ?principleLabel WHERE {
  ?method a gdpo:GDPO0000052 .
  ?method rdfs:label ?methodLabel .
  ?method gdpo:GDPO0000054 ?principle .
  ?principle rdfs:label ?principleLabel .
}
```

### CQ15: Multiple methods evaluating the same principle?

```sparql
SELECT ?principle ?principleLabel (COUNT(?method) AS ?methodCount) WHERE {
  ?method gdpo:GDPO0000054 ?principle .
  ?principle rdfs:label ?principleLabel .
}
GROUP BY ?principle ?principleLabel
HAVING (COUNT(?method) > 1)
```

---

## About Qualities and Dispositions

### CQ17: Which qualities inhere in an artifact?

```sparql
SELECT ?artifact ?quality ?qualityLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?quality bfo:BFO_0000197 ?artifact .
  ?quality rdfs:label ?qualityLabel .
}
```

### CQ18: Which dispositions are realized in which processes?

```sparql
SELECT ?artifact ?disposition ?dispositionLabel ?process ?processLabel WHERE {
  ?disposition bfo:BFO_0000197 ?artifact .
  ?disposition bfo:BFO_0000054 ?process .
  ?disposition rdfs:label ?dispositionLabel .
  ?process rdfs:label ?processLabel .
}
```

---

## About Prescriptions and Temporal Scope

### CQ20: Which principles are part of the Rams ten principles specification?

```sparql
SELECT ?principle ?principleLabel WHERE {
  ?spec a gdpo:GDPO0000034 .
  ?spec gdpo:GDPO0000060 ?principle .
  ?principle rdfs:label ?principleLabel .
}
```

### CQ22: Which agents carried out a design evaluation process?

```sparql
SELECT ?process ?agent ?agentLabel ?artifact WHERE {
  ?process a gdpo:GDPO0000055 .
  ?process gdpo:GDPO0000051 ?agent .
  ?agent rdfs:label ?agentLabel .
  ?process gdpo:GDPO0000465 ?artifact .
}
```

### CQ23: Which prescriptions apply during a specified temporal region? (v4.0.3)

```sparql
SELECT ?prescription ?prescriptionLabel ?temporalRegion WHERE {
  ?prescription a gdpo:GDPO0000061 .
  ?prescription rdfs:label ?prescriptionLabel .
  ?prescription gdpo:GDPO0000467 ?temporalRegion .
}
```

### CQ24: Temporal scope of a design process prescription (v4.0.3)

```sparql
SELECT ?prescription ?prescriptionLabel ?lifecycleStage ?temporalRegion WHERE {
  ?prescription a gdpo:GDPO0000061 .
  ?prescription rdfs:label ?prescriptionLabel .
  OPTIONAL { ?prescription gdpo:GDPO0000063 ?lifecycleStage . }
  OPTIONAL { ?prescription gdpo:GDPO0000467 ?temporalRegion . }
}
```

---

## About Scores and Scales (v4.0.0+)

### CQ25: What score scale was used for a particular evaluation score?

```sparql
SELECT ?scoreComponent ?scoreValue ?scale ?scaleLabel WHERE {
  ?scoreComponent a gdpo:GDPO0000456 .
  ?scoreComponent gdpo:GDPO0000459 ?scoreValue .
  ?scoreComponent gdpo:GDPO0000460 ?scale .
  ?scale rdfs:label ?scaleLabel .
}
```

### CQ26: All per-principle scores for a given evaluation record

```sparql
SELECT ?principleLabel ?scoreValue ?scaleLabel WHERE {
  ?evaluation rdfs:label "Braun SK4 Evaluation Q4 2025"@en .
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

### CQ27: Evaluations using normalized (0–1) scoring scale

```sparql
SELECT ?evaluation ?artifact WHERE {
  ?evaluation gdpo:GDPO0000457 ?scoreComponent .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?scoreComponent gdpo:GDPO0000460 ?scale .
  ?scale rdfs:label "Normalized Ratio Scale (0–1)"@en .
}
```

---

## About Communicative Honesty (v4.0.0+)

### CQ28: Communication content assessed in a communicative honesty evaluation

```sparql
SELECT ?evaluation ?artifact ?content ?contentLabel WHERE {
  ?evaluation a gdpo:GDPO0000452 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000450 ?content .
  ?content rdfs:label ?contentLabel .
}
```

### CQ29: Artifacts with both interaction and communicative honesty evaluations

```sparql
SELECT ?artifact ?interactionEval ?commEval WHERE {
  ?interactionEval a gdpo:GDPO0000455 .
  ?interactionEval gdpo:GDPO0000045 ?artifact .
  ?commEval a gdpo:GDPO0000452 .
  ?commEval gdpo:GDPO0000045 ?artifact .
}
```

---

## Process–Record Linkage

### Find evaluation process that produced a record (truthmaker provenance)

```sparql
SELECT ?record ?process ?agent WHERE {
  ?record a gdpo:GDPO0000044 .
  ?record gdpo:GDPO0000462 ?process .
  ?process gdpo:GDPO0000051 ?agent .
}
```

### Find all records output by a specific evaluation process

```sparql
SELECT ?process ?record ?artifact WHERE {
  ?process a gdpo:GDPO0000055 .
  ?process gdpo:GDPO0000463 ?record .
  ?record gdpo:GDPO0000045 ?artifact .
}
```
