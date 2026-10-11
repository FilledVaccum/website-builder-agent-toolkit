# Pricing: free vs paid (companion to report.md)

*Checked Oct 11, 2026 (MYT) against vendors' official pricing pages, fetched live (curl, or WebFetch for pages rendered with JavaScript). A few pages wouldn't render; for those I used the vendor's own docs or pricing pages through web search, and each one is marked that way. Prices are USD unless noted. Vendors change these often, so recheck before you commit.*

## Ground rules

- **The MCP servers and agent skills themselves cost nothing.** Every MCP server, SKILL.md pack and repo in report.md is free (open source, or a free hosted endpoint). What costs money is the **account on the underlying service** the MCP talks to (Supabase, Vercel, Stripe…), plus your **LLM/IDE subscription** (Claude, Cursor, Codex and so on, which is outside the scope of this table).
- **Categories:**
  - **FOSS** = free and open source; self-host it and pay only for the server.
  - **Free tier** = freemium, with the key limits and the entry paid price listed.
  - **Paid** = paid only (a trial may exist).
  - **Usage** = usage-based or pay-as-you-go.
- **Commercial-use flags:**
  - **Vercel Hobby is the only free tier where I verified an explicit "personal, non-commercial use" clause** (on vercel.com/pricing).
  - Several others are *positioned* for personal or hobby use (Render Hobby, Kinde Free, Appwrite Free), but I didn't check their ToS, so they're marked ⚠️ positioning only.
  - Some free tiers are commercially usable but awkward for production: Webflow Starter has no custom domain; Loops Free adds Loops branding; Supabase and Appwrite Free pause idle projects.
- **"Unverified"** means I couldn't confirm it on an official page today.

---

## 1. Planning and spec

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Spec Kit, OpenSpec, BMAD, Taskmaster, Superpowers, AGENTS.md | FOSS | — | — | Taskmaster calls an LLM API, which you pay for. |
| Kiro (IDE) | Free tier | Kiro Free: 50 credits/mo | Pro $20/mo, Pro+ $40/mo; add-on $0.04/credit | kiro.dev/pricing |
| Notion (+ MCP) | Free tier | Free plan (AI is trial only) | Plus $10/seat/mo | notion.com/pricing |
| Atlassian (Jira/Confluence) | Unverified | — | — | Not fetched. |

## 2. Research and scraping

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Firecrawl | Free tier | 1,000 credits/mo (≈1,000 pages), 2 concurrent | Hobby $16/mo billed yearly (5,000 credits) | firecrawl.dev/pricing |
| Exa | Free tier → Usage | $10 credits every month + $10 onboarding bonus | Usage-based (per-request pricing on page) | exa.ai/pricing |
| Tavily | Free tier → Usage | 1,000 API credits/mo | PAYG $0.008/credit | tavily.com/pricing |
| Apify | Free tier | $5 platform credit/mo | Starter $19/mo + PAYG ($0.2/compute unit) | apify.com/pricing |
| Bright Data | Usage (free tier) | Free tier on some APIs | ~$1 per 1k requests; proxies from $5/GB | brightdata.com/pricing |
| Browserbase | Free tier | 3 concurrent browsers, 1 browser hour | Developer $20/mo | browserbase.com/pricing |
| Crawl4AI, Stagehand, Playwright MCP, Open Lovable | FOSS | — | — | Stagehand/Open Lovable call LLM APIs, which you pay for. |

## 3. UI/UX design

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Figma (+ remote MCP) | Free tier | Starter: free, limited | Professional full seat $16/mo | Remote MCP works on all seats; the desktop MCP needs a Dev/Full paid seat (Figma docs). |
| shadcn/ui (+ MCP), Magic UI, Framelink, Penpot, Onlook | FOSS | — | — | Penpot also has a hosted version (pricing not checked). |
| 21st.dev Magic MCP | Free tier | Hobby: MCP search, 2 component copies/day | Builder $6/mo yearly ($8 quarterly); Builder+AI $15/mo yearly | Via 21st.dev pricing pages (web search; curl got a JS shell). |
| Canva (+ MCP) | Free tier | Canva Free | Pro $12/mo billed yearly ($144/yr) or $18/mo monthly | Via canva.com/pricing (web search). Varies by country. |
| frontend-design, ui-ux-pro-max, taste-skill, impeccable, Vercel skills | FOSS (skills) | — | — | — |

## 4. Assets

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Replicate | Usage | "Try for free" | Per run, e.g. FLUX 1.1 Pro / Recraft V3 **$0.04 per image** | replicate.com/pricing |
| fal.ai | Unverified | — | — | Not fetched. |
| Unsplash API, Iconify, Lucide, Google Fonts | FOSS / free | — | — | Unsplash API rate limits not checked. |
| ElevenLabs | Unverified | — | — | Not fetched. |

## 5. Frontend and docs-grounding

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Context7 | Free tier | 1,000 API calls/mo (then blocked, +20 bonus/day) | Pro $10/seat/mo (2,000 calls/seat, then $5/1k) | context7.com/plans |
| Ref | Free tier | 200 one-time credits | Pro $50/mo (6,000 credits); old $9 Basic closed | docs.ref.tools/usage/pricing (web search) |
| Next DevTools MCP, Astro Docs MCP, Svelte MCP, create-t3-app, better-t-stack, `npx skills` | FOSS | — | — | — |

## 6. Backend, database, auth

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| **Supabase** | Free tier | **2 active projects, 500 MB DB, 50k MAU, 1 GB storage, 5 GB egress; pauses after 1 week idle** | **Pro $25/mo** (incl. $10 compute credit; 8 GB disk, 100k MAU, 250 GB egress) | supabase.com/pricing |
| Firebase | Free tier → Usage | Spark (no-cost): e.g. Auth up to 50k MAU, Firestore 1 GiB, Hosting 10 GiB/mo transfer | Blaze PAYG (Spark quota still free; $300 credit if eligible) | firebase.google.com/pricing |
| Appwrite Cloud | Free tier ⚠️ "hobby" | 2 projects, 75k MAU, 2 GB storage, 5 GB bandwidth, 750k executions; **pauses after 1 week idle** | Pro $25/mo per project | Plan table via appwrite.io pricing (web search). Self-hosted = FOSS. |
| PocketBase | FOSS | — | — | Single binary; just your server. |
| Convex | Free tier | Free & Starter: 1M function calls/mo (then $2.20/1M), 20 GB-hours | Professional $25/developer/mo | convex.dev/pricing. Also self-hostable (FOSS). |
| Neon | Free tier → Usage | 100 projects, 1 GB storage/project, 100 CU-hours, scale-to-zero, no time limit | Launch: usage-based, **no monthly minimum** ($0.106/CU-hour) | neon.com/pricing |
| Turso | Free tier | 100 DBs, 5 GB, 500M rows read, 10M rows written/mo | Developer $4.99/mo | turso.tech/pricing |
| PlanetScale | Paid | No free tier | From $5/mo (dev/low-traffic) | planetscale.com/pricing |
| Prisma Postgres | Free tier | 200k operations/mo | Starter $10/mo (1M ops, then $8/M) | prisma.io/pricing. Prisma ORM is FOSS. |
| MongoDB Atlas | Free tier | M0: 512 MB, free forever | Flex ~$8–30/mo (hourly) | mongodb.com/pricing |
| Upstash Redis | Free tier → Usage | 500k commands/mo, 1 free DB | PAYG $0.20 per 100k commands | upstash.com/pricing/redis |
| Xata | FOSS | — | — | Cloud pricing not checked. |
| **Better Auth**, Auth.js | FOSS | — | — | $0; a library in your app. |
| Clerk | Free tier | **50,000 monthly retained users**, 100 retained orgs | Pro $25/mo ($20/mo yearly); then $0.02/MRU | clerk.com/pricing |
| Kinde | Free tier ⚠️ "hobbyists and personal projects" | 10,500 MAU | From $25/mo | kinde.com/pricing |

## 7. CMS

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Sanity | Free tier | 20 seats, 2 public datasets, 10k documents, 1M CDN req/mo, 100 GB assets & bandwidth | Growth $15/seat/mo | sanity.io/pricing. Startup program: 1 yr Growth free. |
| Payload, Strapi, Directus, TinaCMS, WordPress (self-host) | FOSS | — | — | Their hosted clouds weren't checked. |
| Contentful | Free tier | 1 space, 10 users, 100k API calls/mo, 50 GB CDN/mo, no overages | Lite €300/mo | Via contentful.com/pricing (web search). Expensive for indies. |
| Webflow | Free tier (not launchable) | Starter: 2 pages, 50 CMS items, 1 GB bandwidth, **webflow.io domain only** | Basic $15/mo yearly ($25 monthly); Premium (CMS) $25/mo yearly | Via Webflow help center (web search; May 2026 pricing change). |

## 8. Payments (all usage-based: you pay per transaction, with no monthly fee on the base plans)

| Item | Category | Fees | Notes |
|---|---|---|---|
| **Stripe** | Usage | **US: 2.9% + 30¢** domestic cards; +1% international (cross-border) plus currency conversion; disputes $15. **Malaysia account: 3% + RM1.00** domestic. | stripe.com/us/pricing and stripe.com/pricing (geo-localised to MY). Stripe is **not** a merchant of record: you handle tax (Stripe Tax is extra). |
| **Polar** (MoR) | Usage (+ optional plan) | **Starter (free): 5% + 50¢**; Pro $20/mo: 3.8% + 40¢; +1.5% for non-US cards | polar.sh/resources/pricing. Orgs created from May 27, 2026 start on Starter (the older 4% + 40¢ "Early Member" rate is closed). Handles global sales tax. |
| Paddle (MoR) | Usage | 5% + 50¢ | paddle.com/pricing |
| Lemon Squeezy (MoR) | Usage | 5% + 50¢ (+ extras for international/PayPal/subscriptions) | lemonsqueezy.com/pricing |
| PayPal | Usage | US: 3.49% + fixed fee (checkout) | paypal.com business fees |
| Square, Shopify | Unverified | — | Not fetched. |

## 9–10. Testing, QA, performance, SEO

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Playwright MCP, Chrome DevTools MCP, browser-use, Lighthouse MCPs, axe scanner, marketingskills, mcp-gsc | FOSS | — | — | Google Search Console is free. |
| BrowserStack | Paid (free for OSS) | Free for open source; free trial | From $12.50/mo | browserstack.com/pricing |
| DataForSEO | Usage | Free tools only | PAYG, **$50 minimum payment** | dataforseo.com/pricing |
| Ahrefs | Unverified (paid) | — | — | Not fetched. |

## 11. Version control and CI

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| GitHub (+ MCP) | Free tier | Unlimited public/private repos; **2,000 Actions minutes/mo** (public repos free) | Team $4/user/mo (from GitHub pricing page) | github.com/pricing |
| Claude Code Action / Security Review | FOSS action + usage | Action is free | Needs an Anthropic API key (usage-based) or a Claude plan | Anthropic pricing not fetched (unverified). |
| GitLab | Unverified | — | — | Not fetched. |

## 12. Hosting, deploy, DNS

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
| GitHub Pages | Free | Static only | — | — |

## 13. Monitoring and analytics

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| **Sentry** | Free tier | Developer: **1 user**, 5k errors, email alerts, MCP access | Team $26/mo | sentry.io/pricing |
| **PostHog** | Free tier → Usage | **1M events, 5K session recordings, 1M flag requests/mo** | Usage-based beyond free | posthog.com/pricing |
| Umami | Free tier + FOSS | Cloud Hobby: 100k events/mo, 1 site; self-host free | Cloud Pro $20/mo (1M events) | umami.is/pricing |
| Plausible | Paid (cloud) + FOSS (CE) | Cloud: 30-day trial only. CE: free, self-hosted, AGPL | Cloud from $9/mo (10k pageviews) | plausible.io |
| Google Analytics | Free | Free (GA4) | Analytics 360 (enterprise) | marketingplatform.google.com |
| Vercel Web Analytics | Bundled with Vercel | — | — | — |
| Grafana Cloud | Unverified | — | — | Pricing page didn't render. |

## 14. Email, forms, files

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| **Resend** | Free tier | **3,000 emails/mo, max 100/day**, 3 domains; marketing: 1,000 contacts | **Pro $20/mo (50k emails)**, overage $0.90/1k | resend.com/pricing |
| Loops | Free tier | 1,000 subscribed contacts, 4,000 sends per rolling 30 days, **Loops branding** | $49/mo (1,001–5,000 contacts, unlimited sends) | loops.so/pricing + loops.so/.well-known/pricing.txt |
| Postmark | Free (test) → Paid | 100 emails/mo (testing) | Basic $15/mo (10k emails) | postmarkapp.com/pricing |
| **Tally** | Free tier | **Unlimited forms & submissions** (fair use), 10 MB upload cap | Pro $24/mo (pricing page) or $29/mo (help page): the vendor pages conflict | tally.so/pricing |
| UploadThing | Free tier | 2 GB storage | $10/mo (100 GB); usage-based from $25/mo (250 GB) | uploadthing.com/pricing |
| Netlify Forms | Inside Netlify credits | — | — | — |

## 15. Security

| Item | Category | Free tier / key limits | Entry paid price | Notes |
|---|---|---|---|---|
| Semgrep | Free tier + FOSS | Community Edition FOSS; platform free up to 10 contributors / 10 repos | Paid tiers (contact or page) | semgrep.dev/pricing |
| Snyk (+ agent-scan) | Free tier | 100 tests/mo (agent-scan itself is FOSS) | Team $25/mo | snyk.io/plans |
| Socket | Free tier | Free for individuals and small teams | Team $25/mo | socket.dev/pricing |
| Trail of Bits skills, ToolHive, Docker MCP Gateway, web-check | FOSS | — | — | — |

## 16. AI website builders and boilerplates

All FOSS: bolt.diy, Dyad, Open Lovable, Onlook, OpenHands, screenshot-to-code, Fragments, LlamaCoder, Open SaaS, nextjs/saas-starter, ixartz, BoxyHQ, create-t3-app. You pay only for the LLM API keys and hosting they use. (Hosted v0, Lovable, Bolt.new and Replit weren't checked.)

---

## Cheapest viable fully-free launch stack

| Layer | Pick | Free limit to watch |
|---|---|---|
| Framework + hosting | **Astro or Next.js on Cloudflare Workers/Pages** (not Vercel Hobby, which is non-commercial) | 100k Worker requests/day; static assets free |
| DB + auth + storage | **Supabase Free** (or Neon Free + Better Auth) | 500 MB DB, 50k MAU; **pauses after 7 days idle** (Neon scales to zero and doesn't pause-delete) |
| Auth | Supabase Auth or **Better Auth** ($0) | — |
| Files | Cloudflare R2 | 10 GB, egress free |
| Payments | **Stripe** (no monthly fee) or **Polar Starter** (MoR, 5% + 50¢) | Fees only on revenue |
| Email | **Resend Free** | 100/day, 3,000/mo |
| Forms | **Tally Free** | Unlimited |
| Analytics | **PostHog Free** (or Umami Cloud Hobby) | 1M events/mo |
| Errors | **Sentry Developer** | 1 user, 5k errors |
| Repo + CI | **GitHub Free** | 2,000 Actions min/mo |
| Domain + DNS | **Cloudflare Registrar** (at cost) + free DNS | The only unavoidable cost: domain registration at wholesale price |
| AI tooling | All MCPs and skills in report.md | $0 (LLM/IDE subscription not counted) |

**Fixed monthly cost at launch: $0 + domain** (Cloudflare charges wholesale, typically ~$10/yr for a .com; that figure wasn't checked today).

### What it costs once it outgrows the free tiers

| Trigger | Upgrade | Cost |
|---|---|---|
| >100k requests/day, or you need more Worker CPU | Cloudflare Workers Paid | **$5/mo** |
| DB > 500 MB, or you can't risk idle pausing | Supabase Pro | **$25/mo** |
| >100 emails/day | Resend Pro | **$20/mo** |
| Second teammate needs error access | Sentry Team | $26/mo (optional) |
| >1M analytics events | PostHog usage | Metered (pennies per extra event) |
| Choosing Next.js on Vercel instead of Cloudflare | Vercel Pro (required for commercial use) | $20/mo instead of $5 |

- **Lean paid stack:** Cloudflare $5 + Supabase $25 + Resend $20 ≈ **$50/mo**.
- **With Vercel Pro instead of Workers:** ≈ **$65/mo**.
- **Adding Sentry Team:** ≈ **$90/mo**.
- **On top:** payment fees (2.9% + 30¢ US Stripe / 3% + RM1 MY Stripe / 5% + 50¢ Polar) plus your LLM/IDE subscription.

**Self-hosted alternative:** one VPS (price not checked) running **Coolify or Dokploy (free)** + PocketBase or Appwrite (free) + Umami or Plausible CE (free) + Better Auth + Payload/Strapi, with Cloudflare in front (DNS and R2 free). Fixed cost ≈ VPS + domain, about 3–5x cheaper than the managed stack at small scale. You pay instead in ops time and backups.

### Couldn't verify today
Atlassian, fal.ai, ElevenLabs, Square, Shopify, Ahrefs, GitLab, Grafana Cloud, Anthropic API pricing for Claude Code Action, hosted Penpot/Payload/Strapi clouds, VPS prices, the exact .com price at Cloudflare, and the commercial-use ToS for Netlify, Render, Kinde and Appwrite free tiers.
