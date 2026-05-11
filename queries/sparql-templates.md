# SPARQL Templates

These templates are intended for local graph stores that load
`ontology/gdpo-4.0.3.ttl` and any relevant ABox data.

## Principle Target Expressions

```sparql
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

## Prescribed Process Types

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

## Evaluation Criteria for an Artifact

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Example radio"@en .
  ?evaluation gdpo:GDPO0000045 ?artifact ;
              gdpo:GDPO0000046 ?principle .
  OPTIONAL { ?principle rdfs:label ?principleLabel . }
}
```

## Method-Derived Relevant Principles

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?evaluation ?method ?principle ?principleLabel WHERE {
  ?evaluation gdpo:GDPO0000048 ?method .
  ?method gdpo:GDPO0000054 ?principle .
  OPTIONAL { ?principle rdfs:label ?principleLabel . }
}
ORDER BY ?evaluation ?principleLabel
```

## Score Components

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT ?evaluation ?scoreComponent ?principle ?scoreValue ?scale WHERE {
  ?evaluation gdpo:GDPO0000457 ?scoreComponent .
  OPTIONAL { ?scoreComponent gdpo:GDPO0000458 ?principle . }
  OPTIONAL { ?scoreComponent gdpo:GDPO0000459 ?scoreValue . }
  OPTIONAL { ?scoreComponent gdpo:GDPO0000460 ?scale . }
}
```

## Communicative Honesty Evaluations

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT ?evaluation ?artifact ?content ?principle WHERE {
  ?evaluation a gdpo:GDPO0000044 ;
              gdpo:GDPO0000045 ?artifact ;
              gdpo:GDPO0000450 ?content ;
              gdpo:GDPO0000046 ?principle .
  ?principle a gdpo:GDPO0000025 .
}
```

## Material-Bearer Provenance

```sparql
PREFIX gdpo: <https://www.ramsprinciplesofgooddesign.com/>

SELECT ?informationContent ?bearer WHERE {
  ?informationContent gdpo:GDPO0000464 ?bearer .
}
```
