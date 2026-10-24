"""Bilder, Animationen, Versuchsskizzen und neue Icons für NAWI 2AB K1.3 Stoffumwandlung – alles selbst gezeichnet (keine Buchabbildungen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-3-reaktionen/skizzen.py
Schreibt 2ab-nawi/k1-3-reaktionen/img/*.png|gif, vs-img/d_v1–v9.png, vs-img/i_*.png und neue Icons nach werkzeug/icons/."""
import math, os, shutil
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, "2ab-nawi/k1-3-reaktionen/")
IMG, VSI, ICONS = UNIT + "img/", UNIT + "vs-img/", os.path.join(ROOT, "werkzeug/icons/")
for p in (IMG, VSI): os.makedirs(p, exist_ok=True)
FR = os.path.join(ROOT, "werkzeug/schriften/carlito-Regular.ttf")
FB = os.path.join(ROOT, "werkzeug/schriften/carlito-Bold.ttf")
BG, INK, RED, GREY, BLUE = (242, 243, 238), (59, 74, 47), (204, 0, 30), (122, 132, 145), (128, 170, 230)
OLIVE, GREEN, ORANGE, TEAL, RUST = (59, 74, 47), (127, 168, 58), (217, 119, 43), (46, 125, 140), (140, 59, 46)
CU, CUSO4, IRON, IRONW, RUSTC = (196, 110, 60), (70, 140, 215), (110, 115, 122), (150, 154, 160), (170, 85, 40)
S = 2
f = lambda p, s: ImageFont.truetype(p, int(s * S))


def canvas(w=900, h=629, bg=BG):
    im = Image.new("RGB", (w * S, h * S), bg); return im, ImageDraw.Draw(im)


def ctext(d, x, y, t, font, fill):
    w = d.textlength(t, font=font); d.text((x * S - w / 2, y * S), t, font=font, fill=fill)


def ltext(d, x, y, t, font, fill):
    d.text((x * S, y * S), t, font=font, fill=fill)


def P(*xy):
    return [v * S for v in xy]


def save(im, path, w=None, h=None, q=128):
    w = w or im.width // S; h = h or im.height // S
    im.resize((w, h), Image.LANCZOS).quantize(colors=q).save(path, optimize=True)


def arrow(d, x0, y0, x1, y1, col=INK, w=5, head=16):
    d.line(P(x0, y0, x1, y1), fill=col, width=w * S)
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1, y1), (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45)), (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))]
    d.polygon([(px * S, py * S) for px, py in pts], fill=col)


def darrow(d, x, y0, y1, col, w=5):
    """Doppelpfeil senkrecht (Energiedifferenz)."""
    arrow(d, x, (y0 + y1) / 2, x, y0, col, w); arrow(d, x, (y0 + y1) / 2, x, y1, col, w)


def beaker(d, x, y, w, h, fill=None, level=0.55, line=GREY):
    """Becherglas, (x, y) = linke obere Ecke."""
    if fill:
        d.rectangle(P(x + 5, y + h * (1 - level), x + w - 5, y + h - 5), fill=fill)
    d.line(P(x, y, x + 6, y + h), fill=line, width=5 * S); d.line(P(x + w, y, x + w - 6, y + h), fill=line, width=5 * S)
    d.line(P(x + 6, y + h, x + w - 6, y + h), fill=line, width=5 * S)
    d.line(P(x - 8, y, x, y), fill=line, width=5 * S)
    for k in range(1, 4):
        yy = y + h * k / 4; d.line(P(x + w - 30, yy, x + w - 10, yy), fill=(170, 176, 182), width=2 * S)


def thermometer(d, x, y, h, col=RED, fill=0.5, digital=False, txt=""):
    if digital:
        d.rounded_rectangle(P(x - 34, y, x + 34, y + 70), radius=10 * S, fill=(60, 66, 72), outline=GREY, width=3 * S)
        d.rectangle(P(x - 25, y + 10, x + 25, y + 38), fill=(200, 230, 200))
        ctext(d, x, y + 10, txt, f(FB, 20), (30, 40, 30))
        d.line(P(x, y + 70, x, y + h), fill=(150, 156, 162), width=6 * S)
        return
    d.rounded_rectangle(P(x - 9, y, x + 9, y + h), radius=9 * S, fill=(250, 250, 250), outline=GREY, width=3 * S)
    d.ellipse(P(x - 16, y + h - 14, x + 16, y + h + 18), fill=col, outline=GREY, width=3 * S)
    d.rectangle(P(x - 3, y + h * (1 - fill), x + 3, y + h), fill=col)


def tube(d, cx, top, bot, layers, width=60, label=None, font=None):
    x0, x1 = cx - width / 2, cx + width / 2
    y = bot - 10
    for hgt, col in layers:
        d.rectangle(P(x0 + 6, y - hgt, x1 - 6, y), fill=col); y -= hgt
    d.rounded_rectangle(P(x0, top, x1, bot), radius=width / 2 * S, outline=GREY, width=5 * S)
    d.rectangle(P(x0 - 6, top - 16, x1 + 6, top), fill=(242, 242, 242), outline=GREY, width=3 * S)
    if label: ctext(d, cx, top - 60, label, font or f(FB, 34), RED)


def wool(d, cx, cy, rx, ry, col=IRONW, n=70, seed=1):
    import random
    r = random.Random(seed)
    for _ in range(n):
        a = r.uniform(0, 2 * math.pi); b = a + r.uniform(1.0, 2.6)
        x0, y0 = cx + rx * r.uniform(0.2, 1) * math.cos(a), cy + ry * r.uniform(0.2, 1) * math.sin(a)
        x1, y1 = cx + rx * r.uniform(0.2, 1) * math.cos(b), cy + ry * r.uniform(0.2, 1) * math.sin(b)
        d.line(P(x0, y0, (x0 + x1) / 2 + r.uniform(-10, 10), (y0 + y1) / 2 + r.uniform(-10, 10), x1, y1), fill=col, width=2 * S, joint="curve")


def flame(d, cx, by, h=110, w=46):
    d.polygon(P(cx - w / 2, by, cx, by - h, cx + w / 2, by), fill=(120, 160, 235))
    d.polygon(P(cx - w / 4, by, cx, by - h * 0.55, cx + w / 4, by), fill=(70, 110, 220))


def burner(d, cx, by):
    d.rectangle(P(cx - 14, by - 120, cx + 14, by - 10), fill=(150, 156, 162), outline=GREY, width=3 * S)
    d.rectangle(P(cx - 50, by - 12, cx + 50, by), fill=(110, 116, 122), outline=GREY, width=3 * S)
    flame(d, cx, by - 120)


def bubbles(d, x0, x1, y0, y1, n=14, seed=3, col=(255, 255, 255)):
    import random
    r = random.Random(seed)
    for _ in range(n):
        x, y, s = r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(4, 9)
        d.ellipse(P(x - s, y - s, x + s, y + s), outline=col, width=2 * S)


# ============================================================ Theorie-Bilder
def welle(d, x, y0, y1, col=RED):
    pts = [(x + 9 * math.sin(k / 3.0), y0 - (y0 - y1) * k / 24) for k in range(25)]
    d.line([(px * S, py * S) for px, py in pts], fill=col, width=4 * S, joint="curve")
    arrow(d, pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1] - 6, col, 4, 14)


def handwaermer():
    im, d = canvas(900, 460)
    d.rounded_rectangle(P(80, 110, 400, 360), radius=30 * S, fill=(232, 236, 226), outline=GREY, width=5 * S)
    for i in range(170):
        x, y = 110 + (i * 37) % 260, 140 + (i * 53) % 200
        d.ellipse(P(x, y, x + 6, y + 6), fill=IRON)
    ctext(d, 240, 372, "Eisenpulver + Salz + Wasser + Aktivkohle", f(FR, 24), INK)
    for y in (160, 230, 300): arrow(d, 600, y, 420, y, TEAL, 5)
    ctext(d, 720, 200, "Sauerstoff", f(FB, 30), TEAL); ctext(d, 720, 236, "aus der Luft", f(FR, 26), TEAL)
    for x in (150, 240, 330): welle(d, x, 102, 48)
    ctext(d, 240, 8, "Wärme: über 50 °C", f(FB, 28), RED)
    ctext(d, 450, 418, "Eisen + Sauerstoff → Eisenoxid + Wärme", f(FB, 28), INK)
    save(im, IMG + "handwaermer.png")


def atom(d, cx, cy, r_shell, sym, col, core_col, n_e, offset=0, e_skip=()):
    d.ellipse(P(cx - r_shell, cy - r_shell, cx + r_shell, cy + r_shell), outline=(170, 176, 182), width=3 * S)
    d.ellipse(P(cx - 42, cy - 42, cx + 42, cy + 42), fill=core_col, outline=GREY, width=3 * S)
    ctext(d, cx, cy - 22, sym, f(FB, 36), (255, 255, 255))
    pos = []
    for k in range(n_e):
        a = offset + 2 * math.pi * k / max(n_e, 1)
        pos.append((cx + r_shell * math.cos(a), cy + r_shell * math.sin(a)))
    for k, (x, y) in enumerate(pos):
        if k in e_skip: continue
        d.ellipse(P(x - 11, y - 11, x + 11, y + 11), fill=TEAL, outline=(255, 255, 255), width=2 * S)
    return pos


def redox_gif():
    frames = []
    W, H = 900, 470
    mg, ox = (220, 230), (680, 230)
    N = 26
    for i in range(N + 14):
        im, d = canvas(W, H, (255, 255, 255))
        t = min(1, max(0, (i - 4) / (N - 8)))
        ctext(d, W / 2, 16, "Magnesium + Sauerstoff: Elektronen wandern", f(FB, 30), INK)
        mpos = atom(d, *mg, 120, "Mg", None, (150, 156, 162), 2, offset=-0.0, e_skip=(0, 1))
        opos = atom(d, *ox, 120, "O", None, RED, 8, offset=math.pi / 8, e_skip=(3, 4) if t < 1 else ())
        # 6 Außenelektronen des O (2 Lücken), 2 wandernde Elektronen vom Mg
        targets = [opos[3], opos[4]]
        for k, (sx, sy) in enumerate(mpos):
            tx, ty = targets[k]
            x = sx + (tx - sx) * t; y = sy + (ty - sy) * t - math.sin(math.pi * t) * (90 if k == 0 else -90)
            if t < 1: d.ellipse(P(x - 11, y - 11, x + 11, y + 11), fill=ORANGE, outline=(255, 255, 255), width=2 * S)
        if t >= 1:
            for k in (3, 4):
                x, y = opos[k]; d.ellipse(P(x - 11, y - 11, x + 11, y + 11), fill=ORANGE, outline=(255, 255, 255), width=2 * S)
            d.ellipse(P(mg[0] - 120, mg[1] - 120, mg[0] + 120, mg[1] + 120), fill=(255, 255, 255))
            d.ellipse(P(mg[0] - 42, mg[1] - 42, mg[0] + 42, mg[1] + 42), fill=(150, 156, 162), outline=GREY, width=3 * S)
            ctext(d, mg[0], mg[1] - 22, "Mg", f(FB, 36), (255, 255, 255))
            ctext(d, mg[0] + 66, mg[1] - 80, "2+", f(FB, 34), RUST); ctext(d, ox[0] + 150, ox[1] - 150, "2−", f(FB, 34), TEAL)
            ctext(d, mg[0], 380, "Oxidation: Mg → Mg²⁺ + 2 e⁻", f(FB, 26), RUST)
            ctext(d, ox[0], 380, "Reduktion: O + 2 e⁻ → O²⁻", f(FB, 26), TEAL)
            ctext(d, W / 2, 420, "Mg gibt 2 Elektronen ab – O nimmt sie auf", f(FR, 26), INK)
        else:
            ctext(d, mg[0], 380, "2 Außenelektronen", f(FR, 26), INK); ctext(d, ox[0], 380, "6 Außenelektronen", f(FR, 26), INK)
        frames.append(im.resize((W, H), Image.LANCZOS).convert("P", palette=Image.ADAPTIVE, colors=64))
    dur = [700] * 4 + [70] * (N - 4) + [2600] + [120] * 13
    frames[0].save(IMG + "redox_mg.gif", save_all=True, append_images=frames[1:], duration=dur[:len(frames)], loop=0, optimize=True)
    frames[-1].convert("RGB").save(IMG + "redox_mg_end.png")


def axes(d, x0, y0, w, h, lab=True):
    arrow(d, x0, y0 + h, x0, y0 - 10, INK, 4, 14); arrow(d, x0, y0 + h, x0 + w + 10, y0 + h, INK, 4, 14)
    if lab:
        im_txt = "Energie"
        for k, ch in enumerate(im_txt): pass
        ltext(d, x0 - 30, y0 - 42, "Energie", f(FB, 22), INK)
        ctext(d, x0 + w / 2, y0 + h + 8, "Verlauf der Reaktion", f(FR, 22), INK)


def curve(d, x0, x1, ya, yb, peak, col, w=6, dash=False):
    pts = []
    for i in range(101):
        t = i / 100; x = x0 + (x1 - x0) * t
        base = ya + (yb - ya) * (1 / (1 + math.exp(-(t - 0.5) * 14)))
        pts.append((x, base + (peak - base) * math.exp(-((t - 0.5) / 0.13) ** 2)))
    if dash:
        for i in range(0, 100, 4): d.line(P(*pts[i], *pts[i + 2]), fill=col, width=w * S)
    else:
        d.line([(x * S, y * S) for x, y in pts], fill=col, width=w * S, joint="curve")
    return pts


def levels(d, x0, w, ys):
    for yy in ys:
        for xx in range(int(x0), int(x0 + w), 18): d.line(P(xx, yy, xx + 9, yy), fill=(160, 166, 170), width=2 * S)


def diagramm(d, x0, y0, w, h, exo=True, numbers=None, title=None):
    """Energiediagramm mit Aktivierungsenergie (Pfeil am Gipfel) und Energiedifferenz (Pfeil rechts)."""
    axes(d, x0, y0, w, h)
    ya, yb = (y0 + h * 0.50, y0 + h * 0.85) if exo else (y0 + h * 0.85, y0 + h * 0.50)
    peak = y0 + h * 0.12
    cx0, cx1 = x0 + 20, x0 + w - 90
    curve(d, cx0, cx1, ya, yb, peak, ORANGE)
    px = (cx0 + cx1) / 2
    levels(d, x0, w, (ya, yb))
    d.line(P(px - 40, peak, px + 40, peak), fill=(160, 166, 170), width=2 * S)
    if exo:
        ltext(d, x0 + 8, ya + 6, "Ausgangsstoffe", f(FB, 20), INK); ltext(d, x0 + w - 98, yb - 30, "Endstoffe", f(FB, 20), INK)
    else:
        ltext(d, x0 + 8, ya - 30, "Ausgangsstoffe", f(FB, 20), INK); ltext(d, x0 + w - 98, yb - 30, "Endstoffe", f(FB, 20), INK)
    darrow(d, px, ya, peak, RED, 4)
    dx = x0 + w - 40
    darrow(d, dx, ya, yb, TEAL, 4)
    if numbers:
        for (x, y, n) in [(px + 10, (ya + peak) / 2 - 16, numbers[0]), (dx - 44, (ya + yb) / 2 - 16, numbers[1])]:
            d.ellipse(P(x, y - 2, x + 34, y + 32), fill=(255, 255, 255), outline=INK, width=3 * S); ctext(d, x + 17, y, n, f(FB, 24), INK)
    else:
        lx = px + 10 if exo else px - 135
        ltext(d, lx, (ya + peak) / 2 - 26, "Aktivierungs-", f(FB, 20), RED); ltext(d, lx, (ya + peak) / 2 - 4, "energie", f(FB, 20), RED)
        t1 = "frei werdende" if exo else "aufgenommene"
        ltext(d, dx - 140, (ya + yb) / 2 - 26, t1, f(FB, 20), TEAL); ltext(d, dx - 140, (ya + yb) / 2 - 4, "Energie", f(FB, 20), TEAL)
    if title: ctext(d, x0 + w / 2, y0 - 50, title, f(FB, 28), INK)


def diagramme():
    im, d = canvas(1000, 520, (255, 255, 255))
    diagramm(d, 60, 90, 400, 340, exo=True, title="exotherm")
    diagramm(d, 560, 90, 400, 340, exo=False, title="endotherm")
    save(im, IMG + "diagramm_exo_endo.png")
    im, d = canvas(1000, 520, (255, 255, 255))
    diagramm(d, 60, 90, 400, 340, exo=True, numbers=("1", "2"), title="A")
    x0, y0, w, h = 560, 90, 400, 340
    axes(d, x0, y0, w, h)
    ya, yb, peak = y0 + h * 0.85, y0 + h * 0.50, y0 + h * 0.12
    curve(d, x0 + 20, x0 + w - 90, ya, yb, peak, ORANGE)
    levels(d, x0, w, (ya, yb))
    ltext(d, x0 + 8, ya - 30, "Ausgangsstoffe", f(FB, 20), INK); ltext(d, x0 + w - 98, yb - 30, "Endstoffe", f(FB, 20), INK)
    dx = x0 + w - 40
    darrow(d, dx, ya, yb, TEAL, 4)
    d.ellipse(P(dx - 44, (ya + yb) / 2 - 18, dx - 10, (ya + yb) / 2 + 16), fill=(255, 255, 255), outline=INK, width=3 * S); ctext(d, dx - 27, (ya + yb) / 2 - 16, "3", f(FB, 24), INK)
    ctext(d, x0 + w / 2, y0 - 50, "B", f(FB, 28), INK)
    save(im, IMG + "a10_diagramme.png")
    im, d = canvas(1000, 560, (255, 255, 255))
    x0, y0, w, h = 120, 100, 780, 380
    axes(d, x0, y0, w, h)
    ya, yb = y0 + h * 0.50, y0 + h * 0.88
    cx0, cx1 = x0 + 30, x0 + w - 120
    curve(d, cx0, cx1, ya, yb, y0 + h * 0.06, ORANGE, 6, dash=True)
    curve(d, cx0, cx1, ya, yb, y0 + h * 0.32, GREEN, 7)
    levels(d, x0, w, (ya, yb))
    ltext(d, x0 + 10, ya + 8, "Ausgangsstoffe", f(FB, 22), INK); ltext(d, x0 + w - 120, yb - 32, "Endstoffe", f(FB, 22), INK)
    px = (cx0 + cx1) / 2
    darrow(d, px - 28, ya, y0 + h * 0.06, ORANGE, 4); darrow(d, px + 28, ya, y0 + h * 0.32, GREEN, 4)
    ltext(d, px - 290, y0 + h * 0.06, "ohne Katalysator", f(FB, 24), ORANGE)
    ltext(d, px + 70, y0 + h * 0.24, "mit Katalysator:", f(FB, 24), GREEN)
    ltext(d, px + 70, y0 + h * 0.24 + 30, "niedrigere Aktivierungsenergie", f(FR, 22), GREEN)
    ctext(d, x0 + w / 2, 20, "Ein Katalysator senkt den »Berg« – Anfang und Ende bleiben gleich", f(FB, 28), INK)
    save(im, IMG + "diagramm_kat.png")


def aktivierung_gif():
    W, H = 900, 440
    x0, x1 = 80, 840
    ya, yb, peak = 250, 380, 110
    def y_at(x):
        t = (x - x0) / (x1 - x0)
        base = ya + (yb - ya) * (1 / (1 + math.exp(-(t - 0.5) * 14)))
        return base + (peak - base) * math.exp(-((t - 0.5) / 0.13) ** 2)
    path = [x0 + 40 + k * 8 for k in range(int((x1 - x0 - 80) / 8))]
    frames, dur = [], []
    seq = [x0 + 60] * 5 + [x0 + 60 + (path[len(path) // 2] - x0 - 60) * (k / 20) ** 1.6 for k in range(21)] + path[len(path) // 2::3] + [path[-1]] * 6
    for i, bx in enumerate(seq):
        im, d = canvas(W, H, (255, 255, 255))
        pts = [(x, y_at(x)) for x in range(x0, x1 + 1, 4)]
        d.polygon([(x * S, y * S) for x, y in pts] + [(x1 * S, (H - 10) * S), (x0 * S, (H - 10) * S)], fill=(225, 233, 210))
        d.line([(x * S, y * S) for x, y in pts], fill=OLIVE, width=6 * S, joint="curve")
        by = y_at(bx) - 24
        d.ellipse(P(bx - 22, by - 22, bx + 22, by + 22), fill=ORANGE, outline=RUST, width=3 * S)
        ltext(d, x0, ya - 70, "Ausgangsstoffe", f(FB, 24), INK); ltext(d, x1 - 120, yb - 64, "Endstoffe", f(FB, 24), INK)
        pushing = 5 <= i < 26
        if pushing:
            arrow(d, bx - 80, by + 10, bx - 30, by, RED, 6); ctext(d, 260, 24, "Aktivierungsenergie zuführen (Streichholz, Funke)", f(FB, 26), RED)
        elif bx > path[len(path) // 2]:
            ctext(d, 520, 24, "Jetzt geht es von selbst bergab – Energie wird frei", f(FB, 26), TEAL)
            for k in range(3):
                yy = 180 + k * 40
                if bx > path[len(path) // 2] + 60: d.line(P(760 + k * 20, yy, 750 + k * 20, yy - 20, 770 + k * 20, yy - 40), fill=RED, width=4 * S, joint="curve")
        else:
            ctext(d, 450, 24, "Die Kugel liegt in einer Mulde – allein rollt sie nicht los", f(FB, 26), INK)
        frames.append(im.resize((W, H), Image.LANCZOS).convert("P", palette=Image.ADAPTIVE, colors=48))
        dur.append(700 if i < 5 else (2500 if i == len(seq) - 1 else 70))
    frames[0].save(IMG + "aktivierung.gif", save_all=True, append_images=frames[1:], duration=dur, loop=0, optimize=True)
    frames[-1].convert("RGB").save(IMG + "aktivierung_end.png")


def autokat():
    im, d = canvas(1000, 470, (255, 255, 255))
    d.rounded_rectangle(P(60, 170, 300, 250), radius=10 * S, fill=(200, 205, 210), outline=GREY, width=4 * S)
    d.rounded_rectangle(P(700, 170, 940, 250), radius=10 * S, fill=(200, 205, 210), outline=GREY, width=4 * S)
    d.rounded_rectangle(P(290, 110, 710, 310), radius=40 * S, fill=(178, 184, 190), outline=GREY, width=5 * S)
    d.rectangle(P(360, 140, 640, 280), fill=(240, 236, 226), outline=GREY, width=3 * S)
    for x in range(360, 641, 20): d.line(P(x, 140, x, 280), fill=(190, 186, 176), width=2 * S)
    for y in range(140, 281, 20): d.line(P(360, y, 640, y), fill=(190, 186, 176), width=2 * S)
    for x in range(370, 640, 40):
        for y in range(150, 280, 40): d.ellipse(P(x - 3, y - 3, x + 3, y + 3), fill=(120, 130, 150))
    arrow(d, 80, 210, 280, 210, RUST, 8, 24); arrow(d, 720, 210, 930, 210, GREEN, 8, 24)
    ctext(d, 180, 60, "hinein", f(FB, 28), RUST)
    for k, t in enumerate(["CO", "Stickoxide NOₓ", "Kohlenwasserstoffe"]): ctext(d, 180, 270 + k * 34, t, f(FR, 24), RUST)
    ctext(d, 820, 60, "hinaus", f(FB, 28), GREEN)
    for k, t in enumerate(["CO₂", "Stickstoff N₂", "Wasser H₂O"]): ctext(d, 820, 270 + k * 34, t, f(FR, 24), GREEN)
    ctext(d, 500, 40, "Keramikwabe mit Platin, Palladium, Rhodium", f(FB, 26), INK)
    ctext(d, 500, 420, "tausende feine Kanäle = riesige Oberfläche · arbeitet ab ca. 300 °C", f(FR, 24), INK)
    save(im, IMG + "autokat.png")


# ============================================================ Versuchsskizzen (900 × 629)
def balance(d, x, y, w=300, display="1,20 g"):
    d.rounded_rectangle(P(x, y + 90, x + w, y + 170), radius=14 * S, fill=(225, 228, 232), outline=GREY, width=4 * S)
    d.rectangle(P(x + w / 2 - 70, y + 110, x + w / 2 + 70, y + 150), fill=(200, 230, 200), outline=GREY, width=3 * S)
    ctext(d, x + w / 2, y + 112, display, f(FB, 30), (30, 50, 30))
    d.rectangle(P(x + 40, y + 70, x + w - 40, y + 90), fill=(200, 205, 210), outline=GREY, width=3 * S)


def v1():
    im, d = canvas()
    ctext(d, 450, 22, "Eisenwolle auf der Waage", f(FB, 34), INK)
    balance(d, 80, 220, 330, "1,20 g")
    d.chord(P(150, 230, 340, 330), 0, 180, fill=(250, 250, 250), outline=GREY, width=4 * S)
    wool(d, 245, 262, 70, 30, IRONW, 90)
    ctext(d, 245, 410, "vorher: tarieren, wiegen, tippen", f(FR, 26), INK)
    arrow(d, 440, 300, 510, 300, INK, 6, 20)
    balance(d, 530, 220, 330, "? g")
    d.chord(P(600, 230, 790, 330), 0, 180, fill=(250, 250, 250), outline=GREY, width=4 * S)
    wool(d, 695, 262, 70, 30, (70, 70, 85), 90, seed=4)
    for k in range(9):
        a = -math.pi / 2 + (k - 4) * 0.25; d.line(P(695 + 60 * math.cos(a), 240 + 60 * math.sin(a), 695 + 95 * math.cos(a), 240 + 95 * math.sin(a)), fill=ORANGE, width=3 * S)
    d.rectangle(P(790, 120, 860, 170), fill=(40, 60, 40), outline=GREY, width=3 * S); ctext(d, 825, 128, "4,5 V", f(FB, 22), (230, 190, 60))
    d.line(P(800, 170, 760, 240), fill=GREY, width=4 * S); d.line(P(850, 170, 790, 250), fill=GREY, width=4 * S)
    ctext(d, 695, 410, "Batterie kurz anhalten → glüht", f(FR, 26), INK)
    ctext(d, 450, 470, "Wird die Eisenwolle leichter, schwerer oder bleibt sie gleich?", f(FB, 28), RED)
    ctext(d, 450, 540, "Schutzbrille · nichts Brennbares in der Nähe · erst nach dem Abkühlen anfassen", f(FR, 24), INK)
    save(im, VSI + "d_v1.png")


def v2():
    im, d = canvas()
    ctext(d, 450, 20, "Rost-Ansätze: heute ansetzen, in 1 Woche auswerten", f(FB, 30), INK)
    xs = [150, 340, 530, 720]
    water, salt, oil = (180, 210, 240), (200, 215, 235), (244, 200, 80)
    tube(d, xs[0], 150, 470, [(150, water)], label="1")
    tube(d, xs[1], 150, 470, [(230, (190, 215, 245)), (35, oil)], label="2")
    tube(d, xs[2], 150, 470, [], label="3")
    tube(d, xs[3], 150, 470, [(150, salt)], label="4")
    for k, x in enumerate(xs):
        yy = 330 if k != 1 else 360
        if k == 2: yy = 400
        wool(d, x, yy, 22, 55, IRONW, 40, seed=k + 2)
    d.rectangle(P(xs[2] - 36, 128, xs[2] + 36, 140), fill=(230, 230, 230), outline=GREY, width=2 * S)
    for x, a, b in [(xs[0], "Leitungswasser", "+ Luft"), (xs[1], "abgekochtes Wasser", "unter Öl"), (xs[2], "trocken,", "Parafilm zu"), (xs[3], "Salzwasser", "+ Luft")]:
        ctext(d, x, 500, a, f(FB, 24), INK); ctext(d, x, 534, b, f(FR, 24), INK)
    ctext(d, 450, 585, "Eisenwolle statt Nagel – rostet schneller", f(FR, 24), INK)
    save(im, VSI + "d_v2.png")
    im2 = Image.open(VSI + "d_v2.png").convert("RGB"); im2.save(IMG + "rost_bedingungen.png")


def v3():
    im, d = canvas()
    ctext(d, 450, 20, "Der Kupferbrief", f(FB, 34), INK)
    d.polygon(P(70, 200, 230, 200, 230, 320, 70, 320), fill=CU, outline=GREY)
    d.line(P(150, 200, 150, 320), fill=(150, 80, 40), width=3 * S)
    ctext(d, 150, 340, "1 falten, Ränder", f(FR, 24), INK); ctext(d, 150, 370, "umbiegen, flach drücken", f(FR, 24), INK)
    burner(d, 450, 470)
    d.rectangle(P(410, 250, 490, 290), fill=(40, 40, 40), outline=GREY, width=2 * S)
    d.line(P(490, 270, 600, 220), fill=GREY, width=6 * S)
    ctext(d, 450, 500, "2 ca. 1 Minute", f(FR, 24), INK); ctext(d, 450, 530, "in die Flamme", f(FR, 24), INK)
    d.polygon(P(660, 210, 740, 260, 740, 330, 660, 280), fill=(40, 40, 40), outline=GREY)
    d.polygon(P(740, 260, 840, 210, 840, 280, 740, 330), fill=CU, outline=GREY)
    ctext(d, 700, 350, "außen", f(FB, 24), INK); ctext(d, 795, 350, "innen", f(FB, 24), INK)
    ctext(d, 750, 390, "3 abkühlen, aufklappen", f(FR, 24), INK)
    ctext(d, 450, 590, "Wie sieht der Brief innen aus? Erst tippen!", f(FB, 28), RED)
    save(im, VSI + "d_v3.png")


def station(d, x, y, sol, therm_txt=None, digital=False, therm_fill=0.45):
    beaker(d, x, y, 200, 220, sol, 0.45)
    thermometer(d, x + 140, y - 80, 260, fill=therm_fill, digital=digital, txt=therm_txt or "")


def v4():
    im, d = canvas()
    ctext(d, 450, 20, "Station 1 · Eisenwolle in Kupfersulfatlösung", f(FB, 32), INK)
    station(d, 120, 230, CUSO4, therm_fill=0.42)
    ctext(d, 220, 470, "vorher: Temperatur messen", f(FR, 24), INK)
    arrow(d, 360, 340, 470, 340, INK, 6, 20)
    beaker(d, 520, 230, 200, 220, (110, 165, 190), 0.45)
    wool(d, 600, 390, 50, 28, CU, 80, seed=7)
    thermometer(d, 660, 150, 260, fill=0.58)
    ctext(d, 620, 470, "Wolle untertauchen, 2 min", f(FR, 24), INK)
    ctext(d, 450, 520, "Wird es wärmer oder kälter? Was passiert mit der Wolle?", f(FB, 26), RED)
    ctext(d, 450, 570, "Schutzbrille + Handschuhe · Lösung in den Schwermetall-Behälter", f(FR, 24), INK)
    save(im, VSI + "d_v4.png")


def v5():
    im, d = canvas()
    ctext(d, 450, 20, "Station 2 · Zitronensäure und Natron", f(FB, 32), INK)
    station(d, 120, 230, (225, 236, 240), therm_fill=0.42)
    ctext(d, 220, 470, "vorher: Temperatur messen", f(FR, 24), INK)
    d.line(P(380, 200, 470, 280), fill=GREY, width=6 * S); d.ellipse(P(455, 270, 495, 300), fill=(250, 250, 250), outline=GREY, width=3 * S)
    ctext(d, 420, 160, "3 Spatel Natron", f(FB, 24), INK)
    beaker(d, 520, 230, 200, 220, (225, 236, 240), 0.62)
    bubbles(d, 535, 705, 320, 440, 26, seed=5, col=(140, 160, 170))
    thermometer(d, 660, 150, 260, fill=0.30)
    ctext(d, 620, 470, "sprudelt – tiefste Temperatur ablesen", f(FR, 24), INK)
    ctext(d, 450, 530, "Wird es wärmer oder kälter?", f(FB, 28), RED)
    ctext(d, 450, 575, "Schutzbrille · alles mit viel Wasser in den Ausguss", f(FR, 24), INK)
    save(im, VSI + "d_v5.png")


def v6():
    im, d = canvas()
    ctext(d, 450, 20, "Station 3 · Kältemischung aus Eis und Salz", f(FB, 32), INK)
    for (x, txt, salt) in [(110, "0 °C", False), (520, "? °C", True)]:
        beaker(d, x, 200, 230, 250, None)
        for k in range(14):
            cx, cy = x + 30 + (k % 5) * 38, 300 + (k // 5) * 45
            d.rectangle(P(cx, cy, cx + 30, cy + 30), fill=(205, 230, 245), outline=(140, 180, 210), width=2 * S)
        if salt:
            for k in range(40):
                cx, cy = x + 25 + (k * 37) % 180, 290 + (k * 53) % 140
                d.rectangle(P(cx, cy, cx + 5, cy + 5), fill=(255, 255, 255), outline=(160, 160, 160))
            for k in range(12):
                d.ellipse(P(x + 236 + (k % 2) * 6, 220 + k * 18, x + 244 + (k % 2) * 6, 228 + k * 18), fill=(255, 255, 255), outline=(190, 200, 210))
        thermometer(d, x + 180, 110, 230, digital=True, txt=txt)
    ctext(d, 225, 470, "Eis allein", f(FB, 26), INK); ctext(d, 635, 470, "Eis + 30 g Salz, kräftig rühren", f(FB, 26), INK)
    ctext(d, 450, 530, "Digitalthermometer – die Analog-Thermometer messen nur bis −10 °C", f(FR, 24), INK)
    ctext(d, 450, 572, "Wie kalt wird es? Was siehst du außen am Glas?", f(FB, 26), RED)
    save(im, VSI + "d_v6.png")


def v7():
    im, d = canvas()
    ctext(d, 450, 18, "Was beschleunigt den Zerfall von Wasserstoffperoxid?", f(FB, 30), INK)
    xs = [170, 350, 530, 710]
    h2o2 = (225, 238, 245)
    tube(d, xs[0], 160, 470, [(110, h2o2)], label="1")
    tube(d, xs[1], 160, 470, [(10, (60, 50, 45)), (100, h2o2), (150, (250, 250, 250))], label="2")
    tube(d, xs[2], 160, 470, [(110, h2o2), (60, (248, 248, 248))], label="3")
    tube(d, xs[3], 160, 470, [(110, h2o2)], label="4")
    bubbles(d, xs[1] - 22, xs[1] + 22, 230, 360, 18, 2, (190, 190, 190)); bubbles(d, xs[2] - 22, xs[2] + 22, 300, 400, 10, 4, (190, 190, 190))
    d.rectangle(P(xs[2] - 15, 430, xs[2] + 15, 455), fill=(235, 215, 150), outline=(170, 150, 90), width=2 * S)
    d.rectangle(P(xs[3] - 15, 430, xs[3] + 15, 455), fill=(225, 205, 160), outline=(150, 130, 90), width=2 * S)
    d.line(P(xs[1] + 120, 60, xs[1] + 6, 150), fill=(170, 130, 80), width=6 * S); d.ellipse(P(xs[1] - 6, 140, xs[1] + 14, 160), fill=ORANGE)
    ctext(d, xs[1] + 170, 60, "glimmender Span", f(FR, 22), INK)
    for x, a, b in [(xs[0], "ohne", "Zusatz"), (xs[1], "Braunstein", "(1 Spatelspitze)"), (xs[2], "rohe", "Kartoffel"), (xs[3], "gekochte", "Kartoffel")]:
        ctext(d, x, 495, a, f(FB, 24), INK); ctext(d, x, 527, b, f(FR, 22), INK)
    ctext(d, 450, 575, "je ca. 5 ml Wasserstoffperoxid 3 % · Schutzbrille · Gläser nicht verschließen", f(FR, 24), INK)
    save(im, VSI + "d_v7.png")


def v8():
    im, d = canvas()
    ctext(d, 450, 20, "Brausetablette im Test", f(FB, 34), INK)
    for k, (x, lab, warm, crushed) in enumerate([(160, "A · ganz, kalt", False, False), (450, "B · zerdrückt, kalt", False, True), (740, "C · ganz, warm", True, False)]):
        d.ellipse(P(x - 120, 200, x + 120, 330), fill=(255, 230, 220) if warm else (215, 232, 248), outline=GREY, width=5 * S)
        d.ellipse(P(x - 120, 190, x + 120, 310), outline=GREY, width=3 * S)
        if crushed:
            for j in range(40): cx, cy = x - 60 + (j * 29) % 120, 235 + (j * 17) % 50; d.ellipse(P(cx, cy, cx + 6, cy + 6), fill=(250, 250, 250), outline=(180, 180, 180))
        else:
            d.chord(P(x - 40, 230, x + 40, 290), 180, 360, fill=(250, 250, 250), outline=(170, 170, 170), width=3 * S)
            d.line(P(x - 40, 260, x + 40, 260), fill=(170, 170, 170), width=3 * S)
        bubbles(d, x - 90, x + 90, 215, 300, 10, k + 1, (150, 160, 170))
        ctext(d, x, 350, lab, f(FB, 26), INK)
        if warm: ctext(d, x, 385, "ca. 40 °C", f(FR, 24), RED)
    d.rounded_rectangle(P(390, 420, 510, 560), radius=16 * S, fill=(40, 46, 52), outline=GREY, width=3 * S)
    d.rectangle(P(402, 440, 498, 520), fill=(220, 235, 220)); ctext(d, 450, 460, "00:42", f(FB, 30), (30, 50, 30))
    ctext(d, 450, 585, "Handy als Stoppuhr: stoppen, wenn es nicht mehr sprudelt", f(FR, 24), INK)
    save(im, VSI + "d_v8.png")


def v9():
    im, d = canvas()
    ctext(d, 450, 20, "Kupferoxid und Holzkohle erhitzen (Lehrer-Demo)", f(FB, 30), INK)
    burner(d, 330, 520)
    d.polygon(P(210, 330, 470, 230, 482, 255, 222, 355), outline=GREY, fill=(245, 245, 245))
    d.polygon(P(222, 330, 300, 300, 310, 325, 232, 352), fill=(35, 35, 35))
    d.line(P(470, 240, 600, 190), fill=GREY, width=6 * S)
    ctext(d, 650, 170, "Halter", f(FR, 24), INK)
    ctext(d, 660, 300, "vorher: schwarz", f(FB, 26), INK)
    ctext(d, 660, 340, "nachher: rötliche Körnchen?", f(FB, 26), CU)
    ctext(d, 450, 570, "Öffnung von Personen weg · Fenster auf · vollständig abkühlen lassen", f(FR, 24), INK)
    save(im, VSI + "d_v9.png")


# ============================================================ neue Icons (180 × 108, transparent)
def icon(name, draw):
    ic = Image.new("RGBA", (180 * S, 108 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ic)
    draw(d); ic = ic.resize((180, 108), Image.LANCZOS)
    ic.save(ICONS + name + ".png", optimize=True)


OUT = (110, 115, 120)


def bottle(d, col, label=None, lc=(255, 255, 255)):
    d.rounded_rectangle(P(62, 30, 118, 98), radius=8 * S, fill=col, outline=OUT, width=2 * S)
    d.rectangle(P(78, 14, 102, 30), fill=(230, 232, 235), outline=OUT, width=2 * S)
    if label: d.rectangle(P(68, 52, 112, 76), fill=lc, outline=OUT, width=1 * S)


def jar(d, col, dots=None):
    d.rounded_rectangle(P(56, 28, 124, 98), radius=10 * S, fill=(245, 246, 248), outline=OUT, width=2 * S)
    d.rectangle(P(52, 18, 128, 30), fill=(200, 205, 210), outline=OUT, width=2 * S)
    d.rounded_rectangle(P(62, 56, 118, 94), radius=6 * S, fill=col)
    if dots:
        for k in range(14): x, y = 66 + (k * 13) % 48, 60 + (k * 7) % 30; d.ellipse(P(x, y, x + 5, y + 5), fill=dots)


def new_icons():
    def waage(d):
        d.rounded_rectangle(P(28, 56, 152, 96), radius=8 * S, fill=(225, 228, 232), outline=OUT, width=2 * S)
        d.rectangle(P(58, 66, 122, 86), fill=(200, 230, 200), outline=OUT, width=1 * S)
        d.rectangle(P(44, 46, 136, 56), fill=(200, 205, 210), outline=OUT, width=2 * S)
    icon("waage", waage)
    icon("eisenwolle", lambda d: wool(d, 90, 56, 52, 30, IRONW, 70))
    def schale(d):
        d.chord(P(30, 20, 150, 96), 0, 180, fill=(250, 250, 250), outline=OUT, width=2 * S); d.line(P(30, 58, 150, 58), fill=OUT, width=2 * S)
    icon("schale", schale)
    def kupferblech(d):
        d.polygon(P(36, 30, 140, 22, 150, 82, 44, 92), fill=CU, outline=OUT); d.line(P(50, 40, 120, 34), fill=(225, 150, 100), width=3 * S)
    icon("kupferblech", kupferblech)
    def digi(d):
        d.rounded_rectangle(P(30, 30, 100, 78), radius=8 * S, fill=(60, 66, 72), outline=OUT, width=2 * S)
        d.rectangle(P(38, 38, 92, 60), fill=(200, 230, 200)); d.line(P(100, 54, 156, 54), fill=(170, 176, 182), width=5 * S)
    icon("digitalthermometer", digi)
    icon("kupfersulfat", lambda d: bottle(d, CUSO4, True))
    def handschuhe(d):
        d.rounded_rectangle(P(50, 40, 100, 98), radius=14 * S, fill=(120, 150, 220), outline=OUT, width=2 * S)
        for k in range(4): d.rounded_rectangle(P(50 + k * 13, 14 + (k % 2) * 6, 61 + k * 13, 50), radius=5 * S, fill=(120, 150, 220), outline=OUT, width=2 * S)
        d.rounded_rectangle(P(96, 50, 122, 66), radius=7 * S, fill=(120, 150, 220), outline=OUT, width=2 * S)
    icon("handschuhe", handschuhe)
    icon("zitronensaeure", lambda d: bottle(d, (245, 240, 200), True, (250, 220, 60)))
    icon("natron", lambda d: jar(d, (250, 250, 250), (200, 200, 200)))
    icon("wasserstoffperoxid", lambda d: bottle(d, (225, 238, 245), True, (230, 120, 40)))
    icon("braunstein", lambda d: jar(d, (70, 55, 45), (40, 30, 25)))
    def kartoffel(d):
        d.ellipse(P(36, 30, 112, 86), fill=(200, 160, 100), outline=OUT, width=2 * S)
        for x, y in [(56, 44), (80, 60), (96, 46)]: d.ellipse(P(x, y, x + 5, y + 5), fill=(150, 110, 60))
        d.rectangle(P(118, 46, 152, 80), fill=(245, 225, 160), outline=OUT, width=2 * S)
    icon("kartoffel", kartoffel)
    def holzspan(d):
        d.line(P(26, 86, 146, 26), fill=(200, 160, 100), width=7 * S); d.ellipse(P(138, 18, 156, 34), fill=ORANGE)
    icon("holzspan", holzspan)
    def brause(d):
        d.rounded_rectangle(P(30, 30, 92, 92), radius=31 * S, fill=(250, 250, 250), outline=OUT, width=2 * S); d.line(P(36, 61, 86, 61), fill=OUT, width=2 * S)
        d.rounded_rectangle(P(104, 20, 150, 98), radius=8 * S, fill=(240, 140, 60), outline=OUT, width=2 * S)
    icon("brausetablette", brause)
    icon("kupferoxid", lambda d: jar(d, (35, 35, 35), (10, 10, 10)))
    icon("holzkohle", lambda d: jar(d, (50, 50, 50), (90, 90, 90)))


def icons_kopieren():
    from versuche_daten import VS
    used = {m[1] for v in VS for m in v["mat"]}
    for n in used:
        src = ICONS + n + ".png"
        assert os.path.exists(src), "Icon fehlt: " + n
        shutil.copy(src, VSI + "i_" + n + ".png")
    return used


if __name__ == "__main__":
    import sys; sys.path.insert(0, HERE)
    handwaermer(); redox_gif(); diagramme(); aktivierung_gif(); autokat()
    for fn in (v1, v2, v3, v4, v5, v6, v7, v8, v9): fn()
    new_icons()
    print("Icons:", len(icons_kopieren()))
    print("ok")
