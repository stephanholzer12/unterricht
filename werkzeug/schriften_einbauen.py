"""Schriften lokal statt Google Fonts.
Aufruf im Repository-Ordner: python3 werkzeug/schriften_einbauen.py   (wiederholbar: ändert nichts, wenn schon umgestellt)

Warum: Beim Öffnen einer Seite fragte jedes Handy bei Google nach den Schriften (Datenschutz, und im Schul-WLAN/bei
schwachem Netz kann das hängen). Die Schriften liegen jetzt im Ordner schriften/ (Source Sans 3 und Source Serif 4, Lizenz OFL).
Die Seiten verlinken ../../schriften/schriften.css. Die Ersatzschriften (Calibri, Georgia …) bleiben in den CSS-Angaben
der Seiten unverändert stehen. Speicherschlüssel und Antworten werden nicht angefasst.

Gilt für fertige Seiten (*/*/*.html) und für die Bauskripte/Vorlagen unter werkzeug/ (dort Seiten der Tiefe 2)."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = '<link rel="stylesheet" href="../../schriften/schriften.css">'
RE_PRE = re.compile(r'<link rel="preconnect" href="https://fonts\.(?:googleapis|gstatic)\.com"(?: crossorigin)?>(?:\\n|\n)?')
RE_CSS = re.compile(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*">')

ziele = [f for f in glob.glob(os.path.join(ROOT, "*", "*", "*.html"))
         if not os.path.relpath(f, ROOT).startswith("werkzeug" + os.sep)]
for pat in ("werkzeug/vorlagen/*.html", "werkzeug/vorlagen/*.py", "werkzeug/quellen/**/*.py", "werkzeug/quellen/**/*.html"):
    ziele += glob.glob(os.path.join(ROOT, pat), recursive=True)

n = 0
for f in sorted(set(ziele)):
    with open(f, encoding="utf-8", newline="") as fh:
        s = fh.read()
    if "fonts.googleapis.com" not in s and "fonts.gstatic.com" not in s:
        continue
    neu = RE_PRE.sub("", s)
    neu = RE_CSS.sub(LINK, neu)
    if "fonts.g" in neu:
        print("NICHT vollständig umgestellt:", os.path.relpath(f, ROOT)); continue
    with open(f, "w", encoding="utf-8", newline="") as fh:
        fh.write(neu)
    n += 1
    print("umgestellt:", os.path.relpath(f, ROOT))
print(n, "Dateien")
