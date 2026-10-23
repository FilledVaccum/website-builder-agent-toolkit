# What predicts ChatGPT citations: findings from a large study

A summary of a reported analysis of **129,000 websites, 216,524 pages and 100,000 prompts** (attributed to SE Ranking) that looked at what separates sites ChatGPT cites from sites it doesn't. I only have it second-hand, through a vendor's write-up, and I have not read the original study or checked the numbers. The write-up's sales offers are omitted. Treat everything below as **correlation, not proof of cause**.

- **Use with:** [AI recommendation playbook](ai-recommendation-playbook.md) (levers), [gap audit](ai-visibility-gap-audit.md) (measure), [startup SEO playbook](startup-seo-playbook.md) (checklist).

## The findings

| # | Factor | Reported result | Reading |
|---|---|---|---|
| 1 | **Backlinks / referring domains** | Sites with 32,000+ referring domains were **3.5×** more likely to be cited. The strongest factor in the study | Authority gets you discovered and retrieved. The 32k threshold is far beyond most sites, so read it as "more is better", not a target |
| 2 | **Domain trust** | Very high-trust domains earned nearly **4×** more citations than low-trust ones | Same direction as #1 |
| 3 | **Overall search presence** | Sites with 7,900+ homepage visitors had **2×** the citation likelihood; 190,000+ monthly visitors gave nearly **2×** the citations of smaller sites | AI search isn't separate from search visibility: a site with little presence has fewer chances to enter retrieval |
| 4 | **Reddit and Quora mentions** | Domains with many mentions had **4×** higher citation likelihood; smaller brands also saw lifts | Mentions reinforce what you do, your category and that real people talk about you |
| 5 | **Content depth** | Articles under 800 words averaged **3.2** citations; over 2,900 words averaged **5.1** | Words alone don't do it. The stronger pages had multiple angles, examples, expert quotes, verifiable data and broader topic coverage |
| 6 | **Structure** | Well-structured pages earned **70%** more citations | Clean headings, concise sections, logical order, question-style H2s, clear answers. Walls of text and vague brand story give the model little to extract |
| 7 | **Freshness** | Pages updated in the last 3 months averaged **6.0** citations vs **3.6** for older pages | The write-up says "nearly doubled"; 6.0 vs 3.6 is about **1.7×** |
| 8 | **Question titles and FAQs** | Helped, especially for smaller sites, **when combined** with depth, authority and structure | A supporting factor, not a trick |
| 9 | **llms.txt** | Impact was **negligible** | Consistent with the rest of this repo: don't prioritise it |
| 10 | **Review platforms** | Brands on Trustpilot, Capterra, G2, Sitejabber and Yelp earned **3–6×** more citations than brands with no presence | AI judges you partly by third-party reputation, not only your own site |
| 11 | **Core Web Vitals** | Fast pages were cited **3×** more than slow ones | You don't need perfect scores, just avoid a painfully slow site |

**Summary from the study:** the drivers are backlinks, domain trust, homepage authority, Reddit/Quora presence, deep content, clear structure, recent updates, review-platform visibility and speed. Many of them also help in Google, with extra social, structural and entity signals on top.

## What to do (free actions, in order of effort)

| Effort | Action | Factor |
|---|---|---|
| **Today** | Update your 5–10 most important pages with real changes (new data, examples) and show the update date | 7 |
| **Today** | Check that the site isn't slow: PageSpeed Insights, Search Console Core Web Vitals | 11 |
| **This week** | Restructure key pages: question-style H2s, the answer in the first lines, short sections, a short FAQ | 6, 8 |
| **This week** | Claim free profiles on review sites relevant to you (e.g. G2/Capterra for software, Trustpilot/Sitejabber for consumer, Yelp/Google for local) and collect genuine reviews | 10 |
| **Ongoing** | Take part in relevant Reddit and Quora threads: useful answer first, disclose affiliation, no spam | 4 |
| **Ongoing** | Deepen the pages that matter: more angles, examples, expert quotes, sourced data (not padding) | 5 |
| **Ongoing** | Earn links with real assets: original data, tools, useful resources, digital PR, partnerships, relevant guest posts, unlinked-mention outreach | 1–3 |
| **Skip** | `llms.txt` as a ranking tactic (cheap to add, don't expect results) | 9 |

## Caveats

- **The source is a vendor post selling SEO services.** Its framing ("backlinks mattered most") conveniently supports what it sells. Look for the original study and its method before relying on specific numbers.
- **Correlation, not causation.** Big, trusted, fast, well-reviewed sites tend to have all of these. Adding Reddit mentions or words to a weak site may not move citations.
- **Averages hide a lot.** "5.1 vs 3.2" are averages across sites. The ranges, controls and sample sizes per bucket aren't given.
- **Thresholds like 32,000 referring domains or 190,000 monthly visitors** mostly describe large sites; they aren't realistic goals for a new one.
- **Authority is a long game.** For a young site, structure, freshness, speed, reviews and community presence are the levers you can pull this month.
