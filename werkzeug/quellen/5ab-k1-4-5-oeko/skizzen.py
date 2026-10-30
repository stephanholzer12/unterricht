"""Bilder für TÖW 5AB K1.4–1.5 Ökodesign und Ökobilanz – alles selbst gezeichnet (keine Buchabbildungen).
Lebenszyklus: Inhalt nach Buch S. 23, eigenständig neu gestaltet. Vier Schritte: nach ISO 14040 (öffentliches Abstract) und EU-Empfehlung 2021/2279.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ab-k1-4-5-oeko/skizzen.py  →  5ab-toew/k1-4-5-oeko/img/*.png"""
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


# ------------------------------------------------------------ Einstieg: zwei Flaschen (schematisch, keine echten Produkte)
def flasche(d, cx, top, h, w, col, deckel_col, dick=3, ersatz=False, verklebt=False):
    neck = w * 0.42
    d.rounded_rectangle(P(cx - w / 2, top + 70, cx + w / 2, top + h), radius=26 * S, fill=col, outline=INK, width=dick * S)
    d.polygon([(p * S) for p in (cx - w / 2 + 8, top + 80, cx - neck / 2, top + 42, cx + neck / 2, top + 42, cx + w / 2 - 8, top + 80)], fill=col)
    d.line(P(cx - w / 2 + 8, top + 80, cx - neck / 2, top + 42), fill=INK, width=dick * S)
    d.line(P(cx + w / 2 - 8, top + 80, cx + neck / 2, top + 42), fill=INK, width=dick * S)
    d.rounded_rectangle(P(cx - neck / 2 - 6, top, cx + neck / 2 + 6, top + 44), radius=8 * S, fill=deckel_col, outline=INK, width=3 * S)
    d.rectangle(P(cx - neck / 2 - 6, top + 36, cx + neck / 2 + 6, top + 44), fill=(60, 60, 60))   # Dichtung
    if verklebt:
        for k in range(4): d.line(P(cx - neck / 2 - 6 + k * 14, top + 46, cx - neck / 2 + 4 + k * 14, top + 56), fill=RED, width=2 * S)
    if ersatz:
        x0 = cx + w / 2 + 34
        d.rounded_rectangle(P(x0, top + 10, x0 + neck + 12, top + 54), radius=8 * S, fill=deckel_col, outline=INK, width=3 * S)
        d.rectangle(P(x0, top + 46, x0 + neck + 12, top + 54), fill=(60, 60, 60))
        d.ellipse(P(x0 + 4, top + 70, x0 + neck + 8, top + 88), outline=(60, 60, 60), width=5 * S)
        ctext(d, x0 + (neck + 12) / 2, top + 96, "Ersatzteile", f(FB, 18), TEAL)
    for k in range(1, 4):
        y = top + 70 + (h - 70) * k / 4
        d.line(P(cx - w / 2 + 14, y, cx - w / 2 + 34, y), fill=INK, width=2 * S)


def flaschen():
    im, d = canvas(900, 560)
    ctext(d, 450, 14, "Welche Flasche würdest du beschaffen?", f(FB, 30), INK)
    flasche(d, 230, 90, 330, 112, (205, 230, 235), (120, 180, 200), dick=2)
    flasche(d, 610, 90, 330, 132, (190, 200, 175), OLIVE, dick=5, ersatz=True)
    for x, name, col in ((230, "Flasche A", TEAL), (610, "Flasche B", OLIVE)):
        d.rounded_rectangle(P(x - 75, 440, x + 75, 478), radius=10 * S, fill=col)
        ctext(d, x, 446, name, f(FB, 24), WHITE)
    ctext(d, 230, 490, "sehr leicht · 8 €", f(FR, 22), INK); ctext(d, 230, 518, "Deckel fest verbaut", f(FR, 22), INK)
    ctext(d, 610, 490, "robuster · 30 €", f(FR, 22), INK); ctext(d, 610, 518, "Deckel und Dichtung tauschbar", f(FR, 22), INK)
    save(im, IMG + "flaschen.png")


# ------------------------------------------------------------ Lebenszyklus (Buch S. 23 inhaltlich, eigene Darstellung)
def lebenszyklus():
    im, d = canvas(900, 640)
    ctext(d, 450, 12, "Der Lebenszyklus einer Trinkflasche", f(FB, 30), INK)
    cx, cy, rx, ry = 450, 345, 300, 205
    steps = [("Rohstoffe", ["gewinnen,", "aufbereiten"], TEAL), ("Herstellung", ["Material, Energie,", "Hilfsstoffe"], OLIVE),
             ("Transport und Verkauf", ["Lager,", "Lieferung"], ORANGE), ("Nutzung und Pflege", ["befüllen, trinken,", "reinigen"], GREEN),
             ("Nutzungsende", ["wiederverwenden,", "verwerten, entsorgen"], RED)]
    pos = []
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    for i in range(4):
        if i == 2:
            arrow(d, pos[2][0] - 118, pos[2][1], pos[3][0] + 122, pos[3][1], GREY, 5, 18); continue
        a0 = -math.pi / 2 + i * 2 * math.pi / 5 + 0.40; a1 = a0 + 2 * math.pi / 5 - 0.84
        arrow(d, cx + rx * math.cos(a0), cy + ry * math.sin(a0), cx + rx * math.cos(a1), cy + ry * math.sin(a1), GREY, 5, 18)
    # Rückführung nur als möglicher Weg (gestrichelt)
    a0 = -math.pi / 2 + 4 * 2 * math.pi / 5 + 0.36; a1 = -math.pi / 2 + 2 * math.pi - 0.36
    pts = [(cx + rx * math.cos(a0 + (a1 - a0) * k / 12), cy + ry * math.sin(a0 + (a1 - a0) * k / 12)) for k in range(13)]
    dashed_arrow(d, pts, MUTED, 4)
    ltext(d, 170, 120, "Recycling: möglich,", f(FR, 19), MUTED); ltext(d, 170, 144, "nicht automatisch", f(FR, 19), MUTED)
    for (x, y), (t, z, col) in zip(pos, steps):
        w, h = 228, 104
        d.rounded_rectangle(P(x - w / 2, y - h / 2, x + w / 2, y + h / 2), radius=14 * S, fill=WHITE, outline=col, width=4 * S)
        d.rounded_rectangle(P(x - w / 2, y - h / 2, x + w / 2, y - h / 2 + 34), radius=14 * S, fill=col)
        d.rectangle(P(x - w / 2, y - h / 2 + 20, x + w / 2, y - h / 2 + 34), fill=col)
        ctext(d, x, y - h / 2 + 5, t, fit(d, t, FB, 21, w - 16), WHITE)
        for k, s in enumerate(z): ctext(d, x, y - h / 2 + 40 + k * 26, s, f(FR, 20), INK)
    d.ellipse(P(cx - 150, cy - 56, cx + 150, cy + 56), fill=PALE, outline=OLIVE, width=3 * S)
    ctext(d, cx, cy - 38, "Ökodesign denkt", f(FB, 22), INK); ctext(d, cx, cy - 12, "alle Abschnitte", f(FB, 22), INK); ctext(d, cx, cy + 14, "schon beim Entwurf mit", f(FR, 20), INK)
    save(im, IMG + "lebenszyklus.png")


# ------------------------------------------------------------ Vier Schritte einer Ökobilanz
def schritte():
    im, d = canvas(900, 470)
    ctext(d, 450, 12, "Vier Schritte einer Ökobilanz", f(FB, 30), INK)
    items = [("1 Ziel und Rahmen", ["Was entscheiden wir?", "Welche Leistung?", "Welche Grenzen?"], TEAL),
             ("2 Sachbilanz", ["Mengen zählen:", "was hinein-", "und herausgeht"], OLIVE),
             ("3 Wirkungsabschätzung", ["Welche Umwelt-", "wirkungen –", "wie stark?"], ORANGE),
             ("4 Auswertung", ["Was ist belastbar?", "Was ändert das", "Ergebnis?"], GREEN)]
    w, gap, y = 205, 16, 80
    x0 = (900 - 4 * w - 3 * gap) / 2
    for k, (t, z, col) in enumerate(items):
        x = x0 + k * (w + gap)
        d.rounded_rectangle(P(x, y, x + w, y + 210), radius=16 * S, fill=WHITE, outline=col, width=4 * S)
        d.rounded_rectangle(P(x, y, x + w, y + 46), radius=16 * S, fill=col); d.rectangle(P(x, y + 30, x + w, y + 46), fill=col)
        ctext(d, x + w / 2, y + 10, t, fit(d, t, FB, 22, w - 14), WHITE)
        for j, s in enumerate(z): ctext(d, x + w / 2, y + 62 + j * 30, s, fit(d, s, FR, 21, w - 14), INK)
        if k < 3: arrow(d, x + w + 2, y + 105, x + w + gap - 2, y + 105, GREY, 4, 12)
    # Rückpfeil: mehrfach durchlaufen
    yb = y + 250
    d.line(P(x0 + 3 * (w + gap) + w / 2, y + 212, x0 + 3 * (w + gap) + w / 2, yb), fill=RED, width=4 * S)
    d.line(P(x0 + 3 * (w + gap) + w / 2, yb, x0 + w / 2, yb), fill=RED, width=4 * S)
    arrow(d, x0 + w / 2, yb, x0 + w / 2, y + 214, RED, 4, 16)
    ctext(d, 450, yb + 10, "Die Schritte gehören zusammen und werden oft mehrmals durchlaufen.", f(FB, 21), RED)
    ctext(d, 450, yb + 50, "Lebenszyklus = was untersucht wird · vier Schritte = wie untersucht wird", f(FR, 21), MUTED)
    save(im, IMG + "schritte.png")


# ------------------------------------------------------------ Ein Produkt – viele Umweltwirkungen
def wirkungen():
    im, d = canvas(900, 520)
    ctext(d, 450, 12, "Eine Zahl für das Klima – und die anderen Fragen?", f(FB, 30), INK)
    d.rounded_rectangle(P(330, 196, 570, 312), radius=16 * S, fill=PALE, outline=OLIVE, width=4 * S)
    ctext(d, 450, 206, "Sachbilanz", f(FB, 26), INK); ctext(d, 450, 244, "Material, Energie,", f(FR, 21), INK); ctext(d, 450, 270, "Emissionen", f(FR, 21), INK)
    boxes = [(40, 70, "Klimawirkung", ["kg CO₂-Äquivalente", "← unsere Rechnung"], RED, True),
             (340, 70, "Wasser", ["Verbrauch, Knappheit"], TEAL, False),
             (640, 70, "Ressourcen", ["Rohstoffe, Energieträger"], OLIVE, False),
             (40, 360, "Versauerung", ["Boden, Gewässer"], ORANGE, False),
             (340, 360, "Überdüngung", ["Gewässer"], GREEN, False),
             (640, 360, "Giftige Stoffe", ["Mensch, Umwelt"], MUTED, False)]
    for x, y, t, z, col, fett in boxes:
        w, h = 220, 104
        d.rounded_rectangle(P(x, y, x + w, y + h), radius=14 * S, fill=WHITE, outline=col, width=(6 if fett else 3) * S)
        ctext(d, x + w / 2, y + 12, t, f(FB, 24), col)
        for k, s in enumerate(z): ctext(d, x + w / 2, y + 48 + k * 26, s, f(FB if (fett and k == 1) else FR, 20), INK)
        tx, ty = x + w / 2, (y + h if y < 200 else y)
        sx, sy = 450 + (tx - 450) * 0.35, (196 if y < 200 else 312)
        arrow(d, sx, sy, tx + (sx - tx) * 0.05, ty + (8 if y < 200 else -8), col if fett else GREY, 4 if fett else 3, 14)
    ctext(d, 450, 480, "Jede Wirkung hat ihre eigene Einheit – man darf sie nicht einfach zusammenzählen.", f(FR, 20), MUTED)
    save(im, IMG + "wirkungen.png")


if __name__ == "__main__":
    flaschen(); lebenszyklus(); schritte(); wirkungen()
    for p in sorted(os.listdir(IMG)):
        print(p, os.path.getsize(IMG + p) // 1024, "KB")
