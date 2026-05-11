#!/usr/bin/env python3
"""Lightweight regression checks for GDPO."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from rdflib import Graph, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology" / "gdpo-4.0.3.ttl"
EXAMPLE = ROOT / "examples" / "gdpo-example-abox.ttl"
CATALOG = ROOT / "ontology" / "catalog-v001.xml"

GDPO = Namespace("https://www.ramsprinciplesofgooddesign.com/")
CCO = Namespace("https://www.commoncoreontologies.org/")

EXPECTED_IMPORTS = {
    URIRef("http://purl.obolibrary.org/obo/bfo/2020/bfo.owl"),
    URIRef("https://www.commoncoreontologies.org/2024-11-05/AgentOntology"),
    URIRef("https://www.commoncoreontologies.org/2024-11-06/ArtifactOntology"),
}

PRESCRIPTION_COMPONENTS = {
    GDPO[f"GDPO00000{i}"] for i in range(76, 86)
}

FORBIDDEN_PRESCRIPTION_ABOX_PROPERTIES = {
    CCO["ont00001942"],  # cco:prescribes
    GDPO["GDPO0000063"],  # applies during lifecycle stage
    GDPO["GDPO0000466"],  # applies during temporal region
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def pass_check(message: str) -> None:
    print(f"PASS: {message}")


def parse_graph(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def check_ontology_parse() -> Graph:
    graph = parse_graph(ONTOLOGY)
    pass_check(f"parsed {ONTOLOGY.relative_to(ROOT)}")
    return graph


def check_example_parse() -> None:
    parse_graph(EXAMPLE)
    pass_check(f"parsed {EXAMPLE.relative_to(ROOT)}")


def check_catalog_xml() -> ET.ElementTree:
    tree = ET.parse(CATALOG)
    pass_check(f"parsed {CATALOG.relative_to(ROOT)}")
    return tree


def check_imports(graph: Graph) -> None:
    imports = set(graph.objects(None, OWL.imports))
    missing = EXPECTED_IMPORTS - imports
    unexpected_cco = {
        iri for iri in imports
        if str(iri).startswith(str(CCO)) and iri not in EXPECTED_IMPORTS
    }
    if missing:
        fail("missing expected imports: " + ", ".join(sorted(map(str, missing))))
    if unexpected_cco:
        fail("unexpected CCO imports: " + ", ".join(sorted(map(str, unexpected_cco))))
    pass_check("ontology imports are pinned to BFO 2020 and CCO 2.0")


def check_catalog_pins(tree: ET.ElementTree) -> None:
    root = tree.getroot()
    uris = [value for elem in root.iter() for value in elem.attrib.values()]
    joined = "\n".join(uris)
    if "v2.0-2024-11-06" not in joined:
        fail("catalog does not reference CCO tag v2.0-2024-11-06")
    if "develop" in joined or "v2.1" in joined:
        fail("catalog appears to reference CCO develop or v2.1")
    pass_check("catalog pins CCO to v2.0-2024-11-06")


def check_no_has_value(graph: Graph) -> None:
    triples = list(graph.triples((None, OWL.hasValue, None)))
    if triples:
        fail(f"found {len(triples)} owl:hasValue triple(s)")
    pass_check("no owl:hasValue restrictions")


def check_no_gdpo_class_individual_punning(graph: Graph) -> None:
    classes = {
        subject for subject in graph.subjects(RDF.type, OWL.Class)
        if str(subject).startswith(str(GDPO))
    }
    individuals = {
        subject for subject in graph.subjects(RDF.type, OWL.NamedIndividual)
        if str(subject).startswith(str(GDPO))
    }
    overlap = classes & individuals
    if overlap:
        fail("GDPO class/individual punning found: " + ", ".join(sorted(map(str, overlap))))
    pass_check("no GDPO entity is both owl:Class and owl:NamedIndividual")


def check_named_prescription_components_are_lightweight(graph: Graph) -> None:
    violations = []
    for subject in PRESCRIPTION_COMPONENTS:
        for predicate in FORBIDDEN_PRESCRIPTION_ABOX_PROPERTIES:
            for obj in graph.objects(subject, predicate):
                violations.append((subject, predicate, obj))
    if violations:
        rendered = "; ".join(f"{s} {p} {o}" for s, p, o in violations)
        fail("named prescription component ABox assertions found: " + rendered)
    pass_check("named prescription component individuals remain lightweight")


def main() -> None:
    ontology_graph = check_ontology_parse()
    check_example_parse()
    catalog_tree = check_catalog_xml()
    check_imports(ontology_graph)
    check_catalog_pins(catalog_tree)
    check_no_has_value(ontology_graph)
    check_no_gdpo_class_individual_punning(ontology_graph)
    check_named_prescription_components_are_lightweight(ontology_graph)
    print("All GDPO validation checks passed.")


if __name__ == "__main__":
    main()
