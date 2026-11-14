"""NAWI 4AB · K2.4 Akustik + K3.2 Hör- und Gleichgewichtssinn (Trauner NAWI HAK 4: Teil II »Akustik« S. 60–67, Teil III »Hör- und Gleichgewichtssinn« S. 108–112) – v1.
Grundlage: Auftrag »26-27-4AB-Akustik-Gehoer-Claude-v1« vom 13.11.2026 (Stephan/ChatGPT) – von Claude eigenständig geplant, fachlich geprüft und umgesetzt.
Jahresplan v23: Block »C Akustik, Optik & Sinne«, Einheiten E9 (Akustik, 2 Std., K03, K05) + E10 (Gehör und Gleichgewicht, 2 Std., K07) = 4 Stunden.
Leitidee »Vom Knall zum Kopf«: Quelle → Weg → Stärke → Ohr → Gehirn → Orientierung. Jede Stunde ein Abschnitt dieses Signalwegs.
Keine Daten auf den Kadetten-Seiten (Standard 13.11.2026): Termine trägt Prof. HOLZER im Kalender der privaten Lehrerseite ein.
Versuche: K2.4-V1 (= Jahresplan V4.17, angepasst) und K3.2-V1 (= Jahresplan V4.19, angepasst). V4.18 wird als DEMO K2.4-D2 (Lineal statt Monochord) umgesetzt.
Demos: K2.4-D1 Stimmgabel · K2.4-D2 Lineal · K3.2-D1 Richtungshören · K3.2-D2 drehendes Wasserglas. Keine neuen Jahresplan-Codes.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge).
Rechengrundlage: v = 340 m/s in Luft (Buch S. 61, gilt bei rund 15 °C; bei 20 °C 343 m/s). Wasser 1480 m/s."""

STAND = "14.11.2026"
V = "v1"
ORDNER = "4ab-nawi/k2-4-akustik"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "4ab-nawi/"
EYEBROW = "NAWI · 4AB · K2.4 Akustik · K3.2 Hören und Gleichgewicht"
TITEL = "Vom Knall zum Kopf – Schall, Gehör und Gleichgewicht"
KURZTITEL = "Akustik und Gehör"
BUCH = "Buch S. 60–67, 109–112"
KEY = "26-27-4AB-K2.4-Akustik-TH-Handy-v1"
LERNSEITE_KEY = "26-27-4AB-K2.4-Akustik-Lernseite-Check-v1"
PRAEFIX = "26-27-4AB-K2.4-3.2-Akustik"
KLASSEN = ["4AK", "4BK"]
GRUPPEN = 8            # ca. 26 Kadetten je Klasse: 6 Dreier- und 2 Vierergruppen (Angabe Stephan, Wellen-Einheit)
STUNDEN = 4
V_LUFT = 340           # m/s, Buch S. 61
V_WASSER = 1480        # m/s

VS = {"K2.4-V1": {"titel": "Schallpegel im langen Saal messen", "jp": "V4.17 (angepasst)", "stunde": 2, "aufgabe": 5},
      "K3.2-V1": {"titel": "Luft- und Knochenleitung am eigenen Kopf", "jp": "V4.19 (angepasst, ohne Ohrmodell)", "stunde": 3, "aufgabe": 7}}
DEMOS = {"K2.4-D1": {"titel": "Stimmgabel: sehen, hören, spüren", "jp": "Buch S. 61 und 65 (Stimmgabel #144)", "stunde": 1},
         "K2.4-D2": {"titel": "Lineal an der Tischkante und Tongenerator", "jp": "ersetzt V4.18 (Monochord nicht nachgewiesen)", "stunde": 2},
         "K3.2-D1": {"titel": "Woher kommt das Schnippen?", "jp": "Buch S. 110 (Versuch Richtungshören, ohne Schlauch)", "stunde": 4},
         "K3.2-D2": {"titel": "Drehendes Wasserglas – die träge Lymphe", "jp": "Modell zu Buch S. 112 (nicht im Jahresplan)", "stunde": 4}}

STUNDENNAME = {1: "Stunde 1 · Was ist Schall – und wie schnell ist er?",
               2: "Stunde 2 · Hoch, tief, laut, leise – wie laut ist zu laut?",
               3: "Stunde 3 · Was das Ohr aus Schall macht – und wie du es schützt",
               4: "Stunde 4 · Woher kommt das? Wo bin ich? Richtung und Gleichgewicht"}

STIMMT = ["stimmt", "stimmt nicht"]
JANEIN = ["ja", "nein"]
OHR_TEILE = ["Gehörgang", "Trommelfell", "Gehörknöchelchen", "Schnecke", "Bogengänge", "Hörnerv", "Ohrtrompete"]
WEG = ["Das Trommelfell schwingt mit", "Gehörknöchelchen übertragen und verstärken den Druck",
       "Die Lymphe in der Schnecke wird bewegt", "Haarzellen erzeugen elektrische Signale"]


def _ohr(nr, richtig):
    """Auswahlfeld fürs Beschriften: richtige Antwort zuerst, dann die übrigen Teile."""
    return ["n%d" % nr, "%s) Nummer %d ist …" % ("abcdef"[nr - 1], nr), [richtig] + [x for x in OHR_TEILE if x != richtig]]


def _weg(i, richtig):
    return ["w%d" % i, "%s) %d. Schritt" % ("ghij"[i - 1], i + 1), [richtig] + [x for x in WEG if x != richtig]]


# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 60", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Zwei Schätzfragen zum Start – ohne Punkte, ohne »richtig« oder »falsch«. Entscheide dich einmal. In Stunde 4 schaust du nach, was du heute gedacht hast.",
  "hint": "Einfach tippen, was du vermutest. Deine Antwort bleibt gespeichert.",
  "type": "multi", "vorhersage": True,
  "fields": [["p1", "a) Im Film explodiert ein Raumschiff im Weltall. Hört die Crew im Nachbarschiff den Knall durch den leeren Raum?",
              ["nein, gar nicht", "ja, aber leiser", "ja, genauso laut"], False],
             ["p2", "b) Ein Sturmgewehr wird ohne Gehörschutz abgefeuert. Wie laut ist der Knall am Ohr des Schützen ungefähr (Spitzenwert)?",
              ["über 150 dB", "etwa 100 dB", "etwa 80 dB"], False]],
  "chk": {},
  "aufloesung": [["p1", "nein, gar nicht", "Durch den leeren Raum gibt es keine Teilchen, die den Schall weitergeben. Erst wenn Gas oder Trümmer das Schiff treffen, schwingt dessen Wand – das wäre dann ein Geräusch im Schiff."],
                 ["p2", "über 150 dB", "Am Ohr des Schützen liegt der Knall eines Sturmgewehrs über 160 dB. Schon ein einziger Schuss ohne Gehörschutz kann Haarzellen dauerhaft schädigen."]],
  "sol": [["Auflösung", ["a) nein – im Vakuum breitet sich Schall nicht aus (Buch S. 61). Was Filme zeigen, ist Fiktion.",
                         "b) über 150 dB – am Ohr des Schützen über 160 dB (Spitzenpegel). Darum ist Gehörschutz beim Schießen Pflicht."]]],
  "tipps": [], "tip": ["Schall ist eine Druckwelle", "theorie.html#schall"]},

 {"id": "a1", "nr": 2, "title": "Schall unterwegs", "src": "Buch S. 61", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 6, "marke": "SELBSTSTUDIUM",
  "q": "Fünf kurze Auswahlfragen. Denk bei jeder an das Bild mit den schwingenden Luftteilchen.",
  "hint": "Die Teilchen bleiben ungefähr an ihrem Platz. Was wandert dann eigentlich?",
  "type": "multi",
  "fields": [["was", "a) Was wandert bei Schall in der Luft vom Lautsprecher zu deinem Ohr?",
              ["eine Druckschwankung – die Luftteilchen schwingen nur hin und her", "die Luft selbst strömt zum Ohr", "kleine Schallteilchen fliegen durch die Luft"]],
             ["richtung", "b) In welche Richtung schwingen die Luftteilchen?",
              ["längs – in Ausbreitungsrichtung vor und zurück", "quer – auf und ab", "gar nicht"]],
             ["kurve", "c) Warum zeichnet man Schall trotzdem oft als Wellenlinie?",
              ["Die Linie zeigt, wie der Luftdruck an einer Stelle schwankt", "Die Luftteilchen bewegen sich auf und ab", "Schall ist eigentlich eine Wasserwelle"]],
             ["vakuum", "d) Warum gibt es im Vakuum keinen Schall?",
              ["Es gibt keine Teilchen, die sich anstoßen können", "Im Vakuum ist es zu kalt", "Das Vakuum verschluckt den Schall wie ein Schwamm"]],
             ["schnell", "e) Wo ist Schall am schnellsten?", ["in Stahl", "in Wasser", "in Luft"]]],
  "chk": {"was": {"sel": "eine Druckschwankung – die Luftteilchen schwingen nur hin und her"},
          "richtung": {"sel": "längs – in Ausbreitungsrichtung vor und zurück"},
          "kurve": {"sel": "Die Linie zeigt, wie der Luftdruck an einer Stelle schwankt"},
          "vakuum": {"sel": "Es gibt keine Teilchen, die sich anstoßen können"},
          "schnell": {"sel": "in Stahl"}},
  "fb": {"was": {"die Luft selbst strömt zum Ohr": "Dann gäbe es bei jedem Ton Wind. Die Luft bleibt, nur die Verdichtung wandert weiter.",
                 "kleine Schallteilchen fliegen durch die Luft": "Schall besteht nicht aus eigenen Teilchen. Er ist ein Zustand der Luft: dichter, dünner, dichter …"},
         "richtung": {"quer – auf und ab": "Das wäre eine Querwelle wie beim Seil. Schall in Luft ist eine Längswelle.",
                      "gar nicht": "Die Teilchen schwingen schon – nur ganz wenig und nur hin und her."},
         "kurve": {"Die Luftteilchen bewegen sich auf und ab": "Die Kurve ist ein Diagramm: nach oben Überdruck, nach unten Unterdruck.",
                   "Schall ist eigentlich eine Wasserwelle": "Schall braucht kein Wasser – Luft, Wasser und feste Stoffe leiten ihn."},
         "vakuum": {"Im Vakuum ist es zu kalt": "Kälte allein verhindert Schall nicht. Entscheidend ist, ob Teilchen da sind.",
                    "Das Vakuum verschluckt den Schall wie ein Schwamm": "Im Vakuum ist nichts, was verschlucken könnte – es fehlt der Träger."},
         "schnell": {"in Wasser": "Wasser ist schneller als Luft, aber feste Stoffe wie Stahl sind noch schneller.",
                     "in Luft": "Luft ist der langsamste der drei Stoffe: etwa 340 m/s."}},
  "sol": [["Lösung", ["a) eine Druckschwankung – die Teilchen schwingen nur um ihren Platz.",
                      "b) längs (longitudinal) – in Ausbreitungsrichtung vor und zurück.",
                      "c) Die Wellenlinie ist ein Diagramm des Luftdrucks an einer Stelle (oben Überdruck, unten Unterdruck).",
                      "d) Ohne Teilchen kann keine Verdichtung weitergegeben werden.",
                      "e) in Stahl (rund 5000 m/s), Wasser rund 1480 m/s, Luft rund 340 m/s."]]],
  "tipps": ["Stell dir eine Menschenkette vor, in der jeder seinen Nachbarn kurz anschubst. Wer bewegt sich weit – und was wandert durch die Kette?",
            "k1",
            "Lies im Buch S. 61 den Abschnitt »Schallfeld und Schallausbreitung« und den Versuch mit dem Wecker unter der Glocke."],
  "tip": ["Schall ist eine Druckwelle", "theorie.html#schall"]},

 {"id": "a2", "nr": 3, "title": "Rechnen mit Schall: Gewitter, Echo, Wellenlänge", "src": "Buch-Aufgabe S. 67/1", "own": False, "tag": "Stunde 1", "h": 1, "zeit": 10, "marke": "SELBSTSTUDIUM",
  "q": "Rechne mit v = 340 m/s (Luft bei rund 15 °C). Schreib bei jeder Rechnung die Einheit dazu. Licht des Blitzes darfst du als »sofort da« rechnen.",
  "hint": "Formel: s = v · t. Beim Echo läuft der Schall hin UND zurück.",
  "type": "multi",
  "fields": [["gewitter", "a) Nach einem Blitz hörst du den Donner 6 s später. Wie weit ist das Gewitter entfernt? (mit Einheit)"],
             ["licht", "b) Warum darf man das Licht des Blitzes als »sofort da« rechnen?",
              ["Licht ist fast eine Million Mal schneller als Schall", "Licht braucht genau 3 s pro Kilometer", "Der Blitz ist näher als der Donner"]],
             ["echo", "c) Ihr ruft gegen eine Felswand. Das Echo kommt nach 1,2 s zurück. Wie weit ist die Wand entfernt? (mit Einheit)"],
             ["lambda", "d) Der Kammerton a' hat 440 Hz. Berechne seine Wellenlänge in Luft mit λ = v / f (mit Einheit, auf zwei Kommastellen)."],
             ["winter", "e) Bei 0 °C ist Schall in Luft nur etwa 331 m/s schnell. Was heißt das für die Gewitter-Faustregel »Sekunden durch 3 = Kilometer«?",
              ["Sie bleibt brauchbar – der Unterschied ist nur etwa 3 %", "Sie stimmt im Winter überhaupt nicht", "Im Winter ist Schall schneller als im Sommer"]]],
  "chk": {"gewitter": {"num": 2040, "unit": "m", "tol": 41},
          "licht": {"sel": "Licht ist fast eine Million Mal schneller als Schall"},
          "echo": {"num": 204, "unit": "m", "tol": 4},
          "lambda": {"num": 0.7727, "unit": "m", "tol": 0.0155},
          "winter": {"sel": "Sie bleibt brauchbar – der Unterschied ist nur etwa 3 %"}},
  "fb": {"gewitter": [[56.7, "Du hast v durch t geteilt. Der Weg ist s = v · t."], [18, "Faustregel: Sekunden durch 3 ergibt Kilometer – nicht mal 3."]],
         "echo": [[408, "Das ist der ganze Weg hin und zurück. Die Wand ist nur halb so weit weg."]],
         "lambda": [[1.294, "Du hast f durch v geteilt. Es heißt λ = v / f."], [149600, "Nicht mal, sondern geteilt: λ = v / f."]],
         "licht": {"Licht braucht genau 3 s pro Kilometer": "Die 3 s pro Kilometer gelten für den Schall. Licht schafft 300 000 km in einer Sekunde.",
                   "Der Blitz ist näher als der Donner": "Blitz und Donner entstehen am selben Ort – nur kommen sie verschieden schnell an."},
         "winter": {"Sie stimmt im Winter überhaupt nicht": "Rechne nach: 331 statt 340 m/s ist nur ein kleiner Unterschied.",
                    "Im Winter ist Schall schneller als im Sommer": "Umgekehrt: In wärmerer Luft ist Schall schneller."}},
  "sol": [["Lösung", ["a) s = v · t = 340 m/s · 6 s = 2040 m ≈ 2,0 km (Faustregel: 6 : 3 = 2 km).",
                      "b) Licht ist mit 300 000 km/s fast eine Million Mal schneller als Schall – seine Laufzeit ist hier vernachlässigbar.",
                      "c) Hin und zurück: 340 m/s · 1,2 s = 408 m. Die Wand ist halb so weit weg: 204 m.",
                      "d) λ = v / f = 340 m/s : 440 Hz = 0,77 m (gerundet).",
                      "e) Brauchbar: (340 − 331) : 340 sind etwa 3 % – für eine Schätzung egal."]]],
  "tipps": ["Bei c) zuerst den ganzen Weg ausrechnen, den der Schall läuft. Wie viel davon ist der Weg zur Wand?",
            "k2",
            "Lies im Buch S. 61 die Gewitterregel und auf S. 67 Aufgabe 1. Die Formel λ = v / f kennst du aus der Wellenlehre (Buch S. 55)."],
  "tip": ["Wie schnell ist Schall?", "theorie.html#tempo"]},

 # --------------------------------------------------------------- Stunde 2
 {"id": "a3", "nr": 4, "title": "Die Dezibel-Leiter", "src": "Buch S. 64, 110", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 7, "marke": "SELBSTSTUDIUM",
  "q": "Sechs Auswahl- und Rechenfragen zur Dezibel-Skala. Merke: Jede Stufe von 10 dB heißt zehnmal so viel Schallintensität.",
  "hint": "Intensität und Schalldruck sind nicht dasselbe. Schau dir die Leiter auf der Theorie-Karte an.",
  "type": "multi",
  "fields": [["i10", "a) +10 dB bedeuten für die Schallintensität …", ["zehnmal so viel", "doppelt so viel", "10 % mehr"]],
             ["p10", "b) … und für den Schalldruck?", ["etwa 3,2-mal so viel", "zehnmal so viel", "hundertmal so viel"]],
             ["p20", "c) +20 dB bedeuten für den Schalldruck …", ["zehnmal so viel", "zwanzigmal so viel", "hundertmal so viel"]],
             ["kopfh", "d) Kopfhörer mit 100 dB gegen ein Gespräch mit 60 dB: Wievielmal größer ist die Schallintensität? (nur die Zahl)"],
             ["zwei", "e) Zwei gleich laute Maschinen mit je 80 dB laufen gleichzeitig. Wie hoch ist der Pegel ungefähr?", ["etwa 83 dB", "160 dB", "genau 80 dB"]],
             ["empf", "f) Eine App zeigt 3 dB mehr als vorher. Klingt es jetzt doppelt so laut?",
              ["Nein – doppelt so laut empfinden die meisten erst bei rund 10 dB mehr", "Ja, 3 dB mehr sind doppelt so laut", "Das zeigt die App direkt an"]]],
  "chk": {"i10": {"sel": "zehnmal so viel"}, "p10": {"sel": "etwa 3,2-mal so viel"}, "p20": {"sel": "zehnmal so viel"},
          "kopfh": {"num": 10000, "unit": "", "tol": 1},
          "zwei": {"sel": "etwa 83 dB"},
          "empf": {"sel": "Nein – doppelt so laut empfinden die meisten erst bei rund 10 dB mehr"}},
  "fb": {"i10": {"doppelt so viel": "Doppelte Intensität sind nur etwa +3 dB.", "10 % mehr": "Die Dezibel-Skala zählt in Faktoren, nicht in Prozent."},
         "p10": {"zehnmal so viel": "Genau dieser Fehler stand auf einer Folie im Vorjahr. Zehnfach ist die Intensität – der Schalldruck nur etwa 3,2-fach.",
                 "hundertmal so viel": "Hundertfach wird die Intensität erst bei +20 dB."},
         "p20": {"zwanzigmal so viel": "Dezibel addieren sich, die Faktoren multiplizieren sich: 3,2 · 3,2 …",
                 "hundertmal so viel": "Hundertfach ist bei +20 dB die Intensität, nicht der Schalldruck."},
         "zwei": {"160 dB": "Dezibel darf man nicht einfach addieren. Zwei gleiche Quellen = doppelte Intensität.",
                  "genau 80 dB": "Zwei Maschinen geben mehr Energie ab als eine – ein bisschen steigt der Pegel schon."},
         "empf": {"Ja, 3 dB mehr sind doppelt so laut": "3 dB mehr ist doppelte Intensität. Unser Ohr empfindet das nur als etwas lauter.",
                  "Das zeigt die App direkt an": "Die App misst den Pegel. Wie laut es klingt, ist unsere Empfindung."}},
  "sol": [["Lösung", ["a) zehnmal so viel Intensität.",
                      "b) etwa 3,2-mal so viel Schalldruck (3,2 · 3,2 ≈ 10).",
                      "c) zehnmal so viel Schalldruck (Intensität hundertfach).",
                      "d) 40 dB Unterschied = vier Zehnerstufen: 10 · 10 · 10 · 10 = 10 000-mal so viel Intensität.",
                      "e) etwa 83 dB – doppelte Intensität ergibt rund +3 dB.",
                      "f) Nein. Als etwa doppelt so laut empfinden die meisten rund +10 dB (grobe Faustregel, hängt auch von der Frequenz ab)."]]],
  "tipps": ["Zähle bei d) die Zehnerstufen zwischen 60 dB und 100 dB. Jede Stufe heißt: mal 10.",
            "k4",
            "Lies im Buch S. 64 den Abschnitt »Lautstärke (Schalldruckpegel)« mit dem Kasten über das Addieren von Lautstärken."],
  "tip": ["Dezibel: die Leiter in Zehnerschritten", "theorie.html#dezibel"]},

 {"id": "a4", "nr": 5, "title": "VERSUCH K2.4-V1: Schallpegel im langen Saal", "src": "Buch S. 62–64", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 14, "marke": "VERSUCH",
  "versuch": "K2.4-V1",
  "q": "Ihr messt, wie der Schall mit dem Abstand schwächer wird. Vorne spielt ein Lautsprecher einen gleichmäßigen Ton. "
       "Jede Gruppe misst mit EINEM Handy und dem Pegelmesser unten. Jeder trägt die Werte seiner Gruppe in sein eigenes Arbeitsblatt ein.",
  "hint": "Das Handy ist kein geeichtes Messgerät. Darum vergleichen wir nur: Alle setzen am Lehrertisch die Referenz auf 0 dB und messen dann an ihrem Platz.",
  "type": "multi", "pegel": True,
  "fields": [["grp", "a) Gruppe Nr. · mit (Vornamen genügen)"],
             ["abstand", "b) Unser Messplatz: Abstand zum Lautsprecher in m (steht auf dem Klebezettel am Boden)"],
             ["ruhe", "c) Grundgeräusch an unserem Platz, Ton AUS (relativ zur Referenz, in dB)"],
             ["ton", "d) Ton AN an unserem Platz (relativ zur Referenz, in dB)"],
             ["beob", "e) Was habt ihr beobachtet? (1–2 Sätze, nur was ihr gemessen habt)"],
             ["saal", "f) Im Freien sinkt der Pegel bei doppeltem Abstand um etwa 6 dB. Im Saal war der Abfall meist kleiner. Warum?",
              ["Wände, Decke und Boden werfen Schall zurück", "Schall wird mit dem Abstand schneller", "Die Handys hinten messen immer lauter"]],
             ["schluss", "g) Was heißt das für den Gehörschutz auf dem Schießplatz? (1 Satz)"]],
  "chk": {"saal": {"sel": "Wände, Decke und Boden werfen Schall zurück"},
          "beob": {"kw": [["Wert genannt", r"db|dezibel|leiser|schwaecher|schwächer|weniger|minus|-\s?\d|sank|abnahm|nahm ab"]], "man": True},
          "schluss": {"kw": [["Abstand hilft", r"abstand|weiter weg|entfernung|distanz"], ["trotzdem schützen", r"gehoerschutz|gehörschutz|trotzdem|reicht nicht|nicht genug|immer|tragen|stoepsel|stöpsel|kapsel"]], "need": 1, "man": True}},
  "fb": {"saal": {"Schall wird mit dem Abstand schneller": "Die Schallgeschwindigkeit bleibt gleich. Es kommt Schall auf mehreren Wegen an.",
                  "Die Handys hinten messen immer lauter": "Wir haben alle Handys am Lehrertisch auf 0 dB gesetzt – genau deshalb."}},
  "sol": [["Erwartung (Beispielwerte – eure Werte sind anders)",
           ["Bei 1 m Referenz 0 dB, bei 2 m etwa −4 bis −6 dB, bei 4 m etwa −7 bis −11 dB, bei 8 m etwa −9 bis −15 dB.",
            "f) Wände, Decke, Boden und Möbel werfen Schall zurück (Nachhall). Im Freien wären es −6 dB pro Abstandsverdopplung.",
            "g) Abstand hilft, reicht beim Schießen aber nicht: Die Spitzenwerte bleiben weit über der Gefahrengrenze – Gehörschutz tragen."]]],
  "tipps": ["Vergleiche zuerst die Werte der Klasse am Beamer: Gruppen mit doppeltem Abstand – wie viele dB weniger?",
            "k4",
            "Lies im Buch S. 62 den Kasten »Gründe für die Abnahme der Schallintensität«."],
  "tip": ["Versuch: Pegel messen", "theorie.html#messen"]},

 # --------------------------------------------------------------- Stunde 3
 {"id": "a5", "nr": 6, "title": "Der Weg ins Ohr", "src": "Buch-Aufgabe S. 112/4", "own": False, "tag": "Stunde 3", "h": 3, "zeit": 10, "marke": "SELBSTSTUDIUM",
  "img": "img/ohr-nummern.svg",
  "q": "a) bis f): Beschrifte die Zeichnung – wähle zu jeder Nummer den richtigen Teil. Ein Begriff bleibt übrig. "
       "g) bis j): Der Schall ist im Gehörgang angekommen. Bring die vier nächsten Schritte in die richtige Reihenfolge. k) Wozu braucht das Ohr die Gehörknöchelchen?",
  "hint": "Folge dem Schall von außen nach innen: Luft – Haut – Knochen – Flüssigkeit – Nerv.",
  "type": "multi",
  "fields": [_ohr(1, "Gehörgang"), _ohr(2, "Trommelfell"), _ohr(3, "Gehörknöchelchen"), _ohr(4, "Bogengänge"), _ohr(5, "Schnecke"), _ohr(6, "Hörnerv"),
             _weg(1, WEG[0]), _weg(2, WEG[1]), _weg(3, WEG[2]), _weg(4, WEG[3]),
             ["knochen", "k) Wozu braucht das Ohr die Gehörknöchelchen?",
              ["Sie verstärken den Druck, damit die Schwingung von der Luft in die Flüssigkeit der Schnecke kommt", "Sie verwandeln Schall in elektrischen Strom", "Sie halten Wasser vom Trommelfell fern"]]],
  "chk": dict([("n1", {"sel": "Gehörgang"}), ("n2", {"sel": "Trommelfell"}), ("n3", {"sel": "Gehörknöchelchen"}), ("n4", {"sel": "Bogengänge"}),
               ("n5", {"sel": "Schnecke"}), ("n6", {"sel": "Hörnerv"})]
              + [("w%d" % (i + 1), {"sel": WEG[i]}) for i in range(4)]
              + [("knochen", {"sel": "Sie verstärken den Druck, damit die Schwingung von der Luft in die Flüssigkeit der Schnecke kommt"})]),
  "fb": {"knochen": {"Sie verwandeln Schall in elektrischen Strom": "Das machen erst die Haarzellen in der Schnecke.",
                     "Sie halten Wasser vom Trommelfell fern": "Die Gehörknöchelchen liegen hinter dem Trommelfell, im luftgefüllten Mittelohr."}},
  "sol": [["Lösung", ["1 Gehörgang · 2 Trommelfell · 3 Gehörknöchelchen (Hammer, Amboss, Steigbügel) · 4 Bogengänge · 5 Schnecke · 6 Hörnerv. Übrig bleibt die Ohrtrompete.",
                      "Reihenfolge: Trommelfell schwingt → Gehörknöchelchen übertragen und verstärken → Lymphe in der Schnecke wird bewegt → Haarzellen erzeugen elektrische Signale (→ Hörnerv → Gehirn).",
                      "k) Druckverstärkung (etwa 22-fach): große Fläche des Trommelfells auf das kleine ovale Fenster plus Hebelwirkung. Sonst würde fast der ganze Schall an der Flüssigkeit zurückgeworfen."]]],
  "tipps": ["Die Schnecke sieht aus wie ein Schneckenhaus, die Bogengänge wie drei Ringe darüber.",
            "k5",
            "Lies im Buch S. 109 die Tabelle zu Außen-, Mittel- und Innenohr und auf S. 110 den Abschnitt »Hörvorgang«."],
  "tip": ["Der Weg ins Ohr", "theorie.html#ohr"]},

 {"id": "a6", "nr": 7, "title": "VERSUCH K3.2-V1: Luft- und Knochenleitung", "src": "Buch S. 109–110", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 5, "marke": "VERSUCH",
  "versuch": "K3.2-V1",
  "q": "Ein Mini-Versuch am eigenen Kopf, ohne Material. 1. Summe leise einen Ton. 2. Halte dir mit den Zeigefingern beide Ohren zu und summe gleich weiter. "
       "3. Denk an eine Sprachnachricht mit deiner eigenen Stimme: Wie klingt sie für dich?",
  "hint": "Finger nur auf den Ohrknorpel drücken, nicht in den Gehörgang stecken. Kein Schreien, kein Ton direkt ins Ohr.",
  "type": "multi",
  "fields": [["beob", "a) Mit zugehaltenen Ohren klang mein Summen …", ["lauter oder dumpfer", "leiser", "genau gleich"], False],
             ["weg", "b) Auf welchem Weg kommt dein Summen jetzt zur Schnecke?",
              ["über die Schädelknochen (Knochenleitung)", "über den Gehörgang (Luftleitung)", "gar nicht – du bildest es dir ein"]],
             ["stimme", "c) Warum klingt deine Stimme in einer Sprachnachricht fremd? (1–2 Sätze)"]],
  "chk": {"weg": {"sel": "über die Schädelknochen (Knochenleitung)"},
          "stimme": {"kw": [["Knochenleitung", r"knochen|schaedel|schädel|kopf|innen"], ["Luftleitung / Aufnahme", r"luft|nur von aussen|nur von außen|mikrofon|aufnahme|handy"]], "need": 1, "man": True}},
  "fb": {"weg": {"über den Gehörgang (Luftleitung)": "Den Gehörgang hast du gerade zugehalten.",
                 "gar nicht – du bildest es dir ein": "Du hörst es wirklich – der Schall nimmt einen anderen Weg."}},
  "sol": [["Lösung", ["a) Meist lauter und dumpfer (tiefe Töne kommen stärker an). Das ist eine Beobachtung – wer »leiser« notiert, schreibt es ehrlich auf.",
                      "b) Knochenleitung: Die Schwingung läuft über die Schädelknochen direkt zur Schnecke; mit zugehaltenen Ohren entweicht weniger tiefer Schall nach außen.",
                      "c) Beim Sprechen hörst du dich über Luft- UND Knochenleitung (diese betont tiefe Töne). Das Mikrofon nimmt nur die Luftleitung auf – darum klingt die Aufnahme dünner und fremd."]]],
  "tipps": ["Was ist anders, wenn der Gehörgang zu ist? Woher kann der Schall dann noch kommen?",
            "k5",
            "Im Buch S. 109 siehst du, wie nahe die Schnecke am Schädelknochen (Felsenbein) liegt."],
  "tip": ["Luft- und Knochenleitung", "theorie.html#ohr"]},

 {"id": "a7", "nr": 8, "title": "Statement-Check: Noise-Cancelling statt Gehörschutz?", "src": "Buch S. 109–110", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 6, "marke": "SELBSTSTUDIUM",
  "q": "Beispiel-Aussage (erfunden): Ein Fitness-Influencer sagt in einem Video: »Beim Schießen trag ich einfach meine Noise-Cancelling-Earbuds. Die machen eh alles leise.« "
       "Prüf die Aussage mit dem, was du über Haarzellen und Gehörschutz weißt. Ohne KI.",
  "hint": "Frag dich: Woher weiß er das? Und was passiert bei einem kurzen, sehr lauten Knall im Innenohr?",
  "type": "multi",
  "fields": [["stimmt", "a) Stimmt die Aussage?", JANEIN[::-1]],
             ["warum", "b) Welche Begründung passt am besten?",
              ["ANC-Kopfhörer sind kein geprüfter Gehörschutz und wirken vor allem gegen gleichmäßige tiefe Geräusche – ein Schuss ist ein kurzer, extrem lauter Knall",
               "ANC macht den Schall schneller", "Earbuds sind zu klein für Schall"]],
             ["haar", "c) Was schädigt ein Knalltrauma im Innenohr?", ["die Haarzellen in der Schnecke", "die Ohrmuschel", "das Ohrenschmalz"]],
             ["tinn", "d) Was ist ein Tinnitus?", ["ein Ohrgeräusch ohne äußere Schallquelle", "eine Entzündung des Gehörgangs", "ein Teil des Gleichgewichtsorgans"]],
             ["quelle", "e) Woran erkennst du, dass die Aussage keine gute Quelle ist?",
              ["Er nennt keine Messung und keine Prüfung – nur seine Meinung", "Er hat sehr viele Follower", "Das Video ist kurz"]],
             ["antwort", "f) Schreib ihm eine Antwort in zwei Sätzen: Was soll er stattdessen tragen – und warum?"]],
  "chk": {"stimmt": {"sel": "nein"},
          "warum": {"sel": "ANC-Kopfhörer sind kein geprüfter Gehörschutz und wirken vor allem gegen gleichmäßige tiefe Geräusche – ein Schuss ist ein kurzer, extrem lauter Knall"},
          "haar": {"sel": "die Haarzellen in der Schnecke"},
          "tinn": {"sel": "ein Ohrgeräusch ohne äußere Schallquelle"},
          "quelle": {"sel": "Er nennt keine Messung und keine Prüfung – nur seine Meinung"},
          "antwort": {"kw": [["geprüfter Gehörschutz", r"gehoerschutz|gehörschutz|stoepsel|stöpsel|kapsel|otoplastik|zertifiz|gepruef|geprüf|en 352"],
                             ["Begründung", r"haarzell|knall|innenohr|kaputt|schaed|schäd|tinnitus|zu laut|spitze|wachsen nicht"]], "need": 2, "man": True}},
  "fb": {"stimmt": {"ja": "Schau dir an, wofür ANC gebaut ist – und wofür nicht."},
         "warum": {"ANC macht den Schall schneller": "ANC ändert nichts an der Schallgeschwindigkeit. Es erzeugt Gegenschall.",
                   "Earbuds sind zu klein für Schall": "Auch kleine Stöpsel können sehr gut dämmen – wenn sie dafür gebaut und geprüft sind."},
         "haar": {"die Ohrmuschel": "Die Ohrmuschel sammelt nur den Schall. Der Schaden entsteht tief innen.",
                  "das Ohrenschmalz": "Ohrenschmalz schützt den Gehörgang – mit dem Knalltrauma hat es nichts zu tun."},
         "tinn": {"eine Entzündung des Gehörgangs": "Das wäre eine Gehörgangsentzündung (Otitis externa).",
                  "ein Teil des Gleichgewichtsorgans": "Tinnitus ist ein Symptom, kein Organ."},
         "quelle": {"Er hat sehr viele Follower": "Viele Follower sagen nichts darüber, ob etwas stimmt.",
                    "Das Video ist kurz": "Auch kurze Videos können stimmen – entscheidend ist, woher er es weiß."}},
  "sol": [["Lösung", ["a) nein.",
                      "b) ANC dämpft vor allem gleichmäßige, tiefe Geräusche und ist kein geprüfter Gehörschutz (EN 352). Gegen einen Schuss mit über 150 dB Spitzenpegel schützt es nicht.",
                      "c) die Haarzellen der Schnecke – sie wachsen nicht nach.",
                      "d) ein Ohrgeräusch ohne äußere Schallquelle (Pfeifen, Rauschen, Klingeln).",
                      "e) keine Messung, keine Prüfung, keine Fachquelle – nur Meinung (Quellenkritik: Woher weiß er das?).",
                      "f) Beispiel: »Trag geprüften Gehörschutz – Kapsel oder richtig eingesetzte Stöpsel. ANC ist dafür nicht gemacht, und ein Knall kann Haarzellen für immer zerstören.«"]]],
  "tipps": ["Wofür wurde Noise-Cancelling erfunden: Flugzeug, Zug, Büro – oder Schießplatz?",
            "k6",
            "Lies im Buch S. 109 den Einstieg zum Hörsinn (Lärm am Arbeitsplatz) und auf S. 110 die Tabelle der Lautstärken."],
  "tip": ["Hörschäden und Gehörschutz", "theorie.html#schutz"]},

 # --------------------------------------------------------------- Stunde 4
 {"id": "a8", "nr": 9, "title": "Orientierung: Richtung und Gleichgewicht", "src": "Buch-Aufgabe S. 112/6", "own": False, "tag": "Stunde 4", "h": 4, "zeit": 12, "marke": "SELBSTSTUDIUM",
  "q": "a) und b) zum Richtungshören, c) bis g) zum Gleichgewichtssinn. Bei a) rechnest du mit v = 340 m/s. Bei g) schreibst du einen Satz.",
  "hint": "Lagesinn = Vorhofsäckchen mit Kalkkristallen. Drehsinn = Bogengänge mit träger Lymphe.",
  "type": "multi",
  "fields": [["dt", "a) Ein Knall kommt genau von links. Zum rechten Ohr hat der Schall etwa 0,2 m Umweg. Wie viel später kommt er dort an? Gib das Ergebnis in Millisekunden (ms) an."],
             ["vorne", "b) Warum kannst du »genau vorne« und »genau hinten« schlechter unterscheiden?",
              ["Beide Ohren bekommen den Schall gleichzeitig und gleich laut", "Von hinten kommt kein Schall ins Ohr", "Die Ohrmuschel ist hinten taub"]],
             ["lage", "c) Welches Organ meldet: »Der Kopf ist geneigt«?", ["die Vorhofsäckchen mit den Kalkkristallen", "die Bogengänge", "die Schnecke"]],
             ["dreh", "d) Welches Organ meldet: »Der Kopf beginnt sich zu drehen«?", ["die Bogengänge", "die Vorhofsäckchen", "das Trommelfell"]],
             ["schwindel", "e) Warum wird dir schwindlig, wenn du nach langem Drehen plötzlich stehen bleibst?",
              ["Die träge Lymphe fließt noch weiter und meldet eine Drehung, die es nicht mehr gibt", "Das Blut sammelt sich in den Ohren", "Die Kalkkristalle fallen aus dem Ohr"]],
             ["pilot", "f) Eine Pilotin fliegt in den Wolken eine lange, gleichmäßige Kurve. Nach einiger Zeit fühlt es sich an wie Geradeausflug. Warum?",
              ["Die Bogengänge melden nur Änderungen der Drehung – bei gleichmäßiger Drehung meldet die Lymphe nichts mehr", "Die Schnecke hört das Triebwerk nicht mehr", "Die Wolken drücken auf das Trommelfell"]],
             ["tun", "g) Was muss die Pilotin tun? (1 Satz)"]],
  "chk": {"dt": {"num": 0.5882, "unit": "ms", "tol": 0.0118},
          "vorne": {"sel": "Beide Ohren bekommen den Schall gleichzeitig und gleich laut"},
          "lage": {"sel": "die Vorhofsäckchen mit den Kalkkristallen"},
          "dreh": {"sel": "die Bogengänge"},
          "schwindel": {"sel": "Die träge Lymphe fließt noch weiter und meldet eine Drehung, die es nicht mehr gibt"},
          "pilot": {"sel": "Die Bogengänge melden nur Änderungen der Drehung – bei gleichmäßiger Drehung meldet die Lymphe nichts mehr"},
          "tun": {"kw": [["Instrumente", r"instrument|anzeige|kuenstlicher horizont|künstlicher horizont|cockpit|geraet|gerät|fluglage"], ["nicht dem Gefühl", r"gefuehl|gefühl|nicht vertrauen|nicht dem koerper|nicht dem körper|vertrau"]], "need": 1, "man": True}},
  "fb": {"dt": [[68, "Nicht mal, sondern geteilt: t = s / v."], [1700, "Du hast v durch s geteilt. Die Zeit ist t = s / v."], [0.000588, "Das sind Sekunden. Rechne noch in Millisekunden um (· 1000)."], [0.00059, "Das sind Sekunden. Rechne noch in Millisekunden um (· 1000)."], [0.0006, "Das sind Sekunden. Rechne noch in Millisekunden um (· 1000)."]],
         "vorne": {"Von hinten kommt kein Schall ins Ohr": "Doch – du hörst auch, was hinter dir passiert. Nur der Unterschied zwischen den Ohren fehlt.",
                   "Die Ohrmuschel ist hinten taub": "Die Ohrmuschel hilft sogar beim Unterscheiden – durch ihre Form."},
         "lage": {"die Bogengänge": "Die Bogengänge melden Drehungen, nicht die Lage im Stillstand.", "die Schnecke": "Die Schnecke ist fürs Hören zuständig."},
         "dreh": {"die Vorhofsäckchen": "Die Vorhofsäckchen melden Lage und Beschleunigung geradeaus.", "das Trommelfell": "Das Trommelfell gehört zum Hören."},
         "schwindel": {"Das Blut sammelt sich in den Ohren": "Mit dem Blut hat der Drehschwindel nichts zu tun – denk an die Flüssigkeit in den Bogengängen.",
                       "Die Kalkkristalle fallen aus dem Ohr": "Die Kristalle liegen fest auf ihrer Gallertschicht im Vorhof."},
         "pilot": {"Die Schnecke hört das Triebwerk nicht mehr": "Mit dem Hören hat die Täuschung nichts zu tun.",
                   "Die Wolken drücken auf das Trommelfell": "Wolken üben keinen spürbaren Druck aus. Es geht um den Drehsinn."}},
  "sol": [["Lösung", ["a) t = s / v = 0,2 m : 340 m/s = 0,00059 s ≈ 0,59 ms (rund 0,6 ms).",
                      "b) Von vorne und hinten sind die Wege zu beiden Ohren gleich lang – kein Zeit- und kein Pegelunterschied. Hilfe: Form der Ohrmuschel, Kopf drehen.",
                      "c) die Vorhofsäckchen (Lagesinn): Kalkkristalle folgen der Schwerkraft und biegen die Sinneshärchen.",
                      "d) die Bogengänge (Drehsinn): Sie reagieren auf Drehbeschleunigung.",
                      "e) Die Lymphe ist träge: Beim Stoppen fließt sie weiter und biegt die Gallertkuppel – das Gehirn meldet eine Drehung, die Augen widersprechen.",
                      "f) Bei gleichmäßiger Drehung hat sich die Lymphe angepasst; nur Änderungen werden gemeldet.",
                      "g) Den Instrumenten (z. B. künstlicher Horizont) vertrauen, nicht dem Gefühl."]]],
  "tipps": ["Bei a): t = s / v. Rechne zuerst in Sekunden, dann mal 1000 für Millisekunden.",
            "k8",
            "Lies im Buch S. 110 den Abschnitt »Richtungshören« und auf S. 112 die Abschnitte »Lagesinn« und »Drehsinn«."],
  "tip": ["Gleichgewicht: Lage- und Drehsinn", "theorie.html#gleichgewicht"]},

 # --------------------------------------------------------------- Zusatz
 {"id": "z1", "nr": 10, "title": "Echolot und Fledermaus", "src": "Buch S. 60, 66–67", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Ein Echolot sendet Ultraschall zum Seegrund, eine Fledermaus ruft im Ultraschall. a) Das Signal des Echolots kommt nach 0,08 s zurück. Wasser: v = 1480 m/s. Wie tief ist der See? "
       "b) Das Echo eines Insekts kommt bei der Fledermaus nach 6 ms an. Luft: v = 340 m/s. Wie weit ist das Insekt entfernt? c) Warum nutzt die Fledermaus Ultraschall?",
  "hint": "Beides sind Echos: hin und zurück. Bei b) zuerst 6 ms in Sekunden umrechnen.",
  "type": "multi",
  "fields": [["tiefe", "a) Tiefe des Sees (mit Einheit)"], ["insekt", "b) Entfernung des Insekts (mit Einheit)"],
             ["warum", "c) Warum Ultraschall?", ["Kurze Wellen werden auch von kleinen Insekten deutlich zurückgeworfen", "Ultraschall ist für Menschen besonders laut", "Tiefe Töne gibt es nachts nicht"]]],
  "chk": {"tiefe": {"num": 59.2, "unit": "m", "tol": 1.2}, "insekt": {"num": 1.02, "unit": "m", "tol": 0.03},
          "warum": {"sel": "Kurze Wellen werden auch von kleinen Insekten deutlich zurückgeworfen"}},
  "fb": {"tiefe": [[118.4, "Das ist der Weg hin und zurück. Der See ist nur halb so tief."]],
         "insekt": [[2.04, "Das ist der Weg hin und zurück. Das Insekt ist nur halb so weit weg."], [2040, "Zuerst 6 ms in Sekunden umrechnen: 6 ms = 0,006 s."], [1020, "Zuerst 6 ms in Sekunden umrechnen: 6 ms = 0,006 s."]],
         "warum": {"Ultraschall ist für Menschen besonders laut": "Wir hören Ultraschall gar nicht.", "Tiefe Töne gibt es nachts nicht": "Tiefe Töne gibt es immer – sie wären nur zu »grob« für kleine Beute."}},
  "sol": [["Lösung", ["a) 1480 m/s · 0,08 s = 118,4 m hin und zurück → 59,2 m tief.",
                      "b) 340 m/s · 0,006 s = 2,04 m hin und zurück → 1,02 m.",
                      "c) Ultraschall hat sehr kurze Wellenlängen (bei 50 kHz etwa 7 mm). Kleine Insekten werfen solche Wellen gut zurück – tiefe Töne mit Wellenlängen von Metern »umfließen« sie."]]],
  "tipps": [], "tip": ["Ultraschall und Infraschall", "theorie.html#tonhoehe"]},

 {"id": "z2", "nr": 11, "title": "KI-Fehlerjagd: Fünf Sätze über Dezibel", "src": "Buch S. 64", "own": True, "tag": "Zusatz", "h": 0, "zeit": 6,
  "q": "Eine KI hat Dezibel so erklärt. Genau drei Sätze sind falsch. Entscheide bei jedem Satz. f) Verbessere einen der falschen Sätze. Ohne KI – der Text ist schon da.",
  "hint": "Denk an die Dezibel-Leiter und an die Theorie-Karte zum Gehörschutz.",
  "type": "multi",
  "fields": [["s1", "a) »Dezibel ist eine Skala in Zehnerschritten (logarithmisch).«", STIMMT, False],
             ["s2", "b) »10 dB mehr bedeuten zehnmal so viel Schalldruck.«", STIMMT, False],
             ["s3", "c) »Zwei Rasenmäher mit je 90 dB ergeben zusammen 180 dB.«", STIMMT, False],
             ["s4", "d) »Wer jeden Tag viele Stunden über 85 dB ausgesetzt ist, gefährdet sein Gehör.«", STIMMT, False],
             ["s5", "e) »Noise-Cancelling-Kopfhörer sind ein zertifizierter Gehörschutz.«", STIMMT, False],
             ["fix", "f) Ein falscher Satz – richtig formuliert"]],
  "chk": {"s1": {"sel": "stimmt"}, "s2": {"sel": "stimmt nicht"}, "s3": {"sel": "stimmt nicht"}, "s4": {"sel": "stimmt"}, "s5": {"sel": "stimmt nicht"},
          "fix": {"kw": [["Korrektur", r"intensit|3,2|3\.2|drei komma|93|83|plus 3|\+ ?3|kein gehoerschutz|kein gehörschutz|nicht zertifiziert|nicht gepruef|nicht geprüf|nicht zugelassen"]], "man": True}},
  "fb": {"s1": {"stimmt nicht": "Genau das macht Dezibel aus: Jede 10-dB-Stufe ist ein Faktor 10 in der Intensität."},
         "s2": {"stimmt": "Zehnfach wird die Intensität, der Schalldruck nur etwa 3,2-fach."},
         "s3": {"stimmt": "Dezibel addiert man nicht. Doppelte Intensität ≈ +3 dB."},
         "s4": {"stimmt nicht": "In Österreich muss ab 85 dB am Arbeitsplatz Gehörschutz getragen werden – aus genau diesem Grund."},
         "s5": {"stimmt": "ANC-Kopfhörer sind nicht als Gehörschutz geprüft und im Lärmbereich nicht zulässig."}},
  "sol": [["Lösung", ["a) stimmt · b) stimmt nicht (Intensität ×10, Schalldruck ×3,2) · c) stimmt nicht (etwa 93 dB) · d) stimmt · e) stimmt nicht (kein geprüfter Gehörschutz).",
                      "f) z. B. »10 dB mehr bedeuten zehnmal so viel Schallintensität« oder »Zwei Rasenmäher mit je 90 dB ergeben etwa 93 dB.«"]]],
  "tipps": [], "tip": ["Dezibel: die Leiter in Zehnerschritten", "theorie.html#dezibel"]},

 {"id": "z3", "nr": 12, "title": "60 Sekunden Gehörschutz-Briefing", "src": "Buch S. 109–110", "own": True, "tag": "Zusatz", "h": 0, "zeit": 20,
  "q": "Wahlaufgabe: Erstelle für neue Rekruten ein Gehörschutz-Briefing – als Podcast (höchstens 60 s) ODER als Plakat (A3, Handschrift). "
       "Pflichtinhalte: Haarzellen wachsen nicht nach · ab 85 dB Gehörschutz · Knall ist besonders gefährlich · ANC ist kein Gehörschutz · ein Tipp, wie man Stöpsel richtig einsetzt. "
       "Allein oder zu zweit. KI erlaubt nur fürs Ideensammeln – dann schreibst du dazu, was du gefragt und was du selbst geändert hast. "
       "Nur eigene Stimme, keine fremde Musik, keine Namen anderer. Abgabe: Datei bzw. Foto des Plakats in LMS.",
  "hint": "Fachlich richtig vor schön. Kurz, klar, wie ein echtes Briefing.",
  "type": "multi",
  "fields": [["info", "Titel · Form (Podcast oder Plakat) · 1–2 Sätze zum Inhalt · hochgeladen in LMS am …"]],
  "chk": {"info": {"kw": [["Angaben", r"podcast|plakat|lms|hochgeladen"]], "man": True}},
  "sol": [["Bewertungsraster (10 Punkte)", ["fachlich richtig 4 · alle fünf Pflichtinhalte 2 · verständlich und gegliedert 2 · kreativ 1 · Länge und Abgabe eingehalten 1.",
                                           "Muster: »Euer Gehör hat nur einen Satz Haarzellen – kaputt ist kaputt. Ab 85 dB gilt: Gehörschutz auf. Ein Schuss liegt über 150 dB … Earbuds mit ANC zählen nicht. Stöpsel: rollen, Ohr nach hinten oben ziehen, einsetzen, halten bis er sich ausdehnt.«"]]],
  "tipps": [], "tip": ["Hörschäden und Gehörschutz", "theorie.html#schutz"]},
]

# ---------------------------------------------------------------- Kontrollen
assert [t["nr"] for t in T] == list(range(1, 13))
PFLICHT = [t["nr"] for t in T if t["tag"] != "Zusatz" and not t.get("vorhersage")]
assert PFLICHT == [2, 3, 4, 5, 6, 7, 8, 9], PFLICHT
BESPRECHEN = [3, 5, 8, 9]
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
            for _w, _txt in _m: assert abs(_w - _c["num"]) > (_c["tol"] or 0) * 3, (_t["id"], _k, _w, "typischer Fehlwert liegt zu nah an der Lösung")
            continue
        _opt = [f[2] for f in _t["fields"] if f[0] == _k][0]
        for _o in _m: assert _o in _opt, (_t["id"], _k, _o)
        assert _t["chk"][_k].get("sel") not in _m, (_t["id"], _k, "Rückmeldung für die richtige Antwort")
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz] + [f[1] for f in _t["fields"]]:
        assert "√" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
    assert len(_t.get("tipps", [])) in (0, 3), (_t["id"], "Tipp-Stufen: genau drei oder keine")
# a2 »stimmt« (Statement-Check): richtige Antwort »nein« steht nach JANEIN[::-1] an erster Stelle
assert T[7]["fields"][0][2][0] == "nein"

# Rechenkontrolle (vom Aufgabentext aus gerechnet)
assert V_LUFT * 6 == 2040 and abs(V_LUFT * 1.2 / 2 - 204) < 1e-9
assert abs(round(V_LUFT / 440, 2) - 0.77) < 1e-9 and abs((340 - 331) / 340 - 0.0265) < 0.001
assert 10 ** ((100 - 60) / 10) == 10000 and abs(10 * __import__("math").log10(2) - 3.01) < 0.01
assert abs(10 ** (10 / 20) - 3.162) < 0.001 and abs(10 ** (20 / 20) - 10) < 1e-9
assert abs(0.2 / V_LUFT * 1000 - 0.588) < 0.001 and abs(round(0.2 / V_LUFT * 1000, 2) - 0.59) < 1e-9
assert abs(V_WASSER * 0.08 / 2 - 59.2) < 1e-9 and abs(V_LUFT * 0.006 / 2 - 1.02) < 1e-9
assert abs(10 * __import__("math").log10(2) + 90 - 93) < 0.1
assert abs(300_000_000 / V_LUFT - 882_353) < 1   # »fast eine Million Mal«

GRP = {1: STUNDENNAME[1] + " (Buch S. 60–61, 67)",
       2: STUNDENNAME[2] + " (Buch S. 62–64) · VERSUCH K2.4-V1",
       3: STUNDENNAME[3] + " (Buch S. 109–110) · VERSUCH K3.2-V1",
       4: STUNDENNAME[4] + " (Buch S. 110–112)",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)"}

LERNZIELE = ["**Schall als Druckwelle** erklären und die Größen **Frequenz, Amplitude, Wellenlänge, Schallgeschwindigkeit und Schalldruckpegel** richtig zuordnen",
             "mit **s = v · t** und **v = λ · f** Entfernungen, Echos und Laufzeiten berechnen",
             "einen **Schallpegel vergleichend messen** und Dezibel-Werte richtig deuten – auch für **Gehörschutz** beim Schießen, im Konzert und mit Kopfhörern",
             "erklären, wie das **Ohr** aus Druckschwankungen **Nervensignale** macht und wie **Richtungshören** und **Gleichgewichtssinn** funktionieren"]

WICHTIGSTE = ["**Schall** ist eine Druckwelle: Die Teilchen schwingen nur hin und her, weiter wandert die Verdichtung. Ohne Teilchen (**Vakuum**) gibt es keinen Schall.",
              "In Luft ist Schall rund **340 m/s** schnell (wärmer = schneller). Es gilt **s = v · t**, beim Echo zählt der Weg **hin und zurück**.",
              "Die **Frequenz** bestimmt die **Tonhöhe**, die **Amplitude** die Stärke. **+10 dB** heißt **zehnfache Intensität** – aber nur etwa **3,2-facher Schalldruck**.",
              "Im Ohr verstärken die **Gehörknöchelchen** den Druck; die **Haarzellen** in der Schnecke machen daraus **elektrische Signale**. Kaputte Haarzellen **wachsen nicht nach**.",
              "Die **Vorhofsäckchen** melden Lage und Beschleunigung geradeaus, die **Bogengänge** Drehbeschleunigung – deshalb täuschen uns lange gleichmäßige Drehungen."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Schall", "mechanische Welle in Gas, Flüssigkeit oder festem Stoff; in Luft eine Druck- und Dichtewelle"],
                ["Longitudinalwelle (Längswelle)", "Welle, bei der die Teilchen in Ausbreitungsrichtung hin und her schwingen – so breitet sich Schall in Luft aus"],
                ["Schalldruck p", "Schwankung des Luftdrucks um den normalen Luftdruck, Einheit Pascal (Pa)"],
                ["Frequenz f", "Schwingungen pro Sekunde, Einheit Hertz (Hz); bestimmt die Tonhöhe"],
                ["Amplitude", "größte Auslenkung bzw. größte Druckschwankung; größere Amplitude = stärkerer Schall"],
                ["Wellenlänge λ", "Abstand zweier gleicher Stellen der Welle, Einheit m; es gilt v = λ · f"],
                ["Schallgeschwindigkeit v", "in Luft etwa 340 m/s (bei 15 °C; 343 m/s bei 20 °C), in Wasser etwa 1480 m/s, in Stahl rund 5000 m/s"],
                ["Echo", "zurückgeworfener Schall; die gemessene Zeit gilt für Hin- und Rückweg"],
                ["Schallintensität I", "Schallenergie pro Fläche und Zeit, Einheit W/m²"],
                ["Schalldruckpegel L", "physikalisches Maß in Dezibel (dB); +10 dB = zehnfache Intensität, etwa 3,2-facher Schalldruck"],
                ["Lautstärke", "wie laut wir einen Schall empfinden; hängt vom Pegel UND von der Frequenz ab (Buch: Einheit phon)"],
                ["Hörbereich", "etwa 20 Hz bis 20 000 Hz bei jungen Menschen; nimmt mit dem Alter nach oben hin ab"],
                ["Infraschall / Ultraschall", "Schall unter 20 Hz bzw. über 20 000 Hz – für Menschen nicht hörbar"],
                ["Resonanzkörper", "Hohlkörper oder Platte, die mitschwingt und den Schall verstärkt (Gitarre, Resonanzkasten der Stimmgabel)"],
                ["Trommelfell", "dünne Haut zwischen Außen- und Mittelohr; schwingt mit dem Schall"],
                ["Gehörknöchelchen", "Hammer, Amboss, Steigbügel im Mittelohr; übertragen die Schwingung und verstärken den Druck am ovalen Fenster etwa 22-fach"],
                ["Ohrtrompete", "Verbindung von Mittelohr und Rachen; gleicht den Luftdruck aus (Druck auf den Ohren beim Fliegen)"],
                ["Schnecke", "Teil des Innenohrs mit Lymphe und dem Corti-Organ"],
                ["Haarzellen (Corti-Organ)", "Sinneszellen, die Schwingungen in elektrische Signale umwandeln; wachsen beim Menschen nicht nach"],
                ["Luftleitung / Knochenleitung", "Schall erreicht die Schnecke über Gehörgang und Mittelohr – oder direkt über die Schädelknochen"],
                ["Knalltrauma", "Schädigung des Innenohrs durch einen kurzen, extrem lauten Knall (z. B. Schuss)"],
                ["Tinnitus", "Ohrgeräusch (Pfeifen, Rauschen) ohne äußere Schallquelle"],
                ["Richtungshören", "Orten einer Schallquelle aus Zeit- und Pegelunterschieden zwischen beiden Ohren"],
                ["Vorhofsäckchen (Lagesinn)", "Sinnesfelder mit Kalkkristallen; melden Neigung (Schwerkraft) und Beschleunigung geradeaus"],
                ["Bogengänge (Drehsinn)", "drei flüssigkeitsgefüllte Ringe in drei Ebenen; melden Drehbeschleunigung"],
                ["Lymphe", "Flüssigkeit im Innenohr; ihre Trägheit macht den Drehsinn möglich"]]

# ---------------------------------------------------------------- Wiederholen
WEISST_DU_NOCH = {
    1: [("Aus der Wellenlehre: Was gibt die Frequenz an?", "Schwingungen pro Sekunde – Einheit Hertz (Hz)."),
        ("Bei welcher Welle schwingen die Teilchen in Ausbreitungsrichtung?", "Bei der Längswelle (longitudinal)."),
        ("v = λ · f – was ist λ?", "Die Wellenlänge in Metern.")],
    2: [("Schwingen die Luftteilchen mit dem Schall bis zu deinem Ohr?", "Nein – sie schwingen nur hin und her, die Druckwelle wandert."),
        ("Echo nach 2 s, v = 340 m/s: Wie weit ist die Wand?", "340 m – der Schall läuft 680 m hin und zurück."),
        ("Warum hört man im Weltall keine Explosion?", "Es gibt keine Teilchen, die den Schall weitergeben.")],
    3: [("+10 dB: wievielmal so viel Intensität?", "Zehnmal so viel (Schalldruck etwa 3,2-mal)."),
        ("Was bestimmt die Tonhöhe?", "Die Frequenz."),
        ("Warum war der Pegelabfall im Saal kleiner als im Freien?", "Wände, Decke und Boden werfen Schall zurück.")],
    4: [("Welche Zellen machen aus Schwingungen elektrische Signale?", "Die Haarzellen im Corti-Organ der Schnecke."),
        ("Ist ein Noise-Cancelling-Kopfhörer ein Gehörschutz?", "Nein – er ist nicht als Gehörschutz geprüft."),
        ("Wozu sind die Gehörknöchelchen da?", "Sie übertragen die Schwingung und verstärken den Druck am ovalen Fenster.")],
}

STOPPFRAGEN = {
    "schall": [("Wandert die Luft vom Lautsprecher zu dir?", "Nein. Die Teilchen schwingen nur um ihren Platz; die Verdichtung wandert weiter."),
               ("Was zeigt die Wellenlinie in einer Schallzeichnung?", "Den Luftdruck an einer Stelle: oben Überdruck, unten Unterdruck.")],
    "tempo": [("Donner 9 s nach dem Blitz – wie weit ungefähr?", "9 : 3 = 3 km (genauer 340 m/s · 9 s = 3060 m)."),
              ("Echo nach 0,5 s – wie weit ist die Wand?", "340 m/s · 0,5 s = 170 m hin und zurück, also 85 m.")],
    "tonhoehe": [("Ein Lineal schwingt kürzer über die Tischkante. Was passiert mit dem Ton?", "Er wird höher – die kürzere Zunge schwingt öfter pro Sekunde."),
                 ("Was ist Ultraschall?", "Schall über 20 000 Hz – für Menschen nicht hörbar.")],
    "dezibel": [("70 dB gegen 90 dB: Wievielmal Intensität?", "100-mal (zwei Zehnerstufen)."),
                ("Ist Lautstärke dasselbe wie Schalldruckpegel?", "Nein. Der Pegel ist gemessen, die Lautstärke ist die Empfindung – sie hängt auch von der Frequenz ab.")],
    "ohr": [("Was würde ohne Gehörknöchelchen passieren?", "Fast der ganze Schall würde an der Flüssigkeit der Schnecke zurückgeworfen – wir hörten viel schlechter."),
            ("Wo wird aus Schwingung ein elektrisches Signal?", "In den Haarzellen des Corti-Organs in der Schnecke.")],
    "schutz": [("Warum ist ein einzelner Schuss ohne Gehörschutz gefährlich?", "Der Spitzenpegel liegt weit über 150 dB und kann Haarzellen sofort zerstören."),
               ("Schützt Noise-Cancelling beim Schießen?", "Nein – nicht als Gehörschutz geprüft, wirkt vor allem gegen gleichmäßige tiefe Geräusche.")],
    "richtung": [("Welche zwei Unterschiede nutzt das Gehirn zum Orten?", "Den Zeitunterschied und den Pegelunterschied zwischen den Ohren."),
                 ("Wie groß ist der Zeitunterschied höchstens?", "Etwa 0,6 Millisekunden.")],
    "gleichgewicht": [("Was melden die Bogengänge?", "Drehbeschleunigung – Beginn und Ende einer Drehung."),
                      ("Warum wird man seekrank?", "Augen und Gleichgewichtsorgan melden Widersprüchliches (Deck scheint ruhig, Körper schwankt).")],
}

STOLPERSTEINE = [("»+10 dB = zehnfacher Schalldruck«",
                  "Falsch – stand so auf **Vorjahresfolie 39**. Richtig: +10 dB = **Intensität ×10**, Schalldruck ×3,2; +20 dB = Schalldruck ×10. Mit Aufgabe 4 b) und c) ansprechen."),
                 ("»Die Luft fliegt zum Ohr« / »Die Sinuskurve ist die Bahn der Teilchen«",
                  "Die Teilchen schwingen **längs** um ihren Platz, es wandert die Verdichtung. Die Sinuskurve ist ein **Druck-Diagramm**. Animation aus Stunde 1 noch einmal zeigen."),
                 ("»Lautstärke = Dezibel«",
                  "dB ist der gemessene **Pegel**, die Lautstärke ist die **Empfindung** und frequenzabhängig. dB und phon stimmen nur bei 1000 Hz überein (Buch S. 64)."),
                 ("»Echo: s = v · t«",
                  "Beim Echo zählt der Weg **hin und zurück**: s = v · t / 2. Typischer Fehler in Aufgabe 3 c) (408 statt 204 m)."),
                 ("»Die Bogengänge melden die Lage« / »Schwindel kommt vom Blut«",
                  "**Bogengänge** = Drehbeschleunigung (träge Lymphe), **Vorhofsäckchen** = Lage und Beschleunigung geradeaus (Kalkkristalle, Schwerkraft). Wasserglas-Demo K3.2-D2.")]

# ---------------------------------------------------------------- Quiz (14 Fragen, richtige Antwort an 1. Stelle, Anzeige gemischt)
QUIZ = [
 ("Schall", "Was ist Schall in der Luft?", ["eine Druck- und Dichtewelle", "ein Strom aus Luftteilchen", "eine elektromagnetische Welle", "eine Querwelle wie beim Seil"],
  "Die Luftteilchen schwingen längs um ihren Platz; Verdichtungen und Verdünnungen wandern weiter.", "Buch S. 61"),
 ("Schall", "Warum hört man im Weltall keinen Knall?", ["Es fehlen Teilchen, die den Schall weitergeben", "Es ist dort zu kalt", "Der Schall ist dort zu schnell", "Weil das Licht den Schall überholt"],
  "Schall braucht einen Träger: Gas, Flüssigkeit oder festen Stoff.", "Buch S. 61"),
 ("Tempo", "Wo ist Schall am langsamsten?", ["in Luft", "in Wasser", "in Stahl", "in Holz"],
  "Luft etwa 340 m/s, Wasser etwa 1480 m/s, Stahl rund 5000 m/s.", "Buch S. 61"),
 ("Rechnen", "Donner 3 s nach dem Blitz. Wie weit ist das Gewitter etwa entfernt (v = 340 m/s)?", ["etwa 1 km", "etwa 3 km", "etwa 100 m", "etwa 10 km"],
  "340 m/s · 3 s = 1020 m ≈ 1 km. Faustregel: Sekunden durch 3.", "Buch S. 61"),
 ("Rechnen", "Ein Echo kommt nach 2 s zurück (v = 340 m/s). Wie weit ist die Wand?", ["340 m", "680 m", "170 m", "1360 m"],
  "Der Schall läuft 680 m hin und zurück – die Wand ist halb so weit weg.", "Buch S. 66"),
 ("Tonhöhe", "Was bestimmt die Tonhöhe?", ["die Frequenz", "die Amplitude", "die Schallgeschwindigkeit", "der Luftdruck"],
  "Mehr Schwingungen pro Sekunde = höherer Ton.", "Buch S. 63"),
 ("Hörbereich", "Wie heißt Schall über 20 000 Hz?", ["Ultraschall", "Infraschall", "Überschall", "Hyperton"],
  "Ultraschall liegt über dem menschlichen Hörbereich; Fledermäuse und Delfine nutzen ihn.", "Buch S. 63, 66"),
 ("Dezibel", "Der Pegel steigt um 10 dB. Was gilt?", ["Die Intensität wird zehnmal so groß", "Der Schalldruck wird zehnmal so groß", "Die Intensität verdoppelt sich", "Die Frequenz wird zehnmal so groß"],
  "Intensität ×10, Schalldruck nur etwa ×3,2.", "Buch S. 64"),
 ("Dezibel", "Zwei gleich laute Maschinen mit je 80 dB laufen gleichzeitig. Wie hoch ist der Pegel ungefähr?", ["etwa 83 dB", "160 dB", "80 dB", "100 dB"],
  "Doppelte Intensität ergibt rund +3 dB. Dezibel werden nicht addiert.", "Buch S. 64"),
 ("Ohr", "Was verstärken die Gehörknöchelchen?", ["den Druck auf das ovale Fenster", "die Frequenz des Tons", "den elektrischen Strom im Hörnerv", "die Lymphe im Bogengang"],
  "Großes Trommelfell, kleines ovales Fenster und Hebelwirkung: etwa 22-facher Druck.", "Buch S. 109–110"),
 ("Ohr", "Wo wird Schwingung in ein elektrisches Signal umgewandelt?", ["in den Haarzellen der Schnecke", "im Trommelfell", "in der Ohrtrompete", "in der Ohrmuschel"],
  "Die Haarzellen des Corti-Organs sind die eigentlichen Sinneszellen.", "Buch S. 110"),
 ("Gehörschutz", "Ab welchem Tages-Lärmpegel MUSS in Österreich am Arbeitsplatz Gehörschutz getragen werden?", ["ab 85 dB", "ab 60 dB", "ab 120 dB", "erst ab 140 dB"],
  "VOLV: ab 80 dB muss er bereitgestellt, ab 85 dB getragen werden.", "Buch S. 109"),
 ("Richtung", "Woran erkennt das Gehirn, dass ein Geräusch von links kommt?", ["Am linken Ohr kommt es früher und lauter an", "Das linke Ohr hört höhere Töne", "Das rechte Ohr ist dann taub", "Am Gleichgewichtsorgan"],
  "Zeit- und Pegelunterschiede zwischen beiden Ohren – höchstens etwa 0,6 ms.", "Buch S. 110"),
 ("Gleichgewicht", "Was melden die Bogengänge?", ["Drehbeschleunigung des Kopfes", "die Neigung im Stillstand", "die Lautstärke", "den Luftdruck im Mittelohr"],
  "Die träge Lymphe biegt bei beginnender oder endender Drehung die Gallertkuppel. Die Lage melden die Vorhofsäckchen.", "Buch S. 112"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
assert len(QUIZ) == 14

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 14.11.2026)
QUELLEN = [
 ("W1", "Verordnung Lärm und Vibrationen (VOLV) §§ 3, 4, 14", "Republik Österreich (Gesamttext bei jusline.at)", "https://www.jusline.at/gesetz/volv/gesamt",
  "Auslösewert 80 dB(A) bzw. 135 dB(C) Spitze → Gehörschutz bereitstellen; Expositionsgrenzwert 85 dB(A) bzw. 137 dB(C) → tragen", "Seite geöffnet, Wortlaut §§ 3, 4, 14 gelesen"),
 ("W2", "DGUV Information 212-024 »Gehörschutz in der Praxis«, Abschnitt 4.4", "Deutsche Gesetzliche Unfallversicherung (bei BGN)", "https://vorschriften.bgn-branchenwissen.de/daten/dguv/212_024/4.htm",
  "ANC wirkt am besten bei tiefen Frequenzen; nicht als Gehörschutz zugelassene Kopfhörer dürfen in Lärmbereichen nicht verwendet werden", "Seite geöffnet, Abschnitt gelesen"),
 ("W3", "Safe listening devices and systems: a WHO-ITU standard (18.09.2019)", "World Health Organization", "https://www.who.int/publications-detail/safe-listening-devices-and-systems-a-who-itu-standard",
  "Erwachsene: 80 dB bis zu 40 Stunden pro Woche; Kinder: 75 dB", "Seite geöffnet, Werte und Datum geprüft"),
 ("W4", "Prevalence and global estimates of unsafe listening practices in adolescents and young adults (BMJ Global Health 2022, Dillard et al.)",
  "Peer-reviewte Metaanalyse, Erstautorin Medical University of South Carolina, Mitautorin WHO", "https://doi.org/10.1136/bmjgh-2022-010501",
  "24 % der 12- bis 34-Jährigen hören über Kopfhörer zu laut; 0,67–1,35 Milliarden junge Menschen weltweit gefährdet (33 Studien, 19 046 Personen)", "Abstract bei DOAJ geöffnet"),
 ("W5", "Impedanzanpassung im Mittelohr", "Physikalisch-Astronomische Fakultät, Universität Jena", "https://physik.uni-jena.de/pafmedia/9314/impedanzanpassung-im-mittelohr.pdf",
  "Druck am ovalen Fenster etwa 22-mal so hoch wie am Trommelfell (Flächenverhältnis und Hebel)", "PDF geöffnet"),
 ("W6", "Binaural Hearing (Handbook for Acoustic Ecology)", "Simon Fraser University, Kanada", "https://www.sfu.ca/sonic-studio-webdav/cmns/Handbook/Binaural_Hearing.html",
  "größte Laufzeitdifferenz etwa 0,6 ms; kleinste wahrnehmbare etwa 30 µs; vorne/hinten über die Ohrmuschel", "Seite geöffnet"),
 ("W7", "Vestibular Illusions (#FlySafe)", "Federal Aviation Administration (FAA), USA", "https://medium.com/faa/vestibular-illusions-40ce147aac5f",
  "Bogengänge = Drehbeschleunigung, Otolithen = lineare Beschleunigung; lange gleichmäßige Kurve fühlt sich wie Geradeausflug an (Graveyard Spiral); Instrumenten vertrauen", "Seite geöffnet; Datum nicht angegeben"),
 ("W8", "Acute Acoustic Trauma after Exposure to Assault Rifle Noise among Conscripts in the Finnish Defence Forces (IJERPH 2023)", "Universität Helsinki", "https://doi.org/10.3390/ijerph20043366",
  "0,7–1,5 % der Wehrpflichtigen erlitten ein Knalltrauma, in 88 % ohne Gehörschutz, meist mit Platzpatrone; häufigstes Symptom Tinnitus", "Abstract per Websuche gelesen (Volltext von hier nicht erreichbar)"),
 ("W9", "Prevention works: Hearing loss decimated in the military", "save.ch (Schweizer Fachportal) mit Daten der Schweizer Militärversicherung", "https://news.save.ch/en/?p=1991",
  "Sturmgewehrschuss über 160 dB am Ohr des Schützen; Gehörschäden im Militär durch Prävention etwa zehnmal seltener", "Textauszug per Websuche gelesen"),
 ("W10", "Speed of sound – calculator", "Sengpiel Audio (Universität der Künste Berlin, Tonmeister-Tutorium)", "https://sengpielaudio.com/calculator-speedsound.htm",
  "331,3 m/s bei 0 °C, 340 m/s bei 15 °C, 343 m/s bei 20 °C", "Textauszug per Websuche gelesen"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "Trauner-Filmtipp trauner.at/nawi_v52.aspx (Buch S. 60, Fledermäuse/Ultraschall): Seite ist von hier aus gesperrt – nicht geöffnet. Er steht nur als Buch-Filmtipp in der Zusatzaufgabe; bitte einmal selbst ansehen.",
 "PhET »Sound Waves« (HTML5, Universität Colorado, Quellcode GPL-3.0): gibt es laut Suche, Seite von hier gesperrt – Lizenz, deutsche Fassung und Handybedienung NICHT geprüft. Deshalb nicht eingebaut; die eigene Druckwellen-Animation ersetzt sie.",
 "Podcasts aus dem Jahresplan (Ö1 Wissen aktuell »Schall und Lärm verstehen« 2024; Ö1 Dimensionen »Schallkanonen« 2025; Bayern 2 radioWissen »Das Ohr« 2023): Links waren nicht auffindbar bzw. nicht prüfbar – Freigabe-Liste in der Lehrerseite.",
 "Videos: YouTube ist von hier aus nicht prüfbar. Darum steht auf den Kadetten-Seiten kein Video; stattdessen eigene Animationen. Vorschläge zur Freigabe in der Lehrerseite.",
 "Seilnacht-Filmverzeichnis »Chemische Phänomene erleben«: Chemie-Sammlung; ein Akustik-Titel ist dort nicht zu erwarten – das Verzeichnis wurde in dieser Sitzung nicht geöffnet.",
]
