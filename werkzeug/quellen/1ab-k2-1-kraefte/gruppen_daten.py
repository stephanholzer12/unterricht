"""Gruppenkarten K2.1 Mechanische Kräfte (v2, 11.11.2026) – EINE Quelle für Arbeitsblatt, Unterrichts-PPP und Lösungsmappe.
Stephans Idee vom 11.11.2026: Die Themen sind fest (sieben Gruppen), den Versuch wählt jede Gruppe selbst – mit Material aus dem
NAWI-Saal oder von zu Hause. Die Gruppen erarbeiten ihr Thema selbst (Leitfragen, Buch, Theorie-Seite, Video), bereiten Versuch und
Präsentation vor und schreiben einen Steckbrief (Handout) für die Klasse. Prof. HOLZER macht nur Stunde 1 mit der ganzen Klasse.
Saal-Material: jede Zeile gegen NAWI_Material_und_Inventar.xlsx (Blatt »Lehrmittelbestand«) geprüft, Stand 11.11.2026 – Bestand rechnerisch, nicht gezählt.
Die Versuchsideen sind Vorschläge zum Starten, keine Pflicht. Die erste Idee jeder Gruppe ist der bisher geplante Versuch (v1) und ist erprobt beschrieben
in versuche_daten.py (dort Material, Platz, Beispielwerte für die Lösungsmappe)."""

THEMEN = {1: "Bewegung", 2: "Gewichtskraft", 3: "Auftrieb", 4: "Reibung", 5: "Kapillarwirkung", 6: "Druck", 7: "Kraft und Gegenkraft"}

# Saal-Material: (Bezeichnung, Inventar-Nr., Bestand laut Inventar)
_KM = [("Federkraftmesser 10 N (braun)", "#51", 1), ("Federkraftmesser 10 N / 0,2 N", "#52", 1), ("Digitaler Kraftmesser", "#26", 1)]
_WAAGE = [("Schulwaage 620 g / 0,1 g", "#128", 5)]

G = {
 1: {"thema": "Bewegung", "titel": "Bewegung: Geschwindigkeit und Beschleunigung", "buch": "Buch S. 46–48", "teil": "bewegung", "karte": "k2",
     "leit": ["Was ist der Unterschied zwischen Tempo (Schnelligkeit) und Geschwindigkeit? Warum gehört eine Richtung dazu?",
              "Wie berechnest du die mittlere Schnelligkeit? Nenne die Formel mit Einheiten und rechne 10 m/s in km/h um.",
              "Was heißt »beschleunigen« in der Physik? Nenne drei verschiedene Fälle.",
              "Wo braucht man das im Sport, im Straßenverkehr oder beim Bundesheer? Ein Beispiel mit Zahl."],
     "ideen": ["Normal gehen auf 5 m abgemessener Strecke, Zeit stoppen, dreimal wiederholen und v = s / t berechnen (auch in km/h).",
               "Eine Kugel oder ein Spielzeugauto rollt eine schräge Unterlage hinunter: Zeit für die erste und die zweite Hälfte vergleichen.",
               "Handy-Video mit Zeitlupe: ein Ball rollt gleichmäßig und einmal schneller werdend – Abstände in gleichen Zeitabständen vergleichen."],
     "saal": [("Bandmaß 20 m", "#9", 1), ("Bandmaß 3 m", "#10", 1), ("Gelbe Schnur 50 m (Markierung)", "#57", 1)],
     "haus": "Murmel oder Spielzeugauto, ein Brett oder ein großer Karton als schräge Bahn, Malerkrepp für Markierungen.",
     "formel": "v = s / t (m/s; mal 3,6 ergibt km/h)",
     "achtung": "Nur gehen, nicht laufen. Den Gang nur nach Freigabe durch Prof. HOLZER benutzen."},
 2: {"thema": "Gewichtskraft", "titel": "Masse und Gewichtskraft", "buch": "Buch S. 49–51", "teil": "gewicht", "karte": "k3",
     "leit": ["Was ist der Unterschied zwischen Masse und Gewichtskraft? Welche Einheit hat jede der beiden Größen?",
              "Was bedeutet g in der Formel Gewichtskraft = Masse · g? Berechne die Gewichtskraft eines Rucksacks mit 8 kg.",
              "Warum ist ein Kadett am Mond »leichter«, obwohl seine Masse gleich bleibt?",
              "Wie funktioniert ein Federkraftmesser? Erkläre in zwei Sätzen."],
     "ideen": ["Mehrere Gegenstände zuerst auf der Waage (Masse) und dann am Kraftmesser (Kraft) messen. Prüft in einer Tabelle, ob die Kraft in N ungefähr Masse in kg mal 10 ist.",
               "Einen Becher mit 100 ml und mit 200 ml Wasser an den Kraftmesser hängen und vergleichen.",
               "Einen eigenen Kraftmesser aus einem Gummiring bauen und mit dem Gewichtssatz eichen (Dehnung in cm notieren)."],
     "saal": _KM + _WAAGE + [("Gewichtssatz 10 mg bis 100 g", "#59", 1), ("Messbecher mit Henkel 250 ml", "#87", 1), ("Messbecher mit Henkel 500 ml", "#88", 1)],
     "haus": "Gummiringe, ein kleiner Beutel oder Becher mit Henkel, Gegenstände bis etwa 500 g.",
     "formel": "F_G = m · g (N; m in kg; g = 10 N/kg)",
     "achtung": "Kraftmesser langsam belasten, höchstens bis zum Ende der Skala (10 N)."},
 3: {"thema": "Auftrieb", "titel": "Auftrieb: sinken, schweben, schwimmen", "buch": "Buch S. 52–53", "teil": "auftrieb", "karte": "k4",
     "leit": ["Was ist die Auftriebskraft und in welche Richtung wirkt sie?",
              "Was sagt das Prinzip von Archimedes? Erkläre es in eigenen Worten.",
              "Wann sinkt, schwebt oder schwimmt ein Körper? Vergleiche Gewichtskraft und Auftriebskraft.",
              "Warum schwimmt ein Schiff aus Stahl? Ein Beispiel aus Sicherheit oder Rettung (z. B. Schwimmweste)."],
     "ideen": ["Einen Gegenstand am Kraftmesser zuerst in Luft und dann ganz unter Wasser messen. Der Unterschied ist die Auftriebskraft.",
               "Ein Gefäß mit Wasser steht auf der Waage. Einen Finger oder Stab eintauchen und die Anzeige beobachten.",
               "Knetboot: Eine Kugel aus Knete sinkt, dieselbe Knete als Schiffchen schwimmt. Masse vorher wiegen."],
     "saal": _KM + _WAAGE + [("Aufbewahrungswanne tief", "#7", 7), ("Zylinder gleichen Volumens (5 Stück)", "#171", 5), ("Messbecher mit Henkel 500 ml", "#88", 1)],
     "haus": "Knete, Alufolie, kleine Steine, eine leere Plastikflasche.",
     "formel": "F_A = Gewichtskraft des verdrängten Wassers · ruhiges Schwimmen: F_A = F_G",
     "achtung": "Wasser nur in der Wanne, Waage und Handys trocken halten, Verschüttetes sofort aufwischen."},
 4: {"thema": "Reibung", "titel": "Reibung hilft und bremst", "buch": "Buch S. 54–56", "teil": "reibung", "karte": "k5",
     "leit": ["Was ist Reibung? Erkläre Haftreibung und Gleitreibung mit je einem Beispiel.",
              "Wovon hängt die Reibungskraft ab? Nenne zwei Einflüsse.",
              "Wo ist Reibung nützlich, wo stört sie? Je ein Beispiel.",
              "Warum ist ein gutes Schuhprofil beim Marsch oder im Sport wichtig?"],
     "ideen": ["Einen Becher mit Wasser am Kraftmesser waagrecht über den Tisch ziehen: Kraft beim Losreißen und beim gleichmäßigen Ziehen vergleichen.",
               "Dieselbe Schachtel auf drei Unterlagen ziehen (Tisch, Papier, Stoff) – sonst alles gleich lassen.",
               "Schuhe mit verschiedenem Profil auf einer schrägen Unterlage: Ab welcher Neigung rutscht welcher Schuh?"],
     "saal": _KM + _WAAGE + [("Messbecher mit Henkel 500 ml", "#88", 1)],
     "haus": "Federschachtel oder kleiner Karton, Stoff, Schleifpapier, zwei Schuhe mit verschiedenem Profil, ein Brett.",
     "formel": "keine Pflichtformel · beim gleichmäßigen Ziehen gilt: Zugkraft ungefähr gleich Gleitreibung",
     "achtung": "Waagrecht und langsam ziehen, nicht reißen. Unter 5 N bleiben."},
 5: {"thema": "Kapillarwirkung", "titel": "Kapillarwirkung und Oberflächenspannung", "buch": "Buch S. 57", "teil": "kapillar", "karte": "k6",
     "leit": ["Was bedeuten Kohäsion und Adhäsion? Erkläre den Unterschied.",
              "Was ist Kapillarwirkung? Warum steigt Wasser in engen Räumen (Papier, Röhrchen) nach oben?",
              "Was ist Oberflächenspannung? Ein Beispiel aus der Natur.",
              "Wo begegnet dir Kapillarwirkung im Alltag oder in der Natur? Zwei Beispiele (z. B. Handtuch, Funktionsshirt, Pflanze, Erde)."],
     "ideen": ["Filterpapier-Streifen in Wasser stellen und die feuchte Grenze nach 10, 30 und 60 Sekunden markieren.",
               "Küchenrolle als Brücke zwischen einem vollen und einem leeren Glas – wie weit wandert das Wasser in 15 Minuten?",
               "Eine Büroklammer vorsichtig auf Wasser legen, sodass sie liegen bleibt (Oberflächenspannung)."],
     "saal": [("Filterpapier 50 × 55 mm (100 Stück)", "#54", 100), ("Griffin-Becher 50 ml", "#62", 1), ("Petrischale Glas ø 80 mm", "#106", 7),
              ("Tropfpipette PE 3 ml (50 Stück)", "#156", 50), ("Aufbewahrungswanne tief", "#7", 7)],
     "haus": "Küchenrolle, zwei Gläser oder Plastikbecher, Büroklammern, Lebensmittelfarbe.",
     "formel": "keine Pflichtformel",
     "achtung": "Nur Wasser und Lebensmittelfarbe. Glas nur aus dem Saal und vorsichtig verwenden."},
 6: {"thema": "Druck", "titel": "Druck: Kraft auf eine Fläche", "buch": "Buch S. 58–60", "teil": "druck", "karte": "k7",
     "leit": ["Was ist Druck? Nenne die Formel p = F / A mit Einheiten (Pa, bar).",
              "Warum sinkt man mit Schneeschuhen weniger ein, und warum schneidet ein scharfes Messer besser?",
              "Was passiert in einer verschlossenen Spritze, wenn du drückst? Unterschied zwischen Luft und Wasser.",
              "Warum spürt man beim Tauchen Druck in den Ohren?"],
     "ideen": ["Spritze ohne Nadel: vorne zuhalten und drücken – einmal mit Luft, einmal mit Wasser gefüllt.",
               "Fläche einer Schuhsohle auf Karopapier auszählen und den Druck beim Stehen auf einem und auf zwei Beinen ausrechnen. Rechnet mit einer gewählten Masse von 70 kg – keine echte Körpermasse eintragen.",
               "Glas oder Becher randvoll mit Wasser, eine Postkarte darauf, umdrehen (über der Wanne): Die Karte bleibt – warum?"],
     "saal": [("Kunststoffspritze 50 ml (ohne Nadel)", "#77", 4), ("Luftballone (50 Stück)", "#84", 50), ("Aufbewahrungswanne tief", "#7", 7),
              ("Messbecher mit Henkel 250 ml", "#87", 1)],
     "haus": "Postkarte, Plastikbecher, Karopapier, ein Paar Schuhe.",
     "formel": "p = F / A (Pa = N/m²; 1 bar = 100 000 Pa)",
     "achtung": "Spritze nie auf Personen richten, nicht mit Gewalt drücken. Wasser nur über der Wanne."},
 7: {"thema": "Kraft und Gegenkraft", "titel": "Kraft und Gegenkraft", "buch": "Buch S. 45, 61", "teil": "gegenkraft", "karte": "k8",
     "leit": ["Was sagt das Wechselwirkungsprinzip (Kraft und Gegenkraft)?",
              "Warum heben sich Kraft und Gegenkraft nicht gegenseitig auf?",
              "Ein Buch liegt auf dem Tisch: Was ist ein Kräftegleichgewicht, was ein Wechselwirkungspaar?",
              "Erkläre den Rückstoß an einem Beispiel (Rakete, Rudern, Absprung oder Rückstoß einer Waffe)."],
     "ideen": ["Zwei Kraftmesser mit den Haken ineinander hängen und ruhig ziehen – vergleicht beide Anzeigen bei 1, 2 und 3 N.",
               "Ballon-Rakete: Strohhalm auf eine gespannte Schnur fädeln, aufgeblasenen Ballon daran kleben und loslassen.",
               "Auf einem Skateboard oder Rollbrett einen schweren Ball wegstoßen – nur sitzend, langsam und mit Freigabe."],
     "saal": _KM[:2] + [("Luftballone (50 Stück)", "#84", 50), ("Gelbe Schnur 50 m", "#57", 1)],
     "haus": "Strohhalme, Klebeband, eventuell ein Rollbrett.",
     "formel": "F_1 = −F_2 (gleich groß, entgegengesetzt, auf zwei verschiedene Körper)",
     "achtung": "Ballon nicht in Richtung von Personen loslassen. Rollbrett nur sitzend und nur mit Freigabe."},
}

# Apolin-Videos zu den drei Newton'schen Gesetzen (Links von Stephan, 12.11.2026; YouTube ist von Claudes Umgebung aus gesperrt –
# Stephan hat die Videos ausgewählt und kennt sie, Inhalt und Länge prüft er selbst). Nur verlinkt, nicht eingebettet.
NEWTON = {
 1: {"titel": "1. Newtonsches Grundgesetz", "kurz": "Trägheit", "url": "https://www.youtube.com/watch?v=Y9sN0rgIyJY",
     "fragen": ["Was macht ein Körper, auf den keine resultierende Kraft wirkt?", "Nenne ein Beispiel aus dem Video, bei dem die Trägheit spürbar wird."]},
 2: {"titel": "2. Newtonsches Grundgesetz", "kurz": "F = m · a", "url": "https://www.youtube.com/watch?v=GHo2PI5Cgkg",
     "fragen": ["Wie hängen Kraft, Masse und Beschleunigung zusammen?", "Was passiert mit der Beschleunigung, wenn die Masse doppelt so groß ist und die Kraft gleich bleibt?"]},
 3: {"titel": "3. Newtonsches Grundgesetz", "kurz": "Kraft und Gegenkraft", "url": "https://www.youtube.com/watch?v=zPKRoT3JTNQ",
     "fragen": ["Auf welche Körper wirken Kraft und Gegenkraft?", "Warum heben sie sich trotzdem nicht auf?"]},
}
QUELLE_NEWTON = "Martin Apolin (YouTube)"

# Videos je Gruppe: zuerst die passenden Apolin-Videos, bei Gruppe 7 zusätzlich der kurze Pohl-Versuch (TIB AV-Portal, geprüft 11.11.2026).
VIDEOS = {
 1: [("Apolin: " + NEWTON[1]["titel"] + " (" + NEWTON[1]["kurz"] + ")", NEWTON[1]["url"], QUELLE_NEWTON, NEWTON[1]["fragen"]),
     ("Apolin: " + NEWTON[2]["titel"] + " (" + NEWTON[2]["kurz"] + ")", NEWTON[2]["url"], QUELLE_NEWTON, NEWTON[2]["fragen"])],
 2: [("Apolin: " + NEWTON[2]["titel"] + " (" + NEWTON[2]["kurz"] + ")", NEWTON[2]["url"], QUELLE_NEWTON, NEWTON[2]["fragen"])],
 4: [("Apolin: " + NEWTON[1]["titel"] + " (" + NEWTON[1]["kurz"] + ")", NEWTON[1]["url"], QUELLE_NEWTON, NEWTON[1]["fragen"])],
 7: [("Apolin: " + NEWTON[3]["titel"] + " (" + NEWTON[3]["kurz"] + ")", NEWTON[3]["url"], QUELLE_NEWTON, NEWTON[3]["fragen"]),
     ("Action = Reaction (Pohl-Versuch, IWF Göttingen, 2003)", "https://av.tib.eu/media/30463",
      "1 min · englisch gesprochen, die Bilder genügen · Lizenz CC BY-ND 3.0 DE · TIB AV-Portal", [])],
}

ROLLEN = ["Leitung und Zeit", "Quellen und Video", "Versuch und Material", "Schriftführung (Steckbrief, Teams)", "Präsentation und Probe"]

# Regeln für Material von zu Hause (Sicherheit) – stehen im Arbeitsblatt, auf der PPP-Folie und in der Lösungsmappe
ZUHAUSE_JA = ["Dinge aus Kunststoff, Papier, Karton, Holz und Stoff", "Wasser, Speisesalz, Lebensmittelfarbe", "Knete, Gummiringe, Strohhalme, Klebeband",
              "Spielzeugauto, Murmel, Ball, Schuhe"]
ZUHAUSE_NEIN = ["Feuer, Kerzen, Feuerzeug", "Chemikalien, Reinigungs- und Spülmittel, Spraydosen", "Glas von zu Hause, Messer, Nägel, Spitzes",
                "Strom aus der Steckdose, Akkus, Powerbanks", "Druckbehälter, Feuerwerk, Waffen oder Waffenteile", "Lebensmittel zum Essen, Tiere"]

FREIGABE_FRAGEN = ["Passt der Versuch zu eurem Thema und zeigt er etwas, das man sehen oder messen kann?",
                   "Ändert ihr nur EINE Sache – und bleibt alles andere gleich?",
                   "Steht jedes Material auf der Liste – mit »Saal« oder »von zu Hause« und wer es mitbringt?",
                   "Ist alles harmlos? (Liste »erlaubt / nicht erlaubt«)",
                   "Schafft ihr den Versuch in der Präsentation in höchstens einer Minute?"]

STECKBRIEF = [["kern", "a) Das Wichtigste in drei Sätzen"],
              ["begriffe", "b) Drei bis fünf Fachbegriffe mit Bedeutung"],
              ["formel", "c) Formel mit Einheiten (oder »keine Formel«)"],
              ["versuch", "d) Unser Versuch in zwei Sätzen: Was haben wir gemacht, was sieht man?"],
              ["alltag", "e) Ein Beispiel aus Sport, Bundesheer oder Alltag"],
              ["frage", "f) Eine Kontrollfrage für die Klasse – mit Antwort"],
              ["quelle", "g) Unsere Quellen: Buchseite und eine zweite Quelle (Wer? Datum?)"]]

RASTER = [("Inhalt", 3, "Die Leitfragen sind fachlich richtig und in eigenen Worten beantwortet."),
          ("Versuch", 2, "Der Versuch passt zum Thema, ist sicher, und Beobachtung und Erklärung sind getrennt."),
          ("Steckbrief", 2, "Vollständig, richtig, verständlich – die anderen können damit lernen."),
          ("Präsentation", 2, "Verständlich, höchstens 3 Minuten, jeder spricht."),
          ("Teamarbeit", 1, "Meilensteine pünktlich (Plan in Stunde 2, Steckbrief in Stunde 4).")]

assert sorted(G) == list(range(1, 8))
assert sum(p for _, p, _ in RASTER) == 10
for _n, _g in G.items():
    assert len(_g["leit"]) == 4 and len(_g["ideen"]) == 3, _n
    assert all(len(x) <= 170 for x in _g["leit"]), _n
