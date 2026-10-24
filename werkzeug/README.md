# Werkzeug für die Handy-Seiten

Bauvorlagen für Theorie-Seite (Theorie), Arbeitsblatt (Aufgaben) und Quiz – Stil wie der BHAK-Folienmaster.

## Ordner und Links
- Pro Einheit ein Ordner: `<klasse>-<fach>/k<kapitel>-<thema>/` (z. B. `2ab-nawi/k1-2-bindungen/`, `3bk-pbgw/k2-1-wahlen/`)
- Darin: `theorie.html`, `aufgaben.html`, `quiz.html`, Bilder in `img/`
- Link: `https://stephanholzer12.github.io/unterricht/<ordner>/<seite>.html`
- Neue Einheit in `einheiten.json` eintragen (mit `block` und `jahresplan`, siehe unten), dann `python3 werkzeug/build_index.py` → Klassenseiten; die Startseite listet bewusst keine Klassen

## Klassenseiten (Stoff-Übersicht pro Klasse)
`build_index.py` baut pro Klasse drei Seiten mit festen Namen:
- `<klasse>-<fach>/index.html` – »Gerade dran«, Tests mit Countdown, Fortschritt »Themenblock x von y«, alle bisherigen Einheiten nach den Themenblöcken des Jahresplans; pro Einheit Knöpfe (Theorie-Seite · Arbeitsblatt · Versuche · Quiz …), »Was drankommt« (Teile der Theorie-Seite mit Buchseiten) und »Das Wichtigste in 5 Sätzen«
- `<klasse>-<fach>/begriffe.html` – Fachbegriffe A–Z aus allen bisherigen Theorie-Seiten, mit Suche
- `<klasse>-<fach>/wiederholen.html` – alle Lernziele zum Abhaken (sicher / fast / noch nicht); teilt den Speicher mit »Kann ich das?« der Theorie-Seite

Zusätzlich die **Lehrer-Seite** `lehrer-0f6eec.html` (Adresse in `build_index.py`, Konstante `LEHRER`): vier große Fachkarten, Suche nach Klasse/Thema/Dateiname und kompakter Schnellzugriff auf das aktuelle Material jeder Fach-/Klassengruppe. Fachauswahl und Suche filtern auch die aufklappbaren Materialbereiche; vorhandene direkte Klassenanker bleiben nutzbar. Alle bisherigen Einheiten (auch versteckte), Tests, Dateivermerke und QR-Codes sind weiterhin erreichbar. `lehrer_layout.py` enthält diese Lehreransicht (v1); sie liest oder verändert keine gespeicherten Kadetten-Antworten.

Die Lehrerzentrale wird auf keiner Kadetten-Seite verlinkt. Die Startseite enthält weiterhin keine Fach-/Klassenliste, die Kadetten öffnen den direkten Klassenlink aus LMS bzw. dem QR-Code. Das trennt die Navigation, ist aber **keine Zugriffssperre**: Alle veröffentlichten GitHub-Pages-Adressen bleiben öffentlich erreichbar. Keine vertraulichen Daten auf die Lehrer-Seite stellen.

Es erscheint nur, was in `einheiten.json` steht – kommende Themen bleiben unsichtbar. Felder pro Einheit:
- `block`: Block laut Jahresplan, genau wie in `bloecke.json` (z. B. `"A Atombau & Bindung"`); `jahresplan`: Einheit(en) im Jahresplan (z. B. `"E3–E5"`, nur zur Nachverfolgung)
- optional `"dateien"`: die aktuell gültigen PPP-/Word-Dateien der Einheit, z. B. `{"stand": "18.10.2026", "zip": "26-27-4AB-K1.5a-E-Magnet-v3.zip", "liste": ["26-27-4AB-K1.5a-E-Magnet-TH-Lehrer-v2.pptx", …]}` – bei jeder Lieferung aktualisieren; erscheint nur auf der Lehrer-Seite (»Aktuelle Dateien«)
- optional `"aktuell": true` (sonst ist die zuletzt eingetragene Einheit »Gerade dran«), `"versteckt": true` (schon online, aber noch nicht in der Übersicht)
- Test-Trainings ohne `block`, `kapitel` = »<Nr>. Test · <Datum>« → eigener Kasten mit Countdown
- `bloecke.json` (Reihenfolge der Blöcke) kommt aus dem Jahresplan: `python3 werkzeug/bloecke_aus_jahresplan.py <Jahresplan.xlsx>` (Blatt »Stunden«, Spalte »Block«; Zuordnung Klassenseite → Jahresplan-Klasse oben im Skript)
- `lernseite_lesen.py` holt Buchseiten, Teile, Lernziele, »Das Wichtigste« und Fachbegriffe aus `theorie.html`. Damit alles erscheint, braucht die Theorie-Seite: Abschnitt `id="begriffe"` mit Tabelle (Begriff | Bedeutung), Folie »Das Wichtigste in 5 Sätzen«, Folie »Kann ich das?« mit `.ziel`-Kästchen und `var KEY = "…"`. Fehlt etwas, listet `build_index.py` die Lücken am Ende auf.
- QR-Code für die Klasse: `https://stephanholzer12.github.io/unterricht/<klasse>-<fach>/`

## Bausteine
- **Kadettenansicht v1:** `kadetten_layout.py` ergänzt auf der Klassenseite das aktuelle Thema, Materialzugänge, den Arbeitsauftrag je auswählbarer Phase aus `fahrplan.zeilen` und die Suche in den freigegebenen Themen. Andere Themen sind zunächst zugeklappt; direkte Themenanker öffnen ihren Block. `build_index.py` baut außerdem die Rückkehr zur eigenen Klasse und Materialwechsel in alle in `einheiten.json` eingetragenen Materialseiten ein. Gemeinsame Darstellung/Bedienung: `gemeinsam/kadetten-layout-v1.css` und `kadetten-navigation-v1.js`. Kein Lesen oder Schreiben von Kadetten-Antworten, keine Änderungen an Bewertungsregeln. Nach einem Neubau immer `build_index.py` ausführen (wie bisher über `nach_dem_bauen.py` und die Klassenseiten-Automatik). Die Lehrerzentrale und die neutrale öffentliche Startseite bleiben getrennt.
- `python3 werkzeug/test_kadetten_layout.py` kontrolliert zusätzlich Materialwege, Abgabeanker, doppelte IDs, vollständige Materiallinks und die Übernahme der vorhandenen Arbeitsaufträge; läuft auch in GitHub Actions.
- `archiv/extract.py` (Einmal-Skript, nur zur Ansicht, enthält feste Pfade des alten Chats) + `vorlagen/build_theorie.py`: Theorie aus der TH-Kadetten-PPP (Texte, Bilder, GIFs) → `theorie.html`
- `vorlagen/aufgaben_K1.2_vorlage.html`: Arbeitsblatt (Beispiel K1.2) mit Aufgabentypen text, table, sketch (Foto), strike (Durchstreichen), assign (Zuordnen), puzzle (Rätsel); Speichern im Browser (localStorage), PDF-Abgabe mit jsPDF 2.5.1 (eingebettet) und Schrift Carlito (Teilmenge in `schriften/`, Zeichenbereiche in `ranges.json`)
- `archiv/assemble.py` + `archiv/site.py` (Einmal-Skripte der ersten 2AB-Seiten, nur zur Ansicht – nicht mehr verwenden): setzen Wappen, Tarnmuster, Smiley, Schrift, QR-Code ein und schreiben die fertigen Seiten
- `vorlagen/pdf_auswertung.js`: neue PDF-Abgabe »Auswertung für die Lehrkraft« (ersetzt `buildPdf()` im Arbeitsblatt): Übersicht auf Seite 1 (bearbeitet / automatisch geprüft / Punkte, Summe, Note oder Bewertungsraster), danach jede Aufgabe als Block; Auswahl-, Zahlen- und Ampel-Antworten werden grün/rot markiert, bei Fehlern steht die richtige Lösung daneben, freie Texte »selbst bewerten«. Prüfregeln pro Aufgabe: `pts`, `key` (assign), `check`/`checks` (`all`, `ampel`, `trendAmpel`, `reason`), Präfix `pre`; global optional `RASTER`. Beispiel: `3ab-nawi/k2-3b-trendcheck/`
- `vorlagen/quiz_vorlage.html`: Quiz (Sofort-Feedback, Buchseite pro Frage, QR-Code für die Klasse)

- `quellen/<einheit>/`: Quellen und Bauskript einzelner Einheiten (z. B. `quellen/1ab-k1-2-2-koerper/bauen.py` für NAWI 1AB K1.2.2)

- `icons/`: Standard-Icons für Geräte und Chemikalien (aus den Bindungsarten-Versuchen) – in allen VS-Word-Dateien und Versuchsseiten verwenden, Liste in `icons/README.md`

- `pdf_hilfe.js` + `pdf_hilfe_einbauen.py`: Ersatzwege, wenn ein Handy die PDF nicht herunterlädt (App-Browser wie Instagram/Teams, manche iPhones): nach »PDF erstellen« erscheint ein Feld mit »Teilen / Speichern« und »PDF öffnen«, in App-Browsern zusätzlich der Hinweis »Im Browser öffnen«. Nach jeder neuen Seite mit PDF-Abgabe `python3 werkzeug/pdf_hilfe_einbauen.py` ausführen (setzt das Skript inline in alle Seiten mit jsPDF).
- **Nach dem Bauen einer Einheit immer: `python3 werkzeug/nach_dem_bauen.py`** – führt alle Einbau-Skripte unten, `build_index.py` und die Kontrolle der Reihe nach aus.
- `pdf_programm_auslagern.py`: PDF-Programm (jsPDF 2.5.1) und PDF-Schrift liegen einmal in `gemeinsam/pdf-programm-v1.js` statt in jeder Seite (Seite ca. 100 statt 600 KB; das Handy lädt die gemeinsame Datei nur einmal). Lädt sie beim Öffnen nicht, versucht die Seite es sofort ein zweites Mal. Bei einer geänderten gemeinsamen Datei den Namen hochzählen (`-v2`), nie die alte überschreiben.
- `pdf_erinnerung.js` + `pdf_erinnerung_einbauen.py`: über dem Knopf »PDF erstellen« steht »Du hast noch keine PDF erstellt« bzw. »Du hast seit deiner PDF von 10:42 etwas geändert – PDF neu erstellen« (gelb) oder »✓ Deine PDF passt zu deinen Antworten« (grün). Merkt sich dazu einen Fingerabdruck von Name, Klasse, Antworten und Fotos unter dem eigenen Schlüssel `pdfstand|<Seitenschlüssel>`; der Speicherstand der Seite wird nur gelesen. Nach jeder neuen Seite erneut ausführen (wiederholbar).
- `versuche_pruefen.js` + `versuche_pruefung.json` + `versuche_pruefen_einbauen.py`: Knopf **»Eingaben prüfen«** unter jedem Versuch der Gruppen-Versuchsseiten. Prüft, ob alles ausgefüllt ist (Zahlen bei Messwerten, Mindestlänge) und ob die Texte zu Beobachtung/Erkenntnis/Interpretation/Schlussfolgerung passen (Stichwortgruppen mit Tippfehler-Toleranz, ggf. Reihenfolge). Hilfe in Stufen bei jedem Klick mit Hinweis: 1 Hinweis → 2 Tipp (Schulbuchseite, Link zur Theorie-Seite) → 3 ein fehlender Begriff → ab 4 alle fehlenden Begriffe; die Lösung wird nie verraten, die Lehrkraft bewertet. Zähler liegen in `S.chk` (nicht in `S.a`, sonst zählte der Versuch als bearbeitet); in der PDF steht je Versuch eine Zeile »Selbstkontrolle: n Prüfungen · zuletzt … · höchste Hilfe-Stufe: x«. **Neue Versuchsseite: Regeln in `versuche_pruefung.json` ergänzen** (Einheit-Ordner → Versuch-ID → `beob`/`erk`/`interp`/`schluss`; Stämme ohne Umlaute: ae/oe/ue/ss), dann `nach_dem_bauen.py`. Ohne Regeln meldet das Skript einen Fehler.
- `abgabezeit_einbauen.py`: im PDF-Kopf und im Kopier-Text steht Datum **und Uhrzeit** der Erstellung (Uhr des Handys). Wichtig, wenn ein Kadett »LMS ging nicht« sagt und die PDF per E-Mail schickt. Wird von `nach_dem_bauen.py` mit ausgeführt (wiederholbar); die Quellvorlagen (`pdf_auswertung.js`, `vs_body.html`, `aufgaben_K1.2_vorlage.html`, `bauen.py`) sind schon angepasst.
- `schriften_einbauen.py`: Die Schriften (Source Sans 3, Source Serif 4, Lizenz OFL) liegen im Ordner `schriften/`; alle Seiten verlinken `../../schriften/schriften.css` statt Google Fonts (Datenschutz, kein Fremdserver, geht auch bei schwachem Netz). Neue Bauskripte/Vorlagen: diesen Link verwenden, nie wieder `fonts.googleapis.com`. Nach dem Bauen einer Einheit `python3 werkzeug/schriften_einbauen.py` ausführen (wiederholbar).
- `speicherstatus.js` + `speicherstatus_einbauen.py`: zeigt auf jeder Seite mit PDF-Abgabe 5 Sekunden lang »Gespeichert um 10:42 auf diesem Gerät« (danach blendet es sich aus, damit es keinen Text verdeckt) bzw. eine deutliche Warnung (mit Knopf »Zur PDF«), wenn das Handy das Speichern verweigert (Speicher voll, privater Modus). Der Baustein legt sich von außen um `localStorage.setItem` und ändert nie einen Schlüssel oder Wert; gespeichert wird weiterhin sofort bei jeder Eingabe. Das Skript ändert außerdem die Meldung nach dem normalen PDF-Download auf »PDF wurde erstellt … schau in deinen Downloads nach« (die Seite kann nicht wissen, ob die Datei ankam), setzt `aria-live` auf `#pdfstatus` und färbt »Gespeichert«/»Richtig« dunkler (#3F6B14, 5,3:1 und mehr statt 2,8:1). Nach jeder neuen Seite erneut ausführen: `python3 werkzeug/speicherstatus_einbauen.py` (wiederholbar, ändert nichts doppelt). **Speicherschlüssel (`const KEY = …`) nie umbenennen, solange eine Klasse an der Einheit arbeitet.**
- `teststoff/teststoff.js`: **Teststoff** (eine A4-Seite, Regelwerk 16) für alle Klassen – Daten in `teststoff/daten/<schuljahr>-<klasse>-test<nr>.json`, Anleitung in `teststoff/README.md`.
- `quellen/4ab-test1-training/bauen.py`: Test-Training (Quiz zum Teststoff, mehrere Kapitel) – Vorlage für weitere Test-Trainings: Ordner kopieren, Fragen tauschen, in `einheiten.json` mit `kapitel` = »1. Test · Datum« eintragen.

## Regeln
- Nur Unterrichtsmaterial: keine Noten, keine Schülernamen, keine Testlösungen, keine eingescannten Buchseiten
- Keine Buchinhalte (die Seiten sind öffentlich): Buch-Aufgaben, Lückensätze, Rätsel-Hinweise und Thesen immer in eigenen Worten, Buchabbildungen nur als Verweis (»Karte im Buch S. 19«), alle Grafiken selbst gezeichnet; Seitenzahlen und Kapitelangaben sind erlaubt
- Antworten der Kadetten bleiben im Browser; Abgabe als PDF in LMS

## Lösungshilfe (Handy-Arbeitsblätter)
`python3 werkzeug/loesungshilfe_einbauen.py` baut `loesungshilfe.js` in jede `*/*/aufgaben.html` mit »Prüfen« ein (idempotent; nach jedem neuen Arbeitsblatt ausführen).
- Fehlversuch 1: nur Hinweis. Ab Fehlversuch 2: Tipp mit Link. Ab Fehlversuch 3: Knopf »Lösung zeigen« bei dieser Aufgabe.
- PDF zeigt je Aufgabe: selbst gelöst (1. Versuch) / gelöst nach n Fehlversuchen (mit Tipp) / Lösung angesehen (selbst bewerten).
- Rechenaufgaben: Übungsvariante mit Zufallszahlen, definiert in `loesungshilfe_varianten.json` (zählt nicht für die Abgabe).

## Automatische Kontrolle
`python3 werkzeug/pruefen.py` (läuft auch bei jedem Push als »Seiten pruefen« unter GitHub → Actions): meldet Fremdserver-Links, Tokens, Skript-Syntaxfehler, PDF-Seiten ohne Speicherstatus und **verschwundene/umbenannte Speicherschlüssel** (außer `[schluessel-ok]` steht in der Commit-Nachricht). Pakete für die Automatik sind in `werkzeug/requirements.txt` festgelegt.

`python3 werkzeug/test_lehrer_navigation.py` prüft zusätzlich die Trennung der Kadetten-Navigation, alle Lehrerlinks, Klassenanker und QR-Ziele. Der Test läuft ebenfalls in der GitHub-Kontrolle und braucht keine Zusatzpakete.


## Großzügige Prüfung der Arbeitsblätter (pruefung_nachsicht)
Der Knopf »Prüfen« in `aufgaben.html` (Standard-Prüfung mit `checkField`) bewertet richtige Antworten großzügig:
- **Zahlen:** irgendeine Zahl der Antwort darf stimmen; Tausenderpunkt/-leerzeichen, Komma oder Punkt, `m2`/`m^2`/`m²`, `4*10^-4`; gleichwertige Einheiten (kA/m = 1000 A/m, mT, cm², Vs/m² = T); fehlende Einheit = richtig mit Hinweis; Rundung auf die angeschriebene Stelle (83 statt 82,8); sonst 2 % Spielraum. Falsche Einheit (z. B. V statt A) bleibt falsch.
- **Texte:** ä/ae, ö/oe, ü/ue, ß/ss, Bindestriche, Tippfehler bei einfachen Stichwörtern (ab 6 Buchstaben).
- **Regeln je Einheit korrigieren:** `werkzeug/pruefregeln_korrekturen.json` (Ordner → Aufgabe → Feld). `need` = wie viele Stichwortgruppen genügen, `kw` = neue Stichwörter, 3. Eintrag einer Gruppe = wie viele verschiedene Treffer nötig (»Nenne zwei Gründe« = 2).
- Einbau: `python3 werkzeug/pruefung_nachsicht_einbauen.py` (steht in `nach_dem_bauen.py`; `pruefen.py` verlangt den Block). Neue Aufgaben: Regeln großzügig schreiben (viele Wortstämme, nur so viele Gruppen verlangen wie die Aufgabe fordert).


## Punkte und Notenvorschlag im PDF (notenvorschlag)
Oben auf Seite 1 jeder Abgabe-PDF mit automatischer Prüfung steht ein gelber Kasten: »Für LMS: 31 von 38 Punkten (82 %) · Notenvorschlag 2 – vorläufig«. Am Bildschirm der Schüler erscheint nichts.
- Punkte: 1 je richtige Auswahl-/Zahlen-Antwort, Stichwort-Antworten anteilig, Aufgaben mit angesehener Lösung = 0 (stehen im Kasten), Aufgaben ohne automatische Prüfung (Freitext/Skizze) stehen als »selbst bewerten«; Zusatzaufgaben zählen nur, wenn bearbeitet.
- Schlüssel: ab 88 % = 1, 75 % = 2, 62 % = 3, 50 % = 4, sonst 5 (`SCHLUESSEL` in `werkzeug/notenvorschlag.js`).
- Einbau: `python3 werkzeug/notenvorschlag_einbauen.py` (steht in `nach_dem_bauen.py`; `pruefen.py` verlangt den Block). Versuchs- und Projektseiten haben keinen Kasten (Lehrkraft bewertet).

Unter dem PDF-Knopf steht (aus `pdf_erinnerung.js`) der Ersatzweg-Hinweis: »Geht LMS gerade nicht? Dann schick die PDF per E-Mail an die Lehrkraft.« Ohne E-Mail-Adresse, damit sie nicht auf der öffentlichen Seite steht.
