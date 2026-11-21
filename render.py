#!/usr/bin/env python3
"""Render the 21 November 2026 world-news image.

One 1024x1024 PNG, "THE WORLD IN ONE DAY" edition for Saturday,
November 21, 2026. Same press-briefing concept as the 20 Nov edition:
a single-row header (date | WORLD BRIEFING | breaking strip), a
full-bleed photo hero, an 4x2 grid of photo cards, and a navy footer.

Deterministic and offline: no clocks, no randomness, no network.
Photos are cover-cropped (the crop band is chosen per photo with fy);
text never overflows its frame -- every text block is asserted.
Run twice and the output bytes are identical.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
FONT_FILE = HERE / "fonts" / "InterVariable.ttf"
OUT = HERE / "entry.png"

# ---- canvas ---------------------------------------------------------------
W, H = 1024, 1024
MARGIN = 24
CONTENT_W = W - 2 * MARGIN

# ---- palette --------------------------------------------------------------
NAVY = (14, 27, 46)
INK = (11, 21, 38)
RED = (217, 43, 43)
RED_DARK = (168, 30, 30)
BLUE = (29, 95, 214)
PURPLE = (104, 74, 186)
TEAL = (14, 124, 123)
GREEN = (34, 139, 74)
STEEL = (47, 111, 179)
ORANGE = (214, 110, 28)
MAGENTA = (196, 30, 90)
IVORY = (250, 247, 241)
WHITE = (255, 255, 255)
HAIR = (231, 226, 214)
GREY = (95, 107, 122)
DECK = (58, 69, 86)
FOOT_TXT = (225, 232, 240)
FOOT_DIM = (150, 168, 190)

# ---- type -----------------------------------------------------------------
def inter(size, weight=500):
    """Inter variable font; the optical-size axis only spans 14-32."""
    font = ImageFont.truetype(str(FONT_FILE), size)
    font.set_variation_by_axes([min(max(size, 14), 32), weight])
    return font


def wrap(d, text, font, max_w):
    """Greedy word wrap; returns a list of lines that all fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if d.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def cover(img, tw, th, fy=0.5):
    """Scale img to cover tw x th, then crop the band around focus fy.

    fy is the vertical centre of the wanted band, as a fraction of the
    scaled image height (0 = top, 1 = bottom). A whisper of blur (0.5 px)
    takes the sensor noise off the photos so the PNG stays under 1 MiB;
    it is invisible at card size and leaves the text untouched.
    """
    scaled = ImageOps.fit(img, (tw, th), method=Image.LANCZOS,
                          centering=(0.5, fy))
    return scaled.filter(ImageFilter.GaussianBlur(0.5))


def chip(d, x, y, text, font, bg, fg=WHITE, pad_x=8, h=20):
    """A small coloured label; returns the width it occupied."""
    w = int(d.textlength(text, font=font)) + 2 * pad_x
    d.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=bg)
    d.text((x + pad_x, y + (h - font.size) / 2 - 1), text, font=font, fill=fg)
    return w


# ---- content --------------------------------------------------------------
DATE_TEXT = "Saturday, November 21, 2026"
BREAKING = "Rutte in Warsaw as Poland seeks NATO cover"
HERO = {
    "chip": "WAR — POLAND",
    "chip_bg": RED,
    "headline": "NATO RALLIES FOR POLAND",
    "deck": ("Rutte flies to Warsaw as Poland seeks more NATO air defences "
             "after Russian missiles fell on its soil. A Swedish pilot was "
             "cleared to shoot — but held fire in bad weather."),
    "photo": "hero_warsaw2.jpg",
    "fy": 0.20,
}

# Grid order: row 1 left-to-right, then row 2.
CARDS = [
    {
        "chip": "CLIMATE", "chip_bg": GREEN, "photo": "antalya.jpg",
        "fy": 0.5,
        "headline": "COP31 TALKS SPILL INTO SATURDAY",
        "deck": "No deal by Friday's deadline; a third draft is due "
                "Saturday. Fossil-fuel phase-out stays cut.",
    },
    {
        "chip": "WASHINGTON", "chip_bg": PURPLE, "photo": "trump.jpg",
        "fy": 0.30,
        "headline": "TRUMP: NO IRAN CALL UNTIL 2027",
        "deck": "Trump says he is 'not rushing' a decision on new strikes. "
                "Netanyahu presses for a 4–7-day campaign.",
    },
    {
        "chip": "THE GULF", "chip_bg": STEEL, "photo": "mq9.jpg",
        "fy": 0.5,
        "headline": "IRAN DOWNS 58TH US DRONE",
        "deck": "The IRGC says it shot down a US MQ-9 over the Strait of "
                "Hormuz. An oil tanker also hit mines near Khasab.",
    },
    {
        "chip": "EUROPE", "chip_bg": ORANGE, "photo": "march.jpg",
        "fy": 0.5,
        "headline": "GEN Z MARCHES IN 25 COUNTRIES",
        "deck": "Tens of thousands fill Europe's squares over living costs "
                "and tuition. Protests continue into Saturday.",
    },
    {
        "chip": "WEATHER", "chip_bg": TEAL, "photo": "akvan.jpg",
        "fy": 0.5,
        "headline": "AKVAN FADES, NO LIVES LOST",
        "deck": "The cyclone weakens to a depression over Odisha; 440,000 "
                "evacuated, no deaths. Record rain: 209 mm.",
    },
    {
        "chip": "HEALTH", "chip_bg": MAGENTA, "photo": "pills.jpg",
        "fy": 0.5,
        "headline": "CANCER PILL: TUMOURS VANISH",
        "deck": "Daraxonrasib plus chemo made tumours undetectable in 1 in "
                "12 patients; 60.7% shrank or vanished.",
    },
    {
        "chip": "CONFLICT", "chip_bg": RED_DARK, "photo": "gaza.jpg",
        "fy": 0.5,
        "headline": "GAZA STRIKES KILL 6 AS TRUCE FRAYS",
        "deck": "Six killed in Friday strikes on central Gaza despite the "
                "October truce; 1,600+ dead since it began.",
    },
    {
        "chip": "JUSTICE", "chip_bg": NAVY, "photo": "palisades.jpg",
        "fy": 0.5,
        "headline": "PALISADES ARSONIST CONVICTED",
        "deck": "Rinderknecht, 30, guilty on two federal arson counts for "
                "the fire that killed 12. Up to 40 years.",
    },
]

SOURCES_LINE = "Sources: Reuters · AP · AFP · CNN · IMD · Al Jazeera"
CREDIT_LINE = ("Photos: Wikimedia Commons (CC / public domain) · NOAA · "
               "White House — see PHOTOS.md")

# ---- geometry -------------------------------------------------------------
HEADER_Y0, HEADER_Y1 = 0, 76
HERO_Y0, HERO_Y1 = 76, 470
GRID_Y0, GRID_Y1 = 482, 968
FOOTER_Y0, FOOTER_Y1 = 968, 1024
CARD_W, CARD_H = 235, 237
PHOTO_H = 135
GAP = 14


def main():
    img = Image.new("RGB", (W, H), IVORY)
    d = ImageDraw.Draw(img, "RGBA")

    # ---- header: date | divider | WORLD BRIEFING | breaking strip --------
    date_font = inter(32, 900)
    date_w = int(d.textlength(DATE_TEXT, font=date_font))
    d.text((MARGIN, 18), DATE_TEXT, font=date_font, fill=NAVY)
    x = MARGIN + date_w + 14
    d.line([(x, 20), (x, 52)], fill=HAIR, width=2)
    x += 16
    wb_font = inter(11, 800)
    wb = "WORLD BRIEFING"
    d.text((x, 30), wb, font=wb_font, fill=NAVY)
    x += int(d.textlength(wb, font=wb_font)) + 16

    strip_font = inter(10.5, 500)
    label_font = inter(11, 800)
    strip_text = f"BREAKING NEWS  ›  {BREAKING}"
    strip_w = int(d.textlength(strip_text, font=strip_font)) + 24
    strip_x = x
    assert strip_x + strip_w <= W - MARGIN, "breaking strip overflows header"
    d.rounded_rectangle([strip_x, 22, strip_x + strip_w, 50],
                        radius=4, fill=RED)
    d.text((strip_x + 12, 30), strip_text, font=strip_font, fill=WHITE)
    d.line([(MARGIN, 68), (W - MARGIN, 68)], fill=NAVY, width=2)

    # ---- hero -------------------------------------------------------------
    hero_img = Image.open(ASSETS / HERO["photo"]).convert("RGB")
    hero = cover(hero_img, W, HERO_Y1 - HERO_Y0, fy=HERO["fy"])
    img.paste(hero, (0, HERO_Y0))

    # Dark gradient over the lower hero so the text reads on any photo.
    overlay = Image.new("RGBA", (W, HERO_Y1 - HERO_Y0), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    top = 124
    for yy in range(top, HERO_Y1 - HERO_Y0):
        alpha = int(225 * (yy - top) / (HERO_Y1 - HERO_Y0 - top))
        od.line([(0, yy), (W, yy)], fill=(0, 0, 0, alpha))
    img.paste(overlay, (0, HERO_Y0), overlay)
    d = ImageDraw.Draw(img, "RGBA")

    chip(d, MARGIN, HERO_Y0 + 234, HERO["chip"], inter(12, 800),
         HERO["chip_bg"], h=24)
    headline_font = inter(46, 800)
    headline_w = int(d.textlength(HERO["headline"], font=headline_font))
    assert headline_w <= CONTENT_W, "hero headline too wide"
    d.text((MARGIN, HERO_Y0 + 266), HERO["headline"], font=headline_font,
           fill=WHITE)
    deck_font = inter(15, 400)
    deck_lines = wrap(d, HERO["deck"], deck_font, CONTENT_W)
    assert len(deck_lines) <= 2, f"hero deck overflows: {deck_lines}"
    for i, line in enumerate(deck_lines):
        d.text((MARGIN, HERO_Y0 + 322 + i * 20), line, font=deck_font,
               fill=WHITE)
    d.rectangle([MARGIN, HERO_Y0 + 374, MARGIN + 64, HERO_Y0 + 377],
                fill=RED)

    # ---- grid: 4 x 2 photo cards -----------------------------------------
    for i, card in enumerate(CARDS):
        col, row = i % 4, i // 4
        cx = MARGIN + col * (CARD_W + GAP)
        cy = GRID_Y0 + row * (CARD_H + GAP)
        photo = Image.open(ASSETS / card["photo"]).convert("RGB")
        img.paste(cover(photo, CARD_W, PHOTO_H, fy=card["fy"]), (cx, cy))

        # Chip sits on the photo, bottom-left.
        chip(d, cx + 8, cy + PHOTO_H - 26, card["chip"], inter(10, 800),
             card["chip_bg"], h=20)
        tx = cx + 8
        tw = CARD_W - 16
        hl_font = inter(16, 800)
        hl_lines = wrap(d, card["headline"], hl_font, tw)
        assert len(hl_lines) <= 2, f"card {i} headline overflows"
        hy = cy + PHOTO_H + 8
        for j, line in enumerate(hl_lines):
            d.text((tx, hy + j * 20), line, font=hl_font, fill=INK)
        deck_font = inter(11, 400)
        deck_lines = wrap(d, card["deck"], deck_font, tw)
        assert len(deck_lines) <= 3, f"card {i} deck overflows"
        dy = hy + len(hl_lines) * 20 + 4
        for j, line in enumerate(deck_lines):
            d.text((tx, dy + j * 15), line, font=deck_font, fill=DECK)
        assert dy + len(deck_lines) * 15 <= cy + CARD_H, \
            f"card {i} text past card bottom"

    # ---- footer -----------------------------------------------------------
    d.rectangle([0, FOOTER_Y0, W, FOOTER_Y1], fill=NAVY)
    d.ellipse([26, 984, 52, 1010], outline=FOOT_TXT, width=2)
    d.line([(26, 997), (52, 997)], fill=FOOT_TXT, width=1)
    d.ellipse([(26 + 52) / 2 - 2, 995, (26 + 52) / 2 + 2, 999],
              fill=FOOT_TXT)
    d.text((62, 989), DATE_TEXT, font=inter(13, 800), fill=FOOT_TXT)
    src_x = 62 + int(d.textlength(DATE_TEXT, font=inter(13, 800))) + 12
    d.line([(src_x, 990), (src_x, 1004)], fill=FOOT_DIM, width=1)
    d.text((src_x + 10, 990), SOURCES_LINE, font=inter(12, 500),
           fill=FOOT_TXT)
    d.text((62, 1005), CREDIT_LINE, font=inter(9, 400), fill=FOOT_DIM)
    for k in range(3):
        x0 = 932 + k * 18
        d.polygon([(x0, 1012), (x0 + 10, 1012), (x0 + 2, 980),
                   (x0 - 8, 980)], fill=RED)

    img.save(OUT, format="PNG", compress_level=9, optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
