# Principles: how to read this (Knowledge / Method / Eyes / Hands)

*Researched Oct 11, 2026 (MYT) for Swap. Indie / solo-dev focus.*
*Star counts come from the GitHub search API on 2026-10-11 and are rounded. "Official" means the vendor maintains it. Remote MCP endpoints were checked against vendor docs. I left out anything I couldn't confirm.*

An agent building a website needs four kinds of help. Every item below fits one of them:

| Kind | What it gives the agent | Examples | Cost to the context window |
|---|---|---|---|
| **Knowledge** | Current docs and APIs, so it stops guessing from stale training data | Context7, Astro Docs MCP, Clerk MCP, `@shopify/dev-mcp` | Low |
| **Method** | How to do the job well: process and taste | spec-kit, Superpowers, `frontend-design`, ui-ux-pro-max, impeccable | Very low. Skills load on demand. |
| **Eyes** | It can see and check what it built | Playwright MCP, Chrome DevTools MCP | Medium |
| **Hands** | It can change real infrastructure: DB, deploys, payments, DNS | Supabase, Vercel, Stripe, Cloudflare MCPs | High, and **risky** |

**Opinionated rule:** use skills for *method*, docs MCPs for *knowledge*, one browser MCP for *eyes*, and as few *hands* MCPs as you can (scoped or read-only where possible). Most production damage from agents comes through the "hands" servers.

**What changed in 2025–2026:** most vendors replaced local `npx` servers with **hosted remote MCP servers that use OAuth** (`https://mcp.<vendor>.com/mcp`). Several well-known repos are now **archived** because the hosted endpoint took over (Browserbase, PostHog, Sanity, Railway, Semgrep, Prisma's standalone repo, ElevenLabs, Penpot, Ahrefs, Automattic's WordPress MCP, Storybook). Old blog posts and "awesome" lists still point at those dead installs.
