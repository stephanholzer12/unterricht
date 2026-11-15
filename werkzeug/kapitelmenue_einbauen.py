"""Kapitel-Menü (werkzeug/kapitelmenue.js) in die Theorie-Seiten einbauen – statt der Wischleiste mit Kapiteln.
Aufruf im Repository-Ordner: python3 werkzeug/kapitelmenue_einbauen.py  (läuft auch in nach_dem_bauen.py; mehrfaches Ausführen ändert nichts)

Welche Einheiten? Nur die mit "kapitelmenue": true in werkzeug/einheiten.json (Stephan, 15.11.2026:
alle neuen Einheiten und die noch versteckten; schon sichtbare laufende Einheiten bleiben bei der alten Leiste).
Der Block steht zwischen <!-- kapitelmenue:start --> und <!-- kapitelmenue:end --> vor </body>.
Ändert keine Antworten und keinen Speicherschlüssel; ohne JavaScript bleibt die alte Leiste."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "kapitelmenue.js"), encoding="utf-8").read()
BLOCK = "<!-- kapitelmenue:start -->\n<script>\n" + JS + "</script>\n<!-- kapitelmenue:end -->\n"
RE_BLOCK = re.compile(r"<!-- kapitelmenue:start -->.*?<!-- kapitelmenue:end -->\n?", re.S)

einheiten = json.load(open(os.path.join(ROOT, "werkzeug", "einheiten.json"), encoding="utf-8"))
n, fehler = 0, []
for e in einheiten:
    f = os.path.join(ROOT, e["ordner"], "theorie.html")
    if not os.path.exists(f): continue
    with open(f, encoding="utf-8", newline="") as fh: s = fh.read()
    alt = s
    s = RE_BLOCK.sub("", s)
    if e.get("kapitelmenue"):
        if 'class="toc"' not in s: fehler.append(e["ordner"] + ": keine Kapitel-Leiste (nav.toc) gefunden"); continue
        i = s.rindex("</body>"); s = s[:i] + BLOCK + s[i:]
    if s != alt:
        with open(f, "w", encoding="utf-8", newline="") as fh: fh.write(s)
        n += 1
print(f"Kapitel-Menü: {n} Seite(n) geändert" + ("" if not fehler else " · FEHLER: " + "; ".join(fehler)))
if fehler: raise SystemExit(1)
