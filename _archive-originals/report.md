# Building a complete website end to end with AI agents: MCP servers, skills, and repos by stage

*Researched Oct 11, 2026 (MYT) for Swap. Indie / solo-dev focus.*
*Star counts come from the GitHub search API on 2026-10-11 and are rounded. "Official" means the vendor maintains it. Remote MCP endpoints were checked against vendor docs. I left out anything I couldn't confirm.*

---

## 0. How to read this report (the first-principles view)

An agent building a website needs four kinds of help. Every item below fits one of them:

| Kind | What it gives the agent | Examples | Cost to the context window |
|---|---|---|---|
| **Knowledge** | Current docs and APIs, so it stops guessing from stale training data | Context7, Astro Docs MCP, Clerk MCP, `@shopify/dev-mcp` | Low |
| **Method** | How to do the job well: process and taste | spec-kit, Superpowers, `frontend-design`, ui-ux-pro-max, impeccable | Very low. Skills load on demand. |
| **Eyes** | It can see and check what it built | Playwright MCP, Chrome DevTools MCP | Medium |
| **Hands** | It can change real infrastructure: DB, deploys, payments, DNS | Supabase, Vercel, Stripe, Cloudflare MCPs | High, and **risky** |

**Opinionated rule:** use skills for *method*, docs MCPs for *knowledge*, one browser MCP for *eyes*, and as few *hands* MCPs as you can (scoped or read-only where possible). Most production damage from agents comes through the "hands" servers.

**What changed in 2025–2026:** most vendors replaced local `npx` servers with **hosted remote MCP servers that use OAuth** (`https://mcp.<vendor>.com/mcp`). Several well-known repos are now **archived** because the hosted endpoint took over (Browserbase, PostHog, Sanity, Railway, Semgrep, Prisma's standalone repo, ElevenLabs, Penpot, Ahrefs, Automattic's WordPress MCP, Storybook). Old blog posts and "awesome" lists still point at those dead installs.

---

## 1. Discovery, requirements and planning (PRD, spec-driven development, task breakdown)

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

---

## 2. Research: competitors and content inspiration (scraping, crawling, search)

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Firecrawl MCP** | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Official | 7.6k | Scrape, crawl, map, search and extract any site as LLM-ready markdown. Free tier is limited credits. |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Official | 5.1k | Neural web search plus crawl. Good for finding competitors. |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Official | 2.4k | Search, extract, map and crawl. Generous free credits. |
| Apify MCP | MCP | https://github.com/apify/apify-mcp-server | Official | 10.5k | Thousands of ready-made scrapers ("Actors") for social, maps and e-commerce. |
| Bright Data MCP | MCP | https://github.com/brightdata/brightdata-mcp | Official | 2.7k | Web access that gets past blocks (proxies, unblocker). |
| Crawl4AI | Repo (self-host) | https://github.com/unclecode/crawl4ai | Community (OSS) | 85.2k | Free, self-hosted crawler that outputs markdown. The cheap option. |
| Browserbase MCP | MCP (hosted only) | https://mcp.browserbase.com/mcp (repo archived: https://github.com/browserbase/mcp-server-browserbase) | Official | 3.4k (archived) | Cloud browsers. **The self-host repo was archived in Jul 2026; use the hosted endpoint.** |
| Stagehand | Repo / SDK | https://github.com/browserbase/stagehand | Official | 25.6k | AI browser automation SDK (act, extract, observe). |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Official (Microsoft) | 38.0k | Browse competitor sites through the accessibility tree (also used in stage 9). |
| Open Lovable | Repo | https://github.com/firecrawl/open-lovable | Official (Firecrawl) | 28.7k | Clones any site into a React app. A strong starting point. |

**Top pick:** **Firecrawl MCP** for hosted scraping. **Crawl4AI** if you want it free and self-hosted.

---

## 3. UX/UI design and design systems

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Figma MCP (remote)** | MCP (hosted, OAuth) | https://developers.figma.com/docs/figma-mcp-server/ · endpoint `https://mcp.figma.com/mcp` · guide repo https://github.com/figma/mcp-server-guide | Official | guide 2.1k | Design-to-code context. The remote server also **writes to the canvas** (`use_figma`, `generate_figma_design`, code-to-canvas). Remote works on all seats; the desktop server needs a Dev/Full seat. |
| Framelink (Figma-Context-MCP) | MCP | https://github.com/GLips/Figma-Context-MCP | Community | 16.0k | Popular Figma-to-layout MCP that only needs a personal token. |
| shadcn/ui MCP | MCP (built into the shadcn CLI) | https://ui.shadcn.com/docs/mcp · repo https://github.com/shadcn-ui/ui | Official | 125k | Browse, search and install components from shadcn and any registry with natural language. |
| shadcn-ui-mcp-server | MCP | https://github.com/Jpisnice/shadcn-ui-mcp-server | Community | 3.0k | shadcn context for React, Svelte, Vue and React Native. |
| 21st.dev Magic MCP | MCP | https://github.com/21st-dev/magic-mcp | Official (21st.dev) | 6.0k | "v0 inside your IDE." Searches 10k+ React/Tailwind components and generates UI. Paid tiers. |
| Magic UI MCP | MCP | https://github.com/magicuidesign/mcp | Official | 206 | Animated Magic UI components. |
| Canva MCP | MCP (hosted) | https://www.canva.dev/docs/mcp/ | Official | n/a | Generate and edit Canva designs: social images, OG images, decks. |
| **frontend-design skill** | Skill | https://github.com/anthropics/skills · plugin https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design | Official (Anthropic) | 180k / 150k | Picks a bold, intentional visual direction before writing code. Counters the generic "AI slop" look. |
| UI UX Pro Max | Skill | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community | 135k | Design-system generator (styles, palettes, font pairings, UX rules) for many stacks. |
| Taste Skill | Skill | https://github.com/Leonxlnx/taste-skill | Community | 94.6k | Stronger visual personality, less generic output. |
| Impeccable | Skill pack | https://github.com/pbakaus/impeccable | Community | 79.7k | Design vocabulary plus critique, audit and polish commands for existing UIs. |
| Vercel `web-design-guidelines` | Skill | https://github.com/vercel-labs/agent-skills | Official (Vercel) | 32.2k | Reviews UI against Vercel's accessibility and UX guidelines. |
| Penpot | OSS design tool | https://github.com/penpot/penpot | Official | 60.9k | Free Figma alternative. Its standalone `penpot-mcp` repo is **archived**. |
| Onlook | Repo | https://github.com/onlook-dev/onlook | Community (OSS) | 26.9k | Visual editor that edits your React code directly. |

**Top pick:** **Figma remote MCP** if a design exists. If not, use the **frontend-design skill** plus **shadcn/ui MCP** (cheapest path to a site that doesn't look generic).

---

## 4. Assets: images, icons, fonts, video and audio

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Replicate MCP** | MCP (hosted + `npx replicate-mcp`) | https://replicate.com/docs/reference/mcp | Official | n/a | Run any image or video model (FLUX etc.) for hero images, illustrations and backgrounds. Pay per use. |
| fal MCP server | MCP | https://github.com/raveenb/fal-mcp-server | Community | — | 600+ fal.ai models. There is no official fal MCP. |
| Canva MCP | MCP | https://www.canva.dev/docs/mcp/ | Official | — | Branded graphics and OG images. |
| Unsplash MCP | MCP | https://github.com/hellokaton/unsplash-mcp-server | Community | 237 | Search free stock photos. |
| Iconify MCP | MCP | https://github.com/imjac0b/iconify-mcp-server | Community | 19 | Search 200k+ icons. Small project; check it before you trust it. |
| Lucide | Icon library | https://github.com/lucide-icons/lucide | OSS | 24.9k | Default icon set for shadcn. Agents already know it well, so no MCP is needed. |
| ElevenLabs MCP | MCP | https://github.com/elevenlabs/elevenlabs-mcp | Official | 1.5k (**archived**) | TTS and voiceovers. The repo is archived; ElevenLabs now ships its MCP through its platform. |

**Top pick:** **Replicate MCP** for generated imagery. For icons and fonts, Lucide plus Google Fonts work without any MCP; agents know them.

---

## 5. Frontend scaffolding and code generation (plus docs-grounding)

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Context7** | MCP | https://github.com/upstash/context7 | Official (Upstash) | 62.9k | Pulls current, version-specific docs for thousands of libraries into the prompt. Fixes hallucinated APIs. |
| Ref | MCP | https://github.com/ref-tools/ref-tools-mcp | Official (Ref) | 1.2k | Token-efficient docs search over public and private docs. |
| Next.js DevTools MCP | MCP | https://github.com/vercel/next-devtools-mcp | Official (Vercel) | 826 | Next.js docs, upgrades, and runtime errors and routes from the dev server. |
| Astro Docs MCP | MCP (hosted) | https://docs.astro.build/en/guides/build-with-ai/ · `https://mcp.docs.astro.build/mcp` | Official | — | Current Astro docs. Astro is the best framework for content and marketing sites. |
| Svelte MCP | MCP | https://svelte.dev/docs/mcp (GitHub `sveltejs/mcp` redirects to a renamed repo) | Official | — | Svelte 5 docs plus an autofixer. |
| Vercel agent-skills | Skills | https://github.com/vercel-labs/agent-skills | Official | 32.2k | `react-best-practices`, `composition-patterns`, `react-view-transitions`, `vercel-optimize`, `vercel-deploy-claimable`. |
| `npx skills` (skills.sh) | Skill installer | https://github.com/vercel-labs/skills | Official (Vercel) | 33.8k | Installs SKILL.md packs into any agent (Claude Code, Cursor, Codex and others). |
| create-t3-app | Starter | https://github.com/t3-oss/create-t3-app | Community | 29.2k | Typesafe Next.js + tRPC + Prisma/Drizzle + Auth.js. |
| create-better-t-stack | Starter CLI | https://github.com/AmanVarshney01/create-better-t-stack | Community | 5.8k | Pick-your-stack TS scaffolder (Next, TanStack, Hono, Drizzle, Better Auth, Convex and more). |

**Top pick:** **Context7**, the most effective single MCP for code quality. Pair it with the framework's own docs MCP (Next DevTools or Astro Docs).

---

## 6. Backend, database and auth (indie BaaS landscape)

### 6a. Backend-as-a-service and databases

| Service | MCP / skill | URL | Official? | Notes (free tier: check current pricing) |
|---|---|---|---|---|
| **Supabase** | Hosted MCP `https://mcp.supabase.com/mcp` (+ `?read_only=true&project_ref=`) · skills | https://supabase.com/docs/guides/getting-started/mcp · https://github.com/supabase-community/supabase-mcp · skills https://github.com/supabase/agent-skills (2.7k) | Official | Postgres + Auth + Storage + Realtime + Edge Functions. Free projects pause when inactive. The default indie choice. |
| Firebase | MCP built into the CLI (`npx firebase-tools@latest mcp`) | https://firebase.google.com/docs/ai-assistance/mcp-server | Official | Spark (free) plan. Firestore, Auth, Hosting. |
| Appwrite | Hosted MCP `https://mcp.appwrite.io/` (OAuth); self-hosted: `uvx mcp-server-appwrite` | https://appwrite.io/docs/tooling/ai/mcp-servers | Official | OSS BaaS you can self-host. The docs MCP is now merged into the main MCP. |
| PocketBase | Community MCPs only (e.g. `mrwyndham/pocketbase-mcp`) | https://github.com/pocketbase/pocketbase (61.4k) | Community MCP | Single Go binary backend. Cheapest option when self-hosted. |
| Convex | MCP built into the CLI (`npx convex@latest mcp start`) · skills | https://docs.convex.dev/ai/convex-mcp-server · https://github.com/get-convex/agent-skills | Official | Reactive TS backend. Production access is disabled by default, which is a sensible default. |
| Neon | Hosted MCP `https://mcp.neon.tech/mcp` · skills | https://neon.com/docs/ai/neon-mcp-server · https://github.com/neondatabase/mcp-server-neon · https://github.com/neondatabase/agent-skills | Official | Serverless Postgres with branching. Free tier scales to zero. |
| Turso | Hosted MCP `https://mcp.turso.ai/mcp`; local `tursodb --mcp` | https://docs.turso.tech/integrations/mcp | Official | SQLite at the edge. Generous free tier. |
| PlanetScale | Hosted MCP `https://mcp.pscale.dev/mcp/planetscale` | https://planetscale.com/docs/mcp-server | Official | MySQL/Vitess + Postgres. No free hobby tier anymore. |
| Prisma | `npx prisma mcp` (local) + hosted `https://mcp.prisma.io/mcp` | https://www.prisma.io/blog/announcing-prisma-s-mcp-server-vibe-code-with-prisma-postgres (standalone repo `prisma/mcp` **archived**) | Official | ORM + Prisma Postgres. |
| MongoDB | MCP | https://github.com/mongodb-js/mongodb-mcp-server (1.1k) | Official | Atlas has a free M0 cluster. |
| Upstash | MCP | https://github.com/upstash/mcp-server | Official | Redis/QStash. Free tier. |
| Nhost | `nhost/mcp-nhost` is **archived** | https://github.com/nhost/mcp-nhost | — | Don't rely on it. |
| Xata | No MCP verified | https://github.com/xataio/xata (1.1k) | — | Xata's open-source Postgres platform. |

### 6b. Auth

| Service | MCP / skill | URL | Official? | Notes |
|---|---|---|---|---|
| **Better Auth** | Docs MCP `https://mcp.better-auth.com/mcp` (`npx auth@latest mcp --cursor`) + `@better-auth/mcp` plugin (makes your app an OAuth provider for MCP) | https://better-auth.com/docs/ai-resources/mcp · https://github.com/better-auth/better-auth (30.3k) | Official | Free and self-owned (a library, not a SaaS). The current indie favourite. |
| Clerk | Hosted MCP `https://mcp.clerk.com/mcp` (SDK snippets; beta) + `@clerk/mcp-tools` | https://clerk.com/docs/guides/ai/mcp/clerk-mcp-server | Official | Fastest drop-in UI. Has a free tier. |
| Auth.js (NextAuth) | No MCP | https://github.com/nextauthjs/next-auth (28.4k) | — | Still works, but momentum moved to Better Auth. |
| Kinde | Management MCP `https://<biz>.kinde.com/mcp` | https://docs.kinde.com/mcp-servers/ | Official | Auth + feature flags + billing. |
| Supabase Auth / Firebase Auth | Through their MCPs | see above | Official | Use whatever comes with your BaaS. |

**Top pick:** **Supabase hosted MCP** (scoped with `project_ref` and `read_only=true` by default) plus Supabase agent-skills. For auth outside Supabase: **Better Auth**.

---

## 7. CMS and content

| Name | MCP | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **Sanity** | Hosted `https://mcp.sanity.io` (`npx sanity@latest mcp configure`) | https://www.sanity.io/docs/ai/mcp-server | Official | — | The old repo `sanity-io/sanity-mcp-server` is **archived** in favour of the remote server. |
| Payload | `@payloadcms/plugin-mcp` → `/api/mcp` | https://payloadcms.com/docs/plugins/mcp · https://github.com/payloadcms/payload | Official | 45.2k | Lives inside your Next.js app. Self-hosted and free. Respects access control. |
| Strapi | Built-in MCP (v5.47+, GA in v5.49) at `/mcp` | https://docs.strapi.io/cms/features/strapi-mcp-server · https://github.com/strapi/strapi | Official | 73.3k | Admin-token permissions limit which tools appear. |
| Contentful | MCP | https://github.com/contentful/contentful-mcp-server | Official | 61 | Management API. |
| WordPress | MCP Adapter (Abilities API) | https://github.com/WordPress/mcp-adapter | Official | 1.8k | `Automattic/wordpress-mcp` is **archived/deprecated** in favour of this. |
| Webflow | MCP | https://github.com/webflow/mcp-server | Official | 141 | Data API + Designer. |
| Directus | MCP | https://github.com/directus/mcp | Official | 86 | Self-hostable headless CMS. |
| TinaCMS | No MCP verified | https://github.com/tinacms/tinacms | OSS | 13.8k | Git-backed markdown CMS. Agents can edit the markdown directly. |

**Top pick:** For a marketing or content site, use **markdown/MDX in Git with Astro** (no CMS, so no MCP needed). Once non-developers edit content, use **Sanity remote MCP**. If you want it self-hosted inside Next.js, use **Payload**.

---

## 8. Payments and e-commerce

| Service | MCP | URL | Official? | Notes |
|---|---|---|---|---|
| **Stripe** | Hosted `https://mcp.stripe.com` (OAuth or restricted key) | https://docs.stripe.com/mcp · repo https://github.com/stripe/ai (1.9k; former `agent-toolkit`) | Official | Use restricted keys and test mode. The MCP includes docs search. |
| **Polar** | Hosted `https://mcp.polar.sh/mcp/polar-mcp` (+ `/polar-sandbox`) | https://polar.sh/docs/integrate/mcp · https://github.com/polarsource/polar (10.4k) | Official | Merchant of Record (handles global tax) built for devs and indies. OSS. |
| Paddle | Hosted `https://mcp.paddle.com/mcp` + sandbox + Docs MCP | https://developer.paddle.com/sdks/ai/paddle-mcp · https://github.com/PaddleHQ/paddle-mcp-server | Official | MoR. Code-mode `search`/`execute` tools. |
| Lemon Squeezy | **No official MCP.** Community ones only (e.g. `atharvagupta2003/mcp-lemonsqueezy`) | https://github.com/lmsqueezy/lemonsqueezy.js | Community | Acquired by Stripe; the SDK hasn't been pushed since Nov 2024. Avoid it for new projects. |
| PayPal | MCP / agent toolkit | https://github.com/paypal/agent-toolkit | Official | — |
| Square | MCP | https://github.com/square/square-mcp-server | Official | — |
| Shopify | Dev MCP `npx -y @shopify/dev-mcp@latest` + AI Toolkit plugin | https://www.npmjs.com/package/@shopify/dev-mcp · https://github.com/Shopify/Shopify-AI-Toolkit | Official | Docs, GraphQL schema and Liquid validation. **Sends telemetry by default.** |

**Top pick:** **Stripe MCP** if you handle tax yourself or only sell in a few countries. **Polar MCP** if you're a solo dev selling globally (a merchant of record handles VAT/GST for you; confirm your country is supported).

---

## 9. Testing, QA, accessibility, visual checks

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

---

## 10. Performance and SEO

| Name | Type | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **Chrome DevTools MCP** | MCP | (above) | Official | 53.3k | Perf traces with CrUX field data, plus `lighthouse_audit` for SEO and a11y. Covers most needs. |
| lighthouse-mcp | MCP | https://github.com/priyankark/lighthouse-mcp | Community | 211 | Full Lighthouse including perf. |
| lighthouse-mcp-server | MCP | https://github.com/danielsogl/lighthouse-mcp-server | Community | 71 | 13+ audit tools. |
| **marketingskills** | Skills | https://github.com/coreyhaines31/marketingskills | Community | 54.2k | SEO audit, programmatic SEO, schema markup, copywriting, CRO, analytics. |
| Google Search Console MCP | MCP | https://github.com/AminForou/mcp-gsc | Community | 1.9k | Query GSC data (clicks, coverage). |
| DataForSEO MCP | MCP | https://github.com/dataforseo/mcp-server-typescript | Official | 252 | Keywords, SERP and backlinks (paid API). |
| Ahrefs MCP | MCP | https://github.com/ahrefs/ahrefs-mcp-server | Official | 101 (**archived**) | The repo is archived; Ahrefs moved to a hosted MCP (paid). |
| Vercel `vercel-optimize` / `react-best-practices` | Skills | https://github.com/vercel-labs/agent-skills | Official | 32.2k | Core Web Vitals and React performance patterns. |

**Top pick:** **Chrome DevTools MCP** for measuring, plus **marketingskills** for the method (meta tags, schema, content).

---

## 11. Version control and CI/CD

| Name | Type | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **GitHub MCP** | MCP (hosted + local) | https://github.com/github/github-mcp-server | Official | 33.5k | Repos, PRs, issues, Actions. Use toolsets to cut tool count. |
| Claude Code Action | GitHub Action | https://github.com/anthropics/claude-code-action | Official | 9.5k | `@claude` in PRs and issues; automated reviews and fixes. |
| GitLab MCP | Built-in MCP `https://<gitlab>/api/v4/mcp` | https://docs.gitlab.com/user/model_context_protocol/mcp_server/ | Official | — | OAuth DCR, toolset headers. |
| MCP reference servers (git, filesystem, fetch, memory, sequential-thinking) | MCP | https://github.com/modelcontextprotocol/servers | Official (MCP) | 91.1k | Reference implementations. Fine for local git operations. |

**Top pick:** **GitHub MCP** (or just the `gh` CLI; agents handle it well and it costs no context) plus **Claude Code Action** for PR automation.

---

## 12. Deployment, hosting and DNS (indie landscape)

| Service | MCP / skill | URL | Official? | Notes (free tier: check current pricing) |
|---|---|---|---|---|
| **Vercel** | Hosted `https://mcp.vercel.com` (OAuth; `npx add-mcp https://mcp.vercel.com`, `vercel mcp`) + Vercel plugin and skills | https://vercel.com/docs/agent-resources/vercel-mcp | Official | Best Next.js developer experience. The Hobby tier is **non-commercial** only. Tools: deployments, runtime logs/errors, Web Analytics, docs. |
| **Cloudflare (Pages/Workers, R2, DNS, Registrar)** | Hosted Code-Mode API MCP `https://mcp.cloudflare.com/mcp` + docs/bindings/observability servers · skills | https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/ · https://github.com/cloudflare/mcp-server-cloudflare (4.4k) · https://github.com/cloudflare/mcp · skills https://github.com/cloudflare/skills (3.0k) | Official | Most generous free tier (static hosting, Workers, R2 with no egress fees). DNS + registrar at cost; the **Registrar API (beta, Apr 2026) supports agent domain search and registration**. |
| Netlify | Hosted `https://netlify-mcp.netlify.app/mcp`; local `npx -y @netlify/mcp` | https://docs.netlify.com/build/build-with-ai/netlify-mcp-server · https://github.com/netlify/netlify-mcp | Official | Free tier. Forms built in. `netlify deploy --allow-anonymous` makes instant claimable deploys. |
| Render | MCP | https://github.com/render-oss/render-mcp-server | Official | Free web services spin down when idle. Free Postgres expires. |
| Railway | Hosted `https://mcp.railway.com` (OAuth); `railway mcp install --oauth` | https://docs.railway.com/ai/mcp-server (old repo `railwayapp/railway-mcp-server` **archived**) | Official | Usage-based with trial credits. Good DX for full-stack apps plus DBs. |
| Fly.io | `fly mcp server` (flyctl, experimental) | https://fly.io/docs/mcp/flyctl-server/ | Official | Pay-as-you-go VMs. `fly mcp launch` can also host *your* MCP servers. |
| **Coolify** (self-host) | Built-in read-only MCP at `https://<your-coolify>/mcp` (10 tools); community write-capable `StuMason/coolify-mcp` | https://github.com/coollabsio/coolify (62.9k) | Official (built-in) / community | Self-hosted Vercel/Heroku on a ~$5 VPS. |
| **Dokploy** (self-host) | Official MCP package | https://github.com/Dokploy/dokploy (37.8k) · MCP https://github.com/Dokploy/mcp (395) | Official | Self-host PaaS (Docker/Traefik). |
| GitHub Pages | Through the GitHub MCP / Actions | https://github.com/github/github-mcp-server | Official | Free static hosting. |
| Domains | Cloudflare Registrar API (above). Namecheap and Porkbun MCPs are reported but **I couldn't verify official endpoints**. | https://developers.cloudflare.com/registrar/registrar-api/ | Official (CF) | Cloudflare sells at cost and keeps DNS and CDN in one place. |
| Run your own MCP on Vercel | `mcp-handler` | https://vercel.com/docs/mcp | Official | If your site exposes an MCP. |

**Top pick:** **Vercel MCP** for Next.js apps. **Cloudflare MCP** for static/Astro sites, plus domains, DNS and R2 (cheapest at scale).

---

## 13. Monitoring, analytics, error tracking

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

---

## 14. Transactional and marketing email, forms, file storage (indie "glue")

| Service | MCP / skill | URL | Official? | Notes |
|---|---|---|---|---|
| **Resend** | Hosted `https://mcp.resend.com/mcp` (OAuth); local `npx resend-mcp` · skills | https://resend.com/docs/mcp-server · https://github.com/resend/resend-mcp · https://github.com/resend/resend-skills | Official | Developer email API that pairs with React Email. Has a free tier. |
| Loops | Hosted `https://mcp.loops.so` (OAuth) | https://loops.so/docs/mcp-server | Official | Marketing + transactional email for SaaS. |
| Postmark | MCP (24 tools) | https://github.com/ActiveCampaign/postmark-mcp | Official | Deliverability-focused transactional email. |
| Tally (forms) | Hosted `https://api.tally.so/mcp` | https://developers.tally.so/api-reference/mcp | Official | Free on all plans (beta). Agent creates forms and reads submissions. |
| Netlify Forms | Through the Netlify MCP | (above) | Official | Zero-backend forms. |
| UploadThing | `npx @uploadthing/mcp-server` | https://www.npmjs.com/package/@uploadthing/mcp-server · https://github.com/pingdotgg/uploadthing (5.3k) | Official | File uploads for Next.js. |
| Cloudflare R2 | Through the Cloudflare MCP | (above) | Official | S3-compatible with no egress fees. |
| Supabase Storage | Through the Supabase MCP | (above) | Official | — |

**Top pick:** **Resend** (MCP + skills) for email. **Tally** for forms when there's no backend.

---

## 15. Security review

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

---

## 16. Maintenance and iteration

- **Sentry MCP → fix → PR loop** (Sentry + GitHub MCP + Claude Code Action) is the highest-leverage maintenance loop.
- **PostHog MCP** to find low-converting pages, then iterate with **marketingskills** (CRO) and the **impeccable** skill (polish).
- **Spec Kit / OpenSpec** for changes: write a delta spec before each feature, which keeps the agent on track over months.
- **Superpowers** to keep TDD and verification discipline in long-running repos.
- **AGENTS.md / CLAUDE.md** as long-lived project memory: stack, conventions, "never do X".

---

## 17. SaaS boilerplates and starters (open source)

| Repo | URL | Stars | Stack | Notes |
|---|---|---|---|---|
| **Open SaaS (Wasp)** | https://github.com/wasp-lang/open-saas | 16.1k | React, Node, Prisma, Stripe/Polar/Lemon, email, admin | Most complete free boilerplate. Actively maintained. |
| Next.js SaaS Starter | https://github.com/nextjs/saas-starter | 16.2k | Next.js, Postgres, Drizzle, Stripe, shadcn | Official Next.js team starter. Minimal and clean. Last push Dec 2025. |
| ixartz SaaS-Boilerplate | https://github.com/ixartz/SaaS-Boilerplate | 7.4k | Next.js, Tailwind, shadcn, Clerk, Drizzle | Multi-tenancy, roles, i18n. |
| BoxyHQ SaaS Starter Kit | https://github.com/boxyhq/saas-starter-kit | 4.9k | Next.js, Prisma, SAML SSO | Enterprise-flavoured. |
| create-t3-app | https://github.com/t3-oss/create-t3-app | 29.2k | Next.js, tRPC, Prisma/Drizzle, Auth.js | Scaffolder, not a full SaaS. |
| create-better-t-stack | https://github.com/AmanVarshney01/create-better-t-stack | 5.8k | Mix and match | Modern scaffolder (Better Auth, Drizzle, Convex and others). |
| ~~vercel/nextjs-subscription-payments~~ | https://github.com/vercel/nextjs-subscription-payments | 7.7k | — | **Archived.** Don't start from it. |

---

## 18. End-to-end AI website / app builders (open source)

| Repo | URL | Stars | What it is |
|---|---|---|---|
| **bolt.diy** | https://github.com/stackblitz-labs/bolt.diy | 19.9k | Bolt.new fork; use any LLM. In-browser full-stack generation. |
| **Dyad** | https://github.com/dyad-sh/dyad | 21.8k | Local, open-source v0/Lovable/Bolt alternative. Supabase integration. |
| Open Lovable | https://github.com/firecrawl/open-lovable | 28.7k | Clone and recreate any site as a React app. |
| Onlook | https://github.com/onlook-dev/onlook | 26.9k | Visual "Cursor for designers" over your React/Tailwind code. |
| OpenHands | https://github.com/OpenHands/OpenHands | 90.6k | General autonomous coding agent platform. |
| screenshot-to-code | https://github.com/abi/screenshot-to-code | 80.2k | Screenshot or mockup to HTML/Tailwind/React/Vue. |
| E2B Fragments | https://github.com/e2b-dev/fragments | 6.4k | Next.js template for apps fully generated by AI, run in E2B sandboxes. |
| LlamaCoder | https://github.com/Nutlope/llamacoder | 7.1k | Open-source "Claude Artifacts" style generator. |

(Closed-source equivalents an indie would also look at: v0, Lovable, Bolt.new, Replit. Not listed in detail because they aren't repos.)

---

## 19. Meta-resources: where to discover more

| Resource | URL | Stars | Notes |
|---|---|---|---|
| Official MCP Registry | https://github.com/modelcontextprotocol/registry | 7.3k | Canonical registry (registry.modelcontextprotocol.io). |
| MCP reference servers | https://github.com/modelcontextprotocol/servers | 91.1k | Reference servers plus a large list of third-party ones. |
| punkpeye/awesome-mcp-servers | https://github.com/punkpeye/awesome-mcp-servers | 96.1k | Biggest list. Paired with glama.ai/mcp. |
| wong2/awesome-mcp-servers | https://github.com/wong2/awesome-mcp-servers | 4.4k | Curated (mcpservers.org). |
| appcypher/awesome-mcp-servers | https://github.com/appcypher/awesome-mcp-servers | 5.8k | **Archived.** |
| Smithery, mcp.so, Glama | https://smithery.ai · https://mcp.so · https://glama.ai/mcp/servers | — | Registries and hosting. Quality is uneven; check publishers. |
| anthropics/skills | https://github.com/anthropics/skills | 180k | Official skills + Agent Skills spec (agentskills.io). |
| anthropics/claude-plugins-official | https://github.com/anthropics/claude-plugins-official | 37.7k | Official plugin marketplace (frontend-design, vendor plugins like Figma, Sentry, Stripe…). |
| openai/skills | https://github.com/openai/skills | 28.0k | Codex skills catalog. |
| vercel-labs/skills (skills.sh) | https://github.com/vercel-labs/skills | 33.8k | Cross-agent skill installer and directory. |
| ComposioHQ/awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills | 76.9k | Curated skills list. |
| travisvn/awesome-claude-skills | https://github.com/travisvn/awesome-claude-skills | 15.4k | Curated skills list. |
| hesreallyhim/awesome-claude-code | https://github.com/hesreallyhim/awesome-claude-code | 55.4k | Commands, hooks, workflows. |
| wshobson/agents | https://github.com/wshobson/agents | 40.4k | Multi-harness plugin/subagent marketplace. |
| VoltAgent/awesome-claude-code-subagents | https://github.com/VoltAgent/awesome-claude-code-subagents | 25.6k | 100+ subagents. |
| PatrickJS/awesome-cursorrules | https://github.com/PatrickJS/awesome-cursorrules | 40.9k | Cursor rules (last push May 2026). |
| github/awesome-copilot | https://github.com/github/awesome-copilot | 39.9k | Copilot instructions, agents, skills. |

---

## 20. Top pick per stage (summary)

| # | Stage | Top pick | URL |
|---|---|---|---|
| 1 | Planning / spec | Spec Kit (+ Superpowers skills) | https://github.com/github/spec-kit |
| 2 | Research / scraping | Firecrawl MCP (self-host: Crawl4AI) | https://github.com/firecrawl/firecrawl-mcp-server |
| 3 | UI/UX design | Figma remote MCP. If no design exists: frontend-design skill + shadcn MCP | https://developers.figma.com/docs/figma-mcp-server/ |
| 4 | Assets | Replicate MCP | https://replicate.com/docs/reference/mcp |
| 5 | Frontend + docs | Context7 | https://github.com/upstash/context7 |
| 6 | Backend/DB/auth | Supabase MCP + agent-skills (auth alt: Better Auth) | https://supabase.com/docs/guides/getting-started/mcp |
| 7 | CMS | Sanity remote MCP (or MDX-in-Git / Payload) | https://www.sanity.io/docs/ai/mcp-server |
| 8 | Payments | Stripe MCP (global solo seller: Polar MCP) | https://docs.stripe.com/mcp |
| 9 | Testing / QA | Playwright MCP | https://github.com/microsoft/playwright-mcp |
| 10 | Perf & SEO | Chrome DevTools MCP + marketingskills | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| 11 | VCS / CI | GitHub MCP + Claude Code Action | https://github.com/github/github-mcp-server |
| 12 | Deploy / DNS | Vercel MCP (static/edge/DNS: Cloudflare MCP) | https://vercel.com/docs/agent-resources/vercel-mcp |
| 13 | Monitoring | Sentry MCP + PostHog MCP | https://github.com/getsentry/sentry-mcp |
| 14 | Email / forms | Resend MCP + skills | https://resend.com/docs/mcp-server |
| 15 | Security | Semgrep MCP + Claude Code Security Review + snyk/agent-scan | https://github.com/semgrep/semgrep |
| 16 | Maintenance | Sentry → GitHub → Claude Code Action loop | — |

---

## 21. Minimal end-to-end stack (≈10 items, works in Claude Code / Cursor / Codex)

**Skills (cheap, load on demand):**
1. **Superpowers**: plan, TDD, verify discipline. https://github.com/obra/superpowers
2. **frontend-design** (Anthropic) + **Vercel agent-skills** (react-best-practices, web-design-guidelines). https://github.com/anthropics/skills · https://github.com/vercel-labs/agent-skills
3. **marketingskills**: SEO, schema, copy. https://github.com/coreyhaines31/marketingskills

**MCP servers (keep ~6 connected):**
4. **Context7**: current docs. https://github.com/upstash/context7
5. **shadcn/ui MCP**: components. https://ui.shadcn.com/docs/mcp
6. **Playwright MCP** or **Chrome DevTools MCP** (pick one default): eyes. 
7. **Supabase MCP** (scoped and read-only by default). https://supabase.com/docs/guides/getting-started/mcp
8. **Vercel MCP**: deploys, logs, runtime errors. https://vercel.com/docs/agent-resources/vercel-mcp
9. **Stripe MCP** (test mode, restricted key). https://docs.stripe.com/mcp
10. **Sentry MCP**: production errors. https://github.com/getsentry/sentry-mcp

Plus the **`gh` CLI** instead of the GitHub MCP (zero context cost), and **Spec Kit** run once per project/feature.

---

## 22. Recommended indie stack (managed, generous free tiers)

| Layer | Pick | Agent hook |
|---|---|---|
| Spec & method | Spec Kit + Superpowers + AGENTS.md | Skills / commands |
| Framework | **Next.js** for app/SaaS · **Astro** for marketing/content | Next DevTools MCP / Astro Docs MCP + Context7 |
| UI | shadcn/ui + Tailwind + Lucide; frontend-design / impeccable skills | shadcn MCP |
| Starter | nextjs/saas-starter or Open SaaS | — |
| DB + storage + realtime | **Supabase** (alt: Neon + Drizzle) | Supabase hosted MCP + agent-skills |
| Auth | **Supabase Auth** or **Better Auth** (Clerk if you want hosted UI) | Better Auth docs MCP / Clerk MCP |
| Payments | **Stripe** (or **Polar** as MoR for global tax) | Stripe MCP / Polar MCP |
| Email | **Resend** (+ Loops for marketing) | Resend MCP + skills / Loops MCP |
| Forms | Tally (or Server Actions → Supabase) | Tally MCP |
| Files | Supabase Storage or UploadThing | MCPs |
| CMS | MDX-in-Git → Sanity once others edit | Sanity MCP |
| Hosting | **Vercel** (move to Pro once commercial) | Vercel MCP |
| Domain/DNS/CDN | **Cloudflare** Registrar + DNS | Cloudflare MCP |
| Analytics | **PostHog** (or Vercel Analytics) | PostHog MCP |
| Errors | **Sentry** | Sentry MCP |
| CI / review | GitHub + Claude Code Action + Claude Code Security Review | gh CLI / GitHub MCP |
| QA | Playwright + Chrome DevTools (Lighthouse) | MCPs |

### Cheap / self-hosted alternative (one ~$5–10/mo VPS + Cloudflare free)

| Layer | Pick | Agent hook |
|---|---|---|
| Hosting PaaS | **Coolify** or **Dokploy** on a VPS | Coolify built-in MCP (read-only) / Dokploy MCP |
| Static sites | Cloudflare Pages/Workers (free) or GitHub Pages | Cloudflare MCP / GitHub MCP |
| Backend | **PocketBase** (single binary) or self-hosted **Appwrite** / Supabase | Community PocketBase MCP / `uvx mcp-server-appwrite` |
| DB alt | Turso (SQLite) free tier or Postgres container | Turso MCP |
| Auth | **Better Auth** (library, $0) | Better Auth docs MCP |
| CMS | **Payload** (inside Next.js) or Strapi / Directus | Payload plugin-mcp / Strapi built-in MCP / Directus MCP |
| Payments | **Polar** (OSS, MoR) | Polar MCP |
| Analytics | **Umami** or **Plausible** self-hosted | `@umami/mcp` / getsentry/plausible-mcp (community) |
| Errors | Sentry free dev tier (self-hosted Sentry is heavy) | Sentry MCP |
| Storage | Cloudflare R2 (no egress fees) | Cloudflare MCP |
| Scraping | Crawl4AI | — |
| MCP runtime | ToolHive or Docker MCP Gateway to isolate community servers | — |

---

## 23. Gotchas and hard-won rules

1. **Too many tools fills the context window.** Every connected MCP server puts its tool schemas into the prompt. 10+ servers can use tens of thousands of tokens before you type anything, and tool-selection accuracy drops. Mitigations:
   - Connect per project, not globally.
   - Use toolset filters (GitHub toolsets, Supabase `features=`, PostHog `features=`/`tools=`, Neon `category=`, Chrome DevTools `--slim`).
   - Prefer **skills** (loaded on demand) and **CLIs** (`gh`, `vercel`, `supabase`, `stripe`) when the agent can run a shell.
   - "Code-mode" servers (Cloudflare, Paddle, Appwrite's `search_tools`/`call_tool`) expose 2–4 meta-tools instead of hundreds. That's the direction the industry is moving.
2. **Community MCPs are code running with your credentials.** Tool-poisoning and prompt-injection attacks are real. Prefer vendor-official hosted servers with OAuth. Run `snyk/agent-scan` on your config. Run community servers in ToolHive or Docker MCP Gateway. Pin versions instead of `@latest` for anything with write access.
3. **Prompt injection through "eyes" and "research" tools.** Pages scraped by Firecrawl, Playwright or browser-use can contain instructions. Never pair an unrestricted browsing/scraping MCP with write-capable payments/DB/deploy MCPs in the same autonomous session without human confirmation.
4. **Scope the "hands" servers.** Supabase `read_only=true&project_ref=…`. Stripe restricted keys and test mode. Polar/Paddle sandbox endpoints. Convex keeps production disabled by default; leave it that way. Never point an agent at prod DB credentials.
5. **Archived or moved repos are everywhere in tutorials.** Browserbase, PostHog, Sanity, Railway, Semgrep, Prisma, ElevenLabs, Penpot, Ahrefs, Automattic WordPress MCP, Storybook MCP, Nhost and appcypher's awesome list are all archived. Sentry's repo now redirects to `getsentry/toolkit`; Stripe's `agent-toolkit` is now `stripe/ai`. Check the vendor docs page, not a 2025 blog post.
6. **Telemetry defaults.** Chrome DevTools MCP (`--no-usage-statistics`), Shopify Dev MCP and others send usage data by default.
7. **Figma remote vs desktop conflict.** If both are configured, clients may resolve to the desktop server and miss the remote-only write tools. Give them distinct names.
8. **Free tiers are not production plans.** Vercel Hobby is non-commercial. Supabase free projects pause when idle. Render free services spin down. Recheck vendor pricing before launch; these notes weren't re-checked line by line against each pricing page.
9. **Skills are also code.** SKILL.md packs can bundle scripts. Review popular community packs (Superpowers, ui-ux-pro-max, taste-skill, impeccable) before giving them shell access. Star counts in the 100k range don't prove a pack is safe.

---

## 24. Not verified / dropped

- **Framer MCP**: no official server found. Dropped.
- **Namecheap / Porkbun official MCPs**: mentioned by third parties, but I found no vendor docs. Not recommended.
- **Lemon Squeezy official MCP**: none exists (community only).
- **fal.ai official MCP**: none found (community `raveenb/fal-mcp-server`).
- **Xata MCP, Auth.js MCP**: none found.
- **Svelte MCP repo**: the docs page exists; the GitHub repo was renamed or moved (the API returns 301). Use the docs URL.
