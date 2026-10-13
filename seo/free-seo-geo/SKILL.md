---
name: free-seo-geo
description: >-
  Plans and runs search-ranking and AI-citation (GEO/AEO) work for any website
  using only free tools. Starts by inventorying what the repo already ships,
  which free tools are installed, which are available, and what the user must
  authorize. Use when the user asks for SEO, GEO, AEO, llms.txt, schema,
  sitemaps, Search Console, AI citations, or ranking in search engines or
  AI assistants.
---

# Free SEO and AI citations

Works for any website. Do not assume a framework, a domain, or which files already exist. Discover them.

Run this against the site repository being optimized. This toolkit is a reference library, not the site.

## Rules

- Use free tools only. The paid list in [reference.md](reference.md) is out of scope. Do not install those, and do not propose them as the plan.
- A free tier that needs an account is not installed until the user creates that account. Ask for the credential that blocks the current step. Never ask them to paste a secret into chat; point them at the tool's own connect or OAuth flow.
- Run the inventory before recommending or installing anything. Treat its output as the source of truth for that workspace.
- Do not invent rankings, index coverage, or citation counts. Those come from Search Console, Bing Webmaster, or a citation check. A skill with no data connection describes the page; it does not know where the page ranks.
- Skip a framework SEO library when the inventory says the site already has that layer (metadata, sitemap, robots, JSON-LD).
- `llms.txt` helps assistants discover the site. It is not a ranking factor any engine has committed to. Google AI Overviews use the same ranking system as Google Search, so a page that is not indexed will not be cited.
- Head-term top 3 needs links and domain age. Prefer pages that match a specific query (benefits, eligibility, pricing, comparisons, docs for one product) before broad brand queries.
- Read the site's own notes (`CLAUDE.md`, `AGENTS.md`) when they exist. Site-specific constraints there override generic advice.

## First action

Pass the website root to `scripts/inventory.py` in this skill's directory:

```bash
python3 "<this-skill-dir>/scripts/inventory.py" "<website-root>"
```

If `python3` is missing, do the same checks by hand and use the report template below.

Then read [reference.md](reference.md) only for the tools the inventory marks available or needed. Do not load the whole catalog into the plan.

## Report this before any install

```markdown
## SEO inventory
- Site URL: [found candidate, or unknown]
- Stack: [from the script]
- Project notes: [paths, or none]

### Already in this project
- [robots, sitemap, llms.txt, JSON-LD, metadata — present or missing]

### Free tools installed
- [name — where]

### Free, no account, not installed
- [name — job]

### Needs you
- [account or key, which step it blocks, and that you will not paste it into chat]

### Not applicable
- [framework libraries that do not match this stack]

### Out of scope
- Paid tools stay unused.
```

If the site URL is unknown, ask for the canonical origin before auditing production. Do not guess from a package name.

## Order of work

Stop at the first step whose dependency is in **Needs you**. Do the steps above it. Continue when the user has authorized that dependency.

1. **Inventory.** Always.
2. **Technical baseline, no account.** If this session already has a browser or Lighthouse tool, use that. Otherwise, if Chrome DevTools MCP or Lighthouse is missing and the user asked to optimize, install the free no-account auditor from [reference.md](reference.md) using that repo's current README. Run it on five templates: home, one primary landing page, one article or doc, one page you hope will be cited, and one URL that should stay private (confirm it is disallowed). Record SEO, LCP, and CLS failures.
3. **Search Console.** Blocked until the user can open the property for this exact site. Read coverage, queries, and URL inspection for the five templates. Submit the sitemap if the property has none. Confirm the property host matches the canonical origin (`www` vs apex).
4. **Bing Webmaster.** Same sitemap, only if the user has a Bing key or asks for Bing. The connector is obscure and still the free one to use.
5. **On-page audit.** Use `claude-seo` if installed; otherwise install that free skill when the user asked to optimize. Feed it the Console numbers from step 3. Without Console, limit it to technical and schema findings and say ranks were not measured.
6. **Citation audit.** Use `geo-seo-claude` the same way. Check crawler rules, `llms.txt` depth, schema, and whether the answer is quotable. If `llms.txt` already exists, edit it. Do not add a second generator that overwrites a hand-maintained file.
7. **See the fetched HTML.** Use Firecrawl only when the user has a free-tier key and the baseline could not show what a crawler receives. Otherwise use the browser tools from step 2.
8. **Fix, in this order.**
   1. Indexing blockers: `noindex` on public pages, canonicals on the wrong host, sitemap URLs that redirect to login, soft 404s.
   2. Titles and descriptions on URLs that already get impressions and almost no clicks. Without Console, fix missing titles, descriptions, canonicals, and H1s only.
   3. Internal links from hubs to the specific-query pages.
   4. Citation shape on those pages: a direct answer in the first screen, named sources for any figure, and JSON-LD that matches the visible text.
   5. Public AI crawlers allowed (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended). Private, account, and API paths disallowed.
   6. `llms.txt` lists canonical public URLs only.
9. **Who gets cited.** After the fixes are deployed, run Exa if the user has a free key, using the real target queries. Record who is cited. Elmo or GetCito is the optional monthly tracker and needs the user's own model keys. Skip it until they ask.
10. **Re-measure.** Re-inspect the five URLs in Search Console about two weeks later. Re-run the citation queries. Optionally re-score with `geo-optimizer-skill`.

## Install policy

- Install a **free, no-account** tool only when the user asked to carry out the optimization, and only if the inventory says it is missing and applicable.
- Read the tool README for the current install command. Prefer `npx skills add <owner>/<repo>` for skills and the site's existing MCP config format for MCP servers. Match the file that is already there; do not invent a second config.
- Do not install `next-seo` or `next-sitemap` on a Next.js App Router site that already has `sitemap` and metadata. Do not install Nuxt or Astro SEO packages on any other stack.
- Do not install OpenSEO, DataForSEO, Ahrefs, or any other paid connector.
- Do not print API keys, service-account JSON, or `.env` values. The inventory script does not read `.env` files; do not work around that.

## What "optimized" means here

A page is in good shape when it is indexable on the canonical host, its title matches a query a person would type, the first screen answers that query, the schema matches the visible content, assistants are allowed to read it, and Search Console shows it indexed. Links from other sites are the remaining lever, and no tool in this skill creates them. Use Search Console and Exa to find pages worth pitching; the user places the links.

## More detail

Tool URLs, when each one applies, and the paid exclusions are in [reference.md](reference.md).
