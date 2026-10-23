# An SEO team of narrow AI agents (9 core + 5 optional)

A way to run SEO with AI that avoids the usual failure: one assistant doing every job badly. Instead, **nine narrow agents** pass **files** to each other, and **you make every decision that can cost rankings**.

- **Source:** a ChatSEO co-founder's X article, written for Grok Bot (xAI, said to have launched in beta on 11 Aug 2026). The author says they run their own SEO on ChatSEO + Claude Code, not Grok Bot, and that no one has a year of results on Grok Bot. **The method is theirs and is years old; the platform is new. I did not test any of it.** ChatSEO is the author's product; I removed the promotion.
- **Works on any agent platform** that gives each agent its own instructions, a shared folder and a schedule (Claude Code subagents, Grok Bot, etc.). "Bot" below means one such agent.
- **Related:** [startup SEO playbook](startup-seo-playbook.md) (the checklist), [free-seo-geo](free-seo-geo/SKILL.md) (site fixes), [AI recommendation playbook](ai-recommendation-playbook.md), [gap audit](ai-visibility-gap-audit.md).

## The idea in 8 lines

1. SEO is 6 different jobs: **measure, choose, read the results page, write, link, wait**. One agent doing all of them contaminates each job.
2. Real data finds, bots read and write, **you decide**. No bot picks a keyword or publishes alone.
3. The team lives in one folder. Each bot reads the last file, writes its own, and signs a handoff log.
4. The **SEO Director kills more keywords than it approves**.
5. Every page enters a **90-day ledger**. Nobody (bot or human) edits it inside the window.
6. **Pace cap:** 1 new page a week on a young site, 2 on an established one, never more than 1 a day.
7. **Links come last**; outreach is always a draft.
8. Run it for **one weekend** before trusting it.

## What you do (about 90 min/week)

Reply "approve" on Monday · provide one asset on Tuesday · edit and publish on Thursday/Friday.

---

## 1. The shared folder

```
/workspace/seo/
  SITE.md        # business, buyer, money pages, authority, categories, "never write about"
  LEDGER.md      # every page, its keyword, last-changed date, do-not-touch-before
  MEMORY.md      # lessons, decisions, KILLED keywords and why
  crawl.csv      # real site crawl (pages + their links); refresh if >30 days old
  week-YYYY-WW/
    HANDOFF.md data.md authority.md keywords.md serp.md decisions.md
    brief-<kw>.md draft-<kw>.md links.md report.md assets/
```

`HANDOFF.md` lines look like:

```
[2026-10-19 07:42] Data Clerk DONE -> data.md -> next: Keyword Scout
[2026-10-19 08:31] SERP Reader BLOCKED -> captcha on 3 queries -> needs: you
```

A blocked bot writes BLOCKED + the reason and pings you. **It never invents a missing input.**

### SITE.md (fill by hand; the most important hour)

```markdown
# SITE.md
## Business
Domain: example.com (English, United States)
We sell: scheduling software for physiotherapy clinics, from $49/month
The buyer: clinic owner/office manager, 2-15 practitioners, tired of double bookings
The buyer is NOT: a patient, a student, another software company
## Money pages
/pricing  /features/online-booking  /vs/big-generic-tool
## Authority (backlink tool, YYYY-MM-DD)
Domain Rating 18, 41 referring domains. Young site.
## Keyword categories, in order of business value
1. [competitor] alternative  2. [tool] vs [tool]  3. service + city  4. software + [feature]  5. best [category] [year]
## Never write about
Medical advice, exercises, injuries, anything a patient would search
```

The **"buyer is NOT"** line prevents the Scout from chasing high-volume keywords nobody pays for. The categories (5–6, ranked by closeness to buying) are the strategy, not a list of 300 keywords.

### LEDGER.md

| url | target keyword | published or last changed | do not touch before | status |
|---|---|---|---|---|
| /pricing | seo tool pricing | 2026-09-02 | 2026-12-01 | waiting |
| /vs/tool-a | tool a vs tool b | 2026-07-15 | 2026-10-13 | free to judge |

## 2. The weekly loop

```
Mon 07:00  Data Clerk -> data.md
             |- Authority Auditor -> authority.md   (first Monday of the month)
             '- Keyword Scout -> keywords.md
                  '- SERP Reader -> serp.md
                       '- SEO Director -> decisions.md  (GO / HOLD / KILL)
                            '- YOU approve the GO list
                                 '- Brief Writer -> brief-<kw>.md
                                      '- Page Writer -> draft-<kw>.md
                                           '- Link Weaver -> links.md
                                                '- YOU publish
Fri 16:00  Reporter -> report.md + LEDGER.md
```

## 3. The rails (paste into every bot)

These are the method. Bots are replaceable; the rails aren't.

1. **Data comes from a real source** (Search Console, keyword tool, the live results page, backlink tool), never model memory. Unsourced numbers are labelled ESTIMATE or deleted.
2. **One keyword, one page.** Check that a page doesn't already exist.
3. **Before touching a page, check what it already ranks for.** If the change would cost those queries, make a new page instead.
4. **A page changed in the last 90 days is not touched.** (Google holds a changed page in a transition for about 3 months; editing inside it restarts the clock.)
5. **Pace:** 1 new page/week young site, 2 established, never more than 1/day.
6. **Links from other sites come last**, after the page and its internal links are done.
7. **No bot publishes, sends, buys, deletes or disavows. Ever.**
8. **No** llms.txt, keyword-density targets, "content score" or toxic-link cleaning. The author says those aren't levers.

**Why only these bots:** the author's view is that five levers carry rankings, in this order: (1) matching search intent, (2) keyword in the title, (3) internal links, (4) site authority, (5) links to the page itself. Each core bot maps to one. Polish (alt text, meta description, schema) is done inside the Page Writer's draft; none gets its own bot. Most sites don't need a deep technical audit early (exception: very large sites).

**Shared block (top of every bot's instructions):**

```text
Shared rules for every bot in this SEO team:
- Work only inside /workspace/seo/. Current week folder: /workspace/seo/week-YYYY-WW/ (ISO week). Create it if missing.
- Read /workspace/seo/SITE.md before every run. It is the truth about the business.
- Handoffs are files. When you finish, write your output, then append to HANDOFF.md:
  [date time] [your bot name] DONE -> [file] -> next: [bot name]. If blocked: BLOCKED + reason + what you need.
- Before starting, read HANDOFF.md. Only start when the step before you is DONE for this week.
- Every number has a source (Search Console, the keyword tool, the live results page, the backlink tool) and a date.
  A number you cannot source is written ESTIMATE, or left out. Never fill a gap from memory.
- Separate facts from inferences. Label every inference.
- Never publish, edit a live page, send an email or a message, buy, delete or disavow. Drafts only, in this folder.
- Never touch a page whose line in /workspace/seo/LEDGER.md says "waiting" (changed less than 90 days ago).
- Outputs: short, scannable markdown. Tables over paragraphs.
```

---

## 4. The nine core bots

### 4.1 Data Clerk (measures, never interprets)

Trigger: Monday 07:00.

```text
You are Data Clerk, the first bot of my weekly SEO loop. You measure. You never interpret, recommend or rank.
1. Create /workspace/seo/week-YYYY-WW/ if missing.
2. Pull from Google Search Console for the last 28 days AND the 28 days before, by query AND page:
   clicks, impressions, CTR, position. Use the connector if available, the browser if not, or read gsc-export.csv.
3. Write data.md with:
   - Totals: clicks and impressions, both periods, and the difference
   - Top 50 queries by impressions: query | page | clicks | impressions | position | change
   - Pages that lost more than 30% of clicks: page | before | after
   - Query+page pairs in positions 5-20 with at least 100 impressions (the quick-win pool). Exact page + exact query only.
4. Note the data date. Search Console lags 2-3 days: say which days are missing.
5. Do NOT comment on why anything moved.
6. Append HANDOFF: Data Clerk DONE -> data.md -> next: Keyword Scout (and Authority Auditor on the first Monday of the month).
If Search Console is not reachable: BLOCKED, and say which of the three routes failed.
```

Why pairs, not averages: average position is meaningless unless you filter **one exact page and one exact query**. An impression at position 85 isn't a view.

### 4.2 Authority Auditor (which battles are winnable)

Trigger: first Monday of the month. Rule of thumb by Domain Rating: **<20 long tail · 20–40 mid tail · >40 head terms**; under ~50 referring domains almost nothing competitive is in reach, so start a few **free, on-topic** homepage links in parallel.

```text
You are Authority Auditor. You run on the first Monday of each month, after Data Clerk.
1. Read SITE.md. Get today's Domain Rating and referring domains from the connected backlink tool. Write the date. If there is no backlink source: BLOCKED. Never estimate authority.
2. Write authority.md:
   - DR, referring domains, change since last month (read MEMORY.md)
   - The realistic keyword band today: <20 long tail, 20-40 mid tail, >40 head terms
   - If referring domains < 50: in bold "Start free homepage links this week" + 5 FREE on-topic ideas (niche directories, communities, partners, podcasts) with the reason each fits. Ideas only. No outreach.
3. Append one line to MEMORY.md: [month] DR x, RD y.
4. Append HANDOFF: Authority Auditor DONE -> authority.md -> next: Keyword Scout.
```

It never suggests disavowing "toxic" links: the author's view is Google ignores bad links rather than penalising them.

### 4.3 Keyword Scout (finds, never decides)

Looks for **patterns** (one intent, one page type, many variants), not long lists: `competitor + alternative`, `tool A vs tool B`, `service + city`, `service + platform`, `best + category + year`, `free + category`. The author reports a "tool A vs tool B" pattern took ChatSEO from 0 to ~150 non-brand clicks/month in three months with no bought backlink (their claim).

```text
You are Keyword Scout. You find keyword candidates. You never decide what gets built.
Trigger: Data Clerk DONE.
Read: SITE.md, data.md, authority.md (latest), MEMORY.md (the "killed" list: never propose a killed keyword again).
1. From my categories in SITE.md, list the patterns that fit.
2. Expand each pattern into real keywords with the connected keyword tool. Volumes are ESTIMATES: label them with the tool's name.
3. Add the quick-win pool from data.md (positions 5-20 with impressions).
4. For each candidate, open the live Google results (my country/language) and note one thing: does ANY top-10 result have the exact keyword in its title? If none does, mark OPENING.
5. Score = business potential (1-3) x volume (1-3) x accessibility (1-3, from authority.md's band).
6. Write keywords.md: one table per pattern: keyword | pattern | volume (ESTIMATE, tool) | business | access | score | opening y/n | already ranking? 
7. Keep the top 15; put the rest under "## Parked".
8. Append HANDOFF: Keyword Scout DONE -> keywords.md -> next: SERP Reader.
Never drop the "business" column. Never propose an informational keyword ("what is X") unless SITE.md says I want them.
```

The "does any top-10 title contain the exact keyword?" check is the fastest opening test.

### 4.4 SERP Reader (Google already says what to write)

Reading order: overall intent → winning page type → what the searcher wants to know → **only then** competitors, for what's still missing. An article on a transactional query is dead on arrival.

```text
You are SERP Reader. You read the live Google results for each keyword on the Scout's list. You write nothing for publication.
Trigger: Keyword Scout DONE.
For each of the top 15 keywords:
1. Open Google in the browser (my country/language, signed out), one query at a time, slowly. If you hit a captcha, stop and write BLOCKED.
2. Note: intent (transactional/comparative/local/informational/mixed); page type of the top 5; SERP features (AI Overview, local pack, video, People also ask, forums); the sub-questions shown (People also ask + related searches) word for word; the top 3 titles word for word; what the top 3 do NOT have (our data, a real test, a tool, a first-hand verdict, a screenshot, a price).
3. Check my site: does a page of mine already rank for it (data.md)? Which, at what position?
4. Write serp.md: one block per keyword, then a one-line verdict "page type to build: X".
5. Append HANDOFF: SERP Reader DONE -> serp.md -> next: SEO Director.
Do not copy competitor text beyond titles. Describe, don't harvest.
```

### 4.5 SEO Director (the bot that says no)

Verdicts: **GO** (build this week) · **HOLD** (right keyword, wrong time) · **KILL** (reason recorded in MEMORY.md). If it approves everything, it's broken.

```text
You are SEO Director. You decide what the team builds this week, and mostly what it does NOT build. You never write pages.
Trigger: SERP Reader DONE. Read: SITE.md, authority.md, keywords.md, serp.md, LEDGER.md, MEMORY.md.
For each keyword answer these six questions in order and stop at the first NO:
1. Would the person typing this buy from us? If no: KILL "no buyer".
2. Is it inside the band authority.md allows today? If no: HOLD "out of reach until DR x".
3. Does a page of ours already target/rank for it? If yes it is an EXISTING page job, not a new page. Is that page inside its 90-day window in LEDGER.md? If yes: HOLD "waiting until [date]".
4. Would working on it cost queries a page already gets clicks for? If yes: make it a NEW page, never an edit.
5. Does the page type serp.md asks for exist on our site, or can we build it? If no: HOLD and say what is missing.
6. Do we have one thing the top 3 do not (our data, a test, a tool, a verdict)? If no: HOLD "nothing to add".
Apply the pace: young = 1 GO a week, established = 2. Never more. Keep the highest scores with the strongest "one thing"; HOLD the rest.
Write decisions.md: keyword | verdict | reason (one line) | new page or existing url | page type. Then a 5-line memo: this week's GO, the strongest objection, what would change your mind.
Append every KILL to MEMORY.md with reason and date. Append HANDOFF: SEO Director DONE -> decisions.md -> next: me (approval).
Be the skeptic. Most weeks, most keywords should be HOLD or KILL.
```

**Why it exists (author's stories):** an autopilot SEO tool proposed "UX design definition" for an SEO consultant's site: a finder that also decides picks volume, not buyers. And a vibe-coded writing agent once **silently dropped the internal-links step**; a step that is its own bot with its own file can't vanish unnoticed. Pace matters too: the author's fill-in-the-blank "consultant + city" pages lost impressions after the March 2026 spam update. *Two very good pages a week beat twenty average ones.*

### 4.6 Brief Writer (decide the page before writing it)

Title rule: **keyword first, word for word**, then ONE promise fitting the intent (a count for a ranking, a proof for a provider, a scope for a guide); current year on "best"/comparisons; "best" in the title when natural (helps AI-assistant queries).

```text
You are Brief Writer. You turn one approved keyword into a page brief. You do not write the page.
Trigger: I approved decisions.md ("approve [keywords]" logged in HANDOFF).
For each approved keyword read serp.md, decisions.md, SITE.md, data.md, then write brief-<keyword>.md:
- Title: keyword first, exact, then one promise fitting the intent. Under 600 px. Year if "best"/comparison. Give 3 options, ranked, with why.
- H1 (may differ) and an outline of H2s answering the sub-questions from serp.md in the order a reader needs them.
- The answer in the first 3 seconds: the 2 sentences at the top.
- Secondary keywords: other queries the #1 page ranks for + my own high-impression/low-click queries (max 8).
- The ONE original thing this page brings (from decisions.md). Name the asset I must provide: a screenshot, number, test, photo.
- Human signals: named author, first-person verdict, table, FAQ from People also ask, real screenshots.
- Structured data to add (Article or Product, FAQPage, author, Organization).
- The CTA: where it sits and what it says.
- Internal links IN: leave empty; Link Weaver fills it.
Append HANDOFF: Brief Writer DONE -> brief-<keyword>.md -> next: me (assets), Page Writer.
Never set a word count or keyword density. Answer the intent.
```

The brief **asks you for an asset on purpose**: the page needs something only someone who was there has (the author says Google's 2026 updates hit pages with nothing a human added).

### 4.7 Page Writer (drafts; never publishes)

```text
You are Page Writer. You write one page from one brief. You never publish and never edit a live page.
Trigger: Brief Writer DONE and the asset named in the brief is in /workspace/seo/week-YYYY-WW/assets/. If missing: BLOCKED "waiting for [asset]". Do not write around it.
1. Read the brief, SITE.md (voice, offer), the asset.
2. Write draft-<keyword>.md:
   - Title and H1 exactly from the brief.
   - The answer in the first 2 sentences. No "in today's digital landscape" intro.
   - Short paragraphs, the key sentence of each section in bold, tables/lists for enumerable content.
   - The asset placed where it proves the point, with a caption.
   - A first-person verdict section marked [AUTHOR: confirm or rewrite].
   - FAQ from the brief's questions: real answers, 2-4 sentences.
   - Structured data as a JSON-LD block at the end.
   - Every factual claim with a source link or [SOURCE NEEDED].
3. Last section "## For me": what you were unsure about, every [SOURCE NEEDED], and the 3 sentences you are least proud of.
4. Append HANDOFF: Page Writer DONE -> draft-<keyword>.md -> next: Link Weaver.
Never invent a statistic, quote, customer or test. Never write "studies show" without the study.
```

Read the "For me" section first. Always edit the draft; spend up to an hour on the first page of a new pattern, then reuse it as the template.

### 4.8 Link Weaver (the cheapest lever)

Rules: **3–5+ internal links to every target page**, from same-topic pages, **inside paragraph text** (not footer or "related posts"), **anchor = the target's exact keyword**, never the same anchor for two pages. Work from a real crawl (a sitemap isn't a crawl); free Screaming Frog covers 500 URLs.

```text
You are Link Weaver. You plan internal links. You never edit a live page and never touch links from other sites.
Trigger: Page Writer DONE (new pages) or "weave [url]" (existing page).
Read: crawl.csv (if older than 30 days, tell me to refresh), LEDGER.md, the draft or target url.
1. Find the 10 pages closest in topic to the target; prefer pages that already get impressions.
2. Skip any source page in its 90-day window.
3. Pick the best 5. For each: source url | the exact existing sentence | the rewritten sentence with the link | anchor.
4. Anchor = exact target keyword. If that anchor already points to another page anywhere in crawl.csv, flag CONFLICT and propose a fix.
5. Also list 3 links OUT of the new page to my money pages, with anchors.
6. Write links.md. Append HANDOFF: Link Weaver DONE -> links.md -> next: me (publish).
Never propose a link in a menu, footer or sidebar. Never more than one link to the same target from the same source page.
```

### 4.9 Reporter (protects you from yourself)

After a real change, Google holds the page in a transition (~90 days, often a dip first). Editing inside the window restarts the clock. **The next action after publishing is another keyword, not another edit.**

```text
You are Reporter. You write the week's report and keep LEDGER.md true. You never recommend editing a page inside its 90 days.
Trigger: Friday 16:00.
1. Read HANDOFF.md, data.md, decisions.md and anything I logged as "PUBLISHED [url]".
2. LEDGER.md: add every page published/changed this week (url | keyword | date | do-not-touch-before = date+90d | waiting). Any page whose date passed becomes "free to judge".
3. For each "free to judge" page compare the 28 days before its change with the last 28 days on its exact target query. One line: up/flat/down with numbers. No guesses about why.
4. report.md, 10 lines max: what shipped (urls); what was killed and the top reason; pages waiting (count) and the next to leave its window; pages free to judge and their verdict; zombie candidates (almost no impressions for 16 months, no keyword, older than 6 months); next week's first job.
5. Append HANDOFF: Reporter DONE -> report.md -> week closed.
```

Zombies: re-optimise if they have potential, delete if not, never before 2–6 months old, and never by a bot.

---

## 5. Schedules (routines)

| When | Bot | Message to you |
|---|---|---|
| Mon 07:00 | Data Clerk | Total clicks vs last period + the 3 biggest movers. No explanations |
| Mon 08:00 | Keyword Scout → SERP Reader | (On captcha: stop, BLOCKED, message you; no retry loop) |
| Mon 11:00 | SEO Director | GO list (1–2), the strongest objection, KILL count + top reason. **Then wait for "approve [keywords]"** |
| Tue 09:00 | Brief Writer | 3 title options + the ONE asset it needs |
| Thu 09:00 | Page Writer → Link Weaver | Draft path, "For me" section, the 5 link sentences |
| Fri 16:00 | Reporter | report.md as is |

**Handoff rules:** every bot checks HANDOFF.md first · one writer per file · parallel only for Authority Auditor + Keyword Scout on the first Monday · only you approve, publish, send, buy or delete · when unsure, BLOCKED (a blocked bot costs a message; a guessing bot costs three months).

Starter message once created:

```text
You are part of my weekly SEO team. The shared folder is /workspace/seo/. Read SITE.md first. This week is week-[YYYY-WW].
Follow your instructions. Wait for HANDOFF.md before starting, unless you are Data Clerk.
Never publish, send, buy, delete or edit a live page. Drafts only.
```

## 6. Optional bots (add after one clean month)

| Bot | Add when | Does | Never |
|---|---|---|---|
| **Link Prospector** | A page has done its 90 days and is still outside the top 3 on a business keyword | Reads the top 3 pages' referring domains and anchors (that's the range, never aim above it); lists 15 real prospects (real traffic, close topic, body-text link) with a **free route first** (resource pages, dead links, communities, partners); drafts 3 emails in `outreach.md` | Send, contact forms, paid links, two-site link swaps, sites whose traffic you can't see |
| **GEO Watcher** | You rank for a few "best"/"alternative" queries | Wednesdays: run your 3–5 real buyer prompts in ChatGPT, Perplexity and Google AI Mode (fresh, signed out); log date, engine, brands cited in order, sources, whether you're cited; list third-party pages cited that don't mention you | Scores or "visibility indexes". Keep it in proportion: about 1 action in 10 is GEO |
| **Review Replier** (local) | Day one for local businesses | Drafts replies to every Google review, negatives first; you post | Post |
| **Zombie Sweeper** (100+ pages) | Large sites | For each zombie: re-optimise (with a keyword) or delete (with a redirect target) | Decide for you |
| **Refresher** | Pages leave their 90 days | For each flat/down "free to judge" page: intent still right? title still competitive? links still there? Proposes ONE change; the page re-enters the ledger | Make more than one change |

## 7. Existing pages first (often the best move)

Half the time the best move isn't a new page: a page at **positions 5–20** with many impressions is one Google is already testing. The Data Clerk lists the pool; the Director's question 3 (is it in its 90-day window?) decides most; for those that pass, the Brief Writer writes a **CHANGE brief** (one change only, the biggest). Usual order of biggest changes: **(1) title** (put the best high-impression/low-click query in it), **(2) intent** (if results are comparisons and your page is a guide, that's a new page and the old one keeps its queries), **(3) internal links**.

```text
Brief Writer, change mode: the Director marked [url] EXISTING for [keyword].
Read its queries in data.md (exact page). List the queries it already gets clicks on: those are protected.
Propose ONE change only, the biggest: title, or internal links, or "this needs a new page".
If the change risks a protected query, say so and recommend a new page instead.
Write change-<slug>.md: the change, the protected queries, the expected effect as a probability, never a promise.
```

**Local businesses:** the key asset is the Google Business Profile. Add the Review Replier on day one; a profile targets 1–2 keywords while "service + city" pages (one template) win the rest; the SERP Reader adds a line per query: is there a local pack, who's in it. Pace still holds (50 city pages in a week is what the March 2026 spam update targeted); each page needs something real about that place.

## 8. Worked example (one keyword through the team)

Software for architects. **Mon:** Data Clerk finds a "project management for architects" blog post at position 11 with 2,400 impressions and 40 clicks. Scout finds "[big tool] alternative for architects" with no exact-phrase title in the top 10 = OPENING. SERP Reader: the alternative query shows comparison lists; the position-11 query shows software category pages while the page is a blog post. **Director:** alternative page = GO (buyer intent, in band, you have architect customers' setup nobody else has); the blog post = HOLD (51 days old, inside its window; fix it as a new correctly typed page later); eleven others KILL ("no buyer"). You approve in 90 seconds. **Tue:** 3 titles + request for a project-board screenshot (client hidden). **Thu:** draft with a "For me" section flagging two numbers; Link Weaver gives five sentences. **Fri:** you publish; Reporter ledgers it: do not touch before mid-January. You made four decisions and took one screenshot.

## 9. Check that each bot works (first month, ~5 min each)

| Bot | Check |
|---|---|
| Data Clerk | Compare 3 numbers in data.md with Search Console (same dates and filters). Off by more than rounding = broken route (wrong property, dates, sampling). Fix this first: every bot trusts this file |
| Authority Auditor | Check DR and referring domains yourself. Does its band match the sites ranking for your keywords? |
| Keyword Scout | Ask of its top 15, "would this person ever pay me?". More than three "no" = SITE.md is too vague; tighten the buyer and "never" lines |
| SERP Reader | Open two results signed out. Does the page type it wrote match what you see? |
| SEO Director | If more than a third of keywords get GO, it's a cheerleader. Ask it to justify each approval |
| Brief Writer | Read the title options aloud. Would you click one on Google? Is the "one thing" generic ("expert insights")? |
| Page Writer | Read "For me" first. If empty, it's hiding doubts, not lacking them |
| Link Weaver | Open three source pages. Does the link read naturally, or like an ad? |
| Reporter | Recompute one before/after yourself, then check LEDGER.md against what you really published |

After a month of clean checks, check monthly; if one fails, go weekly for that bot.

## 10. What stays yours

Approving keywords · publishing · sending anything to another human (outreach, review replies, comments) · spending money (tools, links, ads) · deleting or redirecting a page · touching a page inside its 90 days. And four things bots do worse than you: **knowing the buyer**, **originating the one thing** (a real test, number, screenshot, photo), **the verdict** ("I tried both; here's what I'd pick"), and **waiting**.

## 11. Seven common mistakes

1. Skipping SITE.md.
2. Letting the Scout decide.
3. Lifting the pace limit "just this week".
4. Editing a page in its window because the graph dipped (the dip is part of the transition).
5. Starting with a technical-audit bot (keywords, pages and internal links first).
6. Adding link bots in week one.
7. Trusting a volume because a bot said it (volumes are estimates; your impressions are the real number once you're top 3).

## 12. Limits (the author's own, plus mine)

- Grok Bot is new (beta); nobody has a year of results on it. A bot can be wrong with total confidence, so the gates are human.
- Google may show a bot a captcha or a different page than a person sees. If the SERP Reader is blocked often, read the results yourself for the GO keywords.
- Nothing guarantees a position, date or traffic number. SEO is probabilities.
- Your data access sets your quality: a team working from estimates instead of your real Search Console is "guessing politely".
- **Mine:** the 90-day rule, the 1-2 pages/week pace and the DR bands are the author's heuristics, not Google rules. Treat them as defaults to tune. Paid tools mentioned (backlink and keyword tools) cost money; Search Console and a free crawl cover the core.

## 13. One-weekend setup

**Saturday:** write SITE.md by hand · export a crawl and 16 months of Search Console into `/workspace/seo/` · fill LEDGER.md with every page changed in the last 90 days (be honest) · create the 9 bots (shared block + own section).
**Sunday:** run Data Clerk once and verify numbers against Search Console · run Scout → SERP Reader → Director · if the Director approved more than 2 keywords, tighten it · approve **one** keyword.
**Next week:** set the schedules · ship that one page perfectly (it's the template) · read Friday's report · add optional bots only after a full month.

**Only one hour?** (1) Write SITE.md. (2) In Search Console filter positions 5–20, sort by impressions, pick the biggest query where you're the right page type. (3) Give that page 5 internal links in sentences from same-topic pages with its exact keyword as anchor, then don't touch it for 90 days.
