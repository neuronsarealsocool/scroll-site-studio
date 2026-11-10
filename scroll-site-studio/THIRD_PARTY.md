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

## Reference-pack media and notices

Working prompts and hosted-media manifests use neutral names. No media bytes are
bundled in this skill archive. Those separate hosted assets retain their applicable
rights; the package MIT license does not relicense third-party images, videos,
logos, brands or fonts. Hosting copies is not a new rights grant.

The electric vehicle pack requires the full notice in
`licenses/electric-vehicle-explorer.txt`, also supplied beside its hosted media.
Carry applicable notices into any redistribution. Optional public creator/tutorial
credits are omitted; legally required copyright and third-party notices remain.
