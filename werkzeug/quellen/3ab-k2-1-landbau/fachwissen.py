"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, Lehrer-Infos der PPPs und Lösungsmappe K2.1 Formen der Landwirtschaft.
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Word). Grundlage: ChatGPT-Übergabe 11.10, nachgeprüft."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v24 (interne Titelzeile v19): Einheit 4 (E4) »Formen der Landwirtschaft«, Block B Landwirtschaft & Ernährung, 3 Std. Kern, Buch S. 38–48. "
                  "Hier: 4 Stunden (Stephans Vorgabe), 3AK und 3BK gleich – Mi 04.11., Mo 09.11. (zuerst 20 min Test), Mi 11.11., Mo 16.11.; Annahme 50 min."),
    ("K03 ", "die verschiedenen Formen der Landwirtschaft in Bezug auf Bodenbearbeitung, Verwendung von Chemikalien, Kulturformen und Tierhaltung erklären → "
             "Teil 1 (Vergleichstabelle mit genau diesen vier Merkmalen), Aufgabe 1 (vier Merkmale je Form arbeitsteilig, ganze Tabelle an der Tafel + Foto), Aufgabe 2 (Betrieb), Aufgabe 3 (Chemikalien/Pflanzenschutz), Aufgabe 4 (Kennzeichnung)"),
    ("N02 / N03 / N05 ", "Bedeutung für Wirtschaft, Technik, Umwelt (A2, A4, A5, A7) · Informationen aus Medien beschaffen und Fragen formulieren (Podcast, KI-Satz A4, Verpackungen, A8) · "
                         "Ergebnisse mit Kriterien bewerten (A7–A9)"),
    ("P1–P5 ", "Entrepreneurship (Betriebsentscheidung A2, A11) · Verbraucherbildung (Verpackungen, Preis pro Menge A4) · Umwelterziehung (Boden, Nützlinge) · politische Bildung (Gentechnik-Debatte) · "
               "Europa (EU-Bio-Regeln, EU-Verordnung 2026/1388)"),
    ("SDG 2 / 15 · GLV 4 ", "Ernährungssicherung, Leben an Land (Boden, Artenvielfalt) · Krisen- und Resilienzfähigkeit: Versorgung hängt an Boden, Energie, Betriebsmitteln, Lieferketten → Zusatz 10, Theorie »Versorgungssicherheit«"),
    ("Abweichung: ", "4 statt 3 Stunden; Schwerpunkt Gentechnik und Studienkritik (Séralini) als Ergänzung zu Buch S. 45 (Stephans Vorgabe). Kein Versuch (V3.12 Bodenprobe: Inventar reicht nicht für 8 Gruppen, nur 1 Messzylinder und 1 Sieb – spätere eigene Stunde). "
                     "Buch S. 40 (Entwicklung) und S. 46 (globaler Vergleich) nur als OPTIONAL. Kein CLIL. Kein Kahoot (Stephan, 30.10.2026)."),
]

THEMEN = {1: "Acker als Ökosystem, drei Formen, Bio (S. 38–43)", 2: "Pflanzenschutz, Kennzeichnung (S. 43–47)",
          3: "pro Hektar, Gene, Genschere, neue Sorte (S. 45–46)", 4: "Séralini, gute Studie, Folgestudie (Ergänzung)"}


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, _ = PL.aufgaben_der(st)
        z = f"Lesen {PL.minuten(st, ['lesen'])} · Erklären {PL.minuten(st, ['erkl'])} · Aufgaben {PL.minuten(st, ['a'])} · Bespr. {PL.minuten(st, ['bespr'])} · Reserve {PL.minuten(st, ['reserve'])}"
        if PL.minuten(st, ["test"]): z = f"Test {PL.minuten(st, ['test'])} · " + z
        if PL.minuten(st, ["hoeren"]): z += f" · Hören {PL.minuten(st, ['hoeren'])}"
        rows.append([f"{st['std']} · {st['datum']}", THEMEN[st["std"]], "– (kein Versuch)", PL.bereich(nrs), z, st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "Beamer mit TH-Unterricht · Tafel für die Vergleichstabelle (4 Merkmale × 3 Formen) · Partnerkarten (Theorieteil »Partnercheck«) · optional zwei Äpfel (Bio-Übersee / regional) als Anschauung",
            2: "Test (bestehend) · je Gruppe zwei Lebensmittel-Verpackungen, am besten ein Bio- und ein konventionelles Produkt derselben Art (z. B. Milch, Nudeln, Äpfel) mit Preisschild · Ersatz: Beispieldaten auf der Folie",
            3: "Mini-Whiteboards und Stifte (1 je Paar) · Lautsprecher, Podcast #167 bei Minute 05:39 vorbereitet",
            4: "Platz im Raum für eine Skala (Seil oder Linie: »gar nicht glaubwürdig« bis »sehr glaubwürdig«) · Papier für Aufgabe 9 · LMS-Abgabeordner"}


def _karten():
    out = []
    k = I.KLASSEN[0]
    for st in PL.PLAN[k]:
        t, schritte = 0, []
        for name, m, oh, art in st["phasen"]:
            schritte.append(f"Min {t}–{t + m}: {name}" + (" (ohne Handy)" if oh else "")); t += m
        schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
        ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org", "test")))
        out.append((f"3AK und 3BK · Stunde {st['std']} · {st['datum']} · {THEMEN[st['std']]}", schritte, MATERIAL[st["std"]], ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Einheit einblenden vor der ersten Stunde (Mi 04.11.): GitHub → Actions → »Einheit ein-/ausblenden« → 3ab-nawi/k2-1-landbau → einblenden. Die Direktlinks und QR-Codes funktionieren auch versteckt.",
    "TH-Unterricht einmal mit F5 durchklicken: Lösungen erscheinen erst per Klick. Regiefolien je Stunde ausgeblendet am Anfang; Start je Stunde über »Benutzerdefinierte Bildschirmpräsentation«.",
    "Stunde 2: Verpackungen sammeln (je Gruppe zwei, mit Preis pro kg/Liter). Reichen sie nicht, die Beispieldaten auf der Folie »Aufgabe 4« verwenden.",
    "Stunde 3: Podcast #167 (Apple Podcasts, Link im Theorieteil) bei 05:39 starten, ca. 7 min (bis etwa 12:40; ChatGPTs Schnitt ging bis 14:00) – vorher einmal anhören und die Stopp-Stelle festlegen (von mir nicht abgehört).",
    "Medien zur Freigabe (von hier aus nicht prüfbar): Trauner-Filmtipps nawi_v35 (S. 44) und nawi_v39 (S. 46), Niggli-Podcast #185. Passen sie, sag Bescheid – dann baue ich sie ein.",
    "LMS: Abgabeordner »K2.1 Landbau« für 3AK und 3BK anlegen (eine PDF am Mo 16.11. mit Aufgaben 1–9).",
]

AUF_EINEN_BLICK = [
    ["Stunde 1 · Acker und Formen", "Ernte nimmt Nährstoffe mit (jede Form muss düngen) · vier Merkmale: Boden, Dünger/Pflanzenschutz, Kulturen, Tiere · integriert ist ein Vorgehen · Bio = Regeln + Kontrolle, nicht »chemiefrei« · DOK-Versuch: im Schnitt ca. 20 % weniger Ertrag", "Tafel-Matrix"],
    ["Stunde 2 · Test, Pflanzenschutz, Verpackung", "Drei Methoden mit Wirkung und Grenze, Schadschwelle · EU-Bio-Logo + Code + Herkunft; AMA-Biosiegel", "Verpackungen"],
    ["Stunde 3 · Ertrag und Genschere", "Fläche = Menge : Ertrag; 20 % weniger Ertrag = 25 % mehr Fläche · Gen/Genom; Kreuzung, Mutation, Transgenese, Genschere · Leit-RNA findet, Cas9 schneidet, Zelle repariert, dann prüfen · neue Sorte: Nutzen belegen, Umwelt/Lebensmittel, Wirtschaft getrennt · EU-Verordnung ab 2028", "Mini-Whiteboards, Podcast"],
    ["Stunde 4 · Studienkritik", "Séralini 2012: 200 Ratten = 10 je Gruppe und Geschlecht, tumoranfälliger Stamm, EFSA-Kritik · gute Studie: Kontrolle, Zufall, Verblindung, Reichweite · G-TwYST 2019: 50 je Gruppe, keine Schadwirkung des geprüften Maises · Methode ≠ Betrug, Folgestudie ≠ Freibrief", "Skala im Raum, Papier"],
]

KAPITEL = [
 {"titel": "1 Der Acker als Ökosystem (Buch S. 38–39)",
  "text": ["**Agrarökosystem:** Ein Acker ist ein künstlich gehaltenes Pionierstadium. Ohne Eingriff liefe die **Sukzession** über Kräuter und Gebüsch meist bis zum Laubmischwald (Klimaxstadium; im Klimax ist der Biomassezuwachs etwa null – Buch S. 39). Das Buch begründet den Acker damit, dass im Pionierstadium der Biomassezuwachs hoch ist.",
           "**Nährstoffentzug:** Die Ernte entfernt Biomasse und damit N, P, K, Mg, S und Spurenelemente. Bodenuntersuchungen und Nährstoffbilanzen bestimmen, wie viel ergänzt werden muss. Leguminosen liefern über die Symbiose mit Knöllchenbakterien (Rhizobien) nur **Stickstoff**, nicht P oder K.",
           "**Boden:** Porenvolumen (Grob-, Mittel-, Feinporen) steuert Versickerung, Speicherung und Belüftung; Humus und Bodenorganismen stabilisieren die Krümelstruktur. Verdichtung entsteht vor allem bei hoher Radlast auf nassem Boden. Erosion vor allem auf unbedecktem Boden in Hanglage (Wasser) oder großen, kahlen Flächen (Wind). Mehr Pflügen ist nicht automatisch Bodenschutz – reduzierte Bearbeitung und Bodenbedeckung (Zwischenfrüchte, Mulch) wirken oft besser."],
  "nur": ["Biologie-Brücke: Stickstoffkreislauf – Nitrogenase der Rhizobien reduziert N₂ zu NH₃; braucht viel ATP, darum »bezahlt« die Pflanze mit Zucker (Symbiose). Überschüssiger Nitrat-Stickstoff wird ausgewaschen → Grundwasser, Eutrophierung (Buch S. 39: »Intensive Düngung kann das Grundwasser beeinträchtigen«)."],
  "stolper": "»Bio braucht keinen Dünger« und »Sonnenlicht ersetzt Nährstoffe«. Gegenmittel: Stopp-Frage 1, Pfeil »Ernte« in der Grafik.",
  "bild": "img/acker.png"},
 {"titel": "2 Drei Formen der Landwirtschaft (Buch S. 41–43)",
  "text": ["**Konventionell:** alle Betriebe, die »nur« die allgemeinen Gesetze einhalten (Düngeverordnung/Nitrat-Aktionsprogramm, Pflanzenschutzmittelrecht, Tierschutzgesetz). Das ist eine große Bandbreite – von spezialisierten Großbetrieben bis zu kleinen Bergbauernhöfen mit Weidehaltung. Viele konventionelle Betriebe in Österreich nehmen am Agrarumweltprogramm ÖPUL teil.",
           "**Integriert:** im Buch als Mittelstellung mit dem Beispiel Bodenhaltung. Fachlich ist »integriert« vor allem ein Prinzip – integrierter Pflanzenschutz ist in der EU (Richtlinie 2009/128/EG) für **alle** beruflichen Anwender vorgeschrieben. Es gibt keine eigene, EU-weit geschützte »integrierte« Betriebsform mit eigenen Tierhaltungsregeln. Die Drei-Spalten-Darstellung des Buches ist als Lernhilfe brauchbar, wenn du die Überlappung ansprichst.",
           "**Biologisch:** geregelt durch die EU-Öko-Verordnung (EU) 2018/848 (seit 2022). Kein mineralischer Stickstoffdünger, keine chemisch-synthetischen Pflanzenschutzmittel (Ausnahmen in einer Positivliste: z. B. Kupfer, Schwefel, Pflanzenextrakte, Pheromone), keine GVO und keine NGT-Pflanzen, flächengebundene Tierhaltung mit Auslauf, Bio-Futter, jährliche Kontrolle. Bestimmte mineralische P- und K-Dünger (z. B. Rohphosphat, Kaliumsulfat) sind erlaubt – darum ist »Kunstdünger verboten« (Buch S. 42) nur für Stickstoff ganz richtig.",
           "**Tierarzneimittel:** Verordnung (EU) 2019/6, Art. 107: Antibiotika dürfen in der EU **nicht routinemäßig** und nicht zum Ausgleich schlechter Haltung eingesetzt werden – das gilt konventionell wie bio. Bio hat zusätzlich längere Wartezeiten und Höchstzahlen an Behandlungen.",
           "**Langzeitversuch DOK (FiBL, Therwil/CH, seit 1978):** biodynamisch, organisch-biologisch, konventionell, dazu eine ungedüngte Kontrolle, mehrfach wiederholte Parzellen. Mäder u. a. (Science 2002): Bio-Erträge im Mittel ca. 20 % niedriger, bei Winterweizen geringer, bei Kartoffeln deutlich größer; dafür mehr Bodenleben und weniger Energieeinsatz. Urs Niggli leitete das FiBL bis 2020; er bezieht sich im Podcast #185 auf diesen Versuch."],
  "nur": ["**Westermann-Blatt 2017 (Quelle im ZIP):** deutsche Mittelwerte 2015/16, Weizen 80 bzw. 36 dt/ha. ChatGPT hat die pauschale Gegenüberstellung »Tierwohl vs. Bodenschutz« daraus zu Recht verworfen. Die Zahlen nur als historisches Rechenbeispiel verwenden.",
          "Buch S. 41: »Käfighaltung in Österreich seit 2009 verboten« – gilt für herkömmliche Käfige; ausgestaltete Käfige sind in Österreich seit 2020 ebenfalls ausgelaufen. Für die Kadetten reicht: in Österreich keine Käfighaltung von Legehennen."],
  "stolper": "»Integriert = dritte Welt« und »konventionell = Monokultur ohne Tierwohl«. Gegenmittel: Hinweis unter der Tabelle, Aufgabe 2 (konventioneller Betrieb mit Hecken und Fruchtfolge).",
  "bild": None},
 {"titel": "3 Pflanzenschutz und Kennzeichnung (Buch S. 43–47)",
  "text": ["**Schädling/Nützling** sind menschliche Kategorien (Buch-Aufgabe S. 48 Nr. 6: »Gibt es in der Natur wirklich Schädlinge?«). Integrierter Pflanzenschutz: Vorbeugen (Fruchtfolge, Sorte, Saatzeit) → Überwachen (Gelbschalen, Bonitur) → Schadschwelle → Maßnahme → Erfolgskontrolle.",
           "**Resistenz:** Selektion – häufiger Einsatz desselben Wirkstoffs tötet die empfindlichen Individuen, die zufällig widerstandsfähigen überleben und vermehren sich (Biologie-Brücke Evolution). Gegenmittel: Wirkstoffwechsel, weniger Einsätze.",
           "**EU-Bio-Logo:** Pflicht auf vorverpackten Bio-Lebensmitteln aus der EU; darunter Code der Kontrollstelle (AT-BIO-xxx) und Herkunft der landwirtschaftlichen Ausgangsstoffe (»EU-/Nicht-EU-Landwirtschaft«, ggf. Land). **AMA-Biosiegel** (rot-weiß, »Austria«): österreichische Rohstoffe, höchstens ein Drittel nicht aus Österreich, wenn hier nicht in Bio-Qualität erhältlich; schwarz-weiß ohne Ursprungsangabe (Buch S. 43). Verbände (Bio Austria, Demeter) haben teils strengere Richtlinien.",
           "**Bezugsgröße:** Umweltwirkung pro Hektar und pro Kilogramm Produkt kann unterschiedlich ausfallen – Bio ist pro Fläche oft günstiger (weniger Stickstoff, mehr Artenvielfalt), pro Kilogramm wegen geringerer Erträge manchmal nicht. Für die Kadetten genügt: Die Frage »besser?« braucht eine Bezugsgröße."],
  "nur": ["Rechnen: 20 % weniger Ertrag → Ertragsindex 80 → Fläche 100/80 = 1,25 → 25 % mehr Fläche. Bei 36 statt 80 dt/ha: 2,22-fache Fläche = 122 % mehr (nicht »222 % mehr«)."],
  "stolper": "»Bio-Logo = regional« und Prozent-Umkehr (20 % weniger Ertrag = 20 % mehr Fläche). Gegenmittel: KI-Satz in Aufgabe 4, Stopp-Frage 2.",
  "bild": "img/flaeche.png"},
 {"titel": "4 Gentechnik und Genschere (Buch S. 45–46, ergänzt)",
  "text": ["**Begriffe:** Gen = DNA-Abschnitt, der für ein funktionelles Produkt (RNA, Protein) codiert; Genom = gesamte Erbinformation. Mutationszüchtung (Strahlen, Chemikalien, seit den 1930er-Jahren) erzeugt viele zufällige Mutationen; sie fällt rechtlich nicht unter die GVO-Kennzeichnung. Transgenese = Einbau fremder Gene (z. B. NK603-Mais: Glyphosat-Toleranz durch ein Bakteriengen).",
           "**CRISPR/Cas9:** Leit-RNA (guide RNA, ca. 20 Basen passend zur Ziel-DNA neben einer PAM-Sequenz; ähnliche Stellen können mitgeschnitten werden = Off-Target) bindet Cas9 und führt es zur Zielstelle; Cas9 erzeugt einen Doppelstrangbruch. Die Zelle repariert meist durch NHEJ (Nicht-homologe Endverknüpfung, oft kleine Insertionen/Deletionen → Gen ausgeschaltet) oder mit Vorlage durch HDR (gezielte Änderung). Danach: Sequenzieren, Off-Target-Prüfung, Auswahl, Rückkreuzen (CRISPR-Konstrukt entfernen), Sortenprüfung. Nobelpreis Chemie 2020 an Charpentier und Doudna.",
           "**Nachweisbarkeit:** Eine kleine Punktmutation lässt sich nachweisen, wenn man weiß, wo man suchen muss – aber nicht, ob sie durch CRISPR, klassische Mutagenese oder spontan entstanden ist. Darum ist »unsichtbar« zu pauschal, »immer erkennbar« aber auch falsch.",
           "**EU-Recht:** Verordnung (EU) 2026/1388 über NGT-Pflanzen, angenommen 17.06.2026, in Kraft seit 16.07.2026, anwendbar ab 17.07.2028 (EU-Kommission). Kategorie NGT 1 (Veränderungen wie bei konventioneller Züchtung möglich): kein GVO-Zulassungsverfahren, nur Saatgut gekennzeichnet; NGT 2: GVO-Recht mit Risikoprüfung und Kennzeichnung, nationales Anbauverbot möglich. NGT-Pflanzen im Biolandbau verboten (BMLUK). Bis 2028 gelten die bestehenden GVO-Regeln."],
  "nur": ["Niggli-Transkript (#185): Die CRISPR-Passage verknüpft sehr verkürzt mit Covid-Impfstoffen und behauptet fehlende Nachweisbarkeit – nicht als Mechanismuserklärung verwenden. Im automatischen Transkript sind Fachbegriffe teils falsch geschrieben.",
          "Jurassic Park (Einstieg Teil 3): Halbwertszeit von DNA in Knochen ca. 521 Jahre (Allentoft u. a. 2012); nach ca. 1,5 Mio. Jahren auch unter idealen Bedingungen nichts Lesbares mehr. Älteste sequenzierte DNA ca. 2 Mio. Jahre (Grönland, Sedimente, 2022)."],
  "stolper": "»Genschere setzt fertige Eigenschaft ein« und »präzise = sicher«. Gegenmittel: Schritt 4 »Prüfen« in Grafik und Aufgabe 6, Aufgabe 7 b.",
  "bild": "img/genschere.png"},
 {"titel": "5 Studienkritik: Séralini 2012 und G-TwYST 2019 (Ergänzung)",
  "text": ["**Séralini u. a. 2012** (Food and Chemical Toxicology): 2 Jahre, Sprague-Dawley-Ratten, 10 Gruppen je Geschlecht à 10 Tiere (Kontrolle, NK603 in 3 Dosen, NK603 + Roundup in 3 Dosen, Roundup im Wasser in 3 Dosen). Behauptet: mehr Tumore, frühere Sterblichkeit. **EFSA 2012** (DOI 10.2903/j.efsa.2012.2986): unzureichendes Design, zu kleine Gruppen für Krebsfragen (OECD-Richtlinie: 50 je Geschlecht), keine geeignete Statistik, Darstellung lässt keine Schlüsse zu. 2013 zurückgezogen (Begründung des Herausgebers: nicht schlüssig, kein Betrug festgestellt), 2014 in Environmental Sciences Europe wiederveröffentlicht.",
           "**G-TwYST** (Steinberg u. a. 2019, Archives of Toxicology, DOI 10.1007/s00204-019-02400-1): EU-gefördert, NK603 mit und ohne Roundup-Behandlung im Anbau, 90-Tage-, 1-Jahres- und 2-Jahres-Studie, 50 Tiere je Geschlecht und Gruppe in der Langzeitstudie. Keine nachteiligen Effekte, die auf die Verfütterung zurückgehen. Keine exakte Wiederholung aller Séralini-Arme (z. B. kein Roundup im Trinkwasser) – also kein Urteil über Glyphosat allgemein.",
           "**Didaktischer Kern:** gleiche Maßstäbe für beide Seiten. »Keine belastbare Krebsfolgerung« ist keine Garantie für null Risiko; Unsicherheit ist aber auch kein Schadensbeweis. Methodische Schwäche ≠ Betrug; Rückzug ≠ Fälschung."],
  "nur": ["Spontane Tumorrate bei Sprague-Dawley-Weibchen über 2 Jahre: Mammatumore bei einem großen Teil der Tiere (je nach Labor und Studie etwa ein Drittel bis über die Hälfte). Je Geschlecht gab es nur EINE Kontrollgruppe mit 10 Tieren gegen 9 Behandlungsgruppen. Bei 10 Tieren je Gruppe ist ein Unterschied von 3 zu 7 Tieren statistisch kaum von Zufall zu unterscheiden.",
          "Sport-Brücke (Zusatz 12): dieselben Kriterien bei Nahrungsergänzungsmitteln – Placebo, Doppelblind, Randomisierung, Stichprobengröße, vorab festgelegter Endpunkt, unabhängige Replikation."],
  "stolper": "Séralini als Betrüger oder G-TwYST als Freibrief darstellen. Gegenmittel: Merke-Kasten Teil 4, Bewertungskriterien Aufgabe 9.",
  "bild": "img/gruppen.png"},
]

RECHNEN = [
    "**Aufgabe 5:** 80 dt : 80 dt/ha = 1,00 ha · 80 dt : 36 dt/ha = 2,22 ha (2,222…). Zusätzliche Fläche: 1,22 ha = 122 % mehr. Prüfung am Handy: Zahl mit Einheit ha, 2 % Spielraum (2,2 zählt, 2,22 kg nicht).",
    "**Beispiel im Theorieteil (andere Zahlen):** 60 dt Gerste bei 50 dt/ha → 1,2 ha; bei 30 dt/ha → 2 ha.",
    "**Indexbeispiel:** Ertrag 100 → 80 (−20 %) → Fläche 100 : 80 = 1,25 (+25 %).",
    "**Séralini:** 200 : (2 Geschlechter × 10 Gruppen) = 10 Tiere je Gruppe und Geschlecht. G-TwYST: 50 je Gruppe und Geschlecht.",
    "**Übungsvariante am Handy:** Aufgabe 5 mit Menge 40–120 dt, Ertrag 60–90 bzw. 30–45 dt/ha (zählt nicht für die Abgabe; per Skript gegen die Originalzahlen geprüft).",
]

FEHLVORSTELLUNGEN = [
    ["Bio braucht keinen Dünger.", "Auch Bio muss den Nährstoffentzug ersetzen (Mist, Kompost, Leguminosen, erlaubte Mineraldünger).", "Grafik »Acker«: Pfeil Ernte."],
    ["Bio ist chemiefrei / rückstandsfrei.", "Bio verbietet bestimmte Mittel; erlaubte Mittel (z. B. Kupfer) und Abdrift sind möglich.", "Mythos-Folie im Einstieg."],
    ["Konventionell bedeutet Monokultur ohne Tierwohl.", "Auch konventionelle Betriebe nutzen Fruchtfolge, Hecken, Weide, Tierwohlprogramme.", "Aufgabe 2."],
    ["Natürlich heißt ungefährlich.", "Stoff, Dosis und Anwendung entscheiden (Kupfer reichert sich im Boden an).", "Theorie »Was Bio genau heißt«."],
    ["20 % weniger Ertrag = 20 % mehr Fläche.", "100 : 80 = 1,25 → 25 % mehr.", "Stopp-Frage 2."],
    ["Gentechnikfreie Lebensmittel haben keine Gene.", "Alle Lebewesen haben Gene; die Kennzeichnung betrifft die Herstellung.", "Stopp-Frage 3 (Tomate)."],
    ["200 Tiere = große Studie.", "Aufgeteilt waren es 10 je Gruppe und Geschlecht.", "Grafik »200 Ratten«."],
    ["Eine zurückgezogene Studie ist gefälscht.", "Rückzug kann methodische Gründe haben; Betrug braucht eigene Belege.", "Merke-Kasten Teil 4."],
]

FRAGEN = [
    ("Ist Bio gesünder?", "Bio-Produkte haben im Schnitt weniger Pflanzenschutzmittel-Rückstände; ein klarer Gesundheitsvorteil für Menschen ist in Studien schwer nachzuweisen, weil Bio-Käufer oft auch sonst gesünder leben (Störfaktor). Ehrlich: »Weniger Rückstände ja, gesünder – unklar.«"),
    ("Warum ist Bio teurer?", "Weniger Ertrag pro Fläche, mehr Handarbeit (Unkraut), teureres Futter, Kontrollkosten (Buch-Aufgabe Hölzel 5.10 b)."),
    ("Kann Bio die Welt ernähren?", "Mit gleichen Essgewohnheiten bräuchte man mehr Fläche. Studien zeigen, dass es mit weniger Fleisch und weniger Lebensmittelverschwendung eher möglich wäre – das ist eine Szenariofrage, keine einfache Ja/Nein-Antwort."),
    ("Was ist Glyphosat?", "Ein Unkrautvernichtungsmittel (Herbizid), das ein Enzym im Aminosäurestoffwechsel der Pflanzen hemmt (Shikimat-Weg), den Tiere nicht haben. In der EU bis 2033 zugelassen (Verlängerung 2023); die Krebs-Einstufung ist umstritten (IARC »wahrscheinlich krebserregend« 2015 vs. EFSA/ECHA »nicht krebserregend«) – im Unterricht als Beispiel für unterschiedliche Bewertungen, nicht entscheiden."),
    ("Gibt es Genmais in Österreich?", "Anbau: nein, Österreich hat den Anbau von GVO verboten. Gentechnisch veränderte Futtermittel (z. B. Soja) werden in die EU importiert und müssen gekennzeichnet sein; Fleisch von damit gefütterten Tieren muss nicht gekennzeichnet werden (Buch S. 45)."),
    ("Ist die Genschere gefährlich?", "Das Werkzeug selbst ist ein Protein und eine RNA. Entscheidend ist, was verändert wurde und wie die Pflanze genutzt wird – darum wird das Ergebnis geprüft, nicht nur die Methode."),
    ("Biologie-Brücke: Wie binden Leguminosen Stickstoff?", "Knöllchenbakterien (Rhizobien) in Wurzelknöllchen wandeln N₂ aus der Luft mit dem Enzym Nitrogenase in Ammonium um; die Pflanze liefert dafür Zucker – Symbiose."),
    ("Warum werden Schädlinge resistent?", "Selektion: Die wenigen von Natur aus widerstandsfähigen Tiere überleben und vermehren sich – wie bei Antibiotikaresistenz von Bakterien."),
    ("Was bringt das Bundesheer mit Landwirtschaft zu tun?", "Versorgungssicherheit (GLV 4): Bei Krisen hängt Ernährung an Diesel, Dünger, Lieferketten. Das Bundesheer unterstützt im Katastrophenfall (z. B. Hochwasser) auch landwirtschaftliche Regionen – konkrete Verpflegungsplanung kenne ich nicht, darum nur allgemein."),
    ("Was ist eine Kontrollgruppe beim Menschen?", "Eine Gruppe, die ein Scheinmittel (Placebo) bekommt; im Idealfall wissen weder Teilnehmer noch Forscher, wer was bekommt (doppelblind)."),
]

VIDEO_NOTIZ = {
    "moder": "Podcast #167 »Erklär mir Gentechnik, Martin Moder« (Erklär mir die Welt, 01.06.2021, ca. 1 Std.) – Apple-Podcasts-Seite geöffnet und bestätigt. Ausschnitt ab 05:39 aus deiner alten PPP (dort bis 14:00); im Plan jetzt ca. 7 min, damit Stunde 3 Reserve hat. Von mir nicht abgehört. Beobachtungsauftrag: zwei Aussagen und eine überprüfbare Rückfrage notieren. Stand 2021 – Rechtslage seitdem geändert (EU-Verordnung 2026/1388).",
    "niggli": "Podcast #185 »Erklär mir nachhaltige Landwirtschaft, Urs Niggli« (2021) – Folge auf erklärmir.at gelistet, Folgenlink von hier aus nicht prüfbar. ChatGPT-Auswahl N1: Beginn »Bleiben wir kurz beim Biolandbau«, Ende »einen sehr schlechten Stand« (ca. 4–5 min, geschätztes Suchfenster 12–18 min). N2: »Jedes Land kann natürlich einen separaten Weg gehen« bis »die Technologie spielt für mich keine Rolle« (ca. 2–3 min). Nicht eingebaut – nur nach deiner Freigabe; Ersatz ist der Theorie-Abschnitt »Ein Versuch, der seit 1978 läuft«.",
    "trauner": "Trauner-Filmtipps: www.trauner.at/nawi_v35.aspx (Buch S. 44, biologische Schädlingsbekämpfung) und www.trauner.at/nawi_v39.aspx (Buch S. 46, Dokumentation österreichische Landwirtschaft). Von hier aus nicht erreichbar – Ziel, Länge und Verfügbarkeit bitte selbst prüfen; dann als OPTIONAL einbauen.",
}

AUSBLICK = ("Nächste Einheit laut Jahresplan: E5 »Nahrungs- und Genussmittel I« (Buch S. 49–56: Haltbarmachung, Zusatzstoffe, Milch, Fleisch) mit Versuchen V3.13–V3.15. "
            "Anknüpfung: Kennzeichnung (Bio-Logo, Gentechnik) und »Analyse landwirtschaftlicher Produkte« (Buch S. 47–48, Joghurtvergleich) passen als Brücke. "
            "V3.12 Bodenprobe bleibt als eigene Praxisstunde möglich, wenn Messzylinder und Siebe nachgekauft sind (Inventar: je 1 Stück).")

BILDER = [
    ("eigene Grafik", "–", "selbst gezeichnet", "img/acker.png (Theorie Teil 1, PPP)", "Nährstoffentzug, Verdichtung, Erosion"),
    ("eigene Grafik nach Westermann-Daten 2017", "Weizen 80/36 dt/ha", "selbst gezeichnet", "img/flaeche.png (Teil 2, Aufgabe 5)", "Bezugsgröße Fläche"),
    ("eigene Modellzeichnung nach Nobelpreis-Erklärung 2020", "vier Schritte", "selbst gezeichnet", "img/genschere.png (Teil 3, Aufgabe 6)", "Mechanismus als Modell"),
    ("eigene Grafik nach Séralini 2012/EFSA 2012", "Gruppenaufteilung", "selbst gezeichnet", "img/gruppen.png (Teil 4, Aufgabe 8)", "Gesamtzahl ≠ Gruppengröße"),
    ("Trauner NAWI HAK 3, Buchseiten S. 38–48", "–", "nicht verwendet (nur Verweise)", "–", "keine Buchbilder auf öffentlichen Seiten und in den PPPs"),
]

QUELLEN = [
    "**Grundlage:** ChatGPT-Übergabe »26-27-3AB-K2.1-Landbau-Entwurf-ChatGPT-v1.md« (28.10.2026) samt Quellenpaket und Arbeitsfassung v1 (TH-Unterricht, TH-Lehrer, TH-Kadetten, Word, Quiz) – Planung, Aufgaben A1–A12, Lösungen, Quiz und Quellen übernommen, sprachlich vereinfacht, nach Regelwerk umgebaut und nachgeprüft (Prüfbericht).",
    "**Trauner NAWI HAK 3** S. 38–48 (5 Doppelseiten-Bilder im ZIP) vollständig gelesen: Filmtipps nawi_v35 (S. 44) und nawi_v39 (S. 46) bestätigt; Buch-Aufgaben S. 40–48 als Ideen genutzt (Fruchtfolge, Bio-Kennzeichnung, Schädlingsbegriff), nicht wörtlich übernommen.",
    "**Bücher im Projekt durchsucht (project_search 30.10.2026):** Hölzel NAWI HAK 1 (Ökosysteme, Insektizide, Asiatischer Marienkäfer, Hecken als Lösungsansatz, Aufgabe 5.10 Bio teurer) → Idee für Nützlinge und Fragen; Westermann Chemie 1 (pH des Bodens, Kalkung) → Fachwissen; Expedition Chemie 4 Praxisteil (Blumendünger selbst gemacht) → nicht übernommen (Zeit). Weitere Bücher behandeln das Thema nicht.",
    "**EU-Recht, selbst geprüft (30.10.2026):** EU-Kommission »EU legislation on new genomic techniques for plants« (Annahme 17.06.2026, in Kraft 16.07.2026, anwendbar 17.07.2028) und BMLUK »Neue genomische Techniken« (NGT 1/2, Kennzeichnung, Biolandbau-Verbot). Übrige Quellen laut ChatGPT-Übergabe: EFSA 2012, Séralini 2014 (PMC5044955), Steinberg 2019 (PMC7261740), Nobelpreis 2020, EU-Seiten Bio und Tierarzneimittel.",
    "**Medien:** Apple-Podcasts-Seite #167 geöffnet (Titel, Datum 01.06.2021, Dauer 1 Std. bestätigt). Nicht prüfbar: Trauner-Links, Podcast #185 (Folgenlink), Abhören der Audios.",
    "**Jahresplan v24:** E4 (K03, N02/N03/N05, P1–P5, SDG 2/15, GLV 4, Schulprofil Ernährungssicherheit), Versuch V3.12 (nicht durchgeführt), Podcasts E4 (Forschungsquartett, Ö1 – nicht geprüft), Referatsthema »Landwirtschaft 4.0«, Querverbindung PBGW (Neolithische Revolution).",
    "**Inventar:** V3.12 geprüft – Messzylinder 1, feines Sieb 1, Bechergläser 100 ml 3 → für 8 Gruppen nicht ausreichend (darum kein Versuch).",
]
