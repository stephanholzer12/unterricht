"""Theorie PBGW 3BK · K1.3–1.4 Epochen – eine Quelle für Theorie-Seite (theorie.html) und PPP (Lehrer/Kadetten).
Bausteine: ("zeitstrahl",) · ("tiles", [(Überschrift, Text), …]) · ("ul", [...]) · ("ol", [...]) · ("merke", Text) · ("hint", Text)
           ("table", [[Kopf…], [Zeile…], …], [Spaltenbreiten-Anteile]) · ("video", key) · ("reveal", [(Frage, Antwort), …]) · ("jetzt", Text, Link)
**fett** wird in HTML und PPP fett gesetzt."""
from inhalt import LERNZIELE

S = lambda title, blocks, pill=None, sid=None: {"title": title, "blocks": blocks, "pill": pill, "id": sid}

ZEITSTRAHL = [("Ur- und Frühgeschichte", "bis ca. 3000 v. Chr.", 2.2, "A6B88A"), ("Altertum (Antike)", "ca. 3000 v. Chr. – 476", 2.1, "2E7D8C"),
              ("Mittelalter", "476 – ca. 1500", 1.9, "3B4A2F"), ("Neuzeit", "ca. 1500 – 1914/18", 1.8, "D9772B"), ("Zeit­geschichte", "ab 1914/18", 1.75, "8C3B2E")]
WENDE = [("um 3000 v. Chr.", "erste Schrift"), ("476", "Ende Westroms"), ("um 1500", "Buchdruck · Amerika · Reformation"), ("1914/18", "Erster Weltkrieg")]

PARTS = [
 ("einstieg", "Einstieg", "Worum geht es?", [
   S("Science oder Fiction? Die Zeitmaschine", [("tiles", [
       ("Zurück in die Zukunft", "Doc Brown tippt ein Zieldatum in seine Zeitmaschine. Du tippst **»10. Oktober 1582, Rom«** ein. Wo landest du? – Auflösung in Teil 1"),
       ("Mythos oder Fakt?", "»Im Mittelalter glaubten alle, die Erde sei eine Scheibe.« – Auflösung in Teil 2"),
       ("Ein Mönch verrechnet sich", "Um 525 legte der Mönch Dionysius fest: Wir zählen ab Christi Geburt. Doch Jesus kam wohl schon **zwischen 7 und 4 v. Chr.** zur Welt."),
       ("Offene Frage der Forschung", "Leben wir in einer neuen Erd-Epoche – dem **»Zeitalter des Menschen«**? Darüber streiten Forscher bis heute.")])], sid="zeitmaschine"),
   S("Das kannst du nach dieser Einheit", [("ol", LERNZIELE)])]),

 ("teil1", "Teil 1 · Stunde 1 · Buch S. 13", "Wie zählen wir Zeit?", [
   S("Warum brauchen wir einen Kalender?", [("tiles", [
       ("Überleben", "Aussaat und Ernte: Die Nilschwemme musste man genau vorhersagen."),
       ("Glaube", "Feste wie Ostern, Ramadan oder Jom Kippur brauchen ein Datum."),
       ("Wirtschaft", "Löhne, Mieten, Zinsen, Fristen – alles hängt am Datum."),
       ("Militär", "Wer ist wann wo? Im Einsatz zählt die genaue Zeit.")]),
     ("merke", "Schon vor rund **3600 Jahren** beobachteten Menschen den Himmel: Die **Himmelsscheibe von Nebra** zeigt Sonne, Mond und Sterne.")], "Buch S. 13"),
   S("Christi Geburt – und kein Jahr 0", [("ul", [
       "Seit dem 6. Jahrhundert zählt man im christlichen Europa ab **Christi Geburt**.",
       "Davor: **v. Chr.** (vor Christus) – danach: **n. Chr.** (nach Christus).",
       "Auf 1 v. Chr. folgt direkt 1 n. Chr. – **ein Jahr 0 gibt es nicht.**"]),
     ("merke", "**So rechnest du über die Zeitenwende:** beide Zahlen addieren, dann 1 abziehen. Caesars Tod 44 v. Chr. bis 2026: 44 + 2026 − 1 = **2069 Jahre**.")], "Buch S. 13", "jahr0"),
   S("Jahrhunderte richtig zählen", [("table", [["Jahr", "Jahrhundert", "So geht's"],
                                                ["1 bis 100", "1. Jh.", "das erste Jahrhundert"],
                                                ["1194", "12. Jh.", "Hunderterstelle 11 + 1"],
                                                ["1683", "17. Jh.", "16 + 1"],
                                                ["2001 bis 2100", "21. Jh.", "begann am 1. Jänner 2001"],
                                                ["500 bis 401 v. Chr.", "5. Jh. v. Chr.", "rückwärts gezählt"]], [3, 2, 4]),
     ("hint", "»Die 1500er-Jahre« sind das **16.** Jahrhundert.")], "Buch S. 13", "jh"),
   S("Julianisch → gregorianisch", [("tiles", [
       ("46 v. Chr. · Caesar", "**Julianischer Kalender:** alle 4 Jahre ein Schaltjahr = 365¼ Tage. Das ist 11 Minuten zu lang."),
       ("1582 · Papst Gregor XIII.", "Inzwischen 10 Tage zu viel. Auf Donnerstag, 4. Oktober folgte **Freitag, 15. Oktober 1582**."),
       ("Nicht alle machen mit", "Österreich stellt 1583/84 um, evangelische Länder Deutschlands 1700, **Russland erst 1918**, Griechenland 1923."),
       ("Bis heute", "Die »Oktoberrevolution« war für uns am **7. November 1917**. Manche orthodoxe Kirchen feiern Weihnachten am 7. Jänner.")])], "Buch S. 13", "gregor"),
   S("Die Schaltjahr-Regel: 4 – 100 – 400", [("ol", [
       "Durch **4** teilbar → Schaltjahr (2024, 2028)",
       "aber durch **100** teilbar → kein Schaltjahr (1900, 2100)",
       "aber durch **400** teilbar → doch ein Schaltjahr (1600, 2000)"]),
     ("merke", "Die Erde braucht für eine Runde um die Sonne ca. **365,24 Tage**. Der Schalttag am 29. Februar gleicht das aus."),
     ("video", "schalt")], "Buch S. 13", "schalt"),
   S("Andere Kalender", [("table", [["Kalender", "Jahr 1 beginnt mit …", "Besonderheit"],
                                    ["jüdisch", "Erschaffung der Welt (3761 v. Chr.)", "Mond und Sonne, Neujahr im Herbst"],
                                    ["islamisch", "Hidschra: Mohammed geht nach Medina (622)", "Mondjahr, ca. 354 Tage"],
                                    ["koptisch", "Kaiser Diokletian (284)", "Christen in Ägypten"],
                                    ["julianisch", "Christi Geburt", "heute 13 Tage hinter unserem"],
                                    ["gregorianisch", "Christi Geburt", "weltweit im Alltag"]], [2, 4, 3])], "Buch S. 13", "kalender"),
   S("Mondjahr und Sonnenjahr", [("tiles", [
       ("Sonnenjahr", "365,24 Tage – passt immer zu den Jahreszeiten (gregorianisch)."),
       ("Mondjahr", "12 Mondmonate = ca. **354 Tage**. Der Ramadan rückt jedes Jahr ca. 11 Tage nach vorne."),
       ("Faustformeln", "jüdisch ≈ unser Jahr **+ 3760** (ab Herbst + 3761) · islamisch ≈ (unser Jahr **− 622**) · 33 : 32"),
       ("Wirtschaft", "Saudi-Arabien zahlt Beamte seit 2016 nach dem Sonnenjahr – 11 Tage mehr Arbeit fürs gleiche Geld.")])], "Buch S. 13", "mond"),
   S("Zeitrechnungen nach Ereignissen", [("tiles", [
       ("Griechen · Sport", "Sie zählten in **Olympiaden**: 4-Jahres-Abschnitte ab den ersten Olympischen Spielen **776 v. Chr.**"),
       ("Römer", "»ab urbe condita« – seit der **Gründung Roms 753 v. Chr.** – und nach den beiden Konsuln des Jahres."),
       ("Französische Revolution", "Neuer Kalender ab 1792 = Jahr I. Am »18. Brumaire VIII« (9.11.1799) putschte sich **Napoleon** an die Macht."),
       ("Japan · Thailand", "Japan zählt nach Kaiser-Ären: 2026 = **Reiwa 8**. Thailand zählt ab Buddhas Tod: 2026 = **2569**.")])], "Buch S. 13", "ereignisse"),
   S("Zeit im Einsatz", [("tiles", [
       ("Datum-Zeit-Gruppe", "Meldungen tragen eine eindeutige Zeit: **181021BOKT26** = 18. Oktober, 10:21 Uhr, Zone B, Oktober 2026."),
       ("Zeitzonen-Buchstaben", "**Z** = Weltzeit (UTC) · **A** = Winterzeit MEZ (+1 h) · **B** = Sommerzeit MESZ (+2 h)")]),
     ("merke", "**»Tag X«:** Einsatzpläne zählen vom Angriffstag aus (X − 1, X + 2) – wie v. Chr. und n. Chr. mit einem eigenen **Bezugspunkt**. Berühmt: der D-Day am 6. Juni 1944.")], "Bundesheer", "dzg"),
   S("Stopp – kannst du das?", [("reveal", [
       ("Wie viele Jahre liegen zwischen 10 v. Chr. und 10 n. Chr.?", "19 Jahre: 10 + 10 − 1 – ein Jahr 0 gibt es nicht."),
       ("Du tippst »10. Oktober 1582, Rom« in die Zeitmaschine. Wo landest du?", "Nirgends – diesen Tag gab es in Rom nicht: Auf den 4. folgte der 15. Oktober. In Wien gab es ihn – dort galt bis 1584 noch der julianische Kalender.")])], "Teil 1"),
   ("jetzt", "Jetzt: Aufgaben 1–5", "aufgaben.html")]),

 ("teil2", "Teil 2 · Stunde 2 · Buch S. 14", "Die Epochen", [
   S("Was ist eine Epoche?", [("ul", [
       "Historiker teilen die Vergangenheit in **Abschnitte mit gemeinsamen Merkmalen** und geben ihnen Namen.",
       "»Epoche« kommt vom griechischen **epoché** = Haltepunkt.",
       "Epochen sind **Orientierungshilfen** – wie Planquadrate auf einer Landkarte. Die Grenzen ziehen Menschen, nicht die Natur."]),
     ("merke", "Seit der **Renaissance** teilt man in **Altertum – Mittelalter – Neuzeit**. Die Gelehrten sahen ihre Zeit als Wiedergeburt der Antike – dazwischen lag für sie ein »mittleres« Zeitalter.")], "Buch S. 14", "epoche"),
   S("Der Zeitstrahl der Epochen", [("zeitstrahl",),
     ("hint", "Nicht maßstabsgetreu: Die Ur- und Frühgeschichte dauert über 2 Millionen Jahre, die Zeitgeschichte erst gut 100 Jahre.")], "Buch S. 14", "zeitstrahl"),
   S("Die Epochen im Überblick (1)", [("table", [["Epoche", "ungefähr", "typisch"],
                                                 ["Ur- und Frühgeschichte", "bis ca. 3000 v. Chr.", "keine Schrift; Jäger und Sammler, ab ca. 9000 v. Chr. Bauern"],
                                                 ["Altertum (Antike)", "ca. 3000 v. Chr. – 476", "Hochkulturen mit Schrift (Ägypten, Mesopotamien), Griechen, Römisches Reich"],
                                                 ["Mittelalter", "476 – ca. 1500", "Christentum, Lehnswesen, Ritter, Burgen, Klöster, Städte"]], [3, 3, 6])], "Buch S. 14", "ueberblick"),
   S("Die Epochen im Überblick (2)", [("table", [["Epoche", "ungefähr", "typisch"],
                                                 ["Neuzeit", "ca. 1500 – 1914/18", "Buchdruck, Entdeckungen, Reformation, Absolutismus, Revolutionen, Industrialisierung"],
                                                 ["Zeitgeschichte", "ab 1914/18", "Weltkriege, Diktatur und Demokratie, Kalter Krieg, EU, Digitalisierung – es gibt noch Zeitzeugen"]], [3, 3, 6]),
     ("hint", "Die Neuzeit teilt man oft weiter: **Frühe Neuzeit** (bis 1789) und **Moderne**. Die Zeitgeschichte beginnt je nach Buch 1914, 1917 oder 1918.")], "Buch S. 14"),
   S("Urgeschichte: nach Werkstoffen benannt", [("table", [["Abschnitt", "Mitteleuropa, ca.", "Beispiel"],
                                                          ["Steinzeit", "bis ca. 4000 v. Chr.", "Faustkeil, Pfeil und Bogen; ab 5500 v. Chr. erste Bauern"],
                                                          ["Kupferzeit", "ca. 4000 – 2200 v. Chr.", "Ötzis Kupferbeil (um 3300 v. Chr.)"],
                                                          ["Bronzezeit", "ca. 2200 – 800 v. Chr.", "Schwerter und Schmuck aus Bronze"],
                                                          ["Eisenzeit", "ab ca. 800 v. Chr.", "Hallstattzeit, dann Kelten"]], [2, 3, 5]),
     ("merke", "**Österreich gibt einer Epoche den Namen:** Die ältere Eisenzeit heißt nach den Funden in Hallstatt (Salzkammergut) **Hallstattzeit** (ca. 800–450 v. Chr.).")], "Buch S. 14", "urg"),
   S("Das Mittelalter in drei Teilen", [("tiles", [
       ("Frühmittelalter · ca. 500–1000", "Völkerwanderung, Frankenreich, Kaiserkrönung Karls des Großen 800"),
       ("Hochmittelalter · ca. 1000–1250", "Ritter, Burgen, Kreuzzüge, neue Städte – **1194 Wiener Neustadt**"),
       ("Spätmittelalter · ca. 1250–1500", "Pest 1348, Feuerwaffen beenden die Ritterzeit")]),
     ("merke", "**Mythos aufgelöst:** Gebildete Menschen im Mittelalter wussten, dass die Erde eine **Kugel** ist. Die Scheiben-Erde ist ein Vorurteil späterer Zeiten.")], "Buch S. 14", "ma"),
   S("Wendepunkte – wo Epochen enden", [("table", [["Jahr", "Ereignis", "Übergang"],
                                                   ["476", "Germanen setzen den letzten weströmischen Kaiser ab", "Altertum → Mittelalter"],
                                                   ["um 1450", "Gutenberg erfindet den Buchdruck", "Mittelalter → Neuzeit"],
                                                   ["1492", "Kolumbus erreicht Amerika", "Mittelalter → Neuzeit"],
                                                   ["1517", "Luthers Thesen – Reformation", "Mittelalter → Neuzeit"],
                                                   ["1914–18", "Erster Weltkrieg", "Neuzeit → Zeitgeschichte"]], [2, 6, 4]),
     ("hint", "Niemand wachte 1492 auf und sagte: »Jetzt beginnt die Neuzeit!« Wendepunkte legen Historiker im Nachhinein fest.")], "Buch S. 14", "wende"),
   S("Waffen erzählen Geschichte", [("table", [["Epoche", "Waffen und Heer"],
                                               ["Ur- und Frühgeschichte", "Faustkeil, Speer, Pfeil und Bogen – später Bronze- und Eisenschwert"],
                                               ["Altertum", "Phalanx der Griechen, Legion der Römer mit Kurzschwert (Gladius)"],
                                               ["Mittelalter", "Ritter, Burg, Armbrust – ab dem 14. Jh. Kanonen"],
                                               ["Neuzeit", "stehendes Heer, Muskete – 1751/52 Militärakademie Wiener Neustadt"],
                                               ["Zeitgeschichte", "Panzer, Flugzeug, Atombombe (1945), Drohne, Cyberangriff"]], [3, 7]),
     ("hint", "Neue Waffen verändern Gesellschaften – aber Vorsicht: Eine Epoche hat nie nur **eine** Ursache.")], "Bundesheer", "waffen"),
   S("Lange und kurze Jahrhunderte", [("table", [["Name", "Zeitraum", "von … bis …"],
                                                 ["»kurzes« 20. Jh.", "1914 – 1989", "Erster Weltkrieg bis Fall der Berliner Mauer"],
                                                 ["»langes« 19. Jh.", "1789 – 1914", "Französische Revolution bis Erster Weltkrieg"],
                                                 ["»langes« 18. Jh.", "1700 – 1815", "bis zum Wiener Kongress"],
                                                 ["»langes« 16. Jh.", "1450 – 1620", "vom Buchdruck bis zum Dreißigjährigen Krieg"]], [3, 2, 5]),
     ("merke", "Für die Einteilung zählt der **Inhalt** – nicht die runde Jahreszahl.")], "Buch S. 14", "jahrhunderte"),
   S("Wessen Geschichte? Eurozentrismus", [("tiles", [
       ("Passt für …", "Europa, Vorderasien und Nordafrika – die Dreiteilung stammt von europäischen Gelehrten."),
       ("Passt nicht für …", "China zählt nach Herrscherfamilien (Dynastien). Amerika hatte kein »Mittelalter« – dort blühten Maya, Azteken und Inka."),
       ("Gleichzeitig verschieden", "Um 600 v. Chr.: Athen = Antike (Schrift!), Hallstatt = Urgeschichte (keine eigene Schrift)."),
       ("Globalgeschichte", "untersucht alle Weltregionen und ihre Verbindungen – statt nur durch die europäische Brille.")])], "Buch S. 14", "euro"),
   S("Quellenkritik: Wer zieht die Grenzen?", [("video", "zeitstrahl"),
     ("hint", "Achte darauf: Das Video lässt die Antike erst um **500 v. Chr.** beginnen, das Buch schon um **3000 v. Chr.** (Hochkulturen). Und es erzählt aus **deutscher** Sicht."),
     ("merke", "Wer hat recht? **Beide** – sie ziehen die Grenzen nach anderen Merkmalen. Frag immer: Wer hat die Einteilung gemacht – und aus welcher Sicht?")], "Buch S. 14", "video"),
   S("Zeitgeschichte in Österreich", [("table", [["Jahr", "Ereignis"],
                                                 ["1918", "Ende der Monarchie – Republik Österreich"],
                                                 ["1938", "»Anschluss« an das nationalsozialistische Deutsche Reich"],
                                                 ["1945", "Ende des Zweiten Weltkriegs – Zweite Republik"],
                                                 ["1955", "Staatsvertrag und Neutralität – das Bundesheer entsteht"],
                                                 ["1995", "Beitritt zur Europäischen Union"]], [1, 6]),
     ("merke", "Zeitgeschichte = Geschichte mit **Zeitzeugen** – frag deine Großeltern! Wer weiß, woher unsere Demokratie kommt, hält sie nicht für selbstverständlich.")], "Buch S. 14", "zg"),
   S("Stopp – kannst du das?", [("reveal", [
       ("Warum gehört Hallstatt um 600 v. Chr. noch zur Urgeschichte, Athen aber zur Antike?", "In Athen gab es Schrift, in Hallstatt nicht. Ohne eigene schriftliche Quellen zählt eine Zeit zur Ur- und Frühgeschichte."),
       ("Nenne drei Ereignisse, die für den Beginn der Neuzeit stehen.", "Buchdruck (um 1450), Entdeckung Amerikas (1492), Reformation (1517) – auch der Fall Konstantinopels (1453).")])], "Teil 2"),
   ("jetzt", "Jetzt: Aufgaben 6–10 und das Quiz", "aufgaben.html")]),
]

SCHNELLE = [
   S("Ein neues Erdzeitalter?", [("ul", [
       "Auch Geologen teilen ein – in Erd-Epochen. Seit ca. 11 700 Jahren (Ende der letzten Eiszeit) leben wir im **Holozän**.",
       "Vorschlag: **Anthropozän** – das Zeitalter des Menschen, Beginn um 1950 (Atombombentests, Plastik, Beton).",
       "März 2024: Die Fachkommission der Geologen lehnt ab – offiziell bleibt es beim Holozän. Der Streit geht weiter."]),
     ("hint", "Aufgabe 15: Welche Spuren hinterlassen wir?")], "OPTIONAL", "schnelle"),
   S("Auch die Wirtschaft hat Epochen", [("tiles", [
       ("Industrie 1.0 · ab ca. 1780", "Dampfmaschine, Fabrik, Eisenbahn"), ("Industrie 2.0 · ab ca. 1870", "Strom, Fließband, Massenproduktion"),
       ("Industrie 3.0 · ab ca. 1970", "Computer und Roboter"), ("Industrie 4.0 · heute", "Vernetzung, Daten, künstliche Intelligenz")]),
     ("hint", "Mehr dazu im Kapitel »Industrielle Revolution(en)«, Buch S. 46.")], "OPTIONAL"),
   ("jetzt", "Jetzt: Aufgaben 11–15", "aufgaben.html"),
]
