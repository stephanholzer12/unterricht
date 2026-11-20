"""Theorie-Seite K3.1/K3.6 Körper unter Belastung: Theorie-Karten, Teile und Abschnitte.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufe 2 im Arbeitsblatt (Theorie-Karte) und die KURZ-KLÄREN-Folien der Beamer-Präsentation.
Block-Arten: tiles, ul, ol, merke, hint, table, reveal, img (Datei, Alt, Unterschrift), buch, karte, gemeinsam, sim (Simulation aus sims.py), extern (Link), demo (ID, Text), versuch (ID, Text, Anker), film (Titel, Link, Text).
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py, SVG). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "herz": "1 Herz", "kreislauf": "2 Kreislauf", "gefaesse": "3 Gefäße", "puls": "4 Puls", "knochen": "5 Knochen",
          "gelenke": "6 Gelenke", "blut": "7 Blut", "blutgruppen": "8 Blutgruppen", "muskeln": "9 Muskeln", "ergonomie": "10 Ergonomie",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

KARTEN = {
 "k1": {"titel": "Das Herz: vier Räume, vier Ventile", "teil": "herz", "buch": "Buch S. 77–78", "bild": "img/herz.svg",
        "alt": "Schema des Herzens von vorne: rechter Vorhof und rechte Kammer blau, linker Vorhof und linke Kammer rot, dazwischen die Scheidewand. Segelklappen zwischen Vorhof und Kammer, Taschenklappen am Ausgang zu Lungenarterie und Aorta. Die Kammern ziehen sich abwechselnd zusammen.",
        "satz": ["Das **Herz** ist ein faustgroßer **Hohlmuskel**. Eine **Scheidewand** teilt es in zwei Hälften mit je einem **Vorhof** und einer **Kammer**.",
                 "**Systole**: Die Kammern ziehen sich zusammen und pressen das Blut in die Arterien. **Diastole**: Sie erschlaffen und füllen sich.",
                 "**Segelklappen** (Vorhof–Kammer) und **Taschenklappen** (Kammer–Arterie) wirken wie das **Ventil am Fahrradreifen**: nur eine Richtung."],
        "formeln": [("rechts", "sauerstoffarmes Blut → Lunge", ""), ("links", "sauerstoffreiches Blut → Körper", ""), ("Größe", "wie eine Faust, rund 300 g", "")],
        "link": "theorie.html#herz"},
 "k2": {"titel": "Zwei Kreisläufe – eine Acht", "teil": "kreislauf", "buch": "Buch S. 77, 79–80", "bild": "img/kreislauf.svg",
        "alt": "Kreislauf als Acht: oben die Lunge, unten der Körper, in der Mitte das Herz mit rechter und linker Hälfte. Rote Punkte wandern von der Lunge über die linke Herzhälfte in den Körper, blaue Punkte vom Körper über die rechte Hälfte zur Lunge.",
        "satz": ["**Lungenkreislauf**: rechte Kammer → **Lungenarterie** → Lunge (CO₂ ab, O₂ auf) → **Lungenvene** → linker Vorhof.",
                 "**Körperkreislauf**: linke Kammer → **Aorta** → Arterien → Kapillaren der Organe → Venen → **Hohlvenen** → rechter Vorhof.",
                 "**Arterie** heißt »vom Herzen weg«, **Vene** »zum Herzen hin« – egal, ob das Blut sauerstoffreich oder -arm ist."],
        "formeln": [], "link": "theorie.html#kreislauf"},
 "k3": {"titel": "Arterie, Vene, Kapillare", "teil": "gefaesse", "buch": "Buch S. 79", "bild": "img/gefaesse.svg",
        "alt": "Links eine Arterie mit dicker, elastischer Wand, rechts eine Vene mit dünner Wand und einer Klappe, die sich öffnet und schließt. Dazwischen ein feines Netz aus Kapillaren.",
        "satz": ["**Arterien**: dicke, elastische Wand, hoher Druck. **Venen**: dünne Wand, niedriger Druck, **Venenklappen** als Rückschlagventile.",
                 "In den **Kapillaren** ist die Wand hauchdünn: Hier gehen Sauerstoff und Nährstoffe in die Zellen, CO₂ und Abfall zurück ins Blut.",
                 "**Herzminutenvolumen = Schlagvolumen · Puls**: in Ruhe rund 70 ml · 70 pro Minute ≈ **5 l pro Minute**."],
        "formeln": [("HMV", "Herzminutenvolumen: Blut pro Minute", "l/min"), ("SV", "Schlagvolumen: Blut pro Herzschlag", "ml"), ("HF", "Herzfrequenz = Puls", "pro min"),
                    ("HMV = SV · HF", "70 ml · 70 = 4900 ml ≈ 5 l", ""), ("1 l", "= 1000 ml", "")],
        "link": "theorie.html#gefaesse"},
 "k4": {"titel": "Puls und Blutdruck", "teil": "puls", "buch": "Buch S. 80–81", "bild": "img/blutdruck.svg",
        "alt": "Kurve des Drucks in einer Arterie über zwei Herzschläge: Spitzen beim Auspressen (systolisch, etwa 120 mmHg), Täler in der Füllphase (diastolisch, etwa 80 mmHg). Darunter ein Handgelenk mit zwei Fingern an der Speichenarterie.",
        "satz": ["Der **Puls** ist die Druckwelle, die bei jedem Herzschlag durch die Arterien läuft. In Ruhe meist **60–80 pro Minute**.",
                 "Der **Blutdruck** hat zwei Werte in **mmHg**: **systolisch** (beim Auspressen) und **diastolisch** (in der Füllphase). Optimal: unter **120/80**.",
                 "Bei Belastung steigen Puls und Schlagvolumen – die Muskeln bekommen mehr Sauerstoff. Nach der Belastung sinkt der Puls wieder."],
        "formeln": [("mmHg", "Millimeter Quecksilbersäule, Druckeinheit beim Blutdruck", ""), ("120/80", "systolisch / diastolisch", "mmHg")],
        "link": "theorie.html#puls"},
 "k5": {"titel": "Der Röhrenknochen: leicht und stabil", "teil": "knochen", "buch": "Buch S. 108", "bild": "img/knochen.svg",
        "alt": "Längsschnitt durch einen Oberschenkelknochen: außen die Beinhaut, der feste Knochenschaft mit Markhöhle (gelbes Mark), an den Enden schwammartige Knochenbälkchen mit rotem Knochenmark, Wachstumsfugen und Gelenkknorpel.",
        "satz": ["Das **Skelett** stützt, macht Bewegung möglich, **schützt** Organe und bildet im **roten Knochenmark** Blutzellen.",
                 "Innen ist der Knochen ein Gerüst aus **Knochenbälkchen** – Material nur dort, wo Kräfte wirken (**Leichtbau** wie beim Kran).",
                 "In die Länge wächst der Knochen an der **Wachstumsfuge**. Die **Beinhaut** ernährt ihn und hilft beim Heilen."],
        "formeln": [("Sehne", "verbindet Muskel und Knochen", ""), ("Band", "verbindet Knochen mit Knochen", ""), ("Knorpel", "glatt, elastisch: Gleiten, Dämpfen", "")],
        "link": "theorie.html#knochen"},
 "k6": {"titel": "Gelenke: Kugel, Scharnier, Dreh", "teil": "gelenke", "buch": "Buch S. 109", "bild": "img/gelenke.svg",
        "alt": "Oben der Aufbau eines Gelenks: Gelenkkopf, Gelenkpfanne, Knorpel, Kapsel, Gelenkschmiere, Band. Unten drei Symbole: Kugelgelenk mit Pfeilen in alle Richtungen, Scharniergelenk mit Pfeil auf und zu, Drehgelenk mit Kreispfeil.",
        "satz": ["Ein **Gelenk** besteht aus **Gelenkkopf** und **Gelenkpfanne** mit **Knorpel**, umhüllt von der **Gelenkkapsel**. Die **Gelenkschmiere** ernährt den Knorpel und lässt die Flächen gleiten, **Bänder** geben Halt.",
                 "**Kugelgelenk**: Bewegung in alle Richtungen (Schulter, Hüfte). **Scharniergelenk**: nur auf und zu (Ellbogen, Finger).",
                 "**Drehgelenk**: Ein Knochen dreht sich um den anderen (Elle–Speiche, 1. und 2. Halswirbel)."],
        "formeln": [], "link": "theorie.html#gelenke"},
 "k7": {"titel": "Blut: Zellen und Plasma", "teil": "blut", "buch": "Buch S. 81–83", "bild": "img/blut.svg",
        "alt": "Ein Röhrchen Blut nach dem Zentrifugieren: unten etwa 45 Prozent Blutzellen, oben etwa 55 Prozent gelbliches Plasma. Daneben rote Blutkörperchen als Scheiben, ein weißes Blutkörperchen und Blutplättchen.",
        "satz": ["Ein Erwachsener hat rund **5–6 l Blut**: etwa **45 % Zellen** und **55 % Plasma** (vor allem Wasser mit Eiweißen, Salzen, Nährstoffen).",
                 "**Rote Blutkörperchen** (Erythrozyten) tragen mit dem eisenhaltigen **Hämoglobin** Sauerstoff. **Weiße** (Leukozyten) wehren Erreger ab. **Blutplättchen** (Thrombozyten) verschließen Wunden.",
                 "Alle Blutzellen entstehen im **roten Knochenmark**. Rote Blutkörperchen leben rund **120 Tage**."],
        "formeln": [("Hämatokrit", "Anteil der Zellen am Blut", "%"), ("Erythrozyten", "rund 5 Millionen pro µl", ""), ("Leukozyten", "4000–10 000 pro µl", ""),
                    ("Thrombozyten", "150 000–400 000 pro µl", "")],
        "link": "theorie.html#blut"},
 "k8": {"titel": "Blutgruppen: Antigene und Antikörper", "teil": "blutgruppen", "buch": "Buch S. 84–85", "bild": "img/blutgruppen.svg",
        "alt": "Vier rote Blutkörperchen: Gruppe A mit Merkmal A, Gruppe B mit Merkmal B, Gruppe AB mit beiden, Gruppe 0 ohne Merkmal. Darunter die Antikörper im Plasma: A hat Anti-B, B hat Anti-A, AB keine, 0 beide.",
        "satz": ["Die **Blutgruppe** hängt von den **Antigenen** auf den roten Blutkörperchen ab: **A**, **B**, beide (**AB**) oder keines (**0**).",
                 "Im Plasma sitzen **Antikörper** gegen das fehlende Antigen. Treffen sie auf passende Blutkörperchen, **verklumpen** diese.",
                 "Darum verträgt **0** nur rote Konserven der Gruppe 0, **AB** dagegen alle. Dazu kommt der **Rhesusfaktor** (rund 85 % Rh+)."],
        "formeln": [("Verklumpt mit Anti-A", "Antigen A ist da", ""), ("Verklumpt mit Anti-B", "Antigen B ist da", ""), ("mit keinem", "Blutgruppe 0", "")],
        "link": "theorie.html#blutgruppen"},
 "k9": {"titel": "Muskeln: ziehen, nie drücken", "teil": "muskeln", "buch": "Buch S. 110–111", "bild": "img/muskel.svg",
        "alt": "Ein Arm wird gebeugt und gestreckt: Beim Beugen wird der Bizeps vorne am Oberarm kurz und dick, beim Strecken zieht der Trizeps hinten. Die Sehnen verbinden die Muskeln mit den Knochen.",
        "satz": ["Ein Skelettmuskel besteht aus **Muskelfasern** mit Eiweißfäden (**Actin, Myosin**). Sie schieben sich ineinander – der Muskel **verkürzt** sich. Energie: **ATP**.",
                 "Ein Muskel kann nur **ziehen**. Darum arbeiten **Spieler und Gegenspieler** zusammen: **Bizeps** beugt, **Trizeps** streckt den Arm.",
                 "**Langsame Fasern** (Typ I) sind ausdauernd und brauchen Sauerstoff – Marathon. **Schnelle Fasern** (Typ II) sind kräftig, ermüden aber rasch – Sprint, Gewichtheben."],
        "formeln": [("ATP", "Energieträger der Zelle, entsteht v. a. in der Zellatmung mit Sauerstoff", "")],
        "link": "theorie.html#muskeln"},
 "k10": {"titel": "Ergonomie: Arbeit an den Menschen anpassen", "teil": "ergonomie", "buch": "Buch S. 112–113", "bild": "img/hebel.svg",
         "alt": "Zwei Personen tragen dieselbe Kiste: links nah am Körper mit kurzem Hebel und kleinem Kraftpfeil im Rücken, rechts weit vor dem Körper mit langem Hebel und großem Kraftpfeil.",
         "satz": ["**Ergonomie** passt Arbeitsplatz und Arbeitsmittel an den Menschen an – das schützt die Gesundheit und steigert die Leistung (humane und wirtschaftliche Ziele).",
                  "**Heben**: Last **nah am Körper**, aus den Beinen, Rücken gerade, nicht verdrehen. Je weiter die Last weg ist, desto stärker müssen die Rückenmuskeln ziehen (**Hebel**).",
                  "**Sitzen**: Füße flach am Boden, Knie etwa im rechten Winkel, Rückenlehne nutzen, Bildschirm **nicht über Augenhöhe** – und immer wieder aufstehen."],
         "formeln": [("Hebel", "Kraft · Kraftarm = Last · Lastarm", ""), ("Beispiel", "100 N Last, 40 cm vor der Wirbelsäule, Kraftarm 5 cm → 800 N", "vereinfacht")],
         "link": "theorie.html#ergonomie"},
 "k11": {"titel": "Alles auf einen Blick", "teil": "kurz", "buch": "Buch S. 76–85, 107–114", "bild": "img/ueberblick.svg",
         "alt": "Ein Körper mit vier verbundenen Stationen: Herz pumpt, Blut transportiert Sauerstoff, Knochen tragen und bilden Blut, Muskeln ziehen. Pfeile zeigen die Verbindungen.",
         "satz": ["**Herz** pumpt (rechts Lunge, links Körper) → **Blut** bringt Sauerstoff → **Muskeln** ziehen an den **Knochen** → im **Knochenmark** entsteht neues Blut.",
                  "Rechnen: **Herzminutenvolumen = Schlagvolumen · Puls**, Hebel: **Kraft · Kraftarm = Last · Lastarm**.",
                  "Merken: Arterie = vom Herzen weg · 0 verträgt nur 0 · Muskeln ziehen nur · Last nah am Körper."],
         "formeln": [], "link": "theorie.html#kurz"},
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
 {"id": "s0a", "title": "Der Körper unter Belastung", "pill": "Buch S. 75–76, 107",
  "blocks": [("img", "img/ueberblick.svg", KARTEN["k11"]["alt"], "Der Weg dieser Einheit: Herz, Blut, Knochen und Muskeln arbeiten zusammen."),
             ("ul", ["**Das Wichtigste vorab:** Wenn du läufst, marschierst oder eine Kiste hebst, arbeitet dein ganzer Körper zusammen: Das Herz pumpt schneller, "
                     "das Blut bringt Sauerstoff zu den Muskeln, die Muskeln ziehen an den Knochen – und im Knochenmark entsteht ständig neues Blut.",
                     "**Wozu?** Beim Sport willst du wissen, was dein Puls dir sagt. Beim Marsch oder in der Arbeit willst du heben und sitzen, ohne dass dir mit 30 der Rücken wehtut. "
                     "Und wenn jemand Blut braucht, ist es gut zu wissen, welche Konserve passt.",
                     "**Das kannst du nachher:** den Weg des Blutes erklären, deinen Puls messen und deuten, Blutgruppen lesen, Gelenke am Skelett zeigen und deinen Arbeitsplatz ergonomisch prüfen."]),
             ("hint", "Jede Stunde ist ein Abschnitt dieses Weges. Du arbeitest im Arbeitsblatt – diese Seite ist zum Nachschlagen. Oben siehst du, welche Teile zu welcher Stunde gehören.")]},
 {"id": "s0b", "title": "Science oder Fiction? »Bone-Smashing« für ein markantes Kinn", "pill": "Buch S. 108",
  "blocks": [("tiles", [("Im Netz", ["Auf Social Media zeigen manche, wie sie sich mit einem Hammer auf Kiefer und Wangen klopfen. Die Behauptung: Der Knochen wächst danach kräftiger nach."]),
                        ("In Wirklichkeit", ["In die Länge wachsen Knochen nur an den **Wachstumsfugen**. Dicker und fester werden sie durch regelmäßige **Belastung** wie Training – nicht durch Verletzungen. Ein Bruch **heilt** ungeordnet mit einem Knochenwulst – oft schief, mit Schwellung oder Nervenschaden. "
                                             "Ärzte nennen die Idee »abstrus« und warnen vor bleibenden Verformungen (ZDFheute, 10.07.2025)."])]),
             ("ul", ["**Offene Frage der Forschung:** Knochen bauen sich ein Leben lang um und werden durch Belastung tatsächlich stärker – Training ist dafür gut. "
                     "Wie genau die Knochenzellen »spüren«, wo Kraft wirkt, untersucht die Forschung bis heute."]),
             ("merke", "Klopfen und Schlagen ist kein Training. Knochen werden durch Bewegung und Sport stärker – nicht durch Verletzungen.")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("herz", "Teil 1 · Buch S. 77–78 · Stunde 1", "Das Herz", [
  {"id": "herz", "title": "Ein Muskel, der nie Pause macht", "pill": "Buch S. 77–78",
   "blocks": [("buch", "Lies im **Buch S. 77** den Text unter der Herz-Abbildung und die Tabelle **»Aufgabe der beiden Herzhälften«** (3 min). Markiere, wo das Blut die Lunge verlässt."),
              kartenblock("k1"),
              ("demo", "K3.1-D1", "Prof. HOLZER nimmt das Herz aus dem Torso. **Erst vermuten:** Wo genau liegt es? Wie groß ist es? Dann zeigt er die vier Räume und die großen Gefäße. "
                                  "Achtung: Im Bild schaust du von vorne auf den Menschen – seine **rechte** Herzhälfte ist für dich **links**."),
              ("ul", ["Das Herz liegt hinter dem Brustbein, die **Herzspitze** zeigt nach links unten. Es ist etwa so groß wie eine Faust und wiegt rund 300 g.",
                      "Die Herzwand ist vor allem **Herzmuskelgewebe**. Es wird über eigene Gefäße versorgt, die **Herzkranzgefäße**. Werden sie verstopft, droht ein Herzinfarkt.",
                      "Den Takt gibt das Herz **selbst** vor: Spezielle Muskelzellen erzeugen rhythmisch elektrische Erregungen. Das Nervensystem macht den Takt nur schneller oder langsamer.",
                      "Der **Vorhof** sammelt das Blut und drückt es in die **Kammer**. Die Kammer ist viel kräftiger – sie pumpt das Blut in die Arterien. Die Wand der **linken** Kammer ist am dicksten, weil sie das Blut durch den ganzen Körper drücken muss."]),
              ("film", "Filmtipp aus dem Schulbuch: Aufbau und Funktion des Herzens", "https://www.trauner.at/nawi_v120.aspx", "Video des Verlags (Buch S. 78) · öffnet in einem neuen Tab"),
              ("reveal", I.STOPPFRAGEN["herz"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2", "aufgaben.html#card_a1")]),

 ("kreislauf", "Teil 2 · Buch S. 77, 79–80 · Stunde 1", "Zwei Kreisläufe", [
  {"id": "kreislauf", "title": "Lungenkreislauf und Körperkreislauf", "pill": "Buch S. 79–80",
   "blocks": [kartenblock("k2"),
              ("ul", ["Stell dir eine **Acht** vor: Die obere Schleife führt zur Lunge, die untere durch den Körper. In der Mitte sitzt das Herz – zwei Pumpen in einem Muskel, die im gleichen Takt schlagen.",
                      "In der **Lunge** gibt das Blut Kohlenstoffdioxid ab und nimmt Sauerstoff auf. In den **Organen** ist es umgekehrt.",
                      "Das Blut aus Magen und Darm fließt zuerst über die **Pfortader** in die **Leber**. Sie entgiftet und verarbeitet die Nährstoffe, erst dann geht es zurück zum Herzen.",
                      "Wie viel Blut ein Organ bekommt, wird geregelt: Beim Sport fließt viel mehr Blut in die Muskeln, nach dem Essen mehr in den Darm."]),
              ("table", [["Gefäß", "Richtung", "Blut ist …"], ["Aorta", "vom Herzen weg (Körper)", "sauerstoffreich"], ["Hohlvenen", "zum Herzen hin (aus dem Körper)", "sauerstoffarm"],
                         ["Lungenarterie", "vom Herzen weg (zur Lunge)", "**sauerstoffarm**"], ["Lungenvenen", "zum Herzen hin (aus der Lunge)", "**sauerstoffreich**"]]),
              ("merke", "Arterie = vom Herzen weg, Vene = zum Herzen hin. Die Farbe in Zeichnungen (rot/blau) zeigt den Sauerstoff, nicht den Gefäßtyp."),
              ("reveal", I.STOPPFRAGEN["kreislauf"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3 (per Hand)", "aufgaben.html#card_a2")]),

 ("gefaesse", "Teil 3 · Buch S. 79 · Stunde 2", "Blutgefäße", [
  {"id": "gefaesse", "title": "Drei Arten von Leitungen", "pill": "Buch S. 79",
   "blocks": [kartenblock("k3"),
              ("sim", "hmv"),
              ("demo", "K3.1-D2", "Prof. HOLZER zeigt es am eigenen Unterarm: Ein Finger drückt eine sichtbare Vene nahe am Handgelenk ab, ein zweiter streicht sie **Richtung Ellbogen** aus. **Erst vermuten:** Füllt sie sich sofort wieder? "
                                  "Die Vene bleibt bis zur nächsten **Klappe** leer – das Blut kann nicht zurück. Erst wenn der erste Finger loslässt, füllt sie sich von der Hand her. Ihr dürft es danach an euch selbst probieren (nicht bei jedem sind Venen gut sichtbar)."),
              ("ul", ["Die **Arterienwand** hat eine dicke Schicht aus Muskel- und elastischen Fasern. Sie dehnt sich bei jedem Herzschlag und federt zurück – darum fließt das Blut gleichmäßiger.",
                      "In den **Venen** ist der Druck niedrig. Damit das Blut aus den Beinen nach oben kommt, helfen die **Venenklappen** und die **Muskelpumpe**: Die Beinmuskeln drücken beim Gehen die Venen zusammen.",
                      "Wer lange steht oder sitzt, bekommt schwere Beine – die Muskelpumpe fehlt. Darum ist **Bewegung** auch für die Venen gut. Ausgeleierte Venen mit undichten Klappen heißen **Krampfadern**.",
                      "Insgesamt ist das Gefäßnetz eines Erwachsenen sehr lang – die meisten Kilometer sind Kapillaren."]),
              ("reveal", I.STOPPFRAGEN["gefaesse"])]}]),

 ("puls", "Teil 4 · Buch S. 80–81 · Stunde 2", "Puls und Blutdruck", [
  {"id": "puls", "title": "Was dein Herz beim Training macht", "pill": "Buch S. 80–81",
   "blocks": [("buch", "Lies im **Buch S. 80** die Abschnitte **»3.3 Puls«** und **»3.4 Blutdruck«**."),
              kartenblock("k4"),
              ("versuch", "K3.1-V1", "Zu zweit: Ruhepuls messen, 20 Kniebeugen, sofort wieder messen, nach 3 Minuten noch einmal. Freiwillig – wer nicht mitmacht, misst und schreibt mit.", "aufgaben.html#card_a3"),
              ("ul", ["**Tastpunkt:** Speichenarterie an der Innenseite des Handgelenks (daumenseitig). Mit zwei Fingern fühlen, nicht mit dem Daumen. Am Hals tasten wir in der Schule nicht – Druck dort kann Schwindel auslösen.",
                      "**Ruhepuls** meist 60–80 pro Minute. Ausdauertrainierte haben oft weniger: Ihr Herz schafft pro Schlag mehr Blut.",
                      "**Blutdruck** in mmHg: optimal unter 120/80; normal 120–129/80–84; hoch normal 130–139/85–89; ab 140/90 spricht man von Bluthochdruck (Leitlinie der Europäischen Hypertonie-Gesellschaft ESH, 2023). Das Buch nennt auf S. 80 für »normal« diastolisch unter 90 – die Leitlinie zieht die Grenze bei 85.",
                      "Eine einzelne Messung ist **keine Diagnose**. Aufregung, Kaffee oder Treppensteigen ändern Puls und Blutdruck. Beurteilen darf das nur eine Ärztin oder ein Arzt."]),
              ("hint", "Achtung beim Buch S. 81: Im Beispiel stehen 115 ml pro Herzschlag – das ist für Ruhe viel. Links daneben steht 70–120 ml. Wir rechnen in Ruhe mit rund 70 ml."),
              ("reveal", I.STOPPFRAGEN["puls"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: VERSUCH (Aufgabe 4) und Aufgabe 5", "aufgaben.html#card_a3")]),

 ("knochen", "Teil 5 · Buch S. 107–108 · Stunde 3", "Knochen", [
  {"id": "knochen", "title": "Ein Gerüst, das lebt", "pill": "Buch S. 108",
   "blocks": [("buch", "Lies im **Buch S. 108** den Abschnitt **»1.1.1 Bau der Knochen am Beispiel des Röhrenknochens«** mit der Abbildung (3 min)."),
              kartenblock("k5"),
              ("demo", "K3.6-D1", "Prof. HOLZER zeigt am **Skelett-Modell** den Oberschenkelknochen, dazu die Abbildung im **Buch S. 108**. **Erst vermuten:** Ist ein Röhrenknochen innen massiv? Dann zeigt die Abbildung die Bälkchen und die Markhöhle."),
              ("ul", ["Der Mensch hat **über 200 Knochen** (beim Erwachsenen meist 206). Formen: **Röhrenknochen** (Oberschenkel), **kurze** (Handwurzel), **platte** (Schulterblatt, Schädel), **unregelmäßige** (Wirbel).",
                      "Knochen ist hart durch **Kalk** (Calciumphosphat) und elastisch durch **Eiweißfasern** (Kollagen). Beides zusammen macht ihn bruchfest.",
                      "Knochen ist **lebendes Gewebe**: Er wird ständig ab- und aufgebaut. Wer trainiert, bekommt dichtere Knochen; wer lange liegt oder im Weltall schwebt, verliert Knochenmasse.",
                      "**Sehne** (Muskel–Knochen), **Band** (Knochen–Knochen) und **Knorpel** (Gleiten, Dämpfen) gehören mit Muskeln und Knochen zum **Bewegungsapparat** (Hölzel S. 105)."]),
              ("reveal", I.STOPPFRAGEN["knochen"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 6", "aufgaben.html#card_a5")]),

 ("gelenke", "Teil 6 · Buch S. 109–110 · Stunde 3", "Gelenke", [
  {"id": "gelenke", "title": "Kugel, Scharnier, Dreh", "pill": "Buch S. 109",
   "blocks": [kartenblock("k6"),
              ("ul", ["**Feste Knochenverbindungen** bewegen sich nicht: die **Nähte** der Schädelknochen, das zusammengewachsene **Kreuzbein**.",
                      "**Gelenke** sind bewegliche Verbindungen. Probier es an dir: Arm kreisen (Kugel), Ellbogen beugen (Scharnier), Handfläche nach oben und unten drehen (Dreh).",
                      "Das **Knie** ist eigentlich ein Mischgelenk: Gestreckt ist es ein Scharnier, gebeugt kann sich der Unterschenkel ein wenig drehen. Zwei **Menisken** aus Knorpel dämpfen dort zusätzlich.",
                      "**Schleimbeutel** in der Nähe der Gelenke polstern Stellen mit viel Druck (Buch S. 109)."]),
              ("gemeinsam", "GRUPPENARBEIT Skelett-Rallye (Aufgabe 7): Jede Gruppe sucht ihre Körperregion am Modell und am eigenen Körper und zeigt am Ende in 30 Sekunden Knochen und Gelenktyp."),
              ("reveal", I.STOPPFRAGEN["gelenke"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: GRUPPENARBEIT Aufgabe 7", "aufgaben.html#card_a6")]),

 ("blut", "Teil 7 · Buch S. 81–83 · Stunde 4", "Blut", [
  {"id": "blut", "title": "Transport, Abwehr, Reparatur", "pill": "Buch S. 81–83",
   "blocks": [("buch", "Lies im **Buch S. 82** den Kasten zu den **Bestandteilen des Blutes** (2 min)."),
              kartenblock("k7"),
              ("img", "img/gerinnung.svg", "Drei Schritte einer Wunde: Das Gefäß zieht sich zusammen, Blutplättchen lagern sich an und bilden einen Pfropf, Fibrinfäden spinnen ein Netz, in dem sich rote Blutkörperchen fangen.",
               "Blutgerinnung in drei Schritten: Gefäß verengt sich – Blutplättchen-Pfropf – Fibrinnetz."),
              ("ul", ["**Aufgaben des Blutes:** Transport (Sauerstoff, CO₂, Nährstoffe, Abfallstoffe, Hormone, Wärme), Abwehr (weiße Blutkörperchen) und Reparatur (Gerinnung).",
                      "**Blutgerinnung:** Zuerst verengt sich das verletzte Gefäß. Dann lagern sich **Blutplättchen** an (Pfropf, nach 1 bis 3 Minuten). Zuletzt bildet sich aus dem gelösten **Fibrinogen** ein Netz aus **Fibrin**, in dem sich Blutkörperchen fangen – ein fester Wundverschluss, später eine Narbe.",
                      "**Blutbefund:** Die Werte hängen von Alter und Geschlecht ab (Tabelle Buch S. 83). Zu wenig Hämoglobin kann auf **Eisenmangel** hinweisen, viele weiße Blutkörperchen auf eine **Infektion**. Die Beurteilung macht immer eine Ärztin.",
                      "**Blutdoping:** Das Hormon **EPO** regt das Knochenmark an, mehr rote Blutkörperchen zu bilden. Der **Hämatokrit** steigt, das Blut trägt mehr Sauerstoff – wird aber **dicker**. Gerinnsel, Herzinfarkt und Schlaganfall werden wahrscheinlicher. EPO-Doping ist verboten."]),
              ("gemeinsam", "GRUPPENARBEIT Blutdoping (Aufgabe 9): Vier Rollen – Radprofi, Teamärztin, Dopingkontrolle, Nachwuchs-Sportlerin. Danach DISKUSSION mit Prof. HOLZER."),
              ("reveal", I.STOPPFRAGEN["blut"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 8", "aufgaben.html#card_a7")]),

 ("blutgruppen", "Teil 8 · Buch S. 84–85 · Stunde 4", "Blutgruppen", [
  {"id": "blutgruppen", "title": "Welche Konserve passt?", "pill": "Buch S. 84–85",
   "blocks": [kartenblock("k8"),
              ("sim", "blutgruppe"),
              ("table", [["Blutgruppe", "Antigen auf den roten Blutkörperchen", "Antikörper im Plasma", "verträgt rote Konserven", "Häufigkeit (Buch, gerundet)"],
                         ["A", "A", "Anti-B", "A, 0", "45 %"], ["B", "B", "Anti-A", "B, 0", "10 %"], ["AB", "A und B", "keine", "A, B, AB, 0", "5 %"], ["0", "keines", "Anti-A und Anti-B", "nur 0", "40 %"]]),
              ("ul", ["Der Österreicher **Karl Landsteiner** entdeckte das AB0-System 1901 und bekam dafür 1930 den Nobelpreis.",
                      "**Rhesusfaktor:** Wer das Antigen D hat, ist Rhesus-positiv (rund 85 %). Antikörper gegen D bildet ein Rhesus-negativer Mensch erst nach Kontakt – etwa bei einer Schwangerschaft mit einem Rh+-Kind. Heute verhindern Spritzen in der Schwangerschaft und nach der Geburt die Gefahr für das nächste Kind.",
                      "In der Klinik gibt man möglichst **dieselbe** Blutgruppe. Die Regel »0 für alle« gilt nur im Notfall – und nur für rote Konserven der Gruppe **0 Rhesus-negativ**.",
                      "In Österreich wird laut Rotem Kreuz **alle 90 Sekunden** eine Blutkonserve gebraucht. Spenden darf man ab 18 Jahren."]),
              ("film", "Filmtipp aus dem Schulbuch: Blutgruppen (Rotes Kreuz)", "https://www.trauner.at/nawi_v121.aspx", "Video aus dem Schulbuch (Buch S. 84) · öffnet in einem neuen Tab"),
              ("reveal", I.STOPPFRAGEN["blutgruppen"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 8 g) bis k)", "aufgaben.html#card_a7")]),

 ("muskeln", "Teil 9 · Buch S. 110–111 · Stunde 5", "Muskeln", [
  {"id": "muskeln", "title": "Ziehen, nie drücken", "pill": "Buch S. 110–111",
   "blocks": [("buch", "Lies im **Buch S. 111** die Abschnitte **»1.2.2 Zusammenspiel der Muskeln«** und **»1.2.3 Energieversorgung«**."),
              kartenblock("k9"),
              ("ul", ["**Mitmachen:** Leg die linke Hand auf den rechten Oberarm. Beuge den rechten Arm – vorne wird der **Bizeps** hart und dick. Streck ihn – jetzt spannt hinten der **Trizeps**.",
                      "**Bau:** Muskel → Faserbündel → **Muskelfasern** (bis zu 30 cm lang, viele Zellkerne) → **Myofibrillen** aus **Actin** und **Myosin** (Hölzel S. 107). Eine Faser zieht sich ganz oder gar nicht zusammen; die Kraft regelt der Körper vor allem über die **Zahl** der Fasern, die gleichzeitig arbeiten, und wie oft sie gereizt werden.",
                      "**Energie:** ATP stammt vor allem aus der **Zellatmung** – dafür braucht der Muskel Sauerstoff aus dem Blut. Hier schließt sich der Kreis zu Herz und Blut.",
                      "**Muskelfasertypen** (Hölzel S. 108): Typ I langsam und ausdauernd (Marathon), Typ IIa dazwischen (400–800 m), Typ IIx schnell und sehr kräftig, aber rasch müde (Gewichtheben). Training formt die Fasern."]),
              ("film", "Filmtipp aus dem Schulbuch: Beuger und Strecker", "https://www.trauner.at/nawi_v124.aspx", "Video aus dem Schulbuch (Buch S. 111) · öffnet in einem neuen Tab"),
              ("reveal", I.STOPPFRAGEN["muskeln"])]}]),

 ("ergonomie", "Teil 10 · Buch S. 112–113 · Stunde 5", "Ergonomie", [
  {"id": "ergonomie", "title": "Sitzen, heben, tragen – ohne Rückenschmerzen", "pill": "Buch S. 112–113",
   "blocks": [("buch", "Schau dir im **Buch S. 113** die Tabelle **»So sitzt man richtig!«** an."),
              kartenblock("k10"),
              ("sim", "hebel"),
              ("demo", "K3.6-D2", "Ein Freiwilliger hält einen Rucksack mit Gewichten erst eng am Körper, dann mit ausgestreckten Armen weit vorne. **Erst vermuten:** Wo spürt er es im Rücken stärker? "
                                  "Danach zeigt Prof. HOLZER richtiges und falsches Heben (nur mit leichter Last)."),
              ("table", [["Prüfpunkt", "So ist es gut (AUVA, Buch S. 113)"],
                         ["Füße und Knie", "Füße flach am Boden, Knie etwa im rechten Winkel"], ["Arme", "Unterarme liegen locker auf, Ellbogen etwa im rechten Winkel"],
                         ["Rücken", "Rückenlehne nutzen, nicht auf der Stuhlkante, dynamisch sitzen"], ["Bildschirm", "oberste Zeile höchstens auf Augenhöhe, 50–70 cm Abstand (etwa eine Armlänge)"],
                         ["Licht", "hell genug, keine Spiegelung (Fenster seitlich)"], ["Bewegung", "regelmäßig aufstehen – z. B. beim Telefonieren"]]),
              ("ul", ["**Humane Ziele** der Ergonomie: weniger Belastung, weniger Unfälle, mehr Freude an der Arbeit. **Wirtschaftliche Ziele:** bessere Leistung, weniger Krankenstände – das spart dem Betrieb Geld.",
                      "**Hebel:** Die Rückenmuskeln greifen nur wenige Zentimeter hinter der Wirbelsäule an. Eine Last weit vorne wirkt über einen langen Hebel. Darum muss der Rücken ein Vielfaches der Last ziehen – und die Bandscheiben werden zusammengedrückt.",
                      "**Rucksack und Marsch:** schwere Dinge nah an den Rücken, Hüftgurt nutzen, Riemen so einstellen, dass der Rucksack nicht nach hinten zieht."]),
              ("reveal", I.STOPPFRAGEN["ergonomie"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgaben 10 und 11", "aufgaben.html#card_a9")]),
]

SCHNELLE = [
 {"id": "schnell1", "title": "EKG und Defibrillator", "pill": "OPTIONAL · Buch S. 78",
  "blocks": [("ul", ["Ein **EKG** (Elektrokardiogramm) zeichnet die elektrische Erregung des Herzens auf. Die große Zacke zeigt die Erregung der Kammern, die kleinen Wellen davor und danach Vorhöfe und Rückbildung.",
                     "Beim **Kammerflimmern** zucken die Muskelzellen chaotisch – das Herz pumpt nicht mehr. Ein **Defibrillator** unterbricht das Chaos mit einem Stromstoß, damit der eigene Takt wieder übernehmen kann.",
                     "Bei einer **Nulllinie** (kein Signal) hilft ein Schock nicht. In Serien wird das oft falsch gezeigt (Zusatzaufgabe 12).",
                     "**Erste Hilfe:** Notruf 144, Herzdruckmassage, Defi holen lassen – der automatische Defi analysiert selbst und sagt an, was zu tun ist."])]},
 {"id": "schnell2", "title": "Druck bis in die Füße", "pill": "OPTIONAL · Hölzel S. 96",
  "blocks": [("ul", ["Eine Flüssigkeitssäule drückt mit p = ρ · g · h. Für 1,25 m Blut sind das rund 12 000 Pa (etwa 92 mmHg). Darum sammelt sich Blut in den Beinen, wenn die Muskelpumpe fehlt.",
                     "Bei Herzschwäche schafft das Herz den Rücktransport nicht gut – Flüssigkeit tritt ins Gewebe aus, Knöchel schwellen an (Ödeme)."])]},
 {"id": "schnell3", "title": "Peptide, Looksmaxing und der Blick auf die Quelle", "pill": "OPTIONAL",
  "blocks": [("ul", ["Im Netz werden »Peptide« wie **BPC-157** als Heilwunder für Sehnen verkauft. BPC-157 ist **nirgends als Arzneimittel zugelassen**, wurde fast nur an Tieren untersucht und steht auf der **Dopingliste** der WADA (USADA, Sport Integrity Australia).",
                     "Frag bei solchen Trends immer: Wer behauptet es? Gibt es Studien am Menschen? Wer verdient daran – mit Produkten, Coachings oder Klicks?",
                     "Zusatzaufgabe 14 prüft genau das mit einer KI-Antwort."]),
             ("hint", "Zusatzaufgaben und Zusatztexte zählen nicht zum Pflichtfortschritt und sind keine Hausübung.")]},
]
