# Integrating into an existing marketing hero

The upstream scrub engine is built to own a whole page. Copy and adapt it in the
project for a bounded hero; installing this skill does not modify any existing site.

## Preserve the page

Read the original HTML/components, styles, images, and booking behavior. Keep the
wordmark, headline, rating, form, navigation, and content below the hero. Disable
duplicated engine navigation/copy as needed; never remove the real booking form.

Give the flight an explicit scroll range and a pinned viewport stage, followed by
the normal page in document flow. Derive progress from the hero's position/range,
not an assumption that it owns the entire document. Keep layers outside ancestors
whose transforms, filters, opacity, or containment change viewport pinning; inspect
actual stacking/containing blocks. Do not fade an ancestor of fixed layers; fade
the individual layers. Use `overflow-x: clip` on page wrappers rather than hidden,
which can create an unintended vertical scroll container.

## Scope and release engine layers

The upstream `injectCSS()` includes a global `html,body` rule and wraps defaults
in `@layer sw`. For an existing hero, remove that global rule in the project copy
and scope engine styles to the flight. If the host has an unlayered reset, the
engine's layered padding/margins may lose the cascade: inject the scoped rules
unlayered or explicitly integrate them into the host's known layer order.
Retain the `.sw-*` classes and theme variables; do not globally restyle the site.

The sky, stage, copy, route, hint, and navigation use fixed positioning. Hide or
release **every** engine layer after the hero range (and before it if appropriate),
including opaque backgrounds and interactive overlays. An opacity-zero layer can
still intercept clicks: manage pointer events/visibility too. Hide route text
labels if matching the reference's dots-only rail. Disable atmospheric particles
and gradients for a calm photoreal treatment when the art direction calls for it.

Wire listener/rAF/blob cleanup on component unmount if using a framework. The
upstream function does not expose a full destroy lifecycle; add one in the project
copy rather than claiming cleanup exists. Honor reduced motion and cleanup when
changing between fallback and film.

## Overlay timing and end release

Keep original hero content over the opening still. Fade it out during roughly the
first 0.7 viewport-heights of scroll; keep important controls reachable by keyboard
and avoid invisible form focus targets. Near the end, hold the intended final
image and restore the same hero overlay so dates can still be selected.

Each engine poster is a clip's **first** frame. If the tail should hold the final
frame, supply that still explicitly in the project logic while loading/holding
the end; do not fall back to the last scene's opening poster. Where exact matching
is required, composite the hero still into the head/tail locally before extracting
the boundary images. A short fade is a treatment, not a substitute for verifying
the actual frame.

During the end release bring the next real section behind the held film and fade
the film layers individually. A smoothstep easing can pass through the mixed
frame quickly. Do not leave an empty final viewport of hero spacer after hiding
the film; that produces a full black or blank screen before normal content starts.

## Browser acceptance checks

In an active browser tab, scroll across each seam forward/back, the opening fade,
tail hold, restored form, and release. Confirm scroll drives currentTime and the
normal footer is reachable. Check console/network failures, keyboard navigation,
phone layout, reduced motion, unloaded/failed videos, and correct first-frame
posters. A hidden embedded preview may throttle rAF, so verify in an active tab before
rewriting a functioning scrub engine. Never claim iOS was tested using only a
desktop viewport resize.
