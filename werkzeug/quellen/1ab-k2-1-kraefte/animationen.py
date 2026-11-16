"""Animierte Grafiken (SVG mit SMIL) für NAWI 1AB K2.1 Mechanische Kräfte – neue Standards 16.11.2026: Zeigt eine Grafik einen VORGANG,
wird sie animiert. Selbst gezeichnet, kein Fremdserver, kein GIF. Muster: werkzeug/quellen/2ab-k1-5-saeuren/skizzen.py (blende, bewege, szene).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k2-1-kraefte/animationen.py   → schreibt 1ab-nawi/k2-1-kraefte/img/*.svg

Prüfbericht »Welche Grafiken zeigen einen Vorgang?«
  wirkung, bewegung, auftrieb, reibung, kapillar, druck, gegenkraft → animiert (diese Datei)
  gewicht (Erde und Mond im Vergleich – zwei Zustände), einheiten (Tabelle), projekt (Überblick) → bewusst ruhig (PNG aus skizzen.py)
Regeln: Hochformat 440 breit; das Grundbild (ohne Animation) zeigt den ENDZUSTAND; alle Spuren eines Bildes dauern gleich lang (ZYK) und beginnen bei 0 s;
drei Schritte als Überschrift im Bild (Schrift mind. 20); Nachschlage-Teile bleiben ruhig. Zahlen wie in inhalt.py (g = 10 N/kg, 600 N, 0,03 m² / 0,30 m², 2 N)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
IMG = os.path.join(ROOT, I.ORDNER, "img")
os.makedirs(IMG, exist_ok=True)

BG, INK, OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = "#F2F3EE", "#1F2A1C", "#3B4A2F", "#7FA83A", "#D9772B", "#2E7D8C", "#8C3B2E", "#5E6652"
RED, BLUE, LIGHT, WHITE, GRID = "#A33A2B", "#2A5C8C", "#DFE5D0", "#FFFFFF", "#CED6C4"
WATER, GLASS, METAL, WOOD, SNOW = "#A7CDDE", "#DEEAEE", "#B0B6BE", "#CEB080", "#FBFCFD"
FONT = "'Source Sans 3','Carlito','Segoe UI',Arial,sans-serif"
W, L, R, M = 440, 20, 420, 220
ZYK = 12
ENDE, ZURUECK = 0.96, 0.985


def svg(h, body, title):
    # Stil nur für diese Grafik (Klasse k21a) – wichtig, wenn das SVG inline in der Präsentation steht
    st = f"<style>.k21a text{{font-family:{FONT};fill:{INK}}} .k21a .b{{font-weight:700}} .k21a .m{{fill:{MUTED}}}</style>"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="k21a" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{st}<rect width='{W}' height='{h}' rx='18' fill='{BG}'/>{''.join(body)}</svg>")


def t(x, y, s, size=20, cls="", anchor="start", fill=None):
    f = f" style='fill:{fill}'" if fill else ""
    c = f" class='{cls}'" if cls else ""
    return f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' text-anchor='{anchor}'{c}{f}>{s}</text>"


def F(idx):
    """F mit Index als tspan (F_A, F_G, F_R)."""
    return f"F<tspan font-size='70%' dy='5'>{idx}</tspan>"


def arrow(x1, y1, x2, y2, col=INK, w=5, head=15):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2 - 0.6 * head * math.cos(a):.1f}' y2='{y2 - 0.6 * head * math.sin(a):.1f}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<polygon points='{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{col}'/>")


def _spur(punkte):
    p = list(punkte)
    if p[0][0] != 0: p.insert(0, (0, p[0][1]))
    if p[-1][0] < ENDE: p.append((ENDE, p[-1][1]))
    return p + [(ZURUECK, p[0][1]), (1, p[0][1])]


def _werte(p):
    return ";".join(f"{a:.3f}" for a, _ in p), ";".join(v if isinstance(v, str) else f"{v:.4g}" for _, v in p)


def blende(inner, punkte):
    kt, vals = _werte(_spur(punkte))
    return f"<g opacity='{punkte[-1][1]}'>{inner}<animate attributeName='opacity' values='{vals}' keyTimes='{kt}' dur='{ZYK}s' repeatCount='indefinite'/></g>"


def bewege(inner, punkte):
    """punkte = [(Zeitanteil, (dx, dy))]; Grundlage = letzter Punkt (Endzustand)."""
    pp = [(a, f"{v[0]:.1f} {v[1]:.1f}") for a, v in punkte]
    kt, vals = _werte(_spur(pp))
    return (f"<g transform='translate({pp[-1][1]})'>{inner}"
            f"<animateTransform attributeName='transform' type='translate' values='{vals}' keyTimes='{kt}' dur='{ZYK}s' repeatCount='indefinite'/></g>")


def drehe(inner, punkte):
    """punkte = [(Zeitanteil, Winkel in Grad)] – Drehung um den Ursprung der Gruppe."""
    pp = [(a, f"{v:.1f}") for a, v in punkte]
    kt, vals = _werte(_spur(pp))
    return (f"<g transform='rotate({pp[-1][1]})'>{inner}"
            f"<animateTransform attributeName='transform' type='rotate' values='{vals}' keyTimes='{kt}' dur='{ZYK}s' repeatCount='indefinite'/></g>")


def skaliere(inner, punkte):
    """punkte = [(Zeitanteil, (sx, sy))] – um den Ursprung der Gruppe."""
    pp = [(a, f"{v[0]:.3f} {v[1]:.3f}") for a, v in punkte]
    kt, vals = _werte(_spur(pp))
    return (f"<g transform='scale({pp[-1][1]})'>{inner}"
            f"<animateTransform attributeName='transform' type='scale' values='{vals}' keyTimes='{kt}' dur='{ZYK}s' repeatCount='indefinite'/></g>")


def attr(name, punkte):
    """Animation eines Attributs (z. B. y, height) – der Grundwert steht am Element selbst (Endzustand)."""
    kt, vals = _werte(_spur(punkte))
    return f"<animate attributeName='{name}' values='{vals}' keyTimes='{kt}' dur='{ZYK}s' repeatCount='indefinite'/>"


def szene(inner):
    return f"<g>{inner}<animate attributeName='opacity' values='1;1;0;0;1' keyTimes='0;{ENDE - 0.04:.3f};{ENDE};{ZURUECK};1' dur='{ZYK}s' repeatCount='indefinite'/></g>"


def ein(t0, t1=None):
    """Deckkraft: unsichtbar bis t0, sichtbar ab t0 (+0,03) – optional wieder aus bei t1."""
    p = [(0, 0), (t0, 0), (min(t0 + 0.03, 0.95), 1)]
    if t1 is not None: p += [(t1, 1), (t1 + 0.03, 0)]
    return p


def kopf(titel, unter, schritte):
    """Titel, eine Unterzeile und drei Schritte nacheinander im Kasten (Schrift 21)."""
    b = [t(L, 40, titel, 30, "b"), t(L, 70, unter, 20, "m"),
         f"<rect x='{L}' y='86' width='{R - L}' height='46' rx='12' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>"]
    s = []
    for k, (txt, a, z) in enumerate(schritte):
        p = [(0, 1 if a == 0 else 0)] + ([(a + 0.025, 0), (a + 0.05, 1)] if a > 0 else []) + ([(z, 1), (z + 0.025, 0)] if z is not None else [])
        s.append(blende(t(M, 116, f"{k + 1}  {txt}", 21, "b", "middle"), p))
    return b, s


def label(x, y, txt, col, size=20, anchor="start"):
    return t(x, y, txt, size, "b", anchor, col)


def kasten(y, h, titel, col):
    return (f"<rect x='{L}' y='{y}' width='{R - L}' height='{h}' rx='14' fill='{WHITE}' stroke='{col}' stroke-width='3'/>"
            + f"<rect x='{L}' y='{y}' width='{R - L}' height='30' rx='14' fill='{col}'/><rect x='{L}' y='{y + 16}' width='{R - L}' height='14' fill='{col}'/>"
            + t(M, y + 22, titel, 19, "b", "middle", WHITE))


def save(name, s):
    open(os.path.join(IMG, name), "w", encoding="utf-8").write(s)
    return name


# ------------------------------------------------------------------ 1 Was eine Kraft bewirkt
def wirkung():
    H = 640
    b, s = kopf("Was eine Kraft bewirkt", "Eine Kraft ändert Bewegung oder Form.",
                [("Die Kraft macht den Wagen schneller.", 0, 0.32), ("Die Kraft lenkt ihn in die Kurve.", 0.32, 0.64), ("Die Kraft verformt den Ball.", 0.64, None)])
    # A: Tempo ändern
    b.append(kasten(146, 140, "Tempo ändern", GREEN))
    b.append(f"<line x1='{L + 10}' y1='262' x2='{R - 10}' y2='262' stroke='{GRID}' stroke-width='4'/>")
    wagen = (f"<rect x='0' y='-36' width='64' height='30' rx='6' fill='{WOOD}' stroke='{MUTED}' stroke-width='2'/>"
             f"<circle cx='14' cy='-6' r='8' fill='{METAL}' stroke='{INK}' stroke-width='2'/><circle cx='50' cy='-6' r='8' fill='{METAL}' stroke='{INK}' stroke-width='2'/>"
             + arrow(66, -21, 112, -21, RED, 5, 14) + label(116, -14, "F", RED))
    for k, (ln, a, z) in enumerate(((22, 0, 0.1), (44, 0.1, 0.2), (70, 0.2, None))):
        wagen += blende(arrow(0, -54, ln, -54, BLUE, 4, 12) + label(ln + 6, -48, "v", BLUE, 18), ein(a, z) if a > 0 else [(0, 1), (z, 1), (z + 0.02, 0)])
    pts = [(round(0.30 * k / 6, 3), (30 + 230 * (k / 6) ** 2, 262)) for k in range(7)]
    s.append(bewege(wagen, pts))
    # B: Richtung ändern (gleiches Tempo)
    b.append(kasten(300, 160, "Richtung ändern", TEAL))
    cx, cy, r = 220, 492, 122
    th0, th1 = math.radians(210), math.radians(330)
    P = lambda th: (cx + r * math.cos(th), cy + r * math.sin(th))
    x0, y0 = P(th0); x1, y1 = P(th1)
    b.append(f"<path d='M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}' fill='none' stroke='{GRID}' stroke-width='4' stroke-dasharray='8 7'/>")
    kugel = (arrow(0, 0, 58, 0, BLUE, 4, 12) + f"<g transform='rotate(90)'>{arrow(0, 0, 48, 0, RED, 5, 13)}</g>"
             + f"<circle r='15' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>")
    n = 10
    wege, winkel = [], []
    for k in range(n + 1):
        th = th0 + (th1 - th0) * k / n; ta = round(0.34 + 0.26 * k / n, 3)
        wege.append((ta, P(th))); winkel.append((ta, math.degrees(math.atan2(math.cos(th), -math.sin(th)))))
    s.append(bewege(drehe(kugel, winkel), wege))
    b.append(label(L + 14, 354, "F", RED, 18) + t(L + 26, 354, "zeigt zur Kurvenmitte", 17, "", "start", RED))
    # C: Form ändern
    b.append(kasten(474, 150, "Form ändern", ORANGE))
    ball = f"<ellipse rx='46' ry='38' fill='#E2C896' stroke='{INK}' stroke-width='2'/>"
    b.append(f"<g transform='translate(220 560)'>" + skaliere(ball, [(0, (1, 1)), (0.66, (1, 1)), (0.80, (0.72, 1.22))]) + "</g>")
    for sgn in (-1, 1):
        hand = (f"<rect x='{-18 if sgn < 0 else 0}' y='-26' width='18' height='52' rx='8' fill='{LIGHT}' stroke='{MUTED}' stroke-width='2'/>"
                + blende(arrow(-sgn * 34, 0, -sgn * 8, 0, RED, 5, 13), ein(0.66)))
        s.append(bewege(hand, [(0, (220 + sgn * 70, 560)), (0.66, (220 + sgn * 70, 560)), (0.80, (220 + sgn * 56, 560))]))
    b.append(t(M, 614, "keine Ortsänderung – trotzdem eine Kraft", 18, "m", "middle"))
    return save("wirkung.svg", svg(H, b + [szene("".join(s))], "Was eine Kraft bewirkt – animiert"))


# ------------------------------------------------------------------ 2 Bewegung in Bildern
def bewegung():
    H = 620
    b, s = kopf("Bewegung in Bildern", "Ein Punkt pro Sekunde – vergleiche die Abstände.",
                [("Gleiche Abstände: gleichförmig.", 0, 0.32), ("Abstände wachsen: schneller.", 0.32, 0.64), ("Kurve: auch eine Beschleunigung.", 0.64, None)])
    for (y, titel, col, xs, t0) in ((150, "gleichförmig: gleiche Abstände", GREEN, [40 + 90 * i for i in range(5)], 0.02),
                                    (290, "schneller werdend: Abstände wachsen", ORANGE, [40 + 33 * i + 13 * i * i for i in range(5)], 0.34)):
        b.append(kasten(y, 128, titel, col))
        yy = y + 78
        b.append(f"<line x1='{L + 14}' y1='{yy}' x2='{R - 14}' y2='{yy}' stroke='{GRID}' stroke-width='3'/>")
        for i, x in enumerate(xs):
            ti = t0 + 0.06 * i
            s.append(blende(f"<circle cx='{x:.1f}' cy='{yy}' r='12' fill='none' stroke='{col}' stroke-width='3'/>" + t(x, yy + 38, f"t{i}", 17, "m", "middle"), ein(ti)))
        pts = []
        for k in range(17):
            tt = k / 16 * 0.24
            idx = tt / 0.06
            if col == GREEN: x = 40 + 90 * idx
            else: x = 40 + 33 * idx + 13 * idx * idx   # gleichmäßig beschleunigt: Abstände 46, 72, 98, 124
            pts.append((round(t0 + tt, 3), (x, yy)))
        s.append(bewege(f"<circle r='12' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>", pts))
    # Kurve
    b.append(kasten(430, 180, "gleiches Tempo, aber Kurve", TEAL))
    cx, cy, r = 220, 650, 150
    th0, th1 = math.radians(220), math.radians(320)
    P = lambda th: (cx + r * math.cos(th), cy + r * math.sin(th))
    x0, y0 = P(th0); x1, y1 = P(th1)
    b.append(f"<path d='M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}' fill='none' stroke='{GRID}' stroke-width='4' stroke-dasharray='8 7'/>")
    kugel = arrow(0, 0, 50, 0, BLUE, 4, 12) + label(40, -10, "v", BLUE, 18) + f"<circle r='12' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>"
    wege, winkel = [], []
    for k in range(13):
        th = th0 + (th1 - th0) * k / 12; ta = round(0.66 + 0.26 * k / 12, 3)
        wege.append((ta, P(th))); winkel.append((ta, math.degrees(math.atan2(math.cos(th), -math.sin(th)))))
    s.append(bewege(drehe(kugel, winkel), wege))
    b.append(t(M, 600, "Zur Geschwindigkeit gehört die Richtung.", 18, "m", "middle"))
    return save("bewegung.svg", svg(H, b + [szene("".join(s))], "Bewegung in Bildern – animiert"))


# ------------------------------------------------------------------ 3 Auftrieb
def auftrieb():
    H = 652
    b, s = kopf("Auftrieb", "Ein Holzball wird unter Wasser losgelassen.",
                [("Unter Wasser: Auftrieb größer.", 0, 0.30), ("Der Ball steigt nach oben.", 0.30, 0.62), ("Oben schwimmt er: Kräfte gleich.", 0.62, None)])
    b.append(f"<rect x='70' y='160' width='300' height='330' rx='10' fill='{GLASS}' stroke='{MUTED}' stroke-width='3'/>")
    b.append(f"<rect x='73' y='230' width='294' height='257' fill='{WATER}'/>")
    b.append(f"<line x1='73' y1='230' x2='367' y2='230' stroke='{TEAL}' stroke-width='3'/>")
    unter = (arrow(-24, 0, -24, -96, TEAL, 6, 16) + label(-34, -60, F("A"), TEAL, 21, "end")
             + arrow(24, 0, 24, 52, RED, 6, 16) + label(34, 40, F("G"), RED, 21))
    oben = (arrow(-24, 0, -24, -70, TEAL, 6, 16) + label(-34, -44, F("A"), TEAL, 21, "end")
            + arrow(24, 0, 24, 70, RED, 6, 16) + label(34, 52, F("G"), RED, 21))
    ball = (blende(unter, [(0, 1), (0.60, 1), (0.63, 0)]) + blende(oben, ein(0.62))
            + f"<circle r='30' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>")
    pts = [(0, (180, 424)), (0.28, (180, 424))] + [(round(0.28 + 0.32 * k / 8, 3), (180, 424 - (424 - 226) * (1 - (1 - k / 8) ** 2))) for k in range(1, 9)]
    s.append(bewege(ball, pts))
    s.append(blende(t(356, 470, f"{F('A')} &gt; {F('G')}", 22, "b", "end", TEAL), [(0, 1), (0.60, 1), (0.63, 0)]))
    s.append(blende(t(356, 470, f"{F('A')} = {F('G')}", 22, "b", "end", OLIVE), ein(0.62)))
    # ruhig: Nachschlagen
    b.append(kasten(510, 128, "Zum Nachschlagen", OLIVE))
    b.append(t(L + 16, 568, f"schwebt: {F('A')} = {F('G')} (z. B. U-Boot)", 18))
    b.append(t(L + 16, 594, f"sinkt: {F('A')} &lt; {F('G')} (z. B. Stein)", 18))
    b.append(t(L + 16, 618, f"{F('A')} = Gewichtskraft des verdrängten Wassers", 17, "m"))
    return save("auftrieb.svg", svg(H, b + [szene("".join(s))], "Auftrieb – animiert"))


# ------------------------------------------------------------------ 4 Reibung
def reibung():
    H = 640
    b, s = kopf("Reibung", "Sie hält fest, bremst – und lässt dich gehen.",
                [("Leicht ziehen: Der Becher haftet.", 0, 0.28), ("Er gleitet gleichmäßig: Zug = Reibung.", 0.28, 0.60), ("Gehen: Haftreibung schiebt dich an.", 0.60, None)])
    b.append(kasten(146, 220, "Becher wird gezogen", GREEN))
    b.append(f"<rect x='{L + 10}' y='320' width='{R - L - 20}' height='14' fill='{LIGHT}' stroke='{MUTED}' stroke-width='2'/>")
    becher = (f"<polygon points='-34,-70 34,-70 28,0 -28,0' fill='{GLASS}' stroke='{INK}' stroke-width='2'/><rect x='-24' y='-46' width='48' height='44' fill='{WATER}'/>"
              + blende(arrow(36, -36, 66, -36, GREEN, 5, 13) + arrow(-36, -12, -66, -12, RUST, 5, 13), [(0, 1), (0.26, 1), (0.29, 0)])
              + blende(arrow(36, -36, 106, -36, GREEN, 6, 15) + label(72, -46, "Zug", GREEN, 18, "middle")
                       + arrow(-36, -12, -106, -12, RUST, 6, 15) + label(-72, 12, F("R"), RUST, 19, "middle"), ein(0.28)))
    s.append(bewege(becher, [(0, (110, 320)), (0.30, (110, 320)), (0.58, (300, 320))]))
    s.append(blende(t(M, 356, "gleich lang: gleichförmig", 17, "m", "middle"), ein(0.40)))
    b.append(kasten(386, 236, "Abstoßen beim Gehen", ORANGE))
    b.append(f"<rect x='{L + 10}' y='530' width='{R - L - 20}' height='14' fill='{LIGHT}' stroke='{MUTED}' stroke-width='2'/>")
    schuh = (f"<path d='M -60 0 L -60 -24 L -20 -24 L 40 -2 L 40 0 Z' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>"
             + blende(arrow(-50, -50, 40, -50, TEAL, 6, 15) + t(-56, -62, "Boden schiebt dich nach vorn", 17, "b", "start", TEAL), ein(0.66)))
    s.append(bewege(schuh, [(0, (130, 530)), (0.74, (130, 530)), (0.90, (250, 530))]))
    s.append(blende(arrow(160, 560, 90, 560, ORANGE, 6, 15) + t(L + 14, 588, "Fuß drückt den Boden nach hinten", 17, "b", "start", ORANGE), ein(0.62)))
    b.append(t(M, 632, f"vereinfachtes Modell: {F('R')} = μ · {F('N')}", 16, "m", "middle"))
    return save("reibung.svg", svg(H, b + [szene("".join(s))], "Reibung – animiert"))


# ------------------------------------------------------------------ 5 Kapillarwirkung
def kapillar():
    H = 600
    b, s = kopf("Kapillarwirkung", "Wasser steigt in engen, benetzbaren Spalten.",
                [("Der Streifen taucht ins Wasser.", 0, 0.20), ("Das Wasser kriecht hoch.", 0.20, 0.56), ("Im Röhrchen steigt es auch.", 0.56, None)])
    # links: Filterpapier
    b.append(f"<rect x='34' y='160' width='180' height='330' rx='14' fill='{WHITE}' stroke='{GREEN}' stroke-width='3'/>")
    b.append(t(124, 186, "Filterpapier", 19, "b", "middle", GREEN))
    b.append(f"<rect x='54' y='380' width='140' height='96' rx='6' fill='{GLASS}' stroke='{MUTED}' stroke-width='2'/><rect x='56' y='410' width='136' height='64' fill='{WATER}'/>")
    b.append(f"<rect x='104' y='206' width='40' height='226' fill='{WHITE}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<rect x='105' y='258' width='38' height='173' fill='{WATER}' opacity='0.85'>{attr('y', [(0, 431), (0.18, 431), (0.22, 420), (0.54, 258)])}"
             f"{attr('height', [(0, 0), (0.18, 0), (0.22, 11), (0.54, 173)])}</rect>")
    s.append(blende(arrow(176, 420, 176, 272, GREEN, 4, 12) + t(176, 258, "steigt", 16, "b", "middle", GREEN), ein(0.40)))
    b.append(t(124, 504, "Wasserspiegel", 16, "m", "middle"))
    # rechts: Röhrchen
    b.append(f"<rect x='226' y='160' width='180' height='330' rx='14' fill='{WHITE}' stroke='{ORANGE}' stroke-width='3'/>")
    b.append(t(316, 186, "enges Röhrchen", 19, "b", "middle", ORANGE))
    b.append(f"<rect x='246' y='400' width='140' height='76' rx='6' fill='{GLASS}' stroke='{MUTED}' stroke-width='2'/><rect x='248' y='420' width='136' height='54' fill='{WATER}'/>")
    b.append(f"<rect x='305' y='210' width='22' height='250' fill='{GLASS}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<rect x='307' y='300' width='18' height='158' fill='{WATER}'>{attr('y', [(0, 420), (0.58, 420), (0.86, 300)])}{attr('height', [(0, 38), (0.58, 38), (0.86, 158)])}</rect>")
    men = f"<path d='M 307 0 Q 316 10 325 0' fill='none' stroke='{TEAL}' stroke-width='3'/>"
    s.append(bewege(men, [(0, (0, 420)), (0.58, (0, 420)), (0.86, (0, 300))]))
    s.append(blende(arrow(286, 420, 286, 304, GREEN, 4, 12) + t(280, 360, "Steig-", 16, "b", "end", GREEN) + t(280, 378, "höhe", 16, "b", "end", GREEN), ein(0.86)))
    s.append(blende(t(333, 232, "Adhäsion", 16, "b", "start", ORANGE) + t(333, 250, "an der", 15, "", "start", ORANGE) + t(333, 266, "Wand", 15, "", "start", ORANGE), ein(0.62)))
    b.append(t(316, 504, "Wasserspiegel", 16, "m", "middle"))
    # ruhig: Nachschlagen
    b.append(t(L, 540, "Adhäsion = Anziehung verschiedener Stoffe", 18, "b"))
    b.append(t(L, 566, "Kohäsion = Zusammenhalt in einem Stoff", 18, "b"))
    b.append(t(L, 590, "Je enger das Röhrchen, desto höher steigt es.", 17, "m"))
    return save("kapillar.svg", svg(H, b + [szene("".join(s))], "Kapillarwirkung – animiert"))


# ------------------------------------------------------------------ 6 Druck
def druck():
    H = 640
    b, s = kopf("Druck", "p = F / A – Kraft durch Fläche",
                [("Schmale Sohle: sinkt tief ein.", 0, 0.30), ("Schneeschuh: sinkt kaum ein.", 0.30, 0.60), ("Luft zusammendrücken: Druck steigt.", 0.60, None)])
    b.append(kasten(146, 236, "Gleiche Kraft: 600 N", GREEN))
    stiefel = lambda breite: (f"<rect x='-26' y='-92' width='52' height='70' rx='10' fill='#687652' stroke='{INK}' stroke-width='2'/>"
                              f"<rect x='{-breite / 2}' y='-22' width='{breite}' height='22' rx='6' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>"
                              + arrow(0, -128, 0, -96, RED, 5, 13) + label(10, -110, "600 N", RED, 17))
    s.append(bewege(stiefel(52), [(0, (120, 300)), (0.04, (120, 300)), (0.26, (120, 336))]))
    s.append(bewege(stiefel(150), [(0, (320, 300)), (0.34, (320, 300)), (0.54, (320, 308))]))
    b_snow = f"<rect x='{L + 6}' y='300' width='{R - L - 12}' height='56' fill='{SNOW}' opacity='0.92' stroke='{GRID}' stroke-width='2'/>"
    s.append(b_snow)
    s.append(blende(t(120, 374, "A = 0,03 m²", 17, "", "middle") + t(120, 396, "p = 20 000 Pa", 18, "b", "middle", RUST), ein(0.24)))
    s.append(blende(t(320, 374, "A = 0,30 m²", 17, "", "middle") + t(320, 396, "p = 2 000 Pa", 18, "b", "middle", TEAL), ein(0.52)))
    # Spritze
    b.append(kasten(410, 178, "Luft lässt sich zusammendrücken", ORANGE))
    b.append(f"<rect x='60' y='470' width='240' height='54' rx='8' fill='{GLASS}' stroke='{MUTED}' stroke-width='2'/><rect x='38' y='490' width='22' height='14' fill='{GLASS}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<circle cx='32' cy='497' r='14' fill='#E2C4A2' stroke='{INK}' stroke-width='2'/>" + t(32, 534, "Finger", 15, "m", "middle"))
    kolben = (f"<rect x='0' y='472' width='14' height='50' fill='{METAL}' stroke='{INK}' stroke-width='2'/>"
              f"<rect x='14' y='490' width='90' height='14' fill='{METAL}' stroke='{INK}' stroke-width='2'/><rect x='104' y='474' width='12' height='46' fill='{METAL}' stroke='{INK}' stroke-width='2'/>"
              + blende(arrow(156, 497, 122, 497, RUST, 6, 14) + label(138, 466, "drücken", RUST, 16, "middle"), ein(0.62))
              + blende(arrow(-44, 497, -6, 497, RED, 6, 14), ein(0.80)))
    s.append(bewege(kolben, [(0, (250, 0)), (0.62, (250, 0)), (0.84, (165, 0))]))
    for k in range(6):
        x0 = 76 + (k % 3) * 56 + (k // 3) * 22; y0 = 484 + (k // 3) * 24
        x1 = 76 + (x0 - 76) * 0.5
        s.append(bewege(f"<circle r='6' fill='{TEAL}'/>", [(0, (x0, y0)), (0.62, (x0, y0)), (0.84, (x1, y0))]))
    s.append(blende(t(M, 566, "Die Luft drückt den Kolben zurück.", 18, "b", "middle", RED), ein(0.82)))
    b.append(t(M, 616, "Druck ist keine Kraftart – er verbindet Kraft und Fläche.", 16, "m", "middle"))
    return save("druck.svg", svg(H, b + [szene("".join(s))], "Druck – animiert"))


# ------------------------------------------------------------------ 7 Kraft und Gegenkraft
def gegenkraft():
    H = 620
    b, s = kopf("Kraft und Gegenkraft", "Zwei Kraftmesser hängen ineinander.",
                [("Noch kein Zug: beide zeigen 0 N.", 0, 0.28), ("Gezogen: beide zeigen 2 N.", 0.28, 0.62), ("Gleich groß, entgegengesetzt, zwei Körper.", 0.62, None)])
    b.append(kasten(146, 244, "Wechselwirkung: zwei Körper", TEAL))
    def km(name, col):
        k = (f"<rect x='0' y='-16' width='136' height='32' rx='8' fill='{WHITE}' stroke='{col}' stroke-width='3'/>"
             + "".join(f"<line x1='{24 + 20 * i}' y1='-16' x2='{24 + 20 * i}' y2='{-6 if i % 2 else -2}' stroke='{MUTED}' stroke-width='2'/>" for i in range(6))
             + t(24, 34, "0", 14, "m", "middle") + t(64, 34, "2", 14, "m", "middle") + t(104, 34, "4 N", 14, "m", "middle")
             + t(68, -26, name, 17, "b", "middle", col))
        return k
    marke = f"<rect x='-3' y='-14' width='6' height='28' fill='{RED}'/>"
    # A links (fest gehalten), Haken rechts
    b.append(f"<rect x='{L + 6}' y='238' width='20' height='44' rx='8' fill='{LIGHT}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<g transform='translate(44 260)'>{km('Kraftmesser A', GREEN)}<path d='M 136 0 h 18 a 9 9 0 1 1 0 0.1' fill='none' stroke='{INK}' stroke-width='3'/></g>")
    s.append(bewege(marke, [(0, (68, 260)), (0.30, (68, 260)), (0.46, (108, 260))]))
    # B rechts, wird gezogen
    bb = (km("Kraftmesser B", ORANGE) + f"<path d='M 0 0 h -14 a 9 9 0 1 0 0 0.1' fill='none' stroke='{INK}' stroke-width='3'/>"
          + f"<rect x='140' y='-22' width='20' height='44' rx='8' fill='{LIGHT}' stroke='{MUTED}' stroke-width='2'/>"
          + blende(arrow(166, 0, 188, 0, RUST, 5, 12), ein(0.30)))
    s.append(bewege(bb, [(0, (222, 260)), (0.30, (222, 260)), (0.46, (228, 260))]))
    s.append(bewege(marke, [(0, (246, 260)), (0.30, (246, 260)), (0.46, (292, 260))]))
    s.append(blende(t(108, 318, "2 N", 22, "b", "middle", GREEN) + t(292, 318, "2 N", 22, "b", "middle", ORANGE), ein(0.46)))
    s.append(blende(arrow(150, 346, 214, 346, GREEN, 6, 15) + t(146, 352, "B zieht an A", 16, "b", "end", GREEN)
                    + arrow(300, 370, 236, 370, ORANGE, 6, 15) + t(304, 376, "A zieht an B", 16, "b", "start", ORANGE), ein(0.62)))
    # ruhig: Gleichgewicht
    b.append(kasten(404, 200, "Zum Vergleich: Gleichgewicht an EINEM Körper", OLIVE))
    b.append(f"<rect x='120' y='520' width='200' height='14' fill='{WOOD}' stroke='{INK}' stroke-width='2'/>"
             f"<rect x='170' y='488' width='100' height='32' rx='5' fill='#C49678' stroke='{INK}' stroke-width='2'/>")
    b.append(arrow(200, 504, 200, 446, TEAL, 6, 15) + t(194, 460, "Stützkraft", 16, "b", "end", TEAL))
    b.append(arrow(240, 504, 240, 562, RED, 6, 15) + t(250, 552, F("G"), 17, "b", "start", RED))
    b.append(t(M, 590, "Buch: zwei Kräfte am selben Körper – Summe null", 16, "m", "middle"))
    return save("gegenkraft.svg", svg(H, b + [szene("".join(s))], "Kraft und Gegenkraft – animiert"))


ALLE = [wirkung, bewegung, auftrieb, reibung, kapillar, druck, gegenkraft]

if __name__ == "__main__":
    import xml.dom.minidom
    for fn in ALLE:
        name = fn()
        xml.dom.minidom.parse(os.path.join(IMG, name))   # wohlgeformt?
        print("ok", name, os.path.getsize(os.path.join(IMG, name)) // 1024, "KB")
