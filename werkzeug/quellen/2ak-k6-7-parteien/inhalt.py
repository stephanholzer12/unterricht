"""PBGW 2AK · K6–K7 Wahlrecht und Parteien – Geschichte und Ideologie (Trauner PBGW 2, »Jugend und Politik«, S. 23–35) – v1.
Auftrag Stephan 20.11.2026: neue Einheit, 4 Stunden, Start 23.11.2026, letzte Stunde nach den Weihnachtsferien. Referat SPÖ und FPÖ in Stunde 1,
Referat »Befragung von Parteivertretern« in Stunde 3 (21.12.). Lieferung: nur Kadetten-Seiten (GitHub) + private Lösungsseite, keine PPP, kein Word.
Planübersicht v2 (Projekt: claude/Planung-Parteien-Ideologien.md) von Stephan mit »weitermachen« freigegeben (Stunde 2 = 30.11., Referate 12 und 20 min, 4 Pflichtaufgaben + Mindmap).
Jahresplan PBGW 2. Jg.: Block B »Parteien & Ideologien«, E4 + E5 (K01, K02, N01, P4, GLV 1); Wahlrecht-Geschichte aus Buch K6 (Jahresplan E6/E13 berühren das).
E6 »Wahlprogramme kritisch lesen« (K03) bleibt eine eigene Einheit.
Keine Daten auf den Kadetten-Seiten (Standard 13.11.2026). Keine Versuche (PBGW). Kontroversitätsprinzip: Parteien gleich behandeln, nur Buchbeschreibung
oder geprüfte Primärquelle, keine Wertung, keine Wahlempfehlung.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "20.11.2026"
V = "v1"
ORDNER = "2ak-pbgw/k6-7-parteien"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "2ak-pbgw/"
EYEBROW = "PBGW · 2AK · K6–7 Wahlrecht und Parteien"
TITEL = "Wer darf mitreden? Wahlrecht, Parteien und Ideologien"
KURZTITEL = "Wahlrecht und Parteien"
BUCH = "Buch S. 23–35"
KEY = "26-27-2AK-K6-7-Parteien-TH-Handy-v1"
LERNSEITE_KEY = "26-27-2AK-K6-7-Parteien-Lernseite-Check-v1"
PRAEFIX = "26-27-2AK-K6-7-Parteien"
KLASSEN = ["2AK"]
STUNDEN = 4

VS = {}
DEMOS = {}
REFERATE = {1: {"titel": "Referat: SPÖ und FPÖ", "min": 12, "hoer": "3 Hörfragen: Aus welchem Lager kommt die Partei? Wann gegründet? Zwei Grundwerte."},
            3: {"titel": "Referat: Ein Kadett befragt Vertreter mehrerer Parteien zur selben Frage", "min": 20,
                "hoer": "Hörbogen in Aufgabe 4 f) und g): Welche Frage? Bei welcher Partei passte die Antwort zur Buchbeschreibung?"}}

# Stundentitel (kreativ, Fachteil nach dem Doppelpunkt) – EINE Quelle für Fahrplan, Arbeitsblatt, Präsentation, Lösungsseite.
STUNDENTITEL = {1: "Wer darf mitreden? Vom Kaiser zum Wählen mit 16",
                2: "Drei Lager, drei Welten: Wie unsere Parteien entstanden",
                3: "Links, rechts, liberal: Wo stehen die Parteien?",
                4: "Faktencheck: Was stimmt über unsere Parteien?"}
STUNDENNAME = {n: f"Stunde {n} · {t}" for n, t in STUNDENTITEL.items()}

# Zeitleiste (Buch S. 23–26; Wahlalter 1919 = 20 laut politik-lexikon.at, Buch sagt 21)
E1861 = "Kurienwahlrecht: nur Männer mit Besitz, in vier Gruppen"
E1873 = "Zensuswahlrecht: nur wer genug Steuer zahlt (ca. 6 % der Männer)"
E1896 = "5. Kurie: auch Arbeiter wählen – ihre Stimme zählt wenig"
E1907 = "allgemeines, gleiches Wahlrecht für Männer ab 24"
E1918 = "Frauen und Männer wählen gleich"
E1933 = "keine freien Wahlen"
E2007 = "Wählen ab 16"
EREIGNISSE = [E1861, E1873, E1896, E1907, E1918, E1933, E2007]


def opts(richtig):
    return [richtig] + [e for e in EREIGNISSE if e != richtig]


LAGER = ["Liberale und Deutschnationale", "Christlichsoziale", "Sozialdemokraten"]

# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "hd": "A", "niveau": 1, "ziel": 1, "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 23", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Drei Fragen zum Start – ohne Punkte, ohne »richtig« oder »falsch«. Tipp einfach, was du glaubst. Nach dem Besprechen schaust du nach.",
  "hint": "Einfach tippen. Deine Antwort bleibt gespeichert.",
  "type": "multi", "vorhersage": True,
  "fields": [["p1", "a) Seit wann dürfen Frauen in Österreich bei Parlamentswahlen wählen?", ["seit 1918", "seit 1945", "seit 1971"], False],
             ["p2", "b) Im Jahr 1873: Wie viele von 100 Männern ab 24 durften wählen?", ["etwa 6", "etwa 50", "alle"], False],
             ["p3", "c) Gehen 16- und 17-Jährige seltener wählen als 18- bis 20-Jährige?",
              ["Nein – in Studien gingen sie sogar öfter", "Ja – viel seltener", "Das hat noch niemand untersucht"], False]],
  "chk": {},
  "aufloesung": [["p1", "seit 1918", "Seit 1918 – nach dem Ende der Monarchie. Die erste Wahl mit Frauen war im Februar 1919 (Buch S. 23, 25). In der Schweiz kam das Frauenwahlrecht erst 1971."],
                 ["p2", "etwa 6", "Beim Zensuswahlrecht ab 1873 zählte die Steuer. Nur etwa 6 von 100 Männern ab 24 zahlten genug (Buch S. 24)."],
                 ["p3", "Nein – in Studien gingen sie sogar öfter", "Eine Studie der Uni Wien (2014) fand bei Wahlen in Wien und Krems: 16- und 17-Jährige gingen öfter wählen als 18- bis 20-Jährige. Mehr dazu in Zusatz 8."]],
  "sol": [["Auflösung", ["a) seit 1918 (erste Wahl mit Frauen: Februar 1919)", "b) etwa 6 von 100 (Buch S. 24)",
                         "c) Nein – Zeglovits/Aichholzer 2014: Wien 2010 64 % (16–17) gegen 56 % (18–20)."]]],
  "tipps": [], "tip": ["Wahlrecht", "theorie.html#wahlrecht"]},

 {"id": "a1", "hd": "A", "niveau": 1, "ziel": 1, "sim": ["zeitmaschine"], "nr": 2, "title": "Vom Kaiser zum Wählen mit 16", "src": "Buch S. 23–26", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 10, "marke": "SELBSTSTUDIUM",
  "q": "Ordne jeder Jahreszahl zu, was damals beim Wahlrecht neu war. Die Zeitleiste steht im Buch auf S. 23. Danach zwei Fragen zum Nachdenken.",
  "hint": "Die Reihenfolge ist: erst Besitz, dann Steuer, dann alle Männer, dann alle – mit einer Pause dazwischen.",
  "type": "multi",
  "fields": [["j1861", "a) 1861", opts(E1861)], ["j1873", "b) 1873", opts(E1873)], ["j1896", "c) 1896", opts(E1896)],
             ["j1907", "d) 1907", opts(E1907)], ["j1918", "e) 1918", opts(E1918)], ["j1933", "f) 1933 bis 1945", opts(E1933)],
             ["j2007", "g) 2007", opts(E2007)],
             ["frau", "h) Wer durfte 1907 trotz »allgemeinem« Wahlrecht NICHT wählen?", ["Frauen", "Arbeiter ohne Besitz", "Männer über 30"]],
             ["quelle", "i) Das Buch schreibt: Wahlalter 1918 = 21. Eine Seite des Demokratiezentrums Wien schreibt: Wahlalter 1919 = 20. Was machst du?",
              ["eine dritte, unabhängige Quelle prüfen (z. B. Parlament)", "dem Buch glauben – Schulbuch ist Schulbuch", "der Internetseite glauben – sie ist neuer"]]],
  "chk": {"j1861": {"sel": E1861}, "j1873": {"sel": E1873}, "j1896": {"sel": E1896}, "j1907": {"sel": E1907},
          "j1918": {"sel": E1918}, "j1933": {"sel": E1933}, "j2007": {"sel": E2007},
          "frau": {"sel": "Frauen"}, "quelle": {"sel": "eine dritte, unabhängige Quelle prüfen (z. B. Parlament)"}},
  "fb": {"j1907": {E1918: "1907 durften Frauen noch nicht wählen – das kam elf Jahre später.", E1896: "1896 kam erst die 5. Kurie dazu. Gleich war die Stimme damals noch nicht."},
         "j1918": {E1907: "1907 war schon das Männerwahlrecht. 1918 kam etwas Großes dazu.", E2007: "Wählen ab 16 kam viel später."},
         "j1873": {E1861: "1861 entschied der Besitz (Kurien). 1873 kam es auf die Steuer an.", E1896: "Die 5. Kurie kam 1896."},
         "frau": {"Arbeiter ohne Besitz": "Gerade die Arbeiter bekamen 1907 das gleiche Wahlrecht – das hatten sie mit Demonstrationen erkämpft.",
                  "Männer über 30": "Männer ab 24 durften wählen. Ab 30 durfte man sogar gewählt werden."},
         "quelle": {"dem Buch glauben – Schulbuch ist Schulbuch": "Auch Schulbücher können Fehler haben. Prüfen ist besser als glauben.",
                    "der Internetseite glauben – sie ist neuer": "Neuer heißt nicht richtiger. Eine dritte Quelle entscheidet."}},
  "sol": [["Lösung", ["a) 1861 Kurienwahlrecht · b) 1873 Zensuswahlrecht · c) 1896 5. Kurie · d) 1907 allgemeines, gleiches Männerwahlrecht ab 24",
                      "e) 1918 Frauen und Männer gleich · f) 1933–1945 keine freien Wahlen · g) 2007 Wählen ab 16",
                      "h) Frauen · i) eine dritte, unabhängige Quelle prüfen. Stand der Prüfung: Für die Wahl 1919 galt Wahlalter 20 (politik-lexikon.at). Das Buch schreibt 21 – das ist ungenau."]]],
  "tipps": ["Was zählte zuerst: Besitz oder Steuer? Und wann durften die Frauen endlich mit?",
            "k1",
            "Lies im Buch S. 23 die Zeitleiste »Überblick über die Entwicklung des Wahlrechts in Österreich«."],
  "tip": ["Wahlrecht", "theorie.html#wahlrecht"]},

 # --------------------------------------------------------------- Stunde 2
 {"id": "a2", "hd": "B", "niveau": 1, "ziel": 2, "nr": 3, "title": "Drei Lager – deine Tabelle mit der Hand", "src": "Buch S. 27–32", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 13, "marke": "SELBSTSTUDIUM",
  "type": "sketch",
  "q": "Zeichne auf ein Blatt eine Tabelle mit 4 Spalten: Lager · Wer stand dahinter? · Wichtigstes Ziel · Partei heute. Eine Zeile pro Lager, also 3 Zeilen. "
       "Was du im GRUPPENPUZZLE gehört hast, kommt hinein. Fotografiere das Blatt (Datum oben drauf) – danach kommt es in deine Mappe. Dann beantwortest du die Fragen a) bis h).",
  "hint": "Wo steht's? Buch S. 27–30 und Theorie Teil 2. Für g) und h): Buch S. 31–32 und Theorie Teil 3.",
  "fields": [["gruppe", "a) In welcher Expertengruppe warst du?", LAGER, False],
             ["lueger", "b) Wer wurde 1897 Bürgermeister von Wien und hetzte offen gegen Juden?", ["Karl Lueger", "Victor Adler", "Georg von Schönerer"]],
             ["adler", "c) Wer einigte die Arbeiterbewegung beim Parteitag in Hainfeld (1888/89)?", ["Victor Adler", "Karl Lueger", "Karl von Vogelsang"]],
             ["oevp", "d) Aus welchem Lager kommt die heutige ÖVP?", ["aus dem christlichsozialen Lager", "aus dem sozialdemokratischen Lager", "aus dem deutschnationalen Lager"]],
             ["fpoe", "e) Aus welchem Lager kommt die heutige FPÖ?", ["aus dem deutschnationalen (»dritten«) Lager", "aus dem christlichsozialen Lager", "aus dem sozialdemokratischen Lager"]],
             ["wer", "f) Wer stand vor allem hinter der Sozialdemokratie?", ["Arbeiterinnen und Arbeiter", "Großgrundbesitzer", "Bauern und Adel"]],
             ["gruend", "g) Was muss man tun, um in Österreich eine Partei zu gründen?",
              ["die Satzung beim Innenministerium hinterlegen", "1000 Unterschriften sammeln", "den Bundespräsidenten um Erlaubnis bitten"]],
             ["klub", "h) Ab wie vielen Abgeordneten derselben Partei gibt es im Nationalrat einen Klub?", ["5", "1", "10"]]],
  "chk": {"lueger": {"sel": "Karl Lueger"}, "adler": {"sel": "Victor Adler"}, "oevp": {"sel": "aus dem christlichsozialen Lager"},
          "fpoe": {"sel": "aus dem deutschnationalen (»dritten«) Lager"}, "wer": {"sel": "Arbeiterinnen und Arbeiter"},
          "gruend": {"sel": "die Satzung beim Innenministerium hinterlegen"}, "klub": {"sel": "5"}},
  "fb": {"lueger": {"Victor Adler": "Adler war Arzt und Sozialdemokrat – kein Bürgermeister.", "Georg von Schönerer": "Schönerer war deutschnational und auch Antisemit, aber nie Bürgermeister."},
         "adler": {"Karl Lueger": "Lueger war Christlichsozialer.", "Karl von Vogelsang": "Vogelsang gründete mit Lueger die Christlichsoziale Partei."},
         "oevp": {"aus dem sozialdemokratischen Lager": "Aus diesem Lager kommt die SPÖ.", "aus dem deutschnationalen Lager": "Aus diesem Lager kommt die FPÖ."},
         "fpoe": {"aus dem christlichsozialen Lager": "Daraus kommt die ÖVP.", "aus dem sozialdemokratischen Lager": "Daraus kommt die SPÖ."},
         "wer": {"Großgrundbesitzer": "Die hatten schon im Kurienwahlrecht viel Macht.", "Bauern und Adel": "Bauern standen eher bei den Christlichsozialen."},
         "gruend": {"1000 Unterschriften sammeln": "Unterschriften braucht man, um bei einer Wahl antreten zu dürfen – nicht zum Gründen.",
                    "den Bundespräsidenten um Erlaubnis bitten": "Parteien gründet man frei – das ist ein Grundrecht. Man meldet sie nur an."},
         "klub": {"1": "Ein Abgeordneter allein bildet keinen Klub.", "10": "Es reichen weniger."}},
  "sol": [["Lösung", ["Tabelle (Beispiel): Liberale/Deutschnationale – wohlhabendes Bürgertum der Städte, Vereine – Freiheit für Wirtschaft und Einzelne; später: Anschluss an das Deutsche Reich, Antisemitismus – heute FPÖ (»drittes Lager«, FPÖ 1956 gegründet).",
                      "Christlichsoziale – Kleinbürgertum, Bauern, katholische Vereine – Christentum im öffentlichen Leben, soziale Reformen – heute ÖVP (gegründet 1945).",
                      "Sozialdemokraten – Arbeiterinnen und Arbeiter – gleiches Wahlrecht, Arbeiterschutz, Bildung für alle – heute SPÖ (1945 neu gegründet).",
                      "b) Karl Lueger · c) Victor Adler · d) christlichsozial · e) deutschnational (»drittes Lager«) · f) Arbeiterinnen und Arbeiter",
                      "g) Satzung beim Innenministerium hinterlegen (Buch S. 31) · h) 5 (Buch S. 32)"]]],
  "tipps": ["Denk an drei Gruppen von Menschen um 1900: Bürger der Städte, gläubige Katholiken, Arbeiter in den Fabriken.",
            "k2",
            "Lies im Buch S. 27 »Von liberal zu deutschnational«, S. 29 die zwei Abschnitte zu Christlichsozialen und Sozialdemokraten und S. 31 »Wie entsteht eine Partei?«."],
  "tip": ["Drei Lager", "theorie.html#lager"]},

 # --------------------------------------------------------------- Stunde 3
 {"id": "a3", "hd": "B", "niveau": 2, "ziel": 3, "nr": 4, "title": "Links, rechts, liberal – und was sagen die Parteien?", "src": "Buch S. 32–35", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 8, "marke": "SELBSTSTUDIUM",
  "q": "a) bis e) machst du vor dem Referat. f) und g) füllst du während und gleich nach dem REFERAT aus (Hörbogen).",
  "hint": "Wo steht's? Buch S. 32–33 und Theorie Teil 4. Für die Parteien: Buch S. 35 und Theorie Teil 5.",
  "type": "multi",
  "fields": [["herkunft", "a) Woher kommen die Wörter »links« und »rechts« in der Politik?",
              ["von der Sitzordnung in der französischen Nationalversammlung 1789", "von der Sitzordnung im Reichsrat in Wien 1861", "aus dem Militär: linke und rechte Flanke"]],
             ["egal", "b) Was heißt »egalitär«?", ["alle sollen möglichst gleiche Rechte und Chancen haben", "nur die Besten sollen entscheiden", "das eigene Volk kommt zuerst"]],
             ["rechts", "c) Wofür steht »rechts« laut Buch S. 32?", ["elitär, konservativ, nationalistisch", "egalitär, progressiv, internationalistisch", "liberal, ökologisch, pro-europäisch"]],
             ["liberal", "d) Warum passt der Liberalismus schlecht auf die Links-rechts-Linie?",
              ["Er will gleiche Rechte für alle – und gleichzeitig, dass sich Leistung lohnt", "Er ist gegen jede Regel und jedes Gesetz", "Es gibt ihn erst seit 2012"]],
             ["anzahl", "e) Wie viele Parteien haben derzeit einen Klub im Nationalrat?", ["fünf", "sechs", "vier"]],
             ["frage", "f) REFERAT: Welche Frage hat der Referent allen Parteivertretern gestellt? (kurz)"],
             ["passt", "g) REFERAT: Bei welcher Partei passte die Antwort am besten zu ihrer Beschreibung im Buch S. 35? Begründe in 1–2 Sätzen."]],
  "chk": {"herkunft": {"sel": "von der Sitzordnung in der französischen Nationalversammlung 1789"},
          "egal": {"sel": "alle sollen möglichst gleiche Rechte und Chancen haben"},
          "rechts": {"sel": "elitär, konservativ, nationalistisch"},
          "liberal": {"sel": "Er will gleiche Rechte für alle – und gleichzeitig, dass sich Leistung lohnt"},
          "anzahl": {"sel": "fünf"},
          "frage": {"kw": [["Frage", r"\w{3,}"]], "man": True, "kurz": True},
          "passt": {"kw": [["Partei", r"[öo]vp|sp[öo]|fp[öo]|neos|gr[üu]n"], ["Begründung", r"weil|denn|da |passt|buch|beschreib|steht"]], "need": 2, "man": True}},
  "fb": {"herkunft": {"von der Sitzordnung im Reichsrat in Wien 1861": "Die Wörter sind älter und kommen aus Frankreich.",
                      "aus dem Militär: linke und rechte Flanke": "Klingt logisch – stimmt aber nicht. Es geht um Sitzplätze in einem Parlament."},
         "egal": {"nur die Besten sollen entscheiden": "Das wäre »elitär« – das Gegenteil.", "das eigene Volk kommt zuerst": "Das ist »nationalistisch«."},
         "rechts": {"egalitär, progressiv, internationalistisch": "Das sind die Begriffe für links.", "liberal, ökologisch, pro-europäisch": "Diese Begriffe stehen im Buch bei NEOS und Grünen, nicht bei »rechts«."},
         "liberal": {"Er ist gegen jede Regel und jedes Gesetz": "Liberale wollen einen Rechtsstaat – mit möglichst viel Freiheit darin.", "Es gibt ihn erst seit 2012": "2012 wurde NEOS gegründet. Den Liberalismus gibt es seit dem 19. Jahrhundert."},
         "anzahl": {"sechs": "Die KPÖ steht im Buch, hat aber keinen Sitz im Nationalrat.", "vier": "Zähl noch einmal: FPÖ, ÖVP, SPÖ, NEOS, Grüne."}},
  "sol": [["Lösung", ["a) französische Nationalversammlung 1789: links saßen die Revolutionären, rechts die Königstreuen (Buch S. 32).",
                      "b) gleiche Rechte und Chancen · c) elitär, konservativ, nationalistisch",
                      "d) Rechtsgleichheit (egalitär) und Leistung soll Unterschiede machen dürfen (elitär) – darum eine eigene Richtung (Buch S. 33).",
                      "e) fünf Klubs: FPÖ, ÖVP, SPÖ, NEOS, Grüne (dazu ein Abgeordneter ohne Klub, Stand Herbst 2026).",
                      "f) und g): hängen vom Referat ab – gut ist eine Antwort, die eine Partei nennt UND mit der Beschreibung im Buch S. 35 begründet."]]],
  "tipps": ["Links und rechts sind ursprünglich Sitzplätze. Und »liberal« heißt: möglichst viel Freiheit für jeden Einzelnen.",
            "k4",
            "Lies im Buch S. 32 »Was bedeutet rechts, links, liberal?« und S. 33 den Absatz zum Liberalismus."],
  "tip": ["Links, rechts, liberal", "theorie.html#richtung"]},

 # --------------------------------------------------------------- Stunde 4
 {"id": "a4", "hd": "C", "niveau": 2, "ziel": 4, "nr": 5, "title": "Faktencheck: KI-Antwort und Schulbuch auf dem Prüfstand", "src": "Buch S. 23–35", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 11, "marke": "SELBSTSTUDIUM",
  "q": "Ein Chatbot hat auf »Erklär mir die Parteien in Österreich« geantwortet (Beispiel, so ähnlich kommt es vor): "
       "»1. Frauen dürfen in Österreich erst seit 1945 wählen. 2. Die Sozialdemokraten wurden beim Parteitag in Hainfeld 1888/89 geeinigt. "
       "3. Im Nationalrat sitzen derzeit sechs Parteien, darunter die KPÖ. 4. Die FPÖ wurde schon im 19. Jahrhundert gegründet.« "
       "Finde die Fehler – ohne KI. Danach prüfst du eine Zeile aus dem Schulbuch (d) und zwei Aussagen über Quellen (e, f).",
  "hint": "Prüfe jeden Satz mit der Theorie: Wahlrecht (Teil 1), Lager (Teil 2), Parteien heute (Teil 5).",
  "type": "multi",
  "fields": [["wie", "a) Wie viele der vier Sätze sind falsch?", ["drei (Satz 1, 3 und 4)", "alle vier", "nur einer (Satz 1)"]],
             ["s3", "b) Verbessere Satz 3 in einem Satz."],
             ["s4", "c) Verbessere Satz 4 in einem Satz."],
             ["heer", "d) Im Buch S. 34 steht bei den Grünen »Nein« zu »Mehr Geld für das Bundesheer«. Im Juni 2025 nannte der Grünen-Abgeordnete David Stögmüller im Nationalrat den Anstieg des Heeresbudgets »richtig und wichtig« – er kritisierte aber, wofür das Geld ausgegeben wird. Welche Ampel bekommt die Buchzeile?",
              ["gelb – stark vereinfacht, Stand prüfen", "grün – stimmt genau so", "rot – frei erfunden"]],
             ["parl", "e) Welche Quelle ist am besten, wenn du wissen willst, was im Nationalrat wirklich gesagt wurde?",
              ["das Parlament selbst (Parlamentskorrespondenz, Protokolle)", "ein Wahlplakat der Partei", "ein Kommentar in sozialen Medien"]],
             ["umfrage", "f) In einer Umfrage liegt eine Partei bei 40 %. Was stimmt?",
              ["Eine Umfrage ist eine Momentaufnahme mit Schwankungsbreite – keine Wahl", "Die Partei hat damit 40 % der Sitze im Nationalrat", "Umfragen sind auf das Prozent genau"]]],
  "chk": {"wie": {"sel": "drei (Satz 1, 3 und 4)"},
          "s3": {"kw": [["fünf / 5", r"f(ü|ue)nf|\b5\b"], ["KPÖ nicht drin", r"kp(ö|oe)\s*(ist|sitzt)?\s*nicht|ohne\s*kp|nicht.{0,30}kp(ö|oe)|kp(ö|oe).{0,40}(nicht|kein)"]], "need": 1, "man": True,
                 "contra": [r"\bsechs\b|\b6\b.{0,10}partei"]},
          "s4": {"kw": [["1956 / 1955", r"19(55|56)|20\.\s*jahrhundert|nach dem (2\.|zweiten) weltkrieg"], ["Wurzeln / Lager", r"deutschnational|drittes lager|dritten lager|vdu|wurzel|lager"]], "need": 1, "man": True},
          "heer": {"sel": "gelb – stark vereinfacht, Stand prüfen"},
          "parl": {"sel": "das Parlament selbst (Parlamentskorrespondenz, Protokolle)"},
          "umfrage": {"sel": "Eine Umfrage ist eine Momentaufnahme mit Schwankungsbreite – keine Wahl"}},
  "fb": {"wie": {"alle vier": "Satz 2 stimmt: Hainfeld 1888/89 (Buch S. 30).", "nur einer (Satz 1)": "Schau dir auch Satz 3 und 4 genau an."},
         "heer": {"grün – stimmt genau so": "2025 hat ein Grünen-Abgeordneter dem Anstieg ausdrücklich zugestimmt. Ein glattes »Nein« passt nicht mehr.",
                  "rot – frei erfunden": "Erfunden ist es nicht – Ja/Nein-Tabellen vereinfachen stark, und Positionen ändern sich."},
         "parl": {"ein Wahlplakat der Partei": "Ein Plakat ist Werbung – es will überzeugen, nicht genau berichten.",
                  "ein Kommentar in sozialen Medien": "Ein Kommentar ist eine Meinung – oft ohne Beleg."},
         "umfrage": {"Die Partei hat damit 40 % der Sitze im Nationalrat": "Sitze gibt es nur nach einer echten Wahl.",
                     "Umfragen sind auf das Prozent genau": "Umfragen haben eine Schwankungsbreite von etwa 2 bis 3 Prozentpunkten."}},
  "sol": [["Lösung", ["a) Drei Sätze sind falsch – nur Satz 2 stimmt.",
                      "Satz 1: Frauen wählen seit 1918 (erste Wahl Februar 1919).",
                      "b) Satz 3: Im Nationalrat sitzen fünf Parteien (FPÖ, ÖVP, SPÖ, NEOS, Grüne); die KPÖ ist nicht im Nationalrat.",
                      "c) Satz 4: Die FPÖ wurde 1956 gegründet; ihre Wurzeln liegen im deutschnationalen (»dritten«) Lager des 19. Jahrhunderts.",
                      "d) gelb: Die Tabelle vereinfacht stark und ist nicht datiert. Zustimmung zur Erhöhung (2025) heißt noch nicht Zustimmung zu allen Ausgaben.",
                      "e) Parlament (Parlamentskorrespondenz Nr. 564 vom 18.06.2025) · f) Momentaufnahme mit Schwankungsbreite."]]],
  "tipps": ["Drei Dinge prüfen: Jahr des Frauenwahlrechts, Zahl der Parteien im Nationalrat, Gründungsjahr der FPÖ.",
            "k6",
            "Lies im Buch S. 23 die Zeitleiste und S. 33 »Das Neue Österreich …« in der Randspalte. Die KPÖ steht auf S. 35 – prüfe, ob sie im Nationalrat sitzt (Theorie Teil 5)."],
  "tip": ["Faktencheck", "theorie.html#pruefen"]},

 {"id": "a5", "hd": "A", "niveau": 1, "ziel": 2, "nr": 6, "title": "Mindmap mit der Hand: Die Einheit auf einem Blatt", "src": "Buch S. 23–35", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 7, "marke": "SELBSTSTUDIUM",
  "type": "sketch",
  "q": "Zeichne auf ein Blatt eine Mindmap. In der Mitte: »Wahlrecht und Parteien«. Drei Äste: 1 Wahlrecht (drei Jahreszahlen mit Stichwort), "
       "2 Drei Lager → Parteien heute, 3 Links, rechts, liberal (je ein Beispiel-Begriff). Datum oben drauf, fotografieren, ab in die Mappe. Dann schreibst du deinen wichtigsten Satz.",
  "hint": "Wo steht's? Theorie »Das Wichtigste in 5 Sätzen« und deine Tabelle aus Aufgabe 3.",
  "fields": [["satz", "a) Dein wichtigster Satz aus dieser Einheit (1 Satz)"]],
  "chk": {"satz": {"kw": [["Satz", r"\w{4,}.*\w{4,}"]], "man": True}},
  "sol": [["Was gut ist", ["Mindmap mit drei Ästen, je mindestens zwei richtigen Stichworten (z. B. 1907 Männer, 1918 Frauen, 2007 ab 16; christlichsozial → ÖVP …; egalitär, konservativ, liberal).",
                           "Der Satz ist fachlich richtig und in eigenen Worten."]]],
  "tipps": ["Fang mit den Jahreszahlen an, die du dir schon gemerkt hast. Dann die drei Lager.",
            "k8",
            "Blättere im Buch S. 23 (Zeitleiste), S. 27 (drei Lager) und S. 32 (links, rechts) durch."],
  "tip": ["Kurz & knapp", "theorie.html#kurz"]},

 {"id": "ziele", "nr": 7, "title": "Ziele erreicht?", "src": "Buch S. 23–35", "own": True, "tag": "Selbsteinschätzung", "h": 4, "zeit": 1, "selbst": True,
  "q": "Kreuz ehrlich an, wie gut du deine Ziele erreicht hast. Es gibt keine Punkte. Bei »noch nicht«: Lies den Theorie-Teil und die Buchseite daneben noch einmal.",
  "hint": "Das ist für dich und für Prof. HOLZER – damit er weiß, was er noch einmal erklären soll.",
  "type": "multi",
  "fields": [],
  "chk": {}, "sol": [["Selbsteinschätzung", ["Keine Musterlösung – bei »noch nicht« den Theorie-Teil wiederholen."]]],
  "tipps": [], "tip": ["Kurz & knapp", "theorie.html#kurz"]},

 # --------------------------------------------------------------- Zusatz
 {"id": "z1", "hd": "C", "niveau": 2, "ziel": 4, "nr": 8, "title": "Forschung: Wählen 16-Jährige wirklich seltener?", "src": "Uni Wien 2014 · Buch S. 26", "own": True, "tag": "Zusatz", "h": 0, "zeit": 10, "marke": "ZUSATZ",
  "q": "Eva Zeglovits und Julian Aichholzer (Universität Wien) haben 2014 in einer Fachzeitschrift ausgewertet, wer wirklich wählen ging – nicht in einer Umfrage, sondern mit den Wählerverzeichnissen. "
       "Wiener Gemeinderatswahl 2010: 16–17 Jahre 64,2 %, 18–20 Jahre 56,3 %. Krems 2012: 16–17 Jahre 56,3 %, 18–20 Jahre 46,3 %.",
  "hint": "Prozentpunkte = einfach die Differenz der zwei Prozentzahlen.",
  "type": "multi",
  "fields": [["wer", "a) Wer ging in beiden Städten öfter wählen?", ["die 16- bis 17-Jährigen", "die 18- bis 20-Jährigen", "beide gleich oft"]],
             ["pp", "b) Um wie viele Prozentpunkte lagen die 16- bis 17-Jährigen in Krems vorne?"],
             ["grenze", "c) Was ist eine Grenze dieser Studie?", ["nur zwei Gemeindewahlen in zwei Städten – nicht ganz Österreich", "es wurden nur 10 Personen gezählt", "die Wahl fand im Ausland statt"]],
             ["meinung", "d) Wählen mit 16 – deine Meinung: Behauptung (1 Satz) · ein Beleg · das stärkste Gegenargument · deine Antwort darauf. Ohne KI."]],
  "chk": {"wer": {"sel": "die 16- bis 17-Jährigen"},
          "pp": {"num": 10, "unit": "", "tol": 0.2, "nicht": [r"\boder\b"]},
          "grenze": {"sel": "nur zwei Gemeindewahlen in zwei Städten – nicht ganz Österreich"},
          "meinung": {"kw": [["Behauptung", r"\w{4,}"], ["Gegenargument", r"aber|gegen|jedoch|allerdings|kritik|andere"]], "need": 2, "man": True}},
  "fb": {"pp": [[46.3, "Gefragt ist der Abstand – nicht eine der beiden Zahlen."], [102.6, "Nicht zusammenzählen: abziehen."]],
         "grenze": {"es wurden nur 10 Personen gezählt": "Es waren mehrere tausend (Wien über 5000, Krems über 3000).",
                    "die Wahl fand im Ausland statt": "Wien und Krems liegen in Österreich."}},
  "sol": [["Lösung", ["a) die 16- bis 17-Jährigen · b) 56,3 − 46,3 = 10 Prozentpunkte",
                      "c) nur zwei Gemeinde- bzw. Stadtwahlen; ob es bei Nationalratswahlen genauso ist, sagt die Studie allein nicht.",
                      "d) offen – bewertet wird: klare Behauptung, ein Beleg, ein echtes Gegenargument, eine Antwort darauf."]]],
  "tipps": [], "tip": ["Für Schnelle", "theorie.html#schnelle"]},

 {"id": "z2", "hd": "C", "niveau": 2, "ziel": 2, "nr": 9, "title": "Hainfeld 1889 – was davon gilt heute noch?", "src": "Buch-Aufgabe S. 30", "own": False, "tag": "Zusatz", "h": 0, "zeit": 8, "marke": "ZUSATZ",
  "q": "Im Buch S. 30 steht links ein Auszug aus dem Hainfelder Programm der Sozialdemokraten von 1889. Lies ihn. Welche Forderungen von damals sind heute selbstverständlich, über welche wird noch gestritten?",
  "hint": "Denk an Wahlrecht, Arbeitszeit, Kinderarbeit und Schule.",
  "type": "multi",
  "fields": [["erfuellt", "a) Nenne eine Forderung von damals, die heute erfüllt ist – und woran man das sieht."],
             ["offen", "b) Nenne eine Forderung, über die heute noch diskutiert wird (1–2 Sätze)."]],
  "chk": {"erfuellt": {"kw": [["Forderung", r"wahlrecht|kinderarbeit|arbeitszeit|schul|unterricht|bildung|arbeiterschutz|frauen|gleich"]], "need": 1, "man": True},
          "offen": {"kw": [["Thema", r"\w{4,}"]], "man": True}},
  "sol": [["Was gut ist", ["a) z. B. allgemeines, gleiches Wahlrecht für alle (seit 1918), Verbot der Kinderarbeit, unentgeltliche Pflichtschule.",
                           "b) z. B. Arbeitszeit (Arbeitszeitverkürzung), Trennung von Kirche und Staat, kostenlose höhere Bildung – mit Begründung."]]],
  "tipps": [], "tip": ["Drei Lager", "theorie.html#lager"]},

 {"id": "z3", "hd": "B", "niveau": 2, "ziel": 3, "nr": 10, "title": "Kreativ: Wahlplakat für eine erfundene Partei", "src": "nach Buch-Aufgabe S. 34", "own": True, "tag": "Zusatz", "h": 0, "zeit": 15, "marke": "ZUSATZ",
  "type": "sketch",
  "q": "Erfinde eine Partei – keine echte! Gestalte ein Plakat auf A4 mit der Hand: Name, Farbe, ein Slogan und drei Positionen zu Bildung, Umwelt und Sicherheit. "
       "Ordne deine Partei auf der Links-rechts-Linie ein (Pfeil am Rand). Foto hochladen. KI ist nur für Slogan-Ideen erlaubt – dann schreib dazu, was du gefragt und was du geändert hast.",
  "hint": "Ein gutes Plakat versteht man in 5 Sekunden.",
  "fields": [["name", "a) Name deiner erfundenen Partei"],
             ["positionen", "b) Deine drei Positionen in Stichworten (Bildung · Umwelt · Sicherheit)"]],
  "chk": {"name": {"kw": [["Name", r"\w{2,}"]], "man": True, "kurz": True},
          "positionen": {"kw": [["Bildung", r"bild|schul|lern"], ["Umwelt", r"umwelt|klima|natur|energie|öko|oeko"], ["Sicherheit", r"sicher|heer|polizei|schutz|verteid"]], "need": 3, "man": True}},
  "sol": [["Bewertungsraster (freiwillig, keine Note)", ["Name und Slogan passen zusammen · drei klare Positionen · Einordnung begründbar · lesbar aus 2 m · keine echte Partei, keine echte Person."]]],
  "tipps": [], "tip": ["Links, rechts, liberal", "theorie.html#richtung"]},

 {"id": "z4", "hd": "B", "niveau": 2, "ziel": 3, "sim": ["mehrheit"], "nr": 11, "title": "Mehrheit gesucht: Wer kommt mit wem auf 92?", "src": "Buch S. 32 · Parlament", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8, "marke": "ZUSATZ",
  "q": "Der Nationalrat hat 183 Sitze (Mandate). Nach der Wahl 2024: FPÖ 57, ÖVP 51, SPÖ 41, NEOS 18, Grüne 16. Probier es mit dem Mehrheits-Rechner aus.",
  "hint": "Mehrheit = mehr als die Hälfte von 183.",
  "type": "multi",
  "fields": [["mehr", "a) Wie viele Mandate braucht man mindestens für eine Mehrheit?"],
             ["regierung", "b) Wie viele Mandate hatten ÖVP, SPÖ und NEOS zusammen nach der Wahl 2024?"],
             ["neos", "c) Der NEOS-Klub hat heute nur noch 17 Abgeordnete. Warum?",
              ["Ein Abgeordneter wurde 2026 aus Klub und Partei ausgeschlossen – sein Mandat behält er", "NEOS hat einen Sitz an eine andere Partei verkauft", "Es gab eine Nachwahl in einem Wahlkreis"]],
             ["zwei", "d) Wie viele Mandate braucht man für eine Zweidrittelmehrheit, wenn alle 183 Abgeordneten da sind?"]],
  "chk": {"mehr": {"num": 92, "unit": "", "tol": 0, "nicht": [r"%", r"\boder\b"]},
          "regierung": {"num": 110, "unit": "", "tol": 0, "nicht": [r"%", r"\boder\b"]},
          "neos": {"sel": "Ein Abgeordneter wurde 2026 aus Klub und Partei ausgeschlossen – sein Mandat behält er"},
          "zwei": {"num": 122, "unit": "", "tol": 0, "nicht": [r"%", r"\boder\b"]}},
  "fb": {"mehr": [[183, "Das wären alle. Mehr als die Hälfte genügt."], [100, "Mit 100 hätte man eine Mehrheit – gefragt ist das Minimum."]],
         "regierung": [[92, "Das sind nur ÖVP und SPÖ. NEOS gehört auch zur Regierung."]],
         "neos": {"NEOS hat einen Sitz an eine andere Partei verkauft": "Mandate kann man nicht verkaufen – sie gehören der gewählten Person.",
                  "Es gab eine Nachwahl in einem Wahlkreis": "Nachwahlen gibt es beim Nationalrat so nicht."},
         "zwei": [[92, "Das ist die einfache Mehrheit. Zwei Drittel sind mehr."], [183, "Zwei Drittel, nicht alle."]]},
  "sol": [["Lösung", ["a) 92 (183 : 2 = 91,5 → mehr als die Hälfte = 92) · b) 51 + 41 + 18 = 110",
                      "c) Veit Dengler wurde am 09.07.2026 aus Klub und Partei ausgeschlossen; Mandate gehören den Abgeordneten, er sitzt ohne Klub weiter.",
                      "d) 183 · 2/3 = 122"]]],
  "tipps": [], "tip": ["Parteien heute", "theorie.html#heute"]},
]
# Kompetenzmodell (Stephan 20.11.2026): Ziele mit Handlungsdimension A/B/C; »Ziele erreicht?« am Ende des Arbeitsblatts
ZIELE = [{"nr": 1, "hd": "A", "text": "Ich kann erklären, wie aus einem Wahlrecht für wenige reiche Männer das Wahlrecht für alle ab 16 wurde – mit den wichtigsten Jahreszahlen.", "theorie": "wahlrecht", "buch": "Buch S. 23–26"},
         {"nr": 2, "hd": "B", "text": "Ich kann die drei politischen Lager um 1900 beschreiben und den Parteien von heute zuordnen.", "theorie": "lager", "buch": "Buch S. 27–31"},
         {"nr": 3, "hd": "B", "text": "Ich kann Parteien mit links, rechts und liberal beschreiben und sagen, wo diese Einteilung an ihre Grenzen kommt.", "theorie": "richtung", "buch": "Buch S. 32–35"},
         {"nr": 4, "hd": "C", "text": "Ich kann Aussagen über Parteien mit Quellen prüfen und bewerten – Schulbuch, Parlament, Umfrage und KI-Antwort.", "theorie": "pruefen", "buch": "Buch S. 34"}]
GRADE = ["zur Gänze", "überwiegend", "noch nicht"]
_zt = [x for x in T if x["id"] == "ziele"][0]
_TEIL = {"wahlrecht": "Teil 1", "lager": "Teil 2", "richtung": "Teil 4", "pruefen": "Teil 6"}
_zt["fields"] = [["z%d" % z["nr"], f'{"abcd"[z["nr"] - 1]}) {z["hd"]} · {z["text"]} – nachlesen: Theorie {_TEIL[z["theorie"]]}, {z["buch"]}', list(GRADE), False] for z in ZIELE]
assert [t["nr"] for t in T] == list(range(1, 12))
PFLICHT = [t["nr"] for t in T if t["tag"] not in ("Zusatz", "Selbsteinschätzung") and not t.get("vorhersage")]
assert PFLICHT == [2, 3, 4, 5, 6], PFLICHT
BESPRECHEN = [2, 3, 4, 5]
_pf = [t for t in T if t["nr"] in PFLICHT]
assert sum(t["niveau"] == 1 for t in _pf) >= 2 and sum(t["niveau"] == 2 for t in _pf) >= 1
assert {t["hd"] for t in T if "hd" in t} == {"A", "B", "C"}
assert all(t.get("tipps") for t in _pf if t["niveau"] == 2)
assert all("hd" in t for t in T if t["id"] != "ziele")
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True
for _t in T:
    for _k in (_t["chk"] or {}):
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
        if len(_f) > 2: assert len(set(_f[2])) == len(_f[2]), (_t["id"], _f[0], "doppelte Option")
    for _k, _m in _t.get("fb", {}).items():
        if isinstance(_m, list):
            _c = _t["chk"][_k]; assert "num" in _c, (_t["id"], _k)
            for _w, _txt in _m: assert abs(_w - _c["num"]) > max(_c["tol"] or 0, abs(_c["num"]) * 0.02) * 1.5, (_t["id"], _k, _w, "Fehlwert zu nah an der Lösung")
            continue
        _opt = [f[2] for f in _t["fields"] if f[0] == _k][0]
        for _o in _m: assert _o in _opt, (_t["id"], _k, _o)
        assert _t["chk"][_k].get("sel") not in _m, (_t["id"], _k, "Rückmeldung für die richtige Antwort")
    _alle = [_t["q"], _t.get("hint", "")] + [z for _a, zz in _t["sol"] for z in zz] + [f[1] for f in _t["fields"]] + [o for f in _t["fields"] if len(f) > 2 for o in f[2]]
    for _x in _alle:
        for _z in "⇌√≈":
            assert _z not in _x, (_t["id"], _z, "Zeichen fehlt in der PDF-Schrift")
    assert len(_t.get("tipps", [])) in (0, 3), (_t["id"], "Tipp-Stufen: genau drei oder keine")

# Rechenkontrolle (vom Aufgabentext aus gerechnet)
assert round(56.3 - 46.3, 1) == 10.0
assert 183 // 2 + 1 == 92 and 51 + 41 + 18 == 110 and 51 + 41 + 17 == 109 and 183 * 2 // 3 == 122 and 183 * 2 % 3 == 0
assert 57 + 51 + 41 + 18 + 16 == 183 and 57 + 51 + 41 + 17 + 16 + 1 == 183

GRP = {1: STUNDENNAME[1] + " (Buch S. 23–26)",
       2: STUNDENNAME[2] + " (Buch S. 27–32)",
       3: STUNDENNAME[3] + " (Buch S. 32–35) · REFERAT",
       4: STUNDENNAME[4] + " (Buch S. 23–35)",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)"}

LERNZIELE_ALT = ["erklären, wie aus einem **Wahlrecht für wenige reiche Männer** das **Wahlrecht für alle ab 16** wurde – mit den wichtigsten **Jahreszahlen**",
             "die **drei politischen Lager** um 1900 beschreiben und sagen, welche **Parteien heute** aus ihnen kommen",
             "Parteien mit den Begriffen **links, rechts und liberal** beschreiben und sagen, wo diese Einteilung **an ihre Grenzen** kommt",
             "Aussagen über Parteien mit **Quellen prüfen** – Schulbuch, Parlament, Umfrage und KI-Antwort richtig einschätzen"]

LERNZIELE = [z["text"] for z in ZIELE]

WICHTIGSTE = ["Das Wahlrecht wurde in Etappen **erkämpft**: **1861** nur Männer mit Besitz, **1873** nur wer Steuer zahlt, **1907** alle Männer ab 24, **1918** auch die Frauen, **2007** alle ab **16**.",
              "**1933 bis 1945** gab es in Österreich **keine freien Wahlen** – Demokratie ist nicht selbstverständlich.",
              "Um 1900 entstanden **drei Lager**: **christlichsozial** (heute **ÖVP**), **sozialdemokratisch** (heute **SPÖ**) und **deutschnational** (heute **FPÖ**). **Grüne** (1986 im Parlament) und **NEOS** (2012 gegründet) kamen später dazu.",
              "**Parteien** sammeln Interessen, schreiben **Programme**, stellen Kandidaten auf und sitzen als **Klubs** (ab 5 Abgeordneten) im **Nationalrat**.",
              "**Links** heißt eher **egalitär**, **rechts** eher **konservativ**, **liberal** heißt möglichst viel **Freiheit** für den Einzelnen. Echte Parteien passen selten genau in eine Schublade – darum **Quellen prüfen**."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Kurienwahlrecht", "Wahlrecht ab 1861: Wähler in Gruppen (Kurien) nach Besitz eingeteilt; nur Männer mit Besitz, jede Kurie wählt ihre eigenen Abgeordneten"],
                ["Zensuswahlrecht", "Wahlrecht ab 1873: nur wer genug Steuer zahlt, darf wählen; die Stimme der Reichen zählt mehr"],
                ["allgemeines Wahlrecht", "alle Staatsbürger ab einem bestimmten Alter dürfen wählen – egal ob reich oder arm"],
                ["gleiches Wahlrecht", "jede Stimme zählt gleich viel"],
                ["direkt, geheim", "man wählt die Abgeordneten selbst (nicht über Wahlmänner) und niemand sieht, was man wählt"],
                ["aktives / passives Wahlrecht", "aktiv = wählen dürfen (heute ab 16) · passiv = gewählt werden dürfen (heute ab 18)"],
                ["Partei", "Zusammenschluss von Menschen mit gemeinsamen politischen Zielen; tritt bei Wahlen an und will Macht im Staat übernehmen"],
                ["Parteiprogramm", "schriftliche Grundsätze und Ziele einer Partei"],
                ["politisches Lager", "große Gruppe von Menschen und Vereinen mit derselben Weltanschauung, z. B. das christlichsoziale Lager"],
                ["Klub", "Zusammenschluss der Abgeordneten einer Partei im Nationalrat, ab 5 Abgeordneten"],
                ["Mandat", "Sitz im Parlament; der Nationalrat hat 183 Mandate"],
                ["Koalition", "Zusammenarbeit von zwei oder mehr Parteien, damit sie zusammen eine Mehrheit haben"],
                ["Parteienförderung", "Geld vom Staat für Parteien, damit sie arbeiten können und nicht von Spendern abhängig sind"],
                ["links / rechts", "Grundrichtungen aus der Sitzordnung 1789 – links eher egalitär, progressiv, internationalistisch; rechts eher elitär, konservativ, nationalistisch"],
                ["liberal", "möglichst viel Freiheit für den Einzelnen – in Wirtschaft und Gesellschaft"],
                ["egalitär / elitär", "egalitär: alle sollen gleiche Rechte und Chancen haben · elitär: Leistung und Herkunft dürfen Unterschiede machen"],
                ["konservativ / progressiv", "konservativ: Bewährtes bewahren · progressiv: Gesellschaft verändern, Neues durchsetzen"],
                ["Umfrage", "Befragung einer Stichprobe; Momentaufnahme mit Schwankungsbreite, keine Wahl"]]

# ---------------------------------------------------------------- Wiederholen
WEISST_DU_NOCH = {
    2: [("Was zählte beim Zensuswahlrecht?", "Die Steuer: Nur wer genug zahlte, durfte wählen."),
        ("Seit wann dürfen Frauen in Österreich wählen?", "Seit 1918 (erste Wahl im Februar 1919)."),
        ("Ab welchem Alter darfst du heute wählen?", "Ab 16 – seit 2007.")],
    3: [("Aus welchem Lager kommt die ÖVP?", "Aus dem christlichsozialen Lager."),
        ("Wer einigte die Sozialdemokraten in Hainfeld?", "Victor Adler (1888/89)."),
        ("Ab wie vielen Abgeordneten gibt es einen Klub?", "Ab 5.")],
    4: [("Woher kommen links und rechts?", "Von der Sitzordnung in der französischen Nationalversammlung 1789."),
        ("Was heißt egalitär?", "Alle sollen gleiche Rechte und Chancen haben."),
        ("Wie viele Parteien haben einen Klub im Nationalrat?", "Fünf.")],
}

STOPPFRAGEN = {
    "wahlrecht": [("Warum war das Wahlrecht von 1907 noch nicht »allgemein«?", "Frauen durften nicht wählen."),
                  ("Was war 1933 bis 1945?", "Keine freien Wahlen – erst Diktatur in Österreich, dann NS-Herrschaft.")],
    "lager": [("Welche drei Lager gab es um 1900?", "Liberal/deutschnational, christlichsozial, sozialdemokratisch."),
              ("Welches Lager lebt in der FPÖ weiter?", "Das deutschnationale (»dritte«) Lager.")],
    "partei": [("Wie gründet man eine Partei?", "Satzung beim Innenministerium hinterlegen."),
               ("Warum bekommen Parteien Geld vom Staat?", "Damit sie arbeiten können und nicht von großen Spendern abhängig sind.")],
    "richtung": [("Was heißt konservativ?", "Bewährtes bewahren."),
                 ("Warum ist liberal weder links noch rechts?", "Gleiche Rechte für alle (egalitär), aber Leistung soll Unterschiede machen dürfen (elitär).")],
    "heute": [("Welche Parteien bilden seit März 2025 die Regierung?", "ÖVP, SPÖ und NEOS."),
              ("Wie viele Mandate braucht man für eine Mehrheit?", "92 von 183.")],
    "pruefen": [("Welche vier Fragen stellst du an jede Quelle?", "Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere?"),
                ("Ist eine Umfrage eine Wahl?", "Nein – eine Momentaufnahme mit Schwankungsbreite.")],
}

# ABCD-Fragen für »Weißt du noch?« (Frage, richtig, [drei falsche], Erklärung)
WDN_ABCD = {
    2: [("Was zählte beim Zensuswahlrecht ab 1873?", "die Steuer, die man zahlt", ["das Alter", "die Schulbildung", "das Geschlecht allein"], "Nur wer genug Steuer zahlte, durfte wählen – etwa 6 von 100 Männern."),
        ("Seit wann dürfen Frauen in Österreich wählen?", "seit 1918", ["seit 1907", "seit 1945", "seit 1971"], "Seit 1918. 1971 kam das Frauenwahlrecht in der Schweiz."),
        ("Was war 1933 bis 1945?", "keine freien Wahlen", ["Wählen ab 16", "Frauenwahlrecht", "Briefwahl"], "Diktatur in Österreich, danach NS-Herrschaft.")],
    3: [("Aus welchem Lager kommt die heutige ÖVP?", "christlichsozial", ["sozialdemokratisch", "deutschnational", "liberal"], "Christlichsoziale Partei (1891) → ÖVP (1945)."),
        ("Wer einigte die Sozialdemokraten 1888/89 in Hainfeld?", "Victor Adler", ["Karl Lueger", "Georg von Schönerer", "Franz Joseph I."], "Victor Adler, ein Arzt."),
        ("Ab wie vielen Abgeordneten bildet eine Partei einen Klub?", "5", ["1", "10", "20"], "Ab 5 Abgeordneten derselben Partei.")],
    4: [("Woher kommen die Wörter links und rechts?", "Sitzordnung Frankreich 1789", ["Militär-Flanken", "Reichsrat Wien 1861", "Straßenverkehr"], "In der französischen Nationalversammlung 1789."),
        ("Was heißt egalitär?", "gleiche Rechte und Chancen für alle", ["nur die Besten entscheiden", "das eigene Volk zuerst", "Bewährtes bewahren"], "Egalitär ist ein Begriff, der eher links steht."),
        ("Wie viele Parteien haben einen Klub im Nationalrat?", "fünf", ["vier", "sechs", "sieben"], "FPÖ, ÖVP, SPÖ, NEOS, Grüne.")],
}
VERMUTUNG_ABCD = {}
for _n, _qs in list(WDN_ABCD.items()):
    for _q in _qs: assert len(_q) == 4 and len(set([_q[1]] + _q[2])) == 4, _q

# Mitarbeits-Check (10 Fragen aus Pflichtstoff, Bereiche mit n Fragen)
CHECK = [
    {"thema": "Wahlrecht", "n": 3, "fragen": [
        ("w1", "Was zählte beim Zensuswahlrecht (ab 1873)?", "die Steuer, die man zahlt", ["das Alter allein", "die Schulnote", "der Wohnort"], "S. 24"),
        ("w2", "Seit wann dürfen Frauen in Österreich wählen?", "seit 1918", ["seit 1907", "seit 1945", "seit 1971"], "S. 25"),
        ("w3", "Was brachte das Jahr 1907?", "allgemeines, gleiches Wahlrecht für Männer ab 24", ["Wählen ab 16", "Frauenwahlrecht", "Briefwahl"], "S. 25"),
        ("w4", "Seit wann darf man in Österreich ab 16 wählen?", "seit 2007", ["seit 1918", "seit 1992", "seit 2020"], "S. 26"),
        ("w5", "Was war in Österreich von 1933 bis 1945?", "keine freien Wahlen", ["Wählen ab 18", "nur Briefwahl", "Wahlpflicht für alle"], "S. 25")]},
    {"thema": "Drei Lager", "n": 3, "fragen": [
        ("l1", "Aus welchem Lager kommt die ÖVP?", "christlichsozial", ["sozialdemokratisch", "deutschnational", "kommunistisch"], "S. 29"),
        ("l2", "Aus welchem Lager kommt die FPÖ?", "deutschnational (»drittes Lager«)", ["christlichsozial", "sozialdemokratisch", "ökologisch"], "S. 27"),
        ("l3", "Wer stand vor allem hinter der Sozialdemokratie?", "Arbeiterinnen und Arbeiter", ["Großgrundbesitzer", "der Adel", "die Kirche"], "S. 29–30"),
        ("l4", "Wer einigte die Sozialdemokraten 1888/89 in Hainfeld?", "Victor Adler", ["Karl Lueger", "Georg von Schönerer", "Karl von Vogelsang"], "S. 29–30")]},
    {"thema": "Parteien", "n": 2, "fragen": [
        ("p1", "Ab wie vielen Abgeordneten bildet eine Partei im Nationalrat einen Klub?", "5", ["1", "10", "92"], "S. 32"),
        ("p2", "Wie gründet man in Österreich eine Partei?", "Satzung beim Innenministerium hinterlegen", ["1000 Unterschriften sammeln", "Bundespräsident muss zustimmen", "eine Wahl gewinnen"], "S. 31"),
        ("p3", "Wie viele Mandate hat der Nationalrat?", "183", ["100", "92", "250"], "S. 32")]},
    {"thema": "Links, rechts, liberal", "n": 2, "fragen": [
        ("r1", "Woher kommen die Wörter links und rechts?", "Sitzordnung der französischen Nationalversammlung 1789", ["Reichsrat Wien 1861", "Militär-Flanken", "Straßenverkehrsordnung"], "S. 32"),
        ("r2", "Was heißt »konservativ«?", "Bewährtes bewahren", ["alles verändern", "alle sollen gleich sein", "nur die Besten entscheiden"], "S. 32"),
        ("r3", "Was heißt »liberal«?", "möglichst viel Freiheit für den Einzelnen", ["möglichst viel Staat", "das eigene Volk zuerst", "Rückkehr zur Monarchie"], "S. 33")]},
]
assert sum(g["n"] for g in CHECK) == 10 and all(g["n"] <= len(g["fragen"]) for g in CHECK)
for _g in CHECK:
    for _q in _g["fragen"]: assert len(set([_q[2]] + _q[3])) == 4, _q
CHECK_KEY = "26-27-2AK-K6-7-check"
CHECK_CODE = "1907"   # Startcode – steht nur als Prüfsumme in der Seite; Stephan zeigt ihn am Beamer

PARTNERCHECK = []

STOLPERSTEINE = [("»Seit 1907 dürfen alle wählen«",
                  "1907 = **allgemeines** Wahlrecht nur für **Männer** ab 24. Frauen erst **1918**. Aufgabe 2 h)."),
                 ("»Das Buch sagt 21 – also war das Wahlalter 1919 21«",
                  "Für die Wahl **1919** galt **20** (politik-lexikon.at, Demokratiezentrum). Das Buch ist hier ungenau. Aufgabe 2 i) als Quellenkritik nutzen."),
                 ("»Die FPÖ gibt es seit dem 19. Jahrhundert« / »ÖVP = Christlichsoziale Partei«",
                  "Die **Lager** sind alt, die **Parteien** jünger: ÖVP und SPÖ **1945**, FPÖ **1956** (Vorgänger VdU 1949). Aufgabe 5 c)."),
                 ("»Die KPÖ sitzt im Nationalrat« (Buch S. 35 zeigt sie)",
                  "Die KPÖ hat **keinen Sitz** im Nationalrat (Wahl 2024: unter 4 %). Fünf Klubs: FPÖ, ÖVP, SPÖ, NEOS, Grüne. Aufgabe 4 e)."),
                 ("»Rechts = rechtsextrem« / »links = linksextrem«",
                  "Buch S. 32: Es gibt eine Skala **linksextrem – linksradikal – links – Mitte – rechts – rechtsradikal – rechtsextrem**. Demokratische Parteien links und rechts stehen auf dem Boden der Verfassung. Extremismus ist eine eigene Einheit (Buch S. 135).")]

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 20.11.2026)
QUELLEN = [
 ("W1", "Parlamentskorrespondenz Nr. 361 (27.04.2026): Wählen mit 16", "Parlament Österreich",
  "https://www.parlament.gv.at/aktuelles/pk/jahr_2026/pk0361", "Wahlrechtsreform 2007: Wahlalter 16, Briefwahl, 5-jährige Periode, passives Wahlalter 18; erste Bundeswahl ab 16 im Herbst 2008", "Seite geöffnet"),
 ("W2", "Österreich 1918plus: 1919 – Die ersten Wählerinnen", "politik-lexikon.at (Demokratiezentrum Wien)",
  "https://www.politik-lexikon.at/oesterreich1918plus/1919/", "aktives Wahlalter 1919: 20 Jahre", "Seite geöffnet"),
 ("W3", "Mehr als ein Kreuzerl – wie sich unser Wahlsystem entwickelt hat (12.09.2024, einfache Sprache)", "Parlament Österreich",
  "https://www.parlament.gv.at/aktuelles/news/in-einfacher-sprache/MehrAlsEinKreuzerl-Wie-sich-unser-Wahlsystem-entwickelt-hat/", "1907 Männer ab 24; Frauen 11 Jahre später; 1970 183 Mandate; 2007 Wählen ab 16, Briefwahl für alle", "Seite geöffnet"),
 ("W4", "Zeglovits, E. & Aichholzer, J. (2014): Are People More Inclined to Vote at 16 than at 18? Journal of Elections, Public Opinion and Parties 24(3), 351–361", "Universität Wien, Fachzeitschrift",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC4864896", "Wien 2010: 16–17 J. 64,2 %, 18–20 J. 56,3 %; Krems 2012: 56,3 % gegen 46,3 %; Daten aus Wählerverzeichnissen", "Artikel geöffnet"),
 ("W5", "Parlamentskorrespondenz Nr. 564 (18.06.2025): Doppelbudget 2025/26 – steigende Verteidigungsausgaben", "Parlament Österreich",
  "https://www.parlament.gv.at/aktuelles/pk/jahr_2025/pk0564", "UG 14: 4,39 Mrd. € (2025), 4,76 Mrd. € (2026); Stögmüller (Grüne): Anstieg »richtig und wichtig«, Kritik an Prioritäten; Abstimmung nicht angegeben", "Seite geöffnet"),
 ("W6", "SPÖ: Babler-Rückzug (06.10.2026)", "ORF",
  "https://orf.at/stories/3444268/", "Babler gibt Vorsitz ab; ab 2027 Kucher und Holzleitner übergangsweise; Marterbauer soll Vizekanzler werden; Parteitag im Frühjahr 2027", "Seite geöffnet"),
 ("W7", "Nach Babler-Rückzug: So geht es bei der SPÖ weiter (05.10.2026)", "Salzburg24 (APA)",
  "https://www.salzburg24.at/news/oesterreich/nach-babler-rueckzug-so-geht-es-bei-der-spoe-weiter-art-340221", "Zeitplan offen, abhängig von Marterbauers Gesundheit; außerordentlicher Parteitag Frühjahr 2027", "Seite geöffnet"),
 ("W8", "NEOS schließt Veit Dengler aus Klub und Partei aus (09.07.2026)", "ORF",
  "https://orf.at/stories/3435881", "Ausschluss aus Klub und Partei", "laut Prüfbericht K7 v1 geöffnet; Klubstand 17 auf parlament.gv.at bestätigt"),
 ("W9", "Abgeordnete zum Nationalrat – NEOS (zuletzt geändert 29.10.2026)", "Parlament Österreich",
  "https://www.parlament.gv.at/dokument/recherchieren/personen/nationalrat/BEBILD_MIT_NR_N.pdf", "17 NEOS-Abgeordnete", "PDF geöffnet"),
 ("W10", "70 Jahre FPÖ (03.04.2026)", "news.at",
  "https://www.news.at/politik/70-jahre-fpoe-2026", "Gründungsparteitag 7. April 1956; Zusammenschluss VdU und Freiheitspartei 1955; erster Obmann Anton Reinthaller", "Seite geöffnet"),
 ("W11", "Wahltrend Österreich (Stand 19.11.2026)", "PolitPro (Umfrage-Durchschnitt)",
  "https://politpro.eu/de/oesterreich", "FPÖ 39,7 · ÖVP 20,0 · SPÖ 13,9 · Grüne 13,2 · NEOS 6,6 · KPÖ 4,1 %", "Seite geöffnet – nur als Quellenkritik-Beispiel, nicht auf Kadetten-Seiten als Zahl"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "Klubstand von FPÖ, ÖVP, SPÖ und Grünen: nicht einzeln geprüft (parlament.gv.at von hier teilweise gesperrt) – angenommen wie Wahl 2024 (57, 51, 41, 16). Vor Stunde 3 kurz auf parlament.gv.at schauen.",
 "SPÖ-Spitze ab Jänner 2027: Stand 06.10.2026. Vor Stunde 4 (Jänner) neu prüfen, wer die SPÖ führt und wer Vizekanzler ist.",
 "Wahlalter zwischen 1920 und 1945 (ab wann 21?): nicht geprüft. Gesichert: 1919 = 20; vor 1949 laut Buch 21; ab 1949 20.",
 "Ö1-Podcasts aus dem Jahresplan (»Betrifft Geschichte: Sozialdemokratie, Teil 1«, 5 min; Radiokolleg »Was ist konservativ«, »Was ist liberal«): nicht angehört – nur als Vorschlag auf der Lösungsseite.",
 "Trauner-Link www.trauner.at/wahlverhalten (Buch S. 33): nicht geöffnet.",
 "Videos: keine eingebaut (YouTube von hier nicht prüfbar).",
]
