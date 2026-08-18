# cc-sdd (Spec-Driven Development)

**Repository:** [github.com/gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)
**License:** MIT

## Overview

cc-sdd brings structured Spec-Driven Development to AI coding agents. It turns approved specs into long-running autonomous implementation with per-task independent review, TDD, and auto-debug. Works across 8 AI coding agents with the same 17-skill set.

**"Turn approved specs into long-running autonomous implementation"**

## Key Features

- **17 Agent Skills:** Discovery, requirements, design, tasks, autonomous implementation
- **8 AI Coding Agents:** Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, Antigravity
- **13 Languages:** Multi-language support
- **Per-Task Subagent Spawn:** Fresh implementer for each task
- **Independent Review:** Reviewer subagent for each task
- **Auto-Debug:** Root-cause investigation on failure
- **TDD:** RED → GREEN behind feature flags
- **Boundary-First Spec Discipline:** File Structure Plan drives task boundaries

## Workflow

```
/kiro-discovery <idea>
  → brief.md (and roadmap.md for multi-spec)
/kiro-spec-init <feature>
/kiro-spec-requirements <feature>
/kiro-spec-design <feature>
/kiro-spec-tasks <feature>
/kiro-impl <feature>
  → Per-task: fresh implementer + independent reviewer + auto-debug
```

## Skills Included

| Skill | Description |
|-------|-------------|
| `/kiro-discovery` | Route new work, write brief.md |
| `/kiro-spec-init` | Initialize a new spec |
| `/kiro-spec-requirements` | Write EARS-format requirements |
| `/kiro-spec-design` | Architecture with Mermaid diagrams |
| `/kiro-spec-tasks` | Generate task checklist |
| `/kiro-impl` | Autonomous implementation |
| `/kiro-validate-gap` | Gap analysis for existing codebase |
| `/kiro-validate-design` | Design review |
| `/kiro-validate-impl` | Implementation validation |
| `/kiro-spec-status` | Check progress |
| `/kiro-spec-batch` | Multi-spec initiatives |
| `/kiro-steering` | Project-wide rules |

## Installation

```bash
cd your-project
npx cc-sdd@latest
```

## Usage

```bash
# Start discovery
/kiro-discovery Photo albums with upload, tagging, and sharing

# Create spec
/kiro-spec-init photo-albums

# Write requirements
/kiro-spec-requirements photo-albums

# Design architecture
/kiro-spec-design photo-albums

# Generate tasks
/kiro-spec-tasks photo-albums

# Implement autonomously
/kiro-impl photo-albums
```

## Relevance to Our Project

**Very high relevance** — This is the gold standard for spec-driven autonomous implementation. Key takeaways:
- Spec as contract between system parts
- Per-task subagent with fresh context
- Independent review for quality
- Auto-debug on failure
- Works with OpenCode

## Pros & Cons

| Pros | Cons |
|------|------|
| Production-ready | Requires spec discipline |
| Works with 8 agents | Complex workflow |
| Independent review | Learning curve |
| Auto-debug | Large skill set |

## Running This Repo

```bash
cd cloned-repos/cc-sdd
npm install
npx cc-sdd@latest --opencode-skills
# Then in OpenCode: /kiro-discovery <your-idea>
```
