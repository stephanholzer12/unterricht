"""NAWI 1AB · K2.1 Mechanische Kräfte (Trauner NAWI HAK 1, Teil II »Grundlagen der Physik«, Kapitel »Mechanische Kräfte«, S. 44–65) – v1.
Grundlage: Übergabepaket »26-27-1AB-K2.1-Kraefte-Claude-v1« vom 07.11.2026 (Planung, Quellenprüfung, fachliche Korrekturen) – von Claude umgesetzt und nachgeprüft.
Jahresplan: Block »E Physik«, Einheiten E15–E17 (bloecke.json: 3+3+1 = 7 Stunden). Stephans engerer Rahmen: SECHS Stunden einschließlich Gruppenprojekt und Präsentationen.
Keine festen Daten – es zählt die Reihenfolge der Stunden (Ausfälle, Tests, Veranstaltungen). Beide Klassen bekommen denselben Fahrplan.
Sieben Gruppen: 1AK 28 Kadetten = 7 Vierergruppen · 1BK 29 Kadetten = 6 Vierergruppen + 1 Fünfergruppe. Keine namentliche Einteilung auf der öffentlichen Seite.
Versuchs-ID: das bereits vorhandene Gruppenprojekt V1.20 (Stephans Vorgabe) – es werden KEINE neuen Kapitel-Versuchsnummern vergeben.
Eine Quelle für Handy-Seiten, Unterrichts-PPP und Lösungsmappe. Kein CLIL, kein Kahoot, keine Hausübung.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "11.11.2026"
V = "v2"
ORDNER = "1ab-nawi/k2-1-kraefte"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "1ab-nawi/"
EYEBROW = "NAWI · 1AB · K2.1 Mechanische Kräfte"
TITEL = "Mechanische Kräfte – messen, rechnen, erklären"
KURZTITEL = "Mechanische Kräfte"
BUCH = "Buch S. 44–65"
KEY = "26-27-1AB-K2.1-Kraefte-TH-Handy-v1"
VS_KEY = "26-27-1AB-K2.1-Kraefte-VS-Handy-v1"
LERNSEITE_KEY = "26-27-1AB-K2.1-Kraefte-Lernseite-Check-v1"
PRAEFIX = "26-27-1AB-K2.1-Kraefte"
VS_ID = "V1.20"
VS_TITEL = "Gruppenprojekt: sieben Kräfte-Untersuchungen"
KLASSEN = ["1AK", "1BK"]
GRUPPEN = 7
STUNDEN = 6
G_KERN = 10          # N/kg – Näherung für alle Rechnungen dieser Einheit
G_GENAU = 9.81       # nur im Lehrerwissen

# Keine geprüften Videos vorhanden: YouTube ist von hier aus nicht prüfbar, die Trauner-Filmliste nennt zu diesem Kapitel
# keinen von Claude geöffneten Beitrag. Deshalb bewusst kein Video eingebaut (Regelwerk 7: nur Geprüftes verlinken).
VIDEOS = {}
FREIGEGEBEN = set()


def zeigen(key, lehrer=False):
    return key in VIDEOS


# ---------------------------------------------------------------- Stunden (ohne Datum, Reihenfolge zählt)
STUNDENNAME = {1: "Stunde 1 · Was Kräfte bewirken",
               2: "Stunde 2 · Thema erarbeiten, Versuch planen",
               3: "Stunde 3 · Versuch durchführen und üben",
               4: "Stunde 4 · Steckbrief und Probe",
               5: "Stunde 5 · Alle sieben Gruppen präsentieren",
               6: "Stunde 6 · Alles verbinden und einzeln prüfen"}

# ---------------------------------------------------------------- Auswahllisten
STIMMT = ["stimmt", "stimmt nicht"]
JANEIN = ["ja", "nein"]

# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 44", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Zwei Schätzfragen zum Start – es gibt dafür keine Punkte und kein »richtig« oder »falsch«. Entscheide dich einmal. In Stunde 6 schaust du nach, was du heute gedacht hast.",
  "hint": "Einfach tippen, was du vermutest. Deine Antwort wird gespeichert und bleibt stehen.",
  "type": "multi",
  "vorhersage": True,
  "fields": [["p1", "a) Zwei Kraftmesser hängen mit den Haken ineinander. Einer zeigt ruhig 2 N. Was erwartest du am anderen?",
              ["ungefähr 2 N", "ungefähr 1 N", "ungefähr 4 N"], False],
             ["p2", "b) Ein Boot schwimmt ruhig an der Oberfläche. Was vermutest du?",
              ["Auftriebskraft und Gewichtskraft sind gleich groß", "Die Auftriebskraft ist größer", "Die Gewichtskraft ist größer"], False]],
  "chk": {},
  "aufloesung": [["p1", "ungefähr 2 N", "In Ruhe zeigen beide Kraftmesser ungefähr dieselbe übertragene Zugkraft. Die beiden Anzeigen werden nicht addiert."],
                 ["p2", "Auftriebskraft und Gewichtskraft sind gleich groß", "Ruhiges Schwimmen ist ein Kräftegleichgewicht. Nur beim Aufsteigen aus der Ruhe kann die Auftriebskraft vorher größer sein."]],
  "sol": [["Auflösung", ["a) ungefähr 2 N – in Ruhe zeigen beide Geräte dieselbe übertragene Zugkraft. Nicht addieren.",
                         "b) gleich groß – ruhiges Schwimmen ist Kräftegleichgewicht (F_A = F_G)."]]],
  "tipps": [], "tip": ["Was eine Kraft bewirkt", "theorie.html#wirkung"]},

 {"id": "a1", "nr": 2, "title": "Kraft und Bewegung unterscheiden", "src": "Buch S. 45–49", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 13,
  "q": "Fünf kurze Teilaufgaben. a) und b) zum Auswählen, c) bis e) zum Rechnen. Schreib bei den Rechnungen immer die Einheit dazu. Rechne mit g = 10 N/kg.",
  "hint": "Frag dich bei a) und b) zuerst: Ändert sich Tempo, Richtung oder Form? Für c) gilt v = s / t, für e) gilt F = m · a.",
  "type": "multi",
  "fields": [["wirkung", "a) Ein Fahrrad fährt mit unverändertem Tempo durch eine Kurve. Was ändert sich?",
              ["die Richtung seiner Geschwindigkeit", "seine Masse", "keine Bewegungsgröße"]],
             ["verformung", "b) Ein weicher Ball wird zwischen zwei Händen zusammengedrückt. Woran erkennt man die Kraftwirkung?",
              ["an der Verformung", "an einer Änderung der Einheit", "nur an einer Ortsänderung"]],
             ["tempo", "c) Für einen geraden Weg von 5 m werden 4 s gebraucht. Berechne die mittlere Schnelligkeit in m/s (mit Einheit)."],
             ["umrechnen", "d) Wandle dein Ergebnis aus c) in km/h um (mit Einheit)."],
             ["kraft", "e) Eine Masse von 2 kg wird durch eine resultierende Kraft mit 3 m/s² beschleunigt. Wie groß ist die resultierende Kraft? (mit Einheit)"]],
  "chk": {"wirkung": {"sel": "die Richtung seiner Geschwindigkeit"},
          "verformung": {"sel": "an der Verformung"},
          "tempo": {"num": 1.25, "unit": "m/s", "tol": 0.03},
          "umrechnen": {"num": 4.5, "unit": "km/h", "tol": 0.1},
          "kraft": {"num": 6, "unit": "N", "tol": 0.15}},
  "fb": {"wirkung": {"seine Masse": "Die Masse ändert sich durch eine Kurve nicht.",
                     "keine Bewegungsgröße": "Vergleiche die Fahrtrichtung vor und nach der Kurve."},
         "verformung": {"an einer Änderung der Einheit": "Eine Einheit beschreibt eine Größe. Sie wird nicht durch Drücken verändert.",
                        "nur an einer Ortsänderung": "Eine Kraftwirkung braucht keine sichtbare Ortsänderung."}},
  "sol": [["Lösung", ["a) die Richtung seiner Geschwindigkeit – zur Geschwindigkeit gehört auch die Richtung.",
                      "b) an der Verformung – die Formänderung zeigt die Kraftwirkung.",
                      "c) v = s / t = 5 m : 4 s = 1,25 m/s.",
                      "d) 1,25 m/s · 3,6 = 4,5 km/h.",
                      "e) F = m · a = 2 kg · 3 m/s² = 6 N (1 N = 1 kg · m/s²)."]]],
  "tipps": ["Prüf zuerst, was sich ändert: das Tempo, die Richtung oder die Form. Erst danach rechnen.",
            "k1",
            "Lies im Buch S. 45 den Abschnitt »Der Begriff Kraft« und auf S. 46–47 »Die Geschwindigkeit«. Die Formel F = m · a steht auf S. 49."],
  "tip": ["Was eine Kraft bewirkt", "theorie.html#wirkung"]},

 # --------------------------------------------------------------- Stunden 2–5: Gruppenprojekt (v2: Versuch frei wählen, Steckbrief, Mitschrift)
 {"id": "p1", "nr": 3, "title": "Euer Thema selbst erarbeiten", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 15, "projekt": True,
  "marke": "SELBSTSTUDIUM",
  "q": "Wähle zuerst deine Gruppe. Dann erscheint deine Gruppenkarte mit Buchseiten, Theorie-Teil und vier Leitfragen. "
       "Lies die Buchseiten und den Theorie-Teil und beantworte die Leitfragen in eigenen Worten – jeder für sich, besprechen dürft ihr euch. "
       "Zum Schluss sucht ihr ein kurzes Video oder eine zweite Quelle und prüft sie.",
  "hint": "Kurze Sätze genügen. Nicht abschreiben – wer es in eigenen Worten sagen kann, kann es auch präsentieren.",
  "type": "multi",
  "fields": [["grp", "a) Meine Gruppe", ["Gruppe 1 · Bewegung", "Gruppe 2 · Gewichtskraft", "Gruppe 3 · Auftrieb", "Gruppe 4 · Reibung",
                                         "Gruppe 5 · Kapillarwirkung", "Gruppe 6 · Druck", "Gruppe 7 · Kraft und Gegenkraft"], False],
             ["rolle", "b) Meine Rolle", ["Leitung und Zeit", "Quellen und Video", "Versuch und Material", "Schriftführung (Steckbrief, Teams)", "Präsentation und Probe"], False],
             ["lf1", "c) Leitfrage 1 (siehe Gruppenkarte)"],
             ["lf2", "d) Leitfrage 2 (siehe Gruppenkarte)"],
             ["lf3", "e) Leitfrage 3 (siehe Gruppenkarte)"],
             ["lf4", "f) Leitfrage 4 (siehe Gruppenkarte)"],
             ["video", "g) Video oder zweite Quelle: Titel, wer hat es gemacht, wie lang, warum passt es?"]],
  "chk": {},
  "sol": [["Bewertung", ["Antworten zu den Leitfragen je Gruppe: siehe Reiter »Aufgaben« (Gruppenkarten) in der Lösungsmappe.",
                         "Teil des Projekt-Rasters »Inhalt« (3 Punkte). Bewertet Prof. HOLZER."]]],
  "tipps": [], "tip": ["Euer Gruppenprojekt", "theorie.html#projekt"]},

 {"id": "p2", "nr": 4, "title": "Euren Versuch auswählen und planen", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 10, "projekt": True,
  "marke": "GRUPPENARBEIT",
  "q": "Sucht euch einen Versuch zu eurem Thema aus – eine der Ideen auf eurer Gruppenkarte oder eine eigene. Material darf aus dem NAWI-Saal "
       "oder von zu Hause kommen. Schreibt die Materialliste genau auf. Bis zum Ende dieser Stunde zeigt ihr den Plan Prof. HOLZER – ohne Freigabe kein Versuch.",
  "hint": "Ändert nur EINE Sache, alles andere bleibt gleich. Von zu Hause nur Dinge von der Liste »erlaubt«. Wer etwas mitbringt, steht in der Liste.",
  "type": "multi",
  "fields": [["idee", "a) Unser Versuch in zwei Sätzen"],
             ["frage", "b) Was soll man sehen oder messen?"],
             ["aendern", "c) Was ändern wir – und was bleibt gleich?"],
             ["mat", "d) Materialliste: was, wie viel, »Saal« oder »von zu Hause«, wer bringt es mit"],
             ["sicher", "e) Sicherheits-Check", ["Alles steht auf der Liste »erlaubt«", "Etwas ist unklar – wir fragen Prof. HOLZER"], False],
             ["frei", "f) Freigabe", ["Prof. HOLZER hat unseren Plan freigegeben", "noch nicht freigegeben"], False]],
  "chk": {},
  "sol": [["Bewertung", ["Freigabe nach den fünf Fragen auf der Folie »Freigabe«. Teil des Rasters »Versuch« (2 Punkte).",
                         "Die Materiallisten aller Gruppen sind die Grundlage für deine Vorbereitung von Stunde 3 (Reiter »Vorbereitung«)."]]],
  "tipps": [], "tip": ["Euer Gruppenprojekt", "theorie.html#projekt"]},

 {"id": "p3", "nr": 5, "title": "Versuch durchführen und festhalten", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 30, "projekt": True,
  "marke": "VERSUCH",
  "q": "Baut euren Versuch auf, macht ihn und übt ihn gleich so, wie ihr ihn in Stunde 5 zeigen wollt. Jeder trägt die Ergebnisse seiner Gruppe "
       "in sein eigenes Arbeitsblatt ein – abschreiben vom Gruppenzettel ist erlaubt. Macht ein Foto vom Aufbau oder von einer Skizze.",
  "hint": "Schreibt nur auf, was ihr wirklich gesehen oder gemessen habt. Erst Beobachtung, dann Erklärung.",
  "type": "sketch",
  "fotolabel": "Foto vom Aufbau oder von eurer Skizze",
  "fields": [["gemacht", "a) Was haben wir gemacht? (drei kurze Schritte)"],
             ["beob", "b) Beobachtung oder Messwerte mit Einheit"],
             ["erkl", "c) Erklärung mit Fachbegriffen: Warum ist das so?"],
             ["grenze", "d) Was zeigt unser Versuch NICHT? (eine Grenze)"]],
  "chk": {},
  "sol": [["Bewertung", ["Teil des Rasters »Versuch« (2 Punkte): passt zum Thema, sicher durchgeführt, Beobachtung und Erklärung getrennt, Grenze genannt."]]],
  "tipps": [], "tip": ["Euer Gruppenprojekt", "theorie.html#projekt"]},

 {"id": "p4", "nr": 6, "title": "Steckbrief für die Klasse", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 17, "projekt": True,
  "marke": "GRUPPENARBEIT",
  "q": "Euer Steckbrief ist das Handout für alle anderen. Schreibt ihn gemeinsam und tragt ihn jeder in sein Arbeitsblatt ein. "
       "Die Schriftführung tippt danach auf »Handout-PDF erstellen« und stellt das PDF bis zum Ende dieser Stunde in Teams. "
       "Eine Partnergruppe liest ihn und sagt euch, was noch unklar ist.",
  "hint": "Kurz und richtig. Die anderen lernen damit für den Test – schreibt so, dass sie es ohne euch verstehen.",
  "type": "multi",
  "steckbrief": True,
  "fields": [["mitglieder", "Namen in unserer Gruppe"]] + [[k, lab] for k, lab in [
              ["kern", "a) Das Wichtigste in drei Sätzen"],
              ["begriffe", "b) Drei bis fünf Fachbegriffe mit Bedeutung"],
              ["formel", "c) Formel mit Einheiten (oder »keine Formel«)"],
              ["versuch", "d) Unser Versuch in zwei Sätzen: Was haben wir gemacht, was sieht man?"],
              ["alltag", "e) Ein Beispiel aus Sport, Bundesheer oder Alltag"],
              ["kfrage", "f) Eine Kontrollfrage für die Klasse – mit Antwort"],
              ["quelle", "g) Unsere Quellen: Buchseite und eine zweite Quelle (Wer? Datum?)"]]],
  "chk": {},
  "sol": [["Bewertung", ["Raster »Steckbrief« (2 Punkte): vollständig, fachlich richtig, verständlich. Muster je Thema: Reiter »Aufgaben« der Lösungsmappe.",
                         "Prüfe vor Stunde 5 kurz die Steckbriefe in Teams. Ein fachlicher Fehler wird in Stunde 5 bei »Das besprechen wir« geklärt."]]],
  "tipps": [], "tip": ["Euer Gruppenprojekt", "theorie.html#projekt"]},

 {"id": "p5", "nr": 7, "title": "Mitschrift bei den Präsentationen", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 5", "h": 5, "zeit": 3, "projekt": True,
  "marke": "SELBSTSTUDIUM",
  "q": "Während die Gruppen präsentieren, schreibst du mit: zu jeder Gruppe die Kernaussage in einem Satz und eine Formel oder ein Beispiel. "
       "Stichwörter genügen. Am Ende hast du drei Minuten zum Ergänzen – dazu hilft dir der Steckbrief der Gruppe in Teams.",
  "hint": "Handy liegt während der Präsentationen auf dem Tisch. Du darfst auch auf Papier mitschreiben und später abtippen.",
  "type": "multi",
  "fields": [["m%d" % n, "Gruppe %d · %s" % (n, t)] for n, t in [(1, "Bewegung"), (2, "Gewichtskraft"), (3, "Auftrieb"), (4, "Reibung"),
                                                                  (5, "Kapillarwirkung"), (6, "Druck"), (7, "Kraft und Gegenkraft")]],
  "chk": {},
  "sol": [["Bewertung", ["Die Mitschrift ist die Grundlage für Aufgabe 8 in Stunde 6. Kernaussagen je Thema: Reiter »Aufgaben« der Lösungsmappe."]]],
  "tipps": [], "tip": ["Das Wichtigste in 5 Sätzen", "theorie.html#kurz"]},

 # --------------------------------------------------------------- Stunde 6
 {"id": "a3", "nr": 8, "title": "Alle Themen selbst erklären", "src": "Buch S. 45–61", "own": True, "tag": "Stunde 6", "h": 6, "zeit": 16,
  "q": "Zehn kurze Teilaufgaben über alle sieben Gruppenthemen. Allein und ohne KI. Rechne mit g = 10 N/kg und schreib bei Rechnungen die Einheit dazu.",
  "hint": "Markiere in jeder Frage, welche Größe oder welche beiden Körper gemeint sind. Dann wird die Antwort leichter.",
  "type": "multi",
  "fields": [["rucksack", "a) Ein Rucksack hat 6 kg Masse. Berechne seine Gewichtskraft mit g = 10 N/kg (mit Einheit)."],
             ["schwimmen", "b) Ein Boot schwimmt ruhig an der Oberfläche. Wie sind die beiden senkrechten Kräfte im einfachen Modell?",
              ["Auftriebskraft und Gewichtskraft sind gleich groß", "Die Auftriebskraft ist größer", "Die Gewichtskraft ist größer"]],
             ["haftung", "c) Was ermöglicht das Abstoßen beim normalen Gehen?",
              ["die Haftreibung zwischen Schuh und Boden", "möglichst gar keine Wechselwirkung mit dem Boden", "eine immer nach hinten gerichtete Kraft des Bodens auf den Fuß"]],
             ["papier", "d) In Filterpapier steigt der feuchte Rand über den Wasserspiegel. Welche Erklärung passt?",
              ["Wasser breitet sich in feinen benetzbaren Zwischenräumen aus", "Das Papier bildet elektrische Energie", "Wasser wird schwerelos"]],
             ["druck", "e) Eine senkrechte Kraft von 120 N verteilt sich gleichmäßig auf 0,02 m². Berechne den mittleren Druck (mit Einheit)."],
             ["gegenkraft", "f) Die Erde zieht einen Ball nach unten. Was ist die Gegenkraft derselben Wechselwirkung?",
              ["Der Ball zieht die Erde an", "Die Luft bremst den Ball", "Eine Tischplatte drückt irgendeinen Gegenstand hoch"]],
             ["gleichgewicht", "g) Ein Körper bewegt sich gerade und mit gleichbleibender Geschwindigkeit. Welche Aussage kann stimmen?",
              ["Mehrere Kräfte auf ihn gleichen sich aus", "Auf ihn muss zwingend genau eine Kraft wirken", "Seine Geschwindigkeit muss jede Sekunde größer werden"]],
             ["beschleunigung", "h) Ein Fahrzeug hält sein Tempo, ändert aber die Fahrtrichtung. Ist es physikalisch beschleunigt?",
              ["ja, weil sich die Richtung der Geschwindigkeit ändert", "nein, weil nur schneller werden zählt", "nur, wenn seine Masse zunimmt"]],
             ["wegzeit", "i) Ein Körper legt geradeaus 9 m in 6 s zurück. Berechne die mittlere Schnelligkeit (mit Einheit)."],
             ["newton", "j) Auf 3 kg Masse wirkt eine resultierende Kraft von 12 N. Berechne die Beschleunigung (mit Einheit)."]],
  "chk": {"rucksack": {"num": 60, "unit": "N", "tol": 1},
          "schwimmen": {"sel": "Auftriebskraft und Gewichtskraft sind gleich groß"},
          "haftung": {"sel": "die Haftreibung zwischen Schuh und Boden"},
          "papier": {"sel": "Wasser breitet sich in feinen benetzbaren Zwischenräumen aus"},
          "druck": {"num": 6000, "unit": "Pa", "tol": 60},
          "gegenkraft": {"sel": "Der Ball zieht die Erde an"},
          "gleichgewicht": {"sel": "Mehrere Kräfte auf ihn gleichen sich aus"},
          "beschleunigung": {"sel": "ja, weil sich die Richtung der Geschwindigkeit ändert"},
          "wegzeit": {"num": 1.5, "unit": "m/s", "tol": 0.03},
          "newton": {"num": 4, "unit": "m/s²", "tol": 0.1}},
  "fb": {"schwimmen": {"Die Auftriebskraft ist größer": "Dann würde der zunächst ruhende Körper nach oben beschleunigt, solange kein anderer Widerstand ausgleicht.",
                       "Die Gewichtskraft ist größer": "Dann würde der zunächst ruhende Körper nach unten beschleunigt, solange kein anderer Widerstand ausgleicht."},
         "haftung": {"möglichst gar keine Wechselwirkung mit dem Boden": "Ohne Kontaktkraft kannst du dich nicht auf diese Weise abstoßen.",
                     "eine immer nach hinten gerichtete Kraft des Bodens auf den Fuß": "Unterscheide: Fuß auf Boden und Boden auf Fuß."},
         "papier": {"Das Papier bildet elektrische Energie": "Hier wird keine elektrische Energie erzeugt.",
                    "Wasser wird schwerelos": "Die Gewichtskraft wirkt weiterhin."},
         "gegenkraft": {"Die Luft bremst den Ball": "Der Luftwiderstand ist eine andere Wechselwirkung.",
                        "Eine Tischplatte drückt irgendeinen Gegenstand hoch": "Für das Kraftpaar müssen dieselben zwei Körper betrachtet werden."},
         "gleichgewicht": {"Auf ihn muss zwingend genau eine Kraft wirken": "Eine einzelne nicht ausgeglichene Kraft würde seine Geschwindigkeit ändern.",
                           "Seine Geschwindigkeit muss jede Sekunde größer werden": "Die Bewegung wurde als gleichförmig beschrieben."},
         "beschleunigung": {"nein, weil nur schneller werden zählt": "Die physikalische Bedeutung ist weiter als die Alltagssprache.",
                            "nur, wenn seine Masse zunimmt": "Die Masse entscheidet nicht darüber, ob die Geschwindigkeit gerade geändert wird."}},
  "sol": [["Lösung", ["a) F_G = m · g = 6 kg · 10 N/kg = 60 N.",
                      "b) gleich groß – ruhiges Schwimmen ist Kräftegleichgewicht.",
                      "c) die Haftreibung – der Boden wirkt beim Abstoßen nach vorne auf den Fuß.",
                      "d) Wasser breitet sich in feinen benetzbaren Zwischenräumen aus – das ist Kapillarwirkung im porösen Papier.",
                      "e) p = F / A = 120 N : 0,02 m² = 6000 Pa.",
                      "f) Der Ball zieht die Erde an – es wirken Erde auf Ball und Ball auf Erde.",
                      "g) Mehrere Kräfte gleichen sich aus – eine gleichbleibende Geschwindigkeit verlangt keine resultierende Kraft.",
                      "h) ja – auch eine Richtungsänderung ist Beschleunigung.",
                      "i) v = 9 m : 6 s = 1,5 m/s.",
                      "j) a = F / m = 12 N : 3 kg = 4 m/s²."]]],
  "tipps": ["Unterstreiche in der Frage zuerst die gesuchte Größe und bei f) die beiden beteiligten Körper.",
            "k9",
            "Lies im Buch nach: Gewichtskraft S. 50–51 · Auftrieb S. 52–53 · Reibung S. 54–56 · Kapillarkraft S. 57 · Druck S. 58–60 · Kraft und Gegenkraft S. 61."],
  "tip": ["Kraft und Gegenkraft", "theorie.html#gegenkraft"]},

 # --------------------------------------------------------------- Zusatz · Für Schnelle und Neugierige
 {"id": "z1", "nr": 9, "title": "Drei Behauptungen prüfen", "src": "Buch S. 52–61", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Entscheide bei jeder Behauptung, ob sie stimmt. d) Begründe die Behauptung, die dir am schwersten gefallen ist, in einem Satz.",
  "hint": "Achte bei c) darauf, auf welchen Körper die beiden Kräfte wirken.",
  "type": "multi",
  "fields": [["b1", "a) Reibung bremst immer die Bewegung eines Körpers relativ zum Boden.", STIMMT, False],
             ["b2", "b) Bei ruhigem Schwimmen ist die Auftriebskraft größer als die Gewichtskraft.", STIMMT, False],
             ["b3", "c) Stützkraft und Gewichtskraft auf ein Buch sind ein Kraft-Gegenkraft-Paar.", STIMMT, False],
             ["begr", "d) Deine Begründung (1 Satz)"]],
  "chk": {"b1": {"sel": "stimmt nicht"}, "b2": {"sel": "stimmt nicht"}, "b3": {"sel": "stimmt nicht"},
          "begr": {"kw": [["Begründung", r"haft|vorne|gehen|gleichgewicht|gleich gross|gleich groß|gleich|verschieden|zwei koerper|zwei körper|selben koerper|selben körper|buch|boden"]], "man": True}},
  "fb": {"b1": {"stimmt": "Haftreibung kann beim Gehen nach vorne auf den Körper wirken – sie treibt dann an."},
         "b2": {"stimmt": "Im ruhigen Gleichgewicht sind beide Kräfte gleich groß."},
         "b3": {"stimmt": "Beide wirken auf dasselbe Buch. Ein Wechselwirkungspaar wirkt auf verschiedene Körper."}},
  "sol": [["Lösung", ["a) stimmt nicht – Haftreibung kann beim Gehen nach vorne auf den Körper wirken. Reibung wirkt gegen das relative Gleiten an der Kontaktstelle.",
                      "b) stimmt nicht – im ruhigen Gleichgewicht sind Auftriebskraft und Gewichtskraft gleich groß.",
                      "c) stimmt nicht – beide wirken auf das Buch. Die Gegenkraft zur Gewichtskraft auf das Buch ist die Anziehung des Buches auf die Erde."]]],
  "tipps": ["Zeichne bei c) einen Rahmen um »das Buch« und schau, welche Kräfte innerhalb dieses Rahmens angreifen.",
            "k8",
            "Lies im Buch S. 61 den Abschnitt »Kraft und Gegenkraft« und auf S. 54 den Beginn von »Die Reibungskraft«."],
  "tip": ["Kraft und Gegenkraft", "theorie.html#gegenkraft"]},

 {"id": "z2", "nr": 10, "title": "Druck vergleichen", "src": "Buch S. 58", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Modellrechnung: Eine senkrechte Kraft von 600 N verteilt sich zuerst auf 0,03 m², dann auf 0,30 m². a) Berechne den ersten mittleren Druck. b) Berechne den zweiten. "
       "c) Um welchen Faktor ändert sich der Druck? d) Was heißt das für Schneeschuhe?",
  "hint": "p = F / A. Für c) teile den größeren Druck durch den kleineren.",
  "type": "multi",
  "fields": [["p1", "a) Druck bei 0,03 m² (mit Einheit)"], ["p2", "b) Druck bei 0,30 m² (mit Einheit)"],
             ["faktor", "c) Der zweite Druck ist …", ["zehnmal kleiner", "zehnmal größer", "gleich groß"]],
             ["schnee", "d) Bedeutung für Schneeschuhe (1 Satz)"]],
  "chk": {"p1": {"num": 20000, "unit": "Pa", "tol": 200}, "p2": {"num": 2000, "unit": "Pa", "tol": 20},
          "faktor": {"sel": "zehnmal kleiner"},
          "schnee": {"kw": [["größere Fläche", r"groessere flaeche|größere fläche|mehr flaeche|mehr fläche|flaeche|fläche|verteil"],
                            ["kleinerer Druck / sinkt nicht ein", r"kleiner|geringer|weniger|nicht ein|sinkt nicht|einsink"]], "need": 2, "man": True}},
  "sol": [["Lösung", ["a) p = 600 N : 0,03 m² = 20 000 Pa.",
                      "b) p = 600 N : 0,30 m² = 2 000 Pa.",
                      "c) zehnmal kleiner – die Fläche ist zehnmal größer, die Kraft bleibt gleich.",
                      "d) Schneeschuhe verteilen dieselbe Gewichtskraft auf eine größere Fläche. Der mittlere Druck wird kleiner, deshalb sinkt man weniger ein."]]],
  "tipps": ["Die Kraft bleibt gleich. Nur die Fläche ändert sich – vergleiche also die beiden Flächen.",
            "k7",
            "Lies im Buch S. 58 den Abschnitt »Druck« mit dem Beispiel der Schneeschuhe."],
  "tip": ["Druck: Kraft auf eine Fläche", "theorie.html#druck"]},

 {"id": "z3", "nr": 11, "title": "Forschung prüfen: Schmieren mit einem Pulver?", "src": "Recherche im Internet", "own": False, "tag": "Zusatz", "h": 0, "zeit": 10,
  "q": "Lies die Pressemitteilung der TU Wien vom 18.02.2025 »Extrem geringe Reibung durch neues pulverförmiges Schmiermittel« "
       "(tuwien.at → Aktuelles → Presseaussendungen). a) Wer berichtet? b) Worin besteht die Idee des Schmiermittels? "
       "c) Was ist in dem Beitrag NICHT für beliebige Maschinen nachgewiesen? d) Ist eine Pressemitteilung über die eigene Forschung eine unabhängige Quelle?",
  "hint": "Achte auf den Aussender und darauf, wer die Forschung gemacht hat. Die verlinkte Originalarbeit ist Li et al., Advanced Science 2025.",
  "type": "multi",
  "fields": [["wer", "a) Wer berichtet? (Einrichtung und Aussender)"],
             ["idee", "b) Idee des Schmiermittels (1 Satz)"],
             ["nicht", "c) Was ist nicht nachgewiesen? (1 Satz)"],
             ["unab", "d) Ist das eine unabhängige Quelle?", JANEIN, False]],
  "chk": {"wer": {"kw": [["TU Wien", r"tu wien|technische universitaet wien|technische universität wien|aigner"]], "man": True},
          "idee": {"kw": [["fester Stoff schmiert", r"pulver|feststoff|fester stoff|schicht|film|gleit|trocken"]], "man": True},
          "nicht": {"kw": [["kein Ersatz für jede Maschine", r"nicht jede|beliebig|alle maschinen|jeder maschine|universell|ueberall|überall|nicht bewiesen|nicht nachgewiesen|nicht gezeigt"]], "man": True},
          "unab": {"sel": "nein"}},
  "fb": {"unab": {"ja": "Die TU Wien berichtet über ihre eigene Forschung. Das ist ein Eigenbericht und keine unabhängige Bestätigung."}},
  "sol": [["Lösung", ["a) Die TU Wien berichtet über eigene Forschung; Aussender ist Florian Aigner, Forschungsteams Gachot und Eder.",
                      "b) Ein geschichteter fester Stoff kann unter den untersuchten Bedingungen einen gleitenden Film bilden und so die Reibung stark senken.",
                      "c) Nicht nachgewiesen ist ein Ersatz aller Schmiermittel in jeder Maschine. Gezeigt wurde es nur unter den untersuchten Bedingungen.",
                      "d) nein – eine Einrichtung, die über ihre eigene Forschung berichtet, ist keine unabhängige Quelle. Die Originalarbeit (Li et al., Advanced Science 2025, DOI 10.1002/advs.202415268) ist der Nachweis, nicht die Bestätigung."]]],
  "tipps": ["Suche im Beitrag zuerst das Datum und den Namen des Aussenders. Beides steht oben bzw. am Ende.",
            "k5",
            "Lies im Buch S. 54–56 den Abschnitt »Die Reibungskraft«, damit du die Begriffe Haftreibung und Gleitreibung sicher verwendest."],
  "tip": ["Reibung hilft und bremst", "theorie.html#reibung"]},
]

# ---------------------------------------------------------------- Kontrollen
assert [t["nr"] for t in T] == list(range(1, 12))
PFLICHT = [t["nr"] for t in T if t["tag"] != "Zusatz" and not t.get("vorhersage")]
assert PFLICHT == [2, 3, 4, 5, 6, 7, 8], PFLICHT
BESPRECHEN = [2, 8]
for _t in T:
    if _t["nr"] in BESPRECHEN: _t["besprechen"] = True
for _t in T:
    for _k in (_t["chk"] or {}):
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
            if len(_f) < 4: assert _f[2][0] == _t["chk"][_f[0]]["sel"], (_t["id"], _f[0], "richtige Antwort nicht an 1. Stelle")
    for _k, _m in _t.get("fb", {}).items():
        _opt = [f[2] for f in _t["fields"] if f[0] == _k][0]
        for _o in _m: assert _o in _opt, (_t["id"], _k, _o)
        assert _t["chk"][_k].get("sel") not in _m, (_t["id"], _k, "Rückmeldung für die richtige Antwort")
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")
    assert len(_t.get("tipps", [])) in (0, 3), (_t["id"], "Tipp-Stufen: genau drei oder keine")

# Rechenkontrolle (vom Aufgabentext aus gerechnet)
assert abs(5 / 4 - 1.25) < 1e-9 and abs(1.25 * 3.6 - 4.5) < 1e-9 and abs(2 * 3 - 6) < 1e-9
assert abs(6 * G_KERN - 60) < 1e-9 and abs(120 / 0.02 - 6000) < 1e-9 and abs(9 / 6 - 1.5) < 1e-9 and abs(12 / 3 - 4) < 1e-9
assert abs(600 / 0.03 - 20000) < 1e-9 and abs(600 / 0.30 - 2000) < 1e-9 and abs((600 / 0.03) / (600 / 0.30) - 10) < 1e-9

GRP = {1: STUNDENNAME[1] + " (Buch S. 44–49) · mit der ganzen Klasse",
       2: STUNDENNAME[2] + " · Gruppenprojekt " + VS_ID,
       3: STUNDENNAME[3] + " · Gruppenprojekt " + VS_ID,
       4: STUNDENNAME[4] + " · Gruppenprojekt " + VS_ID,
       5: STUNDENNAME[5] + " · Gruppenprojekt " + VS_ID,
       6: STUNDENNAME[6] + " (Buch S. 45–61) · allein und ohne KI",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)"}

LERNZIELE = ["**Kraftwirkungen** erkennen und mit einfachen **Kräftebildern** beschreiben",
             "**Masse, Gewichtskraft, Geschwindigkeit, Beschleunigung und Druck** unterscheiden und die passenden **Einheiten** verwenden",
             "eine einfache **Untersuchung** planen, messen, erklären – und ihre **Grenzen** nennen",
             "die Kernaussage **aller sieben Gruppenthemen** auf Alltag, Sport und Sicherheit übertragen"]

WICHTIGSTE = ["Eine **resultierende Kraft** ändert das Tempo oder die Richtung einer Bewegung; Kräfte können einen Körper auch **verformen**.",
              "**Masse** wird in kg angegeben, **Kraft** in N. Für die Gewichtskraft gilt **F_G = m · g** – in dieser Einheit rechnen wir mit g = 10 N/kg.",
              "Ein ruhig schwimmender Körper hat **gleich große** Auftriebs- und Gewichtskraft.",
              "**Haftreibung** ermöglicht Fortbewegung, **Kapillarwirkung** verteilt Wasser in engen benetzbaren Räumen, **Druck** verbindet Kraft und Fläche (p = F / A).",
              "Ein **Wechselwirkungspaar** wirkt auf **verschiedene** Körper – deshalb ist es etwas anderes als ein **Kräftegleichgewicht** an einem Körper."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Kraft", "Einwirkung zwischen Körpern; erkennbar an einer Bewegungsänderung oder an einer Verformung. Einheit: Newton (N)"],
                ["Newton (N)", "Einheit der Kraft; 1 N = 1 kg · m/s²"],
                ["resultierende Kraft", "gemeinsame Wirkung aller Kräfte auf den betrachteten Körper (Vektorsumme). Nur sie ändert die Bewegung"],
                ["Kräftebild", "Zeichnung mit Kraftpfeilen an einem Körper: Angriffspunkt, Richtung, Betrag (Pfeillänge mit Maßstab)"],
                ["Geschwindigkeit", "Größe mit Betrag und Richtung; mittlerer Betrag auf gerader Strecke: v = s / t"],
                ["Beschleunigung", "Änderung der Geschwindigkeit pro Zeit; auch eine Richtungsänderung ist eine Beschleunigung. Einheit: m/s²"],
                ["Masse m", "Eigenschaft eines Körpers, angegeben in Kilogramm (kg); bleibt am Mond gleich"],
                ["Gewichtskraft F_G", "Gravitationskraft auf einen Körper am jeweiligen Ort: F_G = m · g"],
                ["Ortsfaktor g", "Gewichtskraft pro Kilogramm, Einheit N/kg; auf der Erde ungefähr 9,81 N/kg, in dieser Einheit gerundet 10 N/kg"],
                ["Auftriebskraft F_A", "nach oben gerichtete resultierende Druckkraft eines Fluids; so groß wie die Gewichtskraft des verdrängten Fluids"],
                ["Fluid", "Flüssigkeit oder Gas"],
                ["Verdrängung", "Der eingetauchte Körper nimmt Raum ein, den sonst das Fluid einnehmen würde"],
                ["Haftreibung", "Kontaktkraft, die eine beginnende Relativbewegung verhindert; sie passt sich bis zu einem Höchstwert an"],
                ["Gleitreibung", "Kontaktkraft bei zwei gegeneinander gleitenden Oberflächen"],
                ["Normalkraft F_N", "Kraft senkrecht auf die Kontaktfläche; auf waagrechter Unterlage ohne weitere senkrechte Kraft gleich groß wie die Gewichtskraft"],
                ["Adhäsion", "Anziehung an der Grenzfläche zwischen verschiedenen Stoffen"],
                ["Kohäsion", "Zusammenhalt innerhalb eines Stoffes"],
                ["Kapillarwirkung", "Steigen oder Sinken einer Flüssigkeit in engen Räumen durch Grenzflächeneffekte"],
                ["Oberflächenspannung", "Tendenz einer Flüssigkeitsoberfläche, ihre Fläche zu verkleinern"],
                ["Druck p", "senkrechte Kraft pro Fläche: p = F_N / A. Einheit: Pascal (Pa); 1 Pa = 1 N/m², 1 bar = 100 000 Pa"],
                ["hydrostatisch", "eine ruhende Flüssigkeit betreffend; der Überdruck steigt mit der Tiefe"],
                ["Wechselwirkung", "gegenseitiges Einwirken zweier Körper"],
                ["Gegenkraft", "gleich große, entgegengesetzte Kraft der anderen Seite derselben Wechselwirkung – sie wirkt auf den anderen Körper"],
                ["Kräftegleichgewicht", "die Vektorsumme aller Kräfte auf einen Körper ist null; der Körper ruht oder bewegt sich gleichförmig gerade"]]

# ---------------------------------------------------------------- Wiederholen (aus der tatsächlich gelesenen Einheit K1.4)
WIEDERHOLEN = [("Was macht eine naturwissenschaftliche Hypothese aus?", "Sie ist begründet und prüfbar.", "Quiz K1.4 Erkenntnis, Thema Begriffe"),
               ("Ein gemessener Wert: Beobachtung oder Erklärung?", "Beobachtung.", "Quiz K1.4, Beispiel gemessene Flugweite"),
               ("Warum ändern wir in einem Vergleichsversuch möglichst nur eine Bedingung?",
                "Sonst bleibt unklar, welche Änderung den Unterschied verursacht hat.", "K1.4, Vergleich ohne/mit Büroklammer")]

WEISST_DU_NOCH = {
    2: [("In welcher Gruppe bist du, und welches Thema habt ihr?", "Steht in der Einteilung aus Stunde 1 – Prof. HOLZER zeigt sie noch einmal."),
        ("Woran erkennt man eine Kraftwirkung?", "An einer Änderung von Tempo oder Richtung – oder an einer Verformung.")],
    3: [("Was muss in eurem Versuch gleich bleiben?", "Alles außer der einen Sache, die ihr absichtlich ändert."),
        ("Habt ihr alles Material von zu Hause dabei?", "Wenn nicht: sofort Prof. HOLZER sagen – dann nehmt ihr die Saal-Variante eurer Idee.")],
    4: [("Beobachtung oder Erklärung: »Die Anzeige stieg von 1,0 N auf 2,0 N.«", "Beobachtung – ein gemessener Wert."),
        ("Für wen schreibt ihr den Steckbrief?", "Für die ganze Klasse. Die anderen lernen damit euer Thema für den Test.")],
    5: [("Wie lange hat eure Gruppe für die Präsentation?", "Höchstens drei Minuten einschließlich Versuch. Jeder spricht."),
        ("Was schreibst du bei den anderen Gruppen mit?", "Die Kernaussage in einem Satz und eine Formel oder ein Beispiel.")],
    6: [("Ist Geschwindigkeit eine Kraftart?", "Nein. Geschwindigkeit, Beschleunigung und Druck sind keine Kraftarten."),
        ("Welche Einheit hat die Kraft, welche die Masse?", "Kraft in Newton (N), Masse in Kilogramm (kg).")],
}

STOPPFRAGEN = {
    1: [("»Der Körper bewegt sich, also wirkt eine Kraft.« Was ist daran ungenau?",
         "Für eine unveränderte geradlinige Geschwindigkeit braucht es keine resultierende Kraft. Es können mehrere Kräfte wirken, die sich ausgleichen."),
        ("Ein Auto fährt mit gleichem Tempo durch eine Kurve. Ist es beschleunigt?", "Ja – die Richtung der Geschwindigkeit ändert sich.")],
    2: [("6 kg Masse, g = 10 N/kg. Wie groß ist die Gewichtskraft?", "F_G = 6 kg · 10 N/kg = 60 N."),
        ("Was bleibt am Mond gleich: Masse oder Gewichtskraft?", "Die Masse. Die Gewichtskraft ist kleiner, weil der Ortsfaktor kleiner ist.")],
    3: [("Ein Boot schwimmt ruhig. Wie groß ist die Auftriebskraft?", "Genauso groß wie die Gewichtskraft des Bootes."),
        ("Erfährt ein sinkender Stein Auftrieb?", "Ja – er verdrängt Wasser. Seine Gewichtskraft ist nur größer als die Auftriebskraft.")],
    4: [("Wann ist eine Zugkraftmessung als Gleitreibungsmessung gut auswertbar?", "Beim gleichförmigen waagrechten Ziehen – dann gleichen sich Zugkraft und Gleitreibung annähernd aus."),
        ("Kann Reibung antreiben?", "Ja – die Haftreibung drückt beim Abstoßen den Fuß nach vorne.")],
    5: [("120 N auf 0,02 m². Wie groß ist der mittlere Druck?", "p = 120 N : 0,02 m² = 6000 Pa."),
        ("Ist Druck eine zusätzliche Kraftart?", "Nein. Druck verbindet eine Kraft mit der Fläche, auf die sie wirkt.")],
    6: [("Buch auf dem Tisch: Sind Gewichtskraft und Stützkraft ein Wechselwirkungspaar?",
         "Nein – beide wirken auf das Buch. Das ist ein Kräftegleichgewicht. Die Gegenkraft zur Gewichtskraft ist die Anziehung des Buches auf die Erde."),
        ("Zwei Kraftmesser ineinander, einer zeigt 2 N. Wie groß ist die Zugkraft?", "Ungefähr 2 N. Die Anzeigen werden nicht addiert.")],
}

STOLPERSTEINE = [("»Wo Bewegung ist, wirkt eine Kraft«",
                  "Für eine gleichförmige geradlinige Bewegung braucht es **keine resultierende** Kraft. Gleichgewicht heißt: Vektorsumme null – Ruhe **oder** gleichförmige gerade Bewegung. Mit Aufgabe 8 g) ansprechen."),
                 ("»Geschwindigkeit, Beschleunigung und Druck sind Kraftarten«",
                  "Sie sind **keine** Kräfte. Druck verbindet eine Kraft mit einer Fläche, Geschwindigkeit und Beschleunigung beschreiben die Bewegung. Buch S. 49 listet sie in einer gemeinsamen Übersicht – das lädt zur Verwechslung ein."),
                 ("»Beim Schwimmen ist der Auftrieb größer«",
                  "Beim **ruhigen** Schwimmen gilt F_A = F_G. Nur ein zunächst ruhender, vollständig eingetauchter Körper mit größerem Auftrieb wird nach oben beschleunigt. Buch S. 52 und viele Bilder verkürzen das."),
                 ("»Haftreibung ist immer größer als Gleitreibung«",
                  "Verglichen wird die **maximale** Haftreibung bei derselben Materialpaarung. Die aktuelle Haftreibung passt sich bis zu diesem Maximum an und kann klein sein."),
                 ("»Zwei Kraftmesser zeigen zusammen 4 N«",
                  "Beide Geräte messen **dieselbe** übertragene Zugkraft an verschiedenen Stellen der ruhenden Messkette. Anzeigen werden nicht addiert. Gleichgewichtspaar und Wechselwirkungspaar auseinanderhalten.")]

# ---------------------------------------------------------------- Quiz (12 Fragen, richtige Antwort an 1. Stelle, Anzeige gemischt)
QUIZ = [
 ("Kraftbegriff", "Woran kann man eine mechanische Kraftwirkung erkennen?",
  ["an einer Bewegungsänderung oder einer Verformung", "nur daran, dass etwas warm wird", "nur daran, dass ein Körper schon in Bewegung ist", "an der Einheit, in der man rechnet"],
  "Eine Kraft ändert das Tempo oder die Richtung einer Bewegung oder verformt einen Körper. Eine gleichförmige Bewegung allein beweist keine resultierende Kraft.", "Buch S. 45"),
 ("Einheiten", "Welche Einheit passt zur Kraft?", ["Newton", "Kilogramm", "Pascal", "Meter pro Sekunde"],
  "Newton (N) ist die Krafteinheit. Kilogramm gehört zur Masse, Pascal zum Druck.", "Buch S. 49"),
 ("Bewegung", "Ein Fahrzeug bremst. Ist das eine Beschleunigung?",
  ["ja, seine Geschwindigkeit ändert sich", "nein, Beschleunigung bedeutet nur schneller werden", "nur bei einer Kurve", "nur wenn die Masse zunimmt"],
  "Physikalisch ist jede Änderung der Geschwindigkeit eine Beschleunigung – auch das Langsamerwerden und die Richtungsänderung.", "Buch S. 47–48"),
 ("Rechnen", "Wandle 10 m/s in km/h um.", ["36 km/h", "2,8 km/h", "100 km/h", "3,6 km/h"],
  "Von m/s auf km/h wird mit 3,6 multipliziert: 10 · 3,6 = 36 km/h.", "Buch S. 47"),
 ("Gewichtskraft", "Welche Gewichtskraft hat eine Masse von 8 kg bei g = 10 N/kg?", ["80 N", "8 N", "0,8 N", "800 N"],
  "F_G = m · g = 8 kg · 10 N/kg = 80 N.", "Buch S. 50–51"),
 ("Gewichtskraft", "Was bleibt für einen Rucksack auf Erde und Mond gleich?", ["die Masse", "die Gewichtskraft", "der Ortsfaktor", "der Druck auf die Schulter"],
  "Die Masse ist eine Eigenschaft des Körpers. Die Gewichtskraft hängt vom Ortsfaktor ab, und der ist am Mond kleiner.", "Buch S. 50–51"),
 ("Auftrieb", "Wie groß ist die Auftriebskraft auf einen Körper im Fluid?",
  ["so groß wie die Gewichtskraft des verdrängten Fluids", "immer größer als seine Gewichtskraft", "immer null, wenn er sinkt", "so groß wie seine eigene Masse"],
  "Das ist das Prinzip von Archimedes. Auch ein sinkender Körper erfährt Auftrieb – seine Gewichtskraft ist nur größer.", "Buch S. 52–53"),
 ("Reibung", "Wann ist eine Zugkraftmessung als Gleitreibungsmessung gut auswertbar?",
  ["beim gleichförmigen waagrechten Ziehen", "beim möglichst starken Anreißen", "wenn der Körper vom Tisch abhebt", "wenn man schräg nach oben zieht"],
  "Beim gleichförmigen Ziehen gleichen sich Zugkraft und Gleitreibung waagrecht annähernd aus. Beim Anreißen kommt eine Beschleunigung dazu.", "Buch S. 54–56"),
 ("Reibung", "Welche Aussage zur Haftreibung stimmt?",
  ["Sie kann das Abstoßen beim Gehen ermöglichen", "Sie ist immer eine gleich große Kraft", "Sie ist immer größer als jede andere Reibungskraft", "Sie wirkt nur bei nassen Oberflächen"],
  "Haftreibung verhindert Rutschen und kann dadurch antreiben. Sie passt sich bis zu einem Höchstwert an.", "Buch S. 54–56"),
 ("Kapillarkraft", "Was bedeutet Kohäsion?",
  ["der Zusammenhalt innerhalb eines Stoffes", "die Anziehung zwischen verschiedenen Stoffen an einer Grenzfläche", "die Gewichtskraft pro Fläche", "der Auftrieb in einer engen Röhre"],
  "Kohäsion ist der Zusammenhalt innerhalb eines Stoffes. Die Anziehung zwischen verschiedenen Stoffen heißt Adhäsion.", "Buch S. 57"),
 ("Druck", "Eine Kraft von 100 N wirkt senkrecht auf 0,01 m². Wie groß ist der mittlere Druck?", ["10 000 Pa", "1 000 Pa", "100 Pa", "1 Pa"],
  "p = F / A = 100 N : 0,01 m² = 10 000 Pa.", "Buch S. 58"),
 ("Gegenkraft", "Warum heben sich die beiden Kräfte eines Wechselwirkungspaars nicht gegenseitig auf?",
  ["weil sie auf verschiedene Körper wirken", "weil eine von ihnen grundsätzlich größer ist", "weil sie nacheinander auftreten", "weil eine von ihnen keine echte Kraft ist"],
  "Genau das unterscheidet sie vom Kräftegleichgewicht, bei dem sich Kräfte an demselben Körper ausgleichen. Die Beträge sind gleich groß.", "Buch S. 61"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]
assert len(QUIZ) == 12

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 07.11.2026, aus dem Übergabepaket)
QUELLEN = [
 ("W1", "Newton's Third Law", "OpenStax, University Physics Volume 1 (Rice University)", "https://openstax.org/books/university-physics-volume-1/pages/5-5-newtons-third-law",
  "Wechselwirkungskräfte sind gleich groß und wirken auf verschiedene Körper", "Seite geöffnet, Text geprüft"),
 ("W2", "Friction", "OpenStax, University Physics Volume 1", "https://openstax.org/books/university-physics-volume-1/pages/6-2-friction",
  "Haftreibung passt sich bis zum Maximum an; F_R = μ · F_N ist eine Näherung", "Seite geöffnet, Abschnitte geprüft"),
 ("W3", "Archimedes' Principle and Buoyancy", "OpenStax, University Physics Volume 1", "https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy",
  "Auftrieb = Gewichtskraft des verdrängten Fluids; ruhiges Schwimmen ist Gleichgewicht", "Seite geöffnet, Abschnitte geprüft"),
 ("W4", "Transport of Water and Solutes in Plants", "OpenStax, Biology", "https://openstax.org/books/biology/pages/30-5-transport-of-water-and-solutes-in-plants",
  "Transpirationssog und Kohäsion erklären den Wassertransport hoher Pflanzen", "Seite geöffnet, Abschnitt Xylem geprüft"),
 ("W5", "Fluids, Density, and Pressure", "OpenStax, University Physics Volume 1", "https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure",
  "Druck als Kraft pro Fläche; Gase sind leichter zusammendrückbar als Flüssigkeiten", "Seite geöffnet, Abschnitte geprüft"),
 ("W7", "Messung von Haftreibung und Gleitreibung", "FWU / LEIFIphysik", "https://www.leifiphysik.de/mechanik/reibung-und-fortbewegung/aufgabe/messung-von-haftreibung-und-gleitreibung",
  "Messmethode für Gruppe 4: Losbrechmaximum und gleichförmiges Ziehen unterscheiden", "Aufgabe und Lösung geöffnet"),
 ("W8", "Extrem geringe Reibung durch neues pulverförmiges Schmiermittel (18.02.2025)", "TU Wien, Aussender Florian Aigner",
  "https://www.tuwien.at/tu-wien/aktuelles/presseaussendungen/news/extrem-geringe-reibung-durch-neues-pulverfoermiges-schmiermittel",
  "Zusatzaufgabe 11: aktueller Forschungsbezug und Quellenkritik (Eigenbericht)", "Titel, Datum, Aussender und Kernaussage geprüft"),
 ("W9", "Advanced Solid Lubrication with COK-47", "Hanglin Li et al., Advanced Science 2025", "https://doi.org/10.1002/advs.202415268",
  "Originalpublikation zur TU-Wien-Meldung", "Originalseite geöffnet, Autorenschaft geprüft"),
 ("W13", "Mittlere Geschwindigkeit", "FWU / LEIFIphysik", "https://www.leifiphysik.de/mechanik/gleichfoermige-bewegung/grundwissen/mittlere-geschwindigkeit",
  "Recherchezugang Gruppe 1: Weg durch Zeit und die Aussagegrenze", "Seite geöffnet, Text gelesen"),
 ("W14", "Gewichtskraft", "FWU / LEIFIphysik", "https://www.leifiphysik.de/mechanik/kraft-und-masse-ortsfaktor/grundwissen/gewichtskraft",
  "Recherchezugang Gruppe 2: Gewichtskraft und Ortsfaktor", "Seite geöffnet, Text gelesen"),
 ("W15", "Gravitation – Ursache der Gewichtskraft", "FWU / LEIFIphysik", "https://www.leifiphysik.de/mechanik/kraft-und-masse-ortsfaktor/grundwissen/gravitation-ursache-der-gewichtskraft",
  "Recherchezugang Gruppe 7: gleich große Kräfte zwischen Erde und Körper", "Seite geöffnet, Text gelesen"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "PhET »Forces and Motion: Basics« – Lizenztext, Einbettung und Handybedienung wurden nicht geprüft. Deshalb ist keine Simulation eingebaut.",
 "Journal of Chemical Education, »Soap Boat 2.0« (DOI 10.1021/ed400316a) – Zugriff mit 403 verweigert. Nur als fachlicher Hinweis im Lehrerwissen, nicht als Unterrichtsmedium.",
 "Seilnacht-Filmverzeichnis »Chemische Phänomene erleben« (Ausgabe 2): passende Titel für Oberflächenspannung und Benetzung sind »Die schwimmende Büroklammer«, "
 "»Wasserläufer«, »Konfetti und Seife«, »Benetzung eines Gewebes mit einem Tensid«. Nur das Verzeichnis wurde geöffnet, kein Film angesehen – Einbau durch Prof. HOLZER.",
 "Videos: YouTube ist von hier aus nicht prüfbar. Deshalb ist in dieser Einheit kein Video verlinkt.",
]
