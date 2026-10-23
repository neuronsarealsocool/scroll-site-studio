---
name: scroll-site-studio
description: Create or refine high-end responsive websites in Codex or Claude using supplied templates, prompts, assets and design references. Supports static, editorial, interactive and scroll-driven sites, exact reuse or adaptation, Replicate media generation, in-chat media approval and a growing template library.
metadata:
  version: 0.2.4
---

# Scroll Site Studio

Build a high-end website from the user's brief, existing assets and chosen platform.
All reference packs are platform-neutral design sources. Use the existing project
stack or a suitable frontend for the brief; WordPress/WooCommerce are optional and
require the user to request or agree to that platform. Source themes and prompts
do not select the build stack, including in verbatim mode. Read the platform rule
in `references/creative-direction.md` before using a pack.
The skill name is retained for compatibility; scroll effects are optional. Choose
motion only when it helps the design and visitor's task. A static site can be the
right finished result. Do not add video, pinning or a cinematic journey by default.
Use this folder as the skill root, regardless of which agent loaded it. Instructions
and assets are portable; host-specific tools and paid accounts are not bundled.

## Choose the work, then the references

- **Every website:** read `references/creative-direction.md`. Establish whether the
  user wants exact reuse, adaptation or a mix. Use their supplied templates, prompts,
  assets and references, including uploads added later. Do not force originality
  rules or a fixed aesthetic over a request to reproduce a template faithfully.
- **Continuous camera journey:** read `references/walkthrough.md`, then the bundled
  `vendor/scroll-world/SKILL.md` and relevant prompt/pipeline references.
- **Varied editorial or layered website:** read `vendor/scroll-craft/SKILL.md` and
  its relevant design references. Its complete engine and tools are included.
  Its stylistic bans and uniqueness/fingerprint rules apply only when they serve
  the chosen brief. Exact reuse and the user's branding/scope take precedence.
- **Existing hero only:** use `references/integration.md`; retain the existing page,
  navigation, text and backend. Do not replace a whole website to add a film.
- **New generated media:** read `vendor/replicate-media/SKILL.md` and
  `references/media.md`. Use the user's provider/model. Replicate is the default
  for all new media. Another provider requires the user's explicit choice; do not
  fall back to KIE or another service when Replicate is unavailable. Prepare local
  prompts/placeholders and explain the missing access instead. Do not require both accounts.
- **Publishing:** read `references/publishing.md`. Sites is optional, never assumed
  available in Claude or a plain Codex installation.
- **Extending this library:** read `references/maintaining.md`.
- **Source documents and asset packs:** read `references/source-backups.md`.
  Default to a verified independent online copy, not just original URLs or local
  downloads. Reuse an authorized private backup destination, preserve versions and
  record checksums/access. Backup approval is not approval for public media use.

Do not load all vendor references for a small task. These main instructions resolve
integration choices across the bundled skills. Preserve upstream licenses.

## Establish only the missing decisions

Reuse answers already provided. Establish purpose, brand, supplied design direction,
assets, visitor's next action, exact versus adapted reuse, mobile treatment and
publication target. Discuss continuous/chaptered motion only if motion fits the brief.
For an architectural journey agree a proposed route/floorplan before inventing
connected rooms; reference photos do not establish unseen geometry.

Choose ordinary implementation details autonomously. Installing a skill, preparing
a template or inspecting a model does not authorize paid generation. Before spending,
record model, verified schema, count, duration, resolution, stills, current price
estimate and total/retry allowance. **Always show new or newly selected media here
in chat and obtain explicit asset/version approval before putting it on the web.**
This includes images, videos and other media, public previews/CDNs, staging sites,
public repository assets and deployment archives. Use native chat previews, local
file previews or localhost for review; do not host unapproved media to get a review
link. Generation/model approval and plan approval are not media publication approval.
Record approvals and reuse them for unchanged assets; preserve existing approved live
media without asking again. Material visual changes need renewed approval.
Authorized provider input uploads for generation are part of generation, not site
publication. Read `references/media.md` for the review workflow.

## Prepare

1. Run `python scripts/doctor.py` from this skill directory. It is local and read-only.
   Python 3.10+ is the bootstrap requirement; `python3` may be the command name.
   Use `--mode video` for media encoding or `--mode scroll-craft` for that toolkit.
   FFmpeg/ffprobe and Node are optional for a plain static/CSS site.
2. Run `python scripts/setup.py --plan` for missing dependency installation commands.
   `--install ffmpeg` installs FFmpeg and ffprobe through the host's package manager;
   run only within an authorized setup task. No binaries, accounts or keys are hidden
   in this package. Node is needed for Scroll Craft, not the vanilla starter.
3. Read `catalog.json`. Select a template by fit, not by whichever was last used.
   `reference_packs` can instead supply a source document, example code and assets
   hosted elsewhere. Read the pack's local index and original sources; a pack need
   not be a ready-made HTML template. Keep local originals and make an independent
   private online backup when authorized; keep them out of public hosting until approved.
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

For every site check composition, typography, contrast, responsive layouts, useful
navigation/controls, keyboard access, performance and business-flow outcomes.
For a video/scroll site also verify forward/reverse seeks at every boundary, posters,
mobile selection, tail hold and release. Test reduced motion and failure where relevant.
A desktop viewport is not a real-phone test.
State checks actually run. Build/typecheck the chosen framework; a static starter
needs no framework installation.

Respect publication scope and the mandatory in-chat media approval gate. Reuse an existing site and audience;
do not create duplicates or broaden access implicitly. Return a verified deployed
URL or local files and an honest verification summary. Do not claim production
completeness for unconnected forms, placeholders or unverified device behaviour.
Skill creation itself never deploys a site.
