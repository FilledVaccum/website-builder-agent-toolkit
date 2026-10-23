# Getting AI assistants to recommend your brand (AEO / GEO / LLMO playbook)

How to get **named and recommended inside AI answers** (ChatGPT, Google AI Overviews and AI Mode, Perplexity, Gemini, Claude, Copilot). This builds on top of classic SEO; it doesn't replace it.

- **Companion:** [ai-visibility-gap-audit.md](ai-visibility-gap-audit.md) is the measurement loop (prompts → gaps → root cause → rerun). This file covers the levers you pull once you know the gaps.
- **Site fixes:** [free-seo-geo/SKILL.md](free-seo-geo/SKILL.md).
- **Where the numbers come from:** almost all figures below are **Ahrefs studies (2025) as reported in a third-party guide**. They are one vendor's panel and mostly correlations, and they move every quarter. Treat them as direction, not law. I didn't re-verify them. See [Caveats](#caveats).

---

## TL;DR: run in this order

| # | Action | Why first | Section |
|---|---|---|---|
| 1 | Unblock AI bots (robots.txt, CDN/WAF, JS rendering) | Mentions are useless if the bots can't read you | [5](#5-let-the-bots-in) |
| 2 | Set up measurement: GA4 "AI traffic" channel + a "How did you hear about us?" field | You need a baseline | [6](#6-measure-knowing-it-undercounts) |
| 3 | Refresh your 5–10 most important pages, plus sleeper pages | Freshness is the cheapest lever | [3](#3-write-pages-a-model-can-lift-from) |
| 4 | Run the gap audit and list the listicles that name competitors but not you | This becomes your outreach list | [2](#2-audit-the-gap-before-writing) + [gap audit](ai-visibility-gap-audit.md) |
| 5 | Pick 10 mention targets and pitch about one a day | Third-party mentions are the strongest signal | [4](#4-get-named-where-the-model-already-looks) |
| 6 | Check mention frequency monthly; rerun the full audit quarterly | Answers drift fast | [6](#6-measure-knowing-it-undercounts) |

**The short version:** let them in → find the gap → write to be lifted → get named → measure.

---

## 0. The mental model

### Why bother

- **Small but high-converting:** in June 2025, AI search was **0.5%** of Ahrefs' traffic but **12.1%** of its sign-ups, about **23×** the conversion rate of Google organic.
- **Clicks are shifting:** when an AI Overview shows, the #1 organic result loses **~58%** of its clicks (Ahrefs, Dec 2025). Being named inside the answer is how you get that value back.

### You compete for a mention, not a position

An AI answer is a paragraph, not a ranked list. You're either in it or you're not.

| Source the model draws from | What it means for you |
|---|---|
| **Training data** (web, books, Reddit, YouTube transcripts; refreshed every few months) | New brands aren't in it yet. Consensus across the web builds up here over time. |
| **Live search / retrieval** | SEO pays off twice: if you rank, you're in the pile of pages the model reads. |

### Query fan-out

- **What happens:** the model rewrites the user's prompt into many short searches. Seer Interactive measured **9–11 per prompt** on average, up to 28. One ChatGPT deep-research run made 420.
- **Cover the whole topic:** "one page, one keyword" fails here, because the model checks every corner of the subject.
- **Fan-outs aren't a keyword list:** over 95% have zero search volume, and they change from run to run. Read them as a map of what the model thinks matters.

### Answers are probabilistic

Ask the same question five times and you might be named three times. So stop asking "what's my AI ranking?" and ask **"how often am I named?"** That's what the [gap audit](ai-visibility-gap-audit.md) measures.

### What tilts the odds

| Lever | Evidence (Ahrefs) |
|---|---|
| **Consensus:** many places say the same thing about you | Branded web mentions had the strongest correlation with AI Overview visibility (**0.664**), stronger than backlinks or DR |
| **Freshness** | AI-cited content is **25.7%** fresher than classic Google results; **76%** of ChatGPT's top-cited pages were updated in the last 30 days |
| **Authority** | Ranking in Google gives you a head start for retrieval |

---

## 1. Pick your engine before your tactic

"AI search" is several products, each with its own reading list. Of the top 50 cited domains across AI Overviews, ChatGPT and Perplexity, only **7** appear on all three.

| Engine | What it tends to cite | Implication |
|---|---|---|
| **Google AI Overviews** | Established authority sites, YouTube, Reddit; only **~10.7%** of mentions carry a link | Rank in Google, show up on YouTube and Reddit |
| **Google AI Mode** | **86%** of answers agree with AI Overviews, but only **13.7%** of citations overlap | Separate source pool; track it separately |
| **ChatGPT** | Publishers; median DR of top-cited pages is **90**; only **8–10%** of citations come from Google's top 10 | Editorial or press mentions beat your own pages |
| **Perplexity** | The most Google-like engine; **28.6%** of citations come from Google's top 10 | Strong rankings convert fastest here |

- **Most mentions are unlinked:** only about **28%** of AI mentions carry a link. An unlinked mention still works as word of mouth at scale, because people search your brand name afterwards.

**Where to start:**

| Your situation | Start with |
|---|---|
| Default | Google (AI Overviews / AI Mode) + ChatGPT; they carry most of the volume |
| Already ranking well | Perplexity and AI Overviews; quickest wins |
| Weak rankings, strong press | ChatGPT |

---

## 2. Audit the gap before writing

Run the full [AI visibility gap audit](ai-visibility-gap-audit.md). This section adds three inputs to it.

### 2.1 List every entity the model could name

- **Brand and products:** the brand and every product name.
- **Coined terms:** named features and any metric or framework you invented.
- **People:** founders and the public faces (YouTube, podcasts).
- **Target descriptors:** for each entity, write the words you *want* next to it, such as "cheap", "for agencies" or "AI-powered". This is your benchmark for spotting narrative gaps.

### 2.2 Sort the gaps into six buckets

| Bucket | Symptom |
|---|---|
| **Visibility** | Competitors are named more often than you |
| **Narrative** | You're named but described wrongly (e.g. "budget" when you're premium) |
| **Topic** | A subject you should own where you never come up |
| **Format** | Competitors' videos, comparisons and reviews get cited; you only have blog posts |
| **Web mentions** | Listicles and review sites name competitors, not you |
| **Demand** | Searches in your space where your brand never appears |

One or two buckets usually hold most of the problem. Put the work there.

### 2.3 Filter keywords for AI

AI Overviews show on about **21%** of keywords and **58%** of question queries. **99.9%** of the keywords that trigger them are informational.

For each keyword that already passes your business-value, intent and difficulty checks:

1. Google it and read the AI answer as a customer would.
2. **If the answer fully satisfies the question,** the click is gone. Target a **mention** on the pages the model cites.
3. **If it doesn't,** target the **click** with classic SEO. Tool queries are the safest bet (calculator, checker, generator, template, planner), because AI can't do the job for the user.

**Building the mention target list:** listicles make up **43.8%** of the pages cited by AI Overviews and ChatGPT.

- Collect the top-10 results for "best [category]", "[competitor] alternative" and "[competitor] vs [competitor]".
- For each page, log its type (listicle, comparison or review), which brands it names, and whether you're one of them. Use the gap audit's `sources.csv` columns.
- **Any page that names 3 competitors but not you goes on the outreach list** for section 4.
- **Free way to do it:** Search Console + `mcp-gsc`, plus Exa or a manual SERP check. See [Tooling](#tooling-free).

---

## 3. Write pages a model can lift from

Length doesn't get you cited. Across 174k pages cited in AI Overviews, the correlation between word count and citation was **0.04**, and over half the cited pages were under 1,000 words. Freshness and structure matter more.

### Four writing rules

| Rule | How to apply it | Self-test |
|---|---|---|
| **Answer first** | Open every section with the answer, then give context. Models (and skimmers) weigh the start and end of a passage most. | Does the first sentence under each H2 answer it on its own? |
| **Each section stands alone** | Models split pages into chunks. | Read any H2 out of context. If it needs the paragraph above, rewrite it. |
| **Name things** | Use explicit entities and relationships: "*[Product] [feature]* does *[specific job]*", not "this tool helps with SEO". | Are there no unclear "it" or "this tool" references? |
| **One idea per sentence** | If a sentence takes two reads, split it. | |

Add what generic articles can't offer: real prices, limits, benchmarks, dates and first-party data. See [gap audit step 12](ai-visibility-gap-audit.md#12-publish-information-no-generic-article-has).

### Brand your original ideas

Models flatten originality. If you coin a framework and nobody else uses your name for it, the model absorbs the idea and drops your name.

- **Brand the name:** call it "**The [YourBrand] content scoring matrix**", not "a content scoring matrix".
- **Repeat it** the same way everywhere you publish.

### Fastest win: sleeper pages

A sleeper page used to rank, still has backlinks, and has been losing clicks for months. The authority is still there; the content went stale.

1. In Search Console, compare clicks per page for the **last 3 months vs the same 3 months last year**.
2. List the **10 pages that lost the most clicks**, along with the queries they lost.
3. Check each page's referring domains (Ahrefs Webmaster Tools is free for verified sites; GSC's Links report also works).

| State | Action |
|---|---|
| Has links + declining | **Refresh it properly:** new numbers, examples and sections, not just a new date. |
| No links + declining | A refresh won't save it. Diagnose it with the gap audit (intent, coverage or authority). |

---

## 4. Get named where the model already looks

Your own page saying you're the best is the weakest signal there is. What the model cites is **third parties naming you**.

> **Example from the source guide:** when asked for the best SEO consultants in France, ChatGPT named the author's co-founder. It cited a ranking published by a third party, not his own site.

### Three tiers of mention targets

| Tier | Where | How |
|---|---|---|
| **1. Editorial** (hardest; most cited) | Listicles, review sites, comparison posts, YouTube reviews | Start with the outreach list from 2.3. Add uncited pages that have strong links and cover your topic, since they're likely to be cited next. Pitch about one a day. |
| **2. Communities** | Reddit, Quora, niche forums | Find threads asking the question your product answers and answer them properly, disclosing that you're affiliated. Drive-by brand drops get downvoted and teach the model nothing useful. |
| **3. Your own channels** | YouTube, podcast, LinkedIn | All indexed and readable. Each one gives the model another example of your name next to your topic. |

Earn your inclusion. Never fake or buy mentions. See [gap audit step 13](ai-visibility-gap-audit.md#13-earn-your-place-in-the-third-party-sources).

### YouTube checklist

YouTube is the **most cited domain in AI Overviews**, and YouTube mentions had the strongest correlation with ChatGPT visibility (**0.737**). Aim for **search hits** (found every month), not viral hits (they fade).

- [ ] Pick a topic where a video already ranks in Google's top 3.
- [ ] Title = the keyword. Save the creativity for the thumbnail.
- [ ] Description = a real summary, with the keyword in the first two lines.
- [ ] Timestamps. They become chapters, and chapters show up in Google on their own.
- [ ] Say the keyword out loud. Google processes the audio.
- [ ] Match the format that ranks. If tutorials rank, make a tutorial.

---

## 5. Let the bots in

Many sites block AI without knowing it. Ahrefs found **5.9%** of 140M sites block GPTBot.

### Check 1: robots.txt + CDN

- **robots.txt:** open `https://yourdomain.com/robots.txt` and look for `Disallow` under any of these:

  ```
  User-agent: GPTBot          # OpenAI training
  User-agent: OAI-SearchBot   # ChatGPT search (retrieval: the one that matters most for citations)
  User-agent: ChatGPT-User    # live fetch while a user is chatting
  User-agent: ClaudeBot
  User-agent: PerplexityBot
  User-agent: Google-Extended # Gemini training control (doesn't affect Google Search)
  ```

- **Cloudflare:** check its AI bot / "AI Scrapers and Crawlers" settings and its managed robots.txt. These blocks can be switched on by default.
- **Policy choice:** blocking *training* bots (GPTBot, Google-Extended) is a legitimate decision. Blocking *retrieval* bots (OAI-SearchBot, ChatGPT-User, PerplexityBot) removes you from live answers.
- **Test the response:**

  ```bash
  for ua in GPTBot OAI-SearchBot ClaudeBot PerplexityBot; do
    printf "%-15s " "$ua"; curl -A "$ua" -s -o /dev/null -w "%{http_code}\n" https://yourdomain.com/
  done
  ```

  Anything other than `200` means a closed door. CDNs verify real bots by IP, so a spoofed user-agent from your own machine can get a different result from the real bot. Confirm in your CDN's firewall or bot logs.

### Check 2: JavaScript rendering

ChatGPT's crawler doesn't render JavaScript (Gemini and Copilot do). Turn JS off and load your key pages. If the content disappears, ChatGPT sees an empty shell. **The fix is server-side rendering or static generation.**

### Check 3: URLs the AI makes up

- **The problem:** AI assistants send visitors to 404 pages **2.87×** more often than Google does (about 1% of ChatGPT's clicked URLs).
- **The fix:** filter analytics for AI referrals that land on 404s. Redirect (301) any made-up URL that keeps getting visits to the closest real page.

### About llms.txt

No major model provider officially says it reads `llms.txt`. Publishing one (plus markdown copies of key pages) costs nothing, but rank it **below** the three checks above. See the [free-seo-geo](free-seo-geo/SKILL.md) rules.

### Fill every factual gap yourself

In an Ahrefs experiment, a made-up brand was seeded with three contradictory stories (a blog, Reddit, Medium). **Gemini and Perplexity repeated the fiction in 37–39%** of answers. ChatGPT did so under 7% of the time and cited the official FAQ in 84% of answers.

**The lesson:** when the model has to choose between your vague truth and someone else's specific fiction, it picks the specific fiction.

- Publish an FAQ or "facts" page with **real numbers, dates, founders, prices and locations**, and mark it up with `Organization` / `FAQPage` JSON-LD that matches the visible text.
- If you find a wrong claim, publish the correction on your own site first, then ask the source to fix it.

---

## 6. Measure, knowing it undercounts

No single source is complete. Use all three.

| Source | Setup | Blind spots |
|---|---|---|
| **AI referral traffic** | GA4 → Admin → Channel groups → new channel **"AI traffic"**, with source matching the regex below and placed **above** Referral | ChatGPT in-content links on paid accounts strip the referrer. Perplexity desktop, Copilot on Windows and Grok send none. Those visits land in Direct. |
| **Retrieval-bot hits** | Filter server or CDN logs for `ChatGPT-User`, `OAI-SearchBot`, `PerplexityBot` and `Claude-User` | A page fetched again and again is probably being cited |
| **Self-reported attribution** | Add "How did you hear about us?" to sign-up, with ChatGPT, Perplexity, Google AI and Other as options | Depends on people remembering (Ahrefs credits about 3% of conversions to AI this way) |

```regex
chatgpt|openai|perplexity|gemini\.google|copilot\.microsoft|claude\.ai|deepseek
```

**If you do only one thing here,** add the "How did you hear about us?" question.

**Cadence:** check mention frequency monthly with the gap audit's top prompts. Rerun the full [gap audit](ai-visibility-gap-audit.md) every quarter.

---

## Tooling (free)

| Job | Tool | Where in this repo |
|---|---|---|
| Search Console data (sleepers, queries, coverage) | Google Search Console + `mcp-gsc` | [catalog stage 13](../catalog/stages/13-seo.md) |
| Who gets cited / listicle discovery | Exa (free credit), manual SERP check | [catalog stage 2](../catalog/stages/02-research-competitor-analysis-scraping.md) |
| Backlinks for sleeper pages | Ahrefs Webmaster Tools (free for verified sites), GSC Links report | — |
| Crawler, schema, citability and `llms.txt` checks | `geo-seo-claude`, `claude-seo`, Chrome DevTools MCP | [free-seo-geo](free-seo-geo/SKILL.md) |
| AI grounding queries (Bing) | Bing Webmaster Tools | [seo-geo-llm-tools](seo-geo-llm-tools.md) |
| AI traffic channel | GA4 (free) | [catalog stage 15](../catalog/stages/15-analytics-monitoring-error-tracking.md) |

Paid trackers (e.g. the ChatSEO.app promoted in the source guide, or Ahrefs Brand Radar) aren't required. Everything above can be done for free.

---

## Caveats

- **One source:** almost every figure is Ahrefs data, and Ahrefs also sells the tool that measures it. The studies are large but come from one company's panel.
- **Correlation, not causation:** brands mentioned everywhere also tend to be good brands, so mentions may be a symptom as much as a cause.
- **The numbers decay fast:**
  - The share of AI Overview citations taken from Google's top 10 fell from **76% to ~38%** in later data.
  - **Over 45%** of AI Overview citations change at each refresh (about every 2 days).
  - Recheck any figure older than a quarter.
- **Clean robots.txt ≠ cited:** passing the bot checks proves bots can read you, not that they cite you.
- **What does generalise:** a third party naming you beats you naming yourself. That was true before AI too. Which pages each engine favours next quarter is not stable.
