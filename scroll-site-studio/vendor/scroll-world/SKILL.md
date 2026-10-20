---
name: scroll-world
description: >
  Build a scroll-controlled cinematic landing page or replace an existing hero with
  a camera flight through connected scenes. Use for scroll-scrubbed walkthroughs,
  architectural fly-throughs, and miniature or diorama worlds. Generate media through
  the replicate-media skill and reuse a portable vanilla JavaScript scroll engine.
  Does not apply to ordinary carousels or simple scroll-reveal effects.
license: MIT
metadata:
  upstream: https://github.com/oso95/scroll-world
  upstream_commit: 71cc36d3bb150248ae36a2c552f9cbf88802a79c
  adaptation: Codex with Replicate media generation
---

# Scroll world for Codex + Replicate

Build a pre-rendered camera journey whose video time follows scroll position in
both directions. The browser scrubs video; it does not reconstruct a 3D building.
Use the existing `$replicate-media` skill for media generation, authentication,
model discovery, prediction lifecycle, and output storage. Resolve its SKILL.md
from the current skill catalog (installed alongside this skill in this setup).
This adaptation uses Replicate; do not install, authenticate, or fall back to
Higgsfield or Monid unless the user specifically requests that provider.

The upstream engine, page template, and optional knockout helper are retained.
The generation guides below replace the upstream provider-specific commands.
Before updating this skill from upstream, preserve these local adaptations.

## 0. Bootstrap

- Load `replicate-media`. Prefer its connected Replicate tools if available;
  otherwise use its HTTP workflow with `REPLICATE_API_TOKEN`. Never print the
  token, put it in a command argument, or save it in project files.
- Run `python scripts/replicate_preflight.py` using an absolute script path.
  It only performs metadata GETs and local checks: no upload or prediction.
  It reports model input fields and whether ffmpeg/ffprobe are on PATH.
  `--save-schema <path>` optionally saves the full public model schema for
  local validation. It does not establish available credit or video quality.
- Locate ffmpeg and ffprobe before generating a chain. Existing absolute paths
  are fine; no global PATH change is required. If missing, explain the concrete
  prerequisite and arrange installation within the user's setup scope.
- Python is needed for preflight and the optional Pillow background knockout;
  the browser engine itself has no Python or framework dependency.
- Creating, installing, or adapting the skill does not authorize paid renders.

## 1. Establish the brief

Use the conversation and supplied site/assets first. Ask only for material
missing information: subject, branding, art direction, route, intended devices,
and generation budget. Inspect every relevant reference image before describing
rooms or materials. Preserve existing imagery and copy for a hero replacement.
An architectural route needs an agreed layout; reference photos alone cannot
establish where the rooms physically connect.

Choose the camera architecture by the desired experience:

- **A: continuous walkthrough** for photoreal architecture/hospitality. One
  forward journey, N sequential legs, no extra connector clips. For the Vesper
  style use this, with each destination pinned to the approved room render.
- **B: miniature world** for dioramas. N dive clips plus N-1 aerial connectors.
  Pulling back and rising between scenes is intentional in this style.
- **Locked isometric glide** uses A with a fixed camera angle throughout.

Agree on whether phones receive responsive landscape framing, a static/light
fallback, or a separately generated native 9:16 chain. A native portrait chain
adds generation cost; never generate it silently or present a crop as native.

Before spending, state the selected model, exact clip count/durations, resolution,
stills count, expected cost from current Replicate pricing, and any retry allowance.
Architecture A needs N videos; B needs 2N-1. Do not reuse other providers' credit
prices or assume API metadata includes a balance or price. If pricing is unavailable,
say so. Propose a two-adjacent-clip qualification test for a new model/provider;
it requires generation authorization and counts toward the agreed budget.

## 2. Stills and prompts

Reuse approved site assets when supplied; do not regenerate them merely to use a
particular image model. For new stills, use `replicate-media` with a currently
verified image/reference model. Use built-in image generation only if requested
or accepted as the stills source. Keep one shared design/lighting preamble and
concrete material references across images. Review cohesion before video.

Read [prompts.md](references/prompts.md) for architectural, miniature, and motion
templates. Use supported model reference inputs for consistency; do not assume
all models can combine reference arrays with first/last frames.

## 3. Replicate generation and seam handoffs

Read [pipeline.md](references/pipeline.md) before API calls. Inspect the current
live schema before each build; these verified field names are starting points:

| Replicate model | First frame | Last frame | Quality | Silent video |
|---|---|---|---|---|
| `bytedance/seedance-2.0` | `image` | `last_frame_image` | `resolution` | `generate_audio: false` |
| `kwaivgi/kling-v3-video` | `start_image` | `end_image` | `mode` | `generate_audio: false` |

Keep one model across the chain where practical. Honor a chosen model if its
current endpoint supports the required frame controls. Do not silently substitute
a text-to-video or reference-only endpoint. The preflight script resolves schema
references and checks required fields, enum values, and proposed duration.

**A:** First leg starts from the hero image. Each later leg starts from the
previous leg's actual final decoded frame. For architecture fidelity, supply the
approved destination room as the end image, with a plausible forward viewpoint.
Do not pin to a wide backward-looking view that forces a pullback. Inspect each
leg's final frame and motion before starting the next. The final second should
settle into the same slow forward drift as the next leg's opening.

**B:** Generate dives, extract actual boundary frames, then connect dive i's
last frame to dive i+1's first frame. Connector endpoints must come from the
rendered clips, not independent source stills.

Conditioning is not proof of pixel-identical output. Check actual results for
composition and velocity continuity; use a short crossfade only for residual
detail drift. Preserve first/last frames for every raw and encoded clip. If a
middle leg is redone, target the next leg's existing first frame to protect the
remaining chain. Keep completed work; never restart an entire chain automatically.

Submit through `replicate-media`, record the prediction ID immediately, poll the
same job in short intervals, and save successful files promptly. Do not repeat an
uncertain POST or automatically buy retries outside the agreed scope. Stop on
auth/billing errors. Treat a timeout as a reason to retrieve status, not resubmit.

## 4. Encode and assemble

Read [pipeline.md](references/pipeline.md) for boundary extraction, encoding,
request mapping, and run records. Keep native dimensions, H.264 yuv420p, CRF about
20, GOP 8, faststart, no audio. Extract posters from each delivered clip's first
frame. Keep raw originals. Never upscale a lower-resolution response and call it
native 1080p. Generate mobile portrait media only within the agreed scope.

Copy [scrub-engine.js](references/scrub-engine.js) into the project. It is vanilla
JS with blob-backed seeking, prefetch, short seam crossfades, reduced-motion
fallback, and mobile seek coalescing. Its header documents configuration.
Use [index-template.html](references/index-template.html) only for a full-page
world; replace all sample content and omit absent mobile/connector URLs.

For A set `connectors: []`; for B provide N-1 ordered connector slots. Each
`sections` entry has `id`, `label`, `still` (first-frame poster), and `clip`.
Optional `stillMobile`/`clipMobile` must correspond to the mobile film. More
`scroll` means more dwell; use `linger` sparingly so seam velocity stays natural.

**Existing hero replacement:** Read [hero-integration.md](references/hero-integration.md).
The upstream engine owns fixed viewport layers and global CSS; it must be scoped
and released to preserve the rest of a marketing page. Keep existing wordmark,
headline, rating, booking form, and navigation rather than inventing replacements.

## 5. Verify and deliver

Use a real, active browser tab. Check scroll-driven currentTime, every seam in
both directions, correct posters during loading, reduced-motion fallback, mobile
layout, loading errors, and console output. For a hero replacement verify overlay
fade-out/fade-in, held tail frame, release dissolve without a black interval, and
that the normal page and footer remain reachable. Do not assume an embedded
preview with throttled animation frames demonstrates a broken engine.

Report what was actually tested, unresolved quality issues, and actual generation
cost when known. Never equate schema validation with successful rendering or
seam qualification. Keep non-secret model/version/settings/prediction records.
Explain whether booking is a quote calculator or a real connected reservation flow.

## Supporting resources

- [prompts.md](references/prompts.md): consistent art and camera instructions.
- [pipeline.md](references/pipeline.md): Replicate API workflow and local encoding.
- [hero-integration.md](references/hero-integration.md): existing-page integration.
- `scripts/replicate_preflight.py`: read-only schema/dependency checks; `--help`.
- `references/knockout.py`: optional background removal for flat dioramas; requires Pillow.
