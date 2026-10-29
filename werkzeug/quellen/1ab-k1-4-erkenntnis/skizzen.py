"""Bilder, Animationen, Versuchsskizzen und neue Icons für NAWI 1AB K1.4 Erkenntnisgewinn – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k1-4-erkenntnis/skizzen.py
Schreibt 1ab-nawi/k1-4-erkenntnis/img/*.png|gif, vs-img/d_v1–v4.png, vs-img/i_*.png und neue Icons nach werkzeug/icons/.
Alle Zahlen in den Grafiken stimmen mit inhalt.py überein (Aufgabe 8, Vorjahresdaten)."""
import math, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, "1ab-nawi/k1-4-erkenntnis/")
IMG, VSI, ICONS = UNIT + "img/", UNIT + "vs-img/", os.path.join(ROOT, "werkzeug/icons/")
for p in (IMG, VSI): os.makedirs(p, exist_ok=True)
FR = "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"  # volle Schrift (√, ≈) – die PDF-Teilmenge in werkzeug/schriften hat diese Zeichen nicht
FB = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
BG, WHITE, INK, RED, GREY = (242, 243, 238), (255, 255, 255), (59, 74, 47), (204, 0, 30), (122, 132, 145)
OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = (59, 74, 47), (127, 168, 58), (217, 119, 43), (46, 125, 140), (140, 59, 46), (94, 102, 82)
LIGHT, GRID, YELLOW, BRASS = (223, 229, 208), (214, 220, 204), (240, 200, 40), (200, 160, 70)
S = 2
f = lambda p, s: ImageFont.truetype(p, int(s * S))


def canvas(w=900, h=629, bg=BG):
    im = Image.new("RGB", (w * S, h * S), bg); return im, ImageDraw.Draw(im)


def ctext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w / 2, y * S), t, font=font, fill=fill)


def ltext(d, x, y, t, font, fill):
    d.text((x * S, y * S), t, font=font, fill=fill)


def rtext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w, y * S), t, font=font, fill=fill)


def P(*xy):
    return [v * S for v in xy]


def save(im, path, w=None, h=None, q=128):
    w = w or im.width // S; h = h or im.height // S
    im.resize((w, h), Image.LANCZOS).quantize(colors=q).save(path, optimize=True)


def arrow(d, x0, y0, x1, y1, col=INK, w=5, head=16):
    d.line(P(x0, y0, x1, y1), fill=col, width=int(w * S))
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1, y1), (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45)), (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))]
    d.polygon([(px * S, py * S) for px, py in pts], fill=col)


def darrow(d, x0, y0, x1, y1, col=INK, w=4, head=14):
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    arrow(d, mx, my, x0, y0, col, w, head); arrow(d, mx, my, x1, y1, col, w, head)


def dashed(d, x0, y0, x1, y1, col=GREY, w=2, dash=10):
    L = math.hypot(x1 - x0, y1 - y0); n = max(1, int(L / dash))
    for k in range(0, n, 2):
        a, b = k / n, min(1, (k + 1) / n)
        d.line(P(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a, x0 + (x1 - x0) * b, y0 + (y1 - y0) * b), fill=col, width=int(w * S))


def poly(d, pts, col, w=5):
    d.line([(x * S, y * S) for x, y in pts], fill=col, width=int(w * S), joint="curve")


def frame_of(im, W, H, colors=96):
    W, H, colors = int(W * 0.8), int(H * 0.8), min(colors, 32)
    return im.resize((W, H), Image.LANCZOS).quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


def save_gif(frames, path, dur):
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=dur, loop=0, optimize=True)


# ============================================================ Diagramm-Helfer
class Plot:
    """Achsenkreuz mit Gitter: Datenkoordinaten → Bildpunkte."""
    def __init__(self, d, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.d, self.x0, self.y0, self.w, self.h = d, x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def X(self, x): return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w
    def Y(self, y): return self.y0 + (self.ymax - y) / (self.ymax - self.ymin) * self.h

    def grid(self, dx, dy, xlab=None, ylab=None, xfmt=None, yfmt=None, size=20, xunten=False):
        d = self.d
        x = self.xmin
        while x <= self.xmax + 1e-9:
            d.line(P(self.X(x), self.y0, self.X(x), self.y0 + self.h), fill=GRID, width=S)
            if xfmt: ctext(d, self.X(x), self.Y(0) + 6 if self.ymin < 0 and not xunten else self.y0 + self.h + 6, xfmt(x), f(FR, size), MUTED)
            x += dx
        y = self.ymin
        while y <= self.ymax + 1e-9:
            d.line(P(self.x0, self.Y(y), self.x0 + self.w, self.Y(y)), fill=GRID, width=S)
            if yfmt: rtext(d, self.x0 - 8, self.Y(y) - 12, yfmt(y), f(FR, size), MUTED)
            y += dy
        y_ax = self.Y(0) if self.ymin < 0 < self.ymax else self.y0 + self.h
        arrow(d, self.x0, y_ax, self.x0 + self.w + 24, y_ax, INK, 3, 14)
        arrow(d, self.x0, self.y0 + self.h, self.x0, self.y0 - 20, INK, 3, 14)
        if xlab: rtext(d, self.x0 + self.w + 24, (self.y0 + self.h + 6) if xunten else (y_ax + 30 if self.ymin < 0 else y_ax + 34), xlab, f(FB, size + 2), INK)
        if ylab: ltext(d, self.x0 + 10, self.y0 - 30, ylab, f(FB, size + 2), INK)

    def curve(self, fn, x_from, x_to, col=RED, w=5, n=300):
        poly(self.d, [(self.X(x_from + (x_to - x_from) * i / n), self.Y(fn(x_from + (x_to - x_from) * i / n))) for i in range(n + 1)], col, w)


# ============================================================ Theorie-Bilder K1.4
import random


def flieger_shape(d, cx, cy, sc=1.0, klammer=True, lab=True):
    """Planarflieger schräg von vorne: breiter Flügel, dicke Vorderkante, Rumpf (Kiel) darunter, Büroklammer vorne unten am Kiel."""
    def T(x, y): return (cx + x * sc, cy + y * sc)
    # Flügel (leichte Y-Stellung): linke und rechte Fläche
    L = [T(-300, -10), T(-20, 20), T(-60, 110), T(-330, 70)]
    R = [T(300, -10), T(20, 20), T(60, 110), T(330, 70)]
    for poly_ in (L, R):
        d.polygon([(x * S, y * S) for x, y in poly_], fill=WHITE, outline=GREY, width=2 * S)
    # dicke Vorderkante (gerollter Streifen)
    for side in (-1, 1):
        a, b = T(side * 300, -10), T(side * 20, 20)
        d.line(P(a[0], a[1], b[0], b[1]), fill=(225, 228, 220), width=int(16 * sc * S))
        d.line(P(a[0], a[1] - 8 * sc, b[0], b[1] - 8 * sc), fill=GREY, width=2 * S)
    # Kiel (Rumpf) unter der Mitte
    k = [T(-20, 20), T(20, 20), T(10, 160), T(-6, 150)]
    d.polygon([(x * S, y * S) for x, y in k], fill=(236, 238, 232), outline=GREY, width=2 * S)
    if klammer:
        x0, y0 = T(-14, 34)
        d.rounded_rectangle(P(x0, y0, x0 + 30 * sc, y0 + 56 * sc), radius=int(8 * sc * S), outline=(110, 116, 122), width=3 * S)
        d.rounded_rectangle(P(x0 + 6 * sc, y0 + 8 * sc, x0 + 24 * sc, y0 + 44 * sc), radius=int(6 * sc * S), outline=(110, 116, 122), width=2 * S)
        if lab:
            arrow(d, x0 + 160 * sc, y0 + 100 * sc, x0 + 36 * sc, y0 + 34 * sc, RED, 4, 16)
            ltext(d, x0 + 166 * sc, y0 + 92 * sc, "Büroklammer vorne", f(FB, 22), RED)
            ltext(d, x0 + 166 * sc, y0 + 118 * sc, "unten am Rumpf", f(FB, 22), RED)


def flieger():
    im, d = canvas(900, 560)
    ctext(d, 450, 16, "A: ohne Klammer   ·   B: derselbe Flieger mit Klammer", f(FB, 30), INK)
    flieger_shape(d, 450, 210, 1.15)
    ltext(d, 40, 140, "dicke Vorderkante", f(FB, 22), TEAL); arrow(d, 150, 172, 230, 205, TEAL, 3, 12)
    ltext(d, 650, 120, "Flügel leicht nach oben (Y)", f(FB, 22), TEAL)
    ctext(d, 450, 500, "Nur EINE Änderung: Klammer ab oder dran", f(FB, 28), INK)
    save(im, IMG + "flieger.png")


def beob_exp():
    im, d = canvas(900, 520)
    for x0, tit, col in ((20, "Beobachtung", TEAL), (465, "Experiment", ORANGE)):
        d.rounded_rectangle(P(x0, 20, x0 + 415, 500), radius=18 * S, fill=WHITE, outline=col, width=4 * S)
        ctext(d, x0 + 207, 34, tit, f(FB, 32), col)
    # links: Baum mit Wildtierkamera, Reh
    d.rectangle(P(70, 170, 92, 400), fill=(140, 105, 70)); d.ellipse(P(30, 90, 135, 200), fill=GREEN)
    d.rounded_rectangle(P(92, 250, 140, 300), radius=8 * S, fill=(80, 90, 70), outline=GREY, width=2 * S); d.ellipse(P(108, 264, 126, 282), fill=(30, 30, 30))
    for k in range(3): dashed(d, 140, 275, 300, 230 + k * 45, ORANGE, 2, 8)
    d.ellipse(P(285, 290, 380, 340), fill=(170, 120, 75)); d.rectangle(P(295, 335, 303, 395), fill=(150, 105, 65)); d.rectangle(P(360, 335, 368, 395), fill=(150, 105, 65))
    d.ellipse(P(345, 255, 390, 290), fill=(170, 120, 75)); d.line(P(375, 258, 385, 235), fill=(120, 85, 50), width=3 * S)
    ctext(d, 227, 420, "zuschauen und messen –", f(FB, 24), INK); ctext(d, 227, 450, "nicht eingreifen", f(FB, 24), INK)
    # rechts: Flieger + Hand fügt Klammer hinzu, Bandmaß
    flieger_shape(d, 690, 150, 0.55, True, False)
    d.ellipse(P(560, 200, 620, 240), fill=(230, 190, 160)); ctext(d, 590, 245, "Klammer dran", f(FB, 20), ORANGE)
    d.rectangle(P(500, 340, 860, 356), fill=(250, 235, 160), outline=GREY, width=2 * S)
    for x in range(510, 860, 18): d.line(P(x, 340, x, 348), fill=GREY, width=S)
    ctext(d, 680, 364, "Weite messen", f(FB, 20), INK)
    ctext(d, 672, 420, "eine Bedingung gezielt", f(FB, 24), INK); ctext(d, 672, 450, "verändern und messen", f(FB, 24), INK)
    save(im, IMG + "beob_exp.png")


def theorie():
    im, d = canvas(900, 560)
    ctext(d, 450, 14, "Keine Leiter – zwei Säulen auf vielen Beobachtungen", f(FB, 30), INK)
    # Fundament aus Beobachtungen
    for k in range(9):
        x = 60 + k * 88
        d.rounded_rectangle(P(x, 440, x + 80, 500), radius=8 * S, fill=LIGHT, outline=GREY, width=2 * S)
    ctext(d, 450, 510, "viele geprüfte Beobachtungen und Messungen", f(FB, 24), MUTED)
    for x0, tit, sub, col in ((120, "Gesetz", ["beschreibt: WAS passiert", "regelmäßig, unter", "bestimmten Bedingungen"], TEAL),
                              (500, "Theorie", ["erklärt: WARUM", "verbindet viele Befunde,", "erlaubt Vorhersagen"], OLIVE)):
        d.rounded_rectangle(P(x0, 120, x0 + 280, 430), radius=16 * S, fill=col)
        ctext(d, x0 + 140, 140, tit, f(FB, 36), WHITE)
        for i, t in enumerate(sub): ctext(d, x0 + 140, 210 + i * 36, t, f(FR, 24), WHITE)
    # durchgestrichene Leiter
    lx = 432
    for x in (lx - 18, lx + 18): d.line(P(x, 150, x, 300), fill=GREY, width=4 * S)
    for y in range(165, 300, 28): d.line(P(lx - 18, y, lx + 18, y), fill=GREY, width=3 * S)
    d.line(P(lx - 34, 140, lx + 34, 310), fill=RED, width=6 * S); d.line(P(lx + 34, 140, lx - 34, 310), fill=RED, width=6 * S)
    ctext(d, 450, 330, "keine", f(FB, 22), RED); ctext(d, 450, 354, "Stufen", f(FB, 22), RED)
    ctext(d, 450, 64, "Hypothesen werden an Beobachtungen geprüft – sie stützen oder schwächen Gesetze und Theorien", f(FR, 21), INK)
    save(im, IMG + "theorie.png")


def faltanleitung():
    W, H = 900, 760
    im, d = canvas(W, H)
    ctext(d, 450, 10, "Planarflieger (einfach) – A4 quer", f(FB, 30), INK)
    pw, ph = 230, 150
    pos = [(40, 70), (335, 70), (630, 70), (40, 330), (335, 330), (630, 330)]
    txt = ["1 · halbieren, öffnen", "2 · Unterkante zur Mitte", "3 · noch einmal zur Mitte", "4 · Streifen über die Mitte", "5 · senkrecht falten", "6 · Flügel = Rumpfbreite"]
    for n, ((x, y), t) in enumerate(zip(pos, txt)):
        ctext(d, x + pw / 2, y - 6, t, f(FB, 22), INK)
        if n < 4:
            d.rectangle(P(x, y + 24, x + pw, y + 24 + ph), fill=WHITE, outline=GREY, width=2 * S)
            mid = y + 24 + ph / 2
            dashed(d, x, mid, x + pw, mid, GREY, 2, 8)
            if n >= 1:
                band = {1: ph / 4, 2: ph / 4, 3: ph / 4}[n]
                d.rectangle(P(x, y + 24 + ph - band * (1 if n == 1 else 0.5) - (0 if n == 1 else 0), x + pw, y + 24 + ph), fill=(232, 236, 225), outline=GREY, width=S)
            if n == 0: arrow(d, x + pw / 2, y + 24 + ph - 10, x + pw / 2, y + 24 + 18, ORANGE, 4, 14)
            if n == 1: arrow(d, x + pw / 2 + 50, y + 24 + ph - 6, x + pw / 2 + 50, mid + 8, ORANGE, 4, 14)
            if n == 2: arrow(d, x + pw / 2 + 50, y + 24 + ph - 6, x + pw / 2 + 50, mid + 8, ORANGE, 4, 14)
            if n == 3:
                d.rectangle(P(x, mid - 2, x + pw, mid + 26), fill=(205, 212, 195), outline=GREY, width=S)
                arrow(d, x + pw / 2 + 50, mid + 40, x + pw / 2 + 50, mid - 20, ORANGE, 4, 14)
        elif n == 4:
            d.rectangle(P(x, y + 24, x + pw, y + 24 + ph), fill=WHITE, outline=GREY, width=2 * S)
            d.rectangle(P(x, y + 24 + ph - 30, x + pw, y + 24 + ph), fill=(205, 212, 195), outline=GREY, width=S)
            dashed(d, x + pw / 2, y + 24, x + pw / 2, y + 24 + ph, ORANGE, 3, 8)
            d.arc(P(x + 20, y + 40, x + pw / 2 - 6, y + 120), 200, 340, fill=ORANGE, width=3 * S)
            d.arc(P(x + pw / 2 + 6, y + 40, x + pw - 20, y + 120), 200, 340, fill=ORANGE, width=3 * S)
            ctext(d, x + pw / 2, y + 24 + ph + 6, "Vorderkante außen", f(FR, 20), MUTED)
        else:
            # Ansicht von vorne: flaches Y
            cx, cy = x + pw / 2, y + 100
            poly(d, [(cx - 110, cy - 22), (cx, cy), (cx + 110, cy - 22)], INK, 5)
            d.line(P(cx, cy, cx, cy + 70), fill=INK, width=5 * S)
            ctext(d, cx, cy + 82, "von vorne: flaches Y", f(FR, 20), MUTED)
    # Klammer-Detail
    y = 600
    d.rounded_rectangle(P(40, y, 860, y + 140), radius=14 * S, fill=WHITE, outline=RED, width=3 * S)
    flieger_shape(d, 210, y + 10, 0.36, True, False)
    ltext(d, 420, y + 22, "Für B: Klammer vorne unten am Rumpf,", f(FB, 24), RED)
    ltext(d, 420, y + 54, "direkt hinter der Vorderkante.", f(FB, 24), RED)
    ltext(d, 420, y + 92, "Bei allen Gruppen an derselben Stelle.", f(FR, 22), INK)
    save(im, IMG + "faltanleitung.png")


def messbahn(path=None, titel="Messbahn im Eingangsbereich"):
    im, d = canvas(900, 600)
    ctext(d, 450, 12, titel, f(FB, 30), INK)
    # Seitenansicht
    ltext(d, 30, 60, "von der Seite", f(FB, 22), MUTED)
    d.rectangle(P(30, 92, 870, 104), fill=(190, 196, 202)); ltext(d, 640, 108, "niedrige Decke", f(FB, 20), RED)
    d.rectangle(P(30, 300, 870, 308), fill=(170, 160, 140))
    # Werfer
    d.ellipse(P(60, 150, 100, 190), fill=TEAL); d.rounded_rectangle(P(58, 190, 102, 300), radius=10 * S, fill=TEAL)
    d.line(P(100, 230, 140, 240), fill=TEAL, width=8 * S)
    dashed(d, 30, 240, 160, 240, ORANGE, 2, 6); ltext(d, 150, 214, "Hüfthöhe", f(FB, 20), ORANGE)
    # Flugbahn flach
    pts = [(145 + t * 6.2, 240 + 0.00055 * (t * 6.2) ** 2 * 0.9 + t * 0.12) for t in range(0, 110)]
    poly(d, [(x, min(y, 300)) for x, y in pts], GREEN, 4)
    xl = 145 + 110 * 6.2
    d.ellipse(P(800 - 10, 290, 800 + 10, 310), fill=RED); ctext(d, 790, 316, "1. Bodenkontakt", f(FB, 20), RED)
    d.line(P(130, 300, 130, 330), fill=INK, width=4 * S); ctext(d, 130, 334, "Abwurflinie", f(FB, 20), INK)
    ctext(d, 450, 150, "flach und ruhig – kein hoher Bogen", f(FB, 24), GREEN)
    # Draufsicht
    ltext(d, 30, 380, "von oben", f(FB, 22), MUTED)
    d.rectangle(P(30, 410, 870, 540), fill=WHITE, outline=GREY, width=2 * S)
    d.line(P(130, 410, 130, 540), fill=INK, width=4 * S)
    d.rectangle(P(130, 520, 860, 532), fill=(250, 235, 160), outline=GREY, width=S)
    for x in range(140, 860, 30): d.line(P(x, 520, x, 526), fill=GREY, width=S)
    ltext(d, 600, 494, "Bandmaß 20 m am Rand", f(FB, 20), INK)
    arrow(d, 150, 460, 800, 460, GREEN, 4, 16); ltext(d, 160, 424, "Flugrichtung – Bahn frei, niemand davor", f(FB, 20), GREEN)
    ctext(d, 450, 556, "Werfer und Wartende hinter der Linie · Eingang und Fluchtweg frei", f(FB, 22), RED)
    save(im, path or (IMG + "messbahn.png"))


def landung_gif():
    W, H = 900, 400
    frames = []
    xs = list(range(60, 920, 26))
    contact = None
    for k, x in enumerate(xs):
        im, d = canvas(W, H)
        ctext(d, 450, 12, "Gemessen wird der ERSTE Bodenkontakt", f(FB, 30), INK)
        d.rectangle(P(0, 320, 900, 330), fill=(170, 160, 140))
        d.line(P(70, 300, 70, 340), fill=INK, width=4 * S); ctext(d, 70, 344, "Linie", f(FB, 20), INK)
        if x < 600:
            y = 140 + (x - 60) * 0.33
        else:
            y = 318
            if contact is None: contact = 600
        if contact:
            d.ellipse(P(contact - 9, 309, contact + 9, 327), fill=RED)
            arrow(d, 70, 290, contact, 290, RED, 4, 16); ctext(d, (70 + contact) / 2, 254, "diese Weite", f(FB, 24), RED)
        xx = min(x, 800)
        d.polygon(P(xx - 40, y - 4, xx + 30, y, xx - 40, y + 8), fill=WHITE, outline=GREY)
        if x >= 600: ctext(d, 760, 350, "rutscht weiter – zählt nicht", f(FR, 20), MUTED)
        frames.append(frame_of(im, W, H))
    for _ in range(12): frames.append(frames[-1])
    save_gif(frames, IMG + "landung.gif", 90)


def kreislauf():
    im, d = canvas(900, 640)
    ctext(d, 450, 10, "Forschung ist ein Kreislauf", f(FB, 30), INK)
    cx, cy, r, ry = 450, 330, 300, 225
    steps = ["Frage stellen", "Informationen suchen", "Vermutung aufstellen", "Untersuchung planen", "Untersuchung durchführen", "Daten sammeln", "Modelle, Gesetze entwerfen", "Ergebnisse vorstellen"]
    cols = [TEAL, TEAL, ORANGE, ORANGE, GREEN, GREEN, OLIVE, OLIVE]
    pts = []
    for i, t in enumerate(steps):
        a = -math.pi / 2 + i * 2 * math.pi / 8
        x, y = cx + r * math.cos(a), cy + ry * math.sin(a)
        pts.append((x, y))
    for i in range(8):
        a0 = -math.pi / 2 + i * 2 * math.pi / 8 + 0.30; a1 = a0 + 2 * math.pi / 8 - 0.60
        pa = (cx + r * math.cos(a0), cy + ry * math.sin(a0)); pb = (cx + r * math.cos(a1), cy + ry * math.sin(a1))
        arrow(d, pa[0], pa[1], pb[0], pb[1], GREY, 4, 14)
    for i, ((x, y), t) in enumerate(zip(pts, steps)):
        w = d.textlength(t, font=f(FB, 21)) / S + 24
        d.rounded_rectangle(P(x - w / 2, y - 22, x + w / 2, y + 22), radius=12 * S, fill=cols[i])
        ctext(d, x, y - 13, t, f(FB, 21), WHITE)
    # Rückpfeile innen
    y5 = pts[5][1] - 60
    arrow(d, pts[5][0] + 30, y5, pts[3][0] - 30, y5, RED, 4, 16)
    ctext(d, cx, y5 - 58, "passt nicht?", f(FB, 22), RED); ctext(d, cx, y5 - 32, "zurück und ändern", f(FB, 22), RED)
    arrow(d, pts[7][0] + 40, pts[7][1] + 40, pts[0][0] - 20, pts[0][1] + 40, RED, 4, 16)
    ctext(d, cx - 60, pts[7][1] + 70, "neue Fragen", f(FB, 22), RED)
    save(im, IMG + "kreislauf.png")


VORJ = [(1, "1,80", "10,85", "6,35", "5,78"), (2, "5,10", "5,20", "6,70", "4,23"), (3, "15,31", "4,77", "3,63", "10,18"), (4, "1,97", "9,33", "2,73", "9,14"),
        (5, "5,00", "Ung.", "5,94", "10,46"), (6, "3,50", "6,55", "6,79", "4,80"), (7, "4,10", "6,82", "4,83", "7,90")]


def vorjahr():
    im, d = canvas(900, 560)
    ctext(d, 450, 10, "Flugweiten in m aus einem früheren Jahr – je ein Wurf", f(FB, 28), INK)
    heads = ["Gruppe", "alte 1BK kurz", "alte 1BK lang", "alte 1AK kurz", "alte 1AK lang"]
    xs = [40, 190, 365, 540, 715, 860]
    y = 60
    for c, h in enumerate(heads):
        d.rectangle(P(xs[c], y, xs[c + 1], y + 52), fill=OLIVE, outline=WHITE, width=2 * S); ctext(d, (xs[c] + xs[c + 1]) / 2, y + 14, h, f(FB, 22), WHITE)
    for r, row in enumerate(VORJ):
        yy = y + 52 + r * 56
        for c, v in enumerate(row):
            d.rectangle(P(xs[c], yy, xs[c + 1], yy + 56), fill=LIGHT if r % 2 else WHITE, outline=GRID, width=2 * S)
            ctext(d, (xs[c] + xs[c + 1]) / 2, yy + 14, str(v), f(FB if c == 0 else FR, 26), RED if v == "Ung." else INK)
    ctext(d, 450, 520, "»Ung.« = ungültig, Ursache nicht dokumentiert · Quelle: bisherige Unterrichts-PPP", f(FR, 20), MUTED)
    save(im, IMG + "vorjahr.png")


A_W, B_W = [5.1, 6.0, 5.4], [5.9, 5.0, 6.8]  # bewusst NICHT die Zahlen von Aufgabe 8 (sonst stünde die Lösung im Bild)


def mittelwert():
    im, d = canvas(900, 520)
    ctext(d, 450, 10, "Übungsdaten: drei Würfe je Zustand", f(FB, 28), INK)
    p = Plot(d, 150, 80, 680, 320, 4.0, 7.0, 0, 3)
    x = 4.0
    while x <= 7.0 + 1e-9:
        d.line(P(p.X(x), 80, p.X(x), 400), fill=GRID, width=S); ctext(d, p.X(x), 410, ("%.1f" % x).replace(".", ","), f(FR, 22), MUTED); x += 0.5
    ltext(d, 700, 440, "Weite in m", f(FB, 22), INK)
    for row, (lab, vals, col) in enumerate((("A ohne Klammer", A_W, TEAL), ("B mit Klammer", B_W, ORANGE))):
        y = 160 + row * 150
        rtext(d, 140, y - 14, lab.split(" ")[0], f(FB, 30), col); rtext(d, 140, y + 18, " ".join(lab.split(" ")[1:]), f(FR, 18), col)
        lo, hi = min(vals), max(vals)
        d.rectangle(P(p.X(lo), y + 26, p.X(hi), y + 34), fill=col)
        ctext(d, (p.X(lo) + p.X(hi)) / 2, y + 40, "Spannweite " + ("%.1f" % (hi - lo)).replace(".", ",") + " m", f(FR, 20), col)
        for v in vals: d.ellipse(P(p.X(v) - 11, y - 11, p.X(v) + 11, y + 11), fill=col, outline=WHITE, width=2 * S)
        m = sum(vals) / 3
        d.line(P(p.X(m), y - 40, p.X(m), y + 22), fill=RED, width=4 * S); ctext(d, p.X(m), y - 70, "Mittelwert " + ("%.1f" % m).replace(".", ",") + " m", f(FB, 20), RED)
    save(im, IMG + "mittelwert.png")


def zyklus():
    im, d = canvas(900, 600)
    ctext(d, 450, 10, "Konstruktionszyklus", f(FB, 30), INK)
    steps = ["1 Problem analysieren", "2 Entwerfen", "3 Konstruieren", "4 Testen", "5 Bewerten", "6 Verbessern"]
    cx, cy, rx, ry = 450, 320, 300, 200
    pts = [(cx + rx * math.cos(-math.pi / 2 + i * math.pi / 3), cy + ry * math.sin(-math.pi / 2 + i * math.pi / 3)) for i in range(6)]
    for i in range(6):
        a0 = -math.pi / 2 + i * math.pi / 3 + 0.3; a1 = a0 + math.pi / 3 - 0.6
        arrow(d, cx + rx * math.cos(a0), cy + ry * math.sin(a0), cx + rx * math.cos(a1), cy + ry * math.sin(a1), GREY, 4, 14)
    for i, ((x, y), t) in enumerate(zip(pts, steps)):
        w = d.textlength(t, font=f(FB, 24)) / S + 28
        d.rounded_rectangle(P(x - w / 2, y - 26, x + w / 2, y + 26), radius=12 * S, fill=OLIVE if i < 3 else TEAL)
        ctext(d, x, y - 15, t, f(FB, 24), WHITE)
    ctext(d, cx, cy - 14, "Prototyp", f(FB, 30), MUTED)
    ctext(d, cx, cy + 22, "mehrmals durchlaufen", f(FR, 22), MUTED)
    save(im, IMG + "zyklus.png")


def zielscheiben():
    im, d = canvas(900, 420)
    rnd = random.Random(4)
    cents = [(160, 220), (450, 220), (740, 220)]
    shots = [[(rnd.gauss(0, 48), rnd.gauss(0, 48)) for _ in range(6)], [(52 + rnd.gauss(0, 10), -48 + rnd.gauss(0, 10)) for _ in range(6)], [(rnd.gauss(0, 10), rnd.gauss(0, 10)) for _ in range(6)]]
    for n, ((cx, cy), sh) in enumerate(zip(cents, shots)):
        for rr, c in ((130, WHITE), (100, LIGHT), (70, WHITE), (40, LIGHT), (14, RED)):
            d.ellipse(P(cx - rr, cy - rr, cx + rr, cy + rr), fill=c, outline=GREY, width=2 * S)
        for dx, dy in sh:
            d.ellipse(P(cx + dx - 9, cy + dy - 9, cx + dx + 9, cy + dy + 9), fill=INK, outline=WHITE, width=S)
        ctext(d, cx, 370, f"Scheibe {n + 1}", f(FB, 28), INK)
    ctext(d, 450, 20, "Je 6 Schuss – drei verschiedene Bilder", f(FB, 28), INK)
    save(im, IMG + "zielscheiben.png")


def v1():
    messbahn(VSI + "d_v1.png", I.VS_ID + " · Aufbau im Eingangsbereich")


# ============================================================ neue Icons (180 × 108, transparent)
def icon(name, draw):
    ic = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ic)
    draw(d); ic = ic.resize((180, 108), Image.LANCZOS)
    ic.save(ICONS + name + ".png", optimize=True)


OUT = (110, 115, 120)


def new_icons():
    def papier(d):
        for k, c in ((2, (236, 238, 232)), (1, (246, 247, 243)), (0, WHITE)):
            d.rectangle(P(56 - k * 6, 14 + k * 6, 124 - k * 6, 100 + k * 6 - 12), fill=c, outline=OUT, width=2 * S)
        for y in range(30, 80, 10): d.line(P(64, y, 116, y), fill=(200, 205, 196), width=S)
        ctext(d, 90, 78, "A4", f(FB, 16), (122, 132, 145))
    if not os.path.exists(ICONS + "papier.png"): icon("papier", papier)


def icons_kopieren():
    sys.path.insert(0, HERE)
    from versuche_daten import VS
    used = {m[1] for v in VS for m in v["mat"]}
    for n in used:
        src = ICONS + n + ".png"
        assert os.path.exists(src), "Icon fehlt: " + n
        shutil.copy(src, VSI + "i_" + n + ".png")
    return used


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    import inhalt as I
    flieger(); beob_exp(); theorie(); faltanleitung(); messbahn(); landung_gif(); kreislauf(); vorjahr(); mittelwert(); zyklus(); zielscheiben(); v1()
    new_icons()
    print("Icons:", sorted(icons_kopieren()))
    for p in sorted(os.listdir(IMG)) + ["vs-img/" + x for x in sorted(os.listdir(VSI))]:
        print(p, os.path.getsize((IMG + p) if not p.startswith("vs-img/") else UNIT + p) // 1024, "KB")
