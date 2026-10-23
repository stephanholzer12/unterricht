# Teststoff (eine A4-Seite) – für alle Klassen und Fächer

Regelwerk Abschnitt 16. Jede Teststoff-Seite wird mit **diesem einen Generator** gebaut, damit sie in allen Projekten und Klassen gleich aussieht.

```
node werkzeug/teststoff/teststoff.js werkzeug/teststoff/daten/<schuljahr>-<klasse>-test<nr>.json <Zielordner>
```

- Schreibt die .docx mit dem Namen aus `"datei"` (z. B. `26-27-4AB-Test1-Teststoff-v2.docx`) und prüft, ob sie auf **genau eine Seite** passt.
- Listet alles auf, was gelb markiert ist (`[[…]]`) – diese Liste kurz im Chat an Stephan geben.
- QR-Codes werden aus den Links erzeugt (Python-Paket `qrcode`: `pip install qrcode --break-system-packages`).

## Neue Teststoff-Seite

1. `daten/vorlage.json` kopieren → `daten/<schuljahr>-<klasse>-test<nr>.json` (z. B. `26-27-2ab-test1.json`).
2. Ausfüllen – Lernziele aus »Kann ich das?« der Theorie-Seiten, Fachbegriffe aus den Begriff-Tabellen, Aufgabennummern aus den Fahrplänen in `einheiten.json`.
3. Auszeichnung: `**fett**` · `[[gelb = Stephan ergänzt]]` (was Claude nicht sicher weiß).
4. Ohne Formeln: `"formeln": []` und `"tipp"` weglassen.
5. Bauen, PNG ansehen, im Test-Training-Eintrag von `einheiten.json` bei `dateien.liste` die neue Version eintragen.
6. Neue Fassung = `"datei"` und `"fuss"` mit nächster Versionsnummer (v2, v3 …).

## Felder

| Feld | Inhalt |
|---|---|
| `datei` | Dateiname laut Regelwerk 2, mit `-v<Nr>` |
| `kopf` | `TESTSTOFF · FACH · X. JAHRGANG` |
| `titel` | `<Nr>. Test – <Thema>` |
| `fuss` | `<Klasse> · <Nr>. Test <Fach> · Teststoff · Stand <Datum> · v<Nr>` |
| `termin`, `stoff` | Kasten oben (Wochentag + Datum; Buchseiten + »alle Unterlagen aus dem Unterricht«) |
| `durchgenommen` | Zeilen `[Nr, Thema, Schulbuch, Unterlagen, Aufgaben]` |
| `koennen` | Zeilen `[Nr, "**Thema:** Ich kann … · …", Fachbegriffe]` |
| `formeln`, `tipp` | `[[Formel, Einheit], …]` + Umrechnungs-Tipp (optional) |
| `kein_teststoff` | Liste (OPTIONAL/»Für Schnelle«, nicht durchgenommene Kapitel) |
| `qr` | `[{titel, text, url}]` – Test-Training und Klassenseite, Links vollständig |

`daten/vorlage.json` baut die leere Vorlage `26-27-Vorlage-Teststoff-v<Nr>.docx` (QR-Felder als Platzhalter).
