"""Zeitplan K3.1/K3.6 Herz-Kreislauf + Stützsystem und Ergonomie (3AB) – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Beamer-Präsentation (Phasenleiste, Regie) und Lehrerseite.
Standards 07.11.–20.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Fünf Einzelstunden, jede ist abgeschlossen.
KEINE DATEN in dieser Quelle: Termine stehen nur privat im Kalender der Lehrerseite (Startwerte: Mo 23.11., Mi 25.11., Mo 30.11., Mi 02.12., Mi 09.12.2026, 3AK und 3BK).
Referate (Stephan 20.11.2026, je 10 min mit Brücke): 3AK Stunde 1 »Ernährungstrends«, 3AK Stunde 3 »Looksmaxing«, 3BK Stunde 3 »Peptide«.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "demo" · "erkl" KURZ KLÄREN · "wdh" Weißt du noch? ·
"bespr" BESPRECHEN · "partner" · "selbst" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE
REFERAT_MIN = 10   # Stephan 20.11.2026: je 10 min mit Brücke (einschließlich Rückfragen)
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Folie »Neue Einheit«, Handys bereit", 5, True, "org", ""),
     ("Weißt du noch? Drei Fragen aus der Ernährung", 2, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("DEMO K3.1-D1: Das Herz im Torso – erst vermuten, dann herausnehmen", 5, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Vier Räume, Klappen, Systole und Diastole (Animation)", 6, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Das Herz – lesen im Buch S. 77, dann Weg des Blutes", 9, False, "a2", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Lungen- und Körperkreislauf (Animation)", 4, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Kreislauf-Schema per Hand zeichnen und fotografieren", 6, True, "a3", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Sicherung Herz und Kreislauf", 5, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 5, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Arterie, Vene, Kapillare – Puls und Blutdruck", 5, True, "erkl", "BESPRECHEN"),
     ("DEMO K3.1-D2: Venenklappen am Unterarm", 3, True, "demo", "DEMO"),
     ("VERSUCH K3.1-V1 (Aufgabe 4): Puls in Ruhe, nach 20 Kniebeugen, nach 3 Minuten", 15, False, "a4", "VERSUCH"),
     ("Aufgabe 5: Gefäße und Herzminutenvolumen rechnen", 8, False, "a5", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Pulswerte der Klasse (ohne Namen) und Rechnung", 5, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K3.6-D1: Skelett-Modell – leicht und stabil", 5, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Bau des Knochens, Sehne, Band, Knorpel, Gelenktypen", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 6: Bauplan – lesen im Buch S. 108, dann zuordnen", 8, False, "a6", "SELBSTSTUDIUM"),
     ("GRUPPENARBEIT (Aufgabe 7): Skelett-Rallye am Modell und am eigenen Körper", 13, True, "a7", "GRUPPENARBEIT"),
     ("BESPRECHEN: Sicherung Bauplan und Gelenktypen", 5, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3", 4, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Blut aus dem Knochenmark – Bestandteile, Gerinnung, Blutgruppen (Animation)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 8: Blut im Labor – Bestandteile, Befund, Blutgruppen", 14, False, "a8", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Blutgruppen und Konserven sichern", 3, True, "bespr", "BESPRECHEN"),
     ("KURZ KLÄREN: EPO und Hämatokrit – Rollenkarten verteilen", 2, True, "erkl", "BESPRECHEN"),
     ("GRUPPENARBEIT (Aufgabe 9): Blutdoping mit Rollenkarten", 7, False, "a9", "GRUPPENARBEIT"),
     ("DISKUSSION: Prof. HOLZER fragt die Rollen – Radprofi, Ärztin, NADA, Nachwuchs", 4, True, "bespr", "DISKUSSION"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 5: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 4", 4, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Spieler und Gegenspieler (mitmachen), Muskelfasern, ATP", 5, True, "erkl", "BESPRECHEN"),
     ("DEMO K3.6-D2: Richtig heben – Rucksack nah oder weit weg", 4, True, "demo", "DEMO"),
     ("Aufgabe 10: Muskeln, Hebel und Ergonomie-Check am eigenen Platz", 12, False, "a10", "SELBSTSTUDIUM"),
     ("Aufgabe 11: Mindmap »Körper unter Belastung« per Hand", 7, True, "a11", "SELBSTSTUDIUM"),
     ("PARTNERCHECK: vier Karten über die ganze Einheit", 4, True, "partner", "PARTNERCHECK"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Aufgaben-PDF in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Demo am Torso mit Vorhersage (ABCD-Karte), Kreislauf-Skizze per Hand",
           2: "Pulsversuch zu zweit mit Kniebeugen – Bewegung, Handy nur als Stoppuhr",
           3: "Gruppenarbeit am Skelett-Modell und am eigenen Körper, Kurzpräsentation",
           4: "Rollenkarten und Diskussion zum Blutdoping",
           5: "Mitmach-Selbstversuch, Ergonomie-Check am eigenen Platz, Mindmap per Hand, Partnercheck"}

ZIEL = {1: "Erklären, wie das Herz mit vier Räumen und Klappen das Blut durch zwei Kreisläufe pumpt.",
        2: "Den Puls messen, Werte vor und nach Belastung deuten und das Herzminutenvolumen berechnen.",
        3: "Bau des Knochens, Sehne, Band, Knorpel und die drei Gelenktypen am Skelett zeigen.",
        4: "Bestandteile des Blutes und Blutgruppen erklären – und begründen, warum EPO-Doping gefährlich ist.",
        5: "Spieler und Gegenspieler erklären, richtig heben und den eigenen Arbeitsplatz ergonomisch prüfen."}

MARKE = {1: "DEMO", 2: "VERSUCH", 3: "GRUPPENARBEIT", 4: "GRUPPENARBEIT", 5: "DEMO"}
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
assert sorted(_einmal) == list(range(1, 12)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: DEMO K3.1-D1 nur Herz zeigen (nicht ganz zerlegen), Aufgabe 2 b) wird Zusatz. Das Schema per Hand (Aufgabe 3) bleibt – es ist die Grundlage für alles Weitere.",
 2: "Zeitstopp für den Versuch: spätestens Minute 30 der Stunde. Wenn es knapp wird: nur Ruhepuls und Puls direkt nach den Kniebeugen, die 3-Minuten-Messung entfällt (d) leer lassen, im Protokoll vermerken). "
    "Aufgabe 5 f) wird Zusatz. Geht der Versuch gar nicht (zu wenige dürfen mitmachen): Prof. HOLZER misst an zwei Freiwilligen, die Klasse notiert.",
 3: "Wenn es knapp wird: Die Kurzpräsentation am Skelett nur für drei Gruppen; Aufgabe 6 h) wird Zusatz. Die Gelenktypen (Aufgabe 7 c–h) bleiben Pflicht.",
 4: "Supplierstunde möglich: Aufgabe 8 und die Rollenkarten-Gruppenarbeit (Aufgabe 9) brauchen kein Material; Theorie-Karten und die Gerinnungs-Animation stehen bei den Aufgaben bzw. auf der Theorie-Seite. "
    "Wenn es knapp wird: Aufgabe 8 e) und f) (Befund) werden Zusatz, die Diskussion entfällt – die Rollen schreiben nur d).",
 5: "Wenn es knapp wird: DEMO K3.6-D2 kürzer (nur Rucksack nah/weit, ohne Heben), der Partnercheck entfällt. Die PDF-Abgabe darf bis zum Ende des Tages nachgeholt werden.",
}
AUSFALL = ("Fällt eine der fünf Stunden aus: Stunden 4 und 5 werden zu einer zusammengelegt – Aufgabe 8 nur a)–d) und g)–k), die Doping-Gruppenarbeit (Aufgabe 9) wird Zusatz, "
           "DEMO K3.6-D2 nur 2 min, Aufgabe 10 nur a), b), e), h), i). Stunden 1–3 bleiben unverändert (Herz, Versuch und Gelenke sind die Kerne von K06/K07). Keine Hausübung.")
SUPPLIER = 4

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde

SICHERUNG_TEILE = {1: [(2, ["klappen", "links", "wand"]), (3, ["arterie"])], 2: [(4, ["warum", "diagnose"]), (5, ["hmv", "druck"])],
                   3: [(6, ["band", "sehne", "fuge"]), (7, ["schulter", "ellbogen", "speiche"])], 4: [(8, ["bg1", "empf0", "empfab"]), (9, ["epo", "risiko"])],
                   5: [(10, ["gegen", "nah", "schirm"])]}


def buchstaben_roh(nr, ids):
    t = next(x for x in I.T if x["nr"] == nr)
    return [re.match(r"([a-z])\)", next(f for f in t["fields"] if f[0] == fid)[1]).group(1) for fid in ids]


REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN = 10). Organisation, Reserve und PDF bleiben;
 # Aufgaben dürfen gekürzt werden (der Rest wird für diese Klasse Zusatz, siehe REF_NOTIZ). Nie zwei Stunden in eine pressen, keine Hausübung.
 1: {1: 0, 3: 3, 4: 5, 5: 7, 6: 3, 8: 3},
 2: {1: 0, 2: 4, 3: 2, 4: 13, 5: 6, 6: 4},
 3: {1: 0, 2: 3, 3: 4, 4: 7, 5: 11, 6: 4},
 4: {1: 0, 2: 4, 3: 12, 4: 2, 7: 2},
 5: {1: 0, 2: 4, 3: 3, 4: 11, 6: 1},
}
REF_BLEIBT = {   # bei Referat-Kürzung bleiben von dieser Aufgabe nur diese Teile Pflicht – alles, was wir sichern, muss dabei sein
 (1, 5): "acdefghijk", (2, 4): "abcdfg", (2, 5): "abdg", (3, 4): "abcdefg", (3, 5): "abcdefgh", (4, 3): "abcdghijk", (5, 4): "abefghi"}
REF_NOTIZ = {   # was bei Referat-Kürzung von einer Phase bleibt
 (1, 3): "nur Herz herausnehmen und Lage zeigen",
 (2, 2): "Blutdruck nur in einem Satz",
 (3, 2): "nur Oberschenkelknochen am Skelett zeigen, Rest in der Gruppenarbeit",
 (3, 5): "Kurzpräsentation nur drei Gruppen",
 (4, 7): "nur zwei Rollen fragen",
 (5, 3): "nur Rucksack nah und weit, ohne Heben",
 (5, 6): "nur eine Karte",
}
for (_n, _i), _b in REF_BLEIBT.items():
    _gr = []
    for _x in _b:
        if _gr and ord(_x) == ord(_gr[-1][-1]) + 1: _gr[-1].append(_x)
        else: _gr.append([_x])
    REF_NOTIZ[(_n, _i)] = "Pflicht nur " + ", ".join(g[0] + ")" if len(g) == 1 else (g[0] + "), " + g[1] + ")" if len(g) == 2 else g[0] + ")–" + g[-1] + ")") for g in _gr) + " – der Rest wird Zusatz"
    _nr = int(STUNDE[_n][_i][3][1:])
    for _nr2, _ids in SICHERUNG_TEILE[_n]:
        if _nr2 == _nr:
            _fehlt = [x for x in buchstaben_roh(_nr, _ids) if x not in _b]
            assert not _fehlt, (_n, _nr, "gesicherte Teile wären bei Referat Zusatz", _fehlt)
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve", "pdf") for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
    assert all((_n, i) in REF_NOTIZ for i in _c if re.match(r"a\d+$", STUNDE[_n][i][3]) and _c[i] > 0), (_n, "Aufgabe gekürzt ohne Notiz")
DOPPEL_HINWEIS = {(1, 2): "Gut: vom Herzen direkt zum Pulsversuch. Torso danach wegräumen, damit Platz für die Kniebeugen ist.",
                  (2, 3): "Gut: Kreislauf und Knochenmark hintereinander. Skelett schon vor der Pause bereitstellen.",
                  (3, 4): "Gut: vom Knochenmark direkt zum Blut. Skelett nach der Pause wegräumen.",
                  (4, 5): "Gut: Doping-Diskussion und Muskeln am Stück. Rucksack und Gewichte vorher bereitlegen."}


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art, mk) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]; note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
            if (n, i) in REF_NOTIZ: note += " · " + REF_NOTIZ[(n, i)]
        z.append([name, neu, bool(oh), art, note, mk])
    return z


def variante(a, doppel=False, referat=False):
    """Ablauf als Liste [Name, Minuten, ohne Handy, Art, Hinweis, Marke]. Einzelstunde 50 min, Doppelstunde 105 min mit Pause."""
    ref = ["Referat mit Besprechung und Brückenfrage", REFERAT_MIN, True, "referat", "", ""]
    if not doppel:
        z = _zeilen(a, REF_KUERZEN[a] if referat else None)
        if referat: z.insert(1, ref)
        assert sum(r[1] for r in z) == MIN, (a, referat)
        return z
    b = a + 1
    za = [r for r in _zeilen(a, REF_KUERZEN[a] if referat else None) if r[3] not in ("pdf", "reserve")]   # Referat kürzt die erste Stunde
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


LESEN = {1: "DEMO Torso · Herz und Klappen · Kreislauf-Skizze per Hand · Buch S. 77–78",
         2: "Gefäße, Puls, Blutdruck · DEMO Venenklappen · VERSUCH Puls · Buch S. 79–81",
         3: "DEMO Skelett-Modell · Knochen, Sehne, Band · GRUPPENARBEIT Skelett-Rallye · Buch S. 108–110",
         4: "Blut aus dem Knochenmark · Gerinnung, Blutgruppen · GRUPPENARBEIT Blutdoping · Buch S. 81–85",
         5: "Muskeln, Spieler und Gegenspieler · DEMO Heben · Ergonomie-Check · Mindmap per Hand · Buch S. 110–113"}
# Theorie nach Stunden (Standard 20.11.2026): EINE Zuordnung Teil → Stunde für Fahrplan, Trennbalken, Übersicht, Leiste, Präsentation, Lösungsseite
THEORIE_TEILE_IDS = {1: [("herz", 1, "Herz"), ("kreislauf", 2, "Zwei Kreisläufe")], 2: [("gefaesse", 3, "Blutgefäße"), ("puls", 4, "Puls und Blutdruck")],
                     3: [("knochen", 5, "Knochen"), ("gelenke", 6, "Gelenke")], 4: [("blut", 7, "Blut"), ("blutgruppen", 8, "Blutgruppen")],
                     5: [("muskeln", 9, "Muskeln"), ("ergonomie", 10, "Ergonomie")]}
THEORIE_TEILE = {n: ", ".join(f"Teil {nr} {name}" for _id, nr, name in v) for n, v in THEORIE_TEILE_IDS.items()}
ABGABE = {1: "–", 2: "Messwerte selbst eintragen", 3: "–", 4: "–", 5: "Aufgaben-PDF in LMS"}


BUCH = {1: "Buch S. 76–78", 2: "Buch S. 79–81", 3: "Buch S. 107–110", 4: "Buch S. 81–85", 5: "Buch S. 110–114"}
DEMO_NAME = {"K3.1-D1": "Herz im Torso", "K3.1-D2": "Venenklappen", "K3.6-D1": "Skelett-Modell", "K3.6-D2": "Richtig heben"}
assert set(DEMO_NAME) == set(I.DEMOS)


def _demo(text):
    m = re.search(r"K\d\.\d-D\d", text); return m.group(0)


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan (Stephan 15.11.2026). Liste [Marke, kurzer Text]; ohne Organisation, Reserve, PDF."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        if re.match(r"a\d+$", art):
            nr = int(art[1:])
            ziel = "aufgaben.html#card_" + next(t["id"] for t in I.T if t["nr"] == nr)   # Sprungmarke (Standard 18.11.2026)
            out.append([marke, f"{marke} (Aufgabe {nr})", ziel] if marke in ("VERSUCH", "GRUPPENARBEIT") else ["", f"Aufgabe {nr}", ziel])
        elif art == "demo": out.append(["DEMO", "DEMO " + DEMO_NAME[_demo(text)]])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "bespr": out.append([marke, "Diskussion der Rollen" if marke == "DISKUSSION" else "Sicherung"])
        elif art == "partner": out.append(["PARTNERCHECK", "Partnercheck"])
        elif art == "selbst": out.append(["", "Auflösung Aufgabe 1", "aufgaben.html#card_v0"])
        else: raise ValueError(art)
    return out


# Sicherung (Stephan 15.11.2026): EINE Quelle für Präsentation, Arbeitsblatt (»Am Ende der Stunde sichern wir gemeinsam: …«), Balken, Lösungsseite.
SICHERUNG = {
 1: {"teile": SICHERUNG_TEILE[1], "auch": ["DEMO Herz im Torso"],
     "merken": ["Das Herz hat **vier Räume**. **Klappen** sind Ventile: Das Blut fließt nur in eine Richtung.",
                "**Rechts** zur **Lunge**, **links** in den **Körper**. Arterie heißt **vom Herzen weg** – nicht »sauerstoffreich«."]},
 2: {"teile": SICHERUNG_TEILE[2], "auch": ["VERSUCH: Pulswerte der Klasse"],
     "merken": ["Bei Belastung brauchen die Muskeln mehr Sauerstoff – das Herz schlägt **schneller** und pumpt mehr Blut pro Minute.",
                "**Herzminutenvolumen = Schlagvolumen · Puls**, in Ruhe rund **5 l pro Minute**. Optimaler Blutdruck: unter **120/80 mmHg**."]},
 3: {"teile": SICHERUNG_TEILE[3], "auch": ["GRUPPENARBEIT: Skelett-Rallye"],
     "merken": ["**Sehne**: Muskel–Knochen, **Band**: Knochen–Knochen, **Knorpel**: Gleiten und Dämpfen. Im **roten Knochenmark** entsteht Blut.",
                "**Kugelgelenk** (Schulter, Hüfte), **Scharniergelenk** (Ellbogen, Finger), **Drehgelenk** (Elle–Speiche, Halswirbel)."]},
 4: {"teile": SICHERUNG_TEILE[4], "auch": ["DISKUSSION der Rollen"],
     "merken": ["**Rote** Blutkörperchen: Sauerstoff · **weiße**: Abwehr · **Plättchen**: Gerinnung. Blutgruppe = **Antigene** auf den roten Blutkörperchen.",
                "Blutgruppe **0** verträgt nur **0**, **AB** verträgt alle roten Konserven. **EPO** macht das Blut dicker – Gefahr für Herz und Gehirn."]},
 5: {"teile": SICHERUNG_TEILE[5], "auch": ["DEMO Richtig heben", "PARTNERCHECK"],
     "merken": ["Muskeln **ziehen nur** – darum **Spieler und Gegenspieler** (Bizeps beugt, Trizeps streckt).",
                "Last **nah am Körper** und aus den Beinen heben. Bildschirm **nicht über Augenhöhe**, oft aufstehen und bewegen."]},
}
ANTWORT = {(5, "hmv"): "5,04 l pro Minute – 70 ml · 72 = 5040 ml"}


def buchstaben(nr, ids):
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        m = re.match(r"([a-z]\d?)\)", f[1]); out.append(m.group(1) if m else fid)
    return out


def sicherung_kurz(n):
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


def sicherung_fragen(nr, ids):
    """[(Frage, Antwort)] – Antwort aus der Prüfregel (chk.sel, nie die erste Option) oder aus ANTWORT."""
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        a = ANTWORT.get((nr, fid)) or (t.get("chk", {}).get(fid) or {}).get("sel")
        assert a, (nr, fid)
        out.append((f[1], a))
    return out


for _n in SICHERUNG:
    for _nr, _ids in SICHERUNG[_n]["teile"]:
        assert _nr in aufgaben_der(_n), (_n, _nr)
        sicherung_fragen(_nr, _ids)

BALKEN_TEXT = {"demo": "Jetzt DEMO am Lehrertisch: »{d}«. Erst vermuten – ABCD-Karte bereit, dann schauen.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "diskussion": "Jetzt DISKUSSION: Prof. HOLZER fragt jede Rolle. Danach sichern wir: {s}.",
               "partner": "Jetzt PARTNERCHECK: vier Karten zu zweit – einer fragt, einer antwortet.",
               "selbst": "Jetzt: bei Aufgabe 1 »Auflösung zeigen« und die Selbsteinschätzung auf der Theorie-Seite.",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {Aufgabennr: [[Marke, Text], …]}, "nach": {…}}."""
    vor, nach = {}, {}
    for n, rows in STUNDE.items():
        warte, erste, letzte = [], True, None
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte: vor[nr] = warte
                warte, erste, letzte = [], False, nr
                continue
            if art in ("org", "reserve", "pdf") or (erste and art == "wdh"): continue
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|DISKUSSION|PARTNERCHECK): ", "", text).split(" (")[0]
            key = "diskussion" if marke == "DISKUSSION" else art
            d = DEMO_NAME[_demo(text)] if art == "demo" else ""
            warte.append([marke, BALKEN_TEXT[key].format(d=d, t=t, s=sicherung_kurz(n))])
        if warte and letzte: nach[letzte] = warte
    return {"vor": vor, "nach": nach}


ZUSATZ_TEXT = "Defibrillator-Check, Druck bis in die Füße, KI-Faktencheck Bone-Smashing und Peptide, Blutspende in Zahlen, Rücken-Briefing (Podcast oder Plakat)"
CHECK_ZEILE = "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        _zn = [t["nr"] for t in I.T if t.get("zst") == n]
        if _zn:
            auf += " · Zusatz " + bereich(_zn)   # am Ende der Stunde, nur wenn du früher fertig bist
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n],
                  "theorie_links": [[f"Teil {nr} {name}", "theorie.html#" + tid] for tid, nr, name in THEORIE_TEILE_IDS[n]], "abgabe": ABGABE[n]})
    zus = [t for t in I.T if t["nr"] not in I.PFLICHT and t["id"] != "v0"]
    z.append({"wann": "Für Schnelle", "lesen": ZUSATZ_TEXT, "aufgaben": "Zusatz " + bereich([t["nr"] for t in zus]) + " (stehen am Ende der jeweiligen Stunde)",
              "zeit": "ca. %d min" % sum(t["zeit"] for t in zus), "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": CHECK_ZEILE})
    return z


FAHRPLAN_TEXT = ("Fünf Stunden, ein Körper unter Belastung: Stunde 1 das Herz, Stunde 2 Puls und Gefäße mit Versuch, Stunde 3 Knochen und Gelenke am Skelett, "
                 "Stunde 4 das Blut, Stunde 5 Muskeln und Ergonomie. Alles steht auf EINER Seite »Aufgaben«, du gibst EIN PDF ab. Keine Hausübung. "
                 "Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

# Überblick über die ganze Einheit (Standard 18.11.2026): eine Folie vor der Startfolie von Stunde 1
EINHEIT = {"ziel": "Beim Marsch, beim Training, beim Heben schwerer Kisten arbeitet dein ganzer Körper zusammen: Das Herz pumpt, das Blut bringt Sauerstoff, Knochen tragen und Muskeln ziehen.",
           "am_ende": "Am Ende kannst du erklären, wie Herz, Blut, Knochen und Muskeln zusammenhängen – und weißt, wie du deinen Rücken schonst.",
           "themen": [],
           "stunden": [(1, "DEMO", "Herz im Torso, Kreislauf per Hand"), (2, "VERSUCH", "Puls vor und nach Kniebeugen"), (3, "GRUPPENARBEIT", "Skelett-Rallye"),
                       (4, "GRUPPENARBEIT", "Blut, Blutgruppen, Doping-Rollen"), (5, "DEMO", "Richtig heben, Ergonomie-Check, Mindmap")]}


if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
    print(len(VARIANTEN), "Varianten")
