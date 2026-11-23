# -*- coding: utf-8 -*-
"""Regiepult für die Präsentation auf den privaten Lösungsseiten (Standard 20.11.2026, Skill bhak-unterricht-neue-standards).

EINE Quelle für alle Einheiten, damit die Präsentationen nicht auseinanderlaufen:
Vorschau, Notizen, »Nächster Klick«, Uhr und Stundenuhr, Timer der Phase, »Ablauf dieser Stunde«
(alle Folien nach Phasen mit Minuten, SICHERUNG markiert, antippen = hinspringen), Vollbild und
zweites Fenster für den Beamer, Schwarz (B), Timer (T), Stunde 1–4, Notizen (N), Esc.

Hier stehen nur Bedienung und Aussehen – keine Lösungen, keine Startcodes, keine Namen.
Darum darf die Datei im öffentlichen Repository liegen; die Lösungsseiten selbst nicht.

Einbau in einer Lösungsseite:
    import regiepult as RP
    css   = RP.CSS                      # zusätzlich zur eigenen .folie-CSS der Seite
    markup = RP.html(stunden=[1,2,3], klassen=["3BK"], fuss="51 Folien (Stunde 1: 19 …)")
    js    = RP.JS.replace("__SLIDES__", json.dumps(slides)) \
                 .replace("__ABLAUF__", json.dumps(ablauf)) \
                 .replace("__FCSS__", json.dumps(folien_css)) \
                 .replace("__KEY__", json.dumps(speicherschluessel))

SLIDES: [{"h": Stunde, "phase": "a3"|"start"|…, "marke": "DEMO", "titel": …, "html": …,
          "notiz": …, "klicks": 2, "min": 7}]   (min = Minuten der Phase, für den Timer)
ABLAUF: {"1": [{"von": 0, "bis": 4, "text": "Beginn: Klassenbuch", "phase": "org",
                "marke": "", "ohneHandy": true, "sicherung": false}], …}
"""

CSS = """
/* ---------- Regiepult (werkzeug/regiepult.py) ---------- */
.pv-start .steuer { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin:8px 0; }
.pv-start select { font:inherit; min-height:44px; padding:6px 10px; border:2px solid var(--line); border-radius:10px; background:#fff; }
.pv { display:grid; grid-template-columns:minmax(0,2fr) minmax(0,1fr); gap:16px; align-items:start; }
@media (max-width:860px) { .pv { grid-template-columns:1fr; } }
.pv .steuer { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-top:8px; }
.pv-l { display:grid; gap:8px; min-width:0; }
#pv-wahl { width:100%; max-width:100%; font:inherit; min-height:44px; padding:6px 10px; border:2px solid var(--line); border-radius:10px; background:#fff; }
#pv-ablauf li, .pv-r { overflow-wrap:anywhere; }
.pv-r { min-width:0; background:#fff; border:1px solid var(--line); border-radius:12px; padding:10px 14px; font-size:15.5px; }
.pv-r h3 { margin:12px 0 4px; font-size:16px; }
.stage-wrap { position:relative; overflow:hidden; background:#11150F; border-radius:10px; }
.vstage { width:100%; aspect-ratio:16/9; }
.stage { position:absolute; inset:0; }
.slot { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; }
.slot > .folie { flex:0 0 auto; }   /* 1280x720 darf im Flex-Kasten nicht schrumpfen */
.tbox { position:absolute; right:22px; top:18px; z-index:15; background:#1F2A1C; color:#fff;
  font:700 54px/1 "Source Sans 3",system-ui,sans-serif; padding:10px 20px; border-radius:16px; font-variant-numeric:tabular-nums; }
.tbox.aus { background:#8C3B2E; }
.schwarz { position:absolute; inset:0; background:#000; z-index:20; }
.pvuhr { font-size:22px; font-weight:700; margin:0; }
.pvtimer { font-size:26px; font-weight:700; color:#8C3B2E; margin:4px 0; min-height:1.2em; }
#pv-jetzt { margin:6px 0; font-weight:700; color:var(--olive); }
#pv-ablauf, #pv-notes { margin:0; padding:0; list-style:none; font-size:14.5px; }
#pv-ablauf { max-height:46vh; overflow:auto; border:1px solid var(--line); border-radius:8px; }
#pv-ablauf li { padding:5px 10px; border-bottom:1px solid #EDF1E4; }
#pv-ablauf li.ph { background:#F2F6EA; font-weight:700; color:var(--olive); }
#pv-ablauf li.ph .mi { color:var(--muted); font-weight:700; margin-right:6px; }
#pv-ablauf li.ph.sich { background:#FBF2D6; color:#6B4F00; }
#pv-ablauf li.fo { cursor:pointer; padding-left:20px; }
#pv-ablauf li.fo:hover { background:#EEF3E4; }
#pv-ablauf li.fo.jetzt { background:var(--olive); color:#fff; font-weight:700; }
#pv-notes li { padding:3px 0; }
#pv-next { margin:8px 0 0; color:var(--teal); font-weight:600; }
.mini { font:inherit; font-size:14px; font-weight:700; min-height:34px; padding:2px 10px; border-radius:8px;
  border:2px solid var(--line); background:#fff; color:var(--olive); cursor:pointer; }
#pv-ov { position:fixed; inset:0; background:#11150F; z-index:500; }
#pv-ov[hidden] { display:none; }
#pv-ov .stage-wrap { position:absolute; inset:0; border-radius:0; }
#pv-ov .ovzu { position:absolute; right:10px; top:10px; z-index:30; }
#pv-ov .ovnotiz { position:absolute; left:0; right:0; bottom:0; z-index:25; background:rgba(26,32,22,.94); color:#E7EDDD;
  padding:8px 14px; font-size:16px; max-height:28vh; overflow:auto; }
#pv-ov .ovnotiz[hidden] { display:none; }
"""


def html(stunden, klassen=(), fuss="", bedienung=True):
    """Markup für den Reiter »Präsentation«."""
    std = "".join('<option value="%d">Stunde %d</option>' % (n, n) for n in stunden)
    kl = "".join("<option>%s</option>" % k for k in klassen)
    klfeld = ('<label class="klein" for="pv-kl">Klasse</label><select id="pv-kl">%s</select>' % kl) if kl else ""
    hilfe = ""
    if bedienung:
        hilfe = ('<h3>Bedienung</h3><ul class="pts">'
                 '<li><b>Weiter:</b> Pfeil rechts, Leertaste, Bild-ab (Presenter-Klicker) oder rechts auf die Folie tippen · '
                 '<b>zurück:</b> Pfeil links, Bild-auf oder links tippen.</li>'
                 '<li>Viele Folien haben <b>Schritte</b>: Antworten und Kernsätze kommen per Klick. Was der nächste Klick macht, '
                 'steht rechts unter den Notizen.</li>'
                 '<li><b>B</b> = schwarzer Bildschirm · <b>T</b> = Timer mit der Zeit der Phase (noch einmal drücken = aus) · '
                 '<b>1–9</b> = Anfang der Stunde · <b>N</b> = Notizen im Vollbild ein/aus (sieht dann auch die Klasse) · '
                 '<b>Esc</b> = Vollbild beenden.</li>'
                 '<li>Rechts unter »Ablauf dieser Stunde« stehen alle Folien nach Phasen, mit Minuten. Antippen = hinspringen. '
                 'Die Präsentation merkt sich die letzte Folie.</li>'
                 '<li>Zweites Fenster: klappt, wenn du die Seite direkt in Chrome, Edge oder Firefox öffnest (nicht in der Claude-App). '
                 'Dort doppelklicken = Vollbild.</li></ul>')
    return ('<div class="pv-start"><div class="steuer">'
            '<label class="klein" for="pv-std">Stunde</label><select id="pv-std">%s</select>%s'
            '<button type="button" class="btn" id="pv-voll">Vollbild starten</button>'
            '<button type="button" class="btn alt" id="pv-beamer">Beamer: zweites Fenster</button></div>'
            '<p class="hint" id="pv-status" role="status" aria-live="polite">Ein Bild (Beamer gespiegelt) oder Claude-App: '
            '»Vollbild starten«. Zwei Bildschirme (»Erweitern«): zweites Fenster.</p></div>'
            '<div class="pv"><div class="pv-l">'
            '<div class="stage-wrap vstage" id="pv-buehne"><div class="stage"><div class="slot"></div>'
            '<div class="tbox" hidden></div><div class="schwarz" hidden></div></div></div>'
            '<div class="steuer"><button type="button" class="btn alt" id="pv-zur">◀ zurück</button>'
            '<button type="button" class="btn" id="pv-vor">weiter ▶</button>'
            '<span class="hint" id="pv-schritt"></span>'
            '<button type="button" class="btn alt" id="pv-schwarz" aria-pressed="false">Schwarz (B)</button>'
            '<button type="button" class="btn alt" id="pv-tstart">Timer (T)</button>'
            '<button type="button" class="mini" id="pv-tstop">Timer aus</button></div>'
            '<select id="pv-wahl" aria-label="Folie wählen"></select></div>'
            '<div class="pv-r"><p class="pvuhr"><span id="pv-uhr"></span> '
            '<button type="button" class="mini" id="pv-uhr0">Stundenuhr starten</button></p>'
            '<p class="pvtimer" id="pv-timer"></p><p id="pv-jetzt"></p>'
            '<h3>Ablauf dieser Stunde</h3><ul id="pv-ablauf"></ul>'
            '<h3>Notizen (sieht nur du)</h3><ul id="pv-notes"></ul><p id="pv-next"></p></div></div>'
            + hilfe + ('<p class="hint">%s</p>' % fuss if fuss else "")
            + '<div id="pv-ov" hidden><div class="stage-wrap"><div class="stage"><div class="slot"></div>'
              '<div class="tbox" hidden></div><div class="schwarz" hidden></div></div></div>'
              '<button type="button" class="mini ovzu" id="pv-ovzu">Schließen (Esc)</button>'
              '<div class="ovnotiz" id="pv-ovnotiz" hidden></div></div>') % (std, klfeld)


JS = r"""
/* ---------- Regiepult (werkzeug/regiepult.py) ---------- */
(function () {
  var SL = __SLIDES__, AB = __ABLAUF__, FCSS = __FCSS__, KEY = __KEY__;
  if (!SL.length || !document.getElementById("pv-buehne")) return;
  var $ = function (s, w) { return (w || document).querySelector(s); };
  var I = 0, K = 0, schwarz = false, notesOv = false, TEND = 0, UHR0 = 0, views = [];
  function lies(k) { try { return localStorage.getItem(KEY + "|" + k); } catch (e) { return null; } }
  function schreib(k, v) { try { localStorage.setItem(KEY + "|" + k, v); } catch (e) {} }
  function esc(t) { return String(t).replace(/</g, "&lt;"); }

  function folieHTML(s) {
    var kette = [], gesehen = {};
    SL.forEach(function (x) { if (x.h === s.h && !gesehen[x.phasename]) { gesehen[x.phasename] = 1; kette.push(x.phasename); } });
    var weg = true;
    var fuss = kette.map(function (p) {
      if (p === s.phasename) { weg = false; return '<span class="jetzt">' + esc(p) + "</span>"; }
      return '<span class="' + (weg ? "weg" : "") + '">' + esc(p) + "</span>";
    }).join("");
    return '<div class="kopf">' + (s.marke ? '<span class="marke m-' + s.marke + '">' + s.marke + "</span>" : "")
      + "<h2>" + s.titel + "</h2></div><div class=\"inhalt\">" + s.html + '</div><div class="fuss">' + fuss + "</div>";
  }

  function neueView(wrap, win) { var v = { wrap: wrap, win: win || window, doc: wrap.ownerDocument }; views.push(v); return v; }
  function passe(v) {
    var f = v.wrap.querySelector(".folie"); if (!f) return;
    var sk = Math.min(v.wrap.clientWidth / 1280, v.wrap.clientHeight / 720);
    f.style.transform = "scale(" + sk + ")";
  }
  function malen(v, s) {
    var slot = v.wrap.querySelector(".slot");
    var f = slot.querySelector(".folie");
    if (!f) { f = v.doc.createElement("article"); f.className = "folie"; slot.appendChild(f); }
    f.innerHTML = folieHTML(s);
    f.className = "folie klick-" + K;
    Array.prototype.forEach.call(f.querySelectorAll(".klick"), function (el) {
      el.classList.toggle("da", +(el.className.match(/k(\d+)/) || [0, 99])[1] <= K);
    });
    Array.prototype.forEach.call(f.querySelectorAll(".gafolie"), function (box) {
      var d = ((window.S && S.ga) || {})[box.dataset.ga] || {};
      box.innerHTML = (d.gruppen && d.gruppen.length)
        ? d.gruppen.map(function (g, i) { return '<div class="gr"><b>Gruppe ' + (i + 1) + ':</b> ' + esc(g.join(", ")) + "</div>"; }).join("")
        : '<p class="leer">Noch keine Einteilung – im Reiter »Gruppen« auslosen.</p>';
    });
    v.wrap.querySelector(".schwarz").hidden = !schwarz;
    passe(v);
  }

  function ablaufZeile(n) {
    var rows = AB[String(n)] || [], ul = $("#pv-ablauf"); if (!ul) return;
    var out = "";
    rows.forEach(function (r) {
      out += '<li class="ph' + (r.sicherung ? " sich" : "") + '"><span class="mi">Min ' + r.von + "–" + r.bis + "</span>"
        + (r.marke ? esc(r.marke) + " · " : "") + esc(r.text) + (r.ohneHandy ? ' <span class="pill">ohne Handy</span>' : "") + "</li>";
      SL.forEach(function (s, i) {
        if (s.h === n && (s.ab || s.phase) === r.phase) out += '<li class="fo' + (i === I ? " jetzt" : "") + '" data-i="' + i + '">' + esc(s.titel) + "</li>";
      });
    });
    ul.innerHTML = out;
  }

  function zeichne(neueStunde) {
    var s = SL[I];
    views.forEach(function (v) { malen(v, s); });
    if (neueStunde) { ablaufZeile(s.h); var sel = $("#pv-std"); if (sel) sel.value = String(s.h); }
    else {
      Array.prototype.forEach.call($("#pv-ablauf").querySelectorAll("li.fo"), function (li) {
        li.classList.toggle("jetzt", +li.dataset.i === I);
      });
    }
    var nr = SL.filter(function (x) { return x.h === s.h; }).indexOf(s) + 1;
    var von = SL.filter(function (x) { return x.h === s.h; }).length;
    $("#pv-schritt").textContent = "Folie " + (I + 1) + " von " + SL.length + " · Schritt " + K + " von " + s.klicks
      + " · Stunde " + s.h + ": " + nr + "/" + von;
    $("#pv-notes").innerHTML = "<li>" + esc(s.notiz) + "</li>";
    var danach = SL[I + 1];
    $("#pv-next").textContent = K < s.klicks
      ? "Nächster Klick: Teil " + (K + 1) + " von " + s.klicks
      : (danach ? "Nächste Folie: " + danach.titel.replace(/<[^>]+>/g, "") : "Ende");
    var naechste = null;
    for (var q = I + 1; q < SL.length; q++) { if (SL[q].phasename !== s.phasename) { naechste = SL[q]; break; } }
    $("#pv-jetzt").textContent = "Min " + s.von + "–" + s.bis + " · " + s.phasename + (naechste ? " · danach: " + naechste.phasename : "");
    var w = $("#pv-wahl"); if (w) w.value = String(I);
    var ovn = $("#pv-ovnotiz"); if (ovn) { ovn.hidden = !notesOv; ovn.textContent = s.notiz; }
    schreib("pos", I + ":" + K);
  }

  function geh(d) {
    var s = SL[I];
    if (d > 0 && K < s.klicks) { K++; zeichne(false); return; }
    if (d < 0 && K > 0) { K--; zeichne(false); return; }
    var neu = I + d; if (neu < 0 || neu >= SL.length) return;
    var alt = SL[I].h; I = neu; K = d > 0 ? 0 : SL[I].klicks;
    zeichne(SL[I].h !== alt);
  }
  function stunde(n) { var k = SL.findIndex(function (s) { return s.h === n; }); if (k >= 0) { I = k; K = 0; zeichne(true); } }
  function schw() { schwarz = !schwarz; $("#pv-schwarz").setAttribute("aria-pressed", String(schwarz)); zeichne(false); }
  function timer(min) { TEND = TEND ? 0 : Date.now() + (min || 5) * 60000; tick(); }

  function tick() {
    var d = new Date();
    var uhr = String(d.getHours()).padStart(2, "0") + ":" + String(d.getMinutes()).padStart(2, "0");
    if (UHR0) { var m = Math.floor((Date.now() - UHR0) / 60000); uhr += " · Stunde läuft seit " + m + " min"; }
    $("#pv-uhr").textContent = uhr;
    var txt = "", aus = false;
    if (TEND) {
      var r = Math.round((TEND - Date.now()) / 1000);
      aus = r < 0; if (aus) r = -r;
      txt = (aus ? "+" : "") + Math.floor(r / 60) + ":" + String(r % 60).padStart(2, "0");
    }
    $("#pv-timer").textContent = TEND ? "Timer " + txt : "";
    views.forEach(function (v) {
      var t = v.wrap.querySelector(".tbox");
      t.hidden = !TEND; t.textContent = txt; t.className = "tbox" + (aus ? " aus" : "");
    });
  }
  setInterval(tick, 500);

  function taste(ev) {
    if (ev.target.closest && ev.target.closest("input,textarea,select")) return;
    var tab = document.getElementById("t-praesentation");
    if (tab && tab.hidden && $("#pv-ov").hidden && ev.view === window) return;
    var k = ev.key;
    if (k === "ArrowRight" || k === " " || k === "PageDown") { ev.preventDefault(); geh(1); }
    else if (k === "ArrowLeft" || k === "PageUp") { ev.preventDefault(); geh(-1); }
    else if (k === "b" || k === "B") schw();
    else if (k === "t" || k === "T") timer(SL[I].min);
    else if (/^[1-9]$/.test(k)) stunde(+k);
    else if (k === "n" || k === "N") { notesOv = !notesOv; zeichne(false); }
    else if (k === "Escape" && !$("#pv-ov").hidden) zu();
  }
  document.addEventListener("keydown", taste);

  function auf() {
    var ov = $("#pv-ov"); ov.hidden = false;
    try { ov.requestFullscreen && ov.requestFullscreen().catch(function () {}); } catch (e) {}
    setTimeout(function () { zeichne(false); }, 120);
  }
  function zu() {
    $("#pv-ov").hidden = true;
    try { document.fullscreenElement && document.exitFullscreen(); } catch (e) {}
  }

  neueView($("#pv-buehne"));
  neueView($("#pv-ov .stage-wrap"));
  views.forEach(function (v) {
    v.wrap.addEventListener("click", function (ev) {
      var r = v.wrap.getBoundingClientRect();
      geh(ev.clientX - r.left < r.width / 3 ? -1 : 1);
    });
  });
  window.addEventListener("resize", function () { views.forEach(passe); });
  $("#pv-voll").onclick = auf; $("#pv-ovzu").onclick = zu;
  $("#pv-vor").onclick = function () { geh(1); }; $("#pv-zur").onclick = function () { geh(-1); };
  $("#pv-schwarz").onclick = schw;
  $("#pv-tstart").onclick = function () { timer(SL[I].min); };
  $("#pv-tstop").onclick = function () { TEND = 0; tick(); };
  $("#pv-uhr0").onclick = function () { UHR0 = UHR0 ? 0 : Date.now(); tick(); };
  $("#pv-std").onchange = function (ev) { stunde(+ev.target.value); };
  var wahl = $("#pv-wahl");
  SL.forEach(function (s, i) {
    var o = document.createElement("option");
    o.value = i; o.textContent = "Stunde " + s.h + " · " + (i + 1) + ". " + s.titel.replace(/<[^>]+>/g, "");
    wahl.append(o);
  });
  wahl.onchange = function () { I = +wahl.value; K = 0; zeichne(true); };
  document.addEventListener("click", function (ev) {
    var li = ev.target.closest && ev.target.closest("#pv-ablauf li.fo");
    if (!li) return;
    I = +li.dataset.i; K = 0; zeichne(false);
  });

  $("#pv-beamer").onclick = function () {
    var w = null;
    try { w = window.open("", "beamer", "width=1280,height=760"); } catch (e) {}
    var st = $("#pv-status");
    if (!w) { st.textContent = "Ein zweites Fenster ist hier nicht möglich (z. B. in der Claude-App). Nimm »Vollbild starten« – oder öffne die Seite direkt im Browser."; return; }
    w.document.open();
    w.document.write("<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><title>Beamer</title><style>"
      + FCSS + "html,body{margin:0;height:100%;background:#11150F;overflow:hidden}"
      + ".stage-wrap{position:fixed;inset:0}.stage{position:absolute;inset:0}"
      + ".slot{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}.slot>.folie{flex:0 0 auto}"
      + ".tbox{position:absolute;right:22px;top:18px;z-index:15;background:#1F2A1C;color:#fff;font:700 54px/1 system-ui,sans-serif;padding:10px 20px;border-radius:16px}"
      + ".tbox.aus{background:#8C3B2E}.schwarz{position:absolute;inset:0;background:#000;z-index:20}"
      + "</style></head><body><div class='stage-wrap'><div class='stage'><div class='slot'></div>"
      + "<div class='tbox' hidden></div><div class='schwarz' hidden></div></div></div></body></html>");
    w.document.close();
    var alt = -1; views.forEach(function (v, k) { if (v.win !== window) alt = k; });
    if (alt >= 0) views.splice(alt, 1);
    var v = neueView(w.document.querySelector(".stage-wrap"), w);
    w.addEventListener("resize", function () { passe(v); });
    w.document.addEventListener("keydown", taste);
    w.document.addEventListener("dblclick", function () { try { w.document.documentElement.requestFullscreen(); } catch (e) {} });
    st.textContent = "Beamer-Fenster offen: auf den Beamer ziehen, dort doppelklicken = Vollbild. Hier steuerst du weiter.";
    setTimeout(function () { zeichne(false); passe(v); tick(); }, 60);
  };

  var p0 = (lies("pos") || "0:0").split(":");
  I = Math.min(SL.length - 1, +p0[0] || 0); K = Math.min(SL[I].klicks, +p0[1] || 0);
  zeichne(true); tick();
  window.__regiepultPassen = function () { views.forEach(passe); };
})();
"""
