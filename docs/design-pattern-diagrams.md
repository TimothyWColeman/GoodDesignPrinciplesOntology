# GDPO Design Pattern Diagrams

Mermaid diagrams illustrating the ontological design patterns that answer each competency question.

---

## CQ1: Which design processes does the principle of innovativeness prescribe?

**Pattern:** Principle → Prescription Component → Process

```mermaid
graph LR
    subgraph "Directive ICE Layer"
        P[principle of innovativeness<br/><i>gdpo:GDPO0000020</i>]
        DPP[design process prescription<br/><i>gdpo:GDPO0000061</i>]
    end
    
    subgraph "Process Layer"
        DIP[design innovation process<br/><i>gdpo:GDPO0000014</i>]
    end
    
    P -->|has prescription component<br/><i>gdpo:GDPO0000062</i>| DPP
    DPP -->|prescribes<br/><i>cco:ont00001942</i>| DIP
    
    style P fill:#e1f5fe
    style DPP fill:#fff3e0
    style DIP fill:#f3e5f5
```

---

## CQ2: Which principle of good design prescribes a design use process?

**Pattern:** Reverse lookup from Process → Prescription → Principle

```mermaid
graph RL
    subgraph "Process Layer"
        DUP[design use process<br/><i>gdpo:GDPO0000015</i>]
    end
    
    subgraph "Directive ICE Layer"
        DPP[design process prescription<br/><i>gdpo:GDPO0000061</i>]
        PU[principle of usefulness<br/><i>gdpo:GDPO0000021</i>]
    end
    
    DUP -.->|prescribed by| DPP
    DPP -.->|prescription component of| PU
    
    style PU fill:#e1f5fe
    style DPP fill:#fff3e0
    style DUP fill:#f3e5f5
```

---

## CQ3: Which design evaluation methods operationalize the principle of minimalism?

**Pattern:** Method → operationalizes → Principle

```mermaid
graph LR
    subgraph "Method Layer"
        EMS[evaluation method specification<br/><i>gdpo:GDPO0000052</i>]
    end
    
    subgraph "Principle Layer"
        PM[principle of minimalism<br/><i>gdpo:GDPO0000029</i>]
    end
    
    EMS -->|operationalizes principle<br/><i>gdpo:GDPO0000054</i>| PM
    
    style EMS fill:#fff3e0
    style PM fill:#e1f5fe
```

---

## CQ4: Which design principles apply to a given design lifecycle process?

**Pattern:** Principle → Prescription → applies during → Lifecycle Stage

```mermaid
graph TB
    subgraph "Principle Layer"
        PEF[principle of environmental friendliness<br/><i>gdpo:GDPO0000028</i>]
    end
    
    subgraph "Prescription Layer"
        DPP1[design process prescription]
        DPP2[design process prescription]
    end
    
    subgraph "Lifecycle Stage Layer"
        DUM[design use and maintenance process<br/><i>gdpo:GDPO0000039</i>]
        DEL[design end-of-life handling process<br/><i>gdpo:GDPO0000040</i>]
    end
    
    PEF -->|has prescription component| DPP1
    PEF -->|has prescription component| DPP2
    DPP1 -->|applies during lifecycle stage<br/><i>gdpo:GDPO0000063</i>| DUM
    DPP2 -->|applies during lifecycle stage<br/><i>gdpo:GDPO0000063</i>| DEL
    
    style PEF fill:#e1f5fe
    style DPP1 fill:#fff3e0
    style DPP2 fill:#fff3e0
    style DUM fill:#f3e5f5
    style DEL fill:#f3e5f5
```

---

## CQ5: Which qualities or dispositions are linked to a specific design principle?

**Pattern:** Principle ←is about→ Quality/Disposition (via equivalent class)

```mermaid
graph LR
    subgraph "Principle Layer"
        PH[principle of honesty<br/><i>gdpo:GDPO0000025</i>]
        PU[principle of usefulness<br/><i>gdpo:GDPO0000021</i>]
        PA[principle of aesthetics<br/><i>gdpo:GDPO0000022</i>]
    end
    
    subgraph "Artifact Target Layer"
        DH[design honesty<br/><i>Disposition</i>]
        DU[design usefulness<br/><i>Function</i>]
        DAQ[design aesthetic quality<br/><i>Quality</i>]
    end
    
    PH -->|is about<br/><i>cco:ont00001808</i>| DH
    PU -->|is about<br/><i>cco:ont00001808</i>| DU
    PA -->|is about<br/><i>cco:ont00001808</i>| DAQ
    
    style PH fill:#e1f5fe
    style PU fill:#e1f5fe
    style PA fill:#e1f5fe
    style DH fill:#c8e6c9
    style DU fill:#c8e6c9
    style DAQ fill:#c8e6c9
```

---

## CQ6 & CQ7: What artifacts have been evaluated, and against which principles?

**Pattern:** Evaluation Record → Artifact + Principle

```mermaid
graph TB
    subgraph "Evaluation Record Layer"
        DE[design evaluation<br/><i>gdpo:GDPO0000044</i>]
    end
    
    subgraph "Artifact Layer"
        ME[material entity<br/><i>e.g., Braun SK4</i>]
    end
    
    subgraph "Principle Layer"
        DP[design principle<br/><i>e.g., principle of minimalism</i>]
    end
    
    DE -->|is about evaluated artifact<br/><i>gdpo:GDPO0000045</i>| ME
    DE -->|against principle<br/><i>gdpo:GDPO0000046</i>| DP
    
    style DE fill:#fff3e0
    style ME fill:#ffcdd2
    style DP fill:#e1f5fe
```

---

## CQ8 & CQ9 & CQ10: Evaluation details (method, score, date)

**Pattern:** Evaluation Record with Method, Score, and Timestamp

```mermaid
graph TB
    subgraph "Evaluation Record"
        DE[design evaluation<br/><i>gdpo:GDPO0000044</i>]
    end
    
    subgraph "Evaluation Metadata"
        EMS[evaluation method specification<br/><i>gdpo:GDPO0000052</i>]
        SC["score<br/><i>xsd:decimal</i>"]
        DT["assessed on<br/><i>xsd:dateTime</i>"]
    end
    
    subgraph "Targets"
        ME[material entity]
        DP[design principle]
    end
    
    DE -->|is about using method<br/><i>gdpo:GDPO0000048</i>| EMS
    DE -->|has score<br/><i>gdpo:GDPO0000047</i>| SC
    DE -->|assessed on<br/><i>gdpo:GDPO0000050</i>| DT
    DE -->|is about evaluated artifact| ME
    DE -->|against principle| DP
    
    style DE fill:#fff3e0
    style EMS fill:#e8eaf6
    style SC fill:#f5f5f5
    style DT fill:#f5f5f5
    style ME fill:#ffcdd2
    style DP fill:#e1f5fe
```

---

## CQ11 & CQ12: Evaluation method prescribes process, operationalizes principle

**Pattern:** Method ↔ Process ↔ Principle

```mermaid
graph LR
    subgraph "Method Layer"
        EMS[evaluation method specification<br/><i>gdpo:GDPO0000052</i>]
    end
    
    subgraph "Process Layer"
        DEP[design evaluation process<br/><i>gdpo:GDPO0000055</i>]
    end
    
    subgraph "Principle Layer"
        DP[design principle<br/><i>gdpo:GDPO0000003</i>]
    end
    
    EMS -->|prescribes<br/><i>cco:ont00001942</i>| DEP
    EMS -->|operationalizes principle<br/><i>gdpo:GDPO0000054</i>| DP
    
    style EMS fill:#e8eaf6
    style DEP fill:#f3e5f5
    style DP fill:#e1f5fe
```

---

## CQ15: Which qualities inhere in a given artifact?

**Pattern:** Quality → inheres in → Material Entity

```mermaid
graph RL
    subgraph "Artifact Layer"
        ME[material entity<br/><i>e.g., iPhone 14</i>]
    end
    
    subgraph "Quality Layer"
        DAQ[design aesthetic quality<br/><i>gdpo:GDPO0000006</i>]
        DMQ[design minimalism quality<br/><i>gdpo:GDPO0000013</i>]
        DTQ[design thoroughness quality<br/><i>gdpo:GDPO0000011</i>]
    end
    
    DAQ -->|inheres in<br/><i>bfo:BFO_0000197</i>| ME
    DMQ -->|inheres in<br/><i>bfo:BFO_0000197</i>| ME
    DTQ -->|inheres in<br/><i>bfo:BFO_0000197</i>| ME
    
    style ME fill:#ffcdd2
    style DAQ fill:#c8e6c9
    style DMQ fill:#c8e6c9
    style DTQ fill:#c8e6c9
```

---

## CQ16: Which dispositions are realized in which processes?

**Pattern:** Disposition → realized in → Process

```mermaid
graph LR
    subgraph "Artifact Layer"
        ME[material entity]
    end
    
    subgraph "Disposition Layer"
        DH[design honesty<br/><i>gdpo:GDPO0000009</i>]
        DU[design understandability<br/><i>gdpo:GDPO0000007</i>]
        DD[design durability<br/><i>gdpo:GDPO0000010</i>]
    end
    
    subgraph "Process Layer"
        DIP[design interaction process<br/><i>gdpo:GDPO0000017</i>]
        DCP[design comprehension process<br/><i>gdpo:GDPO0000016</i>]
        DEP[design endurance process<br/><i>gdpo:GDPO0000018</i>]
    end
    
    DH -->|inheres in| ME
    DU -->|inheres in| ME
    DD -->|inheres in| ME
    
    DH -->|realized in<br/><i>bfo:BFO_0000054</i>| DIP
    DU -->|realized in<br/><i>bfo:BFO_0000054</i>| DCP
    DD -->|realized in<br/><i>bfo:BFO_0000054</i>| DEP
    
    style ME fill:#ffcdd2
    style DH fill:#c8e6c9
    style DU fill:#c8e6c9
    style DD fill:#c8e6c9
    style DIP fill:#f3e5f5
    style DCP fill:#f3e5f5
    style DEP fill:#f3e5f5
```

---

## CQ17: Which aspects of honesty does an artifact exhibit?

**Pattern:** Honesty Facets with Basis and Realization

```mermaid
graph TB
    subgraph "Artifact Layer"
        ME[material entity]
    end
    
    subgraph "Honesty Disposition Layer"
        DH[design honesty<br/><i>gdpo:GDPO0000009</i>]
        DMH[design material honesty<br/><i>gdpo:GDPO0000041</i>]
        DFH[design functional honesty<br/><i>gdpo:GDPO0000042</i>]
    end
    
    subgraph "Basis Layer"
        MHB[design material honesty basis<br/><i>gdpo:GDPO0000057</i>]
        FHB[design functional honesty basis<br/><i>gdpo:GDPO0000058</i>]
    end
    
    subgraph "Evaluation Layer"
        DCHE[design communicative<br/>honesty evaluation<br/><i>gdpo:GDPO0000452</i>]
        DCCE[design communication<br/>content entity<br/><i>gdpo:GDPO0000446</i>]
    end
    
    DMH -->|rdfs:subClassOf| DH
    DFH -->|rdfs:subClassOf| DH
    
    DMH -->|inheres in| ME
    DFH -->|inheres in| ME
    
    DMH -->|has basis<br/><i>bfo:BFO_0000218</i>| MHB
    DFH -->|has basis<br/><i>bfo:BFO_0000218</i>| FHB
    
    MHB -->|continuant part of| ME
    FHB -->|continuant part of| ME
    
    DCHE -->|is about evaluated artifact| ME
    DCHE -->|is about communication content<br/><i>gdpo:GDPO0000450</i>| DCCE
    
    style ME fill:#ffcdd2
    style DH fill:#c8e6c9
    style DMH fill:#c8e6c9
    style DFH fill:#c8e6c9
    style MHB fill:#ffe0b2
    style FHB fill:#ffe0b2
    style DCHE fill:#fff3e0
    style DCCE fill:#e8eaf6
```

---

## CQ18: Which principles are part of the Rams ten principles specification?

**Pattern:** Specification → has principle component → Principle Statements

```mermaid
graph TB
    subgraph "Specification Layer"
        RTS[rams ten principles specification 001<br/><i>gdpo:GDPO0000065</i>]
    end
    
    subgraph "Principle Statement Individuals"
        P1[principle of innovativeness 001<br/><i>gdpo:GDPO0000066</i>]
        P2[principle of usefulness 001<br/><i>gdpo:GDPO0000067</i>]
        P3[principle of aesthetics 001<br/><i>gdpo:GDPO0000068</i>]
        P4[principle of understandability 001<br/><i>gdpo:GDPO0000069</i>]
        P5[principle of unobtrusiveness 001<br/><i>gdpo:GDPO0000070</i>]
        P6[principle of honesty 001<br/><i>gdpo:GDPO0000071</i>]
        P7[principle of durability 001<br/><i>gdpo:GDPO0000072</i>]
        P8[principle of thoroughness 001<br/><i>gdpo:GDPO0000073</i>]
        P9[principle of env. friendliness 001<br/><i>gdpo:GDPO0000074</i>]
        P10[principle of minimalism 001<br/><i>gdpo:GDPO0000075</i>]
    end
    
    RTS -->|has principle component<br/><i>gdpo:GDPO0000060</i>| P1
    RTS -->|has principle component| P2
    RTS -->|has principle component| P3
    RTS -->|has principle component| P4
    RTS -->|has principle component| P5
    RTS -->|has principle component| P6
    RTS -->|has principle component| P7
    RTS -->|has principle component| P8
    RTS -->|has principle component| P9
    RTS -->|has principle component| P10
    
    style RTS fill:#bbdefb
    style P1 fill:#e1f5fe
    style P2 fill:#e1f5fe
    style P3 fill:#e1f5fe
    style P4 fill:#e1f5fe
    style P5 fill:#e1f5fe
    style P6 fill:#e1f5fe
    style P7 fill:#e1f5fe
    style P8 fill:#e1f5fe
    style P9 fill:#e1f5fe
    style P10 fill:#e1f5fe
```

---

## CQ19: How does the ontology distinguish qualities from principles?

**Pattern:** Principle (Directive ICE) ↔ Quality/Disposition/Function (BFO Continuant)

```mermaid
graph TB
    subgraph "BFO Upper Ontology"
        SDC[specifically dependent continuant<br/><i>bfo:BFO_0000020</i>]
        ICE[information content entity<br/><i>cco:ont00000958</i>]
    end
    
    subgraph "Artifact-Side Targets<br/>(What IS the case)"
        Q[quality<br/><i>bfo:BFO_0000019</i>]
        D[disposition<br/><i>bfo:BFO_0000016</i>]
        F[function<br/><i>bfo:BFO_0000034</i>]
        DAQ[design aesthetic quality]
        DH[design honesty]
        DU[design usefulness]
    end
    
    subgraph "Principle Layer<br/>(What SHOULD be the case)"
        DICE[directive ICE<br/><i>cco:ont00000965</i>]
        DP[design principle<br/><i>gdpo:GDPO0000003</i>]
        PA[principle of aesthetics]
        PH[principle of honesty]
        PU[principle of usefulness]
    end
    
    SDC --> Q
    SDC --> D
    D --> F
    ICE --> DICE
    DICE --> DP
    
    Q --> DAQ
    D --> DH
    F --> DU
    DP --> PA
    DP --> PH
    DP --> PU
    
    PA -.->|is about| DAQ
    PH -.->|is about| DH
    PU -.->|is about| DU
    
    style SDC fill:#f5f5f5
    style ICE fill:#f5f5f5
    style Q fill:#c8e6c9
    style D fill:#c8e6c9
    style F fill:#c8e6c9
    style DICE fill:#e1f5fe
    style DP fill:#e1f5fe
    style DAQ fill:#c8e6c9
    style DH fill:#c8e6c9
    style DU fill:#c8e6c9
    style PA fill:#e1f5fe
    style PH fill:#e1f5fe
    style PU fill:#e1f5fe
```

---

## CQ20: Which agents carried out a design evaluation process?

**Pattern:** Process → has participant → Agent; Process → has output → Evaluation Record

```mermaid
graph TB
    subgraph "Agent Layer"
        AG[agent<br/><i>cco:ont00001017</i>]
    end
    
    subgraph "Process Layer"
        DEP[design evaluation process<br/><i>gdpo:GDPO0000055</i>]
    end
    
    subgraph "Record Layer"
        DE[design evaluation<br/><i>gdpo:GDPO0000044</i>]
    end
    
    subgraph "Targets"
        ME[material entity]
        DP[design principle]
    end
    
    DEP -->|evaluation carried out by<br/><i>gdpo:GDPO0000051</i>| AG
    DEP -->|has output| DE
    DE -->|is about evaluated artifact| ME
    DE -->|against principle| DP
    
    style AG fill:#ffe0b2
    style DEP fill:#f3e5f5
    style DE fill:#fff3e0
    style ME fill:#ffcdd2
    style DP fill:#e1f5fe
```

---

## Legend

| Color | Meaning |
|-------|---------|
| 🔵 Light Blue | Directive ICE / Principle |
| 🟢 Light Green | Quality / Disposition / Function |
| 🟣 Light Purple | Process |
| 🟠 Light Orange | Basis / Agent |
| 🟡 Cream | Evaluation / Method |
| 🔴 Light Red | Material Entity (Artifact) |

---

## Complete Architecture Overview

```mermaid
graph TB
    subgraph "Normative Layer<br/>(Directive ICEs)"
        RTS[Rams Ten Principles Specification]
        DP[Design Principles<br/><i>10 classes + 10 individuals</i>]
        DPP[Design Process Prescriptions]
        EMS[Evaluation Method Specifications]
    end
    
    subgraph "Descriptive Layer<br/>(BFO Continuants)"
        ME[Material Entity<br/><i>Designed Artifact</i>]
        QDF[Qualities, Dispositions, Functions<br/><i>inhering in artifact</i>]
        HB[Honesty Bases<br/><i>structural grounds</i>]
    end
    
    subgraph "Process Layer<br/>(BFO Occurrents)"
        LSP[Lifecycle Stage Processes<br/><i>sourcing, manufacturing,<br/>distribution, use, end-of-life</i>]
        DEsP[Design Evaluation Process]
    end
    
    subgraph "Record Layer<br/>(ICEs)"
        DE[Design Evaluations<br/><i>with scores, dates, methods</i>]
        DCCE[Communication Content<br/><i>manuals, labels, ads</i>]
    end
    
    RTS -->|has principle component| DP
    DP -->|has prescription component| DPP
    DP -->|is about| QDF
    DPP -->|prescribes| LSP
    DPP -->|applies during lifecycle stage| LSP
    
    QDF -->|inheres in| ME
    HB -->|continuant part of| ME
    QDF -->|has basis| HB
    QDF -->|realized in| LSP
    
    EMS -->|prescribes| DEsP
    EMS -->|operationalizes principle| DP
    DEsP -->|has output| DE
    DEsP -->|has participant| ME
    
    DE -->|is about evaluated artifact| ME
    DE -->|against principle| DP
    DE -->|is about using method| EMS
    DE -->|is about communication content| DCCE
    
    style RTS fill:#bbdefb
    style DP fill:#e1f5fe
    style DPP fill:#e1f5fe
    style EMS fill:#e8eaf6
    style ME fill:#ffcdd2
    style QDF fill:#c8e6c9
    style HB fill:#ffe0b2
    style LSP fill:#f3e5f5
    style DEsP fill:#f3e5f5
    style DE fill:#fff3e0
    style DCCE fill:#e8eaf6
```
