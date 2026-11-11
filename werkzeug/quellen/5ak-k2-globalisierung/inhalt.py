"""IWK 5AK · K2.1 Die Welt ohne Grenzen: Globalisierung (Trauner IWK, Teil II, S. 42–51) – v5.
Neu aufgebaut am 11.11.2026 nach den Schulbuchseiten S. 42–51 und Stephans PPP des Vorjahres (»Globalisierung – wann begann sie?«); die frühere Fassung (v1–v4, Sportuhr-Modellfall,
KI-Regeln, vier Stunden) ist ersetzt. Stundenplan (Stephan, 11.11.2026): Fr 13.11. = Stunde 1 (volle Stunde), Fr 20.11. = Stunde 2 mit angekündigtem Test (Annahme 20 min).
Institutionen der Globalisierung (Buch S. 52–63) folgen als eigene Einheit ab Fr 27.11., Auswirkungen (S. 64–77) danach – nicht Teil dieser Einheit.
Realistisch nutzbar sind 40 min je Stunde (Regel 06.11.2026); Stunde 2: 20 min Test + 20 min Unterricht.
Kein Versuch, kein Kahoot, keine Referate, keine Hausübung. Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "11.11.2026"
V = "v5"
ORDNER = "5ak-iwk/k2-1-globalisierung"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "5ak-iwk/"
EYEBROW = "IWK · 5AK · K2.1 Globalisierung"
TITEL = "Die Welt ohne Grenzen: Globalisierung – Zufall, Überlegenheit oder alternativlos?"
KURZTITEL = "Globalisierung"
BUCH = "Buch S. 42–51"
KEY = "26-27-5AK-K2.1-Global-TH-Handy-v1"
CHECK_KEY = "26-27-5AK-K2.1-Global-Lernseite-Check-v1"
PRAEFIX = "26-27-5AK-K2.1-Global"
KAP = "K2.1"
TEST = "Fr 20.11.2026"

VIDEOS = {}


def zeigen(key, lehrer=False):
    return False


KLASSEN = ["5AK"]
_D = {1: "Fr 13.11.", 2: "Fr 20.11."}
DATEN = {k: dict(_D) for k in KLASSEN}
TEIL_STUNDE = {t: {k: t for k in KLASSEN} for t in (1, 2)}
TEILNAME = {1: "Stunde 1 · Wann begann die Globalisierung – und was treibt sie an?",
            2: "Stunde 2 · Digitalisierung und »Ziele erreicht?« (nach dem Test)"}
TEILKURZ = {1: "Beginn und Antriebskräfte", 2: "Digitalisierung und Statement-Ampel"}
TEILBUCH = {1: "Buch S. 42–47", 2: "Buch S. 48–51"}


def wann(teil=None):
    if teil: return _D[teil]
    return " · ".join(_D[t] for t in (1, 2))


# ======================================================================= Aufgaben
# 3 Pflichtaufgaben (Stunde 1: Aufgabe 1 und 2, Stunde 2: Aufgabe 3) + 3 Zusatzaufgaben (nur wer fertig ist). Höchstens EINE offene Pflichtaufgabe: Aufgabe 1 (Teilfelder, Lehrkraft liest nur c und e).
# Aufgabe 2 und 3 sind überwiegend automatisch prüfbar. KI-Regel (Stephan, 07.11.2026): jede Aufgabe sagt »ohne KI« oder »KI erlaubt«.
# tipp1 = Denkanstoß, karte = Theorie-Karte (Tipp 2, aus theorie_daten.KARTEN), tipp3 = Leseauftrag im Buch.
_OPT = ["Informationsrevolution", "Innovationen im Transport", "Marktwirtschaft", "Liberalisierung", "Transnationale Konzerne", "Normen und Standards"]
T = [
 {"id": "a1", "nr": 1, "title": "Wann begann die Globalisierung?", "src": "Buch S. 43–44", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 9,
  "q": "Lies im Buch S. 43–44 den Abschnitt »Für manche begann die Globalisierung …« und die Absätze darunter. KI: ohne KI. "
       "a) Tipp zuerst, ohne nachzulesen (Was glaubst du?). b) Nenne drei Ereignisse, die man als Beginn ansetzen kann (Stichwort + Jahr). "
       "c) Rechne: Wie viele Jahre liegen zwischen 1492 und 1944? d) Welche Aussage passt zum Buch? e) Welcher Beginn überzeugt dich am meisten? Begründe in 2 Sätzen.",
  "hint": "Es gibt keine richtige Jahreszahl – es zählt, welches Kriterium du wählst.",
  "type": "multi",
  "fields": [["wg", "a) Was glaubst du? Die Globalisierung begann …", ["um 1492 (Kolumbus)", "um 1844 (erste Nachricht per Telegraf)", "um 1944 (IWF und Weltbank)", "erst in den 1980er/1990er Jahren (Technik, Internet)", "je nach Kriterium früher oder später"], False],
             ["drei", "b) Drei Ereignisse (Stichwort + Jahr)"], ["jahre", "c) Jahre zwischen 1492 und 1944"],
             ["buch", "d) Welche Aussage passt zum Buch?", ["Es gibt nur einen einzigen, klar belegten Beginn.", "Je nach Kriterium beginnt die Globalisierung früher oder später.", "Sie begann erst mit dem Internet.", "Sie begann mit dem Ersten Weltkrieg."]],
             ["wahl", "e) Mein Beginn und warum (2 Sätze)"]],
  "chk": {"drei": {"kw": [["drei Ereignisse", r"kolumbus|1492|adam smith|morse|1844|telegraf|iwf|weltbank|1944|gatt|gats|1995|internet|satellit|kommunikationstechn|1980|1960|handelshemmnis|dampf|eisenbahn|container", 3]], "man": True},
          "jahre": {"num": 452, "ende": True},
          "buch": {"sel": "Je nach Kriterium beginnt die Globalisierung früher oder später."},
          "wahl": {"kw": [["Begründung", r"weil|da |denn|deshalb|kriteri|technik|handel|verflecht|regel|netz|kommunikation|zeit|schiff"]], "man": True}},
  "sol": [["Musterlösung", ["a) Ohne Wertung – die Vermutung wird am Ende mit dem Buch verglichen.",
                           "b) Z. B.: 1492 Kolumbus erreicht Amerika · 1844 erste Nachricht per Telegraf (Morse) · 1944 Gründung von IWF und Weltbank · 1980er technische Entwicklungen, Rivalität USA – Sowjetunion · 1995 WTO löst das GATT ab · Kommunikationssatelliten und Internet.",
                           "c) 1944 − 1492 = 452 Jahre.",
                           "d) Je nach Kriterium (Entdeckungen, Handelsliberalismus, Technik, Institutionen) beginnt die Globalisierung früher oder später. Das Buch nennt auch die Deglobalisierung der Zwischenkriegszeit.",
                           "e) Offen. Gute Antworten nennen ein Kriterium (z. B. Verflechtung über Kontinente = 1492; Regeln = 1944; Datenverkehr = Internet) und begründen, warum es Globalisierung ausmacht."]]],
  "fsol": {"wg": "keine Wertung", "drei": "z. B. 1492 Kolumbus · 1844 Telegraf · 1944 IWF/Weltbank", "jahre": "452", "buch": "je nach Kriterium früher oder später", "wahl": "ein Kriterium + Begründung"},
  "tip": ["Wann begann die Globalisierung?", "theorie.html#beginn"], "besprechen": True,
  "tipp1": "Denk an ein Kriterium: Handel über Kontinente, schnelle Nachrichten, gemeinsame Regeln oder Internet – je nachdem beginnt die Globalisierung früher oder später.",
  "tipp3": "Lies im Buch S. 43 den Kasten »Für manche begann die Globalisierung …« und S. 44 die ersten beiden Absätze.",
  "karte": "beginn",
  "wgvergleich": {"feld": "wg", "text": "Das Buch nennt mehrere Standpunkte (1492, Mitte des 19. Jahrhunderts, 1944, 1980er, Kommunikationstechnik). Die Antwort »je nach Kriterium früher oder später« passt am besten – eine einzige Geburtsstunde gibt es nicht.", "richtig": "je nach Kriterium früher oder später"}},

 {"id": "a2", "nr": 2, "title": "Sechs Antriebskräfte und Liberalisierung", "src": "Buch S. 45–47", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 10,
  "q": "Lies im Buch S. 45–47 die Antriebskräfte. KI: ohne KI. a) Ordne vier Beispiele der passenden Antriebskraft zu. b) Erkläre den Begriff »Liberalisierung« in eigenen Worten (1–2 Sätze, Buch S. 46). "
       "c) Nenne einen Bezug zu einem anderen Prozess der Globalisierung (z. B. Konzerne, Transport, Internet).",
  "hint": "Jedes Beispiel passt am besten zu genau einer Antriebskraft. Info: Theorie-Karte »Sechs Antriebskräfte«",
  "type": "multi",
  "fields": [["f1", "a) Ein Konzern produziert auf drei Kontinenten und verkauft weltweit.", _OPT],
             ["f2", "a) Staaten senken Zölle und öffnen die Märkte für Telefon- und Stromanbieter.", _OPT],
             ["f3", "a) Container und Großraumflugzeuge machen Transporte billiger.", _OPT],
             ["f4", "a) Weltweit gelten dieselben Standards für Stecker und Schienen.", _OPT],
             ["libdef", "b) Liberalisierung in eigenen Worten (1–2 Sätze)"], ["libbez", "c) Ein Bezug zu einem anderen Prozess"]],
  "chk": {"f1": {"sel": "Transnationale Konzerne"}, "f2": {"sel": "Liberalisierung"}, "f3": {"sel": "Innovationen im Transport"}, "f4": {"sel": "Normen und Standards"},
          "libdef": {"kw": [["Abbau von Hürden", r"abbau|öffn|oeffn|zoll|handelshemmnis|frei|hürde|huerde|beschränk|beschraenk|dereguli|privatisier"], ["Märkte", r"markt|handel|kapital|güter|gueter|dienstleist|wirtschaft"]], "man": True},
          "libbez": {"kw": [["Bezug", r"konzern|unternehmen|digital|internet|transport|kapital|privatisier|outsourcing|auslager|informations|markt|global|finanz"]], "man": True}},
  "sol": [["Musterlösung", ["a) Konzern auf drei Kontinenten → Transnationale Konzerne · Zölle senken, Märkte öffnen → Liberalisierung · Container und Großraumflugzeuge → Innovationen im Transport · gleiche Stecker- und Schienenstandards → Normen und Standards.",
                           "b) Liberalisierung heißt: Staaten bauen Handelshemmnisse (z. B. Zölle und Beschränkungen) ab und öffnen Märkte für Güter, Dienstleistungen und Kapital; dazu gehören auch Deregulierung und Privatisierung (z. B. Telefon, Strom, Wasser).",
                           "c) Z. B.: Liberalisierung erleichtert es transnationalen Konzernen, weltweit zu produzieren und zu verkaufen. Oder: Das Internet macht den Kapital- und Datenverkehr der liberalisierten Märkte schneller."]]],
  "fsol": {"f1": "Transnationale Konzerne", "f2": "Liberalisierung", "f3": "Innovationen im Transport", "f4": "Normen und Standards", "libdef": "Abbau von Handelshemmnissen, Öffnung der Märkte", "libbez": "z. B. Konzerne nutzen offene Märkte"},
  "tip": ["Sechs Antriebskräfte", "theorie.html#antrieb"], "besprechen": True,
  "tipp1": "Frag dich bei jedem Beispiel: Geht es um Technik, um Regeln, um Unternehmen oder um offene Märkte?",
  "tipp3": "Lies im Buch S. 45 (Informationsrevolution, Transport) und S. 46 (Marktwirtschaft, Liberalisierung, Konzerne, Normen).",
  "karte": "antrieb"},

 {"id": "a3", "nr": 3, "title": "Digital Divide: Wer ist offline?", "src": "Buch S. 48 · ITU 2025", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 8,
  "q": "Lies im Buch S. 48 »Ein Segen für alle?« und werte die Tabelle aus (ITU, Facts and Figures 2025, Anteil der Menschen, die das Internet nutzen). KI: ohne KI. "
       "a) Wie groß ist der Unterschied zwischen Ländern mit hohem und mit niedrigem Einkommen (Prozentpunkte)? b) Unterschied Stadt – Land (Prozentpunkte)? c) Wie viele Menschen sind laut ITU 2025 noch offline? "
       "d) Das Buch nennt rund 32 % ohne Internet. Woran kann es liegen, dass Quellen verschieden zählen? e) Nenne einen Lebensbereich, in dem Offline-Sein heute ein Nachteil ist, und warum (1 Satz).",
  "hint": "Prozentpunkte = Differenz der beiden Prozentwerte. Quellen zählen oft verschieden (Jahr, Messweise).",
  "type": "multi",
  "tab": [["Gruppe", "Internetnutzer 2025"], ["Länder mit hohem Einkommen", "94 %"], ["Länder mit niedrigem Einkommen", "23 %"], ["Stadtbevölkerung", "85 %"], ["Landbevölkerung", "58 %"], ["Männer", "77 %"], ["Frauen", "71 %"]],
  "tabnote": "Quelle: ITU, Facts and Figures 2025 (17.11.2025). Weltweit rund 6 Mrd. Menschen online, 2,2 Mrd. offline.",
  "fields": [["diff", "a) Hoch – niedrig (Prozentpunkte)"], ["sl", "b) Stadt – Land (Prozentpunkte)"],
             ["off", "c) Offline laut ITU 2025", ["rund 2,2 Milliarden", "rund 220 Millionen", "rund 6 Milliarden", "rund 0,5 Milliarden"]],
             ["quelle", "d) Warum zählen Quellen verschieden?", ["Jahr, Messweise und Definition von »Nutzer« können sich unterscheiden.", "Eine der beiden Quellen ist wertlos.", "Das Internet wurde 2025 wieder kleiner.", "Offline gibt es nur auf dem Land."]],
             ["bereich", "e) Lebensbereich und Nachteil (1 Satz)"]],
  "chk": {"diff": {"num": 71, "ende": True}, "sl": {"num": 27, "ende": True}, "off": {"sel": "rund 2,2 Milliarden"},
          "quelle": {"sel": "Jahr, Messweise und Definition von »Nutzer« können sich unterscheiden."},
          "bereich": {"kw": [["Bereich", r"arbeit|bildung|schule|lernen|gesundheit|telemedizin|bank|behörde|behoerde|homeoffice|einkauf|kommunikation|information|nachrichten|corona|amt|job"]], "man": True}},
  "sol": [["Musterlösung", ["a) 94 − 23 = 71 Prozentpunkte. b) 85 − 58 = 27 Prozentpunkte. c) Rund 2,2 Milliarden Menschen (ITU 2025).",
                           "d) Quellen können verschiedene Jahre, Messmethoden und Definitionen (Nutzer, Zugang, Haushalte) verwenden. Darum nennt man Quelle und Jahr und vergleicht nicht blind. Das Buch nennt rund 32 % für 2025; die ITU rund 2,2 Mrd. von ca. 8 Mrd. Menschen, also etwa ein Viertel – gleiche Richtung, andere Zahl.",
                           "e) Z. B. Bildung: Distance Learning und Plattformen setzen Internet voraus. Oder Arbeit/Homeoffice, Telemedizin, Behördenwege, Einkauf. In der Corona-Pandemie hat das die Ungleichheit sichtbar gemacht."]]],
  "fsol": {"diff": "71", "sl": "27", "off": "rund 2,2 Milliarden", "quelle": "Jahr, Messweise, Definition", "bereich": "z. B. Bildung: Plattformen brauchen Internet"},
  "tip": ["Digital Divide", "theorie.html#digital"], "besprechen": True,
  "tipp1": "Prozentpunkte rechnest du als Unterschied: größerer Wert minus kleinerer Wert.",
  "tipp3": "Lies im Buch S. 48 den Abschnitt »Ein Segen für alle?« und den Kasten mit der Definition von »Digital Divide«.",
  "karte": "digital"},

 # ======================================================= Zusatz (nur wer fertig ist, Gruppe 0)
 {"id": "a4", "nr": 4, "title": "Woher kommt dein Alltag?", "src": "Buch S. 44 · Arbeitsaufgabe", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Such im Klassenzimmer oder in deiner Tasche drei Gegenstände mit Herkunftsangabe (Etikett, Typenschild, Aufdruck). KI: ohne KI. Trag ein: Gegenstand und Land. Wo ist die Herkunft schwer zu erkennen – und warum? "
       "Bundesheer-Bezug: Wähle ein Ausrüstungsstück (z. B. Rucksack, Stiefel, Funkgerät) und überlege, welche Stufen der Herstellung im Ausland liegen könnten (als Vermutung kennzeichnen).",
  "hint": "Auf dem Etikett steht oft nur, wo zusammengebaut wurde – nicht, woher die Teile kommen.",
  "type": "multi",
  "fields": [["funde", "Drei Gegenstände mit Land"], ["schwer", "Wo ist die Herkunft schwer zu erkennen – und warum?"], ["heer", "Ausrüstungsstück: mögliche Auslands-Stufen (Vermutung)"]],
  "chk": {"funde": {"kw": [["drei Gegenstände", r"[a-zäöüß]{3,}.{0,20}(china|japan|vietnam|deutschland|österreich|oesterreich|italien|usa|türkei|tuerkei|indien|bangladesch|polen|tschechien|taiwan|korea|indonesien|kambodscha|slowakei|ungarn|frankreich|schweiz|spanien|rumänien|rumaenien|bulgarien|pakistan|thailand|malaysia|mexiko|brasilien)", 3]], "man": True},
          "schwer": {"kw": [["Begründung", r"weil|montage|bauteil|teile|etikett|marke|zusammenbau|rohstoff|nur|angabe|kennzeichn|made in|hergestellt"]], "man": True},
          "heer": {"kw": [["Vermutung", r"vermut|könnte|koennte|wahrscheinlich|möglich|moeglich|vielleicht|rohstoff|bauteil|stoff|chip|montage|nähen|naehen|produktion|ausland"]], "man": True}},
  "sol": [["Musterlösung (Beispiele)", ["Funde: z. B. Rucksack – Vietnam · Handy – China · Kugelschreiber – Deutschland. Die Länder hängen vom Etikett ab.",
                                     "Schwierig: Das Etikett nennt meist den Ort der letzten wesentlichen Fertigung, nicht die Herkunft der Rohstoffe und Bauteile; Marke und Firmensitz sagen wenig.",
                                     "Ausrüstung: z. B. Stiefel – Leder, Gummi, Garn und Montage können aus verschiedenen Ländern stammen; ohne Beleg bleibt es eine Vermutung."]]],
  "fsol": {"funde": "z. B. Rucksack – Vietnam", "schwer": "Etikett nennt nur den Ort der Montage", "heer": "z. B. Stiefel: Material aus dem Ausland (Vermutung)"},
  "tip": ["Wann begann die Globalisierung?", "theorie.html#beginn"], "besprechen": False,
  "tipp1": "Schau auf Etiketten, Typenschilder und Aufdrucke – »Made in …« sagt nicht alles.",
  "tipp3": "Lies im Buch S. 44 den Text »Globalisierung im Alltag« und die Arbeitsaufgabe darunter.",
  "karte": "beginn"},

 {"id": "a5", "nr": 5, "title": "US-Zölle: 2025 und heute", "src": "Buch S. 50–51 · aktuelle Meldung", "own": True, "tag": "Zusatz", "h": 0, "zeit": 10,
  "q": "Das Buch beschreibt US-Zölle des Jahres 2025 (S. 50–51). KI: ohne KI. a) Rechne das Zeitungsbeispiel nach: Ein Gerät kostet vor dem Zoll 799 US-Dollar (Zollwert), der Zollsatz beträgt 145 %. Wie hoch ist der Zoll, wie hoch die Summe (ohne weitere Kosten, gerundet auf ganze US-Dollar)? "
       "b) Nenne eine Gruppe, die von Zöllen profitieren kann, und eine, die verliert. c) Welche Aussage über solche Zollzahlen stimmt?",
  "hint": "Das Buch zeigt den Stand 2025. Lies auch die Karte »Zölle 2025 und heute« im Theorieteil.",
  "type": "multi",
  "fields": [["zoll", "a) Zoll in US-Dollar"], ["summe", "b) Summe in US-Dollar"], ["gv", "b) Eine Gruppe, die profitiert, und eine, die verliert"],
             ["stand", "c) Welche Aussage stimmt?", ["Zollsätze gelten für Waren, Länder und Zeiträume und haben sich seither mehrfach geändert – Datum nennen.", "Sie gelten unverändert für immer.", "Sie wurden nie wirklich erhoben.", "Sie betreffen nur Österreich."]]],
  "chk": {"zoll": {"num": 1159, "ende": True}, "summe": {"num": 1958, "ende": True},
          "gv": {"kw": [["Gewinner", r"heimisch|us-industrie|hersteller|arbeitsplätze|arbeitsplaetze|staat|regierung|zolleinnahmen|landwirt|stahl"], ["Verlierer", r"verbraucher|konsument|importeur|exporteur|händler|haendler|preise|china|unternehmen|apple|aktion|landwirt|kunden"]], "man": True},
          "stand": {"sel": "Zollsätze gelten für Waren, Länder und Zeiträume und haben sich seither mehrfach geändert – Datum nennen."}},
  "sol": [["Musterlösung", ["a) 799 × 1,45 = 1 158,55, gerundet 1 159 US-Dollar Zoll. b) 799 + 1 158,55 = 1 957,55, gerundet 1 958 US-Dollar – das entspricht der Zahl im Zeitungsbeispiel des Buches (Annahme: voller Zoll wird weitergegeben, keine weiteren Kosten).",
                           "Gewinner möglich: heimische Hersteller geschützter Waren, der Staat durch Zolleinnahmen. Verlierer möglich: Verbraucher mit höheren Preisen, Importeure, Exporteure bei Gegenzöllen.",
                           "c) Solche Zahlen hängen von Datum, Ware, Land und Rechtsgrundlage ab. Seither haben sich Zölle durch Urteile, Verhandlungen und Zollpausen mehrfach geändert (siehe Karte im Theorieteil)."]]],
  "fsol": {"zoll": "1159", "summe": "1958", "gv": "z. B. heimische Industrie · Verbraucher", "stand": "Datum und Rechtsgrundlage nennen"},
  "tip": ["Zölle 2025 und heute", "theorie.html#zoelle"], "besprechen": False,
  "tipp1": "Zoll = Zollwert mal Zollsatz. 145 % sind 1,45.",
  "tipp3": "Lies im Buch S. 50 den Abschnitt »Donald Trump – Gegner der Globalisierung oder Deal Maker?« und den Zeitungskasten.",
  "karte": "zoelle"},

 {"id": "a6", "nr": 6, "title": "Stiglitz: Was kritisiert er?", "src": "Buch S. 49 · Buch-Aufgaben 1–3", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Lies im Buch S. 49 den Text von Joseph Stiglitz. KI erlaubt: nur um unbekannte Wörter nachzuschlagen – schreib dazu, was du gefragt hast. a) Nenne stichwortartig seine zentralen Argumente (mindestens drei). "
       "b) Beurteile: Ist Globalisierung für ihn eher positiv oder negativ? Begründe. c) Nimm Stellung zur These, dass die Menschen der wichtigste Produktionsfaktor eines Landes sind (2 Sätze).",
  "hint": "Stiglitz ist US-Ökonom und war nach dem Buch Chefökonom der Weltbank – er bewertet Globalisierung differenziert.",
  "type": "multi",
  "fields": [["args", "a) Zentrale Argumente (mindestens drei)"], ["bewert", "b) Eher positiv oder negativ – warum?"], ["these", "c) Menschen als wichtigster Produktionsfaktor – meine Stellung"]],
  "chk": {"args": {"kw": [["Argumente", r"märkte|maerkte|öffnung|oeffnung|armut|afrika|china|subvention|agrar|patent|biopiraterie|bildung|ausbildung|hochschul|outsourcing|indien|löhne|loehne|ungleich|treibhaus|klima|terror|krankheit|nicht allein|nicht lösen|nicht loesen", 3]], "man": True},
          "bewert": {"kw": [["Urteil", r"positiv|negativ|differenz|beides|chancen|risiken|weil|nicht nur|ungleich|armut|gewinner|verlierer"]], "man": True},
          "these": {"kw": [["Stellung", r"mensch|bildung|ausbildung|produktionsfaktor|kapital|technik|arbeit|zustimm|stimme|weil|denn|rohstoff"]], "man": True}},
  "sol": [["Musterlösung (Beispiele)", ["a) Globalisierung ist mehr als Liberalisierung der Märkte · Offene Märkte allein lösen die Armut nicht · Reiche Staaten behalten Agrarsubventionen, arme müssen Subventionen abbauen · Biopiraterie und Patente auf traditionelles Wissen · Bildung und Hochschulen sind der Schlüssel (Beispiel Indien/Bangalore) · Auch in Industrieländern geraten gering Qualifizierte unter Druck.",
                                     "b) Differenziert: Chancen bei Bildung und Wachstum, aber starke Ungleichheit und Verlierer. Eine eindeutige Antwort ist nicht verlangt, die Begründung zählt.",
                                     "c) Beide Richtungen möglich: Für die These spricht, dass Wissen und Bildung Wirtschaftskraft schaffen (Stiglitz). Dagegen können Rohstoffe, Kapital und Technik eigene Gewichte haben."]]],
  "fsol": {"args": "mind. drei Argumente aus dem Text", "bewert": "differenziert, mit Begründung", "these": "Zustimmung oder Gegenposition mit Begründung"},
  "tip": ["Stiglitz", "theorie.html#stiglitz"], "besprechen": False,
  "tipp1": "Suche im Text Stellen mit »nicht«, »aber« und »Beispiel« – dort steckt oft ein Argument.",
  "tipp3": "Lies im Buch S. 49 den Text »Die Globalisierung aus der Sicht von Joseph Stiglitz« einmal ganz.",
  "karte": "stiglitz"},
]
PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
assert PFLICHT == [1, 2, 3]
ZUSATZ = [t["nr"] for t in T if t["tag"] == "Zusatz"]
BESPRECHEN = [t["nr"] for t in T if t.get("besprechen")]

GRP = {1: TEILNAME[1] + " (Buch S. 42–47) · " + wann(1),
       2: TEILNAME[2] + " (Buch S. 48–51) · " + wann(2),
       0: "ZUSATZ · nur wer fertig ist · keine Hausübung"}

LERNZIELE = ["Ich kann **drei Ereignisse** nennen, die man als Beginn der Globalisierung ansetzen kann, und mein Kriterium begründen.",
             "Ich kann die wichtigsten **Antriebskräfte** der Globalisierung und den Begriff **Liberalisierung** erklären.",
             "Ich kann die **Rolle der Digitalisierung** bewerten und den **Digital Divide** mit Zahlen belegen."]

LEITFRAGE = "War die Globalisierung Zufall, Überlegenheit oder alternativlos – und wem nützt sie heute?"
HEUTE_ZIEL = {1: "Wann begann die Globalisierung, und welche sechs Kräfte treiben sie an?",
              2: "Digitalisierung bewerten, Zahlen zum Digital Divide lesen, Aussagen zur Globalisierung prüfen."}
WICHTIGSTE = ["Globalisierung heißt: Wirtschaft, Gesellschaft und Kultur sind weltweit immer dichter verflochten.",
              "Einen einzigen Beginn gibt es nicht – je nach Kriterium nennt man 1492, 1844, 1944 oder die 1980er/1990er.",
              "Antriebskräfte sind Informationstechnik, billigerer Transport, Marktwirtschaft, Liberalisierung, transnationale Konzerne und gemeinsame Normen.",
              "Die Digitalisierung verbindet die Welt – aber rund ein Viertel der Menschen ist noch offline (Digital Divide).",
              "Zahlen und Aussagen immer mit Quelle, Jahr und Interessen prüfen – das gilt auch für Zölle und Schlagzeilen."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
 ["Globalisierung", "zunehmende wirtschaftliche, gesellschaftliche und kulturelle weltumspannende Verflechtung; seit den 1960er-Jahren als Schlagwort verbreitet"],
 ["Deglobalisierung", "Phase, in der die Verflechtung zurückgeht, z. B. in der Zwischenkriegszeit"],
 ["Informationsrevolution", "Informationen werden durch neue Technik in kürzester Zeit gewonnen, verarbeitet und verbreitet"],
 ["Liberalisierung", "Abbau von Handelshemmnissen und Öffnung von Märkten für Güter, Dienstleistungen und Kapital"],
 ["Neoliberalismus", "Ausrichtung, die vor allem auf freie Märkte und weniger staatliche Eingriffe setzt"],
 ["Deregulierung / Privatisierung", "weniger staatliche Vorschriften / Übergabe öffentlicher Dienste an private Anbieter"],
 ["transnationales Unternehmen / Global Player", "Unternehmen, das weltweit produziert und verkauft; oft durch Fusionen und Übernahmen gewachsen"],
 ["Outsourcing", "Auslagerung von Produktion oder Diensten an andere Betriebe, oft ins Ausland"],
 ["Just-in-time", "Teile werden genau dann geliefert, wenn die Produktion sie braucht"],
 ["Normen und Standards", "gemeinsame technische Regeln, die den internationalen Handel erleichtern"],
 ["Global Village", "»Weltdorf«: durch Informationstechnik schrumpft die räumliche Distanz"],
 ["Global Governance", "Aufgabe, grenzüberschreitende Probleme gemeinsam zu lösen"],
 ["Big Data", "riesige Mengen strukturierter und unstrukturierter Daten; entscheidend ist ihre Verwendung"],
 ["Digital Divide", "digitale Kluft: ungleicher Zugang zu Internet und Technik zwischen Gruppen"],
 ["Protektionismus / Zoll", "Schutz der eigenen Wirtschaft / Abgabe auf eine Ware beim Grenzübertritt, zuerst vom Importeur bezahlt"],
 ["Prozentpunkte", "Unterschied zwischen zwei Prozentwerten (94 % − 23 % = 71 Prozentpunkte)"]]

WEISST_DU_NOCH = {
    2: [("Nenne zwei Ereignisse, die man als Beginn der Globalisierung ansetzen kann.", "z. B. 1492 Kolumbus · 1844 Telegraf · 1944 IWF und Weltbank · 1980er Technik · Internet."),
        ("Nenne zwei Antriebskräfte der Globalisierung.", "z. B. Informationsrevolution, Transporttechnik, Marktwirtschaft, Liberalisierung, transnationale Konzerne, Normen."),
        ("Was bedeutet Liberalisierung?", "Abbau von Handelshemmnissen, Öffnung der Märkte.")],
}

STOPPFRAGEN = {
    1: [("Gibt es einen einzigen Beginn der Globalisierung?", "Nein – je nach Kriterium nennt man 1492, Mitte des 19. Jahrhunderts, 1944 oder die 1980er/1990er."),
        ("Was bedeutet Liberalisierung?", "Abbau von Handelshemmnissen und Öffnung der Märkte für Güter, Dienstleistungen und Kapital.")],
    2: [("Was heißt Digital Divide?", "Ungleicher Zugang zu Technologie und Internet zwischen Gruppen (Einkommen, Stadt/Land, Geschlecht, Alter)."),
        ("Warum nennt man bei Zahlen immer die Quelle und das Jahr?", "Quellen zählen verschieden und Werte ändern sich; nur so kann man sie prüfen und vergleichen.")],
}

PARTNERKARTEN = [("Nenne drei Ereignisse, die man als Beginn ansetzen kann.", "1492, 1844, 1944, 1980er, Internet."),
                 ("Nenne die sechs Antriebskräfte.", "Informationsrevolution, Transport, Marktwirtschaft, Liberalisierung, transnationale Konzerne, Normen."),
                 ("Was heißt Liberalisierung?", "Abbau von Handelshemmnissen, Öffnung der Märkte."),
                 ("Wie viele Menschen sind laut ITU 2025 offline?", "Rund 2,2 Milliarden."),
                 ("Was bedeutet 94 % zu 23 %?", "Internetnutzung in Ländern mit hohem zu niedrigem Einkommen: 71 Prozentpunkte Unterschied."),
                 ("Wer zahlt einen Zoll zuerst?", "Der Importeur."),
                 ("Was gehört zu einer guten Quellenangabe?", "Wer, Jahr, Messweise, mögliche Interessen.")]

STOLPERSTEINE = [("Einen einzigen Beginn der Globalisierung behaupten", "Je nach Kriterium nennt man 1492, Mitte des 19. Jahrhunderts, 1944 oder die 1980er/1990er. Wichtig ist, dass die Kadetten ein Kriterium begründen."),
                 ("Die China-Marine-These als Tatsache nehmen", "Gesichert: Die staatlichen Flottenfahrten (Zheng He, 1405–1433) endeten. Ob China seine Flotte »zerstörte« und warum, ist eine vereinfachte Deutung (EBSCO Research Starter). Als Quellenkritik-Beispiel nutzen."),
                 ("Zahlen der Quellen vermischen", "Buch (rund 32 % ohne Internet) und ITU (2,2 Mrd. offline, rund ein Viertel) zählen verschieden. Quelle, Jahr und Definition nennen, nicht eine Zahl als »falsch« abtun."),
                 ("Zölle von 2025 als heutigen Stand sagen", "Das Buch zeigt 2025. Seither Urteil des Supreme Court (20.02.2026), Vereinbarungen und Zollpausen (China, 09.11.2026). Immer Datum und Rechtsgrundlage nennen."),
                 ("Statements der Ampel parteipolitisch auflösen", "Die Aussagen sind Diskussionsanlässe. Keine Auflösung »richtig/falsch«, sondern Quelle, Zahl und Gegenargument verlangen.")]

# (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite/Hinweis) – 16 Fragen, Antworten werden beim Anzeigen gemischt
QUIZ = [
 ("Begriff", "Was bezeichnet man allgemein mit »Globalisierung«?", ["Die zunehmende wirtschaftliche, gesellschaftliche und kulturelle weltumspannende Verflechtung.", "Nur den Warenhandel zwischen Staaten.", "Die Gründung der WTO im Jahr 1995.", "Die Abschaffung aller Staatsgrenzen."],
  "Das Buch beschreibt Globalisierung als weltumspannende Verflechtung in Wirtschaft, Gesellschaft und Kultur.", "Buch S. 42–43"),
 ("Beginn", "Wann begann die Globalisierung?", ["Das hängt vom Kriterium ab – genannt werden u. a. 1492, Mitte des 19. Jahrhunderts, 1944 und die 1980er.", "Genau am 12. Oktober 1492.", "Erst mit dem Internet um das Jahr 2000.", "Mit dem Ersten Weltkrieg."],
  "Das Buch nennt mehrere Standpunkte; eine einzige Geburtsstunde gibt es nicht.", "Buch S. 43–44"),
 ("Geschichte", "Was bedeutet »Deglobalisierung« in der Zwischenkriegszeit?", ["Verflechtung und Welthandel gingen zurück.", "Der Welthandel wuchs besonders stark.", "Alle Zölle wurden abgeschafft.", "Das Internet wurde abgeschaltet."],
  "Nach der starken Verflechtung bis zum Ersten Weltkrieg erlebte die Welt eine Phase der Deglobalisierung.", "Buch S. 44"),
 ("Kritik", "Die Aussage »China zerstörte seine Marine, weil die Herrscher Angst vor Freihandel hatten« ist …", ["zugespitzt: gesichert ist nur, dass die staatlichen Flottenfahrten (1405–1433) endeten; Gründe und Folgen sind Deutung.", "ein bewiesener Fakt.", "völlig erfunden.", "nur für Europa gültig."],
  "Quellenkritik: Eine einprägsame Überschrift ist noch kein Beleg. Quelle: EBSCO Research Starter zu den Expeditionen des Zheng He.", "Quellenkritik · PPP-Impuls"),
 ("Antriebskräfte", "Container, Hochgeschwindigkeitszüge und Großraumflugzeuge machen Transporte billiger. Zu welcher Antriebskraft gehört das?", ["Innovationen im Transport", "Informationsrevolution", "Liberalisierung", "Normen und Standards"],
  "Die Kosten für See- und Lufttransport sanken bis Mitte des 20. Jahrhunderts um mehr als zwei Drittel.", "Buch S. 45"),
 ("Antriebskräfte", "Welche Antriebskraft meint den Abbau von Zöllen und die Öffnung der Märkte?", ["Liberalisierung", "Informationsrevolution", "Normen und Standards", "Just-in-time"],
  "Liberalisierung bedeutet Abbau von Handelshemmnissen für Güter, Dienstleistungen und Kapital.", "Buch S. 46"),
 ("Antriebskräfte", "Warum erleichtern internationale Normen und Standards den Welthandel?", ["Waren müssen nicht für jeden Markt neu angepasst werden.", "Normen verbieten Importe.", "Normen ersetzen Zölle.", "Normen gelten nur in Österreich."],
  "Gemeinsame Standards (z. B. Stecker, Spurbreiten) senken Kosten und Hürden.", "Buch S. 46"),
 ("Konzerne", "Was sind Global Player laut Buch?", ["Weltweit tätige Unternehmen, meist durch Fusionen und Übernahmen entstanden.", "Staaten mit Atomwaffen.", "Spitzensportler im Ausland.", "Städte mit großem Hafen."],
  "Global Player agieren und reagieren auf globale Herausforderungen und nutzen Kosten- und Steuervorteile.", "Buch S. 46"),
 ("Digital Divide", "Was bedeutet »Digital Divide«?", ["Ungleicher Zugang zu Technologie und Internet zwischen Gruppen.", "Die Teilung eines Netzwerks in zwei Hälften.", "Ein Gesetz über Datenschutz.", "Das Ende der Digitalisierung."],
  "Die Kluft besteht z. B. zwischen Einkommensgruppen, Stadt und Land und Geschlechtern.", "Buch S. 48"),
 ("Zahlen", "Wie viele Menschen waren laut ITU 2025 noch offline?", ["Rund 2,2 Milliarden.", "Rund 220 Millionen.", "Rund 6 Milliarden.", "Praktisch niemand."],
  "ITU, Facts and Figures 2025 (17.11.2025): rund 6 Mrd. online, 2,2 Mrd. offline.", "ITU 2025 · Aufgabe 3"),
 ("Zahlen", "Wie groß ist laut ITU 2025 der Unterschied bei der Internetnutzung zwischen Ländern mit hohem (94 %) und niedrigem Einkommen (23 %)?", ["71 Prozentpunkte", "117 Prozentpunkte", "23 Prozentpunkte", "4 Prozentpunkte"],
  "94 − 23 = 71 Prozentpunkte.", "ITU 2025 · Aufgabe 3"),
 ("Quellen", "Buch und ITU nennen verschiedene Anteile ohne Internet. Was tust du?", ["Jahr, Messweise und Definition vergleichen und beide Quellen nennen.", "Die niedrigere Zahl nehmen.", "Beide Quellen weglassen.", "Die Zahl nehmen, die besser klingt."],
  "Quellen zählen verschieden; entscheidend sind Quelle, Jahr und Definition.", "Buch S. 48 · Aufgabe 3"),
 ("Zoll", "Wer zahlt einen Einfuhrzoll zunächst?", ["Der Importeur.", "Das Ausland automatisch.", "Immer der Verbraucher.", "Die WTO."],
  "Der Importeur führt den Zoll an die Zollbehörde ab. Die spätere Belastung kann sich auf Marge, Lieferanten und Käufer verteilen.", "Buch S. 50–51"),
 ("Zoll aktuell", "Das Buch nennt US-Zölle von bis zu 145 % (2025). Was gilt für solche Zahlen?", ["Sie gelten für Waren, Länder und Zeiträume und haben sich seither mehrfach geändert – Datum nennen.", "Sie gelten unverändert für immer.", "Sie wurden nie erhoben.", "Sie betreffen nur Österreich."],
  "Seither u. a. Urteil des US Supreme Court (20.02.2026) und Zollpausen; am 09.11.2026 meldete die Berliner Zeitung (nach Xinhua, Reuters, dpa): China setzt einen Zusatzzoll von 24 % auf US-Waren für zwei Monate aus.", "Aktuelle Ergänzung zu Buch S. 50–51"),
 ("Stiglitz", "Welche Kernaussage vertritt Stiglitz laut Buch?", ["Offene Märkte allein lösen die Armut nicht; Bildung und Institutionen sind wichtig.", "Globalisierung ist immer gut.", "Globalisierung ist beendet.", "Zölle sind die beste Lösung."],
  "Er kritisiert Subventionen, Biopiraterie und fordert Investitionen in Bildung.", "Buch S. 49"),
 ("Urteil", "Was macht ein begründetes Urteil aus?", ["Eine Entscheidung mit Beleg, Gegenargument und Bedingung.", "Eine möglichst lange Meinung.", "Eine Aussage, der alle zustimmen.", "Ein Satz ohne Einschränkung."],
  "Auch eine Gegenposition ist akzeptabel – wichtig sind Begründung und gekennzeichnete Unsicherheit.", "Buch S. 49–51"),
]
# Sechs Fragen für den Selbstcheck in Stunde 2 (Nummern der Quizfragen, ab 1)
SELBSTCHECK = [2, 5, 6, 9, 10, 14]
assert len(QUIZ) == 16 and all(len(q[2]) == 4 for q in QUIZ)
