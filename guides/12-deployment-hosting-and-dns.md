# 12. Deployment, hosting and DNS (indie landscape)

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

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
