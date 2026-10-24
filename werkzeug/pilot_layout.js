/* PILOT Arbeitsblatt-Layout (alle Arbeitsblätter mit dem Standard-Aufbau, siehe werkzeug/pilot_layout_einbauen.py).
   Ändert keinen Speicherschlüssel und keine Antwort; verschiebt nur Elemente und ändert Anzeigetexte.
     1. Gesamter Fahrplan ist zugeklappt (»Fahrplan öffnen«), damit die Aufgaben schneller erreichbar sind.
     2. Fortschritt getrennt: »Pflicht: x von y ausgefüllt · Zusatz: a von b« (nur Aufgaben ohne Tag »Zusatz« zählen für den Balken).
     3. Knopf »Weiter bei Aufgabe N«: merkt sich die zuletzt bearbeitete Aufgabe (eigener Schlüssel »weiter|<Ordner>«, nicht der Antwort-Speicher) und springt zur nächsten offenen Pflichtaufgabe ab dort (sonst zur ersten offenen). Springt nur, ändert nichts.
   5. Schreibt den Fortschritt (Pflicht x von y) unter »fortschritt|<Ordner>« für den Balken auf der Klassenseite.
     4. Zusatzaufgaben (Tag »Zusatz«, »optional«, »Für Schnelle«) stehen in einem zugeklappten Bereich; er öffnet sich von selbst, wenn dort schon etwas eingetragen ist oder ein Link dorthin zeigt.
   Einbau: python3 werkzeug/pilot_layout_einbauen.py */
(function () {
  if (window.__pilotLayout) return; window.__pilotLayout = true;
  if (typeof T === "undefined" || typeof update !== "function" || typeof isDone !== "function") return;
  var istZus = function (t) { return /^(zusatz|optional|für schnelle)$/i.test(String(t.tag || "").trim()); };
  var pflicht = T.filter(function (t) { return !istZus(t); }), zus = T.filter(istZus);
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
    /* nur zuklappen, wenn ab der ersten Zusatzkarte nur noch Zusatzkarten (und Zwischenüberschriften) folgen */
    var kidsA = Array.prototype.slice.call(tasks.children), a0 = kart.length ? kidsA.indexOf(kart[0]) : -1;
    var sauber = a0 >= 0 && kidsA.slice(a0).every(function (c) { return kart.indexOf(c) >= 0 || !/^card_/.test(c.id || ""); });
    if (kart.length && sauber) {
      zusDet = document.createElement("details"); zusDet.className = "pl-zusatz";
      var s2 = document.createElement("summary"); s2.textContent = (zus.length === 1 ? "Zusatzaufgabe " + zus[0].nr : "Zusatzaufgaben " + zus[0].nr + "–" + zus[zus.length - 1].nr) + " · nur wenn Zeit bleibt";
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
  var dir = location.pathname.replace(/[^\/]*$/, "");
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function erste() {
    var z = lsGet("weiter|" + dir), ab = -1;
    for (var j = 0; j < pflicht.length; j++) if (pflicht[j].id === z) ab = j;
    if (ab >= 0 && !isDone(pflicht[ab])) return pflicht[ab];
    for (var k = 1; k <= pflicht.length; k++) { var t = pflicht[(ab + k + pflicht.length) % pflicht.length]; if (t && !isDone(t)) return t; }
    return null;
  }
  /* Beschriftung und Sprungziel kommen aus derselben Funktion (erste) und werden nach jeder Änderung neu gesetzt */
  function knopfText() {
    var t = erste();
    knopf.textContent = t ? "Weiter bei Aufgabe " + t.nr : "Alle Pflichtaufgaben ausgefüllt – weiter zur Abgabe";
    knopf.title = "Springt zu der Aufgabe, an der du zuletzt gearbeitet hast (sonst zur ersten offenen Pflichtaufgabe)";
  }
  if (tasks) ["input", "change", "click", "focusin"].forEach(function (ev) {
    tasks.addEventListener(ev, function (e) {
      var c = e.target && e.target.closest ? e.target.closest("[id^=card_]") : null;
      if (c) { var id = c.id.slice(5); if (pflicht.some(function (t) { return t.id === id; })) { lsSet("weiter|" + dir, id); knopfText(); } }
    }, true);
  });
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
      if (c) c.textContent = zus.length ? "Pflicht: " + np + " von " + pflicht.length + " ausgefüllt · Zusatz: " + nz + " von " + zus.length : np + " von " + pflicht.length + " ausgefüllt";
      if (bar && pflicht.length) bar.style.width = (np / pflicht.length * 100) + "%";
      lsSet("fortschritt|" + dir, JSON.stringify({ np: np, n: pflicht.length }));
      knopfText();
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
