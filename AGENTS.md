# Agent instructions: website-building toolkit

This directory is a reference library, not a codebase. Use it to pick skills, GitHub repos and MCP servers while building a website.

## How to look things up (progressive disclosure — don't load everything)

1. Start at `README.md` (stage map).
2. Fixed stack wanted? Read `playbook/01-top-pick-per-stage.md` or `playbook/03-recommended-indie-stack.md`.
3. Need options for one stage? Open only that file in `catalog/stages/NN-*.md`.
4. Need install commands? `catalog/01-quick-install-starter-set.md`.
5. Need rationale/detail? `guides/NN-*.md`.
6. Anything about cost, free-tier limits or commercial use? `pricing/pricing.md`.
7. SEO / GEO / `llms.txt`? `seo/README.md`. Competing for AI recommendations? Measure with `seo/ai-visibility-gap-audit.md`, act with `seo/ai-recommendation-playbook.md`.
8. Social video / weekly trend content? `marketing/claude-head-of-content-trends.md`.

## Rules

- Read `playbook/00-principles.md` and `playbook/04-gotchas-and-rules.md` before choosing tools. Short version: skills for *method*, docs MCPs for *knowledge*, one browser MCP for *eyes*, as few *hands* MCPs as possible (read-only or test mode where available).
- Don't recommend repos listed in `catalog/00-legend-and-exclusions.md` as excluded (archived/deprecated).
- Items in `playbook/05-not-verified-or-dropped.md` are unconfirmed; say so if used.
- Each `catalog/stages/NN-*.md` ends with a "💰 Pricing" section (free tier → paid) for that stage's paid services; FOSS tools are omitted.
- Star counts and prices are as of 2026-10-11. Re-check vendor pages before committing to a paid plan.
- Catalog columns: Name | URL | Official? | ★ | Last push | Purpose | Free notes. Skills install via `npx skills add owner/repo` or `/plugin marketplace add owner/repo`.

## Library intake (whenever the user shares a new repo, skill, tool, guide or thread)

Follow `library/README.md`: inspect it, classify it on every dimension in `library/TAXONOMY.md` (add new tag values or dimensions when nothing fits, and log them in the changelog), write a card in `library/items/`, place it (stage catalog row or a cleaned write-up in `seo/`, `marketing/` etc.), then run `python3 library/scripts/build_index.py`. Check a card's `commercial-use`, `cost` and `requires` before recommending the item. Don't push until the user asks.
