# 13. Monitoring, analytics, error tracking

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Service | MCP | URL | Official? | Notes |
|---|---|---|---|---|
| **Sentry** | Hosted `https://mcp.sentry.dev/mcp`; stdio `npx @sentry/mcp-server` | https://github.com/getsentry/sentry-mcp (now redirects to `getsentry/toolkit`, 924★) | Official | Agent gets issues and stack traces → fix. Free dev tier. |
| **PostHog** | Hosted `https://mcp.posthog.com/mcp` (`npx @posthog/wizard mcp add`; `?readonly=true`, `?features=`) | https://posthog.com/docs/model-context-protocol · code in https://github.com/PostHog/posthog/tree/master/services/mcp | Official | Product analytics, flags, session replay, errors, experiments. Large free tier. The old `PostHog/mcp` repo is **archived**. |
| Umami | Official `@umami/mcp` (in the main repo) | https://docs.umami.is/docs/mcp · https://github.com/umami-software/umami (39.3k) | Official | Privacy-first, self-hostable, cookie-free analytics. |
| Plausible | **Community** MCP by the Sentry team | https://github.com/getsentry/plausible-mcp · https://github.com/plausible/analytics (29.4k) | Community | Privacy analytics. Paid cloud or free self-host. |
| Vercel Web Analytics | Through the Vercel MCP | (above) | Official | — |
| Google Analytics | MCP | https://github.com/googleanalytics/google-analytics-mcp (3.4k) | Official (Google) | GA4 Data/Admin API. |
| Grafana | MCP | https://github.com/grafana/mcp-grafana (3.5k) | Official | If you self-host observability. |

**Top pick:** **Sentry MCP** for errors, plus **PostHog MCP** for analytics (or **Umami** if you want it privacy-first and self-hosted).
