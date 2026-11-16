"""NAWI 2AB · K1.5 Säuren und Basen (Trauner NAWI HAK 2, Teil I, Kapitel »Säuren und Basen« S. 53–61 und 65) – v1.
Auftrag Stephan 14.11.2026: Einheit diesmal von Claude ausgearbeitet (statt ChatGPT), 4 Stunden; Stöchiometrie (S. 62–64) wird nicht gemacht.
Jahresplan (NAWI_Jahresplan_2Jg): E8 »Säuren, Basen, Protolyse, Neutralisation, pH-Wert (Laborzyklus 1) – Puffersysteme des Blutes«, 4 Std., K06, K07, N01, N04, P8, SDG 3, SDG 6.
Leitidee »Von sauer bis basisch – und zurück«: Säuren erkennen (Std. 1) → Laugen und Protonen-Pingpong (Std. 2) → pH messen (Std. 3) → Neutralisation und Blut-pH (Std. 4).
Keine Daten auf den Kadetten-Seiten (Standard 13.11.2026). Ein Schülerversuch (K1.5-V1 = Jahresplan V2.18, angepasst), alle Gruppen dasselbe Material; sonst DEMOS.
Demos: K1.5-D1 Rotkraut-Farbenspiel (Buch S. 54–55, = V2.19 als Demo) · K1.5-D2 pH-Meter-Vergleich (während V1) · K1.5-D3 Atemluft und Neutralisation (Buch S. 55, = V2.21 als Demo).
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge).
PDF-Schrift: ⇌ fehlt in der eingebetteten Schrift – in Aufgaben und Lösungen nur → verwenden."""

STAND = "16.11.2026"
V = "v3"
ORDNER = "2ab-nawi/k1-5-saeuren"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "2ab-nawi/"
EYEBROW = "NAWI · 2AB · K1.5 Säuren und Basen"
TITEL = "Von sauer bis basisch – Säuren, Laugen und der pH-Wert"
KURZTITEL = "Säuren und Basen"
BUCH = "Buch S. 53–61, 65"
KEY = "26-27-2AB-K1.5-Saeuren-TH-Handy-v1"
LERNSEITE_KEY = "26-27-2AB-K1.5-Saeuren-Lernseite-Check-v1"
PRAEFIX = "26-27-2AB-K1.5-Saeuren"
KLASSEN = ["2AK", "2BK"]
GRUPPEN = 6            # Stephan 14.11.2026: 6 Gruppen zu viert (ca. 25 Kadetten je Klasse)
STUNDEN = 4

VS = {"K1.5-V1": {"titel": "pH-Detektive: Getränke und Haushalt im Test", "jp": "V2.18 (angepasst: Indikatorpapier statt pH-Meter in den Gruppen)", "stunde": 3, "aufgabe": 6}}
DEMOS = {"K1.5-D1": {"titel": "Rotkraut-Farbenspiel", "jp": "Buch S. 54–55 · Jahresplan V2.19 als Demo (Glasbestand reicht nicht für Gruppen)", "stunde": 1},
         "K1.5-D2": {"titel": "pH-Meter gegen Indikatorpapier", "jp": "Teil von V2.18 – nur 1 pH-Meter (#107)", "stunde": 3},
         "K1.5-D3": {"titel": "Atemluft macht sauer – Natron holt zurück", "jp": "Buch S. 55 · Jahresplan V2.21 als Demo, erweitert um Neutralisation", "stunde": 4}}

# Stundentitel (Stephan 15.11.2026: kreativ und interessant, Fachteil nach dem Doppelpunkt) – EINE Quelle für Fahrplan, Arbeitsblatt, Präsentation, Lösungsseite.
STUNDENTITEL = {1: "Rotkraut lügt nicht: Säuren erkennen",
                2: "Pingpong mit Protonen: Laugen und wer was abgibt",
         3: "pH-Detektive: Wie sauer ist deine Cola wirklich?",
         4: "Sauer gelaufen? Neutralisation und dein Blut beim Sprint"}
STUNDENNAME = {n: f"Stunde {n} · {t}" for n, t in STUNDENTITEL.items()}

SNB = ["sauer", "neutral", "basisch"]

# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 53", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Zwei Fragen zum Start – ohne Punkte, ohne »richtig« oder »falsch«. Entscheide dich einmal. In Stunde 4 schaust du nach, was du heute gedacht hast.",
  "hint": "Einfach tippen, was du vermutest. Deine Antwort bleibt gespeichert.",
  "type": "multi", "vorhersage": True,
  "fields": [["p1", "a) Cola und Zitronensaft: Welches Getränk ist saurer?",
              ["beide etwa gleich sauer", "Zitronensaft ist viel saurer", "Cola ist neutral, nur Zitrone ist sauer"], False],
             ["p2", "b) Ein Spritzer ins Auge: Was ist gefährlicher – eine Säure oder eine Lauge gleicher Stärke?",
              ["die Lauge", "die Säure", "beide sind harmlos"], False]],
  "chk": {},
  "aufloesung": [["p1", "beide etwa gleich sauer", "Im Buch (S. 61) steht Zitronensaft bei pH 2,4 und Cola bei pH 2,8 – nicht einmal eine halbe Stufe auseinander. Mit dem Indikatorpapier sieht man kaum einen Unterschied (VERSUCH in Stunde 3). Genau gerechnet hat Zitronensaft etwa 2,5-mal so viele H₃O⁺-Ionen – »viel saurer« (Faktor 10 und mehr) ist er nicht."],
                 ["p2", "die Lauge", "Laugen zersetzen Fett und Eiweiß und dringen tiefer ins Auge ein als Säuren. Darum: Schutzbrille – und sofort lange mit Wasser spülen."]],
  "sol": [["Auflösung", ["a) etwa gleich sauer: Buch S. 61 Zitronensaft pH 2,4, Cola pH 2,8 (Faktor ca. 2,5 – weniger als eine halbe Stufe). »Zitronensaft ist viel saurer« ist nicht falsch gedacht, aber zu stark.",
                         "b) die Lauge – Laugenverätzungen am Auge sind meist schwerer, weil Laugen tiefer eindringen."]]],
  "tipps": [], "tip": ["Säuren", "theorie.html#saeuren"]},

 {"id": "a1", "sim": ["rotkraut"], "nr": 2, "title": "Säuren erkennen", "src": "Buch S. 54–55", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 10, "marke": "SELBSTSTUDIUM",
  "q": "Acht kurze Auswahlfragen. Bei g) und h) nimmst du die Farben aus der DEMO mit dem Rotkrautsaft.",
  "hint": "Säure heißt: gibt ein H⁺ ab. Denk bei jeder Frage zuerst an dieses kleine Teilchen.",
  "type": "multi",
  "fields": [["was", "a) Was geben Säuren in Wasser ab?", ["H⁺-Ionen (Protonen)", "OH⁻-Ionen (Hydroxid-Ionen)", "Elektronen"]],
             ["oxo", "b) Ein H⁺-Ion bleibt im Wasser nicht allein. Was entsteht?",
              ["H₃O⁺ (Oxonium-Ion) – das H⁺ hängt sich an ein Wassermolekül", "H₂ (Wasserstoffgas)", "OH⁻ (Hydroxid-Ion)"]],
             ["lackmus", "c) Welche Farbe zeigt Lackmus in einer sauren Lösung?", ["rot", "blau", "grün"]],
             ["cola", "d) Welche Säure macht Cola sauer?", ["Phosphorsäure", "Salzsäure", "Schwefelsäure"]],
             ["prickel", "e) Mineralwasser prickelt und schmeckt leicht sauer wegen …", ["Kohlensäure", "Essigsäure", "Zitronensäure"]],
             ["magen", "f) Welche Säure arbeitet in deinem Magen?", ["Salzsäure", "Phosphorsäure", "Kohlensäure"]],
             ["rk_essig", "g) DEMO: Rotkrautsaft mit Essig wurde rot bis rosa. Essig ist also …", SNB, False],
             ["rk_natron", "h) DEMO: Rotkrautsaft mit Natron wurde blau bis grün. Natron ist also …", SNB, False]],
  "chk": {"was": {"sel": "H⁺-Ionen (Protonen)"},
          "oxo": {"sel": "H₃O⁺ (Oxonium-Ion) – das H⁺ hängt sich an ein Wassermolekül"},
          "lackmus": {"sel": "rot"}, "cola": {"sel": "Phosphorsäure"}, "prickel": {"sel": "Kohlensäure"}, "magen": {"sel": "Salzsäure"},
          "rk_essig": {"sel": "sauer"}, "rk_natron": {"sel": "basisch"}},
  "fb": {"was": {"OH⁻-Ionen (Hydroxid-Ionen)": "OH⁻-Ionen machen eine Lösung basisch – das ist das Gegenteil.",
                 "Elektronen": "Elektronen wandern bei Redoxreaktionen (K1.3). Bei Säuren wandert ein Proton."},
         "oxo": {"H₂ (Wasserstoffgas)": "Wasserstoffgas entsteht erst, wenn eine Säure mit einem unedlen Metall reagiert.",
                 "OH⁻ (Hydroxid-Ion)": "OH⁻ ist das Teilchen der Basen. Das H⁺ macht aus H₂O ein H₃O⁺."},
         "lackmus": {"blau": "Blau zeigt Lackmus bei Basen.", "grün": "Lackmus kennt nur rot und blau (und violett dazwischen)."},
         "cola": {"Salzsäure": "Salzsäure gehört in den Magen, nicht in die Flasche.", "Schwefelsäure": "Schwefelsäure steckt in der Autobatterie."},
         "prickel": {"Essigsäure": "Essigsäure riecht man – im Mineralwasser ist gelöstes Kohlenstoffdioxid.",
                     "Zitronensäure": "Zitronensäure steckt in Limonaden, nicht im reinen Mineralwasser."},
         "magen": {"Phosphorsäure": "Die steckt in Cola. Der Magen bildet eine andere starke Säure.",
                   "Kohlensäure": "Kohlensäure ist schwach – der Magen braucht etwas Stärkeres zum Verdauen."},
         "rk_essig": {"neutral": "Neutral bleibt der Rotkrautsaft violett.", "basisch": "Basisch färbt ihn blau bis grün."},
         "rk_natron": {"sauer": "Sauer färbt Rotkrautsaft rot bis rosa.", "neutral": "Neutral bleibt er violett."}},
  "sol": [["Lösung", ["a) H⁺-Ionen (Protonen) · b) H₃O⁺ (Oxonium-Ion) · c) rot",
                      "d) Phosphorsäure · e) Kohlensäure (CO₂ + H₂O) · f) Salzsäure",
                      "g) Essig ist sauer · h) Natron ist basisch (es nimmt H⁺ auf)"]]],
  "tipps": ["Säuren geben etwas ab, das ganz klein und positiv ist. Und im Wasser bleibt es nicht allein.",
            "k1",
            "Lies im Buch S. 54 den Kasten »Das sollten Sie speichern« und S. 55 die Tabelle »Wichtige Säuren«."],
  "tip": ["Säuren", "theorie.html#saeuren"]},

 # --------------------------------------------------------------- Stunde 2
 {"id": "a2", "nr": 3, "title": "Laugen – nützlich und ätzend", "src": "Buch S. 56–57", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 7, "marke": "SELBSTSTUDIUM",
  "q": "Sechs Fragen zu Basen und Laugen – vom Abfluss bis zur Baustelle.",
  "hint": "Basen bilden in Wasser OH⁻-Ionen. Laugen sind gefährlicher, als sie sich anfühlen.",
  "type": "multi",
  "fields": [["oh", "a) Welche Teilchen machen eine Lösung basisch?", ["OH⁻-Ionen (Hydroxid-Ionen)", "H₃O⁺-Ionen (Oxonium-Ionen)", "Cl⁻-Ionen (Chlorid-Ionen)"]],
             ["lauge", "b) Was ist eine Lauge?", ["die Lösung einer Base in Wasser", "jede Flüssigkeit, die schäumt", "eine stark verdünnte Säure"]],
             ["rohr", "c) Rohrreiniger enthält Natriumhydroxid. Warum löst er einen Haar-Pfropfen im Abfluss auf?",
              ["Starke Laugen zersetzen Eiweiß und Fett – auch Haare und Haut", "Er macht das Wasser kochend heiß", "Er saugt die Haare mit Unterdruck weg"]],
             ["verd", "d) Du sollst eine Säure mit Wasser verdünnen. Was kommt zuerst ins Glas?",
              ["das Wasser – dann langsam die Säure dazu", "die Säure – dann das Wasser darauf", "egal, Hauptsache schnell"]],
             ["auge", "e) Ein Spritzer Lauge ist im Auge. Was tust du sofort?",
              ["lange mit viel Wasser spülen und Hilfe holen", "mit Essig neutralisieren", "abwarten, ob es brennt"]],
             ["beton", "f) Pioniere arbeiten mit frischem Beton (pH 12 bis 13). Was folgt daraus?",
              ["Handschuhe und Schutzbrille – nasser Beton kann die Haut verätzen", "nichts – Beton ist neutral", "Beton ist sauer, darum Natron mitnehmen"]]],
  "chk": {"oh": {"sel": "OH⁻-Ionen (Hydroxid-Ionen)"}, "lauge": {"sel": "die Lösung einer Base in Wasser"},
          "rohr": {"sel": "Starke Laugen zersetzen Eiweiß und Fett – auch Haare und Haut"},
          "verd": {"sel": "das Wasser – dann langsam die Säure dazu"},
          "auge": {"sel": "lange mit viel Wasser spülen und Hilfe holen"},
          "beton": {"sel": "Handschuhe und Schutzbrille – nasser Beton kann die Haut verätzen"}},
  "fb": {"oh": {"H₃O⁺-Ionen (Oxonium-Ionen)": "H₃O⁺ macht eine Lösung sauer.",
                "Cl⁻-Ionen (Chlorid-Ionen)": "Chlorid-Ionen sind der Säurerest der Salzsäure – sie machen nichts basisch."},
         "lauge": {"jede Flüssigkeit, die schäumt": "Schaum hat mit basisch nichts zu tun – Bier schäumt auch und ist sauer.",
                   "eine stark verdünnte Säure": "Verdünnte Säure bleibt eine Säure."},
         "rohr": {"Er macht das Wasser kochend heiß": "Er wird beim Lösen warm, aber das ist nicht der Grund.",
                  "Er saugt die Haare mit Unterdruck weg": "Das macht die Saugglocke. Der Rohrreiniger wirkt chemisch."},
         "verd": {"die Säure – dann das Wasser darauf": "Gefährlich: Das erste Wasser erhitzt sich schlagartig und kann samt Säure herausspritzen.",
                  "egal, Hauptsache schnell": "Gerade die Reihenfolge entscheidet. Merksatz: Erst das Wasser, dann die Säure."},
         "auge": {"mit Essig neutralisieren": "Nie im Auge neutralisieren – das kostet Zeit und erzeugt Wärme. Nur Wasser.",
                  "abwarten, ob es brennt": "Laugen brennen oft erst spät – dann ist das Auge schon geschädigt."},
         "beton": {"nichts – Beton ist neutral": "pH 12 bis 13 ist stark basisch.",
                   "Beton ist sauer, darum Natron mitnehmen": "Über 7 heißt basisch. Und gegen Verätzungen hilft Wasser, nicht Natron."}},
  "sol": [["Lösung", ["a) OH⁻-Ionen · b) die Lösung einer Base in Wasser",
                      "c) Starke Laugen zersetzen Eiweiß und Fett – Haare bestehen aus Eiweiß.",
                      "d) Erst das Wasser, dann die Säure – sonst kann es spritzen (Lösungswärme).",
                      "e) Sofort lange (mindestens 10–15 min) mit viel Wasser spülen, Augenarzt/Rettung. Nicht neutralisieren.",
                      "f) Nasser Beton ist stark basisch: Handschuhe, Schutzbrille, lange Kleidung; Spritzer sofort abwaschen."]]],
  "tipps": ["Säuren geben H⁺ ab. Was ist dann wohl das typische Teilchen der Basen?",
            "k2",
            "Lies im Buch S. 56 den Kasten »Das sollten Sie speichern« und den Hinweis links unten zum Verdünnen."],
  "tip": ["Basen und Laugen", "theorie.html#basen"]},

 {"id": "a3", "nr": 4, "title": "Protonen-Pingpong", "src": "Buch S. 58–59", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 10, "marke": "SELBSTSTUDIUM",
  "q": "Bei einer Säure-Base-Reaktion wird ein Proton (H⁺) weitergegeben – wie ein Ball. Wer den Ball abgibt, ist die Säure. Wer ihn fängt, ist die Base. "
       "a) bis c) gehören zu Gleichung 1: HCl + H₂O → Cl⁻ + H₃O⁺. d) und e) gehören zu Gleichung 2: NH₃ + H₂O → NH₄⁺ + OH⁻.",
  "hint": "Vergleiche links und rechts: Wer hat rechts ein H weniger? Wer hat eines mehr?",
  "type": "multi",
  "fields": [["g1s", "a) Gleichung 1: Wer gibt das Proton ab (Säure)?", ["HCl", "H₂O", "Cl⁻"]],
             ["g1b", "b) Gleichung 1: Wer nimmt das Proton auf (Base)?", ["H₂O", "HCl", "Cl⁻"]],
             ["g1n", "c) Gleichung 1: Welches Teilchen trägt danach das Proton?", ["H₃O⁺", "Cl⁻", "H₂O"]],
             ["g2s", "d) Gleichung 2: Wer gibt hier das Proton ab?", ["H₂O", "NH₃", "OH⁻"]],
             ["g2b", "e) Gleichung 2: Wer nimmt es auf?", ["NH₃", "H₂O", "NH₄⁺"]],
             ["ampho", "f) Wasser war in Gleichung 1 die Base und in Gleichung 2 die Säure. Wie heißt so ein Teilchen?", ["Ampholyt", "Katalysator", "Indikator"]],
             ["hno3", "g) Ergänze für Salpetersäure: HNO₃ + H₂O → NO₃⁻ + …", ["H₃O⁺", "OH⁻", "H₂"]]],
  "chk": {"g1s": {"sel": "HCl"}, "g1b": {"sel": "H₂O"}, "g1n": {"sel": "H₃O⁺"}, "g2s": {"sel": "H₂O"}, "g2b": {"sel": "NH₃"},
          "ampho": {"sel": "Ampholyt"}, "hno3": {"sel": "H₃O⁺"}},
  "fb": {"g1s": {"H₂O": "H₂O hat rechts (als H₃O⁺) ein H mehr – es hat das Proton bekommen.", "Cl⁻": "Cl⁻ steht rechts – es ist das, was von HCl übrig bleibt."},
         "g1b": {"HCl": "HCl verliert sein H – es gibt ab, nimmt nicht auf.", "Cl⁻": "Cl⁻ ist ein Produkt, kein Ausgangsstoff."},
         "g1n": {"Cl⁻": "Cl⁻ hat sein Proton gerade verloren.", "H₂O": "H₂O steht links. Rechts heißt es anders."},
         "g2s": {"NH₃": "NH₃ wird zu NH₄⁺ – es bekommt ein H dazu.", "OH⁻": "OH⁻ ist das, was vom Wasser übrig bleibt."},
         "g2b": {"H₂O": "Wasser wird zu OH⁻ – es verliert ein H.", "NH₄⁺": "NH₄⁺ steht rechts – das ist das Ergebnis."},
         "ampho": {"Katalysator": "Ein Katalysator beschleunigt Reaktionen (K1.3).", "Indikator": "Ein Indikator zeigt sauer oder basisch durch seine Farbe an."},
         "hno3": {"OH⁻": "Das Wasser bekommt hier ein Proton – es wird nicht zu OH⁻.", "H₂": "Es entsteht kein Gas. Das Proton wandert zum Wasser."}},
  "sol": [["Lösung", ["Gleichung 1: Säure HCl, Base H₂O, danach trägt H₃O⁺ das Proton (Cl⁻ bleibt übrig).",
                      "Gleichung 2: Säure H₂O, Base NH₃ (wird zu NH₄⁺, Wasser wird zu OH⁻ – darum ist Ammoniaklösung basisch).",
                      "f) Ampholyt · g) HNO₃ + H₂O → NO₃⁻ + H₃O⁺"]]],
  "tipps": ["Zähle bei jedem Teilchen die H-Atome links und rechts. Wer eines verliert, hat abgegeben.",
            "k3",
            "Lies im Buch S. 58 die Beispiele »Protolyse einer starken Säure« und »… einer starken Base«."],
  "tip": ["Protonen-Pingpong", "theorie.html#protolyse"]},

 # --------------------------------------------------------------- Stunde 3
 {"id": "a4", "sim": ["ph"], "nr": 5, "title": "Die pH-Skala lesen", "src": "Buch S. 59–61", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 6, "marke": "SELBSTSTUDIUM",
  "q": "Die pH-Skala geht von 0 bis 14. Jede Stufe ist ein Faktor 10. Sechs Fragen – c) ist eine Rechnung.",
  "hint": "pH 4 hat zehnmal so viele H₃O⁺-Ionen wie pH 5, hundertmal so viele wie pH 6.",
  "type": "multi",
  "fields": [["neutral", "a) Eine Lösung hat pH 7. Sie ist …",
              ["neutral – gleich viele H₃O⁺- und OH⁻-Ionen", "schwach sauer", "schwach basisch"]],
             ["blut", "b) Blut hat pH 7,4. Es ist …", ["schwach basisch", "schwach sauer", "genau neutral"]],
             ["faktor", "c) Zitronensaft hat pH 2, Kaffee pH 5. Wievielmal so viele H₃O⁺-Ionen hat der Zitronensaft? (nur die Zahl)"],
             ["meer", "d) Meerwasser hat pH 8,1 – trotzdem spricht man von »Ozeanversauerung«. Was stimmt?",
              ["Das Meer ist basisch und wird nur weniger basisch", "Das Meer ist schon sauer", "Der pH-Wert des Meeres steigt"]],
             ["seife", "e) Auf einer Flüssigseife steht »pH-hautneutral«. Was bedeutet das?",
              ["Sie hat etwa den pH-Wert der Haut – leicht sauer, um 5", "Sie hat genau pH 7", "Sie enthält weder Säure noch Base"]],
             ["trink", "f) Trinkwasser soll zwischen pH 6,5 und 9,5 liegen. Das Wiener Neustädter Leitungswasser hat etwa pH 7,5. Es ist …",
              ["leicht basisch – und in Ordnung", "sauer – und bedenklich", "stark basisch – nicht trinkbar"]]],
  "chk": {"neutral": {"sel": "neutral – gleich viele H₃O⁺- und OH⁻-Ionen"}, "blut": {"sel": "schwach basisch"},
          "faktor": {"num": 1000, "unit": "", "tol": 0, "nicht": [r"%", r"prozent", r"mol", r"\bph\b", r"\d\s*/\s*\d", r"(^|\s)1\s*/", r"weniger", r"kleiner", r"\boder\b"]},
          "meer": {"sel": "Das Meer ist basisch und wird nur weniger basisch"},
          "seife": {"sel": "Sie hat etwa den pH-Wert der Haut – leicht sauer, um 5"},
          "trink": {"sel": "leicht basisch – und in Ordnung"}},
  "fb": {"neutral": {"schwach sauer": "Sauer ist alles unter 7.", "schwach basisch": "Basisch ist alles über 7."},
         "blut": {"schwach sauer": "7,4 liegt über 7.", "genau neutral": "Fast – aber 7,4 ist knapp über 7."},
         "faktor": [[3, "pH 2 und pH 5 liegen 3 Stufen auseinander – aber jede Stufe ist mal 10, nicht plus 1: 10 · 10 · 10."],
                    [30, "Nicht mal 10 rechnen, sondern dreimal mit 10 malnehmen."], [100, "Das wären nur 2 Stufen. Zähle noch einmal: 2 → 3 → 4 → 5."]],
         "meer": {"Das Meer ist schon sauer": "8,1 liegt über 7 – das Meer ist basisch.",
                  "Der pH-Wert des Meeres steigt": "Er sinkt – darum »Versauerung«: mehr H₃O⁺ durch gelöstes CO₂."},
         "seife": {"Sie hat genau pH 7": "Neutral (pH 7) und hautneutral sind nicht dasselbe – die Haut ist leicht sauer.",
                   "Sie enthält weder Säure noch Base": "Fast jede Seife enthält Säuren oder Basen, um den pH-Wert einzustellen."},
         "trink": {"sauer – und bedenklich": "7,5 liegt über 7 – also leicht basisch.", "stark basisch – nicht trinkbar": "7,5 liegt mitten im erlaubten Bereich."}},
  "sol": [["Lösung", ["a) neutral · b) schwach basisch",
                      "c) 3 pH-Stufen = 10 · 10 · 10 = 1000-mal so viele H₃O⁺-Ionen.",
                      "d) Das Meer ist basisch (pH 8,1) und wird durch gelöstes CO₂ weniger basisch.",
                      "e) etwa der pH-Wert der Haut: leicht sauer, um 5 (Buch: ca. 5,5).",
                      "f) leicht basisch und in Ordnung (Richtwert 6,5 bis 9,5)."]]],
  "tipps": ["Unter 7 sauer, 7 neutral, über 7 basisch. Und: eine Stufe = mal 10.",
            "k4",
            "Lies im Buch S. 59 den Kasten »Änderung des pH-Werts« und sieh dir auf S. 61 die Beispiel-Skala an."],
  "tip": ["Der pH-Wert", "theorie.html#ph"]},

 {"id": "a5", "nr": 6, "title": "VERSUCH K1.5-V1: pH-Detektive", "src": "Versuch im Buch S. 60–61 · angepasst", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 20, "marke": "VERSUCH",
  "versuch": "K1.5-V1",
  "q": "Ihr messt den pH-Wert von sechs Proben aus Küche und Bad. Alle Gruppen haben dasselbe Material. Jeder trägt die Werte seiner Gruppe ins eigene Arbeitsblatt ein. "
       "Die Anleitung steht in der Karte darunter. Erst Vermutung (b), dann messen (c), dann auswerten (d–g).",
  "hint": "Indikatorpapier zeigt nur eine Farbe – den pH-Wert liest du an der Farbskala ab. Das ist eine Schätzung, keine genaue Messung.",
  "type": "multi", "anleitung": True, "opt": ["haut"],
  "fields": [["grp", "a) Gruppe Nr. · mit (Vornamen genügen)"],
             ["verm", "b) Vermutung vor dem Messen: Welche Probe ist am sauersten, welche am stärksten basisch?"],
             ["m1", "c1) pH Zitronensaft"], ["m2", "c2) pH Cola"], ["m3", "c3) pH Mineralwasser (prickelnd)"],
             ["m4", "c4) pH Leitungswasser"], ["m5", "c5) pH Natronlösung"], ["m6", "c6) pH Seifenlösung (Kernseife)"],
             ["haut", "c7) freiwillig: pH deiner Haut (Hand im Beutel, siehe Anleitung)"],
             ["basisch", "d) Welche Probe war bei euch basisch?", ["Natronlösung", "Cola", "Mineralwasser (prickelnd)"]],
             ["co2", "e) Warum ist prickelndes Mineralwasser saurer als Leitungswasser?",
              ["Gelöstes CO₂ bildet mit Wasser Kohlensäure", "Mineralwasser enthält Salzsäure", "Prickeln senkt den pH-Wert durch Bewegung"]],
             ["meter", "f) DEMO K1.5-D2: Prof. HOLZER hat dieselben Proben mit dem pH-Meter gemessen. Was stimmt?",
              ["Das pH-Meter misst genauer (mit Kommastelle), das Papier schätzt nur", "Das Papier ist genauer als das pH-Meter", "Beide zeigen immer genau denselben Wert"]],
             ["schluss", "g) Schlussfolgerung: Was heißt euer Cola-Wert für deine Zähne, wenn du den ganzen Tag schluckweise süße Limo oder Energydrinks trinkst? (1–2 Sätze)"]],
  "chk": {"verm": {"kw": [["Probe genannt", r"zitron|cola|mineral|leitung|natron|seife"]], "man": True, "kurz": False},
          "m1": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True}, "m2": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True},
          "m3": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True}, "m4": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True},
          "m5": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True}, "m6": {"kw": [["Zahl", r"\d"]], "man": True, "kurz": True},
          "basisch": {"sel": "Natronlösung"},
          "co2": {"sel": "Gelöstes CO₂ bildet mit Wasser Kohlensäure"},
          "meter": {"sel": "Das pH-Meter misst genauer (mit Kommastelle), das Papier schätzt nur"},
          "schluss": {"kw": [["sauer / pH niedrig", r"sauer|saeure|säure|ph ?[1-4]|niedrig"], ["Zahnschmelz", r"zahn|zähne|zaehne|schmelz|karies|erosion"],
                             ["oft / lange", r"oft|lange|dauernd|immer|stunden|ganzen tag|schluckweise|ständig|staendig"]], "need": 2, "man": True}},
  "fb": {"basisch": {"Cola": "Schau auf euren Cola-Wert: Lag er unter oder über 7?", "Mineralwasser (prickelnd)": "Prickelndes Mineralwasser ist leicht sauer."},
         "co2": {"Mineralwasser enthält Salzsäure": "Salzsäure gehört nicht ins Mineralwasser – das Prickeln kommt von gelöstem Gas.",
                 "Prickeln senkt den pH-Wert durch Bewegung": "Bewegung ändert den pH-Wert nicht. Es ist das gelöste CO₂."},
         "meter": {"Das Papier ist genauer als das pH-Meter": "Das Papier liefert nur ganze Stufen nach Farbvergleich.",
                   "Beide zeigen immer genau denselben Wert": "Kleine Unterschiede sind normal – das Papier ist eine Schätzung."}},
  "sol": [["Erwartung (Beispielwerte – eure Werte dürfen abweichen)",
           ["Zitronensaft 2–3 · Cola 2–3 · Mineralwasser prickelnd 5–6 · Leitungswasser 7–8 (Wr. Neustadt laut Wasserwerk 7,4–7,6) · Natronlösung 8–9 · Seifenlösung aus Kernseife 9–10.",
            "c7) freiwillig: Haut meist pH 5–6 (leicht sauer, »Säureschutzmantel« aus Schweiß und Talg) – mit Indikatorpapier nur grob ablesbar.",
            "d) Natronlösung (und Seifenlösung) · e) CO₂ + H₂O → H₂CO₃ (Kohlensäure)",
            "f) Das pH-Meter misst elektrisch und genauer (z. B. 2,5 statt »2–3«); das Papier ist eine Farbschätzung.",
            "g) Die Getränke sind stark sauer (pH 2–3). Wer den ganzen Tag schluckweise trinkt, greift den Zahnschmelz immer wieder an – der Speichel hat keine Zeit, die Säure zu neutralisieren."]]],
  "tipps": ["Unter 7 sauer, über 7 basisch. Ein Gas, das man in Wasser löst, kann eine Säure bilden.",
            "k5",
            "Lies im Buch S. 60 den Kasten »Mit Indikatoren führt man …« und S. 55 die Gleichung CO₂ + H₂O → H₂CO₃."],
  "tip": ["Messen mit Indikatorpapier", "theorie.html#messen"]},

 # --------------------------------------------------------------- Stunde 4
 {"id": "a6", "sim": ["neutral", "blut"], "nr": 7, "title": "Neutralisation – im Glas und in deinem Körper", "src": "Buch S. 61–62, 65", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 9, "marke": "SELBSTSTUDIUM",
  "q": "Sechs Auswahlfragen zur Neutralisation und zum Blut-pH. g) füllst du beim PARTNERCHECK aus.",
  "hint": "Bei der Neutralisation treffen sich die beiden Teilchen aus Stunde 1 und 2: H₃O⁺ und OH⁻.",
  "type": "multi",
  "fields": [["ion", "a) Was passiert bei einer Neutralisation zwischen den Teilchen?",
              ["H₃O⁺ + OH⁻ → 2 H₂O", "H₃O⁺ + Cl⁻ → HCl + H₂O", "Na⁺ + OH⁻ → NaOH"]],
             ["salz", "b) Salzsäure + Natronlauge → Natriumchlorid + …", ["Wasser", "Wasserstoff", "Sauerstoff"]],
             ["warm", "c) Mischt man Salzsäure und Natronlauge, wird das Glas warm. Die Reaktion ist …", ["exotherm", "endotherm", "gar keine Reaktion"]],
             ["sod", "d) Sodbrennen: Magensäure steigt in die Speiseröhre. Ein Mittel aus der Apotheke hilft, weil es …",
              ["eine schwache Base enthält, die Säure neutralisiert", "noch mehr Säure liefert", "die Magensäure in Zucker verwandelt"]],
             ["blut", "e) Nach einem harten Sprint sinkt der Blut-pH kurz (z. B. von 7,35 auf 7,13). Was holt ihn am schnellsten zurück?",
              ["schneller atmen – mit dem CO₂ wird Kohlensäure abgeatmet", "viel Wasser trinken", "sofort hinlegen und schlafen"]],
             ["kater", "f) Ein Trainer sagt: »Muskelkater ist Milchsäure im Muskel.« Stimmt das?",
              ["Nein – Laktat ist nach 30 bis 90 Minuten abgebaut, Muskelkater kommt erst 1 bis 3 Tage später", "Ja, genau so", "Ja, aber nur bei Ausdauersport"]],
             ["partner", "g) PARTNERCHECK: mit wem? Wie viele der 4 Karten wusstet ihr?"]],
  "chk": {"ion": {"sel": "H₃O⁺ + OH⁻ → 2 H₂O"}, "salz": {"sel": "Wasser"}, "warm": {"sel": "exotherm"},
          "sod": {"sel": "eine schwache Base enthält, die Säure neutralisiert"},
          "blut": {"sel": "schneller atmen – mit dem CO₂ wird Kohlensäure abgeatmet"},
          "kater": {"sel": "Nein – Laktat ist nach 30 bis 90 Minuten abgebaut, Muskelkater kommt erst 1 bis 3 Tage später"},
          "partner": {"kw": [["Name", r"[a-zäöü]{2}"]], "man": True, "kurz": True}},
  "fb": {"ion": {"H₃O⁺ + Cl⁻ → HCl + H₂O": "Cl⁻ bleibt einfach in der Lösung – es macht nicht mit.",
                 "Na⁺ + OH⁻ → NaOH": "Na⁺ und OH⁻ bleiben getrennt. Die OH⁻ reagieren mit H₃O⁺."},
         "salz": {"Wasserstoff": "Wasserstoffgas entsteht bei Säure + unedlem Metall, nicht bei Säure + Lauge.",
                  "Sauerstoff": "Kein Gas: Aus H₃O⁺ und OH⁻ wird Wasser."},
         "warm": {"endotherm": "Endotherm hieße: Das Glas wird kalt (K1.3).", "gar keine Reaktion": "Es entstehen neue Stoffe – also eine Reaktion."},
         "sod": {"noch mehr Säure liefert": "Mehr Säure würde stärker brennen.", "die Magensäure in Zucker verwandelt": "Aus Säure wird durch eine Base Salz und Wasser – kein Zucker."},
         "blut": {"viel Wasser trinken": "Trinken ist gut, wirkt aber langsam. Der schnellste Hebel ist die Atmung.",
                  "sofort hinlegen und schlafen": "Ausruhen hilft, aber schneller atmen wirkt in Sekunden."},
         "kater": {"Ja, genau so": "Das galt lange als Wahrheit – heute weiß man: Muskelkater kommt von winzigen Verletzungen der Muskelfasern.",
                   "Ja, aber nur bei Ausdauersport": "Muskelkater kommt vor allem nach ungewohnter Belastung, etwa bergab gehen – nicht von Laktat."}},
  "sol": [["Lösung", ["a) H₃O⁺ + OH⁻ → 2 H₂O · b) Wasser (HCl + NaOH → NaCl + H₂O) · c) exotherm",
                      "d) Antazida enthalten schwache Basen (z. B. Carbonate, Hydroxide) und neutralisieren überschüssige Magensäure.",
                      "e) Schneller atmen: CO₂ wird abgeatmet, damit verschwindet Kohlensäure aus dem Blut; dazu puffert Hydrogencarbonat.",
                      "f) Nein. Laktat ist nach 30–90 min abgebaut; Muskelkater (1–3 Tage später) entsteht durch winzige Verletzungen der Muskelfasern."]]],
  "tipps": ["Säure und Base heben sich auf. Welche zwei Teilchen treffen sich dabei?",
            "k6",
            "Lies im Buch S. 65 das Beispiel »Neutralisation von Salzsäure und Natronlauge« und S. 62 oben zum Blut."],
  "tip": ["Neutralisation", "theorie.html#neutral"]},

 # --------------------------------------------------------------- Zusatz
 {"id": "z1", "nr": 8, "title": "KI-Fehlerjagd: Was stimmt hier nicht?", "src": "Buch S. 56–61", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8, "marke": "ZUSATZ",
  "q": "Ein Chatbot hat auf die Frage »Was heißt pH-neutral?« diese Antwort gegeben (Beispiel, so ähnlich kommt es vor): "
       "»1. pH-neutral heißt pH 7. 2. Darum hat ein pH-hautneutrales Duschgel genau pH 7. 3. Das Meer ist durch die Versauerung schon sauer. 4. Laugen sind harmloser als Säuren, weil sie nicht brennen.« "
       "Finde die Fehler – ohne KI. Wenn du willst, stellst du danach einer KI dieselbe Frage und prüfst ihre Antwort.",
  "hint": "Prüfe jeden Satz mit der Theorie: Haut, Meer, Augen.",
  "type": "multi",
  "fields": [["wie", "a) Wie viele der vier Sätze sind falsch?", ["drei (Satz 2, 3 und 4)", "alle vier", "nur einer"]],
             ["meer", "b) Verbessere Satz 3 in einem Satz."],
             ["lauge", "c) Verbessere Satz 4 in einem Satz."],
             ["ki", "d) Freiwillig: Was hat eine echte KI geantwortet – und war es richtig? (Name der KI und 1 Satz)"]],
  "chk": {"wie": {"sel": "drei (Satz 2, 3 und 4)"},
          "meer": {"neg": True, "kw": [["basisch / über 7", r"basisch|alkalisch|8[,.]1|über 7|ueber 7|groesser als 7|größer als 7"], ["weniger basisch / sinkt", r"weniger|sinkt|gesunken|abnimmt|nimmt ab|niedriger"]], "need": 2, "man": True},
          "lauge": {"kw": [["gefährlich / ätzend", r"gefaehrlich|gefährlich|aetz|ätz|verätz|veraetz|schlimmer"], ["Grund / Auge / tief", r"tief|auge|fett|eiweiss|eiweiß|brennen spät|spaet|später|spater"]], "need": 1, "man": True, "contra": [r"ungef(ae|ä)hrlich|harmlos|weniger gef(ae|ä)hrlich"]}},
  "fb": {"wie": {"alle vier": "Satz 1 stimmt: neutral heißt pH 7.", "nur einer": "Schau dir Satz 2, 3 und 4 noch einmal an."}},
  "sol": [["Lösung", ["a) Drei Sätze sind falsch – nur Satz 1 stimmt.",
                      "Satz 2: »hautneutral« heißt etwa der pH-Wert der Haut, also leicht sauer (um 5), nicht pH 7.",
                      "b) Satz 3: Das Meer ist mit pH 8,1 basisch; es wird durch gelöstes CO₂ nur weniger basisch.",
                      "c) Satz 4: Laugen sind oft gefährlicher – sie zersetzen Fett und Eiweiß, dringen tiefer ein und brennen manchmal erst spät."]]],
  "tipps": [], "tip": ["Der pH-Wert", "theorie.html#ph"]},

 {"id": "z2", "nr": 9, "title": "Forschung: Die Meere werden weniger basisch", "src": "PIK 2025 · Buch S. 61", "own": True, "tag": "Zusatz", "h": 0, "zeit": 10, "marke": "ZUSATZ",
  "q": "Das Potsdam-Institut für Klimafolgenforschung (PIK) meldete am 24.09.2025: Der pH-Wert an der Meeresoberfläche ist seit Beginn der Industrialisierung um rund 0,1 gesunken. "
       "Die Ursache ist CO₂ aus Öl, Gas und Kohle, das sich im Meer löst. Rechne nach: 10 hoch 0,1 ergibt 1,26.",
  "hint": "1,26-mal so viel wie vorher – um wie viel Prozent ist das mehr?",
  "type": "multi",
  "fields": [["prozent", "a) Um wie viel Prozent mehr H₃O⁺-Ionen bedeutet ein pH-Rückgang um genau 0,1? (in %)"],
             ["warum", "b) Das PIK schreibt von einer »Zunahme der Versauerung um 30 bis 40 Prozent«. Was ist eine mögliche Erklärung für den Unterschied zu deinem Ergebnis?",
              ["»rund 0,1« ist gerundet – schon 0,11 bis 0,15 ergeben 30 bis 40 %", "Das PIK hat sich verrechnet", "Prozent und pH-Stufen sind dasselbe"]],
             ["schale", "c) Winzige Meeresschnecken zeigen schon Schäden an ihren Schalen. Warum?",
              ["Im saureren Wasser fällt der Schalenbau aus Kalk schwerer, dünne Schalen lösen sich an", "Das Wasser wird zu warm für Schalen", "Basisches Wasser löst Kalk auf"]],
             ["quelle", "d) Was für eine Quelle ist die Meldung vom 24.09.2025?",
              ["eine Pressemitteilung eines Forschungsinstituts – guter Start, Zahlen im Bericht nachprüfen", "eine Werbung eines Unternehmens", "ein Social-Media-Gerücht ohne Absender"]]],
  "chk": {"prozent": {"num": 26, "unit": "", "tol": 0.5, "nicht": [r"mal\b", r"fach", r"\d\s*x\b", r"×", r"\bph\b", r"weniger", r"sinkt", r"abnahme", r"\boder\b"]},
          "warum": {"sel": "»rund 0,1« ist gerundet – schon 0,11 bis 0,15 ergeben 30 bis 40 %"},
          "schale": {"sel": "Im saureren Wasser fällt der Schalenbau aus Kalk schwerer, dünne Schalen lösen sich an"},
          "quelle": {"sel": "eine Pressemitteilung eines Forschungsinstituts – guter Start, Zahlen im Bericht nachprüfen"}},
  "fb": {"prozent": [[1.26, "1,26-mal so viel – das sind 26 % mehr. Gefragt ist der Prozentwert."], [126, "126 % wäre der neue Gesamtwert. Die Zunahme sind 26 %."], [10, "Eine ganze pH-Stufe wäre Faktor 10. Hier geht es nur um 0,1."]],
         "warum": {"Das PIK hat sich verrechnet": "Erst prüfen, dann urteilen: Rechne 10 hoch 0,13 nach – das ergibt 1,35.",
                   "Prozent und pH-Stufen sind dasselbe": "Eine pH-Stufe ist ein Faktor 10, kein Prozent."},
         "schale": {"Das Wasser wird zu warm für Schalen": "Wärme schadet auch, aber hier geht es um die Säure.",
                    "Basisches Wasser löst Kalk auf": "Umgekehrt: Kalk löst sich in Säure (Kalkentferner sind sauer). Je weniger basisch das Meer, desto schwerer wird der Schalenbau."},
         "quelle": {"eine Werbung eines Unternehmens": "Absender ist ein öffentlich finanziertes Forschungsinstitut.",
                    "ein Social-Media-Gerücht ohne Absender": "Absender, Datum und Bericht sind angegeben."}},
  "sol": [["Lösung", ["a) 10^0,1 = 1,26 → 26 % mehr H₃O⁺-Ionen.",
                      "b) Mögliche Erklärung (keine Aussage des PIK): »rund 0,1« ist gerundet; 0,11 → 29 %, 0,15 → 41 %. Prüfen statt »die haben sich verrechnet«.",
                      "c) Im saureren Wasser gibt es weniger Carbonat-Ionen, aus denen die Tiere ihren Kalk (Calciumcarbonat) bauen; dünne Schalen lösen sich sogar an. Das Meer bleibt dabei basisch.",
                      "d) Pressemitteilung des PIK (idw, 24.09.2025) zum Bericht »Planetary Health Check 2025«."]]],
  "tipps": [], "tip": ["Für Schnelle", "theorie.html#schnelle"]},

 {"id": "z3", "nr": 10, "title": "Sicherheits-Briefing: Säuren und Laugen im Dienst", "src": "Buch S. 53, 56", "own": True, "tag": "Zusatz", "h": 0, "zeit": 15, "marke": "ZUSATZ",
  "q": "Gestalte ein kurzes Briefing für Rekruten: als Podcast (höchstens 60 Sekunden) ODER als Plakat (A4, Handschrift, Foto). Pflichtinhalt: "
       "drei Gefahren aus dem Dienst (z. B. nasser Beton pH 12–13, Batteriesäure im Fahrzeug, Rohrreiniger in der Unterkunft), die Erste Hilfe bei einem Spritzer ins Auge und ein Merksatz. "
       "Abgabe der Datei in LMS (ist sie zu groß: Teams).",
  "hint": "Kurz und klar wie eine Befehlsausgabe: Was – Warum – Was tun.",
  "type": "multi",
  "fields": [["form", "a) Was hast du gemacht?", ["Podcast", "Plakat"], False],
             ["merksatz", "b) Dein Merksatz (1 Satz)"]],
  "chk": {"merksatz": {"kw": [["Merksatz", r"\w{3,}"]], "man": True}},
  "sol": [["Bewertungsraster (freiwillig, keine Note)",
           ["3 Gefahren fachlich richtig (pH oder Stoff genannt) · Erste Hilfe: lange mit Wasser spülen, Hilfe holen, nicht neutralisieren · Merksatz verständlich · Zeit/Format eingehalten."]]],
  "tipps": [], "tip": ["Basen und Laugen", "theorie.html#basen"]},
]

# ---------------------------------------------------------------- Anleitung für den Versuch (Karte im Arbeitsblatt, Aufbau nach KLARE_ANWEISUNGEN.md)
ANLEITUNG = {
 "ziel": "Herausfinden, wie sauer oder basisch sechs Proben aus Küche und Bad sind.",
 "material": ["1 Tüpfelplatte (Gruppe 6: 6 kleine Petrischalen)", "6 Stück Indikatorpapier, je ca. 2 cm (liegen bei der Probenstation)",
              "1 weißes Blatt Papier, 1 Stift", "Schutzbrille für jeden", "freiwillig: 1 Gefrierbeutel und 1 Gummiring (Haut-pH)"],
 "gruppen": "6 Gruppen zu viert, jede Gruppe an ihrem Schülertisch. Rollen: Holer (holt die Proben), Tropfer, Ableser, Schreiber.",
 "vorbereitung": "Blatt unter die Tüpfelplatte legen. Mulden 1 bis 6 auf dem Blatt nummerieren. Schutzbrille auf. Der Ableser fotografiert gleich am Anfang die Farbskala (Dose am Lehrertisch) mit dem Handy.",
 "schritte": ["Vermutung in b) eintragen.",
              "Freiwillig (Haut-pH, c7): Gleich am Anfang gibt ein Gruppenmitglied einen Tropfen destilliertes Wasser (bekommt ihr von Prof. HOLZER) in die Handfläche, steckt die Hand in den Gefrierbeutel und schließt ihn locker mit dem Gummiring. Es arbeitet mit der anderen Hand weiter.",
              "Der Holer bringt die Tüpfelplatte zur Probenstation: Gruppe 1–3 zu Mobiltisch 1, Gruppe 4–6 zu Mobiltisch 2. Mit der Pipette der jeweiligen Probe kommen etwa 10 Tropfen in die passende Mulde. Pipette zurück in ihr Gefäß.",
              "Reihenfolge: 1 Zitronensaft · 2 Cola · 3 Mineralwasser · 4 Leitungswasser · 5 Natronlösung · 6 Seifenlösung.",
              "Am Tisch taucht der Tropfer die Spitze eines frischen Stücks Indikatorpapier in jede Mulde und legt es neben die Nummer auf das Blatt.",
              "Gleich danach (innerhalb von 1 Minute): Der Ableser vergleicht die Farben mit dem Foto der Farbskala. Bei Zweifel kurz an der Dose am Lehrertisch nachsehen.",
              "Nach etwa 10 Minuten (freiwillig): Hand aus dem Beutel, ein Stück Indikatorpapier kurz auf die feuchte Handfläche drücken, Farbe ablesen – das ist c7.",
              "Der Schreiber sagt die Werte an, jeder trägt sie in c1 bis c6 ein (c7 freiwillig). Die pH-Meter-Werte (DEMO K1.5-D2) zeigt Prof. HOLZER erst danach beim Besprechen.",
              "Aufräumen: Papier in den Restmüll, Tüpfelplatte (bzw. Petrischalen) an der Wasserleitung ausspülen und zurückgeben."],
 "messwerte": "pH-Wert als ganze Zahl oder Bereich (z. B. »2–3«), ohne Einheit – der pH-Wert hat keine.",
 "sicherheit": ["Schutzbrille auf – Zitronensaft und Seifenlösung brennen im Auge.", "Nichts kosten, nichts trinken: Laborgefäße sind keine Trinkgläser.",
                "Kommt etwas ins Auge: sofort an der Wasserleitung spülen und Prof. HOLZER rufen.",
                "Haut-pH nur auf gesunder Haut ohne Wunde; danach Hände waschen."],
 "abgabe": "Jeder trägt die Werte in sein Arbeitsblatt ein (Abschnitt Aufgabe 6) und gibt am Ende EIN PDF in LMS ab.",
 "auswertung": "Heute: d) bis g) in der Gruppe besprechen und eintragen. Am Ende der Stunde vergleicht die Klasse alle Werte am Beamer.",
 "mat": [["Tüpfelplatte (Gruppe 6: 6 kleine Petrischalen)", "tuepfelplatte"], ["6 Stück Indikatorpapier, je ca. 2 cm", "indikatorpapier"],
            ["weißes Blatt Papier", "papier"], ["Stift", "bleistift"], ["Handy für das Foto der Farbskala", "handy"], ["Schutzbrille für jeden", "brille"],
            ["freiwillig: Gefrierbeutel und Gummiring (Haut-pH)", "beutel"]],
    "station": [["1 Zitronensaft", "zitronensaeure"], ["2 Cola", "flasche"], ["3 Mineralwasser prickelnd", "flasche"], ["4 Leitungswasser", "hahn"],
                ["5 Natronlösung (1 TL Natron in 250 ml Wasser)", "natron"], ["6 Seifenlösung (Kernseife)", "seife"], ["bei jeder Probe eine Tropfpipette", "pipette"]],
    "entsorgung": "Alle Proben sind Lebensmittel oder Haushaltsstoffe: Reste in den Ausguss, mit Wasser nachspülen. Indikatorpapier und Gefrierbeutel in den Restmüll. Tüpfelplatte bzw. Petrischalen an der Wasserleitung ausspülen und zurückgeben.",
    "platz": "Jede Gruppe am eigenen Schülertisch · Probenstationen: Mobiltisch 1 (Gruppe 1–3) und Mobiltisch 2 (Gruppe 4–6) · Farbskala und pH-Meter am Lehrertisch · Ausspülen an der Wasserleitung",
}

# ---------------------------------------------------------------- Kontrollen
# ---- Virtueller Versuch (PhET, Stephan 15.11.2026: externe Simulationen als virtueller Versuch mit Protokoll) ----
# Werte geprüft im Quellcode der Simulation (github.com/phetsims/ph-scale, js/common/model/Solute.ts):
# Limonade 2,5 · Orangensaft 3,5 · Kaffee 5 · Milch 6,5 · Blut 7,4 · Handseife 10 · Abflussreiniger 13; deutsche Namen aus phetsims/babel.
PHET = {"titel": "pH Skala: Grundlagen", "url": "https://phet.colorado.edu/de/simulations/ph-scale-basics",
        "herkunft": "PhET, University of Colorado Boulder · Deutsch · CC BY 4.0 · läuft im Browser, auch am Handy"}
T.append({
    "id": "z4", "nr": 11, "title": "VIRTUELLER VERSUCH K1.5-VV1: pH-Werte messen und verdünnen", "src": "PhET-Simulation · Buch S. 60–61",
    "own": True, "tag": "Zusatz", "h": 0, "zeit": 15, "marke": "ZUSATZ",
    "link": [PHET["titel"] + " öffnen", PHET["url"], PHET["herkunft"]],
    "q": "Öffne die Simulation »pH Skala: Grundlagen« (Knopf oben). Oben wählst du eine Flüssigkeit, mit dem Hahn füllst du sie in den Becher. "
         "Tauch die Sonde des pH-Meters ein. Mit dem Wasserhahn rechts verdünnst du. Das ist ein Versuch am Handy – du schreibst ein Protokoll wie im Labor.",
    "hint": "Die Sonde muss in die Flüssigkeit tauchen, sonst zeigt das Gerät nichts an.",
    "type": "multi",
    "fields": [
        ["verm", "a) Vermutung: Welche ist am sauersten – Kaffee, Limonade oder Orangensaft? Begründe kurz."],
        ["m_lim", "b1) Limonade: pH ="], ["m_or", "b2) Orangensaft: pH ="], ["m_kaf", "b3) Kaffee: pH ="],
        ["m_milch", "b4) Milch: pH ="], ["m_blut", "b5) Blut: pH ="], ["m_seife", "b6) Handseife: pH ="],
        ["sauer", "c) Welche der sechs Flüssigkeiten ist am sauersten?", ["Limonade", "Orangensaft", "Kaffee", "Milch"]],
        ["verd", "d) Nimm Limonade und gib mehrmals Wasser dazu. Was passiert mit dem pH-Wert?",
         ["Er steigt und nähert sich 7", "Er sinkt", "Er bleibt gleich", "Er steigt bis über 7"]],
        ["basisch", "e) Kann man eine Säure nur durch Wasser basisch machen?",
         ["Nein – der pH-Wert kommt 7 immer näher, aber nicht darüber", "Ja, mit genug Wasser wird sie basisch", "Ja, aber nur bei Limonade"]],
        ["erk", "f) Erkenntnis: Was bedeutet das Verdünnen für die Sicherheit im Labor? (1–2 Sätze)"],
        ["vgl", "g) Vergleich: Was kann der virtuelle Versuch besser als der echte – und was nicht? (je ein Punkt)"],
    ],
    "chk": {"verm": {"kw": [["Begründung", r"\w{3,}"]], "need": 1, "man": True},
            "m_lim": {"num": 2.5, "unit": "", "tol": 0.1, "kurz": True}, "m_or": {"num": 3.5, "unit": "", "tol": 0.1, "kurz": True},
            "m_kaf": {"num": 5, "unit": "", "tol": 0.1, "kurz": True}, "m_milch": {"num": 6.5, "unit": "", "tol": 0.1, "kurz": True},
            "m_blut": {"num": 7.4, "unit": "", "tol": 0.1, "kurz": True}, "m_seife": {"num": 10, "unit": "", "tol": 0.1, "kurz": True},
            "sauer": {"sel": "Limonade"}, "verd": {"sel": "Er steigt und nähert sich 7"},
            "basisch": {"sel": "Nein – der pH-Wert kommt 7 immer näher, aber nicht darüber"},
            "erk": {"kw": [["verdünnt / weniger sauer / weniger gefährlich", r"verd(ue|ü)nn|weniger (sauer|gef|aetz|ätz)|harmlos"]], "need": 1, "man": True},
            "vgl": {"kw": [["besser", r"\w{3,}"]], "need": 1, "man": True}},
    "fb": {"m_lim": [[7, "Das ist reines Wasser. Hast du Limonade gewählt und die Sonde eingetaucht?"]],
           "sauer": {"Orangensaft": "Vergleiche b1 und b2: Der kleinere pH-Wert ist saurer.", "Kaffee": "Kaffee liegt bei pH 5 – eher schwach sauer.", "Milch": "Milch ist fast neutral."},
           "verd": {"Er sinkt": "Mehr Wasser – weniger H₃O⁺ pro Liter. Wird es dann saurer oder weniger sauer?", "Er bleibt gleich": "Schau genau aufs pH-Meter, während du Wasser dazugibst.",
                    "Er steigt bis über 7": "Fülle so lange auf, bis der Becher voll ist – wird es wirklich basisch?"},
           "basisch": {"Ja, mit genug Wasser wird sie basisch": "Wasser selbst hat pH 7. Kann eine Mischung mit Wasser über 7 kommen?", "Ja, aber nur bei Limonade": "Probier es auch mit Erbrochenem oder Batteriesäure."}},
    "sol": [["Lösung", ["a) z. B. »Limonade, weil viel Säure drin ist« – Vermutung, keine Bewertung.",
                        "b) Werte in der Simulation: Limonade 2,5 · Orangensaft 3,5 · Kaffee 5,0 · Milch 6,5 · Blut 7,4 · Handseife 10,0 (bei vollem Becher ohne Wasser).",
                        "c) Limonade. d) Der pH-Wert steigt und nähert sich 7. e) Nein – Wasser hat pH 7, die Mischung kommt nicht darüber.",
                        "f) Verdünnte Säure ist weniger sauer und weniger gefährlich – darum verdünnt man (»Erst das Wasser, dann die Säure«). Aber: Auch verdünnt bleibt sie sauer.",
                        "g) Besser: ohne Gefahr, gefährliche Stoffe (Batteriesäure, Abflussreiniger) möglich, genaue Werte, beliebig oft. Nicht: echtes Hantieren, Geruch, Messfehler, Überraschungen – die echte Welt."]]],
    "tipps": ["Sonde eintauchen, dann ablesen. Kleinere Zahl = saurer.", "k4", "Buch S. 60–61: pH-Wert"],
})
# ---- Lesen und prüfen (Stephan 15.11.2026: passende Texte aus ORF Science o. Ä. suchen). ORF/Ö1 hatte nichts Passendes;
# geprüft und verwendet: Quarks (WDR), Linda Fischer, »Darum sind viele Säure-Basen-Kuren Quatsch«, 29.10.2019, aktualisiert 15.02.2022, frei lesbar.
QUARKS = {"titel": "Darum sind viele Säure-Basen-Kuren Quatsch", "url": "https://www.quarks.de/?p=19042",
          "herkunft": "Quarks (WDR) · Linda Fischer · 29.10.2019, aktualisiert 15.02.2022 · frei lesbar, ca. 7 min"}
T.append({
    "id": "z5", "nr": 12, "title": "Lesen und prüfen: »Übersäuert« – was ist dran?", "src": "Quarks (WDR) · Buch S. 61–62",
    "own": True, "tag": "Zusatz", "h": 0, "zeit": 12, "marke": "ZUSATZ",
    "link": ["Artikel bei Quarks öffnen", QUARKS["url"], QUARKS["herkunft"]],
    "q": "Werbung verspricht Basenpulver, basische Socken und Kuren gegen »Übersäuerung«. Lies den Artikel von Quarks (Knopf oben, ca. 7 min) "
         "und prüf ihn mit dem, was du über Blut-pH und Puffer weißt.",
    "hint": "Such im Text nach »7,4«, »Puffer«, »Lunge« und »Urin«.",
    "type": "multi",
    "fields": [
        ["blut", "a) Welchen Blut-pH nennt der Artikel als normal?", ["etwa 7,4 – leicht basisch", "etwa 5,5 – leicht sauer", "genau 7 – neutral", "etwa 9 – basisch"]],
        ["halt", "b) Was hält den Blut-pH laut Artikel konstant?", ["Puffer, die Lunge (CO₂) und die Ausscheidung über den Urin", "Basenpulver", "basische Socken und Decken", "nur die richtige Ernährung"]],
        ["wer", "c) Wem droht laut Artikel wirklich eine Übersäuerung (Acidose)?", ["Menschen mit Vorerkrankungen, z. B. der Nieren oder Diabetes", "jedem, der Fleisch isst", "allen, die viel Sport machen", "jedem, der Cola trinkt"]],
        ["geld", "d) Quellenkritik: Wer verdient am Wort »Übersäuerung« – und warum ist das wichtig, wenn du Werbung liest? (1–2 Sätze)"],
        ["sprint", "e) Nach dem Sprint ist dein Blut kurz saurer (Aufgabe 7). Ist das die »Übersäuerung« aus der Werbung? Begründe kurz."],
    ],
    "chk": {"blut": {"sel": "etwa 7,4 – leicht basisch"}, "halt": {"sel": "Puffer, die Lunge (CO₂) und die Ausscheidung über den Urin"},
            "wer": {"sel": "Menschen mit Vorerkrankungen, z. B. der Nieren oder Diabetes"},
            "geld": {"kw": [["Anbieter / Verkäufer", r"verkau|anbiet|herstell|firma|firmen|unternehm|geld|verdien|gewinn|werb"]], "need": 1, "man": True},
            "sprint": {"kw": [["kurz / Atmung / Puffer", r"kurz|atm|puffer|lunge|co2|co₂|normal|wieder"]], "need": 1, "man": True,
                       "contra": [r"\bja\b[^.!?]{0,40}(übersäuer|uebersaeuer|dieselbe|die gleiche|das gleiche|dasselbe)", r"(dieselbe|die gleiche|das gleiche|dasselbe) (übersäuerung|sache|krankheit)"]}},
    "fb": {"blut": {"etwa 5,5 – leicht sauer": "5,5 ist der pH der Haut, nicht des Blutes.", "genau 7 – neutral": "Blut ist leicht basisch – schau in Aufgabe 7 oder im Artikel."},
           "halt": {"Basenpulver": "Das verkauft die Werbung. Was sagt der Artikel – welche Organe arbeiten?", "nur die richtige Ernährung": "Der Körper regelt das selbst. Womit?"},
           "wer": {"allen, die viel Sport machen": "Beim Sport sinkt der pH nur kurz – und die Atmung holt ihn zurück."}},
    "sol": [["Lösung", ["a) etwa 7,4 (leicht basisch); von Acidose spricht man laut Artikel erst unter 7,35.",
                        "b) Puffer im Blut, die Lunge (atmet CO₂ ab) und der Urin (scheidet Säuren aus – so steht es im Artikel; dahinter arbeiten die Nieren).",
                        "c) Menschen mit Vorerkrankungen, z. B. chronischer Nierenerkrankung oder Diabetes – nicht Gesunde durch normales Essen.",
                        "d) Anbieter von Basenpulver, Kuren, Hotels und »basischer« Kleidung. Wer etwas verkauft, hat ein Interesse daran, dass du ein Problem hast – darum unabhängige Quellen prüfen.",
                        "e) Nein: Der pH sinkt beim Sprint nur kurz und bleibt im Rahmen; Atmung und Puffer holen ihn in Minuten zurück. Das ist normale Regelung, keine Krankheit."]]],
    "tipps": ["Such im Text nach »7,4«, »Lunge« und »Urin«.", "k7", "Buch S. 61–62: Puffer im Blut"],
})

T.append({
    "id": "z6", "nr": 13, "title": "Säure-Alarm im Mund: Zähne, Kaugummi, Sodbrennen", "src": "Zahnmedizin (Stephan-Kurve) · Buch S. 61, 65", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8, "marke": "ZUSATZ",
    "bild": ["img/mundph.svg", "Diagramm: pH-Wert am Zahn nach dem Essen. Beide Kurven fallen nach etwa 5 Minuten unter die kritische Linie 5,5. Kurve B steigt ab Minute 10 schnell wieder auf fast 7, Kurve A bleibt bis etwa Minute 30 unter 5,5.", "Bild antippen – dann wird es groß. Vereinfacht, Werte ungefähr."],
    "q": "Nach dem Essen machen Bakterien im Zahnbelag aus Zucker Säure. Unter pH 5,5 wird der Zahnschmelz angegriffen. Das Diagramm zeigt zwei Kadetten nach demselben Essen: Einer kaut ab Minute 10 einen zuckerfreien Kaugummi, der andere nicht.",
    "hint": "Die rote Linie bei 5,5 ist die Grenze. Alles darunter greift den Zahnschmelz an.",
    "type": "multi",
    "fields": [
        ["kurve", "a) Welche Kurve gehört zum Kadetten mit Kaugummi?", ["Kurve B – sie steigt schnell wieder über 5,5", "Kurve A – sie bleibt länger unter 5,5", "Man kann es nicht erkennen – beide sind gleich"]],
        ["wann", "b) Wann fallen beide Kurven unter 5,5?", ["nach etwa 5 Minuten", "sofort beim ersten Bissen", "erst nach etwa einer Stunde"]],
        ["warum", "c) Warum hilft der Kaugummi?", ["Kauen bringt mehr Speichel – der puffert und neutralisiert die Säure", "Kaugummi enthält eine Säure, die die Bakterien tötet", "Der Kaugummi klebt die Säure fest"]],
        ["schluck", "d) Marsch: Kadett 1 trinkt einen halben Liter Sportgetränk in kleinen Schlucken über zwei Stunden. Kadett 2 trinkt ihn in fünf Minuten und nimmt danach einen Schluck Wasser. Wessen Zähne sind länger unter Säure?", ["Kadett 1 – jeder Schluck senkt den pH wieder", "Kadett 2 – er trinkt mehr auf einmal", "beide gleich – es ist dieselbe Menge"]],
        ["sod", "e) Sodbrennen: Ein Freund rät, einen Esslöffel Zitronensaft zu schlucken. Sinnvoll?", ["Nein – Zitronensaft ist sauer (pH ca. 2–3) und bringt noch mehr Säure", "Ja – Zitronensaft wirkt im Körper basisch", "Ja – Säure neutralisiert Säure"]],
    ],
    "chk": {"kurve": {"sel": "Kurve B – sie steigt schnell wieder über 5,5"}, "wann": {"sel": "nach etwa 5 Minuten"},
            "warum": {"sel": "Kauen bringt mehr Speichel – der puffert und neutralisiert die Säure"},
            "schluck": {"sel": "Kadett 1 – jeder Schluck senkt den pH wieder"},
            "sod": {"sel": "Nein – Zitronensaft ist sauer (pH ca. 2–3) und bringt noch mehr Säure"}},
    "fb": {"kurve": {"Kurve A – sie bleibt länger unter 5,5": "Kaugummi soll helfen – welche Kurve kommt schneller aus dem roten Bereich?",
                     "Man kann es nicht erkennen – beide sind gleich": "Bis Minute 10 sind sie gleich – danach schau genau hin."},
           "wann": {"sofort beim ersten Bissen": "Die Bakterien brauchen ein paar Minuten. Wo schneidet die Kurve die rote Linie?",
                    "erst nach etwa einer Stunde": "Nach einer Stunde sind beide längst wieder oben. Schau auf den Anfang."},
           "warum": {"Kaugummi enthält eine Säure, die die Bakterien tötet": "Mehr Säure würde den Zähnen schaden. Was passiert beim Kauen im Mund?",
                     "Der Kaugummi klebt die Säure fest": "Säure ist gelöst – die lässt sich nicht festkleben. Denk an den Speichel."},
           "schluck": {"Kadett 2 – er trinkt mehr auf einmal": "Die Menge ist gleich. Entscheidend ist, wie oft und wie lange die Zähne in Säure baden.",
                       "beide gleich – es ist dieselbe Menge": "Gleiche Menge, aber unterschiedlich oft. Denk an die Kurve: Jeder Schluck startet sie neu."},
           "sod": {"Ja – Zitronensaft wirkt im Körper basisch": "So steht es in Ratgebern zur »basischen Ernährung«. In Speiseröhre und Magen ist Zitronensaft aber einfach sauer.",
                   "Ja – Säure neutralisiert Säure": "Neutralisieren kann nur eine Base. Säure + Säure bleibt sauer."}},
    "sol": [["Lösung", ["a) Kurve B: Sie ist ab Minute 10 schneller wieder über 5,5. Kauen regt den Speichel an (Flussrate steigt stark).",
                        "b) nach etwa 5 Minuten (Fachliteratur: 5 bis 10 Minuten).",
                        "c) Speichel enthält Hydrogencarbonat – eine Base, die H⁺ aufnimmt (Puffer). Dazu bringt er Calcium und Phosphat zurück in den Zahnschmelz.",
                        "d) Kadett 1: Jeder Schluck senkt den pH wieder unter 5,5, die Zähne bekommen zwei Stunden lang keine Pause. Besser zügig trinken und Wasser nachspülen.",
                        "e) Nein. Gegen Sodbrennen helfen Basen (Antazida, z. B. Calcium- und Magnesiumcarbonat); Zitronensaft ist sauer. Bei häufigem Sodbrennen zum Arzt."]]],
    "tipps": ["Wo kreuzt welche Kurve die rote Linie? Und was macht Speichel mit Säure?", "k6", "Buch S. 65: Neutralisation"],
})
assert [t["nr"] for t in T] == list(range(1, 14))
PFLICHT = [t["nr"] for t in T if t["tag"] != "Zusatz" and not t.get("vorhersage")]
assert PFLICHT == [2, 3, 4, 5, 6, 7], PFLICHT
BESPRECHEN = [2, 4, 6, 7]
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True
for _t in T:
    for _k in (_t["chk"] or {}):
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
            assert len(set(_f[2])) == len(_f[2]), (_t["id"], _f[0], "doppelte Option")
    for _k, _m in _t.get("fb", {}).items():
        if isinstance(_m, list):
            _c = _t["chk"][_k]; assert "num" in _c, (_t["id"], _k)
            for _w, _txt in _m: assert abs(_w - _c["num"]) > max(_c["tol"] or 0, abs(_c["num"]) * 0.02) * 3, (_t["id"], _k, _w, "Fehlwert zu nah an der Lösung")
            continue
        _opt = [f[2] for f in _t["fields"] if f[0] == _k][0]
        for _o in _m: assert _o in _opt, (_t["id"], _k, _o)
        assert _t["chk"][_k].get("sel") not in _m, (_t["id"], _k, "Rückmeldung für die richtige Antwort")
    _alle = [_t["q"], _t.get("hint", "")] + [z for _a, zz in _t["sol"] for z in zz] + [f[1] for f in _t["fields"]] + [o for f in _t["fields"] if len(f) > 2 for o in f[2]]
    for _x in _alle:
        for _z in "⇌√≈":
            assert _z not in _x, (_t["id"], _z, "Zeichen fehlt in der PDF-Schrift")
    assert len(_t.get("tipps", [])) in (0, 3), (_t["id"], "Tipp-Stufen: genau drei oder keine")

# Rechenkontrolle (vom Aufgabentext aus gerechnet)
assert 10 ** (5 - 2) == 1000
assert round(10 ** 0.1, 2) == 1.26 and round((10 ** 0.1 - 1) * 100) == 26
assert round((10 ** 0.11 - 1) * 100) == 29 and round((10 ** 0.15 - 1) * 100) == 41 and round(10 ** 0.13, 2) == 1.35

GRP = {1: STUNDENNAME[1] + " (Buch S. 53–55)",
       2: STUNDENNAME[2] + " (Buch S. 56–59)",
       3: STUNDENNAME[3] + " (Buch S. 59–61) · VERSUCH K1.5-V1",
       4: STUNDENNAME[4] + " (Buch S. 61–62, 65)",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)"}

LERNZIELE = ["**Säuren** und **Basen** an ihren Teilchen (**H₃O⁺**, **OH⁻**) und mit **Indikatoren** erkennen – und Beispiele aus Alltag, Körper und Dienst nennen",
             "eine **Säure-Base-Reaktion** als **Weitergabe eines Protons** beschreiben und in einer einfachen **Gleichung** zeigen, wer abgibt und wer aufnimmt",
             "den **pH-Wert** von Proben **messen**, auf der Skala von 0 bis 14 einordnen und wissen, dass jede Stufe ein **Faktor 10** ist",
             "die **Neutralisation** erklären und sagen, wie **Atmung und Puffer** deinen **Blut-pH** zwischen 7,35 und 7,45 halten – und wie du dich vor **Verätzungen** schützt"]

WICHTIGSTE = ["**Säuren** geben in Wasser **H⁺-Ionen (Protonen)** ab; daraus wird **H₃O⁺**. Sie färben Lackmus rot und Rotkrautsaft rot bis rosa.",
              "**Basen** bilden in Wasser **OH⁻-Ionen**; ihre Lösung heißt **Lauge**. Laugen sind oft gefährlicher, als sie sich anfühlen – vor allem für die Augen.",
              "Nach **Brønsted** ist eine Säure-Base-Reaktion ein **Protonen-Pingpong**: Die **Säure gibt** ein H⁺ ab, die **Base nimmt** es auf. Wasser kann beides (**Ampholyt**).",
              "Der **pH-Wert** reicht von 0 bis 14: unter 7 **sauer**, 7 **neutral**, über 7 **basisch**. Jede Stufe ist ein **Faktor 10**.",
              "Bei der **Neutralisation** wird aus **H₃O⁺ + OH⁻** wieder **Wasser** (und ein Salz). So halten auch **Puffer und Atmung** dein Blut bei pH 7,4."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Säure", "Teilchen bzw. Stoff, der in Wasser H⁺-Ionen (Protonen) abgibt – nach Brønsted ein Protonenspender (Protonendonator)"],
                ["Base", "Teilchen bzw. Stoff, der H⁺-Ionen aufnimmt – nach Brønsted ein Protonenempfänger (Protonenakzeptor); Metallhydroxide bilden in Wasser OH⁻-Ionen"],
                ["Lauge (alkalische Lösung)", "Lösung einer Base in Wasser, z. B. Natronlauge; alkalisch = basisch"],
                ["Proton (H⁺-Ion)", "Wasserstoff-Atom ohne sein Elektron – nur der positiv geladene Kern"],
                ["Oxonium-Ion H₃O⁺", "Wassermolekül mit einem zusätzlichen Proton; macht eine Lösung sauer (vereinfacht oft H⁺ geschrieben)"],
                ["Hydroxid-Ion OH⁻", "negativ geladenes Ion aus Sauerstoff und Wasserstoff; macht eine Lösung basisch"],
                ["Säurerest-Ion", "was von der Säure nach Abgabe des Protons übrig bleibt, z. B. Cl⁻ (Chlorid) aus Salzsäure"],
                ["Protolyse", "Säure-Base-Reaktion, bei der ein Proton von der Säure auf die Base übergeht"],
                ["Säure-Base-Paar", "zwei Teilchen, die sich nur um ein Proton unterscheiden, z. B. HCl und Cl⁻ oder NH₄⁺ und NH₃"],
                ["Ampholyt", "Teilchen, das Säure und Base sein kann – das bekannteste ist Wasser"],
                ["Indikator", "Farbstoff, der durch seine Farbe anzeigt, ob eine Lösung sauer, neutral oder basisch ist (Lackmus, Rotkrautsaft, Universalindikator)"],
                ["pH-Wert", "Zahl von 0 bis 14, die angibt, wie sauer oder basisch eine wässrige Lösung ist; eine Stufe = Faktor 10 bei den H₃O⁺-Ionen; hat keine Einheit"],
                ["neutral", "pH 7 – gleich viele H₃O⁺- und OH⁻-Ionen, z. B. reines Wasser"],
                ["Säureschutzmantel", "dünner, leicht saurer Film aus Schweiß und Talg auf der Haut (pH etwa 5 bis 5,5), der Keime abwehrt; »pH-hautneutral« heißt: an diesen Wert angepasst"],
                ["pH-Meter", "Messgerät, das den pH-Wert elektrisch und genauer bestimmt als Indikatorpapier"],
                ["Neutralisation", "Säure und Base heben sich auf; bei Säure + Lauge im Kern H₃O⁺ + OH⁻ → 2 H₂O, dazu entsteht ein Salz und Wärme (exotherm)"],
                ["Salz", "Ionenverbindung aus Metall-Ionen und Säurerest-Ionen, z. B. Natriumchlorid NaCl"],
                ["Puffer", "Lösung, die den pH-Wert fast konstant hält, wenn etwas Säure oder Base dazukommt – im Blut vor allem Kohlensäure/Hydrogencarbonat"],
                ["Verätzung", "Schädigung von Haut oder Auge durch Säuren oder Laugen; erste Hilfe: sofort lange mit viel Wasser spülen"]]

# ---------------------------------------------------------------- Wiederholen
WEISST_DU_NOCH = {
    1: [("Aus K1.3: Was wandert bei einer Redoxreaktion?", "Elektronen. Heute wandert etwas anderes: ein Proton."),
        ("Ein Wasserstoff-Atom gibt sein einziges Elektron ab. Was bleibt übrig?", "Ein Proton – ein H⁺-Ion."),
        ("Was ist ein Ion?", "Ein geladenes Teilchen – es hat Elektronen abgegeben oder aufgenommen.")],
    2: [("Welches Teilchen geben Säuren ab?", "Ein H⁺-Ion (Proton); im Wasser wird daraus H₃O⁺."),
        ("Welche Farbe hatte Rotkrautsaft mit Essig?", "Rot bis rosa – Essig ist sauer."),
        ("Welche Säure ist in Cola?", "Phosphorsäure.")],
    3: [("Wer ist bei HCl + H₂O → Cl⁻ + H₃O⁺ die Base?", "H₂O – es nimmt das Proton auf."),
        ("Was ist ein Ampholyt?", "Ein Teilchen, das Säure und Base sein kann – z. B. Wasser."),
        ("Was gilt beim Verdünnen von Säuren?", "Erst das Wasser, dann die Säure.")],
    4: [("pH 3 und pH 5: Wievielmal mehr H₃O⁺ hat pH 3?", "100-mal (zwei Stufen, je Faktor 10)."),
        ("Welche Probe war im Versuch basisch?", "Natronlösung (und Seifenlösung)."),
        ("Warum ist Mineralwasser leicht sauer?", "Gelöstes CO₂ bildet Kohlensäure.")],
}

STOPPFRAGEN = {
    "saeuren": [("Warum rülpst man nach Mineralwasser?", "Die Kohlensäure zerfällt wieder in Wasser und CO₂ – das Gas will raus (Buch S. 54)."),
                ("Woran erkennt man eine Säure ohne Kosten?", "Am Indikator: Lackmus wird rot, Rotkrautsaft rot bis rosa, Indikatorpapier gelb bis rot.")],
    "basen": [("Warum fühlt sich Seifenlauge glitschig an?", "Laugen greifen Fett und Eiweiß der obersten Hautschicht an – das fühlt sich seifig an."),
              ("Wie verdünnt man eine Säure richtig?", "Erst das Wasser, dann langsam die Säure dazu – nie umgekehrt.")],
    "protolyse": [("Wer ist bei NH₃ + H₂O → NH₄⁺ + OH⁻ die Säure?", "H₂O – es gibt ein Proton an NH₃ ab."),
                  ("Warum ist Ammoniaklösung basisch?", "Weil dabei OH⁻-Ionen entstehen.")],
    "ph": [("pH 2 gegen pH 4: Wievielmal mehr H₃O⁺?", "100-mal."),
           ("Ist Meerwasser mit pH 8,1 sauer?", "Nein, basisch – es wird nur weniger basisch.")],
    "messen": [("Warum ist Indikatorpapier keine genaue Messung?", "Man vergleicht nur Farben mit einer Skala – das ist eine Schätzung in ganzen Stufen."),
               ("Hat der pH-Wert eine Einheit?", "Nein.")],
    "neutral": [("Was entsteht bei der Neutralisation von Salzsäure mit Natronlauge?", "Kochsalzlösung (NaCl in Wasser) und Wärme."),
                ("Warum schäumt Essig mit Natron?", "Natron nimmt Protonen auf; dabei entsteht CO₂.")],
    "blut": [("In welchem Bereich liegt der Blut-pH normal?", "Zwischen 7,35 und 7,45."),
             ("Wie hilft die Atmung dem Blut-pH?", "Mit dem ausgeatmeten CO₂ verschwindet Kohlensäure aus dem Blut.")],
}

# ABCD-Fragen für »Weißt du noch?« und Vermutungen (Stephan 15.11.2026: digital statt Zettel – die Kadetten zeigen die ABCD-Karte am Handy).
# (Frage, richtige Antwort, [drei falsche], Erklärung). Die Präsentation mischt die Reihenfolge, die richtige steht nicht immer bei A.
WDN_ABCD = {
    1: [("Was wandert bei einer Redoxreaktion (K1.3) von einem Teilchen zum anderen?", "Elektronen", ["Protonen", "Neutronen", "Atomkerne"], "Elektronen. Heute wandert etwas anderes: ein Proton."),
        ("Ein Wasserstoff-Atom gibt sein einziges Elektron ab. Was bleibt übrig?", "ein Proton (H⁺-Ion)", ["ein Neutron", "ein Wasserstoff-Molekül", "gar nichts"], "Übrig bleibt der Kern: ein Proton, also ein H⁺-Ion."),
        ("Was ist ein Ion?", "ein geladenes Teilchen", ["ein ungeladenes Atom", "ein kleines Molekül", "ein freies Elektron"], "Ein Ion hat Elektronen abgegeben oder aufgenommen – es ist geladen.")],
    2: [("Welches Teilchen geben Säuren in Wasser ab?", "H⁺ (ein Proton)", ["OH⁻", "Elektronen", "Na⁺"], "H⁺ – im Wasser wird daraus H₃O⁺."),
        ("Rotkrautsaft und Essig: Welche Farbe?", "rot bis rosa", ["blau", "grün", "gelb"], "Rot bis rosa – Essig ist sauer."),
        ("Welche Säure steckt in Cola – neben der Kohlensäure?", "Phosphorsäure", ["Salzsäure", "Schwefelsäure", "Essigsäure"], "Phosphorsäure (Buch S. 54).")],
    3: [("HCl + H₂O → Cl⁻ + H₃O⁺: Wer fängt das Proton?", "H₂O", ["HCl", "Cl⁻", "niemand"], "Wasser nimmt das Proton auf – hier ist Wasser die Base."),
        ("Ein Teilchen, das Säure UND Base sein kann, heißt …", "Ampholyt", ["Indikator", "Puffer", "Oxonium-Ion"], "Ampholyt – zum Beispiel Wasser."),
        ("Säure verdünnen: Was kommt zuerst ins Gefäß?", "das Wasser", ["die Säure", "egal", "beides gleichzeitig"], "Erst das Wasser, dann die Säure – sonst kann es spritzen.")],
    4: [("pH 3 und pH 5: Wievielmal mehr H₃O⁺ hat pH 3?", "100-mal", ["2-mal", "20-mal", "1000-mal"], "Zwei Stufen, je Faktor 10: 10 · 10 = 100."),
        ("Welche Probe war im Versuch basisch?", "Natronlösung", ["Cola", "Zitronensaft", "Mineralwasser"], "Natronlösung (pH um 8) – und die Seifenlösung."),
        ("Warum ist prickelndes Mineralwasser leicht sauer?", "Gelöstes CO₂ bildet Kohlensäure", ["wegen der Mineralstoffe", "es enthält Salzsäure", "es ist gar nicht sauer"], "CO₂ + H₂O → H₂CO₃ (Kohlensäure).")],
}
VERMUTUNG_ABCD = {   # DEMO-Vermutungen, ebenfalls mit der ABCD-Karte
    "K1.5-D1": [("Rotkrautsaft + Essig wird …", "rot bis rosa", ["blau", "grün", "bleibt violett"], "Rot bis rosa – Essig ist sauer."),
                ("Rotkrautsaft + Natron wird …", "blau bis grün-blau", ["rot", "gelb", "bleibt violett"], "Blau bis grün-blau – Natron ist schwach basisch.")],
    "K1.5-D3": [("Was passiert, wenn man Atemluft in Rotkrautsaft bläst?", "er wird etwas violetter (saurer)", ["er wird grün", "er wird gelb", "nichts – Luft ist neutral"], "Atemluft enthält CO₂ – daraus wird Kohlensäure."),
                ("Und was passiert danach mit Natron?", "es schäumt, die Farbe geht zurück", ["es wird rot", "es wird gelb", "nichts"], "Natron fängt die Protonen ab, CO₂ entweicht – die Säure wird neutralisiert.")],
}
for _n, _qs in list(WDN_ABCD.items()) + list(VERMUTUNG_ABCD.items()):
    for _q in _qs: assert len(_q) == 4 and len(set([_q[1]] + _q[2])) == 4, _q

# Mitarbeits-Check (Stephan 15.11.2026: nach jeder Einheit ein kurzer Kontroll-Check mit Benotung, kein Test; GitHub, 10 Fragen).
# Nur Pflichtstoff (keine Zusatzaufgaben, kein Militärbezug). Gruppen: aus jeder Gruppe werden so viele Fragen gezogen, wie "n" sagt (Summe 10).
# Jede Frage: (id, Frage, richtige Antwort, [drei falsche], Buchseite). "faktor" wird mit Zufallszahlen gebaut (siehe check.py).
CHECK = [
    {"thema": "Säuren", "n": 2, "fragen": [
        ("s1", "Welches Teilchen gibt eine Säure in Wasser ab?", "ein H⁺-Ion (Proton)", ["ein OH⁻-Ion", "ein Elektron", "ein Na⁺-Ion"], "S. 54"),
        ("s2", "Welches Ion macht eine Lösung sauer?", "H₃O⁺ (Oxonium-Ion)", ["OH⁻ (Hydroxid-Ion)", "Cl⁻ (Chlorid-Ion)", "Na⁺ (Natrium-Ion)"], "S. 58–59"),
        ("s3", "Rotkrautsaft wird in einer Lösung rot bis rosa. Die Lösung ist …", "sauer", ["basisch", "neutral", "eine Lauge"], "S. 55"),
        ("s4", "Was ist ein Indikator?", "ein Farbstoff, der je nach pH-Wert die Farbe wechselt", ["ein Gerät, das Strom misst", "ein Stoff, der jede Säure neutralisiert", "eine besonders starke Base"], "S. 54–55")]},
    {"thema": "Laugen", "n": 1, "fragen": [
        ("l1", "Welches Ion macht eine Lösung basisch?", "OH⁻ (Hydroxid-Ion)", ["H₃O⁺ (Oxonium-Ion)", "H⁺ (Proton)", "Cl⁻ (Chlorid-Ion)"], "S. 56"),
        ("l2", "Welche dieser Flüssigkeiten ist eine Lauge?", "Rohrreiniger (pH über 13)", ["Zitronensaft", "Cola", "Speiseessig"], "S. 56–57")]},
    {"thema": "Protonen-Pingpong", "n": 2, "fragen": [
        ("b1", "HCl + H₂O → Cl⁻ + H₃O⁺: Welches Teilchen ist hier die Base?", "H₂O", ["HCl", "Cl⁻", "H₃O⁺"], "S. 58"),
        ("b2", "NH₃ + H₂O → NH₄⁺ + OH⁻: Wer gibt hier das Proton ab?", "H₂O", ["NH₃", "NH₄⁺", "OH⁻"], "S. 58"),
        ("b3", "Ein Teilchen, das ein Proton abgeben UND aufnehmen kann, heißt …", "Ampholyt", ["Indikator", "Puffer", "Katalysator"], "S. 59")]},
    {"thema": "pH-Wert", "n": 2, "fragen": [
        ("p1", "Eine Lösung hat pH 9. Sie ist …", "schwach basisch", ["stark sauer", "neutral", "schwach sauer"], "S. 59"),
        ("p2", "faktor", "", [], "S. 60"),
        ("p3", "Welche Probe aus dem Versuch ist basisch?", "Seifenlösung", ["Cola", "Zitronensaft", "Mineralwasser prickelnd"], "S. 61")]},
    {"thema": "Sicherheit", "n": 1, "fragen": [
        ("x1", "Du verdünnst eine Säure. Was kommt zuerst ins Gefäß?", "das Wasser", ["die Säure", "egal", "beides gleichzeitig"], "S. 57"),
        ("x2", "Lauge spritzt dir ins Auge. Was tust du zuerst?", "sofort lange mit viel Wasser spülen", ["mit Essig neutralisieren", "das Auge reiben", "abwarten, ob es brennt"], "S. 53")]},
    {"thema": "Neutralisation und Blut", "n": 2, "fragen": [
        ("n1", "Säure + Lauge → …", "Salz + Wasser", ["Säure + Wasser", "nur Wasserstoff", "Lauge + Salz"], "S. 65"),
        ("n2", "Wie groß ist der normale pH-Wert deines Blutes?", "7,35 bis 7,45", ["6,0 bis 6,5", "8,5 bis 9,0", "genau 7,0"], "S. 62"),
        ("n3", "Warum atmest du nach einem Sprint schneller?", "um CO₂ abzuatmen – das senkt die Säure im Blut", ["um mehr Milchsäure zu bilden", "weil das Blut zu basisch geworden ist", "um Stickstoff aufzunehmen"], "S. 62")]},
]
assert sum(g["n"] for g in CHECK) == 10 and all(g["n"] <= len(g["fragen"]) for g in CHECK)
for _g in CHECK:
    for _q in _g["fragen"]:
        if _q[1] != "faktor": assert len(set([_q[2]] + _q[3])) == 4, _q
CHECK_KEY = "26-27-2AB-K1.5-check"
CHECK_CODE = "7414"   # Startcode – steht nur als Prüfsumme in der Seite; Stephan zeigt ihn am Beamer (Präsentation, Lösungsseite)

PARTNERCHECK = [  # vier Karten für Stunde 4 (Paar: einer fragt, einer antwortet, dann tauschen)
    ("Was ist eine Säure, was eine Base – nach Brønsted?", "Säure gibt ein Proton (H⁺) ab, Base nimmt es auf."),
    ("pH 3 und pH 6 – wievielmal mehr H₃O⁺ hat pH 3?", "1000-mal (drei Stufen, je Faktor 10)."),
    ("Was passiert, wenn Salzsäure auf Natronlauge trifft?", "H₃O⁺ + OH⁻ → 2 H₂O; übrig bleibt Kochsalzlösung, das Glas wird warm."),
    ("Lauge im Auge – was tust du?", "Sofort lange mit viel Wasser spülen, Hilfe holen, nicht neutralisieren. Laugen sind am Auge oft gefährlicher als Säuren."),
]

STOLPERSTEINE = [("»Leitungswasser und destilliertes Wasser sind basisch«",
                  "Stand so in der **Vorjahrestabelle** (Folie »Basische Stoffe«). Richtig: Wr. Neustädter Leitungswasser ist **leicht basisch (7,4–7,6)**, destilliertes Wasser an der Luft **leicht sauer (um 5,5–6, CO₂)**. Im Versuch offen ansprechen."),
                 ("»Natron ist eine Lauge mit OH⁻«",
                  "Natron (NaHCO₃) ist eine **Brønsted-Base**: Das Hydrogencarbonat-Ion **nimmt H⁺ auf**. Es bildet kaum OH⁻ (pH ca. 8,3). Das Buch zählt es »zu den Basen« (S. 56) – passt zu Brønsted."),
                 ("»pH-hautneutral = pH 7«",
                  "**Hautneutral** heißt: etwa der pH der Haut, **leicht sauer** (Buch ca. 5,5; Studie Lambers 2006: im Mittel unter 5). Mit Aufgabe 5 e) und Zusatz 8."),
                 ("»Eine pH-Stufe = ein bisschen saurer«",
                  "Jede Stufe ist ein **Faktor 10** bei den H₃O⁺-Ionen (pH 2 gegen 5 = 1000-mal). Aufgabe 5 c) – typische Fehlantwort 3."),
                 ("»Bei Verätzung neutralisieren« / »Säure ist schlimmer als Lauge«",
                  "Erste Hilfe ist **immer Wasser, lange spülen**, nie neutralisieren. **Laugen** sind am Auge meist **schlimmer** (dringen tiefer ein). Aufgabe 3 e) und »Was glaubst du?« b).")]

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 14.11.2026)
QUELLEN = [
 ("W1", "Pressemitteilung »Sieben von neun planetaren Grenzen überschritten – Ozeanversauerung im Gefahrenbereich« (24.09.2025)", "Potsdam-Institut für Klimafolgenforschung (PIK) über idw",
  "https://idw-online.de/de/news858658", "Oberflächen-pH seit der Industrialisierung um rund 0,1 gesunken; »30 bis 40 Prozent« mehr Versauerung; Flügelschnecken zeigen Schalenschäden", "Seite geöffnet, Kernaussagen gelesen"),
 ("W2", "SRF Wissen: »Saure Ozeane: Nächste Belastungsgrenze der Erde ist überschritten«", "Schweizer Radio und Fernsehen (öffentlich-rechtlich)",
  "https://www.srf.ch/wissen/klimawandel/planetary-health-check-saure-ozeane-naechste-belastungsgrenze-der-erde-ist-ueberschritten", "Meer heute etwa pH 8,1 – leicht basisch", "Textauszug per Websuche gelesen"),
 ("W3", "Trinkwasserverordnung (TWV), Anhang I Teil C – Indikatorparameter", "Republik Österreich, RIS",
  "https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40172725/NOR40172725.pdf", "pH ≥ 6,5 und ≤ 9,5; Wasser soll nicht korrosiv sein", "Textauszug per Websuche gelesen"),
 ("W4", "Unser Trinkwasser – Informationsblatt gemäß § 6 TWV (Jahresmittel 2023)", "Wasserwerk Wiener Neustadt",
  "https://wiener-neustadt.at/files/drive/wrn/content/service/umwelt-abfall/Wasserwerk/a4_wasserwerte_hp_2024.pdf", "pH je Wasserwerk 7,4 bis 7,6; Gesamthärte 15–20 °dH", "PDF geöffnet"),
 ("W5", "Übersicht über den Säure-Basen-Haushalt (MSD Manual, Ausgabe für Patienten, geprüft 03/2025)", "MSD Manuals",
  "https://www.msdmanuals.com/de/heim/nierenerkrankungen/säure-basen-haushalt/übersicht-über-den-säure-basen-haushalt", "Blut-pH normal etwa 7,35–7,45; CO₂-Abgabe über die Lunge regelt den pH", "Textauszug per Websuche gelesen"),
 ("W6", "Plasma acidosis and peak power after a supramaximal trial in elite sprint and endurance cyclists: effect of bicarbonate (Med Sci Sports Exerc 2023, 55(5), 932–944)", "Fachzeitschrift; Eintrag in der Datenbank des IAT Leipzig",
  "https://lida.sport-iat.de/ta/Record/4082134", "Plasma-pH fiel bei 12 Elite-Radfahrern nach 3 min Vollgas (Placebo-Bedingung, ohne Natron) von 7,35 auf 7,13 (Laktat 1,2 → 19,6 mmol/l); Med Sci Sports Exerc 55 (5), 2023, S. 932–944", "Datenbankeintrag geöffnet (Autoren dort nicht angegeben)"),
 ("W7", "»Freispruch für Lactat« (02.10.2026, J. Hauser)", "Pharmazeutische Zeitung, nach einem Beitrag von S. Phillips (Univ. Edinburgh) in The Conversation",
  "https://www.pharmazeutische-zeitung.de/freispruch-fuer-lactat-168904/", "Laktat nach 30–90 min wieder auf Ausgangswert; Muskelkater 1–3 Tage später – Laktat erklärt ihn nicht", "Seite geöffnet"),
 ("W8", "Interview »Einmal zerstörter Zahnschmelz ist verloren« (21.08.2025, F. Jötten mit A. Lussi)", "Spektrum.de; A. Lussi, emeritierter Klinikdirektor Universität Bern",
  "https://www.spektrum.de/news/zahnmedizin-einmal-zerstoerter-zahnschmelz-ist-verloren/2281803", "Energydrinks gehören zu den erosivsten Getränken (Zitronensäure); Calcium senkt die Erosion; der pH-Wert allein entscheidet nicht", "Seite geöffnet"),
 ("W9", "Natural skin surface pH is on average below 5 (Int J Cosmet Sci 2006, Lambers u. a.)", "Fachzeitschrift; Autoren aus der Forschung eines Haushalts- und Körperpflege-Herstellers",
  "https://doi.org/10.1111/j.1467-2494.2006.00344.x", "330 Personen; natürlicher Haut-pH im Mittel etwa 4,7", "Abstract per Websuche gelesen (PubMed von hier gesperrt) – Interessenlage beachten"),
 ("W10", "Augenverätzungen – Gefährdungspotenzial, Notfallversorgung (Thieme) und S1-Leitlinie »Akute Verätzung am Auge« (DOG/BVA, 2021)", "Deutsche Ophthalmologische Gesellschaft",
  "https://register.awmf.org/assets/guidelines/045-018l_S1_Akute-Veraetzung-am-Auge_2021-01_1.pdf", "Säuren: Koagulationsnekrose; Laugen: Kolliquationsnekrose (tiefer); sofort intensiv spülen; Laugenverätzungen häufiger", "Auszüge per Websuche gelesen"),
 ("W11", "Umgang mit Zement / Sicherheitsdatenblatt Frischbeton", "Haufe Arbeitsschutz; Holcim Schweiz (SDB 2022)",
  "https://holcim.ch/sites/switzerland/files/docs/sicherheitsdatenblatt-frischbeton_de-stand-2022-08-01_ae.pdf", "Frischbeton pH 11–13,5; Zementleim über pH 13; Verätzungsgefahr", "Auszüge per Websuche gelesen"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "Trauner-Filmtipp www.trauner.at/sauer (Buch S. 53): von hier aus gesperrt – nicht geöffnet. Er steht als Buch-Hinweis auf der Theorie-Seite; bitte einmal selbst ansehen.",
 "Videos aus deiner Vorjahres-PPP (musstewissen Chemie, studyflix, Chemie Endlich Verstehen, Duden Learnattack): YouTube ist von hier nicht prüfbar. Darum stehen sie nicht auf den Kadetten-Seiten, sondern als Freigabe-Liste auf der Lösungsseite.",
 "PhET »pH Skala: Grundlagen« (HTML5, Deutsch laut PhET-Suche): Seite von hier gesperrt – Handy-Bedienung nicht geprüft. Statt dessen eine eigene pH-Skala zum Schieben auf der Theorie-Seite; PhET als Freigabe-Vorschlag.",
 "Seilnacht-Filmverzeichnis (pteil2.pdf) nur als Suchauszug lesbar – die Filmtitel in »Säuren und Basen« (5 Filme) und »Neutralisation« (4 Filme) sind nicht vollständig sichtbar.",
 "Podcast: Im Jahresplan-Blatt »Podcasts« steht für E8 »kein eindeutiger Treffer« – keiner eingebaut.",
]
