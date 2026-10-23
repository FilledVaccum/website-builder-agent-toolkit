# Backlink directory submission automation (DRsubmission / Backlink Pilot)

**Repo:** https://github.com/Mimimiraclez/DRsubmission, a fork of [s87343472/backlink-pilot](https://github.com/s87343472/backlink-pilot) (MIT; upstream 375★). Fork: 20★, created 2026-10-19. Checked 2026-10-23 by reading the README, tree and `src/captcha.js`. **I did not run it.**

**What it is:** a Node CLI that drives real Chrome (via `bb-browser`, or Playwright) to fill in "submit your site" forms on web directories, AI-tool directories and startup lists, one after another with a 1-minute gap. Other commands: `scout` (preview a form), `awesome` (draft an awesome-list issue), `indexnow` (ping search engines), `report`, `prune`.

## What the fork changes (its own README)

- Upstream listed 259 sites; this fork keeps **82 auto-form targets** after removing dead, paid, login-walled and no-form ones.
- Adds a batch runner (`run`), a bb-browser 0.14 fix, and per-product tracking.

## Its own results (honest, worth reading)

| Measured | Count |
|---|---|
| Form filled and submit clicked | 70 |
| Fields filled, no submit button | 4 |
| Timeouts | 8 |
| **Live listing verified on a directory** | **0** |

Every success message is "Generic submission completed — verify manually". So treat it as "forms were submitted", not "you got backlinks".

## Should you use it?

**Mostly no, for a normal brand site. Maybe, narrowly, for a new indie/AI product.**

| Concern | Why it matters |
|---|---|
| **Low-value links** | About half the list is generic "web directory" sites (e.g. "All States USA Directory", "Free PR Web Directory"). Google has long treated mass directory links as low value, and it can count paid or manufactured link schemes as spam. |
| **Zero verified listings** | The repo itself found no published listing after 70 submissions. |
| **Doesn't help AI visibility much** | The [AI recommendation playbook](../seo/ai-recommendation-playbook.md) says editorial mentions and listicles drive AI citations, and to avoid manufactured mentions. Bulk directories are the opposite. |
| **Bot-check bypass** | `src/captcha.js` auto-solves simple "click the {colour} button" CAPTCHAs. Beating a site's bot check goes against what the site asked for. |
| **Security surface** | Needs a global `npm install -g bb-browser` plus a Chrome extension, controlling your real browser. Review the code and use a separate Chrome profile with no logged-in accounts. |
| **Reputation and spam** | You give the same email to 80 sites. Use a dedicated address. Spam and follow-up mail will follow. |

## When it can be reasonable

- **A brand-new product** with no mentions anywhere, and you want to be listed on the handful of reputable AI/startup directories (Future Tools, AI Valley and similar in its list). Submit those by hand; it takes minutes and gets you a real page to check.
- **Use `scout`/`awesome`** to prepare submissions you review yourself.
- **Skip the generic web-directory half** of the list entirely.

If you do run it: separate Chrome profile, dedicated email, `--dry-run` first, then verify listings manually after a few weeks and delete targets that produce nothing.

## Tags

See [library/items/drsubmission.md](../library/items/drsubmission.md).
