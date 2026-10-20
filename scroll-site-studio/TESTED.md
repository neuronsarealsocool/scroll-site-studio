# Validation of 0.1.0

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
