"""Bilder, Animationen, Versuchsskizzen und neue Icons für NAWI 4AB K2.1–2.3 Schwingungen und Wellen – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/4ab-k2-1-wellen/skizzen.py
Schreibt 4ab-nawi/k2-1-wellen/img/*.png|gif, vs-img/d_v1–v4.png, vs-img/i_*.png und neue Icons nach werkzeug/icons/.
Alle Zahlen in den Grafiken sind Modellwerte und stimmen mit inhalt.py überein (A1: A = 3 cm, T = 0,8 s)."""
import math, os, shutil, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, "4ab-nawi/k2-1-wellen/")
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


# ============================================================ Theorie-Bilder
def schaukel():
    im, d = canvas(900, 470)
    ctext(d, 450, 14, "Leicht oder schwer – wer schwingt schneller?", f(FB, 32), INK)
    for cx, mass, lab in ((250, 1, "leichter Kadett"), (650, 1.6, "schwerer Kadett")):
        top = 90
        d.line(P(cx - 150, top, cx + 150, top), fill=INK, width=10 * S)
        for sx in (cx - 150, cx + 150): d.line(P(sx, top, sx + (-40 if sx < cx else 40), 400), fill=INK, width=8 * S)
        ang = math.radians(18); L = 230
        hx, hy = cx + L * math.sin(ang), top + L * math.cos(ang)
        for off in (-22, 22): d.line(P(cx + off, top, hx + off, hy), fill=GREY, width=3 * S)
        d.rounded_rectangle(P(hx - 40, hy, hx + 40, hy + 14), radius=5 * S, fill=RUST)
        r = 20 * mass ** 0.5
        d.ellipse(P(hx - r, hy - 2 * r - 30, hx + r, hy - 30), fill=TEAL)
        d.rounded_rectangle(P(hx - r * 0.9, hy - 32, hx + r * 0.9, hy + 2), radius=6 * S, fill=TEAL)
        d.arc(P(cx - L - 10, top - L - 10, cx + L + 10, top + L + 10), 70, 110, fill=ORANGE, width=4 * S)
        ctext(d, cx, 420, lab, f(FB, 26), INK)
    ctext(d, 450, 220, "?", f(FB, 70), RED)
    save(im, IMG + "schaukel.png")


def g1_schwingung():
    im, d = canvas(900, 470, WHITE)
    pl = Plot(d, 100, 50, 720, 320, 0, 2, -5, 5)
    pl.grid(0.25, 1, "t in s", "y in cm", size=24, xfmt=lambda x: ("%.2f" % x).replace(".", ",").rstrip("0").rstrip(",") if abs(x * 4 - round(x * 4)) < 1e-9 else "",
            yfmt=lambda y: ("%+d" % y if y else "0") if y % 2 == 0 else "")
    pl.curve(lambda t: 4 * math.sin(2 * math.pi * t), 0, 2, RED, 5)
    # Amplitude
    darrow(d, pl.X(0.25) + 30, pl.Y(0), pl.X(0.25) + 30, pl.Y(4), TEAL, 4)
    ltext(d, pl.X(0.25) + 40, pl.Y(2.2), "A = 4 cm", f(FB, 28), TEAL)
    # Periodendauer zwischen zwei Maxima
    dashed(d, pl.X(0.75), pl.Y(-4), pl.X(0.75), pl.Y(-4) + 40, ORANGE, 3); dashed(d, pl.X(1.75), pl.Y(-4), pl.X(1.75), pl.Y(-4) + 40, ORANGE, 3)
    darrow(d, pl.X(0.75), pl.Y(-4) + 30, pl.X(1.75), pl.Y(-4) + 30, ORANGE, 4)
    ctext(d, pl.X(1.25), pl.Y(-4) + 36, "T = 1,0 s", f(FB, 28), ORANGE)
    ctext(d, 450, 436, "harmonische Schwingung · f = 1/T = 1,0 Hz", f(FB, 26), MUTED)
    save(im, IMG + "g1_schwingung.png")


def a1_diagramm():
    """Diagramm für Aufgabe 1: A = 3 cm, T = 0,8 s (nichts eingezeichnet – selbst ablesen). Große Schrift fürs Handy."""
    im, d = canvas(720, 500, WHITE)
    pl = Plot(d, 80, 50, 590, 360, 0, 2.4, -4, 4)
    pl.grid(0.2, 1, "t in s", "y in cm", xfmt=lambda x: ("%.1f" % x).replace(".", ",") if round(x * 5) % 2 == 0 and x < 2.3 else "",
            yfmt=lambda y: ("%+d" % y if y else "0"), size=26, xunten=True)
    pl.curve(lambda t: 3 * math.sin(2 * math.pi * t / 0.8), 0, 2.4, TEAL, 6)
    ctext(d, 360, 462, "Gitter: 0,2 s und 1 cm", f(FB, 26), MUTED)
    save(im, IMG + "a1_diagramm.png")


def pendel_gif():
    W, H = 900, 520
    frames = []
    cx, top, L = 300, 70, 330
    amp = math.radians(14)
    N = 24
    for i in range(N):
        t = i / N
        a = amp * math.cos(2 * math.pi * t)
        im, d = canvas(W, H, WHITE)
        ctext(d, W / 2, 10, "Fadenpendel: eine volle Schwingung", f(FB, 30), INK)
        d.rectangle(P(cx - 90, top - 14, cx + 90, top), fill=(200, 205, 210))
        dashed(d, cx, top, cx, top + L + 40, GREY, 2)
        for s_ in (-1, 1):
            x2, y2 = cx + L * math.sin(s_ * amp), top + L * math.cos(amp)
            d.ellipse(P(x2 - 22, y2 - 22, x2 + 22, y2 + 22), outline=GRID, width=3 * S)
        bx, by = cx + L * math.sin(a), top + L * math.cos(a)
        d.line(P(cx, top, bx, by), fill=INK, width=3 * S)
        d.ellipse(P(bx - 22, by - 22, bx + 22, by + 22), fill=BRASS, outline=GREY, width=2 * S)
        ctext(d, cx - L * math.sin(amp) - 10, top + L * math.cos(amp) + 34, "Umkehrpunkt", f(FB, 20), RUST)
        ctext(d, cx + L * math.sin(amp) + 10, top + L * math.cos(amp) + 34, "Umkehrpunkt", f(FB, 20), RUST)
        ctext(d, cx, top + L + 46, "Gleichgewichtslage", f(FB, 20), TEAL)
        # Fortschritt der Schwingung
        x0, y0, w = 590, 150, 260
        ltext(d, x0, 90, "Start rechts:", f(FB, 24), INK)
        d.rounded_rectangle(P(x0, y0, x0 + w, y0 + 34), radius=10 * S, outline=GREY, width=2 * S)
        d.rounded_rectangle(P(x0, y0, x0 + max(18, w * t), y0 + 34), radius=10 * S, fill=ORANGE)
        msg = "rechts → links: erst ½ Schwingung" if t < 0.5 else "links → rechts: zurück = 1 volle"
        ltext(d, x0, y0 + 50, msg, f(FR, 22), INK)
        ltext(d, x0, y0 + 90, "Schwingung", f(FR, 22), INK) if t >= 0.5 else None
        ltext(d, x0, y0 + 150, "Gleicher Ort UND gleiche", f(FB, 22), RUST)
        ltext(d, x0, y0 + 178, "Bewegungsrichtung", f(FB, 22), RUST)
        ltext(d, x0, y0 + 206, "= eine Periode T", f(FB, 22), RUST)
        frames.append(frame_of(im, W, H))
    save_gif(frames, IMG + "pendel.gif", [130] * N)


def g_pendel():
    im, d = canvas(900, 520, WHITE)
    # Fadenpendel
    cx, top, L = 220, 70, 300
    d.rectangle(P(cx - 80, top - 14, cx + 80, top), fill=(200, 205, 210))
    a = math.radians(10)
    dashed(d, cx, top, cx, top + L + 20, GREY, 2)
    bx, by = cx + L * math.sin(a), top + L * math.cos(a)
    d.line(P(cx, top, bx, by), fill=INK, width=3 * S)
    d.ellipse(P(bx - 22, by - 22, bx + 22, by + 22), fill=BRASS, outline=GREY, width=2 * S)
    d.ellipse(P(bx - 4, by - 4, bx + 4, by + 4), fill=RED)
    d.arc(P(cx - 80, top - 80, cx + 80, top + 80), 80, 90, fill=ORANGE, width=4 * S)
    ltext(d, cx + 8, top + 86, "höchstens ca. 10°", f(FB, 18), ORANGE)
    darrow(d, cx - 40, top, cx - 40 + 0, top + L * math.cos(a), TEAL, 3)
    ltext(d, cx - 160, top + 140, "Länge l bis", f(FB, 20), TEAL); ltext(d, cx - 160, top + 164, "zum Schwerpunkt", f(FB, 20), TEAL)
    ctext(d, cx, 420, "Fadenpendel", f(FB, 28), INK)
    ctext(d, cx, 456, "T ≈ 2π·√(l / g)", f(FB, 26), RED)
    ctext(d, cx, 488, "Masse egal (im Modell)", f(FR, 22), MUTED)
    # Federpendel
    cx2 = 640
    d.rectangle(P(cx2 - 80, top - 14, cx2 + 80, top), fill=(200, 205, 210))
    pts = [(cx2, top)]
    for k in range(1, 21): pts.append((cx2 + (22 if k % 2 else -22), top + 12 * k))
    pts.append((cx2, top + 12 * 21 + 6))
    poly(d, pts, GREY, 4)
    by2 = top + 12 * 21 + 6
    d.rectangle(P(cx2 - 34, by2, cx2 + 34, by2 + 60), fill=BRASS, outline=GREY, width=2 * S)
    ctext(d, cx2, by2 + 14, "m", f(FB, 28), INK)
    ltext(d, cx2 + 40, top + 110, "Feder mit", f(FB, 20), TEAL); ltext(d, cx2 + 40, top + 134, "Federkonstante k", f(FB, 20), TEAL)
    darrow(d, cx2 + 70, by2 + 4, cx2 + 70, by2 + 60, ORANGE, 3)
    ltext(d, cx2 + 80, by2 + 18, "auf und ab", f(FR, 18), ORANGE)
    ctext(d, cx2, 420, "Federpendel", f(FB, 28), INK)
    ctext(d, cx2, 456, "T = 2π·√(m / k)", f(FB, 26), RED)
    ctext(d, cx2, 488, "mehr Masse → länger", f(FR, 22), MUTED)
    save(im, IMG + "g_pendel.png")


def g2_daempfung():
    im, d = canvas(900, 470, WHITE)
    pl = Plot(d, 90, 70, 740, 300, 0, 6, -5, 5)
    pl.grid(1, 2.5, "t (Zeit)", "Auslenkung", size=20)
    pl.curve(lambda t: 4.5 * math.exp(-0.18 * t) * math.cos(2 * math.pi * t), 0, 6, TEAL, 4)
    pl.curve(lambda t: 4.5 * math.exp(-0.9 * t) * math.cos(2 * math.pi * t), 0, 6, RED, 5)
    ltext(d, 300, 16, "— schwach gedämpft (Pendel in Luft)", f(FB, 20), TEAL)
    ltext(d, 300, 42, "— stark gedämpft (Stoßdämpfer)", f(FB, 20), RED)
    ctext(d, 450, 420, "Schema – keine Messwerte: Dämpfung gibt Energie an die Umgebung ab, die Amplitude sinkt.", f(FR, 20), MUTED)
    save(im, IMG + "g2_daempfung.png")


def g3_resonanz():
    im, d = canvas(900, 470, WHITE)
    pl = Plot(d, 100, 70, 700, 300, 0, 2, 0, 6)
    pl.grid(0.5, 1, None, "Amplitude", size=20)
    rtext(d, 830, 380, "Erregerfrequenz →", f(FB, 22), INK)
    f0 = 1.0
    amp = lambda fe, z: 1 / math.sqrt((1 - (fe / f0) ** 2) ** 2 + (2 * z * fe / f0) ** 2)
    pl.curve(lambda x: min(5.8, amp(x, 0.09)), 0.02, 2, RED, 5)
    pl.curve(lambda x: amp(x, 0.35), 0.02, 2, TEAL, 5)
    dashed(d, pl.X(1), pl.Y(0), pl.X(1), pl.Y(6), ORANGE, 3)
    ctext(d, pl.X(1), pl.Y(0) + 8, "Eigenfrequenz", f(FB, 20), ORANGE)
    ltext(d, pl.X(1.12), pl.Y(5.4), "schwache Dämpfung", f(FB, 20), RED)
    ltext(d, pl.X(1.35), pl.Y(2.4), "starke Dämpfung", f(FB, 20), TEAL)
    ctext(d, 450, 420, "Schema ohne Zahlen: Das Maximum liegt nahe der Eigenfrequenz; Dämpfung begrenzt es.", f(FR, 20), MUTED)
    save(im, IMG + "g3_resonanz.png")


def welle_gif():
    """Oben transversal (Seil), unten longitudinal (Feder/Luft); je ein rot markiertes Teilchen bleibt am Ort."""
    W, H = 900, 560
    frames = []
    N = 20
    lam = 300.0
    for i in range(N):
        t = i / N
        im, d = canvas(W, H, WHITE)
        ctext(d, W / 2, 8, "Die Störung läuft – das markierte Teilchen bleibt am Ort", f(FB, 28), INK)
        # transversal
        ltext(d, 40, 54, "Transversalwelle (z. B. Seil):", f(FB, 22), TEAL)
        y0 = 160
        pts = []
        for k in range(61):
            x = 60 + k * 13
            y = y0 - 45 * math.sin(2 * math.pi * ((x - 60) / lam - t))
            pts.append((x, y))
        for k in range(0, 61, 3):
            x, y = pts[k]; d.ellipse(P(x - 7, y - 7, x + 7, y + 7), fill=(170, 176, 182))
        mk = 30; x, y = pts[mk]; d.ellipse(P(x - 11, y - 11, x + 11, y + 11), fill=RED)
        darrow(d, x + 24, y0 - 45, x + 24, y0 + 45, RED, 3, 12)
        arrow(d, 640, 245, 820, 245, TEAL, 5, 18); ltext(d, 470, 230, "Ausbreitung", f(FB, 22), TEAL)
        ltext(d, x + 34, y0 - 10, "schwingt quer", f(FB, 20), RED)
        # longitudinal
        ltext(d, 40, 290, "Longitudinalwelle (z. B. Schall in Luft):", f(FB, 22), RUST)
        y1 = 400
        for k in range(61):
            x0 = 60 + k * 13
            x = x0 + 18 * math.sin(2 * math.pi * ((x0 - 60) / lam - t))
            col = RED if k == 30 else (170, 176, 182)
            r = 10 if k == 30 else 6
            d.ellipse(P(x - r, y1 - r, x + r, y1 + r), fill=col)
            if k != 30:
                d.ellipse(P(x - r, y1 - 46 - r, x + r, y1 - 46 + r), fill=(200, 205, 210)); d.ellipse(P(x - r, y1 + 46 - r, x + r, y1 + 46 + r), fill=(200, 205, 210))
        x0 = 60 + 30 * 13
        darrow(d, x0 - 26, y1 + 76, x0 + 26, y1 + 76, RED, 3, 12)
        ltext(d, x0 + 36, y1 + 64, "schwingt längs (vor und zurück)", f(FB, 20), RED)
        arrow(d, 640, 520, 820, 520, RUST, 5, 18); ltext(d, 470, 505, "Ausbreitung", f(FB, 22), RUST)
        frames.append(frame_of(im, W, H, 64))
    save_gif(frames, IMG + "welle.gif", [150] * N)


def g4_ort_zeit():
    im, d = canvas(900, 470, WHITE)
    # links: Ortsbild
    pl = Plot(d, 70, 60, 340, 260, 0, 2, -3.6, 3)
    pl.grid(0.5, 1, "x in m", "y (Momentaufnahme)", size=18, xfmt=lambda x: ("%.1f" % x).replace(".", ",") if abs(x * 2 - round(x * 2)) < 1e-9 else "")
    pl.curve(lambda x: 2.4 * math.sin(2 * math.pi * x / 1.0 + math.pi / 2), 0, 2, TEAL, 4)
    darrow(d, pl.X(0.5), pl.Y(-2.4) + 22, pl.X(1.5), pl.Y(-2.4) + 22, ORANGE, 3)
    ctext(d, pl.X(1.0), pl.Y(-2.4) + 28, "Wellenlänge λ", f(FB, 20), ORANGE)
    ctext(d, 240, 400, "Waagrecht: ORT x → hier liest man λ ab", f(FB, 20), TEAL)
    # rechts: Zeitbild
    pr = Plot(d, 520, 60, 340, 260, 0, 2, -3.6, 3)
    pr.grid(0.5, 1, "t in s", "y an einem festen Ort", size=18, xfmt=lambda x: ("%.1f" % x).replace(".", ",") if abs(x * 2 - round(x * 2)) < 1e-9 else "")
    pr.curve(lambda t: 2.4 * math.cos(2 * math.pi * t / 1.0), 0, 2, RED, 4)
    darrow(d, pr.X(0.5), pr.Y(-2.4) + 22, pr.X(1.5), pr.Y(-2.4) + 22, ORANGE, 3)
    ctext(d, pr.X(1.0), pr.Y(-2.4) + 28, "Periodendauer T", f(FB, 20), ORANGE)
    ctext(d, 690, 400, "Waagrecht: ZEIT t → hier liest man T ab", f(FB, 20), RED)
    ctext(d, 450, 436, "Gleiche Kurvenform – andere Achse! Immer zuerst die waagrechte Achse lesen.", f(FR, 20), MUTED)
    save(im, IMG + "g4_ort_zeit.png")


def ueberlagerung_gif():
    """Zwei Pulse laufen aufeinander zu, überlagern sich und laufen unverändert weiter.
    Oben: gleiches Vorzeichen (+2 und +2 → +4), unten: entgegengesetzt (+2 und −2 → 0)."""
    W, H = 900, 560
    N = 24
    frames = []
    pulse = lambda x, c, a: a * math.exp(-((x - c) / 38.0) ** 2)
    for i in range(N):
        s_ = i / (N - 1)
        c1, c2 = 160 + 580 * s_, 740 - 580 * s_
        im, d = canvas(W, H, WHITE)
        ctext(d, W / 2, 8, "Überlagerung: Auslenkungen werden mit Vorzeichen addiert", f(FB, 28), INK)
        for row, (a2, lab, yb) in enumerate(((60, "gleiche Richtung: +2 cm und +2 cm → +4 cm", 220), (-60, "entgegengesetzt: +2 cm und −2 cm → 0 cm", 440))):
            d.line(P(60, yb, 840, yb), fill=GRID, width=2 * S)
            poly(d, [(x, yb - pulse(x, c1, 60)) for x in range(60, 841, 4)], TEAL, 3)
            poly(d, [(x, yb - pulse(x, c2, a2)) for x in range(60, 841, 4)], ORANGE, 3)
            poly(d, [(x, yb - pulse(x, c1, 60) - pulse(x, c2, a2)) for x in range(60, 841, 4)], RED, 5)
            ltext(d, 60, yb - 150 if row == 0 else yb - 128, lab, f(FB, 22), INK)
            arrow(d, c1 - 30, yb + 20 + (0 if a2 > 0 else 60), c1 + 30, yb + 20 + (0 if a2 > 0 else 60), TEAL, 3, 12)
            arrow(d, c2 + 30, yb + 20 + (0 if a2 > 0 else 60), c2 - 30, yb + 20 + (0 if a2 > 0 else 60), ORANGE, 3, 12)
        ltext(d, 60, 520, "rot = Summe · danach laufen beide Pulse unverändert weiter", f(FR, 20), MUTED)
        frames.append(frame_of(im, W, H, 64))
    dur = [90] * N
    dur[N // 2] = 1600; dur[-1] = 1200; dur[0] = 900
    save_gif(frames, IMG + "ueberlagerung.gif", dur)


def stehende_welle_gif():
    W, H = 900, 380
    N = 20
    frames = []
    lam = 360.0
    for i in range(N):
        t = i / N
        im, d = canvas(W, H, WHITE)
        ctext(d, W / 2 + 120, 8, "Stehende Welle: Knoten ruhen, Bäuche schwingen", f(FB, 26), INK)
        y0 = 200
        d.line(P(90, y0, 810, y0), fill=GRID, width=2 * S)
        for k in range(5):
            dashed(d, 90 + k * lam / 2, y0 - 110, 90 + k * lam / 2, y0 + 110, GRID, 2)
        env = lambda x: 90 * math.sin(2 * math.pi * (x - 90) / lam)
        poly(d, [(x, y0 - env(x)) for x in range(90, 811, 4)], (225, 228, 232), 2)
        poly(d, [(x, y0 + env(x)) for x in range(90, 811, 4)], (225, 228, 232), 2)
        poly(d, [(x, y0 - env(x) * math.cos(2 * math.pi * t)) for x in range(90, 811, 3)], RED, 5)
        for k in range(5):
            x = 90 + k * lam / 2; d.ellipse(P(x - 8, y0 - 8, x + 8, y0 + 8), fill=INK)
            ctext(d, x, y0 + 116, "K", f(FB, 22), INK)
        for k in range(4):
            ctext(d, 90 + lam / 4 + k * lam / 2, y0 + 116, "B", f(FB, 22), RED)
        darrow(d, 90, 74, 90 + lam / 2, 74, ORANGE, 3, 12)
        ctext(d, 90 + lam / 4, 46, "Knotenabstand λ/2", f(FB, 20), ORANGE)
        ltext(d, 330, 342, "K = Knoten (immer Ruhe) · B = Bauch (größte Schwingung)", f(FR, 20), MUTED)
        frames.append(frame_of(im, W, H, 48))
    save_gif(frames, IMG + "stehende_welle.gif", [110] * N)


def g6_huygens():
    im, d = canvas(900, 470, WHITE)
    # links: gerade Front
    x0 = 120
    d.line(P(x0, 90, x0, 380), fill=TEAL, width=6 * S)
    r = 70
    for k in range(5):
        y = 120 + k * 62
        d.ellipse(P(x0 - 6, y - 6, x0 + 6, y + 6), fill=TEAL)
        d.arc(P(x0 - r, y - r, x0 + r, y + r), -90, 90, fill=ORANGE, width=3 * S)
    d.line(P(x0 + r, 90, x0 + r, 380), fill=RED, width=6 * S)
    arrow(d, x0 + r + 20, 235, x0 + r + 100, 235, INK, 4, 16)
    ctext(d, 170, 400, "alte Front (blau) → Elementarwellen", f(FB, 20), INK)
    ctext(d, 170, 428, "neue Front = Einhüllende (rot)", f(FB, 20), RED)
    # rechts: Öffnung → Beugung
    bx = 560
    d.rectangle(P(bx - 8, 70, bx + 8, 200), fill=GREY); d.rectangle(P(bx - 8, 270, bx + 8, 400), fill=GREY)
    for k in range(4): d.line(P(bx - 160 + k * 40, 90, bx - 160 + k * 40, 380), fill=TEAL, width=4 * S)
    for k, rr in enumerate((40, 80, 120, 160, 200)):
        d.arc(P(bx - rr, 235 - rr, bx + rr, 235 + rr), -80, 80, fill=RED, width=4 * S)
    ctext(d, bx + 60, 400, "Öffnung etwa eine Wellenlänge breit:", f(FB, 20), INK)
    ctext(d, bx + 60, 428, "dahinter Halbkreise – Beugung in den Schatten", f(FB, 20), RED)
    ctext(d, 450, 4, "Prinzip von Huygens – ein Modell für die Ausbreitung", f(FB, 28), INK)
    save(im, IMG + "g6_huygens.png")


def g7_spektrum():
    im, d = canvas(900, 470, WHITE)
    ctext(d, 450, 12, "Das elektromagnetische Spektrum (nicht maßstäblich)", f(FB, 28), INK)
    bands = [("Radiowellen", 190, (190, 200, 175)), ("Mikro-\nwellen", 90, (170, 185, 150)), ("Infrarot", 110, (220, 140, 110)), ("sicht-\nbar", 70, None),
             ("UV", 90, (170, 140, 210)), ("Röntgen", 110, (150, 160, 175)), ("Gamma", 110, (110, 120, 135))]
    x = 30; y0, h = 120, 110
    for name, w, col in bands:
        if col is None:
            for k in range(w):
                hue = k / w
                c = [int(255 * max(0, min(1, v))) for v in (1.5 - abs(hue * 3 - 0.0) if hue < 0.5 else abs(hue * 3 - 2.4), 1 - abs(hue * 2 - 1) * 1.1 + 0.2, hue * 1.4 - 0.2)]
                d.line(P(x + k, y0, x + k, y0 + h), fill=tuple(c))
        else:
            d.rectangle(P(x, y0, x + w, y0 + h), fill=col)
        d.rectangle(P(x, y0, x + w, y0 + h), outline=WHITE, width=2 * S)
        for j, line in enumerate(name.split("\n")):
            ctext(d, x + w / 2, y0 + 30 + j * 26 - (12 if "\n" in name else 0), line, f(FB, 20), INK if col is None or sum(col) > 420 else WHITE)
        x += w
    # Markierung Mikrowellen als Teil der Radiowellen
    d.line(P(30, y0 - 14, 310, y0 - 14), fill=OLIVE, width=3 * S); d.line(P(30, y0 - 22, 30, y0 - 6), fill=OLIVE, width=3 * S); d.line(P(310, y0 - 22, 310, y0 - 6), fill=OLIVE, width=3 * S)
    ltext(d, 30, y0 - 48, "Radiowellen im weiteren Sinn (inkl. Mikrowellen)", f(FB, 18), OLIVE)
    arrow(d, 60, 270, 850, 270, RED, 5, 18); ltext(d, 60, 280, "Frequenz und Energie je Photon nehmen zu →", f(FB, 22), RED)
    arrow(d, 850, 330, 60, 330, TEAL, 5, 18); rtext(d, 850, 340, "← Wellenlänge nimmt zu", f(FB, 22), TEAL)
    xs, x = [], 30
    for name, w, col in bands: xs.append(x + w / 2); x += w
    for k, (xc, t) in enumerate(zip(xs, ("Funk, Radio", "Radar, WLAN", "Wärmebild", "Sehen", "Sonnenbrand", "Röntgenbild", "Kernzerfall"))):
        ctext(d, xc, 384 + (22 if k % 2 else 0), t, f(FR, 19), INK)
    d.line(P(xs[5] - 55, 438, xs[6] + 55, 438), fill=RUST, width=4 * S); ctext(d, (xs[5] + xs[6]) / 2, 442, "ionisierend", f(FB, 18), RUST)
    save(im, IMG + "g7_spektrum.png")


# ============================================================ Versuchsskizzen (900 × 629)
def tisch(d, x0, x1, y):
    d.rectangle(P(x0, y, x1, y + 22), fill=(200, 170, 120), outline=GREY, width=2 * S)
    d.line(P(x0 + 30, y + 22, x0 + 30, 600), fill=(170, 140, 95), width=8 * S); d.line(P(x1 - 30, y + 22, x1 - 30, 600), fill=(170, 140, 95), width=8 * S)


def v1():
    im, d = canvas()
    ctext(d, 450, 14, "K2.1-V1 · Aufbau Fadenpendel über die Tischkante", f(FB, 30), INK)
    tisch(d, 60, 520, 420)
    # Stativ: V-Fuß, senkrechter Stab, Doppelmuffe, waagrechter Stab über die Kante
    d.polygon(P(330, 420, 470, 420, 450, 404, 350, 404), fill=GREY)
    d.rectangle(P(395, 70, 405, 404), fill=(150, 156, 162))
    d.rectangle(P(388, 82, 412, 104), fill=(90, 96, 102))
    d.rectangle(P(400, 88, 720, 98), fill=(150, 156, 162))
    d.rectangle(P(655, 82, 685, 104), fill=(90, 96, 102))
    # Bücher auf dem Fuß
    d.rectangle(P(340, 380, 460, 404), fill=TEAL); d.rectangle(P(350, 360, 450, 380), fill=RUST)
    ltext(d, 200, 360, "Fuß beschweren", f(FR, 20), INK)
    # Pendel
    hx, top = 670, 104
    L = 330
    a = math.radians(8)
    bx, by = hx + L * math.sin(a), top + L * math.cos(a)
    dashed(d, hx, top, hx, top + L + 30, GREY, 2)
    d.line(P(hx, top, bx, by), fill=YELLOW, width=3 * S)
    d.rounded_rectangle(P(bx - 14, by - 6, bx + 14, by + 40), radius=6 * S, fill=BRASS, outline=GREY, width=2 * S)
    d.rectangle(P(bx - 6, by - 16, bx + 6, by - 4), fill=BRASS)
    darrow(d, hx - 40, top, hx - 40, by + 17, TEAL, 3)
    ltext(d, hx - 205, 260, "l bis zur Mitte", f(FB, 20), TEAL); ltext(d, hx - 205, 284, "des Gewichts", f(FB, 20), TEAL)
    ctext(d, hx + 90, 120, "Schnur in der", f(FR, 18), INK); ctext(d, hx + 90, 140, "Klemme festklemmen", f(FR, 18), INK)
    d.arc(P(hx - 90, top - 90, hx + 90, top + 90), 80, 90, fill=ORANGE, width=4 * S)
    ltext(d, hx + 16, top + 96, "≤ 10°", f(FB, 20), ORANGE)
    ctext(d, 450, 520, "Schwingungsebene frei – niemand steht davor", f(FB, 24), RED)
    ctext(d, 450, 556, "Messung: 10 volle Schwingungen, zwei Läufe je Länge (0,40 m und 0,90 m)", f(FR, 22), INK)
    save(im, VSI + "d_v1.png")


def v2():
    im, d = canvas()
    ctext(d, 450, 14, "K2.1-V2 · Pendel im Takt anstoßen (Lehrer-Demo)", f(FB, 30), INK)
    hx, top = 300, 190
    d.ellipse(P(hx - 40, top - 70, hx + 40, top + 10), fill=(230, 190, 160), outline=GREY, width=2 * S)
    ctext(d, hx, top - 46, "Hand", f(FB, 20), INK)
    darrow(d, hx - 60, top - 90, hx + 60, top - 90, ORANGE, 4)
    ctext(d, hx, top - 126, "ca. 1 cm hin und her", f(FB, 20), ORANGE)
    L = 230; a = math.radians(12)
    bx, by = hx + L * math.sin(a), top + L * math.cos(a)
    d.line(P(hx, top, bx, by), fill=YELLOW, width=3 * S)
    d.rounded_rectangle(P(bx - 14, by - 6, bx + 14, by + 40), radius=6 * S, fill=BRASS, outline=GREY, width=2 * S)
    d.arc(P(hx - L - 30, top - L - 30, hx + L + 30, top + L + 30), 60, 120, fill=RED, width=4 * S)
    ltext(d, 560, 150, "Drei Takte vergleichen:", f(FB, 24), INK)
    for k, (t, c) in enumerate((("langsam", TEAL), ("im eigenen Rhythmus", RED), ("deutlich schneller", ORANGE))):
        d.ellipse(P(560, 200 + k * 60, 590, 230 + k * 60), fill=c); ltext(d, 604, 202 + k * 60, t, f(FB, 22), INK)
    ctext(d, 450, 470, "Wo wird der Ausschlag am größten?", f(FB, 28), RED)
    ctext(d, 450, 520, "Stopp bei ca. 20 cm Ausschlag · kein Glas, kein Zerstörungsversuch", f(FR, 22), INK)
    save(im, VSI + "d_v2.png")


def v3():
    im, d = canvas()
    ctext(d, 450, 14, "K2.2-V1 · Ein Puls läuft über die Schnur", f(FB, 30), INK)
    y0 = 300
    for k, (c, lab) in enumerate(((60, "Kadett A"), (840, "Kadett B"))):
        d.ellipse(P(c - 26, y0 - 150, c + 26, y0 - 98), fill=TEAL); d.rounded_rectangle(P(c - 24, y0 - 96, c + 24, y0 + 40), radius=10 * S, fill=TEAL)
        ctext(d, c, y0 + 60, lab, f(FB, 20), INK)
    pts = [(x, y0 - 70 * math.exp(-((x - 300) / 50) ** 2)) for x in range(84, 820, 4)]
    poly(d, pts, YELLOW, 6)
    arrow(d, 330, y0 - 110, 480, y0 - 110, TEAL, 5, 18); ctext(d, 405, y0 - 150, "Puls läuft", f(FB, 22), TEAL)
    # Markierung (Büroklammer) in der Mitte
    mx = 560
    d.rounded_rectangle(P(mx - 10, y0 - 22, mx + 10, y0 + 18), radius=6 * S, outline=(120, 126, 132), width=3 * S)
    darrow(d, mx + 34, y0 - 60, mx + 34, y0 + 50, RED, 4)
    ltext(d, mx + 48, y0 - 20, "Büroklammer: bewegt sich nur auf und ab", f(FB, 20), RED)
    ctext(d, 450, 430, "Schnur ca. 3 m · nur leicht gespannt · unter Gesichtshöhe", f(FB, 24), INK)
    ctext(d, 450, 470, "kleine Handbewegung (5–10 cm), kein Ruck", f(FR, 22), INK)
    save(im, VSI + "d_v3.png")


def v4():
    im, d = canvas()
    ctext(d, 450, 14, "K2.2-V2 · Überlagerung am Modell (Simulation oder Grafik)", f(FB, 30), INK)
    d.rounded_rectangle(P(80, 80, 520, 380), radius=16 * S, fill=(40, 46, 52), outline=GREY, width=3 * S)
    d.rectangle(P(100, 100, 500, 340), fill=(20, 40, 70))
    for rr in range(20, 260, 28):
        for cx in (230, 370):
            d.arc(P(cx - rr, 120 - rr, cx + rr, 120 + rr), 0, 180, fill=(120, 170, 230), width=2 * S)
    d.rectangle(P(80, 380, 520, 395), fill=(90, 96, 102))
    ctext(d, 300, 400, "PhET »Welleninterferenz« am Beamer", f(FB, 20), INK)
    rows = [("y1", "y2", "y1 + y2"), ("+2", "+2", "?"), ("+2", "−2", "?"), ("+2", "−1", "?")]
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            x, y = 580 + c * 100, 120 + r * 56
            d.rectangle(P(x, y, x + 100, y + 56), fill=LIGHT if r == 0 else WHITE, outline=GREY, width=2 * S)
            ctext(d, x + 50, y + 14, v, f(FB, 22), INK)
    ctext(d, 730, 352, "alle Werte in cm", f(FR, 20), MUTED)
    ctext(d, 450, 470, "Erst vorhersagen, dann vergleichen – das ist ein Modell, kein Messversuch", f(FB, 24), RED)
    save(im, VSI + "d_v4.png")


# ============================================================ neue Icons (180 × 108, transparent)
def icon(name, draw):
    ic = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ic)
    draw(d); ic = ic.resize((180, 108), Image.LANCZOS)
    ic.save(ICONS + name + ".png", optimize=True)


OUT = (110, 115, 120)


def new_icons():
    def schnur(d):
        d.ellipse(P(36, 24, 106, 94), fill=YELLOW, outline=OUT, width=2 * S)
        d.ellipse(P(60, 48, 82, 70), fill=(250, 250, 245), outline=OUT, width=2 * S)
        for k in range(4): d.arc(P(42 + k * 4, 30 + k * 4, 100 - k * 4, 88 - k * 4), 200, 340, fill=(210, 170, 20), width=2 * S)
        poly(d, [(100, 70), (120, 64), (138, 76), (156, 66)], YELLOW, 4)
    if not os.path.exists(ICONS + "schnur.png"): icon("schnur", schnur)

    def gewicht(d):
        d.rounded_rectangle(P(62, 42, 118, 98), radius=6 * S, fill=BRASS, outline=OUT, width=2 * S)
        d.rectangle(P(82, 28, 98, 42), fill=BRASS, outline=OUT, width=2 * S)
        d.ellipse(P(76, 12, 104, 32), fill=BRASS, outline=OUT, width=2 * S)
        d.line(P(70, 60, 110, 60), fill=(230, 200, 120), width=2 * S)
    if not os.path.exists(ICONS + "gewicht.png"): icon("gewicht", gewicht)

    def bandmass(d):
        d.rounded_rectangle(P(28, 24, 98, 94), radius=14 * S, fill=YELLOW, outline=OUT, width=2 * S)
        d.ellipse(P(48, 44, 78, 74), fill=(250, 250, 240), outline=OUT, width=2 * S)
        d.rectangle(P(96, 74, 160, 90), fill=(250, 235, 160), outline=OUT, width=2 * S)
        for x in range(102, 160, 8): d.line(P(x, 74, x, 80), fill=OUT, width=S)
        d.rectangle(P(156, 70, 164, 94), fill=(150, 156, 162))
    if not os.path.exists(ICONS + "bandmass.png"): icon("bandmass", bandmass)

    def beamer(d):
        d.rounded_rectangle(P(36, 18, 144, 80), radius=6 * S, fill=(40, 46, 52), outline=OUT, width=2 * S)
        d.rectangle(P(44, 26, 136, 72), fill=(120, 170, 230))
        d.polygon(P(20, 92, 160, 92, 146, 80, 34, 80), fill=(150, 156, 162), outline=OUT)
    if not os.path.exists(ICONS + "laptop.png"): icon("laptop", beamer)


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
    schaukel(); g1_schwingung(); a1_diagramm(); pendel_gif(); g_pendel(); g2_daempfung(); g3_resonanz()
    welle_gif(); g4_ort_zeit(); ueberlagerung_gif(); stehende_welle_gif(); g6_huygens(); g7_spektrum()
    for fn in (v1, v2, v3, v4): fn()
    new_icons()
    print("Icons:", sorted(icons_kopieren()))
    for p in sorted(os.listdir(IMG)) + ["vs-img/" + x for x in sorted(os.listdir(VSI))]:
        print(p, os.path.getsize((IMG + p) if not p.startswith("vs-img/") else UNIT + p) // 1024, "KB")
