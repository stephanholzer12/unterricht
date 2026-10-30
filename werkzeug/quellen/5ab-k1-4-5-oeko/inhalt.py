"""TÖW 5AB · K1.4–1.5 Ökodesign und Ökobilanz (Trauner TÖW, S. 19–25) – v1.
Grundlage: ChatGPT-Übergabe v3 vom 29.10.2026 (Planung, Minutenplan, Aufgaben 1–3 mit Lösungen, Quellen Q1–Q9) – von Claude nach dem
Regelwerk (14. Fassung, 29.10.2026) umgesetzt und fachlich nachgeprüft (Prüfbericht).
Jahresplan v22, Zeile 9: Einheit 3 (E3), 2 Std. Kern, K01, K02, N08–N10, P1–P3, SDG 12, Schulprofil »Lebenszyklus eines Ausrüstungsgegenstands«.
Stephan: EINE Stunde je Klasse – 5BK Di 03.11.2026, 5AK Do 05.11.2026 (Annahme 50 min). Test am 12.11.2026 (Umfang offen).
Eine Quelle für Handy-Seiten, Word, PPPs und Lösungsmappe. Keine Versuche (V5.3 bleibt spätere Erweiterung). Keine Kahoot-Tabelle (Stephan, 30.10.2026).
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "30.10.2026"
V = "v1"
ORDNER = "5ab-toew/k1-4-5-oeko"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ab-toew/"
EYEBROW = "TÖW · 5AB · K1.4–1.5 Ökodesign und Ökobilanz"
TITEL = "Ökodesign und Ökobilanz – Ausrüstung über ihre ganze Nutzung bewerten"
KURZTITEL = "Ökodesign und Ökobilanz"
BUCH = "Buch S. 19–25"
KEY = "26-27-5AB-K1.4-1.5-Oeko-TH-Handy-v1"
CHECK_KEY = "26-27-5AB-K1.4-1.5-Oeko-Lernseite-Check-v1"
PRAEFIX = "26-27-5AB-K1.4-1.5-Oeko"
KAP = "K1.4–1.5"
TEST = "Do 12.11.2026"

# Kein Video im Pflichtablauf (eine Stunde). Kein kurzes, seriöses deutschsprachiges Video war von hier aus prüfbar (YouTube gesperrt) – siehe Prüfbericht.
VIDEOS = {}
FREIGEGEBEN = set()


def zeigen(key, lehrer=False):
    return key in FREIGEGEBEN


KLASSEN = ["5BK", "5AK"]          # Reihenfolge nach Termin
DATEN = {"5BK": {1: "Di 03.11."}, "5AK": {1: "Do 05.11."}}
TEIL_STUNDE = {1: {"5BK": 1, "5AK": 1}, 2: {"5BK": 1, "5AK": 1}}
TEILNAME = {1: "Teil 1 · Ökodesign", 2: "Teil 2 · Ökobilanz"}
TEILBUCH = {1: "Buch S. 19–21", 2: "Buch S. 22–25"}
ABSCHNITT_1 = "Ökodesign: Umweltwirkungen bei der Entwicklung mitdenken"
ABSCHNITT_2 = "Ökobilanz: dieselbe Leistung fair vergleichen"


def wann(teil=1):
    return " · ".join(f"{k}: {DATEN[k][1]}" for k in KLASSEN)


LZ_PHASEN = ["Rohstoffe", "Herstellung", "Transport und Verkauf", "Nutzung und Pflege", "Nutzungsende (wiederverwenden, verwerten, entsorgen)"]
OE1 = ["umweltgerechten Gestalten eines Produkts", "Ermitteln und Bewerten der Umweltwirkungen", "Werben mit einem grünen Logo", "Senken des Kaufpreises"]
OE2 = ["Ermitteln und Bewerten der Umweltwirkungen", "umweltgerechten Gestalten eines Produkts", "Werben mit einem grünen Logo", "Senken des Kaufpreises"]
BELEGT = ["belegt", "nicht belegt", "widerlegt"]

# Modelldaten Aufgabe 2 (frei erfunden, keine Messwerte echter Produkte)
N = 1000
MODELL = {"A": {"nutz": 200, "preis": 8, "herst": 3.0, "ende": 0.2, "rein": 0.01, "rk": 0.02},
          "B": {"nutz": 1000, "preis": 30, "herst": 6.0, "ende": 0.5, "rein": 0.01, "rk": 0.02}}


def rechne(m, n=N):
    import math
    fl = math.ceil(n / m["nutz"])
    return {"fl": fl, "herst": fl * m["herst"], "ende": fl * m["ende"], "rein": n * m["rein"],
            "klima": fl * (m["herst"] + m["ende"]) + n * m["rein"], "kauf": fl * m["preis"], "rk": n * m["rk"],
            "kosten": fl * m["preis"] + n * m["rk"]}


R = {k: rechne(v) for k, v in MODELL.items()}
R_B500 = rechne(dict(MODELL["B"], nutz=500))
_r = lambda x: round(x, 6)
assert (R["A"]["fl"], R["B"]["fl"]) == (5, 1)
assert (_r(R["A"]["klima"]), _r(R["B"]["klima"])) == (26.0, 16.5)
assert (_r(R["A"]["kosten"]), _r(R["B"]["kosten"])) == (60.0, 50.0)
assert (R_B500["fl"], _r(R_B500["klima"]), _r(R_B500["kosten"])) == (2, 23.0, 80.0)
assert _r(R["A"]["klima"] - R["B"]["klima"]) == 9.5 and R["A"]["kosten"] - R["B"]["kosten"] == 10

DATENTABELLE = [["Modelldaten (erfunden)", "Flasche A", "Flasche B"],
                ["Nutzungen pro Flasche", "200", "1.000"],
                ["Kaufpreis pro Flasche", "8 €", "30 €"],
                ["Herstellung mit Rohstoffen und Lieferung (pro Flasche)", "3 kg CO₂-Äq.", "6 kg CO₂-Äq."],
                ["Endbehandlung am Nutzungsende (pro Flasche)", "0,2 kg CO₂-Äq.", "0,5 kg CO₂-Äq."],
                ["Reinigung (pro Nutzung)", "0,01 kg CO₂-Äq.", "0,01 kg CO₂-Äq."],
                ["Reinigungskosten (pro Nutzung)", "0,02 €", "0,02 €"]]
MODELL_HINWEIS = "Frei erfundene Modelldaten zum Üben – keine Messwerte echter Produkte. Wir rechnen nur ausgewählte Treibhausgas-Beiträge und vereinfachte Kosten, keine vollständige Ökobilanz."
SYSTEMGRENZE = ("Systemgrenze: Einbezogen sind Herstellung samt Rohstoffen und Lieferung, die Reinigung und die Endbehandlung aller nötigen Flaschen. "
                "Nicht eingerechnet sind das Trinkwasser selbst und die Ersatzteile für B. Eine zusätzliche Recycling-Gutschrift gibt es nicht – mögliche Gutschriften sind in der Endbehandlung schon eingerechnet.")
RECHENWEG = [("Anzahl Flaschen", "1.000 Nutzungen : Nutzungen pro Flasche (bei einem Rest auf ganze Flaschen aufrunden)"),
             ("Klimawirkung", "Flaschen × (Herstellung + Endbehandlung) + 1.000 × Reinigung pro Nutzung"),
             ("Kosten", "Flaschen × Kaufpreis + 1.000 × Reinigungskosten pro Nutzung")]

T = [
 # ======================================================= Teil 1 · Ökodesign (Buch S. 19–21)
 {"id": "a1", "nr": 1, "title": "Eine Trinkflasche verbessern", "src": "Buch S. 20", "own": True, "tag": "Teil 1", "h": 1, "zeit": 5,
  "q": "Zu zweit, zuerst ohne Handy am Mini-Whiteboard oder im Heft: Ein Hersteller will seine Ein-Liter-Trinkflasche für Sport und Ausbildung überarbeiten. "
       "Sie muss dicht, hygienisch und robust bleiben. a) Schlagt drei konkrete Verbesserungen vor. Schreibt dazu als Tabelle: Verbesserung · Abschnitt im Lebenszyklus · erwartete Wirkung. "
       "Fotografiert eure Tabelle. b) Beschreibt in einem Satz einen Zielkonflikt – also eine Verbesserung, die ein anderes Ziel schwieriger macht.",
  "hint": "Abschnitte im Lebenszyklus: Rohstoffe → Herstellung → Transport und Verkauf → Nutzung und Pflege → Nutzungsende. Info: Theorieteil »" + ABSCHNITT_1 + "«",
  "type": "sketch", "ptab": ["Verbesserung", "Abschnitt im Lebenszyklus", "erwartete Wirkung"],
  "fields": [["konflikt", "b) Ein Zielkonflikt (1 Satz)"]],
  "chk": {"konflikt": {"kw": [["zwei Ziele, die sich widersprechen", r"gegen|aber|dafür|dafuer|jedoch|weniger|mehr|leicht|schwer|dünn|duenn|dick|robust|stabil|bruch|bricht|teurer|billig|isolier|gewicht|material|zerleg|trenn"]], "man": True}},
  "sol": [["Beispiel-Tabelle", ["Deckel und Dichtung nachkaufbar · Nutzung und Pflege · ein kleiner Defekt erzwingt keine neue Flasche.",
                               "Weite Öffnung, keine engen Ecken · Nutzung und Pflege · leichter hygienisch zu reinigen.",
                               "Wenige, trennbare, gekennzeichnete Materialien · Herstellung und Nutzungsende · weniger Material, sortenrein verwertbar.",
                               "Andere nachvollziehbare Vorschläge zählen; »weniger Material« nur, wenn die Flasche dicht und robust bleibt."]],
          ["Zielkonflikt", ["z. B. dünnere Wand spart Material und Gewicht, hält aber Stöße schlechter aus – oder: Isolierung hält kühl, braucht aber mehr Material und ist schwer zu zerlegen."]]],
  "fsol": {"konflikt": "z. B. dünnere Wand spart Material, hält aber Stöße schlechter aus"},
  "fsol_rest": ["Tabelle (Beispiel): Deckel und Dichtung nachkaufbar · Nutzung/Pflege · kein Neukauf bei kleinem Defekt",
                "Weite Öffnung · Nutzung/Pflege · leichter hygienisch zu reinigen",
                "Trennbare, gekennzeichnete Materialien · Herstellung/Nutzungsende · sortenrein verwertbar"],
  "tip": [ABSCHNITT_1, "theorie.html#oekodesign"]},

 # ======================================================= Teil 2 · Ökobilanz (Buch S. 22–25)
 {"id": "a2", "nr": 2, "title": "Beschaffung für 1.000 Nutzungen", "src": "Buch S. 23–24", "own": True, "tag": "Teil 2", "h": 2, "zeit": 11,
  "q": "Zu zweit: Für Sport und Ausbildung sollen neue Trinkflaschen beschafft werden. Vergleicht die Modelle A und B für 1.000 Nutzungen einer dichten, hygienisch geeigneten "
       "Ein-Liter-Flasche. Eine Nutzung heißt: befüllen, verwenden, danach reinigen. Beide Modelle erfüllen dieselben Sicherheits- und Hygieneanforderungen, gehen nicht verloren "
       "und erreichen ihre Nutzungsdauer – B, weil Deckel und Dichtung getauscht werden können (diese Ersatzteile sind im Modell nicht eingerechnet). a) Formuliert die gemeinsame Vergleichsleistung und erklärt, warum das Trinkwasser weggelassen werden darf. "
       "b) Berechnet für beide Modelle die Anzahl der Flaschen, die Klimawirkung und die Gesamtkosten (nur die Zahl eintragen). "
       "c) Empfehlt ein Modell. Begründet mit einem ökologischen und einem wirtschaftlichen Argument und nennt eine Information, die für ein umfassendes Umwelturteil noch fehlt.",
  "hint": "Rechenweg: Flaschen = 1.000 : Nutzungen pro Flasche · Klima = Flaschen × (Herstellung + Endbehandlung) + 1.000 × Reinigung · Kosten = Flaschen × Kaufpreis + 1.000 × Reinigungskosten. Info: Theorieteil »So rechnest du den Flaschenvergleich«",
  "tab": DATENTABELLE, "tabnote": MODELL_HINWEIS + " " + SYSTEMGRENZE,
  "tabnote_folie": "Erfundene Modelldaten – keine echten Produkte, keine vollständige Ökobilanz. Einbezogen: Herstellung mit Lieferung, Reinigung, Endbehandlung. Nicht einbezogen: Trinkwasser, Ersatzteile für B. Keine zusätzliche Recycling-Gutschrift.",
  "type": "multi",
  "fields": [["fe", "a) Gemeinsame Vergleichsleistung (funktionale Einheit)"], ["wasser", "a) Warum darf das Trinkwasser weggelassen werden? (1 Satz)"],
             ["nA", "b) Flasche A: Anzahl Flaschen"], ["nB", "b) Flasche B: Anzahl Flaschen"],
             ["kA", "b) Flasche A: Klimawirkung in kg CO₂-Äquivalenten"], ["kB", "b) Flasche B: Klimawirkung in kg CO₂-Äquivalenten"],
             ["eA", "b) Flasche A: Gesamtkosten in Euro"], ["eB", "b) Flasche B: Gesamtkosten in Euro"],
             ["wahl", "c) Wir empfehlen", ["Flasche B", "Flasche A", "beide gleich gut"]],
             ["oeko", "c) Ökologisches Argument (1 Satz)"], ["wirt", "c) Wirtschaftliches Argument (1 Satz)"], ["fehlt", "c) Diese Information fehlt noch (1 Satz)"]],
  "chk": {"fe": {"kw": [["1.000", r"1[.\s',]?000|tausend"], ["Nutzungen", r"nutz|verwend|befüll|befuell|einsatz|einsätz|einsaetz|gebrauch|füllung|fuellung|trinkvorg|liter|[-\s]mal\b"]]},
          "wasser": {"kw": [["bei A und B gleich", r"gleich|beide|beiden|hebt|aufheb|unterschied|egal|dasselbe|selbe"]], "man": True},
          "nA": {"num": 5, "tol": 0}, "nB": {"num": 1, "tol": 0}, "kA": {"num": 26, "tol": 0.05}, "kB": {"num": 16.5, "tol": 0.05}, "eA": {"num": 60, "tol": 0.05}, "eB": {"num": 50, "tol": 0.05},
          "wahl": {"sel": "Flasche B"},
          "oeko": {"kw": [["Klimawirkung kleiner", r"klima|co2|co₂|co 2|treibhaus|emission|16[,.]5|9[,.]5|weniger"]], "man": True},
          "wirt": {"kw": [["Kosten über 1.000 Nutzungen", r"kost|euro|€|billig|günstig|guenstig|50|10|preis|spar"]], "man": True},
          "fehlt": {"kw": [["weitere Umweltwirkung oder echte Daten", r"wasser|ressourc|rohstoff|versauer|überdüng|ueberdueng|eutroph|giftig|toxi|lebensdauer|nutzungsdauer|real|echt|daten|material|ozon|fläche|flaeche|gesundheit|abfall|müll|muell|mikroplastik"]], "man": True}},
  "sol": [["a) Vergleichsleistung und Grenzen", ["1.000 Nutzungen einer dichten, hygienisch geeigneten Ein-Liter-Trinkflasche.",
                                               "Das Trinkwasser ist bei A und B gleich – im Vergleich hebt es sich auf und darf deshalb weggelassen werden (das muss man aber dazuschreiben)."]],
          ["b) Rechnung", ["Flaschen: A 1.000 : 200 = 5 · B 1.000 : 1.000 = 1",
                           "Klima A: 5 × (3 + 0,2) + 1.000 × 0,01 = 16 + 10 = 26 kg CO₂-Äq.",
                           "Klima B: 1 × (6 + 0,5) + 1.000 × 0,01 = 6,5 + 10 = 16,5 kg CO₂-Äq.",
                           "Kosten A: 5 × 8 € + 1.000 × 0,02 € = 40 € + 20 € = 60 €",
                           "Kosten B: 1 × 30 € + 1.000 × 0,02 € = 30 € + 20 € = 50 €"]],
          ["c) Urteil", ["Für die angenommenen 1.000 Nutzungen empfehlen wir Flasche B: Sie verursacht im Modell 9,5 kg CO₂-Äquivalente weniger und kostet insgesamt 10 € weniger.",
                         "Für ein umfassendes Umwelturteil fehlen z. B. Wasser- und Ressourcenverbrauch, weitere Umweltwirkungen oder echte Daten zur Lebensdauer.",
                         "Nicht erlaubt: »B ist in jeder Hinsicht umweltfreundlicher« oder »Metall ist immer besser als Kunststoff« – das Material ist im Modell gar nicht festgelegt."]]],
  "fsol": {"fe": "1.000 Nutzungen einer dichten, hygienischen Ein-Liter-Flasche", "wasser": "bei A und B gleich – hebt sich im Vergleich auf", "nA": "5", "nB": "1", "kA": "26 kg CO₂-Äq.", "kB": "16,5 kg CO₂-Äq.", "eA": "60 €", "eB": "50 €",
           "oeko": "B: 9,5 kg CO₂-Äq. weniger für 1.000 Nutzungen", "wirt": "B: insgesamt 10 € billiger (50 statt 60 €)", "fehlt": "z. B. Wasser, Rohstoffe, echte Lebensdauerdaten"},
  "fsol_rest": ["Rechnung: A 5 × (3 + 0,2) + 1.000 × 0,01 = 26 kg · B 1 × (6 + 0,5) + 10 = 16,5 kg · Kosten A 5 × 8 + 20 = 60 € · B 30 + 20 = 50 €",
                "Nicht erlaubt: »B ist in jeder Hinsicht umweltfreundlicher« oder »Metall ist immer besser« – nur Klima und Kosten, Material nicht festgelegt."],
  "tip": ["So rechnest du den Flaschenvergleich", "theorie.html#rechnen"]},

 {"id": "a3", "nr": 3, "title": "Abschlusscheck", "src": "Buch S. 20, 23–25", "own": True, "tag": "Teil 2", "h": 2, "zeit": 4,
  "q": "Allein, ohne nachzuschauen: a) Ergänze die beiden Sätze. b) Warum wäre der Vergleich »eine Flasche A gegen eine Flasche B« in unserem Fall unfair? (1 Satz) "
       "c) Nenne eine Umweltfrage, die unsere CO₂-Rechnung nicht beantwortet.",
  "hint": "Denk an die gemeinsame Vergleichsleistung und an die Wirkungskategorien. Info: Theorieteil »Sachbilanz und Wirkungsabschätzung«",
  "type": "multi",
  "fields": [["oe1", "a) Ökodesign hilft beim …", OE1], ["oe2", "a) Eine Ökobilanz hilft beim …", OE2],
             ["fair", "b) Warum unfair? (1 Satz)"], ["frage", "c) Eine Umweltfrage, die offen bleibt"]],
  "chk": {"oe1": {"sel": OE1[0]}, "oe2": {"sel": OE2[0]},
          "fair": {"kw": [["unterschiedliche Nutzungsdauer bzw. Leistung", r"nutzung|hält|haelt|halten|lebensdauer|200|1[.]?000|leistung|ersatz|öfter|oefter|mehrere|fünf|fuenf|5 flaschen|länger|laenger|kaputt|nachkauf"]], "man": True},
          "frage": {"kw": [["andere Umweltwirkung", r"wasser|ressourc|rohstoff|material|energie|versauer|überdüng|ueberdueng|eutroph|giftig|toxi|schadstoff|ozon|fläche|flaeche|landnutz|lärm|laerm|artenviel|biodivers|abfall|müll|muell|plastik|verschmutz|gewässer|gewaesser|feinstaub|smog|gesundheit|boden|strahl"]], "man": True}},
  "sol": [["Lösung", ["a) Ökodesign hilft beim umweltgerechten Gestalten eines Produkts; eine Ökobilanz hilft beim Ermitteln und Bewerten seiner Umweltwirkungen.",
                      "b) A hält nur 200 Nutzungen, B 1.000 – eine Flasche A bringt also viel weniger Leistung. Fair ist nur der Vergleich für dieselbe Leistung (1.000 Nutzungen = 5 A gegen 1 B).",
                      "c) z. B. Wasserverbrauch, Rohstoff- und Ressourcenverbrauch, Versauerung, Überdüngung, giftige Stoffe – unsere Rechnung erfasst nur die Klimawirkung."]]],
  "tip": ["Sachbilanz und Wirkungsabschätzung", "theorie.html#wirkung"]},

 # ======================================================= Zusatz · Für Schnelle und zur Wiederholung
 {"id": "a4", "nr": 4, "title": "Partnercheck vor dem Test", "src": "Buch S. 19–25", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Zu zweit, ohne Handy: A nimmt drei Karten aus dem Abschnitt »Partnercheck« im Theorieteil und liest die Fragen vor. B antwortet, A vergleicht mit der Antwort auf der Karte und hakt ab. "
       "Dann tauscht ihr. Trag ein, mit wem du geübt hast und wie viele deiner drei Antworten gepasst haben.",
  "hint": "Ehrlich zählen – es geht um deine Vorbereitung auf den Test, nicht um Punkte.",
  "type": "multi",
  "fields": [["partner", "Partnercheck mit (Vorname)"], ["richtig", "Davon hat gepasst", ["3 von 3", "2 von 3", "1 von 3", "0 von 3"], False],
             ["unsicher", "Da war ich noch unsicher (Stichwort, freiwillig)"]],
  "opt": ["unsicher"],
  "chk": {"partner": {"kw": [["Name", r"[a-zäöüß]{2,}"]], "man": True}},
  "sol": [["Hinweis", ["Kein Lösungsschlüssel – die Antworten stehen auf den Karten im Theorieteil. Unsichere Punkte bitte vor dem Test noch einmal lesen."]]],
  "tip": ["Partnercheck", "theorie.html#partnercheck"]},

 {"id": "a5", "nr": 5, "title": "KI-Check: Was ist belegt?", "src": "Buch S. 24–25", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Eine KI hat zu unserem Flaschenvergleich (Aufgabe 2) drei Sätze geschrieben. Entscheide bei jedem: belegt, nicht belegt (die Daten sagen dazu nichts) oder widerlegt (die Daten zeigen das Gegenteil). "
       "d) Schreib den ersten Satz so um, dass er stimmt. Tipp: Lass dir ruhig selbst von einer KI einen Vergleich schreiben – und prüf ihn genauso streng.",
  "hint": "Was haben wir gerechnet – nur Klima und Kosten über 1.000 Nutzungen? Vergleiche auch Kaufpreis und Gesamtkosten. Info: Theorieteil »Sachbilanz und Wirkungsabschätzung«",
  "type": "multi",
  "fields": [["k1", "a) »Flasche B ist in jeder Hinsicht umweltfreundlicher, weil sie weniger CO₂ verursacht.«", BELEGT, False],
             ["k2", "b) »Flasche B ist billiger, weil ihr Kaufpreis niedriger ist.«", BELEGT, False],
             ["k3", "c) »Für 1.000 Nutzungen verursacht B im Modell 9,5 kg CO₂-Äquivalente weniger als A.«", BELEGT, False],
             ["neu", "d) Der erste Satz, richtig umgeschrieben (1 Satz)"]],
  "chk": {"k1": {"sel": "nicht belegt"}, "k2": {"sel": "widerlegt"}, "k3": {"sel": "belegt"},
          "neu": {"kw": [["nur Klima / nur im Modell", r"klima|co2|co₂|treibhaus|modell|1[.]?000|diese[rn]? (leistung|annahme)|unter|angenommen"]], "man": True}},
  "sol": [["Lösung", ["a) nicht belegt – wir haben nur die Klimawirkung gerechnet; über Wasser, Rohstoffe oder Schadstoffe sagt die Zahl nichts.",
                      "b) widerlegt – der Kaufpreis von B ist höher (30 € statt 8 €). Billiger ist B nur über 1.000 Nutzungen gerechnet: 50 € statt 60 €.",
                      "c) belegt – 26 − 16,5 = 9,5 kg CO₂-Äquivalente.",
                      "d) z. B. »Für 1.000 Nutzungen hat Flasche B im Modell die geringere Klimawirkung – über andere Umweltwirkungen sagt das nichts.«"]]],
  "tip": ["Sachbilanz und Wirkungsabschätzung", "theorie.html#wirkung"]},

 {"id": "a6", "nr": 6, "title": "Was, wenn B früher kaputtgeht?", "src": "Buch S. 24", "own": True, "tag": "Zusatz", "h": 0, "zeit": 4,
  "q": "Maturaniveau: Nimm an, Flasche B hält entgegen der Angabe nur 500 Nutzungen. Alle anderen Modelldaten aus Aufgabe 2 bleiben gleich. "
       "Berechne für 1.000 Nutzungen a) die Anzahl der B-Flaschen, b) die Klimawirkung, c) die Gesamtkosten von B (nur die Zahl). d) Was folgt daraus?",
  "hint": "Gleicher Rechenweg wie in Aufgabe 2 – nur die Nutzungen pro Flasche B ändern sich. Vergleiche danach mit A (26 kg, 60 €).",
  "type": "multi",
  "fields": [["n", "a) Anzahl B-Flaschen"], ["k", "b) Klimawirkung B in kg CO₂-Äquivalenten"], ["e", "c) Gesamtkosten B in Euro"],
             ["folge", "d) Daraus folgt …", ["B bleibt beim Klima besser als A, ist aber teurer.", "B ist jetzt in beiden Punkten schlechter als A.", "B bleibt in beiden Punkten besser als A."]]],
  "chk": {"n": {"num": 2, "tol": 0}, "k": {"num": 23, "tol": 0.05}, "e": {"num": 80, "tol": 0.05}, "folge": {"sel": "B bleibt beim Klima besser als A, ist aber teurer."}},
  "sol": [["Lösung", ["a) 1.000 : 500 = 2 Flaschen B",
                      "b) 2 × (6 + 0,5) + 1.000 × 0,01 = 13 + 10 = 23 kg CO₂-Äquivalente",
                      "c) 2 × 30 € + 1.000 × 0,02 € = 60 € + 20 € = 80 €",
                      "d) B bleibt beim Klima unter A (23 statt 26 kg), ist aber teurer (80 statt 60 €). Die Lebensdauer-Annahme entscheidet mit – Klima und Kosten müssen getrennt geprüft werden."]]],
  "tip": ["So rechnest du den Flaschenvergleich", "theorie.html#rechnen"]},

 {"id": "a7", "nr": 7, "title": "»50 % weniger CO₂« – reicht das?", "src": "Buch S. 24", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Maturaniveau: Ein Anbieter wirbt für seine Trinkflasche mit »50 % weniger CO₂«. Du sollst für die Schule Flaschen beschaffen. "
       "Nenne mindestens drei Angaben, die du verlangst, bevor du dieser Werbung glaubst – und sag kurz, warum.",
  "hint": "Weniger als was? Für welche Leistung? Welche Abschnitte? Woher kommen die Daten? Info: Theorieteil »Ökobilanz: dieselbe Leistung fair vergleichen«",
  "type": "multi",
  "fields": [["ang", "Diese Angaben verlange ich (mindestens drei, mit kurzem Grund)"]],
  "chk": {"ang": {"kw": [["mindestens drei Angaben", r"vergleich|referenz|weniger als|als was|leistung|nutzung|lebensdauer|haltbar|hält|haelt|abschnitt|phase|grenze|systemgrenze|daten|quelle|alter|jahr|methode|wer |berechn|studie|prüf|pruef|reinig|transport|herstell|entsorg|andere umwelt|wasser|ressourc|kosten|preis|ersatz", 3]], "man": True}},
  "sol": [["Erwartung", ["Vergleichsprodukt (weniger als was?) und dieselbe Leistung, z. B. 1.000 Nutzungen · angenommene Lebensdauer · welche Abschnitte des Lebenszyklus gerechnet wurden (Systemgrenze) · "
                        "Herkunft und Alter der Daten, Bewertungsmethode · Annahmen zu Reinigung und Transport · andere Umweltwirkungen außer Klima · für die Beschaffung zusätzlich Kauf-, Pflege- und Ersatzkosten.",
                        "Eine Prozentzahl allein ist kein Freibrief."]]],
  "tip": [ABSCHNITT_2, "theorie.html#oekobilanz"]},

 {"id": "a8", "nr": 8, "title": "Quellencheck: Song Contest 2015", "src": "Buch S. 22", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Lies im Buch S. 22 den Zeitungsartikel über die Ökobilanz des Eurovision Song Contest 2015 in Wien. a) Was meint der Artikel mit »positiver Ökobilanz«? (1 Satz) "
       "b) Welcher Vergleich oder welche Angabe fehlt, damit man das wirklich beurteilen kann? (1 Satz)",
  "hint": "Denk an unsere Flaschen: Ohne gemeinsame Vergleichsleistung und Vergleichsfall ist »gut« oder »schlecht« kaum zu beurteilen.",
  "type": "multi",
  "fields": [["pos", "a) »Positive Ökobilanz« bedeutet dort (1 Satz)"], ["fehlt", "b) Das fehlt für ein echtes Urteil (1 Satz)"]],
  "chk": {"pos": {"kw": [["Maßnahmen / weniger Belastung", r"weniger|gespart|einspar|öffentlich|oeffentlich|öffi|oeffi|mehrweg|becher|müll|muell|abfall|recycl|strom|energie|green event|maßnahm|massnahm"]], "man": True},
          "fehlt": {"kw": [["Vergleichsfall / Bezugsgröße", r"vergleich|ohne|andere|frühere|fruehere|vorjahr|referenz|basis|pro (besucher|person|gast)|gleich|messung|daten|wie viel|klima|co2|co₂|gesamt|ganze"]], "man": True}},
  "sol": [["Erwartung", ["a) Der Artikel nennt Maßnahmen, die Belastungen gesenkt haben sollen (Anreise mit Öffis, Mehrwegbecher, getrennte Wertstoffe, geringer Stromverbrauch) – »positiv« ist dort ein Gesamturteil. Fachlich ist das keine Ökobilanz im Sinn der Methode: Eine Ökobilanz weist Belastungen je Wirkungskategorie aus, kein »positiv«.",
                        "b) Es fehlt ein Vergleichsfall (dieselbe Veranstaltung ohne diese Maßnahmen oder ein anderer Song Contest) und eine gemeinsame Bezugsgröße; außerdem wurden nur einzelne Größen genannt, keine vollständige Ökobilanz.",
                        "Der Text ist historisch (2015); seine Zahlen nicht als heutigen Maßstab verwenden."]]],
  "tip": [ABSCHNITT_2, "theorie.html#oekobilanz"]},

 {"id": "a9", "nr": 9, "title": "Plakat, Video oder Podcast: Ausrüstung mit Ökodesign", "src": "Buch S. 19–25", "own": True, "tag": "Zusatz", "h": 0, "zeit": 25,
  "q": "Kreativ und freiwillig, allein oder zu zweit: Wähle einen Ausrüstungsgegenstand für Sport oder Ausbildung (z. B. Feldflasche, Stirnlampe, Rucksack, Laufschuh). "
       "Mach ein A3-Plakat (mit der Hand), ein Erklärvideo (höchstens 2 Minuten) oder einen Podcast (höchstens 3 Minuten). Pflichtinhalte: 1. die Abschnitte seines Lebenszyklus, "
       "2. zwei Ökodesign-Verbesserungen mit Wirkung, 3. ein Zielkonflikt, 4. warum eine CO₂-Zahl allein für ein Umwelturteil nicht reicht. "
       "Abgabe (freiwillig, Termin sagt Stephan): Plakat als Foto ins PDF, Video oder Podcast als Datei in LMS (Teams nur, wenn die Datei zu groß ist). Trag hier Titel, Form und »hochgeladen am …« ein.",
  "hint": "Keine fremde Musik, keine fremden Bilder. Andere Personen nur mit Zustimmung aufnehmen. Wenn dir eine KI beim Skript hilft, schreib das dazu – und prüf den Inhalt.",
  "type": "multi",
  "fields": [["titel", "Titel"], ["form", "Form (Plakat, Video oder Podcast)"], ["inhalt", "Worum geht es? (1–2 Sätze)"], ["hoch", "hochgeladen in LMS am … / Plakat-Foto im PDF"]],
  "chk": {"titel": {"kw": [["Titel", r"[a-zäöüß]{3,}"]], "man": True}, "form": {"kw": [["Form", r"video|podcast|plakat|audio|film"]], "man": True},
          "inhalt": {"kw": [["Lebenszyklus / Ökodesign", r"lebenszyklus|ökodesign|oekodesign|reparat|ersatz|material|nutzung"]], "man": True}, "hoch": {"kw": [["Abgabe", r"\d|lms|teams|foto|hochgeladen"]], "man": True}},
  "sol": [["Bewertung", ["Raster (10 P.): fachlich richtig 4 · alle vier Pflichtinhalte 2 · verständlich und gut gegliedert 2 · kreativ/ansprechend 1 · Länge und Abgabe eingehalten 1.",
                         "Muss vorkommen: Rohstoffe – Herstellung – Transport – Nutzung und Pflege – Nutzungsende · zwei begründete Verbesserungen (z. B. Ersatzteile, trennbare Materialien) · ein Zielkonflikt · CO₂ ist nur die Klimawirkung, Wasser, Rohstoffe und Schadstoffe fehlen."]]],
  "tip": [ABSCHNITT_1, "theorie.html#oekodesign"]},
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
# Rechenkontrolle vom Aufgabentext aus (Aufgabe 2 und 6)
_c = {t["id"]: t["chk"] for t in T}
assert (_c["a2"]["nA"]["num"], _c["a2"]["nB"]["num"], _c["a2"]["kA"]["num"], _c["a2"]["kB"]["num"], _c["a2"]["eA"]["num"], _c["a2"]["eB"]["num"]) == \
       (R["A"]["fl"], R["B"]["fl"], _r(R["A"]["klima"]), _r(R["B"]["klima"]), R["A"]["kosten"], R["B"]["kosten"])
assert (_c["a6"]["n"]["num"], _c["a6"]["k"]["num"], _c["a6"]["e"]["num"]) == (R_B500["fl"], _r(R_B500["klima"]), R_B500["kosten"])

PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
BESPRECHEN = [1, 2]  # in der Stunde gemeinsam besprechen (TH-Unterricht, Lösungsmappe); Aufgabe 3 ist Diagnose, die PDF zeigt den Stand
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True

GRP = {1: TEILNAME[1] + " (Buch S. 19–21) · " + wann(),
       2: TEILNAME[2] + " (Buch S. 22–25) · in derselben Stunde",
       0: "Zusatz · Für Schnelle und zur Wiederholung vor dem Test am " + TEST + " · freiwillig, keine Hausübung"}

LERNZIELE = ["erklären, wie **Ökodesign** und **Ökobilanz** zusammenhängen",
             "einen Produktvergleich über den **Lebenszyklus** planen – mit **gleicher Leistung** und klaren **Grenzen**",
             "eine vereinfachte **Klimarechnung** auswerten und daraus eine **wirtschaftliche Entscheidung** begründen",
             "erklären, welche Umweltfragen eine reine **CO₂-Angabe** offenlässt"]

LEITFRAGE = "Welche Ausrüstung ist über ihre ganze Nutzung sinnvoll – und welche Angaben brauchen wir, um das zu entscheiden?"

WICHTIGSTE = ["**Ökodesign** heißt: Umweltwirkungen schon bei der **Entwicklung** mitdenken – über den ganzen **Lebenszyklus** von den Rohstoffen bis zum Nutzungsende.",
              "Langlebigkeit, Reparierbarkeit, Ersatzteile und trennbare Materialien sind typische Ökodesign-Ziele; **Zielkonflikte** (z. B. leicht gegen robust) gehören dazu.",
              "Eine **Ökobilanz** ermittelt und bewertet die möglichen Umweltwirkungen eines Produkts – in vier Schritten: **Ziel und Rahmen, Sachbilanz, Wirkungsabschätzung, Auswertung**.",
              "Fair vergleichen kann man nur **dieselbe Leistung** (funktionale Einheit, z. B. 1.000 Nutzungen) mit offengelegter **Systemgrenze** – nicht »ein Stück gegen ein Stück«.",
              "**kg CO₂-Äquivalente** zeigen nur die **Klimawirkung**; Wasser, Rohstoffe oder Schadstoffe sind eigene Fragen, und die **Kosten** prüft man getrennt."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Ökodesign", "umweltgerechte Produktgestaltung: Umweltwirkungen werden schon bei Entwicklung und Planung über den ganzen Lebenszyklus berücksichtigt"],
                ["Lebenszyklus", "Weg eines Produkts von der Rohstoffgewinnung über Herstellung, Transport und Nutzung bis zur Wiederverwendung, Verwertung oder Entsorgung"],
                ["Zielkonflikt", "die Verbesserung eines Ziels erschwert ein anderes, etwa geringes Gewicht gegenüber Robustheit"],
                ["Ökobilanz (Lebenszyklusanalyse)", "Verfahren, das die möglichen Umweltwirkungen eines Produkts oder einer Leistung über den festgelegten Lebenszyklus ermittelt und bewertet"],
                ["funktionale Einheit", "genau festgelegte Leistung als gemeinsame Vergleichsbasis, z. B. 1.000 Nutzungen einer Ein-Liter-Trinkflasche"],
                ["Systemgrenze", "Festlegung, welche Vorgänge in die Untersuchung einbezogen und welche ausgeschlossen werden"],
                ["Sachbilanz", "mengenmäßige Erfassung der Stoff- und Energieflüsse: was hineingeht (Input) und was herauskommt (Output)"],
                ["Wirkungsabschätzung (Wirkungsbilanz)", "Zuordnung der Stoff- und Energieflüsse zu Umweltwirkungen (Klassifizierung) und Berechnung ihres Beitrags (Charakterisierung)"],
                ["Wirkungskategorie", "Umweltproblem, für das gerechnet wird, z. B. Klimawirkung, Ressourcenverbrauch, Versauerung, Überdüngung"],
                ["CO₂-Äquivalent", "Einheit, mit der die Klimawirkung verschiedener Treibhausgase vergleichbar ausgedrückt wird (bezogen auf CO₂)"],
                ["Produkt-, Prozess-, Betriebsbilanz", "Ökobilanz für ein Produkt, für ein einzelnes Verfahren oder für alle Stoff- und Energieströme eines Betriebs bzw. Standorts"],
                ["Lebenszykluskosten", "Kosten über den ganzen Betrachtungszeitraum, etwa Kauf, Betrieb, Pflege, Ersatz und Entsorgung"],
                ["Greenwashing", "Darstellung, die eine Umweltleistung besser erscheinen lässt, als die Belege tragen"]]

WEISST_DU_NOCH = {}

STOPPFRAGEN = {
    1: [("Ein Hersteller druckt ein grünes Blatt auf seine Flasche und nennt sie »Öko-Design«. Ist das Ökodesign?", "Nein – Ökodesign verändert die Gestaltung (Material, Haltbarkeit, Reparatur, Trennbarkeit), nicht nur den Aufdruck. Ein grünes Logo allein ist eher Greenwashing."),
        ("Warum kann eine besonders leichte Flasche am Ende schlechter abschneiden?", "Wenn sie früh kaputtgeht, braucht man öfter eine neue – der Vorteil bei Material und Transport kann dadurch verloren gehen.")],
    2: [("Was ist der Unterschied zwischen Sachbilanz und Wirkungsabschätzung?", "Die Sachbilanz zählt Mengen (Material, Energie, Emissionen). Die Wirkungsabschätzung ordnet diese Mengen Umweltproblemen zu und rechnet ihren Beitrag aus."),
        ("Flasche B hat die geringere Klimawirkung. Ist sie damit in jeder Hinsicht umweltfreundlicher?", "Nein – CO₂-Äquivalente zeigen nur die Klimawirkung. Wasser, Rohstoffe oder Schadstoffe wurden nicht gerechnet.")],
}

PARTNERKARTEN = [("Was ist Ökodesign – in einem Satz?", "Umweltgerechte Produktgestaltung: Umweltwirkungen werden schon bei der Entwicklung über den ganzen Lebenszyklus mitgedacht."),
                 ("Nenne die Abschnitte im Lebenszyklus einer Trinkflasche.", "Rohstoffe → Herstellung → Transport und Verkauf → Nutzung und Pflege → Nutzungsende (wiederverwenden, verwerten, entsorgen)."),
                 ("Nenne zwei typische Ökodesign-Ziele.", "z. B. lange Nutzbarkeit, Reparierbarkeit, Ersatzteile, trennbare Materialien, wenig Energie, keine problematischen Stoffe."),
                 ("Was ist eine funktionale Einheit? Nenne unser Beispiel.", "Die gemeinsame Vergleichsleistung – bei uns 1.000 Nutzungen einer dichten, hygienischen Ein-Liter-Flasche."),
                 ("Nenne die vier Schritte einer Ökobilanz.", "Ziel und Untersuchungsrahmen – Sachbilanz – Wirkungsabschätzung – Auswertung."),
                 ("Was zeigen kg CO₂-Äquivalente – und was nicht?", "Nur die Klimawirkung, nicht Wasser, Rohstoffe, Versauerung oder giftige Stoffe."),
                 ("Produkt-, Prozess- oder Betriebsbilanz: Ein Werk erfasst ein Jahr lang alle Stoff- und Energieströme. Was ist das?", "eine Betriebs- bzw. Standortbilanz"),
                 ("Warum ist »recycelbar« allein kein Beweis für eine gute Umweltbilanz?", "Es sagt nur etwas über das Nutzungsende; Herstellung, Lebensdauer und Nutzung können viel wichtiger sein – und ob wirklich recycelt wird, ist offen.")]

STOLPERSTEINE = [("Nur den Kaufpreis vergleichen", "8 € wirkt billiger als 30 € – aber für 1.000 Nutzungen braucht man **5 Flaschen A**. Erst mit der Zahl der Ersatzflaschen und den Reinigungskosten wird der Vergleich fair (60 € gegen 50 €)."),
                 ("Ein Stück gegen ein Stück", "»3 kg gegen 6 kg« pro Flasche ist der falsche Vergleich. Ohne **funktionale Einheit** (1.000 Nutzungen) wird eine kurzlebige Flasche schöngerechnet."),
                 ("Bezugsgröße übersehen", "Die Reinigung gilt **pro Nutzung** – also 1.000 × 0,01 kg = 10 kg, nicht 0,01 kg. Eine zusätzliche Recycling-Gutschrift wäre doppelt gezählt."),
                 ("CO₂ = ganze Ökobilanz", "kg CO₂-Äquivalente zeigen nur die **Klimawirkung**. Ein Produkt kann beim Klima besser und beim Wasser oder bei Schadstoffen schlechter sein."),
                 ("»Recycelbar« oder »Metall ist besser«", "Materialbehauptungen und Werbewörter ersetzen keinen Vergleich. Im Modell ist das Material nicht festgelegt – und eine vorhandene, funktionierende Flasche wegzuwerfen, folgt aus dem Fall auch nicht.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Ökodesign", "Wann beginnt Ökodesign?", ["schon bei Entwicklung und Planung", "erst bei der Entsorgung", "nach dem Verkauf", "erst, wenn das Produkt kaputt ist"],
  "Frühe Entscheidungen legen Material, Haltbarkeit, Reparatur und Trennbarkeit fest – später lässt sich daran wenig ändern.", "Buch S. 20"),
 ("Ökodesign", "Was ist ein typischer Zielkonflikt beim Ökodesign?", ["dünnere Wand spart Material, hält aber Stöße schlechter aus", "weniger Material spart Rohstoffe und Gewicht", "Ersatzteile verlängern die Nutzung", "Recyclingmaterial senkt den Rohstoffbedarf"],
  "Ein Zielkonflikt heißt: Ein Ziel (weniger Material) erschwert ein anderes (Robustheit). Die anderen Antworten nennen nur Vorteile ohne Gegenspieler.", "Buch S. 20"),
 ("Funktionale Einheit", "Was ist die faire Vergleichsbasis für unsere Flaschen?", ["dieselbe Zahl geeigneter Ein-Liter-Nutzungen", "je eine gekaufte Flasche", "je ein Euro Kaufpreis", "je ein Kilogramm Flasche"],
  "Verglichen wird dieselbe Leistung – bei uns 1.000 Nutzungen. Sonst wird eine kurzlebige Flasche schöngerechnet.", "Buch S. 24"),
 ("Ökobilanz", "Was erfasst die Sachbilanz?", ["Stoff- und Energieflüsse, also Input und Output", "nur den Kaufpreis", "den Werbespruch", "nur das Design"],
  "Sie zählt Mengen: Material, Energie, Abfälle, Emissionen. Bewertet wird erst im nächsten Schritt.", "Buch S. 24"),
 ("Ökobilanz", "Was legt die Systemgrenze fest?", ["welche Vorgänge einbezogen oder ausgeschlossen werden", "wie groß die Flasche ist", "in welchem Land verkauft wird", "wie teuer die Flasche ist"],
  "Ohne offengelegte Grenzen kann niemand ein Ergebnis einordnen oder nachrechnen.", "Buch S. 24"),
 ("Wirkung", "Was messen kg CO₂-Äquivalente?", ["die Klimawirkung verschiedener Treibhausgase, auf CO₂ umgerechnet", "die gesamte Umweltbelastung", "den Wasserverbrauch", "nur den CO₂-Ausstoß beim Transport"],
  "Treibhausgase wie Methan werden auf CO₂ umgerechnet. Andere Umweltwirkungen sind damit nicht erfasst.", "Buch S. 24"),
 ("Wirkung", "16,5 statt 26 kg CO₂-Äquivalente – was darfst du daraus schließen?", ["B hat im Modell die geringere Klimawirkung.", "B ist bei allen Umweltwirkungen besser.", "B braucht sicher weniger Wasser.", "Metall ist immer besser als Kunststoff."],
  "Die Aussage gilt für den gerechneten Indikator und die angegebenen Annahmen – nicht für alles.", "Buch S. 24–25"),
 ("Bilanzarten", "Ein Werk erfasst ein Jahr lang alle Stoff- und Energieströme seines Standorts. Was ist das?", ["eine Betriebs- bzw. Standortbilanz", "eine Produktbilanz", "eine Prozessbilanz", "eine Wirkungsabschätzung"],
  "Die Betriebs- bzw. Standortbilanz betrachtet den ganzen Betrieb über einen Zeitraum, nicht ein einzelnes Produkt.", "Buch S. 23"),
 ("Bewerten", "Welche Angabe muss bei einem Vergleich offengelegt werden?", ["Systemgrenze und Nutzungsannahmen", "nur die Produktfarbe", "nur der Herstellername", "nur der Verkaufsort"],
  "Lebensdauer, Grenzen und Datenquellen bestimmen das Ergebnis mit – ohne sie ist eine Zahl kaum einzuordnen.", "Buch S. 24"),
 ("Greenwashing", "Welche Aussage ist ausreichend belegt?", ["»Für diese Leistung und Grenzen geringere Klimawirkung.«", "»Recycelbar, also automatisch die beste Umweltbilanz.«", "»Billiger, also nachhaltiger.«", "»Grünes Logo, also Ökodesign.«"],
  "Ein begrenztes, belegtes Urteil sagt mehr als ein pauschales Werbeversprechen.", "Buch S. 20, 24–25"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
