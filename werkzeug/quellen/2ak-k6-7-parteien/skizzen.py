"""Eigene Grafiken (SVG) für PBGW 2AK K6–7 Wahlrecht und Parteien – alles selbst gezeichnet, keine Buchabbildungen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ak-k6-7-parteien/skizzen.py   → schreibt 2ak-pbgw/k6-7-parteien/img/*.svg
Handy zuerst: Hochformat, Breite 440, Schrift mindestens 17. Animationen (SMIL) zeigen Vorgänge (Wahlrecht wächst, Lager → Parteien);
das Grundbild ohne Animation zeigt den Endzustand. Zustände (Sitzordnung, Klubs, Prüffragen) bleiben ruhig.
Parteifarben nur zur Unterscheidung; Sitzverteilung nach Klubgröße, nicht die echte Sitzordnung im Saal."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
IMG = os.path.join(ROOT, I.ORDNER, "img")
os.makedirs(IMG, exist_ok=True)

BG, INK, OLIVE, GREEN, ORANGE, TEAL, RUST, MUTED = "#F2F3EE", "#1F2A1C", "#3B4A2F", "#7FA83A", "#D9772B", "#2E7D8C", "#8C3B2E", "#5E6652"
LIGHT, WHITE, GREY = "#DFE5D0", "#FFFFFF", "#B8BCB0"
PF = {"FPÖ": "#2A5C9C", "ÖVP": "#1B8A8C", "SPÖ": "#C0392B", "NEOS": "#B5307A", "Grüne": "#4E8A2A", "ohne": "#8A8A8A"}
FONT = "'Source Sans 3','Carlito','Segoe UI',Arial,sans-serif"
W = 440
L, R, M = 20, 420, 220


def svg(w, h, body, title):
    st = f"<style>text{{font-family:{FONT};fill:{INK}}} .b{{font-weight:700}} .m{{fill:{MUTED}}}</style>"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{st}<rect width='{w}' height='{h}' rx='18' fill='{BG}'/>{body}</svg>")


def t(x, y, s, size=20, cls="", anchor="start", fill=None):
    f = f" style='fill:{fill}'" if fill else ""
    c = f" class='{cls}'" if cls else ""
    return f"<text x='{x}' y='{y}' font-size='{size}' text-anchor='{anchor}'{c}{f}>{s}</text>"


def arrow(x1, y1, x2, y2, col=INK, w=4, head=13):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2 - 0.6 * head * math.cos(a):.1f}' y2='{y2 - 0.6 * head * math.sin(a):.1f}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<polygon points='{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{col}'/>")


def box(x, y, w, h, fill, rx=12, stroke=None):
    s = f" stroke='{stroke}' stroke-width='2'" if stroke else ""
    return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' fill='{fill}'{s}/>"


def zeilen(x, y, liste, size=19, cls="", anchor="middle", fill=None, abst=1.2):
    return "".join(t(x, round(y + k * size * abst), z, size, cls, anchor, fill) for k, z in enumerate(liste))


def save(name, s):
    open(os.path.join(IMG, name), "w", encoding="utf-8").write(s)


# ---- Animation: Gleichtakt, Endzustand = Grundbild
ZYK = 14
ENDE, ZURUECK = 0.96, 0.985


def blende(inner, start, dur=ZYK):
    """Erscheint ab Anteil start und bleibt bis zum Ende; Schleife."""
    a = max(0.001, start); b = min(ENDE - 0.02, start + 0.04)
    return (f"<g opacity='1'>{inner}<animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;{a:.3f};{b:.3f};{ENDE:.3f};{ZURUECK:.3f};1' dur='{dur}s' repeatCount='indefinite'/></g>")


def figur(x, y, col, frau=False, s=1.0, klein=False):
    """Kleine Person: Kopf + Körper (Frau mit Rock). y = Fuß."""
    s = s * (0.78 if klein else 1.0)
    kopf = f"<circle cx='{x:.1f}' cy='{y - 30 * s:.1f}' r='{6 * s:.1f}' fill='{col}'/>"
    if frau:
        koerper = f"<path d='M{x - 3 * s:.1f},{y - 23 * s:.1f} L{x + 3 * s:.1f},{y - 23 * s:.1f} L{x + 9 * s:.1f},{y - 6 * s:.1f} L{x - 9 * s:.1f},{y - 6 * s:.1f} Z' fill='{col}'/>"
    else:
        koerper = f"<rect x='{x - 6 * s:.1f}' y='{y - 23 * s:.1f}' width='{12 * s:.1f}' height='{17 * s:.1f}' rx='{3 * s:.1f}' fill='{col}'/>"
    beine = (f"<rect x='{x - 5 * s:.1f}' y='{y - 7 * s:.1f}' width='{3.5 * s:.1f}' height='{7 * s:.1f}' fill='{col}'/>"
             f"<rect x='{x + 1.5 * s:.1f}' y='{y - 7 * s:.1f}' width='{3.5 * s:.1f}' height='{7 * s:.1f}' fill='{col}'/>")
    return kopf + koerper + beine


def wahlrecht():
    H = 712
    b = [t(L, 42, "Wer durfte wählen?", 30, "b"), t(L, 70, "Jede Reihe: 5 Männer, 5 Frauen, 2 Jugendliche", 18, "m"),
         t(L, 92, "vereinfacht – keine genauen Anteile", 17, "m")]
    REIHEN = [("1861", "Kurien: nur mit Besitz", [1, 0, 0, 0, 0], [0] * 5, [0, 0], OLIVE),
              ("1873", "Zensus: nur mit Steuer", [1, 0, 0, 0, 0], [0] * 5, [0, 0], OLIVE),
              ("1896", "5. Kurie für Arbeiter", [1, 2, 2, 2, 2], [0] * 5, [0, 0], OLIVE),
              ("1907", "alle Männer ab 24", [1] * 5, [0] * 5, [0, 0], OLIVE),
              ("1918", "auch die Frauen", [1] * 5, [1] * 5, [0, 0], OLIVE),
              ("1933–45", "keine freien Wahlen", [0] * 5, [0] * 5, [0, 0], RUST),
              ("2007", "ab 16", [1] * 5, [1] * 5, [1, 1], OLIVE)]
    y0 = 120
    for k, (jahr, txt, m, f, j, col) in enumerate(REIHEN):
        y = y0 + k * 80
        inner = [box(L, y, R - L, 70, WHITE, 12), t(L + 12, y + 28, jahr, 22, "b", fill=col), t(L + 12, y + 54, txt, 16, "m")]
        x = 214
        for v in m:
            inner.append(figur(x, y + 60, OLIVE if v == 1 else ("#B9C79A" if v == 2 else GREY), False, 0.95)); x += 15
        x += 3
        for v in f:
            inner.append(figur(x, y + 60, TEAL if v else GREY, True, 0.95)); x += 15
        x += 2
        for v in j:
            inner.append(figur(x, y + 60, ORANGE if v else GREY, False, 0.95, klein=True)); x += 13
        if jahr == "1933–45":
            inner.append(f"<line x1='208' y1='{y + 12}' x2='{R - 8}' y2='{y + 62}' stroke='{RUST}' stroke-width='4'/>")
        b.append(blende("".join(inner), 0.03 + k * 0.12))
    b.append(t(L, 682, "dunkel = Mann · hell = Stimme zählt wenig", 15, "m") + t(L, 698, "blau = Frau · orange = 16/17 · grau = darf nicht", 15, "m"))
    save("wahlrecht.svg", svg(W, H, "".join(b), "Wer durfte wählen? Von 1861 nur Männer mit Besitz bis 2007 alle ab 16 – mit der Lücke 1933 bis 1945"))


def lager():
    H = 600
    b = [t(L, 42, "Drei Lager → Parteien heute", 28, "b"), t(L, 70, "Buch S. 27–30", 18, "m")]
    SP = [("deutsch-", "national", "Bürger der Städte", "FPÖ", "1956", PF["FPÖ"]),
          ("christlich-", "sozial", "Kirche, Bauern", "ÖVP", "1945", PF["ÖVP"]),
          ("sozial-", "demokratisch", "Arbeiterinnen", "SPÖ", "1945", PF["SPÖ"])]
    for k, (a, c, wer, partei, jahr, col) in enumerate(SP):
        x = L + k * 136
        b.append(box(x, 90, 128, 150, WHITE, 12, col))
        b.append(zeilen(x + 64, 124, [a, c], 19, "b"))
        b.append(t(x + 64, 180, "um 1900", 16, "m", "middle"))
        b.append(zeilen(x + 64, 208, [wer], 16, "", "middle"))
        pfeil = arrow(x + 64, 248, x + 64, 330, col, 5, 15)
        b.append(blende(pfeil, 0.10 + k * 0.15))
        part = box(x + 14, 340, 100, 80, col, 12) + t(x + 64, 378, partei, 26, "b", "middle", WHITE) + t(x + 64, 406, "seit " + jahr, 17, "", "middle", WHITE)
        b.append(blende(part, 0.16 + k * 0.15))
    neu = (t(L, 470, "Neu dazugekommen:", 20, "b")
           + box(L, 485, 190, 70, PF["Grüne"], 12) + t(L + 95, 518, "Grüne", 24, "b", "middle", WHITE) + t(L + 95, 543, "im Nationalrat seit 1986", 15, "", "middle", WHITE)
           + box(L + 210, 485, 190, 70, PF["NEOS"], 12) + t(L + 305, 518, "NEOS", 24, "b", "middle", WHITE) + t(L + 305, 543, "gegründet 2012", 15, "", "middle", WHITE))
    b.append(blende(neu, 0.66))
    b.append(t(L, 585, "Die Lager sind alt – die Parteien sind jünger.", 17, "m"))
    save("lager.svg", svg(W, H, "".join(b), "Drei Lager um 1900 und die Parteien von heute: deutschnational zu FPÖ, christlichsozial zu ÖVP, sozialdemokratisch zu SPÖ; neu Grüne und NEOS"))


def halbkreis_sitze(cx, cy, n_list, r0=70, rows=8, step=17):
    """Sitze im Halbkreis: n_list = [(Anzahl, Farbe)] von links nach rechts."""
    total = sum(n for n, _ in n_list)
    radien = [r0 + i * step for i in range(rows)]
    gesamt_umfang = sum(radien)
    pro = [round(total * r / gesamt_umfang) for r in radien]
    pro[-1] += total - sum(pro)
    sitze = []
    for r, n in zip(radien, pro):
        for i in range(n):
            ang = math.pi - (i + 0.5) / n * math.pi
            sitze.append((ang, cx + r * math.cos(ang), cy - r * math.sin(ang)))
    sitze.sort(key=lambda s: -s[0])
    farben = [c for n, c in n_list for _ in range(n)]
    return "".join(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='6' fill='{c}'/>" for (a, x, y), c in zip(sitze, farben))


def sitzordnung():
    H = 560
    b = [t(L, 42, "Woher links und rechts kommen", 27, "b"), t(L, 70, "Frankreich 1789 – Blick vom Präsidenten", 18, "m")]
    b.append(halbkreis_sitze(M, 280, [(40, RUST), (20, GREY), (40, TEAL)], 60, 6, 18))
    b.append(box(M - 40, 290, 80, 34, OLIVE, 8) + t(M, 313, "Präsident", 16, "b", "middle", WHITE))
    b.append(t(L + 10, 330, "links:", 20, "b", fill=RUST) + t(L + 10, 354, "Revolutionäre", 18))
    b.append(t(R - 10, 330, "rechts:", 20, "b", "end", TEAL) + t(R - 10, 354, "Königstreue", 18, "", "end"))
    b.append(f"<line x1='{L + 10}' y1='420' x2='{R - 10}' y2='420' stroke='{INK}' stroke-width='4'/>")
    b.append(arrow(M, 420, L + 12, 420, RUST, 4, 14) + arrow(M, 420, R - 12, 420, TEAL, 4, 14))
    b.append(zeilen(L + 10, 450, ["egalitär", "progressiv", "internationalistisch"], 18, "", "start", RUST))
    b.append(zeilen(R - 10, 450, ["elitär", "konservativ", "nationalistisch"], 18, "", "end", TEAL))
    b.append(box(M - 70, 385, 140, 26, "#E8DDBB", 8) + t(M, 404, "liberal: Freiheit", 16, "b", "middle"))
    b.append(t(L, 545, "nach Buch S. 32 – Begriffe, keine Parteien", 16, "m"))
    save("sitzordnung.svg", svg(W, H, "".join(b), "Sitzordnung 1789: links Revolutionäre, rechts Königstreue; darunter die Linie mit egalitär, progressiv, internationalistisch links und elitär, konservativ, nationalistisch rechts; liberal darüber"))


def nationalrat():
    H = 560
    b = [t(L, 42, "Nationalrat: 183 Sitze", 28, "b"), t(L, 70, "Klubs, Herbst 2026 (nach Größe, nicht Sitzordnung)", 17, "m")]
    teile = [(41, PF["SPÖ"]), (16, PF["Grüne"]), (17, PF["NEOS"]), (1, PF["ohne"]), (51, PF["ÖVP"]), (57, PF["FPÖ"])]
    b.append(halbkreis_sitze(M, 300, teile, 70, 8, 18))
    b.append(t(M, 290, "183", 34, "b", "middle") + t(M, 312, "Mehrheit ab 92", 16, "m", "middle"))
    leg = [("FPÖ", 57), ("ÖVP", 51), ("SPÖ", 41), ("NEOS", 17), ("Grüne", 16), ("ohne", 1)]
    for k, (p, n) in enumerate(leg):
        x = L + (k % 3) * 135; y = 350 + (k // 3) * 40
        b.append(f"<circle cx='{x + 10}' cy='{y}' r='9' fill='{PF[p]}'/>" + t(x + 26, y + 7, ("ohne Klub" if p == "ohne" else p) + " " + str(n), 19, "b"))
    b.append(box(L, 440, R - L, 70, WHITE, 12, OLIVE) + t(M, 468, "Regierung: ÖVP + SPÖ + NEOS", 20, "b", "middle")
             + t(M, 494, "51 + 41 + 17 = 109 Sitze (Wahl 2024: 110)", 18, "", "middle"))
    b.append(t(L, 540, "Quelle: Parlament, Stand 29.10.2026 (NEOS 17)", 15, "m"))
    save("nationalrat.svg", svg(W, H, "".join(b), "Halbkreis mit 183 Sitzen: FPÖ 57, ÖVP 51, SPÖ 41, NEOS 17, Grüne 16, einer ohne Klub; Regierung ÖVP, SPÖ und NEOS mit 109 Sitzen"))


def partei():
    H = 560
    b = [t(L, 42, "Was Parteien tun", 28, "b"), t(L, 70, "und woher ihr Geld kommt – Buch S. 31", 18, "m")]
    AUF = ["Macht im Staat übernehmen", "Programm umsetzen", "Leute für Ämter heranbilden", "für Politik begeistern"]
    GELD = ["Mitgliedsbeiträge", "Förderung vom Staat", "Klubförderung (ab 5)", "Spenden", "Abgeordnete zahlen mit"]
    b.append(box(L, 90, 195, 280, WHITE, 12, OLIVE) + t(L + 97, 120, "Aufgaben", 21, "b", "middle"))
    for k, a in enumerate(AUF):
        y = 150 + k * 56
        b.append(f"<circle cx='{L + 22}' cy='{y}' r='13' fill='{OLIVE}'/>" + t(L + 22, y + 6, str(k + 1), 16, "b", "middle", WHITE))
        words = a.split(" "); half = (len(words) + 1) // 2
        b.append(zeilen(L + 42, y - 4, [" ".join(words[:half]), " ".join(words[half:])], 16, "", "start"))
    b.append(box(L + 205, 90, 195, 280, WHITE, 12, ORANGE) + t(L + 302, 120, "Geld", 21, "b", "middle"))
    for k, g in enumerate(GELD):
        y = 152 + k * 44
        b.append(f"<circle cx='{L + 226}' cy='{y - 6}' r='10' fill='{ORANGE}'/>" + t(L + 226, y - 1, "€", 14, "b", "middle", WHITE) + t(L + 243, y, g, 16))
    b.append(box(L, 390, R - L, 120, "#EEF1E6", 12) + zeilen(M, 422, ["Gründen: Satzung beim Innenministerium", "Im Nationalrat: ab 5 Abgeordneten ein Klub", "Staatsgeld soll unabhängig von Spendern machen"], 18, "", "middle"))
    save("partei.svg", svg(W, H, "".join(b), "Vier Aufgaben einer Partei und fünf Geldquellen; Gründung mit Satzung beim Innenministerium; Klub ab 5 Abgeordneten"))


def quellencheck():
    H = 560
    b = [t(L, 42, "Faktencheck: 4 Fragen", 28, "b"), t(L, 70, "an jede Aussage über Parteien", 18, "m")]
    FR = [("1", "Wer sagt das?", "Partei, Medium, Behörde, KI?"), ("2", "Woher weiß er das?", "Protokoll, Abstimmung – oder Meinung?"),
          ("3", "Was hat er davon?", "Stimmen, Klicks, Geld?"), ("4", "Was sagen andere?", "zweite, unabhängige Quelle")]
    for k, (n, f, u) in enumerate(FR):
        y = 90 + k * 82
        b.append(box(L, y, R - L, 72, WHITE, 12, TEAL) + f"<circle cx='{L + 32}' cy='{y + 36}' r='20' fill='{TEAL}'/>" + t(L + 32, y + 44, n, 22, "b", "middle", WHITE)
                 + t(L + 64, y + 32, f, 21, "b") + t(L + 64, y + 58, u, 17, "m"))
    for k, (c, w) in enumerate([("#4E7D23", "glaubwürdig"), ("#C98A12", "vorsichtig"), ("#8C3B2E", "weglassen")]):
        x = L + k * 142
        b.append(f"<circle cx='{x + 14}' cy='{438}' r='16' fill='{c}'/>" + t(x + 36, 444, w, 17, "b"))
    b.append(box(L, 475, R - L, 64, "#EEF1E6", 12) + zeilen(M, 500, ["Umfrage ≠ Wahl · Ja/Nein-Tabelle ≠ Abstimmung", "KI und Schulbuch können sich irren"], 17, "", "middle"))
    save("quellencheck.svg", svg(W, H, "".join(b), "Vier Prüffragen: Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere? Dazu eine Ampel grün, gelb, rot"))


def ueberblick():
    H = 560
    b = [t(L, 42, "Wahlrecht und Parteien", 28, "b"), t(L, 70, "die Einheit auf einen Blick", 18, "m")]
    b.append(box(L, 88, R - L, 140, WHITE, 12, OLIVE) + t(L + 14, 116, "1 Wahlrecht", 21, "b", fill=OLIVE))
    for k, (j, w) in enumerate([("1861", "Besitz"), ("1873", "Steuer"), ("1907", "Männer"), ("1918", "Frauen"), ("2007", "ab 16")]):
        x = L + 40 + k * 82
        b.append(f"<circle cx='{x}' cy='160' r='9' fill='{OLIVE}'/>" + t(x, 192, j, 17, "b", "middle") + t(x, 214, w, 16, "", "middle"))
    b.append(f"<line x1='{L + 40}' y1='160' x2='{L + 368}' y2='160' stroke='{OLIVE}' stroke-width='3'/>")
    b.append(box(L, 242, R - L, 150, WHITE, 12, TEAL) + t(L + 14, 270, "2 Lager → Parteien", 21, "b", fill=TEAL))
    for k, (a, p) in enumerate([("christlichsozial", "ÖVP"), ("sozialdemokratisch", "SPÖ"), ("deutschnational", "FPÖ")]):
        y = 300 + k * 28
        b.append(t(L + 14, y, a, 17) + arrow(L + 190, y - 6, L + 250, y - 6, INK, 3, 10) + t(L + 262, y, p, 18, "b", fill=PF[p]))
    b.append(t(L + 14, 384, "neu: Grüne (1986), NEOS (2012)", 17, "m"))
    b.append(box(L, 406, R - L, 140, WHITE, 12, RUST) + t(L + 14, 434, "3 Richtungen", 21, "b", fill=RUST))
    b.append(f"<line x1='{L + 30}' y1='490' x2='{R - 30}' y2='490' stroke='{INK}' stroke-width='3'/>")
    b.append(t(L + 30, 520, "links: egalitär", 17, "", "start") + t(R - 30, 520, "rechts: konservativ", 17, "", "end"))
    b.append(box(M - 75, 452, 150, 26, "#E8DDBB", 8) + t(M, 471, "liberal: Freiheit", 16, "b", "middle"))
    save("ueberblick.svg", svg(W, H, "".join(b), "Überblick: Wahlrecht 1861 bis 2007, drei Lager mit ihren Parteien, Richtungen links, rechts und liberal"))


TEILE = {"wahlrecht.svg": wahlrecht, "lager.svg": lager, "sitzordnung.svg": sitzordnung, "nationalrat.svg": nationalrat,
         "partei.svg": partei, "quellencheck.svg": quellencheck, "ueberblick.svg": ueberblick}
if __name__ == "__main__":
    for n, f in TEILE.items():
        f()
    print("geschrieben:", ", ".join(TEILE))
