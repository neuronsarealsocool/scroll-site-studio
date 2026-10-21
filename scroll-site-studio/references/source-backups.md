# Independent online source backups

Default to an independent online copy of the files in a source pack; original
Drive/document links and local-only downloads are not a complete backup. Use the
user's authorized durable destination, reusing a designated backup location across
packs. A private repository or private cloud folder is the default when asset
publication/redistribution has not been approved. Do not publish pending media to
make a backup public. If no authorized destination is available, retain local copies
and report that online backup is incomplete rather than claiming protection.

## Snapshot and verify

1. Download the actual prompt documents and asset/code archives. Preserve original
   bytes and filenames; label exported conversions as exports rather than originals.
2. Inspect filenames, sizes and relevant source notices without executing downloaded
   code. Exclude credentials/account state. Preserve source URLs and provenance.
3. Upload to the independent destination under a dated/versioned pack path. Keep an
   immutable prior snapshot when sources change. Do not overwrite another pack or
   create a new repository for every file.
4. Store a manifest with source URLs, snapshot date, file sizes and SHA-256 hashes.
   Never store API tokens, signed upload URLs or private machine paths in that manifest.
5. Download/restore the uploaded files and compare sizes/hashes. Only then record
   a verified backup in the catalog. An upload attempt or an HTTP-200 HTML login
   page is not proof the files were backed up.
6. Record the destination and access requirements. A private backup is available
   only to authorized users, not every public skill recipient. Each recipient
   needs their own authorized backup or an approved share. If primary links fail,
   use an accessible verified backup without silently granting broader access.

## Media approval remains separate

A user's request to back up files authorizes private storage at their selected or
contextually authorized destination. It does not approve those media for a public
website, staging site, CDN or public repository. Keep the mandatory in-chat approval
gate for newly selected or changed site media. Do not bundle private backup files
into the public skill release or override source licenses. For unapproved material,
the public catalog can carry links, provenance and access notes rather than copies.

Prefer a durable, authenticated destination over temporary provider-output URLs or
anonymous expiring hosting. State the actual persistence/access limits and avoid
promising that any external service will be available forever.
