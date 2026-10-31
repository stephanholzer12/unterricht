"""NAWI 2AB · K1.3 Stoffumwandlung (Trauner S. 29–37, Korrosionsschutz S. 98) – 4 Stunden (v8).
Jahresplan (Excel v101): »Stoffumwandlung: Redox, Energie, Katalysatoren« = 4 Stunden (Di 03.11., Do 05.11., Di 10.11., Do 12.11.); ab Di 17.11. Säuren und Basen.
Hier in Buch-Reihenfolge auf 4 Stunden zugeschnitten (Stunde 2 = Teststunde, 20 min Test). Reaktionsgeschwindigkeit (Tempo, Buch S. 36–37) ist Zusatz/Selbststudium.
Eine Quelle für Handy-Seiten (Theorie-Seite, Arbeitsblatt, Quiz), Word, PPP, Kahoot und Lehrer-Seite.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "31.10.2026"
V = "v5"
ORDNER = "2ab-nawi/k1-3-reaktionen"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "2ab-nawi/"
EYEBROW = "NAWI · 2AB · K1.3 Stoffumwandlung"
TITEL = "Stoffumwandlung – Redox, Energie und Katalysatoren"
KURZTITEL = "Redox, Energie, Katalysatoren"
BUCH = "Buch S. 29–37"
KEY = "26-27-2AB-K1.3-Reaktionen-TH-Handy-v1"
PRAEFIX = "26-27-2AB-K1.3-Reaktionen"

VIDEOS = {
    "redox": ("Redoxreaktion einfach erklärt", "studyflix", "5 min", "https://studyflix.de/chemie/redoxreaktion-einfach-erklart-4116"),
    "cuo": ("Kupferoxid wird mit Kohlenstoff reduziert", "Filmtipp aus dem Buch S. 31", "kurz", "https://www.trauner.at/nawi_v130"),
    "cufe": ("Kupferoxid wird mit Eisen reduziert", "Filmtipp aus dem Buch S. 31", "kurz", "https://www.trauner.at/nawi_v131"),
    "exoendo_buch": ("Exotherme und endotherme Reaktionen", "Filmtipp aus dem Buch S. 32", "kurz", "https://www.trauner.at/nawi_v19"),
    "exoendo": ("Exotherme und endotherme Reaktion", "studyflix", "2,5 min", "https://studyflix.de/physik/exotherme-und-endotherme-reaktion-1154"),
    "kat": ("Katalysator einfach erklärt", "studyflix", "4 min", "https://studyflix.de/chemie/katalysator-2896"),
}

DATEN = {1: "Di 03.11.", 2: "Do 05.11.", 3: "Di 10.11.", 4: "Do 12.11."}


def first(lst, correct):
    """Liste mit der richtigen Antwort an erster Stelle (Anzeige wird gemischt)."""
    return [correct] + [x for x in lst if x != correct]


BR = ["brennt mit Flamme", "brennt nicht richtig (schmilzt, wird braun)"]
OR = ["Verbindung eines Stoffes mit Sauerstoff", "Abgabe von Elektronen", "Entzug (Abspaltung) von Sauerstoff", "Aufnahme von Elektronen"]
RX = ["Redoxreaktion", "keine Redoxreaktion"]
SCHUTZ = ["Schutzschicht hält Wasser und Sauerstoff fern", "unedleres Zink wird statt dem Eisen oxidiert",
          "Chrom bildet eine dichte, unsichtbare Oxidschicht", "Salz, das das Rosten beschleunigt, wird entfernt", "ohne Wasser kein Rost"]
EE = ["exotherm", "endotherm"]
PF = ["die Aktivierungsenergie", "die frei werdende Energie", "die aufgenommene Energie"]
SCH = ["schäumt deutlich", "kaum oder gar nicht"]
SN = ["stimmt", "stimmt nicht"]
ST = ["Oberfläche (Zerteilung)", "Temperatur", "Konzentration", "Katalysator"]

T = [
 # ======================================================= Stunde 1 · Redoxreaktionen
 {"id": "a1", "nr": 1, "title": "Leichter oder schwerer? (Demo K1.3-V1)", "src": "Buch S. 30", "own": True, "tag": "Stunde 1", "h": 1, "hl": False, "zeit": 3,
  "q": "Eisenwolle liegt auf der Waage und wird mit einer Batterie angezündet. a) Tippe VOR der Demo: Was zeigt die Waage danach? (Der Tipp zählt nicht für die Bewertung.) "
       "b) Was zeigte die Waage wirklich? c) Erkläre in 1–2 Sätzen, woher die zusätzliche Masse kommt.",
  "hint": "Erst tippen, dann zuschauen (fällt die Demo aus, nennt die Lehrkraft Beispielwerte). Info: Theorie-Seite Teil 1 »Lavoisier und die Waage«",
  "type": "multi",
  "fields": [["tipp", "a) Mein Tipp vor der Demo", ["leichter", "schwerer", "gleich schwer"], False],
             ["erg", "b) Ergebnis: Die Eisenwolle ist danach …", ["schwerer", "leichter", "gleich schwer"]],
             ["warum", "c) Woher kommt die zusätzliche Masse? (1–2 Sätze)"]],
  "chk": {"erg": {"sel": "schwerer"},
          "warum": {"kw": [["Sauerstoff aus der Luft", "sauerstoff|o2|o₂|luft"], ["wird eingebaut / verbindet sich", "verbind|eingebaut|einbau|bindet|gebunden|aufgenommen|aufnimm|nimmt|aufnahme|reagier|oxid|dazu|hinzu|kommt"]]}},
  "sol": [["Lösung", ["a) Die meisten tippen »leichter« – wie beim Holz, das zu Asche zerfällt.",
                      "b) schwerer (z. B. 1,20 g → ca. 1,5 g)",
                      "c) Das Eisen verbindet sich mit Sauerstoff aus der Luft zu Eisenoxid. Die Masse des eingebauten Sauerstoffs kommt dazu. "
                      "(Beim Holz entweichen Kohlenstoffdioxid und Wasserdampf als Gase – deshalb ist die Asche leichter. Die Gesamtmasse bleibt in beiden Fällen gleich.)"]]],
  "tip": ["Lavoisier und die Waage", "theorie.html#lavoisier"]},

 {"id": "a2", "nr": 2, "title": "Oxidation – früher und heute", "src": "Buch S. 30", "own": True, "tag": "Stunde 1", "h": 1, "hl": False, "zeit": 4,
  "q": "Die Wörter Oxidation und Reduktion haben heute eine erweiterte Bedeutung. Wähle für jedes Feld die passende Bedeutung. e) Warum spricht man von einer Redoxreaktion?",
  "type": "multi",
  "fields": [["ox_alt", "a) Oxidation – ursprüngliche Bedeutung", first(OR, OR[0])],
             ["ox_neu", "b) Oxidation – heutige Bedeutung", first(OR, OR[1])],
             ["red_alt", "c) Reduktion – ursprüngliche Bedeutung", first(OR, OR[2])],
             ["red_neu", "d) Reduktion – heutige Bedeutung", first(OR, OR[3])],
             ["redox", "e) Redoxreaktion heißt: …", ["Oxidation und Reduktion laufen immer gleichzeitig ab.", "Zuerst läuft die Oxidation ab, Stunden später die Reduktion.",
                                                   "Es gibt nur Oxidationen – Reduktion ist ein anderes Wort dafür.", "Redox ist der Name eines Forschers."]]],
  "chk": {"ox_alt": {"sel": OR[0]}, "ox_neu": {"sel": OR[1]}, "red_alt": {"sel": OR[2]}, "red_neu": {"sel": OR[3]},
          "redox": {"sel": "Oxidation und Reduktion laufen immer gleichzeitig ab."}},
  "sol": [["Lösung", ["Oxidation: früher Verbindung mit Sauerstoff – heute Abgabe von Elektronen",
                      "Reduktion: früher Entzug von Sauerstoff – heute Aufnahme von Elektronen",
                      "e) Die Elektronen, die ein Stoff abgibt, nimmt ein anderer auf – Oxidation und Reduktion laufen immer gleichzeitig ab (REDuktion + OXidation)."]]],
  "tip": ["Was ist eine Redoxreaktion?", "theorie.html#redox"]},

 {"id": "a3", "besprechen": True, "nr": 3, "title": "Magnesium verbrennt – wer gibt, wer nimmt?", "src": "Buch S. 30", "own": True, "tag": "Stunde 1", "h": 1, "hl": False, "zeit": 6,
  "q": "Magnesium verbrennt mit grellem Licht zu weißem Magnesiumoxid: 2 Mg + O₂ → 2 MgO. "
       "a) Wie viele Elektronen gibt ein Magnesium-Atom ab? (Tipp: Magnesium steht in der 2. Hauptgruppe.) b) Wie viele Elektronen nimmt ein Sauerstoff-Atom auf? c)–f) Wähle aus.",
  "type": "multi",
  "fields": [["ea", "a) Elektronen, die ein Mg-Atom abgibt (Zahl)"], ["eb", "b) Elektronen, die ein O-Atom aufnimmt (Zahl)"],
             ["ox", "c) Oxidiert wird …", ["Magnesium", "Sauerstoff", "Magnesiumoxid"]],
             ["red", "d) Reduziert wird …", ["Sauerstoff", "Magnesium", "Magnesiumoxid"]],
             ["om", "e) Das Oxidationsmittel ist …", ["Sauerstoff", "Magnesium", "Magnesiumoxid"]],
             ["rm", "f) Das Reduktionsmittel ist …", ["Magnesium", "Sauerstoff", "Magnesiumoxid"]]],
  "chk": {"ea": {"num": 2, "unit": ""}, "eb": {"num": 2, "unit": ""}, "ox": {"sel": "Magnesium"}, "red": {"sel": "Sauerstoff"},
          "om": {"sel": "Sauerstoff"}, "rm": {"sel": "Magnesium"}},
  "sol": [["Lösung", ["a) 2 Elektronen: Mg → Mg²⁺ + 2 e⁻ (Oxidation)",
                      "b) 2 Elektronen: O + 2 e⁻ → O²⁻ (Reduktion; ein O₂-Molekül nimmt also 4 e⁻ auf)",
                      "c) Magnesium wird oxidiert · d) Sauerstoff wird reduziert",
                      "e) Oxidationsmittel = Sauerstoff (nimmt Elektronen auf) · f) Reduktionsmittel = Magnesium (gibt Elektronen ab)"]]],
  "tip": ["Elektronen wandern: Magnesium verbrennt", "theorie.html#elektronen"]},

 {"id": "a4", "nr": 4, "title": "Kupfer aus schwarzem Pulver", "src": "Buch-Aufgabe S. 31", "own": False, "tag": "Zusatz", "h": 1, "hl": False, "zeit": 5, "opt": ["rm"],
  "q": "Schwarzes Kupferoxid und Holzkohle werden im Reagenzglas erhitzt – danach liegt rötliches Kupfer im Glas (Versuch und Video im Buch S. 31). "
       "a) Ergänze die Gleichung: C + 2 CuO → CO₂ + 2 ___ b) Wohin ist der Sauerstoff gewandert? c) Welcher Stoff wird reduziert? "
       "Zusatz: d) Bei CuO + Fe → Cu + FeO – welcher Stoff ist das Reduktionsmittel?",
  "hint": "Zusatz – nur wenn du mit den Pflichtaufgaben dieser Stunde fertig bist (keine Hausübung). Info: Theorie-Seite Teil 1 »Oxidationsmittel und Reduktionsmittel« · Video: Filmtipp aus dem Buch S. 31 · d) ist freiwillig",
  "type": "multi",
  "fields": [["prod", "a) Es entsteht 2 … (Formel oder Name)"],
             ["wohin", "b) Der Sauerstoff wandert …", ["vom Kupfer zum Kohlenstoff", "vom Kohlenstoff zum Kupfer", "in die Luft", "er verschwindet"]],
             ["red", "c) Reduziert wird …", ["Kupferoxid (CuO)", "Kohlenstoff (C)", "Kohlenstoffdioxid (CO₂)"]],
             ["rm", "d) Zusatz (freiwillig): Das Reduktionsmittel ist …", ["Eisen (Fe)", "Kupferoxid (CuO)", "Kupfer (Cu)"]]],
  "chk": {"prod": {"kw": [["Cu / Kupfer (nur der Stoff, keine Verbindung)", r"^\W*(2\s*)?((reines|elementares|metallisches)\s+)?(cu|kupfer)(\s*\(\s*(cu|kupfer)\s*\)|\s*-?\s*metall)?\W*$"]]}, "wohin": {"sel": "vom Kupfer zum Kohlenstoff"},
          "red": {"sel": "Kupferoxid (CuO)"}, "rm": {"sel": "Eisen (Fe)"}},
  "sol": [["Lösung", ["a) C + 2 CuO → CO₂ + 2 Cu (Kupfer)",
                      "b) Der Sauerstoff wandert vom Kupfer zum Kohlenstoff – Kohlenstoff wird oxidiert, Kupferoxid reduziert.",
                      "c) Kupferoxid wird reduziert (Cu²⁺ nimmt 2 Elektronen auf → Cu).",
                      "d) Eisen ist das Reduktionsmittel – es gibt Elektronen ab und wird selbst oxidiert."]]],
  "tip": ["Oxidationsmittel und Reduktionsmittel", "theorie.html#mittel"]},

 # ======================================================= Stunde 2 · Redox im Alltag (nach dem Test)
 {"id": "a5", "nr": 5, "title": "Der Kupferbrief (Demo K1.3-V3)", "src": "Buch S. 30", "own": True, "tag": "Stunde 2", "h": 2, "hl": False, "zeit": 3,
  "hint": "Beobachtung in der Demo K1.3-V3 (fällt sie aus, zeigt die Lehrkraft ein Foto). Info: Theorie-Seite Teil 2.",
  "q": "Ein gefaltetes Kupferblech (»Brief«) wird in der Brennerflamme erhitzt und nach dem Abkühlen aufgeklappt. a) Tippe vorher: Wie sieht es innen aus? "
       "b) und c) Was siehst du wirklich? d) Erkläre den Unterschied in 1–2 Sätzen.",
  "type": "multi",
  "fields": [["tipp", "a) Mein Tipp: innen ist es …", ["schwarz wie außen", "glänzend wie vorher", "grün"], False],
             ["aussen", "b) Außen ist das Blech …", ["schwarz", "glänzend kupferrot", "grün"]],
             ["innen", "c) Innen ist das Blech …", ["glänzend kupferrot", "schwarz", "grün"]],
             ["warum", "d) Darum ist es innen anders (1–2 Sätze)"]],
  "chk": {"aussen": {"sel": "schwarz"}, "innen": {"sel": "glänzend kupferrot"},
          "warum": {"kw": [["Sauerstoff / Luft", "sauerstoff|luft|o2|o₂"], ["innen fehlt die Luft (gefaltet, dicht)", r"innen.{0,60}(kein|kaum|wenig|nicht|ohne|fehl)|(kein|kaum|wenig|nicht|ohne).{0,60}(innen|hinein|rein\b|dazwischen|zwischen)|gefaltet|zugeklappt|zusammengeklappt|abgeschlossen|abgedichtet|luftdicht|\bdicht|verschlossen|geschützt|abgeschirmt|fehlt"]]}},
  "sol": [["Lösung", ["b) außen schwarz (Kupferoxid) · c) innen glänzend kupferrot",
                      "d) Außen kommt Sauerstoff aus der Luft an das heiße Kupfer – es wird zu schwarzem Kupferoxid oxidiert. "
                      "Innen ist der Brief zugefaltet, dort kommt kaum Luft hin: ohne Luftsauerstoff entsteht dort kein Kupferoxid."]]],
  "tip": ["Redox im Alltag – der Kupferbrief", "theorie.html#alltag"]},

 {"id": "a6", "nr": 6, "title": "Redox-Detektiv", "src": "Buch S. 30", "own": True, "tag": "Stunde 2", "h": 2, "hl": False, "zeit": 3,
  "q": "Ist das eine Redoxreaktion? Entscheide bei jedem Vorgang.",
  "type": "multi",
  "fields": [["nagel", "Ein Eisennagel rostet.", RX, False], ["apfel", "Ein angeschnittener Apfel wird braun.", RX, False],
             ["holz", "Holz brennt im Lagerfeuer.", RX, False], ["akku", "Der Handy-Akku wird aufgeladen.", RX, False],
             ["eis", "Eis schmilzt in der Sonne.", RX, False], ["zucker", "Zucker löst sich im Tee.", RX, False],
             ["patina", "Ein Kupferdach wird mit den Jahren grün (Patina).", RX, False]],
  "chk": {"nagel": {"sel": RX[0]}, "apfel": {"sel": RX[0]}, "holz": {"sel": RX[0]}, "akku": {"sel": RX[0]},
          "eis": {"sel": RX[1]}, "zucker": {"sel": RX[1]}, "patina": {"sel": RX[0]}},
  "sol": [["Lösung", ["Redoxreaktionen: Rosten, brauner Apfel, Verbrennung, Akku laden, Patina am Kupfer (Kupfer wird oxidiert).",
                      "Keine Redoxreaktion: Eis schmelzen (nur der Aggregatzustand ändert sich) und Zucker lösen (es entsteht kein neuer Stoff)."]]],
  "tip": ["Redox im Alltag", "theorie.html#alltag"]},

 {"id": "a7", "nr": 7, "title": "Rostschutz an Gerät und Fahrzeug", "src": "Buch S. 98", "own": True, "tag": "Stunde 2", "h": 2, "hl": False, "zeit": 4,
  "q": "Ordne jeder Maßnahme zu, wie sie das Eisen schützt.",
  "type": "multi",
  "fields": [["lack", "Lack auf dem Radpanzer", first(SCHUTZ, SCHUTZ[0])],
             ["oel", "Den Gewehrlauf nach dem Schießen dünn einölen", first(SCHUTZ, SCHUTZ[0])],
             ["zink", "Verzinkte Leitplanke an der Straße", first(SCHUTZ, SCHUTZ[1])],
             ["edel", "Feldbesteck aus Edelstahl", first(SCHUTZ, SCHUTZ[2])],
             ["wasch", "Das Fahrzeug nach der Winterfahrt waschen", first(SCHUTZ, SCHUTZ[3])],
             ["trock", "Nasse Ausrüstung vor dem Einlagern trocknen", first(SCHUTZ, SCHUTZ[4])]],
  "chk": {"lack": {"sel": SCHUTZ[0]}, "oel": {"sel": SCHUTZ[0]}, "zink": {"sel": SCHUTZ[1]}, "edel": {"sel": SCHUTZ[2]},
          "wasch": {"sel": SCHUTZ[3]}, "trock": {"sel": SCHUTZ[4]}},
  "sol": [["Lösung", ["Lack und Öl: Schutzschicht hält Wasser und Sauerstoff fern",
                      "Verzinken: Zink ist unedler und wird zuerst oxidiert – es »opfert« sich für das Eisen",
                      "Edelstahl: Chrom im Stahl bildet eine dichte, unsichtbare Oxidschicht",
                      "Waschen nach der Winterfahrt: Streusalz beschleunigt das Rosten · Trocknen: ohne Wasser kein Rost"]]],
  "tip": ["Rostschutz an Gerät und Fahrzeug", "theorie.html#schutz"]},

 {"id": "a8", "nr": 8, "title": "Dein Pflegebefehl für den Winter", "src": "Buch S. 98", "own": True, "tag": "Zusatz", "h": 2, "hl": False, "zeit": 5,
  "q": "Kreativ und mit der Hand: Schreib ins Heft oder aufs Mini-Whiteboard einen kurzen »Pflegebefehl« mit 3 Punkten für ein Fahrzeug, eine Waffe oder deine Ausrüstung im Winter. "
       "Jeder Punkt braucht eine chemische Begründung (»…, weil …«). Fotografiere ihn und füge das Foto ein. Tippe außerdem deinen wichtigsten Punkt mit Begründung ab.",
  "hint": "Zusatz – nur wenn du mit den Pflichtaufgaben dieser Stunde fertig bist (keine Hausübung). Handschrift statt Tippen: zuerst schreiben, dann Foto einfügen.",
  "type": "sketch",
  "fields": [["punkt", "Mein wichtigster Punkt mit Begründung"]],
  "chk": {"punkt": {"kw": [["Begründung (weil, damit, sonst …)", r"weil|damit|denn|sonst|da |dadurch|wegen"],
                            ["Wasser, Sauerstoff oder Salz", "wasser|sauerstoff|luft|salz|feucht|nass|zink|öl|oel|schicht"]]}},
  "sol": [["Beispiel", ["1. Nach jeder Fahrt durch Streusalz den Unterboden abspritzen, weil Salz das Rosten beschleunigt.",
                        "2. Lauf und Verschluss nach dem Schießen reinigen und dünn ölen, weil der Ölfilm Wasser und Sauerstoff fernhält.",
                        "3. Nasse Ausrüstung erst trocknen, dann einlagern, weil Eisen ohne Wasser nicht rostet.",
                        "Selbst bewerten: 3 Punkte, jeder mit richtiger Begründung (Wasser, Sauerstoff, Salz, Schutzschicht, Zink)."]]],
  "tip": ["Rostschutz an Gerät und Fahrzeug", "theorie.html#schutz"]},

 # ======================================================= Stunde 3–4 · Energie (während der Stationen der anderen Gruppen)
 {"id": "a9", "nr": 9, "title": "Exotherm oder endotherm?", "src": "Buch-Aufgabe S. 37", "own": False, "tag": "Stunde 3–4", "h": 3, "hl": False, "zeit": 5,
  "q": "Wird bei dem Vorgang Energie an die Umgebung abgegeben (exotherm) oder aus der Umgebung aufgenommen (endotherm)? "
       "Zusatz zu den Buch-Aufgaben: Auch bei Vorgängen ohne neuen Stoff (Gefrieren, Verdunsten) spricht man von exotherm und endotherm.",
  "type": "multi",
  "fields": [["feuer", "Holz brennt im Lagerfeuer.", EE, False],
             ["rg", "Holz wird unter Luftabschluss erhitzt (die entstehenden Gase können abziehen) – ohne Flamme hört die Zersetzung auf.", EE, False],
             ["foto", "Ein Blatt betreibt Fotosynthese.", EE, False],
             ["hw", "Der Handwärmer wird warm.", EE, False],
             ["kp", "Die Sofort-Kältekompresse wird kalt.", EE, False],
             ["gefr", "Wasser gefriert zu Eis.", EE, False],
             ["schweiss", "Schweiß verdunstet auf der Haut.", EE, False]],
  "chk": {"feuer": {"sel": "exotherm"}, "rg": {"sel": "endotherm"}, "foto": {"sel": "endotherm"}, "hw": {"sel": "exotherm"},
          "kp": {"sel": "endotherm"}, "gefr": {"sel": "exotherm"}, "schweiss": {"sel": "endotherm"}},
  "sol": [["Lösung", ["exotherm: Lagerfeuer, Handwärmer, Gefrieren (Wasser gibt beim Erstarren Wärme ab)",
                      "endotherm: Holz unter Luftabschluss zersetzen (braucht ständig Wärme von außen – nie ein dicht verschlossenes Gefäß erhitzen!), Fotosynthese (Lichtenergie), Kältekompresse, Verdunsten von Schweiß (kühlt die Haut)"]]],
  "tip": ["Exotherm und endotherm", "theorie.html#exoendo"]},

 {"id": "a10", "nr": 10, "title": "Energiediagramme lesen", "src": "Buch S. 33–34", "own": True, "tag": "Stunde 3–4", "h": 3, "hl": False, "zeit": 5,
  "img": "img/a10_diagramme.png",
  "q": "Sieh dir die beiden Energiediagramme A und B an. Welcher Reaktionstyp ist das, und was zeigen die Pfeile 1, 2 und 3?",
  "type": "multi",
  "fields": [["a", "Diagramm A zeigt eine … Reaktion", EE, False], ["b", "Diagramm B zeigt eine … Reaktion", EE, False],
             ["p1", "Pfeil 1 zeigt …", PF, False], ["p2", "Pfeil 2 zeigt …", PF, False], ["p3", "Pfeil 3 zeigt …", PF, False],
             ["mehr", "In welchem Diagramm haben die Endstoffe MEHR Energie als die Ausgangsstoffe?", ["B", "A"], False]],
  "chk": {"a": {"sel": "exotherm"}, "b": {"sel": "endotherm"}, "p1": {"sel": PF[0]}, "p2": {"sel": PF[1]}, "p3": {"sel": PF[2]}, "mehr": {"sel": "B"}},
  "sol": [["Lösung", ["A exotherm (Endstoffe liegen tiefer) · B endotherm (Endstoffe liegen höher)",
                      "Pfeil 1 = Aktivierungsenergie (bis zum Gipfel) · Pfeil 2 = frei werdende Energie · Pfeil 3 = aufgenommene Energie",
                      "In B haben die Endstoffe mehr Energie – die Energie wurde aus der Umgebung aufgenommen und steckt jetzt in den Endstoffen."]]],
  "tip": ["Das Energiediagramm", "theorie.html#diagramm"]},

 {"id": "a11", "besprechen": True, "nr": 11, "title": "Das Lagerfeuer im Energiediagramm", "src": "Buch S. 33–34", "own": True, "tag": "Stunde 3–4", "h": 3, "hl": False, "zeit": 6,
  "q": "Zeichne mit der Hand ins Heft das Energiediagramm für die Verbrennung von Holz im Lagerfeuer. Beschrifte: Ausgangsstoffe (Holz + Sauerstoff), "
       "Endstoffe (Kohlenstoffdioxid + Wasser), Aktivierungsenergie, frei werdende Energie. Füge ein Foto ein. "
       "Pflicht: Erkläre in 1–2 Sätzen, warum man das Feuer anzünden muss, es danach aber von selbst weiterbrennt.",
  "hint": "Skizze ins Heft, dann Foto einfügen. Vorbild: Energiediagramm auf der Theorie-Seite (Teil 3).",
  "type": "sketch",
  "fields": [["erkl", "Warum anzünden – und warum brennt es dann von selbst weiter? (Pflicht)"]],
  "chk": {"erkl": {"kw": [["Aktivierungsenergie / Start", "aktivier|start|anzünd|zünd|anfang|zuerst|berg|hügel|barriere"],
                           ["frei werdende Wärme reicht für die nächsten Teilchen", "wärme|energie|hitze|weiter|selbst|nachbar|reicht|nächst"]]}},
  "sol": [["Lösung", ["Skizze: Ausgangsstoffe oben links, Kurve steigt zum Gipfel (Pfeil Aktivierungsenergie), fällt tief ab zu den Endstoffen (Pfeil frei werdende Energie, viel länger).",
                      "Erklärung: Zum Start muss die Aktivierungsenergie zugeführt werden (Streichholz, Feuerzeug). Die Verbrennung ist stark exotherm – "
                      "die frei werdende Wärme reicht, um die nächsten Holzteilchen zu aktivieren. Deshalb brennt das Feuer von selbst weiter."]]],
  "tip": ["Aktivierungsenergie – der Berg vor jeder Reaktion", "theorie.html#aktivierung"]},

 {"id": "a12", "nr": 12, "title": "Masse und Energie – rechnen mit Eisenwolle", "src": "Buch S. 30, 32", "own": True, "tag": "Zusatz", "h": 3, "hl": False, "zeit": 5,
  "hint": "Zusatz – nur wenn du mit den Pflichtaufgaben dieser Stunde fertig bist (keine Hausübung). Info: Theorie-Seite Teil 1 (Lavoisier) und Teil 3.",
  "q": "Bei der Demo K1.3-V1 lagen 1,20 g Eisenwolle auf der Waage. Nach dem Verbrennen zeigte sie 1,52 g. a) Wie viel Gramm Sauerstoff wurden eingebaut? "
       "b) Um wie viel Prozent ist die Masse gestiegen? (auf eine Kommastelle) c) Exotherm oder endotherm – woran erkennst du es?",
  "type": "multi",
  "fields": [["o2", "a) eingebauter Sauerstoff (mit Einheit)"], ["proz", "b) Zunahme in Prozent (mit Rechnung)"],
             ["ee", "c) Die Verbrennung der Eisenwolle ist …", ["exotherm – sie glüht und gibt Wärme und Licht ab", "endotherm – man braucht dafür eine Batterie",
                                                          "endotherm – die Eisenwolle wird schwerer"]]],
  "chk": {"o2": {"num": 0.32, "unit": "g"}, "proz": {"num": 26.7, "unit": ""}, "ee": {"sel": "exotherm – sie glüht und gibt Wärme und Licht ab"}},
  "sol": [["Lösung", ["a) 1,52 g − 1,20 g = 0,32 g Sauerstoff",
                      "b) 0,32 g : 1,20 g · 100 ≈ 26,7 %",
                      "c) exotherm – die Wolle glüht weiter und gibt Wärme und Licht ab. Die Batterie liefert nur die Aktivierungsenergie zum Start."]]],
  "tip": ["Masse und Energie bleiben erhalten", "theorie.html#erhalt"]},

 # ======================================================= Stunde 4 · Katalysatoren (alle)
 {"id": "a13", "besprechen": True, "nr": 13, "title": "Was lässt den Zucker brennen? (Demo K1.3-V7)", "src": "Buch S. 34", "own": True, "tag": "Stunde 4", "h": 4, "hl": False, "zeit": 4,
  "q": "Ein Zuckerwürfel lässt sich mit dem Feuerzeug kaum entzünden – er schmilzt und wird braun. Drei Würfel liegen auf der Unterlage: Würfel 1 pur, Würfel 2 mit etwas Holzasche bestreut, Würfel 3 mit etwas Kochsalz bestreut. "
       "a) Tippe: Welcher Würfel brennt mit Flamme? b) Trag für jeden Würfel ein, was du siehst. c) Welche Rolle spielt die Asche? d) Warum gab es Würfel 3 mit Kochsalz? (1 Satz)",
  "type": "multi",
  "fields": [["tipp", "a) Mein Tipp", ["Würfel 1 · pur", "Würfel 2 · mit Holzasche", "Würfel 3 · mit Kochsalz", "alle drei"], False],
             ["g1", "Würfel 1 · pur", BR, False], ["g2", "Würfel 2 · mit Holzasche", BR, False], ["g3", "Würfel 3 · mit Kochsalz", BR, False],
             ["rolle", "c) Die Asche wirkt hier als …", ["Katalysator – sie senkt die Aktivierungsenergie und wird nicht verbraucht", "zusätzlicher Brennstoff, der mitbrennt", "Löschmittel", "Oxidationsmittel, das Sauerstoff liefert"]],
             ["warum", "d) Darum gab es Würfel 3 mit Kochsalz (1 Satz)"]],
  "chk": {"g1": {"sel": BR[1]}, "g2": {"sel": BR[0]}, "g3": {"sel": BR[1]}, "rolle": {"sel": "Katalysator – sie senkt die Aktivierungsenergie und wird nicht verbraucht"},
          "warum": {"kw": [["Vergleich / Kontrolle", "vergleich|kontroll|gegenprobe|test|prüf|pruef|nur.{0,20}asche|andere.{0,10}pulver|auch.{0,10}pulver"],
                           ["nicht jedes Pulver wirkt", "nicht.{0,25}(jedes|alle|jeder)|nur.{0,25}(asche|bestimmte|manche)|salz.{0,25}(nicht|kein|wirkt)|kein.{0,20}effekt|keine.{0,20}wirkung|nichts"]]}},
  "sol": [["Lösung", ["Würfel 1 und Würfel 3 brennen nicht richtig (schmelzen, werden braun, verkohlen) · Würfel 2 (mit Asche) brennt mit ruhiger, bläulich-gelber Flamme.",
                      "c) Die Asche ist hier ein Katalysator: Sie senkt die Aktivierungsenergie der Verbrennung und wird dabei nicht verbraucht. (Wahrscheinlich wirken Salze von Alkalimetallen wie Kalium und Natrium in der Asche.)",
                      "d) Würfel 3 ist die Kontrolle: Auch ein Pulver auf dem Würfel (Salz) verändert nichts – es kommt auf die Asche an, nicht auf irgendein Pulver."]]],
  "tip": ["Katalysator-Demo und Enzyme", "theorie.html#enzyme"]},

 {"id": "a14", "nr": 14, "title": "Katalysator – stimmt das?", "src": "Buch-Aufgabe S. 37", "own": False, "tag": "Stunde 4", "h": 4, "hl": False, "zeit": 3,
  "q": "Entscheide bei jeder Aussage: stimmt oder stimmt nicht?",
  "type": "multi",
  "fields": [["s1", "Ein Katalysator senkt die Aktivierungsenergie.", SN, False],
             ["s2", "Ein Katalysator wird bei der Reaktion verbraucht und muss ständig nachgefüllt werden.", SN, False],
             ["s3", "Ein Hemmstoff (im Buch: »negativer Katalysator«) macht eine Reaktion langsamer.", SN, False],
             ["s4", "Enzyme wirken in unserem Körper als Katalysatoren.", SN, False],
             ["s5", "Der Autokatalysator ist schuld, dass ein Auto mehr Schadstoffe ausstößt.", SN, False],
             ["s6", "Ein Katalysator macht aus einer endothermen eine exotherme Reaktion.", SN, False]],
  "chk": {"s1": {"sel": "stimmt"}, "s2": {"sel": "stimmt nicht"}, "s3": {"sel": "stimmt"}, "s4": {"sel": "stimmt"},
          "s5": {"sel": "stimmt nicht"}, "s6": {"sel": "stimmt nicht"}},
  "sol": [["Lösung", ["stimmt: 1, 3 und 4 (Hemmstoffe bremsen Reaktionen – zum Beispiel, indem sie einen Katalysator blockieren)",
                      "stimmt nicht: 2 (ein Katalysator wird nicht verbraucht), "
                      "5 (der Autokatalysator verringert den Schadstoffausstoß), 6 (er ändert nur den Weg und das Tempo, nicht die Energie von Anfang und Ende)"]]],
  "tip": ["Was ist ein Katalysator?", "theorie.html#kat"]},

 # ======================================================= Stunde 5 · Reaktionsgeschwindigkeit + Abschluss
 {"id": "a15", "nr": 15, "title": "Die KI irrt sich – Fehlersuche beim Autokatalysator", "src": "Buch S. 35", "own": True, "tag": "Zusatz", "h": 4, "hl": False, "zeit": 10, "opt": ["zusatz"],
  "q": "Ein Kadett hat eine KI gefragt: »Wie funktioniert ein Autokatalysator?« Die Antwort: »Der Autokatalysator ist ein feiner Filter, der die giftigen Abgase zurückhält. "
       "Er besteht aus einer Keramikwabe mit einer Schicht, in der Edelmetalle wie Platin, Palladium und Rhodium fein verteilt sind. Der Katalysator wird dabei langsam verbraucht und muss bei jedem Service "
       "nachgefüllt werden. Er arbeitet am besten, wenn er kalt ist – deshalb stößt ein Auto direkt nach dem Start die wenigsten Schadstoffe aus. Aus giftigem "
       "Kohlenstoffmonoxid macht er Kohlenstoffdioxid.« Die Antwort klingt gut, enthält aber drei Fehler. Finde sie und schreib zu jedem den richtigen Satz. "
       "Zusatz: Stell die Frage selbst einer KI und prüfe die Antwort genauso.",
  "hint": "Zusatz – nur wenn du mit den Pflichtaufgaben dieser Stunde fertig bist (keine Hausübung). Lies im Buch S. 35 oder auf der Theorie-Seite Teil 4 »Der Autokatalysator« nach. KI-Antworten immer mit einer zweiten Quelle prüfen! Das Zusatzfeld ist freiwillig.",
  "type": "multi",
  "fields": [["fehler", "Die drei Fehler – und was richtig ist"], ["zusatz", "Zusatz (freiwillig): Was hat deine KI geantwortet – stimmt es?"]],
  "chk": {"fehler": {"kw": [["kein Filter – er wandelt um", r"kein filter|nicht.{0,20}filter|umwand|wandelt|verwandelt|umgewandelt|reagier"],
                             ["wird nicht verbraucht", r"nicht verbraucht|unverändert|unveraendert|bleibt|nicht nachgef|kein.{0,10}nachf|wird nicht"],
                             ["muss heiß sein – Kaltstart ist schlecht", r"heiß|heiss|warm|temperatur|kaltstart|nach dem start|300"]]}},
  "sol": [["Lösung", ["1. Kein Filter: Der Katalysator hält nichts zurück, er wandelt die Schadstoffe in harmlosere Stoffe um (CO → CO₂, Stickoxide → Stickstoff, Kohlenwasserstoffe → CO₂ + Wasser).",
                      "2. Ein Katalysator wird nicht verbraucht – er liegt nach der Reaktion unverändert vor.",
                      "3. Er arbeitet erst, wenn er heiß ist (ab etwa 300 °C). Direkt nach dem Kaltstart gelangen die meisten Schadstoffe ins Freie.",
                      "Richtig sind: Keramikwabe mit fein verteilten Edelmetallen (Platin, Palladium, Rhodium) · CO wird zu CO₂."]]],
  "tip": ["Der Autokatalysator", "theorie.html#autokat"]},

 {"id": "a16", "nr": 16, "title": "Vier Stellschrauben für das Tempo", "src": "Buch-Aufgabe S. 37", "own": False, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 4,
  "q": "Zusatz zum Thema Tempo (Teil 5 auf der Theorie-Seite, Buch S. 36–37): Welche Stellschraube macht die Reaktion hier schneller oder langsamer? Zusatz zur Buch-Aufgabe: die letzte Zeile.",
  "type": "multi",
  "fields": [["span", "Für das Lagerfeuer wird das Holz in dünne Späne gespalten.", ST, False],
             ["kuehl", "Die Feldverpflegung kommt im Sommer in die Kühlbox.", ST, False],
             ["blas", "Ein glimmender Holzspan flammt in reinem Sauerstoff hell auf – in Luft glimmt er nur.", ST, False],
             ["auspuff", "Im Auspuff wandeln Platin und Rhodium die Abgase rasch um.", ST, False],
             ["mehl", "In einer Mühle explodiert feiner Mehlstaub.", ST, False],
             ["fieber", "Bei Fieber laufen Vorgänge im Körper schneller ab.", ST, False],
             ["speichel", "Im Mund zerlegt das Enzym Amylase die Stärke einer Semmel in Zucker.", ST, False],
             ["schnell", "Eine Reaktion läuft am schnellsten bei …", ["hoher Temperatur und großer Oberfläche", "niedriger Temperatur und kleiner Oberfläche"], False]],
  "chk": {"span": {"sel": ST[0]}, "kuehl": {"sel": ST[1]}, "blas": {"sel": ST[2]}, "auspuff": {"sel": ST[3]}, "mehl": {"sel": ST[0]},
          "fieber": {"sel": ST[1]}, "speichel": {"sel": ST[3]}, "schnell": {"sel": "hoher Temperatur und großer Oberfläche"}},
  "sol": [["Lösung", ["Oberfläche: Späne, Mehlstaub · Temperatur: Kühlbox, Fieber · Konzentration: reiner Sauerstoff statt Luft (Luft hat nur rund 21 % Sauerstoff) · Katalysator: Auspuff, Amylase",
                      "Am schnellsten bei hoher Temperatur und großer Oberfläche."]]],
  "tip": ["Vier Stellschrauben für das Tempo", "theorie.html#tempo"]},

 {"id": "a17", "nr": 17, "title": "Brausetablette im Test (Versuch K1.3-V8)", "src": "Buch S. 36", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 5,
  "hint": "Zusatz. Messwerte aus dem Versuch K1.3-V8 – den Versuch machst du nur, wenn die Lehrkraft ihn freigibt. Sonst rechne nur d) und e) mit den Beispielwerten aus der Lösung. Eure Zeiten dürfen abweichen.",
  "q": "Trag eure Messwerte aus dem Versuch K1.3-V8 ein (Zeit, bis es nicht mehr sprudelt). d) Welcher Ansatz sollte laut Theorie am langsamsten sein? "
       "e) Modellrechnung mit der Faustregel (nicht eure Messung): Eine Tablette braucht in Wasser von 20 °C 80 s. Wie lange bräuchte sie ungefähr bei 40 °C?",
  "type": "multi",
  "fields": [["t1", "a) A · unzerkleinerte halbe Tablette, kaltes Wasser – Zeit in s"], ["t2", "b) B · zerdrückte halbe Tablette, kaltes Wasser – Zeit in s"],
             ["t3", "c) C · unzerkleinerte halbe Tablette, warmes Wasser – Zeit in s"],
             ["schnell", "d) Laut Theorie am langsamsten ist …", ["A · unzerkleinert im kalten Wasser", "B · zerdrückt im kalten Wasser", "C · unzerkleinert im warmen Wasser"]],
             ["rgt", "e) Zeit bei 40 °C (mit Einheit)"]],
  "chk": {"schnell": {"sel": "A · unzerkleinert im kalten Wasser"}, "rgt": {"num": 20, "unit": "s"}},
  "sol": [["Lösung", ["a)–c) Messwerte der Gruppe. Beispiel: A unzerkleinert, kalt ca. 60–120 s; B und C deutlich schneller (oft 20–50 s) – welcher von beiden schneller ist, kann wechseln. Eure Werte dürfen abweichen.",
                      "d) A – die unzerkleinerte halbe Tablette im kalten Wasser: kleinste Oberfläche und niedrigste Temperatur.",
                      "e) Modellrechnung mit der Faustregel: +10 °C → etwa doppelt so schnell. 20 °C → 30 °C: 40 s · 30 °C → 40 °C: 20 s. Also ca. 20 s. Die echte Brausezeit umfasst auch das Auflösen und folgt der Regel nur ungefähr."]]],
  "tip": ["Temperatur – die Faustregel", "theorie.html#rgt"]},

 {"id": "a18", "nr": 18, "title": "Partnercheck – fragt euch gegenseitig ab", "src": "Buch S. 30–36", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 6,
  "q": "Zusatz zur Wiederholung (z. B. vor dem Test K1.3): Arbeitet zu zweit, Handy von B bleibt weg. A öffnet auf der Theorie-Seite die »Partnercheck-Karten« (Teil 5) und stellt B drei Fragen. B antwortet mündlich, "
       "A vergleicht mit der Lösung und hakt ab. Dann tauscht ihr. Trag ein, mit wem du geübt hast, wie viele deiner Antworten richtig waren und was du nochmal lernen musst.",
  "type": "multi",
  "fields": [["partner", "Partnercheck mit (Name)"], ["richtig", "Meine Antworten: richtig waren …", ["3 von 3", "2 von 3", "1 von 3", "0 von 3"], False],
             ["lernen", "Das muss ich nochmal lernen:"]],
  "sol": [["Lösung", ["Die Karten mit Lösungen stehen auf der Theorie-Seite (Teil 5 »Partnercheck-Karten«). Selbst bewerten – ehrlich zählt!"]]],
  "tip": ["Partnercheck-Karten", "theorie.html#partner"]},

 # ======================================================= Für Schnelle und Neugierige
 {"id": "a19", "nr": 19, "title": "Science oder Fiction? Wasser aus Raketentreibstoff", "src": "Buch S. 34–35", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 6,
  "q": "Im Film »Der Marsianer« (2015) braucht ein gestrandeter Astronaut Wasser. Er leitet Raketentreibstoff (Hydrazin, N₂H₄) über einen Katalysator, der ihn zu einem heißen Gasgemisch "
       "zerlegt – darin ist unter anderem Wasserstoff –, und verbrennt den Wasserstoff dann mit Sauerstoff. a) Science oder Fiction? b) Welche Aufgabe hat der Katalysator? "
       "c) Warum ist das Verbrennen des Wasserstoffs gefährlich? (Tipp: Knallgas, Buch S. 35)",
  "type": "multi",
  "fields": [["sf", "a) Das ist …", ["Science – das Prinzip funktioniert wirklich", "Fiction – Wasser kann man nicht herstellen"]],
             ["kat", "b) Aufgabe des Katalysators"], ["gef", "c) Darum ist es gefährlich"]],
  "chk": {"sf": {"sel": "Science – das Prinzip funktioniert wirklich"},
          "kat": {"kw": [["zerlegt / beschleunigt / senkt Aktivierungsenergie", "zerleg|zerfall|spalt|beschleun|aktivier|schneller|startet"]]},
          "gef": {"kw": [["Knallgas / Explosion", "knall|explo|heftig|brand|zünd|feuer|knallt"]]}},
  "sol": [["Lösung", ["a) Science: Satelliten-Steuerdüsen zerlegen Hydrazin wirklich an einem Katalysator (meist Iridium) – es entsteht ein heißes Gemisch aus Stickstoff, Wasserstoff und Ammoniak. Wasserstoff + Sauerstoff → Wasser (2 H₂ + O₂ → 2 H₂O).",
                      "b) Er sorgt dafür, dass das Hydrazin schnell zerfällt – er senkt die Aktivierungsenergie und wird selbst nicht verbraucht.",
                      "c) Wasserstoff und Sauerstoff bilden Knallgas: Die Reaktion ist stark exotherm und kann explodieren – auch im Film geht etwas schief."]]],
  "tip": ["Für Schnelle: Science oder Fiction?", "theorie.html#schnelle"]},

 {"id": "a20", "nr": 20, "title": "Oxidationszahlen (Zusatz)", "src": "Buch-Aufgabe S. 32", "own": False, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 6,
  "q": "Oxidationszahlen zeigen, welche Ladung ein Atom in einer Verbindung hätte, wenn sie aus Ionen bestünde. Bestimme mit den Regeln auf der Theorie-Seite "
       "(»Für Schnelle«) die Oxidationszahl. Zusatz: Beim Thermitverfahren (Gleisbau) reagiert Fe₂O₃ + 2 Al → 2 Fe + Al₂O₃ – welches Element wird oxidiert?",
  "type": "multi",
  "fields": [["h", "Wasserstoff in H₂O", ["+I", "−I", "+II", "−II", "+III", "0"], False], ["cl", "Chlor in NaCl", ["+I", "−I", "+II", "−II", "+III", "0"], False],
             ["ca", "Calcium in CaCl₂", ["+I", "−I", "+II", "−II", "+III", "0"], False], ["al", "Aluminium in Al₂O₃", ["+I", "−I", "+II", "−II", "+III", "0"], False],
             ["o2", "Sauerstoff im O₂-Molekül", ["+I", "−I", "+II", "−II", "+III", "0"], False],
             ["therm", "Zusatz: Beim Thermitverfahren wird oxidiert …", ["Aluminium", "Eisen", "Sauerstoff"]]],
  "chk": {"h": {"sel": "+I"}, "cl": {"sel": "−I"}, "ca": {"sel": "+II"}, "al": {"sel": "+III"}, "o2": {"sel": "0"}, "therm": {"sel": "Aluminium"}},
  "sol": [["Lösung", ["H in H₂O: +I · Cl in NaCl: −I · Ca in CaCl₂: +II · Al in Al₂O₃: +III (2 · (+III) + 3 · (−II) = 0) · O in O₂: 0 (Element)",
                      "Thermit: Aluminium wird oxidiert (0 → +III), Eisen reduziert (+III → 0)."]]],
  "tip": ["Für Schnelle: Oxidationszahlen", "theorie.html#oz"]},

 {"id": "a21", "nr": 21, "title": "Forschung: Ein Ersatz für Iridium", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 8,
  "q": "Für grünen Wasserstoff wird Wasser mit Strom gespalten. Bei einem wichtigen Verfahren (in saurer Umgebung) enthalten die besten Katalysatoren für den Sauerstoff-Teil bisher Iridium – eines der seltensten Metalle der Erde. "
       "Ein Forschungsteam der Northwestern University (USA) stellte im August 2025 gemeinsam mit dem Toyota Research Institute einen Ersatz vor. "
       "a) Welche vier Metalle verwendeten die Forschenden statt Iridium? b) Wie lange lief der neue Katalysator im Test stabil? "
       "c) Warum ist das auch eine Frage der Wirtschaft und Sicherheit für Europa? (1–2 Sätze)",
  "hint": "Recherche im Internet: https://news.northwestern.edu/stories/2025/08/clean-hydrogens-iridium-problem-solved-in-an-afternoon (Englisch) oder auf Deutsch: https://www.ingenieur.de/technik/fachbereiche/chemie/wasserstoffproduktion-neue-katalysatoren-loesen-iridium-engpass/",
  "type": "multi",
  "fields": [["metalle", "a) Die vier Metalle statt Iridium"], ["dauer", "b) Dauer im Test"], ["warum", "c) Wirtschaft und Sicherheit (1–2 Sätze)"]],
  "chk": {"metalle": {"kw": [["Ruthenium", "ruthen"], ["Kobalt", "kobalt|cobalt"], ["Mangan", "mangan"], ["Chrom", "chrom"]]},
          "dauer": {"kw": [["über 1000 Stunden", r"1\.?000|tausend"]]},
          "warum": {"kw": [["selten, teuer, abhängig", "abhängig|abhaengig|selten|teuer|knapp|rohstoff|import|preis|kosten|versorg|china|südafrika"]]}},
  "sol": [["Lösung", ["a) Ruthenium, Kobalt, Mangan und Chrom (Ruthenium ist auch selten, aber viel billiger als Iridium; Kobalt, Mangan und Chrom sind häufig)", "b) über 1000 Stunden, laut Studie bei rund einem Sechzehntel der Kosten – ein Laborergebnis; bis zum Einsatz im Großbetrieb ist laut den Forschenden noch viel zu tun",
                      "c) Iridium ist sehr selten und teuer und fällt fast nur beim Platinabbau in wenigen Ländern an. Wer Katalysatoren aus häufigeren Metallen bauen kann, "
                      "macht Europa unabhängiger von Importen und die Energiewende billiger."]]],
  "tip": ["Für Schnelle: Was weiß die Forschung noch nicht?", "theorie.html#forschung"]},

 {"id": "a22", "nr": 22, "title": "Wirtschaft: Warum werden Katalysatoren gestohlen?", "src": "Recherche im Internet", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 5,
  "q": "Im März 2026 erwischte die Polizei in Wien-Simmering drei Männer, die an parkenden Autos mit dem Winkelschleifer die Katalysatoren abschnitten (Bericht auf wien.orf.at). "
       "a) Nenne die drei Edelmetalle, die einen Katalysator so wertvoll machen. b) Warum genügt im Katalysator wenig Edelmetall – und warum ist die wirksame Oberfläche trotzdem riesig? (2 Sätze)",
  "hint": "Bericht: https://wien.orf.at/stories/3346365/ · Info: Theorie-Seite Teil 4 »Der Autokatalysator«",
  "type": "multi",
  "fields": [["metalle", "a) Die drei Edelmetalle"], ["duenn", "b) Wenig Metall, große Oberfläche (2 Sätze)"]],
  "chk": {"metalle": {"kw": [["Platin", "platin"], ["Palladium", "pallad"], ["Rhodium", "rhod"]]},
          "duenn": {"kw": [["wird nicht verbraucht / wirkt immer wieder", "nicht verbraucht|bleibt|unverändert|unveraendert|immer wieder|wiederholt|mehrmals|nochmal"],
                           ["fein verteilt, große Oberfläche", "oberfläche|oberflaeche|fein verteilt|kontakt|berühr|kanäle|kanaele|wabe|poren|porös|poroes|teilchen"]]}},
  "sol": [["Lösung", ["a) Platin, Palladium und Rhodium – Rhodium war laut ORF (März 2026) mehr als doppelt so viel wert wie gleich schweres 750er-Gold (Preise schwanken).",
                      "b) Jedes Metallteilchen kann immer wieder an Reaktionen mitwirken – es wird nicht verbraucht, deshalb reicht wenig. Die Reaktion läuft nur dort, wo das Abgas das Metall berührt: "
                      "Darum sitzen die Edelmetalle fein verteilt in einer porösen Schicht auf einer Keramikwabe mit tausenden feinen Kanälen (riesige Oberfläche)."]]],
  "tip": ["Der Autokatalysator", "theorie.html#autokat"]},

 {"id": "a23", "nr": 23, "title": "Kreativ-Challenge: Video, Podcast oder Plakat", "src": "Buch S. 34", "own": True, "tag": "Zusatz", "h": 0, "hl": False, "zeit": 25,
  "q": "Erkläre neuen Rekruten, was ein Katalysator macht – allein oder zu zweit, freiwillig (ca. 25 min). Wähle eine Form: "
       "A) Plakat (A3, mit der Hand gezeichnet) · B) Erklärvideo (höchstens 2 Minuten) · C) Podcast (höchstens 2 Minuten). "
       "Pflichtinhalte: Aktivierungsenergie als »Berg«, der Katalysator öffnet einen niedrigeren Weg, er wird nicht verbraucht, ein Beispiel (Autokatalysator oder Enzym). "
       "Regeln: Andere Personen nur mit deren Zustimmung zeigen oder aufnehmen · keine fremde Musik und keine fremden Bilder · KI-Hilfe angeben. "
       "Abgabe: Plakat als Foto hier einfügen; Video oder Podcast in LMS hochladen (Teams nur, wenn die Datei zu groß ist) und hier ein Standbild bzw. einen Screenshot der Abgabe einfügen.",
  "type": "sketch",
  "fields": [["titel", "Form, Titel und 1–2 Sätze zum Inhalt (bei Video/Podcast: »in LMS hochgeladen am …«)"]],
  "chk": {"titel": {"kw": [["Aktivierungsenergie / Berg", "aktivier|berg|hügel|huegel|barriere|hürde|huerde|pass"],
                            ["Katalysator", "katalys|enzym|abkürz|abkuerz|tunnel|pass|schneller"]]}},
  "sol": [["Bewertung", ["Raster (10 Punkte): fachlich richtig 4 · Pflichtinhalte vorhanden (Berg = Aktivierungsenergie, niedrigerer Weg, nicht verbraucht, Beispiel) 2 · verständlich und gegliedert 2 · kreativ 1 · Länge und Abgabe eingehalten 1.",
                         "Musterinhalt: Ohne Katalysator müssen die Teilchen über einen hohen Berg – das schaffen nur wenige. Der Katalysator öffnet einen niedrigeren Pass, viel mehr Teilchen kommen ans Ziel, er selbst bleibt übrig (Autokatalysator: CO → CO₂; Enzym Katalase: H₂O₂ → Wasser + Sauerstoff)."]]],
  "tip": ["Aktivierungsenergie – der Berg vor jeder Reaktion", "theorie.html#aktivierung"]},
]
assert [t["nr"] for t in T] == list(range(1, 24))
PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]

# Offene Erklärungen: »Prüfen« zeigt nur eine Schreibhilfe (Stichwörter), keine automatische Richtig-Wertung,
# und im PDF zählen sie nicht zu den automatischen Punkten – die Lehrkraft bewertet sie (ChatGPT-Bericht v5, N02/N03).
MANUELL = {"a1": ["warum"], "a5": ["warum"], "a8": ["punkt"], "a11": ["erkl"], "a13": ["warum"], "a15": ["fehler"],
           "a19": ["kat"], "a21": ["warum"], "a22": ["duenn"], "a23": ["titel"]}
for _t in T:
    for _k in MANUELL.get(_t["id"], []):
        _t["chk"][_k]["man"] = True

GRP = {1: "Stunde 1 · Di 03.11. · Redoxreaktionen (Buch S. 30–31) · Aufgabe 4 ist Zusatz",
       2: "Stunde 2 · Do 05.11. · nach dem Test: Redox im Alltag, Rost (Buch S. 30–31, 98) · Aufgabe 8 ist Zusatz",
       3: "Stunde 3–4 · Di 10.11. / Do 12.11. · Energie – während die anderen Gruppen an den Stationen sind (Buch S. 32–34) · Aufgabe 12 ist Zusatz",
       4: "Stunde 4 · Do 12.11. · Katalysatoren und Abschluss (Buch S. 34–35) · Aufgabe 15 ist Zusatz",
       0: "Für Schnelle und Neugierige · Zusatz (auch Tempo der Reaktion, Buch S. 36–37)"}

LERNZIELE = ["**Oxidation** als Abgabe und **Reduktion** als Aufnahme von Elektronen erklären und bei einer Redoxreaktion sagen, wer Elektronen abgibt und wer sie aufnimmt",
             "einfache **Redoxgleichungen** lesen und ergänzen (z. B. Magnesium + Sauerstoff, Eisen in Kupfersulfatlösung) und erklären, wie Eisen rostet und wie man es schützt",
             "**exotherme** und **endotherme** Reaktionen unterscheiden, ein Energiediagramm mit **Aktivierungsenergie** zeichnen und erklären, warum die Masse erhalten bleibt",
             "erklären, wie ein **Katalysator** wirkt (Auto, Enzyme) und wie Oberfläche, Temperatur und Konzentration das **Tempo einer Reaktion** ändern"]

WICHTIGSTE = ["Bei einer **Redoxreaktion** wandern Elektronen: Die **Oxidation** ist die Abgabe, die **Reduktion** die Aufnahme von Elektronen – beides läuft immer gleichzeitig ab.",
              "Das **Reduktionsmittel** gibt Elektronen ab (und wird oxidiert), das **Oxidationsmittel** nimmt sie auf (und wird reduziert); Eisen rostet nur mit **Wasser und Sauerstoff**, Salz beschleunigt es.",
              "**Exotherme** Reaktionen geben Energie an die Umgebung ab (Verbrennung, Handwärmer), **endotherme** nehmen Energie auf (Fotosynthese, Kältekompresse).",
              "Fast jede Reaktion braucht zum Start die **Aktivierungsenergie**; Masse und Energie gehen dabei nicht verloren – sie werden nur umgewandelt.",
              "Ein **Katalysator** senkt die Aktivierungsenergie, beschleunigt so die Reaktion und wird **nicht verbraucht**; schneller wird eine Reaktion auch durch **größere Oberfläche, höhere Temperatur und höhere Konzentration**."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Redoxreaktion", "Reaktion, bei der Elektronen von einem Teilchen zu einem anderen wandern (Reduktion + Oxidation)"],
                ["Oxidation", "Abgabe von Elektronen (früher: Verbindung mit Sauerstoff)"],
                ["Reduktion", "Aufnahme von Elektronen (früher: Entzug von Sauerstoff)"],
                ["Oxidationsmittel", "Stoff, der Elektronen aufnimmt – er wird selbst reduziert (Elektronenakzeptor)"],
                ["Reduktionsmittel", "Stoff, der Elektronen abgibt – er wird selbst oxidiert (Elektronendonator)"],
                ["Korrosion", "Zerstörung eines Metalls durch Reaktion mit seiner Umgebung, z. B. Rosten von Eisen"],
                ["exotherm", "Reaktion gibt Energie (meist Wärme) an die Umgebung ab"],
                ["endotherm", "Reaktion nimmt Energie (meist Wärme) aus der Umgebung auf"],
                ["Energiediagramm", "zeigt die Energie der Ausgangsstoffe und Endstoffe im Verlauf einer Reaktion"],
                ["Aktivierungsenergie", "Energie, die man zuführen muss, damit eine Reaktion startet"],
                ["Katalysator", "Stoff, der eine Reaktion beschleunigt, weil er einen Weg mit niedrigerer Aktivierungsenergie öffnet – er wird dabei nicht verbraucht"],
                ["Hemmstoff (Inhibitor)", "Stoff, der eine Reaktion verlangsamt – im Buch »negativer Katalysator«"],
                ["Enzym", "Biokatalysator in Lebewesen, z. B. Amylase im Speichel, Katalase in der Leber"],
                ["Reaktionsgeschwindigkeit", "wie schnell Ausgangsstoffe zu Endstoffen werden – hängt von Oberfläche, Temperatur, Konzentration und Katalysator ab"],
                ["Faustregel (RGT-Regel)", "10 °C wärmer → viele Reaktionen laufen etwa doppelt so schnell"]]

WEISST_DU_NOCH = {
    2: [("Was ist eine Oxidation – heute?", "die Abgabe von Elektronen"),
        ("Magnesium verbrennt zu Magnesiumoxid. Wer ist das Reduktionsmittel?", "Magnesium – es gibt Elektronen ab."),
        ("Warum wird Eisenwolle beim Verbrennen schwerer?", "Sauerstoff aus der Luft wird eingebaut.")],
    3: [("Was braucht Eisen zum Rosten?", "Wasser und Sauerstoff – Salz beschleunigt es."),
        ("Wie schützt Zink das Eisen?", "Zink ist unedler und wird zuerst oxidiert."),
        ("Ist Schmelzen von Eis eine Redoxreaktion?", "Nein – es entsteht kein neuer Stoff, es wandern keine Elektronen.")],
    4: [("Exotherm oder endotherm: der Handwärmer?", "exotherm – er gibt Wärme ab."),
        ("Was zeigt im Energiediagramm der Gipfel?", "die Aktivierungsenergie – den »Berg« zum Start"),
        ("Warum wird es bei Zitronensäure + Natron kalt?", "Die Reaktion ist endotherm – sie nimmt Wärme aus der Umgebung auf.")],
}

STOPPFRAGEN = {
    1: [("Magnesium gibt 2 Elektronen ab. Oxidation oder Reduktion?", "Oxidation – Abgabe von Elektronen."),
        ("Wer ist bei 2 Mg + O₂ → 2 MgO das Oxidationsmittel?", "Sauerstoff – er nimmt die Elektronen auf.")],
    2: [("Welche zwei Dinge braucht Eisen zum Rosten?", "Wasser und Sauerstoff."),
        ("Warum rostet ein verzinkter Zaun kaum?", "Zink ist unedler und wird an Stelle des Eisens oxidiert.")],
    3: [("Exotherm oder endotherm: die Fotosynthese?", "endotherm – sie braucht Lichtenergie."),
        ("Warum muss man ein Lagerfeuer anzünden?", "Es braucht die Aktivierungsenergie zum Start.")],
    4: [("Wird ein Katalysator bei der Reaktion verbraucht?", "Nein."),
        ("Wann arbeitet ein Autokatalysator schlecht?", "kalt, direkt nach dem Start – er braucht ca. 300 °C.")],
}

PARTNERKARTEN = [("Was ist eine Oxidation – heute?", "Abgabe von Elektronen"),
                 ("Was ist eine Reduktion – heute?", "Aufnahme von Elektronen"),
                 ("Was braucht Eisen zum Rosten?", "Wasser und Sauerstoff (Salz beschleunigt)"),
                 ("Nenne ein Beispiel für eine endotherme Reaktion.", "Fotosynthese, Kältekompresse, Zitronensäure + Natron"),
                 ("Was ist die Aktivierungsenergie?", "die Energie, die man zum Start einer Reaktion zuführen muss"),
                 ("Was macht ein Katalysator?", "Er senkt die Aktivierungsenergie, beschleunigt die Reaktion und wird nicht verbraucht."),
                 ("Nenne zwei Metalle im Autokatalysator.", "Platin, Palladium, Rhodium"),
                 ("Warum brennen Holzspäne schneller als ein Holzscheit?", "größere Oberfläche – mehr Teilchen können gleichzeitig reagieren"),
                 ("Wie ändert sich das Tempo bei 10 °C mehr?", "Faustregel: etwa doppelt so schnell")]

STOLPERSTEINE = [("Oxidation = Sauerstoff", "Heute heißt Oxidation **Elektronenabgabe** – Sauerstoff muss nicht dabei sein (Eisen in Kupfersulfat). Kadetten bleiben oft beim alten Begriff."),
                 ("Mittel verwechselt", "Das **Oxidationsmittel wird reduziert**, das **Reduktionsmittel wird oxidiert** – es »bewirkt« beim Partner das Gegenteil. Merksatz: Das Mittel macht es beim anderen."),
                 ("»Verbrennen macht leichter«", "Bei Eisenwolle steigt die Masse (Sauerstoff wird eingebaut); bei Holz scheint sie zu sinken, weil Gase entweichen. Die **Gesamtmasse bleibt erhalten**."),
                 ("Aktivierungsenergie = endotherm", "Auch exotherme Reaktionen brauchen einen Start (Streichholz). Endotherm heißt: Der Vorgang **nimmt insgesamt Wärme auf** – aus der Mischung und der Umgebung (es wird kalt) oder durch ständiges Heizen."),
                 ("Katalysator als Filter oder Verbrauchsstoff", "Der Katalysator **wandelt um** und wird **nicht verbraucht**; er ändert nur den Weg (Aktivierungsenergie), nicht die Energie von Anfang und Ende.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Redox", "Was ist eine Oxidation nach heutiger Sicht?", ["Abgabe von Elektronen", "Aufnahme von Elektronen", "Aufnahme von Protonen", "Abgabe von Sauerstoff"],
  "Oxidation = Elektronenabgabe. Früher meinte man damit nur die Verbindung mit Sauerstoff.", "Buch S. 30"),
 ("Redox", "Was ist eine Reduktion nach heutiger Sicht?", ["Aufnahme von Elektronen", "Abgabe von Elektronen", "Verbindung mit Sauerstoff", "Abkühlen eines Stoffes"],
  "Reduktion = Elektronenaufnahme – sie läuft immer zusammen mit einer Oxidation ab.", "Buch S. 30"),
 ("Redox", "Bei 2 Mg + O₂ → 2 MgO – welcher Stoff wird oxidiert?", ["Magnesium", "Sauerstoff", "Magnesiumoxid", "keiner"],
  "Jedes Mg-Atom gibt 2 Elektronen ab (Mg → Mg²⁺ + 2 e⁻).", "Buch S. 30"),
 ("Redox", "Wie nennt man den Stoff, der Elektronen aufnimmt?", ["Oxidationsmittel", "Reduktionsmittel", "Katalysator", "Enzym"],
  "Das Oxidationsmittel nimmt Elektronen auf und wird dabei selbst reduziert.", "Buch S. 30"),
 ("Redox", "Eisenwolle verbrennt auf der Waage. Was zeigt die Waage danach?", ["mehr als vorher", "weniger als vorher", "genau gleich viel", "null"],
  "Sauerstoff aus der Luft wird eingebaut – es entsteht schwereres Eisenoxid.", "Buch S. 30"),
 ("Redox", "C + 2 CuO → CO₂ + 2 Cu – welcher Stoff wird reduziert?", ["Kupferoxid", "Kohlenstoff", "Kohlenstoffdioxid", "Kupfer"],
  "Kupferoxid gibt seinen Sauerstoff ab, Cu²⁺ nimmt Elektronen auf → Kupfer.", "Buch S. 31"),
 ("Redox", "Welcher Vorgang ist KEINE Redoxreaktion?", ["Eis schmilzt", "Eisen rostet", "Holz brennt", "Ein Apfel wird braun"],
  "Beim Schmelzen ändert sich nur der Aggregatzustand – es entsteht kein neuer Stoff.", "Buch S. 30"),
 ("Rost", "Was braucht Eisen zum Rosten?", ["Wasser und Sauerstoff", "nur Wasser", "nur Sauerstoff", "Wärme und Licht"],
  "Im trockenen Glas und im sauerstoffarmen Wasser unter Öl rostet Eisen kaum.", "Buch S. 98"),
 ("Rost", "Warum schützt eine Zinkschicht das Eisen?", ["Zink ist unedler und wird zuerst oxidiert.", "Zink ist ein Edelmetall.", "Zink zieht Wasser an.", "Zink macht das Eisen magnetisch."],
  "Das unedlere Zink gibt seine Elektronen zuerst ab – es »opfert« sich.", "Buch S. 98"),
 ("Energie", "Was bedeutet exotherm?", ["Energie wird an die Umgebung abgegeben.", "Energie wird aus der Umgebung aufgenommen.", "Es entsteht ein Gas.", "Die Reaktion braucht keinen Start."],
  "ex = hinaus (wie Exit): Die Energie geht nach draußen, meist als Wärme.", "Buch S. 32"),
 ("Energie", "Welche Reaktion ist endotherm?", ["Fotosynthese", "Verbrennung von Holz", "Handwärmer wird warm", "Magnesium verbrennt"],
  "Die Pflanze braucht ständig Lichtenergie von außen.", "Buch S. 32"),
 ("Energie", "Zitronensäure und Natron in Wasser: Das Thermometer zeigt 20 °C → 9 °C. Die Reaktion ist …", ["endotherm", "exotherm", "katalytisch", "eine Oxidation"],
  "Die Lösung kühlt ab – die Reaktion nimmt Wärme aus der Umgebung auf.", "Buch S. 32"),
 ("Energie", "Im Energiediagramm liegen die Endstoffe tiefer als die Ausgangsstoffe. Die Reaktion ist …", ["exotherm", "endotherm", "ohne Energie", "nicht möglich"],
  "Die Energiedifferenz wurde an die Umgebung abgegeben.", "Buch S. 33"),
 ("Energie", "Was ist die Aktivierungsenergie?", ["die Energie zum Start einer Reaktion", "die Energie, die am Ende übrig bleibt", "die Energie im Katalysator", "die Energie des Lichts"],
  "Wie ein Berg, über den die Teilchen zuerst müssen – z. B. das Streichholz beim Lagerfeuer.", "Buch S. 34"),
 ("Katalysator", "Was macht ein Katalysator mit der Aktivierungsenergie?", ["Er senkt sie.", "Er erhöht sie.", "Er verbraucht sie vollständig.", "Er filtert sie heraus."],
  "Mit niedrigerem »Berg« schaffen viel mehr Teilchen den Start – die Reaktion läuft schneller.", "Buch S. 34"),
 ("Katalysator", "Welche Metalle stecken im Autokatalysator?", ["Platin, Palladium, Rhodium", "Eisen, Kupfer, Zink", "Gold, Silber, Blei", "Aluminium und Magnesium"],
  "Die Edelmetalle sitzen fein verteilt in einer porösen Schicht auf einer Keramikwabe.", "Buch S. 35"),
 ("Katalysator", "Wie nennt man Katalysatoren in Lebewesen?", ["Enzyme", "Ionen", "Hormone", "Oxide"],
  "Enzyme wie die Amylase im Speichel sind Biokatalysatoren.", "Buch S. 35"),
 ("Katalysator", "Ein Zuckerwürfel brennt nur, wenn man ihn mit Holzasche bestreut. Welche Rolle hat die Asche?", ["Katalysator – sie senkt die Aktivierungsenergie", "Brennstoff, der mitbrennt", "Löschmittel", "Oxidationsmittel"],
  "Die Asche beschleunigt die Verbrennung und wird nicht verbraucht – wie jeder Katalysator.", "Buch S. 34"),
 ("Tempo", "Warum brennen dünne Holzspäne schneller als ein dicker Scheit?", ["größere Oberfläche", "höhere Dichte", "weniger Sauerstoff", "mehr Wasser"],
  "Je feiner zerteilt, desto mehr Teilchen können gleichzeitig reagieren.", "Buch S. 36"),
 ("Tempo", "Faustregel: Eine Reaktion braucht bei 20 °C 60 s. Wie lange etwa bei 30 °C?", ["30 s", "60 s", "120 s", "6 s"],
  "10 °C wärmer → etwa doppelt so schnell → halbe Zeit.", "Buch S. 36"),
]
