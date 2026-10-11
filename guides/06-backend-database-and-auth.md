# 6. Backend, database and auth (indie BaaS landscape)

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

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
