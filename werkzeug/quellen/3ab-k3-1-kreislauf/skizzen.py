"""Eigene Grafiken (SVG) für NAWI 3AB K3.1/K3.6 Körper unter Belastung – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3ab-k3-1-kreislauf/skizzen.py   → schreibt 3ab-nawi/k3-1-kreislauf/img/*.svg
Handy zuerst: Breite 640, Schrift mindestens 22 (am Handy ca. 12–16 px, Antippen vergrößert). Animationen (SMIL) laufen auch in <img>;
die Browser-Einstellung »weniger Bewegung« stoppt SMIL NICHT (nur der Pause-Knopf in der Präsentation). Alle Zahlen stimmen mit inhalt.py überein.
Standard 16.11.2026 (Skill »animierte Grafiken«): Zeigt ein Bild einen VORGANG, wird es animiert. Das Grundbild ohne Animation zeigt den Endzustand,
die Animation baut ihn auf; alle Spuren eines Bildes laufen 12 s im Gleichtakt; Schritte als kurze Überschrift im Bild.
Animiert (Vorgänge): herz, kreislauf, gefaesse (Venenklappe), blutdruck, gerinnung, muskel. Bewusst ruhig (Bau zum Ablesen, Vergleich): knochen, gelenke, blut, blutgruppen, hebel, ueberblick."""
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




def leader(x1, y1, x2, y2, col=MUTED):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{col}' stroke-width='2'/><circle cx='{x2}' cy='{y2}' r='4' fill='{col}'/>"


def kreis(x, y, r, col):
    return f"<circle r='{r}' fill='{col}' stroke='#fff' stroke-width='2'/>"


# ------------------------------------------------------------------ 1 Herz (animiert): Füllen (Diastole) – Auspressen (Systole)
def herz():
    W, H = 640, 670
    b = [t(320, 40, "Das Herz von vorne (rechts im Körper = links im Bild)", 22, "b", "middle")]
    # Gefäße
    b.append(f"<rect x='120' y='70' width='46' height='120' rx='14' fill='{BLUE}'/>")            # obere Hohlvene
    b.append(f"<rect x='120' y='470' width='46' height='90' rx='14' fill='{BLUE}'/>")            # untere Hohlvene
    b.append(f"<path d='M250 250 C250 150 300 110 380 110 L420 110' fill='none' stroke='{BLUE}' stroke-width='40' stroke-linecap='round'/>")   # Lungenarterie
    b.append(f"<path d='M360 250 C360 120 470 90 520 150 L520 200' fill='none' stroke='{RED}' stroke-width='44' stroke-linecap='round'/>")    # Aorta-Bogen
    b.append(f"<rect x='520' y='230' width='90' height='36' rx='14' fill='{RED}'/>")              # Lungenvene
    # Vorhöfe und Kammern
    b.append(f"<rect x='110' y='190' width='170' height='120' rx='30' fill='#C9D8EC' stroke='{BLUE}' stroke-width='5'/>")      # rechter Vorhof
    b.append(f"<rect x='330' y='190' width='190' height='120' rx='30' fill='#F2C9C2' stroke='{RED}' stroke-width='5'/>")       # linker Vorhof
    rk = f"<path d='M110 320 H280 V500 Q200 470 110 380 Z' fill='#C9D8EC' stroke='{BLUE}' stroke-width='6'/>"
    lk = f"<path d='M330 320 H520 Q520 470 330 540 Z' fill='#F2C9C2' stroke='{RED}' stroke-width='14'/>"
    zieh = lambda inner: (f"<g transform='translate(0 320)'><g><animateTransform attributeName='transform' type='scale' values='1 1;1 1;1 0.86;1 0.86;1 1;1 1' "
                          f"keyTimes='0;0.47;0.55;0.86;0.94;1' dur='{ZYK}s' repeatCount='indefinite'/><g transform='translate(0 -320)'>{inner}</g></g></g>")
    b.append(zieh(rk)); b.append(zieh(lk))
    b.append(f"<line x1='305' y1='190' x2='305' y2='540' stroke='{OLIVE}' stroke-width='14'/>")    # Scheidewand
    # Klappen (Segelklappen: Dreiecke zwischen Vorhof und Kammer; Taschenklappen: Bögen am Ausgang)
    for x in (150, 230):
        b.append(f"<polygon points='{x - 22},314 {x + 22},314 {x},345' fill='#fff' stroke='{INK}' stroke-width='2'/>")
    for x in (370, 470):
        b.append(f"<polygon points='{x - 22},314 {x + 22},314 {x},345' fill='#fff' stroke='{INK}' stroke-width='2'/>")
    b.append(f"<path d='M232 262 q18 14 36 0' fill='none' stroke='#fff' stroke-width='5'/>")
    b.append(f"<path d='M342 262 q18 14 36 0' fill='none' stroke='#fff' stroke-width='5'/>")
    # Beschriftungen
    b.append(t(195, 255, "rechter Vorhof", 21, "b", "middle"))
    b.append(t(425, 255, "linker Vorhof", 21, "b", "middle"))
    b.append(t(195, 420, "rechte", 21, "b", "middle") + t(195, 444, "Kammer", 21, "b", "middle"))
    b.append(t(420, 420, "linke", 21, "b", "middle") + t(420, 444, "Kammer", 21, "b", "middle"))
    b.append(t(20, 140, "Hohl-", 18, "m") + t(20, 160, "vene", 18, "m") + t(20, 520, "Hohl-", 18, "m") + t(20, 540, "vene", 18, "m"))
    b.append(t(320, 600, "▽ Segelklappen  ·  ⌒ Taschenklappen  ·  blau: zur Lunge  ·  rot: Aorta in den Körper", 18, "m", "middle"))
    b.append(t(320, 626, "Blau: Hohlvenen → rechter Vorhof → rechte Kammer → Lungenarterie", 18, "b", "middle", BLUE))
    b.append(t(320, 650, "Rot: Lungenvene → linker Vorhof → linke Kammer → Aorta", 18, "b", "middle", RED))
    # Blut-Punkte: blau rechts, rot links
    blau = [(143, 120), (143, 230), (190, 300), (190, 400), (250, 300), (250, 200), (320, 125), (410, 110)]
    rot = [(600, 248), (520, 248), (420, 270), (420, 330), (420, 420), (360, 300), (360, 200), (430, 110), (520, 160)]
    s = []
    for k, d in enumerate((0.0, 0.08, 0.16)):
        s.append(bewege(f"<circle r='10' fill='{BLUE}' stroke='#fff' stroke-width='2'/>", [(0, f"{blau[0][0]} {blau[0][1]}")] + laufweg(blau[:4], 0.05 + d, 0.42 + d / 2) + laufweg(blau[3:], 0.55 + d / 2, 0.9)))
        s.append(bewege(f"<circle r='10' fill='{RED}' stroke='#fff' stroke-width='2'/>", [(0, f"{rot[0][0]} {rot[0][1]}")] + laufweg(rot[:5], 0.05 + d, 0.42 + d / 2) + laufweg(rot[4:], 0.55 + d / 2, 0.9)))
    s.append(schritt("1  Diastole: Vorhöfe füllen sich, Blut fließt in die Kammern", 0.02, 0.46, 320, 66, 20, "middle", TEAL))
    s.append(schritt("2  Systole: Kammern pressen, Segelklappen zu, Blut in die Arterien", 0.5, 0.92, 320, 66, 20, "middle", RUST))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Herz mit vier Räumen; Vorhöfe füllen sich, dann pressen die Kammern das Blut in Lungenarterie und Aorta", anim=True)


# ------------------------------------------------------------------ 2 Kreislauf als Acht (animiert)
def kreislauf():
    W, H = 640, 720
    b = [t(320, 38, "Zwei Kreisläufe – eine Acht", 24, "b", "middle")]
    b.append(f"<ellipse cx='320' cy='130' rx='170' ry='70' fill='#F6E3E0' stroke='{MUTED}' stroke-width='3'/>")
    b.append(t(320, 125, "Lunge", 26, "b", "middle") + t(320, 155, "CO₂ ab · O₂ auf", 20, "m", "middle"))
    b.append(f"<rect x='150' y='520' width='340' height='150' rx='24' fill='#EFE6D6' stroke='{MUTED}' stroke-width='3'/>")
    b.append(t(320, 580, "Körper (Organe, Muskeln)", 24, "b", "middle") + t(320, 612, "O₂ und Nährstoffe ab · CO₂ auf", 20, "m", "middle"))
    # Herz
    b.append(f"<rect x='230' y='300' width='90' height='120' rx='20' fill='#C9D8EC' stroke='{BLUE}' stroke-width='5'/>")
    b.append(f"<rect x='320' y='300' width='90' height='120' rx='20' fill='#F2C9C2' stroke='{RED}' stroke-width='5'/>")
    b.append(t(275, 350, "rechts", 20, "b", "middle") + t(275, 374, "(Lunge)", 18, "m", "middle") + t(365, 350, "links", 20, "b", "middle") + t(365, 374, "(Körper)", 18, "m", "middle"))
    b.append(t(320, 290, "Herz", 22, "b", "middle"))
    # Bahnen
    lp_b = [(250, 300), (180, 240), (200, 170)]          # rechte Kammer → Lungenarterie → Lunge (blau)
    lp_r = [(440, 170), (460, 240), (390, 300)]          # Lunge → Lungenvene → linker Vorhof (rot)
    kp_r = [(390, 420), (470, 470), (440, 540)]          # linke Kammer → Aorta → Körper (rot)
    kp_b = [(200, 540), (170, 470), (250, 420)]          # Körper → Hohlvenen → rechter Vorhof (blau)
    for pts, col in ((lp_b, BLUE), (lp_r, RED), (kp_r, RED), (kp_b, BLUE)):
        d = "M" + " L".join(f"{x} {y}" for x, y in pts)
        b.append(f"<path d='{d}' fill='none' stroke='{col}' stroke-width='16' stroke-linecap='round' stroke-linejoin='round' opacity='.85'/>")
    b.append(t(70, 230, "Lungen-", 20, "b", fill=BLUE) + t(70, 252, "arterie", 20, "b", fill=BLUE))
    b.append(t(486, 230, "Lungen-", 20, "b", fill=RED) + t(486, 252, "vene", 20, "b", fill=RED))
    b.append(t(486, 470, "Aorta", 22, "b", fill=RED) + t(40, 470, "Hohlvenen", 22, "b", fill=BLUE))
    b.append(t(560, 330, "Lungen-", 18, "m", "middle") + t(560, 350, "kreislauf ↑", 18, "m", "middle"))
    b.append(t(560, 400, "Körper-", 18, "m", "middle") + t(560, 420, "kreislauf ↓", 18, "m", "middle"))
    weg = [(275, 410), (250, 300), (180, 240), (200, 170), (320, 120), (440, 170), (460, 240), (390, 300), (365, 410), (390, 420), (470, 470), (440, 540), (320, 600), (200, 540), (170, 470), (250, 420), (275, 410)]
    s = []
    for k in range(4):
        d0 = k * 0.06
        punkte = laufweg(weg, 0.02 + d0, 0.9)
        # Farbe: blau bis zur Lunge (Index 3), rot bis zum Körper (Index 11), dann blau
        n = len(weg) - 1
        t_l, t_k = 0.02 + d0 + (0.88 - d0) * 4 / n, 0.02 + d0 + (0.88 - d0) * 12 / n
        dot = (f"<circle r='12' fill='{BLUE}' stroke='#fff' stroke-width='2'>"
               f"<animate attributeName='fill' values='{BLUE};{BLUE};{RED};{RED};{BLUE};{BLUE}' keyTimes='0;{t_l:.3f};{t_l + 0.01:.3f};{t_k:.3f};{t_k + 0.01:.3f};1' dur='{ZYK}s' repeatCount='indefinite'/></circle>")
        s.append(bewege(dot, [(0, "275 410")] + punkte))
    s.append(schritt("1  rechts → Lunge: Blut holt Sauerstoff", 0.02, 0.36, 320, 700, 20, "middle", BLUE))
    s.append(schritt("2  links → Körper: Blut gibt Sauerstoff ab", 0.4, 0.92, 320, 700, 20, "middle", RED))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Animation: Blutkreislauf als Acht – rechte Herzhälfte zur Lunge, linke Herzhälfte in den Körper", anim=True)


# ------------------------------------------------------------------ 3 Gefäße mit Venenklappe (animiert)
def gefaesse():
    W, H = 640, 560
    b = [t(320, 38, "Arterie, Kapillaren, Vene", 24, "b", "middle")]
    b.append(f"<circle cx='120' cy='150' r='80' fill='{RED}'/><circle cx='120' cy='150' r='42' fill='#F6E3E0'/>")
    b.append(t(120, 262, "Arterie", 24, "b", "middle", RED) + t(120, 288, "dicke, elastische Wand", 18, "m", "middle") + t(120, 310, "hoher Druck · vom Herzen weg", 18, "m", "middle"))
    b.append(f"<circle cx='520' cy='150' r='80' fill='{BLUE}'/><circle cx='520' cy='150' r='66' fill='#DCE7F3'/>")
    b.append(t(520, 262, "Vene", 24, "b", "middle", BLUE) + t(520, 288, "dünne Wand, Klappen", 18, "m", "middle") + t(520, 310, "niedriger Druck · zum Herzen", 18, "m", "middle"))
    for i in range(7):
        x = 230 + i * 30
        b.append(f"<path d='M{x} 100 C{x + 20} 130 {x - 20} 170 {x} 200' fill='none' stroke='#C77' stroke-width='3'/>")
    b.append(t(320, 230, "Kapillaren", 22, "b", "middle") + t(320, 252, "hauchdünn: Stoffaustausch", 18, "m", "middle"))
    # Längsschnitt Vene mit Klappe
    b.append(f"<rect x='150' y='350' width='340' height='120' rx='20' fill='#DCE7F3' stroke='{BLUE}' stroke-width='6'/>")
    b.append(t(320, 500, "Venenklappe: Blut fließt nur Richtung Herz →", 20, "b", "middle"))
    b.append(t(150, 540, "Füße", 18, "m") + t(490, 540, "Herz", 18, "m", "end"))
    oben = f"<polygon points='0,0 0,58 9,0' fill='{OLIVE}'/>"
    unten = f"<polygon points='0,0 0,-58 9,0' fill='{OLIVE}'/>"
    s = []
    s.append(f"<g transform='translate(320 356)'>{dreh(oben, [(0, '0 0 0'), (0.15, '0 0 0'), (0.2, '-50 0 0'), (0.45, '-50 0 0'), (0.5, '0 0 0'), (0.94, '0 0 0')])}</g>")
    s.append(f"<g transform='translate(320 464)'>{dreh(unten, [(0, '0 0 0'), (0.15, '0 0 0'), (0.2, '50 0 0'), (0.45, '50 0 0'), (0.5, '0 0 0'), (0.94, '0 0 0')])}</g>")
    for k, d in enumerate((0.0, 0.06, 0.12)):
        s.append(bewege(f"<circle r='11' fill='{BLUE}' stroke='#fff' stroke-width='2'/>", [(0, "180 410"), (0.1 + d, "180 410"), (0.42 + d / 2, "460 410")]))
    s.append(schritt("1  Muskel drückt: Klappe geht auf", 0.12, 0.48, 320, 330, 20, "middle", TEAL))
    s.append(schritt("2  Muskel locker: Klappe zu – kein Rückfluss", 0.52, 0.92, 320, 330, 20, "middle", RUST))
    b.append(szene("".join(s)))
    return svg(W, H, "".join(b), "Querschnitte von Arterie und Vene, Kapillaren und eine Vene im Längsschnitt mit Klappe, die das Blut nur zum Herzen durchlässt", anim=True)


# ------------------------------------------------------------------ 4 Blutdruckkurve (animiert)
def blutdruck():
    W, H = 640, 440
    b = [t(320, 38, "Druck in einer Arterie bei jedem Herzschlag", 22, "b", "middle")]
    y = lambda p: 360 - (p - 60) * 4          # 60 mmHg → 360, 130 mmHg → 80
    for p in (80, 120):
        b.append(f"<line x1='80' y1='{y(p)}' x2='610' y2='{y(p)}' stroke='{MUTED}' stroke-dasharray='8 8' stroke-width='2'/>")
    b.append(t(70, y(120) + 8, "120", 20, "b", "end", RED) + t(70, y(80) + 8, "80", 20, "b", "end", BLUE))
    b.append(t(20, 70, "mmHg", 18, "m"))
    b.append(f"<line x1='80' y1='380' x2='610' y2='380' stroke='{INK}' stroke-width='3'/>" + t(600, 410, "Zeit", 18, "m", "end"))
    pts = []
    for k in range(3):
        x0 = 90 + k * 170
        for i in range(0, 171, 5):
            u = i / 170
            if u < 0.25: p = 80 + 40 * math.sin(u / 0.25 * math.pi / 2)
            elif u < 0.35: p = 120 - 25 * (u - 0.25) / 0.1
            elif u < 0.4: p = 95 + 5 * math.sin((u - 0.35) / 0.05 * math.pi)
            else: p = 95 - 15 * (u - 0.4) / 0.6
            pts.append((x0 + i, y(p)))
    d = "M" + " L".join(f"{x:.1f} {yy:.1f}" for x, yy in pts)
    L = 1400
    b.append(f"<path d='{d}' fill='none' stroke='{RED}' stroke-width='6' stroke-linejoin='round' stroke-dasharray='{L}' stroke-dashoffset='0'>"
             f"<animate attributeName='stroke-dashoffset' values='{L};{L};0;0;{L}' keyTimes='0;0.05;0.85;0.98;1' dur='{ZYK}s' repeatCount='indefinite'/></path>")
    b.append(t(150, y(120) - 14, "systolisch: Kammer presst", 19, "b", "start", RED))
    b.append(t(420, y(80) + 32, "diastolisch: Füllphase", 19, "b", "start", BLUE))
    b.append(t(320, 430, "Jede Spitze ist ein Herzschlag – das fühlst du als Puls.", 19, "m", "middle"))
    return svg(W, H, "".join(b), "Animation: Druckkurve in einer Arterie mit Spitzen bei etwa 120 mmHg (systolisch) und Tälern bei etwa 80 mmHg (diastolisch)", anim=True)


# ------------------------------------------------------------------ 5 Röhrenknochen (ruhig)
def knochen():
    W, H = 640, 700
    b = [t(320, 38, "Röhrenknochen im Längsschnitt", 24, "b", "middle")]
    # Gelenkenden
    for cy in (130, 570):
        b.append(f"<ellipse cx='260' cy='{cy}' rx='110' ry='80' fill='{BONE}' stroke='#8A6A44' stroke-width='5'/>")
        for i in range(-3, 4):
            b.append(f"<path d='M{200 + i * 18} {cy - 50} Q{260 + i * 10} {cy} {200 + i * 22} {cy + 50}' fill='none' stroke='#C46A5A' stroke-width='3' opacity='.8'/>")
    b.append(f"<path d='M160 105 A110 80 0 0 1 360 105' fill='none' stroke='{TEAL}' stroke-width='12'/>")   # Gelenkknorpel
    b.append(f"<line x1='170' y1='185' x2='350' y2='185' stroke='{ORANGE}' stroke-width='6' stroke-dasharray='10 6'/>")
    b.append(f"<line x1='170' y1='515' x2='350' y2='515' stroke='{ORANGE}' stroke-width='6' stroke-dasharray='10 6'/>")
    # Schaft
    b.append(f"<rect x='205' y='190' width='110' height='320' fill='{BONE}' stroke='#8A6A44' stroke-width='5'/>")
    b.append(f"<rect x='232' y='200' width='56' height='300' rx='20' fill='#F3E3A0'/>")
    b.append(f"<rect x='199' y='190' width='122' height='320' fill='none' stroke='{RUST}' stroke-width='3' stroke-dasharray='4 4'/>")
    lab = [(110, "Gelenkknorpel", 360, 95, TEAL), (160, "rotes Knochenmark", 330, 150, RED), (210, "Wachstumsfuge", 350, 185, ORANGE),
           (330, "Markhöhle", 288, 330, MUTED), (410, "Knochenschaft", 315, 410, MUTED), (480, "Beinhaut", 321, 470, RUST)]
    for ty, txt, lx, ly, col in lab:
        b.append(leader(410, ty - 6, lx, ly, col) + t(418, ty, txt, 21, "b", fill=col))
    b.append(t(418, 184, "(Knochenbälkchen)", 17, "m") + t(418, 234, "(Längenwachstum)", 17, "m") + t(418, 504, "(ernährt, heilt)", 17, "m") + t(418, 354, "(gelbes Mark, Fett)", 17, "m"))
    b.append(t(320, 680, "Material nur dort, wo Kräfte wirken: Leichtbau wie bei einem Kran.", 19, "m", "middle"))
    return svg(W, H, "".join(b), "Längsschnitt eines Röhrenknochens mit Gelenkknorpel, Knochenbälkchen mit rotem Mark, Wachstumsfuge, Markhöhle, Schaft und Beinhaut")


# ------------------------------------------------------------------ 6 Gelenke (ruhig)
def gelenke():
    W, H = 640, 640
    b = [t(320, 38, "So ist ein Gelenk gebaut", 24, "b", "middle")]
    b.append(f"<rect x='210' y='60' width='70' height='120' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/>")
    b.append(f"<circle cx='245' cy='190' r='52' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/>")
    b.append(f"<path d='M193 196 A52 52 0 0 0 297 196' fill='none' stroke='{TEAL}' stroke-width='8'/>")
    b.append(f"<path d='M175 230 Q245 300 315 230 L315 340 L175 340 Z' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/>")
    b.append(f"<path d='M185 236 Q245 296 305 236' fill='none' stroke='{TEAL}' stroke-width='8'/>")
    b.append(f"<path d='M180 150 Q150 230 180 300 M310 150 Q340 230 310 300' fill='none' stroke='{OLIVE}' stroke-width='6'/>")
    b.append(f"<ellipse cx='245' cy='246' rx='42' ry='8' fill='{LYMPH}'/>")
    b.append(f"<line x1='170' y1='120' x2='170' y2='320' stroke='{ORANGE}' stroke-width='6'/>")
    for ty, txt, lx, ly, col in [(90, "Gelenkkopf", 280, 160, INK), (130, "Gelenkknorpel", 296, 196, TEAL), (170, "Gelenkschmiere", 286, 246, TEAL),
                                 (210, "Gelenkpfanne", 300, 300, INK), (250, "Gelenkkapsel", 316, 230, OLIVE), (290, "Band", 170, 300, ORANGE)]:
        b.append(leader(390, ty - 6, lx, ly, col) + t(398, ty, txt, 20, "b", fill=col))
    # Drei Typen
    y0 = 430
    b.append(f"<circle cx='110' cy='{y0}' r='34' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/><path d='M66 {y0 + 10} A44 44 0 0 0 154 {y0 + 10}' fill='none' stroke='#8A6A44' stroke-width='8'/>")
    for a in (0, 90, 180, 270):
        r = math.radians(a)
        b.append(arrow(110 + 40 * math.cos(r), y0 + 40 * math.sin(r), 110 + 66 * math.cos(r), y0 + 66 * math.sin(r), RED, 4, 12))
    b.append(f"<rect x='260' y='{y0 - 30}' width='120' height='18' rx='8' fill='{BONE}' stroke='#8A6A44' stroke-width='3'/><rect x='260' y='{y0 + 6}' width='120' height='18' rx='8' fill='{BONE}' stroke='#8A6A44' stroke-width='3' transform='rotate(-35 260 {y0 + 15})'/>")
    b.append(f"<circle cx='260' cy='{y0 - 4}' r='14' fill='#8A6A44'/>")
    b.append(f"<path d='M360 {y0 + 40} A100 100 0 0 0 350 {y0 - 40}' fill='none' stroke='{RED}' stroke-width='4'/>")
    b.append(f"<rect x='490' y='{y0 - 50}' width='30' height='100' rx='8' fill='{BONE}' stroke='#8A6A44' stroke-width='3'/><rect x='528' y='{y0 - 50}' width='30' height='100' rx='8' fill='{BONE}' stroke='#8A6A44' stroke-width='3'/>")
    b.append(f"<path d='M486 {y0 + 64} A40 14 0 1 0 566 {y0 + 64}' fill='none' stroke='{RED}' stroke-width='4'/>")
    b.append(t(110, 535, "Kugelgelenk", 22, "b", "middle") + t(110, 560, "alle Richtungen", 18, "m", "middle") + t(110, 582, "Schulter, Hüfte", 18, "m", "middle"))
    b.append(t(320, 535, "Scharniergelenk", 22, "b", "middle") + t(320, 560, "nur auf und zu", 18, "m", "middle") + t(320, 582, "Ellbogen, Finger", 18, "m", "middle"))
    b.append(t(525, 535, "Drehgelenk", 22, "b", "middle") + t(525, 560, "Knochen dreht sich", 18, "m", "middle") + t(525, 582, "Elle–Speiche", 18, "m", "middle"))
    return svg(W, H, "".join(b), "Aufbau eines Gelenks mit Kopf, Pfanne, Knorpel, Schmiere, Kapsel und Band; darunter Kugel-, Scharnier- und Drehgelenk")


# ------------------------------------------------------------------ 7 Blut (ruhig)
def blut():
    W, H = 640, 520
    b = [t(320, 38, "Was im Blut steckt", 24, "b", "middle")]
    b.append(f"<rect x='60' y='70' width='90' height='360' rx='40' fill='#fff' stroke='{MUTED}' stroke-width='4'/>")
    b.append(f"<rect x='64' y='74' width='82' height='196' rx='36' fill='#F3DC8A'/>")
    b.append(f"<rect x='64' y='270' width='82' height='156' rx='0' fill='{RED}'/>")
    b.append(f"<rect x='64' y='264' width='82' height='8' fill='#F4F1E8'/>")
    b.append(leader(160, 170, 150, 170) + t(168, 162, "Plasma ≈ 55 %", 21, "b") + t(168, 186, "90 % Wasser, Eiweiße, Salze,", 17, "m") + t(168, 206, "Nährstoffe, Hormone", 17, "m"))
    b.append(leader(160, 350, 150, 350) + t(168, 344, "Blutzellen ≈ 45 %", 21, "b", fill=RED) + t(168, 368, "(Hämatokrit)", 17, "m"))
    b.append(t(105, 460, "nach dem Schleudern", 16, "m", "middle"))
    x = 470
    b.append(f"<ellipse cx='{x}' cy='120' rx='42' ry='42' fill='{RED}'/><ellipse cx='{x}' cy='120' rx='18' ry='18' fill='#8C2A20'/>")
    b.append(t(x, 190, "rote Blutkörperchen", 20, "b", "middle", RED) + t(x, 212, "Sauerstoff · Hämoglobin", 17, "m", "middle"))
    b.append(f"<circle cx='{x - 30}' cy='290' r='38' fill='#EDE7F2' stroke='#6B4E8C' stroke-width='3'/><path d='M{x - 46} 280 q14 -18 28 0 q10 18 -8 22 q-18 4 -20 -22' fill='#9C82BC'/>")
    b.append(t(x - 30, 352, "weiße Blutkörperchen", 20, "b", "middle", "#6B4E8C") + t(x - 30, 374, "Abwehr", 17, "m", "middle"))
    for dx, dy in ((70, 270), (95, 300), (80, 320)):
        b.append(f"<polygon points='{x + dx},{dy} {x + dx + 12},{dy + 6} {x + dx + 4},{dy + 16} {x + dx - 6},{dy + 8}' fill='{ORANGE}'/>")
    b.append(t(x + 85, 420, "Blutplättchen", 20, "b", "middle", ORANGE) + t(x + 85, 442, "Wundverschluss", 17, "m", "middle"))
    b.append(t(320, 500, "Alle Blutzellen entstehen im roten Knochenmark.", 20, "b", "middle"))
    return svg(W, H, "".join(b), "Blutröhrchen mit 55 Prozent Plasma und 45 Prozent Zellen; rote und weiße Blutkörperchen und Blutplättchen mit ihren Aufgaben")


# ------------------------------------------------------------------ 8 Gerinnung (animiert)
def gerinnung():
    W, H = 640, 470
    b = [t(320, 38, "Blutgerinnung in drei Schritten", 24, "b", "middle")]
    xs = (110, 320, 530)
    for x in xs:
        b.append(f"<rect x='{x - 90}' y='80' width='180' height='240' rx='14' fill='#fff' stroke='{LIGHT}' stroke-width='3'/>")
    # Panel 1: Gefäß verengt sich
    p1 = (f"<path d='M50 160 Q110 {190} 170 160 M50 250 Q110 {220} 170 250' fill='none' stroke='{RED}' stroke-width='10'/>"
          + arrow(110, 120, 110, 168, RUST, 4, 12) + arrow(110, 290, 110, 242, RUST, 4, 12) + t(110, 355, "1  Gefäß verengt sich", 19, "b", "middle"))
    # Panel 2: Plättchen-Pfropf
    p2 = f"<path d='M230 160 H410 M230 250 H410' stroke='{RED}' stroke-width='10'/><rect x='300' y='150' width='40' height='20' fill='#fff'/>"
    for i, (dx, dy) in enumerate(((305, 160), (322, 168), (338, 158), (312, 178), (330, 182))):
        p2 += f"<polygon points='{dx},{dy} {dx + 12},{dy + 6} {dx + 4},{dy + 16} {dx - 6},{dy + 8}' fill='{ORANGE}'/>"
    p2 += t(320, 355, "2  Plättchen-Pfropf", 19, "b", "middle")
    # Panel 3: Fibrinnetz
    p3 = f"<path d='M440 160 H620 M440 250 H620' stroke='{RED}' stroke-width='10'/>"
    for i in range(6):
        p3 += f"<line x1='{470 + i * 20}' y1='140' x2='{500 + i * 12}' y2='230' stroke='#D9B44A' stroke-width='3'/><line x1='{460 + i * 22}' y1='220' x2='{520 + i * 10}' y2='150' stroke='#D9B44A' stroke-width='3'/>"
    for dx, dy in ((500, 180), (540, 195), (520, 210)):
        p3 += f"<circle cx='{dx}' cy='{dy}' r='12' fill='{RED}'/>"
    p3 += t(530, 355, "3  Fibrinnetz", 19, "b", "middle")
    s = [blende(p1, [(0, 0), (0.05, 0), (0.08, 1)]), blende(p2, [(0, 0), (0.33, 0), (0.36, 1)]), blende(p3, [(0, 0), (0.62, 0), (0.65, 1)])]
    b.append(szene("".join(s)))
    b.append(t(320, 410, "Fibrinogen (gelöst) wird an der Wunde zu Fibrin-Fäden.", 19, "m", "middle"))
    b.append(t(320, 440, "Im Netz fangen sich Blutkörperchen – die Wunde ist dicht.", 19, "m", "middle"))
    return svg(W, H, "".join(b), "Animation: Blutgerinnung – das Gefäß verengt sich, Blutplättchen bilden einen Pfropf, ein Fibrinnetz fängt Blutkörperchen", anim=True)


# ------------------------------------------------------------------ 9 Blutgruppen (ruhig)
def blutgruppen():
    W, H = 640, 520
    b = [t(320, 38, "AB0-System: Merkmale und Antikörper", 24, "b", "middle")]
    gr = [("A", ["A"], ["B"]), ("B", ["B"], ["A"]), ("AB", ["A", "B"], []), ("0", [], ["A", "B"])]
    for i, (n, ag, ak) in enumerate(gr):
        x = 90 + i * 155
        b.append(t(x, 90, n, 32, "b", "middle"))
        b.append(f"<circle cx='{x}' cy='170' r='46' fill='{RED}'/><circle cx='{x}' cy='170' r='20' fill='#8C2A20'/>")
        for j, a in enumerate(ag):
            ang = math.radians(-60 if j == 0 else -120) if len(ag) == 2 else math.radians(-90)
            px, py = x + 52 * math.cos(ang), 170 + 52 * math.sin(ang)
            if a == "A":
                b.append(f"<rect x='{px - 10:.0f}' y='{py - 10:.0f}' width='20' height='20' fill='{TEAL}'/>")
            else:
                b.append(f"<polygon points='{px:.0f},{py - 12:.0f} {px + 12:.0f},{py + 10:.0f} {px - 12:.0f},{py + 10:.0f}' fill='#D99A00'/>")
        b.append(t(x, 250, "Merkmal: " + (" und ".join(ag) if ag else "keines"), 17, "m", "middle"))
        for j, a in enumerate(ak):
            yy = 320 + j * 60
            col = TEAL if a == "A" else "#D99A00"
            b.append(f"<path d='M{x} {yy + 30} V{yy + 10} L{x - 14} {yy - 8} M{x} {yy + 10} L{x + 14} {yy - 8}' fill='none' stroke='{col}' stroke-width='6' stroke-linecap='round'/>")
            b.append(t(x + 22, yy + 20, "Anti-" + a, 17, "b", fill=col))
        if not ak:
            b.append(t(x, 350, "keine", 19, "m", "middle"))
    b.append(t(20, 300, "Antikörper im Plasma:", 18, "b"))
    b.append(t(320, 470, "Antikörper treffen auf ihr Merkmal → das Blut verklumpt.", 20, "b", "middle"))
    b.append(t(320, 500, "■ Merkmal A   ▲ Merkmal B", 18, "m", "middle"))
    return svg(W, H, "".join(b), "Rote Blutkörperchen der Gruppen A, B, AB und 0 mit ihren Merkmalen und darunter die Antikörper im Plasma")


# ------------------------------------------------------------------ 10 Muskel: Beuger und Strecker (animiert)
def muskel():
    W, H = 640, 520
    b = [t(320, 38, "Bizeps beugt, Trizeps streckt", 24, "b", "middle")]
    b.append(f"<rect x='80' y='240' width='260' height='26' rx='12' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/>")          # Oberarmknochen
    b.append(t(150, 300, "Oberarm", 18, "m"))
    unter = (f"<rect x='0' y='-12' width='230' height='24' rx='12' fill='{BONE}' stroke='#8A6A44' stroke-width='4'/>"
             f"<circle cx='240' cy='0' r='22' fill='{SKIN}' stroke='#8A6A44' stroke-width='3'/>")
    winkel = [(0, "0 0 0"), (0.08, "0 0 0"), (0.38, "-80 0 0"), (0.55, "-80 0 0"), (0.85, "0 0 0"), (0.94, "0 0 0")]
    b.append(f"<g transform='translate(345 253)'>{dreh(unter, winkel)}</g>")
    biz = (f"<ellipse cx='210' cy='215' rx='110' ry='22' fill='#C0392B'>"
           f"<animate attributeName='ry' values='22;22;40;40;22;22' keyTimes='0;0.08;0.38;0.55;0.85;1' dur='{ZYK}s' repeatCount='indefinite'/>"
           f"<animate attributeName='rx' values='110;110;90;90;110;110' keyTimes='0;0.08;0.38;0.55;0.85;1' dur='{ZYK}s' repeatCount='indefinite'/></ellipse>")
    tri = (f"<ellipse cx='210' cy='292' rx='110' ry='30' fill='#B05A3A'>"
           f"<animate attributeName='ry' values='30;30;18;18;30;30' keyTimes='0;0.08;0.38;0.55;0.85;1' dur='{ZYK}s' repeatCount='indefinite'/></ellipse>")
    b.append(biz + tri)
    b.append(t(210, 175, "Bizeps (Beuger)", 21, "b", "middle", "#C0392B"))
    b.append(t(210, 360, "Trizeps (Strecker)", 21, "b", "middle", "#B05A3A"))
    b.append(t(345, 420, "Ellbogen: Scharniergelenk", 18, "m", "middle"))
    s = [schritt("1  Beugen: Bizeps zieht sich zusammen", 0.06, 0.5, 320, 470, 21, "middle", "#C0392B"),
         schritt("2  Strecken: jetzt zieht der Trizeps", 0.55, 0.92, 320, 470, 21, "middle", "#B05A3A")]
    b.append(szene("".join(s)))
    b.append(t(320, 505, "Muskeln ziehen nur – nie drücken.", 19, "m", "middle"))
    return svg(W, H, "".join(b), "Animation: Der Unterarm wird gebeugt, der Bizeps wird kurz und dick; beim Strecken zieht der Trizeps", anim=True)


# ------------------------------------------------------------------ 11 Hebel beim Heben (ruhig, Vergleich)
def hebel():
    W, H = 640, 470
    b = [t(320, 38, "Gleiche Kiste – anderer Hebel", 24, "b", "middle")]
    for k, (x, weit, txt, kraft) in enumerate(((160, 30, "nah am Körper", 2), (470, 110, "weit vor dem Körper", 6))):
        b.append(f"<circle cx='{x}' cy='110' r='26' fill='{SKIN}' stroke='#8A6A44' stroke-width='3'/>")
        b.append(f"<line x1='{x}' y1='136' x2='{x}' y2='290' stroke='{INK}' stroke-width='10' stroke-linecap='round'/>")
        b.append(f"<line x1='{x}' y1='290' x2='{x - 30}' y2='400' stroke='{INK}' stroke-width='10' stroke-linecap='round'/><line x1='{x}' y1='290' x2='{x + 30}' y2='400' stroke='{INK}' stroke-width='10' stroke-linecap='round'/>")
        b.append(f"<line x1='{x}' y1='170' x2='{x + weit}' y2='220' stroke='{INK}' stroke-width='8' stroke-linecap='round'/>")
        b.append(f"<rect x='{x + weit - 10}' y='215' width='56' height='44' rx='4' fill='#7A6A44'/>")
        b.append(f"<line x1='{x}' y1='250' x2='{x + weit + 18}' y2='250' stroke='{TEAL}' stroke-width='3' stroke-dasharray='6 4'/>")
        b.append(t(x + (weit + 18) / 2, 280, "Lastarm", 16, "b", "middle", TEAL))
        b.append(arrow(x - 18, 180, x - 18, 180 + 28 * kraft, RED, 4 + kraft, 16))
        b.append(t(x, 440, txt, 21, "b", "middle"))
    b.append(t(60, 170, "Kraft der", 16, "b", "middle", RED) + t(60, 190, "Rückenmuskeln", 16, "b", "middle", RED))
    b.append(t(320, 466, "Längerer Lastarm → die Rückenmuskeln müssen viel stärker ziehen.", 18, "m", "middle"))
    return svg(W, H, "".join(b), "Vergleich: Kiste nah am Körper mit kurzem Lastarm und kleinem Kraftpfeil im Rücken, Kiste weit vorne mit langem Lastarm und großem Kraftpfeil")


# ------------------------------------------------------------------ 12 Überblick (ruhig)
def ueberblick():
    W, H = 640, 520
    b = [t(320, 38, "Der Körper unter Belastung", 24, "b", "middle")]
    box = lambda x, y, titel, zeile, col: (f"<rect x='{x - 120}' y='{y - 50}' width='240' height='100' rx='18' fill='#fff' stroke='{col}' stroke-width='5'/>"
                                           + t(x, y - 8, titel, 26, "b", "middle", col) + t(x, y + 24, zeile, 18, "m", "middle"))
    b.append(box(170, 130, "HERZ", "pumpt: rechts Lunge, links Körper", RED))
    b.append(box(470, 130, "BLUT", "bringt Sauerstoff, wehrt ab", "#8C2A20"))
    b.append(box(470, 380, "MUSKELN", "ziehen an den Knochen", "#B05A3A"))
    b.append(box(170, 380, "KNOCHEN", "tragen, schützen, bilden Blut", "#8A6A44"))
    b.append(arrow(292, 120, 348, 120, RED, 5) + t(320, 100, "pumpt", 16, "m", "middle"))
    b.append(arrow(470, 182, 470, 328, "#8C2A20", 5) + t(480, 260, "Sauerstoff", 17, "m"))
    b.append(arrow(348, 380, 292, 380, "#B05A3A", 5) + t(320, 365, "Sehnen", 16, "m", "middle"))
    b.append(arrow(220, 328, 420, 182, "#8A6A44", 5) + t(250, 245, "Knochenmark", 17, "m") + t(250, 265, "bildet Blut", 17, "m"))
    b.append(t(320, 480, "Bei Belastung arbeiten alle vier zusammen.", 20, "b", "middle"))
    return svg(W, H, "".join(b), "Vier Kästen HERZ, BLUT, MUSKELN, KNOCHEN mit Pfeilen: Herz pumpt Blut, Blut bringt Sauerstoff zu den Muskeln, Muskeln ziehen an Knochen, Knochenmark bildet Blut")


TEILE = {"herz.svg": herz, "kreislauf.svg": kreislauf, "gefaesse.svg": gefaesse, "blutdruck.svg": blutdruck, "knochen.svg": knochen, "gelenke.svg": gelenke,
         "blut.svg": blut, "gerinnung.svg": gerinnung, "blutgruppen.svg": blutgruppen, "muskel.svg": muskel, "hebel.svg": hebel, "ueberblick.svg": ueberblick}

if __name__ == "__main__":
    for name, fn in TEILE.items():
        s = fn(); save(name, s); print(name, len(s) // 1024, "KB")
