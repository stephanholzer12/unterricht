"""Skizzen und Icon für die Stationen K1.2 (2AB) im Stil der Bindungsarten-Versuche zeichnen.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/2ab-k1-2-stationen/skizzen.py
Schreibt 2ab-nawi/k1-2-bindungen/vs-img/d_c4b.png, d_c10b.png, d_c3b.png, i_muenze.png und werkzeug/icons/muenze.png."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DST = os.path.join(ROOT, "2ab-nawi/k1-2-bindungen/vs-img/")
FR = os.path.join(ROOT, "werkzeug/schriften/carlito-Regular.ttf")
FB = os.path.join(ROOT, "werkzeug/schriften/carlito-Bold.ttf")
BG, INK, RED, GREY, BLUE, OIL, OIL2 = (242, 243, 238), (59, 74, 47), (204, 0, 30), (122, 132, 145), (128, 170, 230), (244, 200, 80), (246, 226, 150)
f = lambda p, s: ImageFont.truetype(p, s)
S = 2  # Supersampling


def canvas():
    im = Image.new("RGB", (900 * S, 629 * S), BG); return im, ImageDraw.Draw(im)


def ctext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w / 2, y * S), t, font=font, fill=fill)


def save(im, name):
    im.resize((900, 629), Image.LANCZOS).quantize(colors=128).save(DST + name, optimize=True)


def tube(d, cx, layers):
    """Reagenzglas, Boden unten (y=480). layers: [(Höhe px, Farbe)] von unten nach oben."""
    x0, x1, top, bot = cx - 30, cx + 30, 200, 485
    y = bot - 10
    for h, col in layers:
        d.rectangle([(x0 + 6) * S, (y - h) * S, (x1 - 6) * S, y * S], fill=col); y -= h
    d.rounded_rectangle([x0 * S, top * S, x1 * S, bot * S], radius=30 * S, outline=GREY, width=5 * S)
    d.rectangle([(x0 - 6) * S, (top - 16) * S, (x1 + 6) * S, top * S], fill=(242, 242, 242), outline=GREY, width=3 * S)


# ---------- V8 Wer mischt sich mit wem? (ohne Spiritus und Paraffinöl)
im, d = canvas()
ctext(d, 450, 34, "verschließen · 10 s schütteln · 1 min warten", f(FB, 34 * S), INK)
ctext(d, 450, 80, "eine Phase oder zwei?", f(FB, 32 * S), RED)
xs = [180, 360, 540, 720]
for i, x in enumerate(xs): ctext(d, x, 122, str(i + 1), f(FB, 40 * S), RED)
tube(d, xs[0], [(190, BLUE)])
tube(d, xs[1], [(95, BLUE), (95, OIL)])
tube(d, xs[2], [(190, (186, 205, 228))])
tube(d, xs[3], [(18, (255, 255, 255)), (172, OIL2)])
d.rectangle([75 * S, 500 * S, 825 * S, 520 * S], fill=(240, 240, 240), outline=GREY, width=3 * S)
for x, a, b in [(xs[0], "Wasser +", "Glycerin"), (xs[1], "Wasser +", "Olivenöl"), (xs[2], "Nr. 2 +", "Waschmittel"), (xs[3], "Olivenöl +", "Kochsalz")]:
    ctext(d, x, 538, a, f(FR, 28 * S), INK); ctext(d, x, 574, b, f(FB, 28 * S), INK)
save(im, "d_c4b.png")

# ---------- V9 Wasser mit Haut (Münze + Büroklammer)
im, d = canvas()
ctext(d, 225, 34, "1  Tropfen zählen", f(FB, 34 * S), RED)
ctext(d, 675, 34, "2  Büroklammer", f(FB, 34 * S), RED)
# Pipette über Münze
d.rounded_rectangle([210 * S, 110 * S, 240 * S, 230 * S], radius=8 * S, outline=GREY, width=4 * S, fill=(245, 248, 252))
d.ellipse([200 * S, 80 * S, 250 * S, 120 * S], fill=RED)
d.polygon([(225 * S, 245 * S), (215 * S, 268 * S), (235 * S, 268 * S)], fill=BLUE)
# Münze von der Seite mit Wasserberg
d.ellipse([120 * S, 300 * S, 330 * S, 405 * S], fill=BLUE)
d.rectangle([120 * S, 352 * S, 330 * S, 392 * S], fill=(205, 160, 90))
d.ellipse([120 * S, 372 * S, 330 * S, 412 * S], fill=(185, 140, 70), outline=GREY, width=3 * S)
d.ellipse([120 * S, 332 * S, 330 * S, 372 * S], fill=(225, 185, 110), outline=GREY, width=3 * S)
d.chord([120 * S, 270 * S, 330 * S, 395 * S], 180, 360, fill=BLUE, outline=(90, 140, 210), width=3 * S)
ctext(d, 225, 440, "Wasserberg auf der Münze", f(FR, 28 * S), INK)
ctext(d, 225, 478, "erst Wasser, dann Seifenwasser", f(FR, 26 * S), INK)
# Petrischale mit Büroklammer
d.ellipse([500 * S, 250 * S, 860 * S, 420 * S], fill=(170, 205, 240), outline=GREY, width=5 * S)
d.ellipse([500 * S, 238 * S, 860 * S, 400 * S], outline=GREY, width=3 * S)
d.rounded_rectangle([600 * S, 305 * S, 720 * S, 340 * S], radius=14 * S, outline=(80, 85, 90), width=6 * S)
d.rounded_rectangle([615 * S, 313 * S, 705 * S, 333 * S], radius=9 * S, outline=(80, 85, 90), width=5 * S)
d.rectangle([785 * S, 140 * S, 835 * S, 210 * S], fill=(220, 232, 245), outline=(110, 150, 190), width=4 * S)
d.rectangle([800 * S, 122 * S, 820 * S, 140 * S], fill=(225, 225, 225))
d.polygon([(810 * S, 222 * S), (800 * S, 245 * S), (820 * S, 245 * S)], fill=BLUE)
ctext(d, 700, 92, "1 Tropfen Waschmittel →", f(FB, 24 * S), RED)
ctext(d, 680, 440, "auf Filterpapier auflegen,", f(FR, 28 * S), INK)
ctext(d, 680, 478, "Papier sinkt – Klammer bleibt?", f(FR, 26 * S), INK)
d.line([450 * S, 90 * S, 450 * S, 560 * S], fill=(210, 214, 200), width=3 * S)
ctext(d, 450, 572, "Petrischale mit Leitungswasser · eigene Münze (z. B. 10 Cent)", f(FR, 26 * S), INK)
save(im, "d_c10b.png")

# ---------- V2 Salzkörner unter der Lupe (ohne Trocknen)
im, d = canvas()
ctext(d, 225, 60, "Kochsalz · Zucker · Alaun", f(FB, 32 * S), INK)
for i, (lab, col) in enumerate([("Salz", (250, 250, 250)), ("Zucker", (252, 248, 235)), ("Alaun", (236, 240, 248))]):
    y = 160 + i * 115
    d.rectangle([50 * S, y * S, 400 * S, (y + 70) * S], fill=(225, 236, 246), outline=GREY, width=4 * S)
    d.rectangle([50 * S, y * S, 120 * S, (y + 70) * S], fill=(255, 255, 255), outline=GREY, width=4 * S)
    for k in range(7):
        x = 170 + k * 30 + (k % 2) * 6; yy = y + 26 + (k % 3) * 8
        d.rectangle([x * S, yy * S, (x + 12) * S, (yy + 12) * S], fill=col, outline=(110, 115, 120), width=2 * S)
    d.text((58 * S, (y + 20) * S), lab, font=f(FR, 22 * S), fill=INK)
ctext(d, 225, 520, "eine Spatelspitze auf den Objektträger", f(FR, 26 * S), INK)
d.line([425 * S, 330 * S, 490 * S, 330 * S], fill=INK, width=6 * S)
d.polygon([(500 * S, 330 * S), (478 * S, 316 * S), (478 * S, 344 * S)], fill=INK)
d.ellipse([505 * S, 140 * S, 865 * S, 500 * S], fill=(245, 248, 252), outline=(95, 100, 105), width=10 * S)
for x, y, s in [(600, 230, 70), (720, 260, 90), (580, 360, 40), (660, 330, 55), (770, 380, 50)]:
    d.rectangle([x * S, y * S, (x + s) * S, (y + s) * S], outline=GREY, width=5 * S)
    d.rectangle([(x + s // 4) * S, (y + s // 4) * S, (x + 3 * s // 4) * S, (y + 3 * s // 4) * S], outline=(170, 176, 182), width=3 * S)
ctext(d, 685, 535, "unter Lupe oder Mikroskop", f(FB, 28 * S), RED)
save(im, "d_c3b.png")

# ---------- Icon Münze (180 × 108, transparent, flach, graue Kontur)
ic = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ic)
for (x, y, c1, c2) in [(30, 30, (196, 150, 80), (224, 184, 110)), (78, 20, (180, 182, 186), (214, 216, 220))]:
    d.ellipse([x * S, (y + 8) * S, (x + 72) * S, (y + 72) * S], fill=c1, outline=(110, 115, 120), width=2 * S)
    d.ellipse([x * S, y * S, (x + 72) * S, (y + 64) * S], fill=c2, outline=(110, 115, 120), width=2 * S)
    d.ellipse([(x + 14) * S, (y + 12) * S, (x + 58) * S, (y + 52) * S], outline=(150, 120, 70) if c1[0] > 190 else (150, 152, 156), width=2 * S)
ic = ic.resize((180, 108), Image.LANCZOS)
ic.save(DST + "i_muenze.png", optimize=True); ic.save(os.path.join(ROOT, "werkzeug/icons/muenze.png"), optimize=True)
# ---------- Icon Aufbewahrungswanne
ic = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ic)
d.polygon([(22 * S, 34 * S), (158 * S, 34 * S), (146 * S, 92 * S), (34 * S, 92 * S)], fill=(80, 180, 200), outline=(110, 115, 120))
d.rectangle([16 * S, 26 * S, 164 * S, 36 * S], fill=(110, 200, 215), outline=(110, 115, 120), width=2 * S)
d.line([34 * S, 52 * S, 146 * S, 52 * S], fill=(60, 150, 170), width=2 * S)
ic = ic.resize((180, 108), Image.LANCZOS)
ic.save(DST + "i_wanne.png", optimize=True); ic.save(os.path.join(ROOT, "werkzeug/icons/wanne.png"), optimize=True)
print("ok")
