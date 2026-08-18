#!/usr/bin/env python3
"""Generate vision diagram as SVG."""

from mermaid import Mermaid
from pathlib import Path

DIAGRAMS_DIR = Path("docs/diagrams")
DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)

code = """graph TD
    H[Human User Inputs Goal] --> P[Planner Agent LLM]
    P --> C[Coding Agent Backend]
    P --> R[Reviewer Agent Quality]
    P --> D[Doc Writer Docs]
    C --> Dashboard[Progress Dashboard Real-time]
    R --> Dashboard
    D --> Dashboard
    Dashboard --> PA[Permission Auto-Accept]"""

try:
    m = Mermaid(code)
    svg = m.svg_response.text
    output_file = DIAGRAMS_DIR / "vision_diagram_1.svg"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"OK: vision_diagram_1.svg")
except Exception as e:
    print(f"FAIL: vision_diagram_1 - {e}")
