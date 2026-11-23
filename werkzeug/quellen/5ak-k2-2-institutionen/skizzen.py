"""Grafiken IWK 5AK · K2.2 Institutionen – alles selbst gezeichnet als SVG (keine Buchabbildungen).
Vorgänge sind animiert (SMIL, Standard 16.11.2026): streit.svg (Handelsstreit), kredit.svg (IWF-Kredit in Tranchen).
Alle Spuren eines Bildes: gleiche Dauer D, Beginn 0 s, Schleife. Ohne Animation zeigt das Grundbild den Endzustand.
Zustände bleiben ruhig: ueberblick.svg, stimme.svg (Werte zum Ablesen).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ak-k2-2-institutionen/skizzen.py  →  5ak-iwk/k2-2-institutionen/img/*.svg"""
import os, sys
from xml.sax.saxutils import escape as x
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inhalt as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
IMG = os.path.join(ROOT, I.ORDNER, "img") + "/"
os.makedirs(IMG, exist_ok=True)

BG, INK, MUTED, LINE = "#F2F3EE", "#1F2A1C", "#5E6652", "#D3DCC2"
OLIVE, GREEN, ORANGE, TEAL, RUST, WHITE = "#3B4A2F", "#7FA83A", "#D9772B", "#2E7D8C", "#A33A2B", "#FFFFFF"
FONT = "'Source Sans 3', Carlito, 'Segoe UI', Arial, sans-serif"
D = 12.0   # Dauer jeder Animation in Sekunden


def svg(w, h, body, title):
    st = (f"<style>text{{font-family:{FONT};fill:{INK}}} .b{{font-weight:700}} .w{{fill:#fff}} .m{{fill:{MUTED}}}</style>")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{x(title)}">'
            f"<title>{x(title)}</title>{st}<rect width='{w}' height='{h}' rx='18' fill='{BG}'/>{body}</svg>")


def t(xx, y, s, size=20, cls="", anchor="middle", fill=None):
    f = f' style="fill:{fill}"' if fill else ""
    return f'<text x="{xx}" y="{y}" font-size="{size}" text-anchor="{anchor}" class="{cls}"{f}>{x(s)}</text>'


def box(xx, y, w, h, fill, stroke=None, rx=14, dash=False):
    s = f' stroke="{stroke}" stroke-width="3"' if stroke else ""
    d = ' stroke-dasharray="9 7"' if dash else ""
    return f'<rect x="{xx}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}/>'


def pfeil(x0, y0, x1, y1, col=INK, w=5):
    import math
    a = math.atan2(y1 - y0, x1 - x0); hd = 14
    p = [(x1, y1), (x1 - hd * math.cos(a - .45), y1 - hd * math.sin(a - .45)), (x1 - hd * math.cos(a + .45), y1 - hd * math.sin(a + .45))]
    return (f'<line x1="{x0}" y1="{y0}" x2="{x1 - 8 * math.cos(a):.1f}" y2="{y1 - 8 * math.sin(a):.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in p)}" fill="{col}"/>')


def blende(inhalt, ab, bis=D - 0.6):
    """Element ab Sekunde »ab« einblenden, bis »bis« stehen lassen, dann kurz ausblenden (Schleife). Grundbild = sichtbar (Endzustand)."""
    k = lambda s: f"{min(max(s / D, 0), 1):.4f}"
    vals = "0;0;1;1;0;0"
    kt = f"0;{k(ab)};{k(ab + 0.5)};{k(bis)};{k(bis + 0.4)};1"
    return f'<g>{inhalt}<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/></g>'


def bewege(inhalt, von, nach, ab, dauer=1.2, bis=D - 0.6):
    """Element von Punkt »von« nach »nach« bewegen (Grundbild steht am Ziel) und dabei einblenden."""
    k = lambda s: f"{min(max(s / D, 0), 1):.4f}"
    dx0, dy0 = von[0] - nach[0], von[1] - nach[1]
    mv = (f'<animateTransform attributeName="transform" type="translate" values="{dx0} {dy0};{dx0} {dy0};0 0;0 0" '
          f'keyTimes="0;{k(ab)};{k(ab + dauer)};1" dur="{D}s" repeatCount="indefinite"/>')
    return blende(f"<g>{inhalt}{mv}</g>", ab, bis)


def schritte(liste, y0, w):
    """Kurze Überschrift je Schritt, nacheinander eingeblendet, an derselben Stelle (Schrift 20 px)."""
    out = []
    for i, (ab, txt) in enumerate(liste):
        bis = liste[i + 1][0] - 0.2 if i + 1 < len(liste) else D - 0.6
        k = lambda s: f"{min(max(s / D, 0), 1):.4f}"
        last = i + 1 == len(liste)
        vals, kt = ("0;0;1;1;0;0", f"0;{k(ab)};{k(ab + .4)};{k(bis)};{k(bis + .3)};1")
        op = "1" if last else "0"   # Grundbild: nur der letzte Schritt sichtbar
        out.append(f'<g opacity="{op}">{box(16, y0 - 30, w - 32, 44, OLIVE, rx=10)}{t(w / 2, y0, txt, 20, "b w")}'
                   f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/></g>')
    return "".join(out)


def save(name, s):
    open(IMG + name, "w", encoding="utf-8").write(s)
    print("img/" + name, len(s) // 1024 + 1, "KB")


# ---------------------------------------------------------------- 1 Überblick (ruhig)
def ueberblick():
    W, H = 900, 470
    cols = [("WTO", "Welthandelsorganisation", "Genf · 166 Mitglieder", TEAL, ["Regeln für den Handel", "Zölle, Dienstleistungen,", "Patente", "Streit schlichten"], "HANDEL"),
            ("Weltbank", "Weltbankgruppe", "Washington · 189 Mitglieder", OLIVE, ["langfristige Kredite", "für Straßen, Schulen,", "Kraftwerke, Wiederaufbau", "zinslos für die Ärmsten (IDA)"], "PROJEKTE"),
            ("IWF", "Internationaler Währungsfonds", "Washington · 191 Mitglieder", ORANGE, ["kurzfristige Kredite", "für Staaten in einer", "Zahlungskrise", "meist mit Auflagen"], "ZAHLUNGSKRISE")]
    b = [t(W / 2, 40, "Drei Institutionen – drei Aufgaben", 26, "b")]
    for i, (k, lang, ort, col, zeilen, wort) in enumerate(cols):
        x0 = 30 + i * 285
        b.append(box(x0, 64, 270, 380, WHITE, col))
        b.append(box(x0, 64, 270, 92, col))
        b.append(t(x0 + 135, 104, k, 32, "b w"))
        b.append(t(x0 + 135, 136, lang, 17, "w"))
        b.append(t(x0 + 135, 184, ort, 18, "b", fill=col))
        for j, z in enumerate(zeilen):
            b.append(t(x0 + 135, 228 + j * 30, z, 20))
        b.append(box(x0 + 35, 376, 200, 46, col, rx=23))
        b.append(t(x0 + 135, 407, wort, 20, "b w"))
    save("ueberblick.svg", svg(W, H, "".join(b), "Drei Säulen: WTO in Genf mit 166 Mitgliedern für Regeln im Handel; Weltbank in Washington mit 189 Mitgliedern für langfristige Projektkredite; IWF in Washington mit 191 Mitgliedern für kurzfristige Kredite bei Zahlungskrisen, meist mit Auflagen."))


# ---------------------------------------------------------------- 2 Wer hat das Sagen? (ruhig, zum Ablesen)
def stimme():
    W, H = 900, 470
    b = [t(W / 2, 40, "Wer hat das Sagen?", 26, "b")]
    # links: WTO
    b.append(box(24, 62, 400, 384, WHITE, TEAL))
    b.append(t(224, 100, "WTO: ein Land, eine Stimme", 22, "b", fill=TEAL))
    for i, land in enumerate(["USA", "China", "Österreich", "Malawi"]):
        cx = 84 + i * 93
        b.append(f'<circle cx="{cx}" cy="190" r="36" fill="{TEAL}"/>')
        b.append(t(cx, 199, "1", 28, "b w"))
        b.append(t(cx, 256, land, 18))
    b.append(t(224, 320, "Entschieden wird im Konsens.", 20))
    b.append(t(224, 350, "Ein einziges Land kann blockieren.", 20, "b", fill=RUST))
    # rechts: IWF
    b.append(box(446, 62, 430, 384, WHITE, ORANGE))
    b.append(t(661, 100, "IWF: Stimmen nach Kapitalanteil", 22, "b", fill=ORANGE))
    werte = [("USA", 16.49), ("Japan", 6.14), ("China", 6.01), ("Deutschland", 5.31), ("Österreich", 0.81)]
    for i, (land, v) in enumerate(werte):
        y = 138 + i * 52
        b.append(t(580, y + 24, land, 19, anchor="end"))
        b.append(box(592, y + 4, max(4, v * 15), 30, ORANGE if land != "Österreich" else RUST, rx=6))
        b.append(t(600 + v * 15, y + 26, f"{v:.1f} %".replace(".", ","), 19, "b", anchor="start"))
    b.append(t(661, 416, "Stimmanteile in %, gerundet nach Buch S. 62", 16, "m"))
    save("stimme.svg", svg(W, H, "".join(b), "Links: In der WTO hat jedes Land eine Stimme, auch Österreich und Malawi so viel wie die USA; entschieden wird im Konsens, ein Land kann blockieren. Rechts: Stimmanteile im IWF: USA 16,5 Prozent, Japan 6,1, China 6,0, Deutschland 5,3, Österreich 0,8."))


# ---------------------------------------------------------------- 3 Handelsstreit (animiert)
def streit():
    W, H = 440, 640
    b = []
    b.append(t(W / 2, 40, "So läuft ein Handelsstreit", 24, "b"))
    # Länder
    b.append(box(24, 70, 160, 70, WHITE, OLIVE)); b.append(t(104, 113, "Land A", 22, "b"))
    b.append(box(256, 70, 160, 70, WHITE, OLIVE)); b.append(t(336, 113, "Land B", 22, "b"))
    # Schritt 1: Zoll A -> B
    b.append(blende(pfeil(186, 105, 252, 105, RUST) + t(220, 92, "Zoll", 18, "b", fill=RUST), 0.3))
    # Schritt 2: B klagt -> Schiedsgremium
    b.append(blende(pfeil(336, 144, 300, 210, TEAL) + box(110, 214, 220, 80, TEAL) + t(220, 248, "Schiedsgremium", 21, "b w") + t(220, 276, "der WTO", 18, "w"), 3.0))
    b.append(blende(t(220, 326, "Urteil: Land B hat recht.", 20, "b", fill=TEAL), 4.3))
    # Schritt 3: A geht in Berufung -> leere Berufungsinstanz
    b.append(blende(pfeil(104, 144, 120, 380, OLIVE) + box(80, 384, 280, 92, WHITE, RUST, dash=True) + t(220, 420, "Berufungsinstanz", 21, "b", fill=RUST)
                    + t(220, 452, "0 Richter seit Ende 2019", 19, fill=RUST), 6.0))
    # Schritt 4: hängen geblieben
    b.append(blende(f'<line x1="300" y1="396" x2="346" y2="464" stroke="{RUST}" stroke-width="7" stroke-linecap="round"/>'
                    f'<line x1="346" y1="396" x2="300" y2="464" stroke="{RUST}" stroke-width="7" stroke-linecap="round"/>'
                    + t(220, 510, "Das Urteil wird nicht verbindlich.", 20, "b", fill=RUST), 9.0))
    b.append(schritte([(0.3, "1 Land A erhebt Zölle, B klagt"), (3.0, "2 Die WTO-Schiedsstelle urteilt"),
                       (6.0, "3 Land A geht in Berufung …"), (9.0, "4 … und dort sitzt niemand")], 596, W))
    save("streit.svg", svg(W, H, "".join(b), "Animation: Land A erhebt Zölle gegen Land B. Land B klagt bei der WTO, ein Schiedsgremium gibt B recht. Land A geht in Berufung, doch die Berufungsinstanz hat seit Ende 2019 keine Richter. Das Urteil wird nicht verbindlich."))


# ---------------------------------------------------------------- 4 IWF-Kredit (animiert)
def kredit():
    W, H = 440, 640
    b = [t(W / 2, 40, "So läuft ein IWF-Kredit", 24, "b")]
    b.append(box(24, 70, 170, 96, WHITE, OLIVE)); b.append(t(109, 108, "Staat", 24, "b")); b.append(t(109, 140, "Kasse leer", 19, fill=RUST))
    b.append(box(246, 70, 170, 96, ORANGE)); b.append(t(331, 112, "IWF", 28, "b w")); b.append(t(331, 144, "Washington", 18, "w"))
    b.append(blende(pfeil(196, 104, 242, 104, OLIVE) + t(219, 92, "Hilfe?", 16, "b"), 0.3))
    # Schritt 2: Auflagen
    aufl = (box(40, 196, 360, 150, WHITE, ORANGE) + t(220, 228, "Auflagen, z. B. Ukraine 2026:", 20, "b", fill=ORANGE)
            + t(220, 262, "mehr Steuern eintreiben", 20) + t(220, 292, "Korruption bekämpfen", 20) + t(220, 322, "Wechselkurs flexibler", 20))
    b.append(blende(aufl, 2.8))
    # Schritt 3: erste Tranche fließt
    muenze = (f'<circle cx="0" cy="0" r="34" fill="{GREEN}" stroke="{OLIVE}" stroke-width="3"/>' + t(0, -2, "1,5", 20, "b w") + t(0, 18, "Mrd. $", 13, "w"))
    b.append(bewege(f'<g transform="translate(110 420)">{muenze}</g>', (330, 420), (110, 420), 5.6))
    b.append(blende(t(300, 427, "1. Tranche", 20, "b", fill=GREEN), 5.6))
    # Schritt 4: Prüfung, dann nächste Tranche
    b.append(blende(box(40, 476, 360, 56, WHITE, GREEN) + t(220, 512, "Prüfung bestanden → nächste Tranche", 19, "b", fill=OLIVE), 8.6))
    b.append(schritte([(0.3, "1 Ein Staat steckt in der Krise"), (2.8, "2 Der IWF stellt Bedingungen"),
                       (5.6, "3 Das Geld kommt in Stücken"), (8.6, "4 Erst prüfen, dann weiter")], 596, W))
    save("kredit.svg", svg(W, H, "".join(b), "Animation: Ein Staat mit leerer Kasse bittet den IWF um Hilfe. Der IWF stellt Auflagen, zum Beispiel bei der Ukraine 2026: mehr Steuern eintreiben, Korruption bekämpfen, Wechselkurs flexibler. Die erste Tranche von 1,5 Milliarden Dollar fließt. Nach bestandener Prüfung kommt die nächste Tranche."))


ueberblick(); stimme(); streit(); kredit()
