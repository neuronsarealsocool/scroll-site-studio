# Cinematic wipe studio

Create a standalone film-studio landing page with full-screen, scroll-controlled footage and bold red typography. This pack was recovered from a complete single-file HTML implementation. Keep editable semantic HTML, CSS and JavaScript; adapt it into the existing stack when requested. The defining behavior is one continuous film timeline displayed across three synchronized reveal layers, rather than separate unrelated clips. All supplied media URLs are listed in the asset map. New generation defaults to Replicate with a confirmed budget and chat approval before hosting.

## Visual system and content

The page ground is black; footage is displayed at full opacity without a global tint or filter. Red #EB0004 is the strong graphic accent. Use BBH Bartle for the masthead/graphic labels, Alex Brush for script accents and Inter Tight400/500 for supporting copy, with system fallbacks. Base the desktop composition on1470×956 while imposing readable floors on small text. Display type is13.6054vw (200px at1470), the large statistic6.8027vw (100px), work titles max(24px,3.4014vw), UI max(13px,2.0408vw), microcopy max(11px,1.0204vw), title gap max(10px,1.6327vw), header horizontal padding max(16px,2.7211vw) and top inset max(16px,2.1769vw). Use cubic-bezier(.16,1,.3,1) for expo easing; do not apply global negative tracking.

A fixed header divides into three equal flexible columns between the page rails. Present a studio wordmark, a useful work/about navigation and a genuine contact destination. The opening identity is oversized and precisely aligned. The next chapter introduces selected film work with two columns of project titles and supporting descriptions. The closing chapter combines a large Clients counter, a concise studio proposition and contact/footer information. Content remains selectable/readable and links must work independently of the visual effects. Example project/client data is demonstrative until replaced with real content.

## Stage and wipe geometry

Pin one stage to the viewport with video/canvas media covering its complete bounds. Above it place two centred overflow:hidden reveal rectangles. These are geometry windows, not feathered clip masks. Their width grows with normalized reveal progress while their rotation changes; counter-rotate the full-viewport media inside so the picture stays upright. The inner media always remains100vw×100vh and centred; it must not stretch with the opening rectangle. Add only a1.01 inner scale to avoid subpixel fringes, and use backface-visibility:hidden/translate3d where needed.

First reveal: angle=-45°×progress; width=progress×(72vw+72vh); height=72vw+72vh. This diagonal span follows the coverage requirement W cos(theta)+H sin(theta), with a small margin. Second reveal: angle0°, width=progress×102vw, height102vh. Do not reuse the diagonal span for the straight wipe, which would finish coverage prematurely and waste the final motion. Both boxes sit at50%/50%, translated -50%/-50%. Keep hard edges and black backgrounds before frames decode. Hide covered lower layers after coverage completes so they no longer composite. Fade the base stage only at the tail of the first reveal, with coverage verified near .93–.98 instead of revealing black too soon.

## Shared decoding and scroll clock

Provide a900vh runway, approximately300vh per visual chapter, and derive normalized progress from the actual scrollable span. Decode the continuous source once into a shared frame bank where WebCodecs/demuxing is supported. Reuse that bank across all three layer canvases. Bound decoding resolution/frame count/memory for mobile; do not eagerly retain unbounded full-resolution frames. Use a genuine HTMLVideoElement seeking fallback when WebCodecs or the demuxer fails. Draw the correct cover crop and retain the last valid frame during asynchronous seeks.

Each incoming wipe layer runs one second ahead of the layer underneath. For source duration D, reserve total lead2seconds and set each layer’s target to p×max(0,D-2)+i×1second, clamped to D for indices0,1,2. Smooth the actual time using a delta-time exponential response, snap when within the chosen small tolerance, and render only visible layers. Reserve that lead inside the duration so the top layer reaches the final frame at p=1; simply adding time to p×D would freeze it early. Reverse scrolling must use exactly the same mapping. Under reduced motion, hold a useful still and expose all text/navigation without requiring the cinematic sequence.

## Typography choreography

Drive title, statistic, about-copy and work-strip states from the same normalized scroll value. Each top-level group has its own visibility band. Copy moves into a readable middle region, fades as it approaches the header and the lower viewport edge, and leaves without lingering over the next chapter. Base that band on element edges, not just centre positions: take the lesser of eased top-distance/header-clearance and bottom-distance/fold-clearance. Re-measure after fonts load, viewport resize and orientation change.

The work strip initially travels from below the viewport to its measured pin position, then holds. The work heading has its own entrance interval and temporary blur proportional to (1-opacity)²×6px. Apply blur only while entering/leaving; remove the filter completely when settled to avoid a permanent costly blur surface. Descriptions share a centre-to-right rail; use min-width:0 and measured widths to prevent horizontal overflow.

Arrange selected works as two centred columns, with paired rows and generous gaps. As the final release begins, pairs leave top-to-bottom: the left column goes left and the right goes right, accelerating with ease-in. Keep their flight progress separate from normal band opacity. Reduced motion keeps rows in place and removes travel/blur while preserving the content. The large counter and logo share a typographic slot; scale them together rather than applying an independent mobile font floor that breaks alignment. Count only the intended Clients figure, not every numeral in the interface.

## Production checks

Avoid multiple continuous media decodes for the same clip, and pause work when the document is hidden. Recalculate measurements from current viewport dimensions; do not rely solely on a resize event being dispatched by an embedded environment. Loading, missing media and unsupported decoding must yield a readable useful page, rather than an endless loader. Confirm the MP4’s native dimensions, duration, codec and seekability with ffprobe; prepare a compatible H.264 faststart copy only if necessary and approved.

Test opening, both wipe boundaries, text entrances/exits, work row departures and the tail in forward and reverse directions. Inspect intermediate reveal states for uncovered corners, diagonal sampling fringes, distorted media, early frozen frames and lingering compositing layers. Check phone and desktop composition, landscape/short viewports, browser zoom, keyboard navigation, reduced motion, media failure and offscreen behavior. Do not publish diagnostic globals or developer controls as customer-facing features. This is a film-led presentation; connect real enquiries and real project destinations before describing business flows as complete.

## Hosted asset map

Use these hosted copies for the named roles. Media access does not grant additional rights. Keep required notices and verify intended-use rights.

| ID | Role | Direct asset URL |
|---|---|---|
| asset-01 | continuous banner film | [continuous banner film](https://lapis-slate-xvar.here.now/library/cinematic-wipe-studio/media/771f2e092bee41.mp4) |

## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.
