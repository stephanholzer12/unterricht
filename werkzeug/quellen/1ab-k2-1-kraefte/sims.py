"""Interaktive Simulationen für NAWI 1AB K2.1 Mechanische Kräfte (Kadetten regeln selbst und sehen sofort die Wirkung) – Stand 15.11.2026.
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in JS (window.SIMINIT[name](box)).
Theorie-Seite: Blöcke ("sim", name) und ("extern", key). Arbeitsblatt: Feld "sim" einer Aufgabe bzw. Gruppenkarte → aufklappbares »Ausprobieren«.
Fachliche Grundlagen (gerechnet wird mit den Formeln der Einheit, g = 10 N/kg wie in allen Aufgaben):
- kraefte: F_res = F_rechts − F_links, a = F_res / m, x(t) = v0·t + a·t²/2, v(t) = v0 + a·t (ohne Reibung und Luftwiderstand – wie PhET »Bewegung«).
- gewicht: F_G = m · g. Ortsfaktoren gerundet nach NASA Planetary Fact Sheet (D. R. Williams, NSSDCA, abgerufen 15.11.2026):
  Erde 9,8 (gerechnet mit 10), Mond 1,6, Mars 3,7 m/s² = N/kg. Jupiter bewusst weggelassen (NASA 23,1, PhET 24,8 – Quellen uneinig).
- auftrieb: dichte Dose V = 500 cm³; F_A,max = ρ · V · g; Süßwasser 1000 kg/m³, Meerwasser ca. 1025 kg/m³ (Spektrum Lexikon der Geowissenschaften,
  »Meerwasserdichte«, Beispielwert 1027 kg/m³ – schwankt mit Salzgehalt und Temperatur). Schwimmt: eingetauchter Anteil = m / (ρ · V).
- druck: p = F / A mit F = m · g. Auflageflächen sind MODELLWERTE (Stiefelsohle 30 cm × 10 cm, Ski 170 cm × 7 cm, Schneeschuh 25 cm × 60 cm)
  und beim Gehen trägt EIN Fuß die ganze Last – auf der Seite als »ungefähr« gekennzeichnet.
PHET: externe Simulationen (nur Link, neuer Tab). Geprüft 15.11.2026: phet.colorado.edu/de/search (HTML5-Hinweis, deutscher Titel),
deutsche Texte in github.com/phetsims/babel, Modell von »Kräfte und Bewegung: Grundlagen« in doc/model.md des Repos (Massen: Kiste 50 kg, Kühlschrank 200 kg,
Mülltonne 100 kg, Mann 80 kg, Mädchen 40 kg; Kraft −500 … 500 N; Reibung abschaltbar), Lehrerhandbuch »Masses and Springs: Basics« (Erde 9,8, Mond 1,6, Jupiter 24,8)."""

TITEL = {"kraefte": "Kräfte am Wagen", "gewicht": "Kraftmesser auf Erde, Mond und Mars", "auftrieb": "Schwimmt die Dose?", "druck": "Einsinken im Schnee"}
ZEILE = {"kraefte": "Zieh links und rechts – wann wird der Wagen schneller, wann rollt er gleichmäßig?",
         "gewicht": "Gleiche Masse, anderer Ort – was zeigt der Kraftmesser?",
         "auftrieb": "Füll Sand in die Dose – wann schwimmt, schwebt oder sinkt sie?",
         "druck": "Gleiche Kraft, andere Fläche – wie groß ist der Druck?"}

LIZENZ = "PhET Interactive Simulations, University of Colorado Boulder · Lizenz CC BY 4.0 · kostenlos, auf Deutsch, läuft im Browser am Handy"
PHET = {
 "fmb": {"titel": "Kräfte und Bewegung: Grundlagen", "url": "https://phet.colorado.edu/de/simulations/forces-and-motion-basics",
         "text": "Vier Bildschirme: **Tauziehen** (Kräfte addieren), **Bewegung** (ohne Reibung), **Reibung** und **Beschleunigung**. Häkchen setzen bei Kräfte, Kräftesumme und Werte."},
 "fmb_reibung": {"titel": "Kräfte und Bewegung: Grundlagen – Bildschirm Reibung", "url": "https://phet.colorado.edu/de/simulations/forces-and-motion-basics",
                 "text": "Tippe auf **Reibung**. Schieb die Kiste ganz langsam stärker an: Bis zu einer bestimmten Kraft bleibt sie stehen (**Haftreibung**), dann rutscht sie los (**Gleitreibung**). Stell die Reibung auf »keine« und vergleiche."},
 "federn": {"titel": "Massen und Federn: Grundlagen", "url": "https://phet.colorado.edu/de/simulations/masses-and-springs-basics",
            "text": "Häng Massen an Federn. Im Bildschirm **Experimente** kannst du auf **Mond** oder **Jupiter** wechseln – die Feder dehnt sich weniger bzw. mehr."},
 "auftrieb": {"titel": "Auftrieb: Grundlagen", "url": "https://phet.colorado.edu/de/simulations/buoyancy-basics",
              "text": "Leg Blöcke aus verschiedenen Stoffen ins Wasser und lass dir Gewichtskraft und Auftriebskraft als Pfeile anzeigen. Einige Beschriftungen sind noch englisch."},
 "druck": {"titel": "Unter Druck", "url": "https://phet.colorado.edu/de/simulations/under-pressure",
           "text": "Miss den Druck in verschiedenen Tiefen eines Beckens. Was ändert sich, wenn du tiefer gehst – und was, wenn du eine andere Flüssigkeit nimmst?"},
}

HTML = {
 "kraefte": """<div class="sim" data-sim="kraefte">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Kräfte am Wagen</b></div>
 <svg viewBox="0 0 340 130" class="kwbox" aria-hidden="true"></svg>
 <p class="simt">Punkte = Lage des Wagens alle 0,5 s (4 Sekunden lang)</p>
 <div class="kwzahl"><span>F<sub>res</sub> = <b data-o="fres">100 N</b></span><span>a = <b data-o="a">2,0 m/s²</b></span><span>nach 4 s: <b data-o="v">8,0 m/s</b></span></div>
 <label>Kraft nach rechts: <b data-o="fr">200</b> N<input type="range" min="0" max="500" step="50" value="200" data-i="fr" aria-label="Kraft nach rechts in Newton"></label>
 <label>Kraft nach links: <b data-o="fl">100</b> N<input type="range" min="0" max="500" step="50" value="100" data-i="fl" aria-label="Kraft nach links in Newton"></label>
 <label>Masse von Wagen und Ladung: <b data-o="m">50</b> kg<input type="range" min="25" max="200" step="25" value="50" data-i="m" aria-label="Masse in Kilogramm"></label>
 <div class="simb"><button type="button" class="btn ghost" data-a="v0" aria-pressed="false">Wagen rollt schon (2 m/s)</button><button type="button" class="btn" data-a="los">Abspielen</button><button type="button" class="btn ghost" data-a="neu">Neu</button></div>
 <p class="simt" data-o="info"></p>
 <p class="simt">Vereinfachtes Modell: keine Reibung, kein Luftwiderstand. a = F<sub>res</sub> : m.</p>
</div>""",
 "gewicht": """<div class="sim" data-sim="gewicht">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Kraftmesser auf Erde, Mond und Mars</b></div>
 <div class="gwrap"><svg viewBox="0 0 120 230" class="gsvg" aria-hidden="true"></svg>
  <div class="gzahl"><p>Masse: <b data-o="m">20 kg</b> <span class="simt">(bleibt überall gleich)</span></p><p>Ortsfaktor: <b data-o="g">10 N/kg</b></p><p class="gfg">F<sub>G</sub> = <b data-o="fg">200 N</b></p><p class="simt" data-o="genau"></p></div></div>
 <label>Masse (z. B. Rucksack): <b data-o="mv">20</b> kg<input type="range" min="1" max="40" step="1" value="20" aria-label="Masse in Kilogramm"></label>
 <div class="simb"><button type="button" class="btn" data-ort="erde" aria-pressed="true">Erde</button><button type="button" class="btn ghost" data-ort="mond" aria-pressed="false">Mond</button><button type="button" class="btn ghost" data-ort="mars" aria-pressed="false">Mars</button></div>
 <p class="simt" data-o="info"></p>
 <p class="simt">Ortsfaktoren gerundet (NASA): Erde 9,8 – wir rechnen mit 10 N/kg –, Mond 1,6 N/kg, Mars 3,7 N/kg. Kraftmesser bis 400 N.</p>
</div>""",
 "auftrieb": """<div class="sim" data-sim="auftrieb">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Schwimmt die Dose?</b></div>
 <svg viewBox="0 0 320 210" class="abox" aria-hidden="true"></svg>
 <div class="kwzahl"><span>F<sub>G</sub> = <b data-o="fg">3,0 N</b></span><span>F<sub>A</sub> = <b data-o="fa">3,0 N</b></span><span class="phk" data-o="art">schwimmt</span></div>
 <label>Masse der Dose mit Sand: <b data-o="m">300</b> g<input type="range" min="50" max="800" step="10" value="300" aria-label="Masse in Gramm"></label>
 <div class="simb"><button type="button" class="btn" data-w="suess" aria-pressed="true">Süßwasser</button><button type="button" class="btn ghost" data-w="meer" aria-pressed="false">Meerwasser</button></div>
 <p class="simt" data-o="info"></p>
 <p class="simt">Modell: dichte Dose mit 500 cm³ Volumen, g = 10 N/kg. Süßwasser 1000 kg/m³, Meerwasser ca. 1025 kg/m³ (schwankt mit Salz und Temperatur).</p>
</div>""",
 "druck": """<div class="sim" data-sim="druck">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Einsinken im Schnee</b></div>
 <div class="phz"><span class="phw" data-o="p">33 300 Pa</span><span class="simt" data-o="kpa">= 33,3 kPa</span></div>
 <div class="dbars" data-o="bars"></div>
 <label>Du mit Ausrüstung: <b data-o="m">100</b> kg (F = <b data-o="f">1000</b> N)<input type="range" min="50" max="130" step="5" value="100" aria-label="Masse in Kilogramm"></label>
 <div class="simb"><button type="button" class="btn" data-f="stiefel" aria-pressed="true">Stiefel</button><button type="button" class="btn ghost" data-f="ski" aria-pressed="false">Ski</button><button type="button" class="btn ghost" data-f="schnee" aria-pressed="false">Schneeschuh</button></div>
 <p class="simt" data-o="info"></p>
 <p class="simt">Beim Gehen trägt ein Fuß die ganze Last. Flächen ungefähr (Modellwerte): Stiefelsohle 0,03 m², Ski 0,12 m², Schneeschuh 0,15 m². p = F : A, g = 10 N/kg.</p>
</div>""",
}

CSS = """
.sim { border: 2px solid #2E7D8C; border-radius: 12px; background: #fff; padding: 12px 14px; display: grid; gap: 8px; }
.simh { display: flex; gap: 8px; align-items: center; font-size: 18px; flex-wrap: wrap; }
.sim label { display: block; font-size: 17px; } .sim input[type=range] { display: block; width: 100%; min-height: 44px; margin: 2px 0 0; }
.simb { display: flex; gap: 8px; flex-wrap: wrap; } .simb .btn { min-height: 44px; }
.sim .btn { font: inherit; font-size: 16px; font-weight: 700; padding: 8px 14px; border-radius: 999px; border: 2px solid #2E7D8C; background: #2E7D8C; color: #fff; cursor: pointer; }
.sim .btn.ghost { background: #fff; color: #2E7D8C; }
.simt { margin: 0; font-size: 16px; color: #5E6652; }
.phz { display: flex; gap: 12px; align-items: baseline; flex-wrap: wrap; } .phw { font-size: 32px; font-weight: 700; color: #3B4A2F; font-variant-numeric: tabular-nums; }
.phk { font-size: 17px; font-weight: 700; border-radius: 999px; padding: 2px 12px; color: #fff; background: #7CB342; } .phk.sinkt { background: #C0392B; } .phk.schwebt { background: #2A5C8C; }
.kwbox, .abox { width: 100%; height: auto; background: #FBF7F2; border: 2px solid #1F2A1C; border-radius: 10px; }
.kwzahl { display: flex; gap: 14px; flex-wrap: wrap; font-size: 17px; align-items: center; } .kwzahl b { font-size: 20px; color: #3B4A2F; font-variant-numeric: tabular-nums; }
.gwrap { display: grid; grid-template-columns: 110px 1fr; gap: 12px; align-items: start; } .gsvg { width: 110px; height: auto; }
.gzahl p { margin: 0 0 6px; font-size: 17px; } .gzahl b { font-size: 20px; color: #3B4A2F; } .gzahl .gfg b { font-size: 28px; color: #B23A2E; }
.dbars { display: grid; gap: 6px; } .dbar { display: grid; grid-template-columns: 96px 1fr; gap: 8px; align-items: center; font-size: 15px; }
.dbar i { display: block; height: 18px; border-radius: 6px; background: #C9D3BC; min-width: 3px; transition: width .3s; } .dbar.an i { background: #2E7D8C; } .dbar.an { font-weight: 700; }
details.simd { border: 2px solid #2E7D8C; border-radius: 12px; background: #F3F8F9; margin: 10px 0; }
details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; font-size: 17px; min-height: 44px; padding: 10px 14px; }
details.simd > .sim { border: 0; margin: 0 4px 6px; }
.simlink { border: 2px solid #2E7D8C; border-radius: 12px; background: #F3F8F9; padding: 10px 14px; display: grid; gap: 6px; margin: 10px 0; }
.simlink .btn { justify-self: start; text-decoration: none; }
"""

JS = r"""<script>
window.SIMINIT = window.SIMINIT || {};
(function () {
  var NS = "http://www.w3.org/2000/svg";
  function f(x, d) { var s = (d == null ? String(x) : Number(x).toFixed(d)); return s.replace(".", ","); }
  function tsd(n) { return Math.round(n).toLocaleString("de-AT").replace(/\./g, " ").replace(/ /g, " "); }
  function q(box, k) { return box.querySelector('[data-o="' + k + '"]'); }
  function pfeil(x1, y1, x2, y2, farbe, breite) {
    if (Math.abs(x2 - x1) + Math.abs(y2 - y1) < 2) return "";
    var a = Math.atan2(y2 - y1, x2 - x1), h = 9;
    return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + farbe + '" stroke-width="' + (breite || 5) + '" stroke-linecap="round"/>' +
      '<path d="M' + x2 + ' ' + y2 + ' L' + (x2 - h * Math.cos(a - 0.5)) + ' ' + (y2 - h * Math.sin(a - 0.5)) + ' L' + (x2 - h * Math.cos(a + 0.5)) + ' ' + (y2 - h * Math.sin(a + 0.5)) + ' Z" fill="' + farbe + '"/>';
  }
  function knopf(box, attr, wert) { box.querySelectorAll("[" + attr + "]").forEach(function (b) { var an = b.getAttribute(attr) === wert; b.setAttribute("aria-pressed", String(an)); b.classList.toggle("ghost", !an); }); }

  SIMINIT.kraefte = function (box) {
    var svg = box.querySelector(".kwbox"), iR = box.querySelector('[data-i="fr"]'), iL = box.querySelector('[data-i="fl"]'), iM = box.querySelector('[data-i="m"]');
    var bV = box.querySelector('[data-a="v0"]'), v0 = 0, anim = null;
    function werte() { var fr = +iR.value, fl = +iL.value, m = +iM.value, fres = fr - fl; return { fr: fr, fl: fl, m: m, fres: fres, a: fres / m }; }
    function lage(w, t) { return v0 * t + 0.5 * w.a * t * t; }
    function skala(w) {
      var xs = [], t; for (t = 0; t <= 4.001; t += 0.5) xs.push(lage(w, t));
      var lo = Math.min.apply(null, xs.concat([0])), hi = Math.max.apply(null, xs.concat([0])), sp = Math.max(hi - lo, 1);
      return { xs: xs, px: function (x) { return 80 + (x - lo) / sp * 180; } };
    }
    function wagen(x, y, voll) {
      return '<g opacity="' + (voll ? 1 : 0.28) + '"><rect x="' + (x - 18) + '" y="' + (y - 16) + '" width="36" height="20" rx="4" fill="#6B7F4E" stroke="#1F2A1C" stroke-width="1.5"/>' +
        '<circle cx="' + (x - 10) + '" cy="' + (y + 7) + '" r="5" fill="#1F2A1C"/><circle cx="' + (x + 10) + '" cy="' + (y + 7) + '" r="5" fill="#1F2A1C"/></g>';
    }
    function zeichnen(tAnim) {
      var w = werte(), sk = skala(w), s = '<line x1="10" y1="104" x2="330" y2="104" stroke="#8A8F80" stroke-width="2"/>';
      var zuletzt = -99;
      sk.xs.forEach(function (x, i) { var px = sk.px(x); s += '<circle cx="' + px + '" cy="116" r="4" fill="#2E7D8C"/>';
        if (i % 2 === 0 && Math.abs(px - zuletzt) > 22) { s += '<text x="' + px + '" y="128" font-size="9" text-anchor="middle" fill="#5E6652">' + (i / 2) + ' s</text>'; zuletzt = px; } });
      var x0 = sk.px(tAnim == null ? 0 : lage(w, tAnim));
      s += wagen(x0, 88, true);
      var sc = 0.1;
      s += pfeil(x0 + 18, 80, x0 + 18 + w.fr * sc, 80, "#B23A2E");
      s += pfeil(x0 - 18, 80, x0 - 18 - w.fl * sc, 80, "#2A5C8C");
      if (w.fr) s += '<text x="' + (x0 + 22) + '" y="70" font-size="11" fill="#B23A2E">' + w.fr + ' N</text>';
      if (w.fl) s += '<text x="' + (x0 - 22) + '" y="70" font-size="11" text-anchor="end" fill="#2A5C8C">' + w.fl + ' N</text>';
      s += '<text x="10" y="18" font-size="12" fill="#1F2A1C">resultierende Kraft:</text>' + (w.fres ? pfeil(230, 14, 230 + w.fres * 0.16, 14, "#1F2A1C", 4) : '<text x="130" y="18" font-size="12" fill="#1F2A1C">0 N (Gleichgewicht)</text>');
      svg.innerHTML = s;
    }
    function zeig() {
      var w = werte(), v4 = v0 + w.a * 4, txt;
      q(box, "fr").textContent = w.fr; q(box, "fl").textContent = w.fl; q(box, "m").textContent = w.m;
      q(box, "fres").textContent = Math.abs(w.fres) + " N" + (w.fres > 0 ? " nach rechts" : w.fres < 0 ? " nach links" : "");
      q(box, "a").textContent = f(Math.abs(w.a), 2) + " m/s²";
      q(box, "v").textContent = f(Math.abs(v4), 1) + " m/s" + (v4 < -0.05 ? " nach links" : "") + " (" + f(Math.abs(v4) * 3.6, 1) + " km/h)";
      if (w.fres === 0 && v0 === 0) txt = "Die Kräfte gleichen sich aus – der Wagen bleibt stehen.";
      else if (w.fres === 0) txt = "Gleichgewicht, aber der Wagen rollt schon: Er rollt mit gleicher Geschwindigkeit weiter – die Punkte haben gleiche Abstände. Dafür braucht es KEINE resultierende Kraft.";
      else if (v0 > 0 && w.fres < 0) {
        var ts = v0 / -w.a;
        txt = "Die resultierende Kraft zeigt gegen die Bewegung: Der Wagen bremst – die Abstände werden kleiner." + (ts < 4 ? " Nach " + f(ts, 1) + " s steht er kurz still und rollt dann zurück (ohne Reibung)." : "");
      } else txt = "Die resultierende Kraft beschleunigt den Wagen: Die Abstände werden jede halbe Sekunde größer." + (w.m >= 150 ? " Bei großer Masse geht es langsamer – gleiche Kraft, kleinere Beschleunigung." : "");
      q(box, "info").textContent = txt;
      zeichnen(null);
    }
    function stop() { if (anim) cancelAnimationFrame(anim); anim = null; }
    box.addEventListener("input", function () { stop(); zeig(); });
    box.addEventListener("click", function (ev) {
      var b = ev.target.closest("[data-a]"); if (!b) return;
      if (b.dataset.a === "v0") { v0 = v0 ? 0 : 2; b.setAttribute("aria-pressed", String(!!v0)); b.classList.toggle("ghost", !v0); stop(); zeig(); return; }
      if (b.dataset.a === "neu") { iR.value = 200; iL.value = 100; iM.value = 50; v0 = 0; bV.setAttribute("aria-pressed", "false"); bV.classList.add("ghost"); stop(); zeig(); return; }
      stop(); var t0 = null;
      (function schritt(ts) { if (t0 === null) t0 = ts; var t = Math.min(4, (ts - t0) / 1000); zeichnen(t); if (t < 4) anim = requestAnimationFrame(schritt); else anim = null; })(performance.now());
    });
    zeig();
  };

  SIMINIT.gewicht = function (box) {
    var svg = box.querySelector(".gsvg"), inp = box.querySelector("input"), ort = "erde";
    var G = { erde: [10, "der Erde"], mond: [1.6, "dem Mond"], mars: [3.7, "dem Mars"] };
    function zeig() {
      var m = +inp.value, g = G[ort][0], fg = m * g, len = 30 + Math.min(fg, 400) / 400 * 130, s = "";
      s += '<rect x="45" y="4" width="30" height="10" rx="3" fill="#5E6652"/>';
      var zz = "M60 14 ", n = 10, h = len / n; for (var i = 0; i < n; i++) zz += "L" + (i % 2 ? 48 : 72) + " " + (14 + h * (i + 0.5)) + " ";
      zz += "L60 " + (14 + len);
      s += '<path d="' + zz + '" fill="none" stroke="#1F2A1C" stroke-width="2.5"/>';
      for (var k = 0; k <= 4; k++) { var y = 14 + 30 + k / 4 * 130; s += '<line x1="80" y1="' + y + '" x2="92" y2="' + y + '" stroke="#5E6652"/><text x="95" y="' + (y + 4) + '" font-size="10" fill="#5E6652">' + (k * 100) + '</text>'; }
      var yb = 14 + len;
      s += '<line x1="40" y1="' + yb + '" x2="80" y2="' + yb + '" stroke="#B23A2E" stroke-width="3"/>';
      s += '<rect x="36" y="' + (yb + 4) + '" width="48" height="' + (18 + m) + '" rx="7" fill="#6B7F4E" stroke="#1F2A1C" stroke-width="1.5"/>';
      svg.innerHTML = s;
      q(box, "m").textContent = m + " kg"; q(box, "mv").textContent = m;
      q(box, "g").textContent = f(g) + " N/kg"; q(box, "fg").textContent = f(Math.round(fg * 10) / 10) + " N";
      q(box, "genau").textContent = ort === "erde" ? "genauer mit 9,8 N/kg: " + f(Math.round(m * 9.8 * 10) / 10) + " N" : "";
      q(box, "info").textContent = ort === "erde" ? "Auf der Erde: " + m + " kg · 10 N/kg = " + tsd(fg) + " N."
        : "Auf " + G[ort][1] + " hat der Rucksack dieselbe Masse (" + m + " kg), aber nur etwa " + f(Math.round(fg)) + " N Gewichtskraft – " + (ort === "mond" ? "rund ein Sechstel" : "gut ein Drittel") + " der Erde.";
    }
    inp.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-ort]"); if (!b) return; ort = b.dataset.ort; knopf(box, "data-ort", ort); zeig(); });
    zeig();
  };

  SIMINIT.auftrieb = function (box) {
    var svg = box.querySelector(".abox"), inp = box.querySelector("input"), wasser = "suess";
    var RHO = { suess: 1000, meer: 1025 }, V = 500;          /* V in cm³ */
    function zeig() {
      var m = +inp.value, rho = RHO[wasser], mMax = rho / 1000 * V;  /* g, bei dem die Dose ganz eingetaucht im Gleichgewicht wäre */
      var fg = m / 1000 * 10, faMax = mMax / 1000 * 10, art, anteil, fa;
      if (Math.abs(m - mMax) < 5) { art = "schwebt"; anteil = 1; fa = fg; }
      else if (m < mMax) { art = "schwimmt"; anteil = m / mMax; fa = fg; }
      else { art = "sinkt"; anteil = 1; fa = faMax; }
      var wy = 70, hD = 70, wD = 50, xD = 135, yD;
      if (art === "sinkt") yD = 196 - hD; else if (art === "schwebt") yD = 110; else yD = wy - hD * (1 - anteil);
      var s = '<rect x="10" y="' + wy + '" width="300" height="130" fill="' + (wasser === "meer" ? "#9CC3D9" : "#BFDDEB") + '"/><line x1="10" y1="' + wy + '" x2="310" y2="' + wy + '" stroke="#2A5C8C" stroke-width="2"/>';
      s += '<rect x="10" y="196" width="300" height="6" fill="#C9B48A"/>';
      s += '<rect x="' + xD + '" y="' + yD + '" width="' + wD + '" height="' + hD + '" rx="6" fill="#B9B9B0" stroke="#1F2A1C" stroke-width="2"/>';
      var sandH = Math.min(hD - 6, (m / 800) * (hD - 6));
      s += '<rect x="' + (xD + 3) + '" y="' + (yD + hD - 3 - sandH) + '" width="' + (wD - 6) + '" height="' + sandH + '" rx="3" fill="#D9C48F"/>';
      var cx = xD + wD / 2, cy = yD + hD / 2, sc = 9;
      s += pfeil(cx - 9, cy, cx - 9, cy + fg * sc, "#B23A2E") + '<text x="' + (cx - 14) + '" y="' + Math.min(205, cy + fg * sc + 2) + '" font-size="11" text-anchor="end" fill="#B23A2E">F<tspan font-size="8" dy="2">G</tspan></text>';
      s += pfeil(cx + 9, cy, cx + 9, cy - fa * sc, "#2A5C8C") + '<text x="' + (cx + 14) + '" y="' + Math.max(12, cy - fa * sc + 4) + '" font-size="11" fill="#2A5C8C">F<tspan font-size="8" dy="2">A</tspan></text>';
      svg.innerHTML = s;
      q(box, "m").textContent = m; q(box, "fg").textContent = f(fg, 1) + " N"; q(box, "fa").textContent = f(fa, 1) + " N";
      q(box, "art").textContent = art; q(box, "art").className = "phk " + (art === "schwimmt" ? "" : art);
      q(box, "info").textContent = art === "schwimmt" ? "Die Dose schwimmt und taucht zu " + Math.round(anteil * 100) + " % ein. Ruhiges Schwimmen: Auftriebskraft = Gewichtskraft."
        : art === "schwebt" ? "Ganz eingetaucht und im Gleichgewicht: Die Dose schwebt. Auftriebskraft = Gewichtskraft."
        : "Ganz eingetaucht ist die Auftriebskraft höchstens " + f(faMax, 2) + " N – kleiner als die Gewichtskraft. Die Dose sinkt. Auftrieb gibt es trotzdem!";
    }
    inp.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-w]"); if (!b) return; wasser = b.dataset.w; knopf(box, "data-w", wasser); zeig(); });
    zeig();
  };

  SIMINIT.druck = function (box) {
    var inp = box.querySelector("input"), fuss = "stiefel";
    var A = { stiefel: [0.03, "Stiefel"], ski: [0.12, "Ski"], schnee: [0.15, "Schneeschuh"] };
    function zeig() {
      var m = +inp.value, F = m * 10, p = F / A[fuss][0], pMax = F / 0.03;
      q(box, "m").textContent = m; q(box, "f").textContent = tsd(F);
      q(box, "p").textContent = tsd(p) + " Pa"; q(box, "kpa").textContent = "= " + f(p / 1000, 1) + " kPa";
      var bars = "";
      ["stiefel", "ski", "schnee"].forEach(function (k) { var pk = F / A[k][0]; bars += '<div class="dbar' + (k === fuss ? " an" : "") + '"><span>' + A[k][1] + '</span><i style="width:' + Math.max(1, pk / pMax * 100) + '%"></i></div>'; });
      q(box, "bars").innerHTML = bars;
      var fak = (F / A.stiefel[0]) / p;
      q(box, "info").textContent = fuss === "stiefel" ? "Mit dem Stiefel drückt deine ganze Gewichtskraft auf 0,03 m² – großer Druck, du sinkst im weichen Schnee tief ein."
        : "Gleiche Kraft, " + f(Math.round(fak * 10) / 10) + "-mal so große Fläche: Der Druck ist " + f(Math.round(fak * 10) / 10) + "-mal kleiner als mit dem Stiefel. Wie tief du einsinkst, hängt auch vom Schnee ab.";
    }
    inp.addEventListener("input", zeig);
    box.addEventListener("click", function (ev) { var b = ev.target.closest("[data-f]"); if (!b) return; fuss = b.dataset.f; knopf(box, "data-f", fuss); zeig(); });
    zeig();
  };

  function start() { document.querySelectorAll(".sim[data-sim]").forEach(function (b) { if (!b.dataset.go && SIMINIT[b.dataset.sim]) { b.dataset.go = "1"; SIMINIT[b.dataset.sim](b); } }); }
  window.simStart = start;
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
</script>"""


def extern_html(key, md, esc):
    """Externe Simulation als Link-Karte (Theorie-Seite)."""
    p = PHET[key]
    return (f'<div class="simlink"><div class="simh"><span class="tkn">Simulation</span><b>{esc(p["titel"])}</b></div><p class="simt">{md(p["text"])}</p>'
            f'<a class="btn" href="{esc(p["url"])}" target="_blank" rel="noopener">Simulation öffnen</a><p class="simt">{esc(LIZENZ)}</p></div>')

# Gruppenkarten im Arbeitsblatt (Aufgabe 3): eigene Simulationen und PhET-Links je Gruppe (Gruppe 5 Kapillarwirkung, 7 Gegenkraft: nichts Passendes geprüft)
GRUPPE_SIM = {1: ["kraefte"], 2: ["gewicht"], 3: ["auftrieb"], 6: ["druck"]}
GRUPPE_PHET = {1: ["fmb"], 2: ["federn"], 3: ["auftrieb"], 4: ["fmb_reibung"], 6: ["druck"]}
