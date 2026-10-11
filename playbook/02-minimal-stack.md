# Minimal end-to-end stack (≈10 items, works in Claude Code / Cursor / Codex)

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
