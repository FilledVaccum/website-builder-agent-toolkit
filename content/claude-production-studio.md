# The Claude "production studio": data room, motion room, edit room, and a skills shelf

A mental model and workflow for turning a plain-language request into a finished, exportable video **without a video-generation model touching the frame**: the animation is *code* you can read and edit. Adapted from a creator's X article. **Free-only edit:** the article's plan-gated features are described but not promoted; I did not verify any of its claims about Claude's native features (see [Caveats](#caveats)). The open-source skills below were checked on GitHub on 2026-10-24.

- **Related:** [code-rendered video studio](code-rendered-video-studio.md) (the discipline), [Remotion launch-clip tutorial](remotion-launch-clip-tutorial.md) (hands-on), [10 Claude repos](../playbook/06-claude-repos-that-earn-their-place.md).

## 1. The mental model: rooms, not apps

A studio is a set of specialised rooms connected by a workflow. When it all lives in one assistant, there are no exported files to go stale ("I changed the spreadsheet but forgot the chart").

| Room | Job | The article's feature | Availability (per the article; unverified) |
|---|---|---|---|
| **Data room** | Raw numbers become honest charts | Claude Dashboards: connect a data source or CRM, ask in plain language; Claude writes and runs the query, builds a dashboard that updates, and each chart carries its query | Beta, paid plans |
| **Motion room** | Charts and ideas become movement | Claude Motion: titles, chart draw-on, camera moves, beat-timed cuts, exported as MP4; animation written as code | Beta, Team/Enterprise plans |
| **Edit room** | Assemble clips, decks and documents for a human | Docs, Slides, Design co-edited in real time with Claude | Said to be available on all plans incl. free |

**No paid plan? Use the open layer** (section 5): you can build the same workflow with free tools, with Claude Code writing the animation code.

### Why "animation as code" is the whole game

A generator is a black box: wrong clip, re-prompt and hope. Code gives you:

1. **Every value is editable.** The number on screen is a variable, not baked pixels.
2. **Revisions are instant and precise.** "Draw the chart half a second slower" is a one-line change.
3. **Deterministic.** Same input, same output.
4. **Composable.** One value can feed a chart, a title card and a lower third, staying in sync.

You're not generating video; you're **compiling** it.

## 2. Data room: make the number true before you make it pretty

- **Ask the real question, not the chart you think you want.** "Which of our stations run empty before 9am on weekdays" beats "make me a bar chart."
- **Make it name its assumptions:** date range, filters, exclusions. A dashboard that hides its assumptions "lies politely".
- **Find the one number the video is about** before animating anything.
- **Free equivalent:** have Claude Code query your data (a CSV, database or analytics export) with a script that prints the query and its result, and keep the source file with the project. Animate from that checked figure.

## 3. Motion room

Point Claude at a report, chart or product walkthrough; it writes a short animation and exports an MP4 (titles, chart draw-on, camera moves, cuts to a beat). Free route: Remotion or HyperFrames with a skill (below).

## 4. Edit room

Write the narrative **first**, with holes where the video and charts go, then fill the holes from the other rooms. Writing the story before animating prevents beautiful clips that serve no point. The studio isn't done when the MP4 exports; it's done when the piece is in a form someone can read, present or publish.

## 5. The skills layer: open-source repos (live GitHub data, 2026-10-24)

You need two or three, not ten.

### A. Rendering full videos in code

| # | Repo | Stars | Last push | Licence | Use it for |
|---|---|---|---|---|---|
| 1 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 66.6k | 2026-10-23 | custom ("NOASSERTION"; check terms) | Whole videos as React components: titles, charts, transitions, synced audio. The engine |
| 2 | [remotion-dev/skills](https://github.com/remotion-dev/skills) | 5.6k | 2026-10-22 | not stated | Official agent skills: empty project to finished render. Remotion with this is an operator, without it a library |
| 3 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 70.6k | 2026-10-23 | Apache-2.0 | Write HTML, render video; assembles scenes into a promo/explainer cut to music |
| 4 | [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | 2.1k | 2026-10-14 | not stated | Edit your own footage: kill dead pauses, cut stumbles, assemble a Reel, add subtitles ("Herk Edit Kit"; its description also names Codex) |

### B. Moving the web and the interface

| # | Repo | Stars | Last push | Licence | Use it for |
|---|---|---|---|---|---|
| 5 | [motiondivision/motion](https://github.com/motiondivision/motion) | 34.5k | 2026-10-23 | MIT | Site animation: fade-ins, hover, scroll effects (web pages, not video files) |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web) | 32.3k | **2025-09-01** | MIT | Lightweight animated icons, logos and loaders. **No push for about 13 months**; check it still meets your needs |
| 7 | [greensock/GSAP](https://github.com/greensock/GSAP) | 29.6k | 2026-04-13 | custom (GreenSock terms; check) | Complex synchronised timelines where text, images and elements move together |

### C. Teaching Claude taste, not just syntax

| # | Repo | Stars | Last push | Licence | Use it for |
|---|---|---|---|---|---|
| 8 | [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 2.5k | 2026-05-18 | MIT | Craft decisions: how fast things move, easing, the order elements enter. **The author's most underrated pick** |
| 9 | [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) | 816 | 2026-10-13 | not stated | Animated cards, diagrams and charts that appear on cue under the words a speaker says |
| 10 | [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design) | 654 | 2026-10-04 | MIT | Full promo pipeline in pure code (HTML + Playwright): transitions, camera moves, music-synced cuts, SFX |

**"Start here" index:** the article points to [Mort1d/motion-graphics-skills](https://github.com/Mort1d/motion-graphics-skills) as a running index of motion skills. On GitHub it's described as *"Showreel-grade motion graphics from code, with an original soundtrack for every…"* (61★, last push 2026-09-30), so it looks like a skill pack rather than an index. Look before you rely on it.

**Honest pick (the author's):** a **taste skill (#8)** plus **one pipeline skill (#2 or #10)** gets about 80% of the result. Rendering libraries matter once you ship volume; web tools matter only if the output is a site.

Install with: `npx skills add <owner>/<repo>` (see each README).

## 6. The workflow: reference to finished clip

1. **Feed it the reference, not a description.** Give a video, screenshot or link and ask *why it works*: pacing, where the first motion lands, how text enters, when the payoff hits. You get a spec, not a vibe.
2. **Data room first** if the video has numbers. Animating a wrong number is a faster way to be wrong.
3. **Write the story** in a doc or slides, with holes for the video and charts.
4. **Hand the spec and the verified chart to the motion step.** Claude writes the animation as code, matching the reference. Add a taste skill always; a pipeline skill for full promos.
5. **Direct in words.** "The title's a beat late." "Draw the line slower." "Hold the final frame one more second." Each is a one-line edit, not a re-render.
6. **Assemble and ship:** the clip goes into slides, a doc, or an MP4 for a Short/Reel. First export is a draft.

## 7. Common mistakes

- **Animating before the number is checked.**
- **Describing a style instead of showing one** ("clean and modern" gives generic output; a reference gives a match).
- **Installing a rendering library when a taste skill was the real gap** (stiff, ugly motion).
- **Skipping the story:** impressive transitions with no point are watched once.
- **Treating the first export as final:** the whole advantage is that it's editable.

## 8. Your first week

| Day | Do |
|---|---|
| 1 | Co-edit one document or slide deck with Claude (get the feel) |
| 2 | Feed Claude a video you admire; have it write a spec of why it works; keep the spec |
| 3 | Install the motion taste skill (#8) plus one pipeline skill; make one short animation from the spec |
| 4 | Build one chart from a plain-language question over a real (or mocked) data file; animate that figure |
| 5 | Run the whole workflow once, reference to export, on something small and real. Ship it |

One real video beats ten tutorials.

## Caveats

- **Native features unverified.** I didn't confirm "Claude Dashboards", "Claude Motion", or the Docs/Slides/Design co-editing and their plan availability; they come from the article. Check Anthropic's current product pages.
- **Skills are third-party.** Review a skill's `SKILL.md` and scripts before installing; several have no stated licence ("not stated" above), so check before commercial use. Stars show popularity, not quality.
- **Remotion and GSAP licences are custom.** Read their terms for your use.
- **Stale repo:** `lottie-web` hasn't been pushed since September 2025.
- **"No video model" has limits:** code-made motion suits product films, UI motion, charts and typography; it's not for photoreal scenes or complex characters.
