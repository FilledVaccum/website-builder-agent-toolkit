# 15. Security review

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | Type | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **Semgrep MCP** | Built into the CLI: `semgrep mcp` | https://github.com/semgrep/semgrep/tree/develop/cli/src/semgrep/mcp | Official | 17.0k (semgrep) | SAST in the agent loop. The standalone `semgrep/mcp` repo is **archived**. |
| Claude Code Security Review | GitHub Action | https://github.com/anthropics/claude-code-security-review | Official | 6.3k | AI security review on every PR. |
| Trail of Bits skills | Skills | https://github.com/trailofbits/skills | Official (ToB) | 7.5k | Security-audit and vuln-hunting skills. |
| Socket MCP | MCP | https://github.com/SocketDev/socket-mcp | Official | 139 | Scores dependency and supply-chain risk before the agent adds a package. |
| **Snyk agent-scan** | Scanner | https://github.com/snyk/agent-scan | Official (Snyk) | 3.1k | **Scans your MCP servers and skills** for tool poisoning and prompt injection. Run it before adding community MCPs. |
| ToolHive | MCP runtime | https://github.com/stacklok/toolhive | Community/vendor | 2.3k | Runs MCP servers in isolated containers with secrets management. |
| Docker MCP Gateway | MCP runtime | https://github.com/docker/mcp-gateway | Official (Docker) | 1.6k | Containerised, curated MCP catalog behind one gateway. |
| web-check | Repo | https://github.com/lissy93/web-check | Community | 35.1k | Post-deploy OSINT check (headers, TLS, DNS, security.txt). |

**Top pick:** **Semgrep MCP** in the loop, plus **Claude Code Security Review** on PRs, plus **snyk/agent-scan** on your MCP config.
