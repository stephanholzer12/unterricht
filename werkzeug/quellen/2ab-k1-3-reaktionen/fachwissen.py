"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, VS-Fachwissen und private Lehrer-Seite K1.3 Stoffumwandlung."""

STUNDENVORSCHLAG = [
    ["1 · Di 03.11.", "Einstieg (Handwärmer, Mythos), Teil 1 Redox: Lavoisier, Elektronenübergang, Oxidations-/Reduktionsmittel", "K1.3-V1 Demo (12 min) · K1.3-V2 Ansatz (parallel)", "1–3 · Zusatz 4", "Aufgaben ~13 min · Reserve 8 min", "Demo mit Vorhersage: Hand heben »leichter/schwerer/gleich«"],
    ["2 · Do 05.11.", "Test K1.2 (20 min) · Teil 2: Redox im Alltag, Rost, Rostschutz, Eisen + Kupfersulfat", "K1.3-V3 Demo (8 min)", "5–7 · Zusatz 8", "Aufgaben ~10 min · Reserve 7 min", "Test; Demo mit Vorhersage; Zusatz 8 in Handschrift"],
    ["3 · Di 10.11.", "V2 auswerten · Teil 3: exo/endo, Energiediagramm, Aktivierungsenergie, Erhaltung", "V6 Demo (8 min) · Gr. 1–3: Stationen V4 + V5 (3 Runden à 11 min)", "Gr. 4–6: 9–11 · Zusatz 12", "Stationen 33 min · Reserve 2 min", "Demo mit Vorhersage; Stationenbetrieb (Handy nur Protokoll)"],
    ["4 · Do 12.11.", "Teil 4: Katalysator, Enzyme, Autokatalysator, Industrie", "V7 Demo (10 min) · Gr. 4–6: Stationen V4 + V5", "13–14 · Gr. 1–3: 9–11, Deutung V4/V5", "Stationen 33 min · Reserve 4 min", "Demo mit Vorhersage; Stationen"],
    ["5 · Di 17.11.", "Partnercheck · Teil 5: vier Stellschrauben, Faustregel, Staubexplosion · Abschluss", "V8 Gruppenversuch (18 min) · Protokolle fertig (7 min)", "18 · 16–17 · Zusatz 15", "Aufgaben ~9 min · Reserve 5 min", "Partnercheck mündlich, Gruppenversuch (Handy = Stoppuhr)"],
    ["Zusatz", "Für Schnelle: Oxidationszahlen, Forschung, Science oder Fiction", "V9 Lehrer-Demo", "19–23", "–", "–"],
]

CHECKLISTE = [
    "Bis 03.11.: Brausetabletten (9 Stück, gleiche Sorte) und 2 Kartoffeln besorgen; Eis für die Demo am 10.11. einfrieren (Kühlbox).",
    "Zitronensäure suchen (laut Fotoabgleich vorhanden, Gefäß-Nr. fehlt) – sonst Entkalker-Pulver aus dem Supermarkt.",
    "Löschdecke bzw. Sand für K1.3-V1 bereitlegen (Bestand laut Inventar unklar).",
    "Vor Stunde 3: Kupfersulfatlösung (15,0 g Pentahydrat auf 150 ml Lösung) und Zitronensäurelösung (60 g + 90 g Wasser) ansetzen und beschriften; 6 × 6,0 g Natron und 30 g Salz abwiegen; beide Stationen einmal selbst ausprobieren.",
    "Behälter »Schwermetall-Lösungen« und »feste Metallreste« an Station 1 stellen.",
    "Vor Stunde 4: 10,0 g Wasserstoffperoxid 30 % (#127) + 90,0 g Wasser (Handschuhe, Vollsichtschutzbrille); Kartoffel 10 min kochen und abkühlen lassen; Rost-Ansätze aus dem Gestell räumen; Behälter für manganhaltige Reste bereitstellen.",
    "Nur 2 Thermometer im Bestand: Analog (#147, bis −10 °C) an Station 1; Digital (#25) zuerst für die Demo V6, dann an Station 2. Messbereich des Digitalthermometers vorab prüfen.",
    "Für V8: 18 unbenutzte Einweg-Petrischalen (#39); für V9 (Zusatz): Abzug #97 prüfen, sonst Video.",
    "QR-Codes am Beamer (Folie »Dein Lernpfad«); Einheit auf der Klassenseite einblenden (GitHub → Actions → »Einheit ein-/ausblenden«).",
]

STUNDENKARTEN = [
    ("Stunde 1 · Di 03.11. · Redoxreaktionen", [
        "Einstieg (5 min): Handwärmer herumgeben (F-020), Frage »Warum wird er warm?« · Mythos-Folie »Wird Verbrennen leichter?«.",
        "Demo K1.3-V1 (12 min, ohne Handy): Eisenwolle wiegen – Vorhersage per Hand heben, auf der Unterlegplatte zünden. Während die Schale abkühlt (ca. 5 min): Theorie Teil 1 erklären (Elektronen wandern, Animation). Dann nachwiegen, Aufgabe 1 eintragen.",
        "Theorie Teil 1 selbst lesen (10 min): Lernpfad scannen.",
        "Aufgaben 2–3 am Handy (10 min) – währenddessen setzt die Lehrkraft mit zwei Kadetten die Rost-Ansätze K1.3-V2 an.",
        "Besprechung Aufgabe 3 (5 min) · Reserve ca. 8 min – wer früher fertig ist: Zusatz-Aufgabe 4. Keine Hausübung."],
     "Waage 0,01 g, Abdampfschale, Eisenwolle, Batterie 4,5 V, Unterlegplatte · 4 Reagenzgläser, Gestell, Öl, Salz, Parafilm, abgekochtes Wasser",
     "Demo mit Vorhersage (Hand heben); Rost-Ansatz"),
    ("Stunde 2 · Do 05.11. · Test + Rost", [
        "Test K1.2 (20 min, inkl. Austeilen und Einsammeln).",
        "Demo K1.3-V3 Kupferbrief (8 min): Vorhersage »innen schwarz oder glänzend?«, 1 min erhitzen, 2 min abkühlen, aufklappen; Aufgabe 5 gleich dabei.",
        "Theorie Teil 2 lesen (8 min), Aufgaben 6–7 am Handy (7 min) · Reserve ca. 7 min.",
        "Wer früher fertig ist: Zusatz-Aufgabe 8 (Pflegebefehl mit der Hand, Foto ins Arbeitsblatt). Keine Hausübung."],
     "Kupferblech 4 × 4 cm, Bunsenbrenner, Halter, Unterlegplatte, Mini-Whiteboards",
     "Test; Pflegebefehl in Handschrift"),
    ("Stunde 3 · Di 10.11. · Energie + Stationen (Gruppe 1–3)", [
        "Weißt du noch? (3 min, Mini-Whiteboard).",
        "Rost-Ansätze auswerten (4 min): Gläser zeigen, Fotos, Vergleich mit der Vorhersage.",
        "Demo K1.3-V6 Kältemischung mit Vorhersage (8 min) – dabei exotherm/endotherm kurz erklären; Sicherheitsfolie.",
        "Gruppe 1–3: drei Runden à 11 min an Station 1 (V4) und 2 (V5) – messen, beobachten, aufräumen, Erkenntnis eintragen; die jeweils freie Gruppe liest Teil 3 und macht Aufgaben (wer beide Stationen hinter sich hat: Deutung V4/V5 im Protokoll). Gruppe 4–6: Teil 3 lesen, Aufgaben 9–11 (ca. 23 min, Rest = Puffer, Zusatz 12).",
        "Reserve 2 min · keine Hausübung."],
     "Demo V6 (Eis, Salz, Digitalthermometer) · Stationen 1–2 (siehe Herrichte-Liste), Sammelbehälter",
     "Demo mit Vorhersage; Stationenbetrieb – Handy nur fürs Protokoll"),
    ("Stunde 4 · Do 12.11. · Katalysatoren + Stationen (Gruppe 4–6)", [
        "Weißt du noch? (3 min).",
        "Demo K1.3-V7 mit Vorhersage (10 min, Aufgabe 13 gleich dabei) – Katalysator kurz erklären.",
        "Gruppe 4–6: drei Runden à 11 min an Station 1 und 2; Gruppe 1–3: Aufgaben 9–11 fertig, Deutung V4/V5 im Protokoll, Teil 4 lesen, Aufgabe 14 (ca. 27 min von 33).",
        "Reserve 4 min · keine Hausübung."],
     "4 Reagenzgläser, H₂O₂ 3 %, Braunstein-Pulver, Kartoffel roh/gekocht, Holzstäbchen, Feuerzeug · Stationen 1–2",
     "Demo mit Vorhersage; Stationen"),
    ("Stunde 5 · Di 17.11. · Tempo + Abschluss", [
        "Partnercheck Aufgabe 18 (5 min, mündlich) statt »Weißt du noch?«.",
        "Theorie Teil 5 lesen (6 min).",
        "Gruppenversuch K1.3-V8 Brausetablette (18 min inkl. Austeilen und Aufräumen, Handy = Stoppuhr), Aufgabe 17.",
        "Aufgabe 16 (4 min) · Protokolle fertig (Deutung V4/V5 für Gruppe 4–6) und Besprechung der Stationen (7 min).",
        "Abgabe der PDFs (5 min) · Reserve 5 min · Quiz als freiwilliger Selbsttest, Kahoot nur, wenn Zeit bleibt · Zusatz 15 für Schnelle. Keine Hausübung."],
     "18 Einweg-Petrischalen, Brausetabletten 9, warmes Wasser (Wasserkocher), Messzylinder · Kahoot-Tabelle",
     "Partnercheck mündlich; Gruppenversuch"),
]

AUF_EINEN_BLICK = [
    ["1 · 03.11.", "Oxidation = Elektronenabgabe, Reduktion = Elektronenaufnahme – immer gleichzeitig. Eisenwolle wird beim Verbrennen schwerer.", "Waage, Eisenwolle, Batterie · Rost-Ansätze"],
    ["2 · 05.11.", "Rost braucht Wasser + Sauerstoff, Salz beschleunigt. Schutz: Schicht, Zink, Edelstahl, waschen, trocknen.", "Kupferblech, Brenner"],
    ["3 · 10.11.", "Exotherm gibt Energie ab, endotherm nimmt sie auf. Fast jede Reaktion braucht Aktivierungsenergie. Masse und Energie bleiben erhalten.", "Demo V6 · Stationen V4–V5"],
    ["4 · 12.11.", "Katalysator senkt die Aktivierungsenergie und wird nicht verbraucht – Braunstein, Enzyme, Autokatalysator.", "H₂O₂, Braunstein, Kartoffel"],
    ["5 · 17.11.", "Tempo: Oberfläche, Temperatur (+10 °C ≈ doppelt), Konzentration, Katalysator.", "Brausetabletten, Petrischalen"],
]

KAPITEL = [
 {"titel": "1 Redoxreaktionen (Buch S. 30–31)",
  "text": ["**Grundidee:** Bei einer Redoxreaktion wandern Elektronen von einem Teilchen zum anderen. Wer Elektronen abgibt, wird oxidiert; wer sie aufnimmt, wird reduziert. Weil Elektronen nicht verschwinden, laufen beide Teilreaktionen immer zusammen ab.",
           "**Historisch:** Lavoisier (um 1775) erkannte durch genaues Wiegen, dass Metalle beim Verbrennen Sauerstoff aufnehmen. Daher »Oxidation« (oxygène) für die Verbindung mit Sauerstoff, »Reduktion« für die Rückführung (lat. reducere = zurückführen) des Metalls aus dem Oxid. Die Elektronen-Sicht ist allgemeiner: Auch Eisen in Kupfersulfatlösung ist eine Redoxreaktion – ohne Sauerstoffgas als Oxidationsmittel.",
           "**Magnesium + Sauerstoff:** Mg (2 Außenelektronen) → Mg²⁺ + 2 e⁻; O (6 Außenelektronen) + 2 e⁻ → O²⁻. Beide erreichen die Edelgaskonfiguration von Neon. Die Ionen bilden ein Ionengitter (Brücke zu K1.2).",
           "**Oxidationsmittel / Reduktionsmittel:** Das Oxidationsmittel nimmt Elektronen auf (es oxidiert den Partner und wird selbst reduziert), das Reduktionsmittel gibt Elektronen ab. Merksatz für die Kadetten: »Das Mittel macht es beim anderen.«"],
  "nur": ["Bei Molekülverbindungen (z. B. C + O₂ → CO₂) werden Elektronen nicht vollständig übertragen, sondern verschoben. Deshalb braucht man formal die **Oxidationszahlen**: Steigt die Oxidationszahl, liegt eine Oxidation vor. Im Jahresplan bewusst nur als Zusatz (kein Rechendrill) – Aufgabe 20.",
          "Redox-Paare kann man nach ihrem Bestreben, Elektronen abzugeben, ordnen (Redoxreihe/Spannungsreihe: Mg > Zn > Fe > Cu > Ag > Au). Das kommt in der Elektrochemie (Jahresplan E9) – K1.3-V4 bereitet es vor."],
  "stolper": "Kadetten setzen »Oxidation = Sauerstoff« gleich. Gegenbeispiel parat haben: Eisen in Kupfersulfat (K1.3-V4) – das Oxidationsmittel sind Kupfer-Ionen, nicht Sauerstoffgas. (Sauerstoffatome stecken im Sulfat und im Wasser, sie nehmen hier aber keine Elektronen auf.)",
  "bild": "img/redox_mg_end.png"},
 {"titel": "2 Korrosion und Rostschutz (Buch S. 30, 98)",
  "text": ["Eisen rostet nur mit **Wasser und Sauerstoff**. Rost ist wasserhaltiges Eisen(III)-oxid; er ist porös und blättert ab – darum frisst sich Korrosion immer tiefer (anders als die dichte Oxidschicht bei Aluminium oder Chrom).",
           "**Schutzmaßnahmen:** Schutzschicht (Lack, Öl, Fett, Kunststoff), Verzinken (Zink als »Opferanode« – unedler, wird zuerst oxidiert, schützt sogar an Kratzern), Legieren (Edelstahl: ≥ 10,5 % Chrom bildet eine Passivschicht), Salz entfernen, trocken lagern."],
  "nur": ["Elektrochemisch: An der Anode Fe → Fe²⁺ + 2 e⁻, an der Kathode (meist am Rand des Wassertropfens, wo mehr Sauerstoff ist) O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻. Fe²⁺ und OH⁻ bilden Fe(OH)₂, das weiter zu FeO(OH)/Fe₂O₃ · x H₂O oxidiert. Salz erhöht die Leitfähigkeit des Elektrolyten und beschleunigt so den Strom im »Lokalelement«.",
          "Wirtschaft: Studien schätzen die weltweiten Korrosionskosten auf rund 3–4 % der Wirtschaftsleistung – gute Gesprächsbrücke zur Wirtschaftsklasse (ohne die Zahl im Kadettenmaterial)."],
  "stolper": "»Rost ist eine Farbe/Schmutz auf dem Eisen« – nein: Rost IST umgewandeltes Eisen; das Metall wird dünner."},
 {"titel": "3 Exotherm und endotherm, Aktivierungsenergie (Buch S. 32–34)",
  "text": ["**Exotherm:** Die Endstoffe enthalten weniger chemische Energie (in den Bindungen) als die Ausgangsstoffe – der Unterschied geht an die Umgebung (Wärme, Licht, elektrische Energie). **Endotherm:** umgekehrt; der Vorgang nimmt Wärme aus der Mischung und der Umgebung auf (es wird kalt) – manche Vorgänge brauchen auch ständiges Heizen oder Licht (Fotosynthese).",
           "**Energiediagramm:** y-Achse Energie, x-Achse Reaktionsverlauf. Das Buch führt ΔH ein (S. 33): ΔH < 0 exotherm, ΔH > 0 endotherm. Laut Jahresplan keine Enthalpie-Rechnungen – nur das Vorzeichen.",
           "**Aktivierungsenergie:** Auch exotherme Reaktionen starten nicht von selbst (Holz an der Luft). Bindungen müssen erst gelockert werden – der »Berg« im Diagramm. Beim Lagerfeuer liefert die frei werdende Wärme die Aktivierung für die nächsten Teilchen (Kettenwirkung). Das ist eine Erklärung für das Weiterbrennen, nicht die Definition von exotherm (die lautet: Endstoffe energieärmer, ΔH < 0). Die Länge des Aktivierungspfeils sagt nichts darüber, ob eine Reaktion exotherm ist.",
           "**Erhaltung:** Masse (Atome) und Energie bleiben erhalten – Eisenwolle wird schwerer, weil Sauerstoff eingebaut wird (K04!)."],
  "nur": ["Warum läuft eine endotherme Reaktion überhaupt freiwillig (Zitronensäure + Natron, Kältekompresse)? Entscheidend ist die freie Enthalpie ΔG = ΔH − T·ΔS. Entstehen viele Gasteilchen oder lösen sich Ionen, nimmt die Entropie stark zu – das »bezahlt« die aufgenommene Wärme. Oberstufenstoff, nur falls ein Kadett fragt.",
          "Werte zum Einordnen: Verbrennung von Holz ca. −15 bis −18 MJ/kg; Lösen von Ammoniumnitrat +26 kJ/mol (Kältekompresse); Fe + Cu²⁺ ≈ −150 kJ/mol."],
  "stolper": "Aktivierungsenergie ≠ endotherm. Ein Streichholz für das Lagerfeuer macht die Verbrennung nicht endotherm.",
  "bild": "img/diagramm_exo_endo.png"},
 {"titel": "4 Katalysatoren und Enzyme (Buch S. 34–36)",
  "text": ["Ein **Katalysator** öffnet einen anderen Reaktionsweg mit niedrigerer Aktivierungsenergie; er geht aus der Reaktion unverändert hervor. Er ändert das Tempo, nicht die Lage von Anfang und Ende (ΔH bleibt gleich) und auch nicht das Gleichgewicht.",
           "**Positiver/negativer Katalysator** (Buchbegriffe): Nach IUPAC ist ein Katalysator ein Beschleuniger. »Negative Katalysatoren« heißen heute Hemmstoffe/Inhibitoren (z. B. in Rostschutz- oder Konservierungsmitteln); sie wirken auf verschiedene Weise (z. B. Katalysator blockieren, Zwischenstufen abfangen), werden oft verbraucht und »erhöhen die Aktivierungsenergie« nicht allgemein. Die Kadetten lernen: Katalysator beschleunigt, Hemmstoff bremst.",
           "**Autokatalysator (Dreiwege-Kat):** Keramikwabe mit poröser Beschichtung (Washcoat, meist Aluminiumoxid), darin fein verteilte Pt-, Pd-, Rh-Teilchen. Er altert über die Jahre (Hitze, Vergiftung), wird aber nicht pro Reaktion verbraucht. Oxidiert CO und Kohlenwasserstoffe, reduziert NOₓ zu N₂ – braucht etwa 250–300 °C (»Light-off«) und beim Benziner ein genaues Luft-Kraftstoff-Verhältnis (Lambda-Sonde). Kaltstart = Hauptquelle der Emissionen.",
           "**Enzyme:** Biokatalysatoren aus Eiweiß, sehr spezifisch (Schlüssel-Schloss). Katalase zerlegt H₂O₂ (fällt im Stoffwechsel an) – deshalb schäumt rohe Kartoffel/Leber/Blut. Hitze denaturiert das Eiweiß → Enzym unwirksam (gekochte Kartoffel)."],
  "nur": ["Haber-Bosch-Verfahren: N₂ + 3 H₂ ⇌ 2 NH₃ an Eisenkatalysator, 400–500 °C, 150–300 bar. Etwa die Hälfte des Stickstoffs in unseren Körpern stammt rechnerisch aus Kunstdünger – starke Brücke zu Ernährungssicherheit und Wirtschaft (Jahresplan E14).",
          "Katalysator-Diebstahl (ORF Wien, März 2026): Pd, Pt und Rh sind sehr teuer – Rhodium mehr als doppelt so viel wert wie gleich schweres 750er-Gold."],
  "stolper": "»Der Katalysator filtert« bzw. »wird verbraucht« – genau diese Fehler stecken in der KI-Antwort von Aufgabe 15.",
  "bild": "img/diagramm_kat.png"},
 {"titel": "5 Reaktionsgeschwindigkeit (Buch S. 36)",
  "text": ["Teilchen müssen zusammenstoßen – oft genug und mit genug Energie (Stoßtheorie). Mehr Oberfläche → mehr Teilchen können gleichzeitig reagieren; höhere Temperatur → schnellere Teilchen, mehr Stöße über der Aktivierungsenergie; höhere Konzentration/Druck → mehr Stöße; Katalysator → mehr Stöße sind erfolgreich.",
           "**Faustregel (RGT-Regel, van 't Hoff):** +10 °C → etwa doppelt so schnell (in Wirklichkeit Faktor 2–4). Für die Kadetten: »etwa doppelt«.",
           "**Staubexplosion:** Feinster Staub hat riesige Oberfläche und ist mit Luft gut gemischt – Mühlen, Silos, Sägewerke. Buch S. 36 zeigt es mit Bärlappsporen (nicht im Inventar, nur mit Abzug und Schutzscheibe)."],
  "nur": ["Biologie-Brücke: Viele menschliche Enzyme arbeiten bei Körpertemperatur gut; Temperaturoptimum und Hitzestabilität hängen vom Protein ab – eine einheitliche Denaturierungstemperatur gibt es nicht (Savitski et al., Science 2014). Kühlkette bei Lebensmitteln, Fieber als Abwehrreaktion."],
  "stolper": "Kadetten verwechseln »schneller« mit »mehr Energie frei«. Ein Katalysator ändert nur das Tempo, nicht die Wärmemenge."},
]

RECHNEN = [
    "**Masse (A12):** 1,20 g Eisenwolle → 1,52 g. Eingebauter Sauerstoff 0,32 g; Zunahme 0,32 : 1,20 · 100 ≈ 26,7 %. Vollständig zu Fe₃O₄ wären es +38 %, zu Fe₂O₃ +43 %.",
    "**Faustregel (A17):** 80 s bei 20 °C → 40 s bei 30 °C → 20 s bei 40 °C. Allgemein: t = t₀ : 2^(ΔT/10). Übungsvariante mit Zufallszahlen auf dem Arbeitsblatt.",
    "**Verdünnen (V7):** Massenanteile! 10,0 g H₂O₂-Lösung (w = 30 %) enthalten 3,0 g H₂O₂; + 90,0 g Wasser = 100,0 g Lösung mit w = 3 %. (10 ml der 30-%-Lösung wiegen wegen der Dichte ≈ 1,11 g/ml ca. 11 g – mit 90 ml Wasser ergäbe das ≈ 3,3 %.)",
    "**Kupfersulfat (V4):** 15,0 g CuSO₄ · 5 H₂O auf 150 ml Lösung = 10 g Pentahydrat pro 100 ml Lösung (≈ 6,4 g CuSO₄ pro 100 ml; M = 249,7 g/mol). Keine Angabe »10 %« verwenden.",
    "**Zitronensäure (V5):** 60 g + 90 g Wasser = 150 g Lösung, w = 40 % (Dichte ca. 1,2 g/ml → ca. 125 ml).",
]

FEHLVORSTELLUNGEN = [
    ["Beim Verbrennen wird Stoff vernichtet.", "Atome bleiben erhalten; Gase entweichen oder werden eingebaut.", "Eisenwolle auf der Waage (V1) – sie wird schwerer."],
    ["Oxidation braucht immer Sauerstoff.", "Oxidation = Elektronenabgabe, auch ohne Sauerstoffgas.", "Eisen in Kupfersulfat (V4)."],
    ["Endotherme Reaktionen laufen nicht von selbst.", "Viele laufen freiwillig und kühlen dabei.", "Zitronensäure + Natron (V5), Kältekompresse."],
    ["Exotherme Reaktionen brauchen keinen Start.", "Fast jede Reaktion braucht Aktivierungsenergie.", "Holz liegt an der Luft und brennt nicht; Animation »Kugel über den Berg«."],
    ["Der Katalysator wird verbraucht/filtert.", "Er wandelt um und bleibt unverändert.", "Braunstein nach V7 abfiltrieren und zeigen: noch da."],
    ["Salz schmilzt Eis, weil Salz warm ist.", "Salzwasser gefriert erst unter 0 °C; Schmelzen braucht Energie aus der Umgebung.", "Kältemischung (V6) wird viel kälter als 0 °C."],
]

FRAGEN = [
    ("Warum rostet Edelstahl nicht?", "Chrom bildet an der Luft sofort eine hauchdünne, dichte Chromoxidschicht. Wird sie zerkratzt, bildet sie sich neu (Passivierung)."),
    ("Warum rostet Aluminium nicht, obwohl es unedler ist als Eisen?", "Seine Oxidschicht (Al₂O₃) ist dicht und haftet – sie schützt das Metall darunter. Rost dagegen ist porös."),
    ("Kann man Rost rückgängig machen?", "Chemisch ja (Reduktion, z. B. im Hochofen mit Kohlenstoff); Rostumwandler wandeln Rost in eine stabile Schicht um – das abgetragene Metall kommt aber nicht zurück."),
    ("Warum wird mir beim Schwitzen kalt?", "Verdunsten ist endotherm: Die Energie zum Verdunsten kommt aus der Haut. Biologie-Brücke: Thermoregulation."),
    ("Ist Atmung auch eine Verbrennung?", "Ja, eine »stille« Oxidation: Glucose wird mit Sauerstoff zu CO₂ und Wasser oxidiert – in vielen kleinen, enzymgesteuerten Schritten, damit die Energie als ATP nutzbar wird."),
    ("Warum explodiert Mehl, obwohl man damit backt?", "Nur als feiner Staub in der Luft: riesige Oberfläche, jedes Körnchen von Sauerstoff umgeben. Im Sack fehlt beides."),
    ("Braucht ein Elektroauto einen Katalysator?", "Nein – es gibt keine Verbrennungsabgase. Hybride mit Verbrennungsmotor schon."),
    ("Warum hilft Kühlen bei einer Prellung?", "Kälte verlangsamt Stoffwechsel und Entzündungsreaktionen, verengt Gefäße – weniger Schwellung (RGT-Regel im Körper)."),
    ("Was ist im Handwärmer genau?", "Eisenpulver, Wasser, Salz (Elektrolyt, beschleunigt), Aktivkohle (verteilt Luft und Wasser), Vermiculit. Das Eisen rostet in Stunden statt Monaten – exotherm."),
    ("Warum leuchtet ein Knicklicht?", "Chemilumineszenz: Eine Reaktion gibt Energie als Licht ab (statt als Wärme) – eine »kalte« exotherme Reaktion. Im Gefrierfach leuchtet es schwächer, aber länger (Temperatur!)."),
    ("Ist Fieber gefährlich für Enzyme?", "Leichtes Fieber hilft der Abwehr. Sehr hohes Fieber ist ein medizinischer Notfall – viele Abläufe im Körper geraten durcheinander. Eine feste Temperatur, ab der alle Enzyme kaputtgehen, gibt es aber nicht; jedes Eiweiß ist unterschiedlich hitzeempfindlich."),
]

VIDEO_NOTIZ = {
    "redox": "Gut für die Wiederholung zu Hause (Stunde 1). Der zweite Teil mit Oxidationszahlen ist Zusatz – ggf. bei ca. 3 min stoppen.",
    "cuo": "Filmtipp aus dem Buch S. 31: Kupferoxid + Aktivkohle, CO₂-Nachweis mit Kalkwasser – zeigt K1.3-V9, falls die Demo entfällt.",
    "cufe": "Filmtipp aus dem Buch S. 31: Kupferoxid + Eisenpulver glüht durch – passt zum Beispiel CuO + Fe → Cu + FeO.",
    "exoendo_buch": "Filmtipp aus dem Buch S. 32 (englischsprachiger Kanalname, Versuche stumm/kurz) – vorab einmal ansehen.",
    "exoendo": "Kurz (2,5 min), Brausetablette und Lagerfeuer als Beispiele, Energiediagramm mit Aktivierungsenergie.",
    "kat": "4 min: Aktivierungsenergie, Autokatalysator, Enzyme – gut als Einstieg in Stunde 4 oder zur Wiederholung.",
}

AUSBLICK = ("Nächste Einheit laut Jahresplan: E8 Säuren und Basen (Buch S. 53–61), danach Elektrochemie (E9–E10): Batterie, Akku, Brennstoffzelle, Elektrolyse – "
            "dort wird der Elektronenübergang aus K1.3 (Eisen in Kupfersulfat, Redoxreihe) zur Spannungsquelle. Rost und Hochofen kommen in E12 (Metalle) wieder.")

QUELLEN = [
    "**Trauner NAWI 2** S. 29–37 (Theorie, Buch-Aufgaben »Ziele erreicht« 1–7, Versuche S. 31, 33, 36, Filmtipps nawi_v130, v131, v19) und S. 98 (Korrosionsschutz). Buch-Aufgaben S. 37 Nr. 4–7 in eigenen Worten als A9, A14, A16.",
    "**Hölzel Naturwissenschaften HAK II** S. 42–61: Verbrennung von Magnesium in Teilschritten → Teil 1 + A3; Energiediagramm mit Katalysator → Teil 4; V1.9 Brausetabletten → K1.3-V8; V1.10 Eisen in Kupfersulfat → K1.3-V4; drei Merksätze zu Redox → Merkhilfe.",
    "**Expedition Chemie 4** (Theorie S. 34–43, Praxisteil): vier Stellschrauben, Merkhilfe ex = Exit, Kältemischung, Wärmekissen, Glühwürmchen/Knicklicht; Praxisteil V3.1 (Oberfläche) vereinfacht → V8, V3.3 (Eisensalz) → Variante in V7, V4.1 → V4, V4.2 → V5, V4.3 → V6; Perspektivenwechsel Streusalz → Fachwissen/Schlussfolgerung V6.",
    "**Westermann Chemie** S. 34–35: Eisenwolle auf der Waage → K1.3-V1 (Jahresplan V2.15), Kupferbrief → K1.3-V3.",
    "**Treffpunkt Chemie Arbeitsheft** S. 27: Oxidation früher/heute, Magnesium mit Sauerstoff und Chlor → A2, A3.",
    "**Oberstufenbücher** (Redoxgleichungen aufstellen, Oxidationszahlen, Komproportionierung) – nur als Hintergrund, zu schwer für den 2. Jahrgang.",
    "**Jahresplan v33:** Versuche V2.10–V2.17 geprüft; V2.12 (Kältepack/Wärmekissen-Kurven) und V2.14 (Redoxreihe mit Silbernitrat) nicht übernommen (Zeit, Thermometer, Silbernitrat).",
    "**Prüfbericht ChatGPT v4 (24.10.2026):** 29 Punkte nachgeprüft und in v3 umgesetzt bzw. begründet anders gelöst; Quellen u. a. IUPAC Gold Book (exothermic, inhibitor), RSC »What causes iron to rust?«, BASF (Katalysator-Aufbau), NASA/ESA (Hydrazinzersetzung), Carl Roth (Dichte H₂O₂, M CuSO₄·5H₂O).",
    "**Internet (geprüft 24.10.2026):** studyflix-Videos (Redox 4:50, exo/endo 2:30, Katalysator 4:09); Northwestern University 19.08.2025 und ingenieur.de zur Iridium-Ersatz-Studie (mit Toyota Research Institute) → A21; wien.orf.at 18.03.2026 Katalysator-Diebe → A22.",
    "**Geprüft ohne Übernahme:** El-Mo-Experimente, Chemie muss stimmen 7–8, Expedition Physik 4 (kein passender Inhalt mit Inventar-Material).",
]
