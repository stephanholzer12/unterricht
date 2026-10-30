"""Theorie-Seite K2.1 Formen der Landwirtschaft: Teile und Folien. Dieselben Daten bauen die Theorie-Folien der TH-Lehrer-/TH-Kadetten-PPP
und die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag im Schulbuch).
Alles in eigenen Worten; Grafiken selbst gezeichnet (skizzen.py). Lesestopps je Stunde: siehe plan.py (Wortzahl → Lesezeit, ca. 120 Wörter/min)."""
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Zwei Äpfel im Supermarkt", "pill": "Buch S. 38",
  "blocks": [("tiles", [("Apfel A", ["**Bio**, aus Neuseeland", "etwa 18 000 km Transport"]), ("Apfel B", ["**konventionell**, aus der Steiermark", "etwa 150 km Transport"])]),
             ("ul", ["Welcher ist »besser für die Umwelt«? Entscheide dich – per Handzeichen.", "Und vor allem: **Welche Angaben fehlen dir**, um das wirklich zu sagen?"]),
             ("hint", "Leitfrage der Einheit: " + I.LEITFRAGE)]},
 {"id": "s0b", "title": "Mythos-Check: »Bio ist chemiefrei«", "pill": "Buch S. 42",
  "blocks": [("tiles", [("Was viele meinen", ["Bio heißt: keine Chemie, keine Spritzmittel, nichts Künstliches."]),
                        ("Was stimmt", ["Alles besteht aus Chemie – auch Mist und Kompost. Bio **verbietet bestimmte** Mittel (z. B. Mineral-Stickstoffdünger, Gentechnik), erlaubt aber andere unter Auflagen."])]),
             ("hint", "Heute geht es um die Frage: Was unterscheidet die Formen der Landwirtschaft wirklich?")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Teil 1 · Stunde 1
 ("teil1", "Stunde 1 · " + I.wann(1) + " · Buch S. 38–43", I.TEILNAME[1], [
  {"id": "acker", "title": "Der Acker – ein Ökosystem, das wir steuern", "pill": "Buch S. 39",
   "blocks": [("ul", ["Einen **Acker** gibt es nur, weil wir ihn bewirtschaften – er ist ein Agrarökosystem. Ohne Pflügen, Säen und Ernten würden sich nach und nach andere Pflanzen ansiedeln – bei uns wäre daraus irgendwann Wald. Diese natürliche Abfolge heißt **Sukzession**.",
                      "Mit jeder **Ernte** holen wir **Biomasse** vom Feld – und damit die Nährstoffe, die darin stecken (vor allem Stickstoff, Phosphor, Kalium). Sie müssen ersetzt werden, sonst wird der Boden mit den Jahren ärmer. Das gilt für **jede** Form der Landwirtschaft.",
                      "Der Boden ist mehr als Dreck: Poren für Wasser und Luft, Humus, Regenwürmer und Mikroben. Schwere Maschinen auf nassem Boden pressen die Poren zusammen (**Bodenverdichtung**). Liegt der Boden nackt, tragen Regen und Wind die fruchtbare Schicht ab (**Erosion**)."]),
              ("img", "img/acker.png", "Schnitt durch einen Acker: Getreide, darunter Boden mit Poren, Humus und Regenwurm. Ein Pfeil zeigt die Ernte, die Nährstoffe vom Feld mitnimmt, ein zweiter Pfeil Dünger, Mist und Leguminosen, die Nährstoffe zurückbringen. Zusätzlich Pfeile für Verdichtung und Erosion.", "Eigene Zeichnung: Was das Feld verlässt, muss zurück."),
              ("merke", "Ernte nimmt Nährstoffe mit – **Ertrag und Bodenschutz** muss man gemeinsam planen.")]},
  {"id": "formen", "title": "Drei Formen im Vergleich", "pill": "Buch S. 41–43",
   "blocks": [("hint", "Das Buch unterscheidet drei Formen (S. 41). Verglichen wird nach vier Merkmalen: **Boden**, **Dünger und Pflanzenschutz**, **Kulturen**, **Tiere**."),
              ("table", [["Merkmal", "konventionell", "integriert", "biologisch"],
                         ["Boden", "unterschiedlich bearbeitet, Schutz ist Pflicht", "nach Bedarf bearbeitet", "Humus und Bodenleben im Mittelpunkt"],
                         ["Dünger und Pflanzenschutz", "Mineral- und Wirtschaftsdünger, zugelassene Spritzmittel", "erst beobachten, dann gezielt", "**kein** Mineral-Stickstoff, nur erlaubte Bio-Mittel"],
                         ["Kulturen", "Fruchtfolge oder wenige Kulturen", "standortgerechte Sorten", "vielfältige Fruchtfolge, **Leguminosen**"],
                         ["Tiere", "gesetzliche Mindeststandards", "keine eigene Regel", "mehr Platz, Auslauf, Bio-Futter"]]),
              ("ul", ["**Wichtig:** Viele Maßnahmen gibt es in allen drei Formen. Auch konventionelle Betriebe nutzen Fruchtfolge, Hecken oder bodenschonende Bearbeitung.",
                      "»Integriert« ist vor allem ein **Vorgehen** beim Pflanzenschutz (siehe Teil 2). Seine Grundsätze sind in der EU für **alle** Betriebe vorgeschrieben – es ist also keine eigene, streng getrennte dritte Welt. Das Hühnerbeispiel im Buch (Käfig – Boden – Freiland) ist eine Vereinfachung.",
                      "**Hecken** bremsen den Wind und sind Lebensraum für Nützlinge. Eine **Bodenuntersuchung** zeigt, wie viel Dünger wirklich fehlt – so wird nicht zu viel gedüngt.",
                      "**Leguminosen** (Bohnen, Erbsen, Klee) leben mit Knöllchenbakterien zusammen, die Stickstoff aus der Luft binden. So düngen sie auch die nächste Pflanze – andere Nährstoffe wie Phosphor liefern sie aber nicht."]),
              ("merke", "Vergleiche **konkrete Regeln und Maßnahmen** – nicht Etiketten.")]},
  {"id": "bio", "title": "Was Bio genau heißt", "pill": "Buch S. 42–43",
   "blocks": [("tiles", [("Verboten", ["Mineral-Stickstoffdünger (»Kunstdünger«)", "Gentechnik", "chemisch-synthetische Spritzmittel (bis auf wenige Ausnahmen)", "Käfighaltung"]),
                         ("Erlaubt / verlangt", ["Mist, Kompost, Leguminosen", "bestimmte Mittel unter Auflagen, z. B. Pflanzenjauchen oder Kupfer im Wein- und Obstbau", "Platz, Auslauf, Bio-Futter", "regelmäßige **Kontrolle** (meist jedes Jahr)"])]),
              ("ul", ["Kranke Tiere werden auch bei Bio behandelt. Routinemäßig vorbeugend Antibiotika zu geben ist in der EU **überall** verboten – auch konventionell.",
                      "Bio heißt also **nicht** »stofffrei« und auch nicht »garantiert ohne jede Rückstände«. Es heißt: strengere Regeln, die kontrolliert werden."])]},
  {"id": "dok", "title": "Ein Versuch, der seit 1978 läuft", "pill": "Ergänzung",
   "blocks": [("ul", ["In der Schweiz (Therwil bei Basel) vergleicht ein Forschungsinstitut seit **1978** auf denselben Feldern biologische und konventionelle Bewirtschaftung – dazu eine Kontrollfläche, die gar nicht gedüngt wird. Jede Variante liegt mehrmals nebeneinander, damit Zufall und Bodenunterschiede auffallen.",
                      "Ergebnis über viele Jahre: Die Bio-Flächen brachten **im Schnitt rund 20 % weniger Ertrag**, hatten aber mehr Bodenleben. Je nach Kultur war der Unterschied sehr verschieden – bei Weizen kleiner, bei Kartoffeln größer.",
                      "Der Agrarforscher **Urs Niggli** hat dieses Institut lange geleitet und über den Versuch viel veröffentlicht."]),
              ("hint", "Ein Mittelwert aus einem Versuch ist keine Regel für jeden Bio-Betrieb.")]},
  {"id": "stop1", "title": "Stopp – kannst du das?", "pill": "Buch S. 38–43", "blocks": [("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgaben 1 und 2", "aufgaben.html#name"),
 ]),

 # ---------------------------------------------------------------- Teil 2 · Stunde 2 (nach dem Test)
 ("teil2", "Stunde 2 · " + I.wann(2) + " · nach dem Test · Buch S. 43–47", I.TEILNAME[2], [
  {"id": "pflanzenschutz", "title": "Schädlinge, Nützlinge, drei Methoden", "pill": "Buch S. 44",
   "blocks": [("ul", ["Ein **Schädling** ist kein »böses« Tier – er heißt so, weil er **uns** Ertrag oder Vorräte wegfrisst (z. B. Kartoffelkäfer, Blattläuse, Kornkäfer). Ein **Nützling** frisst oder parasitiert Schädlinge (z. B. Marienkäfer, Schlupfwespen, Vögel)."]),
              ("tiles", [("mechanisch", ["absammeln, hacken, Netze, Striegel", "**+** kein Mittel nötig", "**–** viel Arbeit, auf großen Flächen schwer"]),
                         ("biologisch", ["Nützlinge fördern oder aussetzen, Hecken, Blühstreifen", "**+** wirkt dauerhaft", "**–** langsamer, braucht Lebensraum und den richtigen Zeitpunkt"]),
                         ("chemisch", ["zugelassene Pflanzenschutzmittel", "**+** schnell, große Fläche", "**–** trifft oft auch Nützlinge; bei häufigem Einsatz **Resistenz**"])]),
              ("ul", ["**Integrierter Pflanzenschutz** heißt: zuerst vorbeugen (Fruchtfolge, robuste Sorten), dann das Feld beobachten und erst eingreifen, wenn der Befall die **Schadschwelle** überschreitet – also wenn die Bekämpfung mehr bringt, als sie kostet. Ziel ist ein tragbarer Befall, nicht die Ausrottung."]),
              ("merke", "Erst **vorbeugen und beobachten**, dann die passende Methode wählen.")]},
  {"id": "kennzeichnung", "title": "Was die Verpackung verrät – und was nicht", "pill": "Buch S. 43, 47",
   "blocks": [("tiles", [("EU-Bio-Logo", ["Pflicht auf verpackten Bio-Lebensmitteln aus der EU (bei Importen freiwillig)", "darunter **Kontrollstellen-Code** (z. B. AT-BIO-301) und Herkunft: »EU-«, »Nicht-EU-« oder »EU-/Nicht-EU-Landwirtschaft« oder ein Land"]),
                         ("AMA-Biosiegel", ["rot-weiß mit »Austria«: Rohstoffe aus Österreich – höchstens ein Drittel von anderswo, wenn es die Zutat hier nicht gibt (z. B. Vanille)", "schwarz-weiß: bio, Herkunft offen"]),
                         ("Verbände", ["z. B. Bio Austria, Demeter – oft strengere Regeln als das EU-Minimum"])]),
              ("ul", ["Ein Bio-Zeichen sagt etwas über die **Produktionsregeln**. Es sagt **nicht**, dass das Produkt aus der Nähe kommt, gesünder schmeckt oder die beste Klimabilanz hat.",
                      "»EU-Landwirtschaft« heißt nur: irgendwo in der EU. Wo der Rohstoff gewachsen ist und wo er verarbeitet wurde, kann verschieden sein.",
                      "Preise nur **pro gleicher Menge** vergleichen (€ pro kg oder Liter, steht am Regaletikett). Hofladen oder Markt heißen nicht automatisch bio.",
                      "Ob ein Bio-Produkt klimafreundlicher ist, hängt auch vom **Ertrag** ab: Wächst pro Hektar weniger, kann ein Vorteil pro Fläche pro Kilogramm wieder verschwinden. Ohne Daten weiß man es nicht (mehr dazu in Teil 3)."])]},
  {"id": "stop2", "title": "Stopp – kannst du das?", "pill": "Buch S. 43–48", "blocks": [("reveal", I.STOPPFRAGEN[2])]},
  ("jetzt", "Jetzt: Aufgaben 3 und 4", "aufgaben.html#card_a3"),
 ]),

 # ---------------------------------------------------------------- Teil 3 · Stunde 3
 ("teil3", "Stunde 3 · " + I.wann(3) + " · Buch S. 45–46 und Ergänzung", I.TEILNAME[3], [
  {"id": "bezug", "title": "Pro Hektar oder pro Kilogramm?", "pill": "Buch S. 46 · Ergänzung",
   "blocks": [("ul", ["Ertrag misst man in **dt/ha**: 1 dt (Dezitonne) = 100 kg, 1 ha (Hektar) = 10 000 m², also 100 m × 100 m – etwa 1,4 Fußballfelder.",
                      "Hat Bio pro Hektar weniger Dünger- und Spritzmittelbedarf, ist das ein Vorteil **pro Fläche**. Ist der Ertrag kleiner, braucht man für **dieselbe Menge** Essen mehr Fläche. Wer pro Kilogramm rechnet, kann deshalb zu einem anderen Ergebnis kommen.",
                      "So rechnest du: **Fläche = Erntemenge : Ertrag**. Beispiel mit anderen Zahlen: 60 dt Gerste bei 50 dt/ha → 60 : 50 = **1,2 ha**; bei 30 dt/ha → 60 : 30 = **2 ha**.",
                      "Achtung beim Umdrehen: 20 % weniger Ertrag (100 → 80) heißt **25 %** mehr Fläche, denn 100 : 80 = 1,25."]),
              ("img", "img/flaeche.png", "Zwei Felder nebeneinander als Rechtecke: links 1 ha für 80 dt Weizen, rechts 2,22 ha für dieselben 80 dt. Hinweis: alte deutsche Durchschnittswerte 2015/16.", "Eigene Zeichnung zu Aufgabe 5: dieselbe Erntemenge, verschiedene Fläche."),
              ("hint", "Die Zahlen in Aufgabe 5 sind ältere deutsche Mittelwerte (2015/16) – keine heutigen österreichischen Werte. Für einen fairen Vergleich müssen Kultur, Ort und Jahr zusammenpassen.")]},
  ("jetzt", "Jetzt: Aufgabe 5", "aufgaben.html#card_a5"),
  {"id": "sof", "title": "Science oder Fiction? Der Dino aus dem Labor", "pill": "Einstieg",
   "blocks": [("ul", ["Im Film **Jurassic Park** holen Forscher Dino-DNA aus Mücken in Bernstein und füllen die Lücken mit Frosch-DNA – fertig ist der Dinosaurier.",
                      "**Fiction:** DNA zerfällt mit der Zeit; nach rund 66 Millionen Jahren ist davon nichts Brauchbares übrig. **Ein bisschen Science:** Dass man DNA an einer bestimmten Stelle gezielt ändern kann, ist heute Alltag im Labor – mit der Genschere."])]},
  {"id": "gene", "title": "Gene, Züchtung, Gentechnik", "pill": "Buch S. 45",
   "blocks": [("ul", ["Die **DNA** ist die Erbinformation. Ein **Gen** ist ein Abschnitt darauf, der die Bauanleitung z. B. für ein Protein enthält; alle Gene zusammen bilden das **Genom**. Jede Pflanze hat Gene – auch die Bio-Tomate.",
                      "Viele Eigenschaften (z. B. Ertrag) hängen von **vielen Genen und der Umwelt** ab. Ein einzelnes »Ertragsgen«, das alles regelt, gibt es nicht."]),
              ("table", [["Verfahren", "Wie entsteht die Veränderung?", "Danach"],
                         ["Kreuzungszüchtung", "Erbanlagen zweier Eltern werden neu gemischt", "beste Nachkommen auswählen"],
                         ["Mutationszüchtung", "Strahlung oder Chemikalien lösen **zufällige** Veränderungen aus", "brauchbare Pflanzen suchen"],
                         ["klassische Gentechnik (Transgenese)", "ein zusätzliches Gen wird eingebaut, oft aus einer anderen Art (z. B. NK603-Mais)", "prüfen und zulassen"],
                         ["Genschere", "eine **ausgewählte** Stelle wird gezielt verändert", "prüfen und auswählen"]]),
              ("hint", "Gentechnisch veränderte Lebensmittel (GVO) müssen in der EU gekennzeichnet werden; »Gentechnik-frei erzeugt« ist ein eigenes Zeichen (Buch S. 45).")]},
  {"id": "genschere", "title": "Die Genschere in vier Schritten", "pill": "Buch S. 45 · Nobelpreis 2020",
   "blocks": [("img", "img/genschere.png", "Vier Bilder nebeneinander: 1 Die Leit-RNA legt sich an die passende DNA-Stelle. 2 Das Protein Cas9 schneidet beide DNA-Stränge. 3 Die Zelle repariert den Schnitt; die Stelle ist danach verändert. 4 Prüfen: Labor und Feldversuch.", "Eigene Modellzeichnung – keine echte Zelle sieht so aus."),
              ("ol", ["**Ziel finden:** Die **Leit-RNA** passt wie ein Schlüssel zu einer ausgewählten DNA-Stelle und führt Cas9 dorthin. Manchmal schneidet Cas9 auch an ähnlichen Stellen – auch darum wird später geprüft.",
                      "**Schneiden:** **Cas9** ist ein Protein, das die DNA an dieser Stelle durchschneidet.",
                      "**Reparieren:** Die Zelle flickt den Schnitt. Dabei entstehen oft kleine Veränderungen; gibt man eine Vorlage mit, kann man auch eine gewünschte Änderung einbauen.",
                      "**Prüfen:** Ob wirklich das Gewünschte passiert ist und ob die Pflanze im Feld taugt, zeigen erst Labortests und Feldversuche."]),
              ("ul", ["Nicht jede Anwendung baut fremde DNA ein. Präziser heißt aber **nicht automatisch risikofrei** – geprüft wird das Ergebnis, nicht nur die Methode.",
                      "Kleine Veränderungen sieht man im Labor oft, aber man kann nicht immer erkennen, **wie** sie entstanden sind – dieselbe Veränderung kann auch von selbst auftreten."]),
              ("video", "moder"),
              ("hint", "Geschichte: Emmanuelle Charpentier und Jennifer Doudna haben die Genschere 2012 als Werkzeug beschrieben – 2020 bekamen sie dafür den Nobelpreis für Chemie."),
              ("merke", "**Ziel finden – schneiden – reparieren – prüfen** gehören zusammen.")]},
  {"id": "sorte", "title": "Eine neue Sorte beurteilen", "pill": "Buch S. 45 · Ergänzung",
   "blocks": [("tiles", [("Bringt sie, was sie verspricht?", ["Vergleich mit einer normalen Sorte, **an mehreren Orten** und **über mehrere Jahre**; kann der Pilz die Abwehr mit der Zeit überwinden?"]),
                         ("Lebensmittel und Umwelt", ["Inhaltsstoffe, Allergene, Wirkung auf Nützlinge, Auskreuzen in Wildpflanzen"]),
                         ("Wirtschaft", ["Wem gehört das Patent? Was kostet das Saatgut? Dürfen Bauern nachbauen?"])]),
              ("ul", ["Biologische und wirtschaftliche Fragen **getrennt** beantworten: Ein teurer Lizenzvertrag macht eine Pflanze nicht giftig – und eine harmlose Pflanze löst kein Preisproblem.",
                      "**Neues EU-Recht:** Seit 16. Juli 2026 gibt es eine EU-Verordnung für Pflanzen aus neuen Gentechniken wie der Genschere; angewendet wird sie ab **17. Juli 2028**. Bis dahin gelten die alten Gentechnik-Regeln. Im Biolandbau bleiben solche Pflanzen verboten."]),
              ("hint", "Gesetzesnummern und Daten musst du nicht auswendig können."),
              ("merke", "Nicht die Methode allein beurteilen – sondern die **konkrete Pflanze**, ihre Nutzung und die Bedingungen.")]},
  {"id": "stop3", "title": "Stopp – kannst du das?", "pill": "Buch S. 45–46", "blocks": [("reveal", I.STOPPFRAGEN[3])]},
  ("jetzt", "Jetzt: Aufgaben 6 und 7", "aufgaben.html#card_a6"),
 ]),

 # ---------------------------------------------------------------- Teil 4 · Stunde 4
 ("teil4", "Stunde 4 · " + I.wann(4) + " · Ergänzung zu Buch S. 45", I.TEILNAME[4], [
  {"id": "seralini", "title": "Der Versuch von 2012", "pill": "Ergänzung · Studie 2012",
   "blocks": [("table", [["Steckbrief", ""],
                         ["Wer, wann?", "der französische Forscher Gilles-Éric Séralini und Kollegen, 2012"],
                         ["Was?", "Ratten bekamen zwei Jahre lang gentechnisch veränderten Mais (NK603) und/oder ein Spritzmittel (Roundup) – in verschiedenen Mischungen; je Geschlecht **1 Kontrollgruppe** gegen 9 Behandlungsgruppen"],
                         ["Wie viele?", "**200 Ratten**, aufgeteilt auf 2 Geschlechter und 10 Gruppen → nur **10 Tiere je Geschlecht und Gruppe**"],
                         ["Behauptung", "mehr Tumore und frühere Todesfälle – mit Fotos von Ratten mit großen Tumoren"],
                         ["Danach", "2013 von der Zeitschrift zurückgezogen, 2014 in einer anderen Zeitschrift wieder veröffentlicht"]]),
              ("img", "img/gruppen.png", "200 Punkte werden zuerst in Männchen und Weibchen geteilt, dann in je 10 Gruppen zu je 10 Tieren.", "Eigene Zeichnung: Die große Gesamtzahl versteckt kleine Gruppen."),
              ("ul", ["Der verwendete Rattenstamm bekommt **im Alter oft von selbst Tumore**. Das allein macht ihn nicht ungeeignet – bei nur 10 Tieren pro Gruppe kann der **Zufall** aber große Unterschiede erzeugen.",
                      "Die **EFSA** (EU-Behörde für Lebensmittelsicherheit) kritisierte Aufbau, Auswertung und Darstellung: Die Schlüsse über Tumore seien so nicht belegt."])]},
  {"id": "studie", "title": "Woran man eine gute Studie erkennt", "pill": "Ergänzung",
   "blocks": [("table", [["Prüffrage", "Warum?"],
                         ["Was genau wurde untersucht?", "Mais, Spritzmittel und Futtermischung sind verschiedene Dinge – nicht vermischen."],
                         ["Wie groß sind die einzelnen Gruppen?", "Eine große Gesamtzahl kann kleine Gruppen verstecken."],
                         ["Gibt es eine passende **Kontrollgruppe**?", "Nur der Vergleich zeigt, was ohne die Behandlung passiert wäre."],
                         ["Zufällig verteilt und **verblindet**?", "Sonst beeinflussen Erwartungen das Ergebnis."],
                         ["Vorher festgelegt, was gemessen wird?", "Wer viel misst, findet zufällig immer irgendeinen Unterschied."],
                         ["Wie weit reicht das Ergebnis?", "Es gilt nur für das, was wirklich geprüft wurde."]]),
              ("ul", ["Wer eine Studie bezahlt hat, muss offengelegt werden – das ersetzt aber nicht die Prüfung der Methode. Dieselben Fragen passen auch bei Sportprodukten oder Diät-Tipps."])]},
  {"id": "gtwyst", "title": "Was die große Folgestudie zeigte", "pill": "Ergänzung · Steinberg 2019",
   "blocks": [("ul", ["Die EU ließ die Frage neu untersuchen: Das Projekt **G-TwYST** (2019) fütterte Ratten zwei Jahre lang mit demselben NK603-Mais – angebaut mit und ohne Roundup –, diesmal mit **50 Tieren je Geschlecht und Gruppe**.",
                      "Ergebnis: **keine schädliche Wirkung**, die auf das Verfüttern dieses Maises zurückging.",
                      "Was das **nicht** heißt: dass alle Gentech-Pflanzen, alle Genschere-Pflanzen oder jedes Spritzmittel in jeder Menge harmlos sind. Und Séralinis Versuch war schwach gemacht – ein Beweis für Betrug ist das nicht."]),
              ("merke", "Eine schwache Methode ist **kein Betrugsbeweis** – und eine gute Folgestudie ist **kein Freibrief** für alles.")]},
  {"id": "stop4", "title": "Stopp – kannst du das?", "pill": "Ergänzung", "blocks": [("reveal", I.STOPPFRAGEN[4])]},
  ("jetzt", "Jetzt: Aufgaben 8 und 9", "aufgaben.html#card_a8"),
 ]),
]

SCHNELLE = [
 {"id": "partnercheck", "title": "Partnercheck – Karten zum Wiederholen", "pill": "Buch S. 38–46",
  "blocks": [("hint", "Zu zweit: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken (Aufgabe 13)."), ("karten", I.PARTNERKARTEN)]},
 {"id": "versorgung", "title": "Versorgungssicherheit: Was, wenn Nachschub fehlt?", "pill": "Buch S. 40, 46",
  "blocks": [("ul", ["Österreich erzeugt manche Lebensmittel in größerer Menge, als es selbst braucht (z. B. Milch, Rindfleisch), bei anderen deutlich weniger (z. B. Obst, Gemüse, pflanzliche Öle). Wie viel genau, zeigt Statistik Austria jedes Jahr als **Selbstversorgungsgrad**.",
                     "Landwirtschaft braucht selbst Nachschub: Diesel, Dünger, Saatgut, Futter, Strom. Fällt etwas davon aus – Blackout, Krieg, Lieferstopp –, merkt man das am Acker und im Regal.",
                     "Für Krisenvorsorge (auch für das Bundesheer) zählt darum nicht nur der Ertrag, sondern auch: Lager, kurze Wege, mehrere Lieferanten."]),
             ("hint", "Recherche für Neugierige: Suche »Versorgungsbilanz Statistik Austria« – wie hoch ist der Selbstversorgungsgrad bei Getreide und bei Gemüse?")]},
 {"id": "geschichte", "title": "Wie alles anfing: vom Sammeln zum Mähdrescher", "pill": "Buch S. 40",
  "blocks": [("ul", ["In der **Jungsteinzeit** wurden Menschen in mehreren Weltregionen unabhängig voneinander zu Bauern und sesshaft (**Neolithische Revolution**).",
                     "Maschinen, Mineraldünger und Pflanzenschutz haben die Erträge im 20. Jahrhundert stark erhöht – weniger Menschen arbeiten heute in der Landwirtschaft. Die **Grüne Revolution** brachte ertragreiche Sorten in ärmere Länder.",
                     "Trotzdem gibt es Hunger: Essen muss auch **verteilt** und **bezahlbar** sein. Mehr Ertrag allein löst das nicht."])]},
 {"id": "offen", "title": "Was weiß die Forschung noch nicht?", "pill": "Ausblick",
  "blocks": [("ul", ["Welche Mischung aus Ertrag, Bodenschutz und wenig Dünger und Spritzmitteln an einem **bestimmten Ort** am besten funktioniert, ist oft offen – Langzeitversuche wie der seit 1978 sind deshalb so wertvoll.",
                     "Wie sich Pflanzen aus der Genschere über viele Jahre im Feld verhalten, wird man erst mit der Zeit sehen. Darum gibt es Prüfungen und Regeln."])]},
 ("jetzt", "Zu den Zusatzaufgaben 10–13", "aufgaben.html#card_a10"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Acker", "teil2": "Teil 2 · Pflanzenschutz", "teil3": "Teil 3 · Ertrag, Genschere", "teil4": "Teil 4 · Studien",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

if __name__ == "__main__":
    import re
    for pid, _, _, items in PARTS:
        for it in items:
            if isinstance(it, dict):
                txt = " ".join((x if isinstance(x, str) else " ".join(str(y) for y in x)) for b in it["blocks"] if b[0] in ("ul", "ol", "table", "tiles", "merke", "hint") for x in (b[1] if isinstance(b[1], list) else [b[1]]))
                print(f"{pid:9s} {it['id']:15s} {len(re.findall(r'[A-Za-zÄÖÜäöüß]+', txt)):4d} Wörter")
