# Planet Jumping — MotionSites.ai

**All credit for the original Planet Jumping prompt and design reference goes to
[MotionSites.ai](https://www.motionsites.ai/).** Attribution was explicitly supplied
by the user. This library contributes indexing and implementation notes; it does
not claim authorship of the source prompt or experience. Preserve this credit when
using or sharing the reference. Credit does not establish ownership of every
referenced logo, font or media file, or grant redistribution rights.

## Supplied material and backup

Only one asset was supplied: a detailed text build prompt, headed “Planet Jumping”.
There is no supplied screenshot, finished HTML, video/image file, font package or
project code. This is a prompt-only reference pack, not a runnable starter.

- [Credited source](https://www.motionsites.ai/)
- [Private prompt snapshot, 24 October 2026](https://github.com/neuronsarealsocool/scroll-site-studio-source-backups/tree/main/planet-jumping/2026-10-24)

The snapshot preserves `Pasted text.txt` byte-for-byte with a size/SHA-256 manifest.
A fresh GitHub restore verified that file. The original attachment is the precise
source supplied here; the credited website is not a verified public download page
for this exact prompt. The full prompt is not republished in the public skill.
Private access requires repository authorization; other recipients need their own
authorized source copy. Record their source/version instead of inventing a URL.

The text names four MP4s, one JPEG and one SVG on a third-party CloudFront host.
Those URLs remain intact inside the preserved prompt, but the remote files were
not downloaded or backed up, and availability, permissions and canvas compatibility
were not verified. Font files were also not supplied. A prompt backup does not
protect the remote media if its original host disappears. When actual assets become
available, add a new dated snapshot and verify them separately.

## Reference behaviour

The prompt specifies a self-contained HTML document with inline CSS/JavaScript and
no external code libraries. Its media remains external, so “self-contained” does
not mean offline-ready. The core interaction is a rounded canvas mask over
screen-locked imagery: pointer tilt moves the window while its image stays fixed,
then a click expands it to full-screen footage before committing the next state.
A video preloader, docking logo, large condensed planet title, fact rows and custom
cursor complete the composition.

The specified state chain starts at Mars, travels to Earth, then Venus. Venus shows
a Mercury still as the next preview but is terminal. The eight-planet sidebar is
display-only; the source does not provide eight working destinations. Preserve this
scope for exact reuse or explicitly design an extension for a broader brief.

## Reuse modes and platform

- **Verbatim:** obtain the original prompt from an authorized source; preserve its
  requested composition, state model, names, timings and exact media URLs where
  available and approved. Keep the supplied prompt unchanged and record necessary
  technical repairs in the working copy. Do not silently substitute assets or claim
  a complete reproduction when dependencies are missing.
- **Adapted:** reuse the portal-mask transition and staged reveal method for another
  subject or brand, changing the layout, media and navigation to suit the project.
- **Hybrid:** record locked elements, then adapt the rest to the user's references.

Use the user's chosen or existing project/host stack. For a faithful new build the
source's vanilla single-file approach is suitable; WordPress remains optional.
This is click-driven and needs no scroll sequence by default. The source's exact-URL
requirement belongs to faithful reproduction, not unrelated adaptations. Replicate
is the default if new media is requested. New/selected media, including the source
logo, needs in-chat approval before any public site, preview, CDN or repository use.
The source logo's alternative text names Ubernatural; keep brand provenance distinct
from MotionSites.ai's requested prompt/design credit, and adapt branding explicitly.

## Implementation gaps to resolve during a build

The supplied text is a specification with pseudocode, not executable HTML. Expand
CSS shorthand placeholders and omitted timing syntax into valid declarations.
Retain a readable native/system-font fallback; no supplied font files imply no
permission or need to acquire proprietary fonts. Check actual text width and layout.

Handle rejected playback, metadata/load errors, network stalls and transition
timeouts so the preloader and travel lock always release. Waiting for `ended` alone
can hang. Verify any cross-origin media requirements before relying on pixel reads
or canvas export, and provide usable fallbacks when source media is unavailable.

Scope entrance selectors correctly so title/fact visibility returns after reveal.
Preserve keyboard focus and useful navigation; the prompt supplies menu/anchor markup
without complete destinations or menu behaviour. Keep native cursors for touch,
unsupported pointer types and failures of custom-cursor JavaScript. The source's
CSS-only reduced-motion rule does not stop its JavaScript tilt, requestAnimationFrame
loops or travel/preloader footage: implement a readable reduced-motion path too.

Test short mobile viewports as well as 375/768/1440px widths; fixed minimum heights
combined with hidden page overflow can clip essential content. Test touch travel,
resize during animation, repeated clicks, failure recovery, state commits and canvas
mask alignment. The source's planet facts are unverified copy; check them for an
educational site rather than assuming the prompt is an authoritative data source.

Ingestion inspected the text and verified the backed-up bytes. No site was built,
media generated, remote assets tested or production behaviour validated.
