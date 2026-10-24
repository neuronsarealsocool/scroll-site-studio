# Horizon Estates: headline placement reference

User-selected screenshot supplied on 24 October 2026, original size 2560 x 1440.
This refines the headline spacing in the [video audit](horizon-estates-video-audit.md).
For close reuse, this still takes precedence for the headline's spatial relationship
to the house. It does not replace the audit's separate motion and section rules.

## Locked desktop composition

- Set “Live beyond” on the left and “the expected.” on the right, sharing one
  baseline across the upper/middle floors of the house. Keep the heading large
  enough to span most of the scene width, as in the selected still.
- Bring the end of “beyond” tight to the left edge of the visible upper facade.
  Bring the start of “the expected.” tight to the right facade. The house fills
  the opening between the phrases; do not leave wide empty gutters beside it.
- Anchor these inner text edges to the visible architecture at headline height,
  not the full transparent image rectangle or the wider mountain base. Generic
  equal-width columns or `space-between` alone do not establish this relationship.
- Keep both phrases readable in the opening state. Near-touching or shallow
  letter overlap can convey depth, but do not hide “the” or swallow the ending of
  “beyond” behind the house. The screenshot is a proximity reference, not a reason
  to increase occlusion until words disappear.
- Tune house position/scale and type size/spacing together. Preserve the close
  foreground residence, its clear silhouette and the low-left paragraph/actions.
  Do not move the house away from camera to create room for unrelated text columns.

## Responsive and scroll checks

1. Compare the website viewport only. Exclude the recording's browser chrome,
   blue desktop border and presenter inset when judging spacing and alignment.
   The still does not establish exact CSS pixels or browser zoom.
2. At each desktop width, capture the opening state and confirm that both inner
   phrase edges sit beside the upper facade, both phrases are readable, and the
   text and residence still read as one composition.
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
