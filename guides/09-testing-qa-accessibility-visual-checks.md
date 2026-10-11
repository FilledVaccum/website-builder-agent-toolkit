# 9. Testing, QA, accessibility, visual checks

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Playwright MCP** | MCP | https://github.com/microsoft/playwright-mcp | Official (Microsoft) | 38.0k | Drives the browser through accessibility snapshots, which is deterministic and token-efficient. Use it to write and verify E2E tests. |
| **Chrome DevTools MCP** | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Official (Google) | 53.3k | Console, network, perf traces, screenshots, **`lighthouse_audit`** (a11y, SEO, best practices). Use `--slim`. Usage stats are on by default (`--no-usage-statistics`). |
| browser-use | Repo | https://github.com/browser-use/browser-use | Community | 118k | Autonomous browser agent for exploratory QA. |
| executeautomation mcp-playwright | MCP | https://github.com/executeautomation/mcp-playwright | Community | 5.7k | Older Playwright MCP (last push Dec 2025). Prefer Microsoft's. |
| BrowserStack MCP | MCP | https://github.com/browserstack/mcp-server | Official | 154 | Real devices and cross-browser runs, plus a11y. |
| mcp-accessibility-scanner | MCP | https://github.com/JustasMonkev/mcp-accessibility-scanner | Community | 57 | axe-core audits through MCP. |
| Anthropic `webapp-testing` skill | Skill | https://github.com/anthropics/skills | Official | 180k | Playwright-based test-your-own-app skill. |

**Top pick:** **Playwright MCP** for function, plus **Chrome DevTools MCP** for debugging, performance and Lighthouse. Pick one as the default so you don't load both browser tool sets.
