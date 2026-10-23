"""Kasten »Für LMS: x von y Punkten · Notenvorschlag« oben auf Seite 1 der Abgabe-PDF (nur dort, nicht auf dem Bildschirm).
Aufruf: python3 werkzeug/notenvorschlag_einbauen.py   (wiederholbar). Betrifft Seiten mit prüfbaren Aufgaben:
Arbeitsblätter mit `function checkField` und Seiten mit `function pdfStats` (Nobel, Vertiefung). Ändert keinen Speicherschlüssel."""
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "notenvorschlag.js"), encoding="utf-8").read()
RE_BLOCK = re.compile(r"<!-- notenvorschlag:start -->.*?<!-- notenvorschlag:end -->\n?", re.S)
n = 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html"))):
    ordner = os.path.relpath(f, ROOT).replace(os.sep, "/")
    if ordner.startswith("werkzeug"): continue
    s = open(f, encoding="utf-8", newline="").read()
    if not ("function checkField" in s or "function pdfStats" in s) or "async function buildPdf" not in s and "function buildPdf" not in s: continue
    alt = s
    s = RE_BLOCK.sub("", s)
    i = s.rindex("</body>"); s = s[:i] + "<!-- notenvorschlag:start -->\n<script>" + JS + "</script>\n<!-- notenvorschlag:end -->\n" + s[i:]
    if s != alt: open(f, "w", encoding="utf-8", newline="").write(s)
    n += 1; print("Notenvorschlag:", ordner)
print(n, "Seiten")
