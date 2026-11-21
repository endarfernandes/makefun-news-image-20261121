# VERIFICATION — news-image-20261121

Built and verified 21 Nov 2026 (evening WIB). Build only — no kit
check, bundle, commit, push or submit has been run.

## Render

- `render.py` runs clean; all text asserts pass (header fits,
  hero headline ≤ content width, hero deck ≤ 2 lines, every card
  headline ≤ 2 lines, every card deck ≤ 3 lines, no text past any
  card bottom or past y = 1024).
- `entry.png`: PNG, 1024 × 1024, RGB, **977,352 bytes** — under the
  1,048,576-byte (1 MiB) limit with 71,224 bytes to spare.
- SHA-256: `a4285eeeb3f98ac097334adf29bc577f3aff6e9fdd80be34b997e8e125ade7d8`
- **Determinism:** rendered twice; both runs produced the identical
  SHA-256 (`a4285eeeb3f98ac097334adf29bc577f3aff6e9fdd80be34b997e8e125ade7d8`).
- First render (before the photo blur) was 1,074,605 bytes — over
  the limit. A 0.5 px Gaussian blur on photos only brought it to
  977,352 bytes; text is untouched and the blur is invisible at
  card size.

## Entrypoint

- `main.py` is stdlib only. Tested with
  `MAKEFUN_OUTPUT_DIR=/tmp/mf-out python3 main.py` — it copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` correctly.

## Visual check (full size, 600 px, 300 px)

- **Hero:** Warsaw night skyline across the Vistula; no date
  stamp, no watermark. Skyline visible in the upper half, dark
  river/trees at the bottom under the text. Headline "NATO
  RALLIES FOR POLAND" and the two-line deck are white on the
  gradient and read clearly. Red chip, accent line all in place.
- **Header:** date, WORLD BRIEFING and the breaking strip all fit
  on one row; nothing clipped.
- **Grid:** all 8 cards read cleanly. Trump card re-checked after
  the fy change (0.45 → 0.30): the full head is now in frame.
  MQ-9 drone, Madrid march crowd, Akvan satellite swirl, pills,
  Gaza rubble and the Palisades aerial are all recognisable.
  Chips sit on their photos, bottom-left, no overlap with text.
- **Footer:** date, sources line and photo-credit line legible;
  red slashes at the right.
- **600 px:** everything legible — headlines, decks, chips,
  footer.
- **300 px:** layout reads clearly; hero headline, date and card
  headlines are discernible (decks are small at this size, as in
  the 20261120 edition).

## Known limitations (honest)

- The Gaza photo is damage from October 2023, not the 21 Nov
  strikes; the Gen Z march photo is a 2019 Madrid climate march,
  not the 21 Nov protests. Both are labelled SUBJECT in
  PHOTOS.md and are not presented as the day's events.
- The COP31 card photo is Antalya's coast road (the host city),
  not the summit itself — labelled LOCATION.
- Two stories (Trump quote Thursday, Gaza strikes Friday) are
  20 Nov events carried on 21 Nov news pages; the date anchors
  are recorded in STORIES.md and the decks make no false date
  claim.

## Files

- `render.py` — renderer (Pillow + bundled Inter, offline,
  deterministic)
- `main.py` — entrypoint (stdlib only)
- `entry.png` — the image (977,352 bytes, SHA-256 above)
- `STORIES.md`, `PHOTOS.md`, `DESIGN.md`, `VERIFICATION.md`
  (this file), `README.md`
- `assets/` — 9 photos (see PHOTOS.md for licences/SHAs)
- `fonts/InterVariable.ttf` — bundled Inter (OFL)
- `LICENSE` — MIT (from the kit starter)
- `news-image-20261121-kit/` — fresh kit downloaded 21 Nov 2026
  ~19:17 WIB; bundle SHA-256
  `35b3239e3a19cc1d41b80cba8e3f8e629534e23997d93ec2df2750ff3f1d24f4`
  (kit level is only reported by the CLI at check/submit time —
  not recorded here; do not invent it)

## Not done (needs separate user approval each)

Kit check, transcript bundle, commit, push, submit.
