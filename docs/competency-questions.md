# GDPO Competency Questions

This document lists the 20 competency questions that the Good Design Principles Ontology (GDPO) is designed to answer.

## About Principles and Processes

1. **Which design processes does the principle of innovativeness prescribe?**
2. **Which principle of good design prescribes a design use process?**
3. **Which design evaluation methods operationalize the principle of minimalism?**
4. **Which design principles apply to a given design lifecycle process?**
5. **Which qualities or dispositions are linked to a specific design principle?**

## About Evaluations

6. **What artifacts (material entities) have been the subject of a design evaluation?**
7. **Which principles was a particular artifact evaluated against?**
8. **Which evaluation method specification was used in a given design evaluation?**
9. **What numeric score was assigned to an artifact in its last design evaluation?**
10. **On what date was an artifact last assessed for conformity to Rams' principles?**

## About Methods

11. **Which evaluation method specification prescribes a design evaluation process?**
12. **Which principles does a given evaluation method specification operationalize?**
13. **Are there multiple methods used to evaluate the same principle?**
14. **Which principle is most frequently associated with evaluation methods in this ontology?**

## About Qualities and Dispositions

15. **Which qualities (e.g., aesthetic quality, minimalism quality) inhere in a given artifact?**
16. **Which dispositions (e.g., honesty, durability) of an artifact are realized in which processes?**
17. **Which aspects of honesty (material, functional, communicative) does a given artifact exhibit?**

## Historical and Structural

18. **Which principles are part of the Rams ten principles specification?**
19. **How does the ontology distinguish between qualities (e.g., aesthetic quality) and principles (e.g., principle of aesthetics)?**
20. **Which agents carried out a design evaluation process for a given artifact?**

---

## Notes on Answering Competency Questions

### Principle vs. Quality Distinction (CQ19)

GDPO distinguishes:
- **Principles** (directive ICEs): Prescribe what *should* be the case (e.g., `principle of aesthetics`)
- **Qualities** (BFO qualities): Describe what *is* the case in an artifact (e.g., `design aesthetic quality`)

The principle `cco:is_about` the corresponding quality, creating a semantic bridge between normative and descriptive content.

### Honesty Facets (CQ17)

Three facets of honesty are modeled differently:
- **Material honesty**: Disposition inhering in artifact (`design material honesty`)
- **Functional honesty**: Disposition inhering in artifact (`design functional honesty`)
- **Communicative honesty**: Evaluated via `design communicative honesty evaluation` records about communication artifacts

### Evaluation vs. Process (CQ6, CQ20)

- `design evaluation` is an ICE (record/document)
- `design evaluation process` is a BFO process (activity)
- The process `has_output` the evaluation record
- Agents participate in the process, not the record directly
