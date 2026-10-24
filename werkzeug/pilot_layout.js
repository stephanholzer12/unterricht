/* PILOT Arbeitsblatt-Layout (nur Seiten aus werkzeug/pilot_layout_einbauen.py, derzeit 4AB Elektromagnet).
   Ändert keinen Speicherschlüssel und keine Antwort; verschiebt nur Elemente und ändert Anzeigetexte.
     1. Gesamter Fahrplan ist zugeklappt (»Fahrplan öffnen«), damit die Aufgaben schneller erreichbar sind.
     2. Fortschritt getrennt: »Pflicht: x von y ausgefüllt · Zusatz: a von b« (nur Aufgaben ohne Tag »Zusatz« zählen für den Balken).
     3. Knopf »Weiter bei Aufgabe N« (erste offene Pflichtaufgabe) (springt nur, ändert nichts).
     4. Zusatzaufgaben stehen in einem zugeklappten Bereich; er öffnet sich von selbst, wenn dort schon etwas eingetragen ist oder ein Link dorthin zeigt.
   Einbau: python3 werkzeug/pilot_layout_einbauen.py */
(function () {
  if (window.__pilotLayout) return; window.__pilotLayout = true;
  if (typeof T === "undefined" || typeof update !== "function" || typeof isDone !== "function") return;
  var pflicht = T.filter(function (t) { return t.tag !== "Zusatz"; }), zus = T.filter(function (t) { return t.tag === "Zusatz"; });
  var ruhig = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 1 Fahrplan zuklappen */
  var fp = document.querySelector("section.fahrplan");
  if (fp && !fp.closest("details")) {
    var std = fp.querySelector(".std"), det = document.createElement("details"), sm = document.createElement("summary");
    det.className = "pl-fahrplan"; var mh = std && /(\d+)\s*Stunden?/.exec(std.textContent); sm.textContent = "Fahrplan öffnen" + (mh ? " · " + mh[0] : "");
    fp.parentNode.insertBefore(det, fp); det.appendChild(sm); det.appendChild(fp);
  }

  /* 4 Zusatzaufgaben zuklappen */
  var zusDet = null, tasks = document.getElementById("tasks");
  if (tasks && zus.length) {
    var kart = zus.map(function (t) { return document.getElementById("card_" + t.id); }).filter(Boolean);
    if (kart.length) {
      zusDet = document.createElement("details"); zusDet.className = "pl-zusatz";
      var s2 = document.createElement("summary"); s2.textContent = "Zusatzaufgaben " + zus[0].nr + "–" + zus[zus.length - 1].nr + " · nur wenn Zeit bleibt";
      var inh = document.createElement("div"); inh.className = "pl-zusatz-inhalt";
      var kids = Array.prototype.slice.call(tasks.children), ab = kids.indexOf(kart[0]), rest = kids.slice(ab);
      tasks.insertBefore(zusDet, kart[0]); zusDet.appendChild(s2); zusDet.appendChild(inh);
      /* alles ab der ersten Zusatzkarte verschieben – auch die Zwischenüberschriften (»Halbleiter · optional«) */
      rest.forEach(function (c) { inh.appendChild(c); });
      if (zus.some(function (t) { var a = S.a[t.id] || {}; return Object.keys(a).some(function (k) { return a[k] != null && String(a[k]).trim() !== ""; }); })) zusDet.open = true;   /* leere Einträge zählen nicht */
    }
  }
  function oeffneZiel() {
    var id = (location.hash || "").slice(1); if (!id || !zusDet) return;
    var z = document.getElementById(id); if (z && zusDet.contains(z)) { zusDet.open = true; z.scrollIntoView(); }
  }
  window.addEventListener("hashchange", oeffneZiel); oeffneZiel();

  /* 3 Knopf »Zur ersten offenen Pflichtaufgabe« */
  var steps = document.querySelector("ol.steps"), knopf = document.createElement("button");
  knopf.type = "button"; knopf.className = "btn secondary small pl-weiter";
  if (steps) steps.parentNode.insertBefore(knopf, steps.nextSibling);
  function erste() { for (var i = 0; i < pflicht.length; i++) if (!isDone(pflicht[i])) return pflicht[i]; return null; }
  knopf.addEventListener("click", function () {
    var t = erste(), z = t ? document.getElementById("card_" + t.id) : document.getElementById("abgabe");
    if (z) z.scrollIntoView({ behavior: ruhig ? "auto" : "smooth", block: "start" });
  });

  /* 2 Fortschritt getrennt anzeigen */
  var u0 = update;
  update = function () {
    u0();
    try {
      var np = pflicht.filter(isDone).length, nz = zus.filter(isDone).length, c = document.getElementById("count"), bar = document.getElementById("barfill");
      if (c) c.textContent = "Pflicht: " + np + " von " + pflicht.length + " ausgefüllt" + (zus.length ? " · Zusatz: " + nz + " von " + zus.length : "");
      if (bar && pflicht.length) bar.style.width = (np / pflicht.length * 100) + "%";
      var t = erste();
      knopf.textContent = t ? "Weiter bei Aufgabe " + t.nr : "Alle Pflichtaufgaben ausgefüllt – weiter zur Abgabe"; knopf.title = "Springt zur ersten offenen Pflichtaufgabe";
    } catch (e) {}
  };
  update();

  var st = document.createElement("style");
  st.textContent = "details.pl-fahrplan,details.pl-zusatz{background:#fff;border:2px solid #7FA83A;border-radius:16px;margin:14px 0;min-width:0;max-width:100%}" +
    "details.pl-fahrplan>summary,details.pl-zusatz>summary{cursor:pointer;font-weight:700;color:#3B4A2F;padding:14px 16px;min-height:44px;list-style-position:inside}" +
    "details.pl-fahrplan>.fahrplan{border:0;margin:0;padding-top:0}details.pl-zusatz{border-color:#D3DCC2}" +
    ".pl-zusatz-inhalt{display:grid;gap:14px;padding:0 10px 12px}.pl-weiter{margin-top:10px;min-height:44px}";
  document.head.appendChild(st);
})();
