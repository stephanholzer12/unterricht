"""Theorie-Seite K2.4/K3.2 Akustik und Gehör: Theorie-Karten, Teile und Abschnitte.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufe 2 im Arbeitsblatt (Theorie-Karte) und die KURZ-KLÄREN-Folien der Beamer-Präsentation.
Block-Arten: tiles, ul, ol, merke, hint, table, reveal, img (Datei, Alt, Unterschrift), buch, karte, gemeinsam, sim (interaktive Druckwelle), demo (ID, Text), versuch (ID, Text, Anker).
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py, SVG). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "schall": "1 Schall", "tempo": "2 Tempo", "tonhoehe": "3 Tonhöhe", "dezibel": "4 Dezibel", "messen": "5 Messen",
          "ohr": "6 Ohr", "schutz": "7 Schutz", "richtung": "8 Richtung", "gleichgewicht": "9 Gleichgewicht",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

KARTEN = {
 "k1": {"titel": "Schall ist eine Druckwelle", "teil": "schall", "buch": "Buch S. 61", "bild": "img/druckwelle.svg",
        "alt": "Eine Reihe Luftteilchen vor einem schwingenden Lautsprecher: Dichte und dünne Bereiche wandern nach rechts, jedes Teilchen schwingt nur wenig hin und her. Darunter die Druckkurve mit Überdruck und Unterdruck.",
        "satz": ["Eine **Schallquelle schwingt** und stößt die Luftteilchen an. Die Teilchen schwingen nur **hin und her** – weiter wandern **Verdichtung und Verdünnung** (Längswelle).",
                 "Ohne Teilchen kein Schall: Im **Vakuum** breitet sich Schall nicht aus.",
                 "Die Wellenlinie in Zeichnungen zeigt den **Luftdruck an einer Stelle** – keine Auf-und-ab-Bewegung."],
        "formeln": [("p", "Schalldruck: Abweichung vom normalen Luftdruck", "Pa"), ("f", "Frequenz: Schwingungen pro Sekunde", "Hz"), ("A", "Amplitude: größte Druckschwankung", "Pa")],
        "link": "theorie.html#schall"},
 "k2": {"titel": "Wie schnell ist Schall?", "teil": "tempo", "buch": "Buch S. 61, 67", "bild": "img/schallweg.svg",
        "alt": "Oben drei Balken für die Schallgeschwindigkeit in Luft, Wasser und Stahl. Darunter ein Blitz mit Donner und drei Sekunden pro Kilometer. Unten ein Echo: Weg zur Felswand und zurück.",
        "satz": ["In Luft legt Schall rund **340 m pro Sekunde** zurück (bei 15 °C; bei 20 °C 343 m/s) – in Wasser etwa 1480 m/s, in Stahl rund 5000 m/s.",
                 "**s = v · t**. Beim **Echo** läuft der Schall hin **und** zurück: Die Wand ist nur halb so weit weg.",
                 "Aus der Wellenlehre kennst du **v = λ · f** – daraus folgt λ = v / f."],
        "formeln": [("s", "Weg", "m"), ("v", "Schallgeschwindigkeit", "m/s"), ("t", "Zeit", "s"), ("λ", "Wellenlänge", "m"),
                    ("s = v · t", "Echo: s = v · t / 2", ""), ("λ = v / f", "Faustregel Gewitter: Sekunden : 3 = km", "")],
        "link": "theorie.html#tempo"},
 "k3": {"titel": "Tonhöhe und Lautstärke", "teil": "tonhoehe", "buch": "Buch S. 63–64", "bild": "img/tonhoehe.svg",
        "alt": "Vier Druckkurven: oben eine tiefe und eine hohe Frequenz bei gleicher Amplitude, unten eine kleine und eine große Amplitude bei gleicher Frequenz.",
        "satz": ["Die **Frequenz f** bestimmt die **Tonhöhe**: mehr Schwingungen pro Sekunde, höherer Ton. Eine kürzere Linealzunge oder Saite schwingt schneller.",
                 "Die **Amplitude** bestimmt die Stärke: größere Druckschwankung, lauterer Schall.",
                 "Junge Menschen hören etwa **20 Hz bis 20 000 Hz**. Darunter liegt **Infraschall**, darüber **Ultraschall**."],
        "formeln": [("f", "Frequenz", "Hz"), ("1 kHz", "= 1000 Hz", ""), ("Kammerton a'", "440 Hz", "")],
        "link": "theorie.html#tonhoehe"},
 "k4": {"titel": "Dezibel: die Leiter in Zehnerschritten", "teil": "dezibel", "buch": "Buch S. 64, 110", "bild": "img/dbleiter.svg",
        "alt": "Senkrechte Leiter von 0 bis 160 dB mit Beispielen: Hörschwelle, Flüstern, Gespräch, Straßenverkehr, 85 dB Gehörschutzpflicht, Konzert, Schmerzgrenze, Schuss. Neben jeder Zehnerstufe steht mal zehn.",
        "satz": ["Der **Schalldruckpegel** wird in **Dezibel (dB)** angegeben. 0 dB ist ungefähr die Hörschwelle.",
                 "**+10 dB** = **zehnfache Intensität**, aber nur etwa **3,2-facher Schalldruck**. +20 dB = hundertfache Intensität, zehnfacher Schalldruck.",
                 "Die **Lautstärke** ist unsere Empfindung und hängt auch von der Frequenz ab. Grob: +10 dB klingen etwa doppelt so laut."],
        "formeln": [("L", "Schalldruckpegel", "dB"), ("I", "Schallintensität (Energie pro Fläche und Zeit)", "W/m²"),
                    ("+10 dB", "Intensität × 10, Schalldruck × 3,2", ""), ("+3 dB", "doppelte Intensität (zwei gleiche Quellen)", "")],
        "link": "theorie.html#dezibel"},
 "k5": {"titel": "Der Weg ins Ohr", "teil": "ohr", "buch": "Buch S. 109–110", "bild": "img/ohr.svg",
        "alt": "Schnitt durch das Ohr: Ohrmuschel, Gehörgang, Trommelfell, Hammer, Amboss, Steigbügel am ovalen Fenster, Schnecke, Bogengänge, Hörnerv und Ohrtrompete; Pfeile zeigen den Weg des Schalls.",
        "satz": ["**Außenohr**: Ohrmuschel und Gehörgang leiten den Schall zum **Trommelfell**, das mitschwingt.",
                 "**Mittelohr**: **Hammer, Amboss, Steigbügel** übertragen die Schwingung auf das kleine **ovale Fenster** und verstärken den Druck etwa **22-fach** – sonst käme sie kaum in die Flüssigkeit.",
                 "**Innenohr**: Die Druckwelle bewegt **Lymphe** und Grundmembran; die **Haarzellen** im Corti-Organ machen daraus **elektrische Signale** für den Hörnerv."],
        "formeln": [], "link": "theorie.html#ohr"},
 "k6": {"titel": "Hörschäden und Gehörschutz", "teil": "schutz", "buch": "Buch S. 109–110", "bild": "img/gehoerschutz.svg",
        "alt": "Links gesunde Haarzellen mit aufrechten Härchen, rechts geknickte und fehlende Härchen nach Lärm. Darunter Kapselgehörschutz und Stöpsel mit grünem Haken, ein Noise-Cancelling-Ohrhörer mit rotem Kreuz.",
        "satz": ["Zu viel Schall knickt und zerstört **Haarzellen** – beim Menschen **wachsen sie nicht nach**. Ein extrem lauter Knall kann ein **Knalltrauma** auslösen, oft mit **Tinnitus**.",
                 "Auch **lange** Belastung schadet: Am Arbeitsplatz muss ab **80 dB** Gehörschutz bereitstehen, ab **85 dB** muss er getragen werden.",
                 "Nur **geprüfter Gehörschutz** (Stöpsel, Kapsel, Otoplastik) schützt zuverlässig – **Noise-Cancelling-Kopfhörer** sind dafür nicht zugelassen."],
        "formeln": [("80 dB", "40 Stunden pro Woche gelten als sichere Grenze (WHO)", ""), ("+3 dB", "halbe sichere Hördauer", "")],
        "link": "theorie.html#schutz"},
 "k7": {"titel": "Richtungshören", "teil": "richtung", "buch": "Buch S. 110", "bild": "img/richtung.svg",
        "alt": "Kopf von oben, links eine Schallquelle. Der Weg zum linken Ohr ist kürzer, zum rechten Ohr etwa 0,2 m länger. Das rechte Ohr liegt im Schallschatten.",
        "satz": ["Kommt ein Geräusch von der Seite, erreicht es das abgewandte Ohr **etwas später** und **leiser**.",
                 "Bei rund 0,2 m Umweg sind das nur etwa **0,6 Millisekunden** – das Gehirn wertet sogar Unterschiede von wenigen Hundertstel Millisekunden aus.",
                 "Von **genau vorne oder hinten** ist für beide Ohren alles gleich. Dann helfen die Form der **Ohrmuschel** und **Kopfdrehen**."],
        "formeln": [("Δt = Δs / v", "Zeitunterschied zwischen den Ohren", "s"), ("0,2 m : 340 m/s", "≈ 0,0006 s = 0,6 ms", "")],
        "link": "theorie.html#richtung"},
 "k8": {"titel": "Gleichgewicht: Lage- und Drehsinn", "teil": "gleichgewicht", "buch": "Buch S. 111–112", "bild": "img/gleichgewicht.svg",
        "alt": "Links ein Vorhofsäckchen: Kalkkristalle auf einer Gallertschicht kippen bei geneigtem Kopf und biegen die Härchen. Rechts ein Bogengang mit Ampulle: Beim Drehen bleibt die Lymphe zurück und biegt die Gallertkuppel.",
        "satz": ["**Vorhofsäckchen** (Lagesinn): **Kalkkristalle** auf einer Gallertschicht werden von der Schwerkraft gezogen und biegen die Härchen der Sinneszellen – so merkst du Neigung und Beschleunigung geradeaus.",
                 "**Bogengänge** (Drehsinn): drei Ringe in drei Ebenen. Beginnt eine Drehung, bleibt die **träge Lymphe** zurück und biegt die Gallertkuppel in der **Ampulle**.",
                 "Gemeldet werden nur **Änderungen** der Drehung. Nach dem Stoppen fließt die Lymphe kurz weiter – dir wird **schwindlig**."],
        "formeln": [], "link": "theorie.html#gleichgewicht"},
 "k9": {"titel": "Alles auf einen Blick", "teil": "kurz", "buch": "Buch S. 60–67, 109–112", "bild": "img/signalweg.svg",
        "alt": "Der Signalweg in sechs Stationen: Quelle schwingt, Druckwelle in Luft, Pegel in Dezibel, Ohr verstärkt, Haarzellen und Gehirn, Orientierung mit Richtung und Gleichgewicht.",
        "satz": ["**Quelle → Luft → Ohr → Haarzellen → Gehirn → Orientierung**: Das ist der Weg dieser Einheit.",
                 "Rechnen: **s = v · t** (Echo: durch 2) und **λ = v / f**, mit v ≈ 340 m/s in Luft.",
                 "Merken: **+10 dB = Intensität × 10**, Haarzellen wachsen nicht nach, Bogengänge melden **Drehung**, Vorhofsäckchen **Lage**."],
        "formeln": [("s = v · t", "Weg, Geschwindigkeit, Zeit", "m, m/s, s"), ("λ = v / f", "Wellenlänge", "m"), ("+10 dB", "Intensität × 10", "")],
        "link": "theorie.html#kurz"},
}
for _k, _v in KARTEN.items():
    assert len(_v["satz"]) <= 3, (_k, "mehr als drei Sätze")
AUFGABE_KARTE = {t["id"]: t["tipps"][1] for t in I.T if t.get("tipps")}
for _id, _k in AUFGABE_KARTE.items():
    assert _k in KARTEN, (_id, _k)


def karte_html_daten():
    return {k: {"titel": v["titel"], "satz": v["satz"], "bild": v["bild"], "bild_hoch": "", "alt": v["alt"],
                "formeln": v["formeln"], "link": v["link"], "buch": v["buch"]} for k, v in KARTEN.items()}


def kartenblock(key):
    return ("karte", KARTEN[key])


EINSTIEG = [
 {"id": "s0a", "title": "Vom Knall zum Kopf", "pill": "Buch S. 60",
  "blocks": [("img", "img/signalweg.svg", KARTEN["k9"]["alt"], "Der Weg dieser Einheit: von der schwingenden Quelle bis zur Orientierung im Raum."),
             ("ul", ["**Das Wichtigste vorab:** Schall ist eine Druckwelle. Dein Ohr macht daraus elektrische Signale – und dasselbe Innenohr sagt dir, wo oben ist.",
                     "**Wozu?** Beim Schießen, auf der Baustelle, im Konzert und mit Kopfhörern entscheidest du selbst, ob dein Gehör in 30 Jahren noch funktioniert. "
                     "Im Gelände hilft dir das Richtungshören, beim Sport und Fliegen der Gleichgewichtssinn – bis er dich täuscht.",
                     "**Das kannst du nachher:** Entfernungen aus Schallzeiten berechnen, Dezibel richtig lesen, den Weg vom Trommelfell zur Haarzelle erklären und sagen, was dein Gehör wirklich schützt."]),
             ("hint", "Jede Stunde ist ein Abschnitt dieses Weges. Du arbeitest im Arbeitsblatt – diese Seite ist zum Nachschlagen.")]},
 {"id": "s0b", "title": "Science oder Fiction? Explosionen im Weltall", "pill": "Buch S. 61",
  "blocks": [("tiles", [("Im Film", ["In vielen Weltraumfilmen – etwa in der Star-Wars-Reihe – donnern Explosionen und heulen Triebwerke durch das All."]),
                        ("In Wirklichkeit", ["Im fast leeren Weltraum gibt es keine Teilchen, die Schall weitergeben. Eine Explosion wäre **lautlos** – "
                                             "nur Funk oder Trümmer, die das eigene Schiff treffen, würden etwas hörbar machen."])]),
             ("ul", ["**Offene Frage der Forschung:** Vögel und Fische können zerstörte Haarzellen nachbilden, Menschen nicht. Forschungsgruppen weltweit suchen nach Wegen, "
                     "diese Fähigkeit auch beim Menschen anzuschalten – heilen kann man Lärmschwerhörigkeit bis heute nicht."]),
             ("merke", "Filme hier nur in Worten – keine Filmbilder auf dieser Seite (Urheberrecht).")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("schall", "Teil 1 · Buch S. 61 · Stunde 1", "Schall ist eine Druckwelle", [
  {"id": "schall", "title": "Was schwingt, wenn wir etwas hören?", "pill": "Buch S. 61",
   "blocks": [("buch", "Lies im **Buch S. 61** die Abschnitte **»Schall«** und **»Schallfeld und Schallausbreitung«** (3 min). Markiere, was Schall braucht, um sich auszubreiten."),
              kartenblock("k1"),
              ("sim", "druckwelle"),
              ("ul", ["Eine **Schallquelle** – Stimmband, Lautsprechermembran, Stimmgabel – schwingt. Bei jedem Schwung nach vorne drückt sie die Luft davor zusammen (**Verdichtung**), beim Zurückschwingen entsteht eine **Verdünnung**.",
                      "Die Luftteilchen geben den Stoß an ihre Nachbarn weiter. Jedes Teilchen bewegt sich dabei nur Bruchteile eines Millimeters **längs** der Ausbreitungsrichtung hin und her. Das ist eine **Längswelle (Longitudinalwelle)**.",
                      "**Der Schalldruck** ist die kleine Abweichung vom normalen Luftdruck. Selbst ein lautes Gespräch ändert den Luftdruck um weniger als ein Zehntausendstel Prozent.",
                      "Schall braucht einen **Träger**: Gas, Flüssigkeit oder festen Stoff. Im Vakuum gibt es keinen Schall – das zeigt der Wecker unter der leergepumpten Glocke (Buch S. 61)."]),
              ("demo", "K2.4-D1", "Prof. HOLZER schlägt die Stimmgabel an. **Erst vermuten:** Was passiert, wenn sie ins Wasser taucht? Wenn ihr Stiel auf den Tisch drückt? "
                                  "Danach dürft ihr den Stiel am Tisch selbst spüren. Der Tisch schwingt mit und wirkt als **Resonanzkörper** – darum wird es lauter (Brücke zur Resonanz aus der Wellenlehre)."),
              ("reveal", I.STOPPFRAGEN["schall"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2", "aufgaben.html#card_a1")]),

 ("tempo", "Teil 2 · Buch S. 61, 67 · Stunde 1", "Wie schnell ist Schall?", [
  {"id": "tempo", "title": "Blitz, Donner, Echo", "pill": "Buch S. 61, 67",
   "blocks": [("buch", "Lies im **Buch S. 61** den letzten Absatz zur **Schallgeschwindigkeit** mit der Gewitterregel."),
              kartenblock("k2"),
              ("table", [["Stoff", "Schallgeschwindigkeit", "für 1 km braucht Schall"],
                         ["Luft, 0 °C", "331 m/s", "3,0 s"], ["Luft, 15 °C", "340 m/s", "2,9 s"], ["Luft, 20 °C", "343 m/s", "2,9 s"],
                         ["Wasser", "rund 1480 m/s", "0,7 s"], ["Stahl", "rund 5000 m/s", "0,2 s"]]),
              ("ul", ["**Wärmer = schneller:** In Luft steigt v um etwa 0,6 m/s pro Grad. Für Schätzungen ist das egal, für genaue Messungen nicht.",
                      "**Gewitter:** Licht ist fast eine Million Mal schneller als Schall. Zähle die Sekunden zwischen Blitz und Donner und teile durch 3 – das ergibt ungefähr die Entfernung in Kilometern.",
                      "**Echo:** Die gemessene Zeit gilt für **Hin- und Rückweg**. Darum: s = v · t / 2. Genau so messen Echolot und Fledermaus Entfernungen.",
                      "**Wellenlänge:** Mit λ = v / f hat der Kammerton a' (440 Hz) in Luft eine Wellenlänge von rund 0,77 m – tiefe Töne haben Meter, Ultraschall nur Millimeter."]),
              ("merke", "s = v · t. Beim Echo durch 2 teilen. In Luft rechnen wir mit v = 340 m/s."),
              ("reveal", I.STOPPFRAGEN["tempo"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3", "aufgaben.html#card_a2")]),

 ("tonhoehe", "Teil 3 · Buch S. 63–64, 66 · Stunde 2", "Tonhöhe, Lautstärke, Hörbereich", [
  {"id": "tonhoehe", "title": "Hoch oder tief, laut oder leise", "pill": "Buch S. 63–64",
   "blocks": [("buch", "Lies im **Buch S. 63** den Abschnitt **»Tonhöhe«** bis zur schwingenden Saite. Die Formel für die Eigenfrequenzen brauchst du nicht."),
              kartenblock("k3"),
              ("demo", "K2.4-D2", "Ein Lineal an der Tischkante: Je kürzer das schwingende Stück, desto **höher** der Ton – es schwingt öfter pro Sekunde. "
                                  "Schlägst du stärker an, wird der Ton **lauter**, aber nicht höher. Danach spielt Prof. HOLZER Töne mit dem Tongenerator am Beamer – leise, ohne Kopfhörer."),
              ("ul", ["Bei einer Gitarre gilt dasselbe: Greifst du die Saite ab, wird das schwingende Stück kürzer und der Ton höher. Stärker gespannte Saiten klingen ebenfalls höher.",
                      "**Ton, Klang, Geräusch:** Ein reiner Ton ist eine einzige Sinusschwingung. Ein Instrument erzeugt einen **Klang** aus Grundton und Obertönen – darum klingen Gitarre und Trompete verschieden. Ein **Geräusch** hat kein regelmäßiges Muster.",
                      "**Infraschall** (unter 20 Hz): Elefanten verständigen sich damit über Kilometer, auch Erdbeben und Windräder erzeugen ihn. Er ist nicht grundsätzlich gefährlich – entscheidend ist, wie stark er ist.",
                      "**Ultraschall** (über 20 000 Hz): Fledermäuse und Delfine orten damit. In der Medizin macht er Bilder vom Herz oder vom Baby im Bauch, in der Technik prüft er Werkstücke auf Risse und reinigt Brillen.",
                      "Mit dem Alter sinkt die **obere Hörgrenze** – vor allem, weil Haarzellen am Anfang der Schnecke (zuständig für hohe Töne) verloren gehen."]),
              ("hint", "Achtung beim Buch S. 63: Dort steht, dass im Alter das Trommelfell seine Elastizität verliert. Die Hauptursache der Altersschwerhörigkeit sind aber verlorene Haarzellen im Innenohr."),
              ("reveal", I.STOPPFRAGEN["tonhoehe"])]}]),

 ("dezibel", "Teil 4 · Buch S. 64, 110 · Stunde 2", "Dezibel: die Leiter in Zehnerschritten", [
  {"id": "dezibel", "title": "Warum Dezibel und nicht Pascal?", "pill": "Buch S. 64, 110",
   "blocks": [("buch", "Lies im **Buch S. 64** den Abschnitt **»Lautstärke (Schalldruckpegel)«** und sieh dir auf **S. 110** die Tabelle der Alltagsgeräusche an."),
              kartenblock("k4"),
              ("ul", ["Unser Ohr verarbeitet Schalldrücke von 0,00002 Pa (Hörschwelle) bis etwa 20 Pa an der Schmerzgrenze – das ist das Millionenfache. Damit diese riesige Spanne handlich wird, zählt man in **Zehnerstufen**: Jede Stufe von 10 dB ist **zehnmal so viel Intensität**.",
                      "**Drei Größen, nicht verwechseln:** Die **Schallintensität** ist Energie pro Fläche und Zeit (W/m²). Der **Schalldruckpegel** ist das Messergebnis in dB. Die **Lautstärke** ist, wie laut **wir** es empfinden – sie hängt zusätzlich von der Frequenz ab (am empfindlichsten sind wir zwischen etwa 500 und 5000 Hz).",
                      "**Dezibel addiert man nicht.** Zwei gleich laute Quellen liefern doppelte Intensität: Das sind nur etwa **+3 dB**. Zwei Rasenmäher mit je 90 dB ergeben rund 93 dB – nicht 180 dB.",
                      "Das Buch gibt Lautstärken in **phon** an. phon und dB stimmen nur bei 1000 Hz überein – im Alltag nennen Messgeräte und Gesetze dB."]),
              ("table", [["Beispiel", "ungefähr", "Was heißt das?"],
                         ["Hörschwelle", "0 dB", "gerade noch hörbar"], ["Flüstern", "30 dB", ""], ["Gespräch", "60 dB", ""],
                         ["Straßenverkehr", "70–80 dB", "ab 80 dB: Arbeitgeber muss Gehörschutz bereitstellen"],
                         ["Rasenmäher, Werkstatt", "85–95 dB", "ab 85 dB: Gehörschutz tragen"],
                         ["Kopfhörer voll aufgedreht, Disco, Konzert", "100–110 dB", "schon nach Minuten gefährlich"],
                         ["Schmerzgrenze", "um 120–130 dB", ""], ["Schuss am Ohr des Schützen", "über 150 dB (Spitze)", "ein einziger Knall kann schädigen"]]),
              ("hint", "Werte sind Richtwerte, gerundet. Das Buch nennt für Diskotheken auf S. 64 110 phon und auf S. 110 100 dB – beides kommt vor, je nach Musik und Platz."),
              ("reveal", I.STOPPFRAGEN["dezibel"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 4", "aufgaben.html#card_a3")]),

 ("messen", "Teil 5 · Buch S. 62–64 · Stunde 2", "Versuch: Schallpegel im langen Saal", [
  {"id": "messen", "title": "So messt ihr – und warum nur vergleichend", "pill": "Buch S. 62",
   "blocks": [("versuch", "K2.4-V1", "Vorne spielt ein Lautsprecher einen gleichmäßigen Ton. Jede Gruppe misst mit **einem** Handy. "
                                     "**1** Pegelmesser im Arbeitsblatt starten. **2** Am Lehrertisch, 1 m vor dem Lautsprecher, auf »Referenz setzen« tippen – jetzt zeigt das Handy 0 dB. "
                                     "**3** Zurück an euren Platz (Abstand steht am Boden) und messen: Ton aus, Ton an. **4** Werte eintragen, an Prof. HOLZER melden.", "aufgaben.html#card_a4"),
              ("ul", ["**Warum Referenz?** Ein Handy ist kein geeichtes Messgerät, und jedes Handy misst ein bisschen anders. Setzen alle am selben Ort auf 0 dB, fällt dieser Unterschied heraus – wir vergleichen nur noch.",
                      "**Was zu erwarten ist:** Im Freien sinkt der Pegel bei **doppeltem Abstand um etwa 6 dB** – die Energie verteilt sich auf eine viermal so große Fläche. Im Saal werfen Wände, Decke und Boden Schall zurück; der Abfall ist dann kleiner.",
                      "**Datenschutz:** Der Pegelmesser wertet das Mikrofon nur im Handy aus. Es wird nichts aufgenommen, gespeichert oder verschickt."]),
              ("merke", "Doppelter Abstand: im Freien etwa −6 dB. Abstand hilft – ersetzt aber nie den Gehörschutz.")]},
  ("jetzt", "Jetzt im Arbeitsblatt: Versuch K2.4-V1 (Aufgabe 5)", "aufgaben.html#card_a4")]),

 ("ohr", "Teil 6 · Buch S. 109–110 · Stunde 3", "Der Weg ins Ohr", [
  {"id": "ohr", "title": "Vom Trommelfell zur Haarzelle", "pill": "Buch S. 109–110",
   "blocks": [("buch", "Lies im **Buch S. 109** die Tabelle zu **Außen-, Mittel- und Innenohr** und auf **S. 110** den Abschnitt **»Hörvorgang«** (4 min)."),
              kartenblock("k5"),
              ("img", "img/hoervorgang.svg", "Die Schnecke ausgerollt: Der Steigbügel drückt auf das ovale Fenster, eine Welle läuft über die Grundmembran, an einer Stelle werden die Härchen der Haarzellen abgebogen; der Druck entweicht am runden Fenster.",
               "Die Schnecke »ausgerollt«: Hohe Töne bewegen die Grundmembran vorne, tiefe Töne weiter hinten. Dort biegen sich die Härchen – die Haarzelle meldet ein Signal."),
              ("ul", ["**Warum verstärken?** Luft ist leicht beweglich, die Lymphe im Innenohr träge wie Wasser. Ohne Hilfe würde fast der ganze Schall an der Flüssigkeit zurückgeworfen. "
                      "Das große Trommelfell drückt über die Gehörknöchelchen auf das etwa 17-mal kleinere ovale Fenster, die Hebel bringen noch etwas dazu: zusammen rund **22-facher Druck**.",
                      "**Die Ohrtrompete** verbindet Mittelohr und Rachen und gleicht den Luftdruck aus – darum hilft Schlucken beim Landeanflug.",
                      "**Haarzellen** tragen feine Härchen, die in eine Deckmembran ragen. Werden sie abgebogen, öffnen sich Ionenkanäle: Aus der Bewegung wird ein **elektrisches Signal**, das über den Hörnerv zum Gehirn geht. Erst das Gehirn macht daraus »Hören«.",
                      "**Luft- und Knochenleitung:** Schall kommt über Gehörgang und Mittelohr (Luftleitung) – oder über die Schädelknochen direkt zur Schnecke (Knochenleitung). Deine eigene Stimme hörst du über beide Wege; auf einer Aufnahme fehlt die Knochenleitung."]),
              ("versuch", "K3.2-V1", "Summe leise, halte dir dann beide Ohren mit den Fingern zu und summe weiter: Was ändert sich? Denk danach an eine Sprachnachricht mit deiner Stimme.", "aufgaben.html#card_a6"),
              ("reveal", I.STOPPFRAGEN["ohr"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgaben 6 und 7", "aufgaben.html#card_a5")]),

 ("schutz", "Teil 7 · Buch S. 109–110 · Stunde 3", "Hörschäden und Gehörschutz", [
  {"id": "schutz", "title": "Was dein Gehör wirklich schützt", "pill": "Buch S. 109–110",
   "blocks": [kartenblock("k6"),
              ("ul", ["**Lärmschwerhörigkeit** entsteht schleichend: Jahre mit zu viel Lärm zerstören nach und nach Haarzellen, zuerst für hohe Töne. Man merkt es spät – Gespräche im Lärm werden mühsam.",
                      "**Knalltrauma:** Ein Schuss, ein Böller oder eine Explosion direkt am Ohr. Spitzenpegel über 150 dB können Haarzellen sofort zerstören. In einer Studie mit über 220 000 finnischen Wehrpflichtigen hatten fast 9 von 10 Betroffenen beim Knall **keinen** Gehörschutz getragen – meist beim Schießen mit Platzpatronen.",
                      "**Tinnitus** ist ein Ohrgeräusch ohne äußere Schallquelle – Pfeifen, Rauschen, Klingeln. Er kann nach einem Knall vorübergehen oder bleiben. Wer danach Pfeifen oder dumpfes Hören bemerkt: am selben Tag zum Truppenarzt bzw. HNO-Arzt.",
                      "**Kopfhörer:** Laut einer großen Auswertung von 33 Studien (2022) hört jeder Vierte zwischen 12 und 34 Jahren über Kopfhörer zu laut. Die WHO rät: unter 60 % der Maximallautstärke bleiben und Pausen machen."]),
              ("tiles", [("Schützt zuverlässig", ["**Kapselgehörschutz**, **Schaumstoff-Stöpsel** (richtig eingesetzt!), **Otoplastik** – geprüft nach EN 352 und mit Dämmwert angegeben."]),
                         ("Schützt NICHT zuverlässig", ["**Noise-Cancelling-Kopfhörer**: Sie erzeugen Gegenschall und wirken vor allem bei gleichmäßigen, tiefen Geräuschen (Flugzeug, Zug). "
                                                        "Sie sind kein geprüfter Gehörschutz und in Lärmbereichen nicht zugelassen. Watte und Finger im Ohr reichen auch nicht."])]),
              ("hint", "Stöpsel richtig einsetzen: zwischen den Fingern dünn rollen, mit der anderen Hand das Ohr nach hinten oben ziehen, Stöpsel tief einsetzen und kurz halten, bis er sich ausdehnt."),
              ("reveal", I.STOPPFRAGEN["schutz"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 8", "aufgaben.html#card_a7")]),

 ("richtung", "Teil 8 · Buch S. 110 · Stunde 4", "Richtungshören", [
  {"id": "richtung", "title": "Woher kommt das?", "pill": "Buch S. 110",
   "blocks": [("buch", "Lies im **Buch S. 110** den Abschnitt **»Richtungshören«**. Achtung: Im Tipp beim Buchversuch steht »ca. 300 m/s« – rechne in dieser Einheit mit 340 m/s wie auf S. 61."),
              kartenblock("k7"),
              ("demo", "K3.2-D1", "Ein Freiwilliger schließt die Augen. Andere schnippen leise an verschiedenen Stellen – links, rechts, vorne, hinten, oben. Er zeigt, woher es kommt. "
                                  "Danach dasselbe mit einem zugehaltenen Ohr. **Vorher vermuten:** Wo wird er sich am häufigsten irren?"),
              ("ul", ["Bei tiefen Tönen wertet das Gehirn vor allem den **Zeitunterschied** aus, bei hohen Tönen den **Pegelunterschied**: Der Kopf wirft einen »Schallschatten« auf das abgewandte Ohr.",
                      "Im Gelände, im Straßenverkehr und auf dem Schießplatz ist schnelles Orten lebenswichtig. Mit einem Ohr oder mit dichtem Gehörschutz ist es deutlich schwerer – darum gibt es Gehörschutz mit Durchhörfunktion, der Sprache durchlässt und Knalle begrenzt."]),
              ("reveal", I.STOPPFRAGEN["richtung"])]}]),

 ("gleichgewicht", "Teil 9 · Buch S. 111–112 · Stunde 4", "Gleichgewicht: Lage- und Drehsinn", [
  {"id": "gleichgewicht", "title": "Wo ist oben – und drehe ich mich?", "pill": "Buch S. 111–112",
   "blocks": [("buch", "Lies im **Buch S. 112** die Abschnitte **»Lagesinn«** und **»Drehsinn«** (3 min)."),
              kartenblock("k8"),
              ("demo", "K3.2-D2", "Prof. HOLZER dreht ein Glas Wasser mit Papierschnipseln: Am Anfang bleibt das Wasser zurück, nach dem Stoppen dreht es noch weiter. "
                                  "Genau so verhält sich die **Lymphe** in deinen Bogengängen. Keine Drehversuche am eigenen Körper – Sturzgefahr."),
              ("img", "img/bogengang.svg", "Drei Bilder eines Bogengangs: Drehung beginnt – Lymphe bleibt zurück, Kuppel biegt sich. Gleichmäßige Drehung – Kuppel steht gerade. Stopp – Lymphe fließt weiter, Kuppel biegt sich in die andere Richtung.",
               "Beginn, gleichmäßige Drehung, Stopp: Nur Änderungen biegen die Kuppel."),
              ("ul", ["**Drehschwindel:** Nach langem Drehen hast du dich »angepasst«. Beim Stoppen fließt die Lymphe weiter und meldet eine Drehung in die Gegenrichtung – die Augen sehen aber Stillstand. Dieser Widerspruch ist Schwindel.",
                      "**Piloten:** In Wolken oder nachts fehlt der Blick nach draußen. Eine lange, gleichmäßige Kurve fühlt sich nach einiger Zeit wie Geradeausflug an. Wer dem Gefühl folgt, gerät in eine Spirale. Die Regel lautet: **den Instrumenten vertrauen, nicht dem Körper**.",
                      "**Seekrankheit:** Im Schiffsinneren sieht alles ruhig aus, das Gleichgewichtsorgan meldet aber Schaukeln. Hilfe: an Deck gehen und den Horizont anschauen.",
                      "**Sport:** Eiskunstläufer und Tänzer drehen den Kopf ruckartig und halten einen Punkt mit den Augen fest (»Spotting«). Das Training dämpft außerdem die Reaktion des Gehirns auf die Bogengang-Signale."]),
              ("reveal", I.STOPPFRAGEN["gleichgewicht"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 9", "aufgaben.html#card_a8")]),
]

SCHNELLE = [
 {"id": "schnell1", "title": "Ultraschall, Echolot und Wale", "pill": "OPTIONAL · Buch S. 60, 66",
  "blocks": [("ul", ["**Zusatzaufgabe 10** rechnet mit Echolot und Fledermaus. Filmtipp aus dem Schulbuch (S. 60): trauner.at/nawi_v52.aspx.",
                     "**Ökologie:** Wale und Delfine verständigen sich über weite Strecken mit Schall. Schiffsmotoren, Sonar und Bauarbeiten im Meer übertönen ihre Rufe – ein wachsendes Problem für Tiere, die sich im Dunkeln nur über das Hören orientieren.",
                     "**Medizin:** Ultraschall erwärmt Gewebe nur wenig und strahlt nicht wie Röntgen. Darum ist er für Untersuchungen in der Schwangerschaft das Mittel der Wahl."])]},
 {"id": "schnell2", "title": "Kurz zum Dopplereffekt (kein Teststoff)", "pill": "OPTIONAL · Buch S. 65",
  "blocks": [("ul", ["Fährt ein Einsatzfahrzeug mit Folgetonhorn vorbei, klingt der Ton beim Näherkommen höher und beim Wegfahren tiefer. Die Wellen werden vorne zusammengeschoben und hinten auseinandergezogen.",
                     "Das Phänomen heißt **Dopplereffekt** (Buch S. 65). In dieser Einheit ist es **kein Teststoff**."])]},
 {"id": "schnell3", "title": "Für Neugierige: Wie viel Energie steckt im Schall?", "pill": "OPTIONAL",
  "blocks": [("ul", ["Ein Gespräch hat eine Schallintensität von nur etwa einem Millionstel Watt pro Quadratmeter. Um mit der Schallenergie eines Gesprächs eine Tasse Tee zu erwärmen, müsste man über hundert Jahre ununterbrochen reden.",
                     "Trotzdem reicht dieser winzige Druck, um deine Haarzellen zu reizen – das Ohr ist eines der empfindlichsten Messgeräte, die es gibt."]),
             ("hint", "Zusatzaufgaben und Zusatztexte zählen nicht zum Pflichtfortschritt und sind keine Hausübung.")]},
]
