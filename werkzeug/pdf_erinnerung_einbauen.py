"""Erinnerung »PDF noch nicht abgegeben / seit der PDF geändert« für alle Seiten mit PDF-Abgabe (erkennbar an jsPDF).
Aufruf im Repository-Ordner: python3 werkzeug/pdf_erinnerung_einbauen.py
Nach jeder neuen Seite und nach Änderungen an pdf_erinnerung.js erneut ausführen (wiederholbar, ersetzt den Baustein).
Liest den Seitenschlüssel (const KEY = "…") aus der Seite und setzt ihn als window.__PE_KEY davor. Ändert keinen Schlüssel."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "pdf_erinnerung.js"), encoding="utf-8").read()
RE_BLOCK = re.compile(r"<!-- pdferinnerung:start -->.*?<!-- pdferinnerung:end -->\n?", re.S)
RE_KEY = re.compile(r'const KEY = "([^"]+)"')
fehler, n = [], 0
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html"))):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("werkzeug" + os.sep): continue
    with open(f, encoding="utf-8", newline="") as fh: s = fh.read()
    if "jsPDF" not in s: continue
    keys = set(RE_KEY.findall(s))
    if len(keys) != 1 or 'id="pdfbtn"' not in s:
        fehler.append(f"{rel}: Schlüssel/PDF-Knopf nicht eindeutig ({len(keys)} Schlüssel)"); continue
    block = ("<!-- pdferinnerung:start -->\n<script>window.__PE_KEY = " + '"' + keys.pop() + '"' + ";\n" + JS + "</script>\n<!-- pdferinnerung:end -->\n")
    alt = s
    s = RE_BLOCK.sub("", s)
    i = s.rindex("</body>"); s = s[:i] + block + s[i:]
    if s != alt:
        with open(f, "w", encoding="utf-8", newline="") as fh: fh.write(s)
    n += 1; print("PDF-Erinnerung:", rel)
print(n, "Seiten")
if fehler: print("\nFEHLER:"); [print(" -", x) for x in fehler]; sys.exit(1)
