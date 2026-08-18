# OpenCode Multi-Agent Orchestration Research

Comprehensive analysis of open-source projects and academic papers on building self-improving, never-stopping LLM coding pipelines.

**5 Papers Analyzed** | **20+ Open Source Projects** | **6 Orchestration Patterns** | **Architecture Blueprint**

---

## Table of Contents

1. [The Vision](#the-vision)
2. [Open Source Repos](#open-source-repos)
3. [Academic Papers](#academic-papers)
4. [Architecture Patterns](#architecture-patterns)
5. [Implementation Guide](#implementation-guide)
6. [Comparisons](#comparisons)

---

## The Vision

LLM controls OpenCode: prompt, accept permissions, never stop coding like a company pipeline with planner, code reviewer, documenter agents and a progress dashboard.

**Key Components:**
- Multi-Agent Orchestration (7 specialized agents)
- Continuous Operation (never-stopping loop)
- Permission Auto-Accept (risk-based)
- Progress Dashboard (real-time monitoring)

---

## Open Source Repos

### Top Tier

| Project | Focus | Relevance |
|---------|-------|-----------|
| **Sugar** | Full pipeline framework | High |
| **Continuous Agent** | Never-stopping execution | High |
| **OpenCode Orchestrator** | OpenCode integration | High |

### Medium Tier

| Project | Focus | Relevance |
|---------|-------|-----------|
| Oh My OpenAgent | Agent orchestration | Medium-High |
| Sweteam | Team coordination | Medium-High |
| Godcoder | Self-improvement | Medium-High |
| Hermes Studio | Monitoring dashboard | Medium-High |
| OpenCode Agent Live Monitor | Live monitoring | Medium |

### Supporting Projects

- opencode-ai/opencode (Core)
- anthropics/anthropic-cookbook (Reference)
- langchain-ai/langgraph (Framework)
- crewai/crewai (Framework)
- autogen/autogen (Framework)
- mlflow/mlflow (Dashboard)
- langfuse/langfuse (Monitoring)

---

## Academic Papers

### 1. SICA — Self-Improving Code Agents (2025)

**Core Idea:** Agent edits itself — uses experience to improve prompts, tools, and workflows.

**Results:** 17-53% improvement on SWE-Bench Verified

**How It Works:**
1. Experience Collection
2. Self-Reflection
3. Self-Modification
4. Validation

**Relevance:** Directly applicable — agents can improve themselves without external feedback loops.

### 2. Self-Harness — Harnesses That Improve Themselves (2026)

**Core Idea:** The infrastructure controlling the agent (harness) is optimized by the same LLM.

**Results:** 15-52% improvement on Terminal-Bench-2.0

**Key Innovation:** "Meta-prompting" — LLM writes prompts that control itself.

**Relevance:** Orchestrator can improve its own task routing logic.

### 3. AlphaEvolve — Google DeepMind Evolutionary Coding (2025)

**Core Idea:** Evolutionary algorithms + LLMs to discover novel algorithms.

**Results:** Discovered algorithms outperforming human-designed ones.

**Key Innovation:** LLMs as mutation operators in evolutionary algorithms.

**Relevance:** Evolve agent prompts through selection and mutation.

### 4. STOP — Self-Ta Optimizer for Programming (2024)

**Core Idea:** Mathematically proven safety for recursive self-improvement.

**Results:** Formally verified safety properties preserved across iterations.

**Key Innovation:** Formal safety guarantees for self-improving systems.

**Relevance:** Crucial for permission auto-accept system.

### 5. CER — Contextual Experience Replay (2025)

**Core Idea:** Store experiences with rich context and retrieve based on contextual similarity.

**Results:** Significant improvement via context-aware learning.

**Key Innovation:** "Contextual similarity" for transfer learning.

**Relevance:** Agents learn from each other's successes and failures.

---

## Architecture Patterns

### 1. Orchestrator-Worker Pattern (Recommended)
Central orchestrator routes tasks to specialized workers. Simple, scalable, clear separation.

### 2. Pipeline Pattern
Sequential flow through agents. Predictable, easy to monitor, clear quality gates.

### 3. Fan-Out/Fan-In Pattern
Parallel execution of independent subtasks. Maximum throughput, good for batch processing.

### 4. Priority Queue Loop Pattern
Tasks prioritized and executed in order. Never stops, self-healing, handles failures.

### 5. Self-Improving Loop Pattern (SICA-inspired)
Execute → Analyze → Improve → Repeat. Continuous improvement, compound gains.

### 6. Spec-Driven Pattern
Tasks driven by formal specifications. Highest quality, formally verified.

**Recommended Hybrid:** Orchestrator-Worker + Priority Queue Loop + Self-Improving Loop

---

## Implementation Guide

### Step 1: Agent Configuration
Define specialized agents in `.opencode/agents/` with clear roles.

### Step 2: Permission Auto-Accept
Configure risk-based auto-accept for low-risk operations.

### Step 3: Custom Commands
Create orchestration commands for task delegation and monitoring.

### Step 4: Progress Dashboard
Set up MLflow, Langfuse, or Hermes Studio for monitoring.

### Step 5: Continuous Operation
Implement the never-stopping loop with priority queue.

### Step 6: Self-Improvement (SICA)
Add self-improvement loop based on SICA paper.

### Step 7: Experience Replay (CER)
Implement contextual experience replay for learning.

### Step 8: Safety Rules
Establish safety and quality rules based on STOP principles.

---

## Comparisons

### Papers Performance

| Paper | Benchmark | Score | Improvement |
|-------|-----------|-------|-------------|
| SICA | SWE-Bench Verified | 53% | +53% |
| Self-Harness | Terminal-Bench-2.0 | 52% | +52% |
| AlphaEvolve | Matrix Multiplication | Novel | Outperforms human |
| CER | Agent Benchmarks | Significant | +30-40% |

### Project Features

| Project | Orchestration | Monitoring | Self-Improvement |
|---------|---------------|------------|------------------|
| Sugar | ✓ | ✓ | Partial |
| Continuous Agent | Basic | ✓ | ✗ |
| OpenCode Orchestrator | ✓ | Basic | ✗ |
| Hermes Studio | ✗ | ✓ | ✗ |
| Godcoder | Basic | Basic | ✓ |

### Recommendation

**For Our Use Case:**
1. Start with Orchestrator-Worker + Priority Queue Loop
2. Add self-improvement (SICA)
3. Add experience replay (CER)
4. Ensure safety (STOP)
5. Optimize over time (AlphaEvolve)

---

## Links

- [GitHub Repository](https://github.com/AliNikkhah2001/Tools_AI-MCP)
- [SICA Paper](https://arxiv.org/abs/2504.15228)
- [Self-Harness Paper](https://arxiv.org/abs/2606.09498)
- [AlphaEvolve Paper](https://arxiv.org/abs/2506.13131)
- [STOP Paper](https://arxiv.org/abs/2310.02304)
- [CER Paper](https://arxiv.org/abs/2506.06698)
