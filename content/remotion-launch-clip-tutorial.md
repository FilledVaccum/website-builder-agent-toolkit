# Motion engineering with Claude Opus 5.5: build a 20-second launch clip in Remotion

A hands-on companion to the [code-rendered video studio](code-rendered-video-studio.md) workflow. You build **one 20-second, 1080×1080 product launch clip** (a feature demo where a cursor presses *Export* and a finished file appears), driven by a frame-by-frame brief. Adapted from a creator's X article. **Left out:** the article's closing business section (a $150 "Launch Clip" package, offer wording and how to sell it), per this repo's free-only rule. Model claims in the article (Opus 5.5 release, "40% cheaper than Opus 5") are the author's quote and weren't verified.

- **Tools:** Node.js, Claude Code, FFmpeg/FFprobe, [Remotion](https://github.com/remotion-dev/remotion) (custom licence; check its terms for commercial use).
- **Core move:** tell the model *when* the card lands, *when* the product responds and *how long* the headline stays readable, in **frame numbers** so each can be edited separately.

## 1. Give the reference a job

Pick a reference video for **one thing** to learn: a card entrance with a controlled landing, a transition that keeps the product in view, or a cursor action that makes the result obvious. Follow the main object from first position to landing and note what the movement reveals; mark when text becomes readable and when the next event pulls attention away. You're collecting *decisions* to reuse with your own logo, copy and product screen, not shots to copy.

Questions to answer from the reference: how the shot introduces the product · what moves first · where the eye should land · how much time the result gets.

**Prompt (with `reference.mp4` in the project):**

```text
Analyze the main product reveal in reference.mp4.
First report its dimensions, frame rate, and duration using available tools.
Extract overview images, then consecutive frames around the entrance and landing.
Inspect the extracted images with image tools.

Save REFERENCE.md with:
Source timestamps and frame numbers for entrance, landing, hold, and cut.
Object bounding boxes at start and landing, in source-image coordinates.
Movement direction, duration, scale change, opacity change, and visible overshoot.
The order in which product, headline, and supporting labels appear.
The readable hold and the state carried into the next shot.

Label measured values, visual estimates, and proposed creative choices separately.
For an uncertain value, identify the frames needed to check it.

Use our assets to propose one original export-demonstration shot.
Specify its layout, focal point, entrance, product response, and reading hold.
List missing assets and questions requiring approval.
Return this shot plan before implementation.
```

- **Verify positions yourself:** a model's spatial estimates from images are approximate; check important positions against the extracted frames.
- **Sample the reference:** 2 images/second for an overview, then consecutive frames around key events.
- **Typeface:** use an available font and adapt the reference's size *relationships* to your own words.
- **Frame rates:** keep reference timestamps labeled with the source frame rate. A half-second move is 15 frames at 30 fps but 30 frames at 60 fps.

## 2. Write the shot as an event

Give the viewer something to follow: starting state → cursor on the action → press registers → result appears → hold long enough to read the filename.

| Time | Frame (30 fps) | Event |
|---|---|---|
| 4.0 s | 120 | Report visible, card settled |
| 5.0 s | 150 | Cursor approaches *Export* |
| 6.0 s | 180 | Cursor reaches the button |
| 6.5 s | 195 | Press registers |
| 7.0 s | 210 | Finished file appears |
| 7.8 s | 234 | Result label fully readable |
| 14.0 s | 420 | Closing shot begins |

Use these for the first preview, then adjust any interval that feels rushed or empty.

## 3. The brief: five decisions in `BRIEF.md`

Replace bracketed fields with real assets and copy. Coordinates, colours and timing are **starting choices** to review against your own screens.

```text
GOAL
Demonstrate how [product] exports a finished report.
Viewer: [who uses this feature].
Opening copy: [outcome, maximum eight words].
Closing copy: [one next action and destination].

DELIVERY AND ASSETS
Composition: Launch, 1080 by 1080, 30 fps, 600 frames.
All timeline numbers below are global, inclusive frame numbers.
Assets under public/: [logo], [report screen], [exported-file screen], [font], [audio].
Inspect asset dimensions and font loading before implementation.
Request missing screens or illegible crops before proceeding.

LAYOUT
Coordinates use the canvas top-left as origin; units are pixels.
Background #101318, primary text #F5F7FA, accent #8AD8B0.
Keep essential content inside a 64-pixel outer margin.
Headline box: x96, y112, width 888; 64-pixel font, 1.1 line height, maximum two lines.
Product card: x120, y350, width 840, height 480, corner radius 24.
Fit the supplied screen while keeping the export control readable.
Record button and result anchors from the fitted screen.
Layer order: background, card, product content, cursor, headline.

OPENING: FRAMES 0 THROUGH 119
Headline enters during 0 through 18: vertical offset 24 to 0, opacity 0 to 1.
Card enters during 18 through 42: vertical offset 60 to 0, opacity 0 to 1.
Use cubic ease-out with clamped endpoints for both entrances.
Hold the settled layout during 42 through 119.

PRODUCT: FRAMES 120 THROUGH 419
Carry the card into frame 120 at its exact settled position and scale.
Move the cursor to the measured button anchor during 150 through 180.
Choose a path clear of text and record its waypoints.
Press at 195; animate the cursor scale 1 at 192, to 0.92 at 195, back to 1 at 201.
Show the button response at 195 using supplied assets or an approved accent overlay.
Move the cursor toward a clear resting point during 204 through 222.
Show the supplied exported-file state at 210; finish its reveal by 234.
Keep the result readable and stationary through 419.

CLOSING: FRAMES 420 THROUGH 599
Cut to the supplied logo and closing copy at 420.
Fade the closing copy in during 420 through 438; hold through 599.

IMPLEMENTATION AND REVIEW
Drive animated values from useCurrentFrame; expose timing and layout constants.
Use fixed seeds for any variation; keep the camera stationary for this pass.
If audio is supplied, align its audible click with 195 and reveal hit with 210.
First build the opening and render frames 0, 18, 42, 60, 119 plus its moving preview.
Check text wrapping, margins, screen readability, and settled positions.
Report changed files, outputs, and unresolved issues; wait for feedback.
After approval, build the remaining scenes and inspect frames 120, 195, 234, 419, 420, 540, 599.
```

Use a short opening line and let the product demo carry the explanation; move anything needing several sentences to its own scene.

**Check the longest copy.** Test the opening with the longest headline you expect to reuse. If it wraps to three lines, pause the motion pass: shorten the copy, widen the box, or move supporting info to another shot. Record the layout limits (headline width, max lines, logo space, final positions) with the styling, check the actual rendered font, and re-render the landing frame whenever the headline changes. Apply the same check to the closing action, especially when swapping in a longer product name.

## 4. Make every frame reproducible (Remotion)

```text
FRAME NUMBER -> element position -> scale and opacity -> visible product state -> text and cursor state
```

- Drive movement from `useCurrentFrame()` with interpolation or `spring()`. Avoid independent CSS transitions, which can flicker in rendered frames.
- Derive any randomness from a **fixed seed** so a chosen frame stays consistent.
- Write timing in seconds first, then convert (0.6 s = 18 frames at 30 fps). Store entrance offset, destination, duration and landing settings together so a revision touches one set of values.

## 5. Give motion a purpose

| Motion | Job |
|---|---|
| Entrance | Introduce the main object |
| Hold | Leave time to read and understand |
| Cursor movement | Identify the next action |
| Transition | Carry the viewer into the next state |

- Tune the card's approach with `spring()` duration/damping/stiffness/overshoot; keep the destination fixed and change **one** parameter at a time.
- Start with the main object, then bring in supporting info after a small delay (e.g. 0.1 s between headline and label).
- For a subtle push, specify scale 1.00 → 1.03 over three seconds; remember constant percentage changes compound across frames.
- During a reading hold, keep supporting movement quiet.

**Decide what owns the screen:** attention stays on the button until its response appears, then the result owns the reading window. If the cursor crosses a headline during a card entrance, delay one event or change the path. Count the reading window from when words become legible: an 8-frame hold at 30 fps is only ~0.27 s. Play at normal speed and read aloud; extend any hold that ends before you finish. Check interface labels at phone size.

**Motion blur:** decide what it should contribute to a specific fast move (e.g. only on the card entrance, settling with the movement), then inspect rendered states for smeared text and persistent trails.

## 6. Three stills direct the next pass

Render an opening frame, a product-result frame and the closing card, and judge the message and composition before adding movement detail: Is the main text readable? Is the product result visible? Is anything cropped or overlapping? Does the closing action have room?

```bash
npx remotion still Launch out/opening.png --frame=60
npx remotion still Launch out/product.png --frame=240   # change if your result lands elsewhere
npx remotion still Launch out/closing.png --frame=540
```

Then render the interval around a scene boundary and watch how attention transfers:

```bash
npx remotion render Launch out/transition.mp4 --frames=90-149 --codec=h264
```

(At 30 fps that's the end of the opening and the start of the product scene.)

## 7. Corrections the agent can execute

Use four fields: **location, observed problem, change, what stays fixed.**

```text
Revise the Launch composition using BRIEF.md.
Observed defect: the cursor overlaps the result label at global frame 210.

Change only the cursor's post-press path:
Start the departure at 204 and reach its resting point by 210.
Choose the resting point inside the card, with 24 pixels of clearance from the result label.
Use a path that stays clear of the label throughout the move.
Preserve the press at 195, reveal at 210, card geometry, copy, and audio cues.
Hold the cursor at its destination through 419.

Render stills at 195, 210, 222, 240 and a preview of 180 through 249.
Check intermediate frames for overlap and jumps.
Report the changed path coordinates and output filenames for review.
```

- **Fix in this order:** missing information and unreadable text, then timing, then visual detail.
- **Independent critique:** open another session with the brief, images and extracted frames; review up to five frame-specific corrections; send accepted edits to the builder.
- **Repair loop stays local:** observed defect → one scoped edit → affected frames → surrounding scene boundary → normal-speed playback.
- **Frame labels:** state global vs scene-local frames explicitly (local frame 30 in a sequence starting at global frame 120 = global 150).

## 8. Sound has an event frame

Place the click on the visible press and the strongest reveal hit on the visual reveal. A soft lead-in or silence can shift a sound's audible hit away from the start of the file: find the hit in the waveform and playback, then offset the clip.

```text
BUTTON PRESS    frame 195    click transient
RESULT REVEAL   frame 210    reveal accent
CLOSING HOLD    frame 438    music settles
```

Keep sounds and music on separate tracks with adjustable placement and volume. Check the loudest event, the quietest useful cue and the ending on headphones **and** a phone speaker.

## 9. Setup

Install Node.js, Claude Code, FFmpeg and FFprobe first, then:

```bash
npx create-video --yes --blank launch-video
cd launch-video
npx skills add remotion-dev/skills     # Remotion's documented install for agent skills (see note below)
npm run dev
```

Start the model in a second terminal inside `launch-video`:

```bash
claude --model claude-opus-5-5
```

Put product assets under `public/`, the reference at `reference.mp4`, the brief at `BRIEF.md`; create `frames/` (reference images) and `out/` (previews). Extract the reference overview:

```bash
ffmpeg -i reference.mp4 -vf "fps=2,scale=960:-2" frames/ref-%04d.jpg
```

**Note on the skills command:** the article uses `npx remotion skills add`. Remotion's docs (checked 2026-10-24) document `npx skills add remotion-dev/skills` (repo [remotion-dev/skills](https://github.com/remotion-dev/skills), 5.6k★), and also offer skills during project creation. Use whichever works in your version.

**First build prompt (after saving the brief):**

```text
Read BRIEF.md and the installed Remotion guidance.
Inspect public/ and confirm that the required assets are available.
Summarize the opening's layout, event frames, and animation curves.
Flag any conflicting requirements or missing inputs before implementation.
Implement only the first review stage specified in BRIEF.md.
Return the stills, moving preview, changed files, and checks performed.
Wait for approval before continuing.
```

Inspect the opening still before asking for the remaining scenes, using the commands above for each new scene.

## 10. Export what you approved

```bash
npx remotion render Launch out/launch.mp4 --codec=h264
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,duration -of json out/launch.mp4
```

Expect 1080×1080, frame rate `30/1`, about 20 seconds. Watch the exported file at normal speed (first message, product action, ending). Keep the approved render with its brief, scene timing and audio cue list.

## 11. Longer films need scene boundaries

- Give each scene an **incoming and outgoing state**; for a continuous transition, use the card's ending position, scale and highlighted field as the next scene's start.
- Keep fonts, palette, spacing and recurring elements in shared settings; record deliberate exceptions.
- Work on one scene (or a small related group), each with its assets, purpose and boundary states.
- If transitions overlap scenes, subtract the overlap from total duration.
- After a local edit, inspect **both neighbouring boundaries** before watching the whole film.
- Save accepted entrance, cursor and text components for the next project; re-review timing when assets or copy change.

## Caveats

- **Rights:** use your own assets, or a product whose owner has agreed to the demo. Clear rights to any audio and reference footage; don't copy a reference's subjects, logos or copy.
- **Licence:** Remotion has a custom licence; check it before commercial use.
- **Approximate vision:** a model's measurements from frames are estimates; verify against extracted images.
- **Cost:** long agent sessions use a lot of model usage; the staged approvals limit wasted renders.
- **Commands:** `npx remotion` flags and the skills installer change between versions; check the current Remotion docs if something fails.
