"""Theorie-Seite PBGW 3BK · Meilensteine, Hochkulturen, Athen und Rom: Teile und Folien. Dieselben Daten bauen die Theorie-Folien der TH-Lehrer-/TH-Kadetten-PPP
und die Lesestopps der TH-Unterricht (eine Quelle).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag im Schulbuch).
Alles in eigenen Worten (Grundlage: Texte T1–T6 des ChatGPT-Auftrags, überarbeitet); Grafiken selbst gezeichnet (skizzen.py). Keine Buchbilder, kein Buchtext auf öffentlichen Seiten.
Lesestopps je Stunde: siehe plan.py (Wortzahl → Lesezeit, ca. 120 Wörter/min)."""
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Ein Beil verrät mehr, als man denkt", "pill": "Buch S. 30",
  "blocks": [("img", "img/beil.png", "Zeichnung eines Kupferbeils: Klinge aus Kupfer, in einem Holzschaft befestigt. Daneben drei Fragen: Was sehen wir? Was vermuten wir? Was wissen wir nicht?", "Eigene Zeichnung nach dem Typ des Beils von Ötzi – kein Foto des Fundes."),
             ("ul", ["Ötzi kennt ihr aus der Quellenarbeit. Heute schauen wir auf **einen Gegenstand** aus seiner Ausrüstung: das Kupferbeil.",
                     "Was lässt sich **feststellen**? Was ist eine **begründete Vermutung**? Und was lässt sich mit dem Beil allein **nicht belegen**?"]),
             ("hint", "Leitfrage der Einheit: " + I.LEITFRAGE)]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Teil 1 · Stunde 1
 ("teil1", "Stunde 1 · " + I.wann(1) + " · Buch S. 25–39", I.TEILNAME[1], [
  {"id": "vorrat", "title": "Vom Sammeln zum Vorrat", "pill": "Buch S. 25–28",
   "blocks": [("ul", ["Vor rund 12 000 Jahren begann im Vorderen Orient ein Wandel: Menschen bauten Pflanzen an und hielten Tiere. Auch in anderen Weltregionen entstand Landwirtschaft. Der Übergang dauerte **viele Generationen** und verlief je nach Region verschieden. Der Ausdruck **Neolithische Revolution** beschreibt die große Wirkung, nicht einen einzelnen Tag.",
                      "Aus der Ernte ließ sich ein **Vorrat** anlegen. Er musste geschützt, gelagert und verteilt werden. Wenn nicht mehr alle ständig Nahrung suchen mussten, konnten sich einzelne auf andere Arbeiten **spezialisieren**, zum Beispiel auf Töpfern oder Metall. Spezialisierung heißt: Man übt eine Tätigkeit besonders gut und regelmäßig aus."]),
              ("merke", "Landwirtschaft eröffnete neue Möglichkeiten der Versorgung – und veränderte **Arbeit, Abhängigkeiten und Macht**.")]},
  {"id": "probleme", "title": "Neue Möglichkeiten, neue Probleme", "pill": "Buch S. 25–28",
   "blocks": [("tiles", [("Neue Möglichkeiten", ["mehr Menschen an einem Ort versorgen", "Vorräte für schlechte Zeiten", "Platz für Spezialisten"]),
                         ("Neue Probleme", ["**Missernte** trifft viele zugleich", "**Krankheiten** breiten sich im engen Zusammenleben leichter aus", "Land, Tiere und Vorräte sind **ungleich verteilt** – daraus kann Streit entstehen"])]),
              ("ul", ["Wer über wichtige Ressourcen verfügt, kann **Einfluss** gewinnen. Daraus entsteht aber **nicht automatisch ein Staat**: Auch Handel, Konflikte, religiöse Vorstellungen und die örtlichen Bedingungen wirken mit.",
                      "Auch das Bild vom Dorf, in dem Frauen und Männer gleichberechtigt Felder bestellen, ist zu einfach: Gemeinsame Arbeit beweist **keine** politische Gleichstellung."]),
              ("hint", "Zwei Satzbausteine für Aufgabe 2: »… kann … ermöglichen, weil …« und »… kann … führen, weil …«.")]},
  {"id": "metall", "title": "Metall, Können und Austausch", "pill": "Buch S. 29–32",
   "blocks": [("ul", ["Ötzis Ausrüstung enthielt ein **Kupferbeil** – und Geräte aus Holz, Stein und anderen Stoffen. Neue Werkstoffe ersetzten ältere also nicht sofort. Wer Kupfer verarbeitet, braucht **Rohstoff, Brennstoff und Können**. Fehlt der Rohstoff vor Ort, muss er durch **Austausch** beschafft werden, manchmal über weite Strecken.",
                      "**Bronze** besteht aus Kupfer und weiteren Metallen, oft Zinn (zum Beispiel etwa 90 % Kupfer und 10 % Zinn). Die Namen Kupfer-, Bronze- und Eisenzeit helfen bei der Orientierung; ihre Zeitgrenzen gelten **nicht überall gleich**.",
                      "Die Forscher unterscheiden **Befund** (was man am Gegenstand feststellen kann) und **Deutung** (was man begründet daraus schließt). Aus dem Beil allein folgt weder Ötzis Beruf noch sein Rang noch eine Reise."]),
              ("video", "oetzi"),
              ("hint", "Aktuell: Eine Analyse der Bleiisotope im Metall (Südtiroler Archäologiemuseum und Universität Padua, 2024) legt nahe, dass das Kupfer von Ötzis Beil aus der südlichen Toskana stammt. Das zeigt den Weg des **Metalls**, nicht den Weg einer Person.")]},
  {"id": "schrift", "title": "Schrift: Listen und Verwaltung", "pill": "Buch S. 34–35",
   "blocks": [("img", "img/kette.png", "Vier Kästchen in einer Reihe, verbunden durch Pfeile: Ernte und Abgaben, Lager, Liste mit Zeichen und Zahlen, Verteilung. Unter der Liste steht: Wer die Liste führt, hat Einfluss.", "Eigene Zeichnung: Wie Verwaltung funktioniert."),
              ("ul", ["Frühe Schriftzeugnisse aus Mesopotamien sind oft **Listen**: Mengen, Güter, Abgaben. Eine Liste macht Entscheidungen **nachvollziehbar** – und wer sie führt und kontrolliert, kann zugleich **Einfluss** ausüben.",
                      "Schrift entstand nicht nur an einem Ort und entwickelte sich nicht geradlinig von einfachen Bildern zur besten Schrift. Auch **Hieroglyphen** sind nicht bloß Bilder."])]},
  {"id": "staaten", "title": "Frühe Staaten: Stadtstaat und Flächenkönigtum", "pill": "Buch S. 33–39",
   "blocks": [("img", "img/karte.png", "Schematische Karte mit drei Flüssen: der Nil im Westen fließt von Süden nach Norden in ein Delta am Mittelmeer; Euphrat und Tigris im Osten fließen von Nordwesten nach Südosten zum Persischen Golf. Städte: Memphis, Theben, Uruk, Babylon, Ur. Hinweis: Schema, nicht maßstabsgerecht.", "Eigene Karte: Schema, nicht maßstabsgerecht."),
              ("tiles", [("Stadtstaat (Mesopotamien)", ["Eine **Stadt** mit ihrem **Umland** bildet einen eigenen Staat, zum Beispiel Uruk.", "Das Umland liefert viel Nahrung.", "Zwischen den Städten gibt es Austausch, Konkurrenz und Krieg."]),
                         ("Flächenkönigtum (Ägypten)", ["Ein **Königtum** umfasst ein langes Flusstal mit vielen Siedlungen am Nil.", "Der **Pharao** steht an der Spitze einer **Hierarchie** (Menschen und Ämter haben verschiedene Befugnisse).", "Religion hilft, Herrschaft zu begründen."])]),
              ("ul", ["In beiden Räumen mussten **Abgaben, Arbeit und Vorräte** organisiert werden, und Wasser war lebenswichtig. Bewässerung verlangt Zusammenarbeit – ist aber **nicht die einzige Ursache** der Staatenbildung.",
                      "Solche städtischen Gesellschaften nennt das Buch **Hochkulturen**. Der Begriff ist gebräuchlich, legt aber eine Rangordnung nahe. Verschiedene Organisationsformen sagen **nichts über den Wert der Menschen** aus. **Flächenkönigtum** ist hier ein Vergleichsbegriff."]),
              ("merke", "Stadtstaat und Flächenkönigtum lösen **ähnliche Aufgaben** der Versorgung und Herrschaft in **verschiedener Form**.")]},
  {"id": "zeitstrahl", "title": "Der gemeinsame Zeitstrahl", "pill": "Buch S. 24–40 · Aufgabe 8",
   "blocks": [("img", "img/zeitstrahl.png", "Zeittafel mit sechs gleich breiten Zeitbereichen von 10 000 bis 8000 v. Chr. bis 400 bis 500 n. Chr. und drei Zeilen: Vorderer Orient, Alpenraum, Mittelmeerraum. Eingetragen sind die neun Ereignisse der Aufgabe 8. Die Zeitbereiche sind nicht gleich lang.", "Eigene Zeichnung: Die Bereiche sind **nicht gleich lang** – sie sind nur gleich breit gezeichnet."),
              ("ul", ["Die Jahreszahlen sind **Orientierung**, nicht Prüfungsstoff. Wichtiger ist die Begründung: In welche Zeit passt ein Ereignis – und was lief **gleichzeitig, aber an einem anderen Ort**?",
                      "Karten 1–4 ordnest du in Stunde 1 ein, Karten 5–9 erst in Stunde 3."]),
              ("hint", "Nicht als Abfolge lesen: »Ötzi erfindet das Metall, dann entsteht Schrift.« Beides liegt ungefähr in derselben Zeit – aber an verschiedenen Orten.")]},
  {"id": "stop1", "title": "Stopp – kannst du das?", "pill": "Buch S. 25–39", "blocks": [("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt: Aufgaben 1 bis 3 und 8 (Teil 1)", "aufgaben.html#card_a1"),
 ]),

 # ---------------------------------------------------------------- Teil 2 · Stunde 2 (nach dem Test)
 ("teil2", "Stunde 2 · " + I.wann(2) + " · nach dem Test · Buch S. 39–40", I.TEILNAME[2], [
  {"id": "regeln", "title": "Was die Regeln verraten", "pill": "Buch S. 39–40",
   "blocks": [("ul", ["Hammurabi war im 18. Jahrhundert v. Chr. König von Babylon. Mit seinem Namen verbunden ist eine **Rechtssammlung**, die auf einer **Stele** (aufgerichteter Stein mit Inschrift) überliefert ist. Viele Regeln folgen einem Muster: **Wenn** etwas Bestimmtes geschieht, **dann** tritt eine bestimmte Folge ein.",
                      "Die Regeln zeigen, welche **Konflikte geordnet** werden sollten. Ein schlecht gewarteter Damm konnte fremde Felder überschwemmen (§ 53) – eine Frage von **Verantwortung**."]),
              ("table", [["§", "Arbeitsfassung (vereinfacht)"]] + I.T[3]["tab"][1:]),
              ("hint", "Sprachlich vereinfachte Arbeitsfassung nach Buch S. 40, kein wörtliches Zitat. Eine **Mine** ist eine Gewichts- und Recheneinheit für Silber."),
              ("ul", ["Dieselbe Verletzung hat **verschiedene Folgen**, je nachdem, wen sie trifft (§ 196, 198, 199). Der Text macht **soziale Ungleichheit** sichtbar. Beim Knecht (versklavten Menschen) zählt der Kaufpreis: Er wird wie **Eigentum** behandelt."])]},
  {"id": "gleichheit", "title": "Recht ist nicht gleich Gleichheit", "pill": "Buch S. 39–40",
   "blocks": [("tiles", [("Eine schriftliche Regel …", ["macht Folgen **berechenbar**", "kann Konflikte **ordnen**", "kann **Herrschaft stützen**"]),
                         ("… sagt nicht automatisch", ["dass alle **gleich** behandelt werden", "dass jeder Fall im Alltag **so entschieden** wurde", "dass der Text **neutral** ist"])]),
              ("ul", ["Die Sammlung stammt aus dem Umfeld **königlicher Herrschaft**. Sie zeigt auch, wie der Herrscher seine Ordnung **darstellen wollte**.",
                      "Hammurabis Sammlung war **nicht die erste** Rechtssammlung der Geschichte: Ältere sind bekannt. Sie ist kein modernes Gesetzbuch, sondern ein bedeutendes **Zeugnis** königlicher Rechtsetzung.",
                      "»Auge um Auge« ist eine Form der **Vergeltung**. Daneben stehen **Ausgleichszahlungen** – und beides hängt vom Stand ab."]),
              ("merke", "Recht kann Konflikte ordnen und Herrschaft stützen. Prüfe immer: **Inhalt, Perspektive, Grenzen** der Aussage.")]},
  {"id": "stop2", "title": "Stopp – kannst du das?", "pill": "Buch S. 39–40", "blocks": [("reveal", I.STOPPFRAGEN[2])]},
  ("jetzt", "Jetzt: Aufgabe 4", "aufgaben.html#card_a4"),
 ]),

 # ---------------------------------------------------------------- Teil 3 · Stunde 3
 ("teil3", "Stunde 3 · " + I.wann(3) + " · Buch S. 105–118", I.TEILNAME[3], [
  {"id": "athen", "title": "Athen: direkte Beteiligung mit Grenzen", "pill": "Buch S. 107–111",
   "blocks": [("img", "img/athen.png", "Schaubild: In der Mitte die Volksversammlung der erwachsenen männlichen Bürger. Darüber der Rat der 500 (durch Los), daneben die Archonten (durch Los) und die Strategen (durch Wahl). Daneben, ausgeschlossen: Frauen, Versklavte, Metöken.", "Eigenes, vereinfachtes Schaubild – nicht das Schaubild aus dem Schulbuch."),
              ("ul", ["Die griechische Welt bestand aus vielen selbstständigen Gemeinschaften. Eine **Polis** war eine solche Gemeinschaft aus Stadt und Umland. Athen entwickelte vor allem im 5. Jh. v. Chr. eine **direkte Demokratie**: Die beteiligten Bürger entschieden in der **Volksversammlung** selbst. Ein **Rat** bereitete die Beratungen vor.",
                      "Viele Ämter wurden durch **Los** vergeben, die **Strategen** (Heerführer) durch **Wahl**. Mitentscheiden durften nur **erwachsene männliche Bürger**. **Frauen, Versklavte** und **Metöken** (dauerhaft ansässige Menschen ohne Bürgerrecht) waren ausgeschlossen. »Volk« hieß also nicht »alle Bewohner«.",
                      "**Österreich heute:** Die Wahlberechtigten bestimmen **Vertreter**, die an Gesetzen mitwirken und die Regierung kontrollieren. Auch heute sind Wahlrechte an Voraussetzungen gebunden. Der Vergleich fragt nach **Beteiligung, Ausschluss und Kontrolle** – er setzt beides nicht gleich."]),
              ("hint", "Bilder von Athen sind oft **spätere Darstellungen**, keine Augenzeugenbilder. Reformen des Kleisthenes um 508/507 v. Chr. sind ein Orientierungspunkt, aber nicht das ganze Bild der Demokratie."),
              ("merke", "Athen entwickelte weitreichende Beteiligung – **innerhalb einer eng begrenzten Bürgergruppe**.")]},
  {"id": "rom", "title": "Rom: Republik und Machtkonzentration", "pill": "Buch S. 112–115",
   "blocks": [("img", "img/rom.png", "Schaubild: Zwei Konsuln mit begrenzter Amtszeit, daneben der Senat (einflussreiche Familien) und die Volksversammlungen, dazu Volkstribunen mit Einspruchsrecht. Darunter ein zweites Bild: Der Princeps steht über allen Einrichtungen und hat das Heer.", "Eigenes, vereinfachtes Schaubild – die Ordnung veränderte sich im Lauf der Zeit."),
              ("ul", ["Nach der überlieferten Königszeit entstand in Rom eine **Republik** (lat. res publica, »öffentliche Angelegenheit«). Aufgaben waren auf mehrere Einrichtungen verteilt: **zwei Konsuln** mit begrenzter Amtszeit, der **Senat** (einflussreiche Familien), Volksversammlungen, **Volkstribunen** (Einspruchsrecht für die Plebejer).",
                      "Das war **keine moderne Demokratie**: Vermögen, Herkunft und Verbindungen beeinflussten den Zugang zur Politik, Frauen und Versklavte waren ausgeschlossen. Nach Bürgerkriegen setzte sich **Octavian** durch, seit **27 v. Chr.** hieß er **Augustus**. Er ließ die Einrichtungen bestehen und stellte sich als **Wahrer der Republik** dar.",
                      "Tatsächlich vereinte er die **entscheidenden Machtmittel**: den **Oberbefehl über das Heer**, die Gewalt in wichtigen **Provinzen**, Befugnisse von **Konsul** und **Volkstribun** und den **Ehrenname** Augustus. Sich selbst nannte er **Princeps** (»Erster unter Gleichen«). Diese Herrschaftsform heißt **Prinzipat**."]),
              ("merke", "Mehrere Einrichtungen können bestehen bleiben, während die **tatsächliche Macht** bei einer Person liegt.")]},
  {"id": "vergleich", "title": "Athen und Rom im Vergleich", "pill": "Buch S. 107–115",
   "blocks": [("tiles", [("Drei Prüffragen", ["**Wo liegt die entscheidende Macht?**", "**Wer darf beteiligt sein – und wer nicht?**", "**Welche Kontrolle und welche Grenze gibt es?**"]),
                         ("Beispiel Ägypten", ["Macht: beim König und seiner Verwaltung", "Beteiligung: die Bevölkerung entscheidet nicht mit", "Kontrolle: keine moderne Machtkontrolle"])]),
              ("ul", ["Kein Ranking »primitiv – modern«: Es geht um **verschiedene Antworten** auf die Frage, wie Gemeinschaften Macht verteilen.",
                      "»Republik« allein sagt **nicht**, dass alle gleich mitentscheiden. Belege jede Aussage mit einem **konkreten Merkmal** (Los, Konsuln, Heer, Volkstribun …)."]),
              ("hint", "Zum Spaß: In einer bekannten Science-Fiction-Filmreihe wird aus einer Republik ein Kaiserreich – der Senat bleibt noch eine Zeit lang bestehen. Welche historische Entwicklung erinnert daran? (Aufgabe 6 hilft.)")]},
  {"id": "anschluss", "title": "Der Anschluss: Antike und spätere Zeiten", "pill": "Buch S. 115–118",
   "blocks": [("ul", ["Die Absetzung des letzten weströmischen Kaisers **476 n. Chr.** ist ein gebräuchlicher **Orientierungspunkt**. Viele Lebensformen und Einrichtungen veränderten sich über längere Zeit, das **oströmische Reich bestand weiter**.",
                      "Zwischen Antike und Früher Neuzeit liegt das lange **Mittelalter**. In der nächsten Einheit fragen wir, wie sich um 1500 Wissen, Religion, Wirtschaft und Macht veränderten. Antike Vorbilder wurden dabei neu gedeutet – daraus folgt **keine lückenlose Linie** von Athen zur heutigen Demokratie."])]},
  {"id": "stop3", "title": "Stopp – kannst du das?", "pill": "Buch S. 105–118", "blocks": [("reveal", I.STOPPFRAGEN[3])]},
  ("jetzt", "Jetzt: Aufgaben 5 bis 7 und 8 (Teil 2)", "aufgaben.html#card_a5"),
 ]),
]

SCHNELLE = [
 {"id": "partnercheck", "title": "Partnercheck – Karten zum Wiederholen", "pill": "Buch S. 25–40",
  "blocks": [("hint", "Zu zweit: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken (Aufgabe 12)."), ("karten", I.PARTNERKARTEN)]},
 {"id": "stolpern", "title": "Fünf Stolpersteine", "pill": "Zum Nachdenken",
  "blocks": [("karten", I.STOLPERSTEINE)]},
 {"id": "quelle", "title": "Eine Quelle kritisch lesen", "pill": "Quellenkritik",
  "blocks": [("ul", ["**Wer** hat den Text oder das Bild gemacht – und **wann**? Gleichzeitig mit dem Geschehen oder viel später?",
                     "**Wozu**? Soll es informieren, loben, rechtfertigen oder Herrschaft begründen?",
                     "**Was** kann man daraus nur vermuten, und was lässt sich **belegen**?",
                     "Beispiele hier: Hammurabis Sammlung (königliche Selbstdarstellung), Augustus' Tatenbericht (Selbstdarstellung), das Perikles-Gemälde von 1852 (späte Darstellung)."]),
             ("hint", "Auch eine Lagemeldung beim Bundesheer ist eine Quelle mit Blickwinkel – sie wird mit anderen Meldungen verglichen, bevor man entscheidet.")]},
 ("jetzt", "Zu den Zusatzaufgaben 9–12", "aufgaben.html#card_a9"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Vorrat bis Staat", "teil2": "Teil 2 · Hammurabi", "teil3": "Teil 3 · Athen und Rom",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

if __name__ == "__main__":
    import re
    for pid, _, _, items in PARTS:
        for it in items:
            if isinstance(it, dict):
                txt = " ".join((x if isinstance(x, str) else " ".join(str(y) for y in x)) for b in it["blocks"] if b[0] in ("ul", "ol", "table", "tiles", "merke", "hint") for x in (b[1] if isinstance(b[1], list) else [b[1]]))
                print(f"{pid:9s} {it['id']:15s} {len(re.findall(r'[A-Za-zÄÖÜäöüß]+', txt)):4d} Wörter")
