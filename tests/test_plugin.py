"""Tests for agentic-project-grooming-plugin structure and specifications."""

import json
from pathlib import Path
import re

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def extract_frontmatter_aliases(content: str) -> list[str]:
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return []
    fm = match.group(1)
    alias_match = re.search(r"aliases:\s*\n((?:\s*-\s+[^\n]+\n)+)", fm)
    if not alias_match:
        return []
    return [line.strip().lstrip("-").strip() for line in alias_match.group(1).strip().splitlines()]


def test_plugin_manifest_valid():
    manifest_file = PLUGIN_ROOT / "plugin.json"
    assert manifest_file.exists(), "plugin.json must exist"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("name") == "agentic-project-grooming-plugin"
    assert data.get("version") == "0.1.0"
    assert data.get("license") == "MIT"
    assert "project grooming" in data.get("description", "").lower()


def test_license_exists():
    license_file = PLUGIN_ROOT / "LICENSE"
    assert license_file.exists(), "LICENSE must exist"
    content = license_file.read_text(encoding="utf-8")
    assert "MIT License" in content
    assert "Greg PFISTER" in content


def test_contributing_exists():
    contrib_file = PLUGIN_ROOT / "CONTRIBUTING.md"
    assert contrib_file.exists(), "CONTRIBUTING.md must exist"
    content = contrib_file.read_text(encoding="utf-8")
    assert "agentic-project-grooming-plugin" in content


def test_readme_exists():
    readme_file = PLUGIN_ROOT / "README.md"
    assert readme_file.exists(), "README.md must exist"
    content = readme_file.read_text(encoding="utf-8")
    assert "agentic-project-grooming-plugin" in content
    assert "Project_Request_Grooming.md" in content
    assert "@coding" in content
    assert "@coding-document" in content


def test_rules_exist():
    rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
    assert rules_file.exists(), "rules/AGENTS.md must exist"
    content = rules_file.read_text(encoding="utf-8")
    assert "Project Grooming Standards" in content
    assert "Project_Request_Grooming.md" in content
    assert "one question at a time" in content.lower()
    assert "agentic-coding-plugin" in content
    assert "agentic-project-documenting-plugin" in content


def test_skill_exists():
    skill_file = PLUGIN_ROOT / "skills" / "project-grooming" / "SKILL.md"
    assert skill_file.exists(), "skills/project-grooming/SKILL.md must exist"
    content = skill_file.read_text(encoding="utf-8")
    assert "name: project-grooming" in content
    assert "Step 1: Gap Analysis" in content
    assert "Step 2: Consistency & User Grilling" in content
    assert "Step 3: Approval Gate Artifact" in content
    assert "Step 4: Scaffolding & Delegation" in content
    assert "Project_Request_Grooming.md" in content


def test_groom_agent_exists():
    agent_file = PLUGIN_ROOT / "agents" / "coding-groom" / "agent.md"
    assert agent_file.exists(), "agents/coding-groom/agent.md must exist"
    content = agent_file.read_text(encoding="utf-8")
    assert "name: coding-groom" in content
    assert "# Coding - Project Grooming Specialist (@coding-groom)" in content

    aliases = extract_frontmatter_aliases(content)
    assert aliases, "aliases must be defined in frontmatter"
    alias_pattern = re.compile(r"^coding(-.*)?$")
    for alias in aliases:
        assert alias_pattern.match(alias), f"Alias '{alias}' does not match pattern '^coding(-.*)?$'"


def test_central_agent_guide_exists():
    central_file = PLUGIN_ROOT / "agents" / "agent.md"
    assert central_file.exists(), "agents/agent.md must exist"
    content = central_file.read_text(encoding="utf-8")
    assert "name: coding-groom-catalog" in content
    assert "# Coding - Project Grooming Subagents & Architecture" in content
