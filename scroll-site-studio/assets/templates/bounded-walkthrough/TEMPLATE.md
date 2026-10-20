# Bounded walkthrough starter

Static, framework-free semantic HTML/CSS/module JS. Sample identity is fictional.
The SVG is original schematic placeholder art, not a generated property render.
No business form or analytics/backend is connected. No external fonts or images.

Default data-media-ready=false renders a normal one-screen still hero. Hidden film
posters are only assigned when the engine is enabled, so the clean starter has no
missing-image requests. Provide assets/film or use media.py demo in a **copy** of this
template for synthetic test footage. Set data-media-ready=true only after all paired
clips/posters exist. The two supplied scene slots are arrival and threshold. Add
more .flight-scene blocks and update the tail to the final scene's decoded last JPG.
For each new name supply name.mp4, mobile-name.mp4 and first/last JPGs for both.

The default two-leg scroll span is 480svh. Reassess pacing when adding scenes; the
five-leg case used 720svh. Timings depend on scene count. Portrait is native 9:16
when supplied; CSS does not generate that file. Rotate to reload the selected chain.
On reduced motion/save-data/media failure, the normal still hero remains usable.
The bounded engine releases into #introduction and the ordinary page/footer.

Serve on loopback using the skill's serve.py or another local HTTP server. ES module
imports do not reliably work through file://. Inspect browser console, loading,
seams in both directions, small/desktop widths and keyboard access. Physical iOS/
Android testing is separate. Motion mechanics are not a guarantee of exact 3D rooms.

Runtime derived from Scroll World, MIT copyright 2026 cyw. See assets/SCROLL-WORLD-LICENSE.
Original starter/integration additions use the package MIT license.
