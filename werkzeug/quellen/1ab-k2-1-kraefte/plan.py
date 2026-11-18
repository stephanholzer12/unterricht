"""Zeitplan K2.1 Mechanische Kräfte – EINE Quelle für Fahrplan (einheiten.json), Arbeitsblatt (Kasten »So läuft die Stunde«, Balken, Sicherung),
HTML-Präsentation und Lösungsseite.
Neue Standards 07.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Sechs Einzelstunden, jede Stunde ist abgeschlossen.
Neue Standards 15.11.2026 (Vorbild 2AB K1.5): Marke je Phase, Stundentitel, Reihenfolge (folge), Balken zwischen den Aufgaben, Sicherung am Ende jeder Stunde.
KEINE DATEN in dieser Quelle und auf den Kadetten-Seiten (Stephan, 13.11.2026): Termine, Doppelstunden und Referate trägt Prof. HOLZER selbst im
Reiter »Kalender« der privaten Lösungsseite ein. Für jeden möglichen Termin liefert dieses Modul den fertigen Ablauf: Einzelstunde, Einzelstunde MIT Referat,
Doppelstunde, Doppelstunde MIT Referat. Beide Klassen bekommen denselben Fahrplan.
Referate (Stephan, 15.11.2026): durchschnittlich 15–20 min einschließlich Besprechung – gerechnet wird mit 20 min.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "wdh" Weißt du noch? · "erkl" Prof. HOLZER erklärt · "demo" DEMO ·
"gruppen" Gruppen auslosen · "freigabe" · "probe" · "peer" Partnercheck/Probe · "praes" Präsentationen · "bespr" Sicherung · "selbst" Auflösung ·
"org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10        # Klassenbuch, Ankommen, Handys, Aufräumen, Puffer
ARBEIT = MIN - ORG_RESERVE
VS = "v:" + I.VS_ID
REFERAT_MIN = 20        # Schüler-Referat einschließlich Besprechung (Stephan 15.11.2026: im Schnitt 15–20 min) – gerechnet mit 20
PAUSE = 5               # Doppelstunde: Pause ohne Arbeitszeit
DOPPEL_MIN = 2 * MIN + PAUSE   # z. B. 13.35–15.20 Uhr

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit (Arbeitsblatt über den QR-Code)", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu »Erkenntnisgewinn« – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("KURZ KLÄREN: Kraftwirkung, Richtung, resultierende Kraft – Kräftebild an der Tafel, Puck-Frage mit der ABCD-Karte", 9, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Kraft und Bewegung unterscheiden", 13, False, "a2", "SELBSTSTUDIUM"),
     ("SICHERUNG: Aufgabe 2 – Kurve, Tempo, F = m · a", 4, True, "bespr", "BESPRECHEN"),
     ("Gruppen auslosen (Generator), sieben Themen zeigen, »So läuft das Projekt«", 8, True, "gruppen", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: So arbeitet ihr heute – Gruppenkarte im Arbeitsblatt", 2, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Euer Thema selbst erarbeiten (Leitfragen, Buch, Theorie-Seite)", 15, False, "a3", "SELBSTSTUDIUM"),
     ("Aufgabe 4: Euren Versuch auswählen und planen (erst auf Papier)", 10, True, "a4", "GRUPPENARBEIT"),
     ("Freigabe durch Prof. HOLZER – je Gruppe eine Minute", 7, True, "freigabe", "BESPRECHEN"),
     ("SICHERUNG: Jede Gruppe sagt ihre Frage und ihren Versuch in einem Satz", 2, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit, Material an die Plätze", 3, True, "org", ""),
     ("Weißt du noch? Drei Fragen zum Versuchsplan – mit der ABCD-Karte am Handy antworten", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Sicherheit – was erlaubt ist, wo gearbeitet wird", 3, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 5: VERSUCH aufbauen, machen, Ergebnisse eintragen", 30, True, "a5", "VERSUCH"),
     ("PARTNERCHECK: Versuch einmal so vorführen wie in Stunde 5 (Probe)", 2, True, "peer", "PARTNERCHECK"),
     ("SICHERUNG: Was hat euer Versuch gezeigt? Ein Satz je Gruppe", 2, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Aufräumen, ausspülen, Material zurück bzw. einpacken", 3, True, "org", ""),
     ("Reserve", 4, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zum Versuch – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 6: Steckbrief für die Klasse gemeinsam schreiben", 17, False, "a6", "GRUPPENARBEIT"),
     ("Präsentation vorbereiten und mit Stoppuhr proben (3 min)", 9, True, "probe", "GRUPPENARBEIT"),
     ("PARTNERCHECK: Eine andere Gruppe liest den Steckbrief und hört die Probe", 7, True, "peer", "PARTNERCHECK"),
     ("SICHERUNG: Was die andere Gruppe gut erklärt hat und was im Steckbrief noch fehlt", 2, True, "bespr", "BESPRECHEN"),
     ("Handout-PDF in Teams, Zwischenstand als PDF sichern", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 5: [("Beginn: Klassenbuch, Anwesenheit, Material der Gruppen an die Plätze", 4, True, "org", ""),
     ("Weißt du noch? Zwei Fragen zu den Themen – mit der ABCD-Karte am Handy antworten", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Reihenfolge ansagen, Mitschrift erklären", 2, True, "erkl", "BESPRECHEN"),
     ("Sieben Gruppen präsentieren: je 3 min einschließlich Versuch, 1 min Übergang – alle schreiben mit", 28, True, "praes", "PRÄSENTATION"),
     ("SICHERUNG: Zwei fachliche Klärungen aus den Präsentationen", 4, True, "bespr", "BESPRECHEN"),
     ("Aufgabe 7: Mitschrift ergänzen (Steckbriefe in Teams)", 3, False, "a7", "SELBSTSTUDIUM"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 6: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu den Präsentationen – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K2.1-D1: Zwei Kraftmesser ziehen aneinander – erst vermuten (ABCD-Karte), dann zeigen", 4, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Begriffstabelle Kraft, Bewegung, Druck an der Tafel", 6, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 8: Alle Themen selbst erklären – einzeln und ohne KI", 16, False, "a8", "SELBSTSTUDIUM"),
     ("SICHERUNG: Aufgabe 8 – drei Denkfehler, die Druck-Rechnung und die vier Formeln", 7, True, "bespr", "BESPRECHEN"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Kräftebild an der Tafel, Vorhersage mit der ABCD-Karte",
           2: "Selbststudium mit Leitfragen, Versuchsplan auf Papier, Freigabe",
           3: "Selbst gewählter Gruppenversuch mit Probe",
           4: "Steckbrief schreiben, Partnercheck ohne Handy",
           5: "Kurzpräsentationen mit Demonstration, Mitschrift mit der Hand",
           6: "Demo mit Vorhersage, danach Einzelarbeit"}

ZIEL = {1: "Kraftwirkungen erkennen, Masse und Kraft auseinanderhalten – und wissen, in welcher Gruppe du bist.",
        2: "Das eigene Thema mit den Leitfragen verstehen und einen freigegebenen Versuchsplan haben.",
        3: "Den eigenen Versuch sicher machen, Ergebnisse festhalten und ihn einmal vorführen können.",
        4: "Einen Steckbrief schreiben, mit dem die anderen euer Thema lernen können – und die Präsentation sitzt.",
        5: "Das eigene Thema verständlich zeigen und von allen anderen Gruppen die Kernaussage mitnehmen.",
        6: "Alle sieben Themen selbst erklären und die Einheiten sicher verwenden."}

# Überblick über die ganze Einheit (Stephan, 18.11.2026): erste Folie der Einheit, VOR »Heute«.
# Nur das Wichtigste je Stunde (Marke + eine kurze Zeile), keine Minuten, keine Aufgabenliste.
EINHEIT = {
    "ziel": "Kräfte siehst du nicht – aber ihre **Wirkung**: beim Sprint, beim Schwimmen, beim Bremsen, im Dienst.",
    "am_ende": "Am Ende kannst du **alle sieben Kräfte-Themen** erklären, Kräfte **messen** und mit **N, kg und Pa** rechnen.",
    "themen": "7 Gruppen – 7 Themen: Bewegung · Gewichtskraft · Auftrieb · Reibung · Kapillarwirkung · Druck · Kraft und Gegenkraft",
    "stunden": [  # (Stunde, Marke, kurz)
        ("1", "BESPRECHEN", "Was Kräfte bewirken · Masse oder Kraft? · Gruppen auslosen"),
        ("2", "GRUPPENARBEIT", "Euer Thema: Leitfragen klären, Versuch planen"),
        ("3", "VERSUCH", "Euren Kräfte-Versuch machen und fürs Vorführen üben"),
        ("4", "GRUPPENARBEIT", "Steckbrief für alle schreiben · Generalprobe"),
        ("5", "PRÄSENTATION", "Jede Gruppe zeigt ihr Thema – ihr lernt von allen"),
        ("6", "DEMO", "Kraftmesser gegen Kraftmesser · alle Themen allein erklären"),
        ("Danach", "CHECK", "Mitarbeits-Check: 10 Fragen zur ganzen Einheit"),
    ],
    "abgabe": "Jede Stunde: **Arbeitsblatt-PDF in LMS**.",
}

PLAN = {k: [{"std": n, "teile": [n], "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}
MARKE = {1: "BESPRECHEN", 2: "SELBSTSTUDIUM", 3: "VERSUCH", 4: "GRUPPENARBEIT", 5: "PRÄSENTATION", 6: "SELBSTSTUDIUM"}
MARKEN = {"", "BESPRECHEN", "SELBSTSTUDIUM", "GRUPPENARBEIT", "VERSUCH", "PARTNERCHECK", "PRÄSENTATION", "DEMO"}

# ---------------------------------------------------------------- Kontrollen
_Z = {t["nr"]: t["zeit"] for t in I.T}
for n, ph in STUNDE.items():
    assert sum(p[1] for p in ph) == MIN, (n, sum(p[1] for p in ph))
    assert sum(p[1] for p in ph if p[3] in ("org", "reserve")) == ORG_RESERVE, (n, "Organisation und Reserve nicht 10 min")
    assert sum(p[1] for p in ph if p[3] == "reserve") >= 4, (n, "zu wenig Reserve")
    assert any(p[2] for p in ph if p[3] not in ("org", "reserve")), (n, "keine Phase ohne Handy")
    assert all(p[4] in MARKEN for p in ph), n
    assert sum(1 for p in ph if p[3] == "bespr") == 1, (n, "genau eine Sicherung am Ende")
_m = [METHODE[n] for n in sorted(METHODE)]
assert all(a != b for a, b in zip(_m, _m[1:])), "zwei gleiche Methoden hintereinander"
assert len(set(_m)) >= 3
_einmal = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art, mk in ph:
        if re.match(r"a\d+$", art):
            _einmal.setdefault(int(art[1:]), []).append((n, mi))
for nr, lst in _einmal.items():
    t = next(x for x in I.T if x["nr"] == nr)
    assert len(lst) == 1 and lst[0][1] == _Z[nr] and lst[0][0] == t["h"], (nr, lst, _Z[nr], t["h"])
assert sorted(_einmal) == list(range(1, 9)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall und Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Die Gruppen- und Rollenverteilung auf den Anfang von Stunde 2 verschieben. Aufgabe 2 bleibt – sie ist die Rechengrundlage für Stunde 6.",
 2: "Wenn es knapp wird: Leitfrage 4 und die zweite Quelle (g) dürfen in Stunde 3 nachgeholt werden. Die Freigabe des Plans darf nicht entfallen – wer keine hat, nimmt Idee 1 der Gruppenkarte.",
 3: "Zeitstopp bei Minute 38: Versuch beenden, egal wie weit die Gruppen sind – dann Probe, Sicherung, PDF; aufgeräumt wird ab Minute 43. Wenn es knapp wird: Die Probe entfällt, dafür wird in Stunde 4 geprobt. "
    "Fehlt Material von zu Hause: Saal-Variante der Idee nehmen. Nie Werte erfinden – lieber beschreiben, was man gesehen hat.",
 4: "Diese Stunde fällt bei einem Ausfall ZUERST weg: Den Steckbrief schreiben die Gruppen dann in den ersten 15 Minuten von Stunde 5, die Präsentationen werden auf je 2 Minuten gekürzt. "
    "Wenn es nur knapp wird: Den Partnercheck auf zwei Sätze kürzen.",
 5: "Je Gruppe sind 3 Minuten einschließlich Demonstration fest. Wenn es knapp wird: Die Rückmeldung nach jeder Gruppe entfällt, die zwei fachlichen Klärungen bleiben. "
    "Niemals zwei Gruppen gleichzeitig präsentieren lassen.",
 6: "Supplierstunde möglich: Aufgabe 8, die Theorie-Karten und die Selbsteinschätzung brauchen kein Material und keinen Versuch (die DEMO entfällt dann). "
    "Wenn es knapp wird: Die Sicherung auf die beiden Denkfehler »Auftrieb im Gleichgewicht« und »Gegenkraft am anderen Körper« beschränken.",
}
KNAPP = {(k, n): KUERZEN[n] for k in I.KLASSEN for n in KUERZEN}
SUPPLIER = 6
AUSFALL_ZUERST = 4

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
# Referat (20 min): Diese Phasen werden gekürzt (Phasen-Index ab 0 -> neue Minuten), zusammen genau REFERAT_MIN.
# Organisation und Reserve bleiben. 20 von 40 Arbeitsminuten gehen nicht ohne Aufgabenzeit – was dabei wegfällt, steht in REF_FOLGEN.
REF_KUERZEN = {
 1: {1: 0, 3: 5, 4: 8, 5: 2, 6: 2},
 2: {1: 0, 2: 1, 3: 10, 4: 6, 5: 2, 6: 0},
 3: {1: 0, 2: 2, 3: 17, 4: 0, 5: 0},
 4: {1: 0, 2: 12, 3: 4, 4: 2, 5: 0},
 5: {1: 0, 2: 1, 3: 17, 4: 1, 5: 0},
 6: {1: 0, 2: 2, 3: 1, 4: 13, 5: 2, 6: 0},
}
REF_FOLGEN = {
 1: "Aufgabe 2 nur a) bis c) in der Stunde, die Sicherung nur a und c; d) und e) rechnet die Klasse zu Beginn von Stunde 2 gemeinsam (statt »Weißt du noch?«) und sichert e) dabei. "
    "Gruppen nur auslosen und zeigen – »So läuft das Projekt« kommt an den Anfang von Stunde 2.",
 2: "Aufgabe 3 ohne Leitfrage 4 und Quelle g (in Stunde 3 nachholen). Den Versuchsplan in Stichworten. "
    "Die Freigabe machst du im Herumgehen während Aufgabe 4; wer keine bekommt, nimmt Idee 1 der Gruppenkarte.",
 3: "Sehr knapp – besser kein Referat in Stunde 3. Wenn doch: nur 17 Minuten Versuch mit einer Messreihe, Zeitstopp bei Minute 42; die Probe und die Sicherung wandern in Stunde 4.",
 4: "Steckbrief nur mit den Pflichtfeldern (Kernaussage, Formel, Beispiel, Versuch); die Probe einmal ohne Stoppuhr, der Partnercheck in zwei Sätzen.",
 5: "Sehr knapp – besser kein Referat in Stunde 5. Wenn doch: je Gruppe 2 Minuten, Übergang ohne Pause (die nächste Gruppe baut während der Fragen auf); "
    "Aufgabe 7 (Mitschrift ergänzen) wandert an den Anfang von Stunde 6.",
 6: "Aufgabe 8 in 13 Minuten: i) und j) sind dann freiwillig. DEMO nur zeigen (ohne Vermutung), die Begriffstabelle nur zeigen (Theorie »Kurz & knapp«), die Sicherung nur mit den zwei Denkfehlern, "
    "die Auflösung von Aufgabe 1 machen die Kadetten selbst im Arbeitsblatt.",
}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve") for i in _c), (_n, "Organisation und Reserve bleiben")
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
    assert _n in REF_FOLGEN
# Doppelstunde (zwei aufeinanderfolgende Stunden a, a+1): Zwischenstand-PDF und Reserve der ersten, Klassenbuch und »Weißt du noch?« der zweiten entfallen.
# Mit Referat reicht dieser Gewinn nicht ganz für 20 Minuten – REF_DOPPEL kürzt den Rest (("a"|"b", Phasen-Index) -> neue Minuten).
REF_DOPPEL = {
 1: {("a", 1): 0, ("a", 5): 2, ("b", 6): 1},
 2: {("a", 1): 0, ("a", 5): 5, ("b", 4): 0, ("b", 5): 1},
 3: {("a", 1): 0, ("a", 4): 0, ("b", 3): 6, ("b", 5): 1},
 4: {("a", 1): 0, ("a", 4): 5, ("a", 5): 1},
 5: {("a", 1): 0, ("a", 4): 2, ("b", 3): 4},
}


def doppel_kuerzen_text(a):
    """Was eine Doppelstunde a + a+1 mit Referat zusätzlich kürzt (Kalender der Lösungsseite)."""
    out = []
    for (w, i), m in sorted(REF_DOPPEL[a].items()):
        n = a if w == "a" else a + 1
        art = STUNDE[n][i][3]; mi = STUNDE[n][i][1]
        kurz = {"bespr": "Sicherung", "wdh": "»Weißt du noch?«", "peer": "Partnercheck", "demo": "DEMO", "erkl": "Erklären"}.get(art) or _kurzname(STUNDE[n][i][0])
        out.append(f"Stunde {n}: {kurz} " + ("entfällt" if m == 0 else f"{mi} auf {m} min"))
    return ("Klassenbuch, »Weißt du noch?« der zweiten Stunde, Zwischenstand-PDF und Reserve der ersten Stunde gibt es nur einmal. Dazu: "
            + " · ".join(out) + ".")


DOPPEL_HINWEIS = {
 (1, 2): "Gut machbar. Gruppen auslosen und gleich in die selbstständige Arbeit gehen.",
 (2, 3): "Achtung: Material von zu Hause kann nicht mitgebracht werden – alle Gruppen nehmen die Saal-Variante (Idee 1).",
 (3, 4): "Sehr gut: Versuch und Steckbrief hintereinander, nur einmal auf- und abbauen.",
 (4, 5): "Gut: Steckbrief schreiben und gleich präsentieren. Handout vor den Präsentationen in Teams stellen lassen.",
 (5, 6): "Gut: Nach den Präsentationen gleich Aufgabe 8. Die Steckbriefe stehen in Teams.",
}


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art, mk) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]
            note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
        z.append([name, neu, bool(oh), art, note, mk])
    return z


def _chip(art, oh):
    return bool(oh) and art not in ("org", "reserve", "bespr", "erkl", "pause", "referat", "wdh", "gruppen", "freigabe", "demo")


def _referat_zeile():
    return ["Referat einer Mitschülerin bzw. eines Mitschülers einschließlich Besprechung und Brückenfrage", REFERAT_MIN, True, "referat", "", ""]


def variante(a, doppel=False, referat=False):
    """Ablauf als Liste [Name, Minuten, ohne Handy, Art, Hinweis, Marke]. Einzelstunde: Summe 50. Doppelstunde: Summe 105 (mit Pause)."""
    if not doppel:
        z = _zeilen(a, REF_KUERZEN[a] if referat else None)
        if referat:
            z.insert(1, _referat_zeile())
        assert sum(r[1] for r in z) == MIN, (a, referat, sum(r[1] for r in z))
        return z
    b = a + 1
    ca = {i: m for (w, i), m in REF_DOPPEL[a].items() if w == "a"} if referat else None
    cb = {i: m for (w, i), m in REF_DOPPEL[a].items() if w == "b"} if referat else None
    za = [r for r in _zeilen(a, ca) if r[3] not in ("pdf", "reserve")]
    zb = _zeilen(b, cb)[1:]                      # Klassenbuch entfällt
    zb = [r for r in zb if r[3] != "wdh"]       # »Weißt du noch?« entfällt
    z = za + [["Pause (keine Arbeitszeit)", PAUSE, True, "pause", "", ""]] + zb
    if referat:
        z.insert(1, _referat_zeile())
    rest = DOPPEL_MIN - sum(r[1] for r in z)
    assert rest >= 0, (a, referat, rest)
    if referat: assert rest == 0, (a, "Doppelstunde mit Referat: Kürzungen passen nicht", rest)
    if rest:
        z.append(["Puffer, Verlängerung der Arbeitsphasen oder ein Ausgleichsbaustein (Reiter »Ausgleich«)" if rest >= 10 else "Puffer", rest, True, "reserve", "", ""])
    assert sum(r[1] for r in z) == DOPPEL_MIN, (a, referat)
    return z


VARIANTEN = {}
for _n in sorted(STUNDE):
    for _r in (False, True):
        VARIANTEN["%d%s" % (_n, "R" if _r else "")] = variante(_n, False, _r)
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = variante(_n, True, _r)


def _kurzname(name):
    return re.split(r"[:–(?]| einschließlich| mit der ABCD", re.sub(r"^(KURZ KLÄREN|SICHERUNG|PARTNERCHECK|DEMO K2\.1-D1): ", "", name))[0].strip()


def kuerzen_text(n):
    """Was bei einem Referat in Stunde n geändert wird – Kurzfassung für Kalender und Lösungsseite."""
    out = []
    for i, m in sorted(REF_KUERZEN[n].items()):
        name, mi = STUNDE[n][i][0], STUNDE[n][i][1]
        kurz = {"bespr": "Sicherung", "wdh": "»Weißt du noch?«", "selbst": "Auflösung von Aufgabe 1", "peer": "Partnercheck", "demo": "DEMO", "erkl": "Erklären"}.get(STUNDE[n][i][3]) or _kurzname(name)
        out.append(f"{kurz} entfällt" if m == 0 else f"{kurz} {mi} auf {m} min")
    return " · ".join(out) + ". " + REF_FOLGEN[n]


def aufgaben_der(st):
    nrs = sorted({int(p[3][1:]) for p in st["phasen"] if re.match(r"a\d+$", p[3])})
    return nrs, []


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


def minuten(st, arten):
    return sum(p[1] for p in st["phasen"] if any(p[3].startswith(a) for a in arten))


LESEN = {1: "Mit der ganzen Klasse: Was eine Kraft bewirkt, rechnen mit Einheiten · Gruppen auslosen",
         2: "Selbst erarbeiten: Gruppenkarte, Buchseiten und Theorie-Teil deines Themas · Versuch planen, Freigabe",
         3: "Euren Versuch machen und üben · Material von zu Hause mitbringen",
         4: "Steckbrief schreiben, Handout in Teams · Präsentation proben",
         5: "Alle sieben Gruppen präsentieren · du schreibst mit",
         6: "DEMO Kraftmesser · Aufgabe 8 allein · Teile 1 bis 8 als Nachschlagewerk"}

ABGABE = {1: "–", 2: "Plan freigeben lassen", 3: "–", 4: "Handout-PDF in Teams (Schriftführung)", 5: "–", 6: "Arbeitsblatt-PDF in LMS"}

# Theorie-Teile je Stunde (Stephan, 14.11.2026) – zeigt der Fahrplan unter den Aufgaben
THEORIE_TEILE = {1: "Teil 1 Kraft, Teil 2 Bewegung", 2: "Teil eurer Gruppe (Gruppenkarte) und Projekt", 3: "Teil eurer Gruppe", 4: "Teil eurer Gruppe",
                 5: "alle sieben Teile zum Nachlesen nach den Präsentationen", 6: "Teile 1–8 und »Kurz & knapp«"}
BUCH = {1: "Buch S. 44–49", 2: "Buch S. 45–61 (dein Thema)", 3: "Buch S. 45–61 (dein Thema)", 4: "Buch S. 45–61 (dein Thema)", 5: "Buch S. 45–61", 6: "Buch S. 45–61"}
DEMO_NAME = {6: "Kraftmesser"}


# ---------------------------------------------------------------- Reihenfolge der Stunde (Fahrplan, Arbeitsblatt, Präsentation)
_FOLGE = {"wdh": ("BESPRECHEN", "Weißt du noch?"), "erkl": ("BESPRECHEN", "Prof. HOLZER erklärt"), "bespr": ("BESPRECHEN", "Sicherung"),
          "gruppen": ("BESPRECHEN", "Gruppen auslosen"), "freigabe": ("BESPRECHEN", "Freigabe"), "probe": ("GRUPPENARBEIT", "Probe mit Stoppuhr"),
          "praes": ("PRÄSENTATION", "Präsentationen"), "selbst": ("", "Auflösung Aufgabe 1")}


def folge(n):
    """Reihenfolge der Stunde: Liste [Marke, kurzer Text]; Organisation, Reserve und PDF fehlen (stehen nicht im Kadetten-Fahrplan)."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        if re.match(r"a\d+$", art):
            nr = int(art[1:])
            if marke == "VERSUCH": out.append(["VERSUCH", "VERSUCH (Aufgabe %d)" % nr])
            elif marke == "GRUPPENARBEIT": out.append(["GRUPPENARBEIT", "Aufgabe %d in der Gruppe" % nr])
            else: out.append(["", "Aufgabe %d" % nr])
        elif art == "demo": out.append(["DEMO", "DEMO " + DEMO_NAME[n]])
        elif art == "peer": out.append(["PARTNERCHECK", "Probe" if n == 3 else "Partnercheck"])
        else: out.append(list(_FOLGE[art]))
    return out


# ---------------------------------------------------------------- Sicherung am Ende jeder Stunde (Stephan 15.11.2026)
# teile = (Aufgabe, [Feld-IDs]) – nur automatisch prüfbare Teile; auch = weitere Punkte; merken = zwei Merksätze.
SICHERUNG = {
 1: {"teile": [(2, ["wirkung", "tempo", "kraft"])], "auch": ["Kräftebild an der Tafel"],
     "merken": ["Eine **Kraft** ändert Tempo oder Richtung einer Bewegung – oder sie **verformt** einen Körper.",
                "**F = m · a**: Kraft in **Newton (N)**, Masse in **kg**, Beschleunigung in **m/s²**."]},
 2: {"teile": [], "auch": ["Jede Gruppe sagt ihre Frage und ihren Versuch in einem Satz"],
     "merken": ["Ein guter Versuch beantwortet **eine prüfbare Frage**: Was ändern wir, was messen wir, was bleibt gleich?",
                "Gebaut wird erst nach der **Freigabe** – Sicherheit geht vor."]},
 3: {"teile": [], "auch": ["Jede Gruppe sagt in einem Satz, was ihr Versuch gezeigt hat"],
     "merken": ["**Messwerte** schreibt man sofort auf – mit **Einheit**. Nie Werte erfinden.",
                "Jeder Versuch hat **Grenzen**: Wir sagen offen, was er nicht zeigt."]},
 4: {"teile": [], "auch": ["Was die andere Gruppe gut erklärt hat und was im Steckbrief noch fehlt"],
     "merken": ["Ein Steckbrief braucht **Kernaussage, Formel mit Einheit, Beispiel und Versuch**.",
                "Drei Minuten heißt: **ein** Versuch, **eine** Kernaussage, laut und langsam."]},
 5: {"teile": [], "auch": ["Zwei fachliche Klärungen aus den Präsentationen"],
     "merken": ["Gleich große, **entgegengesetzte** Kräfte an **einem** Körper: **Kräftegleichgewicht**. Kraft und Gegenkraft wirken auf **zwei** Körper.",
                "**Auftrieb** = Gewichtskraft des verdrängten Wassers · **Druck** = Kraft durch Fläche."]},
 6: {"teile": [(8, ["schwimmen", "druck", "gegenkraft", "gleichgewicht"])], "auch": ["DEMO Kraftmesser"],
     "merken": ["**Kraft und Gegenkraft** sind gleich groß und wirken auf **verschiedene** Körper.",
                "Die vier Formeln: **v = s / t · F = m · a · F_G = m · g · p = F / A**."]},
}
ANTWORT = {(2, "tempo"): "v = s / t = 5 m : 4 s = 1,25 m/s",
           (2, "kraft"): "F = m · a = 2 kg · 3 m/s² = 6 N",
           (8, "druck"): "p = F / A = 120 N : 0,02 m² = 6000 Pa"}   # Felder ohne Auswahl


def buchstaben(nr, ids):
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        m = re.match(r"([a-z]\d?)\)", f[1]); out.append(m.group(1) if m else fid)
    return out


def sicherung_kurz(n):
    """»Aufgabe 2 a, c, e · Kräftebild an der Tafel« – für Balken, Präsentation und Lösungsseite."""
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


def sicherung_fragen(nr, ids):
    """[(Frage, Antwort)] für die Sicherungs-Folien – Antwort aus der Prüfregel (chk sel) oder ANTWORT, nie die erste Option."""
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        a = ANTWORT.get((nr, fid)) or (t.get("chk", {}).get(fid) or {}).get("sel")
        assert a, (nr, fid)
        out.append((f[1], a))
    return out


def gesichert():
    """Hinweis bei der Aufgabe im Arbeitsblatt: {Aufgabennr: Text}."""
    out = {}
    for n, S in SICHERUNG.items():
        if S["teile"]:
            for nr, ids in S["teile"]:
                out[str(nr)] = "Am Ende der Stunde sichern wir gemeinsam: " + ", ".join(buchstaben(nr, ids)) + "."
        else:
            # Hinweis bei der Aufgabe direkt VOR der Sicherung; liegt keine davor (Stunde 5), bei der Aufgabe danach
            rows = STUNDE[n]; ib = next(i for i, r in enumerate(rows) if r[3] == "bespr")
            vorher = [int(r[3][1:]) for r in rows[:ib] if re.match(r"a\d+$", r[3])]
            if vorher: out[str(vorher[-1])] = "Am Ende der Stunde: " + S["auch"][0] + "."
            else:
                nach = [int(r[3][1:]) for r in rows[ib:] if re.match(r"a\d+$", r[3])]
                out[str(nach[0])] = "Vor dieser Aufgabe, nach den Präsentationen: " + S["auch"][0] + "."
    return out


for _n in SICHERUNG:
    assert len(SICHERUNG[_n]["merken"]) == 2 and SICHERUNG[_n]["auch"], _n
    for _nr, _ids in SICHERUNG[_n]["teile"]:
        assert _nr in aufgaben_der(PLAN[I.KLASSEN[0]][_n - 1])[0], (_n, _nr)
        sicherung_fragen(_nr, _ids)

BALKEN_TEXT = {"demo": "Jetzt DEMO am Lehrertisch: {d}. Erst vermuten – ABCD-Karte bereit, dann schauen.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "gruppen": "Jetzt: Gruppen auslosen – merk dir deine Gruppennummer und tipp sie in Aufgabe 3 an.",
               "freigabe": "Jetzt FREIGABE: Prof. HOLZER kommt zu jeder Gruppe. Plan bereithalten, erst danach wird gebaut.",
               "probe": "Jetzt in der Gruppe: Präsentation vorbereiten und mit Stoppuhr proben – höchstens 3 Minuten.",
               "peer": "Jetzt PARTNERCHECK: {t}.",
               "praes": "Jetzt präsentieren alle sieben Gruppen. Handy weg, du schreibst auf Papier mit – danach tippst du es in Aufgabe 7 ab.",
               "selbst": "Jetzt: bei Aufgabe 1 »Auflösung zeigen« – was hast du in Stunde 1 gedacht?",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {Aufgabennr: [[Marke, Text], …]}, "nach": {Aufgabennr: […]}}.
    Phasen vor der ersten Aufgabe einer Stunde stehen schon im Kasten »So läuft die Stunde« – außer DEMO und KURZ KLÄREN."""
    vor, nach = {}, {}
    for n, rows in STUNDE.items():
        warte, erste, letzte = [], True, None
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte: vor[nr] = vor.get(nr, []) + warte
                warte, erste, letzte = [], False, nr
                continue
            if art in ("org", "reserve", "pdf") or (erste and art == "wdh"): continue
            t = re.sub(r"^(KURZ KLÄREN|SICHERUNG|PARTNERCHECK|DEMO K2\.1-D1): ", "", text).split(" (")[0].split(" – ")[0]
            warte.append([marke, BALKEN_TEXT[art].format(d=DEMO_NAME.get(n, ""), t=t, s=sicherung_kurz(n))])
        if warte and letzte: nach[letzte] = warte
    return {"vor": vor, "nach": nach}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – OHNE Datum und ohne Klasse (beide Klassen gleich), aus PLAN erzeugt, nicht von Hand."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        n = st["std"]
        nrs, _ = aufgaben_der(st)
        auf = bereich(nrs) if nrs else "–"
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n], "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Behauptungen prüfen, Druck rechnen, Forschung prüfen, virtueller Versuch am Handy (PhET), Lesen und prüfen: Winterreifen im Test",
              "aufgaben": "Zusatz 9–13", "zeit": "ca. 53 min", "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"})
    return z


FAHRPLAN_TEXT = ("Sechs Stunden, ein Gruppenprojekt: Stunde 1 mit der ganzen Klasse, Stunden 2 bis 4 selbstständig in der Gruppe, "
                 "Stunde 5 präsentieren alle, Stunde 6 löst du Aufgabe 8 allein. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. "
                 "Keine Hausübung. Welche Stunde heute dran ist, sagt dir Prof. HOLZER – die Reihenfolge zählt, nicht das Datum.")

STUNDENVORSCHLAG = {
 k: [[str(st["std"]),
      LESEN[st["std"]],
      "selbst gewählt (Gruppen)" if st["std"] == 3 else ("Präsentationen" if st["std"] == 5 else ("DEMO K2.1-D1" if st["std"] == 6 else "–")),
      bereich(aufgaben_der(st)[0]) or "–",
      f"{ARBEIT} min Arbeit + 10 min Org./Reserve",
      METHODE[st["std"]]] for st in PLAN[k]] for k in I.KLASSEN}

assert sum(t["zeit"] for t in I.T if t["tag"] == "Zusatz") == 53, sum(t["zeit"] for t in I.T if t["tag"] == "Zusatz")


if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} · {I.STUNDENTITEL[n]} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {mk:13s} {name}")
            t += mi
        print("   Kette:", " → ".join(x[1] for x in folge(n)))
        print("   Sicherung:", sicherung_kurz(n))
        print("   Referat:", kuerzen_text(n)[:160], "…")
    print(len(VARIANTEN), "Varianten ·", balken())
