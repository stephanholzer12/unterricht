"""Zeitplan K2.1 Globalisierung – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Regiefolien der TH-Unterricht und Lösungsmappe.
Stephan (11.11.2026): Fr 13.11. = Stunde 1 (volle Stunde), Fr 20.11. = Stunde 2 mit angekündigtem Test. Institutionen folgen ab Fr 27.11. (eigene Einheit).
Regel 06.11.2026: 50 min = 10 min Organisation und Reserve + 40 min Arbeit. Stunde 2: Test (Annahme 20 min, Dauer von Stephan bestätigen) + ca. 20 min Unterricht.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "erkl" kurze Erklärung/Einstieg · "test" · "org" · "bespr" · "reserve" · "pdf".
Lesezeit aus der Wortzahl (ca. 130 Wörter/min, theorie_daten.py)."""
import inhalt as I

MIN = 50

S1 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"),
      ("Einstieg: Begriffe zur Globalisierung an die Tafel sammeln (Buch S. 42) · Vermutung »Wann begann sie?« per Handzeichen", 4, True, "erkl"),
      ("Lesen: Theorie-Karte »Wann begann die Globalisierung?« und Buch S. 43–44", 3, False, "lesen"),
      ("Aufgabe 1: drei Beginn-Ereignisse, Rechnung, Begründung (Handy)", 9, False, "a1"),
      ("Gemeinsam: Besprechung Aufgabe 1 · Impuls »Folgen für die Weltgeschichte?« (Kolumbus, China-Flotte) · Quellenkritik an der Überschrift", 5, True, "bespr"),
      ("Lesen: Theorie-Karte »Sechs Antriebskräfte« und Buch S. 45–47", 4, False, "lesen"),
      ("Aufgabe 2: Antriebskräfte zuordnen, Liberalisierung erklären (Handy)", 10, False, "a2"),
      ("Besprechung Aufgabe 2: Zuordnung und Liberalisierung an der Tafel", 3, True, "bespr"),
      ("Sicherung ins Heft: Merksatz »Kein einzelner Beginn – sechs Antriebskräfte« · Ausblick Stunde 2", 2, True, "erkl"),
      ("Reserve", 7, True, "reserve")]

S2 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"),
      ("Angekündigter Test inkl. Austeilen und Einsammeln (Dauer angenommen, Stoff und Testnummer: nicht in dieser PPP)", 20, True, "test"),
      ("Weißt du noch? Drei Fragen aus Stunde 1, mündlich", 3, True, "erkl"),
      ("Lesen: Theorie-Karte »Digital Divide« und Buch S. 48", 2, False, "lesen"),
      ("Aufgabe 3: Zahlen zum Digital Divide auswerten (Handy)", 8, False, "a3"),
      ("Besprechung Aufgabe 3: Zahlen, Quellenkritik (Buch 32 % gegen ITU)", 2, True, "bespr"),
      ("Statement-Ampel im Raum: »Ziele erreicht?« (Buch S. 51), zwei Aussagen", 5, True, "erkl"),
      ("PDF erstellen und in LMS hochladen (darf auch nach dem Läuten)", 2, False, "pdf"),
      ("Reserve", 5, True, "reserve")]

M = {1: "Handzeichen + Handyaufgaben + Tafel-Gemeinsam", 2: "Test + Zahlenaufgabe + Bewegung im Raum"}

PLAN = {k: [{"std": n, "datum": I.DATEN[k][n], "teile": [n], "methode": M[n], "phasen": ph} for n, ph in ((1, S1), (2, S2))] for k in I.KLASSEN}


def _ab(st, name):
    t = 0
    for n, m, o, a in st["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


_st = PLAN[I.KLASSEN[0]]
KNAPP = {}
for k in I.KLASSEN:
    KNAPP[(k, 1)] = (f"Zeitstopp: Um Minute {_ab(_st[0], 'Aufgabe 2')} beginnt Aufgabe 2. Wird es knapp: Besprechung von Aufgabe 1 auf den China-Impuls kürzen (3 min), Reserve nutzen. "
                     "Aufgabe 1 und 2 bleiben.")
    KNAPP[(k, 2)] = ("Der Test hat Vorrang. Nach dem Test bleiben etwa 22 Minuten: Wird es knapp, zuerst die Statement-Ampel auf eine Aussage kürzen, dann Weißt du noch? streichen. "
                     "Aufgabe 3 nicht streichen; die PDF darf nach dem Läuten hochgeladen werden.")

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
        arbeit = sum(p[1] for p in st["phasen"] if p[3] not in ("org", "reserve", "test"))
        assert arbeit <= 40 - (20 if st["std"] == 2 else 0) + 2, (k, st["std"], "mehr als 40 min Arbeit", arbeit)
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)


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


LESEN = {1: "Beginn der Globalisierung und Antriebskräfte (Buch S. 42–47)",
         2: "Digitalisierung und Digital Divide (Buch S. 48), Statement-Ampel »Ziele erreicht?« (Buch S. 51)"}
WIE = {1: "ohne Handy: Einstieg an der Tafel, Besprechungen, Sicherung im Heft",
       2: "zuerst Test; ohne Handy: Weißt du noch?, Statement-Ampel im Raum"}

KUERZUNG = ["Zuerst: Zusatzaufgaben 4–6 (sind ohnehin nur für Schnelle).",
            "Dann: Impuls »Folgen für die Weltgeschichte?« in Stunde 1 auf 3 Minuten kürzen.",
            "Dann: Statement-Ampel auf eine Aussage; Weißt du noch? streichen.",
            "Fällt Stunde 1 aus: Aufgabe 1 und 2 wandern in Stunde 2 – dann Test und Aufgaben 1–3 nicht in eine Stunde pressen; Aufgabe 3 und Ampel entfallen oder wandern zu Beginn der Einheit »Institutionen« (27.11.)."]
SUPPLIER = "Supplierstunde möglich: Stunde 1 ohne Stephan – Aufgaben 1 und 2 mit Tipp-Stufen und Theorie-Karten, kein Material nötig. Nur die gemeinsame Besprechung (China-Impuls) entfällt oder folgt in Stunde 2."


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        nrs, _ = aufgaben_der(st)
        teile = [f"Lesen {minuten(st, ['lesen'])} min", f"Aufgaben {minuten(st, ['a'])} min", f"Besprechung {minuten(st, ['bespr'])} min", f"Reserve {minuten(st, ['reserve'])} min"]
        if minuten(st, ["test"]): teile.insert(0, f"Test {minuten(st, ['test'])} min")
        rest = MIN - minuten(st, ["lesen", "a", "bespr", "reserve", "test"])
        teile.insert(len(teile) - 1, f"{'Organisation, Wiederholung, Ampel, PDF' if st['std'] == 2 else 'Organisation, Einstieg, Sicherung'} {rest} min")
        z.append({"wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": LESEN[st["std"]],
                  "aufgaben": bereich(nrs) + (" · Selbstcheck-Quiz (6 Fragen)" if st["std"] == 2 else ""),
                  "zeit": " · ".join(teile), "wie": WIE[st["std"]],
                  "abgabe": "Arbeitsblatt-PDF in LMS (Aufgaben 1–3)" if st["std"] == 2 else "Antworten bleiben am Handy gespeichert"})
    return z


FAHRPLAN_TEXT = ("Dafür sind 2 Stunden eingeplant (Fr 13.11. und Fr 20.11.). Lies den jeweiligen Abschnitt im Buch und die Theorie-Karte, "
                 "mach die Aufgaben 1–3 im Arbeitsblatt und gib am 20.11. die PDF in LMS ab. Am 20.11. schreibst du zuerst den angekündigten Test. Zusatzaufgaben 4–6 sind freiwillig. Keine Hausübung.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for st in PLAN[I.KLASSEN[0]]:
        t = 0; print("Stunde", st["std"], st["datum"])
        for p in st["phasen"]: print(f"  {t:2d}–{t + p[1]:2d}  {p[0]}{' (ohne Handy)' if p[2] else ''}"); t += p[1]
