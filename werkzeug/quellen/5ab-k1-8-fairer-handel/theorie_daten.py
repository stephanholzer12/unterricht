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
                      "Aktuelle Zahlen laut Fairtrade-Meldung vom 11.12.2025 (für konventionellen Kakao): Mindestpreis **3.500 US-Dollar je Tonne**, Prämie **275 US-Dollar je Tonne**.",
                      "**Wie stark der Markt schwankt:** Im Dezember 2023 kostete eine Tonne Kakao über 12.000 US-Dollar, im Oktober 2025 etwa 5.900 (ORF.at), Ende März 2026 nur noch rund 3.100 (APA). Das liegt **unter** dem Fairtrade-Mindestpreis von 3.500 – genau dann zeigt sich, wofür das Sicherheitsnetz da ist."]),
              ("img", "img/preis.png", "Liniendiagramm: ein angenommener Weltmarktpreis schwankt, darüber verläuft waagrecht der Mindestpreis; wo der Markt darunter fällt, fängt der Mindestpreis auf, wo er darüber steigt, gilt der Marktpreis", "Mindestpreis als Sicherheitsnetz – eigene Darstellung, Verlauf des Weltmarktpreises nur angenommen."),
              ("hint", "**Gemeinsam: Aufgabe 2** – zu zweit die Prämie und den Mehrerlös berechnen, danach vergleichen wir die Rechenwege.")]},
  {"id": "zahlen", "title": "Was die Zahlen zeigen – und was nicht", "pill": "Buch S. 38",
   "blocks": [("ul", ["Fairtrade hat im Herbst 2025 gemeinsam mit dem Impact Institute eine Studie zu Kakaobauernfamilien in der Elfenbeinküste veröffentlicht. Danach sank der Anteil der befragten Haushalte in **extremer Armut** von **58 % (2017)** über **36 % (2020)** auf **17 % (2024)**.",
                      "Das klingt gut – aber **lies genau**: Die Studie kommt von Fairtrade selbst und zeigt eine Entwicklung. Sie **beweist nicht**, dass Fairtrade der **einzige** Grund ist, und 17 % in extremer Armut sind noch immer viele.",
                      "Auch der Kakaopreis schwankt stark. Wenn der Weltmarkt hoch liegt, hilft der Mindestpreis wenig – dann zählen andere Dinge wie Prämie, Mitbestimmung und Beratung.",
                      "Auch das Siegel selbst wird kritisiert. Die steirische Schokoladenmanufaktur **Zotter** verzichtet bewusst auf das Fairtrade-Siegel: Grund ist der **Mengenausgleich** (Massenbilanzierung) – er erlaubt, dass in einem Produkt mit Fairtrade-Siegel auch nicht fair gehandelter Kakao steckt, solange die eingekaufte Fairtrade-Menge insgesamt passt. Zotter will für jede Bohne die genaue Herkunft kennen und ist seit 2018 stattdessen über die World Fair Trade Organisation (WFTO) zertifiziert.",
                      "Fairtrade Österreich hält dagegen: Ohne Mengenausgleich müssten Hersteller teurer in getrennten Chargen produzieren – das könnte die Preise erhöhen und am Ende weniger Verkauf und weniger Einkommen für die Bauern bedeuten. Für die Kooperative zähle vor allem, dass verkaufte und bezahlte Menge zusammenpassen.",
                      "Beide Seiten haben ein Interesse: Zotter wirbt mit seinem eigenen, strengeren Zeichen, Fairtrade verteidigt sein System. Das zeigt: Auch bei Firmen und Organisationen lohnt sich die Frage **wer sagt das – und was hat er davon?**"]),
              ("tiles", [("Gute Fragen an jede Studie", ["Wer hat sie bezahlt oder gemacht?", "Wie viele wurden befragt?", "Mit welchem Zeitraum wird verglichen?"]),
                         ("Warnwörter", ["»beweist«, »alle«, »nie«, »allein«", "Zahlen ohne Quelle", "nur Gewinner, keine Gegenstimmen", "ein Siegel ≠ automatisch 100 % Inhalt"])]),
              ("hint", "Wenn du eine Meldung liest, frage zuerst: **Wer sagt das – und was hat er davon?** Das ist auch bei KI-Antworten eine gute Frage."),
              ("reveal", I.STOPPFRAGEN[2])]},
  {"id": "meldungen", "title": "Aktuelle Meldungen – echte Artikel", "pill": "Aufgabe 4",
   "blocks": [("hint", "Zeitungen, Agenturen und Universitäten schreiben über Kakao und Fairtrade – nicht alle meinen dasselbe. Für Aufgabe 4 liest du eine dieser Meldungen (alle auf Deutsch, Stand 06.11.2026):"),
              ("ul", ["[ORF.at, 11.10.2025: Geringe Nachfrage, gute Ernte – Ende der »dramatischen Rallye« beim Kakaopreis](https://orf.at/stories/3407768/)",
                      "[epd/evangelisch.de, 03.04.2026: Westafrikas Bauern kämpfen mit Preissturz](https://www.evangelisch.de/inhalte/254311/03-04-2026/lebensgrundlage-kakao-westafrikas-bauern-kaempfen-mit-preissturz)",
                      "[VOL.AT/APA, 31.03.2026: Schokohasen-Schock – Preise steigen trotz Kakao-Crash](https://www.vol.at/schokohasen-schock-preise-steigen-trotz-kakao-crash/10082315)",
                      "[epd, 01.07.2019: Studie der Uni Göttingen – Fairtrade hilft nicht allen Landarbeitern](https://www.evangelisch.de/inhalte/157512/01-07-2019/studie-fairtrade-hilft-nicht-allen-landarbeitern-afrika)",
                      "[Fairtrade, Herbst 2025: Studie zu Kakaobauern in der Elfenbeinküste (Selbstdarstellung)](https://www.fairtrade.net/at-de/newsroom/presse/pressemitteilungen/weniger-armut-im-kakaoanbau--fairtrade-staerkt-einkommen-von-kak.html)",
                      "[zotter.at, 17.–18.08.2018 (Kurier-Interview): Zotter verzichtet künftig auf das Fairtrade-Logo](https://www.zotter.at/das-ist-zotter/news/news-detailseite/zotter-verzichtet-kuenftig-auf-das-fairtrade-logo)"]),
              ("hint", "Achte darauf, **wer schreibt**: Agentur, Kirchenpresse, Universität oder Fairtrade selbst – und was die Quelle damit erreichen will.")]},
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
  "blocks": [("hint", "Zu zweit: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken."), ("karten", I.PARTNERKARTEN)]},
 {"id": "umschau", "title": "Warum wird Schokolade trotzdem nicht billiger?", "pill": "Ausblick",
  "blocks": [("ul", ["Der Kakaopreis ist seit 2024 stark gefallen – im Supermarkt kamen laut APA-Bericht (31.03.2026) Osterhasen trotzdem 7 bis 29 % teurer in die Regale. Hersteller verweisen auf alte, teure Lieferverträge bis Ende 2026, dazu auf teurere Nüsse, Verpackung und Energie.",
                     "Frage zum Weiterdenken: Wer verdient am Preisverfall – und wer trägt das Risiko? Was sagt das über die Idee eines Mindestpreises?"])]},
 ("jetzt", "Zu den Zusatzaufgaben 4–6", "aufgaben.html#card_a4"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Was heißt fair?", "teil2": "Teil 2 · Mindestpreis",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}
