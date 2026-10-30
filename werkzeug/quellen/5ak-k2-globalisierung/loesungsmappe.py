"""Private Lehrer-Seite (Lösungsmappe) K2 Globalisierung und aktuelle Weltpolitik (5AK) – als Artifact, nur für Stephan. NICHT ins öffentliche Repository legen.
Aus derselben Datenquelle wie alle anderen Ausgaben (inhalt, plan, fachwissen). Keine Versuche in IWK.
Aufruf: python3 loesungsmappe.py <TH-Unterricht.pptx> <Ordner mit Folienbildern s-NN.jpg> <Ziel.html>
Die Folienbilder sind die sichtbaren Folien der TH-Unterricht (LibreOffice-Render), damit die Seite am Beamer-PC als Ersatz taugt."""
import base64, glob, html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as P, fachwissen as F
from pptx import Presentation

PPTX, FOLDIR, ZIEL = sys.argv[1:4]
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
e = lambda t: html.escape(str(t), quote=False)


def md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(t))


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def ul(items):
    return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in items) + "</ul>"


def tab(head, rows, cls=""):
    h = "".join(f"<th>{e(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f"<div class='scroll'><table class='{cls}'><tr>{h}</tr>{b}</table></div>"


# ---------------------------------------------------------------- Überblick
offen = [
    "**Einheit einblenden** vor der ersten Stunde (Fr 13.11.): GitHub → Actions → »Einheit ein-/ausblenden« → 5ak-iwk/k2-globalisierung → einblenden. Die Direktlinks und QR-Codes funktionieren auch versteckt.",
    "**Zeit:** 4 Stunden à 50 min (Fr 13.11., 20.11., 27.11., 04.12.). Am Fr 20.11. zuerst der Test (20 min) – danach bleiben 28 min für Teil 2.",
    "**Aktualitätskarten A–E** vor jedem Termin neu prüfen (Zollrechtslage, Namen in Spitzenämtern, KI-Fristen, KI-Risiko-Quellen). Die Stände stehen im Fachwissen.",
    "**Buchbezug:** Die Stundenzuordnung zu den Buchseiten (S. 41–77) beruht auf dem Inhaltsverzeichnis. Die Seiten selbst hast du nicht als Text im Projekt – bitte kurz gegen das Buch halten.",
    "**Jahresplan:** E3+E4+E5 sind hier auf 4 Stunden zusammengefasst (Vorgabe aus der Übergabe). Kein Referat, kein Kahoot, keine Hausübung.",
    "**LMS-Abgabeordner** für 5AK anlegen (eine PDF mit Aufgaben 1–8 am Fr 04.12.).",
]
uber = "<h2>Was du vor Ort noch prüfen musst</h2>" + ul(offen)
uber += "<h2>Ablauf (3AK und 3BK gleich)</h2><p>" + md(P.FAHRPLAN_TEXT) + "</p>"
uber += tab(["Std.", "Theorie", "Versuch", "Aufgaben", "Zeit", "Methode"], F.STUNDENVORSCHLAG[I.KLASSEN[0]])
uber += "<h2>Stundenkarten (Minuten je Phase, Summe 50)</h2>"
for st in P.PLAN[I.KLASSEN[0]]:
    t0, li = 0, []
    for name, mi, oh, a in st["phasen"]:
        li.append(f"<tr><td class='num'>{t0}–{t0 + mi}</td><td>{e(name)}{' <span class=chip>ohne Handy</span>' if oh and a not in ('org', 'reserve', 'test', 'bespr', 'erkl') else ''}</td></tr>"); t0 += mi
    kn = P.KNAPP.get((I.KLASSEN[0], st["std"]))
    uber += (f"<details class='card'><summary><span class='nr'>{st['std']}</span><span class='ttl'>Stunde {st['std']} · {e(st['datum'])} · {e(I.TEILNAME[st['teile'][0]])}</span></summary>"
             f"<div class='body'><div class='scroll'><table>{''.join(li)}</table></div>" + (f"<p class='warnline'><b>Wenn es knapp wird:</b> {e(kn)}</p>" if kn else "") + "</div></details>")
uber += "<h2>Die 5 größten Stolpersteine</h2>" + "".join(f"<div class='fehler'><b class='k'>{e(a)}</b>{md(b)}</div>" for a, b in I.STOLPERSTEINE)
uber += "<h2>So bewertet die Seite</h2>" + ul([
    "**Automatisch geprüft:** Rechen- und Auswahlfelder (Aufgabe 3: Zoll 15 / Summe 115; Aufgaben 4, 5, 6: Auswahlfelder). Der Zahlenvergleich ist bewusst streng; Fehlversuche zeigen Hinweise.",
    "**Offene Texte bewertest du:** alle Textfelder (z. B. Aufgabe 3 »wer trägt die Last«, 7, 8a–c). Die Seite zeigt nur eine Schreibhilfe mit Stichwörtern und gibt dafür keine Punkte. Aufgabe 1 (Flussbild) und 8c (Urteil) haben zusätzlich ein Foto.",
    "**PDF:** Kasten »Für LMS: x von y Punkten · Notenvorschlag« zählt nur die automatisch geprüften Teile – bei dieser Einheit ist der Vorschlag darum wenig aussagekräftig; die Note kommt aus deiner Bewertung.",
    "**Keine Versuche** in IWK. Aufgabe 8 ist eine Meinungs- und Begründungsaufgabe: bewertet wird die Begründung, nicht die politische Richtung.",
])
uber += "<h2>Links der Kadetten-Seiten</h2><ul>" + "".join(f"<li><span class='mono'>{I.URL}{k}.html</span></li>" for k in ("theorie", "aufgaben", "quiz")) + "</ul>"

herr = "<h2>Vor der Stunde</h2><ul class='check'>"
for n, x in enumerate(F.CHECKLISTE, 1):
    herr += f"<li><label><input type='checkbox' id='h{n}' data-k='h{n}'> {md(x)}</label></li>"
herr += "</ul>"
uber = herr + uber

# ---------------------------------------------------------------- Aufgaben
auf = []
for t in I.T:
    man = [k for k, v in (t.get("chk") or {}).items() if v.get("man")]
    tags = [f"<span class='tag{' zus' if t['h'] == 0 else ''}'>{e(t['tag'])} · {t['zeit']} min</span>"]
    if t.get("besprechen"): tags.append("<span class='tag besp'>BESPRECHEN</span>")
    if man: tags.append("<span class='tag bew'>du bewertest</span>")
    felder = "".join(f"<li>{e(f[1])}" + (f" <span class='klein'>({' · '.join(e(o) for o in f[2])})</span>" if len(f) > 2 and isinstance(f[2], (list, tuple)) else "") + "</li>" for f in t.get("fields", []))
    sol = "".join(f"<p>{'' if h in ('Lösung', 'Beispiel', 'Bewertung') else '<b>' + e(h) + '</b> '}{md(x)}</p>" for h, xs in t["sol"] for x in xs)
    bild = f"<div class='bild'><img src='{b64(UNIT + t['img'], 'image/png')}' alt=''></div>" if t.get("img") else ""
    if t.get("tab"): bild += tab(t["tab"][0], t["tab"][1:]) + f"<p class='klein'>{e(t.get('tabnote', ''))}</p>"
    auf.append(f"<details class='card' data-h='{t['h']}' data-s='{html.escape((t["title"] + " " + t["q"]).lower(), quote=True)}'><summary><span class='nr'>{t['nr']}</span><span class='ttl'>{e(t['title'])}</span>{''.join(tags)}</summary>"
               f"<div class='body'><p class='q'>{md(t['q'])}</p>{bild}<p class='klein'>{e(t['src'])}</p><ul class='felder'>{felder}</ul>"
               f"<div class='box sol'><b class='k'>Lösung</b>{sol}</div>"
               + (f"<div class='box bew'><b class='k'>Bewertungshilfe</b>Offene Felder ({', '.join(man)}): Die Seite prüft nur Stichwörter als Schreibhilfe – fachlich entscheidest du. Musterantwort oben.</div>" if man else "")
               + (f"<p class='klein'>Hinweis für Kadetten: {md(t['hint'])}</p>" if t.get("hint") else "") + "</div></details>")
filt = "".join(f"<button type='button' data-f='{h}' aria-pressed='false'>{e(I.GRP[h].split(' · ')[0] + (' · ' + I.GRP[h].split(' · ')[1] if h else ''))}</button>" for h in (1, 2, 3, 4, 0))
aufgaben = (f"<input class='search' type='search' id='suche' placeholder='Aufgaben durchsuchen' aria-label='Aufgaben durchsuchen'><div class='filter' id='filter'>{filt}</div>"
            + "".join(auf) + "<p class='leer' id='leer' hidden>Nichts gefunden.</p>"
            + "<h2>Zusatzkarten für Schnelle (optional)</h2>" + tab(["Frage", "Lösung"], I.PARTNERKARTEN))

# ---------------------------------------------------------------- Fachwissen
fw = "<h2>Lehrplanbezug</h2><ul>" + "".join(f"<li><b>{e(a)}</b> {md(b)}</li>" for a, b in F.LEHRPLAN) + "</ul>"
for kap in F.KAPITEL:
    fw += f"<h2>{e(kap['titel'])}</h2>" + "".join(f"<p>{md(x)}</p>" for x in kap["text"])
    if kap.get("bild"): fw += f"<div class='bild'><img src='{b64(UNIT + kap['bild'], 'image/png')}' alt=''></div>"
    if kap.get("nur"): fw += "<div class='box fach'><b class='k'>Nur für dich</b>" + "".join(f"<p>{md(y)}</p>" for y in kap["nur"]) + "</div>"
    if kap.get("stolper"): fw += f"<div class='fehler'><b class='k'>Stolperstein</b>{md(kap['stolper'])}</div>"
fw += "<h2>Rechenbeispiele</h2>" + "".join(f"<p>{md(x)}</p>" for x in F.RECHNEN)
fw += "<h2>Häufige Fehlvorstellungen</h2>" + tab(["Fehlvorstellung", "Richtig ist", "So zeigst du es"], F.FEHLVORSTELLUNGEN)
fw += "<h2>Fragen, die Kadetten stellen</h2>" + "".join(f"<p><b>{e(q)}</b><br>{md(a)}</p>" for q, a in F.FRAGEN)
fw += "<h2>Videos und Podcasts</h2>" + "".join(f"<p>{md(x)}</p>" for x in F.VIDEO_NOTIZ.values())
fw += "<h2>Ausblick</h2><p>" + md(F.AUSBLICK) + "</p><h2>Quellen</h2>" + ul(F.QUELLEN)

# ---------------------------------------------------------------- Folien (TH-Unterricht als Bilder)
prs = Presentation(PPTX)
titel = [next((ph.text_frame.text for ph in s.placeholders if ph.placeholder_format.type == 1), "") for s in prs.slides if s._element.get("show") != "0"]
bilder = sorted(glob.glob(os.path.join(FOLDIR, "s-*.jpg")))
assert len(bilder) == len(titel), (len(bilder), len(titel))
nr_phys = [i + 1 for i, s in enumerate(prs.slides) if s._element.get("show") != "0"]
import json
folien_js = json.dumps([[b64(b, "image/jpeg"), t, n] for b, t, n in zip(bilder, titel, nr_phys)], ensure_ascii=False).replace("</", "<\\/")
optionen = "".join(f"<option value='{i}'>Folie {n} · {e(t)}</option>" for i, (t, n) in enumerate(zip(titel, nr_phys)))

STIL = open(os.path.join(HERE, "loesungsmappe_stil.css"), encoding="utf-8").read()
seite = f"""<title>Lösungsmappe Globalisierung 5AK</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="../../schriften/schriften.css">
<style>{STIL}</style>
<div class="wrap">
<header class="lese">
  <div class="eyebrow">IWK · 5AK (13.11.–04.12.) · K2 Globalisierung und aktuelle Weltpolitik · nur für dich</div>
  <h1>Lösungen und Fachwissen: Globalisierung und Weltpolitik</h1>
  <p class="sub">Aufgaben 1–8, die Unterrichts-PPP als Folien und das Fachwissen. Keine Versuche. Buch: Trauner IWK, S. 41–77. Stand {e(I.STAND)} · {e(I.V)}</p>
  <p class="warn">Privat in deinem Konto – nicht an Kadetten weitergeben. Die Kadetten sehen Musterlösungen erst nach der PDF bzw. nach drei Fehlversuchen.</p>
</header>
<nav class="tabs" role="tablist" aria-label="Bereiche">
  <button role="tab" id="t-ueberblick" aria-selected="true">Überblick</button>
  <button role="tab" id="t-aufgaben" aria-selected="false">Aufgaben ({len(I.T)})</button>
  <button role="tab" id="t-folien" aria-selected="false">Folien</button>
  <button role="tab" id="t-fachwissen" aria-selected="false">Fachwissen</button>
</nav>
<section class="panel lese" id="p-ueberblick">{uber}</section>
<section class="panel lese" id="p-aufgaben" hidden>{aufgaben}</section>
<section class="panel" id="p-folien" hidden>
  <div class="steuer"><button class="btn ghost" id="f-zur" type="button">◀ zurück</button><button class="btn" id="f-vor" type="button">weiter ▶</button>
  <select id="f-wahl" aria-label="Folie wählen">{optionen}</select><button class="btn ghost" id="f-voll" type="button">Vollbild</button></div>
  <div class="buehne" id="buehne" tabindex="0"><img id="f-img" alt=""></div>
  <p class="hilfe">Die {len(titel)} sichtbaren Folien der TH-Unterricht (Lösungen sind hier schon aufgedeckt). Weiter: Tippen rechts, Pfeiltaste oder Leertaste · zurück: Tippen links · Vollbild: Knopf oder Taste F. Die Foliennummer entspricht der Nummer in PowerPoint.</p>
</section>
<section class="panel lese" id="p-fachwissen" hidden>{fw}</section>
<footer class="lese">Gebaut aus werkzeug/quellen/5ak-k2-globalisierung (eine Datenquelle für Seiten, PPP und diese Mappe) · Stand {e(I.STAND)}</footer>
</div>
<script>
const F={folien_js};
const tabs=[...document.querySelectorAll('nav.tabs button')];
function zeige(id){{tabs.forEach(b=>{{const on=b.id==='t-'+id;b.setAttribute('aria-selected',on);document.getElementById('p-'+b.id.slice(2)).hidden=!on;}});try{{localStorage.setItem('k2global-tab',id)}}catch(e){{}}}}
tabs.forEach(b=>b.addEventListener('click',()=>zeige(b.id.slice(2))));
try{{const t=localStorage.getItem('k2global-tab');if(t&&document.getElementById('p-'+t))zeige(t)}}catch(e){{}}
// Herrichten: Haken merken
document.querySelectorAll('input[data-k]').forEach(c=>{{try{{c.checked=localStorage.getItem('k2global-'+c.dataset.k)==='1'}}catch(e){{}}
  c.addEventListener('change',()=>{{try{{localStorage.setItem('k2global-'+c.dataset.k,c.checked?'1':'0')}}catch(e){{}}}})}});
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
  if(['ArrowRight',' ','PageDown'].includes(ev.key)){{ev.preventDefault();geh(i+1)}}else if(['ArrowLeft','PageUp'].includes(ev.key)){{ev.preventDefault();geh(i-1)}}
  else if(ev.key==='f'||ev.key==='F')document.getElementById('f-voll').click();}});
geh(0);
</script>
"""
open(ZIEL, "w", encoding="utf-8").write(seite)
print("ok", ZIEL, len(seite) // 1024, "KB")
