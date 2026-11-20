"""NAWI 3AB · K3.1 Herz-Kreislauf-System + K3.6 Stützsystem und Ergonomie (Trauner Naturwissenschaften HAK 3: Teil III »Organsysteme des Menschen«,
Herz-Kreislauf-System S. 76–85, Stützsystem und Ergonomie S. 107–114) – v1.
Grundlage: Auftrag Stephan 20.11.2026 (beide Themen integriert, 5 Stunden, 23.11.–09.12.2026, Referate 3AK Ernährungstrends/Looksmaxing, 3BK Peptide),
Planübersicht im Chat vom 20.11.2026 mit Stephans Entscheidungen: Termine stimmen, Referate je 10 min mit Brücke, kein Blutdruckgerät (nur Puls),
10 Pflichtaufgaben, KEINE Hühnerknochen (Stephan: »habe keine Knochen«).
Jahresplan v24: Block »C Organsysteme des Menschen«, E8 Herz-Kreislauf (3 Std., K06) + E11 Stützsystem und Ergonomie (2 Std., K06, K07) = 5 Stunden.
Leitidee »Der Körper unter Belastung«: Herz pumpt → Gefäße leiten → Knochen tragen und bilden Blut → Blut transportiert → Muskeln ziehen, Ergonomie schont.
Keine Daten auf den Kadetten-Seiten (Standard 13.11.2026): Termine trägt Prof. HOLZER im Kalender der privaten Lehrerseite ein.
Versuch: K3.1-V1 Puls vor und nach Belastung (= Jahresplan V3.19 ohne Blutdruck – kein Messgerät im Inventar).
Demos: K3.1-D1 Torso · K3.1-D2 Venenklappen am Unterarm · K3.6-D1 Röhrenknochen und Skelett · K3.6-D2 Richtig heben (= Jahresplan V3.22, als Demo).
Weitere Quellen: Hölzel Naturwissenschaften HAK III S. 88–97, 105–110; Expedition Biologie 4 Arbeitsheft S. 21–25, 33–35 (Screenshots von Stephan) – alles in eigenen Worten.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "20.11.2026"
V = "v1"
ORDNER = "3ab-nawi/k3-1-kreislauf"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "3ab-nawi/"
EYEBROW = "NAWI · 3AB · K3.1 Herz-Kreislauf · K3.6 Stützsystem und Ergonomie"
TITEL = "Der Körper unter Belastung – Herz, Blut, Knochen, Muskeln"
KURZTITEL = "Körper unter Belastung"
BUCH = "Buch S. 76–85, 107–114"
KEY = "26-27-3AB-K3.1-Kreislauf-TH-Handy-v1"
LERNSEITE_KEY = "26-27-3AB-K3.1-Kreislauf-Lernseite-Check-v1"
PRAEFIX = "26-27-3AB-K3.1-3.6-Koerper"
KLASSEN = ["3AK", "3BK"]
GRUPPEN = 6            # Gruppenarbeit Skelett: sechs Körperregionen (Gruppengröße ergibt sich aus der Klassengröße)
STUNDEN = 5

VS = {"K3.1-V1": {"titel": "Puls vor und nach Belastung", "jp": "V3.19 (angepasst: nur Puls, kein Blutdruckmessgerät im Inventar)", "stunde": 2, "aufgabe": 4}}
DEMOS = {"K3.1-D1": {"titel": "Das Herz im Torso: Lage, Größe, vier Räume", "jp": "Torso 18-teilig (Inventar #148)", "stunde": 1},
         "K3.1-D2": {"titel": "Venenklappen am eigenen Unterarm", "jp": "Expedition Biologie 4 AH S. 35/4 (nicht im Jahresplan)", "stunde": 2},
         "K3.6-D1": {"titel": "Skelett-Modell: leicht und stabil", "jp": "Homo-Skelett (#66), Abbildung Buch S. 108 (kein echter Knochen – Stephan 20.11.2026)", "stunde": 3},
         "K3.6-D2": {"titel": "Richtig heben: Last nah oder weit weg?", "jp": "= Jahresplan V3.22 (als Demo, ohne Fotos)", "stunde": 5}}

STUNDENTITEL = {1: "Der Motor im Brustkorb: Wie dein Herz pumpt",
                2: "Puls-Check: Was dein Herz beim Training macht",
                3: "Gerüst mit Bauplan: Knochen und Gelenke",
                4: "Rotes Wunder: Was im Blut steckt",
                5: "Kraft, Hebel, Haltung: Muskeln und Ergonomie"}
STUNDENNAME = {n: f"Stunde {n} · {t}" for n, t in STUNDENTITEL.items()}

STATIONEN = ["rechte Kammer", "Lungenarterie", "Lungenkapillaren", "Lungenvene", "linker Vorhof", "linke Kammer"]
GELENK = ["Kugelgelenk", "Scharniergelenk", "Drehgelenk"]
FUNKTION = ["verbindet zwei Knochen miteinander", "verbindet Muskel und Knochen", "verringert die Reibung im Gelenk und dämpft Stöße",
            "erzeugt Kraft, indem er sich verkürzt", "gibt dem Körper Festigkeit"]
BESTAND = ["transportieren Sauerstoff", "wehren Krankheitserreger ab", "sorgen für den Wundverschluss", "transportiert gelöste Stoffe und Wärme"]


def _st(i, richtig):
    return ["s%d" % i, "%s) %d. Station" % ("defghi"[i - 1], i + 1), [richtig] + [x for x in STATIONEN if x != richtig]]


def _gel(fid, buchst, name, richtig):
    return [fid, "%s) %s" % (buchst, name), [richtig] + [x for x in GELENK if x != richtig]]


def _fun(fid, buchst, organ, richtig):
    return [fid, "%s) %s …" % (buchst, organ), [richtig] + [x for x in FUNKTION if x != richtig]]


def _best(fid, buchst, name, richtig):
    return [fid, "%s) %s …" % (buchst, name), [richtig] + [x for x in BESTAND if x != richtig]]


# ================================================================ Aufgaben
T = [
 # --------------------------------------------------------------- Stunde 1
 {"id": "v0", "nr": 1, "title": "Was glaubst du?", "src": "Buch S. 76, 108", "own": True, "tag": "Vorhersage", "h": 1, "zeit": 2,
  "q": "Zwei Schätzfragen zum Start – ohne Punkte, ohne »richtig« oder »falsch«. Entscheide dich einmal. In Stunde 5 schaust du nach, was du heute gedacht hast.",
  "hint": "Einfach tippen, was du vermutest. Deine Antwort bleibt gespeichert.",
  "type": "multi", "vorhersage": True,
  "fields": [["p1", "a) Wie viel Blut pumpt dein Herz in Ruhe an EINEM Tag durch den Körper?",
              ["rund 70 Liter", "rund 700 Liter", "rund 7000 Liter"], False],
             ["p2", "b) Was ist bei einem jungen Erwachsenen schwerer?",
              ["das Skelett", "alle Skelettmuskeln zusammen", "beide sind gleich schwer"], False]],
  "chk": {},
  "aufloesung": [["p1", "rund 7000 Liter", "Rund 70 ml pro Schlag mal etwa 70 Schläge pro Minute sind knapp 5 Liter pro Minute – über einen Tag rund 7000 Liter. Das ist ungefähr der Inhalt von 50 Badewannen."],
                 ["p2", "alle Skelettmuskeln zusammen", "Die Skelettmuskeln machen bei Erwachsenen rund 40 % der Körpermasse aus (Buch S. 110: bis zu 45 %), das Skelett nur etwa 15 %. Knochen sind leicht gebaut – wie ein Fachwerk."]],
  "sol": [["Auflösung", ["a) rund 7000 Liter: 70 ml · 70 Schläge pro Minute ≈ 5 l pro Minute, mal 1440 Minuten ≈ 7000 l pro Tag.",
                         "b) die Muskeln: rund 40 % der Körpermasse, das Skelett nur etwa 15 %."]]],
  "tipps": [], "tip": ["Das Herz", "theorie.html#herz"]},

 {"id": "a1", "nr": 2, "title": "Das Herz: vier Räume, zwei Kreisläufe", "src": "Buch S. 77–78 · Hölzel S. 89–90", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 9, "marke": "SELBSTSTUDIUM",
  "q": "Lies im Buch S. 77 den Text unter der Herz-Abbildung und die Tabelle »Aufgabe der beiden Herzhälften« (3 min). Markiere, wo das Blut die Lunge verlässt. "
       "Dann: a) bis c) zum Bau des Herzens. d) bis i): Das Blut kommt aus dem Körper in den rechten Vorhof. Wähle für jede Station, wohin es als Nächstes fließt, bis es wieder zum Körper hinaus will. j) und k) zu den beiden Herzhälften.",
  "hint": "Erst durch die rechte Herzhälfte zur Lunge, dann zurück in die linke Hälfte. Bei jedem Schritt geht es durch eine Klappe oder ein Gefäß.",
  "type": "multi",
  "fields": [["systole", "a) Was passiert in der Systole?",
              ["Die Herzkammern ziehen sich zusammen und pressen das Blut in die Arterien", "Die Herzkammern erschlaffen und füllen sich mit Blut", "Die Vorhöfe ziehen sich zusammen, die Kammern ruhen"]],
             ["segel", "b) Wo liegen die Segelklappen?",
              ["zwischen Vorhof und Kammer", "zwischen Kammer und Arterie", "in den Venen der Beine"]],
             ["klappen", "c) Wozu hat das Herz Klappen?",
              ["Sie lassen das Blut nur in eine Richtung fließen – wie ein Ventil", "Sie erzeugen den Herzschlag", "Sie filtern Krankheitserreger aus dem Blut"]],
             _st(1, STATIONEN[0]), _st(2, STATIONEN[1]), _st(3, STATIONEN[2]), _st(4, STATIONEN[3]), _st(5, STATIONEN[4]), _st(6, STATIONEN[5]),
             ["links", "j) Welche Herzhälfte pumpt sauerstoffreiches Blut in den Körperkreislauf?", ["die linke", "die rechte", "beide abwechselnd"]],
             ["wand", "k) Die Wand der linken Kammer ist viel dicker als die der rechten. Warum?",
              ["Sie muss das Blut durch den ganzen Körper drücken – das braucht mehr Druck", "Links ist mehr Platz im Brustkorb", "Links fließt mehr Blut als rechts"]]],
  "chk": {"systole": {"sel": "Die Herzkammern ziehen sich zusammen und pressen das Blut in die Arterien"},
          "segel": {"sel": "zwischen Vorhof und Kammer"},
          "klappen": {"sel": "Sie lassen das Blut nur in eine Richtung fließen – wie ein Ventil"},
          "s1": {"sel": STATIONEN[0]}, "s2": {"sel": STATIONEN[1]}, "s3": {"sel": STATIONEN[2]},
          "s4": {"sel": STATIONEN[3]}, "s5": {"sel": STATIONEN[4]}, "s6": {"sel": STATIONEN[5]},
          "links": {"sel": "die linke"},
          "wand": {"sel": "Sie muss das Blut durch den ganzen Körper drücken – das braucht mehr Druck"}},
  "fb": {"systole": {"Die Herzkammern erschlaffen und füllen sich mit Blut": "Das ist die Diastole – die Erholungs- und Füllphase.",
                     "Die Vorhöfe ziehen sich zusammen, die Kammern ruhen": "Das ist kurz vor der Systole. In der Systole arbeiten die Kammern."},
         "segel": {"zwischen Kammer und Arterie": "Dort sitzen die Taschenklappen.",
                   "in den Venen der Beine": "Venen haben eigene Klappen. Die Segelklappen gehören zum Herzen."},
         "klappen": {"Sie erzeugen den Herzschlag": "Den Takt geben spezielle Muskelzellen im Herzen vor, nicht die Klappen.",
                     "Sie filtern Krankheitserreger aus dem Blut": "Das machen weiße Blutkörperchen. Klappen sind Ventile."},
         "links": {"die rechte": "Die rechte Hälfte bekommt das sauerstoffarme Blut aus dem Körper und schickt es zur Lunge.",
                   "beide abwechselnd": "Beide Hälften schlagen zwar im gleichen Takt, haben aber verschiedene Aufgaben."},
         "wand": {"Links ist mehr Platz im Brustkorb": "Es geht nicht um Platz, sondern um die Arbeit, die der Muskel leisten muss.",
                  "Links fließt mehr Blut als rechts": "Beide Kammern pumpen pro Schlag gleich viel Blut – sonst würde es sich irgendwo stauen."}},
  "sol": [["Lösung", ["a) Systole: Die Kammern ziehen sich zusammen und pressen das Blut in Aorta und Lungenarterie (Diastole = Erschlaffen und Füllen).",
                      "b) Segelklappen zwischen Vorhof und Kammer; Taschenklappen zwischen Kammer und Arterie.",
                      "c) Klappen sind Ventile: Blut fließt nur in eine Richtung (Hölzel vergleicht sie mit dem Ventil eines Fahrradreifens).",
                      "d)–i) rechter Vorhof → rechte Kammer → Lungenarterie → Lungenkapillaren (CO₂ ab, O₂ auf) → Lungenvene → linker Vorhof → linke Kammer → Aorta.",
                      "j) die linke Herzhälfte.",
                      "k) Die linke Kammer muss das Blut durch den ganzen Körperkreislauf drücken, die rechte nur durch die nahe Lunge – darum mehr Muskel."]]],
  "tipps": ["Stell dir eine Acht vor: Die eine Schleife geht zur Lunge, die andere durch den Körper. In der Mitte sitzt das Herz – rechts für die Lunge, links für den Körper.",
            "k1",
            "Lies im Buch S. 77 die Tabelle »Aufgabe der beiden Herzhälften« und auf S. 78 die Kästen »Vorhof« / »Kammer« und »Klappen«."],
  "tip": ["Das Herz", "theorie.html#herz"]},

 {"id": "a2", "nr": 3, "title": "Handschrift: dein Kreislauf-Schema", "src": "Buch S. 77, 79–80 · Buch-Aufgabe S. 81/2", "own": False, "tag": "Stunde 1", "h": 1, "zeit": 6, "marke": "SELBSTSTUDIUM",
  "type": "sketch",
  "q": "Nimm ein leeres oder kariertes Blatt und schreib oben das Datum. Zeichne mit der Hand ein einfaches Schema des Blutkreislaufs: "
       "1) das Herz als Kästchen mit vier Räumen (rechts und links beschriften!), 2) oben die Lunge, unten den Körper, 3) Pfeile für die Fließrichtung, "
       "4) sauerstoffreiches Blut ROT, sauerstoffarmes BLAU, 5) beschrifte Lungenkreislauf, Körperkreislauf, Aorta und Lungenarterie. "
       "Fotografiere das Blatt und lade das Foto hier hoch. Das Blatt kommt danach in deine Mappe. Dann beantworte a).",
  "hint": "Wo steht's? Theorie-Teil 2 »Zwei Kreisläufe« und Buch S. 79–80. Vorlage zum Vergleichen: die Kreislauf-Animation auf der Theorie-Karte. Foto: Blatt flach, ganzes Blatt, keine Gesichter.",
  "fields": [["arterie", "a) Ein Gefäß führt sauerstoffARMES Blut und heißt trotzdem Arterie. Welches?",
              ["die Lungenarterie", "die Aorta", "die untere Hohlvene"]]],
  "chk": {"arterie": {"sel": "die Lungenarterie"}},
  "fb": {"arterie": {"die Aorta": "Die Aorta führt sauerstoffreiches Blut aus der linken Kammer in den Körper.",
                     "die untere Hohlvene": "Die Hohlvene führt sauerstoffarmes Blut – aber sie ist eine Vene (zum Herzen hin)."}},
  "sol": [["Lösung", ["Schema: Herz mit rechter und linker Hälfte. Rechte Kammer → Lungenarterie (blau) → Lunge → Lungenvene (rot) → linker Vorhof. Linke Kammer → Aorta (rot) → Körper → Hohlvenen (blau) → rechter Vorhof.",
                      "Achtung beim Zeichnen: Im Schema steht »rechts« vom Patienten aus gesehen – im Buch also links im Bild.",
                      "a) die Lungenarterie: Arterie heißt »vom Herzen weg«, nicht »sauerstoffreich«. Umgekehrt führt die Lungenvene sauerstoffreiches Blut."]]],
  "tipps": ["Zeichne zuerst nur das Herz als Kästchen mit Kreuz in der Mitte. Oben ein Kreis = Lunge, unten ein großer Kreis = Körper. Dann die Pfeile.",
            "k2",
            "Schau dir im Buch S. 77 rechts die kleine Kreislauf-Skizze an (Lungenkreislauf oben, Körperkreislauf unten)."],
  "tip": ["Zwei Kreisläufe", "theorie.html#kreislauf"]},

 # --------------------------------------------------------------- Stunde 2
 {"id": "a3", "nr": 4, "title": "VERSUCH K3.1-V1: Puls vor und nach Belastung", "src": "Buch S. 80 (Versuch »Pulszählung«)", "own": False, "tag": "Stunde 2", "h": 2, "zeit": 15, "marke": "VERSUCH",
  "versuch": "K3.1-V1",
  "q": "Ihr arbeitet zu zweit, aber jeder misst seinen EIGENEN Puls. Der Partner hält die Zeit mit der Handy-Stoppuhr und sagt »Start« und »Stopp«. "
       "Mitmachen ist freiwillig: Wer erkältet ist, Beschwerden an Herz, Lunge oder Knie hat oder nicht will, muss keinen Grund nennen. Er ist nur Zeitnehmer und schreibt bei b) bis d) »nicht gemessen«. So geht es:\n"
       "1) Alle sitzen 2 Minuten ruhig. Such den Puls an der Innenseite des Handgelenks, daumenseitig (mit zwei Fingern, nicht mit dem Daumen).\n"
       "2) 30 Sekunden zählen, mal 2 = Ruhepuls pro Minute. Wert in b).\n"
       "3) Alle machen gleichzeitig 20 Kniebeugen in ruhigem Tempo.\n"
       "4) Sofort hinsetzen, wieder 30 Sekunden zählen, mal 2. Wert in c).\n"
       "5) 3 Minuten ruhig sitzen, dann noch einmal messen. Wert in d). In der Pause kannst du schon f) und g) lösen.\n"
       "6) Die Klasse sammelt die Werte ohne Namen.",
  "hint": "Puls nicht mit dem Daumen fühlen – der hat selbst einen spürbaren Puls. Wir tasten nur am Handgelenk.",
  "type": "multi",
  "fields": [["grp", "a) Zeitnehmer war (Vorname genügt)"],
             ["ruhe", "b) Mein Ruhepuls (Schläge pro Minute – oder »nicht gemessen«)"],
             ["nach", "c) Mein Puls direkt nach den Kniebeugen (Schläge pro Minute – oder »nicht gemessen«)"],
             ["erholt", "d) Mein Puls nach 3 Minuten Pause (Schläge pro Minute – oder »nicht gemessen«)"],
             ["beob", "e) Was hast du beobachtet? (1–2 Sätze; wer nicht gemessen hat: die Klassenwerte)"],
             ["warum", "f) Warum schlägt das Herz bei Belastung schneller?",
              ["Die arbeitenden Muskeln brauchen mehr Sauerstoff – also muss mehr Blut pro Minute fließen", "Das Herz wird bei Bewegung kleiner", "Das Blut wird bei Bewegung dünner und fließt schneller von selbst"]],
             ["diagnose", "g) Was darf man aus EINER solchen Messung nicht ableiten?",
              ["eine medizinische Diagnose oder eine Fitness-Note", "dass der Puls bei Belastung steigt", "dass sich der Puls in der Pause wieder senkt"]],
             ["schluss", "h) Was bedeutet das für einen langen Marsch mit Gepäck oder für dein Training? (1 Satz)"]],
  "chk": {"warum": {"sel": "Die arbeitenden Muskeln brauchen mehr Sauerstoff – also muss mehr Blut pro Minute fließen"},
          "diagnose": {"sel": "eine medizinische Diagnose oder eine Fitness-Note"},
          "beob": {"kw": [["Wert genannt", r"\d|stieg|steig|hoeher|höher|schneller|mehr|sank|gesunken|langsamer|wieder"]], "man": True},
          "schluss": {"kw": [["Belastung / Tempo", r"tempo|pause|langsam|einteil|trink|training|ausdauer|trainier|herz|puls|sauerstoff|kondition|steigern|regelm"]], "man": True}},
  "fb": {"warum": {"Das Herz wird bei Bewegung kleiner": "Das Herz ändert seine Größe nicht. Es schlägt schneller – und meist auch kräftiger.",
                   "Das Blut wird bei Bewegung dünner und fließt schneller von selbst": "Das Blut fließt nur, weil das Herz pumpt. Der Bedarf der Muskeln steigt."},
         "diagnose": {"dass der Puls bei Belastung steigt": "Genau das zeigt die Messung. Gefragt ist, was man NICHT daraus schließen darf.",
                      "dass sich der Puls in der Pause wieder senkt": "Auch das zeigt die Messung. Gefragt ist, was man NICHT daraus schließen darf."}},
  "sol": [["Erwartung (Beispielwerte – eure Werte sind anders)",
           ["b) Ruhepuls meist 60–80 pro Minute (Buch S. 80), Sportler oft darunter. c) nach 20 Kniebeugen etwa 100–140. d) nach 3 Minuten wieder nahe am Ruhewert.",
            "f) Die Muskeln arbeiten und brauchen mehr Sauerstoff und Nährstoffe; das Herz schlägt schneller (und kräftiger), damit mehr Blut pro Minute fließt.",
            "g) Eine einzelne Messung mit Fingerzählen ist ungenau und keine Diagnose. Ein schneller Rückgang in der Pause ist höchstens ein grober Hinweis auf gute Ausdauer.",
            "h) z. B.: Gleichmäßiges Tempo und Pausen helfen; regelmäßiges Ausdauertraining senkt den Ruhepuls, weil das Herz pro Schlag mehr Blut schafft."]]],
  "tipps": ["Vergleiche b), c) und d): Wo ist der höchste Wert? Wie schnell kommt der Puls zurück?",
            "k4",
            "Lies im Buch S. 80 den Kasten »Versuch – Pulszählung« und den Abschnitt »3.3 Puls«."],
  "tip": ["Puls und Blutdruck", "theorie.html#puls"]},

 {"id": "a4", "nr": 5, "title": "Gefäße, Herzminutenvolumen, Blutdruck", "src": "Buch S. 79–81", "own": True, "tag": "Stunde 2", "h": 2, "zeit": 8, "marke": "SELBSTSTUDIUM",
  "sim": ["hmv"],
  "q": "a) bis c): kurze Auswahlfragen zu den Blutgefäßen. d) bis f): Rechne mit Herzminutenvolumen = Schlagvolumen · Puls. Schreib die Einheit dazu. g) zum Blutdruck.",
  "hint": "Schlagvolumen in ml mal Schläge pro Minute ergibt ml pro Minute. 1000 ml = 1 l.",
  "type": "multi",
  "fields": [["arterie", "a) Was macht ein Blutgefäß zur Arterie?",
              ["Es führt das Blut vom Herzen weg", "Es führt immer sauerstoffreiches Blut", "Es hat Klappen gegen den Rückfluss"]],
             ["kapillar", "b) Wo werden Sauerstoff und Nährstoffe an die Zellen abgegeben?",
              ["in den Kapillaren", "in der Aorta", "in den Herzklappen"]],
             ["venenklappe", "c) Wozu haben die Venen in den Beinen Klappen?",
              ["Damit das Blut nicht zurück in die Füße sackt", "Damit der Blutdruck in den Beinen steigt", "Damit sich dort Sauerstoff sammelt"]],
             ["hmv", "d) In Ruhe: Schlagvolumen 70 ml, Puls 72 Schläge pro Minute. Wie viele Liter pumpt das Herz pro Minute? (Zahl und Einheit l)"],
             ["tag", "e) Wie viele Liter sind das an einem ganzen Tag (24 Stunden)? Rechne mit deinem Ergebnis aus d)."],
             ["sport", "f) Beim Laufen: Schlagvolumen 120 ml, Puls 150 pro Minute. Wie viele Liter pro Minute? (Zahl und Einheit l)"],
             ["druck", "g) Ein Blutdruck von 120/80 mmHg bedeutet:",
              ["120 beim Auspressen der Kammern (systolisch), 80 in der Füllphase (diastolisch)", "120 Herzschläge, 80 Atemzüge", "120 im rechten Arm, 80 im linken Arm"]]],
  "chk": {"arterie": {"sel": "Es führt das Blut vom Herzen weg"},
          "kapillar": {"sel": "in den Kapillaren"},
          "venenklappe": {"sel": "Damit das Blut nicht zurück in die Füße sackt"},
          "hmv": {"num": 5.04, "unit": "l", "tol": 0.1},
          "tag": {"num": 7257.6, "unit": "l", "tol": 150},
          "sport": {"num": 18, "unit": "l", "tol": 0.36},
          "druck": {"sel": "120 beim Auspressen der Kammern (systolisch), 80 in der Füllphase (diastolisch)"}},
  "fb": {"arterie": {"Es führt immer sauerstoffreiches Blut": "Die Lungenarterie führt sauerstoffarmes Blut. Entscheidend ist die Richtung: vom Herzen weg.",
                     "Es hat Klappen gegen den Rückfluss": "Klappen haben die Venen. Arterien haben eine dicke, elastische Wand."},
         "kapillar": {"in der Aorta": "Die Aortenwand ist viel zu dick für den Stoffaustausch.",
                      "in den Herzklappen": "Klappen sind Ventile, keine Austauschstellen."},
         "venenklappe": {"Damit der Blutdruck in den Beinen steigt": "In den Venen ist der Druck niedrig – darum brauchen sie die Klappen als Rückschlagventile.",
                         "Damit sich dort Sauerstoff sammelt": "Die Klappen haben mit Sauerstoff nichts zu tun. Sie bestimmen die Richtung."},
         "hmv": [[5040, "Das sind Milliliter. Teile durch 1000, dann hast du Liter."], [0.97, "Du hast geteilt. Es heißt Schlagvolumen MAL Puls."]],
         "tag": [[302.4, "Ein Tag hat 24 Stunden mit je 60 Minuten – also 1440 Minuten."], [120.96, "Du hast nur mit 24 multipliziert. Ein Tag hat 1440 Minuten."]],
         "sport": [[18000, "Das sind Milliliter. Teile durch 1000."], [270, "Du hast addiert. Es heißt Schlagvolumen MAL Puls."]],
         "druck": {"120 Herzschläge, 80 Atemzüge": "Blutdruck ist ein Druck in mmHg, keine Anzahl von Schlägen.",
                   "120 im rechten Arm, 80 im linken Arm": "Beide Werte misst man am selben Arm: einer beim Auspressen, einer in der Füllphase."}},
  "sol": [["Lösung", ["a) vom Herzen weg (Venen: zum Herzen hin).",
                      "b) in den Kapillaren – ihre Wand ist hauchdünn.",
                      "c) Venenklappen sind Rückschlagventile: Das Blut kann nur Richtung Herz. Die Beinmuskeln drücken die Venen zusammen (Muskelpumpe).",
                      "d) 70 ml · 72 = 5040 ml = 5,04 l pro Minute.",
                      "e) 5,04 l · 1440 = 7257,6 l ≈ 7300 l pro Tag.",
                      "f) 120 ml · 150 = 18 000 ml = 18 l pro Minute – mehr als dreimal so viel wie in Ruhe.",
                      "g) systolisch (Kammern pressen) 120, diastolisch (Füllphase) 80 mmHg. Optimal sind Werte unter 120 zu 80."]]],
  "tipps": ["Rechne d) in zwei Schritten: erst ml pro Minute, dann durch 1000.",
            "k3",
            "Lies im Buch S. 79 die Tabelle »Unterschiede zwischen Arterien und Venen« und auf S. 81 den Kasten »Beispiel« zum Herzminutenvolumen."],
  "tip": ["Blutgefäße", "theorie.html#gefaesse"]},

 # --------------------------------------------------------------- Stunde 3
 {"id": "a5", "nr": 6, "title": "Bauplan: Knochen, Sehne, Band, Knorpel", "src": "Buch S. 108–109 · Hölzel S. 105–106, Aufgabe K 3.32", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 8, "marke": "SELBSTSTUDIUM",
  "q": "Lies im Buch S. 108 den Abschnitt »1.1.1 Bau der Knochen am Beispiel des Röhrenknochens« mit der Abbildung (3 min). "
       "a) bis e): Ordne jedem Teil des Bewegungsapparats seine Aufgabe zu. f) bis h): drei Fragen zum Röhrenknochen.",
  "hint": "Sehne und Band klingen ähnlich: Die SEHNE hängt am Muskel, das BAND hält Knochen zusammen.",
  "type": "multi",
  "fields": [_fun("band", "a", "Ein Band", FUNKTION[0]), _fun("sehne", "b", "Eine Sehne", FUNKTION[1]), _fun("knorpel", "c", "Der Gelenkknorpel", FUNKTION[2]),
             _fun("muskel", "d", "Ein Muskel", FUNKTION[3]), _fun("knochen", "e", "Ein Knochen", FUNKTION[4]),
             ["fuge", "f) Wo wächst ein Röhrenknochen in die Länge?", ["an der Wachstumsfuge nahe den Enden", "überall gleichmäßig", "in der Mitte des Knochenschafts"]],
             ["mark", "g) Wo werden rote Blutkörperchen gebildet?", ["im roten Knochenmark", "in der Beinhaut", "im Gelenkknorpel"]],
             ["leicht", "h) Warum ist das Innere des Knochens wie ein Gerüst aus Bälkchen gebaut?",
              ["Material nur dort, wo Kräfte wirken – leicht und trotzdem stabil", "Damit der Knochen leichter bricht", "Damit dort Luft zum Atmen gespeichert wird"]]],
  "chk": {"band": {"sel": FUNKTION[0]}, "sehne": {"sel": FUNKTION[1]}, "knorpel": {"sel": FUNKTION[2]},
          "muskel": {"sel": FUNKTION[3]}, "knochen": {"sel": FUNKTION[4]},
          "fuge": {"sel": "an der Wachstumsfuge nahe den Enden"},
          "mark": {"sel": "im roten Knochenmark"},
          "leicht": {"sel": "Material nur dort, wo Kräfte wirken – leicht und trotzdem stabil"}},
  "fb": {"fuge": {"überall gleichmäßig": "In die Länge wächst der Knochen nur an einer bestimmten Knorpelzone.",
                  "in der Mitte des Knochenschafts": "Der Schaft wächst nicht in die Länge – das passiert nahe den Enden."},
         "mark": {"in der Beinhaut": "Die Beinhaut ernährt den Knochen und hilft beim Heilen. Blut wird woanders gebildet.",
                  "im Gelenkknorpel": "Knorpel hat nicht einmal Blutgefäße."},
         "leicht": {"Damit der Knochen leichter bricht": "Im Gegenteil: Die Bälkchen folgen genau den Kraftlinien.",
                    "Damit dort Luft zum Atmen gespeichert wird": "Zwischen den Bälkchen liegt rotes Knochenmark, keine Luft."}},
  "sol": [["Lösung", ["a) Band: verbindet Knochen mit Knochen. b) Sehne: verbindet Muskel und Knochen (z. B. Achillessehne). c) Knorpel: verringert Reibung, dämpft Stöße. "
                      "d) Muskel: erzeugt Kraft durch Verkürzen. e) Knochen: gibt Festigkeit (und dem Muskel Widerstand).",
                      "f) an der Wachstumsfuge (Knorpelzone nahe den Enden). Sie verknöchert erst gegen Ende der Pubertät.",
                      "g) im roten Knochenmark zwischen den Knochenbälkchen (bei Erwachsenen v. a. in platten und kurzen Knochen und an den Enden der Röhrenknochen).",
                      "h) Leichtbau: Die Bälkchen liegen entlang der Biege- und Druckbelastung – wie bei einem Kran oder Flugzeugflügel."]]],
  "tipps": ["Denk an einen Kran: Der Motor (Muskel) zieht am Seil (Sehne), das Seil hängt am Ausleger (Knochen). Die Laschen an den Gelenkbolzen (Bänder) halten die Teile zusammen.",
            "k5",
            "Lies im Buch S. 108 die Beschriftungen beim Röhrenknochen (Wachstumsfuge, Beinhaut, Knochenmarkhöhle, Knochenbälkchen)."],
  "tip": ["Knochen", "theorie.html#knochen"]},

 {"id": "a6", "nr": 7, "title": "GRUPPENARBEIT: Skelett-Rallye", "src": "Buch S. 109–110 · Buch-Aufgaben S. 110/1 und 110/4", "own": False, "tag": "Stunde 3", "h": 3, "zeit": 13, "marke": "GRUPPENARBEIT",
  "rollen": [["GRUPPE 1 · Kopf und Hals", "Schädel, Unterkiefer, Halswirbel – welches Gelenk erlaubt »Nein« schütteln?"],
             ["GRUPPE 2 · Schulter und Oberarm", "Schlüsselbein, Schulterblatt, Oberarmknochen – Schultergelenk"],
             ["GRUPPE 3 · Ellbogen und Unterarm", "Elle, Speiche – Ellbogen und die Drehung der Hand"],
             ["GRUPPE 4 · Hand", "Handwurzel-, Mittelhand-, Fingerknochen – Fingergelenke"],
             ["GRUPPE 5 · Becken und Oberschenkel", "Becken, Oberschenkelknochen – Hüftgelenk"],
             ["GRUPPE 6 · Knie und Fuß", "Kniescheibe, Schienbein, Wadenbein, Fußknochen"]],
  "q": "Jede Gruppe bekommt eine Körperregion (Karten oben). 1) Sucht eure Knochen am Skelett-Modell und ertastet sie am eigenen Körper. "
       "2) Schreibt in b) mindestens drei Knochen eurer Region. 3) Bestimmt die Gelenke c) bis h) – das macht JEDE Gruppe, nicht nur eure Region. "
       "4) Zum Schluss zeigt jede Gruppe in 30 Sekunden am Skelett: unsere Knochen, unser wichtigstes Gelenk, sein Gelenktyp. Jeder trägt die Antworten selbst ein.",
  "hint": "Bewege das Gelenk an dir selbst: Geht es in alle Richtungen (Kugel), nur auf und zu (Scharnier) oder dreht sich ein Knochen um den anderen (Dreh)?",
  "type": "multi",
  "fields": [["grp", "a) Gruppe Nr. · mit (Vornamen genügen)"],
             ["region", "b) Diese Knochen unserer Region haben wir gefunden (mindestens drei)"],
             _gel("schulter", "c", "Schultergelenk", "Kugelgelenk"),
             _gel("ellbogen", "d", "Ellbogengelenk (Beugen und Strecken)", "Scharniergelenk"),
             _gel("speiche", "e", "Gelenk zwischen Elle und Speiche (Hand drehen)", "Drehgelenk"),
             _gel("huefte", "f", "Hüftgelenk", "Kugelgelenk"),
             _gel("finger", "g", "Mittel- oder Endgelenk eines Fingers", "Scharniergelenk"),
             _gel("hals", "h", "Gelenk zwischen 1. und 2. Halswirbel (»Nein« schütteln)", "Drehgelenk"),
             ["schmiere", "i) Wozu dient die Gelenkschmiere?",
              ["Sie ernährt den Knorpel und lässt die Gelenkflächen gleiten", "Sie klebt die Knochen zusammen", "Sie bildet neue Knochenzellen"]]],
  "chk": {"region": {"kw": [["Knochen genannt", r"knochen|schaedel|schädel|kiefer|wirbel|schlüsselbein|schluesselbein|schulterblatt|oberarm|elle|speiche|handwurzel|mittelhand|finger|becken|oberschenkel|kniescheibe|schienbein|wadenbein|fuss|fuß|ferse|zehe"]], "man": True},
          "schulter": {"sel": "Kugelgelenk"}, "ellbogen": {"sel": "Scharniergelenk"}, "speiche": {"sel": "Drehgelenk"},
          "huefte": {"sel": "Kugelgelenk"}, "finger": {"sel": "Scharniergelenk"}, "hals": {"sel": "Drehgelenk"},
          "schmiere": {"sel": "Sie ernährt den Knorpel und lässt die Gelenkflächen gleiten"}},
  "fb": {"schulter": {"Scharniergelenk": "Probier es: Du kannst den Arm nach vorne, hinten, zur Seite heben und kreisen – das schafft kein Scharnier.",
                      "Drehgelenk": "Beim Drehgelenk dreht sich ein Knochen um den anderen. Die Schulter kann viel mehr."},
         "ellbogen": {"Kugelgelenk": "Beim Beugen und Strecken geht der Unterarm nur auf und zu – wie eine Tür.",
                      "Drehgelenk": "Das Drehen der Hand passiert zwischen Elle und Speiche. Gefragt ist Beugen und Strecken."},
         "speiche": {"Kugelgelenk": "Die Speiche dreht sich um die Elle – sie kreist nicht in alle Richtungen.",
                     "Scharniergelenk": "Halt den Ellbogen still und dreh die Handfläche nach oben und unten: Da klappt nichts auf und zu."},
         "huefte": {"Scharniergelenk": "Das Bein kann nach vorne, hinten und zur Seite – also mehr als ein Scharnier.",
                    "Drehgelenk": "Der Oberschenkelkopf ist eine Kugel in einer Pfanne."},
         "finger": {"Kugelgelenk": "Die mittleren und vorderen Fingergelenke gehen nur auf und zu.",
                    "Drehgelenk": "Die Fingerglieder drehen sich nicht umeinander."},
         "hals": {"Kugelgelenk": "Beim »Nein«-Schütteln dreht sich der Kopf um einen Zapfen des 2. Halswirbels.",
                  "Scharniergelenk": "Nicken wäre eher auf und zu. Beim »Nein« drehst du."},
         "schmiere": {"Sie klebt die Knochen zusammen": "Zusammengehalten wird das Gelenk von Kapsel und Bändern.",
                      "Sie bildet neue Knochenzellen": "Das macht die Beinhaut. Die Gelenkschmiere ist eine Flüssigkeit."}},
  "sol": [["Lösung", ["b) z. B. Gruppe 2: Schlüsselbein, Schulterblatt, Oberarmknochen · Gruppe 3: Oberarmknochen, Elle, Speiche · Gruppe 4: Handwurzel-, Mittelhand-, Fingerknochen · "
                      "Gruppe 5: Becken, Oberschenkelknochen · Gruppe 6: Kniescheibe, Schienbein, Wadenbein, Fußwurzel-, Mittelfuß-, Zehenknochen · Gruppe 1: Schädel, Unterkiefer, Halswirbel.",
                      "c) Kugelgelenk · d) Scharniergelenk · e) Drehgelenk · f) Kugelgelenk · g) Scharniergelenk (mittlere und vordere Fingergelenke) · h) Drehgelenk.",
                      "i) Die Gelenkschmiere ernährt den Knorpel und verringert die Reibung.",
                      "Hinweis: Das Knie ist streng genommen ein Dreh-Scharnier-Gelenk (im gebeugten Zustand etwas drehbar) – darum fragen wir es nicht ab."]]],
  "tipps": ["Probier jedes Gelenk an dir aus: Kreisen? Nur auf und zu? Oder drehen?",
            "k6",
            "Lies im Buch S. 109 die Tabelle »Gelenkstypen« mit den Beispielen."],
  "tip": ["Gelenke", "theorie.html#gelenke"]},

 # --------------------------------------------------------------- Stunde 4
 {"id": "a7", "nr": 8, "title": "Blut im Labor: Bestandteile, Befund, Blutgruppen", "src": "Buch S. 81–85 · Expedition Bio 4 AH S. 33", "own": True, "tag": "Stunde 4", "h": 4, "zeit": 14, "marke": "SELBSTSTUDIUM",
  "sim": ["blutgruppe"],
  "q": "Lies im Buch S. 82 den Kasten zu den Bestandteilen des Blutes (2 min). a) bis d): Was leisten die Bestandteile? "
       "e) und f): Ein Blutbefund (Werte für Männer laut Buch S. 83). g) bis i): Blutgruppen-Test im Labor. j) und k): Wer darf welche Blutkonserve bekommen? (Den Rhesusfaktor lassen wir hier weg.)",
  "hint": "Bei den Blutgruppen: Verklumpt das Blut mit Anti-A-Serum, sitzt das Antigen A auf den roten Blutkörperchen.",
  "type": "multi",
  "fields": [_best("ery", "a", "Rote Blutkörperchen (Erythrozyten)", BESTAND[0]),
             _best("leuko", "b", "Weiße Blutkörperchen (Leukozyten)", BESTAND[1]),
             _best("thrombo", "c", "Blutplättchen (Thrombozyten)", BESTAND[2]),
             _best("plasma", "d", "Das Blutplasma", BESTAND[3]),
             ["hb", "e) Ein 18-jähriger Rekrut hat 11 g/dl Hämoglobin (Norm laut Buch für Männer 13–18 g/dl). Was ist ein möglicher Hinweis?",
              ["Blutarmut, häufig durch Eisenmangel – zu wenig Hämoglobin für den Sauerstofftransport", "eine Infektion mit Bakterien", "eine besonders gute Ausdauer"]],
             ["leukozahl", "f) Bei einer anderen Person: 14 000 Leukozyten pro µl (Norm 4000–10 000). Was ist ein möglicher Hinweis?",
              ["Der Körper wehrt gerade Krankheitserreger ab", "Die Person hat zu wenig Eisen", "Das Blut gerinnt nicht mehr"]],
             ["bg1", "g) Kadett Berger: Mit Anti-A-Serum verklumpt sein Blut, mit Anti-B-Serum nicht. Blutgruppe?", ["A", "B", "AB", "0"]],
             ["bg2", "h) Kadettin Lang: Ihr Blut verklumpt mit Anti-A UND mit Anti-B. Blutgruppe?", ["AB", "A", "B", "0"]],
             ["bg3", "i) Kadett Huber: Sein Blut verklumpt mit keinem der beiden Seren. Blutgruppe?", ["0", "A", "B", "AB"]],
             ["empf0", "j) Eine Patientin hat Blutgruppe 0. Welche roten Blutkonserven verträgt sie?", ["nur 0", "A, B, AB und 0", "0 und A"]],
             ["empfab", "k) Ein Patient hat Blutgruppe AB. Welche roten Blutkonserven verträgt er?", ["A, B, AB und 0", "nur AB", "nur 0"]]],
  "chk": {"ery": {"sel": BESTAND[0]}, "leuko": {"sel": BESTAND[1]}, "thrombo": {"sel": BESTAND[2]}, "plasma": {"sel": BESTAND[3]},
          "hb": {"sel": "Blutarmut, häufig durch Eisenmangel – zu wenig Hämoglobin für den Sauerstofftransport"},
          "leukozahl": {"sel": "Der Körper wehrt gerade Krankheitserreger ab"},
          "bg1": {"sel": "A"}, "bg2": {"sel": "AB"}, "bg3": {"sel": "0"},
          "empf0": {"sel": "nur 0"}, "empfab": {"sel": "A, B, AB und 0"}},
  "fb": {"hb": {"eine Infektion mit Bakterien": "Darauf würden eher die weißen Blutkörperchen hinweisen.",
                "eine besonders gute Ausdauer": "Zu wenig Hämoglobin heißt weniger Sauerstofftransport – eher schlechtere Ausdauer."},
         "leukozahl": {"Die Person hat zu wenig Eisen": "Eisen steckt im Hämoglobin der roten Blutkörperchen, nicht in den Leukozyten.",
                       "Das Blut gerinnt nicht mehr": "Für die Gerinnung sind die Blutplättchen zuständig."},
         "bg1": {"B": "Mit Anti-A verklumpt nur Blut, das das Antigen A trägt.", "AB": "Dann müsste es auch mit Anti-B verklumpen.", "0": "Blutgruppe 0 verklumpt mit keinem Serum."},
         "bg2": {"A": "Es verklumpt auch mit Anti-B – also sitzt auch B darauf.", "B": "Es verklumpt auch mit Anti-A – also sitzt auch A darauf.", "0": "Blutgruppe 0 verklumpt mit keinem Serum."},
         "bg3": {"A": "Dann müsste es mit Anti-A verklumpen.", "B": "Dann müsste es mit Anti-B verklumpen.", "AB": "AB verklumpt mit beiden Seren."},
         "empf0": {"A, B, AB und 0": "Menschen mit Blutgruppe 0 haben Antikörper gegen A UND B im Plasma.",
                   "0 und A": "Die Antikörper gegen A würden die Blutkörperchen der Konserve A verklumpen."},
         "empfab": {"nur AB": "AB hat keine Antikörper gegen A oder B – darum verklumpt keine Konserve.",
                    "nur 0": "0 geht, aber AB verträgt noch mehr: Im Plasma sind keine Antikörper gegen A oder B."}},
  "sol": [["Lösung", ["a) Erythrozyten: Sauerstoff (und CO₂) transportieren, mit Hämoglobin. b) Leukozyten: Abwehr. c) Thrombozyten: Blutgerinnung, Wundverschluss. d) Plasma: gelöste Stoffe, Hormone, Wärme.",
                      "e) Hb zu niedrig → möglicher Hinweis auf Blutarmut (Anämie), häufig durch Eisenmangel (Buch S. 83). Ein Befund ist aber keine Diagnose – das beurteilt eine Ärztin.",
                      "f) Leukozyten erhöht → der Körper wehrt vermutlich gerade Krankheitserreger ab.",
                      "g) A · h) AB · i) 0.",
                      "j) nur 0 (Antikörper gegen A und B im Plasma). k) A, B, AB und 0 (keine Antikörper gegen A oder B). In der Klinik gibt man trotzdem möglichst die gleiche Blutgruppe."]]],
  "tipps": ["Bei g) bis i): Verklumpung mit einem Serum = dieses Antigen ist da. Keine Verklumpung = Antigen fehlt.",
            "k8",
            "Lies im Buch S. 84 die Tabelle zum AB0-System und auf S. 83 die Tabelle mit den Blutwerten."],
  "tip": ["Blutgruppen", "theorie.html#blutgruppen"]},

 {"id": "a8", "nr": 9, "title": "GRUPPENARBEIT: Blutdoping – Rollen und Standpunkte", "src": "Buch S. 82 (Aufgabe »Blutdoping«)", "own": False, "tag": "Stunde 4", "h": 4, "zeit": 7, "marke": "GRUPPENARBEIT",
  "rollen": [["RADPROFI", "Ohne Doping glaubt er, nicht mitzuhalten. Er will wissen, was EPO bringt."],
             ["TEAMÄRZTIN", "Sie kennt die Risiken für Herz und Gefäße und soll ehrlich beraten."],
             ["DOPINGKONTROLLE (NADA)", "Sie erklärt, warum EPO verboten ist und wie Kontrollen funktionieren."],
             ["NACHWUCHS-SPORTLERIN", "17 Jahre, großes Talent. Sie fragt: Muss ich das später auch nehmen?"]],
  "q": "Viergruppen: Jeder übernimmt eine Rolle (Karten oben). 1) Lies im Buch S. 82 die Aufgabe »Blutdoping« und die Theorie-Karte (2 min). "
       "2) Jeder sagt in der Gruppe in einem Satz, was seine Rolle denkt (3 min). 3) Beantwortet b) und c) gemeinsam, jeder schreibt selbst. "
       "Danach fragt Prof. HOLZER die Rollen in der Klasse.",
  "hint": "Denk an den Hämatokrit: Mehr rote Blutkörperchen heißt mehr Sauerstoff – aber das Blut wird auch dicker.",
  "type": "multi",
  "fields": [["rolle", "a) Meine Rolle", ["Radprofi", "Teamärztin", "Dopingkontrolle (NADA)", "Nachwuchs-Sportlerin"], False],
             ["epo", "b) Was bewirkt EPO im Körper?",
              ["Das Knochenmark bildet mehr rote Blutkörperchen – der Hämatokrit steigt", "Die Muskeln werden sofort größer", "Das Herz schlägt langsamer"]],
             ["risiko", "c) Warum ist das gefährlich?",
              ["Das Blut wird dicker – Gefahr von Blutgerinnseln, Herzinfarkt und Schlaganfall", "Das Blut wird zu dünn und gerinnt nicht mehr", "Die Knochen werden weich"]],
             ["meinung", "d) Das sagt meine Rolle (1–2 Sätze)"]],
  "chk": {"epo": {"sel": "Das Knochenmark bildet mehr rote Blutkörperchen – der Hämatokrit steigt"},
          "risiko": {"sel": "Das Blut wird dicker – Gefahr von Blutgerinnseln, Herzinfarkt und Schlaganfall"},
          "meinung": {"kw": [["Standpunkt", r"\w{4,}"]], "man": True}},
  "fb": {"epo": {"Die Muskeln werden sofort größer": "EPO wirkt auf die Blutbildung im Knochenmark, nicht direkt auf die Muskeln.",
                 "Das Herz schlägt langsamer": "EPO verändert das Blut, nicht den Herzschlag."},
         "risiko": {"Das Blut wird zu dünn und gerinnt nicht mehr": "Umgekehrt: Mehr Zellen machen das Blut dickflüssiger.",
                    "Die Knochen werden weich": "EPO verändert die Zahl der Blutzellen, nicht den Kalk in den Knochen."}},
  "sol": [["Lösung", ["b) EPO (Erythropoetin) ist ein Hormon, das das rote Knochenmark anregt, mehr Erythrozyten zu bilden. Hämatokrit steigt, Blut transportiert mehr Sauerstoff.",
                      "c) Das Blut wird zähflüssiger; das Herz muss stärker pumpen; Gerinnsel (Thrombosen), Herzinfarkt und Schlaganfall werden wahrscheinlicher. EPO-Doping ist verboten.",
                      "d) Rollen-Antworten offen – z. B. Ärztin: »Der Leistungsgewinn ist das Risiko nicht wert.« NADA: »Fairness und Gesundheit – darum Blutpass und Kontrollen.«"]]],
  "tipps": ["Was passiert mit einer Suppe, in die man immer mehr Nudeln gibt? Sie wird dicker und fließt schlechter.",
            "k7",
            "Lies im Buch S. 82 den Kasten zum Hämatokrit und die Aufgabe »Blutdoping«."],
  "tip": ["Blut", "theorie.html#blut"]},

 # --------------------------------------------------------------- Stunde 5
 {"id": "a9", "nr": 10, "title": "Muskeln, Hebel, Haltung – Ergonomie-Check an deinem Platz", "src": "Buch S. 110–113 · Hölzel S. 107–108", "own": True, "tag": "Stunde 5", "h": 5, "zeit": 12, "marke": "SELBSTSTUDIUM",
  "sim": ["hebel"],
  "q": "a) bis d): Muskeln. Mach dazu den kleinen Selbstversuch: Leg die Hand auf den Oberarm und beuge und strecke den anderen Arm. "
       "e) und f): Hebel und Heben. g) bis i): Ergonomie-Check – steh auf, schau dir deinen Sitzplatz an, setz dich bewusst hin und prüfe dich selbst (Maßband oder Lineal, wenn du willst).",
  "hint": "Ein Muskel kann nur ziehen, nie schieben. Darum braucht jede Bewegung einen Gegenspieler.",
  "type": "multi",
  "fields": [["beuger", "a) Du beugst den Arm. Welcher Muskel verkürzt sich?", ["der Bizeps (Armbeuger)", "der Trizeps (Armstrecker)", "beide gleich stark"]],
             ["gegen", "b) Warum braucht der Bizeps einen Gegenspieler?",
              ["Ein Muskel kann nur ziehen – zum Strecken muss ein anderer Muskel ziehen", "Damit er nicht reißt", "Weil ein Muskel allein zu schwach wäre"]],
             ["typ1", "c) Welche Muskelfasern trainiert ein Marathonläufer vor allem?", ["langsame Fasern (Typ I): ausdauernd, mit Sauerstoff", "schnelle Fasern (Typ IIx): kurz und sehr kraftvoll", "gar keine – Laufen ist nur Atmung"]],
             ["atp", "d) Woher bekommt der Muskel auf Dauer die Energie (ATP)?",
              ["aus der Zellatmung – dafür bringt das Blut Sauerstoff", "direkt aus dem Knochenmark", "aus der Gelenkschmiere"]],
             ["nah", "e) Du hebst eine schwere Munitionskiste. Wie ist es für den Rücken am schonendsten?",
              ["Kiste nah am Körper, aus den Beinen heben, Rücken gerade, nicht verdrehen", "mit gestreckten Beinen und rundem Rücken schnell hochreißen", "Kiste weit vor dem Körper halten, damit sie nicht an die Knie stößt"]],
             ["hebelwert", "f) Ein Rucksack wird doppelt so weit von der Wirbelsäule entfernt gehalten. Was passiert mit der Kraft, die die Rückenmuskeln aufbringen müssen? (vereinfachtes Hebelmodell)",
              ["Sie wird ungefähr doppelt so groß", "Sie bleibt gleich", "Sie wird halb so groß"]],
             ["knie", "g) Sitzt du gerade so, dass deine Füße flach am Boden stehen und die Knie ungefähr einen rechten Winkel bilden?", ["ja", "nein", "weiß nicht"], False],
             ["schirm", "h) Wo sollte die oberste Zeile am Bildschirm (Laptop, PC) liegen?",
              ["auf Augenhöhe oder etwas darunter", "deutlich über Augenhöhe", "egal, Hauptsache groß"]],
             ["aendern", "i) Eine Sache, die ich an meinem Platz oder beim Lernen zu Hause ändere – mit Begründung (1–2 Sätze)"]],
  "chk": {"beuger": {"sel": "der Bizeps (Armbeuger)"},
          "gegen": {"sel": "Ein Muskel kann nur ziehen – zum Strecken muss ein anderer Muskel ziehen"},
          "typ1": {"sel": "langsame Fasern (Typ I): ausdauernd, mit Sauerstoff"},
          "atp": {"sel": "aus der Zellatmung – dafür bringt das Blut Sauerstoff"},
          "nah": {"sel": "Kiste nah am Körper, aus den Beinen heben, Rücken gerade, nicht verdrehen"},
          "hebelwert": {"sel": "Sie wird ungefähr doppelt so groß"},
          "schirm": {"sel": "auf Augenhöhe oder etwas darunter"},
          "aendern": {"kw": [["Änderung", r"sitz|stuhl|tisch|bildschirm|laptop|handy|licht|pause|aufsteh|beweg|lehne|fuss|fuß|haltung|ruecken|rücken|abstand|hoeh|höh"],
                             ["Begründung", r"weil|damit|sonst|dadurch|daher|deshalb|darum|schmerz|verspann|entlast|belast|ermued|ermüd|augen|nacken"]], "need": 2, "man": True}},
  "fb": {"beuger": {"der Trizeps (Armstrecker)": "Der Trizeps liegt hinten am Oberarm – er streckt den Arm.",
                    "beide gleich stark": "Fühl nach: Vorne wird der Muskel beim Beugen hart und dick."},
         "gegen": {"Damit er nicht reißt": "Gegenspieler sind kein Schutz vor dem Reißen – sie machen die Gegenbewegung möglich.",
                   "Weil ein Muskel allein zu schwach wäre": "Auch ein starker Muskel kann nur ziehen. Zurück bringt den Arm erst der Gegenspieler."},
         "typ1": {"schnelle Fasern (Typ IIx): kurz und sehr kraftvoll": "Die braucht der Gewichtheber. Sie ermüden schnell.",
                  "gar keine – Laufen ist nur Atmung": "Laufen ist Muskelarbeit – die Atmung liefert den Sauerstoff dazu."},
         "atp": {"direkt aus dem Knochenmark": "Im Knochenmark entsteht Blut, keine Muskelenergie.",
                 "aus der Gelenkschmiere": "Die Gelenkschmiere schmiert und ernährt den Knorpel."},
         "nah": {"mit gestreckten Beinen und rundem Rücken schnell hochreißen": "So landet die ganze Last auf der Lendenwirbelsäule und den Bandscheiben.",
                 "Kiste weit vor dem Körper halten, damit sie nicht an die Knie stößt": "Je weiter weg die Last, desto länger der Hebel – desto mehr müssen die Rückenmuskeln ziehen."},
         "hebelwert": {"Sie bleibt gleich": "Probier die Simulation: Der Lastarm wird länger, der Kraftarm des Rückenmuskels bleibt gleich.",
                       "Sie wird halb so groß": "Umgekehrt – der längere Lastarm macht die Last für die Wirbelsäule »schwerer«."},
         "schirm": {"deutlich über Augenhöhe": "Dann hebst du dauernd den Kopf – der Nacken verspannt.",
                    "egal, Hauptsache groß": "Die Höhe ist wichtig für Nacken und Augen."}},
  "sol": [["Lösung", ["a) der Bizeps (Beuger). b) Muskeln können sich nur verkürzen (ziehen); gestreckt wird der Arm vom Trizeps (Strecker) – Spieler und Gegenspieler.",
                      "c) Typ I – langsame, ausdauernde Fasern, die aerob (mit Sauerstoff) arbeiten. d) ATP aus der Zellatmung; den Sauerstoff bringt das Blut aus der Lunge.",
                      "e) Nah am Körper, aus den Beinen, Rücken gerade, nicht verdrehen. f) Ungefähr doppelt so groß (Kraft · Kraftarm = Last · Lastarm, vereinfacht).",
                      "g) persönliche Angabe (keine Wertung). h) Oberste Zeile höchstens auf Augenhöhe, Abstand 50–70 cm, etwa eine Armlänge (AUVA).",
                      "i) offen, z. B. »Ich stelle den Laptop auf Bücher, damit ich nicht nach unten schaue – sonst verspannt mein Nacken.«"]]],
  "tipps": ["Spür am eigenen Arm nach: Vorne (Bizeps) wird es beim Beugen hart, hinten (Trizeps) beim Strecken.",
            "k9",
            "Lies im Buch S. 111 »Zusammenspiel der Muskeln« und auf S. 113 die Tabelle »So sitzt man richtig!«."],
  "tip": ["Muskeln", "theorie.html#muskeln"]},

 {"id": "a10", "nr": 11, "title": "Handschrift: Mindmap »Körper unter Belastung«", "src": "Buch S. 76–85, 107–114", "own": True, "tag": "Stunde 5", "h": 5, "zeit": 7, "marke": "SELBSTSTUDIUM",
  "type": "sketch",
  "q": "Deine Zusammenfassung der Einheit – mit der Hand auf ein Blatt (Datum oben). Zeichne eine Mindmap mit »Körper unter Belastung« in der Mitte und vier Ästen: "
       "HERZ, BLUT, KNOCHEN, MUSKELN. Schreib an jeden Ast mindestens zwei Stichwörter. Zieh dann mindestens zwei Querpfeile zwischen den Ästen und beschrifte sie "
       "(z. B. »Knochenmark bildet Blut«). Fotografiere das Blatt und lade es hoch. Das Blatt kommt danach in deine Mappe. Dann beantworte a).",
  "hint": "Wo steht's? Theorie-Seite »Kurz & knapp« und »Alles auf einen Blick«. Foto: Blatt flach, ganzes Blatt, keine Gesichter.",
  "fields": [["quer", "a) Deine wichtigste Verbindung zwischen zwei Ästen in einem Satz"]],
  "chk": {"quer": {"kw": [["zwei Systeme verbunden", r"herz|blut|knochen|mark|muskel|sauerstoff|gelenk|sehne|puls|kreislauf"]], "man": True}},
  "sol": [["Mögliche Lösung", ["Äste z. B. HERZ: vier Räume, Klappen, Puls · BLUT: Erythrozyten, Gerinnung, Blutgruppen · KNOCHEN: Röhrenknochen, Gelenke, Wachstumsfuge · MUSKELN: Beuger/Strecker, ATP, Ergonomie.",
                               "Querpfeile z. B.: »Rotes Knochenmark bildet Blutzellen« · »Muskeln brauchen Sauerstoff – das Herz pumpt schneller« · »Sehnen verbinden Muskeln mit Knochen« · »Doping mit EPO macht das Blut dicker – mehr Arbeit fürs Herz«."]]],
  "tipps": ["Fang mit den vier Ästen an. Für die Querpfeile frag dich: Was braucht der Muskel? Wo entsteht Blut?",
            "k11",
            "Blättere im Buch S. 77–85 und S. 108–113 die fett gedruckten Begriffe durch."],
  "tip": ["Alles auf einen Blick", "theorie.html#kurz"]},

 # --------------------------------------------------------------- Zusatz
 {"id": "z1", "nr": 12, "title": "Zusatz: Science oder Fiction? Der Elektroschock in der Arztserie", "src": "Buch S. 78 (EKG)", "own": True, "tag": "Zusatz", "h": 0, "zeit": 6,
  "q": "In vielen Arztserien piepst der Monitor, zeigt eine flache Linie – und jemand ruft: »Schock!« Der Defibrillator wird angesetzt und das Herz schlägt wieder. "
       "Lies die Theorie im Teil »Für Schnelle« (EKG und Defibrillator) und entscheide.",
  "hint": "Der Defibrillator unterbricht ein chaotisches Zucken des Herzmuskels. Er ist kein Startknopf.",
  "type": "multi",
  "fields": [["ekg", "a) Was zeigt ein EKG?", ["die elektrische Erregung des Herzmuskels", "den Blutdruck", "den Sauerstoff im Blut"]],
             ["flach", "b) Hilft ein Elektroschock bei einer völlig flachen Linie (kein elektrisches Signal)?",
              ["nein – geschockt wird bei Kammerflimmern; bei der Nulllinie hilft Herzdruckmassage", "ja, das ist genau der Zweck", "ja, aber nur zweimal"]],
             ["laie", "c) Ein Mitschüler bricht zusammen und atmet nicht normal. Was ist richtig?",
              ["Notruf 144, Herzdruckmassage starten und den nächsten Defi holen lassen – der Defi sagt selbst, ob geschockt wird", "warten, bis der Notarzt kommt", "nur den Kopf hochlagern"]]],
  "chk": {"ekg": {"sel": "die elektrische Erregung des Herzmuskels"},
          "flach": {"sel": "nein – geschockt wird bei Kammerflimmern; bei der Nulllinie hilft Herzdruckmassage"},
          "laie": {"sel": "Notruf 144, Herzdruckmassage starten und den nächsten Defi holen lassen – der Defi sagt selbst, ob geschockt wird"}},
  "fb": {"flach": {"ja, das ist genau der Zweck": "Das ist die Fiction. Ein Schock ordnet ein chaotisches Signal – eine Nulllinie hat gar kein Signal.",
                   "ja, aber nur zweimal": "Bei einer Nulllinie wird gar nicht geschockt."},
         "laie": {"warten, bis der Notarzt kommt": "Jede Minute ohne Herzdruckmassage verringert die Überlebenschance deutlich.",
                  "nur den Kopf hochlagern": "Bei Atemstillstand zählt sofortige Herzdruckmassage."}},
  "sol": [["Lösung", ["a) die elektrische Erregung des Herzmuskels (Buch S. 78).",
                      "b) Fiction: Defibrillatoren beenden Kammerflimmern. Bei einer Nulllinie (Asystolie) wird nicht geschockt – Herzdruckmassage und Medikamente durch den Notarzt.",
                      "c) Notruf 144, sofort Herzdruckmassage (fest, schnell, Mitte der Brust), Defi holen lassen. Der automatische Defi analysiert selbst und schockt nur, wenn es nötig ist."]]],
  "tipps": [], "tip": ["Für Schnelle", "theorie.html#schnelle"]},

 {"id": "z2", "nr": 13, "title": "Zusatz: Wie stark drückt das Blut in den Füßen?", "src": "Hölzel NAWI HAK III S. 96 (Aufgabe Ü 3.29)", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Im Stehen lastet eine Blutsäule auf den Venen in Beinen und Füßen. Der Druck einer Flüssigkeitssäule ist p = ρ · g · h "
       "(ρ = Dichte des Blutes, rund 1000 kg/m³; g = 9,81 m/s²; h = Höhe in m). a) Eine Person ist 1,70 m groß, ihr Herz liegt 1,25 m über dem Boden. Berechne den Druck der Blutsäule vom Herzen bis zu den Füßen in Pa. "
       "b) Ein Kind: Herz 0,50 m über dem Boden. c) Rechne a) in mmHg um (1 mmHg ≈ 133 Pa).",
  "hint": "1 Pa = 1 N/m². Setze die Zahlen ein: 1000 · 9,81 · 1,25.",
  "type": "multi",
  "fields": [["p1", "a) Druck für den Erwachsenen (in Pa)"], ["p2", "b) Druck für das Kind (in Pa)"], ["mmhg", "c) Ergebnis aus a) in mmHg (gerundet)"]],
  "chk": {"p1": {"num": 12262.5, "unit": "Pa", "tol": 250}, "p2": {"num": 4905, "unit": "Pa", "tol": 100},
          "mmhg": {"kw": [["etwa 92", r"9[0-3]"]], "need": 1}},
  "fb": {"p1": [[12.2625, "Das sind kPa. In Pa ist der Wert tausendmal so groß."], [1250, "Du hast g vergessen: p = ρ · g · h."]],
         "p2": [[500, "Du hast g vergessen: p = ρ · g · h."]]},
  "sol": [["Lösung", ["a) p = 1000 kg/m³ · 9,81 m/s² · 1,25 m ≈ 12 263 Pa ≈ 12,3 kPa.",
                      "b) p = 1000 · 9,81 · 0,50 ≈ 4905 Pa ≈ 4,9 kPa.",
                      "c) 12 263 Pa : 133 Pa ≈ 92 mmHg. Diesen Druck spüren die Venen in den Füßen im Stehen. Darum helfen Venenklappen und die Muskelpumpe der Beine – und darum schwellen die Beine nach langem Stehen."]]],
  "tipps": [], "tip": ["Blutgefäße", "theorie.html#gefaesse"]},

 {"id": "z3", "nr": 14, "title": "Zusatz: KI-Faktencheck – Bone-Smashing und Wunder-Peptide", "src": "Buch S. 108 (Wachstumsfuge)", "own": True, "tag": "Zusatz", "h": 0, "zeit": 12,
  "link": ["Artikel öffnen: ZDFheute zu Looksmaxxing (10.07.2025)", "https://www.zdfheute.de/panorama/looksmaxxing-tiktok-trend-selbstoptimierung-100.html",
           "ZDFheute (öffentlich-rechtlicher Rundfunk, Deutschland), Text von Bettina Blaß und Kim Bachmann · öffnet in einem neuen Tab"],
  "q": "Im Netz behaupten manche: Wer sich mit dem Hammer leicht auf Kiefer und Wangenknochen klopft (»Bone-Smashing«), bekommt ein markanteres Gesicht – der Knochen wachse dicker nach. "
       "1) Frag eine KI, die eure Schule erlaubt: »Kann man mit Bone-Smashing ein markanteres Kinn bekommen?« Kopier die wichtigste Aussage in a). "
       "Ohne KI nimmst du diese Beispiel-Antwort: »Leichtes Klopfen regt den Knochen an, dicker nachzuwachsen. Das ist in Studien belegt, solange man vorsichtig ist.« "
       "2) Prüf die Antwort mit Teil 5 »Knochen« (Wachstum, Heilung) und dem Artikel oben. 3) Beantworte b) bis d).",
  "hint": "KI-Antworten können falsch sein – prüfe, ob sie sich auf Fachleute stützen. Keinen eigenen »Test« am Gesicht machen.",
  "type": "multi",
  "fields": [["ki", "a) Das sagt die KI (wichtigster Satz)"],
             ["fuge", "b) Warum bekommt man durch Klopfen kein dickeres, markanteres Kinn?",
              ["Brüche heilen ungeordnet mit einem Knochenwulst; eine gezielte Formung ist nicht belegt – stärker werden Knochen durch Training", "Weil der Kiefer aus Knorpel besteht", "Doch, das funktioniert nach 3 Wochen"]],
             ["peptid", "c) Das Peptid BPC-157 wird im Netz als »Heilwunder« für Sehnen verkauft. Was stimmt?",
              ["Es ist nicht als Arzneimittel zugelassen, kaum am Menschen untersucht und im Sport verboten", "Es ist ein normales Medikament aus der Apotheke", "Es ist ein Vitamin und völlig harmlos"]],
             ["urteil", "d) Dein Urteil: Wo lag die KI richtig, wo ungenau? Und wer verdient an solchen Trends? (2–3 Sätze)"]],
  "chk": {"fuge": {"sel": "Brüche heilen ungeordnet mit einem Knochenwulst; eine gezielte Formung ist nicht belegt – stärker werden Knochen durch Training"},
          "peptid": {"sel": "Es ist nicht als Arzneimittel zugelassen, kaum am Menschen untersucht und im Sport verboten"},
          "ki": {"kw": [["KI-Aussage", r"\w{4,}"]], "man": True},
          "urteil": {"kw": [["Urteil", r"richtig|falsch|ungenau|stimmt|quelle|belegt|fachleute|arzt|ärzt"], ["Wer verdient", r"influencer|verkauf|geld|verdien|klicks|reichweite|werbung|herstell|shop|abo"]], "need": 2, "man": True}},
  "fb": {"fuge": {"Weil der Kiefer aus Knorpel besteht": "Der Unterkiefer ist ein Knochen.", "Doch, das funktioniert nach 3 Wochen": "Dafür gibt es keinen Beleg – Ärzte warnen vor Brüchen, Nervenschäden und bleibenden Verformungen."},
         "peptid": {"Es ist ein normales Medikament aus der Apotheke": "BPC-157 ist weltweit nicht als Arzneimittel zugelassen.",
                    "Es ist ein Vitamin und völlig harmlos": "Es ist ein künstliches Peptid. Sichere Dosen beim Menschen sind unbekannt."}},
  "sol": [["Lösung", ["b) Mikrobrüche heilen ungeordnet mit einem Knochenwulst (Kallus); dass man so ein Gesicht gezielt formen kann, ist nicht belegt. Stärker werden Knochen durch Training. Ein Bruch heilt oft mit Fehlstellung, Schwellungen, Nervenschäden (ZDFheute, Ärzte zitiert: Christoph Specht, Alexander Schönborn).",
                      "c) BPC-157: nicht als Arzneimittel zugelassen, Daten vor allem aus Tierversuchen, auf der WADA-Verbotsliste (S0, nicht zugelassene Substanzen).",
                      "d) offen – erwartet: KI-Aussage geprüft, Interesse der Influencer/Verkäufer (Klicks, Produkte, Coaching) genannt."]]],
  "tipps": [], "tip": ["Knochen", "theorie.html#knochen"]},

 {"id": "z4", "nr": 15, "title": "Zusatz: Blutspende in Zahlen und der Rhesusfaktor", "src": "Buch S. 84–85", "own": True, "tag": "Zusatz", "h": 0, "zeit": 6,
  "q": "Das Rote Kreuz sagt: In Österreich wird alle 90 Sekunden eine Blutkonserve gebraucht. a) Wie viele Konserven sind das pro Tag? b) Eine Konserve hält 42 Tage. "
       "Warum muss trotzdem ständig gespendet werden? c) Rhesusfaktor (Buch S. 84–85).",
  "hint": "Ein Tag hat 24 · 60 · 60 Sekunden.",
  "type": "multi",
  "fields": [["tag", "a) Konserven pro Tag (gerundet)"],
             ["halt", "b) Warum ständig spenden?", ["Blut ist nur begrenzt haltbar und lässt sich nicht künstlich herstellen", "Weil Konserven nach einem Tag ablaufen", "Weil nur Blutgruppe 0 verwendet wird"]],
             ["rh", "c) Etwa wie viele Menschen in Mitteleuropa sind Rhesus-positiv?", ["etwa 85 %", "etwa 15 %", "etwa 50 %"]]],
  "chk": {"tag": {"num": 960, "unit": "", "tol": 45}, "halt": {"sel": "Blut ist nur begrenzt haltbar und lässt sich nicht künstlich herstellen"}, "rh": {"sel": "etwa 85 %"}},
  "fb": {"tag": [[1440, "Das wäre eine Konserve pro Minute. Es ist eine alle 90 Sekunden."]],
         "halt": {"Weil Konserven nach einem Tag ablaufen": "Rote Blutkonserven halten rund 42 Tage – aber eben nicht ewig.", "Weil nur Blutgruppe 0 verwendet wird": "Man gibt möglichst die gleiche Blutgruppe – alle Gruppen werden gebraucht."},
         "rh": {"etwa 15 %": "15 % sind Rhesus-negativ.", "etwa 50 %": "Schau im Buch S. 85 oben."}},
  "sol": [["Lösung", ["a) 86 400 s : 90 s = 960 – also rund 1000 Konserven pro Tag (Rotes Kreuz).",
                      "b) Blut ist nur rund 42 Tage haltbar und kann nicht künstlich hergestellt werden.",
                      "c) etwa 85 % Rhesus-positiv, 15 % Rhesus-negativ (Buch S. 85)."]]],
  "tipps": [], "tip": ["Blutgruppen", "theorie.html#blutgruppen"]},

 {"id": "z5", "nr": 16, "title": "Zusatz kreativ: Rücken-Briefing für die Rekruten", "src": "Buch S. 112–114", "own": True, "tag": "Zusatz", "h": 0, "zeit": 15,
  "q": "Gestalte ein kurzes Rücken-Briefing für Rekruten: Wie hebt und trägt man richtig (Kisten, Rucksack, Marschgepäck)? Wähle EINE Form: "
       "Sprachnachricht oder Mini-Podcast (höchstens 60 Sekunden) ODER Plakat auf A4 (per Hand, Foto). Pflichtinhalte: drei Regeln, eine Begründung mit dem Hebel und ein Satz zur Wirbelsäule. "
       "Abgabe: Datei bzw. Foto in LMS (große Dateien über Teams). Keine Gesichter, keine Namen anderer Personen.",
  "hint": "Bewertet wird: fachlich richtig (3 Regeln + Hebel), verständlich, Zeitlimit eingehalten.",
  "type": "multi",
  "fields": [["form", "a) Meine Form", ["Sprachnachricht / Podcast", "Plakat"], False],
             ["regeln", "b) Meine drei Regeln (Stichworte)"]],
  "chk": {"regeln": {"kw": [["nah am Körper", r"nah|körpernah|koerpernah|dicht"], ["aus den Beinen", r"bein|knie|hocke|in die knie"], ["Rücken gerade / nicht verdrehen", r"gerade|verdreh|aufrecht|drehen"]], "need": 2, "man": True}},
  "sol": [["Bewertungsraster (kurz)", ["3 Regeln richtig (nah am Körper, aus den Beinen, Rücken gerade/nicht verdrehen) · Hebel richtig begründet · verständlich und im Zeitlimit."]]],
  "tipps": [], "tip": ["Ergonomie", "theorie.html#ergonomie"]},
]

# ---------------------------------------------------------------- Kontrollen
# Zusatzaufgaben stehen am Ende der Stunde, zu der sie passen (Stephan, 18.11.2026); nr und id bleiben, nur die Anzeigereihenfolge ändert sich
ZUSATZ_STUNDE = {"z1": 1, "z2": 2, "z3": 3, "z4": 4, "z5": 5}
for _t in T:
    if _t["tag"] == "Zusatz":
        _t["zst"] = ZUSATZ_STUNDE[_t["id"]]
assert [t["nr"] for t in T] == list(range(1, 17))
PFLICHT = [t["nr"] for t in T if t["tag"] != "Zusatz" and not t.get("vorhersage")]
assert PFLICHT == list(range(2, 12)), PFLICHT
BESPRECHEN = [2, 4, 7, 8, 10]
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
    if _t["tag"] != "Zusatz": assert _t.get("tipps") or _t.get("vorhersage"), (_t["id"], "Pflichtaufgabe ohne Tipp-Stufen")

# Rechenkontrolle (vom Aufgabentext aus gerechnet)
assert abs(70 * 72 / 1000 - 5.04) < 1e-9 and abs(5.04 * 1440 - 7257.6) < 1e-6 and abs(120 * 150 / 1000 - 18) < 1e-9
assert abs(70 * 70 * 1440 / 1000 - 7056) < 1e-6            # »rund 7000 l pro Tag« (Vorhersage, Auflösung)
assert abs(1000 * 9.81 * 1.25 - 12262.5) < 1e-6 and abs(1000 * 9.81 * 0.5 - 4905) < 1e-6 and round(12262.5 / 133) == 92
assert 24 * 3600 / 90 == 960
assert abs(100 * 40 / 5 - 800) < 1e-9 and abs(100 * 20 / 5 - 400) < 1e-9   # Hebelmodell: 10 kg ≈ 100 N, Kraftarm 5 cm (Theorie-Karte k10)

GRP = {1: STUNDENNAME[1] + " (Buch S. 76–78)",
       2: STUNDENNAME[2] + " (Buch S. 79–81) · VERSUCH K3.1-V1",
       3: STUNDENNAME[3] + " (Buch S. 107–110)",
       4: STUNDENNAME[4] + " (Buch S. 81–85)",
       5: STUNDENNAME[5] + " (Buch S. 110–114)",
       0: "Zusatz · Für Schnelle und Neugierige · wer früher fertig ist (keine Hausübung)",
       "z1": "Zusatz zu Stunde 1 · nur wenn du früher fertig bist", "z2": "Zusatz zu Stunde 2 · nur wenn du früher fertig bist",
       "z3": "Zusatz zu Stunde 3 · nur wenn du früher fertig bist", "z4": "Zusatz zu Stunde 4 · nur wenn du früher fertig bist",
       "z5": "Zusatz zu Stunde 5 · nur wenn du früher fertig bist"}

LERNZIELE = ["**Bau und Arbeitsweise des Herzens** beschreiben und den Weg des Blutes durch **Lungen- und Körperkreislauf** erklären",
             "**Puls** messen, Messwerte vor und nach Belastung auswerten und mit dem **Herzminutenvolumen** rechnen",
             "**Bestandteile des Blutes**, ihre Aufgaben, die **Blutgerinnung** und die **Blutgruppen** (AB0) erklären",
             "**Knochen, Gelenke und Muskeln** als Bewegungsapparat beschreiben – und mit **Ergonomie** den eigenen Arbeitsplatz und das Heben verbessern"]

WICHTIGSTE = ["Das **Herz** ist ein Hohlmuskel mit vier Räumen. **Rechts** pumpt es sauerstoffarmes Blut in den **Lungenkreislauf**, **links** sauerstoffreiches Blut in den **Körperkreislauf**. **Klappen** wirken als Ventile.",
              "**Arterien** führen vom Herzen weg, **Venen** zum Herzen hin, in den **Kapillaren** passiert der Stoffaustausch. **Herzminutenvolumen = Schlagvolumen · Puls** – in Ruhe rund 5 Liter pro Minute.",
              "**Blut** besteht aus Zellen (rote und weiße Blutkörperchen, Blutplättchen) und **Plasma**. Es transportiert, wehrt ab und verschließt Wunden. Die **Blutgruppe** hängt von den **Antigenen** auf den roten Blutkörperchen ab.",
              "Das **Skelett** stützt, schützt und bildet im **roten Knochenmark** Blut. **Gelenke** sind z. B. Kugel-, Scharnier- oder Drehgelenke; **Sehnen** verbinden Muskel und Knochen, **Bänder** Knochen mit Knochen.",
              "**Muskeln** können nur **ziehen** – darum gibt es **Spieler und Gegenspieler**. **Ergonomie** passt die Arbeit an den Menschen an: nah am Körper heben, gerade sitzen, Bildschirm nicht zu hoch, oft bewegen."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Herz", "faustgroßer Hohlmuskel (rund 300 g) mit Scheidewand; je Hälfte ein Vorhof und eine Kammer"],
                ["Vorhof / Kammer", "Vorhof sammelt das Blut und drückt es in die Kammer; die kräftigere Kammer pumpt es in die Arterien"],
                ["Segelklappen / Taschenklappen", "Ventile des Herzens: Segelklappen zwischen Vorhof und Kammer, Taschenklappen zwischen Kammer und Arterie"],
                ["Systole / Diastole", "Systole: Kammern ziehen sich zusammen und pumpen; Diastole: Kammern erschlaffen und füllen sich"],
                ["Körperkreislauf", "linke Kammer → Aorta → Arterien → Kapillaren der Organe → Venen → Hohlvenen → rechter Vorhof"],
                ["Lungenkreislauf", "rechte Kammer → Lungenarterie → Lungenkapillaren (CO₂ ab, O₂ auf) → Lungenvenen → linker Vorhof"],
                ["Arterie", "Blutgefäß, das vom Herzen wegführt; dicke, elastische Wand, hoher Druck"],
                ["Vene", "Blutgefäß, das zum Herzen führt; dünne Wand, niedriger Druck, Venenklappen"],
                ["Kapillare", "feinstes Blutgefäß mit hauchdünner Wand; hier findet der Stoffaustausch statt"],
                ["Puls", "Druckwelle in den Arterien bei jedem Herzschlag; in Ruhe meist 60–80 pro Minute"],
                ["Blutdruck", "Druck des Blutes auf die Gefäßwand in mmHg; systolisch / diastolisch, optimal unter 120/80"],
                ["Herzminutenvolumen", "Blutmenge pro Minute = Schlagvolumen · Puls; in Ruhe rund 5 l"],
                ["Erythrozyten", "rote Blutkörperchen ohne Zellkern; transportieren mit dem Hämoglobin Sauerstoff; leben rund 120 Tage"],
                ["Leukozyten", "weiße Blutkörperchen; wehren Krankheitserreger und Fremdstoffe ab"],
                ["Thrombozyten", "Blutplättchen; verschließen Wunden und starten die Blutgerinnung"],
                ["Blutplasma", "flüssiger Teil des Blutes (ca. 55 %): Wasser mit Eiweißen, Salzen, Nährstoffen, Hormonen"],
                ["Hämatokrit", "Anteil der Blutzellen am Blutvolumen in Prozent"],
                ["Fibrin", "Eiweißfäden, die bei der Gerinnung ein Netz über der Wunde bilden"],
                ["Antigen / Antikörper", "Antigen: Merkmal auf der Zelloberfläche; Antikörper: Abwehrstoff, der genau dazu passt und verklumpt"],
                ["AB0-System", "Blutgruppen A, B, AB und 0 nach den Antigenen auf den roten Blutkörperchen"],
                ["Rhesusfaktor", "Antigen D; rund 85 % der Mitteleuropäer sind Rhesus-positiv"],
                ["Röhrenknochen", "langer Knochen mit Schaft, Markhöhle und Gelenkenden, z. B. Oberschenkelknochen"],
                ["Wachstumsfuge", "Knorpelzone nahe den Knochenenden; dort wächst der Knochen in die Länge, bis sie verknöchert"],
                ["rotes Knochenmark", "Gewebe zwischen den Knochenbälkchen, in dem Blutzellen gebildet werden"],
                ["Gelenk", "bewegliche Knochenverbindung aus Gelenkkopf, Gelenkpfanne, Knorpel, Kapsel, Gelenkschmiere und Bändern"],
                ["Kugel-, Scharnier-, Drehgelenk", "Bewegung in alle Richtungen (Schulter) / nur auf und zu (Ellbogen) / Drehung (Elle-Speiche)"],
                ["Sehne", "verbindet Muskel und Knochen, z. B. Achillessehne"],
                ["Band", "verbindet Knochen mit Knochen und stabilisiert Gelenke"],
                ["Knorpel", "glattes, elastisches Gewebe; verringert Reibung und dämpft Stöße"],
                ["Agonist / Antagonist", "Spieler und Gegenspieler, z. B. Bizeps (Beuger) und Trizeps (Strecker)"],
                ["Actin / Myosin", "Eiweißfäden im Muskel; sie schieben sich ineinander, der Muskel verkürzt sich (Energie: ATP)"],
                ["Muskelfasertypen", "Typ I langsam und ausdauernd (aerob); Typ II schnell und kräftig, ermüdet rasch"],
                ["Ergonomie", "Lehre von der Anpassung der Arbeitsbedingungen an den Menschen"]]

# ---------------------------------------------------------------- Wiederholen
WEISST_DU_NOCH = {
    1: [("Aus der Ernährung: Wofür braucht der Körper Eisen?", "Für das Hämoglobin in den roten Blutkörperchen – es transportiert Sauerstoff."),
        ("Was entsteht bei der Zellatmung?", "Energie (ATP), Kohlenstoffdioxid und Wasser – dafür braucht die Zelle Sauerstoff."),
        ("Welche Stoffe werden über die Nahrung aufgenommen und im Körper verteilt?", "Nährstoffe wie Kohlenhydrate, Fette, Eiweiße, dazu Vitamine und Mineralstoffe.")],
    2: [("Welche Herzhälfte pumpt in den Körperkreislauf?", "Die linke."),
        ("Was ist die Systole?", "Die Phase, in der die Kammern sich zusammenziehen und das Blut auspressen."),
        ("Welches Gefäß führt sauerstoffarmes Blut, ist aber eine Arterie?", "Die Lungenarterie.")],
    3: [("Ruhepuls meist zwischen …?", "60 und 80 Schlägen pro Minute."),
        ("Herzminutenvolumen = ?", "Schlagvolumen · Puls – in Ruhe rund 5 l pro Minute."),
        ("Wozu haben Venen Klappen?", "Damit das Blut nur Richtung Herz fließt.")],
    4: [("Wo werden Blutzellen gebildet?", "Im roten Knochenmark."),
        ("Was verbindet eine Sehne?", "Muskel und Knochen."),
        ("Welches Gelenk ist die Schulter?", "Ein Kugelgelenk.")],
    5: [("Was transportieren die roten Blutkörperchen?", "Sauerstoff (mit dem Hämoglobin) und einen Teil des Kohlenstoffdioxids."),
        ("Blutgruppe 0 – welche roten Konserven?", "Nur 0."),
        ("Was bewirkt EPO-Doping und warum ist es gefährlich?", "Mehr rote Blutkörperchen – das Blut wird dicker, Gerinnsel, Infarkt und Schlaganfall drohen.")],
}

STOPPFRAGEN = {
    "herz": [("Warum fließt das Blut im Herzen nur in eine Richtung?", "Wegen der Klappen: Segelklappen zwischen Vorhof und Kammer, Taschenklappen zwischen Kammer und Arterie – Ventile."),
             ("Was passiert in der Diastole?", "Die Kammern erschlaffen und füllen sich mit Blut aus den Vorhöfen.")],
    "kreislauf": [("Wo nimmt das Blut Sauerstoff auf?", "In den Kapillaren der Lunge (Lungenkreislauf)."),
                  ("Welcher Kreislauf beginnt in der linken Kammer?", "Der Körperkreislauf – über die Aorta.")],
    "gefaesse": [("Was unterscheidet Arterien und Venen?", "Arterien führen vom Herzen weg (dick, elastisch, hoher Druck), Venen zum Herzen hin (dünn, Klappen, niedriger Druck)."),
                 ("Warum ist die Kapillarwand so dünn?", "Damit Sauerstoff, Nährstoffe und Abfallstoffe leicht hindurch können.")],
    "puls": [("Wo kann man den Puls gut tasten?", "An der Innenseite des Handgelenks, daumenseitig (Speichenarterie), mit zwei Fingern."),
             ("Was sagt 120/80 mmHg?", "Systolischer Druck 120, diastolischer Druck 80 mmHg – optimal ist darunter.")],
    "knochen": [("Wo wächst ein Röhrenknochen in die Länge?", "An der Wachstumsfuge nahe den Enden."),
                ("Warum ist der Knochen innen wie ein Gerüst gebaut?", "Leichtbau: Material nur entlang der Kraftlinien – leicht und stabil.")],
    "gelenke": [("Nenne ein Kugel-, ein Scharnier- und ein Drehgelenk.", "Schulter oder Hüfte · Ellbogen oder Fingergelenk · Elle–Speiche oder 1./2. Halswirbel."),
                ("Was hält ein Gelenk zusammen?", "Gelenkkapsel und Bänder.")],
    "blut": [("Welche Blutzellen sorgen für den Wundverschluss?", "Die Blutplättchen (Thrombozyten)."),
             ("Was misst der Hämatokrit?", "Den Anteil der Blutzellen am Blutvolumen.")],
    "blutgruppen": [("Warum verklumpt Blut der Gruppe A, wenn es zu Blut der Gruppe B kommt?", "Im Plasma der Gruppe B sind Antikörper gegen A – sie verkleben die A-Blutkörperchen."),
                    ("Welche Blutgruppe hat keine Antikörper gegen A und B?", "AB.")],
    "muskeln": [("Warum braucht jeder Muskel einen Gegenspieler?", "Muskeln können nur ziehen. Für die Gegenbewegung zieht ein anderer Muskel."),
                ("Welche Muskelfasern braucht ein Sprinter vor allem?", "Schnelle Fasern (Typ II) – kräftig, aber sie ermüden rasch.")],
    "ergonomie": [("Wie hebt man eine schwere Kiste?", "Nah am Körper, aus den Beinen, Rücken gerade, nicht verdrehen."),
                  ("Warum ist Ergonomie auch wirtschaftlich wichtig?", "Weniger Ausfälle, weniger Unfälle, bessere Leistung – das spart dem Betrieb Geld.")],
}

STOLPERSTEINE = [("»Arterien führen sauerstoffreiches, Venen sauerstoffarmes Blut«",
                  "Falsch – Arterie heißt **vom Herzen weg**. Gegenbeispiel: **Lungenarterie** (sauerstoffarm) und **Lungenvene** (sauerstoffreich). Mit Aufgabe 3 a) ansprechen."),
                 ("»Rechts und links im Herzbild«",
                  "Herzbilder zeigen die Sicht **von vorne auf den Patienten**: Die rechte Herzhälfte ist im Bild **links**. Am Torso (DEMO K3.1-D1) einmal umdrehen lassen."),
                 ("Herzminutenvolumen: ml und l verwechselt, Tag mit 24 statt 1440 Minuten",
                  "Typische Fehler bei Aufgabe 5 d) und e): 5040 statt 5,04 l; 121 l statt 7258 l pro Tag. Buch S. 81 rechnet mit **115 ml** pro Schlag (ergibt 7,5 l/min) – passt nicht zu den 70–120 ml links daneben in Ruhe; darum rechnen wir mit 70 ml."),
                 ("»Blutgruppe 0 = Universalspender für alles«",
                  "Gilt nur für **rote Blutkonserven** (Erythrozytenkonzentrat), nicht für Plasma; in der Klinik möglichst **gleiche** Blutgruppe. Den Rhesusfaktor lassen wir in Aufgabe 8 bewusst weg."),
                 ("»Muskeln drücken« / »Sehne = Band«",
                  "Muskeln **ziehen nur** (Gegenspieler!). **Sehne**: Muskel–Knochen, **Band**: Knochen–Knochen. Mit Aufgabe 6 a), b) und 10 b) sichern.")]

# ---------------------------------------------------------------- Quiz/Kahoot-Fragenpool (richtige Antwort an 1. Stelle, Anzeige gemischt)
QUIZ = [
 ("Herz", "Welche Herzhälfte pumpt Blut in den Körperkreislauf?", ["die linke", "die rechte", "beide abwechselnd", "keine – das machen die Venen"], "Linke Kammer → Aorta → Körper.", "Buch S. 77"),
 ("Herz", "Was verhindern die Herzklappen?", ["den Rückfluss des Blutes", "den Herzschlag", "die Blutgerinnung", "die Sauerstoffaufnahme"], "Klappen sind Ventile.", "Buch S. 78"),
 ("Herz", "Wie heißt die Phase, in der sich die Kammern zusammenziehen?", ["Systole", "Diastole", "Hämatokrit", "Pfortader"], "Diastole = Füllphase.", "Buch S. 78"),
 ("Kreislauf", "Wo nimmt das Blut Sauerstoff auf?", ["in den Lungenkapillaren", "in der Aorta", "im rechten Vorhof", "in der Leber"], "Gasaustausch in den Lungenbläschen.", "Buch S. 80"),
 ("Gefäße", "Was ist eine Arterie?", ["ein Gefäß, das vom Herzen wegführt", "jedes Gefäß mit sauerstoffreichem Blut", "ein Gefäß mit Klappen", "das feinste Gefäß"], "Lungenarterie = sauerstoffarm!", "Buch S. 79"),
 ("Puls", "Ruhepuls bei Jugendlichen meist …", ["60–80 pro Minute", "20–30 pro Minute", "120–150 pro Minute", "über 200 pro Minute"], "Sportler oft darunter.", "Buch S. 80"),
 ("Rechnen", "70 ml pro Schlag, 70 Schläge pro Minute – wie viel pro Minute?", ["4,9 l", "140 ml", "49 l", "0,49 l"], "70 · 70 = 4900 ml.", "Buch S. 81"),
 ("Blut", "Welche Zellen transportieren Sauerstoff?", ["rote Blutkörperchen", "weiße Blutkörperchen", "Blutplättchen", "Knorpelzellen"], "Mit Hämoglobin.", "Buch S. 82"),
 ("Blut", "Was bildet bei der Gerinnung ein Netz?", ["Fibrin", "Hämoglobin", "Plasma", "Kalk"], "Aus Fibrinogen wird Fibrin.", "Buch S. 83"),
 ("Blutgruppen", "Welche Blutgruppe hat Antikörper gegen A und B?", ["0", "AB", "A", "B"], "Darum verträgt 0 nur 0.", "Buch S. 84"),
 ("Knochen", "Wo werden Blutzellen gebildet?", ["im roten Knochenmark", "in der Beinhaut", "im Gelenkknorpel", "in den Sehnen"], "Zwischen den Knochenbälkchen.", "Buch S. 108"),
 ("Gelenke", "Welches Gelenk ist ein Kugelgelenk?", ["Schultergelenk", "Ellbogengelenk", "Fingergelenk", "Gelenk zwischen Elle und Speiche"], "Bewegung in alle Richtungen.", "Buch S. 109"),
 ("Muskeln", "Welcher Muskel streckt den Arm?", ["Trizeps", "Bizeps", "Herzmuskel", "Wadenmuskel"], "Bizeps beugt, Trizeps streckt.", "Buch S. 111"),
 ("Ergonomie", "Wie hebt man eine schwere Kiste richtig?", ["nah am Körper, aus den Beinen", "mit rundem Rücken, schnell", "weit vor dem Körper", "mit Drehung des Oberkörpers"], "Kurzer Hebel, gerader Rücken.", "Buch S. 113"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]

# ---------------------------------------------------------------- Geprüfte Quellen (Stand 20.11.2026)
QUELLEN = [
 ("W1", "Looksmaxxing: Gefährlicher TikTok-Trend zur Selbstoptimierung (10.07.2025, Bettina Blaß, Kim Bachmann)", "ZDFheute (öffentlich-rechtlicher Rundfunk, Deutschland)",
  "https://www.zdfheute.de/panorama/looksmaxxing-tiktok-trend-selbstoptimierung-100.html",
  "Bone-Smashing: Männer schlagen sich ins Gesicht, um Mikrobrüche zu erzeugen; Arzt Christoph Specht: »abstruse Vorstellung«; Risiken Brüche, Nervenschäden, bleibende Verformungen; Mewing ohne wissenschaftlichen Beleg",
  "Seite am 20.11.2026 geöffnet, Text gelesen"),
 ("W2", "Bluthochdruck – Klassifikation (DocMedicus Gesundheitslexikon, Dr. med. Werner G. Gehring, Stand 09.08.2025)", "DocMedicus, mit Verweis auf ESH-Leitlinie 2023 und ESC-Leitlinie 2024",
  "https://www.gesundheits-lexikon.com/Herz-Kreislauf-Gefaesse/Bluthochdruck-Hypertonie/Klassifikation",
  "optimal < 120 und < 80; normal 120–129 und/oder 80–84; hoch normal 130–139 und/oder 85–89 mmHg", "Seite am 20.11.2026 geöffnet; Achtung: Seite ordnet die Tabelle nicht ganz eindeutig ESH 2018/2023 zu – die Werte sind in beiden gleich"),
 ("W3", "BPC-157: Experimental Peptide Prohibited", "U.S. Anti-Doping Agency (USADA)", "https://www.usada.org/spirit-of-sport/bpc-157-peptide-prohibited/",
  "BPC-157 ist auf der WADA-Verbotsliste (S0, nicht zugelassene Substanzen); nicht als Arzneimittel für Menschen zugelassen", "Textauszug per Websuche gelesen"),
 ("W4", "BPC-157 (Sport Integrity Australia)", "Australische Anti-Doping-Behörde", "https://www.sportintegrity.gov.au/substances/bpc-157",
  "von keiner Behörde weltweit zugelassen; keine Studien am Menschen; WADA S0", "Textauszug per Websuche gelesen"),
 ("W5", "Blutspende: alle 90 Sekunden eine Blutkonserve (Rotes Kreuz, APA 26.06.2025)", "Der Standard / APA",
  "https://www.derstandard.at/story/3000000275687/kritische-lage-bei-blutspenden-5000-konserven-fehlen",
  "alle 90 Sekunden eine Konserve; rund 1000 pro Tag; Konserven 42 Tage haltbar (ORF Wien)", "Textauszug per Websuche gelesen; mehrere Quellen (ORF, gesundheit.gv.at) nennen dieselben Zahlen"),
 ("W6", "Factsheet Augen, Rücken, Gesundheit bei Bildschirmarbeit (27.09.2024)", "AUVA (Allgemeine Unfallversicherungsanstalt, Österreich)",
  "https://auva.at/media/2lzhkc0i/factsheet-digitalisierungskampagne_augen_ruecken_gesundheit_bildschirmarbeit_27092024_bf.pdf",
  "oberste Bildschirmzeile nicht über Augenhöhe; Abstand Kopf–Bildschirm rund 45–75 cm (50 cm); mind. 500 lux; Sitz- und Tischhöhe an Körpergröße anpassen", "Textauszug per Websuche gelesen"),
 ("W7", "Bildschirmarbeit (Gesundheitsportal, Expertenprüfung AUVA)", "gesundheit.gv.at (Gesundheitsministerium)", "https://www.gesundheit.gv.at/leben/lebenswelt/beruf/arbeitsplatz/bildschirmarbeit.html",
  "oberste Zeile nicht über Augenhöhe; Sehabstand ca. 60–80 cm", "Textauszug per Websuche gelesen (Abstand: AUVA-Factsheet nennt 45–75 cm – wir nennen »etwa 50 cm, eine Armlänge«)"),
]
QUELLE = {q[0]: q for q in QUELLEN}

NICHT_GEPRUEFT = [
 "Trauner-Filmtipps nawi_v120 (Herz), nawi_v121 (Blutgruppen, Rotes Kreuz), nawi_v124 (Beuger und Strecker): trauner.at ist von hier aus gesperrt – nicht geöffnet. Sie stehen nur als Buch-Filmtipp auf der Theorie-Seite; bitte einmal selbst ansehen.",
 "Podcasts aus dem Jahresplan (Ö1 Wissen aktuell »Herzinfarkt bei Frauen« 2026, »Rückenschmerzen im Homeoffice« 2022; BIOfunk 65 »Rhesus & Co«): nicht angehört – nur als »bitte anhören« in der Lösungsseite.",
 "Videos: YouTube ist von hier aus nicht prüfbar. Darum steht auf den Kadetten-Seiten kein YouTube-Video; stattdessen eigene Animationen.",
 "Seilnacht-Filmverzeichnis »Chemische Phänomene erleben«: Chemie-Sammlung; zu Herz, Blut und Skelett ist dort nichts zu erwarten – nicht geöffnet.",
 "Muskelanteil »bis zu 45 %« (Buch S. 110) bzw. »rund 40 %«: Lehrbuchwert, nicht an einer Studie geprüft. »Über 300 Muskeln beim Lachen« (Buch S. 110): kein Beleg gefunden – auf den Kadetten-Seiten nicht verwendet.",
]

# ---------------------------------------------------------------- ABCD-Karte: »Weißt du noch?« und DEMO-Vermutungen
WDN_ABCD = {
    1: [("Wofür braucht der Körper Eisen aus der Nahrung?", "für das Hämoglobin im Blut", ["für die Knochenhärte", "für die Verdauung von Fett", "für die Haare"], "Hämoglobin enthält Eisen und bindet Sauerstoff."),
        ("Bei der Zellatmung braucht die Zelle …", "Sauerstoff und Traubenzucker", ["nur Wasser", "Kohlenstoffdioxid und Licht", "Eisen und Calcium"], "Dabei entstehen ATP, CO₂ und Wasser."),
        ("Welche Ernährungsform verzichtet auf Fleisch, aber nicht auf Eier und Milch?", "ovo-lakto-vegetarisch", ["vegan", "Vollwertkost", "Paleo"], "Aus der Einheit Ernährungsweisen.")],
    2: [("Welche Herzhälfte pumpt in den Körper?", "die linke", ["die rechte", "beide abwechselnd", "keine"], "Linke Kammer → Aorta."),
        ("Systole heißt …", "die Kammern ziehen sich zusammen", ["die Kammern füllen sich", "das Herz ruht", "die Klappen wachsen"], "Diastole = Füllphase."),
        ("Die Lungenarterie führt …", "sauerstoffarmes Blut", ["sauerstoffreiches Blut", "Lymphe", "gar kein Blut"], "Arterie = vom Herzen weg.")],
    3: [("Ruhepuls bei Jugendlichen meist …", "60–80 pro Minute", ["20–30 pro Minute", "120–150 pro Minute", "über 200 pro Minute"], "Sportler oft darunter."),
        ("Herzminutenvolumen = …", "Schlagvolumen · Puls", ["Puls : Schlagvolumen", "Blutdruck · Puls", "Puls + Atemzüge"], "In Ruhe rund 5 l pro Minute."),
        ("Venenklappen sorgen dafür, dass …", "das Blut nur Richtung Herz fließt", ["der Puls steigt", "das Blut gerinnt", "die Arterien weiter werden"], "Rückschlagventile.")],
    4: [("Wo werden Blutzellen gebildet?", "im roten Knochenmark", ["in der Leber", "im Herzen", "in den Sehnen"], "Brücke von Stunde 3 zu heute."),
        ("Eine Sehne verbindet …", "Muskel und Knochen", ["Knochen und Knochen", "Haut und Muskel", "zwei Muskeln"], "Bänder verbinden Knochen mit Knochen."),
        ("Das Schultergelenk ist ein …", "Kugelgelenk", ["Scharniergelenk", "Drehgelenk", "festes Gelenk"], "Bewegung in alle Richtungen.")],
    5: [("Rote Blutkörperchen transportieren …", "Sauerstoff", ["Antikörper", "Fibrin", "Hormone für die Gerinnung"], "Mit Hämoglobin."),
        ("Blutgruppe 0 verträgt rote Konserven der Gruppe …", "nur 0", ["A, B, AB und 0", "nur AB", "0 und A"], "0 hat Antikörper gegen A und B."),
        ("EPO-Doping macht das Blut …", "dicker", ["dünner", "heller", "salziger"], "Mehr Zellen – Gerinnselgefahr.")],
}
VERMUTUNG_ABCD = {
    "K3.1-D1": [("Wo liegt das Herz im Brustkorb?", "fast in der Mitte, etwas nach links", ["ganz links unter der Achsel", "rechts neben der Leber", "direkt unter dem Schlüsselbein"], "Hinter dem Brustbein, die Spitze zeigt nach links unten."),
                ("Wie groß ist ein gesundes Herz ungefähr?", "wie eine geschlossene Faust", ["wie ein Fußball", "wie eine Erbse", "wie ein Handy"], "Rund 300 g, faustgroß (Buch S. 77).")],
    "K3.1-D2": [("Prof. HOLZER drückt eine Vene am Unterarm handnah ab und streicht sie Richtung Ellbogen aus. Was passiert?", "Die Vene bleibt bis zur nächsten Klappe leer", ["Die Vene platzt", "Das Blut fließt sofort zurück", "Nichts – Venen haben keine Klappen"], "Die Klappe lässt das Blut nicht zurück. Erst wenn der erste Finger loslässt, füllt sich die Vene von der Hand her.")],
    "K3.6-D1": [("Ein Röhrenknochen ist innen …", "hohl bzw. mit Bälkchen und Mark gefüllt", ["massiv wie ein Stein", "mit Luft gefüllt wie ein Ballon", "aus Knorpel"], "Leichtbau wie ein Fahrradrahmen.")],
    "K3.6-D2": [("Dieselbe Last wird weit vom Körper gehalten. Für den Rücken ist das …", "schwerer", ["leichter", "gleich", "egal, nur die Arme arbeiten"], "Längerer Hebel – die Rückenmuskeln müssen stärker ziehen.")],
}
for _n, _qs in list(WDN_ABCD.items()) + list(VERMUTUNG_ABCD.items()):
    for _q in _qs: assert len(_q) == 4 and len(set([_q[1]] + _q[2])) == 4, _q
assert set(VERMUTUNG_ABCD) == set(DEMOS)
for _v, _d in VS.items(): assert any(t.get("versuch") == _v and t["nr"] == _d["aufgabe"] for t in T), (_v, "Aufgabennummer falsch")

# ---------------------------------------------------------------- Mitarbeits-Check: 10 Fragen, nur Pflichtstoff, kein Militärbezug
CHECK = [
    {"thema": "Herz", "n": 2, "fragen": [
        ("h1", "Welche Herzhälfte pumpt sauerstoffreiches Blut in den Körper?", "die linke", ["die rechte", "beide abwechselnd", "keine"], "S. 77"),
        ("h2", "Wo liegen die Segelklappen?", "zwischen Vorhof und Kammer", ["zwischen Kammer und Arterie", "in den Beinvenen", "in der Lunge"], "S. 78"),
        ("h3", "Was passiert in der Systole?", "Die Kammern ziehen sich zusammen und pumpen", ["Die Kammern füllen sich", "Das Herz steht still", "Die Vorhöfe wachsen"], "S. 78"),
        ("h4", "Welches Gefäß führt sauerstoffarmes Blut, obwohl es eine Arterie ist?", "die Lungenarterie", ["die Aorta", "die Lungenvene", "die Pfortader"], "S. 79–80")]},
    {"thema": "Gefäße und Puls", "n": 2, "fragen": [
        ("p1", "hmv", "", [], "S. 81"),
        ("p2", "Wo findet der Stoffaustausch statt?", "in den Kapillaren", ["in der Aorta", "in den Herzklappen", "in den Hohlvenen"], "S. 79"),
        ("p3", "Wozu haben Venen Klappen?", "damit das Blut nur Richtung Herz fließt", ["damit der Puls steigt", "damit das Blut gerinnt", "damit Sauerstoff gespeichert wird"], "S. 79")]},
    {"thema": "Blut", "n": 2, "fragen": [
        ("b1", "Welche Blutzellen wehren Krankheitserreger ab?", "die weißen Blutkörperchen", ["die roten Blutkörperchen", "die Blutplättchen", "das Plasma"], "S. 82–83"),
        ("b2", "Was bildet bei der Blutgerinnung ein Netz über der Wunde?", "Fibrin", ["Hämoglobin", "Plasma", "Kalk"], "S. 83"),
        ("b3", "Blut verklumpt mit Anti-B-Serum, aber nicht mit Anti-A. Blutgruppe?", "B", ["A", "AB", "0"], "S. 84"),
        ("b4", "Welche roten Konserven verträgt ein Mensch mit Blutgruppe 0?", "nur 0", ["A, B, AB und 0", "nur AB", "0 und A"], "S. 84")]},
    {"thema": "Knochen und Gelenke", "n": 2, "fragen": [
        ("k1", "Wo werden rote Blutkörperchen gebildet?", "im roten Knochenmark", ["in der Beinhaut", "im Gelenkknorpel", "in den Sehnen"], "S. 108"),
        ("k2", "Wo wächst ein Röhrenknochen in die Länge?", "an der Wachstumsfuge", ["in der Mitte des Schafts", "in der Beinhaut", "überall gleich"], "S. 108"),
        ("k3", "Welches Gelenk ist ein Scharniergelenk?", "das Ellbogengelenk (Beugen und Strecken)", ["das Schultergelenk", "das Hüftgelenk", "das Gelenk zwischen Elle und Speiche"], "S. 109"),
        ("k4", "Was verbindet ein Band?", "Knochen mit Knochen", ["Muskel mit Knochen", "Muskel mit Muskel", "Haut mit Knochen"], "S. 109")]},
    {"thema": "Muskeln und Ergonomie", "n": 2, "fragen": [
        ("m1", "Warum braucht der Bizeps einen Gegenspieler?", "Muskeln können nur ziehen", ["Muskeln können nur drücken", "damit er nicht reißt", "damit er mehr Blut bekommt"], "S. 111"),
        ("m2", "Wie hebt man eine schwere Kiste am schonendsten?", "nah am Körper, aus den Beinen, Rücken gerade", ["mit rundem Rücken schnell hochreißen", "weit vor dem Körper", "mit Drehung im Rücken"], "S. 113"),
        ("m3", "Wo sollte die oberste Bildschirmzeile liegen?", "höchstens auf Augenhöhe", ["deutlich über Augenhöhe", "auf Bauchhöhe", "egal"], "S. 113"),
        ("m4", "Was ist Ergonomie?", "die Anpassung der Arbeit an den Menschen", ["ein Muskeltraining", "ein Blutwert", "die Lehre von den Knochen"], "S. 112")]},
]
assert sum(g["n"] for g in CHECK) == 10
CHECK_KEY = "26-27-3AB-K3.1-check"
CHECK_CODE = "7316"   # Startcode – im Seitencode nur als Prüfsumme; Prof. HOLZER zeigt ihn am Beamer

PARTNERCHECK = [
    ("Welche Herzhälfte pumpt in die Lunge – und welche in den Körper?", "Rechts → Lunge (Lungenkreislauf), links → Körper (Körperkreislauf)."),
    ("Herzminutenvolumen bei 80 ml und 75 Schlägen pro Minute?", "80 ml · 75 = 6000 ml = 6 l pro Minute."),
    ("Blutgruppe AB – welche roten Konserven gehen?", "A, B, AB und 0 (keine Antikörper gegen A oder B)."),
    ("Sehne oder Band: Was verbindet Muskel und Knochen?", "Die Sehne. Das Band verbindet Knochen mit Knochen."),
]

# ---------------------------------------------------------------- Kompetenzmodell (Skill bhak-kompetenzmodell, 20.11.2026 – Probe-Einheit)
# hd: A Beobachten und Erfassen · B Untersuchen und Bearbeiten · C Bewerten und Anwenden; niveau 1 = + (Grundlegendes), 2 = ++ (Vertiefung)
ZIELE = [{"nr": 1, "hd": "A", "text": "Ich kann Bau und Arbeit des Herzens beschreiben und den Weg des Blutes durch beide Kreisläufe erklären.", "theorie": "herz", "buch": "Buch S. 77–80"},
         {"nr": 2, "hd": "B", "text": "Ich kann meinen Puls messen, Werte vor und nach Belastung auswerten und das Herzminutenvolumen berechnen.", "theorie": "puls", "buch": "Buch S. 80–81"},
         {"nr": 3, "hd": "A", "text": "Ich kann die Bestandteile des Blutes, die Gerinnung und die Blutgruppen erklären.", "theorie": "blut", "buch": "Buch S. 81–85"},
         {"nr": 4, "hd": "C", "text": "Ich kann Knochen, Gelenke und Muskeln beschreiben und meinen Arbeitsplatz und das Heben ergonomisch verbessern.", "theorie": "knochen", "buch": "Buch S. 108–113"}]
KOMPETENZ = {"a1": ("A", 1, 1), "a2": ("A", 1, 1), "a3": ("B", 1, 2), "a4": ("B", 2, 2), "a5": ("A", 1, 4), "a6": ("B", 1, 4),
             "a7": ("B", 2, 3), "a8": ("C", 2, 3), "a9": ("C", 1, 4), "a10": ("A", 2, 1),
             "z1": ("C", 2, 1), "z2": ("B", 2, 1), "z3": ("C", 2, 4), "z4": ("A", 2, 3), "z5": ("C", 2, 4)}
for _t in T:
    if _t["id"] in KOMPETENZ:
        _t["hd"], _t["niveau"], _t["ziel"] = KOMPETENZ[_t["id"]]
_pf = [t for t in T if t["id"] in KOMPETENZ and t["h"]]
assert sum(t["niveau"] == 1 for t in _pf) >= 2 and any(t["niveau"] == 2 for t in _pf)
assert {t["hd"] for t in T if "hd" in t} == {"A", "B", "C"}
