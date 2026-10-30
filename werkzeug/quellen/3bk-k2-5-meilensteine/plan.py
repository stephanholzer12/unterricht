"""Zeitplan PBGW 3BK · Meilensteine – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarten (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Termine (Stephan): Mo 16.11., Mo 23.11., Mo 30.11.2026. Stundenlänge 50 min = ANNAHME (Stephan: »50 min«).
Am 23.11. zuerst 20 min Test (Stoff kommt von Stephan, noch offen) + 4 min Organisation (Klassenbuch, Austeilen und Einsammeln): danach bleiben 26 min Unterricht.
Minutenplan aus dem ChatGPT-Auftrag (Abschnitt 6) übernommen und nach Regelwerk geändert: Aufgaben mit Zeitangabe, Besprechung als eigene Phase,
Methodenwechsel (Mini-Whiteboard und Kartenlegen · Test und Quellenarbeit am Papier · Aufstellen auf einer Skala), Aufgabe 8 über zwei Stunden geteilt (Karten 1–4 in Stunde 1, 5–9 in Stunde 3).
Stunden 2 und 3 haben keine eigene Reserve: Die Besprechung am Ende ist der Puffer und darf gekürzt werden (siehe KNAPP).
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "erkl" kurze Erklärung · "test" · "org" · "bespr" · "reserve".
Lesen und Erklären sind EIN Zeitbudget und deshalb getrennt ausgewiesen. Lesezeit aus der Wortzahl (ca. 120 Wörter/min, theorie_daten.py), mit Zuschlag für Bilder und Tabellen."""
import inhalt as I

MIN = 50

S1 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Einstieg: Beil zeigen – was sehen wir, was vermuten wir, was wissen wir nicht? (mündlich)", 3, True, "org"),
      ("Lesen: Theorieteil »Vom Sammeln zum Vorrat«, »Neue Möglichkeiten, neue Probleme«, »Metall, Können und Austausch«", 5, False, "lesen"),
      ("Aufgabe 1 am Mini-Whiteboard: Befund, Vermutung, Grenze", 4, True, "a1"),
      ("Kurz klären: Befund und Deutung · Vorrat, Spezialisierung, Abhängigkeit", 3, True, "erkl"),
      ("Aufgabe 2 zu zweit", 8, False, "a2"),
      ("Besprechung Aufgabe 2: »Warum nicht zwangsläufig ein Staat?«", 3, True, "bespr"),
      ("Lesen: Theorieteil »Schrift: Listen und Verwaltung«, »Frühe Staaten: Stadtstaat und Flächenkönigtum«", 4, False, "lesen"),
      ("Aufgabe 3 zu zweit", 8, False, "a3"),
      ("Besprechung Aufgabe 3: Tabelle an der Tafel, Sicherungssatz", 3, True, "bespr"),
      ("Aufgabe 8, Teil 1: Zeitstrahl-Karten 1–4 legen und Schlusssatz", 4, False, "a8"),
      ("Reserve", 3, True, "reserve")]

S2 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("1. Test inkl. Austeilen und Einsammeln (Stoff laut Stephan)", 20, True, "test"),
      ("Test einsammeln, Plätze ordnen", 2, True, "org"),
      ("Einstieg: »Ein Damm bricht – wer trägt die Folgen?« (mündlich)", 2, True, "org"),
      ("Lesen: Theorieteil »Was die Regeln verraten« und »Recht ist nicht gleich Gleichheit«", 4, False, "lesen"),
      ("Kurz klären: Arbeitsfassung, Wenn-dann-Regeln, Quelle ≠ Alltag", 3, True, "erkl"),
      ("Aufgabe 4 zu zweit am Paragrafenblatt (Papier, markieren)", 9, True, "a4"),
      ("Besprechung Aufgabe 4: gleiche Verletzung – ungleiche Folgen; Grenze der Quelle", 6, True, "bespr"),
      ("Sicherung: Stoppfragen und Ausblick auf Stunde 3", 2, True, "org")]

S3 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Weißt du noch? Drei Fragen zu Vorrat, Hammurabi und Quelle", 3, True, "org"),
      ("Lesen: Theorieteil »Athen: direkte Beteiligung mit Grenzen«", 4, False, "lesen"),
      ("Kurz klären: Los und Wahl am Schaubild · wer gehört zum »Volk«?", 2, True, "erkl"),
      ("Aufgabe 5 zu zweit", 8, False, "a5"),
      ("Besprechung Aufgabe 5: Aufstellen auf einer Skala – wie demokratisch war Athen? (0–10)", 2, True, "bespr"),
      ("Lesen: Theorieteil »Rom: Republik und Machtkonzentration«", 4, False, "lesen"),
      ("Aufgabe 6 zu zweit", 7, False, "a6"),
      ("Besprechung Aufgabe 6: Wörter der Republik – Macht beim Princeps", 2, True, "bespr"),
      ("Aufgabe 7 zu zweit (Tabelle ergänzen)", 7, False, "a7"),
      ("Aufgabe 8, Teil 2: Zeitstrahl-Karten 5–9, Begründung und eigene Karte", 5, False, "a8"),
      ("Besprechung Aufgaben 7 und 8, Stoppfragen, Ausblick auf die Frühe Neuzeit", 4, True, "bespr")]

M = {1: "Mini-Whiteboard + Partnerarbeit + Zeitstrahl-Karten legen",
     2: "Test + Quellenarbeit am Paragrafenblatt (Papier, markieren)",
     3: "Aufstellen auf einer Skala (Bewegung) + Vergleichstabelle zu zweit"}

PLAN = {k: [{"std": n, "datum": I.DATEN[k][n], "teile": [n], "methode": M[n], "phasen": ph} for n, ph in ((1, S1), (2, S2), (3, S3))] for k in I.KLASSEN}


def _ab(st, name):
    t = 0
    for n, m, o, a in st["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


_st = PLAN[I.KLASSEN[0]]
KNAPP = {}
for k in I.KLASSEN:
    KNAPP[(k, 1)] = (f"Zeitstopp: Um Minute {_ab(_st[0], 'Aufgabe 3')} beginnt Aufgabe 3. Wird es knapp: Aufgabe 2 b) und c) nur mündlich besprechen; "
                     "die Reserve von 3 Minuten ist der Puffer. Aufgabe 3 bleibt vollständig (K02, K04).")
    KNAPP[(k, 2)] = ("Der Test hat Vorrang. Nach dem Test bleiben 26 Minuten: Wird es knapp, Einstieg mit dem Damm weglassen und Aufgabe 4 f) mündlich besprechen; "
                     "die Besprechung am Ende ist der Puffer. Nichts wird Hausübung.")
    KNAPP[(k, 3)] = (f"Zeitstopp: Um Minute {_ab(_st[2], 'Aufgabe 6')} beginnt Aufgabe 6, um Minute {_ab(_st[2], 'Aufgabe 7')} Aufgabe 7. Wird es knapp: Aufgabe 8 Teil 2 nur Karten 5–9, "
                     "Aufgabe 7 b) mündlich. Aufgabe 6 (Quellenkritik) und die Tabelle in Aufgabe 7 bleiben Pflicht.")

_Z = {t["nr"]: t["zeit"] for t in I.T}
for k, stunden in PLAN.items():
    nrs = {}
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org", "test")), (k, st["std"], "keine Phase ohne Handy")
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"):
                n = int(art[1:]); nrs[n] = nrs.get(n, 0) + mi
                if n != 8: assert [t for t in I.T if t["nr"] == n][0]["h"] == st["std"], (k, n, "Aufgabe in falscher Stunde")
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)
    for n, mi in nrs.items(): assert mi == _Z[n], (k, n, mi, _Z[n])
assert any(p[3] == "reserve" for p in PLAN[I.KLASSEN[0]][0]["phasen"])
assert len(set(M.values())) == 3
assert sum(p[1] for p in S2 if p[3] != "test") == 30 and sum(p[1] for p in S2[3:]) == 26


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


LESEN = {1: "Einstieg + Teil 1 · Vorrat, Metall, Schrift, frühe Staaten (Buch S. 25–39)",
         2: "Teil 2 · Hammurabis Rechtssammlung (Buch S. 39–40)",
         3: "Teil 3 · Athen und Rom (Ergänzungsbuch S. 62–73)"}
WIE = {1: "ohne Handy: Einstieg mündlich, Mini-Whiteboard, Zeitstrahl-Karten legen",
       2: "zuerst Test; ohne Handy: Paragrafenblatt auf Papier lesen und markieren",
       3: "ohne Handy: Aufstellen auf einer Skala, Vergleich zu zweit besprechen"}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand. Alle Klassen gleich → eine Zeile je Stunde."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        nrs, _ = aufgaben_der(st)
        teile = [f"Lesen {minuten(st, ['lesen'])} min", f"Aufgaben {minuten(st, ['a'])} min", f"Besprechung {minuten(st, ['bespr'])} min"]
        if minuten(st, ["reserve"]): teile.append(f"Reserve {minuten(st, ['reserve'])} min")
        if minuten(st, ["test"]): teile.insert(0, f"Test {minuten(st, ['test'])} min")
        z.append({"wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": LESEN[st["std"]],
                  "aufgaben": bereich(nrs) + (" (Teil 1)" if st["std"] == 1 else " (Teil 2)" if st["std"] == 3 else ""),
                  "zeit": " · ".join(teile), "wie": WIE[st["std"]],
                  "abgabe": "Antworten bleiben am Handy gespeichert" + (" · Arbeitsblatt-PDF: Abgabe nach Absprache" if st["std"] == 3 else "")})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Partnercheck, Stolpersteine, Quellenkritik)", "aufgaben": "Zusatz 9–12 · Quiz", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Dafür sind 3 Stunden eingeplant: Mo 16.11., Mo 23.11. und Mo 30.11. Lies den jeweiligen Teil im Theorieteil und mach die Aufgaben 1–8 im Arbeitsblatt. "
                 "Am 23.11. schreibst du zuerst den Test. Keine Hausübung.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for st in PLAN[I.KLASSEN[0]]:
        t = 0; print("Stunde", st["std"], st["datum"])
        for p in st["phasen"]: print(f"  {t:2d}–{t + p[1]:2d}  {p[0]}{' (ohne Handy)' if p[2] else ''}"); t += p[1]
