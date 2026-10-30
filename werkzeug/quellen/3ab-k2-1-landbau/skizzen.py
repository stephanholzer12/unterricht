"""Bilder für NAWI 3AB K2.1 Formen der Landwirtschaft – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3ab-k2-1-landbau/skizzen.py  →  3ab-nawi/k2-1-landbau/img/*.png"""
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


# ------------------------------------------------------------ Acker: Ernte raus, Nährstoffe zurück
def acker():
    im, d = canvas(900, 560, SKY)
    d.rectangle(P(0, 300, 900, 560), fill=SOIL)
    d.rectangle(P(0, 300, 900, 330), fill=BROWN)
    # Poren und Humus
    import random
    random.seed(4)
    for _ in range(70):
        x, y, r = random.randint(20, 880), random.randint(340, 540), random.randint(3, 8)
        d.ellipse(P(x - r, y - r, x + r, y + r), fill=(150, 112, 74))
    for _ in range(40):
        x, y, r = random.randint(20, 880), random.randint(340, 540), random.randint(3, 6)
        d.ellipse(P(x - r, y - r, x + r, y + r), fill=(205, 175, 135))
    # Regenwurm
    pts = [(560 + k * 12, 470 + 10 * math.sin(k / 1.5)) for k in range(12)]
    d.line([(px * S, py * S) for px, py in pts], fill=(196, 108, 108), width=10 * S, joint="curve")
    # Getreidehalme mit Wurzeln
    for x in range(330, 600, 34):
        d.line(P(x, 300, x, 170), fill=GREEN, width=5 * S)
        d.ellipse(P(x - 9, 140, x + 9, 185), fill=YELLOW, outline=(170, 130, 30), width=2 * S)
        for dx in (-14, 0, 14):
            d.line(P(x, 300, x + dx, 360), fill=(230, 220, 190), width=2 * S)
    ltext(d, 610, 370, "Poren, Humus, Bodenleben", f(FB, 20), WHITE)
    # Pfeil Ernte nach oben rechts
    arrow(d, 620, 170, 760, 80, RED, 7, 22)
    label_box(d, 680, 18, 210, 92, "Ernte", ["nimmt Nährstoffe mit"], RED)
    # Pfeil Nährstoffe zurück links
    arrow(d, 150, 110, 300, 250, GREEN, 7, 22)
    label_box(d, 20, 18, 270, 118, "Zurück aufs Feld", ["Dünger, Mist, Kompost,", "Leguminosen"], OLIVE)
    # Verdichtung / Erosion
    ltext(d, 30, 400, "Verdichtung:", f(FB, 20), WHITE); ltext(d, 30, 426, "schwere Maschinen", f(FR, 20), WHITE)
    ltext(d, 30, 470, "Erosion:", f(FB, 20), WHITE); ltext(d, 30, 496, "Wasser und Wind", f(FR, 20), WHITE)
    save(im, IMG + "acker.png")


# ------------------------------------------------------------ Fläche für 80 dt Weizen
def flaeche():
    im, d = canvas(900, 390, BG)
    ctext(d, 450, 18, "Dieselbe Menge: 80 dt Weizen", f(FB, 30), INK)
    sc = 150  # Pixel je Wurzel-ha
    w1 = sc; h1 = sc
    d.rectangle(P(80, 120, 80 + w1, 120 + h1), fill=(214, 196, 120), outline=INK, width=3 * S)
    ctext(d, 80 + w1 / 2, 120 + h1 + 12, "konventionell", f(FB, 22), INK)
    ctext(d, 80 + w1 / 2, 120 + h1 + 40, "80 dt/ha → 1,00 ha", f(FR, 22), INK)
    w2 = sc * 2.222
    d.rectangle(P(360, 120, 360 + w2, 120 + h1), fill=(170, 196, 110), outline=INK, width=3 * S)
    d.line(P(360 + sc, 120, 360 + sc, 120 + h1), fill=INK, width=1 * S)
    d.line(P(360 + 2 * sc, 120, 360 + 2 * sc, 120 + h1), fill=INK, width=1 * S)
    ctext(d, 360 + w2 / 2, 120 + h1 + 12, "bio", f(FB, 22), INK)
    ctext(d, 360 + w2 / 2, 120 + h1 + 40, "36 dt/ha → 80 : 36 = 2,22 ha", f(FR, 22), INK)
    ctext(d, 450, 68, "Fläche = Erntemenge : Ertrag", f(FB, 24), TEAL)
    ctext(d, 450, 352, "Ältere deutsche Durchschnittswerte 2015/16 – kein allgemeiner Wert für jeden Betrieb", f(FR, 18), RED)
    save(im, IMG + "flaeche.png")


# ------------------------------------------------------------ Genschere in vier Schritten (Modell)
def dna(d, x, y, w, cut=None, mark=None, changed=False):
    for row, col in ((0, (59, 74, 47)), (34, (59, 74, 47))):
        if cut is None:
            d.rounded_rectangle(P(x, y + row, x + w, y + row + 14), radius=6 * S, fill=col)
        else:
            d.rounded_rectangle(P(x, y + row, cut - 6, y + row + 14), radius=6 * S, fill=col)
            d.rounded_rectangle(P(cut + 6, y + row, x + w, y + row + 14), radius=6 * S, fill=col)
    for k in range(int(x) + 8, int(x + w) - 4, 14):
        if cut is not None and abs(k - cut) < 10: continue
        d.line(P(k, y + 14, k, y + 34), fill=(160, 170, 150), width=3 * S)
    if mark:
        d.rectangle(P(mark[0], y - 4, mark[1], y + 52), outline=ORANGE, width=3 * S)
    if changed:
        d.rounded_rectangle(P(cut - 12, y, cut + 12, y + 48), radius=6 * S, fill=ORANGE)


def genschere():
    im, d = canvas(1200, 420, BG)
    xs = [20, 315, 610, 905]; W = 275
    tit = ["1 Ziel finden", "2 Schneiden", "3 Reparieren", "4 Prüfen"]
    txt = [["Leit-RNA passt zu", "einer DNA-Stelle"], ["Cas9 schneidet", "beide Stränge"], ["Zelle flickt –", "Stelle verändert"], ["Labor und", "Feldversuch"]]
    cols = [TEAL, RED, OLIVE, GREEN]
    for i, x in enumerate(xs):
        d.rounded_rectangle(P(x, 20, x + W, 400), radius=18 * S, fill=WHITE, outline=cols[i], width=3 * S)
        d.rounded_rectangle(P(x, 20, x + W, 66), radius=18 * S, fill=cols[i]); d.rectangle(P(x, 46, x + W, 66), fill=cols[i])
        ctext(d, x + W / 2, 28, tit[i], f(FB, 26), WHITE)
        for k, t in enumerate(txt[i]): ctext(d, x + W / 2, 320 + k * 30, t, f(FR, 22), INK)
    mid = lambda x: x + W / 2
    # 1: DNA + Leit-RNA (teal Band) an markierter Stelle
    dna(d, xs[0] + 20, 170, W - 40, mark=(mid(xs[0]) - 35, mid(xs[0]) + 35))
    d.rounded_rectangle(P(mid(xs[0]) - 35, 120, mid(xs[0]) + 35, 136), radius=6 * S, fill=TEAL)
    ctext(d, mid(xs[0]), 88, "Leit-RNA", f(FB, 20), TEAL)
    # 2: Cas9 (rote Blase) + Schnitt
    dna(d, xs[1] + 20, 170, W - 40, cut=mid(xs[1]))
    d.ellipse(P(mid(xs[1]) - 55, 120, mid(xs[1]) + 55, 250), outline=RED, width=4 * S)
    ctext(d, mid(xs[1]), 84, "Cas9", f(FB, 22), RED)
    # 3: repariert, Stelle orange
    dna(d, xs[2] + 20, 170, W - 40, cut=mid(xs[2]), changed=True)
    ctext(d, mid(xs[2]), 100, "verändert", f(FB, 20), ORANGE)
    # 4: Pflanze + Häkchen/Fragezeichen
    x = mid(xs[3])
    d.line(P(x, 280, x, 150), fill=GREEN, width=6 * S)
    for dy, sgn in ((240, -1), (205, 1), (170, -1)):
        d.ellipse(P(x + sgn * 10 - (40 if sgn < 0 else 0), dy - 14, x + sgn * 10 + (40 if sgn > 0 else 0), dy + 14), fill=GREEN)
    ctext(d, x + 70, 110, "?", f(FB, 60), ORANGE)
    ctext(d, mid(xs[3]), 285, "Taugt die Sorte?", f(FB, 20), INK)
    for i in range(3):
        arrow(d, xs[i] + W + 2, 210, xs[i + 1] - 2, 210, MUTED, 4, 14)
    save(im, IMG + "genschere.png")


# ------------------------------------------------------------ 200 Ratten → 2 Geschlechter × 10 Gruppen × 10 Tiere
def gruppen():
    im, d = canvas(1000, 470, BG)
    ctext(d, 500, 12, "200 Ratten – aber nur 10 je Gruppe", f(FB, 30), INK)
    for g, (lab, col, y0) in enumerate((("100 Weibchen", RED, 80), ("100 Männchen", TEAL, 270))):
        ltext(d, 20, y0 + 50, lab, f(FB, 22), col)
        for grp in range(10):
            gx = 180 + grp * 80
            d.rounded_rectangle(P(gx, y0, gx + 70, y0 + 150), radius=10 * S, fill=WHITE, outline=col, width=2 * S)
            for k in range(10):
                cx, cy = gx + 18 + (k % 2) * 34, y0 + 18 + (k // 2) * 28
                d.ellipse(P(cx - 9, cy - 9, cx + 9, cy + 9), fill=col)
            if g == 0: ctext(d, gx + 35, y0 - 26, f"G{grp + 1}", f(FB, 18), MUTED)
    ctext(d, 500, 438, "10 Gruppen je Geschlecht (davon 1 Kontrollgruppe) · je 10 Tiere", f(FR, 20), INK)
    save(im, IMG + "gruppen.png")


if __name__ == "__main__":
    acker(); flaeche(); genschere(); gruppen()
    print("Bilder:", sorted(os.listdir(IMG)))
