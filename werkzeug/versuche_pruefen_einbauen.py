"""Knopf »Eingaben prüfen« (Hinweise und Tipps in Stufen) unter jedem Versuch der Versuchsseiten einbauen.
Aufruf im Repository-Ordner: python3 werkzeug/versuche_pruefen_einbauen.py   (wiederholbar: ersetzt den Block)

Quelle der Regeln: werkzeug/versuche_pruefung.json (Einheit-Ordner -> Versuch-ID -> Felder). Das Skript setzt Regeln + werkzeug/versuche_pruefen.js
inline vor </body> jeder Versuchsseite, die in der JSON-Datei steht. Gibt es für eine Versuchsseite mit Versuchen noch keine Regeln, meldet es das
(dann hat diese Seite noch keinen Knopf). Ändert keinen Speicherschlüssel; Prüf-Zähler liegen in S.chk (nicht in S.a).
Neue Versuchsseite: Regeln in der JSON-Datei ergänzen, dann dieses Skript (oder werkzeug/nach_dem_bauen.py) ausführen."""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATEN = json.load(open(os.path.join(ROOT, "werkzeug", "versuche_pruefung.json"), encoding="utf-8"))["einheiten"]
JS = open(os.path.join(ROOT, "werkzeug", "versuche_pruefen.js"), encoding="utf-8").read()
RE_BLOCK = re.compile(r"<!-- vspruefen:start -->.*?<!-- vspruefen:end -->\n?", re.S)
RE_V = re.compile(r"const V = (\[.*?\]);\n", re.S)

fehler, n = [], 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "versuche.html"))):
    ordner = os.path.relpath(os.path.dirname(f), ROOT).replace(os.sep, "/")
    if ordner.startswith("werkzeug"): continue
    s = open(f, encoding="utf-8", newline="").read()
    m = RE_V.search(s)
    if not m or "const KEY" not in s: continue
    ids = [v["id"] for v in json.loads(m.group(1))]
    regeln = DATEN.get(ordner)
    if regeln is None:
        fehler.append(f"{ordner}/versuche.html: keine Regeln in versuche_pruefung.json (Seite bekommt keinen Prüf-Knopf)"); continue
    fehlt = [i for i in ids if i not in regeln]
    if fehlt: fehler.append(f"{ordner}: keine Regeln für Versuch(e) {', '.join(fehlt)}")
    block = ("<!-- vspruefen:start -->\n<script>window.__VS_PRUEFUNG = " + json.dumps(regeln, ensure_ascii=False, separators=(",", ":")) + ";\n" + JS + "</script>\n<!-- vspruefen:end -->\n")
    alt = s
    s = RE_BLOCK.sub("", s)
    i = s.rindex("</body>"); s = s[:i] + block + s[i:]
    if s != alt:
        open(f, "w", encoding="utf-8", newline="").write(s)
    n += 1; print("Prüf-Knopf:", ordner, f"({len(ids)} Versuche)")
print(n, "Versuchsseiten")
if fehler:
    print("\nHinweise:"); [print(" -", x) for x in fehler]; sys.exit(1)
