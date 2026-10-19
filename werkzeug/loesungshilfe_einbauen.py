"""Setzt werkzeug/loesungshilfe.js inline in alle Arbeitsblätter mit »Prüfen« (erkennbar an function showCheck)
und passt in der PDF die Zeile »Bewertung« an (Status: selbst gelöst / nach Tipp / Lösung angesehen).
Übungsvarianten mit neuen Zahlen stehen in werkzeug/loesungshilfe_varianten.json (Schlüssel = Ordner der Einheit).
Aufruf im Repository-Ordner: python3 werkzeug/loesungshilfe_einbauen.py  – nach jedem neuen Arbeitsblatt und nach Änderungen erneut ausführen
(idempotent: ersetzt den Block zwischen <!-- loesungshilfe:start --> und <!-- loesungshilfe:end -->)."""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "loesungshilfe.js"), encoding="utf-8").read()
VAR = json.load(open(os.path.join(ROOT, "werkzeug", "loesungshilfe_varianten.json"), encoding="utf-8"))

ALT = 'txt("Bewertung: " + st, 9.5, "bold", ev && ev.ok ? [70, 110, 40] : muted, M + 4, CW - 4);'
NEU = ('txt("Bewertung: " + (typeof LH_pdf === "function" ? LH_pdf(t, st) : st), 9.5, "bold", '
       '(typeof LH_viewed === "function" && LH_viewed(t)) ? rust : (ev && ev.ok ? [70, 110, 40] : muted), M + 4, CW - 4);')

n = 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "aufgaben.html"))):
    s = open(f, encoding="utf-8").read()
    if "function showCheck" not in s: continue
    ordner = os.path.relpath(os.path.dirname(f), ROOT).replace(os.sep, "/")
    if ALT in s: s = s.replace(ALT, NEU)
    elif NEU not in s: print("ACHTUNG: PDF-Zeile nicht gefunden in", ordner)
    s = re.sub(r"<!-- loesungshilfe:start -->.*?<!-- loesungshilfe:end -->\n?", "", s, flags=re.S)
    block = ("<!-- loesungshilfe:start -->\n<script>\nwindow.LH_VARIANTEN = " + json.dumps(VAR.get(ordner, []), ensure_ascii=False) +
             ";\n" + JS + "</script>\n<!-- loesungshilfe:end -->\n")
    i = s.rindex("</body>")
    s = s[:i] + block + s[i:]
    open(f, "w", encoding="utf-8").write(s); n += 1
    print("Lösungshilfe:", ordner, "· Varianten:", len(VAR.get(ordner, [])))
print(n, "Seiten")
