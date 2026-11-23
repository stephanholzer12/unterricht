"""Theorie-Seite IWK 5AK · K2.2 Institutionen der Globalisierung: Teile und Folien (eine Quelle für Theorie-Seite und Präsentation).
Block-Arten: tiles, ul, ol, merke, hint, table, video, reveal, img (Datei, Alt-Text, Bildunterschrift), karten, buch (Leseauftrag), link.
Alles in eigenen Worten; Grafiken selbst gezeichnet (skizzen.py). Keine Buchbilder, kein Buchtext auf öffentlichen Seiten.
Aktuelle Zahlen: siehe inhalt.QUELLEN (von Claude am 23.11.2026 geöffnet und geprüft)."""
import inhalt as I

EINSTIEG = [
 {"id": "s0a", "title": "Dein Handy, ein Zoll und eine Stadt in der Schweiz", "pill": "Buch S. 52",
  "blocks": [("ul", ["Stell dir vor, dein nächstes Handy kostet plötzlich 20 % mehr, weil ein Land Zölle auf Elektronik erhebt. Wer sorgt dafür, dass so etwas nach Regeln läuft?",
                     "Oder: Ein Land im Krieg braucht Hunderte Milliarden, um Kraftwerke und Brücken wieder aufzubauen. Wer leiht so viel Geld – und zu welchen Bedingungen?",
                     "Die Antworten führen zu drei Organisationen: der **WTO** in Genf, der **Weltbank** und dem **IWF** in Washington. Sie tauchen fast jede Woche in den Nachrichten auf."]),
             ("hint", "Leitfrage der Einheit: " + I.LEITFRAGE),
             ("buch", "Lies zuerst im Buch S. 52 den Einstieg und schau dir auf S. 53 die Tabelle an. Diese Seite erklärt dasselbe noch einmal anders – mit aktuellen Fällen aus 2026.")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 # ---------------------------------------------------------------- Stunde 1
 ("teil1", "Stunde 1 · " + I.STUNDENTITEL[1] + " · Buch S. 52–53", I.TEILNAME[1], [
  {"id": "ueberblick", "title": "Drei Institutionen, drei Aufgaben", "pill": "Buch S. 53",
   "blocks": [("img", "img/ueberblick.svg", "Drei Säulen nebeneinander. WTO, Genf, 166 Mitglieder: Regeln für den Handel. Weltbank, Washington, 189 Mitglieder: langfristige Kredite für Entwicklung. IWF, Washington, 191 Mitglieder: Hilfe bei Zahlungskrisen.",
               "Eigene Grafik. Faustregel: Handel – Projekte – Zahlungskrise."),
              ("tiles", [("WTO · Welthandelsorganisation", ["Sitz in **Genf**, 166 Mitglieder (dazu zählt auch die EU).", "Macht die **Regeln für den Handel**: Zölle, Dienstleistungen, Patente.", "Schlichtet **Streit** zwischen Handelspartnern."]),
                         ("Weltbank", ["Sitz in **Washington**, 189 Mitglieder.", "Vergibt **langfristige Kredite** für Straßen, Schulen, Kraftwerke, Wiederaufbau.", "Den ärmsten Ländern gibt sie über die **IDA** zinslose oder fast zinslose Kredite, oft auch Zuschüsse."]),
                         ("IWF · Internationaler Währungsfonds", ["Sitz in **Washington**, 191 Mitglieder.", "Hilft Staaten, die ihre Rechnungen im Ausland nicht mehr zahlen können (**Zahlungskrise**).", "Gibt **kurzfristige Kredite** – meist mit **Auflagen**."])]),
              ("ul", ["Weltbank und IWF wurden **1944** in **Bretton Woods** (USA) gegründet. Die Welt sollte nach dem Zweiten Weltkrieg wiederaufgebaut werden, und eine Wirtschaftskrise wie in den 1930er-Jahren sollte sich nicht wiederholen.",
                      "Die WTO gibt es seit **1995**. Vorher gab es seit 1948 das Handelsabkommen **GATT**, das in der WTO aufgegangen ist."]),
              ("merke", "Faustregel: **WTO = Handel** · **Weltbank = Projekte und Entwicklung** · **IWF = Zahlungskrise**.")]},
  {"id": "stimme", "title": "Wer hat das Sagen?", "pill": "Buch S. 55, 58, 62",
   "blocks": [("img", "img/stimme.svg", "Links: In der WTO hat jedes Land eine Stimme, dargestellt durch gleich große Kreise für USA, China, Österreich und Malawi. Rechts: Im IWF ist die Stimme der USA ein großer Balken von rund 16 Prozent, China rund 6 Prozent, Österreich unter 1 Prozent.",
               "Eigene Grafik. Werte für den IWF gerundet nach der Grafik im Buch S. 62."),
              ("tiles", [("WTO: ein Land, eine Stimme", ["Jedes Mitglied hat **eine Stimme** – Österreich so viel wie China.", "Entschieden wird im **Konsens**: Ein Beschluss gilt, wenn kein Mitglied förmlich widerspricht.", "Das heißt aber auch: **Ein einziges Land kann blockieren.**"]),
                         ("IWF und Weltbank: Geld zählt", ["Das Stimmrecht richtet sich nach dem **Kapitalanteil** (im IWF heißt er **Quote**).", "Die USA haben im IWF rund **16 %** der Stimmen, China rund 6 %, Österreich unter 1 % (Buch S. 62).", "Wichtige Beschlüsse im IWF brauchen 85 % der Stimmen. Die USA allein können sie also verhindern."])]),
              ("ul", ["Eine ungeschriebene Regel: Den **Präsidenten der Weltbank** stellen die USA (derzeit Ajay Banga), die **Chefin des IWF** kommt aus Europa (derzeit Kristalina Georgiewa aus Bulgarien). An der Spitze der WTO steht seit 2021 **Ngozi Okonjo-Iweala** aus Nigeria, seit 2025 in ihrer zweiten Amtszeit.",
                      "Das ist wie in einem Verein, in dem die, die am meisten Mitgliedsbeitrag zahlen, auch am meisten mitbestimmen. Ob das fair ist, darüber streiten Fachleute seit Jahrzehnten."]),
              ("merke", "WTO: **gleiche Stimme, aber Blockade möglich**. IWF und Weltbank: **mehr Geld, mehr Stimmen**.")]},
  {"id": "aktuell", "title": "Die WTO 2026: Konferenz ohne Durchbruch", "pill": "Buch S. 55–57",
   "blocks": [("img", "img/streit.svg", "Animation: Zwei Länder streiten über Zölle. Der Streit geht an ein Schiedsgremium der WTO, es fällt ein Urteil. Das unterlegene Land geht in Berufung – doch die Berufungsinstanz ist leer, der Pfeil läuft ins Leere. Das Urteil wird nicht rechtskräftig.",
               "Eigene Animation: So läuft ein Handelsstreit – und wo er seit Ende 2019 hängen bleibt."),
              ("ul", ["Vom 26. bis 30. März 2026 trafen sich die Handelsminister der WTO in **Yaoundé (Kamerun)**. Das Ergebnis war mager: Es gab **keinen Plan für eine Reform** der WTO.",
                      "Zum ersten Mal seit **1998** wurde ein wichtiges Versprechen nicht verlängert: Bis dahin hatten alle zugesagt, **keine Zölle auf digitale Übertragungen** zu erheben (z. B. Downloads, Streaming). Seit 1. April 2026 darf jedes Mitglied selbst entscheiden.",
                      "Die **Streitschlichtung** hat ein großes Loch: Seit Ende 2019 hat die **Berufungsinstanz** keine Richter mehr, weil die USA neue Ernennungen blockieren. Ein Land, das verliert, kann einfach Berufung einlegen – und dann passiert nichts. Als Notlösung haben 61 Mitglieder (darunter die EU) ein eigenes Ersatzverfahren vereinbart."]),
              ("video", "gtai"),
              ("hint", "Quellen: GTAI, 2.4.2026 und World Economic Forum, 29.4.2026. Welche Gruppe macht daraus Folie 2?")]},
  {"id": "geld", "title": "Weltbank und IWF 2026: Milliarden für die Ukraine", "pill": "Buch S. 57–62",
   "blocks": [("img", "img/kredit.svg", "Animation: Ein Staat in der Krise bittet den IWF um Hilfe. Der IWF stellt Bedingungen. Die erste Tranche wird ausgezahlt. Dann prüft der IWF, ob die Auflagen erfüllt sind – erst dann fließt die nächste Tranche.",
               "Eigene Animation: So läuft ein IWF-Kredit – Geld in Stücken, gegen Auflagen."),
              ("tiles", [("Weltbank: Wiederaufbau", ["Die Weltbank hat mit der Ukraine, der EU und der UNO geschätzt, was der Wiederaufbau kostet: **fast 588 Mrd. US-Dollar** in zehn Jahren (Stand der Schäden: Ende 2025).",
                                                   "Das ist fast das **Dreifache** dessen, was die ganze Ukraine 2025 erwirtschaftet hat.", "Am meisten braucht es für Verkehr, Energie und Wohnungen (jeweils 90 bis 96 Mrd.)."]),
                         ("IWF: Geld gegen Reformen", ["Am 26. Februar 2026 hat der IWF der Ukraine einen Kredit über **8,1 Mrd. US-Dollar** für vier Jahre genehmigt, 1,5 Mrd. sofort.",
                                                       "Die Auflagen: mehr **Steuern eintreiben**, **Korruption** bekämpfen, den Wechselkurs flexibler machen.", "Der IWF-Kredit ist eine Art Gütesiegel: Erst damit geben auch andere Geldgeber Geld."])]),
              ("ul", ["Die **USA** sind im Jänner 2026 aus **66** internationalen Organisationen ausgetreten, viele davon für Klima, Bildung und Menschenrechte. In IWF und Weltbank bleiben sie, verlangen aber, dass sich beide auf ihren Kernauftrag konzentrieren. Die Weltbank soll zum Beispiel ihr Ziel streichen, 45 % ihrer Finanzierung für Klimaprojekte (Klimaschutz und Anpassung an den Klimawandel) zu verwenden.",
                      "**Sicherheit:** Wiederaufbau und stabile Staatsfinanzen gehören zur Stabilität Europas – ein Staat, der seine Beamten, Spitäler und Stromnetze nicht mehr bezahlen kann, wird verwundbar. Das ist etwas anderes als Sanktionen: Für Sanktionen sind WTO, Weltbank und IWF **nicht** zuständig."]),
              ("hint", "Quellen: Weltbank, 23.2.2026 · IWF, 26.2.2026 · ZDFheute, 8.1.2026 · US-Finanzministerium, 15.4.2026. Alle Links stehen bei den Gruppenthemen.")]},
  {"id": "raster", "title": "Euer Steckbrief: das Raster", "pill": "Aufgabe 2 · Buch S. 52–63",
   "blocks": [("hint", "Jede Gruppe füllt dasselbe Raster aus. So lassen sich die Vorträge am Ende vergleichen."),
              ("table", [["Punkt", "Was gehört hinein?"]] + [[a, b] for a, b in I.RASTER]),
              ("table", [["Gruppe", "Thema", "Leitfragen", "Einstieg"]] + [[f"{n} · {inst}", thema + " (" + buch + ")", fragen, start] for n, inst, thema, buch, fragen, start in I.GRUPPEN]),
              ("ul", ["Jede Gruppe braucht **mindestens zwei Quellen mit Datum**, eine davon nicht das Buch. Gute Startpunkte sind die Seiten der Organisationen selbst, ORF, APA, ZDF oder die Fachagentur GTAI.",
                      "Teilt euch auf: Zwei suchen Fakten (Punkte 1 bis 4), zwei den aktuellen Fall und die Kritik (Punkte 5 bis 7). Am Ende tragt ihr alles zusammen."]),
              ("hint", "Geprüfte Quellen zum Start (von Prof. HOLZER vorbereitet, Stand 23.11.2026):"),
              ("links", [(f"{x[1]}, {x[2]}: {x[0]}", x[3]) for x in I.QUELLEN])]},
  {"id": "stop1", "title": "Stopp – kannst du das?", "pill": "Buch S. 52–55", "blocks": [("reveal", I.STOPPFRAGEN[1])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 1 und 2", "aufgaben.html#card_a1"),
 ]),

 # ---------------------------------------------------------------- Stunde 2
 ("teil2", "Stunde 2 · " + I.STUNDENTITEL[2], I.TEILNAME[2], [
  {"id": "vortrag", "title": "So geht ein 4-Minuten-Vortrag", "pill": "Aufgabe 2 i)–l)",
   "blocks": [("tiles", [("Folie 1 · Steckbrief", ["Name, Sitz, Mitglieder, Leitung", "Aufgabe in einem Satz", "Wer entscheidet?"]),
                         ("Folie 2 · Der aktuelle Fall", ["**Eine Zahl groß** in die Mitte", "Was ist passiert? Wann?", "Quelle mit Datum unten"]),
                         ("Folie 3 · Kritik und Streitfrage", ["Kritik an der Institution und was sie antwortet", "Eine Frage an die Klasse, z. B. »Soll …?«", "Eure Meinung in einem Satz"])]),
              ("ul", ["**Wenig Text.** Höchstens fünf Zeilen pro Folie, keine ganzen Sätze. Was ihr sagt, steht nicht auf der Folie – sonst liest das Publikum statt zuzuhören.",
                      "**Rollen verteilen:** Jeder spricht etwa eine Minute. Eine Person achtet auf die Zeit, eine wechselt die Folien.",
                      "**Erst Papier, dann Gerät:** Skizziert die drei Folien zuerst mit der Hand auf ein Blatt. Das geht schneller, und ihr seht sofort, ob es zu voll ist.",
                      "**Abgabe:** Eine Person pro Gruppe lädt die Folien in LMS hoch. Dateiname: Gruppe-Nummer-Thema, z. B. »Gruppe-3-Weltbank«."]),
              ("merke", "Drei Folien, eine Zahl, eine Frage – und nicht ablesen.")]},
  {"id": "quellen", "title": "Quellen prüfen: Wer sagt das?", "pill": "Aufgabe 2 h)",
   "blocks": [("ul", ["Die **Webseite einer Organisation** ist gut für Fakten: Mitglieder, Beschlüsse, Zahlen. Aber wenn die Weltbank über die Weltbank schreibt, ist das **keine unabhängige Bewertung**.",
                      "Für **Kritik** braucht ihr eine zweite Quelle: eine Zeitung, eine Hilfsorganisation, eine Universität. Auch die hat einen Blickwinkel – schreibt dazu, wer es ist.",
                      "**Datum prüfen:** Das Buch hat den Stand 2025. Mitgliederzahlen, Chefs und Fälle ändern sich. Auf die Folie kommt immer der Stand, z. B. »Stand: Februar 2026«.",
                      "Widersprechen sich zwei Quellen (etwa beim Datum einer Konferenz), nennt beide oder nehmt nur, was beide gleich sagen."]),
              ("hint", "Auch im Bundesheer gilt: Eine Lagemeldung wird mit einer zweiten Meldung verglichen, bevor man entscheidet.")]},
  {"id": "stop2", "title": "Stopp – kannst du das?", "pill": "Aufgabe 2", "blocks": [("reveal", I.STOPPFRAGEN[2])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2, Teil 2", "aufgaben.html#card_a2"),
 ]),

 # ---------------------------------------------------------------- Stunde 3
 ("teil3", "Stunde 3 · " + I.STUNDENTITEL[3] + " · Buch S. 57, 60–63", I.TEILNAME[3], [
  {"id": "vergleich", "title": "WTO, Weltbank und IWF im Vergleich", "pill": "Buch S. 53–62",
   "blocks": [("table", [["", "WTO", "Weltbank", "IWF"],
                         ["Aufgabe", "Regeln für den Handel, Streit schlichten", "langfristige Kredite für Entwicklung und Wiederaufbau", "kurzfristige Kredite bei Zahlungskrisen, Geldpolitik überwachen"],
                         ["Sitz · Mitglieder", "Genf · 166", "Washington · 189", "Washington · 191"],
                         ["Wer entscheidet?", "jedes Mitglied eine Stimme, Konsens", "Stimmen nach Kapitalanteil", "Stimmen nach Quote (Kapitalanteil)"],
                         ["Werkzeug", "Abkommen (GATT, GATS, TRIPS), Streitschlichtung", "Kredite, Beratung, (fast) zinslose IDA-Kredite und Zuschüsse", "Kredite mit Auflagen"],
                         ["Fall 2026", "Zollverbot für digitale Übertragungen ausgelaufen", "Wiederaufbau Ukraine: fast 588 Mrd. US-Dollar", "Ukraine: 8,1 Mrd. US-Dollar mit Auflagen"]]),
              ("hint", "Diese Tabelle ist die Lösung zu Aufgabe 3 a) – füll sie zuerst selbst während der Vorträge aus.")]},
  {"id": "kritik", "title": "Kritik – und was dahintersteckt", "pill": "Buch S. 57, 60–62",
   "blocks": [("tiles", [("WTO", ["**Kritik:** Seit dem Scheitern der Doha-Runde kommen kaum neue Regeln zustande, die Streitschlichtung ist halb gelähmt.", "**Gegenargument:** Ohne WTO gäbe es gar keine gemeinsamen Regeln. Fast der ganze Welthandel läuft unter WTO-Regeln."]),
                         ("Weltbank", ["**Kritik:** Armut ist trotz Jahrzehnten nicht besiegt. Großprojekte wie Staudämme haben Menschen vertrieben und Natur zerstört.", "**Gegenargument:** Die Weltbank hat Schutzregeln eingeführt und finanziert, was private Banken zu riskant finden – etwa den Wiederaufbau im Krieg."]),
                         ("IWF", ["**Kritik:** Die Auflagen (Sparen, Privatisieren) haben in vielen Ländern Arme getroffen, zum Beispiel in Griechenland. Reiche Länder bestimmen mit.", "**Gegenargument:** Ohne Auflagen fließt das Geld vielleicht in Korruption. Und ohne den IWF hätten Länder in der Krise oft gar niemanden, der ihnen Geld leiht."])]),
              ("ul", ["Der Wirtschaftsnobelpreisträger **Joseph Stiglitz**, den du aus K2.1 kennst, hat besonders den IWF scharf kritisiert. Sogar Ökonomen des IWF haben 2016 eingeräumt, dass zu strenges Sparen in der Krise schaden kann (Buch S. 62).",
                      "Ein gutes Urteil hat drei Teile: **Meinung** (»Ich finde …«), **Grund** (»weil …«) und **Gegenargument** (»Allerdings …«)."]),
              ("merke", "Kritik ist nicht gleich Kritik: Bei der WTO geht es um **Blockade**, bei der Weltbank um **Wirkung**, beim IWF um **Auflagen**.")]},
  {"id": "stop3", "title": "Stopp – kannst du das?", "pill": "Buch S. 57–62", "blocks": [("reveal", I.STOPPFRAGEN[3])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3", "aufgaben.html#card_a3"),
 ]),
]

SCHNELLE = [
 {"id": "partnercheck", "title": "Partnercheck – Karten zum Wiederholen", "pill": "Buch S. 52–63",
  "blocks": [("hint", "Zu zweit: Einer liest die Frage, der andere antwortet, dann Antwort aufdecken und abhaken."), ("karten", I.PARTNERKARTEN)]},
 {"id": "stolpern", "title": "Fünf Stolpersteine", "pill": "Zum Nachdenken", "blocks": [("karten", I.STOLPERSTEINE)]},
 {"id": "mehr", "title": "Noch mehr wissen: Warum ein einziges Land die WTO bremsen kann", "pill": "Zusatztheorie · Aufgabe 7",
  "blocks": [("ul", ["Auf der Konferenz in Kamerun wollten fast alle Mitglieder ein Abkommen aufnehmen, das Investitionen in Entwicklungsländern erleichtert. "
                     "Laut EU-Kommission war nur **Indien** dagegen – und weil die WTO im **Konsens** entscheidet, kam es nicht in das Regelwerk.",
                     "Die Mitglieder weichen deshalb immer öfter aus: Wer mitmachen will, schließt ein **Abkommen unter Gleichgesinnten** ab. "
                     "66 Mitglieder haben das 2026 für den elektronischen Handel getan. Es gilt dann aber nur zwischen ihnen.",
                     "Fachleute streiten, ob das die WTO rettet oder langsam zerlegt: Es geht schneller, aber es gibt nicht mehr **eine** Regel für alle."]),
             ("link", ["GTAI: Die 14. Ministerkonferenz der Welthandelsorganisation (2.4.2026)", I.LESE_LINK]),
             ("hint", "Lies den Bericht selbst und mach dann Aufgabe 7. Achte darauf, wer ihn geschrieben hat und für wen – und vergleiche das Datum der Konferenz mit dieser Seite.")]},
 ("jetzt", "Zu den Zusatzaufgaben 5–7", "aufgaben.html#card_a5"),
]

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Überblick", "teil2": "Teil 2 · Vortrag", "teil3": "Teil 3 · Vergleich",
          "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

if __name__ == "__main__":
    import re
    for pid, _, _, items in PARTS:
        for it in items:
            if isinstance(it, dict):
                txt = " ".join((x if isinstance(x, str) else " ".join(str(y) for y in x)) for b in it["blocks"] if b[0] in ("ul", "ol", "table", "tiles", "merke", "hint") for x in (b[1] if isinstance(b[1], list) else [b[1]]))
                print(f"{pid:9s} {it['id']:15s} {len(re.findall(r'[A-Za-zÄÖÜäöüß]+', txt)):4d} Wörter")
