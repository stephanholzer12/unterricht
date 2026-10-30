"""Theorie-Seite K1.4–1.5 Ökodesign und Ökobilanz: Teile und Folien. Dieselben Daten bauen die Theorie-Folien der TH-Lehrer-/TH-Kadetten-PPP
und die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag im Schulbuch).
Alles in eigenen Worten; Grafiken selbst gezeichnet (skizzen.py). Pflicht-Lesestopps: »oekodesign« + »kriterien« (Teil 1) und »oekobilanz« + »schritte« (Teil 2), je etwa 4 Minuten."""
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Welche Flasche würdest du beschaffen?", "pill": "Buch S. 19",
  "blocks": [("img", "img/flaschen.png", "Zwei schematische Trinkflaschen: A sehr leicht, 8 Euro, Deckel fest verbaut; B robuster, 30 Euro, Deckel und Dichtung als Ersatzteile erhältlich", "Zwei ausgedachte Flaschen – keine echten Produkte."),
             ("ul", ["Für Sport und Ausbildung sollen neue Trinkflaschen her. **Flasche A** ist sehr leicht und kostet 8 €, der Deckel ist fest verbaut. **Flasche B** ist robuster, kostet 30 €, Deckel und Dichtung kann man nachkaufen.",
                     "**Welche würdest du beschaffen – per Handzeichen?** Und vor allem: **Welche Information fehlt dir noch**, um das wirklich zu entscheiden?"]),
             ("hint", "Leitfrage der Stunde: " + I.LEITFRAGE)]},
 {"id": "s0b", "title": "Mythos-Check: »Recycelbar – also umweltfreundlich?«", "pill": "Buch S. 20",
  "blocks": [("tiles", [("Was viele meinen", ["Steht »recycelbar« oder »aus Recyclingmaterial« drauf, ist das Produkt automatisch gut für die Umwelt."]),
                        ("Was dahintersteckt", ["Das Wort sagt nur etwas über **einen** Abschnitt im Leben eines Produkts. Ob es lange hält, wie viel Energie die Herstellung braucht und ob wirklich recycelt wird, steht nicht drauf."])]),
             ("hint", "Heute klären wir, wie man so etwas nachvollziehbar prüft – mit Ökodesign und Ökobilanz.")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Teil 1 · Ökodesign
 ("teil1", I.wann() + " · Buch S. 19–21", I.TEILNAME[1], [
  {"id": "oekodesign", "title": I.ABSCHNITT_1, "pill": "Buch S. 19–20",
   "blocks": [("ul", ["**Ökodesign** heißt: Ein Produkt wird so entwickelt, dass es über seinen ganzen Lebenszyklus möglichst wenig Umwelt belastet. Erst nach der Produktion an die Mülltrennung zu denken, reicht nicht. "
                      "Schon die Wahl der Materialien, die Bauweise, der Energiebedarf und die Reparaturmöglichkeiten entscheiden über spätere Belastungen.",
                      "Zum **Lebenszyklus** gehören Rohstoffgewinnung, Herstellung, Transport und Verkauf, Nutzung und Pflege sowie Wiederverwendung, Verwertung oder Entsorgung. "
                      "Eine Verbesserung in einem Abschnitt kann woanders Nachteile bringen: Eine besonders leichte Flasche spart Material und Transportgewicht. Geht sie früh kaputt, frisst der Nachkauf diesen Vorteil wieder auf.",
                      "Wichtige Ziele sind lange Nutzbarkeit, passende Materialmenge, wenig Energie und Hilfsstoffe, Reparierbarkeit, erhältliche Ersatzteile, trennbare Bauteile und der Verzicht auf problematische Stoffe. "
                      "Sicherheit, Hygiene und Gebrauchstauglichkeit bleiben dabei Pflicht."]),
              ("img", "img/lebenszyklus.png", "Kreis aus fünf Abschnitten: Rohstoffe, Herstellung, Transport und Verkauf, Nutzung und Pflege, Nutzungsende. Ein gestrichelter Pfeil vom Nutzungsende zu den Rohstoffen steht für Recycling als möglichen Weg.", "Der Lebenszyklus – Inhalt nach Buch S. 23, eigene Darstellung. Recycling ist ein möglicher Weg zurück, kein Automatismus."),
              ("merke", "Ökodesign verändert die **Gestaltung**. Eine Ökobilanz prüft, welche **Umweltfolgen** damit verbunden sind.")]},
  {"id": "kriterien", "title": "Woran man Ökodesign erkennt", "pill": "Buch S. 20",
   "blocks": [("tiles", [("Lange nutzen", ["haltbar gebaut, reparierbar, **Ersatzteile** erhältlich – ein kleiner Defekt macht nicht das ganze Produkt zu Abfall"]),
                         ("Kluge Materialien", ["so viel wie nötig, so wenig wie möglich; **trennbar** und gekennzeichnet; problematische Stoffe vermeiden"]),
                         ("Wenig Energie", ["in der Herstellung **und** in der Nutzung – bei der Flasche etwa beim Reinigen"])]),
              ("hint", "Bundesheer-Gedanke: Ausrüstung, die sich vor Ort reparieren lässt und für die es Ersatzteile gibt, bleibt länger einsatzbereit. Das ist gut für die Umwelt **und** für die Versorgung."),
              ("hint", "Buch S. 19 vergleicht Glühbirne und LED. Fair ist das nur für **dieselbe Leistung**, z. B. gleich viel Licht über 10.000 Stunden. Wie viele Lampen man dafür braucht, rechnet man mit ein – genau wie bei unseren Flaschen.")]},
  {"id": "vorteile", "title": "Was bringt das – und was nicht?", "pill": "Buch S. 20",
   "blocks": [("tiles", [("Möglicher Nutzen", ["geringere Material- und Nutzungskosten, weniger Abfall, zufriedene Kunden, besseres Image"]),
                         ("Aber", ["Diese Vorteile sind **möglich**, nicht automatisch. Kosten, Umwelt und Image können auch auseinanderlaufen – man muss sie belegen."])]),
              ("ul", ["**Greenwashing** heißt: Ein Produkt wird grüner dargestellt, als die Belege hergeben – etwa durch ein grünes Blatt auf der Packung.",
                      "»Recycelbar« oder »aus Recyclingmaterial« allein belegt noch keine insgesamt gute Umweltbilanz."])]},
  {"id": "eu", "title": "Was gilt heute in der EU?", "pill": "Buch S. 21 · aktualisiert",
   "blocks": [("ul", ["Buch S. 21 beschreibt die ältere Ökodesign-Regelung für Elektrogeräte. Seit **18. Juli 2024** gibt es einen breiteren EU-Rahmen für nachhaltige Produkte: Er kann für fast alle Waren gelten, die genauen Regeln kommen aber **Schritt für Schritt je Produktgruppe**.",
                      "Beispiel **Smartphones und Tablets** (noch nach den älteren Ökodesign-Regeln): Für Geräte, die seit **20. Juni 2025** in der EU verkauft werden, gilt ein EU-Label mit Angaben zu Akku, Robustheit und einer **Reparierbarkeitsklasse A–E**. Ersatzteile müssen noch **sieben Jahre nach dem Verkaufsende** eines Modells erhältlich sein, Updates mindestens **fünf Jahre** danach. Der neue Rahmen soll solche Regeln auf viele weitere Warengruppen ausdehnen.",
                      "Ein **digitaler Produktpass** mit Infos zu Material und Reparatur wird ebenfalls schrittweise eingeführt – noch nicht für jede Ware."]),
              ("hint", "Daten und Gesetzesnummern musst du nicht auswendig können. Wichtig ist die Idee: Die EU verlangt zunehmend Produkte, die länger halten und reparierbar sind.")]},
  {"id": "stop1", "title": "Stopp – kannst du das?", "pill": "Buch S. 19–21", "blocks": [("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgabe 1", "aufgaben.html#name"),
 ]),

 # ---------------------------------------------------------------- Teil 2 · Ökobilanz
 ("teil2", "Gleiche Stunde · Buch S. 22–25", I.TEILNAME[2], [
  {"id": "oekobilanz", "title": I.ABSCHNITT_2, "pill": "Buch S. 22–24",
   "blocks": [("ul", ["Eine **Ökobilanz** untersucht die möglichen Umweltwirkungen eines Produkts oder einer Dienstleistung über den festgelegten Lebenszyklus. Dazu werden Stoff- und Energieflüsse erhoben und mit Umweltwirkungen verknüpft. "
                      "Die Methode hilft bei Entscheidungen – ein fertiges Urteil »umweltfreundlich« liefert sie nicht.",
                      "Zuerst steht die Frage: **Welche Leistung** soll erbracht werden? »Eine Flasche« ist als Vergleich zu ungenau. Bei uns lautet die **funktionale Einheit**: **1.000 Nutzungen einer dichten, hygienischen Ein-Liter-Trinkflasche**. "
                      "So werden kurzlebige und langlebige Produkte auf dieselbe Leistung bezogen.",
                      "Die **Systemgrenze** legt fest, was einbezogen wird – etwa Herstellung, Lieferung, Reinigung und Entsorgung. Ausschlüsse und Annahmen müssen sichtbar bleiben, denn andere Lebensdauern, Daten oder Strommischungen können das Ergebnis verändern.",
                      "Eine Angabe in **kg CO₂-Äquivalenten** beschreibt nur die **Klimawirkung**. Andere Umweltwirkungen sind z. B. **Wasserverbrauch, Rohstoffverbrauch, Versauerung, Überdüngung** oder **giftige Stoffe** – jede wird eigens gerechnet. Ein Produkt kann beim Klima besser und bei einer anderen Wirkung schlechter abschneiden. Ein gutes Urteil nennt daher Ergebnis, Annahmen und Grenzen."]),
              ("merke", "Fair vergleichen heißt: **dieselbe Leistung**, **offene Grenzen**, **gleiche Annahmen**.")]},
  {"id": "schritte", "title": "Vier Schritte einer Ökobilanz", "pill": "Buch S. 24",
   "blocks": [("img", "img/schritte.png", "Vier Kästen nebeneinander: 1 Ziel und Rahmen, 2 Sachbilanz, 3 Wirkungsabschätzung, 4 Auswertung; ein roter Pfeil führt vom vierten zurück zum ersten Schritt", "Die vier Schritte gehören zusammen und werden oft mehrmals durchlaufen."),
              ("table", [["Schritt", "Leitfrage", "Bei der Flasche"],
                         ["1 Ziel und Untersuchungsrahmen", "Was wollen wir entscheiden? Welche Leistung, welche Grenzen?", "Flaschen für 1.000 Nutzungen beschaffen"],
                         ["2 Sachbilanz", "Welche Stoffe und Energiemengen gehen hinein, was kommt heraus?", "Material, Herstellung, Transport, Reinigungswasser und -energie"],
                         ["3 Wirkungsabschätzung", "Zu welchen Umweltwirkungen tragen diese Flüsse bei – und wie stark?", "Treibhausgase in Klimawirkung umrechnen; andere Wirkungen getrennt"],
                         ["4 Auswertung", "Was ist belastbar? Wodurch ändert sich das Ergebnis?", "Lebensdauer und Reinigung prüfen, Entscheidung begrenzen"]]),
              ("hint", "Das Buch (S. 24) beschreibt vor allem Sachbilanz und Wirkungsbilanz. Ziel und Auswertung gehören genauso dazu – so steht es in den internationalen Normen für Ökobilanzen.")]},
  {"id": "wirkung", "title": "Sachbilanz und Wirkungsabschätzung", "pill": "Buch S. 24–25",
   "blocks": [("tiles", [("Sachbilanz (Input–Output)", ["**Hinein:** Rohstoffe, Hilfsstoffe, Energie", "**Heraus:** Produkte, Abfälle, Abwasser, Abgase, Abwärme, Lärm"]),
                         ("Wirkungsabschätzung", ["**Klassifizierung:** Jeder Fluss wird einer oder mehreren Umweltwirkungen zugeordnet.", "**Charakterisierung:** Sein Beitrag wird mit einem Faktor ausgerechnet, z. B. in kg CO₂-Äquivalenten."])]),
              ("img", "img/wirkungen.png", "In der Mitte die Sachbilanz, davon gehen Pfeile zu sechs Umweltwirkungen: Klimawirkung (unsere Rechnung), Wasser, Ressourcen, Versauerung, Überdüngung, giftige Stoffe", "Eine Sachbilanz – viele Umweltwirkungen. Unsere Flaschenrechnung erfasst nur eine davon."),
              ("ul", ["Ein **CO₂-Äquivalent** rechnet andere Treibhausgase wie Methan auf die Wirkung von CO₂ um. Wie stark Methan zählt, hängt vom betrachteten Zeitraum und der Bewertungsgrundlage ab – der Wert im Buch ist nicht mehr aktuell. Für unsere Rechnung brauchst du ihn nicht.",
                      "Wirkungen mit verschiedenen Einheiten darf man **nicht einfach zusammenzählen**. Wer sie trotzdem zu einer Note gewichtet, trifft eine Wertentscheidung und muss sie offenlegen."]),
              ("hint", "Die lange Tabelle der Wirkungskategorien auf Buch S. 25 ist zum Nachschlagen da – du musst sie nicht auswendig können.")]},
  {"id": "bilanzarten", "title": "Produkt-, Prozess- und Betriebsbilanz", "pill": "Buch S. 23",
   "blocks": [("tiles", [("Produktbilanz", ["ein Produkt über die festgelegten Abschnitte seines Lebenszyklus – gut für Vergleiche mit gleicher Leistung"]),
                         ("Prozessbilanz", ["ein einzelnes Verfahren, z. B. das Herstellen oder Reinigen der Flaschen – oft ein Teil einer größeren Untersuchung"]),
                         ("Betriebs- bzw. Standortbilanz", ["alle Stoff- und Energieströme eines Betriebs oder Standorts über einen Zeitraum, z. B. ein Jahr"])]),
              ("hint", "Nicht jede einfache Liste von Ein- und Ausgängen ist schon eine vollständige Ökobilanz nach Norm.")]},
  {"id": "rechnen", "title": "So rechnest du den Flaschenvergleich", "pill": "Buch S. 24",
   "blocks": [("table", [["Was?", "So rechnest du"]] + [[a, b] for a, b in I.RECHENWEG]),
              ("ul", ["**kg CO₂-Äq.** heißt Kilogramm CO₂-Äquivalente – die Einheit für die Klimawirkung.",
                      "**Beispiel mit anderen Zahlen:** Flasche C hält 250 Nutzungen, kostet 5 € und verursacht in der Herstellung 2 kg, am Nutzungsende 0,25 kg CO₂-Äq.; Reinigung wie bei A und B.",
                      "Flaschen: 1.000 : 250 = **4** · Klima: 4 × (2 + 0,25) + 1.000 × 0,01 = 9 + 10 = **19 kg CO₂-Äq.** · Kosten: 4 × 5 € + 1.000 × 0,02 € = 20 € + 20 € = **40 €**"]),
              ("hint", "Achte auf die Bezugsgröße: Herstellung und Endbehandlung gelten **pro Flasche**, Reinigung **pro Nutzung**.")]},
  {"id": "stop2", "title": "Stopp – kannst du das?", "pill": "Buch S. 22–25", "blocks": [("reveal", I.STOPPFRAGEN[2])]},
  ("jetzt", "Jetzt: Aufgaben 2 und 3", "aufgaben.html#card_a2"),
 ]),
]

SCHNELLE = [
 {"id": "partnercheck", "title": "Partnercheck – Karten für die Wiederholung", "pill": "Buch S. 19–25",
  "blocks": [("hint", "Zu zweit vor dem Test: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken (Aufgabe 4)."), ("karten", I.PARTNERKARTEN)]},
 {"id": "vernichtung", "title": "Neu seit Juli 2026: Ware nicht einfach vernichten", "pill": "EU-Ökodesign-Verordnung",
  "blocks": [("ul", ["Der neue EU-Rahmen regelt nicht nur die Gestaltung. Seit Juli 2026 dürfen **große Unternehmen** in der EU unverkaufte **Kleidung, Kleidungszubehör und Schuhe** grundsätzlich nicht mehr vernichten; für mittlere Unternehmen soll das ab 2030 gelten, kleine sind ausgenommen.",
                     "Recherche-Frage: Was müssen Händler jetzt mit unverkaufter Ware tun – und was hat das mit Ökodesign zu tun?"]),
             ("hint", "Quelle zum Start: Zusammenfassung der EU-Ökodesign-Verordnung (EU) 2024/1781, z. B. auf den Seiten der EU-Kommission.")]},
 {"id": "offen", "title": "Offene Fragen: Wo Ökobilanzen unsicher bleiben", "pill": "Ausblick",
  "blocks": [("ul", ["**Wie lange hält ein Produkt wirklich?** Hersteller und Ökobilanzen nehmen eine Lebensdauer an – tatsächlich hängt sie von Pflege, Nutzung und Zufall ab. Unsere Aufgabe 6 zeigt, wie stark diese Annahme das Ergebnis verschiebt.",
                     "**Wie wiegt man verschiedene Umweltwirkungen gegeneinander auf?** Ist weniger Klimawirkung mehr wert als weniger Wasserverbrauch? Darauf gibt es keine rein naturwissenschaftliche Antwort – es braucht offengelegte Werturteile."])]},
 ("jetzt", "Zu den Zusatzaufgaben 4–9", "aufgaben.html#card_a4"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Ökodesign", "teil2": "Teil 2 · Ökobilanz",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

if __name__ == "__main__":
    import re
    for pid, _, _, items in PARTS:
        for it in items:
            if isinstance(it, dict) and it["id"] in ("oekodesign", "oekobilanz"):
                txt = " ".join(x for b in it["blocks"] if b[0] == "ul" for x in b[1])
                print(it["id"], len(re.findall(r"\w+", txt)), "Wörter")
