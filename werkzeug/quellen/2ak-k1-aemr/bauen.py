"""Handy-Arbeitsblatt PBGW 2AK · K1 »70 Jahre AEMR« bauen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ak-k1-aemr/bauen.py
Grundlage: 4ab-nawi/k1-5a-elektromagnet/aufgaben.html (Sofort-Feedback, Lösungen nach Abgabe, PDF, PDF-Hilfe).
Schreibt 2ak-pbgw/k1-aemr/aufgaben.html. Danach: python3 werkzeug/pdf_hilfe_einbauen.py und build_index.py."""
import base64, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
from daten import T, STAND

UNIT = "2ak-pbgw/k1-aemr/"
DST = os.path.join(ROOT, UNIT)
BASE = "https://stephanholzer12.github.io/unterricht/"
os.makedirs(DST, exist_ok=True)
EYEBROW = "PBGW · 2AK · K1 Menschenrechte · Arbeitsblatt »70 Jahre AEMR«"
TITLE = "Menschenrechte-Aufgaben"


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


s = open(os.path.join(ROOT, "4ab-nawi/k1-5a-elektromagnet/aufgaben.html"), encoding="utf-8").read()


def rep(old, new, count=1, regex=False):
    global s
    n = len(re.findall(old, s)) if regex else s.count(old)
    assert n == count, (old[:80], n)
    s = re.sub(old, lambda m: new, s) if regex else s.replace(old, new)


rep("<title>Elektromagnet-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor</div>", EYEBROW + "</div>", 2)
rep("<h1>Elektromagnet-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Elektromagnet-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+',
           lambda m: m.group(1) + qr_b64(BASE + UNIT + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>4AK</option><option>4BK</option>', '<option value="">–</option><option>2AK</option>')

# Anleitung
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Lies zuerst das <b>Arbeitsblatt M1–M4</b> (Papier oder LMS) – ohne Handy, mit Textmarker.</li>
      <li>Dann die Fragen in die <b>gelben Felder</b> eintragen – alles wird am Handy automatisch gespeichert.</li>
      <li><b>Stunde 1</b>: Aufgaben 1–6 · <b>Für Schnelle</b>: 7–10, nur wenn Zeit bleibt.</li>
      <li>Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Ganz unten <b>PDF erstellen</b> und die PDF in LMS hochladen. Deine Frage aus Aufgabe 6 besprechen wir in der nächsten Stunde.</li>
    </ol>""" + s[j:]

# Fahrplan + Material
i = s.index('<section class="fahrplan">'); j = s.index("</section>", i) + 10
s = s[:i] + """<section class="fahrplan"><div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2><p>Lies <strong>M1–M4</strong> auf dem Arbeitsblatt, beantworte die <strong>Aufgaben 1–6</strong> und gib das <strong>PDF</strong> ab. In der nächsten Stunde besprechen und diskutieren wir alles – ohne Handy.</p><div class="tablewrap"><table><thead><tr><th>Stunde</th><th>Lesen</th><th>Aufgaben</th><th>Methode</th><th>Abgabe</th></tr></thead><tbody><tr><td>Stunde 1</td><td>M1 + M2 → M3 → M4 (Papier)</td><td>1–4, dann 5 + 6</td><td>lesen ohne Handy, dann am Handy</td><td>PDF in LMS</td></tr><tr><td>Stunde 2</td><td>–</td><td>Besprechung 1–5 · eure Fragen · Aktuelles</td><td>ohne Handy: Vier-Ecken-Quiz, Aufstellen, Diskussion</td><td>–</td></tr><tr><td>Für Schnelle</td><td>M2 Z. 34–47 · Internet</td><td>7–10</td><td>am Handy</td><td>freiwillig</td></tr></tbody></table></div></section>
  <section class="card" id="material"><div class="head"><span class="nr">Dein Material</span><span class="pill theory">Buch S. 47–52</span></div>
    <h2>Arbeitsblatt »70 Jahre Allgemeine Erklärung der Menschenrechte«</h2>
    <p class="q">Auf Papier oder in LMS (Schroedel aktuell, November 2018).</p>
    <ul class="steps"><li><b>M1</b> Zeitleiste: Die Entwicklung der Menschenrechte – ein langer Weg</li><li><b>M2</b> Text: Die AEMR – ein Meilenstein (Zeile 1–47)</li><li><b>M3</b> Text: Menschenrechte – die weiche Macht</li><li><b>M4</b> Kommentar: Stolz und Schande</li></ul>
    <p class="hint">Tipp: Lies einen Text, dann beantworte die passende Aufgabe – M1 → Aufgabe 1, M2 → 2, M3 → 3, M4 → 4.</p>
  </section>""" + s[j:]

rep("0 von 20 bearbeitet", "0 von %d bearbeitet" % len(T))
rep('<p class="hint"><a href="theorie.html">Zurück zur Lernseite</a> · <a href="quiz.html">Zum Quiz</a></p>',
    '<p class="hint"><a href="#material">Zum Material</a> · <a href="../">Zur Klassenübersicht</a></p>')
rep("Stand 15.10.2026", "Stand " + STAND)

# Daten
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = s[:i] + 'const KEY = "26-27-2AK-K1-AEMR-UE-Handy-v1";\nconst KAP = "K1", THEMA = "AEMR";\nconst T = ' + json.dumps(T, ensure_ascii=False, indent=1) + ";" + s[j:]

# Auswahl mischen (richtige Antwort steht in den Daten an 1. Stelle) – gleiche Liste = gleiche Reihenfolge auf der Seite
rep("function fieldsFor(t) {", """const MIX = {};
function mixed(opts) {
  const k = JSON.stringify(opts);
  if (!MIX[k]) { const a = opts.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } MIX[k] = a; }
  return MIX[k];
}
function fieldsFor(t) {""")
rep("f[2] ? selectField(t.id, f[0], f[2], f[1]) : textField(t.id, f[0], f[1], true, 3)", "f[2] ? selectField(t.id, f[0], f[3] === false ? f[2] : mixed(f[2]), f[1]) : textField(t.id, f[0], f[1], !(t.chk && t.chk[f[0]] && t.chk[f[0]].num !== undefined), 3)")

rep('KAP + " Elektromagnet und Elektromotor – Aufgaben"', 'KAP + " Menschenrechte – 70 Jahre AEMR – Aufgaben"')
rep('clean("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor · Schulbuch S. 29–33, 38")', 'clean("PBGW · 2AK · K1 Menschenrechte · Arbeitsblatt »70 Jahre AEMR« · Schulbuch S. 47–52")')
rep('d.text("Elektromagnet-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Teil 1 und 2): Aufgabe "', '"Noch offen (Stunde 1): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–9 bearbeitet."', '"Alle Aufgaben 1–6 bearbeitet."')
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + 'const GRP = { 1: "Stunde 1 · Lesen und beantworten", 0: "Für Schnelle und Neugierige · optional" };' + s[j:]

_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
assert not re.search("Elektromagnet|4AB|K1\\.5", _plain), re.findall(".{60}(?:Elektromagnet|4AB|K1\\.5).{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)
print("ok", len(s))
