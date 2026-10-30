"""NAWI 3AB · K2.1 Formen der Landwirtschaft (Trauner NAWI HAK 3, S. 38–48) – v2.
Grundlage: ChatGPT-Übergabe »Entwurf-ChatGPT-v1.md« vom 28.10.2026 (Planung, Aufgaben A1–A12 mit Lösungen, Quiz, Quellen) und ChatGPTs
Arbeitsfassung v1 (PPP/Word) – von Claude nach dem Regelwerk (14. Fassung, 29.10.2026) umgesetzt und fachlich nachgeprüft (Prüfbericht).
Jahresplan v24: Einheit 4 (E4), 3 Std. Kern, K03, N02/N03/N05, P1–P5, SDG 2/15, GLV 4. Stephan: 4 Termine, 3AK und 3BK gleich
(Mi 04.11., Mo 09.11., Mi 11.11., Mo 16.11.2026), am 09.11. zuerst der bestehende 1. Test (20 min). Annahme 50 min je Stunde.
Kein Versuch (V3.12 Bodenprobe bleibt spätere Erweiterung). Kein Kahoot (Stephan, 30.10.2026). Eine Quelle für Seiten, Word, PPPs und Lösungsmappe.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "30.10.2026"
V = "v2"                       # v1 = ChatGPT-Arbeitsfassung (28.10.2026)
ORDNER = "3ab-nawi/k2-1-landbau"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "3ab-nawi/"
EYEBROW = "NAWI · 3AB · K2.1 Formen der Landwirtschaft"
TITEL = "Formen der Landwirtschaft – vom Acker bis zur Genschere"
KURZTITEL = "Formen der Landwirtschaft"
BUCH = "Buch S. 38–48"
KEY = "26-27-3AB-K2.1-Landbau-TH-Handy-v1"
CHECK_KEY = "26-27-3AB-K2.1-Landbau-Lernseite-Check-v1"
PRAEFIX = "26-27-3AB-K2.1-Landbau"
KAP = "K2.1"
TEST = "Mo 09.11.2026"

# Medien: (Titel, Quelle, Dauer, Link[, "sim"|"audio"]). Nur geprüfte Links sind freigegeben.
VIDEOS = {
    "moder": ("#167 Erklär mir Gentechnik (Martin Moder)", "Erklär mir die Welt, 1. Juni 2021 · ab 05:39", "ca. 7 min",
              "https://podcasts.apple.com/de/podcast/167-erkl%C3%A4r-mir-gentechnik-martin-moder/id1363234463?i=1000523732893", "audio"),
    # Folgende Links waren von hier aus nicht prüfbar → nicht eingebaut, Liste an Stephan zur Freigabe (Prüfbericht):
    "v35": ("Biologische Schädlingsbekämpfung (Filmtipp im Buch S. 44)", "Trauner-Verlag", "kurz", "https://www.trauner.at/nawi_v35.aspx"),
    "v39": ("Österreichische Landwirtschaft (Filmtipp im Buch S. 46)", "Trauner-Verlag", "kurz", "https://www.trauner.at/nawi_v39.aspx"),
    "niggli": ("#185 Erklär mir nachhaltige Landwirtschaft, Urs Niggli", "Podcast »Erklär mir die Welt«, 2021", "lang", "https://podcasts.apple.com/at/podcast/erkl%C3%A4r-mir-die-welt/id1363234463", "audio"),
}
FREIGEGEBEN = {"moder"}


def zeigen(key, lehrer=False):
    return key in FREIGEGEBEN


KLASSEN = ["3AK", "3BK"]          # gleicher Ablauf, gleiche Termine (Stephan, 30.10.2026)
_D = {1: "Mi 04.11.", 2: "Mo 09.11.", 3: "Mi 11.11.", 4: "Mo 16.11."}
DATEN = {k: dict(_D) for k in KLASSEN}
TEIL_STUNDE = {t: {k: t for k in KLASSEN} for t in (1, 2, 3, 4)}
TEILNAME = {1: "Teil 1 · Acker und Landwirtschaftsformen", 2: "Teil 2 · Pflanzenschutz und Kennzeichnung",
            3: "Teil 3 · Ertrag, Gene und Genschere", 4: "Teil 4 · Was trägt eine Studie?"}
TEILBUCH = {1: "Buch S. 38–43", 2: "Buch S. 43–47", 3: "Buch S. 45–46", 4: "Buch S. 45–46 · Ergänzung"}


def wann(teil=None):
    if teil: return f"3AK und 3BK: {_D[teil]}"
    return "3AK und 3BK: " + " · ".join(_D[t] for t in (1, 2, 3, 4))


# ======================================================================= Aufgaben
# Prüfregeln großzügig: offene Erklärungen »man« (Lehrkraft bewertet), Stichwörter nur als Schreibhilfe.
_KW_BODEN = r"boden|humus|erosion|verdicht|bearbeit|pflug|pflüg|pflueg|struktur|bedeck|zwischenfrucht|schutz"
T = [
 # ======================================================= Teil 1 · Acker und Landwirtschaftsformen (Stunde 1)
 {"id": "a1", "nr": 1, "title": "Landwirtschaftsformen vergleichen", "src": "Buch S. 39, 41–43", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 10,
  "q": "Arbeitsteilig zu zweit: Stephan teilt euch eine Form zu (konventionell, integriert oder biologisch). Wähle sie aus und schreib zu deiner Form je einen kurzen Stichpunkt zu "
       "Boden, Dünger und Pflanzenschutz, Kulturen und Tieren. In der Besprechung füllen wir an der Tafel die ganze Tabelle – fotografiere sie danach und lade das Foto hier hoch. "
       "Achtung: Manche Maßnahmen gibt es in mehreren Formen.",
  "hint": "Stichpunkte reichen. Info: Theorieteil »Drei Formen im Vergleich« und »Was Bio genau heißt«",
  "type": "sketch",
  "fields": [["form", "Unsere Form", ["konventionell", "integriert", "biologisch"], False], ["boden", "Boden"], ["mittel", "Dünger und Pflanzenschutz"], ["kultur", "Kulturen"], ["tiere", "Tiere"]],
  "chk": {"boden": {"kw": [["Bodenbearbeitung oder -schutz", r"boden|humus|erosion|verdicht|bearbeit|pflug|pflüg|pflueg|struktur|bedeck|zwischenfrucht|schutz|bedarf|regenw|kompost|mist"]], "man": True},
          "mittel": {"kw": [["Dünger oder Pflanzenschutz", r"dünger|duenger|mineral|kunstdünger|kunstduenger|mist|gülle|guelle|kompost|jauche|kupfer|spritz|pestizid|mittel|nützling|nuetzling|beobacht|gezielt|bedarf|stickstoff"]], "man": True},
          "kultur": {"kw": [["Fruchtfolge oder Sorten", r"fruchtfolge|monokultur|spezialis|wechsel|sorte|leguminos|hülsen|huelsen|klee|bohne|erbse|vielfalt|vielfält|mischkultur|standort"]], "man": True},
          "tiere": {"kw": [["Haltung", r"gesetz|mindest|standard|regel|platz|auslauf|freiland|weide|futter|stall|licht|stroh|fläche|flaeche|artgerecht|kein|bodenhaltung"]], "man": True}},
  "sol": [["Musterlösung (ganze Tabelle)", ["Konventionell: Boden unterschiedlich bearbeitet, Bodenschutz trotzdem Pflicht · Mineral- und Wirtschaftsdünger, zugelassene Spritzmittel · Fruchtfolge oder Spezialisierung · gesetzliche Mindeststandards, teils höhere Programme.",
                            "Integriert: Bearbeitung nach Bedarf und Bodenzustand · erst beobachten und vorbeugen, chemisch nur gezielt (diese Grundsätze gelten in der EU für alle Betriebe) · standortgerechte Sorten, abgestimmte Fruchtfolge · keine eigene, überall gleiche Tierhaltungsregel.",
                            "Biologisch: Humus, Bodenleben, Fruchtfolge (mechanische Bearbeitung kann auch belasten) · kein Mineral-Stickstoffdünger, keine chemisch-synthetischen Spritzmittel bis auf wenige Ausnahmen · vielfältige Fruchtfolge mit Leguminosen · mehr Platz, Auslauf, Bio-Futter, Kontrolle."]]],
  "fsol": {"form": "zugeteilte Form", "boden": "z. B. bio: Humus, Bodenleben, Fruchtfolge", "mittel": "z. B. bio: kein Mineral-Stickstoff", "kultur": "z. B. bio: Fruchtfolge mit Leguminosen", "tiere": "z. B. bio: Platz, Auslauf, Bio-Futter"},
  "matrix": {"boden": ["unterschiedlich bearbeitet, Bodenschutz Pflicht", "nach Bedarf und Bodenzustand", "Humus, Bodenleben, Fruchtfolge"],
             "mittel": ["Mineral- und Wirtschaftsdünger, zugelassene Spritzmittel", "erst beobachten, dann gezielt", "kein Mineral-Stickstoff, kaum Spritzmittel"],
             "kultur": ["Fruchtfolge oder Spezialisierung", "standortgerechte Sorten, abgestimmte Fruchtfolge", "vielfältige Fruchtfolge, Leguminosen"],
             "tiere": ["gesetzliche Mindeststandards", "keine eigene einheitliche Regel", "mehr Platz, Auslauf, Bio-Futter"]},
  "tip": ["Drei Formen im Vergleich", "theorie.html#formen"],
  "raster": [["Boden", "Dünger und Pflanzenschutz", "Kulturen", "Tiere"], ["konventionell", "integriert", "biologisch"]]},

 {"id": "a2", "nr": 2, "title": "Einen Betrieb beurteilen", "src": "Buch S. 39–43", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 7,
  "q": "Ein konventioneller Betrieb baut abwechselnd Weizen, Ackerbohnen und Gerste an. Er lässt Hecken stehen, untersucht regelmäßig den Boden und spritzt ein zugelassenes Mittel erst, "
       "wenn der Befall zu groß wird. a) Nenne zwei dieser Maßnahmen und was sie jeweils bringen. b) Warum ist der Betrieb damit noch nicht »bio«? (1 Satz) "
       "c) Welche zwei Angaben zur Tierhaltung fehlen dir für ein Urteil? d) Ein Langzeitversuch fand bei Bio im Schnitt rund 20 % weniger Ertrag. Warum gilt das nicht für jeden Bio-Betrieb? (1 Satz)",
  "hint": "Info: Theorieteil »Drei Formen im Vergleich«, »Was Bio genau heißt« und »Ein Versuch, der seit 1978 läuft«",
  "type": "multi",
  "fields": [["schutz", "a) Zwei Maßnahmen und ihre Wirkung"], ["bio", "b) Warum noch nicht bio? (1 Satz)"], ["tier", "c) Zwei fehlende Angaben zur Tierhaltung"], ["ertrag", "d) Warum keine feste Regel? (1 Satz)"]],
  "chk": {"schutz": {"kw": [["zwei Maßnahmen", r"fruchtfolge|hecke|bodenuntersuch|boden untersuch|untersucht|bedarf|befall|schadschwelle|zu groß|zu gross", 2]], "man": True},
          "bio": {"kw": [["Regeln und Kontrolle", r"regel|vorgab|vorschrift|kontroll|zertifi|richtlinie|alle|verordnung|mineral|kunstdünger|kunstduenger|spritz|mittel"]], "man": True},
          "tier": {"kw": [["zwei Angaben", r"platz|auslauf|freiland|weide|futter|fress|stall|haltung|gesund|tierarzt|medikament|antibio|betreu|anzahl|zahl|m²|m2|licht|einstreu|liege", 2]], "man": True},
          "ertrag": {"kw": [["Kultur, Standort oder Jahr", r"kultur|pflanze|standort|boden|klima|wetter|jahr|betrieb|unterschied|durchschnitt|schnitt|mittel|verschieden|versuch"]], "man": True}},
  "sol": [["Musterlösung", ["a) z. B. Fruchtfolge mit Ackerbohnen: Schädlinge und Krankheiten bauen sich weniger auf, die Bohne bringt Stickstoff · Hecken: Lebensraum für Nützlinge, Schutz vor Wind-Erosion · Bodenuntersuchung: nur so viel düngen, wie fehlt · Spritzen erst nach Bedarf: weniger Mittel, weniger Resistenz.",
                            "b) Einzelne gute Maßnahmen ersetzen nicht alle Bio-Vorgaben und die vorgeschriebene Kontrolle – und ob das Mittel bio-erlaubt ist, wissen wir nicht.",
                            "c) z. B. Platz pro Tier, Auslauf, Futter (Herkunft, bio?), Tiergesundheit und Medikamente, Betreuung.",
                            "d) Die 20 % sind ein Mittelwert aus einem Versuch an einem Standort; je nach Kultur, Boden, Wetter und Jahr kann der Unterschied viel kleiner oder größer sein."]]],
  "fsol": {"schutz": "Fruchtfolge (weniger Schädlinge, Bohne bringt Stickstoff) · Hecken (Nützlinge)", "bio": "Einzelmaßnahmen ersetzen nicht alle Bio-Regeln und die Kontrolle",
           "tier": "z. B. Platz und Auslauf, Futter, Tiergesundheit", "ertrag": "Mittelwert eines Versuchs – Kultur, Standort und Jahr verschieden"},
  "tip": ["Drei Formen im Vergleich", "theorie.html#formen"], "besprechen": True},

 # ======================================================= Teil 2 · Pflanzenschutz und Kennzeichnung (Stunde 2, nach dem Test)
 {"id": "a3", "nr": 3, "title": "Blattläuse im Feld", "src": "Buch S. 44", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 6,
  "q": "Auf einem Feld treten Blattläuse auf. Nenne zu jeder Methode eine Wirkung und eine Grenze: a) mechanisch (z. B. absammeln, abspritzen mit Wasser) b) Nützlinge fördern (z. B. Marienkäfer) "
       "c) ein zugelassenes Insektizid. d) Warum ist das Ziel nicht, jede einzelne Laus zu beseitigen? (1 Satz)",
  "hint": "Wirkung = was es bringt. Grenze = wo es nicht reicht oder schadet. Info: Theorieteil »Schädlinge, Nützlinge, drei Methoden«",
  "type": "multi",
  "fields": [["mech", "a) Mechanisch: Wirkung und Grenze"], ["nuetz", "b) Nützlinge: Wirkung und Grenze"], ["chem", "c) Insektizid: Wirkung und Grenze"], ["ziel", "d) Warum nicht jede Laus? (1 Satz)"]],
  "chk": {"mech": {"kw": [["Wirkung", r"entfern|weg|weniger|abs|sammel|direkt|ohne gift|ohne chemie|kein mittel|ohne mittel|schnell"], ["Grenze", r"aufwend|arbeit|zeit|groß|gross|fläche|flaeche|teuer|mühsam|muehsam|schad|beschädig|beschaedig|nicht alle|langsam"]], "man": True},
          "nuetz": {"kw": [["Wirkung", r"fress|frisst|essen|vertilg|dauerhaft|weniger|natürlich|natuerlich|gegenspieler|feind|regul|ohne gift|ohne chemie"], ["Grenze", r"langsam|zeit|dauer|lebensraum|hecke|nicht sofort|nicht alle|wetter|verzöger|verzoeger|zeitpunkt|abhängig|abhaengig|zu spät|zu spaet"]], "man": True},
          "chem": {"kw": [["Wirkung", r"schnell|tötet|toetet|wirkt|weniger|stark|großfläch|grossflaech|zuverlässig|zuverlaessig"], ["Grenze", r"nützling|nuetzling|biene|andere|nebenwirk|resisten|rückst|rueckst|umwelt|wasser|gift|kosten|teuer"]], "man": True},
          "ziel": {"kw": [["Schaden tragbar / Kosten", r"schadschwelle|tragbar|kleiner schaden|wenig schaden|kosten|teuer|lohnt|nützling|nuetzling|futter|nahrung|gleichgewicht|unmöglich|unmoeglich|resisten"]], "man": True}},
  "sol": [["Musterlösung", ["a) Mechanisch: Läuse direkt weg, ohne Mittel · Grenze: viel Arbeit, auf großen Flächen kaum machbar, Pflanzen können leiden.",
                            "b) Nützlinge: fressen die Läuse, wirken dauerhaft · Grenze: wirken langsamer, brauchen Lebensraum (Hecken, Blühstreifen) und den richtigen Zeitpunkt.",
                            "c) Insektizid: wirkt schnell und auf großer Fläche · Grenze: kann auch Nützlinge und Bienen treffen; bei häufigem Einsatz werden Läuse widerstandsfähig (Resistenz).",
                            "d) Ein kleiner Befall kostet weniger, als die Bekämpfung kostet und schadet – ab der Schadschwelle lohnt sich eine Maßnahme. Außerdem brauchen Nützlinge etwas zu fressen."]]],
  "fsol": {"mech": "direkt weg, ohne Mittel · viel Arbeit, große Fläche", "nuetz": "fressen Läuse · langsamer, brauchen Lebensraum", "chem": "schnell · trifft auch Nützlinge, Resistenz",
           "ziel": "kleiner Befall ist tragbar – erst ab der Schadschwelle handeln"},
  "tip": ["Schädlinge, Nützlinge, drei Methoden", "theorie.html#pflanzenschutz"]},

 {"id": "a4", "nr": 4, "title": "Verpackungen und ein KI-Satz", "src": "Buch S. 43, 47", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 9,
  "q": "In Gruppen, zuerst ohne Handy: Vergleicht zwei Verpackungen, die Stephan austeilt. a) Notiert Produkt, Bio-Zeichen (welches?) und den Kontrollstellen-Code (z. B. AT-BIO-…). Steht etwas nicht drauf, schreibt »nicht angegeben«. "
       "b) Notiert die Herkunft der Rohstoffe und den Preis pro kg bzw. pro Liter (steht oft klein am Regaletikett oder rechnet ihn aus). "
       "c) Eine KI hat geschrieben: »Bio ist automatisch regional, pestizidfrei und klimafreundlicher.« Korrigiert die drei Teile stichwortartig.",
  "hint": "Bio-Zeichen sagt etwas über die Produktionsregeln, nicht über die Region. Info: Theorieteil »Was die Verpackung verrät – und was nicht«",
  "type": "multi",
  "fields": [["label", "a) Produkt, Bio-Zeichen, Kontrollstellen-Code"], ["vergleich", "b) Herkunft und Preis pro kg/Liter"], ["ki", "c) Drei Korrekturen zum KI-Satz"]],
  "chk": {"label": {"kw": [["Zeichen oder Code", r"bio|ama|\beu\b|eu-|code|at-bio|kontroll|zeichen|siegel|logo|nicht angegeben"]], "man": True},
          "vergleich": {"kw": [["Herkunft", r"herkunft|österreich|oesterreich|\beu\b|eu-|nicht-eu|nicht eu|land\b|landwirtschaft|region|\baus |nicht angegeben"], ["Preis pro Menge", r"€|euro|\d ?kg|/ ?kg|/ ?l\b|liter|\bpro (kg|liter|l)\b|\bje (kg|liter|l)\b|grundpreis"]], "man": True},
          "ki": {"kw": [["regional", r"region|herkunft|übersee|uebersee|ausland|weit weg|transport|\beu\b|aus aller welt"], ["Pflanzenschutz", r"erlaubt|zugelassen|mittel|kupfer|jauche|pflanzenschutz|nicht pestizidfrei|auch bio|bestimmte"],
                         ["Klima / Bezugsgröße", r"klima|co2|co₂|bilanz|ertrag|fläche|flaeche|pro kg|bezug|transport|daten"]], "man": True}},
  "sol": [["Musterlösung", ["a) hängt von den Verpackungen ab, z. B. EU-Bio-Logo mit Code AT-BIO-301, AMA-Biosiegel – fehlende Angaben als »nicht angegeben« notieren.",
                            "b) Herkunft z. B. »EU-Landwirtschaft«, »Österreich«; nur Preise pro gleicher Menge vergleichen. Rohstoffherkunft und Ort der Verarbeitung können verschieden sein.",
                            "c) Bio ist nicht automatisch regional (Bio-Äpfel können aus Übersee kommen) · nicht pestizidfrei: bestimmte Pflanzenschutzmittel sind auch bio erlaubt · klimafreundlicher nur mit Daten: pro kg kann der geringere Ertrag den Vorteil pro Hektar aufwiegen."]]],
  "fsol": {"label": "je nach Verpackung – fehlende Angaben »nicht angegeben«", "vergleich": "nur Preis pro gleicher Menge; Herkunft ≠ Verarbeitungsort",
           "ki": "nicht automatisch regional · bestimmte Mittel erlaubt · Klima nur mit Daten pro kg"},
  "tip": ["Was die Verpackung verrät – und was nicht", "theorie.html#kennzeichnung"], "besprechen": True},

 {"id": "a5", "nr": 5, "title": "Wie viel Fläche für 8 Tonnen Weizen?", "src": "Buch S. 46 (ha) · Daten: Westermann 2017", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 5,
  "q": "Ältere Durchschnittswerte aus Deutschland (2015/16): Weizen konventionell 80 dt/ha, bio 36 dt/ha (1 dt = 100 kg, 1 ha = 10 000 m²). "
       "Berechne die Fläche für 80 dt Weizen (Rechenweg im Heft, Ergebnis in ha, auf zwei Dezimalstellen gerundet): a) konventionell b) bio. "
       "c) Warum darf man daraus nicht schließen, dass jeder Bio-Acker heute mehr als doppelt so viel Fläche braucht? (1 Satz)",
  "hint": "Fläche = Erntemenge : Ertrag pro ha. Einheit als »ha« schreiben. Info: Theorieteil »Pro Hektar oder pro Kilogramm?«",
  "type": "multi",
  "fields": [["konv", "a) Fläche konventionell (in ha)"], ["bio", "b) Fläche bio (in ha)"], ["bezug", "c) Warum keine allgemeine Regel? (1 Satz)"]],
  "chk": {"konv": {"num": 1, "unit": "ha"}, "bio": {"num": 2.222, "unit": "ha"},
          "bezug": {"kw": [["alt / Ort / Kultur verschieden", r"alt|2015|2016|historisch|früher|frueher|deutschland|land|standort|boden|kultur|jahr|durchschnitt|mittel|heute|unterschied|verschieden|nur weizen"]], "man": True}},
  "sol": [["Musterlösung", ["a) 80 dt : 80 dt/ha = 1,00 ha", "b) 80 dt : 36 dt/ha = 2,22 ha",
                            "c) Das sind alte deutsche Durchschnittswerte für eine Kultur; je nach Land, Boden, Jahr und Kultur ist der Abstand anders – heute und in Österreich können die Zahlen abweichen."]]],
  "fsol": {"konv": "1,00 ha", "bio": "2,22 ha", "bezug": "alte deutsche Durchschnittswerte, eine Kultur – anderswo anders"},
  "tip": ["Pro Hektar oder pro Kilogramm?", "theorie.html#bezug"], "besprechen": True},

 # ======================================================= Teil 3 · Gentechnik und Genschere (Stunde 3)
 {"id": "a6", "nr": 6, "title": "Die Genschere erklären und zeichnen", "src": "Buch S. 45", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 8,
  "q": "a) Was macht die Leit-RNA, was macht Cas9, was macht die Zelle danach? Je 1 kurzer Satz. "
       "b) Vergleiche Kreuzungszüchtung, Mutationszüchtung und Genschere in je einem Satz: Wie entsteht die Veränderung? "
       "c) Zeichnet zu zweit auf dem Mini-Whiteboard die vier Schritte der Genschere (Ziel finden – schneiden – reparieren – prüfen), fotografiert das Bild und ladet es hier hoch.",
  "hint": "Die Zeichnung ist ein Modell – keine Zelle sieht so aus. Info: Theorieteil »Die Genschere in vier Schritten«",
  "type": "sketch",
  "fields": [["rna", "a) Leit-RNA (1 Satz)"], ["cas", "a) Cas9 (1 Satz)"], ["rep", "a) Danach in der Zelle (1 Satz)"],
             ["vergleich", "b) Kreuzung, Mutation, Genschere (je 1 Satz)"]],
  "chk": {"rna": {"kw": [["findet die Zielstelle", r"find|erkenn|such|ziel|stelle|passt|bindet|führt|fuehrt|zeigt|navig|adresse|wegweiser|sequenz"]], "man": True},
          "cas": {"kw": [["schneidet die DNA", r"schneid|schnitt|trenn|zerschneid|schere|cut"]], "man": True},
          "rep": {"kw": [["repariert", r"repar|flick|zusammen|verbind|schließ|schliess|füg|fueg|vorlage"]], "man": True},
          "vergleich": {"kw": [["Kreuzung", r"kreuz|eltern|kombin|misch"], ["Mutation", r"mutation|zufall|zufäll|zufaell|strahl|chemikal"], ["Genschere gezielt", r"gezielt|bestimmte stelle|genau|ausgewählt|ausgewaehlt|ziel|crispr|schere"]], "man": True}},
  "sol": [["Musterlösung", ["Leit-RNA: passt wie ein Schlüssel zu einer ausgewählten DNA-Stelle und führt Cas9 dorthin.",
                            "Cas9: ein Protein, das die DNA an genau dieser Stelle durchschneidet.",
                            "Zelle: repariert den Schnitt; dabei entstehen oft kleine Veränderungen – mit einer mitgelieferten Vorlage auch eine gewünschte. Danach muss man prüfen, was wirklich passiert ist.",
                            "Kreuzung: Erbanlagen zweier Eltern werden neu gemischt, dann die besten Nachkommen ausgewählt · Mutationszüchtung: Strahlung oder Chemikalien erzeugen zufällige Veränderungen, dann auswählen · Genschere: eine ausgewählte Stelle wird gezielt verändert – geprüft und ausgewählt wird auch hier.",
                            "Skizze: vier beschriftete Schritte – Ziel finden (Leit-RNA), schneiden (Cas9), reparieren (Zelle), prüfen (Labor und Feld). Der Schnitt allein ergibt noch keine fertige Sorte."]]],
  "fsol": {"rna": "findet die passende DNA-Stelle", "cas": "schneidet die DNA dort", "rep": "Zelle repariert – oft kleine Veränderung; danach prüfen",
           "vergleich": "Kreuzung mischt · Mutation zufällig · Genschere gezielt – auswählen und prüfen immer"},
  "tip": ["Die Genschere in vier Schritten", "theorie.html#genschere"], "besprechen": True},

 {"id": "a7", "nr": 7, "title": "Eine neue Weizensorte prüfen", "src": "Buch S. 45", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 7,
  "q": "Zu zweit: Eine Firma entwickelt mit der Genschere eine Weizensorte, die weniger oft von einem Pilz befallen wird. a) Was könnte sie bringen? (1 Satz) "
       "b) Formuliere je eine Prüffrage zu Anbau und Ertrag und zu Lebensmittel oder Umwelt. c) Nenne eine wirtschaftliche Frage, die ein Biologe nicht beantworten kann.",
  "hint": "»Könnte« ist noch kein Beweis. Info: Theorieteil »Eine neue Sorte beurteilen«",
  "type": "multi",
  "fields": [["nutzen", "a) Möglicher Nutzen (1 Satz)"], ["anbau", "b) Prüffrage zu Anbau und Ertrag"], ["folgen", "b) Prüffrage zu Lebensmittel oder Umwelt"], ["wirtschaft", "c) Wirtschaftliche Frage"]],
  "chk": {"nutzen": {"kw": [["weniger Verlust / weniger Spritzmittel", r"ertrag|ernte|verlust|weniger|fungizid|spritz|mittel|pilz|gesund|sicher|kosten"]], "man": True},
          "anbau": {"kw": [["Vergleich, Orte, Jahre", r"vergleich|feld|versuch|standort|ort|jahr|ertrag|wetter|klima|boden|wirklich|tatsächlich|tatsaechlich|test"]], "man": True},
          "folgen": {"kw": [["Lebensmittel oder Umwelt", r"inhalt|zusammensetz|lebensmittel|gesund|essen|allerg|nährstoff|naehrstoff|umwelt|insekt|tier|nützling|nuetzling|auskreuz|wild|resisten|boden|nicht.?ziel"]], "man": True},
          "wirtschaft": {"kw": [["Kosten, Lizenz, Abhängigkeit", r"lizenz|patent|preis|kost|teuer|saatgut|nachbau|abhängig|abhaengig|firma|konzern|gewinn|bauer|landwirt|verdien"]], "man": True}},
  "sol": [["Musterlösung", ["a) weniger Ernteverlust und weniger Pilzspritzmittel – möglich, aber erst zu belegen.",
                            "b) z. B. Bringt die Sorte im Vergleich mit einer normalen Sorte an mehreren Orten und über mehrere Jahre wirklich mehr Ertrag? · Kann der Pilz die Abwehr der Sorte mit der Zeit überwinden? · Ist der Weizen genauso zusammengesetzt (Eiweiß, Allergene)? Kreuzt er in verwandte Wildpflanzen aus?",
                            "c) z. B. Wer besitzt das Patent, was kostet das Saatgut, dürfen Bauern selbst nachbauen, werden sie von einer Firma abhängig?"]]],
  "fsol": {"nutzen": "weniger Ernteverlust, weniger Pilzspritzmittel – zu belegen", "anbau": "Vergleich mit normaler Sorte, mehrere Orte und Jahre",
           "folgen": "Zusammensetzung, Allergene, Auskreuzung", "wirtschaft": "Patent, Saatgutpreis, Nachbau, Abhängigkeit"},
  "tip": ["Eine neue Sorte beurteilen", "theorie.html#sorte"]},

 # ======================================================= Teil 4 · Studienkritik (Stunde 4)
 {"id": "a8", "nr": 8, "title": "Séralinis Rattenversuch prüfen", "src": "Buch S. 45 · Ergänzung", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 10,
  "q": "Zu zweit, mit dem Steckbrief im Theorieteil: a) Warum sagt »200 Ratten« allein wenig über die Aussagekraft? (1 Satz) b) Je Geschlecht gab es nur eine Kontrollgruppe mit 10 Tieren. Wozu braucht man sie – und warum sind 10 Tiere dafür wenig? (1–2 Sätze) "
       "c) Der Rattenstamm bekommt im Alter oft von selbst Tumore. Warum ist das bei kleinen Gruppen ein Problem? (1 Satz) "
       "d) Nenne zwei weitere Dinge, die du über den Versuch wissen willst.",
  "hint": "Rechne nach: 200 Ratten, 2 Geschlechter, 10 Gruppen. Info: Theorieteil »Der Versuch von 2012« und »Woran man eine gute Studie erkennt«",
  "type": "multi",
  "fields": [["gruppe", "a) 200 Ratten – warum wenig? (1 Satz)"], ["kontrolle", "b) Kontrollgruppe: wozu – und warum 10 wenig? (1–2 Sätze)"], ["zufall", "c) Spontane Tumore bei kleinen Gruppen (1 Satz)"], ["angaben", "d) Zwei weitere Angaben"]],
  "chk": {"gruppe": {"kw": [["nur 10 pro Gruppe", r"\b10\b|zehn|klein|wenig|verteilt|aufgeteilt|gruppe|pro gruppe|je gruppe"]], "man": True},
          "kontrolle": {"kw": [["Vergleich ohne Behandlung", r"vergleich|ohne|normal|unbehandelt|kein|zufall|von selbst|sowieso|basis|unterschied"]], "man": True},
          "zufall": {"kw": [["Zufall", r"zufall|zufäll|zufaell|schwank|von selbst|sowieso|auch so|ohnehin|unterscheid|ursache|glück|glueck|unsicher|wenig tiere|kleine gruppe"]], "man": True},
          "angaben": {"kw": [["zwei Angaben", r"zufällig|zufaellig|zuteil|verblind|blind|futter|vorher|festgelegt|rohdaten|daten|statistik|wiederhol|geld|finanz|bezahlt|\bwer\b|dosis|menge|wie viel|dauer|\balter|gutacht|kontrollgrupp", 2]], "man": True}},
  "sol": [["Musterlösung", ["a) Die 200 Ratten waren auf 2 Geschlechter und 10 Gruppen verteilt – also nur 10 Tiere je Geschlecht und Gruppe.",
                            "b) Sie zeigt, was ohne die untersuchte Behandlung unter sonst gleichen Bedingungen passiert – erst der Unterschied zählt. Mit nur 10 Tieren schwankt aber schon die Kontrollgruppe selbst stark (bei diesem Stamm bekommen viele Tiere von selbst Tumore).",
                            "c) Bei 10 Tieren kann der Zufall allein große Unterschiede machen; man kann dann nicht trennen, ob ein Tumor vom Futter kommt oder sowieso entstanden wäre.",
                            "d) z. B. Wurden die Tiere zufällig verteilt? Wussten die Prüfer, welche Gruppe sie beurteilen (Verblindung)? Wurde vorher festgelegt, was gemessen wird? Sind alle Rohdaten zugänglich? Wurde der Versuch wiederholt?"]]],
  "fsol": {"gruppe": "nur 10 Tiere je Geschlecht und Gruppe", "kontrolle": "zeigt, was ohne Behandlung passiert – 10 Tiere schwanken stark", "zufall": "Zufall und Wirkung nicht zu trennen",
           "angaben": "z. B. zufällige Zuteilung, Verblindung, vorher festgelegte Messgrößen"},
  "tip": ["Der Versuch von 2012", "theorie.html#seralini"], "besprechen": True},

 {"id": "a9", "nr": 9, "title": "Eine Schlagzeile richtigstellen", "src": "Buch S. 45 · Ergänzung", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 10,
  "q": "Mit der Hand auf Papier: Eine erfundene Schlagzeile lautet »Genmais erzeugt Krebs!«. Schreib eine bessere, sachliche Überschrift und darunter ein Urteil in 4–6 Sätzen. "
       "Verwende: Gruppengröße und Kontrolle, die Kritik der EFSA, was die spätere große Studie gezeigt hat – und was nicht. Unterscheide »schwache Methode« und »bewiesener Betrug«. "
       "Fotografiere das Blatt und lade es hoch; schreib hier deine Überschrift ab.",
  "hint": "Kreativ, aber genau: Eine gute Schlagzeile sagt nicht mehr, als die Daten tragen. Info: Theorieteil »Was die große Folgestudie zeigte«",
  "type": "sketch",
  "fields": [["titel", "Deine Überschrift (abschreiben)"]],
  "chk": {"titel": {"kw": [["sachlich, nicht pauschal", r"nicht|kein|unklar|schwach|zweifel|fraglich|unbewiesen|unsicher|kritik|\?"]], "man": True}},
  "sol": [["Musterlösung", ["Überschrift z. B. »Rattenversuch beweist Krebsgefahr durch Genmais nicht«.",
                            "Urteil: Im Versuch von 2012 waren es nur 10 Ratten je Geschlecht und Gruppe, und der Rattenstamm bekommt oft von selbst Tumore. Der Zufall ist deshalb kaum von einer Wirkung zu trennen. "
                            "Die EFSA kritisierte Aufbau, Auswertung und Darstellung und hielt die Schlüsse für nicht belastbar. Die große EU-Folgestudie G-TwYST (2019, 50 Tiere je Gruppe und Geschlecht) fand beim Verfüttern desselben Maises keine schädliche Wirkung. "
                            "Das gilt aber nur für diesen Mais unter diesen Bedingungen – nicht für alle Gentech-Pflanzen oder jedes Spritzmittel. Eine schwache Methode ist kein Beweis für Betrug.",
                            "Bewertungskriterien: Gruppengröße/Zufall · Kontrolle · Reichweite der Folgestudie begrenzt · keine pauschale Aussage über alle GVO oder Glyphosat · Methode ≠ Betrug."]]],
  "fsol": {"titel": "z. B. »Rattenversuch beweist Krebsgefahr durch Genmais nicht«"},
  "kriterien": ["Gruppengröße und Zufall erklärt", "Kontrolle sinnvoll erklärt", "Folgestudie auf geprüften Mais begrenzt", "keine pauschale Aussage über alle GVO oder Glyphosat", "schwache Methode ≠ Betrug"],
  "tip": ["Was die große Folgestudie zeigte", "theorie.html#gtwyst"], "besprechen": True},

 # ======================================================= Zusatz · Für Schnelle (freiwillig, keine Hausübung)
 {"id": "a10", "nr": 10, "title": "Essen in der Krise", "src": "Buch S. 40, 46 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Eine Großküche (z. B. eine Kaserne) soll auch in einer Krise Kartoffeln bekommen. Betrieb A braucht viel zugekauften Dünger und Diesel. Betrieb B braucht weniger davon, liefert aber nur an einen einzigen Abnehmer. "
       "Nenne für jeden Betrieb eine Schwachstelle und eine Information, die dir für die Entscheidung noch fehlt.",
  "hint": "Denk an Lieferketten: Was passiert, wenn Diesel knapp wird oder der Abnehmer ausfällt? Info: Theorieteil »Versorgungssicherheit: Was, wenn Nachschub fehlt?«",
  "type": "multi",
  "fields": [["resilienz", "Schwachstellen und fehlende Informationen"]],
  "chk": {"resilienz": {"kw": [["Betriebsmittel / Abnehmer", r"dünger|duenger|diesel|treibstoff|energie|zukauf|import|liefer|abnehmer|einzig|abhängig|abhaengig|lager|menge|transport|preis|ausfall"]], "man": True}},
  "sol": [["Musterlösung", ["A hängt von zugekauftem Dünger und Diesel ab; B hängt an einem Abnehmer. Fehlt z. B.: Wie viel liefern sie, wie lange lagerfähig, wie weit ist der Transport, was kostet es, wie lange können sie ohne Nachschub weiterarbeiten? Aus zwei Angaben folgt keine Rangliste."]]],
  "tip": ["Versorgungssicherheit: Was, wenn Nachschub fehlt?", "theorie.html#versorgung"]},

 {"id": "a11", "nr": 11, "title": "Wie sieht Landwirtschaft 2050 aus?", "src": "Buch S. 39–44 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Du darfst einen Betrieb für 2050 planen. Wähle zwei Maßnahmen aus dem Theorieteil (z. B. Leguminosen in der Fruchtfolge, Hecken, Mischkulturen, robuste Sorten), sag, was sie bringen, und nenne eine Bedingung, damit es klappt.",
  "hint": "Bedingung = was muss stimmen (Boden, Klima, Geld, Wissen …). Info: Theorieteil Teil 1 und Teil 3",
  "type": "multi",
  "fields": [["massnahmen", "Zwei Maßnahmen, Wirkung und eine Bedingung"]],
  "chk": {"massnahmen": {"kw": [["zwei Maßnahmen", r"fruchtfolge|leguminos|bohne|klee|hecke|mischkultur|sorte|robust|zwischenfrucht|humus|nützling|nuetzling|sensor|drohne|genschere|bewässer|bewaesser", 2]], "man": True}},
  "sol": [["Musterlösung", ["z. B. Leguminosen in der Fruchtfolge (bringen Stickstoff, weniger Dünger) und Hecken (Nützlinge, weniger Erosion). Bedingung: passender Boden und Standort, Wissen, genug Ertrag, damit sich der Betrieb rechnet."]]],
  "tip": ["Drei Formen im Vergleich", "theorie.html#formen"]},

 {"id": "a12", "nr": 12, "title": "Ein Sport-Pulver prüfen", "src": "Studienkritik · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 4,
  "q": "Werbung: »Unser Pulver macht dich im Sprint schneller.« Schreib drei Fragen auf, die ein guter Versuch beantworten müsste, bevor du das glaubst.",
  "hint": "Dieselben Fragen wie bei Séralini: Vergleich, Zufall, Anzahl, Messung. Info: Theorieteil »Woran man eine gute Studie erkennt«",
  "type": "multi",
  "fields": [["fragen", "Drei Fragen an den Versuch"]],
  "chk": {"fragen": {"kw": [["drei Kriterien", r"vergleich|kontroll|placebo|zufall|zufäll|zufaell|wie viele|anzahl|teilnehm|personen|gleich|training|mess|test|wiederhol|blind|wer bezahlt|finanz|dauer|unabhängig|unabhaengig", 3]], "man": True}},
  "sol": [["Musterlösung", ["z. B. Gab es eine Vergleichsgruppe mit Scheinpulver (Placebo)? Wurde zufällig zugeteilt, und wussten die Sportler nicht, was sie bekommen? Wie viele haben mitgemacht? Gleiches Training? Wurde der Sprinttest vorher festgelegt? Hat jemand Unabhängiger das wiederholt?"]]],
  "tip": ["Woran man eine gute Studie erkennt", "theorie.html#studie"]},

 {"id": "a13", "nr": 13, "title": "Partnercheck", "src": "Buch S. 38–46", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Zu zweit, ohne Handy: A nimmt drei Karten aus dem Abschnitt »Partnercheck« im Theorieteil und liest die Fragen vor. B antwortet, A vergleicht mit der Antwort auf der Karte und hakt ab. "
       "Dann tauscht ihr. Trag ein, mit wem du geübt hast und wie viele deiner drei Antworten gepasst haben.",
  "hint": "Ehrlich zählen – es geht um deine Wiederholung, nicht um Punkte.",
  "type": "multi",
  "fields": [["partner", "Partnercheck mit (Vorname)"], ["richtig", "Davon hat gepasst", ["3 von 3", "2 von 3", "1 von 3", "0 von 3"], False],
             ["unsicher", "Da war ich noch unsicher (Stichwort, freiwillig)"]],
  "opt": ["unsicher"],
  "chk": {"partner": {"kw": [["Name", r"[a-zäöüß]{2,}"]], "man": True}},
  "sol": [["Hinweis", ["Kein Lösungsschlüssel – die Antworten stehen auf den Karten im Theorieteil."]]],
  "tip": ["Partnercheck", "theorie.html#partnercheck"]},
]
assert [t["nr"] for t in T] == list(range(1, 14))
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
assert abs(80 / 80 - T[4]["chk"]["konv"]["num"]) < 1e-9 and abs(80 / 36 - T[4]["chk"]["bio"]["num"]) < 0.001
assert round(80 / 36, 2) == 2.22 and round(100 / 80, 2) == 1.25 and 200 // (2 * 10) == 10

PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
assert PFLICHT == list(range(1, 10))
BESPRECHEN = [t["nr"] for t in T if t.get("besprechen")]

GRP = {1: TEILNAME[1] + " (Buch S. 38–43) · " + wann(1),
       2: TEILNAME[2] + " (Buch S. 43–47) · " + wann(2) + " nach dem Test",
       3: TEILNAME[3] + " (Buch S. 45–46, Ertrag: Ergänzung) · " + wann(3),
       4: TEILNAME[4] + " (Ergänzung zu Buch S. 45) · " + wann(4) + " · PDF-Abgabe",
       0: "Zusatz · Für Schnelle · freiwillig, keine Hausübung"}

LERNZIELE = ["**konventionelle, integrierte und biologische** Landwirtschaft nach Boden, Dünger und Pflanzenschutz, Kulturen und Tierhaltung vergleichen",
             "Angaben auf **Verpackungen** und **Ertragszahlen** prüfen, ohne aus einem Siegel zu viel herauszulesen",
             "erklären, wie die **Genschere (CRISPR/Cas9)** funktioniert, und eine neue Sorte mit Prüffragen beurteilen",
             "bei einer **Studie** Kontrollgruppe, Gruppengröße und Reichweite des Ergebnisses beurteilen"]

LEITFRAGE = "Wie unterscheiden sich Formen der Landwirtschaft wirklich – und woran erkennst du, ob eine Behauptung darüber belegt ist?"
HEUTE_ZIEL = {1: "Konventionell, integriert und bio nach vier Merkmalen vergleichen – nicht nach Etiketten.",
              2: "Pflanzenschutz-Methoden abwägen und Verpackungen richtig lesen.",
              3: "Ertragszahlen richtig rechnen, die Genschere verstehen und eine neue Sorte prüfen.",
              4: "Eine berühmte Studie prüfen und eine Schlagzeile sachlich richtigstellen."}

WICHTIGSTE = ["Ein **Acker** ist ein vom Menschen gemachtes Ökosystem: Mit jeder **Ernte** verlassen Nährstoffe das Feld und müssen ersetzt werden – bei jeder Form der Landwirtschaft.",
              "**Konventionell, integriert und biologisch** unterscheiden sich in Regeln für Boden, Dünger, Pflanzenschutz und Tiere; viele Maßnahmen wie **Fruchtfolge** gibt es in allen drei.",
              "Ein **Bio-Zeichen** garantiert Produktionsregeln und Kontrolle – nicht regionale Herkunft, nicht »ganz ohne Mittel« und nicht automatisch die beste Klimabilanz.",
              "Bei der **Genschere** findet die Leit-RNA die Stelle, **Cas9** schneidet, die Zelle repariert – danach muss die neue Pflanze erst geprüft werden.",
              "Eine **Studie** trägt nur die Schlüsse, die ihr Aufbau erlaubt: Gruppengröße, **Kontrollgruppe** und Reichweite prüfen – und eine schwache Methode ist noch kein Betrug."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Agrarökosystem", "Ökosystem, das durch Landwirtschaft geprägt ist und nur durch menschliche Eingriffe so bleibt (z. B. ein Acker)"],
                ["Biomasse", "alles, was auf einer Fläche lebt und wächst – meist als Trockenmasse gemessen"],
                ["Sukzession", "natürliche Abfolge von Pflanzengesellschaften, die ohne Eingriff auf einer Fläche entsteht – bei uns meist bis zum Wald"],
                ["Bodenverdichtung", "Boden wird durch schwere Maschinen zusammengedrückt; Luft und Wasser kommen schlechter durch"],
                ["Erosion", "Abtrag von fruchtbarem Boden durch Wasser oder Wind"],
                ["Fruchtfolge", "geplanter Wechsel der Pflanzen, die nacheinander auf derselben Fläche wachsen"],
                ["Monokultur", "dieselbe Pflanze wird über Jahre auf derselben Fläche angebaut"],
                ["Leguminosen", "Hülsenfrüchtler wie Bohnen, Erbsen, Klee; leben mit Bakterien zusammen, die Stickstoff aus der Luft binden"],
                ["konventionelle Landwirtschaft", "übliche Landwirtschaft nach den allgemeinen Gesetzen; Mineraldünger und zugelassene Pflanzenschutzmittel sind erlaubt"],
                ["integrierter Pflanzenschutz", "erst vorbeugen und beobachten, dann mehrere Methoden kombinieren; chemisch nur gezielt nach Bedarf – in der EU für alle Betriebe vorgeschrieben"],
                ["biologische (ökologische) Landwirtschaft", "Landwirtschaft nach den EU-Bio-Regeln mit Kontrolle: kein Mineral-Stickstoffdünger, keine Gentechnik, kaum chemisch-synthetische Spritzmittel, mehr Platz und Auslauf für Tiere"],
                ["Schädling / Nützling", "Lebewesen, das aus Sicht des Menschen Ertrag oder Vorräte schädigt / Lebewesen, das Schädlinge frisst oder parasitiert"],
                ["Schadschwelle", "Befallsstärke, ab der eine Bekämpfung mehr bringt, als sie kostet"],
                ["Resistenz", "Schädlinge oder Erreger werden gegen ein Mittel widerstandsfähig, weil die empfindlichen ausgemerzt werden"],
                ["Kontrollstellen-Code", "Code auf Bio-Produkten (z. B. AT-BIO-301), der zeigt, welche Stelle die Bio-Regeln geprüft hat"],
                ["dt/ha", "Dezitonnen pro Hektar: 1 dt = 100 kg, 1 ha = 10 000 m² – Maß für den Ertrag"],
                ["Gen / Genom", "DNA-Abschnitt mit der Information für ein Produkt (z. B. ein Protein) / gesamte Erbinformation eines Lebewesens"],
                ["Mutation", "Veränderung der Erbinformation – von selbst oder ausgelöst"],
                ["Transgenese", "klassische Gentechnik: zusätzliches Erbmaterial wird eingebaut, oft aus einer anderen Art"],
                ["Genschere (CRISPR/Cas9)", "Werkzeug, das eine ausgewählte DNA-Stelle findet (Leit-RNA) und dort schneidet (Cas9); die Zelle repariert danach"],
                ["GVO", "gentechnisch veränderter Organismus"],
                ["Kontrollgruppe", "Vergleichsgruppe ohne die untersuchte Behandlung, sonst unter gleichen Bedingungen"],
                ["Verblindung", "Wer misst oder bewertet, weiß nicht, welche Gruppe er gerade vor sich hat"]]

WEISST_DU_NOCH = {
    2: [("Warum muss auch ein Bio-Acker gedüngt werden?", "Mit jeder Ernte verlassen Nährstoffe das Feld – sie müssen ersetzt werden, bei Bio z. B. mit Mist, Kompost und Leguminosen."),
        ("Ein Betrieb hat Hecken und Fruchtfolge. Ist er damit bio?", "Nein – einzelne Maßnahmen gibt es überall. Bio heißt: alle Bio-Regeln einhalten und kontrolliert werden.")],
    3: [("Was bedeutet der Code AT-BIO-301 auf einer Packung?", "Eine Kontrollstelle hat geprüft, dass nach den Bio-Regeln produziert wurde – über die Region sagt er nichts."),
        ("Warum ist mehr Insektizid nicht automatisch besser?", "Es trifft auch Nützlinge und macht Schädlinge resistent.")],
    4: [("Was macht die Leit-RNA, was macht Cas9?", "Die Leit-RNA findet die passende DNA-Stelle, Cas9 schneidet dort; die Zelle repariert."),
        ("»Die neue Sorte spart Spritzmittel« – ist das schon bewiesen?", "Nein – das muss man mit Feldversuchen an mehreren Orten und über mehrere Jahre prüfen.")],
}

STOPPFRAGEN = {
    1: [("Warum ersetzt Sonnenlicht keinen Dünger?", "Licht liefert Energie, aber keine Nährstoffe wie Stickstoff, Phosphor oder Kalium – die gehen mit der Ernte weg."),
        ("»Bio ist chemiefrei.« Stimmt das?", "Nein – alles besteht aus Chemie, und auch bio sind bestimmte Dünger und Pflanzenschutzmittel erlaubt. Bio verbietet bestimmte Mittel, nicht alle Stoffe.")],
    2: [("Warum ist mehr Insektizid nicht automatisch besser?", "Es trifft auch Nützlinge, kostet mehr und macht Schädlinge schneller resistent – ohne dass der Zusatznutzen das wert ist."),
        ("Ein Produkt hat das EU-Bio-Logo. Kommt es aus Österreich?", "Nicht unbedingt – die Herkunft steht in der Zeile unter dem Logo.")],
    3: [("Ertrag sinkt um 20 %. Wie viel mehr Fläche braucht man für dieselbe Menge?", "100 : 80 = 1,25 – also 25 % mehr Fläche, nicht 20 %."),
        ("Warum ist die neue Sorte nach dem Schnitt noch nicht fertig?", "Man muss erst prüfen, was die Reparatur wirklich verändert hat und wie sich die Pflanze im Feld verhält."),
        ("Hat eine Tomate ohne Gentechnik Gene?", "Ja – jedes Lebewesen hat Gene. »Ohne Gentechnik« betrifft nur, wie die Sorte entstanden ist.")],
    4: [("Warum ist »Die Folgestudie beweist, dass jedes Spritzmittel harmlos ist« falsch?", "Sie hat nur das Verfüttern eines bestimmten Maises unter bestimmten Bedingungen geprüft – nicht jedes Mittel und nicht jede Pflanze."),
        ("Ist eine zurückgezogene Studie automatisch gefälscht?", "Nein – ein Rückzug kann methodische Gründe haben. Für Betrug braucht man eigene Belege.")],
}

PARTNERKARTEN = [("Warum muss ein Acker gedüngt werden?", "Mit der Ernte verlassen Nährstoffe das Feld; sie müssen ersetzt werden – auch bei Bio (Mist, Kompost, Leguminosen)."),
                 ("Nenne die vier Merkmale, nach denen man Landwirtschaftsformen vergleicht.", "Boden, Dünger und Pflanzenschutz, Kulturen (Fruchtfolge), Tierhaltung."),
                 ("Was ist bei Bio verboten?", "Mineral-Stickstoffdünger, Gentechnik, chemisch-synthetische Spritzmittel (wenige Ausnahmen), Käfighaltung."),
                 ("Was bringen Leguminosen?", "Ihre Knöllchenbakterien binden Stickstoff aus der Luft – das düngt auch die nächste Pflanze."),
                 ("Was ist die Schadschwelle?", "Befall, ab dem sich eine Bekämpfung lohnt – darunter wird nichts getan."),
                 ("Was sagt das EU-Bio-Logo nicht?", "Dass das Produkt aus der Region kommt oder die beste Klimabilanz hat."),
                 ("Leit-RNA, Cas9, Zelle – wer macht was?", "Leit-RNA findet die Stelle, Cas9 schneidet, die Zelle repariert."),
                 ("Warum braucht ein Versuch eine Kontrollgruppe?", "Damit man sieht, was ohne die Behandlung passiert – erst der Unterschied zählt.")]

STOLPERSTEINE = [("»Bio = ohne Chemie«", "Auch bio sind bestimmte Dünger und Pflanzenschutzmittel erlaubt. Bio verbietet **bestimmte** Mittel – z. B. Mineral-Stickstoff und Gentechnik –, nicht alle Stoffe."),
                 ("»Integriert = dritte Welt mit eigenen Regeln«", "Integrierter Pflanzenschutz ist ein **Vorgehen** (vorbeugen, beobachten, gezielt handeln), das auch konventionelle Betriebe nutzen. Für Tiere folgt daraus keine eigene Regel – das Hühnerbeispiel im Buch S. 41 ist eine Vereinfachung."),
                 ("Pro Hektar und pro Kilogramm verwechseln", "20 % weniger Ertrag heißt **25 %** mehr Fläche (100 : 80). Alte deutsche Zahlen (2015/16) sind keine heutigen österreichischen Werte."),
                 ("»Genschere = fertige Superpflanze«", "Der Schnitt ist nur Schritt 2 von 4. Die Zelle repariert, und erst Prüfung im Labor und auf dem Feld zeigt, ob die Sorte taugt. Präzise heißt nicht automatisch risikofrei."),
                 ("Studienkritik überziehen", "Methodische Schwächen sind **kein Betrugsbeweis** – und die Folgestudie ist **kein Freibrief** für alle GVO oder jedes Spritzmittel.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite) – aus der ChatGPT-Übergabe, sprachlich vereinfacht
 ("Acker", "Warum müssen auf einem Acker Nährstoffe ersetzt werden?", ["Mit der Ernte verlassen Nährstoffe das Feld.", "Die Ernte nimmt nur Wasser mit.", "Sonnenlicht liefert alle fehlenden Nährstoffe.", "Dünger ersetzt automatisch das Bodenleben."],
  "In der geernteten Biomasse stecken Nährstoffe. Wie viel man ersetzt, muss zum Bedarf passen.", "Buch S. 39"),
 ("Boden", "Was kann passieren, wenn schwere Maschinen über feuchten Boden fahren?", ["Der Boden wird verdichtet, Luft und Wasser kommen schlecht durch.", "Die Artenvielfalt steigt sicher.", "Erosion verschwindet.", "Es entstehen neue Nährstoffe."],
  "Verdichtung drückt die Poren zusammen – Wurzeln, Wasser und Luft kommen schlechter durch.", "Buch S. 39"),
 ("Fruchtfolge", "Wozu ist eine gute Fruchtfolge nützlich?", ["Sie bremst Schädlinge und einseitige Belastung des Bodens.", "Sie ersetzt immer jede Düngung.", "Sie ist bei konventionellen Betrieben verboten.", "Sie erhöht zwangsläufig den Spritzmitteleinsatz."],
  "Wechselnde Pflanzen haben andere Ansprüche und andere Schädlinge – die bauen sich weniger auf.", "Buch S. 41–43"),
 ("Bio", "Welche Aussage zum Pflanzenschutz im Biolandbau stimmt?", ["Bestimmte zugelassene Mittel sind erlaubt.", "Bio verbietet jedes Pflanzenschutzmittel.", "Jeder natürliche Stoff ist in jeder Menge harmlos.", "Das Siegel beweist null Rückstände."],
  "Die Bio-Regeln erlauben nur bestimmte Mittel unter Bedingungen. »Natürlich« heißt nicht ungefährlich.", "Buch S. 42"),
 ("Tierhaltung", "Was hilft dir am meisten, eine Tierhaltung zu beurteilen?", ["Angaben zu Platz, Auslauf, Futter und Tiergesundheit.", "Ob der Hof konventionell oder bio heißt – das genügt.", "Die Größe der Ackerfläche des Betriebs.", "Der Preis des Fleisches im Geschäft."],
  "Eine Bezeichnung allein beschreibt den einzelnen Stall nicht vollständig.", "Buch S. 41–43"),
 ("Kennzeichnung", "Was garantiert ein Bio-Zeichen allein NICHT?", ["Dass das Produkt aus der Region kommt.", "Dass nach Bio-Regeln produziert wurde.", "Dass kontrolliert wurde.", "Dass die Kennzeichnung an Vorgaben gebunden ist."],
  "Produktionsweise und Herkunft sind getrennte Angaben – Herkunftszeile und Kontrollstellen-Code lesen.", "Buch S. 43"),
 ("Pflanzenschutz", "Was passt zum integrierten Pflanzenschutz?", ["Beobachten, vorbeugen und nur bei Bedarf gezielt eingreifen.", "Immer dieselbe Menge spritzen.", "Nützlinge und Schädlinge ausrotten.", "Ein Bio-Siegel ersetzt die Kontrolle des Felds."],
  "Entscheidend sind Befall, erwarteter Schaden und Folgen der Maßnahme.", "Buch S. 44"),
 ("Bezugsgröße", "80 bzw. 36 dt/ha: Welche Fläche braucht die zweite Variante für 80 dt?", ["rund 2,22 ha", "0,45 ha", "genau 1 ha", "36 ha"],
  "80 : 36 = 2,22 ha. Das sind alte deutsche Durchschnittswerte, keine heutigen österreichischen.", "Buch S. 46–47"),
 ("Gene", "Welche Aussage über die Eigenschaften einer Pflanze stimmt?", ["Viele hängen von mehreren Genen und der Umwelt ab.", "Jede hängt nur von einem Gen ab.", "Die Umwelt spielt nie eine Rolle.", "Nur Gentech-Pflanzen haben Gene."],
  "Gene liefern Information; Merkmale entstehen oft aus dem Zusammenspiel vieler Gene mit der Umwelt.", "Buch S. 45 · Ergänzung"),
 ("Genschere", "Welche Reihenfolge beschreibt die Genschere richtig?", ["Leit-RNA findet die Stelle, Cas9 schneidet, die Zelle repariert.", "Cas9 findet die Stelle, die Leit-RNA schneidet, die Zelle repariert.", "Leit-RNA findet die Stelle, Cas9 baut ein fremdes Gen ein – fertig.", "Cas9 schneidet, die Zelle repariert, danach findet die Leit-RNA die Stelle."],
  "Schnitt, Reparatur und danach die Prüfung gehören zusammen.", "Buch S. 45 · Nobelpreis 2020"),
 ("Genschere", "Welche Aussage zur Genschere stimmt?", ["Nicht jede Anwendung baut fremde DNA ein.", "Jede Anwendung baut ein Tiergen ein.", "Weil sie gezielt ist, braucht man keine Prüfung.", "Die Eigenschaften der Pflanze sind egal."],
  "Oft wird nur eine kleine Stelle verändert. Was dabei herauskommt, muss trotzdem untersucht werden.", "Buch S. 45 · Ergänzung"),
 ("Neue Sorte", "Eine Weizensorte soll weniger Pilzbefall haben. Was ist ein guter Beleg?", ["Feldversuche an mehreren Orten über mehrere Jahre.", "Werbung ohne Daten.", "Ein höherer Verkaufspreis.", "Die Bezeichnung »modern«."],
  "Ein Versprechen prüft man mit Vergleichsdaten. Lebensmittel und Umwelt kommen dazu.", "Buch S. 45 · Ergänzung"),
 ("Studie", "Warum reicht »200 Ratten« bei Séralini nicht als Qualitätsmerkmal?", ["Die Gesamtzahl versteckt kleine Vergleichsgruppen.", "Dann braucht man keine Kontrolle.", "Bei Tierversuchen gibt es keinen Zufall.", "Die Zahl zeigt schon die Ursache."],
  "Es waren nur 10 Tiere je Geschlecht und Gruppe.", "Ergänzung · EFSA 2012"),
 ("Zufall", "Der Rattenstamm bekommt im Alter oft von selbst Tumore. Was folgt daraus?", ["Gruppengröße und Auswertung müssen das berücksichtigen.", "Jede Studie mit diesem Stamm ist ungültig.", "Jeder Tumor kommt sicher vom Futter.", "Eine Kontrollgruppe ist verboten."],
  "Der Stamm allein macht eine Studie nicht wertlos – aber bei kleinen Gruppen ist der Zufall kaum von einer Wirkung zu trennen.", "Ergänzung · EFSA 2012"),
 ("Folgestudie", "Was fand die große Folgestudie G-TwYST zum geprüften Mais?", ["Beim Verfüttern keine schädliche Wirkung unter den geprüften Bedingungen.", "Jedes Glyphosat-Mittel ist harmlos.", "Alle Gentech-Pflanzen wurden geprüft.", "Alle CRISPR-Pflanzen wurden untersucht."],
  "Das Ergebnis gilt für diesen Mais unter diesen Bedingungen – kein Pauschalurteil.", "Ergänzung · Steinberg 2019"),
 ("Urteil", "Was belegt eine schwache Methode allein?", ["Dass bestimmte Schlüsse nicht gut abgesichert sind.", "Dass Daten gefälscht wurden.", "Dass das Gegenteil automatisch stimmt.", "Dass man nicht weiterforschen muss."],
  "Schwache Methode, widerlegter Schluss und Betrug sind drei verschiedene Dinge.", "Ergänzung · Studienkritik"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
