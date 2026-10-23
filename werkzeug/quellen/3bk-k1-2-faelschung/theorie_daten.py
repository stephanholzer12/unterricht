"""Theorie PBGW 3BK · K1.2 Fälschung der Hitler-Tagebücher – eine Quelle für Theorie-Seite (theorie.html) und PPP.
Bausteine: ("tiles", [(Überschrift, Text), …]) · ("ul", [...]) · ("ol", [...]) · ("merke", Text) · ("hint", Text) · ("table", [[Kopf…], …], [Breiten]) · ("reveal", [(Frage, Antwort), …]) · ("jetzt", Text, Link)"""
from inhalt import LERNZIELE

S = lambda title, blocks, pill=None, sid=None: {"title": title, "blocks": blocks, "pill": pill, "id": sid}

PARTS = [
 ("einstieg", "Einstieg", "Worum geht es?", [
   S("Eine Weltsensation – oder doch nicht?", [("tiles", [
       ("25. April 1983", "Das Magazin »Stern« präsentiert **die Tagebücher Adolf Hitlers** – rund 60 handgeschriebene Kladden. Ein Reporter hatte sie angeblich aus der DDR gerettet."),
       ("Der Preis", "Der Verlag zahlte dafür rund **9,3 Millionen D-Mark**. Geprüft wurde vorher kaum."),
       ("Nach 11 Tagen", "Am **6. Mai 1983** erklärt das Bundesarchiv offiziell: Die Bände sind **Fälschungen**."),
       ("Deine Frage", "Wie kommt man einer Fälschung auf die Spur – und wie lässt sich ein ganzer Verlag täuschen?")])], sid="einstieg1"),
   S("Das kannst du nach dieser Einheit", [("ol", LERNZIELE)])]),

 ("teil1", "Teil 1 · Buch S. 10–12", "Der Fall", [
   S("Wer ist wer?", [("table", [["Person", "Rolle"],
                                 ["Konrad Kujau", "Fälscher: schrieb die Bände selbst, verkaufte sie als »Hitlers Tagebücher«"],
                                 ["Gerd Heidemann", "»Stern«-Reporter: einziger direkter Kontakt zu Kujau, vermittelte den Kauf"],
                                 ["»Stern«-Verlag", "zahlte rund 9,3 Millionen D-Mark und stellte die Bände 1983 vor"],
                                 ["Bundesarchiv, BKA", "Fachleute, die Papier, Schrift und Inhalt prüften"],
                                 ["Max Domarus", "Historiker: seine Sammlung von Hitlers Reden war die Vorlage für den Text"]], [3, 7])], "Buch S. 10–12", "wer"),
   S("Warum glaubte man daran?", [("tiles", [
       ("Sensation = Geld", "Exklusive Weltsensation – hohe Auflage, hoher Gewinn. Je größer die Aussicht, desto geringer die Lust auf Zweifel."),
       ("Konkurrenz", "Die Angst, ein anderes Magazin könnte zuerst berichten, trieb zur Eile."),
       ("Geheimhaltung", "Nur wenige kannten die »Quelle«; Heidemann hatte als Einziger Kontakt zu Kujau."),
       ("Wunschdenken", "Man wollte glauben, was man sich erhofft hatte – das nennt man **Bestätigungsfehler**.")]),
     ("merke", "Je größer die Sensation, desto gründlicher muss man prüfen – nicht umgekehrt.")], "Buch S. 10–12", "warum"),
   S("Stopp – kannst du das?", [("reveal", [
       ("Wer fälschte die Tagebücher und wer vermittelte sie?", "Kujau fälschte sie, der »Stern«-Reporter Heidemann vermittelte sie."),
       ("Nenne zwei Gründe, warum der »Stern« nicht genauer prüfte.", "z. B. Sensation und viel Geld, Angst vor der Konkurrenz, Geheimhaltung.")])], "Teil 1"),
   ("jetzt", "Weiter mit Teil 2 – dann Aufgaben 1–3", "#teil2")]),

 ("teil2", "Teil 2 · Buch S. 10–12", "Wie flog die Fälschung auf?", [
   S("Äußere Kritik: Ist die Quelle echt?", [("ul", [
       "Fachleute des **Bundesarchivs**, des **Bundeskriminalamts (BKA)** und einer Bundesanstalt für Materialprüfung untersuchten **Papier, Aufkleber, Einband und Schrift**.",
       "Im Papier steckten **Weißmacher**, die erst **nach dem Zweiten Weltkrieg** hergestellt wurden.",
       "Solche Funde nennt man **Anachronismus**: Das Material passt nicht zur angeblichen Zeit.",
       "Auch die Herkunft war dünn: Wo die Bände 1945–1981 waren, ließ sich nicht überprüfen."]),
     ("merke", "**Äußere Kritik** = Material, Echtheit, Herkunft.")], "Buch S. 10–12", "aeussere"),
   S("Innere Kritik: Stimmt der Inhalt?", [("ul", [
       "Die Texte enthielten viele **Fehler** und kaum echte Gedanken – eher Banales im Zeitungsstil.",
       "Die Einträge folgten der **Edition von Max Domarus** (Hitlers Reden und Proklamationen). Wo Domarus irrte, irrte auch das »Tagebuch«.",
       "Wer abschreibt, hat nichts selbst erlebt."]),
     ("merke", "**Innere Kritik** = Inhalt, Absicht, Zusammenhang.")], "Buch S. 10–12", "innere"),
   S("Der Handschrift-Trick", [("ul", [
       "Zuerst verglich man die Schrift der Bände mit **Schriftproben Hitlers**. Die Gutachter sagten: »Gleiche Hand.«",
       "Das Problem: Die Vergleichsproben stammten **ebenfalls vom Fälscher**. Man verglich Fälschung mit Fälschung.",
       "Ein sauberer Vergleich braucht **gesicherte Originale** aus einem Archiv."]),
     ("hint", "Gleiche Hand heißt noch nicht: von Hitler.")], "Buch S. 10–12", "handschrift"),
   S("Werkzeugkasten Quellenkritik", [("tiles", [
       ("Wer?", "Wer hat die Quelle erstellt?"), ("Woher?", "Wie kam sie zu uns – lückenlos belegt?"),
       ("Woraus?", "Passen Material und Form zur Zeit?"), ("Wozu?", "Wem nützt die Quelle – Geld, Macht, Meinung?")]),
     ("merke", "**Eine einzige, ungeprüfte Quelle reicht nie.** Zweite, unabhängige Quelle suchen.")], "Buch S. 10–12", "werkzeug"),
   S("Stopp – kannst du das?", [("reveal", [
       ("Ordne zu: Weißmacher im Papier – äußere oder innere Kritik?", "äußere Kritik (Material, Anachronismus)."),
       ("Warum war das erste Schrift-Gutachten wertlos?", "Die Vergleichsproben stammten auch vom Fälscher.")])], "Teil 2"),
   ("jetzt", "Jetzt: Aufgaben 1–3", "aufgaben.html")]),
]

SCHNELLE = [
   S("So prüfst du eine KI-Antwort", [("ol", [
       "**Behauptung** herausschreiben (z. B. »Aufheller erst ab 1955«).",
       "**Beleg öffnen**: Steht die Quelle wirklich dort, und was genau steht da?",
       "**Primärquelle** suchen (z. B. bundesarchiv.de), nicht nur die KI fragen.",
       "**Urteil** bilden: belegt, teilweise belegt oder nicht belegt."]),
     ("hint", "KI klingt sicher, irrt aber oft bei Zahlen und Quellenangaben. Das ist **Desinformation aus Versehen** – im Lagebild wie im Alltag gefährlich."),
     ("jetzt", "Aufgabe 4: KI-Antwort prüfen", "aufgaben.html")], "OPTIONAL", "ki"),
   S("Für Schnelle: Aufgaben 4–6", [("ul", [
       "**A4** KI-Antwort prüfen (Recherche im Bundesarchiv).",
       "**A5** Geheimes Dokument im Klassenchat – drei Prüffragen.",
       "**A6** Soll ein Archiv Fälschungen aufbewahren? Argumente und Urteil."]),
     ("hint", "Beim Bundesheer entscheidet die Quellenbewertung im Lagebild über Handlungen – auch dort gilt: zwei unabhängige Quellen.")], "OPTIONAL", "schnelle"),
   ("jetzt", "Jetzt: Aufgaben 4–6", "aufgaben.html"),
]
