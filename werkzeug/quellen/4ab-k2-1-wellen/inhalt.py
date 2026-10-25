"""NAWI 4AB · K2.1–2.3 Schwingungen, Wellen und das elektromagnetische Spektrum (Trauner NAWI 4, S. 47–59) – v1.
Grundlage: Entwurf ChatGPT v1 vom 25.10.2026 (fachlich geprüft, Korrekturen im Prüfbericht).
Jahresplan: E6 Schwingungen (2 Std., K03, K05) + E7 Wellen (2 Std., K03) + E8 EM-Spektrum (2 Std., K04) = 6 Std.
Zwei Klassen mit eigenem Stundenplan: 4AK 5 Termine (2 davon nur 30 min wegen Test bzw. Referat), 4BK 4 Termine (+ optional 18.11.).
Deshalb sind Theorie, Aufgaben und PPP nach TEILEN 1–5 gegliedert (»h« = Teil); welche Stunde welcher Teil ist, steht im Fahrplan je Klasse.
Eine Quelle für Handy-Seiten, Word, PPP, Kahoot und Lösungsmappe.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge).
Zeichen √ und ≈ nur in Theorie und Bildern – in Aufgabentexten und Lösungen nicht (die PDF-Schrift kennt sie nicht; clean() ersetzt sie notfalls)."""

STAND = "25.10.2026"
V = "v2"  # v2: Umsetzung ChatGPT-Prüfbericht v2 (Kahoot unverändert v1)
ORDNER = "4ab-nawi/k2-1-wellen"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "4ab-nawi/"
EYEBROW = "NAWI · 4AB · K2.1–2.3 Schwingungen und Wellen"
TITEL = "Schwingungen, Wellen und das elektromagnetische Spektrum"
KURZTITEL = "Schwingungen und Wellen"
BUCH = "Buch S. 47–59"
KEY = "26-27-4AB-K2.1-Wellen-TH-Handy-v1"
PRAEFIX = "26-27-4AB-K2.1-2.3-Wellen"

# (Titel, Quelle, Dauer, Link[, Art]) – Art "sim" = Simulation (Knopf »Simulation öffnen«), "buch" = Medium aus dem Buch, Inhalt ungeprüft:
# erscheint auf der Handy-Seite und in der Kadetten-PPP erst, wenn der Schlüssel in FREIGEGEBEN steht (Stephan hat es angesehen).
VIDEOS = {
    "resonanz_buch": ("Resonanz (Buch-Medium)", "Link aus dem Buch S. 53 (Trauner)", "kurz", "https://www.trauner.at/nawi_v50.aspx", "buch"),
    "stehend_buch": ("Stehende Schallwellen (Buch-Medium)", "Link aus dem Buch S. 56 (Trauner)", "kurz", "https://www.trauner.at/nawi_v51.aspx", "buch"),
    "stehwelle_buch": ("Stehende Welle (Buch-Medium)", "Link aus dem Buch S. 56 (Trauner)", "kurz", "https://www.trauner.at/stehendeWelle.aspx", "buch"),
    "phet_pendel": ("Pendel-Labor", "PhET, University of Colorado (Deutsch, CC BY 4.0)", "Simulation", "https://phet.colorado.edu/de/simulations/pendulum-lab", "sim"),
    "phet_seil": ("Welle an einem Seil", "PhET, University of Colorado (Deutsch, CC BY 4.0)", "Simulation", "https://phet.colorado.edu/de/simulations/wave-on-a-string", "sim"),
    "phet_interferenz": ("Welleninterferenz", "PhET, University of Colorado (Deutsch, CC BY 4.0)", "Simulation", "https://phet.colorado.edu/de/simulations/wave-interference", "sim"),
}
FREIGEGEBEN = set()  # z. B. {"resonanz_buch"} – nach Stephans Freigabe eintragen und neu bauen


def zeigen(key, lehrer=False):
    """Buch-Medien nur nach Freigabe öffentlich zeigen; die Lehrer-PPP zeigt sie immer (mit Hinweis)."""
    v = VIDEOS[key]
    return lehrer or len(v) < 5 or v[4] != "buch" or key in FREIGEGEBEN


KLASSEN = ["4AK", "4BK"]
# Termine je Klasse (Stunde → Datum); 4AK: Test 09.11., Referat EKG/MRT 11.11.; 4BK: Test 11.11., 18.11. nur optional
DATEN = {"4AK": {1: "Mi 04.11.", 2: "Mo 09.11.", 3: "Mi 11.11.", 4: "Mo 16.11.", 5: "Mi 18.11."},
         "4BK": {1: "Mi 04.11.", 2: "Fr 06.11.", 3: "Mi 11.11.", 4: "Fr 13.11."}}
# Welcher Teil in welcher Stunde (für Gruppenköpfe, Versuchsseite, PPP)
TEIL_STUNDE = {1: {"4AK": 1, "4BK": 1}, 2: {"4AK": 2, "4BK": 2}, 3: {"4AK": 3, "4BK": 2}, 4: {"4AK": 4, "4BK": 4}, 5: {"4AK": 5, "4BK": 3}}


def wann(teil):
    """»4AK: Stunde 2 · Mo 09.11. · 4BK: Stunde 2 · Fr 06.11.«"""
    return " · ".join(f"{k}: Stunde {TEIL_STUNDE[teil][k]} · {DATEN[k][TEIL_STUNDE[teil][k]]}" for k in KLASSEN)


def first(lst, correct):
    return [correct] + [x for x in lst if x != correct]


ERG = ["T wird größer", "T wird kleiner", "T bleibt gleich"]

T = [
 # ======================================================= Teil 1 · Schwingungen messen (Buch S. 48–50)
 {"id": "a1", "nr": 1, "title": "Ein Diagramm lesen", "src": "Buch S. 49", "own": True, "tag": "Teil 1", "h": 1, "zeit": 5, "img": "img/a1_diagramm.png",
  "q": "Das Diagramm zeigt die Auslenkung y eines Pendels über die Zeit t (Gitter: 0,2 s und 1 cm). Lies ab bzw. berechne: a) die Amplitude A in cm, "
       "b) die Periodendauer T in s, c) die Frequenz f in Hz (auf zwei Dezimalstellen).",
  "hint": "Amplitude = größte Auslenkung aus der Nulllinie – nicht von oben bis unten. T = Abstand zweier benachbarter Hochpunkte (Maxima) auf der Zeitachse. Info: Theorie Teil 1 »Wie misst man eine Schwingung?«",
  "type": "multi",
  "fields": [["amp", "a) Amplitude A (mit Einheit)"], ["periode", "b) Periodendauer T (mit Einheit)"], ["frequenz", "c) Frequenz f (mit Einheit)"]],
  "chk": {"amp": {"num": 3, "unit": "cm"}, "periode": {"num": 0.8, "unit": "s"}, "frequenz": {"num": 1.25, "unit": "Hz"}},
  "sol": [["Lösung", ["a) A = 3 cm (nicht 6 cm – das wäre der Abstand von ganz oben bis ganz unten).",
                      "b) Hochpunkte bei 0,2 s, 1,0 s und 1,8 s → T = 1,0 s − 0,2 s = 0,8 s.",
                      "c) f = 1 : T = 1 : 0,8 s = 1,25 Hz."]]],
  "tip": ["Wie misst man eine Schwingung?", "theorie.html#groessen"]},

 {"id": "a2", "nr": 2, "title": "Unsere Pendelmessung (Versuch K2.1-V1)", "src": "Buch S. 50", "own": True, "tag": "Teil 1", "h": 1, "zeit": 6, "invs": True,
  "q": "Verwende eure eigenen Messwerte aus dem Versuch K2.1-V1 (Versuchsprotokoll) – nicht die Beispielwerte. a) Periodendauer T bei l = 0,40 m, "
       "b) Periodendauer T bei l = 0,90 m (jeweils mit Einheit), c) Wähle: Was passiert mit T, wenn das Pendel länger wird? "
       "d) Nenne eine Ursache für Messfehler und wie man sie kleiner macht (1–2 Sätze).",
  "hint": "T = (Zeit für 10 volle Schwingungen) : 10. Die Zeit für Aufgabe 2 ist im Versuch schon eingeplant.",
  "type": "multi",
  "fields": [["t40", "a) T bei 0,40 m (eure Messung)"], ["t90", "b) T bei 0,90 m (eure Messung)"], ["trend", "c) Längeres Pendel: …", ERG],
             ["fehler", "d) Messfehler und Verbesserung (1–2 Sätze)"]],
  "chk": {"t40": {"kw": [["Zahl mit Einheit s", r"\d.*(s\b|sek)"]], "man": True}, "t90": {"kw": [["Zahl mit Einheit s", r"\d.*(s\b|sek)"]], "man": True},
          "trend": {"sel": "T wird größer"},
          "fehler": {"kw": [["Ursache (Reaktionszeit, Zählen, Länge, Anstoßen …)", r"reaktion|zu (früh|spät)|stopp|zähl|halb|länge|schwerpunkt|anstoß|anschub|schub|winkel|ausschlag|luft"],
                            ["Verbesserung (mehr Schwingungen, wiederholen, Mittelwert …)", r"mehr|zehn|10|wiederhol|mittel|öfter|oefter|gleich|genau|zwei"]], "man": True}},
  "sol": [["Lösung", ["a) eure eigene Messung – Modellwert zum Vergleich: T ≈ 1,27 s (Abweichungen um einige Hundertstel sind normal).",
                      "b) eure eigene Messung – Modellwert zum Vergleich: T ≈ 1,90 s.",
                      "c) T wird größer – das längere Pendel schwingt langsamer (Verhältnis im Modell 1,90 : 1,27 = 1,5).",
                      "d) z. B. Reaktionszeit beim Starten und Stoppen → 10 volle Schwingungen messen statt einer, zwei Läufe machen und den Mittelwert nehmen. "
                      "Oder: halbe Schwingungen mitgezählt → immer beim Durchgang in dieselbe Richtung zählen."]]],
  "tip": ["Versuch K2.1-V1 und das Fadenpendel", "theorie.html#pendel"]},

 {"id": "a3", "nr": 3, "title": "Das Pendelmodell anwenden", "src": "Buch S. 50", "own": True, "tag": "Teil 1", "h": 1, "zeit": 4,
  "q": "Ein ideales Fadenpendel ist l = 0,81 m lang; g = 9,81 m/s², kleine Auslenkung. a) Berechne T (auf zwei Dezimalstellen, mit Rechenweg im Heft). "
       "b) Wähle: Was passiert mit T, wenn das Pendel viermal so lang ist? c) Wähle: Was passiert mit T, wenn ein doppelt so schwerer Pendelkörper bei gleicher Länge hängt?",
  "hint": "Formel aus Teil 1: T = 2π · Wurzel aus (l : g). Erst l : g rechnen, dann die Wurzel, dann mal 2π.",
  "type": "multi",
  "fields": [["periode", "a) T (mit Einheit)"],
             ["laenge", "b) viermal so lang", ["T wird doppelt so groß", "T wird viermal so groß", "T bleibt gleich", "T wird halb so groß"]],
             ["masse", "c) doppelte Masse", ["T bleibt gleich", "T wird doppelt so groß", "T wird halb so groß", "T wird viermal so groß"]]],
  "chk": {"periode": {"num": 1.8054600126395828, "unit": "s"}, "laenge": {"sel": "T wird doppelt so groß"}, "masse": {"sel": "T bleibt gleich"}},
  "sol": [["Lösung", ["a) l : g = 0,81 : 9,81 = 0,0826 s² → Wurzel = 0,287 s → T = 2π · 0,287 s = 1,81 s.",
                      "b) Wurzel aus 4 = 2 → T wird doppelt so groß.",
                      "c) T bleibt gleich – im Modell des Fadenpendels spielt die Masse keine Rolle (mehr Gewichtskraft, aber auch mehr Trägheit)."]]],
  "tip": ["Das Fadenpendel", "theorie.html#pendel"]},

 # ======================================================= Teil 2 · Dämpfung und Resonanz (Buch S. 51–53)
 {"id": "a4", "nr": 4, "title": "Dämpfen und anregen (Demo K2.1-V2)", "src": "Versuch im Buch S. 53", "own": True, "tag": "Teil 2", "h": 2, "zeit": 3, "invs": True,
  "q": "Beobachte die Demo K2.1-V2. a) Beschreibe in einem Satz, bei welchem Takt der Ausschlag am größten war. b) Wähle den Fachbegriff für diese besonders große Antwort. "
       "c) Erkläre in zwei Sätzen, warum ein Fahrzeug eine Feder UND einen Stoßdämpfer braucht.",
  "hint": "Schreib auf, was du wirklich gesehen hast – auch wenn die Hand nicht ganz gleichmäßig war. Info: Theorie Teil 2 »Dämpfung« und »Resonanz«",
  "type": "multi",
  "fields": [["beob", "a) Beobachtung (1 Satz)"], ["begriff", "b) Fachbegriff", ["Resonanz", "Dämpfung", "Interferenz", "Beugung"]],
             ["fahrzeug", "c) Feder und Stoßdämpfer (2 Sätze)"]],
  "chk": {"beob": {"kw": [["Takt / Rhythmus", r"takt|rhythm|tempo|frequenz|eigen|passend|gleich"]], "man": True},
          "begriff": {"sel": "Resonanz"},
          "fahrzeug": {"kw": [["Feder: speichert / federt", r"feder"], ["Dämpfer: Energie weg / Wärme", r"wärme|waerme|energie|innere|abgeb|umgewand"],
                              ["Nachschwingen hört auf", r"nachschwing|schaukel|wipp|aufhör|stopp|beruhig|schnell ruhig|kurz"]], "need": 2, "man": True}},
  "sol": [["Lösung", ["a) Erwartet: Im eigenen Rhythmus des Pendels (nahe der Eigenfrequenz) wurde der Ausschlag am größten; zu langsam oder zu schnell blieb er klein. Berichte, was du gesehen hast.",
                      "b) Resonanz.",
                      "c) Die Feder fängt Stöße auf, speichert die Energie kurz und gibt sie wieder zurück. Der Stoßdämpfer wandelt Schwingungsenergie in innere Energie (Wärme) um – "
                      "so schaukelt das Fahrzeug nicht lange nach."]]],
  "tip": ["Dämpfung und Resonanz", "theorie.html#resonanz"]},

 {"id": "a5", "nr": 5, "title": "Partnercheck: Schwingungen", "src": "Buch S. 49–53", "own": True, "tag": "Teil 2", "h": 2, "zeit": 6,
  "q": "Arbeitet zu zweit OHNE Handy mit den Partnerkarten (Folie am Beamer bzw. Theorie-Seite am Ende von Teil 2). A stellt 3 Fragen, B antwortet, "
       "A kontrolliert mit der Lösung auf der Karte. Dann Rollen tauschen. Erst danach eintragen: a) Mit wem hast du gearbeitet? (Vorname) "
       "b) Welche Frage war schwierig – und wie lautet die richtige Antwort? (1–2 Sätze) Oder schreib »alle Fragen richtig«.",
  "hint": "Ohne Handy: erst mündlich abfragen, dann eintragen. Die Lehrkraft bewertet b).",
  "type": "multi",
  "fields": [["partner", "a) Partnercheck mit (Vorname)"], ["check", "b) Schwierige Frage und richtige Antwort"]],
  "chk": {"partner": {"kw": [["Vorname", r"[a-zäöüß]{2,}"]], "man": True},
          "check": {"kw": [["Antwort oder »alle richtig«", r"richtig|antwort|amplitude|periode|frequenz|länge|laenge|masse|dämpf|daempf|resonanz|brücke|bruecke|tritt|hz|\d"]], "man": True}},
  "sol": [["Lösung", ["a) Vorname des Partners.",
                      "b) Lösungen der Karten: T = 2 s, f = 0,5 Hz · Amplitude = größte Auslenkung · T hängt von der Länge ab, nicht von der Masse · "
                      "Stoßdämpfer wandelt Schwingungsenergie in Wärme um · Resonanz = große Antwort bei passendem Takt · »ohne Tritt« verhindert Anregung im Takt der Brücke."]]],
  "tip": ["Partnerkarten", "theorie.html#partner"]},

 # ======================================================= Teil 3 · Wellen (Buch S. 54–55)
 {"id": "a6", "nr": 6, "title": "Der Puls läuft – die Büroklammer bleibt (K2.2-V1)", "src": "Buch S. 54–55", "own": True, "tag": "Teil 3", "h": 3, "zeit": 2, "invs": True,
  "q": "Beobachte den Versuch K2.2-V1. a) Beschreibe in 1–2 Sätzen, wie sich die Büroklammer auf der Schnur bewegt und wohin der Puls läuft. "
       "b) Wähle: Welche Wellenart ist die Schnurwelle (und die Kadetten-Welle mit Aufstehen)? c) Wähle: Welche Wellenart ist die Kadetten-Welle mit dem kleinen Schritt vor und zurück?",
  "hint": "Vergleiche zwei Richtungen: Wie bewegt sich ein Teilchen – und wohin läuft die Störung? Info: Theorie Teil 3 »Querwelle und Längswelle«",
  "type": "multi",
  "fields": [["punkt", "a) Büroklammer und Puls (1–2 Sätze)"],
             ["quer", "b) Schnurwelle", ["transversal (Querwelle)", "longitudinal (Längswelle)", "keine Welle"]],
             ["laengs", "c) Schritt vor und zurück", ["longitudinal (Längswelle)", "transversal (Querwelle)", "keine Welle"]]],
  "chk": {"punkt": {"kw": [["Klammer bleibt am Ort / auf und ab", r"auf und ab|rauf|hoch|\bort\b|stelle|bleibt|quer|senkrecht|zurück"], ["Puls läuft weiter / entlang", r"läuft|lauft|weiter|entlang|ende|andere|wandert"]], "man": True,
                   "contra": [r"klammer\w*\s+(bewegt sich|wandert|läuft|lauft|geht|rutscht)\s+(\w+\s+){0,2}(mit|fort|weiter|bis)"]},
          "quer": {"sel": "transversal (Querwelle)"}, "laengs": {"sel": "longitudinal (Längswelle)"}},
  "sol": [["Lösung", ["a) Die Büroklammer bewegt sich nur kurz auf und ab und bleibt an ihrer Stelle. Der Puls läuft entlang der Schnur zum anderen Ende.",
                      "b) transversal – Schwingungsrichtung (auf/ab) steht senkrecht zur Ausbreitungsrichtung (entlang).",
                      "c) longitudinal – die Kadetten schwingen vor und zurück in derselben Richtung, in der die Störung weiterläuft."]]],
  "tip": ["Querwelle und Längswelle", "theorie.html#wellenarten"]},

 {"id": "a7", "nr": 7, "title": "Wellen rechnen", "src": "Buch-Aufgabe S. 55", "own": False, "tag": "Teil 3", "h": 3, "zeit": 6,
  "q": "Zwei Rechnungen mit v = λ · f. a) Der Kammerton hat f = 440 Hz. Schall ist in diesem Beispiel v = 334 m/s schnell. Berechne die Wellenlänge λ in m (auf drei Dezimalstellen). "
       "b) Eine Meereswelle hat die Wellenlänge λ = 300 m und die Periodendauer T = 15 s. Berechne ihre Geschwindigkeit v in m/s.",
  "hint": "a) λ = v : f. b) Zuerst f = 1 : T – oder direkt v = λ : T. Rechenweg ins Heft, Ergebnis mit Einheit eintragen.",
  "type": "multi",
  "fields": [["schall", "a) λ (mit Einheit)"], ["meer", "b) v (mit Einheit)"]],
  "chk": {"schall": {"num": 0.759090909090909, "unit": "m"}, "meer": {"num": 20, "unit": "m/s"}},
  "sol": [["Lösung", ["a) λ = v : f = 334 m/s : 440 Hz = 0,759 m (rund 76 cm). Die 334 m/s gelten für dieses Beispiel – in Luft hängt die Schallgeschwindigkeit von der Temperatur ab.",
                      "b) v = λ : T = 300 m : 15 s = 20 m/s (= 72 km/h)."]]],
  "tip": ["Rechnen mit Wellen: v = λ · f", "theorie.html#rechnen"]},

 # ======================================================= Teil 4 · Überlagerung und Huygens (Buch S. 51, 56–57)
 {"id": "a8", "nr": 8, "title": "Wellen treffen aufeinander (K2.2-V2)", "src": "Buch S. 51, 56", "own": True, "tag": "Teil 4", "h": 4, "zeit": 3, "invs": True,
  "q": "Nutze die Simulation K2.2-V2 bzw. die Animation in Teil 4. a) Zwei Auslenkungen treffen sich an einem Ort: +2 cm und −1 cm. Berechne die Summe in cm. "
       "b) Wähle: Was passiert mit zwei Pulsen (+2 cm und −2 cm), nachdem sie sich getroffen haben? "
       "c) Erkläre in 1–2 Sätzen, warum an einer Stelle mit Auslenkung null nicht die ganze Energie der Wellen verschwunden ist.",
  "hint": "Mit Vorzeichen addieren! Schau dir die Animation »Überlagerung« in Teil 4 noch einmal an.",
  "type": "multi",
  "fields": [["summe", "a) Summe (mit Einheit)"],
             ["danach", "b) Nach dem Treffen …", ["laufen beide unverändert weiter", "prallen sie voneinander ab", "sind beide für immer verschwunden", "verschmelzen sie zu einem großen Puls"]],
             ["energie", "c) Warum ist die Energie nicht weg? (1–2 Sätze)"]],
  "chk": {"summe": {"kw": [["Ergebnis +1 cm (mit Vorzeichen)", r"(^|[^\d.,\-−–‒])\+?\s*(1([.,]0+)?\s*(cm)?|10\s*mm)\s*\.?\s*$"]],
                  # eigene Regel statt num: die gemeinsame Zahlenprüfung liest »−1 cm« (typografisches Minus) als +1 – siehe Prüfbericht
                  "contra": [r"[\-−–‒]\s*(1([.,]0+)?\s*(cm)?|10\s*mm)\s*\.?\s*$"]}, "danach": {"sel": "laufen beide unverändert weiter"},
          "energie": {"kw": [["nur an diesem Ort / kurz", r"ort|stelle|kurz|moment|nur|lokal|dort|punkt"], ["laufen weiter / Energie woanders", r"weiter|woanders|andere|verteilt|danach|bleibt|wieder"]], "man": True}},
  "sol": [["Lösung", ["a) y = (+2 cm) + (−1 cm) = +1 cm.",
                      "b) Sie laufen unverändert weiter – Wellen prallen nicht ab wie Bälle.",
                      "c) Die Auslenkung ist nur an dieser Stelle und in diesem Moment null. Danach laufen beide Pulse mit ihrer Energie weiter; bei einem festen Muster ist die Energie nur anders verteilt."]]],
  "tip": ["Überlagerung (Interferenz)", "theorie.html#interferenz"]},

 {"id": "a9", "nr": 9, "title": "Huygens mit der Hand gezeichnet", "src": "Buch-Aufgabe S. 57", "own": False, "tag": "Teil 4", "h": 4, "zeit": 4,
  "q": "Zeichne ins Heft: eine gerade Wellenfront mit fünf Punkten darauf. Zeichne von jedem Punkt eine gleich große Elementarwelle (Halbkreis) nach vorn "
       "und markiere farbig die neue Wellenfront. Fotografiere die Skizze und füge das Foto ein. Erkläre dann in einem Satz, wie die neue Wellenfront entsteht.",
  "hint": "Handschrift statt Tippen: zuerst zeichnen, dann Foto. Vorbild: Grafik »Prinzip von Huygens« in Teil 4.",
  "type": "sketch",
  "fields": [["front", "Wie entsteht die neue Wellenfront? (1 Satz)"]],
  "chk": {"front": {"kw": [["Elementarwellen", r"elementar|kreis|kleine wellen|halbkreis"], ["gemeinsame Hülle / berühren", r"hüll|huell|gemeinsam|berühr|beruehr|tangent|verbind|außen|aussen|vorder"]], "man": True}},
  "sol": [["Lösung", ["Skizze: fünf gleich große Halbkreise mit Mittelpunkt auf der alten Front, die neue Front berührt alle Halbkreise vorne (gerade Linie parallel zur alten). Ausbreitungsrichtung als Pfeil.",
                      "Satz: Jeder Punkt der alten Wellenfront sendet eine kleine Elementarwelle aus – die gemeinsame Hülle (Einhüllende) aller Elementarwellen ist die neue Wellenfront."]]],
  "tip": ["Das Prinzip von Huygens", "theorie.html#huygens"]},

 # ======================================================= Teil 5 · Elektromagnetisches Spektrum (Buch S. 58–59)
 {"id": "a10", "nr": 10, "title": "Das Spektrum ordnen", "src": "Buch S. 58–59", "own": True, "tag": "Teil 5", "h": 5, "zeit": 4,
  "q": "Ordnet zuerst zu zweit OHNE Handy mündlich, dann eintragen. a) Wähle die Reihenfolge mit zunehmender Frequenz. "
       "b) Welchen Bereich empfängt eine Wärmebildkamera? c) Welcher Bereich ist beim Sonnenschutz der Haut besonders wichtig?",
  "hint": "Grafik »Das elektromagnetische Spektrum« in Teil 5: Nach rechts nimmt die Frequenz zu.",
  "type": "multi",
  "fields": [["ordnung", "a) zunehmende Frequenz", ["Funk → Infrarot → sichtbares Licht → UV → Röntgen", "Röntgen → UV → sichtbares Licht → Infrarot → Funk",
                                                     "Funk → UV → sichtbares Licht → Infrarot → Röntgen", "Infrarot → Funk → UV → sichtbares Licht → Röntgen"]],
             ["kamera", "b) Wärmebildkamera", ["Infrarot", "Ultraschall", "Röntgenstrahlung", "Ultraviolett"]],
             ["sonne", "c) Sonnenschutz der Haut", ["Ultraviolett", "Radiowellen", "Infrarot", "Röntgenstrahlung"]]],
  "chk": {"ordnung": {"sel": "Funk → Infrarot → sichtbares Licht → UV → Röntgen"}, "kamera": {"sel": "Infrarot"}, "sonne": {"sel": "Ultraviolett"}},
  "sol": [["Lösung", ["a) Funk → Infrarot → sichtbares Licht → UV → Röntgen (Gamma käme noch weiter rechts).",
                      "b) Infrarot – eine Wärmebildkamera empfängt die Wärmestrahlung von Körpern. (Restlichtverstärker arbeiten anders.)",
                      "c) Ultraviolett – UV-Strahlung verursacht Sonnenbrand und kann Haut und Augen schädigen."]]],
  "tip": ["Das elektromagnetische Spektrum", "theorie.html#spektrum"]},

 {"id": "a11", "nr": 11, "title": "Funk und Wellenlänge", "src": "Buch-Aufgabe S. 59", "own": False, "tag": "Teil 5", "h": 5, "zeit": 5,
  "q": "Rechne mit c = 3,00 · 10⁸ m/s. a) Ein Truppenfunkgerät sendet im UKW-Bereich mit f = 50 MHz. Berechne die Wellenlänge λ in m. "
       "Ordne dann die Wellenlängen dem richtigen Bereich zu: b) λ = 15 cm, c) λ = 750 nm, d) λ = 3 m.",
  "hint": "1 MHz = 1 000 000 Hz. λ = c : f. Für b)–d): Tabelle »Das elektromagnetische Spektrum« (Teil 5, Spalte Wellenlänge).",
  "type": "multi",
  "fields": [["funk", "a) λ (mit Einheit)"],
             ["kurz", "b) 15 cm", ["Mikrowellen (Teil der Radiowellen)", "sichtbares Licht", "UV", "Gammastrahlung"]],
             ["rot", "c) 750 nm", ["sichtbares Licht (roter Rand)", "Radiowellen", "Röntgenstrahlung", "Mikrowellen"]],
             ["lang", "d) 3 m", ["Radiowellen (UKW)", "sichtbares Licht", "UV", "Gammastrahlung"]]],
  "chk": {"funk": {"num": 6, "unit": "m"}, "kurz": {"sel": "Mikrowellen (Teil der Radiowellen)"}, "rot": {"sel": "sichtbares Licht (roter Rand)"}, "lang": {"sel": "Radiowellen (UKW)"}},
  "sol": [["Lösung", ["a) 50 MHz = 5,0 · 10⁷ Hz; λ = 3,00 · 10⁸ m/s : 5,0 · 10⁷ Hz = 6,0 m.",
                      "b) 15 cm: Mikrowellen (z. B. Radar, Handy, WLAN) – ein Teil des Radiowellenbereichs.",
                      "c) 750 nm: gerade noch sichtbares, tiefrotes Licht (Buch: 380–780 nm; die Grenze ist nicht scharf).",
                      "d) 3 m: Radiowellen – genau der UKW-Rundfunk um 100 MHz."]]],
  "tip": ["Rechnen mit c = λ · f", "theorie.html#emwellen"]},

 {"id": "a12", "nr": 12, "title": "Eine KI-Antwort prüfen", "src": "Buch S. 52–59", "own": True, "tag": "Teil 5", "h": 5, "zeit": 6,
  "q": "Eine KI behauptet: »1. Jede Resonanz zerstört das Bauteil. 2. Bei einer Welle wandert das ganze Material mit. 3. Alle elektromagnetischen Wellen sind in jedem Stoff "
       "300 000 km/s schnell. 4. Nicht-ionisierende Strahlung kann niemals schaden.« Korrigiere jede Aussage mit einem kurzen, handgeschriebenen Satz "
       "(Heft oder Mini-Whiteboard), fotografiere die vier Sätze und füge das Foto ein. Nenne dann den Teil der Theorie, der Aussage 3 widerlegt, und das passende Stichwort.",
  "hint": "Handschrift statt Tippen. KI-Antworten klingen sicher – prüf sie mit der Theorie (Teil 2, 3 und 5).",
  "type": "sketch",
  "fields": [["beleg", "Beleg für Aussage 3: Teil … und Stichwort"]],
  "chk": {"beleg": {"kw": [["Teil 5", r"teil\s*(5|fünf|fuenf)\b|^\s*5\b"], ["Vakuum / nur im Vakuum", r"vakuum|leer|weltraum|weltall|\ball\b|materie|langsamer|stoff"]], "man": True}},
  "sol": [["Lösung", ["1. Resonanz macht die Schwingung groß, zerstört aber nicht automatisch – Dämpfung und Bauweise begrenzen sie (Teil 2).",
                      "2. Bei einer Welle schwingen die Teilchen nur an ihrem Ort; weitergegeben wird die Störung mit ihrer Energie (Teil 3).",
                      "3. 300 000 km/s gilt im Vakuum (und fast in Luft); in Glas oder Wasser sind elektromagnetische Wellen langsamer (Teil 5).",
                      "4. Auch nicht-ionisierende Strahlung kann schaden – z. B. UV (Sonnenbrand) oder ein starker Laser. Es kommt auf Art, Stärke und Dauer an (Teil 5).",
                      "Beleg: Teil 5, Stichwort »im Vakuum«."]]],
  "tip": ["Elektromagnetische Wellen", "theorie.html#emwellen"]},

 {"id": "a13", "nr": 13, "title": "Sicherheitskarte für den Einsatz im Freien", "src": "Buch S. 58–59", "own": True, "tag": "Teil 5", "h": 5, "zeit": 8,
  "q": "Kreativ und mit der Hand: Gestalte auf einer halben Heftseite eine kleine Karte für eine Übung im Freien. Pflicht: 1. Funk als elektromagnetische Welle, "
       "2. UV-Strahlung der Sonne, 3. eine passende Schutzmaßnahme gegen UV, 4. ein Satz, warum man Funk und UV nicht gleich beurteilen darf. "
       "Fotografiere die Karte, füge das Foto ein und tippe ihren Titel ab.",
  "hint": "Kleine Skizze mit Beschriftung genügt – kein Plakat. Keine fremden Bilder; KI-Hilfe angeben.",
  "type": "sketch",
  "fields": [["titel", "Titel deiner Karte"]],
  "chk": {"titel": {"kw": [["Titel", r"[a-zäöüß]{3,}"]], "man": True}},
  "sol": [["Beispiel", ["Titel z. B. »Draußen verbunden – vor UV geschützt«.",
                        "Funkgerät → Radiowellen tragen die Nachricht · Sonne → UV-Strahlung · Schutz: Schatten, Kopfbedeckung, Kleidung, Sonnenbrille, Sonnencreme · "
                        "Satz: »Funk und UV sind beide elektromagnetisch, wirken aber verschieden – UV kann Haut und Augen schädigen; entscheidend sind Strahlungsart, Stärke und Dauer.«",
                        "Bewertung (10 P.): fachlich richtig 4 · alle vier Pflichtinhalte 2 · verständlich beschriftet 2 · eigene Gestaltung 1 · Foto lesbar und rechtzeitig 1."]]],
  "tip": ["Nutzen und Schutz", "theorie.html#schutz"]},

 # ======================================================= Zusatz · Für Schnelle und Neugierige
 {"id": "a14", "nr": 14, "title": "Federpendel statt Fadenpendel", "src": "Buch S. 49–50", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Ein ideales Federpendel hat die Masse m = 0,200 kg und die Federkonstante k = 20,0 N/m. a) Berechne T (auf drei Dezimalstellen). "
       "b) Wähle: Was passiert mit T bei viermal so großer Masse und gleicher Feder?",
  "hint": "Formel aus Teil 1: T = 2π · Wurzel aus (m : k).",
  "type": "multi",
  "fields": [["feder", "a) T (mit Einheit)"], ["vier", "b) viermal so große Masse", ["T verdoppelt sich", "T vervierfacht sich", "T bleibt gleich", "T halbiert sich"]]],
  "chk": {"feder": {"num": 0.6283185307179586, "unit": "s"}, "vier": {"sel": "T verdoppelt sich"}},
  "sol": [["Lösung", ["a) m : k = 0,200 : 20,0 = 0,0100 s² → Wurzel = 0,100 s → T = 2π · 0,100 s = 0,628 s.",
                      "b) T verdoppelt sich (Wurzel aus 4 = 2). Anders als beim Fadenpendel zählt hier die Masse!"]]],
  "tip": ["Das Federpendel", "theorie.html#pendel"]},

 {"id": "a15", "nr": 15, "title": "Die Fallbeschleunigung aus Pendeldaten", "src": "Buch S. 50", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Übungsdaten (keine Messung deiner Gruppe): Ein Fadenpendel ist l = 0,640 m lang, 20 volle Schwingungen dauern 32,6 s. a) Berechne T (auf zwei Dezimalstellen). "
       "b) Stelle T = 2π · Wurzel(l : g) nach g um und berechne g (auf zwei Dezimalstellen). c) Erkläre in einem Satz, warum ein kleiner Unterschied zu 9,81 m/s² kein neues Naturgesetz beweist.",
  "hint": "g = 4π² · l : T². Erst T ausrechnen.",
  "type": "multi",
  "fields": [["periode", "a) T (mit Einheit)"], ["grav", "b) g (mit Einheit)"], ["unsicher", "c) Warum kein neues Naturgesetz? (1 Satz)"]],
  "chk": {"periode": {"num": 1.63, "unit": "s"}, "grav": {"num": 9.509649315664406, "unit": "m/s²"},
          "unsicher": {"kw": [["Messfehler / Messunsicherheit", r"mess|fehler|ungenau|reaktion|runden|ablesen"], ["Modell / Näherung", r"modell|näherung|naeherung|ideal|winkel|länge|laenge|schwerpunkt"]], "need": 1, "man": True}},
  "sol": [["Lösung", ["a) T = 32,6 s : 20 = 1,63 s.",
                      "b) g = 4π² · 0,640 m : (1,63 s)² = 25,27 m : 2,657 s² = 9,51 m/s² (etwa 3 % unter 9,81 m/s²).",
                      "c) Messfehler (z. B. 0,3 s Reaktionszeit auf 32,6 s, Länge nicht bis zum Schwerpunkt gemessen) und die Näherungen des Modells erklären so eine Abweichung – dafür braucht es kein neues Gesetz."]]],
  "tip": ["Das Fadenpendel", "theorie.html#pendel"]},

 {"id": "a16", "nr": 16, "title": "Überlagerung: 3 cm und 1 cm", "src": "Buch-Aufgabe S. 53", "own": False, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Zwei Schwingungen mit gleicher Frequenz haben die Amplituden 3 cm und 1 cm. Zeichne ins Heft beide Schwingungen und ihre Summe – einmal im Gleichtakt "
       "(Berge fallen zusammen) und einmal im Gegentakt (Berg trifft Tal). Füge ein Foto ein und gib dann die Amplitude der Summe an: a) im Gleichtakt, b) im Gegentakt.",
  "hint": "Zeichne auf Karopapier: 1 cm Auslenkung = 2 Kästchen. Summe = Auslenkungen an jeder Stelle mit Vorzeichen addieren.",
  "type": "sketch",
  "fields": [["gleich", "a) Amplitude im Gleichtakt (mit Einheit)"], ["gegen", "b) Amplitude im Gegentakt (mit Einheit)"]],
  "chk": {"gleich": {"num": 4, "unit": "cm"}, "gegen": {"num": 2, "unit": "cm"}},
  "sol": [["Lösung", ["Skizze: zwei Sinuskurven gleicher Periode, darunter die Summe.",
                      "a) Gleichtakt: 3 cm + 1 cm = 4 cm.",
                      "b) Gegentakt: 3 cm − 1 cm = 2 cm – keine vollständige Auslöschung, weil die Amplituden verschieden sind."]]],
  "tip": ["Überlagerung (Interferenz)", "theorie.html#interferenz"]},

 {"id": "a17", "nr": 17, "title": "Forschung 2026: Täuscht ein Wellensignal?", "src": "Forschungskarte (AEI 2026)", "own": True, "tag": "Zusatz", "h": 0, "zeit": 7,
  "q": "Lies die Forschungskarte »Schwarze Löcher – schwerer als erlaubt?« im Abschnitt »Für Schnelle und Neugierige«. a) Trenne in je einem Satz: Was wurde gemessen – und was ist eine Erklärung (Modell)? "
       "b) Erkläre in einem Satz, warum die Schlagzeile »Gravitationslinse bewiesen!« zu weit geht. c) Wähle: Zu welcher Wellenart gehört das Signal?",
  "hint": "Info nur auf der Forschungskarte (Theorie-Seite, Für Schnelle). Messung = was die Detektoren aufgezeichnet haben. Erklärung = was die Forscher daraus schließen.",
  "type": "multi",
  "fields": [["trennung", "a) Gemessen … / Erklärung … (2 Sätze)"], ["sicherheit", "b) Warum zu weit? (1 Satz)"],
             ["welle", "c) Wellenart", ["Gravitationswelle – keine elektromagnetische Welle", "Radiowelle", "Schallwelle", "UV-Strahlung"]]],
  "chk": {"trennung": {"kw": [["gemessen: Signal", r"signal|gemessen|detektor|ligo|aufgezeichnet|registriert"], ["Erklärung: Modell / Linse", r"modell|erklär|erklaer|linse|vermut|annahme|könnte|koennte"]], "man": True},
          "sicherheit": {"kw": [["nicht eindeutig / Vermutung", r"nicht eindeutig|nicht bewiesen|nicht sicher|vermut|hypothese|möglich|moeglich|könnte|koennte|unklar|noch nicht"]], "man": True},
          "welle": {"sel": "Gravitationswelle – keine elektromagnetische Welle"}},
  "sol": [["Lösung", ["a) Gemessen: Die beiden LIGO-Detektoren haben am 23.11.2023 ein Gravitationswellensignal (GW231123) aufgezeichnet. "
                      "Erklärung: Forscher prüfen mit Modellen, ob eine Gravitationslinse das Signal verstärkt und verändert hat.",
                      "b) Die Daten erlauben laut Institut noch keinen eindeutigen Nachweis – es ist eine mögliche Erklärung, keine bewiesene.",
                      "c) Gravitationswelle – sie gehört nicht zum elektromagnetischen Spektrum."]]],
  "tip": ["Forschungskarte", "theorie.html#forschung"]},
]
assert [t["nr"] for t in T] == list(range(1, 18))
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x, (_t["id"], "√ im Aufgabentext – PDF-Schrift kennt das Zeichen nicht")
PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
BESPRECHEN = [1, 3, 4, 7, 8, 11, 12]  # in der Stunde gemeinsam besprechen (Lösungsmappe, Lehrer-PPP); die anderen kontrolliert die PDF
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True

GRP = {1: "Teil 1 · Schwingungen messen (Buch S. 48–50) · " + "4AK und 4BK: Stunde 1 · Mi 04.11.",
       2: "Teil 2 · Dämpfung und Resonanz (Buch S. 51–53) · " + wann(2),
       3: "Teil 3 · Wellen (Buch S. 54–55) · " + wann(3),
       4: "Teil 4 · Überlagerung und Huygens (Buch S. 51, 56–57) · " + wann(4),
       5: "Teil 5 · Elektromagnetisches Spektrum (Buch S. 58–59) · 4AK: Stunde 5 · Mi 18.11. · 4BK: Aufgaben 10–11 in Stunde 3 (Mi 11.11.), 12–13 in Stunde 4 (Fr 13.11.)",
       0: "Zusatz · Für Schnelle und Neugierige · 4AK: 16 und 17 in Stunde 4 (Mo 16.11.) · 4BK: am Mi 18.11., falls die Stunde stattfindet"}

LERNZIELE = ["eine **Schwingung** erkennen und **Amplitude, Periodendauer und Frequenz** aus Messungen und Diagrammen bestimmen (f = 1/T)",
             "untersuchen, wie die **Länge eines Fadenpendels** die Periodendauer verändert, und **Dämpfung** und **Resonanz** an Beispielen erklären",
             "**Schwingung und Welle** unterscheiden, **Quer- und Längswellen** erkennen, **Überlagerung** beschreiben und mit **v = λ · f** rechnen",
             "Beispiele dem **elektromagnetischen Spektrum** zuordnen und **Nutzen und Schutzmaßnahmen** begründen"]

WICHTIGSTE = ["Eine **Schwingung** wiederholt sich um eine Gleichgewichtslage; **Amplitude A**, **Periodendauer T** und **Frequenz f = 1/T** beschreiben sie.",
              "Beim **Fadenpendel** bestimmt bei kleinen Auslenkungen vor allem die **Länge** die Periodendauer – die Masse spielt im Modell keine Rolle.",
              "**Dämpfung** gibt Schwingungsenergie an die Umgebung ab; eine Anregung im passenden Takt kann **Resonanz** auslösen – Dämpfung begrenzt sie.",
              "Eine **Welle** gibt eine Störung weiter, die Teilchen schwingen nur an ihrem Ort; es gilt **v = λ · f**, und treffen Wellen aufeinander, **addieren sich die Auslenkungen**.",
              "Funk, Infrarot, Licht, UV, Röntgen und Gamma sind **elektromagnetische Wellen** – sie brauchen kein Medium; ihr Risiko hängt von **Art, Stärke und Dauer** ab."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Schwingung", "wiederholte Hin-und-her-Bewegung (bzw. Änderung einer Größe) um eine Gleichgewichtslage"],
                ["Auslenkung y", "momentaner Abstand von der Gleichgewichtslage, mit Vorzeichen (+ oder −)"],
                ["Amplitude A", "größte Auslenkung; von Umkehrpunkt zu Umkehrpunkt sind es 2 · A"],
                ["Periodendauer T", "Zeit für eine volle Schwingung (gleicher Ort UND gleiche Bewegungsrichtung)"],
                ["Frequenz f", "Zahl der vollen Schwingungen pro Sekunde; Einheit Hertz (Hz); f = 1/T"],
                ["harmonische Schwingung", "Schwingung mit sinusförmigem Verlauf (Rückstellkraft proportional zur Auslenkung)"],
                ["Fadenpendel", "Körper an einem Faden; T hängt im Modell nur von Länge l und g ab"],
                ["Federpendel", "Körper an einer Feder; T hängt von Masse m und Federkonstante k ab"],
                ["Dämpfung", "Abnahme der Amplitude, weil Schwingungsenergie an die Umgebung abgegeben wird (z. B. als Wärme)"],
                ["Eigenfrequenz", "Frequenz, mit der ein System von selbst (frei) schwingt"],
                ["erzwungene Schwingung", "Schwingung, die von außen regelmäßig angetrieben wird (Erregerfrequenz)"],
                ["Resonanz", "besonders große Schwingung, wenn die Erregerfrequenz nahe der Eigenfrequenz liegt"],
                ["Welle", "Ausbreitung einer Störung (Schwingung) im Raum; transportiert Energie, aber nicht das Material"],
                ["Wellenlänge λ", "Abstand zweier benachbarter Wellenberge (Punkte gleicher Phase)"],
                ["Transversalwelle", "Querwelle: Schwingungsrichtung senkrecht zur Ausbreitungsrichtung (Seil)"],
                ["Longitudinalwelle", "Längswelle: Schwingungsrichtung parallel zur Ausbreitungsrichtung (Schall in Luft)"],
                ["Interferenz", "Überlagerung von Wellen: Auslenkungen werden mit Vorzeichen addiert"],
                ["stehende Welle", "festes Muster aus Knoten (Ruhe) und Bäuchen (große Schwingung); Knotenabstand λ/2"],
                ["Prinzip von Huygens", "jeder Punkt einer Wellenfront sendet Elementarwellen aus; ihre Einhüllende ist die neue Front"],
                ["Beugung", "Wellen laufen hinter Hindernisse und Öffnungen in den »Schatten«"],
                ["elektromagnetisches Spektrum", "alle elektromagnetischen Wellen, geordnet nach Frequenz bzw. Wellenlänge"],
                ["ionisierende Strahlung", "kann Elektronen aus Atomen lösen (Röntgen, Gamma) – kann das Erbgut schädigen"]]

# »Weißt du noch?« am Beginn von Teil 2–5 – nur Inhalte, die BEIDE Klassen schon hatten (4BK macht Teil 5 vor Teil 4)
WEISST_DU_NOCH = {
    2: [("10 volle Schwingungen dauern 20 s. Wie groß ist T?", "T = 20 s : 10 = 2 s."),
        ("Was ist der Unterschied zwischen Auslenkung und Amplitude?", "Auslenkung = der Abstand gerade jetzt; Amplitude = der größte Abstand."),
        ("Was blieb im Pendelversuch gleich, als wir die Länge geändert haben?", "Pendelkörper, kleine Auslenkung, Zählweise – nur l wurde verändert.")],
    3: [("Wohin geht die Energie beim gedämpften Pendel?", "an die Umgebung, vor allem als Wärme (innere Energie)."),
        ("Führt Resonanz immer zum Einsturz?", "Nein – Dämpfung und Bauweise begrenzen die Schwingung.")],
    4: [("Läuft die Büroklammer mit dem Puls zum anderen Ende?", "Nein – sie bewegt sich nur auf und ab, die Störung läuft weiter."),
        ("Die Frequenz verdoppelt sich, v bleibt gleich. Was passiert mit λ?", "λ wird halb so groß.")],
    5: [("Braucht Schall ein Medium?", "Ja – Luft, Wasser oder Festkörper. Im Vakuum gibt es keinen Schall."),
        ("λ = 2 m, f = 5 Hz – wie schnell ist die Welle?", "v = λ · f = 10 m/s.")],
}

STOPPFRAGEN = {
    1: [("Ein Pendel schwingt vom linken zum rechten Umkehrpunkt. Ist das eine volle Schwingung?", "Nein – erst eine halbe. Voll ist sie erst, wenn es wieder links ist."),
        ("T steigt von 1 s auf 2 s. Was passiert mit f?", "f sinkt von 1 Hz auf 0,5 Hz.")],
    2: [("Ein Stoßdämpfer wird warm. Ist Energie verloren gegangen?", "Nein – Schwingungsenergie wurde in Wärme (innere Energie) umgewandelt."),
        ("Warum marschiert man über Brücken »ohne Tritt«?", "Damit der gleichmäßige Schritt die Brücke nicht im Takt ihrer Eigenfrequenz anregt.")],
    3: [("Auf der waagrechten Achse steht »t in s«. Kann man dort λ ablesen?", "Nein – dort liest man T ab. λ braucht eine Ortsachse (x in m)."),
        ("Hört man im luftleeren Weltraum eine Explosion?", "Nein – Schall braucht ein Medium (Luft, Wasser …).")],
    4: [("+3 cm und −2 cm treffen sich. Wie groß ist die Auslenkung dort?", "+1 cm."),
        ("Wie weit liegen zwei benachbarte Knoten einer stehenden Welle auseinander?", "eine halbe Wellenlänge (λ/2).")],
    5: [("Die Frequenz einer elektromagnetischen Welle steigt. Was passiert mit λ?", "λ wird kleiner (c = λ · f bleibt gleich)."),
        ("Ist »nicht ionisierend« dasselbe wie »harmlos«?", "Nein – UV oder ein starker Laser können trotzdem schaden.")],
}

PARTNERKARTEN = [("10 volle Schwingungen dauern 20 s. Wie groß sind T und f?", "T = 2 s, f = 0,5 Hz"),
                 ("Was ist die Amplitude?", "die größte Auslenkung aus der Gleichgewichtslage – nicht der Abstand von Umkehrpunkt zu Umkehrpunkt"),
                 ("Wovon hängt T beim Fadenpendel ab – und wovon nicht?", "von der Länge (und von g) – nicht von der Masse und bei kleinen Winkeln kaum vom Ausschlag"),
                 ("Was macht ein Stoßdämpfer mit der Schwingungsenergie?", "Er wandelt sie in Wärme (innere Energie) um – das Fahrzeug schaukelt nicht nach."),
                 ("Was ist Resonanz?", "eine besonders große Schwingung, wenn die Anregung im Takt der Eigenfrequenz kommt"),
                 ("Warum marschieren Soldaten über Brücken »ohne Tritt«?", "damit der gleichmäßige Schritt die Brücke nicht im Takt ihrer Eigenfrequenz anregt")]

STOLPERSTEINE = [("Halbe Schwingung gezählt", "Eine volle Schwingung endet erst am **gleichen Ort mit gleicher Bewegungsrichtung** – von links nach rechts ist nur eine halbe. Beim Messen immer den Durchgang in dieselbe Richtung zählen (TH-Fachwissen S. 48–50)."),
                 ("Amplitude = Ausschlag von oben bis unten", "Die Amplitude ist die **größte Auslenkung aus der Mitte**; von Umkehrpunkt zu Umkehrpunkt sind es 2 · A (Aufgabe 1: 3 cm, nicht 6 cm)."),
                 ("»Schwerer schwingt schneller«", "Beim Fadenpendel spielt die Masse im Modell **keine Rolle** – beim Federpendel schon. Die beiden Pendel nicht verwechseln."),
                 ("Zeitdiagramm und Ortsbild verwechselt", "Zuerst die **waagrechte Achse** lesen: »t in s« → T ablesen; »x in m« → λ ablesen."),
                 ("»Resonanz zerstört immer« / »Strahlung ist immer radioaktiv«", "Resonanz wird durch **Dämpfung** begrenzt; Tacoma Narrows war vor allem Flattern im Wind. Elektromagnetische Strahlung ist **nicht** radioaktiv – ihr Risiko hängt von Art, Stärke und Dauer ab.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Größen", "Was bedeutet die Amplitude einer Schwingung?", ["die größte Auslenkung", "die Zeit für eine Schwingung", "die Zahl der Schwingungen pro Sekunde", "der Abstand der beiden Umkehrpunkte"],
  "Die Amplitude ist die größte Auslenkung aus der Mitte. Von Umkehrpunkt zu Umkehrpunkt sind es 2 · A.", "Buch S. 49"),
 ("Größen", "20 volle Schwingungen dauern 40 s. Wie groß ist die Periodendauer T?", ["2 s", "0,5 s", "20 s", "40 s"],
  "T = Gesamtzeit : Anzahl = 40 s : 20 = 2 s.", "Buch S. 49"),
 ("Größen", "Ein Pendel hat T = 2 s. Welche Frequenz hat es?", ["0,5 Hz", "2 Hz", "4 Hz", "20 Hz"],
  "f = 1 : T = 1 : 2 s = 0,5 Hz.", "Buch S. 49"),
 ("Pendel", "Ein ideales Fadenpendel wird viermal so lang. Was passiert mit T?", ["T verdoppelt sich", "T vervierfacht sich", "T bleibt gleich", "T halbiert sich"],
  "T wächst mit der Wurzel der Länge: Wurzel aus 4 = 2.", "Buch S. 50"),
 ("Pendel", "Ein Fadenpendel bekommt einen doppelt so schweren Körper. Was passiert mit T?", ["T bleibt gleich", "T verdoppelt sich", "T halbiert sich", "T wird viermal so groß"],
  "Im Modell des Fadenpendels kommt die Masse nicht vor: mehr Gewichtskraft, aber auch mehr Trägheit.", "Buch S. 50"),
 ("Dämpfung", "Wohin geht bei einer gedämpften Schwingung die Energie?", ["an die Umgebung, oft als Wärme", "Sie verschwindet einfach.", "Sie wird zu Masse.", "Sie verdoppelt die Frequenz."],
  "Dämpfung wandelt Schwingungsenergie z. B. durch Reibung in innere Energie um – verloren geht nichts.", "Buch S. 52"),
 ("Resonanz", "Wann wird eine erzwungene Schwingung besonders groß?", ["bei Anregung im Takt der Eigenfrequenz", "bei jeder beliebigen Anregung", "nur ohne jede Anregung", "nur bei sehr großer Masse"],
  "Resonanz: Die Erregerfrequenz liegt nahe der Eigenfrequenz. Dämpfung begrenzt die Amplitude.", "Buch S. 53"),
 ("Wellen", "Was zeigt die Büroklammer auf der Schnur?", ["Sie schwingt am Ort, die Störung läuft weiter.", "Sie läuft mit dem Puls zum Ende.", "Sie bleibt völlig still.", "Sie läuft zur Hand zurück."],
  "Die Teilchen des Mediums schwingen nur an ihrem Ort; weitergegeben wird die Störung.", "Buch S. 54–55"),
 ("Wellen", "Was bedeutet »transversal«?", ["Schwingung senkrecht zur Ausbreitung", "Schwingung parallel zur Ausbreitung", "Ausbreitung ohne Medium", "ein anderes Wort für Schall"],
  "Transversal = Querwelle (Seil). Schall in Luft ist longitudinal.", "Buch S. 55"),
 ("Wellen", "Eine Welle hat λ = 0,5 m und f = 4 Hz. Wie schnell ist sie?", ["2 m/s", "8 m/s", "0,125 m/s", "4,5 m/s"],
  "v = λ · f = 0,5 m · 4 Hz = 2 m/s.", "Buch S. 55"),
 ("Interferenz", "Zwei Auslenkungen treffen sich: +3 cm und −2 cm. Summe?", ["+1 cm", "+5 cm", "−5 cm", "0 cm"],
  "Auslenkungen werden mit Vorzeichen addiert: 3 − 2 = 1.", "Buch S. 56"),
 ("Huygens", "Wie entsteht nach Huygens die neue Wellenfront?", ["als Einhüllende aller Elementarwellen", "durch ein mitreisendes Teilchen", "durch Addition nur positiver Werte", "durch Anhalten der Welle"],
  "Jeder Punkt der Front sendet Elementarwellen aus – ihre gemeinsame Hülle ist die neue Front.", "Buch S. 57"),
 ("Spektrum", "Was brauchen elektromagnetische Wellen, um sich auszubreiten?", ["kein Medium – auch im Vakuum", "immer Luft", "immer Wasser", "immer einen Draht"],
  "Licht der Sonne erreicht uns durch das Vakuum des Weltraums.", "Buch S. 58–59"),
 ("Spektrum", "Welche Strahlung empfängt eine Wärmebildkamera?", ["Infrarot", "Ultraschall", "Röntgenstrahlung", "Ultraviolett"],
  "Wärmebildkameras zeigen die Infrarot-Strahlung warmer Körper – auch in völliger Dunkelheit.", "Buch S. 58–59"),
 ("Spektrum", "Welche Wellenlänge hat UKW-Funk mit 100 MHz (c = 3 · 10⁸ m/s)?", ["3 m", "300 m", "0,03 m", "100 m"],
  "λ = c : f = 3 · 10⁸ m/s : 10⁸ Hz = 3 m.", "Buch S. 59"),
 ("Spektrum", "Die Frequenz steigt, c bleibt gleich. Was passiert mit der Wellenlänge?", ["Sie wird kürzer.", "Sie wird länger.", "Sie bleibt gleich.", "Sie wird null."],
  "c = λ · f: Wird f größer, muss λ kleiner werden.", "Buch S. 59"),
 ("Schutz", "Welche Aussage zum Risiko von Strahlung stimmt?", ["Art, Stärke und Dauer gemeinsam beurteilen", "Nicht-ionisierend ist immer harmlos.", "Nur sichtbares Licht kann schaden.", "Jede Strahlung ist radioaktiv."],
  "UV ist nicht ionisierend und verursacht trotzdem Sonnenbrand – es kommt auf Art, Stärke und Dauer an.", "Buch S. 59"),
 ("Schutz", "Welche Strahlung ist ionisierend?", ["Röntgenstrahlung", "Radiowellen", "rotes Licht", "Wärmestrahlung"],
  "Röntgen- und Gammastrahlung können Elektronen aus Atomen lösen und das Erbgut schädigen.", "Buch S. 59"),
]
