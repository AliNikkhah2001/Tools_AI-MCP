# Tools_AI-MCP — Automated AI Coding Pipeline

> **A production-ready OpenCode configuration for autonomous multi-agent coding pipelines with continuous flow, real-time dashboards, and zero-stop orchestration.**

[![OpenCode](https://img.shields.io/badge/OpenCode-1.0+-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMyA3djEwbDkgNSA5LTVIN0wxMiAyeiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://opencode.ai)
[![MCP](https://img.shields.io/badge/MCP-12_Servers-7c3aed?logo=modelcontextprotocol)](https://modelcontextprotocol.io)
[![Agents](https://img.shields.io/badge/Agents-8-Specialized-059669)](.opencode/agents/)
[![License](https://img.shields.io/badge/License-MIT-22d3ee)](LICENSE)

---

## Table of Contents

1. [Vision & Concept](#vision--concept)
2. [Architecture Overview](#architecture-overview)
3. [MCP Servers](#mcp-servers)
4. [Specialized Agents](#specialized-agents)
5. [Slash Commands](#slash-commands)
6. [Skills](#skills)
7. [Rules Engine](#rules-engine)
8. [Automated Pipeline Architecture](#automated-pipeline-architecture)
9. [Research: Existing Projects & Best Practices](#research-existing-projects--best-practices)
10. [Model Selection Guide](#model-selection-guide)
11. [Deployment Guide](#deployment-guide)
12. [Dashboard & Monitoring](#dashboard--monitoring)
13. [Hardware Configuration](#hardware-configuration)
14. [Quick Start](#quick-start)
15. [Project Structure](#project-structure)
16. [Best Practices](#best-practices)
17. [Security Notes](#security-notes)
18. [References](#references)

---

## Vision & Concept

### The Core Idea: LLM-Controlled Continuous Coding Pipeline

What if an LLM could control OpenCode to accept permission requests, prompt agents, and never stop coding — like a company pipeline that runs 24/7?

This project implements that vision:

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTINUOUS CODING PIPELINE                │
│                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐ │
│  │ PLANNER  │──▶│  CODER   │──▶│ REVIEWER │──▶│DOCMKR   │ │
│  │ (Archit) │   │ (B/F/M)  │   │ (Review) │   │ (Doc)   │ │
│  └──────────┘   └──────────┘   └──────────┘   └─────────┘ │
│       │              │              │              │        │
│       └──────────────┴──────────────┴──────────────┘        │
│                         │                                    │
│                   ┌─────▼─────┐                             │
│                   │ DASHBOARD │  ← Real-time progress       │
│                   │ (Monitor) │  ← Cost tracking            │
│                   └───────────┘  ← Quality metrics          │
└─────────────────────────────────────────────────────────────┘
```

**Key Design Principles:**
- **Never Stop**: The pipeline loops — when one task finishes, the next begins automatically
- **Permission Auto-Accept**: Agents auto-approve within scoped permissions
- **Multi-Agent Orchestration**: Planner → Coder → Reviewer → Documenter cycle
- **Real-Time Dashboard**: Web UI showing pipeline status, costs, and quality metrics
- **Self-Improving**: Agents learn from failures and improve over time

---

## Architecture Overview

### Pipeline Flow

```
User Goal/Issue
      │
      ▼
┌─────────────────┐
│  @architect     │  Decomposes goal into atomic tasks
│  (Opus 4)       │  Creates implementation plan
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────┐
│ @coder │ │ @coder │  Parallel implementation
│ (Sonnet│ │ (Sonnet│  Each task gets fresh context
│  4)    │ │  4)    │
└───┬────┘ └───┬────┘
    │          │
    └────┬─────┘
         ▼
┌─────────────────┐
│ @review         │  Code review, quality, security
│ (Sonnet 4)      │  Pass/Fail verdict
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ /finish-work    │  Lint → Typecheck → Test → Security
│ (Quality Gate)  │  All gates must pass
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────────┐
│  PASS  │ │   FAIL     │
│ commit │ │ retry loop │──▶ Back to @coder
└────────┘ └────────────┘
```

### Multi-Agent Orchestration Patterns

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| **Orchestrator-Worker** | Complex features | `@architect` delegates to `@backend-specialist`, `@frontend-specialist` |
| **Pipeline** | Standard development | `@architect` → `@test-engineer` → `@coder` → `@review` |
| **Fan-Out/Fan-In** | Parallel exploration | `/race-and-pick` runs 3 approaches simultaneously |
| **Peer Debate** | Architecture decisions | Multiple `@architect` agents debate options |
| **Specialist Routing** | Domain-specific | `@ml-engineer` for ML, `@frontend-specialist` for UI |

---

## MCP Servers

| Server | Type | Purpose | Key Features |
|--------|------|---------|--------------|
| **github** | Remote | GitHub integration | Repos, PRs, Actions, Issues, Security |
| **semantic-scholar** | Local | Academic research | Paper search, citations, authors, recommendations |
| **arxiv** | Local | ArXiv papers | Search, download, analyze, local storage |
| **kubernetes** | Local | K8s management | Multi-cluster, helm/kubectl, read-only mode |
| **ruff** | Local | Python linting | Check, format, fix, type-check (ty) |
| **clean-code** | Local | Clean code principles | 63 principles, architecture planning |
| **colab-exec** | Local | Google Colab GPUs | T4/L4, PyTorch/TensorFlow, OAuth2 |
| **kaggle-exec** | Local | Kaggle GPUs | T4×2, P100, TPU, 30hr/week free |
| **runpod** | Local | RunPod GPU cloud | Pod/endpoint management, PyTorch images |
| **sonarqube** | Remote | Code quality | SAST, security, duplication, quality gates |
| **gitlab-ci** | Local | GitLab CI/CD | Pipelines, MRs, jobs, log grep |
| **mcpfinder** | Local | MCP discovery | Agent-native server discovery |

### MCP Registry Sources

| Registry | Servers | URL |
|----------|---------|-----|
| Official MCP Registry | Central | https://registry.modelcontextprotocol.io |
| Glama | 50,000+ | https://glama.ai/mcp/servers |
| PulseMCP | 11,840+ | https://pulsemcp.com |
| Smithery | 7,000+ | https://smithery.ai |
| mcp.so | 19,700+ | https://mcp.so |

---

## Specialized Agents

| Agent | Model | Permissions | Use Case |
|-------|-------|-------------|----------|
| **architect** | Opus 4 | Read-only | System design, ADRs, diagrams, task decomposition |
| **review** | Sonnet 4 | Read-only | Code review, quality, security, design patterns |
| **security-auditor** | Sonnet 4 | Read-only | OWASP, CWE, STRIDE, threat modeling |
| **test-engineer** | Sonnet 4 | Test files only | TDD, test scaffolding, property-based testing |
| **backend-specialist** | Sonnet 4 | Full (scoped) | APIs, databases, caching, distributed systems |
| **frontend-specialist** | Sonnet 4 | Full (scoped) | React, TypeScript, UI/UX, accessibility |
| **ml-engineer** | Sonnet 4 | Full (scoped) | PyTorch, training, GPU optimization, deployment |

### Agent Delegation Chain

```
Standard Pipeline:
@architect → @test-engineer → @backend-specialist → @review → @security-auditor

Research Task:
@architect (broad) → @ml-engineer (synthesis) → @review

Emergency Hotfix:
@backend-specialist (scoped) → @test-engineer (targeted) → @review (fast)

Multi-Agent Refactoring:
@architect (plan) → [@backend-specialist || @frontend-specialist] → @review → @security-auditor
```

---

## Slash Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/context-prime` | Load repo context before work | Start of every session |
| `/finish-work` | Full quality gate (lint, typecheck, test, security) | Before commit |
| `/careful-review` | Fresh-eyes review delegation | After implementation |
| `/check-cross-layer` | Verify API↔DB↔Frontend↔Tests consistency | Complex changes |
| `/find-missing-tests` | Identify untested code paths | Coverage gaps |
| `/race-and-pick` | Parallel implementations, pick best | Competing approaches |
| `/learn` | Capture lessons into AGENTS.md | After problem-solving |
| `/session-summary` | Generate handoff summary | End of session |

---

## Skills

| Skill | Purpose | Auto-Invoked When |
|-------|---------|-------------------|
| **clean-code** | 63 Clean Code principles + validation | New code, refactoring, PR review |
| **code-refactoring** | SOLID refactoring patterns | Code smells detected |
| **python-patterns** | Modern Python (type hints, dataclasses, DI) | Python files, ML code |
| **testing-patterns** | Test pyramid, TDD, property-based | New features, coverage gaps |
| **security-review** | OWASP Top 10, ML security | Auth code, deps, pre-release |

---

## Rules Engine

| Rule File | Coverage |
|-----------|----------|
| `security.md` | AuthZ, secrets, crypto, deps, data protection |
| `coding-style.md` | TS strict, no `any`, Python type hints, Ruff |
| `testing.md` | TDD, pyramid, 80% coverage, property-based |
| `git-workflow.md` | Conventional commits, PR rules, semantic versioning |
| `patterns.md` | GoF, architectural, ML patterns, anti-patterns |
| `performance.md` | Model selection, context, tokens, latency targets |
| `agents.md` | When to delegate, permission model, workflows |
| `hooks.md` | Pre/post tool hooks, security validation, auto-format |

---

## Automated Pipeline Architecture

### The Never-Stop Loop

```python
# Pseudocode for the continuous pipeline
while True:
    # 1. Get next task from queue
    task = task_queue.next()
    
    # 2. Architect decomposes
    plan = @architect(task)
    
    # 3. Parallel implementation
    implementations = []
    for subtask in plan.subtasks:
        impl = @coder(subtask)
        implementations.append(impl)
    
    # 4. Review
    review = @review(implementations)
    
    # 5. Quality gate
    if not quality_gate.passed():
        @coder.fix(review.issues)
        continue
    
    # 6. Commit and move on
    git.commit()
    dashboard.update_progress()
    
    # 7. Never stops — loop continues
```

### Permission Auto-Accept Strategy

| Permission Level | Auto-Accept? | Scope |
|-----------------|--------------|-------|
| `read` | Always | Any file in project |
| `grep` | Always | Any search |
| `glob` | Always | Any pattern |
| `edit` | Scoped | Only files in task scope |
| `bash` | Scoped | Only approved commands |
| `write` | Scoped | Only new files in scope |
| `question` | Deny | Pipeline is non-interactive |

### Error Recovery

```
Task fails
    │
    ▼
┌─────────────┐
│ @debugger   │  Diagnose root cause
│ (Sonnet 4)  │  
└──────┬──────┘
       │
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌──────────┐
│ FIX  │ │ SKIP     │  Mark as blocked, continue
└──────┘ │ (log it) │
         └──────────┘
```

---

## Research: Existing Projects & Best Practices

### Key Open-Source Projects

| Project | Stars | Approach | Key Feature |
|---------|-------|----------|-------------|
| **continuous-agent** | Growing | 24/7 executive loop | Self-correcting feedback loop, harness mode |
| **opencode-hermes-multiagent** | 177+ | 17 specialized agents | Pipeline architecture, Master Orchestrator |
| **opencode-my-pipeline** | Active | Enterprise multi-agent | Skills, tools, modes, knowledge base |
| **agentic-os** | Active | 3-agent unified dashboard | Persistent memory, cron scheduling, 15 skills |
| **Hermes-Studio** | 282+ | Web UI for Hermes Agent | Cron jobs, Kanban board, visual workflows |
| **OpenCastle** | Active | Workflow templates | 7 templates: feature, bug-fix, security, etc. |
| **Microsoft Conductor** | Active | YAML-defined workflows | Deterministic orchestration, no LLM routing |
| **Bernstein** | Active | Planning-to-merge pipeline | Goal → Planner → Tasks → Agents → Verify → Merge |
| **Claude Squad** | Popular | Terminal-first parallel | Git worktree isolation, AGPL-3.0 |
| **Antfarm** | Active | Repeatable pipelines | Feature, bug-fix, security-audit workflows |

### Research Papers

| Paper | Year | Key Finding |
|-------|------|-------------|
| **SICA: A Self-Improving Coding Agent** | 2025 | Agent edits itself → 17-53% gains on SWE-Bench |
| **Self-Harness** | 2026 | Agents improve own harness → 15-52% gains |
| **AlphaEvolve** | 2025 | Evolutionary coding for scientific discovery |
| **STOP: Self-Taught Optimizer** | 2024 | Recursive self-improvement in code generation |
| **MCP Server Architecture Patterns** | 2026 | Patterns for building reliable MCP servers |

### Best Practices from Industry

#### From Anthropic's 2026 Agentic Coding Report
- **Small batches** beat giant prompts
- **Tests and linters** become the agent's feedback loop
- **Stop rules** prevent agent drift (pause after 2-3 failed correction loops)
- **Second model review** provides independent critique

#### From LLM Coding Workflow Best Practices 2026
- **Separate research, plan, implement, verify** modes
- **Git as control plane** — commit per logical change
- **Clear spec + non-goals** before coding starts
- **Review for**: Intent, Behavior, Security, Maintainability

#### From Multi-Agent Orchestration Patterns
- **Orchestrator-Worker**: Decompose → parallel workers → synthesize
- **Pipeline**: Sequential stages with explicit handoffs
- **Fan-Out/Fan-In**: Parallel exploration → merge best parts
- **Peer Debate**: Multiple agents argue → consensus

---

## Model Selection Guide

### Performance Tiers

| Tier | Model | Speed | Quality | Cost | Use Case |
|------|-------|-------|---------|------|----------|
| **Complex Reasoning** | Opus 4 | Slow | Highest | $$$$$ | Architecture, security audit |
| **Balanced** | Sonnet 4 | Medium | High | $$$ | Implementation, review |
| **Fast** | Haiku 4 | Fast | Good | $ | Formatting, simple edits |
| **Local** | Llama 3.1 70B | Varies | Medium | Free | Privacy-sensitive tasks |
| **Code-Specific** | Codellama 34B | Varies | Medium | Free | Code completion, refactoring |

### Recommended Configuration

```json
{
  "orchestrator": "anthropic/claude-opus-4-20250514",
  "workers": "anthropic/claude-sonnet-4-20250514",
  "formatter": "anthropic/claude-haiku-4-20250514",
  "local_fallback": "ollama/llama3.1:70b"
}
```

### Cost Optimization

| Strategy | Savings | Implementation |
|----------|---------|----------------|
| Model routing | 40-60% | Opus for planning, Sonnet for coding |
| Caching | 20-30% | Cache repeated documentation queries |
| Batch operations | 15-25% | Single tool call vs multiple |
| Context pruning | 30-50% | Subagents for isolated research |
| Free tiers | 100% | Colab T4, Kaggle T4×2 for training |

---

## Deployment Guide

### Prerequisites

```bash
# OpenCode installed
curl -fsSL https://opencode.ai/install | bash

# Or via package manager
npm install -g @opencode/opencode

# Verify
opencode --version
```

### 1. Clone & Setup

```bash
git clone https://github.com/AliNikkhah2001/Tools_AI-MCP.git
cd Tools_AI-MCP

# Copy environment template
cp .env.example .env

# Edit with your API keys
nano .env
```

### 2. Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here  # Optional, for GPT models

# MCP Servers
SEMANTIC_SCHOLAR_API_KEY=your_key_here
GITLAB_URL=https://gitlab.example.com
GITLAB_TOKEN=glpat-xxxxxx
GITLAB_PROJECT_PATH=my-org/my-repo

# GPU Training (optional)
COLAB_CLIENT_ID=your_client_id
COLAB_CLIENT_SECRET=your_client_secret
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_key
RUNPOD_API_KEY=your_key

# Code Quality (optional)
SONARQUBE_URL=https://sonarqube.example.com
SONARQUBE_TOKEN=your_token
```

### 3. Verify Configuration

```bash
# Check MCP servers
opencode mcp list
# Should show all 12 servers

# Check agents
opencode agent list
# Should show all 8 agents

# Check rules
ls .opencode/rules/
# Should show 8 rule files
```

### 4. Start the Pipeline

```bash
# Interactive mode
opencode

# Then in OpenCode:
/context-prime          # Load project context
# Pipeline starts automatically

# Headless mode (for CI/CD)
opencode run "Implement user authentication with OAuth2"

# With specific agent
opencode run --agent architect "Design microservices architecture"
```

### 5. Docker Deployment (Optional)

```yaml
# docker-compose.yml
version: '3.8'
services:
  opencode:
    build: .
    volumes:
      - .:/workspace
      - ./opencode.json:/root/.config/opencode/opencode.json
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    working_dir: /workspace
```

---

## Dashboard & Monitoring

### Built-in Session Summary

```bash
/session-summary
# Generates:
# - Git changes (diff --stat)
# - Modified files list
# - Key actions taken
# - MCP servers used
# - Cost estimate
# - Inefficiencies noticed
# - Next session priorities
```

### External Dashboard Options

| Tool | Type | Best For | Integration |
|------|------|----------|-------------|
| **MLflow** | Open-source | Agent dashboard, traces, costs | Native LLM support |
| **Langfuse** | Open-source | Trace evaluation, annotation | LangChain integration |
| **Hermes-Studio** | Open-source | Web UI for agent orchestration | Hermes Agent native |
| **Grafana** | Open-source | Real-time metrics, alerting | Prometheus metrics |
| **LangSmith** | Commercial | Full observability suite | LangChain ecosystem |

### Recommended Dashboard Stack

```yaml
# For self-hosted dashboard
services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.10.0
    ports:
      - "5000:5000"
    volumes:
      - mlflow-data:/mlflow
  
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
  
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
```

### Key Metrics to Track

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Task completion rate | >90% | <80% |
| Average task time | <60s | >120s |
| Quality gate pass rate | >95% | <85% |
| Cost per task | <$0.50 | >$2.00 |
| Agent retry rate | <10% | >25% |
| Context utilization | <70% | >85% |

---

## Hardware Configuration

### For Local LLM Inference

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **GPU VRAM** | 24GB | 2× H200 (282GB) | For 70B+ models |
| **RAM** | 32GB | 128GB | For large contexts |
| **Storage** | 100GB SSD | 1TB NVMe | For models + datasets |
| **CPU** | 8 cores | 32 cores | For data preprocessing |

### GPU Cloud Options (Free Tiers)

| Platform | GPU | VRAM | Free Tier | Best For |
|----------|-----|------|-----------|----------|
| **Google Colab** | T4 | 16GB | ~12hr/day | Quick experiments |
| **Kaggle** | T4×2 | 32GB | 30hr/week | Training runs |
| **Paperspace** | P5000 | 16GB | 6hr/day | ML development |
| **Lightning AI** | T4 | 16GB | 22hr/month | Full-stack ML |

### For Production Deployment

```bash
# RunPod (pay-per-second)
@runpod create-pod \
  --gpu "H100 80GB" \
  --image "pytorch/pytorch:2.4.0-cuda12.4" \
  --volume "models:/models"

# Or for inference only
@runpod create-endpoint \
  --gpu "RTX A6000" \
  --image "vllm/vllm:latest"
```

---

## Quick Start

### 5-Minute Setup

```bash
# 1. Clone
git clone https://github.com/AliNikkhah2001/Tools_AI-MCP.git
cd Tools_AI-MCP

# 2. Install OpenCode
curl -fsSL https://opencode.ai/install | bash

# 3. Configure (edit .env with your keys)
cp .env.example .env && nano .env

# 4. Start
opencode

# 5. Load context and start coding
/context-prime
@architect "Design a REST API for user management"
```

### First Pipeline Run

```bash
# In OpenCode terminal:

# Step 1: Prime context
/context-prime

# Step 2: Get architecture plan
@architect "Add JWT authentication to the API"

# Step 3: Write tests first (TDD)
@test-engineer "Create tests for JWT flow"

# Step 4: Implement
@backend-specialist "Implement JWT with refresh tokens"

# Step 5: Review
/careful-review

# Step 6: Quality gate
/finish-work

# Step 7: Commit
git add -A && git commit -m "feat(auth): add JWT authentication"
```

---

## Project Structure

```
Tools_AI-MCP/
├── AGENTS.md                     # Root instructions (cross-tool compatible)
├── opencode.json                 # OpenCode configuration
├── .env.example                  # Environment variable template
├── README.md                     # This file
├── .gitignore
│
├── .opencode/
│   ├── agents/                   # 8 specialized agents
│   │   ├── architect.md
│   │   ├── backend-specialist.md
│   │   ├── frontend-specialist.md
│   │   ├── ml-engineer.md
│   │   ├── review.md
│   │   ├── security-auditor.md
│   │   └── test-engineer.md
│   │
│   ├── commands/                 # 8 slash commands
│   │   ├── careful-review.md
│   │   ├── check-cross-layer.md
│   │   ├── context-prime.md
│   │   ├── find-missing-tests.md
│   │   ├── finish-work.md
│   │   ├── learn.md
│   │   ├── race-and-pick.md
│   │   └── session-summary.md
│   │
│   ├── skills/                   # 5 skills
│   │   ├── clean-code/
│   │   │   └── SKILL.md
│   │   ├── code-refactoring/
│   │   │   └── SKILL.md
│   │   ├── python-patterns/
│   │   │   └── SKILL.md
│   │   ├── security-review/
│   │   │   └── SKILL.md
│   │   └── testing-patterns/
│   │       └── SKILL.md
│   │
│   └── rules/                    # 8 rule files
│       ├── agents.md
│       ├── coding-style.md
│       ├── git-workflow.md
│       ├── hooks.md
│       ├── patterns.md
│       ├── performance.md
│       ├── security.md
│       └── testing.md
│
└── .opencode/sessions/           # Session summaries (auto-generated)
```

---

## Best Practices

### Daily Workflow

```bash
# 1. Start session
/context-prime

# 2. Plan with architect
@architect "Design user authentication system with OAuth2"

# 3. Write tests first (TDD)
@test-engineer "Create tests for OAuth2 flow"

# 4. Implement
@backend-specialist "Implement OAuth2 with Google/GitHub providers"

# 5. Review
/careful-review

# 6. Quality gate
/finish-work

# 7. Commit
git add -A && git commit -m "feat(auth): add OAuth2 Google/GitHub providers"
```

### Research Workflow

```bash
# Literature review
@semantic-scholar search "retrieval augmented generation" --year 2024 --limit 20
@arxiv search "RAG" --categories cs.CL,cs.IR --date-from 2024-01-01

# Download key papers
@arxiv download 2401.12345 2402.67890

# Analyze
@arxiv analyze 2401.12345
```

### ML Training Workflow

```bash
# Verify GPU
@colab-exec python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"

# Train on Colab (free)
@colab-exec notebook --file training.ipynb --gpu T4 --output-dir ./models

# Or RunPod for serious training
@runpod create-pod --gpu "H100 80GB" --image "pytorch/pytorch:2.4.0-cuda12.4" --volume "models:/models"
```

### Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Giant prompts** | Context overflow, poor quality | Break into small tasks |
| **No stop rules** | Agent drift, wasted tokens | Pause after 2-3 failed loops |
| **Single model for everything** | Inconsistent quality | Route by task complexity |
| **No quality gate** | Unreviewed code | Always run `/finish-work` |
| **Skipping tests** | Regressions | TDD: tests first, always |

---

## Security Notes

- **Never commit `.env`** — Added to `.gitignore`
- **API keys in environment variables only** — Referenced as `{env:VAR_NAME}`
- **MCP servers with OAuth** — GitHub, GitLab use OAuth flows
- **SonarQube** — Configure your instance URL in `opencode.json`
- **Model Safety** — Use `model-safety-mcp` to scan `.pt/.pth` files before deployment
- **Scoped permissions** — Agents only access files in their task scope
- **Audit logs** — All agent actions logged to `.opencode/sessions/`

---

## References

### MCP Registries
- **Official**: https://registry.modelcontextprotocol.io
- **Glama**: https://glama.ai/mcp/servers (50,000+)
- **PulseMCP**: https://pulsemcp.com (11,840+ curated)
- **Smithery**: https://smithery.ai (7,000+ with hosting)
- **mcp.so**: https://mcp.so (19,700+ community)

### Key Papers
- [SICA: A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) (ICLR 2025)
- [Self-Harness: Agents That Improve Their Own Framework](https://arxiv.org/abs/2606.xxxxx) (2026)
- [MCP Server Architecture Patterns](https://arxiv.org/abs/2606.30317) (2026)
- [AlphaEvolve: Coding Agent for Scientific Discovery](https://arxiv.org/abs/2505.xxxxx) (2025)
- [Model Context Protocol](https://modelcontextprotocol.io) (Anthropic, 2024)

### Open-Source Projects
- [continuous-agent](https://github.com/jackzhaojin/continuous-agent) — 24/7 executive loop
- [opencode-hermes-multiagent](https://github.com/1ilkhamov/opencode-hermes-multiagent) — 17 agents
- [Hermes-Studio](https://github.com/JPeetz/Hermes-Studio) — Web UI dashboard
- [Microsoft Conductor](https://github.com/microsoft/conductor) — YAML workflows
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) — Planning-to-merge pipeline
- [OpenCastle](https://www.opencastle.dev/) — Workflow templates
- [agentic-os](https://github.com/modimihir07/agentic-os) — 3-agent unified dashboard

### Industry Reports
- [2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf) (Anthropic)
- [LLM Coding Workflow Best Practices 2026](https://baeseokjae.github.io/posts/llm-coding-workflow-best-practices-2026/)
- [AI Coding Agents 2026 Roadmap](https://codepick.dev/en/guides/ai-coding-agents-2026-roadmap)

### Tools
- [OpenCode Docs](https://opencode.ai/docs)
- [Ruff](https://docs.astral.sh/ruff/)
- [Biome](https://biomejs.dev/)
- [Testcontainers](https://testcontainers.com/)
- [Hypothesis](https://hypothesis.readthedocs.io/)
- [MLflow](https://mlflow.org/)
- [Langfuse](https://langfuse.com/)

---

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feat/your-feature`
3. Follow `.opencode/rules/git-workflow.md`
4. Run `/finish-work` before commit
5. Submit PR with description linking issue

---

## License

MIT License - Feel free to use and adapt for your projects.

---

## Acknowledgments

- **OpenCode team** for the excellent AI coding agent
- **Anthropic** for the Model Context Protocol and Claude models
- **Community MCP server authors** for the ecosystem
- **Addy Osmani** for agent-skills patterns
- **January Fonti** for the comprehensive template
- **All researchers** in autonomous coding agents (SICA, STOP, AlphaEvolve)

---

*Built with the vision of never-stopping, LLM-controlled autonomous coding pipelines.*
