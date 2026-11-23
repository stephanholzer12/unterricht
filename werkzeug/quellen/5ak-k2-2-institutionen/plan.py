"""Zeitplan IWK 5AK · K2.2 Institutionen der Globalisierung – EINE Quelle für Fahrplan (einheiten.json), Arbeitsblatt (»So läuft die Stunde«, Balken),
HTML-Präsentation und Lösungsseite.

Standards 07.11.–23.11.2026: 50 min je Stunde = 10 min Organisation/Reserve + 40 min Arbeit. Drei Einzelstunden, jede ist abgeschlossen.
Aufgabe 2 (Gruppenarbeit: Steckbrief und Folien) läuft über Stunde 1 und 2, Aufgabe 3 (Präsentationen, Vergleich, Urteil) in Stunde 3.
KEINE DATEN in dieser Quelle (Standard 13.11.2026): Termine stehen nur privat im Kalender der Lösungsseite.
Phasen: (Name, Minuten, ohne Handy?, Art, Marke). Art: "a<n>" Aufgabe n · "disk" DISKUSSION · "gruppen" Gruppen auslosen · "erkl" KURZ KLÄREN ·
"wdh" Weißt du noch? · "bespr" BESPRECHEN/Sicherung · "lesen" · "org" · "pdf" · "reserve" · "referat" · "pause"."""
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
     ("Weißt du noch? Drei Fragen zur Globalisierung – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("DISKUSSION K2.2-D1: Vier Ecken – »Dein Handy kostet wegen Zöllen 20 % mehr. Wer ist zuständig?« Erst Ecke wählen, dann begründen", 5, True, "disk", "DISKUSSION"),
     ("SELBSTSTUDIUM: Buch S. 52–53 lesen (Tabelle) und Theorie »Drei Institutionen, drei Aufgaben«", 6, False, "lesen", "SELBSTSTUDIUM"),
     ("Aufgabe 1: Wer ist zuständig? Sechs Fälle zuordnen", 7, False, "a1", ""),
     ("KURZ KLÄREN: Aufgabe 1 auflösen · Konsens oder Kapitalanteil – wer hat das Sagen?", 3, True, "erkl", "BESPRECHEN"),
     ("Eure Gruppen: Einteilung am Beamer, jede Gruppe bekommt ihr Thema", 2, True, "gruppen", "GRUPPENARBEIT"),
     ("Aufgabe 2, Teil 1: Steckbrief nach dem Raster recherchieren", 11, False, "a2", "GRUPPENARBEIT"),
     ("BESPRECHEN: Sicherung – Faustregel Handel · Projekte · Zahlungskrise", 2, True, "bespr", "BESPRECHEN"),
     ("Zwischenstand als PDF sichern", 1, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 2: [("Beginn: Klassenbuch, Anwesenheit, Gruppen zusammensetzen", 4, True, "org", ""),
     ("Weißt du noch? Drei Fragen zu Stunde 1 – mit der ABCD-Karte am Handy antworten", 3, True, "wdh", "BESPRECHEN"),
     ("KURZ KLÄREN: So geht ein 4-Minuten-Vortrag – drei Folien, eine Zahl, eine Streitfrage", 4, True, "erkl", "BESPRECHEN"),
     ("Aufgabe 2, Teil 2: Steckbrief fertig, Folien zuerst auf Papier skizzieren, dann bauen", 22, False, "a2", "GRUPPENARBEIT"),
     ("PARTNERCHECK: Kurzprobe – zwei Gruppen proben Folie 2 und 3 je 3 Minuten und geben sich Rückmeldung", 7, True, "a2", "PARTNERCHECK"),
     ("BESPRECHEN: Sicherung – was einen guten Vortrag ausmacht", 2, True, "bespr", "BESPRECHEN"),
     ("Folien in LMS hochladen, Zwischenstand als PDF sichern", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
 3: [("Beginn: Klassenbuch, Anwesenheit, Folien am Lehrer-PC öffnen", 4, True, "org", ""),
     ("KURZ KLÄREN: Ablauf und Reihenfolge der Gruppen · Vergleichstabelle bereit", 1, True, "erkl", "BESPRECHEN"),
     ("PRÄSENTATION: sechs Gruppen je 4 Minuten plus Wechsel (alle Folien in einer Datei) – die anderen füllen die Vergleichstabelle (Aufgabe 3 a)", 28, True, "a3", "PRÄSENTATION"),
     ("DISKUSSION: Statement-Ampel im Raum – »Ohne die USA sind WTO, Weltbank und IWF am Ende.«", 2, True, "disk", "DISKUSSION"),
     ("Aufgabe 3 c): Urteil in drei Sätzen schreiben", 4, False, "a3", ""),
     ("BESPRECHEN: Sicherung – Vergleichstabelle und Urteil", 2, True, "bespr", "BESPRECHEN"),
     ("Ziele erreicht? Selbsteinschätzung im Arbeitsblatt", 1, False, "a4", ""),
     ("PDF-Abgabe: Arbeitsblatt in LMS", 2, False, "pdf", ""),
     ("Reserve", 6, True, "reserve", "")],
}

METHODE = {1: "Vier-Ecken-Spiel im Raum und Gruppenrecherche",
           2: "Folienskizze auf Papier und Probelauf in Gruppenpaaren (Partnercheck)",
           3: "Präsentationen am Beamer und Statement-Ampel im Raum"}

ZIEL = {1: "WTO, Weltbank und IWF auseinanderhalten und den Steckbrief beginnen.",
        2: "Aus dem Steckbrief drei Folien machen und den Vortrag proben.",
        3: "Vortragen, vergleichen und ein begründetes Urteil schreiben."}

MARKE = {1: "GRUPPENARBEIT", 2: "GRUPPENARBEIT", 3: "PRÄSENTATION"}
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
_teile = {}
for n, ph in STUNDE.items():
    for name, mi, oh, art, mk in ph:
        if re.match(r"a\d+$", art):
            _teile.setdefault(int(art[1:]), []).append((n, mi))
for nr, lst in _teile.items():                      # jede Aufgabe: Summe ihrer Phasen = Zeit der Aufgabe
    assert sum(m for _n, m in lst) == _Z[nr], (nr, lst, _Z[nr])
assert sorted(_teile) == I.PFLICHT + [4], (sorted(_teile), I.PFLICHT)   # 4 = »Ziele erreicht?« (Selbsteinschätzung)
assert sorted({n for n, _m in _teile[2]}) == [1, 2], "Aufgabe 2 läuft über Stunde 1 und 2"

# ---------------------------------------------------------------- Kürzen, Ausfall, Supplier
KUERZEN = {
 1: "Wenn es knapp wird: Vier-Ecken auf 3 min kürzen (nur zwei Begründungen), Aufgabe 1 b) gemeinsam statt allein. "
    "Die Gruppen müssen heute ihr Thema haben und mit dem Steckbrief anfangen – das bleibt.",
 2: "Wenn es knapp wird: Der Probelauf läuft nur mit Folie 2 (aktueller Fall). Die Folien dürfen bis Mittwoch vor Stunde 3 in LMS nachgereicht werden. "
    "Nichts wird Hausübung im Sinn von Neuarbeit: nur Hochladen.",
 3: "Wenn es knapp wird: Statement-Ampel streichen, das Urteil schreiben sie trotzdem (Aufgabe 3 c). "
    "Reicht es noch immer nicht: Vortragszeit auf 3 Minuten je Gruppe, Rückfragen am Ende gesammelt.",
}
AUSFALL = ("Fällt Stunde 2 aus, bekommen die Gruppen in Stunde 3 die ersten 10 Minuten für einen Probelauf; die Vorträge werden auf 3 Minuten gekürzt und die Statement-Ampel entfällt. "
           "Fällt Stunde 3 aus, finden die Vorträge in der ersten Stunde nach den Ferien statt (Stand der Folien bleibt in LMS). "
           "Fällt Stunde 1 aus, beginnt Stunde 2 mit Aufgabe 1 und der Gruppeneinteilung; der Steckbrief wird dann mit den Folien in einem Zug gemacht. Keine Hausübung.")
SUPPLIER = 2   # Stunde 2: Gruppen arbeiten an Steckbrief und Folien nach festem Raster, kein Material

# ---------------------------------------------------------------- Ablauf je Termin: Referat und Doppelstunde
REF_KUERZEN = {   # Phasen-Index -> neue Minuten (Summe der Kürzungen = REFERAT_MIN); Organisation und Reserve bleiben immer
 1: {1: 0, 2: 2, 3: 3, 5: 2},                       # »Weißt du noch?« entfällt, Vier-Ecken und Lesen kürzer, Klären kurz
 2: {1: 0, 2: 2, 4: 2},                             # »Weißt du noch?« entfällt, Vortragstipps kürzer, Probelauf nur Folie 2
}
REF_HINWEIS = {1: "Geht: »Weißt du noch?« fällt weg, Vier-Ecken und Lesen werden kürzer. Gruppeneinteilung und Steckbrief bleiben.",
               2: "Geht: »Weißt du noch?« fällt weg, die Vortragstipps sind kürzer und der Probelauf läuft nur mit Folie 2.",
               3: "In Stunde 3 geht kein zusätzliches Referat: Die sechs Gruppenvorträge sind die Referate dieser Einheit."}
REF_AUFGABE_ZUSATZ = {}
for _n, _c in REF_KUERZEN.items():
    assert sum(STUNDE[_n][i][1] - m for i, m in _c.items()) == REFERAT_MIN, (_n, "Kürzungen ergeben nicht die Referatzeit", sum(STUNDE[_n][i][1] - m for i, m in _c.items()))
    assert all(STUNDE[_n][i][3] not in ("org", "reserve") for i in _c), _n
    assert all(0 <= m < STUNDE[_n][i][1] for i, m in _c.items()), _n
assert set(REF_HINWEIS) == set(STUNDE) and set(REF_KUERZEN) <= set(STUNDE)
DOPPEL_HINWEIS = {(1, 2): "Geht gut: Steckbrief und Folien am Stück, die Gruppen verlieren keine Zeit mit Neu-Einlesen.",
                  (2, 3): "Geht: Nach der Pause gleich präsentieren. Probelauf vor der Pause einplanen."}


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
    if referat and a not in REF_KUERZEN:
        return None
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
        _v = variante(_n, False, _r)
        if _v: VARIANTEN["%d%s" % (_n, "R" if _r else "")] = _v
for _n in sorted(STUNDE)[:-1]:
    for _r in (False, True):
        _v = variante(_n, True, _r)
        if _v: VARIANTEN["%d+%d%s" % (_n, _n + 1, "R" if _r else "")] = _v


def kuerzen_text(n):
    return KUERZEN[n].replace("Wenn es knapp wird: ", "")


def aufgaben_der(n, pflicht=True):
    nrs = sorted({int(p[3][1:]) for p in STUNDE[n] if re.match(r"a\d+$", p[3])})
    return [x for x in nrs if not pflicht or x in I.PFLICHT]


def bereich(nrs):
    out, a = [], None
    for i, n in enumerate(nrs):
        if a is None: a = n
        if i + 1 == len(nrs) or nrs[i + 1] != n + 1:
            out.append(str(a) if a == n else ("%d, %d" % (a, n) if n == a + 1 else "%d–%d" % (a, n))); a = None
    return ", ".join(out)


LESEN = {1: "Vier-Ecken · Buch S. 52–53 · Aufgabe 1 · Gruppen und Steckbrief",
         2: "Vortragstipps · Folien bauen · Probelauf mit einer anderen Gruppe",
         3: "Sechs Vorträge · Vergleichstabelle · Statement-Ampel · Urteil"}
ABGABE = {1: "–", 2: "Folien in LMS (eine Person pro Gruppe)", 3: "Arbeitsblatt-PDF in LMS"}
BUCH = {1: "Buch S. 52–53", 2: "Buch S. 52–63 (euer Thema)", 3: "Buch S. 57, 60–63"}
DEMO_NAME = {1: "Vier Ecken: Wer ist zuständig?"}
DEMO_ID = {1: "K2.2-D1"}

# Theorie nach Stunden (Standard 20.11.2026): (Anker, Kurzname)
THEORIE_TEILE_IDS = {
 1: [("ueberblick", "Drei Institutionen, drei Aufgaben"), ("stimme", "Wer hat das Sagen?"), ("aktuell", "Die WTO 2026"),
     ("geld", "Weltbank und IWF 2026"), ("raster", "Euer Steckbrief")],
 2: [("vortrag", "So geht ein 4-Minuten-Vortrag"), ("quellen", "Quellen prüfen")],
 3: [("vergleich", "WTO, Weltbank und IWF im Vergleich"), ("kritik", "Kritik – und was dahintersteckt")],
}
THEORIE_TEILE = {n: ", ".join(name for _id, name in v) for n, v in THEORIE_TEILE_IDS.items()}


def folge(n):
    """Reihenfolge der Stunde für den Fahrplan: Liste [Marke, Text] bzw. [Marke, Text, Sprungziel]."""
    out = []
    for text, _mi, _oh, art, marke in STUNDE[n]:
        if art in ("org", "reserve", "pdf"): continue
        m = re.match(r"a(\d+)$", art)
        if m:
            nr = int(m.group(1))
            tid = next(t["id"] for t in I.T if t["nr"] == nr)
            if nr == 4: name = "Ziele erreicht?"
            elif nr == 2: name = "Aufgabe 2 (Teil %d%s)" % (n, ", Probelauf" if marke == "PARTNERCHECK" else "")
            elif nr == 3: name = "Aufgabe 3 " + ("a) während der Vorträge" if marke == "PRÄSENTATION" else "c) Urteil")
            else: name = "Aufgabe %d" % nr
            out.append(["" if marke in ("",) else marke, name, "aufgaben.html#card_" + tid])
        elif art == "disk": out.append(["DISKUSSION", "Vier Ecken" if n == 1 else "Statement-Ampel"])
        elif art == "gruppen": out.append(["GRUPPENARBEIT", "Eure Gruppen"])
        elif art == "wdh": out.append(["BESPRECHEN", "Weißt du noch?"])
        elif art == "erkl": out.append(["BESPRECHEN", "Prof. HOLZER erklärt"])
        elif art == "lesen": out.append(["SELBSTSTUDIUM", "Buch lesen"])
        elif art == "bespr": out.append(["BESPRECHEN", "Sicherung"])
        else: raise ValueError(art)
    return out


SICHERUNG = {
 1: {"teile": [(1, ["f1", "f2", "f3", "stimme"])], "auch": ["Vier Ecken: Wer ist zuständig?"],
     "merken": ["Faustregel: **WTO = Handel** (Genf) · **Weltbank = Projekte und Entwicklung** · **IWF = Zahlungskrisen** (beide Washington).",
                "In der WTO hat jedes Mitglied **eine Stimme** (Konsens), in IWF und Weltbank zählt der **Kapitalanteil**."]},
 2: {"teile": [], "auch": ["Probelauf: Was hat gut funktioniert?", "Aufgabe 2: Folien in LMS"],
     "merken": ["Ein guter Kurzvortrag hat **eine Kernaussage pro Folie**, **eine Zahl mit Quelle** und **eine Frage** an die Zuhörer.",
                "Die Webseite einer Organisation ist gut für **Fakten**, aber keine **unabhängige Bewertung** – dafür braucht es eine zweite Quelle."]},
 3: {"teile": [(3, ["wto", "wb", "iwf", "urteil"])], "auch": ["Statement-Ampel"],
     "merken": ["Alle drei Institutionen sind umstritten – aber **die Kritik ist je nach Institution eine andere**: Blockade (WTO), Armut und Großprojekte (Weltbank), Sparauflagen (IWF).",
                "Ein Urteil hat **Meinung, Grund und Gegenargument**."]},
}
ANTWORT = {
 (3, "wto"): "Handel · jedes Mitglied eine Stimme, Konsens · blockiert, Streitschlichtung lahm",
 (3, "wb"): "Kredite für Entwicklung und Wiederaufbau · Stimmen nach Kapital · Armut nicht besiegt, Großprojekte",
 (3, "iwf"): "Kredite bei Zahlungskrisen · Stimmen nach Quote · harte Sparauflagen",
 (3, "urteil"): "Meinung + Grund (weil …) + Gegenargument (aber …) – zum Beispiel: Ohne die USA fehlt viel Geld, aber die USA sind in IWF und Weltbank geblieben.",
}


def _letter_map(nr):
    t = next(x for x in I.T if x["nr"] == nr)
    out, akt = {}, None
    for f in t["fields"]:
        m = re.match(r"([a-z]\d?)\)", f[1])
        if m: akt = m.group(1)
        out[f[0]] = akt or f[0]
    return out


def buchstaben(nr, ids):
    m = _letter_map(nr)
    out = []
    for fid in ids:
        b = m.get(fid, fid)
        if b not in out: out.append(b)
    return out


def sicherung_kurz(n):
    S = SICHERUNG[n]
    return " · ".join([f"Aufgabe {nr} " + ", ".join(b + ")" for b in buchstaben(nr, ids)) for nr, ids in S["teile"]] + S["auch"])


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

BALKEN_TEXT = {"disk": "Jetzt DISKUSSION mit Prof. HOLZER: {t} – Handy weg.",
               "gruppen": "Jetzt die Gruppeneinteilung am Beamer: Merk dir deine Gruppennummer und wähle sie bei Aufgabe 2.",
               "lesen": "Jetzt SELBSTSTUDIUM: {t}.",
               "erkl": "Jetzt erklärt Prof. HOLZER: {t} – Handy weg, zuhören.",
               "bespr": "Jetzt SICHERUNG mit Prof. HOLZER: {s}.",
               "wdh": "Jetzt »Weißt du noch?«: Antwort mit der ABCD-Karte zeigen."}


def balken():
    """Balken im Arbeitsblatt zwischen den Aufgaben: {"vor": {Aufgabennr: [[Marke, Text], …]}, "nach": {…}}.
    Phasen vor der ersten Aufgabe einer Stunde stehen schon im Kasten »So läuft die Stunde«.
    Aufgabe 2 läuft über Stunde 1 und 2 und steht im Block »Stunde 1 und 2«: Was in Stunde 1 nach Aufgabe 1 passiert, kommt HINTER Aufgabe 1.
    Kommt eine Aufgabe in derselben Stunde ein zweites Mal dran (Aufgabe 3: Vorträge, dann Urteil), steht der Balken dazwischen HINTER ihrer Karte."""
    vor, nach = {}, {}
    karte_h = {t["nr"]: t["h"] for t in I.T}
    for n, rows in STUNDE.items():
        warte, erste, letzte, gesehen = [], True, None, set()
        for text, _mi, _oh, art, marke in rows:
            if re.match(r"a\d+$", art):
                nr = int(art[1:])
                if warte:
                    if nr in gesehen: nach.setdefault(nr, []).extend(warte)
                    elif karte_h.get(nr) != n and letzte: nach.setdefault(letzte, []).extend(warte)
                    else: vor.setdefault(nr, []).extend(warte)
                warte, erste = [], False
                gesehen.add(nr)
                letzte = nr if karte_h.get(nr) == n else None
                continue
            if art in ("org", "reserve", "pdf") or (erste and art in ("wdh", "disk", "lesen", "erkl")): continue
            t = re.sub(r"^(KURZ KLÄREN|BESPRECHEN|SELBSTSTUDIUM|DISKUSSION|PARTNERCHECK)( K2\.2-D1)?: ", "", text).split(" (")[0]
            warte.append([marke, BALKEN_TEXT[art].format(t=t, s=sicherung_kurz(n))])
        if warte and letzte: nach.setdefault(letzte, []).extend(warte)
    return {"vor": vor, "nach": nach}


EINHEIT = {
 "ziel": "Zölle, Kredite für die Ukraine, Staaten in Geldnot: Hinter vielen Nachrichten stecken drei Organisationen – WTO, Weltbank und IWF. "
         "Wir finden heraus, wer was macht, wer dort das Sagen hat und warum alle drei gerade unter Druck stehen.",
 "am_ende": "Am Ende kannst du die drei auseinanderhalten, einen aktuellen Fall mit Quelle vortragen und Kritik an ihnen begründet beurteilen.",
 "themen": [f"Gruppe {n}: {inst} – {thema}" for n, inst, thema, *_ in I.GRUPPEN],
 "stunden": [(1, "GRUPPENARBEIT", "Wer ist zuständig? Überblick, Gruppen auslosen, Steckbrief beginnen"),
             (2, "PARTNERCHECK", "Drei Folien bauen und mit einer anderen Gruppe proben"),
             (3, "PRÄSENTATION", "Sechs Vorträge, Vergleich, Statement-Ampel und Urteil – Mitarbeits-Check im Jänner")],
}

ZUSATZ_NRS = [t["nr"] for t in I.T if t.get("tag") == "Zusatz"]
ZUSATZ_LINKS = [["Aufgabe %d · %s" % (t["nr"], t["title"].split(":")[0].split(" – ")[0]), "aufgaben.html#card_" + t["id"]]
                for t in I.T if t.get("tag") == "Zusatz"]


def fahrplan_zeilen():
    z = []
    for n in sorted(STUNDE):
        auf = bereich(aufgaben_der(n)) or "–"
        if n in (1, 2): auf = auf.replace("2", "2 (Teil %d)" % n)
        z.append({"wann": f"Stunde {n}", "titel": I.STUNDENTITEL[n], "marke": MARKE[n], "lesen": LESEN[n], "folge": folge(n), "buch": BUCH[n],
                  "aufgaben": auf, "theorie": THEORIE_TEILE[n],
                  "theorie_links": [[name, "theorie.html#" + tid] for tid, name in THEORIE_TEILE_IDS[n]],
                  "zusatz": "Zusatz %s" % bereich(ZUSATZ_NRS), "zusatz_links": ZUSATZ_LINKS,
                  "abgabe": ABGABE[n]})
    z.append({"wann": "Für Schnelle", "lesen": "Karikaturen deuten, KI-Antwort prüfen, Bericht über die WTO-Konferenz 2026 lesen und prüfen",
              "aufgaben": "Zusatz %s" % bereich(ZUSATZ_NRS), "zeit": "ca. 26 min", "abgabe": "freiwillig"})
    z.append({"wann": "Danach", "lesen": "Mitarbeits-Check: 10 Fragen zur ganzen Einheit, ca. 8 min, zählt zur Mitarbeit – Start mit dem Code von Prof. HOLZER"})
    return z


FAHRPLAN_TEXT = ("Drei Stunden, sechs Gruppen, drei Institutionen: In Stunde 1 klären wir, wer wofür zuständig ist, und ihr startet in der Gruppe. "
                 "In Stunde 2 baut ihr drei Folien und probt. In Stunde 3 präsentiert ihr – je 4 Minuten. Alles steht in EINEM Arbeitsblatt, du gibst EIN PDF ab. "
                 "Keine Hausübung. Welche Stunde heute dran ist, sagt dir Prof. HOLZER.")

STUNDENVORSCHLAG = [[f"Stunde {n}", LESEN[n], bereich(aufgaben_der(n)) or "–", f"{ARBEIT} min Arbeit + 10 min Org./Reserve", METHODE[n]] for n in sorted(STUNDE)]

if __name__ == "__main__":
    for n in sorted(STUNDE):
        t = 0
        print(f"--- Stunde {n}: {I.STUNDENTITEL[n]} ({METHODE[n]})")
        for name, mi, oh, art, mk in STUNDE[n]:
            print(f"  {t:2d}–{t + mi:2d}  {name}{'  [ohne Handy]' if oh and art not in ('org', 'reserve') else ''}")
            t += mi
        print("  Sicherung:", sicherung_kurz(n))
    print(len(VARIANTEN), "Varianten")
    print(balken())
