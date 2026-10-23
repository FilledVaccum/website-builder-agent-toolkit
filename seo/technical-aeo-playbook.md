# Technical AEO: what decides whether AI can read your site

You can make every page quotable and earn mentions everywhere, and still be invisible to AI if the crawlers can't reach or read your pages. This is the **technical access layer**, the third part of a series (1: make pages extractable; 2: earn third-party corroboration; 3: this). Adapted from an AEO article by the founder of an AI-visibility product; I removed their product promotion and the link to their paid workflow. Their statistics are cited but I haven't re-checked the sources.

- **Core point:** `llms.txt` is not a ranking factor, not a confirmed citation signal, and does not "unlock" ChatGPT. **A blocked request guarantees you can't be cited**; access alone doesn't make you win.
- **Related:** [AI recommendation playbook](ai-recommendation-playbook.md) (section 5 has the quick bot checks), [ChatGPT citation factors](chatgpt-citation-factors.md), [free-seo-geo](free-seo-geo/SKILL.md), [gap audit](ai-visibility-gap-audit.md).

## The 30-minute audit (do it in this order)

Don't start at the bottom because the bottom is easiest to ship. (Most audits reverse it because `llms.txt` is easy to screenshot and access logs aren't.)

| # | Check | Pass condition |
|---|---|---|
| 1 | **Search-crawler policy** | `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot` and `Googlebot` can reach public discovery pages |
| 2 | **Training policy** (separate decision) | You've chosen on purpose whether `GPTBot`, `ClaudeBot`, `Google-Extended` may crawl |
| 3 | **Actual responses** | CDN/firewall logs show mostly 200s for those bots, almost no unexplained 401/403/429, no CAPTCHA or challenge on public pages |
| 4 | **Rendered-content test** | A distinctive sentence from each core page appears in *View Source* |
| 5 | **Discovery and indexability** | Internal links, sitemap inclusion, canonical URL, no stray `noindex` / `nosnippet` |
| 6 | **Fetch reliability** | Few redirects, fast first byte, no 5xx |
| 7 | **Accurate schema** | `Organization` and page-specific types only where the same facts are visible |
| 8 | **Optional agent map** | A short `llms.txt`, then move on |

---

## Move 1. Put `llms.txt` in the right place (last)

A short Markdown file at the site root that explains the site and points to key pages.

| It can | It cannot |
|---|---|
| Give agents a quick map of the site | Override `robots.txt` |
| Point tools to product, docs and pricing pages | Open a page blocked by your CDN or firewall |
| Make a big documentation site easier to navigate | Put JavaScript-only content into the HTML |
| | Turn a weak page into a trusted source |
| | Force ChatGPT, Claude or Perplexity to cite you |

**Evidence:** Ahrefs reviewed traffic across **137,210 domains** and found **97% of valid `llms.txt` files received no requests** in the study period (as reported). Google's guidance says the usual Search requirements apply and asks for no special AI file.

**Order:** crawler access → source HTML → indexability and quality → `llms.txt` last. *The file is a map, not the front door.*

## Move 2. Allow the right bot for the right job

"AI crawler" covers three different jobs:

| Job | What it does | Bots |
|---|---|---|
| **Training crawlers** | Collect material that may influence a future model | `GPTBot` (OpenAI), `ClaudeBot` (Anthropic), `Google-Extended` (Google token controlling some Gemini training/grounding use of content Google already crawled) |
| **Search crawlers** | Build/refresh indexes used for current answers and citations | `OAI-SearchBot` (OpenAI), `Claude-SearchBot` (Anthropic), `PerplexityBot`; Google's AI Overviews and AI Mode use normal Google Search infrastructure, so the relevant crawler is `Googlebot` |
| **User-triggered fetchers** | Fetch a page when a person asks an assistant to open it | `ChatGPT-User`, `Claude-User`, `Perplexity-User` |

**What blocking does:**

- Blocking `GPTBot` opts out of potential OpenAI **training**; it does **not** by itself remove you from ChatGPT Search. Summaries, snippets and citations in ChatGPT Search need `OAI-SearchBot`.
- Blocking `Google-Extended` does **not** remove you from Google Search, AI Overviews or AI Mode (Google says so). `Googlebot` controls inclusion.

**Training access is a business decision; search visibility is a discovery decision.** You can allow one and block the other.

**Do this:**

1. Open `yourdomain.com/robots.txt` and search for those seven names, and for broad rules like `User-agent: * / Disallow: /`.
2. Check `noindex`, `nosnippet` and `max-snippet` directives on pages you want cited. A crawler must reach the page before it can read an on-page instruction.
3. Have the person managing the site test the homepage, pricing, product pages and docs: search bots should get a normal **200** on every public page you want discovered.

Example policy (search bots allowed, training decided separately; adapt, don't paste blindly):

```text
User-agent: OAI-SearchBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Googlebot
Allow: /

# Training: your call
User-agent: GPTBot
Disallow: /          # or Allow: /
User-agent: ClaudeBot
Disallow: /          # or Allow: /
User-agent: Google-Extended
Disallow: /          # or Allow: /

# Keep private areas out for everyone
User-agent: *
Disallow: /account/
Disallow: /api/
```

## Move 3. Check what happens before `robots.txt`

A clean `robots.txt` doesn't prove access. Your CDN, firewall, bot protection, rate limit, login wall or location rules can still block the request. Cloudflare introduced **default blocking of AI crawlers on newly onboarded domains in July 2025** and has since moved to more granular search / agent / training controls, which is the distinction your policy should make.

A typical failure: `robots.txt` says `Allow: /` and the browser gets 200, but `OAI-SearchBot` gets **403**; the team concludes the content "isn't authoritative", when authority was never tested. In a GetIntel sample the author cites, none of 37 pages already winning AI citations blocked a named AI crawler: access won't make you win, but a block stops you competing.

**Do this:** ask engineering for the last 30 days of requests from `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot` and `Googlebot`, counting response codes by bot. You want mostly 200 on public content, intentional 404s for URLs that don't exist, almost no unexplained 401/403/429, and no CAPTCHA/browser challenge on public editorial, product, pricing or docs pages.

Simulate a request from a terminal (the source omitted the command; this is mine):

```bash
for ua in OAI-SearchBot Claude-SearchBot PerplexityBot GPTBot ClaudeBot; do
  printf "%-16s " "$ua"
  curl -A "$ua" -s -o /dev/null -w "%{http_code}\n" https://yourdomain.com/pricing
done
```

A 200 only helps you spot an obvious block; it doesn't prove indexing. CDNs often verify real bots by IP, so a spoofed user-agent from your laptop can behave differently from the real bot. For permanent allowlists use the provider's published verification method or IP ranges. **Test the homepage, pricing, product, docs and the five pages you most want cited**; one successful homepage request proves almost nothing about the routes that matter.

## Move 4. Look at the HTML before JavaScript rescues it

Most dedicated AI crawlers don't run JavaScript (Vercel and MERJ tested several major ones and found they didn't render JS; Google, via Googlebot's rendering system, is the main exception). In GetIntel's sample, 35 of 37 highly cited pages returned readable text without JavaScript.

**Test:** open a core page → *View Page Source* → search for a distinctive sentence from the **middle** of the product description or article (not the headline or title tag). If it appears in the browser but not in the source, the page depends on JavaScript for its core content.

Put these in the **first HTML response**: page title and description, primary heading, product definition, pricing and plan details, comparison tables, documentation steps, and internal navigation to other citable pages. Keep calculators, filters, animations and account state on the client. For React/Next.js, server-render or statically generate public pages.

## Move 5. Treat speed as a fetch-reliability problem

There's no credible evidence that shaving 200 ms from a page lifts its ChatGPT citation rate, so don't invent a new GEO factor. The real issue: crawlers work under time, request and bandwidth limits. Slow origins, redirect chains, oversized responses, intermittent 5xx errors and aggressive rate limits reduce successful fetches. A page that times out can't be parsed.

(Contrast: one study summary in this repo reports faster pages cited more often, [ChatGPT citation factors](chatgpt-citation-factors.md). That's a correlation across sites; this article's point is reliability, not a speed ranking factor.)

**Do this:** for your ten most-wanted pages record: final HTTP status · number of redirects · time to first byte · size of the initial HTML · whether the core answer exists in that HTML. Fix in that order. A 3 MB JS bundle matters less to a non-rendering crawler than an HTML response containing only an empty `<div id="root">`, and a perfect Lighthouse score can't compensate for a 403. Also check your XML sitemap and internal links (a page must be discoverable before it can be fetched), keep canonical URLs stable, remove redirect chains, and return honest status codes.

## Move 6. Use schema to clarify visible content

Schema helps a machine label what's already on the page. `Organization` connects a company name to its logo, address and profiles; `Product` / `SoftwareApplication` describe a real offering; `FAQPage` identifies genuine visible Q&As. **It doesn't create evidence.** Google says structured data gives explicit clues, not to mark up invisible information, and that **no special schema is required for AI Overviews or AI Mode**.

Correct order: **(1)** put the fact in visible, server-rendered HTML → **(2)** mark up that same fact accurately → **(3)** validate. The wrong order is 600 lines of JSON-LD for a page that never states the claims in plain English.

**Do this:**

- `Organization` once on the homepage/About page, with `sameAs` links to canonical profiles.
- The most accurate product type on product pages, not every type you can find.
- `FAQPage` only where the page has a real visible Q&A.
- Validate with Google's Rich Results Test and the Schema.org Validator, and compare every marked-up claim with what a person can read.

## Move 7. Ship `llms.txt` for the job it does

Still worth shipping on many SaaS sites: not for a citation lift, but for **agents**. A compact Markdown map helps a coding agent, IDE assistant or support agent understand a documentation site without crawling every page. If you have an API, SDK, docs hub or agent workflow, it's cheap infrastructure.

```markdown
# Company or product name

> One factual paragraph explaining what the product does and for whom.

## Product
- [Overview](https://example.com/product): What this page contains
- [Pricing](https://example.com/pricing): Plans and billing details

## Documentation
- [Quickstart](https://example.com/docs/quickstart): First implementation
- [API reference](https://example.com/docs/api): Endpoints and authentication

## Optional
- [Changelog](https://example.com/changelog): Product updates
```

Use absolute canonical URLs; include the pages an agent needs, not every sitemap URL; generate it from the same content source as the site so it can't drift; return 200 as plain text/Markdown. **Give it one hour.** If it becomes a multi-week project, cancel it and fix the access log instead.

---

## Caveats

- **Vendor source.** The author sells an AI-visibility product; the "GetIntel sample of 37 pages" is their own small, non-random dataset. Treat it as an illustration.
- **Studies cited secondhand** (Ahrefs 137,210 domains, Vercel/MERJ crawler-rendering tests, Cloudflare's July 2025 default). I haven't re-read them; behaviour of crawlers and CDN defaults changes, so re-test your own site.
- **Bot names and behaviour change.** Check each provider's current crawler documentation before editing `robots.txt`.
- **Access isn't ranking.** Passing every check only lets you compete. Authority, quality and corroboration still decide who gets cited.
