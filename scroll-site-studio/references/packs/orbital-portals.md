# Orbital portal experience

Build a self-contained HTML document with inline CSS/JavaScript and
no external code libraries. Its media remains external, so “self-contained” does
not mean offline-ready. The core interaction is a rounded canvas mask over
screen-locked imagery: pointer tilt moves the window while its image stays fixed,
then a click expands it to full-screen footage before committing the next state.
A video preloader, docking logo, large condensed planet title, fact rows and custom
cursor complete the composition.

The state chain starts at Mars, travels to Earth, then Venus. Venus shows
a Mercury still as the next preview but is terminal. The eight-planet sidebar is
display-only; this pack does not provide eight working destinations. Preserve this
scope for this working prompt or explicitly design an extension for a broader brief.

## Implementation requirements

Implement complete, valid CSS and JavaScript; this working prompt is a specification,
not runnable application code.
Retain a readable native/system-font fallback; no supplied font files imply no
permission or need to acquire proprietary fonts. Check actual text width and layout.

Handle rejected playback, metadata/load errors, network stalls and transition
timeouts so the preloader and travel lock always release. Waiting for `ended` alone
can hang. Verify any cross-origin media requirements before relying on pixel reads
or canvas export, and provide usable fallbacks when media is unavailable.

Scope entrance selectors correctly so title/fact visibility returns after reveal.
Preserve keyboard focus and useful navigation; the prompt supplies menu/anchor markup
without complete destinations or menu behaviour. Keep native cursors for touch,
unsupported pointer types and failures of custom-cursor JavaScript. A
CSS-only reduced-motion rule does not stop its JavaScript tilt, requestAnimationFrame
loops or travel/preloader footage: implement a readable reduced-motion path too.

Test short mobile viewports as well as 375/768/1440px widths; fixed minimum heights
combined with hidden page overflow can clip essential content. Test touch travel,
resize during animation, repeated clicks, failure recovery, state commits and canvas
mask alignment. A planet facts are unverified copy; check them for an
educational site rather than assuming the prompt is an authoritative data source.


The manifest now includes four travel/background MP4s, a next-preview JPEG and a
logo SVG. Their actual bytes are available on the library host. Verify motion,
canvas use and endpoints during the build. At least one travel clip uses HEVC; check target-browser decoding and prepare
an approved H.264 derivative if compatibility requires one. Font files are not supplied; choose
licensed type or a readable system fallback. The logo and any recognizable pixels
remain unchanged; select branding deliberately rather than assuming it is generic.

## Project rules

Use this working prompt as written, adapt it, or lock selected elements and combine
the rest with the user's other ideas. Establish the real brand, audience, purpose,
primary action and required functionality. Keep the existing or chosen stack; for
a new project choose a suitable responsive frontend. WordPress and WooCommerce
are optional. Motion is optional unless required by this selected experience.

Default to Replicate for new media, using the bundled media workflow. Confirm the
model inputs and authorized budget before paid jobs. Show newly selected/generated
media in chat and obtain approval before putting it on any public site, preview,
CDN or repository. Reuse explicit approval for unchanged assets. The library host
is asset storage, not automatic approval for every future project's use.

Use real HTML text and semantic controls. Keep content useful before media loads.
Implement keyboard access, visible focus, touch controls, reduced motion, loading
and failure recovery. Test desktop, mobile, short screens and resize. Verify real
actions and label demonstration data. Do not claim a connected backend or measured
performance without testing it. Preserve applicable license notices; hosting a
copy does not grant new rights to brands, fonts or media.

## Hosted asset map

Use these direct URLs in the implementation. [Machine-readable manifest](https://lapis-slate-xvar.here.now/library/orbital-portals/assets.json)
includes file sizes and SHA-256 hashes. Local manifest: `assets/manifests/orbital-portals.json`.

| ID | Role | File |
| --- | --- | --- |
| asset-01 | mars bg | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/71853add431544.mp4) |
| asset-02 | to earth | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/2a4c28730cea46.mp4) |
| asset-03 | to venus | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/0dcfd0be919842.mp4) |
| asset-04 | to mars | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/b799e9ef8e4c40.mp4) |
| asset-05 | mercury | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/7e7d45a4e82b44.jpg) |
| asset-06 | logo | [Open asset](https://lapis-slate-xvar.here.now/library/orbital-portals/media/ede1ec6bf03d48.svg) |
