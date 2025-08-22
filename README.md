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
