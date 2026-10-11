# Recommended indie stack (managed, generous free tiers)

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
