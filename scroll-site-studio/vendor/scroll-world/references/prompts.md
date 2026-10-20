# Art and camera prompts

Keep a shared design preamble across stills and clips. Read the supplied images;
name real materials, fixtures, furniture colors, and openings rather than inventing
them. Keep API parameters outside the prompt and use the selected model's schema.

## Architectural references

Record the actual building's cladding, structure, window frames, interior materials,
furniture, lighting, geography, and approved room order. For new fictional buildings,
agree on these details once. For real properties use a supplied floor plan; do not
claim invented room connections are accurate.

Example Vesper preamble (use only when it matches the inspected references):

```text
Photoreal architectural film of the same lakefront cabin throughout: black-framed
glass, charred cedar cladding, and the approved interior fixtures and furnishings.
Cool blue-teal dusk ambient; warm amber only from lamps and fire; natural white
point; do not oversaturate into orange. Empty, unoccupied, no people. No text,
captions, logos, cuts, or changes to the building's design.
```

Match the palette and time of day across approved source images before motion.
Avoid mixing independent room images that disagree about windows or floor levels.
Use image editing/reference inputs only when supported by the chosen image model.

## Architecture A: continuous walkthrough

First frame: hero image for leg one, then the previous leg's actual final frame.
Last-frame target: approved destination room image composed ahead of the camera,
or the next existing clip's first frame when repairing a middle leg.

```text
[SHARED DESIGN PREAMBLE]
One continuous cinematic architectural camera move. Continue the same slow,
steady forward glide from the supplied first frame. Move through [ACTUAL OPENING]
into [DESTINATION], preserving [OBSERVED MATERIALS, FIXTURES AND FURNITURE].
The camera only ever moves forward and never pulls back. [OPTIONAL GENTLE CRANE
OR LATERAL DETAIL THAT FITS THE ROUTE]. No teleporting through solid walls.
In the final second, settle into a slow steady forward glide toward [NEXT ROOM].
```

Ending on an exterior view is appropriate only if the route really returns there.
Pin the closing target to the hero image if a repeatable opening/closing is desired,
but inspect the generated route for implausible motion. A fade cannot fix an
impossible floor plan. If exact opening/tail pixels are required, use a short
local composite into the clip and extract handoff frames from that final version.

Locked isometric variant: replace the free camera clause with:

```text
The camera keeps exactly the same high isometric angle throughout: no rotation,
orbit, or tilt. It travels straight and level, the world sliding beneath the view.
```

## Architecture B: miniature scene stills

```text
Isometric [MATTE CLAY / PAPERCRAFT / TOY] diorama, cohesive palette [PALETTE],
on a plain solid [BACKGROUND] with a soft contact shadow. [SHARED LIGHTING].
Subject: [SCENE WITH CONCRETE PROPS]. Centered composition, space for the camera
to enter, no text, letters, numbers, or logos.
```

Use a solid background for the video input. Optional transparent versions are
for posters/visual composition, not the full-frame video start image.

## Architecture B: dive

```text
[SHARED DESIGN PREAMBLE]
One continuous cinematic move, no cuts. Begin high and far, looking at the whole
[SCENE] like a miniature. Glide forward and descend toward [FOCAL POINT].
[ROOF OPENS TO REVEAL INTERIOR / CAMERA FLIES LOW ACROSS OPEN SCENE].
Smooth restrained motion and parallax, no text or captions.
```

## Architecture B: connector

First frame: dive i's actual last frame. Last-frame target: dive i+1's actual first
frame. These must be extracted from the rendered clips.

```text
[SHARED DESIGN PREAMBLE]
One continuous camera move, no cuts. Smoothly rise out of [SCENE i], glide across
the same connected miniature world, and arrive above [SCENE i+1], beginning to
descend toward it. Preserve the supplied boundary compositions and lighting.
```

For all styles, inspect motion as well as stills. A matching seam can still stutter
if speed or direction changes abruptly. Keep clip prompts and model settings in a
local manifest; retries and model switches must stay inside the agreed spend.
