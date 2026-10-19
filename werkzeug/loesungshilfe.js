/* Lösungshilfe für die Handy-Arbeitsblätter (aufgaben.html mit »Prüfen«).
   Ziel: Kadetten bleiben beim Üben nicht frustriert stecken – und die Lösung bleibt trotzdem sichtbar im PDF.
   1) Fehlversuch 1: nur »Noch nicht ganz« + Hinweis, was fehlt.  Fehlversuch 2: zusätzlich der Tipp mit Link zur Lernseite.
      Ab Fehlversuch 3: Knopf »Lösung zeigen« bei GENAU dieser Aufgabe.
   2) Wer die Lösung zeigen lässt, bekommt im PDF den Status »Lösung angesehen« – auch wenn danach die richtige Antwort drinsteht.
   3) Rechenaufgaben: Nach Lösung oder richtiger Antwort gibt es eine Übungsvariante mit neuen Zahlen (LH_VARIANTEN).
   Einbau: python3 werkzeug/loesungshilfe_einbauen.py (setzt diese Datei inline ein und passt die PDF-Zeile »Bewertung« an). */
(function () {
  if (window.__loesungshilfe) return; window.__loesungshilfe = true;
  var FEHLER_FUER_TIPP = 2, FEHLER_FUER_LOESUNG = 3;

  S.tries = S.tries || {};      // Fehlversuche je Aufgabe (nur Klicks auf »Prüfen«)
  S.solTask = S.solTask || {};  // Aufgaben, bei denen die Lösung gezeigt wurde: id -> Zahl der Fehlversuche zu dem Zeitpunkt

  var css = ".lh-btn{margin-top:6px;min-height:44px;border-radius:10px;border:2px solid #2E7D8C;background:#fff;color:#1F5F6B;font-weight:700;font-size:16px;font-family:inherit;padding:8px 12px;cursor:pointer}" +
    ".lh-note{margin-top:8px;border-radius:10px;padding:8px 12px;background:#FBF2D6;border:2px solid #C9A227;font-size:15px}" +
    ".lh-var{margin-top:10px;border:2px dashed #7FA83A;border-radius:10px;padding:10px 12px;background:#F6FAEC}" +
    ".lh-var h4{margin:0 0 6px;font-size:16px;color:#3B4A2F}.lh-var label{display:block;font-weight:600;margin-top:8px}" +
    ".lh-var input{width:100%;box-sizing:border-box;min-height:44px;padding:8px;border:2px solid #C9A227;border-radius:8px;background:#FFF7D6;font:inherit}" +
    ".lh-var .fb{margin-top:8px}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  function taskOf(id) { return T.filter(function (t) { return t.id === id; })[0]; }
  function mk(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }

  // ---------- Status einer Aufgabe (für PDF) ----------
  window.LH_viewed = function (t) { return S.solTask && S.solTask[t.id] !== undefined; };
  window.LH_pdf = function (t, base) {
    if (!t.chk) return base;
    var n = (S.tries && S.tries[t.id]) || 0;
    if (LH_viewed(t)) return "Lösung angesehen (nach " + S.solTask[t.id] + " Fehlversuch" + (S.solTask[t.id] === 1 ? "" : "en") + ") – Antwort bitte selbst bewerten";
    var ev = evalTask(t);
    if (ev && ev.ok) return n === 0 ? base + " · selbst gelöst (1. Versuch)" : base + " · gelöst nach " + n + " Fehlversuch" + (n === 1 ? "" : "en") + (n >= FEHLER_FUER_TIPP ? " (mit Tipp)" : "");
    return base + (n ? " · " + n + " Fehlversuch" + (n === 1 ? "" : "e") : "");
  };

  // ---------- »Prüfen« erweitern ----------
  var origCheck = showCheck;
  showCheck = function (t) {
    var r = evalTask(t);
    if (r && !r.ok && !LH_viewed(t)) S.tries[t.id] = (S.tries[t.id] || 0) + 1;
    origCheck(t);
    var fb = $("#fb_" + t.id), n = S.tries[t.id] || 0;
    if (r && !r.ok) {
      // Tipp mit Link erst ab dem 2. Fehlversuch
      if (n < FEHLER_FUER_TIPP) { var links = fb.querySelectorAll("a"); links.forEach(function (a) { if (a.parentNode) a.parentNode.remove(); }); fb.append(mk("div", "", "Lies deine Antwort noch einmal genau – manchmal fehlt nur ein Wort, eine Einheit oder ein Rechenschritt.")); }
      if (n >= FEHLER_FUER_LOESUNG && !LH_viewed(t)) {
        var b = mk("button", "lh-btn", "Ich komme nicht weiter – Lösung zeigen");
        b.type = "button";
        b.addEventListener("click", function () { zeigeLoesung(t, fb); });
        fb.append(b, mk("div", "", "Die Aufgabe steht dann im PDF als »Lösung angesehen«."));
      }
    }
    if (r && r.ok) angebotVariante(t);
    save();
  };

  function zeigeLoesung(t, fb) {
    S.solTask[t.id] = S.tries[t.id] || 0;
    var sol = $("#sol_" + t.id); if (sol) sol.hidden = false;
    var card = $("#card_" + t.id);
    if (card && !card.querySelector(".lh-note")) card.append(mk("div", "lh-note", "Lösung angesehen – das steht so im PDF. Mach unten die Übungsvariante, dann weißt du, ob du es jetzt kannst."));
    fb.querySelectorAll(".lh-btn").forEach(function (b) { b.remove(); });
    angebotVariante(t);
    save();
  }

  // Einzelne gezeigte Lösungen dürfen vom globalen »Lösungen ansehen« nicht wieder versteckt werden
  var origSol = showSolutions;
  showSolutions = function () {
    origSol();
    T.forEach(function (t) { if (LH_viewed(t)) { var x = $("#sol_" + t.id); if (x) x.hidden = false; } });
  };

  // ---------- Übungsvariante mit neuen Zahlen ----------
  // LH_VARIANTEN (je Seite): [{ id:"a3", vars:[{n:"N",min:200,max:1000,step:50}], abgeleitet:{lcm:"l*100"},
  //   text:"… {N} Windungen …", felder:[{label:"Durchflutung Θ", expr:"N*I", einheit:"A"}] }]
  function zufall(v) { var k = Math.round((v.max - v.min) / v.step); var x = v.min + v.step * Math.floor(Math.random() * (k + 1)); return Math.round(x * 1e6) / 1e6; }
  function fmt(x) { return String(Math.round(x * 1e6) / 1e6).replace(".", ","); }
  function auswerten(expr, vals) { var names = Object.keys(vals); return new Function(names.join(","), "return (" + expr + ");").apply(null, names.map(function (k) { return vals[k]; })); }

  function angebotVariante(t) {
    var cfg = (window.LH_VARIANTEN || []).filter(function (c) { return c.id === t.id; })[0];
    var card = $("#card_" + t.id);
    if (!cfg || !card || card.querySelector(".lh-var")) return;
    var box = mk("div", "lh-var");
    var b = mk("button", "lh-btn", "Noch eine Übung mit anderen Zahlen"); b.type = "button";
    box.append(b); card.append(box);
    function neu() {
      box.textContent = "";
      var vals = {}; cfg.vars.forEach(function (v) { vals[v.n] = zufall(v); });
      var shown = Object.assign({}, vals);
      Object.keys(cfg.abgeleitet || {}).forEach(function (k) { shown[k] = auswerten(cfg.abgeleitet[k], vals); });
      var text = cfg.text.replace(/\{(\w+)\}/g, function (_, k) { return fmt(shown[k]); });
      box.append(mk("h4", "", "Übungsvariante – zählt nicht für die Abgabe"), mk("div", "", text));
      var inputs = cfg.felder.map(function (f) {
        var l = mk("label", "", f.label), i = document.createElement("input"); i.type = "text"; i.placeholder = "Hier tippen …"; i.inputMode = "decimal";
        l.append(i); box.append(l); return i;
      });
      var out = mk("div", "fb", ""); out.hidden = true;
      var pr = mk("button", "lh-btn", "Prüfen"); pr.type = "button";
      var nx = mk("button", "lh-btn", "Neue Zahlen"); nx.type = "button"; nx.style.marginLeft = "8px";
      pr.addEventListener("click", function () {
        var alleOk = true, msgs = [];
        cfg.felder.forEach(function (f, k) {
          var soll = auswerten(f.expr, vals), p = parseNum(inputs[k].value);
          var gut = p && !isNaN(p.v) && Math.abs(p.v - soll) <= Math.abs(soll) * 0.02;
          var unitOk = !f.einheit || (p && normU(p.u) === normU(f.einheit));
          if (!gut) { alleOk = false; msgs.push(f.label + ": stimmt noch nicht."); }
          else if (!unitOk) { alleOk = false; msgs.push(f.label + ": Zahl stimmt – Einheit prüfen."); }
        });
        out.hidden = false; out.className = "fb " + (alleOk ? "ok" : "no"); out.textContent = "";
        out.append(mk("strong", "", alleOk ? "Richtig – das kannst du!" : "Noch nicht ganz."));
        msgs.forEach(function (m) { out.append(mk("div", "", m)); });
        if (!alleOk && t.tip) { var d = mk("div", ""); d.append("Tipp: Lies nochmal "); var a = mk("a", "", t.tip[0]); a.href = t.tip[1]; d.append(a, "."); out.append(d); }
      });
      nx.addEventListener("click", neu);
      box.append(pr, nx, out);
    }
    b.addEventListener("click", neu);
  }

  // ---------- Beim Laden wiederherstellen ----------
  function wiederherstellen() {
    T.forEach(function (t) {
      if (LH_viewed(t)) {
        var sol = $("#sol_" + t.id); if (sol) sol.hidden = false;
        var card = $("#card_" + t.id);
        if (card && !card.querySelector(".lh-note")) card.append(mk("div", "lh-note", "Lösung angesehen – das steht so im PDF."));
        angebotVariante(t);
      }
    });
  }
  wiederherstellen();
})();
