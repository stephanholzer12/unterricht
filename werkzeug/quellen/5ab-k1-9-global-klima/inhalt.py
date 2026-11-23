"""TÖW 5AB · K1.9 Globalisierung (Buch Teil I, S. 39–44) gekoppelt mit Klima und Klimaveränderungen (Teil II, S. 69–76, nur Treibhauseffekt und Klimapolitik) – v1.
Grundlage: Planübersicht v1 (Projekt »5. Klasse TÖW«, claude/planuebersicht-globalisierung-klima-ki-v1.md) und Stephans Antworten vom 22.11.2026:
Ziele passen · Klima kommt im Jänner noch mit 1–2 Stunden (hier nur Treibhauseffekt und Konferenzen) · keine Demo, stattdessen Video ·
Globalisierung der Ökosysteme kurz in Stunde 1 · kein Kahoot, beide Klassen machen den Mini-Klimagipfel · gleich bauen.
Jahresplan v22: E6 (Globalisierung, 2 Std., K05, K07) + E7 (Klima, 2 Std., K03) → hier 3 Stunden; Rest von E7 im Jänner.
Keine Daten auf den Kadetten-Seiten: Termine nur im Kalender der privaten Lösungsseite. 5AK: Referat »Luftverschmutzung« in Stunde 2.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge).
Alle Zahlen aus geprüften Quellen (QUELLEN unten); Rechenwege mit Python-Kontrollen am Ende."""

STAND = "22.11.2026"
V = "v1"
ORDNER = "5ab-toew/k1-9-global-klima"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ab-toew/"
EYEBROW = "TÖW · 5AB · K1.9 Globalisierung · Klima"
TITEL = "Ein Planet reicht nicht – Abdruck, KI und Klimapolitik"
KURZTITEL = "Globalisierung, KI und Klima"
BUCH = "Buch S. 39–44, 71–75"
KEY = "26-27-5AB-K1.9-Global-TH-Handy-v1"
LERNSEITE_KEY = "26-27-5AB-K1.9-Global-Lernseite-Check-v1"
PRAEFIX = "26-27-5AB-K1.9-Global-Klima"
KLASSEN = ["5AK", "5BK"]
GRUPPEN = 6
STUNDEN = 3

# Zahlen (geprüft, siehe QUELLEN)
OS_AT, OS_AT_TAG = "2. April", 92          # Overshoot Day Österreich 2026 (GFN, APA/vol.at)
OS_WELT, OS_WELT_TAG = "30. Juli", 211     # Earth Overshoot Day 2026 (Global Footprint Network)
HANDY_KG, RUCKSACK_KG = 0.1, 75            # Handy rund 100 g; Rucksack rund 75 kg (Verbraucherzentrale NRW, Wuppertal Institut 75,3 kg)
GEMINI_WH, OPENAI_WH = 0.24, 0.34          # Herstellerangaben pro Textanfrage (ORF 22.08.2025)
KR_MW, KR_TWH, KR_HH = 150, 1.31, 375_000  # Kronstorf Stufe 1 (ORF 17.07.2026)
KR_WASSER = "5,8 Millionen Liter"          # erwärmtes Kühlwasser pro Tag höchstens, max. 30 °C, 99 l/s (ORF 17.07.2026)
OOE_TWH = 14                               # Stromverbrauch Oberösterreich 2024 (ORF 17.07.2026)
RIND_T, RIND_ZOLL, EU_RIND_T = 99_000, 7.5, 8_000_000   # Mercosur-Kontingent, EU-Verbrauch (WKO-Factsheet, EU-Kommission)

VS = {}   # kein Schülerversuch in dieser Einheit (Stephan: keine Demo, Video)
DEMOS = {}
VIDEO = {1: "Kurzvideo zum ökologischen Fußabdruck (Prof. HOLZER wählt es aus der Liste auf der Lösungsseite)"}

STUNDENTITEL = {1: "Ein Planet reicht nicht: Wie groß ist dein Abdruck?",
                2: "Deine KI-Frage hat ein Gewicht: Rechenzentren in Österreich",
                3: "Gipfel geplatzt: Wer bremst beim Klima, wer verdient am Handel?"}
STUNDENNAME = {n: f"Stunde {n} · {t}" for n, t in STUNDENTITEL.items()}

# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 40", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Zwei Schätzfragen zum Start – ohne Punkte. In Stunde 3 siehst du, was du heute gedacht hast.",
  "hint": "Bauchgefühl reicht. Deine Antwort bleibt gespeichert.",

  "type": "multi", "vorhersage": True,
  "fields": [["p1", "a) Würden alle Menschen so leben wie wir in Österreich: Wie viele Erden bräuchten wir?",
              ["etwa 4 Erden", "etwa 2 Erden", "genau 1 Erde – das passt sich aus"], False],
             ["p2", "b) Google baut in Kronstorf (Oberösterreich) ein Rechenzentrum, auch für KI. Die erste Ausbaustufe braucht im Jahr so viel Strom wie …",
              ["rund 375 000 Haushalte", "rund 3 700 Haushalte", "rund 37 000 Haushalte"], False]],
  "chk": {},
  "aufloesung": [["p1", "etwa 4 Erden", "Österreich hatte 2026 sein Jahresbudget an Natur schon am 2. April verbraucht. 365 : 92 ergibt fast 4 – so viele Erden bräuchte die Menschheit, wenn alle so lebten wie wir."],
                 ["p2", "rund 375 000 Haushalte", "Die erste Stufe (150 MW) kann laut ORF bis zu 1,31 Terawattstunden im Jahr brauchen – so viel wie etwa 375 000 Haushalte."]],
  "sol": [["Auflösung", ["a) etwa 4 Erden (365 : 92 ≈ 4,0).", "b) rund 375 000 Haushalte (ORF, 17.07.2026)."]]],
  "tipps": [], "tip": ["Der ökologische Fußabdruck", "theorie.html#abdruck"]},

 {"id": "a1", "nr": 2, "title": "Mein Abdruck – und der von Österreich", "src": "Buch S. 40, 41 · Buch-Aufgabe S. 40", "own": False, "tag": "Stunde 1", "h": 1, "zeit": 14, "marke": "SELBSTSTUDIUM",
  "sim": ["overshoot"],
  "link": ["Fußabdruck-Rechner für Österreich öffnen", "https://www.mein-fussabdruck.at/", "Rechner im Auftrag des Klimaschutzministeriums (BMLUK) · Schnellrechner ca. 5 min · keine Anmeldung"],
  "q": "Mach den Fußabdruck-Rechner (Knopf oben, ca. 5 min). Die 5AK nimmt ihr Ergebnis vom letzten Mal. Dann beantworte a) bis i).",
  "hint": "Dein Ergebnis zeigst du niemandem. Bei c), d) und f) auf eine Kommastelle runden. Overshoot Day: An diesem Tag ist das Naturbudget eines Jahres aufgebraucht. Erden = 365 : Tag des Jahres. Info im Schulbuch S. 40–41.",

  "type": "multi",
  "fields": [["gha", "a) Mein ökologischer Fußabdruck laut Rechner (Zahl mit Einheit, z. B. 5,2 gha)"],
             ["vgl", "b) Mein Wert liegt im Vergleich zum Österreich-Schnitt (im Rechner schraffiert) …", ["darüber", "etwa gleich", "darunter"], False],
             ["erden", "c) Österreich hatte sein Naturbudget 2026 schon am 2. April aufgebraucht – das ist der 92. Tag des Jahres. Wie viele Erden bräuchte die Menschheit, wenn alle so lebten wie wir? Rechne 365 : 92."],
             ["welt", "d) Für die ganze Menschheit war es 2026 der 30. Juli, der 211. Tag. Wie viele Erden braucht die Menschheit derzeit?"],
             ["was", "e) Was misst der ökologische Fußabdruck?",
              ["die Fläche, die für unseren Konsum und für das Aufnehmen unseres CO₂ nötig ist", "das Gewicht aller Rohstoffe in einem einzelnen Produkt", "nur die Menge an CO₂ in Kilogramm"]],
             ["ruck", "f) Ein Handy wiegt rund 0,1 kg. Sein ökologischer Rucksack wiegt rund 75 kg. Wievielmal schwerer ist der Rucksack als das Handy?"],
             ["rdef", "g) Was steckt im ökologischen Rucksack?",
              ["alle Rohstoffe, Energie und Wasser über den ganzen Lebensweg eines Produkts", "nur das Verpackungsmaterial", "die Fläche, die das Produkt im Regal braucht"]],
             ["muecke", "h) Die Asiatische Tigermücke ist seit 2022 in allen Bundesländern nachgewiesen. Wie kommen solche Arten zu uns?",
              ["mit dem weltweiten Waren- und Reiseverkehr", "Sie wandern zu Fuß über die Alpen", "Zoos lassen sie absichtlich frei"]],
             ["neo", "i) Eine eingewanderte Tierart wie die Tigermücke heißt …", ["Neozoon", "Neophyt", "heimische Art"]]],
  "chk": {"gha": {"kw": [["Zahl", r"\d"]], "need": 1, "man": True},
          "erden": {"num": 3.97, "unit": "", "tol": 0.08},
          "welt": {"num": 1.73, "unit": "", "tol": 0.035},
          "was": {"sel": "die Fläche, die für unseren Konsum und für das Aufnehmen unseres CO₂ nötig ist"},
          "ruck": {"num": 750, "unit": "", "tol": 15},
          "rdef": {"sel": "alle Rohstoffe, Energie und Wasser über den ganzen Lebensweg eines Produkts"},
          "muecke": {"sel": "mit dem weltweiten Waren- und Reiseverkehr"},
          "neo": {"sel": "Neozoon"}},
  "fb": {"erden": [[0.25, "Umgekehrt: 365 durch 92, nicht 92 durch 365."]],
         "welt": [[0.58, "Umgekehrt: 365 durch 211."]],
         "ruck": [[7.5, "Rechne 75 durch 0,1 – durch eine Zahl kleiner als 1 teilen macht das Ergebnis größer."]],
         "was": {"das Gewicht aller Rohstoffe in einem einzelnen Produkt": "Das ist der ökologische Rucksack. Der Fußabdruck rechnet in Fläche.",
                 "nur die Menge an CO₂ in Kilogramm": "Das ist der CO₂-Fußabdruck. Der ökologische Fußabdruck zählt alle Flächen: Acker, Weide, Wald, Fischgründe, Bauland."},
         "rdef": {"nur das Verpackungsmaterial": "Die Verpackung ist nur ein kleiner Teil. Denk an Bergbau, Fabrik, Transport und Strom beim Laden.",
                  "die Fläche, die das Produkt im Regal braucht": "Der Rucksack wird in Kilogramm gemessen, nicht in Fläche."},
         "muecke": {"Sie wandern zu Fuß über die Alpen": "Mücken fliegen nur kurze Strecken. Den weiten Weg schaffen sie als blinde Passagiere.",
                    "Zoos lassen sie absichtlich frei": "Niemand setzt Tigermücken frei. Sie reisen mit Waren und Menschen mit."},
         "neo": {"Neophyt": "Neophyten sind eingewanderte Pflanzen (»phyton« = Pflanze), z. B. das Drüsige Springkraut.",
                 "heimische Art": "Heimisch war sie vor 2012 nicht – erst dann wurde die erste Tigermücke in Österreich gefunden."}},
  "sol": [["Lösung", ["a) persönlicher Wert, z. B. 4–7 gha – wird nicht bewertet, nur dass ein Wert dasteht.",
                      "b) persönlich – keine Wertung.",
                      "c) 365 : 92 ≈ 4,0 – fast vier Erden.",
                      "d) 365 : 211 ≈ 1,7 – die Menschheit braucht derzeit rund 1,7 Erden.",
                      "e) die Fläche (in globalen Hektar), die für Nahrung, Holz, Wohnen, Straßen und das Aufnehmen unseres CO₂ nötig ist.",
                      "f) 75 : 0,1 = 750 – der Rucksack ist rund 750-mal so schwer wie das Handy.",
                      "g) alle Rohstoffe, Energie und Wasser, die ein Produkt von der Mine bis zur Entsorgung braucht (in kg).",
                      "h) mit dem weltweiten Waren- und Reiseverkehr (z. B. in Fracht, in Autos und Lkw).",
                      "i) Neozoon (eingewanderte Tierart). Eine eingewanderte Pflanze heißt Neophyt."]]],
  "tipps": ["Für c) und d): Ein Jahr hat 365 Tage. Reicht das Budget nur bis Tag 92, wie oft passt 92 in 365?",
            "k1",
            "Lies im Buch S. 40 den Abschnitt »Ökologischer Fußabdruck und ökologischer Rucksack« und auf S. 41 »Globalisierung der Ökosysteme« mit den Randbegriffen Neophyt und Neozoon."],
  "tip": ["Der ökologische Fußabdruck", "theorie.html#abdruck"]},

 {"id": "a2", "nr": 3, "title": "Mit der Hand: Drei Abdrücke im Vergleich", "src": "Buch S. 40", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 5, "marke": "SELBSTSTUDIUM",
  "q": "Zeichne auf ein Blatt eine Tabelle: drei Spalten (Fußabdruck · Rucksack · CO₂-Fußabdruck), drei Zeilen (Was wird gemessen? · Einheit · ein Beispiel aus deinem Alltag). Lade ein Foto hoch.",
  "hint": "Datum oben aufs Blatt, flach fotografieren, gutes Licht, kein Name, keine Gesichter. Das Blatt kommt danach in deine Mappe. Wo steht's? Theorie-Teil 1 und 2, Buch S. 40.",

  "type": "sketch",
  "fields": [["unterschied", "Unter das Foto: Was ist der wichtigste Unterschied zwischen Fußabdruck und Rucksack? (1 Satz)"]],
  "chk": {"unterschied": {"kw": [["Fläche", r"flaech|fläch|hektar|gha|boden|land"], ["Gewicht / Material", r"kilo|kg|gewicht|material|rohstoff|produkt|schwer"]], "need": 1, "man": True}},
  "sol": [["Musterlösung (Tabelle)", ["Fußabdruck: Fläche für Konsum und CO₂-Aufnahme · globale Hektar (gha) · z. B. Fleisch braucht viel Weide- und Ackerfläche.",
                                      "Rucksack: alle Rohstoffe, Energie und Wasser eines Produkts über den Lebensweg · Kilogramm · z. B. Handy rund 75 kg.",
                                      "CO₂-Fußabdruck: Treibhausgase, umgerechnet in CO₂ · kg oder t CO₂-Äquivalent · z. B. Autofahrt zum Training.",
                                      "Unterschied: Der Fußabdruck misst Fläche (für einen Menschen oder ein Land), der Rucksack misst Material in kg (für ein Produkt)."]]],
  "tipps": ["Fußabdruck – wie viel Platz auf der Erde? Rucksack – wie viel muss man ausgraben und bewegen? CO₂ – wie viel Abgas in die Luft?",
            "k2",
            "Lies im Buch S. 40 die zwei Absätze über Fußabdruck und Rucksack noch einmal und markiere jeweils das Wort, das sagt, was gemessen wird."],
  "tip": ["Rucksack und CO₂-Fußabdruck", "theorie.html#rucksack"]},

 # --------------------------------------------------------------- Stunde 2
 {"id": "a3", "nr": 4, "title": "Was kostet eine KI-Frage? Rechnen und prüfen", "src": "Buch S. 40, 97 · ORF", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 11, "marke": "SELBSTSTUDIUM",
  "sim": ["ki", "rz"],
  "q": "Google sagt: Eine Textfrage an Gemini braucht 0,24 Wattstunden (Wh). Rechne a) bis d). Prüf dann bei e) bis g) die Quelle.",
  "hint": "OpenAI nennt 0,34 Wh für ChatGPT. Einheit dazuschreiben, auf eine Kommastelle runden. 1 kWh = 1000 Wh, 1 TWh = 1 Milliarde kWh. Prozent: Teil : Ganzes · 100. Info: Theorie-Teil 4 und 5, Buch S. 97.",

  "type": "multi",
  "fields": [["tag", "a) Eure Klasse (25 Kadetten) stellt jeder 20 KI-Fragen pro Tag. Wie viel Strom ist das pro Tag (Gemini-Wert, in Wh)?"],
             ["jahr", "b) Wie viel ist das in einem Jahr (365 Tage)? Gib das Ergebnis in kWh an."],
             ["hh", "c) Kronstorf, Stufe 1: 1,31 TWh = 1 310 000 000 kWh im Jahr, laut ORF so viel wie 375 000 Haushalte. Wie viele kWh braucht ein Haushalt damit pro Jahr?"],
             ["ooe", "d) Oberösterreich brauchte 2024 rund 14 TWh Strom. Wie viel Prozent davon wären die 1,31 TWh?"],
             ["wer", "e) Wer hat die 0,24 Wh berechnet?", ["Google selbst – eine unabhängige Prüfung wird nicht erwähnt", "eine unabhängige Universität", "die EU-Kommission"]],
             ["fehlt", "f) Was ist in den 0,24 Wh laut ORF NICHT enthalten?", ["das Training der KI-Modelle vorher", "der Strom für die Server bei deiner Frage", "die Kühlung im Rechenzentrum"]],
             ["mehr", "g) Jede einzelne Anfrage wird sparsamer. Warum steigt der Strombedarf der Rechenzentren trotzdem? (1–2 Sätze)"]],
  "chk": {"tag": {"num": 120, "unit": "Wh", "tol": 2.4},
          "jahr": {"num": 43.8, "unit": "kWh", "tol": 0.9},
          "hh": {"num": 3493, "unit": "kWh", "tol": 70},
          "ooe": {"num": 9.36, "unit": "%", "tol": 0.19},
          "wer": {"sel": "Google selbst – eine unabhängige Prüfung wird nicht erwähnt"},
          "fehlt": {"sel": "das Training der KI-Modelle vorher"},
          "mehr": {"kw": [["mehr Nutzung", r"mehr|viel|immer|nutz|anfrag|menschen|user|leute|masse|oefter|öfter|staendig|ständig|bild|video"]], "need": 1, "man": True}},
  "fb": {"tag": [[4.8, "Du hast nur eine Person gerechnet: 25 Kadetten · 20 Fragen · 0,24 Wh."], [170, "Das ist der ChatGPT-Wert (0,34 Wh). Gefragt ist der Gemini-Wert 0,24 Wh."]],
         "jahr": [[43800, "Das sind Wattstunden. Für kWh noch durch 1000 teilen."], [0.12, "Du hast nur einen Tag umgerechnet. Ein Jahr hat 365 Tage: 120 Wh · 365."]],
         "hh": [[0.000286, "Umgekehrt: kWh durch Haushalte, also 1 310 000 000 : 375 000."]],
         "ooe": [[0.0936, "Das ist der Anteil als Kommazahl. Für Prozent noch mal 100."], [10.7, "Umgekehrt: 1,31 durch 14, nicht 14 durch 1,31."]],
         "wer": {"eine unabhängige Universität": "Lies genau: Die Zahl stammt aus Berechnungen des Konzerns selbst.",
                 "die EU-Kommission": "Die EU hat diese Zahl nicht berechnet. Wer hat ein Interesse daran, dass KI sparsam wirkt?"},
         "fehlt": {"der Strom für die Server bei deiner Frage": "Den rechnet Google mit – genau das ist ja die Zahl pro Frage.",
                   "die Kühlung im Rechenzentrum": "Google rechnet auch Kühlung und Leerlauf mit ein. Was passiert, bevor du die erste Frage stellst?"}},
  "sol": [["Lösung", ["a) 25 · 20 · 0,24 Wh = 120 Wh pro Tag.",
                      "b) 120 Wh · 365 = 43 800 Wh = 43,8 kWh im Jahr – etwa so viel, wie ein Haushalt in rund 4–5 Tagen braucht.",
                      "c) 1 310 000 000 kWh : 375 000 ≈ 3 493 kWh – rund 3 500 kWh pro Haushalt und Jahr.",
                      "d) 1,31 : 14 · 100 ≈ 9,4 % des Stroms von ganz Oberösterreich (mit Stufe 2 laut ORF etwa ein Drittel mehr).",
                      "e) Google selbst – Herstellerangabe, nicht unabhängig geprüft.",
                      "f) das Training der Modelle; außerdem fehlt das indirekte Wasser (z. B. für die Stromerzeugung).",
                      "g) Immer mehr Menschen fragen immer öfter, auch Bilder und Videos – die Masse frisst die Ersparnis auf (Rebound-Effekt)."]]],
  "tipps": ["a) Erst Fragen pro Tag für die ganze Klasse: 25 · 20. Dann mal 0,24 Wh. b) mal 365, dann durch 1000.",
            "k4",
            "Lies im Buch S. 97 »Bewusster Umgang mit IT« und auf S. 40 den Absatz über den ökologischen Rucksack – auch Daten haben einen."],
  "tip": ["Wo wohnt die KI?", "theorie.html#ki"]},

 {"id": "a4", "nr": 5, "title": "GRUPPENARBEIT: Gemeinderat Kronstorf", "src": "ORF 17.07.2026 · Buch S. 40", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 10, "marke": "GRUPPENARBEIT",
  "img": "img/rechenzentrum.svg",
  "q": "Sondersitzung im Gemeinderat: Braucht ein großes Rechenzentrum eine Umweltverträglichkeitsprüfung (UVP)? Jeder in der Gruppe übernimmt eine Rolle. Besprecht b) bis d) (ca. 6 min), e) und f) trägt jeder selbst ein.",
  "hint": "Danach fragt Prof. HOLZER einzelne Rollen. Ohne KI. Die Zeichnung zeigt den Weg der Energie: Strom rein, rechnen, Wärme, Kühlwasser in den Fluss. Info: Theorie-Teil 5.",

  "type": "multi",
  "fields": [["rolle", "a) Meine Rolle", ["Google-Sprecher", "Bürgerinitiative", "Fischereiverband", "Wirtschaftslandesrat", "Umwelt-NGO", "Offizier Cyberabwehr"], False],
             ["uvp", "b) Warum war in Kronstorf keine UVP nötig?",
              ["Das Projekt lag unter den Schwellenwerten – Rechenzentren sind keine eigene UVP-Kategorie", "Google ist von österreichischen Umweltgesetzen ausgenommen", "Die Gemeinde hat die Prüfung verboten"]],
             ["waerme", "c) Wohin geht fast der ganze Strom, den ein Rechenzentrum verbraucht, am Ende?",
              ["Er wird zu Wärme, die abgeführt werden muss", "Er wird in den Daten gespeichert", "Er fließt zurück ins Netz"]],
             ["abwaerme", "d) Was wäre eine sinnvolle Bedingung für den Bau?",
              ["Abwärme nutzen, z. B. für Fernwärme, und Wasserwerte laufend messen", "mehr Kühlwasser in den Fluss leiten", "die Server nur nachts laufen lassen"]],
             ["urteil", "e) Eure Gruppe in zwei Sätzen: Soll es eine UVP-Pflicht für große Rechenzentren geben? Mit einem Grund."],
             ["stimme", "f) Wie stimmst du persönlich ab?", ["ja, UVP-Pflicht für große Rechenzentren", "nein, bestehende Gesetze reichen", "ja, aber nur ab einer bestimmten Größe"], False]],
  "chk": {"uvp": {"sel": "Das Projekt lag unter den Schwellenwerten – Rechenzentren sind keine eigene UVP-Kategorie"},
          "waerme": {"sel": "Er wird zu Wärme, die abgeführt werden muss"},
          "abwaerme": {"sel": "Abwärme nutzen, z. B. für Fernwärme, und Wasserwerte laufend messen"},
          "urteil": {"kw": [["Entscheidung", r"\bja\b|\bnein\b|sollte|soll|braucht|pflicht|nicht noetig|nicht nötig"],
                            ["Grund", r"strom|wasser|enns|fisch|flaech|fläch|hektar|job|arbeit|investi|wirtschaft|umwelt|transparen|kontroll|daten|sicher|waerme|wärme|natur"]], "need": 2, "man": True}},
  "fb": {"uvp": {"Google ist von österreichischen Umweltgesetzen ausgenommen": "Google muss sich an alle Gesetze halten. Das Problem: Für Rechenzentren gibt es keine eigene UVP-Schwelle.",
                 "Die Gemeinde hat die Prüfung verboten": "Eine Gemeinde kann eine UVP weder verbieten noch verlangen – das regelt das UVP-Gesetz des Bundes."},
         "waerme": {"Er wird in den Daten gespeichert": "Daten speichern keine Energie. Fass einmal ein Ladegerät an, das lange gearbeitet hat.",
                    "Er fließt zurück ins Netz": "Verbrauchter Strom kommt nicht zurück. Er wird in den Chips zu Wärme."},
         "abwaerme": {"mehr Kühlwasser in den Fluss leiten": "Mehr warmes Wasser belastet die Enns noch stärker.",
                      "die Server nur nachts laufen lassen": "Die Dienste laufen rund um die Uhr – du willst auch am Vormittag fragen."}},
  "sol": [["Lösung", ["a) Rolle – keine Wertung.",
                      "b) Das Projekt (ca. 50 ha) lag unter den Schwellenwerten; Rechenzentren sind im UVP-Gesetz keine eigene Kategorie. Umweltorganisationen sprechen von einer Gesetzeslücke.",
                      "c) Fast der ganze Strom wird in den Chips zu Wärme – darum braucht es Kühlung (in Kronstorf bis zu 5,8 Millionen Liter warmes Wasser pro Tag in die Enns, höchstens 30 °C).",
                      "d) Abwärme nutzen (Fernwärme) und die Wasserwerte laufend messen und veröffentlichen.",
                      "e) z. B. »Ja – ein Projekt, das so viel Strom wie 375 000 Haushalte braucht und warmes Wasser in die Enns leitet, sollte vorher geprüft werden.« Auch »Nein« ist richtig, wenn es begründet ist (z. B. Wasserrecht und Bauordnung prüfen schon).",
                      "f) persönliche Meinung – keine Wertung."]]],
  "tipps": ["Was passiert mit der Energie, nachdem ein Chip gerechnet hat? Und wer prüft heute, ob die Enns das verträgt?",
            "k5",
            "Lies im Buch S. 40 den Absatz über den ökologischen Rucksack und im Theorie-Teil 5 den Fall Kronstorf."],
  "tip": ["Der Fall Kronstorf", "theorie.html#kronstorf"]},

 # --------------------------------------------------------------- Stunde 3
 {"id": "a5", "nr": 6, "title": "Klima und Handel: COP31 und Mercosur", "src": "Buch S. 40–41, 71, 73–75", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 8, "marke": "SELBSTSTUDIUM",
  "q": "Zwei Nachrichten aus diesem Herbst: Die Klimakonferenz COP31 ist am 22. November gescheitert, und der Handelsteil des Mercosur-Abkommens gilt seit Mai. Beantworte a) bis h).",
  "hint": "h) ist deine Meinung. Mercosur = Argentinien, Brasilien, Paraguay, Uruguay. COP = die jährliche Weltklimakonferenz der UNO. Info: Theorie-Teile 6–8, Buch S. 40–41 und 73–75.",

  "type": "multi",
  "fields": [["cop", "a) Was ist bei der COP31 in Antalya passiert?",
              ["Die Staaten einigten sich nicht auf ein gemeinsames Abschlusspapier", "Alle Staaten beschlossen den Ausstieg aus Kohle, Öl und Gas bis 2040", "Die Konferenz wurde abgesagt"]],
             ["eu", "b) Warum legte die EU im Schlussplenum Widerspruch ein?",
              ["Im Entwurf wurden Kohle, Öl und Gas nicht einmal ausdrücklich genannt", "Die EU wollte weniger für Klimaschutz zahlen", "Die EU war gegen die Türkei als Gastgeber"]],
             ["paris", "c) Was haben die Staaten 2015 in Paris vereinbart?",
              ["die Erwärmung auf deutlich unter 2 °C, möglichst 1,5 °C zu begrenzen", "bis 2020 alle Kohlekraftwerke zu schließen", "jedes Jahr 10 % weniger Auto zu fahren"]],
             ["treib", "d) Was machen Treibhausgase wie CO₂ in der Atmosphäre?",
              ["Sie halten einen Teil der Wärmestrahlung der Erde zurück – die Erde kühlt schlechter ab", "Sie lassen kein Sonnenlicht mehr zur Erde durch", "Sie machen ein Loch in die Ozonschicht"]],
             ["seit", "e) Seit wann gilt der Handelsteil des EU-Mercosur-Abkommens vorläufig?", ["seit 1. Mai 2026", "seit 2015", "noch gar nicht"]],
             ["at", "f) Wie stimmte Österreich im Rat der EU ab?", ["dagegen", "dafür", "Österreich war nicht dabei"]],
             ["rind", "g) Die Mercosur-Staaten dürfen 99 000 t Rindfleisch zu 7,5 % Zoll in die EU liefern. Die EU isst rund 8 000 000 t pro Jahr. Wie viel Prozent sind die 99 000 t?"],
             ["meinung", "h) Ist Mercosur gut oder schlecht fürs Klima? Ein Argument dafür, eines dagegen, dann dein Urteil (2–3 Sätze)."]],
  "chk": {"cop": {"sel": "Die Staaten einigten sich nicht auf ein gemeinsames Abschlusspapier"},
          "eu": {"sel": "Im Entwurf wurden Kohle, Öl und Gas nicht einmal ausdrücklich genannt"},
          "paris": {"sel": "die Erwärmung auf deutlich unter 2 °C, möglichst 1,5 °C zu begrenzen"},
          "treib": {"sel": "Sie halten einen Teil der Wärmestrahlung der Erde zurück – die Erde kühlt schlechter ab"},
          "seit": {"sel": "seit 1. Mai 2026"},
          "at": {"sel": "dagegen"},
          "rind": {"num": 1.24, "unit": "%", "tol": 0.05},
          "meinung": {"kw": [["Pro", r"export|zoll|billig|preis|handel|wirtschaft|job|maschin|auto|industri|markt"],
                             ["Contra", r"regenwald|wald|abholz|rodung|soja|transport|schiff|co2|co₂|klima|bauer|landwirt|rind|fleisch"]], "need": 2, "man": True}},
  "fb": {"cop": {"Alle Staaten beschlossen den Ausstieg aus Kohle, Öl und Gas bis 2040": "Genau darüber gab es Streit – beschlossen wurde nichts davon.",
                 "Die Konferenz wurde abgesagt": "Sie fand statt, zwei Wochen lang, und dauerte sogar länger als geplant."},
         "eu": {"Die EU wollte weniger für Klimaschutz zahlen": "Es ging um den Text zu den fossilen Energien. Welche drei Wörter fehlten?",
                "Die EU war gegen die Türkei als Gastgeber": "Der Gastgeber war seit Langem fix. Der Streit ging um den Inhalt."},
         "paris": {"bis 2020 alle Kohlekraftwerke zu schließen": "Ein festes Datum für Kohle steht nicht im Pariser Abkommen. Es nennt ein Temperaturziel.",
                   "jedes Jahr 10 % weniger Auto zu fahren": "Das Abkommen schreibt keine Maßnahmen für Einzelne vor, sondern ein Ziel für die Erwärmung."},
         "treib": {"Sie lassen kein Sonnenlicht mehr zur Erde durch": "Sonnenlicht kommt durch. Was passiert mit der Wärme, die der Boden abstrahlt?",
                   "Sie machen ein Loch in die Ozonschicht": "Das Ozonloch ist ein anderes Problem (FCKW). Hier geht es um Wärme."},
         "seit": {"seit 2015": "2015 war Paris. Mercosur wurde im Jänner 2026 unterschrieben.", "noch gar nicht": "Der Handelsteil wird seit Mai vorläufig angewandt."},
         "at": {"dafür": "Österreich hat bis zuletzt dagegen gestimmt – wurde aber überstimmt.", "Österreich war nicht dabei": "Im Rat der EU stimmen alle Mitgliedstaaten ab."},
         "rind": [[0.0124, "Das ist der Anteil als Kommazahl. Für Prozent noch mal 100."], [80.8, "Umgekehrt: 99 000 durch 8 000 000."]]},
  "sol": [["Lösung", ["a) Keine Einigung: Am 22.11.2026 scheiterte das gemeinsame Abschlusspapier – ein Beschluss braucht die Zustimmung von fast 200 Staaten.",
                      "b) Der Entwurf nannte Kohle, Öl und Gas nicht ausdrücklich; er verwies nur allgemein auf den Beschluss von Dubai 2023.",
                      "c) Erwärmung deutlich unter 2 °C, möglichst 1,5 °C (Buch S. 74).",
                      "d) Sie nehmen einen Teil der Wärmestrahlung des Bodens auf und strahlen ihn wieder ab – auch zurück zur Erde (Buch S. 71).",
                      "e) seit 1. Mai 2026 (unterzeichnet am 17. Jänner 2026).",
                      "f) dagegen – mit Frankreich, Polen, Ungarn und Irland; die Mehrheit war dafür.",
                      "g) 99 000 : 8 000 000 · 100 ≈ 1,24 % – etwas mehr als 1 %.",
                      "h) z. B. dafür: weniger Zölle, mehr Exporte von Maschinen und Autos, mehr Handel und Zusammenarbeit beim Klima. Dagegen: mehr Rindfleisch und Soja aus Südamerika können Druck auf den Regenwald machen, lange Transportwege, Druck auf heimische Bauern. Urteil begründet – beide Seiten sind möglich."]]],
  "tipps": ["Alles aus a) bis f) steht in den Theorie-Teilen 6 bis 8. Bei g): Teil durch Ganzes, mal 100.",
            "k8",
            "Lies im Buch S. 73–74 »Klimakonferenzen und Klimapolitik« und S. 40–41 »Internationale Abkommen«."],
  "tip": ["Handel und Klima", "theorie.html#handel"]},

 {"id": "a6", "nr": 7, "title": "Mit der Hand: Mindmap »Ein Planet reicht nicht«", "src": "Buch S. 39–44, 71–75", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 4, "marke": "SELBSTSTUDIUM",
  "q": "Mindmap auf ein leeres Blatt: In die Mitte »Ein Planet reicht nicht«, dazu vier Äste: Abdruck · KI und Rechenzentren · Klimakonferenzen · Handel. An jeden Ast zwei Stichwörter und eine Zahl. Lade ein Foto hoch.",
  "hint": "Die Zahlen findest du in den Aufgaben 2, 4 und 6. Datum oben aufs Blatt, kein Name, keine Gesichter. Das Blatt kommt in deine Mappe.",

  "type": "sketch",
  "fields": [["zahl", "Unter das Foto: Welche Zahl aus der Einheit merkst du dir – und warum? (1 Satz)"]],
  "chk": {"zahl": {"kw": [["Zahl", r"\d"]], "need": 1, "man": True}},
  "sol": [["Muster", ["Abdruck: Fläche, Rucksack · 4 Erden (Österreich). KI: Strom, Kühlwasser · 375 000 Haushalte (Kronstorf). Klimakonferenzen: Paris, COP31 gescheitert · 1,5 °C. Handel: Zölle, Regenwald · 99 000 t Rindfleisch.",
                      "Bewertet wird: vier Äste vollständig, Zahlen stimmen, lesbar."]]],
  "tipps": ["Schau in deine Antworten bei Aufgabe 2, 4 und 6 – dort stehen die Zahlen.", "k9", "Buch S. 39 »Meine Ziele« und S. 76 »Ziele erreicht?« helfen beim Auswählen."],
  "tip": ["Alles auf einen Blick", "theorie.html#kurz"]},

 # --------------------------------------------------------------- Zusatz
 {"id": "z1", "nr": 8, "title": "Lesen und prüfen: Wer hat den CO₂-Fußabdruck erfunden?", "src": "WBUR 19.12.2023 · Buch S. 40", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "link": ["Sendung mit Abschrift öffnen (Englisch)", "https://www.wbur.org/onpoint/2023/12/19/how-big-oil-helped-push-the-idea-of-a-carbon-footprint", "WBUR On Point (Boston), 19.12.2023 · Gast: Geoffrey Supran, Universität Miami · auf Englisch – Teil 2 der Theorie fasst es auf Deutsch zusammen"],
  "q": "Den Begriff »CO₂-Fußabdruck« hat ab 2004 eine Werbekampagne des Ölkonzerns BP bekannt gemacht. Lies Theorie-Teil 2 (Kasten »Wer hat's erfunden?«) und beantworte a) bis c).",
  "hint": "Quellenkritik: Wer sagt das – und wer hat ein Interesse daran? Ohne KI. Quelle: Radiosendung WBUR »On Point« (USA), 19.12.2023, mit dem Forscher Geoffrey Supran.",

  "type": "multi",
  "fields": [["ziel", "a) Was hatte BP davon, dass Menschen über ihren eigenen Fußabdruck nachdenken?",
              ["Der Blick ging weg vom Konzern hin zu den Einzelnen", "BP wollte weniger Öl verkaufen", "BP bekam Geld für jeden Rechner"]],
             ["beweis", "b) Was räumt der Forscher Geoffrey Supran selbst ein?",
              ["Interne Strategiepapiere, die den Plan beweisen, wurden bisher nicht gefunden", "Die Kampagne hat es nie gegeben", "Persönliches Handeln ist sinnlos"]],
             ["sinn", "c) Ist es trotzdem sinnvoll, den eigenen Fußabdruck zu senken? Begründe in 1–2 Sätzen."]],
  "chk": {"ziel": {"sel": "Der Blick ging weg vom Konzern hin zu den Einzelnen"},
          "beweis": {"sel": "Interne Strategiepapiere, die den Plan beweisen, wurden bisher nicht gefunden"},
          "sinn": {"kw": [["Begründung", r"ja|nein|sinnvoll|hilft|beitrag|politik|system|gesetz|beides|einzeln|gemeinsam|vorbild|konzern"]], "need": 1, "man": True}},
  "fb": {"ziel": {"BP wollte weniger Öl verkaufen": "Ein Ölkonzern verdient am Öl. Wem wurde die Verantwortung zugeschoben?", "BP bekam Geld für jeden Rechner": "Der Rechner war gratis. Es ging um das Image."},
         "beweis": {"Die Kampagne hat es nie gegeben": "Die Werbung und der Rechner sind gut belegt. Unsicher ist nur die Absicht dahinter.", "Persönliches Handeln ist sinnlos": "Das sagt er gerade nicht: Er rät, alles Mögliche selbst zu tun – und zusätzlich Politik und Konzerne in die Pflicht zu nehmen."}},
  "sol": [["Lösung", ["a) Die Verantwortung wanderte vom Konzern zu den Einzelnen (»Was tust DU?«) – BP nannte sich damals »Beyond Petroleum«.",
                      "b) Supran sagt selbst: Ein internes Papier, das den Plan beweist (»smoking gun«), fehlt bisher. Belegt sind Werbung und Rechner.",
                      "c) z. B. »Ja – jeder Beitrag zählt und zeigt, was möglich ist. Aber große Hebel liegen bei Politik, Energieversorgern und Konzernen; beides braucht es.«"]]],
  "tipps": [], "tip": ["Rucksack und CO₂-Fußabdruck", "theorie.html#rucksack"], "zst": 1},

 {"id": "z2", "nr": 9, "title": "KI-Check: Kennt die KI ihren eigenen Stromverbrauch?", "src": "Buch S. 97 · ORF", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Frag eine KI: »Wie viel Strom brauchst du für eine Antwort? Nenne eine Quelle.« Vergleiche mit Theorie-Teil 4. Schreib dann eine bessere Frage.",
  "hint": "Achte darauf: Nennt die KI eine Zahl? Eine Quelle mit Datum? Sagt sie, was nicht eingerechnet ist?",

  "type": "multi",
  "fields": [["zahl", "a) Welche Zahl hat die KI genannt (mit Einheit)? Welche KI war es?"],
             ["quelle", "b) Hat sie eine überprüfbare Quelle genannt?", ["ja, mit Herausgeber und Datum", "ja, aber ohne Datum oder Link", "nein"], False],
             ["passt", "c) Passt die Zahl zu den Herstellerangaben aus Teil 4 (0,24 bzw. 0,34 Wh)?", ["ja, etwa gleich", "nein, deutlich höher", "nein, deutlich niedriger"], False],
             ["prompt", "d) Deine bessere Frage an die KI (1–2 Sätze)"]],
  "chk": {"zahl": {"kw": [["Zahl", r"\d"]], "need": 1, "man": True},
          "prompt": {"kw": [["genauer", r"quelle|datum|training|wasser|wh|wattstunde|unabhaengig|unabhängig|vergleich|link|studie"]], "need": 1, "man": True}},
  "sol": [["Hinweise", ["a)–c) Antworten verschieden. Oft nennen KIs ältere Schätzungen (etwa 3 Wh) oder keine Quelle.",
                        "d) z. B. »Nenne die neueste Herstellerangabe in Wattstunden pro Textanfrage mit Quelle und Datum und sag dazu, ob Training und Wasser eingerechnet sind.«"]]],
  "tipps": [], "tip": ["Wo wohnt die KI?", "theorie.html#ki"], "zst": 2},

 {"id": "z3", "nr": 10, "title": "Simulation: Treibhauseffekt selbst einstellen", "src": "PhET · Buch S. 71", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "link": ["Simulation »Treibhauseffekt« öffnen", "https://phet.colorado.edu/de/simulations/greenhouse-effect", "PhET, University of Colorado Boulder · Deutsch · CC BY-NC 4.0 · läuft im Browser"],
  "q": "Öffne die Simulation (Knopf oben). Stell die Menge der Treibhausgase ein und beobachte die Temperatur. Füge dann Wolken hinzu.",
  "hint": "Warte nach jeder Änderung ein paar Sekunden – die Temperatur pendelt sich erst ein.",

  "type": "multi",
  "fields": [["mehr", "a) Du erhöhst die Konzentration der Treibhausgase. Die Temperatur …", ["steigt", "sinkt", "bleibt gleich"]],
             ["null", "b) Was passiert ganz ohne Treibhausgase?", ["Es wird viel kälter – die Erde wäre kaum bewohnbar", "Es wird wärmer", "Nichts ändert sich"]],
             ["beob", "c) Was hast du bei den Wolken beobachtet? (1–2 Sätze)"]],
  "chk": {"mehr": {"sel": "steigt"}, "null": {"sel": "Es wird viel kälter – die Erde wäre kaum bewohnbar"},
          "beob": {"kw": [["Beobachtung", r"\w{3,}"]], "need": 1, "man": True}},
  "fb": {"mehr": {"sinkt": "Schau noch einmal: Mehr Gas hält mehr Wärme zurück.", "bleibt gleich": "Warte ein paar Sekunden nach dem Verstellen."},
         "null": {"Es wird wärmer": "Ohne Gase entweicht die Wärme fast ganz ins All.", "Nichts ändert sich": "Stell den Regler ganz nach links und warte."}},
  "sol": [["Lösung", ["a) steigt.", "b) Es wird viel kälter: Ohne natürlichen Treibhauseffekt läge die Durchschnittstemperatur weit unter 0 °C (Buch S. 71: Leben wäre kaum möglich).",
                      "c) Wolken werfen Sonnenlicht zurück (kühlen) und halten Wärme zurück (wärmen) – die Simulation zeigt beides."]]],
  "tipps": [], "tip": ["Der Treibhauseffekt", "theorie.html#treibhaus"], "zst": 3},

 {"id": "z4", "nr": 11, "title": "Kreativ: Ein Plakat für den nächsten Klimagipfel", "src": "Buch-Aufgabe S. 76/8", "own": False, "tag": "Zusatz", "h": 0, "zeit": 15,
  "q": "Die COP31 ist gescheitert. Entwirf mit der Hand ein Plakat (A4 oder A3), das Menschen in deinem Alter Mut zum Klimaschutz macht. Foto in LMS hochladen.",
  "hint": "Auf das Plakat: ein Slogan, ein Bild, eine Zahl aus der Einheit, ein Tipp für morgen. Allein oder zu zweit. Keine fremden Logos oder Fotos. Buch-Aufgabe S. 76/8.",

  "type": "multi",
  "fields": [["info", "Slogan · Zahl · Tipp · hochgeladen in LMS am …"]],
  "chk": {"info": {"kw": [["Angaben", r"\w{3,}"]], "need": 1, "man": True}},
  "sol": [["Bewertungsraster (10 Punkte)", ["Slogan klar und eigen 2 · Zahl stimmt und Quelle genannt 2 · Tipp umsetzbar 2 · Gestaltung lesbar 2 · Abgabe eingehalten 2."]]],
  "tipps": [], "tip": ["Klimakonferenzen", "theorie.html#konferenzen"], "zst": 3},
]

# ---------------------------------------------------------------- Kontrollen
for _t in T:
    if _t["tag"] == "Zusatz": assert _t.get("zst") in (1, 2, 3), _t["id"]
assert [t["nr"] for t in T] == list(range(1, 12))
PFLICHT = [t["nr"] for t in T if t["tag"] != "Zusatz" and not t.get("vorhersage")]
assert PFLICHT == [2, 3, 4, 5, 6, 7], PFLICHT
BESPRECHEN = [2, 4, 5, 6]
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True
for _t in T:
    for _k in (_t["chk"] or {}):
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
            assert len(set(_f[2])) == len(_f[2]), (_t["id"], _f[0], "doppelte Option")
    for _k, _m in _t.get("fb", {}).items():
        if isinstance(_m, list):
            _c = _t["chk"][_k]; assert "num" in _c, (_t["id"], _k)
            for _w, _txt in _m: assert abs(_w - _c["num"]) > (_c["tol"] or 0) * 3, (_t["id"], _k, _w, "typischer Fehlwert zu nah an der Lösung")
            continue
        _opt = [f[2] for f in _t["fields"] if f[0] == _k][0]
        for _o in _m: assert _o in _opt, (_t["id"], _k, _o)
        assert _t["chk"][_k].get("sel") not in _m, (_t["id"], _k)
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz] + [f[1] for f in _t["fields"]]:
        assert "√" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
    assert len(_t.get("tipps", [])) in (0, 3), _t["id"]

# Rechenkontrolle (vom Aufgabentext aus)
assert abs(365 / OS_AT_TAG - 3.967) < 0.001 and abs(365 / OS_WELT_TAG - 1.730) < 0.001
assert 31 + 28 + 31 + 2 == OS_AT_TAG and 31 + 28 + 31 + 30 + 31 + 30 + 30 == OS_WELT_TAG
assert abs(RUCKSACK_KG / HANDY_KG - 750) < 1e-9
assert abs(25 * 20 * GEMINI_WH - 120) < 1e-9 and abs(120 * 365 / 1000 - 43.8) < 1e-9
assert abs(KR_TWH * 1e9 / KR_HH - 3493.3) < 0.1 and abs(KR_TWH / OOE_TWH * 100 - 9.357) < 0.001
assert abs(KR_MW * 8760 / 1e6 - 1.314) < 0.001          # 150 MW das ganze Jahr = 1,31 TWh – passt zur ORF-Zahl
assert abs(RIND_T / EU_RIND_T * 100 - 1.2375) < 1e-9
assert abs(43.8 / 3493 * 365 - 4.58) < 0.01             # »etwa so viel wie ein Haushalt in rund 4–5 Tagen«

GRP = {1: STUNDENNAME[1] + " (Buch S. 39–41)",
       2: STUNDENNAME[2] + " (Buch S. 40, 97)",
       3: STUNDENNAME[3] + " (Buch S. 40–41, 71–75)",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)",
       "z1": "Zusatz zu Stunde 1 · nur wenn du früher fertig bist", "z2": "Zusatz zu Stunde 2 · nur wenn du früher fertig bist",
       "z3": "Zusatz zu Stunde 3 · nur wenn du früher fertig bist"}

LERNZIELE = ["**ökologischen Fußabdruck, ökologischen Rucksack und CO₂-Fußabdruck** unterscheiden und ihre Einheiten nennen",
             "aus dem **Overshoot Day** ausrechnen, wie viele Erden wir bräuchten, und meinen Fußabdruck mit dem Österreich-Schnitt vergleichen",
             "erklären, warum **KI Strom und Wasser** braucht, und den Strombedarf eines **Rechenzentrums** mit Haushalten vergleichen",
             "**Firmenangaben** prüfen: Wer sagt das, was fehlt, wer hat ein Interesse?",
             "Vor- und Nachteile von **Klimakonferenzen** und **Handelsabkommen** wie Mercosur für Klima, Wirtschaft und Sicherheit abwägen und begründet Stellung nehmen"]

WICHTIGSTE = ["Der **ökologische Fußabdruck** misst Fläche (globale Hektar), der **Rucksack** das Material eines Produkts (kg), der **CO₂-Fußabdruck** die Treibhausgase (CO₂-Äquivalent).",
              "Würden alle wie wir in Österreich leben, bräuchte die Menschheit fast **vier Erden** – Österreichs **Overshoot Day** 2026 war am 2. April.",
              "**KI** läuft in **Rechenzentren**: Strom wird zu Wärme, die mit Wasser oder Luft abgeführt wird. Kronstorf Stufe 1 braucht so viel Strom wie rund **375 000 Haushalte**.",
              "Klimaschutz braucht alle Staaten: Paris 2015 setzte das Ziel **1,5 bis 2 °C** – bei der **COP31** 2026 scheiterte das Abschlusspapier am Streit um Kohle, Öl und Gas.",
              "Handelsabkommen wie **Mercosur** senken Zölle und bringen Exporte – bergen aber Risiken für **Regenwald, Klima und heimische Bauern**. Gute Urteile wägen beides ab."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Globalisierung", "weltweite Verflechtung von Wirtschaft, Handel, Verkehr und Kommunikation"],
                ["ökologischer Fußabdruck", "Fläche, die nötig ist, um alles herzustellen, was ein Mensch oder ein Land verbraucht, und um sein CO₂ aufzunehmen"],
                ["globaler Hektar (gha)", "Flächeneinheit mit weltweit durchschnittlicher Fruchtbarkeit; macht Länder vergleichbar"],
                ["Biokapazität", "Fläche, die die Erde (oder ein Land) jedes Jahr nachwachsen lässt"],
                ["Overshoot Day (Erdüberlastungstag)", "Tag, an dem das Naturbudget eines Jahres verbraucht ist; danach leben wir »auf Pump«"],
                ["ökologischer Rucksack", "alle Rohstoffe, Energie und Wasser, die ein Produkt über seinen ganzen Lebensweg braucht (in kg)"],
                ["CO₂-Fußabdruck", "Menge an Treibhausgasen, die ein Mensch, Produkt oder eine Firma verursacht, umgerechnet in CO₂ (CO₂-Äquivalent)"],
                ["Neophyt / Neozoon", "eingewanderte Pflanze bzw. eingewandertes Tier, z. B. Drüsiges Springkraut bzw. Tigermücke"],
                ["Rechenzentrum", "Gebäude mit vielen Servern, die rund um die Uhr rechnen und speichern – auch für KI"],
                ["Abwärme", "Wärme, die beim Rechnen in den Chips entsteht und abgeführt werden muss; kann z. B. Häuser heizen"],
                ["UVP (Umweltverträglichkeitsprüfung)", "Prüfverfahren vor großen Bauprojekten: Was bedeutet das Projekt für Umwelt und Menschen?"],
                ["Rebound-Effekt", "Effizienz spart Energie, aber weil man mehr nutzt, steigt der Verbrauch insgesamt trotzdem"],
                ["Treibhauseffekt", "Gase in der Atmosphäre halten einen Teil der Wärmestrahlung der Erde zurück; natürlich lebenswichtig, durch den Menschen verstärkt"],
                ["COP", "Conference of the Parties – die jährliche Weltklimakonferenz der UNO"],
                ["Pariser Abkommen", "Vertrag von 2015: Erwärmung deutlich unter 2 °C, möglichst 1,5 °C"],
                ["Freihandelsabkommen", "Vertrag zwischen Staaten, der Zölle und andere Handelshürden senkt"],
                ["Zoll / Zollkontingent", "Abgabe auf eingeführte Waren; ein Kontingent erlaubt eine Menge zu niedrigerem Zoll"],
                ["Mercosur", "Wirtschaftsbündnis von Argentinien, Brasilien, Paraguay und Uruguay"]]

# ---------------------------------------------------------------- Wiederholen
WEISST_DU_NOCH = {
    1: [("Fairer Handel: Was garantiert das Fairtrade-Siegel den Bauern?", "Einen Mindestpreis und eine Prämie für Gemeinschaftsprojekte."),
        ("Was ist eine Ökobilanz?", "Die Umweltwirkungen eines Produkts über den ganzen Lebensweg – von der Rohstoffgewinnung bis zur Entsorgung."),
        ("Nenne eine Säule der Nachhaltigkeit.", "Ökologie, Ökonomie oder Soziales.")],
    2: [("Was misst der ökologische Fußabdruck?", "Die Fläche (globale Hektar), die unser Konsum braucht."),
        ("Wie schwer ist der ökologische Rucksack eines Handys ungefähr?", "Rund 75 kg."),
        ("Wann war Österreichs Overshoot Day 2026?", "Am 2. April – fast vier Erden.")],
    3: [("Wie viel Strom braucht eine Gemini-Frage laut Google?", "0,24 Wh – das Training ist nicht eingerechnet."),
        ("Warum war in Kronstorf keine UVP nötig?", "Das Projekt lag unter den Schwellenwerten; Rechenzentren sind keine eigene UVP-Kategorie."),
        ("Wohin geht der Strom eines Rechenzentrums am Ende?", "Er wird zu Wärme, die abgeführt werden muss.")],
}

STOPPFRAGEN = {
    "abdruck": [("Overshoot Day am 5. Mai (Tag 125): Wie viele Erden?", "365 : 125 ≈ 2,9 Erden."),
                ("Warum misst man den Fußabdruck in globalen Hektar und nicht in normalen?", "Weil ein Hektar Acker in Österreich mehr hergibt als einer in der Wüste – globale Hektar machen das vergleichbar.")],
    "rucksack": [("Was ist schwerer: das Handy oder sein Rucksack?", "Der Rucksack – rund 75 kg gegenüber 0,1 kg."),
                 ("Was zählt beim CO₂-Fußabdruck nicht mit?", "Fläche und Material – er zählt nur Treibhausgase.")],
    "oekosysteme": [("Wie kam die Tigermücke nach Österreich?", "Mit dem Waren- und Reiseverkehr."),
                    ("Neophyt oder Neozoon: das Drüsige Springkraut?", "Neophyt – eine eingewanderte Pflanze.")],
    "ki": [("Wo wird der Strom eines Rechenzentrums am Ende hin?", "Er wird zu Wärme."),
           ("Warum ist die Zahl »0,24 Wh pro Frage« mit Vorsicht zu lesen?", "Google hat sie selbst berechnet; das Training fehlt.")],
    "kronstorf": [("Wie viel Strom braucht Kronstorf Stufe 1 im Jahr?", "Bis zu 1,31 TWh – so viel wie rund 375 000 Haushalte."),
                  ("Was fordern Umweltorganisationen?", "Eine UVP-Pflicht für große Rechenzentren.")],
    "treibhaus": [("Ist der Treibhauseffekt schlecht?", "Der natürliche ist lebenswichtig. Gefährlich ist die Verstärkung durch den Menschen."),
                  ("Welche Gase verstärken ihn vor allem?", "Kohlenstoffdioxid aus Kohle, Öl und Gas, dazu Methan und Lachgas.")],
    "konferenzen": [("Was ist das Ziel von Paris?", "Deutlich unter 2 °C, möglichst 1,5 °C."),
                    ("Warum scheiterte die COP31?", "Der Entwurf nannte Kohle, Öl und Gas nicht – die EU und andere legten Widerspruch ein.")],
    "handel": [("Wie viel Rindfleisch dürfen die Mercosur-Staaten zu niedrigem Zoll liefern?", "99 000 t pro Jahr zu 7,5 % – gut 1 % des EU-Verbrauchs."),
               ("Nenne ein Argument für und eines gegen Mercosur.", "Für: weniger Zölle, mehr Exporte. Gegen: Regenwald, Transport, Druck auf Bauern.")],
}

STOLPERSTEINE = [("»Fußabdruck und Rucksack sind dasselbe«",
                  "Fußabdruck = **Fläche** (gha, für Person oder Land), Rucksack = **Material in kg** (für ein Produkt), CO₂-Fußabdruck = **nur Treibhausgase**. Tabelle aus Aufgabe 3 vorne an die Tafel."),
                 ("»365 : Tag« falsch herum gerechnet",
                  "Viele teilen 92 : 365 = 0,25. Fragen: »Wie oft passt das Budget ins Jahr?« – Aufgabe 2 c) und d)."),
                 ("»KI ist nur Software, die braucht nichts«",
                  "Jede Antwort läuft auf Chips in Rechenzentren; Strom wird zu Wärme. Kronstorf-Zahlen und Rechenzentrum-Rechner zeigen."),
                 ("»Herstellerzahl = Wahrheit«",
                  "0,24 Wh sind eine **Eigenangabe** von Google, ohne Training. Quellenkritik: Wer sagt das, was fehlt? Aufgabe 4 e) und f)."),
                 ("»Treibhauseffekt = Ozonloch«",
                  "Zwei verschiedene Probleme: Treibhauseffekt = Wärme wird zurückgehalten (CO₂, Methan); Ozonloch = UV-Schutz geschwächt (FCKW). Aufgabe 6 d).")]

# ---------------------------------------------------------------- ABCD-Karte: »Weißt du noch?« (Frage, richtig, [3 Ablenker], Erklärung)
WDN_ABCD = {
    1: [("Was garantiert das Fairtrade-Siegel den Bauern?", "einen Mindestpreis und eine Prämie", ["einen Bio-Anbau", "dass nur Kinder unter 18 nicht mitarbeiten", "einen Gratis-Transport nach Europa"], "Mindestpreis plus Fairtrade-Prämie für Gemeinschaftsprojekte."),
        ("Eine Ökobilanz betrachtet …", "den ganzen Lebensweg eines Produkts", ["nur die Herstellung", "nur den Preis", "nur die Verpackung"], "Von der Rohstoffgewinnung bis zur Entsorgung."),
        ("Welche drei Säulen hat die Nachhaltigkeit?", "Ökologie, Ökonomie, Soziales", ["Bio, Fair, Regional", "Strom, Wasser, Wärme", "Bund, Land, Gemeinde"], "Umwelt, Wirtschaft und Gesellschaft gleichzeitig denken.")],
    2: [("Was misst der ökologische Fußabdruck?", "Fläche in globalen Hektar", ["Gewicht in kg", "CO₂ in Tonnen", "Strom in kWh"], "Fläche für Konsum und CO₂-Aufnahme."),
        ("Wie schwer ist der ökologische Rucksack eines Handys etwa?", "rund 75 kg", ["rund 0,1 kg", "rund 750 kg", "rund 7 kg"], "Das Handy selbst wiegt nur etwa 100 g."),
        ("Österreichs Overshoot Day 2026 war am …", "2. April", ["30. Juli", "24. Dezember", "1. Jänner"], "Der 30. Juli war der weltweite Overshoot Day.")],
    3: [("Wie viel Strom braucht eine Gemini-Frage laut Google?", "0,24 Wh", ["24 Wh", "0,24 kWh", "2,4 kWh"], "Herstellerangabe, ohne Training."),
        ("Wohin geht der Strom eines Rechenzentrums am Ende?", "Er wird zu Wärme", ["Er wird gespeichert", "Er fließt zurück ins Netz", "Er verschwindet"], "Darum braucht es Kühlung – in Kronstorf mit Wasser aus der Enns."),
        ("Warum war in Kronstorf keine UVP nötig?", "unter den Schwellenwerten", ["Google ist ausgenommen", "Die Gemeinde hat sie verboten", "UVP gibt es nicht mehr"], "Rechenzentren sind keine eigene UVP-Kategorie.")],
}
VERMUTUNG_ABCD = {}
for _n, _qs in WDN_ABCD.items():
    for _q in _qs: assert len(_q) == 4 and len(set([_q[1]] + _q[2])) == 4, _q

# ---------------------------------------------------------------- Mitarbeits-Check: 10 Fragen, nur Pflichtstoff, kein Militärbezug
CHECK = [
    {"thema": "Abdruck", "n": 3, "fragen": [
        ("f1", "Was misst der ökologische Fußabdruck?", "die Fläche für Konsum und CO₂-Aufnahme", ["das Gewicht eines Produkts", "nur das CO₂ in Tonnen", "den Stromverbrauch in kWh"], "S. 40"),
        ("f2", "In welcher Einheit wird der ökologische Rucksack angegeben?", "in Kilogramm", ["in globalen Hektar", "in Kilowattstunden", "in Grad Celsius"], "S. 40"),
        ("f3", "erden", "", [], "S. 40"),
        ("f4", "Ein Handy wiegt 0,1 kg. Sein Rucksack wiegt rund …", "75 kg", ["0,1 kg", "1 kg", "7500 kg"], "S. 40"),
        ("f5", "Was zählt der CO₂-Fußabdruck?", "Treibhausgase, umgerechnet in CO₂", ["Fläche in Hektar", "alle Rohstoffe in kg", "den Wasserverbrauch"], "S. 40")]},
    {"thema": "Ökosysteme", "n": 1, "fragen": [
        ("o1", "Eine eingewanderte Tierart heißt …", "Neozoon", ["Neophyt", "Endemit", "Biotop"], "S. 41"),
        ("o2", "Wie kommen gebietsfremde Arten wie die Tigermücke zu uns?", "mit Waren- und Reiseverkehr", ["durch Zugvögel im Winter", "nur über Zoos", "gar nicht"], "S. 41–42")]},
    {"thema": "KI und Rechenzentren", "n": 3, "fragen": [
        ("k1", "Wohin geht der Strom, den ein Rechenzentrum verbraucht, am Ende?", "Er wird zu Wärme", ["Er wird in Daten gespeichert", "Er fließt zurück ins Netz", "Er verschwindet spurlos"], "S. 97"),
        ("k2", "Die Angabe »0,24 Wh pro Gemini-Frage« stammt von …", "Google selbst", ["einer unabhängigen Uni", "der EU", "dem Umweltbundesamt"], "S. 97"),
        ("k3", "Was ist in der Zahl pro KI-Frage nicht eingerechnet?", "das Training der Modelle", ["die Kühlung", "der Serverstrom bei der Frage", "der Leerlauf der Server"], "S. 97"),
        ("k4", "Rebound-Effekt heißt: …", "Effizienz spart, aber mehr Nutzung frisst die Ersparnis auf", ["Strom fließt zurück ins Netz", "Server schalten sich nachts ab", "Daten werden zurückgeschickt"], "S. 97"),
        ("k5", "Was ist eine UVP?", "eine Prüfung der Umweltfolgen vor großen Bauprojekten", ["eine Steuer auf Strom", "ein Gütesiegel für Server", "eine Versicherung gegen Hochwasser"], "S. 40")]},
    {"thema": "Klima", "n": 2, "fragen": [
        ("c1", "Was machen Treibhausgase?", "Sie halten einen Teil der Wärmestrahlung zurück", ["Sie lassen kein Licht durch", "Sie zerstören die Ozonschicht", "Sie kühlen die Erde"], "S. 71"),
        ("c2", "Was ist das Ziel des Pariser Abkommens?", "deutlich unter 2 °C, möglichst 1,5 °C", ["genau 3 °C", "keine Erwärmung mehr ab 2016", "4 °C bis 2100"], "S. 74"),
        ("c3", "Woran scheiterte das Abschlusspapier der COP31?", "am Streit um Kohle, Öl und Gas", ["am Streit um den Gastgeber", "an einem Stromausfall", "an der Sprache des Vertrags"], "S. 73–74")]},
    {"thema": "Handel", "n": 1, "fragen": [
        ("h1", "Welche Staaten bilden den Mercosur?", "Argentinien, Brasilien, Paraguay, Uruguay", ["Mexiko, Kanada, USA", "Chile, Peru, Kolumbien, Ecuador", "Spanien, Portugal, Italien, Griechenland"], "S. 40–41"),
        ("h2", "Was macht ein Freihandelsabkommen?", "Es senkt Zölle und Handelshürden", ["Es verbietet Importe", "Es legt Preise im Supermarkt fest", "Es schafft eine gemeinsame Währung"], "S. 40")]},
]
assert sum(g["n"] for g in CHECK) == 10 and all(g["n"] <= len(g["fragen"]) for g in CHECK)
for _g in CHECK:
    for _q in _g["fragen"]:
        if _q[1] != "erden": assert len(set([_q[2]] + _q[3])) == 4, _q
CHECK_KEY = "26-27-5AB-K1.9-check"
CHECK_CODE = "7319"

PARTNERCHECK = [
    ("Erkläre den Unterschied zwischen Fußabdruck und Rucksack.", "Fußabdruck = Fläche in gha (Person, Land), Rucksack = Material in kg (Produkt)."),
    ("Overshoot Day am 10. Mai (Tag 130): Wie viele Erden?", "365 : 130 ≈ 2,8 Erden."),
    ("Warum braucht ein Rechenzentrum Kühlung?", "Fast der ganze Strom wird in den Chips zu Wärme."),
    ("Was fehlt in der Zahl »0,24 Wh pro KI-Frage«?", "Das Training der Modelle; außerdem ist es eine Eigenangabe von Google."),
]
assert abs(365 / 130 - 2.81) < 0.01 and abs(365 / 125 - 2.92) < 0.01

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 22.11.2026)
QUELLEN = [
 ("W1", "Einigung bei COP31 gescheitert (22.11.2026)", "news.ORF.at", "https://orf.at/stories/3448942/",
  "Kein Abschlusspapier; EU legte Widerspruch ein, weil fossile Brennstoffe nicht erwähnt wurden; auch Frankreich und Deutschland gegen den Text; Rekordverlängerung über 49 h (Stand des Artikels 22.11., 19:52; am 23.11. erneut geöffnet)", "Seite geöffnet, gelesen"),
 ("W2", "Großbaustelle von Google in Kronstorf (17.07.2026)", "news.ORF.at", "https://orf.at/stories/3436462/",
  "150 MW, bis 1,31 TWh/Jahr ≈ 375 000 Haushalte; Stufe 2 bis 500 MW; OÖ 14 TWh (2024); bis 5,8 Mio. l Kühlwasser/Tag, max. 30 °C; ca. 50 ha, keine UVP; Forderungen nach UVP-Pflicht", "Seite geöffnet, gelesen"),
 ("W3", "Google: KI-Anfrage braucht Strom wie neun Sekunden TV (22.08.2025)", "news.ORF.at", "https://orf.at/stories/3403199",
  "Gemini 0,24 Wh und 0,26 ml Wasser pro Textanfrage (Eigenberechnung Google); OpenAI 0,34 Wh; Training nicht enthalten", "Seite geöffnet, gelesen"),
 ("W4", "Foresight: KI-Rechenzentren (Nov. 2025)", "ÖAW-ITA und KIT-ITAS für das österreichische Parlament", "https://www.parlament.gv.at/dokument/fachinfos/zukunftsthemen/172_ki-rechenzentren.pdf",
  "IEA: Strombedarf Rechenzentren bis 2030 ca. 945 TWh; Rebound-Effekt; Abwärme; Österreich rund 80 % erneuerbarer Strom; Meldepflichten EU-Energieeffizienzrichtlinie", "PDF geöffnet, gelesen"),
 ("W5", "Overshoot Day in Österreich am 2. April (2026)", "APA, bei vol.at; Berechnung Global Footprint Network", "https://www.vol.at/overshoot-day-in-oesterreich-am-2-april/10082282",
  "Österreich 2.4.2026 (2025: 29.3., 2024: 7.4.); »fast vier Erden« (Greenpeace)", "Seite geöffnet, gelesen"),
 ("W6", "Earth Overshoot Day 2026 falls on July 30", "Global Footprint Network", "https://overshoot.footprintnetwork.org/",
  "Weltweit 30. Juli 2026; spätere Lage als 2025 vor allem wegen Datenrevision", "Suchtreffer und Startseite (Auszug) gelesen"),
 ("W7", "Fußabdruck-Rechner für Österreich", "BMLUK, Fachinhalte footprint-consult", "https://www.mein-fussabdruck.at/",
  "Schnellrechner ca. 5 min; ökologischer Fußabdruck (gha) und CO₂-Fußabdruck; Vergleich mit Österreich-Schnitt; Daten bis 2019, hochgerechnet bis 2022", "Seite geöffnet"),
 ("W8", "Ökologischer Rucksack (Stand 21.05.2024)", "Verbraucherzentrale NRW", "https://www.verbraucherzentrale.nrw/wissen/digitale-welt/mobilfunk-und-festnetz/oekologischer-rucksack-11539",
  "Rucksack = Materialbedarf in kg über den Lebensweg; Handy rund 75 kg; Goldring 5 g → 2000 kg", "Seite geöffnet, gelesen"),
 ("W9", "Die EU-Mercosur-Abkommen im Detail", "Rat der EU", "https://www.consilium.europa.eu/de/policies/eu-mercosur-agreements-explained/",
  "Unterzeichnung 17.01.2026, vorläufige Anwendung 1.5.2026; Kontingente u. a. Rindfleisch, Schutzklauseln", "Seite geöffnet, gelesen"),
 ("W10", "Factsheet EU-Mercosur", "Wirtschaftskammer Österreich (Interessenvertretung!)", "https://www.wko.at/oe/oesterreich/factsheet-mercosur.pdf",
  "Rindfleisch-Kontingent 99 000 t zu 7,5 % Zoll, etwas mehr als 1 % der rund 8 Mio. t EU-Verbrauch", "Auszug per Websuche gelesen; Zahl auch bei EU-Kommission (99 000 t)"),
 ("W11", "Das EU-Mercosur-Abkommen (Auslandsinformationen)", "Konrad-Adenauer-Stiftung", "https://www.kas.de/en/web/auslandsinformationen/artikel/detail/-/content/das-eu-mercosur-abkommen",
  "Gegen das Abkommen im Rat: Frankreich, Polen, Österreich, Ungarn, Irland; Belgien enthalten", "Auszug per Websuche gelesen; Österreichs Nein auch beim Landwirtschaftsministerium"),
 ("W12", "Asiatische Tigermücke", "AGES", "https://www.ages.at/mensch/krankheit/infos-zu-gelsen-und-krankheiten/asiatische-tigermuecke",
  "erste Tigermücke 2012; 2022 in allen Bundesländern; etablierte Populationen in Teilen von Wien, Graz, Linz", "Auszug per Websuche gelesen"),
 ("W13", "How big oil helped push the idea of a carbon footprint (19.12.2023)", "WBUR On Point, mit Geoffrey Supran (Univ. Miami)", "https://www.wbur.org/onpoint/2023/12/19/how-big-oil-helped-push-the-idea-of-a-carbon-footprint",
  "BP-Kampagne 2004–2006, Online-Rechner ca. 2005; kein internes Beweisdokument; persönliches Handeln sinnvoll, aber systemische Lösungen nötig", "Seite geöffnet, gelesen"),
 ("W15", "Measuring the environmental impact of AI inference (21.08.2025)", "Google Cloud Blog (Eigenangabe des Konzerns)", "https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference",
  "0,24 Wh pro mittlerer Gemini-Textanfrage inkl. CPU/RAM, Leerlauf-Maschinen, Kühlung und Rechenzentrums-Overhead; Training nicht enthalten; nur aktive Chips gerechnet wären 0,10 Wh", "Auszug per Websuche gelesen (23.11.2026)"),
 ("W16", "EU-Parlament ruft Gerichtshof zur Prüfung des Mercosur-Abkommens an (21.01.2026)", "epd, bei evangelisch.de", "https://www.evangelisch.de/inhalte/252087/21-01-2026/eu-parlament-ruft-gerichtshof-zur-pruefung-des-mercosur-abkommens",
  "EU-Parlament beschloss knapp (334 : 324, 11 Enthaltungen), ein EuGH-Gutachten einzuholen; Ratifizierung verzögert sich", "Auszug per Websuche gelesen (23.11.2026)"),
 ("W14", "Treibhauseffekt (Simulation)", "PhET, University of Colorado Boulder", "https://phet.colorado.edu/de/simulations/greenhouse-effect",
  "Deutsch, HTML5, Lizenz CC BY-NC 4.0; Treibhausgaskonzentration und Wolken einstellbar", "Seite geöffnet; Bedienung am Handy nicht live getestet"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "Video für Stunde 1: YouTube ist von hier aus nicht prüfbar. Darum steht auf den Kadetten-Seiten kein Video. Vorschläge zur Freigabe stehen auf der Lösungsseite – bitte eines auswählen und vor der Stunde ansehen.",
 "Trauner-Links aus dem Buch (trauner.at/fussabdruck.aspx, /oeko-global.aspx, /globalisierung.aspx) wurden nicht geöffnet.",
 "Podcasts aus deiner Jahresplan-Liste (z. B. Ö1 Dimensionen »Zölle« 2025, »Erklär mir die Welt #61 Globalisierung« 2019) wurden nicht angehört – nur als Vorschlag auf der Lösungsseite.",
 "Mercosur-Gegenstimmen im Rat (Frankreich, Polen, Österreich, Ungarn, Irland) und das Rindfleisch-Kontingent stammen aus Auszügen (KAS, WKO); die Rats-Seite selbst nennt keine Abstimmung. Österreichs Nein bestätigt auch das Landwirtschaftsministerium.",
 "PhET »Treibhauseffekt«: Seite geöffnet, Bedienung am Handy nicht getestet – bitte einmal selbst öffnen.",
 "Seilnacht-Filmverzeichnis: nicht passend (Chemie-Versuche), nicht durchsucht.",
]
