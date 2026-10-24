"""PILOT: kompakteres Arbeitsblatt (Fahrplan zugeklappt, Pflicht/Zusatz getrennt, Knopf zur ersten offenen Pflichtaufgabe).
Nur die hier genannten Seiten. Aufruf: python3 werkzeug/pilot_layout_einbauen.py   (wiederholbar; Block `pilot-layout`).
Zum Zurücknehmen: Seite aus SEITEN streichen und das Skript erneut ausführen (entfernt den Block). Ändert keinen Speicherschlüssel."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEITEN = ["4ab-nawi/k1-5a-elektromagnet/aufgaben.html"]
JS = open(os.path.join(ROOT, "werkzeug", "pilot_layout.js"), encoding="utf-8").read()
RE_BLOCK = re.compile(r"<!-- pilot-layout:start -->.*?<!-- pilot-layout:end -->\n?", re.S)
import glob
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html"))):
    rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
    s = open(f, encoding="utf-8", newline="").read(); alt = s
    s = RE_BLOCK.sub("", s)
    if rel in SEITEN:
        i = s.rindex("</body>"); s = s[:i] + "<!-- pilot-layout:start -->\n<script>" + JS + "</script>\n<!-- pilot-layout:end -->\n" + s[i:]
    if s != alt: open(f, "w", encoding="utf-8", newline="").write(s); print("Pilot-Layout:", rel)
