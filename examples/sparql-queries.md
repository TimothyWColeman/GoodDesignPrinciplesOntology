# GDPO SPARQL Query Examples

Example SPARQL queries for querying the Good Design Principles Ontology.

## Prefixes

All queries assume the following prefix declarations:

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX cco: <https://www.commoncoreontologies.org/>
PREFIX bfo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
```

---

## CQ1: Which design processes does the principle of innovativeness prescribe?

```sparql
SELECT ?process ?processLabel WHERE {
  ?principle rdfs:label "principle of innovativeness"@en .
  ?principle gdpo:GDPO0000062 ?prescription .
  ?prescription cco:ont00001942 ?process .
  ?process rdfs:label ?processLabel .
}
```

---

## CQ7: Which principles was a particular artifact evaluated against?

```sparql
# For a given artifact (e.g., "Braun SK4"), list the principles it was evaluated against

SELECT ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label ?principleLabel .
}
```

---

## CQ8: Which evaluation method specification was used in a given design evaluation?

```sparql
# What method was used in a given design evaluation?

SELECT ?method ?methodLabel WHERE {
  ?evaluation rdfs:label "SK4 evaluation 1970"@en .
  ?evaluation gdpo:GDPO0000048 ?method .
  ?method rdfs:label ?methodLabel .
}
```

---

## CQ9: What numeric score was assigned to an artifact in its last design evaluation?

```sparql
# Retrieve the most recent score(s) given to an artifact

SELECT ?evaluation ?date ?score WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000050 ?date .
  ?evaluation gdpo:GDPO0000047 ?score .
}
ORDER BY DESC(?date)
LIMIT 1
```

---

## CQ18: Which principles are part of the Rams ten principles specification?

```sparql
SELECT ?principle ?principleLabel ?canonicalText WHERE {
  gdpo:GDPO0000065 gdpo:GDPO0000060 ?principle .
  ?principle rdfs:label ?principleLabel .
  OPTIONAL { ?principle gdpo:GDPO0000453 ?canonicalText }
}
ORDER BY ?principleLabel
```

---

## Find all principle classes and their target qualities/dispositions

```sparql
SELECT ?principle ?principleLabel ?target ?targetLabel ?targetType WHERE {
  ?principle rdfs:subClassOf gdpo:GDPO0000003 .
  ?principle rdfs:label ?principleLabel .
  ?principle owl:equivalentClass ?equiv .
  ?equiv owl:intersectionOf ?list .
  ?list rdf:rest*/rdf:first ?restriction .
  ?restriction owl:onProperty cco:ont00001808 .
  ?restriction owl:someValuesFrom ?target .
  ?target rdfs:label ?targetLabel .
  ?target rdfs:subClassOf ?superclass .
  BIND(
    IF(?superclass = bfo:BFO_0000019, "Quality",
    IF(?superclass = bfo:BFO_0000016, "Disposition",
    IF(?superclass = bfo:BFO_0000034, "Function", "Other")))
    AS ?targetType
  )
}
```

---

## List all design lifecycle stage processes

```sparql
SELECT ?process ?processLabel ?definition WHERE {
  ?process rdfs:subClassOf gdpo:GDPO0000019 .
  ?process rdfs:label ?processLabel .
  OPTIONAL { ?process <http://www.w3.org/2004/02/skos/core#definition> ?definition }
}
ORDER BY ?processLabel
```

---

## Find evaluations and their methods for a specific principle

```sparql
SELECT ?evaluation ?artifact ?method ?score ?date WHERE {
  ?evaluation a gdpo:GDPO0000044 .
  ?evaluation gdpo:GDPO0000046 ?principle .
  ?principle rdfs:label "principle of honesty"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  OPTIONAL { ?evaluation gdpo:GDPO0000048 ?method }
  OPTIONAL { ?evaluation gdpo:GDPO0000047 ?score }
  OPTIONAL { ?evaluation gdpo:GDPO0000050 ?date }
}
```

---

## Find communicative honesty evaluations with their communication content

```sparql
SELECT ?evaluation ?artifact ?contentType ?content WHERE {
  ?evaluation a gdpo:GDPO0000452 .
  ?evaluation gdpo:GDPO0000045 ?artifact .
  ?evaluation gdpo:GDPO0000450 ?content .
  ?content a ?contentType .
  FILTER(?contentType IN (
    gdpo:GDPO0000447,  # product manual content
    gdpo:GDPO0000448,  # product label content
    gdpo:GDPO0000449   # product advertisement content
  ))
}
```

---

## Notes

### Property IRIs Reference

| Property | IRI | Description |
|----------|-----|-------------|
| has prescription component | `gdpo:GDPO0000062` | Links principle to prescription |
| prescribes | `cco:ont00001942` | CCO prescribes relation |
| is about | `cco:ont00001808` | CCO aboutness relation |
| is about evaluated artifact | `gdpo:GDPO0000045` | Links evaluation to artifact |
| against principle | `gdpo:GDPO0000046` | Links evaluation to principle |
| has score | `gdpo:GDPO0000047` | Numeric evaluation score |
| is about using method | `gdpo:GDPO0000048` | Links evaluation to method |
| assessed on | `gdpo:GDPO0000050` | Evaluation date |
| has principle component | `gdpo:GDPO0000060` | Links specification to principles |
| has canonical statement text | `gdpo:GDPO0000453` | Rams' original wording |
