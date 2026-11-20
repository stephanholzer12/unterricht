"""Theorie-Seite K6–7 Wahlrecht und Parteien (2AK): Theorie-Karten, Teile und Abschnitte.
Dieselben Daten füttern die Theorie-Seite, die Tipp-Stufe 2 im Arbeitsblatt (Theorie-Karte) und die Präsentation der Lösungsseite.
Block-Arten: tiles, ul, ol, merke, hint, table, reveal, img (Datei, Alt, Unterschrift), buch, karte, gemeinsam, sim.
Alles in eigenen Worten; alle Grafiken selbst gezeichnet (skizzen.py, SVG). Das Schulbuch wird gelesen – die Seite erklärt anders und ergänzt.
Parteien: nur Buchbeschreibung (S. 35, als Fremdbeschreibung gekennzeichnet) und geprüfte Fakten (Gründung, Mandate). Keine Wertung."""
import inhalt as I

TOCLAB = {"einstieg": "Start", "wahlrecht": "1 Wahlrecht", "lager": "2 Drei Lager", "partei": "3 Parteien", "richtung": "4 Links/rechts",
          "heute": "5 Heute", "pruefen": "6 Faktencheck", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}

KARTEN = {
 "k1": {"titel": "Wahlrecht in Etappen", "teil": "wahlrecht", "buch": "Buch S. 23–26", "bild": "img/wahlrecht.svg",
        "alt": "Zeitleiste von 1861 bis 2007. Bei jedem Schritt werden mehr Figuren farbig: 1861 nur wenige reiche Männer, 1873 Männer mit Steuer, 1896 auch Arbeiter mit schwacher Stimme, 1907 alle Männer ab 24, 1918 auch Frauen, 1933 bis 1945 alle grau – keine freien Wahlen, 2007 auch Jugendliche ab 16.",
        "satz": ["Zuerst durfte nur wählen, wer **Besitz** hatte (**Kurienwahlrecht 1861**) oder genug **Steuer** zahlte (**Zensuswahlrecht 1873**, nur ca. 6 % der Männer).",
                 "**1907** kam das **allgemeine, gleiche** Wahlrecht – aber nur für **Männer ab 24**. Die **Frauen** folgten **1918**.",
                 "**1933–1945** gab es **keine freien Wahlen**. Seit **2007** wählst du ab **16**."],
        "formeln": [("allgemein", "alle Staatsbürger ab einem Alter", ""), ("gleich", "jede Stimme zählt gleich", ""), ("direkt · geheim", "selbst wählen · niemand schaut zu", "")],
        "link": "theorie.html#wahlrecht"},
 "k2": {"titel": "Drei Lager um 1900", "teil": "lager", "buch": "Buch S. 27–30", "bild": "img/lager.svg",
        "alt": "Drei Spalten. Links das liberale, später deutschnationale Lager (Bürgertum der Städte), in der Mitte das christlichsoziale Lager (Kirche, Bauern, Kleinbürger), rechts das sozialdemokratische Lager (Arbeiter). Pfeile führen zu den Parteien von heute: FPÖ (1956), ÖVP (1945), SPÖ (1945). Darunter neu dazugekommen: Grüne (1986 im Nationalrat) und NEOS (2012).",
        "satz": ["Mit dem Wahlrecht von 1907 wurden die Parteien groß. Es entstanden **drei Lager**: **deutschnational**, **christlichsozial** und **sozialdemokratisch**.",
                 "Hinter jedem Lager standen andere Menschen: **Bürger** der Städte, **Kirche, Bauern und Kleinbürger**, **Arbeiterinnen und Arbeiter**.",
                 "Aus den Lagern kommen **FPÖ**, **ÖVP** und **SPÖ**. **Grüne** und **NEOS** sind neu dazugekommen."],
        "formeln": [("christlichsozial", "→ ÖVP (1945)", ""), ("sozialdemokratisch", "→ SPÖ (1945)", ""), ("deutschnational", "→ FPÖ (1956)", "")],
        "link": "theorie.html#lager"},
 "k3": {"titel": "Was Parteien tun", "teil": "partei", "buch": "Buch S. 31–32", "bild": "img/partei.svg",
        "alt": "Links vier Aufgaben einer Partei als Symbole: Macht im Staat, Programm umsetzen, Leute für Ämter heranbilden, Menschen für Politik interessieren. Rechts woher das Geld kommt: Mitgliedsbeiträge, Förderung vom Staat, Klubförderung, Spenden, Beiträge der Abgeordneten.",
        "satz": ["Eine **Partei** ist schnell gegründet: **Satzung beim Innenministerium** hinterlegen. Sie darf nicht gegen den Staat gerichtet sein.",
                 "Parteien wollen **Macht** im Staat, ihr **Programm** umsetzen und Menschen für **Politik** gewinnen.",
                 "Im Nationalrat bilden **5 Abgeordnete** einer Partei einen **Klub**. Parteien bekommen **Geld vom Staat**, damit sie nicht von großen Spendern abhängen."],
        "formeln": [("Klub", "ab 5 Abgeordneten", ""), ("Nationalrat", "183 Mandate", ""), ("Mehrheit", "ab 92 Mandaten", "")],
        "link": "theorie.html#partei"},
 "k4": {"titel": "Links, rechts, liberal", "teil": "richtung", "buch": "Buch S. 32–33", "bild": "img/sitzordnung.svg",
        "alt": "Halbkreis eines Parlaments von 1789 von oben. Links sitzen die Revolutionären, rechts die Königstreuen. Darunter eine Linie von links nach rechts mit den Begriffen egalitär, progressiv, internationalistisch auf der linken und elitär, konservativ, nationalistisch auf der rechten Seite. Oben quer darüber: liberal.",
        "satz": ["Die Wörter kommen aus **Frankreich 1789**: **links** saßen die Revolutionären, **rechts** die Königstreuen.",
                 "**Links** steht eher für **egalitär, progressiv, internationalistisch**, **rechts** eher für **elitär, konservativ, nationalistisch** (Buch S. 32).",
                 "**Liberal** heißt: möglichst viel **Freiheit** für den Einzelnen – das passt auf keine Seite ganz."],
        "formeln": [("egalitär", "gleiche Rechte und Chancen für alle", ""), ("konservativ", "Bewährtes bewahren", ""), ("progressiv", "Neues durchsetzen", "")],
        "link": "theorie.html#richtung"},
 "k5": {"titel": "Parteien im Nationalrat heute", "teil": "heute", "buch": "Buch S. 33–35", "bild": "img/nationalrat.svg",
        "alt": "Halbkreis mit 183 Sitzen in Klubfarben: FPÖ 57, ÖVP 51, SPÖ 41, NEOS 17, Grüne 16 und ein Abgeordneter ohne Klub (grau). Darunter: Regierung aus ÖVP, SPÖ und NEOS; Mehrheit ab 92.",
        "satz": ["Im Nationalrat sitzen **fünf Klubs**: **FPÖ, ÖVP, SPÖ, NEOS, Grüne**. Die **KPÖ** steht im Buch, sitzt aber **nicht** im Nationalrat.",
                 "Seit **März 2025** regieren **ÖVP, SPÖ und NEOS** gemeinsam (Koalition). Für eine **Mehrheit** braucht man **92** von 183 Mandaten.",
                 "Die Beschreibungen im Buch S. 35 sind **Fremdbeschreibungen** des Buchs – die Parteien selbst sehen sich oft anders."],
        "formeln": [("Wahl 2024", "FPÖ 57 · ÖVP 51 · SPÖ 41 · NEOS 18 · Grüne 16", ""), ("Klubs Herbst 2026", "NEOS 17, 1 Abgeordneter ohne Klub", "")],
        "link": "theorie.html#heute"},
 "k6": {"titel": "Faktencheck mit vier Fragen", "teil": "pruefen", "buch": "Buch S. 34", "bild": "img/quellencheck.svg",
        "alt": "Vier Fragen als Schilder mit Ampel: Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere, unabhängige Quellen? Darunter eine Ampel grün, gelb, rot.",
        "satz": ["Prüf jede Aussage über Parteien mit **vier Fragen**: **Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere?**",
                 "Eine **Ja/Nein-Tabelle** vereinfacht stark. Eine **Umfrage** ist eine Momentaufnahme – keine **Wahl**.",
                 "Was im Nationalrat gesagt wurde, steht beim **Parlament** selbst. Und eine **KI** kann sich irren – genau wie ein Schulbuch."],
        "formeln": [("grün", "glaubwürdig", ""), ("gelb", "vorsichtig, mehr prüfen", ""), ("rot", "nicht verwenden", "")],
        "link": "theorie.html#pruefen"},
 "k8": {"titel": "Alles auf einen Blick", "teil": "kurz", "buch": "Buch S. 23–35", "bild": "img/ueberblick.svg",
        "alt": "Übersicht in drei Bändern: oben das Wahlrecht von 1861 bis 2007, in der Mitte drei Lager mit Pfeilen zu ÖVP, SPÖ und FPÖ und daneben Grüne und NEOS, unten die Linie links – Mitte – rechts mit liberal darüber.",
        "satz": ["**Wahlrecht:** 1861 Besitz · 1873 Steuer · 1907 Männer · 1918 Frauen · 2007 ab 16.",
                 "**Lager → Parteien:** christlichsozial → ÖVP · sozialdemokratisch → SPÖ · deutschnational → FPÖ; neu: Grüne, NEOS.",
                 "**Richtungen:** links eher egalitär, rechts eher konservativ, liberal = Freiheit. **Quellen prüfen!**"],
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
 {"id": "s0a", "title": "Wer darf mitreden?", "pill": "Buch S. 23",
  "blocks": [("img", "img/ueberblick.svg", KARTEN["k8"]["alt"], "Der Weg dieser Einheit: Wahlrecht, drei Lager, Parteien von heute – und wie man Aussagen über sie prüft."),
             ("ul", ["**Das Wichtigste vorab:** Du darfst ab 16 wählen. Das war nicht immer so – Menschen haben über 150 Jahre dafür gekämpft. Und die Parteien auf deinem Stimmzettel haben Wurzeln, die bis in die Zeit des Kaisers zurückreichen.",
                     "**Wozu?** Bei der nächsten Nationalratswahl stehen auf deinem Stimmzettel Parteien. Wer weiß, wofür sie stehen und woher sie kommen, fällt weniger auf Werbung und Gerüchte herein.",
                     "**Und im Dienst?** Das Bundesheer ist auf die Verfassung angelobt, nicht auf eine Partei. Über sein Geld entscheidet der Nationalrat – also die Parteien. Darum lohnt es sich, ihre Positionen zu kennen und genau zu prüfen.",
                     "**Das kannst du nachher:** die Geschichte des Wahlrechts erzählen, die Parteien ihren Lagern und Richtungen zuordnen und Aussagen über Parteien mit Quellen prüfen."]),
             ("hint", "Du arbeitest im Arbeitsblatt – diese Seite ist zum Nachschlagen.")]},
 {"id": "s0b", "title": "Film oder Geschichte? »So stirbt die Freiheit«", "pill": "Buch S. 26",
  "blocks": [("tiles", [("Im Film", ["In »Star Wars: Episode III« bekommt der Kanzler im Senat Sondervollmachten. Die Abgeordneten jubeln. Eine Senatorin sagt sinngemäß: So stirbt die Freiheit – unter donnerndem Applaus."]),
                        ("In Wirklichkeit", ["Auch in Österreich endete die Demokratie nicht mit einem Knall. 1933 nutzte Bundeskanzler Dollfuß eine Krise im Parlament, um ohne Parlament weiterzuregieren. Danach gab es bis 1945 **keine freien Wahlen** (Buch S. 25–26)."])]),
             ("ul", ["**Kleine Geschichte:** Am 28. November 1905 demonstrierten in Wien riesige Menschenmassen für ein gleiches Wahlrecht. Zwei Jahre später, 1907, durften alle Männer ab 24 gleich wählen (Foto im Buch S. 25).",
                     "**Offene Frage der Forschung:** Macht Wählen ab 16 junge Menschen dauerhaft zu fleißigeren Wählern? Erste Studien aus Österreich sagen: Beim ersten Mal gehen 16-Jährige öfter wählen als 18-Jährige. Ob das ein Leben lang so bleibt, weiß man noch nicht genau."]),
             ("merke", "Filme hier nur in Worten – keine Filmbilder auf dieser Seite (Urheberrecht).")]},
]

PARTS = [
 ("einstieg", "Zum Start", "Einstieg", EINSTIEG),

 ("wahlrecht", "Teil 1 · Buch S. 23–26 · Stunde 1", "Wahlrecht – ein langer Weg", [
  {"id": "wahlrecht", "title": "Vom Kaiser zum Wählen mit 16", "pill": "Buch S. 23–26",
   "blocks": [("buch", "Lies im **Buch S. 23** die Zeitleiste »Überblick über die Entwicklung des Wahlrechts in Österreich« (3 min). Markiere die zwei Jahre, in denen die meisten Menschen neu dazukamen."),
              kartenblock("k1"),
              ("table", [["Jahr", "Was war neu?", "Wer durfte wählen?"],
                         ["1848", "Revolution gegen den Kaiser – niedergeschlagen", "kurz ein gewählter Reichstag, dann wieder keiner"],
                         ["1861", "**Kurienwahlrecht** (Februarpatent, erstes Parlament)", "Männer ab 24 mit **Besitz**, in vier Gruppen (Kurien)"],
                         ["1873", "**Zensuswahlrecht**", "nur wer genug **Steuer** zahlt – ca. 6 % der Männer"],
                         ["1896", "**5. Kurie**", "auch ärmere Männer – aber ihre Stimme zählt viel weniger"],
                         ["1907", "**allgemeines, gleiches, direktes, geheimes** Wahlrecht", "alle **Männer** ab 24"],
                         ["1918", "Ende der Monarchie, Republik", "auch die **Frauen** – erste Wahl im Februar 1919"],
                         ["1933–1945", "Diktatur, dann NS-Herrschaft", "**keine freien Wahlen**"],
                         ["1945", "Zweite Republik", "ehemalige NSDAP-Mitglieder großteils ausgeschlossen"],
                         ["1949 · 1968 · 1992", "Wahlalter sinkt", "ab 20 · ab 19 · ab 18"],
                         ["2007", "Wahlrechtsreform", "ab **16**; dazu **Briefwahl** für alle"]]),
              ("sim", "zeitmaschine"),
              ("tiles", [("Frauen kämpfen mit", ["Schon 1913 demonstrierten Frauen in Wien für ihr Wahlrecht (Foto im Buch S. 25). Es dauerte noch fünf Jahre."]),
                         ("Andere Länder", ["Finnland 1906 als Erstes in Europa, Deutschland 1918, die **Schweiz erst 1971** – dort mussten die Männer per Volksabstimmung zustimmen."]),
                         ("Wählen mit 16", ["Seit 2007 bei Nationalratswahlen. 16- und 17-Jährige gehen beim ersten Mal sogar öfter wählen als 18- bis 20-Jährige (Studie Uni Wien, 2014)."])]),
              ("merke", "**Quellenkritik:** Das Buch schreibt bei 1918 »Wahlalter 21«. Für die Wahl **1919** galt aber **20** (Demokratiezentrum Wien, politik-lexikon.at). Auch Schulbücher können sich irren – darum eine dritte Quelle prüfen."),
              ("reveal", I.STOPPFRAGEN["wahlrecht"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 2", "aufgaben.html#card_a1"),
 ]),

 ("lager", "Teil 2 · Buch S. 27–30 · Stunde 2", "Drei Lager – wie unsere Parteien entstanden", [
  {"id": "lager", "title": "Bürger, Kirche, Arbeiter", "pill": "Buch S. 27–30",
   "blocks": [("buch", "**GRUPPENPUZZLE:** Jede Expertengruppe liest im **Buch S. 27–30** ihren Abschnitt: »Von liberal zu deutschnational(istisch)« · »Von katholischen Vereinen zur Christlichsozialen Partei« · »Vom Arbeiterbildungsverein zur Sozialdemokratischen Partei«."),
              kartenblock("k2"),
              ("tiles", [("Liberal → deutschnational", ["Getragen vom **wohlhabenden Bürgertum** der Städte – Fabrikanten, Ärzte, Anwälte. Sie wollten **Freiheit** für Wirtschaft und Einzelne und gründeten viele **Vereine** (Turner, Feuerwehr, Gesang).",
                                                        "Später wurde daraus eine **deutschnationale** Bewegung: Georg von **Schönerer** wollte den Anschluss an das Deutsche Reich. Viele Vereine schlossen Juden aus (»Arierparagrafen«) – **rassistischer Antisemitismus**."]),
                         ("Christlichsozial", ["Aus **katholischen Vereinen** (z. B. Kolping) entstand **1891** die **Christlichsoziale Partei** (Vogelsang, Lueger). Sie sprach **Kleinbürger, Handwerker und Bauern** an.",
                                               "Karl **Lueger** baute als Wiener Bürgermeister Wasserleitung, Gaswerk und Bäder – und hetzte zugleich offen gegen Juden."]),
                         ("Sozialdemokratisch", ["Aus **Arbeiterbildungsvereinen** wurde eine Bewegung der **Arbeiterinnen und Arbeiter**. Der Arzt Victor **Adler** einigte sie beim Parteitag in **Hainfeld (1888/89)**.",
                                                 "Mit **Massendemonstrationen** erkämpften sie das **Männerwahlrecht 1907**."])]),
              ("table", [["Lager um 1900", "Partei heute", "gegründet"],
                         ["christlichsozial", "ÖVP", "1945"], ["sozialdemokratisch", "SPÖ", "1945 (neu gegründet)"],
                         ["deutschnational (»drittes Lager«)", "FPÖ", "1956 (Vorgänger VdU)"],
                         ["neu: Umweltbewegung", "Grüne", "seit 1986 im Nationalrat"], ["neu: liberal", "NEOS", "2012"]]),
              ("hint", "Bundesheer-Brücke: Das Denkmal des Waffenfabrikanten Josef Werndl in Steyr (Foto Buch S. 27) zeigt einen liberalen Unternehmer – seine Fabrik baute Gewehre für die k. u. k. Armee."),
              ("reveal", I.STOPPFRAGEN["lager"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 3", "aufgaben.html#card_a2"),
 ]),

 ("partei", "Teil 3 · Buch S. 31–32 · Stunde 2", "Was Parteien tun – und wer sie bezahlt", [
  {"id": "partei", "title": "Partei gründen, Programm schreiben, Klub bilden", "pill": "Buch S. 31–32",
   "blocks": [("buch", "Lies im **Buch S. 31** die vier Fragen »Wie entsteht eine Partei?« bis »Wie finanziert sich eine Partei?« (5 min)."),
              kartenblock("k3"),
              ("ul", ["**Gründen:** Die **Satzung** wird beim **Innenministerium** hinterlegt. Die Partei darf sich nicht gegen den Staat richten und kein nationalsozialistisches Gedankengut verbreiten.",
                      "**Ziele:** Macht im Staat übernehmen, das **Parteiprogramm** umsetzen, Menschen für politische Ämter **heranbilden**, Menschen für Politik interessieren.",
                      "**Programm:** Darin stehen die Positionen zu Familie, Umwelt, Wirtschaft, Sicherheit … Vor Wahlen wird ausgewählt und zugespitzt – das ist Werbung.",
                      "**Geld:** Mitgliedsbeiträge, **Parteienförderung** vom Staat, **Klubförderung**, Spenden und Beiträge der Abgeordneten. Die staatliche Förderung soll Parteien **unabhängig** von großen Spendern machen.",
                      "**Klub:** Mindestens **5 Abgeordnete** derselben Partei bilden im Nationalrat einen Klub. Klubs sind die Arbeitsgruppen des Parlaments (Buch S. 32)."]),
              ("hint", "Die Spendenregeln und Förderbeträge im Buch (S. 31) stammen von 2019 bzw. 2022 – sie haben sich seither geändert. Für aktuelle Zahlen: Rechnungshof."),
              ("reveal", I.STOPPFRAGEN["partei"])]},
 ]),

 ("richtung", "Teil 4 · Buch S. 32–33 · Stunde 3", "Links, rechts, liberal", [
  {"id": "richtung", "title": "Woher links und rechts kommen", "pill": "Buch S. 32–33",
   "blocks": [("buch", "Lies im **Buch S. 32** den Abschnitt »Was bedeutet rechts, links, liberal?« und S. 33 den Absatz über den Liberalismus."),
              kartenblock("k4"),
              ("table", [["Begriff", "heißt", "Beispiel-Frage"],
                         ["egalitär", "alle sollen möglichst gleiche Rechte und Chancen haben", "Sollen alle die gleiche Schule besuchen?"],
                         ["elitär", "Leistung und Können dürfen Unterschiede machen", "Sollen die Besten gefördert werden?"],
                         ["progressiv", "Gesellschaft verändern, Neues durchsetzen", "Soll man Gesetze an neue Lebensformen anpassen?"],
                         ["konservativ", "Bewährtes bewahren", "Soll Tradition mehr zählen als Mode?"],
                         ["internationalistisch", "über Grenzen hinweg zusammenarbeiten", "Sollen Staaten mehr gemeinsam entscheiden?"],
                         ["nationalistisch", "das eigene Volk zuerst", "Soll der eigene Staat immer Vorrang haben?"]]),
              ("ul", ["**Liberal** passt auf keine Seite ganz: gleiche **Rechte** für alle (egalitär) – aber wer mehr leistet, soll mehr haben dürfen (elitär).",
                      "Die Linie geht weiter: **linksextrem – linksradikal – links – Mitte – rechts – rechtsradikal – rechtsextrem** (Buch S. 32). Demokratische Parteien links und rechts stehen auf dem Boden der Verfassung; Extremismus ist ein eigenes Thema (Buch S. 135).",
                      "Echte Wählerinnen und Wähler sind schwer einzuteilen: Viele wechseln von Wahl zu Wahl (Buch S. 33). Und bei Sicherheitsfragen – etwa Neutralität oder Bundesheer – verlaufen die Linien oft quer zu links und rechts."]),
              ("gemeinsam", "**Aufstellen im Raum:** Prof. HOLZER liest Begriffe vor (z. B. »konservativ«). Stell dich auf der Linie dorthin, wo der Begriff laut Buch hingehört. Es geht um die Begriffe – nicht um deine eigene Meinung."),
              ("reveal", I.STOPPFRAGEN["richtung"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgabe 4", "aufgaben.html#card_a3"),
 ]),

 ("heute", "Teil 5 · Buch S. 33–35 · Stunde 3", "Die Parteien im Nationalrat heute", [
  {"id": "heute", "title": "Fünf Klubs, eine Regierung aus drei Parteien", "pill": "Buch S. 33–35",
   "blocks": [kartenblock("k5"),
              ("table", [["Partei", "Wurzel", "laut Buch S. 35 (Fremdbeschreibung)", "Mandate Wahl 2024"],
                         ["FPÖ", "deutschnationales Lager, gegründet 1956", "rechtspopulistisch, nationalistisch, konservativ", "57"],
                         ["ÖVP", "christlichsoziales Lager, gegründet 1945", "konservativ, christlich-demokratisch, wirtschaftsliberal", "51"],
                         ["SPÖ", "sozialdemokratisches Lager, gegründet 1945", "sozialdemokratisch, progressiv, sozialistisch", "41"],
                         ["NEOS", "liberal, gegründet 2012", "liberal, pro-europäisch, wirtschaftsliberal", "18 (Klub heute 17)"],
                         ["Grüne", "Umweltbewegung, seit 1986 im Nationalrat", "ökologisch, sozial, progressiv", "16"]]),
              ("ul", ["**Regierung:** Seit **3. März 2025** regieren **ÖVP, SPÖ und NEOS** (Bundeskanzler Christian Stocker, ÖVP). FPÖ und Grüne sind in **Opposition**.",
                      "**Neu im Herbst 2026:** Andreas Babler gibt den **SPÖ-Vorsitz** ab. Ab Anfang 2027 führen Philip Kucher und Eva-Maria Holzleitner die Partei übergangsweise; ein Parteitag im Frühjahr 2027 wählt die neue Spitze. Finanzminister Markus Marterbauer soll Vizekanzler werden (Stand Oktober 2026 – Prof. HOLZER sagt dir, was sich seither getan hat).",
                      "**NEOS-Klub:** Im Juli 2026 wurde der Abgeordnete Veit Dengler aus Klub und Partei ausgeschlossen. Sein **Mandat** behält er – Sitze gehören den gewählten Personen. Darum hat der NEOS-Klub heute 17 statt 18 Abgeordnete.",
                      "**Die KPÖ** steht im Buch (S. 35), hat bei der Wahl 2024 aber die **4-Prozent-Hürde** nicht geschafft – sie sitzt **nicht** im Nationalrat.",
                      "**Umfragen** sehen derzeit die FPÖ klar vorne. Eine Umfrage ist aber eine **Momentaufnahme** mit Schwankungsbreite – Sitze gibt es nur nach einer echten **Wahl**."]),
              ("sim", "mehrheit"),
              ("merke", "Die Beschreibungen in der Tabelle stammen vom **Buch**, nicht von den Parteien. Was eine Partei selbst will, steht in ihrem **Parteiprogramm** auf ihrer eigenen Website (Buch S. 34) – und was sie im Parlament tatsächlich tut, beim **Parlament**."),
              ("reveal", I.STOPPFRAGEN["heute"])]},
 ]),

 ("pruefen", "Teil 6 · Buch S. 34 · Stunde 4", "Faktencheck: Was stimmt über unsere Parteien?", [
  {"id": "pruefen", "title": "Schulbuch, Parlament, Umfrage, KI", "pill": "Buch S. 34",
   "blocks": [kartenblock("k6"),
              ("tiles", [("Ja/Nein-Tabelle (Buch S. 34)", ["Die Tabelle sagt bei den Grünen »Nein« zu mehr Geld fürs Bundesheer. Im **Juni 2025** nannte der Grünen-Abgeordnete David Stögmüller im Nationalrat den Anstieg des Heeresbudgets »richtig und wichtig« – er kritisierte aber, wofür das Geld ausgegeben wird (Parlamentskorrespondenz Nr. 564).",
                                                              "Lehre: **Zustimmung zur Erhöhung** ist nicht dasselbe wie **Zustimmung zu jeder Ausgabe**. Ja/Nein-Tabellen ohne Datum vereinfachen stark → **gelb**."]),
                         ("Heeresbudget 2025/26", ["Der Nationalrat beschloss für die Landesverteidigung **4,39 Mrd. €** (2025) und **4,76 Mrd. €** (2026). Über das Geld des Bundesheeres entscheiden die Parteien im Nationalrat."]),
                         ("KI-Antworten", ["Chatbots klingen sicher – auch wenn sie sich irren. Typisch: veraltete Zahlen (»sechs Parteien im Nationalrat«) oder verwechselte Jahre. Prüfe sie wie jede andere Quelle."])]),
              ("ol", ["**Wer sagt das?** Person, Partei, Medium, Behörde?",
                      "**Woher weiß er das?** Protokoll, Abstimmung, Studie – oder nur Meinung?",
                      "**Was hat er davon?** Stimmen, Klicks, Geld?",
                      "**Was sagen andere, unabhängige Quellen?** Mindestens eine zweite Quelle – am besten das Parlament selbst."]),
              ("gemeinsam", "**Statement-Ampel im Raum:** Prof. HOLZER liest eine Aussage vor. Stell dich in eine Zone: **stimmt · unklar · stimmt nicht**. Dann prüft ihr in Gruppen die Quelle und stellt euch neu auf. Wer wechselt, sagt in einem Satz warum."),
              ("reveal", I.STOPPFRAGEN["pruefen"])]},
  ("jetzt", "Jetzt im Arbeitsblatt: Aufgaben 5 bis 7", "aufgaben.html#card_a4"),
 ]),
]

SCHNELLE = [
 {"id": "sch1", "title": "Zusatz: Forschung, Hainfeld, Wahlplakat, Mehrheit", "pill": "OPTIONAL",
  "blocks": [("ul", ["**Zusatz 8 – Forschung:** Wählen 16-Jährige wirklich seltener? Eine Studie der Uni Wien sagt etwas anderes.",
                     "**Zusatz 9 – Hainfeld 1889:** Was wollten die Sozialdemokraten damals – und was ist heute selbstverständlich?",
                     "**Zusatz 10 – Kreativ:** Erfinde eine Partei und gestalte ihr Wahlplakat.",
                     "**Zusatz 11 – Mehrheit gesucht:** Wer kommt mit wem auf 92 Mandate?"]),
             ("tiles", [("Gewusst?", ["1970 wurde der Nationalrat von 165 auf **183** Sitze vergrößert (Parlament, 2024)."]),
                        ("Zweidrittelmehrheit", ["Für Verfassungsgesetze braucht man **zwei Drittel** – bei voller Besetzung **122** von 183 Stimmen. Darum kann eine Regierung ohne Opposition oft nicht die Verfassung ändern."])]),
             ("hint", "Alles hier ist freiwillig und zählt nicht zum Pflichtteil.")]},
]
