# Stage 18: Security

> Source: free catalog (curated 2026-10-11). Tables: A = Skills, B = GitHub repos, C = Free MCP servers. See [legend](../00-legend-and-exclusions.md), [pricing](../../pricing/pricing.md).

### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Cloudflare security-audit-skill** | https://github.com/cloudflare/security-audit-skill | Official (Cloudflare) | 40.4k | 2026-09-14 | Multi-phase security audit with independently verified findings | FOSS |
| 2 | **Trail of Bits skills** | https://github.com/trailofbits/skills | Official (Trail of Bits) | 7.5k | 2026-10-09 | Vuln detection & audit workflows | FOSS |
| 3 | **security-guidance plugin** | https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance | Official | 150.2k | 2026-10-10 | Warns on risky patterns while editing | FOSS |
| 4 | **security-and-hardening** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | OWASP Top 10, secrets, auth patterns | FOSS |
| 5 | **claude-code-owasp** | https://github.com/agamm/claude-code-owasp | Community | 378 | 2026-09-25 | OWASP Top 10:2025 / ASVS 5.0 skill (niche, <1k★) | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Gitleaks** | https://github.com/gitleaks/gitleaks | OSS | 29.8k | 2026-09-30 | Secret scanning | FOSS |
| 2 | **TruffleHog** | https://github.com/trufflesecurity/trufflehog | OSS | 28.4k | 2026-10-09 | Find/verify leaked credentials | FOSS |
| 3 | **SkillSpector** | https://github.com/NVIDIA/SkillSpector | Official (NVIDIA) | 19.9k | 2026-10-10 | Scan agent skills for malicious patterns/prompt injection | FOSS |
| 4 | **Semgrep CE** | https://github.com/semgrep/semgrep | OSS | 17.0k | 2026-10-09 | SAST (also hosts the MCP) | FOSS |
| 5 | **ZAP** | https://github.com/zaproxy/zaproxy | OSS | 15.9k | 2026-10-08 | DAST web scanner | FOSS |
| 6 | **OSV-Scanner** | https://github.com/google/osv-scanner | Official (Google) | 11.2k | 2026-10-10 | Dependency vulns | FOSS |
| 7 | **Claude Code Security Review** | https://github.com/anthropics/claude-code-security-review | Official | 6.3k | 2026-02-11 | AI security review GitHub Action (quiet since Feb 2026) | FOSS (needs Anthropic API) |
| 8 | **Snyk agent-scan** | https://github.com/snyk/agent-scan | Official | 3.1k | 2026-10-09 | Scan MCP servers & skills | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Semgrep MCP (semgrep mcp)** | https://github.com/semgrep/semgrep/tree/develop/cli/src/semgrep/mcp | Official | 17.0k | 2026-10-09 | SAST scans in the agent loop (standalone semgrep/mcp repo is archived) | FOSS |
| 2 | **Socket MCP** | https://github.com/SocketDev/socket-mcp | Official | 139 | 2026-10-08 | Dependency supply-chain risk scores | Free for individuals |
| 3 | **GitHub MCP (code-scanning/secret-scanning toolsets)** | https://github.com/github/github-mcp-server | Official | 33.5k | 2026-10-08 | Read Dependabot/CodeQL/secret alerts | Free on public repos |

## 💰 Pricing: paid services in this stage (free tier → paid)

*Checked 2026-10-11 on vendor pricing pages; USD. FOSS tools are omitted (they cost $0). Recheck before buying. Full detail: [pricing](../../pricing/pricing.md).*

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Semgrep | Free tier + FOSS | Community Edition FOSS; platform free up to 10 contributors / 10 repos | Paid tiers (contact or page) | semgrep.dev/pricing |
| Snyk (+ agent-scan) | Free tier | 100 tests/mo (agent-scan itself is FOSS) | Team $25/mo | snyk.io/plans |
| Socket | Free tier | Free for individuals and small teams | Team $25/mo | socket.dev/pricing |
