"""PBGW 3BK · K1.2 Quellen und Methoden – Fallstudie »Gefälscht! Der Fall der Hitler-Tagebücher« (Buch S. 10–12) – 1 Stunde (v1).
Jahresplan: Einheit 1 »Geschichte als Entwicklungsprozess; Quellen zur Rekonstruktion und Dekonstruktion …« (K01, N01, P4, P7, GLV 2, GLV 3).
Kurzfassung für EINE Stunde: Pflicht = Aufgaben 1–3 (Nachbesprechung am Stundenende), Aufgaben 4–6 = »Für Schnelle und Neugierige«.
Faktenquelle: Bundesarchiv, Geschichtsgalerie »Pressekonferenz des Bundesarchivs zu Hitler-Tagebüchern« und Chronologie-PDF (Stand 19.10.2026).
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "19.10.2026"
V = "v1"
ORDNER = "3bk-pbgw/k1-2-faelschung"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "3bk-pbgw/"
EYEBROW = "PBGW · 3BK · K1.2 Quellen und Methoden"
TITEL = "Gefälscht! Der Fall der Hitler-Tagebücher"
BUCH = "Buch S. 10–12"
KEY = "26-27-3BK-K1.2-Faelschung-TH-Handy-v1"
PRAEFIX = "26-27-3BK-K1.2-Faelschung"

VIDEOS = {}

AE = ["äußere Kritik", "innere Kritik"]

T = [
 # ======================================================= Stunde 1 · Pflicht
 {"id": "a1", "nr": 1, "title": "Äußere oder innere Kritik?", "src": "Buch S. 10–12", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Ordne jeden Befund zu: Gehört er zur äußeren Quellenkritik (Material, Echtheit, Herkunft) oder zur inneren Quellenkritik (Inhalt)?",
  "hint": "Info: Theorie-Seite Teil 2 »Äußere Kritik« und »Innere Kritik«",
  "type": "multi",
  "fields": [["a", "a) Gutachter untersuchen Papier, Aufkleber und Einband der Bände auf ihr Alter.", AE, False],
             ["b", "b) Fehler aus einem Buch von Max Domarus tauchen im »Tagebuch« wieder auf.", AE, False],
             ["c", "c) Das Papier enthält Weißmacher, die erst nach 1945 hergestellt wurden.", AE, False],
             ["d", "d) Es stehen keine Gefühle und Überlegungen drin, nur Banales im Zeitungsstil.", AE, False],
             ["e", "e) Wo die Bände zwischen 1945 und 1981 waren, lässt sich nicht überprüfen.", AE, False]],
  "chk": {"a": {"sel": "äußere Kritik"}, "b": {"sel": "innere Kritik"}, "c": {"sel": "äußere Kritik"},
          "d": {"sel": "innere Kritik"}, "e": {"sel": "äußere Kritik"}},
  "sol": [["Lösung", ["a) äußere (Material und Alter prüfen) · b) innere (Inhalt abgeschrieben) · c) äußere (Material, Anachronismus) · d) innere (Inhalt passt nicht zu einem Tagebuch) · "
                      "e) äußere (Herkunft)"]]],
  "tip": ["Äußere Kritik prüft das Material und die Herkunft, innere Kritik den Inhalt", "theorie.html#aeussere"]},

 {"id": "a2", "nr": 2, "title": "Der Handschrift-Trick", "src": "Buch S. 10–12", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Bei der ersten Prüfung bestätigten Schriftgutachter: Tagebuch und Hitler-Schriftproben stammen von derselben Hand. Trotzdem war das Gutachten wertlos. "
       "a) Erkläre in 1–2 Sätzen, warum. b) Nenne zwei Dinge, die man hätte besser machen müssen.",
  "hint": "Info: Theorie-Seite Teil 2 »Der Handschrift-Trick«",
  "type": "multi",
  "fields": [["warum", "a) Warum war das Gutachten wertlos? (1–2 Sätze)"], ["besser", "b) Zwei Dinge, die man besser machen musste"]],
  "chk": {"warum": {"kw": [["Vergleichsproben stammten vom Fälscher", "fälsch|kujau|selbe quelle|gleiche quelle|selben quelle|ebenfalls|auch von"]]},
          "besser": {"kw": [["gesicherte Originale", "original|echt|gesichert|archiv"], ["unabhängig / weitere Prüfung", "unabhängig|mehrere|zweite|weitere|material|inhalt|papier"]]}},
  "sol": [["Lösung", ["a) Die Vergleichsproben stammten ebenfalls vom Fälscher. Man verglich Fälschung mit Fälschung – »gleiche Hand« stimmte, bewies aber nichts über Hitler.",
                      "b) z. B.: nur gesicherte Originale (aus einem Archiv) als Vergleich · unabhängige Gutachter · zusätzlich Material und Inhalt prüfen."]]],
  "tip": ["Gleiche Hand heißt noch nicht: von Hitler", "theorie.html#handschrift"]},

 {"id": "a3", "nr": 3, "title": "9,3 Millionen D-Mark", "src": "Buch S. 10–12", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Der »Stern« zahlte über 9 Millionen D-Mark und prüfte die Bände vorher nicht unabhängig. a) Nenne zwei Gründe, warum man so handelt (wirtschaftlich oder aus Zeitdruck). "
       "b) Nenne eine Regel, die den Schaden verhindert hätte.",
  "hint": "Info: Theorie-Seite Teil 1 »Warum glaubte man daran?« und Teil 2 »Wem nützt die Fälschung?«",
  "type": "multi",
  "fields": [["gruende", "a) Zwei Gründe, warum nicht genauer geprüft wurde"], ["regel", "b) Eine Regel, die den Schaden verhindert hätte"]],
  "chk": {"gruende": {"kw": [["Geld / Auflage / Exklusivität", "geld|auflage|verkauf|gewinn|umsatz|exklusiv|sensation|millionen"],
                              ["Konkurrenz / Zeitdruck / Geheimhaltung", "konkurren|zeitdruck|geheim|schnell|zuerst|nur heidemann|einzige"]]},
          "regel": {"kw": [["unabhängige Prüfung vor dem Kauf", "unabhängig|prüf|gutachten|zweite quelle|vier-augen|kontroll|bevor"]]}},
  "sol": [["Lösung", ["a) z. B.: Weltsensation → hohe Auflage und viel Geld · Angst, dass die Konkurrenz zuerst kommt · Geheimhaltung: nur der Reporter Heidemann kannte die »Quelle«.",
                      "b) z. B.: erst zahlen, wenn ein unabhängiges Gutachten vorliegt · Vier-Augen-Prinzip: nie nur eine Person mit Kontakt zur Quelle · eine einzige, ungeprüfte Quelle reicht nie."]]],
  "tip": ["Je größer die Sensation, desto gründlicher die Prüfung", "theorie.html#warum"]},

 # ======================================================= Für Schnelle und Neugierige
 {"id": "a4", "nr": 4, "title": "KI-Antwort prüfen", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Eine KI behauptet: »Das Papier der Tagebücher enthielt optische Aufheller, die es erst ab 1955 gab. Quelle: Bundesarchiv.« "
       "Prüfe die Behauptung: Öffne bundesarchiv.de, Suche »Hitler-Tagebücher Chronologie« (PDF der Geschichtsgalerie). a) Wie lautet dein Urteil? b) Welche Stelle in der Quelle hast du gefunden? (1–2 Sätze)",
  "hint": "Recherche im Internet: bundesarchiv.de – Geschichtsgalerie »Pressekonferenz des Bundesarchivs zu Hitler-Tagebüchern« · Info: Theorie-Seite »So prüfst du eine KI-Antwort«",
  "type": "multi",
  "fields": [["urteil", "a) Dein Urteil", ["teilweise belegt – Weißmacher aus der Nachkriegszeit ja, aber nicht genau »erst ab 1955«", "voll belegt – genau so steht es dort",
                                           "frei erfunden – die Quelle sagt nichts zu Weißmachern", "nicht prüfbar – es gibt keine Quelle"]],
             ["stelle", "b) Welche Stelle hast du gefunden? (1–2 Sätze)"]],
  "chk": {"urteil": {"sel": "teilweise belegt – Weißmacher aus der Nachkriegszeit ja, aber nicht genau »erst ab 1955«"},
          "stelle": {"kw": [["Weißmacher / Weißtöner", "weißmacher|weißtöner|aufheller|weisstöner"], ["Zeit nach 1945 / Jahreszahl", "nach dem 2|nach 1945|1949|1955|nachkrieg"]]}},
  "sol": [["Lösung", ["a) teilweise belegt: Die Chronologie nennt Weißmacher, die erst nach dem 2. Weltkrieg produziert wurden. Die Zahl 1955 steht dort nur für das Papier eines anderen Stücks (»Weißtöner aus der Zeit zwischen 1949 und 1955«), nicht als Grenze für alle Tagebücher.",
                      "b) z. B. die Prüfung des BKA Ende April 1983 (Weißmacher, die erst nach dem 2. WK produziert wurden) und der vom 22.4.1983 (Weißtöner 1949–1955 im Mussolini-Papier).",
                      "Merke: Eine KI trifft oft den Kern, wird aber bei Zahlen ungenau – immer die Primärquelle lesen."]]],
  "tip": ["Behauptung – Beleg öffnen – Primärquelle – Urteil", "theorie.html#ki"]},

 {"id": "a5", "nr": 5, "title": "Geheimes Dokument im Chat", "src": "Buch S. 10–12", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Im Klassenchat taucht ein »geheimes Dokument« auf: Angeblich wird eine Kaserne in Niederösterreich geschlossen. a) Nenne drei Prüffragen, bevor du es weiterleitest. "
       "b) Was tust du, bis du Gewissheit hast?",
  "hint": "Info: Theorie-Seite Teil 2 »Werkzeugkasten Quellenkritik« und »So prüfst du eine KI-Antwort«",
  "type": "multi",
  "fields": [["fragen", "a) Drei Prüffragen"], ["tun", "b) Was tust du bis dahin?"]],
  "chk": {"fragen": {"kw": [["Wer / Herkunft", "wer|woher|absender|herkunft|verfasser|erstellt"], ["Inhalt / Echtheit", "stimmt|echt|fehler|inhalt|passt|stempel|form"], ["Wem nützt es?", "nützt|nutzen|wozu|absicht|zweck"]]},
          "tun": {"kw": [["nicht weiterleiten", "nicht weiter|nicht teilen|zurückhalten|nicht verbreiten|abwarten"], ["zweite Quelle suchen", "zweite|weitere|unabhängig|bundesheer|offizielle|quelle"]]}},
  "sol": [["Lösung", ["a) Wer hat es erstellt (Absender)? Woher kommt es, wer hat es zuerst gepostet? Passen Form und Inhalt (Stempel, Begriffe, Fehler)? Wem nützt es?",
                      "b) Nicht weiterleiten, eine zweite unabhängige Quelle suchen (z. B. Presseaussendung des Bundesheeres), bei Verdacht Vorgesetzte oder Lehrer informieren."]]],
  "tip": ["Wer? Woher? Was? Wozu? – der Werkzeugkasten", "theorie.html#werkzeug"]},

 {"id": "a6", "nr": 6, "title": "Fälschung im Archiv?", "src": "Buch S. 10–12", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Angenommen, ein Archiv bekommt die gefälschten Kladden geschenkt. Soll es Fälschungen aufbewahren? Nenne je ein Argument dafür und dagegen und gib dein Urteil.",
  "type": "multi",
  "fields": [["dafuer", "Ein Argument dafür"], ["dagegen", "Ein Argument dagegen"], ["urteil", "Mein Urteil und eine Begründung (1–2 Sätze)"]],
  "chk": {"dafuer": {"kw": [["Fälschung ist selbst eine Quelle", "quelle|forschung|geschichte|lernen|beweis|dokumentier|medien"]]},
          "dagegen": {"kw": [["Gefahr des Missbrauchs", "missbrauch|verbreit|echt|zusammenhang|verharmlos|aufmerksamkeit|falsch"]]}},
  "sol": [["Lösung", ["Dafür: Die Fälschung ist selbst eine Quelle – für Mediengeschichte und für den Umgang mit der NS-Zeit in den 1980er-Jahren; als Fälschung gekennzeichnet schützt sie vor Missbrauch.",
                      "Dagegen: Auszüge könnten aus dem Zusammenhang gerissen und als »echt« verbreitet werden; Aufmerksamkeit für NS-Verharmlosung.",
                      "Freie Begründung – wichtig ist ein klares Urteil mit Argument."]]],
  "tip": ["Jede Quelle ist eine Quelle – auch eine Fälschung", "theorie.html#schnelle"]},
]

GRP = {1: "Stunde 1 · Pflicht – Aufgaben 1–3 (Buch S. 10–12)", 0: "Für Schnelle und Neugierige · optional"}

LERNZIELE = ["erklären, wie Fachleute 1983 die **Hitler-Tagebücher** als Fälschung entlarvt haben",
             "**äußere** und **innere Quellenkritik** unterscheiden und auf eine Quelle anwenden",
             "erkennen, **wem eine Fälschung nützt**, und begründen, warum eine einzige, ungeprüfte Quelle nie reicht"]

WICHTIGSTE = ["Die **Hitler-Tagebücher** (1983) stammten vom Fälscher **Konrad Kujau**; der »Stern« zahlte dafür über **9 Millionen D-Mark**.",
              "**Äußere Kritik** prüft Material, Echtheit und Herkunft: Im Papier steckten Weißmacher, die erst nach dem Zweiten Weltkrieg hergestellt wurden.",
              "**Innere Kritik** prüft den Inhalt: viele Fehler, keine echten Gedanken – und die Texte waren aus der Edition von **Max Domarus** abgeschrieben.",
              "Ein Gutachten ist nur so gut wie sein **Vergleichsmaterial**: Fälschung gegen Fälschung beweist nichts.",
              "Frage bei jeder Quelle: **Wer? Woher? Woraus? Was? Wozu?** – und: Wem nützt sie? Eine einzige, ungeprüfte Quelle reicht nie."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Quelle", "alles, woraus wir etwas über die Vergangenheit erfahren (Texte, Bilder, Gegenstände)"],
                ["Primärquelle", "stammt aus der Zeit selbst, z. B. ein echtes Tagebuch, ein Befehl, ein Foto"],
                ["Darstellung", "später verfasster Text über die Vergangenheit, z. B. ein Schulbuch"],
                ["Edition", "gesammelte und kommentierte Quellen, z. B. Domarus: Hitlers Reden"],
                ["Provenienz", "Herkunft einer Quelle: Wer hatte sie wann und wo?"],
                ["äußere Quellenkritik", "prüft Material, Schrift und Herkunft: Ist die Quelle echt?"],
                ["innere Quellenkritik", "prüft den Inhalt: Stimmt, was drinsteht, und warum wurde es geschrieben?"],
                ["Anachronismus", "etwas, das nicht in die angebliche Zeit passt, z. B. ein Stoff, den es damals noch nicht gab"],
                ["Desinformation", "bewusst verbreitete Falschinformation, um zu täuschen"],
                ["Lagebild", "Überblick über die Lage; jede Meldung wird nach Quelle und Inhalt bewertet"]]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Der Fall", "Wer hat die »Hitler-Tagebücher« gefälscht?", ["Konrad Kujau", "Gerd Heidemann", "Max Domarus", "Henri Nannen"],
  "Kujau fälschte die Bände; Reporter Heidemann vermittelte sie an den »Stern«.", "Theorie-Seite · Teil 1"),
 ("Der Fall", "Wie viel zahlte der »Stern« für die Tagebücher?", ["über 9 Millionen D-Mark", "etwa 90 000 D-Mark", "genau 1 Million D-Mark", "gar nichts – sie waren geschenkt"],
  "Der Verlag zahlte rund 9,3 Millionen D-Mark – ohne unabhängige Prüfung vorab.", "Theorie-Seite · Teil 1"),
 ("Der Fall", "Warum zahlte der »Stern« ohne genaue Prüfung?", ["Sensation, Konkurrenzdruck und Geheimhaltung", "Das Gesetz verlangte es.", "Hitlers Familie bestätigte die Echtheit.", "Das Bundesarchiv hatte sie schon geprüft."],
  "Hohe Auflage, Angst vor der Konkurrenz, nur ein Reporter kannte die »Quelle«.", "Theorie-Seite · Teil 1"),
 ("Quellenkritik", "Was prüft die äußere Quellenkritik?", ["Material, Echtheit und Herkunft", "ob der Inhalt gefällt", "wie viele Seiten die Quelle hat", "den Preis der Quelle"],
  "Äußere Kritik: Ist die Quelle echt – Papier, Tinte, Schrift, Herkunft?", "Buch S. 10–12"),
 ("Quellenkritik", "Die Prüfer fanden im Papier Stoffe, die erst nach dem Krieg hergestellt wurden. Das ist …", ["äußere Kritik (Anachronismus)", "innere Kritik", "keine Quellenkritik", "ein Beweis für Echtheit"],
  "Material, das es damals noch nicht gab, zeigt: Die Quelle kann nicht aus dieser Zeit stammen.", "Theorie-Seite · Teil 2"),
 ("Quellenkritik", "Fehler aus einem Buch von Max Domarus tauchen im »Tagebuch« auf. Was heißt das?", ["Die Texte wurden abgeschrieben, nicht erlebt.", "Domarus war der Verfasser.", "Die Tagebücher sind echt.", "Domarus hat sie gefälscht."],
  "Wo Domarus irrt, irrt auch das »Tagebuch« – ein klarer Beleg für Abschreiben (innere Kritik).", "Theorie-Seite · Teil 2"),
 ("Quellenkritik", "Warum war das erste Handschrift-Gutachten wertlos?", ["Die Vergleichsproben stammten auch vom Fälscher.", "Die Gutachter konnten nicht lesen.", "Hitler schrieb nie von Hand.", "Die Schrift war zu schlecht."],
  "Fälschung wurde mit Fälschung verglichen – gleiche Hand beweist nichts über Hitler.", "Theorie-Seite · Teil 2"),
 ("Quellenkritik", "Was ist eine Primärquelle?", ["eine Quelle aus der Zeit selbst", "ein später geschriebenes Schulbuch", "eine Zusammenfassung im Internet", "jede KI-Antwort"],
  "Primärquellen stammen aus der Zeit, über die wir etwas wissen wollen.", "Buch S. 10–12"),
 ("Quellenkritik", "Welche Frage gehört in JEDE Quellenkritik?", ["Wem nützt die Quelle?", "Ist sie schön gestaltet?", "Wie lang ist sie?", "Hat sie viele Bilder?"],
  "Absicht und Nutzen helfen, Fälschungen und Propaganda zu erkennen.", "Buch S. 10–12"),
 ("Heute", "Eine KI nennt eine Zahl und eine Quelle. Was tust du?", ["Den Beleg öffnen und in der Primärquelle prüfen.", "Es glauben – KI irrt nie.", "Die Zahl weitergeben.", "Nichts – Quellen sind egal."],
  "Eine KI klingt überzeugend, ist aber kein Beweis; Zahlen und Quellenangaben immer prüfen.", "Theorie-Seite · Für Schnelle"),
]
