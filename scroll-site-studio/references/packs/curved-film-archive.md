# Curved film archive

Build a responsive, single-screen film collection whose central interaction is a curved three-dimensional shelf. The selected VHS case turns from its spine to its illustrated front. Neighbouring spines recede into a shallow bowl on each side, becoming smaller, darker and more closely packed. Opening the selected film grows a paper detail sheet out of the projected cover rectangle; the poster appears through an irregular ink mask. Deliver a working interface with its dataset, image-crop configuration, keyboard and touch controls, and reduced-motion composition.

Use the current project stack. A standalone HTML document with inline CSS and JavaScript is sufficient; no animation library is needed. WordPress is optional. Preserve this interaction and geometry in faithful mode. In adapted mode, the same shelf may hold record sleeves, books or other objects, but recalculate the face proportions and crop data for that medium. A vinyl sleeve cannot use VHS crop coordinates unchanged.

## Art direction and typography

Use warm paper `#ECE8E0`, a lighter sheet `#F3F0EA`, ink `#141414`, muted text `#6D6A63`, cobalt `#1F3FB0`, and a dark rule at `rgba(20,20,20,.9)`. The main easing is `cubic-bezier(.2,.8,.2,1)`. Use Inter Tight for labels, titles and years; Newsreader roman and italic for the synopsis and supporting credit; Noto Sans JP for Japanese labels and titles. The large decorative Japanese lettering needs its own weight-800 subset. Keep appropriate font licenses when self-hosting fonts.

The desktop tape height is `H=min(47vh,33vw)` and shelf centre is `cy=41%`. On a phone up to 767px use `H=min(68vw,40svh)` and `cy=43%`. Measure the resolved height with a probe element rather than independently approximating CSS units in JavaScript. The document is a fixed composition without horizontal overflow. Use ordinary page scrolling inside the phone detail sheet.

Apply a decorative paper-grain layer above the composition with pointer events disabled, multiply blend and opacity .6. Its 220px SVG tile uses fractal-noise turbulence, base frequency .85, three octaves and stitched edges; tint the grain toward RGB (.45,.42,.38) with alpha .22. Do not put the grain inside a pointer target.

The top bar is 76px high with 36px side gutters. Place the archive brand, a 40px horizontal rule and a small archive label on the left. Place Films, About, Journal and a two-line menu on the right with 34px gaps. The label style is Inter Tight 600, 10.5px, line-height 1, tracking .14em and uppercase. Use cobalt consistently for the navigation, titles, arrows and ruler. Resolve navigation destinations or provide actual local panels instead of nonfunctional links.

Put decorative vertical kanji columns behind the shelf, at left 2.4vw/top 13vh and right 2.4vw/top 9vh. Their type size is `min(19vh,12.5vw)`, line-height 1.02 and tracking .02em. Fill the letters with a 3px dot screen: a radial dot of `rgba(64,82,138,.55)` through 36%, transparent from 40%, plus a pale `rgba(110,122,160,.26)` wash. On phones use 22vw and opacity .8. The background lettering is decorative and hidden from assistive technology.

## Required source sheets and crop map

Use the four approved sprite-sheet roles from the pack manifest: `covers` (1744×2336), `spines` (2688×1152), `fix` (1520×2688), and `fix2` (1520×2688). Preload them before showing the shelf. Each case uses rectangular CSS background crops; these sheets are not twenty-four separate images. Keep these sheet dimensions exact because every crop is expressed in original pixels.

| Film ID | Spine sheet | Spine x,y,w,h | Cover sheet | Cover x,y,w,h |
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

For sheet width W and height Hs and crop x,y,w,h, set background size to `(W/w*100)% (Hs/h*100)%`; set background position to `(x/(W-w)*100)% (y/(Hs-h)*100)%`. The detail poster is a clipped 474×900 SVG: its sheet image sits at `(-x*474/w,-y*900/h)` with dimensions `(W*474/w,Hs*900/h)` and `preserveAspectRatio=none`.

## Collection data

Keep the shelf order below. Store each record as an ID, title, romanised title, Japanese title, year, genre, duration and synopsis. The film metadata is fictional reference content. Retain supplied wording only when using an authorized original; otherwise write collection-specific text. Initial selection is index 5.

| ID | Title | Romanised title | Japanese title | Year | Genre | Minutes | Synopsis direction |
|---|---|---|---|---|---|---|---|
| valley | The Silent Valley | SHIZUKANA TANI | 静かな谷 | 1958 | Drama | 104 | A returning teacher confronts her family's exile and a village's silence. |
| bluehour | The Blue Hour | AO NO TOKI | 青の刻 | 1962 | Romance | 97 | Two strangers exchange evasions during a harbour evening. |
| river | River of Salt | SHIO NO KAWA | 塩の川 | 1964 | Drama | 121 | Brothers transport an unwanted cargo toward a changed city. |
| summer | The Last Summer | SAIGO NO NATSU | 最後の夏 | 1966 | Drama | 109 | Friends face the loss of their village beneath a new reservoir. |
| green | The Green Road | MIDORI NO MICHI | 緑の道 | 1969 | Mystery | 101 | A surveyor encounters inexplicable tracks along a forest route. |
| noon | Noon in Ashes | HAI NO SHOGO | 灰の正午 | 1971 | Western | 112 | A desert journey to collect a debt reveals an unexpected instigator. |
| observer | The Observer | KANSATSUSHA | 観察者 | 1973 | Thriller | 96 | A guard questions who is observing whom inside his building. |
| birds | The Fallen Birds | OCHITA TORI | 落ちた鳥 | 1975 | Drama | 118 | A young woman investigates the disappearance of a frontier town's birdsong. |
| storm | Light in the Storm | ARASHI NO HI | 嵐の灯 | 1978 | Drama | 127 | A lighthouse family shelters a mysterious survivor during severe weather. |
| tide | The Long Tide | NAGAI SHIO | 長い潮 | 1981 | Drama | 99 | A woman waits through successive tides for an overdue fishing boat. |
| war | A Quiet War | SHIZUKANA SENSO | 静かな戦争 | 1985 | Comedy | 103 | A long neighbourly feud persists without a spoken explanation. |
| door | Red Door | AKAI TOBIRA | 赤い扉 | 1989 | Thriller | 114 | A cinema worker follows an unknown reel on the venue's last night. |

Render three copies of all twelve records, for 36 virtual tapes. Virtual index is `copy*12+i`; start both the displayed position s and target T at 17. Use the dataset rather than manually duplicating labels or crop markup.

## Shelf geometry

Build a zero-size preserve-3d stage inside a full-width shelf with perspective P=1400px. The shelf top is `cy-H/2-50px` and its height is `H+100px`. Each tape is a zero-size 3D transform node with two H-high faces starting at -H/2. Spine width is `ws=H*142/840`; cover depth is `d=H*474/900`; spacing is `gap=H*.035`. The spine is translated by d/2 on Z. The front face rotates Y by 90° and translates by ws/2 on Z. Use backface visibility hidden and 2px face radii.

Set falloff U to H*1.3 on desktop or H*1.05 below 768px. Wrap relative virtual indices into [-18,18). For relative index r define B=(r+sin(πr)/π)/2 while |r|<1, otherwise sign(r)*.5. Arc length is `u=r*(ws+gap)+(d-ws+1.4*gap)*B`. Screen scale is `sc=1/(1+(abs(u)/U)^1.6)`. Precompute the screen-X integral in 2px increments up to 3U, accumulating `2/(1+(u/U)^1.6)`; interpolate it to obtain signed xsc(u). This integral is what compresses far-away spines smoothly.

Each frame derive `o=smoothstep(max(0,1-abs(r)))`, k=1/sc and hide tapes beyond |u|>1.95U. Set z=`P*(1-k)+o*H*.1`, x=`xsc(u)*k`, y=`(H*.5*(1-sc)*.42+o*H*.012-lift*H*.05)*k`. Y rotation is `sign(u)*min(1,abs(u)/U)*26°*(1-o)-90°*o+tiltY*o`; X rotation is tiltX*o. Compose translate3d then X and Y rotations. Sort z-index by round(3000+z). Spine shade is min(.6,o*.55+(1-sc)*.32); cover shade is (1-o)*.82. Hovering a non-active tape eases lift toward 1 at rate 12.

The floor shadow is centred at `cy+.47H`, width min(96vw,3.6H), height .26H, with a soft radial brown-black falloff. Add a 42px play ring at the active cover's lower-left: left W/2-d/2-6, top cy+.36H. Its scale is smoothstep(max(0,1-abs(T-s)*3)); hide it while detail is open.

## Motion, inputs and caption

Use one animation loop and cap dt at .05 seconds. Ease s toward T using `1-exp(-5.2dt)`, increasing the rate to 18 while dragging. Rebase s and T by complete collection loops when they drift more than four loops away. Active film is round(s) modulo 12. An inactive-tape click selects the nearest corresponding virtual index; a settled active-cover click opens the detail. Ignore a click after a drag. Pointer movement greater than 5px starts a drag; use `T=T0-dx/(ws+gap)` and snap to an integer on release. Wheel movement uses the dominant axis, adds `delta/(ws+gap)*.5`, and snaps after 160ms idle. Disable shelf wheel navigation while detail is open. Arrow buttons and left/right keys step one; Enter opens and Escape closes.

Cover tilt engages only inside .55d horizontally and .55H vertically while abs(T-s)<.3 and detail is closed. There tiltY targets pointer offset divided by .55d times 8°, and tiltX targets negative vertical offset divided by H/2 times 5°. Away from the cover, tiltY is horizontal viewport-relative displacement times 4° and tiltX is zero. Ease both at rate 7.

Position the caption at `cy+H/2+4.2vh`, with 10px gaps and max-width min(80vw,640px). The title is cobalt Inter Tight 600, clamp(28px,3.4vw,46px), tracking -.015em. Show romanised and Japanese titles below in a 9.5px uppercase tracked label, then an 18px rule and a 10.5px YEAR—GENRE line. Place 44px arrow targets on either side of the title at centre ±min(19vw,250px). Swap caption lines through masks: new text moves from dir*105% to zero, existing text moves from its actual current transform to -dir*105%, 650ms with the main easing. Cancel/remove superseded spans without a visible jump.

The bottom ruler covers 1955–1990. Put it 36px from each side and 64px above the bottom; draw a 1px line 12px down, 13px major ticks every five years and 7px minor ticks. A 9px dot represents the interpolated year between adjacent films. At the 1989-to-1958 wrap, switch at the halfway point. Ease the dot at rate 14, but jump directly when the year difference exceeds six. Its fraction is `(year-1955)/35`. A ruler click selects the nearest film year using the shortest direction around the loop.

## Detail reveal and responsive verification

The full-screen paper sheet sits at z60. Desktop uses two columns, 4vw gap, padding 110px 6vw 56px 7vw. The left column has a subtitle, 44–80px cobalt title, muted year/genre/duration, Newsreader 17px/1.5 synopsis at max 42ch, supporting creator information and a real 44px watch action. Resolve that action to actual authorized content or clearly label its unavailable state. Put an accessible close button at the upper-left. Move focus inside, trap focus while open, and restore it to the cover on close.

Read the active cover's projected rectangle. Animate the detail sheet clip from that rectangle, with 3px corners, to full-screen zero-radius inset over 1050ms using cubic-bezier(.76,0,.18,1). Text lines rise from 110% over 900ms starting at 620+i*75ms. The poster uses seven circles in its mask: (150,330,0ms), (340,600,120), (250,120,220), (90,760,300), (400,250,360), (260,860,420), (230,470,180). Starting at 520ms plus each delay, grow radius to 720 over 1250ms ease-out cubic. Distort the mask with fractal-noise frequency .011, three octaves, seed7 and displacement scale120. Closing clips back to the current cover rectangle over 850ms, then hides and cancels the sheet animations.

At ≤767px use a 60px top bar and 16px gutters; hide text navigation but retain the menu. Set caption title to 27px, move arrows to bottom118px at the edges, move ruler to 16px sides/bottom54px and suppress alternate year labels. Show the detail as one scrolling column, poster first at 46svh and title42px. Disable custom cursors on touch. On a fine pointer the optional 58px cursor follows at rate16, scales to1.75 and cobalt over the openable cover, .72 over spines and .55 over buttons; do not obscure actual focus indicators.

Reduced motion makes spring/lift changes immediate, caption changes static, sheet/text transitions1ms and the poster fully revealed immediately. Test all twelve records, both wrap directions, fast repeated selections, resize while open, unavailable-sheet fallback, keyboard focus, phone dragging and long synopsis scrolling. Show every newly generated or newly selected image here in chat before any public use. Replicate is the default provider for replacement media; agree model, cost and scope before generation.

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | spine sprite sheet (2688x1152) | [spine sprite sheet (2688x1152)](https://lapis-slate-xvar.here.now/library/curved-film-archive/media/bef5d7e9e251fd.webp) |
| asset-02 | replacement observer and storm spines (1520x2688) | [replacement observer and storm spines (1520x2688)](https://lapis-slate-xvar.here.now/library/curved-film-archive/media/906f9a9a8b2cd8.webp) |
| asset-03 | replacement river spine (1520x2688) | [replacement river spine (1520x2688)](https://lapis-slate-xvar.here.now/library/curved-film-archive/media/1d302b88229f3e.webp) |
| asset-04 | cover sprite sheet (1744x2336) | [cover sprite sheet (1744x2336)](https://lapis-slate-xvar.here.now/library/curved-film-archive/media/d12de9fb113a52.webp) |

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
