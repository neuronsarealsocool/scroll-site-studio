---
name: scroll-site-studio
description: Build or extend responsive scroll-driven websites, cinematic video walkthroughs, and layered editorial landing pages. Includes reusable templates, media preparation, provider workflows, and desktop/mobile verification for Codex or Claude. Use for a scroll website or a maintained library of scroll templates; ordinary static pages do not require this skill.
metadata:
  version: 0.1.0
---

# Scroll Site Studio

Build a working website from the user's brief, existing assets and chosen platform.
Use this folder as the skill root, regardless of which agent loaded it. Instructions
and assets are portable; host-specific tools and paid accounts are not bundled.

## Choose the work, then the references

- **Continuous camera journey:** read `references/walkthrough.md`, then the bundled
  `vendor/scroll-world/SKILL.md` and relevant prompt/pipeline references.
- **Varied editorial or layered website:** read `vendor/scroll-craft/SKILL.md` and
  its relevant design references. Its complete engine and tools are included.
  Treat its stylistic rules as a starting point; the user's branding and scope win.
- **Existing hero only:** use `references/integration.md`; retain the existing page,
  navigation, text and backend. Do not replace a whole website to add a film.
- **New generated media:** read `vendor/replicate-media/SKILL.md` and
  `references/media.md`. Use the user's provider/model. Replicate is the default
  here; the upstream Scroll Craft KIE helper is an alternative only when chosen.
  Do not require both accounts.
- **Publishing:** read `references/publishing.md`. Sites is optional, never assumed
  available in Claude or a plain Codex installation.
- **Extending this library:** read `references/maintaining.md`.

Do not load all vendor references for a small task. These main instructions resolve
integration choices across the bundled skills. Preserve upstream licenses.

## Establish only the missing decisions

Reuse answers already provided. Establish purpose, brand, assets, visitor's next
action, continuous versus chaptered motion, mobile treatment and publication target.
For an architectural journey agree a proposed route/floorplan before inventing
connected rooms; reference photos do not establish unseen geometry.

Choose ordinary implementation details autonomously. Installing a skill, preparing
a template or inspecting a model does not authorize paid generation. Before spending,
record model, verified schema, count, duration, resolution, stills, current price
estimate and total/retry allowance. Honour any review-before-publication gate.
Plan approval is not approval of unseen footage.

## Prepare

1. Run `python scripts/doctor.py` from this skill directory. It is local and read-only.
   Python 3.10+ is the bootstrap requirement; `python3` may be the command name.
2. Run `python scripts/setup.py --plan` for missing dependency installation commands.
   `--install ffmpeg` installs FFmpeg and ffprobe through the host's package manager;
   run only within an authorized setup task. No binaries, accounts or keys are hidden
   in this package. Node is needed for Scroll Craft, not the vanilla starter.
3. Read `catalog.json`. Select a template by fit, not by whichever was last used.
   `python scripts/catalog.py init <id> --dest <new-directory>` copies a complete
   standalone starter. It refuses an existing destination.
4. For a live-site edit, open its source using the actual hosting workflow before
   edits. Keep generated work and credentials outside public roots.

## Build and prepare media

Use supplied/licensed footage where it fits. Create destination references before
buying a long generated chain. Continue from each previous clip's actual decoded
last frame, and supply a destination frame where supported. Inspect each leg before
generating the next. Conditioning does not prove identical rooms. Keep successful
outputs, prediction IDs and non-secret manifests. Never blindly repeat an uncertain
paid submission.

Keep desktop and portrait media explicitly paired. A crop is not a separately
generated portrait. `python scripts/media.py encode input.mp4 output.mp4 --mobile`
keeps dimensions and uses H.264, yuv420p, short GOP and faststart, without audio.
`probe`, `frames`, `demo` and `smoke` support inspection and offline testing.
Do not upscale and call it native resolution. Read media.py help for arguments.

For the bounded starter edit semantic `.flight-scene` markup and matching sources.
Its engine derives timing from scene count, holds the actual final still, and
releases into normal content. Read its TEMPLATE.md before using it.

## Verify and deliver

Use the host's supported browser tools. If it only permits its own browser API,
adapt the checks instead of running an independent automation harness. Where allowed,
Scroll Craft's supplied harness adds frame/contrast checks. Read
`references/verification.md` for the acceptance matrix and limits.

Verify forward/reverse seeks at every boundary, loading posters, text contrast,
mobile selection, tail hold, release, footer and keyboard access. Test reduced
motion and failure when supported. A desktop viewport is not a real-phone test.
State checks actually run. Build/typecheck the chosen framework; a static starter
needs no framework installation.

Respect publication scope and review gates. Reuse an existing site and audience;
do not create duplicates or broaden access implicitly. Return a verified deployed
URL or local files and an honest verification summary. Do not claim production
completeness for unconnected forms, placeholders or unverified device behaviour.
Skill creation itself never deploys a site.
