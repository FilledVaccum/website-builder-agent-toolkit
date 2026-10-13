# Free SEO / GEO catalog

Decisions follow the job order in `SKILL.md`, not star count. Popularity shifts. Re-check a repo before calling it "the most popular."

Install from the repo's current README. The commands below are the usual form, not a guarantee.

## Default path

| Step | Tool | Cost | Repo |
|---|---|---|---|
| Baseline | Chrome DevTools MCP (Lighthouse) | Free, no account | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| Baseline fallback | Google Lighthouse | Free, no account | https://github.com/GoogleChrome/lighthouse |
| Many URLs | Unlighthouse | Free, no account | https://github.com/harlan-zw/unlighthouse |
| Rankings | mcp-gsc | Free, needs the user's Google account on that property | https://github.com/AminForou/mcp-gsc |
| Bing | mcp-server-bing-webmaster | Free, needs the user's Bing API key | https://github.com/isiahw1/mcp-server-bing-webmaster |
| On-page audit | claude-seo | Free skill | https://github.com/AgriciDaniel/claude-seo |
| Citation audit | geo-seo-claude | Free skill | https://github.com/zubair-trabzada/geo-seo-claude |
| Fetched HTML | Firecrawl MCP | Free tier, needs the user's key | https://github.com/firecrawl/firecrawl-mcp-server |
| Rescore | geo-optimizer-skill | Free, no account | https://github.com/Auriti-Labs/geo-optimizer-skill |
| Who is cited | Exa MCP | Free monthly credits, needs the user's key | https://github.com/exa-labs/exa-mcp-server |

Usual skill install, when the README agrees:

```bash
npx skills add AgriciDaniel/claude-seo
npx skills add zubair-trabzada/geo-seo-claude
npx skills add Auriti-Labs/geo-optimizer-skill
```

Chrome DevTools MCP is an MCP server, not a skill. Add it in the MCP config the site already uses. Lighthouse itself is `npx lighthouse <url>`.

## Use only when the stack matches

| Tool | Use when | Do not use when | Repo |
|---|---|---|---|
| next-seo | Next.js Pages Router and the app does not already set meta tags | App Router with `metadata` / `generateMetadata` | https://github.com/garmeeh/next-seo |
| next-sitemap | Next.js Pages Router and there is no sitemap | `app/sitemap.ts` or another sitemap already exists | https://github.com/iamvishnusankar/next-sitemap |
| schema-dts | TypeScript and the project authors JSON-LD by hand | A schema helper already exists | https://github.com/google/schema-dts |
| Nuxt SEO | The site is Nuxt | Any other framework | https://github.com/harlan-zw/nuxt-seo |
| astro-seo | The site is Astro | Any other framework | https://github.com/jonasmerlin/astro-seo |
| nuxt-llms | The site is Nuxt and has no `llms.txt` | A hand-written `llms.txt` already exists | https://github.com/nuxt-content/nuxt-llms |

## Free, not on the default path

Install one of these only when the default tool cannot do that job.

| Tool | Job | Repo |
|---|---|---|
| Google Analytics MCP | Traffic, after GA4 is on the site. Needs the user's Google account | https://github.com/googleanalytics/google-analytics-mcp |
| search-console-mcp | GSC + Bing + GA in one server, if mcp-gsc is not enough | https://github.com/saurabhsharma2u/search-console-mcp |
| iannuttall/seo | Local crawl plus the user's own GSC and GA4 credentials | https://github.com/iannuttall/seo |
| python-seo-analyzer | One-shot on-page crawl | https://github.com/sethblack/python-seo-analyzer |
| LibreCrawl | Desktop crawl for a large site | https://github.com/PhialsBasement/LibreCrawl |
| seonaut | Self-hosted crawl and audit | https://github.com/StJudeWasHere/seonaut |
| SerpBear | Self-hosted rank history. The user picks the keywords and runs it | https://github.com/towfiqi/serpbear |
| Elmo | Ongoing "did the model cite us." Needs the user's model keys | https://github.com/elmohq/elmo |
| GetCito | Same job, alternate tracker | https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool |
| Notra | Asks buyer questions and records citations. Needs model access | https://github.com/usenotra/notra |
| OneGlanse | Brand mentions across assistants | https://github.com/oneglanse/oneglanse |
| llms.txt spec | Format reference when editing `/llms.txt` | https://github.com/AnswerDotAI/llms-txt |
| GEO paper code | Explains the method. Not an agent plugin | https://github.com/GEO-optim/GEO |
| AutoGEO | Research code for rewrites. Not an agent plugin | https://github.com/cxcscmu/AutoGEO |
| marketingskills | Large marketing pack. Its `ai-seo` skill overlaps the two default skills | https://github.com/coreyhaines31/marketingskills |
| awesome-generative-engine-optimization | Reading list, not a tool | https://github.com/amplifying-ai/awesome-generative-engine-optimization |

`open-seo-mcp-skills` (Ryze) is a hosted connector. Confirm it is still free for the calls you need before using it. It is not part of the default path.

## Paid — do not install

- OpenSEO (`every-app/open-seo`) — pay-as-you-go hosted data
- DataForSEO MCP — paid API
- Ahrefs MCP — paid API

Keyword gaps and backlink prospecting wait until the user already has a free data source (Search Console) or explicitly accepts a paid tool. This skill does not make that pitch.
