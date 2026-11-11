# Bird species atlas

Build an interactive field-guide hero for two birds: Hoopoe and Kingfisher, with Kingfisher selected initially. The page combines a left editorial sidebar, two specimen tabs above a large central stage, and an independently scrolling facts panel on the right. One transparent WebGL canvas spans the entire hero so an enlarged specimen can overlap the interface without panel clipping. There is no video. Use the existing project stack; a single HTML page with inline CSS/module JavaScript is the buildless reference treatment. WordPress is optional. New media uses Replicate by default and requires agreed spending and in-chat approval before publication.

## Assets, libraries and type

Use the approved two PNG illustrations and two GLB specimens in the hosted asset map. Keep each image/model pair associated with its species; the PNG is the loading/failure fallback and also supplies the tab thumbnail and close-up lens. Load the active specimen first and preload the other later. The reference library is Three.js with GLTFLoader, DRACOLoader, MeshoptDecoder and RoomEnvironment. Pin a compatible verified release and decoder path rather than mixing addon versions. Implement pointer interaction directly, without OrbitControls.

Display type is Newsreader400/500 with italic400, body Nunito Sans400/600/700. Use serif fallbacks Iowan Old Style/Georgia and sans Segoe UI/system-ui. Render line icons as inline24×24 SVG symbols, stroke1.5, round caps/joins, usually20px, rather than emoji or an icon font.

Day tokens: background#f6f1e7, panel#fbf8f1, line#e7e0d1, ink#1b1a17, muted#6d685d, sage#4d5a3d, sage text white, sage tint#e9ebdc, chip#efeadd, shadowRGB60,48,28. Dusk: background#14170f, panel#1b1f15, line#2d3324, ink#f2ecdf, muted#a8a392, sage#a9b98a, sage text#14170f, tint#283020, chip#262b1d, shadow black. Ease cubic-bezier(.22,.8,.24,1); palette changes .6seconds. Focus rings are2px sage with2px offset.

## Desktop layout

Above1100px, fill100dvh with grid columns196px / minmax(0,1fr) / clamp(300px,27vw,356px). The absolute full-hero canvas has z-index5 and pointer-events:none; interaction belongs to the accessible stage element. Hide page overflow only when every control and fact remains reachable internally.

Sidebar padding22px12px18px24px, right border1px. Set the atlas name in26px Newsreader, then navigation for Home, Featured, Songbirds, Kingfishers, Owls, Hummingbirds, Raptors and Waders. Example group counts are34,8,11,15,12,9; do not imply those additional species are interactive until implemented. Selected Featured uses sage tint. Navigation controls are14.5px with12px secondary labels,10px corners and7×10px padding. Place an active-species card at the bottom:92×76 image,18px title,12px description and a useful Learn more action.

Centre padding48px18px14px26px, grid rows auto/minmax(0,1fr). Tabs are130px wide with58×52 contained thumbnails,15.5px names,12.5px italic Latin names,8px corners and1px outlines. Selected uses sage tint and a45% sage mixed border. Left/right arrow keys move between tabs; maintain role=tablist/tab, aria-selected and appropriate focus behavior.

The stage fills available space, has tabindex0, a grab cursor and touch-action:none limited to this specimen interaction area. A ground shadow sits at bottom15%, width min(62%,460px), height44px and .22 opacity, shrinking/fading during switches. Add a30px preparing ring and clear loading text; failed GLB uses the species PNG. A top-right drag/zoom hint disappears permanently after first interaction. The left icon rail has four38px circular controls with9px gaps: zoom in, zoom out, expand and light. Use aria-label/aria-pressed and distinguish active states. The bottom46px turn pill contains quarter-turn left,360° and quarter-turn right; put a centred italic caption below.

Right column padding13px26px14px0, rows auto/minmax(0,1fr), gap16px. The top row contains a32px search field, notification button and account button. Either implement their declared behavior or make their illustrative status explicit; do not invent an account service. The detail card has6px corners,22px20px16px padding and internal vertical scrolling. Its polite live article includes family eyebrow;40–54px name; three tag pills;13.5px/1.55 description;21px section headings; four trait rows on22px/88px/1fr tracks; habitat; and a bottom-pinned close-up control. That control uses a76px circular PNG lens with520% background scale, explanatory copy and a chevron that rotates when pressed.

## Species data

Hoopoe: Upupa epops, family UPUPIDAE. Tags Ground forager/Crested/Migrant. Describe cinnamon, black and white plumage, a long curved probing bill, a crest raised into a fan and loose butterfly-like flight. Traits: length25–29cm; wingspan44–48cm; insects/larvae/grubs; Europe/Asia/Africa. Habitat orchards, vineyards and dry grassland. Caption “A crown raised, and the orchard takes notice.” The close-up explains black feather tips in the raised crest; lens position62%22%. Featured title “A crown of cinnamon.” with short text about broad barred wings and its recognizable call.

Kingfisher: Alcedo atthis, family ALCEDINIDAE. Tags River bird/Diver/Iridescent. Describe a small brightly coloured river/lake bird known for hunting dives. Traits: length16–17cm; dive speed up to40km/h as supplied example data; small fish/insects; Europe/Asia. Habitat slow rivers, streams and lakes. Caption “Blink, and the river keeps its secret.” Close-up discusses the mosaic of plumage structure/colour; lens position24%30%. Featured title “A flash of river blue.” Verify biological claims against authoritative sources when adapting this into a factual published guide.

## Scene and framing

Use alpha/antialias renderer, DPR≤2, sRGB output, NeutralToneMapping, exposure1.05. PMREM RoomEnvironment blur .04 with environmentIntensity .95; warm key#fff4e2 intensity1.6 at(2.5,4,5); rim#bfd8ff intensity .5 at(-4,2,-3). Perspective FOV26, facing the origin along-Z. Each specimen rig is pivot(slide/scale/idle)→spin(user quaternion)→holder(normalized GLB). Centre on its bounding-sphere centre and scale holder by1/radius. Maximize supported anisotropy on colour maps and disable specimen frustum culling so overlap remains visible. Home Euler YXZ has yaw .75rad, pitch .12rad.

Observe hero/stage sizes. Frame origin at the stage horizontal centre and44% of stage height. Target specimen pixel radius=min(stageWidth×.5,stageHeight×.6)×1.16. Set camera z=heroHeight/[2 tan(FOV/2)×pixelRadius×zoom] and setViewOffset(W,H,W/2-cx,H/2-cy,W,H), using hero-relative stage coordinates. Ease centre/radius with1-exp(-dt×7), zoom rate6. Verify the computation against actual model radius and viewport, rather than accepting a visually distorted result.

## Interaction and motion

Drag with pointer capture: premultiply spin by world-Y rotation dx×k and world-X rotation dy×k, k=π/max(260,pixelRadius×1.6). Decay release velocity by exp(-dt×4.5). Wheel zoom multiplies by exp(-deltaY×.0016), or .01 under ctrl; clamp .55–3.4. Pinch uses distance ratio; buttons multiply/divide1.35. Turn buttons enqueue±90° or+360°, consumed at rate4.2. Double-click or0 resets quaternion toward home and zoom1 at rate6. Focused-stage arrows rotate .18rad; +/- zoom1.2. Close-up toggles zoom2.6/1 and aria-pressed reflects zoom>2.2.

Expand hides sidebar/right panel by horizontal24px travel and tabs by16px upward, each .5seconds, disabling hidden controls. Reframe to the hero centre at50% height; Escape restores the layout and focus. Dusk eases environment to .28, warm key2.6/#ffc98a, rim1.9 and exposure1 at rate4. After1.8seconds idle, ramp sway over1.5seconds: pivot yaw sin(t×.55)×.16, pitch sin(t×.9)×.03, hover y sin(t×1.3+index)×.028. Stop these under reduced motion.

Species switches last780ms. Direction is sign(newIndex-oldIndex). Outgoing over60% duration uses cubic ease-in: scale1-e, x=-dir×e×slide, yaw offset=-dir×e×1.4. Incoming uses full-duration cubic ease-out, scale=outBack×(.25+.75e), x=dir×(1-e)×slide, yaw=dir×(1-e)×1.6; outBack=1+2.2(t-1)^3+1.2(t-1)^2. slide=stageWidth×.95/pixelRadius world units. Reset incoming orientation/zoom and wait visibly if its model is not ready. Detail children exit .2seconds at opacity0/y-6px, then update all corresponding text/images and enter .6seconds from y12px, staggering45ms. Prevent stale asynchronous loads from replacing a newer selection.

## Responsive and acceptance

At1100px hide sidebar, use minmax(0,1fr)/clamp(280px,36vw,340px), centre padding-left20px. At760px use one100dvh flex column: compact21px brand header; horizontal full-width tabs with44×40 images; flexible stage;34px rail controls; turn pill bottom30px;15px caption; hidden hint; bottom sheet z7, max-height40dvh,16px top corners and safe-area padding,34px name and19px section heads. Focus mode slides the sheet below view and hides the header. Short heights≤620px reduce padding and hide the featured image/description.

Respect reduced motion with instant species changes, no idle drift and collapsed transitions. Test both species, quaternion rotation/inertia, touch pinch, zoom bounds, keyboard reset, close-up, expand/Escape, palette, lost WebGL/model failure, rapid tab changes, font loading and375px horizontal overflow. Verify all non-stage controls work without pointer gestures and all fact content remains reachable. This is a two-species reference experience, not a finished full bird database.

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | kingfisher illustration | [kingfisher illustration](https://lapis-slate-xvar.here.now/library/bird-species-atlas/media/51937aa69c953c.png) |
| asset-02 | kingfisher specimen GLB | [kingfisher specimen GLB](https://lapis-slate-xvar.here.now/library/bird-species-atlas/media/a6cf1807a9dc80.glb) |
| asset-03 | hoopoe illustration | [hoopoe illustration](https://lapis-slate-xvar.here.now/library/bird-species-atlas/media/de19abc4f12fd2.png) |
| asset-04 | hoopoe specimen GLB | [hoopoe specimen GLB](https://lapis-slate-xvar.here.now/library/bird-species-atlas/media/bf810e4935fd2c.glb) |

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
