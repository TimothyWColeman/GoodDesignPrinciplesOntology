# Validation

This folder records the baseline validation checks for the current GDPO release.

## Current Release

- Ontology: `../ontology/gdpo-4.0.3.ttl`
- XML catalog: `../ontology/catalog-v001.xml`
- Imported upper ontologies: BFO 2020 and stable CCO 2.0

## Baseline Checks

Run these checks from the repository root:

```bash
python3 -m pip install -r validation/requirements.txt
python3 validation/validate_gdpo.py
```

The current release should satisfy the following manuscript-alignment checks:

- no `owl:hasValue` target restrictions
- no GDPO entity declared as both `owl:Class` and `owl:NamedIndividual`
- no named prescription-component individual asserting a process-type class as an ABox object-property value
- CCO imports pinned to stable CCO 2.0 version IRIs
- lifecycle-stage applicability for multi-stage prescriptions represented with union fillers rather than repeated intersective `only` restrictions
- `has material bearer` treated as optional lightweight provenance only
- the example communicative-honesty record is typed as a generic evaluation record and is inferred as both an honesty evaluation and a communicative-honesty evaluation under OWL-RL

## Notes

These checks are intentionally lightweight. The article-specific SK4 fixture,
seven SPARQL templates, deterministic results, and two OWL-RL entailment tests
are maintained in `../supplement/manuscript-validation/`. Future releases can
add SHACL shapes, ROBOT reports, broader regression suites, and full DL reasoner
profiles.

The GitHub Actions workflow in `.github/workflows/validate.yml` runs the same
script on pushes and pull requests to `main`.
