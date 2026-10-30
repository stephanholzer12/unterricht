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
   ("Stationen K1.3-V4 + V5 in 3 Runden à 11 min (Gruppen 1–3); Gruppen 4–6: Theorieteil Teil 3 lesen, Aufgaben 9–11", 33, False, "stat"),
   ("Reserve", 2, True, "reserve")]},
 {"std": 4, "datum": "Do 12.11.", "titel": "Katalysatoren und Enzyme", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Demo K1.3-V7: Wasserstoffperoxid + Braunstein/Kartoffel, Aufgabe 13 – dabei Katalysator klären", 10, True, "v:K1.3-V7"),
   ("Stationen K1.3-V4 + V5 in 3 Runden à 11 min (Gruppen 4–6); Gruppen 1–3: Aufgaben 9–11, 14, Deutung V4/V5; Theorieteil Teil 4", 33, False, "stat"),
   ("Reserve und kurze Sicherung (Autokatalysator, Aufgabe 14)", 5, True, "reserve")]},
 {"std": 5, "datum": "Di 17.11.", "titel": "Reaktionsgeschwindigkeit und Abschluss", "phasen": [
   ("Beginn: Klassenbuch, Anwesenheit", 2, True, "org"),
   ("Partnercheck (Aufgabe 18): mündlich zu zweit, Handy von B bleibt weg", 6, True, "a18"),
   ("Lesen: Theorieteil Teil 5 · Buch S. 36", 3, False, "lesen"),
   ("Kurz klären: vier Stellschrauben, Faustregel, Staubexplosion", 5, True, "erkl"),
   ("Aufgabe 16", 4, False, "a16"),
   ("Gruppenversuch K1.3-V8: Brausetablette im Test (Handy = Stoppuhr)", 18, True, "v:K1.3-V8"),
   ("Aufgabe 17 und Protokoll fertig", 5, False, "a17"),
   ("PDF abgeben, Quiz-Hinweis", 2, False, "pdf"),
   ("Reserve", 5, True, "reserve")]},
]
for st in PLAN: assert sum(p[1] for p in st["phasen"]) == 50, (st["std"], sum(p[1] for p in st["phasen"]))

KNAPP = {2: "Der Test hat Vorrang. Wird es knapp: Aufgabe 7 und die Besprechung kürzen, Aufgabe 8 (Zusatz) entfällt.",
         3: "Stationen nie kürzen, sondern bei Bedarf eine Runde auf 9 min: Demo V6 auf 5 min kürzen. Aufgaben 9–11 nicht streichen, sie laufen bei den wartenden Gruppen mit.",
         4: "Reserve ist knapp: Demo V7 auf 8 min, Aufgabe 14 mündlich.",
         5: "Wird es knapp: Partnercheck auf 4 min, PDF darf auch nach dem Läuten abgegeben werden."}
