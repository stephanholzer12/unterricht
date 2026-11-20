"""Mitarbeits-Check K6–7 Wahlrecht und Parteien (2AK) – baut 2ak-pbgw/k6-7-parteien/check.html.
Stephan 15.11.2026: nach jeder Einheit ein kurzer Kontroll-Check mit Benotung (kein Test), auf GitHub, 10 Fragen.

So funktioniert die Seite:
  - Name und Klasse eintragen, »Check starten«. Aus dem Fragenpool (inhalt.CHECK) werden 10 Fragen gezogen, Antworten gemischt;
    die Zahlenfrage bekommt Zufallszahlen. Die Ziehung wird gespeichert – Neuladen ändert nichts.
  - Keine Tipps, kein »Prüfen«, keine Lösung. Nach »Abgeben« ist der Check gesperrt; gezählt wird nur dieser eine Versuch.
  - Punkte und Notenvorschlag (88/75/62/50 %) stehen nur im PDF; dort pro Frage richtig/falsch, aber NICHT die richtige Antwort
    (sonst könnten Kadetten, die später schreiben, abschreiben). Die Lösungen stehen auf Stephans privater Lösungsseite.
  - Die richtigen Antworten stehen nicht im Klartext im Seitencode, sondern nur als Prüfsumme (FNV-1a). Das schützt vor
    schnellem Nachsehen, nicht vor Absicht – darum »Mitarbeit«, kein Test (Stephans Entscheidung, 15.11.2026).
Speicherschlüssel: inhalt.CHECK_KEY (nie umbenennen). Aufruf im Repository-Ordner: python3 werkzeug/quellen/2ak-k6-7-parteien/check.py"""
import html, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

SALZ = "k67-mc|"


def fnv(t):
    h = 2166136261
    for ch in t:
        c = ord(ch)
        if c > 0xFFFF:  # wie JavaScript (UTF-16)
            c -= 0x10000
            for u in (0xD800 + (c >> 10), 0xDC00 + (c & 0x3FF)):
                h = ((h ^ u) * 16777619) & 0xFFFFFFFF
            continue
        h = ((h ^ c) * 16777619) & 0xFFFFFFFF
    return h


POOL = []
for g in I.CHECK:
    fr = []
    for qid, frage, ok, falsch, buch in g["fragen"]:
        if frage == "faktor":
            fr.append({"id": qid, "typ": "faktor", "buch": buch})
        else:
            o = [ok] + falsch; random.Random("k67" + qid).shuffle(o)   # im Seitencode steht die richtige Antwort nicht immer vorne
            fr.append({"id": qid, "f": frage, "o": o, "h": fnv(SALZ + qid + "|" + ok), "buch": buch})
    POOL.append({"thema": g["thema"], "n": g["n"], "fragen": fr})

LOGO = re.search(r'LOGO = "(data:image/png;base64,[^"]+)"', open(os.path.join(ROOT, I.ORDNER, "aufgaben.html"), encoding="utf-8").read()).group(1)
e = lambda x: html.escape(str(x), quote=True)

SEITE = """<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mitarbeits-Check · K6–7 Wahlrecht und Parteien</title>
<link rel="stylesheet" href="../../schriften/schriften.css">
<style>
:root { --ink: #1F2A1C; --olive: #3B4A2F; --muted: #5E6652; --line: #D3DCC2; --bg: #EEF3E4; --rust: #8C3B2E; --teal: #2E7D8C; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 18px/1.5 "Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif; }
.top { background: var(--olive); color: #fff; padding: 12px 16px; display: flex; gap: 12px; align-items: center; }
.top a { color: #fff; font-weight: 700; text-decoration: none; }
main { max-width: 720px; margin: 0 auto; padding: 14px 12px 60px; }
h1 { font-family: "Source Serif 4", Georgia, serif; font-size: 28px; line-height: 1.15; margin: 8px 0 4px; color: var(--olive); }
.eyebrow { font-size: 13px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: var(--rust); }
.card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 14px 16px; margin: 12px 0; }
.regeln { margin: 6px 0 0; padding-left: 1.2em; } .regeln li { margin: 4px 0; }
label.feld { display: grid; gap: 4px; font-weight: 700; margin: 10px 0; }
input[type=text], select { font: inherit; padding: 10px 12px; border: 2px solid var(--line); border-radius: 10px; min-height: 48px; width: 100%; background: #fff; }
.btn { font: inherit; font-weight: 700; font-size: 18px; min-height: 52px; width: 100%; border-radius: 12px; border: 0; background: var(--olive); color: #fff; cursor: pointer; margin-top: 8px; }
.btn[disabled] { opacity: .45; cursor: default; }
.btn.rot { background: var(--rust); }
.leiste { position: sticky; top: 0; z-index: 5; background: var(--bg); padding: 8px 0; display: flex; gap: 10px; align-items: center; justify-content: space-between; font-weight: 700; }
.leiste .uhr { font-variant-numeric: tabular-nums; color: var(--rust); }
.frage { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; margin: 12px 0; }
.frage .nr { display: inline-grid; place-items: center; width: 32px; height: 32px; border-radius: 50%; background: var(--olive); color: #fff; font-weight: 800; margin-right: 8px; }
.frage .q { font-weight: 700; margin: 4px 0 10px; }
.opt { display: flex; gap: 10px; align-items: flex-start; border: 2px solid var(--line); border-radius: 12px; padding: 10px 12px; margin: 8px 0; cursor: pointer; min-height: 48px; }
.opt input { width: 22px; height: 22px; margin-top: 3px; flex: none; accent-color: var(--olive); }
.opt.an { border-color: var(--olive); background: #F1F5E9; }
.gesperrt .opt { cursor: default; opacity: .8; }
.hinweis { font-size: 16px; color: var(--muted); }
.warn { background: #FFF4D6; border-left: 5px solid #B07A00; padding: 10px 12px; border-radius: 10px; font-weight: 600; }
.ok { background: #EEF4E4; border-left: 5px solid #3F6B14; padding: 10px 12px; border-radius: 10px; font-weight: 600; }
#pdfstatus { min-height: 1.4em; font-weight: 600; }
[hidden] { display: none !important; }
</style></head><body>
<main>
<div class="eyebrow">K6–7 Wahlrecht und Parteien · Mitarbeits-Check</div>
<h1>Was ist hängen geblieben?</h1>
<p>10 Fragen zur ganzen Einheit, ca. 8 Minuten. Das ist <b>kein Test</b>, sondern ein kurzer Check – er zählt zur <b>Mitarbeit</b>.</p>

<section id="start" class="card">
<ul class="regeln"><li>Ohne Buch, ohne Theorie-Seite, ohne Nachbar.</li><li>Keine Tipps, kein »Prüfen« – du siehst dein Ergebnis im PDF.</li>
<li><b>Nur ein Versuch zählt.</b> Nach »Abgeben« kannst du nichts mehr ändern.</li><li>Starten kannst du erst, wenn Prof. HOLZER den <b>Startcode</b> zeigt.</li><li>Am Ende: PDF erstellen und in LMS hochladen.</li></ul>
<label class="feld">Vor- und Nachname<input type="text" id="name" autocomplete="name" placeholder="z. B. Max Muster"></label>
<label class="feld">Klasse<select id="klasse"><option value="">bitte wählen …</option>__KLASSEN__</select></label>
<label class="feld">Startcode (sagt dir Prof. HOLZER)<input type="text" id="code" inputmode="numeric" autocomplete="off" maxlength="6" placeholder="4 Ziffern"></label>
<p class="hinweis" id="codehinweis"></p>
<button type="button" class="btn" id="los" disabled>Check starten</button>
</section>

<section id="check" hidden>
<div class="leiste"><span id="stand">0 von 10 beantwortet</span><span class="uhr" id="uhr">0:00</span></div>
<div id="fragen"></div>
<div class="card"><p class="hinweis" id="offen"></p><button type="button" class="btn rot" id="abgeben">Abgeben</button></div>
</section>

<section id="fertig" class="card" hidden>
<p class="ok" id="fertigtext"></p>
<p>Jetzt das PDF erstellen und in <b>LMS</b> hochladen. Dein Ergebnis steht im PDF.</p>
<button type="button" class="btn" id="pdfbtn">PDF erstellen</button>
<p id="pdfstatus" role="status" aria-live="polite"></p>
</section>
<p class="hinweis">Deine Antworten bleiben nur auf diesem Gerät. Prof. HOLZER bespricht die Fragen danach mit der Klasse.</p>
</main>
<script src="../../gemeinsam/pdf-programm-v1.js"></script>
<script>if (!window.jspdf) document.write('<script src="../../gemeinsam/pdf-programm-v1.js?nochmal=1"><\\/script>');</script>
<script>
const KEY = "__KEY__";
const POOL = __POOL__;
const SALZ = "__SALZ__", LOGO = "__LOGO__", START = __START__;
const FONT_R = window.__PDF_FONT_R || "", FONT_B = window.__PDF_FONT_B || "";
const $ = s => document.querySelector(s);
function fnv(t) { let h = 2166136261; for (let i = 0; i < t.length; i++) { h ^= t.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h >>> 0; }
function mischen(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function lies() { try { return JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) { return null; } }
let S = lies() || { name: "", klasse: "", a: {}, fr: null, start: 0, ende: 0, versuche: 0 };
function sichern() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
function fmtZeit(ms) { const s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); }
function uhrzeit(t) { const d = new Date(t); return d.toLocaleDateString("de-AT") + " " + d.toLocaleTimeString("de-AT", { hour: "2-digit", minute: "2-digit" }); }

function faktorFrage(f) { return null; }   /* keine Zahlenfrage in dieser Einheit */
function ziehen() {
  const fr = [];
  POOL.forEach(g => mischen(g.fragen).slice(0, g.n).forEach(f => { const q = f.typ === "faktor" ? faktorFrage(f) : { id: f.id, f: f.f, o: f.o.slice(), h: f.h, buch: f.buch }; q.o = mischen(q.o); fr.push(q); }));
  return mischen(fr);
}
function beantwortet() { return S.fr ? S.fr.filter(q => S.a[q.id] != null).length : 0; }
function zeigeStand() {
  const n = beantwortet(); $("#stand").textContent = n + " von " + S.fr.length + " beantwortet";
  const off = S.fr.length - n; $("#offen").textContent = off ? "Noch " + off + (off === 1 ? " Frage" : " Fragen") + " offen. Offene Fragen zählen 0 Punkte." : "Alle Fragen beantwortet. Kontrolliere kurz – dann abgeben.";
}
function baueFragen() {
  const box = $("#fragen"); box.textContent = "";
  S.fr.forEach((q, i) => {
    const d = document.createElement("div"); d.className = "frage" + (S.ende ? " gesperrt" : "");
    const k = document.createElement("p"); k.className = "q"; const nr = document.createElement("span"); nr.className = "nr"; nr.textContent = i + 1; k.append(nr, document.createTextNode(q.f)); d.append(k);
    q.o.forEach((o, j) => {
      const l = document.createElement("label"); l.className = "opt" + (S.a[q.id] === j ? " an" : "");
      const r = document.createElement("input"); r.type = "radio"; r.name = "q" + i; r.checked = S.a[q.id] === j; r.disabled = !!S.ende;
      r.addEventListener("change", () => { if (S.ende) return; S.a[q.id] = j; sichern(); d.querySelectorAll(".opt").forEach((x, m) => x.classList.toggle("an", m === j)); zeigeStand(); });
      l.append(r, document.createTextNode(o)); d.append(l);
    });
    box.append(d);
  });
  zeigeStand();
}
function ansicht() {
  $("#start").hidden = !!S.fr; $("#check").hidden = !S.fr || !!S.ende; $("#fertig").hidden = !S.ende;
  if (S.fr && !S.ende) baueFragen();
  if (S.ende) $("#fertigtext").textContent = "Abgegeben am " + uhrzeit(S.ende) + " von " + S.name + " (" + S.klasse + ").";
}
$("#name").value = S.name; $("#klasse").value = S.klasse;
function codeOk() { return fnv(SALZ + "start|" + $("#code").value.trim()) === START; }
function startOk() { $("#los").disabled = !($("#name").value.trim().length > 2 && $("#klasse").value && $("#code").value.trim().length >= 4); }
$("#name").addEventListener("input", startOk); $("#klasse").addEventListener("change", startOk); $("#code").addEventListener("input", () => { $("#codehinweis").textContent = ""; startOk(); }); startOk();
$("#los").addEventListener("click", () => {
  if (!codeOk()) { $("#codehinweis").textContent = "Der Code stimmt nicht. Den Startcode zeigt Prof. HOLZER, wenn der Check beginnt."; return; }
  S.name = $("#name").value.trim(); S.klasse = $("#klasse").value; S.fr = ziehen(); S.a = {}; S.start = Date.now(); S.ende = 0;
  S.versuche = (S.versuche || 0) + 1; sichern(); ansicht(); window.scrollTo(0, 0);
});
let zweiter = false;
$("#abgeben").addEventListener("click", () => {
  const off = S.fr.length - beantwortet();
  if (off && !zweiter) { zweiter = true; $("#abgeben").textContent = "Wirklich abgeben? (" + off + " offen)"; return; }
  S.ende = Date.now(); sichern(); ansicht(); window.scrollTo(0, 0);
});
setInterval(() => { if (S.fr && !S.ende) $("#uhr").textContent = fmtZeit(Date.now() - S.start); }, 500);

function auswertung() {
  let p = 0; const zeilen = S.fr.map((q, i) => { const j = S.a[q.id]; const t = j == null ? null : q.o[j]; const ok = t != null && fnv(SALZ + q.id + "|" + t) === q.h; if (ok) p++; return { nr: i + 1, f: q.f, t, ok, buch: q.buch }; });
  const pr = 100 * p / S.fr.length; const note = pr >= 88 ? 1 : pr >= 75 ? 2 : pr >= 62 ? 3 : pr >= 50 ? 4 : 5;
  return { p, n: S.fr.length, pr, note, zeilen };
}
function haken(d, x, y, ok) {
  d.setLineWidth(0.7);
  if (ok) { d.setDrawColor(46, 125, 50); d.line(x, y - 1.6, x + 1.4, y); d.line(x + 1.4, y, x + 4, y - 3.8); }
  else { d.setDrawColor(176, 58, 46); d.line(x, y - 3.6, x + 3.4, y); d.line(x + 3.4, y - 3.6, x, y); }
}
$("#pdfbtn").addEventListener("click", () => {
  const st = $("#pdfstatus");
  if (!window.jspdf) { st.textContent = "Das PDF-Programm wurde nicht geladen. Lade die Seite neu."; return; }
  const A = auswertung(); const { jsPDF } = window.jspdf; const d = new jsPDF({ unit: "mm", format: "a4" });
  if (FONT_R) { d.addFileToVFS("C-R.ttf", FONT_R); d.addFont("C-R.ttf", "C", "normal"); d.addFileToVFS("C-B.ttf", FONT_B); d.addFont("C-B.ttf", "C", "bold"); }
  const F = FONT_R ? "C" : "helvetica", M = 16, W = 210 - 2 * M; let y = 16;
  try { d.addImage(LOGO, "PNG", M, y - 2, 11, 12.6); } catch (e) {}
  d.setFont(F, "bold"); d.setFontSize(15); d.text("Mitarbeits-Check · K6–7 Wahlrecht und Parteien", M + 15, y + 3);
  d.setFont(F, "normal"); d.setFontSize(10.5); d.text("PBGW 2AK · Name: " + S.name + " · Klasse: " + S.klasse, M + 15, y + 9);
  d.text("Start " + uhrzeit(S.start) + " · Abgabe " + uhrzeit(S.ende) + " · Dauer " + fmtZeit(S.ende - S.start) + " min", M + 15, y + 14);
  y += 22;
  d.setFillColor(238, 244, 228); d.setDrawColor(63, 107, 20); d.setLineWidth(0.4); d.roundedRect(M, y, W, 15, 2, 2, "FD");
  d.setFont(F, "bold"); d.setFontSize(12.5); d.setTextColor(31, 42, 28);
  d.text("Für LMS: " + A.p + " von " + A.n + " Punkten · Notenvorschlag " + A.note + " (Mitarbeit)", M + 4, y + 6.5);
  d.setFont(F, "normal"); d.setFontSize(9.5);
  d.text(A.pr.toFixed(1).replace(".", ",") + " % · Schlüssel: ab 88 % 1, ab 75 % 2, ab 62 % 3, ab 50 % 4 · automatisch ausgewertet, kein Test", M + 4, y + 11.8);
  y += 20;
  if ((S.versuche || 1) > 1) { d.setTextColor(176, 58, 46); d.setFont(F, "bold"); d.setFontSize(10); d.text("Achtung: Der Check wurde auf diesem Gerät " + S.versuche + "-mal gestartet.", M, y); d.setTextColor(31, 42, 28); y += 6; }
  d.setFont(F, "bold"); d.setFontSize(11); d.text("Deine Antworten", M, y); y += 2;
  A.zeilen.forEach(z => {
    d.setFont(F, "bold"); d.setFontSize(10.5);
    const fl = d.splitTextToSize(z.nr + ". " + z.f, W - 10); const al = d.splitTextToSize("Deine Antwort: " + (z.t == null ? "– (nicht beantwortet)" : z.t), W - 10);
    const h = fl.length * 4.6 + al.length * 4.4 + 5;
    if (y + h > 282) { d.addPage(); y = 18; }
    y += 5; haken(d, M, y, z.ok); d.text(fl, M + 8, y); y += fl.length * 4.6;
    d.setFont(F, "normal"); d.setTextColor(z.ok ? 46 : 176, z.ok ? 125 : 58, z.ok ? 50 : 46); d.text(al, M + 8, y); d.setTextColor(31, 42, 28); y += al.length * 4.4;
    d.setFontSize(8.5); d.setTextColor(94, 102, 82); d.text((z.ok ? "richtig" : "falsch") + " · Nachlesen: Buch " + z.buch, M + 8, y); d.setTextColor(31, 42, 28); y += 1;
  });
  d.setFontSize(8.5); d.setTextColor(94, 102, 82);
  d.text("Die richtigen Antworten bespricht Prof. HOLZER mit der Klasse. Geht LMS nicht, schick das PDF per E-Mail.", M, 290);
  const nn = (S.name.split(/\\s+/).pop() || "Kadett").replace(/[^A-Za-zÄÖÜäöüß-]/g, "");
  const filename = "K6-7-Check-" + nn + ".pdf";
  const url = URL.createObjectURL(d.output("blob")); const a = document.createElement("a"); a.href = url; a.download = filename; document.body.append(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 30000);
  st.textContent = "PDF wurde erstellt: " + filename + " – schau in deinen Downloads nach, ob sie da ist, und lade sie dann in LMS hoch.";
});
ansicht();
</script>
</body></html>
"""

seite = (SEITE.replace("__KEY__", I.CHECK_KEY).replace("__POOL__", json.dumps(POOL, ensure_ascii=False).replace("</", "<\\/"))
         .replace("__SALZ__", SALZ).replace("__LOGO__", LOGO).replace("__START__", str(fnv(SALZ + "start|" + I.CHECK_CODE)))
         .replace("__KLASSEN__", "".join(f"<option>{e(k)}</option>" for k in I.KLASSEN)))
ZIEL = os.path.join(ROOT, I.ORDNER, "check.html")
open(ZIEL, "w", encoding="utf-8").write(seite)
print("ok", os.path.relpath(ZIEL, ROOT), len(seite) // 1024, "KB")
