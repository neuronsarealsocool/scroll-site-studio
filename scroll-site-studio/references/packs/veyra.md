# VEYRA — MotionSites.ai reference

Credit [MotionSites.ai](https://www.motionsites.ai/) for the reference supplied by
the user. The linked **VEYRA project, concept, art direction, interaction design
and media finishing are credited upstream to [Amir Mušić](https://github.com/amirmushichge/veyra-interactive-car)**.
Preserve both credits and the upstream MIT license and `THIRD_PARTY_NOTICES.md`
when copying its code, documentation or media. This library does not claim original
authorship of the reference, project or assets.

## Sources and verified backup

- [Pinned project v1.0.0](https://github.com/amirmushichge/veyra-interactive-car/tree/v1.0.0)
- [Source ZIP](https://github.com/amirmushichge/veyra-interactive-car/archive/refs/tags/v1.0.0.zip)
- [Upstream reproduction prompt](https://github.com/amirmushichge/veyra-interactive-car/blob/v1.0.0/docs/RECREATE.md)
- [Desktop reference](https://raw.githubusercontent.com/amirmushichge/veyra-interactive-car/v1.0.0/docs/images/desktop.png)
- [Phone reference](https://raw.githubusercontent.com/amirmushichge/veyra-interactive-car/v1.0.0/docs/images/mobile.png)
- [Private snapshot, 24 October 2026](https://github.com/neuronsarealsocool/scroll-site-studio-source-backups/tree/main/veyra/2026-10-24)

Tag v1.0.0 resolved to commit `5779ec0762559b84bd5da3b6ffccf76e747f7587`
at ingestion. The private snapshot preserves the original user-supplied prompt and
the downloaded source ZIP, including source, 18 media files, screenshots, license
and notices. Both file sizes and SHA-256 hashes were verified against a fresh
GitHub restore. Upstream's 32 reference-manifest entries also matched independently
(text line endings normalized as specified; binary bytes unchanged).

The public skill distributes links and usage notes, not the prompt, upstream code
or media. Private access requires repository authorization; other recipients can
obtain the pinned public source and make their own authorized backup. Preserve the
version and inspect the downloaded files rather than following a moving branch.

## What is supplied

The user supplied a reproduction prompt. Its linked release was downloaded and
inspected: a React/TypeScript/Vite scene with CSS, tests, a lockfile and local media.
No runtime 3D model, scroll-scrubbing system or vehicle-sales backend is required.
Node 22+ and pnpm 10.15.1 are declared for this release. Space Grotesk Regular is
imported from Google Fonts, not bundled; offline typography needs an explicit plan.

This is a framed automotive design study with four image-relative hotspots:
Drive, Battery, Paint and Wheels. Hood/battery hover uses four authored forward/
reverse films and a canvas; detail entry zooms/crossfades into still cutaways.
Five paint choices and three wheel choices are independent render alternatives,
not a combined configurator. Appearance menus sit below the vehicle frame.

Active neutral media is `public/media/exterior-polished.png`; active details are
`drive-blue.png` and `battery-blue.png`. Paint/wheel variants live in `config/`.
Earlier stills and dormant optics/detail-flight metadata are retained in the source;
they are not missing active features to invent or enable.

## Reuse modes and platform

**Verbatim:** obtain the pinned release and reuse the implementation, styles,
media bytes and lockfile. Read its project instructions and architecture/media/
verification guides before a build. Keep the full car, image-relative hotspots,
neutral-pose gate, endpoint sequencing, decode gates, frozen detail handoff and
appearance locks. Preserve the source reference manifest; do not regenerate it to
hide a mismatch. Retain upstream credits and describe deviations honestly.

**Adapted:** use its compact product-exploration structure and authored-media
interaction method for another vehicle or product. A replacement set must share
camera, crop, lighting and neutral endpoints; replacing one still alone does not
preserve continuity. State which source behaviour and styling changed.

**Hybrid:** record the locked media, layout, copy or interactions and adapt only
the flexible parts. Scope accessibility fixes separately from a faithful restore
when exact upstream behaviour is requested.

Follow the chosen or existing project/host stack. React/Vite is the source platform
and practical faithful-build default for a new project; WordPress is optional.
For another required stack, establish the original reference before porting its
behaviour. Do not replace this scene with a generic scrolling marketing page.
Original requirements to avoid prices, speculative specifications and sales content
belong to faithful reproduction; adaptations follow the user's actual brief.

## Media and approval

No generation is needed for reproduction. Keep the existing aligned media intact;
do not resize, recolour, retime or regenerate it while claiming exact reuse.
The source's “approved” language describes its reference release, not the current
user's permission to publish. Show newly selected media here and obtain in-chat
approval before public websites, staging, CDNs or repositories. Private backup
does not provide that publication approval.

For separately requested new media, Replicate remains this skill's default.
Upstream's optional LTX guide does not choose LTX automatically. Use another provider
only when explicitly chosen, and authorize any paid generation within the media
workflow. Upstream credits the existing films to Kling via Pika with After Effects
finishing; do not relabel them as Replicate or LTX outputs.

## Build checks and limits

During an authorized build, run the release's frozen-lockfile install, tests,
`verify:reference` and production build after inspecting its scripts. Inspect actual
desktop/phone output, both technical details, all appearances, rapid hover changes,
menu reachability, decoded-frame seams, keyboard controls and reduced motion.
Use its documented preview port or a deliberate free alternate without stopping
unrelated processes. Reference screenshots guide composition, not proof of timing.

The upstream release documents an appearance-close focus race; report it rather
than claiming it is fixed. Physical Safari/touch and enlarged-text support remain
separate checks. Concept cutaways are illustrative, not verified engineering data.

Ingestion checked archive CRC, all 32 upstream reference hashes, source notices,
architecture and desktop/phone screenshots. No packages were installed, downloaded
project code executed, site built, unit suite run, or device behaviour tested here.
Upstream verification reports are provenance, not fresh test results from this skill.
