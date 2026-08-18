#!/usr/bin/env python3
"""Generate architecture pattern diagrams as SVGs."""

from mermaid import Mermaid
from pathlib import Path

DIAGRAMS_DIR = Path("docs/diagrams")
DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)

diagrams = {
    "architecture_diagram_1": """graph TD
    O[Orchestrator LLM Router] --> W1[Worker Backend Dev]
    O --> W2[Worker Frontend Dev]
    O --> W3[Worker Test Writer]""",
    
    "architecture_diagram_2": """graph LR
    P[Plan Agent] --> C[Code Agent]
    C --> R[Review Agent]
    R --> D[Deploy Agent]""",
    
    "architecture_diagram_3": """graph TD
    FO[Fan-Out Splitter] --> W1[Worker 1 Test A]
    FO --> W2[Worker 2 Test B]
    FO --> W3[Worker 3 Test C]
    W1 --> FI[Fan-In Merger]
    W2 --> FI
    W3 --> FI""",
    
    "architecture_diagram_4": """graph TD
    PQ[Priority Queue P1-P5] --> E[Executor LLM Agent]
    E --> RH[Result Handler]
    RH -->|Success| D[Done]
    RH -->|Failure| PQ""",
    
    "architecture_diagram_5": """graph TD
    E[Execute Task] --> A[Analyze Results]
    A --> I[Improve Self]
    I --> E""",
    
    "architecture_diagram_6": """graph TD
    S[Spec Doc Requirements] --> P[Planner Task Breakdown]
    P --> I[Implementer Code Generation]
    I --> V[Verifier Spec Compliance]
    V -->|Pass| PASS[Done]
    V -->|Fail| I"""
}

for name, code in diagrams.items():
    try:
        m = Mermaid(code)
        svg = m.svg_response.text
        output_file = DIAGRAMS_DIR / f"{name}.svg"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(svg)
        print(f"OK: {name}.svg")
    except Exception as e:
        print(f"FAIL: {name} - {e}")
