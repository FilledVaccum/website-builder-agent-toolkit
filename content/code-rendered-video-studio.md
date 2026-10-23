# Motion engineering: build a code-rendered video studio around Claude Opus 5.5

How to get *directed* videos instead of "the same demo" (big centered text, gradient, fade-ins, logo at the end) when an AI model writes the program that draws the frames. The difference isn't a secret prompt; it's the **system around the model**. Adapted from a creator's X article; the model release details below are the author's and I haven't verified them. The newsletter promotion is omitted.

- **Best for:** product films, UI motion, data stories, typography, diagrams, launch explainers.
- **Not for:** photoreal scenes, complex characters, organic movement (use footage or generated video).
- **Hands-on build:** [Remotion launch-clip tutorial](remotion-launch-clip-tutorial.md).
- **Related:** [HyperFrames and Remotion](../playbook/06-claude-repos-that-earn-their-place.md), [video-editor-skills](../library/items/video-editor-skills.md) (editing real footage), [weekly trend picks](../marketing/claude-head-of-content-trends.md) (what to film).

## The core idea

The model doesn't imagine every frame as an image; it **writes a frame function**:

```js
function renderFrame(t, spec, assets) {
  // Draw the exact state of the film at time t
}
```

A renderer calls it across the timeline, captures frames and encodes a video file.

- **The program draws the frames; the renderer makes the film; the review loop decides whether anyone sees it.**
- **Revisions become local:** title too early → change one time value; shape overshoots → change one curve; wrong product screen → swap the asset and re-render. You never ask a video model to regenerate a whole shot and hope it remembers.
- **A prompt makes a clip. A studio makes the next clip without rebuilding itself.**

## The five layers

| Layer | Question |
|---|---|
| **Director** | What is the film trying to say? |
| **Reference** | What should it feel and look like? |
| **Timeline** | What changes at each beat? |
| **Renderer** | How is every frame produced? |
| **Critic** | What failed, exactly where, and why? |

Don't let the model collapse these into one uninspected step. When decisions are missing it fills them with the safest visual defaults, which is where generic output comes from. Remove the missing decisions *before* it starts rendering.

---

## 1. Write a director's brief, not a vibe prompt

"Make an insane product video" leaves every important choice open. (A Claude Code team member's point, quoted in the article: "one-shot" posts usually hide a prompt of ~10k characters with good takes, skills, examples and API keys.)

Answer first: What is the product? What's the one thing the viewer remembers? Which reference may influence the work? Which elements must come from the real product? What would make it unacceptable?

```text
FILM
One sentence: [the idea the viewer should remember]
Audience: [who this is for]
Duration: [seconds]
Formats: [16:9 / 9:16 / 1:1]

ASSETS
Real logo: [path]
Real UI screenshots: [paths]
Brand type and colors: [tokens]
Music or audio reference: [path]

VISUAL RULES
Keep: [specific traits from the reference]
Avoid: [specific visual cliches]
Never invent product screens or metrics

DELIVERABLES
Storyboard, contact sheet, final video, poster frame, source files
```

This separates **facts about the product** from **choices about the film**. The model may invent camera moves; it may not invent your dashboard or quietly replace your logo.

## 2. Give it a reference it can inspect

Without a visual grammar the model supplies its own. Give it a frame, a short film or a folder of past work, and make it **write down what it learned**:

```text
REFERENCE ANALYSIS
Palette: [actual colors, not "premium"]
Typography: [family, width, weight, scale]
Composition: [where the eye goes first]
Pacing: [average time between meaningful changes]
Motion: [snap, glide, overshoot, cut, hold]
Texture: [grain, paper, glass, none]

DO NOT COPY
Subjects, logos, copy, or product-specific imagery
```

The output is a **style guide**, not a collage of borrowed shots. For a product film, have the agent collect the exact screens from the real site and **review that asset list before production**. If an asset is missing, it must stop and ask, not draw a convincing fake.

## 3. Turn the story into states and beats

A list of effects ("zoom, morph, particles") describes activity, not meaning. State what the viewer knows at each moment:

```text
00-02s  HOOK     One image that earns attention
02-05s  PROBLEM  Show the friction, not a paragraph about it
05-09s  REVEAL   The product enters through a real interaction
09-13s  PROOF    One screen or number demonstrates the claim
13-16s  CLOSE    A clean final state and a readable CTA
```

Each beat needs an **entry state, an exit state and a reason to exist**. For UI motion, list the states first (`SEARCH -> RESULT -> DETAIL -> ACTION -> CONFIRMATION`) so the model designs continuity between them: one component can change size, colour, content and position yet stay the same object. The shot list is a contract: if the agent can't explain why shot four exists, cut it.

## 4. Choose the renderer on purpose

- **Small, one-off piece:** a lightweight Canvas or SVG project is enough.
- **Repeatable series:** a framework keeps scene structure, media placement and export maintainable.
  - [Remotion](https://github.com/remotion-dev/remotion): video as React components rendered at known frame numbers (custom licence; check its terms for your use).
  - [HyperFrames](https://github.com/heygen-com/hyperframes): editable HTML composition with explicit timing and seekable animation runtimes (Apache-2.0).
- Neither is automatically better; use the smallest system that supports a film you'll make again.

**Non-negotiable: seekability.** Frame 240 must render directly without replaying frames 0-239. That means no hidden clock, no unseeded randomness, and no animation that only works after the browser has run for eight seconds.

```text
frame = render(time, shot_list, assets, style_tokens, seed)
```

## 5. Make motion have weight

Good motion communicates mass, hierarchy and intent. Springs describe this better than generic ease-in-out, but if everything overshoots, nothing feels precise. Write a rule per object class:

| Object | Motion |
|---|---|
| Micro UI | quick, minimal overshoot |
| Panels | controlled settle |
| Camera | smooth, almost invisible |
| Headlines | strong entrance, stable hold (long enough to read) |
| Mascot | playful, clearly intentional |

Check: after each move, does the viewer know where to look? If not, it's decoration competing with the message.

## 6. Put sound on the same timeline

Many AI films look finished muted; with sound, nothing connects (the click lands after the button, the cut misses the beat, the logo arrives before the music resolves). Treat sound as a **timeline input**:

```text
BEAT GRID
0.00s opening hit · 0.50s first state change · 1.00s product reveal · 1.50s interaction click · 2.00s visual payoff
```

Use a licensed or original track, measure its beats and cut against them. For synthesized sound, place every cue on the same timestamps that drive the picture. **Test:** close your eyes; if the audio has no shape without the picture, it isn't finished.

## 7. Inspect frames before exporting the film

Don't watch a full 60-second export ten times. Ask for a **contact sheet** (one frame at each major beat, plus a short strip around the fastest transitions), then check:

- [ ] Text readable at phone size
- [ ] No element crossing the safe area
- [ ] Real product assets, not invented replacements
- [ ] Consistent type and colour across scenes
- [ ] No awkward mid-transition frames
- [ ] Cuts and sound cues land together
- [ ] First two seconds contain a real hook
- [ ] Last frame is strong enough to be a poster

Then give the model the contact sheet and a critique task:

```text
Do not describe what you intended to make. Judge only the rendered frames.
Identify the three largest defects. Give each a timestamp, evidence, and a local fix.
Patch only those sections, then render the affected frames again.
```

"The agent made a video" stops when the file exists. "The agent directed a video" stops when the evidence says the film works.

## 8. Export variants from the source, not from a crop

A 16:9 launch film and a 9:16 social cut are different compositions (larger type, fewer simultaneous elements, a different camera path, a tighter story). Keep the same assets, timeline and narrative states, and define layout per format:

| Format | Layout |
|---|---|
| 16:9 | more spatial context |
| 9:16 | fewer elements, stronger vertical hierarchy |
| 1:1 | tighter typography, shorter holds |

Render a contact sheet for every variant. An export is correct when the composition survives the format change, not when the encoder finishes.

## 9. Package the studio, not the chat

If the only record is a conversation, you have a lucky session, not a system. Keep decisions in files a later run can read:

```text
motion-studio/
  brief.md        one-sentence goal and product facts
  style-guide.md  palette, type, motion, banned defaults
  shotlist.md     beats, states, timestamps, purpose
  assets/         approved logos, screens, footage, sound
  src/            seekable composition and motion code
  reviews/        contact sheets and defect notes
  out/            exports per format
```

Next video: swap the brief and assets; keep the render contract, review checklist and delivery structure. The agent can resume from a completed gate and say which artifact is missing; it shouldn't claim "done" because the last command exited 0.

## 10. Give long runs gates, not freedom

```text
GATE 1  Approve references and product assets
GATE 2  Approve style guide and shot list
GATE 3  Inspect representative stills
GATE 4  Render rough cut and contact sheet
GATE 5  Repair the three highest-impact defects
GATE 6  Check audio, formats, and final deliverables
```

The agent can work for hours between gates but should not make irreversible brand decisions. A missing interface screenshot is a **blocker, not an invitation to hallucinate one**. If the reference is unclear, output a question or a small test frame, not 900 polished wrong frames. The loop needs a target, an observation, a bounded repair and a way to stop.

---

## The prompt to give the model

```text
You are directing and engineering a code-rendered motion film.

Goal:
Make a [duration]-second film for [product/audience].
The viewer should remember: [one sentence].

Inputs:
- Use only the supplied product assets and approved copy
- Inspect the reference files and write a style-guide.md
- Write shotlist.md with timestamps, entry states, exit states, and purpose

Build:
- Choose a renderer and explain why it fits this project
- Make every frame seekable and deterministic
- Keep motion, audio cues, and transitions on one timeline
- Preserve editable source and a repeatable render command

Review gates:
1. Show the style guide and shot list before building
2. Show a contact sheet before the full render
3. Score hook, readability, continuity, motion, and sound sync
4. Fix the three worst defects and re-render those sections
5. Export 16:9 and 9:16 as separate compositions

Deliver:
final videos, poster frames, contact sheets, source, assets list,
and a short note on what still needs human review.
```

It's long on purpose: it gives the model a sequence of decisions, artifacts and stop conditions you can reuse for the next launch.

## Caveats

- **Model details:** the article says Opus 5.5 was released on 22 September and "performs at the level of Fable 5.1 for most tasks at 40% less cost than Opus 5". That's the author's quote of an announcement; I didn't verify it. The workflow doesn't depend on a specific model.
- **Method, not magic:** it takes real setup (assets, references, review). It's slower than a one-shot prompt and produces better, repeatable results.
- **Licensing:** check Remotion's licence terms for commercial use, and clear the rights to any music or reference material you use.
- **Cost:** long agent runs use a lot of model usage; the gates keep it from burning tokens on wrong frames.
