"""Unterrichts-PPP K2.1 Mechanische Kräfte (TH-Unterricht) – die eine PPP, aus der Prof. HOLZER die sechs Stunden hält.
Aufbau: je Stunde »Heute« → »Weißt du noch?« → »Kurz klären« → Arbeitsauftrag → »Besprechen« → Abgabe.
Unten links auf jeder Folie die Phasenleiste »JETZT <Phase> · x min« und »Danach: …«. Alle Minuten kommen aus plan.py (eine Quelle mit Fahrplan und Lösungsseite).
Ausgeblendet: Bedienung, Regie je Stunde (Minute · Was läuft jetzt? · Folie · Wozu?), Lehrplanbezug, Herrichten, Kürzungsliste, Referat/Doppelstunde, Quellen,
Ausgleichsbausteine (eigene Präsentation »Ausgleich« für die Klasse, die vorne liegt).
Aufruf im Repository-Ordner: python3 werkzeug/quellen/1ab-k2-1-kraefte/unterricht_ppp.py <BHAK_Folienmaster.pptx> <Zielordner>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ppp_basis as B
import inhalt as I, plan as P, theorie_daten as TD, versuche_daten as VD, gruppen_daten as GD, ausgleich as AG
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree

ZIEL = sys.argv[2]
OLIVE, INK, TEAL, RUST, MUTED, WHITE, GREEN, ORANGE, CARD, RED = B.OLIVE, B.INK, B.TEAL, B.RUST, B.MUTED, B.WHITE, B.GREEN, B.ORANGE, B.CARD, B.RED
X0, W = 0.5, 9.0
YC = 4.52
UNIT = B.UNIT
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

FARBE = {"START": MUTED, "WIEDERHOLEN": TEAL, "EINSTIEG": ORANGE, "KURZ KLÄREN": OLIVE, "AUFGABE": GREEN,
         "SELBSTSTUDIUM": TEAL, "GRUPPENARBEIT": ORANGE, "VIDEO": TEAL, "GRUPPEN": OLIVE, "FREIGABE": RUST, "PARTNERCHECK": GREEN,
         "RECHERCHE": TEAL, "PLANEN": TEAL, "VERSUCH": RED, "ZU ZWEIT": GREEN, "PRÄSENTATION": RUST,
         "BESPRECHEN": ORANGE, "ABGABE": RUST, "DISKUSSION": ORANGE}
T = {t["nr"]: t for t in I.T}
METHODE_KURZ = {1: "Mit der ganzen Klasse", 2: "Selbststudium mit Leitfragen", 3: "Selbst gewählter Versuch",
                4: "Steckbrief und Partnercheck", 5: "Kurzpräsentationen", 6: "Tafel und Einzelarbeit"}
PROBLEME = []
SPEC = {}
FOLIE = {}


# ================================================================ Bausteine
def phasen(std):
    return P.STUNDE[std]


def minuten(std, idx):
    return "%d min" % sum(phasen(std)[i][1] for i in idx)


def hinweis(s, art, mins, danach):
    col = FARBE.get(art, OLIVE)
    lab = ("JETZT " + art if art not in ("START", "ABGABE") else art) + (" · " + mins if mins else "")
    w1 = max(2.2, min(4.8, B.FONT_B.getlength(lab) / 100 * 14 / 72 + 0.45))
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


def merke(s, y, txt, size=20, h=None, w=W):
    h = h or B.th(txt, size, w - 0.1, bold=True, pad=0.24)
    c = B.box(s, X0, y, w, h, fill=OLIVE)
    B.text(c, [txt], size=size, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return c, h


def frage_klick(s, y, frage, antwort, w=W, x=X0, size=20):
    hq = B.th(frage, size, w, True, pad=0.06)
    B.tb(s, x, y, w, hq, [frage], size=size, bold=True, after=0)
    ha = B.th(antwort, size, w - 0.2, pad=0.16)
    B.box(s, x, y + hq, w, ha, fill=RGBColor.from_string("FFFFFF"), line=ORANGE, lw=1.5)
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


def titel_von(s):
    return next((ph.text_frame.text for ph in s.placeholders if ph.placeholder_format.type == 1), "?")


def check(s):
    for sh in s.shapes:
        if sh.is_placeholder or sh.name == "Buchseite": continue
        unten = (sh.top + sh.height) / 914400
        if unten > YC + 0.02 and sh.top / 914400 < 4.6:
            PROBLEME.append(f"»{titel_von(s)}«: {sh.name} bis {unten:.2f} in")


def heute_folie(std):
    s = d.slide("Nur Titel", "Stunde %d · Heute" % std)
    ziel = P.ZIEL[std]
    c = B.box(s, X0, 1.0, 6.9, B.th("Ziel: " + ziel, 20, 6.8, pad=0.18), fill=OLIVE)
    B.text(c, [[("Ziel: ", {"bold": True}), (ziel, {})]], size=20, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, after=0)
    y = 1.0 + c.height / 914400 + 0.14
    st = [(sp[3], sp[1]) for sp in SPEC[std] if sp[3]]
    items = ["%s · %s" % (lab, minuten(std, idx)) for lab, idx in st]
    if len(items) <= 4:
        schritte(s, X0, y, 6.9, items, size=20, farbe=GREEN)
    else:
        h1 = (len(items) + 1) // 2
        for col, teil in enumerate((items[:h1], items[h1:])):
            yy = y
            for i, it in enumerate(teil):
                n = i + 1 + col * h1
                cc = B.box(s, X0 + col * 3.5, yy + 0.04, 0.4, 0.4, fill=GREEN)
                B.text(cc, [str(n)], size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
                hh = B.th(it, 18, 3.0, pad=0.04)
                B.tb(s, X0 + col * 3.5 + 0.48, yy, 3.0, hh, [it], size=18, after=0)
                yy += max(0.48, hh + 0.04)
    qr(s, "aufgaben", 7.8, 1.0, 1.05, "Arbeitsblatt")
    qr(s, "theorie", 7.8, 2.5, 1.05, "Theorie")
    return s


def auftrag_folie(titel, nrs, tun, erwartet, ohne_handy=None, layout="Aufgabe"):
    s = d.slide(layout, titel)
    rows = [["Nr.", "Aufgabe", "Zeit", "So arbeitest du"]]
    for n in nrs:
        rows.append([str(n), T[n]["title"], "%d min" % T[n]["zeit"], tun.get(n, "allein am Handy")])
    cells, h = B.auto_grid(s, X0, 1.05, [0.6, 3.6, 0.8, 4.0], rows, size=18, minh=0.42)
    y = 1.05 + h + 0.14
    if ohne_handy:
        hh = B.th("Handy bleibt zuerst weg: " + ohne_handy, 18, W - 0.2, pad=0.18)
        c = B.box(s, X0, y, W, hh, fill=RGBColor.from_string("F6E3DF"), line=RUST)
        B.text(c, [[("Handy bleibt zuerst weg: ", {"bold": True, "color": RUST}), (ohne_handy, {})]], size=18, anchor=MSO_ANCHOR.MIDDLE, after=0); y += hh + 0.12
    if erwartet:
        he = B.th("Am Ende steht da: " + erwartet, 20, W - 0.2, pad=0.18)
        c = B.box(s, X0, y, W, he, fill=WHITE, line=GREEN, lw=1.5)
        B.text(c, [[("Am Ende steht da: ", {"bold": True, "color": GREEN}), (erwartet, {})]], size=20, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return s


def wdh_folie(std, titel="Weißt du noch?"):
    s = d.slide("Nur Titel", titel)
    y = 1.05
    for q, a in I.WEISST_DU_NOCH[std]: y = frage_klick(s, y, q, a)
    return s


# ================================================================ Folien Stunde 1
def s1_wdh():
    s = d.slide("Nur Titel", "Weißt du noch? Aus »Erkenntnisgewinn«")
    y = 1.05
    for q, a, _ in I.WIEDERHOLEN: y = frage_klick(s, y, q, a, size=19)
    return s


def s1_vor():
    s = d.slide("Nur Titel", "Was glaubst du?")
    B.tb(s, X0, 0.98, W, 0.34, [[("Arbeitsblatt öffnen, Aufgabe 1. Keine Punkte, kein richtig oder falsch – nur tippen.", {"color": MUTED})]], size=18, after=0)
    v = T[1]["fields"]
    for i, f in enumerate(v):
        karte(s, X0 + i * 4.6, 1.34, 4.4, 2.1, "Frage %s" % "ab"[i], [f[1].split(") ", 1)[1], [(" · ".join(f[2]), {"color": MUTED, "size": 17})]], [ORANGE, TEAL][i], size=19)
    a = B.tb(s, X0, 3.58, 7.6, 0.55, ["Aufgelöst wird erst in Stunde 6 – die Seite zeigt euch dann eure eigene Vermutung."], size=18, color=RED, bold=True, after=0)
    s._anim.append([a])
    s.shapes.add_picture(B.qr_png(B.URL["aufgaben"]), Inches(8.45), Inches(3.5), Inches(0.78), Inches(0.78))
    return s


def s1_kraft():
    s = d.slide("Nur Titel", "Kurz klären: Was eine Kraft bewirkt")
    B.picture(s, UNIT + "img/wirkung.png", X0, 1.0, 9.0, 2.5)
    c, h = merke(s, 3.6, "Eine Kraft ändert Tempo oder Richtung einer Bewegung – oder sie verformt. Für die Bewegungsänderung zählt die resultierende Kraft.")
    s._anim.append([c])
    return s


def s1_rechnen():
    s = d.slide("Nur Titel", "Kurz klären: rechnen und Einheiten")
    rows = [["Größe", "Zeichen", "Einheit", "Formel"],
            ["Weg / Zeit / Tempo", "s / t / v", "m / s / m/s", "v = s / t · mal 3,6 ergibt km/h"],
            ["Masse", "m", "kg", "auf der Waage"],
            ["Kraft", "F", "N", "F = m · a · 1 N = 1 kg · m/s²"]]
    cells, h = B.auto_grid(s, X0, 0.98, [2.5, 1.5, 1.6, 3.4], rows, size=17, minh=0.38)
    y = 0.98 + h + 0.14
    y = frage_klick(s, y, "Musterbeispiel: 2 kg werden mit 3 m/s² beschleunigt. Wie groß ist die Kraft?",
                    "F = m · a = 2 kg · 3 m/s² = 6 N. Die Einheit gehört dazu.", size=19)
    return s


def s1_bespr():
    s = d.slide("Aufgabe", "Das besprechen wir: Aufgabe 2")
    y = 1.05
    y = frage_klick(s, y, "a) Fahrrad fährt mit gleichem Tempo durch eine Kurve. Was ändert sich?", "Die Richtung der Geschwindigkeit – das ist auch eine Beschleunigung.")
    y = frage_klick(s, y, "c) und d) 5 m in 4 s – wie schnell?", "v = 5 m : 4 s = 1,25 m/s · mal 3,6 = 4,5 km/h.")
    y = frage_klick(s, y, "e) 2 kg mit 3 m/s² – wie groß ist die Kraft?", "F = 2 kg · 3 m/s² = 6 N.")
    return s


def grosse_tabelle(s, zeilen, size=22, y=1.0, lw=1.9):
    """Große, einfache Übersicht: links die Frage (Wer? Was? …), rechts kurz die Antwort."""
    rows = [["", ""]] + [[a, b] for a, b in zeilen]
    cells, h = B.auto_grid(s, X0, y, [lw, W - lw], rows[1:], size=size, head=False, minh=0.5)
    return y + h


def s1_videos():
    s = d.slide("Nur Titel", "Video: Newtons drei Gesetze")
    for i, n in enumerate((1, 2, 3)):
        v = GD.NEWTON[n]; x = X0 + i * 3.05
        s.shapes.add_picture(B.qr_png(v["url"]), Inches(x + 0.7), Inches(0.95), Inches(1.45), Inches(1.45))
        B.tb(s, x, 2.45, 2.85, 0.4, [[("%d. Gesetz" % n, {"bold": True, "color": OLIVE})]], size=20, align=PP_ALIGN.CENTER, after=0)
        B.tb(s, x, 2.85, 2.85, 0.4, [[(v["kurz"], {"bold": True, "color": TEAL})]], size=20, align=PP_ALIGN.CENTER, after=0)
        B.tb(s, x - 0.1, 3.3, 3.05, 0.3, [v["url"].replace("https://", "")], size=9, color=MUTED, align=PP_ALIGN.CENTER, after=0)
    B.tb(s, X0, 3.75, W, 0.36, [[("Martin Apolin, YouTube · ", {"bold": True}), ("Gruppen 1, 2, 4 und 7: Video auf der Gruppenkarte. Alle: Theorie-Seite, Teil 1 und 8.", {})]],
         size=16, after=0)
    return s


def s1_gruppen():
    s = d.slide("Nur Titel", "Eure Gruppen")
    rows = [["Gr.", "Thema", "Buch", "Namen"]]
    for n in range(1, 8):
        g = GD.G[n]; rows.append([str(n), g["thema"], g["buch"].replace("Buch ", ""), ""])
    cells, h = B.auto_grid(s, X0, 0.94, [0.6, 3.1, 1.4, 3.9], rows, size=17, minh=0.38)
    B.tb(s, X0, 0.94 + h + 0.08, W, 0.36, [[("Die Einteilung lost Prof. HOLZER aus. ", {"bold": True, "color": OLIVE}),
                                           ("Sie gilt für alle sechs Stunden.", {})]], size=16, after=0)
    return s


def s1_projekt():
    s = d.slide("Nur Titel", "So läuft euer Projekt")
    grosse_tabelle(s, [["Wer?", "Eure Gruppe – jeder hat eine Rolle"],
                       ["Was?", "Thema selbst erarbeiten · Versuch selbst wählen · Steckbrief · 3 Minuten präsentieren"],
                       ["Abgeben?", "EIN Arbeitsblatt-PDF in LMS · Steckbrief als Handout in Teams"],
                       ["Bis wann?", "Plan: Ende Stunde 2 · Steckbrief: Ende Stunde 4 · PDF: Stunde 6"],
                       ["Wo?", "Arbeitsblatt, Aufgaben 3 bis 7"]], size=21)
    return s


def s1_ende():
    s = d.slide("Nur Titel", "Zwischenstand sichern")
    schritte(s, X0, 1.05, 6.9, ["Arbeitsblatt: »PDF erstellen« und aufheben – noch nicht hochladen.",
                                "Aufgabe 3 a) und b): Gruppe und Rolle schon jetzt eintragen.",
                                "Nächste Stunde arbeitet ihr selbstständig: Thema erarbeiten, Versuch planen."], size=20, farbe=RUST)
    qr(s, "aufgaben", 7.9, 1.05, 1.1, "Arbeitsblatt")
    return s


# ================================================================ Folien Stunde 2
def s2_selbst():
    s = d.slide("Nur Titel", "Heute arbeitet ihr selbstständig")
    schritte(s, X0, 1.0, 6.7, ["Arbeitsblatt öffnen, Aufgabe 3: Gruppe wählen – eure Gruppenkarte erscheint.",
                               "Buchseiten und Theorie-Teil lesen, Leitfragen in eigenen Worten beantworten.",
                               "Aufgabe 4: Versuch aussuchen und planen – erst auf Papier.",
                               "Plan Prof. HOLZER zeigen. Ohne Freigabe kein Versuch."], size=20, farbe=TEAL)
    qr(s, "aufgaben", 7.8, 1.0, 1.1, "Arbeitsblatt")
    return s


def s2_a3():
    return auftrag_folie("Jetzt: Aufgabe 3 – Thema erarbeiten", [3], {3: "allein lesen, in der Gruppe besprechen"},
                         "Vier Leitfragen in eigenen Worten und ein geprüftes Video oder eine zweite Quelle.",
                         ohne_handy="Zuerst im Buch lesen und markieren, dann tippen.")


def s2_a4():
    s = d.slide("Nur Titel", "Euren Versuch selbst wählen")
    karte(s, X0, 0.98, 4.4, 2.5, "Von zu Hause erlaubt", ["Kunststoff, Papier, Holz, Stoff", "Wasser, Salz, Lebensmittelfarbe",
                                                          "Knete, Gummiringe, Strohhalme", "Spielzeugauto, Ball, Schuhe"], GREEN, size=18)
    karte(s, X0 + 4.6, 0.98, 4.4, 2.5, "Nicht erlaubt", ["Feuer, Kerzen", "Chemikalien, Spraydosen", "Glas von zu Hause, Messer, Nägel",
                                                         "Steckdose, Akkus · Waffen, Feuerwerk"], RED, size=18)
    c, h = merke(s, 3.6, "Materialliste genau aufschreiben: was, wie viel, Saal oder zu Hause, wer bringt es mit.", size=18)
    return s


def s2_freigabe():
    s = d.slide("Aufgabe", "Freigabe: je Gruppe eine Minute")
    y = schritte(s, X0, 1.0, 6.9, [x for x in GD.FREIGABE_FRAGEN], size=18, farbe=ORANGE)
    qr(s, "aufgaben", 7.9, 1.0, 1.1, "Arbeitsblatt")
    return s


def s2_ende():
    s = d.slide("Nur Titel", "Sichern und mitbringen")
    schritte(s, X0, 1.05, 9.0, ["Aufgabe 4 f): »freigegeben« eintragen.",
                                "Arbeitsblatt: »PDF erstellen« und aufheben – noch nicht hochladen.",
                                "Nächste Stunde: Material von zu Hause mitbringen. Wer es vergisst, nimmt die Saal-Variante."], size=20, farbe=RUST)
    return s


# ================================================================ Folien Stunde 3
def s3_sicher():
    s = d.slide("Nur Titel", "Sicherheit heute")
    y = 0.95
    for h_, t_ in [("Nur Freigegebenes", "Ihr baut nur, was Prof. HOLZER freigegeben hat."),
                   ("Wasser", "nur in der Wanne, sofort aufwischen."),
                   ("Kraftmesser", "langsam ziehen, nie gegen den Körper."),
                   ("Spritze, Ballon", "nie auf Personen richten."),
                   ("Glas", "nur Saal-Glas; bei Bruch Prof. HOLZER rufen."),
                   ("Gang", "nur gehen, Weg frei halten.")]:
        c = B.box(s, X0, y + 0.03, 0.4, 0.4, fill=ORANGE)
        B.text(c, ["!"], size=18, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
        hh = B.th(h_ + ": " + t_, 20, 8.3, pad=0.02)
        B.tb(s, X0 + 0.52, y, 8.4, hh, [[(h_ + ": ", {"bold": True, "color": OLIVE}), (t_, {})]], size=20, after=0)
        y += max(0.48, hh + 0.02)
    return s


def s3_versuch():
    s = d.slide("Nur Titel", "So läuft der Versuch")
    grosse_tabelle(s, [["Wer?", "Eure Gruppe aus Stunde 1"],
                       ["Was tun?", "Aufbauen · machen · eintragen · vorführen"],
                       ["Abgeben?", "Aufgabe 5 mit Foto – jeder selbst"],
                       ["Bis wann?", "Bis Minute 41, dann aufräumen"],
                       ["Wo?", "Euer Platz laut Freigabe"]], size=28, lw=2.1)
    return s


def s3_probe():
    s = d.slide("Aufgabe", "Probe: einmal vorführen")
    y = frage_klick(s, 1.05, "Was sieht die Klasse in eurem Versuch?", "Eine Sache, die man sehen oder messen kann – in einem Satz.")
    y = frage_klick(s, y, "Was ist eure Erklärung?", "Mit dem Fachbegriff eures Themas. Erst Beobachtung, dann Erklärung.")
    return s


def s3_ende():
    s = d.slide("Nur Titel", "Aufräumen und sichern")
    schritte(s, X0, 1.0, 9.0, ["Gefäße ausspülen, Tische trocken wischen, Saal-Material zurück an den Lehrertisch.",
                               "Eigenes Material wieder einpacken.",
                               "Arbeitsblatt: »PDF erstellen« und aufheben – noch nicht hochladen.",
                               "Nächste Stunde: Steckbrief schreiben und Präsentation proben."], size=19, farbe=RUST)
    return s


# ================================================================ Folien Stunde 4
def s4_steck():
    s = d.slide("Nur Titel", "Euer Steckbrief – das Handout für alle")
    rows = [["", "Das steht drin"]] + [[f[1].split(") ")[0] + ")", f[1].split(") ", 1)[1]] for f in GD.STECKBRIEF]
    cells, h = B.auto_grid(s, X0, 0.95, [0.6, 8.4], rows[1:], size=17, head=False, minh=0.36)
    B.tb(s, X0, 0.95 + h + 0.08, W, 0.36, [[("Schriftführung: ", {"bold": True, "color": RUST}),
                                           ("»Handout-PDF erstellen« und bis Ende der Stunde in Teams stellen.", {})]], size=17, after=0)
    return s


def s4_probe():
    s = d.slide("Aufgabe", "Präsentation: höchstens 3 Minuten")
    rows = [["Teil", "Inhalt", "Zeit"],
            ["1", "Euer Thema in zwei Sätzen und die Formel", "45 s"],
            ["2", "Versuch zeigen: Was sieht man?", "75 s"],
            ["3", "Erklärung und ein Beispiel aus Sport oder Bundesheer", "60 s"]]
    cells, h = B.auto_grid(s, X0, 1.0, [0.8, 6.8, 1.4], rows, size=20, minh=0.48)
    c, hm = merke(s, 1.0 + h + 0.18, "Jeder spricht. Keine PowerPoint nötig – der Steckbrief ist euer Spickzettel. Mit Stoppuhr üben.", size=19)
    return s


def s4_peer():
    s = d.slide("Aufgabe", "Partnercheck")
    y = schritte(s, X0, 1.0, W, ["Gruppe 1 mit 2, 3 mit 4, 5 mit 6 – Gruppe 7 mit Prof. HOLZER.",
                                 "Die Partnergruppe liest euren Steckbrief und hört die Probe.",
                                 "Rückmeldung: zwei Dinge, die gut sind, und eine Sache, die noch unklar ist."], size=19, farbe=GREEN)
    c = B.box(s, X0, y + 0.1, W, 0.55, fill=RGBColor.from_string("F6E3DF"), line=RUST, lw=1.5)
    B.text(c, [[("Ohne Handy: ", {"bold": True, "color": RUST}), ("zuhören, dann reden.", {})]], size=19, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return s


def s4_ende():
    s = d.slide("Nur Titel", "Handout teilen, sichern")
    schritte(s, X0, 1.0, 9.0, ["Schriftführung: Handout-PDF in Teams stellen – Kanal der Klasse.",
                               "Alle: Arbeitsblatt »PDF erstellen« und aufheben.",
                               "Nächste Stunde präsentieren alle sieben Gruppen. Eigenes Material mitbringen!"], size=20, farbe=RUST)
    return s


# ================================================================ Folien Stunde 5
def s5_auftrag():
    s = d.slide("Nur Titel", "Mitschreiben – für Aufgabe 8")
    karte(s, X0, 1.0, 4.4, 2.1, "Zu jeder Gruppe", ["die **Kernaussage** in einem Satz", "eine **Formel** oder ein **Beispiel**"], TEAL, size=20)
    karte(s, X0 + 4.6, 1.0, 4.4, 2.1, "Wohin?", ["Arbeitsblatt, **Aufgabe 7**", "oder auf Papier – später abtippen"], GREEN, size=20)
    c, h = merke(s, 3.35, "In Stunde 6 kommen alle sieben Themen in Aufgabe 8 vor. Die Steckbriefe stehen in Teams.", size=18, w=7.6)
    qr(s, "aufgaben", 8.5, 3.35, 0.72, "")
    return s


def s5_praes():
    s = d.slide("Nur Titel", "Sieben Gruppen · je 3 Minuten")
    rows = [["Gruppe"] + [str(g) for g in range(1, 8)],
            ["Thema"] + ["Bewe-\ngung", "Gewicht", "Auftrieb", "Reibung", "Kapillar", "Druck", "Gegen-\nkraft"],
            ["fertig nach Minute"] + ["%d" % (9 + 4 * g) for g in range(1, 8)]]
    cells, h = B.auto_grid(s, X0, 1.0, [1.85] + [1.02] * 7, rows, size=15, minh=0.4)
    y = 1.0 + h + 0.16
    y = schritte(s, X0, y, W, ["3 Minuten je Gruppe einschließlich Versuch – danach 1 Minute Übergang.",
                               "Jeder in der Gruppe spricht.",
                               "Alle anderen schreiben mit: Kernaussage und Formel oder Beispiel."], size=19, farbe=RUST)
    return s


def s5_klaeren():
    s = d.slide("Aufgabe", "Das besprechen wir")
    y = 1.05
    y = frage_klick(s, y, "Ist Druck eine eigene Kraftart?", "Nein. Druck verbindet eine Kraft mit der Fläche, auf die sie wirkt: p = F / A.")
    y = frage_klick(s, y, "Wie groß ist die Auftriebskraft bei einem ruhig schwimmenden Körper?", "Genauso groß wie seine Gewichtskraft – das ist ein Kräftegleichgewicht.")
    return s


def s5_ende():
    s = d.slide("Nur Titel", "Mitschrift ergänzen, sichern")
    schritte(s, X0, 1.0, 6.8, ["Aufgabe 7 ergänzen – die Steckbriefe der anderen findest du in Teams.",
                               "Arbeitsblatt »PDF erstellen« und aufheben.",
                               "Nächste Stunde: Aufgabe 8 allein, danach Abgabe in LMS."], size=19, farbe=RUST)
    qr(s, "aufgaben", 7.8, 1.0, 1.1, "Arbeitsblatt")
    return s


# ================================================================ Folien Stunde 6
def s6_tabelle():
    s = d.slide("Nur Titel", "Alles zusammen: Größen und Einheiten")
    B.picture(s, UNIT + "img/einheiten.png", X0, 0.95, 9.0, 3.3)
    return s


def s6_denkfehler():
    s = d.slide("Nur Titel", "Drei häufige Denkfehler")
    y = 1.0
    for q, a in [("»Beim Schwimmen ist der Auftrieb größer.«", "Beim ruhigen Schwimmen sind Auftriebskraft und Gewichtskraft gleich groß."),
                 ("»Reibung bremst immer.«", "Haftreibung drückt beim Gehen den Fuß nach vorne – sie treibt an."),
                 ("»Gewichtskraft und Stützkraft am Buch sind Kraft und Gegenkraft.«", "Nein – beide wirken auf das Buch. Ein Wechselwirkungspaar wirkt auf zwei verschiedene Körper.")]:
        y = frage_klick(s, y, q, a, size=19)
    return s


def s6_a4():
    return auftrag_folie("Jetzt: Aufgabe 8 – allein und ohne KI", [8], {8: "allein am Handy, Tipps erlaubt"},
                         "Zehn Teilantworten mit Einheit. Tipps kosten keine Punkte – »Lösung ansehen« zählt null.")


def s6_bespr():
    s = d.slide("Aufgabe", "Das besprechen wir: die Rechenwege")
    y = 1.05
    y = frage_klick(s, y, "a) 6 kg bei g = 10 N/kg", "F_G = m · g = 6 kg · 10 N/kg = 60 N")
    y = frage_klick(s, y, "e) 120 N auf 0,02 m²", "p = F / A = 120 N : 0,02 m² = 6000 Pa")
    y = frage_klick(s, y, "i) 9 m in 6 s   ·   j) 12 N auf 3 kg", "v = 9 m : 6 s = 1,5 m/s   ·   a = 12 N : 3 kg = 4 m/s²")
    return s


def s6_ende():
    s = d.slide("Nur Titel", "Auflösung, Selbsteinschätzung, Abgabe")
    y = schritte(s, X0, 1.0, 6.7, ["Aufgabe 1: »Auflösung zeigen« – die Seite zeigt eure Vermutung aus Stunde 1.",
                                   "Theorie-Seite, »Kann ich das?«: sicher / fast / noch nicht antippen.",
                                   "Arbeitsblatt: »PDF erstellen« und JETZT in LMS hochladen – das ist deine Abgabe.",
                                   "Freiwillig: Kräfte-Check (Quiz) und die Zusatzaufgaben 9 bis 11."], size=19, farbe=RUST)
    qr(s, "aufgaben", 7.9, 1.0, 1.05, "Arbeitsblatt")
    qr(s, "quiz", 7.9, 2.5, 1.05, "Quiz")
    return s


# ================================================================ Ablauf je Stunde
SPEC = {
 1: [("s1_heute", [0], "START", None, "Ziel und Ablauf zeigen", lambda: heute_folie(1)),
     ("s1_wdh", [1], "WIEDERHOLEN", "Weißt du noch?", "An den fairen Test aus K1.4 anknüpfen", s1_wdh),
     ("s1_vor", [2], "EINSTIEG", "Was glaubst du?", "Vorhersagen festhalten – nicht auflösen", s1_vor),
     ("s1_kraft", [3], "KURZ KLÄREN", "Kraftwirkung", "Fehlvorstellung »Bewegung heißt Kraft« ausräumen", s1_kraft),
     ("s1_rechnen", [3], "KURZ KLÄREN", None, "Einheiten und ein Musterbeispiel zeigen, bevor gerechnet wird", s1_rechnen),
     ("s1_videos", [3], "KURZ KLÄREN", "Newton-Videos", "Optional: einen kurzen Ausschnitt aus Video 1 (Trägheit) zeigen – nur wenn Zeit bleibt, sonst nur QR-Codes zeigen", s1_videos),
     ("s1_a2", [4], "AUFGABE", "Aufgabe 2", "Begriffe und die drei Rechnungen anwenden",
      lambda: auftrag_folie("Jetzt: Aufgabe 2", [2], {2: "allein am Handy, Theorie-Karte ist dabei"},
                            "Zwei Auswahlfelder und drei Rechnungen – immer mit Einheit.")),
     ("s1_bespr", [5], "BESPRECHEN", None, "Die drei Rechenwege gemeinsam durchgehen", s1_bespr),
     ("s1_gruppen", [6], "GRUPPEN", "Gruppen", "Gruppen mit dem Generator der Lösungsseite auslosen und zeigen", s1_gruppen),
     ("s1_projekt", [6], "GRUPPEN", "So läuft das Projekt", "Wer, was, abgeben, bis wann, wo – einmal klar für alle", s1_projekt),
     ("s1_ende", [7, 8], "ABGABE", "Sichern", "Zwischenstand sichern; Reserve", s1_ende)],
 2: [("s2_heute", [0], "START", None, "Ziel zeigen, Gruppen setzen sich zusammen", lambda: heute_folie(2)),
     ("s2_wdh", [1], "WIEDERHOLEN", "Wo stehen wir?", "Gruppe, Thema und Rolle aktivieren", lambda: wdh_folie(2)),
     ("s2_selbst", [2], "START", "Selbstständig", "Ablauf der selbstständigen Stunde zeigen", s2_selbst),
     ("s2_a3", [3], "SELBSTSTUDIUM", "Aufgabe 3", "Thema mit Leitfragen erarbeiten – du gehst herum und hilfst", s2_a3),
     ("s2_a4", [4], "GRUPPENARBEIT", "Versuch wählen", "Regeln für Material von zu Hause zeigen, Plan auf Papier", s2_a4),
     ("s2_frei", [5], "FREIGABE", "Freigabe", "Jeden Plan kurz prüfen; Materiallisten fotografieren", s2_freigabe),
     ("s2_ende", [6, 7], "ABGABE", "Sichern", "Sichern, Mitbringen ansagen; Reserve", s2_ende)],
 3: [("s3_heute", [0], "START", None, "Ziel zeigen, Gruppen an ihre Plätze schicken", lambda: heute_folie(3)),
     ("s3_wdh", [1], "WIEDERHOLEN", "Wo stehen wir?", "Plan und Material da?", lambda: wdh_folie(3)),
     ("s3_sicher", [2], "KURZ KLÄREN", "Sicherheit", "Sicherheitsregeln vor dem Aufbau", s3_sicher),
     ("s3_versuch", [3], "VERSUCH", "Versuch", "Folie bleibt während der Arbeit stehen", s3_versuch),
     ("s3_probe", [4], "VERSUCH", "Probe", "Jede Gruppe führt einmal vor – du hörst bei zwei Gruppen zu", s3_probe),
     ("s3_ende", [5, 6, 7], "ABGABE", "Aufräumen", "Aufräumen, sichern; Reserve", s3_ende)],
 4: [("s4_heute", [0], "START", None, "Ziel zeigen", lambda: heute_folie(4)),
     ("s4_wdh", [1], "WIEDERHOLEN", "Wo stehen wir?", "Ergebnis des Versuchs in einem Satz", lambda: wdh_folie(4)),
     ("s4_steck", [2], "GRUPPENARBEIT", "Steckbrief", "Steckbrief gemeinsam schreiben", s4_steck),
     ("s4_probe", [3], "GRUPPENARBEIT", "Präsentation proben", "Drei-Minuten-Ablauf mit Stoppuhr", s4_probe),
     ("s4_peer", [4], "PARTNERCHECK", "Partnercheck", "Partnergruppe liest und hört zu", s4_peer),
     ("s4_ende", [5, 6], "ABGABE", "Teilen", "Handout in Teams, sichern; Reserve", s4_ende)],
 5: [("s5_heute", [0], "START", None, "Ziel zeigen, Reihenfolge ansagen", lambda: heute_folie(5)),
     ("s5_auftrag", [1], "START", "Mitschreiben", "Zuhörer bekommen eine Aufgabe", s5_auftrag),
     ("s5_praes", [2], "PRÄSENTATION", "Präsentationen", "Sieben Gruppen mit fester Zeit", s5_praes),
     ("s5_klaeren", [3], "BESPRECHEN", "Das besprechen wir", "Die häufigsten Fehler aus den Vorträgen geraderücken", s5_klaeren),
     ("s5_ende", [4, 5, 6], "ABGABE", "Ergänzen", "Mitschrift ergänzen, sichern; Reserve", s5_ende)],
 6: [("s6_heute", [0], "START", None, "Ziel zeigen", lambda: heute_folie(6)),
     ("s6_wdh", [1], "WIEDERHOLEN", "Weißt du noch?", "Die sieben Themen kurz aktivieren", lambda: wdh_folie(6)),
     ("s6_tab", [2], "KURZ KLÄREN", "Übersicht", "Alle Größen und Einheiten nebeneinander", s6_tabelle),
     ("s6_denk", [2], "KURZ KLÄREN", None, "Die drei häufigsten Denkfehler ansprechen", s6_denkfehler),
     ("s6_a4", [3], "AUFGABE", "Aufgabe 8", "Einzelleistung ohne KI – zählt für die Note", s6_a4),
     ("s6_bespr", [4], "BESPRECHEN", None, "Rechenwege und Denkfehler ein letztes Mal", s6_bespr),
     ("s6_ende", [5, 6, 7], "ABGABE", "Abgabe", "Auflösung, Selbsteinschätzung, PDF; Reserve", s6_ende)],
}
for _std, _sp in SPEC.items():
    _alle = sorted({i for x in _sp for i in x[1]})
    assert _alle == list(range(len(phasen(_std)))), (_std, _alle, len(phasen(_std)))

DANACH_STUNDE = {1: "Stunde 2 · Thema erarbeiten, Versuch planen", 2: "Stunde 3 · Versuch machen", 3: "Stunde 4 · Steckbrief und Probe",
                 4: "Stunde 5 · alle Gruppen präsentieren", 5: "Stunde 6 · alles verbinden",
                 6: "Ende der Einheit – nächste Einheit: Arbeit und Energie (Buch S. 66)"}
KURZNAME = {"s1_rechnen": "Kurz klären: rechnen", "s1_bespr": "Besprechen A2", "s2_ende": "Sichern", "s3_plaetze": "Wo steht was?",
            "s4_ende": "Sichern", "s5_ende": "Abgabe", "s6_denk": "Drei Denkfehler", "s6_bespr": "Besprechen A4", "s3_ende": "Aufräumen"}


def danach_text(sp, j, std):
    if j + 1 < len(sp):
        nx = sp[j + 1]
        return nx[3] or KURZNAME.get(nx[0], nx[0])
    return DANACH_STUNDE[std]


# ================================================================ Ausgeblendete Lehrer-Folien
def folie_lehrplan():
    s = d.slide("Nur Titel", "Lehrer-Info · Lehrplanbezug", hidden=True)
    rows = [["Code", "Wortlaut", "Wo abgedeckt?"],
            ["K03", "die Grundgrößen und die entsprechenden Einheiten des SI benennen", "Aufgabe 2 c–e, Aufgabe 8 a/e/i/j, Theorie-Karte k9, Quiz 2/4/5/11"],
            ["K02 (zusätzlich)", "einfache naturwissenschaftliche Untersuchungen planen, durchführen, dokumentieren und präsentieren", "Gruppenprojekt V1.20, Stunden 2–5"],
            ["N01", "beobachten, beschreiben, berechnen, darstellen und erläutern", "Arbeitsblatt Aufgabe 5 (Versuch) und 6 (Steckbrief)"],
            ["N02", "Bedeutung für Wirtschaft, Technik und Umwelt erfassen", "Alltagsbeispiel je Gruppe, Zusatzaufgabe 11 (TU Wien)"],
            ["P8", "Gesundheit und Sicherheit", "Sicherheitsregeln, Druck unter Schuh und Schultergurt"],
            ["P7", "Quellen und Medien", "Quellenprüfung Stunde 2, Zusatzaufgabe 11"],
            ["GLV 6", "verantwortungsvoller Umgang mit Modellen und Technik", "Grenzen jedes Versuchs, keine Waffenversuche nötig"]]
    B.auto_grid(s, X0, 0.98, [1.5, 3.6, 3.9], rows, size=12, minh=0.26)
    B.tb(s, X0, 4.62, W, 0.38, [[("Jahresplan: ", {"bold": True, "color": RUST}),
                                 ("Block »E Physik«, E15–E17 = 7 Stunden laut bloecke.json. Hier sind SECHS Stunden geplant – die Lehrer-Seite meldet deshalb eine Abweichung von einer Stunde.", {})]], size=11, after=0)
    return s


def folie_herrichten():
    s = d.slide("Nur Titel", "Lehrer-Info · Vorbereitung (Stunde 3)", hidden=True)
    B.tb(s, X0, 0.92, W, 0.34, [[("Die Gruppen wählen ihren Versuch selbst. ", {"bold": True, "color": RUST}),
                                 ("Was du wirklich brauchst, steht auf den freigegebenen Materiallisten (Stunde 2). Hier die Saal-Grundausstattung je Thema:", {})]], size=11, after=0)
    rows = [["Gr.", "Thema", "Im Saal bereitlegen (Inventar-Nr., Bestand)"]]
    for n in range(1, 8):
        g = GD.G[n]; rows.append([str(n), g["thema"], " · ".join("%s %s" % (a, b) for a, b, c in g["saal"])])
    size = 11
    while size > 8 and B.table_h([0.5, 1.8, 6.7], rows, size=size, minh=0.2) > 3.2: size -= 1
    cells, h = B.auto_grid(s, X0, 1.3, [0.5, 1.8, 6.7], rows, size=size, minh=0.2)
    B.tb(s, X0, 1.32 + h, W, 0.5, [[("Knapp: ", {"bold": True, "color": RUST}),
                                    ("nur 3 Kraftmesser (#51, #52, #26) für bis zu vier Gruppen (2, 3, 4, 7) – bei der Freigabe verteilen, Gummiband-Kraftmesser als Ausweg.", {})]], size=11, after=0)
    return s


def folie_vorversuche():
    s = d.slide("Nur Titel", "Lehrer-Info · Vor der Stunde und offene Punkte", hidden=True)
    items = ["**Stunde 1:** Gruppen mit dem Generator der Lösungsseite auslosen (Reiter »Gruppen«, Namenslisten einmal einfügen) und am Beamer zeigen.",
             "**Teams:** Einen Kanal oder Ordner je Klasse für die Steckbriefe (Handouts) bereitstellen – bis Stunde 4.",
             "**Stunde 2:** Materiallisten bei der Freigabe abfotografieren oder im Arbeitsblatt-Stand der Schriftführung ansehen. Daraus richtest du Stunde 3 her.",
             "**Stunde 3:** Nur das freigegebene Saal-Material bereitlegen. Wer Material von zu Hause vergisst, nimmt Idee 1 der Gruppenkarte (Saal-Variante).",
             "**Kraftmesser** gibt es nur dreimal (#51, #52, #26). Bei der Freigabe festlegen, welche Gruppe wann misst.",
             "**Gang für Gruppe 1** vorher ansehen: 5 m frei, kein Durchgangsverkehr.",
             "**Einheit einblenden**, wenn es losgeht: GitHub → Actions → »Einheit ein-/ausblenden« → 1ab-nawi/k2-1-kraefte."]
    B.tb(s, X0, 0.95, W, 3.5, ["· " + x for x in items], size=13, after=5)
    return s


def folie_kuerzen():
    s = d.slide("Nur Titel", "Lehrer-Info · Wenn eine Stunde ausfällt", hidden=True)
    rows = [["Stunde", "Was zuerst wegfällt"]]
    for n in sorted(P.KUERZEN): rows.append([str(n), P.KUERZEN[n]])
    B.auto_grid(s, X0, 0.95, [1.0, 8.0], rows, size=11, minh=0.24)
    B.tb(s, X0, 4.6, W, 0.4, [[("Nie zwei Stunden in eine pressen und nichts als Hausübung auslagern. ", {"bold": True, "color": RUST}),
                               ("Supplierstunde möglich: Stunde 6 (kein Material, kein Versuch).", {})]], size=12, after=0)
    return s


def folie_referat():
    s = d.slide("Nur Titel", "Lehrer-Info · Referat oder Doppelstunde", hidden=True)
    rows = [["Stunde", "Fällt ein Referat (%d min) in die Stunde, ändert sich:" % P.REFERAT_MIN]]
    for n in sorted(P.STUNDE): rows.append([str(n), P.kuerzen_text(n)])
    size = 11
    while size > 8 and B.table_h([0.8, 8.2], rows, size=size, minh=0.2) > 2.8: size -= 1
    cells, h = B.auto_grid(s, X0, 0.95, [0.8, 8.2], rows, size=size, minh=0.2)
    txt = ("Klassenbuch, »Weißt du noch?«, Zwischenstand-PDF und Reserve gibt es nur einmal – das ergibt 11 bis 15 Minuten, in die ein Referat passt. "
           "Bei Stunde 2 + 3: Material von zu Hause kann nicht mitgebracht werden, alle nehmen die Saal-Variante (Idee 1).")
    hh = B.th("Doppelstunde: " + txt, 11, W, pad=0.04)
    B.tb(s, X0, 1.0 + h, W, hh, [[("Doppelstunde: ", {"bold": True, "color": RUST}), (txt, {})]], size=11, after=0)
    B.tb(s, X0, 1.05 + h + hh, W, 0.3, [[("Die fertigen Abläufe je Termin stehen im Reiter »Kalender« der Lösungsseite. ", {"bold": True, "color": OLIVE}),
                                         ("Dauert ein Referat länger: zuerst die Reserve nehmen.", {})]], size=11, after=0)
    return s


def folien_ausgleich():
    """Ausgeblendete Folien für die Klasse, die vorne liegt (Präsentation »Ausgleich«)."""
    out = []
    for b in AG.BAUSTEINE:
        s = d.slide("Nur Titel", "Ausgleich %s · %s" % (b["id"], b["titel"]), hidden=True)
        w = 6.9 if b["id"] == "A4" else W
        y = schritte(s, X0, 1.0, w, b["tun"], size=18, farbe=FARBE.get(b["marke"], OLIVE))
        merke(s, y + 0.04, "Ergebnis: " + b["ergebnis"].split(". ")[0].rstrip(".") + ".", size=16, w=w)
        if b["id"] == "A4": qr(s, "quiz", 7.9, 1.0, 1.1, "Kräfte-Check")
        hinweis(s, b["marke"], "ca. %d min" % b["min"], "freiwillig · keine Note")
        check(s); out.append(s)
        if b["id"] == "A1":
            s2 = d.slide("Nur Titel", "Ausgleich A1 · Die Behauptungen", hidden=True)
            schritte(s2, X0, 1.0, W, [a for a, r in AG.AUSSAGEN], size=18, farbe=ORANGE)
            hinweis(s2, "DISKUSSION", "ca. 3 min je Behauptung", "Auflösung steht in der Lösungsseite")
            check(s2); out.append(s2)
    return out


def folie_quellen():
    s = d.slide("Nur Titel", "Lehrer-Info · Quellen und was nicht geprüft ist", hidden=True)
    zeilen = ["· Inhalt und Zeiten: dieselbe Datenquelle wie Theorie-Seite, Arbeitsblatt und Lösungsseite (werkzeug/quellen/1ab-k2-1-kraefte)."]
    zeilen += ["· %s – %s (%s)" % (q[0], q[1], q[2]) for q in I.QUELLEN[:6]]
    zeilen += ["· Nicht geprüft: " + x for x in I.NICHT_GEPRUEFT[:3]]
    B.tb(s, X0, 0.95, W, 3.6, zeilen, size=11, after=4)
    return s


def folie_bedienung(nr_regie):
    s = FOLIE["bedien"]
    B.tb(s, X0, 0.95, W, 3.8, [
        [("Eine Datei für beide Klassen. ", {"bold": True, "color": OLIVE}), ("1AK und 1BK haben denselben Fahrplan und keine Daten – Termine und Referate trägst du in der Lösungsseite ein.", {})],
        [("Pro Stunde starten: ", {"bold": True, "color": OLIVE}), ("Bildschirmpräsentation → Benutzerdefinierte Bildschirmpräsentation → »Stunde 1« bis »Stunde 6«. Ohne Menü: im Vortrag die Foliennummer tippen und Enter (die Nummern stehen auf den Regie-Folien).", {})],
        [("Jede Stunde läuft gleich: ", {"bold": True, "color": OLIVE}), ("»Heute« → »Weißt du noch?« → Arbeitsauftrag (Marke: SELBSTSTUDIUM, GRUPPENARBEIT, VERSUCH …) → »Das besprechen wir« → Sichern.", {})],
        [("Unten links ", {"bold": True, "color": OLIVE}), ("steht immer, was JETZT läuft (mit Minuten aus dem Zeitplan) und was DANACH kommt – so sehen auch die Kadetten den Ablauf.", {})],
        [("Antworten erscheinen per Klick. ", {"bold": True, "color": OLIVE}), ("Erst nach der Arbeitszeit klicken, sonst lesen die Kadetten mit.", {})],
        [("Ausgeblendet: ", {"bold": True, "color": OLIVE}), ("Regie je Stunde (Folien %s), Lehrplanbezug, Vorbereitung, offene Punkte, Kürzungsliste, Referat/Doppelstunde und Quellen (Präsentation »Lehrer-Regie«). Ausgleich für die Klasse, die vorne liegt: Präsentation »Ausgleich«." % nr_regie, {})],
        [("Die Kadetten arbeiten am Handy. ", {"bold": True, "color": OLIVE}), ("Diese PPP ersetzt die Seiten nicht – sie führt durch die Stunde. Lösungen stehen in der privaten Lösungsseite, nicht hier.", {})]],
        size=13, after=5)
    return s


# ================================================================ Deck bauen
def bauen():
    global d
    d = B.Deck(True, "NAWI · 1AB · K2.1 · Unterricht"); B.d = d
    d.section("Start")
    s = d.slide("Titelfolie", "Mechanische Kräfte")
    for ph in s.placeholders:
        if ph.placeholder_format.type == 2:
            B.text(ph, ["NAWI · 1AB · K2.1 · Unterrichts-PPP: sechs Stunden, Gruppenprojekt mit selbst gewähltem Versuch · Buch S. 44–65",
                        [("Stand %s · %s · TH-Unterricht (Ablauf)" % (I.STAND, I.V), {"size": 12})]], size=18, color=RGBColor.from_string("C9D6B0"))
    titel = s
    FOLIE["bedien"] = d.slide("Nur Titel", "Lehrer-Info · So führt die PPP", hidden=True)
    lehrplan = folie_lehrplan()
    herrichten = folie_herrichten()
    vorversuche = folie_vorversuche()
    kuerzen = folie_kuerzen()
    referat = folie_referat()
    regie = {std: d.slide("Nur Titel", "Regie · Stunde %d" % std, hidden=True) for std in sorted(SPEC)}
    quellen = folie_quellen()
    for std in sorted(SPEC):
        d.section("Stunde %d" % std)
        sec = d.slide("Abschnitt", I.STUNDENNAME[std])
        for ph in sec.placeholders:
            if ph.placeholder_format.type == 2: ph.text_frame.text = METHODE_KURZ[std]
        FOLIE["sec%d" % std] = sec
        sp = SPEC[std]
        for j, (key, idx, art, schritt, wozu, fn) in enumerate(sp):
            sl = fn(); FOLIE[key] = sl
            hinweis(sl, art, minuten(std, idx), danach_text(sp, j, std))
            B.pill(sl, "Buch S. 44–65", w=2.3)
            check(sl)

    # ---------------- Regie-Folien mit Foliennummern
    nr_von = {sl.slide_id: i + 1 for i, sl in enumerate(d.p.slides)}
    NR = lambda key: nr_von[FOLIE[key].slide_id]
    for std in sorted(SPEC):
        sl = regie[std]
        rows = [["Minute", "Was läuft jetzt?", "Folie", "Wozu?"]]
        zu = {}
        for key, idx, art, schritt, wozu, fn in SPEC[std]:
            for i in idx: zu.setdefault(i, []).append((key, wozu))
        t0 = 0
        for i, (name, mi, oh, a) in enumerate(phasen(std)):
            keys = [x for x, _ in zu[i]]
            fol = ", ".join(dict.fromkeys(str(NR(x)) for x in keys))
            wz = zu[i][0][1] if a != "reserve" else "Puffer – nicht verplanen"
            rows.append(["%d–%d" % (t0, t0 + mi), name + (" · ohne Handy" if oh and a not in ("org", "reserve", "bespr", "wdh") else ""), fol, wz]); t0 += mi
        assert t0 == P.MIN, (std, t0)
        B.tb(sl, X0, 0.94, W, 0.3, [[("Stunde %d · %s · Methode: %s · Benutzerdefinierte Präsentation »Stunde %d«" % (std, I.STUNDENNAME[std].split(" · ")[1], P.METHODE[std], std), {"bold": True, "color": RUST})]], size=11, after=0)
        kn = P.KUERZEN[std]
        hk = B.th("Wenn es knapp wird: " + kn, 10, W, pad=0.04)
        size = 11
        while size > 8 and B.table_h([0.8, 4.2, 0.7, 3.3], rows, size=size, minh=0.2) + hk > 3.85: size -= 1
        cells, h = B.auto_grid(sl, X0, 1.24, [0.8, 4.2, 0.7, 3.3], rows, size=size, minh=0.2)
        B.tb(sl, X0, 1.26 + h, W, hk, [[("Wenn es knapp wird: ", {"bold": True, "color": RUST}), (kn, {})]], size=10, after=0)
    folie_bedienung("%d–%d" % (nr_von[regie[1].slide_id], nr_von[regie[6].slide_id]))
    d.section("Ausgleich")
    ausgleich = folien_ausgleich()

    # ---------------- benutzerdefinierte Präsentationen
    pres = d.p.part._element
    csl = etree.Element("{%s}custShowLst" % NS_P)
    anker = pres.find("{%s}defaultTextStyle" % NS_P)
    if anker is not None: anker.addprevious(csl)
    else: pres.append(csl)
    rid = {sl.slide_id: el.get("{%s}id" % NS_R) for sl, el in zip(d.p.slides, d.p.slides._sldIdLst)}
    nid = [0]

    def show(name, folien):
        cs = etree.SubElement(csl, "{%s}custShow" % NS_P, name=name, id=str(nid[0])); nid[0] += 1
        l = etree.SubElement(cs, "{%s}sldLst" % NS_P)
        for sl in folien: etree.SubElement(l, "{%s}sld" % NS_P).set("{%s}id" % NS_R, rid[sl.slide_id])

    folgen = {std: [FOLIE["sec%d" % std]] + [FOLIE[x[0]] for x in SPEC[std]] for std in sorted(SPEC)}
    show("Alle sechs Stunden", [titel] + sum([folgen[std] for std in sorted(SPEC)], []))
    for std in sorted(SPEC):
        show("Stunde %d" % std, ([titel] if std == 1 else []) + folgen[std])
    show("Lehrer-Regie", [FOLIE["bedien"], lehrplan, herrichten, vorversuche, kuerzen, referat] + [regie[s_] for s_ in sorted(regie)] + [quellen])
    show("Ausgleich", ausgleich)

    os.makedirs(ZIEL, exist_ok=True)
    name = "%s-TH-Unterricht-%s.pptx" % (I.PRAEFIX, I.V)
    d.save(os.path.join(ZIEL, name))
    sicht = [sl for sl in d.p.slides if sl._element.get("show") != "0"]
    for x in PROBLEME: print("ÜBERLAUF", x)
    print("ok", name, "·", len(d.p.slides._sldIdLst), "Folien,", len(sicht), "sichtbar ·", nid[0], "Präsentationen")
    for std in sorted(SPEC):
        print("  Stunde %d: Folien %s · %d min" % (std, [nr_von[x.slide_id] for x in folgen[std]], sum(p[1] for p in phasen(std))))
    return os.path.join(ZIEL, name)


if __name__ == "__main__":
    bauen()
