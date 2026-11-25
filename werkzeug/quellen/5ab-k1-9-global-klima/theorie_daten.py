"""Theorie-Seite TÖW 5AB K1.9 Globalisierung, KI und Klima: Theorie-Karten, Teile und Abschnitte.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufe 2 im Arbeitsblatt (Theorie-Karte) und die Erklär-Folien der Präsentation.
Block-Arten wie in der Vorlage (4AB Akustik): tiles, ul, ol, merke, hint, table, reveal, img, buch, karte, gemeinsam, sim, extern.
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt aktuelle Fälle."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "abdruck": "1 Fußabdruck", "rucksack": "2 Rucksack", "oekosysteme": "3 Arten", "ki": "4 KI", "kronstorf": "5 Kronstorf",
          "treibhaus": "6 Treibhaus", "konferenzen": "7 Konferenzen", "handel": "8 Handel", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

KARTEN = {
 "k1": {"titel": "Der ökologische Fußabdruck", "teil": "abdruck", "buch": "Buch S. 40", "bild": "img/fussabdruck.svg",
        "alt": "Zwei Balken für ein Jahr: Das Naturbudget der Erde reicht bis 30. Juli; würden alle so leben wie wir in Österreich, nur bis 2. April. Danach leben wir auf Pump.",
        "satz": ["Der **ökologische Fußabdruck** zählt die **Fläche**, die für dein Essen, Wohnen, Fahren und Einkaufen nötig ist – plus den Wald, der dein **CO₂** aufnehmen müsste. Einheit: **globale Hektar (gha)**.",
                 "Am **Overshoot Day** ist das Naturbudget der Erde für das Jahr verbraucht: 2026 am **30. Juli**. Würden alle so leben wie wir in Österreich, wäre es schon am **2. April** so weit.",
                 "Wie viele Erden? **365 : Tag des Overshoot Day** – für Österreich 365 : 92 ≈ **4 Erden**."],
        "formeln": [("Erden", "365 : Tag des Overshoot Day", ""), ("Österreich 2026", "Tag 92 → ≈ 4 Erden", ""), ("Welt 2026", "Tag 211 → ≈ 1,7 Erden", "")],
        "link": "theorie.html#abdruck"},
 "k2": {"titel": "Rucksack und CO₂-Fußabdruck", "teil": "rucksack", "buch": "Buch S. 40", "bild": "img/rucksack.svg",
        "alt": "Fünf Stationen eines Handys füllen einen Rucksack: Bergbau, Fabrik, Transport, Nutzung, Entsorgung. Am Ende rund 75 kg, das Handy wiegt 0,1 kg.",
        "satz": ["Der **ökologische Rucksack** ist alles Material, das für **ein Produkt** bewegt wird – von der Mine bis zur Entsorgung, in **Kilogramm**. Ein Handy (0,1 kg) trägt rund **75 kg**.",
                 "Der **CO₂-Fußabdruck** zählt nur **Treibhausgase**, umgerechnet in **CO₂-Äquivalente** (kg oder t).",
                 "Merke: Fußabdruck = **Fläche**, Rucksack = **Material**, CO₂-Fußabdruck = **Gase**."],
        "formeln": [("gha", "Fußabdruck: Fläche", ""), ("kg", "Rucksack: Material", ""), ("kg CO₂e", "CO₂-Fußabdruck: Treibhausgase", "")],
        "link": "theorie.html#rucksack"},
 "k3": {"titel": "Arten und Krankheiten reisen mit", "teil": "oekosysteme", "buch": "Buch S. 41–42", "bild": "img/oekosysteme.svg",
        "alt": "Ein Schiff fährt von Asien nach Österreich, eine Tigermücke reist mit.",
        "satz": ["Mit Waren und Reisenden kommen **fremde Arten** mit: eingewanderte Pflanzen heißen **Neophyten**, Tiere **Neozoen**.",
                 "Die **Asiatische Tigermücke** wurde 2012 erstmals in Österreich gefunden und ist seit 2022 in **allen Bundesländern** nachgewiesen.",
                 "Folge: Ökosysteme werden weltweit **ähnlicher**, und **Krankheitserreger** können sich schneller ausbreiten."],
        "formeln": [], "link": "theorie.html#oekosysteme"},
 "k4": {"titel": "Wo wohnt die KI?", "teil": "ki", "buch": "Buch S. 97", "bild": "img/rechenzentrum.svg",
        "alt": "Strom fließt in Server mit KI-Chips, wird zu Wärme, Kühlwasser trägt sie in den Fluss.",
        "satz": ["Jede KI-Antwort wird in einem **Rechenzentrum** berechnet. Dort wird fast der ganze Strom zu **Wärme** – sie muss mit Luft oder **Wasser** abgeführt werden.",
                 "Google nennt **0,24 Wh** pro Textfrage, OpenAI **0,34 Wh** – das sind **Eigenangaben**. Google rechnet Kühlung und Leerlauf mit ein, das **Training** der Modelle nicht.",
                 "Einzelne Fragen werden sparsamer, aber es gibt **immer mehr** davon: Der Verbrauch steigt trotzdem (**Rebound-Effekt**)."],
        "formeln": [("1 kWh", "= 1000 Wh", ""), ("1 TWh", "= 1 000 000 000 kWh", ""), ("Strom pro Jahr", "Leistung · Stunden (MW · 8760 h)", "MWh")],
        "link": "theorie.html#ki"},
 "k5": {"titel": "Der Fall Kronstorf", "teil": "kronstorf", "buch": "Buch S. 40", "bild": "img/rechenzentrum.svg",
        "alt": "Strom, Server und Kühlung mit den Zahlen für Kronstorf: 150 MW, 1,31 TWh, 5,8 Millionen Liter Kühlwasser pro Tag.",
        "satz": ["Google baut seit April 2026 in **Kronstorf** (Oberösterreich) sein erstes Rechenzentrum in Österreich. Stufe 1: **150 MW**, bis **1,31 TWh** pro Jahr – so viel wie rund **375 000 Haushalte**.",
                 "Bis zu **5,8 Millionen Liter** erwärmtes Kühlwasser pro Tag dürfen in die **Enns** (höchstens 30 °C).",
                 "Eine **UVP** war nicht nötig: Rechenzentren sind im Gesetz keine eigene Kategorie. Umweltorganisationen fordern eine **UVP-Pflicht**."],
        "formeln": [("150 MW · 8760 h", "≈ 1 314 000 MWh ≈ 1,31 TWh", ""), ("1,31 TWh : 375 000", "≈ 3 500 kWh pro Haushalt", "")],
        "link": "theorie.html#kronstorf"},
 "k6": {"titel": "Der Treibhauseffekt", "teil": "treibhaus", "buch": "Buch S. 71", "bild": "img/treibhaus.svg",
        "alt": "Sonnenlicht kommt durch die Atmosphäre zum Boden, der warme Boden strahlt Wärme ab, Treibhausgase halten einen Teil zurück.",
        "satz": ["Sonnenlicht erwärmt den Boden. Der Boden strahlt **Wärme** ab. **Treibhausgase** wie CO₂, Methan und Wasserdampf halten einen Teil davon zurück.",
                 "Der **natürliche** Treibhauseffekt macht die Erde bewohnbar. Durch Kohle, Öl und Gas **verstärken** wir ihn – das ist der **menschengemachte** Treibhauseffekt.",
                 "Mehr dazu (Klimaforschung, Klima im Wandel) kommt im Jänner."],
        "formeln": [], "link": "theorie.html#treibhaus"},
 "k7": {"titel": "Klimakonferenzen", "teil": "konferenzen", "buch": "Buch S. 73–74", "bild": "img/zeitleiste.svg",
        "alt": "Zeitleiste: 1992 Rio (Klimarahmenkonvention), 1995 erste COP in Berlin, 1997 Kyoto, 2015 Paris, 2023 Dubai, 2026 Antalya ohne Abschlusspapier.",
        "satz": ["1992 wurde in Rio die **Klimarahmenkonvention** beschlossen; seit 1995 (Berlin) treffen sich die Staaten fast jedes Jahr zur **Weltklimakonferenz (COP)**. In **Paris 2015** vereinbarten sie: Erwärmung **deutlich unter 2 °C**, möglichst **1,5 °C**.",
                 "Beschlüsse brauchen den Konsens aller Staaten: Ein formeller Widerspruch reicht, um sie zu stoppen – darum sind sie oft schwach.",
                 "Die **COP31** in Antalya endete am **22. November 2026** ohne Abschlusspapier: Die EU legte Widerspruch ein, weil **Kohle, Öl und Gas** im Text nicht einmal genannt wurden."],
        "formeln": [], "link": "theorie.html#konferenzen"},
 "k8": {"titel": "Handelsabkommen: Mercosur", "teil": "handel", "buch": "Buch S. 40–41", "bild": "img/handel.svg",
        "alt": "Von der EU fließen Maschinen und Autos zum Mercosur, von dort Rindfleisch, Geflügel und Zucker in die EU; darunter Chancen und Risiken.",
        "satz": ["Ein **Freihandelsabkommen** senkt Zölle. Das Abkommen mit dem **Mercosur** gilt für Argentinien, Brasilien, Paraguay und Uruguay; der Handelsteil gilt seit **1. Mai 2026** vorläufig.",
                 "**Österreich stimmte dagegen**, wurde aber überstimmt. Nach einer Übergangszeit dürfen sie u. a. bis zu **99 000 t Rindfleisch** zu **7,5 % Zoll** liefern – gut 1 % des EU-Verbrauchs.",
                 "Chancen: **Exporte**, Jobs, Bindung an das **Pariser Klimaabkommen**. Risiken: **Regenwald**, lange Transporte, Druck auf **heimische Bauern**. Gute Urteile wägen ab."],
        "formeln": [("Anteil in %", "Teil : Ganzes · 100", "%"), ("99 000 t : 8 000 000 t · 100", "≈ 1,24 %", "")],
        "link": "theorie.html#handel"},
 "k9": {"titel": "Alles auf einen Blick", "teil": "kurz", "buch": "Buch S. 39–44, 71–75", "bild": "img/ueberblick.svg",
        "alt": "Kette: Konsum, Abdruck, Rechenzentren, Klima, Abkommen.",
        "satz": ["**Konsum → Abdruck → Rechenzentren → Klima → Abkommen**: Das ist der rote Faden der Einheit.",
                 "Rechnen: **Erden = 365 : Tag**, **Prozent = Teil : Ganzes · 100**, **1 TWh = 1 Milliarde kWh**.",
                 "Prüfen: **Wer sagt das?** Firmen, Interessenvertretungen und Ministerien haben verschiedene Interessen."],
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
 {"id": "s0a", "title": "Ein Planet reicht nicht", "pill": "Buch S. 39",
  "blocks": [("img", "img/ueberblick.svg", KARTEN["k9"]["alt"], "Der rote Faden: vom eigenen Konsum bis zu den Abkommen zwischen Staaten."),
             ("ul", ["**Das Wichtigste vorab:** Alles, was du kaufst, isst und nutzt, braucht Fläche, Rohstoffe und Energie – auch das, was »digital« aussieht. Ob wir das in den Griff bekommen, entscheiden am Ende Staaten gemeinsam.",
                     "**Wozu?** Du weißt danach, wie groß dein eigener Abdruck ist und wo er am größten ist. Du kannst bei Diskussionen über Rechenzentren, Klimagipfel und Handelsabkommen mitreden – mit Zahlen statt Schlagworten.",
                     "**Bezug zum Dienst:** Lieferketten, Versorgung mit Lebensmitteln und Energie, Katastrophenhilfe nach Unwettern und sichere Daten sind Themen der Sicherheitspolitik."]),
             ("hint", "Du arbeitest im Arbeitsblatt – diese Seite ist zum Nachschlagen. Die Teile sind nach Stunden geordnet.")]},
 {"id": "s0b", "title": "Science oder Fiction? »Die Cloud schwebt irgendwo«", "pill": "Buch S. 97",
  "blocks": [("tiles", [("Was viele glauben", ["Fotos, Chats und KI-Antworten liegen »in der Cloud« – irgendwo da oben, ohne Gewicht."]),
                        ("In Wirklichkeit", ["Die Cloud sind **Hallen voller Server** auf festem Boden. Sie brauchen Strom, Kühlwasser und Fläche – eine davon entsteht gerade in **Kronstorf** an der Enns."])]),
             ("ul", ["**Offene Frage der Forschung:** Wie viel Strom KI in Zukunft wirklich braucht, weiß niemand genau. Die Internationale Energieagentur rechnet damit, dass sich der Strombedarf aller Rechenzentren bis 2030 ungefähr **verdoppelt** – auf etwa so viel, wie heute ganz Japan verbraucht."]),
             ("tiles", [("Globalisierung in drei Sätzen", ["Länder handeln, reisen und kommunizieren immer enger miteinander. Waren, Daten und Menschen sind in Stunden um die Welt. Auch die Folgen – Abgase, Müll, fremde Arten – kennen keine Grenzen (Buch S. 39)."])])]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("abdruck", "Teil 1 · Buch S. 40 · Stunde 1", "Der ökologische Fußabdruck", [
  {"id": "abdruck", "title": "Wie viel Erde brauchst du?", "pill": "Buch S. 40",
   "blocks": [("buch", "Lies im **Buch S. 40** den Abschnitt **»Ökologischer Fußabdruck und ökologischer Rucksack«** (2 min). Markiere, in welcher Einheit der Fußabdruck gemessen wird."),
              kartenblock("k1"),
              ("sim", "overshoot"),
              ("ul", ["Der Fußabdruck rechnet alles in **Fläche** um: Acker für Brot und Futter, Weide für Rinder, Wald für Holz und Papier, Meer für Fisch, Bauland für Häuser und Straßen – und Wald, der das CO₂ aus Heizung, Verkehr und Strom aufnehmen müsste.",
                      "**Globale Hektar** machen Flächen vergleichbar: Ein Hektar fruchtbarer Acker zählt mehr als ein Hektar karge Steppe.",
                      "Dem steht die **Biokapazität** gegenüber: Was die Erde pro Jahr nachwachsen lässt. Braucht die Menschheit mehr, lebt sie »auf Pump« – Wälder schrumpfen, Fischbestände sinken, CO₂ reichert sich an.",
                      "**Vorsicht beim Vergleichen:** Der weltweite Overshoot Day lag 2026 sechs Tage später als 2025 – vor allem, weil die Berechnung mit neuen Daten verbessert wurde, nicht weil wir weniger verbraucht hätten."]),
              ("reveal", I.STOPPFRAGEN["abdruck"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2", "aufgaben.html#card_a1")]),

 ("rucksack", "Teil 2 · Buch S. 40 · Stunde 1", "Rucksack und CO₂-Fußabdruck", [
  {"id": "rucksack", "title": "Was ein Handy wirklich wiegt", "pill": "Buch S. 40",
   "blocks": [kartenblock("k2"),
              ("ul", ["Für **10 g Kupfer** in einem Handy muss man rund **3,5 kg** Gestein abbauen und verarbeiten. Ein Goldring wiegt 5 g – sein Rucksack rund **2 Tonnen**.",
                      "Darum lohnt sich **länger nutzen, reparieren, weitergeben**: Der Rucksack ist bei der Herstellung schon gepackt. Jedes Jahr mehr Nutzung verteilt ihn auf mehr Zeit.",
                      "Der **CO₂-Fußabdruck** zählt neben CO₂ auch Methan (z. B. von Rindern) und Lachgas – umgerechnet in die Wirkung von CO₂ (**CO₂-Äquivalent**)."]),
              ("tiles", [("Wer hat's erfunden?", ["Bekannt wurde der Begriff »CO₂-Fußabdruck« durch eine **Werbekampagne des Ölkonzerns BP** ab 2004, wenig später kam ein Online-Rechner für Privatleute (WBUR, 2023)."]),
                         ("Was heißt das?", ["Kritiker sagen: Der Blick wandert vom Konzern zu dir. Trotzdem lohnt eigenes Handeln. Am meisten bewegen aber Politik, Energieversorger und Firmen."])]),
              ("reveal", I.STOPPFRAGEN["rucksack"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3 (mit der Hand)", "aufgaben.html#card_a2")]),

 ("oekosysteme", "Teil 3 · Buch S. 41–42 · Stunde 1", "Arten und Krankheiten reisen mit", [
  {"id": "oekosysteme", "title": "Blinde Passagiere", "pill": "Buch S. 41–42",
   "blocks": [kartenblock("k3"),
              ("ul", ["Das **Drüsige Springkraut** stammt aus dem Himalaya. Es wurde als Gartenpflanze eingeführt und verdrängt heute an Bächen heimische Pflanzen (Buch S. 41).",
                      "Die **Tigermücke** reist als Ei oder Larve in kleinsten Wasserresten mit. In Teilen von **Wien, Graz und Linz** überwintert sie schon. Sie kann Krankheiten wie Dengue übertragen – in Österreich gab es bisher keinen gesicherten Fall, der durch sie hier verursacht wurde.",
                      "**Gesundheit:** Wasser in Untersetzern, Regentonnen und Gießkannen regelmäßig ausleeren – dann findet sie keine Brutplätze."]),
              ("reveal", I.STOPPFRAGEN["oekosysteme"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2 h) und i)", "aufgaben.html#card_a1")]),

 ("ki", "Teil 4 · Buch S. 97 · Stunde 2", "Wo wohnt die KI?", [
  {"id": "ki", "title": "Strom rein, Wärme raus", "pill": "Buch S. 97",
   "blocks": [("buch", "Lies im **Buch S. 97** den Abschnitt **»Bewusster Umgang mit IT«** (2 min). Was davon gilt auch für KI?"),
              kartenblock("k4"),
              ("sim", "ki"),
              ("ul", ["Ein **Rechenzentrum** ist eine Halle voller Server. Sie laufen rund um die Uhr. Fast die ganze elektrische Energie wird in den Chips zu **Wärme**.",
                      "Gekühlt wird mit Luft oder **Wasser**. Wird mit Verdunstung gekühlt, spart das Strom, kostet aber viel Wasser – ein Zielkonflikt.",
                      "Die **Hardware** wird oft nach 3 bis 5 Jahren ersetzt. So wächst auch der Berg an Elektroschrott.",
                      "**Abwärme** kann Häuser heizen, wenn ein Fernwärmenetz in der Nähe ist. Österreichs Strom stammt zu rund 80 % aus erneuerbaren Quellen, vor allem aus Wasserkraft.",
                      "**Quellenkritik:** Die Werte pro Frage stammen von den Firmen selbst. Unabhängig geprüft sind sie nicht, und das Training großer Modelle fehlt."]),
              ("reveal", I.STOPPFRAGEN["ki"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 4", "aufgaben.html#card_a3")]),

 ("kronstorf", "Teil 5 · ORF 2026 · Stunde 2", "Der Fall Kronstorf", [
  {"id": "kronstorf", "title": "Ein Rechenzentrum an der Enns", "pill": "Stunde 2",
   "blocks": [kartenblock("k5"),
              ("sim", "rz"),
              ("ul", ["Google kaufte das Grundstück in Kronstorf schon vor 18 Jahren. Im April 2026 begann der Bau auf rund **50 Hektar**.",
                      "**Strom:** Stufe 1 braucht bis 1,31 TWh im Jahr. Stufe 2 (bis 500 MW) könnte noch einmal bis zu 4,4 TWh brauchen – laut ORF würde der Strombedarf Oberösterreichs dadurch um rund ein Drittel steigen. Die Regulierungsbehörde E-Control sagt, das Netz hält das aus.",
                      "**Wasser:** Das Kühlwasser kommt aus Brunnen nahe der Enns. Die Genehmigung erlaubt höchstens 99 Liter pro Sekunde (Spitze), 5,8 Millionen Liter am Tag und 30 °C. Google sagt, laut Gutachten seien die Folgen für die Enns vernachlässigbar, und will mit dem Landesfischereiverband Projekte für die Enns unterstützen.",
                      "**Streit um die UVP:** Die Grünen wollen die »UVP-Lücke« schließen, die SPÖ will das Thema in die neue UVP-Novelle einbringen. Umweltorganisationen wie das Ökobüro schlagen eine UVP-Pflicht ab 50 MW vor (ab 20 MW, wenn Kühlwasser aus Gewässern oder Grundwasser kommt). Die ÖVP hält eine pauschale Pflicht für den falschen Weg, weil Raumordnung, Bau- und Wasserrecht schon prüfen. Auch der Umweltrechtler Wilhelm Bergthaler (Uni Linz) sieht eine UVP-Reform kritisch und will lieber Vorgaben über die Flächenwidmung.",
                      "Über 200 Menschen demonstrierten an der Baustelle."]),
              ("gemeinsam", "GRUPPENARBEIT in Stunde 2: Ihr spielt eine Sondersitzung des Gemeinderats mit Gästen. Er beschließt eine Forderung an den Nationalrat (Aufgabe 5)."),
              ("reveal", I.STOPPFRAGEN["kronstorf"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 5", "aufgaben.html#card_a4")]),

 ("treibhaus", "Teil 6 · Buch S. 71 · Stunde 3", "Der Treibhauseffekt – kurz", [
  {"id": "treibhaus", "title": "Warum CO₂ wärmt", "pill": "Buch S. 71",
   "blocks": [kartenblock("k6"),
              ("tiles", [("Natürlicher Treibhauseffekt", ["Wasserdampf, CO₂ und andere Gase gab es immer. Ohne sie wäre es auf der Erde eisig kalt."]),
                         ("Menschgemachter Treibhauseffekt", ["Kohle, Öl und Gas setzen zusätzliches CO₂ frei, Rinder und Reisfelder Methan. Mehr Wärme bleibt da – die Erde erwärmt sich."])]),
              ("extern", "Treibhauseffekt (PhET)", "https://phet.colorado.edu/de/simulations/greenhouse-effect",
               "Stell die Menge der Treibhausgase ein und schau, wie sich die Temperatur ändert. Füge Wolken hinzu. Dazu gibt es Zusatz 10.",
               "PhET, University of Colorado Boulder · Deutsch · PhET Interactive Simulations · läuft im Browser · öffnet in einem neuen Tab"),
              ("hint", "Klimaforschung und Klima im Wandel der Zeit (Buch S. 70, 72) kommen im Jänner dran."),
              ("reveal", I.STOPPFRAGEN["treibhaus"])]}]),

 ("konferenzen", "Teil 7 · Buch S. 73–75 · Stunde 3", "Klimakonferenzen bis zur COP31", [
  {"id": "konferenzen", "title": "Fast 200 Staaten, ein Text", "pill": "Buch S. 73–75",
   "blocks": [("buch", "Schau dir im **Buch S. 73–74** die Zeitleiste der Klimakonferenzen an (1 min)."),
              kartenblock("k7"),
              ("ul", ["Die **COP31** fand vom 9. bis 20. November 2026 in **Antalya** (Türkei) statt. Die Türkei stellte den Präsidenten, **Australien** leitete die Verhandlungen.",
                      "Sie dauerte mehr als 49 Stunden länger als geplant – so lange wie keine Klimakonferenz vorher – und endete am 22. November ohne gemeinsames Papier.",
                      "Der Entwurf verwies nur allgemein auf den Beschluss von **Dubai 2023** (Abkehr von fossilen Energien). Die EU und weitere Staaten lehnten ab.",
                      "**Warum so schwer?** Ölstaaten verdienen an Öl und Gas, arme Länder wollen Geld für Anpassung, reiche Länder haben den Großteil des CO₂ ausgestoßen (Buch S. 75).",
                      "**Sicherheit:** Hitze, Dürre und Hochwasser nehmen zu. Das Bundesheer hilft bei Assistenzeinsätzen nach Unwettern – Klimaschutz ist auch Katastrophenvorsorge."]),
              ("gemeinsam", "MINI-KLIMAGIPFEL in Stunde 3: Eure Gruppen vertreten Staaten mit verschiedenen Interessen und versuchen, sich auf einen Satz zu einigen (Buch S. 76, Buch-Aufgabe 11)."),
              ("reveal", I.STOPPFRAGEN["konferenzen"])]}]),

 ("handel", "Teil 8 · Buch S. 40–41 · Stunde 3", "Handelsabkommen: Mercosur", [
  {"id": "handel", "title": "Billiger handeln – auf wessen Kosten?", "pill": "Buch S. 40–41",
   "blocks": [("buch", "Lies im **Buch S. 40–41** den Abschnitt **»Internationale Abkommen«** (GATT, WTO) und die Kritik der NGOs (2 min)."),
              kartenblock("k8"),
              ("ul", ["Unterzeichnet wurde das Abkommen am **17. Jänner 2026** in Paraguay. Seit **1. Mai 2026** gilt der Handelsteil vorläufig.",
                      "Im Rat der EU stimmten **Frankreich, Polen, Österreich, Ungarn und Irland dagegen** – die Mehrheit war dafür. Das EU-Parlament ließ Teile des Abkommens vom Europäischen Gerichtshof prüfen.",
                      "**Schutzklauseln:** Steigen Importe zu stark, kann die EU Zollvorteile vorübergehend aussetzen. Viele Supermärkte in Österreich haben angekündigt, beim Frischfleisch bei österreichischer Herkunft zu bleiben.",
                      "**Quellenkritik:** Die Zahl »gut 1 % des EU-Verbrauchs« stammt aus einem Faktenblatt der Wirtschaftskammer, die für das Abkommen ist. Bauernvertreter rechnen anders: Es gehe um die teuersten Teilstücke."]),
              ("reveal", I.STOPPFRAGEN["handel"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 6 und 7", "aufgaben.html#card_a5")]),
]

# Teil → Stunde (eine Quelle für Trennbalken, Übersicht, Fahrplan, Präsentation)
TEIL_STUNDE = {"abdruck": 1, "rucksack": 1, "oekosysteme": 1, "ki": 2, "kronstorf": 2, "treibhaus": 3, "konferenzen": 3, "handel": 3}

SCHNELLE = [
 {"id": "schnell1", "title": "Was du selbst tun kannst", "pill": "OPTIONAL",
  "blocks": [("ul", ["**Essen:** Weniger Fleisch verkleinert den Fußabdruck am stärksten – Rinder brauchen viel Fläche und erzeugen Methan.",
                     "**Handy:** Ein Jahr länger nutzen spart mehr als jede Strom-Spar-App. Der Rucksack ist bei der Herstellung schon gepackt.",
                     "**KI:** Fragen bündeln statt zehnmal neu fragen. Für einfache Fakten reicht oft eine normale Suche.",
                     "**Wege:** Rad oder Öffis statt Elterntaxi zum Training."])]},
 {"id": "schnell2", "title": "Für Neugierige: Wie viel Strom braucht KI 2030?", "pill": "OPTIONAL",
  "blocks": [("ul", ["Die Internationale Energieagentur rechnet für 2030 mit rund 945 TWh für alle Rechenzentren der Welt – etwa so viel, wie Japan heute verbraucht.",
                     "Das Öko-Institut erwartet, dass der Kühlwasserbedarf von Rechenzentren bis 2030 auf fast das Vierfache steigt.",
                     "Seit 2024 müssen große Rechenzentren in der EU jedes Jahr melden, wie viel Strom und Wasser sie brauchen und ob sie Abwärme nutzen."]),
             ("hint", "Zusatzaufgaben und Zusatztexte zählen nicht zum Pflichtfortschritt und sind keine Hausübung.")]},
 {"id": "mehr", "title": "Noch mehr wissen: Wer hat den CO₂-Fußabdruck bekannt gemacht?", "pill": "OPTIONAL",
  "blocks": [("hint", "Quelle: Radiosendung WBUR »On Point« (Boston, USA), 19.12.2023, Gast: Geoffrey Supran, Universität Miami – auf Englisch. Zum Thema passt Teil 2 und Zusatz 8 im Arbeitsblatt."),
             ("ul", ["Ab 2004 machte eine **Werbekampagne des Ölkonzerns BP** den Begriff **»CO₂-Fußabdruck«** bekannt. Wenig später gab es auf der BP-Website einen **Online-Rechner**.",
                     "Nach Supran gab BP für das neue Image (»**Beyond Petroleum**«) über **100 Millionen Dollar im Jahr** aus. Der Blick wandert vom Konzern zu den Einzelnen.",
                     "Supran sagt selbst: **Interne BP-Papiere, die den Plan beweisen, wurden bisher nicht gefunden.** Er stützt sich auf Unterlagen der Werbeagenturen. Er rät trotzdem, selbst zu handeln und **zusätzlich Politik und Firmen in die Pflicht zu nehmen**."]),
             ("reveal", [("Frage 1: Wie viele Menschen berechneten laut Supran im ersten Jahr ihren Fußabdruck? (A: fast eine Viertelmillion · B: etwa 500 · C: über 10 Millionen)",
                          "A – fast eine Viertelmillion. Die Kampagne hat also viele Menschen erreicht."),
                         ("Frage 2: Was fehlt laut Supran noch? (A: ein internes BP-Papier, das den Plan beweist · B: ein Beleg, dass es die Kampagne gab · C: ein Beleg, dass eigenes Handeln sinnlos ist)",
                          "A – er sucht noch nach internen Papieren. Die Kampagne ist belegt, und dass Handeln sinnlos sei, sagt er nicht."),
                         ("Quellenkritik: Wer hat ein Interesse an der Geschichte vom Fußabdruck – und wie prüfst du sie?",
                          "BP hatte ein Interesse an der Werbung, Forscher haben eines an ihrer Studie. Prüfen: Wer sagt es, mit welchem Beleg, und stimmen mehrere unabhängige Quellen überein?")]),
             ("hint", "Brücke zu Teil 2: Eigenes Handeln lohnt sich – Politik und Firmen bewegen am meisten. Zusatzaufgaben und Zusatztexte zählen nicht zum Pflichtfortschritt und sind keine Hausübung.")]},
]
