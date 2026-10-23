"""PBGW 2AK · K1 Grund- und Menschenrechte (Buch S. 45–58) – 2 Stunden (v3).
Stunde 1: Theorie kompakt + Arbeitsblatt »70 Jahre AEMR« (Schroedel 2018) · Stunde 2: Besprechung, Verstöße 2025/26, Stolz und Schande 2026.
Quelle für Handy-Seiten (Theorie-Seite, Arbeitsblatt, Quiz), Word und PPP. Auswahl: richtige Antwort steht an 1. Stelle (Anzeige gemischt),
außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""
import copy
from daten import T as T_AEMR, STAND

ORDNER = "2ak-pbgw/k1-grundrechte"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
EYEBROW = "PBGW · 2AK · K1 Grund- und Menschenrechte"
TITEL = "Menschenrechte – eine unvollständige Geschichte"
BUCH = "Buch S. 46–58"
KEY = "26-27-2AK-K1-Grundrechte-TH-Handy-v3"
V = "v3"

GEN = ["1. Generation (Freiheit)", "2. Generation (Gleichheit)", "3. Generation (Solidarität)"]
RECHTE = ["Meinungsfreiheit", "Recht auf Gesundheit", "Recht auf Bildung", "Wahlrecht", "Recht auf saubere Umwelt", "Vereinsfreiheit"]
ALLE = ["für alle Menschen", "nur für Staatsbürger"]
QUELLEN = ["Bundesverfassung (B-VG)", "EMRK", "EU-Grundrechtecharta", "AEMR"]
FALLRECHT = ["Wahlrecht", "Folterverbot", "Datenschutz", "Meinungsfreiheit"]


def first(lst, correct):
    """Liste mit der richtigen Antwort an erster Stelle (Anzeige wird gemischt)."""
    return [correct] + [x for x in lst if x != correct]


# Aufgaben: 1–6 Arbeitsblatt (Stunde 1), 7 Quellencheck (Stunde 2), 8–11 für Schnelle
T_AB = []
for t in T_AEMR:
    x = copy.deepcopy(t)
    if t["h"] == 0:
        x["nr"] = t["nr"] + 1; x["id"] = "a%d" % x["nr"]
    if x.get("tip") and x["tip"][1] == "#material":
        x["tip"] = [x["tip"][0], "theorie.html#arbeitsblatt"]
    if x.get("tip") and x["tip"][1] == "#a8":
        x["tip"] = [x["tip"][0], "#card_a9"]
    T_AB.append(x)
T_AB[4]["src"] = "Arbeitsblatt Aufgabe 5 · Buch S. 51"

T_Q = {"id": "a7", "nr": 7, "title": "Quellencheck", "src": "Buch S. 52 · Arbeitsblatt M4", "own": True, "tag": "Stunde 2", "h": 2, "hl": False,
       "q": "Vergleiche drei Quellen: den Buchtext S. 52 (ORF, 2022), das Arbeitsblatt M4 (Kommentar, 2018) und die Amnesty-Zahlen (Theorie-Seite Teil 2). "
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
       "tip": ["Stolz oder Schande – 2026?", "theorie.html#teil2"]}

T = [t for t in T_AB if t["h"] == 1] + [T_Q] + [t for t in T_AB if t["h"] == 0]
assert [t["nr"] for t in T] == list(range(1, 12)), [t["nr"] for t in T]

GRP = {1: "Stunde 1 · Theorie und Arbeitsblatt »70 Jahre AEMR«", 2: "Stunde 2 · Stolz und Schande – 2026", 0: "Für Schnelle und Neugierige · optional"}

LERNZIELE = ["Grund- und Menschenrechte unterscheiden und sagen, wo sie in Österreich verankert sind",
             "die Entwicklung von der Magna Charta bis zur AEMR beschreiben",
             "erklären, warum Menschenrechte schwer durchzusetzen sind – und was trotzdem wirkt",
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
 ("AEMR", "Welches Dokument in der Zeitleiste M1 ist das älteste?", ["der Kyros-Zylinder", "die Magna Charta", "die Bill of Rights", "die Französische Erklärung"],
  "Der Kyros-Zylinder stammt aus dem Jahr 539 v. Chr. (Persien) – die Magna Charta aus 1215.", "AB M1"),
 ("AEMR", "Wer leitete die Kommission, die die AEMR ausgearbeitet hat?", ["Eleanor Roosevelt", "Winston Churchill", "Navi Pillay", "Henry Dunant"],
  "Eleanor Roosevelt verkündete die Erklärung am 10.12.1948 um drei Uhr nachts in Paris.", "AB M2"),
 ("Quellen", "Der Text »Stolz und Schande« (M4) von 2018 ist …", ["ein Kommentar – der Autor sagt seine Meinung", "eine Nachricht – nur Fakten", "ein Gesetzestext", "eine Statistik"],
  "Wertende Wörter wie »Schande« zeigen: Meinung. Und er ist von 2018 – Zahlen für 2026 extra prüfen.", "AB M4"),
]
