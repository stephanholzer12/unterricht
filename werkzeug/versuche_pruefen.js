/* »Eingaben prüfen« für die Versuchsseiten (Gruppenprotokoll am Handy).
   Unter jedem Versuch steht ein Knopf. Er prüft, ob alles ausgefüllt ist und ob die Texte zur Frage passen, und gibt Hilfe in Stufen
   – bei jedem weiteren Klick etwas mehr (Lösung wird nie verraten, die Lehrkraft liest und bewertet endgültig):
     1. Klick: Hinweis      (»Erkenntnis ist noch leer«, »passt noch nicht ganz zur Frage – lies die Frage noch einmal«)
     2. Klick: Tipp         (Schulbuchseite, Link zur Theorie-Seite, »die Frage hat mehrere Teile«)
     3. Klick: ein fehlender Begriff / Gedanke wird genannt
     4. Klick und weiter: alle noch fehlenden Begriffe
   Gezählt werden nur Klicks, bei denen etwas nicht gepasst hat. Die Zahl steht in S.chk (eigener Platz im Speicherstand der Seite,
   NICHT in S.a – sonst würde der Versuch als »bearbeitet« zählen); der Speicherschlüssel der Seite bleibt gleich.
   Die PDF bekommt je Versuch eine Zeile »Selbstkontrolle: …« (für die Lehrkraft: Wie oft hat die Gruppe geprüft, welche Stufe erreicht).
   Regeln pro Versuch: werkzeug/versuche_pruefung.json (als window.__VS_PRUEFUNG eingesetzt von versuche_pruefen_einbauen.py). */
(function () {
  if (window.__vspruefen) return; window.__vspruefen = true;
  var DATA = window.__VS_PRUEFUNG || {};
  if (typeof V === "undefined" || typeof S === "undefined") return;
  var MINW = { erk: 3, interp: 6, schluss: 5, beob: 1 };
  var NAMEN = { erk: "Erkenntnis", interp: "Interpretation", schluss: "Schlussfolgerung" };

  var css = ".vp-wrap{margin-top:14px;padding-top:12px;border-top:1px dashed #C9D3B6}" +
    ".vp-hilfe{font-size:15px;color:#5E6652;margin:0 0 8px}" +
    ".vp-box{margin-top:10px;padding:10px 12px;border-radius:10px;border-left:5px solid #B07A00;background:#FFF4D6;color:#3F2D00;font-size:16px;line-height:1.4}" +
    ".vp-box.vp-gut{border-left-color:#3F6B14;background:#EEF4E4;color:#2C3D16}" +
    ".vp-box[hidden]{display:none}.vp-box b{display:block;margin-bottom:4px}" +
    ".vp-box ul{margin:6px 0 0;padding-left:20px}.vp-box li{margin:4px 0}.vp-box a{color:inherit;font-weight:700}" +
    ".vp-box .vp-stufe{font-size:14px;opacity:.85;margin-top:6px}" +
    "input.vp-fehlt,textarea.vp-fehlt{border:2px dashed #8C3B2E!important;background:#FBEDEA!important}" +
    "input.vp-ok,textarea.vp-ok{border:2px solid #3F6B14!important}" +
    "@media print{.vp-wrap{display:none}}";
  var st = document.createElement("style"); st.id = "vp-css"; st.textContent = css; document.head.appendChild(st);

  /* ---------- Text-Hilfen ---------- */
  function norm(s) {
    s = String(s || "").toLowerCase().replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss");
    try { s = s.normalize("NFD").replace(/[̀-ͯ]/g, ""); } catch (e) {}
    return s.replace(/(\d)[.\s'](?=\d{3}(?!\d))/g, "$1").replace(/\s+/g, " ").trim();
  }
  function lev(a, b) {
    var m = a.length, n = b.length, i, j, d = [];
    for (i = 0; i <= m; i++) { d[i] = [i]; } for (j = 1; j <= n; j++) d[0][j] = j;
    for (i = 1; i <= m; i++) for (j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    return d[m][n];
  }
  /* kommt der Stamm im Text vor? (auch in Wortmitte, bei längeren Stämmen mit einem Tippfehler) */
  function hat(stamm, t, wörter) {
    if (t.indexOf(stamm) >= 0) return true;
    if (stamm.length < 6 || stamm.indexOf(" ") >= 0) return false;
    for (var i = 0; i < wörter.length; i++) {
      var w = wörter[i]; if (w.length < stamm.length - 1) continue;
      if (lev(w.slice(0, stamm.length), stamm) <= 1) return true;
    }
    return false;
  }
  function gruppe(g) {
    var i = g.indexOf("="), label = i < 0 ? g : g.slice(0, i), stämme = (i < 0 ? g : g.slice(i + 1)).split(",").map(function (x) { return norm(x); }).filter(Boolean);
    return { label: label, stämme: stämme };
  }
  function wörterZahl(s) { return (String(s).match(/[A-Za-zÄÖÜäöüß0-9]+/g) || []).length; }
  function hatZahl(s) { return /\d/.test(s) || /\b(keine|kein|null)\b/i.test(s); }

  /* ---------- Prüfung eines Versuchs ---------- */
  function felder(v) {
    var L = [], z = v.beob.zeilen, nG = Math.max.apply(null, z.map(function (r) { return r.length; })), R = (DATA[v.id] || {});
    z.forEach(function (row, ri) {
      for (var c = nG; c < v.beob.kopf.length; c++) {
        var key = "b" + ri + "_" + c;
        L.push({ id: v.id + "_" + key, art: "beob", name: row.join(" · ").replace(/\s+·\s+·/g, " ·") + " – " + v.beob.kopf[c], regel: (R.beob || {})[key] || {} });
      }
    });
    ["erk", "interp", "schluss"].forEach(function (k) { L.push({ id: v.id + "_" + k, art: k, name: NAMEN[k], regel: R[k] || {} }); });
    return L;
  }
  function wert(f, v) { var a = (S.a[v.id] || {}); var key = f.id.slice(v.id.length + 1); return String(a[key] == null ? "" : a[key]); }

  function pruefe(v) {
    var out = [], gut = [];
    felder(v).forEach(function (f) {
      var txt = wert(f, v), t = norm(txt), w = t.split(" "), r = f.regel, p = null;
      if (!t && r.opt) return;   /* freiwilliges Feld (z. B. Gegenprobe nur bei aufgerufenen Gruppen): leer ist in Ordnung */
      if (!t) p = { typ: "leer" };
      else if (r.strich && /^[-\u2013\u2014\s]+$/.test(txt)) { /* Strich ist erlaubt */ }
      else if (/([a-z])\1{3,}/.test(t) || (wörterZahl(txt) >= 1 && !/[a-z0-9]/.test(t))) p = { typ: "unsinn" };
      else if (r.zahl && !hatZahl(txt)) p = { typ: "zahl" };
      else if (wörterZahl(txt) < (r.min || MINW[f.art])) p = { typ: "kurz" };
      else if (r.kw) {
        var fehlt = [], n = 0;
        r.kw.forEach(function (g) { var G = gruppe(g), ok = G.stämme.some(function (s) { return hat(s, t, w); }); if (ok) n++; else fehlt.push(G.label); });
        if (n < (r.need || 1)) p = { typ: "inhalt", fehlt: fehlt };
        else if (r.order) {
          var pos = r.order.map(function (s) { return t.indexOf(norm(s)); });
          if (pos.every(function (x) { return x >= 0; })) {
            var auf = pos.every(function (x, i) { return i === 0 || x > pos[i - 1]; }), ab = pos.every(function (x, i) { return i === 0 || x < pos[i - 1]; });
            if (!(auf || (r.orderAny && ab))) p = { typ: "reihenfolge" };
          }
        }
      }
      if (p) { p.f = f; out.push(p); } else gut.push(f);
    });
    return { probleme: out, gut: gut };
  }

  /* ---------- Meldungen nach Stufe ---------- */
  function seite(v) { return v.buch && v.buch.s ? v.buch.s : ""; }
  function meldung(p, stufe, v) {
    var t = p.typ, s = seite(v);
    if (t === "leer") return p.f.art === "beob" ? "noch leer – trage ein, was du gesehen oder gemessen hast." : "noch leer. Lies die Frage über dem Feld und schreibe deine Antwort in ganzen Sätzen.";
    if (t === "unsinn") return "das sieht noch nicht nach einer Antwort aus. Schreibe in Worten, was du beobachtet bzw. gedacht hast.";
    if (t === "zahl") return stufe >= 2 ? "hier fehlt eine Zahl. Tipp: Trage den Messwert ein, wenn möglich mit Einheit (z. B. s, °C, µT). Wurde nichts gemessen, schreibe »keine«." : "hier fehlt noch eine Zahl (Messwert).";
    if (t === "kurz") return stufe >= 2 ? "noch zu kurz. Tipp: Beantworte jeden Teil der Frage und schreibe ganze Sätze – mindestens " + (p.f.regel.min || MINW[p.f.art]) + (((p.f.regel.min || MINW[p.f.art]) === 1) ? " Wort." : " Wörter.") : "noch sehr kurz. Schreibe etwas mehr dazu.";
    if (t === "reihenfolge") return "die Reihenfolge stimmt noch nicht ganz. Lies die Frage noch einmal: Wer ist als Erstes, wer als Letztes dran?";
    /* inhalt */
    var f = p.fehlt || [];
    if (stufe <= 1) return p.f.art === "beob" ? "passt noch nicht ganz zu dem, was beim Versuch zu sehen ist. Schau dir die Durchführung noch einmal an." : "passt noch nicht ganz zur Frage. Lies die Frage noch einmal und beantworte jeden Teil davon.";
    if (stufe === 2) return "Tipp: " + (s ? "Lies im Schulbuch " + s + " nach oder " : "") + "schau auf der Theorie-Seite nach. Die Frage hat oft mehr als einen Teil – hast du jeden beantwortet?";
    if (stufe === 3) return f.length ? "es fehlt noch ein Gedanke, zum Beispiel zu: »" + f[0] + "«." : "es fehlt noch etwas Wichtiges.";
    return f.length ? "es fehlen noch diese Begriffe bzw. Gedanken: " + f.map(function (x) { return "»" + x + "«"; }).join(", ") + "." : "es fehlt noch etwas Wichtiges.";
  }

  /* ---------- Zustand ---------- */
  function chk(v) { S.chk = S.chk || {}; return (S.chk[v.id] = S.chk[v.id] || { n: 0, k: 0, last: 0 }); }

  function zeigen(v, box, res, c) {
    var P = res.probleme;
    box.hidden = false; box.textContent = "";
    box.className = "vp-box" + (P.length ? "" : " vp-gut");
    var kopf = document.createElement("b");
    if (!P.length) {
      kopf.textContent = "✓ Alles ausgefüllt, und deine Texte passen zu den Fragen.";
      box.appendChild(kopf);
      var s = document.createElement("div"); s.textContent = "Ob alles richtig ist, bewertet deine Lehrkraft. Du kannst jetzt zum nächsten Versuch oder unten die PDF erstellen."; box.appendChild(s);
    } else {
      kopf.textContent = P.length + (P.length === 1 ? " Hinweis" : " Hinweise") + " (Prüfung " + c.k + ")";
      box.appendChild(kopf);
      var ul = document.createElement("ul");
      P.forEach(function (p) {
        var li = document.createElement("li"), b = document.createElement("b"); b.style.display = "inline"; b.textContent = p.f.name + ": ";
        li.appendChild(b); li.appendChild(document.createTextNode(meldung(p, c.k, v)));
        ul.appendChild(li);
      });
      box.appendChild(ul);
      if (c.k >= 2) { var a = document.createElement("a"); a.href = "theorie.html"; a.textContent = "Zur Theorie"; var d = document.createElement("div"); d.className = "vp-stufe"; d.appendChild(a); d.appendChild(document.createTextNode(" – dort steht die Theorie zu diesem Versuch.")); box.appendChild(d); }
      var u = document.createElement("div"); u.className = "vp-stufe";
      u.textContent = c.k < 3 ? "Ändere etwas und tippe noch einmal auf »Eingaben prüfen« – du bekommst dann mehr Hilfe." : "Tippe nach dem Ändern wieder auf »Eingaben prüfen«. Kommst du nicht weiter, frag deine Gruppe oder deine Lehrkraft.";
      box.appendChild(u);
    }
    // Felder markieren
    res.gut.forEach(function (f) { var e = document.getElementById(f.id); if (e) { e.classList.remove("vp-fehlt"); if (String(e.value).trim()) e.classList.add("vp-ok"); } });
    P.forEach(function (p) { var e = document.getElementById(p.f.id); if (e) { e.classList.remove("vp-ok"); e.classList.add("vp-fehlt"); } });
  }

  V.forEach(function (v) {
    var card = document.getElementById("card_" + v.id); if (!card) return;
    var body = card.querySelector(".vbody"); if (!body) return;
    var wrap = document.createElement("div"); wrap.className = "vp-wrap";
    var hilfe = document.createElement("p"); hilfe.className = "vp-hilfe";
    hilfe.textContent = "Fertig mit diesem Versuch? Lass prüfen, ob alles ausgefüllt ist und deine Texte zur Frage passen. Du bekommst Hinweise und Tipps – bei jedem weiteren Tippen etwas mehr Hilfe.";
    var btn = document.createElement("button"); btn.type = "button"; btn.className = "btn secondary"; btn.textContent = "Eingaben prüfen";
    var box = document.createElement("div"); box.className = "vp-box"; box.hidden = true; box.setAttribute("role", "status"); box.setAttribute("aria-live", "polite");
    wrap.appendChild(hilfe); wrap.appendChild(btn); wrap.appendChild(box); body.appendChild(wrap);
    btn.addEventListener("click", function () {
      var res = pruefe(v), c = chk(v);
      c.n++; if (res.probleme.length) c.k++; c.last = res.probleme.length; c.t = Date.now();
      if (c.k > (c.max || 0)) c.max = c.k;
      try { save(); } catch (e) {}
      zeigen(v, box, res, c);
    });
    /* Änderung an einem Feld: Markierung wieder wegnehmen */
    card.addEventListener("input", function (ev) { var e = ev.target; if (e && e.classList) { e.classList.remove("vp-fehlt"); e.classList.remove("vp-ok"); } });
  });

  /* ---------- PDF und Kopier-Text: Zeile »Selbstkontrolle« ---------- */
  if (typeof lines === "function") {
    var lines0 = lines;
    window.lines = lines = function (v) {
      var L = lines0(v), c = (S.chk || {})[v.id];
      L.push([!c || !c.n ? "Selbstkontrolle: nicht benutzt"
        : "Selbstkontrolle: " + c.n + (c.n === 1 ? " Prüfung" : " Prüfungen") + " · zuletzt " + (c.last ? c.last + (c.last === 1 ? " Hinweis offen" : " Hinweise offen") : "alles ausgefüllt") + " · höchste Hilfe-Stufe: " + (c.max || 0), "n"]);
      return L;
    };
  }
})();
