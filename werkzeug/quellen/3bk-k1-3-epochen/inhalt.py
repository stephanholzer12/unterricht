"""PBGW 3BK · K1.3–K1.4 Zeit-Einteilung und Epochengliederung (Buch S. 13–14) – 2 Stunden (v1).
Jahresplan: Einheit 2 »Epochen und ihre Merkmale« (2 Std., K03, N01, P4).
Stunde 1: Wie zählen wir Zeit? (Kalender, Zeitrechnungen) · Stunde 2: Die Epochen (Merkmale, Grenzen, Eurozentrismus).
Eine Quelle für Handy-Seiten (Lernseite, Arbeitsblatt, Quiz), Word, PPP und Kahoot.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "18.10.2026"
V = "v1"
ORDNER = "3bk-pbgw/k1-3-epochen"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "3bk-pbgw/"
EYEBROW = "PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen"
TITEL = "Epochen – die Landkarte der Geschichte"
BUCH = "Buch S. 13–14"
KEY = "26-27-3BK-K1.3-Epochen-TH-Handy-v1"
PRAEFIX = "26-27-3BK-K1.3-Epochen"

VIDEOS = {
    "schalt": ("Was ist ein Schaltjahr?", "studyflix", "4 min", "https://studyflix.de/allgemeinwissen/schaltjahr-7284"),
    "zeitstrahl": ("Zeitstrahl Geschichte", "studyflix", "6 min", "https://studyflix.de/geschichte/zeitstrahl-geschichte-7922"),
}

EP = ["Ur- und Frühgeschichte", "Altertum (Antike)", "Mittelalter", "Neuzeit", "Zeitgeschichte"]   # feste Reihenfolge
JN = ["Schaltjahr", "kein Schaltjahr"]


def first(lst, correct):
    """Liste mit der richtigen Antwort an erster Stelle (Anzeige wird gemischt)."""
    return [correct] + [x for x in lst if x != correct]


BEZUG = ["Erschaffung der Welt (3761 v. Chr.)", "Hidschra – Auswanderung Mohammeds nach Medina (622)", "Thronbesteigung Kaiser Diokletians (284)",
         "Gründung der Stadt Rom (753 v. Chr.)", "erste Olympische Spiele (776 v. Chr.)", "Thronbesteigung des jeweiligen Kaisers (heute: 2019)"]

T = [
 # ======================================================= Stunde 1 · Zeit-Einteilung
 {"id": "a1", "nr": 1, "title": "Welches Jahr haben wir heute?", "src": "Buch-Aufgabe S. 13", "own": False, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Stellen Sie fest, welches Jahr heuer im jüdischen und im islamischen (muslimischen) Kalender steht. "
       "Zusatz: Rechne zuerst mit den Faustformeln von der Lernseite und kontrolliere dann im Internet. Erkläre in 1–2 Sätzen, warum die Faustformeln nur ungefähr stimmen.",
  "hint": "Info: Lernseite Teil 1 »Andere Kalender« · Kontrolle: Recherche im Internet, Suchtipp »jüdischer Kalender heute« bzw. »islamischer Kalender heute«",
  "type": "multi",
  "fields": [["jued", "Jüdisches Jahr (Oktober 2026)"], ["islam", "Islamisches Jahr (Oktober 2026)"],
             ["warum", "Warum stimmen die Faustformeln nur ungefähr? (1–2 Sätze)"]],
  "chk": {"jued": {"kw": [["richtiges Jahr", r"\b5787\b"]]}, "islam": {"kw": [["richtiges Jahr", r"\b1448\b"]]},
          "warum": {"kw": [["anderer Jahresbeginn oder kürzeres Jahr", "herbst|september|juni|neujahr|beginn|wechsel|mond|kürzer|354|11 tag|anders"]]}},
  "sol": [["Lösung", ["Jüdisch: 5787 (Neujahr Rosch ha-Schana war am 12. September 2026; davor 5786).",
                      "Islamisch: 1448 (Neujahr war am 16./17. Juni 2026; davor 1447).",
                      "Die Jahre beginnen nicht am 1. Jänner (jüdisch im Herbst, islamisch wandert der Jahresbeginn), und das islamische Mondjahr ist ca. 11 Tage kürzer – "
                      "deshalb holt es jedes Jahr ein Stück auf."]]],
  "tip": ["Mondjahr und Sonnenjahr (Faustformeln)", "theorie.html#mond"]},

 {"id": "a2", "nr": 2, "title": "Schaltjahr oder nicht?", "src": "Buch-Aufgabe S. 13", "own": False, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Berechnen Sie, ob die folgenden Jahre Schaltjahre waren. Zusatz: Ist 2100 ein Schaltjahr?",
  "type": "multi",
  "fields": [["j1804", "1804", JN, False], ["j2000", "2000", JN, False], ["j1700", "1700", JN, False], ["j1902", "1902", JN, False],
             ["j1600", "1600", JN, False], ["j1730", "1730", JN, False], ["j2100", "Zusatz: 2100", JN, False]],
  "chk": {"j1804": {"sel": "Schaltjahr"}, "j2000": {"sel": "Schaltjahr"}, "j1700": {"sel": "kein Schaltjahr"}, "j1902": {"sel": "kein Schaltjahr"},
          "j1600": {"sel": "Schaltjahr"}, "j1730": {"sel": "kein Schaltjahr"}, "j2100": {"sel": "kein Schaltjahr"}},
  "sol": [["Lösung", ["1804 ja (durch 4) · 2000 ja (durch 400) · 1700 nein (durch 100, nicht durch 400) · 1902 nein (nicht durch 4) · "
                      "1600 ja (durch 400) · 1730 nein (nicht durch 4) · Zusatz: 2100 nein (durch 100, nicht durch 400)"]]],
  "tip": ["Die Schaltjahr-Regel: 4 – 100 – 400", "theorie.html#schalt"]},

 {"id": "a3", "nr": 3, "title": "Rechnen über die Zeitenwende", "src": "Theorie S. 13", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Achtung: Ein Jahr 0 gibt es nicht! a) Caesar wurde 44 v. Chr. ermordet. Wie viele Jahre ist das 2026 her? "
       "b) Ötzi starb um 3300 v. Chr. Vor wie vielen Jahren war das (Stand 2026)? Schreib jeweils die Rechnung dazu. "
       "c) Wiener Neustadt wurde 1194 gegründet. In welchem Jahrhundert? d) An welchem Tag begann das 21. Jahrhundert?",
  "type": "multi",
  "fields": [["caesar", "a) Jahre seit Caesars Tod (mit Rechnung)"], ["oetzi", "b) Jahre seit Ötzis Tod (mit Rechnung)"],
             ["jh", "c) Gründung Wiener Neustadt 1194 – im …", ["12. Jahrhundert", "11. Jahrhundert", "13. Jahrhundert", "19. Jahrhundert"]],
             ["beginn", "d) Das 21. Jahrhundert begann am …", ["1. Jänner 2001", "1. Jänner 2000", "31. Dezember 1999", "1. Jänner 2100"]]],
  "chk": {"caesar": {"kw": [["richtiges Ergebnis", r"\b2069\b|\b2\.?069\b"]]}, "oetzi": {"kw": [["richtiges Ergebnis", r"\b5\.?325\b"]]},
          "jh": {"sel": "12. Jahrhundert"}, "beginn": {"sel": "1. Jänner 2001"}},
  "sol": [["Lösung", ["a) 2026 + 44 − 1 = 2069 Jahre (minus 1, weil es kein Jahr 0 gibt)",
                      "b) 2026 + 3300 − 1 = 5325 Jahre (»um 3300« – also ungefähr 5300 Jahre)",
                      "c) 12. Jahrhundert (Hunderterstelle 11 + 1)",
                      "d) am 1. Jänner 2001 – das 1. Jahrhundert umfasst die Jahre 1 bis 100, also endet das 20. mit dem Jahr 2000."]]],
  "tip": ["Christi Geburt – und kein Jahr 0 · Jahrhunderte richtig zählen", "theorie.html#jahr0"]},

 {"id": "a4", "nr": 4, "title": "Wer zählt ab wann?", "src": "Theorie S. 13", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Jede Zeitrechnung braucht einen Bezugspunkt – ein »Jahr 1«. Ordne jeder Zeitrechnung ihren Bezugspunkt zu.",
  "type": "multi",
  "fields": [["jued", "jüdischer Kalender", first(BEZUG, BEZUG[0])],
             ["islam", "islamischer Kalender", first(BEZUG, BEZUG[1])],
             ["kopt", "koptischer Kalender (Christen in Ägypten)", first(BEZUG, BEZUG[2])],
             ["rom", "die alten Römer", first(BEZUG, BEZUG[3])],
             ["griech", "die alten Griechen", first(BEZUG, BEZUG[4])],
             ["japan", "Japan (heute neben unserem Kalender)", first(BEZUG, BEZUG[5])]],
  "chk": {"jued": {"sel": BEZUG[0]}, "islam": {"sel": BEZUG[1]}, "kopt": {"sel": BEZUG[2]}, "rom": {"sel": BEZUG[3]}, "griech": {"sel": BEZUG[4]}, "japan": {"sel": BEZUG[5]}},
  "sol": [["Lösung", ["jüdisch → Erschaffung der Welt (nach jüdischer Überlieferung 3761 v. Chr.)",
                      "islamisch → Hidschra 622 · koptisch → Diokletian 284",
                      "Römer → Gründung Roms 753 v. Chr. (»ab urbe condita«) · Griechen → erste Olympische Spiele 776 v. Chr. (Olympiaden)",
                      "Japan → Kaiser-Ära: seit 2019 Ära Reiwa, 2026 = Reiwa 8"]]],
  "tip": ["Zeitrechnungen nach Ereignissen", "theorie.html#ereignisse"]},

 {"id": "a5", "nr": 5, "title": "Papst Gregor und die verschwundenen Tage", "src": "Theorie S. 13", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "a) Welcher Tag folgte in Rom auf Donnerstag, den 4. Oktober 1582? b) Erkläre in 2 Sätzen, warum die Kalenderreform nötig war. "
       "c) Die »Oktoberrevolution« in Russland fand nach unserem Kalender am 7. November 1917 statt. Erkläre, wie das sein kann.",
  "type": "multi",
  "fields": [["tag", "a) Auf den 4. Oktober 1582 folgte …", ["Freitag, der 15. Oktober 1582", "Freitag, der 5. Oktober 1582", "Freitag, der 14. Oktober 1582", "Montag, der 1. November 1582"]],
             ["warum", "b) Darum war die Reform nötig (2 Sätze)"], ["okt", "c) Oktoberrevolution im November – so geht das"]],
  "chk": {"tag": {"sel": "Freitag, der 15. Oktober 1582"},
          "warum": {"kw": [["julianisches Jahr zu lang", "lang|minut|365|ungenau|abweich|verschob|falsch"], ["10 Tage / Frühling / Ostern verrutscht", "10|zehn|tag|frühling|ostern|sonne|jahreszeit"]]},
          "okt": {"kw": [["Russland: julianischer Kalender", "julian|alt|caesar"], ["13 Tage Unterschied", "13|dreizehn|tage|später|unterschied|hinter"]]}},
  "sol": [["a)", ["Freitag, der 15. Oktober 1582 – die Tage 5. bis 14. Oktober gab es dort nie."]],
          ["b)", ["Das julianische Jahr (365¼ Tage) war um ca. 11 Minuten länger als das Sonnenjahr. Bis 1582 hatte sich das auf 10 Tage summiert – "
                  "Frühlingsbeginn und Ostertermin rutschten immer weiter weg. Gregor XIII. strich 10 Tage und führte die neue Schaltregel ein."]],
          ["c)", ["Russland rechnete 1917 noch nach dem julianischen Kalender – dort war es der 25. Oktober. Der julianische Kalender lag damals 13 Tage hinter dem gregorianischen. "
                  "Russland stellte erst 1918 um."]]],
  "tip": ["Julianisch → gregorianisch", "theorie.html#gregor"]},

 # ======================================================= Stunde 2 · Epochen
 {"id": "a6", "nr": 6, "title": "Die Epochen auf dem Zeitstrahl", "src": "Theorie S. 14", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "a) Ordne jeder Epoche ihren ungefähren Zeitraum zu (Europa, Vorderasien, Nordafrika). "
       "b) Mit welchem Ereignis lässt man das Mittelalter oft beginnen – und mit welchen Ereignissen die Neuzeit?",
  "type": "multi",
  "fields": [["ur", "Ur- und Frühgeschichte", ["bis ca. 3000 v. Chr.", "ca. 3000 v. Chr. – 476 n. Chr.", "476 – ca. 1500", "ca. 1500 – 1914/18", "ab 1914/18"], False],
             ["alt", "Altertum (Antike)", ["bis ca. 3000 v. Chr.", "ca. 3000 v. Chr. – 476 n. Chr.", "476 – ca. 1500", "ca. 1500 – 1914/18", "ab 1914/18"], False],
             ["ma", "Mittelalter", ["bis ca. 3000 v. Chr.", "ca. 3000 v. Chr. – 476 n. Chr.", "476 – ca. 1500", "ca. 1500 – 1914/18", "ab 1914/18"], False],
             ["nz", "Neuzeit", ["bis ca. 3000 v. Chr.", "ca. 3000 v. Chr. – 476 n. Chr.", "476 – ca. 1500", "ca. 1500 – 1914/18", "ab 1914/18"], False],
             ["zg", "Zeitgeschichte", ["bis ca. 3000 v. Chr.", "ca. 3000 v. Chr. – 476 n. Chr.", "476 – ca. 1500", "ca. 1500 – 1914/18", "ab 1914/18"], False],
             ["mabeg", "b) Beginn des Mittelalters", ["Ende des Weströmischen Reichs 476", "Geburt Christi", "Kaiserkrönung Karls des Großen 800", "Pest 1348"]],
             ["nzbeg", "b) Beginn der Neuzeit (um 1500)", ["Buchdruck, Entdeckung Amerikas 1492, Reformation 1517", "Ende des Weströmischen Reichs 476",
                                                        "Französische Revolution 1789", "Erster Weltkrieg 1914"]]],
  "chk": {"ur": {"sel": "bis ca. 3000 v. Chr."}, "alt": {"sel": "ca. 3000 v. Chr. – 476 n. Chr."}, "ma": {"sel": "476 – ca. 1500"},
          "nz": {"sel": "ca. 1500 – 1914/18"}, "zg": {"sel": "ab 1914/18"},
          "mabeg": {"sel": "Ende des Weströmischen Reichs 476"}, "nzbeg": {"sel": "Buchdruck, Entdeckung Amerikas 1492, Reformation 1517"}},
  "sol": [["a)", ["Ur- und Frühgeschichte bis ca. 3000 v. Chr. (erste Schrift) · Altertum ca. 3000 v. Chr. – 476 · Mittelalter 476 – ca. 1500 · "
                  "Neuzeit ca. 1500 – 1914/18 · Zeitgeschichte ab 1914/18"]],
          ["b)", ["Mittelalter: Ende des Weströmischen Reichs 476 · Neuzeit: Buchdruck (um 1450), Entdeckung Amerikas 1492, Reformation 1517"]]],
  "tip": ["Die Epochen im Überblick", "theorie.html#ueberblick"]},

 {"id": "a7", "nr": 7, "title": "Welche Epoche ist das?", "src": "Theorie S. 14", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Ordne jedes Ereignis der richtigen Epoche zu.",
  "type": "multi",
  "fields": [["oetzi", "Ötzi stirbt am Tisenjoch (um 3300 v. Chr.)", EP, False],
             ["olymp", "Erste Olympische Spiele in Olympia (776 v. Chr.)", EP, False],
             ["caesar", "Caesar wird in Rom ermordet (44 v. Chr.)", EP, False],
             ["wn", "Gründung von Wiener Neustadt (1194)", EP, False],
             ["pest", "Die Pest tötet rund ein Drittel der Europäer (1348)", EP, False],
             ["wien", "Die Osmanen belagern Wien (1683)", EP, False],
             ["milak", "Militärakademie Wiener Neustadt gegründet (1751/52)", EP, False],
             ["sv", "Staatsvertrag – das Bundesheer entsteht (1955)", EP, False],
             ["iphone", "Apple stellt das erste iPhone vor (2007)", EP, False]],
  "chk": {"oetzi": {"sel": EP[0]}, "olymp": {"sel": EP[1]}, "caesar": {"sel": EP[1]}, "wn": {"sel": EP[2]}, "pest": {"sel": EP[2]},
          "wien": {"sel": EP[3]}, "milak": {"sel": EP[3]}, "sv": {"sel": EP[4]}, "iphone": {"sel": EP[4]}},
  "sol": [["Lösung", ["Ötzi → Ur- und Frühgeschichte (Kupferzeit) · Olympische Spiele und Caesar → Altertum",
                      "Wiener Neustadt (Hochmittelalter) und Pest (Spätmittelalter) → Mittelalter",
                      "Belagerung Wiens und Militärakademie → Neuzeit · Staatsvertrag und Smartphone → Zeitgeschichte"]]],
  "tip": ["Die Epochen im Überblick", "theorie.html#ueberblick"]},

 {"id": "a8", "nr": 8, "title": "Waffen und Werkzeuge erzählen Geschichte", "src": "Theorie S. 14", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "a) Ordne zu: In welcher Epoche waren diese Waffen typisch? "
       "b) Die Urgeschichte wird nach Werkstoffen eingeteilt (Stein-, Kupfer-, Bronze-, Eisenzeit). Erkläre in 1–2 Sätzen, warum man sie nicht – wie später – nach Herrschern oder Ereignissen benennt.",
  "type": "multi",
  "fields": [["faust", "Faustkeil und Speer mit Steinspitze", EP, False], ["legion", "Kurzschwert (Gladius) und Schild der römischen Legion", EP, False],
             ["ritter", "Ritterrüstung, Lanze und Armbrust", EP, False], ["muskete", "Muskete und Kanone eines stehenden Heeres", EP, False],
             ["drohne", "Kampfdrohne und Cyberangriff", EP, False],
             ["warum", "b) Darum nach Werkstoffen benannt (1–2 Sätze)"]],
  "chk": {"faust": {"sel": EP[0]}, "legion": {"sel": EP[1]}, "ritter": {"sel": EP[2]}, "muskete": {"sel": EP[3]}, "drohne": {"sel": EP[4]},
          "warum": {"kw": [["keine Schrift", "schrift|geschrieben|text|lesen|aufgeschrieben"], ["Funde / Sachkultur", "fund|werkzeug|sach|gegenst|ausgrab|archäolog|material|übrig"]]}},
  "sol": [["a)", ["Faustkeil → Ur- und Frühgeschichte · Gladius → Altertum · Ritter → Mittelalter · Muskete → Neuzeit · Drohne → Zeitgeschichte"]],
          ["b)", ["Aus dieser Zeit gibt es keine Schrift, also keine Namen von Herrschern und keine aufgeschriebenen Ereignisse. "
                  "Erhalten sind nur Gegenstände (Sachkultur) – deshalb ordnet man nach dem Material, aus dem Werkzeuge und Waffen gemacht wurden."]]],
  "tip": ["Waffen erzählen Geschichte · Urgeschichte: nach Werkstoffen benannt", "theorie.html#waffen"]},

 {"id": "a9", "nr": 9, "title": "Lange und kurze Jahrhunderte", "src": "Theorie S. 14", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Manche Historiker lassen Jahrhunderte »lang« oder »kurz« dauern. a) Ordne zu. "
       "b) Begründe in 1–2 Sätzen, warum das »kurze 20. Jahrhundert« genau 1914 beginnt und 1989 endet.",
  "type": "multi",
  "fields": [["kurz20", "das »kurze« 20. Jahrhundert", ["1914 – 1989", "1789 – 1914", "1700 – 1815", "1450 – 1620"]],
             ["lang19", "das »lange« 19. Jahrhundert", ["1789 – 1914", "1914 – 1989", "1700 – 1815", "1450 – 1620"]],
             ["lang16", "das »lange« 16. Jahrhundert", ["1450 – 1620", "1914 – 1989", "1789 – 1914", "1700 – 1815"]],
             ["begr", "b) Warum 1914 bis 1989? (1–2 Sätze)"]],
  "chk": {"kurz20": {"sel": "1914 – 1989"}, "lang19": {"sel": "1789 – 1914"}, "lang16": {"sel": "1450 – 1620"},
          "begr": {"kw": [["1914: Erster Weltkrieg", "weltkrieg|krieg|1914"], ["1989: Mauerfall / Ende Ost-West-Konflikt", "mauer|kalt|ost|kommun|sowjet|wende|1989|eiser"]]}},
  "sol": [["a)", ["kurzes 20. Jh. 1914–1989 · langes 19. Jh. 1789–1914 · langes 16. Jh. 1450–1620 (langes 18. Jh. 1700–1815)"]],
          ["b)", ["1914 beginnt mit dem Ersten Weltkrieg eine neue Zeit (Weltkriege, Diktaturen); 1989 endet mit dem Fall der Berliner Mauer der Ost-West-Konflikt. "
                  "Für die Einteilung zählen die prägenden Ereignisse, nicht die runden Jahreszahlen."]]],
  "tip": ["Lange und kurze Jahrhunderte", "theorie.html#jahrhunderte"]},

 {"id": "a10", "nr": 10, "title": "Wessen Geschichte?", "src": "Theorie S. 14", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "a) Erkläre den Begriff Eurozentrismus in 1–2 Sätzen mit einem Beispiel. "
       "b) Um 600 v. Chr. gehört Athen schon zur Antike, Hallstatt im Salzkammergut aber noch zur Urgeschichte. Warum? "
       "c) Eine Zeittafel aus Deutschland hat eine Spalte »Deutsche Geschichte«. Nenne zwei Ereignisse der österreichischen Zeitgeschichte, die in einer österreichischen Zeittafel stehen müssten.",
  "type": "multi",
  "fields": [["euro", "a) Eurozentrismus (1–2 Sätze, mit Beispiel)"], ["hall", "b) Darum Athen Antike, Hallstatt Urgeschichte"],
             ["oe1", "c) Ereignis 1 (mit Jahr)"], ["oe2", "c) Ereignis 2 (mit Jahr)"]],
  "chk": {"euro": {"kw": [["europäische Sicht / Maßstab", "europ"], ["andere Kulturen / Beispiel", "china|amerika|afrika|asien|indien|inka|maya|andere|welt|kultur|mittelalter"]]},
          "hall": {"kw": [["Schrift", "schrift|geschrieben|schreib|text"]]},
          "oe1": {"kw": [["Ereignis mit Jahr", r"1918|1938|1945|1955|1995|1919|1934|1956"]]},
          "oe2": {"kw": [["Ereignis mit Jahr", r"1918|1938|1945|1955|1995|1919|1934|1956"]]}},
  "sol": [["a)", ["Eurozentrismus heißt: Man beurteilt die Welt mit europäischen Maßstäben. Beispiel: Das »Mittelalter« meint die Zeit zwischen dem Ende der römischen Kultur "
                  "und ihrer Wiederentdeckung – für China, Afrika oder Amerika passt das nicht."]],
          ["b)", ["In Athen gab es Schrift – wir haben Texte, Inschriften, Namen. Die Menschen in Hallstatt hinterließen keine eigenen schriftlichen Quellen, nur Funde (Gräber, Salzbergbau)."]],
          ["c) zum Beispiel", ["1918 Ende der Monarchie, Republik · 1938 »Anschluss« an das Deutsche Reich · 1945 Zweite Republik · 1955 Staatsvertrag, Neutralität, Bundesheer · 1995 EU-Beitritt"]]],
  "tip": ["Wessen Geschichte? Eurozentrismus · Zeitgeschichte in Österreich", "theorie.html#euro"]},

 # ======================================================= Für Schnelle und Neugierige
 {"id": "a11", "nr": 11, "title": "Die militärische Datum-Zeit-Gruppe", "src": "Theorie S. 13", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Im Einsatz steht über jeder Meldung eine Datum-Zeit-Gruppe. Entschlüssle »070630AJAN27«: a) Tag b) Uhrzeit c) Zeitzone d) Monat und Jahr. "
       "e) Schreibe die Datum-Zeit-Gruppe für: Abmarsch am 18. Oktober 2026 (Sommerzeit) um 21:45 Uhr.",
  "type": "multi",
  "fields": [["tag", "a) Tag"], ["zeit", "b) Uhrzeit"],
             ["zone", "c) Zeitzone A bedeutet …", ["Winterzeit in Österreich (MEZ = Weltzeit + 1 h)", "Sommerzeit in Österreich (MESZ = Weltzeit + 2 h)", "Weltzeit (UTC)", "Ortszeit in Amerika"]],
             ["mj", "d) Monat und Jahr", ["Jänner 2027", "Juni 2027", "Juli 2026", "Jänner 2007"]],
             ["dzg", "e) Deine Datum-Zeit-Gruppe"]],
  "chk": {"tag": {"num": 7, "unit": ""}, "zeit": {"kw": [["Uhrzeit", r"0?6[:.]?30"]]},
          "zone": {"sel": "Winterzeit in Österreich (MEZ = Weltzeit + 1 h)"}, "mj": {"sel": "Jänner 2027"},
          "dzg": {"kw": [["Tag + Uhrzeit", r"182145"], ["Zone B", r"182145\s*b"], ["Monat + Jahr", r"okt\s*26"]]}},
  "sol": [["Lösung", ["a) 7. · b) 06:30 Uhr · c) A = MEZ (Winterzeit, Weltzeit + 1 Stunde) · d) Jänner 2027", "e) 182145BOKT26"]]],
  "tip": ["Zeit im Einsatz", "theorie.html#dzg"]},

 {"id": "a12", "nr": 12, "title": "Knobelaufgabe: Geburtstag am 29. Februar", "src": "Theorie S. 13", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Ein Kind wird am 29. Februar 2028 geboren. Wie oft kann es bis einschließlich 2100 an seinem »echten« Geburtstag feiern (den Tag der Geburt nicht mitgezählt)? Schreib deinen Rechenweg dazu.",
  "type": "multi", "fields": [["anz", "Anzahl echter Geburtstage (mit Rechenweg)"]],
  "chk": {"anz": {"kw": [["richtige Anzahl", r"\b17\b"]]}},
  "sol": [["Lösung", ["Schaltjahre nach 2028: 2032, 2036, … 2096 → (2096 − 2032) : 4 + 1 = 17. 2100 ist kein Schaltjahr (durch 100, nicht durch 400). Also 17-mal."]]],
  "tip": ["Die Schaltjahr-Regel: 4 – 100 – 400", "theorie.html#schalt"]},

 {"id": "a13", "nr": 13, "title": "Sport: Marathon und die Olympiaden", "src": "Theorie S. 13", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Die Griechen zählten in Olympiaden: Die 1. Olympiade umfasst die Jahre 776 bis 773 v. Chr., jede Olympiade dauert 4 Jahre. "
       "Die Schlacht bei Marathon (Ursprung des Marathonlaufs) war 490 v. Chr. In welcher Olympiade? Schreib deinen Rechenweg dazu.",
  "type": "multi", "fields": [["olymp", "Nummer der Olympiade (mit Rechenweg)"]],
  "chk": {"olymp": {"kw": [["richtige Olympiade", r"\b72\b"]]}},
  "sol": [["Lösung", ["776 − 490 = 286 Jahre nach Beginn · 286 : 4 = 71,5 → 71 volle Olympiaden sind vorbei → die 72. Olympiade (492–489 v. Chr.). "
                      "Die Griechen schrieben: »im 3. Jahr der 72. Olympiade«."]]],
  "tip": ["Zeitrechnungen nach Ereignissen", "theorie.html#ereignisse"]},

 {"id": "a14", "nr": 14, "title": "Wirtschaft: Ein Kalender spart Geld", "src": "Theorie S. 13", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Saudi-Arabien zahlt seit Oktober 2016 die Gehälter im Staatsdienst nach dem gregorianischen statt nach dem islamischen Kalender – 12 Monatsgehälter pro Jahr wie bisher. "
       "a) Wie viele Tage ist ein islamisches Mondjahr ungefähr kürzer als unser Sonnenjahr? b) Um wie viel Prozent arbeiten die Beamten nun für dasselbe Jahresgehalt mehr? (365 statt 354 Tage, auf eine Kommastelle) "
       "c) Erkläre in 1–2 Sätzen, warum der Staat damit spart.",
  "type": "multi", "fields": [["tage", "a) Tage kürzer"], ["proz", "b) Prozent mehr (mit Rechnung)"], ["warum", "c) Darum spart der Staat"]],
  "chk": {"tage": {"num": 11, "unit": ""}, "proz": {"num": 3.1, "unit": ""},
          "warum": {"kw": [["gleiches Gehalt", "gehalt|lohn|zahl|geld|monat"], ["mehr Tage / längeres Jahr", "länger|mehr|11|tage|arbeit"]]}},
  "sol": [["Lösung", ["a) ca. 11 Tage (354 statt 365)", "b) (365 − 354) : 354 · 100 ≈ 3,1 %",
                      "c) Die 12 Monatsgehälter verteilen sich jetzt auf ein längeres Jahr. Der Staat zahlt pro Jahr nicht mehr, bekommt aber 11 Arbeitstage mehr – das spart rund 3 % der Lohnkosten."]]],
  "tip": ["Mondjahr und Sonnenjahr", "theorie.html#mond"]},

 {"id": "a15", "nr": 15, "title": "Ökologie: Leben wir im Anthropozän?", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Forscher schlugen vor, eine neue Erd-Epoche auszurufen: das Anthropozän, das »Zeitalter des Menschen«. a) Welche Spuren des Menschen würden Geologen in Millionen Jahren finden? Nenne zwei. "
       "b) Wie hat die Fachwelt 2024 entschieden? Suchtipp: »Anthropozän abgelehnt 2024« auf derstandard.at oder orf.at. c) Deine Meinung in 1–2 Sätzen: Brauchen wir den Begriff?",
  "type": "multi", "fields": [["spuren", "a) Zwei Spuren"], ["2024", "b) Entscheidung 2024"], ["meinung", "c) Meine Meinung"]],
  "chk": {"spuren": {"kw": [["Spur des Menschen", "plastik|beton|radioakt|atom|plutonium|co2|kohlen|hühner|knochen|müll|asphalt|abgas|ruß|mikroplastik"]]},
          "2024": {"kw": [["abgelehnt", "abgelehnt|nein|dagegen|nicht anerkannt|ablehn"]]}},
  "sol": [["Lösung", ["a) Plastik und Mikroplastik, Beton, radioaktive Spuren der Atombombentests ab 1950, Ruß aus Kohle, Knochen von Masthühnern …",
                      "b) Im März 2024 lehnte die zuständige Fachkommission der Geologen das Anthropozän als offizielle Erd-Epoche ab (12 dagegen, 4 dafür). Offiziell leben wir weiter im Holozän.",
                      "c) Kein Richtig oder Falsch – die Begründung zählt. Als Begriff für den großen Einfluss des Menschen wird »Anthropozän« weiter verwendet."]]],
  "tip": ["Für Schnelle: Ein neues Erdzeitalter?", "theorie.html#schnelle"]},
]
assert [t["nr"] for t in T] == list(range(1, 16))

GRP = {1: "Stunde 1 · Wie zählen wir Zeit? (Buch S. 13)", 2: "Stunde 2 · Die Epochen (Buch S. 14)", 0: "Für Schnelle und Neugierige · optional"}

LERNZIELE = ["erklären, wie wir Jahre zählen (Christi Geburt, v. Chr. / n. Chr., Jahrhunderte, **kein Jahr 0**) und über die Zeitenwende rechnen",
             "**andere Kalender** nennen (jüdisch, islamisch, julianisch, gregorianisch …) und erklären, warum sie verschieden zählen",
             "die **Epochen** von der Urgeschichte bis zur Zeitgeschichte in der richtigen Reihenfolge nennen – mit Zeitraum, Wendepunkten und typischen Merkmalen",
             "Ereignisse den Epochen zuordnen und erklären, warum Epochengrenzen nicht überall gleich sind (**Eurozentrismus**)"]

WICHTIGSTE = ["Wir zählen die Jahre ab **Christi Geburt** – ein **Jahr 0** gibt es nicht; andere Kalender zählen ab anderen Bezugspunkten (jüdisch 3761 v. Chr., islamisch 622 n. Chr.).",
              "Der **gregorianische Kalender** (1582) verbesserte den julianischen: 10 Tage fielen weg, und volle Hunderterjahre sind nur Schaltjahre, wenn sie durch 400 teilbar sind.",
              "Seit der Renaissance teilt man die Geschichte in **Altertum – Mittelalter – Neuzeit**; davor liegt die schriftlose **Ur- und Frühgeschichte**, danach die **Zeitgeschichte** mit Zeitzeugen.",
              "Wendepunkte wie **476, um 1500 und 1914/18** markieren Epochengrenzen – die Grenzen sind aber Vereinbarungen der Historiker, keine Naturgesetze.",
              "Die Dreiteilung passt für Europa, Vorderasien und Nordafrika – wer sie der ganzen Welt überstülpt, denkt **eurozentrisch**; die **Globalgeschichte** sucht andere Einteilungen."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Epoche", "Zeitabschnitt mit gemeinsamen Merkmalen (griech. epoché = Haltepunkt)"],
                ["Periodisierung", "Einteilung der Geschichte in Epochen"],
                ["Zeitrechnung", "Zählung der Jahre ab einem Bezugspunkt (»Jahr 1«)"],
                ["v. Chr. / n. Chr.", "vor / nach Christi Geburt – ein Jahr 0 gibt es nicht"],
                ["Sonnenjahr / Mondjahr", "365,24 Tage (Erde um die Sonne) / ca. 354 Tage (12 Mondmonate)"],
                ["julianischer Kalender", "Caesars Kalender (46 v. Chr.): Schaltjahr alle 4 Jahre"],
                ["gregorianischer Kalender", "Papst Gregor XIII. (1582): 10 Tage gestrichen, neue Schaltregel"],
                ["Hidschra", "Auswanderung Mohammeds nach Medina 622 – Beginn des islamischen Kalenders"],
                ["Ur- und Frühgeschichte", "Zeit ohne Schrift – nach Werkstoffen eingeteilt (Stein, Kupfer, Bronze, Eisen)"],
                ["Altertum / Antike", "Hochkulturen und griechisch-römische Welt bis 476"],
                ["Mittelalter", "476 bis ca. 1500 – Früh-, Hoch- und Spätmittelalter"],
                ["Neuzeit", "ab ca. 1500 – Buchdruck, Entdeckungen, Reformation, Revolutionen"],
                ["Zeitgeschichte", "jüngste Geschichte, von der noch Zeitzeugen leben"],
                ["Eurozentrismus", "andere Kulturen mit europäischen Maßstäben beurteilen"],
                ["Globalgeschichte", "Geschichte aller Weltregionen und ihrer Verbindungen"]]

WEISST_DU_NOCH = [("Welches Jahr folgt auf 1 v. Chr.?", "1 n. Chr. – ein Jahr 0 gibt es nicht."),
                  ("War 1900 ein Schaltjahr?", "Nein – durch 100, aber nicht durch 400 teilbar."),
                  ("Welcher Kalender richtet sich nach dem Mond?", "der islamische – sein Jahr ist ca. 11 Tage kürzer.")]

STOLPERSTEINE = [("Jahr 0", "Über die Zeitenwende addieren und **1 abziehen** (44 v. Chr. → 2026 = 2069 Jahre) – viele vergessen das."),
                 ("Jahrhundert zählen", "Hunderterstelle **+ 1**: 1194 → 12. Jh., »die 1500er-Jahre« = 16. Jh.; das 21. Jh. begann 2001."),
                 ("Schaltjahr-Regel", "1900 und 2100 sind **keine** Schaltjahre, 2000 schon (durch 400). Viele prüfen nur »durch 4«."),
                 ("Epochengrenzen", "Buch, Video und Zeittafel nennen **verschiedene Jahreszahlen** (Antike ab 3000, 800 oder 500 v. Chr.) – die Begründung zählt, nicht die eine »richtige« Zahl."),
                 ("Gleichzeitig verschieden", "Um 600 v. Chr. ist Griechenland schon Antike, Mitteleuropa noch Urgeschichte – entscheidend ist die **Schrift**. Und: »Finsteres Mittelalter« und »Erde als Scheibe« sind Mythen.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Zeitrechnung", "Ab welchem Ereignis zählen wir unsere Jahre?", ["Christi Geburt", "Gründung Roms", "Erschaffung der Welt", "Auswanderung Mohammeds"],
  "Seit dem 6. Jahrhundert zählt man im christlichen Kulturkreis ab Christi Geburt.", "Buch S. 13"),
 ("Zeitrechnung", "Welches Jahr folgt auf das Jahr 1 v. Chr.?", ["1 n. Chr.", "das Jahr 0", "2 v. Chr.", "0 n. Chr."],
  "Ein Jahr 0 gibt es in unserer Zeitrechnung nicht.", "Buch S. 13"),
 ("Zeitrechnung", "Wie viele Jahre liegen zwischen 10 v. Chr. und 10 n. Chr.?", ["19", "20", "21", "0"],
  "10 + 10 − 1 = 19 – minus 1, weil das Jahr 0 fehlt.", "Buch S. 13"),
 ("Zeitrechnung", "Zu welchem Jahrhundert gehört 1683 (Belagerung Wiens)?", ["17. Jahrhundert", "16. Jahrhundert", "18. Jahrhundert", "15. Jahrhundert"],
  "Hunderterstelle + 1: 16 + 1 = 17.", "Buch S. 13"),
 ("Kalender", "Welcher Tag folgte in Rom auf den 4. Oktober 1582?", ["der 15. Oktober", "der 5. Oktober", "der 14. Oktober", "der 1. November"],
  "Papst Gregor XIII. strich 10 Tage, damit der Kalender wieder zum Sonnenjahr passt.", "Buch S. 13"),
 ("Kalender", "Welches Jahr ist KEIN Schaltjahr?", ["1900", "2000", "2024", "1600"],
  "1900 ist durch 100, aber nicht durch 400 teilbar – also kein Schaltjahr.", "Buch S. 13"),
 ("Kalender", "Wer führte den Kalender mit einem Schaltjahr alle 4 Jahre ein?", ["Gaius Julius Caesar", "Papst Gregor XIII.", "Karl der Große", "Napoleon"],
  "Der julianische Kalender (46 v. Chr.) ist nach Caesar benannt.", "Buch S. 13"),
 ("Kalender", "Warum wandert der Fastenmonat Ramadan durch das Jahr?", ["Das islamische Mondjahr ist ca. 11 Tage kürzer.", "Er wird jedes Jahr neu ausgelost.",
                                                                      "Der Kalender hat 13 Monate.", "Wegen der Sommerzeit"],
  "12 Mondmonate ergeben nur ca. 354 Tage – der Ramadan rückt jedes Jahr ca. 11 Tage nach vorne.", "Buch S. 13"),
 ("Kalender", "Ab welchem Ereignis zählt der islamische Kalender?", ["Auswanderung Mohammeds nach Medina 622", "Geburt Mohammeds", "Erschaffung der Welt", "Gründung Mekkas"],
  "Die Hidschra (Auswanderung) 622 ist das Jahr 1 des islamischen Kalenders.", "Buch S. 13"),
 ("Epochen", "Seit wann teilt man die Geschichte in Altertum, Mittelalter und Neuzeit?", ["seit der Renaissance", "seit der Antike", "seit 1945", "seit Karl dem Großen"],
  "Gelehrte der Renaissance sahen ihre Zeit als Wiedergeburt der Antike – dazwischen lag für sie das »mittlere« Zeitalter.", "Buch S. 14"),
 ("Epochen", "Wonach teilt man die Urgeschichte ein?", ["nach dem Werkstoff der Werkzeuge", "nach den Königen", "nach den Kriegen", "nach den Religionen"],
  "Ohne Schrift bleiben nur Funde – daher Stein-, Kupfer-, Bronze- und Eisenzeit.", "Buch S. 14"),
 ("Epochen", "Mit welchem Ereignis lässt man das Mittelalter oft beginnen?", ["Ende des Weströmischen Reichs 476", "Geburt Christi", "Kaiserkrönung Karls 800", "Entdeckung Amerikas 1492"],
  "476 setzten Germanen den letzten weströmischen Kaiser ab.", "Buch S. 14"),
 ("Epochen", "Was gehört NICHT zum Beginn der Neuzeit um 1500?", ["Ende des Weströmischen Reichs", "Buchdruck", "Entdeckung Amerikas", "Reformation"],
  "476 ist der Beginn des Mittelalters. Buchdruck, 1492 und 1517 stehen für den Beginn der Neuzeit.", "Buch S. 14"),
 ("Epochen", "Welche Epoche ist nach einem Ort in Österreich benannt?", ["die Hallstattzeit (Eisenzeit)", "die Bronzezeit", "das Hochmittelalter", "die Renaissance"],
  "Funde aus Hallstatt im Salzkammergut gaben der älteren Eisenzeit (ca. 800–450 v. Chr.) den Namen.", "Buch S. 14"),
 ("Epochen", "Was ist Zeitgeschichte?", ["Geschichte, von der noch Zeitzeugen leben", "die Zeit vor der Schrift", "nur das 21. Jahrhundert", "die Geschichte der Uhren"],
  "Die jüngste Geschichte nennt man Zeitgeschichte – Zeitzeugen können noch berichten.", "Buch S. 14"),
 ("Epochen", "Das »kurze 20. Jahrhundert« dauert von …", ["1914 bis 1989", "1900 bis 1999", "1918 bis 1945", "1945 bis 2000"],
  "Vom Ersten Weltkrieg bis zum Fall der Berliner Mauer.", "Buch S. 14"),
 ("Epochen", "Was bedeutet Eurozentrismus?", ["andere Kulturen mit europäischen Maßstäben beurteilen", "Europa liegt in der Mitte der Weltkarte",
                                              "der Sitz der EU-Zentralbank", "Geschichte nur aus asiatischer Sicht"],
  "Die Globalgeschichte versucht, diese europäische Sicht zu überwinden.", "Buch S. 14"),
 ("Epochen", "Wiener Neustadt wurde 1194 gegründet. In welcher Epoche?", ["Hochmittelalter", "Antike", "Frühe Neuzeit", "Spätmittelalter"],
  "Das Hochmittelalter reicht etwa von 1000 bis 1250.", "Buch S. 14"),
]

ZEITSTRAHL_KARTEN = [  # Lebender Zeitstrahl (Stunde 2, ohne Handy): (Jahr, Ereignis, Epoche)
 ("um 2,5 Mio. v. Chr.", "erste Steinwerkzeuge in Afrika", 0), ("um 9000 v. Chr.", "Ackerbau beginnt im Vorderen Orient", 0),
 ("um 3300 v. Chr.", "Ötzi stirbt am Tisenjoch", 0), ("um 3000 v. Chr.", "Schrift in Mesopotamien und Ägypten", 1),
 ("um 2580 v. Chr.", "Bau der Cheops-Pyramide", 1), ("um 800 v. Chr.", "Salzbergbau in Hallstatt", 0),
 ("776 v. Chr.", "erste Olympische Spiele", 1), ("44 v. Chr.", "Caesar wird ermordet", 1),
 ("476", "Ende des Weströmischen Reichs", 2), ("800", "Kaiserkrönung Karls des Großen", 2),
 ("1194", "Gründung von Wiener Neustadt", 2), ("1348", "Pest in Europa", 2),
 ("um 1450", "Gutenberg erfindet den Buchdruck", 3), ("1492", "Kolumbus erreicht Amerika", 3),
 ("1517", "Luthers Thesen – Reformation", 3), ("1683", "Osmanen belagern Wien", 3),
 ("1751/52", "Militärakademie Wiener Neustadt", 3), ("1789", "Französische Revolution", 3),
 ("1914", "Erster Weltkrieg beginnt", 4), ("1945", "Ende des Zweiten Weltkriegs", 4),
 ("1955", "Staatsvertrag – Bundesheer entsteht", 4), ("1989", "Fall der Berliner Mauer", 4),
 ("1995", "Österreich tritt der EU bei", 4), ("2007", "das erste iPhone kommt", 4)]
