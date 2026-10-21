# Grow the library

This library covers high-end websites broadly; a template does not need scroll effects.
Prompts, templates and assets support verbatim reuse, guided adaptation and hybrid use.
Read creative-direction.md when recording locked/flexible elements and source versions.
Keep new media local until explicitly approved in chat for publication; adding a source
to a private working library is different from publishing it in a repository/release.

Keep the entrypoint short. Guidance belongs in references, runnable starters in
assets/templates, and discoverable entries in catalog.json. Add a template for a
different structure/interaction, not every palette change.

Default to independent online backups for source documents and assets, not reliance
on the original Drive links. Follow source-backups.md for authorized private storage,
immutable snapshots, manifests and restore verification. Keep backup access separate
from permission to publish media. Record verified backup details in the pack catalog.

A source pack need not be runnable code. A video, long prompt document, reference
screenshots, original images and optional finished theme are enough. Register it in
catalog.json reference_packs with a unique id, description, local index path and HTTPS
source links. Put the short index under references/packs; preserve original prompt
documents and assets outside the public repository when redistribution terms are
unclear, using a separate private online backup as well as local files. The Frostwood
entry demonstrates this structure. Do not force a WordPress
theme through the HTML-only add-template importer.

```text
python scripts/catalog.py add-template --id my-template --source /path/to/sanitized-site --title "My template" --description "When it fits" --license MIT
python scripts/catalog.py add-reference --id useful-reference --url https://example.com --title "Useful reference" --notes "What to learn, not copy"
python scripts/validate.py
python scripts/release.py --out /path/to/releases
```

Imports refuse existing IDs/destinations, private state, caches and symlinks. Review
rights yourself; a scanner cannot establish copyright ownership. Include TEMPLATE.md
with working behaviour, expected assets, dependencies, limits and provenance. Source
references are URLs/notes, not redistribution permission for screenshots or assets.
Client footage and hosting identity do not belong in templates by default.

Version package.json and SKILL.md together, with a concise CHANGELOG entry. release.py
validates and creates a ZIP, SHA256SUMS.json for its files, and an archive checksum.
Stale hashes fail validation after edits; review changes before --write-hashes or a
new release. Keep runtime state outside the skill. Installs never auto-update.

Vendor updates are explicit: stage separately, retain license/commit provenance in
vendor-manifest.json, review differences and rerun tests. Adding references must not
run upstream installers, overwrite the primary skill or change a live site.
