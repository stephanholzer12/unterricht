"""Zeitplan K1.5 Säuren und Basen – EINE Quelle für Fahrplan (einheiten.json), Stundenvorschlag, (spätere) Unterrichts-PPP und Lösungsseite.
Standards 07.11.–13.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Vier Einzelstunden, jede ist abgeschlossen.
KEINE DATEN in dieser Quelle: Termine stehen nur privat im Kalender der Lösungsseite.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "demo" · "erkl" KURZ KLÄREN · "wdh" Weißt du noch? ·
"bespr" BESPRECHEN · "partner" · "bewegung" · "selbst" · "lesen" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE
REFERAT_MIN = 10
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Weißt du noch? Ion, Proton, Elektron (aus K1.3)", 3, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("DEMO K1.5-D1: Rotkraut-Farbenspiel – erst vermuten (Zettel hochhalten), dann zeigen", 9, True, "demo", "DEMO"),
     ("SELBSTSTUDIUM: Buch S. 54 lesen und markieren", 5, True, "lesen", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Säure gibt H⁺ ab, H₃O⁺, Indikatoren", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Säuren erkennen", 10, False, "a2", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Rotkraut-Farben und die Säuren-Tabelle", 5, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 (Zettel hochhalten)", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Laugen, OH⁻, Sicherheit (Auge, erst das Wasser)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Laugen – nützlich und ätzend", 7, False, "a3", "SELBSTSTUDIUM"),
     ("BEWEGUNG: Protonen-Pingpong mit Ball und Schildern (HCl, H₂O, NH₃)", 8, True, "bewegung", "GRUPPENARBEIT"),
     ("Aufgabe 4: Protonen-Pingpong", 10, False, "a4", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Wer gibt ab, wer fängt? Ampholyt Wasser", 6, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit, Schutzbrillen austeilen", 4, True, "org", ""),
     ("Weißt du noch? Zwei Fragen zu Stunde 2", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: pH-Skala, Faktor 10 (pH-Schieber am Beamer)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 5: Die pH-Skala lesen", 6, False, "a5", "SELBSTSTUDIUM"),
     ("VERSUCH K1.5-V1 (Aufgabe 6) mit DEMO K1.5-D2 pH-Meter: messen, ablesen, aufräumen, auswerten", 20, False, "a6", "VERSUCH"),
     ("BESPRECHEN: Klassenwerte am Beamer – Papier gegen pH-Meter", 6, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K1.5-D3: Atemluft macht sauer – Essig und Natron (erst vermuten)", 8, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Neutralisation, Puffer, Blut-pH beim Sport", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 7: Neutralisation – im Glas und in deinem Körper", 9, False, "a7", "SELBSTSTUDIUM"),
     ("PARTNERCHECK: vier Karten über die ganze Einheit", 5, True, "partner", "PARTNERCHECK"),
     ("BESPRECHEN: Sodbrennen, Sprint, Muskelkater", 5, True, "bespr", "BESPRECHEN"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 3, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Demo mit Vorhersage auf Zetteln, Lesen im Buch",
           2: "Bewegung: Protonen-Pingpong mit Ball und Schildern",
           3: "Gruppenversuch mit Rollen – Handy nur zum Eintragen",
           4: "Demo mit Freiwilligem, Partnercheck ohne Handy"}

ZIEL = {1: "Säuren an ihrem Teilchen (H⁺ → H₃O⁺) und mit Indikatoren erkennen.",
        2: "Laugen sicher einschätzen und bei einer Säure-Base-Reaktion sagen, wer abgibt und wer aufnimmt.",
        3: "pH-Werte messen, auf der Skala einordnen und den Faktor 10 pro Stufe anwenden.",
        4: "Die Neutralisation erklären und verstehen, wie Atmung und Puffer den Blut-pH halten."}

MARKE = {1: "DEMO", 2: "GRUPPENARBEIT", 3: "VERSUCH", 4: "PARTNERCHECK"}
PLAN = {k: [{"std": n, "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}

# ---------------------------------------------------------------- Kontrollen
_Z = {t["nr"]: t["zeit"] for t in I.T}
for n, ph in STUNDE.items():
    assert sum(p[1] for p in ph) == MIN, (n, sum(p[1] for p in ph))
    assert sum(p[1] for p in ph if p[3] in ("org", "reserve")) == ORG_RESERVE, (n, "Organisation und Reserve nicht 10 min")
    assert sum(p[1] for p in ph if p[3] == "reserve") >= 5, (n, "zu wenig Reserve")
    assert any(p[2] for p in ph if p[3] not in ("org", "reserve")), (n, "keine Phase ohne Handy")
_m = [METHODE[n] for n in sorted(METHODE)]
assert all(a != b for a, b in zip(_m, _m[1:])) and len(set(_m)) >= 3
_einmal = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art, mk in ph:
        if re.match(r"a\d+$", art):
            _einmal.setdefault(int(art[1:]), []).append((n, mi))
for nr, lst in _einmal.items():
    t = [x for x in I.T if x["nr"] == nr][0]
    assert len(lst) == 1 and lst[0][1] == _Z[nr] and lst[0][0] == t["h"], (nr, lst, _Z[nr], t["h"])
assert sorted(_einmal) == list(range(1, 8)), sorted(_einmal)

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: DEMO K1.5-D1 nur mit drei Gläsern (Essig, Wasser, Natron); das Lesen im Buch wird Teil von Aufgabe 2 (Tipp 3).",
 2: "Wenn es knapp wird: Protonen-Pingpong nur mit HCl und Wasser (4 min); Aufgabe 3 f) wird Zusatz.",
 3: "Zeitstopp für den Versuch: Minute 34 – egal wie weit. Wenn es knapp wird: nur Proben 1, 3, 4 und 5 messen; die pH-Meter-Werte zeigt Prof. HOLZER am Beamer.",
 4: "Wenn es knapp wird: Partnercheck auf zwei Karten kürzen; Teil e) und f) von Aufgabe 7 gemeinsam besprechen. Die PDF-Abgabe darf bis zum Ende des Tages nachgeholt werden.",
}
AUSFALL = ("Fällt eine der vier Stunden aus, wird nichts zusammengepresst: Die drei übrigen Stunden laufen als Stunde 1, 2 und 3 wie geplant "
           "(K06 Protonen-Pingpong und K07 Versuch bleiben). Stunde 4 entfällt: DEMO K1.5-D3 und der Partnercheck fallen weg, "
           "Aufgabe 7 (Neutralisation) wird Zusatz für Schnelle, die Arbeitsblatt-PDF wird am Ende von Stunde 3 abgegeben. "
           "Die Gleichung H₃O⁺ + OH⁻ → 2 H₂O nennst du in Stunde 3 beim Besprechen in einem Satz. Keine Hausübung.")
SUPPLIER = 2   # Aufgabe 3 und 4 brauchen kein Material; das Ballspiel entfällt dann

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN); Organisation, Reserve, Pflichtaufgaben und Versuch bleiben
 1: {1: 0, 3: 6, 4: 1},
 2: {1: 0, 2: 3, 4: 3},
 3: {1: 0, 2: 2, 5: 1},
 4: {1: 0, 2: 6, 5: 2, 6: 3},
}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve") and not re.match(r"a\d+$", STUNDE[_n][i][3]) for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
DOPPEL_HINWEIS = {(1, 2): "Gut: Säuren und Laugen am Stück. Rotkrautsaft und Natron stehen schon.",
                  (2, 3): "Gut: Vom Pingpong direkt zum Messen. Probenstation in der Pause aufbauen.",
                  (3, 4): "Gut: Messwerte und Neutralisation hintereinander. Rotkrautsaft vom Versuchstag weiterverwenden."}


def _chip(art, oh):
    return "ohne Handy" if oh and art not in ("org", "reserve") else ""


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art, mk) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]; note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
        z.append([name, neu, bool(oh), art, note, mk])
    return z


def variante(a, doppel=False, referat=False):
    """Ablauf als Liste [Name, Minuten, ohne Handy, Art, Hinweis, Marke]. Einzelstunde 50 min, Doppelstunde 105 min mit Pause."""
    ref = ["Referat einschließlich kurzer Rückfragen + Brückenfrage", REFERAT_MIN, True, "referat", "", ""]
    if not doppel:
        z = _zeilen(a, REF_KUERZEN[a] if referat else None)
        if referat: z.insert(1, ref)
        assert sum(r[1] for r in z) == MIN, (a, referat)
        return z
    b = a + 1
    za = [r for r in _zeilen(a) if r[3] not in ("pdf", "reserve")]
    zb = [r for r in _zeilen(b)[1:] if r[3] != "wdh"]
    z = za + [["Pause (keine Arbeitszeit)", PAUSE, True, "pause", "", ""]] + zb
    if referat: z.insert(1, ref)
    rest = DOPPEL_MIN - sum(r[1] for r in z)
    assert rest >= 0, (a, referat, rest)
    if rest: z.append(["Puffer oder ein Ausgleichsbaustein" if rest >= 10 else "Puffer", rest, True, "reserve", "", ""])
    assert sum(r[1] for r in z) == DOPPEL_MIN
    return z


VARIANTEN = {}
for _n in sorted(STUNDE):
    for _r in (False, True):
        VARIANTEN["%d%s" % (_n, "R" if _r else "")] = variante(_n, False, _r)
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = variante(_n, True, _r)


def kuerzen_text(n):
    return KUERZEN[n].replace("Wenn es knapp wird: ", "")


def aufgaben_der(n):
    return sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


LESEN = {1: "DEMO Rotkraut-Farbenspiel · Buch S. 54 lesen · Säuren",
         2: "Laugen und Sicherheit · Protonen-Pingpong mit Ball · Buch S. 56–58",
         3: "pH-Skala · VERSUCH pH-Detektive (Gruppen) · Buch S. 59–61",
         4: "DEMO Atemluft und Natron · Neutralisation · Blut-pH · Partnercheck"}
ABGABE = {1: "–", 2: "–", 3: "Messwerte deiner Gruppe eintragen", 4: "Arbeitsblatt-PDF in LMS"}


THEORIE_TEILE = {1: "Teil 1 Säuren", 2: "Teil 2 Laugen, Teil 3 Pingpong", 3: "Teil 4 pH-Wert, Teil 5 Messen", 4: "Teil 6 Neutralisation, Teil 7 Blut"}


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        z.append({"wann": f"Stunde {n}", "marke": MARKE[n], "lesen": LESEN[n], "aufgaben": auf, "theorie": THEORIE_TEILE[n], "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "KI-Fehlerjagd, Forschung Ozeanversauerung, Sicherheits-Briefing (Podcast oder Plakat)",
              "aufgaben": "Zusatz 8–10", "zeit": "ca. 33 min", "abgabe": "freiwillig"})
    return z


FAHRPLAN_TEXT = ("Vier Stunden von sauer bis basisch: Stunde 1 Säuren, Stunde 2 Laugen und Protonen-Pingpong, Stunde 3 pH-Wert und Versuch, "
                 "Stunde 4 Neutralisation und dein Blut. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. Keine Hausübung. "
                 "Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

STUNDENVORSCHLAG = [[f"Stunde {n}", LESEN[n], bereich(aufgaben_der(n)) or "–", f"{ARBEIT} min Arbeit + 10 min Org./Reserve", METHODE[n]] for n in sorted(STUNDE)]

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
    print(len(VARIANTEN), "Varianten")
