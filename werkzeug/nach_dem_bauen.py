"""EIN Aufruf nach dem Bauen oder Ändern einer Einheit: python3 werkzeug/nach_dem_bauen.py
Führt der Reihe nach aus (alle wiederholbar, ändern keinen Speicherschlüssel):
  1. speicherstatus_einbauen.py   – »Gespeichert um …« / Warnung bei Speicherfehler
  2. pdf_erinnerung_einbauen.py   – »Noch keine PDF / seit der PDF geändert / PDF passt«
  3. pdf_programm_auslagern.py    – PDF-Programm + PDF-Schrift aus der Seite in gemeinsam/pdf-programm-v1.js
  4. schriften_einbauen.py        – Schriften lokal statt Google Fonts
  4b. abgabezeit_einbauen.py      – Datum UND Uhrzeit im PDF-Kopf und im Kopier-Text
  4c. versuche_pruefen_einbauen.py – Knopf »Eingaben prüfen« (Hinweise/Tipps in Stufen) unter jedem Versuch; Regeln: werkzeug/versuche_pruefung.json
  4d. pruefung_nachsicht_einbauen.py – großzügigere »Prüfen«-Auswertung der Arbeitsblätter (Einheiten, Rundung, Schreibweise); Korrekturen: werkzeug/pruefregeln_korrekturen.json
  4f. pilot_layout_einbauen.py    – PILOT (nur 4AB Elektromagnet): Fahrplan/Zusatz zugeklappt, Pflicht-Fortschritt
  4e. notenvorschlag_einbauen.py  – Kasten »Für LMS: x von y Punkten · Notenvorschlag« oben auf Seite 1 der PDF (nur im PDF)
  5. build_index.py               – Klassenseiten, Fahrplan, Lehrer-Seite
  6. pruefen.py                   – Kontrolle (dieselbe wie bei jedem Push)
Danach: git status ansehen, nur die eigene Einheit committen, git pull --rebase, git push."""
import os, subprocess, sys
W = os.path.dirname(os.path.abspath(__file__))
for s in ("speicherstatus_einbauen.py", "pdf_erinnerung_einbauen.py", "pdf_programm_auslagern.py",
          "schriften_einbauen.py", "abgabezeit_einbauen.py", "versuche_pruefen_einbauen.py", "pruefung_nachsicht_einbauen.py", "notenvorschlag_einbauen.py", "pilot_layout_einbauen.py", "build_index.py", "pruefen.py"):
    print(f"\n=== {s} ===", flush=True)
    r = subprocess.run([sys.executable, os.path.join(W, s)], cwd=os.path.dirname(W))
    if r.returncode:
        print(f"\nABBRUCH: {s} meldet einen Fehler (siehe oben)."); sys.exit(r.returncode)
print("\nFertig – alles in Ordnung.")
