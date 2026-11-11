"""Bilder für IWK 5AK K2.1 Die Welt ohne Grenzen: Globalisierung – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ak-k2-globalisierung/skizzen.py  →  5ak-iwk/k2-1-globalisierung/img/*.png"""
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



BROWN, BLUE = (120, 86, 52), (46, 125, 140)


# ------------------------------------------------------------ Zeitstrahl: Wann begann die Globalisierung?
def zeitstrahl():
    im, d = canvas(900, 440)
    ctext(d, 450, 12, "Wann begann die Globalisierung? Je nach Kriterium anders", f(FB, 28), INK)
    d.line(P(60, 230, 840, 230), fill=INK, width=6 * S)
    ev = [(100, "1492", "Kolumbus", "Seeweg nach Amerika", OLIVE, 70), (270, "1844", "Telegraf", "erste Nachricht per Strom", TEAL, 290),
          (440, "1944", "IWF und Weltbank", "Regeln nach dem Krieg", ORANGE, 70), (610, "1980er", "Technik", "Rivalität USA – Sowjetunion", BROWN, 290),
          (780, "ab 1990er", "Internet", "Satelliten, Datenverkehr", GREEN, 70)]
    for x, jahr, kurz, text, c, y in ev:
        d.ellipse(P(x - 11, 219, x + 11, 241), fill=c)
        yy = y + 60 if y < 230 else y - 10
        d.line(P(x, 241 if y > 230 else 219, x, y + 70 if y < 230 else y), fill=c, width=3 * S)
        d.rounded_rectangle(P(x - 78, y, x + 78, y + 70), radius=12 * S, fill=WHITE, outline=c, width=3 * S)
        ctext(d, x, y + 6, jahr, f(FB, 24), c)
        ctext(d, x, y + 34, kurz, fit(d, kurz, FB, 18, 140), INK)
        ctext(d, x, y + 53, text, fit(d, text, FR, 14, 146), MUTED)
    ctext(d, 450, 395, "Dazwischen: Zwischenkriegszeit = Phase der Deglobalisierung (Handel geht zurück)", f(FR, 20), MUTED)
    save(im, IMG + "zeitstrahl.png")


# ------------------------------------------------------------ Sechs Antriebskräfte
def antriebe():
    im, d = canvas(900, 520)
    ctext(d, 450, 12, "Sechs Antriebskräfte der Globalisierung (Buch S. 45–47)", f(FB, 28), INK)
    k = [("Informations-", "revolution", OLIVE), ("Transport-", "technik", TEAL), ("Markt-", "wirtschaft", ORANGE),
         ("Liberalisierung", "", BROWN), ("Transnationale", "Konzerne", GREEN), ("Normen und", "Standards", BLUE)]
    for i, (a, b, c) in enumerate(k):
        x, y = 30 + (i % 3) * 290, 70 + (i // 3) * 190
        d.rounded_rectangle(P(x, y, x + 270, y + 160), radius=16 * S, fill=WHITE, outline=c, width=4 * S)
        d.ellipse(P(x + 14, y + 14, x + 54, y + 54), fill=c); ctext(d, x + 34, y + 19, str(i + 1), f(FB, 24), WHITE)
        ctext(d, x + 140, y + 62, a, f(FB, 28), INK)
        if b: ctext(d, x + 140, y + 98, b, f(FB, 28), INK)
    ctext(d, 450, 470, "Ordne zu: Welche Antriebskraft steckt hinter welchem Beispiel?", f(FR, 22), MUTED)
    save(im, IMG + "antriebskraefte.png")


# ------------------------------------------------------------ Digital Divide (ITU Facts and Figures 2025)
def digital():
    im, d = canvas(900, 520)
    ctext(d, 450, 10, "Wer nutzt das Internet? Anteil der Bevölkerung 2025", f(FB, 28), INK)
    gr = [("Länder mit hohem\nEinkommen", 94, GREEN), ("Länder mit niedrigem\nEinkommen", 23, RED), ("Stadt", 85, GREEN), ("Land", 58, ORANGE), ("Männer", 77, GREEN), ("Frauen", 71, ORANGE)]
    x0, base, h = 60, 400, 280
    d.line(P(40, base, 860, base), fill=INK, width=3 * S)
    for i, (t, v, c) in enumerate(gr):
        x = x0 + i * 135 + (i // 2) * 8
        d.rectangle(P(x, base - h * v / 100, x + 100, base), fill=c)
        ctext(d, x + 50, base - h * v / 100 - 36, f"{v} %", f(FB, 26), INK)
        for j, ln in enumerate(t.split("\n")): ctext(d, x + 50, base + 8 + j * 22, ln, fit(d, ln, FR, 18, 130), INK)
    ctext(d, 450, 470, "Quelle: ITU, Facts and Figures 2025 (17.11.2025) · rund 6 Mrd. online, 2,2 Mrd. offline", f(FR, 18), MUTED)
    save(im, IMG + "digital_divide.png")


if __name__ == "__main__":
    zeitstrahl(); antriebe(); digital()
    print("Bilder:", sorted(os.listdir(IMG)))
