"""Theorie-Seite K2.1 Mechanische Kräfte: Theorie-Karten, Teile und Folien.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufen im Arbeitsblatt (Tipp 2 = Theorie-Karte) und die Lesestopps der Unterrichts-PPP.
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), versuch (ID, Titel, Text), karten, buch, gemeinsam.
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt.
Neue Standards 07.11.2026: »Aufgabe zuerst« – die Theorie-Seite ist das Nachschlagewerk, die Karten stehen bei der Aufgabe."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "wirkung": "1 Kraft", "bewegung": "2 Bewegung", "gewicht": "3 Gewicht", "auftrieb": "4 Auftrieb",
          "reibung": "5 Reibung", "kapillar": "6 Kapillar", "druck": "7 Druck", "gegenkraft": "8 Gegenkraft",
          "projekt": "Projekt", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

# ================================================================ Theorie-Karten (höchstens drei Sätze, ein großes Bild, Formelzeichen mit Einheit)
KARTEN = {
 "k0": {"titel": "So läuft euer Gruppenprojekt", "teil": "projekt", "buch": "Buch S. 45–61", "bild": "img/projekt.png",
        "alt": "Ablauf in fünf Schritten: Frage und Vermutung, Plan und Quellen, Messen, Erklären mit Grenze, Präsentieren in drei Minuten.",
        "satz": ["Formuliert eine **prüfbare Frage** und eine Vermutung mit »weil …«.",
                 "Ändert genau **eine Bedingung**; alles andere bleibt gleich.",
                 "Trennt in der Auswertung **Beobachtung** (was ihr gemessen habt) und **Erklärung** (warum es so ist)."],
        "formeln": [], "link": "theorie.html#projekt"},
 "k1": {"titel": "Was eine Kraft bewirkt", "teil": "wirkung", "buch": "Buch S. 45, 49, 61", "bild": "img/wirkung.png",
        "alt": "Derselbe Wagen in drei Situationen: beim Anfahren wird er schneller, in der Kurve ändert sich die Richtung, zwischen zwei Händen wird ein Ball verformt. Kraftpfeile rot, Geschwindigkeitspfeile blau.",
        "satz": ["Eine **Kraft** kann das Tempo oder die Richtung einer Bewegung ändern oder einen Körper **verformen**.",
                 "Kräfte haben eine **Richtung** und werden mit Pfeilen gezeichnet.",
                 "Für die Bewegungsänderung zählt die **resultierende Kraft**, also die gemeinsame Wirkung aller Kräfte auf einen Körper."],
        "formeln": [("F_res", "resultierende Kraft", "N"), ("m", "Masse", "kg"), ("a", "Beschleunigung", "m/s²"),
                    ("F_res = m · a", "1 N = 1 kg · m/s²", "")],
        "link": "theorie.html#wirkung"},
 "k2": {"titel": "Geschwindigkeit und Beschleunigung", "teil": "bewegung", "buch": "Buch S. 46–48", "bild": "img/bewegung.png",
        "alt": "Drei Bildreihen mit gleichen Zeitabständen: gleich große Abstände bei konstantem Tempo, größer werdende Abstände beim Schnellerwerden, gleiche Abstände auf einer Kurve mit sich drehendem Geschwindigkeitspfeil.",
        "satz": ["Die mittlere Schnelligkeit auf gerader Strecke berechnest du mit **v = s / t**.",
                 "Zur Geschwindigkeit gehört auch die **Richtung**.",
                 "**Beschleunigung** heißt: Tempo oder Richtung ändern sich – auch Bremsen und Kurvenfahren gehören dazu."],
        "formeln": [("v", "Schnelligkeit", "m/s"), ("s", "Weg", "m"), ("t", "Zeit", "s"),
                    ("v = s / t", "von m/s auf km/h: mal 3,6", ""), ("a = (v_ende − v_anfang) / Δt", "mittlere Beschleunigung", "m/s²")],
        "link": "theorie.html#bewegung"},
 "k3": {"titel": "Masse und Gewichtskraft", "teil": "gewicht", "buch": "Buch S. 50–51", "bild": "img/gewicht.png",
        "alt": "Derselbe Rucksack auf Erde und Mond: gleiche Masse 6 kg, auf der Erde ein langer Kraftpfeil mit 60 N, am Mond ein kurzer mit etwa 10 N.",
        "satz": ["Die **Masse m** wird in Kilogramm angegeben, die **Gewichtskraft F_G** in Newton.",
                 "Es gilt **F_G = m · g**; g ist der Ortsfaktor in N/kg.",
                 "In dieser Einheit rechnen wir immer mit **g = 10 N/kg** – genauer wären 9,81 N/kg."],
        "formeln": [("F_G", "Gewichtskraft", "N"), ("m", "Masse", "kg"), ("g", "Ortsfaktor", "N/kg"),
                    ("F_G = m · g", "hier mit g = 10 N/kg", "")],
        "link": "theorie.html#gewicht"},
 "k4": {"titel": "Auftrieb: sinken, steigen und schwimmen", "teil": "auftrieb", "buch": "Buch S. 52–53", "bild": "img/auftrieb.png",
        "alt": "Drei Körper im Wasser: vollständig eingetaucht und steigend mit langem Auftriebspfeil, schwebend mit gleich langen Pfeilen, ruhig an der Oberfläche schwimmend mit gleich langen Pfeilen.",
        "satz": ["In Wasser und Luft wirkt eine **Auftriebskraft** nach oben.",
                 "Sie ist so groß wie die **Gewichtskraft des verdrängten** Wassers oder der verdrängten Luft.",
                 "Schwimmt ein Körper ruhig an der Oberfläche, sind **Auftriebskraft und Gewichtskraft gleich groß**."],
        "formeln": [("F_A", "Auftriebskraft", "N"), ("ρ", "Dichte des Fluids", "kg/m³"), ("V", "verdrängtes Volumen", "m³"),
                    ("F_A = ρ · g · V", "nur zur Erweiterung", "")],
        "link": "theorie.html#auftrieb"},
 "k5": {"titel": "Reibung hilft und bremst", "teil": "reibung", "buch": "Buch S. 54–56", "bild": "img/reibung.png",
        "alt": "Links ein Becher auf dem Tisch mit Zugkraft nach rechts, Gleitreibung nach links, Normalkraft nach oben und Gewichtskraft nach unten. Rechts ein Fuß, der den Boden nach hinten drückt, und der Boden, der den Fuß nach vorne drückt.",
        "satz": ["**Gleitreibung** wirkt gegen das Gleiten zweier berührender Oberflächen.",
                 "**Haftreibung** verhindert Rutschen – dadurch kann sie beim Gehen sogar **antreiben**.",
                 "Reibung kann erwünscht sein (Schuhsohle) oder unerwünscht (Lager)."],
        "formeln": [("F_R", "Gleitreibungskraft", "N"), ("F_N", "Normalkraft", "N"), ("μ", "Reibungszahl", "ohne Einheit"),
                    ("F_R = μ · F_N", "einfaches Näherungsmodell", "")],
        "link": "theorie.html#reibung"},
 "k6": {"titel": "Kapillarwirkung und Oberflächenspannung", "teil": "kapillar", "buch": "Buch S. 57", "bild": "img/kapillar.png",
        "alt": "Links ein Filterpapierstreifen, dessen unterer Rand im Wasser steht und dessen feuchte Grenze über dem äußeren Wasserspiegel liegt. Rechts ein enges benetzbares Röhrchen mit angehobenem Wasserstand und Wasserteilchen, die zusammenhalten.",
        "satz": ["**Adhäsion** ist die Anziehung zwischen verschiedenen Stoffen, **Kohäsion** der Zusammenhalt innerhalb eines Stoffes.",
                 "In feinen benetzbaren Zwischenräumen kann Wasser durch **Kapillarwirkung** steigen.",
                 "Das sieht man auch bei saugfähigem Papier; für hohe Pflanzen braucht es zusätzlich den **Transpirationssog**."],
        "formeln": [], "link": "theorie.html#kapillar"},
 "k7": {"titel": "Druck: Kraft auf eine Fläche", "teil": "druck", "buch": "Buch S. 58–60", "bild": "img/druck.png",
        "alt": "Oben dieselbe Gewichtskraft auf einem schmalen Stiefel und auf einem breiten Schneeschuh, der Druckpfeil unter dem Schneeschuh ist deutlich kleiner. Unten eine Spritze ohne Nadel, einmal offen, einmal mit dem Finger verschlossen und zusammengedrückter Luft.",
        "satz": ["**Druck p** beschreibt, wie sich eine senkrecht wirkende Kraft auf eine Fläche verteilt.",
                 "Es gilt **p = F_N / A**; der Druck wird in Pascal angegeben.",
                 "Bei gleicher Kraft bedeutet eine **größere Fläche einen kleineren Druck**."],
        "formeln": [("p", "Druck", "Pa"), ("F_N", "senkrechte Kraft", "N"), ("A", "Fläche", "m²"),
                    ("p = F_N / A", "1 Pa = 1 N/m², 1 bar = 100 000 Pa", "")],
        "link": "theorie.html#druck"},
 "k8": {"titel": "Kraft und Gegenkraft", "teil": "gegenkraft", "buch": "Buch S. 61", "bild": "img/gegenkraft.png",
        "alt": "Links zwei ineinander gehängte Kraftmesser, beide zeigen 2 N; um jedes Gerät ist ein eigener farbiger Rahmen gezeichnet. Rechts ein Buch auf dem Tisch mit Gewichtskraft nach unten und Stützkraft nach oben, beide am selben Buch.",
        "satz": ["Übt Körper A eine Kraft auf Körper B aus, wirkt gleichzeitig eine gleich große, entgegengesetzte Kraft von B auf A.",
                 "Diese beiden Kräfte wirken auf **verschiedene Körper**.",
                 "Beim **Kräftegleichgewicht** gleichen sich dagegen Kräfte an **demselben** Körper aus."],
        "formeln": [], "link": "theorie.html#gegenkraft"},
 "k9": {"titel": "Alle Größen und Einheiten auf einmal", "teil": "kurz", "buch": "Buch S. 45–61, Anhang S. 232", "bild": "img/einheiten.png",
        "alt": "Übersichtstafel: Masse in kg, Kraft in N, Geschwindigkeit in m/s, Beschleunigung in m/s², Druck in Pa, jeweils mit Formel.",
        "satz": ["**Masse** in kg, **Kraft** in N, **Geschwindigkeit** in m/s, **Beschleunigung** in m/s², **Druck** in Pa.",
                 "Die vier Formeln dieser Einheit: **v = s / t · F = m · a · F_G = m · g · p = F / A**.",
                 "Geschwindigkeit, Beschleunigung und Druck sind **keine Kraftarten**."],
        "formeln": [("v = s / t", "Schnelligkeit", "m/s"), ("F = m · a", "resultierende Kraft", "N"),
                    ("F_G = m · g", "Gewichtskraft mit g = 10 N/kg", "N"), ("p = F / A", "Druck", "Pa")],
        "link": "theorie.html#kurz"},
}
for _k, _v in KARTEN.items():
    assert len(_v["satz"]) <= 3, (_k, "mehr als drei Sätze")
AUFGABE_KARTE = {t["id"]: t["tipps"][1] for t in I.T if t.get("tipps")}
for _id, _k in AUFGABE_KARTE.items():
    assert _k in KARTEN, (_id, _k)


def karte_html_daten():
    """Karten als reine Daten für das Arbeitsblatt (Tipp 2)."""
    return {k: {"titel": v["titel"], "satz": v["satz"], "bild": v["bild"], "alt": v["alt"],
                "formeln": v["formeln"], "link": v["link"], "buch": v["buch"]} for k, v in KARTEN.items()}


def kartenblock(key):
    """Dieselbe Karte als Block für die Theorie-Seite."""
    v = KARTEN[key]
    return ("karte", v)


# ================================================================ Einstieg
EINSTIEG = [
 {"id": "s0a", "title": "Warum du Kräfte brauchst", "pill": "Buch S. 44",
  "blocks": [("img", "img/wirkung.png", KARTEN["k1"]["alt"], "Eine Kraft ändert Tempo oder Richtung einer Bewegung – oder sie verformt einen Körper."),
             ("ul", ["**Das Wichtigste vorab:** Kräfte ändern Bewegungen oder Formen. Nicht jeder bewegte Körper hat eine resultierende Kraft.",
                     "**Wozu?** Anfahren, Bremsen und Kurvenfahren musst du bei jedem Fahrzeug verstehen. Beim Marsch entscheidet die Gewichtskraft deiner Ausrüstung, "
                     "beim Sport die Haftreibung deiner Schuhe, beim Schwimmen der Auftrieb, beim Stapfen im Schnee der Druck unter der Sohle.",
                     "**Das kannst du nachher:** zu jedem dieser sieben Themen in einem Satz sagen, was gemessen wird und in welcher Einheit."]),
             ("hint", "Diese Einheit ist ein Projekt: Sieben Gruppen untersuchen je ein Thema und erklären es den anderen. Du brauchst also auch die Themen der anderen Gruppen.")]},
 {"id": "s0b", "title": "Mythos-Check: »Wo etwas fährt, zieht eine Kraft«", "pill": "Buch S. 45",
  "blocks": [("tiles", [("Was viele meinen", ["Wenn sich etwas bewegt, muss ständig eine Kraft wirken. Bleibt die Kraft weg, bleibt der Körper sofort stehen."]),
                        ("Was wirklich gilt", ["Für eine **gleichbleibende** Geschwindigkeit auf gerader Bahn braucht es **keine resultierende** Kraft. "
                                               "Mehrere Kräfte können sich ausgleichen – zum Beispiel Antrieb und Reibung bei konstanter Fahrt."])]),
             ("hint", "Umgekehrt gibt es Kräfte ohne sichtbare Bewegung: Eine belastete Feder bleibt gedehnt, ein Buch drückt auf den Tisch.")]},
 {"id": "s0c", "title": "Science oder Fiction?", "pill": "Buch S. 61",
  "blocks": [("ul", ["In vielen Weltraumfilmen zünden Raumschiffe ihre Triebwerke, um im leeren Raum »vorwärts zu drücken« – als bräuchten sie Luft, von der sie sich abstoßen.",
                     "**Richtig ist:** Eine Rakete stößt Masse nach hinten aus und wird dadurch nach vorne beeinflusst. Das funktioniert **ohne** Luft. "
                     "Umgekehrt dreht in Wirklichkeit kein Raumschiff nach dem Abschalten des Antriebs eine enge Kurve und bleibt dann stehen.",
                     "**Offene Forschungsfrage:** Wie viel Reibung zwischen zwei Oberflächen tatsächlich entsteht, lässt sich noch nicht aus der Rauigkeit allein berechnen. "
                     "Zusatzaufgabe 7 zeigt eine aktuelle Arbeit der TU Wien dazu."]),
             ("merke", "Film nur in Worten besprechen – keine Filmbilder, Figuren oder Logos auf dieser Seite (Urheberrecht).")]},
]

# ================================================================ Teile 1–8
PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("wirkung", "Teil 1 · Buch S. 45, 49, 61", "Was eine Kraft bewirkt", [
  {"id": "wirkung", "title": "Kraft, Kraftpfeil und resultierende Kraft", "pill": "Buch S. 45",
   "blocks": [("buch", "Lies zuerst im **Buch S. 45** den Abschnitt **»Der Begriff Kraft«** (2 min) und markiere die drei Kraftwirkungen."),
              kartenblock("k1"),
              ("ul", ["Eine Bewegung allein beweist noch keine resultierende Kraft. Ein Körper kann sich gerade und mit gleichbleibender Geschwindigkeit bewegen, obwohl sich mehrere Kräfte ausgleichen.",
                      "Eine Kraft ist auch **ohne** sichtbare Bewegung möglich: Eine belastete Feder bleibt gedehnt.",
                      "Ein **Kraftpfeil** zeigt drei Dinge: den Angriffspunkt, die Richtung und den Betrag. Der Betrag steckt in der **Pfeillänge** – dazu muss der Maßstab dabeistehen.",
                      "Kräfte **verschiedener** Körper werden nicht in einem Kräftebild vermischt. Zeichne zuerst einen Rahmen um den Körper, den du betrachtest."]),
              ("merke", "Bei gleichbleibender Masse gilt F_res = m · a. 1 N = 1 kg · m/s². Nur die resultierende Kraft ändert die Bewegung."),
              ("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgaben 1 und 2", "aufgaben.html#name")]),

 ("bewegung", "Teil 2 · Buch S. 46–48", "Geschwindigkeit und Beschleunigung", [
  {"id": "bewegung", "title": "Tempo, Richtung und Änderung", "pill": "Buch S. 46–48",
   "blocks": [("buch", "Lies im **Buch S. 46–47** den Abschnitt **»Die Geschwindigkeit«** und markiere die Formel."),
              kartenblock("k2"),
              ("ul", ["Auf gerader Strecke ohne Umkehr liefert v = s / t den Betrag der **mittleren** Geschwindigkeit. Wie das Tempo unterwegs verlief, sagt dieser Wert nicht.",
                      "Für **km/h** multiplizierst du einen Wert in m/s mit 3,6; in die Gegenrichtung teilst du durch 3,6.",
                      "Bilder in **gleichen Zeitabständen** helfen beim Vergleichen: größere Abstände bedeuten größeres Tempo, gleich große Abstände auf gerader Bahn bedeuten gleichförmige Bewegung.",
                      "In einer Kurve ändert sich die Geschwindigkeit auch bei gleichem Tempo – weil sich die **Richtung** ändert."]),
              ("table", [["Größe", "Zeichen", "Einheit", "Beispiel"],
                         ["Weg", "s", "m", "5 m"],
                         ["Zeit", "t", "s", "4 s"],
                         ["Schnelligkeit", "v", "m/s", "1,25 m/s = 4,5 km/h"],
                         ["Beschleunigung", "a", "m/s²", "2 m/s²: jede Sekunde 2 m/s mehr"]]),
              ("hint", "Lange Beschleunigungsrechnungen und das Addieren von Pfeilen sind in dieser Einheit Zusatzstoff."),
              ("reveal", I.STOPPFRAGEN[1][1:])]}]),

 ("gewicht", "Teil 3 · Buch S. 50–51", "Masse und Gewichtskraft", [
  {"id": "gewicht", "title": "kg oder N?", "pill": "Buch S. 50–51",
   "blocks": [("buch", "Lies im **Buch S. 50** den Abschnitt **»Die Gewichtskraft«** und sieh dir die Abbildung des Federkraftmessers an."),
              kartenblock("k3"),
              ("ul", ["Ein Rucksack mit 6 kg Masse hat mit g = 10 N/kg eine Gewichtskraft von **60 N**.",
                      "Am Mond bleibt seine **Masse** 6 kg. Seine **Gewichtskraft** ist kleiner, weil der Ortsfaktor kleiner ist. Die Alltagsangabe »Gewicht 6 kg« meint fast immer die Masse.",
                      "Eine **Waage** zeigt üblicherweise eine Masse an. Ein **Federkraftmesser** zeigt eine Kraft in Newton.",
                      "Vor dem Messen prüfst du drei Dinge: **Nullpunkt, Messbereich und kleinste Teilung**. Eine Skala mit 0,2-N-Schritten erlaubt keine feineren Messwerte."]),
              ("merke", "g kann als Fallbeschleunigung in m/s² oder als Ortsfaktor in N/kg angegeben werden – beides ist gleichwertig. Wir wechseln die Näherung nicht mitten in einer Aufgabe."),
              ("reveal", I.STOPPFRAGEN[2])]}]),

 ("auftrieb", "Teil 4 · Buch S. 52–53", "Auftrieb: sinken, steigen und schwimmen", [
  {"id": "auftrieb", "title": "Warum ein Stahlschiff schwimmt", "pill": "Buch S. 52–53",
   "blocks": [("buch", "Lies im **Buch S. 52** den Abschnitt **»Auftrieb«**. Die Abbildung dort zeigt Schwimmen, Schweben und Sinken – vergleiche sie mit der Zeichnung hier."),
              kartenblock("k4"),
              ("ul", ["Der Flüssigkeitsdruck ist **unten** am eingetauchten Körper größer als oben. Daraus entsteht die Auftriebskraft.",
                      "Beim **ruhigen Schwimmen** gilt F_A = F_G. Ist bei einem zunächst ruhenden, ganz eingetauchten Körper die Auftriebskraft größer, wird er nach oben beschleunigt.",
                      "Ein Schiff verdrängt durch seine **Form** genug Wasser, um seine ganze Gewichtskraft auszugleichen. Entscheidend ist nicht die Dichte von Stahl, sondern die **mittlere Dichte des ganzen Schiffes** samt Hohlraum.",
                      "Auch ein **sinkender** Körper erfährt Auftrieb. Seine Gewichtskraft ist nur größer."]),
              ("hint", "Achtung beim Buchbild auf S. 53: Dass man im Toten Meer nicht untergehen könne, stimmt so nicht. Die hohe Dichte erleichtert das Schwimmen – eine Sicherheitsgarantie ist das nicht."),
              ("reveal", I.STOPPFRAGEN[3])]}]),

 ("reibung", "Teil 5 · Buch S. 54–56", "Reibung hilft und bremst", [
  {"id": "reibung", "title": "Haften, gleiten, antreiben", "pill": "Buch S. 54–56",
   "blocks": [("buch", "Lies im **Buch S. 54–55** die Abschnitte zu **Haft-, Gleit- und Rollreibung**."),
              kartenblock("k5"),
              ("ul", ["Ziehst du einen ruhenden Gegenstand **langsam** an, steigt die Haftreibung mit deiner Zugkraft mit. Sie hat einen **Höchstwert**.",
                      "Erst **nach** dem Losgleiten misst du bei möglichst gleichförmigem Ziehen die **Gleitreibungskraft**.",
                      "Die **maximale** Haftreibung ist bei vielen Materialpaaren größer als die Gleitreibung. Eine kleine aktuelle Haftkraft ist aber nicht automatisch größer als jede Gleitkraft.",
                      "Reibung hängt von **Material, Oberflächenzustand und Normalkraft** ab. Auf waagrechter Unterlage ohne weitere senkrechte Kraft ist die Normalkraft betragsmäßig gleich der Gewichtskraft.",
                      "Reibung entsteht nicht nur durch sichtbare Rauigkeit, sondern auch durch Wechselwirkungen und Verformungen an den Kontaktstellen."]),
              ("merke", "Reibung wirkt gegen das relative Gleiten an der Kontaktstelle – nicht automatisch gegen die Bewegung über den Boden. Beim Gehen drückt der Boden deinen Fuß nach vorne."),
              ("reveal", I.STOPPFRAGEN[4])]}]),

 ("kapillar", "Teil 6 · Buch S. 57", "Kapillarwirkung und Oberflächenspannung", [
  {"id": "kapillar", "title": "Wie Wasser nach oben kommt", "pill": "Buch S. 57",
   "blocks": [("buch", "Lies im **Buch S. 57** den Abschnitt **»Die Kapillarkraft«** mit Adhäsion und Kohäsion."),
              kartenblock("k6"),
              ("ul", ["Papier besteht aus einem **Netz von Fasern** mit kleinen Zwischenräumen. Wasser benetzt die Fasern und breitet sich darin aus.",
                      "Steigt ein feuchter Rand **über** die äußere Wasseroberfläche, ohne dass jemand nachgießt, zeigt das Kapillarwirkung im porösen Material. Ein schmalerer Streifen hat aber nicht automatisch engere Poren.",
                      "Die **Oberflächenspannung** beschreibt die Tendenz einer Flüssigkeitsoberfläche, ihre Fläche zu verkleinern. Eine vorsichtig aufgelegte Büroklammer kann dadurch oben bleiben, obwohl Metall dichter als Wasser ist – das ist etwas anderes als ein Schiff, das durch Auftrieb getragen wird.",
                      "Bei Pflanzen wirken Wasserpotentialunterschiede, Kohäsion und Verdunstung an den Blättern zusammen. Kapillarwirkung allein erklärt den Transport in einen hohen Baum **nicht**."]),
              ("hint", "Der »Spülmittelfisch« schwimmt wegen Unterschieden der Oberflächenspannung los, nicht wegen Rückstoß. Als Nachweis des Raketenprinzips taugt er nicht."),
              ("reveal", [("Warum reicht Kapillarität für einen hohen Baum nicht?",
                           "Die Verdunstung an den Blättern erzeugt eine Zugspannung, und die Kohäsion überträgt sie im Holz nach unten. Die Steighöhe einer einzelnen Kapillare ist viel kleiner als ein Baum.")])]}]),

 ("druck", "Teil 7 · Buch S. 58–60", "Druck: Kraft auf eine Fläche", [
  {"id": "druck", "title": "Gleiche Kraft, andere Fläche", "pill": "Buch S. 58–60",
   "blocks": [("buch", "Lies im **Buch S. 58** den Abschnitt **»Druck«** mit dem Beispiel der Schneeschuhe."),
              kartenblock("k7"),
              ("ul", ["Schneeschuhe verteilen **dieselbe** Gewichtskraft auf eine größere Fläche. Der mittlere Druck wird kleiner, deshalb sinkt man weniger ein.",
                      "Druck ist **keine zusätzliche Kraftart**. Er verbindet eine Kraft mit der Fläche, auf die sie wirkt.",
                      "In Flüssigkeiten steigt der Überdruck mit der **Tiefe**: p_h = ρ · g · h. Zum absoluten Druck kommt noch der Luftdruck an der Oberfläche dazu.",
                      "Luft übt Druck in **alle** Richtungen aus. Drückst du eingeschlossene Luft vorsichtig zusammen, steigt ihr Druck und sie drückt stärker zurück."]),
              ("hint", "Achtung beim Buchversuch mit der Flasche und mehreren Löchern: Das tiefste Loch liefert nicht automatisch den weitesten Strahl. Die Reichweite hängt auch von der Fallhöhe ab."),
              ("reveal", I.STOPPFRAGEN[5])]}]),

 ("gegenkraft", "Teil 8 · Buch S. 61", "Kraft und Gegenkraft", [
  {"id": "gegenkraft", "title": "Zwei Körper oder ein Körper?", "pill": "Buch S. 61",
   "blocks": [("buch", "Lies im **Buch S. 61** den Abschnitt **»Kraft und Gegenkraft«**."),
              kartenblock("k8"),
              ("ul", ["Beim Abstoßen drückt dein **Fuß den Boden nach hinten**, während der **Boden deinen Fuß nach vorne** drückt. Zwei Kräfte, zwei verschiedene Körper.",
                      "Beim **Rückstoß** stößt ein Körper Masse in eine Richtung aus und wird in die andere Richtung beeinflusst. Raketen brauchen dafür keine Luft.",
                      "Zwei ineinander gehängte Federkraftmesser zeigen bei ruhigem Ziehen in einer Linie annähernd **denselben Betrag**. Aus zwei Anzeigen von 2 N werden nicht 4 N.",
                      "Ein Buch auf dem Tisch ist im **Gleichgewicht**: Gewichtskraft und Stützkraft sind gleich groß und entgegengesetzt – beide am **Buch**. Die Gegenkraft zur Gewichtskraft auf das Buch ist die Anziehung des Buches auf die Erde."]),
              ("merke", "Wechselwirkungspaar: zwei Körper, zwei Kräfte. Kräftegleichgewicht: ein Körper, mehrere Kräfte, Summe null."),
              ("reveal", I.STOPPFRAGEN[6])]},
  ("jetzt", "Jetzt: Aufgabe 4", "aufgaben.html#card_a3")]),

 ("projekt", "Stunden 2–5", "Euer Gruppenprojekt", [
  {"id": "projekt", "title": "Sieben Gruppen, sieben Themen", "pill": "Buch S. 45–61",
   "blocks": [kartenblock("k0"),
              ("gemeinsam", "Die Themenverteilung, die Rollen und die Freigabe eures Versuchsplans macht Prof. HOLZER mit euch gemeinsam in der Stunde."),
              ("table", [["Gruppe", "Thema", "Buch", "Was ihr messt oder beobachtet"],
                         ["1", "Bewegung messen", "S. 46–48", "Weg und Zeit auf 5 m, daraus v in m/s und km/h"],
                         ["2", "Gewichtskraft messen", "S. 49–51", "Masse in g und die Kraft am Kraftmesser in N"],
                         ["3", "Auftrieb über eine Waage", "S. 52–53", "zusätzliche Waagenanzeige bei verschiedenen Eintauchtiefen"],
                         ["4", "Haft- und Gleitreibung", "S. 54–56", "Zugkraft kurz vor dem Losgleiten und beim gleichförmigen Ziehen"],
                         ["5", "Kapillarwirkung in Filterpapier", "S. 57", "Lage der feuchten Grenze nach 10, 30 und 60 s"],
                         ["6", "Luftdruck in einer Spritze", "S. 58–60", "Volumen und spürbarer Widerstand, offen gegen geschlossen"],
                         ["7", "Kraft und Gegenkraft", "S. 45, 61", "beide Anzeigen bei ungefähr 1, 2 und 3 N"]]),
              ("ul", ["**Rollen:** Leitung und Zeit · Quellenprüfung · Aufbau und Messung · Protokoll. In der Fünfergruppe übernimmt ein Kadett zusätzlich Material und Gegenprobe.",
                      "**Quellen prüfen:** Wer schreibt? Gibt es ein Datum? Was ist die Kernaussage? Warum passt die Quelle? Zwei Berichte derselben Organisation sind **nicht** automatisch unabhängig.",
                      "**Echte Werte:** Schreibt nur auf, was ihr gemessen habt. Erwartete Zahlen sind keine Messwerte. Trennt Beobachtung und Erklärung.",
                      "**Präsentation:** höchstens **drei Minuten** einschließlich Versuch. Jeder erklärt einen kurzen Teil. Eine PowerPoint ist nicht nötig – drei Abschnitte im Gruppen-PDF genügen."]),
              ("versuch", I.VS_ID, I.VS_TITEL, "Auf der Versuchsseite findest du den Auftrag deiner Gruppe: Material, Durchführung, Sicherheit und alle Eingabefelder für das Gruppen-PDF.")]}]),
]

# ================================================================ Für Schnelle und Neugierige
SCHNELLE = [
 {"id": "schnell1", "title": "Mehr zum Rechnen", "pill": "OPTIONAL · Buch S. 58, 63",
  "blocks": [("ul", ["**Zusatzaufgabe 6** rechnet denselben Druck für zwei Flächen. Probier danach deine eigene Auflagefläche: Stell dich auf Millimeterpapier, zeichne eine Sohle nach und schätze die Fläche in m².",
                     "Für Kombattanten interessant: Ein Rucksack mit 20 kg Masse hat 200 N Gewichtskraft. Verteilt auf zwei Schultergurte mit je 0,006 m² ergibt das etwa 16 700 Pa – deshalb sind breite Gurte angenehmer.",
                     "**Vorsicht bei Beispielen aus dem Netz:** Für eine Druckrechnung muss die ganze tatsächlich belastete Kontaktfläche angegeben sein. Fehlt sie, ist das Ergebnis nicht belastbar."]),
             ("hint", "Diese Zahlen sind Modellwerte zum Üben, keine Messwerte.")]},
 {"id": "schnell2", "title": "Forschung und Technik", "pill": "OPTIONAL",
  "blocks": [("ul", ["**Zusatzaufgabe 7** führt zu einer Pressemitteilung der TU Wien über ein pulverförmiges Schmiermittel. Übe daran Quellenkritik: Wer berichtet, und wer hat die Forschung gemacht?",
                     "**Offene Frage der Forschung:** Reibung lässt sich noch nicht allein aus der Rauigkeit zweier Oberflächen berechnen. Genau daran arbeiten Tribologen.",
                     "**Pro und Contra zum Diskutieren:** Soll ein neues Schmiermittel in Fahrzeugen des Bundesheeres eingesetzt werden, solange es nur unter Laborbedingungen geprüft ist? Sammelt je zwei Argumente."]),
             ("hint", "Zusatzaufgaben zählen nicht zum Pflichtfortschritt und sind keine Hausübung.")]},
 {"id": "schnell3", "title": "Was in dieser Einheit NICHT dran war", "pill": "OPTIONAL",
  "blocks": [("ul", ["**Hooke'sches Gesetz** (Feder und Dehnung), **Vektoraddition** von Kräften und ausführliche **Beschleunigungsrechnungen** gehören in dieser Einheit nicht zum Pflichtstoff.",
                     "**Arbeit und Energie** (Buch S. 66–77) und **elektrische Kräfte** (ab S. 78) kommen als eigene Einheiten.",
                     "Wenn dich die Feder interessiert: Hänge verschiedene Massen an einen Kraftmesser und trage Kraft gegen Dehnung in ein Diagramm ein. Du wirst einen fast geraden Verlauf finden."]),
             ("hint", "Nicht testrelevant – das steht später auch so auf dem Teststoff.")]},
]
