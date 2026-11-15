"""Handy-Seiten NAWI 2AB · K1.5 Säuren und Basen bauen (Theorie-Seite, Arbeitsblatt mit Versuch; Quiz bestellt Stephan später, 14.11.2026).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-5-saeuren/skizzen.py  und danach  python3 werkzeug/quellen/2ab-k1-5-saeuren/bauen.py
Danach: python3 werkzeug/quellen/2ab-k1-5-saeuren/regeln.py, eintragen.py und python3 werkzeug/nach_dem_bauen.py
Arbeitsblatt-Grundlage: eingefrorene Kopie vorlage_aufgaben.html und Bauweise der Einheit K2.4 Akustik 4AB (Stand 14.11.2026).
Standards 07.–13.11.2026: Arbeitsblatt ist der einzige Arbeitsort (Theorie-Karten, Tipp-Stufen, Versuchsprotokoll mit Anleitung), EIN PDF, Theorie-Seite = Nachschlagewerk,
»Was glaubst du?« mit Auflösung in Stunde 4, Rückmeldung je falscher Antwort, Marken, Fahrplan ohne Datum (Stundenwahl).
NEU in dieser Einheit: Versuchsanleitung als aufklappbare Karte im Arbeitsblatt (KLARE_ANWEISUNGEN) und ein pH-Schieber auf der Theorie-Seite."""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
import plan as P
import theorie_daten as TD
import sims as SIMS
STAND = I.STAND

DST = os.path.join(ROOT, I.ORDNER) + "/"


def bild_mass(src):
    """Breite und Höhe aus der viewBox der eigenen SVG – damit reserviert der Browser den Platz, nichts verrutscht beim Laden."""
    try:
        t = open(os.path.join(DST, src), encoding="utf-8").read(600)
        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', t)
        return (round(float(m.group(1))), round(float(m.group(2)))) if m else None
    except OSError:
        return None


os.makedirs(DST, exist_ok=True)
esc = html.escape
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
CAMO, LOGO, SMILEY = b64(WZ + "/camo.png"), b64(WZ + "/logo.png"), b64(WZ + "/smiley.png")
nb = lambda s: re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
tief = lambda s: re.sub(r"(?<![\w/])([A-Za-zρμ])_([A-Za-zäöü]{1,12}|\d{1,2})\b", r"\1<sub>\2</sub>", s)
md = lambda s: tief(re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(nb(s))))


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


s = ""


def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (old[:90], n); s = s.replace(old, new)


# ================================================================ Arbeitsblatt
s = open(os.path.join(HERE, "vorlage_aufgaben.html"), encoding="utf-8").read()
TITLE = "Arbeitsblatt Säuren und Basen"
rep(' · <a href="quiz.html">Zum Quiz</a>', "")
rep("<title>Epochen-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Epochen-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Epochen-Aufgaben am Handy</h2>", "<h2>" + TITLE + "</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>3BK</option>', '<option value="">–</option>' + "".join(f"<option>{k}</option>" for k in I.KLASSEN))

ZUS = ", ".join(str(t["nr"]) for t in I.T if t["tag"] == "Zusatz")
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li><b>Ein Arbeitsblatt für alles.</b> Aufgaben, Versuch und Theorie-Karten stehen hier. Die <a href="theorie.html">Theorie-Seite</a> ist zum Nachschlagen.</li>
      <li><b>Stunde 1:</b> Aufgaben 1–2 · <b>Stunde 2:</b> Aufgaben 3–4 · <b>Stunde 3:</b> Aufgabe 5 und VERSUCH (Aufgabe 6) · <b>Stunde 4:</b> Aufgabe 7. Zusatz für Schnelle: """ + ZUS + """. Es gibt <b>keine Hausübung</b>.</li>
      <li>Bei jeder Aufgabe steht, wie lange sie dauert und wie du arbeitest: <b>SELBSTSTUDIUM</b> (allein) oder <b>VERSUCH</b> (Gruppe). Tipps kosten keine Punkte.</li>
      <li><b>Abgabe: EIN PDF</b> ganz unten – in Stunde 4 in LMS hochladen. Am Ende jeder Stunde tippst du auf »PDF erstellen« und hebst es nur auf (Sicherung).</li>
    </ol>""" + s[j:]
i = s.index("<!--FAHRPLAN-->"); j = s.index("<!--/FAHRPLAN-->") + len("<!--/FAHRPLAN-->")
s = s[:i] + "<!--FAHRPLAN--><!--/FAHRPLAN-->" + s[j:]
rep("0 von 15 bearbeitet", "0 von %d bearbeitet" % len(I.T))
s = re.sub(r'<p class="hint">Stand [0-9.]+ · v\d+</p>', '<p class="hint">Stand ' + STAND + " · " + I.V + "</p>", s, count=1)

# ---- kurze Eingabefelder (input statt textarea) auch für c.kurz, z. B. Messwerte ----
rep("textField(t.id, f[0], f[1], !(t.chk && t.chk[f[0]] && t.chk[f[0]].num !== undefined), 3)",
    "textField(t.id, f[0], f[1], !(t.chk && t.chk[f[0]] && (t.chk[f[0]].num !== undefined || t.chk[f[0]].kurz)), 3)")
# ---- offene Erklärungen (c.man) bewertet die Lehrkraft ----
rep("  return { ok: parts.every(p => p.ok), parts };\n}", """  parts.forEach(p => { if ((t.chk[p.key] || {}).man) p.man = true; });
  const auto = parts.filter(p => !p.man), man = parts.filter(p => p.man);
  if (!auto.length && man.length) return { ok: man.every(p => p.filled), parts, man: true, manOnly: true };
  return { ok: auto.every(p => p.ok), parts, man: man.length > 0 };
}""")

rep('t.fields.forEach(fl => L.push(fl[1] + ": " + f(fl[0])));',
    't.fields.forEach(fl => L.push(fl[1] + (/[?:.!]$/.test(fl[1]) ? " " : ": ") + f(fl[0])));')

# ---- showCheck: Rückmeldung je gewählter falscher Antwort + Tipp-Stufe 2 ab dem 2. Fehlversuch ----
_i = s.index("function showCheck(t) {"); _j = s.index("\nfunction showSolutions()", _i)
s = s[:_i] + """function showCheck(t) {
  const r = evalTask(t), fb = $("#fb_" + t.id); fb.hidden = false; fb.textContent = "";
  const a = S.a[t.id] || {};
  const auto = r.parts.filter(p => !p.man), man = r.parts.filter(p => p.man), autoOk = auto.every(p => p.ok), viele = r.parts.length > 1;
  const kurz = lab => { const m = String(lab).match(/^([a-k]\\))/); return m ? m[1] + " " : (String(lab).length > 34 ? String(lab).slice(0, 32) + "…: " : lab + ": "); };
  fb.className = "fb " + (r.man ? (autoOk ? "info" : "no") : (r.ok ? "ok" : "no"));
  fb.append(el("strong", { text: r.man ? (autoOk ? (auto.length ? "Die automatisch prüfbaren Teile stimmen." : "Gespeichert.") : "Noch nicht ganz.") : (r.ok ? "Richtig!" : "Noch nicht ganz.") }));
  if (!autoOk) auto.forEach(p => {
    if (p.ok) return;
    const pre = viele ? kurz(p.label) : "";
    const fbo = (t.fb || {})[p.key];
    if (p.kind === "sel" && p.filled && fbo && fbo[a[p.key]]) { fb.append(el("div", { text: pre + fbo[a[p.key]] })); return; }
    if (p.kind === "num" && p.filled && Array.isArray(fbo)) {
      const zm = String(a[p.key] || "").replace(/(\\d)[ .\u00a0\u202f](?=\\d{3}(\\D|$))/g, "$1").replace(",", ".").match(/\\d+(\\.\\d+)?/);
      const z = zm ? parseFloat(zm[0]) : null, hit = z === null ? null : fbo.find(x => Math.abs(z - x[0]) <= Math.abs(x[0]) * 0.02);
      if (hit) { fb.append(el("div", { text: pre + hit[1] })); return; }
    }
    if (p.kind === "kw") { fb.append(el("div", { text: pre + "enthalten: " + p.hits.map(h => h[0] + (h[1] ? " \\u2713" : " \\u2717")).join(", ") })); return; }
    fb.append(el("div", { text: pre + (p.kind === "sel" ? (p.filled ? "Diese Auswahl stimmt noch nicht." : "Noch nichts ausgewählt.") : p.msg) }));
  });
  man.forEach(p => {
    const pre = viele ? kurz(p.label) : "";
    if (!p.filled) { fb.append(el("div", { text: pre + "Deine Antwort fehlt noch." })); return; }
    if ((t.chk[p.key] || {}).kurz) return;   // Messwerte: nur prüfen, ob etwas eingetragen ist
    const da = p.hits.filter(h => h[1]).map(h => h[0]), fehlt = p.hits.filter(h => !h[1]).map(h => h[0]);
    fb.append(el("div", { text: pre + "Schreibhilfe – " + (da.length ? "gefunden: " + da.join(", ") : "noch keines der erwarteten Stichwörter") + (fehlt.length ? " \\u00b7 vielleicht fehlt noch: " + fehlt.join(", ") + " (eine richtige Umschreibung zählt auch)" : "") + "." }));
  });
  if (man.length) fb.append(el("div", { text: "Ob deine Erklärung fachlich stimmt, bewertet Prof. HOLZER. Lies sie noch einmal durch." }));
  if (!r.ok) {
    S.chk = S.chk || {}; S.chk[t.id] = (S.chk[t.id] || 0) + 1; save();
    const st2 = document.getElementById("tipp2_" + t.id);
    if (S.chk[t.id] >= 2 && st2 && !st2.open) { st2.open = true; fb.append(el("div", { text: "Tipp 2 (Theorie-Karte) ist jetzt offen." })); }
  }
}""" + s[_j:]

# ---- Tipp-Stufen, Theorie-Karte, Auflösung, Pegelmesser ----
rep('  if (t.hint) card.append(el("p", { class: "hint", text: t.hint }));',
    '''  if (t.hint) card.append(el("p", { class: "hint", text: t.hint }));
  if (t.versuch) card.append(el("p", { class: "vsid", text: "Versuch " + t.versuch + " · alle Gruppen machen dasselbe · jeder trägt die Werte selbst ein" }));
  if (t.anleitung) card.append(anleitungEl());
  if (t.link) { const lk = el("div", { class: "simlink" }); lk.append(el("a", { class: "btn", href: t.link[1], target: "_blank", rel: "noopener", text: t.link[0] }), el("p", { class: "simt", text: t.link[2] })); card.append(lk); }
  if (t.tipps && t.tipps.length) card.append(tippStufen(t));
  (t.sim || []).forEach(k => {
    if (!SIMHTML[k]) return;
    const d = el("details", { class: "simd" }); d.append(el("summary", { text: "Ausprobieren: " + SIMTITEL[k] + " – " + SIMZEILE[k] }));
    d.insertAdjacentHTML("beforeend", SIMHTML[k]); card.append(d);
    if (window.simStart) window.simStart();
  });''')
rep("function renderTask(t) {", """function karteEl(k) {
  const K = KARTEN[k], box = el("div", { class: "tkarte" });
  box.append(el("div", { class: "tkh" }, el("span", { class: "tkn", text: "Theorie-Karte" }), el("b", { text: K.titel }), el("span", { class: "tkb", text: K.buch })));
  if (K.bild) {
    const pic = el("picture", { class: "bildzoom" });
    pic.append(el("img", Object.assign({ class: "tkimg", src: K.bild, alt: K.alt, loading: "lazy" }, IMGMASS[K.bild] ? { width: IMGMASS[K.bild][0], height: IMGMASS[K.bild][1] } : {})));
    box.append(pic, el("p", { class: "zoomhint", text: "Bild antippen – dann wird es groß." }));
  }
  K.satz.forEach(x => { const p = el("p"); p.innerHTML = fett(x); box.append(p); });
  if (K.formeln && K.formeln.length) {
    const tb = el("table", { class: "tkf" });
    K.formeln.forEach(([z, bed, einh]) => {
      const a = el("td", { class: "z" }), b = el("td"), c = el("td", { class: "e" });
      a.innerHTML = fett(z); b.innerHTML = fett(bed); c.innerHTML = fett(einh || "");
      tb.append(el("tr", {}, a, b, c));
    });
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
  const b = el("button", { class: "btn secondary small", type: "button", text: "Auflösung zeigen (erst in Stunde 4)" });
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
/* ---------------- Versuchsanleitung (KLARE_ANWEISUNGEN.md): Ziel, Material, Gruppen, Vorbereitung, Schritte, Messwerte, Sicherheit, Abgabe, Auswertung ---------------- */
function anleitungEl() {
  /* Aufbau wie die Versuchsseiten (K1.3 Reaktionen): Ziel, Platz, Sicherheit, Geräte & Chemikalien mit Icons, Durchführung, Skizze, Entsorgung */
  const A_ = ANL, dd = el("details", { class: "anl", open: "" });
  dd.append(el("summary", { text: "Anleitung VERSUCH " + VSID + " (antippen zum Zu- oder Aufklappen)" }));
  const html = (tag, cls, x) => { const n = el(tag, cls ? { class: cls } : {}); n.innerHTML = fett(x); return n; };
  const zeile = (k, v, cls) => { const p = el("div", { class: cls || "hint" }); p.append(el("b", { text: k + " " })); const sp = el("span"); sp.innerHTML = fett(v); p.append(sp); return p; };
  const icons = (arr) => { const m = el("div", { class: "mat" }); arr.forEach(([t, ic]) => m.append(el("div", { class: "matitem" }, el("img", { src: "vs-img/i_" + ic + ".png", alt: "", loading: "lazy" }), el("span", { text: t })))); return m; };
  dd.append(html("p", "q", A_.ziel));
  dd.append(zeile("Wo steht der Versuch?", A_.platz));
  const w = el("div", { class: "warn" }); w.append(el("b", { text: "Sicherheit: " })); const ws = el("span"); ws.innerHTML = fett(A_.sicherheit.join(" ")); w.append(ws); dd.append(w);
  dd.append(el("h3", { text: "Geräte & Chemikalien – je Gruppe" }), icons(A_.mat));
  dd.append(el("h3", { text: "An der Probenstation" }), icons(A_.station));
  dd.append(zeile("Gruppen und Rollen:", A_.gruppen), zeile("Vorbereitung:", A_.vorbereitung));
  dd.append(el("h3", { text: "Durchführung" }));
  const ol = el("ol", { class: "steps" }); A_.schritte.forEach(x => ol.append(html("li", "", x))); dd.append(ol);
  if (A_.bild) dd.append(el("picture", { class: "bildzoom" }, el("img", Object.assign({ class: "tkimg", src: A_.bild, alt: A_.alt, loading: "lazy" }, IMGMASS[A_.bild] ? { width: IMGMASS[A_.bild][0], height: IMGMASS[A_.bild][1] } : {}))));
  dd.append(zeile("Messwerte:", A_.messwerte), zeile("Entsorgung und Reinigung:", A_.entsorgung), zeile("Abgabe:", A_.abgabe), zeile("Auswertung:", A_.auswertung));
  return dd;
}

function renderTask(t) {""")
rep('''  const sol = el("div", { class: "sol", id: "sol_" + t.id, hidden: "" }, el("strong", { text: "Musterlösung" }));''',
    '''  if (t.aufloesung) card.append(aufloesungEl(t));
  const sol = el("div", { class: "sol", id: "sol_" + t.id, hidden: "" }, el("strong", { text: "Musterlösung" }));''')

# ---- PDF: Hilfe-Nutzung sichtbar, Vorhersage nicht bewerten, offene Erklärungen bewertet Prof. HOLZER ----
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
    x.pop("besprechen", None)
    TJ.append(x)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = (s[:i] + 'const KEY = "%s";\nconst KAP = "K1.5", THEMA = "Saeuren";\n' % I.KEY
     + "const VSID = " + json.dumps(list(I.VS)[0]) + ";\n"
     + "const ANL = " + json.dumps(dict(I.ANLEITUNG, bild="img/versuch.svg", alt=TD.KARTEN["k5"]["alt"]), ensure_ascii=False) + ";\n"
     + "const KARTEN = " + json.dumps(TD.karte_html_daten(), ensure_ascii=False) + ";\n"
     + "const IMGMASS = " + json.dumps({"img/" + f: bild_mass("img/" + f) for f in sorted(os.listdir(DST + "img")) if f.endswith(".svg")}) + ";\n"
     + "const SIMTITEL = " + json.dumps(SIMS.TITEL, ensure_ascii=False) + ", SIMZEILE = " + json.dumps(SIMS.ZEILE, ensure_ascii=False) + ", SIMHTML = " + json.dumps(SIMS.HTML, ensure_ascii=False).replace("</", "<\\/") + ";\n"
     + "const T = " + json.dumps(TJ, ensure_ascii=False, indent=1) + ";" + s[j:])
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]


def ablauf_daten():
    """Stunden-Ablauf für das Arbeitsblatt (Stephan, 15.11.2026): Wer nur das Arbeitsblatt benutzt, soll trotzdem sehen,
    was in der Stunde gemeinsam passiert (DEMO, Pingpong, Besprechen, Partnercheck) – aus derselben Quelle wie Fahrplan und Lösungsseite."""
    nr_zu_id = {t["nr"]: t["id"] for t in I.T}
    out = {}
    for n, rows in P.STUNDE.items():
        z = []
        for text, minuten, _ohne, art, marke in rows:
            if art in ("org", "reserve"): continue
            t = text
            for pre in ("KURZ KLÄREN: ", "ALLE GEMEINSAM: ", "SELBSTSTUDIUM: ", "BESPRECHEN: ", "PARTNERCHECK: "):
                if t.startswith(pre): t = ("Prof. HOLZER erklärt: " if pre == "KURZ KLÄREN: " else "") + t[len(pre):]
            ziel = None
            if art.startswith("a") and art[1:].isdigit(): ziel = nr_zu_id.get(int(art[1:]))
            if marke == "" and art == "pdf": marke = "ABGABE"
            z.append([marke, t, ziel])
        out[str(n)] = z
    return out


s = s.replace("const GRP = ", "const ABLAUF = " + json.dumps(ablauf_daten(), ensure_ascii=False) + ";\nconst GRP = ", 1)
s = s.replace("const GRP = ", "const BALKEN = " + json.dumps(P.balken(), ensure_ascii=False) + ";\nconst GRP = ", 1)
s = s.replace('T.forEach(t => { const g = t.hl ? "hl" : t.h; if (g !== lastH) { $("#tasks").append(el("div", { class: "grp", text: GRP[g] })); lastH = g; } $("#tasks").append(renderTask(t)); });',
  'T.forEach(t => { const g = t.hl ? "hl" : t.h; if (g !== lastH) { $("#tasks").append(grpEl(g)); lastH = g; } balkenEl("vor", t.nr); $("#tasks").append(renderTask(t)); balkenEl("nach", t.nr); });')
s = s.replace("let lastH = null;", """/* ABCD-Karte (Stephan, 15.11.2026: digital statt Zettel). Die Frage steht am Beamer; jeder tippt A, B, C oder D und hält das Handy hoch.
   Nichts wird gespeichert oder bewertet. */
function abcdAuf() {
  let ov = document.getElementById("abcd");
  if (!ov) {
    ov = el("div", { id: "abcd", role: "dialog", "aria-label": "ABCD-Karte" });
    const wahl = el("div", { class: "abcd-wahl" }), gross = el("button", { type: "button", class: "abcd-gross", hidden: "" });
    ["A", "B", "C", "D"].forEach(b => { const k = el("button", { type: "button", class: "abcd-k abcd-" + b, text: b }); k.addEventListener("click", () => { gross.textContent = b; gross.className = "abcd-gross abcd-" + b; gross.hidden = false; wahl.hidden = true; }); wahl.append(k); });
    gross.addEventListener("click", () => { gross.hidden = true; wahl.hidden = false; });
    const zu = el("button", { type: "button", class: "abcd-zu", text: "Schließen" }); zu.addEventListener("click", () => { ov.hidden = true; });
    ov.append(el("p", { class: "abcd-tipp", text: "Antippen – dann Handy hochhalten. Nochmal tippen = neu wählen." }), wahl, gross, zu);
    document.body.append(ov);
  }
  ov.hidden = false; ov.querySelector(".abcd-gross").hidden = true; ov.querySelector(".abcd-wahl").hidden = false;
}
/* Balken zwischen den Aufgaben (Stephan 15.11.2026): Wer nur Aufgaben macht, läuft direkt auf »Jetzt DEMO …« zu. */
function balkenEl(wo, nr) {
  (BALKEN[wo][String(nr)] || []).forEach(([m, txt]) => {
    const b = el("div", { class: "phbalken" + (m ? " m-" + m : ""), role: "note" });
    b.append(el("span", { class: "phm", text: m || "JETZT" }), el("span", { text: txt }));
    if (/ABCD-Karte/.test(txt)) { const k = el("button", { type: "button", class: "phabcd", text: "ABCD-Karte" }); k.addEventListener("click", abcdAuf); b.append(k); }
    $("#tasks").append(b);
  });
}
function grpEl(g) {
  const box = el("div", { class: "grpbox" }); box.append(el("div", { class: "grp", text: GRP[g] }));
  const z = ABLAUF[String(g)]; if (!z) return box;
  const ol = el("ol", { class: "ablauf" });
  z.forEach(([m, txt, ziel]) => {
    const li = el("li", { class: m && m !== "SELBSTSTUDIUM" && m !== "ABGABE" ? "gem" : "" });
    if (m) li.append(el("span", { class: "abm m-" + m, text: m }));
    if (ziel) { const a = el("a", { href: "#card_" + ziel, text: txt }); li.append(a); } else li.append(el("span", { text: txt }));
    ol.append(li);
  });
  box.append(el("p", { class: "ablaufk", text: "So läuft die Stunde. Fett = mit der ganzen Klasse bzw. in der Gruppe (BESPRECHEN, DEMO, VERSUCH, PARTNERCHECK):" }), ol);
  const kb = el("button", { type: "button", class: "abcdbtn", text: "ABCD-Karte öffnen – für »Weißt du noch?« und Vermutungen" });
  kb.addEventListener("click", abcdAuf); box.append(kb);
  return box;
}
let lastH = null;""", 1)

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
.aufl { margin-top: 10px; display: grid; gap: 8px; }
.marke { font-size: 13px; font-weight: 700; color: #fff; background: #2E7D8C; border-radius: 999px; padding: 2px 10px; margin-left: 4px; }
.marke.m-VERSUCH { background: #A33A2B; } .marke.m-SELBSTSTUDIUM { background: #2E7D8C; }
.vsid { font-weight: 700; color: #A33A2B; margin: 6px 0; }
.qimg img { width: 100%; height: auto; border: 1px solid #D3DCC2; border-radius: 10px; background: #fff; }
.anl { border: 3px solid #A33A2B; border-radius: 14px; background: #FBF1EE; padding: 10px 14px; margin: 10px 0; display: grid; gap: 6px; }
.anl > summary { cursor: pointer; font-weight: 700; color: #A33A2B; font-size: 18px; min-height: 44px; display: flex; align-items: center; }
.anl p, .anl li { font-size: 17px; line-height: 1.45; margin: 2px 0; } .anl ol, .anl ul { margin: 2px 0 4px; padding-left: 22px; }
.anl h3 { margin: 10px 0 2px; font-size: 19px; color: #3B4A2F; }
.anl .q { font-weight: 700; }
.anl .hint { font-size: 16px; color: #5E6652; margin: 2px 0; } .anl .hint b { color: #3B4A2F; }
.anl .warn { background: #F6E3DF; border-left: 4px solid #8C3B2E; border-radius: 8px; padding: 10px 12px; color: #8C3B2E; font-size: 16px; }
.anl .mat { display: grid; grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); gap: 8px; }
.anl .matitem { display: grid; gap: 4px; justify-items: center; text-align: center; font-size: 15px; background: #EEF2E6; border-radius: 10px; padding: 8px; }
.anl .matitem img { width: 72px; height: auto; }
.anl .steps { margin: 0; padding-left: 22px; display: grid; gap: 4px; }
.grpbox { background: #fff; border: 2px solid #D3DCC2; border-radius: 14px; padding: 10px 14px; margin: 14px 0 6px; }
.grpbox .grp { margin-top: 0; color: #3B4A2F; }
.ablaufk { margin: 6px 0 4px; font-size: 15px; color: #5E6652; }
ol.ablauf { margin: 0; padding-left: 22px; display: grid; gap: 6px; font-size: 16px; line-height: 1.35; }
ol.ablauf li.gem { font-weight: 700; color: #3B4A2F; }
ol.ablauf a { color: #2E7D8C; font-weight: 700; }
.abm { display: inline-block; font-size: 12px; font-weight: 800; letter-spacing: .05em; border-radius: 999px; padding: 1px 8px; margin-right: 6px; color: #fff; background: #5E6652; vertical-align: 1px; }
.abm.m-DEMO { background: #2E7D8C; } .abm.m-VERSUCH { background: #8C3B2E; } .abm.m-BESPRECHEN, .abm.m-PARTNERCHECK { background: #3B4A2F; }
.abm.m-SELBSTSTUDIUM { background: #E8DDBB; color: #6B4F00; } .abm.m-ABGABE { background: #7FA83A; }
.phbalken { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; margin: 14px 0; padding: 10px 14px; border-radius: 12px; border-left: 8px solid #3B4A2F; background: #EEF1E6; font-size: 17px; line-height: 1.4; font-weight: 600; color: #1F2A1C; }
.phbalken .phm { font-size: 12.5px; font-weight: 800; letter-spacing: .06em; color: #fff; background: #3B4A2F; border-radius: 6px; padding: 2px 8px; }
.phbalken.m-DEMO { border-color: #2E7D8C; background: #E6F1F3; } .phbalken.m-DEMO .phm { background: #2E7D8C; }
.phbalken.m-VERSUCH { border-color: #8C3B2E; background: #F6E9E6; } .phbalken.m-VERSUCH .phm { background: #8C3B2E; }
.phbalken.m-SELBSTSTUDIUM { border-color: #B8962E; background: #F7F1DE; } .phbalken.m-SELBSTSTUDIUM .phm { background: #8A6400; }
.phabcd { margin-left: auto; min-height: 40px; font: inherit; font-size: 15px; font-weight: 700; border-radius: 999px; border: 2px solid #2E7D8C; background: #fff; color: #2E7D8C; padding: 4px 14px; cursor: pointer; }
.abcdbtn { margin-top: 10px; width: 100%; min-height: 48px; font: inherit; font-weight: 700; font-size: 16px; border-radius: 12px; border: 2px solid #3B4A2F; background: #fff; color: #3B4A2F; cursor: pointer; }
#abcd { position: fixed; inset: 0; z-index: 200; background: #11150F; display: flex; flex-direction: column; padding: 12px; gap: 10px; }
#abcd[hidden] { display: none; }
.abcd-tipp { color: #DDE3D2; margin: 0; text-align: center; font-size: 16px; }
.abcd-wahl { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.abcd-wahl[hidden] { display: none; }
.abcd-k, .abcd-gross { border: 0; border-radius: 18px; color: #fff; font: 800 18vmin/1 "Source Sans 3", system-ui, sans-serif; cursor: pointer; }
.abcd-gross { flex: 1; font-size: 60vmin; }
.abcd-gross[hidden] { display: none; }
.abcd-A { background: #C0392B; } .abcd-B { background: #2A5C8C; } .abcd-C { background: #3E8E41; } .abcd-D { background: #D99A00; }
.abcd-zu { min-height: 52px; font: inherit; font-weight: 700; font-size: 18px; border-radius: 12px; border: 0; background: #fff; color: #3B4A2F; }
.simlink { display: grid; gap: 4px; margin: 8px 0; } .simlink .btn { justify-self: start; text-decoration: none; }
.pegel { border: 3px solid #A33A2B; border-radius: 14px; background: #FBF1EE; padding: 12px 14px; display: grid; gap: 8px; margin: 10px 0; }
.pgh { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; font-size: 19px; }
.pgz { font-size: 44px; font-weight: 700; color: #3B4A2F; text-align: center; font-variant-numeric: tabular-nums; }
.pgbar { height: 14px; border-radius: 7px; background: #E4E7DD; overflow: hidden; } .pgbar span { display: block; height: 100%; width: 2%; background: linear-gradient(90deg,#7FA83A,#E8C02E,#D9772B,#A33A2B); }
.pgi { margin: 0; font-size: 17px; }
.pgbtns { display: flex; gap: 8px; flex-wrap: wrap; } .pgbtns .btn { min-height: 44px; }
.pgerg { display: grid; gap: 8px; font-size: 18px; background: #fff; border-radius: 10px; padding: 10px; }""")
rep('KAP + " Zeit-Einteilung und Epochen – Aufgaben"', '"K1.5 Säuren und Basen – Arbeitsblatt"')
rep('clean("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen · Schulbuch S. 13–14")', 'clean("' + I.EYEBROW + " · Schulbuch S. 53–61, 65" + '")')
rep('d.text("Epochen-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Stunde 1 und 2): Aufgabe "', '"Noch offen (Pflicht): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–10 bearbeitet."', '"Alle Pflicht-Aufgaben bearbeitet."')
rep('el("span", { class: tagCls, text: t.tag })),',
    'el("span", { class: tagCls, text: t.tag }), t.zeit ? el("span", { class: "tag zeit", text: "ca. " + t.zeit + " min" }) : null, t.marke ? el("span", { class: "marke m-" + t.marke, text: t.marke }) : null),')
rep('const tagCls = t.tag.startsWith("Stunde") ?', 'const tagCls = (t.tag.startsWith("Stunde") || t.tag.startsWith("Vorhersage")) ?')
rep('s = String(s).replace(/⊙/g, "(Punkt)")', 's = String(s).replace(/≈/g, "ca.").replace(/⊙/g, "(Punkt)")')
rep(".pill.theory { background: var(--theory); }", ".pill.theory { background: var(--theory); } .tag.zeit { color: var(--teal); border-color: var(--teal); }")
s = s.replace("26-27-3BK-K1.3-Epochen-TH-Handy-v1", I.KEY)
s = s.replace("PBGW 3BK", "NAWI 2AB").replace("3BK · Start", "2AB · Start")
# Musterlösungen erst, wenn die letzte Pflichtaufgabe (Aufgabe 9) bearbeitet ist
rep('''  const b = $("#solbtn"); if (b) b.hidden = !S.pdfDone || S.solSeen;''',
    '''  const b = $("#solbtn"); if (b) b.hidden = !S.pdfDone || S.solSeen || !isDone(T.find(t => t.id === "a6"));''')
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Epochen", "Zeit-Einteilung", "3BK", "Kräfte", "Kraefte", "Akustik", "Pegelmesser", "4AB"]:
    assert bad not in _plain, (bad, re.findall(r".{60}" + bad + r".{20}", _plain)[:3])
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)



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


def bild_tag(src, alt, cls=""):
    k = f' class="{cls}"' if cls else ""
    wh = bild_mass(src)
    k += f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
    return (f'<picture class="bildzoom"><img{k} src="{src}" alt="{esc(alt)}" loading="lazy"></picture>'
            '<p class="zoomhint">Bild antippen – dann wird es groß.</p>')


def figure(src, alt, cap):
    return f'<figure class="fig">{bild_tag(src, alt)}<figcaption>{md(cap)}</figcaption></figure>'


def karte_block(v):
    f = ""
    if v["formeln"]:
        f = '<table class="tkf">' + "".join(f'<tr><td class="z">{md(z)}</td><td>{md(bed)}</td><td class="e">{md(e)}</td></tr>' for z, bed, e in v["formeln"]) + "</table>"
    return ('<div class="tkarte-s">'
            f'<div class="tkh"><span class="tkn">Theorie-Karte</span><b>{esc(v["titel"])}</b><span class="tkb">{esc(v["buch"])}</span></div>'
            + bild_tag(v["bild"], v["alt"], "tkimg") + "".join(f"<p>{md(x)}</p>" for x in v["satz"]) + f + "</div>")





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
    if k == "buch": return f'<div class="buch"><span class="bicon">Buch</span><p>{md(b[1])}</p></div>'
    if k == "karte": return karte_block(b[1])
    if k == "gemeinsam": return f'<div class="gem"><span class="gicon">BESPRECHEN</span><p>{md(b[1])}</p></div>'
    if k == "sim": return SIMS.HTML[b[1]]
    if k == "extern":   # externe Simulation (z. B. PhET) als Link – öffnet in neuem Tab, nichts von fremden Servern eingebettet
        return (f'<div class="sim"><div class="simh"><span class="tkn">Simulation</span><b>{esc(b[1])}</b></div><p class="simt">{md(b[3])}</p>'
                f'<p class="simt">{esc(b[4])}</p><a class="btn" style="justify-self:start;text-decoration:none" href="{esc(b[2])}" target="_blank" rel="noopener">Simulation öffnen</a></div>')
    if k == "demo":
        d = I.DEMOS[b[1]]
        return (f'<div class="dbox"><div class="vhead"><span class="dnr">DEMO {esc(b[1])}</span><span class="vtag">Stunde {d["stunde"]}</span></div>'
                f'<p><strong>{esc(d["titel"])}</strong></p><p>{md(b[2])}</p></div>')
    if k == "versuch":
        v = I.VS[b[1]]
        return (f'<div class="vbox"><div class="vhead"><span class="vnr">VERSUCH {esc(b[1])}</span><span class="vtag">KERN · Stunde {v["stunde"]}</span></div>'
                f'<p><strong>{esc(v["titel"])}</strong></p><p>{md(b[2])}</p><a class="btn small" href="{b[3]}">Zum Versuch im Arbeitsblatt (Aufgabe {v["aufgabe"]})</a></div>')
    raise ValueError(k)


def render(item):
    if isinstance(item, tuple) and item[0] == "jetzt": return jetzt(item[1], item[2])
    return slide(item["title"], "".join(block(b) for b in item["blocks"]), item["pill"], item["id"])


def _teil(pid, eyebrow, title, items):
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
                                                      slide("Alles auf einen Blick", karte_block(TD.KARTEN["k8"])),
                                                      slide("Kann ich das?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [render(x) for x in TD.SCHNELLE]))

toc = "".join(f'<a href="#{p[0]}">{TD.TOCLAB[p[0]]}</a>' for p in PARTS) + '<a href="aufgaben.html">Arbeitsblatt</a>'   # Kapitel-Menü: werkzeug/kapitelmenue.js
body = "".join(f'<section class="part" id="{p[0]}"><div class="band"><div class="eyebrow">{esc(p[1])}</div><h2>{esc(p[2])}</h2></div>{"".join(p[3])}</section>' for p in PARTS)
bt = open(os.path.join(WZ, "vorlagen", "build_theorie.py"), encoding="utf-8").read()
tcss = bt[bt.index("<style>"):bt.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
tcss = tcss.replace("</style>", """.merke { background: var(--olive); color: #fff; border-radius: 12px; padding: 12px 14px; }
.merke strong { color: #C9D8A8; }
ol.goals, ul.pts { margin: 0; padding-left: 24px; display: grid; gap: 6px; }
details.reveal { border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
details.reveal summary { cursor: pointer; font-weight: 700; color: #D9772B; min-height: 44px; display: flex; align-items: center; }
details.reveal p { margin: 8px 0 0; }
.stopq { display: grid; gap: 6px; } .stopq + .stopq { margin-top: 10px; }
.ziel { border: 1px solid #D3DCC2; border-radius: 12px; padding: 10px 12px; display: grid; gap: 6px; } .ziel p { margin: 0; }
.chips { display: flex; gap: 8px; flex-wrap: wrap; }
.chip { font: inherit; font-size: 16px; font-weight: 700; color: #3B4A2F; background: #fff; border: 2px solid #D3DCC2; border-radius: 999px; padding: 6px 14px; cursor: pointer; min-height: 44px; }
.chip[aria-pressed="true"][data-v="sicher"] { background: #E6F0D3; border-color: #7FA83A; }
.chip[aria-pressed="true"][data-v="fast"] { background: #FFF1D6; border-color: #D9772B; }
.chip[aria-pressed="true"][data-v="noch nicht"] { background: #F6E3DF; border-color: #8C3B2E; }
.chip:focus-visible { outline: 3px solid #2E7D8C; outline-offset: 2px; }
.jetzt { display: block; text-align: center; background: #7FA83A; color: #fff; font-weight: 700; font-size: 18px; text-decoration: none; border-radius: 12px; padding: 12px 16px; }
.slide[id], .part { scroll-margin-top: 64px; }
.fig { margin: 0; display: grid; gap: 6px; justify-items: center; }
.fig img { max-width: 100%; height: auto; border-radius: 10px; border: 1px solid #D3DCC2; background: #fff; }
.fig figcaption { font-size: 15px; color: #5E6652; text-align: center; }
.vbox, .dbox { border: 2px solid #A33A2B; border-radius: 12px; padding: 10px 14px; display: grid; gap: 6px; background: #FBF1EE; }
.dbox { border-color: #2A5C8C; background: #EEF3F8; }
.vbox p, .dbox p { margin: 0; }
.vhead { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.vnr, .dnr { font-weight: 700; color: #fff; background: #A33A2B; border-radius: 8px; padding: 2px 10px; } .dnr { background: #2A5C8C; }
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
<title>Säuren und Basen – Theorie</title>
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
    <p>Du arbeitest im <strong>Arbeitsblatt</strong> – dort stehen alle Aufgaben, die Versuche und zu jeder Aufgabe eine Theorie-Karte. Diese Seite brauchst du,
    wenn du mehr wissen willst, und vor dem Test.</p>
    <div class="btns"><a class="btn" href="aufgaben.html">Arbeitsblatt öffnen</a></div>
  </article>
</section>
{body}
<section class="next" id="weiter">
  <div class="eyebrow">Weiter geht's</div>
  <h2>Jetzt bist du dran</h2>
  <div class="btns"><a class="btn" href="aufgaben.html">Arbeitsblatt öffnen</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch Naturwissenschaften HAK 2 Chemie (Trauner) S. 53–61 und 65. Alle Grafiken selbst gezeichnet. <a href="../">Klassenübersicht 2AB</a></p>
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

# ================================================================ Bildlupe (wie K2.1 Kräfte)
ZOOM = """
<style>
.bildzoom { display: block; cursor: zoom-in; }
.bildzoom img { width: 100%; height: auto; max-width: 560px; display: block; margin: 0 auto; }
/* Handy: Grafiken in Theorie-Karten und Abbildungen fast über die ganze Bildschirmbreite (Stephan, 14.11.2026) */
@media (max-width: 600px) {
  .tkarte .bildzoom, .tkarte-s .bildzoom, figure.fig .bildzoom, .anl .bildzoom { margin-left: calc(50% - 50vw + 6px); margin-right: calc(50% - 50vw + 6px); }
}
/* Aufgabenkopf: Marken umbrechen statt über den Kartenrand hinaus (Samsung, 360 px) */
.card { grid-template-columns: minmax(0, 1fr); }
.head .nr { flex-wrap: wrap; row-gap: 6px; min-width: 0; }
.head .nr > * { white-space: nowrap; }
p.zoomhint { margin: 2px 0 0; font-size: 14px; color: #5E6652; }
@media (hover: hover) and (min-width: 900px) { p.zoomhint { display: none; } }
#lupe[hidden] { display: none; }
#lupe { position: fixed; inset: 0; z-index: 9999; background: rgba(20,24,18,.96); display: flex; align-items: center; justify-content: center; overflow: auto; -webkit-overflow-scrolling: touch; touch-action: pinch-zoom; }
#lupe img { max-width: 100%; max-height: 100%; object-fit: contain; background: #fff; border-radius: 8px; }
#lupe { box-sizing: border-box; padding: 66px 6px 6px; }   /* Knöpfe »Drehen« und »Schließen« verdecken das Bild nicht mehr */
#lupe .zu, #lupe .dreh { position: fixed; top: 10px; z-index: 2; font: inherit; font-size: 17px; font-weight: 700; min-height: 44px; padding: 8px 16px; border-radius: 999px; border: 0; background: #fff; color: #2C3424; cursor: pointer; }
#lupe .zu { right: 12px; } #lupe .dreh { left: 12px; }
#lupe.quer img { width: auto; height: auto; max-width: calc(100vh - 78px); max-height: calc(100vw - 12px); transform: rotate(90deg); }
</style>
<div id="lupe" hidden role="dialog" aria-modal="true" aria-label="Bild groß">
  <button type="button" class="dreh">Drehen</button><button type="button" class="zu">Schließen</button><img alt="">
</div>
<script>
(function () {
  var lupe = document.getElementById("lupe"), gross = lupe.querySelector("img");
  function auf(bild) { gross.src = bild.currentSrc || bild.src; gross.alt = bild.alt || ""; lupe.classList.remove("quer"); lupe.hidden = false; document.body.style.overflow = "hidden"; lupe.querySelector(".zu").focus(); }
  function zu() { lupe.hidden = true; gross.removeAttribute("src"); document.body.style.overflow = ""; }
  document.addEventListener("click", function (ev) {
    var p = ev.target.closest && ev.target.closest(".bildzoom, figure.fig, .qimg");
    if (p && !lupe.contains(ev.target)) { var b = p.querySelector("img") || ev.target; if (b.tagName === "IMG") { ev.preventDefault(); auf(b); } }
  });
  lupe.querySelector(".zu").addEventListener("click", zu);
  lupe.querySelector(".dreh").addEventListener("click", function () { lupe.classList.toggle("quer"); });
  lupe.addEventListener("click", function (ev) { if (ev.target === lupe) zu(); });
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape" && !lupe.hidden) zu(); });
})();
</script>
"""
import shutil
os.makedirs(DST + "vs-img", exist_ok=True)
for _n in sorted({ic for _t, ic in I.ANLEITUNG["mat"] + I.ANLEITUNG["station"]}):
    shutil.copyfile(os.path.join(ROOT, "werkzeug", "icons", _n + ".png"), DST + "vs-img/i_" + _n + ".png")
for f in ["theorie.html", "aufgaben.html"]:
    t = open(DST + f, encoding="utf-8").read()
    if "window.SIMINIT" not in t:
        i = t.rfind("</body>")
        t = t[:i] + "<style>" + SIMS.CSS + "</style>" + SIMS.JS + t[i:]
    if 'id="lupe"' not in t:
        i = t.rfind("</body>")
        t = (t[:i] + ZOOM + t[i:]) if i > 0 else t.replace("</html>", ZOOM + "</html>")
        open(DST + f, "w", encoding="utf-8").write(t)

for f in ["theorie.html", "aufgaben.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
