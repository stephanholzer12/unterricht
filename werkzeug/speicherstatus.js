/* Speicherstatus für die Handy-Seiten (Arbeitsblatt, Versuche, Gruppe …).
   Problem: Die Seiten speichern Antworten im Browser (localStorage). Wenn das Handy das Speichern verweigert
   (Speicher voll, privater Modus, Browser blockiert es), merkte der Kadett bisher nichts davon – und verlor beim
   Schließen der Seite alles.
   Diese Datei legt sich von außen um localStorage.setItem und zeigt
     - bei Erfolg unten links:  »Gespeichert um 10:42 auf diesem Gerät«
     - bei einem Fehler oben, nicht zu übersehen:  Warnung + Knopf »Zur PDF«.
   Sie ändert NIE einen Speicherschlüssel und NIE einen gespeicherten Wert: Jeder Aufruf wird unverändert an den
   Browser weitergereicht, ein Fehler wird nach der Anzeige unverändert weitergeworfen (die Seite behandelt ihn wie bisher).
   Gespeichert wird weiterhin bei jeder Eingabe sofort – es gibt bewusst KEIN verzögertes Speichern, damit beim Schließen
   der Seite nichts verloren geht. Verzögert (0,8 s) wird nur die Anzeige.
   Einbau: python3 werkzeug/speicherstatus_einbauen.py (setzt diese Datei inline in alle Seiten mit PDF-Abgabe). */
(function () {
  if (window.__speicherstatus) return; window.__speicherstatus = true;

  var PREFIX = "26-27-";            // alle Speicherschlüssel der Seiten beginnen so
  var ls = null; try { ls = window.localStorage; } catch (e) { ls = null; }
  var failed = {};                  // Schlüssel -> true, solange der letzte Schreibversuch scheiterte
  var okTime = null, timer = null;

  var css = "#ss-status[hidden],#ss-warn[hidden]{display:none}" +
    "#ss-status{position:fixed;left:12px;bottom:12px;z-index:9990;max-width:calc(100% - 24px);padding:6px 12px;border-radius:999px;" +
    "background:#fff;border:1px solid #D3DCC2;color:#2C3424;font:600 14px/1.3 system-ui,sans-serif;box-shadow:0 2px 8px rgba(0,0,0,.12);pointer-events:none}" +
    "#ss-status .ss-ic{color:#3F6B14;font-weight:700;margin-right:6px}" +
    "#ss-warn{position:fixed;left:0;right:0;top:0;z-index:9998;display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:12px 14px;" +
    "background:#F6E3DF;border-bottom:3px solid #8C3B2E;color:#4A150C;font:600 16px/1.4 system-ui,sans-serif}" +
    "#ss-warn span{flex:1 1 220px}" +
    "#ss-warn button{min-height:44px;padding:8px 16px;border-radius:10px;border:0;background:#8C3B2E;color:#fff;font:700 16px system-ui,sans-serif;cursor:pointer}" +
    ".status.ok,.feedback.ok strong{color:#3F6B14}" +   /* dunkleres Grün: 5,3:1 und mehr auf allen Hintergründen der Seiten */
    "body{padding-bottom:48px}" +
    "@media print{#ss-status,#ss-warn{display:none}}";
  var st = document.createElement("style"); st.id = "ss-css"; st.textContent = css; document.head.appendChild(st);

  var pill = document.createElement("div"); pill.id = "ss-status"; pill.hidden = true;
  pill.setAttribute("role", "status"); pill.setAttribute("aria-live", "polite"); pill.setAttribute("aria-atomic", "true");
  var ic = document.createElement("span"); ic.className = "ss-ic"; ic.setAttribute("aria-hidden", "true"); ic.textContent = "✓";
  var pillTxt = document.createElement("span");
  pill.appendChild(ic); pill.appendChild(pillTxt);

  var warn = document.createElement("div"); warn.id = "ss-warn"; warn.hidden = true; warn.setAttribute("role", "alert");
  var warnTxt = document.createElement("span");
  var warnBtn = document.createElement("button"); warnBtn.type = "button"; warnBtn.textContent = "Zur PDF";
  warnBtn.onclick = function () { var b = document.getElementById("pdfbtn"); if (b && b.scrollIntoView) { b.scrollIntoView({ block: "center" }); try { b.focus(); } catch (e) {} } };
  warn.appendChild(warnTxt); warn.appendChild(warnBtn);

  document.body.appendChild(pill); document.body.appendChild(warn);

  function zwei(n) { return (n < 10 ? "0" : "") + n; }

  function zeige() {
    var keys = Object.keys(failed), nurFoto = keys.length > 0;
    for (var i = 0; i < keys.length; i++) if (keys[i].indexOf("-foto-") < 0) nurFoto = false;
    if (keys.length) {
      warnTxt.textContent = nurFoto
        ? "Ein Foto konnte nicht gespeichert werden (Handy-Speicher voll). Es bleibt nur, bis du die Seite schließt – erzeuge bald die PDF."
        : "Speichern auf diesem Gerät nicht möglich! Deine Antworten gehen verloren, wenn du die Seite schließt. Erzeuge jetzt die PDF und gib sie ab.";
      warn.hidden = false; pill.hidden = true;
      return;
    }
    warn.hidden = true;
    if (okTime) {
      pillTxt.textContent = "Gespeichert um " + zwei(okTime.getHours()) + ":" + zwei(okTime.getMinutes()) + " auf diesem Gerät";
      pill.hidden = false;
    }
  }
  function zeigeSpaeter() { if (timer) clearTimeout(timer); timer = setTimeout(zeige, 800); }

  if (ls && typeof Storage !== "undefined") {
    var origSet = Storage.prototype.setItem, origRemove = Storage.prototype.removeItem;
    Storage.prototype.setItem = function (k) {
      if (this === ls && typeof k === "string" && k.indexOf(PREFIX) === 0) {
        try { origSet.apply(this, arguments); }
        catch (e) { failed[k] = true; zeige(); throw e; }      // Fehler sofort zeigen und unverändert weiterwerfen
        if (failed[k]) delete failed[k];
        if (failed["__probe"]) delete failed["__probe"];       // Speichern klappt doch – frühere Warnung beim Öffnen zurücknehmen
        okTime = new Date(); zeigeSpaeter();
        return;
      }
      return origSet.apply(this, arguments);
    };
    Storage.prototype.removeItem = function (k) {
      var r = origRemove.apply(this, arguments);
      if (this === ls && typeof k === "string" && failed[k]) { delete failed[k]; zeigeSpaeter(); }  // z. B. Foto wieder entfernt
      return r;
    };
  }

  /* Gleich beim Öffnen prüfen, ob der Browser überhaupt speichern darf – dann weiß der Kadett es, bevor er tippt. */
  try { if (!ls) throw new Error("kein localStorage"); ls.setItem("__ss_probe", "1"); ls.removeItem("__ss_probe"); }
  catch (e) { failed["__probe"] = true; zeige(); }
})();
