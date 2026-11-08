"""Bilder, Versuchsskizzen und neue Icons für NAWI 1AB K2.1 Mechanische Kräfte – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k2-1-kraefte/skizzen.py
Schreibt 1ab-nawi/k2-1-kraefte/img/*.png, vs-img/d_g1–g7.png, vs-img/i_*.png und neue Icons nach werkzeug/icons/
(kraftmesser, messbecher, messzylinder, spritze – im Stil der Bindungsarten-Icons: flach, farbig, dünne graue Kontur, transparent, 180 × 108 px).
Alle Zahlen in den Grafiken stimmen mit inhalt.py und versuche_daten.py überein."""
import math, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I
import versuche_daten as VD
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
IMG, VSI, ICONS = UNIT + "img/", UNIT + "vs-img/", os.path.join(ROOT, "werkzeug/icons/")
for p in (IMG, VSI): os.makedirs(p, exist_ok=True)
FR = "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"
FB = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
BG, WHITE, INK = (242, 243, 238), (255, 255, 255), (31, 42, 28)
OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = (59, 74, 47), (127, 168, 58), (217, 119, 43), (46, 125, 140), (140, 59, 46), (94, 102, 82)
RED, BLUE, LIGHT, GRID = (163, 58, 43), (42, 92, 140), (223, 229, 208), (206, 214, 196)
WATER, GLASS, METAL, WOOD = (167, 205, 222), (222, 234, 238), (176, 182, 190), (206, 176, 128)
S = 2
f = lambda p, s: ImageFont.truetype(p, int(s * S))
R = lambda s: f(FR, s)
B = lambda s: f(FB, s)


def canvas(w=900, h=560, bg=BG):
    im = Image.new("RGB", (w * S, h * S), bg); return im, ImageDraw.Draw(im)


def P(*xy):
    return [v * S for v in xy]


def ctext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w / 2, y * S), t, font=font, fill=fill)


def ltext(d, x, y, t, font, fill):
    d.text((x * S, y * S), t, font=font, fill=fill)


def rtext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w, y * S), t, font=font, fill=fill)


def save(im, path, w=None, h=None, q=160):
    w = w or im.width // S; h = h or im.height // S
    im.resize((w, h), Image.LANCZOS).quantize(colors=q).save(path, optimize=True)
    print("  ", os.path.relpath(path, ROOT), os.path.getsize(path) // 1024, "KB")


def arrow(d, x0, y0, x1, y1, col=INK, w=5, head=16):
    d.line(P(x0, y0, x1, y1), fill=col, width=int(w * S))
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1, y1), (x1 - head * math.cos(a - 0.42), y1 - head * math.sin(a - 0.42)), (x1 - head * math.cos(a + 0.42), y1 - head * math.sin(a + 0.42))]
    d.polygon([(px * S, py * S) for px, py in pts], fill=col)


def panel(d, x, y, w, h, titel, col=OLIVE):
    d.rounded_rectangle(P(x, y, x + w, y + h), radius=14 * S, fill=WHITE, outline=GRID, width=int(1.5 * S))
    d.rounded_rectangle(P(x, y, x + w, y + 30), radius=14 * S, fill=col)
    d.rectangle(P(x, y + 18, x + w, y + 30), fill=col)
    ctext(d, x + w / 2, y + 5, titel, B(17), WHITE)


def wasser(d, x, y, w, h, level):
    """Gefäß mit Wasser: x,y = linke obere Ecke der Gefäßöffnung, h = Gefäßhöhe, level = Wasserhöhe von unten."""
    d.rectangle(P(x, y, x + w, y + h), fill=GLASS, outline=MUTED, width=int(2 * S))
    d.rectangle(P(x + 2, y + h - level, x + w - 2, y + h - 2), fill=WATER)
    d.line(P(x + 2, y + h - level, x + w - 2, y + h - level), fill=TEAL, width=int(2 * S))


def legende(d, x, y, items):
    for i, (col, txt) in enumerate(items):
        yy = y + i * 26
        d.line(P(x, yy + 9, x + 34, yy + 9), fill=col, width=int(5 * S))
        arrow(d, x + 20, yy + 9, x + 36, yy + 9, col, 5, 11)
        ltext(d, x + 44, yy, txt, R(16), INK)


# ================================================================ 1 · Was eine Kraft bewirkt
def wirkung():
    im, d = canvas(900, 400)
    for i, (x, titel) in enumerate([(20, "Tempo ändern"), (310, "Richtung ändern"), (600, "Form ändern")]):
        panel(d, x, 14, 280, 300, titel, [GREEN, TEAL, ORANGE][i])
    # Panel 1: Wagen wird schneller
    d.rounded_rectangle(P(70, 170, 180, 215), radius=8 * S, fill=WOOD, outline=MUTED, width=int(2 * S))
    for cx in (92, 158): d.ellipse(P(cx - 13, 208, cx + 13, 234), fill=METAL, outline=INK, width=int(2 * S))
    arrow(d, 185, 192, 268, 192, RED, 6, 17); ltext(d, 196, 160, "F", B(20), RED)
    arrow(d, 60, 250, 150, 250, BLUE, 5, 14); ltext(d, 60, 258, "v wird größer", R(15), BLUE)
    ltext(d, 38, 285, "Antrieb größer als Reibung", R(15), MUTED)
    # Panel 2: Kurve
    d.arc(P(345, 110, 575, 290), start=200, end=340, fill=MUTED, width=int(4 * S))
    d.line(P(345, 240, 360, 268), fill=MUTED, width=int(3 * S))
    d.ellipse(P(432, 118, 468, 154), fill=WOOD, outline=INK, width=int(2 * S))
    arrow(d, 450, 136, 450, 212, RED, 6, 17); ltext(d, 458, 170, "F zur Kurvenmitte", R(15), RED)
    arrow(d, 450, 136, 550, 136, BLUE, 5, 14); ltext(d, 470, 108, "v", B(19), BLUE)
    ltext(d, 330, 285, "Tempo gleich, Richtung ändert sich", R(15), MUTED)
    # Panel 3: Ball zusammengedrückt
    d.ellipse(P(680, 150, 800, 240), fill=(226, 200, 150), outline=INK, width=int(2 * S))
    d.rounded_rectangle(P(636, 170, 672, 220), radius=10 * S, fill=LIGHT, outline=MUTED, width=int(2 * S))
    d.rounded_rectangle(P(808, 170, 844, 220), radius=10 * S, fill=LIGHT, outline=MUTED, width=int(2 * S))
    arrow(d, 668, 195, 700, 195, RED, 6, 15); arrow(d, 812, 195, 780, 195, RED, 6, 15)
    ltext(d, 700, 120, "F", B(20), RED); ltext(d, 768, 120, "F", B(20), RED)
    ltext(d, 640, 285, "keine Ortsänderung – trotzdem Kraft", R(15), MUTED)
    legende(d, 20, 330, [(RED, "Kraftpfeil F in Newton (N) – Länge zeigt den Betrag"), (BLUE, "Geschwindigkeitspfeil v in m/s")])
    save(im, IMG + "wirkung.png")


# ================================================================ 2 · Geschwindigkeit und Beschleunigung
def bewegung():
    im, d = canvas(900, 440)
    reihen = [("gleichförmig: gleiche Abstände", [80, 230, 380, 530, 680], GREEN),
              ("schneller werdend: Abstände wachsen", [80, 150, 260, 420, 640], ORANGE)]
    for ri, (titel, xs, col) in enumerate(reihen):
        y = 40 + ri * 150
        ltext(d, 30, y - 26, titel, B(18), col)
        d.line(P(60, y + 56, 860, y + 56), fill=GRID, width=int(2 * S))
        for i, x in enumerate(xs):
            d.ellipse(P(x - 16, y + 24, x + 16, y + 56), fill=WOOD, outline=INK, width=int(2 * S))
            ctext(d, x, y - 2, "t%d" % i, R(14), MUTED)
        for i in range(len(xs) - 1):
            d.line(P(xs[i], y + 76, xs[i + 1], y + 76), fill=col, width=int(3 * S))
            d.line(P(xs[i], y + 70, xs[i], y + 82), fill=col, width=int(3 * S))
            d.line(P(xs[i + 1], y + 70, xs[i + 1], y + 82), fill=col, width=int(3 * S))
            ctext(d, (xs[i] + xs[i + 1]) / 2, y + 84, "Δs", R(14), col)
    # Kurve mit gleichem Tempo
    y = 320
    ltext(d, 30, y - 24, "gleiches Tempo, aber Kurve: die Richtung von v ändert sich", B(18), TEAL)
    d.arc(P(300, y - 10, 600, y + 230), start=190, end=350, fill=GRID, width=int(4 * S))
    for ang, lab in ((200, "t0"), (270, "t1"), (340, "t2")):
        a = math.radians(ang); cx, cy, rx, ry = 450, y + 110, 150, 120
        px, py = cx + rx * math.cos(a), cy + ry * math.sin(a)
        d.ellipse(P(px - 13, py - 13, px + 13, py + 13), fill=WOOD, outline=INK, width=int(2 * S))
        tx, ty = -rx * math.sin(a), ry * math.cos(a)
        n = math.hypot(tx, ty); tx, ty = tx / n * 70, ty / n * 70
        arrow(d, px, py, px + tx, py + ty, BLUE, 5, 13)
        ctext(d, px, py - 34, lab, R(14), MUTED)
    ltext(d, 630, y + 60, "Zur Geschwindigkeit", R(16), INK)
    ltext(d, 630, y + 82, "gehört die Richtung.", R(16), INK)
    ltext(d, 630, y + 112, "v = s / t", B(22), OLIVE)
    ltext(d, 630, y + 140, "m/s · mal 3,6 = km/h", R(15), MUTED)
    save(im, IMG + "bewegung.png")


# ================================================================ 3 · Masse und Gewichtskraft
def gewicht():
    im, d = canvas(900, 420)
    for i, (x, titel, col) in enumerate([(40, "auf der Erde", TEAL), (480, "am Mond", MUTED)]):
        panel(d, x, 14, 380, 360, titel, col)
    for i, (x0, pfeil, kraft, g) in enumerate([(40, 150, "60 N", "g = 10 N/kg"), (480, 25, "ca. 10 N", "g ca. 1,6 N/kg")]):
        cx = x0 + 150
        # Rucksack
        d.rounded_rectangle(P(cx - 58, 70, cx + 58, 190), radius=20 * S, fill=(104, 118, 82), outline=INK, width=int(2 * S))
        d.rounded_rectangle(P(cx - 40, 96, cx + 40, 140), radius=10 * S, fill=(126, 142, 98), outline=MUTED, width=int(2 * S))
        d.arc(P(cx - 74, 62, cx - 34, 118), start=90, end=270, fill=INK, width=int(4 * S))
        d.arc(P(cx + 34, 62, cx + 74, 118), start=270, end=90, fill=INK, width=int(4 * S))
        ctext(d, cx, 200, "m = 6 kg", B(21), OLIVE)
        ctext(d, cx, 226, "(gleich!)", R(15), MUTED)
        arrow(d, cx, 250, cx, 250 + pfeil, RED, 7, 18)
        ltext(d, cx + 14, 254 + pfeil / 2 - 12, "F_G = " + kraft, B(19), RED)
        ctext(d, cx, 342, g, R(16), MUTED)
    d.line(P(40, 380, 860, 380), fill=GRID, width=int(2 * S))
    ctext(d, 450, 388, "F_G = m · g   ·   Masse in kg bleibt gleich, Gewichtskraft in N hängt vom Ort ab", B(18), OLIVE)
    save(im, IMG + "gewicht.png")


# ================================================================ 4 · Auftrieb
def auftrieb():
    im, d = canvas(900, 500)
    titel = ["steigt (aus der Ruhe)", "schwebt", "schwimmt ruhig"]
    cols = [GREEN, TEAL, ORANGE]
    for i in range(3):
        x = 30 + i * 290
        panel(d, x, 14, 260, 376, titel[i], cols[i])
        cx = x + 130
        d.rectangle(P(x + 24, 52, x + 236, 318), fill=GLASS, outline=MUTED, width=int(2 * S))
        d.rectangle(P(x + 26, 92, x + 234, 316), fill=WATER)
        d.line(P(x + 26, 92, x + 234, 92), fill=TEAL, width=int(3 * S))
        ya = 228
        if i == 2:
            d.polygon([(cx - 60) * S, 60 * S, (cx + 60) * S, 60 * S, (cx + 40) * S, 122 * S, (cx - 40) * S, 122 * S],
                      fill=WOOD, outline=INK, width=int(2 * S))
            fa = fg = 70
        else:
            cy = 176
            d.ellipse(P(cx - 34, cy - 34, cx + 34, cy + 34), fill=WOOD, outline=INK, width=int(2 * S))
            fa, fg = (96, 54) if i == 0 else (70, 70)
            if i == 0: arrow(d, cx + 88, cy + 24, cx + 88, cy - 44, GREEN, 5, 14)
        # Kräftepfeile nebeneinander auf derselben Grundlinie – die Längen sind direkt vergleichbar
        arrow(d, cx - 30, ya, cx - 30, ya - fa, TEAL, 7, 17)
        arrow(d, cx + 30, ya, cx + 30, ya + fg, RED, 7, 17)
        rtext(d, cx - 40, ya - fa / 2 - 12, "F_A", B(19), TEAL)
        ltext(d, cx + 40, ya + fg / 2 - 12, "F_G", B(19), RED)
        d.line(P(cx - 52, ya, cx + 52, ya), fill=MUTED, width=int(2 * S))
        ctext(d, cx, 336, "F_A > F_G" if i == 0 else "F_A = F_G", B(21), OLIVE)
    legende(d, 30, 406, [(TEAL, "Auftriebskraft F_A – so groß wie die Gewichtskraft des verdrängten Wassers"),
                         (RED, "Gewichtskraft F_G des Körpers")])
    ltext(d, 30, 464, "Beide Pfeile starten auf derselben grauen Grundlinie – so kannst du ihre Längen direkt vergleichen.", R(16), MUTED)
    save(im, IMG + "auftrieb.png")


# ================================================================ 5 · Reibung
def reibung():
    im, d = canvas(900, 420)
    panel(d, 20, 14, 430, 300, "Becher wird gezogen", GREEN)
    d.rectangle(P(44, 230, 426, 246), fill=LIGHT, outline=MUTED, width=int(2 * S))
    for x in range(50, 424, 18): d.line(P(x, 246, x - 8, 258), fill=GRID, width=int(2 * S))
    d.polygon([152 * S, 156 * S, 244 * S, 156 * S, 234 * S, 230 * S, 162 * S, 230 * S], fill=(226, 232, 238), outline=INK, width=int(2 * S))
    d.rectangle(P(166, 180, 230, 228), fill=WATER)
    d.arc(P(240, 166, 276, 202), start=270, end=90, fill=INK, width=int(4 * S))
    arrow(d, 278, 184, 390, 184, GREEN, 6, 17); ctext(d, 334, 152, "Zugkraft", B(18), GREEN)
    arrow(d, 150, 200, 62, 200, RUST, 6, 17); ctext(d, 104, 168, "F_R", B(18), RUST)
    arrow(d, 198, 232, 198, 296, RED, 6, 16); ltext(d, 206, 258, "F_G", B(18), RED)
    arrow(d, 198, 154, 198, 92, TEAL, 6, 16); ltext(d, 206, 108, "F_N", B(18), TEAL)
    ctext(d, 104, 190, "Reibung", R(15), RUST)
    panel(d, 470, 14, 410, 300, "Abstoßen beim Gehen", ORANGE)
    d.rectangle(P(500, 250, 860, 266), fill=LIGHT, outline=MUTED, width=int(2 * S))
    d.polygon([600 * S, 196 * S, 640 * S, 196 * S, 700 * S, 236 * S, 700 * S, 250 * S, 590 * S, 250 * S],
              fill=(214, 182, 140), outline=INK, width=int(2 * S))
    d.rectangle(P(590, 240, 702, 252), fill=(70, 70, 76), outline=INK, width=int(2 * S))
    arrow(d, 640, 272, 540, 272, ORANGE, 6, 17); ltext(d, 520, 282, "Fuß auf Boden (nach hinten)", R(15), ORANGE)
    arrow(d, 660, 226, 790, 226, TEAL, 6, 17); ltext(d, 700, 196, "Boden auf Fuß (nach vorne)", R(15), TEAL)
    ctext(d, 675, 118, "Haftreibung treibt an!", B(19), OLIVE)
    d.line(P(20, 330, 880, 330), fill=GRID, width=int(2 * S))
    ltext(d, 20, 340, "Reibung wirkt gegen das relative Gleiten an der Kontaktstelle – nicht automatisch gegen die Bewegung über den Boden.", R(16), INK)
    ltext(d, 20, 366, "F_R = μ · F_N ist ein einfaches Näherungsmodell für Gleitreibung. Bis zum Losrutschen gilt F_H kleiner oder gleich μ_H · F_N.", R(16), MUTED)
    save(im, IMG + "reibung.png")


# ================================================================ 6 · Kapillarwirkung
def kapillar():
    im, d = canvas(900, 420)
    panel(d, 30, 14, 400, 320, "Filterpapier im Wasser", TEAL)
    d.rectangle(P(120, 196, 340, 318), fill=GLASS, outline=MUTED, width=int(2 * S))
    d.rectangle(P(122, 244, 338, 316), fill=WATER)
    d.line(P(120, 244, 340, 244), fill=TEAL, width=int(3 * S))
    d.rectangle(P(206, 66, 248, 300), fill=(252, 250, 244), outline=MUTED, width=int(2 * S))
    d.rectangle(P(208, 150, 246, 298), fill=(206, 226, 234))
    d.line(P(206, 150, 248, 150), fill=TEAL, width=int(3 * S))
    d.line(P(258, 150, 300, 150), fill=GREEN, width=int(2 * S))
    arrow(d, 300, 244, 300, 154, GREEN, 5, 14)
    ltext(d, 312, 172, "steigt über den", R(15), GREEN); ltext(d, 312, 192, "Wasserspiegel", R(15), GREEN)
    rtext(d, 112, 234, "Wasserspiegel", R(15), MUTED)
    rtext(d, 198, 118, "feuchte", B(15), TEAL); rtext(d, 198, 138, "Grenze", B(15), TEAL)
    ctext(d, 227, 306, "3 mm tief", R(14), MUTED)
    panel(d, 470, 14, 400, 320, "Enges benetzbares Röhrchen", ORANGE)
    d.rectangle(P(520, 226, 760, 318), fill=GLASS, outline=MUTED, width=int(2 * S))
    d.rectangle(P(522, 258, 758, 316), fill=WATER)
    d.line(P(520, 258, 760, 258), fill=TEAL, width=int(3 * S))
    d.rectangle(P(648, 110, 680, 300), fill=GLASS, outline=MUTED, width=int(2 * S))
    d.rectangle(P(650, 152, 678, 298), fill=WATER)
    d.arc(P(650, 144, 678, 162), start=180, end=360, fill=TEAL, width=int(3 * S))
    d.line(P(580, 152, 646, 152), fill=GREEN, width=int(2 * S))
    arrow(d, 584, 258, 584, 156, GREEN, 5, 14); rtext(d, 574, 190, "Steighöhe", B(15), GREEN)
    arrow(d, 614, 118, 646, 130, ORANGE, 4, 11); rtext(d, 608, 106, "Adhäsion an der Wand", R(14), ORANGE)
    for cx, cy in ((720, 120), (742, 140), (714, 156), (740, 176)):
        d.ellipse(P(cx - 10, cy - 10, cx + 10, cy + 10), fill=WATER, outline=TEAL, width=int(2 * S))
    d.line(P(730, 132, 752, 150), fill=TEAL, width=int(2 * S)); d.line(P(724, 148, 748, 166), fill=TEAL, width=int(2 * S))
    ltext(d, 762, 124, "Kohäsion:", B(16), TEAL); ltext(d, 762, 146, "Wasser hält", R(15), INK); ltext(d, 762, 166, "zusammen", R(15), INK)
    d.line(P(30, 348, 870, 348), fill=GRID, width=int(2 * S))
    ltext(d, 30, 358, "Adhäsion = Anziehung zwischen verschiedenen Stoffen · Kohäsion = Zusammenhalt in einem Stoff.", R(16), INK)
    ltext(d, 30, 384, "Für den Wassertransport in einen hohen Baum braucht es zusätzlich den Transpirationssog.", R(16), MUTED)
    save(im, IMG + "kapillar.png")


# ================================================================ 7 · Druck
def druck():
    im, d = canvas(900, 520)
    panel(d, 20, 14, 860, 250, "Gleiche Kraft, andere Fläche: p = F / A", GREEN)
    for i, (cx, breite, lab, pfeile) in enumerate([(240, 60, "schmale Sohle: großer Druck", 2), (660, 190, "Schneeschuh: kleiner Druck", 6)]):
        d.rounded_rectangle(P(cx - 34, 60, cx + 34, 160), radius=12 * S, fill=(104, 118, 82), outline=INK, width=int(2 * S))
        d.rounded_rectangle(P(cx - breite / 2, 160, cx + breite / 2, 180), radius=6 * S, fill=WOOD, outline=INK, width=int(2 * S))
        arrow(d, cx, 36, cx, 58, RED, 6, 14); ltext(d, cx + 10, 32, "F = 600 N", B(17), RED)
        d.rectangle(P(cx - 130, 196, cx + 130, 212), fill=(236, 240, 246), outline=GRID, width=int(2 * S))
        step = breite / (pfeile + 1)
        for k in range(1, pfeile + 1):
            px = cx - breite / 2 + k * step
            arrow(d, px, 182, px, 196, TEAL, 4, 10)
        ctext(d, cx, 220, lab, B(17), OLIVE)
    ctext(d, 240, 242, "A = 0,03 m²  →  p = 20 000 Pa", R(17), MUTED)
    ctext(d, 660, 242, "A = 0,30 m²  →  p = 2 000 Pa", R(17), MUTED)
    panel(d, 20, 284, 860, 212, "Luft lässt sich zusammendrücken", ORANGE)
    for i, (x, offen, lab) in enumerate([(80, True, "Öffnung offen: Luft entweicht, Kolben geht leicht"),
                                         (490, False, "Öffnung zu: Druck steigt, Kolben drückt zurück")]):
        y = 350
        d.rounded_rectangle(P(x, y, x + 240, y + 54), radius=8 * S, fill=GLASS, outline=MUTED, width=int(2 * S))
        kolben = x + (120 if offen else 96)
        d.rectangle(P(kolben, y + 2, kolben + 14, y + 52), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(kolben + 14, y + 20, x + 300, y + 34), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(x + 300, y + 4, x + 312, y + 50), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(x - 26, y + 20, x, y + 34), fill=GLASS, outline=MUTED, width=int(2 * S))
        if not offen:
            d.ellipse(P(x - 48, y + 12, x - 16, y + 44), fill=(226, 196, 162), outline=INK, width=int(2 * S))
            ctext(d, x - 32, y - 26, "Finger", R(15), INK)
        for k in range(6):
            px, py = x + 12 + (k % 3) * 32, y + 14 + (k // 3) * 24
            d.ellipse(P(px, py, px + 9, py + 9), fill=(196, 214, 226) if offen else TEAL, outline=None)
        arrow(d, x + 330, y + 27, x + 280, y + 27, GREEN if offen else RUST, 6, 15)
        if not offen: arrow(d, kolben - 10, y + 27, kolben - 56, y + 27, RED, 5, 13)
        ctext(d, x + 150, y + 86, lab, R(16), MUTED)
    ctext(d, 450, 470, "Druck ist keine zusätzliche Kraftart – er verbindet eine Kraft mit der Fläche, auf die sie wirkt.", B(17), OLIVE)
    save(im, IMG + "druck.png")


# ================================================================ 8 · Kraft und Gegenkraft
def gegenkraft():
    im, d = canvas(900, 430)
    panel(d, 20, 14, 500, 320, "Wechselwirkung: zwei Körper", TEAL)
    for i, (x, col, lab) in enumerate([(70, GREEN, "Kraftmesser A"), (300, ORANGE, "Kraftmesser B")]):
        d.rounded_rectangle(P(x, 110, x + 150, 180), radius=8 * S, fill=WHITE, outline=col, width=int(3 * S))
        d.rectangle(P(x + 10, 126, x + 130, 150), fill=LIGHT, outline=MUTED, width=int(2 * S))
        for k in range(1, 6): d.line(P(x + 10 + k * 20, 150, x + 10 + k * 20, 158), fill=MUTED, width=int(2 * S))
        d.line(P(x + 50, 126, x + 50, 150), fill=RED, width=int(4 * S))
        ctext(d, x + 75, 186, "2 N", B(21), RED)
        ctext(d, x + 75, 88, lab, B(16), col)
    d.arc(P(212, 134, 246, 162), start=90, end=270, fill=INK, width=int(4 * S))
    d.arc(P(284, 134, 318, 162), start=270, end=90, fill=INK, width=int(4 * S))
    arrow(d, 60, 240, 150, 240, GREEN, 6, 16); ltext(d, 60, 254, "B zieht an A", R(15), GREEN)
    arrow(d, 480, 240, 390, 240, ORANGE, 6, 16); rtext(d, 480, 254, "A zieht an B", R(15), ORANGE)
    ctext(d, 270, 290, "gleich groß · entgegengesetzt · verschiedene Körper", B(17), OLIVE)
    ctext(d, 270, 312, "2 N und 2 N sind NICHT 4 N", B(17), RUST)
    panel(d, 550, 14, 330, 320, "Gleichgewicht: ein Körper", ORANGE)
    d.rectangle(P(600, 220, 840, 236), fill=WOOD, outline=INK, width=int(2 * S))
    d.line(P(630, 236, 630, 290), fill=MUTED, width=int(4 * S)); d.line(P(810, 236, 810, 290), fill=MUTED, width=int(4 * S))
    d.rounded_rectangle(P(660, 176, 780, 220), radius=5 * S, fill=(196, 150, 120), outline=INK, width=int(2 * S))
    d.rectangle(P(656, 172, 784, 182), fill=(232, 226, 210), outline=INK, width=int(2 * S))
    d.rounded_rectangle(P(650, 164, 790, 226), radius=10 * S, fill=None, outline=RUST, width=int(3 * S))
    rtext(d, 644, 186, "Rahmen =", R(14), RUST); rtext(d, 644, 204, "das Buch", R(14), RUST)
    arrow(d, 700, 196, 700, 128, TEAL, 6, 16); ctext(d, 700, 104, "Stützkraft", B(16), TEAL)
    arrow(d, 744, 196, 744, 276, RED, 6, 16); ltext(d, 754, 224, "F_G", B(17), RED)
    ctext(d, 715, 300, "beide am selben Körper – Summe null", R(15), OLIVE)
    d.line(P(20, 350, 880, 350), fill=GRID, width=int(2 * S))
    ltext(d, 20, 360, "Wechselwirkungspaar: zwei Körper, zwei Kräfte. Kräftegleichgewicht: ein Körper, mehrere Kräfte, Summe null.", R(16), INK)
    ltext(d, 20, 386, "Die Gegenkraft zur Gewichtskraft auf das Buch ist die Anziehung des Buches auf die Erde – nicht die Stützkraft.", R(16), MUTED)
    save(im, IMG + "gegenkraft.png")


# ================================================================ 9 · Größen und Einheiten
def einheiten():
    im, d = canvas(900, 430)
    ctext(d, 450, 18, "Alle Größen dieser Einheit auf einen Blick", B(22), OLIVE)
    zeilen = [("Masse", "m", "kg", "Waage", GREEN), ("Kraft", "F", "N", "F = m · a", RED),
              ("Gewichtskraft", "F_G", "N", "F_G = m · g, hier g = 10 N/kg", RUST),
              ("Schnelligkeit", "v", "m/s", "v = s / t, mal 3,6 = km/h", BLUE),
              ("Beschleunigung", "a", "m/s²", "Tempo ODER Richtung ändert sich", TEAL),
              ("Druck", "p", "Pa", "p = F / A, 1 Pa = 1 N/m²", ORANGE)]
    y = 62
    d.rounded_rectangle(P(30, y, 870, y + 34), radius=8 * S, fill=OLIVE)
    for x, t in ((48, "Größe"), (260, "Zeichen"), (380, "Einheit"), (510, "So rechnest du")):
        ltext(d, x, y + 7, t, B(17), WHITE)
    y += 40
    for i, (name, zeichen, einheit, formel, col) in enumerate(zeilen):
        d.rounded_rectangle(P(30, y, 870, y + 44), radius=8 * S, fill=WHITE if i % 2 else (248, 250, 244), outline=GRID, width=int(1.5 * S))
        d.rectangle(P(30, y + 6, 36, y + 38), fill=col)
        ltext(d, 48, y + 11, name, B(18), INK)
        ltext(d, 260, y + 11, zeichen, B(18), col)
        ltext(d, 380, y + 11, einheit, B(18), OLIVE)
        ltext(d, 510, y + 12, formel, R(17), MUTED)
        y += 50
    d.rounded_rectangle(P(30, y + 4, 870, y + 46), radius=10 * S, fill=(246, 227, 223), outline=RUST, width=int(2 * S))
    ctext(d, 450, y + 14, "Geschwindigkeit, Beschleunigung und Druck sind KEINE Kraftarten.", B(18), RUST)
    save(im, IMG + "einheiten.png")


# ================================================================ 10 · Ablauf des Projekts
def projekt():
    im, d = canvas(900, 300)
    ctext(d, 450, 14, "Euer Gruppenprojekt in fünf Schritten", B(22), OLIVE)
    schritte = [("Stunde 2", "Frage und\nVermutung", GREEN), ("Stunde 2", "Plan und\nzwei Quellen", TEAL),
                ("Stunde 3", "Messen –\nechte Werte", RED), ("Stunde 4", "Erklären\nmit Grenze", ORANGE),
                ("Stunde 5", "3 Minuten\npräsentieren", RUST)]
    bw, gap = 150, 32
    x = (900 - (len(schritte) * bw + (len(schritte) - 1) * gap)) / 2
    for i, (wann, txt, col) in enumerate(schritte):
        bx = x + i * (bw + gap)
        d.rounded_rectangle(P(bx, 66, bx + bw, 206), radius=14 * S, fill=WHITE, outline=col, width=int(3 * S))
        d.rounded_rectangle(P(bx, 66, bx + bw, 100), radius=14 * S, fill=col)
        d.rectangle(P(bx, 88, bx + bw, 100), fill=col)
        ctext(d, bx + bw / 2, 72, wann, B(16), WHITE)
        for k, line in enumerate(txt.split("\n")):
            ctext(d, bx + bw / 2, 124 + k * 28, line, B(19), INK)
        d.ellipse(P(bx + bw / 2 - 18, 166, bx + bw / 2 + 18, 202), fill=col)
        ctext(d, bx + bw / 2, 172, str(i + 1), B(20), WHITE)
        if i < len(schritte) - 1:
            arrow(d, bx + bw + 4, 136, bx + bw + gap - 4, 136, MUTED, 4, 12)
    ctext(d, 450, 232, "Nur EINE Bedingung ändern – alles andere gleich halten.", B(18), OLIVE)
    ctext(d, 450, 260, "Beobachtung (was gemessen wurde) und Erklärung (warum) immer trennen.", R(17), MUTED)
    save(im, IMG + "projekt.png")


# ================================================================ Versuchsskizzen der sieben Gruppen
def _vs(titel, zeichnen, name, h=330):
    im, d = canvas(760, h, WHITE)
    d.rounded_rectangle(P(6, 6, 754, h - 6), radius=12 * S, fill=WHITE, outline=GRID, width=int(2 * S))
    ctext(d, 380, 16, titel, B(19), OLIVE)
    zeichnen(d)
    save(im, VSI + "d_" + name + ".png")


def vs_g1(d):
    d.line(P(80, 230, 680, 230), fill=MUTED, width=int(3 * S))
    for x, lab in ((110, "Start"), (650, "Ziel")):
        d.line(P(x, 170, x, 250), fill=RED, width=int(4 * S)); ctext(d, x, 254, lab, B(16), RED)
    d.rectangle(P(110, 236, 650, 248), fill=LIGHT, outline=MUTED, width=int(2 * S))
    for x in range(110, 651, 54): d.line(P(x, 236, x, 248), fill=MUTED, width=int(2 * S))
    ctext(d, 380, 262, "s = 5,0 m (mit dem Bandmaß abgemessen)", R(16), INK)
    cx = 300
    d.ellipse(P(cx - 12, 120, cx + 12, 144), fill=(226, 196, 162), outline=INK, width=int(2 * S))
    d.line(P(cx, 144, cx, 190), fill=INK, width=int(4 * S))
    d.line(P(cx, 190, cx - 16, 228), fill=INK, width=int(4 * S)); d.line(P(cx, 190, cx + 20, 228), fill=INK, width=int(4 * S))
    d.line(P(cx, 158, cx + 26, 174), fill=INK, width=int(3 * S)); d.line(P(cx, 158, cx - 24, 176), fill=INK, width=int(3 * S))
    arrow(d, cx + 34, 150, cx + 110, 150, BLUE, 5, 14); ltext(d, cx + 46, 122, "geht normal", R(15), BLUE)
    d.rounded_rectangle(P(540, 110, 616, 180), radius=10 * S, fill=(50, 56, 62), outline=INK, width=int(2 * S))
    d.rounded_rectangle(P(548, 120, 608, 164), radius=4 * S, fill=(214, 232, 238))
    ctext(d, 578, 130, "00:04,1", B(15), INK); ctext(d, 578, 186, "Stoppuhr", R(15), MUTED)
    ctext(d, 380, 290, "v = s / t  ·  drei Durchgänge, derselbe Kadett geht, derselbe stoppt", B(17), OLIVE)


def vs_g2(d):
    d.rectangle(P(60, 278, 700, 292), fill=LIGHT, outline=MUTED, width=int(2 * S))
    d.line(P(250, 40, 250, 70), fill=MUTED, width=int(4 * S))
    d.rounded_rectangle(P(196, 70, 304, 140), radius=8 * S, fill=WHITE, outline=OLIVE, width=int(3 * S))
    d.rectangle(P(206, 86, 294, 108), fill=LIGHT, outline=MUTED, width=int(2 * S))
    for k in range(1, 5): d.line(P(206 + k * 18, 108, 206 + k * 18, 116), fill=MUTED, width=int(2 * S))
    d.line(P(242, 86, 242, 108), fill=RED, width=int(4 * S))
    ctext(d, 250, 118, "1,4 N", B(16), RED); ctext(d, 250, 38, "Federkraftmesser #51", B(15), OLIVE)
    d.arc(P(234, 134, 266, 162), start=0, end=180, fill=INK, width=int(4 * S))
    d.polygon([206 * S, 170 * S, 294 * S, 170 * S, 284 * S, 250 * S, 216 * S, 250 * S], fill=(226, 232, 238), outline=INK, width=int(2 * S))
    d.rectangle(P(220, 198, 280, 248), fill=WATER)
    d.line(P(206, 198, 294, 198), fill=TEAL, width=int(2 * S))
    d.arc(P(294, 172, 326, 200), start=270, end=90, fill=INK, width=int(4 * S))
    rtext(d, 192, 196, "Messbecher", R(15), MUTED); rtext(d, 192, 216, "250 ml PP", R(15), MUTED)
    d.rounded_rectangle(P(170, 262, 340, 280), radius=6 * S, fill=(236, 240, 246), outline=MUTED, width=int(2 * S))
    ctext(d, 255, 262, "Auffangwanne", R(14), MUTED)
    d.rounded_rectangle(P(460, 200, 640, 254), radius=8 * S, fill=(232, 236, 240), outline=INK, width=int(2 * S))
    d.rounded_rectangle(P(488, 212, 612, 240), radius=4 * S, fill=(214, 232, 238))
    ctext(d, 550, 216, "142,3 g", B(17), INK); ctext(d, 550, 262, "Schulwaage 620 g / 0,1 g", R(15), MUTED)
    arrow(d, 440, 150, 540, 190, MUTED, 4, 12)
    ctext(d, 420, 110, "erst wiegen (Masse in g),", B(16), OLIVE)
    ctext(d, 420, 132, "dann hängen (Kraft in N)", B(16), OLIVE)
    ctext(d, 380, 304, "100 ml Wasser mehr = ungefähr 1 N mehr Gewichtskraft", B(17), OLIVE)


def vs_g3(d):
    # Waage
    d.rounded_rectangle(P(150, 252, 410, 302), radius=8 * S, fill=(232, 236, 240), outline=INK, width=int(2 * S))
    d.rounded_rectangle(P(196, 262, 364, 290), radius=4 * S, fill=(214, 232, 238))
    ctext(d, 280, 266, "+ 2,1 g", B(17), RED)
    ctext(d, 280, 306, "Waage – vorher auf null gestellt", R(14), MUTED)
    # Becherglas mit Wasser
    d.polygon([206 * S, 116 * S, 356 * S, 116 * S, 346 * S, 250 * S, 216 * S, 250 * S], fill=GLASS, outline=INK, width=int(2 * S))
    d.rectangle(P(214, 148, 348, 248), fill=WATER)
    d.line(P(206, 148, 356, 148), fill=TEAL, width=int(3 * S))
    # Glasstab, von Hand gehalten
    d.rectangle(P(272, 62, 290, 208), fill=(238, 244, 246), outline=MUTED, width=int(2 * S))
    d.rectangle(P(274, 148, 288, 206), fill=(198, 220, 230))
    d.ellipse(P(262, 44, 300, 76), fill=(226, 196, 162), outline=INK, width=int(2 * S))
    # Eintauchtiefe links außerhalb des Glases
    d.line(P(158, 148, 204, 148), fill=GREEN, width=int(1.5 * S)); d.line(P(158, 206, 268, 206), fill=GREEN, width=int(1.5 * S))
    arrow(d, 170, 148, 170, 206, GREEN, 4, 11); arrow(d, 170, 206, 170, 148, GREEN, 4, 11)
    rtext(d, 154, 166, "4 cm", B(16), GREEN)
    # Kräftepaar
    arrow(d, 318, 212, 318, 156, TEAL, 5, 14)
    d.line(P(324, 158, 404, 158), fill=TEAL, width=int(1.5 * S))
    ltext(d, 410, 134, "Wasser drückt den", R(15), TEAL); ltext(d, 410, 154, "Stab nach oben", R(15), TEAL)
    arrow(d, 244, 156, 244, 212, RED, 5, 14)
    d.line(P(238, 214, 150, 214), fill=RED, width=int(1.5 * S))
    rtext(d, 146, 206, "Stab drückt das", R(15), RED); rtext(d, 146, 226, "Wasser nach unten", R(15), RED)
    # Hinweise rechts
    ltext(d, 410, 196, "Der Stab wird nicht", R(15), INK)
    ltext(d, 410, 216, "schwerer. Die Waage", R(15), INK)
    ltext(d, 410, 236, "zeigt die Gegenkraft.", B(16), RUST)
    ltext(d, 410, 60, "festhalten – nicht", B(15), OLIVE); ltext(d, 410, 80, "loslassen!", B(15), RUST)
    arrow(d, 404, 68, 308, 60, MUTED, 3, 10)
    ctext(d, 380, 330, "Stab darf Boden und Wand nicht berühren", B(16), RUST)


def vs_g4(d):
    d.rectangle(P(60, 230, 700, 246), fill=LIGHT, outline=MUTED, width=int(2 * S))
    for x in range(66, 698, 20): d.line(P(x, 246, x - 8, 258), fill=GRID, width=int(2 * S))
    d.polygon([150 * S, 140 * S, 266 * S, 140 * S, 252 * S, 228 * S, 164 * S, 228 * S], fill=(226, 232, 238), outline=INK, width=int(2 * S))
    d.rectangle(P(168, 176, 248, 226), fill=WATER)
    d.line(P(150, 176, 266, 176), fill=TEAL, width=int(2 * S))
    ctext(d, 208, 254, "Messbecher 500 ml, ca. 200 ml Wasser", R(15), MUTED)
    d.arc(P(262, 150, 300, 186), start=270, end=90, fill=INK, width=int(4 * S))
    d.rounded_rectangle(P(300, 148, 440, 196), radius=8 * S, fill=WHITE, outline=OLIVE, width=int(3 * S))
    d.rectangle(P(310, 160, 430, 180), fill=LIGHT, outline=MUTED, width=int(2 * S))
    for k in range(1, 7): d.line(P(310 + k * 17, 180, 310 + k * 17, 188), fill=MUTED, width=int(2 * S))
    d.line(P(362, 160, 362, 180), fill=RED, width=int(4 * S))
    ctext(d, 370, 202, "#52 · 10 N / 0,2 N", R(14), MUTED)
    arrow(d, 446, 172, 610, 172, GREEN, 6, 17); ctext(d, 530, 142, "waagrecht ziehen", B(17), GREEN)
    arrow(d, 164, 220, 80, 220, RUST, 5, 15); ltext(d, 66, 192, "F_R", B(17), RUST)
    d.rounded_rectangle(P(430, 36, 700, 118), radius=10 * S, fill=(248, 250, 244), outline=GRID, width=int(2 * S))
    ctext(d, 565, 44, "1. langsam steigern → größter Wert", R(16), INK)
    ctext(d, 565, 68, "   kurz vor dem Losgleiten", B(16), ORANGE)
    ctext(d, 565, 92, "2. dann gleichförmig ziehen → Gleitreibung", R(16), INK)
    ctext(d, 380, 290, "Nicht ruckartig ziehen und nicht schräg nach oben", B(17), RUST)


def vs_g5(d):
    wasser(d, 250, 170, 170, 120, 54)
    ctext(d, 335, 302, "Griffin-Becher 50 ml · 5 bis 10 mm Wasser", R(15), MUTED)
    for i, (x, t, hoehe) in enumerate([(286, "nach 10 s", 44), (348, "nach 60 s", 112)]):
        d.rectangle(P(x, 70, x + 34, 282), fill=(250, 248, 240), outline=MUTED, width=int(2 * S))
        d.rectangle(P(x + 2, 236 - hoehe, x + 32, 280), fill=(216, 232, 238))
        d.line(P(x, 236 - hoehe, x + 34, 236 - hoehe), fill=TEAL, width=int(3 * S))
        ctext(d, x + 17, 28 if i == 0 else 48, t, B(15), TEAL)
    d.line(P(220, 236, 460, 236), fill=TEAL, width=int(2 * S))
    rtext(d, 214, 226, "Wasserspiegel", R(15), MUTED)
    arrow(d, 470, 236, 470, 126, GREEN, 5, 14)
    ltext(d, 480, 150, "steigt über den", R(15), GREEN); ltext(d, 480, 170, "Wasserspiegel", R(15), GREEN)
    ctext(d, 600, 70, "Nur der untere", R(16), INK); ctext(d, 600, 92, "Rand (3 mm)", B(17), RUST)
    ctext(d, 600, 114, "steht im Wasser.", R(16), INK)
    ctext(d, 125, 110, "senkrecht", B(16), OLIVE); ctext(d, 125, 132, "halten", B(16), OLIVE)
    ctext(d, 380, 330, "kein Spülmittel, keine Farbe – nur Leitungswasser", B(16), RUST)


def vs_g6(d):
    for i, (y, offen, lab, col) in enumerate([(70, True, "Öffnung offen – Luft entweicht", GREEN), (190, False, "Öffnung mit dem Finger zu – Druck steigt", RUST)]):
        x = 150
        d.rounded_rectangle(P(x, y, x + 260, y + 60), radius=8 * S, fill=GLASS, outline=MUTED, width=int(2 * S))
        for k in range(1, 6): d.line(P(x + k * 43, y + 46, x + k * 43, y + 58), fill=MUTED, width=int(2 * S))
        kolben = x + (120 if offen else 92)
        d.rectangle(P(kolben, y + 2, kolben + 16, y + 58), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(kolben + 16, y + 22, x + 320, y + 38), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(x + 320, y + 4, x + 334, y + 56), fill=METAL, outline=INK, width=int(2 * S))
        d.rectangle(P(x - 30, y + 22, x, y + 38), fill=GLASS, outline=MUTED, width=int(2 * S))
        for k in range(8):
            px, py = x + 10 + (k % 4) * 26, y + 12 + (k // 4) * 26
            d.ellipse(P(px, py, px + 10, py + 10), fill=(196, 214, 226) if offen else TEAL)
        if offen:
            arrow(d, x - 36, y + 30, x - 96, y + 30, GREEN, 4, 12); ctext(d, x - 66, y + 2, "Luft raus", R(15), GREEN)
        else:
            d.ellipse(P(x - 54, y + 14, x - 20, y + 48), fill=(226, 196, 162), outline=INK, width=int(2 * S))
            arrow(d, kolben - 8, y + 30, kolben - 50, y + 30, RED, 5, 13)
            ltext(d, x + 100, y - 24, "Luft drückt zurück", B(16), RED)
        arrow(d, x + 356, y + 30, x + 300, y + 30, col, 5, 14)
        ctext(d, 380, y + 74, lab, B(16), col)
    ctext(d, 380, 290, "Keine Nadel · nie auf Personen richten · nicht mit Gewalt drücken", B(17), RUST)


def vs_g7(d):
    for i, (x, col, lab, who) in enumerate([(90, GREEN, "Kraftmesser #51", "Kadett A hält ruhig"), (390, ORANGE, "Kraftmesser #52", "Kadett B zieht langsam")]):
        d.rounded_rectangle(P(x, 120, x + 200, 196), radius=10 * S, fill=WHITE, outline=col, width=int(3 * S))
        d.rectangle(P(x + 14, 140, x + 186, 166), fill=LIGHT, outline=MUTED, width=int(2 * S))
        for k in range(1, 9): d.line(P(x + 14 + k * 19, 166, x + 14 + k * 19, 176), fill=MUTED, width=int(2 * S))
        d.line(P(x + 90, 140, x + 90, 166), fill=RED, width=int(5 * S))
        ctext(d, x + 100, 204, "2,0 N", B(20), RED)
        ctext(d, x + 100, 96, lab, B(16), col)
        ctext(d, x + 100, 236, who, R(16), MUTED)
    d.arc(P(272, 146, 310, 180), start=90, end=270, fill=INK, width=int(5 * S))
    d.arc(P(370, 146, 408, 180), start=270, end=90, fill=INK, width=int(5 * S))
    ctext(d, 340, 60, "Haken ineinander, beide in einer Linie", B(17), OLIVE)
    arrow(d, 70, 270, 150, 270, GREEN, 5, 14)
    arrow(d, 610, 270, 530, 270, ORANGE, 5, 14)
    ctext(d, 340, 266, "gleich groß, entgegengesetzt", B(17), OLIVE)
    ctext(d, 340, 300, "2 N und 2 N sind NICHT 4 N – es ist dieselbe Zugkraft", B(17), RUST)


# ================================================================ Icons
def icon(name, zeichnen):
    im = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    zeichnen(d)
    im.resize((180, 108), Image.LANCZOS).save(ICONS + name + ".png", optimize=True)
    print("   icon", name)


def ic_kraftmesser(d):
    d.rounded_rectangle(P(14, 32, 152, 72), radius=8 * S, fill=(255, 255, 255, 255), outline=(120, 128, 112, 255), width=int(2.5 * S))
    d.rectangle(P(26, 42, 140, 58), fill=(223, 229, 208, 255), outline=(150, 156, 142, 255), width=int(1.5 * S))
    for k in range(1, 7): d.line(P(26 + k * 16, 58, 26 + k * 16, 66), fill=(150, 156, 142, 255), width=int(1.5 * S))
    d.line(P(74, 42, 74, 58), fill=(163, 58, 43, 255), width=int(3 * S))
    d.arc(P(150, 40, 174, 64), start=270, end=90, fill=(110, 116, 124, 255), width=int(4 * S))
    d.arc(P(2, 40, 26, 64), start=90, end=270, fill=(110, 116, 124, 255), width=int(4 * S))
    d.line(P(90, 24, 90, 32), fill=(120, 128, 112, 255), width=int(2 * S))


def ic_messbecher(d):
    d.polygon([34 * S, 20 * S, 132 * S, 20 * S, 120 * S, 94 * S, 46 * S, 94 * S],
              fill=(226, 234, 238, 255), outline=(120, 128, 112, 255), width=int(2.5 * S))
    d.polygon([40 * S, 54 * S, 126 * S, 54 * S, 120 * S, 92 * S, 46 * S, 92 * S], fill=(167, 205, 222, 255))
    d.line(P(39, 54, 127, 54), fill=(46, 125, 140, 255), width=int(2.5 * S))
    for k, y in enumerate((34, 44, 64, 76)):
        d.line(P(44 + k, y, 70 + k, y), fill=(120, 128, 112, 255), width=int(1.5 * S))
    d.arc(P(126, 30, 162, 70), start=270, end=90, fill=(120, 128, 112, 255), width=int(4 * S))


def ic_messzylinder(d):
    d.rectangle(P(66, 14, 112, 92), fill=(226, 234, 238, 255), outline=(120, 128, 112, 255), width=int(2.5 * S))
    d.rectangle(P(69, 46, 109, 90), fill=(167, 205, 222, 255))
    d.line(P(66, 46, 112, 46), fill=(46, 125, 140, 255), width=int(2.5 * S))
    for y in (24, 34, 58, 70, 80):
        d.line(P(70, y, 90, y), fill=(120, 128, 112, 255), width=int(1.5 * S))
    d.polygon([54 * S, 92 * S, 124 * S, 92 * S, 118 * S, 100 * S, 60 * S, 100 * S],
              fill=(214, 220, 204, 255), outline=(120, 128, 112, 255), width=int(2 * S))
    d.line(P(62, 14, 116, 14), fill=(120, 128, 112, 255), width=int(2.5 * S))


def ic_spritze(d):
    d.rounded_rectangle(P(30, 40, 124, 70), radius=5 * S, fill=(226, 234, 238, 255), outline=(120, 128, 112, 255), width=int(2.5 * S))
    for k in range(1, 5): d.line(P(30 + k * 19, 62, 30 + k * 19, 70), fill=(150, 156, 142, 255), width=int(1.5 * S))
    d.rectangle(P(58, 42, 68, 68), fill=(176, 182, 190, 255), outline=(110, 116, 124, 255), width=int(2 * S))
    d.rectangle(P(68, 50, 152, 60), fill=(176, 182, 190, 255), outline=(110, 116, 124, 255), width=int(2 * S))
    d.rectangle(P(150, 38, 162, 72), fill=(176, 182, 190, 255), outline=(110, 116, 124, 255), width=int(2 * S))
    d.rectangle(P(18, 50, 30, 60), fill=(226, 234, 238, 255), outline=(120, 128, 112, 255), width=int(2 * S))
    d.rectangle(P(26, 36, 32, 74), fill=(214, 220, 204, 255), outline=(120, 128, 112, 255), width=int(2 * S))


NEUE_ICONS = {"kraftmesser": ic_kraftmesser, "messbecher": ic_messbecher, "messzylinder": ic_messzylinder, "spritze": ic_spritze}


def icons_kopieren():
    """Alle in versuche_daten verwendeten Icons nach vs-img/i_*.png kopieren."""
    gebraucht = sorted({m[1] for v in VD.VS for m in v["mat"]})
    for name in gebraucht:
        src = ICONS + name + ".png"
        assert os.path.exists(src), "Icon fehlt: " + src
        shutil.copyfile(src, VSI + "i_" + name + ".png")
    print("   Icons nach vs-img:", ", ".join(gebraucht))


if __name__ == "__main__":
    print("Icons:")
    for n, fn in NEUE_ICONS.items(): icon(n, fn)
    print("Bilder:")
    wirkung(); bewegung(); gewicht(); auftrieb(); reibung(); kapillar(); druck(); gegenkraft(); einheiten(); projekt()
    print("Versuchsskizzen:")
    _vs("Gruppe 1 · Weg und Zeit auf 5 m messen", vs_g1, "g1")
    _vs("Gruppe 2 · Masse wiegen, dann Gewichtskraft messen", vs_g2, "g2")
    _vs("Gruppe 3 · Glasstab eintauchen, Waage beobachten", vs_g3, "g3", 352)
    _vs("Gruppe 4 · Losgleiten und gleichförmiges Ziehen", vs_g4, "g4")
    _vs("Gruppe 5 · Filterpapierstreifen im Wasser", vs_g5, "g5", 352)
    _vs("Gruppe 6 · Spritze offen und geschlossen", vs_g6, "g6")
    _vs("Gruppe 7 · Zwei Kraftmesser ineinander", vs_g7, "g7")
    icons_kopieren()
