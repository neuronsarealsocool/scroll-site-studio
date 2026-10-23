# Validation record

## 0.2.5 — 23 October 2026

Horizon Estates ingestion: decoded all 15 original PNGs; recorded dimensions and
alpha extrema; visually inspected a contact sheet and checked DOCX CRC/XML. Both
Google document exports were preserved. All 17 file sizes/SHA-256 hashes matched
a fresh restore from the private GitHub backup. No completed theme/code was supplied.
Video title checked; no transcript available. No site, animation, WP runtime or
physical-device test performed; no paid media generation or public source-media upload.

## 0.2.3 — 22 October 2026

Layer source inspection: two ZIPs passed CRC checks; all 14 production images
match byte-for-byte between archives. Inspected prompt DOCX/Markdown exports, hero
PNG, archive trees, theme README/header and block metadata. Five preserved files
were restored from the private GitHub backup and checked against size/SHA-256
manifest entries. Theme expects an absent product CSV. No downloaded theme code
was executed; WordPress/WooCommerce runtime, checkout and physical-device behaviour
remain untested. No new media generation or public source-media upload.

## 0.2.0 — 21 October 2026

Updated workflow scope, default provider, mandatory chat media approval and exact/
adapted/hybrid reuse. Static-site doctor mode makes video/Node dependencies optional;
video and Scroll Craft modes retain the requirements relevant to them. Skill/package
validation and offline integration checks cover the packaged changes. No new media
was generated or published. These are agent instructions, not a technical lock on
all possible publishing tools. Existing template browser checks below are from 0.1.0.

## 0.1.0

20 October 2026. Windows, Python 3.14.3, Node 24.14.1, FFmpeg/ffprobe 9.0.2.

- Skill Creator frontmatter validator passed.
- doctor.py found FFmpeg/ffprobe and required filter/encoder capabilities. setup.py
  --plan printed package-manager commands without installing dependencies.
- Offline media smoke passed: silent H.264/yuv420p, unchanged dimensions, distinct
  first and final decoded frames. No provider API generation was called.
- Integration selftest: copy templates, prevent overwrite, reject private state,
  import a sanitized template/reference, reject query-bearing references, detect
  stale/tampered hashes, install to isolated Codex/Claude directory layouts, and
  create/extract a ZIP with verified per-file checksums.
- JS syntax checks passed for both original starter runtimes.
- Active in-app browser: bounded synthetic demo on 1280x720 and 390x844 viewports;
  media changed from native 1280x720 to native 720x1280 after rotation. Forward and
  reverse currentTime advanced, ending still held and normal page content released.
- Clean static starter rendered without missing media requests; failure fixture
  returned to a normal-height still hero. A forced reduced-motion **test fixture**
  exercised the no-video-source path. This was not a physical OS/device setting test.
- Editorial starter rendered at phone and desktop sizes with no horizontal overflow;
  independent hero planes changed with scroll. No console errors in the normal demos.

Limits: no macOS/Linux execution, real iPhone/Android decoder test, or Claude Code
end-to-end model run. Claude installation layout was tested with the same local
installer, not inside a running Claude instance. Upstream Scroll Craft scripts are
bundled as a pinned snapshot; its external Playwright harness and paid KIE workflow
were not executed. No site was deployed and the working Alder & Form source stayed
unchanged. Placeholder art and test patterns are not finished production media.
