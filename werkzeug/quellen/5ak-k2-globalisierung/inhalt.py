"""IWK 5AK · K2 Globalisierung und aktuelle Weltpolitik (Trauner IWK, S. 41–77) – v2.
Grundlage: ChatGPT-Übergabe »26-27-5AK-K2-Global-Claude-v1« vom 29./30.10.2026 (Planung, Aufgaben 1–8 mit Erwartungshorizont, Karten A–E, Quellen Q1–Q21)
– von Claude nach dem Regelwerk umgesetzt und fachlich nachgeprüft (Prüfbericht). Jahresplan v14: E3 + E4 + E5 zu einer Einheit zusammengefasst
(Stephan, 30.10.2026): Fr 13.11., Fr 20.11. (zuerst 20 min angekündigter Test), Fr 27.11., Fr 04.12.2026; Annahme 50 min je Stunde.
Durchgehender Fall: Sportuhr mit KI-Dienst (didaktisches Modell, keine reale Lieferkette). Kein Versuch, kein Kahoot, keine Referate, keine Hausübung.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge).
Korrekturen gegenüber der Übergabe (Prüfbericht): Zollkarte A aktualisiert (US-Supreme-Court 20.02.2026), Lagarde-Meldung vom 29.10. nur sekundär belegt (Abgang 07.02.2027 laut Reuters) und
nicht verwendet, IEA-Zahlen auf die bestätigten Werte (415 TWh 2024, rund 945 TWh Projektion 2030) gestellt, 02.12.2026-Verbot nur aus einer Sekundärquelle, Primärquelle ungeprüft, weggelassen."""

STAND = "31.10.2026"
V = "v3"                       # v1 = ChatGPT-Übergabe
ORDNER = "5ak-iwk/k2-globalisierung"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ak-iwk/"
EYEBROW = "IWK · 5AK · K2 Globalisierung und Weltpolitik"
TITEL = "Globalisierung und aktuelle Weltpolitik – von der Sportuhr bis zur KI"
KURZTITEL = "Globalisierung und aktuelle Weltpolitik"
BUCH = "Buch S. 41–77"
KEY = "26-27-5AK-K2-Global-TH-Handy-v1"
CHECK_KEY = "26-27-5AK-K2-Global-Lernseite-Check-v1"
PRAEFIX = "26-27-5AK-K2-Global"
KAP = "K2"
TEST = "Fr 20.11.2026"

VIDEOS = {}                      # keine Pflichtvideos, keine Podcasts im Pflichtablauf (Übergabe 11)


def zeigen(key, lehrer=False):
    return False


KLASSEN = ["5AK"]
_D = {1: "Fr 13.11.", 2: "Fr 20.11.", 3: "Fr 27.11.", 4: "Fr 04.12."}
DATEN = {k: dict(_D) for k in KLASSEN}
TEIL_STUNDE = {t: {k: t for k in KLASSEN} for t in (1, 2, 3, 4)}
TEILNAME = {1: "Stunde 1 · Warum steckt in einer Sportuhr die ganze Welt?",
            2: "Stunde 2 · Wer bezahlt den US-Zoll?",
            3: "Stunde 3 · KI: Fortschritt, Macht und Risiko",
            4: "Stunde 4 · Welche Globalisierung wollen wir gestalten?"}
TEILKURZ = {1: "Sportuhr und Verflechtung", 2: "Zölle und Institutionen", 3: "KI und Globalisierung", 4: "Gestalten und urteilen"}
TEILBUCH = {1: "Buch S. 43–48 · 64–70", 2: "Buch S. 50–63", 3: "Buch S. 48 · Ergänzung KI", 4: "Buch S. 65–77"}


def wann(teil=None):
    if teil: return _D[teil]
    return " · ".join(_D[t] for t in (1, 2, 3, 4))


# ======================================================================= Aufgaben
# Politische Urteile und offene Erklärungen: »man« (Lehrkraft bewertet), Stichwörter nur als Schreibhilfe. Automatisch geprüft: Aufgabe 3 a/b (Zahl), 3 c (Wer zahlt zuerst?), 5 (Zuordnung), 4 (Zuordnung).
_KW_STROM = r"bauteil|chip|halbleiter|rohstoff|montage|lieferung|uhr|ware|geld|zahl|euro|dollar|bezahl|kauf|daten|trainingsdaten|server|rechenzentrum|wissen|entwicklung|vorgabe|konstruktion|design|software|know|von |nach |→|->"
T = [
 # ======================================================= Stunde 1
 {"id": "a1", "nr": 1, "title": "Die Sportuhr ist weltweit vernetzt", "src": "Buch S. 43–48", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 14,
  "q": "Modell »Sportuhr« (siehe Fallblatt im Theorieteil, Abschnitt »Was Globalisierung verbindet«; die Orte sind angenommen, keine reale Marke). Zeichne auf Papier ein Flussbild "
       "mit mindestens vier Stationen und fotografiere es. Trage dann hier ein: a) je einen Warenstrom, Geldstrom, Datenstrom und Wissensstrom (»von … nach … : was fließt«), "
       "b) zwei Akteure und ihren Beitrag zum Produkt, c) einen Engpass und eine Station, die davon betroffen wäre (2 Sätze).",
  "hint": "Beschriftete Pfeile zählen mehr als schönes Zeichnen. Info: Theorieteil »Was Globalisierung verbindet«",
  "type": "sketch",
  "fields": [["ware", "a) Warenstrom (von … nach … : was)"], ["geld", "a) Geldstrom (von … nach … : was)"], ["daten", "a) Datenstrom (von … nach … : was)"], ["wissen", "a) Wissensstrom (von … nach … : was)"],
             ["akteure", "b) Zwei Akteure und ihr Beitrag"], ["engpass", "c) Engpass und betroffene Station (2 Sätze)"]],
  "chk": {"ware": {"kw": [["Bauteil, Rohstoff oder Uhr", r"bauteil|chip|halbleiter|rohstoff|montage|lieferung|uhr|ware|teil|produkt|akku|metall"]], "man": True},
          "geld": {"kw": [["Zahlung", r"geld|zahl|euro|dollar|bezahl|kauf|preis|lohn|gewinn|rechnung|überweis|ueberweis|invest"]], "man": True},
          "daten": {"kw": [["Daten", r"daten|training|server|rechenzentrum|cloud|auswert|puls|gps|messwert|app|ki"]], "man": True},
          "wissen": {"kw": [["Entwicklung oder Know-how", r"wissen|entwicklung|vorgabe|konstruktion|design|software|know|forschung|plan|ausbildung|patent|technik"]], "man": True},
          "akteure": {"kw": [["zwei Akteure", r"unternehmen|anbieter|hersteller|zulieferer|montage|firma|konzern|händler|haendler|kunde|käufer|kaeufer|rechenzentrum|beschäftigte|beschaeftigte|staat|zoll", 2]], "man": True},
          "engpass": {"kw": [["Engpass und Folge", r"chip|engpass|fehl|ausfall|verzöger|verzoeger|lieferung|montage|stopp|knapp|rohstoff|server|rechenzentrum|absatz|auslief"]], "man": True}},
  "sol": [["Musterlösung", ["Warenstrom: Halbleiter von Ostasien nach Südostasien (Montage); fertige Uhren von der Montage nach Europa und in die USA. Geldstrom: Käufer in Europa/USA → Anbieter → Zulieferer und Montagebetrieb; Zahlung ans Rechenzentrum für den KI-Dienst.",
                            "Datenstrom: Trainingsdaten der Uhr → Rechenzentrum → Auswertung zurück an die App. Wissensstrom: Entwicklungsvorgaben und Software aus Europa → Hersteller; Know-how der Montagebetriebe → zurück.",
                            "Akteure z. B.: Anbieter (Entwicklung, Marke, Vertrieb) · Montagebetrieb (Fertigung) · Chiphersteller · Rechenzentrumsanbieter. Wert entsteht auch durch Entwicklung, Software und Vertrieb – nicht nur durch Montage.",
                            "Engpass z. B.: Fehlt der Chip, verzögert sich die Montage und damit die Auslieferung nach Europa und in die USA. Beschriftete Verknüpfungen sind wichtiger als künstlerische Gestaltung."]]],
  "fsol": {"ware": "z. B. Chips Ostasien → Montage Südostasien", "geld": "z. B. Käufer → Anbieter → Zulieferer", "daten": "z. B. Trainingsdaten → Rechenzentrum", "wissen": "z. B. Entwicklungsvorgaben → Hersteller",
           "akteure": "z. B. Anbieter (Entwicklung, Vertrieb) · Montagebetrieb (Fertigung)", "engpass": "z. B. Chip fehlt → Montage steht → keine Auslieferung"},
  "tip": ["Was Globalisierung verbindet", "theorie.html#verbindet"], "besprechen": True},

 {"id": "a2", "nr": 2, "title": "Folgen sind ungleich verteilt", "src": "Buch S. 64–70", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 10,
  "q": "Füll je eine Zeile für Wirtschaft, Gesellschaft und Umwelt aus: ein möglicher Vorteil, eine mögliche Belastung und die betroffene Gruppe (jeweils kurz). "
       "Ergänze dann eine Bedingung, unter der sich eine dieser Folgen verändert. Schreib zuerst in dein Heft, dann hierher.",
  "hint": "Es gibt kein »alle gewinnen« und kein »alle verlieren«. Info: Theorieteil »Wer gewinnt – und wer trägt die Kosten?«",
  "type": "multi",
  "fields": [["wirtschaft", "Wirtschaft: Vorteil · Belastung · betroffene Gruppe"], ["gesellschaft", "Gesellschaft: Vorteil · Belastung · betroffene Gruppe"],
             ["umwelt", "Umwelt: Vorteil · Belastung · betroffene Gruppe"], ["bedingung", "Eine Bedingung, unter der sich eine Folge ändert"]],
  "chk": {"wirtschaft": {"kw": [["Vorteil und Belastung", r"markt|absatz|export|arbeitsplat|einkommen|wettbewerb|preis|druck|zulieferer|betrieb|lieferdruck|kosten|billig|unternehm"]], "man": True},
          "gesellschaft": {"kw": [["Vorteil und Belastung", r"einkommen|wissen|bildung|arbeit|lohn|bedingung|ungleich|zugang|migration|abwander|digital|familie|beschäftigte|beschaeftigte|region"]], "man": True},
          "umwelt": {"kw": [["Vorteil und Belastung", r"emission|abfall|rohstoff|energie|effizien|technik|sauber|umwelt|verbrauch|klima|müll|muell|recycl|transport"]], "man": True},
          "bedingung": {"kw": [["Bedingung", r"wenn|falls|kontroll|standard|prüf|pruef|reparier|langlebig|gesetz|regel|mindest|lieferketten|zertifi|überprüf|ueberpruef"]], "man": True}},
  "sol": [["Musterlösung", ["Wirtschaft: Zugang zu größeren Märkten (Vorteil); Wettbewerbs- oder Lieferdruck für bestimmte Betriebe, z. B. Zulieferer mit knappen Margen (Belastung).",
                            "Gesellschaft: Einkommen und Wissenstransfer in der Montageregion (Vorteil); problematische Arbeitsbedingungen oder ungleicher Zugang (Belastung). Bei Abwanderung: Gewinn für die einzelne Person, mögliche Engpässe im Herkunftsland.",
                            "Umwelt: effizientere Produktion, Verbreitung sauberer Technik (Vorteil); Rohstoffbedarf, Emissionen und Elektroschrott (Belastung). Die Umweltwirkung nicht nur aus Transportkilometern ableiten.",
                            "Bedingung z. B.: überprüfbarer Arbeitsstandard oder eine langlebige, reparierbare Uhr – dann verändert sich die Belastung."]]],
  "fsol": {"wirtschaft": "Markt größer · Druck auf Zulieferer", "gesellschaft": "Einkommen, Wissen · schlechte Arbeitsbedingungen", "umwelt": "effizientere Technik · Rohstoffe, Abfall",
           "bedingung": "z. B. überprüfbare Sozialstandards, reparierbare Uhr"},
  "tip": ["Wer gewinnt – und wer trägt die Kosten?", "theorie.html#folgen"], "besprechen": True},

 # ======================================================= Stunde 2
 {"id": "a3", "nr": 3, "title": "Ein Zoll und seine Folgen", "src": "Buch S. 50–51 · Karte A", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 8,
  "q": "Rechenmodell, kein echter Zollbescheid: Ein US-Importeur führt eine Uhr mit einem unveränderten Zollwert von 100 US-Dollar ein. Für das Beispiel gilt ein Zollsatz von 15 Prozent; weitere Kosten bleiben unberücksichtigt. "
       "a) Berechne den Zoll (nur die Zahl, in US-Dollar). b) Berechne Zollwert plus Zoll. c) Wer führt den Zoll zuerst ab? d) Erkläre zwei Wege, wie sich die wirtschaftliche Belastung verteilen kann. "
       "e) Warum lässt sich daraus der Ladenpreis nicht bestimmen? (1 Satz)",
  "hint": "Rechenweg ins Heft. Info: Theorieteil »Zölle: Wer zahlt – und wer trägt die Last?«",
  "type": "multi",
  "fields": [["zoll", "a) Zoll in US-Dollar"], ["summe", "b) Zollwert plus Zoll in US-Dollar"], ["wer", "c) Wer führt den Zoll zuerst ab?"], ["wege", "d) Zwei Wege der Belastung"], ["laden", "e) Warum ist der Ladenpreis offen? (1 Satz)"]],
  "chk": {"zoll": {"num": 15, "ende": True}, "summe": {"num": 115, "ende": True},
          "wer": {"kw": [["Importeur (zahlt an die US-Zollbehörde)", r"importeur|einführer|einfuehrer|importfirma|importierende|einfuhr"]], "man": True},
          "wege": {"kw": [["zwei Wege", r"marge|gewinn|preis|anheb|aufschlag|nachlass|rabatt|lieferant|hersteller|verbraucher|käufer|kaeufer|kunde|weitergeb|teilen", 2]], "man": True},
          "laden": {"kw": [["Gründe", r"nachfrage|vertrag|wechselkurs|kosten|wettbewerb|marge|weitere|annahme|konkurrenz|nicht bekannt|offen|abhängig|abhaengig"]], "man": True}},
  "sol": [["Musterlösung", ["a) 100 × 0,15 = 15 US-Dollar", "b) 100 + 15 = 115 US-Dollar",
                            "c) Zuerst führt der Importeur den Zoll an die zuständige US-Zollbehörde ab.",
                            "d) Z. B.: Der Importeur senkt seine Marge. Oder er erhöht den Preis für Kunden. Auch ein Lieferant kann einen Preisnachlass geben.",
                            "e) Nachfrage, Verträge, Wechselkurs, weitere Kosten und Wettbewerb beeinflussen den Endpreis. »Das Ausland zahlt alles automatisch« und »der Verbraucher zahlt immer genau 15 % mehr« sind beide zu einfach. Die Rechnung setzt einen unveränderten Zollwert voraus."]]],
  "fsol": {"zoll": "15", "summe": "115", "wer": "der Importeur (an die US-Zollbehörde)", "wege": "Marge sinkt · Preis steigt (oder Lieferant gibt Nachlass)", "laden": "Nachfrage, Verträge, Wechselkurs, weitere Kosten, Wettbewerb"},
  "tip": ["Zölle: Wer zahlt – und wer trägt die Last?", "theorie.html#zoelle"], "besprechen": True},

 {"id": "a4", "nr": 4, "title": "Drei Probleme, drei Institutionen", "src": "Buch S. 52–63 · Karte B", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 9,
  "q": "In Dreiergruppen: Trag für WTO, IWF und Weltbank je eine Hauptaufgabe, ein Instrument und eine Grenze ein (Stichwörter). Ordne danach die drei Fälle zu: "
       "Fall 1: Zwei Staaten streiten über eine Handelsbeschränkung. Fall 2: Ein Staat kann seine Zahlungen ans Ausland kurzfristig nicht finanzieren. Fall 3: Ein langfristiges Vorhaben soll Stromversorgung oder Schulen verbessern.",
  "hint": "Auch in der Realität können mehrere Akteure beteiligt sein – hier zählt die Hauptzuständigkeit. Info: Theorieteil »Wer organisiert Regeln und Finanzierung?«",
  "type": "multi",
  "fields": [["wto", "WTO: Hauptaufgabe · Instrument · Grenze"], ["iwf", "IWF: Hauptaufgabe · Instrument · Grenze"], ["wb", "Weltbank: Hauptaufgabe · Instrument · Grenze"],
             ["f1", "Fall 1 (Handelsstreit) gehört vor allem zu …", ["WTO", "IWF", "Weltbank"], False], ["f2", "Fall 2 (Zahlungsproblem) gehört vor allem zu …", ["WTO", "IWF", "Weltbank"], False],
             ["f3", "Fall 3 (langfristiges Vorhaben) gehört vor allem zu …", ["WTO", "IWF", "Weltbank"], False]],
  "chk": {"f1": {"sel": "WTO"}, "f2": {"sel": "IWF"}, "f3": {"sel": "Weltbank"},
          "wto": {"kw": [["Handelsregeln oder Streit", r"handel|regel|streit|verhandl|zoll|schlicht|gatt|dienstleist|schutz"], ["Grenze", r"konsens|keine weltregierung|blockier|berufung|durchsetz|langsam|einstimm|nicht erzwing|kein zwang|macht"]], "man": True},
          "iwf": {"kw": [["Stabilität oder Zahlungsbilanz", r"stabil|währung|waehrung|zahlungsbilanz|kredit|überwach|ueberwach|beratung|finanz|krise|lücke|luecke"], ["Grenze", r"bedingung|auflage|sozial|spar|stimmrecht|nicht alle|kritik|macht|quote"]], "man": True},
          "wb": {"kw": [["Entwicklungsfinanzierung", r"entwicklung|kredit|projekt|infrastruktur|zuschuss|beratung|armut|langfristig|ida|ibrd|schule|strom|vergünstigt"], ["Grenze", r"schulden|folgen|ökolog|oekolog|sozial|auswahl|stimmrecht|kritik|prüf|pruef|abhängig|abhaengig"]], "man": True}},
  "sol": [["Musterlösung", ["WTO: Hauptaufgabe Handelsregeln, Verhandlungen und Streitbeilegung · Instrument: Streitverfahren (Panels) · Grenze: keine Weltregierung, Entscheidungen im Konsens, Berufungsinstanz derzeit blockiert.",
                            "IWF: Hauptaufgabe Stabilität, Überwachung und Beratung, Finanzierung bei Zahlungsbilanzproblemen · Instrument: Kredite mit Auflagen · Grenze: Mittel und Bedingungen lösen nicht automatisch alle sozialen Probleme; Stimmrechte nach Kapitalanteil.",
                            "Weltbank: Hauptaufgabe Entwicklungsfinanzierung und Beratung · Instrument: vergünstigte Kredite (je nach Instrument auch Zuschüsse) für Projekte · Grenze: Projektauswahl, Schulden sowie soziale und ökologische Folgen müssen geprüft werden.",
                            "Fall 1 → WTO · Fall 2 → IWF · Fall 3 → vor allem Weltbank. Die OECD liefert Daten, Analysen und Standards – sie ersetzt weder WTO noch IWF."]]],
  "fsol": {"wto": "Handelsregeln, Streitverfahren · keine Weltregierung", "iwf": "Stabilität, Kredit bei Zahlungsproblemen · Auflagen", "wb": "Entwicklungsprojekte, vergünstigte Kredite · Schulden prüfen",
           "f1": "WTO", "f2": "IWF", "f3": "Weltbank"},
  "tip": ["Wer organisiert Regeln und Finanzierung?", "theorie.html#institutionen"], "besprechen": True},

 # ======================================================= Stunde 3
 {"id": "a5", "nr": 5, "title": "KI: Welche Art von Regel?", "src": "Buch S. 48 · Karten A und C", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 10,
  "q": "Ordne die vier vereinfachten Fälle zu. Die Karten im Theorieteil (Abschnitt »KI braucht Daten, Chips, Strom und Regeln«) nennen die Voraussetzungen; es geht um die Grundidee, nicht um ein Gerichtsurteil. "
       "Fall 1: Ein Unternehmen nutzt KI, die Bewerbungen vorsortiert. Fall 2: Ein Kundendienst setzt einen Chatbot ein, der wie ein Mensch auftritt, ohne es zu sagen. "
       "Fall 3: Ein System bewertet Menschen über längere Zeit nach sachfremdem Sozialverhalten und benachteiligt sie dadurch in einem anderen Lebensbereich. "
       "Fall 4: Jemand lässt einen privaten Trainingsplan sprachlich überarbeiten. Dann: Welches Ziel betont die EU-Regelung, welches der US-KI-Aktionsplan?",
  "hint": "Verbot, Hochrisiko und Transparenzpflicht sind verschiedene Kategorien. Info: Theorieteil »KI braucht Daten, Chips, Strom und Regeln«",
  "type": "multi",
  "fields": [["k1", "Fall 1 (Bewerbungen vorsortieren)", ["mögliche verbotene Praxis", "möglicher Hochrisiko-Einsatz", "Transparenzpflicht", "keine besondere Einstufung aus diesen Angaben"], False],
             ["k2", "Fall 2 (Chatbot im Kundendienst)", ["mögliche verbotene Praxis", "möglicher Hochrisiko-Einsatz", "Transparenzpflicht", "keine besondere Einstufung aus diesen Angaben"], False],
             ["k3", "Fall 3 (soziale Bewertung)", ["mögliche verbotene Praxis", "möglicher Hochrisiko-Einsatz", "Transparenzpflicht", "keine besondere Einstufung aus diesen Angaben"], False],
             ["k4", "Fall 4 (privater Trainingsplan)", ["mögliche verbotene Praxis", "möglicher Hochrisiko-Einsatz", "Transparenzpflicht", "keine besondere Einstufung aus diesen Angaben"], False],
             ["ziele", "EU: betontes Ziel · USA (KI-Aktionsplan): betontes Ziel"]],
  "chk": {"k1": {"sel": "möglicher Hochrisiko-Einsatz"}, "k2": {"sel": "Transparenzpflicht"}, "k3": {"sel": "mögliche verbotene Praxis"}, "k4": {"sel": "keine besondere Einstufung aus diesen Angaben"},
          "ziele": {"kw": [["EU-Ziel", r"grundrecht|sicherheit|vertrauen|risiko|schutz|regel|innovation"], ["US-Ziel", r"innovation|infrastruktur|führung|fuehrung|wirtschaft|sicherheitspolit|tempo|rechenzentr|partner|diplomatie|export"]], "man": True}},
  "sol": [["Musterlösung", ["Fall 1: möglicher Hochrisiko-Einsatz (Bewerberauswahl) – die genauen Voraussetzungen sind zu beachten.",
                            "Fall 2: Transparenzpflicht – man muss erkennen können, dass man mit einer KI spricht.",
                            "Fall 3: mögliche verbotene Praxis (soziale Bewertung) unter den gesetzlichen Bedingungen.",
                            "Fall 4: aus diesen Angaben keine besondere Einstufung; Datenschutz und andere Regeln können trotzdem eine Rolle spielen.",
                            "EU: u. a. Grundrechte, Sicherheit und Vertrauen, außerdem Innovation. USA (Aktionsplan Juli 2025): u. a. Innovation, Infrastruktur, wirtschaftliche und sicherheitspolitische Führung. Beide verfolgen mehrere Ziele – »EU verbietet Innovation, USA haben keinerlei Regeln« ist zu einfach."]]],
  "fsol": {"k1": "möglicher Hochrisiko-Einsatz", "k2": "Transparenzpflicht", "k3": "mögliche verbotene Praxis", "k4": "keine besondere Einstufung aus diesen Angaben", "ziele": "EU: Grundrechte, Sicherheit, Vertrauen · USA: Innovation, Infrastruktur, Führung"},
  "tip": ["KI braucht Daten, Chips, Strom und Regeln", "theorie.html#ki_global"], "besprechen": True},

 {"id": "a6", "nr": 6, "title": "KI-Warnung: Befund, Szenario oder Werbung?", "src": "Buch S. 48 · Quellenkarten 1–4", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 14,
  "q": "Arbeitsteilig: Wähle deine Quellenkarte (1, 2, 3 oder 4 im Theorieteil, Abschnitt »KI-Risiken prüfen«) und trag ein: Aussage – Beleg – mögliche Interessen – Grenze (je ein kurzer Satz). "
       "Nach dem Bericht deiner Gruppe (höchstens 45 Sekunden je Karte) schreib einen Satz: Welche Karte liefert eine Messung, welche eine Position?",
  "hint": "Ein Interesse ist kein Beweis für eine Täuschung – und eine Warnung kann trotzdem begründet sein. Info: Theorieteil »KI-Risiken prüfen«",
  "type": "multi",
  "fields": [["karte", "Meine Karte", ["1", "2", "3", "4"], False], ["aussage", "Aussage der Quelle"], ["beleg", "Beleg (Art der Quelle, Datum)"], ["interesse", "Mögliche Interessen"], ["grenze", "Grenze der Aussage"],
             ["vergleich", "Messung oder Position? (1 Satz)"]],
  "chk": {"aussage": {"kw": [["Aussage", r"warn|fordert|bericht|unterscheid|fehlfunktion|kontrollverlust|simulation|szenario|ziel|aktionsplan|innovation|risiko|test|befund"]], "man": True},
          "beleg": {"kw": [["Art und Datum", r"statement|bericht|studie|simulation|test|plan|regierung|2023|2025|2026|forscher|unterzeichn|fallstudie|bengio|aktionsplan"]], "man": True},
          "interesse": {"kw": [["Interessen", r"interesse|unternehmen|firma|wirtschaft|regierung|politik|werbung|pr\b|ruf|image|geld|investor|wettbewerb|forschung|markt|aufmerksamkeit|keine"]], "man": True},
          "grenze": {"kw": [["Grenze", r"nicht|kein|nur|simulation|künstlich|kuenstlich|unsicher|zukunft|wahrscheinlich|messung|beweis|gestellt|test|ziel|alltag|übertrag|uebertrag"]], "man": True},
          "vergleich": {"kw": [["Messung/Position", r"messung|messen|position|forderung|warn|bericht|simulation|versuch|ziel|plan|statement|befund"]], "man": True}},
  "sol": [["Musterlösung", ["Quellenkarte 1 (CAIS-Statement 30.05.2023): fordert, das Aussterberisiko durch KI als globale Priorität zu behandeln – eine Position, kein Experiment und keine gemessene Wahrscheinlichkeit. Unterzeichner sind Forscher und Leiter von KI-Unternehmen (Fachwissen und wirtschaftliche Interessen zugleich).",
                            "Quellenkarte 2 (International AI Safety Report, Feb. 2026): bündelt Forschungsstand; unterscheidet Fehlfunktionen (gibt es) und umfassenden Kontrollverlust (heute nicht erreicht); Zeitpunkt und Wahrscheinlichkeit bleiben unsicher, Fachleute bewerten sie unterschiedlich.",
                            "Quellenkarte 3 (Forschungsfallstudien Sommer 2026): problematisches Verhalten autonomer Modelle in gestellten Szenarien – kein Bericht über reale Machtübernahme und keine Häufigkeit im Alltag. Der Text stammt von einem KI-Unternehmen (Interessenkonflikt offen benennen), ist aber als Studie prüfbar.",
                            "Quellenkarte 4 (US-KI-Aktionsplan 23.07.2025): nennt erklärte Ziele und Interessen der US-Regierung (Innovation, Infrastruktur, internationale Führung) – Primärbeleg für Politikziele, kein neutraler Wirkungsnachweis.",
                            "Satz: Eine Messung liefert höchstens ein Versuch mit klaren Bedingungen (Quellenkarte 3, in Grenzen); Statement und Aktionsplan sind Positionen, der Bericht bündelt Befunde. Eine mögliche PR-Wirkung beweist weder Täuschung noch, dass die Warnung falsch ist."]]],
  "fsol": {"karte": "A, B, C oder D", "aussage": "was die Quelle sagt", "beleg": "Art der Quelle + Datum", "interesse": "wer hat welches Interesse", "grenze": "was der Befund nicht zeigt", "vergleich": "Position (A, D) vs. Befund/Versuch (B, C)"},
  "tip": ["KI-Risiken prüfen", "theorie.html#ki_risiko"], "besprechen": True},

 {"id": "a7", "nr": 7, "title": "Korrigiere einen fehlerhaften KI-Text", "src": "Buch S. 48 · Karten C–E", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 8,
  "q": "Der Text ist für den Unterricht gebaut und enthält Fehler – er stammt nicht von einem echten KI-Anbieter: »Laut ILO wird KI jeden vierten Arbeitsplatz abschaffen. Das ist ein Beweis, dass die Machtübernahme bereits läuft. "
       "In der EU ist KI seit 2026 vollständig verboten. Die Studie aus einer Simulation zeigt außerdem, wie oft KI im Alltag Menschen täuscht.« "
       "Schreib zu jedem Satz in Stichwörtern, warum er nicht stimmt. Formuliere dann zwei davon richtig und nenn die Quelle. Nenne zum Schluss eine Schutzmaßnahme für einen Betrieb und ihre Grenze.",
  "hint": "Betroffene Tätigkeiten sind keine verlorenen Arbeitsplätze. Info: Theorieteil »KI braucht Daten, Chips, Strom und Regeln«",
  "type": "multi",
  "fields": [["s1", "Satz 1 (ILO) – warum falsch?"], ["s2", "Satz 2 (Machtübernahme) – warum falsch?"], ["s3", "Satz 3 (EU-Verbot) – warum falsch?"], ["s4", "Satz 4 (Simulation) – warum falsch?"],
             ["richtig", "Zwei Sätze richtig formuliert, mit Quelle"], ["schutz", "Schutzmaßnahme und ihre Grenze"]],
  "chk": {"s1": {"kw": [["Tätigkeiten ≠ Arbeitsplätze", r"tätigkeit|taetigkeit|betroffen|einfluss|einwirk|beruf|nicht abgeschafft|kein ersatz|verändert|veraendert|exposure|mögliche|moegliche|messen"]], "man": True},
          "s2": {"kw": [["Arbeit ≠ Macht", r"arbeit|macht|herrschaft|übernahme|uebernahme|kein beweis|nicht gleich|politisch|automatis|kontrolle|nicht dasselbe|verwechsel"]], "man": True},
          "s3": {"kw": [["risikobasiert", r"risiko|nicht verboten|kein verbot|teilweise|bestimmte|einzelne|pflicht|anwendung|regel|transparenz|hochrisiko|nur manche"]], "man": True},
          "s4": {"kw": [["Simulation ≠ Alltag", r"simulation|versuch|künstlich|kuenstlich|bedingung|alltag|häufigkeit|haeufigkeit|quote|nicht übertrag|nicht uebertrag|gestellt|test"]], "man": True},
          "richtig": {"kw": [["Quelle", r"ilo|iea|eu|verordnung|ki-verordnung|bericht|studie|safety|quelle|2025|2026"]], "man": True},
          "schutz": {"kw": [["Maßnahme", r"zugriff|freigabe|mensch|protokoll|prüf|pruef|kontrolle|unabhängig|unabhaengig|rechte|begrenz|schulung|test"], ["Grenze", r"grenze|nicht|kein|nie|garantie|fehler|schwäche|schwaeche|umgeh|aufwand|kosten|restrisiko"]], "man": True}},
  "sol": [["Musterlösung", ["Satz 1: Die ILO misst mögliche Betroffenheit von Tätigkeiten (rund jeder vierte Beschäftigte in einem Beruf mit gewissem Einfluss generativer KI), nicht abgeschaffte Arbeitsplätze; Veränderung von Berufen ist wahrscheinlicher als Ersatz.",
                            "Satz 2: Eine Aufgabe zu automatisieren ist nicht dasselbe, wie politische Herrschaft auszuüben; Arbeit, Macht, Abhängigkeit und Kontrollverlust sind vier verschiedene Fragen.",
                            "Satz 3: Die EU-KI-Verordnung ist risikobasiert (Verbote, Hochrisiko, Transparenz) – kein vollständiges KI-Verbot.",
                            "Satz 4: Ein Versuch unter künstlichen Bedingungen zeigt mögliche Schwachstellen, aber nicht, wie oft etwas im Alltag passiert.",
                            "Schutzmaßnahmen z. B.: begrenzte Zugriffsrechte, menschliche Freigabe bei folgenreichen Entscheidungen, Protokollierung, unabhängige Prüfung. Keine ist eine absolute Sicherheitsgarantie."]]],
  "fsol": {"s1": "Tätigkeiten betroffen ≠ Arbeitsplätze abgeschafft", "s2": "Arbeit verändern ≠ Machtübernahme", "s3": "risikobasiert, kein Totalverbot", "s4": "Simulation sagt nichts über Alltagshäufigkeit",
           "richtig": "z. B. S1 + S3 mit Quelle (ILO 2025, EU-KI-VO)", "schutz": "z. B. menschliche Freigabe – Grenze: keine Garantie"},
  "tip": ["KI braucht Daten, Chips, Strom und Regeln", "theorie.html#ki_global"], "besprechen": True},

 # ======================================================= Stunde 4
 {"id": "a8", "nr": 8, "title": "Gestalten statt nur bewerten", "src": "Buch S. 65–77 · Debattenblatt", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 30,
  "q": "Frage: »Soll der Anbieter unserer Sportuhr für wichtige Bauteile und KI-Dienste mehrere Bezugsquellen aufbauen, auch wenn das die Kosten erhöht?« "
       "8a (7 min): Wähle deine Perspektive und trag zwei begründete Argumente, eine konkrete Maßnahme und einen Nachteil deiner eigenen Lösung ein. "
       "8b (13 min, ohne Handy): Diskussion – trag danach einen belastbaren Zusammenhang und eine offene Behauptung ein, die du beobachtet hast. "
       "8c (10 min, ohne Handy): Schreib auf Papier dein Urteil mit 100–130 Wörtern und fotografiere es. Es braucht: einen Zusammenhang aus der Lieferkette, eine soziale oder ökologische Folge, "
       "eine Grenze deiner Maßnahme und einen Satz »Wenn …, dann könnte …; offen bleibt …«.",
  "hint": "Beide Richtungen sind erlaubt. Bewertet wird Begründung, Gegenargument und gekennzeichnete Unsicherheit – nicht deine politische Richtung. Info: Theorieteil »Kosten verteilen und Abhängigkeiten verringern«",
  "type": "sketch",
  "fields": [["persp", "8a: Meine Perspektive", ["Unternehmensleitung", "Beschäftigte und Zulieferregion", "Nutzer und öffentliche Beschaffung", "Umwelt- und Verbraucherschutz"], False],
             ["arg1", "8a: Argument 1"], ["arg2", "8a: Argument 2"], ["massnahme", "8a: Eine konkrete Maßnahme"], ["nachteil", "8a: Ein Nachteil meiner Lösung"],
             ["zusammenhang", "8b: Ein belastbarer Zusammenhang aus der Diskussion"], ["offen", "8b: Eine offene Behauptung (noch nicht belegt)"]],
  "chk": {"arg1": {"kw": [["Argument", r"weil|da |denn|abhängig|abhaengig|kosten|risiko|liefer|ausfall|preis|arbeit|umwelt|daten|wechsel|qualität|qualitaet|sicher"]], "man": True},
          "arg2": {"kw": [["Argument", r"weil|da |denn|abhängig|abhaengig|kosten|risiko|liefer|ausfall|preis|arbeit|umwelt|daten|wechsel|qualität|qualitaet|sicher"]], "man": True},
          "massnahme": {"kw": [["Maßnahme", r"quelle|lieferant|lager|bestand|standard|vertrag|prüf|pruef|reparier|wechsel|zertifi|kontrolle|partner|mehrere|zweit|investier|regel"]], "man": True},
          "nachteil": {"kw": [["Nachteil", r"kosten|teuer|aufwand|zeit|umstellung|prüf|pruef|vertrag|komplex|preis|mehr|schwierig|nachteil"]], "man": True},
          "zusammenhang": {"kw": [["Zusammenhang", r"weil|dadurch|deshalb|führt|fuehrt|wenn|folge|abhängig|abhaengig|kosten|liefer"]], "man": True},
          "offen": {"kw": [["offene Behauptung", r"nicht|offen|unklar|belegt|behaupt|vermut|unsicher|beweis|fehlt|prüf|pruef"]], "man": True}},
  "sol": [["Musterlösung (Beispiele, kein Muss)", ["Unternehmensleitung: mehrere Bezugsquellen senken das Ausfallrisiko und stärken die Verhandlungsposition · Nachteil: Prüf-, Vertrags- und Umstellungskosten.",
                            "Beschäftigte/Zulieferregion: stabile Aufträge, wenn Standards vertraglich verlangt und kontrolliert werden · Nachteil: Aufträge können auch wegfallen, wenn Quellen gewechselt werden.",
                            "Nutzer/öffentliche Beschaffung: Lieferfähigkeit, Ersatzteile, Wechselmöglichkeit beim KI-Dienst, Kontrolle sensibler Daten · Nachteil: höherer Preis.",
                            "Umwelt-/Verbraucherschutz: überprüfbare Standards, Reparierbarkeit · Nachteil: Standortverlagerung allein garantiert weder faire Arbeit noch geringere Umweltfolgen.",
                            "Urteil (8c): Eine fundierte Gegenposition ist ebenso akzeptabel; die politische Richtung wird nicht benotet. Bewertet werden nachvollziehbare Begründung, fachlich richtige Zusammenhänge, Gegenargument und gekennzeichnete Unsicherheit."]]],
  "fsol": {"persp": "eine der vier Perspektiven", "arg1": "begründetes Argument", "arg2": "begründetes Argument", "massnahme": "z. B. zweite Bezugsquelle, Lagerbestand, Sozialstandards",
           "nachteil": "z. B. höhere Kosten", "zusammenhang": "z. B. mehr Quellen → weniger Ausfallrisiko, aber Mehrkosten", "offen": "z. B. »Das macht die Arbeit automatisch fairer« – nicht belegt"},
  "kriterien": ["Zusammenhang aus der Lieferkette", "soziale oder ökologische Folge", "Grenze der Maßnahme", "Wenn …, dann könnte …; offen bleibt …", "100–130 Wörter"],
  "tip": ["Kosten verteilen und Abhängigkeiten verringern", "theorie.html#gestalten"], "besprechen": True},
]
PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
assert PFLICHT == list(range(1, 9))
BESPRECHEN = [t["nr"] for t in T if t.get("besprechen")]

GRP = {1: TEILNAME[1] + " (Buch S. 43–48, 64–70) · " + wann(1),
       2: TEILNAME[2] + " (Buch S. 50–63) · " + wann(2) + " nach dem Test",
       3: TEILNAME[3] + " (Ergänzung zu Buch S. 48) · " + wann(3),
       4: TEILNAME[4] + " (Buch S. 65–77) · " + wann(4) + " · PDF-Abgabe",
       0: "OPTIONAL · Für Schnelle · im Theorieteil, keine Hausübung"}

LERNZIELE = ["Ich kann an einem Produkt erklären, wie **Waren, Geld, Daten und Wissen** grenzüberschreitend zusammenwirken.",
             "Ich kann **wirtschaftliche, soziale und ökologische Folgen** für verschiedene Gruppen erklären.",
             "Ich kann **WTO, IWF und Weltbank** unterscheiden und aktuelle Handels- oder KI-Regeln einem Problem zuordnen.",
             "Ich kann zu **KI und Globalisierung** ein begründetes Urteil formulieren und sichere Befunde von unsicheren Erwartungen trennen."]

LEITFRAGE = "Wie können wir die Vorteile weltweiter Zusammenarbeit nutzen und zugleich Abhängigkeiten, soziale Kosten und politische Risiken begrenzen?"
HEUTE_ZIEL = {1: "An der Sportuhr zeigen, wie Waren, Geld, Daten und Wissen über Grenzen fließen – und wer dabei gewinnt oder trägt.",
              2: "Zoll als Zahlung und als wirtschaftliche Last unterscheiden; WTO, IWF und Weltbank einem Problem zuordnen.",
              3: "KI-Regeln einordnen und Warnungen als Befund, Szenario oder Position prüfen.",
              4: "Abhängigkeiten und Kosten gestalten statt nur bewerten – mit begründetem eigenem Urteil."}
WICHTIGSTE = ["Globalisierung verbindet Produktion, Menschen, Wissen und Entscheidungen über Grenzen hinweg.",
              "Ihre Folgen hängen davon ab, welche Gruppe wir betrachten und welche Regeln gelten.",
              "Ein Zoll wird zunächst vom Importeur bezahlt; die wirtschaftliche Belastung kann sich verteilen.",
              "WTO, IWF und Weltbank bearbeiten unterschiedliche Probleme und haben begrenzte Macht.",
              "Bei KI müssen wir konkrete Fähigkeiten, globale Abhängigkeiten und unsichere Zukunftsszenarien auseinanderhalten."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
 ["Globalisierung", "dichte, weltweite Verflechtung von Wirtschaft, Menschen, Wissen, Kultur und Entscheidungen; keine starre, überall gültige Definition"],
 ["Internationalisierung", "Ausweitung von Wirtschaft oder Politik über die Staatsgrenze hinaus – weniger dicht als Globalisierung"],
 ["Wertschöpfungskette", "alle Stufen vom Rohstoff über Entwicklung und Herstellung bis zum Verkauf, bei denen Wert entsteht"],
 ["Standortfaktor", "Bedingung, die ein Unternehmen bei der Wahl eines Ortes abwägt: Kosten, Fachwissen, Infrastruktur, Marktzugang, Regeln"],
 ["transnationales Unternehmen", "Unternehmen, das in mehreren Staaten produziert und verkauft"],
 ["Liberalisierung", "Abbau von Handelshürden, z. B. von Zöllen"],
 ["Protektionismus", "Schutz der eigenen Wirtschaft durch Zölle oder andere Hürden"],
 ["Zoll", "Abgabe auf eine Ware beim Grenzübertritt; wird zuerst vom Importeur bezahlt"],
 ["Lieferfähigkeit", "Fähigkeit, bestellte Waren rechtzeitig zu liefern – bei Sport, Rettung oder Bundesheer so wichtig wie der Preis"],
 ["Direktinvestition", "Geld, das ein Unternehmen im Ausland in Anlagen oder Firmen steckt"],
 ["digitale Kluft", "ungleicher Zugang zu Internet und digitaler Technik"],
 ["Fachkräfteabwanderung", "Fachleute verlassen ihr Land, um anderswo zu arbeiten (Brain-Drain); bei Pflegekräften: Abwanderung von Pflegekräften"],
 ["WTO", "Welthandelsorganisation: Regeln, Verhandlungen und Streitbeilegung im Handel (seit 1995)"],
 ["IWF", "Internationaler Währungsfonds: Stabilität, Überwachung, Kredite bei Zahlungsproblemen"],
 ["Weltbank", "Entwicklungsfinanzierung und Beratung, vor allem für langfristige Vorhaben"],
 ["GATT / GATS / TRIPS", "Abkommen im WTO-System: Waren / Dienstleistungen / handelsbezogene Rechte an geistigem Eigentum"],
 ["geistiges Eigentum", "Rechte an Ideen und Erfindungen, z. B. Patente und Urheberrecht"],
 ["generative KI", "KI, die neue Texte, Bilder oder Code erzeugt"],
 ["KI-Modell / KI-Anwendung", "Modell = das trainierte System; Anwendung = der konkrete Einsatz, z. B. ein Chatbot im Kundendienst"],
 ["Hochrisiko-Anwendung", "KI-Einsatz in sensiblen Bereichen (z. B. Bewerberauswahl), für den die EU strengere Pflichten vorsieht"],
 ["Transparenzpflicht", "Pflicht, offenzulegen, dass jemand mit einer KI zu tun hat oder ein Inhalt KI-erzeugt ist"],
 ["Szenario / Simulation", "Szenario = durchgespielte mögliche Zukunft; Simulation = Versuch unter künstlich festgelegten Bedingungen"],
 ["Interessenkonflikt", "Wer etwas sagt, kann zugleich wirtschaftlich davon betroffen sein – das macht die Aussage nicht automatisch falsch, aber man prüft sie genauer"]]

WEISST_DU_NOCH = {
    2: [("Nenne einen Waren-, einen Geld-, einen Daten- und einen Wissensstrom der Sportuhr.", "z. B. Chips nach Südostasien · Zahlung vom Käufer an den Anbieter · Trainingsdaten ins Rechenzentrum · Entwicklungsvorgaben zum Hersteller."),
        ("Ist eine österreichische Marke automatisch ein österreichisches Produkt?", "Nein – Marke und Produktionsstufen sind zu unterscheiden; Entwicklung kann in Österreich liegen, Montage und Bauteile anderswo.")],
    3: [("Wer führt einen Einfuhrzoll zuerst ab – und muss er ihn am Ende allein tragen?", "Der Importeur zahlt zuerst; die Belastung kann sich auf Marge, Preis und Lieferanten verteilen."),
        ("Welche Institution ist bei einem Handelsstreit, welche bei einer Zahlungskrise zuständig?", "WTO bei Handelsstreit, IWF bei akuter Zahlungslücke; die Weltbank finanziert langfristige Entwicklungsvorhaben.")],
    4: [("Nenne die vier Bedeutungen von »KI übernimmt die Macht«.", "Arbeit · politische und wirtschaftliche Macht · Abhängigkeit · Kontrollverlust."),
        ("Warum beweist »ein Viertel betroffen« keine Arbeitslosigkeit?", "Es misst betroffene Tätigkeiten, nicht verlorene Arbeitsplätze.")],
}

STOPPFRAGEN = {
    1: [("Warum reicht eine bekannte Marke nicht als Herkunftsnachweis?", "Marke, Entwicklung und Fertigung können in verschiedenen Ländern liegen – man muss die Produktionsstufen einzeln betrachten."),
        ("Ist Globalisierung nur Warenhandel?", "Nein – auch Geld, Wissen, Menschen, Kultur und Daten gehören dazu.")],
    2: [("Wer zahlt einen Einfuhrzoll zuerst?", "Der Importeur, an die Zollbehörde des Einfuhrlandes."),
        ("Warum ist die WTO keine Weltregierung?", "Ihre Mitglieder entscheiden im Konsens; sie kann Staaten nicht zu etwas zwingen. Außerdem ist sie keine UN-Sonderorganisation.")],
    3: [("Was ist der Unterschied zwischen Verbot, Hochrisiko und Transparenzpflicht?", "Verbot: bestimmte Praktiken sind untersagt. Hochrisiko: strenge Anforderungen für sensible Einsatzbereiche. Transparenz: man muss erkennen können, dass KI im Spiel ist."),
        ("Warum zeigt eine Simulation nicht, wie oft etwas im Alltag passiert?", "Sie läuft unter festgelegten, künstlichen Bedingungen; die Häufigkeit im Alltag wird damit nicht gemessen.")],
    4: [("Ändert eine zweite Bezugsquelle automatisch die Arbeitsbedingungen?", "Nein – sie senkt vor allem die Abhängigkeit; faire Arbeit braucht überprüfbare Standards."),
        ("Was gehört in ein begründetes Urteil?", "Eine Entscheidung mit Beleg, Gegenargument, Bedingung und gekennzeichneter Unsicherheit.")],
}

PARTNERKARTEN = [("Nenne die vier Arten von Strömen bei der Sportuhr.", "Waren, Geld, Daten, Wissen."),
                 ("Wer zahlt einen Zoll zuerst?", "Der Importeur."),
                 ("Bedeutet 15 % Zoll immer 15 % mehr Ladenpreis?", "Nein – Weitergabe, Marge, Nachfrage und Wettbewerb fehlen in der Rechnung."),
                 ("Welches Problem gehört zu WTO, IWF, Weltbank?", "Handelsstreit · akute Zahlungslücke · langfristiges Entwicklungsvorhaben."),
                 ("Was bedeutet GATS?", "Abkommen über den Handel mit Dienstleistungen."),
                 ("Ist die EU-KI-Verordnung ein vollständiges KI-Verbot?", "Nein – sie arbeitet nach Risiko und Einsatzbereich."),
                 ("Was zeigt »ein Viertel betroffen«?", "Betroffene Tätigkeiten – keine Arbeitslosenquote."),
                 ("Was gehört in ein begründetes Urteil?", "Beleg, Gegenargument, Bedingung, Unsicherheit.")]

STOLPERSTEINE = [("Aktuelle Zollzahlen ohne Datum und Warengruppe verallgemeinern", "Zölle gelten für bestimmte Waren, Länder und Zeiträume und werden gerichtlich und politisch geändert. Immer Datum und Rechtsgrundlage nennen; das Buch beschreibt den Stand 2025."),
                 ("WTO, IWF und Weltbank auf dieselbe Aufgabe reduzieren", "Handelsregeln und Streit (WTO), kurzfristige Stabilität und Zahlungsprobleme (IWF), langfristige Entwicklungsfinanzierung (Weltbank). Diese Aufgaben werden oft vermischt – im Buch gegenprüfen."),
                 ("KI-Betroffenheit mit Arbeitsplatzverlust verwechseln", "»Ein Viertel der Beschäftigten arbeitet in einem Beruf mit möglichem KI-Einfluss« heißt nicht, dass ein Viertel der Stellen verschwindet."),
                 ("Simulation, reale Vorfälle und Zukunftsszenarien vermischen", "Ein Versuch in gestellter Umgebung zeigt eine mögliche Schwachstelle – nicht die Häufigkeit im Alltag und keine bereits erfolgte Machtübernahme."),
                 ("Interessen ohne Beleg als persönliche Motive behaupten", "Aus einer Schlagzeile kann man Motive (»Angst«, »PR«) nicht ablesen. Eine Warnung kann fachlich begründet sein und zugleich wirtschaftliche Wirkung haben.")]

# (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite/Hinweis) – 16 Fragen, Antworten werden beim Anzeigen gemischt
QUIZ = [
 ("Begriff", "Ist Globalisierung ausschließlich Warenhandel?", ["Nein, auch Wissen, Geld, Menschen, Kultur und Daten sind betroffen.", "Ja, nur Waren überqueren Grenzen.", "Ja, aber nur Rohstoffe.", "Ja, Wissen und Daten gehören nur zur Digitalisierung."],
  "Globalisierung ist eine dichte, weltweite Verflechtung in mehreren Dimensionen – nicht nur Handel.", "Buch S. 43–48"),
 ("Sportuhr", "Reicht eine bekannte österreichische Marke als Nachweis, dass ein Produkt aus Österreich kommt?", ["Nein, Marke und Produktionsstufen sind zu unterscheiden.", "Ja, die Marke zeigt in der Regel den Ort der Herstellung.", "Ja, wenn der Firmensitz in Österreich liegt.", "Ja, wenn die Marke schon seit Jahrzehnten am Markt ist."],
  "Entwicklung, Bauteile, Montage und Vertrieb können in verschiedenen Ländern liegen. Das Beispiel der Sportuhr ist ein Modell.", "Buch S. 43–48 · Modellfall"),
 ("Folgen", "Welche Aussage über die Folgen der Globalisierung ist am besten begründet?", ["Sie hängen davon ab, welche Gruppe man betrachtet und welche Regeln gelten.", "Alle Menschen profitieren gleich.", "Nur die Industrieländer verlieren.", "Regionale Produkte sind immer besser für die Umwelt."],
  "Es gibt Gewinner und Belastete – auch innerhalb eines Staates. Umweltwirkung nicht nur aus Transportkilometern ableiten.", "Buch S. 64–70"),
 ("Zoll", "Wer zahlt einen Einfuhrzoll zunächst?", ["Der Importeur.", "Das Ausland automatisch.", "Immer der Verbraucher.", "Die WTO."],
  "Der Importeur führt den Zoll an die Zollbehörde ab. Die spätere Belastung kann sich auf Marge, Lieferant und Käufer verteilen.", "Buch S. 50–51"),
 ("Zoll", "Bedeutet ein Zollsatz von 15 Prozent immer 15 Prozent mehr beim Ladenpreis?", ["Nein, dazu fehlen Annahmen über Kosten und Weitergabe.", "Ja, der Preis steigt genau um 15 Prozent.", "Ja, aber nur im ersten Monat.", "Ja, aber nur bei Waren aus China."],
  "Der Zoll wirkt auf den Zollwert. Ob und wie er weitergegeben wird, hängt von Nachfrage, Verträgen, Wettbewerb und Wechselkurs ab.", "Buch S. 50–51 · Aufgabe 3"),
 ("Zoll aktuell", "Was gilt für die US-Zölle des Jahres 2025, die das Buch beschreibt, heute?", ["Ein Teil wurde 2026 gerichtlich gekippt; andere Zollarten gelten weiter – daher immer Datum und Rechtsgrundlage nennen.", "Sie gelten unverändert für alle Waren weiter.", "Sie wurden komplett abgeschafft, es gibt keine US-Zölle mehr.", "Sie betreffen nur die EU."],
  "Der US Supreme Court erklärte am 20.02.2026 die auf IEEPA gestützten Zölle für rechtswidrig. Andere Rechtsgrundlagen (z. B. Section 232 und 301) bestehen weiter. Aktuelle Ergänzung zu Buch S. 50–51; Quellen WKO und IHK, Stand 30.10.2026.", "Aktuelle Ergänzung zu Buch S. 50–51"),
 ("Institutionen", "Zwei Staaten streiten über eine Handelsbeschränkung. Wer ist vor allem zuständig?", ["WTO", "IWF", "Weltbank", "OECD allein"],
  "Die WTO hat Regeln, Verhandlungen und ein Streitverfahren. Die Berufungsinstanz ist derzeit blockiert.", "Buch S. 53–56"),
 ("Institutionen", "Ein Staat hat eine akute Lücke bei der Finanzierung seiner Zahlungen ans Ausland. Wer ist vor allem zuständig?", ["IWF", "WTO", "Weltbank", "UNESCO"],
  "Der IWF sichert Stabilität und kann bei Zahlungsbilanzproblemen Kredite mit Bedingungen geben.", "Buch S. 53, 60–62"),
 ("Institutionen", "Wofür steht GATS inhaltlich?", ["Internationaler Handel mit Dienstleistungen.", "Handel mit Waren.", "Rechte an geistigem Eigentum.", "Entwicklungskredite."],
  "GATT = Waren, GATS = Dienstleistungen, TRIPS = handelsbezogene Rechte an geistigem Eigentum. Die WTO gibt es seit 1995. (Oft verwechselt: GATT wurde nicht von GATS abgelöst, die WTO löste 1995 das GATT als Organisation ab; GATS ist ein eigenes Abkommen.)", "Buch S. 54–56"),
 ("Institutionen", "Wer leitet derzeit (Stand 30.10.2026) den Internationalen Währungsfonds?", ["Kristalina Georgieva.", "Christine Lagarde.", "Ajay Banga.", "Ngozi Okonjo-Iweala."],
  "Georgieva leitet den IWF. Lagarde war IWF-Chefin bis 2019 und ist EZB-Präsidentin. Banga leitet die Weltbankgruppe, Okonjo-Iweala die WTO. Aktuelle Ergänzung – Namen vor dem Unterricht prüfen.", "Aktuelle Ergänzung · Stand 30.10.2026"),
 ("KI Arbeit", "Bedeutet »ein Viertel der Beschäftigten ist betroffen« auch »ein Viertel ist arbeitslos«?", ["Nein, es geht um mögliche Veränderung von Tätigkeiten.", "Ja, genau ein Viertel verliert die Stelle.", "Ja, aber nur in Österreich.", "Ja, wenn die Beschäftigten in Europa arbeiten."],
  "Die ILO-Studie (2025) misst, in wie vielen Berufen generative KI Tätigkeiten verändern könnte – nicht verlorene Arbeitsplätze.", "Aktuelle Ergänzung · Quelle ILO 2025"),
 ("KI Regeln", "Ist die EU-KI-Verordnung ein vollständiges KI-Verbot?", ["Nein, Pflichten hängen von Risiko und Anwendung ab.", "Ja, KI ist in der EU verboten.", "Ja, aber nur für Unternehmen.", "Ja, seit 2026 für alle Anwendungen ohne Ausnahme."],
  "Es gibt Verbote für bestimmte Praktiken, strenge Pflichten für Hochrisiko-Anwendungen und Transparenzpflichten. Fristen wurden 2026 durch den »AI Omnibus« angepasst.", "Aktuelle Ergänzung · Quelle EU-Kommission"),
 ("KI Energie", "Die IEA nennt für 2030 rund 945 TWh Strombedarf der Rechenzentren. Wie ist die Zahl einzuordnen?", ["Als Projektion, nicht als Messwert.", "Als gemessener Wert von 2030.", "Als Verbrauch allein der KI.", "Als gesicherte Obergrenze."],
  "Gemessen ist 2024 (rund 415 TWh). Die 2030-Zahl ist ein Szenario, und »alle Rechenzentren« ist nicht gleich »nur KI«. Aktuelle Ergänzung; Quelle IEA »Energy and AI« (2025).", "Aktuelle Ergänzung · Quelle IEA"),
 ("KI Risiko", "Beweist ein Versuch in einer Simulation, wie oft KI im Alltag täuscht?", ["Nein, die Versuchsbedingungen begrenzen die Schlussfolgerung.", "Ja, die Häufigkeit ist damit gemessen.", "Ja, aber nur bei Chatbots.", "Ja, wenn die Simulation viele Läufe umfasst."],
  "Eine Simulation kann ein mögliches Versagen unter bestimmten Bedingungen zeigen. Die Häufigkeit im Alltag misst sie nicht.", "Aktuelle Ergänzung · Quellenkarten"),
 ("Quellen", "Beweist die Warnung von KI-Firmenchefs automatisch, dass sie nur aus Werbegründen warnen?", ["Nein, Motive lassen sich aus einer Schlagzeile nicht ablesen.", "Ja, Firmen wollen immer nur Werbung.", "Ja, sonst würden sie nicht warnen.", "Ja, sobald das Unternehmen selbst KI verkauft."],
  "Eine Warnung kann fachlich begründet sein und zugleich die öffentliche Wahrnehmung beeinflussen. Interessen sind eine prüfbare Hypothese, kein Beweis.", "Aktuelle Ergänzung · Aufgabe 6"),
 ("Urteil", "Was macht ein begründetes Urteil aus?", ["Eine Entscheidung mit Beleg, Gegenargument und Bedingung.", "Eine möglichst lange Meinung.", "Eine Aussage, der alle zustimmen.", "Ein Satz ohne Einschränkung."],
  "Auch eine fundierte Gegenposition ist akzeptabel. Wichtig sind Begründung, richtige Zusammenhänge und gekennzeichnete Unsicherheit.", "Aufgabe 8"),
]
# Sechs Fragen für den Selbstcheck in Stunde 4 (Nummern der Quizfragen, ab 1)
SELBSTCHECK = [4, 5, 8, 11, 14, 16]
assert len(QUIZ) == 16 and all(len(q[2]) == 4 for q in QUIZ)
