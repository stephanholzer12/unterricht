"""Versuch K1.4-V1 Papierflieger mit und ohne Büroklammer (1AB) – eine Quelle für versuche.html, VS-Word, VS-PPP, Herrichte-Liste und Lösungsmappe.
= Jahresplan V1.4 »Papierflieger-Wettbewerb: Hypothese und Gegenprobe« (v64, Blatt Versuche, Zeile 7), überarbeitet nach ChatGPT-Übergabe v4, Abschnitt 11 und 14.
Material: [Text auf der Seite, Icon, Herrichte-Schlüssel, Stück je Ansatz]. Eine gemeinsame Messbahn im Eingangsbereich; Flieger, Klammer, Papier je Gruppe.
Status: dokumentiert und angepasst, NICHT praktisch erprobt – Vorversuch (Hallenprobe) durch Stephan, siehe VS-Fachwissen."""
import inhalt as I

GRUPPEN = 8  # Klassengröße nicht bestätigt → Regelwerk: 8 Gruppen annehmen (3–4 Kadetten); bei weniger Kadetten weniger Gruppen

# Herrichte-Schlüssel → (Bezeichnung, Icon, Inventar-Nr. / Fundort, Bestand laut Inventar, Art) – Art: "chem" Chemikalie/Verbrauchsmaterial, "geraet" Gerät/Lehrmittel
LM = {
    "papier": ("A4-Kopierpapier, 80 g/m², alle aus demselben Packen", "papier", "Kopierraum / Sekretariat – kein Inventar-Eintrag (»A-Papier: nicht im Inventar/prüfen«)", None, "chem"),
    "klammer": ("Büroklammer aus Metall, alle gleich groß (je Gruppe dieselbe für die ganze Reihe)", "klammer", "Ergänzung F-038 · NAWI-Saal E21", "sehr viele (nicht gezählt)", "geraet"),
    "bandmass": ("Bandmaß 20 m", "bandmass", "Lehrmittel #9 · NAWI-Saal E21 (Zählung im Inventar leer → vorher prüfen)", 1, "geraet"),
    "kiste": ("Schachtel oder Mappe für die fertigen Flieger (flach lagern)", "dose", "Klassenraum – kein Inventar", None, "geraet"),
    "handy": ("Handy als Protokoll-Handy (Kadetten)", "handy", "Geräte der Kadetten – kein Inventar", None, "geraet"),
    "bleistift": ("Bleistift (Gruppennummer auf den Flügel)", "bleistift", "Kadetten", None, "geraet"),
}
JE_GRUPPE = {"papier", "klammer", "handy", "bleistift"}  # braucht jede Gruppe selbst; Bandmaß und Kiste gibt es einmal

VS = [
 {"id": "flieger", "nr": I.VS_ID, "titel": I.VS_TITEL, "bindung": "Hypothese und Gegenprobe · eine gemeinsame Messbahn im Eingangsbereich",
  "stunde": 2, "wann": "1AK: Stunde 2 (Do 05.11., 2. Std.) · 1BK: Stunde 3 (Mo 09.11.)", "form": "Gruppenversuch an einer gemeinsamen Messbahn", "kern": True, "zeit": 45,
  "jp": "= Jahresplan V1.4 (überarbeitet: derselbe Flieger ohne/mit Klammer statt zwei verschiedener Modelle). Nicht verwechseln mit V1.7 (E5, fünf Würfe je Modell).",
  "quelle": "Trauner S. 28–32 (Theoriebezug, kein Buchversuch); Faltung: W. Gruber, »Ballons, Raketen und Papierflieger«, 4.4 Planarflieger (einfach), S. 34–35; "
            "Vergleichslogik: NZ Ministry of Education »Paper planes – Level 4«; Altfolien 13–31 der bisherigen PPP (Vorjahresdaten)",
  "intro": "Macht eine Büroklammer vorne am Rumpf euren Flieger besser? Ihr vergleicht denselben Flieger ohne Klammer (A) und mit Klammer (B) – dreimal abwechselnd, mit festen Regeln. Eure Hypothese steht schon fest (Aufgabe 4).",
  "sicher": "Nur werfen, wenn die Bahn frei ist – nie in Richtung von Personen. Flach und ruhig aus Hüfthöhe werfen, kein Kraftwurf. Nicht zum Flieger rennen. Das Bandmaß liegt am Rand, nicht quer im Weg. Eingang und Fluchtweg bleiben frei.",
  "mat": [["A4-Papier: 1 Blatt für den Flieger + 1 Reserve", "papier", "papier", 2], ["Büroklammer (dieselbe für die ganze Reihe)", "klammer", "klammer", 1],
          ["Bandmaß 20 m (eines für alle, am Rand der Messbahn)", "bandmass", "bandmass", 1], ["Protokoll-Handy", "handy", "handy", 1], ["Schachtel für die fertigen Flieger (eine für die Klasse)", "dose", "kiste", 1],
          ["Bleistift für die Gruppennummer", "bleistift", "bleistift", 1]],
  "entsorgung": "Flieger mit Gruppennummer abgeben (für Stunde 4 und das Kraft-Kapitel). Büroklammern zurück in die Schachtel, Bandmaß aufrollen. Papierreste ins Altpapier.",
  "schritte": ["Rollen festlegen: Werfer (bleibt die ganze Reihe gleich), Messer am Landepunkt, Protokollführer, in Vierergruppen ein Prüfer, der auf die Regeln achtet.",
               "Probewurf mit A (zählt nicht). Danach wird an Flieger und Wurf nichts mehr verändert.",
               "Drei Vergleichspaare: ungerade Gruppen A, B · B, A · A, B – gerade Gruppen B, A · A, B · B, A. Flach aus Hüfthöhe werfen, Fuß hinter der Linie.",
               "Gemessen wird die Weite bis zum ersten Bodenkontakt, entlang des Bandmaßes ab der Abwurflinie, auf 0,1 m gerundet. Nicht dort messen, wo der Flieger nach dem Rutschen liegt.",
               "Nach jedem Wurf sofort eintragen: Weite und Auffälliges. Deckenkontakt: Wert bleibt, Vermerk »Decke«. Ungültig (Fuß über der Linie, Person in der Bahn, Klammer abgefallen): wiederholen und notieren.",
               "Gegenprobe (nur die Gruppen, die Stephan aufruft): Ein zweiter Werfer wirft dieselben drei Paare. Getrennt in den Zeilen »Gegenprobe« eintragen.",
               "Mittelwert und Spannweite rechnet ihr in Stunde 4 aus. Werte heute zusätzlich auf das Papierblatt der Gruppe schreiben – das sammelt Stephan ein."],
  "skizze": "v1",
  "beob": {"titel": "Eure Messwerte in m – alle Würfe, auch die kurzen",
           "kopf": ["Paar", "A ohne Klammer in m", "B mit Klammer in m", "Decke/Wand oder Auffälliges"],
           "zeilen": [["Paar 1"], ["Paar 2"], ["Paar 3"], ["Mittelwert (Stunde 4)"], ["kleinster – größter Wert (Stunde 4)"], ["Gegenprobe Paar 1"], ["Gegenprobe Paar 2"], ["Gegenprobe Paar 3"]]},
  "erk": "Vergleicht eure Werte: Welcher Zustand flog im Mittel weiter – und um wie viel? Wie stark streuen die Werte? Gab es Kontakte mit Decke oder Wand?",
  "interp": "Unterstützen eure Daten eure Hypothese, sprechen sie dagegen oder sind sie unklar? Begründe mit Einzelwerten, Spannweite und – wenn vorhanden – der Gegenprobe.",
  "schluss": "Nenne eine Grenze eures Versuchs und eine Änderung, die beim nächsten Mal die Unsicherheit verkleinert. Auch beim Heer wird neue Ausrüstung so erprobt: mit vorher festgelegtem Kriterium und mehreren Durchgängen.",
  "buch": {"s": "S. 28–32", "kap": "4 Erkenntnisgewinn in den Naturwissenschaften: 4.1 Von der Hypothese zur Theorie, 4.2 Wissenschaftliche Forschung (S. 29)", "versuch": False},
  "erwartet": [["Ergebnis", "offen – es wird bewusst keine Wirkung der Klammer vorweggenommen. Der Planarflieger hat schon eine schwere Vorderkante; ob die Klammer im Eingangsbereich hilft oder schadet, zeigt erst die Messung."],
               ["Streuung", "Von Hand geworfen streuen die Weiten deutlich (Erfahrung Vorjahr: Werte einer Klasse zwischen ca. 1,8 m und 15 m – andere Flieger, je ein Wurf). Spannweiten von 1 m und mehr sind normal."],
               ["Kontakte", "Bei flachem Abwurf aus Hüfthöhe sollten Deckenkontakte selten sein; im Vorversuch prüfen."]],
  "erwartet_tab": [["z. B. 5,3", "z. B. 5,9", "–"], ["z. B. 4,9", "z. B. 6,2", "Decke bei B"], ["z. B. 5,6", "z. B. 5,4", "–"], ["5,3", "5,8", ""], ["4,9–5,6", "5,4–6,2", ""], ["", "", ""], ["", "", ""], ["", "", ""]],
  "erk_l": "Beispiel: »B flog im Mittel 0,5 m weiter (5,8 m statt 5,3 m). Die Werte streuen um rund 0,7 m und überlappen. Bei B gab es einen Deckenkontakt.« – Eure Werte und Aussage sind entscheidend, nicht das Beispiel.",
  "interp_l": "Begründet eingeordnet: unterstützt (klar weiter, wenig Überlappung, Gegenprobe ähnlich) · spricht dagegen (gleich weit oder kürzer) · unklar (starke Streuung, Überlappung, Kontakte nur bei einem Zustand). Ein einzelner Wert entscheidet nicht.",
  "schluss_l": "Grenzen: nur drei Paare, Wurfkraft von Hand nie gleich, ein Werfer, niedrige Decke, Klammer ändert Masse UND Schwerpunkt. Verbesserung z. B.: mehr Paare, Startrampe oder Gummischleuder für gleichen Abwurf, zweiter Flieger als Wiederholung.",
  "lehrer": ["Vorversuch (Hallenprobe) VOR der ersten Stunde im Eingangsbereich: einen Planarflieger falten, je 3–4 ruhige Würfe ohne und mit Klammer aus Hüfthöhe. Fliegen beide ohne Deckenkontakt? Wie weit ungefähr? Reicht die Länge? Klammersitz hält?",
             "Abwurflinie: eine Bodenfuge wählen (Kreide nicht im Inventar). Bandmaß #9 (20 m) am Rand auslegen, Nullpunkt an der Fuge. Zustand des Bandmaßes vorher prüfen – im Inventar ist keine aktuelle Zählung eingetragen.",
             "Papier: ein Packen 80-g-Kopierpapier für alle Gruppen (nicht im Inventar → Kopierraum). Büroklammern F-038: je Gruppe eine, alle aus derselben Schachtel und gleich groß.",
             "Kapazität einer Messbahn: 8 Gruppen × 6 Würfe × ca. 30 s ≈ 24 min (Planannahme, nicht gemessen). Wird es langsamer: weniger Gruppen bilden oder die Gegenprobe in Stunde 4 verschieben – nicht Wiederholungen streichen.",
             "Wartende Gruppen: Prüfer beobachtet die werfende Gruppe (Linie, Bahn frei), der Rest füllt die Spalte »Auffälliges« der eigenen Reihe nach oder ist beim nächsten Wurf bereit.",
             "Daten sichern: Protokoll-Handy speichert im Browser; zusätzlich Papierblatt (VS-AB) je Gruppe, das du am Ende einsammelst. 1AK: Daten vom 05.11. bis 12.11. aufbewahren, 1BK: vom 09.11. bis 11.11.",
             "1BK baut am 04.11. und fliegt am 09.11.: Flieger flach in einer Schachtel lagern, Gruppennummer auf dem Flügel. Vor dem Test kurz auf Knicke prüfen – verbogene Flieger im Probewurf korrigieren, danach nicht mehr."],
  "fehler": ["Nur die guten Würfe eingetragen oder kurze Würfe als »Fehlwurf« gestrichen.", "Gemessen bis zum Stillstand statt bis zum ersten Bodenkontakt.",
             "Zwischen den Würfen am Flieger nachgebogen oder die Klammer verschoben.", "Werfer gewechselt, ohne es zu notieren; Werte zweier Werfer zusammen gemittelt.",
             "Deckenkontakte gelöscht oder durch 0 ersetzt."],
  "fach": ["Die Klammer ändert Masse und Schwerpunktlage gleichzeitig. Der Test zeigt die Wirkung dieser einen Änderung – er trennt die beiden Ursachen nicht.",
           "Mehrere Würfe desselben Fliegers sind keine unabhängige Stichprobe verschiedener Flieger. Drei Paare sind ein Unterrichtskompromiss, kein Wirksamkeitsnachweis; keine Standardabweichung oder Signifikanz verlangen.",
           "Nach dem Loslassen wirkt keine Wurfkraft mehr: Im Gleitflug wirken Gewichtskraft und die Luftkraft (aufgeteilt in Auftrieb und Widerstand). Gruber S. 20 zeichnet einen fortwirkenden »Schub« – für den antriebslosen Flug nicht übernehmen."],
  "vorversuch": "Hallenprobe im Eingangsbereich: Faltung (ca. 10 min für Ungeübte?), Klammersitz, flacher Abwurf ohne Deckenkontakt mit und ohne Klammer, nutzbare Länge, freier Bereich ohne Durchgangsverkehr."},
]
assert [v["nr"] for v in VS] == [I.VS_ID]

SICHERHEIT = [("Bahn frei", "nur werfen, wenn niemand in der Flugbahn steht oder geht – nie in Richtung von Personen"),
              ("Flach werfen", "ruhig aus Hüfthöhe, kein Kraftwurf, kein hoher Bogen – die Decke ist niedrig"),
              ("Nicht rennen", "erst nach der Landung zum Flieger gehen, messen, zurückholen"),
              ("Stolperfallen", "Bandmaß am Rand, Taschen weg vom Boden, Eingang und Fluchtweg bleiben frei"),
              ("Büroklammer", "nicht aufbiegen, nicht mit der Spitze voran werfen")]
