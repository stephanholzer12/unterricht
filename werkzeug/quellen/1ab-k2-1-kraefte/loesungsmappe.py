"""Private Lehrer-Seite (Lösungsmappe) K2.1 Mechanische Kräfte – als Artifact, nur für Prof. HOLZER.
NICHT ins öffentliche Repository legen und nicht auf Kadetten-Seiten verlinken.
Aus derselben Datenquelle wie Handy-Seiten und Unterrichts-PPP (inhalt, theorie_daten, versuche_daten, plan, fachwissen).
Aufruf: python3 loesungsmappe.py <TH-Unterricht.pptx> <Ordner mit Folienbildern s-NN.jpg> <Ziel.html>
Die Folienbilder sind die sichtbaren Folien der TH-Unterricht (LibreOffice-Render), damit die Seite am Beamer-PC als Ersatz taugt."""
import base64, glob, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, theorie_daten as TD, versuche_daten as VD, plan as P, fachwissen as F
from pptx import Presentation

PPTX, FOLDIR, ZIEL = sys.argv[1:4]
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
e = lambda t: html.escape(str(t), quote=False)


def md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(t))


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def ul(items, cls=""):
    return f"<ul class='{cls}'>" + "".join(f"<li>{md(x)}</li>" for x in items) + "</ul>"


def tab(head, rows, cls=""):
    h = "".join(f"<th>{e(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f"<div class='scroll'><table class='{cls}'><tr>{h}</tr>{b}</table></div>"


def slug(x):
    s = re.sub(r"<[^>]+>|[*_`]", "", str(x)).lower().translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))
    return "-".join(re.findall(r"[a-z0-9]+", s)[:5])


# ---------------------------------------------------------------- Überblick
uber = "<h2>Was du vor Ort noch prüfen musst</h2>" + ul(F.OFFEN)
uber += "<h2>Die sechs Stunden</h2><p>" + md(P.FAHRPLAN_TEXT) + "</p>"
uber += tab(["Std.", "Theorie / Projektschritt", "Versuch", "Aufgaben", "Zeit", "Methode"], P.STUNDENVORSCHLAG[I.KLASSEN[0]])
uber += ("<p class='klein'>Beide Klassen haben denselben Fahrplan. Die Daten stehen als »geplant« – es zählt die Reihenfolge, "
         "nicht der Termin. 1AK kann die Doppelstunde für zwei benachbarte Stunden nutzen; die Pause ist keine Arbeitszeit.</p>")

uber += "<h2>Stundenkarten (Minuten je Phase, Summe je 50)</h2>"
for std in sorted(P.STUNDE):
    t0, li = 0, []
    for name, mi, oh, a in P.STUNDE[std]:
        chip = " <span class='chip'>ohne Handy</span>" if oh and a not in ("org", "reserve", "bespr", "erkl") else ""
        li.append(f"<tr><td class='num'>{t0}–{t0 + mi}</td><td>{e(name)}{chip}</td></tr>"); t0 += mi
    offen = " open" if std == 1 else ""
    uber += (f"<details class='card'{offen}><summary><span class='nr'>{std}</span><span class='ttl'>{e(I.STUNDENNAME[std])}</span>"
             f"<span class='tag'>{e(P.METHODE[std])}</span></summary>"
             f"<div class='body'><p class='q'>Ziel: {e(P.ZIEL[std])}</p><div class='scroll'><table>{''.join(li)}</table></div>"
             f"<p class='warnline'><b>Wenn es knapp wird:</b> {e(P.KUERZEN[std].replace('Wenn es knapp wird: ', ''))}</p></div></details>")

uber += "<h2>Die 5 größten Stolpersteine</h2>" + "".join(f"<div class='fehler'><b class='k'>{e(a)}</b>{md(b)}</div>" for a, b in I.STOLPERSTEINE)

uber += "<h2>Gerätebelegung in Stunde 3</h2>" + ul([
    "**Erste 14 Minuten:** Gruppe 2 hat Kraftmesser #51, Gruppe 4 hat #52. Gruppe 7 bereitet in dieser Zeit Zeichnung, Tabelle und Erklärung vor.",
    "**Zweite 14 Minuten:** Gruppe 7 bekommt beide Geräte. Gruppen 2 und 4 werten ihre Werte aus.",
    "Die übrigen Gruppen arbeiten die ganze Zeit mit eigenen Gefäßen und Waagen – sie sind von dem Wechsel nicht betroffen.",
    "In der Präsentationsstunde die Geräte in der Reihenfolge 2, 4, 7 weitergeben.",
])

uber += "<h2>So bewertet die Seite</h2>" + ul([
    "**Automatisch geprüft:** Aufgabe 2 (5 Felder) und Aufgabe 4 (10 Felder), je 1 Punkt. Zahlen werden großzügig geprüft (Komma oder Punkt, sinnvolle Rundung, umgerechnete Einheiten); eine falsche Dimension bleibt falsch.",
    "**Du bewertest:** Aufgabe 3, das Gruppenprojekt. Raster: Inhalt 4 · Quellen 3 · Darstellung und Zeit 2 · Teamarbeit und Meilensteine 1. Halbe Punkte sind möglich.",
    "**Notenschlüssel Projekt:** ab 8,8 von 10 Sehr gut · ab 7,5 Gut · ab 6,2 Befriedigend · ab 5 Genügend · darunter Nicht genügend. Halbe Punkte nicht aufrunden.",
    "**Aufgabe 1** ist eine Schätzung ohne Punkte. Die Seite zeigt die eigene Vermutung in Stunde 6 neben der Auflösung.",
    "**Tipps kosten keine Punkte.** Im PDF steht bei jeder Aufgabe, welche Tippstufen offen waren. Nur »Lösung angesehen« zählt null Punkte.",
    "**Die Selbsteinschätzung der Kadetten ist keine Note.** Im PDF steht sie getrennt von den Punkten.",
])

uber += "<h2>Links der Kadetten-Seiten</h2><ul>" + "".join(
    f"<li><b>{lab}</b><br><span class='mono'>{I.URL}{k}.html</span></li>"
    for k, lab in (("aufgaben", "Arbeitsblatt (Schritt 1)"), ("theorie", "Theorie zum Nachschlagen"),
                   ("versuche", "Versuchsseite / Gruppenprotokoll"), ("quiz", "Kräfte-Check (Quiz)"))) + "</ul>"
uber += ("<p class='warnline'><b>Die Einheit ist noch versteckt.</b> Direktlink und QR-Code gehen schon; auf der Klassenseite erscheint sie erst nach "
         "GitHub → Actions → »Einheit ein-/ausblenden« → <span class='mono'>1ab-nawi/k2-1-kraefte</span>.</p>")

# ---------------------------------------------------------------- Herrichten (abhakbar)
ABSCHNITTE = [("chem", "Flüssigkeiten und Verbrauchsmaterial"), ("geraet", "Geräte")]
herr = ("<p>Zum Abhaken – die Haken bleiben nur in diesem Browser gespeichert. In dieser Einheit gibt es <b>keine Chemikalien</b>: "
        "nur Leitungswasser, kein Spülmittel, keine Färbelösung, keine Flamme. Nichts muss angesetzt oder verdünnt werden.</p>"
        "<div class='werkzeug'><button type='button' class='btn ghost' id='h-nur' aria-pressed='false'>Nur offene zeigen</button>"
        "<span class='zaehler' id='h-zaehler'>0 von 0 abgehakt</span><div class='balken'><i id='h-balken'></i></div></div>")

benutzt = {}
for v in VD.VS:
    for text, ic, key, n in v["mat"]:
        benutzt.setdefault(key, []).append(v["gruppe"])

herr += "<h2>Gesamtliste für alle sieben Gruppen</h2>"
n_haken = 0
for ab, lab in ABSCHNITTE:
    zeilen = [(k, g) for k, g in benutzt.items() if VD.LM[k][4] == ab]
    if not zeilen: continue
    herr += f"<h3>{e(lab)}</h3><ul class='check'>"
    for key, grp in zeilen:
        bez, ic, fund, best, art = VD.LM[key]
        gs = sorted(set(grp))
        stueck = "je Gruppe" if key in VD.JE_GRUPPE else str(len(gs))
        n_haken += 1
        herr += (f"<li><label><input type='checkbox' data-k='hm-{e(key)}'> <b>{e(stueck)}</b> · {e(bez)}"
                 f"<br><span class='klein'>{e(fund)} · Bestand laut Inventar: {e(best)} · für Gruppe {', '.join(str(g) for g in gs)}"
                 f" · am Vortag möglich</span></label></li>")
    herr += "</ul>"

herr += "<h2>Je Gruppe</h2>"
for v in VD.VS:
    herr += f"<details class='card'><summary><span class='nr'>{v['gruppe']}</span><span class='ttl'>{e(v['titel'])}</span><span class='tag'>{e(v['platz'].split(' – ')[0].split(',')[0])}</span></summary><div class='body'><ul class='check'>"
    for text, ic, key, nn in v["mat"]:
        bez, ic2, fund, best, art = VD.LM[key]
        n_haken += 1
        herr += (f"<li><label><input type='checkbox' data-k='hg-{e(v['id'])}-{e(key)}'> <b>{nn} ×</b> {md(text)}"
                 f"<br><span class='klein'>{e(fund)} · Bestand: {e(best)}</span></label></li>")
    herr += f"</ul><p class='klein'><b>Platz:</b> {e(v['platz'])}</p><p class='klein'><b>Wegräumen:</b> {e(v['entsorgung'])}</p></div></details>"

herr += "<h2>Vor der Stunde</h2><ul class='check'>"
for x in F.CHECKLISTE:
    n_haken += 1
    herr += f"<li><label><input type='checkbox' data-k='hv-{slug(x)}'> {md(x)}</label></li>"
herr += "</ul>"

# ---------------------------------------------------------------- Aufgaben
auf = []
for t in I.T:
    tags = [f"<span class='tag{' zus' if t['h'] == 0 else ''}'>{e(t['tag'])} · {t['zeit']} min</span>"]
    if t.get("besprechen"): tags.append("<span class='tag besp'>BESPRECHEN</span>")
    if t["id"] == "a2": tags.append("<span class='tag bew'>du bewertest</span>")
    if t["id"] == "v0": tags.append("<span class='tag bew'>ohne Punkte</span>")
    felder = "".join(
        f"<li>{e(f[1])}" + (f" <span class='klein'>({' · '.join(e(o) for o in f[2])})</span>" if len(f) > 2 and isinstance(f[2], (list, tuple)) else "") + "</li>"
        for f in t.get("fields", []))
    sol = "".join(f"<p>{'' if h in ('Lösung', 'Beispiel', 'Bewertung') else '<b>' + e(h) + '</b> '}{md(x)}</p>" for h, xs in t["sol"] for x in xs)
    tipps = ""
    if t.get("tipps"):
        k = t["tipps"][1]
        karte = TD.KARTEN.get(k, {}).get("titel", k)
        tipps = ("<div class='box fach'><b class='k'>Tippstufen (freiwillig, kosten keine Punkte)</b>"
                 f"<p><b>1 · Denkanstoß</b> {md(t['tipps'][0])}</p><p><b>2 · Theorie-Karte</b> {e(karte)}</p><p><b>3 · Buch</b> {md(t['tipps'][2])}</p></div>")
    auf.append(f"<details class='card' data-h='{t['h']}' data-s='{html.escape((t['title'] + ' ' + t['q']).lower(), quote=True)}'>"
               f"<summary><span class='nr'>{t['nr']}</span><span class='ttl'>{e(t['title'])}</span>{''.join(tags)}</summary>"
               f"<div class='body'><p class='q'>{md(t['q'])}</p><p class='klein'>{e(t['src'])}</p>"
               + (f"<ul class='felder'>{felder}</ul>" if felder else "")
               + f"<div class='box sol'><b class='k'>Lösung</b>{sol}</div>" + tipps
               + (f"<p class='klein'>Hinweis für Kadetten: {md(t['hint'])}</p>" if t.get("hint") else "") + "</div></details>")

filt = "".join(f"<button type='button' data-f='{h}' aria-pressed='false'>{e(I.GRP[h].split(' · ')[0])}</button>" for h in (1, 2, 6, 0))
aufgaben = (f"<input class='search' type='search' id='suche' placeholder='Aufgaben durchsuchen' aria-label='Aufgaben durchsuchen'>"
            f"<div class='filter' id='filter'>{filt}</div>" + "".join(auf) + "<p class='leer' id='leer' hidden>Nichts gefunden.</p>"
            + "<h2>Quizfragen (Kräfte-Check) mit Lösung</h2>"
            + tab(["Thema", "Frage", "Richtig", "Erklärung", "Buch"],
                  [[q[0], q[1], q[2][0], q[3], q[4]] for q in I.QUIZ]))

# ---------------------------------------------------------------- Versuche (7 Gruppen)
vs = (f"<p><b>{e(I.VS_ID)} · {e(I.VS_TITEL)}.</b> Eine Versuchs-ID für das ganze Projekt – die sieben Gruppen sind Teilaufträge, "
      "keine neuen Nummern. Alle Zahlen unten sind <b>Beispielwerte</b>, keine Messdaten.</p>")
for v in VD.VS:
    bild = UNIT + "vs-img/d_" + v["skizze"] + ".png"
    kopf = (f"<div class='vsgrid'><div><p>{md(v['intro'])}</p>"
            f"<p class='klein'>{e(v['form'])} · ca. {v['zeit']} min · {e(v['wann'])} · {e(v['bindung'])}</p>"
            f"<div class='box fach'><b class='k'>Wo steht der Versuch?</b>{e(v['platz'])}</div>"
            f"<div class='fehler'><b class='k'>Sicherheit</b>{md(v['sicher'])}</div></div>"
            + (f"<img src='{b64(bild, 'image/png')}' alt='Aufbau {e(v['titel'])}'>" if os.path.exists(bild) else "") + "</div>")
    mat = tab(["Material", "Inventar / Fundort", "Stück"],
              [[m[0], VD.LM[m[2]][2], str(m[3])] for m in v["mat"]])
    schritte = "<h3>Durchführung</h3><ol>" + "".join(f"<li>{md(s)}</li>" for s in v["schritte"]) + "</ol>"
    beob = "<h3>Beispielwerte (erfunden – das Ergebnis ist offen)</h3>" + tab(
        v["beob"]["kopf"], [z + list(v["erwartet_tab"][i]) for i, z in enumerate(v["beob"]["zeilen"][:len(v["erwartet_tab"])])])
    erw = "".join(f"<div class='box fach'><b class='k'>Erwartet: {e(a)}</b>{md(b)}</div>" for a, b in v["erwartet"])
    deut = "".join(f"<div class='box sol'><b class='k'>{lab}</b><p class='q'>{md(v[k])}</p><p>{md(v[k + '_l'])}</p></div>"
                   for k, lab in (("erk", "Erkenntnis"), ("interp", "Interpretation"), ("schluss", "Schlussfolgerung")))
    rest = ("<h3>Tipps für dich</h3>" + ul(v["lehrer"]) + "<h3>Typische Pannen</h3>"
            + "".join(f"<div class='fehler'>{md(x)}</div>" for x in v["fehler"])
            + "<h3>Fachlich genau</h3>" + "".join(f"<div class='box fach'>{md(x)}</div>" for x in v["fach"])
            + f"<div class='box bew'><b class='k'>Vorher selbst ausprobieren</b>{md(v['vorversuch'])}</div>"
            + f"<p class='klein'><b>Wegräumen:</b> {e(v['entsorgung'])}</p>"
            + f"<p class='klein'>Quelle: {e(v['quelle'])} · {e(v['jp'])}</p>")
    vs += (f"<details class='card'><summary><span class='nr'>{v['gruppe']}</span><span class='ttl'>{e(v['titel'])}</span>"
           f"<span class='tag'>{e(v['buch']['s'])}</span>{'<span class=\"tag\">KERN</span>' if v.get('kern') else '<span class=\"tag zus\">ZUSATZ</span>'}</summary>"
           f"<div class='body'>{kopf}<h3>Material</h3>{mat}{schritte}{beob}{erw}{deut}{rest}</div></details>")

vs += "<h2>Sicherheitsregeln der Messstunde</h2>" + "".join(f"<div class='fehler'><b class='k'>{e(a)}</b>{md(b)}</div>" for a, b in VD.SICHERHEIT)
vs += ("<h2>Gefahren-Check: harmlosere Alternativen</h2>" + tab(["Geprüft", "Ergebnis"], [
    ["Chemikalien", "Keine. Nur Leitungswasser. Färbelösung und Spülmittel wurden bewusst weggelassen – sie bringen für die Fragen nichts."],
    ["Flamme, Abzug", "Nicht nötig. Es wird nichts erhitzt und nichts gezündet; der mobile Abzug bleibt zu."],
    ["Glas", "Nur bei Gruppe 3 (400-ml-Becherglas und Glasstab). Alle anderen Gefäße sind PP-Kunststoff."],
    ["Spritze", "Ohne Nadel, ohne Flüssigkeit. Nicht auf Personen richten, nicht mit Gewalt drücken."],
    ["Strom und Wasser", "Waagen und Handys trocken halten. Wasser holen und ausspülen nur an der Wasserleitung."],
    ["Kraftmesser", "Langsam ziehen, unter 5 N bleiben, nie gegen Gesicht oder Körper richten."],
]))

# ---------------------------------------------------------------- Fachwissen
fw = "<h2>Lehrplanbezug</h2><ul>" + "".join(f"<li><b>{e(a)}</b> {md(b)}</li>" for a, b in F.LEHRPLAN) + "</ul>"
fw += "<h2>Die Theorie in Kurzform</h2>"
for k, karte in TD.KARTEN.items():
    bild = UNIT + karte["bild"] if karte.get("bild") else None
    fw += (f"<details class='card'><summary><span class='nr'>{e(k[1:])}</span><span class='ttl'>{e(karte['titel'])}</span>"
           f"<span class='tag'>{e(karte['buch'])}</span></summary><div class='body'>"
           + "".join(f"<p>{md(s)}</p>" for s in karte["satz"])
           + (f"<div class='bild'><img src='{b64(bild, 'image/png')}' alt='{e(karte.get('alt', ''))}'></div>" if bild and os.path.exists(bild) else "")
           + "</div></details>")
fw += "<h2>Wo die Quellen verkürzen – und was hier steht</h2>" + tab(["Quelle", "Verkürzung", "Verwendete Fassung"], F.KORREKTUREN)
fw += "<h2>Häufige Fehlvorstellungen</h2>" + tab(["Fehlvorstellung", "Richtig ist", "So zeigst du es"], F.FEHLVORSTELLUNGEN)
fw += "<h2>Fragen, die Kadetten stellen</h2>" + "".join(f"<p><b>{e(q)}</b><br>{md(a)}</p>" for q, a in F.FRAGEN)
fw += "<h2>Rechenkontrolle</h2>" + ul(F.RECHENKONTROLLE)
fw += "<h2>Fachbegriffe</h2>" + tab(I.FACHBEGRIFFE[0], I.FACHBEGRIFFE[1:])
fw += "<h2>Ausblick</h2><p>" + md(F.AUSBLICK) + "</p>"
fw += "<h2>Geprüfte Quellen</h2><ul>" + "".join(
    f"<li><b>{e(q[0])} – {e(q[1])}</b><br>{e(q[2])}<br><span class='mono'>{e(q[3])}</span></li>" for q in I.QUELLEN) + "</ul>"
fw += "<h2>Nicht geprüft – nicht eingebaut</h2>" + ul(I.NICHT_GEPRUEFT)

# ---------------------------------------------------------------- Folien (TH-Unterricht als Bilder)
prs = Presentation(PPTX)
titel = [next((ph.text_frame.text for ph in s.placeholders if ph.placeholder_format.type == 1), "") for s in prs.slides if s._element.get("show") != "0"]
bilder = sorted(glob.glob(os.path.join(FOLDIR, "s-*.jpg")))
assert len(bilder) == len(titel), (len(bilder), len(titel))
nr_phys = [i + 1 for i, s in enumerate(prs.slides) if s._element.get("show") != "0"]
folien_js = json.dumps([[b64(b, "image/jpeg"), t, n] for b, t, n in zip(bilder, titel, nr_phys)], ensure_ascii=False).replace("</", "<\\/")
optionen = "".join(f"<option value='{i}'>Folie {n} · {e(t)}</option>" for i, (t, n) in enumerate(zip(titel, nr_phys)))

STIL = open(os.path.join(HERE, "loesungsmappe_stil.css"), encoding="utf-8").read()
ZUSATZ = """
.werkzeug { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; margin: 10px 0 14px; }
.zaehler { font-weight: 700; color: var(--olive); }
.balken { flex: 1 1 140px; height: 10px; border-radius: 999px; background: #dfe4d2; overflow: hidden; }
.balken i { display: block; height: 100%; width: 0; background: var(--olive); transition: width .2s; }
.vsgrid { display: grid; grid-template-columns: 1fr; gap: 12px; align-items: start; }
.vsgrid img { width: 100%; height: auto; border-radius: 10px; background: #fff; }
@media (min-width: 760px) { .vsgrid { grid-template-columns: 1.1fr 1fr; } }
"""
seite = f"""<title>Lösungsmappe Mechanische Kräfte 1AB</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="schriften/schriften.css">
<style>{STIL}{ZUSATZ}</style>
<div class="wrap">
<header class="lese">
  <div class="eyebrow">NAWI · 1AB (1AK, 1BK) · K2.1 Mechanische Kräfte · nur für dich</div>
  <h1>Lösungen und Fachwissen: sechs Stunden mit Gruppenprojekt</h1>
  <p class="sub">Aufgaben 1–7 (5–7 Zusatz), Gruppenprojekt {e(I.VS_ID)} mit sieben Teilaufträgen, Herrichte-Liste zum Abhaken,
     die Unterrichts-PPP als Folien und das Fachwissen. Buch: Trauner NAWI HAK 1, S. 44–65. Stand {e(I.STAND)} · {e(I.V)}</p>
  <p class="warn">Privat in deinem Konto – nicht an Kadetten weitergeben und nicht ins Repository legen.
     Die Kadetten sehen Musterlösungen erst nach der PDF bzw. nach drei Fehlversuchen.</p>
</header>
<nav class="tabs" role="tablist" aria-label="Bereiche">
  <button role="tab" id="t-ueberblick" aria-selected="true">Überblick</button>
  <button role="tab" id="t-herrichten" aria-selected="false">Herrichten</button>
  <button role="tab" id="t-aufgaben" aria-selected="false">Aufgaben ({len(I.T)})</button>
  <button role="tab" id="t-versuche" aria-selected="false">Versuche ({len(VD.VS)})</button>
  <button role="tab" id="t-folien" aria-selected="false">Folien</button>
  <button role="tab" id="t-fachwissen" aria-selected="false">Fachwissen</button>
</nav>
<section class="panel lese" id="p-ueberblick">{uber}</section>
<section class="panel lese" id="p-herrichten" hidden>{herr}</section>
<section class="panel lese" id="p-aufgaben" hidden>{aufgaben}</section>
<section class="panel lese" id="p-versuche" hidden>{vs}</section>
<section class="panel" id="p-folien" hidden>
  <div class="steuer"><button class="btn ghost" id="f-zur" type="button">◀ zurück</button><button class="btn" id="f-vor" type="button">weiter ▶</button>
  <select id="f-wahl" aria-label="Folie wählen">{optionen}</select><button class="btn ghost" id="f-voll" type="button">Vollbild</button></div>
  <div class="buehne" id="buehne" tabindex="0"><img id="f-img" alt=""></div>
  <p class="hilfe">Die {len(titel)} sichtbaren Folien der TH-Unterricht (Lösungen sind hier schon aufgedeckt). Weiter: Tippen rechts, Pfeiltaste oder Leertaste ·
     zurück: Tippen links · Vollbild: Knopf oder Taste F. Die Foliennummer entspricht der Nummer in PowerPoint.</p>
</section>
<section class="panel lese" id="p-fachwissen" hidden>{fw}</section>
<footer class="lese">Gebaut aus werkzeug/quellen/1ab-k2-1-kraefte (eine Datenquelle für Handy-Seiten, Unterrichts-PPP und diese Mappe) · Stand {e(I.STAND)}</footer>
</div>
<script>
const F={folien_js};
const tabs=[...document.querySelectorAll('nav.tabs button')];
function zeige(id){{tabs.forEach(b=>{{const on=b.id==='t-'+id;b.setAttribute('aria-selected',on);document.getElementById('p-'+b.id.slice(2)).hidden=!on;}});try{{localStorage.setItem('k21-tab',id)}}catch(e){{}}}}
tabs.forEach(b=>b.addEventListener('click',()=>zeige(b.id.slice(2))));
try{{const t=localStorage.getItem('k21-tab');if(t&&document.getElementById('p-'+t))zeige(t)}}catch(e){{}}
// Herrichten: Haken merken, zählen, filtern
const PRE='k21-';
function warnung(){{const h=document.getElementById('speicherhinweis');if(h){{h.hidden=false;return;}}
  const p=document.createElement('p');p.id='speicherhinweis';p.setAttribute('role','status');p.setAttribute('aria-live','polite');
  p.style.cssText='background:#fff3cd;color:#5c4400;border:1px solid #d9b44a;padding:8px 12px;margin:8px 0;border-radius:6px';
  p.textContent='Diese Vorbereitungshaken konnten nicht gespeichert werden. Sie gelten nur für die aktuelle Sitzung.';
  const n=document.querySelector('nav.tabs');(n?n.parentNode:document.body).insertBefore(p,n?n.nextSibling:document.body.firstChild);}}
function sichern(k,v){{try{{localStorage.setItem(PRE+k,v)}}catch(e){{warnung()}}}}
try{{localStorage.setItem(PRE+'probe','1');localStorage.removeItem(PRE+'probe')}}catch(e){{warnung()}}
const haken=[...document.querySelectorAll('#p-herrichten input[data-k]')];
let nurOffen=false;
function stand(){{const n=haken.filter(c=>c.checked).length;
  document.getElementById('h-zaehler').textContent=n+' von '+haken.length+' abgehakt';
  document.getElementById('h-balken').style.width=(haken.length?100*n/haken.length:0)+'%';
  haken.forEach(c=>{{const li=c.closest('li');if(li)li.hidden=nurOffen&&c.checked;}});}}
haken.forEach(c=>{{try{{c.checked=localStorage.getItem(PRE+c.dataset.k)==='1'}}catch(e){{}}
  c.addEventListener('change',()=>{{sichern(c.dataset.k,c.checked?'1':'0');stand();}});}});
document.getElementById('h-nur').addEventListener('click',ev=>{{nurOffen=!nurOffen;ev.currentTarget.setAttribute('aria-pressed',nurOffen);
  ev.currentTarget.textContent=nurOffen?'Alle zeigen':'Nur offene zeigen';stand();}});
stand();
// Aufgaben: Suche und Filter
const karten=[...document.querySelectorAll('#p-aufgaben details.card')];let fil=null;
function filtern(){{const q=document.getElementById('suche').value.toLowerCase().trim();let n=0;
  karten.forEach(k=>{{const ok=(!q||k.dataset.s.includes(q))&&(fil===null||k.dataset.h===fil);k.hidden=!ok;if(ok)n++;}});document.getElementById('leer').hidden=n>0;}}
document.getElementById('suche').addEventListener('input',filtern);
document.querySelectorAll('#filter button').forEach(b=>b.addEventListener('click',()=>{{fil=(fil===b.dataset.f)?null:b.dataset.f;
  document.querySelectorAll('#filter button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.f===fil));filtern();}}));
// Folien
let i=0;const img=document.getElementById('f-img'),wahl=document.getElementById('f-wahl'),bu=document.getElementById('buehne');
function geh(n){{i=Math.max(0,Math.min(F.length-1,n));img.src=F[i][0];img.alt='Folie '+F[i][2]+': '+F[i][1];wahl.value=i;}}
document.getElementById('f-vor').onclick=()=>geh(i+1);document.getElementById('f-zur').onclick=()=>geh(i-1);wahl.onchange=()=>geh(+wahl.value);
bu.addEventListener('click',ev=>{{const r=bu.getBoundingClientRect();geh(ev.clientX-r.left<r.width/3?i-1:i+1)}});
document.getElementById('f-voll').onclick=()=>{{try{{bu.requestFullscreen&&bu.requestFullscreen().catch(()=>{{}})}}catch(e){{}}}};
document.addEventListener('keydown',ev=>{{if(document.getElementById('p-folien').hidden)return;
  const z=ev.target;if(z&&(/^(INPUT|SELECT|TEXTAREA)$/.test(z.tagName)||z.isContentEditable))return;
  if(ev.key===' '&&z&&/^(BUTTON|A)$/.test(z.tagName))return;
  if(['ArrowRight',' ','PageDown'].includes(ev.key)){{ev.preventDefault();geh(i+1)}}else if(['ArrowLeft','PageUp'].includes(ev.key)){{ev.preventDefault();geh(i-1)}}
  else if(ev.key==='f'||ev.key==='F')document.getElementById('f-voll').click();}});
geh(0);
</script>
"""
open(ZIEL, "w", encoding="utf-8").write(seite)
print("ok", ZIEL, len(seite) // 1024, "KB ·", len(titel), "Folien ·", n_haken, "Haken")
