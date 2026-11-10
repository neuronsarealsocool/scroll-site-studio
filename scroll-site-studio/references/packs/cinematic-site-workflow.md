# Cinematic site workflow

Build a high-end responsive website around the actual business and visitor action.
Use the following planning and implementation method within the chosen project.

## Core working method

1. **Inspect and understand.** Keep the existing project, host and stack. Establish
   the offer, audience, confirmed identity, project scope and real primary action.
   Ask only for facts that materially affect a decision; do not invent trust claims,
   prices or connected business functions. Identify fictional/demo content.
2. **Make a small style tile.** Preserve supplied logos, products and labels. Use
   shared site tokens for typography, palette, controls, representative content and
   imagery treatment. It is a tangible direction board, not a claim that a homepage
   or brand manual is finished. Explore directions when useful; no fixed aesthetic.
3. **Plan the story before footage.** Present a table titled **Visual Story** with
   exactly `Scene`, `Visual story`, `Website copy` as its three column labels.
   Include transition beats, HTML copy/CTA timing and deliberate no-copy intervals.
   Three main scenes can be a starting point, not a mandatory count. Guided mode
   waits at the agreed story checkpoint; autonomous layout work can continue.
4. **Separate pacing from duration.** Add a scroll pacing plan with stable beat IDs,
   enter/exit behaviour, framing, desktop/mobile travel in viewport heights, source
   frame ranges, copy ranges and holds. Keep one timeline configuration. More source
   frames do not create more scroll distance; a frozen frame does not create motion.
5. **Prove a representative implementation.** In the actual project, test a poster,
   pinned region, short representative sequence and one HTML chapter transition
   before producing all dependent footage. Local placeholders are technical checks,
   not finished media. Keep the real page useful before animation completes.
6. **Produce connected media through Replicate.** Maintain a ledger of prompts,
   reference files, model/settings, prediction IDs, status, costs when known and
   local outputs. Start with one candidate per planned scene within the authorized
   budget; avoid indefinite retries. Retrieve pending jobs before resubmitting.
   Inspect a clip's chosen final raster frame before supplying it to the next
   compatible model. Compare spatial joins and motion direction/speed, not just
   similar-looking stills. Model guidance does not guarantee continuity.
7. **Prepare media and build.** Preserve originals; use FFmpeg/ffprobe as appropriate
   for inspected browser assets. Suggestions such as 18fps WebP extraction
   are tunable examples, not universal requirements or playback-rate promises.
   Verify actual frame count, dimensions, numbering, posters and endpoints. Separate
   semantic HTML from generated imagery; keep content and timeline editable.
8. **Verify and hand off.** Test composition, joins, normal/reverse/fast scrolling,
   navigation/actions, responsive changes, keyboard use, reduced motion and failure
   states. Report passed/failed/not-tested results and measured performance with
   conditions. Build success alone proves neither smooth motion nor visual quality.

## Mobile and frame-loading method

Use one responsive website/codebase with separately composed media where needed.
Choose a separately composed mobile asset where the sequence needs one. Choose the applicable scope
explicitly and do not stretch landscape video to claim a portrait deliverable.

Keep navigation above the entire page, outside pinned ancestors. Plan text-safe
areas, focal points and subject bounds per beat, using short-screen layouts that
can flow rather than shrinking copy. Keep primary actions usable before and after
the story; support accessible menus and immediate **Skip animation** behaviour.

Map each beat independently to its frame interval; a hold maps to one frame. Keep
boundary choices consistent in reverse. Request only the chosen variant on first
load and check reduced motion before prefetch. Bound request concurrency and decoded
memory separately; prioritize the current/nearby frames, discard stale responses
and release evicted resources. Use on-demand drawing and bounded pixel density.

On orientation/variant changes, preserve beat and local progress and prevent obsolete
loads from taking over. Reduced motion uses a composed still and normal readable
content without a full sequence download or long pinned spacer. Media failure,
hidden tabs, skipping and teardown must stop unnecessary work while retaining a
useful poster and primary action. Measure transfer and estimate decoded memory
separately; a compressed frame size is not its decoded memory footprint.

Only a small 300x300 transparent product reference is supplied. It is not a high-resolution hero master or finished film.

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

Use these direct URLs in the implementation. [Machine-readable manifest](https://lapis-slate-xvar.here.now/library/cinematic-site-workflow/assets.json)
includes file sizes and SHA-256 hashes. Local manifest: `assets/manifests/cinematic-site-workflow.json`.

| ID | Role | File |
| --- | --- | --- |
| asset-01 | small transparent product reference | [Open asset](https://lapis-slate-xvar.here.now/library/cinematic-site-workflow/media/3d806d062e1143.png) |
