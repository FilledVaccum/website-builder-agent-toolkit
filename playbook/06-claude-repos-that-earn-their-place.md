# 10 Claude/agent repos that earn their place (and what to skip)

From a creator's article ("I tried 100+ Claude repos; these are the 10 I use"). The author's workflow is *finish something a business will pay for* (edited videos, a booking app, a scraped lead list). Stars and licences below are **live GitHub data from 2026-10-23**, not from the article. Opinions are the author's.

> Install **one** tool for the problem you have now. Installing everything at once makes it impossible to tell what broke.

## The 10

| # | Repo | Stars | Licence | Use it for | Stage in this repo |
|---|---|---|---|---|---|
| 1 | [HyperFrames](https://github.com/heygen-com/hyperframes) (HeyGen) | 70.3k | Apache-2.0 | Tell the agent what you want; it builds the video in HTML/animation and renders a real MP4 locally (captions, title cards, promos). No per-render fee. Alternative: [Remotion](https://github.com/remotion-dev/remotion) (66.5k★, custom licence, check commercial terms) | 20 content production |
| 2 | [Google Workspace CLI](https://github.com/googleworkspace/cli) | 31.8k | Apache-2.0 | Agents work across Drive, Gmail, Calendar, Docs, Sheets, Slides, Chat. Works from Claude Code, Codex or any agent, not tied to one app. Setup needs a Google Cloud project; give it access only to the apps you need | 22 business ops |
| 3 | [Apify MCP server](https://github.com/apify/apify-mcp-server) | 12.7k | MIT | Ready-made scrapers for Instagram, TikTok, Amazon, Reddit, maps and more, for sites Claude can't read. **Scrapers run on Apify's cloud (pay per usage; free plan had $5/mo credit)**. Alternative: [Firecrawl](https://github.com/firecrawl/firecrawl) (AGPL-3.0) | 2 research |
| 4 | **Scrollcraft** (author's own) | n/a | n/a | Scroll-driven "Apple-style" sites: a scroll engine, design rules, and a checker that screenshots along the scroll. **I could not find the author's repo** (searches only returned unrelated projects). Treat as unverified | 3 design / 5 frontend |
| 5 | [Humanizer](https://github.com/blader/humanizer) | 59.8k | MIT | Skill built on Wikipedia editors' guide to AI-writing patterns. Removes repetitive contrast sentences, forced triples and hype words from copy and cold emails while keeping the meaning | 20 content production |
| 6 | [Addy Osmani's Agent Skills](https://github.com/addyosmani/agent-skills) | 109.8k | MIT | `/spec` → `/plan` → `/build` keep the spec and tasks in **files**, so a fresh session can resume after context compaction. The spec also surfaces edge cases (double bookings, refunds, time zones) and can go to the client. Alternatives: [Superpowers](https://github.com/obra/superpowers) (303.9k★), [Matt Pocock's skills](https://github.com/mattpocock/skills) (301.3k★) | 1 planning |
| 7 | [Expo skills](https://github.com/expo/skills) (official) | 3.0k | MIT | Mobile app from idea to your phone, plus App Store/TestFlight guidance and Expo's "20 things that make an app look AI-built". **Ask for the skills by name; they don't always auto-load.** Apple Developer Program was $99/yr in the walkthrough | 5 frontend |
| 8 | [Supabase agent-skills](https://github.com/supabase/agent-skills) + [Stripe `stripe/ai`](https://github.com/stripe/ai) | 2.9k / 2.0k | MIT | Auth, database and payments guidance (users see only their own data; verify webhooks truly come from Stripe). Start Stripe with the `stripe-best-practices` skill, not the whole plugin (the broader plugin can steer vendor choices toward Stripe). Set the Supabase connector to read-only while inspecting | 6 backend, 7 auth, 9 payments |
| 9 | [Playwright CLI](https://github.com/microsoft/playwright-cli) + Claude security review | 14.5k | Apache-2.0 | Opens a real browser and clicks through the customer journey, writes re-runnable tests; lighter on context than a browser MCP. Security: Anthropic's [claude-code-security-review](https://github.com/anthropics/claude-code-security-review) (6.5k★, MIT-style Action, last push 2026-02-11) is the closest repo I found to what the article calls "Claude Security"; the plugin with separate challenge agents is **not confirmed** | 11 testing, 18 security |
| 10 | [OpenSEO](https://github.com/every-app/open-seo) | 24.6k | MIT | Keyword, ranking and backlink data for the agent. Free trial credits were small; data is stored on the provider by default (self-host to avoid that) | 13 SEO |

**Rule from the article:** installing a skill doesn't replace checking. Before launch, log in as a test user and confirm you can't read another user's data. Make verification part of the project.

## Token-saving tools: the author's test (treat with caution)

On JetBrains coding tasks the author measured far less than advertised savings. These are their results, not universal:

| Tool | Repo (stars) | Claim vs author's result |
|---|---|---|
| Caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (114.5k) | Claims 65% fewer tokens; author saw ~8.5% fewer *output* tokens |
| RTK | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) (84.3k) | Claims 60–90%; no meaningful saving, and costlier at low effort |
| Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (174.1k) | ~10% per task, about half the advertised; open Windows issue that could stall messages |
| Codeburn | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) (11.6k) | Not a saver, a **meter**: local tool showing token spend and waste (e.g. an unused MCP server that loads every message). Worth a look |
| claude-mem | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) (102.4k) | At the author's recording time it sent usage data by default |
| Context Mode | [mksglu/context-mode](https://github.com/mksglu/context-mode) (31.9k) | At recording time an open issue could burn through usage |

Output-token cuts and money saved per task are different measurements. Defaults and issues are version-sensitive: **check the current README and issues before installing.**

## Where to start

1. Pick the tool that solves your most frequent problem. Practical starters: Google Workspace CLI, Apify, Scrollcraft, Humanizer.
2. A concrete first project from the author: find businesses without a website, build a sample page, clean the copy with Humanizer, send them the link.
3. Anyone can install a repo. A client pays for the finished thing that solves their problem.

## Caveats

- The author built Scrollcraft and says the HyperFrames recommendation isn't sponsored; I can't verify either.
- Star counts here are higher than the catalog's 2026-10-11 numbers for the same repos because they were re-read today.
- Tags and cards: see [`library/`](../library/INDEX.md) (all ten have cards).
