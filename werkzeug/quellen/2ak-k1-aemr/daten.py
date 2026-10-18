"""Aufgaben PBGW 2AK · K1 »70 Jahre AEMR« (Arbeitsblatt Schroedel aktuell 11/2018, Aufgaben 1–5 umformuliert).
Eine Quelle für Handy-Arbeitsblatt, Word (AB/Loesung) und PPP. Bei Auswahlfeldern steht die richtige Antwort
an erster Stelle; die Anzeige wird gemischt (außer f[3] is False = feste Reihenfolge, z. B. stimmt/stimmt nicht)."""

STAND = "18.10.2026"
SJ = ["stimmt", "stimmt nicht"]
SS = ["Stolz", "Schande"]
G = ["nur für bestimmte Gruppen", "für die Bürger eines Staates", "für die Menschen in Europa", "für alle Menschen weltweit"]


def fx(opts, correct):
    """Feste Reihenfolge (z. B. stimmt / stimmt nicht) – richtige Antwort steht im chk."""
    return opts


T = [
 {"id": "a1", "nr": 1, "title": "Ein langer Weg", "src": "Arbeitsblatt M1 · Theorie S. 50", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Schau dir die Zeitleiste M1 an. Achtung: Die Kästchen stehen nicht immer in der richtigen Reihenfolge – achte auf die Jahreszahlen! "
       "a) Welches Dokument ist das älteste? b) Wie viele Jahre liegen zwischen der Magna Charta und der AEMR? "
       "c) Für wen galten die Rechte? Ordne zu. d) Beschreibe in 2–3 Sätzen mit eigenen Worten, wie sich die Idee der Menschenrechte verändert hat.",
  "type": "multi",
  "fields": [["alt", "a) Das älteste Dokument", ["Kyros-Zylinder (539 v. Chr.)", "Magna Charta (1215)", "Bill of Rights (1689)", "Unabhängigkeitserklärung USA (1776)"]],
             ["jahre", "b) Jahre zwischen Magna Charta (1215) und AEMR (1948)"],
             ["mc", "c) Magna Charta, 1215 – galt …", G],
             ["fr", "c) Französische Erklärung der Menschen- und Bürgerrechte, 1789 – galt …", G],
             ["aemr", "c) Allgemeine Erklärung der Menschenrechte, 1948 – gilt …", G],
             ["emrk", "c) Europäische Menschenrechtskonvention, 1950 – gilt …", G],
             ["entw", "d) So hat sich die Idee verändert (2–3 Sätze)"]],
  "chk": {"alt": {"sel": "Kyros-Zylinder (539 v. Chr.)"}, "jahre": {"num": 733, "unit": ""},
          "mc": {"sel": G[0]}, "fr": {"sel": G[1]}, "aemr": {"sel": G[3]}, "emrk": {"sel": G[2]},
          "entw": {"kw": [["früher nur für wenige", "früher|anfangs|zuerst|damals|nur|wenige|gruppe|adel|kirche|bürger|land"], ["heute für alle Menschen", "alle|jede|welt"]]}},
  "sol": [["a) und b)", ["Kyros-Zylinder, 539 v. Chr. (Persien)", "1948 − 1215 = 733 Jahre"]],
          ["c)", ["Magna Charta → nur bestimmte Gruppen (Freiheit der Kirche, Rechte des Adels)", "Französische Erklärung → die Bürger eines Staates (Frankreich)",
                  "AEMR → alle Menschen weltweit", "EMRK → die Menschen in Europa (alle Staaten des Europarats)"]],
          ["d) Muster", ["Früher galten Rechte nur in einem Land und oft nur für bestimmte Gruppen – sie wurden den Herrschern abgerungen. "
                         "Mit der Zeit kamen mehr Rechte und mehr Menschen dazu. Seit der AEMR 1948 gelten sie für alle Menschen auf der Welt; "
                         "danach wurden sie in Verträgen verbindlich gemacht (EMRK 1950, UN-Pakte 1966)."]]],
  "tip": ["M1 – auf die Jahreszahlen achten", "#material"]},

 {"id": "a2", "nr": 2, "title": "Was ist an der AEMR neu?", "src": "Arbeitsblatt M2 · Theorie S. 47", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Lies M2. a) Stimmt das? Entscheide bei jedem Satz. b) Erkläre in 2–3 Sätzen, was die AEMR von den älteren Dokumenten aus M1 unterscheidet.",
  "type": "multi",
  "fields": [["s1", "Die AEMR haben Männer und Frauen aus acht verschiedenen Ländern ausgearbeitet.", SJ, False],
             ["s2", "Die AEMR beruht auf einer bestimmten Religion.", SJ, False],
             ["s3", "Die Rechte gelten unabhängig von Alter, Geschlecht und Nationalität.", SJ, False],
             ["s4", "1948 waren die Staaten durch einen Vertrag verpflichtet, die Rechte einzuhalten.", SJ, False],
             ["s5", "1948 konnte man kontrollieren, ob die Staaten ihr Versprechen halten.", SJ, False],
             ["s6", "Der größte Erfolg: Menschenrechte sind aus dem Bewusstsein der Menschen nicht mehr wegzudenken.", SJ, False],
             ["neu", "b) Der Unterschied zu den älteren Dokumenten (2–3 Sätze)"]],
  "chk": {"s1": {"sel": "stimmt"}, "s2": {"sel": "stimmt nicht"}, "s3": {"sel": "stimmt"}, "s4": {"sel": "stimmt nicht"},
          "s5": {"sel": "stimmt nicht"}, "s6": {"sel": "stimmt"},
          "neu": {"kw": [["für alle Menschen", "alle|jede|welt|unabhängig"], ["Vergleich mit früher", "früher|älter|vorher|davor|nur|land|staat|bürger|gruppe"]]}},
  "sol": [["a)", ["stimmt · stimmt nicht (Grundlage sind die Achtung vor dem Leben und der Wert jedes Menschen) · stimmt · "
                  "stimmt nicht (keine vertragliche Bindung) · stimmt nicht (keine Kontrolle) · stimmt"]],
          ["b) Muster", ["Die älteren Dokumente galten nur in einem Land und oft nur für bestimmte Gruppen. Die AEMR gilt zum ersten Mal für alle Menschen "
                         "auf der Welt – egal welches Alter, Geschlecht oder welche Nationalität. Sie wurde von Ländern aus verschiedenen Kontinenten "
                         "gemeinsam ausgearbeitet und hängt an keiner Religion. Sie war aber zuerst nur ein Versprechen, kein Vertrag."]]],
  "tip": ["M2, Zeile 1–33", "#material"]},

 {"id": "a3", "nr": 3, "title": "Warum ist Durchsetzen so schwer?", "src": "Arbeitsblatt M3 · Theorie S. 47, 50", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Lies M3. a) Nenne die drei Dinge, die es auf der Welt – anders als in einem Staat – nicht gibt. "
       "b) Was ist mit »weichen« Sanktionen gemeint? Beschreibe in 1–2 Sätzen mit einem Beispiel. "
       "c) Vergleich mit Österreich: Wer prüft bei uns, ob der Staat Grundrechte verletzt?",
  "type": "multi",
  "fields": [["drei", "a) Diese drei Dinge gibt es auf der Welt nicht"],
             ["weich", "b) »Weiche« Sanktionen (1–2 Sätze, mit Beispiel)"],
             ["oe", "c) In Österreich prüft das …", ["der Verfassungsgerichtshof", "das Bundesheer", "Amnesty International", "die UNO-Generalversammlung"]]],
  "chk": {"drei": {"kw": [["Weltregierung", "regierung"], ["Weltpolizei", "polizei"], ["Weltgericht", "gericht"]]},
          "weich": {"kw": [["öffentlich anprangern", "pranger|öffentlich|ächt|bloß|kritik|kritisier|medien"], ["Druck auf die Regierung", "druck|regierung|ruf|image|schäm"]]},
          "oe": {"sel": "der Verfassungsgerichtshof"}},
  "sol": [["a)", ["Weltregierung, Weltpolizei, Weltgericht – die Regeln stehen auf dem Papier, aber es fehlen Strafen (Sanktionen)."]],
          ["b)", ["Staaten, NGOs wie Amnesty International und Medien machen Verstöße öffentlich – sie stellen den Staat »an den Pranger«. "
                  "Kein Staat will als Rechtsbrecher dastehen; der Druck kann ihn dazu bringen, sein Verhalten zu ändern."]],
          ["c)", ["der Verfassungsgerichtshof in Wien; danach kann man sich an den Europäischen Gerichtshof für Menschenrechte in Straßburg wenden (Buch S. 47, 50)."]]],
  "tip": ["M3 · Buch S. 47 und 50", "#material"]},

 {"id": "a4", "nr": 4, "title": "Stolz und Schande", "src": "Arbeitsblatt M4 · Theorie S. 51–52", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Lies M4. a) Ordne zu: Ist das für den Verfasser ein Grund für Stolz oder für Schande? "
       "b) Erkläre in 2–3 Sätzen, warum er den Jahrestag einen »Tag für Stolz und Schande« nennt. "
       "c) Quellencheck: Was für ein Text ist M4 – und aus welchem Jahr stammt er?",
  "type": "multi",
  "fields": [["z1", "Menschenrechte stehen in fast allen Verfassungen.", SS, False],
             ["z2", "Die Berichte von Amnesty International lesen sich wie eine Todesanzeige.", SS, False],
             ["z3", "Es gibt so viele Pakte und Konventionen, dass man sie zu einer Pyramide stapeln kann.", SS, False],
             ["z4", "Die Hilferufe aus Syrien, dem Jemen und Afghanistan werden überhört.", SS, False],
             ["z5", "Politiker sprechen verächtlich über Flüchtlinge.", SS, False],
             ["erkl", "b) Darum »Stolz und Schande« (2–3 Sätze)"],
             ["art", "c) M4 ist …", ["ein Kommentar (Meinung)", "eine Nachricht (nur Fakten)", "ein Gesetzestext", "eine Statistik"]],
             ["jahr", "c) M4 stammt aus dem Jahr …"]],
  "chk": {"z1": {"sel": "Stolz"}, "z2": {"sel": "Schande"}, "z3": {"sel": "Stolz"}, "z4": {"sel": "Schande"}, "z5": {"sel": "Schande"},
          "erkl": {"kw": [["auf dem Papier gut", "papier|verfassung|konvention|pakt|gesetz|vertr|stolz"], ["Wirklichkeit schlecht", "realität|wirklich|praxis|verletz|amnesty|todes|schande|tatsächlich|alltag"]]},
          "art": {"sel": "ein Kommentar (Meinung)"}, "jahr": {"num": 2018, "unit": ""}},
  "sol": [["a)", ["Stolz · Schande · Stolz · Schande · Schande"]],
          ["b) Muster", ["Auf dem Papier sind die Menschenrechte großartig: Sie stehen in fast allen Verfassungen und in vielen verbindlichen Verträgen – "
                         "darauf kann man stolz sein. In der Wirklichkeit werden sie aber jeden Tag verletzt (Mord, Folter, überhörte Hilferufe, "
                         "verächtliche Sprache) – das ist eine Schande."]],
          ["c)", ["ein Kommentar (Meinung, wertende Wörter wie »Schande« oder »Todesanzeige«) aus dem Jahr 2018, zum 70. Jahrestag – aus deutscher Sicht. "
                  "Ob das 2026 noch stimmt, prüfen wir in der nächsten Stunde."]]],
  "tip": ["M4 – Stolz = Papier, Schande = Wirklichkeit", "#material"]},

 {"id": "a5", "nr": 5, "title": "Nur ein schöner Traum?", "src": "Arbeitsblatt Aufgabe 5", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Manche sagen: »Die AEMR ist ein schöner Traum, der nie wahr wird – in der echten Welt bringt sie nichts.« In der nächsten Stunde diskutieren wir darüber. "
       "Bereite dich vor: a) Nenne ein Argument FÜR diese Meinung – mit einem Beispiel aus M3 oder M4. "
       "b) Nenne ein Argument DAGEGEN – mit einem Beispiel aus M1, M2 oder M3. c) Wie sehr stimmst du der Meinung zu? d) Begründe deine Wahl in 2 Sätzen.",
  "type": "multi",
  "fields": [["pro", "a) Argument dafür – mit Beispiel aus M3 oder M4"],
             ["contra", "b) Argument dagegen – mit Beispiel aus M1, M2 oder M3"],
             ["skala", "c) Ich stimme der Meinung zu …", ["1 – gar nicht", "2 – eher nicht", "3 – teils, teils", "4 – eher schon", "5 – voll und ganz"], False],
             ["begr", "d) Meine Begründung (2 Sätze)"]],
  "chk": {"pro": {"kw": [["Beispiel aus M3/M4", "durchsetz|strafe|sanktion|polizei|gericht|regierung|amnesty|verletz|folter|mord|syrien|jemen|afghanistan|flücht|papier|verbindlich"]]},
          "contra": {"kw": [["Beispiel aus M1–M3", "verfassung|konvention|emrk|pakt|vertrag|druck|pranger|bewusstsein|maßstab|gericht|1950|1966|weich|öffentlich"]]}},
  "sol": [["Für die Meinung", ["Die AEMR ist nicht verbindlich, es gibt keine Weltpolizei und keine Strafen (M3).",
                               "Amnesty berichtet jedes Jahr von Mord, Folter und Rechtlosigkeit (M4); 2025 gab es so viele Hinrichtungen wie seit 1981 nicht."]],
          ["Gegen die Meinung", ["Aus der AEMR wurden verbindliche Verträge: EMRK 1950, UN-Pakte 1966 (M1) – in Europa kann man beim EGMR klagen.",
                                 "Öffentlicher Druck wirkt (M3); die Rechte sind »aus dem Bewusstsein nicht mehr wegzudenken« (M2).",
                                 "113 Staaten haben die Todesstrafe für alle Verbrechen abgeschafft (Amnesty, Mai 2026)."]],
          ["c) und d)", ["Kein Richtig oder Falsch – die Begründung zählt."]]],
  "tip": ["M3 und M4 für »dafür«, M1–M3 für »dagegen«", "#material"]},

 {"id": "a6", "nr": 6, "title": "Deine Frage für die nächste Stunde", "src": "Fragen-Box", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Was möchtest du zum Thema Menschenrechte wissen – oder was hat dich überrascht? Schreib eine echte Frage auf. "
       "Dein Lehrer sammelt die Fragen aus euren PDFs und beantwortet sie in der nächsten Stunde.",
  "type": "multi",
  "fields": [["frage", "Meine Frage"],
             ["thema", "Worum geht es?", ["Bundesheer und Soldaten", "Todesstrafe", "ein Land aus den Nachrichten", "Flucht und Asyl", "Internet und Handy",
                                          "Sport (WM in Saudi-Arabien)", "etwas anderes"], False]],
  "sol": [["Lösung", ["Deine Frage wird in der nächsten Stunde besprochen."]]]},

 # ---------------- Für Schnelle und Neugierige
 {"id": "a7", "nr": 7, "title": "Wo beginnen Menschenrechte?", "src": "Arbeitsblatt M2, Z. 34–47", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Eleanor Roosevelt sagt: Menschenrechte beginnen »an den kleinen Plätzen, nahe dem eigenen Heim«. a) Nenne zwei solche »kleinen Plätze« aus deinem Leben "
       "(z. B. Klasse, Kaserne, Sportverein, Klassenchat). b) Beschreibe für einen davon in 1–2 Sätzen, wie dort jemandem die gleiche Würde genommen werden könnte – "
       "und was du dagegen tun kannst.",
  "type": "multi", "fields": [["plaetze", "a) Zwei »kleine Plätze« aus meinem Leben"], ["wuerde", "b) Was dort passieren könnte – und was ich tun kann"]],
  "sol": [["Beispiele", ["Klassenchat: Jemand wird ausgelacht oder ein peinliches Foto wird verschickt → nicht weiterleiten, dagegenhalten, Lehrer oder Vertrauensperson informieren.",
                         "Sportverein: Ein Spieler wird wegen seiner Herkunft beschimpft → Trainer einschalten, sich vor ihn stellen."]]]},

 {"id": "a8", "nr": 8, "title": "Rechnen: Die Abstimmung 1948", "src": "Info im Aufgabentext", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Am 10. Dezember 1948 hatte die UNO 58 Mitglieder. 48 stimmten für die AEMR, kein Staat dagegen, 8 enthielten sich, 2 stimmten nicht mit. "
       "a) Wie viel Prozent der Mitglieder stimmten dafür? (auf eine Kommastelle gerundet) b) Wie alt wird die AEMR am 10. Dezember 2026? "
       "c) Österreich ist seit 1955 bei der UNO. Wie viele Jahre nach der Abstimmung war das?",
  "type": "multi", "fields": [["proz", "a) Prozent dafür"], ["alter", "b) Alter der AEMR am 10.12.2026 (Jahre)"], ["oe", "c) Jahre bis zum UNO-Beitritt Österreichs"]],
  "chk": {"proz": {"num": 82.8, "unit": ""}, "alter": {"num": 78, "unit": ""}, "oe": {"num": 7, "unit": ""}},
  "sol": [["Lösung", ["a) 48 : 58 · 100 = 82,8 %", "b) 2026 − 1948 = 78 Jahre", "c) 1955 − 1948 = 7 Jahre – Österreich war 1948 noch von den Alliierten besetzt."]]],
  "tip": ["Prozent = Teil : Ganzes · 100", "#a8"]},

 {"id": "a9", "nr": 9, "title": "Soldaten und Menschenrechte", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Österreichische Soldaten sind im Auslandseinsatz, z. B. bei KFOR im Kosovo. Im Krieg gelten zusätzlich die Genfer Abkommen (Kriegsvölkerrecht). "
       "a) Nenne zwei Regeln der Genfer Abkommen. b) Wen schützen sie? Suchtipp: »Genfer Abkommen einfach erklärt« auf roteskreuz.at oder bundesheer.at.",
  "type": "multi", "fields": [["regeln", "a) Zwei Regeln"], ["wen", "b) Geschützt werden …"]],
  "chk": {"wen": {"kw": [["Zivilisten", "zivil"], ["Verwundete oder Gefangene", "gefangen|verwundet|verletzt|krank"]]}},
  "sol": [["Lösung", ["Regeln: Zivilisten dürfen nicht angegriffen werden · Verwundete und Kranke werden versorgt – egal von welcher Seite · "
                      "Kriegsgefangene werden menschlich behandelt, Folter ist verboten · Sanitäter und das Rote Kreuz dürfen nicht angegriffen werden.",
                      "Geschützt: Zivilisten, Verwundete, Kranke, Schiffbrüchige, Kriegsgefangene, Sanitätspersonal."]]],
  "tip": ["Recherche: roteskreuz.at", "https://www.roteskreuz.at"]},

 {"id": "a10", "nr": 10, "title": "Aktuell: Preise für Menschenrechte", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Rund um den 10. Dezember, den Tag der Menschenrechte, werden wichtige Preise verliehen. a) Wer bekommt 2026 den Friedensnobelpreis? b) Wofür? (1 Satz) "
       "c) Wer bekommt den Sacharow-Preis 2026 des EU-Parlaments? (Entscheidung am 22. Oktober) Suchtipp: orf.at, nobelprize.org, europarl.europa.eu.",
  "type": "multi", "fields": [["nobel", "a) Friedensnobelpreis 2026"], ["wofuer", "b) Wofür? (1 Satz)"], ["sacharow", "c) Sacharow-Preis 2026"]],
  "chk": {"nobel": {"kw": [["Navi Pillay", "pillay"]]}},
  "sol": [["Lösung", ["a) Navi (Navanethem) Pillay aus Südafrika – bekanntgegeben am 9. Oktober 2026.",
                      "b) für ihren Einsatz für Frieden und Völkerrecht: Sie hat mitgeholfen, dass Kriegsverbrechen, Verbrechen gegen die Menschlichkeit und "
                      "Völkermord vor Gericht kommen (Richterin am Ruanda-Tribunal und am Internationalen Strafgerichtshof, UN-Hochkommissarin für Menschenrechte).",
                      "c) Entscheidung am 22. Oktober 2026 – schau auf europarl.europa.eu nach."]]],
  "tip": ["Recherche: orf.at", "https://orf.at"]},
]
