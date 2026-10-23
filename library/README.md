# Library: every resource you give me, tagged

Each resource (repo, skill, MCP, tool, guide, prompt) has **one card** in `items/<slug>.md`, with tags from [TAXONOMY.md](TAXONOMY.md).

- [INDEX.md](INDEX.md) is **generated** from the cards. It has the full table plus a "by tag" view for every dimension. Don't edit it by hand.

```bash
python3 library/scripts/build_index.py   # regenerate INDEX.md after adding or editing cards
```

## Finding things

- **By stage or type:** open [INDEX.md](INDEX.md) and jump to the dimension you want, e.g. *By task → video-editing* or *By cost → free*.
- **By any field:** `grep -l "task:.*captioning" library/items/*.md`.
- **Before recommending an item:** check `commercial-use`, `cost`, `requires` and `trust.verified`.

## Intake procedure (for the agent, whenever the user shares something new)

1. **Inspect it.**
   - For a GitHub repo: description, stars, last push, license, topics, file tree, README, and any `SKILL.md` or `plugin.json`.
   - For a pasted article: identify who wrote it and what they sell.
2. **Classify it on every dimension** in [TAXONOMY.md](TAXONOMY.md).
   - If no value fits, **add a new value**.
   - If the item needs a new way to slice the library, **add a new dimension**.
   - Log either change in the taxonomy changelog. The taxonomy should grow with the content.
3. **Write the card** at `items/<slug>.md`, using the format below.
4. **Place it.**
   - If it matches a lifecycle stage 01–19, add a row to the right table (Skills, Repos or MCPs) in `catalog/stages/NN-*.md`, plus pricing if it's paid.
   - If the user pasted content (a guide or thread), write a cleaned "peak version" in the right folder: `seo/`, `marketing/`, `content/`, … Link it with `local:`.
5. **Rebuild** with `python3 library/scripts/build_index.py`.
6. **Report** the tags and placement to the user. Push only when they ask.

## Card format

```markdown
---
name: Human name
url: https://...
local: path/in/repo.md        # or -
summary: One line on what it does and why it matters.
type: [skill-pack, plugin, github-repo]
stage: [20-content-production]
task: [video-editing, captioning]
content: [video, audio]
content-format: [vlog, long-form-video]
agent: [claude-code]
software: [davinci-resolve, ffmpeg]
channel: [youtube]
cost: free-needs-paid-deps
license: cc-by-nc-4.0
commercial-use: no
requires: [paid-software, paid-api, python]
level: advanced
source: community
maturity: new
verified: yes
stars: 4
last_push: 2026-10-23
added: 2026-10-23
related: [other-slug]
---

Free-form notes: what's inside, how to install, caveats, how it compares to similar items.
```
