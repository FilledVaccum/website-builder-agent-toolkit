# Free catalog: the best agent skills, GitHub repos and free MCP servers for building a website, by stage

*Curated Oct 11, 2026 (MYT) for Swap. Quality bar: official/vendor-maintained or clear category leaders, usually 1k+ ★, active in roughly the last 6 months. Each subsection is ranked by quality/popularity and capped at the strongest picks. Star counts and last-push dates come from the GitHub API today. Every repo was checked to exist; hosted MCP endpoints were checked against vendor docs. MCPs listed here are free to use: open source, or hosted on a service with a usable free tier. Paid-only servers are excluded (DataForSEO: $50 minimum; Ahrefs: archived/paid; Replicate: pay-per-run; Fly.io: no free plan).*

**Legend:** Official = vendor-maintained. Community = third party. ★ = GitHub stars (for a sub-skill or plugin inside a monorepo, these are the parent repo's stars). "—" = hosted endpoint with no public repo. "(niche, <1k★)" marks items kept only because they're the best available in a thin category. Skills install with `npx skills add owner/repo`, or as Claude Code plugins with `/plugin marketplace add owner/repo`.

**Excluded on purpose (archived or deprecated):** browserbase/mcp-server-browserbase (use the hosted endpoint), PostHog/mcp, sanity-io/sanity-mcp-server, railwayapp/railway-mcp-server, semgrep/mcp, prisma/mcp, elevenlabs/elevenlabs-mcp, penpot/penpot-mcp, ahrefs/ahrefs-mcp-server, Automattic/wordpress-mcp, storybookjs/mcp, nhost/mcp-nhost, langchain-ai/mcpdoc, houtini-ai/geo-analyzer, appcypher/awesome-mcp-servers, vercel/nextjs-subscription-payments.


---

## 1. Planning, requirements & spec


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Superpowers** | https://github.com/obra/superpowers | Community | 297.5k | 2026-10-10 | Brainstorm → write-plan → execute-plan → TDD → verify skills; the most-installed skills framework | FOSS |
| 2 | **addyosmani agent-skills (interview-me, spec-driven-development, planning-and-task-breakdown)** | https://github.com/addyosmani/agent-skills | Community (Addy Osmani) | 104.8k | 2026-10-10 | PRD-first and task-decomposition skills with acceptance criteria | FOSS |
| 3 | **Matt Pocock — Skills for Real Engineers** | https://github.com/mattpocock/skills | Community | 285.7k | 2026-10-09 | Small, composable engineering/productivity skills (an alternative to process-heavy BMAD/Spec Kit) | FOSS |
| 4 | **planning-with-files** | https://github.com/OthmanAdi/planning-with-files | Community | 27.4k | 2026-10-10 | Persistent markdown plans that survive long agent sessions | FOSS |
| 5 | **PM Skills Marketplace** | https://github.com/phuryn/pm-skills | Community | 26.9k | 2026-10-10 | 100+ product-management skills (discovery, PRD, strategy, launch) | FOSS |
| 6 | **Product-Manager-Skills** | https://github.com/deanpeters/Product-Manager-Skills | Community | 7.2k | 2026-09-01 | PM frameworks (JTBD, PRDs, roadmaps) as skills | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Spec Kit** | https://github.com/github/spec-kit | Official (GitHub) | 140.8k | 2026-10-10 | Spec-driven development toolkit: /specify → /plan → /tasks → /implement | FOSS |
| 2 | **OpenSpec** | https://github.com/Fission-AI/OpenSpec | Community | 71.6k | 2026-10-09 | Lightweight SDD with change proposals; good for brownfield | FOSS |
| 3 | **BMAD-METHOD** | https://github.com/bmad-code-org/BMAD-METHOD | Community | 54.0k | 2026-10-11 | Analyst/PM/Architect/Dev agent workflow | FOSS |
| 4 | **Taskmaster** | https://github.com/eyaltoledano/claude-task-master | Community | 28.2k | 2026-04-28 | PRD → dependency-ordered tasks (CLI + MCP) | FOSS; needs your LLM API key |
| 5 | **AGENTS.md** | https://github.com/agentsmd/agents.md | Open standard | 24.9k | 2026-09-10 | One instructions file read by Codex, Cursor, Copilot, etc. | FOSS |
| 6 | **Mermaid** | https://github.com/mermaid-js/mermaid | OSS | 90.6k | 2026-10-11 | Text → diagrams (sitemaps, flows, ERDs) agents can write | FOSS |
| 7 | **Excalidraw** | https://github.com/excalidraw/excalidraw | OSS | 133.6k | 2026-10-11 | Whiteboard / wireframes | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Taskmaster MCP** | https://github.com/eyaltoledano/claude-task-master | Community | 28.2k | 2026-04-28 | Task breakdown/next-task tools over MCP | FOSS, runs locally |
| 2 | **Notion MCP (hosted)** | https://github.com/makenotion/notion-mcp-server | Official | 4.7k | 2026-09-20 | Read/write PRDs & research in Notion | Notion Free plan works |
| 3 | **Sequential Thinking / Memory reference servers** | https://github.com/modelcontextprotocol/servers | Official (MCP) | 91.1k | 2026-10-11 | Structured step-by-step reasoning; knowledge-graph memory | FOSS |
| 4 | **Excalidraw MCP (+skill)** | https://github.com/yctimlin/mcp_excalidraw | Community | 2.5k | 2026-10-09 | Agent draws/edits wireframes & diagrams | FOSS |

---

## 2. Research, competitor analysis & scraping


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **last30days** | https://github.com/mvanhorn/last30days-skill | Community | 64.0k | 2026-10-11 | Researches a topic across Reddit, X, YouTube, HN and the web, then synthesizes | FOSS |
| 2 | **Browserbase skills** | https://github.com/browserbase/skills | Official | 3.7k | 2026-09-29 | Web access/browsing skills for agents | FOSS; Browserbase free plan for cloud browsers |
| 3 | **Firecrawl skills** | https://github.com/firecrawl/skills | Official | 119 | 2026-10-08 | Search/scrape/crawl/interact skills for Claude Code, Codex, Cursor | FOSS; Firecrawl free 1,000 credits/mo |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Firecrawl** | https://github.com/firecrawl/firecrawl | Official | 190.4k | 2026-10-10 | Web → LLM-ready markdown; self-hostable | FOSS (AGPL) or hosted free tier |
| 2 | **browser-use** | https://github.com/browser-use/browser-use | Community | 117.6k | 2026-10-09 | Autonomous browser agent | FOSS |
| 3 | **Scrapling** | https://github.com/D4Vinci/Scrapling | Community | 86.8k | 2026-10-11 | Adaptive, anti-bot-resilient scraping framework | FOSS |
| 4 | **Crawl4AI** | https://github.com/unclecode/crawl4ai | Community | 85.2k | 2026-10-11 | Self-hosted crawler → markdown | FOSS |
| 5 | **Scrapy** | https://github.com/scrapy/scrapy | OSS | 64.7k | 2026-10-10 | Classic Python crawling framework | FOSS |
| 6 | **Lightpanda** | https://github.com/lightpanda-io/browser | Community | 36.3k | 2026-10-11 | Fast headless browser built for agents | FOSS |
| 7 | **ScrapeGraphAI** | https://github.com/ScrapeGraphAI/Scrapegraph-ai | Community | 31.7k | 2026-10-06 | LLM-driven structured extraction | FOSS |
| 8 | **Crawlee** | https://github.com/apify/crawlee | Official (Apify) | 26.1k | 2026-10-11 | Node crawling/browser automation library | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Playwright MCP** | https://github.com/microsoft/playwright-mcp | Official (Microsoft) | 38.0k | 2026-10-08 | Browse sites via accessibility snapshots | FOSS |
| 2 | **Firecrawl MCP** | https://github.com/firecrawl/firecrawl-mcp-server | Official | 7.6k | 2026-10-09 | Scrape/crawl/map/search/extract | Free 1,000 credits/mo (or self-host Firecrawl) |
| 3 | **Apify MCP** | https://github.com/apify/apify-mcp-server | Official | 10.5k | 2026-10-09 | Thousands of ready scrapers (Actors) | Free $5 credit/mo |
| 4 | **Exa MCP** | https://github.com/exa-labs/exa-mcp-server | Official | 5.1k | 2026-10-07 | Neural web search + crawl | Free $10 credits/mo |
| 5 | **Bright Data MCP** | https://github.com/brightdata/brightdata-mcp | Official | 2.7k | 2026-10-11 | Unblocked web access, SERP | Free tier on some APIs |
| 6 | **Tavily MCP** | https://github.com/tavily-ai/tavily-mcp | Official | 2.4k | 2026-10-05 | Search/extract/map/crawl | Free 1,000 credits/mo |

---

## 3. UX/UI design & design systems


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **UI UX Pro Max** | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community | 134.7k | 2026-10-10 | Design-system generator: styles, palettes, font pairings, UX rules | FOSS |
| 2 | **Taste Skill** | https://github.com/Leonxlnx/taste-skill | Community | 94.6k | 2026-10-09 | Pushes agents away from generic "AI slop" UI | FOSS |
| 3 | **Impeccable** | https://github.com/pbakaus/impeccable | Community | 79.7k | 2026-10-11 | Design vocabulary + critique/audit/polish commands | FOSS |
| 4 | **frontend-design (+ theme-factory, brand-guidelines)** | https://github.com/anthropics/skills/tree/main/skills/frontend-design | Official (Anthropic) | 180.5k | 2026-10-09 | Bold, intentional visual direction before coding; also a Claude Code plugin | FOSS |
| 5 | **web-design-guidelines** | https://github.com/vercel-labs/agent-skills | Official (Vercel) | 32.2k | 2026-08-28 | Audit UI against Vercel accessibility/UX guidelines | FOSS |
| 6 | **Hallmark** | https://github.com/Nutlope/hallmark | Community (Nutlope) | 29.9k | 2026-08-06 | Anti-AI-slop design skill | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **shadcn/ui** | https://github.com/shadcn-ui/ui | OSS | 125.3k | 2026-10-11 | Copy-in React components + registry (+ built-in MCP) | FOSS |
| 2 | **Tailwind CSS** | https://github.com/tailwindlabs/tailwindcss | OSS | 97.9k | 2026-10-09 | Utility CSS every agent knows | FOSS |
| 3 | **Open Design** | https://github.com/nexu-io/open-design | Community | 100.5k | 2026-10-11 | Open-source Claude Design alternative (local-first design app) | FOSS |
| 4 | **Penpot** | https://github.com/penpot/penpot | OSS | 60.9k | 2026-10-11 | Open-source Figma alternative | FOSS |
| 5 | **daisyUI** | https://github.com/saadeghi/daisyui | OSS | 42.6k | 2026-10-08 | Tailwind component classes | FOSS |
| 6 | **HeroUI** | https://github.com/heroui-inc/heroui | OSS | 30.9k | 2026-10-11 | React UI library (ex-NextUI) | FOSS |
| 7 | **Onlook** | https://github.com/onlook-dev/onlook | Community | 26.9k | 2026-08-25 | Visual editor over your React/Tailwind code | FOSS |
| 8 | **Radix Primitives** | https://github.com/radix-ui/primitives | OSS | 19.4k | 2026-10-09 | Accessible unstyled primitives under shadcn | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Figma MCP (remote)** | https://developers.figma.com/docs/figma-mcp-server/ | Official | — | — | Design context → code; write to canvas | Remote server works on all seats incl. free Starter |
| 2 | **shadcn/ui MCP** | https://ui.shadcn.com/docs/mcp | Official | 125.3k | 2026-10-11 | Browse/search/install components from any registry | FOSS |
| 3 | **Google Stitch MCP (remote)** | https://stitch.withgoogle.com/docs/mcp/setup | Official (Google) | 1.8k | 2026-10-01 | Generate UI screens & design systems from prompts | Free with Stitch quota |
| 4 | **Framelink Figma MCP** | https://github.com/GLips/Figma-Context-MCP | Community | 16.0k | 2026-10-10 | Figma layout → code with a personal token | FOSS |
| 5 | **TalkToFigma** | https://github.com/grab/cursor-talk-to-figma-mcp | Community (Grab) | 7.0k | 2026-07-26 | Agent reads & edits Figma via plugin | FOSS |
| 6 | **21st.dev Magic MCP** | https://github.com/21st-dev/magic-mcp | Official | 6.0k | 2026-09-09 | Search 10k+ components, generate UI | Free Hobby (limited copies/day) |
| 7 | **Canva MCP** | https://www.canva.dev/docs/mcp/ | Official | — | — | Generate/edit Canva designs | Canva Free account |

---

## 4. Assets: images, icons, fonts, video


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **canvas-design / algorithmic-art / theme-factory** | https://github.com/anthropics/skills/tree/main/skills | Official (Anthropic) | 180.5k | 2026-10-09 | Posters, generative art, themed visual assets | FOSS |
| 2 | **Remotion skills** | https://github.com/remotion-dev/skills | Official | 5.0k | 2026-10-07 | Agents build videos (promo, hero loops) with Remotion | FOSS |
| 3 | **logo-design-skill** | https://github.com/kaankiziltug/logo-design-skill | Community | 2.7k | 2026-09-30 | Logo design process and principles for agents | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Remotion** | https://github.com/remotion-dev/remotion | OSS | 63.2k | 2026-10-11 | Programmatic video in React | Free for individuals/small teams (company license above a size; see repo) |
| 2 | **sharp** | https://github.com/lovell/sharp | OSS | 32.7k | 2026-10-11 | Image resize/convert (AVIF/WebP) | FOSS |
| 3 | **Squoosh** | https://github.com/GoogleChromeLabs/squoosh | Official (Google) | 26.0k | 2026-10-07 | Image compression codecs | FOSS |
| 4 | **Lucide** | https://github.com/lucide-icons/lucide | OSS | 24.9k | 2026-10-11 | Default shadcn icon set | FOSS |
| 5 | **Heroicons** | https://github.com/tailwindlabs/heroicons | OSS | 23.9k | 2026-05-12 | Tailwind team SVG icons | FOSS |
| 6 | **Iconify** | https://github.com/iconify/iconify | OSS | 6.4k | 2026-10-10 | 200k+ icons, one syntax | FOSS |
| 7 | **Fontsource** | https://github.com/fontsource/fontsource | OSS | 6.2k | 2026-10-11 | Self-host open-source fonts via npm | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Hugging Face MCP (hosted hf.co/mcp)** | https://github.com/huggingface/hf-mcp-server | Official | 303 | 2026-10-07 | Use HF Spaces (e.g. image models) and Hub search from agents | Free HF account (Space GPU quotas apply) |
| 2 | **Canva MCP** | https://www.canva.dev/docs/mcp/ | Official | — | — | Social/OG images, branded graphics | Canva Free |
| 3 | **Excalidraw MCP** | https://github.com/yctimlin/mcp_excalidraw | Community | 2.5k | 2026-10-09 | Diagrams and illustrations | FOSS |

---

## 5. Frontend scaffolding & code generation


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Vercel agent-skills (react-best-practices, composition-patterns, react-view-transitions)** | https://github.com/vercel-labs/agent-skills | Official | 32.2k | 2026-08-28 | React/Next patterns from Vercel engineering | FOSS |
| 2 | **next-skills** | https://github.com/vercel-labs/next-skills | Official (Vercel) | 983 | 2026-09-16 | Next.js-specific skills | FOSS |
| 3 | **frontend-ui-engineering / incremental-implementation** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | Component architecture, responsive, WCAG AA, thin vertical slices | FOSS |
| 4 | **web-artifacts-builder** | https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder | Official | 180.5k | 2026-10-09 | Multi-component React/Tailwind/shadcn builds | FOSS |
| 5 | **awesome-cursorrules** | https://github.com/PatrickJS/awesome-cursorrules | Community | 40.9k | 2026-05-30 | Framework-specific Cursor rules (Next, Astro, Svelte…) | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Next.js** | https://github.com/vercel/next.js | OSS (Vercel) | 143.1k | 2026-10-11 | React framework for apps/SaaS | FOSS |
| 2 | **Astro** | https://github.com/withastro/astro | OSS | 63.2k | 2026-10-11 | Best for content/marketing sites | FOSS |
| 3 | **Nuxt** | https://github.com/nuxt/nuxt | OSS | 60.9k | 2026-10-11 | Vue full-stack framework | FOSS |
| 4 | **React Router (v7 framework mode)** | https://github.com/remix-run/react-router | OSS | 56.6k | 2026-10-09 | Full-stack React | FOSS |
| 5 | **SvelteKit** | https://github.com/sveltejs/kit | OSS | 20.8k | 2026-10-11 | Svelte full-stack | FOSS |
| 6 | **Open Lovable** | https://github.com/firecrawl/open-lovable | Official (Firecrawl) | 28.7k | 2026-10-09 | Clone any site into a React app | FOSS |
| 7 | **Dyad** | https://github.com/dyad-sh/dyad | Community | 21.8k | 2026-10-09 | Local open-source v0/Lovable/Bolt alternative | FOSS |
| 8 | **bolt.diy** | https://github.com/stackblitz-labs/bolt.diy | Community | 19.9k | 2026-10-11 | Open-source Bolt, any LLM | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Context7** | https://github.com/upstash/context7 | Official (Upstash) | 62.9k | 2026-10-10 | Current version-specific library docs | Free 1,000 calls/mo |
| 2 | **Next.js DevTools MCP** | https://github.com/vercel/next-devtools-mcp | Official | 826 | 2026-09-15 | Next docs, upgrades, live dev-server errors/routes | FOSS |
| 3 | **Astro Docs MCP (remote)** | https://mcp.docs.astro.build/mcp | Official | — | — | Current Astro docs | Free |
| 4 | **Svelte MCP** | https://svelte.dev/docs/mcp | Official | — | — | Svelte 5 docs + autofixer | Free |
| 5 | **shadcn/ui MCP** | https://ui.shadcn.com/docs/mcp | Official | 125.3k | 2026-10-11 | Install components by prompt | FOSS |

---

## 6. Backend, BaaS & database


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Supabase agent-skills** | https://github.com/supabase/agent-skills | Official | 2.7k | 2026-10-02 | Postgres/RLS/Auth/Edge Functions best practices | FOSS |
| 2 | **Cloudflare skills** | https://github.com/cloudflare/skills | Official | 3.0k | 2026-10-10 | Workers, D1, R2, KV, Durable Objects | FOSS |
| 3 | **Neon agent-skills** | https://github.com/neondatabase/agent-skills | Official | 100 | 2026-10-09 | Serverless Postgres patterns | FOSS |
| 4 | **Prisma skills** | https://github.com/prisma/skills | Official | 68 | 2026-10-08 | Prisma ORM/Postgres skills | FOSS |
| 5 | **Convex agent-skills** | https://github.com/get-convex/agent-skills | Official | 64 | 2026-10-01 | Convex backend skills | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Supabase** | https://github.com/supabase/supabase | OSS | 111.4k | 2026-10-11 | Postgres + Auth + Storage + Realtime (self-hostable) | FOSS or Free tier |
| 2 | **PocketBase** | https://github.com/pocketbase/pocketbase | OSS | 61.4k | 2026-10-08 | Backend in one Go binary | FOSS |
| 3 | **Appwrite** | https://github.com/appwrite/appwrite | OSS | 57.6k | 2026-10-11 | Self-hostable BaaS | FOSS or Free tier |
| 4 | **Drizzle ORM** | https://github.com/drizzle-team/drizzle-orm | OSS | 36.0k | 2026-10-09 | Type-safe SQL ORM | FOSS |
| 5 | **Turso (Limbo)** | https://github.com/tursodatabase/turso | OSS | 24.7k | 2026-10-11 | SQLite-compatible DB in Rust | FOSS |
| 6 | **Convex backend** | https://github.com/get-convex/convex-backend | OSS | 12.7k | 2026-10-11 | Reactive TS backend (self-hostable) | FOSS or Free tier |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Supabase MCP (hosted mcp.supabase.com)** | https://github.com/supabase/mcp | Official | 2.9k | 2026-10-09 | Schema, SQL, migrations, logs, branches | Supabase Free (2 projects) |
| 2 | **Neon MCP (hosted)** | https://github.com/neondatabase/mcp-server-neon | Official | 650 | 2026-10-04 | Projects, branches, SQL | Neon Free (100 projects) |
| 3 | **Firebase MCP (firebase-tools mcp)** | https://firebase.google.com/docs/ai-assistance/mcp-server | Official | 4.5k | 2026-10-10 | Auth, Firestore, rules, hosting | Spark (no-cost) plan |
| 4 | **MongoDB MCP** | https://github.com/mongodb-js/mongodb-mcp-server | Official | 1.1k | 2026-10-11 | Atlas + DB operations | M0 free cluster |
| 5 | **Convex MCP (npx convex mcp start)** | https://docs.convex.dev/ai/convex-mcp-server | Official | 12.7k | 2026-10-11 | Tables, functions, logs; prod off by default | Convex Free |
| 6 | **Appwrite MCP (hosted)** | https://appwrite.io/docs/tooling/ai/mcp-servers | Official | — | — | Projects, DB, users, docs search | Appwrite Free / self-host |
| 7 | **Turso MCP (hosted + tursodb --mcp)** | https://docs.turso.tech/integrations/mcp | Official | — | — | SQLite databases | Turso Free (100 DBs) |

---

## 7. Auth


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Better Auth skills** | https://github.com/better-auth/skills | Official | 221 | 2026-09-01 | Better Auth setup/plugins best practices | FOSS |
| 2 | **Clerk skills** | https://github.com/clerk/skills | Official | 88 | 2026-10-10 | Clerk integration patterns | FOSS |
| 3 | **Supabase agent-skills (Auth/RLS)** | https://github.com/supabase/agent-skills | Official | 2.7k | 2026-10-02 | Supabase Auth + RLS | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Better Auth** | https://github.com/better-auth/better-auth | OSS | 30.3k | 2026-10-11 | Most comprehensive TS auth library | FOSS |
| 2 | **Keycloak** | https://github.com/keycloak/keycloak | OSS | 37.3k | 2026-10-11 | Self-hosted IAM/SSO | FOSS |
| 3 | **Auth.js (NextAuth)** | https://github.com/nextauthjs/next-auth | OSS | 28.4k | 2026-07-22 | Classic Next.js auth | FOSS |
| 4 | **SuperTokens** | https://github.com/supertokens/supertokens-core | OSS | 15.3k | 2026-10-06 | Self-hostable Auth0 alternative | FOSS |
| 5 | **ZITADEL** | https://github.com/zitadel/zitadel | OSS | 15.3k | 2026-10-09 | Identity infrastructure | FOSS |
| 6 | **Logto** | https://github.com/logto-io/logto | OSS | 14.7k | 2026-10-11 | Auth for SaaS/AI apps | FOSS |
| 7 | **Ory Kratos** | https://github.com/ory/kratos | OSS | 13.9k | 2026-07-29 | Headless identity | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Better Auth docs MCP** | https://better-auth.com/docs/ai-resources/mcp | Official | — | — | Docs/examples for setup | Free |
| 2 | **Clerk MCP (remote, beta)** | https://clerk.com/docs/guides/ai/mcp/clerk-mcp-server | Official | — | — | Current SDK snippets/patterns | Free (Clerk free: 50k MRU) |
| 3 | **Supabase MCP** | https://github.com/supabase/mcp | Official | 2.9k | 2026-10-09 | Manage Supabase Auth via DB tools | Supabase Free |

---

## 8. CMS & content


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **WordPress agent-skills** | https://github.com/WordPress/agent-skills | Official | 2.2k | 2026-10-05 | Blocks, themes, plugins best practices | FOSS |
| 2 | **Sanity agent-toolkit** | https://github.com/sanity-io/agent-toolkit | Official | 188 | 2026-10-09 | Rules/skills for building with Sanity | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Strapi** | https://github.com/strapi/strapi | OSS | 73.3k | 2026-10-09 | Headless CMS (built-in MCP in v5.47+) | FOSS |
| 2 | **Payload** | https://github.com/payloadcms/payload | OSS | 45.2k | 2026-10-10 | Next.js-native CMS/backend | FOSS |
| 3 | **Directus** | https://github.com/directus/directus | OSS | 38.4k | 2026-10-09 | DB → headless CMS + admin | FOSS (BSL for large orgs) |
| 4 | **Decap CMS** | https://github.com/decaporg/decap-cms | OSS | 19.4k | 2026-10-11 | Git-based CMS for static sites | FOSS |
| 5 | **TinaCMS** | https://github.com/tinacms/tinacms | OSS | 13.8k | 2026-10-09 | Markdown + visual editing in Git | FOSS |
| 6 | **Starlight** | https://github.com/withastro/starlight | OSS (Astro) | 9.4k | 2026-10-09 | Docs sites on Astro | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Sanity MCP (remote mcp.sanity.io)** | https://www.sanity.io/docs/ai/mcp-server | Official | — | — | Query/edit content, deploy schemas | Sanity Free (20 seats, 10k docs) |
| 2 | **Strapi MCP (built-in /mcp)** | https://docs.strapi.io/cms/features/strapi-mcp-server | Official | 73.3k | 2026-10-09 | CRUD/publish/media tools scoped by admin token | FOSS |
| 3 | **Payload MCP plugin** | https://payloadcms.com/docs/plugins/mcp | Official | 45.2k | 2026-10-10 | Collections/globals via /api/mcp | FOSS |
| 4 | **WordPress MCP Adapter** | https://github.com/WordPress/mcp-adapter | Official | 1.8k | 2026-10-08 | Abilities API → MCP | FOSS |
| 5 | **Directus MCP** | https://github.com/directus/mcp | Official | 86 | 2026-02-04 | Content tools for Directus (repo quiet since Feb 2026) | FOSS |
| 6 | **Contentful MCP** | https://github.com/contentful/contentful-mcp-server | Official | 61 | 2026-10-11 | Management API | Contentful Free plan |

---

## 9. Payments & e-commerce


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Stripe skills (stripe-best-practices, stripe-docs, upgrade-stripe…)** | https://github.com/stripe/ai/tree/main/skills | Official | 1.9k | 2026-10-11 | Stripe integration best practices & upgrades | FOSS |
| 2 | **Shopify AI Toolkit** | https://github.com/Shopify/Shopify-AI-Toolkit | Official | 594 | 2026-10-08 | Plugins/skills for Shopify dev in Claude Code, Codex, Cursor | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Medusa** | https://github.com/medusajs/medusa | OSS | 36.7k | 2026-10-10 | Headless commerce platform | FOSS |
| 2 | **Saleor** | https://github.com/saleor/saleor | OSS | 23.4k | 2026-10-09 | GraphQL headless commerce | FOSS |
| 3 | **Polar** | https://github.com/polarsource/polar | OSS | 10.4k | 2026-10-11 | MoR billing platform (open source) | FOSS / 5% + 50¢ hosted |
| 4 | **Lago** | https://github.com/getlago/lago | OSS | 10.7k | 2026-10-09 | Usage-based billing | FOSS |
| 5 | **stripe-node** | https://github.com/stripe/stripe-node | Official | 4.5k | 2026-10-10 | Stripe Node SDK | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Stripe MCP (remote mcp.stripe.com)** | https://docs.stripe.com/mcp | Official | 1.9k | 2026-10-11 | API + docs tools; use restricted keys | No monthly fee; test mode free |
| 2 | **Polar MCP (remote)** | https://polar.sh/docs/integrate/mcp | Official | 10.4k | 2026-10-11 | Products, customers, subscriptions | Free Starter; sandbox endpoint |
| 3 | **Paddle MCP (remote + sandbox)** | https://developer.paddle.com/sdks/ai/paddle-mcp | Official | — | — | Billing API (code-mode) | No monthly fee; sandbox free |
| 4 | **Shopify Dev MCP (@shopify/dev-mcp)** | https://www.npmjs.com/package/@shopify/dev-mcp | Official | — | — | Docs, GraphQL schema, Liquid validation | FOSS (telemetry on by default) |
| 5 | **PayPal agent toolkit / MCP** | https://github.com/paypal/agent-toolkit | Official | 196 | 2026-09-01 | PayPal APIs | No monthly fee; sandbox free |

---

## 10. Email & forms


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Resend skills** | https://github.com/resend/resend-skills | Official | 200 | 2026-10-09 | Send/receive email patterns, React Email | FOSS |
| 2 | **marketingskills (email-sequence, onboarding, copy)** | https://github.com/coreyhaines31/marketingskills | Community | 54.2k | 2026-10-08 | Lifecycle email & form/CRO copy | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **React Hook Form** | https://github.com/react-hook-form/react-hook-form | OSS | 44.9k | 2026-10-10 | Form state/validation | FOSS |
| 2 | **listmonk** | https://github.com/knadh/listmonk | OSS | 23.7k | 2026-10-11 | Self-hosted newsletter manager | FOSS |
| 3 | **React Email** | https://github.com/resend/react-email | Official (Resend) | 19.8k | 2026-10-08 | Build emails in React | FOSS |
| 4 | **Formbricks** | https://github.com/formbricks/formbricks | OSS | 13.1k | 2026-10-10 | Open-source surveys/forms | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Resend MCP (remote mcp.resend.com)** | https://resend.com/docs/mcp-server | Official | — | — | Send email, contacts, broadcasts, domains | Free 3,000/mo (100/day) |
| 2 | **Loops MCP (remote)** | https://loops.so/docs/mcp-server | Official | — | — | Contacts, campaigns, transactional | Free 1,000 contacts / 4,000 sends |
| 3 | **Postmark MCP** | https://github.com/ActiveCampaign/postmark-mcp | Official | 57 | 2026-09-28 | Transactional send/templates/diagnostics | Free 100 test emails/mo |
| 4 | **Tally MCP (remote)** | https://developers.tally.so/api-reference/mcp | Official | — | — | Create forms, read submissions | Free plan, unlimited forms |

---

## 11. Testing, QA & accessibility


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **webapp-testing** | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Official | 180.5k | 2026-10-09 | Playwright-based testing of your own app | FOSS |
| 2 | **test-driven-development / browser-testing-with-devtools** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | TDD pyramid + DevTools-driven verification | FOSS |
| 3 | **Superpowers (TDD, verification-before-completion)** | https://github.com/obra/superpowers | Community | 297.5k | 2026-10-10 | Red-green-refactor discipline | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Playwright** | https://github.com/microsoft/playwright | Official (Microsoft) | 97.5k | 2026-10-10 | E2E testing | FOSS |
| 2 | **Playwright CLI** | https://github.com/microsoft/playwright-cli | Official | 13.9k | 2026-09-28 | Token-efficient Playwright CLI for coding agents | FOSS |
| 3 | **Vitest** | https://github.com/vitest-dev/vitest | OSS | 17.2k | 2026-10-10 | Unit/component tests | FOSS |
| 4 | **axe-core** | https://github.com/dequelabs/axe-core | Official (Deque) | 7.6k | 2026-10-09 | Accessibility engine | FOSS |
| 5 | **Pa11y** | https://github.com/pa11y/pa11y | OSS | 4.6k | 2026-09-28 | CLI accessibility testing | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Chrome DevTools MCP** | https://github.com/ChromeDevTools/chrome-devtools-mcp | Official (Google) | 53.3k | 2026-10-11 | Console, network, screenshots, lighthouse_audit (a11y/SEO/best-practices) | FOSS |
| 2 | **Playwright MCP** | https://github.com/microsoft/playwright-mcp | Official | 38.0k | 2026-10-08 | Deterministic browser automation for E2E | FOSS |
| 3 | **BrowserStack MCP** | https://github.com/browserstack/mcp-server | Official | 154 | 2026-10-09 | Real devices, a11y | Free for open-source projects; trial |

---

## 12. Performance


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **performance-optimization + web-performance-auditor (/webperf)** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | Measure-first Core Web Vitals workflow | FOSS |
| 2 | **vercel-optimize / react-best-practices** | https://github.com/vercel-labs/agent-skills | Official | 32.2k | 2026-08-28 | Next/React perf patterns | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Lighthouse** | https://github.com/GoogleChrome/lighthouse | Official (Google) | 30.9k | 2026-10-11 | Perf/SEO/a11y audits | FOSS |
| 2 | **web-vitals** | https://github.com/GoogleChrome/web-vitals | Official | 8.6k | 2026-10-06 | Field CWV measurement | FOSS |
| 3 | **Lighthouse CI** | https://github.com/GoogleChrome/lighthouse-ci | Official | 7.1k | 2026-03-27 | Lighthouse on every commit (last push Mar 2026) | FOSS |
| 4 | **Unlighthouse** | https://github.com/harlan-zw/unlighthouse | Community | 4.9k | 2026-10-11 | Lighthouse across the whole site | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Chrome DevTools MCP** | https://github.com/ChromeDevTools/chrome-devtools-mcp | Official | 53.3k | 2026-10-11 | Perf traces + CrUX field data + insights | FOSS |
| 2 | **lighthouse-mcp** | https://github.com/priyankark/lighthouse-mcp | Community | 211 | 2026-10-06 | Full Lighthouse incl. performance via MCP (niche, <1k★) | FOSS |

---

## 13. SEO


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **marketingskills (seo-audit, programmatic-seo, schema-markup, site-architecture, ai-seo)** | https://github.com/coreyhaines31/marketingskills | Community | 54.2k | 2026-10-08 | De-facto SEO/CRO skill pack | FOSS |
| 2 | **claude-seo** | https://github.com/AgriciDaniel/claude-seo | Community | 18.7k | 2026-10-04 | 26 sub-skills + 19 subagents: technical SEO, E-E-A-T, schema, GEO, content | FOSS |
| 3 | **open-seo-mcp-skills** | https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills | Community | 4.7k | 2026-09-24 | SEO + GEO skills with a free MCP (keyword research, audits, rank tracking) | FOSS; vet before use (young repo, fast star growth) |
| 4 | **iannuttall/seo** | https://github.com/iannuttall/seo | Community | 568 | 2026-09-27 | 70+ SEO audit tools via local CLI + MCP using your own credentials | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **OpenSEO** | https://github.com/every-app/open-seo | Community | 23.1k | 2026-10-08 | Open-source Semrush/Ahrefs alternative | FOSS |
| 2 | **next-seo** | https://github.com/garmeeh/next-seo | OSS | 8.5k | 2026-07-29 | Meta/OG/JSON-LD for Next.js | FOSS |
| 3 | **next-sitemap** | https://github.com/iamvishnusankar/next-sitemap | OSS | 3.7k | 2026-05-13 | sitemap.xml + robots.txt for Next.js | FOSS |
| 4 | **SerpBear** | https://github.com/towfiqi/serpbear | OSS | 2.1k | 2026-05-14 | Self-hosted rank tracker | FOSS |
| 5 | **python-seo-analyzer** | https://github.com/sethblack/python-seo-analyzer | OSS | 1.5k | 2026-10-08 | Crawl-based on-page SEO analysis | FOSS |
| 6 | **Nuxt SEO** | https://github.com/harlan-zw/nuxt-seo | OSS | 1.4k | 2026-10-11 | Technical SEO + AEO for Nuxt | FOSS |
| 7 | **astro-seo** | https://github.com/jonasmerlin/astro-seo | OSS | 1.4k | 2026-08-28 | SEO tags for Astro | FOSS |
| 8 | **schema-dts** | https://github.com/google/schema-dts | Official (Google) | 1.2k | 2026-10-02 | Typed Schema.org JSON-LD | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **mcp-gsc (Google Search Console)** | https://github.com/AminForou/mcp-gsc | Community | 1.9k | 2026-09-15 | Clicks, queries, coverage, URL inspection | FOSS; GSC is free |
| 2 | **Google Analytics MCP** | https://github.com/googleanalytics/google-analytics-mcp | Official (Google) | 3.4k | 2026-10-02 | GA4 traffic data for SEO | FOSS; GA4 free |
| 3 | **Chrome DevTools MCP (lighthouse_audit)** | https://github.com/ChromeDevTools/chrome-devtools-mcp | Official | 53.3k | 2026-10-11 | Lighthouse SEO + a11y audits | FOSS |
| 4 | **search-console-mcp** | https://github.com/saurabhsharma2u/search-console-mcp | Community | 300 | 2026-09-02 | GSC + Bing Webmaster + GA in one server | FOSS |
| 5 | **Bing Webmaster MCP** | https://github.com/isiahw1/mcp-server-bing-webmaster | Community | 28 | 2026-02-10 | Bing Webmaster API (no official Bing MCP exists) | FOSS; Bing WMT free; low stars, only option |

---

## 14. GEO / AEO / AI-search visibility / llms.txt


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **marketingskills: ai-seo** | https://github.com/coreyhaines31/marketingskills | Community | 54.2k | 2026-10-08 | Optimize for AI answers/citations (LLMO/GEO) | FOSS |
| 2 | **claude-seo: seo-geo** | https://github.com/AgriciDaniel/claude-seo | Community | 18.7k | 2026-10-04 | GEO sub-skill: AI Overviews, citations, llms.txt | FOSS |
| 3 | **open-seo-mcp-skills (GEO skills)** | https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills | Community | 4.7k | 2026-09-24 | GEO/AI-visibility skills + MCP | FOSS; vet before use |
| 4 | **orangeo AI-visibility skill** | https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill | Community | 140 | 2026-06-09 | Checks robots.txt for AI bots, llms.txt, schema, citation signals (niche, <1k★) | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **llms.txt spec** | https://github.com/AnswerDotAI/llms-txt | Standard (Answer.AI) | 2.7k | 2026-09-24 | The /llms.txt proposal + tooling | FOSS |
| 2 | **llms-txt-hub** | https://github.com/thedaviddias/llms-txt-hub | Community | 912 | 2026-10-11 | Largest directory of llms.txt sites/tools | FOSS |
| 3 | **GEO paper code (Princeton, KDD 2024)** | https://github.com/GEO-optim/GEO | Research | 339 | 2025-10-30 | Reference implementation of "GEO: Generative Engine Optimization" | FOSS (research code; last push Oct 2025) |
| 4 | **geo-score** | https://github.com/jianruntech/geo-score | Community | 513 | 2026-10-11 | 0–100 AI-citability score on an open GEO rubric | FOSS |
| 5 | **GetCito** | https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool | Community | 484 | 2026-09-28 | Open-source AIO/AEO/GEO tracker | FOSS |
| 6 | **OneGlanse** | https://github.com/oneglanse/oneglanse | Community | 211 | 2026-10-04 | Tracks brand visibility in ChatGPT, Perplexity, Gemini, Claude, AI Overviews | FOSS |
| 7 | **nuxt-llms (+ starlight-llms-txt, mkdocs-llmstxt)** | https://github.com/nuxt-content/nuxt-llms | Official (Nuxt) | 171 | 2026-10-11 | Auto-generate /llms.txt from your site | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Chrome DevTools MCP** | https://github.com/ChromeDevTools/chrome-devtools-mcp | Official | 53.3k | 2026-10-11 | lighthouse_audit includes an "agentic browsing" category | FOSS |
| 2 | **Firecrawl MCP** | https://github.com/firecrawl/firecrawl-mcp-server | Official | 7.6k | 2026-10-09 | See your pages as AI crawlers do; build llms.txt input | Free 1,000 credits/mo |
| 3 | **Exa MCP** | https://github.com/exa-labs/exa-mcp-server | Official | 5.1k | 2026-10-07 | Run AI-search-style queries to check whether you get cited | Free $10/mo |

---

## 15. Analytics, monitoring & error tracking


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Sentry skills** | https://github.com/getsentry/skills | Official | 1.0k | 2026-10-09 | Sentry team's own dev skills | FOSS |
| 2 | **observability-and-instrumentation** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | Logging, RED metrics, OTel tracing | FOSS |
| 3 | **analytics-tracking** | https://github.com/coreyhaines31/marketingskills | Community | 54.2k | 2026-10-08 | Event/tracking-plan setup | FOSS |
| 4 | **PostHog skills** | https://github.com/PostHog/skills | Official | 72 | 2026-10-11 | PostHog integration skills (marked "under construction") | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Uptime Kuma** | https://github.com/louislam/uptime-kuma | OSS | 92.3k | 2026-10-11 | Self-hosted uptime monitoring | FOSS |
| 2 | **Sentry** | https://github.com/getsentry/sentry | OSS | 45.5k | 2026-10-11 | Error tracking (self-hostable) | FOSS or Free tier |
| 3 | **PostHog** | https://github.com/PostHog/posthog | OSS | 40.2k | 2026-10-11 | Product analytics, replay, flags | FOSS or Free tier |
| 4 | **Umami** | https://github.com/umami-software/umami | OSS | 39.3k | 2026-10-10 | Privacy-first analytics | FOSS |
| 5 | **SigNoz** | https://github.com/SigNoz/signoz | OSS | 32.3k | 2026-10-11 | OpenTelemetry observability | FOSS |
| 6 | **Plausible CE** | https://github.com/plausible/analytics | OSS | 29.4k | 2026-10-09 | Privacy analytics (self-host) | FOSS (AGPL) |
| 7 | **OpenPanel** | https://github.com/Openpanel-dev/openpanel | OSS | 7.1k | 2026-10-09 | Web + product analytics | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Sentry MCP (remote mcp.sentry.dev; repo now getsentry/toolkit)** | https://github.com/getsentry/toolkit | Official | 924 | 2026-10-10 | Issues, stack traces, Seer | Free Developer plan |
| 2 | **PostHog MCP (remote)** | https://posthog.com/docs/model-context-protocol | Official | — | — | Analytics, flags, errors, SQL | Free 1M events/mo |
| 3 | **Google Analytics MCP** | https://github.com/googleanalytics/google-analytics-mcp | Official | 3.4k | 2026-10-02 | GA4 reports | Free |
| 4 | **Grafana MCP** | https://github.com/grafana/mcp-grafana | Official | 3.5k | 2026-10-09 | Dashboards, Prometheus/Loki queries | FOSS with self-hosted Grafana |
| 5 | **Umami MCP (@umami/mcp)** | https://docs.umami.is/docs/mcp | Official | 39.3k | 2026-10-10 | Query Umami stats | FOSS / Cloud Hobby free |

---

## 16. Version control & CI/CD


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Claude Code plugins: commit-commands, code-review, pr-review-toolkit** | https://github.com/anthropics/claude-code/tree/main/plugins | Official | 150.2k | 2026-10-10 | Commits, PR review workflows | FOSS |
| 2 | **ci-cd-and-automation / shipping-and-launch** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | Quality-gate pipelines, staged rollouts | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **act** | https://github.com/nektos/act | OSS | 72.3k | 2026-08-09 | Run GitHub Actions locally | FOSS |
| 2 | **Claude Code Action** | https://github.com/anthropics/claude-code-action | Official | 9.5k | 2026-10-09 | @claude in PRs/issues | FOSS (needs Anthropic API/plan) |
| 3 | **release-please** | https://github.com/googleapis/release-please | Official (Google) | 7.6k | 2026-10-08 | Automated releases/changelogs | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **GitHub MCP** | https://github.com/github/github-mcp-server | Official | 33.5k | 2026-10-08 | Repos, PRs, issues, Actions, code scanning | FOSS; GitHub Free |
| 2 | **GitLab MCP (built-in)** | https://docs.gitlab.com/user/model_context_protocol/mcp_server/ | Official | — | — | Issues/MRs/pipelines | GitLab Free tier |
| 3 | **Git reference server** | https://github.com/modelcontextprotocol/servers | Official (MCP) | 91.1k | 2026-10-11 | Local git operations | FOSS |

---

## 17. Hosting, deployment, DNS & domains


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Cloudflare skills** | https://github.com/cloudflare/skills | Official | 3.0k | 2026-10-10 | Workers/Pages/R2/DNS | FOSS |
| 2 | **vercel-deploy-claimable** | https://github.com/vercel-labs/agent-skills | Official | 32.2k | 2026-08-28 | Deploy to Vercel with a claimable URL | FOSS |
| 3 | **HashiCorp agent-skills** | https://github.com/hashicorp/agent-skills | Official | 892 | 2026-10-05 | Terraform/infra skills | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Coolify** | https://github.com/coollabsio/coolify | OSS | 62.9k | 2026-10-11 | Self-hosted Vercel/Heroku | FOSS |
| 2 | **Dokploy** | https://github.com/Dokploy/dokploy | OSS | 37.8k | 2026-10-08 | Self-host PaaS (Docker/Traefik) | FOSS |
| 3 | **Vercel CLI** | https://github.com/vercel/vercel | Official | 16.4k | 2026-10-07 | Deploy/preview from terminal | FOSS |
| 4 | **CapRover** | https://github.com/caprover/caprover | OSS | 15.2k | 2026-10-09 | Docker + nginx PaaS | FOSS |
| 5 | **Kamal** | https://github.com/basecamp/kamal | OSS (37signals) | 14.6k | 2026-10-08 | Zero-downtime deploys to any server | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Cloudflare MCP (remote mcp.cloudflare.com)** | https://github.com/cloudflare/mcp-server-cloudflare | Official | 4.4k | 2026-10-09 | Code-mode API: Workers, DNS, R2, Registrar | Free plan |
| 2 | **Vercel MCP (remote mcp.vercel.com)** | https://vercel.com/docs/agent-resources/vercel-mcp | Official | — | — | Deployments, logs, runtime errors | Hobby free but NON-COMMERCIAL |
| 3 | **Netlify MCP** | https://github.com/netlify/netlify-mcp | Official | 67 | 2026-10-10 | Deploy, env vars, functions, forms | Free 300 credits/mo |
| 4 | **Render MCP** | https://github.com/render-oss/render-mcp-server | Official | 179 | 2026-10-10 | Services, logs, DBs | Free instances (sleep after 15 min) |
| 5 | **Railway MCP (remote mcp.railway.com)** | https://docs.railway.com/ai/mcp-server | Official | — | — | Projects, deploys | Trial credits, then $1/mo free plan |
| 6 | **Coolify built-in MCP** | https://github.com/coollabsio/coolify | Official | 62.9k | 2026-10-11 | Read-only server/app status | FOSS |
| 7 | **Dokploy MCP** | https://github.com/Dokploy/mcp | Official | 395 | 2026-09-23 | Manage Dokploy apps | FOSS |

---

## 18. Security


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Cloudflare security-audit-skill** | https://github.com/cloudflare/security-audit-skill | Official (Cloudflare) | 28.2k | 2026-09-14 | Multi-phase security audit with independently verified findings | FOSS |
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

---

## 19. Maintenance & iteration


### A. Skills

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Superpowers (systematic-debugging)** | https://github.com/obra/superpowers | Community | 297.5k | 2026-10-10 | Root-cause debugging discipline | FOSS |
| 2 | **debugging-and-error-recovery / documentation-and-adrs** | https://github.com/addyosmani/agent-skills | Community | 104.8k | 2026-10-10 | Triage → fix → guard; ADRs | FOSS |
| 3 | **Matt Pocock skills** | https://github.com/mattpocock/skills | Community | 285.7k | 2026-10-09 | Day-to-day engineering skills for long-lived repos | FOSS |

### B. GitHub repos

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Renovate** | https://github.com/renovatebot/renovate | OSS | 22.7k | 2026-10-11 | Automated dependency updates | FOSS |
| 2 | **Claude Code Action** | https://github.com/anthropics/claude-code-action | Official | 9.5k | 2026-10-09 | Automated fixes/reviews from issues | FOSS |
| 3 | **Uptime Kuma** | https://github.com/louislam/uptime-kuma | OSS | 92.3k | 2026-10-11 | Know when the site is down | FOSS |

### C. Free MCP servers

| # | Name | URL | Official? | ★ | Last push | Purpose | Free notes |
|---|---|---|---|---|---|---|---|
| 1 | **Sentry MCP** | https://github.com/getsentry/toolkit | Official | 924 | 2026-10-10 | Error → fix loop | Free Developer plan |
| 2 | **GitHub MCP** | https://github.com/github/github-mcp-server | Official | 33.5k | 2026-10-08 | Issues/PRs for iteration | FOSS |
| 3 | **Notion MCP** | https://github.com/makenotion/notion-mcp-server | Official | 4.7k | 2026-09-20 | Changelog/roadmap docs | Notion Free |

---

## Quick-install starter set (best free skill + repo + MCP per stage)

| Stage | Skill | Repo | MCP |
|---|---|---|---|
| 1. Planning | Superpowers | Spec Kit | Taskmaster MCP |
| 2. Research | last30days | Firecrawl (or Crawl4AI) | Playwright MCP / Firecrawl MCP |
| 3. Design | UI UX Pro Max + frontend-design | shadcn/ui | Figma remote MCP (or shadcn MCP) |
| 4. Assets | canvas-design (Anthropic) | sharp + Lucide | Hugging Face MCP |
| 5. Frontend | Vercel agent-skills | Next.js / Astro | Context7 |
| 6. Backend | Supabase agent-skills | Supabase | Supabase MCP |
| 7. Auth | Better Auth skills | Better Auth | Better Auth docs MCP |
| 8. CMS | WordPress/Sanity toolkit (if used) | Payload (or MDX in Git) | Sanity MCP / Payload MCP plugin |
| 9. Payments | Stripe skills (stripe/ai) | stripe-node / Polar | Stripe MCP (test mode) |
| 10. Email & forms | Resend skills | React Email + React Hook Form | Resend MCP + Tally MCP |
| 11. Testing | webapp-testing | Playwright | Playwright MCP |
| 12. Performance | addyosmani performance-optimization | Lighthouse / Unlighthouse | Chrome DevTools MCP |
| 13. SEO | marketingskills + claude-seo | next-seo + next-sitemap + schema-dts | mcp-gsc + GA MCP |
| 14. GEO | marketingskills ai-seo | llms.txt spec + framework llms plugin | Chrome DevTools MCP (agentic-browsing audit) |
| 15. Analytics | Sentry skills | PostHog / Umami | Sentry MCP + PostHog MCP |
| 16. VCS & CI | Claude Code commit/review plugins | Claude Code Action | GitHub MCP |
| 17. Hosting | Cloudflare skills | Coolify (self-host) / Vercel CLI | Cloudflare MCP |
| 18. Security | Cloudflare security-audit-skill | Gitleaks + Semgrep | Semgrep MCP |
| 19. Maintenance | Superpowers systematic-debugging | Renovate | Sentry MCP + GitHub MCP |

**Minimal install (about 10 commands):**
```bash
npx skills add obra/superpowers
npx skills add vercel-labs/agent-skills
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
npx skills add coreyhaines31/marketingskills
npx skills add supabase/agent-skills
# MCPs (Claude Code syntax; other clients take the same URL/command)
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add playwright -- npx @playwright/mcp@latest
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim
claude mcp add --transport http supabase "https://mcp.supabase.com/mcp?read_only=true"
claude mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
claude mcp add --transport http stripe https://mcp.stripe.com
```
(The Context7 URL and the Playwright package name come from the vendors' READMEs; check each README for the current install line.)


## Counts

| Stage | Skills | Repos | Free MCPs |
|---|---|---|---|
| 1. Planning, requirements & spec | 6 | 7 | 4 |
| 2. Research, competitor analysis & scraping | 3 | 8 | 6 |
| 3. UX/UI design & design systems | 6 | 8 | 7 |
| 4. Assets: images, icons, fonts, video | 3 | 7 | 3 |
| 5. Frontend scaffolding & code generation | 5 | 8 | 5 |
| 6. Backend, BaaS & database | 5 | 6 | 7 |
| 7. Auth | 3 | 7 | 3 |
| 8. CMS & content | 2 | 6 | 6 |
| 9. Payments & e-commerce | 2 | 5 | 5 |
| 10. Email & forms | 2 | 4 | 4 |
| 11. Testing, QA & accessibility | 3 | 5 | 3 |
| 12. Performance | 2 | 4 | 2 |
| 13. SEO | 4 | 8 | 5 |
| 14. GEO / AEO / AI-search visibility / llms.txt | 4 | 7 | 3 |
| 15. Analytics, monitoring & error tracking | 4 | 7 | 5 |
| 16. Version control & CI/CD | 2 | 3 | 3 |
| 17. Hosting, deployment, DNS & domains | 3 | 5 | 7 |
| 18. Security | 5 | 8 | 3 |
| 19. Maintenance & iteration | 3 | 3 | 3 |
| **Total (entries, some repeated across stages)** | **67** | **116** | **84** |

## Sources and registries used

- **GitHub search API** (via the cursor-github connector): keyword and topic searches (`topic:agent-skills`, "seo mcp", "llms.txt", "generative engine optimization", "search console mcp", "ai visibility tracker", security/testing/a11y skills) plus batch `repo:` checks for stars, archived status and last push.
- **Official MCP Registry:** https://github.com/modelcontextprotocol/registry (registry.modelcontextprotocol.io). **Reference servers:** https://github.com/modelcontextprotocol/servers
- **MCP directories:** punkpeye/awesome-mcp-servers (glama.ai/mcp/servers), wong2/awesome-mcp-servers (mcpservers.org), smithery.ai, mcp.so, PulseMCP (pulsemcp.com), RankSpotAI/awesome-seo-mcp (an SEO-specific list).
- **Skill registries and collections:**
  - anthropics/skills and the agentskills.io spec (agentskills/agentskills).
  - anthropics/claude-plugins-official and anthropics/claude-code/plugins.
  - vercel-labs/skills (skills.sh) and vercel-labs/agent-skills.
  - VoltAgent/awesome-agent-skills, ComposioHQ/awesome-claude-skills, travisvn/awesome-claude-skills, hesreallyhim/awesome-claude-code.
  - sickn33/agentic-awesome-skills, alirezarezvani/claude-skills, wshobson/agents.
  - SkillsMP (skillsmp.com), claude-plugins.dev/skills, openai/skills, github/awesome-copilot, PatrickJS/awesome-cursorrules, bergside/awesome-design-skills.
- **Vendor docs used to confirm hosted MCPs:** Figma, Google Stitch, shadcn, Astro, Svelte, Supabase, Neon, Firebase, Convex, Appwrite, Turso, Clerk, Better Auth, Sanity, Strapi, Payload, Stripe, Polar, Paddle, Shopify, Resend, Loops, Tally, Vercel, Netlify, Railway, Cloudflare, Sentry, PostHog, Umami, GitLab, Semgrep.
- **Pricing and free-tier claims** come from pricing.md (checked against vendor pricing pages today).
