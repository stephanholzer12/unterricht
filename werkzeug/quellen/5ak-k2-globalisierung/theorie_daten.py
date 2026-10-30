"""Theorie-Seite K2 Globalisierung und aktuelle Weltpolitik: Teile und Folien. Dieselben Daten bauen die Theorie-Folien der TH-Lehrer-/TH-Kadetten-PPP
und die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag im Schulbuch).
Alles in eigenen Worten; Grafiken selbst gezeichnet (skizzen.py), keine Buchabbildungen. Lesezeit: ca. 130 Wörter/min (siehe woerter()).
Aktuelle Karten (A–E) tragen Datum und Quelle. Stand der Recherche: 30.10.2026 – vor 13.11., 20.11., 27.11. und 04.12. erneut prüfen."""
import re
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Eine Sportuhr – woher kommt sie?", "pill": "Modellfall",
  "blocks": [("tiles", [("Die Marke", ["Ein österreichischer Anbieter entwickelt und verkauft eine Sportuhr mit KI-Auswertung."]),
                        ("Das Produkt", ["Bauteile, Montage und Datenverarbeitung können ganz woanders stattfinden."])]),
             ("ul", ["Ist eine österreichische Marke automatisch ein österreichisches Produkt? Gib zwei begründete Vermutungen ab.",
                     "Die Uhr ist ein **didaktisches Modell** – keine recherchierte Lieferkette einer echten Marke."]),
             ("hint", "Leitfrage der Einheit: " + I.LEITFRAGE)]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Stunde 1
 ("teil1", I.TEILNAME[1].split(" · ")[0] + " · " + I.wann(1) + " · " + I.TEILBUCH[1], I.TEILNAME[1].split(" · ", 1)[1], [
  {"id": "verbindet", "title": "Was Globalisierung verbindet", "pill": "Buch S. 43–48",
   "blocks": [("ul", ["**Globalisierung** heißt: Wirtschaft, Menschen, Wissen, Kultur und Entscheidungen sind weltweit dicht miteinander verbunden. **Internationalisierung** meint die Ausweitung über die Staatsgrenze hinaus – weniger dicht. Eine überall gültige, starre Grenze zwischen beiden Begriffen gibt es nicht.",
                      "An jedem Produkt kann man vier **Ströme** verfolgen: **Waren** (Bauteile, fertige Produkte), **Geld** (Zahlungen, Investitionen), **Daten** (Messwerte, Auswertungen) und **Wissen** (Entwicklung, Software, Know-how). Auch Menschen und Kultur wandern über Grenzen.",
                      "**Fall Sportuhr (Modell):** Ein österreichischer Anbieter lässt eine Sportuhr aus international beschafften Bauteilen herstellen. Zur Uhr gehört ein KI-Dienst für die Auswertung von Trainingsdaten. Die Orte im Bild sind **gesetzte Annahmen**."]),
              ("img", "img/sportuhr.png", "Modell der Sportuhr: sechs Stationen von Entwicklung in Europa über Halbleiter aus Ostasien, Montage in Südostasien und Rohstoffe aus mehreren Regionen bis zum Rechenzentrum und zum Absatz in Europa und den USA, verbunden durch Pfeile.",
               "Modellfall Sportuhr: Stationen und Orte sind **angenommen**, keine echte Lieferkette."),
              ("merke", "Eine **Marke** sagt nicht, wo Bauteile, Montage und Datenverarbeitung stattfinden."),
              ("hint", "Bei der Beschaffung für Sport, Rettung oder Bundesheer zählen neben dem Preis auch Lieferfähigkeit, Ersatzteile und die Kontrolle sensibler Daten.")]},
  {"id": "entstehung", "title": "Wie die Verflechtung entstand", "pill": "Buch S. 43–46",
   "blocks": [("ul", ["**Ältere Netze:** Handelswege über Land und Meer verbanden Weltregionen schon lange vor der Industrie.",
                      "**Kolonialzeit:** Die Expansion europäischer Mächte baute Handelsnetze auf – oft mit Zwang und Ausbeutung.",
                      "**Industrialisierung und Transport:** Dampfschiff, Eisenbahn, später Container und Flugzeug machten Transporte schneller und billiger. Das Buch zeigt auf S. 43, wie stark die Reisegeschwindigkeiten stiegen.",
                      "**Nach 1945:** IWF und Weltbank (Bretton Woods 1944) sowie das GATT-Abkommen über den Warenhandel (1947/48) schufen Regeln; Zölle wurden schrittweise gesenkt.",
                      "**Digitalisierung:** Das Internet bringt Daten in Sekunden um die Welt und macht auch Dienstleistungen grenzüberschreitend."]),
              ("merke", "Es gibt **keine einzige Geburtsstunde** der Globalisierung – je nach Blickwinkel beginnt sie früher oder später.")]},
  {"id": "warum", "title": "Warum Unternehmen weltweit arbeiten", "pill": "Buch S. 45–47",
   "blocks": [("ul", ["Unternehmen wählen **Standorte** nach **Standortfaktoren**: Kosten, Fachwissen, Infrastruktur, Marktzugang und rechtliche Regeln. Die **Wertschöpfungskette** wird aufgeteilt, weil nicht jede Stufe überall gleich gut möglich ist.",
                      "Antriebskräfte laut Buch (S. 45–46): bessere Informations- und Verkehrstechnik, **Marktwirtschaft und Liberalisierung** (weniger Handelshürden), flexible Produktion (**Just-in-time**: Teile kommen genau dann, wenn man sie braucht), **transnationale Unternehmen** und gemeinsame **Normen**.",
                      "Dazu kommen **Daten**: Ein KI-Dienst kann in einem Rechenzentrum in einem anderen Land laufen als dort, wo die Uhr getragen wird."]),
              ("table", [["Standortfaktor", "Beispiel Sportuhr (Modell)"], ["Kosten", "Montage dort, wo Fertigung günstiger ist"], ["Fachwissen", "Chips von Spezialisten; Software aus Europa"],
                         ["Infrastruktur", "Häfen, Strom und Rechenzentren"], ["Marktzugang", "Absatz in Europa und den USA"], ["Regeln", "Zölle, Datenschutz, Arbeits- und Umweltstandards"]]),
              ("merke", "Weltweite Arbeitsteilung spart Kosten – sie schafft aber auch **Abhängigkeiten**.")]},
  {"id": "stop1a", "title": "Stopp – kannst du das?", "pill": "Buch S. 43–47", "blocks": [("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgabe 1", "aufgaben.html#a1"),
  {"id": "folgen", "title": "Wer gewinnt – und wer trägt die Kosten?", "pill": "Buch S. 48, 64–70",
   "blocks": [("ul", ["Die Folgen sind **ungleich verteilt** – auch innerhalb eines Staates. Beschäftigte, Betriebe, Regionen und Verbraucher sind verschieden betroffen.",
                      "**Chancen:** größere Märkte, Einkommen, Wissenstransfer, effizientere Technik. **Belastungen:** Wettbewerbs- und Lieferdruck, niedrige Löhne und schlechte Arbeitsbedingungen, Rohstoffverbrauch und Abfall.",
                      "**Menschen:** Fachkräfte und Pflegekräfte wandern ab (Fachkräfteabwanderung). Für die Person kann das ein Gewinn sein, dem Herkunftsland fehlen sie dann. Rücküberweisungen und Rückkehr mildern das teilweise.",
                      "**Digitale Kluft:** Wer keinen Zugang zu Internet und Technik hat, nutzt die Chancen kaum. Das Buch nennt dazu auf S. 48 den Anteil der Weltbevölkerung ohne Internet.",
                      "Umweltfolgen lassen sich nicht allein aus **Transportkilometern** ablesen – Herstellung, Energie und Lebensdauer zählen mit."]),
              ("merke", "Frage nie nur »Ist Globalisierung gut?«, sondern: **Für wen, unter welchen Regeln?**")]},
  {"id": "stop1b", "title": "Stopp – kannst du das?", "pill": "Buch S. 64–70", "blocks": [("reveal", I.STOPPFRAGEN[1][1:])]},
  ("jetzt", "Jetzt: Aufgabe 2", "aufgaben.html#a2"),
 ]),

 # ---------------------------------------------------------------- Stunde 2
 ("teil2", I.TEILNAME[2].split(" · ")[0] + " · " + I.wann(2) + " · nach dem Test · " + I.TEILBUCH[2], I.TEILNAME[2].split(" · ", 1)[1], [
  {"id": "zoelle", "title": "Zölle: Wer zahlt – und wer trägt die Last?", "pill": "Buch S. 50–51 · Karte A",
   "blocks": [("ul", ["Ein **Zoll** ist eine Abgabe auf eine Ware beim Grenzübertritt. Er wird nach dem **Zollwert** der Ware und einem **Zollsatz** berechnet. Rechtlich muss ihn der **Importeur** an die Zollbehörde des Einfuhrlandes abführen.",
                      "Die **wirtschaftliche Last** kann woanders liegen: Der Importeur kann seine Marge senken, den Preis erhöhen oder einen Nachlass vom Lieferanten verlangen. Wie sich das verteilt, hängt von Nachfrage, Verträgen, Wechselkurs und Wettbewerb ab.",
                      "Trump-Zölle sind ein **datierter Fall**: Das Buch beschreibt den Stand von 2025. Seither hat sich die Rechtslage geändert (Karte A)."]),
              ("tiles", [("Karte A · Zölle (Stand 30.10.2026)", [
                  "Der **US Supreme Court** erklärte am 20.02.2026 die auf IEEPA gestützten Zölle für rechtswidrig. Rückerstattungen laufen nicht automatisch. Zölle nach **Section 232** (z. B. Stahl, Aluminium) und **Section 301** gelten weiter; in Details unterscheiden sich die Quellen (WKO, IHK) – vor dem Unterricht neu prüfen.",
                  "Für die EU nennt die EU-Kommission im Handelsrahmen mit den USA eine **Obergrenze von 15 %** für die meisten EU-Ausfuhren, mit Ausnahmen und Sonderregeln, etwa bei Metallen. Das ist kein einheitlicher Zoll auf alle Einfuhren.",
                  "Die US-Regierung will heimische Produktion, wirtschaftliche Sicherheit und Verhandlungsmacht stärken. Betroffene Firmen und Verbraucher sehen Preisrisiken, Unsicherheit und Gegenmaßnahmen. Ob ein Zoll Arbeitsplätze sichert, hängt von Vorleistungen, Wechselkursen, Nachfrage und Reaktionen anderer Staaten ab."])]),
              ("hint", "Der US-KI-Aktionsplan (23.07.2025) setzt auf Innovation und Infrastruktur auch mit Partnern. »Gegen jede Globalisierung« beschreibt die US-Politik daher nicht – eher Schutz plus ausgewählte Abhängigkeiten. Das ist eine Schlussfolgerung, kein Zitat.")]},
  {"id": "stop2a", "title": "Stopp – kannst du das?", "pill": "Buch S. 50–51", "blocks": [("reveal", I.STOPPFRAGEN[2][:1])]},
  ("jetzt", "Jetzt: Aufgabe 3", "aufgaben.html#a3"),
  {"id": "institutionen", "title": "Wer organisiert Regeln und Finanzierung?", "pill": "Buch S. 52–63 · Karte B",
   "blocks": [("ul", ["**WTO** (seit 1995, Nachfolgerin des GATT-Systems von 1947/48): Regeln und Verhandlungen für den Handel, dazu ein Streitverfahren. **GATT** = Waren, **GATS** = Dienstleistungen, **TRIPS** = Rechte an geistigem Eigentum. Mitglieder entscheiden im Konsens; die WTO ist keine Weltregierung und keine UN-Sonderorganisation. Die Berufungsinstanz im Streitverfahren ist derzeit blockiert.",
                      "**IWF** (Bretton Woods 1944): wacht über die Stabilität des Währungssystems, berät und gibt Ländern mit Zahlungsbilanzproblemen Kredite, oft mit Auflagen. Stimmrechte folgen dem Kapitalanteil.",
                      "**Weltbank** (ebenfalls Bretton Woods): finanziert Entwicklung und berät – mit vergünstigten Krediten und, je nach Instrument, Zuschüssen. Projektauswahl, Schulden und soziale sowie ökologische Folgen werden kritisch diskutiert.",
                      "Weitere Akteure: die **OECD** erarbeitet Daten, Analysen und Standards; **Unternehmen** organisieren Produktion und Datenverarbeitung; **NGOs** bringen Anliegen ein. Entscheidungen beruhen auf Mitgliedern und Machtverhältnissen – nicht auf den Wünschen einer Person."]),
              ("table", [["Funktion (Karte B, Stand 30.10.2026)", "Person"], ["IWF", "Kristalina Georgieva (seit 01.10.2019, zweite Amtszeit seit 01.10.2024)"],
                         ["Weltbankgruppe", "Ajay Banga (seit 02.06.2023)"], ["WTO", "Ngozi Okonjo-Iweala (zweite Amtszeit seit 01.09.2025)"], ["Christine Lagarde", "IWF 2011–2019, derzeit EZB-Präsidentin (Abgang für Februar 2027 gemeldet)"]]),
              ("hint", "Die Aufgaben sind wichtiger als die Namen. Meldungen über Wechsel in Spitzenämtern immer mit Datum und Primärquelle prüfen.")]},
  {"id": "stop2b", "title": "Stopp – kannst du das?", "pill": "Buch S. 52–63", "blocks": [("reveal", I.STOPPFRAGEN[2][1:])]},
  ("jetzt", "Jetzt: Aufgabe 4", "aufgaben.html#a4"),
 ]),

 # ---------------------------------------------------------------- Stunde 3
 ("teil3", I.TEILNAME[3].split(" · ")[0] + " · " + I.wann(3) + " · " + I.TEILBUCH[3], I.TEILNAME[3].split(" · ", 1)[1], [
  {"id": "ki_global", "title": "KI braucht Daten, Chips, Strom und Regeln", "pill": "Ergänzung zu Buch S. 48 · Karten C und E",
   "blocks": [("ul", ["KI ist selbst ein globales Produkt: **Daten**, **Chips** (Halbleiter aus wenigen Regionen), **Strom**, **Rechenzentren**, Fachleute und **Regeln** kommen aus verschiedenen Ländern. Wer davon abhängt, ist verwundbar.",
                      "**Arbeit (Karte E):** Laut ILO (2025) arbeitet etwa jeder vierte Beschäftigte weltweit in einem Beruf, auf den generative KI einen gewissen Einfluss haben könnte. Das misst **betroffene Tätigkeiten**, nicht verlorene Arbeitsplätze; Veränderung ist wahrscheinlicher als vollständiger Ersatz.",
                      "**Energie (Karte E):** Nach der IEA brauchten Rechenzentren 2024 rund 415 TWh Strom (etwa 1,5 % des weltweiten Verbrauchs); für 2030 ist rund 945 TWh eine **Projektion**. TWh = Terawattstunde. »Alle Rechenzentren« ist nicht gleich »nur KI«.",
                      "**EU-Regeln (Karte C):** Die KI-Verordnung arbeitet nach **Risiko** und Einsatzbereich: **Verbote** (z. B. bestimmte soziale Bewertung), **Hochrisiko** (z. B. Bewerberauswahl) und **Transparenzpflichten** (z. B. Chatbot, KI-erzeugte Inhalte). Sie ist **kein** KI-Verbot. Rein militärische, Verteidigungs- und nationale Sicherheitszwecke sind in Artikel 2 gesondert ausgenommen – das ist kein rechtsfreier Raum.",
                      "**USA:** Der KI-Aktionsplan (23.07.2025) setzt auf Innovation, Infrastruktur und internationale Führung. Datenschutz und Urheberrecht sind eigene Rechtsgebiete."]),
              ("table", [["Zeitpunkt (Karte C)", "Einordnung"], ["01.08.2024", "Verordnung in Kraft"], ["02.02.2025", "erste Verbote, KI-Kompetenzpflicht"], ["02.08.2025", "Regeln für KI-Modelle mit allgemeinem Zweck"],
                         ["27.07.2026", "Änderung »AI Omnibus« in Kraft"], ["02.08.2026", "u. a. Transparenzregeln anwendbar"], ["02.12.2027", "Hochrisiko nach Anhang III (z. B. Beschäftigung)"], ["02.08.2028", "Hochrisiko bei Produkten (Anhang I)"]]),
              ("hint", "Für ältere Systeme gilt eine Übergangsfrist für die technische Kennzeichnung bis 02.12.2026. Fristen sind Stand 30.10.2026 – nicht die Grafik von 2024 verwenden.")]},
  {"id": "stop3a", "title": "Stopp – kannst du das?", "pill": "Karten C bis E", "blocks": [("reveal", I.STOPPFRAGEN[3][:1])]},
  ("jetzt", "Jetzt: Aufgabe 5", "aufgaben.html#a5"),
  {"id": "ki_risiko", "title": "KI-Risiken prüfen", "pill": "Ergänzung zu Buch S. 48 · Karte D",
   "blocks": [("ul", ["»Übernimmt KI die Macht?« sind vier verschiedene Fragen. **Arbeit:** Welche Tätigkeiten werden automatisiert oder unterstützt? **Macht:** Wer kontrolliert Rechenleistung, Daten und Plattformen? **Abhängigkeit:** Wer verliert Fähigkeiten, wenn er sich auf Systeme verlässt? **Kontrollverlust:** Könnten künftige Systeme menschliche Aufsicht wirksam umgehen?",
                      "Eine Aufgabe zu automatisieren ist nicht dasselbe, wie politische Herrschaft auszuüben.",
                      "Unterscheide beim Prüfen: **Befund** (gemessen), **Simulation** (Versuch unter festgelegten Bedingungen), **Szenario** (durchgespielte Zukunft) und **Motive** (aus Schlagzeilen nicht ablesbar)."]),
              ("img", "img/vier_fragen.png", "Vier Felder: Arbeit, Macht, Abhängigkeit und Kontrollverlust, jeweils mit einer Leitfrage.", "Die vier Bedeutungen von »Übernahme« – nicht ineinander rutschen lassen."),
              ("merke", "Eine Warnung kann **fachlich begründet** sein und zugleich die **öffentliche Wahrnehmung** eines Unternehmens beeinflussen. Interessen sind eine prüfbare Hypothese, kein Beweis.")]},
  {"id": "quellenkarten", "title": "Quellenkarten A–D für Aufgabe 6", "pill": "Karten A bis D",
   "blocks": [("tiles", [("Karte A · Warnstatement (30.05.2023)", ["Das CAIS-Statement fordert, das Risiko eines Aussterbens durch KI global ernst zu nehmen – neben anderen Großrisiken. Unterzeichnet haben es Forscher und Leiter von KI-Unternehmen.", "**Prüfauftrag:** Was wird gefordert? Welche Messung oder Wahrscheinlichkeit liefert das Statement selbst?"]),
                        ("Karte B · International AI Safety Report (03.02.2026)", ["Der Bericht (Vorsitz Yoshua Bengio, über 100 Fachleute) bündelt den Forschungsstand. Er unterscheidet heutige **Fehlfunktionen** von einem hypothetischen **umfassenden Kontrollverlust**. Erste relevante Fähigkeiten zeigen sich in Tests, nicht aber auf dem nötigen Gesamtniveau; Fachleute bewerten Wahrscheinlichkeit und Folgen verschieden.", "**Prüfauftrag:** Welche Unsicherheit bleibt? Was unterscheidet Fehlfunktion und Kontrollverlust?"]),
                        ("Karte C · Forschungsfallstudien (Sommer 2026)", ["Eine Studie testet autonome KI-Modelle in gezielt gestalteten, ausgedachten Szenarien und berichtet problematisches Verhalten, etwa verdeckte Änderungen. Die Autoren nennen selbst Einschränkungen; pro Modell gab es nur wenige Durchläufe. Der Text stammt von einem KI-Unternehmen (Interessenkonflikt!), die Methode ist trotzdem prüfbar.", "**Prüfauftrag:** Unter welchen künstlichen Bedingungen wurde beobachtet? Wie weit reicht der Befund?"]),
                        ("Karte D · US-KI-Aktionsplan (23.07.2025)", ["Ein Regierungsprogramm der USA mit erklärten Zielen: Innovation beschleunigen, Infrastruktur aufbauen, international führen.", "**Prüfauftrag:** Welche Ziele und Interessen werden genannt? Sind sie schon nachgewiesene Ergebnisse?"])]),
              ("hint", "In die gemeinsame Tabelle: Aussage – Art der Quelle – Beleg – mögliche Interessen – Grenze. Pro Karte höchstens 45 Sekunden Bericht. Kein eigenes KI-Konto nötig.")]},
  {"id": "stop3b", "title": "Stopp – kannst du das?", "pill": "Karte D", "blocks": [("reveal", I.STOPPFRAGEN[3][1:])]},
  ("jetzt", "Jetzt: Aufgaben 6 und 7", "aufgaben.html#a6"),
 ]),

 # ---------------------------------------------------------------- Stunde 4
 ("teil4", I.TEILNAME[4].split(" · ")[0] + " · " + I.wann(4) + " · " + I.TEILBUCH[4], I.TEILNAME[4].split(" · ", 1)[1], [
  {"id": "gestalten", "title": "Kosten verteilen und Abhängigkeiten verringern", "pill": "Buch S. 65–77",
   "blocks": [("ul", ["**Unternehmen** können Abhängigkeiten senken: mehrere Bezugsquellen, Lagerbestände, überprüfbare Sozialstandards, reparierbare Produkte und Wechselmöglichkeiten beim Dienstanbieter. Das kostet Geld und Zeit.",
                      "**Politik** setzt Regeln: Mindeststandards, Transparenz in Lieferketten, internationale Abkommen. Grenzen: unterschiedliche Interessen der Staaten, schwierige Kontrolle.",
                      "**Arbeitnehmervertretungen** (Gewerkschaften) bringen Beschäftigteninteressen ein; **Einzelne** entscheiden über Kauf, Nutzung und Daten.",
                      "Das Buch stellt auf S. 72–77 Alternativen und Reformideen vor, z. B. eine **öko-soziale Marktwirtschaft**, die **Ziele für nachhaltige Entwicklung** (SDGs) und zivilgesellschaftliche Bewegungen wie Attac. Sie haben Möglichkeiten und Grenzen – keine ist ein Allheilmittel.",
                      "**Standortverlagerung allein** garantiert weder faire Arbeit noch geringere Umweltfolgen. Mehrere Maßnahmen lassen sich kombinieren."]),
              ("table", [["Diskussionsrunde (Aufgabe 8)", "So läuft sie"], ["Perspektiven", "Unternehmensleitung · Beschäftigte und Zulieferregion · Nutzer und öffentliche Beschaffung · Umwelt- und Verbraucherschutz"],
                         ["Ablauf", "je 1 min Ausgangsposition, dann moderierte Rückfragen, Beobachter notieren"], ["Regeln", "Argumente auf Menschenwürde, Demokratie und überprüfbare Tatsachen beziehen; niemand muss die eigene Haltung spielen"]]),
              ("merke", "Ein **begründetes Urteil** hat: Entscheidung · Beleg · Gegenargument · Bedingung · gekennzeichnete Unsicherheit (»Wenn …, dann könnte …; offen bleibt …«).")]},
  {"id": "stop4", "title": "Stopp – kannst du das?", "pill": "Buch S. 65–77", "blocks": [("reveal", I.STOPPFRAGEN[4])]},
  ("jetzt", "Jetzt: Aufgabe 8", "aufgaben.html#a8"),
 ]),
]

SCHNELLE = [
 {"id": "opt1", "title": "OPTIONAL: Echte Sportuhr prüfen", "pill": "Vertiefung",
  "blocks": [("ul", ["Prüfe eine reale Sportuhr oder ein Smartphone anhand der Herstellerunterlagen: Welche Lieferketteninformationen sind belegt? **Lücken ausdrücklich stehen lassen.**",
                     "Kein Pflichtstoff, keine Hausübung."])]},
 {"id": "opt2", "title": "OPTIONAL: Science oder Fiction?", "pill": "Vertiefung",
  "blocks": [("ul", ["Eine Serie zeigt, wie ein Bordcomputer die Kontrolle über ein Raumschiff übernimmt. Ordne die Szene den **vier Bedeutungen von Übernahme** zu (Arbeit, Macht, Abhängigkeit, Kontrollverlust). Es genügt, die Szene zu beschreiben – kein Vorwissen nötig."])]},
 {"id": "opt3", "title": "OPTIONAL: Pflegekräfte-Abwanderung", "pill": "Vertiefung",
  "blocks": [("ul", ["Stelle die Interessen von Pflegekraft, Herkunftsregion und Aufnahmeland gegenüber. Berücksichtige Rücküberweisungen und Rückkehr."])]},
 {"id": "opt4", "title": "OPTIONAL: Rechenzentren als Grafik", "pill": "Vertiefung",
  "blocks": [("ul", ["Stelle den IEA-Wert für 2024 (rund 415 TWh) und die Projektion für 2030 (rund 945 TWh) als eigene Grafik dar. **Beobachtung und Projektion** sichtbar trennen; keine Zwischenwerte als Messdaten erfinden."])]},
 {"id": "opt5", "title": "OPTIONAL: Hilfen und Hürden für kleine Firmen", "pill": "Vertiefung",
  "blocks": [("ul", ["Welche KI-Regeln helfen kleineren Unternehmen, welche Kosten könnten neue Eintrittshürden schaffen? Suche erst **konkrete Belege**; urteile nicht allein aus einer Vermutung über Motive."])]},
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Stunde 1 · Sportuhr", "teil2": "Stunde 2 · Zölle", "teil3": "Stunde 3 · KI", "teil4": "Stunde 4 · Gestalten",
          "begriffe": "Fachbegriffe", "kurz": "Kurz & knapp", "schnelle": "Optional"}


def _text(b):
    k = b[0]
    if k in ("ul", "ol"): return " ".join(b[1])
    if k == "table": return " ".join(" ".join(r) for r in b[1])
    if k == "tiles": return " ".join(h + " " + " ".join(x if isinstance(x, str) else " ".join(x) for x in (bl if isinstance(bl, list) else [bl])) for h, bl in b[1])
    if k in ("merke", "hint", "buch"): return b[1]
    if k == "img": return b[3]
    return ""


def woerter(ids):
    """Wortzahl der genannten Abschnitte (Lesezeit-Prüfung in plan.py)."""
    allei = {it["id"]: it for p in PARTS for it in p[3] if isinstance(it, dict)}
    n = 0
    for i in ids:
        for b in allei[i]["blocks"]: n += len(re.sub(r"\*\*", "", _text(b)).split())
    return n


if __name__ == "__main__":
    for ids in (["verbindet", "entstehung", "warum"], ["folgen"], ["zoelle"], ["institutionen"], ["ki_global"], ["ki_risiko"], ["gestalten"], ["quellenkarten"]):
        w = woerter(ids); print(ids, w, "Wörter ≈", round(w / 130, 1), "min")
