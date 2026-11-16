"""Eigene Grafiken (SVG) für NAWI 2AB K1.5 Säuren und Basen – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-5-saeuren/skizzen.py   → schreibt 2ab-nawi/k1-5-saeuren/img/*.svg
Handy zuerst: Hochformat, Breite 440, Schrift mindestens 17 (am Handy ca. 14 px). Animationen (SMIL) laufen auch in <img>; bei »weniger Bewegung« stehen sie still.
Farben der pH-Skala: übliche Universalindikator-Farben (ungefähr); Rotkraut-Farben ungefähr (Anthocyane, je nach Saft verschieden)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
IMG = os.path.join(ROOT, I.ORDNER, "img")
os.makedirs(IMG, exist_ok=True)

BG, INK, OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = "#F2F3EE", "#1F2A1C", "#3B4A2F", "#7FA83A", "#D9772B", "#2E7D8C", "#8C3B2E", "#5E6652"
RED, BLUE, LIGHT, WHITE = "#C0392B", "#2A5C8C", "#DFE5D0", "#FFFFFF"
O_COL, H_COL, CL_COL, N_COL, NA_COL = "#D9534F", "#FFFFFF", "#6BAF4A", "#4A7BD0", "#9B6FC4"
FONT = "'Source Sans 3','Carlito','Segoe UI',Arial,sans-serif"
STILL = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"
UI = ["#C62828", "#E53935", "#F4511E", "#FB8C00", "#FFB300", "#FDD835", "#C0CA33", "#7CB342", "#43A047", "#00897B", "#1E88E5", "#3949AB", "#5E35B1", "#6A1B9A", "#4A148C"]
RK = [(1, 2, "#C2185B", "stark sauer", "rot"), (3, 4, "#C2508A", "sauer", "rosa"), (5, 6, "#8A4C9E", "schwach sauer", "rotviolett"),
      (7, 7, "#5C5BA8", "neutral", "violett"), (8, 9, "#3F6FB5", "schwach basisch", "blau"), (10, 12, "#3E9A6A", "basisch", "grün"), (13, 14, "#D4C21A", "stark basisch", "gelb")]


def svg(w, h, body, title, anim=False):
    st = f"<style>text{{font-family:{FONT};fill:{INK}}} .b{{font-weight:700}} .m{{fill:{MUTED}}} {STILL if anim else ''}</style>"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{st}<rect width='{w}' height='{h}' rx='18' fill='{BG}'/>{body}</svg>")


def t(x, y, s, size=24, cls="", anchor="start", fill=None, weight=None):
    f = f" style='fill:{fill}'" if fill else ""
    w = f" font-weight='{weight}'" if weight else ""
    c = f" class='{cls}'" if cls else ""
    return f"<text x='{x}' y='{y}' font-size='{size}' text-anchor='{anchor}'{c}{f}{w}>{s}</text>"


def arrow(x1, y1, x2, y2, col=INK, w=4, head=14):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2 - 0.6 * head * math.cos(a):.1f}' y2='{y2 - 0.6 * head * math.sin(a):.1f}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<polygon points='{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{col}'/>")


def kreis(x, y, r, col, lab="", size=None, txt=INK):
    s = f"<circle cx='{x}' cy='{y}' r='{r}' fill='{col}' stroke='{INK}' stroke-width='2'/>"
    if lab: s += t(x, y + (size or int(r * 0.9)) * 0.36, lab, size or int(r * 0.9), "b", "middle", txt)
    return s


def wasser(x, y, s=1.0):
    """H2O: rotes O mit zwei H."""
    return (kreis(x - 22 * s, y + 16 * s, 11 * s, H_COL, "H", int(13 * s)) + kreis(x + 22 * s, y + 16 * s, 11 * s, H_COL, "H", int(13 * s))
            + kreis(x, y, 20 * s, O_COL, "O", int(18 * s), WHITE))


def oxonium(x, y, s=1.0):
    return (kreis(x - 24 * s, y + 14 * s, 11 * s, H_COL, "H", int(13 * s)) + kreis(x + 24 * s, y + 14 * s, 11 * s, H_COL, "H", int(13 * s))
            + kreis(x, y - 25 * s, 11 * s, H_COL, "H", int(13 * s)) + kreis(x, y, 20 * s, O_COL, "O", int(18 * s), WHITE)
            + t(x + 34 * s, y - 18 * s, "+", int(26 * s), "b", "middle", RED))


def hydroxid(x, y, s=1.0):
    return (kreis(x + 22 * s, y + 14 * s, 11 * s, H_COL, "H", int(13 * s)) + kreis(x, y, 20 * s, O_COL, "O", int(18 * s), WHITE)
            + t(x - 30 * s, y - 16 * s, "−", int(28 * s), "b", "middle", BLUE))


def proton(x, y, r=13):
    return kreis(x, y, r, RED, "H⁺", 15, WHITE)


def save(name, s):
    open(os.path.join(IMG, name), "w", encoding="utf-8").write(s)


# Alle Grafiken im Hochformat, Breite 440: am Handy (ca. 350 px) wird jede Schrift mindestens ca. 14 px groß.
W = 440
L, R, M = 20, 420, 220          # linker Rand, rechter Rand, Mitte


def kopf(titel, unter, farbe=None):
    b = [t(L, 42, titel, 30, "b", fill=farbe)]
    for k, z in enumerate(unter):
        b.append(t(L, 74 + k * 26, z, 20, "m"))
    return b


def balken(y, h, text, size=21, col=OLIVE, txtcol=WHITE):
    zeilen = text if isinstance(text, list) else [text]
    out = [f"<rect x='{L}' y='{y}' width='{R - L}' height='{h}' rx='12' fill='{col}'/>"]
    y0 = y + h / 2 - (len(zeilen) - 1) * size * 0.62 + size * 0.36
    for k, z in enumerate(zeilen):
        out.append(t(M, round(y0 + k * size * 1.24), z, size, "b", "middle", txtcol))
    return out


def linie(y):
    return f"<line x1='{L}' y1='{y}' x2='{R}' y2='{y}' stroke='{LIGHT}' stroke-width='3'/>"


# ---- Hilfen für Animationen in Schleife (SMIL: läuft in <img> und inline; in den Folien lässt sich der Lauf per Pause-Knopf anhalten).
# Grundregel: Das Grundbild (ohne Animation) zeigt den ENDZUSTAND; die Animation baut ihn Schritt für Schritt auf.
# Alle Spuren eines Bildes haben dieselbe Dauer und beginnen bei 0 s – dadurch laufen sie im Gleichtakt.
ZYK = 12          # Sekunden je Durchlauf
ENDE, ZURUECK = 0.96, 0.985   # ab ENDE ist die Szene ausgeblendet, bis ZURUECK springt alles unsichtbar auf den Start


def _spur(punkte):
    p = list(punkte)
    if p[0][0] != 0:
        p.insert(0, (0, p[0][1]))
    if p[-1][0] < ENDE:
        p.append((ENDE, p[-1][1]))
    return p + [(ZURUECK, p[0][1]), (1, p[0][1])]


def _werte(p):
    kt = ";".join(f"{a:.3f}" for a, _ in p)
    vals = ";".join(v if isinstance(v, str) else f"{v:.3g}" for _, v in p)
    return kt, vals


def blende(inner, punkte, dur=ZYK):
    """Gruppe mit Deckkraft-Verlauf. punkte = [(Zeitanteil 0–1, Deckkraft)]; Grundwert = letzter Punkt."""
    kt, vals = _werte(_spur(punkte))
    return (f"<g opacity='{punkte[-1][1]}'>{inner}"
            f"<animate attributeName='opacity' values='{vals}' keyTimes='{kt}' dur='{dur}s' repeatCount='indefinite'/></g>")


def bewege(inner, punkte, dur=ZYK):
    """Gruppe, die sich bewegt. punkte = [(Zeitanteil, 'x y')]; Grundlage = letzter Punkt (Endzustand)."""
    kt, vals = _werte(_spur(punkte))
    return (f"<g transform='translate({punkte[-1][1]})'>{inner}"
            f"<animateTransform attributeName='transform' type='translate' values='{vals}' keyTimes='{kt}' dur='{dur}s' repeatCount='indefinite'/></g>")


def szene(inner, dur=ZYK):
    """Ganze Szene: sichtbar bis ENDE, dann kurz aus, Rücksprung unsichtbar, wieder ein."""
    return (f"<g>{inner}<animate attributeName='opacity' values='1;1;0;0;1' keyTimes='0;{ENDE - 0.04:.3f};{ENDE};{ZURUECK};1' dur='{dur}s' repeatCount='indefinite'/></g>")


def bogen(p0, p1, p2, t0, t1, n=8):
    """Punkte entlang einer Kurve von p0 über Steuerpunkt p1 nach p2 (Zeit t0 → t1), für die Flugbahn des Protons."""
    out = []
    for i in range(n + 1):
        s = i / n
        x = (1 - s) ** 2 * p0[0] + 2 * s * (1 - s) * p1[0] + s * s * p2[0]
        y = (1 - s) ** 2 * p0[1] + 2 * s * (1 - s) * p1[1] + s * s * p2[1]
        out.append((round(t0 + (t1 - t0) * s, 3), f"{x:.1f} {y:.1f}"))
    return out


def _marke(punkte, dur=ZYK):
    """Nur der animateTransform-Teil (für ein Element, das selbst wandert, z. B. eine Linie)."""
    kt, vals = _werte(_spur(punkte))
    return f"<animateTransform attributeName='transform' type='translate' values='{vals}' keyTimes='{kt}' dur='{dur}s' repeatCount='indefinite'/>"


# ------------------------------------------------------------------ 1 Säure in Wasser (HCl gibt H⁺ an H2O) – ANIMIERT
def saeure():
    H = 720
    Y = 250
    b = kopf("Säure in Wasser", ["HCl gibt sein H⁺ an Wasser ab."])
    b.append(f"<rect x='{L}' y='104' width='{R - L}' height='44' rx='12' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
    s = []
    # drei Schritte als Überschrift, nacheinander
    for txt, pts in (("1  HCl trifft auf Wasser.", [(0, 1), (0.16, 1), (0.18, 0)]),
                     ("2  Das H⁺ springt zum Wasser.", [(0, 0), (0.19, 0), (0.22, 1), (0.38, 1), (0.40, 0)]),
                     ("3  Es entsteht H₃O⁺: sauer!", [(0, 0), (0.43, 0), (0.47, 1)])):
        s.append(blende(t(M, 133, txt, 21, "b", "middle"), pts))
    # Säurerest Cl (zuerst rechts neben dem Proton, am Ende links)
    cl = kreis(0, 0, 30, CL_COL, "Cl", 24, WHITE)
    cl += blende(t(38, -26, "−", 32, "b", "middle", BLUE), [(0, 0), (0.40, 0), (0.47, 1)])
    cl += blende(t(21, 66, "HCl", 24, "b", "middle"), [(0, 1), (0.38, 1), (0.41, 0)])
    cl += blende(t(0, 66, "Cl⁻", 24, "b", "middle"), [(0, 0), (0.42, 0), (0.47, 1)])
    cl += blende(t(0, 94, "Säurerest", 19, "m", "middle"), [(0, 0), (0.52, 0), (0.60, 1)])
    s.append(bewege(cl, [(0, f"95 {Y}"), (0.40, f"95 {Y}"), (0.55, f"80 {Y}")]))
    # Wasser kommt von rechts, nimmt das Proton auf und wird zum Oxonium-Ion
    w = blende(f"<circle cx='0' cy='-8' r='64' fill='{RED}'/>", [(0, 0), (0.58, 0), (0.68, 0.16), (0.80, 0.08), (0.92, 0.16)])
    w += kreis(-30, 17.5, 13.75, H_COL, "H", 16) + kreis(30, 17.5, 13.75, H_COL, "H", 16) + kreis(0, 0, 25, O_COL, "O", 22, WHITE)
    w += blende(t(38, -34, "+", 32, "b", "middle", RED), [(0, 0), (0.40, 0), (0.47, 1)])
    w += blende(t(0, 66, "H₂O", 24, "b", "middle"), [(0, 1), (0.38, 1), (0.41, 0)])
    w += blende(t(0, 66, "H₃O⁺", 24, "b", "middle"), [(0, 0), (0.42, 0), (0.47, 1)])
    w += blende(t(0, 94, "macht sauer", 19, "b", "middle", RED), [(0, 0), (0.52, 0), (0.60, 1)])
    s.append(bewege(w, [(0, f"360 {Y}"), (0.08, f"360 {Y}"), (0.18, f"300 {Y}"), (0.40, f"300 {Y}"), (0.55, f"330 {Y}")]))
    # das Proton: rot und „H⁺“ im Flug, nach der Landung ein ganz normales H im Oxonium-Ion
    pr = blende(kreis(0, 0, 15, RED, "H⁺", 15, WHITE), [(0, 1), (0.38, 1), (0.44, 0)]) + blende(kreis(0, 0, 13.75, H_COL, "H", 16), [(0, 0), (0.38, 0), (0.44, 1)])
    flug = [(0, f"137 {Y}"), (0.20, f"137 {Y}")] + bogen((137, Y), (218, 140), (300, Y - 31), 0.20, 0.38)[1:] + [(0.40, f"300 {Y - 31}"), (0.55, f"330 {Y - 31}")]
    s.append(bewege(pr, flug))
    s.append(blende(t(M, 412, "HCl + H₂O → Cl⁻ + H₃O⁺", 24, "b", "middle"), [(0, 0), (0.50, 0), (0.60, 1)]))
    b.append(szene("".join(s)))
    b.append(linie(452))
    b.append(t(L, 488, "Säuren im Alltag", 24, "b"))
    items = [("Zitrone", "Zitronensäure", "#F4D03F", "pH ~2,4"), ("Cola", "Phosphorsäure", "#5D4037", "pH ~2,5–3"),
             ("Mineralwasser", "Kohlensäure", "#AED6F1", "pH ~5–6"), ("Magen", "Salzsäure", "#E8A598", "pH 1–2")]
    for i, (n, s_, c, ph) in enumerate(items):
        x, y = L + (i % 2) * 204, 504 + (i // 2) * 106
        b.append(f"<rect x='{x}' y='{y}' width='196' height='96' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
        b.append(f"<circle cx='{x + 32}' cy='{y + 48}' r='20' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b += [t(x + 62, y + 32, n, 20 if len(n) < 12 else 18, "b"), t(x + 62, y + 56, s_, 17, "m"), t(x + 62, y + 82, ph, 19, "b", fill=RUST)]
    save("saeure.svg", svg(W, H, "".join(b), "Animation: HCl trifft auf Wasser, das H-plus springt zum Wassermolekül, es entstehen Cl-minus und H3O-plus; darunter Säuren im Alltag", anim=True))


# ------------------------------------------------------------------ 2 Lauge (NaOH in Wasser) + Alltag
def lauge():
    H = 700
    b = kopf("Lauge: OH⁻ macht basisch", ["Natriumhydroxid löst sich:", "Na⁺ und OH⁻ schwimmen getrennt."])
    # Kristall 3×3 (fest). Vier Teilchen (Ecke rechts) lösen sich ab und wandern ins Wasser – ANIMIERT.
    wandern = {(2, 0): ("na", 245, 168), (2, 1): ("oh", 345, 160), (2, 2): ("na", 360, 236), (1, 2): ("oh", 262, 240)}
    for r in range(3):
        for c in range(3):
            x, y = 50 + c * 40, 150 + r * 40
            if (c, r) in wandern: continue
            b.append(kreis(x, y, 17, NA_COL, "Na", 14, WHITE) if (r + c) % 2 == 0 else kreis(x, y, 17, O_COL, "OH", 13, WHITE))
    b.append(t(90, 290, "NaOH (fest)", 21, "b", "middle"))
    b.append(arrow(158, 190, 200, 190, OLIVE, 5))
    b.append(f"<rect x='205' y='122' width='{R - 205}' height='146' rx='14' fill='#E3F0F7' stroke='{TEAL}' stroke-width='3'/>")
    s_ = []
    for i, ((c, r), (k, bx, by)) in enumerate(wandern.items()):
        sx, sy = 50 + c * 40, 150 + r * 40
        t0 = 0.10 + 0.13 * i
        t1 = t0 + 0.22
        weg = [(0, f"{sx} {sy}"), (t0, f"{sx} {sy}"), (t1, f"{bx} {by}")]
        if k == "na":
            inner = kreis(0, 0, 17, NA_COL, "Na", 14, WHITE) + blende(t(22, -12, "+", 24, "b", "middle", RED), [(0, 0), (t1, 0), (t1 + 0.07, 1)])
        else:
            inner = (blende(kreis(0, 0, 17, O_COL, "OH", 13, WHITE), [(0, 1), (t1, 1), (t1 + 0.07, 0)])
                     + blende(hydroxid(0, 0, 0.8), [(0, 0), (t1, 0), (t1 + 0.07, 1)]))
        s_.append(bewege(inner, weg))
    b.append(szene("".join(s_)))
    b.append(t(312, 296, "Natronlauge", 21, "b", "middle", TEAL))
    b.append(linie(320))
    b.append(t(L, 358, "Laugen im Alltag und im Dienst", 24, "b"))
    items = [("Rohrreiniger", "pH über 13", "löst Haare, Fett – und Haut"), ("Laugenbrezel", "kurz in Lauge getaucht", "nach dem Backen harmlos"),
             ("nasser Beton", "pH 12–13", "Handschuhe und Brille!")]
    for i, (n, ph, s_) in enumerate(items):
        y = 376 + i * 104
        b.append(f"<rect x='{L}' y='{y}' width='{R - L}' height='94' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
        b += [t(L + 18, y + 36, n, 23, "b"), t(R - 18, y + 36, ph, 20, "b", "end", BLUE), t(L + 18, y + 72, s_, 19, "m")]
    save("lauge.svg", svg(W, H, "".join(b), "Animation: Natriumhydroxid löst sich, Na-plus und OH-minus wandern ins Wasser; Laugen im Alltag", anim=True))


# ------------------------------------------------------------------ 3 Protonen-Pingpong (animiert)
def protolyse():
    H = 720
    b = kopf("Protonen-Pingpong", ["Die Säure gibt ab, die Base fängt.", "Der rote Ball ist das Proton (H⁺)."])
    D = "3.2s"
    # Runde 1: HCl + H2O
    y1 = 230
    b.append(t(L, 140, "1   HCl + H₂O → Cl⁻ + H₃O⁺", 23, "b", fill=OLIVE))
    b += [kreis(80, y1, 30, CL_COL, "Cl", 24, WHITE), wasser(320, y1 - 8, 1.2)]
    b.append(f"<g><circle cx='124' cy='{y1}' r='15' fill='{RED}' stroke='{INK}' stroke-width='2'>"
             f"<animate attributeName='cx' values='124;124;320;320' keyTimes='0;0.25;0.6;1' dur='{D}' repeatCount='indefinite'/>"
             f"<animate attributeName='cy' values='{y1};{y1};{y1 - 42};{y1 - 42}' keyTimes='0;0.25;0.6;1' dur='{D}' repeatCount='indefinite'/></circle></g>")
    b.append(f"<path d='M140 {y1 - 26} Q 230 {y1 - 76} 304 {y1 - 48}' fill='none' stroke='{RED}' stroke-width='3' stroke-dasharray='8 7'/>")
    b += [t(80, y1 + 62, "Säure (gibt)", 20, "b", "middle", RED), t(320, y1 + 62, "Base (fängt)", 20, "b", "middle", BLUE)]
    b.append(linie(335))
    # Runde 2: H2O + NH3
    y2 = 440
    b.append(t(L, 376, "2   H₂O + NH₃ → OH⁻ + NH₄⁺", 23, "b", fill=OLIVE))
    b += [kreis(62, y2 + 10, 13, H_COL, "H", 15), kreis(90, y2 - 8, 24, O_COL, "O", 21, WHITE)]
    b += [kreis(320, y2, 28, N_COL, "N", 23, WHITE), kreis(282, y2 + 26, 13, H_COL, "H", 15), kreis(358, y2 + 26, 13, H_COL, "H", 15), kreis(320, y2 + 42, 13, H_COL, "H", 15)]
    b.append(f"<g><circle cx='118' cy='{y2 + 10}' r='15' fill='{RED}' stroke='{INK}' stroke-width='2'>"
             f"<animate attributeName='cx' values='118;118;320;320' keyTimes='0;0.25;0.6;1' dur='{D}' begin='0.4s' repeatCount='indefinite'/>"
             f"<animate attributeName='cy' values='{y2 + 10};{y2 + 10};{y2 - 42};{y2 - 42}' keyTimes='0;0.25;0.6;1' dur='{D}' begin='0.4s' repeatCount='indefinite'/></circle></g>")
    b += [t(90, y2 + 82, "Säure: Wasser!", 20, "b", "middle", RED), t(320, y2 + 82, "Base: Ammoniak", 20, "b", "middle", BLUE)]
    b.append(t(M, 568, "Nur ein kleiner Teil des Ammoniaks reagiert.", 18, "m", "middle"))
    b += balken(600, 96, ["Wasser kann beides:", "es ist ein Ampholyt."], 23)
    save("protolyse.svg", svg(W, H, "".join(b), "Protonenübergang: HCl gibt an Wasser ab, Wasser gibt an Ammoniak ab", anim=True))


# ------------------------------------------------------------------ 4 pH-Skala mit Beispielen (senkrecht)
def phskala():
    H = 930
    b = kopf("Die pH-Skala", ["unter 7 sauer · 7 neutral · über 7 basisch"])
    y0, h = 110, 46
    x0, bw = 120, 64
    bsp = {0: "", 1: "Magensaft (1–2)", 2: "Zitrone, Cola", 3: "Apfelsaft", 5: "Kaffee, Haut (um 5)", 7: "reines Wasser",
           8: "Blut 7,4 · Meer 8,1", 9: "Natron (um 8–9)", 10: "Kernseife (9–10)", 13: "nasser Beton (12–13)"}
    for i in range(15):
        y = y0 + i * h
        b.append(f"<rect x='{x0}' y='{y}' width='{bw}' height='{h + 0.6}' fill='{UI[i]}'/>")
        b.append(t(x0 + bw / 2, y + h / 2 + 9, str(i), 25, "b", "middle", WHITE if i not in (4, 5, 6) else INK))
        if bsp.get(i):
            b.append(f"<line x1='{x0 + bw + 4}' y1='{y + h / 2}' x2='{x0 + bw + 18}' y2='{y + h / 2}' stroke='{INK}' stroke-width='2'/>")
            b.append(t(x0 + bw + 24, y + h / 2 + 7, bsp[i], 20, "b"))
    b.append(f"<rect x='{x0}' y='{y0}' width='{bw}' height='{15 * h}' fill='none' stroke='{INK}' stroke-width='2'/>")
    b.append(arrow(60, y0 + 6.6 * h, 60, y0 + 0.4 * h, RED, 5))
    b.append(arrow(60, y0 + 8.4 * h, 60, y0 + 14.6 * h, BLUE, 5))
    b.append(f"<text transform='translate(40 {y0 + 3.5 * h}) rotate(-90)' font-size='22' font-weight='700' text-anchor='middle' style='fill:{RED}'>SAUER · mehr H₃O⁺</text>")
    b.append(f"<text transform='translate(40 {y0 + 11.5 * h}) rotate(-90)' font-size='22' font-weight='700' text-anchor='middle' style='fill:{BLUE}'>BASISCH · mehr OH⁻</text>")
    b.append(t(60, y0 + 7.5 * h + 8, "7", 22, "b", "middle", GREEN))
    b += balken(y0 + 15 * h + 18, 92, ["Jede Stufe = Faktor 10:", "pH 2 hat 1000-mal so viele", "H₃O⁺ wie pH 5"], 21)
    save("phskala.svg", svg(W, H, "".join(b), "pH-Skala von 0 bis 14 mit Beispielen aus Alltag und Körper"))


# ------------------------------------------------------------------ 5 Rotkraut-Farbskala (senkrecht)
def rotkraut():
    H = 640
    b = kopf("Rotkrautsaft als Indikator", ["Ungefähre Farben – jeder Saft", "ist ein bisschen anders."])
    for i, (a, e, c, wort, farbe) in enumerate(RK):
        y = 130 + i * 72
        b.append(f"<rect x='{L}' y='{y}' width='86' height='60' rx='12' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b.append(t(L + 104, y + 27, f"pH {a}" if a == e else f"pH {a}–{e}", 22, "b"))
        b.append(t(L + 104, y + 52, wort, 18, "m"))
        b.append(t(R, y + 38, farbe, 22, "b", "end"))
    save("rotkraut.svg", svg(W, H, "".join(b), "Farben des Rotkrautsafts von stark sauer rot bis stark basisch gelb"))


# ------------------------------------------------------------------ 6 Versuch: Ablauf
def versuch():
    H = 940
    b = kopf("VERSUCH K1.5-V1", ["So messt ihr – in 4 Schritten"], RUST)
    # 1 Tüpfelplatte
    b.append(t(L, 140, "1  Je ca. 10 Tropfen in eine Mulde", 21, "b"))
    b.append(f"<rect x='{L}' y='156' width='{R - L}' height='206' rx='16' fill='{WHITE}' stroke='{INK}' stroke-width='2'/>")
    proben = ["Zitrone", "Cola", "Mineral", "Leitung", "Natron", "Seife"]
    for i, p in enumerate(proben):
        cx, cy = 85 + (i % 3) * 135, 202 + (i // 3) * 96
        b.append(f"<circle cx='{cx}' cy='{cy}' r='26' fill='#EEF3F8' stroke='{MUTED}' stroke-width='2'/>")
        b += [t(cx, cy + 9, str(i + 1), 24, "b", "middle"), t(cx, cy + 50, p, 18, "m", "middle")]
    # 2 Papier
    b.append(t(L, 406, "2  Papier eintauchen, aufs Blatt legen", 21, "b"))
    farben = ["#E53935", "#F4511E", "#FDD835", "#7CB342", "#00897B", "#1E88E5"]
    for i, c in enumerate(farben):
        x = L + 14 + i * 66
        b.append(f"<rect x='{x}' y='422' width='38' height='84' rx='4' fill='#F3E9A8' stroke='{MUTED}' stroke-width='1.5'/>")
        b.append(f"<rect x='{x}' y='466' width='38' height='40' rx='4' fill='{c}'/>")
        b.append(t(x + 19, 534, str(i + 1), 21, "b", "middle"))
    # 3 Farbskala (Foto)
    b.append(t(L, 582, "3  Mit dem Foto der Farbskala vergleichen", 21, "b"))
    bw = (R - L) / 15
    for i in range(15):
        b.append(f"<rect x='{L + i * bw:.1f}' y='598' width='{bw + 0.5:.1f}' height='44' fill='{UI[i]}'/>")
        if i % 2 == 0: b.append(t(L + i * bw + bw / 2, 668, str(i), 18, "b", "middle"))
    # 4 eintragen + pH-Meter
    b.append(t(L, 714, "4  Werte eintragen (Aufgabe 6, c1–c6)", 21, "b"))
    b.append(f"<rect x='{L}' y='734' width='196' height='120' rx='16' fill='{OLIVE}'/>")
    b.append(f"<rect x='{L + 22}' y='750' width='152' height='50' rx='8' fill='#D7E8C0'/>")
    b.append(t(L + 98, 787, "2,5", 32, "b", "middle"))
    b.append(t(L + 98, 836, "pH-Meter", 22, "b", "middle", WHITE))
    b += [t(236, 772, "DEMO K1.5-D2:", 20, "b", fill=TEAL), t(236, 800, "Prof. HOLZER misst", 19), t(236, 826, "dieselben Proben.", 19)]
    b += balken(872, 46, "Papier schätzt · pH-Meter misst genauer", 20, RUST)
    save("versuch.svg", svg(W, H, "".join(b), "Ablauf des pH-Versuchs mit Tüpfelplatte, Indikatorpapier, Farbskala und pH-Meter"))


# ------------------------------------------------------------------ 7 Neutralisation (animiert)
def neutralisation():
    H = 700
    b = kopf("Neutralisation", ["Säure trifft Lauge: H₃O⁺ und OH⁻", "werden zu Wasser."])
    for x, lab, col in ((L, "Salzsäure", "#FBE3E0"), (226, "Natronlauge", "#E3ECF8")):
        b.append(f"<path d='M{x + 6} 120 v150 a14 14 0 0 0 14 14 h154 a14 14 0 0 0 14 -14 v-150' fill='{col}' stroke='{INK}' stroke-width='3'/>")
        b.append(t(x + 97, 316, lab, 22, "b", "middle"))
    b += [oxonium(78, 190, 0.9), kreis(150, 236, 20, CL_COL, "Cl", 17, WHITE), t(176, 216, "−", 26, "b", "middle", BLUE)]
    b += [hydroxid(290, 195, 0.95), kreis(366, 236, 20, NA_COL, "Na", 16, WHITE), t(392, 216, "+", 26, "b", "middle", RED)]
    b.append(linie(340))
    b.append(t(M, 390, "H₃O⁺ + OH⁻ → 2 H₂O", 30, "b", "middle"))
    b.append("<g opacity='0'><animate attributeName='opacity' values='0;0;1;1;0' keyTimes='0;0.35;0.5;0.9;1' dur='4s' repeatCount='indefinite'/>"
             + wasser(150, 450, 1.0) + wasser(290, 450, 1.0) + "</g>")
    b += [t(M, 530, "Na⁺ und Cl⁻ bleiben übrig:", 20, "b", "middle", OLIVE), t(M, 558, "Kochsalzlösung (ein Salz)", 20, "b", "middle", OLIVE)]
    b += balken(584, 96, ["Salzsäure + Natronlauge:", "Das Glas wird warm (exotherm)."], 21, ORANGE)
    save("neutralisation.svg", svg(W, H, "".join(b), "Salzsäure und Natronlauge neutralisieren sich zu Kochsalzlösung und Wasser", anim=True))


# ------------------------------------------------------------------ 8 Blut-Puffer
def blutpuffer():
    H = 860
    b = kopf("Dein Blut bleibt bei pH 7,4", ["Puffer fängt H⁺ ab –", "die Lunge atmet CO₂ aus."])
    box = [("Muskel", "bildet CO₂ und H⁺", "#F6D3CF"), ("Blut", "Puffer: HCO₃⁻ fängt H⁺", "#F3C6C6"), ("Lunge", "atmet CO₂ aus", "#D6E8F2")]
    for i, (n, s_, c) in enumerate(box):
        y = 124 + i * 96
        b.append(f"<rect x='{L}' y='{y}' width='{R - L}' height='72' rx='14' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b += [t(L + 18, y + 45, n, 25, "b"), t(R - 18, y + 45, s_, 19, "", "end")]
        if i < 2: b.append(arrow(M, y + 74, M, y + 94, INK, 4))
    b.append(t(M, 444, "HCO₃⁻ + H⁺ → H₂CO₃", 25, "b", "middle"))
    b.append(t(M, 476, "→ H₂O + CO₂", 25, "b", "middle"))
    b.append(t(M, 506, "Das CO₂ verlässt den Körper über die Lunge.", 18, "m", "middle"))
    x0, x1 = 40, 400
    def px(ph): return x0 + (ph - 6.8) / (7.8 - 6.8) * (x1 - x0)
    b.append(t(px(7.4), 556, "normal 7,35–7,45", 20, "b", "middle", OLIVE))
    b.append(f"<rect x='{x0}' y='568' width='{x1 - x0}' height='40' rx='6' fill='{LIGHT}'/>")
    b.append(f"<rect x='{px(7.35):.1f}' y='568' width='{px(7.45) - px(7.35):.1f}' height='40' fill='{GREEN}'/>")
    b.append(t(px(6.95), 595, "Azidose", 17, "b", "middle", RUST))
    b.append(t(px(7.66), 595, "Alkalose", 17, "b", "middle", BLUE))
    dx = round(px(7.4) - px(7.13), 1)
    b.append(f"<line x1='{px(7.13):.1f}' y1='562' x2='{px(7.13):.1f}' y2='614' stroke='{RED}' stroke-width='4'>"
             + _marke([(0, f"{dx} 0"), (0.12, f"{dx} 0"), (0.35, "0 0"), (0.55, "0 0"), (0.80, f"{dx} 0")]) + "</line>")
    for ph in (6.8, 7.0, 7.2, 7.4, 7.6, 7.8):
        b.append(t(px(ph), 636, str(ph).replace(".", ","), 18, "b", "middle"))
    b += [t(M, 670, "nach hartem Sprint: 7,13", 20, "b", "middle", RED), t(M, 696, "kurz und normal – die Atmung gleicht aus", 18, "", "middle", RED)]
    b += balken(720, 120, ["Schneller atmen = mehr CO₂ raus", "= weniger Kohlensäure"], 21)
    b.append(t(M, 822, "Studie: Radsportler, Med Sci Sports Exerc 2023", 15, "", "middle", "#E7EED8"))
    save("blutpuffer.svg", svg(W, H, "".join(b), "Muskel, Blut und Lunge halten den Blut-pH mit Puffer und Atmung bei 7,4; die rote Marke fällt beim Sprint auf 7,13 und kehrt zurück", anim=True))


# ------------------------------------------------------------------ 9 Überblick
def ueberblick():
    H = 760
    b = [t(M, 44, "Von sauer bis basisch", 30, "b", "middle")]
    for x, w, col, rnd, lab in ((L, 194, "#FBE3E0", RED, "SAUER"), (226, 194, "#E3ECF8", BLUE, "BASISCH")):
        b.append(f"<rect x='{x}' y='66' width='{w}' height='236' rx='16' fill='{col}' stroke='{rnd}' stroke-width='3'/>")
        b.append(t(x + w / 2, 102, lab, 26, "b", "middle", rnd))
    b += [oxonium(117, 160, 0.9), t(117, 222, "H₃O⁺", 24, "b", "middle"), t(117, 252, "pH unter 7", 19, "", "middle"), t(117, 280, "Lackmus rot", 19, "", "middle")]
    b += [hydroxid(323, 160, 1.0), t(323, 222, "OH⁻", 24, "b", "middle"), t(323, 252, "pH über 7", 19, "", "middle"), t(323, 280, "Lackmus blau", 19, "", "middle")]
    bw = (R - L) / 15
    for i in range(15):
        b.append(f"<rect x='{L + i * bw:.1f}' y='322' width='{bw + 0.5:.1f}' height='34' fill='{UI[i]}'/>")
    b.append(t(M, 384, "7 = neutral", 21, "b", "middle"))
    b.append(f"<rect x='{L}' y='404' width='{R - L}' height='158' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
    b += [t(M, 440, "Protonen-Pingpong", 23, "b", "middle"), proton(M, 486, 16), arrow(80, 486, 196, 486, RED, 3), arrow(244, 486, 360, 486, RED, 3),
          t(90, 534, "Säure gibt", 20, "b", "middle", RED), t(350, 534, "Base fängt", 20, "b", "middle", BLUE)]
    b.append(f"<rect x='{L}' y='578' width='{R - L}' height='164' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
    b += [t(M, 614, "Neutralisation", 23, "b", "middle"), t(M, 656, "H₃O⁺ + OH⁻ → 2 H₂O", 24, "b", "middle"),
          t(M, 690, "Säure + Lauge →", 19, "", "middle"), t(M, 716, "Salz + Wasser", 19, "", "middle")]
    save("ueberblick.svg", svg(W, H, "".join(b), "Überblick: sauer und basisch, pH-Skala, Protonenübergang und Neutralisation"))


# ------------------------------------------------------------------ 10 pH im Mund nach dem Essen (Zusatz 13)
# Verlauf vereinfacht nach der Stephan-Kurve (Stephan 1940er): pH fällt in 5–10 min unter den kritischen Wert 5,5,
# ohne Hilfe dauert die Erholung 30–60 min (DocCheck Flexikon »Stephan-Kurve«; Ernährungs-Umschau 10/2014, S. 41–44);
# zuckerfreier Kaugummi regt den Speichel an und verkürzt die Phase (Prophylaxe Journal 3/2016; zm-online 2010). Werte ungefähr.
KURVE_A = [(0, 6.8), (3, 6.0), (6, 5.3), (10, 4.9), (15, 5.0), (25, 5.4), (35, 5.8), (45, 6.2), (60, 6.6)]
KURVE_B = [(0, 6.8), (3, 6.0), (6, 5.3), (10, 4.9), (13, 5.3), (16, 5.8), (20, 6.3), (25, 6.7), (35, 6.9), (60, 6.9)]


def mundph():
    H = 620
    b = kopf("Säure-Alarm im Mund", ["pH-Wert am Zahn nach dem Essen", "zwei Kadetten, gleiches Essen"])
    x0, x1, y0, y1 = 70, 410, 140, 440            # Achsen: 0–60 min, pH 7,5 (oben) bis 4,5 (unten)
    def px(m): return x0 + m / 60 * (x1 - x0)
    def py(ph): return y0 + (7.5 - ph) / 3.0 * (y1 - y0)
    b.append(f"<rect x='{x0}' y='{py(5.5):.1f}' width='{x1 - x0}' height='{y1 - py(5.5):.1f}' fill='#F6D3CF'/>")
    for ph in (5, 6, 7):
        b.append(f"<line x1='{x0}' y1='{py(ph):.1f}' x2='{x1}' y2='{py(ph):.1f}' stroke='{LIGHT}' stroke-width='2'/>")
        b.append(t(x0 - 10, py(ph) + 7, str(ph), 20, "b", "end"))
    b.append(t(x0 - 10, py(7.5) + 4, "pH", 18, "m", "end"))
    b.append(f"<line x1='{x0}' y1='{py(5.5):.1f}' x2='{x1}' y2='{py(5.5):.1f}' stroke='{RED}' stroke-width='3' stroke-dasharray='10 7'/>")
    b.append(t(x1 - 4, py(5.5) - 10, "5,5 kritisch", 20, "b", "end", RED))
    b.append(t(x1 - 4, y1 - 14, "Zahnschmelz wird angegriffen", 18, "b", "end", RUST))
    b.append(f"<line x1='{x0}' y1='{y0}' x2='{x0}' y2='{y1}' stroke='{INK}' stroke-width='3'/>")
    b.append(f"<line x1='{x0}' y1='{y1}' x2='{x1}' y2='{y1}' stroke='{INK}' stroke-width='3'/>")
    for m in (0, 10, 20, 30, 40, 50, 60):
        b.append(f"<line x1='{px(m):.1f}' y1='{y1}' x2='{px(m):.1f}' y2='{y1 + 8}' stroke='{INK}' stroke-width='2'/>")
        b.append(t(px(m), y1 + 30, str(m), 19, "b", "middle"))
    b.append(t(M + 20, y1 + 58, "Minuten nach dem Essen", 19, "m", "middle"))
    b.append(arrow(px(0) + 14, y0 - 4, px(0) + 2, py(6.8) - 10, INK, 3, 11))
    b.append(t(px(0) + 18, y0 - 6, "Essen", 19, "b"))
    # Die Kurven zeichnen sich einmal von links nach rechts (eine Minute pro Sekunde) und bleiben dann stehen – Bildlauf per Beschneidung.
    b.append(f"<clipPath id='mphclip'><rect x='{x0 - 8}' y='{y0 - 20}' width='{x1 - x0 + 24}' height='{y1 - y0 + 40}'>"
             f"<animate attributeName='width' values='0;{x1 - x0 + 24}' dur='6s' fill='freeze'/></rect></clipPath>")
    for pts, col, dash, lab, ly in ((KURVE_A, RUST, "", "A", 6.45), (KURVE_B, TEAL, " stroke-dasharray='12 6'", "B", 7.15)):
        d = " ".join(f"{'M' if i == 0 else 'L'}{px(m):.1f},{py(ph):.1f}" for i, (m, ph) in enumerate(pts))
        b.append(f"<path d='{d}' fill='none' stroke='{col}' stroke-width='5' stroke-linejoin='round'{dash} clip-path='url(#mphclip)'/>")
        b.append(f"<g opacity='1'>{kreis(px(55), py(ly), 15, col, lab, 20, WHITE)}<animate attributeName='opacity' values='0;0;1' keyTimes='0;0.9;1' dur='6s' fill='freeze'/></g>")
    b += balken(530, 70, ["vereinfacht nach der Stephan-Kurve", "(Zahnmedizin) – Werte ungefähr"], 19)
    save("mundph.svg", svg(W, H, "".join(b), "pH-Wert am Zahn nach dem Essen: Kurve A und Kurve B fallen nach etwa 5 Minuten unter 5,5; Kurve B steigt ab Minute 10 schnell wieder, Kurve A erst nach etwa 30 Minuten", anim=True))


TEILE = {"saeure.svg": saeure, "lauge.svg": lauge, "protolyse.svg": protolyse, "phskala.svg": phskala, "rotkraut.svg": rotkraut,
         "versuch.svg": versuch, "neutralisation.svg": neutralisation, "blutpuffer.svg": blutpuffer, "ueberblick.svg": ueberblick, "mundph.svg": mundph}
if __name__ == "__main__":
    for n, f in TEILE.items():
        f()
    print("geschrieben:", ", ".join(TEILE))
