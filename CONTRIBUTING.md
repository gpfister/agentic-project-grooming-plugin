# Contributing to agentic-project-grooming-plugin

Thank you for contributing to **`agentic-project-grooming-plugin`**! This plugin provides interactive project grooming, requirement clarification, and workspace scaffolding capabilities for Google Antigravity.

---

## 1. Core Guidelines
- Adhere to the standards defined in [`rules/AGENTS.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-project-grooming-plugin/rules/AGENTS.md).
- Keep subagent definitions modular, declarative, and isolated in `agents/<agent>/agent.md`.
- Skills must include valid YAML frontmatter (`name`, `description`) matching the skill directory name.
- Grilling must strictly follow the **one question at a time** principle using `ask_question`.

---

## 2. Directory Structure

```text
agentic-project-grooming-plugin/
├── plugin.json         # Plugin manifest
├── pyproject.toml      # Project metadata & test dependencies
├── README.md           # Documentation
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # Contribution guidelines
├── agents/             # Subagent definitions
│   ├── agent.md        # Central subagent & architecture specification
│   └── coding-groom/   # Interactive project grooming specialist (@coding-groom)
│       └── agent.md
├── skills/             # Progressive-disclosure skills
│   └── project-grooming/# 4-step grooming & scaffolding workflow
│       └── SKILL.md
├── rules/              # Plugin-scoped rules
│   └── AGENTS.md
└── tests/              # Test suite
    └── test_plugin.py
```

---

## 3. Testing
Run tests using `pytest` or `uv`:

```bash
uv run pytest
# or
pytest
```

Validate plugin manifest:

```bash
python3 -m json.tool plugin.json
```
