# Horizon Estates: headline placement reference

User-selected screenshot supplied on 24 October 2026, original size 2560 x 1440.
This refines the headline spacing in the [video audit](horizon-estates-video-audit.md).
For close reuse, this still takes precedence for the headline's spatial relationship
to the house. It does not replace the audit's separate motion and section rules.

## Locked desktop composition

- Set “Live beyond” on the left and “the expected.” on the right, sharing one
  baseline across the upper/middle floors of the house. Keep the heading prominent
  in proportion to the house. Cap its growth when the house reaches its maximum
  size; do not stretch the type across an ultrawide viewport independently.
- Place the end of “beyond” near the left upper facade and the start of
  “the expected.” near the right facade, with a visible safety gap on both sides.
  The house should connect the phrases compositionally without touching their
  letterforms. Readability takes precedence over the earlier “tight” wording.
- Anchor these inner text edges to the visible architecture at headline height,
  not the full transparent image rectangle or the wider mountain base. Generic
  equal-width columns or `space-between` alone do not establish this relationship.
- Show every letter of both phrases completely in the opening state. No house,
  balcony, foliage or mountain edge may clip the ending of “beyond”, the beginning
  of “the expected.”, or the outside edges of either phrase. Judge clearance over
  the entire glyph height, not just one facade edge at the baseline. Keep motion
  behind the subject later in the scroll separate from this readable arrival state.
- Tune house position/scale and type size/spacing together. Preserve the close
  foreground residence, its clear silhouette and the low-left paragraph/actions.
  Do not move the house away from camera to create room for unrelated text columns.

## Ultrawide correction, 24 October 2026

The user supplied a 3440 x 1271 screenshot showing the deployed regression. It is
a failure example, not another target composition. The prior implementation let
viewport-based type keep growing after the residence hit its size cap, and a
viewport-relative headline height drifted down onto the wider mountain.

Tie headline height and maximum size to the rendered house plane. Leave breathing
room beyond its complete silhouette across the text band, including balconies and
trees. A typical desktop screenshot alone is insufficient proof of this layout.

## Responsive and scroll checks

1. Compare the website viewport only. Exclude the recording's browser chrome,
   blue desktop border and presenter inset when judging spacing and alignment.
   The still does not establish exact CSS pixels or browser zoom.
2. Capture the opening at 1280 x 720, 1440 x 900, 1920 x 1080 and the reported
   3440 x 1271 size. Also check a shallow ultrawide viewport. Both phrases must
   have complete letterforms, a visible gap from the silhouette and safe outer
   gutters. Verify actual occlusion, not just horizontal overflow or text boxes.
3. Check an intermediate scroll state and the hero exit in both directions.
   Preserve the audit's passing-behind/parallax effect while avoiding sustained
   loss of whole words. Do not use one frozen screenshot to infer animation timing.
4. On narrow screens, use a deliberate readable stacked/reflowed heading close
   to the house. Do not force the desktop split into overflow or obscure words.
   Reduced-motion and no-JavaScript states must retain a readable composition.

## Source retention

The original screenshot and its size/SHA-256 manifest are preserved unchanged in
the [private headline-reference snapshot](https://github.com/neuronsarealsocool/scroll-site-studio-source-backups/tree/main/horizon-estates/2026-10-24-headline-reference).
Access requires repository authorization. The public skill contains these authored
placement rules, not the uploaded screenshot; redistribution is not approved.

The [private ultrawide failure snapshot](https://github.com/neuronsarealsocool/scroll-site-studio-source-backups/tree/main/horizon-estates/2026-10-24-ultrawide-correction)
preserves the user-reported regression and its checksum manifest. It is evidence
for the correction, not an asset for public redistribution.
