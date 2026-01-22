## Appendix (Extended Validation Artifact for GDPO)

This appendix provides a runnable validation artifact that reproduces and extends
the paper’s validation points, including property-chain behavior, punning/target
constraints, and closed-world data-quality checks.

### What it validates

**TBox / ontology checks**
1. `gdpo:aims at artifact-side target (GDPO0000454)` has *no asserted OWL range* (to avoid level-mixing under punning).
2. The two GDPO property chains are present:
   - `(gdpo:is about using method ∘ gdpo:operationalizes principle) ⊑ gdpo:has evaluation-relevant principle`
   - `(gdpo:has prescription component ∘ cco:prescribes) ⊑ gdpo:prescribes via prescription component`
3. **OWL 2 DL safety guard**: `gdpo:prescribes via prescription component` is *not* asserted as a subproperty of `cco:prescribes`.
4. Rams principle categories use the `owl:hasValue` pattern on `gdpo:aims at artifact-side target`.
5. Targets used in those definitions are OWL2-punned and (as classes) fall under
   `quality ∪ function ∪ disposition` (allowing relational quality where used).

**ABox / instance-data checks (closed-world / SHACL-like)**
6. Every `gdpo:design evaluation record` has:
   - `gdpo:is about evaluated artifact`
   - `gdpo:against principle`
   - `gdpo:assessed during temporal region`
7. Every `gdpo:design evaluation score` has:
   - `gdpo:score for principle`
   - `gdpo:score value`
   - `gdpo:has score scale`

**Hygiene / robustness checks**
8. For method and evaluation relations that *should* point to **principle tokens**,
   detect accidental pointers to **principle classes**:
   - `gdpo:operationalizes principle`
   - `gdpo:against principle`
   - `gdpo:score for principle`

**Rule-materialized demonstrations (no OWL reasoner required)**
9. Materialize the two property chains as explicit triples (for inspection and QA).
10. Materialize defined-class behavior for communicative honesty evaluations:
    an evaluation record that is (a) against the honesty principle token and
    (b) about communication content is classified as `gdpo:design communicative honesty evaluation`.

**Contrast demonstrations**
11. Add a range axiom to `gdpo:aims at artifact-side target` and show the resulting level-mixing (targets typed as dependent continuants).
12. Add a naive existential (`someValuesFrom`) definition and show the resulting “phantom target” instance creation.

### How to run

Unzip the artifact, then:

```bash
python run_extended_validation.py
```

Optional: include intentional negative tests (expected to be flagged, not “mysterious failures”):

```bash
python run_extended_validation.py --negative
```

The runner writes:
- `extended_validation_output.txt`
- `gdpo_extended_validation_inferred.ttl`
