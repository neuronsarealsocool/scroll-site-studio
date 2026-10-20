# Grow the library

Keep the entrypoint short. Guidance belongs in references, runnable starters in
assets/templates, and discoverable entries in catalog.json. Add a template for a
different structure/interaction, not every palette change.

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
