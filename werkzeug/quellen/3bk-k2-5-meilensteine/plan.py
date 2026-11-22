"""Zeitplan PBGW 3BK · Meilensteine – EINE Quelle für Fahrplan (einheiten.json), Arbeitsblatt (»So läuft die Stunde«, Balken),
HTML-Präsentation und Lösungsseite.

Standards 07.11.–20.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Drei Einzelstunden, jede ist abgeschlossen.
In Stunde 2 steht der 1. Test (22 min einschließlich Austeilen und Einsammeln) in den 40 min Arbeit; der Test ersetzt dort »Weißt du noch?«.
KEINE DATEN in dieser Quelle (Standard 13.11.2026): Termine stehen nur privat im Kalender der Lösungsseite.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "demo" · "erkl" KURZ KLÄREN · "wdh" Weißt du noch? ·
"bespr" BESPRECHEN/Sicherung · "lesen" · "test" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE
REFERAT_MIN = 10
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE
TEST_MIN = 22

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Quellen und Epochen – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K2.1-D1: Ötzis Kupferbeil am Beamer – erst vermuten (ABCD-Karte), dann auflösen", 4, True, "demo", "DEMO"),
     ("Aufgabe 1: Befund, Vermutung, Grenze am Mini-Whiteboard", 4, True, "a1", "GRUPPENARBEIT"),
     ("SELBSTSTUDIUM: Buch S. 25–28 lesen und den Merksatz markieren", 4, True, "lesen", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Befund und Deutung · Vorrat, Spezialisierung, Abhängigkeit", 3, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Landwirtschaft – was hängt womit zusammen?", 7, False, "a2", "GRUPPENARBEIT"),
     ("Aufgabe 3: Stadtstaat und Flächenkönigtum", 7, False, "a3", "GRUPPENARBEIT"),
     ("Aufgabe 8, Teil 1: Zeitstrahl-Karten 1–4 legen", 3, True, "a8", "GRUPPENARBEIT"),
     ("BESPRECHEN: Sicherung – Vorrat, Macht und die Grenze einer Quelle", 4, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit, Plätze ordnen", 4, True, "org", ""),
     ("1. Test einschließlich Austeilen und Einsammeln (Stoff laut Teststoff)", TEST_MIN, True, "test", ""),
     ("KURZ KLÄREN: Arbeitsfassung, Wenn-dann-Regeln, Quelle ist nicht der Alltag (Paragrafenblatt auf Papier)", 4, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 4: Hammurabi – Ordnung, Verantwortung und Ungleichheit", 9, False, "a4", "GRUPPENARBEIT"),
     ("BESPRECHEN: Sicherung – gleiche Verletzung, ungleiche Folge", 4, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 und 2 – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("SELBSTSTUDIUM: Buch S. 105–110 lesen (Athen)", 3, True, "lesen", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Los und Wahl – wer gehört zum »Volk«?", 2, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 5: Athen – wer entscheidet mit?", 7, False, "a5", "GRUPPENARBEIT"),
     ("SELBSTSTUDIUM: Buch S. 111–115 lesen (Republik und Prinzipat)", 3, True, "lesen", "SELBSTSTUDIUM"),
     ("Aufgabe 6: Augustus – Aussage und Machtverteilung", 6, False, "a6", "GRUPPENARBEIT"),
     ("Aufgabe 7: Vier Formen der Herrschaft vergleichen", 5, False, "a7", "GRUPPENARBEIT"),
     ("Aufgabe 8, Teil 2: Karten 5–9, Begründung und eigene Karte", 4, True, "a8", "GRUPPENARBEIT"),
     ("Ziele erreicht? Selbsteinschätzung im Arbeitsblatt", 2, False, "a13", ""),
     ("BESPRECHEN: Aufstellen auf einer Skala (0–10) und Sicherung", 3, True, "bespr", "BESPRECHEN"),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Mini-Whiteboard und Zeitstrahl-Karten legen",
           2: "Test und Quellenarbeit am Paragrafenblatt (Papier, markieren)",
           3: "Aufstellen auf einer Skala (Bewegung) und Vergleich zu zweit"}

ZIEL = {1: "Erklären, wie aus Vorräten, Können und Austausch größere Gemeinschaften und frühe Staaten wurden.",
        2: "An Hammurabis Rechtssammlung zeigen, was schriftliches Recht ordnet – und was es nicht gleich macht.",
        3: "Athen, die römische Republik und das Prinzipat nach Beteiligung und Kontrolle vergleichen."}

MARKE = {1: "DEMO", 2: "GRUPPENARBEIT", 3: "DISKUSSION"}
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
_teile = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art, mk in ph:
        if re.match(r"a\d+$", art):
            _teile.setdefault(int(art[1:]), []).append((n, mi))
for nr, lst in _teile.items():                      # jede Aufgabe: Summe ihrer Phasen = Zeit der Aufgabe
    assert sum(m for _n, m in lst) == _Z[nr], (nr, lst, _Z[nr])
assert sorted(_teile) == I.PFLICHT + [13], (sorted(_teile), I.PFLICHT)   # 13 = »Ziele erreicht?« (Selbsteinschätzung)
assert [n for n, _m in _teile[8]] == [1, 3], "Aufgabe 8 läuft über Stunde 1 und 3"
for nr, lst in _teile.items():                      # einteilige Aufgaben stehen in ihrer Stunde laut inhalt.py
    if len(lst) == 1:
        assert lst[0][0] == [t for t in I.T if t["nr"] == nr][0]["h"], (nr, lst)
assert sum(p[1] for p in STUNDE[2] if p[3] == "test") == TEST_MIN

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Aufgabe 8 Teil 1 (Zeitstrahl-Karten) wandert in Stunde 3; Aufgabe 2 a) nur zwei statt drei Zusammenhänge. "
    "Aufgabe 3 bleibt vollständig (K02, K04).",
 2: "Der Test hat Vorrang. Wenn es danach knapp wird: Aufgabe 4 d) und f) werden Zusatz, die Sicherung läuft mündlich über b) und c). "
    "Nichts wird Hausübung.",
 3: "Wenn es knapp wird: Aufgabe 7 nur für Athen und das Prinzipat ausfüllen (Republik gemeinsam an der Tafel), "
    "Aufgabe 8 c) wird Zusatz. Die Skala am Schluss kann auf zwei Minuten gekürzt werden.",
}
AUSFALL = ("Fällt eine der drei Stunden aus, wird nichts zusammengepresst. Entfällt Stunde 1, rücken die anderen nach und Aufgabe 1 wird "
           "gemeinsam im Einstieg der nächsten Stunde erledigt. Entfällt Stunde 3, werden Aufgabe 7 und Aufgabe 8 Teil 2 Zusatz für Schnelle, "
           "die Arbeitsblatt-PDF wird am Ende von Stunde 2 abgegeben, und der Vergleich Athen–Rom wird beim Einstieg der nächsten Einheit in fünf Minuten "
           "mündlich nachgeholt. Der Test in Stunde 2 bleibt in jedem Fall. Keine Hausübung.")
SUPPLIER = 3   # Stunde 3 braucht kein Material: lesen, Aufgaben 5–8 mit Tipp-Stufen; die Skala nur, wenn jemand da ist

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN); Organisation, Reserve und Test bleiben immer
 1: {1: 0, 2: 2, 4: 1, 5: 1},                       # »Weißt du noch?« entfällt, DEMO und Lesen kürzer, Sicherung bleibt
 3: {1: 0, 3: 0, 7: 0},                             # »Weißt du noch?« und KURZ KLÄREN entfallen, Aufgabe 7 wird Zusatz (siehe REF_HINWEIS)
}
REF_HINWEIS = {1: "Kein Problem: »Weißt du noch?« fällt weg, DEMO und Lesen werden kürzer. Die Sicherung bleibt vollständig.",
               2: "In Stunde 2 geht kein Referat: Der Test braucht 22 Minuten. Referat bitte in Stunde 1 oder in einer anderen Einheit.",
               3: "Nur mit Abstrich: »Weißt du noch?« und das kurze Erklären fallen weg, Aufgabe 7 (Vergleichstabelle) wird Zusatz für Schnelle. "
                  "Der Vergleich kommt dann in der Sicherung mündlich."}
REF_AUFGABE_ZUSATZ = {3: [7]}                        # Aufgaben, die bei einem Referat zu Zusatz werden
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve", "test") for i in _c), _n
    for _i in _c:                                    # eine Aufgabe darf nur wegfallen, wenn sie als Zusatz vermerkt ist
        _m = re.match(r"a(\d+)$", STUNDE[_n][_i][3])
        assert not _m or int(_m.group(1)) in REF_AUFGABE_ZUSATZ.get(_n, []), (_n, _i, "Aufgabe gekürzt, aber nicht als Zusatz vermerkt")
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
assert set(REF_HINWEIS) == set(STUNDE) and set(REF_KUERZEN) <= set(STUNDE)
DOPPEL_HINWEIS = {(1, 2): "Geht: Vom Vorrat direkt zum Recht. Der Test liegt dann in der zweiten Hälfte – Pause vorher einhalten.",
                  (2, 3): "Geht: Nach dem Test Hammurabi und Athen am Stück. Paragrafenblätter für beide Teile vorbereiten."}


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
    ref = ["Referat einschließlich kurzer Rückfragen + Brückenfrage", REFERAT_MIN, True, "referat", "", ""]
    if referat and a not in REF_KUERZEN:
        return None                                  # z. B. Stunde 2: Der Test lässt kein Referat zu (siehe REF_HINWEIS)
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
        _v = variante(_n, False, _r)
        if _v: VARIANTEN["%d%s" % (_n, "R" if _r else "")] = _v
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        _v = variante(_n, True, _r)
        if _v: VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = _v


def kuerzen_text(n):
    return KUERZEN[n].replace("Wenn es knapp wird: ", "")


def aufgaben_der(n, pflicht=True):
    nrs = sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})
    return [x for x in nrs if not pflicht or x in I.PFLICHT]


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


LESEN = {1: "DEMO Ötzis Beil · Buch S. 25–28 lesen · Vorrat, Metall, Schrift, frühe Staaten",
         2: "1. Test · Hammurabis Rechtssammlung am Paragrafenblatt",
         3: "Athen und Rom lesen · vergleichen · Aufstellen auf einer Skala"}
ABGABE = {1: "–", 2: "–", 3: "Arbeitsblatt-PDF in LMS"}
BUCH = {1: "Buch S. 25–39", 2: "Buch S. 39–40", 3: "Buch S. 105–118"}
DEMO_NAME = {1: "Ötzis Kupferbeil"}
DEMO_ID = {1: "K2.1-D1"}

# Theorie nach Stunden (Standard 20.11.2026): (Anker, Kurzname). Die Einheit nummeriert ihre Theorie-Teile nicht –
# die Abschnitte heißen bei den Kadetten wie auf der Theorie-Seite, damit Verweise im Text weiter stimmen.
THEORIE_TEILE_IDS = {
 1: [("vorrat", "Vom Sammeln zum Vorrat"), ("probleme", "Neue Möglichkeiten, neue Probleme"), ("metall", "Metall, Können und Austausch"),
     ("schrift", "Schrift: Listen und Verwaltung"), ("staaten", "Frühe Staaten"), ("zeitstrahl", "Der gemeinsame Zeitstrahl")],
 2: [("regeln", "Was die Regeln verraten"), ("gleichheit", "Recht ist nicht gleich Gleichheit")],
 3: [("athen", "Athen"), ("rom", "Rom"), ("vergleich", "Athen und Rom im Vergleich"), ("anschluss", "Antike und spätere Zeiten")],
}
THEORIE_TEILE = {n: ", ".join(name for _id, name in v) for n, v in THEORIE_TEILE_IDS.items()}


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan (Standard 15.11./18.11.2026): Liste [Marke, Text] bzw. [Marke, Text, Sprungziel].
    Organisation, Reserve und PDF-Sicherung stehen nicht im Kadetten-Fahrplan."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        m = re.match(r"a(\d+)$", art)
        if m:
            nr = int(m.group(1))
            tid = next(t["id"] for t in I.T if t["nr"] == nr)
            name = ("Ziele erreicht?" if nr == 13 else "Aufgabe %d" % nr + (" (Teil %d)" % (1 if n == 1 else 2) if nr == 8 else ""))
            out.append(["" if marke in ("", "GRUPPENARBEIT") else marke, name, "aufgaben.html#card_" + tid])
        elif art == "demo": out.append(["DEMO", "DEMO " + DEMO_NAME[n]])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "lesen": out.append(["SELBSTSTUDIUM", "Buch lesen"])
        elif art == "test": out.append(["", "1. Test"])
        elif art == "bespr": out.append(["BESPRECHEN", "Sicherung"])
        else: raise ValueError(art)
    return out


# Sicherung (Standard 15.11.2026): Was wird am Ende der Stunde gemeinsam gesichert? EINE Quelle für Präsentation, Arbeitsblatt
# (»Am Ende der Stunde sichern wir gemeinsam: …«), Balken und Lösungsseite. teile = (Aufgabe, [Feld-IDs]); auch = weitere Punkte; merken = Merksätze.
SICHERUNG = {
 1: {"teile": [(2, ["staat"]), (3, ["s1", "s2", "s5", "gemeinsam"])], "auch": ["DEMO Ötzis Beil", "Aufgabe 1: Befund – Vermutung – Grenze"],
     "merken": ["Vorräte machen **Spezialisierung** möglich – und wer die **Verteilung** kontrolliert, bekommt **Macht**.",
                "Ein **Befund** ist das, was man feststellen kann. Eine **Deutung** geht darüber hinaus und braucht eine Begründung."]},
 2: {"teile": [(4, ["f196", "f198", "f199", "entsch", "gleich"])], "auch": ["Grenze der Quelle: was die Sammlung nicht zeigt"],
     "merken": ["Hammurabis Sammlung ordnet **Verantwortung**: Wer Schaden verursacht, haftet – nach festen **Wenn-dann-Regeln**.",
                "**Schriftlich heißt nicht gleich**: Die Folge hing vom **Stand des Opfers** ab."]},
 3: {"teile": [(5, ["rat", "arch", "strat", "aus"]), (6, ["name", "macht"]), (7, ["wahl"])],
     "auch": ["Aufgabe 8: Zeitstrahl", "Skala: Wie demokratisch war Athen?"],
     "merken": ["In Athen entschied die **Volksversammlung** – aber nur erwachsene männliche Bürger; Frauen, Metöken und versklavte Menschen blieben außen vor.",
                "Augustus ließ die **Formen der Republik** bestehen und hielt die **Macht** über Heer, Ämter und Geld selbst."]},
}
ANTWORT = {   # Felder ohne Auswahl: kurze Musterantwort für die Sicherungs-Folien
 (2, "staat"): "Kein Automatismus: Handel, Konflikte, Religion und örtliche Bedingungen wirken mit.",
 (3, "gemeinsam"): "Abgaben, Arbeit und Vorräte organisieren – mit Aufzeichnungen.",
 (4, "gleich"): "Schriftlich heißt nicht gleich: Die Strafe hing vom Stand des Opfers ab.",
 (5, "aus"): "Frauen · zugewanderte Metöken · versklavte Menschen.",
 (6, "macht"): "Befehl über die wichtigsten Heere, Amtsbefugnisse auf Dauer, Geld und Ansehen.",
 (7, "wahl"): "Athen: Volksversammlung und Los – viele Bürger entscheiden mit, aber eben nur Bürger. "
             "Prinzipat: Heer und die wichtigsten Befugnisse bei einer Person – Senat und Ämter kontrollieren ihn kaum. "
             "(Nicht: »verteilte Macht = alle entscheiden mit« – in der römischen Republik war die Macht auf viele Ämter verteilt, "
             "mitentschieden hat trotzdem vor allem die Oberschicht.)",
}


def _letter_map(nr):
    """Feld-ID -> Buchstabe der Teilaufgabe. Felder ohne »a)« gehören zum zuletzt genannten Buchstaben (z. B. die Auswahlzeilen unter a))."""
    t = next(x for x in I.T if x["nr"] == nr)
    out, akt = {}, None
    for f in t["fields"]:
        m = re.match(r"([a-z]\d?)\)", f[1])
        if m: akt = m.group(1)
        out[f[0]] = akt or f[0]
    return out


def buchstaben(nr, ids):
    m = _letter_map(nr)
    out = []
    for fid in ids:
        b = m.get(fid, fid)
        if b not in out: out.append(b)
    return out


def sicherung_kurz(n):
    """»Aufgabe 2 c) · Aufgabe 3 a), b) · DEMO Ötzis Beil« – für Balken, Präsentation und Lösungsseite."""
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(b + ")" for b in buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


def sicherung_fragen(nr, ids):
    """[(Frage, Antwort)] für die Sicherungs-Folien – Antwort = richtige Auswahl aus der Prüfregel oder Eintrag in ANTWORT."""
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        a = ANTWORT.get((nr, fid)) or (t.get("chk", {}).get(fid) or {}).get("sel")   # richtige Antwort aus der Prüfregel, nicht die erste Option
        assert a, (nr, fid)
        out.append((f[1], a))
    return out


for _n in SICHERUNG:
    for _nr, _ids in SICHERUNG[_n]["teile"]:
        assert _nr in aufgaben_der(_n), (_n, _nr)
        sicherung_fragen(_nr, _ids)

BALKEN_TEXT = {"demo": "Jetzt DEMO am Beamer: {d}. Erst vermuten – ABCD-Karte bereit, dann auflösen.",
               "lesen": "Jetzt SELBSTSTUDIUM: {t}.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "test": "Jetzt der 1. Test. Handys weg, Unterlagen in die Tasche.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {Aufgabennr: [[Marke, Text], …]}, "nach": {…}}.
    Phasen vor der ersten Aufgabe einer Stunde stehen schon im Kasten »So läuft die Stunde« – außer DEMO, Test und KURZ KLÄREN."""
    vor, nach = {}, {}
    # Die Karte einer Aufgabe steht im Block ihrer Stunde laut inhalt.py. Aufgabe 8 läuft über Stunde 1 und 3,
    # ihre Karte sitzt aber in Stunde 3 – der Schluss-Balken der Stunde 1 muss deshalb an die letzte Karte DIESER Stunde (22.11.2026).
    karte_h = {t["nr"]: t["h"] for t in I.T}
    for n, rows in STUNDE.items():
        warte, erste, letzte = [], True, None
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte: vor.setdefault(nr, []).extend(warte)
                warte, erste = [], False
                if karte_h.get(nr) == n: letzte = nr
                continue
            if art in ("org", "reserve", "pdf") or (erste and art == "wdh"): continue
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|SELBSTSTUDIUM|ALLE GEMEINSAM|PARTNERCHECK): ", "", text).split(" (")[0]
            warte.append([marke, BALKEN_TEXT[art].format(d=DEMO_NAME.get(n, ""), t=t, s=sicherung_kurz(n))])
        if warte and letzte: nach.setdefault(letzte, []).extend(warte)
    return {"vor": vor, "nach": nach}


# Überblicksfolie der ganzen Einheit (Standard 18.11.2026) – eine Quelle für die Präsentation
EINHEIT = {
 "ziel": "Wir schauen uns an, wie Menschen ihr Zusammenleben organisiert haben, als die Gruppen größer wurden: Vorräte, Verwaltung, Recht und "
         "Mitbestimmung. Dieselben Fragen stellen sich heute in jedem Verein, in jeder Firma und in jedem Staat.",
 "am_ende": "Am Ende kannst du erklären, wie aus Dörfern Staaten wurden, was Hammurabis Recht über Ungleichheit zeigt und wie viel Mitbestimmung "
            "es in Athen und Rom wirklich gab.",
 "stunden": [(1, "DEMO", "Vorrat, Metall und Schrift: Wie Macht entsteht"),
             (2, "GRUPPENARBEIT", "1. Test, danach Hammurabis Rechtssammlung"),
             (3, "DISKUSSION", "Athen, Rom und der Vergleich – mit Skala und Mitarbeits-Check danach")],
}


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        if n in (1, 3): auf += " (Aufgabe 8: Teil %d)" % (1 if n == 1 else 2)
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n],
                  "theorie_links": [[name, "theorie.html#" + tid] for tid, name in THEORIE_TEILE_IDS[n]],
                  "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Eigene Lieferliste, KI-Fehlerjagd, Woher kam das Kupfer?, Partnercheck",
              "aufgaben": "Zusatz 9–12", "zeit": "ca. 31 min", "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"})
    return z


FAHRPLAN_TEXT = ("Drei Stunden vom Vorrat zum Staat: Stunde 1 Landwirtschaft, Metall und frühe Staaten, Stunde 2 der 1. Test und Hammurabis Recht, "
                 "Stunde 3 Athen, Rom und der Vergleich. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. Keine Hausübung. "
                 "Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

STUNDENVORSCHLAG = [[f"Stunde {n}", LESEN[n], bereich(aufgaben_der(n)) or "–", f"{ARBEIT} min Arbeit + 10 min Org./Reserve", METHODE[n]] for n in sorted(STUNDE)]

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n}: {I.STUNDENTITEL[n]} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
        print("  Sicherung:", sicherung_kurz(n))
    print(len(VARIANTEN), "Varianten")
