"""PDF-Programm (jsPDF 2.5.1) und PDF-Schrift aus den Seiten in EINE gemeinsame Datei auslagern: gemeinsam/pdf-programm-v1.js
Aufruf im Repository-Ordner: python3 werkzeug/pdf_programm_auslagern.py   (wiederholbar; neu gebaute Seiten danach erneut)

Warum: Jede Abgabeseite trug das PDF-Programm (355 KB) und die eingebettete PDF-Schrift (2 × 64 KB) selbst mit – rund 480 KB
von ca. 600 KB je Seite. Als gemeinsame Datei lädt das Handy sie einmal und nimmt sie danach aus dem Zwischenspeicher.
Die Seite lädt die Datei beim Öffnen (wie vorher den eingebetteten Teil); danach geht »PDF erstellen« auch ohne Netz.
Ändert keinen Speicherschlüssel und keine Antwort. Bei einer neuen Version der gemeinsamen Datei den Namen hochzählen (-v2).
Seiten ohne exakt dieses Programm bzw. diese Schrift werden NICHT angefasst (Meldung)."""
import glob, hashlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "pdf-programm-v1.js"
ZIEL = os.path.join(ROOT, "gemeinsam", NAME)
RE_JS = re.compile(r"<script>\s*(/\* jsPDF 2\.5\.1 \(MIT\) \*/.*?)\s*</script>\n?", re.S)
RE_FONT = re.compile(r'(FONT_[RB])\s*=\s*"([A-Za-z0-9+/=]{20000,})"')
TAG = (f'<script src="../../gemeinsam/{NAME}"></script>\n'
       # Lädt die Datei beim ersten Mal nicht (Funkloch), sofort ein zweites Mal versuchen – noch bevor die Seite weiterläuft.
       f'<script>if (!window.jspdf) document.write(\'<script src="../../gemeinsam/{NAME}?nochmal=1"><\\/script>\');</script>\n')
ALT_TAG = f'<script src="../../gemeinsam/{NAME}"></script>\n'

seiten = [f for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html")))
          if not os.path.relpath(f, ROOT).startswith("werkzeug" + os.sep)]
jsv, fontv, plan, fehler = set(), {}, [], []
for f in seiten:
    s = open(f, encoding="utf-8").read()
    if "/* jsPDF 2.5.1 (MIT) */" not in s:
        continue
    j = RE_JS.findall(s); fo = RE_FONT.findall(s)
    if len(j) != 1 or sorted(n for n, _ in fo) != ["FONT_B", "FONT_R"]:
        fehler.append(f"{os.path.relpath(f, ROOT)}: Aufbau unerwartet – nicht angefasst"); continue
    code = re.sub(r"\n//# sourceMappingURL=\S+\s*$", "", j[0].rstrip())
    jsv.add(code)
    for n, v in fo: fontv.setdefault(n, set()).add(v)
    plan.append(f)
if len(jsv) > 1 or any(len(v) > 1 for v in fontv.values()):
    print("FEHLER: Seiten haben unterschiedliche PDF-Programme/Schriften – abgebrochen, nichts geändert."); sys.exit(1)

if plan:
    inhalt = ("/* Gemeinsame Datei aller Abgabeseiten: jsPDF 2.5.1 (MIT-Lizenz, https://github.com/parallax/jsPDF) + eingebettete PDF-Schrift.\n"
              "   Erzeugt von werkzeug/pdf_programm_auslagern.py – nicht von Hand ändern. */\n"
              + jsv.pop() + "\n;\nwindow.__PDF_FONT_R = \"" + fontv["FONT_R"].pop() + "\";\nwindow.__PDF_FONT_B = \"" + fontv["FONT_B"].pop() + "\";\n")
    os.makedirs(os.path.dirname(ZIEL), exist_ok=True)
    if os.path.exists(ZIEL) and open(ZIEL, encoding="utf-8").read() != inhalt:
        print(f"FEHLER: {NAME} gibt es schon mit anderem Inhalt – neue Version (-v2) anlegen."); sys.exit(1)
    open(ZIEL, "w", encoding="utf-8").write(inhalt)
    print(f"gemeinsam/{NAME}: {len(inhalt.encode()) // 1024} KB")

# schon ausgelagerte Seiten auf den aktuellen Lade-Baustein bringen
for f in seiten:
    s = open(f, encoding="utf-8", newline="").read()
    if ALT_TAG in s and TAG not in s:
        open(f, "w", encoding="utf-8", newline="").write(s.replace(ALT_TAG, TAG, 1)); print("Lade-Baustein erneuert:", os.path.relpath(f, ROOT))

for f in plan:
    s = open(f, encoding="utf-8", newline="").read()
    s = RE_JS.sub(lambda m: TAG, s, count=1)
    s = RE_FONT.sub(lambda m: f"{m.group(1)} = window.__PDF_{m.group(1)} || \"\"", s)
    open(f, "w", encoding="utf-8", newline="").write(s)
    print("ausgelagert:", os.path.relpath(f, ROOT), f"({len(s.encode()) // 1024} KB)")
if fehler:
    print("\nHinweise:"); [print(" -", x) for x in fehler]; sys.exit(1)
