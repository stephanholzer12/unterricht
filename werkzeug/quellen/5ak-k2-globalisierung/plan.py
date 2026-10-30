"""Zeitplan K2 Globalisierung und aktuelle Weltpolitik – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarten (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Annahme laut Übergabe: 50 min je Stunde. Fr 13.11., Fr 20.11. (zuerst 20 min angekündigter Test, Stoff und Nummer unbekannt – nichts ergänzt), Fr 27.11., Fr 04.12.2026.
Minutenplan der ChatGPT-Übergabe (Abschnitt 7) übernommen und nach Regelwerk angepasst: Klassenbuch (2 min) je Stunde, Besprechung als eigene Phase, Reserve je Stunde,
Methodenwechsel (nie dieselbe Methode in zwei Stunden hintereinander), je Stunde eine Phase ohne Handy. Aufgabe 8 besteht aus drei Phasen (8a, 8b, 8c) – ihre Summe ist die Aufgabenzeit.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "erkl" kurze Erklärung · "test" · "org" · "bespr" · "reserve" · "pdf".
Lesezeit aus der Wortzahl (ca. 130 Wörter/min, theorie_daten.py) – wird unten geprüft."""
import inhalt as I

MIN = 50

S1 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Einstieg: »Ist eine österreichische Marke automatisch ein österreichisches Produkt?« – zwei Vermutungen an die Tafel", 3, True, "org"),
      ("Lesen: Theorieteil »Was Globalisierung verbindet«, »Wie die Verflechtung entstand«, »Warum Unternehmen weltweit arbeiten«", 4, False, "lesen"),
      ("Kurz klären: Begriff, Antriebskräfte, Strömeübersicht am Bild", 4, True, "erkl"),
      ("Aufgabe 1 zu zweit: Flussbild der Sportuhr auf Papier, dann Foto und Einträge", 14, False, "a1"),
      ("Besprechung Aufgabe 1: Beispiel-Flussbild und Engpässe an der Tafel", 3, True, "bespr"),
      ("Lesen: Theorieteil »Wer gewinnt – und wer trägt die Kosten?«", 2, False, "lesen"),
      ("Aufgabe 2 allein (Heft, dann Handy)", 10, False, "a2"),
      ("Besprechung Aufgabe 2: zwei verkürzte Aussagen korrigieren", 4, True, "bespr"),
      ("Sicherung auf Papier: »Unsere Uhr wäre besonders verwundbar, wenn …, weil …«", 2, True, "org"),
      ("Reserve", 2, True, "reserve")]

S2 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Angekündigter Test inkl. Austeilen und Einsammeln (Stoff und Testnummer: nicht in dieser PPP)", 20, True, "test"),
      ("Wiedereinstieg: Sportuhr erinnern, Modellimport in die USA vorstellen", 1, True, "org"),
      ("Lesen: Theorieteil »Zölle: Wer zahlt – und wer trägt die Last?« (mit Karte A)", 2, False, "lesen"),
      ("Aufgabe 3 allein rechnen, kurzer Partnercheck", 8, False, "a3"),
      ("Besprechung Aufgabe 3: Zahler und Last unterscheiden", 2, True, "bespr"),
      ("Lesen: Theorieteil »Wer organisiert Regeln und Finanzierung?« (mit Karte B)", 2, False, "lesen"),
      ("Aufgabe 4 in Dreiergruppen: Vergleichskarte und drei Fälle", 9, False, "a4"),
      ("Sicherung: je Organisation ein Auftrag und eine Grenze · Namenskarte kurz prüfen", 3, True, "bespr"),
      ("Reserve", 1, True, "reserve")]

S3 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Einstieg: vier Bedeutungen von »Übernahme« an der Tafel zuordnen", 3, True, "org"),
      ("Lesen: Theorieteil »KI braucht Daten, Chips, Strom und Regeln« (Karten C–E)", 3, False, "lesen"),
      ("Aufgabe 5 zu zweit: Fallkarten sortieren, EU und USA vergleichen", 10, False, "a5"),
      ("Kurz klären: Modell oder Anwendung · Verbot, Hochrisiko, Transparenz an je einem Beispiel", 3, True, "erkl"),
      ("Lesen: Theorieteil »KI-Risiken prüfen« und die eigene Quellenkarte", 3, False, "lesen"),
      ("Aufgabe 6 arbeitsteilig: Quellenkarten 1–4, gemeinsame Tabelle", 14, False, "a6"),
      ("Aufgabe 7 allein: fehlerhaften KI-Text korrigieren", 8, False, "a7"),
      ("Besprechung Aufgaben 5–7 · Sicherung auf Papier: eine Schutzmaßnahme und ihre Grenze", 3, True, "bespr"),
      ("Reserve", 1, True, "reserve")]

S4 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Rückblick: Sportuhr und drei Institutionenkarten · Aktualitätshinweis (KI-Frist 02.12.)", 2, True, "org"),
      ("Lesen: Theorieteil »Kosten verteilen und Abhängigkeiten verringern«", 3, False, "lesen"),
      ("Aufgabe 8a: vier Perspektivgruppen bereiten Argumente und Maßnahme vor", 7, False, "a8"),
      ("Aufgabe 8b: strukturierte Diskussion ohne Handy", 13, True, "a8"),
      ("Aufgabe 8c: eigenes Urteil mit der Hand schreiben (100–130 Wörter), dann Foto", 10, True, "a8"),
      ("Foto 8c und Einträge aus 8b nachtragen, dann Selbstcheck: sechs Quizfragen", 5, False, "bespr"),
      ("PDF erstellen und in LMS hochladen", 4, False, "pdf"),
      ("Brücke: »Wenn Regeln und Technik Macht schaffen – was macht dann die Macht des Westens aus?«", 2, True, "org"),
      ("Reserve", 2, True, "reserve")]

M = {1: "Handzeichen + Flussbild auf Papier zu zweit + Tafel",
     2: "Test + Rechnung allein + Dreiergruppen-Matrix",
     3: "Fallkarten sortieren + arbeitsteilige Quellenkarten + Textkorrektur allein",
     4: "Perspektivgruppen + strukturierte Diskussion + Handschrift"}

PLAN = {k: [{"std": n, "datum": I.DATEN[k][n], "teile": [n], "methode": M[n], "phasen": ph} for n, ph in ((1, S1), (2, S2), (3, S3), (4, S4))] for k in I.KLASSEN}


def _ab(st, name):
    t = 0
    for n, m, o, a in st["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


_st = PLAN[I.KLASSEN[0]]
KNAPP = {}
for k in I.KLASSEN:
    KNAPP[(k, 1)] = (f"Zeitstopp: Um Minute {_ab(_st[0], 'Aufgabe 2')} beginnt Aufgabe 2. Wird es knapp: Die Kurzerklärung auf Begriff und eine Antriebskraft kürzen und die Besprechung von Aufgabe 1 auf zwei Beispiele. "
                     "Aufgabe 1 und 2 bleiben vollständig.")
    KNAPP[(k, 2)] = ("Der Test hat Vorrang. Nach dem Test bleiben 28 Minuten: Wird es knapp, zuerst den Namensüberblick (Karte B) kürzen, dann die Besprechung von Aufgabe 3. "
                     "Aufgabe 4 nicht streichen; notfalls den letzten Fall als Einstieg in Stunde 4 sichern.")
    KNAPP[(k, 3)] = (f"Zeitstopp: Um Minute {_ab(_st[2], 'Aufgabe 6')} beginnt Aufgabe 6. Wird es knapp: Aufgabe 5 b (EU/USA) mündlich und die Besprechung am Ende auf die Schutzmaßnahme kürzen. "
                     "Die vier Bedeutungen von »Übernahme« bleiben Pflicht.")
    KNAPP[(k, 4)] = (f"Zeitstopp: Um Minute {_ab(_st[3], 'Aufgabe 8a')} beginnt Aufgabe 8a. Wird es knapp: Selbstcheck auf drei Fragen kürzen; die PDF darf auch nach dem Läuten hochgeladen werden. "
                     "Kein Rollentribunal, keine Referate, kein Film zusätzlich.")

_Z = {t["nr"]: t["zeit"] for t in I.T}
for k, stunden in PLAN.items():
    nrs = []
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org", "test")), (k, st["std"], "keine Phase ohne Handy")
        assert any(p[3] == "reserve" for p in st["phasen"]), (k, st["std"], "keine Reserve")
        summen = {}
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"): summen[int(art[1:])] = summen.get(int(art[1:]), 0) + mi
        for n, mi in summen.items():
            nrs.append(n); assert mi == _Z[n], (k, n, mi, _Z[n])
            assert [t for t in I.T if t["nr"] == n][0]["h"] == st["std"], (k, n, "Aufgabe in falscher Stunde")
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)
assert len(set(M.values())) == 4


def aufgaben_der(st):
    return sorted({int(p[3][1:]) for p in st["phasen"] if p[3].startswith("a")}), []


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


def minuten(st, arten):
    return sum(p[1] for p in st["phasen"] if any(p[3].startswith(a) for a in arten))


LESEN = {1: "Einstieg + Verflechtung, Entstehung, Standortwahl, Folgen (Buch S. 43–48, 64–70)",
         2: "Zölle (Karte A) und WTO, IWF, Weltbank (Karte B) (Buch S. 50–63)",
         3: "KI braucht Daten, Chips, Strom und Regeln · KI-Risiken prüfen (Ergänzung zu Buch S. 48)",
         4: "Kosten verteilen und Abhängigkeiten verringern (Buch S. 65–77)"}
WIE = {1: "ohne Handy: Einstieg an der Tafel, Flussbild auf Papier, Besprechung",
       2: "zuerst Test; ohne Handy: Wiedereinstieg und Sicherung",
       3: "ohne Handy: Einstieg, kurze Klärung, Sicherung auf Papier",
       4: "ohne Handy: Rückblick, Diskussion 8b, Urteil 8c mit der Hand"}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        nrs, _ = aufgaben_der(st)
        teile = [f"Lesen {minuten(st, ['lesen'])} min", f"Aufgaben {minuten(st, ['a'])} min", f"Besprechung {minuten(st, ['bespr'])} min", f"Reserve {minuten(st, ['reserve'])} min"]
        if minuten(st, ["test"]): teile.insert(0, f"Test {minuten(st, ['test'])} min")
        rest = MIN - minuten(st, ["lesen", "a", "bespr", "reserve", "test"])
        teile.insert(len(teile) - 1, f"Organisation, Erklärung{', PDF' if st['std'] == 4 else ''} {rest} min")
        z.append({"wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": LESEN[st["std"]],
                  "aufgaben": bereich(nrs) + (" · Selbstcheck-Quiz (6 Fragen)" if st["std"] == 4 else ""),
                  "zeit": " · ".join(teile), "wie": WIE[st["std"]],
                  "abgabe": "Arbeitsblatt-PDF in LMS (alle Aufgaben 1–8)" if st["std"] == 4 else "Antworten bleiben am Handy gespeichert"})
    return z


FAHRPLAN_TEXT = ("Dafür sind 4 Stunden eingeplant (Fr 13.11., Fr 20.11., Fr 27.11., Fr 04.12.). Lies den jeweiligen Abschnitt im Theorieteil, "
                 "mach die Aufgaben 1–8 im Arbeitsblatt und gib am 04.12. die PDF in LMS ab. Am 20.11. schreibst du zuerst den angekündigten Test. Keine Hausübung.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for st in PLAN[I.KLASSEN[0]]:
        t = 0; print("Stunde", st["std"], st["datum"])
        for p in st["phasen"]: print(f"  {t:2d}–{t + p[1]:2d}  {p[0]}{' (ohne Handy)' if p[2] else ''}"); t += p[1]
