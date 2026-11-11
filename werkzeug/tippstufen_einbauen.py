"""Setzt werkzeug/tippstufen.js inline in Arbeitsblätter, deren Aufgaben ein Feld tipp1 haben (Tipp-Stufen, Theorie-Karte, »Was glaubst du?«).
Aufruf im Repository-Ordner: python3 werkzeug/tippstufen_einbauen.py  (idempotent: ersetzt den Block zwischen <!-- tippstufen:start --> und <!-- tippstufen:end -->).
Seiten ohne tipp1 bleiben unverändert."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "tippstufen.js"), encoding="utf-8").read()
n = 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "aufgaben.html"))):
    s = open(f, encoding="utf-8").read()
    if "function showCheck" not in s: continue
    s2 = re.sub(r"<!-- tippstufen:start -->.*?<!-- tippstufen:end -->\n?", "", s, flags=re.S)
    if '"tipp1"' in s2:
        i = s2.rindex("</body>")
        s2 = s2[:i] + "<!-- tippstufen:start -->\n<script>\n" + JS + "</script>\n<!-- tippstufen:end -->\n" + s2[i:]
        n += 1; print("Tipp-Stufen:", os.path.relpath(os.path.dirname(f), ROOT))
    if s2 != s: open(f, "w", encoding="utf-8").write(s2)
print(n, "Seiten")
