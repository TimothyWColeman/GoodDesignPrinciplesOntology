# GDPO Extended Validation Artifact

This artifact extends the original “validation template” by adding validation points
beyond the two OWL property chains, including:

- **OWL2-punning / targets-as-universals checks** for `gdpo:GDPO0000454` (aims-at artifact-side target)
- **OWL 2 DL safety guard** for the *prescribes-via-prescription-component* chain (no subPropertyOf `cco:prescribes`)
- **ABox completeness checks** (SHACL-like, closed-world) for evaluation records and score components
- **RDF hygiene checks** to catch accidental links to principle *classes* when principle *tokens* are intended
- **Inverse-property closure demonstrations** (where declared in the ontology)
- **Defined-class regression** (rule-materialized) for communicative honesty evaluations
- Two contrast demonstrations from the paper:
  - **Range axiom on aims-at** ⇒ level-mixing under punning
  - **Existential (someValuesFrom)** ⇒ “phantom target instance” creation

## Files

- `gdpo_extended_validation.ttl` — base toy ABox (intended-to-pass)
- `gdpo_extended_validation_negative.ttl` — optional negative tests (load with `--negative`)
- `gdpo_validation_shapes.ttl` — companion SHACL shapes graph (documentation); runner evaluates equivalent checks
- `queries.sparql` — SPARQL reference patterns (not required by the runner)
- `run_extended_validation.py` — runnable validation script
- `gdpo_extended_validation_inferred.ttl` — output inferred graph (written by runner)
- `extended_validation_output.txt` — pasteable output report (written by runner)
- `appendix_extended_validation_artifact.md` — paste-ready appendix text (markdown)
- `GoodDesignPrinciplesOntology20260116v4.0.3.ttl` — ontology used for the run (included for reproducibility)

## How to run

From this directory:

```bash
python run_extended_validation.py
```

To include the intentional negative tests:

```bash
python run_extended_validation.py --negative
```
