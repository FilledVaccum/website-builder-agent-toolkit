# AI visibility gap audit (GEO competitor-gap playbook)

A repeatable audit that shows **where AI assistants recommend competitors instead of you**, **why**, and **what to fix first**. You then rerun the exact same audit to prove the fix worked.

- **Use it for:** a product or service site that competes for buying decisions ("best X", "X vs Y", "X alternatives").
- **Engines:** ChatGPT, Claude, Gemini, Google AI Mode. Perplexity and Copilot are optional.
- **Cost:** free. It's mostly manual work. The free tools are listed in [Tooling](#tooling-free).
- **Relation to [free-seo-geo](free-seo-geo/SKILL.md):** that skill fixes *your site*. This playbook measures *the market* and decides which fixes matter. Run this first, then use free-seo-geo for steps 9 and 12.
- **Levers to pull after the audit** (engine differences, writing rules, mention tiers, YouTube, bot checks, GA4 measurement): [ai-recommendation-playbook.md](ai-recommendation-playbook.md).

> **Core rule:** measure before you write. Most wasted GEO work is new content written for a gap that turned out to be technical, a page that was out of date, or a third-party problem.

---

## The loop at a glance

| Phase | Steps | Output | Gate before the next phase |
|---|---|---|---|
| **A. Measure** | 1–4 | Results log (every answer, every run) | ≥ 3 runs on each high-value prompt, all engines |
| **B. Diagnose** | 5–7 | Topic scorecard + source map | Gaps ranked by size × value |
| **C. Root-cause** | 8–10 | One root cause per priority topic | Each topic is tagged with one cause from step 11 |
| **D. Act** | 11–13 | Change list (fix, update, new page, technical, third-party) | Changes deployed **and** recrawled |
| **E. Prove** | 14 | Before/after delta | Keep working the topics that moved |

---

## Definitions (keep these separate, always)

| Term | Meaning | Example |
|---|---|---|
| **Mention** | Your brand is named anywhere in the answer | "...tools like A, B and **You**" |
| **Recommendation** | The answer picks, ranks first, or endorses you for the user's need | "For SSO at a startup, **use You**" |
| **Citation** | One of your URLs appears as a source | Your blog linked while A is recommended |
| **Win** | A recommendation, ideally with a citation | |

A citation without a recommendation is **not a win**. Your page is feeding the engine's answer for someone else.

---

## Phase A: Measure

### 1. Build a fixed prompt set (30–50 prompts)

Write prompts around **buying decisions**, not keywords. Use the words a buyer would type before choosing.

| Intent bucket | Share | Template |
|---|---|---|
| Category | ~25% | "best [category] tools for [segment]" |
| Comparison | ~15% | "[you] vs [competitor]", "[competitor A] vs [competitor B]" (you're absent from these, which matters) |
| Alternatives | ~15% | "[competitor] alternatives", "cheaper than [competitor]" |
| Use case | ~20% | "[category] for [specific job / industry / stack]" |
| Pricing / cost | ~10% | "how much does [category] cost", "free [category] with [feature]" |
| Problem-based | ~15% | "how do I [problem your product solves]" |

- **Tag each prompt** with `topic` (fill this in at step 5), `intent`, and `value` (1–3, how close it is to a purchase).
- **Freeze the set.** Version the file (`prompts-v1.csv`), because changing prompts between runs breaks comparisons.

### 2. Run the identical set on every engine

- **Same conditions every time:** paste the prompt word for word. Use a fresh chat, no memory or custom instructions, logged out where possible, the same country, and web search on.
- **Record every answer** using the [results-log schema](#results-log-schema).

### 3. Score mention, recommendation and citation separately

For each answer, list **every** company mentioned and recommended and **every** cited URL, for you *and* your competitors. You need the competitor data for step 6.

### 4. Repeat the high-value prompts

- **How many runs:** run every `value = 3` prompt **≥ 3 times** on each engine, on different days if you can.
- **What counts:** a gap is real when it shows up in **≥ 2 of 3 runs, on ≥ 2 engines, across related prompts**. A single screenshot proves nothing.

---

## Phase B: Diagnose

### 5. Group prompts into buying topics

Cluster prompts by the *decision* behind them, not by wording. For example, "best auth API", "SSO provider for SaaS", "SAML authentication tools" and "SCIM providers" all go in **Enterprise auth**. Aim for 5–10 topics.

### 6. Compute the competitor gap per topic

For each topic and each brand, calculate:

- `presence rate` = answers mentioning the brand ÷ total answers (all runs × engines)
- `recommendation rate` = answers recommending the brand ÷ total answers
- `citation share` = your cited URLs ÷ all cited URLs
- **`gap` = top competitor's recommendation rate − your recommendation rate**
- **`priority` = gap × average topic value**

Work from the top of the priority list. A competitor at **18/25** against your **4/25** comes first. A prompt where you both appeared once is noise.

### 7. Map the sources behind competitor wins

Open **every** URL cited when a competitor won, and log it in the [source-map schema](#source-map-schema). After 20–30 prompts the same pages and domains keep coming back. That repeated set is your real target list.

---

## Phase C: Root-cause (per priority topic)

### 8. Check whether you already have a page that should win

If you do, find out why it loses before you write anything new:

- **Intent match:** does it answer *this* question, or a nearby one?
- **Freshness:** are the prices, features, screenshots and year still current?
- **Findability:** is the answer in the first screen, or buried under marketing copy?
- **Evidence:** does the competitor's page have proof, data, comparisons or limits that yours lacks?

A second page on the same intent usually gives you **two weak pages**. Fix the right one.

### 9. Check the technical layer

| Check | Pass condition |
|---|---|
| Indexable | Returns 200, no `noindex`, canonical points to itself on the canonical host |
| Google eligible | Indexed in Search Console (AI Overviews and AI Mode only use pages that can appear in normal Search) |
| Internal links | Linked from at least one hub or nav page, not orphaned |
| Crawler access | robots.txt **and the CDN/WAF** allow `OAI-SearchBot` (ChatGPT search), `ChatGPT-User`, `ClaudeBot`, `PerplexityBot`, `Bingbot` and `Googlebot` |
| Rendered content | The answer is in the server HTML, not only injected by client-side JS |

For how to run these checks, see [free-seo-geo](free-seo-geo/SKILL.md) steps 2–3 and the [crawler rules](seo-geo-llm-tools.md).

### 10. Look at the searches underneath the prompt

Engines often don't search for the sentence the user typed.

- **Google AI Mode** uses *query fan-out*: it runs several related searches behind one question.
- **Bing Webmaster Tools** reports the *grounding queries* its AI used to retrieve cited pages. Check that report for your site.
- **Use these sub-queries** to see what the engine is actually trying to find, such as "SCIM pricing" or "SAML setup time". Make sure a page of yours answers each one.

---

## Phase D: Act

### 11. Assign one root cause, then one action

| Root cause | Evidence | Action |
|---|---|---|
| **Technical** | Fails a step 9 check | Fix it. Don't write anything until it passes. |
| **Wrong page wins / intent mismatch** | Your page exists but answers a different question | Rewrite or restructure that page. |
| **Outdated** | Old prices, features or year | Update it and show a visible "updated" date. |
| **Coverage gap** | Sub-queries from step 10 go unanswered | Add sections to the existing page. |
| **Missing page** | No page covers this intent at all | Create **one** page. |
| **Third-party owned** | Step 7 sources are mostly external lists, reviews, videos and threads | Go to step 13. Your site alone won't fix this. |

### 12. Publish information no generic article has

Give the engine a reason to retrieve **you**:

- first-party data and benchmarks
- real pricing and plan limits
- specific feature limits and honest drawbacks
- comparison criteria, with the scoring method stated
- customer results with numbers
- screenshots, and differences by use case

Another 2,000-word summary of what's already online adds nothing. Put the direct answer first, name a source for every figure, and make sure the JSON-LD matches the visible text.

### 13. Earn your place in the third-party sources

For each recurring external source from step 7:

1. Note why competitors are in it (a review, a partnership, a data submission, an active community member).
2. Pursue **legitimate** inclusion where you fit: send data to list maintainers, correct outdated entries, and take part in relevant discussions as a disclosed representative.
3. **Don't** manufacture mentions, buy placements, or astroturf forums. That isn't GEO, and engines and communities discount it.

---

## Phase E: Prove

### 14. Rerun the identical audit after a recrawl

- **What stays the same:** the prompts (same version), the engines, the conditions and the run counts.
- **When to rerun:** usually 2–6 weeks after deploying. Confirm the pages were recrawled in Search Console or Bing first.

| Metric (per topic) | Baseline | Rerun | Δ |
|---|---|---|---|
| Your recommendation rate | | | |
| Your citation share | | | |
| Top competitor's recommendation rate | | | |
| Mentioned → recommended conversions | | | |
| Topics newly entered | | | |

Put more work into the **topics that moved**. Leave the topics that didn't move and diagnose them again. Don't start a fresh content sprint.

---

## Templates

### Results-log schema

`results-YYYY-MM-DD.csv`, one row per answer:

```csv
run_id,date,engine,model,prompt_id,prompt_version,topic,intent,value,brands_mentioned,brands_recommended,top_recommendation,cited_urls,you_mentioned,you_recommended,you_cited,notes
```

### Source-map schema

`sources.csv`, one row per cited URL in a competitor win:

```csv
url,domain,owner(you|competitor|third-party),page_type(listicle|review|comparison|docs|forum|video|news|vendor),competitors_named,you_named,claim_supported,times_seen,engines
```

### Topic scorecard

| Topic | Prompts | Answers | Your rec. rate | Top competitor (rate) | Gap | Avg value | Priority | Root cause | Action |
|---|---|---|---|---|---|---|---|---|---|

---

## Tooling (free)

| Job | Tool | Where in this repo |
|---|---|---|
| Run prompts and log answers | Manual, in each engine's own app (keeps the conditions honest) | — |
| Find who gets cited for a query | Exa (free monthly credit) | [catalog stage 2](../catalog/stages/02-research-competitor-analysis-scraping.md) |
| Indexing, coverage and queries | Google Search Console + `mcp-gsc` | [catalog stage 13](../catalog/stages/13-seo.md) |
| AI grounding queries and citations | Bing Webmaster Tools | [seo-geo-llm-tools](seo-geo-llm-tools.md) |
| Crawler, robots, schema and citability checks | `geo-seo-claude`, `claude-seo`, Chrome DevTools MCP | [free-seo-geo](free-seo-geo/SKILL.md) |
| Monthly tracking (optional) | Elmo / GetCito (needs your own model keys) | [free-seo-geo](free-seo-geo/SKILL.md) step 9 |

## Anti-patterns

- Optimizing one query at a time instead of whole topics.
- Counting a citation as a win.
- Acting on a single run or a single engine.
- Changing the prompt set between the baseline and the rerun.
- Writing new content before running the technical checks (step 9) and the existing-page check (step 8).
- Producing generic long-form content with no first-party information.
- Faking third-party mentions.
