"""Handy-Seiten NAWI 1AB · K2.1 Mechanische Kräfte bauen (Theorie-Seite, Arbeitsblatt, Quiz, Versuchsseite).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k2-1-kraefte/skizzen.py  und danach  python3 werkzeug/quellen/1ab-k2-1-kraefte/bauen.py
Arbeitsblatt-Grundlage: eingefrorene Kopie vorlage_aufgaben.html (= Stand der K1.4-Vorlage vom 30.10.2026).
Versuchsseite-Grundlage: eingefrorene Kopie vorlage_versuche.html.
NEU in dieser Einheit (Probe nach den Standards vom 07.11.2026, nur hier – kein globaler Umbau):
  · Lernpfad »Aufgabe zuerst«: Arbeitsblatt ist Schritt 1, die Theorie-Seite ist das Nachschlagewerk.
  · Theorie-Karte (höchstens drei Sätze, großes eigenes Bild, Formelzeichen mit Einheit) direkt bei der Aufgabe – Tipp-Stufe 2.
  · Freiwillige Tipp-Stufen 1/2/3 unter jeder Pflichtaufgabe; ab dem 2. Fehlversuch öffnet Stufe 2 von selbst.
  · Rückmeldung je gewählter falscher Antwort (Feld »fb« in inhalt.py).
  · »Was glaubst du?« mit Auflösung am Ende der Einheit.
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
s = open(os.path.join(HERE, "vorlage_aufgaben.html"), encoding="utf-8").read()
TITLE = "Kräfte-Aufgaben"
rep("<title>Epochen-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Epochen-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Epochen-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>3BK</option>', '<option value="">–</option><option>1AK</option><option>1BK</option>')

PFL = ", ".join(str(n) for n in I.PFLICHT)
ZUS = ", ".join(str(t["nr"]) for t in I.T if t["tag"] == "Zusatz")
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li><b>Hier geht es los.</b> Du musst die Theorie nicht vorher durchlesen: Unter jeder Aufgabe steht eine <b>Theorie-Karte</b> mit dem Wichtigsten in drei Sätzen.
          Wer mehr wissen will, öffnet den <a href="theorie.html">Theorieteil</a> zum Nachschlagen.</li>
      <li><b>Auszufüllen:</b> Aufgabe 1 (Schätzung, ohne Punkte) und die Pflichtaufgaben """ + PFL + """ – zusammen die vier im Balken oben.
          <b>Zusatz</b> für Schnelle: """ + ZUS + """. Es gibt <b>keine Hausübung</b>.</li>
      <li>Bei jeder Aufgabe steht, wie lange sie ungefähr dauert. <b>Tipps kosten keine Punkte</b> – benutz sie ruhig.
          Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt; die Lösung wird dabei nicht verraten.</li>
      <li>Ganz unten <b>PDF erstellen</b> und in LMS hochladen. Das Gruppen-Protokoll gebt ihr getrennt über die <a href="versuche.html">Versuchsseite</a> ab.</li>
    </ol>""" + s[j:]
i = s.index("<!--FAHRPLAN-->"); j = s.index("<!--/FAHRPLAN-->") + len("<!--/FAHRPLAN-->")
s = s[:i] + "<!--FAHRPLAN--><!--/FAHRPLAN-->" + s[j:]
rep("0 von 15 bearbeitet", "0 von %d bearbeitet" % len(I.T))
s = re.sub(r'<p class="hint">Stand [0-9.]+ · v\d+</p>', '<p class="hint">Stand ' + STAND + " · " + I.V + "</p>", s, count=1)

# ---- offene Erklärungen (c.man) bewertet die Lehrkraft; automatisch geprüft wird nur der Rest ----
rep("  return { ok: parts.every(p => p.ok), parts };\n}", """  /* offene Erklärungen (c.man) zeigen nur eine Schreibhilfe; »richtig« bezieht sich auf die automatisch prüfbaren Teile */
  parts.forEach(p => { if ((t.chk[p.key] || {}).man) p.man = true; });
  const auto = parts.filter(p => !p.man), man = parts.filter(p => p.man);
  if (!auto.length && man.length) return { ok: man.every(p => p.filled), parts, man: true, manOnly: true };
  return { ok: auto.every(p => p.ok), parts, man: man.length > 0 };
}""")

# ---- showCheck: Rückmeldung je gewählter falscher Antwort + Tipp-Stufe 2 ab dem 2. Fehlversuch ----
_i = s.index("function showCheck(t) {"); _j = s.index("\nfunction showSolutions()", _i)
s = s[:_i] + """function showCheck(t) {
  const r = evalTask(t), fb = $("#fb_" + t.id); fb.hidden = false; fb.textContent = "";
  const a = S.a[t.id] || {};
  const auto = r.parts.filter(p => !p.man), man = r.parts.filter(p => p.man), autoOk = auto.every(p => p.ok), viele = r.parts.length > 1;
  const kurz = lab => { const m = String(lab).match(/^([a-j]\))/); return m ? m[1] + " " : (String(lab).length > 34 ? String(lab).slice(0, 32) + "…: " : lab + ": "); };
  fb.className = "fb " + (r.man ? (autoOk ? "info" : "no") : (r.ok ? "ok" : "no"));
  fb.append(el("strong", { text: r.man ? (autoOk ? (auto.length ? "Die automatisch prüfbaren Teile stimmen." : "Gespeichert.") : "Noch nicht ganz.") : (r.ok ? "Richtig!" : "Noch nicht ganz.") }));
  if (!autoOk) auto.forEach(p => {
    if (p.ok) return;
    const pre = viele ? kurz(p.label) : "";
    /* Rückmeldung genau zur gewählten falschen Antwort */
    const fbo = (t.fb || {})[p.key];
    if (p.kind === "sel" && p.filled && fbo && fbo[a[p.key]]) { fb.append(el("div", { text: pre + fbo[a[p.key]] })); return; }
    if (p.kind === "kw") { fb.append(el("div", { text: pre + "enthalten: " + p.hits.map(h => h[0] + (h[1] ? " \\u2713" : " \\u2717")).join(", ") })); return; }
    fb.append(el("div", { text: pre + (p.kind === "sel" ? (p.filled ? "Diese Auswahl stimmt noch nicht." : "Noch nichts ausgewählt.") : p.msg) }));
  });
  man.forEach(p => {
    const pre = viele ? kurz(p.label) : "";
    if (!p.filled) { fb.append(el("div", { text: pre + "Deine Antwort fehlt noch." })); return; }
    const da = p.hits.filter(h => h[1]).map(h => h[0]), fehlt = p.hits.filter(h => !h[1]).map(h => h[0]);
    fb.append(el("div", { text: pre + "Schreibhilfe – " + (da.length ? "gefunden: " + da.join(", ") : "noch keines der erwarteten Stichwörter") + (fehlt.length ? " \\u00b7 vielleicht fehlt noch: " + fehlt.join(", ") + " (eine richtige Umschreibung zählt auch)" : "") + "." }));
  });
  if (man.length) fb.append(el("div", { text: "Ob deine Erklärung fachlich stimmt, bewertet Prof. HOLZER. Lies sie noch einmal durch." }));
  /* Tipp-Stufe 2 (Theorie-Karte) öffnet ab dem 2. Fehlversuch von selbst */
  if (!r.ok) {
    S.chk = S.chk || {}; S.chk[t.id] = (S.chk[t.id] || 0) + 1; save();
    const st2 = document.getElementById("tipp2_" + t.id);
    if (S.chk[t.id] >= 2 && st2 && !st2.open) { st2.open = true; fb.append(el("div", { text: "Tipp 2 (Theorie-Karte) ist jetzt offen." })); }
  }
}""" + s[_j:]

# ---- Tipp-Stufen und Theorie-Karte unter der Aufgabe ----
rep('  if (t.hint) card.append(el("p", { class: "hint", text: t.hint }));',
    '''  if (t.hint) card.append(el("p", { class: "hint", text: t.hint }));
  if (t.tipps && t.tipps.length) card.append(tippStufen(t));''')
rep("function renderTask(t) {", """function karteEl(k) {
  const K = KARTEN[k], box = el("div", { class: "tkarte" });
  box.append(el("div", { class: "tkh" }, el("span", { class: "tkn", text: "Theorie-Karte" }), el("b", { text: K.titel }), el("span", { class: "tkb", text: K.buch })));
  if (K.bild) box.append(el("img", { class: "tkimg", src: K.bild, alt: K.alt, loading: "lazy" }));
  K.satz.forEach(x => { const p = el("p"); p.innerHTML = fett(x); box.append(p); });
  if (K.formeln && K.formeln.length) {
    const tb = el("table", { class: "tkf" });
    K.formeln.forEach(([z, bed, einh]) => tb.append(el("tr", {}, el("td", { class: "z", text: z }), el("td", { text: bed }), el("td", { class: "e", text: einh || "" }))));
    box.append(tb);
  }
  box.append(el("a", { class: "tklink", href: K.link, text: "Mehr dazu im Theorieteil" }));
  return box;
}
function fett(x) {
  return String(x).replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c])).replace(/\\*\\*(.+?)\\*\\*/g, "<b>$1</b>");
}
function tippStufen(t) {
  const box = el("div", { class: "tipps" });
  box.append(el("div", { class: "tippk", text: "Brauchst du Hilfe? Tipps kosten keine Punkte." }));
  const labels = ["Tipp 1 · Denkanstoß", "Tipp 2 · Theorie-Karte", "Tipp 3 · im Schulbuch nachlesen"];
  t.tipps.forEach((x, k) => {
    const dd = el("details", { class: "tipp" });
    if (k === 1) dd.id = "tipp2_" + t.id;
    dd.append(el("summary", { text: labels[k] }));
    if (k === 1 && KARTEN[x]) dd.append(karteEl(x));
    else { const p = el("p"); p.innerHTML = fett(x); dd.append(p); }
    dd.addEventListener("toggle", () => { if (!dd.open) return; S.chk = S.chk || {}; S.chk["tipp_" + t.id] = Math.max(S.chk["tipp_" + t.id] || 0, k + 1); save(); });
    box.append(dd);
  });
  return box;
}
function tippText(t) {
  const n = (S.chk || {})["tipp_" + t.id] || 0;
  return n ? " \\u00b7 Hilfe: " + (n === 1 ? "Tipp 1" : "Tipp 1\\u2013" + n) : " \\u00b7 ohne Tipp";
}
function aufloesungEl(t) {
  const box = el("div", { class: "aufl" });
  const b = el("button", { class: "btn secondary small", type: "button", text: "Auflösung zeigen (erst in Stunde 6)" });
  const out = el("div", { class: "fb info", hidden: "" });
  b.addEventListener("click", () => {
    const a = S.a[t.id] || {}; out.hidden = false; out.textContent = "";
    t.aufloesung.forEach(([k, richtig, warum]) => {
      const mein = a[k], ok = mein === richtig;
      out.append(el("div", {}, el("b", { text: ok ? "Du hast richtig vermutet: " : "Du hast gedacht: " }),
        (mein || "— nichts ausgewählt —") + (ok ? ". " : ". Richtig ist: " + richtig + ". ") + warum));
    });
  });
  box.append(b, out);
  return box;
}

function renderTask(t) {""")
rep('''  const sol = el("div", { class: "sol", id: "sol_" + t.id, hidden: "" }, el("strong", { text: "Musterlösung" }));''',
    '''  if (t.aufloesung) card.append(aufloesungEl(t));
  const sol = el("div", { class: "sol", id: "sol_" + t.id, hidden: "" }, el("strong", { text: "Musterlösung" }));''')

# ---- PDF: Hilfe-Nutzung sichtbar, Vorhersage nicht bewerten ----
rep('''    let st = "selbst bewerten";
    if (ev) {''', '''    let st = "selbst bewerten";
    if (t.frei) st = "Vorhersage – wird nicht bewertet";
    else if (ev && ev.man) {
      const au = ev.parts.filter(p => !p.man);
      st = (au.length ? "automatisch geprüft: " + (au.every(p => p.ok) ? "richtig" : "noch nicht richtig") + " · " : "") + "Erklärung: bewertet Prof. HOLZER";
    }
    else if (ev) {''')
rep('txt("Bewertung: " + (typeof LH_pdf === "function" ? LH_pdf(t, st) : st)',
    'txt("Bewertung: " + (typeof LH_pdf === "function" ? LH_pdf(t, st) : st) + (t.tipps && t.tipps.length ? tippText(t) : "")')
rep("(ev && ev.ok ? [70, 110, 40] : muted)", "(ev && ev.ok && !ev.man && !t.frei ? [70, 110, 40] : muted)")

# ---- Daten einsetzen ----
TJ = []
for t in I.T:
    x = dict(t)
    if not x["chk"]: x["chk"] = None
    if x.pop("vorhersage", False): x["frei"] = True
    x.pop("projekt", None); x.pop("besprechen", None)
    TJ.append(x)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = (s[:i] + 'const KEY = "%s";\nconst KAP = "K2.1", THEMA = "Kraefte";\n' % I.KEY
     + "const KARTEN = " + json.dumps(TD.karte_html_daten(), ensure_ascii=False) + ";\n"
     + "const T = " + json.dumps(TJ, ensure_ascii=False, indent=1) + ";" + s[j:])
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]

rep(".fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }",
    """.fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }
.fb.info { background: #E8F1F3; border: 2px solid #2E7D8C; }
.tipps { display: grid; gap: 8px; margin: 10px 0; }
.tippk { font-size: 15px; color: #5E6652; }
details.tipp { border: 2px solid #D3DCC2; border-radius: 12px; background: #F7F9F2; }
details.tipp > summary { cursor: pointer; font-weight: 700; font-size: 18px; color: #3B4A2F; padding: 12px 14px; min-height: 44px; display: flex; align-items: center; }
details.tipp[open] > summary { border-bottom: 1px solid #D3DCC2; }
details.tipp > p { margin: 0; padding: 12px 14px; font-size: 18px; line-height: 1.5; }
.tkarte { padding: 12px 14px; display: grid; gap: 8px; }
.tkh { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; font-size: 18px; }
.tkn { background: #2E7D8C; color: #fff; font-size: 13px; font-weight: 700; border-radius: 999px; padding: 3px 10px; }
.tkb { background: #6E7F4E; color: #fff; font-size: 13px; font-weight: 700; border-radius: 999px; padding: 3px 10px; }
.tkimg { width: 100%; height: auto; border: 1px solid #D3DCC2; border-radius: 10px; background: #fff; }
.tkarte p { margin: 0; font-size: 18px; line-height: 1.5; }
table.tkf { border-collapse: collapse; width: 100%; font-size: 17px; }
table.tkf td { border-top: 1px solid #D3DCC2; padding: 5px 4px; }
table.tkf td.z { font-weight: 700; color: #3B4A2F; }
table.tkf td.e { color: #2E7D8C; font-weight: 700; text-align: right; white-space: nowrap; }
.tklink { font-weight: 700; color: #2E7D8C; min-height: 44px; display: inline-flex; align-items: center; }
.aufl { margin-top: 10px; display: grid; gap: 8px; }""")
rep('KAP + " Zeit-Einteilung und Epochen – Aufgaben"', '"K2.1 Mechanische Kräfte – Aufgaben"')
rep('clean("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen · Schulbuch S. 13–14")', 'clean("' + I.EYEBROW + " · Schulbuch S. 44–65" + '")')
rep('d.text("Epochen-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Stunde 1 und 2): Aufgabe "', '"Noch offen (Pflicht): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–10 bearbeitet."', '"Alle Pflicht-Aufgaben bearbeitet."')
rep('el("span", { class: tagCls, text: t.tag })),', 'el("span", { class: tagCls, text: t.tag }), t.zeit ? el("span", { class: "tag zeit", text: "ca. " + t.zeit + " min" }) : null),')
rep('const tagCls = t.tag.startsWith("Stunde") ?', 'const tagCls = (t.tag.startsWith("Stunde") || t.tag.startsWith("Vorhersage")) ?')
rep('s = String(s).replace(/⊙/g, "(Punkt)")', 's = String(s).replace(/√/g, "Wurzel ").replace(/≈/g, "ca.").replace(/⊙/g, "(Punkt)")')
rep(".pill.theory { background: var(--theory); }", ".pill.theory { background: var(--theory); } .tag.zeit { color: var(--teal); border-color: var(--teal); }")
s = s.replace("26-27-3BK-K1.3-Epochen-TH-Handy-v1", I.KEY)
# Klassennavigation (wird von build_index.py ohnehin neu gesetzt) schon hier auf 1AB stellen
s = s.replace("PBGW 3BK", "NAWI 1AB").replace("3BK · Start", "1AB · Start")
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Epochen", "Zeit-Einteilung", "3BK"]:
    assert bad not in _plain, re.findall(r".{60}" + bad + r".{20}", _plain)[:3]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Kräfte-Check – Quiz</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Kräfte-Check</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Kräfte-Check am Handy</h2>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Kräfte-Check"')
qv = qv.replace("Frage 1 von 16", "Frage 1 von %d" % len(I.QUIZ))
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
    h = "".join(f"<th>{md(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join((f"<th scope=row>{md(c)}</th>" if k == 0 else f"<td>{md(c)}</td>") for k, c in enumerate(r)) + "</tr>" for r in rows[1:])
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


ul = lambda xs: '<ul class="pts">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ul>"
ol = lambda xs: '<ol class="goals">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ol>"
merke = lambda x: f'<div class="merke">{md(x)}</div>'
hint = lambda x: f'<p class="hint">{md(x)}</p>'
reveal = lambda q, a: f'<div class="stopq"><p><strong>{md(q)}</strong></p><details class="reveal"><summary>Erst überlegen – dann Lösung anzeigen</summary><p>{md(a)}</p></details></div>'
jetzt = lambda txt, href: f'<a class="jetzt" href="{href}">{esc(txt)} →</a>'
VS_BY_NR = {v["nr"]: v for v in VD.VS}


def figure(src, alt, cap):
    return f'<figure class="fig"><img src="{src}" alt="{esc(alt)}" loading="lazy"><figcaption>{md(cap)}</figcaption></figure>'


def karte_block(v):
    f = ""
    if v["formeln"]:
        f = '<table class="tkf">' + "".join(f'<tr><td class="z">{md(z)}</td><td>{md(bed)}</td><td class="e">{md(e)}</td></tr>' for z, bed, e in v["formeln"]) + "</table>"
    return ('<div class="tkarte-s">'
            f'<div class="tkh"><span class="tkn">Theorie-Karte</span><b>{esc(v["titel"])}</b><span class="tkb">{esc(v["buch"])}</span></div>'
            f'<img class="tkimg" src="{v["bild"]}" alt="{esc(v["alt"])}" loading="lazy">'
            + "".join(f"<p>{md(x)}</p>" for x in v["satz"]) + f + "</div>")


def versuch_block(nr, titel, text):
    v = VS_BY_NR.get(nr) or VD.VS[0]
    return (f'<div class="vbox"><div class="vhead"><span class="vnr">{esc(nr)}</span><span class="vtag">KERN</span></div>'
            f'<p><strong>{esc(titel)}</strong></p><p>{md(text)}</p><a class="btn small" href="versuche.html">Zur Versuchsseite</a></div>')


def block(b):
    k = b[0]
    if k == "tiles": return tiles(b[1])
    if k == "ul": return ul(b[1])
    if k == "ol": return ol(b[1])
    if k == "merke": return merke(b[1])
    if k == "hint": return hint(b[1])
    if k == "table": return table(b[1])
    if k == "reveal": return "".join(reveal(q, a) for q, a in b[1])
    if k == "img": return figure(b[1], b[2], b[3])
    if k == "versuch": return versuch_block(b[1], b[2], b[3])
    if k == "buch": return f'<div class="buch"><span class="bicon">Buch</span><p>{md(b[1])}</p></div>'
    if k == "karte": return karte_block(b[1])
    if k == "gemeinsam": return f'<div class="gem"><span class="gicon">Gemeinsam</span><p>{md(b[1])}</p></div>'
    raise ValueError(k)


def render(item):
    if isinstance(item, tuple) and item[0] == "jetzt": return jetzt(item[1], item[2])
    return slide(item["title"], "".join(block(b) for b in item["blocks"]), item["pill"], item["id"])


def _teil(pid, eyebrow, title, items):
    """Die erste Folie eines Teils trägt sonst dieselbe id wie der Abschnitt selbst – das gäbe doppelte ids
    (test_kadetten_layout). Der Anker bleibt am <section>, die Folie darin verliert die doppelte id."""
    arts = [render(x).replace(f'<article class="slide" id="{pid}">', '<article class="slide">', 1) for x in items]
    return (pid, eyebrow, title, arts)


PARTS = [_teil(*p) for p in TD.PARTS]
LZ = slide("Das kannst du nach dieser Einheit", ol(I.LERNZIELE), I.BUCH, "ziele")
PARTS[0] = (PARTS[0][0], PARTS[0][1], PARTS[0][2], PARTS[0][3] + [LZ])
PARTS.append(("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]))
CHECK = "".join(f'<div class="ziel"><p>{md(z)}</p><div class="chips" role="group" aria-label="Selbstcheck">' + "".join(
    f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht")) + "</div></div>"
    for k, z in enumerate(I.LERNZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                      slide("Alle Größen und Einheiten", karte_block(TD.KARTEN["k9"])),
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
.chip { font: inherit; font-size: 16px; font-weight: 700; color: #3B4A2F; background: #fff; border: 2px solid #D3DCC2; border-radius: 999px; padding: 6px 14px; cursor: pointer; min-height: 44px; }
.chip[aria-pressed="true"][data-v="sicher"] { background: #E6F0D3; border-color: #7FA83A; }
.chip[aria-pressed="true"][data-v="fast"] { background: #FFF1D6; border-color: #D9772B; }
.chip[aria-pressed="true"][data-v="noch nicht"] { background: #F6E3DF; border-color: #8C3B2E; }
.chip:focus-visible { outline: 3px solid #2E7D8C; outline-offset: 2px; }
.jetzt { display: block; text-align: center; background: #7FA83A; color: #fff; font-weight: 700; font-size: 18px; text-decoration: none; border-radius: 12px; padding: 12px 16px; }
.slide[id], .part { scroll-margin-top: 56px; }
.fig { margin: 0; display: grid; gap: 6px; justify-items: center; }
.fig img { max-width: 100%; height: auto; border-radius: 10px; border: 1px solid #D3DCC2; background: #fff; }
.fig figcaption { font-size: 15px; color: #5E6652; text-align: center; }
.vbox { border: 2px solid #A33A2B; border-radius: 12px; padding: 10px 14px; display: grid; gap: 6px; background: #FBF1EE; }
.vbox p { margin: 0; }
.vhead { display: flex; gap: 8px; align-items: center; }
.vnr { font-weight: 700; color: #fff; background: #A33A2B; border-radius: 8px; padding: 2px 10px; }
.vtag { font-size: 13px; font-weight: 700; color: #fff; background: #3B4A2F; border-radius: 999px; padding: 2px 10px; }
.vbox .btn { justify-self: start; background: #A33A2B; color: #fff; text-decoration: none; font-weight: 700; border-radius: 10px; padding: 10px 14px; }
.buch { display: flex; gap: 12px; align-items: center; background: #EEF3E4; border: 2px solid #3B4A2F; border-radius: 12px; padding: 10px 14px; }
.buch p { margin: 0; } .bicon { font-weight: 700; color: #fff; background: #3B4A2F; border-radius: 8px; padding: 4px 10px; white-space: nowrap; }
.gem { display: flex; gap: 12px; align-items: center; background: #FFF4EA; border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
.gem p { margin: 0; } .gicon { font-weight: 700; color: #fff; background: #D9772B; border-radius: 8px; padding: 4px 10px; white-space: nowrap; }
.tkarte-s { border: 2px solid #2E7D8C; border-radius: 12px; background: #F3F8F9; padding: 12px 14px; display: grid; gap: 8px; }
.tkh { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; font-size: 18px; }
.tkn { background: #2E7D8C; color: #fff; font-size: 13px; font-weight: 700; border-radius: 999px; padding: 3px 10px; }
.tkb { background: #6E7F4E; color: #fff; font-size: 13px; font-weight: 700; border-radius: 999px; padding: 3px 10px; }
.tkimg { width: 100%; height: auto; border: 1px solid #D3DCC2; border-radius: 10px; background: #fff; }
.tkarte-s p { margin: 0; font-size: 18px; line-height: 1.5; }
table.tkf { border-collapse: collapse; width: 100%; font-size: 17px; }
table.tkf td { border-top: 1px solid #C2D4D8; padding: 5px 4px; }
table.tkf td.z { font-weight: 700; color: #3B4A2F; }
table.tkf td.e { color: #2E7D8C; font-weight: 700; text-align: right; white-space: nowrap; }
</style>""")
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Mechanische Kräfte – Theorie</title>
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
<section class="part" id="nachschlagen">
  <div class="band"><div class="eyebrow">So arbeitest du</div><h2>Diese Seite ist dein Nachschlagewerk</h2></div>
  <article class="slide">
    <p>Beginne beim <strong>Arbeitsblatt</strong>. Dort steht bei jeder Aufgabe das Wichtigste in drei Sätzen auf einer Theorie-Karte.
    Diese Seite hier brauchst du, wenn du mehr wissen willst, wenn du etwas nachlesen möchtest – und vor dem Test.</p>
    <div class="btns"><a class="btn" href="aufgaben.html">1 · Arbeitsblatt</a><a class="btn alt" href="versuche.html">2 · Gruppenprojekt {esc(I.VS_ID)}</a><a class="btn alt" href="quiz.html">3 · Kräfte-Check (Quiz)</a></div>
  </article>
</section>
{body}
<section class="next" id="weiter">
  <div class="eyebrow">Weiter geht's</div>
  <h2>Jetzt bist du dran</h2>
  <div class="btns"><a class="btn" href="aufgaben.html">1 · Arbeitsblatt A1–A{len(I.T)}</a><a class="btn alt" href="versuche.html">2 · Gruppenprojekt</a><a class="btn alt" href="quiz.html">3 · Kräfte-Check (Quiz)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch Naturwissenschaften HAK 1 (Trauner) S. 44–65. Alle Grafiken selbst gezeichnet. <a href="../">Klassenübersicht 1AB</a></p>
  <p class="hint">Stand {STAND} · {I.V}</p>
</section>
</main>
<script>
(function () {{
  var KEY = "{I.LERNSEITE_KEY}", S = {{}};
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

# ================================================================ Versuchsseite (Gruppenprojekt)
s = open(os.path.join(HERE, "vorlage_versuche.html"), encoding="utf-8").read()
VDATA = []
for v in VD.VS:
    x = {k: v[k] for k in ("id", "nr", "titel", "bindung", "intro", "sicher", "entsorgung", "schritte", "skizze", "beob", "erk", "interp", "schluss", "buch", "kern")}
    x["mat"] = [[m[0], m[1]] for m in v["mat"]]
    x["platz"] = v["platz"]
    x["vorab"] = VD.VORAB
    x["nach"] = VD.NACH
    VDATA.append(x)
i = s.index("const V = ") + len("const V = "); j = s.index("];\nconst KEY", i) + 1
s = s[:i] + json.dumps(VDATA, ensure_ascii=False) + s[j:]
rep('const KEY = "26-27-2AB-K1.2-Bindungen-VS-Handy-v1";', 'const KEY = "%s";' % I.VS_KEY)
rep('<option value="">–</option><option>2A</option><option>2B</option>', '<option value="">–</option><option>1AK</option><option>1BK</option>')
s = s.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
rep("<h1>Bindungs-Versuche</h1>", "<h1>Gruppenprojekt Kräfte</h1>")
rep("<title>Bindungs-Versuche</title>", "<title>Gruppenprojekt Kräfte</title>")
rep('d.text("Bindungs-Versuche", M + 15, y + 11.5)', 'd.text("Gruppenprojekt Kräfte", M + 15, y + 11.5)')
s = s.replace('"K1.2 Die Bindungsarten – Versuchsprotokoll"', '"K2.1 Mechanische Kräfte – Gruppenprotokoll"')
s = s.replace('clean("K1.2 Versuche · "', 'clean("K2.1 Gruppenprojekt · "').replace('"K1.2-Versuche-" + slug(S.ich)', '"K2.1-Gruppenprojekt-" + slug(S.ich)')
s = s.replace('s = String(s).replace(/⊙/g, "(Punkt)")', 's = String(s).replace(/√/g, "Wurzel ").replace(/≈/g, "ca.").replace(/⊙/g, "(Punkt)")')
s = s.replace("Erklärt mit den Teilchen.", "Ordnet eure Daten ein: unterstützt, spricht dagegen oder unklar?")
s = re.sub(r'(alt="QR-Code zur Versuchsseite" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "versuche.html"), s, count=1)

# Zusatzfelder: Frage/Quellen/Plan vor der Messtabelle, Grenze/Alltag danach
rep('  body.append(el("h3", { text: v.beob.titel }));', """  if (v.platz) body.append(el("p", { class: "hint" }, el("b", { text: "Wo steht der Versuch? " }), v.platz));
  if (v.vorab) {
    body.append(el("h3", { text: "Stunde 2: Frage, Quellen und Plan" }));
    v.vorab.forEach(([k, lab, hw]) => body.append(field(v.id, k, lab, true, hw)));
  }
  body.append(el("h3", { text: v.beob.titel }));""")
rep('  body.append(field(v.id, "erk", "Erkenntnis", true, v.erk), field(v.id, "interp", "Interpretation", true, v.interp), field(v.id, "schluss", "Schlussfolgerung", true, v.schluss));',
    """  body.append(el("h3", { text: "Stunde 4: Auswerten und erklären" }));
  body.append(field(v.id, "erk", "Erkenntnis", true, v.erk), field(v.id, "interp", "Interpretation", true, v.interp), field(v.id, "schluss", "Schlussfolgerung", true, v.schluss));
  if (v.nach) v.nach.forEach(([k, lab, hw]) => body.append(field(v.id, k, lab, true, hw)));""")
rep('''  [["Erkenntnis", "erk"], ["Interpretation", "interp"], ["Schlussfolgerung", "schluss"]].forEach(([t, k]) => { L.push([t + ":", "h"]); L.push(["  " + (filled(a[k]) ? a[k].trim() : "— keine Antwort —"), filled(a[k]) ? "n" : "x"]); });''',
    '''  (v.vorab || []).concat([["erk", "Erkenntnis"], ["interp", "Interpretation"], ["schluss", "Schlussfolgerung"]], v.nach || []).forEach(fl => {
    const k = fl[0], t = fl[1]; L.push([t + ":", "h"]); L.push(["  " + (filled(a[k]) ? String(a[k]).trim() : "— keine Antwort —"), filled(a[k]) ? "n" : "x"]); });''')

i = s.index('<section class="card safety">'); j = s.index("</section>", i) + 10
s = s[:i] + '<section class="card safety">\n    <h2>Sicherheit in dieser Einheit</h2>\n    <ul class="steps">\n' + "".join(
    f"      <li><b>{esc(a)}:</b> {esc(b)}</li>\n" for a, b in VD.SICHERHEIT) + "    </ul>\n  </section>" + s[j:]
i = s.index("/*STATIONEN*/"); j = s.index("/*/STATIONEN*/")
s = s[:i] + "/*STATIONEN*/\n" + json.dumps([["Gruppe %d · %s" % (v["gruppe"], v["titel"]), v["id"]] for v in VD.VS], ensure_ascii=False) + \
    """.forEach(([t, id]) => { $("#vs").append(el("div", { class: "grp", text: t })); V.filter(v => v.id === id).forEach(v => $("#vs").append(versuch(v))); });\n""" + s[j:]
s = s.replace('text: v.station ? "KERN · Station " + v.station : (v.demo ? "KERN · Demo" : "ZUSATZ")', 'text: "KERN"')
s = s.replace('(v.station ? "KERN · Station " + v.station + " · " : (v.demo ? "KERN · Lehrer-Demo · " : "ZUSATZ · "))', '"KERN · "')
i = s.index("<!--PLAN-->"); j = s.index("<!--/PLAN-->") + len("<!--/PLAN-->")
PLANHTML = ('<!--PLAN--><section class="card" id="plan">\n'
            '    <div class="head"><span class="nr">Ablauf</span><span class="pill theory">Gruppenprojekt ' + I.VS_ID + '</span></div>\n'
            '    <h2>So läuft das Projekt</h2>\n'
            '    <ul class="steps">\n'
            '      <li><b>Sieben Gruppen, sieben Themen.</b> Jede Gruppe öffnet nur ihren eigenen Auftrag weiter unten. Die anderen bleiben zugeklappt – ihr hört sie in Stunde 5.</li>\n'
            '      <li><b>Rollen:</b> Leitung und Zeit · Quellenprüfung · Aufbau und Messung · Protokoll. In der Fünfergruppe kommt Material und Gegenprobe dazu.</li>\n'
            '      <li><b>Stunde 2:</b> Frage, Vermutung, geänderte und gleich bleibende Bedingung, zwei geprüfte Quellen. Danach gibt Prof. HOLZER euren Plan frei.</li>\n'
            '      <li><b>Stunde 3:</b> messen. Schreibt nur auf, was ihr wirklich gemessen habt. Erwartete Zahlen sind keine Messwerte.\n'
            '          Die Gruppen 2, 4 und 7 teilen sich zwei Kraftmesser: <b>nach 14 Minuten wird gewechselt.</b></li>\n'
            '      <li><b>Stunde 4:</b> Erkenntnis, Interpretation, Schlussfolgerung, Grenze und Alltagsbeispiel ausfüllen. Dann die Drei-Minuten-Erklärung üben.</li>\n'
            '      <li><b>Stunde 5:</b> jede Gruppe höchstens <b>3 Minuten</b> einschließlich Versuch. Jeder erklärt einen kurzen Teil. Eine PowerPoint ist nicht nötig.</li>\n'
            '    </ul>\n'
            '    <p class="hint"><b>Abgabe:</b> Ein Protokoll-Handy je Gruppe trägt alles ein. Der Protokollführer schreibt im Feld »Ich gebe diese PDF ab als« '
            'nacheinander jeden Nachnamen hinein, tippt jedes Mal »PDF erstellen« und schickt die PDF in den Gruppenchat. Jeder lädt seine eigene PDF in LMS hoch. '
            'Eure persönlichen Aufgaben 1, 2 und 4 gebt ihr getrennt über das <a href="aufgaben.html">Arbeitsblatt</a> ab.</p>\n'
            '  </section><!--/PLAN-->')
s = s[:i] + PLANHTML + s[j:]
s = re.sub(r"<!--STAND-->.*?<!--/STAND-->", '<!--STAND--><p class="hint" style="text-align:center;margin:18px 0 8px">' + I.EYEBROW + " · Gruppenprojekt " + I.VS_ID + " · Stand " + STAND + " · " + I.V + "</p><!--/STAND-->", s, flags=re.S)
s = s.replace("26-27-2AB-K1.2-Bindungen-VS-Handy-v1", I.VS_KEY)
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Bindungsarten", "K1.2", "Wellen", "Pendel"]:
    assert bad not in _plain, re.findall(r".{60}" + re.escape(bad) + r".{30}", _plain)[:3]
_alt = 'clean("K2.1 Gruppenprojekt · " + (S.name || "") + " · Seite " + p + " von " + n)'
assert s.count(_alt) == 1, s.count(_alt)
s = s.replace(_alt, 'clean("K2.1 Gruppenprojekt · " + ((S.name || "").length > 70 ? (S.name || "").slice(0, 67) + " …" : (S.name || "")) + " · Seite " + p + " von " + n)')
open(DST + "versuche.html", "w", encoding="utf-8").write(s)

for f in ["theorie.html", "aufgaben.html", "versuche.html", "quiz.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
