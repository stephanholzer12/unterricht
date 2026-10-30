"""Fachwissen für die Lehrkraft (nur für Stephan): Lehrer-Infos der PPP und Lösungsmappe K2 Globalisierung und aktuelle Weltpolitik (5AK IWK).
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Lösungsmappe). Grundlage: ChatGPT-Übergabe v1, nachgeprüft (Stand 30.10.2026)."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v14: E3 + E4 + E5 zu einer Einheit zusammengefasst (Stephan, 30.10.2026), Block B Globalisierung (E5 steht im Plan in Block C Akteure → »bitte abgleichen« ist gewollt). Buch S. 41–77. "
                  "Vier Stunden: Fr 13.11., Fr 20.11. (zuerst 20 min angekündigter Test), Fr 27.11., Fr 04.12.; Annahme 50 min."),
    ("Kompetenzen laut Plan: ", "K03, K04, K05 · N01, N03 · P2, P3, P4, P6, P7 · SDG 8, 10, 17 · GLV 1 und 5, ergänzend GLV 2 und 6 (KI). Die Wortlaute stehen im Jahresplan IWK_Jahresplan_5Jg_v14 – dort die Lehraufgaben der E3–E5 gegenprüfen; ich habe sie hier nicht neu formuliert."),
    ("Zuordnung: ", "Aufgabe 1–2 (Verflechtung, Folgen: E3) · Aufgabe 3–4 (Zölle, WTO/IWF/Weltbank: E4/E5) · Aufgabe 5–7 (KI-Regeln, Quellenprüfung: GLV 2/6, N01/N03) · Aufgabe 8 (Gestalten und Urteilen: SDG 8/10/17, P-Kompetenzen)."),
    ("Abweichungen: ", "Kein Versuch, kein CLIL, kein Kahoot, keine Referate, keine Hausübung. Testnummer und Teststoff am 20.11. sind unbekannt – es wurde nichts ergänzt. Sicherheitspolitischer Bezug sparsam (Beschaffung, Lieferfähigkeit, Artikel 2 der KI-Verordnung)."),
]

THEMEN = {1: "Sportuhr, Verflechtung, Folgen (S. 43–48, 64–70)", 2: "Zölle, WTO, IWF, Weltbank (S. 50–63)", 3: "KI: Regeln, Risiken, Quellen (Ergänzung zu S. 48)", 4: "Gestalten und urteilen (S. 65–77)"}


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, _ = PL.aufgaben_der(st)
        z = f"Lesen {PL.minuten(st, ['lesen'])} · Erklären {PL.minuten(st, ['erkl'])} · Aufgaben {PL.minuten(st, ['a'])} · Bespr. {PL.minuten(st, ['bespr'])} · Reserve {PL.minuten(st, ['reserve'])}"
        if PL.minuten(st, ["test"]): z = f"Test {PL.minuten(st, ['test'])} · " + z
        rows.append([f"{st['std']} · {st['datum']}", THEMEN[st["std"]], "– (kein Versuch)", PL.bereich(nrs), z, st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "Beamer mit TH-Unterricht · Tafel · Papier für das Flussbild (A4, Stifte) · Karten mit den Orten der Sportuhr nicht nötig (Bild im Theorieteil)",
            2: "Test (bestehend, Stoff unbekannt) · Taschenrechner nicht nötig · Dreiergruppen für Aufgabe 4 · Karte B (Namen) vorher prüfen",
            3: "Vier Quellenkarten (im Theorieteil, Abschnitt »Quellenkarten«; bei Bedarf ausdrucken) · Tafel für die vier Bedeutungen von »Übernahme« · Papier für die Sicherung",
            4: "Platz für vier Perspektivgruppen · Papier und Stifte für 8c · Moderator bestimmen · LMS-Abgabeordner · Selbstcheck-Quiz (6 Fragen: Nr. " + ", ".join(map(str, I.SELBSTCHECK)) + ")"}


def _karten():
    out = []
    k = I.KLASSEN[0]
    for st in PL.PLAN[k]:
        t, schritte = 0, []
        for name, m, oh, art in st["phasen"]:
            schritte.append(f"Min {t}–{t + m}: {name}" + (" (ohne Handy)" if oh else "")); t += m
        schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
        ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org", "test")))
        out.append((f"5AK · Stunde {st['std']} · {st['datum']} · {THEMEN[st['std']]}", schritte, MATERIAL[st["std"]], ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Einheit einblenden vor der ersten Stunde (Fr 13.11.): GitHub → Actions → »Einheit ein-/ausblenden« → 5ak-iwk/k2-globalisierung → einblenden. Die Direktlinks und QR-Codes funktionieren auch versteckt.",
    "Aktualitätskarten A–E vor jedem Termin neu prüfen (13.11., 20.11., 27.11., 04.12.): Zölle (Karte A), Namen in Spitzenämtern (Karte B), KI-Fristen (Karte C), KI-Risiko-Quellen (Karten D, E).",
    "Stunde 2: Test hat Vorrang (20 min). Stoff und Nummer kenne ich nicht – nichts ergänzt. Dreiergruppen für Aufgabe 4 einteilen.",
    "Stunde 3: Quellenkarten A–D auf Papier mitnehmen (oder die Seite am Beamer). Karte C stammt von Anthropic, dem Hersteller von Claude – Interessenkonflikt offen ansprechen (gehört zur Aufgabe).",
    "Stunde 4: Perspektiven (vier Gruppen) und Moderator vorab festlegen; Diskussion ohne Handy; Urteil 8c mit der Hand. LMS-Abgabeordner anlegen (eine PDF mit den Aufgaben 1–8).",
    "Medien: Es gibt keine Pflichtvideos. Optionale Podcast-Kandidaten (Ö1) habe ich nicht geprüft – nur freigeben, wenn du sie vorher hörst.",
]

AUF_EINEN_BLICK = [
    ["Stunde 1 · Sportuhr", "Globalisierung = dichte weltweite Verflechtung; vier Ströme (Waren, Geld, Daten, Wissen) · Marke ≠ Herkunft · Standortfaktoren · Folgen ungleich verteilt, »für wen, unter welchen Regeln?«", "Flussbild auf Papier"],
    ["Stunde 2 · Zölle und Institutionen", "Zoll: rechtlicher Zahler = Importeur, wirtschaftliche Last verteilt sich · Rechenmodell 100 × 15 % = 15; 115 · WTO Regeln/Streit, IWF Stabilität/Zahlungsprobleme, Weltbank Entwicklung", "Dreiergruppen"],
    ["Stunde 3 · KI", "Vier Bedeutungen von »Übernahme« · EU-KI-Verordnung risikobasiert · ILO: betroffene Tätigkeiten ≠ Arbeitsplatzverlust · IEA: 2024 gemessen, 2030 Projektion · Befund, Simulation, Szenario, Position", "Quellenkarten"],
    ["Stunde 4 · Gestalten", "Maßnahmen und Grenzen (Unternehmen, Politik, Arbeitnehmervertretung, Einzelne) · begründetes Urteil mit Beleg, Gegenargument, Bedingung, Unsicherheit · Brücke zur »Macht des Westens«", "Diskussion ohne Handy"],
]

KAPITEL = [
 {"titel": "1 Globalisierung als Begriff (Buch S. 43–48)",
  "text": ["Es gibt keine einheitliche Definition und keine einzelne Geburtsstunde. Das Buch zählt Antriebskräfte auf (Informationsrevolution, Transport, Marktwirtschaft und Liberalisierung, Postfordismus und Just-in-time, transnationale Konzerne, Normen). Digital Divide: Das Buch nennt für 2025 etwa 32 % der Weltbevölkerung ohne Internet (S. 48) – Datum und Quelle bei Bedarf prüfen.",
           "Didaktisch zählt der Fall Sportuhr: Er ist ein **Modell** (Orte gesetzt). Vor Kadetten nie behaupten, eine reale Marke produziere so."],
  "nur": ["Buchfehler S. 43: »GATT 1995 von GATS abgelöst« ist falsch. Richtig: WTO seit 01.01.1995 als Nachfolgerin des GATT-Systems; GATS regelt Dienstleistungen."],
  "stolper": "Marke = Herkunft; Globalisierung = nur Handel; Umweltwirkung nur aus Transportkilometern ablesen."},
 {"titel": "2 Zölle (Buch S. 50–51) und die Rechtslage 2026",
  "text": ["Rechtlicher Zahler: der Importeur; wirtschaftliche Last: Marge, Preis, Lieferant. Das Buch zeigt den Stand 2025 (u. a. iPhone-Beispiel mit 145 % Zoll, S. 50–51). **Seither hat sich die Rechtslage geändert:** Der US Supreme Court erklärte am 20.02.2026 (6:3) die auf IEEPA gestützten Zölle für rechtswidrig (WKO, Seite vom 23.10.2026). Sie wurden ab 24.02.2026 nicht mehr erhoben; Rückerstattungen laufen über die US-Zollbehörde (CBP-Verfahren »CAPE«) und nicht automatisch.",
           "Weiter gelten Zölle nach Section 232 (z. B. Stahl, Aluminium) und Section 301. Ein befristeter Zusatzzoll nach Section 122 (10 %) lief am 24.07.2026 ab. Laut IHK Chemnitz (Stand 21.08.2026) gelten seither Section-301-Zölle; WKO und IHK weichen in Details voneinander ab – deshalb ist Karte A bewusst vorsichtig formuliert.",
           "EU-US-Handelsrahmen: laut IHK seit 01.07.2026 in Kraft (EU-Verordnung 2026/1455, von mir nicht im Volltext geprüft); die EU-Kommission nennt eine US-Zollobergrenze von 15 % für die meisten EU-Ausfuhren. Ausnahmen und Metalle gesondert."],
  "nur": ["Das Handover beschreibt nur den 15-%-Rahmen und enthält die Gerichtsentscheidung nicht – ohne diese Korrektur wäre Karte A veraltet. Vor 20.11. neu prüfen (Primärquellen von hier aus teilweise nicht abrufbar)."],
  "stolper": "Zollzahlen ohne Datum, Warengruppe und Rechtsgrundlage nennen; »das Ausland zahlt« oder »der Verbraucher zahlt genau 15 %«."},
 {"titel": "3 WTO, IWF, Weltbank (Buch S. 52–63)",
  "text": ["**WTO:** seit 01.01.1995; GATT (Waren), GATS (Dienstleistungen), TRIPS (geistiges Eigentum); drei Grundprinzipien laut Buch; Entscheidungen im Konsens; Streitbeilegungsorgan; die Berufungsinstanz ist seit Jahren blockiert, einige Mitglieder nutzen die Ersatzlösung MPIA (zuletzt rund 61 Mitglieder). Die 14. Ministerkonferenz (Jaunde, 26.–30.03.2026) endete ohne Abschlusserklärung; das E-Commerce-Moratorium lief aus.",
           "**IWF:** Bretton Woods 1944, 27.12.1945 gegründet; Überwachung, technische Hilfe, Kredite mit Bedingungen (frühere Strukturanpassungsprogramme sind der Kern der Kritik); Stimmrechte nach Quoten (Diagramm Buch S. 62 nicht aktuell – keine Prozentwerte verwenden). **Weltbank:** IBRD, IDA, IFC, MIGA, ICSID; Entwicklungsfinanzierung; Kritik an Großprojekten (Beispiel Inga-Damm im Buch).",
           "**Namen (Stand 30.10.2026):** IWF Georgieva (seit 01.10.2019, 2. Amtszeit seit 01.10.2024), Weltbank Banga (seit 02.06.2023), WTO Okonjo-Iweala (2. Amtszeit seit 01.09.2025), Lagarde war 2011–2019 IWF-Chefin und ist EZB-Präsidentin."],
  "nur": ["**Lagarde-Meldung (Handover: Abschied am 29.10.2026, Amtswechsel 07.02.2027):** gemeldet, aber Primärquelle (Europäischer Rat/EZB) nicht geprüft; Reuters/Börsen-Zeitung (Stand 29.10.2026) berichten über den vorzeitigen Abgang zum 07.02.2027 und eine mögliche WEF-Wahl am 02.11. Vor dem Termin neu prüfen. [Rest der alten Notiz:] (nur ältere Meldungen über einen möglichen früheren Abgang). Deshalb steht in Kadettenmaterial kein Datum dazu; das Quiz verlangt nur »Georgieva leitet den IWF«.",
           "Buchunklarheiten: S. 53 ordnet die WTO »im Gefüge der UN« ein – sie ist keine UN-Sonderorganisation (WTO-Seite »WTO und UNO«). Mitglieder: S. 53 nennt 166, S. 54 nennt 164 – im Material keine Zahl verwenden. IWF als »Entwicklungshilfe« (S. 53) ist ungenau – Hauptaufgabe: Stabilität und Zahlungsprobleme."],
  "stolper": "WTO, IWF und Weltbank auf dieselbe Aufgabe reduzieren; Entscheidungen auf Einzelpersonen zurückführen."},
 {"titel": "4 KI-Regeln (EU) und US-Politik",
  "text": ["Risikobasiert: Verbote (Art. 5, z. B. soziale Bewertung unter den gesetzlichen Bedingungen), Hochrisiko (Anhang III, z. B. Beschäftigung/Bewerberauswahl), Transparenz (Art. 50: Chatbots, KI-erzeugte Inhalte). **AI Omnibus** (Amtsblatt 24.07.2026, in Kraft 27.07.2026, Quelle: Lewis Silkin und EU-Seiten): Anhang-III-Hochrisiko-Pflichten ab 02.12.2027, Anhang-I-Produkte ab 02.08.2028; Transparenzregeln ab 02.08.2026; Übergangsfrist für die Kennzeichnung bestimmter älterer Systeme bis 02.12.2026.",
           "Artikel 2: ausschließlich militärische, Verteidigungs- oder nationale Sicherheitszwecke sind ausgenommen – kein pauschaler Freibrief für jede Nutzung durch das Bundesheer; Zweck und Anwendung entscheiden. Training, Urheberrecht und Datenschutz bleiben eigene Rechtsgebiete.",
           "US-KI-Aktionsplan (23.07.2025): drei Säulen – Innovation beschleunigen, Infrastruktur aufbauen, international führen (Diplomatie und Sicherheit)."],
  "nur": ["**Nicht übernommen:** Das Handover nennt »02.12.2026: neue Verbote für nicht einvernehmliche intime KI-Inhalte« – ein einziger Treffer (complexdiscovery.com) nennt es, die Verordnung selbst war nicht abrufbar; deshalb weggelassen. Vor dem Termin in EUR-Lex prüfen. Die Verordnungsnummer 2026/1744 aus dem Handover habe ich nicht im Volltext verglichen.",
           "Beim Termin 04.12. ist der 02.12.2026 bereits vorbei: Hinweis im Rückblick (»Übergangsfrist Kennzeichnung ältere Systeme ist abgelaufen – genaue Anwendung nicht Prüfungsstoff«)."],
  "stolper": "»EU verbietet KI« und »USA haben keine Regeln«; Verbot, Hochrisiko und Transparenzpflicht gleichsetzen."},
 {"titel": "5 KI-Risiken, Arbeit und Energie (Karten D und E)",
  "text": ["**ILO (20.05.2025):** etwa jeder vierte Beschäftigte in einem Beruf mit gewissem möglichem Einfluss generativer KI; misst Tätigkeiten, nicht Stellen. **IEA:** Rechenzentren rund 415 TWh (2024, etwa 1,5 % des weltweiten Stroms), Projektion rund 945 TWh für 2030 (»Energy and AI«, 04/2025). Das Handover nennt 485 TWh (2025) und 950 TWh aus einem Bericht vom 16.04.2026 – das konnte ich nicht bestätigen (Seite nicht abrufbar); verwendet sind nur die bestätigten Werte.",
           "**International AI Safety Report 2026** (03.02.2026, Vorsitz Yoshua Bengio, über 100 Fachleute): unterscheidet Fehlfunktionen von hypothetischem umfassendem Kontrollverlust; erste relevante Fähigkeiten in Tests, aber nicht auf dem nötigen Gesamtniveau; Bewertungslücke. **CAIS-Statement** 30.05.2023: Position, kein Experiment. **Karte C:** »Agentic Misalignment in Summer 2026« (Alignment Science Blog, 13.07.2026): fiktive Szenarien, nur wenige Läufe je Modell, Autoren nennen eigene Einschränkungen."],
  "nur": ["**Interessenkonflikt:** Karte C stammt von Anthropic – dem Hersteller von Claude, mit dem dieses Material gebaut wurde. Das habe ich in Karte C und Aufgabe 6 offen benannt; es gehört zur Lernaufgabe (Interesse ≠ Falschheit). Die Einzelheiten der Studie habe ich nur anhand der Seite und ihrer Zusammenfassung geprüft."],
  "stolper": "Betroffenheit ≠ Arbeitsplatzverlust; Simulation ≠ Alltagshäufigkeit; Motive aus Schlagzeilen ablesen."},
 {"titel": "6 Gestalten und urteilen (Buch S. 65–77)",
  "text": ["Buchbezüge: Standortdumping, Arbeitsbedingungen, Lohndumping, Migration, Care-/Brain-Drain, Globalisierungskritik; Alternativen (u. a. Neokeynesianismus, öko-soziale Marktwirtschaft, SDGs, Weltsozialforum, Attac, Social Entrepreneurship). Das Debattenblatt (Pro/Kontra-Methode) bleibt ohne Seitenzahl; für Aufgabe 8 gibt es vier Perspektiven statt Tribunal.",
           "Bewertung von 8c: nachvollziehbare Begründung, richtige Zusammenhänge, Gegenargument, gekennzeichnete Unsicherheit. Die politische Richtung wird nicht benotet. Es gibt keinen neuen Notenschlüssel."],
  "nur": ["Brücke zur nächsten Einheit: Wirtschaft, Standards, Währungen, Technologie und Institutionen als verschiedene Quellen von Macht – die vertiefte Behandlung (EU, USA, NATO, »Macht des Westens«) bleibt der Folgeeinheit."],
  "stolper": "Standortverlagerung = faire Arbeit; Interessen ohne Beleg als Motive behaupten."},
]

RECHNEN = ["Zoll: Zollwert × Zollsatz = 100 × 0,15 = 15 US-Dollar; Zollwert + Zoll = 115 US-Dollar. Die Rechnung gilt nur bei unverändertem Zollwert; Annahmen zu Weitergabe, Marge und Wechselkurs fehlen bewusst.",
           "Übungsvariante (Seite): andere Zollwerte und Sätze, z. B. 80 USD und 10 % → 8 und 88; 160 USD und 25 % → 40 und 200.",
           "TWh: 1 TWh = 1 Milliarde kWh. 415 TWh sind rund 1,5 % des Weltstroms (IEA), also rund 27 000 TWh Weltverbrauch – nur zur Einordnung, nicht Pflichtstoff."]

FEHLVORSTELLUNGEN = [
    ["»Das Ausland zahlt den Zoll.«", "Der Importeur zahlt zuerst; die Last verteilt sich.", "Rechnung 100 → 115; wer kann Marge, Preis, Lieferantenpreis ändern?"],
    ["»15 % Zoll = 15 % mehr Ladenpreis.«", "Hängt von Weitergabe, Nachfrage, Wettbewerb ab.", "Aufgabe 3 e)"],
    ["»Trump ist gegen jede Globalisierung.«", "Schutz plus ausgewählte Abhängigkeiten (Aktionsplan).", "Karte A; Schlussfolgerung kennzeichnen"],
    ["»WTO = Weltregierung / UN-Organisation.«", "Mitgliederorganisation mit Konsens, keine UN-Sonderorganisation.", "Buch S. 53 ist hier ungenau"],
    ["»Ein Viertel betroffen = Viertel arbeitslos.«", "Betroffene Tätigkeiten, keine Stellen.", "ILO 2025"],
    ["»Simulation zeigt Alltagshäufigkeit.«", "Sie zeigt mögliche Schwachstellen unter Testbedingungen.", "Aufgabe 6, 7"],
    ["»EU hat KI verboten.«", "Risikobasierte Regeln.", "Fallkarten Aufgabe 5"],
    ["»Warnung = PR / echte Angst.«", "Motive nicht ablesbar; Interessen sind Hypothese.", "Aufgabe 6"],
]

FRAGEN = [("Dürfen die USA solche Zölle einfach verhängen?", "Nur mit Rechtsgrundlage. Der Supreme Court hat 2026 eine wichtige gekippt; andere (Section 232/301) gelten. Stand und Quelle nennen, bei Unsicherheit »vor dem Unterricht geprüft am …«."),
          ("Wer kontrolliert die WTO?", "Ihre Mitglieder; Entscheidungen im Konsens. Das schützt kleine Staaten und macht Reformen langsam."),
          ("Warum nutzt das Bundesheer nicht einfach nur heimische Technik?", "Beschaffung hängt an Lieferfähigkeit, Ersatzteilen und Datenkontrolle; vollständige Unabhängigkeit ist teuer und oft unmöglich. Keine Behauptung über eine konkrete Beschaffungsstelle."),
          ("Ist Anthropics Studie nicht Werbung?", "Der Interessenkonflikt ist real und wird in Aufgabe 6 genannt. Ob eine Studie trägt, zeigt Methode und Reichweite – nicht allein der Absender.")]

VIDEO_NOTIZ = {"keine": "Keine Pflichtvideos. Optionale Kandidaten aus dem Jahresplan: Ö1 Dimensionen »Zölle: Regulierungsinstrument oder Konfliktpotenzial für den Welthandel?« (24 min, 2025), Ö1 Journal-Panorama »Lieferketten: Sauber bis zum Ursprung?« (29 min, 2024), Ö1 Radiokolleg »Das ABC der Finanzwelt …« (12 min, 2019). Abspielbarkeit und Zeitmarken nicht geprüft – nur nach eigenem Anhören einsetzen, mit drei Hörfragen vorab."}

AUSBLICK = ("Nächste Einheit laut Handover: Wirtschaftliche Verflechtung, Standards, Währungen, Technologie und Institutionen als unterschiedliche Quellen von Macht; EU, USA, NATO und die »Macht des Westens« werden dort vertieft. "
            "Die Brücke in Stunde 4 ist nur die offene Frage, kein Stoff.")

BILDER = [
    ("Buch S. 43 · Trichter (Geschwindigkeiten)", "Stunde 1, nur Lehrer-Beamer: Was wird schneller, was bleibt Entfernung? Öffentlich: eigenes Modell (Sportuhr-Grafik)."),
    ("Buch S. 53 · Institutionentabelle", "Stunde 2, nur Lehrer: Welche Aufgaben vermischt die Tabelle? Öffentlich: eigene Aufgabenstruktur (Aufgabe 4)."),
    ("Buch S. 62 · IWF-Stimmrechte", "OPTIONAL, nur Lehrer: Datenstand klären; keine Prozentwerte öffentlich."),
    ("Buch S. 65 · Stadt/Armut", "Stunde 4 nur bei Bedarf, nur Lehrer."),
    ("Debattenblatt (ohne Seitenzahl)", "Grundlage für Aufgabe 8; öffentlich: eigene Rollenübersicht mit vier Perspektiven."),
]

QUELLEN = [
    "WKO (Seite vom 23.10.2026): Urteil des US Supreme Court vom 20.02.2026 zu IEEPA-Zöllen; IHK Chemnitz (Stand 21.08.2026): Zollregime seit 24.07.2026, EU-US-Rahmen seit 01.07.2026.",
    "EU-Kommission: EU-US trade deal (Q1) – Suchauszug; direkter Abruf nicht möglich. Warenspezifische Anwendung nicht geprüft.",
    "IWF/Weltbank/WTO-Leitungsseiten (Q2, Q5, Q6) – aus dem Handover übernommen und mit allgemeinem Wissen abgeglichen; Primärseiten von hier teilweise nicht abrufbar.",
    "Lagarde-Mitteilung des Europäischen Rates vom 29.10.2026 (Q3): nicht abrufbar, nicht bestätigt, nicht verwendet.",
    "WTO: DSB-Sitzung 25.09.2026 (Q9) nicht abrufbar; Berufungsinstanz blockiert und MPIA (rund 61 Mitglieder) nach Suchtreffern; MC14 Jaunde ohne Erklärung.",
    "EU-KI-Verordnung und AI Omnibus (Q12–Q15): Lewis Silkin und EU-Seiten (Suchtreffer): Amtsblatt 24.07.2026, in Kraft 27.07.2026; Fristen 02.12.2027 (Anhang III) und 02.08.2028 (Anhang I).",
    "ILO »Generative AI and Jobs« (20.05.2025, Q18). IEA »Energy and AI« (04/2025): 415 TWh 2024, rund 945 TWh 2030 (Projektion). IEA-Seite »Key Questions« (16.04.2026, Q19): nicht abrufbar.",
    "International AI Safety Report 2026 (03.02.2026, Q16); CAIS-Statement (30.05.2023, Q20); Anthropic Alignment Science Blog »Agentic Misalignment in Summer 2026« (13.07.2026, Q17) – Hersteller von Claude: Interessenkonflikt.",
    "Schulbuch IWK (Trauner), S. 41–77, Buchnotiz privat im Projekt. Buchfehler: S. 43 (GATT/GATS), S. 53 (WTO im UN-Gefüge; 166 vs. 164 Mitglieder), S. 62 (Stimmrechte nicht aktuell).",
]
