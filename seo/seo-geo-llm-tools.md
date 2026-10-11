# SEO and GEO tools for LLMs

Reference list of GitHub repos, MCP servers, and agent skills for SEO and GEO (Generative Engine Optimization) with Claude Code, Cursor, Codex, and other coding agents.

Star counts are from the GitHub API on **11 October 2026**. Re-check stars before relying on popularity rankings.

GEO here means optimizing content so AI answer engines (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) crawl, understand, and cite a site. AEO (Answer Engine Optimization) and LLM SEO are the same job under other names.

## What to install

For Claude Code:

1. **GEO-first skill:** [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) — citability, crawlers, `llms.txt`, brand mentions, schema, PDF report.
2. **Full SEO + GEO audit:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) — technical SEO, E-E-A-T, schema, local, ecommerce. Runs without a paid data vendor.
3. **Live keyword, rank, and Search Console data:** [every-app/open-seo](https://github.com/every-app/open-seo) (all-in-one hosted MCP) or [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) (Google's own API only).

For Cursor:

```bash
npx skills add aaron-he-zhu/aaron-marketing-skills
npx skills add every-app/open-seo
```

Then connect an MCP server for live data. Skills tell the agent the workflow. MCP gives it real numbers.

## Skills people actually install

These are the high-star agent skill packs. Several are prompt workflows (`SKILL.md`) rather than a local crawler. Hosted products in this list ship a remote MCP plus skills.

| Repo | Stars | Forks | Created | Last push | What it is |
|---|---:|---:|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 54,160 | 8,041 | 2026-01-15 | 2026-10-08 | Default marketing skill pack for Claude Code. SEO is one part of CRO, copy, analytics, and growth. |
| [every-app/open-seo](https://github.com/every-app/open-seo) | 23,036 | 3,013 | 2026-02-27 | 2026-10-08 | Open-source Semrush/Ahrefs-style platform: keywords, ranks, backlinks, audits, AI visibility. MCP at `https://app.openseo.so/mcp`. Pay-as-you-go hosted app; the repo is the agent layer. |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 18,686 | — | 2026-02-07 | 2026-10-04 | Dedicated SEO + GEO Claude Code plugin. 26 sub-skills, 19 sub-agents. MIT. Homepage: https://claude-seo.md |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 10,995 | 1,675 | 2026-02-18 | 2026-10-11 | GEO-first skill. Citability scoring, AI crawler analysis, brand authority, schema, platform-specific optimization, PDF reports. |
| [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) | 4,747 | 366 | 2026-08-29 | 2026-09-24 | Skills plus a remote MCP (`https://connector.get-ryze.ai/mcp`) over Search Console, GA4, and ads. Keyword research, rank tracking, backlinks, AI visibility. MIT. Grew very fast after launch. |
| [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) | 4,123 | 551 | 2026-01-21 | 2026-09-24 | 49 marketing skills for Claude Code and claude.ai (Google Ads, Meta Ads, SEO, AI visibility). Same Ryze data path. |
| [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) | 3,917 | 495 | 2026-03-27 | 2026-10-09 | 45 skills. SEO and GEO plus ads and analytics, with an MCP login. |
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | 3,787 | 856 | 2026-04-13 | 2026-10-11 | GEO content platform: write, inspect, and distribute content across sites. |
| [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) | 2,901 | 371 | 2025-12-18 | 2026-10-11 | 120 skills, 16 of them SEO/GEO. Portable install via `npx skills`. Entrypoint `/aaron-marketing:seo-geo`. |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | 2,733 | — | — | 2026-03-02 | AI marketing suite for Claude Code. 15 skills with parallel subagents. Older companion to geo-seo-claude. |
| [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog) | 2,357 | — | — | 2026-10-09 | Blog skill suite, dual-optimized for search and AI citation. Companion to claude-seo. |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | 1,321 | — | — | 2026-06-07 | Claude Code skill for AEO and GEO. |
| [gooseworks-ai/goose-skills](https://github.com/gooseworks-ai/goose-skills) | 1,242 | — | — | 2026-10-10 | Growth and GTM skills plus data APIs for Claude Code, Codex, and Cursor. |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | 1,036 | — | — | 2026-10-10 | CLI + Python + MCP + Astro. Scores crawlability, `llms.txt`, JSON-LD, and citability. MIT. |
| [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | 1,028 | — | — | 2026-10-06 | 160+ marketing skills covering SEO, social, and content. |
| [yaojingang/yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) | 871 | — | — | 2026-10-01 | GEO skill collection. Homepage: https://yaojingang.github.io/yao-geo-skills/ |
| [AgriciDaniel/codex-seo](https://github.com/AgriciDaniel/codex-seo) | 803 | — | — | 2026-09-11 | Codex-first SEO skill suite. 26 workflows, DataForSEO / Gemini / Google / Firecrawl, GEO. |
| [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) | 963 | — | — | 2026-07-23 | LLM-first SEO skill for Antigravity, Codex, and Claude. 16 sub-skills, 10 agents. |
| [rampstackco/claude-skills](https://github.com/rampstackco/claude-skills) | 947 | — | — | 2026-10-07 | Stack-agnostic skills for the website lifecycle, including SEO. |
| [indranilbanerjee/digital-marketing-pro](https://github.com/indranilbanerjee/digital-marketing-pro) | 864 | — | — | 2026-10-11 | Marketing OS covering strategy, SEO, AEO/GEO, paid, content, CRM. |
| [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) | 765 | — | — | 2026-06-17 | SEO audit skill for OpenClaw, Claude Code, and other agents. |
| [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills) | 714 | — | — | 2026-10-11 | 77 marketing skills including SEO. |
| [leopard627/fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) | 714 | — | — | 2026-09-25 | Claude Code skill for SEO, AEO, GEO, and Naver. |
| [tigerless-labs/seo-ops](https://github.com/tigerless-labs/seo-ops) | 702 | — | — | 2026-09-01 | Crawler's-eye pass/fail report from a URL. 26 checks. |
| [unifapi-agent/agents](https://github.com/unifapi-agent/agents) | 589 | — | — | 2026-09-05 | Marketing agents plugin: SEO audits and GEO / AI visibility. |
| [mykpono/ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) | 88 | — | — | 2026-10-01 | `AGENTS.md` skill. Works in Claude Code, Cursor, Codex, Copilot, Windsurf. Audit, plan, execute. |

The old standalone repo [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (216 stars) is a signpost. New installs come from `aaron-marketing-skills`. The old 20-skill line is frozen at tag `v9.9.12`.

## MCP servers that return real data

Skills describe the workflow. These servers are what an agent queries for numbers.

| Repo | Stars | Created | Last push | Data |
|---|---:|---|---|---|
| [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | 7,583 | 2024-12-06 | 2026-10-09 | Official Firecrawl MCP. Page fetch and search. Not an SEO product; most SEO agents use it to read pages and SERPs. |
| [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) | 1,898 | 2025-03-14 | 2026-09-15 | Google Search Console. The most-used SEO-specific MCP. |
| [iannuttall/seo](https://github.com/iannuttall/seo) | 568 | 2026-07-10 | 2026-09-27 | Local CLI + MCP. Own crawl, Search Console, and GA4. About 70 audit tools. |
| [avansaber/seo-monster](https://github.com/avansaber/seo-monster) | 539 | 2026-05-28 | 2026-10-04 | Local MCP over Search Console, GA4, PageSpeed Insights, and Cloudflare. Uses your credentials. |
| [dataforseo/mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript) | 252 | 2025-04-10 | 2026-10-02 | Official DataForSEO MCP: SERP, keywords, backlinks, on-page. Paid API. |
| [AKzar1el/mcp-geo](https://github.com/akzar1el/mcp-geo) | 37 | — | 2026-09-24 | AI visibility tracker MCP. Queries ChatGPT, Claude, Perplexity, Gemini, and Google AI Overviews. Needs API keys. Can self-host on Cloudflare Workers. |
| [ahrefs/ahrefs-mcp-server](https://github.com/ahrefs/ahrefs-mcp-server) | 101 | 2025-04-25 | 2026-02-19 | Official Ahrefs MCP. Stale as of this note. |
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 470 | — | 2026-09-26 | 18 Google Maps tools and 3 skills for local SEO. |

Hosted MCPs (account required, not fully local):

- OpenSEO: `https://app.openseo.so/mcp` — keywords, SERP, backlinks, rank tracking, Search Console, AI visibility.
- Ryze: `https://connector.get-ryze.ai/mcp` — Search Console, GA4, ads, DataForSEO.
- NotFair: OAuth MCP bundled with the plugin — Search Console, analytics, ads.

## GEO products

Separate from skill packs. These track citations or run a GEO workflow as a product.

| Repo | Stars | Last push | What it does |
|---|---:|---|---|
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | 3,787 | 2026-10-11 | Content engineering and multi-site distribution. |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | 1,036 | 2026-10-10 | Scores whether AI engines can crawl and cite a site. CLI, library, MCP. |
| [aigclink/geolook](https://github.com/aigclink/geolook) | 760 | 2026-08-10 | Diagnosis through tickets, execution, and verification. |
| [jianruntech/geo-score](https://github.com/jianruntech/geo-score) | 521 | 2026-10-11 | 0–100 readiness score plus ask-and-check against engines. |
| [yaojingang/GEORank](https://github.com/yaojingang/GEORank) | 492 | 2026-09-16 | GEO ranking platform. |
| [ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) | 484 | 2026-09-28 | GetCito. Open-source AI-search visibility tracker. |
| [elmohq/elmo](https://github.com/elmohq/elmo) | 428 | 2026-10-11 | Tracks citations in ChatGPT, Claude, Perplexity, Gemini. Created 2025-08-29. |
| [usenotra/notra](https://github.com/usenotra/notra) | 260 | 2026-10-11 | Asks buyer questions to ChatGPT, Claude, and Gemini and records who gets cited. |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | 224 | 2026-06-14 | ICLR 2026 research. Learns what generative engines prefer and rewrites pages. |
| [mverab/eGEOagents](https://github.com/mverab/eGEOagents) | 199 | 2026-10-09 | CLI + Claude Code skills. Audit, ranking simulation, rewrite, competitor comparison. MIT. Based on published GEO research. |
| [rubenmarcus/aeo.js](https://github.com/rubenmarcus/aeo.js) | 142 | 2026-10-06 | AEO library for making a site discoverable by ChatGPT, Claude, and Perplexity. |
| [dodopayments/dualmark](https://github.com/dodopayments/dualmark) | 108 | 2026-09-15 | Markdown twins of pages so AI crawlers get a clean version. |
| [AI2HU/gego](https://github.com/AI2HU/gego) | 103 | 2026-07-23 | Brand GEO tracking across LLMs. |

Curated lists (not tools):

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) — 520 stars
- [GEO-optim/GEO](https://github.com/GEO-optim/GEO) — 339 stars, Apache-2.0. Original Princeton / Georgia Tech KDD 2024 paper code. Last push 2025-10-30. Reference, not a product.
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) — 130 stars
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) — 124 stars
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) — 117 stars

## Crawlers

| Repo | Stars | Last push | Notes |
|---|---:|---|---|
| [PhialsBasement/LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) | 1,020 | 2026-09-29 | Desktop SEO crawler. Open-source Screaming Frog alternative. |
| [crawlseo/crawlseo](https://github.com/crawlseo/crawlseo) | 630 | 2026-10-06 | GSC + site crawler + Core Web Vitals dashboard. |
| [lokoe-mehdi/scouter](https://github.com/lokoe-mehdi/scouter) | 74 | 2026-08-10 | Self-hosted web crawler with an MCP server. JS rendering, duplicates, internal PageRank. |
| [Shantodotdev/blacksparrow](https://github.com/Shantodotdev/blacksparrow) | 6 | 2026-10-08 | Rust crawler, ~120 technical rules, `llms.txt` and AI-bot checks, native MCP. Very new. |
| [zagi/arachnit-crawler](https://github.com/zagi/arachnit-crawler) | — | — | Self-hosted crawler with optional local LLM analysis and pgvector near-duplicate detection. |

## Smaller GEO skills worth knowing

Lower stars. Overlap with the packs above. Useful if a specific workflow matches.

| Repo | Stars | Last push | Notes |
|---|---:|---|---|
| [TheSmokeDev/geo-skills](https://github.com/TheSmokeDev/geo-skills) | 27 | 2026-09-03 | Local GEO score (0–100) for Claude Code and Codex. No paid API. |
| [seoskillsai/seo-skills-ai](https://github.com/seoskillsai/seo-skills-ai) | 21 | 2026-10-08 | 27 sub-skills, Python audit engine, optional DataForSEO and Firecrawl. |
| [vishalmdi/goog-geo](https://github.com/vishalmdi/goog-geo) | 11 | 2026-05-18 | Claude skill scored against Google's AI optimization guide. |
| [Ch1nyzzz/AgentGEO](https://github.com/Ch1nyzzz/AgentGEO) | 5 | 2026-07-27 | Autonomous rewrite loop with 11 registered tools. Research-style. |
| [nickllama/claude-skill-seo-geo-optimizer](https://github.com/nickllama/claude-skill-seo-geo-optimizer) | 0 | 2026-06-14 | SEO + GEO + AEO audit skill. Notes that 2026 studies did not reproduce the original Princeton percentage lifts. |
| [kubical-ai/aeo-geo-optimization](https://github.com/kubical-ai/aeo-geo-optimization) | 1 | 2026-03-05 | 29-signal docs audit with approve-each-change workflow. |

Also useful as a spec, not a tool: [jdevalk/specification.website](https://github.com/jdevalk/specification.website) (875 stars, updated 2026-10-11). Platform-agnostic website spec covering HTML, accessibility, security, SEO, and agent-readiness.

## Install notes

### claude-seo (Claude Code)

Public MIT repo. There is also a private community mirror at `AI-Marketing-Hub/claude-seo` that requires membership. Use the public repo.

```text
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel
```

Commands: `/seo audit <url>`, `/seo geo <url>`, `/seo technical`, `/seo schema`, `/seo content`, `/seo page`.

Optional paid extensions: DataForSEO, Firecrawl, Banana. The core audit runs without them. The `seo-geo` skill treats `llms.txt` as present-or-missing and does not treat it as a proven citation ranking lever.

### geo-seo-claude

```text
/geo audit <url>
/geo quick <url>
/geo citability <url>
/geo crawlers <url>
/geo llmstxt <url>
/geo brands <url>
/geo schema <url>
/geo report <url>
```

### OpenSEO

Preferred on Claude Code: one plugin install adds MCP and skills.

```text
/plugin marketplace add every-app/open-seo
/plugin install openseo@openseo
```

MCP only: `https://app.openseo.so/mcp`

Skills for Cursor and other agents:

```bash
npx skills add every-app/open-seo
```

Workflows include `seo-project-setup`, `keyword-research`, `keyword-clustering`, `competitive-landscape`, `competitor-analysis`, `link-prospecting`, `local-seo`, `seo-audit`, AI visibility audit, and AI prompt research.

### Ryze

```text
claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp
claude plugin marketplace add Ryze-AI-Adgent/open-seo-mcp-skills
claude plugin install open-seo-mcp-skills@ryze
```

Skills: `seo-audit`, `keyword-research`, `rank-tracking`, `competitor-gap`, `backlink-check`, `ai-visibility`, `seo-vs-ads`.

### NotFair

```text
/plugin marketplace add nowork-studio/notfair-plugin
/plugin install notfair@nowork-studio
```

```text
/notfair:seo-analysis
/notfair:geo-optimizer
/notfair:search-console
/notfair:google-analytics
```

Codex:

```bash
codex plugin marketplace add nowork-studio/notfair-plugin --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

### aaron-marketing-skills (Cursor and 70+ hosts)

```bash
npx skills add aaron-he-zhu/aaron-marketing-skills
npx skills add aaron-he-zhu/aaron-marketing-skills -s keyword-research
```

Claude Code:

```text
/plugin marketplace add aaron-he-zhu/aaron-marketing-skills
/plugin install aaron-marketing@aaron
```

## How the layers fit

1. **Skill** — tells the agent the audit or rewrite procedure. Best defaults: `geo-seo-claude` for GEO, `claude-seo` for full SEO.
2. **MCP** — live data. `mcp-gsc` for Search Console only. OpenSEO or Ryze when you want keywords, ranks, and backlinks.
3. **Scraper** — Firecrawl MCP when the agent needs to read pages.
4. **Crawler** — LibreCrawl or Scouter when a one-page skill audit is not enough.
5. **Citation tracker** — Elmo, Notra, GetCito, or `mcp-geo` when the question is "did the model cite us," not "is the page well structured."
6. **Research code** — `GEO-optim/GEO` and `cxcscmu/AutoGEO` explain the methods. They are not the tools to install in an agent.

## Caveats

- Star counts in this file are a snapshot from 11 October 2026. Several repos (especially Ryze and OpenSEO) gained stars very quickly after launch. Popularity is real in the agent-skill scene; it is not the same as a mature crawler.
- A high-star skill pack is mostly instructions. It will invent numbers unless an MCP or API is connected.
- Google's own AI optimization guidance treats AI Overviews as the same ranking system as classic Search. Pages still need to be indexed and eligible for snippets. `claude-seo` follows that and down-weights `llms.txt` as a citation lever.
- The original Princeton GEO paper's specific percentage lifts were not reproduced by 2026 follow-up studies. Direction of the tactics (statistics, named sources, clear answer blocks) still holds. Passage-level answer blocks around 134–167 words show up in several of these skills.
