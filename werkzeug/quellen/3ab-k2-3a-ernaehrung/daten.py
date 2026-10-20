"""Aufgaben NAWI 3AB · K2.3a Ernährungsweisen (Buch S. 68–72) – aus PPP 26-27-3AB-K2.1a-Ernaehrungsweisen-Lehrer.pptx
(Stephans alte Kapitelnummer K2.1a; nach dem aktuellen Buch-Schema jetzt K2.3a, Schwesterunit zu K2.3b Trend-Check).
Eine Quelle für Handy-Arbeitsblatt, Word (AB/Loesung) und PPP. Bei Auswahlfeldern steht die richtige Antwort
an erster Stelle; die Anzeige wird gemischt (außer f[3] is False = feste Reihenfolge)."""

STAND = "20.10.2026"

FORMEN = ["vegan", "Pescetarier", "lakto", "Flexitarier", "ovo", "Vollwert", "ovolakto"]
SJT = ["falsch", "teilweise", "stimmt"]
STUFEN = ["Stufe 1+2 (sehr empfehlenswert)", "Stufe 3 (weniger empfehlenswert)", "Stufe 4 (nicht empfehlenswert)"]

T = [
 {"id": "a1", "nr": 1, "title": "Ernährungs-Coach", "src": "Buch S. 69–70", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Wähle für jede Person: Was läuft bei ihrer Ernährung schief – und welche 3 Tipps gibst du ihr?",
  "type": "multi",
  "fields": [["lisa", "Lisa, schwanger: „Ich esse jetzt für zwei! Und abends ein Glas Wein.“ – deine 3 Tipps"],
             ["markus", "Markus, Heeressportler: „Zwei Riesenportionen am Tag, beim Training Energydrinks.“ – deine 3 Tipps"],
             ["opa", "Opa Franz, 84: „Ich trink kaum was, hab eh keinen Durst. Mittags Schweinsbraten.“ – deine 3 Tipps"],
             ["tim", "Tim, 15: „Kein Frühstück, mittags Pommes mit Cola, Obst mag ich nicht.“ – deine 3 Tipps"]],
  "chk": {"lisa": {"kw": [["kein Alkohol/Zigaretten", "alkohol|zigaretten|wein"], ["nicht für zwei essen", "zwei|240|1000|wenig mehr|mehrbedarf"]]},
          "markus": {"kw": [["Nährstoffdichte/mehrere Mahlzeiten", "nährstoffdichte|mehrere|kleine mahlzeiten"], ["Wasser statt Energydrinks", "wasser|saft|tee|energydrink"]]},
          "opa": {"kw": [["Trinken ohne Durst", "trinken|durst|wasser"], ["weniger Fett/seltener Schweinsbraten", "fett|schweinsbraten|selten"]]},
          "tim": {"kw": [["Frühstück/mehrere Mahlzeiten", "frühstück|mahlzeit"], ["Wasser statt Cola, Obst/Gemüse", "wasser|cola|obst|gemüse|vollkorn"]]}},
  "sol": [["Lisa, schwanger", ["Nicht für zwei essen – nur ca. 1.000 kJ (≈ 240 kcal) mehr pro Tag", "Kein Alkohol, keine Zigaretten", "Koffein nur eingeschränkt"]],
          ["Markus, Heeressportler", ["Mehrere kleine Mahlzeiten statt Riesenportionen", "Auf Nährstoffdichte achten", "Wasser, verdünnte Säfte oder Tees statt Energydrinks"]],
          ["Opa Franz, 84", ["„Trinken ohne Durst“ üben", "Braucht weniger Energie – Fett einsparen, Schweinsbraten nur selten"]],
          ["Tim, 15", ["Energie auf mehrere Mahlzeiten verteilen – Frühstück nicht auslassen", "Wasser statt Cola, wenig Fett und Süßes, täglich Obst, Gemüse und Vollkorn"]]],
  "tip": ["Lernseite Teil 1 · Personengruppen", "theorie.html#teil1"]},

 {"id": "a2", "nr": 2, "title": "Wer bin ich?", "src": "Buch S. 70–71", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Ordne jede Ich-Aussage der passenden Ernährungsform zu.",
  "type": "multi",
  "fields": [["s1", "„Nur Pflanzen – sogar Honig lasse ich weg.“", FORMEN],
             ["s2", "„Statt Fleisch esse ich Fisch.“", FORMEN],
             ["s3", "„Milch und Käse ja, Eier und Fleisch nein.“", FORMEN],
             ["s4", "„Selten Fleisch, viel Gemüse, Obst, Fisch.“", FORMEN],
             ["s5", "„Eier ja, Milchprodukte und Fleisch nein.“", FORMEN],
             ["s6", "„Frisch, natürlich, wenig verarbeitet.“", FORMEN],
             ["s7", "„Eier, Milch, Käse ja – Fleisch nein.“", FORMEN]],
  "chk": {"s1": {"sel": "vegan"}, "s2": {"sel": "Pescetarier"}, "s3": {"sel": "lakto"}, "s4": {"sel": "Flexitarier"},
          "s5": {"sel": "ovo"}, "s6": {"sel": "Vollwert"}, "s7": {"sel": "ovolakto"}},
  "sol": [["Lösung", ["vegan – nur Pflanzliches, auch Honig wird abgelehnt", "Pescetarier – Fisch statt Fleisch",
                      "lakto – + Milch und Milchprodukte", "Flexitarier – selten Fleisch, viel Gemüse, Obst, Fisch",
                      "ovo – + Eier", "Vollwert – möglichst natürlich, frisch, wenig verarbeitet",
                      "ovolakto – + Milch und Eier (größte Gruppe der Vegetarier, als Dauerkost geeignet)"]]],
  "tip": ["Lernseite Teil 2 · Alternative Ernährungsformen", "theorie.html#teil2"]},

 {"id": "a3", "nr": 3, "title": "Speiseplan-Check", "src": "Buch S. 70–71", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Welche Ernährungsform(en) dürfen das Gericht essen – vegan, lakto, ovo, ovolakto, Pescetarier? Nenne alle passenden. Achtung bei Honig und Gelatine!",
  "type": "multi",
  "fields": [["curry", "Gemüsecurry mit Reis"], ["spaetzle", "Käsespätzle (Käse + Ei im Teig)"], ["eierspeis", "Eierspeise mit Brot"],
             ["forelle", "Forelle mit Erdäpfeln"], ["honig", "Honigbrot"], ["gummi", "Gummibärchen (mit Gelatine)"]],
  "chk": {"curry": {"kw": [["alle Formen", "alle|vegan|lakto|ovo|pesc"]]},
          "spaetzle": {"kw": [["ovolakto und Pescetarier", "ovolakto|pesc"]]},
          "eierspeis": {"kw": [["ovo, ovolakto, Pescetarier", "ovo|ovolakto|pesc"]]},
          "forelle": {"kw": [["nur Pescetarier", "pesc"]]},
          "honig": {"kw": [["alle außer vegan", "lakto|ovo|ovolakto|pesc"]]},
          "gummi": {"kw": [["keine Form", "keine|niemand|nein"]]}},
  "sol": [["Gemüsecurry", ["alle Formen"]], ["Käsespätzle (Käse + Ei)", ["ovolakto, Pescetarier"]],
          ["Eierspeise", ["ovo, ovolakto, Pescetarier"]], ["Forelle", ["nur Pescetarier"]],
          ["Honigbrot", ["alle außer vegan – Honig wird bei veganer Kost abgelehnt (Buch S. 70)"]],
          ["Gummibärchen", ["für keine Form – Gelatine wird aus Knochen und Häuten von Schwein oder Rind gewonnen; "
                             "Produkte mit V-Label sind ohne Gelatine, Knochen und Schlachtfette (Buch S. 71)"]],
          ["Diskussion", ["Käse kann mit tierischem Lab hergestellt sein – streng genommen dann nicht vegetarisch."]]],
  "tip": ["Lernseite Teil 2.1 · Vegetarismus", "theorie.html#teil21"]},

 {"id": "a4", "nr": 4, "title": "Fleischlos-Ranking", "src": "Buch S. 70", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Bring die Gründe für Vegetarismus in eine Rangliste (1 = für dich wichtigster Grund). Einigt euch danach zu viert auf eine Top 3. "
       "Gründe: Tiere haben ein Recht auf Leben · Fleisch als religiöses Tabu · Ekel vor toten Tieren · Tierfutter fehlt den Menschen · "
       "Umwelt: Massentierhaltung · Gesundheit: weniger Krankheiten.",
  "type": "multi",
  "fields": [["eigene", "Deine Rangliste (alle 6 Gründe, 1 = wichtigster)"], ["gruppe", "Eure Top 3 zu viert (nach der Diskussion)"]],
  "sol": [["Kein Richtig oder Falsch", ["Es zählt die Begründung.",
          "Hintergrund: Innerhalb von zehn Jahren hat sich die Zahl der vegetarisch bzw. vegan lebenden Menschen in Österreich verdreifacht; "
          "16 % der 15- bis 29-Jährigen essen fleischlos.",
          "Wirtschaftsbezug: Welche Gründe sprechen eine Zielgruppe (15–29-Jährige) in der Werbung besonders an?"]]],
  "tip": ["Lernseite Teil 2.1 · Vegetarismus", "theorie.html#teil21"]},

 {"id": "a5", "nr": 5, "title": "Faktencheck", "src": "Buch S. 71", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Stimmt, teilweise oder falsch? Begründe kurz mit dem, was du über die Bewertung des Vegetarismus weißt.",
  "type": "multi",
  "fields": [["f1", "„Vegetarische Kost ist langweilig.“", SJT, False],
             ["f2", "„Nur viel Fleisch bringt genug Eiweiß.“", SJT, False],
             ["f3", "„Ohne Fleisch lebt man automatisch gesünder.“", SJT, False],
             ["f4", "„Vegan ist für alle Menschen das Beste.“", SJT, False],
             ["begr", "Begründe eine deiner Antworten in 1–2 Sätzen"]],
  "chk": {"f1": {"sel": "falsch"}, "f2": {"sel": "falsch"}, "f3": {"sel": "teilweise"}, "f4": {"sel": "falsch"}},
  "sol": [["f1", ["falsch – abwechslungsreiche (ovo)laktovegetarische Kost ist möglich"]],
          ["f2", ["falsch – Eiweiß auch aus Milch, Eiern, Hülsenfrüchten"]],
          ["f3", ["teilweise – nicht bei Puddingvegetarismus (vor allem Süßes und Mehlspeisen statt Fleisch)"]],
          ["f4", ["falsch – Mangel an Eiweiß, Eisen, Kalzium, Jod möglich; für Säuglinge, Kleinkinder und besondere Gruppen wird abgeraten"]],
          ["Hintergrund", ["Vegetarier haben im Schnitt normale Blutzuckerwerte, geringere Cholesterinwerte und seltener Übergewicht (Buch S. 71)."]]],
  "tip": ["Lernseite Teil 2.1 · Vegetarismus", "theorie.html#teil21"]},

 {"id": "a6", "nr": 6, "title": "Wertstufen-Check", "src": "Buch S. 72", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Ordne jedes Lebensmittel seiner Wertstufe zu.",
  "type": "multi",
  "fields": [["apfel", "Apfel", STUFEN, False], ["vollkorn", "Vollkornbrot", STUFEN, False], ["nuss", "Nüsse", STUFEN, False],
             ["karotte", "Karottenrohkost", STUFEN, False], ["milch", "H-Milch", STUFEN, False], ["wurst", "Extrawurst", STUFEN, False],
             ["mais", "Dosenmais", STUFEN, False], ["pommes", "Pommes frites", STUFEN, False], ["pizza", "Fertigpizza", STUFEN, False],
             ["vitamin", "Vitamintabletten", STUFEN, False]],
  "chk": {"apfel": {"sel": STUFEN[0]}, "vollkorn": {"sel": STUFEN[0]}, "nuss": {"sel": STUFEN[0]}, "karotte": {"sel": STUFEN[0]},
          "milch": {"sel": STUFEN[1]}, "wurst": {"sel": STUFEN[1]}, "mais": {"sel": STUFEN[1]},
          "pommes": {"sel": STUFEN[2]}, "pizza": {"sel": STUFEN[2]}, "vitamin": {"sel": STUFEN[2]}},
  "sol": [["Stufe 1+2 (sehr empfehlenswert)", ["Apfel, Vollkornbrot, Nüsse, Karottenrohkost – roh oder schonend verarbeitet; "
                                               "die Hälfte der täglichen Nahrung sollte so aussehen"]],
          ["Stufe 3 (weniger empfehlenswert)", ["H-Milch, Extrawurst, Dosenmais – nur selten"]],
          ["Stufe 4 (nicht empfehlenswert)", ["Pommes frites, Fertigpizza, Vitamintabletten – übertrieben verarbeitet, nicht essen"]],
          ["Kritik laut Buch", ["Die Einteilung ist nicht ganz unproblematisch – H-Milch etwa ist trotz Stufe 3 eine gute Kalziumquelle."]]],
  "tip": ["Lernseite Teil 2.2 · Vollwerternährung", "theorie.html#teil22"]},

 {"id": "a7", "nr": 7, "title": "Bundesheer-Verpflegung im Feld", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False,
  "q": "Das Bundesheer verpflegt Soldaten im Feld mit der Einmannpackung (EPA). a) Recherchiere: Wie viele kcal hat eine EPA ungefähr, und für wie viele Tage "
       "oder Mahlzeiten ist sie gedacht? b) Vergleiche mit dem Tagesbedarf eines jungen Erwachsenen (ca. 2.200–2.800 kcal, je nach Belastung). "
       "c) Nenne deine Quelle (z. B. bundesheer.at).",
  "type": "multi", "fields": [["kcal", "a) kcal der EPA laut Quelle"], ["vergleich", "b) Vergleich mit dem Tagesbedarf"], ["quelle", "c) Quelle"]],
  "sol": [["Lösung", ["Kein fixer Wert – die EPA-Zusammensetzung ändert sich, und das Bundesheer veröffentlicht die Energiewerte nicht einheitlich online. "
                      "Wichtig ist der Rechenweg: EPA-kcal im Verhältnis zum Tagesbedarf, und ob eine EPA allein für einen vollen Einsatztag reichen würde."]]],
  "tip": ["Recherche: bundesheer.at", "https://www.bundesheer.at"]},
]
