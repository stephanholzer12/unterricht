"""Simulationen zum Selbst-Regeln für TÖW 5AB K1.9 Globalisierung, KI und Klima (Standard 14.11.2026).
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in JS (window.SIMINIT[name](box)).
Theorie-Seite: Blöcke ("sim", name). Arbeitsblatt: Feld "sim" einer Aufgabe → aufklappbares »Ausprobieren«.
Fachliche Grundlagen (Stand 22.11.2026, Quellen in inhalt.QUELLEN):
- overshoot: Erden = 365 / Tag des Overshoot Day (Modell des Global Footprint Network, gerundet). Österreich 2026: 2. April = Tag 92 (≈ 3,97);
  Welt 2026: 30. Juli = Tag 211 (≈ 1,73). Umgekehrt: Tag = 365 / Erden. Vereinfacht: Schaltjahre und Datenrevisionen bleiben unberücksichtigt.
- ki: Strom pro Tag = Personen · Fragen · Wh je Frage. Gemini 0,24 Wh, ChatGPT 0,34 Wh (Herstellerangaben, ORF 22.08.2025, ohne Training).
  Vergleich Haushalt: 1,31 TWh / 375 000 Haushalte ≈ 3 490 kWh pro Jahr (ORF 17.07.2026) → ≈ 9,6 kWh pro Tag.
- rz: Stufe 2 500 MW → 4,38 TWh ≈ ORF »bis zu 4,4 TWh«.
- rz: Energie pro Jahr = Leistung · 8760 h (Modell: Volllast das ganze Jahr – echte Auslastung ist niedriger). 150 MW → 1,314 TWh ≈ ORF-Wert 1,31 TWh.
  Haushalte = kWh / 3 493; Anteil Oberösterreich = TWh / 14 TWh (2024)."""

TITEL = {"overshoot": "Overshoot-Rechner: Wie viele Erden?", "ki": "KI-Strom-Rechner", "rz": "Rechenzentrum-Rechner"}
ZEILE = {"overshoot": "Schieb den Overshoot Day – wie viele Erden bräuchten wir?",
         "ki": "Wie viele Fragen stellt eure Klasse? Wie viel Strom ist das?",
         "rz": "Stell die Leistung ein – wie viele Haushalte, wie viel von Oberösterreich?"}

HTML = {
 "overshoot": """<div class="sim" data-sim="overshoot">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Overshoot-Rechner: Wie viele Erden?</b></div>
 <div class="simb" role="group" aria-label="Beispiel"><button type="button" class="btn small" data-a="at" aria-pressed="true">Österreich 2026</button><button type="button" class="btn secondary small" data-a="welt" aria-pressed="false">Welt 2026</button></div>
 <svg viewBox="0 0 320 96" aria-hidden="true"></svg>
 <label>Overshoot Day: <b data-o="tag">2. April (Tag 92)</b><input type="range" min="30" max="365" step="1" value="92" data-i="tag" aria-label="Tag des Jahres"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Rechnung: 365 Tage : Tag des Overshoot Day. Vereinfachtes Modell, Werte gerundet.</p>
</div>""",
 "ki": """<div class="sim" data-sim="ki">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>KI-Strom-Rechner</b></div>
 <div class="simb" role="group" aria-label="KI"><button type="button" class="btn small" data-a="g" aria-pressed="true">Gemini 0,24 Wh</button><button type="button" class="btn secondary small" data-a="o" aria-pressed="false">ChatGPT 0,34 Wh</button></div>
 <label>Kadetten: <b data-o="p">25</b><input type="range" min="1" max="30" step="1" value="25" data-i="p" aria-label="Anzahl Kadetten"></label>
 <label>KI-Fragen pro Person und Tag: <b data-o="n">20</b><input type="range" min="1" max="200" step="1" value="20" data-i="n" aria-label="Fragen pro Tag"></label>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Herstellerangaben pro Textfrage, ohne Training. Bilder und Videos brauchen viel mehr.</p>
</div>""",
 "rz": """<div class="sim" data-sim="rz">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Rechenzentrum-Rechner</b></div>
 <div class="simb" role="group" aria-label="Beispiel"><button type="button" class="btn small" data-a="s1" aria-pressed="true">Kronstorf Stufe 1 (150 MW)</button><button type="button" class="btn secondary small" data-a="s2" aria-pressed="false">Stufe 2 (500 MW)</button></div>
 <label>Leistung: <b data-o="mw">150 MW</b><input type="range" min="10" max="650" step="10" value="150" data-i="mw" aria-label="Leistung in Megawatt"></label>
 <svg viewBox="0 0 320 60" aria-hidden="true"></svg>
 <div class="ergebnis" data-o="erg"></div>
 <p class="simt">Modell: Volllast rund um die Uhr (8760 h). In echt ist die Auslastung niedriger. Haushalt ≈ 3 500 kWh pro Jahr.</p>
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
details.simd { margin: 10px 0; } details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; min-height: 44px; display: flex; align-items: center; }
"""

JS = """<script>
(function () {
  var SIMINIT = window.SIMINIT = window.SIMINIT || {};
  function q(box, o) { return box.querySelector('[data-o="' + o + '"]'); }
  function f(x, d) { return (typeof d === "number" ? x.toFixed(d) : String(x)).replace(".", ","); }
  function tsd(x) { return String(Math.round(x)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\\u202f"); }
  function knopf(box, wahl) { box.querySelectorAll(".simb [data-a]").forEach(function (x) { var an = x === wahl; x.setAttribute("aria-pressed", an); x.classList.toggle("secondary", !an); }); }
  var MON = ["Jänner", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"], ML = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  function datum(tag) { var m = 0; while (tag > ML[m]) { tag -= ML[m]; m++; } return tag + ". " + MON[m]; }

  SIMINIT.overshoot = function (box) {
    var r = box.querySelector('[data-i="tag"]'), svg = box.querySelector("svg");
    function zeig() {
      var tag = +r.value, erden = 365 / tag, x = 10 + 300 * tag / 365, g = "";
      g += "<rect x='10' y='14' width='300' height='26' rx='6' fill='#fff' stroke='#5E6652'/>";
      g += "<rect x='10' y='14' width='" + (x - 10).toFixed(1) + "' height='26' rx='6' fill='#7FA83A'/>";
      if (tag < 365) g += "<rect x='" + x.toFixed(1) + "' y='14' width='" + (310 - x).toFixed(1) + "' height='26' fill='#A33A2B' opacity='.85'/><text x='" + ((x + 310) / 2).toFixed(1) + "' y='32' font-size='12' fill='#fff' text-anchor='middle' font-weight='700'>auf Pump</text>";
      var n = Math.min(10, Math.ceil(erden - 1e-9));
      for (var i = 0; i < n; i++) { var anteil = Math.min(1, erden - i); g += "<circle cx='" + (22 + i * 30) + "' cy='70' r='12' fill='#2A5C8C' opacity='" + (0.25 + 0.75 * anteil).toFixed(2) + "'/>"; }
      svg.innerHTML = g;
      q(box, "tag").textContent = datum(tag) + " (Tag " + tag + ")";
      q(box, "erg").innerHTML = "365 : " + tag + " = <b>" + f(erden, 2) + " Erden</b>" + (erden > 1.005 ? " – das Naturbudget reicht nur bis zum " + datum(tag) + "." : " – das Budget reicht das ganze Jahr.");
    }
    r.addEventListener("input", function () { knopf(box, null); zeig(); });
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return; r.value = b.dataset.a === "at" ? 92 : 211; knopf(box, b); zeig(); });
    zeig();
  };

  SIMINIT.ki = function (box) {
    var rp = box.querySelector('[data-i="p"]'), rn = box.querySelector('[data-i="n"]'), wh = 0.24;
    function zeig() {
      var p = +rp.value, n = +rn.value, tag = p * n * wh, jahr = tag * 365 / 1000, hh = jahr / 3493 * 365;
      q(box, "p").textContent = p; q(box, "n").textContent = n;
      q(box, "erg").innerHTML = p + " · " + n + " · " + f(wh, 2) + " Wh = <b>" + f(tag, tag < 100 ? 1 : 0) + " Wh pro Tag</b><br>im Jahr: <b>" + f(jahr, 1) + " kWh</b> – so viel braucht ein Haushalt in etwa <b>" + f(hh, 1) + " Tagen</b>";
    }
    rp.addEventListener("input", zeig); rn.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return; wh = b.dataset.a === "g" ? 0.24 : 0.34; knopf(box, b); zeig(); });
    zeig();
  };

  SIMINIT.rz = function (box) {
    var r = box.querySelector('[data-i="mw"]'), svg = box.querySelector("svg");
    function zeig() {
      var mw = +r.value, twh = mw * 8760 / 1e6, hh = twh * 1e9 / 3493, ant = twh / 14 * 100;
      q(box, "mw").textContent = mw + " MW";
      var w = Math.min(300, 300 * ant / 100);
      svg.innerHTML = "<rect x='10' y='14' width='300' height='24' rx='6' fill='#fff' stroke='#5E6652'/><rect x='10' y='14' width='" + w.toFixed(1) + "' height='24' rx='6' fill='#D9772B'/>"
        + "<text x='10' y='54' font-size='11' fill='#5E6652'>Anteil am Stromverbrauch Oberösterreichs (14 TWh, 2024)</text>";
      q(box, "erg").innerHTML = mw + " MW · 8760 h ≈ <b>" + f(twh, 2) + " TWh pro Jahr</b><br>so viel wie rund <b>" + tsd(Math.round(hh / 1000) * 1000) + " Haushalte</b> · <b>" + f(ant, 1) + " %</b> von Oberösterreich";
    }
    r.addEventListener("input", function () { knopf(box, null); zeig(); });
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-a]"); if (!b) return; r.value = b.dataset.a === "s1" ? 150 : 500; knopf(box, b); zeig(); });
    zeig();
  };

  function start() { document.querySelectorAll(".sim[data-sim]").forEach(function (b) { if (!b.dataset.go && SIMINIT[b.dataset.sim] && b.offsetParent !== null) { b.dataset.go = "1"; SIMINIT[b.dataset.sim](b); } }); }
  window.simStart = start;
  document.addEventListener("toggle", function () { start(); }, true);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
</script>"""
