"""Zeitplan K2.4/K3.2 Akustik und Gehör – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Beamer-Präsentation (Phasenleiste, Regie) und Lehrerseite.
Standards 07.11.–13.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Vier Einzelstunden, jede ist abgeschlossen.
KEINE DATEN in dieser Quelle: Termine stehen nur privat im Kalender der Lehrerseite.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "demo" · "erkl" KURZ KLÄREN · "wdh" Weißt du noch? ·
"bespr" BESPRECHEN · "partner" · "selbst" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE
REFERAT_MIN = 10
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen aus der Wellenlehre", 2, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("DEMO K2.4-D1: Stimmgabel – erst vermuten, dann sehen, hören, spüren", 6, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Schall ist eine Druckwelle (Animation), Vakuum", 6, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Schall unterwegs", 6, False, "a2", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: s = v · t, Echo hin und zurück, λ = v / f", 4, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Rechnen mit Schall", 10, False, "a3", "SELBSTSTUDIUM"),
     ("BESPRECHEN: die Echo-Falle und die Faustregel", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K2.4-D2: Lineal an der Tischkante, Tongenerator am Beamer", 6, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Hörbereich, Infra- und Ultraschall, Dezibel-Leiter", 6, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 4: Die Dezibel-Leiter", 7, False, "a4", "SELBSTSTUDIUM"),
     ("VERSUCH K2.4-V1 (Aufgabe 5): Referenz am Lehrertisch, Messung am eigenen Platz", 14, False, "a5", "VERSUCH"),
     ("BESPRECHEN: Messwerte der Klasse am Beamer", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Aufbau des Ohrs, Hörvorgang (Animation), Druckverstärkung", 7, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 6: Der Weg ins Ohr", 10, False, "a6", "SELBSTSTUDIUM"),
     ("VERSUCH K3.2-V1 (Aufgabe 7): Luft- und Knochenleitung am eigenen Kopf", 5, True, "a7", "VERSUCH"),
     ("KURZ KLÄREN: Haarzellen, Knalltrauma, Tinnitus, Gehörschutz", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 8: Statement-Check Noise-Cancelling", 6, False, "a8", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Antwort an den Influencer", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K3.2-D1: Woher kommt das Schnippen? (Augen zu)", 6, True, "demo", "DEMO"),
     ("DEMO K3.2-D2: drehendes Wasserglas + KURZ KLÄREN Lage- und Drehsinn", 7, True, "demo", "DEMO"),
     ("Aufgabe 9: Orientierung – Richtung und Gleichgewicht", 12, False, "a9", "SELBSTSTUDIUM"),
     ("BESPRECHEN: der Pilotenfall", 4, True, "bespr", "BESPRECHEN"),
     ("PARTNERCHECK: vier Karten über die ganze Einheit", 4, True, "partner", "PARTNERCHECK"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Demo mit Vorhersage per Handzeichen, Rechnen in Einzelarbeit",
           2: "Messrunde durch den langen Saal – Handy nur als Messgerät, Bewegung",
           3: "Selbstversuch am eigenen Kopf, Statement-Check",
           4: "Mitmach-Demos mit Augen zu, Partnercheck ohne Handy"}

ZIEL = {1: "Erklären, was beim Schall wandert – und mit s = v · t Entfernungen berechnen.",
        2: "Tonhöhe und Lautstärke den richtigen Größen zuordnen und Dezibel-Werte richtig deuten.",
        3: "Den Weg vom Trommelfell bis zur Haarzelle erklären – und wissen, was das Gehör wirklich schützt.",
        4: "Erklären, wie wir Richtungen hören und Lage und Drehung spüren – und wo uns das täuscht."}

MARKE = {1: "DEMO", 2: "VERSUCH", 3: "SELBSTSTUDIUM", 4: "DEMO"}
PLAN = {k: [{"std": n, "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}

# ---------------------------------------------------------------- Kontrollen
_Z = {t["nr"]: t["zeit"] for t in I.T}
for n, ph in STUNDE.items():
    assert sum(p[1] for p in ph) == MIN, (n, sum(p[1] for p in ph))
    assert sum(p[1] for p in ph if p[3] in ("org", "reserve")) == ORG_RESERVE, (n, "Organisation und Reserve nicht 10 min")
    assert sum(p[1] for p in ph if p[3] == "reserve") >= 5, (n, "zu wenig Reserve")
    assert any(p[2] for p in ph if p[3] not in ("org", "reserve")), (n, "keine Phase ohne Handy")
_m = [METHODE[n] for n in sorted(METHODE)]
assert all(a != b for a, b in zip(_m, _m[1:])) and len(set(_m)) >= 3
_einmal = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art, mk in ph:
        if re.match(r"a\d+$", art):
            _einmal.setdefault(int(art[1:]), []).append((n, mi))
for nr, lst in _einmal.items():
    t = [x for x in I.T if x["nr"] == nr][0]
    assert len(lst) == 1 and lst[0][1] == _Z[nr] and lst[0][0] == t["h"], (nr, lst, _Z[nr], t["h"])
assert sorted(_einmal) == list(range(1, 10)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: DEMO K2.4-D1 nur mit Wasser und Tisch (ohne Resonanzkasten), Aufgabe 3 e) wird Zusatz. Die Echo-Rechnung c) bleibt – sie ist der häufigste Fehler.",
 2: "Zeitstopp für den Versuch: Minute 34 – egal wie weit. Wenn es knapp wird: Grundgeräusch (c) weglassen, nur »Ton an« messen; Aufgabe 4 f) wird Zusatz. "
    "Geht das Handy-Mikrofon nicht: Gruppe schreibt die Werte einer Nachbargruppe ab (im Protokoll vermerken).",
 3: "Supplierstunde möglich: Aufgabe 6, der Mini-Versuch und Aufgabe 8 brauchen kein Material; die Theorie-Karten und die Hörvorgang-Animation stehen im Arbeitsblatt bzw. auf der Theorie-Seite. "
    "Wenn es knapp wird: Das Besprechen der Influencer-Antwort an den Anfang von Stunde 4 legen.",
 4: "Wenn es knapp wird: DEMO K3.2-D1 auf drei Durchgänge kürzen, der Partnercheck entfällt. "
    "Die PDF-Abgabe darf bis zum Ende des Tages nachgeholt werden.",
}
AUSFALL = ("Fällt eine der vier Stunden aus: Stunden 1 und 2 werden zu einer zusammengelegt – DEMO K2.4-D1 nur 3 min (Wasser), Aufgabe 3 nur a) und c), "
           "der Versuch K2.4-V1 wird zur 5-min-DEMO (Prof. HOLZER misst mit einem Handy bei 1, 2, 4 und 8 m, die Klasse notiert), Aufgabe 4 bleibt. "
           "Stunden 3 und 4 bleiben unverändert, weil K07 (Ohr, Gleichgewicht) sonst nicht abgedeckt ist. Keine Hausübung.")
SUPPLIER = 3

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN); Organisation, Reserve, Pflichtaufgaben und Versuche bleiben
 1: {1: 0, 3: 4, 4: 4, 6: 2, 8: 1},
 2: {1: 0, 2: 3, 3: 4, 6: 1},
 3: {1: 0, 2: 5, 5: 3, 7: 0},
 4: {1: 0, 2: 4, 3: 6, 5: 2, 6: 2},
}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit")
    assert all(STUNDE[_n][i][3] not in ("org", "reserve") for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
DOPPEL_HINWEIS = {(1, 2): "Gut: Rechnen und Messen hintereinander. Lautsprecher und Maßband stehen schon.",
                  (2, 3): "Gut: Vom Pegel direkt ins Ohr. Nach dem Versuch Handys wegräumen lassen.",
                  (3, 4): "Gut: Ohr, Schutz und Gleichgewicht am Stück. Wasserglas schon vorher füllen."}


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art, mk) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]; note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
        z.append([name, neu, bool(oh), art, note, mk])
    return z


def variante(a, doppel=False, referat=False):
    """Ablauf als Liste [Name, Minuten, ohne Handy, Art, Hinweis, Marke]. Einzelstunde 50 min, Doppelstunde 105 min mit Pause."""
    ref = ["Referat einschließlich kurzer Rückfragen", REFERAT_MIN, True, "referat", "", ""]
    if not doppel:
        z = _zeilen(a, REF_KUERZEN[a] if referat else None)
        if referat: z.insert(1, ref)
        assert sum(r[1] for r in z) == MIN, (a, referat)
        return z
    b = a + 1
    za = [r for r in _zeilen(a) if r[3] not in ("pdf", "reserve")]
    zb = [r for r in _zeilen(b)[1:] if r[3] != "wdh"]
    z = za + [["Pause (keine Arbeitszeit)", PAUSE, True, "pause", "", ""]] + zb
    if referat: z.insert(1, ref)
    rest = DOPPEL_MIN - sum(r[1] for r in z)
    assert rest >= 0, (a, referat, rest)
    if rest: z.append(["Puffer oder ein Ausgleichsbaustein" if rest >= 10 else "Puffer", rest, True, "reserve", "", ""])
    assert sum(r[1] for r in z) == DOPPEL_MIN
    return z


VARIANTEN = {}
for _n in sorted(STUNDE):
    for _r in (False, True):
        VARIANTEN["%d%s" % (_n, "R" if _r else "")] = variante(_n, False, _r)
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = variante(_n, True, _r)


def aufgaben_der(n):
    return sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


LESEN = {1: "DEMO Stimmgabel · Druckwelle · Theorie-Karten 1 und 2 · Buch S. 61",
         2: "DEMO Lineal und Tongenerator · Dezibel-Leiter · VERSUCH Schallpegel messen · Buch S. 63–64",
         3: "Aufbau des Ohrs, Hörvorgang · Mini-Versuch am eigenen Kopf · Gehörschutz · Buch S. 109–110",
         4: "DEMOS Richtungshören und Wasserglas · Lage- und Drehsinn · Partnercheck · Buch S. 110–112"}
ABGABE = {1: "–", 2: "Messwerte deiner Gruppe eintragen", 3: "–", 4: "Arbeitsblatt-PDF in LMS"}


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        z.append({"wann": f"Stunde {n}", "marke": MARKE[n], "lesen": LESEN[n], "aufgaben": auf, "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Echolot und Fledermaus, KI-Fehlerjagd, Gehörschutz-Briefing (Podcast oder Plakat)",
              "aufgaben": "Zusatz 10–12", "zeit": "ca. 34 min", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Vier Stunden, ein Weg: vom Knall zum Kopf. Stunde 1 Schall und Tempo, Stunde 2 messen in Dezibel, Stunde 3 das Ohr und sein Schutz, "
                 "Stunde 4 Richtung und Gleichgewicht. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. Keine Hausübung. "
                 "Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
    print(len(VARIANTEN), "Varianten")
