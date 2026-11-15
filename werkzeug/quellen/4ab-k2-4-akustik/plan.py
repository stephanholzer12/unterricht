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
REFERAT_MIN = 20   # Stephan 15.11.2026: Referate in der 4BK dauern mit Besprechung 15–20 min
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen aus der Wellenlehre", 2, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("DEMO K2.4-D1: Stimmgabel – erst vermuten, dann sehen, hören, spüren", 6, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Schall ist eine Druckwelle (Animation), Vakuum", 6, True, "erkl", "BESPRECHEN"),
     ("KURZ KLÄREN: s = v · t, Echo hin und zurück, λ = v / f", 4, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Schall unterwegs – lesen im Buch S. 61, dann Fragen und Rechnungen", 16, False, "a2", "SELBSTSTUDIUM"),
     ("BESPRECHEN: die Echo-Falle und die Faustregel", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K2.4-D2: Lineal an der Tischkante, Tongenerator am Beamer", 6, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Hörbereich, Infra- und Ultraschall, Dezibel-Leiter", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Hoch, tief, laut – die Dezibel-Leiter", 8, False, "a3", "SELBSTSTUDIUM"),
     ("VERSUCH K2.4-V1 (Aufgabe 4): Referenz am Lehrertisch, Messung am eigenen Platz", 14, False, "a4", "VERSUCH"),
     ("BESPRECHEN: Messwerte der Klasse am Beamer", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Aufbau des Ohrs, Hörvorgang (Animation), Druckverstärkung", 7, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 5: Der Weg ins Ohr", 10, False, "a5", "SELBSTSTUDIUM"),
     ("VERSUCH K3.2-V1 (Aufgabe 6): Luft- und Knochenleitung am eigenen Kopf", 5, True, "a6", "VERSUCH"),
     ("KURZ KLÄREN: Haarzellen, Knalltrauma, Tinnitus – Rollenkarten verteilen", 3, True, "erkl", "BESPRECHEN"),
     ("GRUPPENARBEIT (Aufgabe 7): Gehörschutz-Lagebesprechung mit Rollenkarten", 9, False, "a7", "GRUPPENARBEIT"),
     ("DISKUSSION: Prof. HOLZER fragt die Rollen – Rekrut, Ausbilder, Ärztin, Influencer", 3, True, "bespr", "DISKUSSION"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K3.2-D1: Woher kommt das Schnippen? (Augen zu)", 6, True, "demo", "DEMO"),
     ("DEMO K3.2-D2: drehendes Wasserglas + KURZ KLÄREN Lage- und Drehsinn", 7, True, "demo", "DEMO"),
     ("Aufgabe 8: Orientierung – Richtung und Gleichgewicht", 12, False, "a8", "SELBSTSTUDIUM"),
     ("BESPRECHEN: der Pilotenfall", 4, True, "bespr", "BESPRECHEN"),
     ("PARTNERCHECK: vier Karten über die ganze Einheit", 4, True, "partner", "PARTNERCHECK"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Demo mit Vorhersage per Handzeichen, Rechnen in Einzelarbeit",
           2: "Messrunde durch den langen Saal – Handy nur als Messgerät, Bewegung",
           3: "Selbstversuch am eigenen Kopf, Gruppenarbeit mit Rollenkarten und Diskussion",
           4: "Mitmach-Demos mit Augen zu, Partnercheck ohne Handy"}

ZIEL = {1: "Erklären, was beim Schall wandert – und mit s = v · t Entfernungen berechnen.",
        2: "Tonhöhe und Lautstärke den richtigen Größen zuordnen und Dezibel-Werte richtig deuten.",
        3: "Den Weg vom Trommelfell bis zur Haarzelle erklären – und wissen, was das Gehör wirklich schützt.",
        4: "Erklären, wie wir Richtungen hören und Lage und Drehung spüren – und wo uns das täuscht."}

MARKE = {1: "DEMO", 2: "VERSUCH", 3: "GRUPPENARBEIT", 4: "DEMO"}
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
assert sorted(_einmal) == list(range(1, 9)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: DEMO K2.4-D1 nur mit Wasser und Tisch (ohne Resonanzkasten), Aufgabe 2 j) wird Zusatz. Die Echo-Rechnung h) bleibt – sie ist der häufigste Fehler.",
 2: "Zeitstopp für den Versuch: Minute 34 – egal wie weit. Wenn es knapp wird: Grundgeräusch (c) weglassen, nur »Ton an« messen; Aufgabe 3 f) und g) werden Zusatz. "
    "Geht das Handy-Mikrofon nicht: Gruppe schreibt die Werte einer Nachbargruppe ab (im Protokoll vermerken). Fällt der Versuch ganz aus: virtueller Versuch K2.4-VV1 (Zusatz 12) wird Pflicht.",
 3: "Supplierstunde möglich: Aufgabe 5, der Mini-Versuch und die Gruppenarbeit (Aufgabe 7) brauchen kein Material; die Theorie-Karten und die Hörvorgang-Animation stehen im Arbeitsblatt bzw. auf der Theorie-Seite. "
    "Wenn es knapp wird: Die Diskussion der Rollen an den Anfang von Stunde 4 legen.",
 4: "Wenn es knapp wird: DEMO K3.2-D1 auf drei Durchgänge kürzen, der Partnercheck entfällt. "
    "Die PDF-Abgabe darf bis zum Ende des Tages nachgeholt werden.",
}
AUSFALL = ("Fällt eine der vier Stunden aus: Stunden 1 und 2 werden zu einer zusammengelegt – DEMO K2.4-D1 nur 3 min (Wasser), Aufgabe 2 nur a) bis e) und h), "
           "der Versuch K2.4-V1 wird zur 5-min-DEMO (Prof. HOLZER misst mit einem Handy bei 1, 2, 4 und 8 m, die Klasse notiert) oder zum virtuellen Versuch K2.4-VV1 am Handy, Aufgabe 3 bleibt. "
           "Stunden 3 und 4 bleiben unverändert, weil K07 (Ohr, Gleichgewicht) sonst nicht abgedeckt ist. Keine Hausübung.")
SUPPLIER = 3

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN = 20). Organisation, Reserve und PDF bleiben;
 # Aufgaben dürfen gekürzt werden (der Rest wird für diese Klasse Zusatz, siehe REF_NOTIZ). Nie zwei Stunden in eine pressen, keine Hausübung.
 1: {1: 0, 3: 3, 4: 3, 5: 2, 6: 8, 7: 1},
 2: {1: 0, 2: 0, 3: 3, 4: 3, 5: 12, 6: 1},
 3: {1: 0, 2: 3, 3: 6, 4: 4, 5: 1, 6: 5, 7: 0},
 4: {1: 0, 2: 3, 3: 4, 4: 8, 5: 2, 6: 0, 7: 1},
}
REF_NOTIZ = {   # was bei Referat-Kürzung von einer Aufgabe bleibt
 (1, 6): "Pflicht nur a), b), d), f), h) – der Rest wird Zusatz",
 (2, 2): "die Tonhöhe zeigt Prof. HOLZER kurz am Tongenerator (bei KURZ KLÄREN)",
 (2, 4): "nur a), b), e) – der Rest wird Zusatz",
 (2, 5): "Zeitstopp Minute 42, Grundgeräusch c) weglassen",
 (3, 3): "nur Beschriften a)–f); der Weg g)–k) wird Zusatz",
 (3, 4): "Selbstversuch kurz, c) wird Zusatz",
 (3, 6): "nur b)–d) und h) in der Gruppe; e)–g) gemeinsam beim Besprechen von Stunde 4",
 (4, 4): "Pflicht nur a)–e); den Pilotenfall f), g) klären wir gemeinsam",
}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve", "pdf") for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
    assert all((_n, i) in REF_NOTIZ for i in _c if re.match(r"a\d+$", STUNDE[_n][i][3]) and _c[i] > 0), (_n, "Aufgabe gekürzt ohne Notiz")
DOPPEL_HINWEIS = {(1, 2): "Gut: Rechnen und Messen hintereinander. Lautsprecher und Maßband stehen schon.",
                  (2, 3): "Gut: Vom Pegel direkt ins Ohr. Nach dem Versuch Handys wegräumen lassen.",
                  (3, 4): "Gut: Ohr, Schutz und Gleichgewicht am Stück. Wasserglas schon vorher füllen."}


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


LESEN = {1: "DEMO Stimmgabel · Druckwelle · Theorie-Karten 1 und 2 · Buch S. 61",
         2: "DEMO Lineal und Tongenerator · Dezibel-Leiter · VERSUCH Schallpegel messen · Buch S. 63–64",
         3: "Aufbau des Ohrs, Hörvorgang · Mini-Versuch am eigenen Kopf · GRUPPENARBEIT Gehörschutz · Buch S. 109–110",
         4: "DEMOS Richtungshören und Wasserglas · Lage- und Drehsinn · Partnercheck · Buch S. 110–112"}
THEORIE_TEILE = {1: "Teil 1 Schall, Teil 2 Tempo", 2: "Teil 3 Tonhöhe, Teil 4 Dezibel, Teil 5 Messen", 3: "Teil 6 Ohr, Teil 7 Schutz", 4: "Teil 8 Richtung, Teil 9 Gleichgewicht"}
ABGABE = {1: "–", 2: "Messwerte deiner Gruppe eintragen", 3: "–", 4: "Arbeitsblatt-PDF in LMS"}


BUCH = {1: "Buch S. 60–61", 2: "Buch S. 62–64", 3: "Buch S. 109–110", 4: "Buch S. 110–112"}
DEMO_NAME = {"K2.4-D1": "Stimmgabel", "K2.4-D2": "Lineal und Tongenerator", "K3.2-D1": "Woher kommt das Schnippen?", "K3.2-D2": "Drehendes Wasserglas"}
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
            out.append([marke, f"{marke} (Aufgabe {nr})"] if marke in ("VERSUCH", "GRUPPENARBEIT") else ["", f"Aufgabe {nr}"])
        elif art == "demo": out.append(["DEMO", "DEMO " + DEMO_NAME[_demo(text)]])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "bespr": out.append([marke, "Diskussion der Rollen" if marke == "DISKUSSION" else "Sicherung"])
        elif art == "partner": out.append(["PARTNERCHECK", "Partnercheck"])
        elif art == "selbst": out.append(["", "Auflösung Aufgabe 1"])
        else: raise ValueError(art)
    return out


# Sicherung (Stephan 15.11.2026): EINE Quelle für Präsentation, Arbeitsblatt (»Am Ende der Stunde sichern wir gemeinsam: …«), Balken, Lösungsseite.
SICHERUNG = {
 1: {"teile": [(2, ["was", "vakuum", "gewitter", "echo"])], "auch": ["DEMO Stimmgabel"],
     "merken": ["Schall ist eine **Druckwelle**: Die Luftteilchen schwingen nur **hin und her**, die Welle wandert. Ohne Teilchen – im **Vakuum** – gibt es **keinen Schall**.",
                "**s = v · t**, in Luft rund **340 m/s**. Beim **Echo** läuft der Schall **hin und zurück** – darum durch 2 teilen."]},
 2: {"teile": [(3, ["i10", "zwei", "empf"]), (4, ["saal"])], "auch": ["VERSUCH: Messwerte der Klasse"],
     "merken": ["Die **Frequenz** bestimmt die **Tonhöhe**, die **Amplitude** die **Lautstärke**.",
                "**+10 dB = zehnmal so viel Intensität.** Ab **85 dB** schadet Dauerlärm – dann **Gehörschutz**."]},
 3: {"teile": [(5, ["w1", "knochen"]), (7, ["nach", "schiess", "anc"])], "auch": ["VERSUCH K3.2-V1", "DISKUSSION der Rollen"],
     "merken": ["Trommelfell → Gehörknöchelchen → Schnecke → **Haarzellen** → Hörnerv → Gehirn.",
                "Zerstörte **Haarzellen wachsen nicht nach**. Geprüfter Gehörschutz **vor dem ersten Knall** – nicht erst danach."]},
 4: {"teile": [(8, ["vorne", "lage", "dreh", "pilot"])], "auch": ["DEMO Wasserglas", "PARTNERCHECK"],
     "merken": ["Richtung hören: Das abgewandte Ohr hört den Schall **später und leiser**.",
                "**Bogengänge** melden Drehungen, **Vorhofsäckchen** die Lage. Ohne Sicht können sie täuschen – darum vertraut die Pilotin den **Instrumenten**."]},
}
ANTWORT = {(2, "gewitter"): "rund 2 km – 340 m/s · 6 s = 2040 m",
           (2, "echo"): "204 m – 340 m/s · 1,2 s = 408 m hin und zurück, halb so viel"}


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


ZUSATZ_TEXT = "Echolot und Fledermaus, KI-Fehlerjagd, Gehörschutz-Briefing (Podcast oder Plakat), virtueller Versuch am Handy (PhET), Lesen und prüfen"
CHECK_ZEILE = "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n], "abgabe": ABGABE[n]})
    zus = [t for t in I.T if t["nr"] not in I.PFLICHT and t["id"] != "v0"]
    z.append({"wann": "Für Schnelle", "lesen": ZUSATZ_TEXT, "aufgaben": "Zusatz " + bereich([t["nr"] for t in zus]),
              "zeit": "ca. %d min" % sum(t["zeit"] for t in zus), "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": CHECK_ZEILE})
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
