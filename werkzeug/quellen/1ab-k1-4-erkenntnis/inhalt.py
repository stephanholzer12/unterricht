"""NAWI 1AB · K1.4 Erkenntnisgewinn in den Naturwissenschaften (Trauner NAWI HAK 1, S. 28–32) – v1.
Grundlage: ChatGPT-Übergabe v4 vom 28.10.2026 (Planung, Quellenauswahl, Korrekturen) – von Claude umgesetzt und fachlich nachgeprüft (Prüfbericht).
Jahresplan v64, Zeile 7: E3, 3 Std. Kern, K01, N06, GLV 2. Stephan: 4 Kalenderstunden je Klasse, am 06.11. 20 min Test → 180 min E3.
Zwei Klassen mit eigenem Stundenplan: 1AK 05.11. (Doppelstunde), 06.11., 12.11. (1. Std.; 2. Std. Kraftbegriff); 1BK 04., 06., 09., 11.11.
Deshalb ist alles nach TEILEN 1–4 gegliedert (»h« = Teil); welche Stunde welcher Teil ist, steht im Fahrplan je Klasse (plan.py).
Eine Quelle für Handy-Seiten, Word, PPPs und Lösungsmappe. Kein Kahoot (Stephan, 29.10.2026).
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge, z. B. Zuordnen)."""

STAND = "30.10.2026"
V = "v2"
ORDNER = "1ab-nawi/k1-4-erkenntnis"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "1ab-nawi/"
EYEBROW = "NAWI · 1AB · K1.4 Erkenntnisgewinn"
TITEL = "Erkenntnisgewinn – vermuten, prüfen, vorsichtig schließen"
KURZTITEL = "Erkenntnisgewinn"
BUCH = "Buch S. 28–32"
KEY = "26-27-1AB-K1.4-Erkenntnis-TH-Handy-v1"
PRAEFIX = "26-27-1AB-K1.4-Erkenntnis"
VS_ID = "K1.4-V1"
VS_TITEL = "Papierflieger mit und ohne Büroklammer"

# (Titel, Quelle, Dauer, Link[, Art]). »stephan« = aus Stephans bisheriger PPP (Altfolie 6/7), Inhalt und Länge von hier nicht prüfbar (YouTube gesperrt).
VIDEOS = {
    "apolin1": ("Hypothese und Theorie – Teil 1", "Martin Apolin (YouTube), aus der bisherigen Unterrichts-PPP · freiwillig, Länge vorher prüfen", "kurz", "https://www.youtube.com/watch?v=PDwV0oIuK0w", "stephan"),
    "apolin2": ("Hypothese und Theorie – Teil 2 (Popper)", "Martin Apolin (YouTube), aus der bisherigen Unterrichts-PPP · freiwillig, Länge vorher prüfen", "kurz", "https://www.youtube.com/watch?v=_g7BQWR7XUs", "stephan"),
}
FREIGEGEBEN = {"apolin1", "apolin2"}  # Stephan verwendet beide Videos laut eigener Angabe regelmäßig in dieser Einheit


def zeigen(key, lehrer=False):
    return True


KLASSEN = ["1AK", "1BK"]
DATEN = {"1AK": {1: "Do 05.11. (1. Std.)", 2: "Do 05.11. (2. Std.)", 3: "Fr 06.11.", 4: "Do 12.11. (1. Std.)"},
         "1BK": {1: "Mi 04.11.", 2: "Fr 06.11.", 3: "Mo 09.11.", 4: "Mi 11.11."}}
# Welcher Teil in welcher Stunde
TEIL_STUNDE = {1: {"1AK": 1, "1BK": 1}, 2: {"1AK": 2, "1BK": 3}, 3: {"1AK": 3, "1BK": 2}, 4: {"1AK": 4, "1BK": 4}}
TEILNAME = {1: "Teil 1 · Vermuten und prüfen", 2: "Teil 2 · Der Papierflieger-Test", 3: "Teil 3 · Wie Forschung wirklich läuft", 4: "Teil 4 · Auswerten und vorsichtig schließen"}
TEILBUCH = {1: "Buch S. 28–29", 2: "Buch S. 29", 3: "Buch S. 29", 4: "Buch S. 29–32"}


def wann(teil):
    """»1AK: Stunde 2 · Do 05.11. (2. Std.) · 1BK: Stunde 3 · Mo 09.11.«"""
    return " · ".join(f"{k}: Stunde {TEIL_STUNDE[teil][k]} · {DATEN[k][TEIL_STUNDE[teil][k]]}" for k in KLASSEN)


ZUORDNUNG = ["Beobachtung", "Hypothese (Vermutung)", "Vorhersage"]
STIMMT = ["stimmt", "stimmt nicht"]
FACH = ["Biologie", "Chemie", "Physik", "keine NAWI-Frage"]
WURF = ["gültig – zählt", "ungültig – wiederholen", "zählt, Kontakt notieren"]
ZYKLUS = ["Problem analysieren", "Entwerfen", "Konstruieren", "Testen", "Bewerten", "Verbessern"]
PRUEFBAR = ["prüfbar", "nicht prüfbar"]
ZIEL = ["zufällige Streuung", "systematischer Fehler", "genau und wenig Streuung"]

T = [
 # ======================================================= Teil 1 · Vermuten und prüfen (Buch S. 28–29)
 {"id": "a1", "nr": 1, "title": "Beobachtung, Vermutung oder Vorhersage?", "src": "Buch S. 29", "own": True, "tag": "Teil 1", "h": 1, "zeit": 3,
  "q": "Ordne jede Aussage zum Papierflieger-Test zu: Ist sie eine Beobachtung, eine Hypothese (begründete Vermutung) oder eine Vorhersage für den nächsten Test?",
  "hint": "Beobachtung = was gemessen oder gesehen wurde. Hypothese = vermuteter Zusammenhang mit Begründung. Vorhersage = was wir beim nächsten Test erwarten. Info: Theorieteil Teil 1 »Vermutung, Vorhersage, Beobachtung«",
  "type": "multi",
  "fields": [["s1", "a) »Beim ersten Wurf landete der Flieger 6,4 m hinter der Linie.«", ZUORDNUNG, False],
             ["s2", "b) »Mit Büroklammer fliegt er im Mittel weiter, weil die schwerere Nase ihn ruhiger gleiten lässt.«", ZUORDNUNG, False],
             ["s3", "c) »Bei unseren drei Vergleichspaaren erwarten wir mit Klammer den größeren Mittelwert.«", ZUORDNUNG, False],
             ["s4", "d) »Bei Wurf 2 hat der Flieger die Decke gestreift.«", ZUORDNUNG, False],
             ["s5", "e) »Vielleicht flog er weiter, weil Kadett Huber fester geworfen hat.«", ZUORDNUNG, False]],
  "chk": {"s1": {"sel": "Beobachtung"}, "s2": {"sel": "Hypothese (Vermutung)"}, "s3": {"sel": "Vorhersage"}, "s4": {"sel": "Beobachtung"}, "s5": {"sel": "Hypothese (Vermutung)"}},
  "sol": [["Lösung", ["a) Beobachtung – ein gemessener Wert, noch keine Erklärung.",
                      "b) Hypothese – ein vermuteter Zusammenhang mit Begründung (»weil …«). Man kann ihn prüfen.",
                      "c) Vorhersage – das erwartete Ergebnis eines bestimmten Tests, abgeleitet aus der Hypothese.",
                      "d) Beobachtung – sie wird im Protokoll notiert und nicht gelöscht.",
                      "e) Hypothese (Vermutung) über eine Ursache – prüfbar, z. B. mit einem zweiten Werfer."]]],
  "tip": ["Vermutung, Vorhersage, Beobachtung", "theorie.html#hypothese"]},

 {"id": "a2", "nr": 2, "title": "Stimmt das?", "src": "Buch-Aufgabe Kap. 4", "own": False, "tag": "Teil 1", "h": 1, "zeit": 2,
  "q": "Nach der Buch-Aufgabe »Erkenntnisgewinn in den Naturwissenschaften« (Aufgabenkasten im Kapitel 4): Entscheide bei jeder Aussage, ob sie stimmt. Begründungen besprechen wir danach gemeinsam.",
  "hint": "Denk an Sinnestäuschungen, an Beobachtungen ohne Experiment und daran, was eine wissenschaftliche Theorie ist. Info: Theorieteil Teil 1",
  "type": "multi",
  "fields": [["b1", "a) Auf unsere Sinne können wir uns immer verlassen.", STIMMT, False],
             ["b2", "b) Neues Wissen gewinnt man nur durch Experimente.", STIMMT, False],
             ["b3", "c) Die Biologie kommt ohne Chemie und Physik aus.", STIMMT, False],
             ["b4", "d) Eine wissenschaftliche Theorie ist bloß eine geratene Vermutung.", STIMMT, False],
             ["b5", "e) Mit physikalischen Gesetzen beschreiben wir, wie Vorgänge in der Natur unter bestimmten Bedingungen ablaufen.", STIMMT, False]],
  "chk": {"b1": {"sel": "stimmt nicht"}, "b2": {"sel": "stimmt nicht"}, "b3": {"sel": "stimmt nicht"}, "b4": {"sel": "stimmt nicht"}, "b5": {"sel": "stimmt"}},
  "sol": [["Lösung", ["a) stimmt nicht – Sinne lassen sich täuschen (optische Täuschungen, Gefühl für Wärme). Darum messen wir mit Geräten und wiederholen.",
                      "b) stimmt nicht – auch genaues Beobachten (z. B. mit einer Wildtierkamera), Auswerten von Daten und Modelle bringen Erkenntnisse.",
                      "c) stimmt nicht – Atmung, Verdauung oder Nervenleitung lassen sich nur mit Chemie und Physik verstehen.",
                      "d) stimmt nicht – eine wissenschaftliche Theorie verbindet viele geprüfte Befunde und macht überprüfbare Vorhersagen.",
                      "e) stimmt – ein Gesetz beschreibt eine Regelmäßigkeit, oft als Formel, und gilt unter bestimmten Bedingungen."]]],
  "tip": ["Theorie, Gesetz und Modell", "theorie.html#theorie"]},

 {"id": "a3", "nr": 3, "title": "Welches Fach – oder gar keines?", "src": "Buch S. 28–29", "own": True, "tag": "Teil 1", "h": 1, "zeit": 3,
  "q": "Ordne jede Frage dem passenden Fach zu. Eine Frage ist gar keine naturwissenschaftliche Frage.",
  "hint": "Lebewesen → Biologie, Stoffe und ihre Umwandlung → Chemie, Bewegung, Kräfte, Licht, Schall, Strom → Physik. Fragen nach »sollen wir …?« beantwortet keine Messung. Info: Theorieteil Teil 1 »Welche Fragen kann NAWI beantworten?«",
  "type": "multi",
  "fields": [["f1", "a) Verändert eine Büroklammer an der Nase die Flugweite eines Papierfliegers?", FACH, False],
             ["f2", "b) Keimen Kressesamen bei Licht schneller als im Dunkeln?", FACH, False],
             ["f3", "c) Rostet ein Eisennagel in Salzwasser schneller als in Leitungswasser?", FACH, False],
             ["f4", "d) Soll das Bundesheer mehr Geld für neue Hubschrauber ausgeben?", FACH, False],
             ["f5", "e) Wie verändert regelmäßiges Lauftraining den Ruhepuls?", FACH, False]],
  "chk": {"f1": {"sel": "Physik"}, "f2": {"sel": "Biologie"}, "f3": {"sel": "Chemie"}, "f4": {"sel": "keine NAWI-Frage"}, "f5": {"sel": "Biologie"}},
  "sol": [["Lösung", ["a) Physik – Bewegung, Kräfte, Flug.",
                      "b) Biologie – Wachstum eines Lebewesens.",
                      "c) Chemie – Eisen reagiert mit Sauerstoff und Wasser, ein neuer Stoff (Rost) entsteht.",
                      "d) keine NAWI-Frage – eine wirtschaftliche und politische Entscheidung. Messungen können Fakten liefern, die Entscheidung selbst treffen Menschen.",
                      "e) Biologie – Anpassung des Körpers an Training (mit Bezug zum Sport)."]]],
  "tip": ["Welche Fragen kann NAWI beantworten?", "theorie.html#fragen"]},

 {"id": "a4", "nr": 4, "title": "Unsere Vermutung – vor dem ersten Wurf", "src": "Buch S. 29", "own": True, "tag": "Teil 1", "h": 1, "zeit": 4,
  "q": "Arbeitet in eurer Versuchsgruppe und schreibt die Antworten VOR dem Versuch auf. Danach darf nichts mehr geändert werden. a) Eure Hypothese in einem Satz mit »weil …«. "
       "b) Eure Vorhersage für die drei Vergleichspaare: Was erwartet ihr für A (ohne Klammer) und B (mit Klammer)? c) Welches Ergebnis würde gegen eure Hypothese sprechen?",
  "hint": "Auch »Mit Klammer fliegt er kürzer, weil …« ist eine gute Hypothese – wichtig ist, dass ihr sie vorher festlegt und begründet. Info: Theorieteil Teil 1 »Unser Versuch: der Plan«",
  "type": "multi",
  "fields": [["hyp", "a) Unsere Hypothese (ein Satz mit »weil«)"], ["vor", "b) Unsere Vorhersage für die Vergleichspaare"], ["gegen", "c) Das würde gegen unsere Hypothese sprechen"]],
  "chk": {"hyp": {"kw": [["Klammer / Gewicht vorne", r"klammer|gewicht|schwer|nase|vorn|masse|schwerpunkt"], ["Begründung (weil …)", r"weil|denn|da |deshalb|darum|daher"]], "man": True},
          "vor": {"kw": [["Vergleich A und B / mit und ohne", r"\bb\b|\ba\b|mit|ohne|klammer|mittel|weiter|kürzer|kuerzer|gleich|weniger|mehr"]], "man": True},
          "gegen": {"kw": [["Gegenbefund", r"weiter|kürzer|kuerzer|gleich|kein|nicht|unterschied|mittel|weniger|mehr"]], "man": True}},
  "sol": [["Beispiel", ["a) »Mit Büroklammer an der Nase fliegt unser Flieger im Mittel weiter, weil die schwerere Nase ihn ruhiger und gerader gleiten lässt.« (Auch »kürzer, weil er schwerer ist« ist zulässig, wenn es vorher begründet festgelegt wurde.)",
                        "b) »Wir erwarten, dass der Mittelwert von B größer ist als der von A.«",
                        "c) »Wenn B im Mittel gleich weit oder kürzer fliegt als A, spricht das gegen unsere Hypothese.« Ein einzelner kurzer B-Flug widerlegt sie noch nicht – es zählt die ganze Messreihe."]]],
  "tip": ["Unser Versuch: der Plan", "theorie.html#plan"]},

 # ======================================================= Teil 2 · Der Papierflieger-Test (Buch S. 29)
 {"id": "a5", "nr": 5, "title": "Zählt der Wurf?", "src": "Buch S. 29", "own": True, "tag": "Teil 2", "h": 2, "zeit": 3,
  "q": "Vor dem Start legen wir die Regeln fest – nicht erst, wenn wir den Sieger kennen. Entscheide für jeden Fall nach unseren Messregeln. f) Wähle: Was genau messen wir?",
  "hint": "Regulär schlechte Flüge zählen. Ungültig ist ein Wurf nur, wenn eine vorher festgelegte Regel verletzt wurde. Decken- und Wandkontakte werden nicht gelöscht. Info: Theorieteil Teil 2 »Die Messregeln«",
  "type": "multi",
  "fields": [["w1", "a) Der Flieger geht nach 2 m steil zu Boden.", WURF, False],
             ["w2", "b) Der Werfer steht beim Abwurf mit dem Fuß über der Abwurflinie.", WURF, False],
             ["w3", "c) Der Flieger streift die Decke und landet bei 5,1 m.", WURF, False],
             ["w4", "d) Eine Person geht durch die Flugbahn, der Flieger prallt an ihr ab.", WURF, False],
             ["w5", "e) Bei Zustand B fällt die Büroklammer im Flug ab.", WURF, False],
             ["mess", "f) Gemessen wird …", ["die Weite bis zum ersten Bodenkontakt", "die Weite bis zum Stillstand", "die Flugzeit in Sekunden", "nur der weiteste Wurf der Gruppe"]]],
  "chk": {"w1": {"sel": "gültig – zählt"}, "w2": {"sel": "ungültig – wiederholen"}, "w3": {"sel": "zählt, Kontakt notieren"},
          "w4": {"sel": "ungültig – wiederholen"}, "w5": {"sel": "ungültig – wiederholen"}, "mess": {"sel": "die Weite bis zum ersten Bodenkontakt"}},
  "sol": [["Lösung", ["a) gültig – auch ein kurzer, regulärer Flug zählt. Sonst würden wir nur die guten Werte behalten.",
                      "b) ungültig – Regel »hinter der Linie abwerfen« verletzt. Wurf wiederholen und den Vorfall notieren.",
                      "c) zählt, Kontakt notieren – der Wert bleibt in der Tabelle, in der Spalte »Decke/Wand« steht ein Vermerk. Nicht löschen, nicht durch 0 ersetzen.",
                      "d) ungültig – Eingriff von außen. Erst werfen, wenn die Flugbahn frei ist.",
                      "e) ungültig – der Zustand B war nicht mehr gegeben. Klammer fester aufschieben, Wurf wiederholen, Vorfall notieren.",
                      "f) die Weite bis zum ersten Bodenkontakt, entlang des Bandmaßes ab der Abwurflinie, auf 0,1 m gerundet."]]],
  "tip": ["Die Messregeln", "theorie.html#regeln"]},

 # ======================================================= Teil 3 · Wie Forschung wirklich läuft (Buch S. 29)
 {"id": "a6", "nr": 6, "title": "Alte Messdaten kritisch lesen", "src": "Buch S. 29", "own": True, "tag": "Teil 3", "h": 3, "zeit": 7, "img": "img/vorjahr.png",
  "q": "Arbeitet zuerst zu zweit OHNE Handy mit der Tabelle (Beamer bzw. Theorieteil Teil 3). Zwei Klassen haben in einem früheren Jahr einen kurzen und einen langen Flieger verglichen – je ein Wurf pro Flieger. "
       "a) Alte 1AK: In wie vielen Gruppen flog der kurze Flieger weiter? b) Alte 1BK: Welche Gruppe passt nicht zum Muster der anderen vollständigen Paare? "
       "c) Alte 1BK: Bei welcher Gruppe fehlt ein gültiger Wert? d) Reichen diese Daten, um zu sagen, WARUM ein Flieger weiter flog? Begründe in 2 Sätzen.",
  "hint": "Vergleiche in jeder Zeile »kurz« und »lang«. »Ung.« heißt ungültig bzw. fehlend. Zu d): Wie viele Würfe gab es, und was war bei den Fliegern alles verschieden?",
  "type": "multi",
  "fields": [["anz", "a) Anzahl der Gruppen (Zahl)"],
             ["muster", "b) Gruppe, die nicht ins Muster passt", ["Gruppe 3", "Gruppe 1", "Gruppe 4", "Gruppe 7"]],
             ["fehlt", "c) Gruppe mit fehlendem Wert", ["Gruppe 5", "Gruppe 3", "Gruppe 4", "Gruppe 6"]],
             ["warum", "d) Reichen die Daten für eine Ursache? (2 Sätze)"]],
  "chk": {"anz": {"kw": [["3 Gruppen", r"^\s*(in\s+)?(3|drei)\b(?![.,]\d)(?!.*\b(oder|bis)\b)"]]},
          "muster": {"sel": "Gruppe 3"}, "fehlt": {"sel": "Gruppe 5"},
          "warum": {"contra": [r"^\s*ja\b"], "kw": [["nein / reicht nicht", r"nein|reicht nicht|zu wenig|nicht genug|nicht sagen"],
                           ["Grund (nur ein Wurf, viele Unterschiede, Werfer, Bauform …)", r"ein(em)? wurf|einmal|wiederhol|werfer|bauform|form|falt|unterschied|viele|mehrere|gleichzeitig|dokument|decke|zufall|streu"]], "need": 2, "man": True}},
  "sol": [["Lösung", ["a) 3 – in Gruppe 1, 2 und 6 der alten 1AK flog der kurze Flieger weiter, in Gruppe 3, 4, 5 und 7 der lange.",
                      "b) Gruppe 3 – dort flog der kurze Flieger (15,31 m) viel weiter als der lange (4,77 m); in den anderen vollständigen Paaren der alten 1BK flog der lange weiter.",
                      "c) Gruppe 5 – beim langen Flieger steht »Ung.«; ohne zweiten Wert ist kein Vergleich möglich. Die Ursache ist nicht dokumentiert.",
                      "d) Nein. Jede Gruppe hatte nur einen Wurf je Flieger, und zwischen kurzem und langem Flieger war vieles gleichzeitig verschieden (Form, Faltung, Werfer, Abwurf). "
                      "Eine Gruppe mit anderem Ergebnis hat deshalb nicht automatisch falsch gemessen."]]],
  "tip": ["Alte Daten kritisch lesen", "theorie.html#vorjahr"]},

 {"id": "a7", "nr": 7, "title": "Partnercheck: So läuft Forschung", "src": "Buch S. 29", "own": True, "tag": "Teil 3", "h": 3, "zeit": 5,
  "q": "Arbeitet zu zweit OHNE Handy mit den Partnerkarten (Beamer bzw. Ende von Teil 3). A stellt 3 Fragen, B antwortet, A kontrolliert mit der Lösung auf der Karte. Dann Rollen tauschen. "
       "Erst danach eintragen: a) Mit wem hast du gearbeitet? (Vorname) b) Welche Frage war schwierig – und wie lautet die richtige Antwort? (1–2 Sätze) Oder schreib »alle Fragen richtig«.",
  "hint": "Erst mündlich abfragen, dann eintragen. Die Lehrkraft bewertet b).",
  "type": "multi",
  "fields": [["partner", "a) Partnercheck mit (Vorname)"], ["check", "b) Schwierige Frage und richtige Antwort"]],
  "chk": {"partner": {"kw": [["Vorname", r"[a-zäöüß]{2,}"]], "man": True},
          "check": {"kw": [["Antwort oder »alle richtig«", r"richtig|kreislauf|modell|vereinfach|grenze|veröffentl|veroeffentl|begutacht|peer|wiederhol|semmelweis|hände|haende|messung|bedingung"]], "man": True}},
  "sol": [["Lösung", ["a) Vorname des Partners.",
                      "b) Lösungen der Karten: Forschung ist ein Kreislauf mit Rückschritten · ein Modell ist eine Vereinfachung für einen Zweck und hat Grenzen · "
                      "Methode veröffentlichen, damit andere prüfen und wiederholen können · Begutachtung senkt Fehler, garantiert aber keine Wahrheit · "
                      "Semmelweis: Händewaschen mit Chlorkalk, Vorhersage weniger Tote durch Kindbettfieber · abweichendes Ergebnis → zuerst Messung und Bedingungen prüfen."]]],
  "tip": ["Partnerkarten", "theorie.html#partner"]},

 # ======================================================= Teil 4 · Auswerten und vorsichtig schließen (Buch S. 29–32)
 {"id": "a8", "nr": 8, "title": "Mittelwert und Spannweite", "src": "Buch S. 29", "own": True, "tag": "Teil 4", "h": 4, "zeit": 4,
  "q": "Übungsdaten (nicht eure Messung): Ein Flieger flog ohne Klammer 3,8 m · 4,6 m · 4,2 m und mit Klammer 5,1 m · 3,9 m · 5,4 m. "
       "a) Berechne den Mittelwert ohne Klammer (A) in m. b) Berechne den Mittelwert mit Klammer (B) in m. c) Berechne die Spannweite von B in m. d) Wähle die passende Schlussfolgerung.",
  "hint": "Mittelwert = Summe der Werte : Anzahl der Werte. Spannweite = größter Wert − kleinster Wert. Info: Theorieteil Teil 4 »Mittelwert und Spannweite«",
  "type": "multi",
  "fields": [["ma", "a) Mittelwert A (mit Einheit)"], ["mb", "b) Mittelwert B (mit Einheit)"], ["sb", "c) Spannweite B (mit Einheit)"],
             ["schluss", "d) Schlussfolgerung", ["B flog im Mittel 0,6 m weiter, die Werte überlappen aber stark – noch keine Entscheidung möglich (unklar).",
                                                   "Damit ist bewiesen, dass eine Büroklammer jeden Flieger verbessert.",
                                                   "A war besser, weil der kürzeste Wurf bei B war.",
                                                   "Man kann gar nichts sagen, weil ein Wert klein war."]]],
  "chk": {"ma": {"num": 4.2, "unit": "m"}, "mb": {"num": 4.8, "unit": "m"}, "sb": {"num": 1.5, "unit": "m"},
          "schluss": {"sel": "B flog im Mittel 0,6 m weiter, die Werte überlappen aber stark – noch keine Entscheidung möglich (unklar)."}},
  "sol": [["Lösung", ["a) (3,8 + 4,6 + 4,2) m : 3 = 12,6 m : 3 = 4,2 m.",
                      "b) (5,1 + 3,9 + 5,4) m : 3 = 14,4 m : 3 = 4,8 m.",
                      "c) 5,4 m − 3,9 m = 1,5 m.",
                      "d) unklar: B war im Mittel um 0,6 m weiter, aber die Werte von A (3,8–4,6 m) und B (3,9–5,4 m) überlappen stark, und es sind nur drei Würfe. Noch keine Entscheidung möglich."]]],
  "tip": ["Mittelwert und Spannweite", "theorie.html#mittelwert"]},

 {"id": "a9", "nr": 9, "title": "Eine KI-Antwort prüfen", "src": "Buch S. 29", "own": True, "tag": "Teil 4", "h": 4, "zeit": 4,
  "q": "Eine KI schreibt zu unserem Versuch: 1. »Wenn B weiter fliegt, ist eure Hypothese bewiesen.« 2. »Wenn ein einziger B-Flug kurz war, ist die Hypothese widerlegt.« "
       "3. »Eine Behauptung, die keine denkbare Beobachtung widerlegen kann, ist keine prüfbare wissenschaftliche Hypothese.« 4. »Wird eine Hypothese oft bestätigt, wird sie automatisch zum Gesetz.« "
       "Entscheide bei jeder Aussage, ob sie stimmt. e) Schreib Aussage 1 in einem Satz richtig.",
  "hint": "KI-Antworten klingen sicher, sind es aber nicht immer. Prüf jede Aussage mit Teil 1 und Teil 4 des Theorieteils.",
  "type": "multi",
  "fields": [["k1", "Aussage 1", STIMMT, False], ["k2", "Aussage 2", STIMMT, False], ["k3", "Aussage 3", STIMMT, False], ["k4", "Aussage 4", STIMMT, False],
             ["korr", "e) Aussage 1 richtig formuliert (1 Satz)"]],
  "chk": {"k1": {"sel": "stimmt nicht"}, "k2": {"sel": "stimmt nicht"}, "k3": {"sel": "stimmt"}, "k4": {"sel": "stimmt nicht"},
          "korr": {"kw": [["unterstützt / spricht für", r"unterstütz|unterstuetz|stütz|stuetz|spricht (\w+ )?(für|fuer|dafür|dafuer)|passt|hinweis|stärk|staerk"], ["nicht bewiesen / vorläufig / unter diesen Bedingungen", r"nicht (endgültig |endgueltig |sicher )?bewiesen|kein (endgültiger |endgueltiger )?beweis|beweis \w+ (es|das) (aber )?nicht|bewiesen ist (sie|die hypothese|das|es) (\w+ )*nicht|vorläufig|vorlaeufig|unter (diesen|unseren) bedingungen|nur für|nur fuer|nur bei|vorsichtig|wahrscheinlich"]], "need": 2, "man": True}},
  "sol": [["Lösung", ["1. stimmt nicht – ein passendes Ergebnis unterstützt die Hypothese unter unseren Bedingungen, beweist sie aber nicht endgültig.",
                      "2. stimmt nicht – unsere Hypothese betrifft den Mittelwert. Ein einzelner kurzer Flug widerlegt sie nicht; es zählt die ganze geplante Messreihe.",
                      "3. stimmt – das ist Poppers Idee der Falsifizierbarkeit. Nicht prüfbar heißt aber nicht automatisch falsch.",
                      "4. stimmt nicht – es gibt keine automatische Stufenleiter Hypothese → Gesetz → Theorie. Ein Gesetz beschreibt eine Regelmäßigkeit, eine Theorie erklärt.",
                      "e) z. B. »Wenn B unter unseren Bedingungen im Mittel klar weiter fliegt, unterstützt das unsere Vorhersage – bewiesen ist die Hypothese damit nicht, und die Begründung (»weil …«) hat der Test gar nicht geprüft.«"]]],
  "tip": ["Widerlegbar muss es sein", "theorie.html#popper"]},

 {"id": "a10", "nr": 10, "title": "Forschen oder konstruieren?", "src": "Buch S. 29", "own": True, "tag": "Teil 4", "h": 4, "zeit": 4,
  "q": "Zu zweit: Unser Papierflieger-Projekt lässt sich auch als Konstruktionszyklus beschreiben – so arbeiten Technikerinnen und Techniker. Ordne jede Tätigkeit dem passenden Schritt zu. "
       "g) Welche EINE Änderung würdet ihr als Nächstes testen – und was muss dabei gleich bleiben?",
  "hint": "Überleg bei jeder Tätigkeit: Kommt sie vor dem Bauen, beim Bauen oder nach dem Test? Info: Theorieteil Teil 4 »Forschen oder konstruieren?«",
  "type": "multi",
  "fields": [["z4", "a) Wir werfen drei Vergleichspaare und schreiben alles auf.", ZYKLUS, False],
             ["z1", "b) Wir legen fest, was »weit« heißt und wie Deckenkontakte zählen.", ZYKLUS, False],
             ["z6", "c) Wir schieben die Klammer 2 cm nach hinten und testen neu.", ZYKLUS, False],
             ["z3", "d) Wir falten den Flieger nach Anleitung.", ZYKLUS, False],
             ["z5", "e) Wir vergleichen Mittelwerte, Spannweiten und Kontakte.", ZYKLUS, False],
             ["z2", "f) Wir wählen den Planarflieger und planen die Klammer vorne am Rumpf.", ZYKLUS, False],
             ["naechst", "g) Unsere nächste Änderung – und was gleich bleibt"]],
  "chk": {"z1": {"sel": "Problem analysieren"}, "z2": {"sel": "Entwerfen"}, "z3": {"sel": "Konstruieren"}, "z4": {"sel": "Testen"}, "z5": {"sel": "Bewerten"}, "z6": {"sel": "Verbessern"},
          "naechst": {"kw": [["eine Änderung", r"klammer|position|flügel|fluegel|papier|falt|rumpf|ecken|höhe|hoehe|werf|nase|größe|groesse|form"], ["bleibt gleich", r"gleich|selb|nicht ändern|nicht aendern|konstant|sonst nichts|nur eine|alles andere"]], "need": 2, "man": True}},
  "sol": [["Lösung", ["a) Testen · b) Problem analysieren · c) Verbessern · d) Konstruieren · e) Bewerten · f) Entwerfen.",
                      "g) z. B. »Wir schieben die Klammer 2 cm nach hinten. Gleich bleiben derselbe Flieger, derselbe Werfer, dieselbe Abwurfhöhe und die drei Vergleichspaare.«",
                      "Unterschied: Beim Forschen prüfen wir eine Hypothese (Was stimmt?). Beim Konstruieren verbessern wir einen Entwurf für ein Ziel (Was funktioniert besser?). Beide brauchen faire Tests."]]],
  "tip": ["Forschen oder konstruieren?", "theorie.html#zyklus"]},

 # ======================================================= Zusatz · Für Schnelle und Neugierige
 {"id": "a11", "nr": 11, "title": "Zufällig oder systematisch?", "src": "Buch S. 29–32", "own": True, "tag": "Zusatz", "h": 0, "zeit": 4, "img": "img/zielscheiben.png",
  "q": "Drei Schützen haben je 6 Schuss auf eine Scheibe abgegeben (Bild). Ordne jede Scheibe zu. d) Ein Werfer lässt den Flieger immer etwas nach links los. Welche Fehlerart ist das?",
  "hint": "Zufällige Fehler streuen in alle Richtungen. Ein systematischer Fehler verschiebt alle Treffer in dieselbe Richtung. Info: Theorieteil »Für Schnelle«",
  "type": "multi",
  "fields": [["sch1", "a) Scheibe 1", ZIEL, False], ["sch2", "b) Scheibe 2", ZIEL, False], ["sch3", "c) Scheibe 3", ZIEL, False],
             ["links", "d) Immer etwas nach links", ["systematischer Fehler", "zufällige Streuung", "gar kein Fehler"]]],
  "chk": {"sch1": {"sel": "zufällige Streuung"}, "sch2": {"sel": "systematischer Fehler"}, "sch3": {"sel": "genau und wenig Streuung"}, "links": {"sel": "systematischer Fehler"}},
  "sol": [["Lösung", ["a) Scheibe 1: zufällige Streuung – die Treffer liegen verstreut um die Mitte.",
                      "b) Scheibe 2: systematischer Fehler – eng beisammen, aber alle nach rechts oben verschoben (z. B. verstelltes Visier).",
                      "c) Scheibe 3: genau und wenig Streuung – eng beisammen in der Mitte.",
                      "d) systematischer Fehler – er wirkt immer in dieselbe Richtung. Mehr Würfe helfen dagegen nicht, man muss die Ursache beheben."]]],
  "tip": ["Zufällig oder systematisch?", "theorie.html#zielscheiben"]},

 {"id": "a12", "nr": 12, "title": "Prüfbar oder nicht?", "src": "Buch S. 29", "own": True, "tag": "Zusatz", "h": 0, "zeit": 4,
  "q": "Entscheide, ob man die Aussage mit Beobachtungen oder Messungen prüfen kann. e) Ist eine nicht prüfbare Aussage automatisch falsch? Begründe in einem Satz.",
  "hint": "Prüfbar heißt: Man kann sagen, welche Beobachtung gegen die Aussage sprechen würde. Info: Theorieteil Teil 4 »Widerlegbar muss es sein«",
  "type": "multi",
  "fields": [["p1", "a) Mit größeren Flügeln fliegt unser Flieger im Mittel länger.", PRUEFBAR, False],
             ["p2", "b) Ein unsichtbarer Geist lenkt jeden Flieger – aber nur, wenn niemand hinschaut.", PRUEFBAR, False],
             ["p3", "c) Kressesamen keimen bei 20 °C schneller als bei 10 °C.", PRUEFBAR, False],
             ["p4", "d) Mein Flieger ist der beste – verliert er, zählt der Wurf eben nicht.", PRUEFBAR, False],
             ["auto", "e) Nicht prüfbar = falsch? (1 Satz)"]],
  "chk": {"p1": {"sel": "prüfbar"}, "p2": {"sel": "nicht prüfbar"}, "p3": {"sel": "prüfbar"}, "p4": {"sel": "nicht prüfbar"},
          "auto": {"kw": [["nein / nicht automatisch", r"nein|nicht automatisch|nicht unbedingt|nicht falsch|nicht zwingend|kann (trotzdem|auch) (stimm|wahr|richtig)|wahr sein|richtig sein|weiß man nicht|weiss man nicht"]], "man": True}},
  "sol": [["Lösung", ["a) prüfbar – Vergleichsreihe mit zwei Flügelgrößen, sonst alles gleich.",
                      "b) nicht prüfbar – so formuliert, dass keine Beobachtung sie widerlegen kann.",
                      "c) prüfbar – zwei Schalen bei verschiedenen Temperaturen, Keimlinge zählen.",
                      "d) nicht prüfbar – jede Niederlage wird nachträglich ausgeklammert. Regeln müssen vorher feststehen.",
                      "e) Nein – sie liegt nur außerhalb dessen, was die Naturwissenschaft mit Messungen entscheiden kann. Wir können sie weder bestätigen noch widerlegen."]]],
  "tip": ["Widerlegbar muss es sein", "theorie.html#popper"]},

 {"id": "a13", "nr": 13, "title": "Forschungskarte: Wiederholen", "src": "Buch S. 29", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Lies die Forschungskarte »Wiederholen ist Pflicht« im Theorieteil (Für Schnelle). a) Wie viele Experimente konnte das Team am Ende tatsächlich wiederholen? "
       "b) Wie groß waren die gemessenen Effekte bei der Wiederholung im Vergleich zum Original (Median)? c) Was bedeutet das für unseren Papierflieger-Test? (1 Satz)",
  "hint": "Alle Zahlen stehen auf der Karte. Zu c): Denk an die Gegenprobe mit einem zweiten Werfer.",
  "type": "multi",
  "fields": [["anz", "a) Tatsächlich wiederholt", ["50 Experimente", "alle 193 Experimente", "10 Experimente", "kein einziges Experiment"]],
             ["eff", "b) Effekte bei der Wiederholung", ["deutlich kleiner", "genau gleich groß", "doppelt so groß", "gar nicht messbar"]],
             ["uns", "c) Bedeutung für unseren Test (1 Satz)"]],
  "chk": {"anz": {"sel": "50 Experimente"}, "eff": {"sel": "deutlich kleiner"},
          "uns": {"kw": [["wiederholen / Gegenprobe / anderer Werfer", r"wiederhol|gegenprobe|zweite[nr]? werfer|andere[nr]? (werfer|gruppe)|andere|bestätig|bestaetig|nachmach|nochmal|noch einmal|mehr würfe|mehr wuerfe|genau beschreib|protokoll"]], "man": True}},
  "sol": [["Lösung", ["a) 50 Experimente (aus 23 Fachartikeln) – geplant waren 193.",
                      "b) deutlich kleiner – im Median um 85 % kleiner als in den Originalarbeiten.",
                      "c) Ein einzelnes Ergebnis reicht nicht: Erst wenn eine Wiederholung – z. B. die Gegenprobe mit einem zweiten Werfer – ein ähnliches Ergebnis liefert, vertrauen wir ihm mehr. Dafür muss das Protokoll genau sein."]]],
  "tip": ["Wiederholen ist Pflicht", "theorie.html#forschung"]},

 {"id": "a14", "nr": 14, "title": "Video, Podcast oder Plakat", "src": "Buch S. 28–29", "own": True, "tag": "Zusatz", "h": 0, "zeit": 25,
  "q": "Kreativ, freiwillig, allein oder zu zweit: Erkläre neuen Rekruten in höchstens 2 Minuten (Video), 3 Minuten (Podcast) oder auf einem A3-Plakat (mit der Hand), was eine Hypothese und was eine wissenschaftliche Theorie ist. "
       "Pflichtinhalte: 1. Hypothese = begründete, prüfbare Vermutung. 2. Theorie = Erklärung, die viele geprüfte Befunde verbindet. 3. ein Beispiel aus unserem Papierflieger-Test. 4. warum »nur eine Theorie« ein Irrtum ist. "
       "Abgabe (freiwillig, Termin sagt Stephan): Plakat als Foto ins PDF, Video oder Podcast als Datei in LMS (Teams nur, wenn die Datei zu groß ist). Trag hier Titel, Form und »hochgeladen am …« ein.",
  "hint": "Keine fremde Musik, keine fremden Bilder. Andere Personen nur mit Zustimmung aufnehmen. Wenn dir eine KI beim Skript hilft, schreib das dazu – und prüf den Inhalt.",
  "type": "multi",
  "fields": [["titel", "Titel"], ["form", "Form (Video, Podcast oder Plakat)"], ["inhalt", "Worum geht es? (1–2 Sätze)"], ["hoch", "hochgeladen in LMS am … / Plakat-Foto im PDF"]],
  "chk": {"titel": {"kw": [["Titel", r"[a-zäöüß]{3,}"]], "man": True}, "form": {"kw": [["Form", r"video|podcast|plakat|audio|film"]], "man": True},
          "inhalt": {"kw": [["Hypothese", r"hypothes|vermut"], ["Theorie", r"theorie"]], "man": True}, "hoch": {"kw": [["Abgabe", r"\d|lms|teams|foto|hochgeladen"]], "man": True}},
  "sol": [["Bewertung", ["Raster (10 P.): fachlich richtig 4 · alle vier Pflichtinhalte 2 · verständlich und gut gegliedert 2 · kreativ/ansprechend 1 · Länge und Abgabe eingehalten 1.",
                         "Muss vorkommen: Hypothese begründet und prüfbar · Theorie verbindet viele Befunde und erlaubt Vorhersagen · Beispiel Büroklammer-Test · »nur eine Theorie« verwechselt den Alltagsbegriff (Vermutung) mit dem wissenschaftlichen."]]],
  "tip": ["Theorie, Gesetz und Modell", "theorie.html#theorie"]},
]
assert [t["nr"] for t in T] == list(range(1, 15))
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
# Rechenkontrolle Aufgabe 8 (vom Aufgabentext aus)
assert abs((4.8 + 5.6 + 5.2) / 3 - 5.2) < 1e-9 and abs((6.1 + 4.9 + 6.4) / 3 - 5.8) < 1e-9 and abs(6.4 - 4.9 - 1.5) < 1e-9

PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
BESPRECHEN = [1, 2, 3, 5, 6, 8, 9]  # in der Stunde gemeinsam besprechen (TH-Unterricht, Lösungsmappe); die anderen kontrolliert die PDF
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True

GRP = {1: TEILNAME[1] + " (Buch S. 28–29) · 1AK: Stunde 1 · Do 05.11. · 1BK: Stunde 1 · Mi 04.11.",
       2: TEILNAME[2] + " (Buch S. 29) · " + wann(2) + " · im Eingangsbereich",
       3: TEILNAME[3] + " (Buch S. 29) · beide Klassen: Fr 06.11. nach dem Test",
       4: TEILNAME[4] + " (Buch S. 29–32) · " + wann(4),
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)"}

LERNZIELE = ["eine **naturwissenschaftliche Frage** erkennen und **Biologie, Chemie oder Physik** zuordnen – und Fragen erkennen, die keine Messung beantworten kann",
             "**Beobachtung, Hypothese, Vorhersage und Theorie** unterscheiden und erklären, warum eine Theorie mehr ist als eine Vermutung",
             "einen **fairen Test** planen und durchführen: nur eine Sache ändern, Messregeln vorher festlegen, wiederholen, alles aufschreiben",
             "aus Messwerten **vorsichtig schließen**: Mittelwert und Spannweite nutzen, Grenzen nennen und sagen, ob die Daten die Vermutung unterstützen, dagegen sprechen oder unklar sind"]

WICHTIGSTE = ["Eine **Beobachtung** beschreibt, was wir sehen oder messen; eine **Hypothese** ist eine begründete, **prüfbare** Vermutung; eine **Vorhersage** sagt, was beim nächsten Test herauskommen sollte.",
              "Eine wissenschaftliche **Theorie** ist keine Vermutung, sondern eine Erklärung, die **viele geprüfte Befunde** verbindet und Vorhersagen erlaubt; ein **Gesetz** beschreibt eine Regelmäßigkeit unter bestimmten Bedingungen.",
              "Ein **fairer Test** ändert nur **eine** Sache, legt die Regeln **vorher** fest, wiederholt die Messung und behält **alle gültigen** Werte – auch die schlechten.",
              "Ein passendes Ergebnis **unterstützt** eine Hypothese, **beweist** sie aber nicht; eine Aussage, die keine Beobachtung widerlegen kann, ist **nicht prüfbar** – aber nicht automatisch falsch.",
              "Forschung ist ein **Kreislauf**: Ergebnisse werden veröffentlicht, von anderen geprüft und wiederholt – und werfen neue Fragen auf."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Beobachtung", "was man wahrnimmt oder misst (Ergebnis, auch im Experiment); »beobachten« als Methode heißt: zuschauen, ohne einzugreifen"],
                ["Experiment (Versuch)", "gezielter Eingriff: eine Bedingung wird geplant verändert und die Wirkung gemessen"],
                ["qualitativ", "Ergebnis in Worten (»der Flieger kippt nach links«)"],
                ["quantitativ", "Ergebnis als Zahl, meist mit Einheit (»5,8 m«)"],
                ["Hypothese", "begründete, prüfbare Vermutung über einen Zusammenhang; man kann sagen, was gegen sie sprechen würde"],
                ["Vorhersage", "erwartetes Ergebnis eines bestimmten Tests, abgeleitet aus Hypothese oder Theorie"],
                ["Theorie (wissenschaftlich)", "zusammenhängende Erklärung, die viele geprüfte Befunde verbindet und überprüfbare Vorhersagen erlaubt"],
                ["Gesetz", "Beschreibung einer Regelmäßigkeit unter bestimmten Bedingungen, oft als Formel"],
                ["Modell", "gezielte Vereinfachung für einen Zweck; zeigt manches, lässt anderes weg – hat Grenzen"],
                ["fairer Test (Variablen kontrollieren)", "nur eine Bedingung wird verändert, alle anderen bleiben gleich"],
                ["Gegenprobe", "Wiederholung unter etwas anderen Bedingungen (z. B. anderer Werfer), um ein Ergebnis zu überprüfen"],
                ["Mittelwert", "Summe aller Werte geteilt durch die Anzahl der Werte"],
                ["Spannweite", "größter Wert minus kleinster Wert – zeigt, wie stark die Werte streuen"],
                ["Falsifizierbarkeit", "eine Aussage ist so formuliert, dass eine Beobachtung sie widerlegen könnte (Karl Popper)"],
                ["Publikation", "Veröffentlichung von Methode und Ergebnissen, damit andere sie prüfen können"],
                ["Begutachtung (Peer Review)", "Fachleute prüfen eine Arbeit vor der Veröffentlichung; das senkt Fehler, garantiert aber keine Wahrheit"],
                ["Konstruktionszyklus", "Arbeitsweise der Technik: Problem analysieren → Entwerfen → Konstruieren → Testen → Bewerten → Verbessern"]]

WEISST_DU_NOCH = {
    2: [("Was ist der Unterschied zwischen Hypothese und Vorhersage?", "Die Hypothese ist die begründete Vermutung (»weil …«), die Vorhersage das erwartete Ergebnis genau dieses Tests."),
        ("Warum habt ihr eure Hypothese VOR dem ersten Wurf aufgeschrieben?", "Damit wir sie nicht nachträglich an das Ergebnis anpassen.")],
    3: [("Ist eine wissenschaftliche Theorie »nur eine Vermutung«?", "Nein – sie verbindet viele geprüfte Befunde und erlaubt Vorhersagen."),
        ("Welche Frage gehört zur Chemie: Keimung, Rost oder Flugweite?", "Rost – ein neuer Stoff entsteht.")],
    4: [("Ein Flug streift die Decke. Was macht ihr mit dem Wert?", "Behalten und in der Spalte Decke/Wand vermerken – nicht löschen, nicht durch 0 ersetzen."),
        ("Was macht die Gegenprobe?", "Ein zweiter Werfer wiederholt die Vergleichspaare – so sehen wir, ob das Ergebnis auch bei jemand anderem ähnlich ist.")],
}

STOPPFRAGEN = {
    1: [("»Unser Flieger flog einmal weiter – also ist unsere Theorie bewiesen.« Was ist falsch?", "Ein einzelner Wert sagt wenig, und auch viele Werte beweisen eine Hypothese nicht endgültig. Außerdem prüfen wir eine Hypothese zu einer Änderung, keine Theorie."),
        ("Ist »Sollen wir mehr Geld für Hubschrauber ausgeben?« eine naturwissenschaftliche Frage?", "Nein – das ist eine Entscheidung (Wirtschaft, Politik). Messungen liefern nur Fakten dazu.")],
    2: [("Warum werfen wir A und B abwechselnd statt erst dreimal A und dann dreimal B?", "Damit Übung, Müdigkeit oder ein verbogener Flieger nicht nur einen Zustand treffen."),
        ("Was ändert die Büroklammer alles?", "Vor allem Masse und Schwerpunkt, außerdem klemmt sie den Rumpf zusammen. Darum können wir nicht sagen, was davon wirkt.")],
    3: [("Ist Forschung eine gerade Linie von Schritt 1 bis 8?", "Nein – ein Kreislauf mit Rückschritten und neuen Fragen."),
        ("Garantiert eine Begutachtung, dass ein Ergebnis stimmt?", "Nein – sie senkt Fehler; Vertrauen entsteht, wenn andere das Ergebnis wiederholen.")],
    4: [("B: 5,1 m, 6,3 m, 5,7 m. Wie groß ist der Mittelwert?", "(5,1 + 6,3 + 5,7) m : 3 = 17,1 m : 3 = 5,7 m."),
        ("Die Daten sind unklar. Ist der Versuch dann gescheitert?", "Nein – »noch keine Entscheidung möglich« ist ein erlaubtes Ergebnis.")],
}
assert abs((5.1 + 6.3 + 5.7) / 3 - 5.7) < 1e-9

PARTNERKARTEN = [("Ist Forschung eine gerade Linie von Schritt 1 bis Schritt 8?", "Nein – ein Kreislauf: Man geht zurück, ändert Bedingungen und findet neue Fragen."),
                 ("Was ist ein Modell – und was hat jedes Modell?", "eine gezielte Vereinfachung für einen Zweck; jedes Modell hat Grenzen"),
                 ("Warum veröffentlichen Forscher ihre Methode ganz genau?", "damit andere sie prüfen und den Versuch wiederholen können"),
                 ("Garantiert eine Begutachtung (Peer Review), dass ein Ergebnis stimmt?", "Nein – sie senkt Fehler. Sicherer wird es, wenn andere das Ergebnis wiederholen."),
                 ("Was führte Semmelweis 1847 in Wien ein – und was sagte er voraus?", "Händewaschen mit Chlorkalklösung; Vorhersage: weniger Mütter sterben am Kindbettfieber"),
                 ("Eine Gruppe misst etwas ganz anderes als alle anderen. Hat sie falsch gemessen?", "Nicht automatisch – zuerst Messung, Bedingungen und Protokoll prüfen.")]

STOLPERSTEINE = [("»Theorie = Vermutung«", "Im Alltag heißt »Theorie« oft »Vermutung«. In der Naturwissenschaft ist eine **Theorie** eine gut geprüfte Erklärung vieler Befunde (Zelltheorie, Evolutionstheorie). Mit Aufgabe 2d und 9 gezielt ansprechen (TH-Fachwissen Abschnitt 2)."),
                 ("Stufenleiter Hypothese → Gesetz → Theorie", "Buch S. 29 klingt so, als würde eine oft bestätigte Hypothese automatisch zum Gesetz bzw. zur Theorie und eine Theorie sei »mehrere Gesetze«. Gesetz **beschreibt**, Theorie **erklärt** – keine Rangfolge (National Academy of Sciences 1998)."),
                 ("»Bestätigt = bewiesen« / »ein Gegenwert = widerlegt«", "Klassenversuche **unterstützen** oder **schwächen** eine begrenzte Hypothese. Unsere Hypothese betrifft den **Mittelwert** – ein einzelner kurzer Flug widerlegt sie nicht."),
                 ("Schlechte Würfe streichen", "Regulär kurze Flüge zählen; ungültig nur nach vorher festgelegter Regel. Deckenkontakte bleiben mit Vermerk in der Tabelle – nie still löschen oder durch 0 ersetzen."),
                 ("»Die Klammer wirkt, weil sie schwerer ist«", "Die Klammer ändert **Masse und Schwerpunkt zugleich** – der Test zeigt die Wirkung dieser einen Änderung, nicht, welche Ursache dahinter steckt. Auch »nicht prüfbar = falsch« vermeiden.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Begriffe", "»Der Flieger landete bei 6,4 m.« – Was ist das?", ["eine Beobachtung", "eine Hypothese", "eine Theorie", "ein Gesetz"],
  "Ein gemessener Wert ist eine Beobachtung. Eine Erklärung dafür ist ein weiterer Schritt.", "Buch S. 29"),
 ("Begriffe", "Was macht eine Hypothese aus?", ["Sie ist begründet und prüfbar.", "Sie ist schon bewiesen.", "Sie ist eine bloße Meinung.", "Sie gilt für alle Zeiten."],
  "Eine Hypothese ist eine begründete Vermutung – und man muss sagen können, was gegen sie sprechen würde.", "Buch S. 29"),
 ("Begriffe", "Was ist eine Vorhersage?", ["das erwartete Ergebnis eines bestimmten Tests", "eine Erklärung vieler Befunde", "ein gemessener Wert", "ein Modell"],
  "Aus der Hypothese leiten wir ab, was beim nächsten Test herauskommen sollte – das ist die Vorhersage.", "Buch S. 29"),
 ("Theorie", "Was ist eine wissenschaftliche Theorie?", ["eine Erklärung, die viele geprüfte Befunde verbindet", "eine geratene Vermutung", "ein einzelnes Messergebnis", "eine Meinung von Experten"],
  "Im Alltag heißt »Theorie« oft »Vermutung« – in der Wissenschaft ist sie gut geprüft und erlaubt Vorhersagen.", "Buch S. 29"),
 ("Theorie", "Wird eine oft bestätigte Hypothese automatisch zum Gesetz?", ["Nein – Gesetz und Theorie sind keine Stufen einer Leiter.", "Ja, nach zehn Bestätigungen.", "Ja, sobald ein Professor zustimmt.", "Nein, weil es keine Gesetze gibt."],
  "Ein Gesetz beschreibt eine Regelmäßigkeit, eine Theorie erklärt. Bestätigungen machen keine automatische Rangstufe daraus.", "Buch S. 29"),
 ("Fragen", "Welche Frage ist KEINE naturwissenschaftliche Frage?", ["Soll das Heer neue Hubschrauber kaufen?", "Rostet Eisen in Salzwasser schneller?", "Keimt Kresse im Licht schneller?", "Fliegt der Flieger mit Klammer weiter?"],
  "Ob man etwas kaufen soll, ist eine Entscheidung. Messungen liefern Fakten dazu, entscheiden aber nicht.", "Buch S. 28"),
 ("Modell", "Was gilt für jedes Modell?", ["Es vereinfacht für einen Zweck und hat Grenzen.", "Es ist eine exakte Kopie der Wirklichkeit.", "Es ist immer falsch.", "Es gilt nur in der Physik."],
  "Ein Modell zeigt manches und lässt anderes weg – darum fragen wir immer nach seinen Grenzen.", "Buch S. 29"),
 ("Fairer Test", "Was ist bei einem fairen Vergleich das Wichtigste?", ["nur eine Bedingung verändern", "möglichst viel gleichzeitig ändern", "nur den besten Wurf zählen", "die Regeln nach dem Test festlegen"],
  "Ändert man nur eine Sache, kann man ihr den Unterschied zuschreiben.", "Buch S. 29"),
 ("Fairer Test", "Ein regulärer Wurf geht nach 2 m zu Boden. Was tun?", ["Er zählt und wird eingetragen.", "Er wird gelöscht.", "Er wird durch 0 ersetzt.", "Er wird so oft wiederholt, bis er weit ist."],
  "Auch schlechte reguläre Flüge zählen. Wer sie streicht, verfälscht das Ergebnis.", "Buch S. 29"),
 ("Fairer Test", "Was macht eine Gegenprobe mit einem zweiten Werfer?", ["Sie prüft, ob das Ergebnis auch bei jemand anderem ähnlich ist.", "Sie beweist die Hypothese.", "Sie ersetzt die erste Messreihe.", "Sie zeigt, ob die Masse die Ursache ist."],
  "Die Gegenprobe prüft die Übertragbarkeit – sie trennt aber nicht Masse und Schwerpunkt.", "Buch S. 29"),
 ("Auswerten", "4,0 m, 5,0 m und 6,0 m – wie groß ist der Mittelwert?", ["5,0 m", "15,0 m", "2,0 m", "6,0 m"],
  "(4,0 + 5,0 + 6,0) m : 3 = 15,0 m : 3 = 5,0 m.", "Buch S. 29"),
 ("Auswerten", "4,0 m, 5,0 m und 6,0 m – wie groß ist die Spannweite?", ["2,0 m", "5,0 m", "15,0 m", "1,0 m"],
  "Spannweite = größter minus kleinster Wert: 6,0 m − 4,0 m = 2,0 m.", "Buch S. 29"),
 ("Popper", "Welche Aussage ist NICHT wissenschaftlich prüfbar?", ["Ein unsichtbarer Geist lenkt jeden Flieger, wenn keiner hinsieht.", "Mit größeren Flügeln fliegt er im Mittel weiter.", "Kresse keimt bei 20 °C schneller als bei 10 °C.", "Rost entsteht schneller in Salzwasser."],
  "Keine denkbare Beobachtung könnte sie widerlegen – darum ist sie nicht prüfbar. Falsch ist sie damit nicht automatisch.", "Buch S. 29–32"),
 ("Forschung", "Was bewirkt eine Begutachtung (Peer Review)?", ["Sie senkt Fehler, garantiert aber keine Wahrheit.", "Sie beweist jedes Ergebnis.", "Sie ersetzt jede Wiederholung.", "Sie ist nur eine Formalität ohne Nutzen."],
  "Fachleute prüfen Methode und Schlüsse. Vertrauen wächst erst, wenn andere das Ergebnis wiederholen.", "Buch S. 29"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
