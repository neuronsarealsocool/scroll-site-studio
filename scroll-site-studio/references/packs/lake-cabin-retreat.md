# Lake cabin retreat - Incomplete Prompt - Watch YouTube Video First

**Incomplete prompt — watch the YouTube video first.** [Watch on YouTube](https://www.youtube.com/watch?v=GJxchJkk4Lk) and review the [lake cabin website](https://www.thebreadcrumb.co/resources/vesper-built/view/Vesper.dc.html) before using this partial working outline.

Use this incomplete reference outline to plan a responsive marketing and booking website for a private whole-home cabin beside a quiet mountain lake. The reference brief has three usable stages: build the hospitality page; optionally replace its hero with a connected camera flight; or integrate that flight into an existing approved page. Agree which stage applies. Keep the chosen project stack; WordPress is optional. Use the prompt directly, adapt the brand and setting, or combine selected sections with another reference.

## Art direction and content

The house sleeps six and accepts one booking at a time. Establish a calm evening atmosphere with deep teal #16292D and #1F3A3F, cream #F4F1EA, amber #F5A623 and mist #A8BDC3. Use thin Darker Grotesque display headlines and Hanken Grotesk body text, generous negative space, small uppercase eyebrows with one amber dot, and 20px card corners. Avoid decorative gradients and generic travel decoration. The exterior is a consistent black-framed glass cabin with charred cedar and warm interior lighting. Do not let separate images imply different buildings.

Build these sections in order: fixed transparent navigation that gains a solid background on scroll; full-height hero film; short host introduction and property facts; interior spaces; amenities on a dark teal field; masonry gallery; reviews; rates and availability; host contact; closing film; oversized footer wordmark. The hero includes a subdued large wordmark behind the house, “Where the evening slows down.”, a booking card with check-in, check-out, guest stepper and availability action, and a clearly labelled example rating of 4.9 from 214 stays. Label fictional review and property data as demonstration content until the owner supplies genuine information.

The host note explains the evening-star name and introduces the stay. Example fact blocks: six guests, 180 feet of shoreline, 40 minutes from the foothills and complete privacy. The space grid contains great room, kitchen, primary suite, soaking bath and reading nook. Amenities include cedar hot tub and sauna, lakeside fire pit, private dock and canoe, followed by an included checklist. Contact shows host names, email, phone and location using owner-supplied values before production.

Use an illustrative nightly rate of $540, two-night minimum and a separately configurable cleaning fee. Compute nights from local calendar dates, handle month/year boundaries and daylight-saving changes without fractional nights, prevent departure before arrival, cap guests at six and display the complete total before submission. Native date controls need visible labels and inline validation. Availability requires a real calendar integration; a calculation or local success state must not claim a reservation was made. Connect a genuine booking destination when supplied.

## Media brief

This pack includes the approved five-second hero loop and first-frame poster. The remaining property imagery and any full connected walkthrough still need owner-supplied or generated assets. Obtain approved owner photography or generate a coherent set with Replicate after confirming model, aspect ratios, resolution and budget. Show every new result in chat and obtain publication approval before hosting it. Do not substitute another provider automatically.

- Exterior hero, 16:9: straight-on front, cabin low and centred, land connection at left, blue-hour mist over water, amber windows, chimney smoke and open sky for the wordmark.
- Great room, 4:5: double-height glazing, wood stove, low linen sofa and soft lamplight.
- Kitchen, 4:5: matte black cabinets, honed soapstone island, pine-framed window and kettle steam.
- Primary suite, 4:5: low linen bed beside glass with first-light lake fog.
- Bath, 4:5: carved stone tub, forest window, candle and rain.
- Reading nook, 4:5: built-in window seat, wool throw, book and wet glass.
- Hot tub and sauna, 5:6: cedar deck, steam, dusk and warm light.
- Fire pit, 5:6: two chairs, wool blanket and mountain silhouettes.
- Dock and canoe, 5:6: still dawn water and cedar construction.
- Exterior day, 16:9: wide shoreline establishing view of the same building.

For the initial atmospheric hero, animate the approved exterior with locked exposure, restrained mist, smoke and fire. The source treatment uses calm 0.6× playback and a 1.2-second crossfade between two stacked videos at the loop boundary. Confirm playback duration and visible seam on the actual encoded result. Reuse the approved loop in the closing section; pause it offscreen and provide a still for reduced motion.

## Optional connected walkthrough

Before generating a flight, inspect all supplied room images and approve a route/floorplan. Photographs do not establish unseen corridors. The intended seven-leg story is lake arrival to deck, great room, kitchen, reading nook, bedroom, bath and departure over water. Keep the original hero copy, rating and booking card, fading them out over the first roughly 0.7 screen heights. Reveal the same overlay again over the final held still so dates remain usable.

Generate sequentially through Replicate using verified current schemas. Each subsequent clip starts from the preceding clip’s actual decoded final frame, with the approved destination room image supplied when the model supports it. Inspect each handoff before continuing. Describe actual materials, forward-only movement, a slow forward glide in the last second, cool blue-teal dusk and amber light confined to lamps/fire. Keep rooms unoccupied. A model failure does not authorize paid retries or a provider change; preserve successful outputs and reconcile prediction status before resubmitting.

The historic brief targeted seven 8–10 second legs at native 1080p. Treat this as a creative target, not current availability or a preapproved spend. Use ffprobe to inspect frame timing. Extract the actual last decoded frame, rather than assuming a near-tail seek is frame exact. For an isolated repair, condition its end on the next accepted clip’s first frame where supported. If the start/end must match the approved hero precisely, composite that still over approximately 0.35 seconds at the head/tail and inspect the result. Encode browser-delivery H.264, yuv420p, CRF20, GOP8, faststart, no audio; save each clip’s first frame as its poster and the final intended still separately.

## Integration and acceptance

Scope the flight to the existing hero and release its layers after that runway. Fade fixed layers separately: ancestor opacity or transforms can change containing blocks. Keep the host page reset from defeating layered engine CSS; remove engine html/body styling and use overflow-x:clip where hidden would create a second scrolling container. Keep only route dots when labels crowd the page. At completion, hold the explicit final still and dissolve into the next section as it enters, with a smoothstep blend and no black gap.

Compose a separate phone layout and portrait film only if approved; a crop is not a separately generated portrait. Test forward and reverse scrubbing at every seam, restored overlay, loading poster, final hold, release, reachable footer, keyboard controls, reduced motion, failed media, booking validation and readable mobile grids. Use the host’s supported browser tools and inspect document visibility when animation appears stalled. Report real-phone checks separately from emulated viewport checks.

## Hosted asset map

[Machine-readable asset manifest](https://lapis-slate-xvar.here.now/library/lake-cabin-retreat/assets.json). Approved five-second hero loop and first-frame poster only. Interior imagery and a full connected walkthrough are not included.

| ID | Role | File |
|---|---|---|
| asset-01 | lake hero loop | [Open asset](https://lapis-slate-xvar.here.now/library/lake-cabin-retreat/media/a7fbc22c28bd68.mp4) |
| asset-02 | lake hero poster | [Open asset](https://lapis-slate-xvar.here.now/library/lake-cabin-retreat/media/a8457947339765.jpg) |

The loop is a silent 1920×1080 H.264 browser-delivery copy of the approved 3840×2160 source, preserving the full 16:9 composition and approximately 5.04-second duration. Use the poster for loading and reduced motion. This is a landscape preview, not a separately generated portrait sequence.


## Reuse and scope

This is the complete public working specification for this pack, independently worded from the recovered brief. Detailed neutral source documents and implementation bodies are retained in the owner’s private backup; they are not redistributed as public source code. Use this working prompt verbatim, adapt it or combine it with other references. Keep the existing stack; WordPress is optional. Replicate is the default for new generated media. Confirm costs before spending and approve the actual media in chat before publication.

## Live website reference

[View the lake cabin website](https://www.thebreadcrumb.co/resources/vesper-built/view/Vesper.dc.html). This is the live example supplied for this pack. The property media remains a generation/supply brief; linking the example does not bundle or approve new media.

## YouTube reference

[Watch on YouTube](https://www.youtube.com/watch?v=GJxchJkk4Lk)
