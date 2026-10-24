# Scroll Site Studio 0.2.8

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
