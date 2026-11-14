"""Interaktive Simulationen für NAWI 2AB K1.5 Säuren und Basen (Kadetten regeln selbst, sehen sofort die Wirkung).
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in SIM_JS (window.SIMINIT[name](box)).
Theorie-Seite: Blöcke ("sim", name). Arbeitsblatt: Feld "sim" einer Aufgabe → aufklappbares »Ausprobieren«.
Fachliche Grundlagen (Stand 14.11.2026):
- Rotkraut: Farben ungefähr (Anthocyane); Natron (NaHCO3) erreicht höchstens etwa pH 8,3; Speiseessig etwa pH 2,5–3.
- Neutralisation: H3O+ + OH- -> 2 H2O, Na+ und Cl- bleiben gelöst (Kochsalzlösung), Säure + Lauge ist exotherm.
- Blut: Henderson-Hasselbalch-Gleichung pH = 6,1 + lg( c(HCO3-) / (0,03 * pCO2) ), HCO3- in mmol/l, pCO2 in mmHg.
  Ruhe 24 / 40 -> 7,40 · nach Sprint ca. 12 / 40 -> 7,10 (Studie: 7,13) · Hecheln in Ruhe 24 / 25 -> 7,61 (Alkalose)."""

TITEL = {"rotkraut": "Rotkraut-Mixer", "ph": "pH-Schieber", "neutral": "Säure trifft Lauge", "blut": "Blut-pH-Regler"}
ZEILE = {"rotkraut": "Gib Essig oder Natron dazu – wie ändert sich die Farbe?",
         "ph": "Schieb den pH-Wert – Farbe, Beispiel und Faktor ändern sich mit.",
         "neutral": "Tropf Natronlauge in Salzsäure – wann ist die Lösung neutral?",
         "blut": "Regle Atmung und Puffer – bleibt dein Blut im grünen Bereich?"}

HTML = {
 "rotkraut": """<div class="sim" data-sim="rotkraut">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Rotkraut-Mixer</b></div>
 <div class="rkm"><svg viewBox="0 0 120 150" class="rkglas" aria-hidden="true"><path d="M18 10 h84 l-8 128 a8 8 0 0 1 -8 8 h-52 a8 8 0 0 1 -8 -8 z" fill="#EEF3F8" stroke="#1F2A1C" stroke-width="3"/><path class="rkfl" d="M24 40 h72 l-6 98 a6 6 0 0 1 -6 6 h-48 a6 6 0 0 1 -6 -6 z" fill="#5A63B0"/><g class="rkbl"></g></svg>
  <div><div class="phz"><span class="phw" data-o="ph">pH ca. 7,5</span></div><p class="simt" data-o="wort">blau-violett – leicht basisch</p><p class="simt" data-o="z">Im Glas: Leitungswasser + Rotkrautsaft</p></div></div>
 <div class="simb"><button type="button" class="btn" data-a="essig">+ 1 Tropfen Essig</button><button type="button" class="btn" data-a="natron">+ 1 Prise Natron</button><button type="button" class="btn ghost" data-a="neu">Neu</button></div>
 <p class="simt" data-o="info">Tipp: Erst Essig, dann Natron – was passiert?</p>
 <p class="simt">Vereinfachtes Modell, Farben und Werte ungefähr.</p>
</div>""",
 "ph": """<div class="sim" data-sim="ph">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>pH-Schieber</b></div>
 <div class="phz"><span class="phw" data-o="ph">pH 7,0</span><span class="phk" data-o="art">neutral</span></div>
 <input type="range" min="0" max="14" step="0.1" value="7" aria-label="pH-Wert einstellen">
 <div class="phband" aria-hidden="true"></div>
 <div class="phfarben"><div><span class="sw" data-o="ui"></span>Indikatorpapier</div><div><span class="sw" data-o="rk"></span>Rotkrautsaft</div></div>
 <p class="simt" data-o="vgl"></p>
 <p class="simt" data-o="bsp"></p>
 <p class="simt">Farben ungefähr – echte Papiere und Säfte weichen ab. Faustregel: eine Stufe = Faktor 10.</p>
</div>""",
 "neutral": """<div class="sim" data-sim="neutral">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Säure trifft Lauge</b></div>
 <svg viewBox="0 0 320 200" class="nbox" aria-hidden="true"></svg>
 <div class="nzahl"><span><b data-o="h">10</b> H₃O⁺</span><span><b data-o="oh">0</b> OH⁻</span><span><b data-o="w">0</b> neue H₂O</span><span data-o="t">20,0 °C</span></div>
 <div class="phz"><span class="phk sauer" data-o="art">sauer</span></div>
 <div class="simb"><button type="button" class="btn" data-a="plus">+ 2 OH⁻ (Natronlauge)</button><button type="button" class="btn ghost" data-a="neu">Neu</button></div>
 <p class="simt" data-o="info">Im Becher: Salzsäure mit 10 H₃O⁺ und 10 Cl⁻.</p>
 <p class="simt">Modell mit wenigen Teilchen; Temperatur nur als Richtung (wird wärmer).</p>
</div>""",
 "blut": """<div class="sim" data-sim="blut">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Blut-pH-Regler</b></div>
 <div class="phz"><span class="phw" data-o="ph">pH 7,40</span><span class="phk" data-o="art">normal</span></div>
 <div class="bbar" aria-hidden="true"><span class="bok"></span><i data-o="mark"></i></div>
 <div class="bskala" aria-hidden="true"><span>6,8</span><span>7,1</span><span>7,4</span><span>7,7</span></div>
 <label>CO₂ im Blut (Atmung): <b data-o="co2">40</b> mmHg <span class="simt">← schneller atmen · langsamer atmen →</span><input type="range" min="20" max="70" step="1" value="40" data-i="co2" aria-label="CO2 im Blut"></label>
 <label>Puffer Hydrogencarbonat: <b data-o="hco3">24</b> mmol/l <span class="simt">(Milchsäure beim Sprint verbraucht Puffer)</span><input type="range" min="8" max="34" step="1" value="24" data-i="hco3" aria-label="Hydrogencarbonat"></label>
 <div class="simb"><button type="button" class="btn ghost" data-a="ruhe">Ruhe</button><button type="button" class="btn ghost" data-a="sprint">Nach dem Sprint</button><button type="button" class="btn ghost" data-a="atmen">Sprint + schnell atmen</button><button type="button" class="btn ghost" data-a="hecheln">Hecheln in Ruhe</button></div>
 <p class="simt" data-o="info"></p>
 <p class="simt">Gerechnet mit der Henderson-Hasselbalch-Gleichung (Medizin): pH = 6,1 + lg (Hydrogencarbonat ÷ (0,03 · CO₂)). Vereinfacht – der Körper regelt noch mehr.</p>
</div>""",
}

CSS = """
.sim { border: 2px solid #2E7D8C; border-radius: 12px; background: #fff; padding: 12px 14px; display: grid; gap: 8px; }
.simh { display: flex; gap: 8px; align-items: center; font-size: 18px; flex-wrap: wrap; }
.sim label { display: grid; gap: 4px; font-size: 17px; } .sim input[type=range] { width: 100%; min-height: 44px; }
.simb { display: flex; gap: 8px; flex-wrap: wrap; } .simb .btn { min-height: 44px; }
.sim .btn { font: inherit; font-size: 16px; font-weight: 700; padding: 8px 14px; border-radius: 999px; border: 2px solid #2E7D8C; background: #2E7D8C; color: #fff; cursor: pointer; }
.sim .btn.ghost { background: #fff; color: #2E7D8C; }
.simt { margin: 0; font-size: 16px; color: #5E6652; }
.phz { display: flex; gap: 12px; align-items: baseline; flex-wrap: wrap; } .phw { font-size: 36px; font-weight: 700; color: #3B4A2F; font-variant-numeric: tabular-nums; }
.phk { font-size: 19px; font-weight: 700; border-radius: 999px; padding: 2px 12px; color: #fff; background: #7CB342; } .phk.sauer { background: #C0392B; } .phk.basisch { background: #2A5C8C; }
.phband { height: 16px; border-radius: 8px; }
.phfarben { display: flex; gap: 16px; flex-wrap: wrap; font-size: 17px; } .phfarben div { display: flex; gap: 8px; align-items: center; }
.sw { display: inline-block; width: 44px; height: 30px; border-radius: 8px; border: 2px solid #1F2A1C; }
.rkm { display: grid; grid-template-columns: 110px 1fr; gap: 12px; align-items: center; } .rkglas { width: 110px; height: auto; }
.rkfl { transition: fill .5s; }
.rkm .phw { font-size: 28px; white-space: nowrap; }
.nbox { width: 100%; height: auto; background: #FBF7F2; border: 2px solid #1F2A1C; border-radius: 0 0 14px 14px; }
.nzahl { display: flex; gap: 14px; flex-wrap: wrap; font-size: 17px; } .nzahl b { font-size: 22px; color: #3B4A2F; }
.bbar { position: relative; height: 22px; border-radius: 8px; background: linear-gradient(90deg, #E8B4AC 0%, #E8B4AC 55%, #DFE5D0 55%, #DFE5D0 65%, #B9CDE4 65%, #B9CDE4 100%); }
.bbar .bok { position: absolute; top: 0; bottom: 0; left: 55%; width: 10%; background: #7FA83A; }
.bbar i { position: absolute; top: -6px; width: 6px; height: 34px; margin-left: -3px; background: #1F2A1C; border-radius: 3px; transition: left .3s; }
.bskala { display: flex; justify-content: space-between; font-size: 14px; color: #5E6652; }
details.simd { border: 2px solid #2E7D8C; border-radius: 12px; background: #F3F8F9; margin: 10px 0; }
details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; font-size: 17px; min-height: 44px; padding: 10px 14px; }
details.simd > .sim { border: 0; margin: 0 4px 6px; }
"""

JS = r"""<script>
window.SIMINIT = window.SIMINIT || {};
(function () {
  var UI = ["#C62828","#E53935","#F4511E","#FB8C00","#FFB300","#FDD835","#C0CA33","#7CB342","#43A047","#00897B","#1E88E5","#3949AB","#5E35B1","#6A1B9A","#4A148C"];
  var RK = [[2,"#C2185B"],[4,"#C2508A"],[6,"#8A4C9E"],[7,"#5C5BA8"],[9,"#3F6FB5"],[12,"#3E9A6A"],[14.1,"#D4C21A"]];
  function f(x) { return String(x).replace(".", ","); }
  function rkFarbe(p) { for (var i = 0; i < RK.length; i++) if (p <= RK[i][0] + 0.49) return RK[i][1]; return RK[RK.length - 1][1]; }
  function q(box, k) { return box.querySelector('[data-o="' + k + '"]'); }

  SIMINIT.ph = function (box) {
    var inp = box.querySelector("input");
    var BSP = [[1.5,"Magensaft"],[2.4,"Zitronensaft"],[2.8,"Cola"],[5,"Kaffee, Haut"],[5.5,"Mineralwasser prickelnd"],[6.6,"Milch"],[7,"reines Wasser"],[7.4,"Blut"],[7.5,"Leitungswasser Wr. Neustadt"],[8.1,"Meerwasser"],[8.3,"Natronlösung"],[9.5,"Kernseifenlösung"],[12.5,"nasser Beton"],[13.5,"Rohrreiniger"]];
    box.querySelector(".phband").style.background = "linear-gradient(90deg," + UI.join(",") + ")";
    function zahl(n) { return n >= 1e6 ? Math.round(n / 1e6).toLocaleString("de-AT") + " Millionen" : Math.round(n).toLocaleString("de-AT"); }
    function zeig() {
      var p = Math.round(parseFloat(inp.value) * 10) / 10;
      q(box, "ph").textContent = "pH " + f(p.toFixed(1));
      var art = p < 6.95 ? "sauer" : p > 7.05 ? "basisch" : "neutral"; q(box, "art").textContent = art; q(box, "art").className = "phk " + art;
      q(box, "ui").style.background = UI[Math.min(14, Math.round(p))];
      q(box, "rk").style.background = rkFarbe(p);
      var d = 7 - p, v;
      if (Math.abs(d) < 0.05) v = "Gleich viele H₃O⁺- und OH⁻-Ionen.";
      else if (d > 0) v = "Etwa " + zahl(Math.pow(10, d)) + "-mal so viele H₃O⁺-Ionen wie in neutralem Wasser.";
      else v = "Etwa " + zahl(Math.pow(10, -d)) + "-mal so viele OH⁻-Ionen wie in neutralem Wasser.";
      q(box, "vgl").textContent = v;
      var best = BSP[0]; BSP.forEach(function (b) { if (Math.abs(b[0] - p) < Math.abs(best[0] - p)) best = b; });
      q(box, "bsp").textContent = "In der Nähe: " + best[1] + " (pH " + f(best[0]) + ")";
    }
    inp.addEventListener("input", zeig); zeig();
  };

  SIMINIT.rotkraut = function (box) {
    var netto = 0, schaum = 0;                       /* netto < 0: mehr Essig, > 0: mehr Natron */
    var TAB = {"-8": 3.0, "-7": 3.2, "-6": 3.4, "-5": 3.7, "-4": 4.0, "-3": 4.5, "-2": 5.4, "-1": 6.4, "0": 7.5, "1": 8.0, "2": 8.2};
    function ph() { if (netto <= -8) return 3.0; if (netto >= 3) return 8.3; return TAB[String(netto)]; }
    var WORT = [[3.4,"rot – deutlich sauer"],[4.6,"rosa – sauer"],[6.5,"rotviolett – schwach sauer"],[7.2,"violett – etwa neutral"],[7.9,"blau-violett – leicht basisch"],[9,"blau – schwach basisch"]];
    function zeig(info) {
      var p = ph();
      box.querySelector(".rkfl").setAttribute("fill", p >= 7.3 && p < 7.9 ? "#5A63B0" : rkFarbe(p));
      q(box, "ph").textContent = "pH ca. " + f(p.toFixed(1));
      for (var i = 0; i < WORT.length; i++) if (p <= WORT[i][0]) { q(box, "wort").textContent = WORT[i][1]; break; }
      var g = box.querySelector(".rkbl"); g.innerHTML = "";
      for (var k = 0; k < schaum; k++) g.innerHTML += '<circle cx="' + (34 + (k * 23) % 54) + '" cy="' + (48 + (k * 37) % 70) + '" r="' + (3 + k % 3) + '" fill="#fff" opacity=".85"/>';
      if (info) q(box, "info").textContent = info;
    }
    box.addEventListener("click", function (ev) {
      var a = ev.target.closest("[data-a]"); if (!a) return;
      if (a.dataset.a === "neu") { netto = 0; schaum = 0; zeig("Neu: Leitungswasser + Rotkrautsaft (Leitungswasser ist leicht basisch, pH 7,4–7,6)."); return; }
      if (a.dataset.a === "essig") { netto = Math.max(-12, netto - 1); schaum = 0; zeig(ph() <= 3.05 ? "Viel saurer wird es mit Essig nicht – Speiseessig selbst hat etwa pH 2,5 bis 3." : "Essig gibt H⁺ ab – mehr H₃O⁺, der Saft wird roter."); return; }
      var warSauer = netto < 0; netto = Math.min(6, netto + 1); schaum = warSauer ? 8 : 0;
      zeig(warSauer ? "Es schäumt: Natron fängt die Protonen ab, dabei entsteht CO₂. Die Farbe geht zurück." : (ph() >= 8.25 ? "Mehr Natron hilft nicht: Natronlösung bleibt bei etwa pH 8,3. Für Gelb bräuchte man eine starke Lauge – die verwenden wir nicht." : "Natron nimmt H⁺ auf – leicht basisch, der Saft wird blauer."));
    });
    zeig();
  };

  SIMINIT.neutral = function (box) {
    var svg = box.querySelector(".nbox"), h, oh, w, na, temp;
    function zufall(n, s) { var a = []; for (var i = 0; i < n; i++) { s = (s * 9301 + 49297) % 233280; a.push(s / 233280); } return a; }
    function teilchen(x, y, typ) {
      if (typ === "h") return '<circle cx="' + x + '" cy="' + y + '" r="11" fill="#D9534F" stroke="#1F2A1C" stroke-width="1.5"/><text x="' + x + '" y="' + (y + 4) + '" font-size="10" text-anchor="middle" fill="#fff" font-weight="700">H₃O</text>';
      if (typ === "oh") return '<circle cx="' + x + '" cy="' + y + '" r="11" fill="#2A5C8C" stroke="#1F2A1C" stroke-width="1.5"/><text x="' + x + '" y="' + (y + 4) + '" font-size="10" text-anchor="middle" fill="#fff" font-weight="700">OH</text>';
      if (typ === "w") return '<circle cx="' + x + '" cy="' + y + '" r="8" fill="#AED6F1" stroke="#5E6652" stroke-width="1"/>';
      if (typ === "cl") return '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#6BAF4A"/>';
      return '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#9B6FC4"/>';
    }
    function zeichnen() {
      var s = "", pos = zufall(80, 7), k = 0;
      function setz(n, typ) { for (var i = 0; i < n; i++) { s += teilchen(20 + pos[k % 80] * 280, 20 + pos[(k + 37) % 80] * 160, typ); k++; } }
      setz(Math.min(w, 24), "w"); setz(10, "cl"); setz(na, "na"); setz(h, "h"); setz(oh, "oh");
      svg.innerHTML = s;
      q(box, "h").textContent = h; q(box, "oh").textContent = oh; q(box, "w").textContent = w;
      q(box, "t").textContent = f(temp.toFixed(1)) + " °C";
      var art = h > oh ? "sauer" : oh > h ? "basisch" : "neutral";
      q(box, "art").textContent = art === "neutral" ? "neutral – Kochsalzlösung" : art; q(box, "art").className = "phk " + art;
    }
    function neu() { h = 10; oh = 0; w = 0; na = 0; temp = 20; zeichnen(); q(box, "info").textContent = "Im Becher: Salzsäure mit 10 H₃O⁺ und 10 Cl⁻ (grün)."; }
    box.addEventListener("click", function (ev) {
      var a = ev.target.closest("[data-a]"); if (!a) return;
      if (a.dataset.a === "neu") { neu(); return; }
      na += 2; var neuOH = 2, weg = Math.min(h, neuOH); h -= weg; oh += neuOH - weg; w += 2 * weg; temp += weg * 0.4;
      zeichnen();
      q(box, "info").textContent = weg ? "Jedes OH⁻ fängt ein H⁺: H₃O⁺ + OH⁻ → 2 H₂O. Na⁺ (lila) und Cl⁻ (grün) bleiben übrig." + (h === 0 && oh === 0 ? " Genau neutral!" : "")
        : "Kein H₃O⁺ mehr da – jetzt sammelt sich OH⁻, die Lösung wird basisch.";
    });
    neu();
  };

  SIMINIT.blut = function (box) {
    var co2 = box.querySelector('[data-i="co2"]'), hc = box.querySelector('[data-i="hco3"]');
    var PRE = { ruhe: [40, 24, "Ruhe: Puffer und Atmung im Gleichgewicht."], sprint: [40, 12, "Nach dem Sprint: Milchsäure hat viel Puffer verbraucht – das Blut wird sauer (Studie: 7,13)."],
      atmen: [28, 12, "Du atmest schnell und tief: CO₂ geht hinaus, damit verschwindet Kohlensäure – der pH steigt wieder."],
      hecheln: [25, 24, "Hecheln in Ruhe: zu viel CO₂ abgeatmet – das Blut wird zu basisch (Alkalose). Schwindel, Kribbeln."] };
    function zeig(txt) {
      var p = 6.1 + Math.log10(parseFloat(hc.value) / (0.03 * parseFloat(co2.value)));
      q(box, "co2").textContent = co2.value; q(box, "hco3").textContent = hc.value;
      q(box, "ph").textContent = "pH " + f(p.toFixed(2));
      var art = p < 7.35 ? "Azidose (zu sauer)" : p > 7.45 ? "Alkalose (zu basisch)" : "normal";
      q(box, "art").textContent = art; q(box, "art").className = "phk " + (p < 7.35 ? "sauer" : p > 7.45 ? "basisch" : "");
      q(box, "mark").style.left = Math.max(0, Math.min(100, (p - 6.8) / 0.9 * 100)) + "%";
      if (txt) q(box, "info").textContent = txt;
      else q(box, "info").textContent = "Normal ist 7,35 bis 7,45. Mehr CO₂ = mehr Kohlensäure = saurer. Mehr Puffer = basischer.";
    }
    co2.addEventListener("input", function () { zeig(); }); hc.addEventListener("input", function () { zeig(); });
    box.addEventListener("click", function (ev) { var a = ev.target.closest("[data-a]"); if (!a || !PRE[a.dataset.a]) return; co2.value = PRE[a.dataset.a][0]; hc.value = PRE[a.dataset.a][1]; zeig(PRE[a.dataset.a][2]); });
    zeig();
  };

  function start() { document.querySelectorAll(".sim[data-sim]").forEach(function (b) { if (!b.dataset.go && SIMINIT[b.dataset.sim]) { b.dataset.go = "1"; SIMINIT[b.dataset.sim](b); } }); }
  window.simStart = start;
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
</script>"""


def templates():
    return "".join(f'<template id="simtpl-{k}">{v}</template>' for k, v in HTML.items())
