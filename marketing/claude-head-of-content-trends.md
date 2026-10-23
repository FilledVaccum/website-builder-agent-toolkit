# Claude as Head of Content: weekly short-form video trend picks

A Claude Project that tells you **every Monday which TikTok/Reels trends to film this week**, whether you're early or late, and writes **your version shot by shot**.

- **What it replaces:** hours of scrolling the For You page and guessing whether a sound is "a trend".
- **What it needs:** a **trend data source** Claude can read. Claude has no live view of TikTok on its own.
- **Where it fits in this repo:** promotion after launch. For being *recommended by AI assistants*, see [../seo/ai-recommendation-playbook.md](../seo/ai-recommendation-playbook.md). This file covers *social video*.
- **Source:** adapted from a Virlo launch guide. Virlo's claims (an 18M+ video database, a brand-safety pipeline, the trend stages) are theirs and I haven't verified them. The stage thresholds below are my suggested defaults, not Virlo's.

> **Rule zero:** if Claude isn't connected to a trend data source, it must say so and stop. Otherwise it will make up plausible trends and creator counts.

---

## 1. The job description (write this before touching tools)

| Part | Definition |
|---|---|
| **Owns** | Which content trends to film this week. A **trend** is a format hundreds of creators copy; a **topic** is just what they talk about. |
| **Perfect Monday** | Pull this week's trends → compare creator counts with last week → drop the ones that don't fit → pick 1–3 → write your version. |
| **Decides alone** | Early or late, and fit or skip (with a one-line reason). |
| **Good output** | Something you can film on a phone today, with *what to keep the same* and *what to make yours*. |

---

## 2. Trend data sources

| Source | Cost | What you get | Can Claude read it directly? |
|---|---|---|---|
| **Virlo** (Trends → sort by "Most creators this week") | Free account (per source) | Creators per trend this week vs last week, a stage label, a keep/change "recipe", brand-safety, effort and tone ratings | Yes, via its Claude connector (per source) |
| **TikTok Creative Center** (Trends: songs, hashtags, creators, videos) | Free | Trending sounds and hashtags with growth curves, by region and industry | No. Export or paste it in, or attach screenshots |
| **Instagram Reels** (trending-audio arrow ↗ in the audio picker) | Free | Rising audio on Reels | No. Paste it in manually |
| **YouTube Shorts** (Shorts tab, "trending" audio) | Free | Rising Shorts audio and formats | No. Paste it in manually |

**Without a connector:** every Monday, paste the top 20 trends with **creators this week** and **creators last week** into the Project chat. The prompts below work the same way.

---

## 3. Lifecycle stage: early or late?

What matters is the **week-over-week (WoW) change in the number of creators posting the trend**, not view counts.

`WoW = (creators this week − creators last week) ÷ creators last week`

| Stage | Suggested rule (tune it) | Action |
|---|---|---|
| **Fresh** | First seen ≤ 2 weeks ago and still growing | Jump on it now. Biggest upside, least proof. |
| **Rising** | WoW ≥ +25% | Film it **this week**. |
| **Peaking** | WoW between −10% and +25%, at high volume | Post your version now, before it turns. |
| **Fading** | WoW ≤ −25% | You're late. Only post if it fits you unusually well. |
| **Archived** | Fading for 2+ weeks, or below the noise floor | Keep for reference only. |

**Worked examples (from the source guide):**

- **Then-and-now:** 67 → 263 creators, **+293%**, so **Rising** even though it's two months old. Age doesn't make a trend late; slowing growth does.
- **Makeup transition:** 222 → 106 creators, **−52%**, so **Fading**. Half the creators left in a week.

**Filter out fake trends:** a sound that's widely used but **not with the same format** isn't a trend. Check 3–5 sample videos before you count it.

---

## 4. Setup: a Claude Project

1. **Connect the data source.** In Claude, go to Settings → Connectors and add your trend source (e.g. Virlo), then sign in. If you don't have a connector, plan to paste the data in (section 2).
2. **Create the Project:** Projects → New project. Name it `HEAD OF CONTENT – [business]`. Add a description of what you sell.
3. **Add knowledge files (optional, recommended):** your brand voice notes, banned topics, the 5 best-performing videos you've posted (with links and why they worked), and your filming constraints (team size, locations, props).
4. **Paste the instructions** below, filling in the brackets.

```text
I am [name]. I run [business]. I sell [product/service] to [audience] in [market/region].
Brand voice: [3 adjectives]. Never: [banned topics/styles]. Filming capacity: [who, where, phone only?].

You are my Head of Content. Your job: tell me which short-form video trends to film this week.

DATA RULES
- Use [Virlo / the trend data I paste] as the only source of trends and creator counts.
- If no trend data is available in this chat, say "No trend data connected" and stop. Never invent trends, counts or sounds.
- Never promise a trend will go viral.

WHEN I ASK WHAT TO FILM
1. Pull this week's content trends (formats creators are copying, not just sounds or topics).
2. Rank by creators this week vs last week. Show both numbers and the % change.
3. Assign a stage: Fresh, Rising (≥ +25% WoW), Peaking (−10% to +25% at high volume), Fading (≤ −25%), Archived.
4. Skip anything that doesn't fit my business, brand voice or filming capacity, with a one-line reason.
5. Rate each kept trend: fit (1–5), effort (phone-only? props? people?), brand-safety risk (low/med/high).
6. For the top 1–3, give: KEEP THE SAME (sound, structure, timing, the hook mechanic), MAKE IT MINE (subject, setting, product, punchline), then a beat-by-beat script:
   - Hook / opening shot (0–2s)
   - Each beat with timestamp, shot, on-screen text
   - Caption (with a call to action) + 3–5 hashtags
   - Shot list I can film on a phone today
7. If a trend is Fading, say it's late, and only keep it if fit = 5.

FORMAT
Start with a table: Trend | Creators (this wk / last wk / %) | Stage | Fit | Effort | Risk | Film it? Then the scripts.
```

---

## 5. The prompts

| When | Prompt |
|---|---|
| **Every Monday** | `What trends should I film this week for [business]? Top 3, ranked.` |
| Catching one early | `Which of this week's trends are Fresh or Rising and fit [business], before they peak?` |
| Writing a script | `Write my version of [trend] for [what I'm promoting this week: product/listing/launch/offer].` |
| Checking timing | `Is it too late to post [trend]? Show the creator counts.` |
| Posting first elsewhere | `Which of this week's TikTok trends haven't spread to Instagram Reels yet, so I could post them there first?` |
| Reviewing results | `Here are last week's results [views, watch time, saves, profile visits]. What should I double down on?` |

---

## 6. Examples by industry (from the source guide)

| Business | Trend (stage) | Your version |
|---|---|---|
| Real estate | Then-and-now (Rising) | The listing on the day you took it → the same room staged. Caption: comment to get the listing. |
| SaaS | Paparazzi bowing (Fresh) | The team bows to a laptop showing a major feature release. |
| Restaurant / café | Rock-paper-scissors food (Fresh) | Staff play it over a signature platter. |
| Salon | Upside-down makeup (Peaking) | A client's transformation timed to the beat drop. |

---

## 7. The first 30 days

| Week | Do |
|---|---|
| 1 | Ask the Monday question. Film the **one** trend that fits best, and post it. |
| 2 | If it worked, post a second take on it, then add a second trend. |
| 3 | Take your best TikTok trend and post it **first on Reels** if it hasn't arrived there yet. |
| 4 | Lock in the routine: **Monday** pick, **Tuesday** film, **Wednesday** post, **Friday** paste the results back in. |

**Running several businesses?** Make one Project per business, with the same instructions and different brackets.

---

## Guardrails

- **Licensed audio:** brand or business accounts often can't use commercial music. Use the platform's commercial sound library, or pick trends that work with original audio.
- **Disclosure:** label paid partnerships or sponsored content as the platform requires.
- **Measure what counts:** watch time, saves, shares, profile visits and leads. Views alone don't tell you much. Feed the results back weekly (prompt above) so the picks improve.
- **No viral promises.** A trend is a format to borrow, not a guarantee.
