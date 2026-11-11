"""Lehrer-Hintergrund K2.1 Mechanische Kräfte: Lehrplanbezug, fachliche Korrekturen zu den Quellen,
Fehlvorstellungen, Fragen der Kadetten, Checkliste vor der Stunde, Rechenkontrolle.
Wird von der privaten Lösungsmappe gelesen (und später vom TH-Fachwissen-Word). Keine Kadetten-Inhalte.
Quelle der Inhalte: inhaltliche Ausarbeitung vom 07.11.2026 (Abschnitte 9, 10, 15) plus eigene Prüfung."""

LEHRPLAN = [
    ("K03 (verbindlich)", "die Grundgrößen und die entsprechenden Einheiten des Internationalen Einheitensystems benennen – abgedeckt in Aufgabe 2 c–e, Aufgabe 8 a/e/i/j, Theorie-Karte »Alle Größen und Einheiten« und Quiz 2/4/5/11."),
    ("K02 (zusätzlich sichtbar)", "einfache naturwissenschaftliche Untersuchungen planen, durchführen, dokumentieren und präsentieren – das Gruppenprojekt V1.20 über die Stunden 2 bis 5. Der Jahresplan wird dadurch nicht geändert."),
    ("N01", "beobachten, beschreiben, berechnen, darstellen und erläutern – Versuchsseite: Beobachtung, Erkenntnis, Interpretation, Schlussfolgerung."),
    ("N02", "Bedeutung für Wirtschaft, Technik und Umwelt erfassen – Alltagsbeispiel je Gruppe, Zusatzaufgabe 11 zur TU-Wien-Meldung."),
    ("P8", "Gesundheit und Sicherheit – Sicherheitsregeln der Messstunde, Druck unter Schuhsohle und Schultergurt."),
    ("P7", "Quellen und Medien – Quellenprüfung in Stunde 2, Zusatzaufgabe 11."),
    ("GLV 6", "verantwortungsvoller Umgang mit wissenschaftlichen Modellen und Technik – jede Gruppe nennt eine Grenze ihrer Untersuchung. Waffenversuche sind dafür nicht nötig."),
    ("Jahresplan", "Block »E Physik«, E15–E17 sind 7 Stunden laut bloecke.json. Geplant sind hier SECHS Stunden einschließlich Präsentationen; die Lehrer-Seite meldet deshalb eine Abweichung von einer Stunde."),
]

# Was in den Quellen verkürzt dargestellt ist und welche Fassung hier verwendet wird.
KORREKTUREN = [
    ["Trauner S. 45; Kohl-PDF S. 31", "Ruhe als einziges Kennzeichen des Gleichgewichts",
     "Gleichgewicht heißt: resultierende Kraft null. Auch eine geradlinige gleichförmige Bewegung ist Gleichgewicht."],
    ["Trauner S. 49; Hölzel S. 104–105", "F = m · a ohne Angabe, welche Kraft gemeint ist",
     "Für die Beschleunigung zählt F_res, die Summe aller äußeren Kräfte auf den Körper."],
    ["Trauner S. 52; Kohl-PDF S. 222", "»Beim Schwimmen ist der Auftrieb größer als die Gewichtskraft«",
     "Steigen aus der Ruhe und ruhiges Schwimmen trennen. Beim ruhigen Schwimmen gilt F_A = F_G."],
    ["Trauner S. 54; grünes Buch S. 50–51", "»Reibung wirkt immer gegen die Bewegung relativ zum Boden«",
     "Sie wirkt gegen das relative Gleiten an der Kontaktstelle oder gegen dessen Tendenz. Haftreibung kann antreiben."],
    ["Trauner S. 55; Kohl-PDF S. 203", "»Haftreibung ist immer größer als Gleitreibung«",
     "Verglichen wird die maximale Haftreibung derselben Materialpaarung. Die aktuelle Haftreibung passt sich bis dorthin an."],
    ["Trauner S. 57; VERITAS S. 37", "Kapillarität als vollständige Erklärung für den Wassertransport hoher Pflanzen",
     "Transpirationssog und Kohäsion gehören dazu. Aus der Streifenbreite folgt kein Porenradius."],
    ["Trauner S. 61", "Spülmittelfisch als Rückstoß",
     "Der Antrieb kommt aus einem Gefälle der Oberflächenspannung (Marangoni). Deshalb hier nicht als Nachweis des Raketenprinzips."],
    ["Trauner S. 53", "»Im Toten Meer kann man nicht untergehen«",
     "Die hohe Dichte erleichtert das Schwimmen; eine Sicherheitsgarantie folgt daraus nicht. Aussage nicht übernommen."],
    ["Trauner S. 59; Versuchspool V1.91", "»Das tiefste Loch liefert immer den weitesten Strahl«",
     "Ausflussgeschwindigkeit und Fallhöhe wirken zusammen; im idealen Modell gilt R = 2·√(h·(H−h)). Reichweite ist kein Druckmaß."],
    ["Grünes Buch S. 48", "Münzen verschiedener Masse auf einer Karte als Trägheitsvergleich",
     "Mit der Masse ändert sich gleichzeitig die Reibung. Der Trick zeigt Trägheit, isoliert aber keine Massenabhängigkeit."],
    ["Hölzel S. 112 (Ballonaufgaben)", "Nur die Gasmasse als Masse des Ballons",
     "Hülle, Korb und Last gehören zur gesamten Gewichtskraft."],
    ["VERITAS Trommelfellaufgabe", "Hydrostatischer Überdruck direkt als Kraft auf das Trommelfell",
     "Entscheidend ist die Druckdifferenz zwischen beiden Seiten. Deshalb keine Kernrechnung daraus."],
]

FEHLVORSTELLUNGEN = [
    ["»Wo Bewegung ist, wirkt eine Kraft.«", "Für gleichförmige geradlinige Bewegung braucht es keine resultierende Kraft.",
     "Buch flach über den Tisch schieben: Zugkraft und Reibung gleichen sich aus, das Tempo bleibt."],
    ["»Geschwindigkeit, Beschleunigung und Druck sind Kraftarten.«", "Nur Gewichtskraft, Auftrieb, Reibung und Kapillarkraft sind Kräfte. Druck verbindet Kraft und Fläche.",
     "Einheitentabelle an der Tafel: N gegen m/s, m/s² und Pa."],
    ["»Beim Schwimmen ist der Auftrieb größer.«", "Beim ruhigen Schwimmen sind Auftriebs- und Gewichtskraft gleich groß.",
     "Zwei gleich lange Pfeile an einem schwimmenden Körper zeichnen lassen."],
    ["»Haftreibung ist immer größer.«", "Verglichen wird die maximale Haftreibung derselben Paarung.",
     "Beim Versuch von Gruppe 4 langsam anziehen und den Zeiger beobachten: Er steigt, bevor etwas rutscht."],
    ["»Zwei Kraftmesser zeigen zusammen 4 N.«", "Beide messen dieselbe übertragene Zugkraft an verschiedenen Stellen.",
     "Gruppe 7 vorführen lassen und beide Anzeigen gleichzeitig vorlesen."],
    ["»Der eingetauchte Stab wird schwerer.«", "Die Masse des gehaltenen Stabs bleibt gleich; die Waage misst die Gegenkraft auf Wasser und Gefäß.",
     "Beide Körper getrennt einrahmen und die Kraftpfeile einzeichnen."],
    ["»Im Weltraum gibt es nichts zum Abdrücken, also kann eine Rakete nicht fliegen.«", "Rückstoß braucht keine Luft: Die Rakete stößt Masse aus und wird in die Gegenrichtung beschleunigt.",
     "Mit dem Wechselwirkungsbild Rakete ↔ ausgestoßenes Gas erklären."],
]

FRAGEN = [
    ("Muss auf einen bewegten Körper eine Kraft wirken?",
     "Nein. Für ein unverändertes Tempo auf gerader Bahn braucht es keine resultierende Kraft; es können sich mehrere Kräfte ausgleichen."),
    ("Warum addiert man die beiden Kraftmesseranzeigen nicht?",
     "Sie messen die übertragene Spannungskraft an zwei Stellen derselben ruhenden Messkette. Die Anzeige zählt nicht, wie viele Personen ziehen."),
    ("Wird der Glasstab unter Wasser schwerer?",
     "Nein. Die von außen gehaltene Masse bleibt gleich. Die Waage zeigt die zusätzliche, nach unten übertragene Kraft des Stabs auf Wasser und Gefäß."),
    ("Warum reicht Kapillarität nicht für einen hohen Baum?",
     "Die Verdunstung an den Blättern erzeugt Zugspannung, die Kohäsion überträgt sie im Xylem. Die Steighöhe einer einzelnen Kapillare erklärt das nicht."),
    ("Was zeigt der Spritzenversuch nicht?",
     "Er misst weder Druck noch Kraft. Er zeigt qualitativ, dass sich Gas zusammendrücken lässt und dabei stärker zurückdrückt – kein Zahlenbeweis für p = F / A."),
    ("Fallen alle Körper gleich schnell?",
     "Bei gleichem Anfangszustand und vernachlässigbarem Luftwiderstand haben sie am selben Ort dieselbe Fallbeschleunigung. Die Luft verändert reale Ergebnisse."),
    ("Warum rechnen wir mit 10 N/kg und nicht mit 9,81?",
     "Damit die Kadetten im Kopf rechnen können. 9,81 N/kg ist genauer; die Näherung wird genannt und innerhalb einer Aufgabe nicht gewechselt."),
    ("Ist Druck eine Kraft?",
     "Nein. Druck sagt, wie sich eine senkrechte Kraft auf eine Fläche verteilt: p = F_N / A, Einheit Pascal (1 Pa = 1 N/m²)."),
    ("Warum heben sich Kraft und Gegenkraft nicht auf?",
     "Weil sie auf verschiedene Körper wirken. Beim Kräftegleichgewicht wirken die Kräfte dagegen auf denselben Körper."),
    ("Ist eine Kurve bei gleichem Tempo eine Beschleunigung?",
     "Ja. Zur Geschwindigkeit gehört die Richtung; ändert sie sich, ist das eine Beschleunigung – auch ohne Tempoänderung."),
]

RECHENKONTROLLE = [
    "Aufgabe 2 c) v = 5 m : 4 s = 1,25 m/s · d) 1,25 · 3,6 = 4,5 km/h · e) F = 2 kg · 3 m/s² = 6 N.",
    "Aufgabe 8 a) F_G = 6 kg · 10 N/kg = 60 N · e) p = 120 N : 0,02 m² = 6000 Pa · i) v = 9 m : 6 s = 1,5 m/s · j) a = 12 N : 3 kg = 4 m/s².",
    "Zusatzaufgabe 10: p₁ = 600 N : 0,03 m² = 20 000 Pa · p₂ = 600 N : 0,30 m² = 2 000 Pa – zehnmal kleiner.",
    "Gruppe 3, Modellwerte für den 8-mm-Stab: 2 / 4 / 6 cm Eintauchtiefe ergeben rechnerisch etwa 1,0 / 2,0 / 3,0 g zusätzlich. Das sind Rechenwerte, keine Messdaten.",
    "Kraftmesser 10 N mit 0,2-N-Teilung: Die kleinste ablesbare Stufe entspricht rund 20 g Masse. Feinere Werte sind nicht ablesbar.",
    "Gruppe 7: Bei 2 N angestrebter Zugkraft zeigen beide Geräte ungefähr 2 N – nicht 4 N.",
]

CHECKLISTE = [
    "Zwei analoge Kraftmesser (#51, #52): Nullpunkt, Skala und Messbereich geprüft.",
    "Drei Waagen aus dem 5er-Pack #128 eingeschaltet und auf Funktion geprüft; Höchstlast 620 g im Kopf.",
    "PP-Messbecher 250 ml (#87) und 500 ml (#88) unterschieden und den Zug am Henkel einmal selbst ausprobiert.",
    "Ein intaktes 400-ml-Becherglas (#15) und ein intakter Glasstab (#120) liegen bereit.",
    "Eine saubere 50-ml-Spritze ohne Nadel (#77) und zwei gleich breite Filterpapierstreifen (#54) liegen bereit.",
    "Bandmaße (#9, #10) da und der 5-m-Gehweg für Gruppe 1 ist frei – kein Durchgangsverkehr.",
    "Wasser, zwei Auffangwannen (#6) und etwas zum Aufwischen sind bereit.",
    "**Vorversuch Pflicht:** Auftrieb (Gruppe 3) mit der tatsächlich verwendeten Waage vorgeführt – ist das Signal bei 2 cm stabil sichtbar?",
    "Reibungsaufbau (Gruppe 4) einmal selbst gezogen: Hebt der Becher vorne ab? Sind die Werte lesbar?",
    "Die Gruppen haben Zugriff auf das Trauner-Buch; die zweite Quelle für Gruppe 3 und 5 ist vorbereitet (privat, keine Buchscans online).",
    "Einheit einblenden, wenn es losgeht: GitHub → Actions → »Einheit ein-/ausblenden« → 1ab-nawi/k2-1-kraefte.",
]

OFFEN = [
    "**Geräte sind nur im Inventar belegt, nicht heute gezählt.** Vor Stunde 3 wirklich nachsehen – besonders Kraftmesser, Waagen, Wannen und Filterpapier.",
    "**Der Kraftmesserwechsel nach 14 Minuten ist verbindlich** (Gruppen 2 und 4 → Gruppe 7). Es gibt nur zwei analoge Geräte; der digitale #26 wird nicht gebraucht.",
    "**Gruppenstärke:** 1AK sieben Vierergruppen, 1BK sechs Vierergruppen und eine Fünfergruppe. Keine namentliche Einteilung vorgegeben.",
    "**Keine festen Termine:** Im Fahrplan steht »geplant«. Es zählt die Reihenfolge der Stunden, nicht das Datum.",
    "**Fällt eine Stunde aus**, entfällt zuerst Stunde 4. Das Meilenstein-PDF aus Stunde 3 taugt als Präsentationsunterlage.",
    "**Supplierstunde möglich: Stunde 6** – Aufgabe 8, Theorie-Karten und Selbsteinschätzung brauchen kein Material und keinen Versuch.",
    "**Noch nicht geliefert:** TH-Lehrer- und TH-Kadetten-PPP, Word (AB/Lösung/Fachwissen), Kahoot-Tabelle und ZIP. Das war als Teillieferung so bestellt.",
]

AUSBLICK = ("Als Nächstes kommt »Arbeit und Energie« (Trauner S. 66–77). Die Begriffe Kraft, Weg und Gewichtskraft aus dieser Einheit "
            "werden dort zu W = F · s und zu den Energieformen weitergeführt. Die elektrischen Kräfte (ab S. 78) folgen danach als eigene Einheit; "
            "für beide liegen die vollständigen Buchseiten noch nicht vor.")
