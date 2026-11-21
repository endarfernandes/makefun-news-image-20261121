# THE WORLD IN ONE DAY — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/endarfernandes/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/endarfernandes/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for the make.fun bounty
[**news-image-20261121 — "Sum up 21 November's world news in one
image"**](https://make.fun/bounty/news-image-20261121).

One 1024 × 1024 image, nine stories: NATO rallies for Poland as
Rutte flies to Warsaw, COP31 spills into overtime, Trump holds off
any Iran decision until 2027, Iran downs a 58th US drone, Gen Z
marches across 25 European countries, Cyclone Akvan fades with no
lives lost, a cancer pill makes tumours vanish, Gaza strikes kill
six as the truce frays, and the Palisades arsonist is convicted.

## How it works

`render.py` (Pillow + the bundled Inter font) draws the image
offline and deterministically — no network, no randomness, no
clocks. `main.py` (stdlib only) copies the pre-rendered
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.

```sh
python3 render.py   # writes entry.png (1024x1024, < 1 MiB)
```

## Files

- `entry.png` — the image
- `render.py`, `main.py` — renderer and entrypoint
- `STORIES.md` — the 9 stories, sources, and the stories dropped
- `PHOTOS.md` — photo credits, licences and SHA-256s
- `DESIGN.md` — layout, palette, type
- `VERIFICATION.md` — build and visual verification
- `assets/` — 9 freely licensed photos (Wikimedia Commons CC /
  public domain, NOAA, White House)

## Try make.fun

Sign up with my referral link and we both get a bonus:
[https://make.fun/r/zpp83a0k](https://make.fun/r/zpp83a0k)
(referral code `zpp83a0k`).

## Licence

MIT — see `LICENSE`.
