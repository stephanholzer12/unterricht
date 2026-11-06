"""Unterrichts-PPP K1.8 Fairer Handel (TH-Unterricht, 2 Stunden: Stunde 1 = Testtag, Stunde 2 = eine Woche später) – die kurze, geführte PPP für den Frontalunterricht im Saal.
Stephans Auftrag (29.10.2026): gekürzte TH-Lehrer, in der GENAU steht, was die Kadetten in welcher Reihenfolge tun; Theorie nur dort
wiederholt, wo es Schwierigkeiten oder falsche Vorstellungen gibt; die wichtigsten Aufgaben werden gemeinsam durchgegangen.
Aufbau nach »bhak-ppp-gestaltung« Abschnitt 10–14 (Muster Wellen v6 bzw. 1AB K1.4): ausgeblendete Lehrer-Info »So führt die PPP …«,
ausgeblendete Regie je Klasse (Minute · Was läuft jetzt? · Folie · Wozu?), »Heute« → Einstieg → »Lesen: …« → »KURZ KLÄREN« → Arbeitsauftrag → Besprechen;
unten links ein Phasenhinweis (JETZT … · Minuten / Danach: …). Beide Klassen haben denselben Ablauf (5BK Di 10.11./Di 17.11., 5AK Do 12.11./Do 19.11.).
Alle Minuten kommen aus plan.py (eine Quelle mit Fahrplan, Stundenkarte und Lösungsmappe).
Aufruf im Repository-Ordner: python3 werkzeug/quellen/5ab-k1-8-fairer-handel/unterricht_ppp.py <BHAK_Folienmaster_Vorlage.pptx> <Zielordner>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bauen_ppp as B
import inhalt as I, plan as P, theorie_daten as TD, fachwissen as F
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree

ZIEL = sys.argv[2]
OLIVE, INK, TEAL, RUST, MUTED, WHITE, GREEN, ORANGE, CARD, RED = B.OLIVE, B.INK, B.TEAL, B.RUST, B.MUTED, B.WHITE, B.GREEN, B.ORANGE, B.CARD, B.RED
X0, W = 0.5, 9.0
YC = 4.52                         # Inhalt endet hier; darunter der Phasenhinweis (4.6–5.0), dann die Master-Fußzeile
UNIT = B.UNIT
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

FARBE = {"LESEN": TEAL, "KURZ KLÄREN": OLIVE, "AUFGABE": GREEN, "VERSUCH": RED, "BESPRECHEN": ORANGE, "BAUEN": GREEN,
         "START": MUTED, "TEST": MUTED, "ABGABE": RUST, "WEG": MUTED, "EINSTIEG": ORANGE, "WIEDERHOLEN": TEAL, "ZU ZWEIT": GREEN}
TITEL = {it["id"]: it["title"] for p in TD.PARTS for it in p[3] if isinstance(it, dict)}
TITEL.update({it["id"]: it["title"] for it in TD.EINSTIEG})
T = {t["nr"]: t for t in I.T}


# ================================================================ Bausteine
STD = 1   # aktuelle Stunde beim Bauen


def phasen(k=None, std=None):
    return P.PLAN[k or I.KLASSEN[0]][(std or STD) - 1]["phasen"]


def minuten(idx):
    m = sum(phasen()[i][1] for i in idx)
    assert all(sum(phasen(k)[i][1] for i in idx) == m for k in I.KLASSEN)
    return f"{m} min"


def hinweis(s, art, mins, danach):
    """Phasenhinweis unten links: was JETZT läuft und was danach kommt."""
    col = FARBE.get(art, OLIVE)
    lab = ("JETZT " + art if art not in ("START", "ABGABE", "TEST", "WEG") else art) + (" · " + mins if mins else "")
    w1 = max(2.2, min(4.6, B.FONT_B.getlength(lab) / 100 * 14 / 72 + 0.45))
    c = B.box(s, X0, 4.62, w1, 0.38, fill=col)
    B.text(c, [lab], size=14, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE, after=0)
    if danach:
        B.tb(s, X0 + w1 + 0.1, 4.62, W - w1 - 0.1, 0.38, [[("Danach: ", {"bold": True, "color": col}), (danach, {})]], size=14, anchor=MSO_ANCHOR.MIDDLE, after=0)


def karte(s, x, y, w, h, kopf, zeilen, akzent=GREEN, size=20):
    c = B.box(s, x, y, w, h, fill=CARD)
    band = s.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(0.08))
    band.fill.solid(); band.fill.fore_color.rgb = akzent; band.line.fill.background(); band.shadow.inherit = False
    c.text_frame.margin_top = Inches(0.14)
    B.text(c, [[(kopf, {"bold": True, "color": OLIVE})]] + list(zeilen), size=size, after=2)
    return c


def merke(s, y, txt, size=20, h=None):
    h = h or B.th(txt, size, W - 0.1, bold=True, pad=0.24)
    c = B.box(s, X0, y, W, h, fill=OLIVE)
    B.text(c, [txt], size=size, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return c, h


def frage_klick(s, y, frage, antwort, w=W, x=X0, size=20):
    """Frage fett, darunter Antwortkasten; die Antwort erscheint per Klick (Lehrer). Gibt neue y zurück."""
    hq = B.th(frage, size, w, True, pad=0.06)
    B.tb(s, x, y, w, hq, [frage], size=size, bold=True, after=0)
    ha = B.th(antwort, size, w - 0.2, pad=0.16)
    fr = B.box(s, x, y + hq, w, ha, fill=RGBColor.from_string("FFFFFF"), line=ORANGE, lw=1.5)
    a = B.tb(s, x + 0.08, y + hq + 0.02, w - 0.16, ha - 0.04, [antwort], size=size, color=RED, anchor=MSO_ANCHOR.MIDDLE, after=0)
    s._anim.append([a])
    return y + hq + ha + 0.1


def qr(s, key, x, y, size, label):
    s.shapes.add_picture(B.qr_png(B.URL[key]), Inches(x), Inches(y), Inches(size), Inches(size))
    B.tb(s, x - 0.3, y + size, size + 0.6, 0.3, [label], size=14, bold=True, color=OLIVE, align=PP_ALIGN.CENTER, after=0)


def schritte(s, x, y, w, items, size=20, farbe=TEAL):
    for i, it in enumerate(items):
        h = B.th(it, size, w - 0.6, pad=0.06)
        c = B.box(s, x, y + 0.04, 0.42, 0.42, fill=farbe)
        B.text(c, [str(i + 1)], size=16, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
        B.tb(s, x + 0.55, y, w - 0.55, h, [it], size=size, after=0); y += max(0.5, h + 0.06)
    return y


PROBLEME = []


def titel_von(s):
    return next((ph.text_frame.text for ph in s.placeholders if ph.placeholder_format.type == 1), "?")


def check(s):
    """Kontrolle: nichts unter die Inhaltsgrenze (außer Phasenhinweis, Fußzeile, Pill)."""
    for sh in s.shapes:
        if sh.is_placeholder or sh.name == "Buchseite": continue
        unten = (sh.top + sh.height) / 914400
        if unten > YC + 0.02 and sh.top / 914400 < 4.6:
            PROBLEME.append(f"»{titel_von(s)}«: {sh.name} {sh.text_frame.text[:40] if sh.has_text_frame else ''!r} bis {unten:.2f} in")


# ================================================================ Folien je Teil
# Jede Folie: (Schlüssel, Phasen-Indizes in plan.py, Art für den Hinweis, Schritt für die »Heute«-Folie oder None, Wozu? für die Regie, Zeichenfunktion)
SPEC = {}
FOLIE = {}            # Schlüssel → Folie
NACH = {}             # Schlüssel → Text »Danach: …«


def lesen_folie(teil, buch, abschnitte, leitfrage, idx):
    titel = f"Lesen: Theorieteil · Teil {teil}"
    s = d.slide("Nur Titel", titel)
    y = 1.05
    if buch:
        bh = max(0.62, B.th(buch, 20, W - 0.95, pad=0.2))
        c = B.box(s, X0, y, W, bh, fill=CARD, line=OLIVE, lw=1.5)
        ic = B.box(s, X0 + 0.1, y + bh / 2 - 0.27, 0.62, 0.54, fill=OLIVE)
        B.text(ic, [[("BUCH", {"size": 12, "bold": True, "color": WHITE})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
        B.tb(s, X0 + 0.82, y, W - 0.9, bh, [buch], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0); y += bh + 0.12
    B.tb(s, X0, y, 6.9, 0.36, [[("Im Theorieteil genau diese Abschnitte:", {"bold": True, "color": TEAL})]], size=18, after=0); y += 0.4
    for a in abschnitte:
        c = B.box(s, X0, y, 6.9, 0.44, fill=RGBColor.from_string("E8F1F3"), line=TEAL, lw=1.25)
        hh = max(0.44, B.th("»" + TITEL[a] + "«", 20, 6.4, True, pad=0.16))
        c.height = Inches(hh)
        B.text(c, [[("»" + TITEL[a] + "«", {"bold": True})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0); y += hh + 0.06
    qr(s, "theorie", 7.75, 1.05 + (bh + 0.12 if buch else 0), 1.2, "Theorieteil")
    y += 0.08
    hq = B.th("Leitfrage: " + leitfrage, 20, W - 0.1, pad=0.2)
    c = B.box(s, X0, y, W, hq, fill=RGBColor.from_string("FFF4EA"), line=ORANGE, lw=1.5)
    B.text(c, [[("Leitfrage: ", {"bold": True, "color": ORANGE}), (leitfrage, {})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return s


def auftrag_folie(titel, nrs, tun, erwartet, ohne_handy=False, layout="Aufgabe"):
    """Arbeitsphase: welche Aufgaben, was genau tun, wie lange, was am Ende dastehen soll."""
    s = d.slide(layout, titel)
    rows = [["Nr.", "Aufgabe", "Zeit", "So arbeitest du"]]
    for n in nrs:
        rows.append([str(n), T[n]["title"], f"{T[n]['zeit']} min", tun.get(n, "allein am Handy")])
    cells, h = B.auto_grid(s, X0, 1.05, [0.6, 4.0, 0.9, 3.5], rows, size=18, minh=0.42)
    y = 1.05 + h + 0.12
    if ohne_handy:
        c = B.box(s, X0, y, W, 0.45, fill=RGBColor.from_string("F6E3DF"), line=RUST)
        B.text(c, [[("Handy bleibt zuerst weg: ", {"bold": True, "color": RUST}), (ohne_handy, {})]], size=18, anchor=MSO_ANCHOR.MIDDLE, after=0); y += 0.55
    if erwartet:
        he = B.th("Am Ende steht da: " + erwartet, 20, W - 0.2, pad=0.18)
        c = B.box(s, X0, y, W, he, fill=RGBColor.from_string("FFFFFF"), line=GREEN, lw=1.5)
        B.text(c, [[("Am Ende steht da: ", {"bold": True, "color": GREEN}), (erwartet, {})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return s


# ---------------------------------------------------------------- Inhalte (kurz, nur das Wichtigste)
def test_folie():
    s = d.slide("Nur Titel", "Test")
    c = B.box(s, X0, 1.2, W, 1.3, fill=OLIVE)
    B.text(c, ["Tisch frei, Handy weg, Stift bereit.", "Danach geht es kurz mit einem neuen Thema weiter."], size=24, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=4)
    B.tb(s, X0, 2.8, W, 0.8, ["Fairer Handel ist heute und nächste Woche Thema – er gehört nicht zum Teststoff."], size=20, color=MUTED, align=PP_ALIGN.CENTER, after=0)
    return s


def _heute(titel, items, qr_a=True):
    s = d.slide("Nur Titel", titel)
    B.tb(s, X0, 0.98, W, 0.32, [[(I.wann(STD) + " · " + I.BUCH, {"bold": True, "color": TEAL})]], size=16, after=0)
    c = B.box(s, X0, 1.36, 7.0, B.th("Ziel: " + I.LEITFRAGE, 20, 6.9, pad=0.16), fill=OLIVE)
    B.text(c, [[("Ziel: ", {"bold": True}), (I.LEITFRAGE, {})]], size=20, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, after=0)
    y = 1.36 + c.height / 914400 + 0.12
    h1 = (len(items) + 1) // 2
    for col, part in enumerate((items[:h1], items[h1:])):
        yy = y
        for i, it in enumerate(part):
            n = i + 1 + col * h1
            cc = B.box(s, X0 + col * 3.6, yy + 0.04, 0.4, 0.4, fill=GREEN)
            B.text(cc, [str(n)], size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
            hh = B.th(it, 18, 3.1, pad=0.04)
            B.tb(s, X0 + col * 3.6 + 0.48, yy, 3.1, hh, [it], size=18, after=0); yy += max(0.5, hh + 0.04)
    qr(s, "theorie", 7.75, 1.36, 1.05, "Theorieteil")
    qr(s, "aufgaben", 7.75, 2.85, 1.05, "Arbeitsblatt")
    return s


def heute1():
    ph = phasen()
    return _heute("Heute: Fairer Handel – Teil 1", [f"Schätzen und reden · {ph[3][1]} min", f"Lesen Teil 1 · {ph[4][1]} min", f"Kurz klären · {ph[5][1]} min",
                                                   f"Aufgabe 1 zu zweit · {ph[6][1]} min", f"Besprechen · {ph[7][1]} min"])


def heute2():
    ph = phasen()
    return _heute("Heute: Fairer Handel – Teil 2", [f"Rückblick · {ph[1][1]} min", f"Lesen Teil 2 · {ph[2][1]} min", f"Mindestpreis klären · {ph[3][1]} min", f"Aufgabe 2 zu zweit · {ph[4][1]} min",
                                                   f"Besprechen · {ph[5][1]} min", f"Zahlen prüfen · {ph[6][1]} min", f"Aufgabe 3 Gruppe · {ph[7][1]} min", f"PDF in LMS · {ph[8][1]} min"])


def einst1():
    s = d.slide("Nur Titel", "Gemeinsam: Was kostet deine Schokolade wirklich?")
    karte(s, X0, 1.0, 4.4, 1.5, "Handzeichen", ["Wer isst oder trinkt pro Woche Schokolade, Kakao, Kaffee oder Riegel?"], ORANGE, size=18)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.5, "Schätzfrage", ["Wie viel vom Ladenpreis einer Tafel Schokolade kommt beim Kakaobauern an?"], GREEN, size=18)
    for k, (t, x) in enumerate([("1 %", 0.5), ("6 %", 2.8), ("20 %", 5.1), ("50 %", 7.4)]):
        c = B.box(s, x, 2.75, 2.0, 0.8, fill=CARD, line=OLIVE, lw=1.5)
        B.text(c, [t], size=26, bold=True, color=OLIVE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    B.tb(s, X0, 3.75, W, 0.7, ["Wir sammeln die Schätzungen an der Tafel – die Zahl suchen wir nächste Stunde gemeinsam. Wichtig ist die Frage: Woher bekommen wir verlässliche Zahlen?"], size=18, color=MUTED, after=0)
    return s


def klaeren_1():
    s = d.slide("Nur Titel", "Kurz klären: fairer Handel und drei Säulen")
    B.picture(s, UNIT + "img/saeulen.png", X0, 1.0, 5.0, 2.9)
    y = 1.0
    y = frage_klick(s, y, "Ist Fairtrade automatisch Bio?", "Nein – Bio wird gefördert, aber nicht überall verlangt. Fair und Bio sind zwei Siegel.", w=4.1, x=5.5, size=18)
    y = frage_klick(s, y, "Ist »fair« in der Werbung geschützt?", "Nein – darum zählt, wer das Siegel vergibt und kontrolliert.", w=4.1, x=5.5, size=18)
    B.tb(s, X0, 3.95, 5.0, 0.4, ["Eigene Darstellung nach Buch S. 37"], size=14, color=MUTED, after=0)
    return s


def a1_auftrag():
    return auftrag_folie("Jetzt: Aufgabe 1 – zu zweit zuordnen", [1], {1: "zu zweit am Handy, Schulbuch S. 37 aufschlagen"},
                         "6 Beispiele den drei Säulen zugeordnet – danach besprechen wir es gemeinsam")


def a1_loesung():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 1")
    rows = [["Beispiel", "Säule"]] + [[t, z] for _, t, z in I.SELB]
    cells, h = B.auto_grid(s, X0, 1.0, [6.4, 2.6], rows, size=16, minh=0.4)
    for r in cells[1:]:
        s._anim.append([r[1]])
    return s


def reserve1():
    s = d.slide("Nur Titel", "Noch Zeit? Stoppfragen und Quiz")
    y = 1.0
    for q, a in I.STOPPFRAGEN[1]:
        y = frage_klick(s, y, q, a, w=6.6, size=16)
    qr(s, "quiz", 7.8, 1.0, 1.2, "Quiz")
    B.tb(s, X0, y + 0.02, 6.6, 0.5, ["Nächste Stunde: Mindestpreis, Prämie – und wie belastbar die Zahlen sind."], size=16, bold=True, color=OLIVE, after=0)
    return s


def rueck2():
    s = d.slide("Nur Titel", "Rückblick: Teil 1")
    y = 1.0
    for q, a in I.STOPPFRAGEN[1]:
        y = frage_klick(s, y, q, a, w=W, size=18)
    B.tb(s, X0, y + 0.05, W, 0.8, ["Und die Schätzung von letzter Woche: Wie viel vom Ladenpreis kommt beim Bauern an? Wir suchen die Zahl jetzt – und fragen, wie belastbar sie ist."], size=18, color=MUTED, after=0)
    return s


def klaeren_2():
    s = d.slide("Nur Titel", "Kurz klären: Mindestpreis und Prämie")
    B.picture(s, UNIT + "img/preis.png", X0, 1.0, 4.6, 2.86)
    y = 1.0
    y = frage_klick(s, y, "Mindestpreis oder Marktpreis – was gilt, wenn der Markt höher liegt?", "Der Marktpreis. Der Mindestpreis ist nur die Untergrenze.", w=3.9, x=5.7, size=16)
    y = frage_klick(s, y, "Wofür ist die Prämie?", "Zusatzgeld für Gemeinschaftsprojekte, über die die Mitglieder abstimmen.", w=3.9, x=5.7, size=16)
    B.tb(s, X0, 3.9, 5.0, 0.6, ["Eigene Darstellung, Verlauf angenommen. Echte Preise je Tonne: Dez. 2023 über 12.000 · Okt. 2025 ca. 5.900 (ORF.at) · März 2026 ca. 3.100 (APA)."], size=12, color=MUTED, after=0)
    return s


def a2_auftrag():
    return auftrag_folie("Jetzt: Aufgabe 2 – zu zweit rechnen", [2], {2: "zu zweit am Handy, Rechenweg im Heft"},
                         "a) Prämie · b) Erlös zum Mindestpreis · c) Mehrerlös gegenüber dem Weltmarkt · d) was bei 12.000 US-Dollar gilt")


def a2_daten():
    s = d.slide("Aufgabe", "Aufgabe 2: Daten und Rechenweg")
    rows = [list(r) for r in I.DATENTABELLE]
    cells, h = B.auto_grid(s, X0, 1.0, [4.0, 2.6], rows, size=16, minh=0.4)
    B.tb(s, X0, 1.05 + h, 6.6, 0.8, [I.TABNOTE], size=12, color=RUST, bold=True, after=0)
    karte(s, 7.3, 1.0, 2.2, 3.45, "Rechenweg", [[("Prämie", {"bold": True})], "Tonnen × Prämie", [("Erlös", {"bold": True})], "Tonnen × Mindestpreis", [("Mehrerlös", {"bold": True})], "(Mindest- − Weltmarktpreis) × Tonnen"], GREEN, size=14)
    return s


def a2_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 2")
    rows = [["Frage", "Rechnung", "Ergebnis"], ["a) Prämie", "40 × 275", "11.000 US-Dollar"], ["b) Erlös zum Mindestpreis", "40 × 3.500", "140.000 US-Dollar"],
            ["c) Mehrerlös", "(3.500 − 3.100) × 40", "16.000 US-Dollar"], ["d) Weltmarkt bei 12.000", "Marktpreis gilt", "Prämie kommt dazu"]]
    cells, h = B.auto_grid(s, X0, 1.05, [3.3, 3.1, 2.6], rows, size=18, minh=0.5)
    for r in cells[1:]:
        s._anim.append([r[1], r[2]])
    c, hm = merke(s, 1.05 + h + 0.15, "Der Mindestpreis ist ein Sicherheitsnetz, kein Fixpreis.", size=20)
    s._anim.append([c])
    return s


def zahlen2():
    s = d.slide("Nur Titel", "Kurz klären: Was zeigen die Zahlen – und was nicht?")
    for k, (jahr, wert) in enumerate([("2017", "58 %"), ("2020", "36 %"), ("2024", "17 %")]):
        c = B.box(s, X0 + k * 2.0, 1.0, 1.8, 1.15, fill=CARD, line=OLIVE, lw=1.5)
        B.text(c, [[(wert, {"size": 28, "bold": True, "color": OLIVE})], jahr], size=16, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    B.tb(s, 6.6, 1.0, 2.9, 1.2, ["Haushalte in extremer Armut, befragte Kakaobauern in der Elfenbeinküste. Studie von Fairtrade und Impact Institute, Herbst 2025."], size=14, color=MUTED, after=0)
    y = 2.35
    y = frage_klick(s, y, "Beweist das, dass Fairtrade der einzige Grund ist?", "Nein – die Studie zeigt eine Entwicklung. Und sie stammt von Fairtrade selbst.", size=18)
    y = frage_klick(s, y, "Welche Frage stellen wir bei jeder Studie?", "Wer hat sie gemacht – und was hat er davon?", size=18)
    return s


def a3_auftrag():
    s = d.slide("Aufgabe", "Jetzt: Aufgabe 3 – Fair einkaufen in der Kaserne?")
    for k, (kopf, txt) in enumerate([b for b in next(x for x in TD.PARTS[2][3] if isinstance(x, dict) and x["id"] == "diskussion")["blocks"] if b[0] == "karten"][0][1]):
        x, y = X0 + (k % 2) * 4.55, 1.0 + (k // 2) * 1.55
        karte(s, x, y, 4.45, 1.45, kopf, [txt], [GREEN, ORANGE, TEAL, RUST][k], size=14)
    B.tb(s, X0, 4.1, W, 0.4, ["6 min Diskussion in Vierergruppen · dann entscheidet die Gruppe · danach reden wir gemeinsam"], size=16, bold=True, color=OLIVE, after=0)
    return s


def abgabe():
    s = d.slide("Nur Titel", "PDF abgeben – und Zusatz für Schnelle")
    y = schritte(s, X0, 1.05, 6.6, ["Arbeitsblatt: »PDF erstellen« → in LMS hochladen.", "Kein Download? »Teilen / Speichern« oder »PDF öffnen«. Geht LMS nicht: PDF per E-Mail an Prof. HOLZER.",
                                    "Noch Zeit? Quiz und Partnercheck-Karten (Theorieteil, Für Schnelle). Zusatzaufgaben sind freiwillig."], size=20, farbe=RUST)
    qr(s, "aufgaben", 7.6, 1.0, 1.2, "Arbeitsblatt"); qr(s, "quiz", 7.6, 2.75, 1.2, "Quiz")
    return s


def zusatz_folie():
    s = d.slide("Nur Titel", "OPTIONAL: Für Schnelle", hidden=True)
    rows = [["Nr.", "Zusatzaufgabe", "Zeit"]] + [[str(n), T[n]["title"], f"{T[n]['zeit']} min"] for n in (4, 5, 6)]
    cells, h = B.auto_grid(s, X0, 1.05, [0.7, 6.9, 1.4], rows, size=18, minh=0.4)
    B.tb(s, X0, 1.05 + h + 0.1, W, 0.6, ["Nur, wenn die Pflicht fertig ist. Keine Hausübung. Aufgabe 6 (Plakat, Video, Podcast) ist freiwillig."], size=16, after=0)
    return s


# ---------------------------------------------------------------- Ablauf: (Schlüssel, Phasen-Indizes, Art, Abschnitt, Wozu?, Funktion)
SPECS = {
 1: [("test1", [0, 1], "TEST", "Start", "Klassenbuch, dann Test (20 min angenommen)", test_folie),
     ("heute1", [2], "START", "Start", "Ankommen nach dem Test; Ziel und Ablauf zeigen (QR für Theorieteil und Arbeitsblatt)", heute1),
     ("einst1", [3], "EINSTIEG", "Teil 1", "Gemeinsam schätzen, Handzeichen zählen; Zahl noch nicht auflösen", einst1),
     ("lesen1", [4], "LESEN", "Teil 1", "Selbst lesen, auch im Schulbuch S. 35–36 – nicht vorerklären",
      lambda: lesen_folie(1, "Schulbuch S. 35–36: Was soll der faire Handel für Bauernfamilien verändern? Markiere es.", ["fairhandel"], "Welche drei Säulen haben die Fairtrade-Standards?", [4])),
     ("klaeren1", [5], "KURZ KLÄREN", "Teil 1", "Drei Säulen zeigen; Fehlvorstellung »Fair = Bio«", klaeren_1),
     ("a1", [6], "ZU ZWEIT", "Teil 1", "Zuordnung mit Schulbuch S. 37", a1_auftrag),
     ("a1l", [7], "BESPRECHEN", "Teil 1", "Gemeinsam durchgehen, Lösungen per Klick", a1_loesung),
     ("res1", [8], "WIEDERHOLEN", "Teil 1", "Puffer: Stoppfragen, Quiz – nichts Neues beginnen", reserve1)],
 2: [("heute2", [0], "START", "Start", "Klassenbuch; Ziel und Ablauf (QR)", heute2),
     ("rueck2", [1], "WIEDERHOLEN", "Teil 2", "Stoppfragen von Teil 1; Schätzung von letzter Woche wieder aufgreifen", rueck2),
     ("lesen2", [2], "LESEN", "Teil 2", "Selbst lesen, auch Schulbuch S. 37",
      lambda: lesen_folie(2, "Schulbuch S. 37: Was passiert, wenn der Weltmarktpreis tief fällt? Unterstreiche es.", ["mindestpreis"], "Was ist der Unterschied zwischen Mindestpreis und Prämie?", [2])),
     ("klaeren2", [3], "KURZ KLÄREN", "Teil 2", "Mindestpreis als Sicherheitsnetz, Prämie zusätzlich", klaeren_2),
     ("a2", [4], "AUFGABE", "Teil 2", "Rechnen zu zweit", a2_auftrag),
     ("a2d", [4], "AUFGABE", "Teil 2", "Diese Folie bleibt während der Arbeitszeit stehen", a2_daten),
     ("a2b", [5], "BESPRECHEN", "Teil 2", "Rechenweg zeilenweise per Klick; Frage d) im Plenum", a2_bespr),
     ("zahlen2", [6], "KURZ KLÄREN", "Teil 2", "Studie lesen: belegt oder nicht? Quellenkritik", zahlen2),
     ("a3", [7], "AUFGABE", "Teil 2", "Gruppendiskussion mit Rollenkarten (6 min), dann Plenum", a3_auftrag),
     ("abgabe", [8, 9], "ABGABE", "Abschluss", "PDF in LMS; Quiz und Zusatz; Reserve", abgabe)],
}
for _std, _sp in SPECS.items():
    assert sorted({i for x in _sp for i in x[1]}) == list(range(len(P.PLAN[I.KLASSEN[0]][_std - 1]["phasen"]))), _std
DANACH = {1: {"test1": "Ankommen und Ziel", "heute1": "Einstieg", "einst1": "Lesen Teil 1", "lesen1": "Kurz klären", "klaeren1": "Aufgabe 1", "a1": "Besprechen",
              "a1l": "Wiederholen", "res1": "Ende – nächste Woche Teil 2"},
         2: {"heute2": "Rückblick", "rueck2": "Lesen Teil 2", "lesen2": "Kurz klären", "klaeren2": "Aufgabe 2", "a2": "Daten", "a2d": "Besprechen", "a2b": "Zahlen prüfen",
             "zahlen2": "Aufgabe 3", "a3": "PDF abgeben", "abgabe": "Ende – nächstes Thema laut Jahresplan"}}


# ================================================================ Deck bauen
def bauen():
    global d, STD
    d = B.Deck(True, "TÖW · 5AB · K1.8 Fairer Handel · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Fairer Handel")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["TÖW · 5AB · K1.8 · Unterrichts-PPP · " + I.wann() + " · Buch S. 35–38",
                        [(f"Stand {I.STAND} · {I.V_UNT} · TH-Unterricht (Ablauf, 2 Stunden)", {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    bedien = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    regie = {(k, st): d.slide("Nur Titel", f"Regie {k} · {I.DATEN[k][st]} · Stunde {st}", hidden=True) for st in (1, 2) for k in I.KLASSEN}
    ziele = d.slide("Nur Titel", "Lehrer-Info · Lernziele und Abdeckung", hidden=True)
    ablauf = {1: [titel], 2: [titel]}
    for STD in (1, 2):
        abschnitt = None
        for key, idx, art, absch, wozu, fn in SPECS[STD]:
            if absch != abschnitt:
                d.section(f"Stunde {STD} · {absch}"); abschnitt = absch
            s = fn(); FOLIE[(STD, key)] = s
            hinweis(s, art, minuten(idx), DANACH[STD][key])
            if absch.startswith("Teil") or absch == "Abschluss":
                B.pill(s, I.TEILBUCH[STD], w=2.2)
            check(s)
            ablauf[STD].append(s)
    STD = 1
    d.section("Optional")
    zusatz = zusatz_folie()

    nr_von = {s.slide_id: i + 1 for i, s in enumerate(d.p.slides)}
    NR = lambda std, key: nr_von[FOLIE[(std, key)].slide_id]
    for st in (1, 2):
        for k in I.KLASSEN:
            s = regie[(k, st)]
            rows = [["Minute", "Was läuft jetzt?", "Folie", "Wozu?"]]; t0 = 0
            zu = {}
            for key, idx, art, absch, wozu, fn in SPECS[st]:
                for i in idx: zu.setdefault(i, []).append((key, wozu))
            for i, (name, mi, oh, a) in enumerate(phasen(k, st)):
                fol = ", ".join(dict.fromkeys(str(NR(st, x)) for x, _ in zu[i]))
                wz = " / ".join(dict.fromkeys(w for _, w in zu[i])) if a != "reserve" else "Puffer – nichts Neues beginnen"
                rows.append([f"{t0}–{t0 + mi}", name, fol, wz]); t0 += mi
            assert t0 == 50
            B.tb(s, X0, 0.98, W, 0.3, [[(f"{k} · {I.DATEN[k][st]} · Benutzerdefinierte Präsentation »{k} {I.DATEN[k][st]} Stunde {st}« · Foliennummern gelten für diese Datei", {"bold": True, "color": RUST})]], size=11, after=0)
            kn = P.KNAPP[(k, st)]
            hk = B.th("Wenn es knapp wird: " + kn, 10, W, pad=0.04)
            size = 11
            while size > 8 and B.table_h([0.8, 4.0, 0.7, 3.5], rows, size=size, minh=0.2) + hk > 3.95: size -= 1
            cells, h = B.auto_grid(s, X0, 1.28, [0.8, 4.0, 0.7, 3.5], rows, size=size, minh=0.2)
            B.tb(s, X0, 1.3 + h, W, hk, [[("Wenn es knapp wird: ", {"bold": True, "color": RUST}), (kn, {})]], size=10, after=0)
    B.tb(bedien, X0, 0.98, W, 4.1, [
        [("Eine Datei, zwei Stunden, beide Klassen. ", {"bold": True, "color": OLIVE}), ("Stunde 1 (Testtag, kurz): 5BK Di 10.11., 5AK Do 12.11. Stunde 2: 5BK Di 17.11., 5AK Do 19.11. (Annahme – bitte prüfen). Benutzerdefinierte Präsentationen je Klasse und Stunde: Menü Bildschirmpräsentation.", {})],
        [("Stunde 1: ", {"bold": True, "color": OLIVE}), ("Test (20 min angenommen) → Ankommen → Schätzen (gemeinsam) → Lesen Teil 1 → Kurz klären → Aufgabe 1 → Besprechen → Reserve.", {})],
        [("Stunde 2: ", {"bold": True, "color": OLIVE}), ("Rückblick → Lesen Teil 2 → Mindestpreis klären → Aufgabe 2 → Besprechen → Zahlen prüfen → Aufgabe 3 (Gruppendiskussion) → PDF.", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht, was JETZT läuft (Minuten aus plan.py) und was DANACH kommt.", {})],
        [("Zeit: ", {"bold": True, "color": OLIVE}), ("50 min nominal, aber realistisch höchstens 40 – deshalb 6 bzw. 8 min Reserve. Zeitstopp und Kürzungsweg auf der Regiefolie.", {})],
        [("Nicht eingebaut: ", {"bold": True, "color": OLIVE}), ("Videos, Lösungsmappe, Lehrer-/Kadetten-PPP. Zusatz 4–6: ausgeblendete Folie »OPTIONAL«.", {})]],
        size=13, after=5)
    rows = [["Lernziel (Kadetten)", "Wo?"], [B.plain(I.LERNZIELE[0]), "Stunde 1: Lesen, Klären, A1"], [B.plain(I.LERNZIELE[1]), "Stunde 2: Klären, A2"],
            [B.plain(I.LERNZIELE[2]), "Stunde 2: Zahlen prüfen, Zusatz 4"], [B.plain(I.LERNZIELE[3]), "Stunde 2: A3 Gruppendiskussion"]]
    cells, h = B.auto_grid(ziele, X0, 1.0, [6.4, 2.6], rows, size=13, minh=0.3)
    B.tb(ziele, X0, 1.05 + h, W, 1.5, ["Jahresplan E5 (Wirtschafts-, Umwelt- und Warenethik; Fairer Handel), 2 Std. – hier nur Fairer Handel (Buch S. 35–38); Ethik S. 31–34 bleibt offen."], size=13, after=0)

    pres = d.p.part._element
    csl = etree.Element("{%s}custShowLst" % NS_P)
    anker = pres.find("{%s}defaultTextStyle" % NS_P)
    if anker is not None: anker.addprevious(csl)
    else: pres.append(csl)
    rid = {s.slide_id: el.get("{%s}id" % NS_R) for s, el in zip(d.p.slides, d.p.slides._sldIdLst)}
    nid = [0]

    def show(name, folien):
        cs = etree.SubElement(csl, "{%s}custShow" % NS_P, name=name, id=str(nid[0])); nid[0] += 1
        l = etree.SubElement(cs, "{%s}sldLst" % NS_P)
        for sl in folien: etree.SubElement(l, "{%s}sld" % NS_P).set("{%s}id" % NS_R, rid[sl.slide_id])

    for st in (1, 2):
        for k in I.KLASSEN:
            show(f"{k} {I.DATEN[k][st]} Stunde {st}", ([titel] if st == 1 else []) + [x for x in ablauf[st] if x is not titel])
    show("Lehrer-Regiepläne", [bedien] + list(regie.values()) + [ziele])
    show("Optional: Für Schnelle", [zusatz])

    os.makedirs(ZIEL, exist_ok=True)
    name = f"{I.PRAEFIX}-TH-Unterricht-{I.V_UNT}.pptx"
    d.save(os.path.join(ZIEL, name))
    sicht = [s for s in d.p.slides if s._element.get("show") != "0"]
    for x in PROBLEME: print("ÜBERLAUF", x)
    print("ok", name, len(d.p.slides._sldIdLst), "Folien,", len(sicht), "sichtbar ·", nid[0], "Präsentationen")


if __name__ == "__main__":
    bauen()
