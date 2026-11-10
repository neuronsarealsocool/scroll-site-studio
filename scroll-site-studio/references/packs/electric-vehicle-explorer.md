# Electric vehicle explorer

Build a framed electric-vehicle exploration scene with a full-car view, four
image-relative hotspots and appearance menus below the frame. The hotspots are
Drive, Battery, Paint and Wheels. Hood and battery interactions use authored
forward/reverse films, with still cutaways for detail states. This is a compact
product study, not a runtime 3D model, a combined vehicle configurator or a sales
backend. React/Vite or another selected frontend can implement the state machine.

Use the polished exterior as the neutral still and the blue drive/battery images
as active details. Keep earlier stills and additional optics imagery available
without inventing unsupported features. Paint and wheel images are independent
render alternatives; do not imply every combination exists. Pair the four authored
hover films by role and direction. Keep image-relative hotspot positions tied to
the same crop transform as the visible car.

Define explicit neutral, hover-forward, hover-reverse, detail and appearance states.
Gate appearance/detail changes until the neutral pose is restored. Wait for useful
decoded frames before switching between stills, canvas and films. Freeze the detail
handoff so the background cannot drift under the cutaway. Lock conflicting actions
during travel, recover from rejected playback and timeouts, and preserve the last
useful still after errors. Rapid input must not trigger stale transitions.

Fit the complete car and essential controls on desktop and short/mobile screens.
Provide tap and keyboard alternatives to hover, visible focus and reachable menus.
Reduced motion must suppress JavaScript film/zoom behaviour as well as CSS animation.
Switch useful stills while preserving every navigation path. Test all hotspots,
appearance options, interrupted transitions, loading failures and repeated Back.

The 20-file manifest contains 18 scene media files and two composition screenshots.
Reference screenshots are comparison aids, not flattened page backgrounds. Keep
aligned media bytes unchanged for exact asset reuse; replacing a still requires
checking every film endpoint. New replacement media defaults to Replicate and must
share camera, crop, light, identity and neutral endpoints.

Mandatory license and third-party notices accompany this pack in
`licenses/electric-vehicle-explorer.txt` in the skill and at the hosted
`LICENSE-NOTICES.txt` alongside this prompt. Carry them into redistributions.
They are an intentional exception to neutral public naming. The top-level package
license does not replace those notices or grant rights to depicted brands/fonts.

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

Use these direct URLs in the implementation. [Machine-readable manifest](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/assets.json)
includes file sizes and SHA-256 hashes. Local manifest: `assets/manifests/electric-vehicle-explorer.json`.

| ID | Role | File |
| --- | --- | --- |
| asset-01 | desktop | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/72f7675e1cf543.png) |
| asset-02 | mobile | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/d716226149d34a.png) |
| asset-03 | battery-blue | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/90e956d525584b.png) |
| asset-04 | battery-hover-forward | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/2092bdd6534a4a.mp4) |
| asset-05 | battery-hover-reverse | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/087cba459ac84e.mp4) |
| asset-06 | battery | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/545b4066544549.png) |
| asset-07 | electric-green | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/1306e84e815645.png) |
| asset-08 | graphite | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/1b5da2ffbc1f42.png) |
| asset-09 | lime-green | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/6a94dcf4b0d544.png) |
| asset-10 | sky-blue | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/f59c5bf239c241.png) |
| asset-11 | wheels-aero | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/b6360b840df84c.png) |
| asset-12 | wheels-forged | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/4eced439fce249.png) |
| asset-13 | drive-blue | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/5e98f4aa575642.png) |
| asset-14 | drive | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/e5ec009c805649.png) |
| asset-15 | exterior-blue | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/4cb449689e4441.png) |
| asset-16 | exterior-polished | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/162e2a3e090740.png) |
| asset-17 | exterior | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/62e06733f83942.png) |
| asset-18 | hood-hover-forward | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/e4a3a0877c9a44.mp4) |
| asset-19 | hood-hover-reverse | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/68aff0db637f4d.mp4) |
| asset-20 | lenses-blue | [Open asset](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/media/93e8de8e5f664d.png) |

[Required notices](https://lapis-slate-xvar.here.now/library/electric-vehicle-explorer/LICENSE-NOTICES.txt).
