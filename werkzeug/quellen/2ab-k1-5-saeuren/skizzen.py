"""Eigene Grafiken (SVG) für NAWI 2AB K1.5 Säuren und Basen – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-5-saeuren/skizzen.py   → schreibt 2ab-nawi/k1-5-saeuren/img/*.svg
Handy zuerst: Breite 640, Schrift mindestens 20. Animationen (SMIL) laufen auch in <img>; bei »weniger Bewegung« stehen sie still.
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


# ------------------------------------------------------------------ 1 Säure in Wasser (HCl gibt H⁺ an H2O)
def saeure():
    W, H = 640, 520
    b = [t(24, 44, "Säure in Wasser: ein Proton wechselt den Platz", 26, "b"),
         t(24, 74, "Chlorwasserstoff (HCl) gibt sein H⁺ an ein Wassermolekül ab.", 20, "m")]
    # vorher
    b += [kreis(80, 170, 26, CL_COL, "Cl", 22, WHITE), proton(118, 170), wasser(220, 160)]
    b += [t(100, 230, "HCl", 22, "b", "middle"), t(220, 230, "H₂O", 22, "b", "middle")]
    b.append(arrow(285, 170, 345, 170, OLIVE, 5))
    # nachher
    b += [kreis(400, 170, 26, CL_COL, "Cl", 22, WHITE), t(432, 148, "−", 28, "b", "middle", BLUE), oxonium(530, 168)]
    b += [t(400, 230, "Cl⁻", 22, "b", "middle"), t(530, 230, "H₃O⁺", 22, "b", "middle")]
    b.append(t(400, 258, "Säurerest", 18, "m", "middle"))
    b.append(t(545, 258, "macht sauer", 18, "m", "middle"))
    b.append(f"<line x1='24' y1='290' x2='616' y2='290' stroke='{LIGHT}' stroke-width='3'/>")
    b.append(t(24, 326, "Säuren im Alltag", 22, "b"))
    items = [("Zitrone", "Zitronensäure", "#F4D03F", "pH ~2,4"), ("Cola", "Phosphorsäure", "#5D4037", "pH ~2,5–3"),
             ("Mineralwasser", "Kohlensäure", "#AED6F1", "pH ~5–6"), ("Magen", "Salzsäure", "#E8A598", "pH 1–2")]
    for i, (n, s_, c, ph) in enumerate(items):
        x = 24 + i * 152
        b.append(f"<rect x='{x}' y='344' width='140' height='150' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
        b.append(f"<circle cx='{x + 70}' cy='388' r='26' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b += [t(x + 70, 440, n, 20, "b", "middle"), t(x + 70, 462, s_, 16, "m", "middle"), t(x + 70, 484, ph, 17, "b", "middle", RUST)]
    save("saeure.svg", svg(W, H, "".join(b), "HCl gibt ein Proton an Wasser ab; Säuren im Alltag"))


# ------------------------------------------------------------------ 2 Lauge (NaOH in Wasser) + Alltag
def lauge():
    W, H = 640, 500
    b = [t(24, 44, "Lauge: OH⁻-Ionen machen basisch", 26, "b"),
         t(24, 74, "Natriumhydroxid löst sich – Na⁺ und OH⁻ schwimmen getrennt.", 20, "m")]
    # Kristall
    for r in range(3):
        for c in range(3):
            x, y = 70 + c * 34, 130 + r * 34
            if (r + c) % 2 == 0: b.append(kreis(x, y, 14, NA_COL, "Na", 12, WHITE))
            else: b.append(kreis(x, y, 14, O_COL, "OH", 11, WHITE))
    b.append(t(104, 252, "NaOH (fest)", 20, "b", "middle"))
    b.append(arrow(175, 165, 240, 165, OLIVE, 5))
    b.append(t(208, 150, "Wasser", 16, "m", "middle"))
    b.append(f"<rect x='255' y='100' width='360' height='170' rx='14' fill='#E3F0F7' stroke='{TEAL}' stroke-width='3'/>")
    pos = [(300, 150, "na"), (380, 220, "oh"), (450, 140, "na"), (540, 210, "oh"), (330, 230, "oh"), (560, 140, "na")]
    for x, y, k in pos:
        if k == "na": b += [kreis(x, y, 16, NA_COL, "Na", 13, WHITE), t(x + 20, y - 12, "+", 22, "b", "middle", RED)]
        else: b.append(hydroxid(x, y, 0.75))
    b.append(t(435, 292, "Natronlauge: viele OH⁻", 20, "b", "middle", TEAL))
    b.append(f"<line x1='24' y1='318' x2='616' y2='318' stroke='{LIGHT}' stroke-width='3'/>")
    b.append(t(24, 352, "Laugen im Alltag und im Dienst", 22, "b"))
    items = [("Rohrreiniger", "pH über 13", "löst Haare, Fett, Haut"), ("Laugenbrezel", "kurz in Lauge getaucht", "beim Backen harmlos"),
             ("nasser Beton", "pH 12–13", "Handschuhe, Brille!")]
    for i, (n, ph, s_) in enumerate(items):
        x = 24 + i * 202
        b.append(f"<rect x='{x}' y='368' width='188' height='112' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
        b += [t(x + 94, 404, n, 21, "b", "middle"), t(x + 94, 432, ph, 18, "b", "middle", BLUE), t(x + 94, 460, s_, 16, "m", "middle")]
    save("lauge.svg", svg(W, H, "".join(b), "Natriumhydroxid löst sich in Na-plus und OH-minus; Laugen im Alltag"))


# ------------------------------------------------------------------ 3 Protonen-Pingpong (animiert)
def protolyse():
    W, H = 640, 520
    b = [t(24, 44, "Protonen-Pingpong", 28, "b"), t(24, 74, "Die Säure gibt ab, die Base fängt. Der rote Ball ist das Proton.", 20, "m")]
    D = "3.2s"
    # Zeile 1: HCl + H2O
    y1 = 190
    b += [t(24, 112, "1  HCl + H₂O → Cl⁻ + H₃O⁺", 22, "b", fill=OLIVE)]
    b += [kreis(90, y1, 26, CL_COL, "Cl", 22, WHITE), wasser(330, y1 - 8)]
    b.append(f"<g><circle cx='128' cy='{y1}' r='13' fill='{RED}' stroke='{INK}' stroke-width='2'>"
             f"<animate attributeName='cx' values='128;128;330;330' keyTimes='0;0.25;0.6;1' dur='{D}' repeatCount='indefinite'/>"
             f"<animate attributeName='cy' values='{y1};{y1};{y1 - 34};{y1 - 34}' keyTimes='0;0.25;0.6;1' dur='{D}' repeatCount='indefinite'/></circle></g>")
    b += [t(90, y1 + 54, "Säure (gibt ab)", 18, "b", "middle", RED), t(330, y1 + 54, "Base (fängt)", 18, "b", "middle", BLUE)]
    b.append(f"<path d='M140 {y1 - 22} Q 230 {y1 - 70} 316 {y1 - 40}' fill='none' stroke='{RED}' stroke-width='3' stroke-dasharray='8 7'/>")
    b += [t(470, y1 - 6, "→ Cl⁻", 24, "b"), t(470, y1 + 26, "→ H₃O⁺", 24, "b")]
    b.append(f"<line x1='24' y1='262' x2='616' y2='262' stroke='{LIGHT}' stroke-width='3'/>")
    # Zeile 2: NH3 + H2O
    y2 = 375
    b += [t(24, 300, "2  NH₃ + H₂O → NH₄⁺ + OH⁻", 22, "b", fill=OLIVE)]
    b += [kreis(88, y2 + 8, 11, H_COL, "H", 13), kreis(110, y2 - 8, 20, O_COL, "O", 18, WHITE)]
    b += [kreis(330, y2, 24, N_COL, "N", 20, WHITE), kreis(296, y2 + 22, 11, H_COL, "H", 13), kreis(364, y2 + 22, 11, H_COL, "H", 13), kreis(330, y2 + 36, 11, H_COL, "H", 13)]
    b.append(f"<g><circle cx='132' cy='{y2 + 8}' r='13' fill='{RED}' stroke='{INK}' stroke-width='2'>"
             f"<animate attributeName='cx' values='132;132;330;330' keyTimes='0;0.25;0.6;1' dur='{D}' begin='0.4s' repeatCount='indefinite'/>"
             f"<animate attributeName='cy' values='{y2 + 8};{y2 + 8};{y2 - 34};{y2 - 34}' keyTimes='0;0.25;0.6;1' dur='{D}' begin='0.4s' repeatCount='indefinite'/></circle></g>")
    b += [t(110, y2 + 66, "Säure: Wasser!", 18, "b", "middle", RED), t(330, y2 + 74, "Base: Ammoniak", 18, "b", "middle", BLUE)]
    b += [t(470, y2 - 6, "→ OH⁻", 24, "b"), t(470, y2 + 26, "→ NH₄⁺", 24, "b")]
    b.append(f"<rect x='24' y='470' width='592' height='38' rx='10' fill='{OLIVE}'/>")
    b.append(t(320, 496, "Wasser kann beides – es ist ein Ampholyt.", 20, "b", "middle", WHITE))
    save("protolyse.svg", svg(W, H, "".join(b), "Protonenübergang: HCl gibt an Wasser ab, Wasser gibt an Ammoniak ab", anim=True))


# ------------------------------------------------------------------ 4 pH-Skala mit Beispielen
def phskala():
    W, H = 640, 470
    b = [t(24, 44, "Die pH-Skala", 28, "b"), t(24, 74, "Unter 7 sauer · 7 neutral · über 7 basisch", 20, "m")]
    x0, w = 30, 580 / 15
    bsp = [(1.5, "Magensaft"), (2.4, "Zitrone"), (2.5, "Cola"), (5, "Kaffee"), (5, "Haut"), (7, "reines Wasser"),
           (7.4, "Blut"), (8.1, "Meer"), (8.3, "Natron"), (9.5, "Seife"), (12.5, "nasser Beton")]
    oben = [(1.5, "Magensaft", 0, "middle"), (2.6, "Cola, Zitrone", 1, "middle"), (5, "Kaffee, Haut", 0, "middle"), (7, "Wasser", 1, "end"),
            (7.4, "Blut 7,4", 3, "middle"), (8.1, "Meer 8,1", 2, "start"), (9.5, "Seife", 0, "middle"), (12.5, "nasser Beton", 0, "middle")]
    for i in range(15):
        b.append(f"<rect x='{x0 + i * w:.1f}' y='250' width='{w + 0.6:.1f}' height='54' fill='{UI[i]}'/>")
        b.append(t(x0 + i * w + w / 2, 286, str(i), 20, "b", "middle", WHITE if i not in (4, 5, 6) else INK))
    b.append(f"<rect x='{x0}' y='250' width='580' height='54' fill='none' stroke='{INK}' stroke-width='2'/>")
    for ph, lab, lev, anc in oben:
        x = x0 + (ph + 0.5) * w
        y = 230 - lev * 34
        b.append(f"<line x1='{x:.1f}' y1='{y + 6 if anc == 'middle' else y - 14}' x2='{x:.1f}' y2='250' stroke='{INK}' stroke-width='1.5'/>")
        b.append(t(x + (-5 if anc == "end" else 5 if anc == "start" else 0), y, lab, 17, "b", anc))
    b += [t(x0 + 3 * w, 336, "SAUER", 22, "b", "middle", RED), t(x0 + 7.5 * w, 336, "NEUTRAL", 20, "b", "middle", GREEN), t(x0 + 12 * w, 336, "BASISCH", 22, "b", "middle", BLUE)]
    b.append(arrow(x0 + 6.8 * w, 360, x0 + 0.3 * w, 360, RED, 4))
    b.append(arrow(x0 + 8.2 * w, 360, x0 + 14.7 * w, 360, BLUE, 4))
    b += [t(x0 + 3.5 * w, 386, "immer mehr H₃O⁺", 18, "b", "middle", RED), t(x0 + 11.5 * w, 386, "immer mehr OH⁻", 18, "b", "middle", BLUE)]
    b.append(f"<rect x='24' y='408' width='592' height='46' rx='10' fill='{OLIVE}'/>")
    b.append(t(320, 439, "Jede Stufe = Faktor 10:  pH 2 hat 1000-mal so viele H₃O⁺ wie pH 5", 19, "b", "middle", WHITE))
    save("phskala.svg", svg(W, H, "".join(b), "pH-Skala von 0 bis 14 mit Beispielen aus Alltag und Körper"))


# ------------------------------------------------------------------ 5 Rotkraut-Farbskala
def rotkraut():
    W, H = 640, 330
    b = [t(24, 44, "Rotkrautsaft als Indikator", 28, "b"), t(24, 74, "Ungefähre Farben – jeder Saft ist ein bisschen anders.", 20, "m")]
    x = 24
    breit = 592 / len(RK)
    for i, (a, e, c, wort, farbe) in enumerate(RK):
        xx = x + i * breit
        b.append(f"<path d='M{xx + 14:.1f} 100 h{breit - 28:.1f} l-6 120 a10 10 0 0 1 -10 10 h{-(breit - 48):.1f} a10 10 0 0 1 -10 -10 z' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b.append(t(xx + breit / 2, 262, f"pH {a}" if a == e else f"pH {a}–{e}", 17, "b", "middle"))
        b.append(t(xx + breit / 2, 286, farbe, 16, "", "middle"))
        b.append(t(xx + breit / 2, 310, wort, 13, "m", "middle"))
    save("rotkraut.svg", svg(W, H, "".join(b), "Farben des Rotkrautsafts von stark sauer rot bis stark basisch gelb"))


# ------------------------------------------------------------------ 6 Versuch: Ablauf
def versuch():
    W, H = 640, 560
    b = [t(24, 44, "VERSUCH K1.5-V1: so messt ihr", 26, "b", fill=RUST), t(24, 74, "Tüpfelplatte · Indikatorpapier · Farbskala", 20, "m")]
    # Tüpfelplatte
    b.append(f"<rect x='24' y='96' width='300' height='190' rx='16' fill='{WHITE}' stroke='{INK}' stroke-width='2'/>")
    proben = ["Zitrone", "Cola", "Mineral", "Leitung", "Natron", "Seife"]
    farben = ["#E53935", "#F4511E", "#FDD835", "#7CB342", "#00897B", "#1E88E5"]
    for i, p in enumerate(proben):
        cx, cy = 74 + (i % 3) * 100, 150 + (i // 3) * 86
        b.append(f"<circle cx='{cx}' cy='{cy}' r='26' fill='#EEF3F8' stroke='{MUTED}' stroke-width='2'/>")
        b += [t(cx, cy + 8, str(i + 1), 22, "b", "middle"), t(cx, cy + 46, p, 15, "m", "middle")]
    b.append(t(174, 310, "1 Tropfen rein (ca. 10 Tropfen je Mulde)", 17, "b", "middle"))
    # Papierstreifen
    b.append(t(360, 120, "2 Indikatorpapier eintauchen,", 18, "b"))
    b.append(t(360, 144, "   auf das Blatt legen", 18, "b"))
    for i, c in enumerate(farben):
        b.append(f"<rect x='{360 + i * 42}' y='160' width='30' height='70' rx='4' fill='#F3E9A8' stroke='{MUTED}' stroke-width='1.5'/>")
        b.append(f"<rect x='{360 + i * 42}' y='196' width='30' height='34' rx='4' fill='{c}'/>")
        b.append(t(375 + i * 42, 252, str(i + 1), 18, "b", "middle"))
    # Farbskala
    b.append(t(24, 360, "3 Farbe an der Farbskala am Lehrertisch ablesen", 18, "b"))
    for i in range(15):
        b.append(f"<rect x='{24 + i * 26}' y='374' width='26' height='40' fill='{UI[i]}'/>")
        b.append(t(37 + i * 26, 436, str(i), 15, "b", "middle"))
    # pH-Meter
    b.append(f"<rect x='450' y='330' width='150' height='180' rx='18' fill='{OLIVE}'/>")
    b.append(f"<rect x='470' y='350' width='110' height='54' rx='8' fill='#D7E8C0'/>")
    b.append(t(525, 389, "2,5", 32, "b", "middle"))
    b.append(t(525, 440, "pH-Meter", 20, "b", "middle", WHITE))
    b.append(t(525, 466, "DEMO K1.5-D2", 16, "b", "middle", "#F2D98A"))
    b.append(f"<line x1='525' y1='510' x2='525' y2='540' stroke='{INK}' stroke-width='6'/>")
    b.append(t(24, 470, "4 Werte eintragen – jeder im eigenen", 18, "b"))
    b.append(t(24, 494, "   Arbeitsblatt (Aufgabe 6, c1–c6)", 18, "b"))
    b.append(t(24, 530, "Papier = Schätzung · pH-Meter = genauer", 18, "b", fill=RUST))
    save("versuch.svg", svg(W, H, "".join(b), "Ablauf des pH-Versuchs mit Tüpfelplatte, Indikatorpapier, Farbskala und pH-Meter"))


# ------------------------------------------------------------------ 7 Neutralisation (animiert)
def neutralisation():
    W, H = 640, 520
    b = [t(24, 44, "Neutralisation", 28, "b"), t(24, 74, "H₃O⁺ und OH⁻ treffen sich – es entsteht Wasser.", 20, "m")]
    # Becher links und rechts
    for x, lab, col in ((24, "Salzsäure", "#FBE3E0"), (336, "Natronlauge", "#E3ECF8")):
        b.append(f"<path d='M{x + 10} 100 v150 a14 14 0 0 0 14 14 h252 a14 14 0 0 0 14 -14 v-150' fill='{col}' stroke='{INK}' stroke-width='3'/>")
        b.append(t(x + 150, 290, lab, 21, "b", "middle"))
    b += [oxonium(110, 170, 0.8), kreis(220, 200, 18, CL_COL, "Cl", 15, WHITE), t(244, 182, "−", 24, "b", "middle", BLUE)]
    b += [hydroxid(420, 175, 0.85), kreis(540, 200, 18, NA_COL, "Na", 14, WHITE), t(564, 182, "+", 24, "b", "middle", RED)]
    b.append(f"<line x1='24' y1='312' x2='616' y2='312' stroke='{LIGHT}' stroke-width='3'/>")
    # Gleichung animiert
    b.append(t(320, 350, "H₃O⁺  +  OH⁻   →   2 H₂O", 28, "b", "middle"))
    b.append("<g opacity='0'><animate attributeName='opacity' values='0;0;1;1;0' keyTimes='0;0.35;0.5;0.9;1' dur='4s' repeatCount='indefinite'/>"
             + wasser(220, 410, 0.9) + wasser(420, 410, 0.9) + "</g>")
    b.append(t(320, 470, "Na⁺ und Cl⁻ bleiben übrig: Kochsalzlösung (ein Salz)", 19, "b", "middle", OLIVE))
    b.append(f"<rect x='24' y='484' width='592' height='26' rx='8' fill='{ORANGE}'/>")
    b.append(t(320, 503, "Salzsäure + Natronlauge: Das Glas wird warm (exotherm).", 17, "b", "middle", WHITE))
    save("neutralisation.svg", svg(W, H, "".join(b), "Salzsäure und Natronlauge neutralisieren sich zu Kochsalzlösung und Wasser", anim=True))


# ------------------------------------------------------------------ 8 Blut-Puffer
def blutpuffer():
    W, H = 640, 520
    b = [t(24, 44, "Dein Blut bleibt bei pH 7,4", 28, "b"), t(24, 74, "Puffer fängt H⁺ ab – die Lunge atmet CO₂ aus.", 20, "m")]
    # Muskel, Blut, Lunge
    box = [(24, "Muskel", "bildet CO₂ und H⁺", "#F6D3CF"), (232, "Blut", "Puffer: HCO₃⁻ fängt H⁺", "#F3C6C6"), (440, "Lunge", "atmet CO₂ aus", "#D6E8F2")]
    for x, n, s_, c in box:
        b.append(f"<rect x='{x}' y='100' width='176' height='120' rx='16' fill='{c}' stroke='{INK}' stroke-width='2'/>")
        b += [t(x + 88, 146, n, 24, "b", "middle"), t(x + 88, 180, s_, 15, "", "middle")]
    b.append(arrow(204, 160, 228, 160, INK, 4))
    b.append(arrow(412, 160, 436, 160, INK, 4))
    b.append(t(320, 262, "HCO₃⁻ + H⁺  →  H₂CO₃  →  H₂O + CO₂", 24, "b", "middle"))
    b.append(t(320, 292, "Hydrogencarbonat fängt das Proton – als CO₂ verlässt es den Körper.", 17, "m", "middle"))
    # Skala-Ausschnitt
    x0, x1 = 60, 580
    def px(ph): return x0 + (ph - 6.8) / (7.8 - 6.8) * (x1 - x0)
    b.append(f"<rect x='{x0}' y='340' width='{x1 - x0}' height='34' rx='6' fill='{LIGHT}'/>")
    b.append(f"<rect x='{px(7.35):.1f}' y='340' width='{px(7.45) - px(7.35):.1f}' height='34' fill='{GREEN}'/>")
    for ph in (6.8, 7.0, 7.2, 7.4, 7.6, 7.8):
        b.append(t(px(ph), 398, str(ph).replace(".", ","), 17, "b", "middle"))
    b.append(t(px(7.4), 332, "normal 7,35–7,45", 17, "b", "middle", OLIVE))
    b.append(f"<line x1='{px(7.13):.1f}' y1='336' x2='{px(7.13):.1f}' y2='378' stroke='{RED}' stroke-width='4'/>")
    b.append(t(px(7.13), 424, "nach hartem Sprint: 7,13 (kurz, normal)", 16, "b", "middle", RED))
    b.append(t(px(6.9), 360, "Azidose", 15, "b", "middle", RUST))
    b.append(t(px(7.65), 360, "Alkalose", 15, "b", "middle", BLUE))
    b.append(f"<rect x='24' y='446' width='592' height='58' rx='10' fill='{OLIVE}'/>")
    b.append(t(320, 470, "Schneller atmen = mehr CO₂ raus = weniger Kohlensäure", 18, "b", "middle", WHITE))
    b.append(t(320, 494, "Studie: Radsportler, Plasma-pH 7,35 → 7,13 (Med Sci Sports Exerc 2023)", 14, "", "middle", "#E7EED8"))
    save("blutpuffer.svg", svg(W, H, "".join(b), "Muskel, Blut und Lunge halten den Blut-pH mit Puffer und Atmung bei 7,4"))


# ------------------------------------------------------------------ 9 Überblick
def ueberblick():
    W, H = 640, 440
    b = [t(320, 44, "Von sauer bis basisch", 28, "b", "middle")]
    b.append(f"<rect x='24' y='66' width='280' height='150' rx='16' fill='#FBE3E0' stroke='{RED}' stroke-width='3'/>")
    b.append(f"<rect x='336' y='66' width='280' height='150' rx='16' fill='#E3ECF8' stroke='{BLUE}' stroke-width='3'/>")
    b += [t(164, 100, "SAUER", 26, "b", "middle", RED), t(476, 100, "BASISCH", 26, "b", "middle", BLUE)]
    b += [oxonium(110, 160, 0.75), t(210, 150, "H₃O⁺", 22, "b", "middle"), t(210, 180, "pH unter 7", 17, "", "middle"), t(210, 204, "Lackmus rot", 17, "", "middle")]
    b += [hydroxid(420, 160, 0.85), t(522, 150, "OH⁻", 22, "b", "middle"), t(522, 180, "pH über 7", 17, "", "middle"), t(522, 204, "Lackmus blau", 17, "", "middle")]
    for i in range(15):
        b.append(f"<rect x='{24 + i * 39.47:.1f}' y='236' width='40' height='30' fill='{UI[i]}'/>")
    b.append(t(320, 288, "7 = neutral", 18, "b", "middle"))
    b.append(f"<rect x='24' y='304' width='292' height='120' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
    b += [t(170, 334, "Protonen-Pingpong", 20, "b", "middle"), proton(170, 372), arrow(70, 372, 150, 372, RED, 3), arrow(190, 372, 270, 372, RED, 3),
          t(70, 410, "Säure gibt", 16, "b", "middle", RED), t(270, 410, "Base fängt", 16, "b", "middle", BLUE)]
    b.append(f"<rect x='326' y='304' width='290' height='120' rx='14' fill='{WHITE}' stroke='{LIGHT}' stroke-width='3'/>")
    b += [t(471, 334, "Neutralisation", 20, "b", "middle"), t(471, 372, "H₃O⁺ + OH⁻ → 2 H₂O", 20, "b", "middle"),
          t(471, 404, "Säure + Base → Salz + Wasser", 16, "", "middle")]
    save("ueberblick.svg", svg(W, H, "".join(b), "Überblick: sauer und basisch, pH-Skala, Protonenübergang und Neutralisation"))


TEILE = {"saeure.svg": saeure, "lauge.svg": lauge, "protolyse.svg": protolyse, "phskala.svg": phskala, "rotkraut.svg": rotkraut,
         "versuch.svg": versuch, "neutralisation.svg": neutralisation, "blutpuffer.svg": blutpuffer, "ueberblick.svg": ueberblick}
if __name__ == "__main__":
    for n, f in TEILE.items():
        f()
    print("geschrieben:", ", ".join(TEILE))
