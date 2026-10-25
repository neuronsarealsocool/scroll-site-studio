---
updated_at: 2026-10-20T20:19:58.285+11:00
edited_seconds: 30
created: 2026-10-20T17:48
updated: 2026-10-24T16:33
---
# Scroll Site Studio

A reusable skill for building high-end responsive websites with **Codex or
Claude Code**, and growing a library of templates and design references over time. Scroll effects and video are optional.

## Install

Download and extract the [v0.2.11 release](https://github.com/neuronsarealsocool/scroll-site-studio/releases/tag/v0.2.11),
then open a terminal inside the extracted `scroll-site-studio` folder. With Python 3.10+:

```text
python scripts/install.py --agent codex
```

Or, for Claude Code:

```text
python scripts/install.py --agent claude
```

If you cloned this repository instead, the skill is one folder deeper:

```text
python scroll-site-studio/scripts/install.py --agent codex
python scroll-site-studio/scripts/install.py --agent claude
```

Choose the agent you use; both are not required. Existing installations are never
overwritten. Add `--project /path/to/project` for a project-local installation.

Codex: invoke `$scroll-site-studio` on the next turn. Claude Code: invoke
`/scroll-site-studio` or ask it to read the installed `SKILL.md`.

## Design and media defaults

- Build high-end websites with the interaction that suits the brief; scroll is optional.
- Default to Replicate for generated media. Switch providers only when explicitly chosen.
- Show new/selected media here in chat and get approval before putting it anywhere on
  the web, including staging, CDNs and public repositories. Use local/chat previews
  while approval is pending. Existing approved unchanged media retains approval.
- Use prompts, templates and assets verbatim, as guidelines, or in a hybrid. Respect
  the user's other ideas/references and record what must stay exact.

## What's included

- A main workflow combining camera walkthroughs and varied editorial scroll design.
- Bundled Scroll World, Scroll Craft and Replicate Media skills with license notices.
- Two framework-free starters: a bounded walkthrough and a layered editorial page.
- FFmpeg/ffprobe dependency checks, encoding helpers and an offline synthetic demo.
- A template/reference catalog with import, validation and release tools.
- Media budget, mandatory in-chat media approval and mobile verification guidance.

FFmpeg executables, Python/Node runtimes, paid media, API keys and publishing accounts
are not embedded. Setup helpers use the recipient's OS package manager. Sites is an
optional separately installed connector; ordinary static hosting is also supported.
Read [third-party notices](scroll-site-studio/THIRD_PARTY.md) for component provenance.

## Start a project

From the skill folder:

```text
python scripts/doctor.py
python scripts/setup.py --plan
python scripts/catalog.py list
python scripts/catalog.py init bounded-walkthrough --dest ../my-website
python scripts/serve.py --root ../my-website --port 4500
```

The default starter uses original placeholder art. To test video mechanics for free,
run `python scripts/media.py demo ../my-website` with FFmpeg installed. It generates
synthetic test patterns, not architectural footage, and never calls a paid model.

## Grow the library

Add reusable sites under `assets/templates` through the catalog importer, and add
public source URLs with notes as design references. Keep client secrets and media
rights separate from template code. The [maintenance guide](scroll-site-studio/references/maintaining.md)
explains updates, checksums and releases.

Example request:

```
Use Scroll Site Studio to build my studio website. Propose the camera route first,
use separate portrait footage, and let me approve videos before publication. My
generation budget is US$10.
```

## Validation and limits

The original 0.1.0 starters were tested on Windows for template creation, local media preparation,
installer targets, archive integrity and desktop/portrait browser behaviour. macOS,
Linux, real-phone decoders and an end-to-end Claude Code run remain unverified.
See [the validation record](scroll-site-studio/TESTED.md). Starter layouts do not
include a connected business backend. Use real licensed assets and test your result.

## License

MIT for original package work. Bundled components retain their own MIT licenses;
FFmpeg and other external dependencies retain their own licenses. This project is
independent of OpenAI, Anthropic, Replicate and the upstream skill authors.

## Reference pack platform choice

All packs, including Layer and Frostwood, default to the user-selected or existing
project/host stack; new projects use a suitable responsive frontend. WordPress and
WooCommerce are optional choices. A supplied WP theme or WP-specific prompt never
selects the stack automatically, including for verbatim design reuse.

## Reference packs

Not every contribution needs to be a coded template. Detailed prompt documents, videos, images and example themes can be registered as linked source packs. [Frostwood](scroll-site-studio/references/packs/frostwood.md) is the first example; originals remain in their source Drive folder.

## Source resilience

The workflow now defaults to independent online backups for source-pack files rather than depending on original Drive links. Use an authorized private destination, preserve versions and verify restored checksums. The Frostwood pack has an owner-private GitHub snapshot; it is accessible only to authorized users and is separate from approval to publish media.

## Layer reference pack

[Layer](scroll-site-studio/references/packs/layer.md) adds a premium coffee
showcase with detailed product/ingredient prompts, a hero reference, asset QA and
a WordPress/WooCommerce example. Use it verbatim, adapt it, or combine it with
other references. All five source files have a verified private backup; the public
skill contains links and guidance. The source theme needs product data that is
not supplied in its archives. Replicate and in-chat media approval remain the defaults.

## Horizon Estates reference pack

[Horizon Estates](scroll-site-studio/references/packs/horizon-estates.md) adds
architectural parallax direction with Orange and Purple asset sets, detailed prompts
and an inspected image map. All 15 original PNGs and both document exports are
backed up privately with verified checksums. It is a prompt-and-assets pack, with
WordPress optional; no finished theme or site code is supplied.

The [timestamped video audit](scroll-site-studio/references/packs/horizon-estates-video-audit.md)
records the final hero scale, headline overlap, scroll entrances, count-up figures,
section order and layout details, with private checksum-verified review evidence.

The user-selected [headline placement reference](scroll-site-studio/references/packs/horizon-estates-headline-reference.md)
requires visible clearance and complete headline letters at desktop and ultrawide sizes.
The uploaded still is backed up privately and is not bundled in the release.

## Planet Jumping — MotionSites.ai

All credit for the original Planet Jumping prompt/design reference goes to
[MotionSites.ai](https://www.motionsites.ai/). This prompt-only pack describes a
cinematic canvas portal experience. One supplied text file is backed up privately;
referenced media and fonts were not supplied. The source prompt is not included
in the public release. See [the pack index](scroll-site-studio/references/packs/planet-jumping.md) for reuse guidance and dependency limits.

## VEYRA — MotionSites.ai reference

Credit [MotionSites.ai](https://www.motionsites.ai/) for the supplied reference,
and retain the upstream VEYRA project credit to
[Amir Mušić](https://github.com/amirmushichge/veyra-interactive-car). The pack
indexes a pinned automotive interaction scene with source and 18 bundled media
files. The prompt and source ZIP have a verified private backup. See [the pack index](scroll-site-studio/references/packs/veyra.md) for reuse and verification details.

## Darrell Wilson method — Replicate adaptation

Credit [Darrel Wilson](https://www.youtube.com/@darrelwilson) for the tutorial and
method. This pack combines a business-led style tile, visual-story table, matched
media handoffs, scroll pacing and a dedicated mobile workflow. Replicate replaces
the source provider; mandatory in-chat media approval and optional WordPress remain.
Original sources and separate working adaptations have a verified private backup.
See [the pack index](scroll-site-studio/references/packs/darrell-wilson-method.md) for sources and limits.
