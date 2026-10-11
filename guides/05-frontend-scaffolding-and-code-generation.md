# 5. Frontend scaffolding and code generation (plus docs-grounding)

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

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
