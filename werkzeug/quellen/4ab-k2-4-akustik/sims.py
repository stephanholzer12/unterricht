"""Simulationen zum Selbst-Regeln für 4AB K2.4/K3.2 Akustik (Stephan 14.11.2026: Kadetten regeln selbst, sehen sofort die Wirkung).
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in JS (window.SIMINIT[name](box)).
Theorie-Seite: Blöcke ("sim", name). Arbeitsblatt: Feld "sim" einer Aufgabe → aufklappbares »Ausprobieren«.
Fachliche Grundlagen (Stand 15.11.2026):
- druck: Längswelle, Auslenkung s = A·sin(ωt − kx), Druck p ~ −ds/dx ~ cos(ωt − kx): Druckmaximum dort, wo die Teilchen zusammenrücken. Vakuum: kein Träger.
- echo: s = v·t; Echo/Echolot: Entfernung = v·t/2. v Luft 340 m/s (ca. 15 °C), Wasser 1480 m/s (Buch S. 61, 66).
- db: ΔL = 10·lg(I2/I1) → Intensität × 10^(ΔL/10), Schalldruck × 10^(ΔL/20). n gleiche Quellen: +10·lg(n) dB (2 → +3, 10 → +10; Buch S. 64 Kasten).
  Beispielwerte nach Buch S. 110 (Tabelle Alltagsgeräusche); VOLV: ab 85 dB(A) Gehörschutz tragen.
- richtung: Umweg zum abgewandten Ohr höchstens ca. 0,2 m (Kopfbreite + Umweg, vereinfacht 0,2 m · sin θ); Δt = s / 340 m/s (max. ≈ 0,59 ms).
- bogen: vereinfachtes Modell der Kuppel: Ausschlag ~ (Drehgeschwindigkeit Kopf − Drehgeschwindigkeit Lymphe); Lymphe holt mit
  Zeitkonstante ca. 2,5 s auf (in Wirklichkeit einige Sekunden). Gleichmäßige Drehung → keine Meldung; Stopp → Gegen-Drehgefühl."""

TITEL = {"druck": "Druckwelle selbst einstellen", "echo": "Echo- und Gewitter-Rechner", "db": "Dezibel-Rechner",
         "richtung": "Zeitunterschied zwischen den Ohren", "bogen": "Bogengang: Drehung beginnt – Stopp"}
ZEILE = {"druck": "Regle Frequenz und Amplitude – und saug die Luft ab.",
         "echo": "Stell die Zeit ein – wie weit ist es? Mit und ohne Echo.",
         "db": "Schieb zwei Pegel – wievielmal mehr Intensität und Druck?",
         "richtung": "Dreh die Schallquelle um deinen Kopf – wie viel später kommt der Schall am anderen Ohr an?",
         "bogen": "Dreh den Kopf und stopp – was meldet der Bogengang?"}

HTML = {
 "druck": """<div class="sim" data-sim="druck">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Druckwelle selbst einstellen</b></div>
 <canvas width="640" height="300" aria-label="Animation: Luftteilchen einer Schallwelle mit Druckkurve"></canvas>
 <label>Frequenz (Tonhöhe): <b data-o="f">langsam</b><input type="range" min="1" max="5" step="1" value="2" data-i="f" aria-label="Frequenz"></label>
 <label>Amplitude (Stärke): <b data-o="a">mittel</b><input type="range" min="1" max="3" step="1" value="2" data-i="a" aria-label="Amplitude"></label>
 <div class="simb"><button type="button" class="btn small" data-a="luft">Luft absaugen (Vakuum)</button><button type="button" class="btn secondary small" data-a="pause">Anhalten</button></div>
 <p class="simt">Schau auf das rote Teilchen: Es bleibt fast an seinem Platz. Die orange Kurve zeigt den Druck – oben dichte, unten dünne Luft.</p>
</div>""",
 "echo": """<div class="sim" data-sim="echo">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Echo- und Gewitter-Rechner</b></div>
 <div class="simb" role="group" aria-label="Situation"><button type="button" class="btn small" data-a="gewitter" aria-pressed="true">Gewitter</button><button type="button" class="btn secondary small" data-a="echo" aria-pressed="false">Echo an der Wand</button><button type="button" class="btn secondary small" data-a="lot" aria-pressed="false">Echolot (Wasser)</button></div>
 <svg viewBox="0 0 320 90" class="echobild" aria-hidden="true"></svg>
 <label>Gemessene Zeit: <b data-o="t">3,0 s</b><input type="range" min="1" max="60" step="1" value="15" data-i="t" aria-label="Zeit"></label>
 <p class="simt" data-o="rech"></p>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt" data-o="info"></p>
</div>""",
 "db": """<div class="sim" data-sim="db">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Dezibel-Rechner</b></div>
 <svg viewBox="0 0 320 210" class="dbleiter" aria-hidden="true"></svg>
 <label><span><span class="mk a">▶</span> Pegel A: <b data-o="a">60 dB</b> <span class="simt" data-o="anam">Gespräch</span></span><input type="range" min="0" max="160" step="5" value="60" data-i="a" aria-label="Pegel A"></label>
 <label><span><span class="mk b">▶</span> Pegel B: <b data-o="b">100 dB</b> <span class="simt" data-o="bnam">Kopfhörer laut</span></span><input type="range" min="0" max="160" step="5" value="100" data-i="b" aria-label="Pegel B"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt"><b>Gleiche Quellen zusammen:</b> Wie viele gleich laute Maschinen laufen?</p>
 <div class="simb" role="group" aria-label="Anzahl gleicher Quellen"><button type="button" class="btn secondary small" data-n="1">1</button><button type="button" class="btn secondary small" data-n="2">2</button><button type="button" class="btn secondary small" data-n="4">4</button><button type="button" class="btn secondary small" data-n="10">10</button></div>
 <p class="simt" data-o="quell">Tipp: Wähle die Anzahl der Maschinen mit je 80 dB.</p>
 <p class="simt">Ohne Formel: Zähle Zehnerstufen. +10 dB = Intensität ×10. Werte nach Buch S. 110, gerundet.</p>
</div>""",
 "richtung": """<div class="sim" data-sim="richtung">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Zeitunterschied zwischen den Ohren</b></div>
 <svg viewBox="0 0 320 250" class="rbild" aria-hidden="true"></svg>
 <label>Richtung der Schallquelle: <b data-o="w">90° (genau links)</b><input type="range" min="0" max="180" step="5" value="90" data-i="w" aria-label="Richtung in Grad"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Vereinfacht: Der Umweg zum abgewandten Ohr ist höchstens etwa 0,2 m; Schall in Luft 340 m/s.</p>
</div>""",
 "bogen": """<div class="sim" data-sim="bogen">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Bogengang: Drehung beginnt – Stopp</b></div>
 <canvas width="480" height="360" aria-label="Animation: Bogengang mit Lymphe und Kuppel"></canvas>
 <div class="simb"><button type="button" class="btn small" data-a="los">Kopf dreht sich</button><button type="button" class="btn secondary small" data-a="stopp">Stopp</button><button type="button" class="btn secondary small" data-a="neu">Neu</button></div>
 <div class="ergebnis" data-o="erg">Gehirn: <b>keine Drehung.</b></div>
 <p class="simt">Orange: Kuppel mit Sinneshärchen · blau: Lymphe. Vereinfachtes Modell – die echte Lymphe braucht einige Sekunden.</p>
</div>""",
}

CSS = """
.sim { border: 2px solid #2E7D8C; border-radius: 12px; background: #fff; padding: 12px 14px; display: grid; gap: 8px; }
.simh { display: flex; gap: 8px; align-items: center; font-size: 18px; flex-wrap: wrap; }
.sim canvas, .sim svg { width: 100%; height: auto; border-radius: 10px; background: #F2F3EE; display: block; }
.sim label { display: grid; gap: 4px; font-size: 17px; } .sim input[type=range] { width: 100%; min-height: 44px; }
.simb { display: flex; gap: 8px; flex-wrap: wrap; } .simb .btn { min-height: 44px; }
.sim .btn.small { width: auto; font-size: 16px; padding: 8px 14px; }
.sim .btn.secondary { background: #fff; color: #3B4A2F; border: 2px solid #3B4A2F; }
.simb .btn[aria-pressed="true"] { background: #3B4A2F; color: #fff; }
.simt { margin: 0; font-size: 16px; color: #5E6652; }
.sim .ergebnis { background: #3B4A2F; color: #fff; border-radius: 10px; padding: 10px 12px; font-size: 18px; line-height: 1.35; }
.sim .ergebnis b { color: #FFE7A3; }
.sim .mk.a { color: #2E7D8C; } .sim .mk.b { color: #D9772B; }
details.simd { margin: 10px 0; } details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; min-height: 44px; display: flex; align-items: center; }
"""

JS = """<script>
(function () {
  var SIMINIT = window.SIMINIT = window.SIMINIT || {};
  function q(box, o) { return box.querySelector('[data-o="' + o + '"]'); }
  function f(x, d) { return (typeof d === "number" ? x.toFixed(d) : String(x)).replace(".", ","); }
  function tsd(x) { return String(Math.round(x)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\\u202f"); }
  var RUHIG = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  SIMINIT.druck = function (box) {
    var cv = box.querySelector("canvas"), g = cv.getContext("2d"), fr = 2, a = 2, luft = true, lauf = !RUHIG, t0 = 0, tt = 0;
    var FN = ["", "sehr langsam", "langsam", "mittel", "schnell", "sehr schnell"], AN = ["", "klein", "mittel", "groß"];
    var P = []; for (var c = 0; c < 34; c++) for (var r = 0; r < 6; r++) P.push([30 + c * 18, 26 + r * 22 + (c % 2 ? 6 : 0), c === 17 && r === 2]);
    function zeichne(t) {
      g.clearRect(0, 0, 640, 300); g.fillStyle = "#F2F3EE"; g.fillRect(0, 0, 640, 300);
      var lam = 260 / fr * 1.4, om = 2 * Math.PI * fr * 0.35, amp = 3 + a * 3;
      g.fillStyle = "#3B4A2F"; g.fillRect(4, 20, 12, 140); g.fillStyle = "#D9772B"; g.fillRect(16 + (luft ? amp : 0) * Math.sin(om * t), 26, 6, 128);
      if (luft) P.forEach(function (p) { var s = amp * Math.sin(om * t - 2 * Math.PI * (p[0] - 20) / lam); g.beginPath(); g.fillStyle = p[2] ? "#A33A2B" : "#2E7D8C"; g.arc(p[0] + s, p[1], p[2] ? 7 : 5, 0, 7); g.fill(); });
      else { g.fillStyle = "#5E6652"; g.font = "bold 22px sans-serif"; g.fillText("Vakuum: keine Teilchen – kein Schall", 120, 95); }
      g.strokeStyle = "#5E6652"; g.setLineDash([5, 5]); g.beginPath(); g.moveTo(30, 230); g.lineTo(630, 230); g.stroke(); g.setLineDash([]);
      g.fillStyle = "#D9772B"; g.font = "bold 20px sans-serif"; g.fillText("p", 8, 236);
      if (luft) { g.strokeStyle = "#D9772B"; g.lineWidth = 4; g.beginPath();
        for (var x = 30; x <= 630; x += 4) { var y = 230 - (12 + a * 10) * Math.cos(om * t - 2 * Math.PI * (x - 20) / lam); if (x === 30) g.moveTo(x, y); else g.lineTo(x, y); } g.stroke(); g.lineWidth = 1; }
    }
    function tick(ms) { if (lauf) tt += (ms - (t0 || ms)) / 1000; t0 = ms; zeichne(tt); requestAnimationFrame(tick); }
    box.querySelectorAll("input").forEach(function (i) { i.addEventListener("input", function () {
      if (i.dataset.i === "f") { fr = +i.value; q(box, "f").textContent = FN[fr]; } else { a = +i.value; q(box, "a").textContent = AN[a]; } }); });
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return;
      if (b.dataset.a === "luft") { luft = !luft; b.textContent = luft ? "Luft absaugen (Vakuum)" : "Luft wieder hinein"; }
      else { lauf = !lauf; b.textContent = lauf ? "Anhalten" : "Weiter"; } });
    if (!lauf) box.querySelector('[data-a="pause"]').textContent = "Weiter";
    requestAnimationFrame(tick);
  };

  SIMINIT.echo = function (box) {
    var M = { gewitter: { v: 340, k: 0.2, med: "Luft", hin: false, ziel: "Gewitter" }, echo: { v: 340, k: 0.05, med: "Luft", hin: true, ziel: "Wand" },
              lot: { v: 1480, k: 0.01, med: "Wasser", hin: true, ziel: "Seegrund" } };
    var art = "gewitter", r = box.querySelector("input"), svg = box.querySelector("svg"), t0 = null;
    function zeit() { return +r.value * M[art].k; }
    function zeig() {
      var m = M[art], t = zeit(), s = m.v * t, d = m.hin ? s / 2 : s, nk = m.k >= 0.1 ? 1 : 2;   /* so viele Stellen, wie der Regler wirklich hat – Anzeige und Rechnung passen zusammen */
      q(box, "t").textContent = f(t, nk) + " s";
      q(box, "rech").innerHTML = "Weg des Schalls: s = v · t = " + tsd(m.v) + " m/s · " + f(t, nk) + " s = <b>" + f(s, s < 10 ? 2 : 0) + " m</b>";
      q(box, "erg").innerHTML = m.hin ? m.ziel + ": hin <b>und</b> zurück – also durch 2: <b>" + f(d, d < 10 ? 2 : d < 100 ? 1 : 0) + " m</b>"
        : "Entfernung des Gewitters: <b>" + f(d, 0) + " m</b> · Faustregel: " + f(t, 1) + " : 3 ≈ <b>" + f(t / 3, 1) + " km</b>";
      q(box, "info").textContent = m.hin ? "Schall in " + m.med + ": " + tsd(m.v) + " m/s. Achtung Falle: Ohne »durch 2« wäre das Ziel doppelt so weit weg."
        : "Das Licht des Blitzes ist praktisch sofort da – nur der Donner braucht Zeit.";
    }
    function bild(ms) {
      if (t0 === null) t0 = ms; var m = M[art], p = RUHIG ? 1 : ((ms - t0) / 2200) % 1;
      var x0 = 30, x1 = 290, pos = m.hin ? (p < 0.5 ? x0 + (x1 - x0) * p * 2 : x1 - (x1 - x0) * (p - 0.5) * 2) : x1 - (x1 - x0) * p;
      var quelle = m.hin ? "<rect x='14' y='36' width='16' height='18' rx='3' fill='#3B4A2F'/>" : "<path d='M282 6 l-10 22 h10 l-8 24 l20 -30 h-11 l8 -16 z' fill='#D9A12B'/><text x='300' y='80' font-size='11' fill='#5E6652' text-anchor='end'>Blitz</text>";
      var ziel = m.hin ? "<rect x='292' y='14' width='14' height='62' fill='" + (art === "lot" ? "#8A6A44" : "#7A7F72") + "'/><text x='300' y='88' font-size='11' fill='#5E6652' text-anchor='end'>" + m.ziel + "</text>"
        : "<circle cx='22' cy='45' r='10' fill='#F1D8B8' stroke='#8A6A44'/><text x='8' y='80' font-size='11' fill='#5E6652'>du</text>";
      var bg = art === "lot" ? "<rect x='0' y='0' width='320' height='90' fill='#DCEBF2'/>" : "";
      svg.innerHTML = bg + "<line x1='30' y1='45' x2='290' y2='45' stroke='#B7C2A2' stroke-dasharray='6 5'/>" + quelle + ziel
        + "<circle cx='" + pos + "' cy='45' r='7' fill='#2E7D8C'/>" + (m.hin ? "<text x='160' y='30' font-size='12' text-anchor='middle' fill='#1F5966'>" + (p < 0.5 ? "hin →" : "← zurück") + "</text>" : "");
      if (!RUHIG) requestAnimationFrame(bild);
    }
    r.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return; art = b.dataset.a;
      box.querySelectorAll("[data-a]").forEach(function (x) { var on = x === b; x.setAttribute("aria-pressed", on); x.classList.toggle("secondary", !on); });
      r.value = art === "gewitter" ? 15 : art === "echo" ? 20 : 10; zeig(); if (RUHIG) bild(0); });
    zeig(); requestAnimationFrame(bild);
  };

  var LEITER = [[0, "Hörschwelle"], [30, "Blätterrauschen"], [50, "Unterhaltung"], [60, "Gespräch, Büro"], [70, "Straßenverkehr"], [80, "starker Verkehr"],
                [90, "Lkw, Fabrikhalle"], [100, "Kopfhörer laut, Disco"], [110, "Presslufthammer"], [120, "Rockkonzert vorne, Schmerzgrenze beginnt"], [130, "Schmerzgrenze"], [150, "Schuss am Ohr (Spitze)"]];
  function name(L) { var n = ""; LEITER.forEach(function (b) { if (L >= b[0] - 2) n = b[1]; }); return (LEITER.some(function (b) { return b[0] === L; }) ? "" : "etwa: ") + n; }
  SIMINIT.db = function (box) {
    var ra = box.querySelector('[data-i="a"]'), rb = box.querySelector('[data-i="b"]'), svg = box.querySelector("svg");
    var y = function (L) { return 196 - L * 1.15; }, g = "<rect x='40' y='" + y(160) + "' width='18' height='" + (y(85) - y(160)) + "' fill='#F3D8D1'/><rect x='40' y='" + y(85) + "' width='18' height='" + (y(0) - y(85)) + "' fill='#DDE8CC'/>";
    for (var L = 0; L <= 160; L += 20) g += "<text x='34' y='" + (y(L) + 4) + "' font-size='10' text-anchor='end' fill='#5E6652'>" + L + "</text>";
    LEITER.forEach(function (b) { if ([0, 30, 60, 80, 100, 120, 150].indexOf(b[0]) >= 0) g += "<line x1='58' x2='66' y1='" + y(b[0]) + "' y2='" + y(b[0]) + "' stroke='#3B4A2F'/><text x='70' y='" + (y(b[0]) + 4) + "' font-size='11' fill='#1F2A1C'>" + b[0] + " · " + b[1] + "</text>"; });
    g += "<line x1='58' x2='316' y1='" + y(85) + "' y2='" + y(85) + "' stroke='#8C3B2E' stroke-dasharray='3 3'/><text x='316' y='" + (y(85) - 3) + "' font-size='10' fill='#8C3B2E' text-anchor='end'>ab 85 dB: Gehörschutz tragen</text>";
    g += "<polygon class='ma' points='40,0 26,-7 26,7' fill='#2E7D8C'/><polygon class='mb' points='40,0 26,-7 26,7' fill='#D9772B'/>";
    svg.innerHTML = g;
    var HOCH = "⁰¹²³⁴⁵⁶⁷⁸⁹";
    function hoch(n) { return String(n).split("").map(function (c) { return HOCH[+c]; }).join(""); }
    function fak(x) { if (x >= 1e6) { var e = Math.floor(Math.log10(x) + 1e-9), m = x / Math.pow(10, e); return (Math.abs(m - 1) < 0.01 ? "" : "rund " + f(m, 1) + " · ") + "10" + hoch(e); }
      return x >= 100 ? tsd(x) : x >= 10 ? f(x, 0) : f(x, 1); }
    function zeig() {
      var a = +ra.value, b = +rb.value, d = Math.abs(b - a);
      q(box, "a").textContent = a + " dB"; q(box, "b").textContent = b + " dB"; q(box, "anam").textContent = name(a); q(box, "bnam").textContent = name(b);
      svg.querySelector(".ma").setAttribute("transform", "translate(0," + y(a) + ")"); svg.querySelector(".mb").setAttribute("transform", "translate(0," + y(b) + ")");
      q(box, "erg").innerHTML = d === 0 ? "Beide gleich laut gemessen." : (b > a ? "B" : "A") + " ist <b>" + d + " dB</b> höher = " + f(d / 10, d % 10 ? 1 : 0) + " Zehnerstufe" + (d === 10 ? "" : "n")
        + "<br>Intensität <b>× " + fak(Math.pow(10, d / 10)) + "</b> · Schalldruck <b>× " + fak(Math.pow(10, d / 20)) + "</b>";
    }
    ra.addEventListener("input", zeig); rb.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var bt = ev.target.closest("[data-n]"); if (!bt) return; var n = +bt.dataset.n, L = 80 + 10 * Math.log10(n);
      box.querySelectorAll("[data-n]").forEach(function (x) { x.setAttribute("aria-pressed", x === bt); x.classList.toggle("secondary", x !== bt); });
      q(box, "quell").innerHTML = n + (n === 1 ? " Maschine" : " gleiche Maschinen") + " mit je 80 dB: zusammen etwa <b>" + f(Math.round(L), 0) + " dB</b>"
        + (n === 1 ? "." : " – nicht " + (80 * n) + " dB! " + n + "-fache Intensität = +" + f(Math.round(10 * Math.log10(n)), 0) + " dB."); });
    zeig();
  };

  SIMINIT.richtung = function (box) {
    var r = box.querySelector("input"), svg = box.querySelector("svg");
    function zeig() {
      var w = +r.value, a = w * Math.PI / 180, qx = 160 - 115 * Math.sin(a), qy = 130 - 115 * Math.cos(a);
      var umweg = 0.2 * Math.abs(Math.sin(a)), dt = umweg / 340 * 1000;
      q(box, "w").textContent = w + "° " + (w === 0 ? "(genau vorne)" : w === 90 ? "(genau links)" : w === 180 ? "(genau hinten)" : w < 90 ? "(vorne links)" : "(hinten links)");
      svg.innerHTML = "<text x='160' y='16' font-size='12' text-anchor='middle' fill='#5E6652'>vorne</text><text x='160' y='246' font-size='12' text-anchor='middle' fill='#5E6652'>hinten</text>"
        + "<line x1='" + qx + "' y1='" + qy + "' x2='118' y2='130' stroke='#2E7D8C' stroke-width='3'/><line x1='" + qx + "' y1='" + qy + "' x2='202' y2='130' stroke='#D9772B' stroke-width='3' stroke-dasharray='7 5'/>"
        + "<circle cx='160' cy='130' r='42' fill='#F1D8B8' stroke='#8A6A44' stroke-width='2'/><polygon points='150,90 170,90 160,76' fill='#F1D8B8' stroke='#8A6A44' stroke-width='2'/>"
        + "<ellipse cx='117' cy='130' rx='6' ry='13' fill='#D9B48C'/><ellipse cx='203' cy='130' rx='6' ry='13' fill='#D9B48C'/>"
        + "<circle cx='" + qx + "' cy='" + qy + "' r='11' fill='#A33A2B'/><text x='" + qx + "' y='" + (qy + 4) + "' font-size='10' fill='#fff' text-anchor='middle'>!</text>";
      q(box, "erg").innerHTML = "Umweg zum rechten Ohr ≈ " + f(umweg, 2) + " m<br>Zeitunterschied <b>" + f(dt, 2) + " ms</b>"
        + (dt < 0.05 ? "<br>Kein Unterschied – vorne oder hinten? Da irren wir uns oft." : "");
    }
    r.addEventListener("input", zeig); zeig();
  };

  SIMINIT.bogen = function (box) {
    var cv = box.querySelector("canvas"), c = cv.getContext("2d"), s = { wh: 0, ziel: 0, wl: 0, ph: 0, pl: 0 }, last = null;
    function schritt(dt) { s.wh += Math.max(-dt * 3, Math.min(dt * 3, s.ziel - s.wh)); s.wl += (s.wh - s.wl) * dt / 2.5; s.ph += s.wh * dt; s.pl += s.wl * dt; }
    function draw(ms) {
      var dt = last === null ? 0 : Math.min(0.1, (ms - last) / 1000); last = ms; schritt(dt);
      var cx = 240, cy = 175, R = 128, rel = s.wh - s.wl;
      c.clearRect(0, 0, 480, 360); c.fillStyle = "#F2F3EE"; c.fillRect(0, 0, 480, 360);
      c.lineWidth = 28; c.strokeStyle = "#DDEEF1"; c.beginPath(); c.arc(cx, cy, R, 0, 7); c.stroke(); c.lineWidth = 1;
      c.fillStyle = "#2E7D8C"; for (var i = 0; i < 16; i++) { var a = s.pl + i * Math.PI / 8; c.beginPath(); c.arc(cx + R * Math.cos(a), cy + R * Math.sin(a), 5, 0, 7); c.fill(); }
      var a0 = s.ph - Math.PI / 2, bieg = Math.max(-0.9, Math.min(0.9, -rel * 0.7));
      c.save(); c.translate(cx + R * Math.cos(a0), cy + R * Math.sin(a0)); c.rotate(a0 + Math.PI / 2); c.fillStyle = "#D9772B"; c.beginPath();
      c.moveTo(-12, 16); c.quadraticCurveTo(bieg * 30, 0, bieg * 46, -20); c.lineTo(12 + bieg * 46, -20); c.quadraticCurveTo(12 + bieg * 30, 0, 12, 16); c.fill(); c.restore();
      c.save(); c.translate(cx, cy); c.rotate(s.ph); c.fillStyle = "#F1D8B8"; c.strokeStyle = "#8A6A44"; c.lineWidth = 3;
      c.beginPath(); c.arc(0, 0, 46, 0, 7); c.fill(); c.stroke(); c.beginPath(); c.moveTo(-10, -44); c.lineTo(0, -62); c.lineTo(10, -44); c.fill(); c.stroke(); c.restore();
      var dreht = Math.abs(s.wh) > 0.05;
      q(box, "erg").innerHTML = Math.abs(rel) < 0.18 ? "Gehirn: <b>keine Drehung</b>" + (dreht ? " – obwohl sich der Kopf gleichmäßig dreht!" : ".")
        : rel > 0 ? "Gehirn: <b>Ich drehe mich.</b> Die träge Lymphe bleibt zurück und biegt die Kuppel."
        : "Gehirn: <b>Ich drehe mich in die andere Richtung!</b>" + (dreht ? "" : " – obwohl der Kopf steht. Das ist Schwindel.");
      requestAnimationFrame(draw);
    }
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return;
      if (b.dataset.a === "los") s.ziel = 1.6; else if (b.dataset.a === "stopp") s.ziel = 0; else { s.wh = s.ziel = s.wl = s.ph = s.pl = 0; } });
    requestAnimationFrame(draw);
  };

  function start() { document.querySelectorAll(".sim[data-sim]").forEach(function (b) { if (!b.dataset.go && SIMINIT[b.dataset.sim] && b.offsetParent !== null) { b.dataset.go = "1"; SIMINIT[b.dataset.sim](b); } }); }
  window.simStart = start;
  document.addEventListener("toggle", function () { start(); }, true);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
</script>"""
