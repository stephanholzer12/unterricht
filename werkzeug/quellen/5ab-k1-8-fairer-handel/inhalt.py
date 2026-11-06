"""TÖW 5AB · K1.8 Fairer Handel (Trauner TÖW, S. 35–38) – v1.
Auftrag Stephan 06.11.2026: neue Einheit für GitHub + Unterrichts-PPP, sonst nichts (Teillieferung). Neue Regeln aus demselben Auftrag: realistisch höchstens 40 von 50 min,
menschlichere Sprache wie im Schulbuch, Verweise auf das Schulbuch, Einstieg »Das Wichtigste vorab / wozu / warum interessant«, mehr Gruppenarbeit und Diskussion,
gemeinsame Aufgaben deutlich kennzeichnen, aktuelle Daten, deutschsprachige Quellen/Papers.
Nachtrag 06.11.2026: Test 5BK Di 10.11., 5AK Do 12.11. – die Einheit läuft am Testtag (kurz, nach dem Test) und zum Teil eine Woche später weiter
(Annahme: 5BK Di 17.11., 5AK Do 19.11. – Stephan nannte nur den 19.11.). Testdauer angenommen: 20 min.
Jahresplan v22, Zeile 5: Einheit 5 (E5) Wirtschafts-, Umwelt- und Warenethik; Fairer Handel, 2 Std. (hier: Fairer Handel allein, Ethik S. 31–34 bleibt offen), K06, N05, N11, P1, P2, P4, P6, SDG 8/12/16, GLV 1/5.
Quellen: Fairtrade Österreich (Jahresbericht 2026, Meldung 11.12.2025; Fairtrade-Studie Côte d'Ivoire, Meldung 29.09./06.10.2025 – Zahlen verschiedener Fairtrade-Seiten weichen ab, darum nur die gemeinsamen Werte), lebensmittelpraxis.de 07.11.2025, polis aktuell 4/2020, bpb APuZ 2012 (siehe Prüfhinweise).
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "06.11.2026"
V = "v1"
V_UNT = "v1"
ORDNER = "5ab-toew/k1-8-fairer-handel"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ab-toew/"
EYEBROW = "TÖW · 5AB · K1.8 Fairer Handel"
TITEL = "Fairer Handel – was steckt hinter dem Siegel?"
KURZTITEL = "Fairer Handel"
BUCH = "Buch S. 35–38"
KEY = "26-27-5AB-K1.8-Fairtrade-TH-Handy-v1"
CHECK_KEY = "26-27-5AB-K1.8-Fairtrade-Lernseite-Check-v1"
PRAEFIX = "26-27-5AB-K1.8-Fairtrade"
KAP = "K1.8"
TEST = "5BK Di 10.11. · 5AK Do 12.11."

VIDEOS = {}
FREIGEGEBEN = set()


def zeigen(key, lehrer=False):
    return key in FREIGEGEBEN


KLASSEN = ["5BK", "5AK"]          # Reihenfolge nach Termin
DATEN = {"5BK": {1: "Di 10.11.", 2: "Di 17.11."}, "5AK": {1: "Do 12.11.", 2: "Do 19.11."}}
TEIL_STUNDE = {1: {"5BK": 1, "5AK": 1}, 2: {"5BK": 2, "5AK": 2}}
TEILNAME = {1: "Teil 1 · Was heißt fair?", 2: "Teil 2 · Was bringt es – und was nicht?"}
TEILBUCH = {1: "Buch S. 35–37", 2: "Buch S. 36–38"}
ABSCHNITT_1 = "Fairer Handel: worum geht es?"
ABSCHNITT_2 = "Mindestpreis, Prämie und der Weltmarkt"


def wann(teil=None):
    if teil: return " · ".join(f"{k}: {DATEN[k][TEIL_STUNDE[teil][k]]}" for k in KLASSEN)
    return " · ".join(f"{k}: {DATEN[k][1]} und {DATEN[k][2]}" for k in KLASSEN)


# ---- Zahlen (Stand 06.11.2026), alle in eigenen Worten wiedergegeben
KAKAO = {"min": 3500, "praemie": 275, "datum": "11.12.2025", "gilt": "1. Oktober 2026 in Ghana und der Elfenbeinküste, anderswo seit 11. Juni 2026"}
UMSATZ = {"jahr": 2025, "mio": 796, "plus": "12,7 %"}
STUDIE = {"datum": "29.09.2025", "arm2017": 58, "arm2020": 36, "arm2024": 17}  # Fairtrade und Impact Institute
MODELL = {"t": 40, "wm": 2800}
assert MODELL["t"] * KAKAO["praemie"] == 11000 and MODELL["t"] * KAKAO["min"] == 140000 and (KAKAO["min"] - MODELL["wm"]) * MODELL["t"] == 28000

SAEULEN = ["Soziales", "Ökologisches", "Ökonomisches"]
SELB = [["s1", "Verbot ausbeuterischer Kinderarbeit", "Soziales"],
        ["s2", "Liste verbotener Pflanzenschutzmittel (Pestizide)", "Ökologisches"],
        ["s3", "Rückverfolgbarkeit der Ware vom Feld bis ins Regal", "Ökonomisches"],
        ["s4", "Förderung gewerkschaftlicher Organisation der Beschäftigten", "Soziales"],
        ["s5", "Förderung des Bio-Anbaus", "Ökologisches"],
        ["s6", "Transparente Handelsbeziehungen zwischen Käufer und Produzent", "Ökonomisches"]]

DATENTABELLE = [["Angabe (vereinfachtes Modell)", "Wert"],
                ["Menge, die die Kooperative verkauft", "40 Tonnen Kakao"],
                ["Fairtrade-Mindestpreis", "3.500 US-Dollar je Tonne"],
                ["Fairtrade-Prämie (kommt zusätzlich)", "275 US-Dollar je Tonne"],
                ["Weltmarktpreis (nur angenommen)", "2.800 US-Dollar je Tonne"]]
TABNOTE = ("Mindestpreis und Prämie für konventionellen Kakao laut Fairtrade-Meldung vom 11.12.2025 (gilt in Ghana und der Elfenbeinküste ab 1. Oktober 2026). "
           "Der Weltmarktpreis ist hier nur angenommen. Vereinfachtes Modell: ohne Gebühren, Transport und Aufschläge.")
SEL_D = ["Dann gilt der höhere Marktpreis – die Prämie kommt trotzdem dazu.", "Dann bleibt es bei 3.500 US-Dollar, der Markt ist egal.", "Dann entfällt die Prämie."]

BELEGT = ["belegt", "nicht belegt", "widerlegt"]

T = [
 # ======================================================= Teil 1 (Buch S. 35–37)
 {"id": "a1", "nr": 1, "title": "Die drei Säulen – was gehört wohin?", "src": "Buch S. 37", "own": True, "tag": "Teil 1", "h": 1, "zeit": 6, "gem": True,
  "q": "Zu zweit oder zu dritt: Die Standards von Fairtrade stehen auf drei Säulen – Soziales, Ökologisches und Ökonomisches. Ordnet jedes Beispiel der passenden Säule zu. "
       "Die Antwort steht im Schulbuch auf S. 37 im Kasten »Standards von Fairtrade«. Danach besprechen wir die Zuordnung gemeinsam.",
  "hint": "Soziales = Menschen und ihre Rechte · Ökologisches = Natur und Anbau · Ökonomisches = Handel und Geldfluss. Info im Schulbuch S. 37 und im Theorieteil »Fairer Handel: worum geht es?«",
  "type": "multi",
  "fields": [[k, t, SAEULEN, False] for k, t, _ in SELB],
  "chk": {k: {"sel": s} for k, _, s in SELB},
  "sol": [["Lösung (nach dem Schulbuch S. 37)", ["Soziales: Verbot ausbeuterischer Kinderarbeit · Förderung gewerkschaftlicher Organisation.",
                                                  "Ökologisches: Liste verbotener Pestizide · Förderung des Bio-Anbaus.",
                                                  "Ökonomisches: Rückverfolgbarkeit der Ware · transparente Handelsbeziehungen.",
                                                  "Hinweis: Der Mindestpreis steht im Buch bei den sozialen Standards; man kann ihn auch als wirtschaftliche Absicherung sehen."]]],
  "tip": [ABSCHNITT_1, "theorie.html#fairhandel"]},

 # ======================================================= Teil 2 (Buch S. 36–38)
 {"id": "a2", "nr": 2, "title": "Wie viel Prämie kommt zusammen?", "src": "Buch S. 36–38", "own": True, "tag": "Teil 2", "h": 2, "zeit": 7,
  "q": "Zu zweit: Eine Kakao-Kooperative in der Elfenbeinküste verkauft 40 Tonnen Kakao zu Fairtrade-Bedingungen. Die Zahlen stehen in der Tabelle. "
       "a) Wie hoch ist die Fairtrade-Prämie insgesamt? b) Wie viel Geld bringt der Verkauf zum Mindestpreis? (ohne Prämie) c) Der Weltmarktpreis liegt nur bei 2.800 US-Dollar je Tonne. "
       "Wie viel mehr bekommt die Kooperative durch den Mindestpreis als zum Weltmarktpreis? d) Was gilt, wenn der Weltmarktpreis auf 5.000 US-Dollar steigt? (Alle Beträge in US-Dollar, nur die Zahl eintragen.)",
  "hint": "Prämie = Tonnen × Prämie je Tonne · Erlös = Tonnen × Mindestpreis · Unterschied = (Mindestpreis − Weltmarktpreis) × Tonnen. Info im Theorieteil »" + ABSCHNITT_2 + "«",
  "tab": DATENTABELLE, "tabnote": TABNOTE,
  "tabnote_folie": "Vereinfachtes Modell. Mindestpreis und Prämie: Fairtrade-Meldung vom 11.12.2025. Weltmarktpreis nur angenommen.",
  "type": "multi",
  "fields": [["pr", "a) Prämie insgesamt in US-Dollar"], ["er", "b) Erlös zum Mindestpreis in US-Dollar"], ["mehr", "c) So viel mehr als zum Weltmarktpreis (US-Dollar)"],
             ["d", "d) Bei 5.000 US-Dollar Weltmarktpreis gilt …", SEL_D]],
  "chk": {"pr": {"num": 11000, "tol": 0.02}, "er": {"num": 140000, "tol": 0.02}, "mehr": {"num": 28000, "tol": 0.02}, "d": {"sel": SEL_D[0]}},
  "sol": [["Rechnung", ["a) 40 × 275 = 11.000 US-Dollar Prämie – sie geht an die Gemeinschaft und wird für Projekte genutzt, über die die Mitglieder abstimmen.",
                        "b) 40 × 3.500 = 140.000 US-Dollar",
                        "c) (3.500 − 2.800) × 40 = 700 × 40 = 28.000 US-Dollar mehr",
                        "d) Der Mindestpreis ist nur die Untergrenze. Liegt der Markt höher, gilt der höhere Marktpreis – die Prämie kommt zusätzlich."]]],
  "fsol": {"pr": "11.000", "er": "140.000", "mehr": "28.000", "d": SEL_D[0]},
  "fsol_rest": ["Rechnung: a) 40 × 275 = 11.000 · b) 40 × 3.500 = 140.000 · c) (3.500 − 2.800) × 40 = 28.000"],
  "tip": [ABSCHNITT_2, "theorie.html#mindestpreis"]},

 {"id": "a3", "nr": 3, "title": "Diskussion: Fair einkaufen in der Kaserne?", "src": "Buch-Aufgabe S. 38", "own": True, "tag": "Teil 2", "h": 2, "zeit": 10, "gem": True,
  "q": "In Vierergruppen mit Rollenkarten aus dem Theorieteil (»Diskussionsgrundlage«): Stellt euch vor, die Kaserne kauft für Kantine und Sportbuffet neu Kaffee und Schokoriegel ein. "
       "Diskutiert 6 Minuten und entscheidet dann als Gruppe. a) Eure Entscheidung. b) Zwei Gründe dafür. c) Das stärkste Gegenargument. d) Welche Information würdet ihr noch nachprüfen, bevor ihr entscheidet? "
       "Danach stellen die Gruppen ihre Entscheidung vor und Prof. HOLZER diskutiert mit euch.",
  "hint": "Es gibt keine einzige richtige Entscheidung – wichtig sind gute Gründe und die Frage, woher die Zahlen kommen. Info: Theorieteil »Diskussionsgrundlage« und »Was die Zahlen zeigen – und was nicht«. Ähnliche Fragen stehen im Schulbuch S. 38.",
  "type": "multi",
  "fields": [["wahl", "a) Unsere Entscheidung", ["Wir kaufen Fairtrade-Produkte ein.", "Wir kaufen nur einen Teil fair ein (z. B. nur Kaffee).", "Wir kaufen weiter wie bisher ein."], False],
             ["pro", "b) Zwei Gründe für unsere Entscheidung"], ["contra", "c) Das stärkste Gegenargument"], ["pruef", "d) Das würden wir noch nachprüfen"]],
  "chk": {"pro": {"kw": [["zwei Gründe", r"preis|kost|euro|€|teurer|billig|qualit|geschmack|bauer|kinder|arbeit|umwelt|bio|sieg|fair|lieferk|ruf|image|truppe|energie|sport|budget|glaub", 2]], "man": True},
          "contra": {"kw": [["ein Gegenargument", r"preis|kost|teurer|budget|beleg|studie|beweis|kontroll|siegel|nicht sicher|wenig|klein|markt|aber|trotzdem|gruppe|selbst"]], "man": True},
          "pruef": {"kw": [["Quelle / Zahl", r"quell|studie|zahl|daten|beleg|unabh|prüf|pruef|nachsehen|nachlesen|woher|wer hat|kontroll|vergleich|preis|kost"]], "man": True}},
  "sol": [["Hinweis", ["Keine Musterentscheidung. Gute Antworten nennen Kosten UND Wirkung und sagen, woher die Zahlen stammen (z. B. stammt die Fairtrade-Studie vom Herbst 2025 von Fairtrade und dem Impact Institute, nicht von einer unabhängigen Stelle).",
                       "Starke Gegenargumente: höhere Preise bei knappem Budget · Wirkung nur teilweise belegt · Siegel garantiert nicht alles · nur ein Teil des Sortiments ist fair.",
                       "Nachprüfen: unabhängige Studien, tatsächliche Preisunterschiede, Anteil von Fairtrade im Sortiment, Kontrollen der Lieferkette."]]],
  "tip": ["Diskussionsgrundlage", "theorie.html#diskussion"]},

 # ======================================================= Zusatz
 {"id": "a4", "nr": 4, "title": "Belegt oder nicht? Die Fairtrade-Studie", "src": "Buch S. 38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Lies im Theorieteil den Abschnitt »Was die Zahlen zeigen – und was nicht«. Entscheide bei jeder Aussage: belegt, nicht belegt (die Studie sagt dazu nichts) oder widerlegt (die Zahlen zeigen das Gegenteil). "
       "d) Schreibe Aussage c so um, dass sie durch die Zahlen gedeckt ist.",
  "hint": "Achte auf Wörter wie »keine«, »alle«, »allein«, »beweist«. Info: Theorieteil »Was die Zahlen zeigen – und was nicht«",
  "type": "multi",
  "fields": [["k1", "a) »Der Anteil der befragten Haushalte in extremer Armut ist von 58 % (2017) auf 17 % (2024) gesunken.«", BELEGT, False],
             ["k2", "b) »Mit Fairtrade gibt es in der Elfenbeinküste keine extreme Armut mehr.«", BELEGT, False],
             ["k3", "c) »Die Studie beweist, dass Fairtrade der einzige Grund für die Verbesserung ist.«", BELEGT, False],
             ["neu", "d) Aussage c, richtig umgeschrieben (1 Satz)"]],
  "chk": {"k1": {"sel": "belegt"}, "k2": {"sel": "widerlegt"}, "k3": {"sel": "nicht belegt"},
          "neu": {"kw": [["Studie zeigt / könnte", r"zeigt|deutet|hinweis|zusammenhang|könnte|koennte|mit dazu|auch|mehrere|nicht allein|nicht nur|laut|fairtrade selbst|befragt"]], "man": True}},
  "sol": [["Lösung", ["a) belegt – die Studie nennt 58 % (2017), 36 % (2020) und 17 % (2024).",
                      "b) widerlegt – 2024 lebten noch 17 % der Haushalte in extremer Armut.",
                      "c) nicht belegt – die Studie zeigt eine Entwicklung, aber nicht, dass Fairtrade der einzige Grund ist (auch Preise und andere Programme spielen mit).",
                      "d) z. B. »Die Studie zeigt, dass es den befragten Kakaobauern heute besser geht als früher – ob das allein an Fairtrade liegt, sagt sie nicht.«"]]],
  "tip": ["Was die Zahlen zeigen – und was nicht", "theorie.html#zahlen"]},

 {"id": "a5", "nr": 5, "title": "Siegel-Jagd in Kantine oder Supermarkt", "src": "Buch-Aufgabe S. 38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 10,
  "q": "Bewegungsaufgabe, allein oder zu zweit: Geh in die Kantine, ins Buffet oder in einen Supermarkt. Finde drei Produkte mit Fairtrade-Siegel und zu jedem ein ähnliches Produkt ohne Siegel. "
       "Notiere Produkt und Preis. Beurteile dann: Ist der Unterschied groß oder klein – und würdest du den Aufpreis zahlen?",
  "hint": "Kakao, Kaffee, Tee, Bananen, Zucker, Saft, Reis oder Baumwolle sind typische Fairtrade-Waren. Vergleiche gleiche Mengen (z. B. Preis pro 100 g). Info im Schulbuch S. 38 (Aufgabe 6).",
  "type": "multi",
  "fields": [["p1", "Produkt 1 (mit Siegel) · Preis · Vergleichsprodukt · Preis"], ["p2", "Produkt 2 (mit Siegel) · Preis · Vergleichsprodukt · Preis"], ["p3", "Produkt 3 (mit Siegel) · Preis · Vergleichsprodukt · Preis"],
             ["urteil", "Mein Urteil: Aufpreis ja oder nein – warum? (2 Sätze)"]],
  "chk": {"p1": {"kw": [["Produkt und Preis", r"\d"]], "man": True}, "p2": {"kw": [["Produkt und Preis", r"\d"]], "man": True}, "p3": {"kw": [["Produkt und Preis", r"\d"]], "man": True},
          "urteil": {"kw": [["Begründung", r"preis|teurer|billig|aufpreis|wert|lohn|bauer|fair|qualit|egal|ja|nein|weil"]], "man": True}},
  "sol": [["Hinweis", ["Eigene Beobachtung, keine Musterlösung. Gute Antworten vergleichen gleiche Mengen und sagen, ob der Preisunterschied im Alltag spürbar ist."]]],
  "tip": [ABSCHNITT_1, "theorie.html#fairhandel"]},

 {"id": "a6", "nr": 6, "title": "KI-Check: Stimmt, was die KI sagt?", "src": "Buch S. 36–38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Frag eine KI: »Bringt Fairtrade den Kakaobauern wirklich etwas?« Kopiere zwei Aussagen aus der Antwort. Suche für jede Aussage eine Quelle (Zahlen aus dem Theorieteil, Fairtrade Österreich oder eine unabhängige Studie) "
       "und entscheide, ob sie belegt ist. Wenn ein Beleg fehlt, schreib dazu, was du noch nachprüfen würdest.",
  "hint": "Die KI darf dir helfen – aber du prüfst. Frag auch nach Gegenargumenten. Info: Theorieteil »Was die Zahlen zeigen – und was nicht«",
  "type": "multi",
  "fields": [["a1", "Aussage 1 der KI"], ["b1", "Beleg gefunden? Quelle oder Hinweis"], ["a2", "Aussage 2 der KI"], ["b2", "Beleg gefunden? Quelle oder Hinweis"]],
  "chk": {"a1": {"kw": [["Aussage", r"[a-zäöüß]{4,}"]], "man": True}, "b1": {"kw": [["Quelle / Hinweis", r"quell|studie|fairtrade|beleg|nicht|www|http|zahl|prüf|pruef|\d"]], "man": True},
          "a2": {"kw": [["Aussage", r"[a-zäöüß]{4,}"]], "man": True}, "b2": {"kw": [["Quelle / Hinweis", r"quell|studie|fairtrade|beleg|nicht|www|http|zahl|prüf|pruef|\d"]], "man": True}},
  "sol": [["Hinweis", ["Eigene Recherche. Prüfen, ob Aussagen mit Zahlen (Prämie, Mindestpreis, Einkommen) zu den Angaben im Theorieteil passen und ob die KI Quellen nennt, die es wirklich gibt."]]],
  "tip": ["Was die Zahlen zeigen – und was nicht", "theorie.html#zahlen"]},

 {"id": "a7", "nr": 7, "title": "Partnercheck vor dem Test-Thema Fairtrade", "src": "Buch S. 35–38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Zu zweit, ohne Handy: A nimmt drei Karten aus dem Abschnitt »Partnercheck« im Theorieteil und liest die Fragen vor. B antwortet, A vergleicht mit der Antwort auf der Karte und hakt ab. "
       "Dann tauscht ihr. Trag ein, mit wem du geübt hast und wie viele deiner drei Antworten gepasst haben.",
  "hint": "Ehrlich zählen – es geht um deine Vorbereitung, nicht um Punkte.",
  "type": "multi",
  "fields": [["partner", "Partnercheck mit (Vorname)"], ["richtig", "Davon hat gepasst", ["3 von 3", "2 von 3", "1 von 3", "0 von 3"], False],
             ["unsicher", "Da war ich noch unsicher (Stichwort, freiwillig)"]],
  "opt": ["unsicher"],
  "chk": {"partner": {"kw": [["Name", r"[a-zäöüß]{2,}"]], "man": True}},
  "sol": [["Hinweis", ["Kein Lösungsschlüssel – die Antworten stehen auf den Karten im Theorieteil."]]],
  "tip": ["Partnercheck", "theorie.html#partnercheck"]},

 {"id": "a8", "nr": 8, "title": "Zwei Quellen, zwei Blickwinkel", "src": "Buch S. 38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 20,
  "q": "Gruppenpuzzle, zu zweit: Eine Person liest Quelle 1, die andere Quelle 2 (Links im Theorieteil, Abschnitt »Für Schnelle«). Erzählt euch gegenseitig in eigenen Worten, was in eurer Quelle steht. "
       "a) Kernaussage von Quelle 1 (1–2 Sätze) b) Kernaussage von Quelle 2 (1–2 Sätze) c) Wo ergänzen oder widersprechen sich die Quellen? d) Euer Urteil: Wie sicher ist die Wirkung von Fairtrade? Wer hat die Quelle geschrieben – und welches Interesse könnte er haben?",
  "hint": "Quelle 1 stammt von Fairtrade selbst, Quelle 2 ist ein älterer, kritischer Fachartikel. Info: Theorieteil »Für Schnelle« mit den Links",
  "type": "multi",
  "fields": [["q1", "a) Kernaussage Quelle 1"], ["q2", "b) Kernaussage Quelle 2"], ["vgl", "c) Ergänzen oder widersprechen sich die Quellen?"], ["urteil", "d) Unser Urteil und das Interesse der Autoren"]],
  "chk": {"q1": {"kw": [["Kernaussage", r"[a-zäöüß]{5,}"]], "man": True}, "q2": {"kw": [["Kernaussage", r"[a-zäöüß]{5,}"]], "man": True},
          "vgl": {"kw": [["Vergleich", r"ergänz|erganz|widerspr|aber|dagegen|ähnlich|aehnlich|beide|unterschied|kritik|nicht"]], "man": True},
          "urteil": {"kw": [["Urteil / Interesse", r"interesse|selbst|unabh|neutral|werb|studie|beleg|nicht sicher|teilweise|kritisch"]], "man": True}},
  "sol": [["Hinweis", ["Quelle 1 (Fairtrade Deutschland, Prämienstudie, Kurzfassung 2019): wie Prämie und Mindestpreis in Kooperativen wirken – Auftraggeber ist Fairtrade, das Ergebnis ist positiv gefärbt.",
                       "Quelle 2 (bpb, Aus Politik und Zeitgeschichte, 2012): Chancen UND Kritik – z. B. »fair« ist nicht geschützt, Siegel sind unübersichtlich, Gefahr von »Fair Washing«. Älter, Zahlen nicht mehr aktuell.",
                       "Gutes Urteil: beide Quellen zusammen lesen, Interessen nennen, unabhängige Studien suchen."]]],
  "tip": ["Für Schnelle", "theorie.html#schnelle"]},

 {"id": "a9", "nr": 9, "title": "Plakat, Video oder Podcast: Marketing für faire Produkte", "src": "Buch-Aufgabe S. 38", "own": True, "tag": "Zusatz", "h": 0, "zeit": 25,
  "q": "Kreativ und freiwillig, allein oder zu zweit: Entwickle ein Marketingkonzept für ein fair gehandeltes Produkt, das Kadetten wirklich kaufen würden (z. B. Energieriegel, Kaffee, Sporttrikot). "
       "Mach ein A3-Plakat (mit der Hand), ein Erklärvideo (höchstens 2 Minuten) oder einen Podcast (höchstens 3 Minuten). Pflichtinhalte: 1. Zielgruppe, 2. Slogan, 3. zwei Argumente mit belegten Fakten, 4. ein ehrlicher Hinweis, was das Siegel NICHT garantiert. "
       "Abgabe (freiwillig, Termin gibt Prof. HOLZER bekannt): Plakat als Foto ins PDF, Video oder Podcast als Datei in LMS (Teams nur, wenn die Datei zu groß ist). Trag hier Titel, Form und »hochgeladen am …« ein.",
  "hint": "Keine fremde Musik, keine fremden Bilder, keine echten Marken-Logos. Andere Personen nur mit Zustimmung aufnehmen. Wenn dir eine KI beim Skript hilft, schreib das dazu – und prüf den Inhalt.",
  "type": "multi",
  "fields": [["titel", "Titel"], ["form", "Form (Plakat, Video oder Podcast)"], ["inhalt", "Worum geht es? (1–2 Sätze)"], ["hoch", "hochgeladen in LMS am … / Plakat-Foto im PDF"]],
  "chk": {"titel": {"kw": [["Titel", r"[a-zäöüß]{3,}"]], "man": True}, "form": {"kw": [["Form", r"video|podcast|plakat|audio|film"]], "man": True},
          "inhalt": {"kw": [["Produkt / Zielgruppe", r"fair|siegel|kakao|kaffee|riegel|zielgruppe|slogan|preis|kunde|kadett"]], "man": True}, "hoch": {"kw": [["Abgabe", r"\d|lms|teams|foto|hochgeladen"]], "man": True}},
  "sol": [["Bewertung", ["Raster (10 P.): fachlich richtig 4 · alle vier Pflichtinhalte 2 · verständlich und gut gegliedert 2 · kreativ/ansprechend 1 · Länge und Abgabe eingehalten 1.",
                         "Muss vorkommen: Zielgruppe · Slogan · zwei belegte Fakten (z. B. Mindestpreis, Prämie, Einkommen laut Studie mit Quelle) · Grenze des Siegels (z. B. nicht automatisch Bio, keine Garantie für alles)."]]],
  "tip": [ABSCHNITT_1, "theorie.html#fairhandel"]},
]
assert [t["nr"] for t in T] == list(range(1, 10))
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
_c = {t["id"]: t["chk"] for t in T}
assert (_c["a2"]["pr"]["num"], _c["a2"]["er"]["num"], _c["a2"]["mehr"]["num"]) == (11000, 140000, 28000)

PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
BESPRECHEN = [1, 2, 3]
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True

GRP = {1: TEILNAME[1] + " (" + TEILBUCH[1] + ") · " + wann(1),
       2: TEILNAME[2] + " (" + TEILBUCH[2] + ") · " + wann(2),
       0: "Zusatz · Für Schnelle und Neugierige · freiwillig, keine Hausübung"}

LERNZIELE = ["erklären, was **fairer Handel** ist und auf welchen **drei Säulen** die Fairtrade-Standards stehen",
             "**Mindestpreis** und **Prämie** erklären und an einem Beispiel durchrechnen",
             "Aussagen zu Fairtrade als **belegt oder nicht belegt** einordnen und die **Quelle** kritisch prüfen",
             "eine **eigene Kaufentscheidung** mit Gründen und Gegenargumenten begründen"]

LEITFRAGE = "Was bringt das Fairtrade-Siegel den Menschen, die unseren Kakao anbauen – und was bringt es uns?"

WICHTIGSTE = ["**Fairer Handel** soll Bauernfamilien im globalen Süden bessere Preise, Arbeitsbedingungen und Perspektiven geben – das Siegel zeigt, dass **Standards** eingehalten und kontrolliert werden.",
              "Die Fairtrade-Standards stehen auf **drei Säulen**: **Soziales**, **Ökologisches** und **Ökonomisches**.",
              "Der **Mindestpreis** ist eine Untergrenze, wenn der Weltmarkt einbricht; die **Prämie** kommt zusätzlich und wird für Gemeinschaftsprojekte genutzt.",
              "Fairtrade ist **nicht automatisch Bio** und garantiert nicht alles – wie stark es wirkt, muss man mit **Zahlen und Quellen** prüfen.",
              "Studien von Fairtrade selbst sind nützlich, aber **nicht unabhängig** – ein gutes Urteil vergleicht mehrere Quellen."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["fairer Handel", "Handel, der Produzenten im globalen Süden bessere Preise, Arbeitsbedingungen und langfristige Handelsbeziehungen sichern soll"],
                ["Fairtrade-Siegel", "Gütesiegel, das zeigt, dass ein Produkt nach den Fairtrade-Standards erzeugt und gehandelt wurde; vergeben wird es von unabhängig kontrollierten Systemen, nicht vom Verkäufer selbst"],
                ["Standards", "Regeln, die Produzenten und Händler einhalten müssen – aufgebaut auf drei Säulen: Soziales, Ökologisches, Ökonomisches"],
                ["Mindestpreis", "Untergrenze, unter die der Preis nicht fallen darf; bei höherem Marktpreis gilt der Marktpreis"],
                ["Fairtrade-Prämie", "Geldbetrag, der zusätzlich zum Preis gezahlt wird; die Kooperative entscheidet gemeinsam, wofür sie ihn nutzt (z. B. Schule, Brunnen, Gesundheit)"],
                ["Kooperative", "Zusammenschluss vieler Kleinbauernfamilien, um gemeinsam zu verkaufen und mitzubestimmen"],
                ["Weltmarktpreis", "Preis, zu dem ein Rohstoff an der Börse gehandelt wird; er kann stark schwanken"],
                ["existenzsicherndes Einkommen", "Einkommen, mit dem eine Familie Essen, Wohnen, Schule und Gesundheit bezahlen kann (englisch: living income)"],
                ["Rückverfolgbarkeit", "Möglichkeit, den Weg einer Ware vom Anbau bis ins Regal nachzuvollziehen"],
                ["Land Grabbing", "gezielte Vertreibung von Menschen von ihrem Land – oft mit staatlicher Unterstützung – um dort Intensiv-Landwirtschaft zu betreiben"],
                ["Fair Washing", "Werbung, die ein Produkt fairer darstellt, als die Belege hergeben – vergleichbar mit Greenwashing"]]

WEISST_DU_NOCH = {}

STOPPFRAGEN = {
    1: [("Ist ein Produkt mit Fairtrade-Siegel automatisch Bio?", "Nein – die Standards fördern Bio-Anbau, verlangen ihn aber nicht in jedem Fall. Fair und Bio sind zwei verschiedene Dinge."),
        ("Nenne ein Beispiel für jede der drei Säulen.", "z. B. Soziales: Verbot ausbeuterischer Kinderarbeit · Ökologisches: Liste verbotener Pestizide · Ökonomisches: Rückverfolgbarkeit der Ware.")],
    2: [("Der Weltmarktpreis liegt über dem Mindestpreis. Bringt der Mindestpreis dann etwas?", "Dann gilt der höhere Marktpreis. Der Mindestpreis ist ein Sicherheitsnetz für den Fall, dass der Weltmarkt einbricht – die Prämie kommt in beiden Fällen dazu."),
        ("Die Studie über das Einkommen der Kakaobauern stammt von Fairtrade selbst. Was folgt daraus?", "Die Zahlen sind eine Information, aber keine unabhängige Prüfung. Man vergleicht sie mit anderen Quellen und fragt, wer die Daten erhoben hat.")],
}

PARTNERKARTEN = [("Was ist fairer Handel – in einem Satz?", "Handel, der Produzenten im globalen Süden bessere Preise, Arbeitsbedingungen und stabile Handelsbeziehungen sichern soll."),
                 ("Nenne die drei Säulen der Fairtrade-Standards.", "Soziales, Ökologisches, Ökonomisches."),
                 ("Was ist der Unterschied zwischen Mindestpreis und Prämie?", "Der Mindestpreis ist die Untergrenze für den Verkaufspreis. Die Prämie ist zusätzliches Geld für Gemeinschaftsprojekte."),
                 ("Warum ist ein Fairtrade-Produkt nicht automatisch Bio?", "Fairtrade fördert Bio-Anbau, schreibt ihn aber nicht in jedem Fall vor – Fair und Bio sind verschiedene Siegel."),
                 ("Was bedeutet Land Grabbing?", "Menschen werden gezielt von ihrem Land vertrieben, damit dort Intensiv-Landwirtschaft betrieben werden kann."),
                 ("Warum sollte man einer Fairtrade-Studie von Fairtrade selbst nicht blind vertrauen?", "Wer ein Interesse am Ergebnis hat, wählt vielleicht Daten günstig aus. Man vergleicht mit unabhängigen Quellen.")]

STOLPERSTEINE = [("Fairtrade = Bio", "Beides sind eigene Siegel. Fairtrade fördert Bio-Anbau, verlangt ihn aber nicht überall."),
                 ("Mindestpreis = immer der Preis", "Liegt der Weltmarkt höher, gilt der höhere Marktpreis. Der Mindestpreis ist nur die Untergrenze."),
                 ("Prämie = Lohn", "Die Prämie kommt zusätzlich zum Preis und geht an die Gemeinschaft, nicht als Lohn an Einzelne."),
                 ("Studie = Beweis", "Eine Studie von Fairtrade selbst zeigt eine Entwicklung, beweist aber nicht, dass Fairtrade der einzige Grund ist."),
                 ("»Fair« = geschützter Begriff", "Das Wort »fair« ist nicht gesetzlich geschützt – darum zählt, wer das Siegel vergibt und kontrolliert.")]

QUIZ = [
 ("Fairer Handel", "Was ist das Ziel von fairem Handel?", ["bessere Preise und Bedingungen für Produzenten im globalen Süden", "möglichst niedrige Preise für Käufer", "mehr Werbung für Markenprodukte", "weniger Handel mit dem Ausland"],
  "Fairer Handel soll Bauernfamilien bessere Preise, Arbeitsbedingungen und stabile Handelsbeziehungen sichern.", "Buch S. 35–36"),
 ("Standards", "Auf welchen drei Säulen stehen die Fairtrade-Standards?", ["Soziales, Ökologisches, Ökonomisches", "Preis, Qualität, Werbung", "Bio, Regional, Saisonal", "Kontrolle, Gewinn, Verpackung"],
  "Das Schulbuch (S. 37) zeigt die drei Säulen – sie entsprechen den drei Säulen der Nachhaltigkeit.", "Buch S. 37"),
 ("Standards", "Welches Beispiel gehört zu den sozialen Standards?", ["Verbot ausbeuterischer Kinderarbeit", "Liste verbotener Pestizide", "Rückverfolgbarkeit der Ware", "Förderung des Bio-Anbaus"],
  "Kinderarbeit und gewerkschaftliche Organisation gehören zum Sozialen; Pestizide und Bio zum Ökologischen; Rückverfolgbarkeit zum Ökonomischen.", "Buch S. 37"),
 ("Standards", "Welches Beispiel gehört zu den ökologischen Standards?", ["Liste verbotener Pestizide", "transparente Handelsbeziehungen", "Verbot von Kinderarbeit", "Förderung von Gewerkschaften"],
  "Der Schutz von Boden und Wasser sowie Bio-Anbau zählen zum Ökologischen.", "Buch S. 37"),
 ("Mindestpreis", "Was ist der Fairtrade-Mindestpreis?", ["eine Untergrenze für den Preis", "der Preis im Supermarkt", "ein Zuschlag für Bio", "der Gewinn der Händler"],
  "Er ist ein Sicherheitsnetz: Fällt der Weltmarktpreis darunter, bekommen die Produzenten trotzdem den Mindestpreis.", "Buch S. 37"),
 ("Mindestpreis", "Der Weltmarktpreis liegt höher als der Mindestpreis. Was gilt?", ["der höhere Marktpreis", "weiter der Mindestpreis", "gar kein Preis", "der Mindestpreis minus Prämie"],
  "Der Mindestpreis ist nur die Untergrenze. Liegt der Markt höher, gilt der Marktpreis.", "Buch S. 37–38"),
 ("Prämie", "Wofür wird die Fairtrade-Prämie genutzt?", ["für Gemeinschaftsprojekte, über die die Mitglieder entscheiden", "als Lohn für einzelne Bauern", "für Werbung des Händlers", "für die Verpackung"],
  "Die Kooperative entscheidet gemeinsam, z. B. über Schulen, Brunnen oder bessere Anbaumethoden.", "Buch S. 37"),
 ("Rechnung", "40 Tonnen Kakao, Prämie 275 US-Dollar je Tonne. Wie hoch ist die Prämie?", ["11.000 US-Dollar", "275 US-Dollar", "140.000 US-Dollar", "1.100 US-Dollar"],
  "40 × 275 = 11.000. Die Prämie kommt zusätzlich zum Preis.", "Buch S. 37"),
 ("Land Grabbing", "Was bedeutet Land Grabbing?", ["Menschen werden von ihrem Land vertrieben, damit dort Intensiv-Landwirtschaft entsteht", "Bauern kaufen gemeinsam Land", "Land wird aufgeforstet", "ein Handelsabkommen über Getreide"],
  "Fairtrade engagiert sich dagegen, weil Kleinbauernfamilien ihre Lebensgrundlage verlieren.", "Buch S. 37"),
 ("Quellen", "Fairtrade veröffentlicht eine Studie über seine eigene Wirkung. Was ist sinnvoll?", ["Ergebnisse mit unabhängigen Quellen vergleichen", "alles glauben, weil es Zahlen sind", "alles ablehnen, weil es Werbung ist", "nur die Überschrift lesen"],
  "Zahlen von Fairtrade selbst sind nützlich, aber nicht unabhängig – man vergleicht und fragt nach der Methode.", "Buch S. 38"),
 ("Bio", "Ist ein Fairtrade-Produkt automatisch Bio?", ["nein – Fairtrade fördert Bio, verlangt es aber nicht in jedem Fall", "ja, immer", "nur bei Kaffee", "nur bei Schokolade"],
  "Fair und Bio sind zwei verschiedene Siegel mit eigenen Regeln.", "Buch S. 37"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
