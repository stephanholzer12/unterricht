"""Zeitplan K1.4 Erkenntnisgewinn je Klasse – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarten (TH-Fachwissen),
Regiefolien der TH-Unterricht und Lösungsmappe.
Annahme laut Übergabe: 50 min je Stunde (Doppelstunde = 2 × 50 min, Pause außerhalb). Am 06.11. in beiden Klassen 20 min Test inkl. Austeilen/Einsammeln.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "a<n>" Aufgabe n · "v:<ID>" Versuch · "lesen" · "erkl" kurze Erklärung · "bau" Flieger bauen ·
"test" · "org" · "bespr" · "reserve" · "pdf" · "z<n>" Zusatz n. Lesen und Erklären sind EIN Zeitbudget und deshalb getrennt ausgewiesen."""
import inhalt as I

MIN = 50
VS = "v:" + I.VS_ID

TEIL1 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"), ("Einstieg: Büroklammer-Behauptung – tippen per Handzeichen", 3, True, "org"),
         ("Heute, Lernziele, Gruppen 1–8 einteilen", 2, True, "org"),
         ("Lesen: Buch S. 29 (4.1) + Theorieteil Teil 1 »Vermutung, Vorhersage, Beobachtung«, »Theorie, Gesetz und Modell«, »Welche Fragen kann NAWI beantworten?«", 5, False, "lesen"),
         ("Kurz klären: Hypothese – Vorhersage – Theorie, keine Stufenleiter", 5, True, "erkl"),
         ("Aufgabe 1", 3, False, "a1"), ("Aufgabe 2", 2, False, "a2"), ("Aufgabe 3", 3, False, "a3"), ("Besprechung Aufgaben 1–3", 2, True, "bespr"),
         ("Versuchsplan gemeinsam: Was ändern, messen, gleich lassen?", 3, True, "erkl"), ("Aufgabe 4 in der Gruppe (vor dem Versuch!)", 4, False, "a4"),
         ("Flieger bauen nach Faltanleitung, Gruppennummer drauf", 10, True, "bau"), ("Flieger abgeben, Ausblick", 2, True, "org"), ("Reserve", 3, True, "reserve")]

def teil2(start):
    return [start, ("Lesen: Theorieteil Teil 2 »Die Messregeln« und »So läuft der Test«", 3, False, "lesen"), ("Aufgabe 5", 3, False, "a5"),
            ("Weg in den Eingangsbereich, Bandmaß und Linie zeigen", 4, True, "org"), ("Sicherheit, Rollen, Abwurf vorzeigen; je Gruppe ein Probewurf (ohne Messen)", 5, True, "erkl"),
            ("Versuch " + I.VS_ID + ": drei Vergleichspaare je Gruppe (eine Messbahn)", 24, True, VS),
            ("Gegenprobe: zweiter Werfer bei einer Gruppe", 3, True, VS), ("Zurück, Flieger und Papierblätter abgeben", 2, True, "org")]

TEIL3 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"), ("1. Test inkl. Austeilen und Einsammeln", 20, True, "test"),
         ("Lesen: Buch S. 29 (4.2) + Theorieteil »Wien 1847« und Teil 3 »Forschung ist ein Kreislauf«", 5, False, "lesen"),
         ("Kurz klären: Kreislauf, Modell, Begutachtung", 3, True, "erkl"), ("Aufgabe 6 zu zweit (erst ohne Handy)", 7, True, "a6"),
         ("Aufgabe 7 Partnercheck (ohne Handy)", 5, True, "a7"), ("Besprechung", 3, True, "bespr"), ("Reserve", 4, True, "reserve")]

TEIL4 = [("Beginn: Klassenbuch, Anwesenheit", 3, True, "org"), ("Weißt du noch? Eure Hypothesen wieder hervorholen", 3, True, "org"),
         ("Lesen: Theorieteil Teil 4 »Mittelwert und Spannweite«, »Drei mögliche Ergebnisse«, »Widerlegbar muss es sein«", 4, False, "lesen"),
         ("Kurz klären: Rechenweg, »unklar«, widerlegbar", 3, True, "erkl"),
         ("Auswertung " + I.VS_ID + ": Mittelwert, Spannweite, Erkenntnis, Interpretation, Schlussfolgerung", 10, False, VS),
         ("Klassenübersicht an der Tafel: Mittelwerte A und B je Gruppe", 4, True, "erkl"),
         ("Aufgabe 8", 4, False, "a8"), ("Aufgabe 9 KI-Check", 4, False, "a9"), ("Aufgabe 10 zu zweit (erst ohne Handy)", 4, True, "a10"),
         ("Besprechung", 3, True, "bespr"), ("PDF-Abgabe: Arbeitsblatt + Versuchsprotokoll", 4, False, "pdf"), ("Reserve", 4, True, "reserve")]

M_T1 = "Vorhersage per Handzeichen + Flieger bauen mit der Hand"
M_T2 = "Gruppenversuch in Bewegung (Eingangsbereich)"
M_T3 = "Partnerarbeit ohne Handy (Datenkritik, Partnercheck)"
M_T4 = "Klassenübersicht an der Tafel + Partnerarbeit"

PLAN = {
 "1AK": [
  {"std": 1, "datum": I.DATEN["1AK"][1], "teile": [1], "methode": M_T1, "phasen": TEIL1},
  {"std": 2, "datum": I.DATEN["1AK"][2], "teile": [2], "methode": M_T2,
   "phasen": teil2(("Zweite Stunde der Doppelstunde: Klassenbuch, Flieger austeilen", 2, True, "org")) + [("Reserve", 4, True, "reserve")]},
  {"std": 3, "datum": I.DATEN["1AK"][3], "teile": [3], "methode": M_T3, "phasen": TEIL3},
  {"std": 4, "datum": I.DATEN["1AK"][4], "teile": [4], "methode": M_T4, "phasen": TEIL4},
 ],
 "1BK": [
  {"std": 1, "datum": I.DATEN["1BK"][1], "teile": [1], "methode": M_T1, "phasen": TEIL1},
  {"std": 2, "datum": I.DATEN["1BK"][2], "teile": [3], "methode": M_T3, "phasen": TEIL3},
  {"std": 3, "datum": I.DATEN["1BK"][3], "teile": [2], "methode": M_T2,
   "phasen": teil2(("Beginn: Klassenbuch, Flieger aus der Schachtel austeilen", 3, True, "org")) + [("Reserve", 3, True, "reserve")]},
  {"std": 4, "datum": I.DATEN["1BK"][4], "teile": [4], "methode": M_T4, "phasen": TEIL4},
 ],
}

# Enge Stunden: Zeitstopp und was zuerst wegfällt – Pflichtziele bleiben, nichts wird Hausübung
def _ab(k, std, name):
    t = 0
    for n, m, o, a in [x for x in PLAN[k] if x["std"] == std][0]["phasen"]:
        if n.startswith(name): return t
        t += m
    raise KeyError(name)


KNAPP = {
 ("1AK", 2): f"Zeitstopp: Um Minute {_ab('1AK', 2, 'Zurück')} geht es zurück, egal wie weit ihr seid. Wenn es knapp wird: 1. Die Gegenprobe entfällt – das als Grenze im Protokoll notieren. "
             "2. Nie Vergleichspaare streichen; lieber eine Gruppe weniger messen lassen und das im Protokoll vermerken.",
 ("1BK", 3): f"Zeitstopp: Um Minute {_ab('1BK', 3, 'Zurück')} geht es zurück. Wenn es knapp wird: 1. Die Gegenprobe entfällt – als Grenze notieren. 2. Keine Vergleichspaare streichen.",
 ("1AK", 3): f"Nach Klassenbuch und Test bleiben {50 - _ab('1AK', 3, 'Lesen')} min. Zeitstopp: Um Minute {_ab('1AK', 3, 'Besprechung')} beginnt die Besprechung. Wenn es knapp wird: Aufgabe 7 nur mit 2 Karten je Kadett.",
 ("1BK", 2): f"Nach Klassenbuch und Test bleiben {50 - _ab('1BK', 2, 'Lesen')} min. Zeitstopp: Um Minute {_ab('1BK', 2, 'Besprechung')} beginnt die Besprechung. Wenn es knapp wird: Aufgabe 7 nur mit 2 Karten je Kadett.",
 ("1AK", 4): f"Zeitstopp: Um Minute {_ab('1AK', 4, 'PDF')} PDFs erstellen, danach nur noch Reserve. Wenn es knapp wird: Aufgabe 10 g) mündlich, Klassenübersicht nur mit 4 Gruppen.",
 ("1BK", 4): f"Zeitstopp: Um Minute {_ab('1BK', 4, 'PDF')} PDFs erstellen. Wenn es knapp wird: Aufgabe 10 g) mündlich, Klassenübersicht nur mit 4 Gruppen.",
}

for k, stunden in PLAN.items():
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve", "org")), (k, st["std"], "keine Phase ohne Handy")
        assert sum(p[1] for p in st["phasen"] if p[3] == "reserve") >= 3, (k, st["std"], "zu wenig Reserve")
for k in PLAN:  # Methoden zweier aufeinanderfolgender Stunden verschieden
    m = [st["methode"] for st in PLAN[k]]
    assert all(a != b for a, b in zip(m, m[1:])), m
# jede Pflichtaufgabe kommt in jeder Klasse genau einmal vor; Aufgabenzeit = Zeit in inhalt.py
_IN_V = {I.VS_ID: []}
_Z = {t["nr"]: t["zeit"] for t in I.T}
for k in PLAN:
    nrs = []
    for st in PLAN[k]:
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"):
                nrs.append(int(art[1:])); assert mi == _Z[int(art[1:])], (k, art, mi, _Z[int(art[1:])])
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)
# Teil-Zuordnung in inhalt.py passt zum Plan
for k in PLAN:
    for st in PLAN[k]:
        assert I.TEIL_STUNDE[st["teile"][0]][k] == st["std"] and I.DATEN[k][st["std"]] == st["datum"], (k, st["std"])


def aufgaben_der(st):
    nrs, zus = [], []
    for name, mi, oh, art in st["phasen"]:
        if art.startswith("a"): nrs.append(int(art[1:]))
        if art.startswith("z"): zus.append(int(art[1:]))
    return sorted(nrs), sorted(zus)


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
    for k, stunden in PLAN.items():
        for st in stunden:
            nrs, zus = aufgaben_der(st)
            t = st["teile"][0]
            teil = I.TEILNAME[t]
            extra = ["1. Test (20 min)"] if any(p[3] == "test" for p in st["phasen"]) else []
            if t == 1: lesen = "Einstieg + " + teil + " · Buch S. 29 (4.1) · Flieger bauen"
            elif t == 2: lesen = teil + " · Versuch " + I.VS_ID + " im Eingangsbereich"
            elif t == 3: lesen = " · ".join(extra + [teil + " · Buch S. 29 (4.2)"])
            else: lesen = teil + " · Versuch " + I.VS_ID + " auswerten"
            auf = (bereich(nrs) if nrs else "–") + (" · Zusatz " + bereich(zus) if zus else "")
            if t == 2: auf = bereich(nrs) + " · Versuchsprotokoll"
            if t == 4: auf += " · Versuchsprotokoll · Quiz freiwillig"
            m_auf = minuten(st, ["a", "v:", "bau"]); m_res = minuten(st, ["reserve"]); m_bes = minuten(st, ["bespr"])
            zeit = f"Aufgaben und Versuch ca. {m_auf} min · " + (f"Besprechung {m_bes} min · " if m_bes else "") + f"Reserve {m_res} min"
            ohne = [p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org", "bespr", "test", "erkl")]
            wie = ("ohne Handy: " + ", ".join(dict.fromkeys(ohne))) if ohne else "am Handy"
            abgabe = "Arbeitsblatt-PDF + Versuchs-PDF in LMS" if any(p[3] == "pdf" for p in st["phasen"]) else ("Flieger abgeben" if t == 1 else ("Papierblatt der Gruppe abgeben" if t == 2 else "–"))
            z.append({"klasse": k, "wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": lesen, "aufgaben": auf, "zeit": zeit, "wie": wie, "abgabe": abgabe})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Zielscheiben, Forschungskarte)", "aufgaben": "Zusatz 11–14", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Die Theorie ist in vier Teile gegliedert – deine Klasse macht sie in dieser Reihenfolge: 1AK Teil 1 → 2 → 3 → 4, 1BK Teil 1 → 3 → 2 → 4 "
                 "(Teil 3 kommt am Fr 06.11. nach dem Test). Der Papierflieger-Test (Teil 2) findet im Eingangsbereich statt. Pflichtaufgaben werden in der Stunde fertig, "
                 "es gibt keine Hausübung. Abgabe: Arbeitsblatt-PDF und Versuchs-PDF in LMS – 1AK am Do 12.11., 1BK am Mi 11.11.")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
    for k, v in KNAPP.items(): print(k, v)
