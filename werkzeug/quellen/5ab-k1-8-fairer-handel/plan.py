"""Zeitplan K1.8 Fairer Handel (2 Stunden je Klasse, Stunde 1 = Testtag) – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarte (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Annahme laut Übergabe: 50 min je Stunde. Beide Klassen haben denselben Ablauf (5BK Di 03.11., 5AK Do 05.11.).
Minutenplan der ChatGPT-Übergabe v3 übernommen; nach Regelwerk ergänzt um Klassenbuch (1 min), PDF-Abgabe (2 min) und Reserve (4 min, Regelwerk 18: 3–8 min).
Dafür wurden die beiden Erklärphasen und der zweite Lesestopp um 1 min, die Erklärphasen um 1 bzw. 2 min und die Sicherung von 7 auf 5 min gekürzt (im Prüfbericht offen genannt).
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "erkl" kurze Erklärung · "org" · "bespr" · "reserve" · "pdf".
Lesen und Erklären sind EIN Zeitbudget und deshalb getrennt ausgewiesen."""
import inhalt as I

MIN = 50

# Stunde 1 = Testtag: Test 20 min (Annahme), danach kurze Einheit. Realistisch nutzbar höchstens 40 von 50 min – der Rest ist Puffer (Reserve).
STUNDE1 = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
           ("TEST (Stoff: siehe Testankündigung, nicht Fairer Handel)", 20, True, "org"),
           ("Ankommen nach dem Test: Material weg, Handy bereit, Arbeitsblatt-Seite öffnen", 3, True, "org"),
           ("Einstieg gemeinsam: Wie viel vom Ladenpreis kommt beim Kakaobauern an? (Schätzen per Handzeichen)", 4, True, "erkl"),
           ("Lesen: Theorieteil »" + I.ABSCHNITT_1 + "« und Schulbuch S. 35–36", 3, False, "lesen"),
           ("Kurz klären: fairer Handel, drei Säulen, Fair ≠ Bio", 3, True, "erkl"),
           ("Aufgabe 1 zu zweit: Beispiele den drei Säulen zuordnen", 6, False, "a1"),
           ("Besprechung Aufgabe 1 (gemeinsam)", 3, True, "bespr"),
           ("Reserve: Stoppfragen, Quiz, Ausblick auf nächste Woche", 6, True, "reserve")]

STUNDE2 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"),
           ("Rückblick auf Teil 1: Stoppfragen, Schätzung vom Einstieg", 4, True, "erkl"),
           ("Lesen: Theorieteil »" + I.ABSCHNITT_2 + "« und Schulbuch S. 37", 4, False, "lesen"),
           ("Kurz klären: Mindestpreis als Sicherheitsnetz, Prämie zusätzlich (Diagramm an der Tafel)", 4, True, "erkl"),
           ("Aufgabe 2 zu zweit: Prämie und Mehrerlös berechnen", 7, False, "a2"),
           ("Besprechung Aufgabe 2: Rechenweg und Frage d) Weltmarkt höher als Mindestpreis", 4, True, "bespr"),
           ("Kurz klären: Was die Zahlen zeigen – und was nicht (Studie, Quellenkritik)", 4, True, "erkl"),
           ("Aufgabe 3 Gruppendiskussion: Fair einkaufen in der Kaserne?", 10, True, "a3"),
           ("PDF erstellen und in LMS hochladen", 2, False, "pdf"),
           ("Reserve: Quiz, Partnercheck, Hinweis auf Zusatzaufgaben", 8, True, "reserve")]

M_STD = "Handzeichen, Partnerarbeit, Mini-Whiteboard und Gruppendiskussion; Handy nur für Arbeitsblatt und PDF"

PLAN = {k: [{"std": 1, "datum": I.DATEN[k][1], "teile": [1], "methode": M_STD, "phasen": STUNDE1},
            {"std": 2, "datum": I.DATEN[k][2], "teile": [2], "methode": M_STD, "phasen": STUNDE2}] for k in I.KLASSEN}


def _ab(k, std, name):
    t = 0
    for n, m, o, a in [x for x in PLAN[k] if x["std"] == std][0]["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


KNAPP = {(k, 1): "Zeitstopp: Dauert der Test länger als 20 Minuten, entfallen zuerst die Besprechung und die Reserve. Aufgabe 1 kann auch am Anfang der nächsten Stunde fertig besprochen werden. "
                 "Die Aufgabe selbst nie streichen, sie ist die Grundlage für Teil 2."
         for k in I.KLASSEN}
KNAPP.update({(k, 2): f"Zeitstopp: Um Minute {_ab(k, 2, 'Aufgabe 3')} beginnt die Gruppendiskussion, egal wie weit die Paare bei Aufgabe 2 sind. Wenn es knapp wird: "
                      "1. Aufgabe 2 d) nur im Plenum klären. 2. »Was die Zahlen zeigen« als Impuls an der Tafel in 2 Minuten statt 4. 3. Die PDF darf nach dem Läuten hochgeladen werden."
              for k in I.KLASSEN})

for k, stunden in PLAN.items():
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org")), (k, st["std"], "keine Phase ohne Handy")
        # realistisch nutzbar: höchstens 40 min vor der Reserve (Regel vom 06.11.2026)
        assert sum(p[1] for p in st["phasen"] if p[3] != "reserve") <= 44, (k, st["std"], "zu voll")
# jede Pflichtaufgabe kommt in jeder Klasse genau einmal vor; Aufgabenzeit = Zeit in inhalt.py
_Z = {t["nr"]: t["zeit"] for t in I.T}
for k in PLAN:
    nrs = []
    for st in PLAN[k]:
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"):
                nrs.append(int(art[1:])); assert mi == _Z[int(art[1:])], (k, art, mi, _Z[int(art[1:])])
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)


def aufgaben_der(st):
    nrs = sorted(int(p[3][1:]) for p in st["phasen"] if p[3].startswith("a"))
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


def fahrplan_zeilen():
    """Zeilen für einheiten.json (Feld »fahrplan«) – aus PLAN erzeugt, nicht von Hand."""
    z = []
    texte = {1: "Testtag: kurze Einheit nach dem Test · Einstieg + " + I.TEILNAME[1] + " (Buch S. 35–37)", 2: I.TEILNAME[2] + " (Buch S. 36–38)"}
    wie = {1: "ohne Handy: Einstieg per Handzeichen, Besprechung; Aufgabe 1 am Handy zu zweit", 2: "ohne Handy: Rückblick, Besprechung, Gruppendiskussion; Aufgabe 2 am Handy zu zweit"}
    for k in I.KLASSEN:
        for st in PLAN[k]:
            nrs, _ = aufgaben_der(st)
            m_auf = minuten(st, ["a"]); m_les = minuten(st, ["lesen"]); m_bes = minuten(st, ["bespr"]); m_res = minuten(st, ["reserve"])
            z.append({"klasse": k, "wann": "Stunde %d" % st["std"], "datum": st["datum"], "lesen": texte[st["std"]],
                      "aufgaben": bereich(nrs) + (" · Quiz freiwillig" if st["std"] == 2 else ""),
                      "zeit": f"Lesen {m_les} min · Aufgaben {m_auf} min · Besprechung {m_bes} min · Reserve {m_res} min",
                      "wie": wie[st["std"]], "abgabe": "Arbeitsblatt-PDF in LMS (am Ende von Stunde 2)" if st["std"] == 2 else "keine Abgabe in Stunde 1"})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige · Partnercheck-Karten zum Wiederholen",
              "aufgaben": "Zusatz 4–9", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Dafür sind 2 Stunden eingeplant (die erste ist ein Testtag und daher kurz): Lies Teil 1 und 2 im Theorieteil und im Schulbuch S. 35–38, "
                 "mach die Aufgaben 1–3 im Arbeitsblatt und gib die PDF am Ende der zweiten Stunde in LMS ab. Es gibt keine Hausübung.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    t = 0
    for p in STUNDE1 + STUNDE2: print(f"{t:2d}–{t + p[1]:2d}  {p[0]}"); t += p[1] if t + p[1] < 50 else -t
