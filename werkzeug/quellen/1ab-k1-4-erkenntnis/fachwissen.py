"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, VS-Fachwissen, Lehrer-Infos der PPPs und Lösungsmappe K1.4 Erkenntnisgewinn.
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Word)."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v64, Zeile 7: E3 »Erkenntnisgewinn: Beobachtung, Hypothese, Experiment, Theorie – Falsifizierbarkeit«, 3 Std. Kern, Trauner S. 28–32 (Kap. 4, 4.1–4.2). "
                  "Hier: 4 Kalenderstunden je Klasse, am Fr 06.11. 20 min Test → je 180 min E3 (Annahme 50-min-Stunden; Klassenbuch ca. 3 min je Stunde eingerechnet)."),
    ("K01 ", "naturwissenschaftliche Fragestellungen erkennen und deren Phänomene den Teilbereichen Biologie, Chemie, Physik zuordnen → A3 (Zuordnen inkl. »keine NAWI-Frage«), A4 (eigene prüfbare Frage/Hypothese), A12, Teil 1 »Welche Fragen …«"),
    ("N06 ", "Verlässlichkeit einer Aussage abschätzen, Gültigkeitsgrenzen erkennen, Schlüsse ziehen → A5 (Messregeln), A6 (Vorjahresdaten), A8 (Mittelwert/Spannweite), A9 (KI-Check), K1.4-V1 Interpretation und Schlussfolgerung, Gegenprobe"),
    ("GLV 2 ", "Informationsresilienz: eine nicht widerlegbare Behauptung ist keine wissenschaftlich prüfbare Hypothese → Teil 4 »Widerlegbar muss es sein«, A9 Aussage 3, A12; Bezug Lagemeldung / Behauptungen im Netz"),
    ("P / SDG ", "in der Jahresplanzeile nicht belegt; nebenbei: Gesundheit (Semmelweis, Ruhepuls), Medienbildung (KI-Antwort prüfen)"),
    ("Schulprofil: ", "Erprobung einer Ausrüstungsänderung mit vorher festgelegtem Kriterium · Beobachtungsposten/Wildtierkamera · Geländemodell (Sandkasten) bei der Lagebesprechung · Zielscheiben (zufälliger/systematischer Fehler) · Lagemeldung muss überprüfbar sein"),
    ("Buchabdeckung: ", "Trauner S. 28–29 vollständig gesichtet (Foto); S. 30–32 nur als Aufgabenkasten-Ausschnitt ohne Seitenzahl vorhanden (→ A2 »Buch-Aufgabe S. 30–32«). "
                        "Buch-Mikroskopierauftrag S. 28 bewusst nicht übernommen (eigene Einheit). Die Vereinfachung S. 29 (Hypothese → Gesetz bzw. Theorie, »Theorie = mehrere Gesetze«, »bewiesen«) wird für die Kadetten präzisiert."),
    ("Abweichung: ", "4 statt 3 Stunden (Stephans Termine); Gliederung nach Teilen (1AK und 1BK in anderer Reihenfolge); V1.4 überarbeitet: derselbe Flieger ohne/mit Klammer statt zweier Modelle; "
                     "V1.7 (E5) nicht vorgezogen; Versuchsort Eingangsbereich statt NAWI-Gang; kein CLIL (Didaktik-Blatt sieht es vor – Stephans Vorgabe hat Vorrang)."),
]


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, zus = PL.aufgaben_der(st)
        t = st["teile"][0]
        extra = ["Test 20 min"] if any(p[3] == "test" for p in st["phasen"]) else []
        vs = [(p[0], p[1]) for p in st["phasen"] if p[3].startswith("v:")]
        rows.append([f"{st['std']} · {st['datum']}", " · ".join(extra + [I.TEILNAME[t]]),
                     " · ".join(f"{n.split(':')[0]} {m} min" for n, m in vs) or ("Flieger bauen 10 min" if t == 1 else "–"),
                     PL.bereich(nrs) + (" · Zusatz " + PL.bereich(zus) if zus else ""),
                     f"Reserve {PL.minuten(st, ['reserve'])} · Bespr. {PL.minuten(st, ['bespr'])}", st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "A4-Papier (2 je Gruppe), Bleistifte, Schachtel für die Flieger · Faltanleitung am Beamer · Einstiegs-Flieger mit Klammer zum Zeigen",
            2: "Bandmaß 20 m (#9), Büroklammern F-038 (1 je Gruppe), die Flieger der Gruppen, Papierblätter VS-AB (1 je Gruppe), Ersatzpapier",
            3: "Test (eigene Unterlagen) · Vorjahres-Tabelle am Beamer · Partnerkarten (Beamer oder ausgedruckt)",
            4: "eingesammelte Papierblätter der Gruppen · Tafel/Flipchart für die Klassenübersicht · Flieger aufbewahren für den Kraft-Einstieg"}


def _karten():
    out = []
    for k in PL.PLAN:
        for st in PL.PLAN[k]:
            schritte = [f"{name} ({m} min)" for name, m, oh, art in st["phasen"]]
            if (k, st["std"]) in PL.KNAPP: schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
            mat = MATERIAL[st["teile"][0]]
            ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org")))
            out.append((f"{k} · Stunde {st['std']} · {st['datum']} · " + I.TEILNAME[st["teile"][0]], schritte, mat, ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Bis spätestens Di 03.11.: Hallenprobe im Eingangsbereich – einen Planarflieger nach der Faltanleitung falten (Zeit stoppen: reichen 10 min?), je 3–4 ruhige Würfe aus Hüfthöhe ohne und mit Klammer. Fliegen beide ohne Deckenkontakt? Grob wie weit? Hält die Klammer?",
    "Abwurflinie festlegen: eine Bodenfuge (Kreide ist nicht im Inventar). Prüfen, ob Durchgangsverkehr in der Stunde zu erwarten ist (Pausenzeiten, Besucher) – ggf. Kollegen/Sekretariat kurz informieren.",
    "Bandmaß 20 m (#9) aus E21 holen und prüfen (im Inventar keine aktuelle Zählung). Bandmaß 3 m (#10) als Reserve.",
    "Ein Packen 80-g-Kopierpapier für alle Gruppen (Kopierraum – nicht im Inventar). Büroklammern F-038: 8 gleich große aus derselben Schachtel + Reserve.",
    "VS-AB (Papierblatt) je Gruppe kopieren – 8 Stück + 2 Reserve; dient als Sicherung der Messwerte bis Stunde 4.",
    "Gruppen 1–8 vorab überlegen (Klassengröße nicht bestätigt; bei weniger Kadetten weniger Gruppen, je 3–4). Ungerade Gruppen beginnen mit A, gerade mit B.",
    "1BK: Flieger am Mi 04.11. einsammeln, flach in einer Schachtel bis Mo 09.11. lagern. 1AK: Papierblätter vom Do 05.11. bis Do 12.11. aufbewahren.",
    "Test am Fr 06.11. (20 min inkl. Austeilen/Einsammeln) – danach Teil 3. Der Teststoff dieses Tests ist NICHT E3 (nicht festgelegt).",
    "Einheit auf der Klassenseite einblenden, wenn es losgeht (GitHub → Actions → »Einheit ein-/ausblenden« → 1ab-nawi/k1-4-erkenntnis → einblenden). Bis dahin ist sie versteckt, die Links funktionieren aber.",
    "Ö1-Podcast »Peer Review und Open Science« (2020, eigene Sammlung) – falls du einen Ausschnitt in Teil 3 spielen willst: 2–3 min vorher heraussuchen (nicht im Zeitplan, nur bei Reserve).",
]

AUF_EINEN_BLICK = [
    ["Teil 1 · Std. 1 (beide)", "Beobachtung ≠ Deutung; Hypothese = begründet und prüfbar; Vorhersage = erwartetes Testergebnis; Gesetz beschreibt, Theorie erklärt – keine Leiter. Fragen zuordnen. Hypothese aufschreiben, Flieger bauen.", MATERIAL[1]],
    ["Teil 2 · 1AK Std. 2 · 1BK Std. 3", "Fairer Test: nur Klammer ab/dran; erster Bodenkontakt; drei Paare abwechselnd; alle Würfe zählen, Kontakte vermerken; Gegenprobe mit zweitem Werfer.", MATERIAL[2]],
    ["Teil 3 · Fr 06.11. (beide, nach Test)", "Forschung als Kreislauf; Modell = Vereinfachung mit Grenzen; Veröffentlichung, Begutachtung, Wiederholung; Semmelweis; Vorjahresdaten kritisch lesen.", MATERIAL[3]],
    ["Teil 4 · Std. 4 (beide)", "Mittelwert, Spannweite; unterstützt / spricht dagegen / unklar; Falsifizierbarkeit (nicht prüfbar ≠ falsch); Forschen vs. Konstruieren; Ausblick Kraft.", MATERIAL[4]],
]

KAPITEL = [
 {"titel": "1 Beobachtung, Hypothese, Vorhersage, Theorie (Buch S. 28–29)",
  "text": ["**Beobachtung und Deutung trennen:** »6,4 m« ist eine Beobachtung; »weil die Nase schwerer ist« ist schon eine Deutung. Die Trennung ist das wichtigste Werkzeug der ganzen Einheit – in jeder Aufgabe wiederkehren lassen.",
           "**Hypothese:** begründete, prüfbare Vermutung über einen Zusammenhang. Prüfbar heißt: Man kann vorher angeben, welche Beobachtung dagegen sprechen würde. Die Hypothese betrifft hier einen **Mittelwert** (»im Mittel weiter«) – darum widerlegt ein einzelner kurzer Flug sie nicht.",
           "**Vorhersage:** das aus der Hypothese abgeleitete erwartete Ergebnis eines konkreten Tests (»bei drei Paaren hat B den größeren Mittelwert«). Viele Schulbücher vermischen Hypothese und Vorhersage – im Unterricht konsequent trennen.",
           "**Gesetz und Theorie:** Ein Gesetz beschreibt eine Regelmäßigkeit (oft als Formel, z. B. Fallgesetz ohne Luftwiderstand); eine Theorie erklärt und verbindet viele Befunde (Zelltheorie, Keimtheorie, Evolutionstheorie, Atomtheorie). Es gibt **keine Rangfolge** Hypothese → Gesetz → Theorie; eine Theorie wird auch nicht zum Gesetz, wenn sie »oft genug« bestätigt ist (National Academy of Sciences 1998, Kap. 1 und Glossar).",
           "**Was Trauner S. 29 vereinfacht:** »Hypothese = unbewiesene Annahme … die bewiesen oder widerlegt werden kann« und »bestätigen wiederholte Experimente die Hypothese, dann wird sie zum Gesetz bzw. zur Theorie (= mehrere Gesetze)«. Für die Kadetten präzisiert: Ergebnisse **unterstützen** Hypothesen; endgültige Beweise gibt es in den empirischen Wissenschaften nicht. Die Kapitelüberschrift »Von der Hypothese zur Theorie« bleibt als Buchnavigation.",
           "**Galilei-Beispiel im Buch:** nur mit Bedingung verwenden (»ohne Luftwiderstand fallen alle Körper gleich schnell«). Keine zusätzlichen historischen Details erfinden (der Turm von Pisa ist als Experiment nicht sicher belegt)."],
  "nur": ["Begriffsgebrauch ist zwischen Fächern und historisch nicht einheitlich (»Ohmsches Gesetz«, »Relativitätstheorie«, »Zellenlehre«). Für den Unterricht reicht die Abgrenzung beschreiben/erklären; keine absolute Definition behaupten.",
          "Popper (1902 Wien – 1994 London): Falsifizierbarkeit als Abgrenzungskriterium (»Logik der Forschung«, 1934). Nicht prüfbar heißt nicht sinnlos oder falsch, nur außerhalb empirischer Prüfung."],
  "stolper": "»Theorie = Vermutung« (Alltagssprache) und »oft bestätigt = bewiesen = Gesetz«. Gegenmittel: Grafik »zwei Säulen, keine Leiter«, Aufgabe 2d und 9.",
  "bild": "img/theorie.png"},
 {"titel": "2 Der faire Test: K1.4-V1 Papierflieger (Buch S. 29, Jahresplan V1.4)",
  "text": ["**Warum derselbe Flieger:** Im alten Wettbewerb (kurz gegen lang) änderten sich Form, Faltung, Fläche, Masse, Werfer und Abwurf gleichzeitig – eine Ursache ließ sich nicht isolieren (Vorjahresdaten zeigen das gut). Jetzt ändert sich nur »Klammer ab/dran«.",
           "**Was die Klammer ändert:** Masse und Schwerpunktlage gleichzeitig (der Schwerpunkt wandert nach vorne). Der Test beantwortet nur: Welche Wirkung hat diese konkrete Änderung bei diesem Modell und diesem Abwurf? Er trennt die beiden Ursachen nicht.",
           "**Messgröße:** Vorwärtsweite bis zum ersten Bodenkontakt entlang des Bandmaßes, auf 0,1 m gerundet. Die Rundung ist keine geprüfte Messunsicherheit von ±0,1 m. Nicht Flugzeit, nicht Bahnlänge, nicht Rutschweite.",
           "**Reihenfolge A,B · B,A · A,B (bzw. umgekehrt):** verteilt Übungseffekte, Ermüdung und allmähliche Verformung des Fliegers auf beide Zustände. Drei Paare sind ein Unterrichtskompromiss; mehrere Würfe desselben Fliegers sind keine unabhängige Stichprobe verschiedener Flieger.",
           "**Ausschlussregeln vorher:** gültig = jeder reguläre Flug; ungültig nur bei Linienübertritt, Eingriff von außen, abgefallener Klammer – dann wiederholen und notieren. Decken-/Wandkontakt: Wert bleibt mit Vermerk, er ist aber kein unbehinderter Weitenwert. Sind A und B ungleich oft betroffen, ist die Weitenfrage nicht sauber entschieden.",
           "**Gegenprobe:** zweiter Werfer, getrennt protokolliert. Prüft die Übertragbarkeit auf einen anderen Werfer – nicht Masse vs. Schwerpunkt. Werte verschiedener Werfer nie unbemerkt zusammen mitteln.",
           "**Raum:** Eingangsbereich, lang genug, Decke niedrig (Maße nicht bekannt – nicht den historischen 15,5-m-NAWI-Gang übertragen). Flacher, ruhiger Abwurf aus Hüfthöhe; kein universeller »optimaler Abwurfwinkel«."],
  "nur": ["Physik dahinter (für Fragen, nicht für E3): Im antriebslosen Gleitflug wirken nur Gewichtskraft und die Luftkraft (zerlegt in Auftrieb senkrecht zur Anströmung und Widerstand entgegen der Flugrichtung). Die Hand wirkt nach dem Loslassen nicht mehr – ein fortwirkender »Schub« wie bei Gruber S. 20 ist für den Papierflieger falsch.",
          "Mehr Masse allein ändert im gleichmäßigen Gleitflug den Gleitwinkel nicht (der hängt vom Verhältnis Auftrieb zu Widerstand ab), nur das Tempo. Ein Schwerpunkt weiter vorne ändert die Trimmung – ob die Weite steigt oder sinkt, hängt vom Modell und vom Abwurf ab. Bei rund 1 m Abwurfhöhe bestimmt ohnehin vor allem die Abwurfphase die Weite. Darum keine Wirkung vorwegnehmen.",
          "V-Stellung (Gruber: »Y-Stellung«, Flügel in der Vorderansicht leicht nach oben) ist nicht dasselbe wie der Anstellwinkel (Winkel des Flügels zur anströmenden Luft) – im MINT-Lösungsblatt verwechselt."],
  "stolper": "Kurze Flüge als »Fehlwurf« streichen, bis zum Stillstand messen, zwischen den Würfen nachbiegen. Gegenmittel: Aufgabe 5 VOR dem Versuch, Prüfer-Rolle, Regel-Folie bleibt stehen.",
  "bild": "img/messbahn.png"},
 {"titel": "3 Wie Forschung läuft: Kreislauf, Modell, Begutachtung (Buch S. 29)",
  "text": ["**Kreislauf statt Linie:** Hölzel S. 14 nennt acht idealisierte Schritte und betont selbst, dass Forschung kein gerader Weg ist. Im Unterricht: Rückpfeile (Messung prüfen, Bedingungen ändern) und neue Fragen am Ende.",
           "**Modelle:** gezielte Vereinfachungen für einen Zweck mit Grenzen (Bohrs Atommodell aus Trauner S. 29; Geländemodell im Sandkasten; der Papierflieger als einfaches Modell eines Flugzeugs – der Versuch selbst ist eine echte Untersuchung, kein Modell). Hölzel S. 19 zeigt absichtlich ungeeignete Mondmodelle – nur mit sichtbarer Kritik verwenden, nicht als Lösung.",
           "**Publikation und Begutachtung:** Methode und Daten so beschreiben, dass andere wiederholen können; Peer Review prüft Methode und Schlüsse, findet aber nicht jeden Fehler und garantiert keine Wahrheit. Vertrauen entsteht durch unabhängige Wiederholung (Reproduzierbarkeit).",
           "**Semmelweis (Einstieg):** Wien 1847, Erste Gebärklinik: Sterblichkeit 1841–1846 im Mittel ca. 10 % (Zweite Klinik unter 4 %); April 1847 18,3 %; Chlorkalk-Handwaschung ab Mitte Mai; Juni 2,2 %, Juli 1,2 %, August 1,9 %. Viele Kollegen lehnten ab; die Erklärung (Erreger) kam mit der Keimtheorie (Pasteur, Koch) Jahrzehnte später. Gutes Beispiel für Hypothese → Vorhersage → Test → Widerstand der Fachwelt.",
           "**Vorjahresdaten (A6):** je Gruppe ein Wurf je Flieger, zwei verschiedene Flieger, Werfer nicht dokumentiert. Alte 1AK: kurz weiter in G1, G2, G6; lang in G3, G4, G5, G7. Alte 1BK: G3 widerspricht dem Muster; G5 »Ung.« – kein Paarvergleich. Datum/Schuljahr der Erhebung nicht bekannt; keine Gruppe als unfähig darstellen."],
  "nur": ["Reproducibility Project: Cancer Biology (eLife, 7.12.2021): 193 geplante Experimente aus 53 Artikeln, 50 aus 23 tatsächlich wiederholt; Effekte im Median 85 % kleiner; bei positiven Effekten ca. 40 % nach mindestens 3 von 5 Kriterien erfolgreich. Grund für viele Ausfälle: fehlende Methodenangaben und Daten.",
          "Biologie-Brücke: Keimversuch mit Licht/Dunkel (Didaktik-Blatt v64) hat dieselbe Logik wie der Flieger-Test – gute Hausaufgabe für eine spätere Bio-Einheit, nicht in E3."],
  "stolper": "»Eine Gruppe mit anderem Ergebnis hat falsch gemessen.« Gegenmittel: zuerst Bedingungen und Protokoll prüfen (A6 d, Partnerkarte 6).",
  "bild": "img/kreislauf.png"},
 {"titel": "4 Auswerten, Falsifizierbarkeit, Konstruktionszyklus (Buch S. 29–32)",
  "text": ["**Mittelwert und Spannweite:** zuerst alle Einzelwerte ansehen, dann Mittelwerte. Spannweite = größter − kleinster Wert. Keine Standardabweichung, kein Signifikanztest als Pflicht. Die alte Folie 13 leitete aus der halben Spannweite »± 8 cm Messunsicherheit« ab – das ist keine Messunsicherheit und wurde gestrichen.",
           "**Drei erlaubte Ergebnisse:** unterstützt · spricht dagegen · unklar. Kein starres Entscheidungskriterium aus überlappenden Spannweiten, aber: Überlappen die Werte stark und ist der Mittelwertunterschied klein, ist die ehrliche Antwort »unklar«.",
           "**Falsifizierbarkeit (GLV 2):** prüfbare Aussagen benennen ihren möglichen Gegenbefund. Immunisierung (»verliert er, zählt der Wurf nicht«) macht eine Aussage unprüfbar. Nicht prüfbar ≠ falsch.",
           "**Forschen vs. Konstruieren (MINT-Modul »Vom Binärsystem zum Papierflieger«, AB 2.1):** Forschen fragt »Was stimmt?« (Hypothese prüfen, eine Variable). Konstruieren fragt »Was funktioniert besser?« (Entwurf verbessern, mehrere Durchläufe). Beide brauchen faire Tests; während einer Vergleichsreihe nicht heimlich mehrere Merkmale optimieren. Das MINT-Modul plant dafür 4 Lektionen (180 min) – in E3 nur 4 min Zuordnung (A10).",
           "**Ausblick 1AK 12.11. (2. Std. Kraftbegriff):** »Die Hand hat losgelassen – warum fliegt er weiter? Welche Kräfte wirken jetzt?« Fehlvorstellung »Bewegung braucht ständig eine Kraft in Bewegungsrichtung« sammeln, nicht gleich auflösen."],
  "nur": ["Physik-Anschlüsse (Stephan: mechanische Kräfte, Geschwindigkeit, Arbeit/Energie, elektrische Kräfte): Kraftbild nach dem Loslassen (Trauner S. 45, 49–50, 61) · Luftwiderstand gezielt verändern (ab S. 54) · Geschwindigkeit auf einer festgelegten Strecke v = s/t (S. 46; nicht aus Weite/Gesamtzeit) · Energie: Höhenenergie m·g·h, Bewegungsenergie ½·m·v², Übertragung an die Luft (S. 67–73) – Auftrieb und Wurfkraft sind Kräfte, keine Energieformen · elektrische Kräfte: geriebener Ballon zieht Papierschnipsel an (S. 79–80, Pool V1.31) – nicht als Erklärung des Fliegens.",
          "Formeln erst in den jeweiligen Einheiten einführen, nicht in E3. Gruber S. 13–28 als Lehrerhintergrund (Trimmung, Abwurf, Kräftebild – Schub-Pfeil korrigieren)."],
  "stolper": "Einzelwert als Beweis oder Widerlegung; Mittelwert über verschiedene Werfer; »unklar« als Versagen. Gegenmittel: Satzgerüst auf der Folie, Klassenübersicht mit allen Gruppen.",
  "bild": "img/mittelwert.png"},
]

RECHNEN = [
    "**Aufgabe 8:** (3,8 + 4,6 + 4,2) m : 3 = 12,6 m : 3 = 4,2 m · (5,1 + 3,9 + 5,4) m : 3 = 14,4 m : 3 = 4,8 m · Spannweite B = 5,4 m − 3,9 m = 1,5 m (A: 0,8 m). Überlappung A 3,8–4,6 m und B 3,9–5,4 m → »unklar«. Werte bewusst unter 5 m: Die Zahlenprüfung erlaubt 2 % Spielraum – bei Mittelwerten über 5 m würde ein Nachbarwert (z. B. 5,1 statt 5,2) als richtig zählen.",
    "**Stopp-Frage Teil 4:** (5,1 + 6,3 + 5,7) m : 3 = 17,1 m : 3 = 5,7 m. **Quiz:** 4,0/5,0/6,0 m → Mittelwert 5,0 m, Spannweite 2,0 m.",
    "**Kapazität Messbahn:** 8 Gruppen × 6 Würfe × 0,5 min = 24 min (Planannahme). Probewürfe 8 × ca. 20 s ≈ 3 min, in der Sicherheitsphase (5 min). Gegenprobe 1 Gruppe × 6 Würfe × 0,5 min = 3 min. Wird es knapp: Gegenprobe entfällt, als Grenze notieren.",
    "**Vorjahr alte 1BK (lang − kurz):** G1 +9,05 · G2 +0,10 · G3 −10,54 · G4 +7,36 · G6 +3,05 · G7 +2,72 · G5 nicht berechenbar. **Alte 1AK:** G1 −0,57 · G2 −2,47 · G3 +6,55 · G4 +6,41 · G5 +4,52 · G6 −1,99 · G7 +3,07.",
]

FEHLVORSTELLUNGEN = [
    ["Eine Theorie ist eine bloße Vermutung.", "Eine wissenschaftliche Theorie verbindet viele geprüfte Befunde und erlaubt Vorhersagen.", "Mythos-Folie im Einstieg; Zelltheorie als Biologie-Beispiel; Aufgabe 2d."],
    ["Oft bestätigte Hypothesen werden zu Gesetzen, Gesetze zu Theorien.", "Gesetz beschreibt, Theorie erklärt – keine Leiter.", "Grafik »zwei Säulen, keine Leiter«; KI-Check Aussage 4."],
    ["Ein passendes Ergebnis beweist die Hypothese.", "Es unterstützt sie unter diesen Bedingungen.", "Gegenprobe mit zweitem Werfer; Forschungskarte (Wiederholung)."],
    ["Ein einziger Gegenwert widerlegt die Hypothese.", "Unsere Hypothese betrifft den Mittelwert – es zählt die ganze Messreihe.", "KI-Check Aussage 2; Übungsdaten A8."],
    ["Schlechte Würfe darf man streichen.", "Nur nach vorher festgelegten Regeln ungültig.", "Aufgabe 5 vor dem Versuch; Prüfer-Rolle."],
    ["Die Klammer wirkt, weil sie schwerer ist.", "Masse und Schwerpunkt ändern sich gleichzeitig – der Test trennt sie nicht.", "Stopp-Frage Teil 2; Schlussfolgerung im Protokoll."],
    ["Nicht prüfbar heißt falsch.", "Es heißt: mit Messungen nicht entscheidbar.", "Aufgabe 12 e; Popper-Folie."],
    ["Eine abweichende Gruppe hat falsch gemessen.", "Erst Bedingungen und Protokoll prüfen.", "Vorjahresdaten (A6), Gruppe 3 der alten 1BK."],
]

FRAGEN = [
    ("Ist die Evolutionstheorie dann auch »nur eine Theorie«?", "Sie ist eine wissenschaftliche Theorie im starken Sinn: Sie verbindet Fossilien, Genetik, Anatomie und Beobachtungen an heutigen Arten und macht prüfbare Vorhersagen."),
    ("Gibt es in der Naturwissenschaft überhaupt Beweise?", "In der Mathematik ja. In den Naturwissenschaften sprechen wir von gut gestützten Ergebnissen – sie gelten, bis neue Befunde etwas anderes zeigen."),
    ("Warum dürfen wir den schlechten Wurf nicht streichen?", "Weil wir sonst nur die passenden Werte behalten – das Ergebnis würde unsere Erwartung bestätigen, egal was wirklich passiert."),
    ("Warum fliegt ein Flieger mal links, mal rechts?", "Kleinste Asymmetrien in Faltung und Abwurf, Luftbewegungen. Genau deshalb wiederholen wir und vergleichen Mittelwerte."),
    ("Warum haben viele Semmelweis nicht geglaubt?", "Seine Erklärung passte nicht zu den damaligen Vorstellungen, Erreger waren unbekannt, und viele Ärzte fühlten sich angegriffen. Er hatte Unterstützer (z. B. Skoda, Hebra), veröffentlichte seine Daten aber erst 1861 selbst ausführlich. Gute Daten setzen sich nicht immer sofort durch – Veröffentlichung und Prüfung durch andere gehören dazu."),
    ("Ist ein Computermodell auch ein Modell?", "Ja – z. B. Wettermodelle. Auch sie vereinfachen und haben Grenzen; darum vergleicht man sie mit Messungen."),
    ("Warum werden so viele Studien nicht wiederholt?", "Wiederholungen bringen wenig Ansehen und Geld, und oft fehlen Angaben zur Methode. Darum ist ein genaues Protokoll so wichtig."),
    ("Ist Astrologie eine Wissenschaft?", "Ihre Vorhersagen wurden geprüft und haben sich nicht bestätigt; vage Aussagen sind kaum prüfbar. Das ist der Unterschied zu einer wissenschaftlichen Hypothese."),
    ("Wie testet das Bundesheer neue Ausrüstung?", "Allgemein gilt: vorher festgelegte Kriterien, Vergleich mit der alten Ausrüstung unter gleichen Bedingungen, mehrere Durchgänge, Protokoll – genau wie unser Test (keine Angaben zu konkreten Verfahren)."),
    ("Biologie-Brücke: Warum macht man Medikamentenstudien »doppelt verblindet«?", "Weder Patient noch Arzt wissen, wer das Medikament bekommt – so beeinflussen Erwartungen das Ergebnis nicht. Unsere feste Messregel erfüllt einen ähnlichen Zweck."),
]

VIDEO_NOTIZ = {
    "apolin1": "Martin Apolin, »Hypothese und Theorie – Teil 1« (YouTube, Link aus der bisherigen E3-PPP, Altfolie 6). Stephan verwendet beide Teile regelmäßig. Inhalt und Länge von hier nicht prüfbar (YouTube gesperrt) – vorher ansehen; im Zeitplan nicht enthalten (Theorieteil zum Selbstansehen bzw. bei Reserve).",
    "apolin2": "Martin Apolin, »Hypothese und Theorie – Teil 2« mit Popper (Altfolie 7). Wie Teil 1. Gut zu Teil 4 »Widerlegbar muss es sein«.",
    "altfolie18": "»So funktioniert Fliegen wirklich« (Altfolie 18, https://www.youtube.com/watch?v=VH0k0H7MgWc&t=234s) – nur als Anknüpfung für die Kraft-Einheit, in E3 nicht eingebaut (Inhalt nicht prüfbar; Auftriebserklärung vorher prüfen: keine »gleichzeitige Ankunft an der Hinterkante«).",
    "podcast": "Ö1 »Dimensionen«: Peer Review und Open Science (2020, ca. 24 min, Jahresplan P03-03 »Kernvorschlag«, eigene Sammlung) – im Theorieteil als Hör-Tipp genannt, Ausschnitt nur bei Reserve in Teil 3. Alternativen laut Jahresplan: P03-01 Biologie Passion Podcast Folge 034 Meselson-Stahl (12 min), P03-02 Forschungsquartett (14 min).",
}

AUSBLICK = ("Danach laut Stephan direkt »Physik – Kraftbegriff« (1AK ab Do 12.11., 2. Stunde; 1BK nach dem 11.11.). Der Flieger bleibt als Anknüpfung: Kräfte nach dem Loslassen, Luftwiderstand, "
            "später Geschwindigkeit (v = s/t auf festgelegter Strecke), Arbeit/Energie und elektrische Kräfte (Ballon und Papierschnipsel). V1.7 (E5, fünf Würfe je Modell, Messunsicherheit) bleibt eigene Aktivität. "
            "Den Konstruktionszyklus (MINT AB 2.1) dort ausführlich aufgreifen: ein Merkmal gezielt verändern, nachdem die Ausgangsmessung steht.")

BILDER = [  # Bildverzeichnis: (Quelle, Seite/Ausschnitt, Art, Einsatz, Zweck)
    ("Trauner NAWI HAK 1", "S. 29 (Foto image(2), rechte Seite)", "übernommene Buchabbildung – nur Beamer/Lehrer", "TH-Unterricht »Lesen im Buch S. 29«, TH-Lehrer", "Leseauftrag sichtbar machen"),
    ("Hölzel NAWI HAK 1", "S. 14 Abb. 1.2.1 (acht Schritte)", "inhaltliche Nutzung, neu gezeichnet", "img/kreislauf.png (Theorie Teil 3, PPP)", "Forschungskreislauf mit Rückpfeilen"),
    ("NAWI-Buch, Titel unbekannt (Upload image(20261028-065601))", "S. 13 Abb. 13.1/13.2", "inhaltliche Nutzung, neu gezeichnet", "img/beob_exp.png", "Beobachten vs. Experimentieren, qualitativ/quantitativ"),
    ("Physikband, Titel unbekannt (Upload image(10))", "S. 189 Abb. 21.2 Zielscheiben", "Idee, neu gezeichnet", "img/zielscheiben.png (Für Schnelle, A11)", "zufällige vs. systematische Fehler"),
    ("Gruber, Ballons, Raketen und Papierflieger", "S. 34–35, 4.4 Planarflieger (einfach), Variante 6b", "Faltfolge neu gezeichnet und in eigenen Worten", "img/faltanleitung.png, Theorie Teil 1, PPP", "gemeinsame Bauvorlage"),
    ("MINT-Modul »Vom Binärsystem zum Papierflieger«", "AB 2.1 Konstruktionszyklus", "inhaltliche Nutzung, neu gezeichnet", "img/zyklus.png, A10", "Forschen vs. Konstruieren"),
    ("Bisherige E3-PPP (Stephan)", "Altfolien 24 und 28 (Tabellen)", "Daten übernommen, neu gesetzt", "img/vorjahr.png, A6", "echte Vorjahresdaten kritisch lesen"),
    ("eigene Grafiken", "–", "selbst gezeichnet", "flieger.png, theorie.png, messbahn.png, landung.gif, mittelwert.png, d_v1.png", "Einstieg, Begriffe, Aufbau, Messregel, Auswertung"),
]

QUELLEN = [
    "**Grundlage:** ChatGPT-Übergabe »E3 – Erkenntnisgewinn« v4 (28.10.2026) mit Quellenpaket – Planung, Quellenauswahl, Altfolien-Auswahl und fachliche Korrekturen übernommen und von Claude nachgeprüft (Prüfbericht).",
    "**Trauner NAWI HAK 1** S. 28–29 (Foto) – Kern; Aufgabenkasten »Erkenntnisgewinn« (Ausschnitt ohne Seitenzahl, Kap. 4) → A2. S. 30–32 nicht vollständig gesehen.",
    "**Hölzel NAWI HAK 1** S. 13–21, 24–25 (Fotos): S. 14 Kreislauf → Teil 3; S. 15 Ü1.2 (wirtschaftliche/ethische Fragen) → Idee für A3 d; S. 19–20 Mondmodelle geprüft, nicht übernommen (Zeit, Astronomie); S. 21 Protokoll → VS-AB.",
    "**Weitere Buchbilder:** NAWI-Buch S. 13–15 (Beobachten/Experimentieren, Modelle) → Teil 1/3; Physikband S. 188–191 (Fehlerarten, Peer Review) → A11, Teil 3; Paradigmenwechsel und Standardabweichung nicht übernommen.",
    "**Bücher im Projekt durchsucht (project_search 29.10.2026):** Hölzel S. 16–17 Erde als Kugel (Theorie → abgeleitete Hypothese → Weltumsegelung) – geprüft, nicht übernommen (Weltumsegelung belegt nicht alle Eigenschaften der Erde); Hölzel S. 21 Protokollaufbau → VS-AB; Hölzel V1.3 »Wer misst am genauesten?« (dreimal wiederholen) → Begründung für Wiederholungen; Trauner Versuch »Luftreibung« (Buch und Papier fallen lassen, Kap. Mechanische Kräfte) → Ausblick Kraft; Expedition Physik 4 »Kriterien zur Zuverlässigkeit von Internetquellen« → Idee zu A9 (KI-Check). Westermann Chemie, Treffpunkt Chemie, El-Mo, Chemie muss stimmen: nichts Passenderes zu Hypothese/Papierflieger.",
    "**Gruber, Ballons, Raketen und Papierflieger** (78 S.): S. 34–35 Faltvorlage; S. 20–28 Lehrerhintergrund mit Korrektur (kein Schub nach dem Loslassen).",
    "**MINT-Modul »Vom Binärsystem zum Papierflieger«** 2.0–2.2: Konstruktionszyklus → A10; Lösungsblatt präzisiert (V-Stellung ≠ Anstellwinkel; »je leichter, desto besser« nicht pauschal).",
    "**Fachquellen:** National Academy of Sciences, Teaching About Evolution and the Nature of Science (1998), Kap. 1 und Glossar; National Research Council, A Framework for K-12 Science Education (2012), Kap. 3; NZ Ministry of Education »Paper planes – Level 4« (Vergleichslogik); NASA Glenn »Gliders«, »Vector Balance of Forces – Glider« (Kraftbild, für später).",
    "**Selbst geprüft (29.10.2026):** eLife 75830, Rodgers & Collings »Reproducibility in Cancer Biology: What have we learned?« (7.12.2021); Originalarbeiten Errington u. a., eLife 71601 und 67995 → Forschungskarte A13; Wikipedia »Ignaz Semmelweis« (Sterblichkeitszahlen 1841–1847) → Einstieg.",
    "**Jahresplan v64:** Zeile 7, Codes K01/N06/GLV 2, Versuche V1.4 (überarbeitet) und V1.7 (nicht vorgezogen), Podcasts P03-01–03, Didaktik & Übersicht.",
    "**Inventar (Stand 25.10.2026):** #9 Bandmaß 20 m, #10 Bandmaß 3 m (E21, aktuelle Zählung leer), F-038 Büroklammern (»sehr viele«), Kreide und A4-Papier nicht im Inventar.",
    "**Nicht prüfbar von hier:** Apolin-Videos (YouTube hier gesperrt) – Stephan hat bestätigt, dass sie bei ihm laufen; Ö1-Podcast (eigene Sammlung). Keine weiteren Videos ungeprüft eingebaut.",
]
