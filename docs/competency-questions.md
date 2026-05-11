# Competency Questions

These competency questions summarize the intended query surface of GDPO 4.0.3.
They are grouped by modeling concern and mapped to the main classes and
properties used to answer them.

## Principles and Prescriptions

| Question | Main ontology elements |
|----------|------------------------|
| Which target class expressions are associated with each principle? | `design principle`, `aims at artifact-side target` |
| Which process types are prescribed by each principle? | `has prescription component`, `cco:prescribes`, `design process prescription` |
| Which prescriptions apply during a given lifecycle stage? | `applies during lifecycle stage`, `design lifecycle stage process` |
| Which principles are included in the Rams ten principles specification? | `rams ten principles specification`, `has principle component` |
| How does GDPO distinguish principles from artifact-side qualities, functions, and dispositions? | `design principle`, target class expressions, artifact-side target classes |

## Evaluations

| Question | Main ontology elements |
|----------|------------------------|
| What artifacts have been evaluated? | `design evaluation record`, `is about evaluated artifact` |
| Which principle criterion was an artifact evaluated against? | `against principle` |
| During which temporal region was the evaluation assessed? | `assessed during temporal region` |
| Which method specification was used? | `is about using method`, `evaluation method specification` |
| What score values and scales are associated with the evaluation? | `has score component`, `score value`, `has score scale` |

## Methods and Relevance

| Question | Main ontology elements |
|----------|------------------------|
| Which methods operationalize which principles? | `evaluation method specification`, `operationalizes principle` |
| Which principles are relevant because of method use? | `has evaluation-relevant principle`, property chain over method use |
| Which principles were explicitly selected as criteria? | `against principle` |

## Honesty and Communication

| Question | Main ontology elements |
|----------|------------------------|
| Which records are honesty evaluations? | `design honesty evaluation`, `against principle` |
| Which records are communicative honesty evaluations? | `design communicative honesty evaluation`, `is about communication content` |
| Which communication content entities were assessed? | `design communication content entity`, `product manual content`, `product label content`, `product advertisement content` |
| How are material and functional honesty distinguished? | `design material honesty`, `design functional honesty`, honesty basis classes |

## Provenance

| Question | Main ontology elements |
|----------|------------------------|
| Which evaluation process produced a record? | `is evaluation record output of`, `has evaluation record output` |
| Which agent carried out an evaluation process? | `evaluation carried out by` |
| Which information content entities have material-bearer provenance? | `has material bearer` |

## Coverage Notes

GDPO is designed to answer these questions through ontology structure and ABox
assertions. Some answers require reasoning over OWL restrictions or property
chains; others can be answered directly from asserted instance data.
