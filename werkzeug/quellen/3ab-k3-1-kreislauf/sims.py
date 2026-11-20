"""Simulationen zum Selbst-Regeln für 3AB K3.1/K3.6 Körper unter Belastung (Standard 14.11.2026: Kadetten regeln selbst, sehen sofort die Wirkung).
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in JS (window.SIMINIT[name](box)).
Theorie-Seite: Blöcke ("sim", name). Arbeitsblatt: Feld "sim" einer Aufgabe → aufklappbares »Ausprobieren«.
Fachliche Grundlagen (Stand 20.11.2026):
- hmv: Herzminutenvolumen = Schlagvolumen · Herzfrequenz (Buch S. 81). Regler: Puls 40–200 /min, Schlagvolumen 50–150 ml. Tag: · 1440 min.
  Vergleich: Badewanne ≈ 150 l (Richtwert, gerundet). Hinweis bei Puls über 180: in Ruhe nie, nur bei maximaler Belastung.
- blutgruppe: AB0-Regel für rote Blutkonserven (Erythrozytenkonzentrat): Verklumpung, wenn der Empfänger Antikörper gegen ein Antigen der Spenderzellen hat.
  A: Anti-B · B: Anti-A · AB: keine · 0: Anti-A und Anti-B (Buch S. 84). Rhesus wird bewusst weggelassen (Hinweis in der Simulation).
- hebel: vereinfachtes Hebelmodell der Lendenwirbelsäule: Kraft der Rückenstrecker F = Last · Lastarm / Kraftarm, Kraftarm 5 cm (Lehrbuch-Richtwert für den Abstand
  der Rückenstrecker von der Bandscheibe), g ≈ 10 N/kg. Oberkörpergewicht und Bauchdruck sind NICHT eingerechnet – auf der Seite als »vereinfachtes Modell« gekennzeichnet."""

TITEL = {"hmv": "Herzminutenvolumen-Rechner", "blutgruppe": "Welche Konserve passt?", "hebel": "Hebel am Rücken"}
ZEILE = {"hmv": "Regle Puls und Schlagvolumen – wie viel Blut pro Minute und pro Tag?",
         "blutgruppe": "Wähle Spender und Empfänger – verklumpt das Blut?",
         "hebel": "Schieb die Last weiter weg – wie stark müssen die Rückenmuskeln ziehen?"}

HTML = {
 "hmv": """<div class="sim" data-sim="hmv">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Herzminutenvolumen-Rechner</b></div>
 <svg viewBox="0 0 320 120" class="hmvbild" aria-hidden="true"></svg>
 <div class="simb" role="group" aria-label="Situation"><button type="button" class="btn small" data-a="ruhe" aria-pressed="true">in Ruhe</button><button type="button" class="btn secondary small" data-a="marsch" aria-pressed="false">Marsch</button><button type="button" class="btn secondary small" data-a="sprint" aria-pressed="false">Sprint</button></div>
 <label>Puls: <b data-o="hf">70 pro Minute</b><input type="range" min="40" max="200" step="5" value="70" data-i="hf" aria-label="Puls"></label>
 <label>Schlagvolumen: <b data-o="sv">70 ml</b><input type="range" min="50" max="150" step="5" value="70" data-i="sv" aria-label="Schlagvolumen"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt" data-o="info"></p>
</div>""",
 "blutgruppe": """<div class="sim" data-sim="blutgruppe">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Welche Konserve passt?</b></div>
 <p class="simt"><b>Blutkonserve (Spender):</b></p>
 <div class="simb" role="group" aria-label="Spender" data-g="sp"><button type="button" class="btn small" data-bg="A">A</button><button type="button" class="btn secondary small" data-bg="B">B</button><button type="button" class="btn secondary small" data-bg="AB">AB</button><button type="button" class="btn secondary small" data-bg="0">0</button></div>
 <p class="simt"><b>Patient (Empfänger):</b></p>
 <div class="simb" role="group" aria-label="Empfänger" data-g="em"><button type="button" class="btn small" data-bg="A">A</button><button type="button" class="btn secondary small" data-bg="B">B</button><button type="button" class="btn secondary small" data-bg="AB">AB</button><button type="button" class="btn secondary small" data-bg="0">0</button></div>
 <svg viewBox="0 0 320 130" class="bgbild" aria-hidden="true"></svg>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Nur rote Blutkonserven, ohne Rhesusfaktor. In der Klinik gibt man möglichst die gleiche Blutgruppe.</p>
</div>""",
 "hebel": """<div class="sim" data-sim="hebel">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Hebel am Rücken</b></div>
 <svg viewBox="0 0 320 200" class="hbbild" aria-hidden="true"></svg>
 <label>Last (Kiste, Rucksack): <b data-o="m">10 kg</b><input type="range" min="2" max="30" step="1" value="10" data-i="m" aria-label="Masse der Last"></label>
 <label>Abstand der Last von der Wirbelsäule: <b data-o="r">20 cm</b><input type="range" min="10" max="60" step="5" value="20" data-i="r" aria-label="Abstand"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Vereinfachtes Modell: Rückenmuskeln greifen 5 cm hinter der Wirbelsäule an, 1 kg ≈ 10 N. Das Gewicht des Oberkörpers ist nicht eingerechnet – in Wirklichkeit kommt noch mehr dazu.</p>
</div>""",
}

CSS = """
.sim { border: 2px solid #2E7D8C; border-radius: 12px; background: #fff; padding: 12px 14px; display: grid; gap: 8px; }
.simh { display: flex; gap: 8px; align-items: center; font-size: 18px; flex-wrap: wrap; }
.sim canvas, .sim svg { width: 100%; height: auto; border-radius: 10px; background: #F2F3EE; display: block; }
.sim label { display: grid; gap: 4px; font-size: 17px; } .sim input[type=range] { width: 100%; min-height: 44px; }
.simb { display: flex; gap: 8px; flex-wrap: wrap; } .simb .btn { min-height: 44px; min-width: 52px; }
.sim .btn.small { width: auto; font-size: 16px; padding: 8px 14px; }
.sim .btn.secondary { background: #fff; color: #3B4A2F; border: 2px solid #3B4A2F; }
.simb .btn[aria-pressed="true"] { background: #3B4A2F; color: #fff; }
.simt { margin: 0; font-size: 16px; color: #5E6652; }
.sim .ergebnis { background: #3B4A2F; color: #fff; border-radius: 10px; padding: 10px 12px; font-size: 18px; line-height: 1.35; }
.sim .ergebnis b { color: #FFE7A3; }
details.simd { margin: 10px 0; } details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; min-height: 44px; display: flex; align-items: center; }
"""

JS = """<script>
(function () {
  var SIMINIT = window.SIMINIT = window.SIMINIT || {};
  function q(box, o) { return box.querySelector('[data-o="' + o + '"]'); }
  function f(x, d) { return (typeof d === "number" ? x.toFixed(d) : String(x)).replace(".", ","); }
  function tsd(x) { return String(Math.round(x)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\\u202f"); }
  var RUHIG = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function druecke(gruppe, knopf) { gruppe.querySelectorAll("[aria-pressed]").forEach(function (b) { var an = b === knopf; b.setAttribute("aria-pressed", String(an)); b.classList.toggle("secondary", !an); }); }

  SIMINIT.hmv = function (box) {
    var rh = box.querySelector('[data-i="hf"]'), rs = box.querySelector('[data-i="sv"]'), svg = box.querySelector("svg"), t0 = null;
    var LAGE = { ruhe: [70, 70], marsch: [110, 100], sprint: [180, 120] };
    function zeig() {
      var hf = +rh.value, sv = +rs.value, ml = hf * sv, l = ml / 1000, tag = l * 1440;
      q(box, "hf").textContent = hf + " pro Minute"; q(box, "sv").textContent = sv + " ml";
      q(box, "erg").innerHTML = "HMV = " + sv + " ml · " + hf + " = " + tsd(ml) + " ml = <b>" + f(l, 1) + " l pro Minute</b><br>an einem Tag: <b>" + tsd(tag) + " l</b> ≈ " + f(tag / 150, 0) + " Badewannen";
      q(box, "info").textContent = hf >= 180 ? "So hoch steigt der Puls nur bei maximaler Belastung – nicht lange durchzuhalten."
        : hf <= 50 ? "So niedrig ist der Ruhepuls oft bei gut trainierten Ausdauersportlern – ihr Herz schafft pro Schlag mehr."
        : l > 12 ? "Bei Belastung fließt viel mehr Blut, vor allem in die Muskeln." : "In Ruhe pumpt das Herz rund 5 Liter pro Minute.";
    }
    function bild(ms) {
      if (t0 === null) t0 = ms;
      var hf = +rh.value, sv = +rs.value, p = RUHIG ? 0.5 : ((ms - t0) / (60000 / hf)) % 1, sch = 1 - 0.18 * Math.max(0, Math.sin(p * Math.PI * 2)) * sv / 100;
      var rx = 34 * sch, ry = 40 * sch, voll = Math.min(1, (hf * sv) / 18000);
      svg.innerHTML = "<ellipse cx='70' cy='60' rx='" + rx.toFixed(1) + "' ry='" + ry.toFixed(1) + "' fill='#C0392B'/><text x='70' y='65' font-size='14' fill='#fff' text-anchor='middle' font-weight='700'>Herz</text>"
        + "<rect x='150' y='18' width='150' height='84' rx='8' fill='#fff' stroke='#5E6652' stroke-width='2'/>"
        + "<rect x='152' y='" + (100 - 82 * voll).toFixed(1) + "' width='146' height='" + (82 * voll).toFixed(1) + "' rx='6' fill='#E8A5A0'/>"
        + "<text x='225' y='112' font-size='12' fill='#5E6652' text-anchor='middle'>Blut pro Minute (Skala bis 18 l)</text>"
        + "<path d='M108 60 H144' stroke='#C0392B' stroke-width='6' marker-end='url(#pf)'/><defs><marker id='pf' viewBox='0 0 10 10' refX='6' refY='5' markerWidth='4' markerHeight='4' orient='auto'><path d='M0 0 L10 5 L0 10z' fill='#C0392B'/></marker></defs>";
      if (!RUHIG) requestAnimationFrame(bild);
    }
    [rh, rs].forEach(function (r) { r.addEventListener("input", zeig); });
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return; var w = LAGE[b.dataset.a]; rh.value = w[0]; rs.value = w[1]; druecke(b.parentNode, b); zeig(); });
    zeig(); requestAnimationFrame(bild); if (RUHIG) bild(0);
  };

  SIMINIT.blutgruppe = function (box) {
    var AG = { A: ["A"], B: ["B"], AB: ["A", "B"], "0": [] }, AK = { A: ["B"], B: ["A"], AB: [], "0": ["A", "B"] }, sp = "A", em = "A", svg = box.querySelector("svg");
    function zelle(x, y, ag, klumpt) {
      var s = "<circle cx='" + x + "' cy='" + y + "' r='16' fill='#C0392B'/><circle cx='" + x + "' cy='" + y + "' r='7' fill='#A93226'/>";
      ag.forEach(function (a, i) { var w = (i === 0 ? -1 : 1) * 0.9 + (ag.length === 1 ? 0.9 : 0); s += "<rect x='" + (x + 18 * Math.cos(w) - 4) + "' y='" + (y - 18 * Math.sin(w) - 4) + "' width='8' height='8' fill='" + (a === "A" ? "#2E7D8C" : "#D99A00") + "'/>"; });
      return s;
    }
    function zeig() {
      var gegen = AK[em].filter(function (a) { return AG[sp].indexOf(a) >= 0; }), klumpt = gegen.length > 0, s = "";
      var pos = klumpt ? [[150, 50], [170, 62], [158, 76], [178, 44], [140, 70], [186, 74]] : [[110, 40], [190, 40], [250, 70], [150, 90], [210, 100], [80, 85]];
      pos.forEach(function (p) { s += zelle(p[0], p[1], AG[sp], klumpt); });
      AK[em].forEach(function (a, i) { for (var k = 0; k < 3; k++) { var x = 40 + k * 110 + i * 40, y = 118; s += "<path d='M" + x + " " + y + " l6 -8 m-6 8 l-6 -8 m6 8 v6' stroke='" + (a === "A" ? "#2E7D8C" : "#D99A00") + "' stroke-width='3' fill='none'/>"; } });
      svg.innerHTML = s + (klumpt ? "<text x='160' y='22' font-size='15' text-anchor='middle' fill='#8C3B2E' font-weight='700'>verklumpt!</text>" : "");
      q(box, "erg").innerHTML = "Konserve <b>" + sp + "</b> zu Patient <b>" + em + "</b>: " + (klumpt
        ? "<b>verklumpt</b> – der Patient hat Antikörper gegen " + gegen.join(" und ") + " im Plasma."
        : "<b>passt</b> – der Patient hat keine Antikörper gegen die Merkmale der Konserve" + (AG[sp].length ? "" : " (0 trägt keine Merkmale A oder B)") + ".");
    }
    box.addEventListener("click", function (ev) {
      var b = ev.target.closest("[data-bg]"); if (!b) return; var g = b.parentNode;
      g.querySelectorAll("[data-bg]").forEach(function (x) { x.classList.toggle("secondary", x !== b); x.setAttribute("aria-pressed", String(x === b)); });
      if (g.dataset.g === "sp") sp = b.dataset.bg; else em = b.dataset.bg; zeig();
    });
    box.querySelectorAll("[data-bg]").forEach(function (x) { x.setAttribute("aria-pressed", String(!x.classList.contains("secondary"))); });
    zeig();
  };

  SIMINIT.hebel = function (box) {
    var rm = box.querySelector('[data-i="m"]'), rr = box.querySelector('[data-i="r"]'), svg = box.querySelector("svg");
    function zeig() {
      var m = +rm.value, r = +rr.value, last = m * 10, kraft = last * r / 5;
      q(box, "m").textContent = m + " kg"; q(box, "r").textContent = r + " cm";
      var x = 110 + r * 3.2, pf = Math.min(150, 12 + kraft / 25);
      svg.innerHTML = "<rect x='96' y='40' width='14' height='140' rx='6' fill='#E8DCC0' stroke='#8A6A44' stroke-width='2'/>"
        + "<text x='103' y='196' font-size='12' text-anchor='middle' fill='#5E6652'>Wirbelsäule</text>"
        + "<line x1='103' y1='70' x2='" + x + "' y2='70' stroke='#3B4A2F' stroke-width='5'/>"
        + "<rect x='" + (x - 18) + "' y='72' width='36' height='" + (18 + m) + "' rx='4' fill='#7A6A44'/><text x='" + x + "' y='" + (88 + m / 2) + "' font-size='12' fill='#fff' text-anchor='middle'>" + m + " kg</text>"
        + "<line x1='" + x + "' y1='" + (92 + m) + "' x2='" + x + "' y2='" + (120 + m) + "' stroke='#5E6652' stroke-width='3'/>"
        + "<line x1='80' y1='70' x2='80' y2='" + (70 + pf) + "' stroke='#A33A2B' stroke-width='" + Math.min(14, 3 + kraft / 300) + "'/>"
        + "<text x='60' y='60' font-size='12' fill='#A33A2B' text-anchor='middle'>Rücken-</text><text x='60' y='48' font-size='12' fill='#A33A2B' text-anchor='middle'>muskeln</text>"
        + "<text x='" + ((103 + x) / 2) + "' y='62' font-size='12' text-anchor='middle' fill='#3B4A2F'>" + r + " cm</text>";
      q(box, "erg").innerHTML = "Last " + tsd(last) + " N · Lastarm " + r + " cm · Kraftarm 5 cm<br>Rückenmuskeln ziehen mit rund <b>" + tsd(kraft) + " N</b> – das ist <b>" + f(kraft / last, 0) + "-mal</b> die Last.";
    }
    [rm, rr].forEach(function (x) { x.addEventListener("input", zeig); }); zeig();
  };

  function start() { document.querySelectorAll(".sim[data-sim]").forEach(function (b) { if (!b.dataset.go && SIMINIT[b.dataset.sim] && b.offsetParent !== null) { b.dataset.go = "1"; SIMINIT[b.dataset.sim](b); } }); }
  window.simStart = start;
  document.addEventListener("toggle", function () { start(); }, true);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
</script>"""
