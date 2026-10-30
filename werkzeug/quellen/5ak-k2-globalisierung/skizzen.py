"""Bilder für IWK 5AK K2 Globalisierung – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ak-k2-globalisierung/skizzen.py  →  5ak-iwk/k2-globalisierung/img/*.png"""
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


# ------------------------------------------------------------ Modell Sportuhr
def sportuhr():
    im, d = canvas(900, 560)
    ctext(d, 450, 12, "Modell »Sportuhr mit KI-Dienst« – Orte sind angenommen, keine echte Lieferkette", fit(d, "Modell »Sportuhr mit KI-Dienst« – Orte sind angenommen, keine echte Lieferkette", FB, 24, 860), INK)
    st = [(30, 70, "1 Entwicklung", ["und Vermarktung", "Europa"], OLIVE), (320, 70, "2 Halbleiter", ["Ostasien"], TEAL), (610, 70, "3 Montage", ["Südostasien"], ORANGE),
          (30, 300, "4 Rohstoffe", ["mehrere", "Weltregionen"], BROWN), (320, 300, "5 Rechenzentrum", ["internationaler", "Anbieter"], BLUE), (610, 300, "6 Absatz", ["Europa und USA"], GREEN)]
    for x, y, t, ls, c in st:
        label_box(d, x, y, 260, 130, t, ls, c)
    ctext(d, 450, 450, "Verbinde die Stationen mit Pfeilen und beschrifte sie: Waren · Geld · Daten · Wissen", fit(d, "Verbinde die Stationen mit Pfeilen und beschrifte sie: Waren · Geld · Daten · Wissen", FB, 22, 860), INK)
    ctext(d, 450, 492, "Mindestens vier Stationen. Wer bezahlt wen? Was fließt zurück?", f(FR, 20), MUTED)
    save(im, IMG + "sportuhr.png")


# ------------------------------------------------------------ Vier Bedeutungen von »Übernahme«
def vier_fragen():
    im, d = canvas(900, 480)
    ctext(d, 450, 12, "»KI übernimmt die Macht« – vier verschiedene Fragen", f(FB, 28), INK)
    felder = [(30, 70, "Arbeit", ["Welche Tätigkeiten werden", "automatisiert oder unterstützt?"], GREEN),
              (460, 70, "Macht", ["Wer kontrolliert Rechenleistung,", "Daten und Plattformen?"], TEAL),
              (30, 260, "Abhängigkeit", ["Wer verliert Fähigkeiten oder", "Spielraum, wenn er sich verlässt?"], ORANGE),
              (460, 260, "Kontrollverlust", ["Könnten künftige Systeme", "Aufsicht wirksam umgehen?"], RED)]
    for x, y, t, ls, c in felder:
        label_box(d, x, y, 410, 160, t, ls, c)
    ctext(d, 450, 440, "Nicht ineinander rutschen lassen: Automatisieren ist nicht Herrschaft ausüben.", f(FB, 20), MUTED)
    save(im, IMG + "vier_fragen.png")


if __name__ == "__main__":
    sportuhr(); vier_fragen()
    print("Bilder:", sorted(os.listdir(IMG)))
