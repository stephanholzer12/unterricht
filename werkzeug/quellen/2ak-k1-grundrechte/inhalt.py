"""PBGW 2AK · K1 Grund- und Menschenrechte (Buch S. 45–58) – ganze Einheit, 4 Stunden.
Stunde 1–2: Theorie aus der TH-PPP (Buch), Stunde 3–4: Arbeitsblatt »70 Jahre AEMR« (Schroedel 2018) mit Besprechung und Aktuellem.
Quelle für Handy-Seiten (Lernseite, Arbeitsblatt, Quiz), Word und PPP. Auswahl: richtige Antwort steht an 1. Stelle (Anzeige gemischt),
außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""
import copy
from daten import T as T_AEMR, STAND

ORDNER = "2ak-pbgw/k1-grundrechte"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
EYEBROW = "PBGW · 2AK · K1 Grund- und Menschenrechte"
TITEL = "Menschenrechte – eine unvollständige Geschichte"
BUCH = "Buch S. 46–58"
KEY = "26-27-2AK-K1-Grundrechte-TH-Handy-v2"
V = "v2"

GEN = ["1. Generation (Freiheit)", "2. Generation (Gleichheit)", "3. Generation (Solidarität)"]
RECHTE = ["Meinungsfreiheit", "Recht auf Gesundheit", "Recht auf Bildung", "Wahlrecht", "Recht auf saubere Umwelt", "Vereinsfreiheit"]
ALLE = ["für alle Menschen", "nur für Staatsbürger"]
QUELLEN = ["Bundesverfassung (B-VG)", "EMRK", "EU-Grundrechtecharta", "AEMR"]
FALLRECHT = ["Wahlrecht", "Folterverbot", "Datenschutz", "Meinungsfreiheit"]


def first(lst, correct):
    """Liste mit der richtigen Antwort an erster Stelle (Anzeige wird gemischt)."""
    return [correct] + [x for x in lst if x != correct]


SIT = [("Du postest deine Meinung zur Wehrdienstreform.", GEN[0], "Meinungsfreiheit"),
       ("Nach einem Bänderriss kommst du ins Spital.", GEN[1], "Recht auf Gesundheit"),
       ("Du besuchst die BHAK ohne Schulgeld.", GEN[1], "Recht auf Bildung"),
       ("Du wählst bei der Nationalratswahl.", GEN[0], "Wahlrecht"),
       ("Du läufst im Wald bei sauberer Luft.", GEN[2], "Recht auf saubere Umwelt"),
       ("Du gründest einen Fitness-Verein.", GEN[0], "Vereinsfreiheit")]
f1, c1 = [], {}
for k, (s, g, r) in enumerate(SIT, 1):
    f1 += [["g%d" % k, "%d) %s – Generation" % (k, s), GEN, False], ["r%d" % k, "%d) Recht" % k, RECHTE]]
    c1["g%d" % k] = {"sel": g}; c1["r%d" % k] = {"sel": r}
f1.append(["eigen", "Zusatz: ein eigenes Beispiel aus deinem Alltag – Situation, Generation, Recht"])

FALL = [("A", "Kadett Lukas, 17, will bei der Nationalratswahl wählen.", "Wahlrecht", "nur für Staatsbürger", "Bundesverfassung (B-VG)"),
        ("B", "Ein Asylwerber wird bei der Festnahme geschlagen und gedemütigt.", "Folterverbot", "für alle Menschen", "EMRK"),
        ("C", "Eine Behörde gibt Gesundheitsdaten weiter und wendet dabei EU-Recht an.", "Datenschutz", "für alle Menschen", "EU-Grundrechtecharta")]
f2, c2 = [], {}
for b, s, r, a, q in FALL:
    f2 += [["r" + b, "%s: %s – Welches Recht?" % (b, s), first(FALLRECHT, r)], ["a" + b, "%s: Gilt es …" % b, ALLE, False], ["q" + b, "%s: Rechtsquelle" % b, first(QUELLEN, q)]]
    c2["r" + b] = {"sel": r}; c2["a" + b] = {"sel": a}; c2["q" + b] = {"sel": q}

T_TH = [
 {"id": "a1", "nr": 1, "title": "Rechte in deinem Alltag", "src": "Buch-Aufgabe S. 48", "own": False, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Ordne jede Situation einer Generation zu und nenne das Recht. Zusatz: Das Buch verlangt zehn eigene Beispiele – hier sind sechs vorgegeben, ergänze eines.",
  "type": "multi", "fields": f1, "chk": c1,
  "sol": [["Lösung", ["1) 1. Generation – Meinungsfreiheit", "2) 2. Generation – Recht auf Gesundheit", "3) 2. Generation – Recht auf Bildung",
                      "4) 1. Generation – Wahlrecht", "5) 3. Generation – Recht auf saubere Umwelt", "6) 1. Generation – Vereinsfreiheit"]]],
  "tip": ["Drei Generationen von Menschenrechten", "theorie.html#generationen"]},
 {"id": "a2", "nr": 2, "title": "Fallkarten", "src": "Theorie S. 46–47", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Zuerst zu zweit ohne Handy besprechen, dann eintragen: Welches Recht ist betroffen? Gilt es für alle oder nur für Staatsbürger? Welche Rechtsquelle passt?",
  "type": "multi", "fields": f2, "chk": c2,
  "sol": [["Lösung", ["A: Wahlrecht – demokratisches Grundrecht, nur für Staatsbürger ab 16 (Bundesverfassung)",
                      "B: Folterverbot – gilt für alle Menschen (Art. 3 EMRK); Beschwerde beim VfGH, dann beim EGMR",
                      "C: Datenschutz – die EU-Grundrechtecharta gilt, weil EU-Recht angewendet wird (Art. 51)"]]],
  "tip": ["Grundrecht oder Menschenrecht? · Wo verankert?", "theorie.html#teil1"]},
 {"id": "a3", "nr": 3, "title": "Wehrpflicht und Gewissen", "src": "Theorie S. 46", "own": True, "tag": "Stunde 1", "h": 1, "hl": False,
  "q": "Dein Freund will aus Gewissensgründen keine Waffe tragen. a) Welche Pflicht und welches Recht stoßen aufeinander? b) Wie löst Österreich den Konflikt? "
       "c) Nimm in 2–3 Sätzen Stellung: Ist es fair, wenn Grundwehrdienst plus Übungen und Zivildienst je 9 Monate dauern (Reformentwurf 2027)?",
  "type": "multi",
  "fields": [["pflicht", "a) Die Pflicht", ["Wehrpflicht (Landesverteidigung)", "Schulpflicht", "Steuerpflicht", "Meldepflicht"]],
             ["recht", "a) Das Recht", ["Gewissensfreiheit", "Wahlrecht", "Recht auf Eigentum", "Vereinsfreiheit"]],
             ["loesung", "b) So löst Österreich den Konflikt"],
             ["stellung", "c) Meine Stellungnahme (2–3 Sätze)"]],
  "chk": {"pflicht": {"sel": "Wehrpflicht (Landesverteidigung)"}, "recht": {"sel": "Gewissensfreiheit"},
          "loesung": {"kw": [["Zivildienst / Ersatzdienst", "zivil|ersatz"]]}},
  "sol": [["a) und b)", ["Pflicht: Landesverteidigung (Art. 9a B-VG) – Recht: Gewissensfreiheit (Art. 9 EMRK)", "Lösung: Zivildienst als Ersatzdienst · Gleichheitsfrage: Die Wehrpflicht gilt nur für Männer."]],
          ["c) Mögliche Argumente", ["Pro: gleiche Belastung für beide; Rettung und Pflege brauchen Personal.", "Contra: Der Ersatzdienst darf nicht wie eine Strafe wirken; späterer Einstieg in Job oder Studium.",
                                     "Keine »richtige« Lösung – die Begründung zählt."]]],
  "tip": ["Grundrechte und Bundesheer – aktuell", "theorie.html#bundesheer"]},
 {"id": "a4", "nr": 4, "title": "Verschleppte Kinder", "src": "Buch-Aufgabe S. 56", "own": False, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "Recherchiere im Internet über die Verschleppung von Kindern aus der Ukraine. a) Was ist bis heute gegen dieses Unrecht geschehen? (zwei Beispiele) "
       "Zusatz: b) Welche Rechte werden verletzt? c) Wer nennt die Zahl von über 20.000 Kindern? Info: Lernseite Teil 2 · Recherche: orf.at oder tagesschau.de, Suchwort »Ukraine verschleppte Kinder«.",
  "type": "multi",
  "fields": [["was", "a) Was ist geschehen? (zwei Beispiele)"], ["rechte", "b) Verletzte Rechte"],
             ["wer", "c) Die Zahl »über 20.000« nennt …", ["die ukrainische Regierung (Kiew)", "die UNO", "die russische Regierung", "Amnesty International"]]],
  "chk": {"was": {"kw": [["Strafgerichtshof / Haftbefehl", "haftbefehl|strafgericht|istgh|icc"], ["Rückholung oder Sanktionen", "zurück|rückhol|sanktion"]]},
          "rechte": {"kw": [["Familie", "famili|eltern"], ["Kinderrechte / Identität", "kind|identität|sprache"]]},
          "wer": {"sel": "die ukrainische Regierung (Kiew)"}},
  "sol": [["a)", ["2023: Haftbefehle des Internationalen Strafgerichtshofs gegen Putin und Lwowa-Belowa", "rund 2.100 Kinder zurückgeholt (Save Ukraine, Mai 2026)",
                  "EU-Sanktionen im Mai 2026 · NGOs dokumentieren Namen und Fälle"]],
          ["b) und c)", ["Schutz der Familie (Art. 16 AEMR), Freiheit und Sicherheit (Art. 3), Kinderrechte (Identität, Sprache, Familie), Kriegsvölkerrecht: Deportationsverbot",
                         "Die Zahl stammt von der ukrainischen Regierung – unabhängig nicht geprüft. Kiew und Moskau sind Kriegsparteien."]]],
  "tip": ["Verschleppte Kinder aus der Ukraine", "theorie.html#kinder"]},
 {"id": "a5", "nr": 5, "title": "Todesstrafe – pro und contra", "src": "Buch-Aufgabe S. 58", "own": False, "tag": "Stunde 2", "h": 2, "hl": False,
  "q": "1. Erarbeite je drei Argumente für und gegen die Todesstrafe. 2. Diskutiert in der Klasse über Beibehaltung oder Abschaffung (ohne Handy). Zusatz: Schreib danach deine Meinung in 2 Sätzen auf.",
  "type": "multi",
  "fields": [["pro", "Drei Argumente dafür (Sicht der Befürworter)"], ["contra", "Drei Argumente dagegen"], ["meinung", "Zusatz: Meine Meinung (2 Sätze)"]],
  "chk": {"contra": {"kw": [["Recht auf Leben", "leben"], ["Justizirrtum", "irrtum|unschuld|fehlurteil|dna"], ["Abschreckung nicht belegt", "abschreck"]]}},
  "sol": [["Pro (Sicht der Befürworter)", ["Vergeltung, Gerechtigkeit für Opfer", "Abschreckung (behauptet)", "Der Täter kann nie wieder töten."]],
          ["Contra", ["Recht auf Leben (Art. 3 AEMR)", "Justizirrtümer sind nicht korrigierbar – DNA-Analysen (Buch S. 57)", "Abschreckung ist wissenschaftlich nicht belegt", "trifft oft Arme und Minderheiten"]]],
  "tip": ["Todesstrafe weltweit", "theorie.html#todesstrafe"]},
]

# Arbeitsblatt-Aufgaben (Stunde 3, Zusatz) – neu nummeriert
T_AB = []
for t in T_AEMR:
    x = copy.deepcopy(t)
    x["nr"] = t["nr"] + (5 if t["h"] == 1 else 6); x["id"] = "a%d" % x["nr"]
    if t["h"] == 1:
        x["tag"], x["h"] = "Stunde 3", 3
    if x.get("tip") and x["tip"][1] == "#material":
        x["tip"] = [x["tip"][0], "theorie.html#teil3"]
    if x.get("tip") and x["tip"][1] == "#a8":
        x["tip"] = [x["tip"][0], "#card_a14"]
    T_AB.append(x)
T_AB[4]["src"] = "Arbeitsblatt Aufgabe 5 · Buch S. 51"
T_AB[5]["q"] = T_AB[5]["q"].replace("in der nächsten Stunde", "in Stunde 4")
T_AB[4]["q"] = T_AB[4]["q"].replace("In der nächsten Stunde", "In Stunde 4")

T_Q = {"id": "a12", "nr": 12, "title": "Quellencheck", "src": "Theorie S. 52 · Arbeitsblatt M4", "own": True, "tag": "Stunde 4", "h": 4, "hl": False,
       "q": "Vergleiche drei Quellen: den Buchtext S. 52 (ORF, 2022), das Arbeitsblatt M4 (Kommentar, 2018) und die Amnesty-Zahlen (Lernseite Teil 2). "
            "Was ist Nachricht, was Meinung? Wie aktuell? Wer steckt dahinter?",
       "type": "multi",
       "fields": [["orf", "ORF 2022 ist …", ["eine Nachricht mit Quelle", "ein Kommentar", "Werbung", "ein Gesetzestext"]],
                  ["orfakt", "Stimmt der ORF-Text 2026 noch?", ["nein – veraltet, 2026 Platz 19 statt 31", "ja – noch genau so"], False],
                  ["m4", "M4 (Prantl, 2018) ist …", ["ein Kommentar (Meinung)", "eine Nachricht (nur Fakten)", "eine Statistik"]],
                  ["amnesty", "Amnesty: Wer steckt dahinter – und was ist zu beachten? (1–2 Sätze)"]],
       "chk": {"orf": {"sel": "eine Nachricht mit Quelle"}, "orfakt": {"sel": "nein – veraltet, 2026 Platz 19 statt 31"}, "m4": {"sel": "ein Kommentar (Meinung)"},
               "amnesty": {"kw": [["NGO", "ngo|organisation|nicht.?staatlich|verein"], ["Ziel / Mindestzahlen", "ziel|abschaff|mindest|china|kampagne"]]}},
       "sol": [["Lösung", ["ORF 2022: Nachricht mit Quelle (Reporter ohne Grenzen) – aber veraltet: 2026 Platz 19 statt 31.",
                           "Prantl, M4: Kommentar = Meinung; wertende Wörter wie »Schande«, »Todesanzeige«; Stand 2018, deutsche Sicht.",
                           "Amnesty: NGO mit klarem Ziel (Abschaffung der Todesstrafe); zählt aus Berichten = Mindestzahlen; China fehlt.",
                           "Merke: Nicht nur fragen »Stimmt das?« – sondern: Wer sagt das, wann und warum?"]]],
       "tip": ["Stolz oder Schande – 2026?", "theorie.html#teil4"]}

T = T_TH + [t for t in T_AB if t["h"] == 3] + [T_Q] + [t for t in T_AB if t["h"] == 0]
assert [t["nr"] for t in T] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [t["nr"] for t in T]

GRP = {1: "Stunde 1 · Grund- und Menschenrechte", 2: "Stunde 2 · Verstöße gegen Menschenrechte", 3: "Stunde 3 · Arbeitsblatt »70 Jahre AEMR«",
       4: "Stunde 4 · Stolz und Schande – 2026", 0: "Für Schnelle und Neugierige · optional"}

LERNZIELE = ["Grund- und Menschenrechte unterscheiden und sagen, wo sie in Österreich verankert sind",
             "Rechte aus deinem Alltag den drei Generationen zuordnen",
             "die Entwicklung von der Magna Charta bis zur AEMR beschreiben und erklären, warum Durchsetzen schwer ist",
             "aktuelle Verstöße mit Zahlen beschreiben, Quellen prüfen und begründet Stellung nehmen"]

WICHTIGSTE = ["**Menschenrechte** hat jeder, weil er Mensch ist – **Grundrechte** garantiert die Verfassung, manche nur für Staatsbürger.",
              "In Österreich stehen sie im **Staatsgrundgesetz 1867** und in der **EMRK** (Verfassungsrang 1964); Beschwerde beim VfGH, dann beim EGMR.",
              "Die **AEMR** (10.12.1948) gilt für alle Menschen weltweit – sie ist aber **kein Vertrag**; verbindlich wurden EMRK und UN-Pakte.",
              "Ohne Weltpolizei wirken vor allem **Gerichte, Sanktionen und öffentlicher Druck** (»weiche Macht«).",
              "Auf dem Papier stark, in der Wirklichkeit oft verletzt (2025: 2.707 Hinrichtungen) – Menschenrechte muss man **immer wieder verteidigen**."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Grundrechte", "in der Verfassung garantierte, einklagbare Rechte – manche nur für Staatsbürger"],
                ["Menschenrechte", "angeborene, unveräußerliche Rechte jedes Menschen"],
                ["StGG 1867", "Staatsgrundgesetz – Kern der Grundrechte (Dezemberverfassung)"],
                ["EMRK / EGMR", "Europäische Menschenrechtskonvention (1950) / Gerichtshof in Straßburg"],
                ["VfGH", "Verfassungsgerichtshof in Wien – prüft Grundrechtsverletzungen"],
                ["AEMR", "Allgemeine Erklärung der Menschenrechte (UNO 1948), nicht verbindlich"],
                ["wsk-Rechte", "wirtschaftliche, soziale und kulturelle Rechte (2. Generation)"],
                ["Völkerrecht", "Regeln zwischen Staaten (Verträge, Gewohnheit)"],
                ["Konvention / Pakt", "Vertrag zwischen Staaten – verbindlich, z. B. EMRK, UN-Pakte 1966"],
                ["Sanktion", "Strafe oder Druckmittel gegen einen Staat"],
                ["weiche Macht", "Druck durch Öffentlichkeit statt durch Strafen"],
                ["NGO", "Nichtregierungsorganisation, z. B. Amnesty International"],
                ["Zivildienst", "Ersatzdienst für Wehrpflichtige, die aus Gewissensgründen verweigern"],
                ["Kommentar", "Text, in dem jemand seine Meinung sagt"]]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Grundrechte", "Welches Recht gilt in Österreich nur für Staatsbürger?", ["das Wahlrecht", "das Folterverbot", "das Recht auf Leben", "die Meinungsfreiheit"],
  "Das Wahlrecht ist ein demokratisches Grundrecht für Staatsbürger. Folterverbot und Recht auf Leben sind Menschenrechte – sie gelten für jeden.", "Buch S. 46"),
 ("Grundrechte", "Welche Grundrechte schützen dich VOR dem Staat?", ["die liberalen Grundrechte", "die demokratischen Grundrechte", "die sozialen Grundrechte", "die Wahlrechte"],
  "Liberale Rechte wie Meinungsfreiheit oder Privatsphäre sind Abwehrrechte gegen den Staat. Demokratische Rechte = Mitbestimmung, soziale = Leistung.", "Buch S. 46"),
 ("Grundrechte", "Was steht NICHT in der österreichischen Verfassung?", ["soziale Grundrechte", "das Wahlrecht", "die Meinungsfreiheit", "die Gleichheit vor dem Gesetz"],
  "Soziale Grundrechte wie soziale Sicherung stehen nicht in der Verfassung – sie sind in einfachen Gesetzen geregelt.", "Buch S. 46"),
 ("Verankerung", "Seit wann hat die EMRK in Österreich Verfassungsrang?", ["seit 1964", "seit 1867", "seit 1948", "seit 2009"],
  "Österreich trat 1958 der EMRK bei, 1964 bekam sie Verfassungsrang. 1867 = Staatsgrundgesetz, 2009 = EU-Grundrechtecharta.", "Buch S. 47, 50"),
 ("Verankerung", "Wo sitzt der Europäische Gerichtshof für Menschenrechte?", ["in Straßburg", "in Wien", "in Den Haag", "in Brüssel"],
  "Der EGMR in Straßburg wacht über die EMRK. In Den Haag sitzt der Internationale Strafgerichtshof, in Wien der VfGH.", "Buch S. 47"),
 ("Generationen", "Das Recht auf eine saubere Umwelt gehört zur …", ["3. Generation (Solidarität)", "1. Generation (Freiheit)", "2. Generation (Gleichheit)", "zu keiner Generation"],
  "Frieden, Entwicklung und saubere Umwelt sind Solidaritätsrechte – 2022 hat die UNO das Recht auf eine gesunde Umwelt anerkannt.", "Buch S. 47–48"),
 ("Österreich", "Seit wann ist die Todesstrafe in Österreich ganz abgeschafft?", ["seit 1968", "seit 1945", "seit 1867", "seit 2000"],
  "1950 wurde sie im normalen Strafrecht abgeschafft, 1968 auch im Standrecht – seitdem ganz.", "Buch S. 50"),
 ("Bundesheer", "Wer leistet Zivildienst?", ["Wehrpflichtige, die aus Gewissensgründen keine Waffe tragen wollen", "alle Frauen", "Berufssoldaten", "Soldaten nach dem Grundwehrdienst"],
  "Wehrpflicht und Gewissensfreiheit stoßen aufeinander – der Zivildienst ist der Ersatzdienst.", "Buch S. 46"),
 ("Verstöße", "Wie viele Hinrichtungen hat Amnesty für 2025 gezählt?", ["2.707", "270", "27.070", "707"],
  "So viele wie seit 1981 nicht – und das sind Mindestzahlen, China ist nicht eingerechnet.", "Buch S. 57"),
 ("Verstöße", "Welchen Platz hat Österreich in der Rangliste der Pressefreiheit 2026?", ["Platz 19", "Platz 31", "Platz 1", "Platz 64"],
  "Österreich hat aufgeholt (Buch: Platz 31). Platz 1 Norwegen, die USA sind auf Platz 64 gefallen.", "Buch S. 52"),
 ("Verstöße", "Was verbieten die Genfer Abkommen?", ["Zivilisten zu deportieren", "die Wehrpflicht", "Wahlen im Krieg", "Pressekonferenzen im Krieg"],
  "Das Kriegsvölkerrecht schützt Zivilisten, Verwundete und Gefangene – die Verschleppung von Kindern verstößt dagegen.", "Buch S. 56"),
 ("AEMR", "Was wurde am 10. Dezember 1948 in Paris verkündet?", ["die Allgemeine Erklärung der Menschenrechte", "die EMRK", "das Staatsgrundgesetz", "die EU-Grundrechtecharta"],
  "Die UNO-Generalversammlung verkündete die AEMR – Eleanor Roosevelt leitete die Kommission.", "Buch S. 47 · AB M2"),
 ("AEMR", "Warum ist die AEMR rechtlich nicht verbindlich?", ["Sie ist eine Erklärung, kein Vertrag.", "Österreich hat dagegen gestimmt.", "Sie gilt nur in Europa.", "Sie wurde 1966 aufgehoben."],
  "Verbindlich wurden die Inhalte erst durch Verträge: EMRK (1950) und UN-Pakte (1966). Österreich war 1948 noch nicht bei der UNO.", "Buch S. 47 · AB M2"),
 ("Durchsetzen", "Was ist mit »weicher Macht« gemeint?", ["Verstöße öffentlich machen und so Druck erzeugen", "Soldaten in ein Land schicken", "Verbrecher vor ein Weltgericht stellen", "Gesetze für andere Länder beschließen"],
  "NGOs, Medien und Staaten stellen Verstöße an den Pranger. Kein Staat will als Rechtsbrecher dastehen.", "Buch S. 51 · AB M3"),
 ("Quellen", "Der Text »Stolz und Schande« (M4) von 2018 ist …", ["ein Kommentar – der Autor sagt seine Meinung", "eine Nachricht – nur Fakten", "ein Gesetzestext", "eine Statistik"],
  "Wertende Wörter wie »Schande« zeigen: Meinung. Und er ist von 2018 – Zahlen für 2026 extra prüfen.", "AB M4"),
]
