# OpenCode Pipeline Template

**Repository:** [github.com/jiyuan0125/opencode-pipeline-template](https://github.com/jiyuan0125/opencode-pipeline-template)

## Overview

Build production-grade LLM code generation pipelines using OpenCode's native skill + subagent + command system. No custom agent framework required — just OpenCode and your deterministic scripts.

## Key Features

- **Three-Layer Separation:** Skill (methodology), Subagent (sandbox), Command (trigger)
- **11 Methodology Templates:** Pipeline master, test fix, fusion, build, behavior fix, and more
- **10 Sandboxed Agents:** Each with path-level permission rules
- **3 User Commands:** `/fix-tests`, `/fuse-module`, `/build-module`
- **Deterministic Scripts:** Bash scripts for AST, validation, CI pipeline logic

## Architecture

```
User types /fix-tests my-module
  → Command routes to pipeline-test-fix subagent
    → Subagent loads pipeline-test-fix skill (methodology)
      → Subagent runs pytest, reads failures, fixes code
        → Permission sandbox enforces file boundaries
          → Result returned to user
```

## Three-Layer Separation

| Layer | Location | Purpose |
|-------|----------|---------|
| **Skill** | `.opencode/skills/<name>/SKILL.md` | Methodology (what to do, how to diagnose) |
| **Subagent** | `.opencode/agent/<name>.md` | Permission sandbox + model config |
| **Command** | `.opencode/command/<name>.md` | User-facing trigger |

## Skills Included

| Skill | Description |
|-------|-------------|
| `pipeline-master` | Orchestrator: chains stages in order |
| `pipeline-test-fix` | Diagnose pytest failures, fix code, verify |
| `pipeline-fusion` | Read reference code, generate business logic |
| `pipeline-build` | Enhance CRUD skeleton with validation guards |
| `pipeline-behavior-fix` | Compare against reference, patch missing logic |
| `pipeline-fe-infra` | Generate Vue3+Element-Plus admin scaffolding |
| `pipeline-fe-page` | Fill empty Vue templates with data tables |
| `pipeline-fe-ir` | Compile business rules into structured test IR |
| `pipeline-rule-extract` | Extract common business rules |
| `pipeline-rule-convert` | Add testable acceptance criteria |
| `pipeline-rule-review` | Check rules for duplicates, contradictions |

## Installation

```bash
git clone https://github.com/jiyuan0125/opencode-pipeline-template.git
cd opencode-pipeline-template/examples
```

## Usage

```bash
# Step 1: Generate CRUD skeleton (deterministic)
python scaffold.py user

# Step 2: Run CRUD tests (should pass)
python -m pytest tests/test_user.py::TestCRUD -q

# Step 3: Open opencode, then type:
#   /fuse-module user
```

## Relevance to Our Project

**Very high relevance** — This shows how to build pipelines with OpenCode's native primitives. Key takeaways:
- Three-layer separation pattern
- Permission sandboxing for subagents
- Deterministic + LLM hybrid approach
- Production-ready pipeline patterns

## Pros & Cons

| Pros | Cons |
|------|------|
| Uses OpenCode natively | Requires OpenCode |
| Clean separation of concerns | Focused on Python/Vue |
| Permission sandboxing | Limited to specific use cases |
| Production-ready patterns | Smaller community |

## Running This Repo

```bash
cd cloned-repos/opencode-pipeline-template/examples
python scaffold.py user
python -m pytest tests/test_user.py::TestCRUD -q
# Then use OpenCode: /fuse-module user
```
