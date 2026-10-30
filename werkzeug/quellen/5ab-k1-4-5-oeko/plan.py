"""Zeitplan K1.4–1.5 Ökodesign und Ökobilanz – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarte (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Annahme laut Übergabe: 50 min je Stunde. Beide Klassen haben denselben Ablauf (5BK Di 03.11., 5AK Do 05.11.).
Minutenplan der ChatGPT-Übergabe v3 übernommen; nach Regelwerk ergänzt um Klassenbuch (2 min), PDF-Abgabe (2 min) und Reserve (2 min).
Dafür wurden die beiden Erklärphasen um je 1 min und der zweite Lesestopp um 1 min gekürzt und die Sicherung von 7 auf 5 min verkürzt (im Prüfbericht offen genannt).
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "lesen" · "erkl" kurze Erklärung · "org" · "bespr" · "reserve" · "pdf".
Lesen und Erklären sind EIN Zeitbudget und deshalb getrennt ausgewiesen."""
import inhalt as I

MIN = 50

STUNDE = [("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
          ("Einstieg: zwei Flaschen – welche beschaffen, welche Information fehlt? (Handzeichen)", 3, True, "org"),
          ("Lesen: Theorieteil »" + I.ABSCHNITT_1 + "« und »Woran man Ökodesign erkennt«", 4, False, "lesen"),
          ("Kurz klären: Lebenszyklus, Ökodesign ≠ grüner Aufdruck, Smartphone-Beispiel", 3, True, "erkl"),
          ("Aufgabe 1 zu zweit am Mini-Whiteboard, danach Foto", 5, True, "a1"),
          ("Lesen: Theorieteil »" + I.ABSCHNITT_2 + "« und »Vier Schritte einer Ökobilanz«", 4, False, "lesen"),
          ("Kurz klären: vier Schritte, funktionale Einheit, Systemgrenze, CO₂-Äquivalent", 5, True, "erkl"),
          ("Aufgabe 2 zu zweit", 11, False, "a2"),
          ("Besprechung Aufgabe 2: Rechenweg und »Welche Behauptung wäre nicht erlaubt?«", 5, True, "bespr"),
          ("Aufgabe 3 Abschlusscheck allein", 4, False, "a3"),
          ("PDF erstellen und in LMS hochladen", 2, False, "pdf"),
          ("Reserve: Testhinweis 12.11., Quiz und Partnercheck zum Wiederholen", 2, True, "reserve")]

M_STD = "Mini-Whiteboard zu zweit + Handzeichen + Besprechung an der Tafel"

PLAN = {k: [{"std": 1, "datum": I.DATEN[k][1], "teile": [1, 2], "methode": M_STD, "phasen": STUNDE}] for k in I.KLASSEN}


def _ab(k, std, name):
    t = 0
    for n, m, o, a in [x for x in PLAN[k] if x["std"] == std][0]["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


KNAPP = {(k, 1): f"Zeitstopp: Um Minute {_ab(k, 1, 'Besprechung')} beginnt die Besprechung von Aufgabe 2, egal wie weit die Paare sind. Wenn es knapp wird: "
                 "1. Die Besprechung zeigt nur die Musterrechnung (Folie) und die Frage »Welche Behauptung wäre nicht erlaubt?« – die Grenzen der Aussage nie streichen. "
                 "2. Aufgabe 3 bleibt als kurzer Abschluss; die PDF darf am Stundenende auch nach dem Läuten noch hochgeladen werden."
         for k in I.KLASSEN}

for k, stunden in PLAN.items():
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org")), (k, st["std"], "keine Phase ohne Handy")
# jede Pflichtaufgabe kommt in jeder Klasse genau einmal vor; Aufgabenzeit = Zeit in inhalt.py
_Z = {t["nr"]: t["zeit"] for t in I.T}
for k in PLAN:
    nrs = []
    for st in PLAN[k]:
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"):
                nrs.append(int(art[1:])); assert mi == _Z[int(art[1:])], (k, art, mi, _Z[int(art[1:])])
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)
# Übergabe: Lesen 4 + 5 min, Erklären 4 + 6 min, Sicherung 7 min → hier 4 + 4, 3 + 5, 5 (siehe Kopf)
assert sum(p[1] for p in STUNDE if p[3] in ("lesen", "erkl")) == 16


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
    for k in I.KLASSEN:
        st = PLAN[k][0]
        nrs, _ = aufgaben_der(st)
        m_auf = minuten(st, ["a"]); m_les = minuten(st, ["lesen"]); m_bes = minuten(st, ["bespr"]); m_res = minuten(st, ["reserve"])
        z.append({"klasse": k, "wann": "Stunde 1", "datum": st["datum"],
                  "lesen": "Einstieg + " + I.TEILNAME[1] + " (Buch S. 19–21) + " + I.TEILNAME[2] + " (Buch S. 22–25)",
                  "aufgaben": bereich(nrs) + " · Quiz freiwillig",
                  "zeit": f"Lesen {m_les} min · Aufgaben {m_auf} min · Besprechung {m_bes} min · Reserve {m_res} min",
                  "wie": "ohne Handy: Einstieg per Handzeichen, Aufgabe 1 am Mini-Whiteboard, Besprechung",
                  "abgabe": "Arbeitsblatt-PDF in LMS (am Stundenende)"})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige · Partnercheck-Karten zum Wiederholen vor dem Test am " + I.TEST,
              "aufgaben": "Zusatz 4–9", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Dafür ist 1 Stunde eingeplant: Lies Teil 1 und Teil 2 im Theorieteil, mach die Aufgaben 1–3 im Arbeitsblatt und gib die PDF am Stundenende in LMS ab. "
                 "Es gibt keine Hausübung. Zum Wiederholen vor dem Test am " + I.TEST + ": Quiz und Partnercheck.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    t = 0
    for p in STUNDE: print(f"{t:2d}–{t + p[1]:2d}  {p[0]}"); t += p[1]
