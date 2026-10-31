"""Handy-Seiten NAWI 2AB · K1.3 Stoffumwandlung bauen (Theorie-Seite, Arbeitsblatt, Versuchsseite, Quiz).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-3-reaktionen/skizzen.py  und danach  python3 werkzeug/quellen/2ab-k1-3-reaktionen/bauen.py
Arbeitsblatt-Grundlage: 3bk-pbgw/k1-3-epochen/aufgaben.html (Sofort-Feedback, gemischte Auswahl, Lösungen nach Abgabe, PDF).
Versuchsseite-Grundlage: 2ab-nawi/k1-2-bindungen/versuche.html (gleicher Aufbau wie die Bindungsarten-Versuche).
Danach: python3 werkzeug/nach_dem_bauen.py"""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
import theorie_daten as TD
import versuche_daten as VD
STAND = I.STAND

UNIT = I.ORDNER + "/"
DST = os.path.join(ROOT, UNIT)
os.makedirs(DST, exist_ok=True)
esc = html.escape
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
CAMO, LOGO, SMILEY = b64(WZ + "/camo.png"), b64(WZ + "/logo.png"), b64(WZ + "/smiley.png")
nb = lambda s: re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
md = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(nb(s)))


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


s = ""


def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (old[:90], n); s = s.replace(old, new)


# ================================================================ Arbeitsblatt
s = open(os.path.join(ROOT, "3bk-pbgw/k1-3-epochen/aufgaben.html"), encoding="utf-8").read()
TITLE = "Stoffumwandlung-Aufgaben"
rep("<title>Epochen-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Epochen-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Epochen-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>3BK</option>', '<option value="">–</option><option>2A</option><option>2B</option>')
def _ber(nrs):
    out, a = [], None
    for k, n in enumerate(nrs):
        if a is None: a = n
        if k + 1 == len(nrs) or nrs[k + 1] != n + 1: out.append(str(a) if a == n else "%d–%d" % (a, n)); a = None
    return ", ".join(out)
_ST = {1: "Stunde 1", 2: "Stunde 2", 3: "Stunde 3–4", 4: "Stunde 4"}
_ZU = {3: " (während die anderen Gruppen an den Stationen sind)"}
INTRO = ("      <li><b>Pflicht</b> – " + " · ".join("<b>%s</b>: %s%s" % (_ST[h], _ber([t["nr"] for t in I.T if t["h"] == h and t["tag"] != "Zusatz"]), _ZU.get(h, "")) for h in range(1, 5)) + ".</li>\n"
         "      <li><b>Zusatz in der Stunde</b>, wenn du früher fertig bist: " + _ber([t["nr"] for t in I.T if t["h"] and t["tag"] == "Zusatz"]) +
         " · <b>Für Schnelle</b>: " + _ber([t["nr"] for t in I.T if not t["h"]]) + ". Es gibt <b>keine Hausübung</b>.</li>")
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Lies zuerst den passenden Teil der <a href="theorie.html">Theorie-Seite</a>, dann die Aufgaben in die <b>gelben Felder</b> – alles wird am Handy gespeichert.</li>
      """ + INTRO + """
      <li>Bei jeder Aufgabe steht, wie lange sie ungefähr dauert. Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Nach Stunde 4 (Do 12.11.) ganz unten <b>PDF erstellen</b> und in LMS hochladen. Die Zeitangaben sind Richtwerte – Lesen und Versuche dauern oft länger, dafür gehen Aufgaben meist schneller.</li>
    </ol>""" + s[j:]
i = s.index("<!--FAHRPLAN-->"); j = s.index("<!--/FAHRPLAN-->") + len("<!--/FAHRPLAN-->")
s = s[:i] + "<!--FAHRPLAN--><!--/FAHRPLAN-->" + s[j:]  # wird von build_index.py aus einheiten.json gefüllt
rep("0 von 15 bearbeitet", "0 von %d bearbeitet" % len(I.T))
s = re.sub(r'<p class="hint">Stand [0-9.]+ · v\d+</p>', '<p class="hint">Stand ' + STAND + " · " + I.V + "</p>", s, count=1)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = s.replace('if (t.type === "multi") return t.fields.every(f => filled(a[f[0]]));', 'if (t.type === "multi") return t.fields.every(f => (t.opt || []).includes(f[0]) || filled(a[f[0]]));')
s = s.replace('if (t.type === "sketch") return !!a.foto && t.fields.every(f => filled(a[f[0]]));', 'if (t.type === "sketch") return !!a.foto && t.fields.every(f => (t.opt || []).includes(f[0]) || filled(a[f[0]]));')
s = s.replace('const parts = Object.entries(t.chk).map(([k, c]) =>', '/* freiwillige Felder (t.opt) zählen nur, wenn ausgefüllt */\n  const parts = Object.entries(t.chk).filter(([k]) => !((t.opt || []).includes(k) && !(a[k] != null && String(a[k]).trim() !== ""))).map(([k, c]) =>')
assert "(t.opt || [])" in s
# ---- K1.3 v4: offene Erklärungen (c.man) bewertet die Lehrkraft (ChatGPT-Bericht v5, N02/N03) ----
rep("  return { ok: parts.every(p => p.ok), parts };\n}", """  /* K1.3: offene Erklärungen (c.man) zeigen nur eine Schreibhilfe; »richtig« bezieht sich nur auf die automatisch prüfbaren Teile */
  parts.forEach(p => { if ((t.chk[p.key] || {}).man) p.man = true; });
  const auto = parts.filter(p => !p.man), man = parts.filter(p => p.man);
  if (!auto.length && man.length) return { ok: man.every(p => p.filled), parts, man: true, manOnly: true };
  return { ok: auto.every(p => p.ok), parts, man: man.length > 0 };
}""")
_i = s.index("function showCheck(t) {"); _j = s.index("\nfunction showSolutions()", _i)
s = s[:_i] + """function showCheck(t) {
  const r = evalTask(t), fb = $("#fb_" + t.id); fb.hidden = false; fb.textContent = "";
  const auto = r.parts.filter(p => !p.man), man = r.parts.filter(p => p.man), autoOk = auto.every(p => p.ok), viele = r.parts.length > 1;
  fb.className = "fb " + (r.man ? (autoOk ? "info" : "no") : (r.ok ? "ok" : "no"));
  fb.append(el("strong", { text: r.man ? (autoOk ? (auto.length ? "Die automatisch prüfbaren Teile stimmen." : "Gespeichert.") : "Noch nicht ganz.") : (r.ok ? "Richtig!" : "Noch nicht ganz.") }));
  if (!autoOk) auto.forEach(p => {
    if (p.kind === "strike") fb.append(el("div", { text: p.n + " von " + p.of + " richtig durchgestrichen." }));
    else if (p.kind === "kw" && !p.ok) fb.append(el("div", { text: (viele ? p.label + ": " : "") + "enthalten: " + p.hits.map(h => h[0] + (h[1] ? " ✓" : " ✗")).join(", ") }));
    else if (!p.ok) fb.append(el("div", { text: (viele ? p.label + ": " : "") + (p.kind === "sel" ? (p.filled ? "Auswahl stimmt noch nicht." : "Noch nichts ausgewählt.") : p.msg) }));
  });
  man.forEach(p => {
    const pre = viele ? p.label + ": " : "";
    if (!p.filled) { fb.append(el("div", { text: pre + "Deine Erklärung fehlt noch." })); return; }
    const da = p.hits.filter(h => h[1]).map(h => h[0]), fehlt = p.hits.filter(h => !h[1]).map(h => h[0]);
    fb.append(el("div", { text: pre + "Schreibhilfe – " + (da.length ? "gefunden: " + da.join(", ") : "noch keines der erwarteten Stichwörter") + (fehlt.length ? " · vielleicht fehlt noch: " + fehlt.join(", ") + " (eine richtige Umschreibung zählt auch)" : "") + "." }));
  });
  if (man.length) fb.append(el("div", { text: "Ob deine Erklärung fachlich stimmt, bewertet die Lehrkraft. Lies sie noch einmal durch." }));
  if (t.tip && (!r.ok || man.some(p => p.filled && p.hits.some(h => !h[1])))) fb.append(el("div", {}, "Tipp: Lies nochmal ", el("a", { href: t.tip[1], text: t.tip[0] }), "."));
}""" + s[_j:]
rep('    let st = "selbst bewerten";\n    if (ev) {', '    let st = "selbst bewerten";\n    if (ev && ev.man) { const au = ev.parts.filter(p => !p.man); st = (au.length ? "automatisch geprüft: " + (au.every(p => p.ok) ? "richtig" : "noch nicht richtig") + " · " : "") + "Erklärung: bewertet die Lehrkraft"; }\n    else if (ev) {')
rep("(ev && ev.ok ? [70, 110, 40] : muted)", "(ev && ev.ok && !ev.man ? [70, 110, 40] : muted)")
s = s[:i] + 'const KEY = "%s";\nconst KAP = "K1.3", THEMA = "Stoffumwandlung";\nvar PL_ZUSATZ_ENDE = true;   /* Zusatzaufgaben 4, 8, 12, 15 bleiben in ihrer Stunde, nur 19–23 werden zugeklappt */\nconst T = ' % I.KEY + json.dumps(I.T, ensure_ascii=False, indent=1) + ";" + s[j:]
rep(".fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }", ".fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }\n.fb.info { background: #E8F1F3; border: 2px solid #2E7D8C; }")
rep('KAP + " Zeit-Einteilung und Epochen – Aufgaben"', 'KAP + " Stoffumwandlung – Aufgaben"')
rep('clean("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen · Schulbuch S. 13–14")', 'clean("NAWI · 2AB · K1.3 Stoffumwandlung · Schulbuch S. 29–37, 98")')
rep('d.text("Epochen-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Stunde 1 und 2): Aufgabe "', '"Noch offen (Pflicht): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–10 bearbeitet."', '"Alle Pflicht-Aufgaben bearbeitet."')
# Zeit je Aufgabe und rote Kennzeichnung »Versuch im Buch«
rep('el("span", { class: tagCls, text: t.tag })),', 'el("span", { class: tagCls, text: t.tag }), t.zeit ? el("span", { class: "tag zeit", text: "ca. " + t.zeit + " min" }) : null),')
rep('el("span", { class: "pill" + (t.own ? " theory" : ""), text: t.src })', 'el("span", { class: "pill" + (t.src.startsWith("Versuch im Buch") ? " versuch" : (t.own ? " theory" : "")), text: t.src })')
rep(".pill.theory { background: var(--theory); }", ".pill.theory { background: var(--theory); } .pill.versuch { background: #A33A2B; } .tag.zeit { color: var(--teal); border-color: var(--teal); }")
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]
s = s.replace("26-27-3BK-K1.3-Epochen-TH-Handy-v1", I.KEY)  # Bausteine (pdferinnerung) mit altem Schlüssel
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Epochen", "Zeit-Einteilung"]:
    assert bad not in _plain, re.findall(r".{60}" + bad + r".{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Reaktions-Check – Quiz</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Reaktions-Check</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Reaktions-Check am Handy</h2>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Reaktions-Check"')
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

# ================================================================ Theorie-Seite
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
reveal = lambda q, a: f'<div class="stopq"><p><strong>{md(q)}</strong></p><details class="reveal"><summary>Erst überlegen – dann Lösung anzeigen</summary><p>{md(a)}</p></details></div>'
jetzt = lambda txt, href: f'<a class="jetzt" href="{href}">{esc(txt)} →</a>'
VS_BY_NR = {v["nr"]: v for v in VD.VS}


def video(key):
    t, q, d, u = I.VIDEOS[key]
    lab = f"Video ansehen ({d})" if d != "kurz" else "Video ansehen"
    return (f'<div class="video"><div><strong>Video: {esc(t)}</strong><br><span class="hint">{esc(q)}{" · " + esc(d) if d != "kurz" else ""} · Ton an oder Kopfhörer</span></div>'
            f'<a class="btn small" href="{u}" target="_blank" rel="noopener">{lab}</a></div>')


def figure(src, alt, cap):
    return f'<figure class="fig"><img src="{src}" alt="{esc(alt)}" loading="lazy"><figcaption>{md(cap)}</figcaption></figure>'


def versuch(nr, titel, text):
    v = VS_BY_NR[nr]
    return (f'<div class="vbox"><div class="vhead"><span class="vnr">{esc(nr)}</span><span class="vtag">{"KERN" if v["kern"] else "ZUSATZ"}</span></div>'
            f'<p><strong>{esc(titel)}</strong></p><p>{md(text)}</p><a class="btn small" href="versuche.html#card_{v["id"]}">Zum Versuchsprotokoll</a></div>')


def karten(items):
    return '<div class="karten">' + "".join(f'<details class="karte"><summary><span class="knr">{k + 1}</span> {md(q)}</summary><p>{md(a)}</p></details>' for k, (q, a) in enumerate(items)) + "</div>"


def block(b):
    k = b[0]
    if k == "tiles": return tiles(b[1])
    if k == "ul": return ul(b[1])
    if k == "ol": return ol(b[1])
    if k == "merke": return merke(b[1])
    if k == "hint": return hint(b[1])
    if k == "table": return table(b[1])
    if k == "video": return video(b[1])
    if k == "reveal": return "".join(reveal(q, a) for q, a in b[1])
    if k == "img": return figure(b[1], b[2], b[3])
    if k == "versuch": return versuch(b[1], b[2], b[3])
    if k == "karten": return karten(b[1])
    raise ValueError(k)


def render(item):
    if isinstance(item, tuple) and item[0] == "jetzt": return jetzt(item[1], item[2])
    return slide(item["title"], "".join(block(b) for b in item["blocks"]), item["pill"], item["id"])


PARTS = [(pid, eyebrow, title, [render(x) for x in items]) for pid, eyebrow, title, items in TD.PARTS]
LZ = slide("Das kannst du nach dieser Einheit", ol(I.LERNZIELE), I.BUCH, "ziele")
PARTS[0] = (PARTS[0][0], PARTS[0][1], PARTS[0][2], PARTS[0][3] + [LZ])
PARTS.append(("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]))
CHECK = "".join(f'<div class="ziel"><p>{md(z)}</p><div class="chips" role="group" aria-label="Selbstcheck">' + "".join(f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht")) + "</div></div>" for k, z in enumerate(I.LERNZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                       slide("Kann ich das?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [render(x) for x in TD.SCHNELLE]))

toc = "".join(f'<a href="#{p[0]}">{TD.TOCLAB[p[0]]}</a>' for p in PARTS) + '<a href="#weiter">Aufgaben</a>'
body = "".join(f'<section class="part" id="{p[0]}"><div class="band"><div class="eyebrow">{esc(p[1])}</div><h2>{esc(p[2])}</h2></div>{"".join(p[3])}</section>' for p in PARTS)
bt = open(os.path.join(WZ, "vorlagen", "build_theorie.py"), encoding="utf-8").read()
tcss = bt[bt.index("<style>"):bt.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
tcss = tcss.replace("</style>", """.merke { background: var(--olive); color: #fff; border-radius: 12px; padding: 12px 14px; }
.merke strong { color: #C9D8A8; }
ol.goals, ul.pts { margin: 0; padding-left: 24px; display: grid; gap: 6px; }
details.reveal { border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
details.reveal summary { cursor: pointer; font-weight: 700; color: #D9772B; }
details.reveal p { margin: 8px 0 0; }
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
.slide[id], .part { scroll-margin-top: 56px; }
.video { display: flex; gap: 12px; align-items: center; justify-content: space-between; flex-wrap: wrap; background: #FFF4EA; border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
.video .btn { background: #D9772B; color: #fff; text-decoration: none; font-weight: 700; border-radius: 10px; padding: 8px 14px; }
.fig { margin: 0; display: grid; gap: 6px; justify-items: center; }
.fig img { max-width: 100%; height: auto; border-radius: 10px; border: 1px solid #D3DCC2; background: #fff; }
.fig figcaption { font-size: 15px; color: #5E6652; text-align: center; }
.vbox { border: 2px solid #A33A2B; border-radius: 12px; padding: 10px 14px; display: grid; gap: 6px; background: #FBF1EE; }
.vbox p { margin: 0; }
.vhead { display: flex; gap: 8px; align-items: center; }
.vnr { font-weight: 700; color: #fff; background: #A33A2B; border-radius: 8px; padding: 2px 10px; }
.vtag { font-size: 13px; font-weight: 700; color: #fff; background: #3B4A2F; border-radius: 999px; padding: 2px 10px; }
.vbox .btn { justify-self: start; background: #A33A2B; color: #fff; text-decoration: none; font-weight: 700; border-radius: 10px; padding: 8px 14px; }
.karten { display: grid; gap: 8px; }
.karte { border: 1px solid #D3DCC2; border-radius: 12px; padding: 10px 12px; background: #fff; }
.karte summary { cursor: pointer; font-weight: 700; color: #3B4A2F; }
.karte p { margin: 8px 0 0; color: #2E7D8C; font-weight: 700; }
.knr { display: inline-block; min-width: 26px; text-align: center; background: #2E7D8C; color: #fff; border-radius: 999px; font-size: 14px; margin-right: 4px; }
</style>""")
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Stoffumwandlung – Theorie</title>
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
{body}
<section class="next" id="weiter">
  <div class="eyebrow">Weiter geht's</div>
  <h2>Jetzt bist du dran</h2>
  <div class="btns"><a class="btn" href="aufgaben.html">2 · Arbeitsblatt A1–A{len(I.T)}</a><a class="btn alt" href="versuche.html">V · Versuche</a><a class="btn alt" href="quiz.html">3 · Reaktions-Check (Quiz)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch NAWI 2 (Trauner) S. 29–37 (Stoffumwandlung) und S. 98 (Korrosionsschutz). Alle Grafiken selbst gezeichnet. <a href="../">Klassenübersicht 2AB</a></p>
  <p class="hint">Stand {STAND} · {I.V}</p>
</section>
</main>
<script>
(function () {{
  var KEY = "26-27-2AB-K1.3-Reaktionen-Lernseite-Check-v1", S = {{}};
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

# ================================================================ Versuchsseite
s = open(os.path.join(ROOT, "2ab-nawi/k1-2-bindungen/versuche.html"), encoding="utf-8").read()
VDATA = []
for v in VD.VS:
    x = {k: v[k] for k in ("id", "nr", "titel", "bindung", "intro", "sicher", "entsorgung", "schritte", "skizze", "beob", "erk", "interp", "schluss", "buch", "kern")}
    if v.get("platz"): x["platz"], x["platz_kurz"] = v["platz"], v["platz_kurz"]
    x["mat"] = [[m[0], m[1]] for m in v["mat"]]
    if v.get("station"): x["station"] = v["station"]
    if v.get("demo"): x["demo"] = True
    VDATA.append(x)
i = s.index("const V = ") + len("const V = "); j = s.index("];\nconst KEY", i) + 1
s = s[:i] + json.dumps(VDATA, ensure_ascii=False) + s[j:]
rep('  if (v.sicher) body.append(', '  if (v.platz) body.append(el("div", { class: "hint", style: "margin:6px 0" }, el("b", { text: "Wo steht der Versuch? " }), v.platz));\n  if (v.sicher) body.append(')
rep('el("h2", { text: v.titel }), el("p", { class: "hint", text: v.bindung }));', 'el("h2", { text: v.titel }), el("p", { class: "hint", text: v.bindung + (v.platz_kurz ? " · Platz: " + v.platz_kurz : "") }));')
rep('const KEY = "26-27-2AB-K1.2-Bindungen-VS-Handy-v1";', 'const KEY = "26-27-2AB-K1.3-Reaktionen-VS-Handy-v1";')
s = s.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
rep("<h1>Bindungs-Versuche</h1>", "<h1>Reaktions-Versuche</h1>")
rep("<title>Bindungs-Versuche</title>", "<title>Reaktions-Versuche</title>")
rep('d.text("Bindungs-Versuche", M + 15, y + 11.5)', 'd.text("Reaktions-Versuche", M + 15, y + 11.5)')
s = s.replace('"K1.2 Die Bindungsarten – Versuchsprotokoll"', '"K1.3 Stoffumwandlung – Versuchsprotokoll"')
s = s.replace('clean("K1.2 Versuche · "', 'clean("K1.3 Versuche · "').replace('"K1.2-Versuche-" + slug(S.ich)', '"K1.3-Versuche-" + slug(S.ich)')
s = re.sub(r'(alt="QR-Code zur Versuchsseite" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "versuche.html"), s, count=1)
i = s.index("/*STATIONEN*/"); j = s.index("/*/STATIONEN*/")
s = s[:i] + """/*STATIONEN*/
[["Stunde 1 · Di 03.11. · Demo und Klassen-Ansatz – mittippen und eintragen", v => v.id === "eisenwolle" || v.id === "rost"],
 ["Stunde 2 · Do 05.11. · Demo nach dem Test", v => v.id === "kupferbrief"],
 ["Stunde 3 · Di 10.11. · Demo vor den Stationen – mittippen und eintragen", v => v.id === "kaelte"],
 ["Stunde 3–4 · Stationen 1 und 2 – drei Runden à 11 Minuten (Stunde 3: Gruppe 1–3, Stunde 4: Gruppe 4–6). An der Station: messen, beobachten, aufräumen, Erkenntnis eintragen", v => !!v.station],
 ["Stunde 4 · Do 12.11. · Demo Katalysator – mittippen und eintragen", v => v.id === "katalysator"],
  ["Zusatz – Gruppenversuch und Video, nur wenn Zeit bleibt (V8 nur nach Freigabe der Lehrkraft, V9 nur als Video)", v => !v.kern]].forEach(([t, fn]) => {
  $("#vs").append(el("div", { class: "grp", text: t }));
  V.filter(fn).forEach(v => $("#vs").append(versuch(v)));
});
""" + s[j:]
# Anzeige: KERN-Tag für Klassen-Ansatz/Gruppenversuch statt ZUSATZ
s = s.replace('text: v.station ? "KERN · Station " + v.station : (v.demo ? "KERN · Demo" : "ZUSATZ")', 'text: v.station ? "KERN · Station " + v.station : (v.demo ? "KERN · Demo" : (v.kern ? "KERN" : "ZUSATZ"))')
s = s.replace('(v.station ? "KERN · Station " + v.station + " · " : (v.demo ? "KERN · Lehrer-Demo · " : "ZUSATZ · "))', '(v.station ? "KERN · Station " + v.station + " · " : (v.demo ? "KERN · Demo · " : (v.kern ? "KERN · " : "ZUSATZ · ")))')
i = s.index('<section class="card safety">'); j = s.index("</section>", i) + 10
s = s[:i] + '<section class="card safety">\n    <h2>Sicherheit in dieser Einheit</h2>\n    <ul class="steps">\n' + "".join(
    f"      <li><b>{esc(a)}:</b> {esc(b)}</li>\n" for a, b in VD.SICHERHEIT) + "    </ul>\n  </section>" + s[j:]
s = s.replace('<li><b>Ein Protokoll-Handy pro Gruppe.</b>', '<li><b>Ein Protokoll-Handy pro Gruppe</b> – es liegt abseits vom Arbeitsplatz.</li><li style="display:none">', 1)
i = s.index("<!--PLAN-->"); j = s.index("<!--/PLAN-->") + len("<!--/PLAN-->")
s = s[:i] + """<!--PLAN--><section class="card" id="plan">
    <div class="head"><span class="nr">Ablauf</span><span class="pill theory">Versuche K1.3-V1 bis V9</span></div>
    <h2>So laufen die Versuche</h2>
    <ul class="steps">
      <li><b>Stunde 1 und 2:</b> Demos K1.3-V1 und V3 – erst tippen, dann zuschauen und hier eintragen. Rost-Ansatz K1.3-V2 heute ansetzen, Auswertung am Di 10.11.</li>
      <li><b>Stunde 3:</b> Zuerst Demo K1.3-V6 (Kältemischung) – erst tippen, dann zuschauen.</li>
      <li><b>Stunde 3–4: 6 Gruppen zu viert, 2 Stationen.</b> Stunde 3: Gruppe 1–3 an den Stationen, Gruppe 4–6 macht die Aufgaben 9–12. Stunde 4: umgekehrt. <b>Station 1 steht am Mobiltisch 1, Station 2 an einem Schülertisch (IKT-Tisch, nicht am Fenster)</b> (zum Ausspülen: Wasserleitung 1 bzw. 2); die Demos macht die Lehrkraft am Lehrertisch.</li>
      <li><b>Drei Runden à 11 Minuten:</b> Runde 1 – Gruppe 1 (bzw. 4) an Station 1, Gruppe 2 (bzw. 5) an Station 2, Gruppe 3 (bzw. 6) macht Aufgaben. Danach rückt jede Gruppe weiter: Station 1 → Station 2 → Aufgaben → Station 1.</li>
      <li><b>An der Station messen, beobachten und Fotos machen</b>, aufräumen, wie ihr sie vorgefunden habt, und gleich die <b>Erkenntnis</b> eintragen. <b>Interpretation und Schlussfolgerung</b> schreibt ihr, sobald ihr beide Stationen fertig habt – in eurer Aufgabenzeit – was fehlt, am Stundenende. Es gibt keine Hausübung.</li>
      <li><b>Stunde 4:</b> Demo K1.3-V7 (Zuckerwürfel mit Lithiumchlorid, Katalysator). <b>Zusatz:</b> Gruppenversuch K1.3-V8 (Brausetablette, nur nach Freigabe) und K1.3-V9 (nur als Video).</li>
    </ul>
    <p class="hint"><b>Abgabe:</b> Jeder gibt seine eigene Versuchs-PDF ab (Namen der Gruppe + dein Nachname) – in LMS nach Stunde 4 (Do 12.11.).</p>
  </section><!--/PLAN-->""" + s[j:]
s = re.sub(r"<!--STAND-->.*?<!--/STAND-->", '<!--STAND--><p class="hint" style="text-align:center;margin:18px 0 8px">NAWI · 2AB · K1.3 Versuche · Stand ' + STAND + " · " + I.V + "</p><!--/STAND-->", s, flags=re.S)
s = s.replace("26-27-2AB-K1.2-Bindungen-VS-Handy-v1", "26-27-2AB-K1.3-Reaktionen-VS-Handy-v1")
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Bindungsarten", "K1.2"]:
    assert bad not in _plain, re.findall(r".{60}" + re.escape(bad) + r".{30}", _plain)[:5]
# Fußzeile im Versuchs-PDF: lange Gruppennamen kürzen, damit »K1.3 Versuche · … · Seite x von y« auf die Seite passt (Test mit 4 langen Namen)
_alt = 'clean("K1.3 Versuche · " + (S.name || "") + " · Seite " + p + " von " + n)'
assert s.count(_alt) == 1, s.count(_alt)
s = s.replace(_alt, 'clean("K1.3 Versuche · " + ((S.name || "").length > 70 ? (S.name || "").slice(0, 67) + " …" : (S.name || "")) + " · Seite " + p + " von " + n)')
open(DST + "versuche.html", "w", encoding="utf-8").write(s)

for f in ["theorie.html", "aufgaben.html", "versuche.html", "quiz.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
