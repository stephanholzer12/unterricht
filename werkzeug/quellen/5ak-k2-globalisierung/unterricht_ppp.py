"""Unterrichts-PPP K2 Globalisierung und aktuelle Weltpolitik (TH-Unterricht, 5AK IWK) – die kurze, geführte PPP für den Frontalunterricht im Saal.
Nach »bhak-ppp-gestaltung«: Lesestopps mit exaktem Abschnittstitel und QR, »KURZ KLÄREN« mit Grafik und Klick-Antwort, alle Pflichtaufgaben 1–8 mit Zeit und erwartetem Ergebnis,
Regie je Stunde als ausgeblendete Tabelle (Minute · Was läuft · Folie · Wozu, aus plan.py), Phasenhinweis unten links, benutzerdefinierte Präsentationen je Stunde,
»Aufgabe n«, »Buch S.«, keine Buchbilder. Alle Minuten kommen aus plan.py. Ein Test in Stunde 2 (20 min) ist nicht Teil dieser PPP.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/5ak-k2-globalisierung/unterricht_ppp.py <BHAK_Folienmaster_Vorlage.pptx> <Zielordner>"""
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
         "START": MUTED, "TEST": MUTED, "ABGABE": RUST, "EINSTIEG": ORANGE, "WIEDERHOLEN": TEAL, "ZU ZWEIT": GREEN, "GRUPPE": GREEN}
TITEL = {it["id"]: it["title"] for p in TD.PARTS for it in p[3] if isinstance(it, dict)}
TITEL.update({it["id"]: it["title"] for it in TD.EINSTIEG})
T = {t["nr"]: t for t in I.T}


# ================================================================ Bausteine
def phasen(teil, k=None):
    k = k or I.KLASSEN[0]
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
    s = d.slide("Nur Titel", f"Stunde {teil} · Heute")
    wann = I.wann(teil)
    B.tb(s, X0, 0.98, W, 0.32, [[(I.TEILKURZ[teil] + " · " + wann, {"bold": True, "color": TEAL})]], size=16, after=0)
    ziel = HEUTE_ZIEL[teil]
    c = B.box(s, X0, 1.36, 7.0, B.th("Ziel: " + ziel, 20, 6.9, pad=0.16), fill=OLIVE)
    B.text(c, [[("Ziel: ", {"bold": True}), (ziel, {})]], size=20, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, after=0)
    y = 1.36 + c.height / 914400 + 0.12
    st = [(sp[3], sp[1]) for sp in SPEC[teil] if sp[3]]
    items = [f"{lab} · {minuten(teil, idx)}" for lab, idx in st]
    if len(items) <= 3: schritte(s, X0, y, 6.6, items, size=18, farbe=GREEN)
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
    titel = "Lesen: " + (TITEL[abschnitte[0]] if len(abschnitte) == 1 else f"Theorieteil Stunde {teil}")
    if len(titel) > 40: titel = f"Lesen: Theorieteil Stunde {teil}"
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


def auftrag_folie(titel, nrs, tun, erwartet, ohne_handy=False, layout="Aufgabe", zeit=None):
    """Arbeitsphase: welche Aufgaben, was genau tun, wie lange, was am Ende dastehen soll."""
    s = d.slide(layout, titel)
    rows = [["Nr.", "Aufgabe", "Zeit", "So arbeitest du"]]
    for n in nrs:
        rows.append([str(n), T[n]["title"], f"{zeit or T[n]['zeit']} min", tun.get(n, "allein am Handy")])
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




# ---------------------------------------------------------------- Inhalte (kurz, nur das Wichtigste – Aufgaben und Lösungen stehen in Seite, Theorie und Lösungsmappe)
HEUTE_ZIEL = I.HEUTE_ZIEL
GR = RGBColor.from_string("FFFFFF")
K0 = I.KLASSEN[0]


def bild(s, name, x, y, w, h):
    B.picture(s, UNIT + "img/" + name, x, y, w, h)


def notiz(s, y, txt, size=16, farbe=None):
    B.tb(s, X0, y, W, 0.5, [[(txt, {})]], size=size, color=farbe or INK, after=0)


# ---- Stunde 1
def t1_einst():
    s = d.slide("Nur Titel", "Marke oder Produkt – woher kommt es?")
    karte(s, X0, 1.0, 4.4, 1.35, "Die Marke", ["Österreichischer Anbieter · Entwicklung und Vertrieb"], GREEN)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.35, "Das Produkt", ["Bauteile · Montage · Datenverarbeitung – wo?"], ORANGE)
    frage_klick(s, 2.55, "Ist eine österreichische Marke automatisch ein österreichisches Produkt? Zwei begründete Vermutungen an die Tafel.",
                "Nein – Marke, Entwicklung, Bauteile, Montage und Daten können in verschiedenen Ländern liegen. Die Sportuhr ist ein Modell, keine echte Marke.")
    return s


def t1_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: vier Ströme am Modell")
    bild(s, "sportuhr.png", X0, 1.0, 4.6, 2.86)
    y = frage_klick(s, 1.0, "Welche vier Ströme verbinden die Stationen?", "Waren · Geld · Daten · Wissen", w=4.3, x=5.2, size=18)
    y = frage_klick(s, y, "Ist Globalisierung nur Warenhandel?", "Nein – auch Wissen, Geld, Menschen, Kultur und Daten.", w=4.3, x=5.2, size=18)
    return s


def t1_a1():
    s = auftrag_folie("Jetzt: Aufgabe 1 – Flussbild zu zweit", [1], {1: "zu zweit: Papier, dann Foto"},
                      "Flussbild mit ≥ 4 Stationen · je ein Waren-, Geld-, Daten-, Wissensstrom · zwei Akteure · ein Engpass",
                      ohne_handy="Erst auf Papier zeichnen, dann fotografieren und eintippen.")
    notiz(s, 3.95, "Modell: Entwicklung (Europa) · Halbleiter (Ostasien) · Montage (Südostasien) · Rohstoffe · Rechenzentrum · Absatz (Europa, USA)")
    return s


def t1_a1b():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 1 – Beispielströme")
    rows = [["Strom", "Beispiel (Modell)"], ["Waren", "Chips Ostasien → Montage Südostasien · Uhren → Europa, USA"], ["Geld", "Käufer → Anbieter → Zulieferer · Zahlung ans Rechenzentrum"],
            ["Daten", "Trainingsdaten → Rechenzentrum → Auswertung zurück"], ["Wissen", "Entwicklungsvorgaben, Software, Know-how"]]
    cells, h = B.auto_grid(s, X0, 0.98, [1.4, 7.6], rows, size=16, minh=0.34)
    for r in cells[1:]: s._anim.append(r[1:])
    frage_klick(s, 0.98 + h + 0.12, "Engpass: Der Chip fehlt – wer ist betroffen?", "Montage und Auslieferung. Wert entsteht auch durch Entwicklung, Software und Vertrieb – nicht nur durch Montage.", size=18)
    return s


def t1_lesen2():
    return lesen_folie(1, "**Buch S. 48 und 64–70** zum Nachschlagen", ["folgen"], "Für wen ist eine Folge ein Vorteil, für wen eine Belastung?", [6])


def t1_a2():
    return auftrag_folie("Jetzt: Aufgabe 2 – allein", [2], {2: "erst im Heft, dann am Handy"}, "je eine Zeile Wirtschaft, Gesellschaft, Umwelt: Vorteil · Belastung · Gruppe + eine Bedingung")


def t1_a2b():
    s = d.slide("Aufgabe", "Besprechen: zwei verkürzte Aussagen")
    y = frage_klick(s, 1.05, "»Alle profitieren gleich.«", "Nein – Gruppen sind verschieden betroffen; es kommt auf Regeln und Bedingungen an.")
    y = frage_klick(s, y, "»Regional ist immer besser für die Umwelt.«", "Nein – Herstellung, Energie und Lebensdauer zählen, nicht nur Transportkilometer.")
    return s


def t1_sich():
    s = d.slide("Nur Titel", "Sicherung auf Papier")
    karte(s, X0, 1.05, W, 1.5, "Schreib einen Satz ins Heft", ["Unsere Uhr wäre besonders verwundbar, wenn …, weil …"], ORANGE, size=24)
    notiz(s, 2.8, "Ohne Handy · danach sind Aufgaben 1 und 2 fertig.")
    return s


# ---- Stunde 2
def t2_a3():
    s = auftrag_folie("Jetzt: Aufgabe 3 – allein rechnen", [3], {3: "allein, Rechenweg im Heft"}, "Zoll und Summe in US-Dollar · Zahler · zwei Wege der Belastung · Grund für den offenen Ladenpreis")
    notiz(s, 3.95, "Modell: Zollwert 100 US-Dollar · Zollsatz 15 Prozent · weitere Kosten bleiben unberücksichtigt")
    return s


def t2_a3b():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 3")
    y = frage_klick(s, 1.05, "Zoll und Summe?", "100 × 0,15 = 15 US-Dollar · 100 + 15 = 115 US-Dollar")
    y = frage_klick(s, y, "Wer zahlt zuerst – und wer trägt die Last?", "Der Importeur zahlt zuerst; die Last kann bei Marge, Preis oder Lieferant liegen – offen.")
    y = frage_klick(s, y, "Warum bleibt der Ladenpreis offen?", "Nachfrage, Verträge, Wechselkurs, weitere Kosten, Wettbewerb.", size=18)
    return s


def t2_a4():
    s = auftrag_folie("Jetzt: Aufgabe 4 – Dreiergruppen", [4], {4: "Dreiergruppe: Matrix + drei Fälle"}, "je Organisation Aufgabe · Instrument · Grenze + Fälle 1–3 zugeordnet")
    notiz(s, 3.95, "Fall 1: Streit über Handelsbeschränkung · Fall 2: Zahlungslücke ans Ausland · Fall 3: Strom oder Schulen, langfristig", size=16)
    return s


def t2_sich():
    s = d.slide("Aufgabe", "Sichern: drei Organisationen, drei Fälle")
    rows = [["", "WTO", "IWF", "Weltbank"], ["Aufgabe", "Handelsregeln, Streit", "Stabilität, Zahlungsprobleme", "Entwicklungsfinanzierung"],
            ["Grenze", "keine Weltregierung, Berufung blockiert", "Auflagen lösen nicht alles", "Schulden und Folgen prüfen"], ["Fall", "1 · Handelsstreit", "2 · Zahlungslücke", "3 · Strom, Schulen"]]
    cells, h = B.auto_grid(s, X0, 0.98, [1.4, 2.5, 2.5, 2.6], rows, size=16, minh=0.34)
    for r in cells[1:]: s._anim.append(r[1:])
    frage_klick(s, 0.98 + h + 0.12, "Wer leitet den IWF? (Namenskarte B)", "Georgieva – Lagarde war bis 2019 IWF-Chefin, jetzt EZB. Namen vor dem Termin prüfen.", size=18)
    return s


# ---- Stunde 3
def t3_uebernahme():
    s = d.slide("Nur Titel", "Vier Bedeutungen von »Übernahme«")
    bild(s, "vier_fragen.png", X0, 1.0, 4.2, 2.24)
    karte(s, 4.9, 1.0, 4.6, 2.24, "Ordne zu", ["1 · Ein Chatbot schreibt Kundenmails.", "2 · Ein Konzern kontrolliert Chips und Rechenzentren.", "3 · Ein Team plant ohne KI nicht mehr.", "4 · Ein System umgeht seine Aufsicht."], TEAL, size=16)
    frage_klick(s, 3.3, "Welches Feld passt zu 1–4?", "1 Arbeit · 2 Macht · 3 Abhängigkeit · 4 Kontrollverlust (Nr. 4 ist nur eine Möglichkeit).", size=16)
    return s


def t3_a5():
    return auftrag_folie("Jetzt: Aufgabe 5 – zu zweit", [5], {5: "zu zweit am Handy"}, "vier Fälle zugeordnet · je ein betontes Ziel von EU und USA")


def t3_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: drei Kategorien")
    for i, (kopf, txt, col) in enumerate((("Verbot", "z. B. bestimmte soziale Bewertung", RUST), ("Hochrisiko", "z. B. Bewerberauswahl", ORANGE), ("Transparenz", "z. B. Chatbot gibt sich als Mensch aus", TEAL))):
        karte(s, X0 + i * 3.05, 1.0, 2.9, 1.5, kopf, [txt], col, size=16)
    frage_klick(s, 2.7, "Ist die EU-KI-Verordnung ein KI-Verbot?", "Nein – Pflichten nach Risiko und Einsatz. Ausschließlich militärische, Verteidigungs- oder nationale Sicherheitszwecke sind nach Artikel 2 ausgenommen (bei auch ziviler Nutzung gilt die Verordnung) – kein rechtsfreier Raum.", size=18)
    return s


def t3_a6():
    s = auftrag_folie("Jetzt: Aufgabe 6 – Quellenkarten arbeitsteilig", [6], {6: "eine Karte je Gruppe, Tabelle gemeinsam"}, "Aussage – Art der Quelle – Beleg – Interesse – Grenze · 45 Sekunden Bericht je Karte")
    notiz(s, 3.95, "A: CAIS-Statement 2023 · B: AI Safety Report 2026 · C: Fallstudien 2026 · D: US-KI-Aktionsplan 2025", size=16)
    return s


def t3_a7():
    return auftrag_folie("Jetzt: Aufgabe 7 – allein", [7], {7: "allein am Handy"}, "vier Fehler begründet · zwei Sätze richtig mit Quelle · eine Schutzmaßnahme mit Grenze")


def t3_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgaben 5–7")
    y = frage_klick(s, 1.05, "Fälle 1–4 (Bewerber, Chatbot, Bewertung, Trainingsplan)?", "Hochrisiko · Transparenz · verbotene Praxis · keine besondere Einstufung", size=18)
    y = frage_klick(s, y, "Welche Karte liefert eine Messung?", "Keine allein: C zeigt einen Versuch unter Bedingungen, A und D sind Positionen, B bündelt Befunde.", size=18)
    y = frage_klick(s, y, "Eine Schutzmaßnahme – und ihre Grenze?", "z. B. menschliche Freigabe – keine Garantie gegen jeden Fehler.", size=18)
    return s


# ---- Stunde 4
def t4_rueck():
    s = d.slide("Nur Titel", "Rückblick: Sportuhr und drei Institutionen")
    for i, (kopf, col) in enumerate((("WTO", GREEN), ("IWF", TEAL), ("Weltbank", ORANGE))):
        karte(s, X0 + i * 3.05, 1.0, 2.9, 0.9, kopf, [], col, size=20)
    y = frage_klick(s, 2.05, "Handelsstreit · Zahlungskrise · Schulprojekt – wer ist zuständig?", "WTO · IWF · Weltbank", size=18)
    karte(s, X0, y + 0.05, W, 1.05, "Aktualitätshinweis", ["Die Übergangsfrist für die Kennzeichnung älterer KI-Systeme lief bis 02.12.2026 – seit zwei Tagen vorbei (Stand Karte C prüfen)."], ORANGE, size=16)
    return s


def t4_a8a():
    s = auftrag_folie("Jetzt: Aufgabe 8a – Perspektivgruppen", [8], {8: "Gruppe, dann am Handy"}, "2 Argumente · 1 Maßnahme · 1 Nachteil der eigenen Lösung", zeit=7)
    notiz(s, 3.9, "Soll der Anbieter für wichtige Bauteile und KI-Dienste mehrere Bezugsquellen aufbauen, auch wenn das die Kosten erhöht?", size=16, farbe=OLIVE)
    return s


def t4_a8b():
    s = d.slide("Aufgabe", "Aufgabe 8b: Diskussion ohne Handy · 13 min")
    y = schritte(s, X0, 1.05, W, ["Je 1 Minute Ausgangsposition pro Perspektive.", "Moderierte Rückfragen, dann der gemeinsame Zielkonflikt.", "Beobachter: ein belastbarer Zusammenhang, eine offene Behauptung."], size=20, farbe=GREEN)
    karte(s, X0, y + 0.1, W, 1.1, "Regeln", ["Argumente auf Menschenwürde, Demokratie und überprüfbare Tatsachen beziehen. Niemand muss die eigene Haltung spielen."], RUST, size=16)
    return s


def t4_a8c():
    s = d.slide("Aufgabe", "Aufgabe 8c: eigenes Urteil mit der Hand · 8 min")
    y = schritte(s, X0, 1.05, W, ["100–130 Wörter auf Papier – entscheide dich für einen Vorschlag.", "Zusammenhang aus der Lieferkette · soziale oder ökologische Folge · Grenze der Maßnahme.",
                                  "Ein Satz: »Wenn …, dann könnte …; offen bleibt …«. Danach Foto in die Aufgabe 8."], size=19, farbe=GREEN)
    notiz(s, y + 0.1, "Beide Richtungen sind erlaubt. Bewertet wird die Begründung – nicht deine politische Richtung.", size=16, farbe=RUST)
    return s


def t4_check():
    s = d.slide("Nur Titel", "Selbstcheck: sechs Quizfragen")
    schritte(s, X0, 1.05, 6.9, ["Quiz per QR-Code öffnen: genau sechs Fragen.", "Einwände und Unsicheres sofort fragen.", "Das Quiz zählt nicht für die Note."], size=20, farbe=TEAL)
    qr(s, "quizcheck", 7.75, 1.05, 1.3, "Quiz (6 Fragen)")
    return s


def t4_abgabe():
    s = d.slide("Nur Titel", "Abgabe: eine PDF in LMS")
    schritte(s, X0, 1.05, 6.9, ["Arbeitsblatt: alle Aufgaben 1–8 fertig? Dann »PDF erstellen« → in LMS hochladen.", "Kein Download? »Teilen / Speichern« oder »PDF öffnen«. Geht LMS nicht: PDF per E-Mail an Stephan.", "Fotos nicht vergessen: Aufgabe 1 (Flussbild) und Aufgabe 8c (Urteil)."], size=20, farbe=RUST)
    qr(s, "aufgaben", 7.75, 1.05, 1.3, "Arbeitsblatt")
    return s


def t4_bruecke():
    s = d.slide("Nur Titel", "Brücke zur nächsten Einheit")
    karte(s, X0, 1.05, W, 1.7, "Offene Frage", ["Wenn Regeln und Technik Macht schaffen: Was macht dann die Macht des Westens aus?"], OLIVE, size=24)
    notiz(s, 3.0, "Kein Stoff, nur die Anschlussfrage. Fertig? Reserve nutzen, nichts Neues beginnen.", size=18)
    return s


def zusatz_folie():
    s = d.slide("Nur Titel", "OPTIONAL: Für Schnelle", hidden=True)
    rows = [["Nr.", "OPTIONAL (Theorieteil, ganz unten)"]] + [[str(i + 1), it["title"].replace("OPTIONAL: ", "")] for i, it in enumerate(TD.SCHNELLE)]
    cells, h = B.auto_grid(s, X0, 1.05, [0.7, 8.3], rows, size=18, minh=0.42)
    B.tb(s, X0, 1.05 + h + 0.15, W, 0.8, ["Nur, wenn die Pflicht fertig ist. Keine Hausübung. Quiz »Globalisierung-Check« (16 Fragen) freiwillig."], size=18, after=0)
    return s


# ---------------------------------------------------------------- Ablauf je Stunde: (Schlüssel, Phasen, Art, Schritt auf »Heute«, Wozu?, Funktion)
SPEC = {
 1: [("t1_heute", [0], "START", None, "Klassenbuch; Ziel und Ablauf zeigen (QR Arbeitsblatt, Theorieteil)", lambda: heute_folie(1)),
     ("t1_einst", [1], "EINSTIEG", None, "Vorwissen: Marke ≠ Produkt – Vermutungen sammeln, noch nicht auflösen", t1_einst),
     ("t1_lesen", [2], "LESEN", "Lesen", "Begriff, Entstehung, Standortwahl selbst lesen – Stephan erklärt nicht vor",
      lambda: lesen_folie(1, "**Buch S. 43–48** zum Nachschlagen", ["verbindet", "entstehung", "warum"], "Welche Verbindungen gehen über den Warenhandel hinaus?", [2])),
     ("t1_klaeren", [3], "KURZ KLÄREN", "Kurz klären", "Vier Ströme am Bild; Globalisierung ≠ nur Warenhandel", t1_klaeren),
     ("t1_a1", [4], "ZU ZWEIT", "Aufgabe 1", "Flussbild der Sportuhr (K03-nah): Ströme, Akteure, Engpass", t1_a1),
     ("t1_a1b", [5], "BESPRECHEN", "Besprechen", "Beispielströme per Klick; Engpass besprechen", t1_a1b),
     ("t1_lesen2", [6], "LESEN", "Lesen: Folgen", "Gewinner und Belastete: selbst lesen", t1_lesen2),
     ("t1_a2", [7], "AUFGABE", "Aufgabe 2", "Folgen für Wirtschaft, Gesellschaft, Umwelt unterscheiden", t1_a2),
     ("t1_a2b", [8], "BESPRECHEN", None, "Zwei verkürzte Aussagen korrigieren", t1_a2b),
     ("t1_sich", [9, 10], "ABGABE", None, "Ein Satz auf Papier; Reserve", t1_sich)],
 2: [("t2_heute", [0, 1, 2], "TEST", None, "Klassenbuch, Test (20 min); Wiedereinstieg Modellimport; Ziel der Stunde", lambda: heute_folie(2)),
     ("t2_lesen", [3], "LESEN", "Lesen: Zölle", "Zoll als Zahlung und Last selbst lesen (mit Karte A)",
      lambda: lesen_folie(2, "**Buch S. 50–51** zum Nachschlagen · Karte A", ["zoelle"], "Wer führt den Zoll zuerst ab – und wer trägt die Last?", [3])),
     ("t2_a3", [4], "AUFGABE", "Aufgabe 3", "Modellrechnung, Zahler und Last unterscheiden", t2_a3),
     ("t2_a3b", [5], "BESPRECHEN", None, "Rechnung, Zahler, offener Ladenpreis", t2_a3b),
     ("t2_lesen2", [6], "LESEN", "Lesen: Institutionen", "WTO, IWF, Weltbank selbst lesen (mit Karte B)",
      lambda: lesen_folie(2, "**Buch S. 52–63** zum Nachschlagen · Karte B", ["institutionen"], "Welches Problem gehört zu welcher Organisation?", [6])),
     ("t2_a4", [7], "GRUPPE", "Aufgabe 4", "Matrix und drei Fälle in Dreiergruppen", t2_a4),
     ("t2_sich", [8, 9], "BESPRECHEN", None, "Je Organisation Aufgabe und Grenze sichern; Namen prüfen; Reserve", t2_sich)],
 3: [("t3_heute", [0], "START", None, "Klassenbuch; Ziel von Stunde 3", lambda: heute_folie(3)),
     ("t3_uebern", [1], "EINSTIEG", None, "Vier Bedeutungen von »Übernahme« trennen", t3_uebernahme),
     ("t3_lesen", [2], "LESEN", "Lesen: KI-Regeln", "Daten, Chips, Strom, Regeln selbst lesen (Karten C–E)",
      lambda: lesen_folie(3, "**Buch S. 48** zum Anschluss · Karten C bis E", ["ki_global"], "Welche Art von Regel gilt für welchen Einsatz?", [2])),
     ("t3_a5", [3], "ZU ZWEIT", "Aufgabe 5", "Fallkarten sortieren, EU und USA vergleichen", t3_a5),
     ("t3_klaeren", [4], "KURZ KLÄREN", "Kurz klären", "Verbot, Hochrisiko, Transparenz an je einem Beispiel", t3_klaeren),
     ("t3_lesen2", [5], "LESEN", "Lesen: Risiken", "Befund, Simulation, Szenario, Position",
      lambda: lesen_folie(3, "**Buch S. 48** zum Nachschlagen · Karte D", ["ki_risiko"], "Befund, Simulation, Szenario oder Position?", [5])),
     ("t3_a6", [6], "GRUPPE", "Aufgabe 6", "Quellenprüfung arbeitsteilig an vier Karten", t3_a6),
     ("t3_a7", [7], "AUFGABE", "Aufgabe 7", "Fehlerhaften KI-Text korrigieren", t3_a7),
     ("t3_bespr", [8, 9], "BESPRECHEN", None, "Fälle, Quellenkarten, Schutzmaßnahme; Reserve", t3_bespr)],
 4: [("t4_heute", [0], "START", None, "Klassenbuch; Ziel von Stunde 4", lambda: heute_folie(4)),
     ("t4_rueck", [1], "EINSTIEG", None, "Rückblick Sportuhr und Institutionen; Datumsbewusstsein KI-Frist", t4_rueck),
     ("t4_lesen", [2], "LESEN", "Lesen: Gestalten", "Maßnahmen und Grenzen selbst lesen",
      lambda: lesen_folie(4, "**Buch S. 65–77** zum Nachschlagen", ["gestalten"], "Wie nutzen wir die Vorteile und begrenzen Abhängigkeiten, Kosten und Risiken?", [2])),
     ("t4_a8a", [3], "GRUPPE", "Aufgabe 8a", "Vier Perspektiven bereiten Argumente und Maßnahme vor", t4_a8a),
     ("t4_a8b", [4], "BEWEGUNG", "Aufgabe 8b", "Strukturierte Diskussion ohne Handy", t4_a8b),
     ("t4_a8c", [5], "AUFGABE", "Aufgabe 8c", "Eigenes Urteil mit der Hand; Foto danach", t4_a8c),
     ("t4_check", [6], "WIEDERHOLEN", "Selbstcheck", "Sechs Quizfragen; Einwände klären", t4_check),
     ("t4_abgabe", [7], "ABGABE", "Abgabe", "PDF erstellen, in LMS hochladen", t4_abgabe),
     ("t4_bruecke", [8, 9], "EINSTIEG", None, "Brücke zur nächsten Einheit; Reserve", t4_bruecke)],
}

for teil, sp in SPEC.items():
    alle = sorted({i for x in sp for i in x[1]})
    assert alle == list(range(len(phasen(teil)))), (teil, alle)

DANACH_TEIL = {1: "Stunde 2 am Fr 20.11.: zuerst Test", 2: "Stunde 3 am Fr 27.11.: KI", 3: "Stunde 4 am Fr 04.12.: Gestalten und PDF-Abgabe",
               4: "Ende der Einheit – nächste Einheit: Macht des Westens"}

KURZ_TITEL = {"t1_einst": "Marke oder Produkt", "t1_a2b": "Besprechen", "t1_sich": "Sicherung auf Papier", "t2_a3b": "Besprechen", "t2_sich": "Sicherung", "t3_uebern": "Vier Bedeutungen",
              "t3_bespr": "Besprechen", "t4_rueck": "Rückblick", "t4_bruecke": "Brücke", "t1_lesen": "Lesen"}


def FOLIE_TITEL(spec):
    return KURZ_TITEL.get(spec[0], spec[0])


# ================================================================ Deck bauen
def bauen():
    global d
    d = B.Deck(True, "IWK · 5AK · K2 Globalisierung · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Globalisierung und aktuelle Weltpolitik")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["IWK · 5AK · K2 · Unterrichts-PPP · " + " · ".join(I.DATEN[K0][n] for n in (1, 2, 3, 4)) + " · Buch S. 41–77",
                        [(f"Stand {I.STAND} · {I.V} · TH-Unterricht (Ablauf) – zum Nachlesen: Theorieteil", {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    bedien = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    regie = {st["std"]: d.slide("Nur Titel", f"Regie {K0} · {st['datum']} · Stunde {st['std']}", hidden=True) for st in P.PLAN[K0]}
    quellen = d.slide("Nur Titel", "Lehrer-Info · Was vor dem Unterricht zu prüfen ist", hidden=True)
    for teil in (1, 2, 3, 4):
        d.section(f"Stunde {teil}")
        sec = d.slide("Abschnitt", I.TEILNAME[teil].split(" · ", 1)[1])
        for ph in sec.placeholders:
            if ph.placeholder_format.type == 2: ph.text_frame.text = I.TEILBUCH[teil] + " · " + I.wann(teil)
        FOLIE[f"t{teil}_sec"] = sec
        sp = SPEC[teil]
        for j, (key, idx, art, schritt, wozu, fn) in enumerate(sp):
            s = fn(); FOLIE[key] = s
            nxt = sp[j + 1] if j + 1 < len(sp) else None
            nn = (nxt[3] or FOLIE_TITEL(nxt)) if nxt else DANACH_TEIL[teil]
            hinweis(s, art, minuten(teil, idx), nn)
            B.pill(s, I.TEILBUCH[teil], w=2.4)
            check(s)
    d.section("Optional")
    zusatz = zusatz_folie()

    nr_von = {s.slide_id: i + 1 for i, s in enumerate(d.p.slides)}
    NR = lambda key: nr_von[FOLIE[key].slide_id]
    folgen = {t: [FOLIE[f"t{t}_sec"]] + [FOLIE[x[0]] for x in SPEC[t]] for t in (1, 2, 3, 4)}
    for st in P.PLAN[K0]:
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
        B.tb(s, X0, 0.98, W, 0.3, [[(f"{K0} · {st['datum']} · Benutzerdefinierte Präsentation »Stunde {teil} {st['datum']}« · Foliennummern gelten für diese Datei", {"bold": True, "color": RUST})]], size=10, after=0)
        kn = P.KNAPP[(K0, teil)]
        hk = B.th("Wenn es knapp wird: " + kn, 10, W, pad=0.04)
        size = 11
        while size > 8 and B.table_h([0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2) + hk > 3.95: size -= 1
        cells, h = B.auto_grid(s, X0, 1.28, [0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2)
        B.tb(s, X0, 1.3 + h, W, hk, [[("Wenn es knapp wird: ", {"bold": True, "color": RUST}), (kn, {})]], size=10, after=0)
    B.tb(bedien, X0, 0.98, W, 4.1, [
        [("Eine Datei, eine Klasse. ", {"bold": True, "color": OLIVE}), ("F5 zeigt alle sichtbaren Folien in Unterrichtsreihenfolge (Stunde 1 → 4).", {})],
        [("Pro Stunde starten: ", {"bold": True, "color": OLIVE}), ("Bildschirmpräsentation → Benutzerdefinierte Bildschirmpräsentation → z. B. »Stunde 2 Fr 20.11.«. Ohne Menü: Foliennummer tippen und Enter (Nummern auf den Regiefolien).", {})],
        [("Jede Stunde läuft gleich: ", {"bold": True, "color": OLIVE}), ("»Heute« → »Lesen: …« (genaue Abschnitte im Theorieteil, Leitfrage) → »Kurz klären« (nur Fehlvorstellungen, Antwort per Klick) → »Jetzt: Aufgabe …« → »Besprechen« (Lösung per Klick, erst nach der Arbeitszeit).", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht, was JETZT läuft (Minuten aus plan.py) und was DANACH kommt.", {})],
        [("Stunde 2: ", {"bold": True, "color": OLIVE}), ("zuerst der angekündigte Test (20 min, nicht in dieser PPP; Stoff und Nummer unbekannt).", {})],
        [("Nachschlagen: ", {"bold": True, "color": OLIVE}), ("Theorieteil bleibt vollständig; Lösungen in der privaten Lösungsmappe. OPTIONAL: ausgeblendete Folie am Ende.", {})],
        [("Regiepläne: ", {"bold": True, "color": OLIVE}), (f"Folien {nr_von[regie[1].slide_id]}–{nr_von[regie[4].slide_id]} (ausgeblendet), Präsentation »Lehrer-Regiepläne«.", {})]],
        size=13, after=5)
    B.tb(quellen, X0, 0.98, W, 4.1, ["· " + x for x in [
        "Zollfolien (Stunde 2) zeigen nur das Rechenmodell; der Rechtsstand wechselt: Supreme Court 20.02.2026 (IEEPA-Zölle gekippt), Section 232/301 gelten weiter. Vor dem 20.11. Karte A neu prüfen.",
        "Namenskarte B: Georgieva (IWF), Banga (Weltbank), Okonjo-Iweala (WTO). Lagardes Abgang zum 07.02.2027 ist laut Reuters/Börsen-Zeitung (Stand 29.10.2026) gemeldet, Primärquelle prüfen; auf den Folien steht er nicht.",
        "KI-Fristen (Karte C) nach AI Omnibus: 02.08.2026 Transparenz, 02.12.2027 Anhang III, 02.08.2028 Anhang I; Übergangsfrist Kennzeichnung ältere Systeme bis 02.12.2026.",
        "Karte C der Quellenprüfung stammt von Anthropic (Hersteller von Claude): Interessenkonflikt offen ansprechen – gehört zu Aufgabe 6.",
        "Keine Buchbilder auf den Folien (frei weitergebbar); keine Podcasts im Pflichtablauf; Aufgabe 8 ohne Rollentribunal.",
        "Geprüft: in LibreOffice gerendert und alle Folien angesehen. Ein Abspieltest in Microsoft PowerPoint (Klicks, benutzerdefinierte Präsentationen) steht aus."]], size=13, after=5)

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

    show(f"{K0} gesamt", [titel] + sum([folgen[t] for t in (1, 2, 3, 4)], []))
    for st in P.PLAN[K0]:
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
