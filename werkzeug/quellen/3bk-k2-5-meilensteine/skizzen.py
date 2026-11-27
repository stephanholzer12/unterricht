"""Bilder für PBGW 3BK · Meilensteine – alles selbst gezeichnet (keine Buchabbildungen, keine Fotos von Fundstücken).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3bk-k2-5-meilensteine/skizzen.py  →  3bk-pbgw/k2-5-meilensteine/img/*.png"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
IMG = UNIT + "img/"
os.makedirs(IMG, exist_ok=True)
FR = "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"
FB = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
BG, WHITE, INK, RED, GREY = (242, 243, 238), (255, 255, 255), (59, 74, 47), (163, 58, 43), (122, 132, 145)
OLIVE, GREEN, ORANGE, TEAL, MUTED = (59, 74, 47), (127, 168, 58), (217, 119, 43), (46, 125, 140), (94, 102, 82)
LIGHT, PALE = (223, 229, 208), (238, 243, 228)
S = 2
f = lambda p, s: ImageFont.truetype(p, int(s * S))


def canvas(w=900, h=600, bg=BG):
    im = Image.new("RGB", (w * S, h * S), bg); return im, ImageDraw.Draw(im)


def P(*xy):
    return [v * S for v in xy]


def ctext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w / 2, y * S), t, font=font, fill=fill)


def fit(d, t, path, size, maxw):
    while size > 12 and d.textlength(t, font=f(path, size)) / S > maxw: size -= 1
    return f(path, size)


def ltext(d, x, y, t, font, fill):
    d.text((x * S, y * S), t, font=font, fill=fill)


def save(im, path, q=128):
    im.resize((im.width // S, im.height // S), Image.LANCZOS).quantize(colors=q).save(path, optimize=True)


def arrow(d, x0, y0, x1, y1, col=INK, w=5, head=16):
    d.line(P(x0, y0, x1, y1), fill=col, width=int(w * S))
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1, y1), (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45)), (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))]
    d.polygon([(px * S, py * S) for px, py in pts], fill=col)


def dashed_arrow(d, pts, col, w=4, dash=12):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        L = math.hypot(x1 - x0, y1 - y0); n = max(1, int(L / dash))
        for k in range(0, n, 2):
            a, b = k / n, min(1, (k + 1) / n)
            d.line(P(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a, x0 + (x1 - x0) * b, y0 + (y1 - y0) * b), fill=col, width=int(w * S))
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    arrow(d, x1 - (x1 - x0) * 0.001, y1 - (y1 - y0) * 0.001, x1, y1, col, w, 16)


def label_box(d, x, y, w, h, title, lines, col):
    d.rounded_rectangle(P(x, y, x + w, y + h), radius=14 * S, fill=WHITE, outline=col, width=3 * S)
    d.rounded_rectangle(P(x, y, x + w, y + 40), radius=14 * S, fill=col)
    d.rectangle(P(x, y + 26, x + w, y + 40), fill=col)
    ctext(d, x + w / 2, y + 7, title, f(FB, 22), WHITE)
    for k, t in enumerate(lines):
        ctext(d, x + w / 2, y + 50 + k * 26, t, f(FR, 20), INK)



BROWN, SOIL, SKY, YELLOW, BLUE = (120, 86, 52), (176, 138, 96), (232, 241, 243), (222, 182, 62), (46, 125, 140)


COPPER, WOOD, SAND, SEA = (184, 115, 51), (120, 86, 52), (240, 232, 210), (200, 224, 236)
RIVER = (46, 125, 140)


def fitbox(d, x, y, w, h, title, lines, col, tsize=22, lsize=20, head=40):
    d.rounded_rectangle(P(x, y, x + w, y + h), radius=14 * S, fill=WHITE, outline=col, width=3 * S)
    d.rounded_rectangle(P(x, y, x + w, y + head), radius=14 * S, fill=col)
    d.rectangle(P(x, y + head - 14, x + w, y + head), fill=col)
    ctext(d, x + w / 2, y + 7, title, fit(d, title, FB, tsize, w - 16), WHITE)
    for k, t in enumerate(lines):
        ctext(d, x + w / 2, y + head + 10 + k * (lsize + 7), t, fit(d, t, FR, lsize, w - 16), INK)


def pill(d, x, y, text, col, size=20):
    fo = f(FB, size); w = d.textlength(text, font=fo) / S + 22
    d.rounded_rectangle(P(x, y, x + w, y + size + 14), radius=(size + 14) // 2 * S, fill=col)
    ctext(d, x + w / 2, y + 6, text, fo, WHITE)
    return w


# ------------------------------------------------------------ Ötzis Beil (Schema)
def beil():
    im, d = canvas(900, 540, PALE)
    # Schaft (Holz) und Klinge (Kupfer) – vereinfacht, kein Foto des Fundes
    d.line(P(110, 480, 290, 120), fill=WOOD, width=30 * S)
    d.polygon(P(285, 95, 400, 60, 425, 195, 305, 175), fill=COPPER, outline=(120, 70, 30))
    d.polygon(P(300, 100, 380, 76, 392, 120, 310, 135), fill=(214, 150, 84))
    for yy in (172, 190, 208):  # Riemen
        x0 = 290 - (yy - 120) * 0.5
        d.line(P(x0 - 22, yy + 4, x0 + 22, yy - 6), fill=(70, 50, 30), width=7 * S)
    for txt, tx, ty, sx, sy, ax, ay in (("Klinge aus Kupfer", 30, 40, 240, 62, 330, 100), ("Riemen", 30, 215, 125, 228, 255, 190), ("Schaft aus Holz", 235, 405, 228, 418, 175, 400)):
        ltext(d, tx, ty, txt, f(FB, 26), INK); arrow(d, sx, sy, ax, ay, MUTED, 3, 12)
    fitbox(d, 500, 30, 370, 130, "Was sehen wir?", ["Klinge aus Kupfer im Schaft", "Material und Form sind sichtbar"], OLIVE)
    fitbox(d, 500, 195, 370, 130, "Was vermuten wir?", ["Rohstoff, Brennstoff und Können", "waren nötig – Austausch möglich"], TEAL)
    fitbox(d, 500, 360, 370, 130, "Was wissen wir nicht?", ["Beruf, Rang, Reise Ötzis –", "das belegt das Beil allein nicht"], RED)
    save(im, IMG + "beil.png")


# ------------------------------------------------------------ Verwaltungskette
def kette():
    im, d = canvas(900, 400, BG)
    xs = (10, 240, 470, 700)
    data = [("Ernte, Abgaben", ["ein Teil der Ernte", "wird abgeliefert"], OLIVE), ("Lager", ["Getreide, Vieh,", "Krüge, Ziegel"], TEAL),
            ("Liste", ["Zeichen für Waren", "und für Zahlen"], ORANGE), ("Verteilung", ["an Arbeiter,", "Tempel, Beamte"], GREEN)]
    for x, (t, ls, c) in zip(xs, data): fitbox(d, x, 40, 190, 125, t, ls, c, 24, 21)
    for x in xs[:-1]: arrow(d, x + 194, 100, x + 232, 100, INK, 5, 16)
    arrow(d, 565, 300, 565, 172, RED, 5, 16)
    d.rounded_rectangle(P(310, 305, 820, 375), radius=14 * S, fill=WHITE, outline=RED, width=3 * S)
    ctext(d, 565, 322, "Wer die Liste führt und kontrolliert, hat Einfluss.", fit(d, "Wer die Liste führt und kontrolliert, hat Einfluss.", FB, 24, 480), RED)
    save(im, IMG + "kette.png")


# ------------------------------------------------------------ Karte (Schema)
def karte():
    W, H = 900, 640
    im, d = canvas(W, H, SAND)
    X = lambda lon: 20 + (lon - 28) / 24 * 860
    Y = lambda lat: 30 + (39.5 - lat) / 17.5 * 560
    pt = lambda lat, lon: (X(lon), Y(lat))
    poly = lambda pts, col: d.polygon([c * S for p in [pt(*q) for q in pts] for c in p], fill=col)
    # Mittelmeer, Persischer Golf, Rotes Meer (stark vereinfacht)
    poly([(36.4, 28), (36.2, 30.5), (36.3, 33), (36.6, 34.6), (36.8, 35.9), (36.0, 35.8), (34.5, 35.9), (33.2, 35.4), (31.7, 34.5), (31.1, 32.2), (31.4, 30.0), (30.9, 28)], SEA)
    poly([(30.3, 47.7), (29.7, 49.5), (28.0, 51.0), (26.0, 52.0), (24.0, 52.0), (24.0, 51.0), (26.5, 49.8), (28.7, 48.3)], SEA)
    poly([(29.9, 32.5), (28.2, 33.7), (25.5, 35.2), (22.0, 37.2), (22.0, 38.4), (25.0, 36.8), (28.3, 34.9), (30.0, 34.0)], SEA)
    line = lambda pts, w: d.line([c * S for p in [pt(*q) for q in pts] for c in p], fill=RIVER, width=int(w * S), joint="curve")
    line([(22.4, 31.7), (24.1, 32.9), (25.7, 32.6), (27.2, 31.2), (29.0, 31.2), (30.0, 31.2), (31.0, 31.1)], 9)
    line([(31.0, 31.1), (31.5, 30.4)], 6); line([(31.0, 31.1), (31.4, 31.8)], 6); line([(31.0, 31.1), (31.5, 31.1)], 6)
    line([(39.0, 38.8), (37.3, 38.0), (36.0, 38.4), (35.3, 40.1), (34.4, 41.0), (33.4, 43.3), (32.5, 44.4), (31.1, 45.4), (30.7, 46.5), (30.5, 47.8)], 9)   # Unterlauf nach Süden gezogen, damit Euphrat und Tigris klar getrennt bleiben
    line([(38.0, 40.5), (37.0, 42.0), (36.3, 43.1), (35.5, 43.5), (34.0, 43.8), (33.3, 44.4), (32.5, 45.8), (31.5, 47.2), (31.0, 47.5)], 9)
    for name, lat, lon, dx, dy, col in (("Memphis", 29.85, 31.25, 14, -12, OLIVE), ("Theben", 25.7, 32.6, 14, -12, OLIVE), ("Babylon", 32.5, 44.4, -118, -34, ORANGE),
                                        ("Uruk", 31.1, 45.4, -66, 16, ORANGE), ("Ur", 30.7, 46.5, 12, 16, ORANGE)):
        x, y = pt(lat, lon); d.ellipse(P(x - 8, y - 8, x + 8, y + 8), fill=col, outline=WHITE, width=2 * S)
        ltext(d, x + dx, y + dy, name, f(FB, 22), INK)
    for txt, lat, lon, col in (("Nil", 27.6, 31.6, RIVER), ("Euphrat", 34.6, 37.2, RIVER), ("Tigris", 36.0, 43.9, RIVER)):
        x, y = pt(lat, lon); ltext(d, x + 10, y, txt, f(FB, 24), col)
    ltext(d, X(28.2), Y(28.3), "ÄGYPTEN", f(FB, 25), (150, 120, 60)); ltext(d, X(39.6), Y(29.2), "MESOPOTAMIEN", f(FB, 30), (150, 120, 60))
    ltext(d, X(28.6), Y(34.6), "Mittelmeer", f(FR, 24), RIVER); ltext(d, X(34.0), Y(25.6), "Rotes Meer", f(FR, 21), RIVER); ltext(d, X(48.9), Y(25.2), "Persischer", f(FR, 22), RIVER); ltext(d, X(49.4), Y(24.3), "Golf", f(FR, 22), RIVER)
    d.rounded_rectangle(P(20, 596, 420, 632), radius=10 * S, fill=WHITE, outline=MUTED, width=2 * S)
    ltext(d, 32, 602, "Schema, nicht maßstabsgerecht", f(FB, 22), RED)
    save(im, IMG + "karte.png")


# ------------------------------------------------------------ Athen
def athen():
    im, d = canvas(900, 620, BG)
    fitbox(d, 20, 25, 270, 120, "Rat der 500", ["bereitet Beratungen vor", "Besetzung: Los"], TEAL, 24, 21)
    fitbox(d, 315, 25, 270, 120, "Archonten", ["hohe Beamte", "Besetzung: Los"], TEAL, 24, 21)
    fitbox(d, 610, 25, 270, 120, "Strategen", ["Heerführer", "Besetzung: Wahl"], ORANGE, 24, 21)
    arrow(d, 155, 150, 255, 238, TEAL, 5, 16)
    d.rounded_rectangle(P(180, 240, 720, 385), radius=18 * S, fill=OLIVE)
    ctext(d, 450, 258, "Volksversammlung", f(FB, 34), WHITE)
    ctext(d, 450, 305, "erwachsene männliche Bürger", f(FR, 25), WHITE)
    ctext(d, 450, 338, "entscheiden unmittelbar selbst", f(FR, 25), WHITE)
    d.rounded_rectangle(P(80, 440, 820, 590), radius=16 * S, fill=WHITE, outline=RED, width=4 * S)
    ctext(d, 450, 455, "Ohne politische Mitbestimmung", f(FB, 28), RED)
    for x, t in ((220, "Frauen"), (450, "Versklavte"), (680, "Metöken")):
        d.rounded_rectangle(P(x - 90, 505, x + 90, 560), radius=12 * S, fill=(246, 227, 223), outline=RED, width=2 * S); ctext(d, x, 516, t, f(FB, 28), RED)
    save(im, IMG + "athen.png")


# ------------------------------------------------------------ Rom
def rom():
    im, d = canvas(900, 720, BG)
    d.rounded_rectangle(P(10, 10, 890, 335), radius=16 * S, fill=PALE, outline=OLIVE, width=3 * S)
    ctext(d, 450, 20, "Republik: Macht auf mehrere Einrichtungen verteilt", f(FB, 28), OLIVE)
    xs = (25, 245, 465, 685)
    for x, (t, ls, c) in zip(xs, [("Konsuln", ["zwei an der Spitze,", "Amtszeit begrenzt"], TEAL), ("Senat", ["einflussreiche", "Familien"], OLIVE),
                                   ("Volksversammlungen", ["wählen Amtsträger,", "wirken mit"], GREEN), ("Volkstribunen", ["Einspruchsrecht", "für die Plebejer"], ORANGE)]):
        fitbox(d, x, 80, 190, 130, t, ls, c, 22, 21)
    ctext(d, 450, 245, "Oberschicht mit großem Einfluss · Frauen und Versklavte ausgeschlossen", fit(d, "Oberschicht mit großem Einfluss · Frauen und Versklavte ausgeschlossen", FB, 22, 840), RED)
    arrow(d, 450, 342, 450, 392, INK, 6, 20)
    d.rounded_rectangle(P(10, 395, 890, 710), radius=16 * S, fill=(246, 227, 223), outline=RED, width=3 * S)
    ctext(d, 450, 405, "Prinzipat: die Einrichtungen bleiben – die Macht liegt beim Princeps", fit(d, "Prinzipat: die Einrichtungen bleiben – die Macht liegt beim Princeps", FB, 28, 860), RED)
    d.rounded_rectangle(P(215, 455, 685, 565), radius=16 * S, fill=RED)
    ctext(d, 450, 465, "Princeps (Augustus)", f(FB, 32), WHITE)
    ctext(d, 450, 508, "Heer · Provinzen · Befugnisse von", f(FR, 24), WHITE); ctext(d, 450, 535, "Konsul und Volkstribun", f(FR, 24), WHITE)
    d.rounded_rectangle(P(50, 595, 850, 690), radius=14 * S, fill=WHITE, outline=MUTED, width=3 * S)
    ctext(d, 450, 608, "Konsuln · Senat · Volksversammlungen · Volkstribunen", f(FB, 24), MUTED)
    ctext(d, 450, 648, "bestehen weiter, kontrollieren ihn aber kaum", f(FR, 24), MUTED)
    arrow(d, 450, 590, 450, 570, RED, 5, 16)
    save(im, IMG + "rom.png")


# ------------------------------------------------------------ Zeittafel (Aufgabe 8)
def zeitstrahl(mit_loesung=False, dateiname="zeitstrahl.png"):
    """Raster der Zeitbereiche. Ohne Lösung für die öffentliche Theorie-Seite (Aufgabe 8 soll nicht abschreibbar sein,
    Prüfbericht 27.11.2026), mit Lösung nur für die Lehrerzentrale und die Sicherungsfolie."""
    W, H = 900, 640
    im, d = canvas(W, H, BG)
    bins = ["10 000–\n8000 v. Chr.", "4000–\n3000 v. Chr.", "2000–\n1500 v. Chr.", "600–\n400 v. Chr.", "100 v. Chr.–\n100 n. Chr.", "400–\n500 n. Chr."]
    x0, cw, y0, hh, rh = 150, 125, 20, 80, 150
    if mit_loesung:   # hervorgehobene Spalte wäre im leeren Raster ein Hinweis auf die Lösung
        d.rounded_rectangle(P(x0 + cw, y0, x0 + 2 * cw, y0 + hh + 3 * rh), radius=0, fill=(255, 241, 214))
    for k, b in enumerate(bins):
        x = x0 + k * cw
        d.rectangle(P(x + 3, y0, x + cw - 3, y0 + hh - 6), fill=OLIVE)
        for j, ln in enumerate(b.split("\n")): ctext(d, x + cw / 2, y0 + 12 + j * 26, ln, f(FB, 20), WHITE)
    rows = ["Vorderer Orient", "Alpenraum", "Mittelmeer- raum"]
    for r, name in enumerate(rows):
        y = y0 + hh + r * rh
        d.rectangle(P(10, y + 4, x0 - 6, y + rh - 4), fill=TEAL); ctext(d, 77, y + rh / 2 - 22, name.split()[0], fit(d, name.split()[0], FB, 22, 125), WHITE)
        if len(name.split()) > 1: ctext(d, 77, y + rh / 2 + 6, name.split()[1], fit(d, name.split()[1], FB, 22, 125), WHITE)
        d.line(P(10, y + rh, W - 10, y + rh), fill=LIGHT, width=2 * S)
    ev = [(0, 0, "1", "Landwirtschaft"), (1, 1, "2", "Ötzis Beil"), (0, 1, "3", "Schrift"), (0, 1, "4", "Uruk wird|Stadt"), (0, 2, "5", "Hammurabi"),
          (2, 3, "6", "Athen"), (2, 3, "7", "Republik"), (2, 4, "8", "Augustus"), (2, 5, "9", "Ende Westroms")]
    slot = {}
    for r, c, n, t in (ev if mit_loesung else []):
        k = slot.get((r, c), 0); slot[(r, c)] = k + 1
        n_in = sum(1 for e in ev if e[0] == r and e[1] == c)
        x = x0 + c * cw + cw / 2; y = y0 + hh + r * rh
        if n_in == 1: cy = y + 45
        else: cy = y + 32 + k * 62
        if n_in == 1:
            d.ellipse(P(x - 18, cy - 18, x + 18, cy + 18), fill=ORANGE); ctext(d, x, cy - 14, n, f(FB, 24), WHITE)
            lines = t.split(" ") if len(t) > 12 else [t]
            for j, ln in enumerate(lines): ctext(d, x, cy + 26 + j * 24, ln, fit(d, ln, FB, 20, cw - 8), INK)
        else:
            xx = x0 + c * cw + 22
            d.ellipse(P(xx - 15, cy - 15, xx + 15, cy + 15), fill=ORANGE); ctext(d, xx, cy - 12, n, f(FB, 21), WHITE)
            for j, ln in enumerate(t.split("|")): ltext(d, xx + 20, cy - 14 + j * 22, ln, fit(d, ln, FB, 19, cw - 48), INK)
    d.rounded_rectangle(P(10, 598, 890, 634), radius=10 * S, fill=WHITE, outline=MUTED, width=2 * S)
    hin = ("Die Zeitbereiche sind verschieden lang – nur gleich breit gezeichnet."
           if mit_loesung else
           "Zeitbereiche verschieden lang, nur gleich breit gezeichnet. Die neun Karten ordnest du im Arbeitsblatt zu.")
    ltext(d, 22, 603, hin, fit(d, hin, FB, 21, 860), RED)
    save(im, IMG + dateiname)   # Achtung: »name« ist im Rumpf als Schleifenvariable vergeben


# ====================================================================== Animierte Grafiken (SVG, Standard 16.11.2026)
# Zwei Grafiken zeigen einen Vorgang und müssen sich darum aufbauen: die Kette vom Vorrat zur Verwaltung
# und der Übergang von der Republik zum Prinzipat. Endzustand = das ganze Bild, Schleife mit Pause.
SFONT = "'Source Sans 3',system-ui,-apple-system,'Segoe UI',sans-serif"
HEX = lambda c: "#%02x%02x%02x" % c
ZYK, ENDE, ZURUECK = 13, 0.95, 0.98


def _svg(w, h, body, titel):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{titel}">'
            f"<title>{titel}</title><style>text{{font-family:{SFONT};fill:{HEX(INK)}}}.b{{font-weight:700}}</style>"
            f"<rect width='{w}' height='{h}' rx='16' fill='{HEX(BG)}'/>{body}</svg>")


def _blende(inner, start):
    """Erscheint ab »start« (Anteil der Schleife) und bleibt bis zum Ende stehen."""
    a = max(0.001, start); b = min(ENDE - 0.02, start + 0.05)
    return (f"<g opacity='1'><animate attributeName='opacity' values='0;0;1;1;0;0' "
            f"keyTimes='0;{a:.3f};{b:.3f};{ENDE:.3f};{ZURUECK:.3f};1' dur='{ZYK}s' repeatCount='indefinite'/>{inner}</g>")


def _kasten(x, y, w, h, titel, unter="", fuell=None, rand=None):
    f, r = HEX(fuell or PALE), HEX(rand or OLIVE)
    gr = 22 if len(titel) <= 13 else (20 if len(titel) <= 18 else 18)
    o = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='12' fill='{f}' stroke='{r}' stroke-width='3'/>"
    o += f"<text class='b' x='{x + w / 2}' y='{y + (h / 2 + 7 if not unter else h / 2 - 4)}' font-size='{gr}' text-anchor='middle'>{titel}</text>"
    if unter:
        us = 18 if len(unter) <= 34 else 15
        o += f"<text x='{x + w / 2}' y='{y + h / 2 + 22}' font-size='{us}' text-anchor='middle' style='fill:{HEX(MUTED)}'>{unter}</text>"
    return o


def _pfeil(x1, y1, x2, y2, col=None, w=5):
    c = HEX(col or (140, 59, 46))
    import math as _m
    a = _m.atan2(y2 - y1, x2 - x1); k = 14
    p1 = (x2 - k * _m.cos(a - 0.45), y2 - k * _m.sin(a - 0.45))
    p2 = (x2 - k * _m.cos(a + 0.45), y2 - k * _m.sin(a + 0.45))
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2 - 0.6 * k * _m.cos(a):.1f}' y2='{y2 - 0.6 * k * _m.sin(a):.1f}' stroke='{c}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{c}'/>")


def kette_svg():
    b = ""
    b += _blende(_kasten(20, 60, 190, 80, "Ernte und Abgaben"), 0.02)
    b += _blende(_pfeil(214, 100, 252, 100), 0.16)
    b += _blende(_kasten(256, 60, 160, 80, "Lager"), 0.22)
    b += _blende(_pfeil(420, 100, 458, 100), 0.34)
    b += _blende(_kasten(462, 60, 190, 80, "Liste", "Zeichen und Zahlen", (251, 242, 214), (201, 162, 39)), 0.40)
    b += _blende(_pfeil(656, 100, 694, 100), 0.52)
    b += _blende(_kasten(698, 60, 182, 80, "Verteilung"), 0.58)
    b += _blende(f"<text class='b' x='450' y='195' font-size='24' text-anchor='middle' style='fill:{HEX((140, 59, 46))}'>"
                 f"Wer die Liste führt, hat Einfluss.</text>", 0.72)
    b += _blende(f"<text x='450' y='228' font-size='19' text-anchor='middle' fill='{HEX(MUTED)}'>"
                 f"Vorrat → Verwaltung → Macht</text>", 0.80)
    open(IMG + "kette.svg", "w", encoding="utf-8").write(_svg(900, 250, b, "Von der Ernte über Lager und Liste zur Verteilung"))


def rom_svg():
    b = _blende(_kasten(60, 30, 780, 96, "Römische Republik", "Ämter · Senat · Volksversammlungen"), 0.02)
    b += _blende(_pfeil(450, 132, 450, 176), 0.22)
    b += _blende(f"<text x='472' y='162' font-size='17' style='fill:{HEX(MUTED)}'>Bürgerkriege: Heere folgen einzelnen Feldherren</text>", 0.28)
    b += _blende(_kasten(60, 182, 780, 104, "Prinzipat des Augustus", "dieselben Einrichtungen – aber Heer und wichtigste Befugnisse bei einer Person",
                         (243, 226, 221), (140, 59, 46)), 0.44)
    b += _blende(f"<text class='b' x='450' y='322' font-size='23' text-anchor='middle' style='fill:{HEX((140, 59, 46))}'>"
                 f"Die Form bleibt. Die Macht wechselt.</text>", 0.66)
    open(IMG + "rom.svg", "w", encoding="utf-8").write(_svg(900, 345, b, "Von der Republik zum Prinzipat"))


if __name__ == "__main__":
    beil(); kette(); karte(); athen(); rom()
    kette_svg(); rom_svg()                                    # animiert: zeigen einen Vorgang (Standard 16.11.2026)
    zeitstrahl()                                              # öffentlich: leeres Raster
    zeitstrahl(True, "zeitstrahl_loesung.png")                # nur Lehrerzentrale und Sicherungsfolie
    print("Bilder:", sorted(os.listdir(IMG)))
