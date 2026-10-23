"""Handy-Arbeitsblatt »Vertiefung zu den Versuchen« (Aufgaben 11–17) für NAWI 2AB · K1.2 Die Bindungsarten bauen.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ab-k1-2-stationen/bauen_vertiefung.py <jspdf.umd.min.js>
Schreibt 2ab-nawi/k1-2-bindungen/vertiefung.html.
Baut auf den eingefrorenen Kopien aufgaben_basis.html, pruefen.js, pdf_pruefung.js in diesem Ordner auf
(Stand 19.10.2026 aus quellen/1ab-k1-1-2-nobel2026, generisch gemacht) – nicht von anderen Einheiten abhängig."""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
JSPDF = sys.argv[1]
UNIT = "2ab-nawi/k1-2-bindungen/"
DST = os.path.join(ROOT, UNIT)
BASE = "https://stephanholzer12.github.io/unterricht/"
EYEBROW = "NAWI · 2AB · K1.2 Die Bindungsarten"
TITEL = "Vertiefung zu den Versuchen"
STAND = "19.10.2026"
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()

# ---------------------------------------------------------------- Aufgaben (Daten: richtige Antwort steht in der Datenquelle, Anzeige mischt bzw. ist neutral sortiert)
BIND = ["Ionenbindung", "Atombindung", "Metallbindung"]
T = [
 {"id": "a11", "nr": 11, "title": "Bindungs-Detektiv", "src": "Theorie S. 20–25", "h": "3–4", "type": "choose", "opts": BIND,
  "q": "Lies die Steckbriefe. Welche Bindung hält den Stoff zusammen? Tippe bei jedem Stoff die passende Bindungsart an.",
  "items": ["Glänzt, lässt sich biegen und leitet den Strom schon als Feststoff – Patronenhülse aus Messing",
            "Weiße Würfelchen, hart und spröde, schmilzt erst bei 801 °C – Kochsalz NaCl",
            "Gas für die Brennstoffzelle eines Fahrzeugs – Wasserstoff H₂",
            "Streusalz CaCl₂ – Calcium ist ein Metall, Chlor ein Nichtmetall",
            "Traubenzucker im Energieriegel – besteht nur aus C, H und O",
            "Rettungsdecke aus Aluminium im Erste-Hilfe-Set",
            "Wasser in der Feldflasche – H₂O"],
  "key": {"sol": [2, 0, 1, 0, 1, 2, 1]}},
 {"id": "a12", "nr": 12, "title": "Vorhersage zur Demo K1.2-V4", "src": "Theorie S. 21, 25", "h": "3–4", "type": "choose", "opts": ["leitet", "leitet nicht"],
  "q": "In Stunde 4 prüft die Lehrkraft mit dem Multimeter, was den Strom leitet. Tipp vorher: Leitet die Probe oder nicht? Denk daran: Strom braucht frei bewegliche, geladene Teilchen.",
  "items": ["Kupferblech", "Kochsalz, fest (trocken)", "Zucker, fest", "destilliertes Wasser", "Kochsalz in Wasser gelöst", "Zucker in Wasser gelöst"],
  "key": {"sol": [0, 1, 1, 1, 0, 1]}},
 {"id": "a13", "nr": 13, "title": "Mythos oder Fakt?", "src": "Theorie S. 21–27", "h": "3–4", "type": "myth", "opts": ["Mythos", "Fakt"],
  "q": "Entscheide bei jeder Aussage: Mythos oder Fakt? Begründe in einem Satz mit den Teilchen. Info auch aus euren Stationen A–D.",
  "items": ["Destilliertes Wasser leitet den Strom sehr gut.",
            "Eis schwimmt, weil Luftbläschen darin eingeschlossen sind.",
            "Ein Salzkristall zerspringt unter dem Hammer, ein Metall verbiegt sich nur.",
            "Öl und Wasser mischen sich nicht, weil Öl unpolar und Wasser polar ist.",
            "Waschmittel schwächt die Wasserstoffbrücken an der Wasseroberfläche – darum geht die Büroklammer unter."],
  "key": {"sol": ["Mythos", "Mythos", "Fakt", "Fakt", "Fakt"],
          "why": ["Im reinen Wasser gibt es kaum Ionen; erst gelöste Salze machen es leitfähig.",
                  "Wasserstoffbrücken halten die Moleküle im Eis auf Abstand – Eis (0,92 g/cm³) ist weniger dicht als Wasser.",
                  "Beim Salz verschieben sich die Ionenschichten, gleiche Ladungen stoßen sich ab; beim Metall hält das Elektronengas die Kationen zusammen.",
                  "Ähnliches löst sich in Ähnlichem: Polar mischt sich mit polar, unpolar mit unpolar.",
                  "Die Oberflächenspannung sinkt, die »Haut« des Wassers trägt die Klammer nicht mehr."]}},
 {"id": "a14", "nr": 14, "title": "Wasser – ein besonderes Molekül", "src": "Theorie S. 23, 26", "h": "3–4", "type": "gaps",
  "q": "Ergänze die Lücken mit den passenden Fachbegriffen.",
  "sents": [["Im Wassermolekül zieht das ", 0, "-Atom die Bindungselektronen stärker an als die H-Atome."],
            ["Dadurch ist das O-Atom leicht negativ (δ–), die H-Atome sind leicht ", 1, " (δ+)."],
            ["Weil das Molekül gewinkelt ist, ist Wasser ein ", 2, "."],
            ["Das δ+ H eines Moleküls zieht das δ– O des Nachbarn an: Das ist eine ", 3, "."],
            ["Diese Kräfte halten die Wasseroberfläche wie eine Haut zusammen – das nennt man ", 4, "."]],
  "key": {"acc": [["Sauerstoff", "O", "Sauerstoffatom", "Sauerstoff-Atom"], ["positiv", "positiv geladen", "plus"], ["Dipol", "Dipolmolekül"],
                  ["Wasserstoffbrücke", "Wasserstoffbrückenbindung", "Wasserstoffbrücken", "H-Brücke", "Wasserstoffbrückenbindungen"], ["Oberflächenspannung"]],
          "sol": ["Sauerstoff", "positiv", "Dipol", "Wasserstoffbrücke", "Oberflächenspannung"]}},
 {"id": "a15", "nr": 15, "title": "So entsteht Kochsalz", "src": "Theorie S. 20–21", "h": "3–4", "type": "order",
  "q": "Bring die Schritte der Ionenbindung von Natrium und Chlor in die richtige Reihenfolge. Wähle bei jedem Schritt die Nummer 1–5.",
  "items": ["Die Ionen ziehen sich an und bauen ein Ionengitter auf.",
            "Natrium (1 Außenelektron) und Chlor (7 Außenelektronen) treffen aufeinander.",
            "Das Chlor-Atom nimmt das Elektron auf und wird zum Anion Cl⁻.",
            "Das Natrium-Atom gibt sein Außenelektron ab und wird zum Kation Na⁺.",
            "Beide Ionen haben jetzt 8 Außenelektronen – den Edelgaszustand."],
  "key": {"sol": [5, 1, 3, 2, 4]}},
 {"id": "a16", "nr": 16, "title": "Elektrolytgetränk nach dem Marsch", "src": "Theorie S. 21 · Salze im Körper", "h": "3–4", "type": "multi",
  "q": "Nach einem 25-km-Marsch im Sommer bekommt die Kompanie ein Elektrolytgetränk mit Natrium- und Kaliumsalzen.",
  "parts": [["a", "a) Erkläre in 2 Sätzen, warum das Getränk den Strom leitet, Zuckerwasser aber nicht."],
            ["b", "b) Begründe in 1–2 Sätzen, warum der Körper diese Salze nach starkem Schwitzen braucht."]],
  "key": {"kw": {"a": ["ion", "ionen", "geladen", "ladung"]},
          "sol": ["Im Getränk sind Salze gelöst – frei bewegliche, geladene Ionen (z. B. Na⁺, K⁺, Cl⁻), die den Strom tragen. Zucker besteht aus ungeladenen Molekülen (Atombindung).",
                  "Mit dem Schweiß verliert der Körper Salze. Natrium- und Kalium-Ionen braucht er z. B. für Nerven und Muskeln – fehlen sie, drohen Krämpfe und Leistungsabfall."]}},
 {"id": "a17", "nr": 17, "title": "Für Schnelle: Science oder Fiction?", "src": "Theorie S. 26", "h": "3–4", "tag": "OPTIONAL", "type": "multi",
  "q": "In einem Actionfilm springt ein Soldat in einen zugefrorenen Bergsee und taucht unter dem Eis weiter – im Winter. Der Film zeigt: Unter dem Eis ist der See nicht gefroren.",
  "parts": [["t", "Science oder Fiction? Erkläre in 3 Sätzen, warum ein See von oben zufriert, was das für die Fische bedeutet – und welche Gefahr trotzdem für den Soldaten besteht."]],
  "key": {"sol": ["Science: Eis ist wegen der Wasserstoffbrücken weniger dicht (0,92 g/cm³) und schwimmt oben; darunter bleibt flüssiges Wasser (am Grund etwa 4 °C), Fische überleben. Für den Menschen ist das Wasser aber eiskalt – Unterkühlung droht in wenigen Minuten, und man findet das Loch im Eis schwer wieder."]}},
]
assert [t["nr"] for t in T] == list(range(11, 18))
for t in T:
    if t["type"] == "choose": assert len(t["items"]) == len(t["key"]["sol"])
NOTE = ("Auswahl, Lücken und Reihenfolge werden automatisch geprüft; Aufgabe 16 a) wird auf Stichwörter geprüft (Ion, geladen). "
        "Begründungen in Aufgabe 13, 16 b) und 17 beurteilt die Lehrkraft. »1. Versuch« = beim ersten Prüfen richtig. »Fehlversuche« = Klicks auf »Prüfen« mit mindestens einem Fehler.")

# Render-, Fertig- und Text-Funktionen wie im Muster (eingefroren aus quellen/1ab-k1-1-2-nobel2026/bauen.py)
NB = open(os.path.join(HERE, "render_teile.js"), encoding="utf-8").read()
RENDER_JS, DONE_JS, LINES_JS = NB.split("//----TEIL----\n")


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


def wrap(src):
    te = src.index("</title>") + 8; rest = src[te:]; bs = rest.index("<header")
    return ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="robots" content="noindex">\n' + src[:te] + "\n" + rest[:bs] + "</head>\n<body>\n" + rest[bs:] + "\n</body>\n</html>\n")


def cut(src, start, end, new):
    a = src.index(start); b = src.index(end, a)
    return src[:a] + new + src[b:]


def rp(src, x, y, n=-1):
    assert x in src, x[:60]
    return src.replace(x, y) if n < 0 else src.replace(x, y, n)


src = open(os.path.join(HERE, "aufgaben_basis.html"), encoding="utf-8").read()
src = rp(src, "<title>Wie groß bist du wirklich? – Arbeitsblatt</title>", f"<title>{TITEL} – Arbeitsblatt</title>")
src = rp(src, "NAWI · 1AB · K1.2.2 Messen und Messfehler", EYEBROW)
src = rp(src, "<h1>Wie groß bist du wirklich?</h1>", f"<h1>{TITEL}</h1>")
src = rp(src, "<option>1AK</option><option>1BK</option>", "<option>2A</option><option>2B</option>")
src = rp(src, "<h2>Arbeitsblatt am Handy</h2>", "<h2>Vertiefung am Handy</h2>")
src = rp(src, "Stunde 1: Aufgaben 1–4 · Stunde 2: Aufgaben 5–10.",
         "Stunde 3–4, während deine Gruppe nicht an einer Station ist (oder auf die nächste Station wartet): Aufgaben 11–16, Aufgabe 17 für Schnelle. Jeder arbeitet am eigenen Handy.")
src = rp(src, "Schulbuch (Trauner) S. 17–19", 'Schulbuch (Trauner) S. 19–28 · <a href="versuche.html">Versuchsseite</a> · Aufgaben 1–10: <a href="aufgaben.html">Arbeitsblatt</a>')
src = rp(src, '<span id="count">0 von 10 bearbeitet</span>', f'<span id="count">0 von {len(T)} bearbeitet</span>')
src = rp(src, 'const KEY = "26-27-1AB-K1.2.2-Koerper-UE-Handy-v1";', 'const KEY = "26-27-2AB-K1.2-Bindungen-Vertiefung-Handy-v1";')
src = rp(src, 'const TITLE = "K1.2.2 Wie groß bist du wirklich?";', f'const TITLE = "K1.2 {TITEL}";')
src = cut(src, "const GERAETE", "// ---------- Zustand", "const T = " + json.dumps(T, ensure_ascii=False, indent=1) + ";\n\n")
PRUEF_JS = open(os.path.join(HERE, "pruefen.js"), encoding="utf-8").read()
PDF_JS = (open(os.path.join(HERE, "pdf_pruefung.js"), encoding="utf-8").read()
          .replace("__EYEBROW__", json.dumps(EYEBROW, ensure_ascii=False)).replace("__TITEL__", json.dumps(TITEL, ensure_ascii=False))
          .replace("__KAPTITEL__", json.dumps("K1.2 " + TITEL, ensure_ascii=False)).replace("__BUCHS__", "19–28").replace("__NOTE__", json.dumps(NOTE, ensure_ascii=False)))
src = cut(src, "// ---------- Säulendiagramm zum Antippen ----------", "// ---------- Fortschritt ----------", RENDER_JS + "\n" + PRUEF_JS + "\n")
src = cut(src, "function buildPdf() {", "function savePdf() {", PDF_JS)
src = rp(src, 'let S = { name: "", klasse: "", a: {} };', 'let S = { name: "", klasse: "", a: {}, chk: {}, pdfDone: false, solSeen: false, snap: {} };')
src = rp(src, 'say("ok", "PDF wurde erstellt: " + filename + " – schau in deinen Downloads nach, ob sie da ist, und lade sie dann in LMS hoch.");', 'say("ok", "PDF wurde erstellt: " + filename + " – schau in deinen Downloads nach, ob sie da ist, und lade sie dann in LMS hoch."); afterPdf();')
src = rp(src, '<p class="status" id="pdfstatus" hidden aria-live="polite"></p>', '<p class="status" id="pdfstatus" hidden aria-live="polite"></p>\n    <button class="btn secondary" type="button" id="solbtn" hidden>Musterlösungen ansehen</button>\n    <p class="hint" id="solnote" hidden>Die Musterlösungen stehen jetzt bei den Aufgaben. Wenn du danach noch einmal eine PDF erstellst, steht darauf »nach Lösungseinsicht erstellt«.</p>', 1)
src = rp(src, '$("#pdfbtn").addEventListener("click", savePdf);', '$("#pdfbtn").addEventListener("click", savePdf);\n$("#solbtn").addEventListener("click", () => { S.solSeen = true; save(); showSolutionsAll(); });', 1)
src = rp(src, 'if (raw) S = Object.assign(S, JSON.parse(raw)); } catch (e) {}', 'if (raw) S = Object.assign(S, JSON.parse(raw)); } catch (e) {}\nS.chk = S.chk || {};', 1)
src = rp(src, '$("#copyArea").value = asText();\n}', '$("#copyArea").value = asText();\n  showSolutionsAll();\n}', 1)
src = rp(src, '"Alle Aufgaben bearbeitet.");', '"Alle Aufgaben bearbeitet.") + unchecked();', 1)
src = rp(src, "Nach jeder Aufgabe kontrollieren wir gemeinsam.", "Drück bei jeder Aufgabe auf <b>Prüfen</b>: Du siehst sofort, was stimmt. Ab dem 2. Fehlversuch gibt es einen Tipp, ab dem 3. kannst du die Lösung ansehen.")
src = rp(src, "Ganz unten <b>PDF erstellen</b> und die PDF in LMS hochladen.", "Ganz unten <b>PDF erstellen</b> und in LMS hochladen. Im PDF stehen dein Ergebnis und deine Versuche.")
CSS = """.r-ok { border-color: #2E7D3A !important; background-color: #E3F1DA !important; }
.r-bad { border-color: #B33A2C !important; background-color: #FBE3DE !important; border-style: dashed !important; }
.chk { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; margin-top: 4px; }
.chk .fb { font-weight: 700; flex: 1 1 12em; font-size: 16px; }
.fb.ok { color: #2E7D3A; } .fb.bad { color: #B33A2C; } .fb.info { color: var(--muted); font-weight: 400; }
.solbox { background: #E8F3F5; border-left: 4px solid var(--teal); border-radius: 10px; padding: 10px 12px; display: grid; gap: 4px; font-size: 16px; }
.solbox strong { color: var(--teal); }
.solbox[hidden], .chk [hidden] { display: none !important; }
.sent2 { border"""
src = rp(src, ".sent2 { border", CSS, 1)
src = cut(src, "function isDone(t) {", "function update() {", DONE_JS)
src = cut(src, "function answerLines(t) {", "function asText() {", LINES_JS)
src = rp(src, 'clean("NAWI · 1AB · K1.2.2 Messen und Messfehler · Schulbuch S. 17–19")', f'clean("{EYEBROW} · Schulbuch S. 19–28")') if 'clean("NAWI · 1AB · K1.2.2 Messen und Messfehler · Schulbuch S. 17–19")' in src else src
src = src.replace('const filename = "K1.2.2-Koerper-" + slug(S.name) + ".pdf";', 'const filename = "K1.2-Vertiefung-" + slug(S.name) + ".pdf";')
assert 'K1.2-Vertiefung-' in src
# Stand-Datum im Fuß
src = rp(src, "</main>", f'  <p class="hint" style="text-align:center;margin:18px 0 8px">{EYEBROW} · Vertiefung · Stand {STAND}</p>\n</main>', 1)
tpl = open(os.path.join(WZ, "vorlagen", "aufgaben_K1.2_vorlage.html"), encoding="utf-8").read()
rep = {"__BASECSS__": tpl[tpl.index("<style>"):tpl.index("</style>") + 8], "__CAMO__": b64(WZ + "/camo.png"), "__LOGO__": b64(WZ + "/logo.png"), "__SMILEY__": b64(WZ + "/smiley.png"),
       "__FONTR__": b64(WZ + "/schriften/carlito-Regular.ttf"), "__FONTB__": b64(WZ + "/schriften/carlito-Bold.ttf"),
       "__RANGES__": open(WZ + "/schriften/ranges.json").read().strip(), "__QR__": qr_b64(BASE + UNIT + "vertiefung.html"),
       "__JSPDF__": open(JSPDF, encoding="utf-8").read()}
for k, v_ in rep.items(): src = src.replace(k, v_)
src = src.replace("</style>\n\n<header", ".row .choose { margin-top: 4px; }\n</style>\n\n<header", 1)
assert not re.search(r"__[A-Z]+__", src)
for bad in ["Körpergröße", "K1.2.2", "Wie groß", "1AK", "Nobel"]:
    assert bad not in src.split("/* jsPDF")[0] and bad not in src.split("</script>\n<script>")[-1], bad
open(DST + "vertiefung.html", "w", encoding="utf-8").write(wrap(src))
print("vertiefung.html", len(src) // 1024, "KB")
