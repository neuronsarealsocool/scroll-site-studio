# Point-cloud companion — complete working prompt

Build a single-page product presentation for **ION OS**, an on-device assistant. Its visual subject is a real human head-and-shoulders scan rendered as approximately60,000 individually moving grains. The same bust must remain recognizably continuous through the entire page: a pointer-reactive opening, a framed OS demonstration on lavender, an enlarged upper-left Memory composition, then a dust transition into an upper-right Agents composition. Scrolling backward must reverse the choreography. This is the particle design; do not replace it with a film or a different product theme.

Use this complete specification directly, adapt selected parts to another brand, or combine it with other references. Keep the project’s existing stack; the reference implementation is buildless HTML/CSS/ES modules. WordPress is optional. No paid media generation is needed for the supplied scan and gallery files. If new media is requested, Replicate is the default, costs must be agreed first, and the actual result needs approval in chat before publication.

## 1. Files, dependencies and assets

For a buildless implementation produce index.html, tokens.css, style.css and main.js, with modules for cloud rendering, cursor interaction, liquid simulation, scroll poses, frame choreography, text/data reveals, the progressive veil, smooth corners, header/clock and colour conversions. Serve through HTTP; ES modules do not constitute a reliable file:// deliverable. Keep these modules small enough to edit independently. Do not flatten the website into an iframe, screenshot or opaque monolithic export.

Use verified Three.js0.186.1 with PCDLoader, EffectComposer, RenderPass, UnrealBloomPass, OutputPass and GPUComputationRenderer from that same release. Core import: https://cdn.jsdelivr.net/npm/three@0.186.1/build/three.module.js ; addon import prefix: https://cdn.jsdelivr.net/npm/three@0.186.1/examples/jsm/ . The core and original font endpoints were checked and returned200 during the corrected build. Never silently mix core and addon revisions.

Use these roles, with their final approved hosted URLs inserted before delivery:

| Role | URL | Contract |
|---|---|---|
| Head-and-shoulders point cloud | https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/0efcd6f363c852.pcd | PCD v0.7 binary,59,750 XYZ float32 points; preserve geometry and orientation pipeline |
| People gallery | https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/48d411d5c12622.webp |640×430 WebP, used in the first floating photograph widget |
| Places gallery | https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/9101dd00cbe3b4.webp |640×430 WebP, used in the second floating photograph widget |

The public geometry must be explicitly approved before publishing it. Gallery approval persists for unchanged bytes. Retain all applicable notices with distributed code/fonts/models; a hosted file is not a new license. For an exact build, do not replace a missing model with an unlabelled procedural approximation. Keep the page’s complete text and a clear failure state available when WebGL or the model cannot load.

Display fonts are Geist Pixel Square and Geist Pixel Circle, weight400, swap rendering. Verified functional font sources: https://cdn.jsdelivr.net/npm/geist@1.8.1/dist/fonts/geist-pixel/GeistPixel-Square.woff2 and https://cdn.jsdelivr.net/npm/geist@1.8.1/dist/fonts/geist-pixel/GeistPixel-Circle.woff2 . Declare them through @font-face. Do not preload these fonts. Body text prefers locally installed Helvetica Neue, then Helvetica, Inter and Arial. Before first paint, compare the canvas widths of `mmmmmlliiWWQ@` at72px monospace versus72px Helvetica Neue followed by monospace; if equal, mark the no-Helvetica condition and load Inter400/500 from its functional font stylesheet. Preserve usable fallbacks if that request fails.

Set lang=en, UTF-8, viewport width=device-width/initial-scale=1/viewport-fit=cover, a meaningful ION OS title and theme colour#000000. Add a js class before paint, then load font declarations, token stylesheet, main stylesheet, import map and the module entry point in a predictable order.

## 2. Global geometry and tokens

Use one scaling unit `u=clamp(.85px,100vw/1470,1.3px)` on desktop. The reference design frame is1470×956. Spacing variables are4/8/12/16/24/32/48/72/120/192 multiplied byu. Reset box sizing for elements and pseudo-elements; body margin0; horizontal overflow uses clip, not a second scrolling container. Disable overscroll bounce; inherit link colour and remove link decoration except where a specific interactive treatment calls for it. Body is400 medium text with antialiasing and -.011em tracking. Do not add decorative borders, strokes, icon fonts or shadows; only the specified light-mode floating-widget lift uses a shadow. Functional focus outlines remain necessary.

| Token group | Values |
|---|---|
| Ground/surfaces | site#000000; bg#121214; panel#18181a; card#242428; control#3c3c40 |
| Ink | primary#fcfcfc; secondary#a4a4aa; muted#88888e |
| Accents | lavender#c8a9eb; yellow#e2e626; cyan#7cf8fa; coral#f0634f; steel#6f83a2 |
| Dark glass |rgba(24,24,26,.52); light glass rgba(252,252,252,.08); blur24u/saturate1.4 |
| Fills/rule | primary-white alpha .06/.10/.16; rule alpha .14; chip blur12u/saturate1.4 |
| Light ground/ink |#e8e5ef; surface rgba(252,251,255,.82), second surface rgba(255,255,255,.6); ink#17161b/#5d5a67/#8e8a98 |
| Light fills/rule |rgba(23,22,27,.05),.09 and .1; glass blur20u/saturate1.5 |
| Light lift | x0,y24u,blur60u,spread-24u,rgba(60,40,110,.18) |
| Type | small13u/1.3/tracking0; medium16u/1.45/-.011em; large28u/1.15/-.025em; caps tracking .06em |
| Display | d1=min(176u,12.6vw),line-height .86; d2=56u,line-height1 |
| Radii |6u/10u/14u/20u; pill999px; standard button height44u; gutter48u |
| Easing | out(.23,1,.32,1); expo(.16,1,.3,1); move(.77,0,.175,1) |
| Durations | press160ms; UI240ms; entrance600ms; stagger60ms; entry blur12u/y16u; press scale .97 |

The Dawn gradient is90degrees, with percentage/colour stops (0,#f3624f), (21,#b0665d), (32,#645a5b), (42,#314045), (53,#141519), (63,#243b41), (74,#456272), (84,#6f82a2), (95,#a6a0d0), (100,#b7a6dc). The Golden gradient is90degrees with stops (0,#caaaeb), (45,#d1c0a6), (100,#e4e728). Express these as valid CSS with a space between each colour and stop percentage.

At width≤767px setu=100vw/430, small=max(12px,13u), medium=max(15px,16u), large=max(22px,28u), d2=44u and gutter16px. Under reduced motion set the press/UI/entry/stagger durations, entry blur and entry travel to0, with the specific short opacity-only exceptions below.

For elements marked data-sq, apply60% corner smoothing, using each element’s measured size and computed top-left radius. A corner consists of cubic/arc/cubic segments; limit its smoothing to min(.6,budget/r-1), where budget=min(width,height)/2 andr≤budget. Recompute using ResizeObserver. Keep border-radius as the fallback if the clip path is unsupported. Do not allow smoothing to clip focus indications or interactive text.

## 3. Layer tree and semantic content

The document’s ground is the html background. A fixed full-viewport stage sits atz1 with pointer-events:none; inside it the giant hero title is behind the canvas and the framed headline is above it. Memory and Agents content isz2. Append the progressive blur veil after those screens atz2. The OS section and fixed hero note usez3. The header isz10. Give the stage a real black fill only while it is framed; its unframed rendering canvas remains transparent.

Use a visually hidden h1 as the accessible version of the giant title. The visible title’s spans read “Hello,” and “I’m ION”. The header contains a9-square mark linked to the top; a local24-hour clock with separate seconds; a cyan status dot and “ION is listening”; links Status/Agents/Memory; Sign in; Join the waitlist. A fictional marketing demo must not imply that accounts, encryption or real agent execution are connected. Connect owner-supplied endpoints when provided; otherwise make button outcomes clear and useful without fake success.

The hero itself takes zero layout height; the OS runway begins at page top. Its fixed note contains a “Private beta” badge, “ION OS0.9 · on-device memory”, and three-line proposition: “ION is the operating system” / “that sees you.” / “It asks before it acts.” The third line is muted. The framed stage contains a ION OS badge and “Everything around you,” followed by “in one quiet place.”

Seven OS widgets must exist, with the exact roles and data-at values in section8. Their copy/data:

- People photograph caption “People” with count4, using the People gallery file.
- Places photograph caption “Places” with count9, using the Places gallery file.
- Add-image control with a CSS plus glyph.
- Tool chips Summarize with⌘S, Rewrite with⌘R and Later withL.
- “Focus this week” mini chart, “+12%”, bars[46,62,34,28,74,58,66], axis “Thu” and “Now”; the last bar is the current yellow one.
- Composer initially “Ask ION anything…”, later typing “Move my3pm with Ana to Friday and tell her why it moved.” Keep natural spacing in the rendered copy. Its accessory row has plus, Image, Doc, microphone and send glyphs, and a thin Golden gradient along the bottom.
- Completion toast with a lavender checked disc: “Done. Ana has the new time.” This is part of the clearly illustrative choreography, not proof of a real message being sent.

Memory is a right-side text column: eyebrow “On-device”/“Memory”; heading “ION remembers, so you don’t have to.” and muted continuation “Everything it keeps stays on your device.” Paragraph: “The people, places and promises you’d want a friend to remember, held where only you can reach them.” Chips People/Places/Promises/Preferences. First panel is “Remembered”, Day/Week/Month tabs and the dataset in section9; below it show1,204 moments kept and312 forgotten on request. Second panel is “Where it lives”, Encrypted badge, a100% lavender track, legend “On this device ·100%” and “Cloud ·0%”, then chips “Forget anytime” with⌘⌫ and “Export” with⌘E.

Agents is a left-side text column: eyebrow Live/Agents; heading “It acts for you.” with muted continuation “And it asks before it does.” Paragraph: “Agents take the busywork, from the inbox to the calendar to errands, and stop at anything that’s yours to decide.” Chips Ask ION⌘K, Summarize⌘S and LaterL. First panel “Time saved today” has a2h14m badge, the Today chart below, and “3,240 handled this week ·3 waiting for you”. Second panel “Golden time” has yellow “Needs you ·3”, value78%, label “handled while you focused”,48ticks with37on, and “22% needed you ·they wait for you at9:30”. Add proper spaces around text/numbers; preserve the supplied example values. These are demonstration metrics until connected to genuine user data.

## 4. Header and clock

Place the header top12px, centred with width:max-content and max-width=viewport-24px. Its bar uses4px inset; height40u+8px; radius14u; background rgba(64,64,72,.55); backdrop blur24u/saturate1.4/brightness .5. Default header ink#c4c4ca. The mark tile is40u square, radius14u-4px, #46464d. Its3×3 squares are4u with3u gaps: base muted, alternating secondary, centre primary ink. Clock has12u left margin,16u size, regular weight, tabular figures; seconds use header ink. Rules are1px×16u with16u horizontal margins and white .2alpha.

Status uses8u gap and a6u cyan dot; pulse every1.8seconds with half-cycle opacity .35. Navigation gap16u. Buttons are40u high with16u horizontal padding and concentric corners, pressing to .97. Sign in uses#46464d, hover#52525a; the yellow main button uses dark text and hover#ecf04a. The first button after navigation has16u left margin; button-to-button gap4px. Apply hover treatments only to hover-capable fine pointers.

When the OS ground crosses its light threshold, switch bar to rgba(24,24,28,.72), rules towhite .16, tile/Sign in#48484d and hover#55555a. Animate relevant backgrounds/ink over400ms with the out curve. Entrance is600ms expo from opacity0, y-16u and blur12u, skipped under reduced motion.

At≤1100px hide status and its adjacent rule. At≤767px use top/left/right8px, automatic width and a flex-filling bar; hide all rules, navigation and Sign in; push Join the waitlist to the far right. Keep touch targets usable even where visual height scales down.

Format the clock with en-GB, two-digit hour/minute/second, hourCycle:h23. Update HH:MM only when changed, seconds independently, and datetime with ISO. Schedule at1000-currentMilliseconds+5ms. On becoming visible, refresh immediately; do not continuously poll or use aria-live for seconds.

## 5. Hero typography and transition

The title is absolutely positioned in the stage, margin0, horizontally centred, uppercase, regular Pixel Square, secondary ink, line-height .86 and tracking0. Its top is --bust-top+40px; fallback bust-top=107%-min(78%,98.4vw); shift title upward by half its own height. The original short brand uses font-size=(100vw-48px)/6.536 and one line. On phones it uses(100vw-48px)/3.192, left bearing-.038em and two block spans. The neutral ION name has the same three-letter length as the original. Keep those reference denominators initially, then measure actual Pixel-font ink because glyph metrics can still vary; make only a documented fitting correction needed to retain24px rails. Keep the line break and reference placement.

Cut a soft elliptical transparency window around the projected head rather than painting a solid patch over the title. Its radial mask is transparent through64%, opaque at100%; fallback radii24vh/30vh and centre50%/130%. On cloud placement, while the hero is active, convert head NDC to pixels inside the title’s box: x=(ndcX+1)×width/2-titleLeft; y=(1-ndcY)×height/2-(titleTop-titleHeight/2). RadiusX=headPixelWidth×.5/.64; radiusY=headPixelHeight×.5×1.08/.64. Round writes to whole pixels and update only changed values.

The note is fixed left/bottom24px, z3, large text. Metadata flex-wraps with16u gaps,24u bottom margin and small muted text. The lead has balanced wrapping, primary ink and a separate muted final span. Shared badges are32u tall,12u horizontal padding,8u gap,10u corners, white .14fill, chip blur and small500text. Their dots are6u lavender, cyan for Live, and yellow text for needs-you. On phones, the note becomes a glass card at left/right/bottom8px,16px padding,20u corners, medium text; metadata bottom gap12u and secondary ink.

Entrance runs once with js enabled. Title fades/rises/blurs into place; metadata and lead follow at60/120ms. At raw OS progress>.05 add the hero-out state; remove it only at≤.03. The exit lasts700ms: opacity to0, title y-4vh/scale .97/blur16px; note metadata/lead y-16px/blur10px. Hide after760ms; lead uses70ms motion delay and830ms visibility delay. Reverse restoration uses1100ms expo, metadata80ms delay, lead160ms. Use individual translate/scale/filter/opacity properties so they do not overwrite the title’s base centring transform. Reduced motion removes entrance and travel/scale/blur; return/exit is200ms opacity only.

## 6. Scan preparation, fit and placement

Load the actual PCD with PCDLoader. RotateXπ, thenY .05, thenX .19. Compute its bounds. Centre Y andZ on the bounding box, but deriveX from the head: divide the upper45% of scan height into48rows, calculate(minX+maxX)/2 for each occupied row and take the median. Translate by that head-line X and the Y/Z centres. Keep a raw Float32Array of the transformed positions. Do not jitter the source into a different face.

Use camera FOV30°, near .01/far40, desired height share .78, bottom bleed .07, maximum width1.3viewport widths, point-size constant .005 and head-centreY .10model units. Fit view=max(scanHeight/.78,scanWidth/(1.3×aspect)); cameraZ=view/[2tan15°]. Head-in-rig=(0,.10-boxMinY,0). Set heroY=(-view/2-.07view+headInRigY)/(view/2); unitsPerPx=view/hostHeight. Update --bust-top=(1+.07-scanHeight/view)×100%, rounded to2decimals. Reapply the last pose after resizing.

The base-pivot Group has YXZ rotation order; its child points mesh is offsetY=-boxMinY. A pose contains x/y(head target in NDC), scale, yaw, pitch androll. To place it, first scale and rotate by pose+gaze×anchor. Rotate headInRig×scale by that orientation to obtain lift. Compute half=(cameraZ-liftZ)tan15°, then rig position=(x×half×aspect-liftX,y×half-liftY,0). Set final rotation to pose+full gaze afterward. This preserves the base anchoring while the head leads the turn.

Use localPerPx=unitsPerPx/scale; set particle uUnits accordingly and uSize=.005×scale. Project local head(0,.10,0) for headNDC. Derive head dimensions from the scan above .10-(top-.10); headPixelSize=headSize×scale/unitsPerPx. Set the text-veil centre to headNDC and its radius to max(headPixelHeight/hostHeight,.001). Notify the title-mask placement callback.

## 7. Rendering, bloom and grains

The renderer has alpha:true, antialias:false, transparent black clear colour and no scene background. Cap DPR at2 and keep it fixed across runtime quality changes. Use a half-float non-MSAA composer target, RenderPass, bloom and OutputPass. Bloom starts strength .020/radius .9/threshold0. Preserve hue: apply bloomStrength after extracting luminance L=max(dot(rgb,[.2126,.7152,.0722]),.00001), multiplying bloomRGB by L^.60/L. This restores faint haze without a tint. Use five blur kernels3/5/7/9/11 and run their targets at CSS resolution, correcting composer/DPR sizing. The high-pass averages four diagonal taps with source offset(DPR/(2W),DPR/(2H)). Ensure final alpha is at least max(r,g,b) after the output transfer so premultiplied compositing does not discard the haze.

Create one instanced quad per scan point, double sided, corners±1 and two triangles. aHome stores the actual point; aRef points to the centre of a texel in the smallest power-of-two square covering all points:2^ceil(log2(sqrt(N))). Do not frustum-cull the grains. Before liquid allocation, bind zero1×1float textures for state and flow.

Particle parameters: streak .8; gradient centre(0,.10), radius .40; grain .335; initial scatter/dim0; viewport/head/headRadius/time as dynamic uniforms. State texel xy holds pixel offsets andzw pixel velocities. Convert offsets to model coordinates withuUnits. For scattering, derive stable per-texel random XYZ from sine/dot hashes with vectors(12.9898,78.233),(39.3468,11.135),(73.156,52.235) and multipliers43758.5453/24634.6345/9631.7453. Withk=scatter², fling is normalized(random-.5+.001)×(.35+.65randomX)×.05. Add drift(sin(.7t+randomY2π),cos(.6t+randomZ2π),0)×.01, scaled byk. Drop grains according to step(1-.7scatter,randomZ).

Project each displaced point and its velocity-advanced position. Screen-space velocity supplies a trail of min(speed×1.25,18)×.8pixels. Quad half-side is uSize×(1-.45scatter)/(2clipW)×.5viewportHeight. Fade the direction choice with smoothstep(0,1.5,trailLength); mix the X-axis toward a consistently signed velocity direction. Stretch the quad along that axis and offset it backward by half the trail. Record its normalized tail distance so the fragment shader can dither the end rather than showing a rectangular smear.

Gradientt=distance(homeXY,gradientCentre)/.40. Two clamped piecewise linear ramps share stops0%,32%,100%. Touched colours are white,#c8a9eb,#e2e626. The resting ramp reduces OKLCH chroma to .6 while preserving hue/lightness, approximately#c2b0d7 and#dfe389 for the latter stops. Interpolate between resting/touched using flow ink×.6. Film grain mixes an overlay blend of a screen-space hash with the colour at strength .335; hashes use the same numerical dot constants above. Convert sRGB to linear before the renderer’s final colourspace stage.

Discard dropped grains. Also discard trail fragments when clamp(tail,0,1)×.55×trailFade exceeds the screen-space hash. To reduce interference under text, compute normalized head distance in aspect-corrected NDC, divided byheadRadius. edge=smoothstep(.3,1.3,distance); direction=-clamp(headX/.3,-1,1); side=smoothstep(-.2,1,direction×(pixelNdcX-headX)). Multiply grain colour by(1-.1dim)(1-.6dim×edge)(1-.45dim×side). The cloud remains present but subdued near the reading columns.

Observe stage size and update renderer/composer dimensions, camera aspect, viewport uniform and fitting. Render only when something changes or a spring/simulation remains unsettled. Stop on document visibility changes. Release GPU resources and observers if the host unmounts the experience. A failure must not leave an infinite loading state or invisible document.

## 8. Scroll poses, pointer springs and GPU liquid

Measure absolute tops of OS, Memory and Agents on body resize; use current viewport height. Define around(section,[a,b]) as smoothstep(sectionTop+a×vh,sectionTop+b×vh,scrollY). Left pose=(-.66,.64,3.3,.48,.03,-.28) and right=(+.66,.64,3.3,-.48,.03,+.28), orderedx/y/scale/yaw/pitch/roll. Constants: centre drop .08; OS-in[.12,.8]; OS-out[2.2,3.2]; Memory approach[-1,-.2]; Agents transition[-.6,.1]; condensation .42.

Compute inOS/outOS using those windows, toLeft around Memory, andu=clamp((y-(agentsTop-.6vh))/(.7vh),0,1). Side interpolation is smoothstep(.3,.7,u); scatter=smoothstep(0,.4,u)×(1-smoothstep(.6,1,u)). Centre pose is(0,heroY-.08inOS(1-outOS),1,0,0,0). Interpolate each key from that centre to the left/right screen blend bytoLeft; multiply scale by1-.42scatter. Return heroWeight=1-inOS and dim=toLeft.

All springs have mass1, semi-implicit Euler substeps no longer than1/240second and dt clamped0–.25second. Snap when displacement<eps and speed<10eps. Pose/hero/dim usek30/c11; dustk26/c10; gaze yaw/pitch110/15; roll45/9; screen float10/6; gradient centre18/8. Gradient tolerance1e-5, other tolerances1e-4. Start by snapping to the current scroll pose, including mid-page loads.

Read the canvas’s transformed viewport box from the frame controller’s stored scale/translation, not repeated layout reads. In the hero, raycast the pointer to planeZ=.41. Use the projected eye position to compute yaw=clamp(atan2(hitX-eyeX,.41),-.6,.6), pitch=clamp(atan2(eyeY-hitY,.41),-.35,.3); multiply targets byheroWeight and roll=-.18yaw. Off-hero pointer coordinates give float targetsfx=clamp(2px/W-1),fy=clamp(1-2py/H); weightf=1-heroWeight. Add .035fxf/.05fyf to position and .07fxf/-.04fyf to yaw/pitch before placement. Gradient centre comes from the pointer ray transformed into point-local coordinates intersectingZ0, clamped to scan bounds±.1; when absent, return to the head.

Enable pointer-driven effects only for hover-capable fine pointers, no reduced motion and non-touch pointer types. Pointer leaving html, or pointerout without relatedTarget, returns gaze to rest. If pointer/reduced-motion capabilities change while running, reset immediately. Keep the loop awake only while springs move, dust>.001 or liquid remains active.

Allocate GPUComputationRenderer lazily on the first eligible pointer move, with half-float render targets. Home texture is float RGBA(x,y,random,1), with unused texels marked inactive. Flow depends on itself with linear filtering; state depends on itself and flow. The wake square spansmax(scanWidth,scanHeight)+.30 centred on the bounds. Flow channels areXY velocity, Z energy, W touched ink; state isXY pixel offset/ZW velocity.

For each frame setf=clamp(dt×60,.25,3). Smooth pointer with1-(1-.22)^f. Presence approaches1 at .1 and0 at .035 under the same frame-rate correction. A stationary pointer expires after1500ms; continue simulating270frames after presence reaches0. Local pointer delta divided bylocalPerPx/f becomes velocity, clamped±60 and smoothed .5; pass wake/40 clamped±1. Simulation time advancesf/60×(1+1.6presence). Parameters: radius150px, inkRadius110px, strength .5, spread1, turbulence .6, return1.2; decay .968^f; inkDecay .97^f.

Flow processing backtracesUV by local flowXY×texel×2.5, combines the centre .52 with four neighbours .12 each, and computes pointer Gaussian exp(-distancePx²/150²)×presence. Add pointer velocity×Gaussian×.22. Energy is the larger of prior energy and Gaussian×clamp(pointerSpeed×2.5,0,1). Apply the decay; move velocity components toward0 by1.2/127 and energy toward0 by1.2/255. Ink is max(previousInk×inkDecay-.002, Gaussian at110px). Clamp velocities±1. This pass spreads a transient velocity wake and a slower touched-colour field.

For each active state texel, use seed=homeZ and light=.45+1.1seed. Sample flow at the displaced home point. Letn be the soft-normalized vector from pointer to particle, Gaussian use150px radius, andenergy=clamp(2flowEnergy+Gaussian,0,1). Acceleration contains: outwardn×Gaussian×1.25×strength×spread×light; tangentialperp(n)×Gaussian×1.45×strength×spread×(.4+seed); drag towardflowVelocity×42×spread×light byenergy×.08; and two curl-noise octaves, second octave half amplitude atfrequency2.3/offset7.1, scaledenergy×1.2×spread×turbulence×light. Noise position ispointPx×.0095+(.35time,-.2time). Return acceleration subtracts offset×(.006+.02return)×(.65+.7seed). Integrate velocity withf, damp bymix(.93,.955,energy)^f, then integrate offset. When offset² andvelocity² areboth<.0004, zero them. The quintic value-noise hash uses123.34/456.21, dot offset45.32 and curl epsilon .35. After compute, bind current state/flow targets to the grain material.

## 9. Framed OS and floating widgets

The OS section is420vh atz3, with a sticky top0/height100vh pin, clipped overflow and noninteractive visual-plane pointer events unless a real control is activated. The framed stage hides overflow, receives a black fill and uses the transform around viewport centre. Its centred headline sits5.5% from top, gap16u, large type, initial alpha0 and top-centred transform origin.

Raw frame progresss=clamp((scrollY-osTop)/vh,0,3.2), followed by a26/10spring. The incoming phaseq=clamp(p/1.7), hold .5screen, outgoingo=clamp((p-1.7-.5)/1). Normalize any segment withclamp((x-a)/(b-a)). Use cubic ease-in-out for frame scale, quartic ease-out for the headline, expo-out for widget arrival and smoothstep for alpha.

Frame factorK=inOut(segment(q,.06,.5))×(1-inOut(o)); scale=1-(1-.56)K. It is framed whenq>0 ando<1. Set stage translate(frameX,frameY)/scale; radius=28K/scale pixels so the visible rounded radius is28px at rest. Frame pointer drift is-4K times the drift spring. Share `{scale,tx,ty}` with the cloud so its gaze coordinates follow the transformed stage. Clear stage transform and radius once unframed.

Ground blendG=segment(q,.1,.42)×(1-segment(o,.3,.9)); interpolate black toRGB232,229,239. Header light state isG>.5. Framed headline alphaE=quarticOut(segment(q,.2,.44))×(1-smoothstep(0,.4,o)); translateY=(1-E)24px and scale1/.56. Apply blur(1-E)10px only while partly visible.

| Widget | at / drift | Desktop position | Size | z |
|---|---|---|---|---|
| Tools |.40 /9 |left61vw,top25vh |chip row |3 |
| People |.42 /12 |left12vw,top25vh |200u×170u |4 |
| Chart |.46 /14 |left73vw,top33vh |250u wide,16u/16u/12u padding |5 |
| Places |.48 /16 |left15.5vw,top47vh |160u×136u |6 |
| Add image |.50 /18 |left5vw,top48vh |6u/6u/6u/12u padding,12u gap |7 |
| Composer |.58 /6 |centred,top78vh-20px |560u wide,16u padding |8 |
| Completion |.72 /11 |left70vw,top68vh |48u high,16u horizontal padding |9 |

For a widget with centre offset(cx,cy) from viewport centre, arrivalt=segment(q,at,at+.22). Exit order is reverse at-order; normalized exit start forranki is i×(1-.45)/(N-1), with exit duration .45. Let tOut use that window, e=expoOut(t), eOut=tOut^2.2, scaleK=1+(3.6-1)×[(1-e)+eOut], and presence=e(1-tOut). TranslateX=cx(scaleK-1)+springX×drift×presence; Y likewise, additionally multiplied by per-widget sway. Alpha=smoothstep(0,.45,t)×[1-smoothstep(.3,1,tOut)]. Blur=44×[(scaleK-1)/(3.6-1)]^.55 while flying. Glass=clamp((1.5-scaleK)/(.5),0,1), solid=1-glass. Set opacity/transform only when their serialized values change and remove tiny/settled filters rather than retaining permanent blur layers.

Widget bases use14u corners, white ink, small text and no stray outline. Backfill isRGB30,30,34 at solid alpha; glass fill isRGBA28,28,32,.8×glass, backdrop blur16u×glass/saturate(1+.4glass), with the specified light lift. Muted local widget ink is#cacad0 and#b4b4ba. Photograph cards use20u corners,6u/6u/8u padding,8u gap, image fill/cover and inner radius20u-6u; captions space the title/count with6u side padding.

Small key controls are34u square with10u corners and fill .06; send uses primary ink with dark glyph. Tool chips are32u tall,12u horizontal padding,8u gap, keyboard cap20u tall with6u padding and black .28background. The miniature bars occupy84uheight with6ugaps and3ucorners; collapseY .08 and grow over900ms expo with40ms per-bar stagger when the composer/landing phase completes. Their axis is muted and edge-aligned.

The composer reserves two medium-text lines. At full arrival, wait350ms then type one character every34ms; leaving reverses to the initial placeholder, cancels pending timers and resets the miniature chart. Caret1.5px×1.1em blinks1second in steps, half-cycle invisible. Accessory row gap6u, trailing controls margin-left:auto. Bottom glow is2u high, pill-shaped, inset24u and Golden gradient. Draw plus with12u×1.5px bars; microphone with7u×11u outline capsule and11u×5u stand; arrow with8u squared1.5px strokes rotated toward send; checked disc20u with a dark check atleft34%/top24%, width26%/height44%.

Pointer drift uses normalized[-1,1] coordinates. Frame spring16/8; each widget’s stiffness=7+13×(drift-minDrift)/(maxDrift-minDrift), damping=2sqrt(k)×.95. Vertical sway multipliers in DOM order are[1,.7,1.15,.8,1.2,.6,.9]. Disable pointer drift while progress≤0, on touch or under reduced motion. Measure widget centres on resize, and initialize a mid-runway load to the actual progress. Under reduced motion widgets only fade, glass stays1, composition text appears complete and no large camera approach is used.

## 10. Memory/Agents layout and data animation

Each reading screen is relative,z2 with padding64vh0/24vh0; Agents extends bottom padding48vh. Desktop text width=min(520u,38vw), gap72u. Memory starts at56vw, Agents at24px. Its header gap24u, eyebrow gap16u, title large regular text, continuation and paragraph secondary, paragraph max40ch. Chip lists wrap with8ugaps; chips36u high/12u horizontal padding,10u corners, white .14glass and small type, with8ugap to22u keyboard caps.

Panels have24u padding/gap,20u corners,RGBA40,40,44,.56 glass and local muted#94949a. Panel header is a balanced flex row,16ugap; title medium500, note small muted. Segment controls have4ugap/padding,10u outer corners; tab buttons28u high,12u horizontal padding,6u corners, small500type and selected fill .1/primary ink. Preserve role=tablist/tab, aria-selected, keyboard access and visible focus; changing the selection actually swaps chart data.

| Range | Values | Axis labels | now index |
|---|---|---|---|
| Day |14,22,46,38,18,26,58,44,30,62,40,72 |8AM,10AM,12PM,2PM,4PM,Now |11 |
| Week |48,62,30,24,70,56,66 |Thu,Fri,Sat,Sun,Mon,Tue,Now |6 |
| Month |34,52,28,61,44,22,57,70,38,26,49,63,31,55,72,40,24,58,66,35,47,69,29,53,74,42,36,60,51,68 |Sep22,Sep29,Oct6,Oct13,Now |29 |
| Today |10,10,10,10,10,10,10,10,10,10,84,10,10,10,10,24,24,24,66,40,10,10,10,52,10,92,30,10,10,48,64 |6AM,8AM,10AM,12PM,2PM,Now |30 |

Charts are140u high with4ugaps; bars minimum14u high,2ucorners, fill .06 for future, lavender for previous values>10 and yellow fornow. ScaleY starts0 at the bottom. Enter over900ms expo, delayed320ms+18ms×index. Axis is small muted with Now uppercase, tracking .06em and lavender. Remove/readd growth after two frames when rebuilding a selected dataset, and do not leave stale bars after a range change.

The storage track is28u high, pill, clipped, fill .06; the lavender100% segment reveals by inset from100% right to0 over1400ms expo after420ms. Legend wraps with8u/24ugaps,12u top gap reduction and8udots. The golden-time stat is large with a medium percentage mark separated2u; its label issmall muted. Ticks are48pieces,2u wide,28u rail height,1ucorners, initialY .4; reveal800ms expo after380ms+14ms×index, lavender active/yellow current as defined by the dataset.

For reveal groups, split headings into visually hidden-from-AT word spans while retaining their complete accessible label. A panel itself begins at delay0 and its children at160ms. Traverse eyebrow, title words, paragraph, chip items, panel header/text, stat, chart, ticks, track, legend and note. Words stagger45ms, chips60ms, other pieces90ms, with60ms after the final word.

IntersectionObserver root margin is-12%0/-20%0. Entry adds the visible state and restarts counters; exit removes it and records whether the element left above or below the root centre, so reverse entry uses the appropriate direction. Default reveal:1200ms in/520ms out, y32px, opacity0, blur12u. Above-screen departure usesy-24px; wordsy .35em/1100ms duration; panelsy48px. Chips and panels do not blur. Remove translation/blur at rest. Counters restart at0, delay250ms, last1400ms expo; use en-US thousands and format134minutes as2h14m. Never announce every animated numeric frame to assistive technology.

Element parallax uses -(elementMid-(scrollY+vh/2))×depth, updated in a scroll rAF; skip elements farther than1.5viewport heights and clear translation when remeasuring body resize. Under reduced motion remove parallax/counters/typing/bar/tick/track movement; show their final meaningful values and use only a200ms opacity reveal with no delay.

## 11. Progressive veil, assembly and fallbacks

Append a pointer-transparent fixed16vh strip along the bottom atz2 after content. Fill it with six layered backdrop blurs .75/1.5/3/6/12/24px, without a tint. Layeri uses a vertical mask transparent ati/6, black at(i+1)/6 and(i+2)/6; its next stop at(i+3)/6 returns transparent except where it crosses the end, when it stays black. Clamp percentage stops. This should progressively soften material behind the bottom edge without hiding controls or turning the whole page grey.

Initialize header/clock, smooth corners and reveals; then the cloud and veil; then scroll landmarks and frame choreography; after model readiness initialize cursor/liquid coordination. Install the title-mask callback after those objects are present and update it on body resize. Avoid a race where a late-loaded font/model leaves stale title or widget measurements. A mid-page load starts directly at its current frame/pose rather than playing the entire introduction first.

The source has development hooks and an optional percentage-scroll query; keep such diagnostics out of public customer flows. If retained for QA, make them read-only and never rely on them as a substitute for real browser interaction. Use actual buttons/keyboard navigation for acceptance testing. Treat waitlist/sign-in/agent execution as unconnected marketing actions until their real integrations are supplied; validation or a demo animation is not a successful backend operation.

Phone requirements include the explicit font/header/title/note changes above, readable content, no horizontal overflow, no pointer-only requirements and touch-safe scrolling. For reading columns/widgets, adapt their desktop positioning into a narrow composition that keeps all essential content reachable; disclose necessary responsive implementation choices because the original does not provide every mobile widget coordinate. Do not squeeze a1470px desktop canvas into a phone and call it a separate mobile design. Reduced motion must retain the identity, real point-cloud form, every section and meaningful data without the long simulated camera movement.

## 12. Acceptance matrix

- At1470×956, title ink respects24px rails and the head crosses the lower middle letters through the soft mask. The neutral three-letter brand is measured rather than assumed to have identical glyph metrics.
- At rest, head grains are pale lavender-grey and shoulders pale yellow-green, with only a faint matching haze. Pointer movement adds a white/local full-colour spot, leads the head before the body, creates restrained swirls/streaks and settles in roughly1–2seconds.
- First scroll dissolves title/note upward over700ms. Subsequent scroll scales the stage to .56 on#e8e5ef with28px visible corners; the dense dark-glass header and centred OS headline arrive.
- Seven widgets enter from large blurred foreground scale in .40/.42/.46/.48/.50/.58/.72 order, settle into glass, type the composer and drift with fine-pointer input. Exit reverses their order, returns the ground to black and expands the stage. Reversing scroll reproduces all states without stale timers or hidden copy.
- Memory places a3.3×bust upper-left, facing right, dimmed beneath readable text. Day/Week/Month updates the actual chart and aria-selected. Agents drops70% of grains at peak dust, condenses the body, moves it across and restores it upper-right facing left.
- Check wide, narrow, short-height and rotated viewports; model/font/network failure; no WebGL; reduced motion; keyboard access and mid-page loads. Every real interaction has an honest outcome. No horizontal scroll, clean console, bounded GPU memory, hidden-tab pause and zero idle rAF after springs/liquid settle.

Keep source documents privately as recovery material where redistribution terms are unclear. This public working prompt preserves the operative design and mathematical specification in independently organized wording. It does not grant new rights to external fonts, code or scan geometry, and it does not turn illustrative privacy/agent claims into verified product capabilities.


## Hosted asset map

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | people gallery | [people gallery](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/48d411d5c12622.webp) |
| asset-02 | places gallery | [places gallery](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/9101dd00cbe3b4.webp) |
| asset-03 | head and shoulders point-cloud geometry (59750 points) | [head and shoulders point-cloud geometry (59750 points)](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/0efcd6f363c852.pcd) |

| reference-preview-loop | reference preview loop | [reference preview loop](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/411ddff143bbe1.mp4) |
| reference-preview-poster | reference preview poster | [reference preview poster](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/16d04525efd0ca.jpg) |

Keep the [required geometry notice](https://lapis-slate-xvar.here.now/library/point-cloud-companion/notices.txt) with distributed copies. The two gallery images and exact model were approved in chat for this pack. New or changed media still requires approval.

## Implementation notes

The public example uses ION OS branding while retaining the supplied composition, data and motion. Status navigation targets the framed section. Account/waitlist actions open honest preview dialogs; there is no authentication, signup collection or personal-memory backend. Chart tabs support arrow keys, Home and End. Missing WebGL leaves normal readable page content. These usability repairs do not claim an implemented operating system or backend.

On phones, the example allows a 2.5-viewport-width bust fit instead of the desktop 1.3 limit, so the head stays large while shoulders crop naturally. The framed headline is18px within46vw. Floating photographs use30vw/27vw widths, the toolbar omits desktop shortcut keycaps, the small chart stays within33vw, and composer/toast positions are composed for the narrow viewport. Desktop camera, shader, spring and scroll constants remain those specified above.


## Library preview video

The supplied seven-second reference clip plays silently in a loop in the library card and detail preview while visible. Its first frame is the still fallback for reduced motion or failed playback. This clip is reference media for the pack, not a replacement for the interactive point-cloud implementation described above. Retain the geometry notice with the model.
