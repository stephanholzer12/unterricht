"""IWK 5AK · K2.2 Institutionen der Globalisierung (WTO, Weltbank, IWF) – 3 Stunden, Gruppenpräsentationen.
Trauner IWK 5, Teil II »Aspekte der Internationalisierung und Globalisierung«, Kapitel »Institutionen der Globalisierung« S. 52–63 = K2.2.
Seitenangaben immer nur nach dem Trauner-Schulbuch. Jahresplan v14: E5 »Akteure der Weltwirtschaft« (2 Std., Referat/Präsentation), K05, N01, N03,
P2, P4, P7, SDG 8, SDG 17, GLV 5 »Wirtschaftliche Ordnungsmacht, Mandate, Instrumente und Grenzen unterscheiden«.
Stephan 23.11.2026: 3 Stunden (Fr 27.11., Fr 4.12., Fr 18.12.), 6 Gruppen (2 je Institution), je 4 min mit 3 Folien am Beamer, Referatsthemen 5 (WTO)
und 6 (IWF) laufen als normale Gruppenreferate. Lieferung wie K2.1: GitHub, Präsentation und Lösungsseite.
Aktuelle Fakten (von Claude am 23.11.2026 geöffnet und geprüft) – siehe QUELLEN unten. Eine Quelle für Handy-Seiten und Lösungsseite.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "23.11.2026"
V = "v1"
ORDNER = "5ak-iwk/k2-2-institutionen"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ak-iwk/"
EYEBROW = "IWK · 5AK · Institutionen der Globalisierung"
TITEL = "WTO, Weltbank, IWF – wer regelt die Weltwirtschaft?"
KURZTITEL = "Institutionen der Globalisierung: WTO, Weltbank, IWF"
BUCH = "Buch S. 52–63"
KEY = "26-27-5AK-K2.2-Institut-TH-Handy-v1"
CHECK_KEY = "26-27-5AK-K2.2-Institut-Lernseite-Check-v1"
PRAEFIX = "26-27-5AK-K2.2-Institut"
KAP = "K2.2"
LEITFRAGE = "Wer macht die Regeln für Handel und Geld zwischen den Staaten – und wer hat dabei das Sagen?"

# Medien: (Titel, Quelle, Dauer, Link[, "link"|"sim"|"audio"]). Nur geprüfte Links sind freigegeben.
VIDEOS = {
    "gtai": ("GTAI: Die 14. Ministerkonferenz der Welthandelsorganisation (2. April 2026)", "Germany Trade & Invest", "Lesen, ca. 5 min",
             "https://www.gtai.de/de/trade/welt/zoll/ministerkonferenz-welthandelsorganisation-1988008", "link"),
}
FREIGEGEBEN = {"gtai"}


def zeigen(key, lehrer=False):
    return key in FREIGEGEBEN

# Geprüfte Quellen (Titel, Herausgeber, Datum, Link, Kernaussage) – stehen auf der Lösungsseite und als Rechercheeinstieg
QUELLEN = [
 ("WTO MC14: Zollmoratorium für digitale Übertragungen erstmals seit 1998 nicht verlängert; E-Commerce-Abkommen von 66 Mitgliedern; IFDA nicht aufgenommen",
  "GTAI (Karl Martin Fischer u. a.)", "02.04.2026", "https://www.gtai.de/de/trade/welt/zoll/ministerkonferenz-welthandelsorganisation-1988008"),
 ("MC14: kein Reform-Arbeitsplan, keine Ministererklärung; Ersatz-Berufungsverfahren MPIA mit 61 Mitgliedern",
  "World Economic Forum (Don Rodney Junio)", "29.04.2026", "https://www.weforum.org/stories/all/mc14-yaounde-wto-trade/"),
 ("Weltbank RDNA5: Wiederaufbau der Ukraine kostet fast 588 Mrd. US-Dollar (Stand 31.12.2025), fast das Dreifache des BIP 2025; direkte Schäden über 195 Mrd.",
  "Weltbank, Pressemitteilung", "23.02.2026", "https://www.worldbank.org/en/news/press-release/2026/02/23/updated-ukraine-recovery-and-reconstruction-needs-assessment-released"),
 ("IWF genehmigt der Ukraine 8,1 Mrd. US-Dollar (48 Monate, 1,5 Mrd. sofort); Auflagen: Steuereinnahmen, Korruptionsbekämpfung, flexibler Wechselkurs",
  "IWF, Pressemitteilung 26/66", "26.02.2026", "https://www.imf.org/en/news/articles/2026/02/26/pr-26066-ukraine-imf-executive-board-approves-usd-8point1-billion-under-an-eff-arrangement"),
 ("USA treten aus 66 internationalen Organisationen aus (Memorandum vom 7.1.2026)", "ZDFheute", "08.01.2026",
  "https://www.zdfheute.de/politik/ausland/usa-internationale-organisationen-rueckzug-un-diplomatie-100.html"),
 ("USA bleiben in IWF und Weltbank, fordern aber Reformen: IWF zurück zum Kernauftrag, Weltbank soll das 45-%-Klimaziel streichen",
  "US-Finanzministerium, Erklärung von Scott Bessent", "15.04.2026", "https://home.treasury.gov/news/press-releases/sb0442"),
 ("IWF hat 191 Mitglieder (Liechtenstein seit 21.10.2024)", "IWF, Pressemitteilung 24/387", "21.10.2024",
  "https://www.imf.org/en/news/articles/2024/10/21/pr-24387-liechtenstein-principality-of-liechtenstein-becomes-imfs-191st-member"),
 ("WTO-Generaldirektorin Okonjo-Iweala: zweite Amtszeit ab 1.9.2025, von allen 166 Mitgliedern im Konsens bestätigt", "WTO, Allgemeiner Rat",
  "29.11.2024", "https://www.wto.org/english/news_e/news24_e/gc_29nov24_e.htm"),
]

KLASSEN = ["5AK"]
_D = {1: "Fr 27.11.", 2: "Fr 4.12.", 3: "Fr 18.12."}
DATEN = {k: dict(_D) for k in KLASSEN}
TEILNAME = {1: "Teil 1 · Drei Institutionen im Überblick", 2: "Teil 2 · Vom Steckbrief zum Vortrag", 3: "Teil 3 · Vergleichen und beurteilen"}

# Stundentitel: kreativ, mit Fachteil nach dem Doppelpunkt (Standard 15.11.2026)
STUNDENTITEL = {1: "Wer ist hier zuständig? WTO, Weltbank und IWF im Überblick",
                2: "Drei Folien, vier Minuten: Aus Fakten wird ein Vortrag",
                3: "Gipfeltreffen im Klassenzimmer: Präsentationen und Urteil"}

# ======================================================================= Gruppen (6, je Institution 2)
# (Nr, Institution, Thema, Buchseiten, Leitfragen, Einstieg für die Recherche)
GRUPPEN = [
 (1, "WTO", "Regeln für den Welthandel", "Buch S. 53–55",
  "Welche drei Grundprinzipien gelten? Wie entscheidet die WTO, und wie läuft ein Handelsstreit?",
  "wto.org (Seite »What we do«) · Buch S. 53–55"),
 (2, "WTO", "Die WTO in der Krise", "Buch S. 55–57",
  "Warum ist die Doha-Runde gescheitert? Warum funktioniert die Streitschlichtung nicht mehr richtig? Was brachte die Konferenz in Kamerun 2026?",
  "GTAI-Bericht vom 2.4.2026 (Link in der Theorie) · Buch S. 55–57"),
 (3, "Weltbank", "Geld für Entwicklung und Wiederaufbau", "Buch S. 57–59",
  "Aus welchen fünf Teilen besteht die Weltbankgruppe? Wofür vergibt sie Kredite? Was kostet der Wiederaufbau der Ukraine?",
  "worldbank.org (Pressemitteilung vom 23.2.2026) · Buch S. 57–59"),
 (4, "Weltbank", "Die Weltbank in der Kritik", "Buch S. 59–60",
  "Warum gibt es trotz Weltbank noch so viel Armut? Was lief beim Inga-Staudamm schief? Was verlangen die USA heute von der Weltbank?",
  "Buch S. 59–60 · Erklärung des US-Finanzministeriums vom 15.4.2026"),
 (5, "IWF", "Feuerwehr für Staaten in Geldnot", "Buch S. 61–62",
  "Wann hilft der IWF? Wie viel Stimmgewicht haben die USA, China und Österreich – und warum? Was bekommt die Ukraine?",
  "imf.org (Pressemitteilung vom 26.2.2026) · Grafik Buch S. 62"),
 (6, "IWF", "Kredite mit Auflagen – Hilfe oder Zwang?", "Buch S. 61–63",
  "Was sind Strukturanpassungsprogramme? Warum spricht man von »Austerität«? Welche Auflagen hat die Ukraine 2026 bekommen?",
  "Buch S. 61–63 · IWF-Pressemitteilung vom 26.2.2026"),
]
GRUPPEN_WAHL = ["Gruppe %d · %s: %s" % (n, inst, thema) for n, inst, thema, *_ in GRUPPEN]

RASTER = [("Aufgabe", "Wofür ist die Institution da? (1 Satz)"),
          ("Sitz und Mitglieder", "Wo sitzt sie, wie viele Mitglieder, wer leitet sie?"),
          ("Wer entscheidet?", "Jedes Land eine Stimme oder nach Geld? Konsens oder Mehrheit?"),
          ("Werkzeuge", "Womit arbeitet sie: Regeln, Streitschlichtung, Kredite, Auflagen?"),
          ("Aktueller Fall", "Ein Fall aus 2025/2026 mit einer Zahl, einem Datum und einer Quelle"),
          ("Kritik", "Was werfen Kritiker vor – und was antwortet die Institution?"),
          ("Bezug Österreich und Sicherheit", "Was hat Österreich davon? Was hat das mit Sicherheit zu tun?")]

# ======================================================================= Aufgaben
# Offene Erklärungen »man« (Lehrkraft bewertet), Stichwörter nur als Schreibhilfe. Auswahlfelder prüft die Seite selbst.
ZUST = ["WTO", "Weltbank", "IWF"]

T = [
 # ======================================================= Stunde 1
 {"id": "a1", "nr": 1, "title": "Wer ist zuständig?", "src": "Buch S. 53", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 7,
  "q": "Sechs echte Fälle aus den Nachrichten. Ordne jedem die Institution zu, die dafür zuständig ist. Dann beantworte die Frage zum Stimmrecht.",
  "hint": "Die Tabelle auf Buch S. 53 hilft. Info: Theorie »Drei Institutionen, drei Aufgaben« und »Wer hat das Sagen?«",
  "type": "multi",
  "fields": [["f1", "a) Die USA heben Zölle auf Stahl an. Die EU hält das für unfair und will dagegen vorgehen.", ZUST, False],
             ["f2", "Die Ukraine braucht Geld, um zerstörte Kraftwerke, Brücken und Wohnhäuser wieder aufzubauen.", ZUST, False],
             ["f3", "Ein Staat kann seine Importe nicht mehr bezahlen. Seine Währung verliert stark an Wert.", ZUST, False],
             ["f4", "Indien und Südafrika wollen, dass der Patentschutz für Impfstoffe eine Zeit lang nicht gilt.", ZUST, False],
             ["f5", "Ein sehr armes Land bekommt einen zinslosen Kredit für Schulen und Brunnen.", ZUST, False],
             ["f6", "Die Ukraine bekommt 8,1 Mrd. US-Dollar Kredit – muss dafür aber mehr Steuern eintreiben und Korruption bekämpfen.", ZUST, False],
             ["stimme", "b) Warum haben die USA im IWF und in der Weltbank viel mehr Gewicht als Österreich?",
              ["Weil sich das Stimmrecht nach dem Kapitalanteil richtet – wer mehr einzahlt, hat mehr Stimmen",
               "Weil jedes Land gleich viele Stimmen hat, die USA aber öfter abstimmen",
               "Weil der Sitz in Washington ist und dort nur die USA entscheiden",
               "Weil Österreich kein Mitglied ist"]]],
  "chk": {"f1": {"sel": "WTO"}, "f2": {"sel": "Weltbank"}, "f3": {"sel": "IWF"}, "f4": {"sel": "WTO"}, "f5": {"sel": "Weltbank"}, "f6": {"sel": "IWF"},
          "stimme": {"sel": "Weil sich das Stimmrecht nach dem Kapitalanteil richtet – wer mehr einzahlt, hat mehr Stimmen"}},
  "sol": [["Musterlösung", ["a) Zölle → WTO · Wiederaufbau Ukraine → Weltbank · Zahlungskrise, Währung → IWF · Patentschutz (TRIPS) → WTO · "
                          "zinsloser Kredit für ein armes Land → Weltbank (IDA) · Kredit mit Auflagen für den Staatshaushalt → IWF.",
                          "b) Im IWF und in der Weltbank richtet sich das Stimmgewicht nach dem eingezahlten Kapital (Quote). Die USA haben im IWF rund 16 % "
                          "der Stimmen, Österreich unter 1 % (Buch S. 62). In der WTO hat dagegen jedes Mitglied eine Stimme, entschieden wird im Konsens."]]],
  "fsol": {},
  "tip": ["Drei Institutionen, drei Aufgaben", "theorie.html#ueberblick"], "besprechen": True},

 {"id": "a2", "nr": 2, "title": "Euer Steckbrief und eure drei Folien", "src": "Buch S. 52–63 · Gruppenthema", "own": True,
  "tag": "Stunde 1 und 2", "h": 2, "zeit": 40,
  "q": "Ihr recherchiert in der Gruppe zu eurem Thema und baut daraus drei Folien für einen Vortrag von 4 Minuten. "
       "Teil 1 (Stunde 1): Steckbrief nach dem Raster. Teil 2 (Stunde 2): Folien bauen und mit einer anderen Gruppe proben. Jeder trägt die Ergebnisse seiner Gruppe selbst ein.",
  "hint": "Raster und Gruppenthemen stehen in der Theorie unter »Euer Steckbrief«. Mindestens eine Quelle außer dem Buch, mit Datum. "
          "Folienvorlage zum Herunterladen: https://stephanholzer12.github.io/unterricht/5ak-iwk/k2-2-institutionen/Folienvorlage-Gruppen.pptx – genau diese drei Folien füllen. Die Folien gibt eine Person pro Gruppe als Datei in LMS ab (Name der Datei: Gruppe-Nummer-Thema).",
  "type": "multi",
  "fields": [["gruppe", "Unsere Gruppe und unser Thema", GRUPPEN_WAHL, False],
             ["mit", "Wir sind (Vornamen)"],
             ["aufgabe", "a) Aufgabe der Institution (1 Satz)"],
             ["sitz", "b) Sitz, Mitglieder, Leitung"],
             ["entscheid", "c) Wer entscheidet – und wie?"],
             ["werkzeug", "d) Werkzeuge: Regeln, Streitschlichtung, Kredite, Auflagen …"],
             ["fall", "e) Aktueller Fall: Was ist passiert? Eine Zahl, ein Datum"],
             ["kritik", "f) Kritik und Antwort darauf"],
             ["oesterreich", "g) Bezug zu Österreich und zur Sicherheit"],
             ["quellen", "h) Unsere Quellen (mindestens zwei, mit Datum; eine davon nicht das Buch)"],
             ["folien", "i) Stunde 2: Unsere drei Folien – Titel von Folie 1, 2 und 3"],
             ["streit", "j) Unsere Streitfrage für die Klasse (Folie 3)"],
             ["probe", "k) Probelauf mit Gruppe Nr. … – was hat die andere Gruppe gelobt, was sollen wir ändern?"],
             ["abgabe", "l) Folien als Datei in LMS abgegeben?", ["ja, von uns hochgeladen", "noch nicht"], False]],
  "chk": {"aufgabe": {"kw": [["Handel, Entwicklung oder Währung", r"handel|zoll|regel|entwickl|armut|kredit|wiederaufbau|währung|waehrung|zahlung|stabil|finanz"]], "man": True},
          "sitz": {"kw": [["Genf oder Washington", r"genf|washington"], ["Zahl der Mitglieder", r"16\d|18\d|19\d|\d{3}"]], "man": True},
          "entscheid": {"kw": [["Konsens, eine Stimme oder Kapitalanteil", r"konsens|stimme|kapital|quote|anteil|gewicht|mehrheit|einzahl"]], "man": True},
          "werkzeug": {"kw": [["Regeln, Streit, Kredit oder Auflage", r"regel|streit|schlicht|kredit|darlehen|auflage|bedingung|abkommen|beratung|zinslos"]], "man": True},
          "fall": {"kw": [["Zahl und Datum", r"\d"]], "man": True},
          "kritik": {"kw": [["Kritikpunkt", r"kritik|vorwurf|armut|ungleich|macht|blockier|auflage|spar|umwelt|staudamm|umsied|reich|usa|konsens"]], "man": True},
          "oesterreich": {"kw": [["Österreich oder Sicherheit", r"österreich|oesterreich|eu|export|sicher|ukraine|krieg|wiederaufbau|liefer|abhängig|abhaengig|stabil"]], "man": True},
          "quellen": {"kw": [["Quelle mit Datum", r"\d{4}|\d\.\d"]], "man": True},
          "folien": {"kw": [["drei Titel", r"1|2|3|steckbrief|fall|streit"]], "man": True},
          "streit": {"kw": [["Frage oder These", r"\?|soll|sollte|braucht|brauchen|ist|sind"]], "man": True},
          "probe": {"kw": [["Gruppe und Rückmeldung", r"\d|gut|lob|ändern|aendern|besser|zu lang|zu viel|lauter|zeit"]], "man": True},
          "abgabe": {"sel": "ja, von uns hochgeladen"}},
  "opt": ["probe"],
  "sol": [["So bewertest du (Raster)", ["Steckbrief a)–g) vollständig und sachlich richtig (Zuständigkeiten nicht vermischt)",
                                       "aktueller Fall mit Zahl, Datum und Quelle (2025/2026)", "zwei Quellen mit Datum, mindestens eine außer dem Buch",
                                       "drei Folien: Steckbrief · Fall · Streitfrage, wenig Text, Quelle auf der Folie", "Probelauf gemacht, Rückmeldung eingearbeitet"]],
          ["Erwartung je Gruppe", ["Gruppe 1: Meistbegünstigung, Gegenseitigkeit, Liberalisierung; Konsens; DSB. Fall: Zölle und Gegenzölle, Streit vor der WTO.",
                                   "Gruppe 2: Doha 2001–2016 ohne Ergebnis; Berufungsinstanz seit Ende 2019 lahm (USA blockieren Richter); MC14 März 2026: Zollverbot auf digitale Übertragungen erstmals seit 1998 ausgelaufen, keine Reform.",
                                   "Gruppe 3: IBRD, IDA, IFC, MIGA, ICSID; Ukraine: fast 588 Mrd. US-Dollar Wiederaufbau, fast 3 × BIP 2025 (Weltbank 23.2.2026).",
                                   "Gruppe 4: Armut nicht besiegt; Inga-Staudamm, Umsiedlungen, »safeguards« nicht verpflichtend; USA verlangen 2026 Fokus auf Armut und Wachstum statt Klimaziel.",
                                   "Gruppe 5: Kredite bei Zahlungsbilanzproblemen; Stimmanteil nach Quote (USA rund 16 %, Österreich unter 1 %); Ukraine 8,1 Mrd. US-Dollar, 1,5 Mrd. sofort (26.2.2026).",
                                   "Gruppe 6: Strukturanpassung, Sparpolitik, Privatisierung, Öffnung; Kritik: soziale Folgen (Griechenland); Ukraine-Auflagen: Steuern, Korruption, Wechselkurs."]]],
  "fsol": {"aufgabe": "WTO: Regeln für den Handel · Weltbank: Kredite für Entwicklung · IWF: Hilfe bei Zahlungskrisen",
           "fall": "Zahl + Datum + Quelle (2025/2026)", "quellen": "zwei Quellen mit Datum, eine außer dem Buch"},
  "kriterien": ["Steckbrief vollständig und richtig", "Fall mit Zahl, Datum, Quelle", "zwei Quellen mit Datum", "drei Folien nach Vorlage", "Probelauf"],
  "tip": ["Euer Steckbrief: das Raster", "theorie.html#raster"], "besprechen": True},

 # ======================================================= Stunde 3
 {"id": "a3", "nr": 3, "title": "Vergleichen und urteilen", "src": "Buch S. 57, 60–62", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 31,
  "q": "Während der Vorträge füllst du die Vergleichstabelle aus (Stichworte genügen). Danach schreibst du dein Urteil zum Statement in 3 Sätzen: "
       "Stimmst du zu? Warum? Was spricht dagegen?",
  "hint": "Statement: »Ohne die USA sind WTO, Weltbank und IWF am Ende.« Info: Theorie »Im Vergleich« und »Kritik – und was dahintersteckt«",
  "type": "multi",
  "fields": [["wto", "a) WTO: Aufgabe · wer entscheidet · ein Kritikpunkt"],
             ["wb", "Weltbank: Aufgabe · wer entscheidet · ein Kritikpunkt"],
             ["iwf", "IWF: Aufgabe · wer entscheidet · ein Kritikpunkt"],
             ["beste", "b) Welcher Vortrag hat dir am meisten erklärt – und warum? (1 Satz)"],
             ["urteil", "c) Dein Urteil zum Statement (3 Sätze: Meinung · Grund · Gegenargument)"]],
  "chk": {"wto": {"kw": [["Handel und Konsens", r"handel|zoll|regel|konsens|stimme|streit"]], "man": True},
          "wb": {"kw": [["Entwicklung und Kapitalanteil", r"entwickl|kredit|armut|wiederaufbau|kapital|anteil|gewicht|stimm"]], "man": True},
          "iwf": {"kw": [["Zahlungskrise und Auflagen", r"zahlung|währung|waehrung|kredit|auflage|bedingung|quote|anteil|spar"]], "man": True},
          "urteil": {"kw": [["Meinung, Grund und Gegenargument", r"weil|denn|deshalb|da "], ["Gegenargument", r"aber|jedoch|trotzdem|andererseits|dagegen|allerdings"]], "man": True}},
  "opt": ["beste"],
  "sol": [["Musterlösung", ["a) WTO: Regeln für den Handel · jedes Mitglied eine Stimme, Konsens · Kritik: blockiert, Streitschlichtung lahm, Doha gescheitert. "
                          "Weltbank: Kredite für Entwicklung und Wiederaufbau · Stimmen nach Kapitalanteil, USA stark · Kritik: Armut nicht besiegt, Großprojekte schaden Menschen und Natur. "
                          "IWF: Kredite bei Zahlungskrisen, Überwachung der Geldpolitik · Stimmen nach Quote · Kritik: harte Sparauflagen, reiche Länder bestimmen.",
                          "c) Beispiel: »Ich stimme nur teilweise zu. Die USA haben im IWF und in der Weltbank das größte Stimmgewicht und zahlen am meisten ein – ohne sie fehlt viel Geld. "
                          "Aber die USA sind 2026 in IWF und Weltbank geblieben, und auch die WTO arbeitet mit 166 Mitgliedern weiter, etwa mit einem eigenen Ersatz-Streitverfahren.« "
                          "(Gegenteilige Urteile zählen genauso, wenn sie begründet sind und ein Gegenargument nennen.)"]]],
  "fsol": {"wto": "Handel · Konsens · blockiert", "wb": "Entwicklung · Kapitalanteil · Armut/Großprojekte", "iwf": "Zahlungskrise · Quote · Sparauflagen",
           "urteil": "Meinung + Grund (weil …) + Gegenargument (aber …)"},
  "kriterien": ["alle drei Institutionen richtig unterschieden", "Urteil mit Grund", "Gegenargument genannt"],
  "tip": ["WTO, Weltbank und IWF im Vergleich", "theorie.html#vergleich"], "besprechen": True},

 # ======================================================= Zusatz · Für Schnelle (freiwillig, keine Hausübung)
 {"id": "a5", "nr": 5, "title": "Zwei Karikaturen deuten", "src": "Buch-Aufgabe S. 63 · Zusatz", "own": False, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Schau dir die beiden Karikaturen im Buch auf S. 63 an (Aufgabe 3). Beschreib jede in einem Satz und sag, welche Kritik sie ausdrückt.",
  "hint": "Neu formuliert nach der Buch-Aufgabe S. 63 (Nr. 3). Die Bilder sind nur im Buch. Erst beschreiben (Was sehe ich?), dann deuten (Was meint der Zeichner?).",
  "type": "multi",
  "fields": [["k1", "a) Karikatur 1 (»Welthandelsmeisterschaft«): Beschreibung und Aussage"],
             ["k2", "b) Karikatur 2 (Fisch und großes Tier): Beschreibung und Aussage"],
             ["stimmt", "c) Stimmt die Kritik heute noch? Ein Beispiel aus dieser Einheit"]],
  "chk": {"k1": {"kw": [["Norden gewinnt, Süden verliert", r"nord|süd|sued|regel|unfair|gewinn|reich|arm|spielregel"]], "man": True},
          "k2": {"kw": [["Stärkerer frisst Schwächeren", r"groß|gross|klein|fress|stark|schwach|china|eu|macht|konkurrenz"]], "man": True},
          "stimmt": {"kw": [["Beispiel", r"stimm|quote|usa|blockier|doha|zoll|auflage|ukraine|digital|\d"]], "man": True}},
  "sol": [["Musterlösung", ["a) Ein Fußballspiel »Nord gegen Süd«: Der Norden gewinnt, weil er die Regeln gemacht hat. Kritik: Die Handelsregeln nützen vor allem den reichen Industrieländern.",
                          "b) Ein kleiner Fisch spricht zu einem riesigen Tier mit der Flagge Chinas, das ihn gleich frisst. Kritik: Im Handel setzt sich der Stärkere durch, Partnerschaft auf Augenhöhe ist schwer.",
                          "c) z. B. ja: Im IWF entscheiden die reichen Länder nach Kapitalanteil mehr mit; oder teilweise: In der WTO hat jedes Land eine Stimme und kann blockieren."]]],
  "fsol": {"k1": "Norden macht die Regeln und gewinnt", "k2": "der Größere frisst den Kleineren", "stimmt": "z. B. Stimmgewicht nach Kapital im IWF"},
  "tip": ["Kritik – und was dahintersteckt", "theorie.html#kritik"]},

 {"id": "a6", "nr": 6, "title": "Eine KI-Antwort prüfen", "src": "Buch S. 53–62 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Eine KI hat auf »Erkläre den IWF in drei Sätzen« geantwortet: »Der IWF sitzt in Genf und vergibt vor allem langfristige Kredite für Schulen und Straßen. "
       "Jedes der 166 Mitglieder hat eine Stimme. Geleitet wird er traditionell von einem US-Amerikaner.« Finde die Fehler und schreib einen besseren Prompt.",
  "hint": "Ohne ChatGPT oder eine andere KI lösen – du prüfst die KI, nicht umgekehrt. Info: Theorie »Drei Institutionen, drei Aufgaben« und »Wer hat das Sagen?«",
  "type": "multi",
  "fields": [["fehler", "a) Die Fehler und ihre Korrektur (mindestens drei)"],
             ["prompt", "b) Dein besserer Prompt"],
             ["warum", "c) Warum vermischt die KI das wohl? (1 Satz)"]],
  "chk": {"fehler": {"kw": [["Washington", r"washington"], ["kurzfristige Kredite bei Zahlungskrisen", r"kurzfrist|zahlung|währung|waehrung|krise|weltbank"],
                             ["191 Mitglieder, Stimmen nach Quote", r"191|quote|kapital|anteil|gewicht"], ["Leitung Europa", r"europ|georgiev|bulgar|lagarde|weltbank.*usa|usa.*weltbank"]], "need": 3, "man": True},
          "prompt": {"kw": [["Quellen und Stand", r"quelle|stand|datum|offiziell|imf|beleg|aktuell|prüf|pruef"]], "man": True},
          "warum": {"kw": [["Verwechslung WTO/Weltbank", r"wto|weltbank|verwechs|ähnlich|aehnlich|vermisch|zusammen"]], "man": True}},
  "sol": [["Musterlösung", ["a) Sitz: Washington, nicht Genf (Genf = WTO). · Aufgabe: kurzfristige Kredite bei Zahlungskrisen und Überwachung der Geldpolitik; "
                          "langfristige Kredite für Schulen und Straßen vergibt die Weltbank. · Mitglieder: 191, nicht 166 (166 = WTO); Stimmen nach Quote, nicht eine Stimme je Land. "
                          "· Leitung: traditionell eine Europäerin oder ein Europäer (derzeit Kristalina Georgiewa); der Weltbank-Präsident ist traditionell US-Amerikaner.",
                          "b) z. B. »Erkläre den IWF in drei Sätzen: Sitz, Aufgabe, Stimmrecht. Gib zu jeder Angabe die Quelle und den Stand an und grenze den IWF von WTO und Weltbank ab.«",
                          "c) Die KI mischt Merkmale der drei ähnlichen Organisationen (Genf und 166 von der WTO, Projektkredite und US-Leitung von der Weltbank)."]]],
  "fsol": {"fehler": "Washington · Zahlungskrisen statt Projekte · 191 und Quote · Leitung Europa", "prompt": "… mit Quellen, Stand und Abgrenzung", "warum": "Merkmale von WTO und Weltbank vermischt"},
  "tip": ["Wer hat das Sagen?", "theorie.html#stimme"]},
]
assert [t["nr"] for t in T] == [1, 2, 3, 5, 6]   # 4 = »Ziele erreicht?«, 7 = Lesen und prüfen (unten eingefügt)
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")

GRP = {1: "Stunde 1 · " + STUNDENTITEL[1] + " (Buch S. 52–53)",
       2: "Stunde 1 und 2 · Gruppenarbeit: Steckbrief und Folien (Buch S. 52–63)",
       3: "Stunde 3 · " + STUNDENTITEL[3],
       0: "Zusatz · Für Schnelle und Neugierige · freiwillig, keine Hausübung"}

WICHTIGSTE = ["Die **WTO** (Genf, 166 Mitglieder) macht die Regeln für den Welthandel und schlichtet Handelsstreit. Jedes Mitglied hat eine Stimme, entschieden wird im **Konsens**.",
              "Die **Weltbank** (Washington) vergibt **langfristige Kredite** für Entwicklung und Wiederaufbau, die ärmsten Länder bekommen zinslose Kredite über die IDA.",
              "Der **IWF** (Washington, 191 Mitglieder) hilft Staaten in **Zahlungskrisen** mit Krediten – meist gegen **Auflagen** wie Sparen oder Reformen.",
              "Im IWF und in der Weltbank richtet sich das **Stimmrecht nach dem Kapitalanteil**: Die USA haben im IWF rund 16 % der Stimmen, Österreich unter 1 %.",
              "Alle drei stehen in der **Kritik**: Die WTO ist blockiert, der Weltbank wird vorgeworfen, Armut nicht besiegt zu haben, dem IWF harte Sparauflagen. 2026 ist der Druck groß – vor allem von den USA."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["WTO", "Welthandelsorganisation in Genf: Regeln für den Handel mit Waren, Dienstleistungen und geistigem Eigentum"],
                ["Weltbank", "Gruppe von fünf Institutionen in Washington, die Kredite für Entwicklung und Wiederaufbau vergibt"],
                ["IWF (Internationaler Währungsfonds)", "hilft Staaten bei Zahlungskrisen mit Krediten und überwacht die Geldpolitik"],
                ["Bretton Woods", "Ort der Konferenz 1944 in den USA, auf der Weltbank und IWF gegründet wurden"],
                ["Zoll", "Abgabe auf Waren, die über eine Grenze gebracht werden"],
                ["Meistbegünstigung", "ein Handelsvorteil für ein WTO-Mitglied gilt sofort für alle Mitglieder"],
                ["Liberalisierung", "Abbau von Zöllen und anderen Handelshemmnissen"],
                ["Konsens", "ein Beschluss gilt, wenn kein Mitglied deutlich dagegen ist – ein Land kann also blockieren"],
                ["Streitschlichtung (DSB)", "Verfahren der WTO, wenn sich zwei Mitglieder über Handelsregeln streiten"],
                ["Quote", "Kapitalanteil eines Landes im IWF; danach richten sich Stimmen und Kreditrahmen"],
                ["Zahlungsbilanz", "Gegenüberstellung aller Zahlungen eines Landes mit dem Ausland"],
                ["IDA", "Teil der Weltbank, der den ärmsten Ländern zinslose, langfristige Kredite gibt"],
                ["Auflage (Konditionalität)", "Bedingung, die ein Land für einen Kredit erfüllen muss"],
                ["Strukturanpassungsprogramm", "Paket aus Sparen, Privatisieren und Marktöffnung, das IWF und Weltbank vor allem in den 1980er- und 1990er-Jahren verlangten"],
                ["Austerität", "strenge Sparpolitik des Staates"],
                ["Moratorium", "vereinbarte Pause: Etwas wird eine Zeit lang nicht getan, z. B. keine Zölle erheben"]]

WEISST_DU_NOCH = {
    2: [("Wofür ist die WTO zuständig, wofür der IWF?", "WTO: Regeln für den Handel. IWF: Hilfe bei Zahlungskrisen."),
        ("Warum haben die USA im IWF mehr Gewicht als Österreich?", "Das Stimmrecht richtet sich nach dem Kapitalanteil (Quote).")],
}

STOPPFRAGEN = {
    1: [("Ein Land streitet mit einem anderen über Zölle. Wer ist zuständig?", "Die WTO – mit ihrer Streitschlichtung."),
        ("Was unterscheidet die Kredite von Weltbank und IWF?", "Weltbank: langfristig, für Entwicklungsprojekte. IWF: kurzfristig, wenn ein Staat in einer Zahlungskrise steckt."),
        ("Warum kann in der WTO ein einziges Land eine Einigung verhindern?", "Weil im Konsens entschieden wird.")],
    2: [("Was gehört auf Folie 2?", "Der aktuelle Fall: eine Zahl groß, ein Datum, die Quelle unten."),
        ("Ist die Webseite einer Organisation eine unabhängige Quelle über sie selbst?", "Nein – sie ist gut für Fakten, aber die Bewertung schreibt die Organisation über sich selbst.")],
    3: [("Nenne je einen Kritikpunkt an WTO, Weltbank und IWF.", "WTO: blockiert, Streitschlichtung lahm. Weltbank: Armut nicht besiegt, Großprojekte. IWF: harte Sparauflagen."),
        ("Was heißt Austerität?", "Strenge Sparpolitik des Staates.")],
}

PARTNERKARTEN = [("Wo sitzt die WTO, wo IWF und Weltbank?", "WTO in Genf, IWF und Weltbank in Washington."),
                 ("Was heißt Meistbegünstigung?", "Ein Vorteil für ein Mitglied gilt sofort für alle Mitglieder."),
                 ("Wie entscheidet die WTO?", "Im Konsens – jedes Mitglied hat eine Stimme."),
                 ("Wonach richtet sich das Stimmrecht im IWF?", "Nach der Quote, also dem Kapitalanteil."),
                 ("Was macht die IDA?", "Sie gibt den ärmsten Ländern zinslose, langfristige Kredite."),
                 ("Was ist eine Auflage?", "Eine Bedingung für einen Kredit, z. B. sparen oder Korruption bekämpfen."),
                 ("Was ist 2026 bei der WTO passiert?", "Das Zollverbot für digitale Übertragungen wurde erstmals seit 1998 nicht verlängert."),
                 ("Was kostet laut Weltbank der Wiederaufbau der Ukraine?", "Fast 588 Mrd. US-Dollar (Stand Ende 2025).")]

STOLPERSTEINE = [("WTO, Weltbank und IWF verwechseln", "Faustregel: WTO = Handel (Genf), Weltbank = Projekte und Entwicklung, IWF = Geld- und Zahlungskrisen. Weltbank und IWF sitzen beide in Washington."),
                 ("»Jedes Land eine Stimme« überall", "Das gilt nur in der WTO. In IWF und Weltbank richtet sich das Stimmrecht nach dem Kapitalanteil."),
                 ("Zölle = Sanktionen", "Zölle sind Handelspolitik und fallen unter WTO-Regeln. Sanktionen sind außenpolitische Strafmaßnahmen – dafür ist keine der drei Institutionen zuständig."),
                 ("Die Webseite der Organisation ist neutral", "Sie ist gut für Zahlen und Fakten, aber keine unabhängige Bewertung. Für Kritik braucht man eine zweite Quelle."),
                 ("Veraltete Zahlen aus dem Buch", "Mitgliederzahlen, Präsidenten und Fälle ändern sich. Immer mit Datum und aktueller Quelle angeben – das Buch hat den Stand 2025.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Überblick", "Wo hat die WTO ihren Sitz?", ["Genf", "Washington", "New York", "Brüssel"], "Die WTO sitzt in Genf, IWF und Weltbank in Washington.", "Buch S. 53"),
 ("Überblick", "Welche Institution ist für Handelsstreit zwischen Staaten zuständig?", ["WTO", "Weltbank", "IWF", "UNO-Sicherheitsrat"], "Die WTO hat dafür ein eigenes Streitschlichtungsverfahren.", "Buch S. 55"),
 ("Überblick", "Ein Staat kann seine Importe nicht mehr bezahlen. Wer hilft kurzfristig?", ["IWF", "WTO", "Weltbank", "OECD"], "Der IWF vergibt kurzfristige Kredite zum Ausgleich von Zahlungsdefiziten.", "Buch S. 53, 61"),
 ("Überblick", "Wer vergibt langfristige Kredite für Straßen, Schulen und Kraftwerke?", ["Weltbank", "IWF", "WTO", "Die EZB"], "Das ist Entwicklungsfinanzierung – Aufgabe der Weltbank.", "Buch S. 53, 58"),
 ("Gründung", "Wo wurden Weltbank und IWF 1944 gegründet?", ["Bei der Konferenz von Bretton Woods in den USA", "In Genf bei der WTO", "In Marrakesch", "In Wien bei der OPEC"],
  "Bretton Woods (New Hampshire) war die Konferenz zur Neuordnung der Weltwirtschaft nach dem Krieg.", "Buch S. 57–58"),
 ("WTO", "Was heißt Meistbegünstigung?", ["Ein Handelsvorteil für ein Mitglied gilt sofort für alle Mitglieder", "Das reichste Land bekommt die meisten Vorteile",
  "Entwicklungsländer zahlen keine Zölle", "Die WTO bevorzugt ihre Gründungsmitglieder"], "Vorteile werden unverzüglich und ohne Bedingung allen gewährt.", "Buch S. 54"),
 ("WTO", "Wie entscheidet die WTO?", ["Im Konsens – kein Mitglied darf deutlich dagegen sein", "Mit Stimmen nach Kapitalanteil", "Die USA entscheiden allein", "Die Generaldirektorin entscheidet"],
  "Deshalb kann ein einzelnes Land Einigungen blockieren.", "Buch S. 55"),
 ("WTO", "Welches Abkommen regelt den Patentschutz?", ["TRIPS", "GATS", "GATT", "NAMA"], "TRIPS = Abkommen über geistiges Eigentum wie Patente und Marken.", "Buch S. 54, 56"),
 ("WTO aktuell", "Was passierte bei der WTO-Konferenz in Kamerun im März 2026?", ["Das Zollverbot für digitale Übertragungen wurde erstmals seit 1998 nicht verlängert",
  "Alle Zölle weltweit wurden abgeschafft", "Die USA traten aus der WTO aus", "Die Doha-Runde wurde erfolgreich abgeschlossen"],
  "Seit 1. April 2026 dürfen Mitglieder Zölle auf digitale Übertragungen erheben – das liegt in ihrem Ermessen (GTAI, 2.4.2026).", "Buch S. 55–57"),
 ("Weltbank", "Was macht die IDA, ein Teil der Weltbank?", ["Sie gibt den ärmsten Ländern zinslose Langzeitkredite", "Sie schlichtet Handelsstreit", "Sie überwacht Wechselkurse", "Sie druckt Geld"],
  "Die IDA ist das wichtigste Finanzierungsinstrument für sehr arme Länder.", "Buch S. 58"),
 ("Weltbank", "Wie verteilt sich das Stimmrecht in der Weltbank?", ["Nach Wirtschaftskraft und Kapitalanteil – reiche Länder haben mehr Stimmen", "Jedes Land hat eine Stimme",
  "Nur die Gründungsmitglieder stimmen ab", "Nach der Einwohnerzahl"], "Gewichtetes Stimmrecht: USA, Japan, Deutschland, Großbritannien und Frankreich sind am stärksten.", "Buch S. 58"),
 ("Weltbank aktuell", "Wie viel kostet laut Weltbank-Schätzung vom Februar 2026 der Wiederaufbau der Ukraine?", ["Fast 588 Mrd. US-Dollar", "Rund 5,9 Mrd. US-Dollar", "Rund 58 Mrd. US-Dollar", "Über 5 Billionen US-Dollar"],
  "Das ist fast das Dreifache der ukrainischen Wirtschaftsleistung 2025 (Stand der Schäden: Ende 2025).", "Buch S. 57–59"),
 ("IWF", "Wonach richtet sich das Stimmgewicht eines Landes im IWF?", ["Nach seiner Quote, also dem Kapitalanteil", "Nach der Fläche des Landes", "Nach der Einwohnerzahl", "Jedes Land hat gleich viel"],
  "Die USA haben im IWF rund 16 % der Stimmen, Österreich unter 1 %.", "Buch S. 61–62"),
 ("IWF", "Was ist eine Auflage bei einem IWF-Kredit?", ["Eine Bedingung, die das Land für das Geld erfüllen muss", "Eine Strafzahlung an den IWF", "Ein Zoll auf Importe", "Eine Spende ohne Rückzahlung"],
  "Typische Auflagen: Staatsausgaben senken, Steuern eintreiben, Märkte öffnen, Korruption bekämpfen.", "Buch S. 61"),
 ("IWF", "Was heißt Austerität?", ["Strenge Sparpolitik des Staates", "Öffnung der Grenzen", "Abwertung der Währung", "Schuldenerlass"], "Kritiker sagen: Zu viel Sparen kann Krisenländer tiefer hineinreißen.", "Buch S. 62"),
 ("IWF aktuell", "Was hat der IWF der Ukraine im Februar 2026 genehmigt?", ["Einen Kredit über 8,1 Mrd. US-Dollar für vier Jahre – mit Reformauflagen", "Einen Schuldenerlass über 588 Mrd. US-Dollar",
  "Den Ausschluss aus dem IWF", "Ein Handelsabkommen mit der EU"], "1,5 Mrd. wurden sofort ausgezahlt, der Rest folgt in Tranchen nach Prüfungen (IWF, 26.2.2026).", "Buch S. 61"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]


# ====================================================================== Kompetenzmodell (Skill bhak-kompetenzmodell, 20.11.2026)
# hd: A verstehen und wiedergeben · B anwenden und analysieren · C diskutieren, interpretieren, begründen, bewerten
ZIELE = [{"nr": 1, "hd": "A", "text": "Ich kann Aufgaben, Sitz und Aufbau von WTO, Weltbank und IWF beschreiben und sie auseinanderhalten.",
          "theorie": "ueberblick", "buch": "Buch S. 53–61"},
         {"nr": 2, "hd": "A", "text": "Ich kann erklären, warum im IWF und in der Weltbank reiche Länder mehr Stimmen haben als in der WTO.",
          "theorie": "stimme", "buch": "Buch S. 55, 58, 62"},
         {"nr": 3, "hd": "B", "text": "Ich kann zu einer Institution einen aktuellen Fall recherchieren, mit Quelle und Datum belegen und vortragen.",
          "theorie": "raster", "buch": "Buch S. 52–63"},
         {"nr": 4, "hd": "C", "text": "Ich kann Kritik an WTO, Weltbank und IWF begründet beurteilen und ein Gegenargument nennen.",
          "theorie": "kritik", "buch": "Buch S. 57, 60–62"}]
KOMPETENZ = {"a1": ("A", 1, 1), "a2": ("B", 1, 3), "a3": ("C", 2, 4), "a5": ("C", 2, 4), "a6": ("C", 2, 1)}
for _t in T:
    if _t["id"] in KOMPETENZ:
        _t["hd"], _t["niveau"], _t["ziel"] = KOMPETENZ[_t["id"]]

# ---------------------------------------------------------------- »Ziele erreicht?« (Selbsteinschätzung, keine Punkte)
_ZT = {1: "Theorie »Drei Institutionen, drei Aufgaben« · Buch S. 53–61", 2: "Theorie »Wer hat das Sagen?« · Buch S. 55, 58, 62",
       3: "Theorie »Euer Steckbrief« · Buch S. 52–63", 4: "Theorie »Kritik – und was dahintersteckt« · Buch S. 57, 60–62"}
_ZZ = {"id": "zz", "nr": 4, "title": "Ziele erreicht? Deine Selbsteinschätzung", "src": "Meine Ziele (Theorie oben)", "own": True,
       "tag": "Selbsteinschätzung", "h": 3, "zeit": 1, "type": "multi", "vorhersage": True,
       "q": "Schätz ehrlich ein, wie gut du die vier Ziele der Einheit erreicht hast. Es gibt keine Punkte. Bei »noch nicht«: Lies den angegebenen Theorie-Teil und die Buchseite noch einmal.",
       "hint": "Ehrlich ist besser als schön – das hilft dir bei der Matura.",
       "fields": [["ziel%d" % z["nr"], "Ziel %d (%s): %s – bei »noch nicht«: %s" % (z["nr"], z["hd"], z["text"], _ZT[z["nr"]]),
                   ["zur Gänze", "überwiegend", "noch nicht"], False] for z in ZIELE],
       "chk": {}, "sol": [["Hinweis", ["Selbsteinschätzung – keine richtige oder falsche Antwort."]]],
       "tip": ["Meine Ziele", "theorie.html#ziele"]}
T.insert(min(i for i, t in enumerate(T) if t["tag"] == "Zusatz"), _ZZ)

# ====================================================================== Zusatztheorie für Schnelle (Standard 23.11.2026)
# Geprüfter Artikel: GTAI »Die 14. Ministerkonferenz der Welthandelsorganisation«, 02.04.2026, Karl Martin Fischer, Dr. Melanie Jordan, Julia Merle,
# Udo Sellhast; Herausgeber Germany Trade & Invest (gefördert vom Bundeswirtschaftsministerium). Von Claude am 23.11.2026 geöffnet und geprüft.
LESE_LINK = VIDEOS["gtai"][3]
T.append({"id": "les", "nr": 7, "title": "Lesen und prüfen: Was brachte die WTO-Konferenz 2026?", "src": "GTAI, 02.04.2026 · Zusatz", "own": True,
  "tag": "Zusatz", "h": 0, "zeit": 10, "type": "multi", "hd": "B", "niveau": 2, "ziel": 3,
  "q": "Du bist mit allem fertig? Lies den Bericht über die WTO-Konferenz in Kamerun (Link in der Theorie, »Noch mehr wissen«) und filtere das Wichtigste heraus.",
  "hint": "Quelle: Germany Trade & Invest (GTAI), »Die 14. Ministerkonferenz der Welthandelsorganisation«, 2. April 2026. Info: Theorie »Die WTO 2026«",
  "fields": [["drei", "a) Die drei wichtigsten Ergebnisse – in eigenen Worten, als Stichpunkte"],
             ["moratorium", "b) Was gilt seit 1. April 2026 bei digitalen Übertragungen?",
              ["Die Mitglieder dürfen Zölle darauf erheben – ob sie es tun, entscheidet jedes Land selbst",
               "Zölle darauf sind für immer verboten", "Alle Länder müssen sofort 10 % Zoll erheben", "Die WTO erhebt selbst eine Digitalsteuer"]],
             ["abkommen", "c) Was haben 66 Mitglieder vereinbart?",
              ["Ein eigenes Abkommen über elektronischen Handel, das erst nach 45 Ratifizierungen gilt",
               "Den Austritt aus der WTO", "Eine neue Berufungsinstanz mit sieben Richtern", "Die Abschaffung aller Agrarzölle"]],
             ["indien", "d) Warum wurde das Investitionsabkommen (IFDA) nicht in die WTO aufgenommen?",
              ["Weil laut EU-Kommission Indien als einziges Land dagegen war – und die WTO im Konsens entscheidet",
               "Weil die USA es verboten haben", "Weil es niemand unterschrieben hat", "Weil die Generaldirektorin dagegen war"]],
             ["kritik", "e) Quellenkritik: Wer steht hinter GTAI, und für wen ist der Text geschrieben? Was fällt dir beim Datum der Konferenz auf? (zwei Punkte)"],
             ["bruecke", "f) Brücke zur Stunde: Was zeigt der Bericht über das Konsensprinzip? (ein Satz)"]],
  "chk": {"moratorium": {"sel": "Die Mitglieder dürfen Zölle darauf erheben – ob sie es tun, entscheidet jedes Land selbst"},
          "abkommen": {"sel": "Ein eigenes Abkommen über elektronischen Handel, das erst nach 45 Ratifizierungen gilt"},
          "indien": {"sel": "Weil laut EU-Kommission Indien als einziges Land dagegen war – und die WTO im Konsens entscheidet"},
          "drei": {"man": True, "kw": [["Moratorium ausgelaufen", r"moratori|digital|elektron|zoll"], ["E-Commerce-Abkommen", r"66|abkommen|e-commerce|ecommerce|plurilateral"],
                                       ["IFDA oder TRIPS offen", r"ifda|invest|indien|trips|patent|offen|keine entscheidung"]]},
          "kritik": {"man": True, "kw": [["Herausgeber und Zielgruppe", r"ministerium|regierung|bund|deutsch|unternehm|firma|wirtschaft|export"],
                                         ["Datum widersprüchlich", r"29|30|datum|unterschied|anders|widersprech|nacht"]]},
          "bruecke": {"man": True, "kw": [["ein Land kann blockieren", r"ein land|einzig|blockier|alle zustimmen|konsens|veto|verhinder"]]}},
  "fsol": {"drei": "Zollverbot für digitale Übertragungen ausgelaufen · E-Commerce-Abkommen von 66 Mitgliedern · IFDA und TRIPS ohne Entscheidung",
           "kritik": "GTAI ist die Außenwirtschaftsagentur Deutschlands (gefördert vom Wirtschaftsministerium), schreibt für Unternehmen; Ende 29. oder 30. März – Quellen nennen unterschiedliche Tage",
           "bruecke": "Ein einziges Land kann eine Einigung verhindern."},
  "sol": [["Musterlösung", [
    "a) Das Zollverbot für digitale Übertragungen ist erstmals seit 1998 ausgelaufen. · 66 Mitglieder wollen ein eigenes E-Commerce-Abkommen. · "
    "Das Investitionsabkommen (IFDA) und der Patentschutz (TRIPS) blieben ohne Entscheidung.",
    "b) Seit 1. April 2026 dürfen Mitglieder Zölle auf digitale Übertragungen erheben; ob sie es tun, liegt in ihrem Ermessen.",
    "c) Ein plurilaterales Abkommen über elektronischen Handel, das zuerst nur zwischen den Teilnehmenden gilt, sobald 45 es ratifiziert haben.",
    "d) Laut EU-Kommission stimmte Indien als einziges Land gegen die Aufnahme – im Konsensprinzip reicht das.",
    "e) GTAI ist die Agentur der deutschen Bundesregierung für Außenwirtschaft, gefördert vom Bundeswirtschaftsministerium; sie schreibt für Unternehmen, "
    "die exportieren. Der Bericht nennt den 26. bis 29. März, die WTO und andere Quellen nennen den 30. März als letzten Tag (die Konferenz endete in der Nacht).",
    "f) Im Konsens kann schon ein einziges Land eine Einigung verhindern, die fast alle anderen wollen."]]],
  "tip": ["Die WTO 2026", "theorie.html#aktuell"]})
assert [t["nr"] for t in T] == list(range(1, 8)), "Aufgaben müssen in Reihenfolge stehen (Stephan 23.11.2026)"
PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] not in ("Zusatz", "Selbsteinschätzung")]
assert PFLICHT == [1, 2, 3]
BESPRECHEN = [t["nr"] for t in T if t.get("besprechen")]
_pf = [t for t in T if t["nr"] in PFLICHT]
assert sum(t["niveau"] == 1 for t in _pf) >= 2 and any(t["niveau"] == 2 for t in _pf), "Pflicht: mindestens zwei + und eine ++"
assert {t["hd"] for t in T if "hd" in t} == {"A", "B", "C"}, "A, B und C müssen vorkommen"

LERNZIELE = [z["text"] for z in ZIELE]
HEUTE_ZIEL = {1: "WTO, Weltbank und IWF auseinanderhalten – und mit der Gruppe den Steckbrief beginnen.",
              2: "Aus dem Steckbrief drei klare Folien machen und den Vortrag proben.",
              3: "Vortragen, zuhören, vergleichen – und ein begründetes Urteil schreiben."}

# ====================================================================== ABCD-Karte (Standard 15.11.2026)
WDN_ABCD = {
 1: [("Was treibt die Globalisierung am stärksten an?", "Billiger Transport, Digitalisierung und offene Märkte – mehrere Kräfte zusammen",
      ["Nur das Internet", "Nur die Kolonialzeit", "Ein Beschluss der UNO"], "Erinnerung an K2.1: Es gibt nicht die eine Ursache, sondern mehrere Antriebskräfte."),
     ("Was heißt Liberalisierung?", "Zölle und andere Handelshemmnisse abbauen", ["Neue Zölle einführen", "Märkte für Ausländer schließen", "Staatsbetriebe gründen"],
      "Genau das ist auch eines der drei WTO-Prinzipien."),
     ("Wer war laut Buch ein bekannter Kritiker der Globalisierung, wie sie läuft?", "Joseph Stiglitz", ["Adam Smith", "Kristalina Georgiewa", "Ngozi Okonjo-Iweala"],
      "Stiglitz kritisiert vor allem den IWF – das kommt heute wieder vor.")],
 2: [("Welche Institution ist für Handelsstreit zuständig?", "WTO", ["IWF", "Weltbank", "OECD"], "Die WTO hat dafür die Streitschlichtung (DSB)."),
     ("Wonach richtet sich das Stimmrecht im IWF?", "Nach dem Kapitalanteil (Quote)", ["Jedes Land eine Stimme", "Nach der Einwohnerzahl", "Nach der Fläche"],
      "Darum haben die USA rund 16 % der Stimmen, Österreich unter 1 %."),
     ("Wo sitzt die Weltbank?", "Washington", ["Genf", "Wien", "Brüssel"], "IWF und Weltbank sitzen beide in Washington, die WTO in Genf.")],
}
VERMUTUNG_ABCD = {
 "K2.2-D1": ("Dein neues Handy wird wegen Zöllen 20 % teurer. Wer ist zuständig, wenn sich die EU dagegen wehren will?", "Die WTO",
             ["Der IWF", "Die Weltbank", "Niemand – Zölle darf jedes Land frei festlegen"],
             "Zölle regelt die WTO. Völlig frei ist kein Mitglied: Es hat sich auf Höchstzölle und Regeln verpflichtet. Wehren kann man sich mit der Streitschlichtung – "
             "die funktioniert seit Ende 2019 allerdings nur noch eingeschränkt."),
}

# ====================================================================== Mitarbeits-Check (Standard 15.11.2026)
MCHECK = [
 {"thema": "Überblick", "n": 3, "fragen": [
   ("u1", "Wo sitzt die WTO?", "Genf", ["Washington", "Wien", "New York"], "S. 53"),
   ("u2", "Welche Institution hilft Staaten in Zahlungskrisen?", "Der IWF", ["Die WTO", "Die Weltbank", "Die OECD"], "S. 53, 61"),
   ("u3", "Welche Institution vergibt langfristige Kredite für Entwicklungsprojekte?", "Die Weltbank", ["Der IWF", "Die WTO", "Die EZB"], "S. 53, 58"),
   ("u4", "Wo wurden Weltbank und IWF gegründet?", "In Bretton Woods (USA), 1944", ["In Genf, 1995", "In Marrakesch, 1994", "In Paris, 1961"], "S. 57–58")]},
 {"thema": "WTO", "n": 2, "fragen": [
   ("w1", "Wie entscheidet die WTO?", "Im Konsens – jedes Mitglied hat eine Stimme", ["Nach Kapitalanteil", "Mit einfacher Mehrheit der reichen Länder", "Die Generaldirektorin allein"], "S. 55"),
   ("w2", "Was bedeutet Meistbegünstigung?", "Ein Vorteil für ein Mitglied gilt für alle Mitglieder", ["Arme Länder zahlen keine Zölle", "Die größten Länder bekommen Rabatt", "Zölle dürfen nur steigen"], "S. 54"),
   ("w3", "Warum funktioniert die WTO-Streitschlichtung seit Ende 2019 nur eingeschränkt?", "Die Berufungsinstanz hat keine Richter, weil die USA Ernennungen blockieren",
    ["Weil die WTO aufgelöst wurde", "Weil es keine Handelsstreitigkeiten mehr gibt", "Weil die EU ausgetreten ist"], "S. 57")]},
 {"thema": "Weltbank", "n": 2, "fragen": [
   ("b1", "Was macht die IDA?", "Zinslose Langzeitkredite für die ärmsten Länder", ["Handelsstreit schlichten", "Wechselkurse festlegen", "Zölle einheben"], "S. 58"),
   ("b2", "Woran richtet sich das Stimmrecht in der Weltbank?", "An der Wirtschaftskraft bzw. dem Kapitalanteil", ["Jedes Land eine Stimme", "An der Einwohnerzahl", "An der Fläche"], "S. 58"),
   ("b3", "Was ist ein häufiger Kritikpunkt an der Weltbank?", "Großprojekte wie Staudämme haben Menschen vertrieben", ["Sie vergibt gar keine Kredite", "Sie hat keine Mitglieder", "Sie entscheidet im Konsens"], "S. 60")]},
 {"thema": "IWF", "n": 3, "fragen": [
   ("i1", "Wonach richtet sich das Stimmgewicht im IWF?", "Nach der Quote (Kapitalanteil)", ["Nach der Einwohnerzahl", "Jedes Land gleich", "Nach dem Alter der Mitgliedschaft"], "S. 61–62"),
   ("i2", "Was ist eine Auflage?", "Eine Bedingung, die ein Land für einen Kredit erfüllen muss", ["Eine Strafe für zu viel Export", "Eine Spende ohne Rückzahlung", "Ein Zoll"], "S. 61"),
   ("i3", "Was heißt Austerität?", "Strenge Sparpolitik", ["Schuldenerlass", "Mehr Staatsausgaben", "Abschaffung der Währung"], "S. 62"),
   ("i4", "Was gehörte zu Strukturanpassungsprogrammen?", "Sparen, Privatisieren, Märkte öffnen", ["Zölle erhöhen", "Banken verstaatlichen", "Mehr Beamte einstellen"], "S. 61")]},
]
assert sum(g["n"] for g in MCHECK) == 10
assert all(len(f[3]) == 3 for g in MCHECK for f in g["fragen"])
MCHECK_KEY = "26-27-5AK-K2.2-Institut-check"
MCHECK_CODE = "4719"   # Startcode – im Seitencode nur als Prüfsumme; Prof. HOLZER zeigt ihn am Beamer
