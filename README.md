# OpenCode AI Engineering Configuration

A production-ready OpenCode configuration for AI engineering, model training, research, server setup, and clean code practices.

## 🎯 Overview

This repository contains a comprehensive OpenCode setup with:
- **12 MCP servers** for AI engineering workflows
- **8 specialized agents** for different development roles
- **7 slash commands** for quality gates and workflows
- **5 skills** for clean code, refactoring, testing, security, and Python patterns
- **7 rule files** covering security, coding style, testing, git, patterns, performance, and agents

---

## 📦 MCP Servers Configured

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

### Required Environment Variables

```bash
# .env file (create from .env.example)
SEMANTIC_SCHOLAR_API_KEY=your_key_here
GITLAB_URL=https://gitlab.example.com
GITLAB_TOKEN=glpat-xxxxxx
GITLAB_PROJECT_PATH=my-org/my-repo
```

---

## 🤖 Specialized Agents

| Agent | Model | Permissions | Use Case |
|-------|-------|-------------|----------|
| **review** | Sonnet 4 | Read-only | Code review, quality, security |
| **architect** | Opus 4 | Read-only | System design, ADRs, diagrams |
| **security-auditor** | Sonnet 4 | Read-only | OWASP, CWE, threat modeling |
| **test-engineer** | Sonnet 4 | Test files only | TDD, test scaffolding |
| **backend-specialist** | Sonnet 4 | Full (scoped) | APIs, databases, distributed systems |
| **frontend-specialist** | Sonnet 4 | Full (scoped) | React, TypeScript, accessibility |
| **ml-engineer** | Sonnet 4 | Full (scoped) | PyTorch, training, deployment |

### Agent Delegation Pattern

```
@architect → @test-engineer → @implementer → @review → @security-auditor
```

---

## ⚡ Slash Commands

| Command | Description |
|---------|-------------|
| `/learn` | Capture lessons into AGENTS.md |
| `/finish-work` | Full quality gate (lint, typecheck, test, security) |
| `/check-cross-layer` | Verify API↔DB↔Frontend↔Tests consistency |
| `/context-prime` | Load project context before work |
| `/careful-review` | Fresh-eyes review delegation |
| `/find-missing-tests` | Identify untested code paths |
| `/race-and-pick` | Parallel implementations, pick best |
| `/session-summary` | Generate handoff summary |

---

## 🎓 Skills

| Skill | Purpose | Auto-Invoked When |
|-------|---------|-------------------|
| **clean-code** | 63 Clean Code principles + validation | New code, refactoring, PR review |
| **code-refactoring** | SOLID refactoring patterns | Code smells detected, `/clean` |
| **python-patterns** | Modern Python (type hints, dataclasses, DI) | Python files, ML code |
| **testing-patterns** | Test pyramid, TDD, property-based | New features, coverage gaps |
| **security-review** | OWASP Top 10, ML security | Auth code, deps, pre-release |

---

## 📏 Rules (Always Active)

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

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/YOUR_USERNAME/opencode-ai-engineering.git
cd opencode-ai-engineering
cp .env.example .env  # Add your API keys
```

### 2. Install OpenCode
```bash
# Follow https://opencode.ai/docs/installation
# Or via npm: npm install -g @opencode/opencode
```

### 3. Verify Configuration
```bash
opencode mcp list
# Should show all 12 servers

opencode agent list
# Should show all 8 agents
```

### 4. Start Working
```bash
opencode
# Then in OpenCode:
/context-prime          # Load project context
# ... do work ...
/finish-work            # Quality gate before commit
```

---

## 🔧 MCP Server Details

### Research & Literature
```bash
# Search papers
@semantic-scholar search "transformer attention mechanism" --year 2023 --min-citations 100
@arxiv search "diffusion models" --categories cs.LG,cs.CV --date-from 2024-01-01

# Download & analyze
@arxiv download 2401.12345
@semantic-scholar get-paper 649def34f8be52c8b66281af98ae884c09aef38b
```

### GPU Training (No Local GPU Needed)
```bash
# Google Colab (free T4)
@colab-exec python -c "import torch; print(torch.cuda.get_device_name(0))"

# Kaggle (free T4×2)
@kaggle-exec notebook --gpu --file train.ipynb

# RunPod (pay-per-second)
@runpod create-pod --gpu "RTX A6000" --image "pytorch/pytorch:2.4.0-cuda12.4"
```

### Code Quality
```bash
# Lint & format
@ruff check src/
@ruff format src/
@ruff check --fix src/

# Security scan
@sonarqube scan --project=my-project

# Clean code validation
@clean-code validate src/
```

### Kubernetes
```bash
# Cluster management
@kubernetes get pods -n production
@kubernetes logs deployment/api -n production
@kubernetes apply -f manifests/
```

---

## 📁 Project Structure

```
.
├── AGENTS.md                 # Root instructions (cross-tool compatible)
├── opencode.json             # OpenCode configuration
├── .env.example              # Environment variable template
├── README.md                 # This file
├── .opencode/
│   ├── agents/               # 8 specialized agents
│   │   ├── review.md
│   │   ├── architect.md
│   │   ├── security-auditor.md
│   │   ├── test-engineer.md
│   │   ├── backend-specialist.md
│   │   ├── frontend-specialist.md
│   │   └── ml-engineer.md
│   ├── commands/             # 8 slash commands
│   │   ├── learn.md
│   │   ├── finish-work.md
│   │   ├── check-cross-layer.md
│   │   ├── context-prime.md
│   │   ├── careful-review.md
│   │   ├── find-missing-tests.md
│   │   ├── race-and-pick.md
│   │   └── session-summary.md
│   ├── skills/               # 5 skills
│   │   ├── clean-code/SKILL.md
│   │   ├── code-refactoring/SKILL.md
│   │   ├── python-patterns/SKILL.md
│   │   ├── testing-patterns/SKILL.md
│   │   └── security-review/SKILL.md
│   └── rules/                # 8 rule files
│       ├── security.md
│       ├── coding-style.md
│       ├── testing.md
│       ├── git-workflow.md
│       ├── patterns.md
│       ├── performance.md
│       ├── agents.md
│       └── hooks.md
└── .opencode/sessions/       # Session summaries (auto-generated)
```

---

## 🎯 Best Practices

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

---

## 🔐 Security Notes

- **Never commit `.env`** - Added to `.gitignore`
- **API keys in environment variables only** - Referenced as `{env:VAR_NAME}`
- **MCP servers with OAuth** - GitHub, GitLab use OAuth flows
- **SonarQube** - Configure your instance URL in `opencode.json`
- **Model Safety** - Use `model-safety-mcp` to scan `.pt/.pth` files before deployment

---

## 📚 References

### MCP Registries
- **Official**: https://registry.modelcontextprotocol.io
- **Glama**: https://glama.ai/mcp/servers (50,000+)
- **PulseMCP**: https://pulsemcp.com (11,840+ curated)
- **Smithery**: https://smithery.ai (7,000+ with hosting)
- **mcp.so**: https://mcp.so (19,700+ community)

### Key Papers
- [MCP Server Architecture Patterns](https://arxiv.org/abs/2606.30317) (2026)
- [Model Context Protocol](https://modelcontextprotocol.io) (Anthropic, 2024)
- [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) (Robert C. Martin)

### Tools
- [OpenCode Docs](https://opencode.ai/docs)
- [Ruff](https://docs.astral.sh/ruff/)
- [Biome](https://biomejs.dev/)
- [Testcontainers](https://testcontainers.com/)
- [Hypothesis](https://hypothesis.readthedocs.io/)

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feat/your-feature`
3. Follow `.opencode/rules/git-workflow.md`
4. Run `/finish-work` before commit
5. Submit PR with description linking issue

---

## 📄 License

MIT License - Feel free to use and adapt for your projects.

---

## 🙏 Acknowledgments

- **OpenCode team** for the excellent AI coding agent
- **Anthropic** for the Model Context Protocol
- **Community MCP server authors** for the ecosystem
- **Addy Osmani** for agent-skills patterns
- **January Fonti** for the comprehensive template