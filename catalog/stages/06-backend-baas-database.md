# Stage 6: Backend, BaaS & database

> Source: free catalog (curated 2026-10-11). Tables: A = Skills, B = GitHub repos, C = Free MCP servers. See [legend](../00-legend-and-exclusions.md), [pricing](../../pricing/pricing.md).

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

## 💰 Pricing: paid services in this stage (free tier → paid)

*Checked 2026-10-11 on vendor pricing pages; USD. FOSS tools are omitted (they cost $0). Recheck before buying. Full detail: [pricing](../../pricing/pricing.md).*

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| **Supabase** | Free tier | **2 active projects, 500 MB DB, 50k MAU, 1 GB storage, 5 GB egress; pauses after 1 week idle** | **Pro $25/mo** (incl. $10 compute credit; 8 GB disk, 100k MAU, 250 GB egress) | supabase.com/pricing |
| Firebase | Free tier → Usage | Spark (no-cost): e.g. Auth up to 50k MAU, Firestore 1 GiB, Hosting 10 GiB/mo transfer | Blaze PAYG (Spark quota still free; $300 credit if eligible) | firebase.google.com/pricing |
| Appwrite Cloud | Free tier ⚠️ "hobby" | 2 projects, 75k MAU, 2 GB storage, 5 GB bandwidth, 750k executions; **pauses after 1 week idle** | Pro $25/mo per project | Plan table via appwrite.io pricing (web search). Self-hosted = FOSS. |
| Convex | Free tier | Free & Starter: 1M function calls/mo (then $2.20/1M), 20 GB-hours | Professional $25/developer/mo | convex.dev/pricing. Also self-hostable (FOSS). |
| Neon | Free tier → Usage | 100 projects, 1 GB storage/project, 100 CU-hours, scale-to-zero, no time limit | Launch: usage-based, **no monthly minimum** ($0.106/CU-hour) | neon.com/pricing |
| Turso | Free tier | 100 DBs, 5 GB, 500M rows read, 10M rows written/mo | Developer $4.99/mo | turso.tech/pricing |
| PlanetScale | Paid | No free tier | From $5/mo (dev/low-traffic) | planetscale.com/pricing |
| Prisma Postgres | Free tier | 200k operations/mo | Starter $10/mo (1M ops, then $8/M) | prisma.io/pricing. Prisma ORM is FOSS. |
| MongoDB Atlas | Free tier | M0: 512 MB, free forever | Flex ~$8–30/mo (hourly) | mongodb.com/pricing |
| Upstash Redis | Free tier → Usage | 500k commands/mo, 1 free DB | PAYG $0.20 per 100k commands | upstash.com/pricing/redis |
