# Curved film archive

Build **The Film Room**, a polished, responsive film archive presented as a single-screen shelf of twelve fictional VHS releases. Use this specification as a complete working prompt. The defining composition is a deep, curved row of narrow tape spines with one illustrated front cover facing the viewer at the centre. Selecting a neighbouring spine brings that tape forward, turns its cover towards the viewer, updates the caption and moves a marker along a year ruler. Opening the selected cover expands a paper detail sheet from the cover's actual projected rectangle. Its poster appears through an irregular, spreading ink mask.

For a fresh implementation, use a single HTML document with inline CSS and vanilla JavaScript. No framework, animation library or backend is necessary. Retain an existing project's stack when integrating this experience. WordPress is optional and must not be inferred from the choice of reference pack. Keep the visual composition, twelve-film dataset, sprite crops, arc geometry and interaction timings below in faithful mode. In adapted mode these mechanics can support books, records or another collection, but recalculate the dimensions and sprite crops for that medium. This pack's faithful example is VHS, not vinyl.

## Visual composition

Fill the viewport with warm paper. Place the archive's small cobalt identity and navigation at the top. Across the middle, the tapes form a shallow bowl: far spines sink slightly, recede, darken and compress towards both edges. There should be roughly eleven visible spines to either side when the viewport permits. The selected case rotates by 90 degrees, exposes its full front and projects slightly forward. A soft, low shadow grounds the row.

Behind the tapes, place two oversized vertical columns of screened Japanese lettering: `映画` on the left and `の記憶` on the right. Below the active cover, show its cobalt title, romanised and Japanese titles, a small rule, and its year and genre. Previous and next controls flank the title on desktop. Near the bottom, a fine ruler spans 1955–1990 and carries a small cobalt selection dot. Keep the composition open and precise; do not add marketing sections, gradients behind text, rounded cards or a conventional thumbnail grid.

Use one `requestAnimationFrame` loop for continuous geometry, spring movement, cursor following and ink-mask radii. Use the Web Animations API for caption masks and sheet/text transitions. Reveal content through translation inside masks, clipping and scale. Do not replace the specified reveals with opacity fades.

## Supplied sprite sheets

The complete visual collection comes from four approved WebP sheets. Use these direct, self-hosted URLs. Do not generate substitute artwork or assume that each film has its own image file.

| Sheet key | Pixel dimensions | Contents | Direct URL |
|---|---|---|---|
| `covers` | 1744 × 2336 | Twelve fronts arranged in four columns and three rows | https://lapis-slate-xvar.here.now/library/curved-film-archive/media/d12de9fb113a52.webp |
| `spines` | 2688 × 1152 | Main row of twelve narrow spines; nine crops used | https://lapis-slate-xvar.here.now/library/curved-film-archive/media/bef5d7e9e251fd.webp |
| `fix` | 1520 × 2688 | Replacement River of Salt spine | https://lapis-slate-xvar.here.now/library/curved-film-archive/media/1d302b88229f3e.webp |
| `fix2` | 1520 × 2688 | Replacement Observer and Light in the Storm spines | https://lapis-slate-xvar.here.now/library/curved-film-archive/media/906f9a9a8b2cd8.webp |

The illustrated faces have worn paper, condensed display lettering, duotone imagery, cobalt, vermilion, black and cream. Use the approved pixels unchanged. Text embedded inside the artwork is part of those pixels; neutral interface branding does not require erasing it. Retain required legal notices. Hosting a copy does not confer ownership or additional usage rights.

Create a sheet dictionary containing each URL and its original width and height, and a crop dictionary keyed by `spine-<film-id>` and `cover-<film-id>`. Each crop is `[sheetKey, x, y, width, height]`, in original sheet pixels.

| Film ID | Spine key | Spine x,y,w,h | Front key | Front x,y,w,h |
|---|---|---|---|---|
| valley | spines | 266,31,189,1089 | covers | 497,72,344,659 |
| bluehour | spines | 492,31,189,1089 | covers | 914,72,342,659 |
| river | fix | 197,54,324,2566 | covers | 1332,72,344,659 |
| summer | spines | 937,31,188,1089 | covers | 74,813,344,676 |
| green | spines | 1157,31,185,1090 | covers | 497,815,344,674 |
| noon | spines | 44,32,184,1088 | covers | 74,72,347,659 |
| observer | fix2 | 371,15,349,2655 | covers | 915,815,342,675 |
| birds | spines | 1573,31,183,1089 | covers | 1331,815,345,675 |
| storm | fix2 | 808,15,347,2656 | covers | 74,1571,345,681 |
| tide | spines | 2012,31,188,1089 | covers | 496,1577,343,678 |
| war | spines | 2236,31,189,1089 | covers | 913,1579,343,676 |
| door | spines | 2462,31,188,1089 | covers | 1331,1579,344,677 |

For sheet dimensions `W × Hs` and crop `(x,y,w,h)`, apply the following CSS background calculations. These are normalized to the remaining image extent, not simply `x/W` and `y/Hs`.

```text
background-size: (W / w * 100)% (Hs / h * 100)%
background-position: (x / (W-w) * 100)% (y / (Hs-h) * 100)%
```

The detail poster uses an SVG viewport and clipping rectangle of 474 × 900. Place its sheet `<image>` at `x=-x*474/w`, `y=-y*900/h`, with `width=W*474/w`, `height=Hs*900/h` and `preserveAspectRatio="none"`. This reproduces the same crop in the poster's coordinates. Do not put an entire uncropped sheet inside a cover or a poster.

Preload all four sheets with `Image` objects. Wait for successful load/decode before replacing the loading state with the completed shelf. A failed sheet must produce a legible, named fallback face and an actionable retry message; it must not leave an endless loader or a completely blank archive. Keep the selected film's metadata available even if its art cannot load.

## Typography and tokens

Self-host the fonts and retain their licenses. A single-file delivery can embed the font bytes as base64 WOFF2 in `@font-face` rules. Keep fonts outside CSS sprite coordinates: the asset art already contains its own display lettering.

| Family | Weight/style | Application |
|---|---|---|
| Inter Tight, variable 100–900 | 500 and 600 | Navigation, labels, titles, years, controls and metadata |
| Newsreader, variable 200–800 | Roman 400 and italic 400 | Detail synopsis and secondary italic line |
| Noto Sans JP | 500 | Small Japanese text; second family in the sans stack |
| Noto Sans JP Big | 800, subset containing `映画の記憶` | Large decorative kanji; use `font-display:block` for this subset |
| Noto Serif SC | 700 | Optional compatibility embedding; it has no visible role in this composition |

The sans stack is `"Inter Tight","Noto Sans JP",system-ui,sans-serif`. The serif stack is `"Newsreader",Georgia,serif`. Ensure Japanese glyphs render correctly, including the large decorative characters; do not ship missing-glyph boxes while claiming font fidelity.

```css
--paper:#ECE8E0;
--sheet:#F3F0EA;
--ink:#141414;
--muted:#6D6A63;
--cobalt:#1F3FB0;
--rule:rgba(20,20,20,.9);
--ease:cubic-bezier(.2,.8,.2,1);
--H:min(47vh,33vw);
--cy:41%;
```

The main document has a paper background, hidden viewport overflow and antialiased text. Avoid accidental text selection during a shelf drag; keep reading text and useful metadata selectable in the detail view. Hide the ordinary pointer only on fine-pointer devices when the working custom cursor is present. Preserve it for coarse pointers, failed initialization and accessibility fallbacks.

Use a shared `.lbl` style: Inter Tight 600, 10.5px, line-height 1, letter-spacing .14em, uppercase. A small boxed label is an inline flex box, 21px high, with 8px horizontal padding and a 1px dark rule.

Cover the composition with a fixed, pointer-transparent grain layer at z-index 40, multiply blend and opacity .6. Use a repeating 220px SVG tile with `feTurbulence` type `fractalNoise`, base frequency .85, three octaves and stitched tiles. Its color matrix rows are `0 0 0 0 .45`, `0 0 0 0 .42`, `0 0 0 0 .38`, `0 0 0 .22 0`. The grain is decorative and must not intercept input or enter the accessibility tree.

## Desktop placement

Use fixed viewport placement for the archive stage. Measure the actual resolved `--H` through a probe element with `height:var(--H)` so CSS and JavaScript remain in agreement after resizing. Convert `--cy` to the corresponding viewport Y coordinate before calculating transforms.

### Header and large lettering

The top bar is 76px high with 36px side padding, cobalt text and space between its two groups. On the left, arrange a home control labelled `THE FILM ROOM`, a 40 × 1px line and `FILM ARCHIVE`, with 16px gaps. On the right, arrange `FILMS`, `ABOUT`, `JOURNAL` with 34px gaps and a 26 × 12px menu button built from two 1.5px lines.

Make these controls meaningful. Films returns to the shelf or closes an auxiliary panel. About opens concise archive information. Journal opens an actual local reading panel or entry list. The menu exposes the same destinations on smaller screens. Do not ship `href="#"` links that silently do nothing. Use the neutral interface identity consistently, including inside the detail sheet.

The kanji columns sit behind the tapes at z-index 1, use `writing-mode:vertical-rl`, the large subset font at weight 800, size `min(19vh,12.5vw)`, line-height 1.02 and letter-spacing .02em. Put `映画` at left 2.4vw/top 13vh and `の記憶` at right 2.4vw/top 9vh. Clip the following layered background into transparent text: a repeating 3 × 3px radial dot, `rgba(64,82,138,.55)` from 0–36% and transparent from 40%, over a flat `rgba(110,122,160,.26)` wash. Mark both columns as decorative.

### Shelf, faces and grounding

Centre the floor shadow at Y `cy+.47H`. Its width is `min(96vw,3.6H)` and its height is `.26H`. Use `radial-gradient(50% 50% at 50% 40%, rgba(40,32,20,.30), rgba(40,32,20,.10) 55%, transparent 72%)`.

The full-width shelf starts at `cy-H/2-50px`, has height `H+100px`, perspective 1400px with origin 50% 50%, z-index 10 and `touch-action:pan-y`. A zero-sized, centred stage and every zero-sized tape node use `transform-style:preserve-3d`.

Each tape has two faces of height H with their top at `-H/2`. Centre their widths around the tape's local origin. Use 2px radii and hidden back faces. The narrow spine has width `ws` and transform `translateZ(d/2)`. The broad front has width `d` and transform `rotateY(90deg) translateZ(ws/2)`. The front's shadow is `0 34px 60px -30px rgba(20,16,10,.6)`. Add a black `::after` shading layer to each face, controlled by its own `--shade` value. Decorative faces must not add duplicate keyboard stops.

Put a 42px circular open affordance near the active cover's lower-left corner: X `W/2-d/2-6`, Y `cy+.36H`. Give it a 1px cobalt border, `rgba(236,232,224,.8)` fill and a 12px cobalt triangle. It opens the film's detail sheet, not an imaginary video player. Its accessible name must communicate that action.

### Caption, arrows, ruler and footer

Centre a caption grid at Y `cy+H/2+4.2vh`, with a 10px gap. Its line masks have a responsive width capped at 640px and constrained to 80vw. The title is cobalt Inter Tight 600, `clamp(28px,3.4vw,46px)`, tracking -.015em. Below it, show `ROMAJI / Japanese title` in cobalt at 9.5px, weight 600 and .24em tracking. Follow it with a centred 18 × 1px cobalt rule, then the ink year/genre line at 10.5px, weight 500 and .08em tracking. Use `YEAR — GENRE` and uppercase the genre visually.

Place two 44px arrow buttons on the title's line at centre X plus or minus `min(19vw,250px)`. Their 24 × 12px SVGs have a 1.2px cobalt stroke; the left path is `M6 1L1 6l5 5M1 6h23`, and the right is its mirror. Give them explicit previous/next labels, visible keyboard focus and adequate touch targets.

The ruler has 36px side gutters, bottom offset 64px and height 40px. Draw its 1px cobalt line 12px from the top at .75 opacity. Include every year from 1955 through 1990. Ticks at multiples of five are 13px tall at .75 opacity; other ticks are 7px at .4. Major labels use Inter Tight 500, 9.5px, cobalt, below the rule. Left-align 1955 and right-align 1990. The selection dot is 9px and cobalt. The whole intended ruler hit area should respond to selecting a year without requiring a click on a 1px line.

Place a small cobalt footer 36px from both sides and 24px above the bottom. Use a truthful demo/collection line such as `THE FILM ROOM / FICTIONAL FILM COLLECTION`. Do not claim ownership of the artwork or offer dead social links. If social controls are included, connect them to actual destinations or use clearly labelled local information actions.

## The collection

Use the following shelf order and structured fields: ID, display title, romanised title, Japanese title, release year, genre, duration in minutes and synopsis. The works are fictional; these descriptions do not imply that full films are supplied. The initial selected record is index 5, Noon in Ashes.

| Index | ID | Title | Romanised title | Japanese title | Year | Genre | Minutes | Synopsis |
|---|---|---|---|---|---|---|---|---|
| 0 | valley | The Silent Valley | SHIZUKANA TANI | 静かな谷 | 1958 | Drama | 104 | A teacher comes home to the valley that forced her family away. Her search for an explanation uncovers an agreement the villagers still refuse to discuss. |
| 1 | bluehour | The Blue Hour | AO NO TOKI | 青の刻 | 1962 | Romance | 97 | As evening settles over the docks, a bereaved woman and a passing traveller invent new lives for one another. Dawn threatens their fragile arrangement. |
| 2 | river | River of Salt | SHIO NO KAWA | 塩の川 | 1964 | Drama | 121 | Brothers guide a heavily laden barge towards a city transformed in their absence. Each bend in the river brings a different account of what awaits them. |
| 3 | summer | The Last Summer | SAIGO NO NATSU | 最後の夏 | 1966 | Drama | 109 | With their village marked for flooding, three friends spend a final season deciding which memories to carry away and which to leave beneath the water. |
| 4 | green | The Green Road | MIDORI NO MICHI | 緑の道 | 1969 | Mystery | 101 | A forest survey leads a solitary mapmaker along a trail that seems to predict his movements. The tracks ahead begin to resemble his own. |
| 5 | noon | Noon in Ashes | HAI NO SHOGO | 灰の正午 | 1971 | Western | 112 | An old obligation sends a rider across a bleached desert. At the end of the journey, the identity of the person demanding payment changes everything. |
| 6 | observer | The Observer | KANSATSUSHA | 観察者 | 1973 | Thriller | 96 | During his overnight rounds, a guard discovers signs that someone knows his route before he takes it. Soon the building itself becomes his chief suspect. |
| 7 | birds | The Fallen Birds | OCHITA TORI | 落ちた鳥 | 1975 | Drama | 118 | Birdsong disappears from a remote settlement, and its residents accept the silence. The mayor's daughter follows the absence beyond the town's familiar boundaries. |
| 8 | storm | Light in the Storm | ARASHI NO HI | 嵐の灯 | 1978 | Drama | 127 | A keeper and his son shelter an unidentified sailor as a storm isolates their lighthouse. Across three nights, the stranger's story grows harder to believe. |
| 9 | tide | The Long Tide | NAGAI SHIO | 長い潮 | 1981 | Drama | 99 | A fishing boat misses its return, leaving a woman to measure the wait against the harbour's rising water. The town gradually changes around her vigil. |
| 10 | war | A Quiet War | SHIZUKANA SENSO | 静かな戦争 | 1985 | Comedy | 103 | A garden wall divides two households locked in a decades-long contest of tiny retaliations. Neither side can quite remember the first offence. |
| 11 | door | Red Door | AKAI TOBIRA | 赤い扉 | 1989 | Thriller | 114 | On a cinema's last night, its projectionist discovers an unfamiliar reel. Following its clues leads through rooms that do not appear on the building's plans. |

Render three copies of the twelve records, creating 36 virtual tape nodes. A node's virtual index is `v=copy*12+i`. Start both the displayed shelf position `s` and target position `T` at `17`, which is `12+5`. Use data-driven rendering rather than separately maintained captions and faces.

## Exact arc geometry

Measure H after font/layout initialization and on relevant viewport changes. Let W be the viewport width, `cy` the shelf centre Y coordinate, and P the shelf perspective. The symbols below are independent of CSS pixel dimensions of the source sheets.

```text
ws = H * 142/840
d = H * 474/900
gap = H * .035
U = H * 1.3                  desktop
U = H * 1.05                 viewport width below 768px
P = 1400
```

The relative virtual index is wrapped into `[-18,18)`:

```text
r = mod(v-s+18,36)-18
mod(a,n) = ((a % n)+n) % n
B(r) = (r+sin(PI*r)/PI)/2    when abs(r)<1
B(r) = sign(r)*.5            otherwise
u = r*(ws+gap)+(d-ws+1.4*gap)*B(r)
sc = 1/(1+(abs(u)/U)^1.6)
```

The extra B term opens a smooth gap for the turning front rather than letting its neighbours collide. Compress screen-space X with an integral of the scale function. Precompute `XS` from zero to `3U` in 2px increments, accumulating `2/(1+(u/U)^1.6)`. Obtain `xsc(u)` by looking up/interpolating `XS[abs(u)/2]` and applying the sign of u. Recompute this table after H or U changes. Do not use a straight, uniformly spaced row as a substitute.

For every visible tape on every frame:

```text
smoothstep(a) = a*a*(3-2*a)   for a clamped to [0,1]
o = smoothstep(max(0,1-abs(r)))
hide node when abs(u)>U*1.95
k = 1/sc
z = P*(1-k)+o*H*.1
x = xsc(u)*k
y = (H*.5*(1-sc)*.42+o*H*.012-lift*H*.05)*k
rotateY = sign(u)*min(1,abs(u)/U)*26*(1-o)-90*o+tiltY*o
rotateX = tiltX*o
transform = translate3d(x,y,z) rotateX(rotateX deg) rotateY(rotateY deg)
z-index = round(3000+z)
spine shade = min(.6,o*.55+(1-sc)*.32)
front shade = (1-o)*.82
```

`o=1` gives the selected front and `o=0` gives a spine. For a hovered non-active tape, meaning `abs(r)>.5`, ease its lift towards 1 with `1-exp(-12*dt)`; otherwise ease it towards zero. Keep nodes outside the cutoff noninteractive and hidden from assistive technology. Avoid forced layout reads inside the per-tape loop.

## Motion and selection state

Use delta time in seconds and cap it at .05. The shelf uses exponential interpolation:

```text
s += (T-s)*(1-exp(-rate*dt))
rate = 5.2                   normal movement
rate = 18                    while dragging
```

Rebase s and T by matching whole twelve-film loops when the position drifts beyond four loops, preserving their difference and the displayed sequence. The active record is `mod(round(s),12)`. Change the caption only when this record changes; derive slide direction from `sign(T-s)` with a stable fallback for direct/snap selections.

Calculate the ruler year by interpolating between the records at `floor(s)` and `floor(s)+1`. Across the 1989-to-1958 seam, switch years at the half-step rather than sweeping the dot backwards across every intermediate year. Ease the displayed marker at `1-exp(-14*dt)`; jump immediately when the difference exceeds six years. Its horizontal fraction is `(year-1955)/35`.

Enable active-cover tilt only when the pointer is within `.55d` of viewport centre X and `.55H` of cy, the shelf is settled to `abs(T-s)<.3`, and no detail/panel is open. In that region, target `tiltY=(mx-W/2)/(.55d)*8` degrees and `tiltX=-(my-cy)/(H/2)*5` degrees. Elsewhere target `tiltY=(mx-W/2)/W*4` and `tiltX=0`. Ease both using `1-exp(-7*dt)`. Disable decorative pointer tilt for coarse pointers and reduced motion.

The lower-left open ring has scale `smoothstep(max(0,1-abs(T-s)*3))`; set its scale to zero while the detail sheet is open.

## Input behaviour

- Clicking a non-active tape selects its nearest equivalent position by setting `T=round(T+r)`. Clicking the settled active cover opens its detail. Suppress click activation after a drag.
- Previous and next arrow buttons step by one. Left and right keyboard arrows provide the same movement when the archive owns keyboard navigation. Enter opens the selected film. Escape closes the topmost open panel or detail.
- A pointer drag begins only after movement exceeds 5px. Retain the starting target `T0` and set `T=T0-dx/(ws+gap)`. Snap T to its nearest integer on release. Handle pointer cancellation and release capture cleanly. A vertical gesture must remain usable for scrolling a mobile detail.
- Wheel movement uses whichever of deltaX/deltaY has the larger absolute magnitude, adds `delta/(ws+gap)*.5` to T, and snaps after 160ms without a new wheel event. Normalize non-pixel wheel delta modes. Do not navigate the shelf or prevent detail scrolling while any detail or auxiliary panel is open.
- Clicking the ruler maps its X coordinate to a year, finds the nearest record year, and selects the shortest path around the twelve-record loop. Clamp pointer coordinates at the endpoints. Give keyboard users equivalent year/record selection through semantic controls.

Do not let global shortcuts intercept typing or activate underlying archive controls while a modal is open. Keep one authoritative collection selection so caption, poster, ruler, accessible name and highlighted state cannot disagree during quick navigation.

## Caption transition

Each caption line is a clipped mask. On a record change, append the new text span over the existing one and translate it from `dir*105%` vertically to zero. Move outgoing spans from their current computed transform to `-dir*105%`, then remove them. Use 650ms, `cubic-bezier(.2,.8,.2,1)` and `fill:both`. During rapid stepping, cancel or supersede existing transitions without leaving orphaned spans or exposing all captions at once. Do not fade text. Announce the selected title/year through a restrained live region after selection settles, not on every animation frame.

## Full-screen detail sheet

Use a fixed sheet with `--sheet` background, z-index 60 and a true closed/hidden state. Desktop content is a two-column grid with a 4vw gap and padding `110px 6vw 56px 7vw`. Place a boxed `CLOSE / 閉じる` control at left 36px/top 28px. Put the cobalt archive identity at top right. Give the sheet dialog semantics and label it with the selected title.

Vertically centre the text column, cap it at 520px and use an 18px gap. Put every entrance-animated item inside a separate overflow mask, in this order:

1. Cobalt romanised/Japanese subtitle using `.lbl`.
2. Cobalt Inter Tight 600 title at `clamp(44px,5.2vw,80px)` and -.03em tracking.
3. Muted year, genre and runtime: `YEAR / GENRE / N min`.
4. Newsreader roman synopsis at 17px/1.5 and max-width 42ch.
5. Newsreader italic muted collection note, such as `A fictional release from The Film Room collection. 監督作品`.
6. A 44px cobalt-outline film-availability action.

No full films or trailers are included with these sheets. In this build label the final action `FILM NOT AVAILABLE / 本編未公開` or an equally clear unavailable state and provide readable explanatory text. Do not create a fake playable video, a dead watch link or an alert pretending that a film has been opened. A later authorized film URL may replace this state without changing the sheet layout.

The right column holds the poster SVG with `viewBox="0 0 474 900"` and a height capped at `min(100%,78vh)`. Apply the supplied front crop, not the spine. Use a rectangular clip for the poster bounds and a second mask for the ink reveal. Distort a group of seven white mask circles with an SVG filter: `feTurbulence` type `fractalNoise`, base frequency .011, three octaves, seed 7, feeding a displacement map with scale 120 and R/G displacement channels.

| Circle centre X | Centre Y | Additional delay in ms |
|---|---|---|
| 150 | 330 | 0 |
| 340 | 600 | 120 |
| 250 | 120 | 220 |
| 90 | 760 | 300 |
| 400 | 250 | 360 |
| 260 | 860 | 420 |
| 230 | 470 | 180 |

### Open sequence

Snap the selection target to its current intended record, fill all detail fields and point the SVG image at the correct cropped sheet. Reset all mask-circle radii to zero. Read the projected bounding rectangle of the actual front face with `getBoundingClientRect()` after its geometry has been updated. Derive viewport inset distances from that rectangle.

Show the detail sheet and animate its clip path from `inset(top right bottom left round 3px)` to `inset(0 round 0)` over 1050ms using `cubic-bezier(.76,0,.18,1)`. The initial paper rectangle must align with the selected cover; a generic centre-screen scale is not equivalent.

Animate the six text items upwards from `translateY(110%)` to zero over 900ms, with delays `620+i*75` ms. At 520ms plus each circle's additional delay, grow that circle's radius from zero to 720 over 1250ms using ease-out cubic, `1-(1-t)^3`. Update radii through the existing animation loop; do not start another permanent rAF loop.

Move focus into the dialog, keep Tab/Shift+Tab within it and make the underlying stage inert while it is open. Preserve a reference to the opener for focus restoration. Allow Escape and the close button to work during the entrance as well as after it.

### Close sequence

Read the current selected cover rectangle again, including after a viewport resize. Animate the sheet clip from full-screen back to that rectangle over 850ms with the same sheet easing. Then hide it, cancel outstanding text/clip animations, reset reveal state and restore the underlying stage. Restore focus to the opener or the selected cover's accessible control if the original opener is no longer present. Guard rapid open/close actions against stale completion callbacks.

## Fine-pointer cursor

Use the custom cursor only on a fine pointer after successful initialization. It is a fixed 58px element at z-index 100, pointer-transparent and hidden from the accessibility tree. Compose a 1.5px ink ring, a 6px ink dot, and a hidden white two-line `OPEN / 開く` label in Inter Tight 600 at 10px. Ease its displayed location towards the pointer at `1-exp(-16*dt)`.

Over the settled, openable cover, scale the ring to 1.75, fill it cobalt and reveal the label by scale/clip. Over an inactive spine, use scale .72. Over a button, link or the ruler, use scale .55 and hide the centre dot. Ring-transform timing is .5s; colour and dot changes .4s; label movement .45s. Reset correctly when the pointer leaves the viewport, opens a dialog or changes pointer type. Visible keyboard focus must remain independent of this decoration.

## Phone composition, 767px and below

Use `--H:min(68vw,40svh)` and `--cy:43%`, with the smaller depth-falloff U specified above. The composition is deliberately rearranged rather than merely scaled down.

- Make the top bar 60px high with 16px side gutters. Hide the desktop text navigation, retain a usable menu button and shorten the divider to 22px.
- Set the large kanji to 22vw and opacity .8. Keep it behind the artwork, not behind essential small labels.
- Use a 27px caption title. Place the arrow controls at the screen edges, 118px above the bottom, leaving the title centred and readable.
- Give the ruler 16px side gutters and a 54px bottom offset. Hide alternate major year labels to prevent collisions while preserving all tick marks and navigation.
- Reflow the detail into one scrolling column. Put the poster first at 46svh, followed by the text; use a 42px detail title. Keep the close action reachable, support normal vertical scrolling and accommodate safe-area insets without clipping content.
- Remove the custom cursor and decorative pointer tilt. Horizontal finger movement scrubs the shelf; a tap opens the selected cover. Preserve the drag threshold so a swipe does not open a film accidentally.

Recalculate geometry on viewport changes. Check short landscape viewports, mobile browser chrome changes and narrow widths as well as a tall phone. Essential navigation, caption and ruler must not overlap. When viewport height is insufficient, choose a smaller responsive shelf or allow an accessible overflow treatment rather than hiding controls outside the screen.

## Reduced motion and accessibility

Respect `prefers-reduced-motion` on load and if it changes. Set the shelf position directly to its target, make hover lift immediate, remove decorative tilt and cursor lag, replace caption slides with immediate swaps, and use 1ms sheet/text transitions. Treat the ink animation as already five seconds old so the complete poster is immediately visible. Keep the alternate presentation fully functional, not an inert poster.

Use semantic buttons and navigation, readable accessible names and clear focus indicators. Keep the 36 visual copies from producing 36 confusing duplicate controls: offer a single understandable twelve-record selection model or a selected-cover control plus previous/next actions and a correctly labelled film list. Do not hide essential film names only in CSS background art. Decorative masks, grain and kanji should be inaccessible. Make small visible labels sit inside practical 44px interaction targets where relevant. Honor system contrast preferences where feasible without losing readable content.

The detail and auxiliary panels need focus containment, Escape, background inertness and focus restoration. Any font or image loading error must leave metadata and navigation operable. Do not trap the keyboard in the shelf, prevent browser zoom, or block native vertical scrolling inside a phone detail. Use a no-script message with useful collection context if the shelf depends on JavaScript.

## Completion checks

Verify the delivered interface with the actual hosted sheets and inspect the crops visually. Check that the opening record is Noon in Ashes, every front matches its spine/title, the three replacement spines are used, and all twelve records appear in the correct order. Test both loop directions, long drags, wheel bursts, quick repeated arrow presses, endpoint ruler clicks and selection after resizing.

Confirm that far spines shrink, darken, sink and pack together; the selected front opens adequate space between its neighbours; and no face appears reversed or as a full sprite sheet. Inspect the start, middle and end of the clip expansion and ink reveal. Open/close during an animation, resize with the detail open and verify that the closing paper returns to the current cover.

Check desktop and phone viewport compositions, keyboard-only operation, visible focus, focus restoration, real panel destinations, mobile detail scrolling, pointer cancellation, reduced motion and simulated image-loading failure. A desktop phone-sized viewport is a responsive check, not evidence of testing a physical device. Run appropriate syntax/build checks for the chosen stack and report verification limits honestly.

Deliver the full implementation and a working public example when publication is requested. Keep the full working prompt, all four asset URLs and any required notices together in the pack. Do not replace an independently existing adapted example when publishing this faithful VHS version; update this pack's example link to the new correct build.

## Reuse and media workflow

Use this independently authored working prompt verbatim, adapt it, or combine its locked elements with other references. Keep the current frontend unless a platform change is requested. Replicate is the default for any new media generation; verify the chosen model, scope, current cost and retry allowance before spending. The four supplied sheets can be reused under their existing unchanged-media approval. Show any newly selected, newly generated or materially altered media in chat and obtain approval before placing it on a public site, asset host or release. Preserve required font and third-party license notices.


## Example implementation refinements

The public VHS example also exposes a Reduce motion switch in its navigation menu; it combines that preference with the operating system setting. Below 500px height, landscape composition reduces tape height and moves the caption above the ruler. For desktop-width landscape, use H=32svh, cy=35%, a 56px top bar, 26px caption title, 4px caption gaps, and the ruler 44px above the bottom. Phone-width landscape uses H=38svh, cy=40%, a 22px title and a 38px ruler bottom offset. Keep the cursor native on phone-width layouts. The example uses the fictional collection label rather than claiming authorship of supplied artwork.
