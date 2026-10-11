# 1. Discovery, requirements and planning (PRD, spec-driven development, task breakdown)

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Spec Kit** | Repo + CLI + agent commands | https://github.com/github/spec-kit | Official (GitHub) | 140.8k | Spec-driven development: `/specify → /plan → /tasks → /implement`. Works with Claude Code, Cursor, Copilot, Codex and others. |
| OpenSpec | Repo + CLI | https://github.com/Fission-AI/OpenSpec | Community | 71.6k | Lighter SDD. Strong for brownfield work and change proposals. |
| BMAD-METHOD | Repo (agent personas + workflows) | https://github.com/bmad-code-org/BMAD-METHOD | Community | 54.0k | Analyst → PM → Architect → Dev agent workflow. Heavy, but complete. |
| Taskmaster (claude-task-master) | MCP + CLI | https://github.com/eyaltoledano/claude-task-master | Community | 28.2k | Turns a PRD into dependency-ordered tasks over MCP. Last push was Apr 2026, so momentum is slowing. |
| Superpowers | Skills framework | https://github.com/obra/superpowers | Community | 297k | Brainstorm → plan → TDD → subagent-execute skills. The most popular skill pack overall. |
| Kiro | Agentic IDE (spec-driven) | https://github.com/kirodotdev/Kiro | Official (AWS) | 4.4k | IDE built around requirements, design and tasks specs. |
| AGENTS.md | Open format | https://github.com/agentsmd/agents.md | Standard | 24.9k | One project-instructions file that Codex, Cursor, Copilot and others read. |
| Notion MCP | MCP (hosted) | https://github.com/makenotion/notion-mcp-server | Official | 4.7k | Pull PRDs and research from Notion into the agent. |
| Atlassian MCP | MCP (hosted) | https://github.com/atlassian/atlassian-mcp-server | Official | 1.1k | Jira and Confluence, if requirements live there. |

**Top pick:** **Spec Kit** for greenfield work. Add **Superpowers** skills for the execution discipline (TDD, planning, subagents).
