# Layer coffee product showcase

A detailed prompt and asset reference for a premium coffee storefront, with a
curved ingredient selector surrounding one large drink. Read the original prompt
document for verbatim use; this index is a guide, not a replacement for its detail.

## Platform default

Use this pack with the user's chosen stack or the existing project/host stack.
For a new project without a specified stack, choose a suitable responsive frontend.
WordPress/WooCommerce are optional, only for a user-selected WP build or an existing
WP project. The supplied theme and WP-specific source prompts do not change this
default, even when reproducing the design verbatim. Preserve the design and record
any platform-specific prompt adaptation; see ../creative-direction.md.

## Sources and backup

- [Video](https://www.youtube.com/watch?v=lKQIOiDN2ME)
- [Prompt document](https://docs.google.com/document/d/1h_Bx6WuQOpAi2iuUp0jNxMY7LYsQroNUPqGZ6zjvI7o/edit)
- [Assets, reference and theme](https://drive.google.com/drive/folders/1bVpKNAKOutE6NfxstNA1vKwgwZf28DOY)
- [Independent private snapshot, 22 October 2026](https://github.com/neuronsarealsocool/scroll-site-studio-source-backups/tree/main/layer/2026-10-22)

The snapshot preserves the two original ZIPs and hero PNG, plus DOCX and Markdown
exports of the native Google document. Its manifest records five file sizes and
SHA-256 hashes, verified against a fresh GitHub restore. Access requires private
repository authorization; other skill recipients need their own authorized copy.
No source images, theme code or complete prompts are redistributed in this package.

## Inspected contents

- `assets-20260828T165440Z-1-001.zip`: 14 production images under `assets/`:
  five cups, five ingredients, one background and three editorial photographs.
- `layer-hero-direction (1).png`: the full hero composition reference. This sits
  beside the ZIPs in Drive; it is not inside their `assets/` folders.
- `layer-theme.zip`: WordPress block theme 1.0.5; declares WordPress 6.5+ and
  PHP 7.4+. Includes `layer/drink-selector`, templates, patterns and the same
  14 production images, byte-identical to the asset ZIP.
- Prompt document: hero direction, master-cup and matched-variation prompts,
  ingredient/editorial prompts, geometry locks and an asset-alignment QA workflow.

The cup order is Caramel Cloud, Mocha Cream, Strawberry Cold Foam, Pistachio Oat
Latte and Brown Sugar Latte. Match the source filenames rather than guessing paths.
The source theme README expects `layer-products.csv`, but that file is absent
from the supplied folder and both ZIPs. Create/import actual variable products
and map them before claiming functional purchasing. The README describes disabled
purchasing with fixture prices until valid mappings exist; this was not runtime-tested.

## Choose how to use it

**Verbatim:** use the full source prompts and approved assets. Preserve the warm
cream studio setting, central cup/tray, curved ingredient navigation, typography
roles, product controls and specified transition timing where requested. Resolve
the missing product data and reference-image path before building.

**Adapted:** reuse the method for another product or brand: consistent product
geometry, a clear selected state, supporting ingredient/object cutouts, restrained
navigation and editorial sections. Choose the platform the user wants; WordPress,
WooCommerce and scroll animation are not compulsory.

**Hybrid:** record which composition, copy, assets or behaviours are locked, then
adapt the remaining elements to the user's other references and requirements.

The source labels generation prompts for ChatGPT 5.6. Replicate remains this
skill's default. Preserve creative wording when requested verbatim and explicitly
adapt provider/model parameters; do not silently switch generation services.
Generate a master product first, then matched variants using a shared geometry
lock. Review the contact sheet, overlays, transparency, cup bounds, tray placement
and crop consistency before accepting the set.

## Build and acceptance

Only if WordPress is selected, inspect the theme before installing it, supply WooCommerce product
data and verify variable sizes, displayed prices, cart state, errors and checkout
against the real store. For other stacks, implement equivalent behaviour with
semantic controls and the chosen commerce backend. A visual carousel alone is not
a functioning store.

Compose mobile separately: keep product, label, selection and purchase controls
legible and reachable; test touch/keyboard input, loading/failure states, rapid
selection, reduced motion and layout overflow. Keep pending selection and committed
product data in sync throughout transitions. Test every product and size.

Both ZIPs passed CRC checks; the reference PNG and document exports were inspected.
Downloaded theme code was not executed, and no WordPress/checkout or physical-device
test was performed. No separate redistribution license was found in the inspected
archives or theme header; linked availability does not establish reuse rights.
Preserve provenance and resolve rights for the intended use. Obtain in-chat approval
before any newly selected source or generated media appears on a hosted website,
preview, CDN or public repository. Private backup is separate from media approval.
