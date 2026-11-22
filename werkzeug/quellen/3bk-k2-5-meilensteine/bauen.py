"""Handy-Seiten PBGW 3BK · K2.1–5.4 Meilensteine, Hochkulturen, Athen und Rom bauen (Theorie-Seite, Arbeitsblatt, Quiz). Keine Versuchsseite (keine Versuche in PBGW).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3bk-k2-5-meilensteine/skizzen.py  und danach  python3 werkzeug/quellen/3bk-k2-5-meilensteine/bauen.py
Arbeitsblatt-Grundlage: eingefrorene Kopie vorlage_aufgaben.html (= 3bk-pbgw/k1-3-epochen/aufgaben.html vom 25.10.2026), Anpassungen wie 1AB K1.4 v3
(offene Erklärungen man, freiwillige Felder opt) und neu: Datentabelle bei der Aufgabe (t.tab).
Danach: python3 werkzeug/quellen/3bk-k2-5-meilensteine/regeln.py und python3 werkzeug/nach_dem_bauen.py"""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
import plan as PL
import theorie_daten as TD
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
TITLE = "Meilensteine – Arbeitsblatt"   # Standard 11.11.2026: die Seite heißt für die Kadetten überall »Arbeitsblatt«
rep("<title>Epochen-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Epochen-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Epochen-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
def _ber(nrs):
    out, a = [], None
    for k, n in enumerate(nrs):
        if a is None: a = n
        if k + 1 == len(nrs) or nrs[k + 1] != n + 1: out.append(str(a) if a == n else "%d–%d" % (a, n)); a = None
    return ", ".join(out)
_TL = {1: "Stunde 1", 2: "Stunde 2", 3: "Stunde 3"}
INTRO = ("      <li><b>Pflicht</b> – " + " · ".join("<b>%s</b>: %s" % (_TL[h], _ber([t["nr"] for t in I.T if t["h"] == h and t["tag"] not in ("Zusatz", "Selbsteinschätzung")])) for h in range(1, 4))
         + ". Welche Stunde heute dran ist, sagt dir Prof. HOLZER – tipp sie im <b>Fahrplan</b> oben an.</li>\n"
         "      <li><b>Zusatz</b> für Schnelle: " + _ber([t["nr"] for t in I.T if not t["h"]]) + " – für alle, die früher fertig sind. Es gibt <b>keine Hausübung</b>.</li>")
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Hier arbeitest du. Oben bei jeder Stunde steht <b>»So läuft die Stunde«</b> – dort siehst du, was gemeinsam passiert und wann du dran bist.</li>
      """ + INTRO + """
      <li>Bei jeder Aufgabe steht, wie lange sie ungefähr dauert. Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Du brauchst mehr Erklärung? Der <a href="theorie.html">Theorieteil</a> ist zum Nachschlagen da; bei jeder Aufgabe steht, wo es dort steht.</li>
      <li>Deine Antworten bleiben am Handy gespeichert. Am Ende erstellst du eine <b>PDF</b> und lädst sie in <b>LMS</b> hoch.</li>
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
  /* Skizzen-Aufgaben: die Zeichnung (Foto) bewertet immer die Lehrkraft – nie pauschal »Richtig!« (ChatGPT-Bericht v2, Befund 3) */
  if (t.type === "sketch") { const fo = !!(S.a[t.id] || {}).foto; parts.push({ key: "foto", label: "Zeichnung (Foto)", kind: "foto", man: true, filled: fo, ok: fo, hits: [] }); }
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
    if (p.kind === "foto") { fb.append(el("div", { text: p.filled ? "Zeichnung: Foto ist da – sie bewertet die Lehrkraft." : "Zeichnung: Das Foto deiner Zeichnung fehlt noch." })); return; }
    if (!p.filled) { fb.append(el("div", { text: pre + "Deine Erklärung fehlt noch." })); return; }
    const da = p.hits.filter(h => h[1]).map(h => h[0]), fehlt = p.hits.filter(h => !h[1]).map(h => h[0]);
    fb.append(el("div", { text: pre + "Schreibhilfe – " + (da.length ? "gefunden: " + da.join(", ") : "noch keines der erwarteten Stichwörter") + (fehlt.length ? " · vielleicht fehlt noch: " + fehlt.join(", ") + " (eine richtige Umschreibung zählt auch)" : "") + "." }));
  });
  if (man.some(p => p.kind !== "foto")) fb.append(el("div", { text: "Ob deine Erklärung fachlich stimmt, bewertet die Lehrkraft. Lies sie noch einmal durch." }));
  if (t.tip && (!r.ok || man.some(p => p.filled && p.hits.some(h => !h[1])))) fb.append(el("div", {}, "Tipp: Lies nochmal ", el("a", { href: t.tip[1], text: t.tip[0] }), "."));
}""" + s[_j:]
rep('    let st = "selbst bewerten";\n    if (ev) {', '    let st = "selbst bewerten";\n    if (ev && ev.man) { const au = ev.parts.filter(p => !p.man); st = (au.length ? "automatisch geprüft: " + (au.every(p => p.ok) ? "richtig" : "noch nicht richtig") + " · " : "") + (ev.parts.some(p => p.man && p.kind === "foto") ? (ev.parts.some(p => p.kind === "foto" && p.filled) ? "Zeichnung" : "Zeichnung (Foto fehlt)") + (ev.parts.some(p => p.man && p.kind !== "foto") ? " und Erklärung" : "") : "Erklärung") + ": bewertet die Lehrkraft"; }\n    else if (ev) {')
rep("(ev && ev.ok ? [70, 110, 40] : muted)", "(ev && ev.ok && !ev.man ? [70, 110, 40] : muted)")
s = s[:i] + 'const KEY = "%s";\nconst KAP = "%s", THEMA = "Meilensteine";\nconst T = ' % (I.KEY, I.KAP) + json.dumps(I.T, ensure_ascii=False, indent=1) + ";" + s[j:]
rep(".fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }", ".fb.no { background: #F6E3DF; border: 2px solid #8C3B2E; }\n.fb.info { background: #E8F1F3; border: 2px solid #2E7D8C; }")
rep('KAP + " Zeit-Einteilung und Epochen – Aufgaben"', '"K2.1–5.4 Meilensteine – Arbeitsblatt"')
rep('clean("PBGW · 3BK · K1.3–1.4 Zeit-Einteilung und Epochen · Schulbuch S. 13–14")', 'clean("PBGW · 3BK · K2.1–5.4 Meilensteine · Schulbuch S. 23–44 und 105–118")')
rep('d.text("Epochen-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Stunde 1 und 2): Aufgabe "', '"Noch offen (Pflicht): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–10 bearbeitet."', '"Alle Pflicht-Aufgaben bearbeitet."')
# Zeit je Aufgabe und rote Kennzeichnung »Versuch im Buch«
rep('el("span", { class: tagCls, text: t.tag })),', 'el("span", { class: tagCls, text: t.tag }), t.zeit ? el("span", { class: "tag zeit", text: "ca. " + t.zeit + " min" }) : null),')
rep('const tagCls = t.tag.startsWith("Stunde") ?', 'const tagCls = (t.tag.startsWith("Stunde") || t.tag.startsWith("Teil")) ?')
# K1.4–1.5: Datentabelle direkt bei der Aufgabe (t.tab, erste Zeile = Kopf) und Hinweis darunter (t.tabnote)
rep('  if (t.img) card.append(el("div", { class: "qimg" }, el("img", { src: t.img, alt: "Abbildung zu Aufgabe " + t.nr })));',
    '  if (t.img) card.append(el("div", { class: "qimg" }, el("img", { src: t.img, alt: "Abbildung zu Aufgabe " + t.nr })));\n'
    '  if (t.tab) { const tb = el("table", { class: "dtab" }); t.tab.forEach((r, i) => tb.append(el("tr", {}, ...r.map((c, j) => el(i === 0 || j === 0 ? "th" : "td", { text: c }))))); '
    'card.append(el("div", { class: "dwrap" }, tb)); if (t.tabnote) card.append(el("p", { class: "hint dnote", text: t.tabnote })); }')
rep(".fb.info { background: #E8F1F3; border: 2px solid #2E7D8C; }", ".fb.info { background: #E8F1F3; border: 2px solid #2E7D8C; }\n"
    ".dwrap { overflow-x: auto; margin: 6px 0; } .dtab { border-collapse: collapse; width: 100%; font-size: 14px; } .dtab th, .dtab td { border: 1px solid #D3DCC2; padding: 5px 6px; text-align: left; vertical-align: top; } "
    ".dtab tr:first-child th { background: #3B4A2F; color: #fff; } .dtab td { text-align: right; white-space: nowrap; } .dtab tr:nth-child(odd) td { background: #F4F7EE; } .dnote { font-weight: 700; color: #8C3B2E; }")
s = s.replace('el("label", { class: "lbl", text: "Deine Skizze (Foto)" })', 'el("label", { class: "lbl", text: "Foto (Mini-Whiteboard oder Papier)" })')
s = s.replace('"Foto der Heftskizze aufnehmen"', '"Foto aufnehmen"')
# √ und ≈ kennt die PDF-Schrift nicht – vor dem Filtern ersetzen
rep('s = String(s).replace(/⊙/g, "(Punkt)")', 's = String(s).replace(/√/g, "Wurzel ").replace(/≈/g, "ca.").replace(/⊙/g, "(Punkt)")')
rep('el("span", { class: "pill" + (t.own ? " theory" : ""), text: t.src })', 'el("span", { class: "pill" + (t.src.startsWith("Versuch im Buch") ? " versuch" : (t.own ? " theory" : "")), text: t.src })')
rep(".pill.theory { background: var(--theory); }", ".pill.theory { background: var(--theory); } .pill.versuch { background: #A33A2B; } .tag.zeit { color: var(--teal); border-color: var(--teal); }")
# ---- Kompetenz-Chips (Skill bhak-kompetenzmodell, 20.11.2026): Buchstabe und Plus immer sichtbar, Farbe nur zusätzlich ----
rep('  card.append(el("h2", { text: t.title }));',
    '  card.append(el("h2", {}, ...(t.hd ? [el("span", { class: "kchip k" + t.hd, title: KOMP_TITEL[t.hd] + (t.niveau === 2 ? " · Vertiefung" : " · Grundlegendes"), text: t.hd + " " + (t.niveau === 2 ? "++" : "+") }), " "] : []), t.title));')
rep('    txt("Aufgabe " + t.nr + ": " + t.title, 13, "bold", olive, M, CW - 50);',
    '    txt("Aufgabe " + t.nr + ": " + (t.hd ? "[" + t.hd + " " + (t.niveau === 2 ? "++" : "+") + "] " : "") + t.title, 13, "bold", olive, M, CW - 50);')
rep("</style>", ".kchip{display:inline-block;font:700 .78em/1.5 'Source Sans 3',sans-serif;padding:0 .45em;border-radius:6px;margin-right:.25em;vertical-align:.12em;border:1.5px solid currentColor;white-space:nowrap}"
    ".kchip.kA{color:#1f5fa8;background:#e8f0fa}.kchip.kB{color:#b3261e;background:#fbeaea}.kchip.kC{color:#111;background:#ececec}"
    "@media (prefers-color-scheme:dark){.kchip.kC{color:#eee;background:#333}}</style>")
s = s.replace("const T = ", "const KOMP_TITEL = {A: \"Verstehen und wiedergeben\", B: \"Anwenden und analysieren\", C: \"Begründen und bewerten\"};\nconst T = ", 1)

i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]


# ---- Stundenablauf, Balken, ABCD-Karte und Sicherung (Standard 15.11.2026) ----
def ablauf_daten():
    """Kasten »So läuft die Stunde« im Arbeitsblatt: Wer nur Aufgaben macht, soll trotzdem sehen, was gemeinsam passiert
    (DEMO, Test, Erklären, Sicherung) – aus derselben Quelle wie Fahrplan, Präsentation und Lösungsseite."""
    nr_zu_id = {t["nr"]: t["id"] for t in I.T}
    out = {}
    for n, rows in PL.STUNDE.items():
        z = []
        for text, _minuten, _ohne, art, marke in rows:
            if art in ("org", "reserve"): continue
            t = text
            for pre in ("KURZ KLÄREN: ", "SELBSTSTUDIUM: ", "BESPRECHEN: ", "ALLE GEMEINSAM: ", "DEMO "):
                if t.startswith(pre): t = ("Prof. HOLZER erklärt: " if pre == "KURZ KLÄREN: " else "") + t[len(pre):]   # Marke steht schon als Chip davor
            ziel = None
            m = re.match(r"a(\d+)$", art)
            if m: ziel = nr_zu_id.get(int(m.group(1)))
            if marke == "" and art == "pdf": marke = "ABGABE"
            z.append([marke, t, ziel])
        out[str(n)] = z
    return out


s = s.replace("const GRP = ", "const ABLAUF = " + json.dumps(ablauf_daten(), ensure_ascii=False) + ";\nconst GRP = ", 1)
s = s.replace("const GRP = ", "const BALKEN = " + json.dumps(PL.balken(), ensure_ascii=False) + ";\nconst GRP = ", 1)
GESICHERT = {str(nr): ", ".join(b + ")" for b in PL.buchstaben(nr, ids)) for n in PL.SICHERUNG for nr, ids in PL.SICHERUNG[n]["teile"]}
s = s.replace("const GRP = ", "const GESICHERT = " + json.dumps(GESICHERT, ensure_ascii=False) + ";\nconst GRP = ", 1)
rep('T.forEach(t => { const g = t.hl ? "hl" : t.h; if (g !== lastH) { $("#tasks").append(el("div", { class: "grp", text: GRP[g] })); lastH = g; } $("#tasks").append(renderTask(t)); });',
    'T.forEach(t => { const g = t.hl ? "hl" : t.h; if (g !== lastH) { $("#tasks").append(grpEl(g)); lastH = g; } balkenEl("vor", t.nr); const kc = renderTask(t); gesichertEl(kc, t.nr); $("#tasks").append(kc); balkenEl("nach", t.nr); });')
rep("let lastH = null;", """/* ABCD-Karte (Standard 15.11.2026: digital statt Zettel hochhalten). Die Frage steht am Beamer; jeder tippt A, B, C oder D
   und hält das Handy hoch. Nichts wird gespeichert, nichts bewertet. */
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
/* Hinweis auf der Aufgabe: Diese Teile werden am Ende der Stunde gemeinsam gesichert. */
function gesichertEl(card, nr) {
  const g = GESICHERT[String(nr)]; if (!g) return;
  const p = el("p", { class: "gesichert" }); p.append(el("span", { class: "phm", text: "SICHERUNG" }), el("span", { text: "Am Ende der Stunde sichern wir gemeinsam: " + g + "." }));
  const h = card.querySelector(".head"); if (h && h.nextSibling) card.insertBefore(p, h.nextSibling); else card.append(p);
}
/* Balken zwischen den Aufgaben: Wer nur Aufgaben macht, läuft direkt auf »Jetzt DEMO …« zu. */
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
    if (ziel) { li.append(el("a", { href: "#card_" + ziel, text: txt })); } else li.append(el("span", { text: txt }));
    ol.append(li);
  });
  box.append(el("p", { class: "ablaufk", text: "So läuft die Stunde. Fett = mit der ganzen Klasse (BESPRECHEN, DEMO, GRUPPENARBEIT, DISKUSSION):" }), ol);
  if (z.some(([m]) => m === "SELBSTSTUDIUM")) box.append(selbstHilfe());
  const kb = el("button", { type: "button", class: "abcdbtn", text: "ABCD-Karte öffnen – für »Weißt du noch?« und Vermutungen" });
  kb.addEventListener("click", abcdAuf); box.append(kb);
  return box;
}
/* Was heißt SELBSTSTUDIUM? (Standard 22.11.2026) – steht überall dort, wo die Marke vorkommt. */
function selbstHilfe() {
  const d = el("details", { class: "selbsth" });
  d.append(el("summary", { text: "Was heißt Selbststudium?" }));
  const ul = el("ul");
  ["Lies den angegebenen Abschnitt im Buch (die Seite steht dabei) oder in der Theorie ganz durch.",
   "Markiere die wichtigsten Stellen: Fachbegriffe, Definitionen, Zahlen.",
   "Schreib dir Stichworte, eine kleine Skizze oder offene Fragen in die Mappe.",
   "Erst dann die Aufgaben dazu lösen. Offene Fragen in der Stunde an Prof. HOLZER."].forEach(t => ul.append(el("li", { text: t })));
  d.append(ul);
  return d;
}
let lastH = null;""")
rep("</style>", """.grpbox { background: #fff; border: 2px solid #D3DCC2; border-radius: 14px; padding: 10px 14px; margin: 14px 0 6px; }
.grpbox .grp { margin-top: 0; color: #3B4A2F; }
.ablaufk { margin: 6px 0 4px; font-size: 15px; color: #5E6652; }
ol.ablauf { margin: 0; padding-left: 22px; display: grid; gap: 6px; font-size: 16px; line-height: 1.35; }
ol.ablauf li.gem { font-weight: 700; color: #3B4A2F; }
ol.ablauf a { color: #2E7D8C; font-weight: 700; }
.abm { display: inline-block; font-size: 12px; font-weight: 800; letter-spacing: .05em; border-radius: 999px; padding: 1px 8px; margin-right: 6px; color: #fff; background: #5E6652; vertical-align: 1px; }
.abm.m-DEMO { background: #2E7D8C; } .abm.m-BESPRECHEN, .abm.m-DISKUSSION { background: #3B4A2F; }
.abm.m-GRUPPENARBEIT, .abm.m-PARTNERCHECK { background: #6B4F8A; }
.abm.m-SELBSTSTUDIUM { background: #E8DDBB; color: #6B4F00; } .abm.m-ABGABE { background: #7FA83A; }
.phbalken { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; margin: 14px 0; padding: 10px 14px; border-radius: 12px; border-left: 8px solid #3B4A2F; background: #EEF1E6; font-size: 17px; line-height: 1.4; font-weight: 600; color: #1F2A1C; }
.phbalken .phm { font-size: 12.5px; font-weight: 800; letter-spacing: .06em; color: #fff; background: #3B4A2F; border-radius: 6px; padding: 2px 8px; }
.phbalken.m-DEMO { border-color: #2E7D8C; background: #E6F1F3; } .phbalken.m-DEMO .phm { background: #2E7D8C; }
.phbalken.m-SELBSTSTUDIUM { border-color: #B8962E; background: #F7F1DE; } .phbalken.m-SELBSTSTUDIUM .phm { background: #8A6400; }
.gesichert { display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; margin: 6px 0 10px; padding: 6px 10px; border-radius: 10px; background: #EEF1E6; font-size: 15.5px; font-weight: 600; color: #3B4A2F; }
.gesichert .phm { font-size: 12px; font-weight: 800; letter-spacing: .06em; color: #fff; background: #3B4A2F; border-radius: 6px; padding: 2px 7px; }
.phabcd { margin-left: auto; min-height: 44px; font: inherit; font-size: 15px; font-weight: 700; border-radius: 999px; border: 2px solid #2E7D8C; background: #fff; color: #2E7D8C; padding: 4px 14px; cursor: pointer; }
.selbsth { margin: 8px 0 2px; border: 2px solid #B8962E; border-radius: 10px; padding: 6px 12px; background: #F7F1DE; font-size: 15.5px; }
.selbsth summary { cursor: pointer; font-weight: 700; color: #8A6400; min-height: 44px; display: flex; align-items: center; }
.selbsth ul { margin: 4px 0 6px; padding-left: 20px; display: grid; gap: 4px; }
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
.abcd-zu { min-height: 52px; font: inherit; font-weight: 700; font-size: 18px; border-radius: 12px; border: 0; background: #fff; color: #3B4A2F; }</style>""")
s = s.replace("26-27-3BK-K1.3-Epochen-TH-Handy-v1", I.KEY)  # Bausteine (pdferinnerung) mit altem Schlüssel
for blk in re.findall(r"<!-- ([a-z_]+):start -->", s):  # Bausteine kommen mit nach_dem_bauen.py frisch hinein
    pass
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
for bad in ["Epochen-", "Zeit-Einteilung", "Erkenntnis", "1AK", "Ökodesign", "Ökobilanz", "5AB", "Flasche"]:
    assert bad not in _plain, re.findall(r".{60}" + bad + r".{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Quiz zum Üben – Meilensteine</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Quiz zum Üben</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Quiz zum Üben am Handy</h2>")
qv = qv.replace("</h1>", "</h1>\n<a href=\"aufgaben.html\" class=\"abbtn\">Arbeitsblatt öffnen – dort arbeitest du</a>", 1)
qv = qv.replace("</style>", ".abbtn{display:block;text-align:center;background:#7FA83A;color:#fff;font-weight:700;font-size:19px;text-decoration:none;border-radius:12px;padding:14px 16px;margin:10px 0;min-height:44px}</style>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Quiz"')
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
    h = "".join(f"<th>{md(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join((f"<th scope=row>{md(c)}</th>" if k == 0 else f"<td>{md(c)}</td>") for k, c in enumerate(r)) + "</tr>" for r in rows[1:])
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


ul = lambda xs: '<ul class="pts">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ul>"
ol = lambda xs: '<ol class="goals">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ol>"
merke = lambda x: f'<div class="merke">{md(x)}</div>'
hint = lambda x: f'<p class="hint">{md(x)}</p>'
reveal = lambda q, a: f'<div class="stopq"><p><strong>{md(q)}</strong></p><details class="reveal"><summary>Erst überlegen – dann Lösung anzeigen</summary><p>{md(a)}</p></details></div>'
jetzt = lambda txt, href: f'<a class="jetzt" href="{href}">{esc(txt)} →</a>'


def video(key):
    if not I.zeigen(key):
        return ""  # Buch-Medium noch nicht von Stephan freigegeben
    t, q, d, u = I.VIDEOS[key][:4]
    sim = len(I.VIDEOS[key]) > 4 and I.VIDEOS[key][4] == "sim"
    if len(I.VIDEOS[key]) > 4 and I.VIDEOS[key][4] == "link":
        return (f'<div class="video sim"><div><strong>Zum Lesen: {esc(t)}</strong><br><span class="hint">{esc(q)} · {esc(d)}</span></div>'
                f'<a class="btn small" href="{u}" target="_blank" rel="noopener">Meldung öffnen</a></div>')
    if len(I.VIDEOS[key]) > 4 and I.VIDEOS[key][4] == "audio":
        return (f'<div class="video"><div><strong>Podcast: {esc(t)}</strong><br><span class="hint">{esc(q)} · {esc(d)} · im Unterricht gemeinsam</span></div>'
                f'<a class="btn small" href="{u}" target="_blank" rel="noopener">Podcast öffnen</a></div>')
    if sim:
        return (f'<div class="video sim"><div><strong>Simulation: {esc(t)}</strong><br><span class="hint">{esc(q)} · im Browser, auch am Handy</span></div>'
                f'<a class="btn small" href="{u}" target="_blank" rel="noopener">Simulation öffnen</a></div>')
    lab = f"Video ansehen ({d})" if d != "kurz" else "Video ansehen"
    return (f'<div class="video"><div><strong>Video: {esc(t)}</strong><br><span class="hint">{esc(q)}{" · " + esc(d) if d != "kurz" else ""}</span></div>'
            f'<a class="btn small" href="{u}" target="_blank" rel="noopener">{lab}</a></div>')


def figure(src, alt, cap):
    # Breite und Höhe mitgeben: Sonst wächst die Seite beim Nachladen und der Sprung aus dem Arbeitsblatt landet zu tief (Standard 18.11.2026).
    import struct
    _p = os.path.join(ROOT, I.ORDNER, src)
    _w, _h = struct.unpack(">II", open(_p, "rb").read(24)[16:24]) if os.path.exists(_p) else (900, 600)
    return f'<figure class="fig"><img src="{src}" alt="{esc(alt)}" width="{_w}" height="{_h}" loading="lazy"><figcaption>{md(cap)}</figcaption></figure>'


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
    if k == "karten": return karten(b[1])
    if k == "buch": return f'<div class="buch"><span class="bicon">Buch</span><p>{md(b[1])}</p></div>'
    raise ValueError(k)


def render(item):
    if isinstance(item, tuple) and item[0] == "jetzt": return jetzt(item[1], item[2])
    return slide(item["title"], "".join(block(b) for b in item["blocks"]), item["pill"], item["id"])


PARTS = [(pid, eyebrow, title, [render(x) for x in items]) for pid, eyebrow, title, items in TD.PARTS]
# »Meine Ziele« statt der alten Lernziele (Skill bhak-kompetenzmodell, 20.11.2026)
LZ = slide("Meine Ziele", hint("A = verstehen und wiedergeben · B = anwenden und analysieren · C = begründen und bewerten · + Grundlegendes, ++ Vertiefung")
           + '<ol class="mziele">' + "".join(f'<li><span class="kchip k{z["hd"]}">{z["hd"]}</span> {md(z["text"])}</li>' for z in I.ZIELE) + "</ol>", I.BUCH, "ziele")
PARTS[0] = (PARTS[0][0], PARTS[0][1], PARTS[0][2], PARTS[0][3] + [LZ])
PARTS.append(("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]))
CHECK = "".join(f'<div class="ziel"><span class="kchip k{z["hd"]}">{z["hd"]}</span><p>{md(z["text"])}</p><div class="chips" role="group" aria-label="Selbsteinschätzung">' + "".join(
    f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{lab}</button>' for v, lab in (("sicher", "zur Gänze"), ("fast", "überwiegend"), ("noch nicht", "noch nicht")))
    + "</div></div>" for k, z in enumerate(I.ZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                       slide("Ziele erreicht?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen. "
                                                                                     "Dieselbe Einschätzung steht als Aufgabe 13 im Arbeitsblatt und kommt ins PDF.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [render(x) for x in TD.SCHNELLE]))

# Theorie nach Stunden ordnen (Standard 20.11.2026): Trennbalken vor dem Teil einer Stunde, Übersicht ganz oben
STUNDE_TEIL = {1: "teil1", 2: "teil2", 3: "teil3"}
TEIL_STUNDE = {v: k for k, v in STUNDE_TEIL.items()}
toc = "".join(f'<a href="#{p[0]}">{("S" + str(TEIL_STUNDE[p[0]]) + " · ") if p[0] in TEIL_STUNDE else ""}{TD.TOCLAB[p[0]]}</a>' for p in PARTS) + '<a href="aufgaben.html">Arbeitsblatt</a>'


def _trenner(pid):
    n = TEIL_STUNDE.get(pid)
    if not n: return ""
    return (f'<div class="stdtrenner" id="stunde{n}"><span class="sbn">STUNDE {n}</span><span class="sbt">{esc(I.STUNDENTITEL[n])}</span>'
            f'<span class="sbk">{esc(PL.THEORIE_TEILE[n])} · {esc(PL.BUCH[n])}</span></div>')


UEBERSICHT = ('<div class="stduebersicht"><b>Welche Theorie gehört zu welcher Stunde?</b><ul>' + "".join(
    f'<li><a href="#stunde{n}">Stunde {n}</a>: ' + ", ".join(f'<a href="#{tid}">{esc(name)}</a>' for tid, name in PL.THEORIE_TEILE_IDS[n]) + "</li>"
    for n in sorted(PL.THEORIE_TEILE_IDS)) + "</ul></div>"
              '<a class="abbtn" href="aufgaben.html">Arbeitsblatt öffnen – dort arbeitest du</a>'
              '<p class="hint">Diese Seite ist zum Nachschlagen. Gearbeitet wird im Arbeitsblatt; dort steht auch, wie die Stunde läuft.</p>')
body = UEBERSICHT + "".join(f'{_trenner(p[0])}<section class="part" id="{p[0]}"><div class="band"><div class="eyebrow">{esc(p[1])}</div><h2>{esc(p[2])}</h2></div>{"".join(p[3])}</section>' for p in PARTS)
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
.video.sim { background: #E8F1F3; border-color: #2E7D8C; } .video.sim .btn { background: #2E7D8C; }
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
.buch { display: flex; gap: 12px; align-items: center; background: #EEF3E4; border: 2px solid #3B4A2F; border-radius: 12px; padding: 10px 14px; }
.buch p { margin: 0; } .bicon { font-weight: 700; color: #fff; background: #3B4A2F; border-radius: 8px; padding: 4px 10px; }
.karte { border: 1px solid #D3DCC2; border-radius: 12px; padding: 10px 12px; background: #fff; }
.karte summary { cursor: pointer; font-weight: 700; color: #3B4A2F; }
.karte p { margin: 8px 0 0; color: #2E7D8C; font-weight: 700; }
.knr { display: inline-block; min-width: 26px; text-align: center; background: #2E7D8C; color: #fff; border-radius: 999px; font-size: 14px; margin-right: 4px; }
.kchip { display: inline-block; font: 700 .78em/1.5 "Source Sans 3", sans-serif; padding: 0 .45em; border-radius: 6px; margin-right: .25em; vertical-align: .12em; border: 1.5px solid currentColor; white-space: nowrap; }
.kchip.kA { color: #1f5fa8; background: #e8f0fa; } .kchip.kB { color: #b3261e; background: #fbeaea; } .kchip.kC { color: #111; background: #ececec; }
ol.mziele { display: grid; gap: 8px; padding-left: 22px; } .ziel > .kchip { justify-self: start; }
.stdtrenner { margin: 44px 0 6px; padding: 16px 18px; border-radius: 14px; background: #3B4A2F; color: #fff; display: flex; flex-direction: column; gap: 6px; scroll-margin-top: 60px; box-shadow: 0 0 0 4px rgba(217,119,43,.35); }
.stdtrenner .sbn { align-self: flex-start; background: #D9772B; border-radius: 999px; padding: 4px 14px; font-size: 20px; font-weight: 800; letter-spacing: .06em; }
.stdtrenner .sbt { font-size: 20px; font-weight: 700; line-height: 1.3; }
.stdtrenner .sbk { font-size: 15px; opacity: .85; }
.stduebersicht { margin: 12px 0; border: 2px solid #D3DCC2; border-radius: 12px; padding: 10px 14px; background: #F7F9F2; }
.stduebersicht ul { margin: 6px 0 0; padding-left: 20px; display: grid; gap: 4px; } .stduebersicht a { color: #2E7D8C; font-weight: 700; }
.abbtn { display: block; text-align: center; background: #7FA83A; color: #fff; font-weight: 700; font-size: 19px; text-decoration: none; border-radius: 12px; padding: 14px 16px; margin: 10px 0 4px; min-height: 44px; }
</style>""")
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Meilensteine – Theorie</title>
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
  <div class="btns"><a class="btn" href="aufgaben.html">1 · Arbeitsblatt (hier arbeitest du)</a><a class="btn alt" href="quiz.html">2 · Quiz zum Üben</a><a class="btn alt" href="check.html">3 · Mitarbeits-Check (mit Startcode)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch PBGW 3 (Trauner) S. 23–44 und S. 105–118. Alle Grafiken selbst gezeichnet. Ergänzungen: Pressemeldung des Südtiroler Archäologiemuseums zum Kupfer von Ötzis Beil (1.3.2024), Seite des Louvre zur Hammurabi-Stele. Jahreszahlen sind Orientierung. <a href="../">Klassenübersicht 3BK</a></p>
  <p class="hint">Stand {STAND} · {I.V}</p>
</section>
</main>
<script>
(function () {{
  var KEY = "{I.CHECK_KEY}", S = {{}};
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
