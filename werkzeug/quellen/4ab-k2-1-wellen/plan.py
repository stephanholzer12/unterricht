"""Zeitplan K2.1–2.3 je Klasse – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, Stundenkarten (TH-Fachwissen, PPP) und Lösungsmappe.
Jede Stunde = 50 min (Annahme aus dem Entwurf, von Stephan zu bestätigen). Phasen: (Name, Minuten, ohne Handy?, Art)
Art: "a<n>" = Aufgabe n, "v:<ID>" = Versuch (Aufgabenzeit darin enthalten – nicht doppelt zählen), "lesen", "test", "ref", "org", "bespr", "reserve", "pdf", "z<n>" = Zusatz n."""
import inhalt as I

MIN = 50
PLAN = {
 "4AK": [
  {"std": 1, "datum": "Mi 04.11.", "teile": [1], "methode": "Messung mit Vorhersage (alle Gruppen am selben Pendel)", "phasen": [
     ("Organisation, Gruppen 1–8 einteilen", 2, True, "org"), ("Einstieg: Schaukel – tippen per Handzeichen", 3, True, "org"),
     ("Teil 1 lesen bzw. erklären", 8, False, "lesen"), ("Aufgabe 1", 5, False, "a1"),
     ("Versuch K2.1-V1 Pendel (inkl. Aufgabe 2)", 18, False, "v:K2.1-V1"), ("Aufgabe 3", 4, False, "a3"),
     ("Besprechung (Aufgaben 1–3)", 4, True, "bespr"), ("Reserve", 6, True, "reserve")]},
  {"std": 2, "datum": "Mo 09.11.", "teile": [2], "methode": "Demo mit Vorhersage + Partnercheck", "phasen": [
     ("1. Test inkl. Austeilen und Einsammeln", 20, True, "test"), ("Wechsel zum Thema", 1, True, "org"), ("Weißt du noch?", 2, True, "org"),
     ("Teil 2 lesen bzw. erklären", 6, False, "lesen"), ("Demo K2.1-V2 Resonanz (inkl. Aufgabe 4)", 7, False, "v:K2.1-V2"),
     ("Aufgabe 5 Partnercheck (ohne Handy)", 6, True, "a5"), ("Besprechung", 4, True, "bespr"), ("Reserve", 4, True, "reserve")]},
  {"std": 3, "datum": "Mi 11.11.", "teile": [3], "methode": "Referat + Kadetten-Welle (Bewegung)", "phasen": [
     ("Organisation", 1, True, "org"), ("Referat EKG/MRT inkl. Fragen", 20, True, "ref"), ("Weißt du noch? + Übergang Schwingung → Welle", 3, True, "org"),
     ("Teil 3 lesen bzw. erklären", 6, False, "lesen"), ("Versuch K2.2-V1 Schnur und Kadetten-Welle (inkl. Aufgabe 6)", 8, True, "v:K2.2-V1"),
     ("Aufgabe 7", 6, False, "a7"), ("Besprechung", 3, True, "bespr"), ("Reserve", 3, True, "reserve")]},
  {"std": 4, "datum": "Mo 16.11.", "teile": [4], "methode": "Simulation + Skizzen mit der Hand", "phasen": [
     ("Organisation", 1, True, "org"), ("Weißt du noch?", 3, True, "org"), ("Teil 4 lesen bzw. erklären", 6, False, "lesen"),
     ("Simulation K2.2-V2 (inkl. Aufgabe 8)", 6, False, "v:K2.2-V2"), ("Aufgabe 9 Huygens-Skizze (Handschrift)", 4, True, "a9"),
     ("Zusatz 16 Überlagerung zeichnen (Handschrift)", 8, True, "z16"), ("Zusatz 17 Forschungskarte (zu zweit)", 7, False, "z17"),
     ("Besprechung", 5, True, "bespr"), ("Zwischenstand speichern, Fotos einfügen", 3, False, "org"), ("Reserve", 7, True, "reserve")]},
  {"std": 5, "datum": "Mi 18.11.", "teile": [5], "methode": "Faktencheck + Gestaltung (Handschrift)", "phasen": [
     ("Organisation", 1, True, "org"), ("Weißt du noch?", 3, True, "org"), ("Teil 5 lesen bzw. erklären", 11, False, "lesen"),
     ("Aufgabe 10 Spektrum ordnen (zuerst mündlich)", 4, True, "a10"), ("Aufgabe 11", 5, False, "a11"), ("Aufgabe 12 KI-Check (Handschrift)", 6, True, "a12"),
     ("Aufgabe 13 Sicherheitskarte (Handschrift)", 8, True, "a13"), ("Besprechung", 3, True, "bespr"), ("PDF-Abgabe (Arbeitsblatt + Versuche)", 4, False, "pdf"),
     ("Reserve", 5, True, "reserve")]},
 ],
 "4BK": [
  {"std": 1, "datum": "Mi 04.11.", "teile": [1], "methode": "Messung mit Vorhersage (alle Gruppen am selben Pendel)", "phasen": [
     ("Organisation, Gruppen 1–8 einteilen", 2, True, "org"), ("Einstieg: Schaukel – tippen per Handzeichen", 3, True, "org"),
     ("Teil 1 lesen bzw. erklären", 8, False, "lesen"), ("Aufgabe 1", 5, False, "a1"),
     ("Versuch K2.1-V1 Pendel (inkl. Aufgabe 2)", 18, False, "v:K2.1-V1"), ("Aufgabe 3", 4, False, "a3"),
     ("Besprechung (Aufgaben 1–3)", 4, True, "bespr"), ("Reserve", 6, True, "reserve")]},
  {"std": 2, "datum": "Fr 06.11.", "teile": [2, 3], "methode": "Demo + Partnercheck + Kadetten-Welle", "phasen": [
     ("Weißt du noch?", 2, True, "org"), ("Teil 2 lesen bzw. erklären", 6, False, "lesen"),
     ("Demo K2.1-V2 Resonanz (inkl. Aufgabe 4)", 7, False, "v:K2.1-V2"), ("Aufgabe 5 Partnercheck (ohne Handy)", 6, True, "a5"),
     ("Übergang Schwingung → Welle", 1, True, "org"), ("Teil 3 lesen bzw. erklären", 7, False, "lesen"),
     ("Versuch K2.2-V1 Schnur und Kadetten-Welle (inkl. Aufgabe 6)", 8, True, "v:K2.2-V1"),
     ("Aufgabe 7", 6, False, "a7"), ("Besprechung", 3, True, "bespr"), ("Zwischenstand speichern", 1, False, "org"), ("Reserve", 3, True, "reserve")]},
  {"std": 3, "datum": "Mi 11.11.", "teile": [5], "methode": "Spektrum ordnen (mündlich, zu zweit)", "phasen": [
     ("1. Test inkl. Austeilen und Einsammeln", 20, True, "test"), ("Wechsel zum Thema", 1, True, "org"), ("Weißt du noch?", 2, True, "org"),
     ("Teil 5 lesen bzw. erklären", 11, False, "lesen"), ("Aufgabe 10 Spektrum ordnen (zuerst mündlich)", 4, True, "a10"), ("Aufgabe 11", 5, False, "a11"),
     ("Besprechung", 3, True, "bespr"), ("Reserve", 4, True, "reserve")]},
  {"std": 4, "datum": "Fr 13.11.", "teile": [4], "methode": "Simulation + Skizzen und Karte mit der Hand", "phasen": [
     ("Organisation", 1, True, "org"), ("Weißt du noch?", 3, True, "org"), ("Teil 4 lesen bzw. erklären", 6, False, "lesen"),
     ("Simulation K2.2-V2 (inkl. Aufgabe 8)", 6, False, "v:K2.2-V2"), ("Aufgabe 9 Huygens-Skizze (Handschrift)", 4, True, "a9"),
     ("Aufgabe 12 KI-Check (Handschrift)", 6, True, "a12"), ("Aufgabe 13 Sicherheitskarte (Handschrift)", 8, True, "a13"),
     ("Besprechung", 4, True, "bespr"), ("PDF-Abgabe (Arbeitsblatt + Versuche)", 5, False, "pdf"), ("Reserve", 7, True, "reserve")]},
 ],
}
# Enge Stunden (ChatGPT-Bericht v2, Befund 10): Zeitstopp und Kürzungsreihenfolge – Pflichtziele bleiben, nichts wird Hausübung
KNAPP = {
 ("4AK", 3): "Zeitstopp: Um Minute 44 beginnt die Besprechung, egal wie weit ihr seid. Wenn es knapp wird: 1. Kadetten-Welle längs nur einmal (5 Kadetten statt 10). "
             "2. Interpretation und Schlussfolgerung von K2.2-V1 gemeinsam mündlich sichern – jede Gruppe schreibt nur einen Satz. 3. Aufgabe 7b in der Besprechung gemeinsam rechnen. "
             "Nachholreserve: Stunde 4 hat mit den Zusätzen 16/17 Luft.",
 ("4BK", 2): "Zeitstopp: Um Minute 21 kommt der Übergang zu Teil 3, um Minute 43 die Besprechung. Wenn es knapp wird: 1. Resonanz-Demo nur mit zwei Takten (langsam / im eigenen Takt). "
             "2. Partnercheck mit 2 statt 3 Fragen. 3. Kadetten-Welle längs mit 5 Kadetten. 4. Interpretation und Schlussfolgerung von K2.2-V1 gemeinsam mündlich, jede Gruppe ein Satz. "
             "Der optionale Termin am 18.11. ist keine Voraussetzung.",
}

ZUSATZTERMIN_4BK = {"datum": "Mi 18.11.", "methode": "Vertiefung (nur falls die Stunde stattfindet)", "phasen": [
     ("Wiederholung", 3, True, "org"), ("Zusatz 14", 8, False, "z14"), ("Zusatz 15", 8, False, "z15"), ("Zusatz 16 (Handschrift)", 8, True, "z16"),
     ("Zusatz 17 (zu zweit)", 7, False, "z17"), ("Besprechung", 6, True, "bespr"), ("PDF ergänzen", 4, False, "pdf"), ("Reserve", 6, True, "reserve")]}

for k, stunden in PLAN.items():
    for st in stunden:
        assert sum(p[1] for p in st["phasen"]) == MIN, (k, st["std"], sum(p[1] for p in st["phasen"]))
        assert any(p[2] for p in st["phasen"] if p[3] not in ("reserve",)), (k, st["std"], "keine Phase ohne Handy")
assert sum(p[1] for p in ZUSATZTERMIN_4BK["phasen"]) == MIN
for k in PLAN:  # Methoden zweier aufeinanderfolgender Stunden verschieden
    m = [st["methode"] for st in PLAN[k]]
    assert all(a != b for a, b in zip(m, m[1:])), m
# jede Pflichtaufgabe kommt in jeder Klasse genau einmal vor (direkt oder in ihrem Versuch)
_IN_V = {"K2.1-V1": [2], "K2.1-V2": [4], "K2.2-V1": [6], "K2.2-V2": [8]}
for k in PLAN:
    nrs = []
    for st in PLAN[k]:
        for name, mi, oh, art in st["phasen"]:
            if art.startswith("a"): nrs.append(int(art[1:]))
            if art.startswith("v:"): nrs += _IN_V[art[2:]]
    assert sorted(nrs) == I.PFLICHT, (k, sorted(nrs), I.PFLICHT)


def aufgaben_der(st):
    nrs, zus = [], []
    for name, mi, oh, art in st["phasen"]:
        if art.startswith("a"): nrs.append(int(art[1:]))
        if art.startswith("v:"): nrs += _IN_V[art[2:]]
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
            teile = " + ".join(f"Teil {t}" for t in st["teile"])
            vors = [p[0].split(" (inkl.")[0] for p in st["phasen"] if p[3].startswith("v:")]
            extra = [p[0] for p in st["phasen"] if p[3] in ("test", "ref")]
            lesen = " · ".join(([e.split(" inkl.")[0] for e in extra]) + (["Einstieg"] if st["std"] == 1 else []) + [teile] + vors)
            auf = bereich(nrs) + (" · Zusatz " + bereich(zus) if zus else "")
            if st["std"] == len(stunden): auf += " · Quiz freiwillig"
            m_auf = minuten(st, ["a", "v:"]); m_res = minuten(st, ["reserve"]); m_bes = minuten(st, ["bespr"])
            zeit = f"Aufgaben und Versuche ca. {m_auf} min · Besprechung {m_bes} min · Reserve {m_res} min"
            if zus: zeit = zeit.replace(" · Besprechung", f" · Zusatz {minuten(st, ['z'])} min · Besprechung")
            ohne = [p[0].split(" (")[0].split(" – ")[0] for p in st["phasen"] if p[2] and (p[3] not in ("reserve", "org", "bespr", "test", "ref") or "tippen" in p[0])]
            wie = "ohne Handy: " + ", ".join(dict.fromkeys(ohne)) if ohne else "am Handy"
            abgabe = "Arbeitsblatt-PDF + Versuchs-PDF in LMS" if any(p[3] == "pdf" for p in st["phasen"]) else "–"
            z.append({"klasse": k, "wann": f"Stunde {st['std']}", "datum": st["datum"], "lesen": lesen, "aufgaben": auf, "zeit": zeit, "wie": wie, "abgabe": abgabe})
    z.append({"klasse": "4BK", "wann": "Zusatztermin", "datum": ZUSATZTERMIN_4BK["datum"], "lesen": "nur falls die Stunde stattfindet · Vertiefung",
              "aufgaben": "Zusatz 14–17", "zeit": "ca. 31 min Aufgaben", "wie": "Überlagerung mit der Hand zeichnen", "abgabe": "PDF ergänzen (freiwillig)"})
    z.append({"wann": "Für Schnelle", "lesen": "Für Schnelle und Neugierige (Forschungskarte, Ausblick)", "aufgaben": "14–17", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Die Theorie ist in Teile gegliedert – deine Klasse macht sie in dieser Reihenfolge: 4AK Teil 1 → 2 → 3 → 4 → 5, 4BK Teil 1 → 2 + 3 → 5 → 4. "
                 "Pflichtaufgaben werden in der Stunde fertig, es gibt keine Hausübung. Abgabe: Arbeitsblatt-PDF und Versuchs-PDF in LMS "
                 "(4AK nach Stunde 5 am Mi 18.11., 4BK nach Stunde 4 am Fr 13.11.).")


if __name__ == "__main__":
    import json
    print(json.dumps(fahrplan_zeilen(), ensure_ascii=False, indent=1))
