# Point-cloud companion

Create a polished responsive product page built around an interactive point-cloud bust. A transparent three.js canvas remains behind the content. The initial full-screen bust reacts to the pointer; scrolling shrinks the dark composition into a rounded frame on lavender, flies seven glass widgets in from the camera, holds them, then reverses that movement. The bust subsequently enlarges at the upper-left beside a Memory section, dissolves into dust, crosses the page and reforms at the upper-right beside an Agents section. Keep the experience coherent when scrolled backward or loaded partway through.

Use the existing project stack or buildless HTML, CSS and ES modules. Separate the cloud renderer, pointer/liquid simulation, scroll poses, frame choreography, header, reveal system, smooth-corner utility and progressive veil. WordPress is optional. Use a compatible pinned three.js version with PCDLoader, EffectComposer, RenderPass, UnrealBloomPass, OutputPass and GPUComputationRenderer. Do not execute downloaded reference code. Obtain new generated media through Replicate only after agreeing scope and cost; show new or newly selected assets here in chat and obtain approval before publication.

## Composition, tokens and content

Use black as the page ground; dark surfaces #121214, #18181a and #242428; controls #3c3c40; primary ink #fcfcfc, secondary #a4a4aa and muted #88888e. Accent colors are lavender #c8a9eb, yellow #e2e626, cyan #7cf8fa, coral #f0634f and steel #6f83a2. The light frame ground is #e8e5ef, with light ink #17161b/#5d5a67/#8e8a98. Glass uses rgba(24,24,26,.52), blur24u and saturate1.4; light glass rgba(252,252,252,.08). Surface fills have alpha .06/.10/.16 and rules .14. Only the light-mode widget lift uses a shadow: y24u, blur60u, spread-24u, rgba(60,40,110,.18).

Define one desktop design unit `u=clamp(.85px,100vw/1470,1.3px)`. Space steps are 4,8,12,16,24,32,48,72,120,192u; radii6,10,14,20u and a pill. Desktop gutter48u. Body type is16u/1.45 with -.011em tracking, small13u/1.3, large28u/1.15 with -.025em, display56u/1 and giant min(176u,12.6vw)/.86. Use Geist Pixel Square for the title, Geist Pixel Circle where appropriate, and Helvetica Neue with Inter/Arial fallback for body text. Keep font license notices if distributing font files. Default UI timing: press160ms, UI240ms, entry600ms, stagger60ms. Eases: out(.23,1,.32,1), expo(.16,1,.3,1), move(.77,0,.175,1).

Provide a fixed compact glass header with a 3×3 square mark, live local HH:MM:SS clock, status indicator, Status/Agents/Memory navigation, Sign in and Join the waitlist. This is a marketing demo; only claim real authentication, waitlist submission or agent actions when connected. The hero uses a large two-part pixel greeting and a lower-left private-beta note explaining a companion that remembers locally and asks before acting. Memory content covers people, places, promises and preferences, an interactive Day/Week/Month chart, remembered/deleted counters and a storage panel showing device100%/cloud0%. Agents content covers time saved, a today chart, handled/waiting counts, a78% figure and48 activity ticks with37 active. Treat these values as demo data, not actual product measurements.

Keep layers in this order: page ground; fixed stage z1 containing title, canvas and frame heading; content screens z2; progressive bottom veil z2 later in DOM; OS widgets and hero note z3; header z10. Use overflow-x:clip and overscroll-behavior:none. The stage itself must not intercept pointer events. Preserve accessible headings, real section anchors, labelled controls and static text equivalents for visual statistics.

## Header and hero geometry

Header is centred12px from the top, maximum width viewport minus24px, with4px inset and40u controls. Its bar is rgba(64,64,72,.55), blur24u, saturate1.4, brightness.5, radius14u. The mark is40u square with4u pixels and3u gaps. The status dot is6u cyan, pulsing over1.8s. A light-ground state darkens the bar to rgba(24,24,28,.72) and transitions colors/background400ms. Hide status at≤1100px. At≤767px position the header8px from all top/side edges, remove rules, nav and Sign in, and put the waitlist action at the right. Update the clock at the next second boundary with `1000-currentMilliseconds+5`; do not announce every second through aria-live.

The title is behind the canvas, centred, with font size `(100vw-48px)/6.536` so its ink stops24px from both screen edges. Its vertical position is bust-top+40px with translateY(-50%). Cut a radial transparent window behind the projected head: transparent through64%, opaque by100%; update the centre from the head's projected NDC and the title box. RadiusX is headPixelWidth*.5/.64; radiusY is headPixelHeight*.5*1.08/.64. Write rounded CSS values only on change. On phones use two block lines, font size `(100vw-48px)/3.192` and left-.038em.

The desktop hero note is fixed24px from left/bottom, large body size, with a small meta row24u above it. The phone note becomes an8px-inset glass card with16px padding and16px body copy. Initial title/meta/lead entries use blur12px and Y16px over600ms, staggered0/60/120ms. On hero exit, title moves up4vh, scales.97 and blurs16px; meta/lead move up16px and blur10px. Exit opacity takes700ms and visibility changes after760ms; return takes1100ms, with meta/lead delays80/160ms. Reduced motion uses only a200ms opacity change.

## Bust asset, camera and particle rendering

The manifest must supply one binary PCD bust and two640×430 gallery images for People and Places. Never substitute later car-film adaptation assets for the original bust or widget pictures. Rotate the PCD by Xπ, then Y.05 and X.19. Compute its bounds; centre Y/Z conventionally, but derive X from the median centre of48 horizontal rows across the top45% of its height. Put the points in a rig pivoting at the bust base with YXZ rotation order.

Camera FOV30°, near/far .01/40. Bust target height is.78 viewport height, bottom bleed.07 and maximum width1.3 viewport widths. Point size.005, head centreY.10. Fit view size to max(modelHeight/.78,modelWidth/(1.3*aspect)); cameraZ=view/2/tan(FOV/2). Keep unitsPerPixel=view/hostHeight and update the CSS bust-top. Place a pose by targeting the head in NDC rather than the model's bounding-box centre: rotate/scale the head offset, compute the camera half-height at the rotated head depth, and subtract that offset when positioning the rig. Use the complete pose plus gaze for final rotation; retain projected head dimensions for title masking and content veiling.

Use an alpha WebGL renderer without antialiasing, DPR capped2 and transparent black clear. Composer uses a HalfFloat target without MSAA: RenderPass, bloom strength.020/radius.9/threshold0, then OutputPass. Bloom should preserve hue while compressing its luminance with exponent.60, rather than applying a color tint. Run bloom blur at CSS resolution with kernels3,5,7,9,11 and a four-tap high-pass average. Preserve alpha at least as high as the brightest output channel so the faint haze survives compositing.

Render one instanced quad per point, with aHome and aRef attributes; reference texels occupy a power-of-two square with side `2^ceil(log2(sqrt(pointCount)))`. Keep the mesh uncullable. Until liquid interaction exists, use a zero float texture for state and flow. Base uniforms include streak.8, gradient centre(0,.10), gradient radius.40, grain.335, scatter0 and dim0. The touched gradient goes white at0%, lavender at32%, yellow at100%; the resting gradient keeps lightness/hue but multiplies OKLCH chroma by.6. Blend touched color by local flow ink*.6.

For dust use deterministic per-point random vectors. Scatter displacement and drift scale with scatter², fling amplitude .05 and slow oscillatory drift.01; drop70% of grains by full scatter and shrink the survivors45%. Convert simulated point velocity to a screen-aligned streak: projected velocity length times1.25, capped18px, weighted by streak.8. Dither the trailing fragment rather than drawing a solid rectangular tail. Add overlay film grain at.335. On Memory/Agents, dim particles according to projected head distance and which side faces the text, keeping the head legible without competing with the copy.

## Scroll pose and pointer dynamics

All springs use mass1, semi-implicit Euler substeps≤1/240s and frame dt clamped0–.25s. Snap when abs(error)<eps and abs(velocity)<10eps. Pose stiffness/damping30/11; dust26/10; gaze yaw/pitch110/15; roll45/9; screen float10/6; gradient18/8. Gradient eps1e-5; others1e-4. Run animation on demand, pause on visibilitychange, and stop when springs, dust and liquid settle. Loading mid-page must immediately snap to the correct scroll pose before the first reveal.

Measure OS, Memory and Agents tops on body resize. Left pose is x-.66,y.64,scale3.3,yaw.48,pitch.03,roll-.28; right mirrors x/yaw/roll. OS influence enters across .12–.8vh from its top and leaves2.2–3.2vh; centre drops.08 NDC during that phase. The move toward Memory spans -1 to-.2vh relative to its top. Agents transfer spans -.6 to+.1vh: normalized u drives side=smoothstep(.3,.7,u), dust=smoothstep(0,.4,u)*(1-smoothstep(.6,1,u)); shrink by1-.42*dust. Interpolate centre toward left/right using the Memory transition; dim by that same transition and hero weight=1-OS-entry.

Enable pointer interaction only for hover-capable fine pointers without reduced motion. Intersect a camera ray through the pointer with depthD=.41, using the transformed stage rectangle. Clamp yaw±.6, pitch[-.35,.3], weight by hero influence, and set roll=-.18*yaw. On content screens use normalized pointer float at x*.035/y*.05 and yaw*.07/pitch-*.04. Track gradient centre by intersecting the pointer ray with local Z0 and clamping to the model box plus.1. On pointer exit ease gaze back to zero; if the input media query changes to disabled, reset interaction immediately.

Initialize GPU liquid only on the first valid pointer move. Use HalfFloat ping-pong state and flow at the point-reference texture size. Flow spans the model's largest XY extent plus.3. Set radius150px, inkRadius110px, strength.5, spread1, turbulence.6, return1.2. Normalize frame f=clamp(dt*60,.25,3); pointer smoothing is1-(1-.22)^f. Presence attack.1/release.035; a pointer stationary1500ms counts as absent, and simulation may decay for270 more frames. Clamp wake velocity±60, smooth it.5, pass wake/40 clamped±1. Flow decay=.968^f and inkDecay=.97^f. Advect by flow*texel*2.5 and diffuse with centre.52 plus four neighbours*.12. Apply radial/swirl forces1.25/1.45, flow-following42*.08, curl turbulence on scale.0095, and return force `.006+.02*return`. Velocity damping interpolates.93–.955 with energy. Zero offsets/velocities when both squared magnitudes are below.0004. Feed the resulting textures back into the point shader.

## Framed OS choreography

The hero consumes no document height. OS occupies420vh and contains a sticky100vh pin. Scroll coordinate s=clamp((scrollY-osTop)/vh,0,3.2), smoothed by26/10. Entrance length1.7, hold.5, exit1.0; q=clamp(p/1.7), o=clamp((p-2.2)/1). Apply hero-out above raw s.05 and remove below.03. Frame amount k=easeInOutCubic(segment(q,.06,.5))*(1-easeInOutCubic(o)); scale=1-.44k and visible radius=28px, implemented as28*k/scale. Pointer frame drift is-4*k times a16/8 spring. Ground reaches lavender over q.1–.42 and returns over o.3–.9; header switches above half ground transition. Frame heading enters q.2–.44, exits o0–.4, with24px rise,10px blur and inverse .56 scale compensation.

Seven widgets appear in this order: tools at.40, People.42, chart.46, Places.48, add image.50, composer.58, toast.72. Each entrance lasts.22 of q. Exit order reverses the threshold order; exit start is `i*(1-.45)/(n-1)` and exit length.45. Initial perspective-like scale3.6, blur44px with exponent.55, glass threshold1.5. For entrance e=easeOutExpo(t), exit eOut=tOut^2.2, scale=1+2.6*((1-e)+eOut); offset each card centre by centre*(scale-1), then add its pointer drift weighted e*(1-tOut). Fade with smoothstep entrance t/.45 and exit (tOut-.3)/.7. Glass amount=clamp((1.5-scale)/.5). Stop writing styles when unchanged.

| Widget | Position | Size | Z | Drift |
|---|---|---|---|---|
| People | left12vw,top25vh | 200u×170u | 4 |12 |
| Places | left15.5vw,top47vh |160u×136u |6 |16 |
| Add image |left5vw,top48vh |contents with6u/12u padding |7 |18 |
| Tools |left61vw,top25vh |three32u chips |3 |9 |
| Chart |left73vw,top33vh |width250u, padding16u |5 |14 |
| Composer |centred,top78vh-20px |width560u,padding16u |8 |6 |
| Toast |left70vw,top68vh |height48u |9 |11 |

Each card drift spring has stiffness7+13*(drift-min)/(max-min), damping2*sqrt(k)*.95; vertical weights are1,.7,1.15,.8,1.2,.6,.9 in DOM order. Ignore pointer drift before OS progress begins, on touch and under reduced motion. The chart grows after landing, stagger40ms; composer begins350ms later at34ms/character. Reverse these states when leaving. Reduced motion fades widgets only, uses full glass and displays complete text.

## Data, reveals and final checks

Memory Day values are14,22,46,38,18,26,58,44,30,62,40,72 (now11). Week:48,62,30,24,70,56,66 (now6). Month:34,52,28,61,44,22,57,70,38,26,49,63,31,55,72,40,24,58,66,35,47,69,29,53,74,42,36,60,51,68 (now29). Default range Week. Agent today values:10,10,10,10,10,10,10,10,10,10,84,10,10,10,10,24,24,24,66,40,10,10,10,52,10,92,30,10,10,48,64 (now30). Demo counters:1204 remembered,312 removed;134 minutes saved;3240 handled this week;3 awaiting a decision;78% handled,22% requiring attention. Do not present these as real telemetry.

Content screen columns have width min(520u,38vw),72u gaps, padding64vh 0 24vh; Memory starts56vw from the left, Agents24px, with an extra48vh final bottom pad. Use a responsive stacked version on narrow devices so content does not remain38vw wide. Panels have24u padding,14u corners and dark translucent glass. Their stat bars are140u high, bottom-aligned, with lavender past data and yellow current data. Enter on IntersectionObserver rootMargin -12% top/-20% bottom; reveal words45ms apart, chips60ms and other pieces90ms, beginning panel internals160ms after the panel. Entry duration1200ms, exit520ms; title word entry1100ms; translate32px and blur12px. Counters start after250ms, run1400ms ease-out expo, and use locale grouping or hours/minutes formatting. Apply content parallax depths.04/.06/.1 only within1.5 viewports of visibility, and measure without the previous translate applied.

Add a fixed16vh progressive bottom blur with six layers of.75,1.5,3,6,12,24px and staggered linear-gradient masks; no tint. Rounded elements use60% smoothed corners if a squircle path utility is available, recomputed by ResizeObserver; border-radius remains the fallback. At≤767px set u=100vw/430, body floor15px, small floor12px, large floor22px and gutters16px. Reduced motion removes dust, liquid, gaze, drift, parallax, counting, bar/tick/caret animation and large transforms. Verify forward/reverse OS phases, reload within every chapter, light/dark header contrast, chart tabs, mobile overflow, WebGL/PCD failure, keyboard paths, and a genuinely idle render loop.

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | people gallery | [people gallery](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/48d411d5c12622.webp) |
| asset-02 | places gallery | [places gallery](https://lapis-slate-xvar.here.now/library/point-cloud-companion/media/9101dd00cbe3b4.webp) |

The gallery files above do not replace the head point-cloud geometry. Keep an exact recreation pending until that geometry is supplied and approved. An explicitly labelled procedural fallback may be used in an adaptation.

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
