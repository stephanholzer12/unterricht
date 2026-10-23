/* Erinnerung beim Knopf »PDF erstellen«: Ist die Arbeit schon als PDF abgegeben – und passt die PDF noch zu den Antworten?
   Zeigt direkt über dem PDF-Knopf einen von drei Hinweisen:
     - Antworten da, aber noch keine PDF       -> »Du hast noch keine PDF erstellt …« (gelb)
     - nach der letzten PDF etwas geändert     -> »Du hast seit deiner PDF von 10:42 etwas geändert …« (gelb)
     - PDF passt zum aktuellen Stand           -> »✓ Deine PDF von 10:42 passt zu deinen Antworten …« (grün)
   Wie: Nach einer erfolgreichen PDF (Meldung »PDF wurde erstellt« bzw. »Gespeichert:« in #pdfstatus) merkt sich die Seite einen
   Fingerabdruck von Name, Klasse und Antworten (S.name, S.ich, S.klasse, S.a) und der Fotos. Der Fingerabdruck liegt unter einem
   EIGENEN Schlüssel »pdfstand|<Seitenschlüssel>«. Der Speicherstand der Seite (const KEY) wird nur gelesen, nie geschrieben.
   Prüf-Zähler, »Lösung angesehen« usw. zählen nicht als Änderung.
   Einbau: python3 werkzeug/pdf_erinnerung_einbauen.py (setzt den Seitenschlüssel als window.__PE_KEY davor). */
(function () {
  if (window.__pdferinnerung) return; window.__pdferinnerung = true;
  var KEY = window.__PE_KEY; if (!KEY) return;
  var SNAP = "pdfstand|" + KEY;
  var btn = document.getElementById("pdfbtn"), st = document.getElementById("pdfstatus");
  if (!btn || !btn.parentNode) return;
  var ls = null; try { ls = window.localStorage; } catch (e) { ls = null; }
  var memSnap = null;

  var css = "#pe-hinweis{margin:10px 0;padding:10px 12px;border-radius:10px;font-weight:600;font-size:16px;line-height:1.4;border-left:5px solid #B07A00;background:#FFF4D6;color:#4A3400}" +
    "#pe-hinweis.pe-ok{border-left-color:#3F6B14;background:#EEF4E4;color:#2C3D16}#pe-hinweis[hidden]{display:none}@media print{#pe-hinweis{display:none}}";
  var stl = document.createElement("style"); stl.id = "pe-css"; stl.textContent = css; document.head.appendChild(stl);
  var box = document.createElement("p"); box.id = "pe-hinweis"; box.hidden = true; box.setAttribute("aria-live", "polite");
  btn.parentNode.insertBefore(box, btn);

  function get(k) { try { return ls ? ls.getItem(k) : null; } catch (e) { return null; } }
  function hash(s) { var h = 5381; for (var i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0; return (h >>> 0).toString(36) + "-" + s.length; }

  /* Fingerabdruck des aktuellen Stands; inhalt = ob überhaupt schon etwas eingetragen ist */
  function stand() {
    var raw = get(KEY), o = {};
    try { o = raw ? JSON.parse(raw) : {}; } catch (e) { o = {}; }
    var a = o && o.a ? o.a : {}, fotos = [];
    try {
      for (var i = 0; ls && i < ls.length; i++) {
        var k = ls.key(i);
        if (k && k.indexOf(KEY + "-foto") === 0) { var v = get(k); if (v) fotos.push(k + ":" + hash(v)); }
      }
    } catch (e) {}
    fotos.sort();
    var aTxt = JSON.stringify(a), inhalt = false;
    for (var key in a) { var v2 = a[key]; if (v2 !== "" && v2 !== null && v2 !== false && !(v2 && typeof v2 === "object" && !Object.keys(v2).length)) { inhalt = true; break; } }
    if (fotos.length) inhalt = true;
    return { h: hash([o.name || "", o.ich || "", o.klasse || "", aTxt, fotos.join("|")].join("\u0001")), inhalt: inhalt };
  }
  function snap() {
    if (memSnap) return memSnap;
    try { var s = JSON.parse(get(SNAP) || "null"); if (s && s.h) return s; } catch (e) {}
    return null;
  }
  function zeit(t) {
    var d = new Date(t), h = new Date(), z = function (n) { return (n < 10 ? "0" : "") + n; };
    var uhr = z(d.getHours()) + ":" + z(d.getMinutes());
    return d.toDateString() === h.toDateString() ? "von " + uhr : "vom " + d.getDate() + "." + (d.getMonth() + 1) + ". um " + uhr;
  }
  function zeige() {
    var jetzt = stand(), s = snap();
    if (!s) {
      if (!jetzt.inhalt) { box.hidden = true; return; }
      box.className = ""; box.textContent = "Du hast noch keine PDF erstellt. Abgegeben ist deine Arbeit erst, wenn die PDF in LMS hochgeladen ist.";
    } else if (s.h !== jetzt.h) {
      box.className = ""; box.textContent = "Du hast seit deiner PDF " + zeit(s.t) + " etwas geändert. Erstelle die PDF neu und lade die neue Datei in LMS hoch.";
    } else {
      box.className = "pe-ok"; box.textContent = "✓ Deine PDF " + zeit(s.t) + " passt zu deinen Antworten. Hast du sie schon in LMS hochgeladen?";
    }
    box.hidden = false;
  }
  var t1 = null, t2 = null;
  function spaeter() { clearTimeout(t1); clearTimeout(t2); t1 = setTimeout(zeige, 700); t2 = setTimeout(zeige, 2500); }
  ["input", "change", "click"].forEach(function (ev) { document.addEventListener(ev, spaeter, true); });

  /* Erfolgreiche PDF erkennen */
  var zuletzt = "";
  function pruefeStatus() {
    if (!st || st.hidden) return;
    var txt = (st.textContent || "").trim();
    if (txt === zuletzt) return; zuletzt = txt;
    if (/^(PDF wurde erstellt|Gespeichert:)/.test(txt)) {
      setTimeout(function () {
        memSnap = { h: stand().h, t: Date.now() };
        try { if (ls) ls.setItem(SNAP, JSON.stringify(memSnap)); } catch (e) {}
        zeige();
      }, 300);
    }
  }
  btn.addEventListener("click", function () { zuletzt = ""; }, true);   // gleiche Meldung bei der nächsten PDF trotzdem erkennen
  if (st && window.MutationObserver) new MutationObserver(pruefeStatus).observe(st, { childList: true, characterData: true, subtree: true, attributes: true });
  if (document.readyState === "complete") zeige(); else window.addEventListener("load", zeige);
})();
