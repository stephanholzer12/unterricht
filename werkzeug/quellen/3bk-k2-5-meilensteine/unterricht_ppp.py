"""Unterrichts-PPP PBGW 3BK · Meilensteine (TH-Unterricht) – die kurze, geführte PPP für den Frontalunterricht im Saal.
Neu gebaut nach »bhak-ppp-gestaltung« 10–14 (der ChatGPT-Auftrag enthielt keine fertige Unterrichts-PPP): Lesestopps mit exaktem Abschnittstitel und QR, »KURZ KLÄREN« mit Grafik und Klick-Antwort,
alle Pflichtaufgaben 1–8 mit Zeit und erwartetem Ergebnis, Regie je Stunde als Tabelle Minute · Was läuft · Folie · Wozu (aus plan.py), Phasenhinweis unten links,
benutzerdefinierte Präsentationen je Stunde, keine Buchbilder, nur eigene Grafiken. Alle Minuten kommen aus plan.py.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/3bk-k2-5-meilensteine/unterricht_ppp.py <BHAK_Folienmaster_Vorlage.pptx> <Zielordner>"""
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
def phasen(teil, k="3BK"):
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
                B.tb(s, X0 + col * 3.6 + 0.48, yy, 3.1, hh, [it], size=18, after=0); yy += max(0.42 if len(items) >= 7 else 0.5, hh + 0.02)
    qr(s, "aufgaben", 7.75, 1.36, 1.05, "Arbeitsblatt")
    qr(s, "theorie", 7.75, 2.85, 1.05, "Theorieteil")
    return s


def lesen_folie(teil, buch, abschnitte, leitfrage, idx):
    titel = "Lesen: " + (TITEL[abschnitte[0]] if len(abschnitte) == 1 else f"Theorieteil Teil {teil}")
    if len(titel) > 40: titel = f"Lesen: Theorieteil Teil {teil}"
    s = d.slide("Nur Titel", titel)
    y = 1.05
    if buch:
        bh = max(0.5, B.th(buch, 20, W - 0.95, pad=0.1))
        c = B.box(s, X0, y, W, bh, fill=CARD, line=OLIVE, lw=1.5)
        ic = B.box(s, X0 + 0.1, y + bh / 2 - 0.27, 0.62, 0.54, fill=OLIVE)
        B.text(ic, [[("BUCH", {"size": 12, "bold": True, "color": WHITE})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
        B.tb(s, X0 + 0.82, y, W - 0.9, bh, [buch], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0); y += bh + 0.06
    B.tb(s, X0, y, 6.9, 0.36, [[("Im Theorieteil genau diese Abschnitte:", {"bold": True, "color": TEAL})]], size=18, after=0); y += 0.36
    for a in abschnitte:
        hh = max(0.42, B.th("»" + TITEL[a] + "«", 20, 6.4, True, pad=0.1))
        c = B.box(s, X0, y, 6.9, hh, fill=RGBColor.from_string("E8F1F3"), line=TEAL, lw=1.25)
        B.text(c, [[("»" + TITEL[a] + "«", {"bold": True})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0); y += hh + 0.04
    qr(s, "theorie", 7.75, 1.05 + (bh + 0.06 if buch else 0), 1.2, "Theorieteil")
    y += 0.04
    hq = B.th("Leitfrage: " + leitfrage, 20, W - 0.1, pad=0.2)
    c = B.box(s, X0, y, W, hq, fill=RGBColor.from_string("FFF4EA"), line=ORANGE, lw=1.5)
    B.text(c, [[("Leitfrage: ", {"bold": True, "color": ORANGE}), (leitfrage, {})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return s


def auftrag_folie(titel, nrs, tun, erwartet, ohne_handy=False, layout="Aufgabe", zeiten=None):
    """Arbeitsphase: welche Aufgaben, was genau tun, wie lange, was am Ende dastehen soll."""
    s = d.slide(layout, titel)
    rows = [["Nr.", "Aufgabe", "Zeit", "So arbeitest du"]]
    for n in nrs:
        rows.append([str(n), T[n]["title"], f"{(zeiten or {}).get(n, T[n]['zeit'])} min", tun.get(n, "allein am Handy")])
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
HEUTE_ZIEL = I.HEUTE_ZIEL
GR = RGBColor.from_string("FFFFFF")


def bild(s, name, x, y, w, h):
    B.picture(s, UNIT + "img/" + name, x, y, w, h)


def tabelle_klick(s, rows, colw, size=16, y=0.98):
    cells, h = B.auto_grid(s, X0, y, colw, rows, size=size, minh=0.3)
    for r in cells[1:]: s._anim.append(r[1:])
    return cells, h


# ---- Stunde 1
def t1_einstieg():
    s = d.slide("Nur Titel", "Ein Beil verrät mehr, als man denkt")
    bild(s, "beil.png", X0, 1.0, 5.2, 3.3)
    karte(s, 5.9, 1.0, 3.6, 3.3, "Mündlich, 3 min", ["Was lässt sich **feststellen**?", "Was ist eine **begründete Vermutung**?", "Was lässt sich **nicht** belegen?"], TEAL, size=18)
    return s


def t1_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: Befund, Deutung, Staat?")
    karte(s, X0, 1.0, 4.4, 1.5, "Befund", ["was man **feststellen** kann: Kupferklinge im Holzschaft"], OLIVE, size=18)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.5, "Deutung", ["was man **begründet** daraus schließt – und was offen bleibt"], TEAL, size=18)
    y = frage_klick(s, 2.7, "Warum führt Landwirtschaft nicht zwangsläufig zu einem Staat?", "Handel, Konflikte, Religion und die örtlichen Bedingungen wirken mit – es gibt keinen Automatismus.", size=18)
    return s


def t1_a1():
    return auftrag_folie("Jetzt: Aufgabe 1 – am Mini-Whiteboard", [1], {1: "zu zweit am Mini-Whiteboard, dann eintragen"},
                         "Stichworte zu Befund · Vermutung · Grenze (Beruf, Rang oder Reise ist nicht belegt)", ohne_handy="Erst am Mini-Whiteboard, dann eintragen.")


def t1_a2():
    return auftrag_folie("Jetzt: Aufgabe 2 – zu zweit", [2], {2: "zu zweit am Handy"}, "3 Sätze »kann …, weil …« · 1 neues Problem · 1–2 Sätze: warum nicht zwangsläufig ein Staat")


def t1_a2_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 2")
    y = frage_klick(s, 1.05, "Nenne einen Zusammenhang mit »kann …, weil …«.", "z. B. Vorräte können Spezialisierung unterstützen, weil nicht mehr jeder ständig Nahrung beschaffen muss.")
    y = frage_klick(s, y, "Ein neues Problem durch Vorräte?", "Missernte, Krankheiten im engen Zusammenleben, ungleiche Verteilung – Streit.")
    return s


def t1_karte():
    s = d.slide("Nur Titel", "Orientierung: Nil, Euphrat und Tigris")
    bild(s, "karte.png", 1.5, 0.98, 4.9, 3.5)
    karte(s, 6.55, 1.0, 2.95, 3.4, "Schema", ["Karte ist **nicht maßstabsgerecht**.", "Städte: Memphis, Theben, Uruk, Babylon, Ur"], TEAL, size=18)
    return s


def t1_a3():
    return auftrag_folie("Jetzt: Aufgabe 3 – zu zweit", [3], {3: "zu zweit am Handy"}, "8 Zuordnungen · gemeinsame Aufgabe · ein Unterschied · warum ein Fluss allein keinen Staat erklärt")


def t1_a3_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 3 – die Tabelle")
    tabelle_klick(s, [["Kriterium", "Stadtstaat Mesopotamien", "Flächenkönigtum Ägypten"]] + [r for r in I.T[2]["tab"][1:]], [2.8, 3.1, 3.1])
    return s


def t1_a8():
    return auftrag_folie("Jetzt: Aufgabe 8, Teil 1 – Zeitstrahl", [8], {8: "Karten 1–4 legen, dann Schlusssatz"}, "Karten 1–4 im richtigen Zeitbereich · 1 Satz: Was haben Landwirtschaft, Metall, Schrift und Städte mit Organisation und Herrschaft zu tun?",
                         zeiten={8: 4})


def t1_pc():
    s = d.slide("Nur Titel", "Reserve: Partnercheck mit Karten")
    schritte(s, X0, 1.05, 6.6, ["A zieht 3–4 Karten (Theorieteil »Partnercheck«) und liest vor.", "B antwortet, A vergleicht und hakt ab.", "Tauschen. Handy nur für die Karten – dann weg."], size=20, farbe=TEAL)
    qr(s, "theorie", 7.75, 1.05, 1.2, "Theorieteil")
    return s


# ---- Stunde 2
def t2_einstieg():
    s = d.slide("Nur Titel", "Ein Damm bricht – wer trägt die Folgen?")
    karte(s, X0, 1.0, W, 1.2, "Lage", ["Ein Damm wurde nicht instand gehalten. Das Wasser steht auf den Feldern der Nachbarn."], ORANGE)
    frage_klick(s, 2.4, "Wer sollte die Folgen tragen – und wer entscheidet darüber?", "Eine Gemeinschaft braucht Regeln zur Zuständigkeit. Genau das regelt § 53 bei Hammurabi.")
    return s


def t2_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: Wenn-dann und Aussagegrenze")
    karte(s, X0, 1.0, 4.4, 1.4, "Wenn – dann", ["»**Wenn** … geschieht, **dann** folgt …« – so sind viele Regeln gebaut."], OLIVE, size=18)
    karte(s, X0 + 4.6, 1.0, 4.4, 1.4, "Arbeitsfassung", ["sprachlich **vereinfacht** nach Buch S. 40, kein wörtliches Zitat"], TEAL, size=18)
    y = frage_klick(s, 2.55, "Zeigt die Sammlung den Rechtsalltag?", "Nein – sie zeigt, welche Konflikte geordnet werden sollten und wie der König seine Ordnung darstellte. Wie jeder Fall wirklich entschieden wurde, wissen wir nicht.", size=18)
    return s


def t2_text():
    s = d.slide("Aufgabe", "Aufgabe 4: Arbeitsfassung der Rechtssammlung")
    rows = [["§", "Arbeitsfassung (vereinfacht)"]] + I.T[3]["tab"][1:]
    B.auto_grid(s, X0, 0.98, [0.7, 8.3], rows, size=16, minh=0.3)
    return s


def t2_a4():
    return auftrag_folie("Jetzt: Aufgabe 4 – zu zweit am Paragrafenblatt", [4], {4: "zu zweit, Papier, markieren"}, "a) Problem § 53 · b) drei Rechtsfolgen · c) was entscheidet · d) Eigentum · e) Regel ≠ Gleichheit · f) Grenze der Quelle",
                         ohne_handy="Erst auf dem Papier markieren, dann eintippen.")


def t2_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 4")
    y = frage_klick(s, 1.0, "Was entscheidet bei § 196, 198 und 199 über die Folge?", "Der gesellschaftliche Stand des Opfers.", size=18)
    y = frage_klick(s, y, "Belege den Schutz von Eigentum.", "z. B. § 53 (Getreide ersetzen), § 233 (Wand neu bauen), § 199 (Zahlung an den Besitzer).", size=18)
    y = frage_klick(s, y, "Ergänze: »Die Sammlung zeigt …; ob …, können wir aus ihr allein nicht feststellen.«", "… eine hierarchische Gesellschaft und geordnete Konflikte; ob jeder Fall im Alltag so entschieden wurde.", size=18)
    return s


def t2_sich():
    s = d.slide("Nur Titel", "Stopp – kannst du das?")
    y = 1.05
    for q, a in I.STOPPFRAGEN[2]: y = frage_klick(s, y, q, a, size=20)
    return s


# ---- Stunde 3
def t3_wdn():
    s = d.slide("Nur Titel", "Weißt du noch?")
    y = 1.0
    for q, a in I.WEISST_DU_NOCH[3]: y = frage_klick(s, y, q, a, size=18)
    return s


def t3_klaeren():
    s = d.slide("Nur Titel", "Kurz klären: Los, Wahl und »Volk«")
    bild(s, "athen.png", X0, 0.98, 4.7, 3.3)
    y = frage_klick(s, 1.0, "Los oder Wahl: Strategen?", "Gewählt. Rat und Archonten wurden gelost.", w=4.2, x=5.3, size=18)
    y = frage_klick(s, y, "Wer gehörte zum »Volk«?", "Nur erwachsene männliche Bürger.", w=4.2, x=5.3, size=18)
    return s


def t3_a5():
    return auftrag_folie("Jetzt: Aufgabe 5 – zu zweit", [5], {5: "zu zweit am Schaubild"}, "Einrichtung · Los/Wahl · drei Gruppen ohne Mitbestimmung · Vergleich mit Österreich · Urteilssatz")


def t3_skala():
    s = d.slide("Nur Titel", "Aufstellen: Wie demokratisch war Athen?")
    c = B.box(s, X0, 1.05, W, 0.9, fill=RGBColor.from_string("F6E3DF"), line=RUST, lw=2)
    B.text(c, [[("0 = gar nicht · 10 = vollständig – nach heutigen Maßstäben", {"bold": True, "color": RUST})]], size=22, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    B.box(s, X0 + 0.3, 2.35, W - 0.6, 0.22, fill=ORANGE)
    B.tb(s, X0, 2.65, 3.2, 0.4, ["0 gar nicht"], size=18, bold=True, after=0)
    B.tb(s, X0 + W - 3.2, 2.65, 3.2, 0.4, ["10 vollständig"], size=18, bold=True, align=PP_ALIGN.RIGHT, after=0)
    B.tb(s, X0, 3.2, W, 0.9, ["Stell dich im Raum auf die Linie. Zwei von euch sagen, warum – für Bürger und für Ausgeschlossene."], size=20, after=0)
    return s


def t3_rom():
    s = d.slide("Nur Titel", "Orientierung: Republik und Prinzipat")
    bild(s, "rom.png", 1.6, 0.98, 4.7, 3.5)
    karte(s, 6.45, 1.0, 3.05, 3.4, "Prinzipat", ["Einrichtungen bleiben, die **Macht** liegt beim Princeps."], RUST, size=18)
    return s


def t3_a6():
    s = d.slide("Aufgabe", "Aufgabe 6: Quelle – Arbeitsfassung")
    c = B.box(s, X0, 1.0, W, 1.5, fill=GR, line=TEAL, lw=2)
    B.text(c, [[("»Augustus stellt in seinem Tatenbericht dar, er habe nach dem Ende der Bürgerkriege die staatliche Macht wieder dem Senat und dem römischen Volk übertragen. Seinen Vorrang beschreibt er über sein Ansehen.«", {"bold": True})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0)
    B.tb(s, X0, 2.6, W, 0.3, ["Arbeitsfassung nach Ergänzungsbuch S. 71 (M3), sprachlich vereinfacht – kein wörtliches Zitat."], size=14, color=MUTED, after=0)
    schritte(s, X0, 3.0, W, ["Wie nannte er sich selbst?", "Welchen Eindruck will er erzeugen?", "Welche Machtmittel lagen bei ihm – und warum prüfen wir die Aussage?"], size=18, farbe=GREEN)
    return s


def t3_a6_arbeit():
    return auftrag_folie("Jetzt: Aufgabe 6 – zu zweit", [6], {6: "zu zweit am Handy"}, "Selbstbezeichnung (Princeps) · gewünschter Eindruck · zwei Machtmittel · Quelle ist Selbstdarstellung")


def t3_a6_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgabe 6")
    y = frage_klick(s, 1.0, "Welche Machtmittel lagen bei Augustus?", "Oberbefehl über das Heer, Gewalt in Provinzen, Befugnisse von Konsul und Volkstribun, Ehrenname Augustus.", size=18)
    y = frage_klick(s, y, "Warum ist der Tatenbericht nützlich – und warum muss man ihn prüfen?", "Er zeigt das gewollte Bild, ist aber Selbstdarstellung: mit anderen Quellen und der tatsächlichen Machtverteilung vergleichen.", size=18)
    return s


def t3_a7():
    s = auftrag_folie("Jetzt: Aufgabe 7 – zu zweit (Tabelle)", [7], {7: "zu zweit am Handy"}, "Tabelle für Athen, Republik, Prinzipat ergänzen · zwei Ordnungen mit je einem Merkmal begründen")
    return s


def t3_a7_tab():
    s = d.slide("Aufgabe", "Aufgabe 7: Wo liegt die entscheidende Macht?")
    rows = [["Ordnung", "Wo liegt die entscheidende Macht?"]] + [[r[0], r[1]] for r in I.T[6]["tab"][1:]]
    B.auto_grid(s, X0, 0.98, [2.6, 6.4], rows, size=16, minh=0.3)
    B.tb(s, X0, 4.0, W, 0.5, [[("Ergänze am Handy: ", {"bold": True, "color": TEAL}), ("Beteiligung und Ausschluss · Kontrolle und Grenze", {})]], size=18, after=0)
    return s


def t3_a8():
    return auftrag_folie("Jetzt: Aufgabe 8, Teil 2 – Zeitstrahl", [8], {8: "Karten 5–9 legen, begründen, eigene Karte"}, "Karten 5–9 im richtigen Zeitbereich · Begründung bei zwei Karten · eigene Karte: gleichzeitig, aber nicht überall",
                         zeiten={8: 5})


def t3_bespr():
    s = d.slide("Aufgabe", "Besprechen: Aufgaben 7 und 8")
    y = frage_klick(s, 1.0, "Republik und Prinzipat: Was ist der Unterschied bei der Kontrolle?", "Republik: Befristung, zwei Konsuln, Einspruch der Tribunen. Prinzipat: formale Einrichtungen begrenzen den Princeps kaum.", size=18)
    y = frage_klick(s, y, "Eigene Karte (Aufgabe 8): gleichzeitig, aber nicht überall?", "z. B. Schrift in Mesopotamien – Ötzi ohne Schrift in den Alpen.", size=18)
    return s


def t3_ende():
    s = d.slide("Nur Titel", "Stopp, Quiz und Ausblick")
    y = 1.05
    for q, a in I.STOPPFRAGEN[3][:2]: y = frage_klick(s, y, q, a, w=6.8, size=16)
    qr(s, "quiz", 7.75, 1.05, 1.2, "Quiz")
    B.tb(s, X0, min(y, 3.75), W, 0.5, ["Weiter: Frühe Neuzeit um 1500 – antike Vorbilder werden neu gedeutet."], size=18, after=0)
    return s


def zusatz_folie():
    s = d.slide("Nur Titel", "OPTIONAL: Für Schnelle", hidden=True)
    rows = [["Nr.", "Zusatzaufgabe", "Zeit"]] + [[str(n), T[n]["title"], f"{T[n]['zeit']} min"] for n in (9, 10, 11, 12)]
    cells, h = B.auto_grid(s, X0, 1.05, [0.7, 6.9, 1.4], rows, size=20, minh=0.46)
    B.tb(s, X0, 1.05 + h + 0.15, W, 0.8, [f"Nur, wenn die Pflicht fertig ist. Keine Hausübung. Quiz »Meilenstein-Check« ({len(I.QUIZ)} Fragen) freiwillig."], size=18, after=0)
    return s


# ---------------------------------------------------------------- Ablauf je Stunde: (Schlüssel, Phasen, Art, Schritt auf »Heute«, Wozu?, Funktion)
SPEC = {
 1: [("t1_heute", [0], "START", None, "Klassenbuch; Ziel und Ablauf zeigen (QR Arbeitsblatt, Theorieteil)", lambda: heute_folie(1)),
     ("t1_einst", [1], "EINSTIEG", None, "Beil zeigen: Befund, Vermutung, Grenze mündlich sammeln – noch nicht auflösen", t1_einstieg),
     ("t1_lesen", [2], "LESEN", "Lesen", "Grundlagen selbst lesen – Stephan erklärt nicht vor",
      lambda: lesen_folie(1, "**Buch S. 25–32** zum Nachschlagen", ["vorrat", "probleme", "metall"], "Was braucht man, um Kupfer zu verarbeiten – und was folgt aus dem Beil allein nicht?", [2])),
     ("t1_a1", [3], "ZU ZWEIT", "Aufgabe 1", "Quellenkritik an einem Gegenstand (K01), Mini-Whiteboard", t1_a1),
     ("t1_klaeren", [4], "KURZ KLÄREN", "Kurz klären", "Befund ≠ Deutung; kein Automatismus zum Staat", t1_klaeren),
     ("t1_a2", [5], "AUFGABE", "Aufgabe 2", "Zusammenhänge begründen (K02, K04)", t1_a2),
     ("t1_a2b", [6], "BESPRECHEN", None, "Zusammenhang mit »weil« und Problem sichern", t1_a2_bespr),
     ("t1_lesen2", [7], "LESEN", "Lesen", "Schrift und frühe Staaten selbst lesen",
      lambda: lesen_folie(1, "**Buch S. 33–39** zum Nachschlagen", ["schrift", "staaten"], "Welche Aufgaben lösten Stadtstaat und Flächenkönigtum – und worin unterscheiden sie sich?", [7])),
     ("t1_karte", [7], "LESEN", None, "Karte zur Orientierung beim Lesen (Schema)", t1_karte),
     ("t1_a3", [8], "ZU ZWEIT", "Aufgabe 3", "Staatsformen vergleichen (K05)", t1_a3),
     ("t1_a3b", [9], "BESPRECHEN", "Tabelle", "Tabelle gemeinsam füllen (Klick je Zeile)", t1_a3_bespr),
     ("t1_a8", [10], "AUFGABE", "Zeitstrahl", "Karten 1–4 legen (K08), Schlusssatz", t1_a8),
     ("t1_pc", [11], "ZU ZWEIT", None, "Reserve: Partnercheck – nichts Neues beginnen", t1_pc)],
 2: [("t2_heute", [0, 1, 2], "TEST", None, "Klassenbuch, Test (20 min), einsammeln; danach Ziel von Teil 2", lambda: heute_folie(2)),
     ("t2_einst", [3], "EINSTIEG", "Einstieg", "Zuständigkeit und Verantwortung: Vorwissen für § 53", t2_einstieg),
     ("t2_lesen", [4], "LESEN", "Lesen", "Regeln und Grenze der Quelle selbst lesen",
      lambda: lesen_folie(2, "**Buch S. 39–40** zum Nachschlagen", ["regeln", "gleichheit"], "Welche Konflikte ordnet die Sammlung – und was zeigt sie nicht?", [4])),
     ("t2_klaeren", [5], "KURZ KLÄREN", "Kurz klären", "Wenn-dann-Muster, Arbeitsfassung, Quelle ≠ Alltag", t2_klaeren),
     ("t2_text", [6], "ZU ZWEIT", None, "Arbeitsfassung (Papier und Folie) lesen und markieren", t2_text),
     ("t2_a4", [6], "ZU ZWEIT", "Aufgabe 4", "Quellenarbeit am Paragrafenblatt (K01)", t2_a4),
     ("t2_bespr", [7], "BESPRECHEN", "Besprechen", "gleiche Verletzung – ungleiche Folgen; Eigentum; Grenze der Quelle", t2_bespr),
     ("t2_sich", [8], "ABSCHLUSS", None, "Stoppfragen sichern; Ausblick auf Stunde 3", t2_sich)],
 3: [("t3_heute", [0], "START", None, "Klassenbuch; Ziel von Teil 3", lambda: heute_folie(3)),
     ("t3_wdn", [1], "WIEDERHOLEN", "Weißt du noch?", "Vorwissen aus Stunde 1 und 2 aktivieren (Mini-Whiteboard)", t3_wdn),
     ("t3_lesen", [2], "LESEN", "Lesen", "Athen selbst lesen",
      lambda: lesen_folie(3, "**Ergänzungsbuch S. 62–65** zum Nachschlagen", ["athen"], "Wer gehörte zum »Volk« – und wer nicht?", [2])),
     ("t3_klaeren", [3], "KURZ KLÄREN", "Kurz klären", "Los und Wahl am Schaubild; wer gehört zum Volk", t3_klaeren),
     ("t3_a5", [4], "ZU ZWEIT", "Aufgabe 5", "Beteiligung und Ausschluss vergleichen (K06)", t3_a5),
     ("t3_skala", [5], "BEWEGUNG", None, "Aufstellen auf einer Skala – Urteil sichtbar machen, ohne Handy", t3_skala),
     ("t3_lesen2", [6], "LESEN", "Lesen", "Rom und Augustus selbst lesen",
      lambda: lesen_folie(3, "**Ergänzungsbuch S. 68–71** zum Nachschlagen", ["rom"], "Welche Einrichtungen bleiben – und wo liegt die Macht?", [6])),
     ("t3_rom", [6], "LESEN", None, "Schaubild zur Orientierung", t3_rom),
     ("t3_a6q", [7], "ZU ZWEIT", None, "Quelle lesen (Arbeitsfassung)", t3_a6),
     ("t3_a6", [7], "AUFGABE", "Aufgabe 6", "Selbstaussage und Machtverteilung (K01, K06)", t3_a6_arbeit),
     ("t3_a6b", [8], "BESPRECHEN", None, "Machtmittel und Quellenkritik sichern", t3_a6_bespr),
     ("t3_a7t", [9], "ZU ZWEIT", None, "Vergleichstabelle zeigen", t3_a7_tab),
     ("t3_a7", [9], "AUFGABE", "Aufgabe 7", "Vier Herrschaftsformen vergleichen (K06, N02)", t3_a7),
     ("t3_a8", [10], "AUFGABE", "Zeitstrahl", "Karten 5–9 legen, begründen, eigene Karte (K08)", t3_a8),
     ("t3_bespr", [11], "BESPRECHEN", "Besprechen", "Republik ↔ Prinzipat; Ungleichzeitigkeit", t3_bespr),
     ("t3_ende", [11], "ABSCHLUSS", None, "Stoppfragen, Quiz-QR, Ausblick", t3_ende)],
}

for teil, sp in SPEC.items():
    alle = sorted({i for x in sp for i in x[1]})
    assert alle == list(range(len(phasen(teil)))), (teil, alle)

DANACH_TEIL = {1: "Stunde 2 am Mo 23.11.: zuerst Test", 2: "Stunde 3 am Mo 30.11.: Athen und Rom", 3: "Ende der Einheit – nächstes Kapitel: Frühe Neuzeit (Buch S. 61)"}

FOLIE_NAME = {"t1_einst": "Einstieg", "t1_karte": "Karte", "t1_a2b": "Besprechen", "t1_pc": "Partnercheck", "t2_text": "Arbeitsfassung", "t2_sich": "Stoppfragen", "t3_skala": "Aufstellen",
              "t3_rom": "Schaubild", "t3_a6q": "Quelle", "t3_a6b": "Besprechen", "t3_a7t": "Tabelle", "t3_ende": "Quiz und Ausblick", "t3_lesen2": "Lesen: Rom"}


def FOLIE_TITEL(spec):
    return FOLIE_NAME.get(spec[0], spec[0])


# ================================================================ Deck bauen
def bauen():
    global d
    K = I.KLASSEN[0]
    d = B.Deck(True, "PBGW · 3BK · K2.1–5.4 Meilensteine · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Meilensteine: Vom Vorrat zum Staat")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["PBGW · 3BK · K2.1–5.4 · Unterrichts-PPP · " + " · ".join(I.DATEN[K][n] for n in (1, 2, 3)) + " · Buch S. 23–44, Ergänzungsbuch S. 58–73",
                        [(f"Stand {I.STAND} · {I.V} · TH-Unterricht (Ablauf) – zum Nachlesen: TH-Lehrer", {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    bedien = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    regie = {st["std"]: d.slide("Nur Titel", f"Regie 3BK · Stunde {st['std']} · {st['datum']}", hidden=True) for st in P.PLAN[K]}
    quellen = d.slide("Nur Titel", "Lehrer-Info · Aufbau und Prüfstand", hidden=True)
    for teil in (1, 2, 3):
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
    folgen = {t: [FOLIE[f"t{t}_sec"]] + [FOLIE[x[0]] for x in SPEC[t]] for t in (1, 2, 3)}
    for st in P.PLAN[K]:
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
        B.tb(s, X0, 0.98, W, 0.3, [[(f"3BK · {st['datum']} · Benutzerdefinierte Präsentation »Stunde {teil} {st['datum']}« · Foliennummern gelten für diese Datei", {"bold": True, "color": RUST})]], size=10, after=0)
        kn = P.KNAPP[(K, teil)]
        hk = B.th("Wenn es knapp wird: " + kn, 10, W, pad=0.04)
        size = 11
        while size > 8 and B.table_h([0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2) + hk > 3.95: size -= 1
        cells, h = B.auto_grid(s, X0, 1.28, [0.75, 4.2, 0.65, 3.4], rows, size=size, minh=0.2)
        B.tb(s, X0, 1.3 + h, W, hk, [[("Wenn es knapp wird: ", {"bold": True, "color": RUST}), (kn, {})]], size=10, after=0)
    B.tb(bedien, X0, 0.98, W, 4.1, [
        [("Eine Datei, eine Klasse. ", {"bold": True, "color": OLIVE}), ("F5 zeigt alle sichtbaren Folien in Unterrichtsreihenfolge (Stunde 1 → 3).", {})],
        [("Pro Stunde starten: ", {"bold": True, "color": OLIVE}), ("Bildschirmpräsentation → Benutzerdefinierte Bildschirmpräsentation → z. B. »Stunde 2 Mo 23.11.«. Ohne Menü: Foliennummer tippen und Enter (Nummern auf den Regiefolien).", {})],
        [("Jede Stunde läuft gleich: ", {"bold": True, "color": OLIVE}), ("»Heute« → »Lesen: …« (genaue Abschnitte im Theorieteil, Leitfrage) → »Kurz klären« (nur Fehlvorstellungen, Antwort per Klick) → »Jetzt: Aufgabe …« → »Besprechen« (Lösung per Klick, erst nach der Arbeitszeit).", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht, was JETZT läuft (Minuten aus plan.py) und was DANACH kommt.", {})],
        [("Stunde 2: ", {"bold": True, "color": OLIVE}), ("zuerst der Test (20 min, Stoff von dir, nicht in dieser PPP). Paragrafenblatt (TH-AB) ausdrucken.", {})],
        [("Nachschlagen statt zeigen: ", {"bold": True, "color": OLIVE}), ("TH-Lehrer und Theorieteil bleiben vollständig; Lösungen auch in TH-Loesung und der privaten Lösungsmappe. Zusatz 9–12: ausgeblendete Folie »OPTIONAL«.", {})],
        [("Regiepläne: ", {"bold": True, "color": OLIVE}), (f"Folien {nr_von[regie[1].slide_id]}–{nr_von[regie[3].slide_id]} (ausgeblendet), Präsentation »Lehrer-Regiepläne«.", {})]],
        size=13, after=5)
    B.tb(quellen, X0, 0.98, W, 4.1, ["· " + x for x in [
        "Grundlage: ChatGPT-Auftrag v2 (Ablauf je Termin, Texte, Aufgaben) – der Auftrag enthielt keine fertige Unterrichts-PPP; sie wurde hier neu gebaut.",
        "Alle 8 Pflichtaufgaben mit Zeit und »Am Ende steht da«; Aufgabe 8 über zwei Stunden geteilt (Karten 1–4 in Stunde 1, 5–9 in Stunde 3).",
        "Lesestopps mit genauen Abschnittstiteln und QR-Code; »Kurz klären« mit eigener Grafik; Regie als Tabelle aus plan.py.",
        "Methodenwechsel (Mini-Whiteboard und Karten · Test und Papier-Quellenarbeit · Aufstellen auf einer Skala); Klassenbuch je Stunde; Reserve nur in Stunde 1, in Stunde 2 und 3 ist die Besprechung der Puffer.",
        "Nur eigene Grafiken, keine Buchbilder (darum frei weitergebbar). Hammurabi- und Augustus-Text sind Arbeitsfassungen, keine Zitate.",
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

    show("3BK gesamt", [titel] + sum([folgen[t] for t in (1, 2, 3)], []))
    for st in P.PLAN[K]:
        show(f"Stunde {st['std']} {st['datum']}", ([titel] if st["std"] == 1 else []) + folgen[st["std"]])
    show("Lehrer-Regiepläne", [bedien] + [regie[n] for n in (1, 2, 3)] + [quellen])
    show("Optional: Für Schnelle", [zusatz])

    os.makedirs(ZIEL, exist_ok=True)
    name = f"{I.PRAEFIX}-TH-Unterricht-{I.V}.pptx"
    d.save(os.path.join(ZIEL, name))
    sicht = [s for s in d.p.slides if s._element.get("show") != "0"]
    for x in PROBLEME: print("ÜBERLAUF", x)
    print("ok", name, len(d.p.slides._sldIdLst), "Folien,", len(sicht), "sichtbar ·", nid[0], "Präsentationen")
    for t in (1, 2, 3): print("  Stunde", t, "Folien", [nr_von[x.slide_id] for x in folgen[t]])


if __name__ == "__main__":
    bauen()
