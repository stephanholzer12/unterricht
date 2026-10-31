"""Lösungsübersicht für die Lehrkraft: alle Klassen und Einheiten geordnet an einer Stelle.

Die Seite wird von build_index.py bei jedem Lauf neu gebaut und liest nur einheiten.json
(Felder `lehrerseite`, `dateien`, `seiten`, `block`, `kapitel`, `titel`, `versteckt`).
Neue Einheiten erscheinen deshalb von selbst, sobald sie in einheiten.json stehen.

Keine Zugriffssperre: Die Seite liegt öffentlich auf GitHub Pages, ist aber auf keiner
Kadetten-Seite verlinkt. Die Lösungen selbst stehen NICHT hier, sondern in den privaten
Lehrer-Seiten bzw. in den Word-Dateien; die Seite enthält nur Verweise und Dateinamen.
Kein Zugriff auf localStorage (keine Antworten der Kadetten).
"""
import html
import re

esc = html.escape

FACH_REIHE = ["NAWI", "PBGW", "TÖW", "IWK"]
LOES_DATEI = re.compile(r"(?i)l(?:oe|ö)sung")
DATEI_ENDUNG = re.compile(r"(?i)\.(docx|pptx|xlsx|pdf)$")

CSS = """
/* Lösungsübersicht – nur auf dieser Seite. */
[hidden] { display: none !important; }
main.wide { max-width: 1180px; }
.top-inner, nav.toc div, footer { max-width: 1180px; }
.top-text h1 { overflow-wrap: anywhere; }
nav.toc a { min-height: 40px; display: inline-flex; align-items: center; }
/* .tag steht sonst nur im Lehrerzentrale-CSS */
.tag { display: inline-block; font-size: 14px; font-weight: 700; border-radius: 999px; padding: 2px 10px; background: var(--olive); color: #fff; vertical-align: 1px; }
.loes-hinweis { border-left: 5px solid var(--teal); }
.loes-hinweis p { margin: 4px 0; }
.loes-werkzeug { display: grid; gap: 10px; }
.loes-werkzeug label.t { display: block; font-size: 16px; font-weight: 700; margin-bottom: 5px; }
.loes-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.loes-chip { font: inherit; font-weight: 700; font-size: 16px; cursor: pointer; min-height: 44px; padding: 6px 14px; border-radius: 999px;
  border: 2px solid var(--line); background: var(--card); color: var(--olive); }
.loes-chip[aria-pressed="true"] { border-color: var(--olive); background: var(--olive); color: #fff; }
.loes-nur { display: flex; align-items: center; gap: 10px; min-height: 44px; font-weight: 700; cursor: pointer; }
.loes-nur input { width: 22px; height: 22px; accent-color: var(--olive); }
#loes-stand { margin: 0; }
.loes-klasse { padding: 0; overflow: hidden; scroll-margin-top: 70px; }
.loes-klasse > h2 { margin: 0; padding: 14px 16px; font-size: 24px; border-bottom: 3px solid var(--fachfarbe, var(--olive)); display: flex; align-items: baseline; flex-wrap: wrap; gap: 4px 12px; }
.loes-klasse > h2 .meta { font-family: var(--font-body); font-size: 15px; font-weight: 400; }
.loes-klasse.f-nawi { --fachfarbe: #286977; } .loes-klasse.f-pbgw { --fachfarbe: #345B86; }
.loes-klasse.f-toew { --fachfarbe: #3B4A2F; } .loes-klasse.f-iwk { --fachfarbe: #8C3B2E; }
.loes-klasse > h2 a { color: var(--fachfarbe, var(--olive)); text-decoration: none; }
.loes-liste { display: grid; }
.loes-zeile { padding: 14px 16px; border-top: 1px solid var(--line); display: grid; gap: 8px; min-width: 0; }
.loes-zeile:first-child { border-top: 0; }
.loes-kopf { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 10px; overflow-wrap: anywhere; }
.loes-kopf strong { font-size: 19px; }
.chip { display: inline-block; font-size: 14px; font-weight: 700; border-radius: 999px; padding: 2px 10px; white-space: nowrap; }
.chip.seite { background: #E1EFC9; color: #2C4A0C; border: 1.5px solid #7FA83A; }
.chip.word { background: #FBE9D4; color: #7A3E0A; border: 1.5px solid var(--orange); }
.chip.keine { background: #ECEDE6; color: #4A503F; border: 1.5px solid #B9BFA9; }
.chip.test { background: #E3EEF1; color: #1F5662; border: 1.5px solid var(--teal); }
.chip.versteckt { background: #fff; color: var(--rust); border: 1.5px solid var(--rust); }
.loes-zeile .links a.btn { min-height: 44px; display: inline-flex; align-items: center; }
.loes-zeile details { font-size: 14px; }
.loes-zeile summary { cursor: pointer; font-weight: 700; color: var(--teal); min-height: 32px; }
.loes-zeile ul { margin: 4px 0 0; padding-left: 0; list-style: none; display: grid; gap: 2px; }
.loes-zeile code { font-family: Consolas, "Courier New", monospace; font-size: 13px; overflow-wrap: anywhere; word-break: break-all; }
.loes-zeile .zip { color: var(--muted); margin-top: 4px; }
.loes-leer { padding: 16px; color: var(--muted); font-style: italic; }
@media (min-width: 900px) { .loes-zeile { grid-template-columns: minmax(0, 1.1fr) minmax(0, 1.4fr); align-items: start; }
  .loes-zeile .loes-kopf, .loes-zeile .loes-dateien { grid-column: 1; } .loes-zeile .links, .loes-zeile .loes-sonst { grid-column: 2; grid-row: 1 / span 2; } }
@media print { .loes-werkzeug, #loes-sprung { display: none !important; } }
"""

JS = """
/* Keine localStorage-Zugriffe: Filter verändern nichts Gespeichertes. */
(function () {
  var fach = '', nur = false, input = document.getElementById('loes-suche');
  var chips = Array.from(document.querySelectorAll('.loes-chip[data-fach-filter]'));
  var sprung = Array.from(document.querySelectorAll('#loes-sprung a'));
  var klassen = Array.from(document.querySelectorAll('.loes-klasse'));
  var stand = document.getElementById('loes-stand'), leer = document.getElementById('loes-leer');
  function normal(s) { return String(s).toLowerCase().replace(/ß/g, 'ss').normalize('NFD').replace(/[\\u0300-\\u036f]/g, ''); }
  function filtern() {
    var woerter = normal(input.value).trim().split(/\\s+/).filter(Boolean), zeilen = 0, klassenAnz = 0;
    klassen.forEach(function (k) {
      var sicht = 0;
      var fachOk = !fach || k.dataset.fach === fach;
      Array.from(k.querySelectorAll('.loes-zeile')).forEach(function (z) {
        var text = normal(k.dataset.suche + ' ' + z.dataset.suche);
        var ok = fachOk && (!nur || z.dataset.status === 'seite') && woerter.every(function (w) { return text.indexOf(w) >= 0; });
        z.hidden = !ok;
        if (ok) sicht++;
      });
      k.hidden = sicht === 0;
      if (sicht) { zeilen += sicht; klassenAnz++; }
    });
    sprung.forEach(function (a) {
      var k = document.getElementById(a.getAttribute('href').slice(1));
      a.hidden = !k || k.hidden;
    });
    stand.textContent = zeilen + (zeilen === 1 ? ' Einheit' : ' Einheiten') + ' in ' + klassenAnz + (klassenAnz === 1 ? ' Klasse' : ' Klassen') + ' angezeigt';
    leer.hidden = zeilen > 0;
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var an = c.getAttribute('aria-pressed') !== 'true';
      chips.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      c.setAttribute('aria-pressed', an ? 'true' : 'false');
      fach = an ? c.dataset.fachFilter : '';
      filtern();
    });
  });
  document.getElementById('loes-nur').addEventListener('change', function (e) { nur = e.target.checked; filtern(); });
  input.addEventListener('input', filtern);
  document.getElementById('loes-alle').addEventListener('click', function () {
    fach = ''; nur = false; input.value = '';
    document.getElementById('loes-nur').checked = false;
    chips.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
    filtern();
  });
  filtern();
})();
"""


def _loesungsdateien(e):
    """Word-/Datei-Lösungen einer Einheit (nur echte Dateinamen, keine Hinweistexte)."""
    liste = (e.get("dateien") or {}).get("liste", [])
    return [f for f in liste if LOES_DATEI.search(f) and DATEI_ENDUNG.search(f)]


def _status(e, ist_test, dateien):
    if e.get("lehrerseite"):
        return "seite", "Lehrer-Seite vorhanden"
    if dateien:
        return "word", "Nur Word-Lösung"
    if ist_test:
        return "test", "Test-Training"
    return "keine", "Noch keine Lösung hinterlegt"


def _sortkey(e, plan, ist_test, kap_key):
    block = e.get("block") or ""
    return (ist_test, plan.index(block) if block in plan else 999, kap_key(e["kapitel"]), e["ordner"])


def _zeile(e, ist_test, knoepfe):
    dateien = _loesungsdateien(e)
    status, text = _status(e, ist_test, dateien)
    block = re.sub(r"^[A-Z]\s+", "", e.get("block") or "")
    kopf = ['<div class="loes-kopf">']
    if ist_test:
        kopf.append('<span class="tag" style="background:var(--orange);color:#fff">Test</span>')
    elif block:
        kopf.append(f'<span class="tag">{esc(block)}</span>')
    kopf.append(f'<strong>{esc(e["kapitel"])}</strong> <span>{esc(e["titel"])}</span>')
    if e.get("versteckt"):
        kopf.append('<span class="chip versteckt">für Kadetten ausgeblendet</span>')
    kopf.append(f'<span class="chip {status}">{esc(text)}</span></div>')
    links = []
    if e.get("lehrerseite"):
        links.append(f'<a class="btn teal" href="{esc(e["lehrerseite"])}" target="_blank" rel="noopener noreferrer">Lösungen öffnen (Lehrer-Seite)</a>')
    links.append(knoepfe(dict(e, unter=e["ordner"])))
    teile = [f'<div class="links small">{"".join(links)}</div>']
    if dateien:
        lis = "".join(f"<li><code>{esc(f)}</code></li>" for f in dateien)
        zip_ = (e.get("dateien") or {}).get("zip")
        zeile = f'<div class="zip">Paket: <code>{esc(zip_)}</code></div>' if zip_ else ""
        teile.append(f'<details class="loes-dateien"><summary>Lösungs-Dateien (Word) · {len(dateien)}</summary><ul>{lis}</ul>{zeile}</details>')
    suche = " ".join([e["kapitel"], e["titel"], e.get("block") or "", text, *dateien])
    return (f'<article class="loes-zeile" data-status="{status}" data-suche="{esc(suche, quote=True)}">'
            f'{"".join(kopf)}{"".join(teile)}</article>')


def seite(klassen, *, kopf, fuss, knoepfe, kap_key, bloecke, lehrer_seite):
    """Baut die komplette Lösungsübersicht als HTML-Text.

    klassen       – Liste der Klassen-Dicts aus build_index.main()
    kopf / fuss   – Seitenkopf bzw. -fuß von build_index
    knoepfe       – Funktion für die Seiten-Knöpfe einer Einheit
    kap_key       – Sortierschlüssel für Kapitelnummern
    bloecke       – Dict Klasse → Blöcke laut Jahresplan (Reihenfolge)
    lehrer_seite  – Dateiname der Lehrerzentrale (Rücklink)
    """
    def fachpos(k):
        f = k["k"]["fach"]
        return (FACH_REIHE.index(f) if f in FACH_REIHE else 99, k["k"]["klasse"])

    ordnung = sorted(klassen, key=fachpos)
    faecher = [f for f in FACH_REIHE if any(k["k"]["fach"] == f for k in ordnung)]
    faecher += sorted({k["k"]["fach"] for k in ordnung} - set(FACH_REIHE))

    n_einheiten = n_seiten = n_word = n_keine = 0
    karten, mit_karte = [], []
    for k in ordnung:
        o, fach, klasse = k["ordner"], k["k"]["fach"], k["k"]["klasse"]
        plan = [b["block"] for b in bloecke.get(o, [])]
        zeilen = [(e, False) for e in k["units"] + k["versteckt"]
                  if not re.match(r"\d+\.\s*Test", e["kapitel"])]
        zeilen += [(e, True) for e in k["tests"]]
        zeilen += [(e, True) for e in k["versteckt"] if re.match(r"\d+\.\s*Test", e["kapitel"])]
        zeilen.sort(key=lambda z: _sortkey(z[0], plan, z[1], kap_key))
        if not zeilen:
            continue
        mit = sum(1 for e, t in zeilen if e.get("lehrerseite"))
        fachlich = [(e, t) for e, t in zeilen if not t]
        n_einheiten += len(fachlich)
        n_seiten += sum(1 for e, t in fachlich if e.get("lehrerseite"))
        n_word += sum(1 for e, t in fachlich if not e.get("lehrerseite") and _loesungsdateien(e))
        n_keine += sum(1 for e, t in fachlich if not e.get("lehrerseite") and not _loesungsdateien(e))
        stil = {"NAWI": "nawi", "PBGW": "pbgw", "TÖW": "toew", "IWK": "iwk"}.get(fach, "nawi")
        meta = f"{len(fachlich)} Einheiten · {mit} Lehrer-Seiten" if len(fachlich) != 1 else f"1 Einheit · {mit} Lehrer-Seiten"
        suche = f"{fach} {klasse}"
        mit_karte.append(k)
        karten.append(
            f'<section class="card loes-klasse f-{stil}" id="l-{esc(o)}" data-fach="{esc(fach)}" data-suche="{esc(suche, quote=True)}">'
            f'<h2><a href="{esc(o)}/">{esc(fach)} {esc(klasse)}</a><span class="meta">{esc(meta)}</span></h2>'
            f'<div class="loes-liste">{"".join(_zeile(e, t, knoepfe) for e, t in zeilen)}</div></section>')

    sprung = "".join(f'<a class="btn light" href="#l-{esc(k["ordner"])}">{esc(k["k"]["fach"])} {esc(k["k"]["klasse"])}</a>'
                     for k in mit_karte)
    chips = "".join(f'<button type="button" class="loes-chip" data-fach-filter="{esc(f)}" aria-pressed="false">{esc(f)}</button>' for f in faecher)

    out = [kopf("Lösungen – alle Klassen", "BHAK FÜR FÜHRUNG UND SICHERHEIT · LEHRERANSICHT · PRIVAT", "", "Lösungen – alle Klassen")]
    out[0] = out[0].replace("</style>", CSS + "</style>").replace("<main>", '<main class="wide">')
    out[0] = re.sub(r'<nav class="toc".*?</nav>',
                    f'<nav class="toc" aria-label="Lösungsübersicht"><div><a href="{esc(lehrer_seite)}">← Lehrerzentrale</a>'
                    '<a href="#loes-werkzeug">Suchen</a><a href="#loes-sprung">Klassen</a></div></nav>', out[0], flags=re.S)
    out.append(
        '<section class="card loes-hinweis" aria-labelledby="loes-info"><h2 id="loes-info" style="margin:0 0 4px">Alle Lösungen an einer Stelle</h2>'
        f'<p><strong>{n_einheiten} Einheiten</strong> aus {len(ordnung)} Klassen: '
        f'<span class="chip seite">{n_seiten} mit Lehrer-Seite</span> '
        f'<span class="chip word">{n_word} nur Word-Lösung</span> '
        f'<span class="chip keine">{n_keine} ohne Lösung</span></p>'
        '<p class="meta">Neue Einheiten erscheinen hier automatisch, sobald sie in der Plattform eingetragen sind. '
        'Die Lösungen selbst liegen in deinen privaten Lehrer-Seiten (Anmeldung mit deinem Claude-Konto) bzw. in den Word-Dateien – '
        'diese Seite ist nur das geordnete Inhaltsverzeichnis. Öffentliche Adresse ohne Zugriffssperre: nicht weitergeben, nicht für Kadetten verlinken.</p></section>')
    out.append(
        '<section class="card loes-werkzeug" id="loes-werkzeug" aria-label="Lösungen filtern">'
        '<div><label class="t" for="loes-suche">Klasse, Thema oder Dateiname suchen</label>'
        '<input class="search" type="search" id="loes-suche" placeholder="z. B. 4AB, Wellen oder Redox" autocomplete="off"></div>'
        f'<div class="loes-chips" role="group" aria-label="Fach wählen">{chips}</div>'
        '<label class="loes-nur"><input type="checkbox" id="loes-nur"> Nur Einheiten mit Lehrer-Seite zeigen</label>'
        '<div class="loes-chips"><button type="button" class="loes-chip" id="loes-alle">Alle anzeigen</button></div>'
        '<p class="meta" id="loes-stand" role="status"></p></section>')
    out.append(f'<nav id="loes-sprung" class="links small" aria-label="Zu einer Klasse springen">{sprung}</nav>')
    out.extend(karten)
    out.append('<p class="empty" id="loes-leer" hidden>Keine passende Einheit gefunden. Suche ändern oder „Alle anzeigen“ wählen.</p>')
    out.append(fuss(JS, text="Lösungsübersicht v1 · wird automatisch aktualisiert · Öffentliche Seite, keine Zugriffssperre – nur für die Lehrkraft"))
    return "".join(out)
