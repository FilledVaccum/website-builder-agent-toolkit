# Startup SEO playbook: the full checklist

A practical, ordered SEO checklist for a startup site, from domain to AI search. Adapted from a founder's X thread (author's claim: **1B+ impressions and 1M+ clicks** from SEO; not verified). Opinions are the author's; where I disagree or can't back a claim, it's flagged in [Judgement calls](#judgement-calls-read-before-acting).

- **Use with:** [free-seo-geo](free-seo-geo/SKILL.md) (inventory and fixes), [AI recommendation playbook](ai-recommendation-playbook.md) (AI answers), [gap audit](ai-visibility-gap-audit.md) (measure).
- **Order of work:** domain → technical → indexing → analytics → quick wins → blog → backlinks → social → AI search. Do the weekly loop (section 4) forever.

---

## 1. Domain

| Rule | Why |
|---|---|
| TLD: `.com`, `.org`, `.dev`, `.ai` or `.io` | Familiar to users and well supported |
| Keyword-like name (e.g. `osssoftware.org`) | Helps relevance and recall |
| About 14 letters or fewer | Easy to type and say |
| No `-` or `_` | Looks spammy and is harder to share |
| One topic per domain where possible | Clear topical focus |
| Pick `www` **or** non-`www`, redirect the other (301) | Avoids duplicate versions |

## 2. Technical SEO

**Quick check:** give your URL to Claude or Codex and ask: *"Is this page doing everything right for technical SEO?"* They'll list the details. Then verify with Search Console.

- [ ] **HTML renders for bots.** The content is in the server response, not only added by JavaScript. Test: view source or `curl` the URL.
- [ ] **HTTPS** everywhere.
- [ ] **Mobile-friendly.**
- [ ] **Fast enough to not feel broken.** PageSpeed Insights is enough. In Search Console, open **Core Web Vitals**; green means you're fine.
- [ ] **Short, stable URLs.** The slug should match the title and H1. No random strings.
- [ ] **One H1 per page.**
- [ ] **Unique title and meta description per page.**
- [ ] **Alt text** on images that matter.
- [ ] **Canonical URL** on every indexable page (the clean URL, without a query string).
- [ ] **No 404s and no redirect chains.**
- [ ] **No orphan pages.** Every important URL has at least one internal link pointing to it. (A crawler such as SEOgets lists orphans; Screaming Frog free also works.)

## 3. Indexing

1. Submit **`sitemap.xml`** in Google Search Console (GSC).
2. Check the **Pages** report: are all your pages indexed?
3. Repeat for **Bing** (Webmaster Tools) and **Yandex** if relevant. IndexNow covers Bing and Yandex.
4. Make sure **`robots.txt`** exists and allows your public pages (ask an AI assistant to review it).
5. **Request indexing** in GSC (URL Inspection → Request indexing) for new pages. Tools like IndexRusher automate this.
6. Fix **"Crawled – currently not indexed"** on pages that should rank.
7. **Don't waste crawl budget.** Don't launch with a huge number of pages, folders, tags or groups. Index the first batch, then expand.

## 4. Analytics and the weekly loop

**Tools:** Google Search Console (free), a small Ahrefs plan (optional), SEOgets and DataFast (the author's picks, both paid third-party products).

**Once a week, look at:**

| Signal | Action |
|---|---|
| Queries with **impressions but few clicks** | Put the query into the H1 and meta title of the page that shows for it |
| Pages that **used to get clicks and decayed** | Update the content |

## 5. Low-hanging fruit (do before writing anything new)

| Situation | Action |
|---|---|
| **Pages in positions 8–20** (closer to page 1 than any new article) | Add the exact query (if it makes sense) to H1 / title / H2. Add one section the current top results have and you lack. |
| **Lots of impressions, almost no clicks** | Rewrite title + meta; keep the keyword. |
| **Old pages with a little traffic** | Update them before writing new ones. Regular real updates help. |
| **Google knows the page but didn't index it** | Request indexing page by page. If that fails, remove or rewrite it; Google may never index it. |
| **Thin pages competing for the same query** | Keep the stronger URL; merge the weaker into it or 301 redirect. |

## 6. Quick 5-minute wins

- [ ] GSC → URL Inspection → **Request indexing** for the page.
- [ ] Put the target keyword in the **first 60 characters** of the title.
- [ ] Add the main query to the **H1** if it's missing.
- [ ] Add **2 internal links** from older posts to the page you want to push.
- [ ] Add alt text to the first image.
- [ ] Add a **3-question FAQ** at the bottom, using real queries from GSC.
- [ ] Submit or resubmit `sitemap.xml`.
- [ ] Search `site:yourdomain.com` and check which pages are indexed and how they look.
- [ ] Google your **brand + product keyword**. If a page mentions you without a link, ask them to add one.
- [ ] Ask ChatGPT *"best tool for [keyword]"*, open the cited URLs, and contact those authors (see [Judgement calls](#judgement-calls-read-before-acting) on paying for links).
- [ ] Post the article URL on X / LinkedIn / Reddit with the keyword in the first line.
- [ ] Paste the URL into Claude: *"What 5 on-page fixes can I do in 5 minutes?"*

## 7. Blog

- **Cadence:** 1 good post a week. Write it yourself with AI assistance. Prioritise keywords where you already rank well.
- **Scale with AI, then upgrade:** tools like SEObot can generate drafts. See which get traction, then rewrite the promising ones into high-quality, human-made articles.
- **Before writing:** search the keyword on Google. Match the format that already ranks. Answer the question better than the current top 5.
- **Put in original material** that shows real experience: screenshots, your own numbers, what you actually tried.
- **Refresh posts that already get impressions.** Change the date **only** if the content really changed. No date tricks.
- **Page types to add on top of the weekly post:** "best X", "X vs Y", "X alternatives", and "how to" for the exact job your product does.

## 8. Backlinks

**Find who AI and Google already trust:**

1. Ask ChatGPT *"What's the best tool for…"*. List the URLs it used. Do the same in **Claude, Perplexity, Gemini and Grok**.
2. Search Google for your keywords. Find the pages that rank.
3. Contact those authors and ask to be included.

**Other places that still work:**

- Guest posts on sites that already rank for your keywords.
- "Best tools" roundups.
- **Unlinked brand mentions:** search Google for your brand name, then ask each site to turn the mention into a link.
- Directories (the author uses ListingBott to submit widely; see [Judgement calls](#judgement-calls-read-before-acting)).
- Link all your pages across all your sites where it makes sense, and **internally link** every site (post to post, page to page).

**When you pick a site to link out from or guest post on, check that it has:** real traffic, a topic close to yours, and a link that looks natural on the page. Avoid anything spammy.

## 9. Social media SEO

Social posts get indexed fast (Reddit, X, Substack, LinkedIn).

- **Watch rising keywords:** Google Trends, Radar on X.
- **Post around those trends** and include product links where they fit.
- **Find relevant posts through Google Search** and add useful comments. Mention the product only where it adds value. No spam.
- **Keyword in the first line** of every post.
- **Repurpose each good blog post** (linking back to the original URL):
  - 1 X thread
  - 1 LinkedIn post
  - 1 Reddit answer, where it helps
- **Reply under bigger posts in your niche.** Useful reply first; link only if it adds something.

## 10. AI search

Same game as SEO. Ask ChatGPT, Claude, Perplexity and Gemini:

- *"What's the best tool for [my keyword]?"*
- *"Best alternatives to [competitor]."*

If they don't mention you, look at **who they did mention**, and get onto those same pages. Measure it properly with the [gap audit](ai-visibility-gap-audit.md) and act with the [AI recommendation playbook](ai-recommendation-playbook.md).

---

## Judgement calls (read before acting)

| Author's tip | Caution |
|---|---|
| **Pay authors or swap links** to be included | Google's spam policy treats paid links meant to pass ranking signals as link schemes unless marked `rel="sponsored"` or `nofollow`. Paying for *inclusion* in an editorial review can also breach the publisher's disclosure rules. Prefer earned mentions, real data, partnerships and clearly disclosed sponsorships. |
| **"List on as many directories as possible"** (ListingBott) | Bulk generic directories give little value and can look manipulative. See [backlink-opportunities](../marketing/backlink-opportunities.md) and [the DRsubmission write-up](../marketing/backlink-directory-submission.md): pick relevant, reputable ones. |
| **"Social media backlinks have really high weight for Google"** | Author's experience, not a documented Google signal; most social links are `nofollow`. Social still helps discovery and indexing. |
| **Domain rules** (max 14 letters, specific TLDs) | Reasonable heuristics, not ranking rules. A great brand name beats a keyword domain. |
| **Mass-generated AI blog posts** (SEObot) | Fine as drafts, risky if published unedited at scale. Google targets scaled low-value content, which is why the author edits the winners by hand. |
| **Named tools** (IndexRusher, SEOgets, DataFast, SEObot, ListingBott) | Third-party paid products the author promotes, possibly with affiliate ties. I haven't tested them. Free alternatives: GSC, Bing Webmaster Tools, IndexNow, Screaming Frog (free tier). |
| **"1B impressions / 1M clicks"** | The author's own claim. |
