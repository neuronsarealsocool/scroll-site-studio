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

Download and extract the [v0.4.10 release](https://github.com/neuronsarealsocool/scroll-site-studio/releases/tag/v0.4.10),
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

## Neutral reference library

- [Alpine editorial retreat](scroll-site-studio/references/packs/alpine-editorial.md): 19 media files.
- [Coffee product carousel](scroll-site-studio/references/packs/coffee-product-carousel.md): 15 media files.
- [Architectural landscape journey](scroll-site-studio/references/packs/architectural-landscape.md): 15 media files.
- [Orbital portal experience](scroll-site-studio/references/packs/orbital-portals.md): 6 media files.
- [Electric vehicle explorer](scroll-site-studio/references/packs/electric-vehicle-explorer.md): 20 media files.
- [Cinematic site workflow](scroll-site-studio/references/packs/cinematic-site-workflow.md): 1 media files.
- [The Visual Story Method - Incomplete Prompt - Watch YouTube Video First](scroll-site-studio/references/packs/desktop-mobile-workflow.md): 1 media files.
- [Tower and room tours](scroll-site-studio/references/packs/tower-room-tours.md): 12 media files.

[Browse prompts and assets](https://lapis-slate-xvar.here.now/library/browse.html). Direct hosted URLs replace original
asset locations in these working packs. The fifteen prompts can be reused as written
or adapted. All packs and future additions use neutral names, with WordPress optional,
Replicate for new media and approval in chat before new media is published.

Required licenses and recognizable media remain; this does not erase Git history
or grant new rights over third-party assets. Private working backups stay private.

## Recovered prompt packs

Version 0.4.1 includes seven independently worded working specifications recovered from the chat audit: lake cabin retreat, private aviation journey, racing driver profile, cinematic wipe studio, point-cloud companion, curved film archive and bird species atlas. The library now has fifteen packs and 157 hosted media/support files. Detailed neutral source documents remain in the private working backup. The Alder & Form pack includes its approved screenshot and a media brief, and the Point-cloud companion pack includes its approved exact geometry and required notice.
