/* PDF-Sicherung (Probe, Stand 12.11.2026).
   Problem: Antworten liegen nur im Browser-Speicher. Safari (iPhone), DuckDuckGo, privater Modus, Handywechsel
   oder »Verlauf löschen« können sie entfernen. Lösung ohne Server: Jede PDF, die die Seite erstellt, trägt die
   Antworten unsichtbar mit (Feld »Keywords« der PDF-Eigenschaften, Kennung BHAKSICHERUNG1). Mit dem Knopf
   »Antworten aus PDF zurückholen« liest die Seite sie wieder ein – in jedem Browser, auf jedem Gerät.
   Gesichert werden nur die Speicher-Einträge dieser Seite (KEY und KEY-…, also auch Fotos). KEY, S und S.a
   bleiben unverändert. Eigener Zusatz-Schlüssel: keiner.
   Einbau: python3 werkzeug/pdf_sicherung_einbauen.py (idempotent). Design nur funktional, an das Bestehende angelehnt. */
(function () {
  if (window.__pdfSicherung) return; window.__pdfSicherung = true;
  var MARKE = "BHAKSICHERUNG1:", MAX = 6000000;
  function key() { try { return typeof KEY === "string" ? KEY : null; } catch (e) { return null; } }
  function b64(str) { var b = new TextEncoder().encode(str), s = "", i; for (i = 0; i < b.length; i += 8192) s += String.fromCharCode.apply(null, b.subarray(i, i + 8192)); return btoa(s); }
  function unb64(s) { var r = atob(s), b = new Uint8Array(r.length), i; for (i = 0; i < r.length; i++) b[i] = r.charCodeAt(i); return new TextDecoder("utf-8", { fatal: true }).decode(b); }
  function paket() {
    var k = key(); if (!k) return null;
    try { if (typeof save === "function") save(); } catch (e) {}
    var ls = {}, fotos = {}, i, n, v, name = "";
    try {
      for (i = 0; i < localStorage.length; i++) { n = localStorage.key(i); if (n === k || n.indexOf(k + "-") === 0) { v = localStorage.getItem(n); if (n.indexOf(k + "-foto-") === 0) fotos[n] = v; else ls[n] = v; } }
    } catch (e) { return null; }
    if (!ls[k]) return null;
    try { name = (JSON.parse(ls[k]).name || ""); } catch (e) {}
    var p = { v: 1, key: k, zeit: new Date().toISOString(), name: name, ls: ls, fotos: true };
    Object.keys(fotos).forEach(function (f) { p.ls[f] = fotos[f]; });
    var s = b64(JSON.stringify(p));
    if (s.length > MAX) { Object.keys(fotos).forEach(function (f) { delete p.ls[f]; }); p.fotos = false; s = b64(JSON.stringify(p)); }
    return s.length > MAX ? null : MARKE + s + ":ENDE";
  }
  // --- Einbetten: jede neue PDF bekommt die Sicherung als Eigenschaft ---
  function haken() {
    var J = window.jspdf && window.jspdf.jsPDF; if (!J || J.__sicherung) return !!J;
    J.__sicherung = true;
    J.API.events.push(["initialized", function () { try { var p = paket(); if (p) this.setProperties({ keywords: p }); } catch (e) {} }]);
    return true;
  }
  if (!haken()) { var tr = 0, iv = setInterval(function () { if (haken() || ++tr > 40) clearInterval(iv); }, 250); }
  // --- Zurückholen ---
  function mk(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  function lesen(buf) {
    var b = new Uint8Array(buf), s = "", i; for (i = 0; i < b.length; i += 8192) s += String.fromCharCode.apply(null, b.subarray(i, i + 8192));
    var a = s.lastIndexOf(MARKE); if (a < 0) return { fehler: "In dieser PDF steckt keine Sicherung. Nimm eine PDF, die du auf dieser Seite ab dem Einbau der Sicherung erstellt hast." };
    var e = s.indexOf(":ENDE", a); if (e < 0) return { fehler: "Die Sicherung in dieser PDF ist unvollständig." };
    var roh = s.slice(a + MARKE.length, e).replace(/\\\r?\n/g, "").replace(/[^A-Za-z0-9+\/=]/g, "");
    try { return { p: JSON.parse(unb64(roh)) }; } catch (x) { return { fehler: "Die Sicherung in dieser PDF lässt sich nicht lesen." }; }
  }
  function bauen() {
    var k = key(), anker = document.getElementById("resetwrap"); if (!k || !anker || document.getElementById("ps-box")) return;
    var st = mk("style"); st.textContent = ".ps-box{margin:12px 0;border:2px solid #D3DCC2;border-radius:12px;padding:10px 12px;background:#F7FAF0}.ps-box summary{min-height:44px;display:flex;align-items:center;font-weight:700;cursor:pointer}" +
      ".ps-box p{margin:8px 0;font-size:16px;line-height:1.45}.ps-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}.ps-b{min-height:48px;flex:1 1 140px;border-radius:10px;border:2px solid #3B4A2F;background:#3B4A2F;color:#fff;font-weight:700;font-size:17px;font-family:inherit;padding:8px 12px;cursor:pointer}" +
      ".ps-b.alt{background:#fff;color:#3B4A2F}.ps-msg{border-radius:10px;padding:10px 12px;background:#fff;border:2px solid #D3DCC2}.ps-msg.err{border-color:#B3261E}.ps-warn{background:#FFF4CC;border-bottom:2px solid #C9A227;padding:10px 14px;font:16px/1.4 system-ui,sans-serif;color:#2C3424}";
    document.head.appendChild(st);
    var box = mk("details", "ps-box"); box.id = "ps-box";
    box.appendChild(mk("summary", "", "Antworten weg? Aus einer PDF zurückholen"));
    box.appendChild(mk("p", "", "Jede PDF von dieser Seite enthält eine Sicherung deiner Antworten. Wähle deine letzte PDF aus (Downloads oder LMS). Das geht auch auf einem anderen Handy oder in einem anderen Browser."));
    var inp = mk("input"); inp.type = "file"; inp.accept = "application/pdf,.pdf"; inp.hidden = true; inp.setAttribute("aria-label", "PDF mit Sicherung auswählen");
    var wahl = mk("button", "ps-b", "PDF auswählen"); wahl.type = "button"; wahl.onclick = function () { inp.value = ""; inp.click(); };
    var out = mk("div"); out.setAttribute("aria-live", "polite");
    var row = mk("div", "ps-row"); row.appendChild(wahl); box.appendChild(inp); box.appendChild(row); box.appendChild(out);
    function sag(txt, err) { out.textContent = ""; var m = mk("p", "ps-msg" + (err ? " err" : ""), txt); out.appendChild(m); return m; }
    inp.addEventListener("change", function () {
      var f = inp.files && inp.files[0]; if (!f) return;
      var fr = new FileReader();
      fr.onerror = function () { sag("Die Datei konnte nicht gelesen werden.", true); };
      fr.onload = function () {
        var r = lesen(fr.result); if (r.fehler) { sag(r.fehler, true); return; }
        var p = r.p;
        if (!p || p.v !== 1 || !p.ls || p.key !== k || typeof p.ls[k] !== "string") { sag("Diese PDF gehört zu einem anderen Arbeitsblatt. Öffne das passende Arbeitsblatt und versuche es dort.", true); return; }
        var n = 0; try { n = Object.keys(JSON.parse(p.ls[k]).a || {}).length; } catch (x) { sag("Die Sicherung in dieser PDF lässt sich nicht lesen.", true); return; }
        var d = new Date(p.zeit), wann = isNaN(d) ? "" : d.toLocaleString("de-AT", { day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit" });
        sag("Sicherung gefunden: " + (p.name ? p.name + " · " : "") + wann + " · " + n + " bearbeitete Aufgaben" + (p.fotos === false ? " · ohne Fotos (zu groß)" : "") + ". Laden ersetzt alles, was jetzt auf diesem Gerät in diesem Arbeitsblatt steht.");
        var rr = mk("div", "ps-row"), ja = mk("button", "ps-b", "Diese Antworten laden"), nein = mk("button", "ps-b alt", "Abbrechen"); ja.type = nein.type = "button";
        nein.onclick = function () { out.textContent = ""; };
        ja.onclick = function () {
          try {
            var weg = [], i, nm; for (i = 0; i < localStorage.length; i++) { nm = localStorage.key(i); if (nm === k || nm.indexOf(k + "-") === 0) weg.push(nm); }
            var alt = {}; weg.forEach(function (x) { alt[x] = localStorage.getItem(x); });
            try { weg.forEach(function (x) { localStorage.removeItem(x); }); Object.keys(p.ls).forEach(function (x) { if (x === k || x.indexOf(k + "-") === 0) localStorage.setItem(x, p.ls[x]); }); }
            catch (e2) { Object.keys(p.ls).forEach(function (x) { try { localStorage.removeItem(x); } catch (e3) {} }); Object.keys(alt).forEach(function (x) { try { localStorage.setItem(x, alt[x]); } catch (e3) {} }); throw e2; }
            location.reload();
          } catch (e) { sag("Das Laden hat nicht geklappt (der Speicher dieses Browsers ist gesperrt oder voll). Es wurde nichts geändert.", true); }
        };
        rr.appendChild(ja); rr.appendChild(nein); out.appendChild(rr);
      };
      fr.readAsArrayBuffer(f);
    });
    anker.parentNode.insertBefore(box, anker);
    // Browser, die Daten löschen: deutlich warnen
    var ua = navigator.userAgent || "", grund = "";
    if (/DuckDuckGo/i.test(ua)) grund = "DuckDuckGo löscht gespeicherte Antworten oft von selbst.";
    try { localStorage.setItem("ps-test", "1"); localStorage.removeItem("ps-test"); } catch (e) { grund = "Dieser Browser speichert gerade nichts (privater Modus oder Speicher gesperrt)."; }
    if (grund) { var w = mk("div", "ps-warn"); w.setAttribute("role", "status"); var bb = mk("strong", "", "Achtung: "); w.appendChild(bb); w.appendChild(document.createTextNode(grund + " Erstelle am Ende jeder Stunde die PDF – daraus kannst du deine Antworten zurückholen.")); document.body.insertBefore(w, document.body.firstChild); }
    try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {}); } catch (e) {}
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", bauen); else bauen();
})();
