"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, Lehrer-Infos der PPPs und Lösungsmappe K1.4–1.5 Ökodesign und Ökobilanz.
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Word)."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v22, Zeile 9: Einheit 3 (E3) »Ökodesign und Ökobilanz«, Block A Ökologisches Wirtschaften, 2 Std. Kern (Mindestumfang 2), Buch S. 19–25, "
                  "Sozialform Einzelarbeit / Unterrichtsgespräch. Hier: 1 Stunde je Klasse (Stephans Vorgabe) – 5BK Di 03.11., 5AK Do 05.11.; Annahme 50 min."),
    ("K01 ", "die Grundlagen, Instrumente und Prinzipien ökologischen Wirtschaftens analysieren → Teil 1 und 2 (Ökodesign/Ökobilanz unterscheiden, Lebenszyklus, vier Schritte, Grenzen), Aufgabe 1, 2 a, 3"),
    ("K02 ", "ökologisches Wissen bei wirtschaftlichen Fragestellungen anwenden → Aufgabe 2 b–c (Klima und Kosten für dieselbe Leistung, Beschaffungsentscheidung), Zusatz 5–7"),
    ("N08 / N09 ", "Lebenszyklus von Waren erklären (Grafik, Flaschenfall) · Waren und Technologien naturwissenschaftlich, wirtschaftlich, ökologisch beschreiben (Nutzungsdauer, Ersatzteile, Wirkungskategorien)"),
    ("N10 ", "Warenproben naturwissenschaftlich untersuchen – im Jahresplan zugeordnet, in dieser gekürzten Stunde NICHT praktisch abgedeckt (keine Warenuntersuchung). V5.3 bleibt spätere Erweiterung."),
    ("P1–P3 / SDG 12 ", "Entrepreneurship (Produktverbesserung, Beschaffungsentscheidung) · Verbraucherbildung (Kaufpreis gegen Nutzungskosten, Werbeaussagen prüfen) · Umwelterziehung (Ressourcen, Lebensdauer, Problemverlagerung) · SDG 12 nachhaltige Konsum- und Produktionsmuster"),
    ("Schulprofil: ", "»Lebenszyklus eines Ausrüstungsgegenstands« → Trinkflasche für Sport und Ausbildung; Ersatzteile und Reparatur vor Ort als Frage der Einsatzbereitschaft (didaktische Ergänzung, kein GLV-Code in der Jahresplanzeile)."),
    ("Abweichung: ", "1 statt 2 Stunden (Stephans Vorgabe) – Grundzüge beider Themen bleiben vollständig, Recherche, Podcasts, Versuch V5.3 und Buch-Aufgaben S. 21/25 entfallen bzw. sind Zusatz. "
                     "Minutenplan aus der ChatGPT-Übergabe v3, ergänzt um Klassenbuch, PDF-Abgabe und Reserve. Kein CLIL."),
]


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, _ = PL.aufgaben_der(st)
        rows.append([f"{st['std']} · {st['datum']}", I.TEILNAME[1] + " + " + I.TEILNAME[2], "– (kein Versuch)",
                     PL.bereich(nrs) + " · Zusatz 4–9",
                     f"Lesen {PL.minuten(st, ['lesen'])} · Erklären {PL.minuten(st, ['erkl'])} · Aufgaben {PL.minuten(st, ['a'])} · Bespr. {PL.minuten(st, ['bespr'])} · Reserve {PL.minuten(st, ['reserve'])}",
                     st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "Beamer mit TH-Unterricht · Mini-Whiteboards und Stifte (1 je Paar) · Tafel für die Musterrechnung · optional zwei echte Trinkflaschen zum Zeigen (eine leichte, eine robuste)"}


def _karten():
    out = []
    for k in I.KLASSEN:
        st = PL.PLAN[k][0]
        t, schritte = 0, []
        for name, m, oh, art in st["phasen"]:
            schritte.append(f"Min {t}–{t + m}: {name}" + (" (ohne Handy)" if oh else "")); t += m
        schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, 1)])
        ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org")))
        out.append((f"{k} · Stunde 1 · {st['datum']} · Ökodesign und Ökobilanz", schritte, MATERIAL[1], ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Mini-Whiteboards und Stifte bereitlegen (1 je Paar) – für Aufgabe 1. Wer keines hat, schreibt ins Heft.",
    "TH-Unterricht vorher einmal mit F5 durchklicken: Lösungen erscheinen erst per Klick (Aufgabe 2 schrittweise). Regiefolie ausgeblendet am Anfang.",
    "QR-Codes testen (Theorieteil, Arbeitsblatt, Quiz). Die Einheit ist auf der Klassenseite noch versteckt: vor der ersten Stunde (Di 03.11.) einblenden – GitHub → Actions → »Einheit ein-/ausblenden« → 5ab-toew/k1-4-5-oeko → einblenden. Die Direktlinks funktionieren auch versteckt.",
    "Optional: zwei echte Trinkflaschen (leicht/robust) als Anschauung für den Einstieg – nicht bewerten, ob sie »besser« sind; Daten von echten Produkten haben wir nicht.",
    "Test am Do 12.11.: Teststoff und Dauer sind noch offen. Ob K1.4–1.5 dazugehört, entscheidest du – das Paket enthält keinen Teststoff.",
    "LMS: Abgabeordner »K1.4–1.5 Öko« für 5AK und 5BK anlegen (PDF des Arbeitsblatts am Stundenende).",
]

AUF_EINEN_BLICK = [
    ["Min 0–12 · Einstieg, Teil 1 lesen, klären", "Ökodesign = Umweltwirkungen schon beim Entwurf mitdenken, über den ganzen Lebenszyklus. Ziele: lange nutzen, Reparatur, Ersatzteile, trennbare Materialien. Grüner Aufdruck ist kein Ökodesign.", "Beamer, ggf. zwei Flaschen"],
    ["Min 12–17 · Aufgabe 1", "Drei Verbesserungen mit Lebenszyklus-Abschnitt und Wirkung, ein Zielkonflikt – zu zweit am Mini-Whiteboard, dann Foto.", "Mini-Whiteboards"],
    ["Min 17–26 · Teil 2 lesen, klären", "Ökobilanz in vier Schritten; funktionale Einheit (1.000 Nutzungen); Systemgrenze; CO₂-Äquivalent = nur Klima.", "Beamer"],
    ["Min 26–50 · Aufgabe 2, Besprechung, Aufgabe 3, PDF", "5/1 Flaschen, 26/16,5 kg CO₂-Äq., 60/50 € → B; Grenzen der Aussage. Abschlusscheck allein. PDF in LMS.", "Tafel für die Musterrechnung"],
]

KAPITEL = [
 {"titel": "1 Ökodesign: Gestaltung über den Lebenszyklus (Buch S. 19–21)",
  "text": ["**Begriff:** Ökodesign (Ecodesign) ist umweltgerechte Produktgestaltung. Der Kern ist der **Zeitpunkt**: In der Entwicklung wird ein großer Teil der späteren Umweltwirkungen festgelegt (Material, Bauweise, Energiebedarf, Reparierbarkeit, Trennbarkeit). Was dort entschieden ist, lässt sich in Produktion, Nutzung und Entsorgung kaum noch ändern.",
           "**Lebenszyklus:** Rohstoffe → Herstellung → Transport und Verkauf → Nutzung und Pflege → Nutzungsende (wiederverwenden, verwerten, entsorgen). Das Buch zeigt auf S. 23 eine ausführlichere Tabelle (Rohstoffe, Hilfsstoffe, Energie, Produktionsprozess, Distribution, Konsumation, End of Life) – im Unterricht genügt die Fünfer-Gliederung.",
           "**Systemdenken und Problemverlagerung:** Eine Verbesserung in einem Abschnitt kann eine Belastung in einen anderen verschieben (leichter → kurzlebiger; Isolierung → mehr Material, schlechter trennbar). Genau deshalb braucht Ökodesign die Bewertung über den ganzen Lebenszyklus – und damit die Ökobilanz.",
           "**Vorteile (Buch S. 20) als Möglichkeiten formulieren:** günstigere Produktion, Kundenvertrauen, Ressourcenschonung, Image. Sie können auseinanderfallen (ein langlebiges Produkt verkauft sich seltener). Für Kadetten: »möglich, nicht automatisch – Nachweis verlangen«.",
           "**Rechtslage (Buch S. 21 veraltet):** Die Ökodesign-Richtlinie 2009/125/EG für energieverbrauchsrelevante Produkte ist für bestehende Durchführungsverordnungen weiter Grundlage. Seit **18.07.2024** gilt zusätzlich die Verordnung (EU) 2024/1781 (»ESPR«) als Rahmen für fast alle physischen Waren (Ausnahmen u. a. Lebens- und Futtermittel, Arzneimittel). Konkrete Anforderungen kommen über **delegierte Rechtsakte je Produktgruppe**; der erste Arbeitsplan (April 2025) nennt Textilien/Bekleidung, Reifen, Möbel, Matratzen, Eisen/Stahl, Aluminium sowie Reparierbarkeit und Recycling bei Elektrogeräten.",
           "**Smartphones und Tablets:** Verordnung (EU) 2023/1670 (Ökodesign, noch auf Basis der Richtlinie 2009/125/EG) und 2023/1669 (Energielabel). Für jedes ab **20.06.2025** in Verkehr gebrachte Gerät: Robustheit, Akku-Haltbarkeit, Reparierbarkeitsklasse A–E, IP-Schutzklasse auf dem Label. Ersatzteile mindestens **sieben Jahre nach Verkaufsende** des Modells, Betriebssystem-Updates mindestens **fünf Jahre** nach Verkaufsende des letzten Geräts. Das ist das Beispiel für die Kadetten; Paragrafen und Stichtage sind Nachschlagewissen, kein Teststoff (außer du legst es fest)."],
  "nur": ["**Digitaler Produktpass (DPP):** Wird produktgruppenweise mit den delegierten Rechtsakten verpflichtend; das zentrale Register war gesetzlich bis 19.07.2026 vorgesehen – Stand vor der Stunde prüfen. Nicht behaupten, jede Ware habe schon einen Pass.",
          "**Vernichtungsverbot:** Seit Juli 2026 dürfen große Unternehmen unverkaufte Bekleidung, Bekleidungszubehör und Schuhe grundsätzlich nicht mehr vernichten; mittlere ab Juli 2030; Klein- und Kleinstunternehmen ausgenommen (Theorieteil »Für Schnelle«).",
          "**Bundesheer-Bezug:** Ersatzteilverfügbarkeit und Reparierbarkeit hängen mit Einsatzbereitschaft und Versorgung zusammen. Das ist eine didaktische Brücke, keine Aussage über konkrete Beschaffungsverfahren des Bundesheeres."],
  "stolper": "»Ökodesign = grünes Logo / Recyclingmaterial« und »leichter ist immer besser«. Gegenmittel: Stopp-Frage Teil 1, Zielkonflikt in Aufgabe 1 verpflichtend.",
  "bild": "img/lebenszyklus.png"},
 {"titel": "2 Ökobilanz: Methode in vier Schritten (Buch S. 22–24)",
  "text": ["**Begriff:** Ökobilanz (Life Cycle Assessment, LCA) = Zusammenstellung und Beurteilung der Input- und Outputflüsse und der potenziellen Umweltwirkungen eines Produktsystems über seinen Lebenszyklus. Methodischer Bezug: ISO 14040/14044 (hier nur öffentliches Abstract gelesen) und EU-Methoden zum Umweltfußabdruck (PEF).",
           "**Vier Schritte:** 1 Ziel und Untersuchungsrahmen (Zweck, funktionale Einheit, Systemgrenze, Annahmen) · 2 Sachbilanz (Inventar: Mengen hinein/heraus) · 3 Wirkungsabschätzung (Klassifizierung + Charakterisierung) · 4 Auswertung (Ergebnisse, Sensitivität, Grenzen, Empfehlungen). Iterativ, nicht linear. Das Buch beschreibt v. a. Schritt 2 und 3 (»Sachbilanz« und »Wirkungsbilanz«) – Schritt 1 und 4 in der Stunde ausdrücklich ergänzen.",
           "**Funktionale Einheit:** die quantifizierte Leistung, auf die sich alles bezieht. Ohne sie gewinnt im Vergleich »pro Stück« immer das kurzlebige Produkt. Unser Fall: 1.000 Nutzungen einer dichten, hygienischen Ein-Liter-Trinkflasche (A: 5 Stück, B: 1 Stück). Klassisches Lehrbuchbeispiel: Mehrweg- gegen Einweggebinde pro 1.000 l abgefüllter Getränk.",
           "**Systemgrenze:** was einbezogen wird. Gleiche Vorgänge in beiden Varianten (hier das Trinkwasser) darf man weglassen, weil sie sich beim Vergleich aufheben – das muss aber gesagt werden.",
           "**Buch S. 24 präzisieren:** »Ökobilanzen, die mit derselben Methode erstellt wurden, sind vergleichbar« ist zu kurz. Es müssen auch funktionale Einheit, Systemgrenzen, Datenqualität und Annahmen zusammenpassen."],
  "nur": ["**Allokation und Recycling:** Bei Nebenprodukten oder Recycling muss man Lasten aufteilen (Masse, Wert, Systemerweiterung, Gutschrift). Darum im Flaschenmodell keine zusätzliche Recycling-Gutschrift – sie ist in der »Endbehandlung« schon enthalten; eine zweite wäre Doppelzählung.",
          "**Bilanzarten (Buch S. 23):** Produktbilanz (Produkt über Lebenszyklus), Prozessbilanz (ein Verfahren), Betriebs-/Standortbilanz (alle Ströme eines Standorts in einem Zeitraum – Grundlage im Umweltmanagement, z. B. EMAS, Buch S. 26 ff.). Eine einfache Input-Output-Liste ist noch keine normgerechte Produktökobilanz."],
  "stolper": "Vergleich »ein Stück gegen ein Stück« und »gleiche Methode = vergleichbar«. Gegenmittel: Stopp-Frage, Aufgabe 3 b, Stolperstein-Folie.",
  "bild": "img/schritte.png"},
 {"titel": "3 Wirkungsabschätzung und CO₂-Äquivalente (Buch S. 24–25)",
  "text": ["**Klassifizierung:** Jeder Fluss der Sachbilanz wird den Wirkungskategorien zugeordnet, zu denen er beiträgt (SO₂ → Versauerung; Phosphat → Überdüngung; CO₂, CH₄, N₂O → Klima).",
           "**Charakterisierung:** Mit Faktoren wird der Beitrag in eine gemeinsame Einheit je Kategorie umgerechnet – für das Klima in kg CO₂-Äquivalenten (Treibhauspotenzial, meist über 100 Jahre).",
           "**Methan-Faktor im Buch (»1 kg CH₄ ≈ 24 kg CO₂«):** entspricht keinem IPCC-Bericht genau (SAR 21, TAR 23, AR4 25, AR5 28, AR6 27–29,8). Der Wert hängt vom Zeithorizont und vom Bericht ab; für die Stunde nicht nötig, nicht als Teststoff verwenden.",
           "**Viele Kategorien:** Buch S. 25 listet 14 »wesentliche Wirkungskategorien« – kein zeitloser ISO-Katalog; die Auswahl hängt von der Methode ab (die EU-Methode PEF/EF nutzt 16 Kategorien). In der Stunde genügen Klima, Ressourcen und ein weiteres Beispiel.",
           "**Nicht addieren:** Kategorien haben verschiedene Einheiten. Eine Gewichtung zu einer Gesamtzahl ist möglich, enthält aber Werturteile und muss offengelegt werden."],
  "nur": ["IPCC AR6 (2021), GWP über 100 Jahre: CH₄ fossil 29,8 · CH₄ nicht fossil 27,0 · N₂O 273 (CO₂ = 1). Ältere Berichte: AR4 CH₄ = 25, AR5 CH₄ = 28. Über 20 Jahre ist Methan deutlich wirksamer (AR6 ca. 80).",
          "Biologie-Brücke: Überdüngung (Eutrophierung) → Algenblüte, Sauerstoffmangel; Versauerung → Waldschäden, Gewässer; Klima → Treibhauseffekt (Buch S. 71). Gut für Fragen aus der Klasse."],
  "stolper": "»CO₂-Zahl = ganze Ökobilanz« und »B ist in jeder Hinsicht besser«. Gegenmittel: Grafik »Eine Zahl für das Klima – und die anderen Fragen?«, KI-Check (Zusatz 5).",
  "bild": "img/wirkungen.png"},
 {"titel": "4 Der Flaschenfall: Modell, Rechnung, Urteil (Aufgabe 2)",
  "text": ["**Modelldaten:** frei erfunden, keine Messwerte echter Produkte, Material bewusst nicht festgelegt. Diese Kennzeichnung steht überall sichtbar (Theorieteil, Arbeitsblatt, Folien).",
           "**Was die Kadetten üben:** Vergleich auf gleicher Leistung und Interpretation EINES Indikators plus Kosten. Sie erheben keine Sachbilanz und machen keine vollständige Wirkungsabschätzung – die Zahlen sind schon zusammengefasste Klimabeiträge.",
           "**Urteil mit Grenze:** »Für 1.000 Nutzungen empfehlen wir B: im Modell 9,5 kg CO₂-Äq. und 10 € weniger. Für ein umfassendes Urteil fehlen z. B. Wasser, Ressourcen, echte Lebensdauerdaten.« Nicht zulässig: »B ist immer und in jeder Hinsicht besser«, »Metall ist besser als Kunststoff«, »vorhandene Flaschen wegwerfen«.",
           "**Lebenszykluskosten:** Kaufpreis allein täuscht (8 € gegen 30 €); über die Leistung gerechnet 60 € gegen 50 €. Klima und Kosten getrennt ausweisen – eine Ökobilanz ersetzt keine Kostenrechnung und umgekehrt.",
           "**Sensitivität (Zusatz 6):** Hält B nur 500 Nutzungen, braucht man 2 Stück → 23 kg CO₂-Äq. (noch unter A) aber 80 € (teurer als A). Die Lebensdauer-Annahme entscheidet mit."],
  "nur": ["Reale Trinkflaschen-Ökobilanzen hängen stark von Reinigung (Spülmaschine, Warmwasser, Strommix) und Nutzungszahl ab. Deshalb ist die Reinigung im Modell bei beiden gleich und ein großer Posten (10 kg) – das zeigt, dass die Nutzungsphase wichtig sein kann."],
  "stolper": "Reinigung nur einmal ansetzen (0,01 statt 10 kg) · Herstellung pro Flasche vergleichen · nur Kaufpreise vergleichen · zusätzliche Recycling-Gutschrift. Gegenmittel: Rechenweg-Folie, Besprechung mit der Frage »Welche Behauptung wäre nicht erlaubt?«.",
  "bild": "img/flaschen.png"},
]

RECHNEN = [
    "**Aufgabe 2:** Flaschen A = 1.000 : 200 = 5; B = 1.000 : 1.000 = 1 · Klima A = 5 × (3 + 0,2) + 1.000 × 0,01 = 16 + 10 = 26 kg CO₂-Äq. · Klima B = 1 × (6 + 0,5) + 10 = 16,5 kg CO₂-Äq. · Kosten A = 5 × 8 + 1.000 × 0,02 = 40 + 20 = 60 € · Kosten B = 30 + 20 = 50 € · Differenz 9,5 kg und 10 €.",
    "**Zusatz 6:** B mit 500 Nutzungen → 2 Flaschen · 2 × 6,5 + 10 = 23 kg CO₂-Äq. · 2 × 30 + 20 = 80 €.",
    "**Rechenbeispiel im Theorieteil (Flasche C):** 250 Nutzungen → 4 Flaschen · 4 × (2 + 0,25) + 10 = 19 kg CO₂-Äq. · 4 × 5 + 20 = 40 €. Bewusst andere Zahlen als in Aufgabe 2, damit die Lösung nicht verraten wird.",
    "**Übungsvarianten am Handy:** Aufgabe 2 mit zufälligen Herstellungswerten (A 2–4 kg, B 5–8 kg) und Preisen (A 6–12 €, B 20–40 €); Zusatz 6 mit 250 oder 500 Nutzungen. Die Formeln ergeben mit den Originalzahlen genau die Lösungen (per Skript geprüft).",
]

FEHLVORSTELLUNGEN = [
    ["Ökodesign ist ein schönes, grünes Design.", "Ökodesign verändert Material, Haltbarkeit, Reparatur und Trennbarkeit – über den Lebenszyklus.", "Stopp-Frage 1 (grünes Blatt auf der Flasche); Mythos-Folie."],
    ["»Recycelbar« bedeutet umweltfreundlich.", "Sagt nur etwas über das Nutzungsende; Herstellung und Lebensdauer können wichtiger sein.", "Mythos-Check im Einstieg; Partnerkarte 8."],
    ["Die billigere Flasche ist die wirtschaftlichere.", "Entscheidend sind die Kosten für dieselbe Leistung (Lebenszykluskosten).", "Aufgabe 2: 8 € gegen 30 € → 60 € gegen 50 €."],
    ["Man vergleicht ein Stück mit einem Stück.", "Man vergleicht dieselbe Leistung (funktionale Einheit).", "Aufgabe 3 b; Stolperstein-Folie."],
    ["Weniger CO₂ = in jeder Hinsicht umweltfreundlicher.", "CO₂-Äquivalente zeigen nur die Klimawirkung.", "Grafik »Eine Zahl für das Klima«; KI-Check."],
    ["Eine Ökobilanz liefert ein objektives Endurteil.", "Ergebnis hängt von Annahmen, Grenzen und Daten ab; Gewichtung ist ein Werturteil.", "Zusatz 6 (Lebensdauer), Zusatz 7 (»50 % weniger CO₂«)."],
    ["Metall ist immer besser als Kunststoff (oder umgekehrt).", "Pauschale Material-Ranglisten sind nicht belegt – es kommt auf Leistung, Nutzung und Daten an.", "Modell ohne festgelegtes Material; Besprechung »nicht erlaubte Behauptung«."],
]

FRAGEN = [
    ("Ist dann eine Glasflasche besser als eine Plastikflasche?", "Kommt auf Nutzungszahl, Transportwege, Reinigung und Datenbasis an. Mehrweg-Glas schneidet bei vielen Umläufen und kurzen Wegen oft gut ab, bei langen Transporten schlechter. Eine pauschale Antwort gibt es nicht – genau das zeigt die Ökobilanz."),
    ("Warum zählt die Reinigung so viel (10 kg)?", "Weil sie 1.000-mal anfällt. Die Nutzungsphase kann bei langlebigen Produkten den größten Anteil haben – bei Elektrogeräten ist es oft der Strom im Betrieb."),
    ("Woher kommen die echten Zahlen für Ökobilanzen?", "Aus Messungen bei Herstellern, aus Datenbanken mit Durchschnittswerten (z. B. für Strom, Stahl, Transport) und aus Annahmen. Darum muss man Datenquelle und Alter angeben."),
    ("Gilt das Smartphone-Label auch für mein altes Handy?", "Nein – es gilt für Geräte, die seit 20.06.2025 in der EU in Verkehr gebracht werden. Ersatzteile müssen dann noch sieben Jahre nach dem Verkaufsende des Modells erhältlich sein."),
    ("Was ist der Unterschied zwischen Ökobilanz und CO₂-Fußabdruck?", "Der CO₂-Fußabdruck ist nur die Klimawirkung (eine Kategorie). Eine Ökobilanz betrachtet mehrere Umweltwirkungen."),
    ("Was ist der ökologische Fußabdruck aus dem Buch S. 40?", "Ein anderes Maß: die Fläche, die nötig wäre, um den Verbrauch eines Menschen oder Landes zu decken. Nicht mit der Ökobilanz eines Produkts verwechseln."),
    ("Kann man alle Umweltwirkungen zu einer Zahl zusammenrechnen?", "Rechnerisch mit Gewichtung ja, aber die Gewichte sind Werturteile (Was ist schlimmer – Wasser oder Klima?). Darum muss das offengelegt werden."),
    ("Biologie-Brücke: Warum ist Überdüngung ein Umweltproblem?", "Zu viel Stickstoff und Phosphor lässt Algen wachsen; beim Abbau wird Sauerstoff verbraucht, Fische ersticken. Das misst die Kategorie Eutrophierung."),
    ("Ist Recycling nicht immer gut?", "Meist besser als Deponie oder Verbrennung, aber es kostet Energie, und oft wird das Material schlechter (Downcycling). Länger nutzen und reparieren steht in der Abfallhierarchie davor."),
    ("Wie kauft das Bundesheer Ausrüstung?", "Darüber haben wir hier keine geprüften Angaben. Allgemein gilt für öffentliche Beschaffung: Kriterien vorher festlegen, Angebote für dieselbe Leistung vergleichen, Kosten über die Nutzungsdauer betrachten – genau unsere Logik."),
]

VIDEO_NOTIZ = {
    "kein_video": "Kein Video im Pflichtablauf (eine Stunde). Das Buch S. 19–25 enthält keinen Filmtipp, nur Links zu Recherchen (trauner.at/ecomatrix, gastherme, stahl, alt-Antriebe – nicht geprüft, für spätere Vertiefung). Ein kurzes, seriöses deutschsprachiges Erklärvideo war von hier aus nicht prüfbar (YouTube gesperrt) – nichts ungeprüft eingebaut.",
    "podcast": "Jahresplan-Podcasts zu E3: »Tauwetter #16: Welche Getränkeverpackungen sind wirklich klimafreundlich?« (No Bullshit – der profil-Wissenschafts-Podcast, 2021, ca. 29 min) und Ö1 Dimensionen »Wiederbefüllen, Recycling oder Wegwerfen – nachhaltigste Getränkeverpackung« (2019, ca. 24 min). Weder angehört noch auf Verfügbarkeit geprüft – nicht eingebaut. Passt später als Hörauftrag mit Beobachtungsfrage (»Welche funktionale Einheit wird verglichen? Was ändert das Ergebnis?«).",
    "ubaweb": "Umweltbundesamt (DE), Themenseiten Ökodesign und Ökobilanz – seriöse Startseiten für Recherche-Zusatzaufgaben (umweltbundesamt.de/themen/wirtschaft-konsum/produkte/oekodesign).",
}

AUSBLICK = ("Laut Buch- und Jahresplanfolge kommt danach »Ökologisches Management und Umweltmanagement« (Buch S. 26–30, E4) – im Auftrag nicht genannt. Anknüpfung: Die Betriebs-/Standortbilanz "
            "(Buch S. 23) ist die Grundlage von Umweltmanagementsystemen wie EMAS. V5.3 »Vereinfachte Lebenszyklusanalyse eines Produkts« (45 min) bleibt als Praxisstunde möglich, wenn Zeit ist (Inventar vorher prüfen).")

BILDER = [  # Bildverzeichnis: (Quelle, Seite/Ausschnitt, Art, Einsatz, Zweck)
    ("Trauner TÖW", "S. 23, Tabelle Lebenszyklus", "inhaltliche Nutzung, neu gezeichnet (vereinfacht)", "img/lebenszyklus.png (Theorie Teil 1, PPP)", "Lebenszyklus sichtbar machen"),
    ("ISO 14040 (Abstract), EU-Empfehlung 2021/2279", "vier Phasen", "inhaltliche Nutzung, eigene Darstellung", "img/schritte.png (Theorie Teil 2, PPP)", "Methode vom Lebenszyklus unterscheiden"),
    ("Trauner TÖW", "S. 24–25 (Wirkungsbilanz, Wirkungskategorien)", "Idee, eigene Darstellung (Auswahl von 6 Kategorien)", "img/wirkungen.png", "CO₂ ist nur eine Wirkung"),
    ("eigene Grafik", "–", "selbst gezeichnet, keine echten Produkte", "img/flaschen.png (Einstieg, Aufgabe 2)", "Einstieg und Modellfall"),
    ("Trauner TÖW, Buchseiten-Fotos S. 19–25", "–", "nicht verwendet (nur Verweise)", "–", "Buchbilder kommen nicht auf öffentliche Seiten und nicht in die Kadetten-PPP"),
]

QUELLEN = [
    "**Grundlage:** ChatGPT-Übergabe »Ökodesign und Ökobilanz« v3 (29.10.2026) mit Quellenpaket – Planung, Minutenplan, Aufgaben 1–3, Quizfragen, Quellen Q1–Q9 übernommen und von Claude nachgeprüft (Prüfbericht).",
    "**Trauner TÖW** S. 19–25 (vier Buchseiten-Fotos aus der Übergabe) – vollständig gelesen: S. 19 Einstieg Glühbirnenverbot, S. 20 Ökodesign und Vorteile, S. 21 Instrumente, Ökodesign-Verordnung (alter Stand), Aufgaben 1–8, S. 22 Song Contest 2015 (→ Zusatz 8), S. 23 Lebenszyklus, Bilanzarten, S. 24 Input-Output, Sach- und Wirkungsbilanz, S. 25 Wirkungskategorien und Aufgaben 1–5. Buch-Aufgaben S. 21/25 nicht übernommen (Recherche, Zeit) – Inhalte stecken in Aufgabe 1–3.",
    "**Bücher im Projekt durchsucht (project_search 30.10.2026):** Westermann Chemie 1 (Treibhausgase, CO₂-Äquivalente, Klimakonferenzen), Chemie muss stimmen (Biokunststofftaschen: Herstellung vs. Verbrennung) – geprüft, nichts übernommen (NAWI-Niveau, nicht zum Thema Produktbilanz). Kein anderes Buch behandelt Ökodesign oder Ökobilanz.",
    "**Unabhängige Zweitprüfung (Prüf-Agent, 30.10.2026):** Smartphone-Verordnung 2023/1670 (EUR-Lex), ESPR-Arbeitsplan April 2025 – eingearbeitet. **EU-Recht, selbst geprüft (30.10.2026):** Noerr-Zusammenfassung zur ESPR (Inkrafttreten 18.07.2024, delegierte Rechtsakte, Produktpass, Vernichtungsverbot ab Juli 2026); Verbraucherzentrale »Energielabel für Smartphones und Tablets« (seit 20.06.2025; Ersatzteile bis 7 Jahre, Updates 5 Jahre, Reparierbarkeit A–E). Übergabe-Quellen Q1–Q8 (EU-Kommission, EUR-Lex, ISO) laut ChatGPT geprüft.",
    "**Methodik:** ISO 14040:2006 (öffentliches Abstract), EU-Empfehlung 2021/2279 (PEF), EU-Kommission »LCA und Umweltfußabdruck-Methoden«; IPCC AR6 WG1 Tabelle 7.15 (GWP-Werte, Nur-für-dich-Kasten).",
    "**Jahresplan v22:** Zeile 9 (E3), K01/K02, N08–N10, P1–P3, SDG 12, Schulprofil; Versuche V5.3 (nicht durchgeführt); Podcasts E3 (nicht geprüft); Querverbindung NAWI Stoff- und Energieflüsse; Referatsthemen 3/4 (Ökodesign an einem Produkt, Ökobilanz eines T-Shirts) als Idee für Zusatz 9.",
    "**Nicht prüfbar von hier:** Videos (YouTube gesperrt), Podcasts (nicht angehört), Bedienung der PPP in Microsoft PowerPoint (nur gerendert).",
]
