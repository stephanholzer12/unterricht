"""Bilder für TÖW 5AB K1.8 Fairer Handel – alles selbst gezeichnet (keine Buchabbildungen).
Säulen: Inhalt nach Buch S. 37, eigene Gestaltung. Preislogik: eigene Darstellung mit angenommenen Zahlen (Mindestpreis 3.500 US-Dollar je Tonne laut Fairtrade-Meldung 11.12.2025).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ab-k1-8-fairer-handel/skizzen.py  →  5ab-toew/k1-8-fairer-handel/img/*.png"""
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



def saeulen():
    im, d = canvas(900, 520)
    ctext(d, 450, 22, "Fairtrade-Standards: drei Säulen", fit(d, "Fairtrade-Standards: drei Säulen", FB, 30, 800), INK)
    d.rounded_rectangle(P(60, 90, 840, 130), radius=14 * S, fill=OLIVE)
    ctext(d, 450, 96, "Fairer Handel – bessere Bedingungen für Produzenten", fit(d, "Fairer Handel – bessere Bedingungen für Produzenten", FB, 24, 740), WHITE)
    spalten = [("Soziales", GREEN, ["Verbot ausbeuterischer", "Kinderarbeit", "Gewerkschaftliche", "Organisation"]),
               ("Ökologisches", TEAL, ["Verbotene Pestizide", "(Liste)", "Förderung des", "Bio-Anbaus"]),
               ("Ökonomisches", ORANGE, ["Rückverfolgbarkeit", "der Ware", "Transparente", "Handelsbeziehungen"])]
    for k, (t, c, zl) in enumerate(spalten):
        x = 90 + k * 260
        d.rounded_rectangle(P(x, 150, x + 220, 470), radius=16 * S, fill=WHITE, outline=c, width=4 * S)
        d.rounded_rectangle(P(x, 150, x + 220, 205), radius=16 * S, fill=c)
        ctext(d, x + 110, 160, t, fit(d, t, FB, 30, 200), WHITE)
        for i, z in enumerate(zl):
            ctext(d, x + 110, 235 + i * 42, z, f(FR, 22), INK)
    save(im, IMG + "saeulen.png")


def preis():
    im, d = canvas(900, 560)
    ctext(d, 450, 18, "Mindestpreis: das Sicherheitsnetz (Zahlen angenommen)", fit(d, "Mindestpreis: das Sicherheitsnetz (Zahlen angenommen)", FB, 28, 840), INK)
    x0, y0, x1, y1 = 120, 90, 860, 470     # Diagrammfläche
    vmax = 5000.0
    Y = lambda v: y1 - (v / vmax) * (y1 - y0)
    for v in (0, 1000, 2000, 3000, 4000, 5000):
        d.line(P(x0, Y(v), x1, Y(v)), fill=LIGHT, width=2 * S)
        d.text((x0 * S - 12 * S - d.textlength(f"{v:,}".replace(",", "."), font=f(FR, 20)), (Y(v) - 11) * S), f"{v:,}".replace(",", "."), font=f(FR, 20), fill=MUTED)
    d.line(P(x0, Y(3500), x1, Y(3500)), fill=GREEN, width=5 * S)
    ltext(d, x0 + 8, Y(3500) - 30, "Mindestpreis 3.500", f(FB, 22), GREEN)
    welt = [2900, 2500, 2800, 3300, 4200, 4900, 4300, 3000]     # ausgedachter Verlauf
    pts = [(x0 + 50 + i * (x1 - x0 - 100) / (len(welt) - 1), Y(v)) for i, v in enumerate(welt)]
    d.line([(px * S, py * S) for px, py in pts], fill=ORANGE, width=5 * S)
    for px, py in pts: d.ellipse(P(px - 6, py - 6, px + 6, py + 6), fill=ORANGE)
    ltext(d, 130, Y(4650), "Steigt der Weltmarkt: Marktpreis gilt", f(FB, 20), ORANGE)
    ltext(d, pts[1][0] - 80, Y(2100) + 8, "Weltmarkt fällt: Mindestpreis fängt auf", f(FB, 20), RED)
    ctext(d, 490, 492, "angenommener Verlauf des Weltmarktpreises (US-Dollar je Tonne)", f(FR, 22), MUTED)
    d.line(P(x0, y0, x0, y1), fill=INK, width=3 * S); d.line(P(x0, y1, x1, y1), fill=INK, width=3 * S)
    ctext(d, 450, 522, "Die Prämie (275 je Tonne) kommt in beiden Fällen zusätzlich.", f(FB, 22), INK)
    save(im, IMG + "preis.png")


if __name__ == "__main__":
    saeulen(); preis(); print("Bilder:", sorted(os.listdir(IMG)))
