/* Tipp-Stufen, Theorie-Karte und »Was glaubst du?« für Handy-Arbeitsblätter (Stephan, 07.11.2026: Aufgabe zuerst, Theorie dazu).
   Nur aktiv bei Aufgaben mit Feld tipp1 / karte (T im Seitencode). Zustand nur zusätzlich in S.tipps (S.a und KEY bleiben unverändert).
   Tipp 1 = Denkanstoß · Tipp 2 = Theorie-Karte (aus derselben Datenquelle wie Theorie-Seite) · Tipp 3 = Leseauftrag im Buch.
   Fehlversuch 2 öffnet Tipp 2 automatisch. Im PDF steht pro Aufgabe »Hilfe: Tipp 1, 2« bzw. »ohne Tipp«. Tipps kosten keine Punkte.
   Einbau: python3 werkzeug/tippstufen_einbauen.py (idempotent, über nach_dem_bauen.py). Design nur funktional – an das bestehende Design angelehnt. */
(function () {
  if (window.__tippstufen) return; window.__tippstufen = true;
  S.tipps = S.tipps || {};
  var css = ".tp{margin-top:10px;display:grid;gap:8px}.tp-row{display:flex;gap:8px;flex-wrap:wrap}" +
    ".tp-b{min-height:44px;border-radius:10px;border:2px solid #7FA83A;background:#fff;color:#3B4A2F;font-weight:700;font-size:16px;font-family:inherit;padding:8px 12px;cursor:pointer}" +
    ".tp-b[aria-expanded=true]{background:#E6F0D3}.tp-b.used{border-color:#3B4A2F}" +
    ".tp-p{border:2px solid #D3DCC2;border-radius:12px;padding:10px 12px;background:#F7FAF0;font-size:18px;line-height:1.45}.tp-p p{margin:0 0 8px}" +
    ".tp-p img{width:100%;height:auto;border-radius:8px;border:1px solid #D3DCC2;background:#fff;cursor:zoom-in}.tp-p a{font-weight:700;color:#1F5F6B}" +
    ".tp-big{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:99;display:flex;align-items:center;justify-content:center;padding:10px}.tp-big img{max-width:100%;max-height:100%;background:#fff;border-radius:8px}" +
    ".wg-end{border:2px solid #2E7D8C;border-radius:14px;padding:12px 14px;background:#E8F1F3;font-size:17px;margin-top:14px}.wg-end h3{margin:0 0 6px;font-size:18px}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  function mk(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  function rich(el, s) { String(s).split("**").forEach(function (p, i) { if (i % 2) { var b = document.createElement("strong"); b.textContent = p; el.appendChild(b); } else el.appendChild(document.createTextNode(p)); }); return el; }
  function opened(id) { return S.tipps[id] || (S.tipps[id] = []); }
  function mark(id, n) { var a = opened(id); if (a.indexOf(n) < 0) { a.push(n); a.sort(); try { save(); } catch (e) {} } }
  function karteEl(k) {
    var d = mk("div");
    (k.text || []).forEach(function (s) { d.appendChild(rich(mk("p"), s)); });
    if (k.bild) { var im = mk("img"); im.src = k.bild[0]; im.alt = k.bild[1]; im.addEventListener("click", function () {
      var o = mk("div", "tp-big"), i2 = mk("img"); i2.src = k.bild[0]; i2.alt = k.bild[1]; o.appendChild(i2); o.addEventListener("click", function () { o.remove(); }); document.body.appendChild(o); }); d.appendChild(im); }
    var p = mk("p"); var a = mk("a", "", "Mehr in der Theorie, " + k.teil); a.href = k.link; p.appendChild(a); p.appendChild(document.createTextNode(" · " + k.buch)); d.appendChild(p);
    return d;
  }
  var panels = {};
  function build(t) {
    var card = document.getElementById("card_" + t.id); if (!card) return;
    var box = mk("div", "tp"), row = mk("div", "tp-row"), pp = {};
    var defs = [[1, "Tipp 1 · Denkanstoß"], [2, "Tipp 2 · Theorie-Karte"], [3, "Tipp 3 · Im Buch lesen"]];
    defs.forEach(function (d) {
      var n = d[0]; if (n === 1 && !t.tipp1) return; if (n === 2 && !t.karteD) return; if (n === 3 && !t.tipp3) return;
      var b = mk("button", "tp-b", d[1]); b.type = "button"; b.setAttribute("aria-expanded", "false");
      var p = mk("div", "tp-p"); p.hidden = true;
      if (n === 1) p.appendChild(rich(mk("p"), t.tipp1)); if (n === 3) p.appendChild(rich(mk("p"), t.tipp3)); if (n === 2) p.appendChild(karteEl(t.karteD));
      b.addEventListener("click", function () { var open = p.hidden; p.hidden = !open; b.setAttribute("aria-expanded", String(open)); if (open) { mark(t.id, n); b.classList.add("used"); } });
      if ((S.tipps[t.id] || []).indexOf(n) >= 0) b.classList.add("used");
      pp[n] = [b, p]; row.appendChild(b);
    });
    box.appendChild(mk("div", "lbl", "Hilfe auf Abruf (kostet keine Punkte)")); box.appendChild(row);
    Object.keys(pp).forEach(function (n) { box.appendChild(pp[n][1]); });
    var cr = card.querySelector(".checkrow"); if (cr) card.insertBefore(box, cr); else card.appendChild(box);
    panels[t.id] = pp;
  }
  function open2(t) { var pp = panels[t.id]; if (pp && pp[2] && pp[2][1].hidden) pp[2][0].click(); }
  T.forEach(function (t) { if (t.tipp1 || t.karteD) build(t); });
  var oc = showCheck;
  showCheck = function (t) { oc(t); if ((S.tries && S.tries[t.id] || 0) >= 2 && t.karteD) open2(t); };
  // Was glaubst du? – Vergleich am Ende
  var wgT = T.filter(function (t) { return t.wgvergleich; })[0], wgBox;
  function wgRefresh() {
    if (!wgT) return;
    var done = S.pdfDone || T.filter(function (t) { return t.tag !== "Zusatz"; }).every(function (t) { return isDone(t); });
    if (!wgBox) { wgBox = mk("div", "wg-end"); wgBox.hidden = true; var tk = document.getElementById("tasks"); tk.parentNode.insertBefore(wgBox, tk.nextSibling); }
    wgBox.hidden = !done; if (!done) return;
    var w = wgT.wgvergleich, mine = ((S.a[wgT.id] || {})[w.feld]) || "";
    wgBox.textContent = ""; wgBox.appendChild(mk("h3", "", "Was glaubst du? – dein Vergleich"));
    wgBox.appendChild(mk("p", "", mine ? "Du hast gedacht: »" + mine + "«. " + (mine === w.richtig ? "Das passt gut zum Buch. " : "Das Buch sieht es etwas anders. ") + w.text : w.text));
  }
  var ou = update; update = function () { ou.apply(this, arguments); wgRefresh(); };
  window.addEventListener("load", function () {
    var o = window.LH_pdf;
    window.LH_pdf = function (t, base) {
      var r = o ? o(t, base) : base; if (!(t.tipp1 || t.karteD)) return r;
      var a = (S.tipps || {})[t.id] || []; return r + (a.length ? " · Hilfe: Tipp " + a.join(", ") : " · ohne Tipp");
    };
    wgRefresh();
  });
})();
