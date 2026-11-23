"""Zeitplan TÖW 5AB K1.9 Globalisierung, KI und Klima – EINE Quelle für Fahrplan (einheiten.json), Arbeitsblatt (Balken, »So läuft die Stunde«),
Präsentation (Phasenleiste, Regie) und private Lösungsseite.
Standards 07.11.–23.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Drei Einzelstunden, jede ist abgeschlossen.
KEINE DATEN in dieser Quelle: Termine stehen nur privat im Kalender der Lösungsseite (Startwerte in termine_k1-9.py, nicht im Repository).
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "video" · "erkl" KURZ KLÄREN · "wdh" Weißt du noch? ·
"bespr" BESPRECHEN/DISKUSSION · "skala" Aufstellen im Raum · "gipfel" Mini-Klimagipfel · "partner" · "selbst" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE
REFERAT_MIN = 10   # Annahme: Referat inkl. Rückfragen 10 min (Stephan hat keine Dauer genannt)
PAUSE = 5
DOPPEL_MIN = 2 * MIN + PAUSE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Aufgabe 1: Was glaubst du? Zwei Schätzfragen", 2, False, "a1", ""),
     ("VIDEO: Kurzvideo zum ökologischen Fußabdruck – mit Beobachtungsauftrag", 4, True, "video", "VIDEO"),
     ("KURZ KLÄREN: Fußabdruck, Rucksack, CO₂-Fußabdruck und Arten, die mitreisen (Animationen)", 7, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2: Mein Abdruck – Rechner, Overshoot, Rucksack, Tigermücke", 14, False, "a2", "SELBSTSTUDIUM"),
     ("Aufgabe 3: Mit der Hand – drei Abdrücke als Tabelle", 5, True, "a3", "SELBSTSTUDIUM"),
     ("BESPRECHEN: anonymer Klassenschnitt am Whiteboard und Sicherung", 7, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Wo wohnt die KI? Strom, Wärme, Kühlwasser – der Fall Kronstorf (Animation)", 5, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 4: Was kostet eine KI-Frage? Rechnen und prüfen", 11, False, "a4", "SELBSTSTUDIUM"),
     ("KURZ KLÄREN: Rollenkarten verteilen", 1, True, "erkl", "BESPRECHEN"),
     ("GRUPPENARBEIT (Aufgabe 5): Gemeinderat Kronstorf mit Rollenkarten", 10, False, "a5", "GRUPPENARBEIT"),
     ("DISKUSSION: Prof. HOLZER fragt die Rollen, Abstimmung per Handzeichen", 3, True, "bespr", "DISKUSSION"),
     ("PARTNERCHECK: vier Karten zu Stunde 1 und 2", 3, True, "partner", "PARTNERCHECK"),
     ("BESPRECHEN: Sicherung", 3, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 5, True, "reserve", ""),
     ("Puffer (Organisation)", 1, True, "org", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2", 2, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Treibhauseffekt (Animation) und Klimakonferenzen bis zur COP31", 7, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 6: Klima und Handel – COP31 und Mercosur", 8, False, "a6", "SELBSTSTUDIUM"),
     ("DISKUSSION: Aufstellen auf der Skala »Mercosur – gut oder schlecht fürs Klima?«", 4, True, "skala", "DISKUSSION"),
     ("GRUPPENARBEIT: Mini-Klimagipfel – Staaten verhandeln einen gemeinsamen Satz", 9, True, "gipfel", "GRUPPENARBEIT"),
     ("Aufgabe 7: Mit der Hand – Mindmap der Einheit", 4, True, "a7", "SELBSTSTUDIUM"),
     ("Auflösung »Was glaubst du?«", 1, False, "selbst", ""),
     ("BESPRECHEN: Sicherung", 3, True, "bespr", "BESPRECHEN"),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Video mit Beobachtungsauftrag, Tabelle mit der Hand, anonymer Klassenschnitt am Whiteboard",
           2: "Rollenspiel »Gemeinderat« in Gruppen, Diskussion mit Abstimmung, Partnercheck",
           3: "Aufstellen auf einer Skala im Raum, Mini-Klimagipfel, Mindmap mit der Hand"}

ZIEL = {1: "Fußabdruck, Rucksack und CO₂-Fußabdruck unterscheiden und ausrechnen, wie viele Erden wir bräuchten.",
        2: "Den Strom von KI-Fragen und Rechenzentren mit Haushalten vergleichen und Firmenangaben prüfen.",
        3: "Erklären, warum Klimagipfel scheitern, und Mercosur begründet beurteilen."}

MARKE = {1: "VIDEO", 2: "GRUPPENARBEIT", 3: "DISKUSSION"}
PLAN = {k: [{"std": n, "methode": METHODE[n], "phasen": STUNDE[n]} for n in sorted(STUNDE)] for k in I.KLASSEN}
NR2ID = {t["nr"]: t["id"] for t in I.T}

# Überblick über die ganze Einheit (Folie »Neue Einheit«, Standard 18.11.2026)
EINHEIT = {"ziel": "Alles, was wir kaufen, essen und nutzen, braucht Fläche, Rohstoffe und Energie – auch die KI auf deinem Handy. Ob wir das in den Griff bekommen, entscheiden am Ende Staaten gemeinsam.",
           "am_ende": "Am Ende kannst du deinen eigenen Abdruck einschätzen, den Strom eines Rechenzentrums mit Haushalten vergleichen und bei Klimagipfeln und Handelsabkommen mit Zahlen mitreden.",
           "themen": "Fußabdruck · Rucksack · KI und Rechenzentren · Treibhauseffekt · COP31 · Mercosur",
           "stunden": [(1, "VIDEO", "Wie groß ist dein Abdruck? Rechner, Overshoot Day, Rucksack eines Handys"),
                       (2, "GRUPPENARBEIT", "Rechenzentren: KI-Strom rechnen, Gemeinderat Kronstorf spielen"),
                       (3, "DISKUSSION", "COP31 und Mercosur: Skala im Raum, Mini-Klimagipfel, PDF-Abgabe")]}

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
 1: "Wenn es knapp wird: Das Video fällt weg (die Animationen reichen). 5AK hat den Rechner schon gemacht – dort bleibt mehr Zeit. Aufgabe 3 (Tabelle) darf am Beginn von Stunde 2 fertig werden.",
 2: "Wenn es knapp wird: Der Partnercheck fällt weg, die Diskussion fragt nur drei Rollen (Google, Bürgerinitiative, Umwelt-NGO). Aufgabe 4 g) wird Zusatz.",
 3: "Wenn es knapp wird: Der Mini-Klimagipfel wird kürzer (nur eine Verhandlungsrunde), die Skala bleibt. Zusatzaufgaben entfallen ersatzlos.",
}
AUSFALL = ("Fällt eine der drei Stunden aus: Stunde 2 und 3 werden NICHT zusammengepresst. Stattdessen: Stunde 3 verliert den Mini-Klimagipfel und das Video aus Stunde 1 entfällt; "
           "Treibhauseffekt und Klimakonferenzen kommen in die Jänner-Stunden zum Klima. Keine Hausübung.")
SUPPLIER = 1
KUERZUNGSLISTE = ["Zusatzaufgaben 8–11 (fallen ersatzlos weg)", "Video in Stunde 1", "Partnercheck in Stunde 2",
                  "Mini-Klimagipfel kürzen (eine Runde)", "Diskussion Kronstorf nur mit drei Rollen"]

# ---------------------------------------------------------------- Ablauf je Termin: Referat (5AK Stunde 2: Luftverschmutzung)
SICHERUNG_TEILE = {1: [(2, ["erden", "was", "rdef", "neo"])], 2: [(4, ["jahr", "wer", "fehlt"]), (5, ["uvp", "waerme"])], 3: [(6, ["cop", "eu", "treib", "rind"])]}

REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN). Aufgaben bleiben ganz.
 1: {2: 0, 3: 5, 6: 3},
 2: {1: 0, 2: 3, 6: 1, 7: 0},
 3: {1: 0, 4: 0, 5: 5},
}
REF_NOTIZ = {(1, 2): "Video entfällt", (2, 1): "»Weißt du noch?« entfällt – das Referat ersetzt den Einstieg", (2, 6): "nur zwei Rollen fragen",
             (2, 7): "Partnercheck entfällt", (3, 4): "Skala entfällt", (3, 5): "nur eine Verhandlungsrunde"}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve", "pdf") and not re.match(r"a\d+$", STUNDE[_n][i][3]) for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
DOPPEL_HINWEIS = {}


def _zeilen(n, cuts=None):
    z = []
    for i, (name, mi, oh, art, mk) in enumerate(STUNDE[n]):
        neu, note = mi, ""
        if cuts and i in cuts:
            neu = cuts[i]; note = "entfällt" if neu == 0 else f"gekürzt, sonst {mi} min"
            if (n, i) in REF_NOTIZ: note += " · " + REF_NOTIZ[(n, i)]
        z.append([name, neu, bool(oh), art, note, mk])
    return z


def variante(a, referat=False):
    ref = ["Referat mit Rückfragen und Brückenfrage", REFERAT_MIN, True, "referat", "", ""]
    z = _zeilen(a, REF_KUERZEN[a] if referat else None)
    if referat: z.insert(1, ref)
    assert sum(r[1] for r in z) == MIN, (a, referat)
    return z


VARIANTEN = {}
for _n in sorted(STUNDE):
    for _r in (False, True):
        VARIANTEN["%d%s" % (_n, "R" if _r else "")] = variante(_n, _r)

REFERATE = [{"klasse": "5AK", "stunde": 2, "thema": "Luftverschmutzung",
             "bruecke": ("Luftschadstoff oder Treibhausgas? Feinstaub und Stickoxide schaden direkt unserer Lunge, CO₂ wärmt das Klima. "
                         "Frage an die Klasse: Was davon entsteht, wenn ein Rechenzentrum mit Strom aus einem Gaskraftwerk läuft?"),
             "antwort": "Beides: CO₂ (Klima) und – je nach Kraftwerk – Stickoxide (Luft). Mit Wasserkraft fast keines von beiden im Betrieb."}]


def aufgaben_der(n):
    return sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


LESEN = {1: "VIDEO Fußabdruck · Fußabdruck, Rucksack, CO₂ · Arten reisen mit · Buch S. 40–42",
         2: "Rechenzentren und KI · GRUPPENARBEIT Gemeinderat Kronstorf · Buch S. 97",
         3: "Treibhauseffekt · Klimakonferenzen bis COP31 · Mercosur · Mini-Klimagipfel · Buch S. 40–41, 71–75"}
THEORIE = {1: [("Teil 1 Fußabdruck", "abdruck"), ("Teil 2 Rucksack", "rucksack"), ("Teil 3 Arten reisen mit", "oekosysteme")],
           2: [("Teil 4 KI", "ki"), ("Teil 5 Kronstorf", "kronstorf")],
           3: [("Teil 6 Treibhauseffekt", "treibhaus"), ("Teil 7 Konferenzen", "konferenzen"), ("Teil 8 Mercosur", "handel")]}
THEORIE_TEILE = {n: ", ".join(t for t, _ in v) for n, v in THEORIE.items()}
ABGABE = {1: "–", 2: "–", 3: "Arbeitsblatt-PDF in LMS"}
BUCH = {1: "Buch S. 39–42", 2: "Buch S. 40, 97", 3: "Buch S. 40–41, 71–75"}
DEMO_NAME = {}
assert set(DEMO_NAME) == set(I.DEMOS)


def _ziel(nr):
    return "aufgaben.html#card_" + NR2ID[nr]


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan: [Marke, Text, Ziel?]; ohne Organisation, Reserve, PDF."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        if re.match(r"a\d+$", art):
            nr = int(art[1:])
            out.append([marke, f"{marke} (Aufgabe {nr})", _ziel(nr)] if marke in ("GRUPPENARBEIT",) else ["", f"Aufgabe {nr}", _ziel(nr)])
        elif art == "video": out.append(["VIDEO", "Video Fußabdruck"])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Rollen verteilen" if "Rollenkarten" in text else "Prof. HOLZER erklärt"])
        elif art == "bespr": out.append([marke, "Diskussion der Rollen" if marke == "DISKUSSION" else ("Klassenschnitt und Sicherung" if n == 1 else "Sicherung")])
        elif art == "skala": out.append(["DISKUSSION", "Skala im Raum"])
        elif art == "gipfel": out.append(["GRUPPENARBEIT", "Mini-Klimagipfel"])
        elif art == "partner": out.append(["PARTNERCHECK", "Partnercheck"])
        elif art == "selbst": out.append(["", "Auflösung Aufgabe 1", _ziel(1)])
        else: raise ValueError(art)
    return out


SICHERUNG = {
 1: {"teile": SICHERUNG_TEILE[1], "auch": ["anonymer Klassenschnitt"],
     "merken": ["**Fußabdruck** = Fläche in gha, **Rucksack** = Material in kg, **CO₂-Fußabdruck** = Treibhausgase.",
                "Österreichs Overshoot Day 2026: **2. April** – 365 : 92 ≈ **4 Erden**."]},
 2: {"teile": SICHERUNG_TEILE[2], "auch": ["DISKUSSION: Abstimmung UVP"],
     "merken": ["In Rechenzentren wird fast der ganze Strom zu **Wärme** – Kühlung mit Luft oder Wasser.",
                "**0,24 Wh** pro Frage ist eine **Firmenangabe ohne Training** – wer sagt was, und was fehlt?"]},
 3: {"teile": SICHERUNG_TEILE[3], "auch": ["Ergebnis Mini-Klimagipfel"],
     "merken": ["Treibhausgase halten **Wärme** zurück. Paris 2015: **deutlich unter 2 °C**, möglichst **1,5 °C**.",
                "Die **COP31** scheiterte am Streit um Kohle, Öl und Gas. **Mercosur**: mehr Handel, aber Risiken für Regenwald und Bauern."]},
}
ANTWORT = {(2, "erden"): "rund 4 – 365 : 92 ≈ 4,0",
           (4, "jahr"): "43,8 kWh – 120 Wh · 365 = 43 800 Wh",
           (6, "rind"): "rund 1,24 % – 99 000 : 8 000 000 · 100"}


def buchstaben(nr, ids):
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        m = re.match(r"([a-z]\d?)\)", f[1]); out.append(m.group(1) if m else fid)
    return out


def sicherung_kurz(n):
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


def sicherung_fragen(nr, ids):
    """[(Frage, Antwort)] – Antwort aus der Prüfregel (chk.sel, nie die erste Option) oder aus ANTWORT."""
    t = next(x for x in I.T if x["nr"] == nr)
    out = []
    for fid in ids:
        f = next(x for x in t["fields"] if x[0] == fid)
        a = ANTWORT.get((nr, fid)) or (t.get("chk", {}).get(fid) or {}).get("sel")
        assert a, (nr, fid)
        out.append((f[1], a))
    return out


for _n in SICHERUNG:
    for _nr, _ids in SICHERUNG[_n]["teile"]:
        assert _nr in aufgaben_der(_n), (_n, _nr)
        sicherung_fragen(_nr, _ids)

BALKEN_TEXT = {"video": "Jetzt VIDEO am Beamer: Achte darauf, was alles zum Fußabdruck zählt. Handy weg.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "diskussion": "Jetzt DISKUSSION: Prof. HOLZER fragt die Rollen, dann stimmen alle per Handzeichen ab.",
               "skala": "Jetzt DISKUSSION im Raum: Stell dich auf die Skala – links »schlecht fürs Klima«, rechts »gut«. Begründe deinen Platz.",
               "gipfel": "Jetzt GRUPPENARBEIT: Mini-Klimagipfel. Eure Gruppe ist ein Staat – einigt euch mit den anderen auf einen Satz.",
               "partner": "Jetzt PARTNERCHECK: vier Karten zu zweit – einer fragt, einer antwortet.",
               "selbst": "Jetzt: bei Aufgabe 1 »Auflösung zeigen« – was hast du in Stunde 1 gedacht?",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
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
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|DISKUSSION|PARTNERCHECK|VIDEO|GRUPPENARBEIT): ", "", text).split(" (")[0]
            key = "diskussion" if (marke == "DISKUSSION" and art == "bespr") else art
            txt = "Jetzt verteilt Prof. HOLZER die Rollenkarten. Lies deine Rolle, dann geht es los." if "Rollenkarten" in text else BALKEN_TEXT[key].format(t=t, s=sicherung_kurz(n))
            warte.append([marke, txt])
        if warte and letzte: nach[letzte] = warte
    return {"vor": vor, "nach": nach}


ZUSATZ_TEXT = "Wer hat den CO₂-Fußabdruck erfunden? · KI-Check · Treibhaus-Simulation · Plakat für den Klimagipfel"
CHECK_ZEILE = "Mitarbeits-Check im Jänner: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"


def zusatz_links(n):
    return [[f"Zusatz {t['nr']} {t['title'].split(':')[0]}", "aufgaben.html#card_" + t["id"]] for t in I.T if t.get("zst") == n]


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        zl = zusatz_links(n)
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n], "theorie_links": [[t, "theorie.html#" + a] for t, a in THEORIE[n]],
                  "abgabe": ABGABE[n], "zusatz": ", ".join(x[0] for x in zl), "zusatz_links": zl})
    zus = [t for t in I.T if t["tag"] == "Zusatz"]
    z.append({"wann": "Für Schnelle", "lesen": ZUSATZ_TEXT, "aufgaben": "Zusatz " + bereich([t["nr"] for t in zus]) + " (am Ende des Arbeitsblatts)",
              "zeit": "ca. %d min" % sum(t["zeit"] for t in zus), "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": CHECK_ZEILE})
    return z


FAHRPLAN_TEXT = ("Drei Stunden, ein roter Faden: vom eigenen Abdruck über die Rechenzentren der KI bis zu den Klimagipfeln und Handelsabkommen. "
                 "Alles steht in EINEM Arbeitsblatt, du gibst am Ende von Stunde 3 EIN PDF ab. Keine Hausübung. Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
    print(len(VARIANTEN), "Varianten")
