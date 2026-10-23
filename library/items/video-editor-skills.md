---
name: Video Editor Skills (DaVinci Resolve)
url: https://github.com/appariciojunior/video-editor-skills
local: -
summary: 12 Claude Code skills that make Claude a first-pass editor for YouTube vlogs/classes in DaVinci Resolve Studio (transcript cuts, pacing, B-roll, music, captions, Remotion overlays, export).
type: [skill-pack, plugin, github-repo]
stage: [20-content-production, 04-assets]
task: [video-editing, rough-cut, pacing, b-roll, captioning, audio-mixing, music-scoring, sound-design, motion-graphics, video-export, automation]
content: [video, audio, text]
content-format: [vlog, tutorial-class, talking-head, long-form-video]
agent: [claude-code]
software: [davinci-resolve, ffmpeg, remotion, figma, epidemic-sound]
channel: [youtube]
cost: free-needs-paid-deps
license: cc-by-nc-4.0
commercial-use: no
requires: [paid-software, paid-api, api-key, local-install, python, node]
level: advanced
source: community
maturity: new
verified: yes
stars: 4
last_push: 2026-10-23
added: 2026-10-23
related: [claude-head-of-content-trends]
---

## What it is

A skills-only package with **no code**: method, numbers, rules and traps learned on real edits. Claude builds the small scripts together with you, for your setup. You film and make the taste calls; Claude imports, cuts, scores, captions and helps you export.

| Skill | Teaches Claude |
|---|---|
| `video-editor-setup` | Workspace, safe key handling, Resolve template, which scripts to build |
| `edit-video` | One-command flow: ingest → cut → build in Resolve → report |
| `rough-cut` | What to keep: retakes, false starts, punchlines |
| `vlog-pacing` | Silence detection, pads, pause rules, jump-cut zoom |
| `broll` | Finding and cutting B-roll by action and story |
| `resolve-scripting` | What works in the Resolve API, what silently fails, what crashes it |
| `voice-and-audio` | Loudness normalisation, diagnosing a muffled voice, EQ recipe |
| `music-and-sound` | Epidemic Sound cues per section, ducking, restrained SFX |
| `captions` | Clean, correct, one-line captions |
| `motion-overlays` | Remotion brand kit timed to your words, kept clear of the face and captions |
| `figma-roundtrip` | Design the kit in Figma and keep code and boards in sync |
| `youtube-export` | Deliver settings for high quality without huge files |

The repo also includes `templates/config.example.json` (starting values) and `LEARNINGS.md`, a set of hard-won rules. Two examples:
- Cut from transcript words, not from volume. That gave 120 pieces instead of about 800.
- Pause settings differ by format: a class works at 0.5 s max pause / 0.3 s kept, a vlog at 1.0 / 0.6.

## Install

```bash
/plugin install https://github.com/appariciojunior/video-editor-skills
# or
cp -R skills/* ~/.claude/skills/
```

Then say **"set up my video editor"**. When the workspace is ready, drop footage in `raw video/` and say **"edit the new video"**.

## Requirements and costs

- **DaVinci Resolve Studio (paid).** The free version of Resolve has no external scripting.
- **A speech-to-text API with word timestamps (usually paid).** The author used ElevenLabs Scribe; any per-word-timing service works.
- **Free tools:** ffmpeg, Python 3.9+, and Node 18+ (Node only for motion graphics).
- **Optional:** Epidemic Sound MCP (paid subscription), Figma MCP, Remotion.

## Caveats

- **Licence: CC BY-NC 4.0. No commercial use.** You can't use it in client work, paid courses or anything sold without asking the author. GitHub shows the license as "NOASSERTION", but `plugin.json` and the README both say CC-BY-NC-4.0.
- **Very new:** created 2026-10-23, 4★, a single author. There's no track record yet.
- **Safety:** raw footage stays read-only, Resolve gets additive changes only, and keys are never printed. These are design rules written into the skills, not enforced by code.
