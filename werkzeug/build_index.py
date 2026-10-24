"""Klassenübersichten aus einheiten.json erzeugen. Aufruf im Repository-Ordner: python3 werkzeug/build_index.py

Pro Klasse (z. B. 2ab-nawi/) entstehen drei Seiten mit festen Namen (Links und QR-Codes bleiben gleich):
- index.html       Stoff-Übersicht: »Gerade dran«, Tests, alle bisherigen Einheiten nach Themenblöcken des
                   Jahresplans (mit Inhalt der Theorie-Seite und »Das Wichtigste in 5 Sätzen«)
- begriffe.html    Fachbegriffe A–Z aus allen bisherigen Theorie-Seiten, mit Suche
- wiederholen.html Lernziele aller Einheiten zum Abhaken (sicher / fast / noch nicht) – teilt den Speicher
                   mit dem Selbstcheck »Kann ich das?« der Theorie-Seiten

Daten:
- einheiten.json: pro Einheit klasse, fach, ordner, kapitel, titel, block (z. B. "A Atombau & Bindung"),
  jahresplan (z. B. "E3"), seiten. Optional: "aktuell": true (sonst ist die zuletzt eingetragene Einheit
  »Gerade dran«), "versteckt": true (Einheit ist schon online, erscheint aber noch nicht in der Übersicht).
  Test-Trainings: kapitel = "<Nr>. Test · <Datum>" (ohne block).
  Optional "dateien": {"stand": "18.10.2026", "zip": "…-v3.zip", "liste": ["…-TH-Lehrer-v2.pptx", …]} – die aktuell
  gültigen PPP-/Word-Dateien der Einheit; erscheinen nur auf der Lehrer-Seite.
- bloecke.json: Reihenfolge der Themenblöcke laut Jahresplan (aus bloecke_aus_jahresplan.py).
- Theorie-Seiten (theorie.html): Buchseiten, Teile, Lernziele, »Das Wichtigste«, Fachbegriffe (lernseite_lesen.py).

Es erscheinen nur Einheiten, die in einheiten.json stehen – kommende Themen bleiben unsichtbar.
Die Startseite index.html verlinkt KEINE Klassen (damit keine Klasse die Seiten der anderen sieht).
"""
import base64, datetime, html, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "werkzeug"))
from lernseite_lesen import lesen  # noqa: E402
import fahrplan as fp  # noqa: E402
import lehrer_layout as ll  # noqa: E402
import kadetten_layout as ks  # noqa: E402

W = lambda *p: os.path.join(ROOT, "werkzeug", *p)
E = json.load(open(W("einheiten.json"), encoding="utf-8"))
BLOECKE = json.load(open(W("bloecke.json"), encoding="utf-8")) if os.path.exists(W("bloecke.json")) else {}
B64 = lambda f: base64.b64encode(open(W(f), "rb").read()).decode()
LOGO, CAMO, SMILEY = B64("logo.png"), B64("camo.png"), B64("smiley.png")
SCHULJAHR = (2026, 2027)
HEUTE = datetime.date.today()
STAND = HEUTE.strftime("%d.%m.%Y")
esc = html.escape
BASIS = "https://stephanholzer12.github.io/unterricht/"
# Lehrer-Seite: fester Arbeitslink für Stephan, nirgends auf Kadetten-Seiten verlinkt.
# Die öffentliche Adresse ist keine Zugriffssperre.
LEHRER = "lehrer-0f6eec.html"

# Seite → (Beschriftung, Stil). Reihenfolge der Knöpfe wie der Lernpfad: Theorie-Seite → Arbeitsblatt → Quiz
NAMEN = {"theorie.html": ("Theorie", "teal"), "aufgaben.html": ("Arbeitsblatt", ""), "quiz.html": ("Quiz", ""),
         "versuche.html": ("Versuche", "rust"), "vertiefung.html": ("Vertiefung", ""), "uebung.html": ("Übung", ""), "projekt.html": ("Projekt", ""),
         "gruppe.html": ("Gruppe", ""), "teststoff.html": ("Teststoff", "rust"), "kurz.html": ("Gruppe kompakt", "")}
REIHE = ["theorie.html", "aufgaben.html", "versuche.html", "vertiefung.html", "uebung.html", "projekt.html", "gruppe.html", "kurz.html", "quiz.html"]

CSS = """
:root { --bg: #EEF3E4; --card: #FFFFFF; --ink: #1F2A1C; --olive: #3B4A2F; --teal: #2E7D8C; --green: #7FA83A;
  --rust: #8C3B2E; --orange: #D9772B; --muted: #5E6652; --line: #D3DCC2; --soft: #F5F8EF; color-scheme: light;
  --font-head: Cambria, "Source Serif 4", Georgia, serif; --font-body: Calibri, "Source Sans 3", "Segoe UI", sans-serif; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 56px; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
html, body { background: var(--bg); color: var(--ink); }
body { margin: 0; font-family: var(--font-body); font-size: 18px; line-height: 1.45; }
img { max-width: 100%; height: auto; }
.top { background: var(--card); position: relative; border-bottom: 1px solid var(--line); }
.top .camo { position: absolute; left: 0; top: 0; width: 190px; pointer-events: none; }
.top .logo { position: absolute; left: 8px; top: 6px; width: 52px; }
.top-inner { max-width: 720px; margin: 0 auto; padding: 18px 16px 16px; min-height: 104px; display: flex; align-items: center; gap: 12px; }
.top-text { margin-left: 150px; flex: 1; min-width: 0; }
.eyebrow { font-weight: 700; font-size: 14px; color: var(--teal); letter-spacing: .04em; }
h1 { font-family: var(--font-head); color: var(--olive); font-size: 34px; line-height: 1.05; margin: 2px 0 0; }
.top .smiley { width: 64px; height: 64px; flex: 0 0 64px; }
@media (max-width: 520px) {
  .top .camo { width: 112px; } .top .logo { width: 32px; left: 6px; top: 4px; }
  .top-inner { padding-top: 54px; min-height: 0; } .top-text { margin-left: 0; } h1 { font-size: 30px; }
  .top .smiley { width: 52px; height: 52px; flex-basis: 52px; } }
nav.toc { position: sticky; top: 0; z-index: 5; background: var(--olive); }
nav.toc div { max-width: 720px; margin: 0 auto; display: flex; gap: 6px; overflow-x: auto; padding: 8px 16px; scrollbar-width: none; }
nav.toc a { flex: 0 0 auto; color: #fff; text-decoration: none; font-weight: 700; font-size: 15px; padding: 5px 12px; border-radius: 999px; border: 1.5px solid rgba(255,255,255,.45); }
nav.toc a[aria-current="page"] { background: #fff; color: var(--olive); }
nav.toc a:hover, nav.toc a:focus-visible { background: #fff; color: var(--olive); outline: none; }
main { max-width: 720px; margin: 0 auto; padding: 18px 16px 48px; display: grid; gap: 14px; }
h2 { font-family: var(--font-head); color: var(--olive); font-size: 25px; line-height: 1.15; margin: 10px 0 0; }
h3 { font-family: var(--font-head); color: var(--olive); font-size: 21px; line-height: 1.2; margin: 0; text-wrap: balance; }
.card { background: var(--card); border-radius: 14px; padding: 14px 16px; box-shadow: 0 2px 6px rgba(31,42,28,.12); display: grid; gap: 8px; }
.hero { border-left: 6px solid var(--green); }
.hero h3 { font-size: 24px; }
.badge { display: inline-block; font-size: 13px; font-weight: 700; color: #fff; background: var(--green); border-radius: 999px; padding: 2px 10px; vertical-align: 2px; letter-spacing: .03em; }
.badge.test { background: var(--orange); }
.meta { color: var(--muted); font-size: 15px; }
.links { display: flex; flex-wrap: wrap; gap: 8px; }
a.btn { text-decoration: none; font-weight: 700; color: #fff; background: var(--olive); border-radius: 10px; padding: 9px 16px; font-size: 17px; }
a.btn.teal { background: var(--teal); } a.btn.rust { background: var(--rust); } a.btn.light { background: var(--soft); color: var(--olive); border: 1.5px solid var(--line); }
a.btn:focus-visible, button:focus-visible, summary:focus-visible, input:focus-visible { outline: 3px solid var(--teal); outline-offset: 2px; }
.tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
@media (max-width: 520px) { .tiles { grid-template-columns: 1fr 1fr; } .tiles a:last-child { grid-column: 1 / -1; } }
.tiles a { display: block; text-decoration: none; color: var(--ink); background: var(--card); border-radius: 14px; padding: 12px 14px; box-shadow: 0 2px 6px rgba(31,42,28,.12); }
.tiles b { display: block; font-family: var(--font-head); color: var(--olive); font-size: 28px; line-height: 1.1; }
.tiles span { font-size: 15px; color: var(--muted); }
.bar { height: 10px; background: var(--line); border-radius: 999px; overflow: hidden; display: flex; }
.bar i { display: block; height: 100%; }
details.block { background: var(--card); border-radius: 14px; box-shadow: 0 2px 6px rgba(31,42,28,.12); }
details.block > summary { list-style: none; cursor: pointer; padding: 12px 16px; display: flex; align-items: center; gap: 12px; background: var(--olive); color: #fff; border-radius: 14px; }
details.block[open] > summary { border-radius: 14px 14px 0 0; }
details.block > summary::-webkit-details-marker { display: none; }
details.block > summary .nr { flex: 0 0 38px; height: 38px; border-radius: 50%; background: #fff; color: var(--olive); font-weight: 700; font-size: 18px; display: grid; place-items: center; }
details.block > summary .t { flex: 1; min-width: 0; }
details.block > summary .t small { display: block; color: #C9D3B0; font-weight: 700; font-size: 13px; letter-spacing: .04em; }
details.block > summary .t strong { font-family: var(--font-head); font-size: 21px; font-weight: 700; }
details.block > summary::after { content: "▾"; font-size: 20px; transition: transform .2s; }
details.block:not([open]) > summary::after { transform: rotate(-90deg); }
.units { display: grid; gap: 0; }
.unit { padding: 14px 16px; display: grid; gap: 8px; border-top: 1px solid var(--line); }
.unit:first-child { border-top: 0; }
.unit.now { background: #F3F8E8; }
details.mehr { border: 1.5px solid var(--line); border-radius: 10px; background: var(--soft); }
details.mehr > summary { cursor: pointer; padding: 7px 12px; font-weight: 700; color: var(--olive); font-size: 16px; }
details.mehr > div { padding: 0 12px 10px; }
details.mehr ol, details.mehr ul { margin: 0; padding-left: 22px; display: grid; gap: 4px; font-size: 16px; }
details.mehr a:not(.btn) { color: var(--teal); font-weight: 700; text-decoration: none; }
details.mehr .s { color: var(--muted); font-size: 14px; white-space: nowrap; }
p.note { margin: 6px 0 0; color: var(--muted); font-size: 15px; }
footer { max-width: 720px; margin: 0 auto; padding: 0 16px 32px; color: var(--muted); font-size: 14px; }
.empty { color: var(--muted); font-style: italic; }
/* Fachbegriffe */
.search { width: 100%; font: inherit; font-size: 18px; padding: 10px 14px; border: 2px solid var(--line); border-radius: 12px; background: #FFFDE8; }
.abc { display: flex; flex-wrap: wrap; gap: 6px; }
.abc a { text-decoration: none; font-weight: 700; color: var(--olive); background: var(--card); border: 1.5px solid var(--line); border-radius: 8px; min-width: 34px; text-align: center; padding: 4px 6px; font-size: 16px; }
.letter { font-family: var(--font-head); color: var(--olive); font-size: 26px; margin: 8px 0 0; }
dl.terms { margin: 0; display: grid; gap: 8px; }
dl.terms > div { background: var(--card); border-radius: 12px; padding: 10px 14px; box-shadow: 0 1px 4px rgba(31,42,28,.1); }
dl.terms dt { font-weight: 700; color: var(--ink); font-size: 19px; }
dl.terms dd { margin: 2px 0 0; }
dl.terms dd a { display: inline-block; margin-top: 4px; font-size: 14px; font-weight: 700; color: var(--teal); text-decoration: none; }
/* Wiederholen */
.ziel { display: grid; gap: 6px; padding: 8px 0; border-top: 1px dashed var(--line); }
.ziel p { margin: 0; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { font: inherit; font-size: 15px; font-weight: 700; border-radius: 999px; padding: 5px 14px; border: 1.5px solid var(--line); background: var(--card); color: var(--olive); cursor: pointer; touch-action: manipulation; }
.chip[aria-pressed="true"][data-v="sicher"] { background: var(--green); border-color: var(--green); color: #fff; }
.chip[aria-pressed="true"][data-v="fast"] { background: var(--orange); border-color: var(--orange); color: #fff; }
.chip[aria-pressed="true"][data-v="noch nicht"] { background: var(--rust); border-color: var(--rust); color: #fff; }
.ziel .hin { display: none; font-size: 15px; } .ziel.nn .hin { display: block; }
.ziel .hin a { color: var(--teal); font-weight: 700; }
.legend { display: flex; flex-wrap: wrap; gap: 12px; font-size: 15px; color: var(--muted); }
.legend i { display: inline-block; width: 12px; height: 12px; border-radius: 3px; margin-right: 5px; vertical-align: -1px; }
.filter { display: flex; flex-wrap: wrap; gap: 6px; }
.filter button { font: inherit; font-size: 15px; font-weight: 700; border-radius: 999px; padding: 6px 14px; border: 1.5px solid var(--olive); background: var(--card); color: var(--olive); cursor: pointer; }
.filter button[aria-pressed="true"] { background: var(--olive); color: #fff; }
body.nur-offen .ziel.ok { display: none; }
@media print { nav.toc, .chips, .filter, .links, .search, .abc, .noprint { display: none !important; } .card, details.block { box-shadow: none; border: 1px solid #ccc; } body { background: #fff; } details.block > summary { color: #000; background: #eee; } }
"""

JS_COUNTDOWN = """
document.querySelectorAll('[data-datum]').forEach(function (el) {
  var d = new Date(el.dataset.datum + 'T00:00:00'), h = new Date(); h.setHours(0, 0, 0, 0);
  var t = Math.round((d - h) / 86400000);
  el.textContent = t > 1 ? 'in ' + t + ' Tagen' : t === 1 ? 'morgen' : t === 0 ? 'heute' : 'vorbei';
  if (t < 0) el.classList.add('vorbei');
});
"""


def kopf(titel, eyebrow, aktiv, k_titel):
    nav = [("index.html", "Übersicht"), ("index.html#themen", "Themen"), ("begriffe.html", "Begriffe"), ("wiederholen.html", "Wiederholen")]
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == aktiv else ""}>{esc(n)}</a>' for h, n in nav)
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>{esc(k_titel)}</title>
<style>{CSS}</style>
</head>
<body>
<header class="top">
  <img class="camo" alt="" src="data:image/png;base64,{CAMO}">
  <img class="logo" alt="BHAK Wappen" src="data:image/png;base64,{LOGO}">
  <div class="top-inner">
    <div class="top-text"><div class="eyebrow">{esc(eyebrow)}</div><h1>{esc(titel)}</h1></div>
    <img class="smiley" alt="" src="data:image/png;base64,{SMILEY}">
  </div>
</header>
<nav class="toc" aria-label="Klassenseiten"><div>{links}</div></nav>
<main>
"""


FUSS = "Die Übersicht wächst mit: Jede neue Einheit erscheint hier, sobald wir dort sind. Antworten bleiben nur auf deinem Handy gespeichert, Abgabe als PDF in LMS."


def klassen_kopf(titel, eyebrow, aktiv, k_titel):
    return ks.kopf(kopf(titel, eyebrow, aktiv, k_titel))


def fuss(js="", text=FUSS):
    return f"""</main>
<footer>Stand {STAND} · {text}</footer>
{f"<script>{js}</script>" if js else ""}
</body>
</html>
"""


def kap_key(k):
    teile = re.findall(r"\d+|[a-z]", k.lower().lstrip("k"))
    return [(0, int(t)) if t.isdigit() else (1, t) for t in teile]


def blockname(b):
    return re.sub(r"^[A-Z]\s+", "", b)


def sortkey_begriff(b):
    s = unicodedata.normalize("NFD", b.lower())
    s = "".join(c for c in s if not unicodedata.combining(c)).replace("ß", "ss")
    return re.sub(r"^[^a-z0-9]+", "", s) or s


def buchstabe(b):
    k = sortkey_begriff(b)
    return k[0].upper() if k and k[0].isalpha() else "#"


def test_datum(kapitel):
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.?", kapitel.split("·", 1)[-1])
    if not m:
        return None
    t, mo = int(m.group(1)), int(m.group(2))
    try:
        return datetime.date(SCHULJAHR[0] if mo >= 9 else SCHULJAHR[1], mo, t)
    except ValueError:
        return None


def test_termine(e):
    """Termine eines Tests als [(Klasse oder "", Datum), …].
    Bevorzugt das Feld "termine" in einheiten.json ({"4AK": "2026-11-09", …}) – nur so bekommen
    parallel geführte Klassen mit verschiedenen Terminen jeweils den richtigen Countdown.
    Ohne dieses Feld wie bisher das erste Datum aus dem Kapiteltext (reicht bei einem Termin)."""
    tm = e.get("termine")
    if isinstance(tm, dict) and tm:
        paare = []
        for kl, iso in tm.items():
            try:
                paare.append((kl, datetime.date.fromisoformat(iso)))
            except (TypeError, ValueError):
                pass
        if paare:
            return sorted(paare, key=lambda x: x[1])
    d = test_datum(e["kapitel"])
    return [("", d)] if d else []


def erster_termin(e):
    """Frühestes Datum eines Tests – für Sortierung und die Kachel »nächster Test«."""
    tm = test_termine(e)
    return tm[0][1] if tm else None


def knoepfe(e, nur=None):
    seiten = sorted(e["seiten"], key=lambda s: REIHE.index(s) if s in REIHE else 99)
    if nur:
        seiten = [s for s in seiten if s in nur]
    return "".join(f'<a class="btn {NAMEN.get(s, (s, ""))[1]}" href="{esc(e["unter"])}/{s}">{esc(NAMEN.get(s, (s, ""))[0])}</a>' for s in seiten)


def daten_klasse(ordner, es):
    """Einheiten einer Klasse mit den Daten aus den Theorie-Seiten anreichern und nach Blöcken ordnen."""
    tests, units, versteckt = [], [], []
    for e in es:
        e = dict(e, unter=e["ordner"].split("/", 1)[1])
        if e.get("versteckt"):
            versteckt.append(e)
            continue
        if re.match(r"\d+\.\s*Test", e["kapitel"]):
            tests.append(e)
            continue
        th = os.path.join(ROOT, e["ordner"], "theorie.html")
        e["lern"] = lesen(th) if "theorie.html" in e["seiten"] and os.path.exists(th) else None
        units.append(e)
    akt = [u for u in units if u.get("aktuell")] or units[-1:]
    for u in units:
        u["jetzt"] = u in akt
    plan = [b["block"] for b in BLOECKE.get(ordner, [])]
    bl = {}
    for u in units:
        bl.setdefault(u.get("block") or "", []).append(u)
    reihe = [b for b in plan if b in bl] + sorted(b for b in bl if b not in plan and b) + ([""] if "" in bl else [])
    bloecke = []
    for b in reihe:
        nr = plan.index(b) + 1 if b in plan else None
        bloecke.append({"name": blockname(b) if b else "Weitere Themen", "nr": nr, "units": sorted(bl[b], key=lambda u: kap_key(u["kapitel"]))})
    return tests, units, bloecke, len(plan), versteckt


def unit_html(u, mit_mehr=True):
    L = u["lern"] or {}
    meta = " · ".join(x for x in [u["kapitel"], L.get("buch", "")] if x)
    badge = ' <span class="badge">Gerade dran</span>' if u["jetzt"] else ""
    mehr = ""
    if mit_mehr and L.get("teile"):
        li = "".join(f'<li><a href="{esc(u["unter"])}/theorie.html#{esc(t["id"])}">{esc(t["titel"])}</a>' + (f' <span class="s">{esc(t["buch"])}</span>' if t["buch"] else "") + "</li>" for t in L["teile"])
        mehr += f'<details class="mehr"><summary>Was drankommt ({len(L["teile"])} Teile)</summary><div><ol>{li}</ol></div></details>'
    if mit_mehr and L.get("kurz"):
        mehr += f'<details class="mehr"><summary>Das Wichtigste in {len(L["kurz"])} Sätzen</summary><div><ol>{"".join(f"<li>{k}</li>" for k in L["kurz"])}</ol></div></details>'
    z = (u.get("fahrplan") or {}).get("zeilen")
    if mit_mehr and z:
        n = fp.stunden(u["fahrplan"])
        li = "".join(f'<li><strong>{esc(r["wann"])}</strong> · {esc(r["lesen"])}' + (f' <span class="s">Aufgaben {esc(r["aufgaben"])}</span>' if r.get("aufgaben") and r["aufgaben"] != "–" else "") + "</li>" for r in z)
        mehr = f'<details class="mehr"><summary>Fahrplan ({n} {"Stunde" if n == 1 else "Stunden"})</summary><div><ul class="fpl">{li}</ul></div></details>' + mehr
    such = esc(" ".join([u["titel"], u["kapitel"], u.get("block", "")]), quote=True)
    return f'<div class="unit{" now" if u["jetzt"] else ""}" id="{esc(u["unter"])}" data-ks-thema="{such}"><div class="eyebrow">{esc(meta)}</div><h3>{esc(u["titel"])}{badge}</h3><div class="links">{knoepfe(u)}</div>{mehr}</div>'


def seite_index(ordner, k, tests, units, bloecke, n_plan, n_begriffe, n_ziele):
    out = [klassen_kopf(f'{k["fach"]} {k["klasse"]}', "BHAK für Führung und Sicherheit · Deine Klassenseite", "index.html", f'{k["fach"]} {k["klasse"]} – Übersicht')]
    if tests:
        out.append('<a class="ks-testlink" href="#ks-tests">Test vorbereiten → Teststoff und Training</a>')
    jetzt = [u for u in units if u["jetzt"]]
    for u in jetzt:
        L = u["lern"] or {}
        out.append(ks.start(u, L.get("buch", "")))
    if tests:
        out.append('<section id="ks-tests" aria-label="Tests vorbereiten"><h2>Tests vorbereiten</h2>')
    for t in tests:
        tm = test_termine(t)
        if len(tm) > 1:
            # Eigene Termine je Klasse: Datum einmal aus dem Feld »termine«, nicht zusätzlich aus dem Kapiteltext.
            titel_tx = esc(t["kapitel"].split("·")[0].strip())
            cd = "".join(f' · {esc(kl)} {d.strftime("%d.%m.")} (<span data-datum="{d.isoformat()}"></span>)' for kl, d in tm)
        else:
            titel_tx = esc(t["kapitel"])
            cd = f' · <span data-datum="{tm[0][1].isoformat()}"></span>' if tm else ""
        out.append(f'<section class="card" style="border-left:6px solid var(--orange)"><div class="eyebrow" style="color:var(--orange)">{titel_tx}{cd}</div>'
                   f'<h3>{esc(t["titel"])} <span class="badge test">Test</span></h3><div class="links">{knoepfe(t)}</div></section>')
    if tests:
        out.append('</section>')
    out.append('<div class="ks-hilfen"><a href="begriffe.html">Begriff nachschlagen<span>Fachbegriffe A–Z mit Suche</span></a>'
               '<a href="wiederholen.html">Für den Unterricht üben<span>Lernziele und Links zum Nachlesen</span></a></div>')
    out.append('<h2 id="themen">Alle Themen</h2><div class="ks-themen-suche"><label for="ks-themen-suche">Thema finden</label>'
               '<input class="search" id="ks-themen-suche" type="search" placeholder="Titel oder Kapitel eingeben …" aria-controls="ks-themenliste">'
               '<p class="meta" id="ks-themen-treffer" role="status"></p></div><div id="ks-themenliste">')
    if not units:
        out.append('<p class="empty">Hier erscheinen die Einheiten, sobald wir damit anfangen.</p>')
    for b in bloecke:
        nr = b["nr"] or "·"
        klein = f'THEMENBLOCK {b["nr"]} VON {n_plan}' if b["nr"] else "THEMENBLOCK"
        n = len(b["units"])
        out.append(f'<details class="block ks-themenblock"><summary><span class="nr">{nr}</span><span class="t"><small>{klein} · {n} {"Einheit" if n == 1 else "Einheiten"}</small><strong>{esc(b["name"])}</strong></span></summary>'
                   f'<div class="units">{"".join(unit_html(u) for u in b["units"])}</div></details>')
    out.append('</div><p class="note">Tipp: Speichere diese Klassenseite als Favorit. Beginne oben beim aktuellen Thema. Weitere Themen findest du über die Suche.</p>')
    out.append(fuss(JS_COUNTDOWN))
    return "".join(out)


def abc_link(c):
    return f'<a href="#b-{esc(c)}">{esc(c)}</a>'


def seite_begriffe(k, units):
    out = [klassen_kopf("Fachbegriffe A–Z", f'{k["fach"]} {k["klasse"]} · alle Begriffe bisher', "begriffe.html", f'{k["fach"]} {k["klasse"]} – Fachbegriffe')]
    alle = []
    for u in units:
        for b, d in (u["lern"] or {}).get("begriffe", []):
            alle.append((b, d, u))
    alle.sort(key=lambda x: (sortkey_begriff(x[0]), kap_key(x[2]["kapitel"])))
    if not alle:
        out.append('<p class="empty">Noch keine Fachbegriffe – sie erscheinen hier, sobald die ersten Theorie-Seiten online sind.</p>')
        out.append(fuss())
        return "".join(out), 0
    beispiel = ", ".join(list(dict.fromkeys(b for b, _, _ in alle[:: max(1, len(alle) // 3)]))[:3])  # drei Begriffe der Klasse
    buchst = []
    for b, _, _ in alle:
        if buchstabe(b) not in buchst:
            buchst.append(buchstabe(b))
    out.append(f'<div class="card noprint"><label for="such" class="eyebrow">BEGRIFF SUCHEN · {len(alle)} BEGRIFFE AUS {len({id(u) for _, _, u in alle})} EINHEITEN</label>'
               f'<input id="such" class="search" type="search" placeholder="z. B. {esc(beispiel)} …" autocomplete="off">'
               f'<div class="abc">{"".join(abc_link(c) for c in buchst)}</div><p id="treffer" class="meta" style="margin:0" aria-live="polite"></p></div>')
    cur = None
    for b, d, u in alle:
        c = buchstabe(b)
        if c != cur:
            if cur is not None:
                out.append("</dl>")
            out.append(f'<h2 class="letter" id="b-{esc(c)}">{esc(c)}</h2><dl class="terms">')
            cur = c
        such = esc((b + " " + re.sub(r"<[^>]+>", "", d)).lower(), quote=True)
        out.append(f'<div data-s="{such}"><dt>{esc(b)}</dt><dd>{d}<br><a href="{esc(u["unter"])}/theorie.html#begriffe">{esc(u["kapitel"])} · {esc(u["titel"])}</a></dd></div>')
    out.append("</dl>")
    js = """
var inp = document.getElementById('such'), tr = document.getElementById('treffer');
function filt() {
  var q = inp.value.trim().toLowerCase(), n = 0;
  document.querySelectorAll('dl.terms > div').forEach(function (d) { var ok = !q || d.dataset.s.indexOf(q) > -1; d.hidden = !ok; if (ok) n++; });
  document.querySelectorAll('dl.terms').forEach(function (dl) { var leer = !dl.querySelector('div:not([hidden])'); dl.hidden = leer; dl.previousElementSibling.hidden = leer; });
  tr.textContent = q ? (n === 0 ? 'Kein Treffer – probier ein kürzeres Wort.' : n + (n === 1 ? ' Treffer' : ' Treffer')) : '';
}
inp.addEventListener('input', filt);
"""
    out.append(fuss(js))
    return "".join(out), len(alle)


def seite_wiederholen(ordner, k, units, bloecke, n_plan):
    out = [klassen_kopf("Wiederholen", f'{k["fach"]} {k["klasse"]} · alle Lernziele bisher', "wiederholen.html", f'{k["fach"]} {k["klasse"]} – Wiederholen')]
    n = sum(len((u["lern"] or {}).get("ziele", [])) for u in units)
    out.append('<section class="card"><div class="eyebrow">KANN ICH DAS?</div><p style="margin:0">Tippe bei jedem Lernziel ehrlich an, wie sicher du bist. '
               'Bei »noch nicht« steht gleich der Link zur Theorie-Seite. Deine Markierungen bleiben nur auf deinem Handy – und erscheinen auch auf den Theorie-Seiten.</p>'
               '<div class="bar" id="bar" aria-hidden="true"><i data-v="sicher" style="background:var(--green)"></i><i data-v="fast" style="background:var(--orange)"></i><i data-v="noch nicht" style="background:var(--rust)"></i></div>'
               '<div class="legend" id="leg" aria-live="polite"></div>'
               '<div class="filter noprint" role="group" aria-label="Anzeige"><button type="button" id="f-alle" aria-pressed="true">Alle Lernziele</button><button type="button" id="f-offen" aria-pressed="false">Nur noch nicht sichere</button></div></section>')
    if not n:
        out.append('<p class="empty">Noch keine Lernziele – sie erscheinen hier, sobald die ersten Theorie-Seiten online sind.</p>')
    for b in bloecke:
        teile = []
        for u in b["units"]:
            L = u["lern"] or {}
            if not (L.get("ziele") or L.get("kurz")):
                continue
            key = L["key"] if L.get("ziele_sync") else f'26-27-{ordner}-{u["unter"]}-Uebersicht-Check'
            kurz = f'<details class="mehr"><summary>Das Wichtigste in {len(L["kurz"])} Sätzen</summary><div><ol>{"".join(f"<li>{x}</li>" for x in L["kurz"])}</ol></div></details>' if L.get("kurz") else ""
            ziele = "".join(
                f'<div class="ziel" data-key="{esc(key)}" data-z="{i}"><p>{z}</p><div class="chips" role="group" aria-label="Selbstcheck">'
                + "".join(f'<button type="button" class="chip" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht"))
                + f'</div><div class="hin">→ Noch einmal lesen: <a href="{esc(u["unter"])}/theorie.html">Theorie-Seite {esc(u["kapitel"])}</a>'
                + (f' · danach das <a href="{esc(u["unter"])}/quiz.html">Quiz</a>' if "quiz.html" in u["seiten"] else "") + '</div></div>'
                for i, z in enumerate(L.get("ziele", [])))
            meta = " · ".join(x for x in [u["kapitel"], L.get("buch", "")] if x)
            teile.append(f'<div class="unit"><div class="eyebrow">{esc(meta)}</div><h3>{esc(u["titel"])}</h3>{kurz}<div>{ziele}</div>'
                         f'<div class="links">{knoepfe(u, nur=["theorie.html", "quiz.html"])}</div></div>')
        if teile:
            nr = b["nr"] or "·"
            klein = f'THEMENBLOCK {b["nr"]} VON {n_plan}' if b["nr"] else "THEMENBLOCK"
            out.append(f'<details class="block" open><summary><span class="nr">{nr}</span><span class="t"><small>{klein}</small><strong>{esc(b["name"])}</strong></span></summary><div class="units">{"".join(teile)}</div></details>')
    js = """
function lies(k) { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } }
function schreib(k, o) { try { localStorage.setItem(k, JSON.stringify(o)); } catch (e) {} }
var Z = [].slice.call(document.querySelectorAll('.ziel'));
function zeige() {
  var c = { 'sicher': 0, 'fast': 0, 'noch nicht': 0 }, cache = {};
  Z.forEach(function (z) {
    var S = cache[z.dataset.key] || (cache[z.dataset.key] = lies(z.dataset.key)), v = S[z.dataset.z] || null;
    z.querySelectorAll('.chip').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.v === v)); });
    if (v) c[v]++;
    z.classList.toggle('ok', v === 'sicher'); z.classList.toggle('nn', v === 'noch nicht');
  });
  var n = Z.length || 1, offen = Z.length - c['sicher'] - c['fast'] - c['noch nicht'];
  document.querySelectorAll('#bar i').forEach(function (i) { i.style.width = (100 * c[i.dataset.v] / n) + '%'; });
  document.getElementById('leg').innerHTML = '<span><i style="background:var(--green)"></i>' + c['sicher'] + ' sicher</span><span><i style="background:var(--orange)"></i>' + c['fast'] + ' fast</span><span><i style="background:var(--rust)"></i>' + c['noch nicht'] + ' noch nicht</span><span><i style="background:var(--line)"></i>' + offen + ' offen</span>';
}
document.addEventListener('click', function (ev) {
  var b = ev.target.closest('.chip'); if (!b) return;
  var z = b.closest('.ziel'), S = lies(z.dataset.key);
  S[z.dataset.z] = S[z.dataset.z] === b.dataset.v ? null : b.dataset.v;
  schreib(z.dataset.key, S); zeige();
});
function filter(nur) {
  document.body.classList.toggle('nur-offen', nur);
  document.getElementById('f-alle').setAttribute('aria-pressed', String(!nur));
  document.getElementById('f-offen').setAttribute('aria-pressed', String(nur));
}
document.getElementById('f-alle').onclick = function () { filter(false); };
document.getElementById('f-offen').onclick = function () { filter(true); };
window.addEventListener('pageshow', zeige);
zeige();
"""
    out.append(fuss(js))
    return "".join(out), n


def qr_svg(url):
    import qrcode, qrcode.image.svg
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, border=2, box_size=10,
                      error_correction=qrcode.constants.ERROR_CORRECT_M)
    svg = img.to_string(encoding="unicode")
    svg = re.sub(r"<\?xml[^>]*>", "", svg).replace(' id="qr-path"', "")   # sonst steht die ID mehrfach auf der Seite
    return svg.replace("<svg ", '<svg role="img" aria-label="QR-Code" ', 1)


ART = [(r"-TH-Lehrer", "PPP Lehrer"), (r"-TH-Kadetten", "PPP Kadetten"), (r"-VS-Lehrer", "PPP Versuche Lehrer"), (r"-VS-Kadetten", "PPP Versuche Kadetten"),
       (r"-UE-Lehrer", "PPP Übung Lehrer"), (r"-UE-Kadetten", "PPP Übung Kadetten"), (r"-AB", "Word Arbeitsblatt"), (r"-Loesung", "Word Lösung"),
       (r"-Fachwissen", "Word Fachwissen"), (r"-Teststoff", "Word Teststoff"), (r"-Kahoot", "Kahoot-Tabelle")]


def art(name):
    for muster, text in ART:
        if re.search(muster, name):
            return text
    return name.rsplit(".", 1)[-1].upper()


def stunden_html(e, ordner):
    """Geplante Stunden laut Jahresplan im Vergleich zum Fahrplan der Einheit – nur für die Lehrer-Seite."""
    jp = fp.jahresplan(BLOECKE, ordner, e.get("jahresplan"))
    n = fp.stunden(e.get("fahrplan"))
    if not n:
        return '<div class="warn">Fahrplan fehlt (Stunde 1, Stunde 2 …)</div>'
    if not jp:
        return f'<div class="std">⏱ Fahrplan: {n} Std. · Jahresplan: keine Stunden gefunden</div>'
    ist, brutto = jp
    # Maßgeblich ist der Fahrplan (so viele Stunden braucht die Klasse wirklich); der Jahresplan hinkt oft hinterher
    if n == ist:
        return f'<div class="std">⏱ {n} Std. · wie im Jahresplan</div>'
    return f'<div class="std">⏱ {n} Std. laut Fahrplan <span class="s">(Jahresplan: {ist})</span></div>'


def dateien_html(e):
    """Aktuell gültige Dateien einer Einheit (Feld »dateien« in einheiten.json) – nur für die Lehrer-Seite."""
    d = e.get("dateien")
    # Alte Materialnummer (Feld »alt_nummer«): Dateien behalten ihren Namen, die Zuordnung bleibt nachvollziehbar.
    alt = e.get("alt_nummer")
    hinweis = (f'<div class="alt-nr">Alte Materialnummer: <strong>{esc(alt)}</strong> – '
               f'PPP-/Word-Dateien heißen weiter so, aktuelle Unterrichtseinheit ist {esc(e.get("kapitel", ""))}.</div>') if alt else ""
    if not d:
        return hinweis + '<div class="files leer">Aktuelle PPP-/Word-Dateien: noch nicht vermerkt</div>'
    zeilen = "".join(f'<li><span class="art">{esc(art(f))}</span> <code>{esc(f)}</code></li>' for f in d.get("liste", []))
    zip_ = f'<div><span class="art">Paket</span> <code>{esc(d["zip"])}</code></div>' if d.get("zip") else ""
    stand = f' · Stand {esc(d["stand"])}' if d.get("stand") else ""
    return f'{hinweis}<details class="files"><summary>Aktuelle Dateien{stand}</summary>{zip_}<ul>{zeilen}</ul></details>'


LEHRER_CSS = """
.sichtbtn{font:inherit;font-weight:700;min-height:40px;padding:6px 12px;border-radius:10px;border:2px solid #C8102E;background:#fff;color:#C8102E;cursor:pointer}.sichtbtn.ein{border-color:#3B4A2F;color:#3B4A2F}.sichtbtn[disabled]{opacity:.5}
#sichtmsg{position:fixed;left:12px;right:12px;bottom:12px;z-index:50;padding:12px 14px;border-radius:12px;background:#1F2A1C;color:#fff;display:none}#sichtmsg.on{display:block}

.grid { display: grid; gap: 14px; grid-template-columns: 1fr; }
@media (min-width: 900px) { main.wide { max-width: 1180px; } .grid { grid-template-columns: 1fr 1fr; } .top-inner, nav.toc div, footer { max-width: 1180px; } }
.kl { display: grid; gap: 10px; }
.kl-head { display: flex; align-items: flex-start; gap: 12px; }
.kl-head .t { flex: 1; min-width: 0; }
.kl-head h3 { font-size: 26px; }
.qrbtn { flex: 0 0 auto; border: 1.5px solid var(--line); background: var(--soft); border-radius: 10px; padding: 4px; cursor: pointer; width: 76px; height: 76px; }
.qrbtn svg { width: 100%; height: 100%; display: block; }
.sub { background: var(--soft); border-radius: 10px; padding: 10px 12px; display: grid; gap: 6px; }
.sub .eyebrow { font-size: 13px; }
.warn { color: var(--rust); font-size: 14px; }
.std { color: var(--olive); font-size: 14px; font-weight: 700; }
.small a.btn { font-size: 15px; padding: 6px 12px; }
.ulist { display: grid; gap: 0; }
.ulist > div { padding: 8px 0; border-top: 1px dashed var(--line); display: grid; gap: 4px; }
.ulist > div:first-child { border-top: 0; }
.files { font-size: 14px; }
.files.leer { color: var(--muted); font-style: italic; }
.alt-nr { font-size: 14px; color: var(--muted); background: var(--soft); border-left: 4px solid var(--teal); border-radius: 6px; padding: 6px 10px; margin: 6px 0; }
.files summary { cursor: pointer; font-weight: 700; color: var(--teal); }
.files ul { margin: 4px 0 0; padding-left: 0; list-style: none; display: grid; gap: 2px; }
.files code { font-family: Consolas, "Courier New", monospace; font-size: 13px; word-break: break-all; }
.files .art { display: inline-block; min-width: 9.5em; color: var(--muted); font-weight: 700; }
.files li, .files > div { padding: 2px 0; }
@media (max-width: 600px) { .files .art { display: block; min-width: 0; font-size: 12px; } }
.tag { display: inline-block; font-size: 14px; font-weight: 700; border-radius: 999px; padding: 2px 10px; background: var(--olive); color: #fff; vertical-align: 1px; }
.url { font-size: 13px; color: var(--muted); word-break: break-all; }
#tests a { color: var(--teal); font-weight: 700; }
#beamer { position: fixed; inset: 0; z-index: 50; background: #fff; display: none; flex-direction: column; align-items: center; justify-content: center; gap: 18px; padding: 24px; text-align: center; }
#beamer.on { display: flex; }
#beamer .q { width: min(70vh, 86vw); }
#beamer .q svg { width: 100%; height: auto; display: block; }
#beamer h2 { font-size: 40px; margin: 0; }
#beamer .url { font-size: 22px; color: var(--ink); }
#beamer button { font: inherit; font-weight: 700; font-size: 18px; border: 0; border-radius: 10px; padding: 10px 22px; background: var(--olive); color: #fff; cursor: pointer; }
"""


def sicht_knopf(e, ausblenden):
    """Knopf auf der Lehrer-Seite: Einheit für diese Klasse aus- bzw. einblenden (startet die GitHub-Action)."""
    akt = "ausblenden" if ausblenden else "einblenden"
    return f'<button type="button" class="sichtbtn {"aus" if ausblenden else "ein"}" data-ordner="{esc(e["ordner"])}" data-aktion="{akt}">{"👁 Ausblenden" if ausblenden else "👁 Wieder einblenden"}</button>'


def seite_lehrer(klassen):
    klassen = sorted(klassen, key=lambda k: k["k"]["klasse"])  # 1AB, 2AB, 2AK, 3AB, 3BK, 4AB, 5AB, 5AK
    # Eine Zeile je echter Klasse: 4AB liefert zwei Zeilen (4AK 09.11., 4BK 11.11.), kein gemeinsames Datum mehr.
    tests = []
    for k in klassen:
        for t in k["tests"]:
            tm = test_termine(t)
            if tm:
                tests.extend((d, kl or k["k"]["klasse"], t, k) for kl, d in tm)
            else:
                tests.append((None, k["k"]["klasse"], t, k))
    tests.sort(key=lambda x: (x[0] is None, x[0] or HEUTE))
    out = [kopf("Lehrerzentrale", "BHAK FÜR FÜHRUNG UND SICHERHEIT · LEHRERANSICHT", "", "Lehrerzentrale – Fächer und Klassen")]
    out[0] = out[0].replace("</style>", LEHRER_CSS + ll.CSS + "</style>").replace("<main>", '<main class="wide">')
    out[0] = re.sub(r'<nav class="toc".*?</nav>', '<nav class="toc" aria-label="Lehrerzentrale"><div>'
        '<a href="#faecher">Fächer</a><a href="#schnellzugriff">Schnellzugriff</a>'
        '<a href="#tests">Tests</a><a href="#klassen-titel">Alle Materialien</a></div></nav>', out[0], flags=re.S)
    out.append(ll.uebersicht(klassen, knoepfe))
    if tests:
        li = "".join(f'<li class="lehrer-test" data-fach="{esc(k["k"]["fach"])}"><strong>{esc(k["k"]["fach"])} {esc(kl)}</strong> · {esc(t["kapitel"].split("·")[0].strip())}'
                     + (f' · {d.strftime("%d.%m.")} (<span data-datum="{d.isoformat()}"></span>)' if d else " · Termin folgt")
                     + f' · <a href="{esc(t["ordner"])}/quiz.html">Test-Training</a></li>' for d, kl, t, k in tests)
        out.append(f'<section class="card" id="tests"><h2>Tests</h2><ul style="margin:0;padding-left:20px;display:grid;gap:4px">{li}</ul>'
                   '<p class="meta" id="lehrer-tests-leer" hidden>Für dieses Fach sind noch keine Tests hinterlegt.</p></section>')
    else:
        out.append('<section class="card" id="tests"><h2>Tests</h2><p class="meta">Noch keine Tests hinterlegt.</p></section>')
    out.append('<h2 id="klassen-titel">Alle Materialien</h2><div class="grid" id="klassen">')
    for k in klassen:
        o, kk = k["ordner"], k["k"]
        url = BASIS + o + "/"
        qr = qr_svg(url)
        jetzt = next((u for u in k["units"] if u["jetzt"]), None)
        blk = next((b for b in k["bloecke"] if jetzt in b["units"]), None) if jetzt else None
        stand = f'Themenblock {blk["nr"]} von {k["n_plan"]} · {esc(blk["name"])}' if blk and blk["nr"] else "noch keine Einheit"
        aktuell_titel = jetzt["titel"] if jetzt else "Noch kein aktuelles Thema"
        h = [f'<details class="card kl lehrer-gruppe" id="{esc(o)}" {ll.attribute(k)}><summary>{esc(kk["fach"])} {esc(kk["klasse"])}'
             f'<span class="meta">{esc(aktuell_titel)}</span></summary><div class="kl-inhalt"><div class="kl-head"><div class="t"><div class="eyebrow">{stand}</div><h3>{esc(kk["fach"])} {esc(kk["klasse"])}</h3>'
             f'<div class="url">{esc(url)}</div></div>'
             f'<button type="button" class="qrbtn" data-titel="{esc(kk["fach"])} {esc(kk["klasse"])}" data-url="{esc(url)}" aria-label="QR-Code {esc(kk["klasse"])} groß zeigen">{qr}</button></div>'
             f'<div class="links small"><a class="btn" href="{esc(o)}/">Klassenseite</a><a class="btn light" href="{esc(o)}/begriffe.html">Begriffe ({k["n_b"] if k["n_b"] else "noch keine hinterlegt"})</a>'
             f'<a class="btn light" href="{esc(o)}/wiederholen.html">Wiederholen ({k["n_z"]})</a></div>']
        if jetzt:
            e2 = dict(jetzt, unter=jetzt["ordner"])
            h.append(f'<div class="sub"><div class="eyebrow">GERADE DRAN · {esc(jetzt["kapitel"])}</div><strong>{esc(jetzt["titel"])}</strong><div class="links small">{knoepfe(e2)}</div>{stunden_html(jetzt, o)}{dateien_html(jetzt)}</div>')
        rows = []
        for b in k["bloecke"]:
            for u in b["units"]:
                e2 = dict(u, unter=u["ordner"])
                warn = f'<div class="warn">Fehlt auf der Theorie-Seite: {esc(", ".join(u["fehlt"]))}</div>' if u.get("fehlt") else ""
                rows.append(f'<div><div><span class="tag">{esc(b["name"])}</span> <strong>{esc(u["kapitel"])}</strong> {esc(u["titel"])}</div><div class="links small">{knoepfe(e2)}{sicht_knopf(u, True)}</div>{stunden_html(u, o)}{dateien_html(u)}{warn}</div>')
        for t in k["tests"]:
            e2 = dict(t, unter=t["ordner"])
            rows.append(f'<div><div><span class="tag" style="background:var(--orange);color:#fff">Test</span> <strong>{esc(t["kapitel"])}</strong> {esc(t["titel"])}</div><div class="links small">{knoepfe(e2)}</div>{dateien_html(t)}</div>')
        for v in k["versteckt"]:
            e2 = dict(v, unter=v["ordner"])
            rows.append(f'<div><div><span class="tag">versteckt</span> <strong>{esc(v["kapitel"])}</strong> {esc(v["titel"])}</div><div class="links small">{knoepfe(e2)}{sicht_knopf(v, False)}</div>{dateien_html(v)}</div>')
        n = len(rows)
        h.append(f'<details class="mehr"><summary>Alle Einheiten ({n})</summary><div class="ulist">{"".join(rows)}</div></details></div></details>')
        out.append("".join(h))
    out.append("</div>")
    out.append('<div id="beamer" role="dialog" aria-modal="true" aria-hidden="true" aria-label="QR-Code für die Klasse"><h2 id="bt"></h2><div class="q" id="bq"></div><div class="url" id="bu"></div><button type="button" id="bx">Schließen</button></div>')
    js = JS_COUNTDOWN + """
var bm = document.getElementById('beamer'), fokusVorBeamer = null;
document.querySelectorAll('.qrbtn').forEach(function (b) {
  b.addEventListener('click', function () {
    fokusVorBeamer = document.activeElement;
    document.getElementById('bt').textContent = b.dataset.titel;
    document.getElementById('bu').textContent = b.dataset.url;
    document.getElementById('bq').innerHTML = b.innerHTML;
    bm.classList.add('on'); bm.setAttribute('aria-hidden', 'false'); document.getElementById('bx').focus();
  });
});
function zu() { if (!bm.classList.contains('on')) return; bm.classList.remove('on'); bm.setAttribute('aria-hidden', 'true'); if (fokusVorBeamer) fokusVorBeamer.focus(); }
var SMSG = document.createElement('div'); SMSG.id = 'sichtmsg'; document.body.appendChild(SMSG);
function sagen(t) { SMSG.textContent = t; SMSG.classList.add('on'); setTimeout(function () { SMSG.classList.remove('on'); }, 9000); }
/* Ein-/Ausblenden ohne GitHub-Token: Diese Seite liegt öffentlich auf GitHub Pages – ein Token im
   Browser-Speicher wäre für jedes Skript derselben Adresse lesbar. Stattdessen: Ordnername in die
   Zwischenablage, GitHub-Action öffnen, dort eingeloggt »Run workflow«. Kein Token auf der Webseite. */
try { localStorage.removeItem('gh_token'); } catch (e) {}   /* alten Token aufräumen, falls je einer getippt wurde */
var ACTION_URL = 'https://github.com/stephanholzer12/unterricht/actions/workflows/einheit-sichtbar.yml';
document.querySelectorAll('.sichtbtn').forEach(function (b) {
  b.addEventListener('click', function () {
    var ordner = b.dataset.ordner, aus = b.dataset.aktion === 'ausblenden';
    if (!confirm((aus ? 'Einheit ausblenden?\\n' : 'Einheit wieder einblenden?\\n') + ordner +
                 '\\n\\nNur diese Klasse. Der Direktlink bleibt aktiv.\\n\\nGitHub öffnet sich: dort »Run workflow«, Ordner einfügen, »' +
                 b.dataset.aktion + '« wählen.')) return;
    try { if (navigator.clipboard) navigator.clipboard.writeText(ordner); } catch (e) {}
    sagen('Ordner kopiert: ' + ordner + ' — in GitHub bei »Run workflow« einfügen, »' + b.dataset.aktion + '« wählen. Danach 1–2 Minuten warten und diese Seite neu laden.');
    window.open(ACTION_URL, '_blank', 'noopener');
  });
});
document.getElementById('bx').onclick = zu;
bm.addEventListener('click', function (e) { if (e.target === bm) zu(); });
document.addEventListener('keydown', function (e) { if (e.key === 'Escape') zu(); if (e.key === 'Tab' && bm.classList.contains('on')) { e.preventDefault(); document.getElementById('bx').focus(); } });
"""
    out.append(fuss(js + ll.JS, text="Lehrerzentrale v1 · wird automatisch aktualisiert · QR-Code antippen = groß für den Beamer · Öffentliche Seite, keine Zugriffssperre"))
    return "".join(out)


def anker_entfernen(e):
    """Regel: Links auf aufgaben/versuche/vertiefung/uebung/projekt.html springen immer an den ANFANG (Name und Klasse zuerst),
    nie auf einen Anker wie #card_a4. Wird bei jedem Lauf für alle Seiten jeder Einheit erzwungen."""
    n = 0
    d = os.path.join(ROOT, e["ordner"])
    if not os.path.isdir(d):
        return 0
    for f in os.listdir(d):
        if not f.endswith(".html") or f in ("index.html", "begriffe.html", "wiederholen.html"):
            continue
        pfad = os.path.join(d, f)
        t = open(pfad, encoding="utf-8").read()
        neu = re.sub(r'((?:aufgaben|versuche|vertiefung|uebung|projekt)\.html)#[A-Za-z0-9_\-]+', r'\1', t)
        if neu != t:
            open(pfad, "w", encoding="utf-8").write(neu); n += 1
    return n


def main():
    gruppen = {}
    for e in E:
        gruppen.setdefault(e["ordner"].split("/")[0], []).append(e)
    luecken, klassen = [], []
    for ordner, es in gruppen.items():
        k = es[0]
        for e in es:
            if anker_entfernen(e):
                print(f'{e["ordner"]}: Anker-Links auf das Arbeitsblatt entfernt (Sprung immer nach oben)')
        for e in es:
            if not e.get("versteckt") and not re.match(r"\d+\.\s*Test", e["kapitel"]):
                ge = fp.einbauen(e, ROOT)
                if ge:
                    print(f'{e["ordner"]}: Fahrplan aktualisiert in {", ".join(ge)}')
        tests, units, bloecke, n_plan, versteckt = daten_klasse(ordner, es)
        html_b, n_b = seite_begriffe(k, units)
        html_w, n_z = seite_wiederholen(ordner, k, units, bloecke, n_plan)
        html_i = seite_index(ordner, k, tests, units, bloecke, n_plan, n_b, n_z)
        for name, inhalt in (("index.html", html_i), ("begriffe.html", html_b), ("wiederholen.html", html_w)):
            open(os.path.join(ROOT, ordner, name), "w", encoding="utf-8").write(inhalt)
        print(f"{ordner}/: {len(units)} Einheit(en), {len(tests)} Test(s), {len(bloecke)} Block/Blöcke, {n_b} Begriffe, {n_z} Lernziele")
        for u in units:
            L, fehlt = u["lern"], []
            for s in ("theorie.html", "aufgaben.html", "quiz.html"):
                if s not in u["seiten"]:
                    fehlt.append(NAMEN[s][0])
            if L:
                if not L["begriffe"]:
                    fehlt.append("Fachbegriffe")
                if not L["kurz"]:
                    fehlt.append("»Das Wichtigste in 5 Sätzen«")
                if not L["ziele_sync"]:
                    fehlt.append("»Kann ich das?«-Selbstcheck")
            if not u.get("block"):
                fehlt.append("Block in einheiten.json")
            if not fp.stunden(u.get("fahrplan")):
                fehlt.append("Fahrplan (Stunde 1, Stunde 2 …)")
            if fehlt:
                luecken.append(f'  {u["ordner"]}: fehlt {", ".join(fehlt)}')
                u["fehlt"] = fehlt
        klassen.append({"ordner": ordner, "k": k, "tests": tests, "units": units, "bloecke": bloecke, "n_plan": n_plan,
                        "versteckt": versteckt, "n_b": n_b, "n_z": n_z})
    start = '<section class="card"><h3>Hallo!</h3><p style="margin:0">Scanne den QR-Code deiner Klasse oder öffne den Link aus LMS, um zu deinen Seiten zu kommen.</p></section>'
    seite = kopf("Unterricht am Handy", "BHAK für Führung und Sicherheit", "", "Unterricht am Handy")
    seite = re.sub(r'<nav class="toc".*?</nav>\n', "", seite, flags=re.S)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(seite + start + fuss(text="BHAK für Führung und Sicherheit"))
    print("index.html: Startseite ohne Klassenliste")
    open(os.path.join(ROOT, LEHRER), "w", encoding="utf-8").write(seite_lehrer(klassen))
    print(LEHRER + ": Lehrer-Seite mit allen Klassen (nicht verlinkt) →", BASIS + LEHRER)
    ks.einbauen(E, ROOT)
    if luecken:
        print("Lücken in den Einheiten (für die Übersicht hilfreich zu ergänzen):")
        print("\n".join(luecken))


if __name__ == "__main__":
    main()
