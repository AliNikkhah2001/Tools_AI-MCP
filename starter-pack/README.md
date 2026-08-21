# OpenCode Starter Pack — Autonomous Multi-Agent Coding Pipeline

> **Production-ready OpenCode configuration for autonomous multi-agent coding pipelines with continuous flow, real-time dashboards, and zero-stop orchestration.**
> Optimized for free model access via LM Studio + Deepseek Coder V2 + Superpowers plugin.

---

## 🚀 5-Minute Quick Start

```bash
# 1. Clone the starter pack into any new project
git clone <this-repo> my-project
cd my-project

# 3. OpenCode will auto-load the configuration
opencode

# 5. Load context and start coding
/context-prime

# 6. Start the standard pipeline
@architect "Design a REST API for user management"
@test-engineer "Create tests for JWT authentication flow"
@backend-specialist "Implement JWT with refresh tokens"
/careful-review
/finish-work

# 7. Commit
git add -A && git commit -m "feat(auth): add JWT authentication"
```

---

## 📦 What's Included — Full Inventory

### 📁 Project Structure
```
starter-pack/
├── README.md              # This comprehensive guide
├── AGENTS.md              # Agent guidelines + permission model
├── guardrails.md          # Safety gates, anti-patterns, conventions
├── .opencode/
│   ├── agents/            # (empty — add project-specific agent configs)
│ │   └── *.md             # Agent configurations
│ ├── commands/            # 8 slash commands for orchestration
│ │   ├── context-prime.md
│ │   ├── finish-work.md
│ │   └── careful-review.md
│ ├── rules/               # 8 rule files (copy from template)
│ │   ├── agents.md
│ │   ├── coding-style.md
│ │   ├── git-workflow.md
│ │   ├── hooks.md
│ │   ├── patterns.md
│ │   ├── performance.md
│ │   ├── security.md
│ │   └── testing.md
│ ├── skills/              # 5 production skills + Superpowers skills
│ │   ├── clean-code/SKILL.md
│ │   ├── python-patterns/SKILL.md
│ │   ├── code-refactoring/SKILL.md
│ │   ├── security-review/SKILL.md
│ │   ├── testing-patterns/SKILL.md
│ │   └── superpowers/     # Superpowers plugin skills
│ │       ├── brainstorming/SKILL.md
│ │       ├── test-driven-development/SKILL.md
│ │       └── ... (12 total)
│ ├── plugins/
│   ├── compaction.ts      # Token compaction + ANSI stripping
│   └── superpowers/       # Superpowers plugin (installed via npm)
│ └── .git/                # Git repo (already initialized)
```

### 🤖 Agents (7 Total)
All agents use `deepseek-coder-v2` model via LM Studio at `localhost:1234/v1`.

| Agent | Role | Permissions | When to Use |
|-------|------|-------------|-------------|
| **@architect** | System design, ADRs, diagrams, task decomposition | Read-only | Start of any new feature; architecture planning |
| **@review** | Code review — correctness, design, readability, security | Read-only | Before `/finish-work`; fresh-eyes pass |
| **@security-auditor** | OWASP Top 10, CWE, STRIDE, threat modeling | Read-only | Auth code, deps, pre-release, security gates |
| **@test-engineer** | TDD — write tests first (RED → GREEN) | Test files only | Before implementation; coverage gaps |
| **@backend-specialist** | APIs, databases, caching, distributed systems | Full (scoped) | API design, DB schemas, caching, distributed systems |
| **@frontend-specialist** | React, TypeScript, UI/UX, accessibility | Full (scoped) | Components, forms, styling, accessibility |
| **@ml-engineer** | PyTorch, training loops, GPU optimization, deployment | Full (scoped) | Training scripts, GPU setups, model deployment |

**Standard Pipeline**:
```
@architect → @test-engineer → @implementer → @review → @security-auditor
```

**Emergency Hotfix**:
```
@implementer (scoped) → @test-engineer (targeted) → @review (fast)
```

**Research Task**:
```
@analyzer (broad research) → @architect (synthesis) → @implementer
```

**How to invoke**: `@agent-name "task description"` — e.g., `@architect "Design a REST API for user management with OAuth2"`

### ⌘ Slash Commands (8 Total)
| Command | Description | When to Use |
|---------|-------------|-------------|
| `/context-prime` | Load repo context before real work starts | Start of every session; before complex tasks |
| `/finish-work` | Full quality gate: lint → typecheck → test → security | Before every commit; never skip |
| `/careful-review` | Fresh-eyes review delegation with structured checklist | After implementation; before `/finish-work` |
| `/check-cross-layer` | Verify API↔DB↔Frontend↔Tests consistency | Complex multi-layer changes |
| `/find-missing-tests` | Identify untested code paths and suggest scaffolding | Coverage drops; new feature addition |
| `/race-and-pick` | Parallel implementations — run 3 approaches, pick best | Competing approaches; uncertainty |
| `/learn` | Capture non-obvious lessons into `AGENTS.md` | After problem-solving; new insight discovered |
| `/session-summary` | Generate handoff summary with git stats, cost, next steps | End of session; handoff or next-day resume |

**Usage**: Type any command in the OpenCode terminal. Most accept optional file arguments, e.g. `/careful-review path/to/file.py`.

### ⚙️ Skills (5 Production + 12 Superpowers)
Skills are auto-invoked by agents via `.opencode/rules/agents.md` and `AGENTS.md`, or manually via `@skill-name`.

#### 5 Production Skills (Built-in)

**1. `@clean-code` — Clean Code Principles**
- **12 Rules**: meaningful names, small functions, no bad comments, formatting, data hiding, error handling, boundaries, unit tests (FIRST), classes, emergence, concurrency
- **Automated validation**: `ruff check . --select=ALL` + `ruff format . --check` + `mypy . --strict`
- **Review checklist**: Names, function size, no duplication, tests, error handling, no commented code, inverted dependencies, protected boundaries
- **Invoke when**: Writing new code, refactoring, PR review, establishing project standards

**2. `@python-patterns` — Modern Python Best Practices**
- **Type hints** on all public functions/classes
- **Dataclasses** over regular classes for data containers
- **Pathlib** over `os.path`
- **Structured logging** with `structlog` (JSON output)
- **Error handling** with Result types (`Ok`/`Err`)
- **Dependency injection** via Protocols
- **Configuration** with Pydantic + Hydra/OmegaConf
- **Testing patterns** with pytest + Hypothesis + parametrized + async
- **ML-specific patterns**: reproducibility (set_seed), checkpointing, config hashing
- **Ruff configuration** (pyproject.toml) included

**Invoke when**: Python files, ML code, public functions, type hinting needs.

**3. `@code-refactoring` — SOLID Refactoring Patterns**
- **When to refactor**: Rule of 3; code smells; before adding features; during code review
- **11 patterns**: Extract Method, Replace Conditional with Polymorphism, Introduce Parameter Object, Replace Inheritance with Delegation, + anti-patterns table
- **Safe workflow**: Ensure tests pass → small steps → run tests after each step → commit after green → use IDE tools
- **Anti-patterns**: Long Method → Extract Method; Large Class → Extract Class; Duplicate Code → Extract Method/Class; +8 more

**Invoke when**: Code smells detected; reviewer suggests improvement; before adding features; technical debt identification.

**3. `@security-review` — OWASP Top 10 Security Auditing**
- **Full A01-A10 checklist**: Broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, authentication failures, software integrity failures, logging/monitoring failures, SSRF
- **Code review patterns**: Input validation, authorization policies, secrets detection, SAST integration
- **ML-specific security**: Model artifact scanning, data poisoning prevention, adversarial robustness
- **MCP servers**: sonarqube, model-safety-mcp, semgrep-mcp, ingero

**Invoke when**: `@security-auditor` agent activated; `/careful-review` includes security focus; new auth/authorization code; dependency updates; pre-release security gate.

**Output**: Severity-rated findings with exploit scenarios and fixes.

**4. `@testing-patterns` — Test Pyramid & Strategies**
- **Test pyramid**: 70% unit / 20% integration / 10% E2E
- **Unit testing**: FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely); AAA pattern; parameterized; property-based with Hypothesis
- **Integration testing**: Testcontainers (PostgreSQL); Pact API contracts; Playwright E2E
- **Test organization**: `tests/unit/`, `tests/integration/`, `tests/e2e/`, `tests/fixtures/`, `conftest.py`
- **Coverage targets**: Unit 80% / 95% critical; Integration 70% / 90% critical; E2E 100% critical
- **CI pipeline**: GitHub Actions with unit/integration/e2e jobs; mutation testing (mutmut / stryker)

**Invoke when**: Writing new code (TDD: test first); `/find-missing-tests`; coverage drops below threshold.

**5. compaction.ts — Token Compaction Plugin**
- **ANSI stripping**: Removes color codes that bloat context without diagnostic utility
- **Git diff truncation**: 35 lines/file max; retains file path and hunk headers; adds truncation marker
- **Test log compression**: Extracts only failures/assertions from pytest/vitest/go test/cargo test; filters passing tests
- **Failure pinpointing**: Exact `AssertionError`, expected/received values, top stack trace frames
- **Hook**: `afterToolExecution` — transforms bash/exec/terminal output before storing in context history
- **Config**: `maxDiffLinesPerFile: 35`, `maxStackTraceLines: 20`, `enableAnsiStripping: true`, `rawCharThreshold: 1500` (≈375 tokens)

#### 12 Superpowers Skills (Installed via npm plugin)
The Superpowers plugin (`superpowers@6.3.0`) adds 12 agentic skills for enhanced coding workflows. Installed via:
```bash
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix ~/.config/opencode
```

| Skill | Description | When to Use |
|-------|-------------|-------------|
| **brainstorming** | Turn ideas into fully formed designs and specs through collaborative dialogue. Classifies requests into Spike/Bounded/Architectural paths with hard approval gates before any implementation. | Before any creative work — creating features, building components, adding functionality, or modifying behavior. Uses hard approval gates. |
| **test-driven-development** | Write the test first. Watch it fail. Write minimal code to pass. Core principle: "If you didn't watch the test fail, you don't know if it tests the right thing." | Always for new features, bug fixes, refactoring. Never skip TDD "just this once." |
| **systematic-debugging** | Structured debugging process guidance. | When diagnosing and fixing bugs systematically. |
| **subagent-driven-development** | Coordinate multi-agent development workflows. | When managing complex development through subagent orchestration. |
| **dispatching-parallel-agents** | Run multiple implementation approaches in parallel, then select the best. | When competing approaches need parallel exploration and evaluation. |
| **finishing-a-development-branch** | Complete a development branch with proper handoff and verification. | When closing out a feature branch before merge. |
| **receiving-code-review** | Handle incoming code reviews systematically. | When code reviews are being received and need structured response. |
| **requesting-code-review** | Request code reviews following proper workflows. | When you need others to review your code changes. |
| **using-git-worktrees** | Manage git worktrees for parallel development streams. | When working on multiple branches or features simultaneously. |
| **using-superpowers** | Understand and use the Superpowers skill framework effectively. | When learning the Superpowers framework and its workflows. |
| **writing-plans** | Document plans and specifications clearly. | When creating detailed project plans and specifications. |
| **writing-skills** | Document and structure skill definitions. | When creating or documenting new skills for the framework. |

**How to use Superpowers skills:**
```bash
# List available skills
opencode skill list

# Use a specific skill (examples)
opencode skill use brainstorm
opencode skill use test-driven-development
opencode skill use systematic-debugging
```

### 🔒 Guardrails — Safety and Quality Gates

### Mandatory Checks (Never Skip `/finish-work`)

1. **Quality Gate**
   - `npm run lint` passes
   - `npx tsc --noEmit` passes
   - `npm test` passes with 80%+ coverage
   - Security audit clean (no high-severity vulnerabilities)
   - Format check: `npm run format:check`

2. **Model Safety**
   - Never commit `.env` files — added to `.gitignore`
   - API keys only in environment variables (`{env:VAR_NAME}`)
   - No `eval()`, `exec()`, `Function()` with user input
   - Path traversal protection: validate file paths with `path.resolve()`
   - Model safety: scan `.pt`/`.pth` files before deployment

3. **Permission Model**
   - **Read**: Always allowed — any file in project
   - **Grep**: Always allowed — any search
   - **Glob**: Always allowed — any pattern
   - **Edit**: Scoped — only files in task scope
   - **Bash**: Scoped — only approved commands
   - **Write**: Scoped — only new files in task scope
   - **Question**: Denied — pipeline is non-interactive

4. **Anti-Patterns to Avoid**
   | Anti-Pattern | Problem | Solution |
   |-------------|---------|----------|
   | Giant prompts | Context overflow, poor quality | Break into small tasks |
   | No stop rules | Agent drift, wasted tokens | Pause after 2-3 failed correction loops |
   | Single model for everything | Inconsistent quality | Route by task complexity |
   | No quality gate | Unreviewed code | Always run `/finish-work` |
   | Skipping tests | Regressions | TDD: tests first, always |

5. **MCP Server Safety**
   - Disable when not needed (high token usage)
   - API keys rotated quarterly; store in `.env`
   - Free tier preference: use `deepseek-coder-v2` locally

### Conventions

#### Commit Messages (Conventional Commits)
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```
Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `security`, `ci`
Scopes: `auth`, `api`, `db`, `ui`, `ml`, `infra`, `config`

#### PR Template
- **Title**: Same as commit convention; link issue (`fixes #123`)
- **Description**: What, Why, How; screenshots for UI changes
- **Reviewers**: Minimum 2 approvals (1 domain expert, 1 cross-functional)
- **Checks**: All CI green (lint, typecheck, unit, integration, security)
- **Size**: <400 lines changed; split large PRs

---

## 🔗 MCP Servers (12 Total)

| Server | Type | Best For | Keys Needed |
|--------|------|----------|-------------|
| `github` | Remote | Repo browsing, PR management, issue tracking | `GITHUB_TOKEN` (optional; read-only works without) |
| `semantic-scholar` | Local | Academic paper search, citations, authors | `SEMANTIC_SCHOLAR_API_KEY` (optional; works locally without) |
| `arxiv` | Local | ArXiv papers — search, download, analyze | None |
| `kubernetes` | Local | Cluster management, helm/kubectl, read-only mode | None |
| `ruff` | Local | Python linting, formatting, type-checking | None |
| `clean-code` | Local | 63 Clean Code principles + validation | None |
| `colab-exec` | Local | Google Colab GPUs (T4/L4), PyTorch/TensorFlow | Colab OAuth credentials |
| `kaggle-exec` | Local | Kaggle GPUs (T4×2, P100, TPU) | `KAGGLE_USERNAME`/`KAGGLE_KEY` |
| `runpod` | Local | RunPod GPU cloud — pod/endpoint management | `RUNPOD_API_KEY` |
| `sonarqube` | Remote | SAST, security, duplication, quality gates | `SONARQUBE_URL`/`TOKEN` (optional) |
| `gitlab-ci` | Local | GitLab CI/CD pipelines, MRs, jobs, log grep | `GITLAB_URL`/`TOKEN`/`PROJECT_PATH` |
| `mcpfinder` | Local | Discover MCP servers programmatically | None |

**Most work locally without API keys**. Enable only what you need.

---

## 🎯 Standard Workflow

### New Feature (Recommended)

```bash
# 1. Prime context
/context-prime

# 2. Get architecture plan
@architect "Design user authentication system with OAuth2"

# 3. Write tests first (TDD)
@test-engineer "Create tests for OAuth2 flow"

# 4. Implement
@backend-specialist "Implement JWT with refresh tokens"

# 5. Review
/careful-review

# 6. Quality gate (lint → typecheck → test → security)
/finish-work

# 7. Commit
git add -A && git commit -m "feat(auth): add JWT authentication with OAuth2 providers"
```

### Emergency Hotfix

```bash
@backend-specialist (scoped fix) → @test-engineer (targeted test) → @review (fast) → /finish-work
```

### Research Task

```bash
@analyzer "Search for RAG architectures 2024-2025"  # Uses semantic-scholar MCP
@architect "Synthesize findings into architecture ADR"
@implementer "Implement proven patterns"
```

### Parallel Exploration

```bash
/race-and-pick "Implement auth" "approach1" "approach2" "approach3"
# 3 subagents compete; best solution selected; compaction plugin optimizes context
```

---

## 📦 How to Use This Starter Pack

### Option A: Clone the Starter Pack
```bash
git clone <this-repo>/starter-pack my-project
cd my-project

# OpenCode auto-loads configuration (includes Superpowers plugin)
opencode

# Start coding
/context-prime
@architect "Your feature description"
```

### Option B: Manual Copy
```bash
# From the Tools_AI-MCP directory
cp -r starter-pack my-new-project
cd my-new-project
opencode
# Config is auto-loaded with all plugins including Superpowers
```

### Option C: Programmatic Setup

The `opencode.json` in both `~/.config/opencode/` and the project root contains:
- 12 MCP server configurations (agent-lsp, context7, playwright, github, semantic-scholar, arxiv, kubernetes, ruff, clean-code, colab-exec, kaggle-exec, runpod)
- 7 agent definitions with `deepseek-coder-v2` model and proper permission models
- 12 Superpowers skills (via `superpowers@6.3.0` npm plugin)
- Plugin registration for `token-compaction-plugin`
- Instructions pointing to `AGENTS.md` and `.opencode/rules/*.md`

Just copy these files and you're ready to go.

---

## 🛠️ Development & Customization

### Adding a New Agent
1. Create `.opencode/agents/agent-name.md` with frontmatter:
```yaml
description: Your agent description
mode: subagent
model: deepseek-coder-v2
temperature: 0.2
permission:
  edit: allow  # or deny for read-only
  bash: allow  # or deny
  read: allow
  grep: allow
  glob: allow
```
2. Reference in `AGENTS.md` or `opencode.json`

### Adding a New Skill
1. Create `.opencode/skills/skill-name/SKILL.md` following the template of existing skills
2. Add rule entry in `.opencode/rules/skills.md` (or create one)
3. Reference in agent configs via `system prompt` or agent instructions

### Customizing MCP Servers
Edit `opencode.json` to:
- Enable/disable servers: `"enabled": true/false`
- Add custom servers with `type: local|remote`, `command`, `env`
- Configure remote URLs and environment variables

### Modifying the Pipeline
Edit the standard workflow in `AGENTS.md` or add new slash commands in `.opencode/commands/`. The compaction plugin `.opencode/plugins/compaction.ts` automatically optimizes all tool output.

---

## 📦 What's Included — Full List

| Category | Files |
|----------|-------|
| **Root** | `README.md`, `AGENTS.md`, `guardrails.md` |
| **.opencode/agents/** | (empty — add project-specific agent configs) |
| **.opencode/commands/** | `context-prime.md`, `finish-work.md`, `careful-review.md` |
| **.opencode/rules/** | *(copy from original repo: 8 rule files)* |
| **.opencode/skills/clean-code/SKILL.md** | 12 Clean Code rules + automated validation |
| **.opencode/skills/python-patterns/SKILL.md** | Type hints, dataclasses, pathlib, structlog, error handling, DI, config, testing, ML patterns |
| **.opencode/skills/code-refactoring/SKILL.md** | 11 refactoring patterns + safe workflow + anti-patterns |
| **.opencode/skills/security-review/SKILL.md** | OWASP Top 10 + code review patterns + ML security |
| **.opencode/skills/testing-patterns/SKILL.md** | Test pyramid + unit/integration/E2E patterns + CI + mutation testing |
| **.opencode/skills/superpowers/** | 12 Superpowers skills (brainstorming, TDD, debugging, parallel agents, git worktrees, code review, and more) |
| **.opencode/plugins/compaction.ts** | Token compaction + ANSI stripping + git diff truncation |
| **.opencode/plugins/superpowers/** | Superpowers npm plugin (installed via `npm install`) |
| **Git repo** | Initialized with all above files committed |

---

## 🐛 Troubleshooting

| Issue | Fix |
|-------|-----|
| "MCP server failed — executable not found" | Install via `uvx <server-name-mcp-server>` or ensure it's in PATH |
| "Model not found" | Ensure LM Studio is running at `http://localhost:1234/v1` and `deepseek-coder-v2` is loaded |
| "Permission denied" | Check agent permission model in `.opencode/agents/*.md`; read-only agents cannot edit |
| "Tests failing after /finish-work" | Run `/find-missing-tests` to identify gaps; add tests per skill guidelines |
| "Context too large" | The compaction plugin automatically truncates diffs and extracts only failures |
| "Agent drift" | Pause pipeline; run `/session-summary`; reset with `/context-prime`; resume with fresh context |

### Superpowers-Specific Issues
- **Skills not appearing**: Ensure OpenCode was restarted after plugin installation
- **Skill commands not recognized**: Use `opencode skill list` to see available skills, then `opencode skill use <name>`
- **Plugin not loading**: Verify the plugin line is in `opencode.json` and OpenCode v1.18.19+ is used

---

## 📞 Need Help?

- Check `AGENTS.md` for agent-specific guidance
- Run `/context-prime` to reload repo context
- Run `/finish-work` to trigger full quality gate
- Review `guardrails.md` for safety requirements
- All 17 skills (5 production + 12 Superpowers) have `SKILL.md` with detailed patterns and anti-patterns
- Review `SUPERPOWERS.md` in the superpowers npm package for detailed skill documentation

**Built for**: autonomous multi-agent coding pipelines with continuous flow, real-time dashboards, and zero-stop orchestration — optimized for free model access via LM Studio + Deepseek Coder V2 + Superpowers plugin.

*Built with the vision of never-stopping, LLM-controlled autonomous coding pipelines. Adapt freely for your projects.*