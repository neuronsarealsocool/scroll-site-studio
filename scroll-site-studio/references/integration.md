# Bounded hero integration

Derive progress from the hero and sticky stage, not the entire document. Avoid global
fixed layers covering normal content and ancestor overflow that breaks sticky.
Each `.flight-scene` has its opening picture poster and muted inline video with
data-flight-src and data-flight-mobile-src. Portrait selection is orientation-based;
remount on rotation. Pair every scene's desktop/portrait posters and footage.

The tail is the final decoded frame, not a last scene's opening poster. Timing is
scene-count based. Hide all subsequent scenes initially, not just scene two.
Outer height controls pacing; 720svh is an example for five legs, not a minimum.
Keep normal content and a skip link. Fade the headline early, restore on tail, and
keep invisible copy out of keyboard focus. Reduced motion, save-data and failed
media collapse to the original still rather than a tall empty spacer.

Keep request/listener/rAF/blob cleanup. Prime mobile decoding via eligible user
gestures including touchend, retry rejected or pending priming and coalesce seeks.
The portable engine adds bounded recovery for stuck seeks. This still requires real
device checks; it cannot guarantee every autoplay/low-power condition. A hidden,
throttled preview is not proof that a working engine is broken.
