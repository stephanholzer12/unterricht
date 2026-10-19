"""Gemeinsame Daten für die Lehrer-Unterlagen der Stationen K1.2 (2AB, Stunde 3–4).
Versuchsdaten kommen aus der Versuchsseite (versuche.html, Feld V) – eine Quelle für Handy, Word und PPP."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
UNIT = os.path.join(ROOT, "2ab-nawi/k1-2-bindungen/")
STAND = "19.10.2026"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = {"versuche": BASE + "2ab-nawi/k1-2-bindungen/versuche.html", "vertiefung": BASE + "2ab-nawi/k1-2-bindungen/vertiefung.html",
       "training": BASE + "2ab-nawi/test1-training/quiz.html", "klasse": BASE + "2ab-nawi/", "lernseite": BASE + "2ab-nawi/k1-2-bindungen/theorie.html"}


def versuche():
    s = open(UNIT + "versuche.html", encoding="utf-8").read()
    a = s.index("const V = ") + 10; b = s.index("];\n", a) + 1
    return json.loads(s[a:b])


KERN_IDS = ["haut", "wasserstrahl", "mischen", "kristall", "sproede", "multimeter"]

# Fahrplan Stunde 1–4 (gleich in einheiten.json, PPP und Word)
FAHRPLAN = {
 "text": "Stunde 1–2: Lernseite und Arbeitsblatt (Aufgaben 1–10). Stunde 3–4: Stationen A–D und Vertiefung (Aufgaben 11–16), Demo, Besprechung, Teststoff.",
 "zeilen": [
  {"wann": "Stunde 1", "lesen": "Einstieg + Teil 1 · Warum verbinden sich Atome? + Teil 2 · Ionenbindung + Teil 3 · Atombindung", "aufgaben": "1–4 · 6", "abgabe": "–"},
  {"wann": "Stunde 2", "lesen": "Teil 4 · Metallbindung + Teil 5 · Zwischenmolekulare Kräfte + Überblick", "aufgaben": "5 · 7–10 · Quiz", "abgabe": "Arbeitsblatt-PDF in LMS"},
  {"wann": "Stunde 3", "lesen": "Versuchsseite: Gruppe 1–4 an den Stationen A–D · Gruppe 5–8 Vertiefung", "aufgaben": "Protokoll A–D · Vertiefung 11–16", "wie": "ohne Handy: Versuche an den Stationen (Handy nur zum Protokollieren)", "abgabe": "–"},
  {"wann": "Stunde 4", "lesen": "Demo K1.2-V4 (alle) · Wechsel: Gruppe 5–8 Stationen A–D · Gruppe 1–4 Vertiefung · Besprechung · Teststoff für 05.11.", "aufgaben": "Protokoll A–D + V4 · Vertiefung 11–16", "wie": "ohne Handy: Demo mit Vorhersage, Besprechung im Plenum", "abgabe": "Versuchs-PDF (Gruppe) + Vertiefungs-PDF (jeder) in LMS"},
  {"wann": "Für Schnelle", "lesen": "Vertiefung Aufgabe 17 · Test-Training-Quiz", "aufgaben": "17", "abgabe": "–"},
 ]}

# Herrichte-Liste: [Icon, Gerät/Chemikalie, Inventar/Ort, A, B, C, D, Demo, Bestand, Hinweis]
# (je 1 Satz pro Station – die Gruppen wandern; Zahlen = Stück bzw. Menge für alle 8 Gruppen)
HERRICHTEN = [
 ["wanne", "Aufbewahrungswanne (je Station eine)", "Lehrmittel Nr. 6/7", 1, 1, 1, 1, "–", "9", ""],
 ["petrischale", "Petrischale", "Glas ø 80 mm / Einmal-PS", 2, "", "", "", "", "7 + 20", "eine Ersatzschale, falls Seifenreste"],
 ["pipette", "Tropfpipette", "Glas 10 Stk. / PE 50 Stk.", 1, "", 1, "", "", "60", ""],
 ["becher", "Becherglas 100 mL", "Lehrmittel", 1, 1, "", "", 3, "6", "Demo: 3 Bechergläser (dest. Wasser, Salz-, Zuckerlösung)"],
 ["becher", "Becherglas 400 mL (blaues Wasser)", "Lehrmittel", "", "", 1, "", "", "2", "Leitungswasser + 1 Tropfen Lebensmittelfarbe"],
 ["klammer", "Büroklammer", "nicht im Inventar – Büro", 2, "", "", "", "", "–", "fehlt im Inventar: 2 aus dem Büro mitnehmen"],
 ["filterpapier", "Filterpapier 50 × 55 mm", "Lehrmittel (100 Stk.)", 10, "", "", "", "", "100", ""],
 ["muenze", "Münze (10 Cent)", "Kadetten – eigene", "", "", "", "", "", "–", "Kadetten bringen eigene Münze mit"],
 ["seife", "Vollwaschmittel in Tropfflasche", "Gefäß 39", "x", "", "x", "", "", "1350 mL", "einmal in eine Tropfflasche umfüllen"],
 ["ballon", "Luftballon (aufgeblasen)", "Lehrmittel (50 Stk.)", "", 2, "", "", "", "50", "einer als Ersatz"],
 ["tuch", "Elektrostatisches Reibetuch", "Lehrmittel Nr. 41", "", 1, "", "", "", "1", "sonst Pullover oder Haare"],
 ["hahn", "Wasserhahn", "Waschbecken im Saal", "", 1, "", "", "", "–", "Station B ans Waschbecken"],
 ["reagenzglas", "Reagenzglas 160 × 16 mm", "Lehrmittel (100 Stk.)", "", "", 32, "", "", "100", "4 pro Gruppe – nicht spülen lassen, in Sammelbecher"],
 ["gestell", "Reagenzglasgestell", "Lehrmittel", "", "", 2, "", "", "40", ""],
 ["parafilm", "Parafilm (Streifen vorschneiden)", "Lehrmittel", "", "", "32 Stk.", "", "", "1 Rolle", "Streifen am Vortag schneiden"],
 ["spatel", "Spatel", "Doppelspatel", "", "", 1, 3, "", "≥ 4", ""],
 ["farbe", "Lebensmittelfarbe blau", "F-023 (5 Fläschchen)", "", "", "x", "", "", "5", ""],
 ["glycerin", "Glycerin", "Gefäß 169 / 228", "", "", "ca. 60 mL", "", "", "2 L", "in kleines Becherglas mit Pipette"],
 ["oel", "Olivenöl", "Gefäß 132–141", "", "", "ca. 100 mL", "", "", "10 × 100 mL", "1 Flasche reicht für 8 Gruppen"],
 ["salz", "Kochsalz", "Gefäß 175 / 223 / 276", "", "", "x", "x", "x", "3 × 500 g", ""],
 ["zucker", "Zucker", "Gefäß 277 / 278", "", "", "", "x", "x", "2 × 1 kg", ""],
 ["alaun", "Kaliumalaun (grobe Kristalle)", "Gefäß 196", "", "", "", "x", "", "250 g", ""],
 ["zinn", "Zinn gekörnt", "Gefäß 234", "", "", "", "x", "", "100 g", ""],
 ["bleche", "Kupferblech-Streifen", "Gefäß 150 / Metallbleche-Satz", "", "", "", 1, 1, "1 Satz", "Demo: Kupferblech aus dem Satz"],
 ["moerser", "Mörser mit Pistill", "F-001", "", "", "", 1, "", "1", ""],
 ["unterlage", "Alu-Unterlegplatte", "Lehrmittel Nr. 173", "", "", "", 1, "", "1", ""],
 ["mikroskop", "Mikroskop (oder nur Lupe)", "Monokular LED", "", "", "", 1, "", "5", "1 reicht, Lupe genügt auch"],
 ["lupe", "Lupe", "Lupensatz", "", "", "", 2, "", "10", ""],
 ["objekttraeger", "Objektträger", "Lehrmittel (50 Stk.)", "", "", "", 6, "", "50", ""],
 ["destwasser", "dest. Wasser", "Gefäß 155–158", "", "", "", "", "ca. 150 mL", "4 × 5 L", "Demo"],
 ["multimeter", "Digitalmultimeter + Messleitungen", "Lehrmittel", "", "", "", "", 1, "1", "Batterie prüfen!"],
 ["brille", "Schutzbrille", "Facheinsatz 30 Stk.", "", "", 4, 4, "", "61", ""],
 ["dose", "Sammelbehälter »organische Reste« + Sammelbecher Reagenzgläser", "Saal", "", "", 2, "", "", "–", "Öl NICHT in den Ausguss"],
]

STOLPERSTEINE = [
 ["»Salz leitet Strom.«", "Nur gelöst oder geschmolzen – im festen Ionengitter sitzen die Ionen fest (Demo K1.2-V4)."],
 ["»Öl schwimmt, weil es unpolar ist.«", "Oben schwimmt es wegen der geringeren Dichte; dass es sich nicht mischt, liegt an polar/unpolar (Station C)."],
 ["»Im Eis ist Luft eingeschlossen.«", "Wasserstoffbrücken halten die Moleküle im Eis auf Abstand – weitmaschiges Gitter, geringere Dichte."],
 ["»Der Ballon zieht das Wasser magnetisch an.«", "Es ist elektrische Ladung: Die Wasser-Dipole drehen sich zum geladenen Ballon (Station B)."],
 ["»Mit Seife wird das Wasser schwerer – darum sinkt die Klammer.«", "Seife (Tensid) schwächt die Wasserstoffbrücken an der Oberfläche, die Oberflächenspannung sinkt (Station A)."],
]

# Besprechung in Stunde 4 (Plenum) – Frage, Antwort (in der Lehrer-PPP per Klick)
BESPRECHUNG = [
 ["A · Wasser mit Haut", "Warum passen viel weniger Tropfen Seifenwasser auf die Münze?",
  "Wasserstoffbrücken halten die Oberfläche wie eine Haut zusammen (Wasserberg). Waschmittel schwächt sie – die Oberflächenspannung sinkt, der Berg bricht früher, die Klammer sinkt."],
 ["B · Der scheue Wasserstrahl", "Warum biegt sich der Strahl zum geriebenen Ballon?",
  "Der Ballon ist elektrisch geladen. Wassermoleküle sind Dipole (δ+ / δ–) und drehen sich mit der passenden Seite zum Ballon – sie werden angezogen."],
 ["C · Wer mischt sich mit wem?", "Warum mischen sich Glycerin und Wasser, Öl und Wasser aber nicht – und warum löst sich Salz nicht im Öl?",
  "Ähnliches löst sich in Ähnlichem: Glycerin und Wasser sind polar, Öl ist unpolar. Salz-Ionen brauchen polare Wasser-Dipole. Waschmittel verbindet Öl und Wasser (Emulsion)."],
 ["D · Salz und Metall", "Warum sind alle Salzkörner Würfel und warum zerbricht Alaun, während Zinn und Kupfer sich nur verformen?",
  "Das Ionengitter ist regelmäßig – jede Ecke hat dieselbe Ordnung. Unter Druck verschieben sich die Ionenschichten, gleiche Ladungen stoßen sich ab: Bruch. Beim Metall hält das Elektronengas die Kationen weiter zusammen."],
]

DEMO = [["Kupferblech", "leitet", "Elektronengas – freie Elektronen"], ["Kochsalz, fest", "leitet nicht", "Ionen sitzen fest im Gitter"],
        ["Zucker, fest", "leitet nicht", "Moleküle, keine Ladungen"], ["destilliertes Wasser", "leitet (fast) nicht", "kaum Ionen"],
        ["Kochsalzlösung", "leitet", "frei bewegliche Ionen (Elektrolyt)"], ["Zuckerlösung", "leitet nicht", "Moleküle ohne Ladung"]]

# Erwartete Ergebnisse je Versuch (für VS-Loesung und VS-Fachwissen)
LOESUNG = {
 "haut": {"beob": ["ca. 20–40 Tropfen, hoher »Wasserberg« über dem Rand", "deutlich weniger Tropfen (oft nur die Hälfte), flacher Tropfen", "schwimmt, liegt in einer kleinen Delle der Oberfläche", "sinkt sofort"],
          "erk": "Mit Seifenwasser passen viel weniger Tropfen auf die Münze; die schwimmende Büroklammer geht nach dem Waschmitteltropfen unter.",
          "interp": "Zwischen den Wassermolekülen wirken Wasserstoffbrücken. An der Oberfläche ziehen sie die Moleküle nach innen und zur Seite – die Oberfläche wirkt wie eine gespannte Haut (Oberflächenspannung). Waschmittel (Tenside) schieben sich zwischen die Wassermoleküle und schwächen die Brücken.",
          "schluss": "Wasserläufer gehen unter und ertrinken. Waschmittel gehört nicht in Bäche oder Teiche – Abwasser im Feldlager über Sammelbehälter/Kanal entsorgen.",
          "info": ["Partnerversuch an der Station · ca. 7 min", "Station A: Petrischale, Pipette, Becherglas, Büroklammer, Filterpapier, Waschmittel in einer Wanne. Münzen bringen die Kadetten mit.", "Nach jeder Gruppe Schale mit Leitungswasser ausspülen – schon Spuren von Waschmittel verderben die Klammer. Ersatzschale bereitstellen.", "Fehler: Klammer direkt aufs Wasser gedrückt (sinkt) – darum Filterpapier. Münze nicht ganz trocken – weniger Tropfen.", "Idee: Naturwissenschaften HAK 1 (Trauner), Beobachtung »Oberflächenspannung« (Münze); Jahresplan V2.8"]},
 "wasserstrahl": {"beob": ["keine Veränderung", "der Strahl biegt sich deutlich zum Ballon hin"],
          "erk": "Der Wasserstrahl wird zum geriebenen Ballon hin gebogen, ohne ihn zu berühren.",
          "interp": "Durch Reiben wird der Ballon elektrisch geladen. Wassermoleküle sind Dipole (O δ–, H δ+). Sie drehen sich mit der entgegengesetzt geladenen Seite zum Ballon und werden angezogen.",
          "schluss": "Kaum: Öl besteht aus unpolaren Molekülen ohne Teilladungen – es gibt keine Dipole, die der Ballon anziehen könnte.",
          "info": ["Partnerversuch am Waschbecken · ca. 5 min", "Station B: 2 Luftballone (einer Ersatz), Reibetuch Nr. 41, Becherglas.", "Strahl so dünn wie möglich. An trockenen Tagen gelingt es besser.", "Fehler: Ballon wird nass – dann ist er entladen. Mit dem Reibetuch abtrocknen und neu reiben.", "Versuch im Schulbuch S. 27; Jahresplan: nicht als eigene ID geführt"]},
 "mischen": {"beob": ["eine Phase, klar und blau", "zwei Phasen – Öl oben, blaues Wasser unten", "trübe, milchige Mischung (Emulsion), trennt sich nur langsam", "Salzkörner bleiben ungelöst am Boden, Öl bleibt klar"],
          "erk": "»Mag Wasser«: Wasser, Glycerin, Kochsalz. »Mag Öl«: Olivenöl. Waschmittel bringt Öl und Wasser zusammen.",
          "interp": "Wasser und Glycerin sind polare Moleküle mit Wasserstoffbrücken – sie mischen sich. Öl ist unpolar (nur Van-der-Waals-Kräfte), es mischt sich nicht mit Wasser. Salz-Ionen werden nur von polaren Wasser-Dipolen umhüllt, nicht von Öl. Tenside haben einen polaren und einen unpolaren Teil und verbinden beide Phasen.",
          "schluss": "Tarnschminke ist unpolar (Fett, Wachs): Wasser allein löst sie nicht. Öl löst sie (Ähnliches löst sich in Ähnlichem), Seife emulgiert sie.",
          "info": ["Gruppenversuch an der Station · ca. 7 min", "Station C: 32 Reagenzgläser (4 pro Gruppe) – nicht spülen lassen, benutzte in den Sammelbecher. Parafilm-Streifen vorschneiden. Blaues Wasser im 400-mL-Becherglas.", "Kochsalz in Öl: nur eine Spatelspitze, sonst sieht man nichts Neues.", "Ölreste in den Ausguss – Sammelbehälter an die Station stellen.", "Ohne Brennspiritus und Paraffinöl (Fassung 11.10. geändert); Idee: Chemie 1 (Westermann) S. 66"]},
 "kristall": {"beob": ["kleine Würfel, alle gleich geformt, glatte Flächen", "unregelmäßige, längliche Klötzchen", "klare, regelmäßige Kristalle, oft Bruchstücke von Achtflächnern"],
          "erk": "Kochsalz-Körner sind Würfel – große und kleine haben dieselbe Form.",
          "interp": "Im Ionengitter sind Na⁺ und Cl⁻ abwechselnd in einem würfelförmigen Raster angeordnet. Jeder Kristall wächst nach demselben Muster, darum hat jedes Korn dieselbe Form.",
          "schluss": "Die äußere Form spiegelt die regelmäßige Anordnung der Teilchen im Inneren wider; ein Salzkristall bricht entlang der Gitterebenen.",
          "info": ["Gruppenversuch an Station D (mit K1.2-V3) · ca. 4 min", "Lupe reicht; Mikroskop nur mit kleinster Vergrößerung und Licht von unten.", "Kein Trocknen von Tropfen nötig (Unterschied zur Versuchsseite vom 11.10.).", "Fehler: zu viel Salz auf dem Objektträger – nur eine Spatelspitze verteilen.", "Idee: Jahresplan V2.6 (Kristalle) vereinfacht"]},
 "sproede": {"beob": ["zerspringt in viele kleine Bruchstücke mit glatten Kanten", "wird platt gedrückt, bleibt ganz", "lässt sich biegen und zurückbiegen, bricht nicht"],
          "erk": "Alaun (ein Salz) ist spröde, Zinn und Kupfer (Metalle) sind verformbar.",
          "interp": "Im Ionengitter liegen nach dem Verschieben gleiche Ladungen übereinander und stoßen sich ab – der Kristall bricht. Im Metall gleiten die Kationen-Schichten ab, das Elektronengas hält sie weiter zusammen.",
          "schluss": "Patronenhülsen und Kabel müssen verformbar sein und dürfen nicht splittern; Metalle leiten außerdem Strom und Wärme.",
          "info": ["Gruppenversuch an Station D · ca. 4 min", "Nur 1 Mörser – darum Station. Schutzbrille, Pistill drücken, nicht schlagen.", "Kupferstreifen nicht zu oft biegen (Kaltverfestigung, bricht dann doch).", "Fehler: Zinnkorn springt weg – auf die Unterlegplatte legen.", "Versuchsseite K1.2 (11.10.) unverändert"]},
 "multimeter": {"beob": ["wenige Ω · ja", "wenige Ω · ja", "wenige Ω · ja", "OL · nein", "OL · nein", "OL oder sehr hoher Wert · (fast) nein", "einige kΩ · ja", "OL · nein"],
          "erk": "Kupfer und Kochsalzlösung leiten. Festes Salz, Zucker, Zuckerlösung und destilliertes Wasser leiten nicht.",
          "interp": "Strom braucht frei bewegliche, geladene Teilchen: im Metall die Elektronen des Elektronengases, in der Salzlösung die Ionen. Im festen Salz sitzen die Ionen fest; Zucker besteht aus ungeladenen Molekülen.",
          "schluss": "Schweiß ist eine Salzlösung – nasse, verschwitzte Haut leitet deutlich besser als trockene. Darum nie mit nassen Händen an elektrische Geräte.",
          "info": ["Lehrer-Demo zu Beginn von Stunde 4 · ca. 6 min (nur 1 Multimeter)", "Vorher Vorhersage im Plenum (Hände heben oder ABCD-Karten), Kadetten haben in Vertiefung Aufgabe 12 schon getippt.", "Bereich 200 kΩ; Spitzen nach jeder Lösung mit dest. Wasser abspülen.", "Fehler: Leitungswasser statt dest. Wasser – leitet dann schon etwas.", "Jahresplan V2.5/V2.7"]},
}
