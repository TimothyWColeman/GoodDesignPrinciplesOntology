# GDPO Design Patterns

Version: 4.0.3  
Last Updated: 2026-01-17

This document describes the key design patterns used in GDPO, with Mermaid diagrams illustrating the relationships between classes and properties.

---

## Table of Contents

1. [Prescription Component Pattern](#1-prescription-component-pattern)
2. [Evaluation Record Pattern](#2-evaluation-record-pattern)
3. [Reified Score Pattern](#3-reified-score-pattern)
4. [Temporal Region Indexing Pattern](#4-temporal-region-indexing-pattern-v402)
5. [Aims-At Pattern](#5-aims-at-pattern-v402)
6. [Process–Record Linkage Pattern](#6-processrecord-linkage-pattern)
7. [Honesty Evaluation Patterns](#7-honesty-evaluation-patterns)
8. [Lifecycle Stage Pattern](#8-lifecycle-stage-pattern)

---

## 1. Prescription Component Pattern

Principles prescribe processes via reified prescription components, enabling temporal and conditional qualifiers.

```mermaid
graph LR
    subgraph ICE["Information Content Entities"]
        P[design principle]
        DPP[design process prescription]
    end
    
    subgraph Processes["Process Types"]
        PROC[design process]
        LCS[design lifecycle stage process]
    end
    
    P -->|has prescription component| DPP
    DPP -->|cco:prescribes| PROC
    DPP -->|applies during lifecycle stage| LCS
    
    style P fill:#e1f5fe
    style DPP fill:#e1f5fe
    style PROC fill:#fff3e0
    style LCS fill:#fff3e0
```

**Example:**
```turtle
gdpo:GDPO0000067  # principle of usefulness statement
    gdpo:GDPO0000062 gdpo:GDPO0000077 .  # has prescription component

gdpo:GDPO0000077  # usefulness prescription
    cco:ont00001942 gdpo:GDPO0000015 ;   # prescribes: design use process
    gdpo:GDPO0000063 gdpo:GDPO0000039 .  # applies during: use and maintenance
```

**When to use:** When you need to specify what processes a principle prescribes and under what conditions (lifecycle stage, temporal scope).

---

## 2. Evaluation Record Pattern

Evaluation records capture assessments with full provenance linking artifact, principle(s), method, and temporal context.

```mermaid
graph TB
    subgraph Record["Design Evaluation Record (ICE)"]
        DER[design evaluation record]
    end
    
    subgraph Targets["What is Evaluated"]
        ART[material entity<br/>artifact]
        PRIN[design principle]
    end
    
    subgraph Context["Evaluation Context"]
        METH[evaluation method<br/>specification]
        TR[temporal region]
    end
    
    DER -->|is about evaluated artifact| ART
    DER -->|against principle| PRIN
    DER -->|is about using method| METH
    DER -->|assessed during temporal region| TR
    
    style DER fill:#e8f5e9
    style ART fill:#fce4ec
    style PRIN fill:#e1f5fe
    style METH fill:#e1f5fe
    style TR fill:#f3e5f5
```

**Necessary conditions (equivalentClass):**
- `is about evaluated artifact` some `material entity`
- `against principle` some `design principle`
- `assessed during temporal region` some `temporal region`

---

## 3. Reified Score Pattern

For multi-criterion evaluations, scores are reified as separate entities with principle and scale context.

```mermaid
graph TB
    subgraph Evaluation
        DER[design evaluation record]
    end
    
    subgraph Scores["Score Components"]
        SC1[design evaluation score]
        SC2[design evaluation score]
    end
    
    subgraph Context
        P1[principle 1]
        P2[principle 2]
        SCALE[score scale specification]
    end
    
    DER -->|has score component| SC1
    DER -->|has score component| SC2
    SC1 -->|score value| V1["4.8 (xsd:decimal)"]
    SC1 -->|score for principle| P1
    SC1 -->|has score scale| SCALE
    SC2 -->|score value| V2["5.0 (xsd:decimal)"]
    SC2 -->|score for principle| P2
    SC2 -->|has score scale| SCALE
    
    style DER fill:#e8f5e9
    style SC1 fill:#fff8e1
    style SC2 fill:#fff8e1
    style SCALE fill:#e1f5fe
```

**When to use:** When evaluating against multiple principles or using multiple scoring scales. Prefer this over multiple `has score` literals directly on the record.

**Legacy shortcut:** For single-criterion evaluations, `has score` (xsd:decimal) directly on the record is acceptable.

---

## 4. Temporal Region Indexing Pattern (v4.0.3)

GDPO v4.0.3 introduces BFO 2020–compliant temporal indexing using temporal regions instead of (or in addition to) xsd:dateTime literals.

```mermaid
graph TB
    subgraph Continuants["Continuant Entities"]
        DER[design evaluation record]
        DPP[design process prescription]
    end
    
    subgraph Temporal["BFO Temporal Regions"]
        TR1[temporal region<br/>e.g., Q4 2025]
        TR2[temporal region<br/>e.g., 2025-12-15]
    end
    
    DER -->|assessed during temporal region| TR2
    DPP -->|applies during temporal region| TR1
    
    subgraph Legacy["Legacy Pattern"]
        DER -.->|assessed_on| DT["xsd:dateTime"]
    end
    
    style DER fill:#e8f5e9
    style DPP fill:#e1f5fe
    style TR1 fill:#f3e5f5
    style TR2 fill:#f3e5f5
    style DT fill:#eeeeee
```

**Properties:**

| Property | Domain | Range | Use |
|----------|--------|-------|-----|
| `assessed during temporal region` (GDPO0000468) | evaluation record | BFO:temporal region | When evaluation occurred |
| `applies during temporal region` (GDPO0000467) | process prescription | BFO:temporal region | When prescription applies |
| `assessed_on` (GDPO0000050) | evaluation record | xsd:dateTime | Legacy timestamp |

**When to use temporal regions:**
- Integration with time ontologies (OWL-Time)
- Interval-based reasoning (periods, not instants)
- Full BFO 2020 compliance

**When legacy xsd:dateTime is acceptable:**
- Lightweight timestamping
- Point-in-time records
- Systems not requiring temporal region modeling

---

## 5. Aims-At Pattern (v4.0.3)

Principles aim at artifact-side targets (qualities, functions, dispositions) using OWL2 punning.

```mermaid
graph LR
    subgraph Principles["Principle Classes"]
        PA[principle of aesthetics]
        PU[principle of usefulness]
        PH[principle of honesty]
    end
    
    subgraph Targets["Artifact-Side Targets (Punned)"]
        AQ[design aesthetic quality]
        UF[design usefulness]
        DH[design honesty]
    end
    
    PA -->|aims at artifact-side target| AQ
    PU -->|aims at artifact-side target| UF
    PH -->|aims at artifact-side target| DH
    
    style PA fill:#e1f5fe
    style PU fill:#e1f5fe
    style PH fill:#e1f5fe
    style AQ fill:#fff3e0
    style UF fill:#fff3e0
    style DH fill:#fff3e0
```

**Implementation notes:**
- Target values are punned individuals (classes treated as individuals)
- OWL range restrictions intentionally omitted (v4.0.3) to avoid treating targets as instances of BFO categories
- Validate via SHACL: target must be an IRI and a subclass of quality/function/disposition

**SHACL validation:**
```turtle
gdpo-shapes:AimsAtTargetShape a sh:NodeShape ;
    sh:targetSubjectsOf gdpo:GDPO0000454 ;
    sh:property [
        sh:path gdpo:GDPO0000454 ;
        sh:nodeKind sh:IRI ;
        sh:message "Target must be an IRI (punned class)"
    ] .
```

---

## 6. Process–Record Linkage Pattern

Evaluation processes produce evaluation records, establishing truthmaker provenance.

```mermaid
graph LR
    subgraph Process["Occurrent"]
        DEP[design evaluation process]
    end
    
    subgraph Record["ICE"]
        DER[design evaluation record]
    end
    
    subgraph Participants
        AGENT[agent]
        ART[artifact]
    end
    
    DEP -->|has evaluation record output| DER
    DER -->|is evaluation record output of| DEP
    DEP -->|evaluation carried out by| AGENT
    DEP -->|has evaluated artifact participant| ART
    
    style DEP fill:#fff3e0
    style DER fill:#e8f5e9
    style AGENT fill:#fce4ec
    style ART fill:#fce4ec
```

**Truthmaker grounding:** The evaluation record's assertions are grounded in:
1. The evaluation process that produced it
2. The outcome-bearing configuration measured during that process

---

## 7. Honesty Evaluation Patterns

GDPO distinguishes interaction honesty (artifact-borne) from communicative honesty (claims/marketing).

### 7a. Interaction Honesty Evaluation

```mermaid
graph TB
    IHE[design interaction<br/>honesty evaluation]
    ART[artifact]
    POH[principle of honesty]
    
    IHE -->|is about evaluated artifact| ART
    IHE -->|against principle| POH
    
    style IHE fill:#e8f5e9
    style ART fill:#fce4ec
    style POH fill:#e1f5fe
```

**Use for:** Evaluating whether controls, affordances, and perceptible cues align with actual functions.

### 7b. Communicative Honesty Evaluation

```mermaid
graph TB
    CHE[design communicative<br/>honesty evaluation]
    ART[artifact]
    POH[principle of honesty]
    CC[communication content<br/>manual / label / ad]
    
    CHE -->|is about evaluated artifact| ART
    CHE -->|against principle| POH
    CHE -->|is about communication content| CC
    
    style CHE fill:#e8f5e9
    style ART fill:#fce4ec
    style POH fill:#e1f5fe
    style CC fill:#e1f5fe
```

**Use for:** Evaluating whether manuals, labels, or advertisements truthfully represent the artifact.

**Communication content subclasses:**
- `product manual content` (GDPO0000447)
- `product label content` (GDPO0000448)
- `product advertisement content` (GDPO0000449)

---

## 8. Lifecycle Stage Pattern

Environmental friendliness and other lifecycle-dependent principles use lifecycle stage processes.

```mermaid
graph TB
    subgraph Principle
        PEF[principle of<br/>environmental friendliness]
    end
    
    subgraph Prescription
        DPP[design process prescription]
    end
    
    subgraph Stages["Lifecycle Stage Processes"]
        SRC[sourcing]
        MFG[manufacturing]
        DST[distribution]
        USE[use & maintenance]
        EOL[end-of-life]
    end
    
    PEF -->|has prescription component| DPP
    DPP -->|applies during lifecycle stage| SRC
    DPP -->|applies during lifecycle stage| MFG
    DPP -->|applies during lifecycle stage| DST
    DPP -->|applies during lifecycle stage| USE
    DPP -->|applies during lifecycle stage| EOL
    
    style PEF fill:#e1f5fe
    style DPP fill:#e1f5fe
    style SRC fill:#fff3e0
    style MFG fill:#fff3e0
    style DST fill:#fff3e0
    style USE fill:#fff3e0
    style EOL fill:#fff3e0
```

**Lifecycle stage classes:**
| Class | Description |
|-------|-------------|
| `design sourcing process` | Material/component acquisition |
| `design manufacturing process` | Artifact production |
| `design distribution process` | Delivery to end users |
| `design use and maintenance process` | Normal operation and upkeep |
| `design end-of-life handling process` | Disposal, recycling, reuse |

---

## Color Legend

| Color | Meaning |
|-------|---------|
| Blue (#e1f5fe) | Information Content Entities (ICE) |
| Orange (#fff3e0) | Processes (Occurrents) |
| Green (#e8f5e9) | Evaluation Records |
| Pink (#fce4ec) | Material Entities / Agents |
| Purple (#f3e5f5) | Temporal Regions |
| Yellow (#fff8e1) | Score Components |
| Gray (#eeeeee) | Legacy / Deprecated |

---

## Version History

| Version | Patterns Added/Changed |
|---------|------------------------|
| v1.4.7 | Evaluation Record Pattern |
| v1.5.1 | Lifecycle Stage Pattern |
| v3.0.0 | Prescription Component Pattern |
| v4.0.0 | Reified Score Pattern, Honesty Evaluation Patterns, Process–Record Linkage |
| v4.0.3 | Temporal Region Indexing Pattern, Aims-At Pattern (range removal) |
