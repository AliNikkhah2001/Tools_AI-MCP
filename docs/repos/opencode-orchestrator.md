# OpenCode Orchestrator

**Repository:** [github.com/cloudpftc/opencode-orchestrator](https://github.com/cloudpftc/opencode-orchestrator)
**Stars:** 2 | **Commits:** 5,973 | **Language:** TypeScript

## Overview

OpenCode Orchestrator (formerly Claude Flow/Ruflo) is an enterprise-grade AI agent orchestration platform for OpenCode. It deploys 60+ specialized agents in coordinated swarms with self-learning capabilities, fault-tolerant consensus, and enterprise-grade security.

## Key Features

- **60+ Specialized Agents:** Coder, tester, reviewer, architect, security, and more
- **Swarm Coordination:** Mesh, hierarchical, ring, and star topologies
- **Consensus Protocols:** Raft, BFT, Gossip, CRDT for fault tolerance
- **Self-Learning Loop:** Agents improve from their own experience
- **Q-Learning Router:** Intelligent task routing to optimal agents
- **RuVector Intelligence:** SONA self-optimization, EWC++ no-forgetting, Flash Attention
- **Memory System:** AgentDB with HNSW (150x-12,500x faster retrieval)
- **Multi-Provider Support:** Claude, GPT, Gemini, Ollama

## Architecture

```
User → OpenCode Orchestrator (CLI/MCP) → Router → Swarm → Agents → Memory → LLM Providers
                       ↑                          ↓
                       └──── Learning Loop ←──────┘
```

## Installation

```bash
npm install -g cloudpftc-opencode-orchestrator
```

## Usage

```bash
# Start orchestrator
opencode-orchestrator start

# Deploy a swarm
opencode-orchestrator swarm deploy --topology mesh --agents 10

# Monitor agent activity
opencode-orchestrator status
```

## Directory Structure

```
opencode-orchestrator/
├── .agents/           # Agent definitions
├── .opencode/         # OpenCode configuration
├── agents/            # Agent implementations
├── bin/               # CLI binaries
├── plugin/            # Plugin system
├── scripts/           # Automation scripts
├── tests/             # Test suite
├── v2/, v3/           # Version-specific code
├── opencode.json      # OpenCode config
└── package.json       # Node.js dependencies
```

## Relevance to Our Project

**High relevance** — This is the most comprehensive orchestration platform for OpenCode. Key takeaways:
- Swarm coordination patterns for multi-agent systems
- Self-learning loop architecture
- Consensus protocols for fault tolerance
- Memory system with fast retrieval

## Pros & Cons

| Pros | Cons |
|------|------|
| 60+ pre-built agents | Very large codebase (9720 files) |
| Enterprise-grade features | Complex setup |
| Self-learning capabilities | Limited documentation |
| Multiple consensus protocols | Active development (5973 commits) |

## Running This Repo

```bash
cd cloned-repos/opencode-orchestrator
npm install
npm run build
npm start
```
