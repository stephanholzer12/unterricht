"""Theorie-Seite K1.8 Fairer Handel: Teile und Folien. Dieselben Daten bauen die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img, karten, buch (Leseauftrag im Schulbuch).
Neue Regeln (Auftrag 06.11.2026): Einstieg »Das Wichtigste vorab«, Schulbuchverweise, gemeinsame Aufgaben als Block »gemeinsam« gekennzeichnet (hier: hint mit Marke »Gemeinsam«).
Alles in eigenen Worten; Grafiken selbst gezeichnet (skizzen.py). Pflicht-Lesestopps: »fairhandel« (Teil 1) und »mindestpreis« (Teil 2), je etwa 3 Minuten."""
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Das Wichtigste vorab – und warum es dich betrifft", "pill": "Buch S. 35",
  "blocks": [("ul", ["**Was du heute mitnimmst:** Was »fair« beim Handel konkret heißt (Mindestpreis, Prämie, drei Säulen) – und wie du prüfst, ob eine Aussage über Fairtrade wirklich stimmt.",
                     "**Warum du das brauchst:** Schokoriegel, Energy-Kaffee, Bananen in der Kantine, Sport-Shirts – vieles davon kommt aus Ländern, in denen Bauern- und Arbeiterfamilien wenig verdienen. Du entscheidest jede Woche mit deinem Einkauf, und im Beruf später vielleicht über Einkauf für eine ganze Truppe.",
                     "**Warum es interessant ist:** Hinter einem kleinen Siegel stecken Zahlen, Interessen und Streit. Wer das durchschaut, lässt sich bei Werbung und Schlagzeilen nicht so leicht beeindrucken."]),
             ("hint", "Leitfrage der Stunde: " + I.LEITFRAGE)]},
 {"id": "s0b", "title": "Gemeinsam: Was kostet deine Schokolade wirklich?", "pill": "Gemeinsam · Buch S. 35",
  "blocks": [("hint", "**Gemeinsam mit Prof. HOLZER, per Handzeichen:** Wer isst oder trinkt pro Woche Schokolade, Kakao, Kaffee oder Energyriegel? Wie viel Prozent vom Ladenpreis kommt beim Bauern an, der den Kakao anbaut – 1 %, 6 %, 20 % oder 50 %?"),
             ("ul", ["Wir sammeln eure Schätzungen an der Tafel und kommen in der nächsten Stunde darauf zurück.",
                     "Wichtig ist nicht die richtige Zahl, sondern die Frage: **Woher bekommen wir überhaupt verlässliche Zahlen?**"])]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Teil 1 · Was heißt fair?
 ("teil1", I.wann(1) + " · Buch S. 35–37", I.TEILNAME[1], [
  {"id": "fairhandel", "title": I.ABSCHNITT_1, "pill": "Buch S. 35–37",
   "blocks": [("buch", "**Lies im Schulbuch S. 35–36** (Fairer Handel, Aufgabe 1 und die Texte dazu) und markiere: Was soll der faire Handel für Bauernfamilien verändern?"),
              ("ul", ["**Fairer Handel** heißt: Bauern- und Arbeiterfamilien im globalen Süden bekommen bessere Preise, bessere Arbeitsbedingungen und feste Handelsbeziehungen. Das Fairtrade-Siegel zeigt, dass ein Produkt nach bestimmten **Standards** erzeugt und kontrolliert wird.",
                      "Diese Standards stehen auf **drei Säulen** (Buch S. 37): **Soziales** (z. B. Verbot ausbeuterischer Kinderarbeit), **Ökologisches** (z. B. verbotene Pestizide, Bio-Anbau fördern) und **Ökonomisches** (z. B. Rückverfolgbarkeit, transparente Handelsbeziehungen).",
                      "Das erinnert dich an die **drei Säulen der Nachhaltigkeit** aus dem letzten Thema – nur auf den Handel bezogen.",
                      "Aktuelle Zahl: Laut Fairtrade Österreich lag der Umsatz mit Fairtrade-Produkten in Österreich 2025 bei rund **796 Millionen Euro**, ein Plus von 12,7 %. (Angabe von Fairtrade selbst.)"]),
              ("img", "img/saeulen.png", "Drei Spalten unter dem Titel Fairer Handel: Soziales, Ökologisches, Ökonomisches, jeweils mit zwei Beispielen", "Die drei Säulen – Inhalt nach Buch S. 37, eigene Darstellung."),
              ("hint", "**Gemeinsam: Aufgabe 1** – zu zweit die Beispiele den Säulen zuordnen, dann besprechen wir es zusammen."),
              ("merke", "Fairtrade ist **nicht automatisch Bio**: Bio-Anbau wird gefördert, aber nicht überall verlangt. »Fair« und »Bio« sind zwei Siegel mit eigenen Regeln.")]},
  {"id": "grenzen", "title": "Was ein Siegel nicht kann", "pill": "Buch S. 36–37",
   "blocks": [("tiles", [("Das Siegel zeigt", ["Es gibt festgelegte Regeln, und jemand kontrolliert sie."]),
                         ("Das Siegel zeigt nicht", ["dass **alle** Probleme gelöst sind – oder dass der Preis im Regal automatisch gerecht aufgeteilt ist."])]),
              ("ul", ["Das Wort »**fair**« selbst ist nicht gesetzlich geschützt – jeder Händler darf es in die Werbung schreiben. Darum zählt, **wer** das Siegel vergibt und kontrolliert.",
                      "**Fair Washing** heißt: Ein Produkt wird fairer dargestellt, als die Belege hergeben – das Gegenstück zu Greenwashing."]),
              ("hint", "Bundesheer-Gedanke: Auch für Kasernen, Küchen und Ausrüstung wird laufend eingekauft – große Einkäufer haben viel Einfluss darauf, woher Waren kommen. Genau darüber diskutieren wir in Aufgabe 3."),
              ("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgabe 1", "aufgaben.html#card_a1"),
 ]),

 # ---------------------------------------------------------------- Teil 2 · Mindestpreis
 ("teil2", I.wann(2) + " · Buch S. 36–38", I.TEILNAME[2], [
  {"id": "mindestpreis", "title": I.ABSCHNITT_2, "pill": "Buch S. 37–38",
   "blocks": [("buch", "**Lies im Schulbuch S. 37** den Abschnitt zu Mindestpreis und Prämie und unterstreiche: Was passiert, wenn der Weltmarktpreis tief fällt?"),
              ("ul", ["Der **Mindestpreis** ist eine **Untergrenze**: Fällt der Weltmarktpreis darunter, bekommen die Produzenten trotzdem den Mindestpreis. Liegt der Weltmarktpreis höher, gilt der höhere Preis.",
                      "Die **Fairtrade-Prämie** kommt **zusätzlich**. Die Kooperative – der Zusammenschluss vieler Bauernfamilien – entscheidet gemeinsam, wofür sie das Geld nutzt, z. B. für Schulen, Brunnen oder Gesundheit.",
                      "Aktuelle Zahlen laut Fairtrade-Meldung vom 11.12.2025 (für konventionellen Kakao): Mindestpreis **3.500 US-Dollar je Tonne**, Prämie **275 US-Dollar je Tonne**."]),
              ("img", "img/preis.png", "Liniendiagramm: ein angenommener Weltmarktpreis schwankt, darüber verläuft waagrecht der Mindestpreis; wo der Markt darunter fällt, fängt der Mindestpreis auf, wo er darüber steigt, gilt der Marktpreis", "Mindestpreis als Sicherheitsnetz – eigene Darstellung, Verlauf des Weltmarktpreises nur angenommen."),
              ("hint", "**Gemeinsam: Aufgabe 2** – zu zweit die Prämie und den Mehrerlös berechnen, danach vergleichen wir die Rechenwege.")]},
  {"id": "zahlen", "title": "Was die Zahlen zeigen – und was nicht", "pill": "Buch S. 38",
   "blocks": [("ul", ["Fairtrade hat im Herbst 2025 gemeinsam mit dem Impact Institute eine Studie zu Kakaobauernfamilien in der Elfenbeinküste veröffentlicht. Danach sank der Anteil der befragten Haushalte in **extremer Armut** von **58 % (2017)** über **36 % (2020)** auf **17 % (2024)**.",
                      "Das klingt gut – aber **lies genau**: Die Studie kommt von Fairtrade selbst und zeigt eine Entwicklung. Sie **beweist nicht**, dass Fairtrade der **einzige** Grund ist, und 17 % in extremer Armut sind noch immer viele.",
                      "Auch der Kakaopreis schwankt stark. Wenn der Weltmarkt hoch liegt, hilft der Mindestpreis wenig – dann zählen andere Dinge wie Prämie, Mitbestimmung und Beratung."]),
              ("tiles", [("Gute Fragen an jede Studie", ["Wer hat sie bezahlt oder gemacht?", "Wie viele wurden befragt?", "Mit welchem Zeitraum wird verglichen?"]),
                         ("Warnwörter", ["»beweist«, »alle«, »nie«, »allein«", "Zahlen ohne Quelle", "nur Gewinner, keine Gegenstimmen"])]),
              ("hint", "Wenn du eine Meldung liest, frage zuerst: **Wer sagt das – und was hat er davon?** Das ist auch bei KI-Antworten eine gute Frage."),
              ("reveal", I.STOPPFRAGEN[2])]},
  {"id": "diskussion", "title": "Diskussionsgrundlage: Fair einkaufen in der Kaserne?", "pill": "Gemeinsam · Buch S. 38",
   "blocks": [("hint", "**Gemeinsam: Aufgabe 3** – Vierergruppe, jeder bekommt eine Rolle. 6 Minuten Diskussion, dann entscheidet die Gruppe. Danach diskutiert Prof. HOLZER mit euch."),
              ("karten", [("Rolle 1 – Küchenchef", "Du hast ein festes Budget. Du fragst: Was kostet es mehr, und wie viele Portionen verlieren wir dadurch?"),
                          ("Rolle 2 – Sportoffizier", "Du willst gute Energiequellen für Training und Marsch. Du fragst: Schmeckt es, gibt es Qualität, und was sagen die Kadetten?"),
                          ("Rolle 3 – Umwelt- und Ethikbeauftragter", "Du willst, dass der Einkauf Wirkung hat. Du fragst: Wer kontrolliert das Siegel, und was bringt es den Bauern wirklich?"),
                          ("Rolle 4 – Kritischer Beobachter", "Du prüfst die Zahlen. Du fragst: Woher stammt die Information, wer hat ein Interesse daran, und was wird nicht gesagt?")]),
              ("hint", "Es gibt keine einzig richtige Entscheidung – wichtig sind gute Gründe, ein starkes Gegenargument und die Frage, welche Zahl ihr noch nachprüfen würdet.")]},
  ("jetzt", "Jetzt: Aufgaben 2 und 3", "aufgaben.html#card_a2"),
 ]),
]

SCHNELLE = [
 {"id": "partnercheck", "title": "Partnercheck – Karten für die Wiederholung", "pill": "Buch S. 35–38",
  "blocks": [("hint", "Zu zweit: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken (Aufgabe 7)."), ("karten", I.PARTNERKARTEN)]},
 {"id": "schnelle", "title": "Zwei Quellen, zwei Blickwinkel", "pill": "Aufgabe 8",
  "blocks": [("ul", ["**Quelle 1 (Fairtrade, Selbstdarstellung):** Fairtrade Deutschland, Kurzfassung zur Wirkung der Fairtrade-Prämie (Suche: »Fairtrade Prämienstudie Kurzfassung«).",
                     "**Quelle 2 (kritisch, 2012):** Bundeszentrale für politische Bildung, Aus Politik und Zeitgeschichte, Beitrag zu fairem Handel (Suche: »bpb APuZ 2012 Fairer Handel«). Die Zahlen sind älter, die Fragen bleiben aktuell.",
                     "Auftrag: Jede Person liest eine Quelle und erklärt sie der anderen – dann vergleicht ihr (Aufgabe 8)."]),
             ("hint", "Das ist ein deutschsprachiger Fachartikel bzw. ein Papier mit Einordnung – Interessen der Verfasser immer mitlesen.")]},
 {"id": "umschau", "title": "Kakao wird teurer – was heißt das für dich?", "pill": "Ausblick",
  "blocks": [("ul", ["Der Weltmarktpreis für Kakao ist in den letzten Jahren stark gestiegen und wieder gefallen. Das spürst du im Supermarkt bei Schokolade und Riegeln.",
                     "Frage zum Weiterdenken: Wenn der Weltmarkt sehr hoch liegt – bringt der Mindestpreis den Bauern dann noch etwas? Und was bleibt von der Prämie?"])]},
 ("jetzt", "Zu den Zusatzaufgaben 4–9", "aufgaben.html#card_a4"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Was heißt fair?", "teil2": "Teil 2 · Mindestpreis",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}
