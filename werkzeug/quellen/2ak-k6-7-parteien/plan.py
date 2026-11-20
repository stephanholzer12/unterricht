"""Zeitplan K6–7 Wahlrecht und Parteien (2AK) – EINE Quelle für Fahrplan (einheiten.json), Arbeitsblatt-Ablauf, Präsentation und Lösungsseite.
Standards 07.–20.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Vier Einzelstunden, jede ist abgeschlossen.
Die Referate stehen FEST im Plan (Stephan 20.11.2026): Stunde 1 Referat SPÖ und FPÖ (12 min), Stunde 3 Referat Befragung (20 min).
KEINE DATEN in dieser Quelle: Termine stehen nur privat im Kalender der Lösungsseite.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "neu" Neue Einheit · "wdh" Weißt du noch? · "referat" ·
"lesen" · "puzzle" · "bewegung" · "ampel" · "erkl" · "bespr" · "org" · "pdf" · "reserve"."""
import re
import inhalt as I

MIN = 50
ORG_RESERVE = 10
ARBEIT = MIN - ORG_RESERVE

STUNDE = {
 1: [("Beginn: Klassenbuch, Anwesenheit, Handys bereit", 4, True, "org", ""),
     ("Neue Einheit: Worum es in vier Stunden geht", 2, True, "neu", "BESPRECHEN"),
     ("Aufgabe 1: Was glaubst du? Drei Vorhersagen tippen", 2, False, "a1", ""),
     ("REFERAT: SPÖ und FPÖ – mit drei Hörfragen", 12, True, "referat", "REFERAT"),
     ("SELBSTSTUDIUM: Buch S. 23–25 lesen (Zeitleiste und Kästen)", 6, True, "lesen", "SELBSTSTUDIUM"),
     ("Aufgabe 2: Vom Kaiser zum Wählen mit 16", 10, False, "a2", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Auflösung »Was glaubst du?« und die Frage 20 oder 21", 7, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 – mit der ABCD-Karte", 3, False, "wdh", "BESPRECHEN"),
     ("GRUPPENPUZZLE: Expertengruppen zu den drei Lagern (Buch S. 27–30), dann Stammgruppen", 14, True, "puzzle", "GRUPPENARBEIT"),
     ("SELBSTSTUDIUM: Buch S. 31 lesen – Wie entsteht eine Partei? Wie finanziert sie sich?", 5, True, "lesen", "SELBSTSTUDIUM"),
     ("Aufgabe 3: Drei Lager – deine Tabelle mit der Hand", 13, False, "a3", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Drei Lager → drei Parteien", 4, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 2 – mit der ABCD-Karte", 3, False, "wdh", "BESPRECHEN"),
     ("ALLE GEMEINSAM: Sitzordnung 1789 und Aufstellen auf der Links-rechts-Linie", 6, True, "bewegung", "BESPRECHEN"),
     ("Aufgabe 4: Links, rechts, liberal (a bis e vor dem Referat)", 8, False, "a4", "SELBSTSTUDIUM"),
     ("REFERAT: Ein Kadett befragt Vertreter mehrerer Parteien – Hörbogen Aufgabe 4 f und g", 20, True, "referat", "REFERAT"),
     ("BESPRECHEN: Wer hat wie geantwortet?", 2, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 4: [("Beginn: Klassenbuch, Anwesenheit", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 3 – mit der ABCD-Karte", 3, False, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: Was hat sich seit Dezember getan? (Stand vorher prüfen)", 5, True, "erkl", "BESPRECHEN"),
     ("STATEMENT-AMPEL im Raum: »Die Grünen sind gegen mehr Geld fürs Bundesheer.«", 8, True, "ampel", "DISKUSSION"),
     ("Aufgabe 5: Faktencheck – KI-Antwort und Schulbuch", 11, False, "a5", "SELBSTSTUDIUM"),
     ("BESPRECHEN: Die drei Fehler der KI", 3, True, "bespr", "BESPRECHEN"),
     ("Aufgabe 6: Mindmap mit der Hand", 7, True, "a6", "SELBSTSTUDIUM"),
     ("Aufgabe 7: Ziele erreicht? – ehrlich ankreuzen", 1, False, "a7", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Referat mit Hörfragen, Vorhersage mit der ABCD-Karte",
           2: "Gruppenpuzzle (Expertengruppen) ohne Handy, Tabelle mit der Hand",
           3: "Bewegung: Aufstellen auf der Links-rechts-Linie, Referat mit Hörbogen",
           4: "Statement-Ampel im Raum, Mindmap mit der Hand"}

ZIEL = {1: "Erklären, wie das Wahlrecht in Etappen für alle erkämpft wurde.",
        2: "Die drei Lager um 1900 beschreiben und den Parteien von heute zuordnen.",
        3: "Parteien mit links, rechts und liberal beschreiben – und die Grenzen dieser Einteilung sehen.",
        4: "Aussagen über Parteien mit Quellen prüfen und die Einheit auf einem Blatt zusammenfassen."}

MARKE = {1: "REFERAT", 2: "GRUPPENARBEIT", 3: "REFERAT", 4: "DISKUSSION"}

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
for n, r in I.REFERATE.items():
    assert sum(p[1] for p in STUNDE[n] if p[3] == "referat") == r["min"], n

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Lesen im Buch wird Teil von Aufgabe 2 (Tipp 3); Besprechen nur Auflösung und 20 oder 21 (4 min). Dauert das Referat länger, i) von Aufgabe 2 gemeinsam besprechen.",
 2: "Wenn es knapp wird: Gruppenpuzzle nur Expertengruppen (8 min) und kurze Runde im Plenum; g) und h) von Aufgabe 3 werden gemeinsam gelöst.",
 3: "Wenn es knapp wird: Aufstellen nur mit zwei Begriffen (3 min). Das Referat hat Vorrang; f) und g) dürfen am Anfang von Stunde 4 fertig werden.",
 4: "Wenn es knapp wird: Statement-Ampel nur einmal aufstellen (4 min), Aufgabe 5 e) und f) gemeinsam. Die PDF-Abgabe darf bis zum Ende des Tages nachgeholt werden.",
}
AUSFALL = ("Fällt eine der vier Stunden aus, wird nichts zusammengepresst: Fällt Stunde 2 aus, wird das Gruppenpuzzle zum Lesen im Buch (Aufgabe 3 allein, 15 min) am Anfang von Stunde 3, "
           "das Aufstellen entfällt. Fällt Stunde 4 aus, wird Aufgabe 5 Zusatz und die Mindmap kommt ans Ende von Stunde 3 (statt Besprechen). Die Referate bleiben an ihren Terminen. Keine Hausübung.")
SUPPLIER = 2   # Gruppenpuzzle mit Buch, keine Technik nötig

LESEN = {1: "REFERAT SPÖ und FPÖ · Buch S. 23–25 · Wahlrecht in Etappen",
         2: "GRUPPENPUZZLE drei Lager · Buch S. 27–31 · Parteien gründen und finanzieren",
         3: "Aufstellen links–rechts · REFERAT Befragung · Buch S. 32–35",
         4: "STATEMENT-AMPEL · Faktencheck · Mindmap"}
ABGABE = {1: "–", 2: "Foto deiner Tabelle", 3: "–", 4: "Arbeitsblatt-PDF in LMS"}

THEORIE_LINKS = {1: [("Teil 1 Wahlrecht", "wahlrecht")], 2: [("Teil 2 Drei Lager", "lager"), ("Teil 3 Was Parteien tun", "partei")],
                 3: [("Teil 4 Links, rechts, liberal", "richtung"), ("Teil 5 Parteien heute", "heute")], 4: [("Teil 6 Faktencheck", "pruefen")]}
THEORIE_TEILE = {n: ", ".join(t for t, _k in v) for n, v in THEORIE_LINKS.items()}
TEIL_STUNDE = {k: n for n, v in THEORIE_LINKS.items() for _t, k in v}
BUCH = {1: "Buch S. 23–26", 2: "Buch S. 27–32", 3: "Buch S. 32–35", 4: "Buch S. 23–35"}


def aufgaben_der(n):
    return sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


def _ziel(nr):
    return "aufgaben.html#card_" + next(t["id"] for t in I.T if t["nr"] == nr)


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan: [Marke, kurzer Text, (Ziel)]; ohne Organisation, Reserve, PDF."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        if re.match(r"a\d+$", art):
            nr = int(art[1:]); out.append(["", "Aufgabe %d" % nr, _ziel(nr)])
        elif art == "neu": out.append(["BESPRECHEN", "Neue Einheit"])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "referat": out.append(["REFERAT", "Referat"])
        elif art == "lesen": out.append(["SELBSTSTUDIUM", "Buch lesen"])
        elif art == "puzzle": out.append(["GRUPPENARBEIT", "Gruppenpuzzle"])
        elif art == "bewegung": out.append(["BESPRECHEN", "Aufstellen links–rechts"])
        elif art == "ampel": out.append(["DISKUSSION", "Statement-Ampel"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "bespr": out.append(["BESPRECHEN", "Sicherung"])
        else: raise ValueError(art)
    return out


# Sicherung am Ende jeder Stunde (teile = (Aufgabe, [Feld-IDs]))
SICHERUNG = {
 1: {"teile": [(2, ["j1907", "j1918", "frau", "quelle"])], "auch": ["Auflösung »Was glaubst du?«", "Referat SPÖ und FPÖ"],
     "merken": ["Das Wahlrecht wurde in Etappen **erkämpft**: Besitz → Steuer → **alle Männer (1907)** → **auch Frauen (1918)** → **ab 16 (2007)**.",
                "**Quellen prüfen**: Auch ein Schulbuch kann sich irren – für 1919 gilt **Wahlalter 20**."]},
 2: {"teile": [(3, ["oevp", "fpoe", "wer", "klub"])], "auch": ["Gruppenpuzzle"],
     "merken": ["Drei Lager um 1900: **christlichsozial → ÖVP**, **sozialdemokratisch → SPÖ**, **deutschnational → FPÖ**.",
                "Eine **Partei** gründet man mit der **Satzung beim Innenministerium**; im Nationalrat bilden **5 Abgeordnete** einen **Klub**."]},
 3: {"teile": [(4, ["herkunft", "egal", "liberal", "anzahl"])], "auch": ["Referat: Befragung"],
     "merken": ["**Links** eher **egalitär**, **rechts** eher **konservativ**, **liberal** = viel **Freiheit** für den Einzelnen.",
                "Echte Parteien passen selten genau in eine Schublade – darum **genau hinhören** und **Quellen vergleichen**."]},
 4: {"teile": [(5, ["wie", "heer", "umfrage"])], "auch": ["Statement-Ampel"],
     "merken": ["Vier Fragen an jede Quelle: **Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere?**",
                "Eine **Umfrage** ist keine **Wahl**, eine **Ja/Nein-Tabelle** ist keine **Abstimmung** – Stand und Quelle prüfen."]},
}
ANTWORT = {}


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

BALKEN_TEXT = {"referat": "Jetzt REFERAT: {r}. Handy weg, zuhören – {h}",
               "lesen": "Jetzt SELBSTSTUDIUM: {t}.",
               "puzzle": "Jetzt GRUPPENPUZZLE: Expertengruppe lesen (Buch S. 27–30), dann in der Stammgruppe erklären. Handy weg.",
               "bewegung": "Jetzt alle gemeinsam: Aufstellen auf der Links-rechts-Linie.",
               "ampel": "Jetzt STATEMENT-AMPEL im Raum: Stell dich zu »stimmt«, »unklar« oder »stimmt nicht«.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t}. Handy weg, zuhören.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "neu": "Jetzt: Prof. HOLZER stellt die neue Einheit vor.",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {nr: [[Marke, Text]]}, "nach": {nr: [...]}}."""
    vor, nach = {}, {}
    for n, rows in STUNDE.items():
        warte, erste, letzte = [], True, None
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte: vor[nr] = warte
                warte, erste, letzte = [], False, nr
                continue
            if art in ("org", "reserve", "pdf") or (erste and art in ("wdh", "neu")): continue
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|ALLE GEMEINSAM|SELBSTSTUDIUM|REFERAT|GRUPPENPUZZLE|STATEMENT-AMPEL im Raum): ", "", text).split(" (")[0]
            r = I.REFERATE.get(n, {})
            warte.append([marke, BALKEN_TEXT[art].format(t=t, s=sicherung_kurz(n), r=r.get("titel", "").replace("Referat: ", ""), h=r.get("hoer", "")).replace("?.", "?")])
        if warte and letzte: nach[letzte] = warte
    return {"vor": vor, "nach": nach}


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n], "theorie_links": [[t, "theorie.html#" + k] for t, k in THEORIE_LINKS[n]], "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Forschung: Wählen 16-Jährige seltener?, Hainfeld 1889 heute, Wahlplakat für eine erfundene Partei, Mehrheits-Rechner",
              "aufgaben": "Zusatz 8–11", "zeit": "ca. 40 min", "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"})
    return z


FAHRPLAN_TEXT = ("Vier Stunden von 1848 bis heute: Stunde 1 Wahlrecht, Stunde 2 die drei Lager, Stunde 3 links, rechts, liberal mit Referat, "
                 "Stunde 4 Faktencheck. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. Keine Hausübung. Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

STUNDENVORSCHLAG = [[f"Stunde {n}", LESEN[n], bereich(aufgaben_der(n)) or "–", f"{ARBEIT} min Arbeit + 10 min Org./Reserve", METHODE[n]] for n in sorted(STUNDE)]

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
