#!/usr/bin/env python3
"""Reproduce the query and OWL-RL checks reported in the GDPO paper."""

from __future__ import annotations

import sys
from pathlib import Path

import owlrl
import rdflib
from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph, Namespace, OWL, RDF


SUPPLEMENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SUPPLEMENT_DIR.parents[1]
ONTOLOGY = REPO_ROOT / "ontology" / "gdpo-4.0.3.ttl"
FIXTURE = SUPPLEMENT_DIR / "fixture.ttl"
QUERY_DIR = SUPPLEMENT_DIR / "queries"
EXPECTED_OUTPUT = SUPPLEMENT_DIR / "expected-output.txt"
ACTUAL_OUTPUT = SUPPLEMENT_DIR / "validation-output.txt"

GDPO = Namespace("https://www.ramsprinciplesofgooddesign.com/")
EXAMPLE = Namespace("http://example.org/gdpo-demo/")

QUERY_FILES = {
    "A2.1 target expressions": "a2-1-target-expressions.rq",
    "A2.2 artifact evaluations": "a2-2-artifact-evaluations.rq",
    "A2.3 artifact comparison (additional)": "a2-3-artifact-comparison.rq",
    "A2.4 communicative honesty": "a2-4-communicative-honesty.rq",
    "A2.5 disposition realization": "a2-5-disposition-realization.rq",
    "A2.6 method operationalizations": "a2-6-method-operationalizations.rq",
    "A2.7 lifecycle applicability": "a2-7-lifecycle-applicability.rq",
}

EXPECTED_QUERY_ROWS = {
    "A2.1 target expressions": 10,
    "A2.2 artifact evaluations": 3,
    "A2.3 artifact comparison (additional)": 2,
    "A2.4 communicative honesty": 1,
    "A2.5 disposition realization": 1,
    "A2.6 method operationalizations": 3,
    "A2.7 lifecycle applicability": 7,
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_turtle(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def combined_graph(ontology_graph: Graph, fixture_graph: Graph) -> Graph:
    graph = Graph()
    for triple in ontology_graph:
        graph.add(triple)
    for triple in fixture_graph:
        graph.add(triple)
    return graph


def query_row_counts(graph: Graph) -> dict[str, int]:
    counts = {}
    for label, filename in QUERY_FILES.items():
        query_text = (QUERY_DIR / filename).read_text(encoding="utf-8")
        counts[label] = len(list(graph.query(query_text)))
    return counts


def gdpo_punning_overlap(graph: Graph) -> set:
    classes = {
        subject
        for subject in graph.subjects(RDF.type, OWL.Class)
        if str(subject).startswith(str(GDPO))
    }
    individuals = {
        subject
        for subject in graph.subjects(RDF.type, OWL.NamedIndividual)
        if str(subject).startswith(str(GDPO))
    }
    return classes & individuals


def render_report(
    has_value_count: int,
    punning_count: int,
    query_counts: dict[str, int],
    durability_relevance: set,
    honesty_types: set,
) -> str:
    lines = [
        "GDPO manuscript supplement validation",
        f"RDFLib: {rdflib.__version__}",
        f"OWL-RL: {owlrl.__version__}",
        "Ontology: ontology/gdpo-4.0.3.ttl",
        "Fixture: supplement/manuscript-validation/fixture.ttl",
        f"owl:hasValue triples in ontology: {has_value_count}",
        f"GDPO class/named-individual overlap: {punning_count}",
        "Query rows:",
    ]
    for label in QUERY_FILES:
        lines.append(f"  {label}: {query_counts[label]}")
    lines.extend(
        [
            "Durability evaluation relevance:",
            *[f"  {value}" for value in sorted(map(str, durability_relevance))],
            "Manual-honesty evaluation types:",
            *[f"  {value}" for value in sorted(map(str, honesty_types))],
            "PASS: all expected query and entailment checks succeeded",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    ontology_graph = parse_turtle(ONTOLOGY)
    fixture_graph = parse_turtle(FIXTURE)
    graph = combined_graph(ontology_graph, fixture_graph)

    has_value_count = len(list(ontology_graph.triples((None, OWL.hasValue, None))))
    if has_value_count:
        fail(f"found {has_value_count} owl:hasValue triple(s)")

    punning_overlap = gdpo_punning_overlap(ontology_graph)
    if punning_overlap:
        fail("GDPO class/named-individual overlap: " + ", ".join(map(str, punning_overlap)))

    wrong_example_type = (
        EXAMPLE["Eval_SK4_ManualHonesty_2024"],
        RDF.type,
        GDPO["GDPO0000449"],
    )
    if wrong_example_type in fixture_graph:
        fail("manual-honesty evaluation is typed as product advertisement content")

    query_counts = query_row_counts(graph)
    for label, expected in EXPECTED_QUERY_ROWS.items():
        actual = query_counts[label]
        if actual != expected:
            fail(f"{label} returned {actual} row(s), expected {expected}")

    DeductiveClosure(OWLRL_Semantics).expand(graph)

    durability_evaluation = EXAMPLE["Eval_SK4_Durability_2024"]
    durability_relevance = set(
        graph.objects(durability_evaluation, GDPO["GDPO0000059"])
    )
    expected_relevance = {GDPO["GDPO0000072"], GDPO["GDPO0000074"]}
    if durability_relevance != expected_relevance:
        fail(
            "durability relevance mismatch: "
            + ", ".join(sorted(map(str, durability_relevance)))
        )

    honesty_evaluation = EXAMPLE["Eval_SK4_ManualHonesty_2024"]
    required_honesty_types = {
        GDPO["GDPO0000044"],
        GDPO["GDPO0000452"],
        GDPO["GDPO0000455"],
    }
    honesty_types = set(graph.objects(honesty_evaluation, RDF.type))
    if not required_honesty_types.issubset(honesty_types):
        missing = required_honesty_types - honesty_types
        fail("manual-honesty inference missing type(s): " + ", ".join(map(str, missing)))

    report = render_report(
        has_value_count,
        len(punning_overlap),
        query_counts,
        expected_relevance,
        required_honesty_types,
    )
    ACTUAL_OUTPUT.write_text(report, encoding="utf-8")
    print(report, end="")

    if EXPECTED_OUTPUT.exists():
        expected_report = EXPECTED_OUTPUT.read_text(encoding="utf-8")
        if report != expected_report:
            fail("validation output differs from expected-output.txt")


if __name__ == "__main__":
    main()
