# Scroll Site Studio 0.4.3

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

## Reference packs

Eight neutral working packs include direct hosted asset maps. Use their prompts as
written, adapt them, or combine selected parts with other ideas. WordPress remains
optional. New media defaults to Replicate and still requires in-chat approval.

- [Alpine editorial retreat](references/packs/alpine-editorial.md): 19 media files.
- [Coffee product carousel](references/packs/coffee-product-carousel.md): 15 media files.
- [Architectural landscape journey](references/packs/architectural-landscape.md): 15 media files.
- [Orbital portal experience](references/packs/orbital-portals.md): 6 media files.
- [Electric vehicle explorer](references/packs/electric-vehicle-explorer.md): 20 media files.
- [Cinematic site workflow](references/packs/cinematic-site-workflow.md): 1 media files.
- [Desktop and mobile workflow](references/packs/desktop-mobile-workflow.md): 1 media files.
- [Tower and room tours](references/packs/tower-room-tours.md): 12 media files.

[Browse the hosted library](https://lapis-slate-xvar.here.now/library/browse.html). The release includes working prompts,
asset manifests and required notices; media bytes are hosted separately. Originals
and private working backups are outside the public package. Required notices and
recognizable imagery can identify a source; neutral naming is not full anonymity.

## Expanded reference library

Fifteen packs cover architecture, hospitality, commerce, aviation, racing, film, particle interfaces, archives, natural-history viewers and production workflows. The catalog links 156 approved hosted media and support files. The lake-cabin pack contains a detailed media brief; the Point-cloud companion pack now includes its approved exact geometry and required notice. Detailed neutral source documents are maintained privately when public redistribution terms are unclear.
