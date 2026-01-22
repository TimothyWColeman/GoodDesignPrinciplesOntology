#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GDPO extended validation artifact runner.

This script extends the earlier GDPO validation template by checking additional
"reasoning-sensitive" points beyond the two property chains, including:

- OWL2 punning constraints for aims-at target proxies
- Guard rails for OWL 2 DL regularity (structural check for role-hierarchy hazards)
- Closed-world completeness checks (SHACL-like) for evaluation records & score components
- RDF hygiene checks (catch accidental pointers to principle *classes* when tokens are intended)
- Small rule-based materialization of:
    * GDPO property chains
    * inverse properties (where asserted)
    * hasValue "aims-at" links for canonical statement tokens
    * communicative honesty evaluation classification
- Contrast demonstrations:
    * adding an OWL range to aims-at triggers level-mixing under punning
    * using someValuesFrom can create a "phantom target instance"

No external reasoner is required; everything is done via explicit graph inspection
and small rule closures.

Outputs (written alongside this script):
  - extended_validation_output.txt
  - gdpo_extended_validation_inferred.ttl
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection


# Namespaces
GDPO = Namespace("https://www.ramsprinciplesofgooddesign.com/")
BFO = Namespace("http://purl.obolibrary.org/obo/")
CCO = Namespace("https://www.commoncoreontologies.org/")
EX = Namespace("http://example.org/gdpo-extended-validation/")


# Key GDPO IRIs
AIMS_AT = GDPO["GDPO0000454"]  # aims at artifact-side target
DESIGN_PRINCIPLE = GDPO["GDPO0000003"]
PRINCIPLE_SPEC = GDPO["GDPO0000035"]

EVAL_RECORD = GDPO["GDPO0000044"]
EVAL_SCORE = GDPO["GDPO0000456"]
EVAL_SCORE_SCALE = GDPO["GDPO0000461"]

ABOUT_ARTIFACT = GDPO["GDPO0000045"]     # is about evaluated artifact
AGAINST_PRINCIPLE = GDPO["GDPO0000046"]  # against principle
ABOUT_METHOD = GDPO["GDPO0000048"]       # is about using method
OPERATIONALIZES = GDPO["GDPO0000054"]    # operationalizes principle
EVAL_RELEVANT = GDPO["GDPO0000059"]      # has evaluation-relevant principle
ASSESS_DURING = GDPO["GDPO0000468"]      # assessed during temporal region

HAS_SCORE_COMPONENT = GDPO["GDPO0000457"]
SCORE_FOR_PRINCIPLE = GDPO["GDPO0000458"]
SCORE_VALUE = GDPO["GDPO0000459"]
HAS_SCORE_SCALE = GDPO["GDPO0000460"]

ABOUT_COMM_CONTENT = GDPO["GDPO0000450"]
COMM_HONESTY_EVAL = GDPO["GDPO0000452"]
PRINCIPLE_OF_HONESTY = GDPO["GDPO0000025"]

HAS_PRESCRIPTION_COMPONENT = GDPO["GDPO0000062"]
PRESCRIBES_VIA_COMPONENT = GDPO["GDPO0000064"]
CCO_PRESCRIBES = CCO["ont00001942"]


# Rams principle category classes
RAMS_PRINCIPLE_CATEGORIES: List[URIRef] = [
    GDPO["GDPO0000020"], GDPO["GDPO0000021"], GDPO["GDPO0000022"], GDPO["GDPO0000023"], GDPO["GDPO0000024"],
    GDPO["GDPO0000025"], GDPO["GDPO0000026"], GDPO["GDPO0000027"], GDPO["GDPO0000028"], GDPO["GDPO0000029"],
]

# Allowed "target category" superclasses (for the target-as-universal constraint)
# Note: GDPO uses relational quality for at least one target (innovativeness).
ALLOWED_TARGET_SUPERS: Set[URIRef] = {
    BFO["BFO_0000019"],  # quality
    BFO["BFO_0000034"],  # function
    BFO["BFO_0000016"],  # disposition
    BFO["BFO_0000145"],  # relational quality
}


def rdf_list(g: Graph, node: URIRef | BNode) -> List[URIRef | BNode]:
    return list(Collection(g, node))


def local_name(uri: URIRef) -> str:
    s = str(uri)
    if "#" in s:
        return s.rsplit("#", 1)[-1]
    return s.rsplit("/", 1)[-1]


def is_named_individual(g: Graph, x: URIRef) -> bool:
    return (x, RDF.type, OWL.NamedIndividual) in g


def is_subclass_of(g: Graph, cls: URIRef, sup: URIRef) -> bool:
    """RDFS subclassOf* traversal (no OWL reasoning)."""
    if cls == sup:
        return True
    visited: Set[URIRef] = set()
    stack: List[URIRef] = [cls]
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for parent in g.objects(cur, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                if parent == sup:
                    return True
                stack.append(parent)
    return False


def token_is_design_principle(g: Graph, token: URIRef) -> bool:
    """
    Heuristic "principle token" check:
      token is owl:NamedIndividual and has rdf:type some class that is a subclass of gdpo:design principle.
    """
    if not is_named_individual(g, token):
        return False
    for t in g.objects(token, RDF.type):
        if isinstance(t, URIRef) and is_subclass_of(g, t, DESIGN_PRINCIPLE):
            return True
    return False


@dataclass(frozen=True)
class HasValueAxiom:
    cls: URIRef
    prop: URIRef
    value: URIRef


def extract_hasvalue_axioms(g: Graph, prop: URIRef) -> List[HasValueAxiom]:
    """
    Extract axioms of the form:
        C owl:equivalentClass [ owl:intersectionOf ( ... [ owl:onProperty prop ; owl:hasValue v ] ... ) ].
    """
    axioms: List[HasValueAxiom] = []
    for C in set(g.subjects(OWL.equivalentClass, None)):
        if not isinstance(C, URIRef):
            continue
        for eq in g.objects(C, OWL.equivalentClass):
            inter_nodes = list(g.objects(eq, OWL.intersectionOf))
            if not inter_nodes:
                continue
            for item in rdf_list(g, inter_nodes[0]):
                if (item, OWL.onProperty, prop) in g and (item, OWL.hasValue, None) in g:
                    v = next(g.objects(item, OWL.hasValue))
                    if isinstance(v, URIRef):
                        axioms.append(HasValueAxiom(C, prop, v))
    return axioms


def materialize_hasvalue_inferences(g: Graph, axioms: List[HasValueAxiom]) -> int:
    """If x rdf:type C and C has (p hasValue v), materialize x p v."""
    added = 0
    for ax in axioms:
        for x in g.subjects(RDF.type, ax.cls):
            if (x, ax.prop, ax.value) not in g:
                g.add((x, ax.prop, ax.value))
                added += 1
    return added


def materialize_property_chain(g: Graph, p1: URIRef, p2: URIRef, p_out: URIRef) -> int:
    """Materialize: (p1 o p2) subPropertyOf p_out."""
    added = 0
    for s, _, m in g.triples((None, p1, None)):
        for _, _, o in g.triples((m, p2, None)):
            if (s, p_out, o) not in g:
                g.add((s, p_out, o))
                added += 1
    return added


def materialize_inverse_properties(g: Graph, inverse_pairs: Sequence[Tuple[URIRef, URIRef]]) -> int:
    """Materialize explicit inverse triples for declared inverse property pairs."""
    added = 0
    for p, inv in inverse_pairs:
        for s, _, o in g.triples((None, p, None)):
            if (o, inv, s) not in g:
                g.add((o, inv, s))
                added += 1
        for s, _, o in g.triples((None, inv, None)):
            if (o, p, s) not in g:
                g.add((o, p, s))
                added += 1
    return added


def materialize_range_inference(g: Graph, prop: URIRef) -> int:
    """Apply RDFS range: if prop rdfs:range R and s prop o then o rdf:type R."""
    added = 0
    ranges = list(g.objects(prop, RDFS.range))
    if not ranges:
        return 0
    for _, _, o in g.triples((None, prop, None)):
        for R in ranges:
            if (o, RDF.type, R) not in g:
                g.add((o, RDF.type, R))
                added += 1
    return added


def materialize_existentials_somevaluesfrom(g: Graph, prop: URIRef) -> Tuple[int, int]:
    """
    Minimal existential materialization for demonstration only.

    For each class C with a SubClassOf restriction:
        C subClassOf [ onProperty prop ; someValuesFrom D ]
    and each x rdf:type C, ensure some y with x prop y and y rdf:type D.
    Creates a fresh blank node if missing.

    Returns (triples_added, blank_nodes_created).
    """
    added = 0
    bnodes = 0

    restrictions: List[Tuple[URIRef, URIRef]] = []
    for C in set(g.subjects(RDFS.subClassOf, None)):
        if not isinstance(C, URIRef):
            continue
        for r in g.objects(C, RDFS.subClassOf):
            if (r, RDF.type, OWL.Restriction) in g and (r, OWL.onProperty, prop) in g:
                for D in g.objects(r, OWL.someValuesFrom):
                    if isinstance(D, URIRef):
                        restrictions.append((C, D))

    for C, D in restrictions:
        for x in g.subjects(RDF.type, C):
            ok = False
            for o in g.objects(x, prop):
                if (o, RDF.type, D) in g:
                    ok = True
                    break
            if ok:
                continue
            y = BNode()
            bnodes += 1
            g.add((x, prop, y)); added += 1
            g.add((y, RDF.type, D)); added += 1

    return added, bnodes


def check_property_chain_exact(g: Graph, prop: URIRef, chain: List[URIRef]) -> bool:
    """Check prop owl:propertyChainAxiom is exactly the given RDF list."""
    for lst in g.objects(prop, OWL.propertyChainAxiom):
        if isinstance(lst, (URIRef, BNode)):
            items = rdf_list(g, lst)
            # Keep only URIRefs and require exact match length/order
            if len(items) == len(chain) and all(isinstance(i, URIRef) for i in items) and list(items) == chain:
                return True
    return False


def check_disjointness_violations(g: Graph) -> List[Tuple[URIRef, URIRef, URIRef]]:
    """Return (individual, disjointClassA, disjointClassB) for disjointness violations."""
    disjoint_pairs: Set[Tuple[URIRef, URIRef]] = set()
    for a, _, b in g.triples((None, OWL.disjointWith, None)):
        if isinstance(a, URIRef) and isinstance(b, URIRef):
            disjoint_pairs.add((a, b))
            disjoint_pairs.add((b, a))

    violations: List[Tuple[URIRef, URIRef, URIRef]] = []
    for x in set(g.subjects(RDF.type, None)):
        if not isinstance(x, URIRef):
            continue
        types = {t for t in g.objects(x, RDF.type) if isinstance(t, URIRef)}
        for t in types:
            for u in types:
                if t != u and (t, u) in disjoint_pairs:
                    violations.append((x, t, u))

    # de-dup symmetric pairs
    uniq: Set[Tuple[str, str, str]] = set()
    out: List[Tuple[URIRef, URIRef, URIRef]] = []
    for x, t, u in violations:
        key = (str(x), min(str(t), str(u)), max(str(t), str(u)))
        if key in uniq:
            continue
        uniq.add(key)
        out.append((x, t, u))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ontology", default="GoodDesignPrinciplesOntology20260116v4.0.3.ttl")
    ap.add_argument("--toy", default="gdpo_extended_validation.ttl")
    ap.add_argument("--negative", action="store_true", help="Also load gdpo_extended_validation_negative.ttl")
    ap.add_argument("--out-report", default="extended_validation_output.txt")
    ap.add_argument("--out-inferred", default="gdpo_extended_validation_inferred.ttl")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    ont_path = (here / args.ontology).resolve()
    toy_path = (here / args.toy).resolve()
    neg_path = (here / "gdpo_extended_validation_negative.ttl").resolve()

    ont = Graph()
    ont.parse(str(ont_path), format="turtle")

    g = Graph()
    for prefix, ns in [("gdpo", GDPO), ("bfo", BFO), ("cco", CCO), ("ex", EX), ("owl", OWL), ("rdfs", RDFS), ("rdf", RDF)]:
        g.bind(prefix, ns)
    g += ont

    toy = Graph()
    toy.parse(str(toy_path), format="turtle")
    g += toy

    if args.negative:
        neg = Graph()
        neg.parse(str(neg_path), format="turtle")
        g += neg

    report_lines: List[str] = []
    def line(s: str = "") -> None:
        report_lines.append(s)

    line("GDPO EXTENDED VALIDATION REPORT")
    line("=" * 34)
    line(f"Ontology: {ont_path.name}")
    line(f"Toy ABox:  {toy_path.name}" + (" (+ negative tests)" if args.negative else ""))
    line("")

    # 1) Ontology structural checks
    line("1) Ontology structural checks")
    line("-" * 32)

    has_range = any(True for _ in ont.objects(AIMS_AT, RDFS.range))
    if not has_range:
        line(f"PASS: {local_name(AIMS_AT)} has no rdfs:range axiom (avoids level-mixing under punning).")
    else:
        ranges = ", ".join(local_name(r) for r in ont.objects(AIMS_AT, RDFS.range) if isinstance(r, URIRef))
        line(f"FAIL: {local_name(AIMS_AT)} has rdfs:range axiom(s): {ranges}")

    ok_chain_eval = check_property_chain_exact(ont, EVAL_RELEVANT, [ABOUT_METHOD, OPERATIONALIZES])
    ok_chain_presc = check_property_chain_exact(ont, PRESCRIBES_VIA_COMPONENT, [HAS_PRESCRIPTION_COMPONENT, CCO_PRESCRIBES])

    line(("PASS" if ok_chain_eval else "FAIL") + f": property chain for {local_name(EVAL_RELEVANT)} is (aboutMethod o operationalizes).")
    line(("PASS" if ok_chain_presc else "FAIL") + f": property chain for {local_name(PRESCRIBES_VIA_COMPONENT)} is (hasPrescriptionComponent o cco:prescribes).")

    if (PRESCRIBES_VIA_COMPONENT, RDFS.subPropertyOf, CCO_PRESCRIBES) in ont:
        line(f"FAIL: {local_name(PRESCRIBES_VIA_COMPONENT)} asserted subPropertyOf cco:prescribes (regularity hazard with the chain).")
    else:
        line(f"PASS: {local_name(PRESCRIBES_VIA_COMPONENT)} is NOT asserted subPropertyOf cco:prescribes (regularity guard holds).")

    axioms = extract_hasvalue_axioms(ont, AIMS_AT)
    by_cls: Dict[URIRef, List[URIRef]] = {}
    for ax in axioms:
        by_cls.setdefault(ax.cls, []).append(ax.value)

    missing_defs = [c for c in RAMS_PRINCIPLE_CATEGORIES if c not in by_cls]
    if missing_defs:
        line("FAIL: Missing aims-at hasValue definition(s) for: " + ", ".join(local_name(c) for c in missing_defs))
    else:
        line("PASS: All 10 Rams principle categories have an aims-at hasValue definition.")

    bad_punning: List[URIRef] = []
    bad_sup: List[URIRef] = []
    for c in RAMS_PRINCIPLE_CATEGORIES:
        for t in by_cls.get(c, []):
            if (t, RDF.type, OWL.Class) not in ont or (t, RDF.type, OWL.NamedIndividual) not in ont:
                bad_punning.append(t)
            ok = any(is_subclass_of(ont, t, sup) for sup in ALLOWED_TARGET_SUPERS)
            if not ok:
                bad_sup.append(t)

    if not bad_punning:
        line("PASS: All aims-at targets used in Rams definitions are OWL2-punned (owl:Class + owl:NamedIndividual).")
    else:
        line("FAIL: Non-punned aims-at targets: " + ", ".join(local_name(t) for t in sorted(set(bad_punning), key=str)))

    if not bad_sup:
        line("PASS: All aims-at targets (as classes) are under quality/function/disposition (allowing relational quality).")
    else:
        line("FAIL: Targets not under allowed BFO superclasses: " + ", ".join(local_name(t) for t in sorted(set(bad_sup), key=str)))

    inv_pairs: List[Tuple[URIRef, URIRef]] = []
    for p, _, q in ont.triples((None, OWL.inverseOf, None)):
        if isinstance(p, URIRef) and isinstance(q, URIRef):
            inv_pairs.append((p, q))
    inv_pairs = list({(p, q) for p, q in inv_pairs})
    line(f"INFO: Ontology declares {len(inv_pairs)} owl:inverseOf pair(s).")
    line("")

    # 2) Closed-world completeness
    line("2) Closed-world data completeness checks (SHACL-like)")
    line("-" * 55)

    eval_missing: Dict[str, List[URIRef]] = {"artifact": [], "principle": [], "time": []}
    for e in g.subjects(RDF.type, EVAL_RECORD):
        if not isinstance(e, URIRef):
            continue
        if not any(True for _ in g.objects(e, ABOUT_ARTIFACT)):
            eval_missing["artifact"].append(e)
        if not any(True for _ in g.objects(e, AGAINST_PRINCIPLE)):
            eval_missing["principle"].append(e)
        if not any(True for _ in g.objects(e, ASSESS_DURING)):
            eval_missing["time"].append(e)

    if not any(eval_missing.values()):
        line("PASS: All evaluation records have evaluated artifact, criterion principle, and assessment time.")
    else:
        line("FAIL: Some evaluation records are incomplete:")
        for k, vals in eval_missing.items():
            if vals:
                line(f"  - missing {k}: " + ", ".join(local_name(v) for v in vals))

    score_missing: Dict[str, List[URIRef]] = {"scoreFor": [], "value": [], "scale": []}
    for sc in g.subjects(RDF.type, EVAL_SCORE):
        if not isinstance(sc, URIRef):
            continue
        if not any(True for _ in g.objects(sc, SCORE_FOR_PRINCIPLE)):
            score_missing["scoreFor"].append(sc)
        if not any(True for _ in g.objects(sc, SCORE_VALUE)):
            score_missing["value"].append(sc)
        if not any(True for _ in g.objects(sc, HAS_SCORE_SCALE)):
            score_missing["scale"].append(sc)

    if not any(score_missing.values()):
        line("PASS: All score components have criterion principle, numeric value, and score scale.")
    else:
        line("FAIL: Some score components are incomplete:")
        for k, vals in score_missing.items():
            if vals:
                line(f"  - missing {k}: " + ", ".join(local_name(v) for v in vals))

    line("")

    # 3) Hygiene checks
    line("3) Token-vs-class hygiene checks")
    line("-" * 33)

    token_props = [OPERATIONALIZES, AGAINST_PRINCIPLE, SCORE_FOR_PRINCIPLE]
    hygiene_violations: List[Tuple[URIRef, URIRef, URIRef, str]] = []
    for p in token_props:
        for s, _, o in g.triples((None, p, None)):
            if not (isinstance(s, URIRef) and isinstance(o, URIRef)):
                continue
            if not token_is_design_principle(g, o):
                why = []
                if (o, RDF.type, OWL.Class) in g:
                    why.append("owl:Class")
                if not is_named_individual(g, o):
                    why.append("not owl:NamedIndividual")
                hygiene_violations.append((s, p, o, ", ".join(why) if why else "not a design-principle token"))

    if not hygiene_violations:
        line("PASS: No misuse detected for operationalizes/against/score-for (objects look like principle tokens).")
    else:
        line("FLAG: Potential misuse detected (these relations should point to principle TOKENS):")
        for s, p, o, why in hygiene_violations[:20]:
            line(f"  - {local_name(s)} {local_name(p)} {local_name(o)}  [{why}]")
        if len(hygiene_violations) > 20:
            line(f"  ... ({len(hygiene_violations)-20} more)")
        if args.negative:
            line("NOTE: These are expected if you ran with --negative.")

    line("")

    # 4) Rule-based materialization
    line("4) Rule-based materialization (safe closure)")
    line("-" * 43)

    hasvalue_axioms_all = extract_hasvalue_axioms(g, AIMS_AT)
    added_aims = materialize_hasvalue_inferences(g, hasvalue_axioms_all)
    line(f"INFO: Materialized {added_aims} aims-at triples from hasValue definitions (token -> target proxy).")

    added_evalrel = materialize_property_chain(g, ABOUT_METHOD, OPERATIONALIZES, EVAL_RELEVANT)
    added_presc = materialize_property_chain(g, HAS_PRESCRIPTION_COMPONENT, CCO_PRESCRIBES, PRESCRIBES_VIA_COMPONENT)
    line(f"INFO: Materialized {added_evalrel} has-evaluation-relevant-principle triples (method traceability chain).")
    line(f"INFO: Materialized {added_presc} prescribes-via-component triples (prescription-component chain).")

    added_inv = materialize_inverse_properties(g, inv_pairs)
    line(f"INFO: Materialized {added_inv} inverse-property triples (from owl:inverseOf).")

    inferred_comm_honesty = 0
    for e in list(g.subjects(RDF.type, EVAL_RECORD)):
        if not isinstance(e, URIRef):
            continue
        if not any(True for _ in g.objects(e, ABOUT_COMM_CONTENT)):
            continue
        for p in g.objects(e, AGAINST_PRINCIPLE):
            if isinstance(p, URIRef) and (p, RDF.type, PRINCIPLE_OF_HONESTY) in g:
                if (e, RDF.type, COMM_HONESTY_EVAL) not in g:
                    g.add((e, RDF.type, COMM_HONESTY_EVAL))
                    inferred_comm_honesty += 1

    toy_eval = EX["Eval_Toy_ManualHonesty_001"]
    if (toy_eval, RDF.type, COMM_HONESTY_EVAL) in g:
        line(f"PASS: {local_name(toy_eval)} classified as design communicative honesty evaluation.")
    else:
        line(f"FAIL: {local_name(toy_eval)} NOT classified as design communicative honesty evaluation.")

    line(f"INFO: Inferred {inferred_comm_honesty} communicative honesty evaluation(s) (defined-class style).")
    line("")

    # 5) Disjointness
    line("5) Disjointness violation detection")
    line("-" * 34)

    disj_viol = check_disjointness_violations(g)
    if not disj_viol:
        line("PASS: No disjointness violations detected in loaded graphs.")
    else:
        line("FLAG: Disjointness violations detected:")
        for x, a, b in disj_viol[:20]:
            line(f"  - {local_name(x)} typed as both {local_name(a)} and {local_name(b)}")
        if len(disj_viol) > 20:
            line(f"  ... ({len(disj_viol)-20} more)")
        if args.negative:
            line("NOTE: These are expected if you ran with --negative.")

    line("")

    # 6) Contrast demonstrations
    line("6) Contrast demonstrations (expected 'FLAG' outcomes)")
    line("-" * 55)

    range_contrast = Graph()
    range_contrast += g
    range_contrast.add((AIMS_AT, RDFS.range, BFO["BFO_0000019"]))

    added_range = materialize_range_inference(range_contrast, AIMS_AT)
    targets = {ax.value for ax in hasvalue_axioms_all}
    typed_by_range = [t for t in targets if (t, RDF.type, BFO["BFO_0000019"]) in range_contrast]
    if typed_by_range:
        ex_t = sorted(typed_by_range, key=str)[0]
        line(f"FLAG: With an added rdfs:range on aims-at, {len(typed_by_range)} target proxies become rdf:type quality (level-mixing risk).")
        line(f"      Example: {local_name(ex_t)} is inferred rdf:type BFO_0000019 under the range rule.")
    else:
        line("INFO: Range-contrast did not type any target proxies as quality (unexpected under typical RDFS range inference).")

    line(f"INFO: Range-contrast added {added_range} rdf:type triple(s) via the range rule.")

    exist_added, exist_bnodes = materialize_existentials_somevaluesfrom(g, AIMS_AT)
    if exist_bnodes > 0:
        line(f"FLAG: Existential (someValuesFrom) demo created {exist_bnodes} blank-node 'phantom target' instance(s).")
        line(f"      (Added {exist_added} triple(s) to satisfy existentials.)")
    else:
        line("INFO: No existential demo blank nodes created (unexpected if the naive class is present).")

    line("")

    # Write outputs
    out_report = here / args.out_report
    out_inferred = here / args.out_inferred

    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    g.serialize(destination=str(out_inferred), format="turtle")

    print("\n".join(report_lines))
    print(f"\nWrote: {out_report.name}")
    print(f"Wrote: {out_inferred.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
