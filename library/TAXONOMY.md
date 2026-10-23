# Tag taxonomy

Every item in `library/items/` gets tags from **each** dimension below.

## This taxonomy grows with the content

- **New value:** if no existing value describes an item well, add a new one. Don't force a poor fit.
- **New dimension:** if a new kind of content needs a new way to slice it (e.g. `language`, `industry`, `audience`, `pricing-model`), add a numbered section here and use it on the card. `build_index.py` picks up any new frontmatter key as a dimension automatically.
- **Merge or rename:** when two values mean the same thing, keep one and update the cards that use the other.
- **Sync:** every new value or dimension goes into this file and the [changelog](#changelog) in the same commit. `build_index.py` prints `add to TAXONOMY.md: …` for anything used on a card but not listed here.

Tags are lowercase-kebab. A field can hold several values: `[a, b]`.

## 1. `type`: what the item *is*

| Tag | Meaning |
|---|---|
| `skill` | A single SKILL.md an agent loads on demand |
| `skill-pack` | A repo or bundle of several skills |
| `plugin` | Installable Claude Code plugin (`.claude-plugin/`) |
| `mcp-server` | MCP server (local or hosted) |
| `github-repo` | Lives in a GitHub repo (add this alongside other types) |
| `library` | Code library or framework you import |
| `cli-tool` | Command-line tool |
| `app` | Desktop or web software you operate (e.g. DaVinci Resolve) |
| `saas` | Hosted service with an account |
| `guide` | Explanatory article or how-to |
| `playbook` | Step-by-step operational procedure |
| `prompt` | Copyable prompt or Project instructions |
| `template` | Starter file, config or boilerplate |
| `dataset` | Data source |
| `inspiration-gallery` | Curated gallery of examples to browse for ideas (not shippable assets) |
| `asset-library` | Downloadable assets (images, backgrounds, icons, sections) |
| `ui-kit` | Ready-made design files (Figma, Framer) |
| `community` | Network or forum of people |

## 2. `stage`: where it fits in the website lifecycle

`01-planning`, `02-research`, `03-design`, `04-assets`, `05-frontend`, `06-backend`, `07-auth`, `08-cms`, `09-payments`, `10-email-forms`, `11-testing`, `12-performance`, `13-seo`, `14-geo`, `15-analytics`, `16-vcs-ci`, `17-hosting`, `18-security`, `19-maintenance`

Plus stages after launch:

| Tag | Meaning |
|---|---|
| `20-content-production` | Making content: video, images, copy |
| `21-marketing-distribution` | Promoting it: social, outreach, trends |

The numbers 01–19 match the files in [`catalog/stages/`](../catalog/stages/).

## 3. `task`: the job it does

Pick the specific jobs. Add new ones as needed, then list them here.

- **Planning & research:** `spec-writing`, `task-breakdown`, `competitor-research`, `web-scraping`, `trend-research`
- **Design & build:** `ui-design`, `design-system`, `code-generation`, `docs-grounding`, `site-building`, `figma-templates`, `design-inspiration`, `ui-animation-reference`, `icon-search`, `font-identification`, `background-assets`, `networking`
- **SEO / GEO:** `seo-audit`, `technical-seo`, `schema-markup`, `keyword-research`, `geo-audit`, `citation-tracking`, `ai-crawler-access`, `content-optimization`, `outreach`, `measurement`
- **Video:** `video-editing`, `rough-cut`, `pacing`, `b-roll`, `captioning`, `audio-mixing`, `music-scoring`, `sound-design`, `motion-graphics`, `video-export`, `scriptwriting`
- **Ops:** `testing`, `monitoring`, `deployment`, `security-review`, `automation`

## 4. `content`: the media it works on

`text`, `code`, `image`, `video`, `audio`, `data`, `web-pages`

## 5. `content-format`: what kind of output

`short-form-video`, `long-form-video`, `vlog`, `tutorial-class`, `talking-head`, `blog-article`, `landing-page`, `listicle`, `comparison-page`, `social-post`, `report`

Leave it empty (`[]`) when it doesn't apply.

## 6. `platform`: where it runs and what it targets

Use three separate fields:

- **`agent`** (which AI host runs it): `claude-code`, `claude-ai`, `cursor`, `codex`, `copilot`, `any-agent`
- **`software`** (other tools it drives): e.g. `davinci-resolve`, `figma`, `framer`, `remotion`, `ffmpeg`, `google-search-console`, `ga4`, `bing`, `cloudflare`, `epidemic-sound`, `ffmpeg`, `virlo`, `tiktok-creative-center`
- **`channel`** (where the output is published or surfaced): `youtube`, `tiktok`, `instagram-reels`, `google-search`, `google-ai-overviews`, `chatgpt`, `perplexity`, `gemini`, `bing`, `website`

## 7. `cost`: what you pay to use it as intended

| Tag | Meaning |
|---|---|
| `free` | $0, including everything it needs |
| `free-needs-paid-deps` | The item is free, but it needs paid software or APIs |
| `freemium` | Free tier, then paid |
| `paid` | Paid only |
| `usage-based` | Pay per use |
| `unknown` | Pricing not confirmed |

## 8. `license`

The SPDX id (`mit`, `apache-2.0`, `cc-by-4.0`, `cc-by-nc-4.0`, …), or `proprietary` (all rights reserved or site terms) or `unknown`.

Also set `commercial-use`: `yes`, `no`, or `ask-author`.

## 9. `requires`: setup blockers

`account`, `api-key`, `paid-software`, `paid-api`, `oauth`, `local-install`, `python`, `node`, `gpu`, `none`

## 10. `level`: who can use it

`beginner` (paste and go), `intermediate` (some setup), `advanced` (scripting or APIs)

## 11. `trust`: how much to rely on it

| Field | Values |
|---|---|
| `source` | `official` (vendor), `community`, `vendor-content` (marketing from a company selling something), `user-authored` |
| `maturity` | `new` (< 3 months or < 50★), `active`, `established` (1k+★ or long track record), `archived` |
| `verified` | `yes` (I checked it exists and the facts match), `partial`, `no` (claims taken as given) |

## 12. Metadata (not tags)

`name`, `url`, `local` (path in this repo, if a copy exists), `stars`, `last_push`, `added` (date), `summary` (one line), `related` (other card slugs).

---

## Changelog

| Date | Change | Triggered by |
|---|---|---|
| 2026-10-23 | Initial taxonomy: 11 tag dimensions + metadata. Added stages `20-content-production` and `21-marketing-distribution`, video tasks, and software `virlo`, `tiktok-creative-center`. | video-editor-skills, claude-head-of-content-trends |
| 2026-10-23 | Added types `inspiration-gallery`, `asset-library`, `ui-kit`, `community`; tasks `site-building`, `figma-templates`, `design-inspiration`, `ui-animation-reference`, `icon-search`, `font-identification`, `background-assets`, `networking`; cost `unknown`; software `framer`. | 11 design-resource sites |
