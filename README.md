# The Good Design Principles Ontology (GDPO): Making Rams’ Philosophy Actionabe

The **Good Design Principles Ontology (GDPO)** is an applied ontology that formalizes Dieter Rams’ *Ten Principles of Good Design* within a rigorous semantic framework (**BFO 2020, CCO 2.0**).  

Rams’ philosophy has shaped generations of products—from Braun’s SK4 record player to Apple’s iPhone—but until now it has remained a human-readable philosophy rather than a machine-interpretable framework.  

**GDPO changes that**, turning “good design” into structured, computable data that can be embedded directly into the workflows of design-driven companies.

---

## Why GDPO Matters for Industry

Leading firms such as **Apple, IDEO, and Braun** already anchor their design culture in principles like *honesty*, *minimalism*, and *usefulness*. But today’s design teams operate in complex product lifecycle environments:

- Global supply chains  
- Sustainability reporting  
- Regulatory compliance  
- Digital twin ecosystems  

Rams’ principles, in their original narrative form, cannot be measured, audited, or integrated into these systems.  

**GDPO provides the missing bridge:**

- **Structured Design Evaluation**  
  Captures who reviewed a design, when, using which method, against which principle, and with what score.  
  → Evaluations become traceable, auditable, and comparable.  

- **Lifecycle & Sustainability Integration**  
  Principles like durability and environmental friendliness are tied to lifecycle processes (*sourcing, manufacturing, use, end-of-life*).  
  → Links Rams’ ideals to ESG dashboards, supply chain ethics, and circular economy metrics.  

- **Design Toolchain Embedding**  
  Works inside tools designers already use (Figma, CAD/PLM, generative design).  
  → Dashboards can flag violations (e.g., minimalism, durability) or auto-score prototypes.  

---

## Innovation Potential

GDPO is not just a compliance framework—it’s an **innovation enabler**:

- **AI-Assisted Design**  
  Serves as a constraint layer for generative design tools, ensuring outputs respect Rams’ principles.  
  → Imagine AI prototypes that are honest, minimal, and durable by default.  

- **Cross-Company Benchmarking**  
  Formalized principles allow companies to benchmark design quality across portfolios and industries.  

- **Future-Proofing Brand Integrity**  
  Enforces timeless principles in a world dominated by speed and novelty.  
  → Transforms Rams’ motto *“Less, but better”* into a living rule across development stages.  

---

## Value Proposition

- **For Apple**  
  Extend Jony Ive’s Rams-inspired legacy by embedding “good design” into AI-assisted prototyping and lifecycle compliance.  

- **For IDEO**  
  Strengthen human-centered design methodologies with computable principles, creating new opportunities for scalable, principle-driven innovation.  

- **For Braun**  
  Reconnect with Rams’ origins by auditing and evolving products against the very ideals the company introduced.  

# GoodDesignPrinciplesOntology
Good Design Principles

The Good Design Principles Ontology (GDPO) formally represents Rams’ Ten Principles of Good Design as a hierarchy of classes within the framework of Basic Formal Ontology (BFO 2020) and aligned with the Common Core Ontologies (CCO 2.0).

Modeling approach 
• Each of Rams’ principles is represented as a class under ‘design principle’ (a directive information content entity, DICE). 
• Every principle prescribes one or more design process types (e.g., design innovation process, design use process, design interaction process, design lifecycle process). 
• Process classes are occurrents that have participants: an Agent and a Material Entity (the designed artifact).
• Realizable entities are modeled on the artifact side: functions and dispositions ‘inhere in’ a material entity and are ‘realized in’ the appropriate process types; qualities (e.g., aesthetic, unobtrusiveness, minimalism, thoroughness) are modeled as qualities that ‘inhere in’ a material entity (qualities are not realized).
• The historically bounded set of the ten principles is captured by the class ‘rams ten principles specification’, a principle specification that ‘has continuant part’ each of the ten principle classes.

Intended use: GDPO supports principled annotation and comparison of design practices and artifacts against Rams’ framework. Conformance scoring, assessment methods, and provenance may be added at the instance (ABox) level without altering the TBox: e.g., evaluation records, assessors, dates, and methods.

Interoperability: All assertions use BFO 2020 relations (including ‘has continuant part’ for ICE–ICE mereology) and CCO classes for agents and artifacts, ensuring compatibility with adjacent ontologies and data pipelines.

Each of Rams’ ten principles is represented as a distinct class under Design Principle:

1) Design Innovativeness – Good design is innovative.
2) Design Usefulness – Good design makes a product useful.
3) Design Aesthetic Quality – Good design is aesthetic.
4) Design Understandability – Good design makes a product understandable.
5) Design Unobtrusiveness – Good design is unobtrusive.
6) Design Honesty – Good design is honest.
7) Design Durability – Good design is long lasting.
8) Design Thoroughness – Good design is thorough down to the last detail.
9) Design Environmental Friendliness – Good design is environmentally friendly.
10) Design Minimalism – Good design is as little design as possible.

All ten principles are modeled as directive information content entities (DICE), which means they prescribe norms or constraints that design processes should follow. These classes are linked upward to Good Design, providing a unifying node for reasoning about Rams’ philosophy as a whole. Subclass axioms connect each principle to either qualities (such as aesthetic quality or durability) or roles and processes (such as understandability or usefulness).


Relationships and Usage: The ontology enables modeling of how design principles prescribe and evaluate design processes and artifacts.

Each design principle is modeled as prescriptive, guiding particular types of design processes. For example, Design Innovativeness prescribes design innovation processes, while Design Environmental Friendliness prescribes design lifecycle processes that minimize ecological impact.

Principles are tied to artifacts through the qualities, functions, or dispositions they emphasize. For example, Design Aesthetic Quality captures perceptual form, while Design Usefulness specifies the function an artifact fulfills in its context of use.

The ontology can also be used for evaluation and annotation. Principles can serve as annotation points in assessing whether a product conforms to one or more aspects of Rams’ framework. For example, a Braun SK4 record player may be annotated as conforming to Design Minimalism and Design Usefulness, while an iPhone may be annotated as conforming to Design Aesthetic Quality and Design Understandability.

Applications of the Ontology: This ontology can be used for design evaluation, enabling structured assessment of products or prototypes against Rams’ principles. It can support historical analysis by comparing design philosophies across time, such as mapping Rams’ principles against Apple’s design language or contemporary sustainability standards. It can also be used pedagogically, teaching design students how abstract principles are represented ontologically and applied to real-world cases. Finally, it can be integrated into digital design tools, where it can guide concept generation and ensure conformity with the principles of good design.

The Good Design Principles Ontology (GDPO) preserves and formalizes the intellectual legacy of Dieter Rams, transforming his Ten Principles into machine-readable and logically coherent entities. By aligning with BFO 2020 and CCO 2.0, the ontology ensures interoperability with broader knowledge ecosystems, enabling designers, historians, educators, and technologists to apply Rams’ vision systematically.

This ontology is not only a representation of Rams’ philosophy but also a living framework for modeling and evaluating design practices, ensuring that good design—innovative, useful, aesthetic, honest, and sustainable—remains an enduring ideal.

## 20 Competency Questions

# About Principles and Processes
1) Which design processes does the principle of innovativeness prescribe?
2) Which principle of good design prescribes a design use process?
3) Which design evaluation methods operationalize the principle of minimalism?
4) Which design principles apply to a given design lifecycle process?
5) Which qualities or dispositions are linked to a specific design principle?

# About Evaluations
6) What artifacts (material entities) have been the subject of a design evaluation?
7) Which principles was a particular artifact evaluated against?
8) Which evaluation method specification was used in a given design evaluation?
9) What numeric score was assigned to an artifact in its last design evaluation?
10) On what date was an artifact last assessed for conformity to Rams’ principles?

# About Methods
11) Which evaluation method specification prescribes a design evaluation process?
12) Which principles does a given evaluation method specification operationalize?
13) Are there multiple methods used to evaluate the same principle?
14) Which principle is most frequently associated with evaluation methods in this ontology?

# About Qualities and Dispositions
15) Which qualities (e.g., aesthetic quality, minimalism quality) inhere in a given artifact?
16) Which dispositions (e.g., honesty, durability) of an artifact are realized in which processes?
17) Which aspects of honesty (material, functional, communicative) does a given artifact exhibit?

# Historical and Structural
18) Which principles are part of the Rams ten principles specification?
19) How does the ontology distinguish between qualities (e.g., aesthetic quality) and principles (e.g., principle of aesthetics)?
20) Which agents carried out a design evaluation process for a given artifact?

## SPARQL Queries

# CQ1. Which design processes does the principle of innovativeness prescribe?
- Find processes prescribed by the "principle of innovativeness"
  
SELECT ?process ?processLabel WHERE {
  ?principle rdfs:label "principle of innovativeness"@en .
  ?principle <https://www.commoncoreontologies.org/ont00001942> ?process .
  ?process rdfs:label ?processLabel .
}

# CQ7. Which principles was a particular artifact evaluated against?
(Say the artifact is a Braun SK4 record player individual, labeled “Braun SK4”)
- For a given artifact, list the principles it was evaluated against

SELECT ?principle ?principleLabel WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000045> ?artifact .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000046> ?principle .
  ?principle rdfs:label ?principleLabel .
}

# CQ8. Which evaluation method specification was used in a given design evaluation?
(Say evaluation record labeled “SK4 evaluation 1970”)
- What method was used in a given design evaluation?

SELECT ?method ?methodLabel WHERE {
  ?evaluation rdfs:label "SK4 evaluation 1970"@en .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000048> ?method .
  ?method rdfs:label ?methodLabel .
}

# CQ9. What numeric score was assigned to an artifact in its last design evaluation?
- Retrieve the score(s) given to an artifact in its evaluations

SELECT ?evaluation ?date ?score WHERE {
  ?artifact rdfs:label "Braun SK4"@en .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000045> ?artifact .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000050> ?date .
  ?evaluation <https://www.ramsprinciplesofgooddesign.com/GDPO0000047> ?score .
}
ORDER BY DESC(?date)
LIMIT 1


