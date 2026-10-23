"""Datum UND Uhrzeit im PDF-Kopf und im Kopier-Text aller Abgabeseiten.
Aufruf im Repository-Ordner: python3 werkzeug/abgabezeit_einbauen.py   (wiederholbar)

Warum: Meldet ein Kadett »LMS ging nicht« und schickt die PDF per E-Mail, zeigt das PDF selbst, wann es erstellt wurde
(Uhrzeit des Handys des Kadetten, auf die Minute). Seiten der neuesten Generation (»Abgabe: Datum, Uhrzeit«) hatten das schon.
Ändert keinen Speicherschlüssel und keine Antwort."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = ('new Date().toLocaleDateString("de-AT") + ", " + new Date().toLocaleTimeString("de-AT", { hour: "2-digit", minute: "2-digit" })')
D = 'new Date().toLocaleDateString("de-AT")'
ERS = [  # (alt, neu)
    ('d.text("Datum: " + ' + D + ', M + 140, y);', 'd.text("Datum: " + ' + STAMP + ', W - M, y, { align: "right" });'),
    ('d.text("Datum: " + ' + D + ', W - M, y + 4, { align: "right" });', 'd.text("Datum: " + ' + STAMP + ', W - M, y + 4, { align: "right" });'),
    ('d.text("KLASSE", M + 112, y + 3.6); d.text("DATUM", M + 140, y + 3.6);', 'd.text("KLASSE", M + 100, y + 3.6); d.text("DATUM, UHRZEIT", M + 122, y + 3.6);'),
    ('d.text(clean(S.klasse || "—"), M + 112, y + 7.6); d.text(' + D + ', M + 140, y + 7.6);',
     'd.text(clean(S.klasse || "—"), M + 100, y + 7.6); d.text(' + STAMP + ', M + 122, y + 7.6);'),
]
ziele = [f for f in glob.glob(os.path.join(ROOT, "*", "*", "*.html")) if not os.path.relpath(f, ROOT).startswith("werkzeug" + os.sep)]
for pat in ("werkzeug/vorlagen/*.html", "werkzeug/vorlagen/*.py", "werkzeug/vorlagen/*.js", "werkzeug/quellen/**/*.py", "werkzeug/quellen/**/*.html"):
    ziele += glob.glob(os.path.join(ROOT, pat), recursive=True)
n = 0
for f in sorted(set(ziele)):
    s = open(f, encoding="utf-8", newline="").read(); neu = s
    for alt, ers in ERS:
        neu = neu.replace(alt, ers)
    # Kopier-Text: nur dort ersetzen, wo noch keine Uhrzeit dahinter steht (sonst würde sie doppelt eingefügt)
    neu = re.sub(r'" · " \+ ' + re.escape(D) + r'(?! \+ ", ")', lambda m: '" · " + ' + STAMP, neu)
    if neu != s:
        open(f, "w", encoding="utf-8", newline="").write(neu); n += 1; print("Uhrzeit ergänzt:", os.path.relpath(f, ROOT))
print(n, "Dateien")
