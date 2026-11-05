---
name: coding-groom-catalog
description: Architecture overview and catalog for the agentic-project-grooming-plugin subagents.
enable_write_tools: false
enable_subagent_tools: false
enable_mcp_tools: false
tools:
  - read_file
  - list_dir
---

# Coding - Project Grooming Subagents & Architecture (agents/agent.md)

This document defines the subagent architecture and catalog for the **`agentic-project-grooming-plugin`**.

---

## 1. Architectural Overview

The `agentic-project-grooming-plugin` provides interactive project grooming, requirement clarification, repository gap analysis, and scaffolding delegation across workspaces. It isolates project scoping into a specialized subagent (`@coding-groom`), ensuring projects are systematically analyzed across 7 core dimensions and approved via `Project_Request_Grooming.md` before code or repository structures are generated.

### Directory Structure
```text
agents/
├── agent.md                    # Master subagent guide (this file)
└── coding-groom/               # Interactive Project Grooming Specialist (@coding-groom)
    └── agent.md
```

---

## 2. Subagent Catalog

| Agent Handle | Directory | `enable_write_tools` | `enable_subagent_tools` | `enable_mcp_tools` | Allowed Tools | Description |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **`@coding-groom`** | [`agents/coding-groom/`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-project-grooming-plugin/agents/coding-groom/) | `True` | `True` | `True` | `read_file`, `list_dir`, `run_command`, `ask_question`, `write_file`, `invoke_subagent`, `send_message` | Interactive project grooming specialist auditing repositories, grilling users one question at a time across 7 dimensions (via direct `ask_question` when standalone, or Question Relay Protocol `[QUESTION_RELAY_REQUEST]` / `[QUESTION_RELAY_RESPONSE]` when delegated), authoring `Project_Request_Grooming.md` approval artifacts (relayed via `[ARTIFACT_APPROVAL_REQUEST]` / `[ARTIFACT_APPROVAL_RESPONSE]` when delegated under a caller orchestrator, or direct interactive `write_file` with `RequestFeedback=True` when standalone), and delegating scaffolding to `@coding` and `@coding-document`. |

---

## 3. Project Grooming & Delegation Pipeline

```text
Gap Analysis (Step 1) ──> User Grilling (Step 2) ──────────────────────────────┐
                           (Standalone: direct ask_question 1 at a time)        │
                           (Subagent: [QUESTION_RELAY_REQUEST] via send_message)│
                                  ▲                                             │
                                  │                                             ▼
                              (Revisions) <────────────── Write Project_Request_Grooming.md (Step 3)
                                                           (Standalone: write_file RequestFeedback=True)
                                                           (Subagent: [ARTIFACT_APPROVAL_REQUEST] via send_message)
                                                                                │
                                                                   [ARTIFACT_APPROVAL_RESPONSE: APPROVED]
                                                                                ▼
                                                                   Scaffolding Delegation (Step 4)
                                                                   ├── @coding (scaffolding code/repos)
                                                                   └── @coding-document (vault/ADRs)
```
