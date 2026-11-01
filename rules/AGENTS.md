# Project Grooming Standards — agentic-project-grooming-plugin

This rule set applies whenever the `agentic-project-grooming-plugin` is active in an Antigravity session.

---

## 1. Non-Destructive Analysis & Gap Auditing
- **Read-Only Inspection**: During initial repository assessment, strictly examine workspace structure, existing source code, git configuration, package manifests, and documentation using non-destructive inspection tools (`read_file`, `list_dir`, `run_command`).
- **Comprehensive Gap Identification**: Identify missing workspace essentials before prompting the user, including:
  - Repository topology and git status (`.git/`, sub-repos, branch conventions).
  - Project manifests (`pyproject.toml`, `package.json`, `plugin.json`, `Cargo.toml`).
  - License files (`LICENSE`, `COPYING`).
  - Project documentation (`README.md`, architecture guides, ADRs).
  - Workspace automation (`Makefile`, setup scripts, CI/CD workflows).
  - Code hygiene and linting configurations (`.gitignore`, `.editorconfig`, linters).
- **No Premature Mutation**: Never alter repository files, scaffold code, or modify project structure prior to interactive clarification and explicit approval of `Project_Request_Grooming.md`.

---

## 2. Interactive User Interrogation (Matt Pocock Style Grilling)
- **One Question at a Time**: When asking for user clarification, always use `ask_question` asking strictly **one question at a time**. Never combine multiple inquiries into a single turn.
- **Relentless Deep Clarification**: Interrogate vague, ambiguous, or incomplete requirements. Challenge assumptions and clarify edge cases until the project requirements are concrete across the 7 core dimensions:
  1. **Project Identification**: Official project name, tagline, core purpose, and problem statement.
  2. **Goals & Target Audience**: End-user personas, key pain points addressed, expected user outcomes, and value proposition.
  3. **Known Restrictions & Standards**: Target runtime platforms, language/runtime versions, architectural constraints, security/compliance rules, and coding standards.
  4. **Repository Topology**: Monorepo, polyrepo/sub-repo, or standalone repository layout; submodule or worktree strategies; workspace coordination rules.
  5. **Licensing**: License type (e.g. MIT, Apache 2.0, AGPL, proprietary), copyright holder, copyright year, and third-party attribution constraints.
  6. **Documentation Requirements**: Vault setup (Obsidian), documentation structure, README formats, feature specifications, and Architecture Decision Records (ADRs).
  7. **Workspace Tooling**: Package managers (`uv`, `npm`, `cargo`), test frameworks, linters/formatters, task runners (`Makefile`), and CI/CD automation.

---

## 3. Approval Gate & Artifact Protocol
- **Artifact Authoring**: Synthesize all gathered requirements, architectural decisions, and gap remediation plans into `Project_Request_Grooming.md` in the session artifact directory (`<appDataDir>/brain/<conversation-id>/Project_Request_Grooming.md`).
- **Sole and Final Tool Call Rule**:
  - Writing `Project_Request_Grooming.md` using `write_file` with `ArtifactMetadata={"RequestFeedback": True, "UserFacing": True}` must be the **sole and final tool call** of that turn.
  - Never batch secondary tool calls after authoring the artifact so Antigravity renders interactive Approve / Reject buttons.
- **User Revision Loop**:
  - If the user requests modifications or rejects the artifact, return to Section 2 (User Grilling) to clarify questions before regenerating `Project_Request_Grooming.md`.
  - Scaffolding and delegation proceed **only** upon explicit approval (`[GATE_APPROVED]`).

---

## 4. Cross-Plugin Scaffolding & Delegation
When `Project_Request_Grooming.md` is approved, coordinate with companion plugins dynamically:
- **Scaffolding Delegation (`@coding`)**:
  - Check if `agentic-coding-plugin` is installed:
    - **Installed**: Invoke `@coding` via `invoke_subagent(TypeName="coding", Role="Coding Workflow Orchestrator", Prompt=...)` to generate repositories, Makefile, scripts, licensing, and boilerplate code according to the approved grooming artifact.
    - **Not Installed**: Execute local fallback scaffolding directly or provide manual scaffolding guidance.
- **Documentation Archival Delegation (`@coding-document`)**:
  - Check if `agentic-document-plugin` is installed:
    - **Installed**: Invoke `@coding-document` via `invoke_subagent(TypeName="coding-document", Role="Documentation Specialist", Prompt=...)` to initialize the `<project>-obsidian/` knowledge vault, document architecture designs, and index initial ADRs.
    - **Not Installed**: Generate local markdown documentation templates directly in the workspace.

---

## 5. Communication & Links
- Keep communication concise, crisp, and high-signal.
- Always provide clickable markdown links using the `file://` scheme when referencing workspace files, directories, and code artifacts.
- Use GitHub Flavored Markdown alerts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`) appropriately to emphasize key points without nesting.
