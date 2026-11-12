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
from permission to publish media. Record verification details in private backup state; public catalogs link only to working prompts and hosted asset manifests.

Every current and future pack must default to platform-neutral design reuse.
Record the source platform privately and any theme as optional example code;
do not turn its prerequisites into requirements for every build. Follow the platform
choice rule in creative-direction.md, including for verbatim reuse. WordPress and
WooCommerce require a user choice or an existing WP project.

A source pack need not be runnable code. A video, long prompt document, reference
screenshots, original images and optional finished theme are enough. Register it in
catalog.json reference_packs with a unique id, description, local index path and HTTPS
source links. Put the short index under references/packs; preserve original prompt
documents and assets outside the public repository when redistribution terms are
unclear, using a separate private online backup as well as local files. Use the neutral working-pack structure below. Do not force a WordPress
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


## Neutral working packs and asset hosting

For every current and future pack, use a descriptive neutral ID/title, neutral file
names and approved copies hosted at the user's chosen asset destination. For this
library the current destination is `https://lapis-slate-xvar.here.now/library/`.
Other recipients must choose a destination they control; this is not a shared
upload account. Put the hosted URLs directly into working prompts and manifests.
Include known associated YouTube videos as clearly labelled YouTube references in
each pack’s catalog, working prompt and library page. Preserve those links in
copied/downloaded prompts and private backups, including for future packs. Use
links supplied or verified for that pack; do not invent an association or add a
generic channel link. Do not download/rehost video media merely to add a link.
Omit other optional creator credits, referral URLs, original filenames and private
backup addresses unless requested. Retain functional
provider instructions and legally required copyright/license/third-party notices.
Never remove watermarks or misrepresent authorship, rights or generation provenance.

Maintain full prompt detail in the owner's private working backup when public
redistribution terms are unclear. Public guides must be independently authored
working instructions or texts whose redistribution is authorized. Verbatim reuse
applies to the chosen working prompt; exact original-source reuse needs access to
an authorized copy. Keep necessary adaptations explicit. A self-hosted asset URL
does not establish ownership or erase recognizable branding inside media.

Future intake: inspect rights/notices, select descriptive names, prepare working
prompts, obtain in-chat approval for new/selected media, upload to the designated
host, replace asset URLs, hash-verify downloads, and update private backups and the
public catalog. An explicit request to rehost a specified existing set authorizes
that set; it does not remove future media approval. Keep backup credentials/state
outside public releases. Required license notices are an exception to neutral naming.

Do not promise forensic anonymity: pixels, embedded metadata, license notices and
existing Git history/releases may identify earlier sources. Do not rewrite history
or delete past releases as part of an ordinary catalog update.

For hosted-media packs, set `asset_manifest`, `asset_base_url` and `media_count` in
the catalog. Each manifest entry needs a unique ID/URL, positive byte size, SHA-256
and a URL beneath that base. List every URL in the working prompt. Validation
checks these relationships without downloading media or spending generation budget.
