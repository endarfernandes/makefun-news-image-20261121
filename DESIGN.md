# DESIGN — news-image-20261121 ("THE WORLD IN ONE DAY")

Same concept as the 20261120 R3 edition: a press-briefing broadsheet
for one day's world news. One image, nine stories, no stats strip,
no per-story source lines on the cards — sources live in the footer
and in STORIES.md.

## Layout (1024 × 1024)

| Zone | y range | Content |
|------|---------|---------|
| Header | 0–76 | One row: big navy date (32 px Black) \| hairline divider \| WORLD BRIEFING (11 px ExtraBold) \| red BREAKING NEWS strip. Navy rule at y = 68. |
| Hero | 76–470 | Full-bleed Warsaw night photo (1024 × 394), dark gradient over the lower half, red chip at y ≈ 310, headline 46 px ExtraBold at y ≈ 342, deck 15 px (max 2 lines) at y ≈ 398, 64 px red accent line at y ≈ 450. |
| Grid | 482–968 | 4 × 2 cards, each 235 × 237, 14 px gutters. Photo 235 × 135, cover-cropped; coloured chip overlaid bottom-left ON the photo; headline 16 px ExtraBold (max 2 lines); deck 11 px (max 3 lines). |
| Footer | 968–1024 | Navy bar: globe icon, date 13 px ExtraBold, sources line 12 px, photo-credit line 9 px, three red diagonal slashes at the right. |

Margin 24 px; content width 976 px. Background IVORY
(250, 247, 241).

## Palette

NAVY (14, 27, 46) — header text, footer, JUSTICE chip. INK
(11, 21, 38) — card headlines. RED (217, 43, 43) — WAR chip,
breaking strip, accent line, footer slashes. RED_DARK (168, 30, 30)
— CONFLICT chip. BLUE (29, 95, 214) and PURPLE (104, 74, 186) —
WASHINGTON chip. TEAL (14, 124, 123) — WEATHER chip. GREEN
(34, 139, 74) — CLIMATE chip. STEEL (47, 111, 179) — THE GULF
chip. ORANGE (214, 110, 28) — EUROPE chip. MAGENTA (196, 30, 90)
— HEALTH chip. HAIR (231, 226, 214) — header divider. GREY
(95, 107, 122). DECK (58, 69, 86) — card decks. FOOT_TXT
(225, 232, 240), FOOT_DIM (150, 168, 190).

## Type

Bundled Inter variable font (`fonts/InterVariable.ttf`, OFL).
`inter(size, weight)` sets the optical-size axis (clamped 14–32)
and the weight axis. Headlines are ExtraBold (800), the date is
Black (900), decks are Regular (400).

## Photo treatment

Photos are cover-cropped to their frame with `ImageOps.fit`
(centre-x, vertical focus `fy` per photo). A 0.5 px Gaussian blur
is applied to photos only — never to text — to take sensor noise
off so the PNG stays under 1 MiB; it is invisible at card size.
The hero gradient runs from y = hero_y0 + 124 to the hero bottom,
black alpha up to 225/255, so white text reads on any photo.

Crop choices: hero `fy = 0.20` keeps the Warsaw skyline band in
frame and the river/trees dark at the bottom for the text. Trump
`fy = 0.30` keeps the whole head in the 235 × 135 card (the
20261120 edition used 0.45 and cut the top of the hair). All
other cards use `fy = 0.5` (centre).

## Determinism

No clocks, no randomness, no network. `render.py` writes
`entry.png` with `compress_level=9, optimize=True`. Two runs
produce byte-identical output (verified — same SHA-256).

## What changed vs 20261120 R3

- New date, new 9 stories, new hero (Warsaw night skyline).
- New chips: THE GULF (steel), EUROPE (orange), HEALTH
  (magenta), CONFLICT (dark red); JUSTICE moved to navy.
- Photos: 6 new downloads, 3 reused (trump, akvan, antalya).
- Photo blur (0.5 px) added — the first render ran 26 KB over
  the 1 MiB limit without it.
- Trump crop focus moved 0.45 → 0.30 so the head is not cut.
- Everything else — geometry, palette, type scale, footer,
  breaking-strip treatment — is identical to R3.
