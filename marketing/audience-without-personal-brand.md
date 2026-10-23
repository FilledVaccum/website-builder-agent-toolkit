# Build an audience without a "personal brand": three distribution assets

For builders who accept that **distribution comes before product** but don't want to post their daily thoughts online. Adapted from a founder's article (the author runs a creator-partnership business, a UGC marketplace and a news site, and mentions all three). Their claims and results are theirs; I didn't verify them. Things to check before acting are in [Judgement calls](#judgement-calls-read-before-acting).

**The idea:** you don't need a personal brand to own a distribution asset. Pick one of three routes and stay with it for about two years.

| Route | You get | Time to results | Cost | Fits you if… |
|---|---|---|---|---|
| **1. Borrow a creator's audience** | Instant reach through a partner | Weeks to months (after outreach) | Low: your time, plus a build subscription | You can build simple software or products fast |
| **2. SEO + GEO** | An owned, compounding asset that raises the value of the business if you sell | 6–24 months | Low-medium: keyword and backlink data, plus some paid placements | You can wait, and can follow a steady process |
| **3. A media site** | Audience, backlinks and warm relationships in a high-value niche | 6–24 months | Low: hosting plus your time | You can interview or write about professionals |

---

## 1. Borrow someone else's distribution

**Why it works (author's numbers):** over 200M content creators exist; only about 2% (~4M) have 100k+ followers; around half earn under $15k a year; 67% have never done a brand deal. Many have an audience and no product. You have product skills and no audience.

**Author's result:** about 1,000 cold emails to US creators led to ~15 conversations, then a partnership with a large homesteading creator, which became a 7-figure creator business. (Reply rates on mass cold email are low.)

### Playbook

1. **Find creators in one niche.** Pull TikTok/Instagram creators for a vertical (finance, parenting, pets, cooking…) with a scraping API such as Apify. Check the platform's terms and the privacy rules first.
2. **Write tailored outreach by hand, about 10 minutes each.**
   - Open their profile and watch their last two videos.
   - Make the **first line explicitly about one of them**.
   - The author expects **5–10% replies**, against ~1% for generic mass email. Inboxes are full of generic AI-written messages, so effort stands out.
3. **Test demand before building.** Make a landing page with a signup form and discounted early-customer offers. Offer to set it up free for the creator.
4. **If there's demand and the product is simple** (a mini-SaaS), offer to **front the build cost** yourself (the author cites a ~$60/month AI coding subscription).
5. **Agree a revenue or profit share.** Draft the structure with an AI assistant, **then have a real lawyer review it** before you sign anything that matters.
6. **Launch.** You've done the hard part: finding the first audience.

**Outreach template (edit it, don't paste it):**

```text
Subject: your [specific video topic] video

Hi [name],
I watched your [video title]; [one specific, genuine reaction]. 
I build [simple product type] and noticed your audience keeps asking about [specific thing].
I'd like to build a [specific product] with you, at no cost to you. I'd cover the build, you'd keep [x]% of what it earns.
Worth a 15-minute call? I've put a one-page mock-up here: [link].
[Name]
```

---

## 2. SEO + GEO (own the asset)

**Why:** it's the long-term, lowest-cost acquisition you can own, and it adds to the sale value of the business, unlike a business that depends on one person's posting.

**Author's case:** after relying on Meta ads (constant new creative, tired audiences, algorithm swings), they built their own publishing/SEO software; within two months a store's traffic went from ~90% Meta ads to ~90% Google and AI search, with slow, compounding growth since April.

### Setup

1. **Keyword research first.**
   - Connect an AI assistant to Ahrefs (MCP) or the DataForSEO API to find **low-competition keywords** (difficulty under about 20), with real volume and clear intent.
   - Prioritise **question-style queries**. AI engines answer those, and you want to be the cited source.
2. **A content engine on a schedule.** Each article should have:
   - a **direct answer in the first paragraph** (this is what gets you quoted instead of scrolled past),
   - clean heading structure,
   - schema markup,
   - first-hand data or examples a model can't get elsewhere,
   - internal links.
3. **A review loop with Search Console, every two weeks.** An agent checks what's ranking, what's dead, which pages to merge or remove, and which new keywords to test. This loop turns a content pile into a compounding asset.
4. **Backlinks, systematised.**
   - Use a backlinks API (e.g. DataForSEO) to find sites with decent authority and traffic in your target market and a **similar field**. Relevance beats raw DR.
   - Find "write for us" / "contribute" pages with a scraper.
   - Have AI draft personalised pitches. Some placements charge a fee; budget for the good ones (and see the note on paid links below).
5. **Delegate the grind.** Everything but final editorial judgment can be automated. Your job is taste and the fortnightly review.

Related: [startup SEO playbook](../seo/startup-seo-playbook.md), [AI recommendation playbook](../seo/ai-recommendation-playbook.md), [free-seo-geo](../seo/free-seo-geo/SKILL.md), [gap audit](../seo/ai-visibility-gap-audit.md).

---

## 3. Build a media asset

**The mechanics:** start a news/interview site in a **high-value niche** (the author's example: a site for wealth and business stories). Offer professionals (lawyers, wealth managers, founders…) a feature or interview.

**Why it compounds (author's reasoning):**
- Being featured is a flex, so most people accept, and most have never been asked.
- They share the piece with their network. That's borrowed distribution that points to a platform you own.
- Some add it to their press page, which is a backlink that strengthens your domain, which grows organic traffic, which makes the next approach easier.
- Every interview is a warm relationship that could become a client, partner or buyer. No personal face needed.

**To start:**
1. Choose a niche where interviewees are valuable to you (clients, partners, buyers).
2. Set up a simple site (e.g. WordPress with a news template). Add About, contact and editorial-policy pages.
3. Publish 5–10 pieces first so the site looks real.
4. Pitch 10 people a week: a specific angle, a 5-question interview, a deadline.
5. Send each guest the live link and make it easy to share and link.

---

## The honest part: it takes 1–2 years

Every route, a personal brand included, takes **at least a year, realistically two**, if you're bootstrapping. The author's point: it's a 20–30-year game built from small, boring, daily actions (10 emails to creators, the scheduled article, the backlink pitch nobody sees). If nothing has worked yet, nothing is wrong; it's just early.

**Rule:** pick the one asset you can stomach building for two years, and put in reps every day.

---

## Judgement calls (read before acting)

| Claim / step | Caution |
|---|---|
| Creator statistics (200M creators, 2%, $15k, 67%) | Author cites them without sources here; I didn't verify. |
| "5–10% reply rate" and "most people say yes" | Author's experience. Expect lower, and measure your own. |
| Scraping creators (Apify) | Check each platform's terms and the privacy and email rules where you and the recipients are (e.g. GDPR, CAN-SPAM). Keep outreach one-to-one and honest, with a clear way to opt out. |
| Revenue/profit share | Get a lawyer. An AI draft is only a starting point. |
| Paid placements and fee-based guest posts | Links you pay for should be marked `rel="sponsored"` (or `nofollow`) and disclosed. Undisclosed paid links can breach Google's spam policy and the publisher's rules. |
| Tools named | Ahrefs and DataForSEO are paid (DataForSEO has a $50 minimum top-up per [pricing](../pricing/pricing.md)). A free route is Search Console plus manual research. |
| Media site | Disclose any sponsored features, and don't charge people to be "interviewed" without saying so. Quality and accuracy matter: a thin site of unvetted features helps nobody. |
| Timeline | 1–2 years is the author's estimate and fits normal SEO timelines. |
