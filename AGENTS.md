# AGENTS.md

## Commands
Build:     `npm run build`
Test:      `npm test`
Test (single): `npm test -- path/to/file.test.ts`
Lint:      `npm run lint`
Typecheck: `npx tsc --noEmit`
Format:    `npm run format`
Python Lint: `ruff check .`
Python Format: `ruff format .`
Python Typecheck: `mypy .`

## Code Style
- TypeScript strict mode. No `any`.
- Named exports only. No default exports.
- Async/await over `.then()` chains.
- Error messages: lowercase, no trailing period.
- Descriptive variable names. No single letters except loop counters.
- Max 200 lines per file. Max 4 parameters per function.
- Python: Ruff for linting/formatting, mypy for type checking
- Python: Pydantic for validation, SQLAlchemy 2.0 for ORM
- Python: pytest with fixtures, hypothesis for property testing

## Architecture
- Layered: presentation → application → domain → infrastructure
- Dependency inversion: domain defines interfaces, infrastructure implements
- No circular dependencies between modules
- Database: repository pattern, migrations versioned
- ML: Separate data, training, serving pipelines

## Rules & Restrictions
- Never commit without passing lint + typecheck + tests
- No direct DB access in application layer
- All external calls behind interfaces
- Secrets via environment variables only
- PRs require: review approval + CI green + updated docs
- ML experiments tracked with MLflow/W&B
- Model artifacts scanned for safety before deployment

## Design Patterns (Reference)
- **Creational**: Factory, Builder, Abstract Factory
- **Structural**: Adapter, Decorator, Facade, Proxy
- **Behavioral**: Strategy, Observer, Command, Template Method
- **Architectural**: Repository, Unit of Work, CQRS, Event Sourcing
- **ML Patterns**: Feature Store, Model Registry, A/B Testing, Canary Deployment

## Python-Specific
- uv for package management, ruff for formatting
- Type hints required on all public functions
- Dataclasses over regular classes for data containers
- Pathlib over os.path
- Structured logging with structlog

## Available MCP Servers
- **github**: Repository, PR, Actions, Issues management
- **semantic-scholar**: Academic paper search, citations, authors
- **arxiv**: ArXiv paper search, download, analysis
- **kubernetes**: Cluster management, deployments, logs
- **ruff**: Python linting, formatting, type checking
- **clean-code**: Clean code principles, architecture planning
- **colab-exec**: Execute Python on Google Colab GPUs (T4/L4)
- **kaggle-exec**: Execute Python on Kaggle GPUs
- **runpod**: Manage RunPod GPU instances for training
- **sonarqube**: Code quality, security, duplication analysis
- **gitlab-ci**: GitLab CI/CD pipelines, MRs, jobs
- **mcpfinder**: Discover MCP servers programmatically