# Racing driver profile

Build a responsive driver portfolio with a layered portrait-and-helmet WebGL opening, a race-circuit season panel, a seven-entry career timeline, an editorial paddock report and a dark sign-off framed by cyan. The interaction signature is a helmet that first burns away from crown to chin, then reappears only beneath the moving pointer's liquid trail. A depth photograph remains visible beneath it. The first three content blocks form a sticky stack: each incoming block covers, shrinks and darkens the preceding one. Preserve this grammar in faithful mode; adapt athlete, team and copy only when the user selects adaptation.

Use the existing project stack. A standalone HTML/CSS/JavaScript implementation is sufficient, with an inline module and pinned three.js/Lenis versions; do not require a framework or WordPress. Keep source modules small if the host project already uses React. WordPress is optional. Put all supplied media URLs in one role-based asset map. The full private original contains exact shader bodies, vector paths, circuit samples and halftone coordinates; this independently written working prompt specifies their behavior without redistributing those large implementation bodies. An exact source reconstruction requires the owner's authorized original and its data, rather than claiming a newly generated circuit is identical.

## Design system and data

Use a near-white ground #f7fafb, primary ink #090a0b, panel #0e0f14, raised surfaces #1b1d24/#2a2d36, cyan #02d2e3, pale contours #ebeef1 and rules #dfe5e9. Dark muted copy is #b6c1c8; secondary light-ground copy is black at35%. Map dots/grid/outer rings use #7a7a7a/#4d4d4d/#1e1e1e; timeline outlines #535450 and fills white10%; rail white20%; footer faint text white40%. Keep the theme fixed, with each section choosing its own light/dark surface.

Use Oswald bold uppercase for display names, headings, years and figures, and Space Grotesk uppercase for UI, metadata and body. Nominal sizes are96px name,70px small-name,52px compact display,38px figures,20px action,18px lead/meta,16px nav,14px body,12px eyebrows,55px section heading and36px years. Main heading leading .95, uppercase runs .9 and cap-height figures .72; text reveal wrappers need at least1.1 leading and must not clip descenders. Track figures-.08em, labels-.04em and eyebrows-.02em. Timings:150ms fast UI,250ms normal hover,700ms plate inset. Entrance easing cubic-bezier(.2,0,0,1), plate easing(.33,0,0,1).

The reference dataset is a fictional demo treatment, not verified live sporting information. Use driver ID012, an Italy metadata row, a rookie-season2026 row, a team row, next-race date2026-07-27 and a circuit thumbnail. Hero statistics are12 races,3 podiums and118 points. Season plate showsP1 in the championship,6 wins and9 podiums. Paddock figures areP4 last result,+12 points gained,P1 championship,118 points. Keep these as supplied demo values in faithful mode; verify and replace before presenting them as current facts. Use actual user-approved names and branding rather than implying an endorsement or creating a false copyright notice.

Root size is16px below1280px. At1280–1440 use1.111111vw; at1441–1920 use .833333vw and multiply hero/season type by1920/1440. Above1920 set root pixels to16*width/1920. Timeline/paddock/footer use container query units, `designPx(v)=v/1440*100cqw`. Breakpoints are640/768/1024/1280, with a short-height query at≤500px.

## Shared motion and sticky stack

Use one reference-counted requestAnimationFrame ticker. Register Lenis first with smoothWheel:true and run scroll readers afterward; use native scroll under reduced motion. A subscriber runs only when time-last exceeds its requested interval. Render canvases while in view plus ten frames after exit, and stop them while the document is hidden. A60fps cap is1000/60-2 milliseconds, so120Hz screens land on alternating frames rather than40fps.

Spring state is value/velocity, mass1,1ms integration substeps and64ms frame cap. Rest thresholds are error/velocity .01, or .001 for opacity-like ranges. Keep modes: once never replays after its initial entrance; always reverses when disabled; forward holds its arrived state once scrolled above the viewport. Spring tension/friction pairs: reveal90/26, row/item170/24, sheet190/26, figure200/24, type210/24, year190/24, copy110/26 or150/24, name190/24, veil70/24, clear140/26, label110/26, waiting progress10/30, ready progress170/26, year-settle32/26 and trigger140/30.

Text reveals split into words or letters, each with a spring from opacity0/Y.35em for words or Y.3em for letters to opacity1/Y0. Delay each unit by delayIn+i*stagger. Keep a visually hidden complete string and aria-hide animated fragments. Do not apply an overflow crop that trims low-leading letters. Scroll scrub progress interpolates numbers, unit-bearing values and simple transforms across named top/centre/bottom positions. Timeline row gates use a bottom inset25%; calendar gates20%.

Wrap hero, season and timeline in a relative dark stack. Hero and season are sticky top0 with z0/z10; timeline is relative z20. Transform only each sticky layer's inner wrapper. Derive coverage p=clamp(1-nextBlockTop/viewportHeight); inner scale=1-.1p and dark overlay opacity=.55p. At p0 remove the transform completely so the fixed loading veil remains viewport-relative. At p1 hide the covered inner scene. On phones below640px keep scale1 and shade only. Never create an overflow:hidden ancestor that destroys sticky positioning; use overflow-x:clip where necessary.

## Hero layout, menu and loader

The hero fills100lvh with an absolute full-bleed canvas behind content. From1280px, use an overlay composition: masthead at the top, left identity column(max26.0625rem), right bracket-panel column13.625rem, actions at the bottom, portrait centred behind. Gutters are2rem horizontally and1.5rem vertically, reducing vertical padding to.75rem for short viewports. Desktop masthead navigation stays at the viewport centre, independently of logo and garage action widths.

Below1280px fit the scene subject to a measurable layout-owned box rather than crop the canvas blindly. Below1024px the figure owns the bottom70% of the hero; below640px64%. Identity and panels become a row from768px, otherwise a column; hide the right panels below640px. The lower readability ramp is22% high with opacity stops0/6/20/45/74/93/100% at0/26/46/64/80/91/100%. Below768px a second ramp under the figure spans26rem with its foot13rem below the figure box.

Identity contains a small driver ID, a large name and three icon-labelled metadata rows. The name is96px at desktop,70px at1024–1279 and on small screens, with breakpoint-specific52px where needed to avoid collisions. Right panels use four10px corner brackets without a continuous border. Next race contains event, venue, semantic date and map. Statistics are three figures with12px labels and38px Oswald numerals. The footer row has a trailer action, chamfered profile button and social links; hide trailer/socials below640px and make the profile button full width. Profile frame is220×50 with an8px chamfer, dark fill, cyan quarter-opacity ring and corner accents. Hover floods it cyan from the left over250ms and changes type to black.

Use a two-line burger below1280px. Append its full-screen menu sheet to body, outside transformed ancestors. Include all five section links and the garage action. Lock document scroll and stop Lenis while open; focus the close button, trap focus, close on Escape and restore focus. Close automatically when crossing back above1280px. Reveal links at120+i*55ms using170/24 springs.

The loading veil is fixed z50, near-white, role=status. Centre a7.2×8.5rem helmet silhouette with a faint12% background shell and a top-down progress fill; use one value for that fill and the4px progress meter at the bottom. Progress is a readiness illustration: ease toward.7 with10/30, then toward1 with170/26 when every texture/model/program is ready. Do not label it measured download percentage. Ready clears veil content upward.75rem with140/26;430+240ms later lift the veil with70/24 and begin the page/scene entrance simultaneously. Remove only when rendered opacity≤.004, with3000ms hidden-tab backstop. From ready, the veil must no longer intercept input. Entrance delays relative to handover: masthead0, identity180, panels900 and actions1500ms; meta rows start180+260+i*130ms.

## Portrait and helmet scene

Manifest roles include a Draco-compressed helmet GLB, studio HDR, noise texture, diffuse/depth/alpha/normal portrait maps, loader silhouette, static contour fallback, UI marks, timeline photographs, paddock cutout and footer suit/helmet plates. Configure DRACOLoader explicitly; load HDR with RGBELoader and prefilter through PMREMGenerator. Use anonymous CORS on anything drawn to canvas. Preserve model material textures, front-side rendering, transparency, depthWrite:false and environment intensity1.3. Put a merged helmet-wireframe on the same worn pivot as the solid shell. Preupload textures, compile programs asynchronously and render one warm-up frame before reporting ready.

Hero construction tiers: mobile when width<768 or coarse-pointer width<1024; tablet for other coarse pointers or width<1280; desktop otherwise. DPR caps1/1.25/1.5. Desktop renders every tick with antialiasing; mobile/tablet cap60 and omit antialiasing. Pointer only on fine hover without reduced motion. Trail samples28/44/72; no mobile outline or post-burn reveal. Reduced motion freezes the settled scene after entrance; mobile save-data or≤2GB device memory also freezes. Retune on width or pointer-class changes; ignore height-only changes on coarse pointers so browser chrome does not rebuild the scene. Gate the hero scene after scrollY>1.15*viewportHeight even though its sticky rectangle still intersects.

Use the parameter table below as the baseline. Fit overrides apply afterward: disable backdrop reveal below1024; set touch sweep amount.76; below640 set sweep radius.95, warp.18 and sweep amount.55; finally set sweep amount0 if the tier disables reveal. Fit below1280 to the layout-owned subject box, and shift the subject right.25 world units at1024–1279. From1280 use the full-canvas composition.

The subject rises200 CSS pixels over2 seconds, ease-out quadratic. A4-second intro clock burns the helmet starting at normalized.14: threshold a mixture of55% screen height and45% noise using smoothstep(.14,1,intro), softness.02. Cyan burn glow is4*intact*(1-intact), strength4. Fade wireframe in on the burn curve so a full solid shell and its outline do not coexist.

Afterward reveal the helmet through max(pointerTrail,sweepTrail). Build the pointer trail from weighted capsules along smoothed pointer history, with taper and speed-dependent radius. Threshold at.08±.005; warp coordinates with two scrolling noise fetches at scale2.9, strength1.29. Speed pace attacks.09/releases.205 relative to peak.029 NDC/frame and gates reveal via smoothstep(.06,.21,pace), so a resting pointer leaves no parked helmet blob. The backdrop uses the same mask with alternating linear greys.62/.44. Helmet pitch/yaw amplitudes2.5°/2.1° pass through two cascaded.17 filters, moving as a worn helmet rather than freely rotating. Subject parallax.02; portrait depth parallax.005; normal-map relight.32.

The helmet outline is a soft Gaussian band of width.15 moving crown-to-chin for3.1s, with a new wave each1.2s, maximum opacity.09, color lifted64% toward white. Extend the wave beyond the geometry bounds so its ends fade rather than wrap abruptly. The animated contour backdrop uses a four-sine analytic field, scale3.8,2.5 bands, derivative-based thickness1.4, opacity.85 and crossed displacement amplitude.37/speed1.66. Reuse the same field for the paddock/footer2D marching-squares canvas on a96-cell long-edge grid, drawn at24ms intervals only while visible.

## Season map, lap and chequered joins

The season section is dark, min-height100lvh (680px below640). Put a cyan two-line heading at the left with a white punctuation mark, small rule and supporting season copy. Heading words stagger110ms; lines130ms. Intro words stagger34ms beginning350ms. A277×78 chamfered standings plate sits bottom-right with83px badge cell; its frame arrives260ms and text430ms. Badge globe37×23 spins its meridian over10s. Rows stagger110ms, figures then labels70ms later, letters22ms apart. Keep figure/data values from the demo dataset unless explicitly adapting.

Chequered canvas seams carry the prior block's color into each new section. Their height is34svh, driven from top-at-bottom to top-at-top with140/30 smoothing. Hero→season and season→timeline carry light; timeline→paddock carries dark. They sit above artwork at desktop and behind readable copy on phones. A source-identical chequer pattern needs the retained original generation algorithm, not a generic CSS checkerboard fade.

The circuit has a1440×800 stage. From1024 use cover scale=max(width/1440,height/800), centre it, and mask top/bottom10%. Below1024 fit the track bounding box plus46px padding to width and remove the edge mask. Seat a2560×1440 map at artwork-adjusted dimensions1438.43×809.11 and Y≈-4.559. Canvas DPR cap2, or1 on coarse pointers. Grid axes are x645.31/1276.96/1908.61 and y697.98, overrunning the artboard4000 units; dash12.15/8.35 drifts by20.5 every7s. Hub(1278.48,699.5) has rings69.85/356.06/442.61 and a ping growing10.63→96.63 over4.2s with opacity.4*(1-v)^2.

Use the authorized track ribbon and ordered centreline data when exact reconstruction is requested. Start the lap from the chequered flag, clockwise, once when35% of the stage enters. Duration6000ms ease-in-out sine; pace distance by local path curvature so corners slow and straights accelerate. Draw the head as additive cyan glow plus white filament and illuminate four turn markers as reached. Reveal the same ribbon through a30-unit stroked lap mask, not a disconnected trace. At lap completion cool heat1→0 over800ms ease-out cubic, then arm the pointer reticle; do not replay or reverse the lap.

The map landmass has8004 dots, radius1.75, baked to an offscreen canvas once per resize. Use original lattice data for source fidelity. Only update active lit cells; index them by lattice rows/columns instead of scanning every point. Reticle arms follow the pointer's row and column; lit discs square up from.7 to1 lattice pitch above threshold.34, with alternating lattice parity. Parameters: light radius170,waveSpeed.16,fade.9, default autonomous source none; clamp dt.1. Disable pointer light on touch/reduced motion and clear it on document leave/blur.

## Career timeline

Keep seven photographic entries. Frame1440×2700 begins with169px inset, then no-gap alternating centre462px and side217px rows, ending32px below the final row. Centre plate width710, side333, same stepped-corner outline, image overscan110%. Plate fill insets5% on hover over700ms while outline remains fixed. Side plates sit at their gutter; centre plates at50%. Heading sits top-right on desktop, centred on tablet, left as one row on phone.

| Year | Frame/alignment | Content direction | Centre copy width |
|---|---|---|---|
|2012|centre|First karting experience at age six|228 |
|2015|side/right|Karting trophy photograph|— |
|2019|centre|Joining a junior development programme|272 |
|2021|side/left|Single-seater garage photograph|— |
|2024|centre|Progress through Formula2 and a top-level team announcement|278 |
|2025|side/right|Team garage photograph|— |
|2026|centre|Arrival at top-level racing while retaining home/family ties|284 |

Three parallax planes move via top, not transform: centre plate±20px, side plate±60px, copy±110px over top-at-bottom→bottom-at-top. Image inner travel is-10%→0 during the first half of the row's crossing. Years reveal letter-by-letter,26ms apart with190/24; centre years hold2200ms then settle to opacity.4 using32/26. Copy rises.75rem after220ms using110/26. Hovering a plate dims other rows to.3 over700ms, only on hover devices.

The central rail is16px wide with a1px white progress thread and square marker9px desktop/20px tablet. Rail starts at the block top on desktop and first photograph below1024. Progress ends on the last entry's centre minus50px, not at the section foot, using top-at-centre→bottom-at-bottom. Rotate its square through1800° over the complete run. Below640 remove the rail, make rows natural-height columns with2.5rem gaps, set plates82% wide alternating left/right,40px minimum heading and30px minimum year, and17px minimum copy. Keep bottom150 design pixels desktop, narrower5cqw when applicable.

## Paddock, calendar and sign-off

Paddock returns to light, using a1440×800 composition. Its cutout portrait is102.0363% of section height, x65.6917%, with an upward-only48px parallax travel. The base melts into a169-design-pixel dark calendar band. A96px-style left heading, report and217×50 chamfered story action balance two bracket panels at the right. Meeting panel arrives320ms and its text410; stats panel460ms, rows90ms apart, figure letters24ms. Below1024 panels exchange sides at1px design units and the calendar spreads1.75×; below640 hide those panels and use a1062px natural composition, portrait cap599px/x48.5%/lift328px, then report/action and last-three-round grid. Do not invent a real story endpoint; provide a functioning local article or authorized destination.

| Round | Event | Date | Result/state |
|---|---|---|---|
|11|Austrian GP|29 Jun|P6 |
|12|British GP|12 Jul|P4 |
|13|Belgian GP|27 Jul|Live |
|14|Hungarian GP|03 Aug|Upcoming ring |
|15|Dutch GP|31 Aug|Upcoming ring |

Calendar cards rise at560+i*90ms, event names110ms later. Dashed connectors crawl toward the live round with5200ms period. Live marker radius5.5 pulses outward3.4 times that radius over3200ms; opacity.5*(1-v)^2. Accent brackets widen5 design pixels on hover. On phones show only three final rounds, no connectors, markers, brackets or pulse.

The footer is cyan with a dark panel inset16 design pixels. Put white10% animated contours behind a suit plate and helmet plate. The figure belongs to the section, outside the inset panel, hanging beyond the lower edge; its parallax finishes exactly at bottom-at-bottom, moving60px→0. Mask the suit to show only its lower portion (transparent69%, opaque72%) so its own exported head stays behind the separate helmet. Suit height96.078%, bottom-1.225%, aspect1.15902; helmet top1.25%,height83.364%,aspect1.5. A source-approved logo mask at top-left fills cyan; top-right headline and left navigation use the same display grammar. Navigation letters arrive at260+i*80ms, foot row at640/720/800ms. Legal action275×50 is hollow with a cyan hover flood. Replace fictional legal/copyright labels with the actual owner and working links; preserve any required third-party license notices separately.

At640–1023 footer height104cqw and figure scale.87/shift3%; below640 footer680px,24px gutters,30px navigation, full-width50px legal button and no figure or large headline. Every scene/model/image failure must name the missing role and allow reading/navigation. Without WebGL, show approved static contours and diffuse portrait in the fitted subject box, and lift the loader immediately. Test loading/cached loading, model decode failure, coarse-pointer tier switching, reduced motion, scroll reversal at every stack join, phone landscape, menu focus and real action destinations. Never call browser-emulation verification a physical-phone test.

## Baseline scene parameters

The following values preserve the measured scene tuning. Later layout and device overrides apply in the order described above.

| Parameter | Value |
|---|---|
| cameraZ | 6.5 |
| subjectScale | 1.15 |
| subjectX | 0 |
| subjectY | 0.42 |
| subjectParallax | 0.02 |
| riseDistance | 200 |
| riseDuration | 2 |
| headScale | 0.8 |
| headY | 0.58 |
| headParallax | 0.005 |
| headRelight | 0.32 |
| helmetScale | 0.69 |
| helmetX | -0.08 |
| helmetY | 0.45 |
| helmetZ | 0 |
| helmetFollow | 0.01 |
| helmetAmpX | 2.5 |
| helmetCurveX | 0 |
| helmetAmpY | 2.1 |
| helmetCurveY | 0 |
| helmetBrightness | 1 |
| trailRadius | 0.46 |
| trailIdleScale | 0.28 |
| trailTaper | 1.9 |
| trailTaperIdle | 1.6 |
| trailTaperFast | 1.25 |
| trailLength | 0.64 |
| revealThreshold | 0.08 |
| revealEdge | 0.005 |
| revealWarp | 1.29 |
| revealWarpScale | 2.9 |
| revealSpeed | 1.25 |
| pointerLerp | 0.17 |
| pacePeak | 0.029 |
| paceAttack | 0.09 |
| paceRelease | 0.205 |
| paceThreshold | 0.06 |
| paceRamp | 0.15 |
| outlinePeriod | 3.1 |
| sweepWarp | 0.86 |
| sweepLength | 0.67 |
| sweepRadius | 0.33 |
| outlineStagger | 1.2 |
| outlineOpacity | 0.09 |
| outlineWidth | 0.15 |
| outlineBase | 0 |
| outlineLightness | 0.64 |
| bgLineScale | 3.8 |
| bgLineCount | 2.5 |
| bgLineThickness | 1.4 |
| bgLineOpacity | 0.85 |
| bgWaveAmount | 0.37 |
| bgWaveSpeed | 1.66 |
| bgRevealLightness | 0.62 |
| bgRevealLightnessAlt | 0.44 |
| bgRevealOpacity | 1 |
| introDuration | 4 |
| burnStart | 0.14 |
| burnSoftness | 0.02 |
| burnGlow | 4 |
| autoSweepAmount | 0 |
| autoSweepPeriod | 5 |
| autoSweepStroke | 0.45 |
| autoSweepHold | 0 |

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | reveal noise | [reveal noise](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/52f6706ecfb274.webp) |
| asset-02 | portrait depth | [portrait depth](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/83832ddaea1b33.webp) |
| asset-03 | studio environment HDR | [studio environment HDR](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/7d1ca2300066e8.hdr) |
| asset-04 | Draco-compressed helmet, embedded baked PBR maps | [Draco-compressed helmet, embedded baked PBR maps](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/3b96e1c0d82427.glb) |
| asset-05 | portrait color | [portrait color](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/216aed48ad2a34.webp) |
| asset-06 | portrait normals | [portrait normals](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/1af8da56084baa.webp) |
| asset-07 | masthead logo | [masthead logo](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/a56bd92d0ae46c.webp) |
| asset-08 | country flag | [country flag](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/bf8d50fea02639.webp) |
| asset-09 | rookie mark | [rookie mark](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/a851a6d1838080.svg) |
| asset-10 | team mark | [team mark](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/800d9ebf526d77.webp) |
| asset-11 | next circuit | [next circuit](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/13775f6b41e5d4.webp) |
| asset-12 | portrait alpha | [portrait alpha](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/78cf2af686268b.webp) |
| asset-13 | trailer cue | [trailer cue](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/4b53d643a5ac0c.svg) |
| asset-14 | loader helmet mask | [loader helmet mask](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/8e94e804bad9f3.png) |
| asset-15 | stat icon flag | [stat icon flag](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/474b3ad6b23044.svg) |
| asset-16 | stat icon bars | [stat icon bars](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/d13beb88e35770.svg) |
| asset-17 | no-WebGL contour fallback | [no-WebGL contour fallback](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/b18b0d3e6319f3.svg) |
| asset-18 | paddock portrait | [paddock portrait](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/32834d009b9b72.webp) |
| asset-19 | stat icon trophy | [stat icon trophy](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/5c46ffeb9b5169.svg) |
| asset-20 | stat icon gauge | [stat icon gauge](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/35629e47875db5.svg) |
| asset-21 | career plate 2019 | [career plate 2019](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/1a3846da30b1af.webp) |
| asset-22 | career plate 2012 | [career plate 2012](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/5acd555b050c5c.webp) |
| asset-23 | career plate 2021 | [career plate 2021](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/6ccf86c8cbbf3e.webp) |
| asset-24 | career plate 2015 | [career plate 2015](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/ed3f0cba149669.webp) |
| asset-25 | career plate 2024 | [career plate 2024](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/7b9cf5ee6b63d7.webp) |
| asset-26 | career plate 2025 | [career plate 2025](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/52a472d83be23d.webp) |
| asset-27 | footer wordmark mask | [footer wordmark mask](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/7d49ab56889c2b.png) |
| asset-28 | career plate 2026 | [career plate 2026](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/8088e8f69e9e72.webp) |
| asset-29 | footer helmet cutout | [footer helmet cutout](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/2f6bc45ff1c267.webp) |
| asset-30 | footer suit cutout | [footer suit cutout](https://lapis-slate-xvar.here.now/library/racing-driver-profile/media/c8c3ea7953e135.webp) |

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
