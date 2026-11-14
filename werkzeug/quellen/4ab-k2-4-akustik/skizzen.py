"""Eigene Grafiken (SVG) für NAWI 4AB K2.4/K3.2 Akustik und Gehör – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/4ab-k2-4-akustik/skizzen.py   → schreibt 4ab-nawi/k2-4-akustik/img/*.svg
Handy zuerst: Breite 640, Schrift mindestens 22 (am Handy ca. 12–16 px, Antippen vergrößert). Animationen (SMIL) laufen auch in <img>,
bei »weniger Bewegung« (prefers-reduced-motion) bleiben sie stehen. Alle Zahlen stimmen mit inhalt.py überein."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
IMG = os.path.join(ROOT, I.ORDNER, "img")
os.makedirs(IMG, exist_ok=True)

BG, INK, OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = "#F2F3EE", "#1F2A1C", "#3B4A2F", "#7FA83A", "#D9772B", "#2E7D8C", "#8C3B2E", "#5E6652"
RED, BLUE, LIGHT, BONE, SKIN, LYMPH = "#A33A2B", "#2A5C8C", "#DFE5D0", "#EADFC8", "#F1C9A8", "#BFE0E8"
FONT = "'Source Sans 3','Carlito','Segoe UI',Arial,sans-serif"
STILL = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def svg(w, h, body, title, anim=False):
    st = f"<style>text{{font-family:{FONT};fill:{INK}}} .b{{font-weight:700}} .m{{fill:{MUTED}}} {STILL if anim else ''}</style>"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{st}<rect width='{w}' height='{h}' rx='18' fill='{BG}'/>{body}</svg>")


def t(x, y, s, size=24, cls="", anchor="start", fill=None, weight=None):
    f = f" fill='{fill}'" if fill else ""
    w = f" font-weight='{weight}'" if weight else ""
    c = f" class='{cls}'" if cls else ""
    return f"<text x='{x}' y='{y}' font-size='{size}' text-anchor='{anchor}'{c}{f}{w}>{s}</text>"


def arrow(x1, y1, x2, y2, col=INK, w=4, head=14):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2 - 0.6 * head * math.cos(a):.1f}' y2='{y2 - 0.6 * head * math.sin(a):.1f}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<polygon points='{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{col}'/>")


def save(name, s):
    open(os.path.join(IMG, name), "w", encoding="utf-8").write(s)


def sinus_pfad(x0, x1, y0, amp, lam, phase=0.0, n=160, hull=None):
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        e = hull(x) if hull else 1
        pts.append((x, y0 - amp * e * math.sin(2 * math.pi * (x - x0) / lam + phase)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)


# ------------------------------------------------------------------ 1 Druckwelle (animiert)
def druckwelle():
    W, H, T, LAM = 640, 560, 1.6, 200
    b = [t(24, 44, "Schall in Luft: eine Längswelle", 28, "b")]
    b.append(t(24, 76, "Die Teilchen schwingen nur hin und her – die Verdichtung wandert.", 21, "m"))
    # Lautsprecher
    b.append(f"<rect x='22' y='130' width='34' height='170' rx='6' fill='{OLIVE}'/>")
    b.append(f"<rect x='54' y='140' width='12' height='150' rx='4' fill='{ORANGE}'><animate attributeName='x' values='54;62;54;46;54' dur='{T}s' repeatCount='indefinite' calcMode='spline' keySplines='.37 0 .63 1;.37 0 .63 1;.37 0 .63 1;.37 0 .63 1'/></rect>")
    cols, rows, x0, dx = 26, 7, 92, 20
    for c in range(cols):
        x = x0 + c * dx
        ph = ((x - 60) / LAM) % 1.0
        beg = -(1 - ph) * T
        for r in range(rows):
            y = 140 + r * 24 + (6 if c % 2 else 0)
            hl = (c == 13 and r == 3)
            fill = RED if hl else TEAL
            rad = 8 if hl else 6
            b.append(f"<circle cx='{x}' cy='{y}' r='{rad}' fill='{fill}'><animate attributeName='cx' values='{x};{x + 8};{x};{x - 8};{x}' dur='{T}s' begin='{beg:.3f}s' "
                     f"repeatCount='indefinite' calcMode='spline' keySplines='.37 0 .63 1;.37 0 .63 1;.37 0 .63 1;.37 0 .63 1'/></circle>")
    b.append(t(352, 330, "dieses Teilchen bleibt fast an seinem Platz", 20, "", "middle", RED))
    # Druckkurve
    b.append(t(24, 384, "Druck an jeder Stelle (Diagramm, keine Teilchenbahn)", 22, "b"))
    b.append(f"<line x1='92' y1='470' x2='612' y2='470' stroke='{MUTED}' stroke-width='2' stroke-dasharray='6 6'/>")
    b.append(t(600, 410, "Überdruck", 20, "m", "end"))
    b.append(t(600, 540, "Unterdruck", 20, "m", "end"))
    b.append("<clipPath id='kc'><rect x='92' y='395' width='520' height='150'/></clipPath>")
    # p ∝ cos(k(x - 60) - ωt): Pfad bei t=0, nach rechts verschoben
    d = sinus_pfad(92 - LAM, 612, 470, 55, LAM, phase=math.pi / 2 - 2 * math.pi * (92 - 60) / LAM)
    b.append(f"<g clip-path='url(#kc)'><path d='{d}' fill='none' stroke='{ORANGE}' stroke-width='5'>"
             f"<animateTransform attributeName='transform' type='translate' from='0 0' to='{LAM} 0' dur='{T}s' repeatCount='indefinite'/></path></g>")
    b.append(t(24, 470, "p", 26, "b", fill=ORANGE))
    return svg(W, H, "".join(b), "Animation: Schall als Längswelle mit Druckkurve", anim=True)


# ------------------------------------------------------------------ 2 Schallweg: Tempo, Gewitter, Echo
def schallweg():
    W, H = 640, 660
    b = [t(24, 44, "Wie schnell ist Schall?", 28, "b")]
    for i, (n, v, col) in enumerate([("Luft", 340, TEAL), ("Wasser", 1480, BLUE), ("Stahl", 5000, OLIVE)]):
        y = 80 + i * 56
        b.append(t(24, y + 30, n, 24, "b"))
        w = 330 * v / 5000
        b.append(f"<rect x='130' y='{y + 8}' width='{max(w, 26):.0f}' height='32' rx='8' fill='{col}'/>")
        b.append(t(140 + max(w, 26), y + 32, f"{'rund ' if v > 340 else ''}{v:,} m/s".replace(",", " "), 22))
    # Gewitter
    y0 = 290
    b.append(t(24, y0, "Gewitter: Sekunden durch 3 = Kilometer", 24, "b"))
    b.append(f"<polygon points='60,{y0 + 20} 40,{y0 + 70} 58,{y0 + 70} 44,{y0 + 115} 82,{y0 + 52} 64,{y0 + 52} 80,{y0 + 20}' fill='#E8C02E' stroke='{INK}' stroke-width='2'/>")
    for k in range(4):
        x = 110 + k * 160
        b.append(f"<line x1='{x}' y1='{y0 + 70}' x2='{x}' y2='{y0 + 90}' stroke='{INK}' stroke-width='3'/>")
        b.append(t(x, y0 + 118, f"{k} km", 22, "", "middle"))
        b.append(t(x, y0 + 60, f"{k * 3} s", 22, "m", "middle"))
    b.append(f"<line x1='110' y1='{y0 + 80}' x2='590' y2='{y0 + 80}' stroke='{INK}' stroke-width='3'/>")
    # Echo
    y1 = 470
    b.append(t(24, y1, "Echo: hin UND zurück", 24, "b"))
    b.append(f"<rect x='560' y='{y1 + 20}' width='56' height='150' fill='{BONE}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(t(588, y1 + 104, "Fels", 20, "m", "middle"))
    b.append(f"<circle cx='60' cy='{y1 + 95}' r='26' fill='{SKIN}' stroke='{INK}' stroke-width='2'/>")
    b.append(arrow(100, y1 + 70, 548, y1 + 70, ORANGE, 5))
    b.append(arrow(548, y1 + 120, 100, y1 + 120, TEAL, 5))
    b.append(t(324, y1 + 58, "hin: s", 22, "", "middle", ORANGE))
    b.append(t(324, y1 + 154, "zurück: s", 22, "", "middle", TEAL))
    b.append(t(24, y1 + 182, "Gemessene Zeit gilt für 2 · s  →  s = v · t / 2", 22, "b"))
    return svg(W, H, "".join(b), "Schallgeschwindigkeit, Gewitterregel und Echo")


# ------------------------------------------------------------------ 3 Tonhöhe und Lautstärke
def tonhoehe():
    W, H = 640, 600
    b = [t(24, 44, "Frequenz → Tonhöhe · Amplitude → Stärke", 26, "b")]
    panels = [("tief: wenige Schwingungen", 30, 300, 40, 0), ("hoch: viele Schwingungen", 330, 300, 40, 1),
              ("schwach: kleine Amplitude", 30, 300, 18, 2), ("stark: große Amplitude", 330, 300, 52, 3)]
    for lab, x, w, amp, k in panels:
        y = 80 if k < 2 else 330
        b.append(f"<rect x='{x}' y='{y}' width='{w - 20}' height='220' rx='14' fill='#fff' stroke='{LIGHT}' stroke-width='3'/>")
        b.append(t(x + 14, y + 34, lab, 21, "b"))
        lam = 140 if k == 0 else (50 if k == 1 else 90)
        yc = y + 135
        b.append(f"<line x1='{x + 14}' y1='{yc}' x2='{x + w - 34}' y2='{yc}' stroke='{MUTED}' stroke-width='2' stroke-dasharray='5 5'/>")
        b.append(f"<path d='{sinus_pfad(x + 14, x + w - 34, yc, amp, lam)}' fill='none' stroke='{ORANGE if k < 2 else TEAL}' stroke-width='5'/>")
        b.append(t(x + w - 34, y + 206, "Zeit →", 18, "m", "end"))
    b.append(t(24, 584, "Gleiche Frequenz bei 3 und 4: gleiche Tonhöhe, aber verschieden stark.", 20, "m"))
    return svg(W, H, "".join(b), "Tonhöhe und Stärke im Vergleich")


# ------------------------------------------------------------------ 4 Dezibel-Leiter
def dbleiter():
    W, H = 640, 880
    b = [t(24, 44, "Die Dezibel-Leiter", 28, "b"), t(24, 76, "Jede Stufe: 10-mal so viel Intensität", 22, "m")]
    top, bot = 110, 830
    y = lambda L: bot - (bot - top) * L / 160

    def farbe(L):
        return GREEN if L < 70 else ("#E8C02E" if L < 85 else (ORANGE if L < 120 else RED))
    for L in range(0, 160, 10):
        b.append(f"<rect x='150' y='{y(L + 10):.0f}' width='46' height='{y(L) - y(L + 10):.0f}' fill='{farbe(L)}' stroke='#fff' stroke-width='2'/>")
    for L in range(0, 170, 10):
        b.append(f"<line x1='140' y1='{y(L):.0f}' x2='206' y2='{y(L):.0f}' stroke='{INK}' stroke-width='3'/>")
        b.append(t(132, y(L) + 8, f"{L}", 22, "b" if L % 40 == 0 else "", "end"))
        if L < 160: b.append(t(60, y(L + 5) + 7, "×10", 18, "m", "middle"))
    b.append(t(80, 104, "dB", 22, "b", "end"))
    ex = [(0, "Hörschwelle"), (30, "Flüstern"), (60, "Gespräch"), (70, "Straßenverkehr 70–80"),
          (100, "Kopfhörer laut, Disco"), (120, "Schmerzgrenze ab ca. 120–130"), (155, "Schuss am Ohr: über 150 (Spitze)")]
    for L, s in ex:
        b.append(f"<line x1='206' y1='{y(L):.0f}' x2='236' y2='{y(L):.0f}' stroke='{MUTED}' stroke-width='2'/>")
        b.append(t(244, y(L) + 8, s, 22))
    for L, s, col in [(80, "80 dB: Gehörschutz bereitstellen", ORANGE), (85, "85 dB: Gehörschutz tragen", RED)]:
        b.append(f"<line x1='150' y1='{y(L):.0f}' x2='620' y2='{y(L):.0f}' stroke='{col}' stroke-width='3' stroke-dasharray='8 6'/>")
        b.append(t(620, y(L) - 5, s, 18, "", "end", col, 700))
    b.append(t(24, 868, "+10 dB: Intensität ×10, Schalldruck ×3,2", 22, "b"))
    return svg(W, H, "".join(b), "Dezibel-Leiter von 0 bis 160 dB mit Beispielen")


# ------------------------------------------------------------------ 5 Ohr (beschriftet bzw. nummeriert)
def spirale(cx, cy, r0, r1, turns, n=120):
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * turns * i / n
        r = r1 - (r1 - r0) * i / n
        pts.append((cx + r * math.cos(a + math.pi), cy + r * math.sin(a + math.pi)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def ohr_basis():
    b = []
    b.append(f"<path d='M200 120 Q420 80 620 150 L620 560 Q420 600 200 540 Z' fill='{BONE}' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<path d='M70 170 Q20 260 50 350 Q70 420 110 440 Q90 380 100 330 Q120 300 120 260 Q120 200 90 160 Z' fill='{SKIN}' stroke='{INK}' stroke-width='3'/>")
    b.append(f"<path d='M95 300 L250 290 L250 340 L95 330 Z' fill='#F8E3D2' stroke='{INK}' stroke-width='3'/>")
    b.append(f"<ellipse cx='256' cy='315' rx='8' ry='34' fill='{ORANGE}' stroke='{INK}' stroke-width='2'/>")
    b.append(f"<path d='M262 270 Q300 250 330 270 L340 360 Q300 380 262 360 Z' fill='#FBF6EC' stroke='{MUTED}' stroke-width='2'/>")
    b.append(f"<path d='M262 306 Q275 280 290 292 L296 316' fill='none' stroke='{RUST}' stroke-width='7' stroke-linecap='round'/>")
    b.append(f"<path d='M290 292 Q306 286 312 304' fill='none' stroke='{RUST}' stroke-width='7' stroke-linecap='round'/>")
    b.append(f"<path d='M312 304 L330 300 M312 304 L330 316' stroke='{RUST}' stroke-width='6' stroke-linecap='round'/>")
    b.append(f"<rect x='330' y='296' width='8' height='24' fill='{TEAL}'/>")
    b.append(f"<path d='M300 370 Q320 440 360 520' fill='none' stroke='#C9B79A' stroke-width='22' stroke-linecap='round'/>")
    for (cx, cy, rx, ry, rot) in [(410, 205, 46, 30, -20), (450, 215, 30, 52, 10), (420, 238, 54, 22, 0)]:
        b.append(f"<ellipse cx='{cx}' cy='{cy}' rx='{rx}' ry='{ry}' transform='rotate({rot} {cx} {cy})' fill='none' stroke='{TEAL}' stroke-width='10'/>")
    b.append(f"<circle cx='392' cy='300' r='26' fill='{LYMPH}' stroke='{TEAL}' stroke-width='3'/>")
    b.append(f"<path d='{spirale(470, 360, 8, 58, 2.6)}' fill='none' stroke='{TEAL}' stroke-width='16' stroke-linecap='round'/>")
    b.append(f"<path d='{spirale(470, 360, 8, 58, 2.6)}' fill='none' stroke='{LYMPH}' stroke-width='8' stroke-linecap='round'/>")
    b.append(f"<path d='M520 330 Q570 300 630 300' fill='none' stroke='#E8C02E' stroke-width='12' stroke-linecap='round'/>")
    return b


def ohr(nummern=False):
    W, H = 640, 640
    b = [t(24, 44, "Das Ohr im Schnitt" if not nummern else "Beschrifte die Nummern 1 bis 6", 28, "b")] + ohr_basis()
    if nummern:
        marks = [(1, 170, 312), (2, 256, 232), (3, 300, 232), (4, 420, 150), (5, 470, 450), (6, 600, 268)]
        lines = [(170, 312, 170, 312), (256, 245, 256, 285), (300, 245, 296, 285), (420, 163, 420, 185), (470, 437, 470, 410), (600, 281, 600, 300)]
        for (n, x, y), (x1, y1, x2, y2) in zip(marks, lines):
            if (x1, y1) != (x2, y2): b.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{INK}' stroke-width='3'/>")
            b.append(f"<circle cx='{x}' cy='{y}' r='19' fill='{OLIVE}'/>" + t(x, y + 9, str(n), 26, "b", "middle", "#fff"))
        b.append(t(24, 620, "Ein Teil ist gezeichnet, aber nicht nummeriert.", 20, "m"))
    else:
        lab = [("Ohrmuschel", 20, 480, 70, 440), ("Gehörgang", 120, 270, 170, 300), ("Trommelfell", 170, 210, 254, 282),
               ("Gehörknöchelchen", 260, 175, 300, 268), ("Bogengänge", 430, 112, 420, 180), ("Hörnerv", 640 - 16, 260, 610, 298),
               ("Schnecke", 520, 470, 490, 410), ("ovales Fenster", 270, 420, 334, 322), ("Ohrtrompete", 250, 590, 340, 500)]
        for s, x, y, x2, y2 in lab:
            anc = "end" if x > 560 else "start"
            b.append(f"<line x1='{x2}' y1='{y2}' x2='{x + (0 if anc == 'start' else 0)}' y2='{y - 8}' stroke='{MUTED}' stroke-width='2'/>")
            b.append(t(x, y, s, 22, "b", anc))
        b.append(t(24, 630, "Außenohr | Mittelohr | Innenohr", 20, "m"))
    return svg(W, H, "".join(b), "Schnitt durch das Ohr" + (" mit Nummern 1 bis 6" if nummern else " mit Beschriftung"))


# ------------------------------------------------------------------ 6 Hörvorgang (Schnecke ausgerollt, animiert)
def hoervorgang():
    W, H = 640, 560
    b = [t(24, 44, "Die Schnecke »ausgerollt«", 28, "b"), t(24, 76, "Eine Welle läuft über die Grundmembran.", 21, "m")]
    x0, x1, yc = 110, 610, 290
    b.append(f"<rect x='{x0}' y='190' width='{x1 - x0}' height='200' rx='60' fill='{LYMPH}' stroke='{TEAL}' stroke-width='4'/>")
    b.append(t(x0 + 20, 228, "Vorhoftreppe", 20, "m"))
    b.append(t(x0 + 20, 376, "Paukentreppe", 20, "m"))
    # Steigbügel am ovalen Fenster (oben links), rundes Fenster unten links
    b.append(f"<rect x='70' y='212' width='40' height='26' fill='{RUST}'><animate attributeName='x' values='70;80;70' dur='0.8s' repeatCount='indefinite'/></rect>")
    b.append(t(24, 180, "Steigbügel · ovales Fenster", 20, "b"))
    b.append(f"<path d='M110 330 Q96 352 110 374' fill='none' stroke='{ORANGE}' stroke-width='6'><animate attributeName='d' values='M110 330 Q96 352 110 374;M110 330 Q86 352 110 374;M110 330 Q96 352 110 374' dur='0.8s' repeatCount='indefinite'/></path>")
    b.append(t(24, 418, "rundes Fenster", 20, "b"))
    hull = lambda x: math.exp(-((x - 380) / 95) ** 2) * 0.95 + 0.05
    frames = [sinus_pfad(x0 + 20, x1 - 30, yc, 34, 70, phase=-2 * math.pi * k / 8, n=120, hull=hull) for k in range(9)]
    b.append(f"<path d='{frames[0]}' fill='none' stroke='{OLIVE}' stroke-width='6'><animate attributeName='d' values='{';'.join(frames)}' dur='0.8s' repeatCount='indefinite'/></path>")
    for k in range(9):
        x = 340 + k * 10
        b.append(f"<line x1='{x}' y1='{yc - 4}' x2='{x}' y2='{yc - 26}' stroke='{RED}' stroke-width='3'/>")
    b.append(t(380, 166, "hier: Haarzellen gereizt", 22, "b", "middle", RED))
    b.append(arrow(380, 172, 380, 236, RED, 3, 12))
    b.append(t(x0, 450, "vorne: hohe Töne", 22, "b"))
    b.append(t(x1, 450, "hinten: tiefe Töne", 22, "b", "end"))
    b.append(t(24, 500, "Die Lage der Wellenspitze verrät dem Gehirn die Tonhöhe.", 21))
    b.append(t(24, 532, "Lautstärke: wie stark die Härchen gebogen werden.", 21))
    return svg(W, H, "".join(b), "Animation: Wanderwelle in der ausgerollten Schnecke", anim=True)


# ------------------------------------------------------------------ 7 Gehörschutz
def haarzelle(x, y, kaputt=False):
    s = f"<rect x='{x - 16}' y='{y}' width='32' height='70' rx='12' fill='#F7D6C4' stroke='{INK}' stroke-width='2'/>"
    for k, dx in enumerate((-10, -3, 4, 11)):
        if kaputt and k % 2 == 0:
            s += f"<path d='M{x + dx} {y} l{8 if k else -8} -14 l10 4' fill='none' stroke='{RED}' stroke-width='3'/>"
        elif kaputt:
            continue
        else:
            s += f"<line x1='{x + dx}' y1='{y}' x2='{x + dx}' y2='{y - 34 + k * 3}' stroke='{OLIVE}' stroke-width='3'/>"
    return s


def gehoerschutz():
    W, H = 640, 700
    b = [t(24, 44, "Haarzellen: einmal kaputt, immer kaputt", 26, "b")]
    b.append(f"<rect x='24' y='70' width='286' height='200' rx='14' fill='#fff' stroke='{GREEN}' stroke-width='4'/>")
    b.append(f"<rect x='330' y='70' width='286' height='200' rx='14' fill='#fff' stroke='{RED}' stroke-width='4'/>")
    for k in range(4): b.append(haarzelle(80 + k * 60, 150))
    for k in range(4): b.append(haarzelle(386 + k * 60, 150, kaputt=k != 1))
    b.append(t(167, 255, "gesund", 22, "b", "middle", GREEN))
    b.append(t(473, 255, "nach Lärm / Knall", 22, "b", "middle", RED))
    b.append(t(24, 320, "Was schützt wirklich?", 26, "b"))
    # Kapsel
    b.append(f"<rect x='24' y='340' width='186' height='300' rx='14' fill='#fff' stroke='{GREEN}' stroke-width='4'/>")
    b.append(f"<path d='M62 470 Q117 360 172 470' fill='none' stroke='{OLIVE}' stroke-width='12'/><rect x='46' y='460' width='38' height='70' rx='14' fill='{OLIVE}'/><rect x='150' y='460' width='38' height='70' rx='14' fill='{OLIVE}'/>")
    b.append(t(117, 580, "Kapsel", 22, "b", "middle")); b.append(t(117, 612, "geprüft ✓", 22, "b", "middle", GREEN))
    # Stöpsel
    b.append(f"<rect x='227' y='340' width='186' height='300' rx='14' fill='#fff' stroke='{GREEN}' stroke-width='4'/>")
    b.append(f"<path d='M280 470 q0 -40 30 -40 h30 q14 0 14 20 v40 q0 20 -14 20 h-30 q-30 0 -30 -40z' fill='#F0B34A' stroke='{INK}' stroke-width='2'/>")
    b.append(t(320, 580, "Stöpsel", 22, "b", "middle")); b.append(t(320, 612, "richtig eingesetzt ✓", 20, "b", "middle", GREEN))
    # ANC
    b.append(f"<rect x='430' y='340' width='186' height='300' rx='14' fill='#fff' stroke='{RED}' stroke-width='4'/>")
    b.append(f"<circle cx='510' cy='460' r='34' fill='#DDD' stroke='{INK}' stroke-width='2'/><rect x='534' y='452' width='44' height='16' rx='8' fill='#DDD' stroke='{INK}' stroke-width='2'/>")
    b.append(f"<line x1='470' y1='410' x2='570' y2='510' stroke='{RED}' stroke-width='8'/><line x1='570' y1='410' x2='470' y2='510' stroke='{RED}' stroke-width='8'/>")
    b.append(t(523, 580, "Noise-Cancelling", 21, "b", "middle")); b.append(t(523, 612, "kein Gehörschutz ✗", 20, "b", "middle", RED))
    b.append(t(24, 680, "Geprüfter Gehörschutz trägt eine Prüfnorm (EN 352) und einen Dämmwert.", 19, "m"))
    return svg(W, H, "".join(b), "Gesunde und geschädigte Haarzellen, geeigneter und ungeeigneter Gehörschutz")


# ------------------------------------------------------------------ 8 Richtungshören
def richtung():
    W, H = 640, 560
    b = [t(24, 44, "Richtungshören: Kopf von oben", 28, "b")]
    cx, cy, r = 380, 290, 110
    b.append(f"<path d='M{cx + 20} {cy - 130} L{cx + r + 120} {cy - 160} L{cx + r + 120} {cy + 160} L{cx + 20} {cy + 130} Z' fill='#E4E7DD' opacity='.9'/>")
    b.append(t(cx + r + 110, cy - 140, "Schallschatten", 21, "m", "end"))
    b.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{SKIN}' stroke='{INK}' stroke-width='3'/>")
    b.append(f"<path d='M{cx - 18} {cy - r + 4} L{cx} {cy - r - 22} L{cx + 18} {cy - r + 4}' fill='{SKIN}' stroke='{INK}' stroke-width='3'/>")
    b.append(t(cx, cy - r - 30, "vorne", 20, "m", "middle"))
    b.append(f"<ellipse cx='{cx - r}' cy='{cy}' rx='12' ry='26' fill='{SKIN}' stroke='{INK}' stroke-width='3'/>")
    b.append(f"<ellipse cx='{cx + r}' cy='{cy}' rx='12' ry='26' fill='{SKIN}' stroke='{INK}' stroke-width='3'/>")
    b.append(t(cx - r + 24, cy + 6, "links", 20, "b"))
    b.append(t(cx + r - 24, cy + 6, "rechts", 20, "b", "end"))
    sx = 70
    b.append(f"<circle cx='{sx}' cy='{cy}' r='20' fill='{RED}'/>")
    for k in range(1, 4):
        b.append(f"<path d='M{sx + 20 + k * 22} {cy - 26 - k * 8} Q{sx + 34 + k * 26} {cy} {sx + 20 + k * 22} {cy + 26 + k * 8}' fill='none' stroke='{RED}' stroke-width='3'/>")
    b.append(t(sx, cy + 56, "Knall", 22, "b", "middle", RED))
    b.append(arrow(sx + 24, cy, cx - r - 16, cy, ORANGE, 5))
    b.append(f"<path d='M{cx - r + 6} {cy + 40} A{r + 22} {r + 22} 0 0 0 {cx + r - 8} {cy + 46}' fill='none' stroke='{TEAL}' stroke-width='5' stroke-dasharray='10 8'/>")
    b.append(t(cx, cy + r + 66, "Umweg zum rechten Ohr: etwa 0,2 m", 22, "b", "middle", TEAL))
    b.append(t(24, 500, "0,2 m : 340 m/s ≈ 0,6 ms später – und leiser.", 23, "b"))
    b.append(t(24, 534, "Das Gehirn wertet diese Unterschiede aus.", 21, "m"))
    return svg(W, H, "".join(b), "Kopf von oben mit Schallquelle links, Umweg und Schallschatten zum rechten Ohr")


# ------------------------------------------------------------------ 9 Gleichgewicht: Lagesinn und Drehsinn
def macula(x, y, kipp):
    g = f"<g transform='rotate({kipp} {x + 120} {y + 110})'>"
    g += f"<rect x='{x}' y='{y + 120}' width='240' height='60' fill='#F7D6C4' stroke='{INK}' stroke-width='2'/>"
    shift = kipp * 0.9
    for k in range(5):
        hx = x + 30 + k * 45
        g += f"<line x1='{hx}' y1='{y + 120}' x2='{hx + shift:.0f}' y2='{y + 78}' stroke='{OLIVE}' stroke-width='4'/>"
    g += f"<rect x='{x + shift:.0f}' y='{y + 40}' width='240' height='44' rx='8' fill='#E9EFF2' stroke='{TEAL}' stroke-width='2'/>"
    for k in range(9):
        g += f"<polygon points='{x + 14 + k * 26 + shift:.0f},{y + 40} {x + 26 + k * 26 + shift:.0f},{y + 22} {x + 38 + k * 26 + shift:.0f},{y + 40}' fill='#fff' stroke='{MUTED}' stroke-width='2'/>"
    return g + "</g>"


def gleichgewicht():
    W, H = 640, 800
    b = [t(24, 44, "Lagesinn: Vorhofsäckchen", 26, "b")]
    b.append(macula(40, 70, 0)); b.append(macula(340, 70, 18))
    b.append(t(160, 300, "Kopf gerade", 21, "", "middle")); b.append(t(470, 300, "Kopf geneigt", 21, "", "middle"))
    b.append(t(24, 336, "Kalkkristalle ziehen die Gallertschicht – die Härchen biegen sich.", 20, "m"))
    b.append(t(24, 392, "Drehsinn: Bogengang mit Ampulle", 26, "b"))
    cx, cy, R = 320, 600, 130
    b.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='none' stroke='{TEAL}' stroke-width='34'/>")
    b.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='none' stroke='{LYMPH}' stroke-width='24'/>")
    b.append(f"<circle cx='{cx}' cy='{cy - R}' r='34' fill='{LYMPH}' stroke='{TEAL}' stroke-width='4'/>")
    b.append(f"<path d='M{cx + 4} {cy - R + 28} Q{cx - 22} {cy - R} {cx - 10} {cy - R - 30}' fill='#F5E6B8' stroke='{ORANGE}' stroke-width='4'/>")
    b.append(t(cx + 46, cy - R - 20, "Gallertkuppel", 20, "b"))
    b.append(f"<path d='M{cx - R - 50} {cy + 40} A{R + 50} {R + 50} 0 0 1 {cx - 40} {cy - R - 46}' fill='none' stroke='{INK}' stroke-width='5'/>")
    b.append(arrow(cx - 60, cy - R - 44, cx - 30, cy - R - 47, INK, 5))
    b.append(t(cx - R - 60, cy - 90, "Kopf dreht", 21, "b", "end"))
    b.append(f"<path d='M{cx + R - 30} {cy + 70} A{R - 26} {R - 26} 0 0 0 {cx + R - 30} {cy - 70}' fill='none' stroke='{RED}' stroke-width='5'/>")
    b.append(arrow(cx + R - 26, cy - 60, cx + R - 40, cy - 80, RED, 5))
    b.append(t(cx + R + 30, cy + 10, "Lymphe", 21, "b", "start", RED))
    b.append(t(cx + R + 30, cy + 38, "bleibt zurück", 21, "", "start", RED))
    b.append(t(24, 784, "Nur Änderungen der Drehung biegen die Kuppel.", 21, "m"))
    return svg(W, H, "".join(b), "Lagesinn mit Kalkkristallen und Drehsinn mit Bogengang, Lymphe und Gallertkuppel")


# ------------------------------------------------------------------ 10 Bogengang in drei Phasen
def bogengang():
    W, H = 640, 470
    b = [t(24, 44, "Drehen: Beginn – gleichmäßig – Stopp", 26, "b")]
    for k, (lab, bieg, lym) in enumerate([("Drehung beginnt", -22, "bleibt zurück"), ("gleichmäßig", 0, "dreht mit"), ("Stopp", 22, "fließt weiter")]):
        cx, cy, R = 110 + k * 210, 220, 70
        b.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='none' stroke='{TEAL}' stroke-width='22'/>")
        b.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='none' stroke='{LYMPH}' stroke-width='14'/>")
        b.append(f"<circle cx='{cx}' cy='{cy - R}' r='22' fill='{LYMPH}' stroke='{TEAL}' stroke-width='3'/>")
        b.append(f"<path d='M{cx} {cy - R + 20} Q{cx + bieg * 0.6:.0f} {cy - R} {cx + bieg} {cy - R - 20}' fill='none' stroke='{ORANGE}' stroke-width='7' stroke-linecap='round'/>")
        if k < 2: b.append(arrow(cx - R - 26, cy + 10, cx - R - 6, cy - 30, INK, 4, 12))
        b.append(t(cx, cy + R + 50, lab, 21, "b", "middle"))
        b.append(t(cx, cy + R + 80, "Lymphe " + lym, 19, "m", "middle"))
        b.append(t(cx, cy + R + 108, "Kuppel " + ("gebogen" if bieg else "gerade"), 19, "", "middle", ORANGE if bieg else GREEN, 700))
    b.append(t(24, 450, "Schwarzer Pfeil: Kopf dreht sich. Orange: Gallertkuppel in der Ampulle.", 18, "m"))
    return svg(W, H, "".join(b), "Bogengang in drei Phasen einer Drehung")


# ------------------------------------------------------------------ 11 Signalweg (Leitidee)
def signalweg():
    W, H = 640, 560
    b = [t(24, 44, "Vom Knall zum Kopf", 30, "b")]
    st = [("1", "Quelle schwingt", ["Stimmgabel, Schuss"], ORANGE), ("2", "Druckwelle", ["340 m/s in Luft"], TEAL), ("3", "Pegel in dB", ["×10 je 10 dB"], "#C79A1E"),
          ("4", "Ohr verstärkt", ["Trommelfell,", "Knöchelchen"], RUST), ("5", "Haarzellen", ["→ Hörnerv", "→ Gehirn"], RED), ("6", "Orientierung", ["Richtung,", "Gleichgewicht"], OLIVE)]
    pos = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1)]
    for (n, h, s, col), (c, r) in zip(st, pos):
        x, y = 24 + c * 205, 80 + r * 230
        b.append(f"<rect x='{x}' y='{y}' width='180' height='190' rx='18' fill='#fff' stroke='{col}' stroke-width='5'/>")
        b.append(f"<circle cx='{x + 40}' cy='{y + 42}' r='24' fill='{col}'/>" + t(x + 40, y + 52, n, 28, "b", "middle", "#fff"))
        b.append(t(x + 16, y + 112, h, 24, "b"))
        for k, z in enumerate(s): b.append(t(x + 16, y + 146 + 26 * k, z, 19, "m"))
    for c in (0, 1):
        b.append(arrow(24 + c * 205 + 184, 175, 24 + c * 205 + 202, 175, INK, 4, 12))
        b.append(arrow(24 + (c + 1) * 205 - 6, 405, 24 + c * 205 + 186, 405, INK, 4, 12))
    b.append(arrow(524, 274, 524, 306, INK, 4, 12))
    b.append(t(24, 545, "Stunde 1: 1–2 · Stunde 2: 3 · Stunde 3: 4–5 · Stunde 4: 6", 20, "m"))
    return svg(W, H, "".join(b), "Der Signalweg in sechs Stationen")


TEILE = {"druckwelle.svg": druckwelle, "schallweg.svg": schallweg, "tonhoehe.svg": tonhoehe, "dbleiter.svg": dbleiter,
         "ohr.svg": lambda: ohr(False), "ohr-nummern.svg": lambda: ohr(True), "hoervorgang.svg": hoervorgang, "gehoerschutz.svg": gehoerschutz,
         "richtung.svg": richtung, "gleichgewicht.svg": gleichgewicht, "bogengang.svg": bogengang, "signalweg.svg": signalweg}

if __name__ == "__main__":
    for name, fn in TEILE.items():
        s = fn(); save(name, s); print(name, len(s) // 1024, "KB")
