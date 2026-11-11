"""Unterrichts-PPP K2.1 Globalisierung (TH-Unterricht, 5AK IWK) – die kurze, geführte PPP für den Frontalunterricht im Saal.
Nach »bhak-ppp-gestaltung«: Lesestopps mit exaktem Abschnittstitel und QR, »KURZ KLÄREN« mit Grafik und Klick-Antwort, alle Pflichtaufgaben 1–3 mit Zeit und erwartetem Ergebnis,
Regie je Stunde als ausgeblendete Tabelle (Minute · Was läuft · Folie · Wozu, aus plan.py), Phasenhinweis unten links, benutzerdefinierte Präsentationen je Stunde,
»Aufgabe n«, »Buch S.«, keine Buchbilder. Alle Minuten kommen aus plan.py. Der Test in Stunde 2 (20 min, Dauer angenommen) ist nicht Teil dieser PPP.
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


def notiz(s, y, txt, size=16, farbe=None, w=None):
    B.tb(s, X0, y, w or W, 0.5, [[(txt, {})]], size=size, color=farbe or INK, after=0)


# ---- Stunde 1
def t1_einst():
    s = d.slide("Nur Titel", "Was verbindest du mit Globalisierung?")
    karte(s, X0, 1.0, 4.3, 1.5, "An die Tafel (Buch S. 42)", ["Sammelt Begriffe, die ihr mit Globalisierung verbindet. Je ein Begriff pro Zuruf."], GREEN, size=18)
    karte(s, X0 + 4.5, 1.0, 4.5, 2.6, "Vermutung per Handzeichen: Wann begann sie?",
          ["1 · um 1492 (Kolumbus)", "2 · um 1844 (Telegraf)", "3 · um 1944 (IWF, Weltbank)", "4 · erst 1980er/1990er (Technik, Internet)", "5 · je nach Kriterium früher oder später"], ORANGE, size=16)
    notiz(s, 3.75, "Noch nicht auflösen – am Arbeitsblatt tippt jeder zuerst allein (»Was glaubst du?«).", size=16, farbe=RUST)
    return s


def t1_a1():
    s = auftrag_folie("Jetzt: Aufgabe 1 – Wann begann sie?", [1], {1: "allein am Handy, ohne KI"},
                      "Tipp (ohne Wertung) · drei Ereignisse mit Jahr · 452 Jahre · passende Aussage · eigener Beginn mit Begründung",
                      ohne_handy=None)
    notiz(s, 3.95, "Tipps auf Abruf unter der Aufgabe: Denkanstoß · Theorie-Karte · Buch.", size=16)
    return s


def t1_a1b():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 1 – der Zeitstrahl")
    bild(s, "zeitstrahl.png", X0, 1.0, 4.4, 2.15)
    y = frage_klick(s, 1.0, "Gibt es einen einzigen Beginn?", "Nein – je nach Kriterium: 1492, 1844, 1944, 1980er, Internet.", w=4.4, x=5.1, size=17)
    y = frage_klick(s, y, "1944 − 1492 = ?", "452 Jahre.", w=4.4, x=5.1, size=17)
    notiz(s, 3.3, "Zwei, drei Kadetten nennen ihr Kriterium – ohne Wertung (Aufgabe 1 e).", size=16)
    return s


def t1_china():
    s = d.slide("Nur Titel", "Gemeinsam: Folgen für die Weltgeschichte?")
    karte(s, X0, 1.0, W, 0.95, "Überschrift aus dem Vorjahr", ["»Vor 500 Jahren zerstörte China seine Marine, weil die Herrscher Angst vor Freihandel hatten.«"], ORANGE, size=18)
    y = frage_klick(s, 2.05, "Quellenkritik: Was ist gesichert?", "Die staatlichen Flottenfahrten unter Zheng He (1405–1433) endeten. »Zerstört« und »Angst vor Freihandel« sind Deutungen.", size=17)
    y = frage_klick(s, y, "Gedankenspiel (kein Fakt): Wäre China weitergesegelt?", "Offen – Vermutungen sammeln: Handelszentrum Asien? Kolonien? Rolle Europas?", size=17)
    return s


def t1_lesen2():
    return lesen_folie(1, "**Buch S. 45–47** zum Nachschlagen", ["antrieb", "liberal"], "Welche sechs Kräfte treiben die Globalisierung an – und was heißt Liberalisierung?", [5])


def t1_a2():
    return auftrag_folie("Jetzt: Aufgabe 2 – Antriebskräfte", [2], {2: "allein am Handy, ohne KI"}, "vier Beispiele zugeordnet · Liberalisierung in eigenen Worten · ein Bezug zu einem anderen Prozess")


def t1_a2b():
    s = d.slide("Aufgabe", "Besprechen: Antriebskräfte und Liberalisierung")
    bild(s, "antriebskraefte.png", X0, 1.0, 4.2, 2.43)
    y = frage_klick(s, 1.0, "Konzern auf drei Kontinenten?", "Transnationale Konzerne", w=4.5, x=5.0, size=16)
    y = frage_klick(s, y, "Zölle senken, Märkte öffnen?", "Liberalisierung", w=4.5, x=5.0, size=16)
    y = frage_klick(s, y, "Container, Großraumflugzeuge?", "Innovationen im Transport", w=4.5, x=5.0, size=16)
    y = frage_klick(s, y, "Gleiche Stecker und Schienen?", "Normen und Standards", w=4.5, x=5.0, size=16)
    notiz(s, 3.5, "Liberalisierung = Handelshemmnisse abbauen, Märkte öffnen. Neoliberalismus: Befürworter und Kritiker kennen (Buch S. 46–47).", size=12, w=4.3)
    return s


def t1_sich():
    s = d.slide("Nur Titel", "Sicherung ins Heft")
    karte(s, X0, 1.05, W, 1.5, "Merksatz", ["Es gibt keinen einzelnen Beginn der Globalisierung – und sechs Kräfte treiben sie an."], ORANGE, size=22)
    notiz(s, 2.8, "Ohne Handy · danach sind Aufgaben 1 und 2 fertig. Ausblick: Fr 20.11. zuerst der angekündigte Test, danach Digitalisierung (Buch S. 48).", size=16)
    return s


# ---- Stunde 2
def t2_wdn():
    s = d.slide("Nur Titel", "Weißt du noch? Drei Fragen aus Stunde 1")
    y = 1.0
    for q, a in I.WEISST_DU_NOCH[2]:
        y = frage_klick(s, y, q, a, size=17)
    return s


def t2_a3():
    s = auftrag_folie("Jetzt: Aufgabe 3 – Digital Divide", [3], {3: "allein am Handy, ohne KI"}, "71 und 27 Prozentpunkte · 2,2 Mrd. offline · Grund für verschiedene Zahlen · ein Lebensbereich")
    notiz(s, 3.95, "ITU 2025: hohes Einkommen 94 % · niedriges 23 % · Stadt 85 % · Land 58 % · Männer 77 % · Frauen 71 %", size=16)
    return s


def t2_a3b():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 3")
    bild(s, "digital_divide.png", X0, 1.0, 3.9, 2.25)
    y = frage_klick(s, 1.0, "Hoch − niedrig? Stadt − Land?", "94 − 23 = 71 · 85 − 58 = 27 Prozentpunkte", w=4.9, x=4.6, size=15)
    y = frage_klick(s, y, "Buch: rund 32 %. ITU: 2,2 Mrd. offline.", "Quellen zählen verschieden: Jahr, Messweise, Definition. Quelle nennen.", w=4.9, x=4.6, size=15)
    y = frage_klick(s, y, "Corona und Digitalisierung?", "Homeoffice und Distance Learning beschleunigt – Ungleichheit sichtbar.", w=4.9, x=4.6, size=15)
    return s


def t2_ampel():
    s = d.slide("Nur Titel", "Statement-Ampel im Raum – ohne Handy")
    for i, (kopf, col) in enumerate((("stimmt", GREEN), ("unklar", ORANGE), ("stimmt nicht", RUST))):
        karte(s, X0 + i * 3.05, 1.0, 2.9, 0.8, kopf, [], col, size=20)
    y = schritte(s, X0, 1.95, W, ["Stephan liest eine Aussage vor. Alle stellen sich in eine Zone.", "Gruppen prüfen mit den vier Fragen: Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere?",
                                  "Neu aufstellen. Wer wechselt, sagt in einem Satz warum. Keine Note."], size=16, farbe=GREEN)
    return s


def t2_ampel2():
    s = d.slide("Nur Titel", "Aussagen zur Ampel (Buch S. 51)")
    karte(s, X0, 1.0, 4.4, 1.55, "Aussage 1", ["Globalisierung ist eine Bereicherung für Europa."], GREEN, size=18)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.55, "Aussage 4", ["Die Schäden des US-Handelskriegs zeigen, wie eng die Weltwirtschaft verflochten ist."], GREEN, size=18)
    frage_klick(s, 2.7, "Hilfe zu Aussage 4 (Stand 09.11.2026)", "China setzt den Zusatzzoll von 24 % auf US-Waren für weitere zwei Monate aus, 10 % bleiben (Berliner Zeitung, nach Xinhua, Reuters, dpa). Heißt das »Krieg vorbei«? Offen.", size=15)
    return s


def t2_abgabe():
    s = d.slide("Nur Titel", "Abgabe: eine PDF in LMS")
    schritte(s, X0, 1.05, 6.9, ["Arbeitsblatt: Aufgaben 1–3 fertig? Dann »PDF erstellen« → in LMS hochladen.", "Kein Download? »Teilen / Speichern« oder »PDF öffnen«. Geht LMS nicht: PDF per E-Mail an Stephan.",
                                "Wer fertig ist: Selbstcheck-Quiz (6 Fragen) oder Zusatzaufgaben 4–6."], size=18, farbe=RUST)
    qr(s, "aufgaben", 7.75, 1.05, 1.2, "Arbeitsblatt")
    qr(s, "quizcheck", 7.75, 2.75, 1.2, "Quiz (6 Fragen)")
    return s


def zusatz_folie():
    s = d.slide("Nur Titel", "ZUSATZ: Für Schnelle", hidden=True)
    rows = [["Nr.", "Zusatzaufgabe (Arbeitsblatt, ganz unten)", "Zeit"]] + [[str(n), T[n]["title"], f"{T[n]['zeit']} min"] for n in I.ZUSATZ]
    cells, h = B.auto_grid(s, X0, 1.05, [0.7, 7.0, 1.3], rows, size=18, minh=0.42)
    B.tb(s, X0, 1.05 + h + 0.15, W, 0.8, ["Nur, wenn die Pflicht fertig ist. Keine Hausübung. Quiz »Globalisierung-Check« (16 Fragen) freiwillig."], size=18, after=0)
    return s


def kuerzung_folie():
    s = d.slide("Nur Titel", "Lehrer-Info · Kürzungsliste und Supplierstunde", hidden=True)
    B.tb(s, X0, 0.98, W, 4.0, [[("Wenn Zeit verloren geht, in dieser Reihenfolge:", {"bold": True, "color": OLIVE})]] + ["· " + x for x in P.KUERZUNG] + [[(P.SUPPLIER, {"bold": True, "color": RUST})]], size=13, after=5)
    return s


# ---------------------------------------------------------------- Ablauf je Stunde: (Schlüssel, Phasen, Art, Schritt auf »Heute«, Wozu?, Funktion)
SPEC = {
 1: [("t1_heute", [0], "START", None, "Klassenbuch; Ziel und Ablauf zeigen (QR Arbeitsblatt, Theorieteil)", lambda: heute_folie(1)),
     ("t1_einst", [1], "EINSTIEG", None, "Begriffe sammeln (Buch S. 42); Vermutung zum Beginn per Handzeichen, noch nicht auflösen", t1_einst),
     ("t1_lesen", [2], "LESEN", "Lesen", "Theorie-Karte und Buch S. 43–44 selbst lesen – Stephan erklärt nicht vor",
      lambda: lesen_folie(1, "**Buch S. 43–44** zum Nachschlagen", ["beginn"], "Wann begann die Globalisierung – und nach welchem Kriterium?", [2])),
     ("t1_a1", [3], "AUFGABE", "Aufgabe 1", "Beginn der Globalisierung: Tipp, drei Ereignisse, Rechnung, Begründung", t1_a1),
     ("t1_a1b", [4], "BESPRECHEN", "Besprechen", "Zeitstrahl, Kriterien; Lösungen per Klick", t1_a1b),
     ("t1_china", [4], "BESPRECHEN", "Gemeinsam", "Quellenkritik an einer Überschrift; Gedankenspiel China-Flotte", t1_china),
     ("t1_lesen2", [5], "LESEN", "Lesen: Antriebskräfte", "Sechs Antriebskräfte und Liberalisierung selbst lesen",
      t1_lesen2),
     ("t1_a2", [6], "AUFGABE", "Aufgabe 2", "Vier Beispiele zuordnen, Liberalisierung erklären", t1_a2),
     ("t1_a2b", [7], "BESPRECHEN", None, "Zuordnung per Klick; Liberalisierung an der Tafel", t1_a2b),
     ("t1_sich", [8, 9], "ABGABE", None, "Merksatz ins Heft; Ausblick Stunde 2; Reserve", t1_sich)],
 2: [("t2_heute", [0, 1], "TEST", None, "Klassenbuch, Test (20 min, Dauer angenommen); Ziel der Stunde", lambda: heute_folie(2)),
     ("t2_wdn", [2], "WIEDERHOLEN", None, "Drei Fragen aus Stunde 1, mündlich", t2_wdn),
     ("t2_lesen", [3], "LESEN", "Lesen: Digital Divide", "Theorie-Karte und Buch S. 48 selbst lesen",
      lambda: lesen_folie(2, "**Buch S. 48** zum Nachschlagen", ["digital"], "Wer ist offline – und warum zählen Quellen verschieden?", [3])),
     ("t2_a3", [4], "AUFGABE", "Aufgabe 3", "ITU-Zahlen auswerten, Quellenkritik", t2_a3),
     ("t2_a3b", [5], "BESPRECHEN", None, "Zahlen, Buch gegen ITU, Corona", t2_a3b),
     ("t2_ampel", [6], "BEWEGUNG", "Ampel", "Statement-Ampel im Raum: so läuft sie", t2_ampel),
     ("t2_ampel2", [6], "BEWEGUNG", None, "Zwei Aussagen (Buch S. 51); Hilfe zu Aussage 4 mit Stand 09.11.2026", t2_ampel2),
     ("t2_abgabe", [7, 8], "ABGABE", "Abgabe", "PDF erstellen, in LMS hochladen; Reserve: Selbstcheck-Quiz", t2_abgabe)],
}

for teil, sp in SPEC.items():
    alle = sorted({i for x in sp for i in x[1]})
    assert alle == list(range(len(phasen(teil)))), (teil, alle)

DANACH_TEIL = {1: "Stunde 2 am Fr 20.11.: zuerst Test", 2: "Fr 27.11.: Institutionen der Globalisierung (WTO, IWF, Weltbank)"}

KURZ_TITEL = {"t1_einst": "Begriffe und Vermutung", "t1_a1b": "Besprechen", "t1_china": "Gemeinsam", "t1_sich": "Sicherung ins Heft", "t2_wdn": "Weißt du noch?",
              "t2_a3b": "Besprechen", "t2_ampel2": "Aussagen", "t1_a2b": "Besprechen", "t1_lesen": "Lesen"}


def FOLIE_TITEL(spec):
    return KURZ_TITEL.get(spec[0], spec[0])


# ================================================================ Deck bauen
def bauen():
    global d
    d = B.Deck(True, "IWK · 5AK · K2.1 Globalisierung · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Die Welt ohne Grenzen: Globalisierung")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["IWK · 5AK · K2.1 · Unterrichts-PPP · " + " · ".join(I.DATEN[K0][n] for n in (1, 2)) + " · Buch S. 42–51",
                        [(f"Stand {I.STAND} · {I.V} · TH-Unterricht (Ablauf) – zum Nachlesen: Theorieteil", {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    bedien = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    regie = {st["std"]: d.slide("Nur Titel", f"Regie {K0} · {st['datum']} · Stunde {st['std']}", hidden=True) for st in P.PLAN[K0]}
    quellen = d.slide("Nur Titel", "Lehrer-Info · Was vor dem Unterricht zu prüfen ist", hidden=True)
    kuerz = kuerzung_folie()
    for teil in (1, 2):
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
    d.section("Zusatz")
    zusatz = zusatz_folie()

    nr_von = {s.slide_id: i + 1 for i, s in enumerate(d.p.slides)}
    NR = lambda key: nr_von[FOLIE[key].slide_id]
    folgen = {t: [FOLIE[f"t{t}_sec"]] + [FOLIE[x[0]] for x in SPEC[t]] for t in (1, 2)}
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
        [("Eine Datei, eine Klasse. ", {"bold": True, "color": OLIVE}), ("F5 zeigt alle sichtbaren Folien in Unterrichtsreihenfolge (Stunde 1 → 2).", {})],
        [("Pro Stunde starten: ", {"bold": True, "color": OLIVE}), ("Bildschirmpräsentation → Benutzerdefinierte Bildschirmpräsentation → z. B. »Stunde 2 Fr 20.11.«. Ohne Menü: Foliennummer tippen und Enter (Nummern auf den Regiefolien).", {})],
        [("Jede Stunde läuft gleich: ", {"bold": True, "color": OLIVE}), ("»Heute« → »Lesen« (Theorie-Karte, Buch) → »Jetzt: Aufgabe …« → »Besprechen« (Lösung per Klick, erst nach der Arbeitszeit). Dazwischen Gemeinsam-Folien (Tafel, Ampel).", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht, was JETZT läuft (Minuten aus plan.py) und was DANACH kommt.", {})],
        [("Stunde 2: ", {"bold": True, "color": OLIVE}), ("zuerst der angekündigte Test (20 min angenommen, nicht in dieser PPP; Stoff und Nummer unbekannt).", {})],
        [("Aufgaben am Handy: ", {"bold": True, "color": OLIVE}), ("Tipp-Stufen unter jeder Aufgabe (Denkanstoß, Theorie-Karte, Buch). KI-Regel: jede Aufgabe sagt »ohne KI« oder »KI erlaubt«.", {})],
        [("Regiepläne: ", {"bold": True, "color": OLIVE}), (f"Folien {nr_von[regie[1].slide_id]}–{nr_von[regie[2].slide_id]} (ausgeblendet), Präsentation »Lehrer-Regiepläne«.", {})]],
        size=13, after=5)
    B.tb(quellen, X0, 0.98, W, 4.1, ["· " + x for x in [
        "Zölle: Berliner Zeitung 09.11.2026 (Anika Schlünz, nach Xinhua/Reuters/dpa): China setzt 24 % Zusatzzoll für zwei Monate aus, 10 % bleiben. Supreme Court 20.02.2026 (WKO, 23.10.2026). Ein Trump-Xi-Treffen am Rand des APEC-Gipfels in Shenzhen wurde angekündigt, Ergebnis ungeprüft – vor dem 20.11. neu prüfen.",
        "Digital Divide: ITU Facts and Figures 2025 (17.11.2025). Buch nennt rund 32 % – bewusst als Quellenkritik. Beispielländer aus deiner PPP vom Vorjahr (Stand 2024) sind nicht geprüft und stehen nicht auf den Folien.",
        "China-Flotte: EBSCO Research Starter (Zheng He, 1405–1433). Überschrift »zerstörte« als zugespitzt behandeln; Szenarien sind Gedankenspiel.",
        "Jahresplan E3 nennt Ö1 Dimensionen »Zölle: Regulierungsinstrument oder Konfliktpotenzial …« (24 min, 2025) und radioWissen »Globalisierung um das Jahr 1000« – nicht geprüft, nicht eingebaut; du entscheidest.",
        "Keine Buchbilder auf Folien und Seiten (deine PPP enthält Buchseiten, Wikipedia-Bilder, Kartenausschnitte: nicht übernommen). Grafiken selbst gezeichnet.",
        "Geprüft: in LibreOffice gerendert. Ein Abspieltest in Microsoft PowerPoint (Klicks, benutzerdefinierte Präsentationen) steht aus."]], size=12, after=5)

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

    show(f"{K0} gesamt", [titel] + sum([folgen[t] for t in (1, 2)], []))
    for st in P.PLAN[K0]:
        show(f"Stunde {st['std']} {st['datum']}", ([titel] if st["std"] == 1 else []) + folgen[st["std"]])
    show("Lehrer-Regiepläne", [bedien] + [regie[n] for n in (1, 2)] + [quellen, kuerz])
    show("Zusatz: Für Schnelle", [zusatz])

    os.makedirs(ZIEL, exist_ok=True)
    name = f"{I.PRAEFIX}-TH-Unterricht-{I.V}.pptx"
    d.save(os.path.join(ZIEL, name))
    sicht = [s for s in d.p.slides if s._element.get("show") != "0"]
    for x in PROBLEME: print("ÜBERLAUF", x)
    print("ok", name, len(d.p.slides._sldIdLst), "Folien,", len(sicht), "sichtbar ·", nid[0], "Präsentationen")
    for t in (1, 2): print("  Stunde", t, "Folien", [nr_von[x.slide_id] for x in folgen[t]])


if __name__ == "__main__":
    bauen()
