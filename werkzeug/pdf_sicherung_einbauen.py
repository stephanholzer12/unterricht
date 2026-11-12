"""Setzt werkzeug/pdf_sicherung.js inline in Handy-Seiten mit PDF-Abgabe (Probe).
Aufruf im Repository-Ordner: python3 werkzeug/pdf_sicherung_einbauen.py <ordner> [<ordner> …]   (z. B. 1ab-nawi/k2-1-kraefte)
Ohne Ordner: nur die Probe-Einheiten aus der Liste PROBE. Wiederholbar; ändert keinen Speicherschlüssel.
Ersetzt einen vorhandenen Block zwischen <!-- pdf_sicherung:start --> und <!-- pdf_sicherung:end -->."""
import glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "pdf_sicherung.js"), encoding="utf-8").read()
BLOCK = "<!-- pdf_sicherung:start -->\n<script>\n" + JS + "</script>\n<!-- pdf_sicherung:end -->\n"
n = 0
PROBE = ["1ab-nawi/k2-1-kraefte", "5ak-iwk/k2-1-globalisierung"]  # Probe-Einheiten (Stephan, 12.11.2026); ohne Angabe werden genau diese behandelt
for ordner in (sys.argv[1:] or PROBE):
    for f in sorted(glob.glob(os.path.join(ROOT, ordner, "*.html"))):
        s = open(f, encoding="utf-8").read()
        if "jspdf" not in s.lower() or 'id="resetwrap"' not in s: continue
        s = re.sub(r"<!-- pdf_sicherung:start -->.*?<!-- pdf_sicherung:end -->\n?", "", s, flags=re.S)
        i = s.rindex("</body>")
        open(f, "w", encoding="utf-8").write(s[:i] + BLOCK + s[i:]); n += 1
        print("PDF-Sicherung:", os.path.relpath(f, ROOT))
print(n, "Seiten")
