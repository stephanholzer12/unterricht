"""Speicherstatus + ehrliche PDF-Meldung für alle Handy-Seiten mit PDF-Abgabe (erkennbar an jsPDF).
Aufruf im Repository-Ordner: python3 werkzeug/speicherstatus_einbauen.py
Nach jeder neuen Seite und nach Änderungen an speicherstatus.js erneut ausführen (mehrfaches Ausführen ändert nichts).

Was es tut:
 1. Setzt werkzeug/speicherstatus.js inline vor </body> (zwischen <!-- speicherstatus:start --> und <!-- speicherstatus:end -->):
    sichtbarer Speicherstatus, Warnung bei Speicherfehlern, dunkleres Grün für »Gespeichert«/»Richtig«.
 2. Ändert die Meldung nach dem normalen PDF-Download von »Gespeichert: …« auf »PDF wurde erstellt: …«. Der Browser meldet
    nämlich nur, dass der Download gestartet wurde, nicht ob die Datei wirklich auf dem Handy liegt.
    (Die Meldung im Claude-Viewer, wo das Speichern bestätigt wird, bleibt »Gespeichert«.)
 3. Setzt aria-live="polite" auf die PDF-Statuszeile #pdfstatus (Screenreader sagen Statusänderungen an).
Es ändert KEINEN Speicherschlüssel (const KEY = …) und keine Antwort.
In den Quell-Vorlagen (werkzeug/quellen, werkzeug/vorlagen) werden nur Punkt 2 und 3 angewendet, damit neu gebaute Seiten
gleich stimmen; der Baustein aus Punkt 1 kommt dort durch diesen Skriptlauf nach dem Bauen dazu."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = open(os.path.join(ROOT, "werkzeug", "speicherstatus.js"), encoding="utf-8").read()
BLOCK = "<!-- speicherstatus:start -->\n<script>\n" + JS + "</script>\n<!-- speicherstatus:end -->\n"

MSG_ALT = 'say("ok", "Gespeichert: " + filename + " – jetzt in LMS hochladen.");'
MSG_NEU = ('say("ok", "PDF wurde erstellt: " + filename + '
           '" – schau in deinen Downloads nach, ob sie da ist, und lade sie dann in LMS hoch.");')
# Nur der normale Download-Weg (Ankerklick mit blob-URL) – dort weiß die Seite nicht, ob die Datei ankam.
RE_MSG = re.compile(r"(setTimeout\(\(\) => URL\.revokeObjectURL\(url\), 30000\);\s*)" + re.escape(MSG_ALT))
RE_PDFSTATUS = re.compile(r'<([a-z]+)([^>]*\bid="pdfstatus"[^>]*)>')
RE_BLOCK = re.compile(r"<!-- speicherstatus:start -->.*?<!-- speicherstatus:end -->\n?", re.S)


def lesen(f):
    with open(f, encoding="utf-8", newline="") as fh:
        return fh.read()


def schreiben(f, s):
    with open(f, "w", encoding="utf-8", newline="") as fh:
        fh.write(s)


def meldung_und_aria(s):
    s, n_msg = RE_MSG.subn(lambda m: m.group(1) + MSG_NEU, s)

    def aria(m):
        return m.group(0) if "aria-live" in m.group(2) else f'<{m.group(1)}{m.group(2)} aria-live="polite">'
    s, n_aria = RE_PDFSTATUS.subn(aria, s)
    return s, n_msg, n_aria


seiten, fehler = 0, []
for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html"))):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("werkzeug" + os.sep): continue
    s = lesen(f)
    if "jsPDF" not in s: continue
    alt = s
    s, n_msg, n_aria = meldung_und_aria(s)
    s = RE_BLOCK.sub("", s)
    i = s.rindex("</body>")
    s = s[:i] + BLOCK + s[i:]
    if n_msg < 1 and "PDF wurde erstellt:" not in s: fehler.append(f"{rel}: Download-Meldung nicht gefunden")
    if "id=\"pdfstatus\"" not in s: fehler.append(f"{rel}: #pdfstatus fehlt")
    if s != alt: schreiben(f, s)
    seiten += 1
    print("Speicherstatus:", rel, "(Meldung geändert)" if n_msg else "")
print(seiten, "Seiten")

# Quellen und Vorlagen: nur Meldung + aria-live
quellen = 0
for pat in ("werkzeug/quellen/**/*.html", "werkzeug/quellen/**/*.py", "werkzeug/vorlagen/*.html"):
    for f in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
        s = lesen(f)
        if MSG_ALT not in s and "pdfstatus" not in s: continue
        neu, n_msg, n_aria = meldung_und_aria(s)
        if neu != s:
            schreiben(f, neu); quellen += 1
            print("Quelle/Vorlage:", os.path.relpath(f, ROOT), f"(Meldung {n_msg}, aria {n_aria})")
print(quellen, "Quell-/Vorlagendateien angepasst")

if fehler:
    print("\nFEHLER:"); [print(" -", x) for x in fehler]; sys.exit(1)
