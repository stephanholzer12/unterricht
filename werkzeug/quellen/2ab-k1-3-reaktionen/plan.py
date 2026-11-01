"""Zeitplan K1.3 Stoffumwandlung (2A und 2B gleiche Termine) – EINE Quelle für die Regiefolien der TH-Unterricht (und zum Abgleich mit Fahrplan und Stundenvorschlag).
Annahme: 50 min je Stunde. Stunde 2 beginnt mit dem Test K1.2 (20 min inkl. Austeilen/Einsammeln). Die Zeiten für Aufgaben, Demos, Stationen und Reserve
entsprechen der Spalte »Zeit« im Stundenvorschlag (fachwissen.py) und den Fahrplan-Zeilen; keine Hausübungen.
Phasen: (Name, Minuten, ohne Handy?, Art). Art: "org" · "einst" · "lesen" · "erkl" · "a<n>" Aufgabe · "v:<ID>" Versuch · "test" · "bespr" · "pdf" · "reserve" · "stat" Stationen."""
import inhalt as I

PLAN = [
 {"std": 1, "datum": "Di 03.11.", "titel": "Redox: Lavoisier und der Elektronenübergang", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Einstieg: Handwärmer und Mythos »Verbrennen macht leichter« – Handzeichen", 4, True, "einst"),
   ("Lesen: Buch S. 30–31 + Theorieteil Teil 1 (Lavoisier, Redoxreaktion, Elektronen, Mittel)", 6, False, "lesen"),
   ("Demo K1.3-V1: Eisenwolle auf der Waage (Tipp VOR der Demo; V2 wird parallel angesetzt)", 12, True, "v:K1.3-V1"),
   ("Kurz klären: Oxidation = Elektronenabgabe, Mittel macht es beim anderen", 5, True, "erkl"),
   ("Aufgaben 1–3 (Besprechung gleich danach)", 13, False, "a1"),
   ("Reserve", 8, True, "reserve")]},
 {"std": 2, "datum": "Do 05.11.", "titel": "Redox im Alltag: Rost und Rostschutz", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Test K1.2 inkl. Austeilen und Einsammeln", 20, True, "test"),
   ("Lesen: Theorieteil Teil 2 (Rost, Rostschutz, Eisen in Kupfersulfat) · Buch S. 30, 98", 3, False, "lesen"),
   ("Demo K1.3-V3: Kupferbrief, dabei kurz klären (Rost = Redox, Salz beschleunigt)", 8, True, "v:K1.3-V3"),
   ("Aufgaben 5–7 (Besprechung gleich danach)", 10, False, "a5"),
   ("Reserve", 7, True, "reserve")]},
 {"std": 3, "datum": "Di 10.11.", "titel": "Energie: exotherm und endotherm, Stationen", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Auswertung K1.3-V2 (Rost-Ansätze nach einer Woche)", 3, True, "v:K1.3-V2"),
   ("Demo K1.3-V6: Kältemischung, dabei exotherm/endotherm klären", 8, True, "v:K1.3-V6"),
   ("Stationen erklären: Sicherheit, Rotation, Protokoll am Handy", 2, True, "erkl"),
   ("Stationen K1.3-V4 + V5 in 3 Runden à 11 min (Gruppen 1–3: je 2 Stationsrunden + 1 freie Runde mit Teil 3 lesen und Aufgabe 9); Gruppen 4–6: Teil 3 lesen, Aufgaben 9–11, Fragen zur Deutung V4/V5 vorab lesen", 33, False, "stat"),
   ("Reserve", 2, True, "reserve")]},
 {"std": 4, "datum": "Do 12.11.", "titel": "Katalysatoren, Enzyme und Abschluss", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Demo K1.3-V7: Wasserstoffperoxid 3 % mit und ohne Braunstein, Aufgabe 13 – dabei Katalysator klären", 8, True, "v:K1.3-V7"),
   ("Stationen K1.3-V4 + V5 in 3 Runden à 11 min (Gruppen 4–6: je 2 Stationsrunden + 1 freie Runde mit Teil 4 lesen und Aufgabe 14); Gruppen 1–3: Aufgaben 10–11, Teil 4 lesen, Aufgabe 14, Deutung und Schluss V4/V5", 33, False, "stat"),
   ("Auswertung V4/V5 (Gruppen 4–6: Deutung und Schluss ins Protokoll, 3 min; Gruppen 1–3: Protokoll prüfen), danach Besprechen: Katalysator, Aufgabe 13 und 14 (2 min)", 5, True, "bespr"),
   ("PDF abgeben, Quiz-Hinweis, Ausblick Säuren und Basen", 1, False, "pdf"),
   ("Reserve (nur 1 min – Lesen und Versuche dauern oft länger)", 1, True, "reserve")]},
]
for st in PLAN: assert sum(p[1] for p in st["phasen"]) == 50, (st["std"], sum(p[1] for p in st["phasen"]))

KNAPP = {2: "Der Test hat Vorrang. Wird es knapp: Aufgabe 7 und die Besprechung kürzen, Aufgabe 8 (Zusatz) entfällt.",
         3: "Stationen nie kürzen, sondern bei Bedarf eine Runde auf 9 min: Demo V6 auf 5 min kürzen. Aufgaben 9–11 nicht streichen, sie laufen bei den wartenden Gruppen mit.",
         4: "Die Reserve ist nur 1 min: Bei Bedarf Runde 3 auf 9 min kürzen, Demo V7 auf 6 min, Aufgabe 14 mündlich; die Deutung V4/V5 der Gruppen 4–6 (Auswertung) wird nicht gestrichen. Tempo (Teil 5) ist Zusatz/Selbststudium und fällt nie in die Stunde. Das PDF darf auch nach dem Läuten abgegeben werden."}


# Vorschlag V11-02 (Entscheidung bei Stephan): Arbeitszeit je Gruppenhälfte, Minuten. Pflichtarbeit wird nicht in Hausübung oder Reserve geschoben.
# Rotation je Stunde: 3 Runden à 11 min, jede Gruppe der Stationshälfte hat 2 Stationsrunden + 1 freie Runde (Aufgabenzeit).
GRUPPENHAELFTEN = {
 "Gruppen 1–3": [
   ("Std 3 · Stationsrunden V4/V5 (Erkenntnis gleich an der Station)", 22),
   ("Std 3 · freie Runde: Teil 3 lesen 6 + Aufgabe 9 (5)", 11),
   ("Std 4 · Aufgaben 10–11 (5 + 6)", 11),
   ("Std 4 · Teil 4 lesen 5, Aufgabe 14 (3)", 8),
   ("Std 4 · Deutung und Schluss V4/V5 (beide Versuche)", 8),
   ("Std 4 · Puffer", 6)],
 "Gruppen 4–6": [
   ("Std 3 · Teil 3 lesen 6, Aufgaben 9–11 (5 + 5 + 6), Fragen zur Deutung vorab lesen 2", 24),
   ("Std 3 · Puffer", 9),
   ("Std 4 · Stationsrunden V4/V5 (Erkenntnis gleich an der Station)", 22),
   ("Std 4 · freie Runde: Teil 4 lesen 5, Aufgabe 14 (3), Puffer 3", 11),
   ("Std 4 · Auswertung: Deutung und Schluss V4/V5 (letzte Minuten)", 3)]}
assert sum(m for _, m in GRUPPENHAELFTEN["Gruppen 1–3"] if _.startswith("Std 3")) == 33
assert sum(m for _, m in GRUPPENHAELFTEN["Gruppen 1–3"] if _.startswith("Std 4")) == 33
assert sum(m for _, m in GRUPPENHAELFTEN["Gruppen 4–6"] if _.startswith("Std 3")) == 33
assert sum(m for _, m in GRUPPENHAELFTEN["Gruppen 4–6"] if _.startswith("Std 4")) == 36   # 33 + 3 min Auswertung
