"""Theorie-Seite K1.5 Säuren und Basen: Theorie-Karten, Teile und Abschnitte.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufe 2 im Arbeitsblatt (Theorie-Karte) und später die KURZ-KLÄREN-Folien der Unterrichts-PPP.
Block-Arten: tiles, ul, ol, merke, hint, table, reveal, img (Datei, Alt, Unterschrift), buch, karte, gemeinsam, sim (pH-Schieber), demo (ID, Text), versuch (ID, Text, Anker).
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py, SVG). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "saeuren": "1 Säuren", "basen": "2 Laugen", "protolyse": "3 Pingpong", "ph": "4 pH-Wert", "messen": "5 Messen",
          "neutral": "6 Neutralisation", "blut": "7 Blut", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

KARTEN = {
 "k1": {"titel": "Säuren geben Protonen ab", "teil": "saeuren", "buch": "Buch S. 54–55", "bild": "img/saeure.svg",
        "alt": "Links ein HCl-Molekül und ein Wassermolekül. Ein kleines rotes H-plus wandert vom HCl zum Wasser. Rechts bleiben ein Chlorid-Ion und ein Oxonium-Ion H3O+ übrig. Darunter Alltagsbeispiele: Zitrone, Cola, Mineralwasser, Magen.",
        "satz": ["Eine **Säure** gibt in Wasser ein **H⁺-Ion** ab – das ist nur ein **Proton**. Es hängt sich sofort an ein Wassermolekül: Es entsteht **H₃O⁺** (Oxonium-Ion).",
                 "Je mehr H₃O⁺ in einer Lösung schwimmen, desto **saurer** ist sie. Übrig bleibt das **Säurerest-Ion**, z. B. Cl⁻ aus Salzsäure.",
                 "Ein **Indikator** macht Säuren sichtbar: **Lackmus wird rot**, **Rotkrautsaft rot bis rosa**."],
        "formeln": [("H⁺", "Proton (Wasserstoff-Ion)", ""), ("H₃O⁺", "Oxonium-Ion – macht sauer", ""), ("HCl + H₂O → H₃O⁺ + Cl⁻", "Salzsäure in Wasser", "")],
        "link": "theorie.html#saeuren"},
 "k2": {"titel": "Basen und Laugen", "teil": "basen", "buch": "Buch S. 56–57", "bild": "img/lauge.svg",
        "alt": "Ein Natriumhydroxid-Kristall löst sich in Wasser: Natrium-Ionen und blaue Hydroxid-Ionen OH- schwimmen getrennt. Daneben drei Laugen aus dem Alltag: Rohrreiniger, Laugenbrezel, nasser Beton.",
        "satz": ["**Basen** bilden in Wasser **OH⁻-Ionen** (Hydroxid-Ionen). Ihre Lösung heißt **Lauge** – z. B. Natronlauge aus Natriumhydroxid.",
                 "Laugen fühlen sich seifig an, weil sie **Fett und Eiweiß** der Haut angreifen. Im **Auge** sind sie besonders gefährlich: Sie dringen tief ein.",
                 "Darum: **Schutzbrille**, und bei einem Spritzer sofort **lange mit Wasser spülen**. Beim Verdünnen gilt: **Erst das Wasser, dann die Säure.**"],
        "formeln": [("OH⁻", "Hydroxid-Ion – macht basisch", ""), ("NaOH → Na⁺ + OH⁻", "Natriumhydroxid in Wasser", ""), ("Lackmus", "wird bei Basen blau", "")],
        "link": "theorie.html#basen"},
 "k3": {"titel": "Protonen-Pingpong (Brønsted)", "teil": "protolyse", "buch": "Buch S. 58–59", "bild": "img/protolyse.svg",
        "alt": "Zwei Zeilen. Oben gibt HCl ein Proton an H2O ab: es entstehen Cl- und H3O+. Unten gibt H2O ein Proton an NH3 ab: es entstehen OH- und NH4+. Das Proton ist ein roter Ball mit Pfeil.",
        "satz": ["Bei jeder Säure-Base-Reaktion wandert **ein Proton** von einem Teilchen zum anderen. Wer **abgibt**, ist die **Säure**; wer **aufnimmt**, ist die **Base**.",
                 "Trick: Zähle die H links und rechts. **Ein H weniger** = hat abgegeben (Säure). **Ein H mehr** = hat aufgenommen (Base).",
                 "**Wasser** kann beides: Bei HCl nimmt es auf, bei NH₃ gibt es ab. So ein Teilchen heißt **Ampholyt**."],
        "formeln": [("HCl + H₂O → Cl⁻ + H₃O⁺", "Säure HCl · Base H₂O", ""), ("NH₃ + H₂O → NH₄⁺ + OH⁻", "Säure H₂O · Base NH₃", "")],
        "link": "theorie.html#protolyse"},
 "k4": {"titel": "Die pH-Skala", "teil": "ph", "buch": "Buch S. 59–61", "bild": "img/phskala.svg",
        "alt": "Waagrechte Farbskala von pH 0 (rot) über 7 (grün) bis 14 (violett). Darüber Beispiele: Magensaft 1–2, Zitronensaft 2,4, Cola 2,5 bis 3, Kaffee 5, Haut um 5, Milch 6,6, reines Wasser 7, Blut 7,4, Meer 8,1, Natronlösung 8,3, Seifenlösung 9–10, nasser Beton 12–13. Darunter: jede Stufe mal 10.",
        "satz": ["Der **pH-Wert** reicht bei den meisten Lösungen von **0 bis 14**: unter 7 **sauer**, genau 7 **neutral**, über 7 **basisch**.",
                 "**Jede Stufe ist ein Faktor 10:** pH 4 hat zehnmal so viele H₃O⁺-Ionen wie pH 5 – und tausendmal so viele wie pH 7.",
                 "Dein Körper hat viele pH-Welten: Magen pH 1–2, Haut um 5, Blut 7,4."],
        "formeln": [("pH < 7", "sauer – mehr H₃O⁺ als OH⁻", ""), ("pH = 7", "neutral – gleich viele", ""), ("pH > 7", "basisch – mehr OH⁻ als H₃O⁺", ""),
                    ("1 Stufe", "Faktor 10", ""), ("3 Stufen", "Faktor 1000", "")],
        "link": "theorie.html#ph"},
 "k5": {"titel": "Messen: Papier oder pH-Meter?", "teil": "messen", "buch": "Buch S. 60", "bild": "img/versuch.svg",
        "alt": "Ablauf des Versuchs in vier Bildern: Tüpfelplatte mit sechs nummerierten Mulden, Tropfen hinein, Indikatorpapier eintauchen, Farbe mit der Farbskala vergleichen. Daneben ein pH-Meter mit Anzeige 2,5.",
        "satz": ["**Indikatorpapier** zeigt eine Farbe. Den pH-Wert liest du an der **Farbskala** ab – das ist eine **Schätzung** in ganzen Stufen.",
                 "Ein **pH-Meter** misst elektrisch und zeigt Kommastellen. Es ist **genauer**, muss aber eingestellt (kalibriert) werden.",
                 "**Kohlensäure:** Gelöstes CO₂ macht Wasser leicht sauer – darum ist prickelndes Mineralwasser saurer als Leitungswasser."],
        "formeln": [("CO₂ + H₂O → H₂CO₃", "Kohlendioxid + Wasser → Kohlensäure", ""), ("pH", "hat keine Einheit", "")],
        "link": "theorie.html#messen"},
 "k6": {"titel": "Neutralisation", "teil": "neutral", "buch": "Buch S. 65", "bild": "img/neutralisation.svg",
        "alt": "Links ein Becherglas mit roten H3O+-Ionen und Chlorid-Ionen (Salzsäure), rechts eines mit blauen OH--Ionen und Natrium-Ionen (Natronlauge). Beim Mischen werden aus H3O+ und OH- zwei Wassermoleküle; Natrium- und Chlorid-Ionen bleiben übrig. Ein Thermometer zeigt: warm.",
        "satz": ["Treffen Säure und Base zusammen, reagieren **H₃O⁺ und OH⁻** zu **Wasser**. Säure und Base heben sich auf – das ist die **Neutralisation**.",
                 "Übrig bleiben Metall-Ionen und Säurerest-Ionen: ein **Salz**. Aus Salzsäure und Natronlauge wird **Kochsalzlösung**.",
                 "Bei Salzsäure und Natronlauge wird das Glas **warm** – die Reaktion ist **exotherm**."],
        "formeln": [("H₃O⁺ + OH⁻ → 2 H₂O", "Kern: Säure + Lauge", ""), ("HCl + NaOH → NaCl + H₂O", "Säure + Base → Salz + Wasser", "")],
        "link": "theorie.html#neutral"},
 "k7": {"titel": "Dein Blut bleibt bei 7,4", "teil": "blut", "buch": "Buch S. 61–62", "bild": "img/blutpuffer.svg",
        "alt": "Kreislauf: Muskeln bilden CO2, das im Blut zu Kohlensäure wird. Hydrogencarbonat fängt H+ ab (Puffer). In der Lunge wird CO2 ausgeatmet. Daneben ein schmaler grüner Bereich von pH 7,35 bis 7,45 auf einer Skala.",
        "satz": ["Der **Blut-pH** liegt normal zwischen **7,35 und 7,45** – schwach basisch und eng geregelt.",
                 "Ein **Puffer** aus **Kohlensäure und Hydrogencarbonat** fängt zusätzliche H⁺ oder OH⁻ ab, sodass sich der pH-Wert kaum ändert.",
                 "Bei harter Belastung sinkt der pH kurz. Du atmest dann schneller: Mit dem **CO₂** verschwindet **Kohlensäure** aus dem Blut."],
        "formeln": [("CO₂ + H₂O → H₂CO₃", "Kohlensäure im Blut", ""), ("HCO₃⁻ + H⁺ → H₂CO₃", "Hydrogencarbonat fängt H⁺ ab", "")],
        "link": "theorie.html#blut"},
 "k8": {"titel": "Alles auf einen Blick", "teil": "kurz", "buch": "Buch S. 53–65", "bild": "img/ueberblick.svg",
        "alt": "Übersicht: links SAUER mit H3O+ und rotem Lackmus, rechts BASISCH mit OH- und blauem Lackmus, in der Mitte die pH-Skala mit 7 neutral. Unten: H3O+ + OH- wird zu Wasser (Neutralisation) und der Proton-Ball von der Säure zur Base.",
        "satz": ["**Sauer** = viele H₃O⁺, pH unter 7 · **basisch** = viele OH⁻, pH über 7 · **neutral** = pH 7.",
                 "**Säure gibt** ein Proton ab, **Base nimmt** es auf. **Säure + Base → Salz + Wasser.**",
                 "**Schutz:** Brille auf, erst Wasser dann Säure, bei Spritzern lange mit Wasser spülen."],
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
 {"id": "s0a", "title": "Von sauer bis basisch", "pill": "Buch S. 53",
  "blocks": [("img", "img/ueberblick.svg", KARTEN["k8"]["alt"], "Der Weg dieser Einheit: Säuren, Laugen, das Protonen-Pingpong, der pH-Wert – und wie sich alles wieder aufhebt."),
             ("ul", ["**Das Wichtigste vorab:** Ob etwas sauer oder basisch ist, hängt an einem einzigen winzigen Teilchen – dem **Proton (H⁺)**. Wer es abgibt, ist eine Säure. Wer es aufnimmt, ist eine Base.",
                     "**Wozu?** Du trinkst täglich Säuren (Cola, Energydrinks, Mineralwasser), wäschst dich mit Laugen und hast im Magen eine starke Säure. "
                     "Im Dienst begegnen dir Batteriesäure im Fahrzeug, nasser Beton (stark basisch) und Reiniger in der Unterkunft – ein Spritzer ins Auge ist dann ein Notfall.",
                     "**Sport und Gesundheit:** Dein Blut muss fast genau bei pH 7,4 bleiben. Beim Sprint gerät es kurz aus dem Takt – und deine Atmung holt es zurück.",
                     "**Das kannst du nachher:** Säuren und Laugen erkennen, pH-Werte messen und lesen, eine Säure-Base-Reaktion erklären und dich vor Verätzungen schützen."]),
             ("hint", "Du arbeitest im Arbeitsblatt – diese Seite ist zum Nachschlagen. Die Filmtipp-Seite des Schulbuchs: www.trauner.at/sauer (Buch S. 53).")]},
 {"id": "s0b", "title": "Science oder Fiction? Säureblut, das durch Stahl frisst", "pill": "Buch S. 54",
  "blocks": [("tiles", [("Im Film", ["In der »Alien«-Filmreihe hat das Monster Säure statt Blut. Ein Tropfen frisst sich in Sekunden durch mehrere Stahldecks des Raumschiffs."]),
                        ("In Wirklichkeit", ["Starke Säuren greifen viele Metalle wirklich an – unedle Metalle wie Zink oder Eisen lösen sich unter Gasbildung auf. "
                                             "Aber das dauert Minuten bis Stunden, nicht Sekunden. Und ein Körper voller starker Säure würde sich selbst verätzen."])]),
             ("ul", ["**Echte Säure-Waffen der Natur:** Ameisen sprühen **Ameisensäure** gegen Feinde. Dein **Magen** arbeitet mit **Salzsäure** (pH 1–2) und schützt sich mit einer Schleimschicht.",
                     "**Kleine Geschichte:** 1923 kamen der Däne **Johannes Brønsted** und der Engländer **Thomas Lowry** unabhängig voneinander auf dieselbe Idee: "
                     "Eine Säure ist ein Teilchen, das ein Proton abgibt. Diese Sicht benutzen wir bis heute (Buch S. 58).",
                     "**Offene Frage der Forschung:** Die Meere nehmen viel CO₂ auf und werden dadurch weniger basisch. Wie gut sich Korallen, Muscheln und winzige Meeresschnecken daran anpassen können, ist noch nicht geklärt."]),
             ("merke", "Filme hier nur in Worten – keine Filmbilder auf dieser Seite (Urheberrecht).")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("saeuren", "Teil 1 · Buch S. 53–55 · Stunde 1", "Säuren – sauer macht's", [
  {"id": "saeuren", "title": "Was macht eine Säure sauer?", "pill": "Buch S. 54–55",
   "blocks": [("buch", "Lies im **Buch S. 54** den Kasten **»Das sollten Sie speichern«** (2 min). Markiere die zwei Teilchen, in die eine Säure in Wasser zerfällt."),
              kartenblock("k1"),
              ("ul", ["Eine Säure wie **Chlorwasserstoff (HCl)** gibt in Wasser ihr Wasserstoff-Atom **ohne Elektron** ab – übrig bleibt nur der Kern, ein **Proton (H⁺)**.",
                      "Ein freies Proton gibt es im Wasser praktisch nicht: Es hängt sich an ein Wassermolekül. Aus H₂O wird **H₃O⁺**, das **Oxonium-Ion**. Viele Bücher schreiben vereinfacht nur H⁺.",
                      "Was von der Säure übrig bleibt, ist das **Säurerest-Ion**: Cl⁻ (Chlorid) aus Salzsäure, NO₃⁻ (Nitrat) aus Salpetersäure, SO₄²⁻ (Sulfat) aus Schwefelsäure.",
                      "Weil eine saure Lösung **Ionen** enthält, leitet sie elektrischen Strom – das brauchst du in der nächsten Einheit (Batterie).",
                      "Saure Lösungen **lösen unedle Metalle** (dabei entsteht Wasserstoff – darum Fisch mit Zitrone nicht in Alufolie einwickeln) und **lösen Kalk** (dabei sprudelt CO₂ – so entkalkt Essig den Wasserkocher)."]),
              ("table", [["Säure", "Formel", "wo du sie triffst"],
                         ["Salzsäure", "HCl", "im Magen (Verdauung, tötet Keime)"], ["Phosphorsäure", "H₃PO₄", "in Cola"],
                         ["Kohlensäure", "H₂CO₃", "im Mineralwasser – entsteht aus CO₂ + H₂O"], ["Schwefelsäure", "H₂SO₄", "Batteriesäure im Fahrzeug"],
                         ["Essigsäure", "CH₃COOH", "Essig, Salatsauce"], ["Zitronensäure", "–", "Zitrone, Limonade, Energydrinks"]]),
              ("tiles", [("Merkhilfe HNO₃", ["**Salpetersäure:** Wer sie ins Gesicht bekommt, landet beim **HNO-Arzt**. H, N, O – und **drei O** für Hals, Nase, Ohren."]),
                         ("Merkhilfe H₂SO₄", ["**Schwefelsäure** steckt in der **Fahrzeugbatterie**: **2 Pole** = 2 H, **S** wie Schwefel, **4 Räder** = 4 O."]),
                         ("Merkhilfe H₃PO₄", ["**Phosphorsäure** (in Cola): **nach drei kommt vier** – 3 H, ein P, 4 O."])]),
              ("img", "img/rotkraut.svg", "Farbskala des Rotkrautsafts: stark sauer rot, sauer rosa, schwach sauer rotviolett, neutral violett, schwach basisch blau, basisch grün, stark basisch gelb.",
               "Rotkrautsaft als Indikator: Die Farbe verrät, wie sauer oder basisch eine Lösung ist (ungefähre Werte)."),
              ("demo", "K1.5-D1", "Prof. HOLZER gibt Rotkrautsaft in vier Gläser mit Wasser. Dazu kommen **Essig, Zitronensaft, nichts** und **Natron**. "
                                  "**Erst vermuten:** Welche Farbe bekommt jedes Glas? Dann vergleicht ihr. Warum heißt Rotkraut in manchen Gegenden Blaukraut? Mit Essig oder Äpfeln gekocht wird es rot, ohne Säure eher blau-violett. "
                                  "**Zum Schluss:** Ein Stück **Marmor** (Kalk) kommt in Essig – es sprudelt. Säuren lösen Kalk."),
              ("sim", "rotkraut"),
              ("reveal", I.STOPPFRAGEN["saeuren"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2", "aufgaben.html#card_a1")]),

 ("basen", "Teil 2 · Buch S. 56–57 · Stunde 2", "Basen und Laugen – seifig, nützlich, ätzend", [
  {"id": "basen", "title": "Das Gegenstück zu den Säuren", "pill": "Buch S. 56–57",
   "blocks": [("buch", "Lies im **Buch S. 56** den Kasten **»Das sollten Sie speichern«** und den Merksatz links unten zum Verdünnen."),
              kartenblock("k2"),
              ("ul", ["**Natriumhydroxid (NaOH)** ist ein fester Stoff aus Na⁺- und OH⁻-Ionen. Im Wasser lösen sich die Ionen voneinander – es entsteht **Natronlauge**.",
                      "Laugen im Alltag: **Rohrreiniger** (Natriumhydroxid) löst Haare und Fett im Abfluss, die **Laugenbrezel** wird vor dem Backen in verdünnte Lauge getaucht, "
                      "Echte **Seife** (z. B. Kernseife) und **Waschmittel** sind basisch – viele Flüssigseifen und Duschgele sind dagegen auf den Haut-pH eingestellt (»pH-hautneutral«, leicht sauer); **nasser Beton** hat pH 12 bis 13.",
                      "**Natron** (Natriumhydrogencarbonat, im Backpulver) ist eine milde Base: Es **nimmt H⁺ auf** und gibt dabei CO₂ ab – darum geht der Teig auf.",
                      "**Erst das Wasser, dann die Säure:** Beim Verdünnen von Säuren wird viel Wärme frei. Gießt man Wasser in die Säure, kann das erste Wasser schlagartig sieden und Säure herausspritzen."]),
              ("tiles", [("Säure im Auge", ["greift die Oberfläche an und bildet eine Art Schorf – die Säure kommt dadurch weniger tief."]),
                         ("Lauge im Auge", ["löst Fett und Eiweiß auf und **dringt immer tiefer** ein. Oft brennt es anfangs kaum – darum besonders gefährlich."]),
                         ("Erste Hilfe", ["Sofort **lange (10–15 min und mehr) mit viel Wasser spülen**, Auge dabei offen halten, Hilfe holen. **Nicht** neutralisieren."])]),
              ("hint", "Im Buch S. 57 steht der Versuch »Chemisches Schiffeversenken« mit Natrium. Den machen wir nicht – Natrium ist ein Gefahrstoff."),
              ("reveal", I.STOPPFRAGEN["basen"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3", "aufgaben.html#card_a2")]),

 ("protolyse", "Teil 3 · Buch S. 58–59 · Stunde 2", "Protonen-Pingpong – Säure-Base-Reaktionen", [
  {"id": "protolyse", "title": "Wer gibt ab, wer fängt?", "pill": "Buch S. 58–59",
   "blocks": [("buch", "Lies im **Buch S. 58** den Kasten **»Das sollten Sie speichern«** und das erste Beispiel »Protolyse einer starken Säure«."),
              kartenblock("k3"),
              ("ul", ["Brønsted schaut nicht auf den Stoff, sondern auf das, **was ein Teilchen tut**: Gibt es ein Proton ab, wirkt es als Säure. Nimmt es eines auf, wirkt es als Base.",
                      "Darum braucht jede Säure einen Partner: **Ohne Base, die fängt, kann keine Säure abgeben.** Das Ganze heißt **Protolyse**.",
                      "Nach der Abgabe wird aus der Säure ein Teilchen, das das Proton wieder nehmen könnte: HCl wird zu Cl⁻. Solche Paare heißen **Säure-Base-Paare**.",
                      "**Ammoniak (NH₃)** hat gar kein OH – und ist trotzdem eine Base: Es nimmt vom Wasser ein Proton. Dabei bleibt OH⁻ übrig, darum ist Ammoniaklösung basisch. Das passiert nur bei einem kleinen Teil der NH₃-Teilchen – trotzdem reicht es für einen pH um 11."]),
              ("gemeinsam", "**Protonen-Pingpong mit Ball:** Ein Kadett ist HCl und hält den Ball (das Proton). Er wirft ihn einem Kadetten zu, der H₂O spielt. Der wird damit zu H₃O⁺ – "
                            "und muss ein Schild umdrehen. Danach dasselbe mit Wasser und Ammoniak."),
              ("reveal", I.STOPPFRAGEN["protolyse"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 4", "aufgaben.html#card_a3")]),

 ("ph", "Teil 4 · Buch S. 59–61 · Stunde 3", "Der pH-Wert – sauer, neutral, basisch in Zahlen", [
  {"id": "ph", "title": "Eine Skala von 0 bis 14", "pill": "Buch S. 59–61",
   "blocks": [("buch", "Lies im **Buch S. 59** den Kasten **»Änderung des pH-Werts«** und schau dir auf **S. 61** die Beispiel-Skala am Rand an."),
              kartenblock("k4"),
              ("sim", "ph"),
              ("extern", "pH Skala: Grundlagen", "https://phet.colorado.edu/de/simulations/ph-scale-basics",
               "Miss Kaffee, Limonade, Blut oder Abflussreiniger mit dem pH-Meter – und verdünne mit Wasser. Dazu gibt es den **virtuellen Versuch** im Arbeitsblatt (Zusatz 11).",
               "PhET, University of Colorado Boulder · Deutsch · CC BY 4.0"),
              ("extern", "pH Skala", "https://phet.colorado.edu/de/simulations/ph-scale",
               "Für Neugierige: Hier siehst du, wie viele H₃O⁺- und OH⁻-Teilchen in der Lösung sind – und warum eine pH-Stufe Faktor 10 bedeutet.",
               "PhET, University of Colorado Boulder · Deutsch · CC BY 4.0"),
              ("ul", ["In reinem Wasser gibt es **gleich viele H₃O⁺- und OH⁻-Ionen** – darum ist es neutral (pH 7). Kommt eine Säure dazu, steigen die H₃O⁺ und der pH-Wert **sinkt**.",
                      "**Faktor 10 pro Stufe:** Zitronensaft (pH 2) hat **tausendmal** so viele H₃O⁺-Ionen wie Kaffee (pH 5). Darum wirken kleine Unterschiede beim pH-Wert groß.",
                      "**pH-hautneutral** heißt nicht pH 7, sondern: etwa der pH-Wert der Haut – **leicht sauer**. Schweiß und Talg bilden auf der Haut einen dünnen **Säureschutzmantel**, der Keime abwehrt. Das Buch nennt ca. 5,5, eine Studie mit 330 Personen fand im Mittel sogar unter 5 (Messung an der Haut, 2006). **Kernseife** (pH 9–10) hebt den Haut-pH für einige Stunden an – gesunde Haut holt ihn selbst zurück.",
                      "**Trinkwasser** soll in Österreich zwischen pH 6,5 und 9,5 liegen (Richtwert der Trinkwasserverordnung). Das Wiener Neustädter Leitungswasser hat laut Wasserwerk pH 7,4 bis 7,6 – leicht basisch."]),
              ("hint", "Das Buch zeigt auf S. 59 auch Konzentrationen wie 10⁻⁷ mol/l. Die musst du nicht rechnen – wichtig ist nur: eine Stufe = Faktor 10."),
              ("reveal", I.STOPPFRAGEN["ph"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 5", "aufgaben.html#card_a4")]),

 ("messen", "Teil 5 · Buch S. 60 · Stunde 3", "Messen: Indikatorpapier und pH-Meter", [
  {"id": "messen", "title": "pH-Detektive", "pill": "Buch S. 60–61",
   "blocks": [kartenblock("k5"),
              ("versuch", "K1.5-V1", "Sechs Proben aus Küche und Bad: Zitronensaft, Cola, Mineralwasser, Leitungswasser, Natronlösung, Seifenlösung – und freiwillig **eure Haut**. Alle Gruppen machen dasselbe – "
                                    "die Anleitung steht im Arbeitsblatt bei Aufgabe 6.", "aufgaben.html#card_a5"),
              ("demo", "K1.5-D2", "Während ihr messt, misst Prof. HOLZER dieselben Proben mit dem **pH-Meter**. Am Ende vergleicht die Klasse: Wo liegen Papier und Gerät nah beisammen, wo nicht?"),
              ("ul", ["**Destilliertes Wasser** ist an der Luft meist **nicht** genau neutral: Es nimmt CO₂ auf und wird leicht sauer. Darum nehmen wir Leitungswasser als Vergleich.",
                      "**Farbstoffe** in Cola oder Saft können die Farbe des Papiers verfälschen – ein Grund, warum das pH-Meter genauer ist. Bei **Tinte** oder stark gefärbten Säften taugen Indikatoren gar nicht.",
                      "Messwerte sind **Beispiele**, keine Wahrheit von oben: Weicht euer Wert ab, schreibt ihn ehrlich auf und überlegt, warum."]),
              ("reveal", I.STOPPFRAGEN["messen"])]}]),

 ("neutral", "Teil 6 · Buch S. 65 · Stunde 4", "Neutralisation – Säure und Base heben sich auf", [
  {"id": "neutral", "title": "Aus sauer und basisch wird Wasser", "pill": "Buch S. 65",
   "blocks": [("buch", "Lies im **Buch S. 65** das Beispiel **»Neutralisation von Salzsäure HCl und Natronlauge NaOH«**."),
              kartenblock("k6"),
              ("demo", "K1.5-D3", "Rotkrautsaft in Leitungswasser – ein Kadett bläst mit dem eigenen Strohhalm hinein (nur blasen, nicht saugen): Die Farbe wird **violetter**, denn aus seinem CO₂ entsteht **Kohlensäure**. "
                                  "Dann gibt Prof. HOLZER **Essig** dazu (rot) und danach **Natron** (es schäumt, die Farbe geht zurück). **Erst vermuten:** Was passiert bei jedem Schritt?"),
              ("ul", ["Trifft eine Säure auf eine **Lauge** (z. B. Salzsäure auf Natronlauge), passiert im Kern immer dasselbe: **H₃O⁺ + OH⁻ → 2 H₂O**. Die anderen Ionen (z. B. Na⁺ und Cl⁻) schwimmen nur mit. Das Glas wird dabei warm. Merkspruch: **Jedes OH⁻ braucht ein H⁺** – erst dann ist alles Wasser.",
                      "Dampft man das Wasser ab, bleibt das **Salz** als Kristall zurück – aus Salzsäure und Natronlauge wird Kochsalz. Mehr zu Salzen kommt in der Einheit »Salze und Kunstdünger«.",
                      "**Sodbrennen:** Magensäure steigt in die Speiseröhre. Mittel aus der Apotheke (**Antazida**) enthalten schwache Basen (z. B. Calcium- und Magnesiumcarbonat), die einen Teil der Säure neutralisieren. Ein Löffel **Zitronensaft** hilft nicht – er ist selbst sauer (Zusatz 13).",
                      "**Essig + Natron** ist auch eine Säure-Base-Reaktion: Das Hydrogencarbonat nimmt Protonen auf, dabei entsteht CO₂ – darum schäumt es. Hier ist kein OH⁻ im Spiel, und das Glas wird sogar ein wenig **kühler**: Nicht jede Säure-Base-Reaktion gibt Wärme ab."]),
              ("sim", "neutral"),
              ("reveal", I.STOPPFRAGEN["neutral"])]}]),

 ("blut", "Teil 7 · Buch S. 61–62 · Stunde 4", "Warum dein Blut bei 7,4 bleibt", [
  {"id": "blut", "title": "Puffer, Atmung und Sport", "pill": "Buch S. 61–62",
   "blocks": [("buch", "Lies im **Buch S. 62** den Abschnitt zum **Blut** (Kohlensäure und Bicarbonat) und den Kasten zur **Atmung**."),
              kartenblock("k7"),
              ("ul", ["Ein **Puffer** ist ein Paar aus schwacher Säure und ihrer Base. Kommt Säure dazu, fängt die Base die H⁺ ab; kommt Base dazu, gibt die Säure H⁺ ab. Der pH-Wert bleibt fast gleich.",
                      "Im Blut puffern vor allem **Kohlensäure und Hydrogencarbonat**, dazu Eiweiße wie das Hämoglobin.",
                      "**Sport:** Bei einem harten Sprint sammeln sich im Muskel viele H⁺-Ionen. In einer Studie mit 12 Elite-Radfahrern (3 Minuten Vollgas, ohne Natron) sank der Blut-pH von 7,35 auf 7,13. "
                      "Du atmest schneller und tiefer – so verlässt mehr CO₂ den Körper, und der pH steigt wieder.",
                      "**Mythos Muskelkater:** Lange hieß es, Milchsäure (Laktat) sei schuld. Laktat ist aber nach 30 bis 90 Minuten wieder auf dem Ausgangswert – "
                      "Muskelkater kommt erst nach 1 bis 3 Tagen. Ursache sind winzige Verletzungen der Muskelfasern.",
                      "Sinkt der Blut-pH unter 7,35, spricht man von **Azidose**, steigt er über 7,45, von **Alkalose**. Nach einem harten Sprint ist eine kurze Azidose **normal** – Atmung und Puffer gleichen sie in Minuten aus. Hält eine Azidose oder Alkalose an (z. B. bei einer Krankheit), muss sie ärztlich behandelt werden."]),
              ("sim", "blut"),
              ("reveal", I.STOPPFRAGEN["blut"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 7", "aufgaben.html#card_a6")]),
]

SCHNELLE = [
 {"id": "schnell1", "title": "Ozeanversauerung – Forschung aktuell", "pill": "OPTIONAL · Zusatz 9",
  "blocks": [("ul", ["Das Potsdam-Institut für Klimafolgenforschung meldete im September 2025: Die Grenze für die **Ozeanversauerung** ist überschritten. Der pH-Wert an der Meeresoberfläche ist seit Beginn der Industrialisierung um **rund 0,1** gesunken.",
                     "Ursache ist **CO₂** aus Öl, Gas und Kohle: Ein Teil löst sich im Meer und bildet **Kohlensäure** – dieselbe Reaktion wie im Mineralwasser.",
                     "Winzige **Flügelschnecken**, Futter für Fische und Wale, zeigen schon Schäden an ihren **Kalkschalen**. Korallenriffe stehen unter Druck.",
                     "**Zusatz 9** rechnet nach, was 0,1 pH-Stufen bedeuten – und prüft, warum das Institut 30 bis 40 % schreibt."])]},
 {"id": "schnell2", "title": "Energydrinks und deine Zähne", "pill": "OPTIONAL · Zusatz 13",
  "blocks": [("ul", ["Zahnschmelz wird von Säuren angegriffen. Ein Berner Zahnmediziner, der seit Jahrzehnten dazu forscht, zählt **Energydrinks zu den erosivsten Getränken** – vor allem wegen der **Zitronensäure**.",
                     "Der pH-Wert allein entscheidet aber nicht: **Joghurt** ist sauer, schadet den Zähnen aber kaum – sein **Calcium** wirkt dagegen.",
                     "Das Schlimmste ist **schluckweises Trinken über Stunden**: Die Zähne baden dann immer wieder in Säure. Besser: zügig trinken und danach einen Schluck **Wasser**.",
                     "Nach dem Essen machen Bakterien im Zahnbelag aus Zucker Säure: In **5 bis 10 Minuten** fällt der pH am Zahn unter **5,5** – ab da wird der Zahnschmelz angegriffen. Der **Speichel** puffert und bringt den pH in 30 bis 60 Minuten zurück. **Zuckerfreier Kaugummi** regt den Speichel an und verkürzt diese Zeit. **Zusatz 13** zeigt das als Kurve (»Stephan-Kurve«)."])]},
 {"id": "schnell3", "title": "Sicherheit im Dienst", "pill": "OPTIONAL · Zusatz 10",
  "blocks": [("table", [["Stoff", "pH ungefähr", "Gefahr", "Schutz"],
                        ["Batteriesäure (Fahrzeug)", "unter 1", "verätzt Haut und Augen, frisst Kleidung", "Brille, Handschuhe, nicht kippen"],
                        ["Rohrreiniger", "über 13", "verätzt besonders die Augen", "Brille, Handschuhe, nie mischen"],
                        ["nasser Beton/Zement", "12–13", "Verätzung oft erst nach Stunden bemerkt", "Handschuhe, lange Kleidung, Brille"],
                        ["Essigreiniger", "2–3", "reizt Augen und Haut", "nicht mit Chlorreiniger mischen"]]),
             ("hint", "Zusatz 10: Mach daraus ein 60-Sekunden-Briefing als Podcast oder ein Plakat. Zusatzaufgaben sind freiwillig und keine Hausübung.")]},
]
