"""Zeitplan K2.1 Mechanische Kräfte – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Regiefolien der Unterrichts-PPP und Lösungsmappe.
Neue Standards 07.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Sechs Einzelstunden, jede Stunde ist abgeschlossen.
KEINE DATEN in dieser Quelle und auf den Kadetten-Seiten (Stephan, 13.11.2026): Termine, Doppelstunden und Referate ändern sich ständig. Prof. HOLZER trägt sie
selbst im Reiter »Kalender« der privaten Lösungsseite ein (Standardwerte stehen in der privaten Datei termine_k2_1.py, nicht im Repository).
Für jeden möglichen Termin liefert dieses Modul den fertigen Ablauf: Einzelstunde, Einzelstunde MIT Referat, Doppelstunde (zwei aufeinanderfolgende Stunden), Doppelstunde MIT Referat.
Beide Klassen bekommen denselben Fahrplan.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "v:<ID>" Gruppenversuch · "erkl" gemeinsame Erklärung · "wdh" Wiederholen ·
"plan" Versuchsplan · "freigabe" · "peer" Peer-Feedback · "praes" Präsentation · "org" · "bespr" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10        # Klassenbuch, Ankommen, Handys, Aufräumen, Puffer
ARBEIT = MIN - ORG_RESERVE
VS = "v:" + I.VS_ID
REFERAT_MIN = 10        # ein Schüler-Referat einschließlich kurzer Rückfragen (Annahme – bei längeren Referaten Reserve und »Wenn es knapp wird« nutzen)
PAUSE = 5               # Doppelstunde: Pause ohne Arbeitszeit
DOPPEL_MIN = 2 * MIN + PAUSE   # z. B. 13.35–15.20 Uhr

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys weg", 6, True, "org"),
     ("Weißt du noch? Drei Fragen aus »Erkenntnisgewinn«", 3, True, "wdh"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1"),
     ("Gemeinsam: Kraftwirkung, Richtung, resultierende Kraft – Kräftebild an der Tafel", 9, True, "erkl"),
     ("Aufgabe 2 am Handy (Theorie-Karten und Tipp-Stufen sind dabei)", 13, False, "a2"),
     ("Besprechung Aufgabe 2: die drei Rechenwege", 3, True, "bespr"),
     ("Gruppen auslosen (Generator), Themen zeigen, »So läuft das Projekt«", 8, True, "erkl"),
     ("Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Wo stehen wir? Gruppe, Thema und Rolle", 3, True, "wdh"),
     ("So arbeitet ihr heute selbstständig – Gruppenkarte im Arbeitsblatt", 2, True, "erkl"),
     ("Aufgabe 3: Thema erarbeiten mit Leitfragen, Buch und Theorie-Seite", 15, False, "a3"),
     ("Aufgabe 4: Versuch aussuchen, Materialliste schreiben (erst auf Papier)", 10, True, "a4"),
     ("Freigabe durch Prof. HOLZER – je Gruppe eine Minute", 8, True, "freigabe"),
     ("Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"),
     ("Wo stehen wir? Plan und Material da?", 2, True, "wdh"),
     ("Sicherheit: was erlaubt ist, wo gearbeitet wird", 3, True, "erkl"),
     ("Aufgabe 5: Versuch aufbauen, machen, Ergebnisse eintragen", 30, True, "a5"),
     ("Versuch einmal so vorführen wie in Stunde 5 (Probe)", 3, True, "peer"),
     ("Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Aufräumen, ausspülen, Material zurück bzw. einpacken", 3, True, "org"),
     ("Reserve", 4, True, "reserve")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Wo stehen wir? Was zeigt unser Versuch?", 3, True, "wdh"),
     ("Aufgabe 6: Steckbrief gemeinsam schreiben", 17, False, "a6"),
     ("Präsentation vorbereiten und mit Stoppuhr proben (3 min)", 10, True, "erkl"),
     ("Partnercheck: andere Gruppe liest den Steckbrief und hört die Probe", 8, True, "peer"),
     ("Handout-PDF in Teams, Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 5: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Start: Mitschrift erklären, Reihenfolge ansagen", 3, True, "erkl"),
     ("Sieben Gruppen präsentieren: je 3 min einschließlich Versuch, 1 min Übergang – alle schreiben mit", 28, True, "praes"),
     ("Das besprechen wir: zwei fachliche Klärungen", 4, True, "bespr"),
     ("Aufgabe 7: Mitschrift ergänzen (Steckbriefe in Teams)", 3, False, "a7"),
     ("Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 6: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Weißt du noch? Drei kurze Rückfragen zu den Gruppenthemen", 3, True, "wdh"),
     ("Gemeinsame Übersicht: Begriffstabelle Kraft – Bewegung – Druck an der Tafel", 8, True, "erkl"),
     ("Aufgabe 8 einzeln und ohne KI", 16, False, "a8"),
     ("Besprechung: drei häufige Denkfehler und die vier Rechenwege", 8, True, "bespr"),
     ("Auflösung der Vorhersagen aus Stunde 1 und Selbsteinschätzung", 3, False, "selbst"),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
}

METHODE = {1: "Gemeinsames Kräftebild an der Tafel, Vorhersage per Handzeichen",
           2: "Selbststudium mit Leitfragen, Versuchsplan auf Papier, Freigabe",
           3: "Selbst gewählter Gruppenversuch mit Probe",
           4: "Steckbrief schreiben, Partnercheck ohne Handy",
           5: "Kurzpräsentationen mit Demonstration, Beobachtungsbogen mit der Hand",
           6: "Begriffstabelle gemeinsam an der Tafel, danach Einzelarbeit"}

ZIEL = {1: "Kraftwirkungen erkennen, Masse und Kraft auseinanderhalten – und wissen, in welcher Gruppe du bist.",
        2: "Das eigene Thema mit den Leitfragen verstehen und einen freigegebenen Versuchsplan haben.",
        3: "Den eigenen Versuch sicher machen, Ergebnisse festhalten und ihn einmal vorführen können.",
        4: "Einen Steckbrief schreiben, mit dem die anderen euer Thema lernen können – und die Präsentation sitzt.",
        5: "Das eigene Thema verständlich zeigen und von allen anderen Gruppen die Kernaussage mitnehmen.",
        6: "Alle sieben Themen selbst erklären und die Einheiten sicher verwenden."}

PLAN = {k: [{"std": n, "teile": [n], "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}
MARKE = {1: "BESPRECHEN", 2: "SELBSTSTUDIUM", 3: "VERSUCH", 4: "GRUPPENARBEIT", 5: "PRÄSENTATION", 6: "SELBSTSTUDIUM"}  # Marken laut Skill 11.11.2026 (GEMEINSAM -> BESPRECHEN, EINZELARBEIT -> SELBSTSTUDIUM)

# ---------------------------------------------------------------- Kontrollen
_Z = {t["nr"]: t["zeit"] for t in I.T}
for n, ph in STUNDE.items():
    assert sum(p[1] for p in ph) == MIN, (n, sum(p[1] for p in ph))
    assert sum(p[1] for p in ph if p[3] in ("org", "reserve")) == ORG_RESERVE, (n, "Organisation und Reserve nicht 10 min")
    assert sum(p[1] for p in ph if p[3] == "reserve") >= 4, (n, "zu wenig Reserve")
    assert any(p[2] for p in ph if p[3] not in ("org", "reserve")), (n, "keine Phase ohne Handy")
_m = [METHODE[n] for n in sorted(METHODE)]
assert all(a != b for a, b in zip(_m, _m[1:])), "zwei gleiche Methoden hintereinander"
assert len(set(_m)) >= 3
# Aufgabenzeiten: jede Pflicht- und Vorhersageaufgabe kommt genau einmal mit der Zeit aus inhalt.py vor
_einmal = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art in ph:
        if re.match(r"a\d+$", art):
            nr = int(art[1:]); _einmal.setdefault(nr, []).append(mi)
for nr, mins in _einmal.items():
    assert len(mins) == 1 and mins[0] == _Z[nr], (nr, mins, _Z[nr])
assert sorted(_einmal) == list(range(1, 9)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall und Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Die Gruppen- und Rollenverteilung auf den Anfang von Stunde 2 verschieben. Aufgabe 2 bleibt – sie ist die Rechengrundlage für Stunde 6.",
 2: "Wenn es knapp wird: Leitfrage 4 und die zweite Quelle (g) dürfen in Stunde 3 nachgeholt werden. Die Freigabe des Plans darf nicht entfallen – wer keine hat, nimmt Idee 1 der Gruppenkarte.",
 3: "Zeitstopp: Nach 41 Minuten wird aufgeräumt, egal wie weit die Gruppen sind. Wenn es knapp wird: Die Probe entfällt, dafür wird in Stunde 4 geprobt. "
    "Fehlt Material von zu Hause: Saal-Variante der Idee nehmen. Nie Werte erfinden – lieber beschreiben, was man gesehen hat.",
 4: "Diese Stunde fällt bei einem Ausfall ZUERST weg: Den Steckbrief schreiben die Gruppen dann in den ersten 15 Minuten von Stunde 5, die Präsentationen werden auf je 2 Minuten gekürzt. "
    "Wenn es nur knapp wird: Den Partnercheck auf zwei Sätze kürzen.",
 5: "Je Gruppe sind 3 Minuten einschließlich Demonstration fest. Wenn es knapp wird: Die Rückmeldung nach jeder Gruppe entfällt, die zwei fachlichen Klärungen bleiben. "
    "Niemals zwei Gruppen gleichzeitig präsentieren lassen.",
 6: "Supplierstunde möglich: Aufgabe 8, die Theorie-Karten und die Selbsteinschätzung brauchen kein Material und keinen Versuch. "
    "Wenn es knapp wird: Die Besprechung auf die beiden Denkfehler »Auftrieb im Gleichgewicht« und »Gegenkraft am anderen Körper« beschränken.",
}
KNAPP = {(k, n): KUERZEN[n] for k in I.KLASSEN for n in KUERZEN}
SUPPLIER = 6
AUSFALL_ZUERST = 4


# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
# Referat: Diese Phasen werden gekürzt (Phasen-Nummer ab 0 -> neue Minuten), zusammen genau REFERAT_MIN. Aufgaben mit Punkten und der Versuch bleiben, soweit es geht.
REF_KUERZEN = {
 1: {1: 0, 3: 7, 6: 5, 7: 0},
 2: {1: 2, 3: 12, 4: 8, 5: 6, 6: 0},
 3: {1: 0, 3: 27, 4: 0, 5: 0},
 4: {1: 1, 2: 14, 3: 8, 4: 5},
 5: {1: 2, 2: 23, 3: 2, 5: 0},
 6: {1: 0, 2: 5, 4: 5, 5: 2},
}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit")
    assert all(STUNDE[_n][i][3] not in ("org", "reserve") for i in _c), (_n, "Organisation und Reserve bleiben")
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
# Doppelstunde (zwei aufeinanderfolgende Stunden a, a+1): Klassenbuch, »Weißt du noch?«, Zwischenstand-PDF der ersten und Reserve der ersten entfallen
# (nur einmal nötig). Die gewonnenen Minuten bleiben als Puffer oder reichen für ein Referat.
DOPPEL_HINWEIS = {
 (1, 2): "Gut machbar. Gruppen auslosen und gleich in die selbstständige Arbeit gehen.",
 (2, 3): "Achtung: Material von zu Hause kann nicht mitgebracht werden – alle Gruppen nehmen die Saal-Variante (Idee 1).",
 (3, 4): "Sehr gut: Versuch und Steckbrief hintereinander, nur einmal auf- und abbauen.",
 (4, 5): "Gut: Steckbrief schreiben und gleich präsentieren. Handout vor den Präsentationen in Teams stellen lassen.",
 (5, 6): "Gut: Nach den Präsentationen gleich Aufgabe 8. Die Steckbriefe stehen in Teams.",
}


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]
            note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
        z.append([name, neu, bool(oh), art, note])
    return z


def _chip(art, oh):
    return bool(oh) and art not in ("org", "reserve", "bespr", "erkl", "pause", "referat", "wdh")


def _referat_zeile():
    return ["Referat einer Mitschülerin bzw. eines Mitschülers einschließlich kurzer Rückfragen", REFERAT_MIN, True, "referat", ""]


def variante(a, doppel=False, referat=False):
    """Ablauf als Liste [Name, Minuten, ohne Handy, Art, Hinweis]. Einzelstunde: Summe 50. Doppelstunde: Summe 105 (mit Pause)."""
    if not doppel:
        z = _zeilen(a, REF_KUERZEN[a] if referat else None)
        if referat:
            z.insert(1, _referat_zeile())
        assert sum(r[1] for r in z) == MIN, (a, referat, sum(r[1] for r in z))
        return z
    b = a + 1
    za = [r for r in _zeilen(a) if r[3] not in ("pdf", "reserve")]
    zb = [r for r in _zeilen(b)][1:]            # Klassenbuch entfällt
    zb = [r for r in zb if r[3] != "wdh"]       # »Weißt du noch?« entfällt
    z = za + [["Pause (keine Arbeitszeit)", PAUSE, True, "pause", ""]] + zb
    if referat:
        z.insert(1, _referat_zeile())
    rest = DOPPEL_MIN - sum(r[1] for r in z)
    assert rest >= 0, (a, referat, rest)
    if rest:
        z.append(["Puffer, Verlängerung der Arbeitsphasen oder ein Ausgleichsbaustein (Reiter »Ausgleich«)" if rest >= 10 else "Puffer", rest, True, "reserve", ""])
    assert sum(r[1] for r in z) == DOPPEL_MIN, (a, referat)
    return z


VARIANTEN = {}
for _n in sorted(STUNDE):
    for _r in (False, True):
        VARIANTEN["%d%s" % (_n, "R" if _r else "")] = variante(_n, False, _r)
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = variante(_n, True, _r)


def kuerzen_text(n):
    """»Weißt du noch? entfällt · Kräftebild 9 -> 7 min · …« – was bei einem Referat in Stunde n geändert wird."""
    out = []
    for i, m in sorted(REF_KUERZEN[n].items()):
        name, mi = STUNDE[n][i][0], STUNDE[n][i][1]
        kurz = re.split(r"[:–(?]| einschließlich", name)[0].strip()
        out.append(f"{kurz} entfällt" if m == 0 else f"{kurz} {mi} auf {m} min")
    return " · ".join(out)


def aufgaben_der(st):
    nrs, zus = [], []
    for name, mi, oh, art in st["phasen"]:
        if art.startswith("a") and art != "org": nrs.append(int(art[1:]))
        if art.startswith("z"): zus.append(int(art[1:]))
    return sorted(set(nrs)), sorted(set(zus))


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
         6: "Teile 3 bis 8 als Nachschlagewerk · Buch S. 50–61 · Fachbegriffe"}


ABGABE = {1: "–", 2: "Plan freigeben lassen", 3: "–", 4: "Handout-PDF in Teams (Schriftführung)", 5: "–", 6: "Arbeitsblatt-PDF in LMS"}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – OHNE Datum und ohne Klasse (beide Klassen gleich), aus PLAN erzeugt, nicht von Hand."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        n = st["std"]
        nrs, _ = aufgaben_der(st)
        auf = bereich(nrs) if nrs else "–"
        if n == 6: auf += " · Quiz freiwillig"
        z.append({"wann": f"Stunde {n}", "marke": MARKE[n], "lesen": LESEN[n], "aufgaben": auf, "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Druck selbst nachrechnen, Forschungsbeitrag prüfen)",
              "aufgaben": "Zusatz 9–11", "zeit": "ca. 26 min", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Sechs Stunden, ein Gruppenprojekt: Stunde 1 mit der ganzen Klasse, Stunden 2 bis 4 selbstständig in der Gruppe, "
                 "Stunde 5 präsentieren alle, Stunde 6 löst du Aufgabe 8 allein. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. "
                 "Keine Hausübung. Welche Stunde heute dran ist, sagt dir Prof. HOLZER – die Reihenfolge zählt, nicht das Datum.")

STUNDENVORSCHLAG = {
 k: [[str(st["std"]),
      LESEN[st["std"]],
      "selbst gewählt (Gruppen)" if st["std"] == 3 else ("Präsentationen" if st["std"] == 5 else "–"),
      bereich(aufgaben_der(st)[0]) or "–",
      f"{minuten(st, ['a', 'v:', 'plan', 'praes', 'peer', 'freigabe', 'selbst'])} min Arbeit · {minuten(st, ['reserve'])} min Reserve",
      METHODE[st["std"]]] for st in PLAN[k]] for k in I.KLASSEN}


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
        print("   Kürzen:", KUERZEN[n][:90], "…")
