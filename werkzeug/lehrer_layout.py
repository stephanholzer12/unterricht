"""Lehrerzentrale v1: Fachauswahl und Schnellzugriff, nur auf der Lehrer-Seite.

Keine Anmeldung und keine Zugriffssperre: Die Kadetten-Seiten erhalten weder
die Fachauswahl noch Links zur Lehrerzentrale oder zu anderen Klassenseiten.
"""
import html

esc = html.escape
FAECHER = [
    ("NAWI", "Naturwissenschaften", "nawi"),
    ("PBGW", "Politische Bildung, Geschichte und Wirtschafts- und Sozialgeschichte", "pbgw"),
    ("TÖW", "Technologie, Ökologie und Warenlehre", "toew"),
    ("IWK", "Internationale Wirtschafts- und Kulturräume", "iwk"),
]


def suchtext(k):
    """Nur vorhandene Metadaten, keine Antworten oder Browser-Speicherstände."""
    fach = k["k"]["fach"]
    lang = next((name for kurz, name, _ in FAECHER if kurz == fach), fach)
    daten = [fach, lang, k["k"]["klasse"]]
    for e in k["units"] + k["tests"] + k["versteckt"]:
        daten.extend([e.get("titel", ""), e.get("kapitel", ""), e.get("block", "")])
        dateien = e.get("dateien", {})
        daten.extend(dateien.get("liste", []))
        daten.append(dateien.get("zip", ""))
    return " ".join(daten)


def attribute(k):
    return f'data-fach="{esc(k["k"]["fach"], quote=True)}" data-suche="{esc(suchtext(k), quote=True)}"'


def uebersicht(klassen, knoepfe):
    """Fachkarten und eine kompakte Zeile je vorhandener Fach-/Klassengruppe."""
    out = ['<section id="faecher" aria-labelledby="faecher-titel"><div class="lehrer-heading">'
           '<h2 id="faecher-titel">Deine Fächer</h2><span class="meta">Lehrerzentrale · v1</span></div>'
           '<div class="fachkarten">']
    vorhanden = {k["k"]["fach"] for k in klassen}
    faecher = FAECHER + [(f, f, "weiteres") for f in sorted(vorhanden - {f[0] for f in FAECHER})]
    for fach, name, stil in faecher:
        gruppe = [k for k in klassen if k["k"]["fach"] == fach]
        if not gruppe:
            continue
        namen = " · ".join(k["k"]["klasse"] for k in gruppe)
        out.append(f'<button type="button" class="fachkarte fach-{stil}" data-fach-filter="{esc(fach)}" '
                   f'aria-pressed="false" aria-controls="schnellzugriff klassen tests">'
                   f'<strong>{esc(fach)}</strong><span>{esc(name)}</span><small>{esc(namen)}</small></button>')
    out.append('</div></section><section class="card lehrer-werkzeuge" aria-label="Materialien filtern">'
               '<div class="lehrer-suchfeld"><label for="lehrer-suche">Klasse, Thema oder Dateiname suchen</label>'
               '<input class="search" type="search" id="lehrer-suche" placeholder="z. B. 4AB, Magnet oder Teststoff" '
               'aria-controls="schnellzugriff klassen"></div>'
               '<button type="button" class="lehrer-reset" id="lehrer-alle">Alle anzeigen</button>'
               '<p class="meta" id="lehrer-filterstand" role="status"></p></section>')
    out.append('<section id="schnellzugriff" aria-labelledby="schnell-titel"><h2 id="schnell-titel">Schnellzugriff</h2>'
               '<p class="meta">Aktuelles Thema je Fach-/Klassengruppe · Material direkt öffnen</p><div class="lehrer-zeilen">')
    for k in klassen:
        fach, klasse, o = k["k"]["fach"], k["k"]["klasse"], k["ordner"]
        jetzt = [u for u in k["units"] if u["jetzt"]]
        out.append(f'<article class="lehrer-zeile lehrer-gruppe" {attribute(k)}>'
                   f'<div class="lehrer-gruppenname"><a href="{esc(o)}/">{esc(fach)} {esc(klasse)}</a>'
                   f'<div class="meta">Klassenseite</div></div><div class="lehrer-aktuell">')
        for u in jetzt:
            e = dict(u, unter=u["ordner"])
            out.append(f'<div><div class="eyebrow">{esc(u["kapitel"])}</div><strong>{esc(u["titel"])}</strong>'
                       f'<div class="links small">{knoepfe(e, nur=["theorie.html", "aufgaben.html", "versuche.html", "quiz.html"])}</div></div>')
        if not jetzt:
            out.append('<span class="meta">Noch kein aktuelles Thema hinterlegt</span>')
        out.append(f'</div><div class="lehrer-aktionen"><a href="#{esc(o)}">Alle Materialien</a>'
                   f'<button type="button" class="lehrer-qr" data-qr-ziel="{esc(o)}" '
                   f'aria-label="QR-Code für {esc(fach)} {esc(klasse)} groß zeigen">QR-Code</button></div></article>')
    out.append('</div><p class="empty" id="lehrer-leer" hidden>Keine passende Gruppe gefunden. '
               'Suche ändern oder „Alle anzeigen“ wählen.</p></section>')
    return "".join(out)


CSS = """
/* Lehrerzentrale v1 – nur in seite_lehrer eingebaut. */
[hidden] { display: none !important; }
main.wide { max-width: 1180px; }
.top-inner, nav.toc div, footer { max-width: 1180px; }
.top-text h1 { overflow-wrap: anywhere; }
nav.toc a { min-height: 40px; display: inline-flex; align-items: center; }
.lehrer-heading { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-bottom: 12px; }
.lehrer-heading h2 { margin: 0; }
.fachkarten { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }
.fachkarte { --fachfarbe: var(--olive); font: inherit; text-align: left; cursor: pointer; padding: 16px; border: 2px solid var(--line); border-top: 5px solid var(--fachfarbe); border-radius: 14px; background: var(--card); color: var(--ink); display: grid; align-content: start; gap: 6px; }
.fach-nawi { --fachfarbe: #286977; } .fach-pbgw { --fachfarbe: #345B86; } .fach-toew { --fachfarbe: #3B4A2F; } .fach-iwk { --fachfarbe: #8C3B2E; }
.fachkarte strong { color: var(--fachfarbe); font-family: var(--font-head); font-size: 28px; }
.fachkarte span { font-size: 16px; } .fachkarte small { color: var(--muted); font-size: 14px; }
.fachkarte[aria-pressed="true"] { border-color: var(--fachfarbe); background: var(--soft); }
.lehrer-werkzeuge { grid-template-columns: minmax(0, 1fr) auto; align-items: end; gap: 8px 14px; }
.lehrer-suchfeld label { display: block; font-size: 16px; font-weight: 700; margin-bottom: 5px; }
.lehrer-reset, .lehrer-qr { font: inherit; font-weight: 700; cursor: pointer; border: 1.5px solid var(--line); border-radius: 10px; color: var(--olive); background: var(--soft); min-height: 44px; padding: 8px 12px; }
#lehrer-filterstand { grid-column: 1 / -1; margin: 0; }
#schnellzugriff > h2 { margin-bottom: 4px; } #schnellzugriff > p { margin: 0 0 12px; }
.lehrer-zeilen { background: var(--card); border-radius: 14px; box-shadow: 0 2px 6px rgba(31,42,28,.12); }
.lehrer-zeile { display: grid; grid-template-columns: 120px minmax(0, 1fr) 132px; gap: 16px; padding: 16px; border-bottom: 1px solid var(--line); align-items: start; }
.lehrer-zeile:last-child { border-bottom: 0; }
.lehrer-gruppenname a, .lehrer-aktionen a { color: var(--teal); font-weight: 700; }
.lehrer-gruppenname a { font-size: 19px; }
.lehrer-aktionen { display: grid; gap: 6px; }
.lehrer-aktionen a { min-height: 44px; display: flex; align-items: center; font-size: 15px; }
.lehrer-aktuell { display: grid; gap: 14px; min-width: 0; overflow-wrap: anywhere; }
.lehrer-aktuell .links { margin-top: 8px; } .lehrer-aktuell a.btn { min-height: 40px; display: inline-flex; align-items: center; }
.lehrer-gruppe { min-width: 0; }
details.kl { display: block; padding: 0; align-self: start; }
details.kl > summary { cursor: pointer; padding: 16px; font-weight: 700; color: var(--olive); overflow-wrap: anywhere; }
details.kl > summary .meta { display: block; font-weight: 400; padding-left: 20px; }
.kl-inhalt { display: grid; gap: 12px; padding: 0 16px 16px; }
.kl-inhalt .kl-head h3 { font-size: 22px; }
#klassen-titel { margin-bottom: 0; }
@media (max-width: 920px) { .fachkarten { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 600px) { .lehrer-zeile { grid-template-columns: 1fr; gap: 8px; } .lehrer-aktionen { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 16px; } .lehrer-werkzeuge { grid-template-columns: 1fr; } .lehrer-reset { justify-self: start; } nav.toc div { flex-wrap: wrap; overflow-x: visible; } }
@media (max-width: 600px) { html { scroll-padding-top: 120px; } }
@media (max-width: 380px) { .fachkarten { grid-template-columns: 1fr; } }
@media (pointer: coarse) { .lehrer-aktuell a.btn, nav.toc a { min-height: 44px; } }
@media print { .fachkarten, .lehrer-werkzeuge, .lehrer-aktionen { display: none !important; } }
"""


JS = """
/* Keine localStorage-Zugriffe: Lehrerfilter verändern keine gespeicherten Antworten. */
(function () {
  var fach = '', input = document.getElementById('lehrer-suche');
  var karten = Array.from(document.querySelectorAll('[data-fach-filter]'));
  var gruppen = Array.from(document.querySelectorAll('.lehrer-gruppe'));
  var vorherOffen = new Map();
  function normal(s) { return String(s).toLowerCase().replace(/ß/g, 'ss').normalize('NFD').replace(/[\\u0300-\\u036f]/g, ''); }
  function filtern() {
    var woerter = normal(input.value).trim().split(/\\s+/).filter(Boolean), n = 0;
    gruppen.forEach(function (g) {
      var text = normal(g.dataset.suche);
      var passt = (!fach || g.dataset.fach === fach) && woerter.every(function (w) { return text.indexOf(w) >= 0; });
      g.hidden = !passt;
      if (g.classList.contains('lehrer-zeile') && passt) n++;
      if (g.matches('details.kl')) {
        [g].concat(Array.from(g.querySelectorAll('details.mehr'))).forEach(function (d) {
          if (woerter.length && passt) { if (!vorherOffen.has(d)) vorherOffen.set(d, d.open); d.open = true; }
        });
      }
    });
    if (!woerter.length) { vorherOffen.forEach(function (offen, d) { d.open = offen; }); vorherOffen.clear(); }
    document.querySelectorAll('.lehrer-test').forEach(function (t) { t.hidden = !!fach && t.dataset.fach !== fach; });
    var testLeer = document.getElementById('lehrer-tests-leer');
    if (testLeer) testLeer.hidden = Array.from(document.querySelectorAll('.lehrer-test')).some(function (t) { return !t.hidden; });
    document.getElementById('lehrer-filterstand').textContent = (fach || 'Alle Fächer') + ' · ' + n + ' von ' + document.querySelectorAll('.lehrer-zeile').length + ' Gruppen';
    document.getElementById('lehrer-leer').hidden = n !== 0;
    karten.forEach(function (k) { k.setAttribute('aria-pressed', String(k.dataset.fachFilter === fach)); });
  }
  karten.forEach(function (k) { k.addEventListener('click', function () { fach = fach === k.dataset.fachFilter ? '' : k.dataset.fachFilter; filtern(); }); });
  input.addEventListener('input', filtern);
  document.getElementById('lehrer-alle').addEventListener('click', function () { fach = ''; input.value = ''; filtern(); });
  document.querySelectorAll('[data-qr-ziel]').forEach(function (b) { b.addEventListener('click', function () {
    var gruppe = document.getElementById(b.dataset.qrZiel), qr = gruppe && gruppe.querySelector('.qrbtn');
    if (qr) qr.click();
  }); });
  function zielOeffnen() {
    var id; try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { return; }
    var ziel = id && document.getElementById(id);
    if (ziel && ziel.matches('details.kl')) { fach = ''; input.value = ''; filtern(); ziel.open = true; ziel.scrollIntoView(); }
  }
  window.addEventListener('hashchange', zielOeffnen);
  filtern(); zielOeffnen();
})();
"""
