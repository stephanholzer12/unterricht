"""Eigene Grafiken (SVG) für TÖW 5AB K1.9 Globalisierung, KI und Klima – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ab-k1-9-global-klima/skizzen.py   → schreibt 5ab-toew/k1-9-global-klima/img/*.svg
Handy zuerst: Breite 640, Schrift mindestens 22 (am Handy ca. 12–16 px, Antippen vergrößert). Animationen (SMIL) laufen auch in <img>;
die Browser-Einstellung »weniger Bewegung« stoppt SMIL NICHT (nur der Pause-Knopf in der Präsentation). Alle Zahlen stimmen mit inhalt.py überein.
Standard 16.11.2026 (Skill »animierte Grafiken«): Zeigt ein Bild einen VORGANG, wird es animiert. Das Grundbild ohne Animation zeigt den Endzustand,
die Animation baut ihn auf; alle Spuren eines Bildes laufen 12 s im Gleichtakt; Schritte als kurze Überschrift im Bild.
Animiert (Vorgang): fussabdruck.svg, rucksack.svg, oekosysteme.svg, rechenzentrum.svg, treibhaus.svg, handel.svg. Bewusst ruhig (zum Ablesen): zeitleiste.svg, ueberblick.svg."""
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


def dreh(inner, punkte, dur=ZYK):
    """Gruppe, die sich dreht. punkte = [(Zeitanteil, 'Winkel cx cy')]; Grundlage = letzter Punkt."""
    kt, vals = _werte(_spur(punkte))
    return (f"<g transform='rotate({punkte[-1][1]})'>{inner}"
            f"<animateTransform attributeName='transform' type='rotate' values='{vals}' keyTimes='{kt}' dur='{dur}s' repeatCount='indefinite'/></g>")


def wert(attr, punkte, dur=ZYK):
    """Nur das <animate>-Element für ein Attribut (x2, cx, rx, width, d, stroke …); das Attribut selbst trägt den Endwert."""
    kt, vals = _werte(_spur(punkte))
    return f"<animate attributeName='{attr}' values='{vals}' keyTimes='{kt}' dur='{dur}s' repeatCount='indefinite'/>"


def szene(inner, dur=ZYK):
    """Ganze Szene: sichtbar bis ENDE, dann kurz aus, Rücksprung unsichtbar, wieder ein."""
    return (f"<g>{inner}<animate attributeName='opacity' values='1;1;0;0;1' keyTimes='0;{ENDE - 0.04:.3f};{ENDE};{ZURUECK};1' dur='{dur}s' repeatCount='indefinite'/></g>")


def schritt(text, von, bis, x, y, size=22, anchor="start", fill=None, cls="b"):
    """Kurze Schritt-Überschrift im Bild: erscheint bei von, verschwindet bei bis (bis=None: bleibt bis zum Ende)."""
    pts = [(0, 0), (von, 0), (von + 0.02, 1)]
    if bis is not None:
        pts += [(bis, 1), (bis + 0.02, 0)]
    return blende(t(x, y, text, size, cls, anchor, fill), pts)


def punkt_klang(col, r=10):
    """Schallpaket: Punkt mit zwei Bögen davor (Mittelpunkt bei 0 0, Schall läuft nach rechts)."""
    return (f"<circle r='{r}' fill='{col}'/>"
            f"<path d='M{r + 8} -11 Q{r + 17} 0 {r + 8} 11' fill='none' stroke='{col}' stroke-width='3' stroke-linecap='round'/>"
            f"<path d='M{r + 18} -17 Q{r + 31} 0 {r + 18} 17' fill='none' stroke='{col}' stroke-width='3' stroke-linecap='round' opacity='.55'/>")


def laufweg(pts, t0, t1):
    """Zeit-Punkte für bewege(): gleichmäßig entlang einer Folge von Punkten (x, y)."""
    n = len(pts) - 1
    return [(round(t0 + (t1 - t0) * i / n, 4), f"{x:.1f} {y:.1f}") for i, (x, y) in enumerate(pts)]




# ------------------------------------------------------------------ 1 Naturbudget eines Jahres (animiert)
def fussabdruck():
    W, H = 640, 470
    x0, x1 = 40, 600
    X = lambda tag: x0 + (x1 - x0) * tag / 365
    b = [t(24, 44, "Das Naturbudget der Erde für ein Jahr", 28, "b"),
         t(24, 74, "Was die Erde in einem Jahr nachwachsen lässt – und wann es verbraucht ist", 19, "m")]
    for k, m in enumerate(["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]):
        xm = X(k * 365 / 12 + 15)
        b.append(t(xm, 120, m, 18, "m", "middle"))
    s = []
    for row, (name, tag, txt, y) in enumerate([("Erde (alle Menschen)", I.OS_WELT_TAG, "30. Juli → 365 : 211 ≈ 1,7 Erden", 150),
                                                ("Wenn alle lebten wie in Österreich", I.OS_AT_TAG, "2. April → 365 : 92 ≈ 4 Erden", 290)]):
        t0 = 0.12 + row * 0.38
        b.append(t(x0, y - 10, name, 22, "b"))
        b.append(f"<rect x='{x0}' y='{y}' width='{x1 - x0}' height='44' rx='8' fill='#fff' stroke='{MUTED}'/>")
        gw = X(tag) - x0
        s.append(f"<rect x='{x0}' y='{y}' height='44' rx='8' fill='{GREEN}' width='{gw:.1f}'>" + wert("width", [(0, 0), (t0, 0), (t0 + 0.14, gw)]) + "</rect>")
        rw = x1 - X(tag)
        s.append(blende(f"<rect x='{X(tag):.1f}' y='{y}' height='44' width='{rw:.1f}' fill='{RED}' opacity='.85'/>"
                        + t((X(tag) + x1) / 2, y + 30, "auf Pump", 20, "b", "middle", "#fff"), [(0, 0), (t0 + 0.15, 0), (t0 + 0.2, 1)]))
        s.append(blende(f"<line x1='{X(tag):.1f}' x2='{X(tag):.1f}' y1='{y - 6}' y2='{y + 50}' stroke='{INK}' stroke-width='3'/>"
                        + t(x0, y + 78, txt, 22, "b"), [(0, 0), (t0 + 0.15, 0), (t0 + 0.2, 1)]))
    # Erden für Österreich
    erde = lambda cx, cy, op=1: f"<g opacity='{op}'><circle cx='{cx}' cy='{cy}' r='20' fill='{BLUE}'/><path d='M{cx - 10} {cy - 8} q8 -6 14 2 q-4 8 4 12 q-10 6 -16 -2z' fill='{GREEN}'/></g>"
    er = "".join(erde(72 + 52 * k, 420, 1) for k in range(4))
    s.append(blende(er + t(290, 418, "≈ 4 Erden, wenn alle", 18, "m") + t(290, 442, "so lebten wie wir in Österreich", 18, "m"), [(0, 0), (0.7, 0), (0.75, 1)]))
    s.append(schritt("Jahresbeginn: Das Budget ist voll.", 0.02, 0.12, 330, 44, 18))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Zwei Balken für ein Jahr. Das Naturbudget der Erde ist am 30. Juli verbraucht; würden alle so leben wie in Österreich, schon am 2. April; danach leben wir auf Pump. Vier Erdkugeln zeigen: So viele bräuchten wir, wenn alle so lebten wie in Österreich.", anim=True)


# ------------------------------------------------------------------ 2 Ökologischer Rucksack eines Handys (animiert)
def rucksack():
    W, H = 640, 520
    b = [t(24, 44, "Der ökologische Rucksack eines Handys", 28, "b"),
         t(24, 74, "Alles, was für ein Handy bewegt und verbraucht wird – in Kilogramm", 19, "m")]
    stationen = [("Bergbau", "Erz, Gestein"), ("Fabrik", "Chips, Glas"), ("Transport", "Schiff, Lkw"), ("Nutzung", "Strom beim Laden"), ("Entsorgung", "Recycling")]
    s = []
    for k, (n, z) in enumerate(stationen):
        y = 120 + k * 72
        t0 = 0.08 + k * 0.14
        s.append(blende(f"<rect x='24' y='{y}' width='250' height='58' rx='10' fill='#fff' stroke='{OLIVE}' stroke-width='2'/>"
                        + t(40, y + 26, f"{k + 1}  {n}", 22, "b") + t(40, y + 50, z, 18, "m"), [(0, 0), (t0, 0), (t0 + 0.03, 1)]))
        s.append(blende(bewege(f"<circle r='9' fill='{ORANGE}'/>", [(0, f"274 {y + 29}"), (t0 + 0.03, f"274 {y + 29}"), (t0 + 0.1, f"470 {330}"), (t0 + 0.11, f"470 {330}")]),
                        [(0, 0), (t0, 0), (t0 + 0.02, 1), (t0 + 0.1, 1), (t0 + 0.11, 0)]))
    # Rucksack
    b.append(f"<path d='M380 200 q90 -50 180 0 v230 q0 30 -30 30 h-120 q-30 0 -30 -30z' fill='#fff' stroke='{OLIVE}' stroke-width='4'/>")
    b.append(f"<path d='M430 190 q40 -40 80 0' fill='none' stroke='{OLIVE}' stroke-width='6'/>")
    fill_end = 230
    s.append(f"<rect x='384' y='{460 - fill_end}' width='172' rx='6' fill='{ORANGE}' opacity='.75' height='{fill_end}'>"
             + wert("height", [(0, 0), (0.15, 0), (0.3, 70), (0.44, 120), (0.58, 150), (0.72, 225), (0.86, fill_end)])
             + wert("y", [(0, 460), (0.15, 460), (0.3, 390), (0.44, 340), (0.58, 310), (0.72, 235), (0.86, 460 - fill_end)]) + "</rect>")
    s.append(blende(t(470, 300, "≈ 75 kg", 40, "b", "middle", "#fff"), [(0, 0), (0.86, 0), (0.89, 1)]))
    # Handy
    b.append(f"<rect x='560' y='92' width='44' height='76' rx='8' fill='{INK}'/><rect x='565' y='100' width='34' height='56' rx='3' fill='{TEAL}'/>")
    b.append(t(582, 188, "0,1 kg", 20, "b", "middle"))
    b.append(t(24, 505, "Verhältnis: 75 kg : 0,1 kg = 750-mal so schwer wie das Handy selbst", 19, "m"))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Fünf Stationen eines Handys – Bergbau, Fabrik, Transport, Nutzung, Entsorgung – füllen nacheinander einen Rucksack. Am Ende wiegt er rund 75 kg, das Handy nur 0,1 kg.", anim=True)


# ------------------------------------------------------------------ 3 Arten reisen mit (animiert)
def oekosysteme():
    W, H = 640, 430
    b = [t(24, 44, "Arten reisen mit", 28, "b"), t(24, 74, "Globalisierung der Ökosysteme (Buch S. 41)", 19, "m")]
    b.append(f"<rect x='24' y='100' width='170' height='150' rx='14' fill='#E6EDF3' stroke='{BLUE}' stroke-width='2'/>" + t(109, 135, "Asien", 24, "b", "middle"))
    b.append(f"<rect x='446' y='100' width='170' height='150' rx='14' fill='#EEF3E4' stroke='{OLIVE}' stroke-width='2'/>" + t(531, 135, "Österreich", 24, "b", "middle"))
    b.append(f"<path d='M194 200 C280 160 360 160 446 200' fill='none' stroke='{MUTED}' stroke-width='3' stroke-dasharray='8 6'/>")
    schiff = (f"<path d='M-34 0 h68 l-12 16 h-44z' fill='{OLIVE}'/><rect x='-18' y='-16' width='30' height='16' fill='{ORANGE}'/>"
              f"<rect x='-30' y='-12' width='10' height='12' fill='{TEAL}'/>")
    s = [bewege(schiff, [(0, "200 196"), (0.1, "200 196"), (0.6, "440 196")])]
    muecke = (f"<ellipse cx='0' cy='0' rx='14' ry='5' fill='{INK}'/><path d='M-4 -2 l-10 -14 M4 -2 l10 -14' stroke='{MUTED}' stroke-width='2'/>"
              f"<path d='M-8 3 h4 M0 3 h4 M8 3 h4' stroke='#fff' stroke-width='2'/>")
    s.append(bewege(muecke, [(0, "200 176"), (0.1, "200 176"), (0.6, "500 215"), (0.62, "500 215")]))
    s.append(schritt("Mit Waren und Reisenden kommen fremde Arten mit.", 0.1, None, 24, 290, 20))
    s.append(blende(t(24, 330, "Tigermücke (Neozoon): seit 2022 in allen Bundesländern", 18)
                    + t(24, 360, "Drüsiges Springkraut (Neophyt): verdrängt heimische Pflanzen", 18)
                    + t(24, 390, "Folge: Ökosysteme werden weltweit ähnlicher –", 18, "b") + t(24, 412, "und Krankheitserreger reisen schneller.", 18, "b"), [(0, 0), (0.62, 0), (0.66, 1)]))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Ein Schiff fährt von Asien nach Österreich, eine Tigermücke reist mit. Darunter: Tigermücke seit 2022 in allen Bundesländern, Drüsiges Springkraut verdrängt heimische Pflanzen.", anim=True)


# ------------------------------------------------------------------ 4 Rechenzentrum: Strom wird Wärme (animiert)
def rechenzentrum():
    W, H = 640, 570
    b = [t(24, 44, "Wo wohnt die KI? Im Rechenzentrum", 28, "b"),
         t(24, 74, "Strom rein – rechnen – Wärme raus", 20, "m")]
    # Strom
    b.append(f"<rect x='24' y='110' width='120' height='110' rx='12' fill='#FFF6D6' stroke='{ORANGE}' stroke-width='2'/>"
             f"<path d='M90 124 l-22 40 h18 l-12 38 l34 -50 h-18 l14 -28z' fill='{ORANGE}'/>" + t(84, 240, "Strom", 20, "b", "middle"))
    # Server
    b.append(f"<rect x='250' y='100' width='140' height='150' rx='10' fill='{INK}'/>")
    for k in range(5):
        b.append(f"<rect x='262' y='{112 + k * 27}' width='116' height='18' rx='3' fill='#3D4A38'/><circle cx='366' cy='{121 + k * 27}' r='4' fill='{GREEN}'/>")
    b.append(t(320, 272, "Server mit KI-Chips", 20, "b", "middle"))
    # Kühlung / Fluss
    b.append(f"<rect x='470' y='110' width='146' height='110' rx='12' fill='#E6F1F3' stroke='{TEAL}' stroke-width='2'/>" + t(543, 150, "Kühlung", 22, "b", "middle") + t(543, 178, "mit Wasser", 18, "m", "middle"))
    b.append(f"<path d='M24 360 C160 330 300 390 440 350 S600 330 616 345 V420 H24z' fill='{LYMPH}'/>" + t(40, 405, "Fluss (Enns)", 20, "b"))
    b.append(f"<path d='M160 470 h80 v-30 l30 -24 l30 24 v30 h80' fill='none' stroke='{MUTED}' stroke-width='3' stroke-dasharray='8 6'/>" + t(250, 500, "oder: Abwärme heizt Häuser (Fernwärme)", 18, "m"))
    s = []
    for k in range(3):
        d = k * 0.08
        s.append(bewege(f"<circle r='8' fill='{ORANGE}'/>", [(0, "144 165"), (0.05 + d, "144 165"), (0.2 + d, "250 165"), (0.21 + d, "250 165")]))
        s.append(bewege(f"<circle r='8' fill='{RED}'/>", [(0, "390 165"), (0.3 + d, "390 165"), (0.45 + d, "470 165"), (0.46 + d, "470 165")]))
        s.append(bewege(f"<circle r='8' fill='{RED}' opacity='.8'/>", [(0, "543 220"), (0.55 + d, "543 220"), (0.75 + d, "470 360"), (0.76 + d, "470 360")]))
    s.append(schritt("1  Strom fließt in die Server", 0.03, 0.27, 24, 300, 20))
    s.append(schritt("2  Die Chips rechnen – fast aller Strom wird zu Wärme", 0.27, 0.52, 24, 300, 20))
    s.append(schritt("3  Kühlwasser trägt die Wärme fort", 0.52, None, 24, 300, 20))
    b.append(szene("".join(s)))
    b.append(t(24, 525, "Kronstorf, Stufe 1: 150 MW · bis 1,31 TWh im Jahr ≈ 375 000 Haushalte", 17, "m") + t(24, 548, "bis 5,8 Millionen Liter warmes Kühlwasser pro Tag in die Enns", 17, "m"))
    return svg(W, H, "".join(b), "Animation: Strom fließt in Server mit KI-Chips; die Chips machen daraus Wärme; Kühlwasser trägt sie in den Fluss. Alternativ heizt die Abwärme Häuser. Zahlen für Kronstorf: 150 MW, bis 1,31 TWh im Jahr, bis 5,8 Millionen Liter warmes Wasser pro Tag.", anim=True)


# ------------------------------------------------------------------ 5 Treibhauseffekt (animiert)
def treibhaus():
    W, H = 640, 520
    b = [t(24, 44, "Der Treibhauseffekt", 28, "b"), t(24, 74, "Buch S. 71 – vereinfacht", 19, "m")]
    b.append(f"<circle cx='80' cy='130' r='34' fill='#F2C14E'/>")
    b.append(f"<rect x='0' y='170' width='640' height='120' fill='#DCE8EE' opacity='.8'/>" + t(616, 200, "Atmosphäre", 18, "m", "end"))
    for (x, y) in [(220, 230), (300, 205), (380, 250), (460, 215), (540, 245)]:
        b.append(f"<g><circle cx='{x}' cy='{y}' r='9' fill='{MUTED}'/><circle cx='{x - 14}' cy='{y}' r='7' fill='{RED}'/><circle cx='{x + 14}' cy='{y}' r='7' fill='{RED}'/></g>")
    b.append(t(24, 270, "Treibhausgase (CO₂ …)", 18, "b"))
    b.append(f"<path d='M0 400 Q160 380 320 400 T640 395 V520 H0z' fill='{GREEN}' opacity='.55'/>" + t(24, 500, "Erdboden", 20, "b"))
    s = []
    s.append(bewege(f"<path d='M0 0 l18 0 m-9 -9 l9 9 l-9 9' stroke='#E0A800' stroke-width='5' fill='none'/>", [(0, "110 150"), (0.02, "110 150"), (0.22, "300 390"), (0.23, "300 390")]))
    s.append(schritt("1  Sonnenlicht kommt durch die Luft bis zum Boden", 0.02, 0.25, 24, 340, 20))
    s.append(bewege(f"<circle r='9' fill='{RED}'/>", [(0, "320 390"), (0.27, "320 390"), (0.45, "420 240"), (0.5, "520 110"), (0.51, "520 110")]))
    s.append(schritt("2  Der warme Boden strahlt Wärme ab – ein Teil entweicht ins All", 0.25, 0.52, 24, 340, 20))
    s.append(bewege(f"<circle r='9' fill='{RED}'/>", [(0, "330 390"), (0.53, "330 390"), (0.66, "380 250"), (0.8, "300 390"), (0.81, "300 390")]))
    s.append(schritt("3  Treibhausgase halten einen Teil zurück – der Boden bleibt wärmer", 0.52, None, 24, 340, 20))
    s.append(blende(t(24, 370, "Mehr CO₂ aus Kohle, Öl und Gas → mehr Wärme bleibt da → Erwärmung", 19, "b", fill=RED), [(0, 0), (0.82, 0), (0.85, 1)]))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Sonnenlicht kommt durch die Atmosphäre zum Boden. Der warme Boden strahlt Wärme ab; ein Teil entweicht ins All, ein Teil wird von Treibhausgasen zurückgehalten. Mehr CO₂ heißt mehr zurückgehaltene Wärme.", anim=True)


# ------------------------------------------------------------------ 6 Zeitleiste Klimakonferenzen (ruhig)
def zeitleiste():
    W, H = 640, 500
    b = [t(24, 44, "Klimakonferenzen: ein langer Weg", 28, "b"), t(24, 74, "Buch S. 73–74 · ergänzt bis 2026", 19, "m")]
    b.append(f"<line x1='70' y1='100' x2='70' y2='470' stroke='{OLIVE}' stroke-width='5'/>")
    ev = [("1992", "Rio: Klimarahmenkonvention – erste COP 1995 in Berlin", GREEN),
          ("1997", "Kyoto-Protokoll: erste Reduktionsziele für Industriestaaten", GREEN),
          ("2015", "Paris: Erwärmung deutlich unter 2 °C, möglichst 1,5 °C", GREEN),
          ("2023", "Dubai: Abkehr von fossilen Energien beschlossen", GREEN),
          ("2026", "Antalya (COP31): kein gemeinsames Abschlusspapier", RED)]
    for k, (j, txt, c) in enumerate(ev):
        y = 125 + k * 72
        b.append(f"<circle cx='70' cy='{y}' r='14' fill='{c}'/>" + t(100, y - 4, j, 24, "b") + t(100, y + 24, txt, 18))
    b.append(f"<path d='M62 {125 + 4 * 72 - 8} l16 16 M78 {125 + 4 * 72 - 8} l-16 16' stroke='#fff' stroke-width='4'/>")
    return svg(W, H, "".join(b), "Zeitleiste: 1992 Rio Klimarahmenkonvention (erste COP 1995 Berlin), 1997 Kyoto, 2015 Paris (deutlich unter 2 Grad, möglichst 1,5), 2023 Dubai (Abkehr von fossilen Energien), 2026 Antalya COP31 ohne Abschlusspapier.")


# ------------------------------------------------------------------ 7 Handel EU – Mercosur (animiert)
def handel():
    W, H = 640, 500
    b = [t(24, 44, "Mercosur: Was fließt wohin?", 28, "b"), t(24, 74, "seit 1. Mai 2026 vorläufig in Kraft", 19, "m")]
    b.append(f"<rect x='24' y='100' width='200' height='130' rx='14' fill='#E6EDF3' stroke='{BLUE}' stroke-width='2'/>" + t(124, 150, "EU", 30, "b", "middle") + t(124, 180, "mit Österreich", 18, "m", "middle"))
    b.append(f"<rect x='416' y='100' width='200' height='130' rx='14' fill='#EEF3E4' stroke='{OLIVE}' stroke-width='2'/>" + t(516, 150, "Mercosur", 28, "b", "middle") + t(516, 178, "AR · BR · PY · UY", 18, "m", "middle"))
    b.append(arrow(230, 140, 410, 140, BLUE, 4) + arrow(410, 195, 230, 195, OLIVE, 4))
    s = []
    for k in range(3):
        s.append(bewege(f"<rect x='-10' y='-8' width='20' height='16' rx='3' fill='{BLUE}'/>", [(0, "240 128"), (0.05 + k * 0.08, "240 128"), (0.3 + k * 0.08, "400 128"), (0.31 + k * 0.08, "400 128")]))
        s.append(bewege(f"<circle r='8' fill='{RUST}'/>", [(0, "400 207"), (0.4 + k * 0.08, "400 207"), (0.65 + k * 0.08, "240 207"), (0.66 + k * 0.08, "240 207")]))
    s.append(schritt("→ Maschinen, Autos, Chemie: weniger Zoll", 0.05, None, 24, 270, 20, fill=BLUE))
    s.append(schritt("← Rindfleisch 99 000 t zu 7,5 % Zoll, Geflügel, Zucker", 0.4, None, 24, 300, 20, fill=RUST))
    s.append(blende(f"<rect x='24' y='330' width='290' height='140' rx='12' fill='#fff' stroke='{GREEN}' stroke-width='2'/>"
                    + t(40, 362, "Chancen", 22, "b") + t(40, 392, "Exporte, Jobs, Paris-Bindung", 18) + t(40, 420, "weniger Abhängigkeit von", 18) + t(40, 446, "einzelnen Großmächten", 18), [(0, 0), (0.7, 0), (0.74, 1)]))
    s.append(blende(f"<rect x='326' y='330' width='290' height='140' rx='12' fill='#fff' stroke='{RED}' stroke-width='2'/>"
                    + t(342, 362, "Risiken", 22, "b") + t(342, 392, "Regenwald, Soja, Rinder", 18) + t(342, 420, "lange Transportwege", 18) + t(342, 446, "Druck auf heimische Bauern", 18), [(0, 0), (0.74, 0), (0.78, 1)]))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Von der EU fließen Maschinen, Autos und Chemie zum Mercosur, von dort Rindfleisch (99 000 Tonnen zu 7,5 Prozent Zoll), Geflügel und Zucker in die EU. Darunter Chancen (Exporte, Jobs) und Risiken (Regenwald, Transport, Bauern).", anim=True)


# ------------------------------------------------------------------ 8 Überblick (ruhig)
def ueberblick():
    W, H = 640, 470
    b = [t(24, 44, "Ein Planet reicht nicht – der rote Faden", 26, "b")]
    kette = [("Konsum", "Essen, Handy, Fahrten"), ("Abdruck", "Fläche · Rucksack · CO₂"), ("Rechenzentren", "auch KI braucht Strom und Wasser"),
             ("Klima", "Treibhausgase halten Wärme zurück"), ("Abkommen", "Paris, COP31, Mercosur")]
    for k, (n, z) in enumerate(kette):
        y = 70 + k * 78
        b.append(f"<rect x='40' y='{y}' width='560' height='62' rx='12' fill='#fff' stroke='{OLIVE}' stroke-width='2'/>" + t(60, y + 30, n, 24, "b") + t(60, y + 54, z, 18, "m"))
        if k < 4: b.append(arrow(320, y + 62, 320, y + 78, OLIVE, 3, 10))
    return svg(W, H, "".join(b), "Überblick als Kette: Konsum, Abdruck, Rechenzentren, Klima, Abkommen.")


TEILE = {"fussabdruck.svg": fussabdruck, "rucksack.svg": rucksack, "oekosysteme.svg": oekosysteme, "rechenzentrum.svg": rechenzentrum,
         "treibhaus.svg": treibhaus, "zeitleiste.svg": zeitleiste, "handel.svg": handel, "ueberblick.svg": ueberblick}

if __name__ == "__main__":
    for name, fn in TEILE.items():
        s = fn(); save(name, s); print(name, len(s) // 1024, "KB")
