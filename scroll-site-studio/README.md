# Scroll Site Studio 0.2.12

A portable high-end website skill and template library for Codex or Claude Code. Scroll effects are optional. Built from the
Alder & Form workflow, with complete Scroll World, Scroll Craft and Replicate Media
instruction sets bundled locally. The original site's photos, paid footage, source,
hosting identity, database, enquiries and credentials are not included.

## Install

Extract the archive and open a terminal in this folder, using Python 3.10+:

```text
python scripts/install.py --agent codex
python scripts/install.py --agent claude
```

Choose your agent; both are not required. The installer copies this whole folder to
`~/.codex/skills/scroll-site-studio` (respects CODEX_HOME) or
`~/.claude/skills/scroll-site-studio`. Add `--project /path/to/project` to target
project-local `.agents/skills` or `.claude/skills`. Existing installs are never
overwritten; explicitly move an old copy to a backup before updating. Manual copying
also works.

Codex: use `$scroll-site-studio` on the next turn. Claude Code: invoke
`/scroll-site-studio` or ask it to read this folder's SKILL.md. Plain Claude chat
without file/terminal/browser access cannot execute the workflow by itself.

## Dependencies

```text
python scripts/doctor.py
python scripts/setup.py --plan
python scripts/setup.py --install ffmpeg
```

FFmpeg and ffprobe are installed as a pair through WinGet, Homebrew, apt, dnf or
pacman when available. The package includes setup helpers, not OS-specific binaries.
Windows Gyan builds are GPLv3; copying their executables into a public release also
requires satisfying corresponding distribution/source obligations. This package
leaves that distribution with the package-manager provider. See THIRD_PARTY.md.
Python/Node runtimes are not embedded. Setup prints commands when a manager is
missing; it does not execute downloaded shell scripts or accept license prompts.

The vanilla starters need no Node packages. Scroll Craft needs Node 18+; its optional
browser harness additionally needs Chrome and playwright-core in the **build project**.
The agent's supported browser tools can instead perform acceptance checks. No paid
generation runs during installation or testing. Accounts/keys are needed only when
generating or publishing through the chosen service.

## Creative direction and media approval

Use supplied prompts, templates and assets verbatim, as adaptable guidelines, or
in a hybrid with named locked elements. Follow other user ideas and references;
do not force scroll effects, uniqueness rules or a single style on every site.
Replicate is always the default for media generation. A different provider needs
an explicit user choice. Show actual new/selected media in this chat and obtain
approval before uploading it to websites, previews, CDNs or public repositories.
Use local/native chat previews while approval is pending. See references/media.md
and references/creative-direction.md. Existing approved unchanged media stays approved.

## Start

```text
python scripts/catalog.py list
python scripts/catalog.py init bounded-walkthrough --dest ../my-scroll-site
python scripts/serve.py --root ../my-scroll-site --port 4500
```

Open http://127.0.0.1:4500. The starter is a local static layout with an original
SVG placeholder and motion disabled until clips are supplied. To qualify mechanics
without spending credits, generate an offline technical demo:

```text
python scripts/media.py demo ../my-scroll-site
```

It creates synthetic moving test patterns, matched posters, native landscape/portrait
files and enables the film. These are not architectural renders. It refuses existing
film assets and requires the bundled starter. It never calls a generation provider.

## Maintain and share

catalog.json indexes two starters and source references. See references/maintaining.md
for adding entries. The validator checks manifests, relative references, licensing,
hashes and accidental private state. release.py creates a ZIP plus SHA-256 after
validation and never uploads. Keep runtime files in site projects, not this skill.

Example prompt:

> Use Scroll Site Studio to build a studio website. Keep a walkthrough in the hero,
> use separate portrait footage, propose the camera route first, and let me approve
> videos before publication. My media budget is US$10.

Templates are starting points. They do not make every backend or business workflow
production-ready. Publishing uses the recipient's own chosen host and credentials.

## Reference pack platform choice

All packs, including Layer and Frostwood, default to the user-selected or existing
project/host stack; new projects use a suitable responsive frontend. WordPress and
WooCommerce are optional choices. A supplied WP theme or WP-specific prompt never
selects the stack automatically, including for verbatim design reuse.

## Source packs

The Frostwood pack links its video, detailed prompt document and original image/theme archives. It can guide close reproduction or a different design brief. Originals stay in their existing Drive location; the library provides an index and usage notes rather than republishing the source media. See references/packs/frostwood.md.

The Layer pack adds a premium coffee product showcase, detailed matched-asset
prompts, a hero reference and a WooCommerce theme example. See
references/packs/layer.md for reuse modes, the private backup and missing product
data. Source packs guide other platforms too; they are not runnable HTML starters.

The Horizon Estates pack adds architectural parallax direction, 15 Orange/Purple
images and a detailed prompt document. Its index maps source filenames, real alpha
channels and missing deliverables. See references/packs/horizon-estates.md.

## Independent backups

Default to a verified independent online copy of source documents and assets, in a designated private repository/folder when public use is not approved. Preserve dated versions and checksum manifests, and verify by downloading the copies. Private backup does not approve public website use. See references/source-backups.md.

## Planet Jumping — MotionSites.ai

All credit for the original Planet Jumping prompt/design reference goes to
[MotionSites.ai](https://www.motionsites.ai/). This prompt-only pack describes a
cinematic canvas portal experience. One supplied text file is backed up privately;
referenced media and fonts were not supplied. The source prompt is not included
in the public release. See references/packs/planet-jumping.md for reuse guidance and dependency limits.

## VEYRA — MotionSites.ai reference

Credit [MotionSites.ai](https://www.motionsites.ai/) for the supplied reference,
and retain the upstream VEYRA project credit to
[Amir Mušić](https://github.com/amirmushichge/veyra-interactive-car). The pack
indexes a pinned automotive interaction scene with source and 18 bundled media
files. The prompt and source ZIP have a verified private backup. See references/packs/veyra.md for reuse and verification details.

## Darrell Wilson method — Replicate adaptation

Credit [Darrel Wilson](https://www.youtube.com/@darrelwilson) for the tutorial and
method. This pack combines a business-led style tile, visual-story table, matched
media handoffs, scroll pacing and a dedicated mobile workflow. Replicate replaces
the source provider; mandatory in-chat media approval and optional WordPress remain.
Original sources and separate working adaptations have a verified private backup.
See references/packs/darrell-wilson-method.md for sources and limits.

## Bart method — Replicate adaptation

Credit [Bart Slodyczka / Barty-Bart](https://github.com/Barty-Bart/gpt-6-astra-10k-websites).
The pack follows Desktop Build with Mobile Refinement in one responsive project.
Original pinned source and separate Replicate working prompts are privately backed
up and restore-verified. No finished site or production media is supplied.
See references/packs/bart-method.md for workflow, credit and limits.
