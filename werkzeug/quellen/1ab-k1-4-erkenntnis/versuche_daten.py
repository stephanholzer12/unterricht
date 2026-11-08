"""Versuch K1.4-V1 Papierflieger mit und ohne Büroklammer (1AB) – eine Quelle für versuche.html, VS-Word, VS-PPP, Herrichte-Liste und Lösungsmappe.
= Jahresplan V1.4 »Papierflieger-Wettbewerb: Hypothese und Gegenprobe« (v64, Blatt Versuche, Zeile 7), überarbeitet nach ChatGPT-Übergabe v4, Abschnitt 11 und 14.
Material: [Text auf der Seite, Icon, Herrichte-Schlüssel, Stück je Ansatz]. Eine gemeinsame Messbahn im Eingangsbereich; Flieger, Klammer, Papier je Gruppe.
Status: dokumentiert und angepasst, NICHT praktisch erprobt – Vorversuch (Hallenprobe) durch Stephan, siehe VS-Fachwissen.
Stand 08.11.2026 (Stephan): vereinfacht, weil die Zeit nicht reichte – jede Gruppe wirft nur EINMAL A (ohne Klammer) und EINMAL B (mit Klammer) = ein Paar.
Kein Probewurf im Versuch (Testflüge machen die Kadetten vorher), keine Gegenprobe. Ausgewertet werden die Werte der GANZEN KLASSE (Klassentabelle, Stunde 4).
Die alten Zeilen der Messtabelle (Paar 2/3, Mittelwert/Spannweite je Gruppe, Gegenprobe) bleiben im Speicher der Seite erhalten (Schlüssel b1…b7) und sind nur sichtbar, wenn dort schon etwas steht."""
import inhalt as I

GRUPPEN = 8  # Maximal pro Klasse: 1AK 28 Kadetten = 7 Vierergruppen; 1BK 29 Kadetten = 5 Vierergruppen + 3 Dreiergruppen

# Herrichte-Schlüssel → (Bezeichnung, Icon, Inventar-Nr. / Fundort, Bestand laut Inventar, Art) – Art: "chem" Chemikalie/Verbrauchsmaterial, "geraet" Gerät/Lehrmittel
LM = {
    "papier": ("A4-Kopierpapier, 80 g/m², alle aus demselben Packen", "papier", "Kopierraum / Sekretariat – kein Inventar-Eintrag (»A-Papier: nicht im Inventar/prüfen«)", None, "chem"),
    "klammer": ("Büroklammer aus Metall, alle gleich groß (je Gruppe dieselbe für die ganze Reihe)", "klammer", "Ergänzung F-038 · NAWI-Saal E21", "sehr viele (nicht gezählt)", "geraet"),
    "bandmass": ("Bandmaß 20 m", "bandmass", "Lehrmittel #9 · NAWI-Saal E21 (aktuelle Zählung im Inventar leer → vorher prüfen)", "historisch erfasst: 1, aktuell nicht gezählt", "geraet"),
    "kiste": ("Schachtel oder Mappe für die fertigen Flieger (flach lagern)", "dose", "Klassenraum – kein Inventar", None, "geraet"),
    "handy": ("Handy als Protokoll-Handy (Kadetten)", "handy", "Geräte der Kadetten – kein Inventar", None, "geraet"),
    "bleistift": ("Bleistift (Gruppennummer auf den Flügel)", "bleistift", "Kadetten", None, "geraet"),
}
JE_GRUPPE = {"papier", "klammer", "handy", "bleistift"}  # braucht jede Gruppe selbst; Bandmaß und Kiste gibt es einmal

# ---------------------------------------------------------------- Messtabelle
# Die Zeilen-Nummer ist der Speicherschlüssel auf der Seite (b<Zeile>_<Spalte>). Zeilen 0–7 gab es schon (Stand 05.11.), sie behalten ihre Nummer.
# ALT = frühere Zeilen: auf der Webseite nur sichtbar, wenn dort schon etwas eingetragen ist; in Word, Folien und Mappe fehlen sie.
ZEILEN_VOLL = (
    [["Unser Wurfpaar"],
     ["Weiteres Paar 2 – Würfe 3 und 4 (schon gemessen)"], ["Weiteres Paar 3 – Würfe 5 und 6 (schon gemessen)"],
     ["Mittelwert nur eurer Gruppe (schon eingetragen)"], ["kleinster – größter Wert nur eurer Gruppe (schon eingetragen)"],
     ["Gegenprobe Paar 1 (schon eingetragen)"], ["Gegenprobe Paar 2 (schon eingetragen)"], ["Gegenprobe Paar 3 (schon eingetragen)"]]
    + [["Klassentabelle · Gruppe %d" % g] for g in range(1, 9)]
    + [["Mittelwert der Klasse"], ["kleinster – größter Wert"],
       ["Gruppen, die weiter flogen (Zahl)"]])
ALT = [1, 2, 3, 4, 5, 6, 7]
SICHTBAR = [i for i in range(len(ZEILEN_VOLL)) if i not in ALT]   # Zeilen für Word, Folien, Mappe
ZEILEN = [ZEILEN_VOLL[i] for i in SICHTBAR]

# Beispielwerte (NICHT gemessen): acht Gruppen, ein Paar je Gruppe
BEISPIEL = [(5.3, 5.9, "–"), (4.9, 6.2, "Decke bei B"), (5.6, 5.4, "–"), (6.1, 6.0, "–"), (4.4, 5.7, "–"), (5.8, 5.2, "–"), (5.0, 5.5, "–"), (4.7, 5.9, "–")]
_A = [b[0] for b in BEISPIEL]; _B = [b[1] for b in BEISPIEL]
_mA, _mB = sum(_A) / 8, sum(_B) / 8
_nA = sum(1 for a, b in zip(_A, _B) if a > b); _nB = sum(1 for a, b in zip(_A, _B) if b > a)
assert (round(_mA, 1), round(_mB, 1), _nA, _nB) == (5.2, 5.7, 3, 5) and min(_A) == 4.4 and max(_A) == 6.1 and min(_B) == 5.2 and max(_B) == 6.2
_kom = lambda x: ("%.1f" % x).replace(".", ",")
ERWARTET_TAB = ([["z. B. " + _kom(BEISPIEL[0][0]), "z. B. " + _kom(BEISPIEL[0][1]), "–"]]
                + [[_kom(a), _kom(b), c] for a, b, c in BEISPIEL]
                + [[_kom(_mA), _kom(_mB), ""], [_kom(min(_A)) + "–" + _kom(max(_A)), _kom(min(_B)) + "–" + _kom(max(_B)), ""], [str(_nA), str(_nB), ""]])
assert len(ERWARTET_TAB) == len(ZEILEN)
# Kurzfassung für die Folie »Messwerte & Erkenntnis« und die Lösungsmappe (fünf Zeilen)
ZEILEN_FOLIE = [["Unser Wurfpaar"], ["Klassentabelle (Gruppe 1–8)"], ["Mittelwert der Klasse"], ["kleinster – größter Wert der Klasse"], ["Gruppen, in denen dieser Zustand weiter flog"]]
TAB_FOLIE = [ERWARTET_TAB[0], ["8 Zeilen, siehe Protokoll", "", ""], ERWARTET_TAB[-3], ERWARTET_TAB[-2], ERWARTET_TAB[-1]]

VS = [
 {"id": "flieger", "nr": I.VS_ID, "titel": I.VS_TITEL, "bindung": "Hypothese und Wiederholung durch alle Gruppen · eine gemeinsame Messbahn im Eingangsbereich",
  "platz": "Eingangsbereich, gemeinsame Messbahn (Abwurflinie an der Bodenfuge, Bandmaß am Rand). Nicht im NAWI-Saal: kein Lehrertisch, kein Mobiltisch, keine Wasserleitung nötig. Keine Flamme, kein Beamer – es gilt das Papierblatt der Gruppe. Platzverteilung ist ein Vorschlag.",
  "gefahren": [["Chemikalien", "keine – nur Papier und Büroklammer", "nichts zu ersetzen"], ["Ansetzen / Verdünnen", "nichts nötig", "–"], ["Abzug / Flamme", "nicht nötig", "–"],
               ["Restgefahr", "Flieger in Gesichtshöhe, Durchgangsverkehr im Eingangsbereich, Rennen auf glattem Boden", "flach aus Hüfthöhe, Bahn frei, Wurf nur auf Kommando, Fluchtweg frei, Schulwart informieren"]],
  "stunde": 2, "wann": "1AK: Stunde 2 (Do 05.11., 2. Std.) · 1BK: Stunde 3 (Mo 09.11.)", "form": "Gruppenversuch an einer gemeinsamen Messbahn", "kern": True, "zeit": 28,
  "jp": "= Jahresplan V1.4 (überarbeitet: derselbe Flieger ohne/mit Klammer statt zwei verschiedener Modelle; seit 08.11.2026 nur ein Paar je Gruppe, Auswertung mit den Werten der ganzen Klasse). Nicht verwechseln mit V1.7 (E5, fünf Würfe je Modell).",
  "quelle": "Trauner S. 28–32 (Theoriebezug, kein Buchversuch); Faltung: W. Gruber, »Ballons, Raketen und Papierflieger«, 4.4 Planarflieger (einfach), S. 34–35; "
            "Vergleichslogik: NZ Ministry of Education »Paper planes – Level 4«; Altfolien 13–31 der bisherigen PPP (Vorjahresdaten)",
  "intro": "Ihr prüft: Fliegt derselbe Papierflieger mit einer Büroklammer anders als ohne? A = ohne Klammer. B = mit Klammer. Jede Gruppe wirft einmal A und einmal B. Das ist ein Paar. Weil jede Gruppe nur ein Paar hat, wertet ihr in Stunde 4 die Werte der ganzen Klasse gemeinsam aus. Eure Vermutung steht bereits im Arbeitsblatt.",
  "sicher": "Nur werfen, wenn die Bahn frei ist – nie in Richtung von Personen. Flach und ruhig aus Hüfthöhe werfen, kein Kraftwurf. Nicht zum Flieger rennen. Der Messer steht seitlich außerhalb der Bahn. Das Bandmaß liegt am Rand, nicht quer im Weg. Eingang und Fluchtweg bleiben frei.",
  "mat": [["A4-Papier: 1 Blatt für den Flieger + 1 Reserve", "papier", "papier", 2], ["Büroklammer (dieselbe für die ganze Reihe)", "klammer", "klammer", 1],
          ["Bandmaß 20 m (eines für alle, am Rand der Messbahn)", "bandmass", "bandmass", 1], ["Protokoll-Handy", "handy", "handy", 1], ["Schachtel für die fertigen Flieger (eine für die Klasse)", "dose", "kiste", 1],
          ["Bleistift für die Gruppennummer", "bleistift", "bleistift", 1]],
  "entsorgung": "Flieger mit Gruppennummer abgeben (für Stunde 4 und das Kraft-Kapitel). Büroklammern zurück in die Schachtel, Bandmaß aufrollen. Papierreste ins Altpapier.",
  "schritte": [
    "Teilt die Rollen auf: Ein Kadett wirft beide Würfe. Ein Kadett misst die Weite. Ein Kadett trägt die Werte ein. In Vierergruppen prüft der vierte Kadett die Regeln.",
    "Eure Testflüge habt ihr schon gemacht. Ab jetzt ändert ihr nichts mehr am Flieger und an eurer Wurftechnik.",
    "Seht oben unter „So laufen die Versuche“ nach, womit eure Gruppe beginnt. Gruppen 1, 3, 5 und 7 werfen zuerst A, dann B. Gruppen 2, 4, 6 und 8 werfen zuerst B, dann A.",
    "Wartet, bis Prof. HOLZER eure Gruppe aufruft. Dann stellt sich der Werfer hinter die Abwurflinie. Werft ruhig und flach aus Hüfthöhe.",
    "Wechselt zwischen den Würfen die Klammer. Beginnt eure Gruppe mit A, steckt ihr die Klammer nach dem ersten Wurf vorne an den Rumpf. Beginnt eure Gruppe mit B, nehmt ihr sie nach dem ersten Wurf ab.",
    "Messt vom Abwurfpunkt bis zur ersten Stelle, an der der Flieger den Boden berührt. Tragt die Weite sofort in das passende Feld ein, in Metern mit einer Nachkommastelle, zum Beispiel 4,6 m. A = ohne Klammer, B = mit Klammer. Berührt der Flieger Decke oder Wand, notiert das in der letzten Spalte. Ist ein Wurf ungültig (zum Beispiel Fuß über der Linie), wiederholt ihn.",
    "Schreibt beide Werte auch auf das Papierblatt und gebt es Prof. HOLZER. Klassentabelle, Mittelwerte und Spannweiten füllt ihr erst in Stunde 4 aus."
  ],
  "skizze": "v1",
  "beob": {"titel": "Tragt eure Messwerte ein",
           "kopf": ["Zeile", "A ohne Klammer in m", "B mit Klammer in m", "Decke/Wand oder Auffälliges"],
           "zeilen": ZEILEN},
  "beob_web": {"titel": "Tragt eure Messwerte ein", "kopf": ["Zeile", "A ohne Klammer in m", "B mit Klammer in m", "Decke/Wand oder Auffälliges"], "zeilen": ZEILEN_VOLL, "alt": ALT},
  "beob_folie": {"kopf": ["Zeile", "A ohne Klammer", "B mit Klammer"], "zeilen": ZEILEN_FOLIE, "tab": TAB_FOLIE},
  "erk": "Vergleicht die Werte der ganzen Klasse: Welcher Zustand flog im Mittel weiter – und um wie viel? In wie vielen Gruppen flog B weiter als A? Wie stark streuen die Werte? Gab es Kontakte mit Decke oder Wand?",
  "interp": "Unterstützen die Werte der Klasse eure Hypothese, sprechen sie dagegen oder sind sie unklar? Begründe mit den Mittelwerten, den Spannweiten und der Anzahl der Gruppen, in denen B weiter flog.",
  "schluss": "Nenne eine Grenze eures Versuchs und eine Änderung, die beim nächsten Mal die Unsicherheit verkleinert. Auch beim Heer wird neue Ausrüstung so erprobt: mit vorher festgelegtem Kriterium und mehreren Durchgängen.",
  "buch": {"s": "S. 28–32", "kap": "4 Erkenntnisgewinn in den Naturwissenschaften: 4.1 Von der Hypothese zur Theorie, 4.2 Wissenschaftliche Forschung (S. 29)", "versuch": False},
  "erwartet": [["Ergebnis", "offen – es wird bewusst keine Wirkung der Klammer vorweggenommen. Der Planarflieger hat schon eine schwere Vorderkante; ob die Klammer im Eingangsbereich hilft oder schadet, zeigt erst die Messung."],
               ["Streuung", "Von Hand geworfen streuen die Weiten deutlich (Erfahrung Vorjahr: Werte einer Klasse zwischen ca. 1,8 m und 15 m – andere Flieger, je ein Wurf). Mit nur einem Wurf je Zustand und Gruppe ist die Spannweite der Klasse eher größer als 1 m."],
               ["Kontakte", "Bei flachem Abwurf aus Hüfthöhe sollten Deckenkontakte selten sein; im Vorversuch prüfen."]],
  "erwartet_tab": ERWARTET_TAB,
  "erk_l": "Beispiel: »B flog im Mittel 0,5 m weiter (5,7 m statt 5,2 m). B war in 5 von 8 Gruppen weiter, A in 3. A streut von 4,4 m bis 6,1 m, B von 5,2 m bis 6,2 m – die Bereiche überlappen stark. Ein Deckenkontakt gab es nur bei B (Gruppe 2).« – Eure Werte und Aussage sind entscheidend, nicht das Beispiel (die Beispielwerte sind nicht gemessen).",
  "interp_l": "Begründet eingeordnet, bezogen auf die EIGENE Vorhersage: unterstützt (klar in die vorhergesagte Richtung, wenig Überlappung, die Mehrzahl der Gruppen zeigt dasselbe) · spricht dagegen (klar das Gegenteil) · unklar (kleiner Unterschied bei starker Überlappung, gemischtes Bild in den Gruppen oder ungleich viele Kontakte). Im Beispiel: unklar, weil der Unterschied nur 0,5 m beträgt, die Werte stark überlappen, B nur in 5 von 8 Gruppen weiter flog und der Kontakt nur bei B war. Die Begründung (»weil …«) prüft der Test nicht.",
  "schluss_l": "Grenzen: nur ein Wurf je Zustand und Gruppe, Wurfkraft von Hand nie gleich, je Gruppe ein anderer Werfer und ein eigener Flieger, niedrige Decke, Klammer ändert Masse UND Schwerpunkt. Verbesserung z. B.: mehr Würfe je Gruppe, Startrampe oder Gummischleuder für gleichen Abwurf, derselbe Werfer für alle Gruppen, mehrere Flieger je Gruppe.",
  "lehrer": ["Vorversuch (Hallenprobe) VOR der ersten Stunde im Eingangsbereich: einen Planarflieger falten, je 3–4 ruhige Würfe ohne und mit Klammer aus Hüfthöhe. Fliegen beide ohne Deckenkontakt? Wie weit ungefähr? Reicht die Länge? Klammersitz hält?",
             "Abwurflinie: eine Bodenfuge wählen (Kreide nicht im Inventar). Bandmaß #9 (20 m) am Rand auslegen, Nullpunkt an der Fuge. Zustand des Bandmaßes vorher prüfen – im Inventar ist keine aktuelle Zählung eingetragen.",
             "Papier: ein Packen 80-g-Kopierpapier für alle Gruppen (nicht im Inventar → Kopierraum). Büroklammern F-038: je Gruppe eine, alle aus derselben Schachtel und gleich groß.",
             "Kapazität einer Messbahn (vereinfacht seit 08.11.2026): 8 Gruppen × 2 Würfe × ca. 30 s ≈ 8 min, dazu Klammer anstecken/abnehmen und Wechsel ≈ 6 min, also rund 14 min (Planannahmen, nicht gemessen). Kein Probewurf im Versuch: Die Testflüge machen die Kadetten vorher beim Bauen. Es gibt keine Gegenprobe mehr. Wird es langsamer: Gruppen, die nicht mehr drankommen, schreiben die Werte einer Nachbargruppe ab (als »übernommene Werte« kennzeichnen).",
             "Wartende Gruppen: Prüfer beobachtet die werfende Gruppe (Linie, Bahn frei), der Rest ist beim nächsten Wurf bereit. Reihenfolge der Gruppen: 1 bis 8 nacheinander; ungerade Gruppen beginnen mit A, gerade mit B (so trifft Übung, Ermüdung und Verformung beide Zustände gleich).",
             "Daten sichern: Protokoll-Handy speichert im Browser; zusätzlich Papierblatt (VS-AB) je Gruppe mit den zwei Werten, das du am Ende einsammelst. In Stunde 4 tragen die Gruppensprecher ihre zwei Werte an der Tafel in die Klassentabelle ein (Zeile = Gruppennummer), alle übertragen sie ins Protokoll. 1AK: Daten vom 05.11. bis 12.11. aufbewahren, 1BK: vom 09.11. bis 11.11.",
             "1AK hat den Versuch am 05.11. noch mit drei Paaren gemacht: Wer mehr als ein Paar eingetragen hat, sieht die Zeilen »Weiteres Paar 2/3« weiter. Für die Klassentabelle gilt bei allen Gruppen nur das erste Paar (»Unser Wurfpaar«).",
             "1BK baut am 04.11. und fliegt am 09.11.: Flieger flach in einer Schachtel lagern, Gruppennummer auf dem Flügel. Vor dem Test kurz auf Knicke prüfen – verbogene Flieger bei den Testflügen korrigieren, danach nicht mehr."],
  "fehler": ["Nur die guten Würfe eingetragen oder kurze Würfe als »Fehlwurf« gestrichen.", "Gemessen bis zum Stillstand statt bis zum ersten Bodenkontakt.",
             "Zwischen den Würfen am Flieger nachgebogen oder die Klammer verschoben.", "Werfer gewechselt, ohne es zu notieren; Werte zweier Werfer zusammen gemittelt.",
             "Deckenkontakte gelöscht oder durch 0 ersetzt."],
  "fach": ["Die Klammer ändert Masse und Schwerpunktlage gleichzeitig und klemmt den Rumpf zusammen (Flügelstellung in der Hallenprobe ansehen). Der Test zeigt die Wirkung dieser einen Änderung – er trennt die beiden Ursachen nicht.",
           "Hier fliegt jede Gruppe mit ihrem EIGENEN Flieger und einem eigenen Werfer, einmal pro Zustand. Das Paar einer Gruppe sagt allein fast nichts; erst die Werte der Klasse zusammen (7–8 Paare) erlauben einen Vergleich. Die Streuung enthält Werfer, Faltung und Zufall. Das ist ein Unterrichtskompromiss, kein Wirksamkeitsnachweis; keine Standardabweichung oder Signifikanz verlangen.",
           "Die Reihenfolge (ungerade Gruppen A, B – gerade B, A) verteilt Übungs- und Verformungseffekte auf beide Zustände. Bei nur einem Paar je Gruppe ist das die einzige Kontrolle dafür.",
           "Nach dem Loslassen wirkt keine Wurfkraft mehr: Im Gleitflug wirken Gewichtskraft und die Luftkraft (aufgeteilt in Auftrieb und Widerstand). Gruber S. 20 zeichnet einen fortwirkenden »Schub« – für den antriebslosen Flug nicht übernehmen."],
  "vorversuch": "Hallenprobe im Eingangsbereich: Faltung (ca. 10 min für Ungeübte?), Klammersitz, flacher Abwurf ohne Deckenkontakt mit und ohne Klammer, nutzbare Länge, freier Bereich ohne Durchgangsverkehr."},
]
assert [v["nr"] for v in VS] == [I.VS_ID]

SICHERHEIT = [("Bahn frei", "nur werfen, wenn niemand in der Flugbahn steht oder geht – nie in Richtung von Personen"),
              ("Flach werfen", "ruhig aus Hüfthöhe, kein Kraftwurf, kein hoher Bogen – die Decke ist niedrig"),
              ("Nicht rennen", "erst nach der Landung zum Flieger gehen, messen, zurückholen"),
              ("Stolperfallen", "Bandmaß am Rand, Taschen weg vom Boden, Eingang und Fluchtweg bleiben frei"),
              ("Büroklammer", "nicht aufbiegen; den Flieger mit Klammer nie in Richtung Gesicht oder Personen werfen")]
