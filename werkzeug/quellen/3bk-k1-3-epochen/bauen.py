"""Handy-Seiten PBGW 3BK · K1.3–1.4 Epochen bauen (Lernseite, Arbeitsblatt, Quiz).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3bk-k1-3-epochen/bauen.py
Arbeitsblatt-Grundlage: 4ab-nawi/k1-5a-elektromagnet/aufgaben.html (Sofort-Feedback, Lösungen nach Abgabe, PDF).
Danach: python3 werkzeug/pdf_hilfe_einbauen.py und python3 werkzeug/build_index.py"""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
import theorie_daten as TD
STAND = I.STAND

UNIT = I.ORDNER + "/"
DST = os.path.join(ROOT, UNIT)
os.makedirs(DST, exist_ok=True)
esc = html.escape
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
CAMO, LOGO, SMILEY = b64(WZ + "/camo.png"), b64(WZ + "/logo.png"), b64(WZ + "/smiley.png")
nb = lambda s: re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
md = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(nb(s)))


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


FAHRPLAN_ROWS = [["Stunde 1", "Einstieg + Teil 1 · Wie zählen wir Zeit?", "1–5", "ohne Handy: Zeitmaschinen-Rätsel und Rechen-Challenge (Mini-Whiteboard), dann am Handy", "–"],
                 ["Stunde 2", "Teil 2 · Die Epochen", "6–10 · Quiz", "ohne Handy: lebender Zeitstrahl, dann am Handy", "PDF in LMS"],
                 ["Für Schnelle", "Für Schnelle und Neugierige", "11–15", "am Handy", "freiwillig"]]
FAHRPLAN = ('<section class="fahrplan"><div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2>'
            '<p>Lies die <strong>Lernseite</strong> Teil für Teil, mach die passenden <strong>Aufgaben</strong> im Arbeitsblatt, teste dich mit dem <strong>Quiz</strong> '
            'und gib nach Stunde 2 das <strong>PDF</strong> ab.</p><div class="tablewrap"><table><thead><tr><th>Stunde</th><th>Lesen</th><th>Aufgaben</th><th>Methode</th><th>Abgabe</th></tr></thead><tbody>'
            + "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in FAHRPLAN_ROWS) + "</tbody></table></div></section>")

# ================================================================ Arbeitsblatt
s = open(os.path.join(ROOT, "4ab-nawi/k1-5a-elektromagnet/aufgaben.html"), encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (old[:80], n); s = s.replace(old, new)


TITLE = "Epochen-Aufgaben"
rep("<title>Elektromagnet-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Elektromagnet-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Elektromagnet-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>4AK</option><option>4BK</option>', '<option value="">–</option><option>3BK</option>')
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Lies zuerst den passenden Teil der <a href="theorie.html">Lernseite</a>, dann die Aufgaben in die <b>gelben Felder</b> – alles wird am Handy gespeichert.</li>
      <li><b>Stunde 1</b>: 1–5 · <b>Stunde 2</b>: 6–10 · <b>Für Schnelle</b>: 11–15.</li>
      <li>Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Nach Stunde 2 ganz unten <b>PDF erstellen</b> und in LMS hochladen.</li>
    </ol>""" + s[j:]
i = s.index('<section class="fahrplan">'); j = s.index("</section>", i) + 10
s = s[:i] + FAHRPLAN + s[j:]
rep("0 von 20 bearbeitet", "0 von %d bearbeitet" % len(I.T))
rep('<p class="hint"><a href="theorie.html">Zurück zur Lernseite</a> · <a href="quiz.html">Zum Quiz</a></p>',
    '<p class="hint"><a href="theorie.html">Zur Lernseite</a> · <a href="quiz.html">Zum Quiz</a> · <a href="../">Klassenübersicht</a></p>')
rep("Stand 15.10.2026", "Stand " + STAND + " · " + I.V)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = s[:i] + 'const KEY = "%s";\nconst KAP = "K1.3", THEMA = "Epochen";\nconst T = ' % I.KEY + json.dumps(I.T, ensure_ascii=False, indent=1) + ";" + s[j:]
rep("function fieldsFor(t) {", """const MIX = {};
function mixed(opts) {
  const k = JSON.stringify(opts);
  if (!MIX[k]) { const a = opts.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } MIX[k] = a; }
  return MIX[k];
}
function fieldsFor(t) {""")
rep("f[2] ? selectField(t.id, f[0], f[2], f[1]) : textField(t.id, f[0], f[1], true, 3)",
    "f[2] ? selectField(t.id, f[0], f[3] === false ? f[2] : mixed(f[2]), f[1]) : textField(t.id, f[0], f[1], !(t.chk && t.chk[f[0]] && t.chk[f[0]].num !== undefined), 3)")
rep('KAP + " Elektromagnet und Elektromotor – Aufgaben"', 'KAP + " Zeit-Einteilung und Epochen – Aufgaben"')
rep('clean("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor · Schulbuch S. 29–33, 38")', 'clean("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen · Schulbuch S. 13–14")')
rep('d.text("Elektromagnet-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Teil 1 und 2): Aufgabe "', '"Noch offen (Stunde 1 und 2): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–9 bearbeitet."', '"Alle Pflicht-Aufgaben 1–10 bearbeitet."')
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
assert not re.search(r"Elektromagnet|4AB|K1\.5", _plain), re.findall(r".{60}(?:Elektromagnet|4AB|K1\.5).{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Epochen-Check – Quiz</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Epochen-Check</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Epochen-Check am Handy</h2>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Epochen-Check"')
qv = qv.replace('Frage 1 von 16', 'Frage 1 von %d' % len(I.QUIZ))
a, b = qv.index("const Q = ["), qv.index("];", qv.index("const Q = [")) + 2
qv = qv[:a] + "const Q = [\n" + qs + "\n];" + qv[b:]
qv = qv.replace("if (p >= 13) return", "if (p >= %d) return" % (len(I.QUIZ) - 3)).replace("if (p >= 9) return", "if (p >= %d) return" % (len(I.QUIZ) // 2 + 2))
if "[hidden]" not in qv: qv = qv.replace("<style>", "<style>\n[hidden] { display: none !important; }", 1)
for k, v_ in {"__CAMO__": CAMO, "__LOGO__": LOGO, "__SMILEY__": SMILEY, "__QR__": qr_b64(I.URL + "quiz.html")}.items(): qv = qv.replace(k, v_)
assert not re.search(r"__[A-Z]+__", qv) and "Bindung" not in qv


def wrap(src):
    te = src.index("</title>") + 8; rest = src[te:]; bs = rest.index("<header")
    return ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="robots" content="noindex">\n' + src[:te] + "\n" + rest[:bs] + "</head>\n<body>\n" + rest[bs:] + "\n</body>\n</html>\n")


open(DST + "quiz.html", "w", encoding="utf-8").write(wrap(qv) if not qv.lstrip().startswith("<!doctype") else qv)

# ================================================================ Lernseite
def slide(title, body, pill=None, sid=None):
    head = f'<div class="slidehead"><h3>{esc(title)}</h3>' + (f'<span class="pill">{esc(pill)}</span>' if pill else "") + "</div>"
    return f'<article class="slide"{" id=" + chr(34) + sid + chr(34) if sid else ""}>{head}{body}</article>'


def tiles(items):
    return '<div class="tiles">' + "".join(f'<div class="tile"><h4>{esc(h)}</h4>{"".join("<p>" + md(x) + "</p>" for x in (b if isinstance(b, list) else [b]) if x)}</div>' for h, b in items) + "</div>"


def table(rows):
    h = "".join(f"<th>{esc(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join((f"<th scope=row>{md(c)}</th>" if k == 0 else f"<td>{md(c)}</td>") for k, c in enumerate(r)) + "</tr>" for r in rows[1:])
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


ul = lambda xs: '<ul class="pts">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ul>"
ol = lambda xs: '<ol class="goals">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ol>"
merke = lambda x: f'<div class="merke">{md(x)}</div>'
hint = lambda x: f'<p class="hint">{md(x)}</p>'
stat = lambda z, t: f'<div class="stat"><b>{esc(z)}</b><span>{md(t)}</span></div>'
reveal = lambda q, a: f'<div class="stopq"><p><strong>{md(q)}</strong></p><details class="reveal"><summary>Erst überlegen – dann Lösung anzeigen</summary><p>{md(a)}</p></details></div>'
jetzt = lambda txt, href: f'<a class="jetzt" href="{href}">{esc(txt)} →</a>'


def video(key):
    t, q, d, u = I.VIDEOS[key]
    return (f'<div class="video"><div><strong>Video: {esc(t)}</strong><br><span class="hint">{esc(q)} · {esc(d)} · Ton an oder Kopfhörer</span></div>'
            f'<a class="btn small" href="{u}" target="_blank" rel="noopener">Video ansehen ({esc(d)})</a></div>')


def zeitstrahl():
    seg = "".join(f'<div class="zs-seg" style="flex:{w};background:#{c}"><b>{esc(n)}</b><span>{esc(z)}</span></div>' for n, z, w, c in TD.ZEITSTRAHL)
    wen = "".join(f'<li><b>{esc(j)}</b> {esc(e)}</li>' for j, e in TD.WENDE)
    return f'<div class="zs"><div class="zs-bar">{seg}</div><div class="zs-arrow">→ heute</div></div><p class="hint"><strong>Wendepunkte:</strong></p><ul class="pts zs-w">{wen}</ul>'


def block(b):
    k = b[0]
    if k == "zeitstrahl": return zeitstrahl()
    if k == "tiles": return tiles(b[1])
    if k == "ul": return ul(b[1])
    if k == "ol": return ol(b[1])
    if k == "merke": return merke(b[1])
    if k == "hint": return hint(b[1])
    if k == "table": return table(b[1])
    if k == "video": return video(b[1])
    if k == "reveal": return "".join(reveal(q, a) for q, a in b[1])
    raise ValueError(k)


def render(item):
    if isinstance(item, tuple) and item[0] == "jetzt": return jetzt(item[1], item[2])
    return slide(item["title"], "".join(block(b) for b in item["blocks"]), item["pill"], item["id"])


PARTS = [(pid, eyebrow, title, [render(x) for x in items]) for pid, eyebrow, title, items in TD.PARTS]
PARTS.append(("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]))
CHECK = "".join(f'<div class="ziel"><p>{md(z)}</p><div class="chips" role="group" aria-label="Selbstcheck">' + "".join(f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht")) + "</div></div>" for k, z in enumerate(I.LERNZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                       slide("Kann ich das?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [render(x) for x in TD.SCHNELLE]))

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1 · Zeit", "teil2": "Teil 2 · Epochen", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}
toc = "".join(f'<a href="#{p[0]}">{TOCLAB[p[0]]}</a>' for p in PARTS) + '<a href="#weiter">Aufgaben</a>'
body = "".join(f'<section class="part" id="{p[0]}"><div class="band"><div class="eyebrow">{esc(p[1])}</div><h2>{esc(p[2])}</h2></div>{"".join(p[3])}</section>' for p in PARTS)
bt = open(os.path.join(WZ, "vorlagen", "build_theorie.py"), encoding="utf-8").read()
tcss = bt[bt.index("<style>"):bt.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
tcss = tcss.replace("</style>", """.merke { background: var(--olive); color: #fff; border-radius: 12px; padding: 12px 14px; }
.merke strong { color: #C9D8A8; }
ol.goals, ul.pts { margin: 0; padding-left: 24px; display: grid; gap: 6px; }
details.reveal { border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
details.reveal summary { cursor: pointer; font-weight: 700; color: #D9772B; }
details.reveal p { margin: 8px 0 0; }
.stat { background: #2E7D8C; color: #fff; border-radius: 12px; padding: 12px 14px; display: grid; gap: 4px; }
.stat b { font-family: Cambria, "Source Serif 4", Georgia, serif; font-size: 28px; }
.stat strong { color: #fff; }
.stopq { display: grid; gap: 6px; }
.stopq + .stopq { margin-top: 10px; }
.ziel { border: 1px solid #D3DCC2; border-radius: 12px; padding: 10px 12px; display: grid; gap: 6px; }
.ziel p { margin: 0; }
.chips { display: flex; gap: 8px; flex-wrap: wrap; }
.chip { font: inherit; font-size: 16px; font-weight: 700; color: #3B4A2F; background: #fff; border: 2px solid #D3DCC2; border-radius: 999px; padding: 6px 14px; cursor: pointer; }
.chip[aria-pressed="true"][data-v="sicher"] { background: #E6F0D3; border-color: #7FA83A; }
.chip[aria-pressed="true"][data-v="fast"] { background: #FFF1D6; border-color: #D9772B; }
.chip[aria-pressed="true"][data-v="noch nicht"] { background: #F6E3DF; border-color: #8C3B2E; }
.chip:focus-visible { outline: 3px solid #2E7D8C; outline-offset: 2px; }
.jetzt { display: block; text-align: center; background: #7FA83A; color: #fff; font-weight: 700; font-size: 18px; text-decoration: none; border-radius: 12px; padding: 12px 16px; }
.fahrplan { background: #fff; border: 2px solid #7FA83A; border-radius: 16px; padding: 14px 16px; min-width: 0; }
.fahrplan h2 { font-family: Cambria, "Source Serif 4", Georgia, serif; color: #3B4A2F; margin: 2px 0 6px; } .fahrplan p { margin: 0 0 8px; }
.fahrplan table { width: 100%; border-collapse: collapse; font-size: 15px; } .fahrplan th, .fahrplan td { border-bottom: 1px solid #D3DCC2; padding: 5px 6px; text-align: left; vertical-align: top; }
.fahrplan .tablewrap { overflow-x: auto; max-width: 100%; }
.slide[id], .part { scroll-margin-top: 56px; }
.zs { display: grid; gap: 4px; }
.zs-bar { display: flex; gap: 3px; border-radius: 12px; overflow: hidden; }
.zs-seg { color: #fff; padding: 10px 6px; display: grid; gap: 2px; align-content: start; min-width: 0; hyphens: manual; }
.zs-seg b { font-size: 15px; line-height: 1.15; overflow-wrap: anywhere; } .zs-seg span { font-size: 13px; line-height: 1.2; }
.zs-arrow { text-align: right; font-weight: 700; color: #3B4A2F; font-size: 14px; }
@media (max-width: 520px) { .zs-bar { flex-direction: column; } .zs-seg { flex: none !important; grid-template-columns: 1fr auto; align-items: baseline; } }
.video { display: flex; gap: 12px; align-items: center; justify-content: space-between; flex-wrap: wrap; background: #FFF4EA; border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
.video .btn { background: #D9772B; color: #fff; text-decoration: none; font-weight: 700; border-radius: 10px; padding: 8px 14px; }
</style>""")
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Epochen – Lernseite</title>
<link rel="stylesheet" href="../../schriften/schriften.css">
{tcss}
</head>
<body>
<header class="top">
  <img class="camo" alt="" src="data:image/png;base64,{CAMO}">
  <img class="logo" alt="BHAK Wappen" src="data:image/png;base64,{LOGO}">
  <div class="top-inner">
    <div class="top-text"><div class="eyebrow">{esc(I.EYEBROW)} · {esc(I.BUCH)}</div><h1>{esc(I.TITEL)}</h1></div>
    <img class="smiley" alt="" src="data:image/png;base64,{SMILEY}">
  </div>
</header>
<nav class="toc" aria-label="Inhalt"><div>{toc}</div></nav>
<main>
{FAHRPLAN}
{body}
<section class="next" id="weiter">
  <div class="eyebrow">Weiter geht's</div>
  <h2>Jetzt bist du dran</h2>
  <div class="btns"><a class="btn" href="aufgaben.html">2 · Arbeitsblatt A1–A{len(I.T)}</a><a class="btn alt" href="quiz.html">3 · Epochen-Check (Quiz)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch PBGW 3 (Trauner) S. 13–14 (Zeit-Einteilung, Epochengliederung). Kalenderdaten Stand Oktober 2026. <a href="../">Klassenübersicht 3BK</a></p>
  <p class="hint">Stand {STAND} · {I.V}</p>
</section>
</main>
<script>
(function () {{
  var KEY = "{I.KEY}-Lernseite-Check", S = {{}};
  try {{ S = JSON.parse(localStorage.getItem(KEY) || "{{}}") || {{}}; }} catch (e) {{ S = {{}}; }}
  var chips = document.querySelectorAll(".chip[data-z]");
  function paint() {{ chips.forEach(function (c) {{ c.setAttribute("aria-pressed", String(S[c.dataset.z] === c.dataset.v)); }}); }}
  chips.forEach(function (c) {{ c.addEventListener("click", function () {{
    S[c.dataset.z] = S[c.dataset.z] === c.dataset.v ? null : c.dataset.v; paint();
    try {{ localStorage.setItem(KEY, JSON.stringify(S)); }} catch (e) {{}}
  }}); }});
  paint();
}})();
</script>
</body>
</html>
"""
open(DST + "theorie.html", "w", encoding="utf-8").write(page)
for f in ["theorie.html", "aufgaben.html", "quiz.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
