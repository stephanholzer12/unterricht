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
     ("Weißt du noch? Drei Fragen zu K1.3 (Ion, Proton, Elektron) – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Zwei Vorhersagen tippen", 2, False, "a1", ""),
     ("DEMO K1.5-D1: Rotkraut-Farbenspiel – erst vermuten (Vermutung mit der ABCD-Karte am Handy zeigen), dann zeigen", 9, True, "demo", "DEMO"),
     ("SELBSTSTUDIUM: Buch S. 54 lesen und markieren", 5, True, "lesen", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Säure gibt H⁺ ab, H₃O⁺, Indikatoren", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Säuren erkennen", 10, False, "a2", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Rotkraut-Farben und die Säuren-Tabelle", 5, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Laugen, OH⁻, Sicherheit (Auge, erst das Wasser)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 3: Laugen – nützlich und ätzend", 7, False, "a3", "SELBSTSTUDIUM"),
     ("ALLE GEMEINSAM: Protonen-Pingpong mit Ball und Schildern (HCl, H₂O, NH₃) – die ganze Klasse spielt mit", 8, True, "bewegung", "BESPRECHEN"),
     ("Aufgabe 4: Protonen-Pingpong", 10, False, "a4", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Wer gibt ab, wer fängt? Ampholyt Wasser", 6, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit, Schutzbrillen austeilen", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2 – mit der ABCD-Karte am Handy antworten", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: pH-Skala, Faktor 10 (pH-Schieber am Beamer)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 5: Die pH-Skala lesen", 6, False, "a5", "SELBSTSTUDIUM"),
     ("VERSUCH K1.5-V1 (Aufgabe 6) mit DEMO K1.5-D2 pH-Meter: messen, ablesen, aufräumen, auswerten", 20, False, "a6", "VERSUCH"),
     ("BESPRECHEN: Klassenwerte am Beamer – Papier gegen pH-Meter", 6, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3 – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("DEMO K1.5-D3: Atemluft macht sauer – Essig und Natron (erst vermuten)", 8, True, "demo", "DEMO"),
     ("KURZ KLÄREN: Neutralisation, Puffer, Blut-pH beim Sport", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 7: Neutralisation – im Glas und in deinem Körper", 9, False, "a7", "SELBSTSTUDIUM"),
     ("PARTNERCHECK: vier Karten über die ganze Einheit", 5, True, "partner", "PARTNERCHECK"),
     ("BESPRECHEN: Sodbrennen, Sprint, Muskelkater", 5, True, "bespr", "BESPRECHEN"),
     ("Auflösung »Was glaubst du?« und Selbsteinschätzung", 2, False, "selbst", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 3, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Demo mit Vorhersage über die ABCD-Karte, Lesen im Buch",
           2: "Bewegung: Protonen-Pingpong mit Ball und Schildern",
           3: "Gruppenversuch mit Rollen – Handy nur zum Eintragen",
           4: "Demo mit Freiwilligem, Partnercheck ohne Handy"}

ZIEL = {1: "Säuren an ihrem Teilchen (H⁺ → H₃O⁺) und mit Indikatoren erkennen.",
        2: "Laugen sicher einschätzen und bei einer Säure-Base-Reaktion sagen, wer abgibt und wer aufnimmt.",
        3: "pH-Werte messen, auf der Skala einordnen und den Faktor 10 pro Stufe anwenden.",
        4: "Die Neutralisation erklären und verstehen, wie Atmung und Puffer den Blut-pH halten."}

MARKE = {1: "DEMO", 2: "BESPRECHEN", 3: "VERSUCH", 4: "PARTNERCHECK"}
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
           "Die Gleichung H₃O⁺ + OH⁻ → 2 H₂O nennst du in Stunde 3 beim Besprechen in einem Satz. "
           "Kann der echte VERSUCH nicht stattfinden (Material, Supplierung), ersetzt der virtuelle Versuch K1.5-VV1 (Zusatz 11, PhET) ihn – dann zählt er als Pflicht. Keine Hausübung.")
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


BUCH = {1: "Buch S. 53–55", 2: "Buch S. 56–59", 3: "Buch S. 59–61", 4: "Buch S. 61–62, 65"}
DEMO_NAME = {1: "Rotkraut-Farbenspiel", 4: "Atemluft macht sauer"}


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan (Stephan 15.11.2026: man soll sehen, wann die DEMO dran ist, z. B. nach Aufgabe 1).
    Liste [Marke, kurzer Text]; Organisation, Reserve und PDF-Sicherung fehlen (stehen nicht im Kadetten-Fahrplan)."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        if re.match(r"a\d+$", art):
            nr = int(art[1:]); out.append(["VERSUCH" if marke == "VERSUCH" else "", ("VERSUCH (Aufgabe %d)" % nr) if marke == "VERSUCH" else "Aufgabe %d" % nr])
        elif art == "demo": out.append(["DEMO", "DEMO " + DEMO_NAME[n]])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "lesen": out.append(["SELBSTSTUDIUM", "Buch lesen"])
        elif art == "bewegung": out.append(["BESPRECHEN", "Protonen-Pingpong"])
        elif art == "bespr": out.append(["BESPRECHEN", "Sicherung"])
        elif art == "partner": out.append(["PARTNERCHECK", "Partnercheck"])
        elif art == "selbst": out.append(["", "Auflösung Aufgabe 1"])
        else: raise ValueError(art)
    return out


# Sicherung (Stephan 15.11.2026): Was wird am Ende der Stunde gemeinsam gesichert? EINE Quelle für Präsentation, Arbeitsblatt
# (»Wird gemeinsam gesichert: …«), Fahrplan-Balken und Lösungsseite. teile = (Aufgabe, [Feld-IDs]); auch = weitere Punkte; merken = Merksätze.
SICHERUNG = {
 1: {"teile": [(2, ["oxo", "cola", "rk_essig", "rk_natron"])], "auch": ["DEMO Rotkraut"],
     "merken": ["Säuren geben in Wasser ein **H⁺** ab – daraus wird **H₃O⁺**. Das macht eine Lösung **sauer**.",
                "Ein **Indikator** zeigt mit seiner Farbe: sauer, neutral oder basisch."]},
 2: {"teile": [(3, ["verd", "auge"]), (4, ["g2s", "g2b", "ampho"])], "auch": ["Protonen-Pingpong"],
     "merken": ["Laugen enthalten **OH⁻**. Lauge im Auge: **sofort lange mit Wasser spülen**.",
                "Die **Säure gibt** ein Proton ab, die **Base nimmt** es auf. Wasser kann beides – ein **Ampholyt**."]},
 3: {"teile": [(5, ["faktor", "meer"]), (6, ["co2", "meter"])], "auch": ["VERSUCH: Klassenwerte gegen pH-Meter"],
     "merken": ["pH **unter 7 sauer**, **7 neutral**, **über 7 basisch** – eine Stufe ist **Faktor 10**.",
                "**Indikatorpapier schätzt**, das **pH-Meter misst** genauer."]},
 4: {"teile": [(7, ["ion", "warm", "sod", "blut", "kater"])], "auch": ["DEMO Atemluft", "PARTNERCHECK"],
     "merken": ["**Säure + Lauge → Salz + Wasser**. Im Kern: **H₃O⁺ + OH⁻ → 2 H₂O**.",
                "**Puffer und Atmung** halten deinen Blut-pH zwischen **7,35 und 7,45**."]},
}
ANTWORT = {(5, "faktor"): "1000-mal – drei Stufen: 10 · 10 · 10"}   # Felder ohne Auswahl


def buchstaben(nr, ids):
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        m = re.match(r"([a-z]\d?)\)", f[1]); out.append(m.group(1) if m else fid)
    return out


def sicherung_kurz(n):
    """»Aufgabe 2 b, d, g, h · DEMO Rotkraut« – für Balken, Präsentation und Lösungsseite."""
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


def sicherung_fragen(nr, ids):
    """[(Frage, Antwort)] für die Sicherungs-Folien – Antwort = richtige Auswahl (erste Option) oder ANTWORT."""
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        a = ANTWORT.get((nr, fid)) or (t.get("chk", {}).get(fid) or {}).get("sel")   # richtige Antwort aus der Prüfregel (nicht die erste Option!)
        assert a, (nr, fid)
        out.append((f[1], a))
    return out


for _n in SICHERUNG:
    for _nr, _ids in SICHERUNG[_n]["teile"]:
        assert _nr in aufgaben_der(_n), (_n, _nr)
        sicherung_fragen(_nr, _ids)

BALKEN_TEXT = {"demo": "Jetzt DEMO am Lehrertisch: {d}. Erst vermuten – ABCD-Karte bereit, dann schauen.",
               "lesen": "Jetzt SELBSTSTUDIUM: Buch S. 54 lesen, den Merksatz markieren, drei Säuren aus dem Alltag suchen.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "bewegung": "Jetzt alle gemeinsam: Protonen-Pingpong mit Ball und Schildern.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "partner": "Jetzt PARTNERCHECK: vier Karten zu zweit – einer fragt, einer antwortet.",
               "selbst": "Jetzt: bei Aufgabe 1 »Auflösung zeigen« und die Selbsteinschätzung auf der Theorie-Seite.",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {Aufgabennr: [[Marke, Text], …]}, "nach": {Aufgabennr: […]}}.
    Phasen vor der ersten Aufgabe einer Stunde stehen schon im Kasten »So läuft die Stunde« – außer DEMO und KURZ KLÄREN (die sollen sichtbar sein)."""
    vor, nach = {}, {}
    for n, rows in STUNDE.items():
        warte, erste, letzte = [], True, None
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte: vor[nr] = warte
                warte, erste, letzte = [], False, nr
                continue
            if art in ("org", "reserve", "pdf") or (erste and art == "wdh"): continue
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|ALLE GEMEINSAM|PARTNERCHECK|SELBSTSTUDIUM): ", "", text).split(" (")[0]
            warte.append([marke, BALKEN_TEXT[art].format(d=DEMO_NAME.get(n, ""), t=t, s=sicherung_kurz(n))])
        if warte and letzte: nach[letzte] = warte
    return {"vor": vor, "nach": nach}


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n], "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "KI-Fehlerjagd, Forschung Ozeanversauerung, Sicherheits-Briefing (Podcast oder Plakat), virtueller Versuch am Handy (PhET), Lesen und prüfen: »Übersäuert« – was ist dran?, Säure-Alarm im Mund",
              "aufgaben": "Zusatz 8–13", "zeit": "ca. 70 min", "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"})
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
