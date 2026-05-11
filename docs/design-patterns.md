# GDPO Design Patterns

GDPO 4.0.3 represents Rams' ten principles as directive information content
entities while keeping them distinct from the artifact-side qualities,
functions, dispositions, material bases, processes, and communication content
they concern.

## Target-Expression Pattern

Principle categories use `aims at artifact-side target` only with OWL class
expressions.

```text
principle of honesty
  SubClassOf:
    aims at artifact-side target only
      (design material honesty or design functional honesty)
```

This says what kind of target the principle concerns. It does not assert that a
particular artifact already has that quality, function, disposition, material
basis, process, or communication content.

The pattern intentionally avoids:

- punned class-as-individual target proxies
- `owl:hasValue` target restrictions
- dummy target individuals standing in for unrealized design possibilities

## Prescription-Component Pattern

Principles carry process-level prescriptive force through `design process
prescription` components.

```text
principle of usefulness
  SubClassOf:
    has prescription component some
      (
        design process prescription
        and cco:prescribes only design use process
        and applies during lifecycle stage only design use and maintenance process
      )
```

This separates the artifact-side target from what the principle prescribes
designers or evaluators to attend to. Lifecycle applicability is modeled with
stage process types such as sourcing, manufacturing, distribution, use and
maintenance, and end-of-life handling.

For multi-stage applicability, GDPO uses a union filler inside the `only`
restriction. This avoids the logical problem where repeated `only` restrictions
combine as an intersection rather than as a list of alternatives.

## Evaluation-Record Pattern

Evaluation results are represented as information content entities.

```text
design evaluation record
  EquivalentTo:
    information content entity
    and is about evaluated artifact some material entity
    and against principle some design principle
    and assessed during temporal region some BFO temporal region
```

The evaluation record is about an artifact, against a principle, and temporally
indexed. It may also be linked to the method used, the evaluation process that
produced it, score components, communication content, and optional material
bearer provenance.

Scores should normally be represented as reified `design evaluation score`
components rather than as bare numeric literals on the record. This lets each
score carry its principle criterion and score scale.

## Criterion-Method Relevance Pattern

GDPO distinguishes explicit criterion selection from method-derived relevance.

```text
is about using method o operationalizes principle
  SubPropertyOf:
    has evaluation-relevant principle
```

An evaluation can be explicitly `against principle` one principle while using a
method that operationalizes additional principles. This supports traceable
evaluation without flattening all relevance into a single manually asserted
criterion list.

## Modality-Specific Evaluation Pattern

Some evaluations are specialized by the kind of evidence they concern.

```text
design communicative honesty evaluation
  EquivalentTo:
    design honesty evaluation
    and is about communication content some design communication content entity
```

This handles manuals, labels, advertisements, product descriptions, interface
messages, and other communicated claims. Communicative honesty is not modeled as
a product-borne disposition; it is assessed through evaluation records about
communication content.

## Lightweight Material-Bearer Provenance

`has material bearer` may be used to record the material artifact that bears an
information content entity, such as a paper report, PDF, label, or product
manual.

This relation is intentionally optional. It is not a replacement for the full
BFO concretization pattern and should not be used to collapse an information
content entity into the physical object that bears it.
