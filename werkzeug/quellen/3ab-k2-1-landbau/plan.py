"""Zeitplan K2.1 Formen der Landwirtschaft – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarten (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Annahme laut Übergabe: 50 min je Stunde. 3AK und 3BK haben denselben Ablauf und dieselben Termine (Mi 04.11., Mo 09.11., Mi 11.11., Mo 16.11.).
Am 09.11. zuerst der bestehende 1. Test (20 min, bestätigt) – Landwirtschaft ist dort kein Teststoff.
Minutenplan der ChatGPT-Übergabe (11.5) übernommen und nach Regelwerk geändert: Klassenbuch (2 min) je Stunde, Besprechung als eigene Phase,
Methodenwechsel (nie dieselbe Methode in zwei Stunden hintereinander), Partnercheck mit Karten in Stunde 1, Aufstellen auf einer Skala in Stunde 4.
Nach der unabhängigen Prüfung (30.10.2026): Stunde 2 entlastet (Aufgabe 4: 9 min), Aufgabe 5 an den Anfang von Stunde 3, Podcast auf ca. 7 min gekürzt.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "hoeren" · "erkl" kurze Erklärung · "test" · "org" · "bespr" · "reserve" · "pdf".
Lesen und Erklären sind EIN Zeitbudget und deshalb getrennt ausgewiesen. Lesezeit aus der Wortzahl (ca. 120 Wörter/min, theorie_daten.py)."""
import inhalt as I

MIN = 50

S1 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Einstieg: zwei Äpfel und »Bio ist chemiefrei?« – Handzeichen, je ein Grund", 4, True, "org"),
      ("Lesen: Theorieteil »Der Acker – ein Ökosystem, das wir steuern«, »Drei Formen im Vergleich«, »Was Bio genau heißt«", 6, False, "lesen"),
      ("Kurz klären: Ernte nimmt Nährstoffe mit · vier Merkmale · integriert ist ein Vorgehen", 4, True, "erkl"),
      ("Aufgabe 1 arbeitsteilig zu zweit (jedes Paar eine Form)", 10, False, "a1"),
      ("Besprechung Aufgabe 1: Tabelle an der Tafel gemeinsam füllen, dann Foto", 4, True, "bespr"),
      ("Lesen: »Ein Versuch, der seit 1978 läuft«", 3, False, "lesen"),
      ("Aufgabe 2 zu zweit", 7, False, "a2"),
      ("Besprechung Aufgabe 2: »Warum ist der Betrieb noch nicht bio?«", 3, True, "bespr"),
      ("Partnercheck mit den Karten 1–4", 3, True, "pc"),
      ("Reserve", 4, True, "reserve")]

S2 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("1. Test inkl. Austeilen und Einsammeln (Biomoleküle und Ernährung)", 20, True, "test"),
      ("Lesen: Theorieteil »Schädlinge, Nützlinge, drei Methoden«", 3, False, "lesen"),
      ("Aufgabe 3 allein", 6, False, "a3"),
      ("Lesen: »Was die Verpackung verrät – und was nicht«", 2, False, "lesen"),
      ("Aufgabe 4 in Gruppen an echten Verpackungen", 9, True, "a4"),
      ("Besprechung Aufgaben 3 und 4: Schadschwelle und KI-Satz", 3, True, "bespr"),
      ("Reserve", 5, True, "reserve")]

S3 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Lesen: Theorieteil »Pro Hektar oder pro Kilogramm?«", 2, False, "lesen"),
      ("Aufgabe 5 allein", 5, False, "a5"),
      ("Lesen: »Gene, Züchtung, Gentechnik« und »Die Genschere in vier Schritten«", 5, False, "lesen"),
      ("Kurz klären: vier Schritte am Bild · präzise ist nicht automatisch risikofrei", 3, True, "erkl"),
      ("Hören: Podcast Moder ab 05:39 (ca. 7 min) – zwei Aussagen und eine Rückfrage notieren", 7, True, "hoeren"),
      ("Aufgabe 6: zuerst am Mini-Whiteboard zeichnen, dann Foto und Sätze tippen", 8, False, "a6"),
      ("Lesen: »Eine neue Sorte beurteilen«", 2, False, "lesen"),
      ("Aufgabe 7 zu zweit", 7, False, "a7"),
      ("Besprechung Aufgaben 5–7: Rechenweg, vier Schritte, Prüffragen", 4, True, "bespr"),
      ("Reserve", 5, True, "reserve")]

S4 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
      ("Weißt du noch? zwei Fragen zur Genschere", 2, True, "org"),
      ("Einstieg: »Genmais erzeugt Krebs!« – auf einer Skala aufstellen: Wie glaubwürdig?", 3, True, "org"),
      ("Lesen: Theorieteil »Der Versuch von 2012« und »Woran man eine gute Studie erkennt«", 5, False, "lesen"),
      ("Aufgabe 8 zu zweit", 10, False, "a8"),
      ("Lesen: »Was die große Folgestudie zeigte«", 2, False, "lesen"),
      ("Kurz klären: schwache Methode ≠ Betrug · Folgestudie ≠ Freibrief", 2, True, "erkl"),
      ("Aufgabe 9 mit der Hand auf Papier, dann Foto", 10, True, "a9"),
      ("Partner liest gegen (fünf Kriterien) · nochmal aufstellen: Hat sich eure Einschätzung geändert?", 4, True, "bespr"),
      ("PDF erstellen und in LMS hochladen", 3, False, "pdf"),
      ("Reserve", 7, True, "reserve")]

M = {1: "Handzeichen + arbeitsteilige Partnerarbeit + Partnercheck mit Karten",
     2: "Test + Produktprüfung in Gruppen an echten Verpackungen",
     3: "Mini-Whiteboard zu zweit + Hörauftrag",
     4: "Aufstellen auf einer Skala (Bewegung) + Handschrift auf Papier"}

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
    KNAPP[(k, 1)] = (f"Zeitstopp: Um Minute {_ab(_st[0], 'Aufgabe 2')} beginnt Aufgabe 2. Wird es knapp: Der Versuch seit 1978 wird nur kurz erzählt statt gelesen; "
                     "Aufgabe 2 d) darf auch mündlich besprochen werden. Aufgabe 1 bleibt vollständig (K03).")
    KNAPP[(k, 2)] = ("Der Test hat Vorrang. Nach dem Test bleiben 28 Minuten: Wird es knapp, Aufgabe 3 d) mündlich besprechen; "
                     "fehlen Verpackungen, die Beispieldaten auf der Folie nehmen. Nichts wird Hausübung.")
    KNAPP[(k, 3)] = (f"Zeitstopp: Um Minute {_ab(_st[2], 'Aufgabe 6')} beginnt Aufgabe 6. Wird es knapp: Podcast nach 5 Minuten stoppen "
                     "und den Rest in zwei Sätzen erzählen; Aufgabe 5 c) mündlich. Die vier Schritte der Genschere bleiben Pflicht.")
    KNAPP[(k, 4)] = (f"Zeitstopp: Um Minute {_ab(_st[3], 'Aufgabe 9')} beginnt Aufgabe 9. Wird es knapp: Zweites Aufstellen weglassen; "
                     "die PDF darf auch nach dem Läuten noch hochgeladen werden.")

_Z = {t["nr"]: t["zeit"] for t in I.T}
for k, stunden in PLAN.items():
    nrs = []
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org", "test")), (k, st["std"], "keine Phase ohne Handy")
        assert any(p[3] == "reserve" for p in st["phasen"]), (k, st["std"], "keine Reserve")
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"):
                n = int(art[1:]); nrs.append(n); assert mi == _Z[n], (k, art, mi, _Z[n])
                assert [t for t in I.T if t["nr"] == n][0]["h"] == st["std"], (k, n, "Aufgabe in falscher Stunde")
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)
# Methodenwechsel: nie dieselbe Methode in zwei Stunden hintereinander, mindestens drei verschiedene
assert len(set(M.values())) == 4


def aufgaben_der(st):
    return sorted(int(p[3][1:]) for p in st["phasen"] if p[3].startswith("a")), []


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


def minuten(st, arten):
    return sum(p[1] for p in st["phasen"] if any(p[3].startswith(a) for a in arten))


LESEN = {1: "Einstieg + Teil 1 · Acker, drei Formen, Bio (Buch S. 38–43)",
         2: "Teil 2 · Pflanzenschutz, Verpackung (Buch S. 43–47)",
         3: "Teil 3 · pro Hektar, Gene, Genschere, neue Sorte (Buch S. 45–46) · Podcast-Ausschnitt",
         4: "Teil 4 · Séralini-Versuch, gute Studie, Folgestudie (Ergänzung zu Buch S. 45)"}
WIE = {1: "ohne Handy: Einstieg per Handzeichen, Tabelle an der Tafel, Partnercheck mit Karten",
       2: "zuerst Test; ohne Handy: Verpackungen in Gruppen lesen",
       3: "ohne Handy: Podcast hören, Genschere zuerst am Mini-Whiteboard zeichnen",
       4: "ohne Handy: Aufstellen auf einer Skala, Urteil mit der Hand schreiben"}


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand. Beide Klassen gleich → eine Zeile je Stunde."""
    z = []
    for st in PLAN[I.KLASSEN[0]]:
        nrs, _ = aufgaben_der(st)
        teile = [f"Lesen {minuten(st, ['lesen'])} min", f"Aufgaben {minuten(st, ['a'])} min", f"Besprechung {minuten(st, ['bespr'])} min", f"Reserve {minuten(st, ['reserve'])} min"]
        if minuten(st, ["test"]): teile.insert(0, f"Test {minuten(st, ['test'])} min")
        if minuten(st, ["hoeren"]): teile.insert(1, f"Hören {minuten(st, ['hoeren'])} min")
        z.append({"wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": LESEN[st["std"]],
                  "aufgaben": bereich(nrs) + (" · Quiz freiwillig" if st["std"] == 4 else ""),
                  "zeit": " · ".join(teile), "wie": WIE[st["std"]],
                  "abgabe": "Arbeitsblatt-PDF in LMS (alle Aufgaben 1–9)" if st["std"] == 4 else "Antworten bleiben am Handy gespeichert"})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Versorgung, Geschichte, Partnercheck)", "aufgaben": "Zusatz 10–13 · Quiz", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Dafür sind 4 Stunden eingeplant (3AK und 3BK gleich: Mi 04.11., Mo 09.11., Mi 11.11., Mo 16.11.). Lies den jeweiligen Teil im Theorieteil, "
                 "mach die Aufgaben 1–9 im Arbeitsblatt und gib am 16.11. die PDF in LMS ab. Am 09.11. schreibst du zuerst den Test. Keine Hausübung.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for st in PLAN[I.KLASSEN[0]]:
        t = 0; print("Stunde", st["std"], st["datum"])
        for p in st["phasen"]: print(f"  {t:2d}–{t + p[1]:2d}  {p[0]}{' (ohne Handy)' if p[2] else ''}"); t += p[1]
