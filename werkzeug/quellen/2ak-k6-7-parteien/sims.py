"""Interaktive Simulationen für PBGW 2AK K6–7 Wahlrecht und Parteien (Kadetten stellen selbst ein, sehen sofort die Wirkung).
Jede Simulation: HTML ohne IDs (mehrfach einsetzbar) + Startfunktion in JS (window.SIMINIT[name](box)).
Fachliche Grundlagen (Stand 20.11.2026), vereinfachtes Modell:
- Zeitmaschine: Buch S. 23–26 (1861 Kurien, Männer ab 24 mit Besitz; Großgrundbesitzerinnen nur über Bevollmächtigte; 1873 Zensus 10 Gulden,
  1882 auf 5 Gulden gesenkt; 1896 5. Kurie; 1907 alle Männer ab 24, Frauen verlieren das Großgrundbesitz-Wahlrecht; 1918 alle);
  Wahlalter 1919 = 20 (politik-lexikon.at); 1933–1945 keine freien Wahlen; vor 1949 laut Buch 21; 1949 20, 1968 19, 1992 18, 2007 16 (Buch, Parlament PK 361).
  Zwischen 1920 und 1932 genaues Wahlalter nicht geprüft – die Simulation zeigt 20 und sagt das dazu.
- Mehrheit: Mandate Wahl 2024 (BMI): FPÖ 57, ÖVP 51, SPÖ 41, NEOS 18, Grüne 16 = 183; Klubstand Herbst 2026: NEOS 17, 1 ohne Klub (Parlament 29.10.2026)."""

TITEL = {"zeitmaschine": "Wahlrecht-Zeitmaschine", "mehrheit": "Mehrheits-Rechner"}
ZEILE = {"zeitmaschine": "Stell Jahr, Person und Geldbeutel ein – hättest du wählen dürfen?",
         "mehrheit": "Tipp Parteien an – reicht es für eine Mehrheit im Nationalrat?"}

HTML = {
 "zeitmaschine": """<div class="sim" data-sim="zeitmaschine">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Wahlrecht-Zeitmaschine</b></div>
 <label>Jahr: <b data-o="jahr">1861</b><input type="range" min="1861" max="2026" step="1" value="1861" data-i="jahr" aria-label="Jahr"></label>
 <div class="zmrow" role="group" aria-label="Person"><span>Person:</span>
  <button type="button" class="btn ghost" data-p="mann" aria-pressed="true">Mann</button><button type="button" class="btn ghost" data-p="frau" aria-pressed="false">Frau</button></div>
 <label>Alter: <b data-o="alter">17</b> Jahre<input type="range" min="15" max="40" step="1" value="17" data-i="alter" aria-label="Alter"></label>
 <div class="zmrow" role="group" aria-label="Geldbeutel"><span>Geldbeutel:</span>
  <button type="button" class="btn ghost" data-g="reich" aria-pressed="false">Großgrundbesitz</button><button type="button" class="btn ghost" data-g="mittel" aria-pressed="false">Handwerker, zahlt etwas Steuer</button><button type="button" class="btn ghost" data-g="arm" aria-pressed="true">Arbeiter ohne Besitz</button></div>
 <div class="zmerg"><span class="zmamp" data-o="amp">✗</span><div><b data-o="kurz">Nein</b><p class="simt" data-o="warum"></p></div></div>
 <p class="simt">Vereinfachtes Modell nach Buch S. 23–26. Für dich heute: <b>ab 16</b>.</p>
</div>""",
 "mehrheit": """<div class="sim" data-sim="mehrheit">
 <div class="simh"><span class="tkn">Ausprobieren</span><b>Mehrheits-Rechner</b></div>
 <div class="zmrow" role="group" aria-label="Stand"><span>Stand:</span>
  <button type="button" class="btn ghost" data-s="wahl" aria-pressed="true">Wahl 2024</button><button type="button" class="btn ghost" data-s="klub" aria-pressed="false">Klubs Herbst 2026</button></div>
 <div class="mhp" data-o="parteien"></div>
 <div class="mhbar" aria-hidden="true"><span data-o="balken"></span><i></i></div>
 <div class="mhzahl"><b data-o="summe">0</b> von 183 Mandaten · Mehrheit ab <b>92</b> · Zweidrittel ab <b>122</b></div>
 <p class="simt" data-o="text">Tipp Parteien an.</p>
</div>""",
}

CSS = """
.sim { border: 2px solid #2E7D8C; border-radius: 12px; background: #fff; padding: 12px 14px; display: grid; gap: 10px; }
.simh { display: flex; gap: 8px; align-items: center; font-size: 18px; flex-wrap: wrap; }
.sim label { display: grid; gap: 4px; font-size: 17px; } .sim input[type=range] { width: 100%; min-height: 44px; }
.sim .btn { font: inherit; font-size: 16px; font-weight: 700; padding: 8px 14px; min-height: 44px; border-radius: 999px; border: 2px solid #2E7D8C; background: #2E7D8C; color: #fff; cursor: pointer; }
.sim .btn.ghost { background: #fff; color: #2E7D8C; }
.sim .btn.ghost[aria-pressed="true"] { background: #2E7D8C; color: #fff; }
.simt { margin: 0; font-size: 16px; color: #5E6652; }
.zmrow { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; font-size: 17px; }
.zmerg { display: grid; grid-template-columns: 64px 1fr; gap: 12px; align-items: center; background: #F3F5EE; border-radius: 12px; padding: 10px; }
.zmerg b { font-size: 22px; color: #3B4A2F; }
.zmamp { width: 64px; height: 64px; border-radius: 50%; display: grid; place-items: center; font-size: 36px; font-weight: 800; color: #fff; background: #8C3B2E; }
.zmamp.ja { background: #4E7D23; } .zmamp.halb { background: #C98A12; } .zmamp.keine { background: #5E6652; }
.mhp { display: flex; gap: 8px; flex-wrap: wrap; }
.mhp .btn { border-color: var(--pc); color: var(--pc); background: #fff; }
.mhp .btn[aria-pressed="true"] { background: var(--pc); color: #fff; }
.mhbar { position: relative; height: 26px; border-radius: 8px; background: #E4E7DD; overflow: hidden; }
.mhbar span { display: block; height: 100%; width: 0; background: #7FA83A; transition: width .3s; }
.mhbar span.nein { background: #B9A27A; }
.mhbar i { position: absolute; top: 0; bottom: 0; left: 50.27%; width: 3px; background: #1F2A1C; }
.mhzahl { font-size: 18px; } .mhzahl b { font-size: 22px; color: #3B4A2F; }
details.simd { border: 2px solid #2E7D8C; border-radius: 12px; background: #F3F8F9; margin: 10px 0; }
details.simd > summary { cursor: pointer; font-weight: 700; color: #2E7D8C; font-size: 17px; min-height: 44px; padding: 10px 14px; }
details.simd > .sim { border: 0; margin: 0 4px 6px; }
"""

JS = r"""<script>
window.SIMINIT = window.SIMINIT || {};
(function () {
  function q(box, k) { return box.querySelector('[data-o="' + k + '"]'); }
  function waehle(gruppe, attr, wert) { gruppe.forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute(attr) === wert)); }); }

  /* Regeln: [ergebnis, kurz, warum]; ergebnis: ja | halb | nein | keine */
  function regel(j, p, a, g) {
    if (j >= 1933 && j <= 1945) return ["keine", "Niemand", j <= 1938 ? "Diktatur in Österreich: Das Parlament war ausgeschaltet, es gab keine freien Wahlen." : "NS-Herrschaft: Österreich gehörte zum Deutschen Reich, es gab keine freien Wahlen."];
    if (j < 1919) {
      if (a < 24) return ["nein", "Nein", "Zu jung: Bis 1918 durften nur Männer ab 24 wählen."];
      if (p === "frau") {
        if (j < 1907 && g === "reich") return ["halb", "Nur über einen Mann", "Frauen mit Großgrundbesitz durften ihre Stimme nur durch einen Bevollmächtigten abgeben lassen – meist einen Mann."];
        return ["nein", "Nein", j >= 1907 ? "1907 bekamen alle Männer das Wahlrecht – Frauen nicht. Sogar die Großgrundbesitzerinnen verloren es." : "Frauen waren grundsätzlich ausgeschlossen."];
      }
      if (j >= 1907) return ["ja", "Ja – und deine Stimme zählt gleich viel", "Seit 1907: allgemeines, gleiches, direktes und geheimes Wahlrecht für Männer ab 24."];
      if (g === "reich") return ["ja", "Ja – und deine Stimme zählt viel", "Großgrundbesitzer hatten eine eigene Kurie: Wenige Tausend Wähler bestimmten viele Abgeordnete."];
      if (g === "mittel") {
        if (j < 1873) return ["halb", "Vielleicht", "Kurienwahlrecht: Es kam auf Besitz und Steuer in deiner Kurie an – viele Handwerker waren dabei, viele nicht."];
        if (j < 1882) return ["nein", "Nein", "Zensuswahlrecht: In Wien brauchte man mindestens 10 Gulden Steuer pro Jahr – nur etwa 6 % der Männer schafften das."];
        return ["ja", "Ja", "Ab 1882 reichten 5 Gulden Steuer – damit durften auch kleinere Handwerker wählen."];
      }
      if (j >= 1896) return ["halb", "Ja – aber deine Stimme zählt wenig", "Seit 1896 gibt es die 5. Kurie für alle Männer ab 24. Aber: 5,3 Millionen Wähler bestimmten nur 72 Abgeordnete."];
      return ["nein", "Nein", "Wer keinen Besitz hatte und keine Steuer zahlte, durfte nicht wählen."];
    }
    var min = j < 1933 ? 20 : j < 1949 ? 21 : j < 1968 ? 20 : j < 1992 ? 19 : j < 2007 ? 18 : 16;
    var hinweis = j < 1933 ? " (So galt es 1919. Das Buch nennt 21 – in den Jahren danach wurde das Wahlalter angehoben; das genaue Jahr ist hier nicht geprüft.)" : j < 1949 ? " (laut Buch; ehemalige NSDAP-Mitglieder waren 1945 großteils ausgeschlossen)" : "";
    if (a < min) return ["nein", "Noch nicht", "Wahlalter " + j + ": ab " + min + "." + hinweis];
    return ["ja", "Ja", (j >= 2007 ? "Seit 2007 wählt man ab 16 – Frauen und Männer gleich." : "Allgemeines, gleiches Wahlrecht für Frauen und Männer ab " + min + ".") + hinweis];
  }

  SIMINIT.zeitmaschine = function (box) {
    var J = box.querySelector('[data-i="jahr"]'), A = box.querySelector('[data-i="alter"]');
    var P = box.querySelectorAll("[data-p]"), G = box.querySelectorAll("[data-g]"), p = "mann", g = "arm";
    function zeig() {
      var j = +J.value, a = +A.value; q(box, "jahr").textContent = j; q(box, "alter").textContent = a;
      var r = regel(j, p, a, g), amp = q(box, "amp");
      amp.className = "zmamp " + r[0]; amp.textContent = r[0] === "ja" ? "✓" : r[0] === "halb" ? "~" : r[0] === "keine" ? "–" : "✗";
      q(box, "kurz").textContent = r[1]; q(box, "warum").textContent = r[2];
    }
    P.forEach(function (b) { b.addEventListener("click", function () { p = b.getAttribute("data-p"); waehle(P, "data-p", p); zeig(); }); });
    G.forEach(function (b) { b.addEventListener("click", function () { g = b.getAttribute("data-g"); waehle(G, "data-g", g); zeig(); }); });
    J.addEventListener("input", zeig); A.addEventListener("input", zeig); zeig();
  };

  SIMINIT.mehrheit = function (box) {
    var D = {wahl: [["FPÖ", 57, "#2A5C9C"], ["ÖVP", 51, "#1B8A8C"], ["SPÖ", 41, "#C0392B"], ["NEOS", 18, "#B5307A"], ["Grüne", 16, "#4E8A2A"]],
             klub: [["FPÖ", 57, "#2A5C9C"], ["ÖVP", 51, "#1B8A8C"], ["SPÖ", 41, "#C0392B"], ["NEOS", 17, "#B5307A"], ["Grüne", 16, "#4E8A2A"], ["ohne Klub", 1, "#6B6B6B"]]};
    var stand = "wahl", an = {}, S = box.querySelectorAll("[data-s]"), wrap = q(box, "parteien");
    function baue() {
      wrap.textContent = "";
      D[stand].forEach(function (x) {
        var b = document.createElement("button"); b.type = "button"; b.className = "btn"; b.style.setProperty("--pc", x[2]);
        b.textContent = x[0] + " " + x[1]; b.setAttribute("aria-pressed", String(!!an[x[0]]));
        b.addEventListener("click", function () { an[x[0]] = !an[x[0]]; b.setAttribute("aria-pressed", String(!!an[x[0]])); zeig(); });
        wrap.appendChild(b);
      });
      zeig();
    }
    function zeig() {
      var sum = 0, namen = [];
      D[stand].forEach(function (x) { if (an[x[0]]) { sum += x[1]; namen.push(x[0]); } });
      q(box, "summe").textContent = sum;
      var bal = q(box, "balken"); bal.style.width = (sum / 183 * 100).toFixed(1) + "%"; bal.className = sum >= 92 ? "" : "nein";
      q(box, "text").textContent = !namen.length ? "Tipp Parteien an." :
        namen.join(" + ") + " = " + sum + (sum >= 122 ? ": Zweidrittelmehrheit – damit ließe sich sogar die Verfassung ändern (wenn alle da sind)." :
        sum >= 92 ? ": Mehrheit! Alle anderen haben zusammen " + (183 - sum) + (sum === 92 ? " – sehr knapp, eine einzige Stimme macht den Unterschied." : ".") : ": keine Mehrheit – es fehlen " + (92 - sum) + ".");
    }
    S.forEach(function (b) { b.addEventListener("click", function () { stand = b.getAttribute("data-s"); waehle(S, "data-s", stand); baue(); }); });
    baue();
  };

  window.simStart = function () {
    document.querySelectorAll(".sim[data-sim]").forEach(function (box) {
      if (box.dataset.go) return; var f = SIMINIT[box.dataset.sim]; if (!f) return; box.dataset.go = "1"; f(box);
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", window.simStart); else window.simStart();
})();
</script>"""
