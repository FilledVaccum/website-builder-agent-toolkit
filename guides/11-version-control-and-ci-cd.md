# 11. Version control and CI/CD

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | Type | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **GitHub MCP** | MCP (hosted + local) | https://github.com/github/github-mcp-server | Official | 33.5k | Repos, PRs, issues, Actions. Use toolsets to cut tool count. |
| Claude Code Action | GitHub Action | https://github.com/anthropics/claude-code-action | Official | 9.5k | `@claude` in PRs and issues; automated reviews and fixes. |
| GitLab MCP | Built-in MCP `https://<gitlab>/api/v4/mcp` | https://docs.gitlab.com/user/model_context_protocol/mcp_server/ | Official | — | OAuth DCR, toolset headers. |
| MCP reference servers (git, filesystem, fetch, memory, sequential-thinking) | MCP | https://github.com/modelcontextprotocol/servers | Official (MCP) | 91.1k | Reference implementations. Fine for local git operations. |

**Top pick:** **GitHub MCP** (or just the `gh` CLI; agents handle it well and it costs no context) plus **Claude Code Action** for PR automation.
