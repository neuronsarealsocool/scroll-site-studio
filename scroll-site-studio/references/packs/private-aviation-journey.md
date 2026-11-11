# Private aviation journey

Build a premium private-aviation website on a blue-black ground. Deliver editable components in the existing project stack; the recovered user brief chose React, TypeScript, Vite and Tailwind. Keep shared asset references in one module, the Three.js flight scene in another, and the hero camera controller in a dedicated hook. A framework-free build is also a valid adaptation if requested. Do not flatten the design into an image or iframe. New generated media defaults to Replicate, requires an agreed budget, and must be approved in chat before publication.

## Composition and tokens

Use ink oklch(0.12 0.01 250), raised night oklch(0.16 0.014 250), slate oklch(0.34 0.018 250), mist oklch(0.72 0.018 245), frost oklch(0.95 0.008 240), ice oklch(0.85 0.07 230), deeper ice oklch(0.6 0.1 240) and white hairlines at .12 alpha. Display typography is Forum400, body Red Hat Display400/500/600, labels Red Hat Mono400/500 at11px uppercase with .2em tracking. Horizontal padding is clamp(20px,5vw,72px), easing cubic-bezier(.22,.8,.2,1), pill controls48px high. The page progresses through a full-screen jet, pinned aircraft reel, opening charter film and benefit list, ownership arc, contact over clouds, then footer.

The opening headline is “Quiet, above everything.” with a short arrival-focused description, an “Explore the Jet” action, five view captions and segmented progress. The pearl jet holds straight and level; the camera changes position. Keep the cabin/aircraft silhouette visible against charcoal cloud, with restrained vignette and bottom shading.

## Shared flight scene

Use antialiasing, DPR capped at2, sRGB output and ACES filmic mapping. Background and exponential fog are #05070a with density .03. Build a dark-room PMREM with soft top/side panels. Hemisphere light uses #9fb4cc above #05070a at .35; warm key #fff6ec intensity2.2 at(-6,10,-4); cool rim #9fbadb intensity .7 at(8,2,10). The hero GLB needs Meshopt decoding. Centre its bounding box, turn -90° about Y to point the nose down -Z, and scale the longest dimension to10. Preserve painted windows and normal maps when assigning physical finishes; clearcoat roughness .08 and fog:false prevent cloud fog from erasing the airframe.

Finishes: pearl #e9ecef metal .35/rough .32/clearcoat1; obsidian #1a1d23 metal .6/rough .22/environment2.4; silver #b9bec6 metal .9/rough .26; navy #16223a metal .5/rough .3; bronze #9a7a5a metal .85/rough .3. Keep other material properties consistent unless the mesh requires a separate transparent/glass treatment.

Animate y=.06 sin(2πt/6)+.025 sin(2πt/4), roll=.006 sin(2πt/12)+.0008 sin(2πt/.25), pitch=.004 sin(2πt/6). Clouds comprise150 sprites outside a clear tunnel, |x|7–35, plus70 lower-deck sprites at y-9 to-15. Stream through a160-unit Z box at16units/s, with z=-120+((baseZ+16t) mod160). Fade the first/last12% and the region within about3units of the camera. Tint #5d6672, with brightness .05+1.5 exp(-distance²/1400) around the jet. Produce cloud textures in code from five256px value-noise ellipses, five octaves and alpha d^1.4×.9; avoid visible wrap resets.

## Camera stages and input ownership

Each deliberate gesture advances or reverses exactly one complete2.6second quadratic Bézier move with ease-in-out cubic. The look target interpolates with the same easing. Hold the settled camera until the next fresh gesture.

| View | Camera position | Look target | Via point from previous view |
|---|---|---|---|
| Front three-quarter | 5.6,.3,-12.5 | 3.4,-.5,-1 | initial |
| Side profile | 17,.6,.5 | 0,.1,0 | 15,1.4,-9 |
| Elevated three-quarter | 10,9.5,5 | 0,-.4,-.5 | 16,6,3 |
| Flight deck | 3.1,1,-7.4 | 0,.3,-3.4 | 8,5,-6 |
| Engine and wing | 5.6,2.2,6.8 | 1,.2,1.2 | 5.6,2.4,-1 |
| Wide rear three-quarter | -12,3.6,17 | 0,0,-2.5 | 1.5,4.8,14 |

For portrait screens multiply the distance from each target by min(2.2,1.3/aspect). A fresh wheel gesture follows220ms without wheel events. Ignore momentum and cancel wheel scrolling while the hero owns an active move. At settled stage5, the next downward gesture releases into the page. At stage0 upward input cannot go past the first view. Returning to the top restores control at the current camera stage. Touch uses a40px swipe and cancels only the hero-owned movement. Support ArrowDown/PageDown/Space forward, ArrowUp/PageUp reverse; do not trap focus or prevent form typing.

Settled captions are numbered Profile, Wing, Flight deck, Power and Onward, with one sentence each about level cabin, swept wing, crew/cabin separation, quiet rear engines and the next destination. Display0N/05 and five28×2px segments. Change the helper text between initial exploration, forward/backward views and continuing below. Show download progress with a260px line and remove the loader after the scene is ready; provide a useful fallback when GLB/WebGL fails.

## Aircraft, charter and ownership

Aircraft occupies380vh with a sticky100svh stage. Use heading and01/05 counter at left, a4:5 video-card reel centrally, masked copy at right. Progress p spans0–4; for d=i-p apply y=d×cardHeight×.78, scale=1-min(|d|,1.6)×.2 and brightness=1-min(|d|,1)×.62. Replace right-hand content when round(p) changes, revealing lines upward from105%. The five finishes are obsidian flagship, pearl city jet, silver concept, navy working cabin and bronze family aircraft. Cards tilt up to5°Y/4°X, lift18px and track an edge light. Click or Enter opens a native dialog with its loop, finish, specification sentence and enquiry action.

The charter film is92vh. As it enters, animate inset from9.2vw with28px corners to1.2vw with10px corners. The video is120% high with -8% centre-relative parallax. Headline “Charter on your clock.” leads to a flight enquiry and five ruled benefits: two-hour confirmation, one coordinator, private terminals, departure-local food and inclusive travel. Treat business claims as example copy until confirmed. Beside the list, reuse the hero jet in an80vh top-down canvas, drifting with scroll as its key light moves.

Ownership pairs text with five3:4 cards on a wrapping arc. For active-relative offset d, x=d×width×.78, y=|d|^1.25×34px, z=-|d|×170px, rotateY=-24°d, rotateZ=3°d. Nonactive scale .82; neighbours alpha .55; hide beyond|d|2. Use1second transitions, arrow buttons, left/right keys and40px swipes. Themes: fractional hours, cabin craft, full ownership, care and leaseback. Keep headline/action synchronized with the active card.

## Contact, sound and delivery

Use the cloud-only loop behind contact at55% opacity. Provide Name, Email, Interest chips (Charter/Ownership/General) and Message, with real validation and aria-invalid. Post JSON to an owner-configured endpoint; announce success only on an OK response. Without an endpoint, use a clearly described email-draft fallback and explicitly say nothing has been sent. Never ship invented contact addresses as genuine destinations.

Sound starts only after a visitor enables it. The optional Web Audio design uses55/82.4/110.6Hz pad tones through a260Hz low-pass,520Hz band-pass wind,140Hz low-pass engine noise with a faint2960Hz whine, a260→1500→320Hz whoosh during a move and hover chimes throttled140ms. Master gain eases to .5. Pause/resume appropriately on visibility changes.

Play only the visible feature film, contact background and active reel card with its neighbours; loops are muted, inline, poster-backed and preload:none. Reduced motion removes flight interpolation/float and pauses videos, retaining readable content and direct navigation. Verify five gestures/five moves, sixth-gesture release, reverse navigation, dialogs, form errors/success semantics, ownership keys/swipe, loading failure,1440×900 and390×844 layouts and a reachable footer. Three unused alternative aircraft models remain private optional references and are not required for this working build.

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | card-argent loop | [card-argent loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/ca8ec0f1c17b1e.mp4) |
| asset-02 | card-nocturne poster | [card-nocturne poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/e66c46706fcc2c.webp) |
| asset-03 | card-lumen poster | [card-lumen poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/4121566d9aa4e7.webp) |
| asset-04 | aircraft model hero | [aircraft model hero](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/924230d4f2fdd5.glb) |
| asset-05 | card-lumen loop | [card-lumen loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/de4e74daa1ab0a.mp4) |
| asset-06 | card-argent poster | [card-argent poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/69b330a417a5f3.webp) |
| asset-07 | card-meridian poster | [card-meridian poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/078a04ec9d7b93.webp) |
| asset-08 | card-solace poster | [card-solace poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/f3cc953f8d11ff.webp) |
| asset-09 | card-meridian loop | [card-meridian loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/5ca24fdcb051b7.mp4) |
| asset-10 | own-fractional poster | [own-fractional poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/842fbe5f79ef79.webp) |
| asset-11 | card-nocturne loop | [card-nocturne loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/02db14739bc212.mp4) |
| asset-12 | card-solace loop | [card-solace loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/5ee5fdaa9f8f16.mp4) |
| asset-13 | own-fractional loop | [own-fractional loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/609e05f3a635d1.mp4) |
| asset-14 | own-cabin poster | [own-cabin poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/80d1c84d59096f.webp) |
| asset-15 | own-cabin loop | [own-cabin loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/e376dc5a495e12.mp4) |
| asset-16 | own-full poster | [own-full poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/6906e14a7b9e24.webp) |
| asset-17 | own-full loop | [own-full loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/b47ef676c82501.mp4) |
| asset-18 | own-detail poster | [own-detail poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/1a736423ddcfa5.webp) |
| asset-19 | own-lease poster | [own-lease poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/2d854a71a1076e.webp) |
| asset-20 | own-lease loop | [own-lease loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/3ccaa870be68f6.mp4) |
| asset-21 | charter poster | [charter poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/f4b91570cc0ca3.webp) |
| asset-22 | own-detail loop | [own-detail loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/6df9aebc9d3834.mp4) |
| asset-23 | clouds poster | [clouds poster](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/7f0a87187625ee.webp) |
| asset-24 | charter loop | [charter loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/1f3c28ef8359f4.mp4) |
| asset-25 | clouds loop | [clouds loop](https://lapis-slate-xvar.here.now/library/private-aviation-journey/media/58c644aa06b1fe.mp4) |

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
