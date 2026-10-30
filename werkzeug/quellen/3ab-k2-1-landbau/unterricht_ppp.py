"""Unterrichts-PPP K2.1 Formen der Landwirtschaft (TH-Unterricht) – die kurze, geführte PPP für den Frontalunterricht im Saal.
v1 = ChatGPT-Arbeitsfassung (40 Folien, 28.10.2026): Reihenfolge und Inhalte je Termin übernommen und verbessert (Stephan, 30.10.2026: »verbessere sie nur und teste sie«).
Verbessert nach »bhak-ppp-gestaltung« 10–14: Lesestopps mit exaktem Abschnittstitel und QR, »KURZ KLÄREN« mit Grafik und Klick-Antwort, alle Pflichtaufgaben 1–9
mit Zeit und erwartetem Ergebnis (ChatGPT: A1 und A3 fehlten), Regie je Stunde als Tabelle Minute · Was läuft · Folie · Wozu (aus plan.py statt Fließtext),
Phasenhinweis unten links, benutzerdefinierte Präsentationen je Stunde, »Aufgabe n« statt »A2«, »Buch S.« statt »Theorie S.«, keine Buchbilder.
3AK und 3BK haben denselben Ablauf und dieselben Termine. Alle Minuten kommen aus plan.py.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/3ab-k2-1-landbau/unterricht_ppp.py <BHAK_Folienmaster_Vorlage.pptx> <Zielordner>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bauen_ppp as B
import inhalt as I, plan as P, theorie_daten as TD
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

FARBE = {"LESEN": TEAL, "KURZ KLÄREN": OLIVE, "AUFGABE": GREEN, "BESPRECHEN": ORANGE, "HÖREN": TEAL, "BEWEGUNG": ORANGE,
         "START": MUTED, "TEST": MUTED, "ABGABE": RUST, "EINSTIEG": ORANGE, "WIEDERHOLEN": TEAL, "ZU ZWEIT": GREEN}
TITEL = {it["id"]: it["title"] for p in TD.PARTS for it in p[3] if isinstance(it, dict)}
TITEL.update({it["id"]: it["title"] for it in TD.EINSTIEG})
T = {t["nr"]: t for t in I.T}


# ================================================================ Bausteine
def phasen(teil, k="3AK"):
    st = [x for x in P.PLAN[k] if x["teile"] == [teil]][0]
    return st["phasen"]


def minuten(teil, idx):
    """Minuten der Phasen idx im Teil; unterscheiden sich die Klassen, beide nennen."""
    m = {k: sum(phasen(teil, k)[i][1] for i in idx) for k in I.KLASSEN}
    assert len(set(m.values())) == 1, m
    return f"{m[I.KLASSEN[0]]} min"


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


def heute_folie(teil):
    s = d.slide("Nur Titel", f"Teil {teil} · Heute")
    wann = I.wann(teil)
    B.tb(s, X0, 0.98, W, 0.32, [[(I.TEILNAME[teil] + " · " + wann, {"bold": True, "color": TEAL})]], size=16, after=0)
    ziel = HEUTE_ZIEL[teil]
    c = B.box(s, X0, 1.36, 7.0, B.th("Ziel: " + ziel, 20, 6.9, pad=0.16), fill=OLIVE)
    B.text(c, [[("Ziel: ", {"bold": True}), (ziel, {})]], size=20, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, after=0)
    y = 1.36 + c.height / 914400 + 0.12
    st = [(sp[3], sp[1]) for sp in SPEC[teil] if sp[3]]
    items = [f"{lab} · {minuten(teil, idx)}" for lab, idx in st]
    if len(items) <= 4: schritte(s, X0, y, 6.6, items, size=18, farbe=GREEN)
    else:
        h1 = (len(items) + 1) // 2
        for col, part in enumerate((items[:h1], items[h1:])):
            yy = y
            for i, it in enumerate(part):
                n = i + 1 + col * h1
                c = B.box(s, X0 + col * 3.6, yy + 0.04, 0.4, 0.4, fill=GREEN)
                B.text(c, [str(n)], size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
                hh = B.th(it, 18, 3.1, pad=0.04)
                B.tb(s, X0 + col * 3.6 + 0.48, yy, 3.1, hh, [it], size=18, after=0); yy += max(0.5, hh + 0.04)
    qr(s, "aufgaben", 7.75, 1.36, 1.05, "Arbeitsblatt")
    qr(s, "theorie", 7.75, 2.85, 1.05, "Theorieteil")
    return s


def lesen_folie(teil, buch, abschnitte, leitfrage, idx):
    titel = "Lesen: " + (TITEL[abschnitte[0]] if len(abschnitte) == 1 else f"Theorieteil Teil {teil}")
    if len(titel) > 40: titel = f"Lesen: Theorieteil Teil {teil}"
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
        hh = max(0.44, B.th("»" + TITEL[a] + "«", 20, 6.4, True, pad=0.16))
        c = B.box(s, X0, y, 6.9, hh, fill=RGBColor.from_string("E8F1F3"), line=TEAL, lw=1.25)
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




# ---------------------------------------------------------------- Inhalte (kurz, nur das Wichtigste – Grundlage: ChatGPT v1, Folien 3–34)
HEUTE_ZIEL = I.HEUTE_ZIEL
GR = RGBColor.from_string("FFFFFF")


def bild(s, name, x, y, w, h):
    B.picture(s, UNIT + "img/" + name, x, y, w, h)


# ---- Stunde 1
def t1_einstieg():
    s = d.slide("Nur Titel", "Ist Bio automatisch umweltfreundlicher?")
    karte(s, X0, 1.0, 4.4, 1.35, "Apfel A", ["**Bio** aus Neuseeland · ca. 18 000 km"], GREEN)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.35, "Apfel B", ["**konventionell** aus der Steiermark · ca. 150 km"], OLIVE)
    y = 2.55
    y = frage_klick(s, y, "Handzeichen: Welcher ist besser? Und welche Angaben fehlen dir?", "Transportweg, Lagerung (Kühlhaus!), Ertrag, Dünger und Spritzmittel – »bio« allein beantwortet das nicht.")
    return s


def t1_mythos():
    s = d.slide("Nur Titel", "Mythos-Check: »Bio ist chemiefrei«")
    karte(s, X0, 1.0, 4.4, 1.55, "Was viele meinen", ["Bio = keine Chemie, keine Spritzmittel"], ORANGE)
    y = frage_klick(s, 2.75, "Stimmt das? Stellung nehmen – mit einem Grund.", "Nein: Alles ist Chemie. Bio verbietet bestimmte Mittel (Mineral-Stickstoff, Gentechnik), erlaubt andere unter Auflagen.")
    return s


def t1_klaeren_acker():
    s = d.slide("Nur Titel", "Kurz klären: Was die Ernte mitnimmt")
    bild(s, "acker.png", X0, 1.0, 4.6, 3.3)
    y = frage_klick(s, 1.0, "Warum ersetzt Sonnenlicht keinen Dünger?", "Licht liefert Energie, keine Nährstoffe (N, P, K) – die gehen mit der Ernte weg.", w=4.3, x=5.2, size=18)
    y = frage_klick(s, y, "Muss auch Bio düngen?", "Ja – mit Mist, Kompost, Leguminosen.", w=4.3, x=5.2, size=18)
    return s


def t1_klaeren_formen():
    s = d.slide("Nur Titel", "Kurz klären: vier Merkmale, drei Formen")
    rows = [["Merkmal", "konventionell", "integriert", "biologisch"], ["Boden", "", "", ""], ["Dünger und Pflanzenschutz", "", "", ""], ["Kulturen", "", "", ""], ["Tiere", "", "", ""]]
    cells, h = B.auto_grid(s, X0, 1.0, [2.6, 2.1, 2.1, 2.2], rows, size=16, minh=0.34)
    y = frage_klick(s, 1.0 + h + 0.12, "Ist »integriert« eine eigene dritte Welt?", "Nein – ein Vorgehen (beobachten, dann gezielt), das auch konventionelle Betriebe nutzen.", size=18)
    return s


def t1_a1():
    s = auftrag_folie("Jetzt: Aufgabe 1 – arbeitsteilig zu zweit", [1], {1: "zu zweit, eine Spalte je Paar"},
                      "eure Form mit 4 Stichpunkten – nach der Besprechung Foto der Tafel", ohne_handy="Erst im Heft sammeln, dann eintippen.")
    B.tb(s, X0, 3.9, W, 0.5, [[("Formen: ", {"bold": True, "color": OLIVE}), ("Reihe 1 → konventionell · Reihe 2 → integriert · Reihe 3 → biologisch", {})]], size=18, after=0)
    return s


def t1_a1_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 1 – die Matrix")
    M1 = I.T[0]["matrix"]
    rows = [["", "konventionell", "integriert", "biologisch"]]
    for lab, k in (("Boden", "boden"), ("Dünger, Schutz", "mittel"), ("Kulturen", "kultur"), ("Tiere", "tiere")):
        rows.append([lab] + M1[k])
    cells, h = B.auto_grid(s, X0, 0.98, [1.2, 2.6, 2.6, 2.6], rows, size=16, minh=0.3)
    for r in cells[1:]: s._anim.append(r[1:])
    return s


def t1_lesen_dok():
    return lesen_folie(1, None, ["dok"], "Wie viel weniger Ertrag hatte Bio im Schnitt – und gilt das für jeden Betrieb?", [6])


def t1_a2():
    return auftrag_folie("Jetzt: Aufgabe 2 – zu zweit", [2], {2: "zu zweit am Handy"}, "a) 2 Maßnahmen mit Wirkung · b) 1 Satz »warum nicht bio« · c) 2 Angaben Tierhaltung · d) 1 Satz zu den 20 %")


def t1_a2_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 2")
    y = 1.05
    y = frage_klick(s, y, "Hecken und Fruchtfolge – reicht das für »bio«?", "Nein – einzelne Maßnahmen gibt es überall. Bio heißt: alle Regeln plus jährliche Kontrolle.")
    y = frage_klick(s, y, "Gilt »20 % weniger Ertrag« für jeden Bio-Betrieb?", "Nein – Mittelwert eines Versuchs; Kultur, Boden, Jahr verschieden.")
    return s


# ---- Stunde 2
def t2_heute_extra(): pass


def t2_a3():
    return auftrag_folie("Jetzt: Aufgabe 3 – allein", [3], {3: "allein am Handy"}, "zu drei Methoden je eine Wirkung und eine Grenze + 1 Satz zur Schadschwelle")


def t2_a4():
    s = auftrag_folie("Jetzt: Aufgabe 4 – Verpackungen in Gruppen", [4], {4: "Gruppe, zwei Verpackungen"}, "Zeichen, Code, Herkunft, Preis pro kg · 3 Korrekturen zum KI-Satz",
                      ohne_handy="Erst Verpackungen lesen und notieren, dann eintippen.")
    B.tb(s, X0, 3.95, W, 0.5, [[("Keine Verpackungen? ", {"bold": True, "color": RUST}), ("Beispiel: Bio-Milch »AT-BIO-301 · Österreich-Landwirtschaft · 1,59 €/l«", {})]], size=16, after=0)
    return s


def t2_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: pro Hektar oder pro Kilogramm?")
    bild(s, "flaeche.png", X0, 1.0, 5.2, 3.2)
    y = frage_klick(s, 1.0, "Fläche = Menge : Ertrag. 20 % weniger Ertrag – wie viel mehr Fläche?", "100 : 80 = 1,25 → 25 % mehr, nicht 20 %.", w=3.7, x=5.8, size=18)
    return s


def t2_a5():
    return auftrag_folie("Jetzt: Aufgabe 5 – allein rechnen", [5], {5: "allein, Rechenweg im Heft"}, "zwei Flächen in ha (2 Dezimalstellen) + 1 Satz, warum das keine Regel ist")


def t2_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgaben 3 und 4")
    y = 1.05
    y = frage_klick(s, y, "Warum soll nicht jede Laus weg?", "Kleiner Befall ist tragbar – erst ab der Schadschwelle lohnt sich eine Maßnahme.")
    y = frage_klick(s, y, "»Bio ist automatisch regional, pestizidfrei und klimafreundlicher.«", "nicht regional (Herkunftszeile!) · bestimmte Mittel erlaubt · Klima nur mit Daten")
    return s


# ---- Stunde 3
def t3_partnercheck():
    s = d.slide("Nur Titel", "Partnercheck mit drei Karten")
    y = schritte(s, X0, 1.05, 6.6, ["A zieht 3 Karten (Theorieteil »Partnercheck«) und liest vor.", "B antwortet, A vergleicht und hakt ab.", "Tauschen. Handy nur für die Karten – dann weg."], size=20, farbe=TEAL)
    qr(s, "theorie", 7.75, 1.05, 1.2, "Theorieteil")
    return s


def t3_sof():
    s = d.slide("Nur Titel", "Science oder Fiction? Der Dino aus dem Labor")
    karte(s, X0, 1.0, W, 1.2, "Im Film Jurassic Park", ["Dino-DNA aus Mücken in Bernstein, Lücken mit Frosch-DNA gefüllt – fertig ist der Dinosaurier."], ORANGE)
    y = frage_klick(s, 2.4, "Science oder Fiction?", "Fiction: DNA zerfällt, nach 66 Mio. Jahren ist nichts übrig. Science: DNA gezielt an einer Stelle ändern – das kann die Genschere.")
    return s


def t3_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: die Genschere in vier Schritten")
    bild(s, "genschere.png", X0 + 0.9, 0.98, W - 1.8, 2.25)
    y = frage_klick(s, 3.3, "Präziser Schnitt = sicher?", "Nein – geprüft wird das Ergebnis, nicht nur die Methode.", size=18)
    return s


def t3_hoeren():
    s = d.slide("Nur Titel", "Hören: Martin Moder erklärt Gentechnik")
    t, q, du, u = I.VIDEOS["moder"][:4]
    karte(s, X0, 1.0, 6.9, 1.25, "Podcast »Erklär mir die Welt« #167 (2021)", ["ab **05:39**, ca. 7 min (bis etwa 12:40)"], TEAL)
    s.shapes.add_picture(B.qr_png(u), Inches(7.75), Inches(1.0), Inches(1.2), Inches(1.2))
    y = schritte(s, X0, 2.45, W, ["Notiere zwei Aussagen von Moder.", "Notiere eine Rückfrage, die man überprüfen könnte.", "Achtung: Stand 2021 – das EU-Recht hat sich seither geändert."], size=20, farbe=TEAL)
    return s


def t3_a6():
    return auftrag_folie("Jetzt: Aufgabe 6 – zu zweit am Mini-Whiteboard", [6], {6: "erst zeichnen, dann Foto und tippen"}, "3 Sätze (Leit-RNA, Cas9, Zelle) · 3 Verfahren verglichen · Foto der 4-Schritte-Skizze",
                        ohne_handy="Zuerst zeichnen, erst dann fotografieren und tippen.")


def t3_a7():
    return auftrag_folie("Jetzt: Aufgabe 7 – zu zweit", [7], {7: "zu zweit am Handy"}, "1 möglicher Nutzen · 2 Prüffragen (Anbau, Lebensmittel/Umwelt) · 1 wirtschaftliche Frage")


def t3_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgaben 5–7")
    y = 1.05
    y = frage_klick(s, y, "80 dt bei 80 bzw. 36 dt/ha – welche Flächen?", "1,00 ha und 2,22 ha (alte deutsche Werte 2015/16)")
    y = frage_klick(s, y, "Was macht die Leit-RNA, was Cas9, was die Zelle?", "findet die Stelle · schneidet · repariert – danach prüfen")
    y = frage_klick(s, y, "Wie prüft man die Pilz-Sorte? Und Patente?", "Feldversuche: Vergleichssorte, mehrere Orte und Jahre · Patente sind eine wirtschaftliche Frage")
    return s


# ---- Stunde 4
def t4_skala():
    s = d.slide("Nur Titel", "»Genmais erzeugt Krebs!« – stell dich auf")
    c = B.box(s, X0, 1.05, W, 0.9, fill=RGBColor.from_string("F6E3DF"), line=RUST, lw=2)
    B.text(c, [[("Erfundene Schlagzeile: »Genmais erzeugt Krebs!«", {"bold": True, "color": RUST})]], size=24, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    bar = B.box(s, X0 + 0.3, 2.35, W - 0.6, 0.22, fill=ORANGE)
    B.tb(s, X0, 2.65, 3.2, 0.4, ["gar nicht glaubwürdig"], size=18, bold=True, after=0)
    B.tb(s, X0 + W - 3.2, 2.65, 3.2, 0.4, ["sehr glaubwürdig"], size=18, bold=True, align=PP_ALIGN.RIGHT, after=0)
    B.tb(s, X0, 3.2, W, 0.9, ["Stell dich im Raum auf die Linie. Zwei von euch sagen, warum. Am Ende der Stunde stellt ihr euch noch einmal auf."], size=20, after=0)
    return s


def t4_a8():
    s = auftrag_folie("Jetzt: Aufgabe 8 – zu zweit mit dem Steckbrief", [8], {8: "zu zweit am Handy"}, "4 kurze Antworten: Gruppengröße, Kontrolle, Zufall, zwei weitere Angaben")
    return s


def t4_gruppen():
    s = d.slide("Aufgabe", "Aufgabe 8: 200 Ratten – wie viele je Gruppe?")
    bild(s, "gruppen.png", X0, 1.0, W, 3.0)
    a = B.tb(s, X0, 4.05, W, 0.45, ["200 : (2 Geschlechter × 10 Gruppen) = 10 Tiere je Gruppe"], size=20, bold=True, color=RED, align=PP_ALIGN.CENTER, after=0)
    s._anim.append([a])
    return s


def t4_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: was die Folgestudie zeigt – und was nicht")
    karte(s, X0, 1.0, 4.4, 1.5, "G-TwYST 2019", ["50 Tiere je Gruppe · derselbe Mais · keine Schadwirkung beim Verfüttern"], GREEN, size=18)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.5, "Nicht geprüft", ["alle Gentech-Pflanzen · Genschere-Pflanzen · jedes Spritzmittel"], RUST, size=18)
    y = frage_klick(s, 2.7, "Ist Séralini damit ein Betrüger?", "Nein – schwache Methode ist kein Betrugsbeweis. Und die Folgestudie ist kein Freibrief.", size=18)
    return s


def t4_a9():
    return auftrag_folie("Jetzt: Aufgabe 9 – mit der Hand schreiben", [9], {9: "allein auf Papier, dann Foto"}, "sachliche Überschrift + Urteil in 4–6 Sätzen (Gruppengröße, Kontrolle, EFSA, Folgestudie, Methode ≠ Betrug)",
                        ohne_handy="Mit der Hand schreiben – das Handy nur für das Foto.")


def t4_bespr():
    s = d.slide("Aufgabe", "Partner liest gegen – und noch einmal aufstellen")
    rows = [["Kriterium", "✓"]] + [[k, "☐"] for k in I.T[8]["kriterien"]]
    cells, h = B.auto_grid(s, X0, 1.0, [8.0, 1.0], rows, size=18, minh=0.4)
    y = frage_klick(s, 1.0 + h + 0.12, "Beispiel-Überschrift", "»Rattenversuch beweist Krebsgefahr durch Genmais nicht«", size=18)
    return s


def t4_abgabe():
    s = d.slide("Nur Titel", "Abgabe: eine PDF in LMS")
    y = schritte(s, X0, 1.05, 6.9, ["Arbeitsblatt: alle Aufgaben 1–9 fertig? Dann »PDF erstellen« → in LMS hochladen.", "Kein Download? »Teilen / Speichern« oder »PDF öffnen«. Geht LMS nicht: PDF per E-Mail an Stephan.",
                                    "Quiz »Landbau-Check« zum Wiederholen – freiwillig."], size=20, farbe=RUST)
    qr(s, "aufgaben", 7.75, 1.05, 1.15, "Arbeitsblatt"); qr(s, "quiz", 7.75, 2.75, 1.15, "Quiz")
    return s


def zusatz_folie():
    s = d.slide("Nur Titel", "OPTIONAL: Für Schnelle", hidden=True)
    rows = [["Nr.", "Zusatzaufgabe", "Zeit"]] + [[str(n), T[n]["title"], f"{T[n]['zeit']} min"] for n in (10, 11, 12, 13)]
    cells, h = B.auto_grid(s, X0, 1.05, [0.7, 6.9, 1.4], rows, size=20, minh=0.46)
    B.tb(s, X0, 1.05 + h + 0.15, W, 0.8, ["Nur, wenn die Pflicht fertig ist. Keine Hausübung. Quiz »Landbau-Check« (16 Fragen) freiwillig."], size=18, after=0)
    return s


# ---------------------------------------------------------------- Ablauf je Stunde: (Schlüssel, Phasen, Art, Schritt auf »Heute«, Wozu?, Funktion)
SPEC = {
 1: [("t1_heute", [0], "START", None, "Klassenbuch; Ziel und Ablauf zeigen (QR Arbeitsblatt, Theorieteil)", lambda: heute_folie(1)),
     ("t1_einst", [1], "EINSTIEG", None, "Vorwissen: Handzeichen, fehlende Angaben sammeln – noch nicht auflösen", t1_einstieg),
     ("t1_mythos", [1], "EINSTIEG", None, "Fehlvorstellung »Bio = chemiefrei« offenlegen", t1_mythos),
     ("t1_lesen", [2], "LESEN", "Lesen", "Grundlagen selbst lesen – Stephan erklärt nicht vor",
      lambda: lesen_folie(1, "**Buch S. 39 und 41–43** zum Nachschlagen", ["acker", "formen", "bio"], "Welche vier Merkmale unterscheiden die Formen?", [2])),
     ("t1_acker", [3], "KURZ KLÄREN", "Kurz klären", "Nährstoffentzug: jede Form muss düngen", t1_klaeren_acker),
     ("t1_formen", [3], "KURZ KLÄREN", None, "Vier Merkmale an die Tafel; »integriert« ist ein Vorgehen", t1_klaeren_formen),
     ("t1_a1", [4], "ZU ZWEIT", "Aufgabe 1", "K03 vollständig: 4 Merkmale × 3 Formen, arbeitsteilig", t1_a1),
     ("t1_a1b", [5], "BESPRECHEN", "Tabelle", "Tabelle gemeinsam füllen (Klick je Zeile), dann Foto der Tafel", t1_a1_bespr),
     ("t1_dok", [6], "LESEN", "Langzeitversuch", "Wie man Formen vergleicht: Wiederholung, Kontrolle, Mittelwert", t1_lesen_dok),
     ("t1_a2", [7], "AUFGABE", "Aufgabe 2", "Anwenden: konventioneller Betrieb mit guten Maßnahmen", t1_a2),
     ("t1_a2b", [8], "BESPRECHEN", None, "»Warum nicht bio?« und »20 % für alle?« klären", t1_a2_bespr),
     ("t1_pc", [9, 10], "ZU ZWEIT", "Partnercheck", "Karten 1–4 gegenseitig abfragen (ohne Handy); Reserve", t3_partnercheck)],
 2: [("t2_heute", [0, 1], "TEST", None, "Klassenbuch, Test (20 min); danach Ziel von Teil 2", lambda: heute_folie(2)),
     ("t2_lesen", [2], "LESEN", "Lesen", "Drei Methoden selbst lesen",
      lambda: lesen_folie(2, "**Buch S. 44**: Schädlingskontrolle", ["pflanzenschutz"], "Was bringt jede Methode – und wo hat sie ihre Grenze?", [2])),
     ("t2_a3", [3], "AUFGABE", "Aufgabe 3", "Methoden abwägen, Schadschwelle", t2_a3),
     ("t2_lesen2", [4], "LESEN", "Lesen", "Kennzeichnung selbst lesen, bevor die Verpackungen kommen",
      lambda: lesen_folie(2, None, ["kennzeichnung"], "Was sagt das Bio-Zeichen – und was nicht?", [4])),
     ("t2_a4", [5], "ZU ZWEIT", "Aufgabe 4", "Echte Verpackungen lesen (ohne Handy), KI-Satz korrigieren", t2_a4),
     ("t2_bespr", [6, 7], "BESPRECHEN", None, "Schadschwelle und KI-Satz sichern; Reserve", t2_bespr)],
 3: [("t3_heute", [0], "START", None, "Klassenbuch; Ziel von Teil 3", lambda: heute_folie(3)),
     ("t3_lesen0", [1], "LESEN", "Lesen", "Bezugsgröße selbst lesen",
      lambda: lesen_folie(3, None, ["bezug"], "Fläche = Menge : Ertrag – warum sind 20 % weniger Ertrag 25 % mehr Fläche?", [1])),
     ("t3_a5", [2], "AUFGABE", "Aufgabe 5", "Rechnen mit Bezugsgröße", t2_a5),
     ("t3_lesen", [3], "LESEN", "Lesen", "Gene und Genschere selbst lesen",
      lambda: lesen_folie(3, "**Buch S. 45**: Gentechnik in der Landwirtschaft", ["gene", "genschere"], "Wer findet die Stelle, wer schneidet, wer repariert?", [3])),
     ("t3_klaeren", [4], "KURZ KLÄREN", "Kurz klären", "Vier Schritte am Bild; präzise ≠ risikofrei", t3_klaeren),
     ("t3_hoeren", [5], "HÖREN", "Podcast", "Moder ab 05:39 (ca. 7 min): zwei Aussagen, eine Rückfrage", t3_hoeren),
     ("t3_a6", [6], "ZU ZWEIT", "Aufgabe 6", "Mechanismus erst am Mini-Whiteboard zeichnen, dann Foto", t3_a6),
     ("t3_lesen2", [7], "LESEN", None, "Prüffragen an eine neue Sorte",
      lambda: lesen_folie(3, None, ["sorte"], "Welche Fragen sind biologisch, welche wirtschaftlich?", [7])),
     ("t3_a7", [8], "AUFGABE", "Aufgabe 7", "Anwendung bewerten (N05)", t3_a7),
     ("t3_bespr", [9, 10], "BESPRECHEN", None, "Rechenweg, vier Schritte, Prüffragen; Reserve", t3_bespr)],
 4: [("t4_heute", [0, 1], "START", None, "Klassenbuch; »Weißt du noch?« mündlich; Ziel von Teil 4", lambda: heute_folie(4)),
     ("t4_skala", [2], "BEWEGUNG", "Aufstellen", "Vorurteil sichtbar machen – Bewegung, ohne Handy", t4_skala),
     ("t4_lesen", [3], "LESEN", "Lesen", "Steckbrief und Prüffragen selbst lesen",
      lambda: lesen_folie(4, None, ["seralini", "studie"], "Warum sagt »200 Ratten« wenig über die Aussagekraft?", [3])),
     ("t4_a8", [4], "ZU ZWEIT", "Aufgabe 8", "Studienaufbau prüfen", t4_a8),
     ("t4_gruppen", [4], "ZU ZWEIT", None, "Gruppenaufteilung per Klick auflösen (am Ende der Arbeitszeit)", t4_gruppen),
     ("t4_lesen2", [5], "LESEN", None, "Folgestudie selbst lesen",
      lambda: lesen_folie(4, None, ["gtwyst"], "Was zeigt die Folgestudie – und was nicht?", [5])),
     ("t4_klaeren", [6], "KURZ KLÄREN", "Kurz klären", "Methode ≠ Betrug, Folgestudie ≠ Freibrief", t4_klaeren),
     ("t4_a9", [7], "AUFGABE", "Aufgabe 9", "Urteil mit der Hand schreiben (kreativ, N05)", t4_a9),
     ("t4_bespr", [8], "BESPRECHEN", "Gegenlesen", "Partner prüft 5 Kriterien; zweites Aufstellen", t4_bespr),
     ("t4_abgabe", [9, 10], "ABGABE", "Abgabe", "PDF in LMS; Reserve", t4_abgabe)],
}

for teil, sp in SPEC.items():
    alle = sorted({i for x in sp for i in x[1]})
    assert alle == list(range(len(phasen(teil)))), (teil, alle)

DANACH_TEIL = {1: "Stunde 2 am Mo 09.11.: zuerst Test", 2: "Stunde 3 am Mi 11.11.: Genschere", 3: "Stunde 4 am Mo 16.11.: Studien und PDF-Abgabe",
               4: "Ende der Einheit – nächstes Kapitel: Nahrungs- und Genussmittel (Buch S. 49)"}


def FOLIE_TITEL(spec):
    return {"t1_mythos": "Mythos-Check", "t1_formen": "vier Merkmale", "t1_a2b": "Besprechen", "t2_bespr": "Besprechen", "t3_lesen2": "Lesen: neue Sorte", "t3_lesen0": "Lesen",
            "t3_bespr": "Besprechen", "t4_gruppen": "200 Ratten", "t4_lesen2": "Lesen: Folgestudie", "t1_einst": "Mythos-Check", "t3_sof": "Lesen"}.get(spec[0], spec[0])


# ================================================================ Deck bauen
def bauen():
    global d
    d = B.Deck(True, "NAWI · 3AB · K2.1 Landwirtschaft · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Formen der Landwirtschaft")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["NAWI · 3AB · K2.1 · Unterrichts-PPP · 3AK und 3BK: " + " · ".join(I.DATEN["3AK"][n] for n in (1, 2, 3, 4)) + " · Buch S. 38–48",
                        [(f"Stand {I.STAND} · {I.V} · TH-Unterricht (Ablauf) – zum Nachlesen: TH-Lehrer", {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    bedien = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    regie = {st["std"]: d.slide("Nur Titel", f"Regie 3AK und 3BK · Stunde {st['std']} · {st['datum']}", hidden=True) for st in P.PLAN["3AK"]}
    quellen = d.slide("Nur Titel", "Lehrer-Info · Was gegenüber v1 verbessert ist", hidden=True)
    for teil in (1, 2, 3, 4):
        d.section(f"Stunde {teil}")
        sec = d.slide("Abschnitt", I.TEILNAME[teil])
        for ph in sec.placeholders:
            if ph.placeholder_format.type == 2: ph.text_frame.text = I.TEILBUCH[teil] + " · " + I.wann(teil)
        FOLIE[f"t{teil}_sec"] = sec
        sp = SPEC[teil]
        for j, (key, idx, art, schritt, wozu, fn) in enumerate(sp):
            s = fn(); FOLIE[key] = s
            nxt = sp[j + 1] if j + 1 < len(sp) else None
            nn = (nxt[3] or FOLIE_TITEL(nxt)) if nxt else DANACH_TEIL[teil]
            hinweis(s, art, minuten(teil, idx), nn)
            B.pill(s, I.TEILBUCH[teil], w=2.2)
            check(s)
    d.section("Optional")
    zusatz = zusatz_folie()

    nr_von = {s.slide_id: i + 1 for i, s in enumerate(d.p.slides)}
    NR = lambda key: nr_von[FOLIE[key].slide_id]
    folgen = {t: [FOLIE[f"t{t}_sec"]] + [FOLIE[x[0]] for x in SPEC[t]] for t in (1, 2, 3, 4)}
    for st in P.PLAN["3AK"]:
        s = regie[st["std"]]; teil = st["std"]
        rows = [["Minute", "Was läuft jetzt?", "Folie", "Wozu?"]]; t0 = 0
        zu = {}
        for key, idx, art, schritt, wozu, fn in SPEC[teil]:
            for i in idx: zu.setdefault(i, []).append((key, wozu))
        for i, (name, mi, oh, a) in enumerate(st["phasen"]):
            fol = ", ".join(dict.fromkeys(str(NR(x)) for x, _ in zu[i]))
            wz = zu[i][0][1] if a != "reserve" else "Puffer – nichts Neues beginnen"
            rows.append([f"{t0}–{t0 + mi}", name + (" · ohne Handy" if oh and a not in ("org", "reserve", "test", "bespr", "erkl") else ""), fol, wz]); t0 += mi
        assert t0 == 50
        B.tb(s, X0, 0.98, W, 0.3, [[(f"3AK und 3BK · {st['datum']} · Benutzerdefinierte Präsentation »Stunde {teil} {st['datum']}« · Foliennummern gelten für diese Datei", {"bold": True, "color": RUST})]], size=10, after=0)
        kn = P.KNAPP[("3AK", teil)]
        hk = B.th("Wenn es knapp wird: " + kn, 10, W, pad=0.04)
        size = 11
        while size > 8 and B.table_h([0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2) + hk > 3.95: size -= 1
        cells, h = B.auto_grid(s, X0, 1.28, [0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2)
        B.tb(s, X0, 1.3 + h, W, hk, [[("Wenn es knapp wird: ", {"bold": True, "color": RUST}), (kn, {})]], size=10, after=0)
    B.tb(bedien, X0, 0.98, W, 4.1, [
        [("Eine Datei, beide Klassen, gleiche Termine. ", {"bold": True, "color": OLIVE}), ("F5 zeigt alle sichtbaren Folien in Unterrichtsreihenfolge (Stunde 1 → 4).", {})],
        [("Pro Stunde starten: ", {"bold": True, "color": OLIVE}), ("Bildschirmpräsentation → Benutzerdefinierte Bildschirmpräsentation → z. B. »Stunde 2 Mo 09.11.«. Ohne Menü: Foliennummer tippen und Enter (Nummern auf den Regiefolien).", {})],
        [("Jede Stunde läuft gleich: ", {"bold": True, "color": OLIVE}), ("»Heute« → »Lesen: …« (genaue Abschnitte im Theorieteil, Leitfrage) → »Kurz klären« (nur Fehlvorstellungen, Antwort per Klick) → »Jetzt: Aufgabe …« → »Besprechen« (Lösung per Klick, erst nach der Arbeitszeit).", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht, was JETZT läuft (Minuten aus plan.py) und was DANACH kommt.", {})],
        [("Stunde 2: ", {"bold": True, "color": OLIVE}), ("zuerst der Test (20 min, nicht in dieser PPP). Verpackungen mitbringen.", {})],
        [("Nachschlagen statt zeigen: ", {"bold": True, "color": OLIVE}), ("TH-Lehrer und Theorieteil bleiben vollständig; Lösungen auch in TH-Loesung und der privaten Lösungsmappe. Zusatz 10–13: ausgeblendete Folie »OPTIONAL«.", {})],
        [("Regiepläne: ", {"bold": True, "color": OLIVE}), (f"Folien {nr_von[regie[1].slide_id]}–{nr_von[regie[4].slide_id]} (ausgeblendet), Präsentation »Lehrer-Regiepläne«.", {})]],
        size=13, after=5)
    B.tb(quellen, X0, 0.98, W, 4.1, ["· " + x for x in [
        "Grundlage: ChatGPTs TH-Unterricht v1 (40 Folien) – Reihenfolge der Termine, Einstieg (Bio-Apfel), Hörauftrag Moder, Schlagzeile, Sportbeispiel übernommen.",
        "Neu: Folien zu Aufgabe 1 (Matrix arbeitsteilig, Besprechung per Klick) und Aufgabe 3; alle 9 Pflichtaufgaben mit Zeit und »Am Ende steht da«.",
        "Neu: Lesestopps mit genauen Abschnittstiteln und QR-Code; »Kurz klären« mit eigener Grafik statt Stichpunkt-Listen; Regie als Tabelle aus plan.py.",
        "Neu: Methodenwechsel (Handzeichen und Partnercheck · Verpackungen in Gruppen · Mini-Whiteboard und Podcast · Aufstellen auf einer Skala), Klassenbuch und Reserve je Stunde; Aufgabe 5 am Anfang von Stunde 3.",
        "Korrigiert: »A2« → »Aufgabe 2«, »Theorie S.« → »Buch S.«; Regie-Fließtext ersetzt; keine Buchbilder (darum frei weitergebbar).",
        "Geprüft: in LibreOffice gerendert und alle Folien angesehen; Abspieltest in Microsoft PowerPoint (Klicks, benutzerdefinierte Präsentationen) steht aus."]], size=13, after=5)

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

    show("3AK und 3BK gesamt", [titel] + sum([folgen[t] for t in (1, 2, 3, 4)], []))
    for st in P.PLAN["3AK"]:
        show(f"Stunde {st['std']} {st['datum']}", ([titel] if st["std"] == 1 else []) + folgen[st["std"]])
    show("Lehrer-Regiepläne", [bedien] + [regie[n] for n in (1, 2, 3, 4)] + [quellen])
    show("Optional: Für Schnelle", [zusatz])

    os.makedirs(ZIEL, exist_ok=True)
    name = f"{I.PRAEFIX}-TH-Unterricht-{I.V}.pptx"
    d.save(os.path.join(ZIEL, name))
    sicht = [s for s in d.p.slides if s._element.get("show") != "0"]
    for x in PROBLEME: print("ÜBERLAUF", x)
    print("ok", name, len(d.p.slides._sldIdLst), "Folien,", len(sicht), "sichtbar ·", nid[0], "Präsentationen")
    for t in (1, 2, 3, 4): print("  Stunde", t, "Folien", [nr_von[x.slide_id] for x in folgen[t]])


if __name__ == "__main__":
    bauen()
