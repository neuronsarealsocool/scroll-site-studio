# Licensing and provenance

The top-level license covers the original integration instructions, portable scripts,
SVG placeholders and starter code authored for this package. Independent components
retain their own licenses. No ownership of those projects is claimed.

| Component | Source | License / changes |
|---|---|---|
| Scroll World | https://github.com/oso95/scroll-world | MIT, copyright 2026 cyw; Codex/Replicate adaptation from the locally developed skill. Two personal example paths in pipeline.md made portable. |
| Scroll Craft | https://github.com/nateherkai/scroll-craft | MIT, copyright 2026 Nate Herk; complete installed skill snapshot, root upstream LICENSE added. |
| Replicate Media | Local workflow instructions developed for this project | MIT under this package; no provider SDK, credentials or media outputs. |
| Bounded flight engine | Derived from the Scroll World integration developed for Alder & Form | Original upstream MIT notice retained beside template runtime. Additional lifecycle recovery is local to this starter. |

vendor-manifest.json records content hashes and known provenance. The Scroll Craft
snapshot came from the prior local installation; its exact upstream commit was not
recorded then, so file hashes identify it rather than an invented commit SHA.

FFmpeg/ffprobe, Python, Node, Chrome and Playwright are external dependencies, not
embedded executables or libraries in this ZIP. Install using the recipient's package
manager or official vendor instructions. FFmpeg licenses depend on the selected
build; https://ffmpeg.org/legal.html describes LGPL/GPL distinctions. Gyan Windows
builds are GPLv3: https://www.gyan.dev/ffmpeg/builds/ . If binaries are redistributed
in a future release, include the exact applicable licenses and complete corresponding
source/build materials as required; this release avoids binary redistribution.

Sites and other hosting connectors remain separately installed services. Their
implementations, paid accounts, API keys, and plugin bundles are not copied. The
publishing adapter explains how to use tools available in the recipient's environment.

No original property reference photographs, stock imagery, generated videos, client
branding, proprietary design screenshots or font files are bundled. Catalog design
references link to sources without copying their media. Follow the applicable rights
when adding assets. Source code licenses do not grant rights to referenced brands.

## Planet Jumping reference credit

All credit for the original Planet Jumping prompt/design reference goes to
[MotionSites.ai](https://www.motionsites.ai/), as explicitly specified by the user.
The original supplied prompt is preserved privately, not relicensed under this
package MIT license. Public distribution includes attribution and authored usage
notes only. No referenced media, fonts, logo or finished site is bundled.

## VEYRA reference credit

Credit [MotionSites.ai](https://www.motionsites.ai/) for the reference supplied by
the user. The upstream VEYRA project credits concept, art direction, interaction
design and media finishing to [Amir Mušić](https://github.com/amirmushichge/veyra-interactive-car).
Retain its MIT LICENSE and THIRD_PARTY_NOTICES.md when reusing source or media.
The pinned source ZIP is backed up privately; no upstream code, media or prompt is
bundled in this public skill. Upstream dependency/font notices remain applicable.
