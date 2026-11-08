"""Zeitplan K2.1 Mechanische Kräfte – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Regiefolien der Unterrichts-PPP und Lösungsmappe.
Neue Standards 07.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Sechs Einzelstunden, jede Stunde ist abgeschlossen.
Keine festen Daten: Der Plan weicht oft ab (Ausfälle, Tests, Veranstaltungen). Es zählt die Reihenfolge der Stunden, nicht das Datum.
Beide Klassen bekommen denselben Fahrplan. Die 1AK darf Stunde 3 und 4 als Doppelstunde verbinden (Pause ohne Arbeitszeit) – Prof. HOLZER entscheidet.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "v:<ID>" Gruppenversuch · "erkl" gemeinsame Erklärung · "wdh" Wiederholen ·
"plan" Versuchsplan · "freigabe" · "peer" Peer-Feedback · "praes" Präsentation · "org" · "bespr" · "pdf" · "reserve"."""
import inhalt as I

MIN = 50
ORG_RESERVE = 10        # Klassenbuch, Ankommen, Handys, Aufräumen, Puffer
ARBEIT = MIN - ORG_RESERVE
VS = "v:" + I.VS_ID

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys weg", 6, True, "org"),
     ("Weißt du noch? Drei Fragen aus »Erkenntnisgewinn«", 3, True, "wdh"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1"),
     ("Gemeinsam: Kraftwirkung, Richtung, resultierende Kraft – Kräftebild an der Tafel", 9, True, "erkl"),
     ("Aufgabe 2 am Handy (Theorie-Karten und Tipp-Stufen sind dabei)", 13, False, "a2"),
     ("Besprechung Aufgabe 2: die drei Rechenwege", 3, True, "bespr"),
     ("Sieben Gruppen bilden, Themen und Rollen verteilen, Buchseiten zeigen", 8, True, "erkl"),
     ("Zwischenstand als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Wo stehen wir? Gruppe, Thema und Rolle noch einmal nennen", 3, True, "wdh"),
     ("Eigene Vermutung in der Gruppe festhalten (noch ohne Handy, auf Papier)", 4, True, "erkl"),
     ("Gezielte Recherche: zugewiesene Buchseiten und eine zweite Quelle prüfen", 15, False, "a3"),
     ("Versuchsplan schreiben: geänderte Bedingung, gleich bleibende Bedingungen, Messfelder", 9, True, "plan"),
     ("Freigabe durch Prof. HOLZER – je Gruppe ungefähr eine Minute", 7, True, "freigabe"),
     ("Meilenstein-PDF der Gruppe", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"),
     ("Wo stehen wir? Plan der eigenen Gruppe noch einmal lesen", 3, True, "wdh"),
     ("Sicherheit und Materialverteilung, Plätze zeigen", 4, True, "erkl"),
     ("Messphase: Aufbau und Messung – Kraftmesserwechsel nach 14 min", 28, True, VS),
     ("Erste Deutung in der Gruppe notieren (noch am Platz)", 3, False, "erkl"),
     ("Aufräumen, ausspülen, Geräte zurück", 3, True, "org"),
     ("Meilenstein-PDF der Gruppe", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Wo stehen wir? Messwerte der Gruppe vorlesen", 3, True, "wdh"),
     ("Daten prüfen und Grenzen ergänzen: Was zeigt euer Versuch nicht?", 12, False, "erkl"),
     ("Drei-Minuten-Erklärung vorbereiten (Beobachtung – Deutung – Grenze)", 10, True, "erkl"),
     ("Partnergruppe prüft nach dem Raster und gibt Rückmeldung", 8, True, "peer"),
     ("Überarbeiten", 5, False, "erkl"),
     ("Meilenstein-PDF der Gruppe", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 5: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Start und Beobachtungsauftrag für die Zuhörer erklären", 3, True, "erkl"),
     ("Sieben Gruppen präsentieren: je 3 min einschließlich Versuch, 1 min Übergang", 28, True, "praes"),
     ("Zwei gemeinsame fachliche Klärungen", 4, True, "bespr"),
     ("Beobachtungsübersicht vervollständigen (Aufgabe 3 c)", 3, False, "a3"),
     ("Endprodukt der Gruppe als PDF sichern", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
 6: [("Beginn: Klassenbuch, Anwesenheit", 6, True, "org"),
     ("Weißt du noch? Drei kurze Rückfragen zu den Gruppenthemen", 3, True, "wdh"),
     ("Gemeinsame Übersicht: Begriffstabelle Kraft – Bewegung – Druck an der Tafel", 8, True, "erkl"),
     ("Aufgabe 4 einzeln und ohne KI", 16, False, "a4"),
     ("Besprechung: drei häufige Denkfehler und die vier Rechenwege", 8, True, "bespr"),
     ("Auflösung der Vorhersagen aus Stunde 1 und Selbsteinschätzung", 3, False, "selbst"),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf"),
     ("Reserve", 4, True, "reserve")],
}

METHODE = {1: "Gemeinsames Kräftebild an der Tafel, Vorhersage per Handzeichen",
           2: "Recherche in der Gruppe mit Buch und zweiter Quelle, Plan auf Papier",
           3: "Gruppenversuch an Plätzen im Saal (Handy nur als Stoppuhr und Protokoll)",
           4: "Peer-Feedback zwischen zwei Gruppen nach Raster, ohne Handy",
           5: "Kurzpräsentationen mit Demonstration, Beobachtungsbogen mit der Hand",
           6: "Begriffstabelle gemeinsam an der Tafel, danach Einzelarbeit"}

ZIEL = {1: "Kraftwirkungen erkennen, Masse und Kraft auseinanderhalten – und wissen, in welcher Gruppe du bist.",
        2: "Eine prüfbare Frage, zwei geprüfte Quellen und einen freigegebenen Versuchsplan haben.",
        3: "Echte Messwerte aufnehmen und sofort eine erste Deutung dazuschreiben.",
        4: "Aus den Messwerten eine Erklärung mit einer Grenze machen – und sie in drei Minuten erzählen können.",
        5: "Das eigene Thema verständlich zeigen und von allen anderen Gruppen eine Kernaussage mitnehmen.",
        6: "Alle sieben Themen selbst erklären und die Einheiten sicher verwenden."}

PLAN = {k: [{"std": n, "datum": "geplant", "teile": [n], "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}

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
# Aufgabenzeiten: Aufgabe 1, 2 und 4 kommen genau einmal mit der Zeit aus inhalt.py vor; Aufgabe 3 läuft über mehrere Stunden
_einmal = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art in ph:
        if art.startswith("a") and art != "a3":
            nr = int(art[1:]); _einmal.setdefault(nr, []).append(mi)
for nr, mins in _einmal.items():
    assert len(mins) == 1 and mins[0] == _Z[nr], (nr, mins, _Z[nr])
assert sorted(_einmal) == [1, 2, 4], sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall und Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Die Gruppen- und Rollenverteilung auf den Anfang von Stunde 2 verschieben. Aufgabe 2 bleibt – sie ist die Rechengrundlage für Stunde 6.",
 2: "Wenn es knapp wird: Nur EINE zweite Quelle statt zweier verlangen und das als Grenze notieren. Die Freigabe des Plans darf nicht entfallen.",
 3: "Zeitstopp: Nach 41 Minuten wird aufgeräumt, egal wie weit die Gruppen sind. Wenn es knapp wird: Die freiwillige zweite Messreihe (Gruppe 4: 400 ml) entfällt. "
    "Nie Pflichtmesswerte streichen und keine Modellwerte eintragen – lieber qualitativ auswerten und die Grenze dokumentieren.",
 4: "Diese Stunde fällt bei einem Ausfall ZUERST weg. Das Meilenstein-PDF aus Stunde 3 enthält schon Frage, Messwerte, Kernaussage und Grenze und taugt als Präsentationsunterlage. "
    "Wenn es nur knapp wird: Das Peer-Feedback auf zwei Sätze kürzen.",
 5: "Je Gruppe sind 3 Minuten einschließlich Demonstration fest. Wenn es knapp wird: Die Rückmeldung nach jeder Gruppe entfällt, die zwei fachlichen Klärungen bleiben. "
    "Niemals zwei Gruppen gleichzeitig präsentieren lassen.",
 6: "Supplierstunde möglich: Aufgabe 4, die Theorie-Karten und die Selbsteinschätzung brauchen kein Material und keinen Versuch. "
    "Wenn es knapp wird: Die Besprechung auf die beiden Denkfehler »Auftrieb im Gleichgewicht« und »Gegenkraft am anderen Körper« beschränken.",
}
KNAPP = {(k, n): KUERZEN[n] for k in I.KLASSEN for n in KUERZEN}
SUPPLIER = 6
AUSFALL_ZUERST = 4


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


LESEN = {1: "Einstieg + Teil 1 · Was eine Kraft bewirkt + Teil 2 · Geschwindigkeit · Buch S. 45–49",
         2: "Teil des eigenen Gruppenthemas (Theorie-Seite) + zugewiesene Buchseiten + eine zweite Quelle",
         3: "Versuchsseite: eigener Gruppenauftrag · Gruppenprojekt " + I.VS_ID,
         4: "Theorie-Karte des eigenen Themas noch einmal · Versuchsseite auswerten",
         5: "Alle sieben Themen hören · Beobachtungsauftrag",
         6: "Teile 3 bis 8 als Nachschlagewerk · Buch S. 50–61 · Fachbegriffe"}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        n = st["std"]
        nrs, _ = aufgaben_der(st)
        auf = bereich(nrs) if nrs else "–"
        if n in (2, 3, 4, 5): auf = (auf + " · " if nrs else "") + "Gruppen-Protokoll"
        if n == 6: auf += " · Quiz freiwillig"
        m_auf = minuten(st, ["a", "v:", "plan", "praes", "peer", "freigabe", "selbst"])
        m_res = minuten(st, ["reserve"]); m_bes = minuten(st, ["bespr"])
        zeit = (f"Aufgaben und Projekt ca. {m_auf} min · " + (f"Besprechung {m_bes} min · " if m_bes else "") + f"Reserve {m_res} min")
        ohne = [p[0].split(":")[0].split(" (")[0] for p in st["phasen"] if p[2] and p[3] not in ("org", "reserve", "bespr", "wdh")]
        wie = ("ohne Handy: " + ", ".join(dict.fromkeys(ohne))) if ohne else "am Handy"
        if n == 3: abgabe = "Meilenstein-PDF der Gruppe"
        elif n == 5: abgabe = "Gruppen-PDF in LMS"
        elif n == 6: abgabe = "Arbeitsblatt-PDF in LMS"
        else: abgabe = "Zwischenstand als PDF"
        z.append({"wann": f"Stunde {n}", "datum": "geplant", "lesen": LESEN[n], "aufgaben": auf, "zeit": zeit, "wie": wie, "abgabe": abgabe})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Druck selbst nachrechnen, Forschungsbeitrag prüfen)",
              "aufgaben": "Zusatz 5–7", "zeit": "ca. 26 min", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Diese Einheit ist ein Projekt über sechs Stunden. In Stunde 1 lernst du die Grundbegriffe und bekommst dein Gruppenthema. "
                 "In den Stunden 2 bis 4 plant, messt und erklärt eure Gruppe. In Stunde 5 präsentieren alle sieben Gruppen. "
                 "In Stunde 6 verbindest du alle Themen und löst Aufgabe 4 allein. Die Daten sind geplant – es kann sich etwas verschieben, die Reihenfolge bleibt. "
                 "Pflichtaufgaben werden in der Stunde fertig, es gibt keine Hausübung. Abgabe: dein Arbeitsblatt-PDF und das Gruppen-PDF in LMS.")

STUNDENVORSCHLAG = {
 k: [[str(st["std"]),
      LESEN[st["std"]],
      I.VS_ID if any(p[3] == VS for p in st["phasen"]) else ("Präsentationen" if st["std"] == 5 else "–"),
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
