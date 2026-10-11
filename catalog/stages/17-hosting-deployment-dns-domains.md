# Stage 17: Hosting, deployment, DNS & domains

> Source: free catalog (curated 2026-10-11). Tables: A = Skills, B = GitHub repos, C = Free MCP servers. See [legend](../00-legend-and-exclusions.md), [pricing](../../pricing/pricing.md).

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

## 💰 Pricing: paid services in this stage (free tier → paid)

*Checked 2026-10-11 on vendor pricing pages; USD. FOSS tools are omitted (they cost $0). Recheck before buying. Full detail: [pricing](../../pricing/pricing.md).*

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| **Vercel** | Free tier 🚫 **non-commercial** | Hobby: 1M CDN requests, 100 GB transfer, 1 GB Blob/mo | **Pro $20/mo** (+$20 usage credit) | vercel.com/pricing: "Hobby plan is for personal, non-commercial use." |
| **Cloudflare Workers/Pages** | Free tier → Usage | Workers Free: **100k requests/day**; Pages: 500 builds/mo; static assets free | Workers Paid **$5/mo minimum** (10M req + 30M CPU-ms incl.) | developers.cloudflare.com pricing/limits. No non-commercial clause on these pages. |
| **Cloudflare R2** | Free tier → Usage | 10 GB-month, 1M Class A, 10M Class B ops/mo; **egress always free** | $0.015/GB-month | developers.cloudflare.com/r2/pricing |
| Cloudflare Registrar | Usage (at cost) | — | Domains "at cost", no markup | cloudflare.com/products/registrar |
| Netlify | Free tier | **300 credits/mo hard cap** (credits cover deploys, compute, forms, bandwidth); never overcharges | Personal $9/mo; Pro $20/mo | netlify.com/pricing. Commercial-use terms not checked. |
| Render | Free tier ⚠️ "personal projects" | Free instances **spin down after 15 min idle**; free Postgres **expires after 30 days** | Paid instances from $7/mo; Pro workspace $25/mo | render.com/pricing + render.com/docs/free (web search) |
| Railway | Trial → Usage | 30-day trial with $5 credit, then $1/mo free plan (0.5 GB RAM) | Hobby $5/mo (incl. $5 usage); Pro $20/mo | railway.com/pricing |
| Fly.io | Usage | No free plan for new orgs (trial only); 10 GB volume free | Pay-as-you-go, no platform fee (example: app + 10 GB volume ≈ $5.19/mo) | fly.io/docs/about/pricing |
| **Coolify** | FOSS (+ optional cloud) | Self-host: free, all features | Coolify Cloud $5/mo (2 servers) + $3/server | coolify.io docs/pricing (web search) |
| **Dokploy** | FOSS (+ optional cloud) | Self-host: free | Cloud $4.50/server/mo (7-day trial) | dokploy.com/pricing |
