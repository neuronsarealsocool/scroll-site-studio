# Validation record

## 0.3.0 — 10 November 2026

Prepared eight neutral working prompts and 89 distinct media files with SHA-256
manifests. Required vehicle-pack notices and pinned vendor license files retained.
No new media generated, source application executed or existing client site changed.
All 89 hosted media downloads matched file sizes/SHA-256 and returned wildcard
CORS with a localhost Origin. Decoded 72 raster images, parsed two SVGs and probed
15 clips (H.264 plus one HEVC travel asset). A fresh private GitHub clone matched
all 163 backup files, including 152 manifest payload hashes across eight packs.
Archive CRC/document XML and working-prompt URL targets passed inspection.

Package validation, Codex skill validation and the portable self-test passed.
Negative manifest checks rejected an external asset host, invalid byte size and
malformed SHA-256. Pinned vendor integrity is unchanged. Media playback, endpoint
continuity and newly built websites were not browser/device acceptance-tested.

Earlier detailed validation records remain in Git history. Original starter tests
covered Windows creation/install targets, local encoding, archive integrity and
desktop/portrait browser behaviour. macOS, Linux, physical phones and an end-to-end
Claude Code run remain unverified. A pack specification is not tested site code.
