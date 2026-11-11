"""Theorie-Seite K2.1 Globalisierung: Teile und Folien. Dieselben Daten bauen die Theorie-Folien der TH-Lehrer-/TH-Kadetten-PPP und die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag im Schulbuch).
Alles in eigenen Worten (Buch S. 42–51 als Orientierung, kein Buchtext, keine Buchbilder); Grafiken selbst gezeichnet (skizzen.py). Lesezeit: ca. 130 Wörter/min.
KARTEN = Theorie-Karten für die Tipp-Stufen im Arbeitsblatt (höchstens 3 kurze Sätze, ein Bild). Aktuelle Zahlen tragen Datum und Quelle (Stand 11.11.2026)."""
import re
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Das Wichtigste vorab – wozu brauchst du das?", "pill": "Einstieg",
  "blocks": [("tiles", [("Wozu das Ganze?", ["Fast alles, was du nutzt, hängt an weltweiten Netzen: Handy, Sportschuhe, Treibstoff, Funkgeräte, Streaming. Wer Globalisierung versteht, versteht Preise, Lieferengpässe und Machtfragen."]),
                        ("Für dich", ["**Sport und Heer:** Ausrüstung und Rohstoffe kommen oft aus dem Ausland – Lieferfähigkeit ist Sicherheitspolitik. **Beruf:** Handel, Daten und Regeln bestimmen, wo Jobs entstehen. **Alltag:** Jede Zeitungsmeldung über Zölle trifft am Ende auch Preise."])]),
             ("ul", ["Dein Buch: Teil II »Aspekte der Internationalisierung und Globalisierung«, Kapitel »Die Welt ohne Grenzen«, **S. 42–51**.",
                     "Heute geht es um zwei Fragen: Wann begann die Globalisierung – und was treibt sie an? Danach: Was bringt die Digitalisierung, und wer bleibt dabei draußen?"]),
             ("hint", "Leitfrage: " + I.LEITFRAGE + " Die Institutionen der Globalisierung (WTO, IWF, Weltbank) und die Auswirkungen kommen ab 27.11.")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Stunde 1
 ("teil1", I.TEILNAME[1].split(" · ")[0] + " · " + I.wann(1) + " · " + I.TEILBUCH[1], I.TEILNAME[1].split(" · ", 1)[1], [
  {"id": "beginn", "title": "Wann begann die Globalisierung?", "pill": "Buch S. 42–44",
   "blocks": [("ul", ["**Globalisierung** heißt: Wirtschaft, Gesellschaft und Kultur sind weltweit immer dichter verflochten. Das Wort wird seit den 1960er-Jahren häufig benutzt, das Phänomen ist aber viel älter.",
                      "Einen **einzigen Beginn** gibt es nicht. Je nachdem, was du als Kennzeichen ansiehst, setzt du ihn früher oder später an. Das Buch nennt unter anderem: **1492** (Kolumbus erreicht Amerika), **1844** (erste Nachricht per Telegraf), **1944** (Gründung von IWF und Weltbank), die **1980er** (neue Technik, Rivalität USA – Sowjetunion) und **Kommunikationssatelliten und Internet**.",
                      "Manche Fachleute sprechen schon im 15. Jahrhundert von einer »ersten Globalisierung«. Sicher ist: Ab der Mitte des 19. Jahrhunderts nahm der Handel besonders stark zu, bis der Erste Weltkrieg das beendete. In der **Zwischenkriegszeit** ging die Verflechtung zurück (**Deglobalisierung**).",
                      "Im Alltag spürst du sie täglich: Obst aus Übersee, Geräte aus Asien, Nachrichten in Sekunden. Prüf bei deinen Sachen, woher sie kommen."]),
              ("img", "img/zeitstrahl.png", "Zeitstrahl mit fünf Zeitpunkten: 1492 Kolumbus, 1844 Telegraf, 1944 IWF und Weltbank, 1980er Technik, ab den 1990ern Internet. Darunter der Hinweis auf die Deglobalisierung der Zwischenkriegszeit.",
               "Je nach Kriterium beginnt die Globalisierung früher oder später."),
              ("merke", "Es gibt **keine einzelne Geburtsstunde** – wichtig ist, dass du dein **Kriterium** begründest."),
              ("buch", "Lies im Buch S. 43 den Kasten »Für manche begann die Globalisierung …« und S. 44 die ersten beiden Absätze. Die Aufgaben am Rand von S. 42–44 eignen sich fürs Heft.")]},
  {"id": "china", "title": "Folgen für die Weltgeschichte? – ein Gedankenspiel", "pill": "Gemeinsam",
   "blocks": [("ul", ["**Gemeinsam:** Wir besprechen das in der Klasse. Zwischen 1405 und 1433 schickte China große Flotten unter **Zheng He** bis nach Indien und Ostafrika. Danach endeten die staatlichen Seefahrten. Das ist gesichert.",
                      "Oft liest man verkürzt: »China zerstörte seine Marine, weil die Herrscher Angst vor Freihandel hatten.« Das ist eine **vereinfachte Deutung**. Quellen nennen eher hohe Kosten und innenpolitischen Streit – wie viel davon stimmt, ist unter Fachleuten diskutiert.",
                      "Gedankenspiel, **kein Fakt**: Was wäre geschehen, wenn China weitergesegelt wäre – eine Globalisierung mit Zentrum in Asien? Wer hätte Kolonien gegründet? Welche Rolle hätte Europa gespielt?",
                      "Quellenkritik an einer Überschrift: Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere Quellen?"]),
              ("hint", "Quellen: EBSCO Research Starter »Zheng He's Naval Expeditions« (geprüft am 11.11.2026). Die Folgen im Gedankenspiel sind Vermutungen.")]},
  {"id": "stop1a", "title": "Stopp – kannst du das?", "pill": "Buch S. 43–44", "blocks": [("reveal", I.STOPPFRAGEN[1][:1])]},
  ("jetzt", "Jetzt: Aufgabe 1", "aufgaben.html#a1"),
  {"id": "antrieb", "title": "Sechs Antriebskräfte der Globalisierung", "pill": "Buch S. 45–47",
   "blocks": [("ul", ["**1 · Informationsrevolution:** Neue Technik (PC, Handy, Navigation, Netze) bringt Informationen in kürzester Zeit um die Welt. Das Internet verändert Arbeit, Lernen und Freizeit. Noch ist es nicht überall verbreitet.",
                      "**2 · Innovationen im Transport:** Containerschiffe, Hochgeschwindigkeitszüge und Großraumflugzeuge machten Transporte billiger und schneller. Bis zur Mitte des 20. Jahrhunderts sanken die Kosten für See- und Lufttransport um mehr als zwei Drittel.",
                      "**3 · Marktwirtschaft:** Nach dem Zusammenbruch der kommunistischen Systeme in Osteuropa (1989/1991) setzte sich das marktwirtschaftliche System fast weltweit durch – auch das kommunistisch regierte China hat heute marktwirtschaftliche Elemente.",
                      "**4 · Liberalisierung:** Abbau von Handelshemmnissen und Öffnung der Märkte für Güter, Dienstleistungen und Kapital (siehe nächster Abschnitt).",
                      "**5 · Transnationale Konzerne:** Unternehmen gründen Tochterfirmen im Ausland, nutzen Kosten- und Steuervorteile und teilen die Arbeit weltweit auf. **Global Player** sind meist durch Fusionen und Übernahmen entstanden.",
                      "**6 · Normen und Standards:** Gemeinsame technische Regeln (z. B. Stecker, Spurbreiten, ISO-Normen) erleichtern den internationalen Handel.",
                      "Dazu kommen neue Produktionskonzepte: **Lean Production** und **Just-in-time** (Teile kommen genau dann, wenn man sie braucht) und **Outsourcing** (Auslagerung an andere Betriebe)."]),
              ("img", "img/antriebskraefte.png", "Sechs Felder: Informationsrevolution, Transporttechnik, Marktwirtschaft, Liberalisierung, Transnationale Konzerne, Normen und Standards.", "Sechs Antriebskräfte – ordne die Beispiele aus Aufgabe 2 zu."),
              ("merke", "Es gibt nicht **die eine** Ursache – die sechs Kräfte verstärken sich gegenseitig."),
              ("buch", "Lies im Buch S. 45 (Informationsrevolution, Transport) und S. 46 (Marktwirtschaft bis Normen). Die Begriffsliste am linken Rand von S. 46 (Global Village, Global Player …) ist gutes Nachschlagematerial.")]},
  {"id": "liberal", "title": "Liberalisierung und Neoliberalismus", "pill": "Buch S. 46–47",
   "blocks": [("ul", ["Der **Liberalismus** war im 19. Jahrhundert die wichtigste politische Idee des aufstrebenden Bürgertums. Er forderte drei Freiheiten: **individuelle** Freiheit, **politische** Freiheit (durch den Rechtsstaat) und **wirtschaftliche** Freiheit (Eigentum, freie Märkte).",
                      "Heute spricht man vom **Neoliberalismus**, wenn es vor allem um die wirtschaftliche Seite geht: Märkte für Güter, Dienstleistungen und Kapital werden geöffnet, Handelshemmnisse abgebaut. Dazu gehören **Deregulierung** (weniger Vorschriften) und **Privatisierung** (z. B. Telefon, Energie, Wasser) sowie die Öffnung der Finanzmärkte.",
                      "**Zwei Sichtweisen, beide gehören zur Diskussion:** Befürworter nennen Wohlstand, Wettbewerb und Innovation. Kritiker – im Buch zitiert Kurt Rothschild – sehen die Gefahr, dass wirtschaftliche Interessen die Demokratie überlagern. Als Gewährsmann der Marktgesellschaft nennt der Text Friedrich Hayek.",
                      "Die Buch-Aufgabe 2 auf S. 47 fragt dich nach deiner Stellungnahme. Prüf dafür: Wer sagt das? Welche Belege nennt er? Welche Interessen hat er?"]),
              ("hint", "Das ist eine Diskussionsfrage – du bildest dir dein eigenes Urteil. Es gibt hier keine »richtige« Partei.")]},
  {"id": "stop1b", "title": "Stopp – kannst du das?", "pill": "Buch S. 46–47", "blocks": [("reveal", I.STOPPFRAGEN[1][1:])]},
  ("jetzt", "Jetzt: Aufgabe 2", "aufgaben.html#a2"),
 ]),

 # ---------------------------------------------------------------- Stunde 2
 ("teil2", I.TEILNAME[2].split(" · ")[0] + " · " + I.wann(2) + " · nach dem Test · " + I.TEILBUCH[2], I.TEILNAME[2].split(" · ", 1)[1], [
  {"id": "digital", "title": "Digitalisierung und Digital Divide", "pill": "Buch S. 48 · ITU 2025",
   "blocks": [("ul", ["Eine Prognose aus dem Jahr 2015 (im Buch zitiert) erwartete: Technik und Kapital gewinnen an Bedeutung, Arbeit verliert an Gewicht; Produktion kehrt teils näher an die Märkte zurück; Kundinnen und Kunden werden an der Herstellung beteiligt. **Prüf selbst:** Was davon spürst du heute?",
                      "**Wer ist offline?** Laut der UN-Organisation **ITU** (Facts and Figures 2025, 17.11.2025) nutzen rund **6 Milliarden** Menschen das Internet, **2,2 Milliarden** nicht. In Ländern mit hohem Einkommen sind es **94 %** Nutzer, in Ländern mit niedrigem Einkommen **23 %**. In Städten sind **85 %** online, auf dem Land **58 %**. Bei Männern **77 %**, bei Frauen **71 %**.",
                      "Diese Ungleichheit heißt **Digital Divide**. Das Buch nennt etwa 32 % ohne Internet – die ITU zählt für 2025 rund ein Viertel. **Quellen zählen verschieden** (Jahr, Messweise, Definition von »Nutzer«). Darum immer Quelle und Jahr nennen.",
                      "**Corona-Pandemie:** Homeoffice, Distance Learning und Online-Termine wurden stark beschleunigt. Wer keine Geräte oder keinen Zugang hatte, wurde abgehängt. Auch zwischen den Generationen gibt es Unterschiede in der Nutzung."]),
              ("img", "img/digital_divide.png", "Balkendiagramm: Internetnutzung 2025 in Ländern mit hohem Einkommen 94 Prozent, mit niedrigem Einkommen 23 Prozent, Stadt 85, Land 58, Männer 77, Frauen 71 Prozent.",
               "Digital Divide in Zahlen (ITU, Facts and Figures 2025)."),
              ("merke", "**Prozentpunkte** sind der Unterschied zweier Prozentwerte: 94 % − 23 % = **71 Prozentpunkte**."),
              ("buch", "Lies im Buch S. 48 den Abschnitt »Ein Segen für alle?« und die Prognose von 2015. Die Buch-Aufgaben 1–3 am Seitenende eignen sich fürs Heft (Länder mit wenig Internet recherchieren: Startseite ITU DataHub).")]},
  {"id": "stop2a", "title": "Stopp – kannst du das?", "pill": "Buch S. 48", "blocks": [("reveal", I.STOPPFRAGEN[2])]},
  ("jetzt", "Jetzt: Aufgabe 3", "aufgaben.html#a3"),
  {"id": "ampel", "title": "Ziele erreicht? Statement-Ampel im Raum", "pill": "Buch S. 51 · Gemeinsam",
   "blocks": [("ul", ["**So läuft es (ohne Handy):** Prof. Holzer liest eine Aussage vor. Du stellst dich in eine Zone: **stimmt – unklar – stimmt nicht**. Dann prüft ihr in der Gruppe die Aussage mit den vier Fragen (Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere?) und stellt euch neu auf. Wer wechselt, sagt in einem Satz warum.",
                      "**Aussagen (nach Buch S. 51, in eigenen Worten):** (1) Globalisierung ist eine Bereicherung für Europa. (2) Als Gegenreaktion auf die Globalisierung gewinnt der Nationalismus wieder an Bedeutung. (3) Lokale Wirtschaftskreisläufe sollten globale ersetzen. (4) Die Schäden des US-Handelskriegs zeigen, wie eng die Weltwirtschaft verflochten ist.",
                      "Es gibt **keine Note** und keine »richtige Seite«. Gute Begründungen nennen eine Zahl, eine Quelle und ein Gegenargument."]),
              ("hint", "Heute probieren wir zwei Aussagen. Übrige Aussagen kannst du in Ruhe selbst prüfen.")]},
 ]),
]

KARTEN = {
 "beginn": {"text": ["Es gibt **keinen einzigen Beginn** der Globalisierung – je nach **Kriterium** nennt man 1492, 1844, 1944, die 1980er oder das Internet.",
                     "Die **Zwischenkriegszeit** war eine Phase der **Deglobalisierung**.",
                     "Wichtig: Dein Kriterium begründen."], "bild": ("img/zeitstrahl.png", "Zeitstrahl mit fünf möglichen Anfängen der Globalisierung"), "teil": "Teil 1", "link": "theorie.html#beginn", "buch": "Buch S. 43–44"},
 "antrieb": {"text": ["Sechs Kräfte treiben die Globalisierung an: **Information, Transport, Marktwirtschaft, Liberalisierung, Konzerne, Normen**.",
                      "**Liberalisierung** = Zölle und Hürden **abbauen**, Märkte **öffnen**.",
                      "Normen (z. B. Stecker) und Containerschiffe senken Kosten."], "bild": ("img/antriebskraefte.png", "Sechs Antriebskräfte der Globalisierung"), "teil": "Teil 1", "link": "theorie.html#antrieb", "buch": "Buch S. 45–47"},
 "digital": {"text": ["**Digital Divide** = ungleicher Zugang zu Internet und Technik.",
                      "ITU 2025: **94 %** online in reichen, **23 %** in ärmsten Ländern; **2,2 Mrd.** Menschen offline.",
                      "**Prozentpunkte** = größerer Wert minus kleinerer Wert."], "bild": ("img/digital_divide.png", "Balkendiagramm zur Internetnutzung 2025"), "teil": "Teil 2", "link": "theorie.html#digital", "buch": "Buch S. 48"},
 "zoelle": {"text": ["Ein **Zoll** ist eine Abgabe auf Importe; zuerst zahlt ihn der **Importeur**.",
                     "Das Buch zeigt den Stand **2025** (bis 145 % auf China-Waren). Seither wurde vieles geändert.",
                     "Immer **Datum und Rechtsgrundlage** nennen."], "bild": None, "teil": "Zusatz", "link": "theorie.html#zoelle", "buch": "Buch S. 50–51"},
 "stiglitz": {"text": ["Joseph **Stiglitz** (US-Ökonom) sagt: **Offene Märkte allein** lösen die Armut nicht.",
                       "Er kritisiert Subventionen der reichen Staaten und fordert Investitionen in **Bildung**.",
                       "Er beschreibt auch Verlierer in den Industriestaaten."], "bild": None, "teil": "Zusatz", "link": "theorie.html#stiglitz", "buch": "Buch S. 49"},
}

SCHNELLE = [
 {"id": "zoelle", "title": "ZUSATZ · Aufgabe 5: US-Zölle 2025 und heute", "pill": "Aktuell",
  "blocks": [("ul", ["Ein **Zoll** ist eine Abgabe auf Importe. Er wird nach dem **Zollwert** und dem **Zollsatz** berechnet; zuerst zahlt ihn der **Importeur**. Wer ihn am Ende trägt (Marge, Preis, Lieferant), hängt von Nachfrage, Verträgen und Wettbewerb ab.",
                     "Das Buch beschreibt den Stand **2025**: massive US-Zölle, bis zu 145 % auf Waren aus China, Gegenzölle von 125 %.",
                     "**Seither:** Der US Supreme Court erklärte am **20.02.2026** die auf IEEPA gestützten Zölle für rechtswidrig (WKO, Seite vom 23.10.2026). Im Oktober 2025 hatten Trump und Xi vereinbart, bestimmte Zölle etwa ein Jahr auszusetzen. Am **09.11.2026** berichtete die Berliner Zeitung (nach Xinhua, Reuters, dpa): China setzt den Zusatzzoll von 24 % auf US-Waren für weitere zwei Monate aus, ein Aufschlag von 10 % bleibt; die Vereinbarung ist laut Artikel noch nicht endgültig.",
                     "Heißt das »Handelskrieg vorbei«? Das lässt sich aus der Meldung nicht sagen. Darum: immer **Datum, Ware, Land und Rechtsgrundlage** nennen."]),
             ("hint", "Quellen: Berliner Zeitung 09.11.2026 (Autorin Anika Schlünz, Agenturen Xinhua/Reuters/dpa); WKO (23.10.2026). Stand der Meldungen vor dem Unterricht erneut prüfen.")]},
 {"id": "stiglitz", "title": "ZUSATZ · Aufgabe 6: Stiglitz und die Kritik an der Globalisierung", "pill": "Buch S. 49",
  "blocks": [("ul", ["Joseph **Stiglitz** ist US-Ökonom und war laut Buch Chefökonom der Weltbank. Er sieht Globalisierung **differenziert**.",
                     "Seine Hauptpunkte (Buch S. 49): Globalisierung ist mehr als Marktöffnung. Offene Märkte allein lösen die Armut nicht. Reiche Staaten behalten Subventionen, arme sollen sie abbauen. Patente auf traditionelles Wissen nennt er **Biopiraterie**. **Bildung** ist der Schlüssel (Beispiel Bangalore/Indien).",
                     "Auch in den Industriestaaten geraten **gering Qualifizierte** unter Druck."]),
             ("merke", "Prüfe jede Position: Wer sagt das, mit welchen Belegen, und was könnte ein Gegenargument sein?")]},
 {"id": "alltag", "title": "ZUSATZ · Aufgabe 4: Woher kommt dein Alltag?", "pill": "Bewegung · Buch S. 44",
  "blocks": [("ul", ["Geh zu zweit durch den Raum oder schau in deine Tasche und such **drei Gegenstände** mit Herkunftsangabe. Trag Gegenstand und Land ein.",
                     "Auf Etiketten steht oft nur, **wo zusammengebaut** wurde – nicht, woher Rohstoffe und Bauteile stammen.",
                     "**Bundesheer-Bezug:** Wähle ein Ausrüstungsstück (Rucksack, Stiefel, Funkgerät) und überlege, welche Stufen im Ausland liegen könnten. Ohne Beleg ist das eine Vermutung."])]},
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Stunde 1 · Beginn", "teil2": "Stunde 2 · Digital", "begriffe": "Fachbegriffe", "kurz": "Kurz & knapp", "schnelle": "Zusatz"}


def _text(b):
    k = b[0]
    if k in ("ul", "ol"): return " ".join(b[1])
    if k == "table": return " ".join(" ".join(r) for r in b[1])
    if k == "tiles": return " ".join(h + " " + " ".join(x if isinstance(x, str) else " ".join(x) for x in (bl if isinstance(bl, list) else [bl])) for h, bl in b[1])
    if k in ("merke", "hint", "buch"): return b[1]
    if k == "img": return b[3]
    return ""


def woerter(ids):
    """Wortzahl der genannten Abschnitte (Lesezeit-Prüfung)."""
    allei = {it["id"]: it for p in PARTS for it in p[3] if isinstance(it, dict)}
    allei.update({it["id"]: it for it in SCHNELLE})
    n = 0
    for i in ids:
        for b in allei[i]["blocks"]: n += len(re.sub(r"\*\*", "", _text(b)).split())
    return n


if __name__ == "__main__":
    for ids in (["beginn", "china"], ["antrieb", "liberal"], ["digital"], ["ampel"]):
        w = woerter(ids); print(ids, w, "Wörter ≈", round(w / 130, 1), "min")
