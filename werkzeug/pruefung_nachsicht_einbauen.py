"""Großzügigere Prüfung (Zahlen, Einheiten, Rundung, Schreibweise, Tippfehler) in die Arbeitsblätter mit »Prüfen«-Knopf einbauen.
Aufruf im Repository-Ordner: python3 werkzeug/pruefung_nachsicht_einbauen.py   (wiederholbar: ersetzt den Block)
Betrifft alle aufgaben.html mit `function checkField`. Quelle: werkzeug/pruefung_nachsicht.js + werkzeug/pruefregeln_korrekturen.json.
Ändert keinen Speicherschlüssel. Block steht NACH dem Seitenprogramm (vor </body>)."""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "pruefung_nachsicht.js"), encoding="utf-8").read()
KOR = json.load(open(os.path.join(ROOT, "werkzeug", "pruefregeln_korrekturen.json"), encoding="utf-8"))["einheiten"]
RE_BLOCK = re.compile(r"<!-- nachsicht:start -->.*?<!-- nachsicht:end -->\n?", re.S)
n = 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "aufgaben.html"))):
    ordner = os.path.relpath(os.path.dirname(f), ROOT).replace(os.sep, "/")
    if ordner.startswith("werkzeug"): continue
    s = open(f, encoding="utf-8", newline="").read()
    if "function checkField" not in s: continue
    block = ("<!-- nachsicht:start -->\n<script>window.__CHK_KORREKTUR = " + json.dumps(KOR.get(ordner, {}), ensure_ascii=False, separators=(",", ":")) + ";\n" + JS + "</script>\n<!-- nachsicht:end -->\n")
    alt = s
    s = RE_BLOCK.sub("", s)
    i = s.rindex("</body>"); s = s[:i] + block + s[i:]
    if s != alt: open(f, "w", encoding="utf-8", newline="").write(s)
    n += 1; print("Großzügige Prüfung:", ordner)
print(n, "Arbeitsblätter")
