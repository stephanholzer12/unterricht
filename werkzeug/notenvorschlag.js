/* Punkte und Notenvorschlag nur im PDF (für die Lehrkraft, zum Eintragen in LMS) – auf dem Bildschirm der Schüler erscheint nichts.
   Wie: Beim Erstellen der PDF wird der Kasten »Punkte für LMS« ganz oben auf Seite 1 (Rand, über dem Kopf) ergänzt.
   Wertung (automatisch, nur was die Seite selbst prüfen kann):
     - jede Auswahl-/Zahlen-Antwort = 1 Punkt; Stichwort-Antworten anteilig (gefundene Stichwortgruppen / verlangte); »durchstreichen«-Aufgaben anteilig
     - Aufgaben mit angesehener Lösung = 0 Punkte (Lehrkraft bewertet selbst); Zusatzaufgaben zählen nur, wenn bearbeitet
     - Aufgaben ohne automatische Prüfung (Freitext, Skizze, Foto) stehen als »selbst bewerten« im Kasten und zählen nicht mit
   Notenschlüssel (Vorschlag): ab 88 % = 1, ab 75 % = 2, ab 62 % = 3, ab 50 % = 4, darunter 5. Ändern: SCHLUESSEL unten.
   Seiten mit eigenem Ergebnis-Kasten (Nobel, Vertiefung) nehmen »x von y Antworten richtig« aus pdfStats().
   Einbau: python3 werkzeug/notenvorschlag_einbauen.py */
(function () {
  if (window.__notenvorschlag) return; window.__notenvorschlag = true;
  var SCHLUESSEL = [[88, 1], [75, 2], [62, 3], [50, 4]];
  function note(p) { for (var i = 0; i < SCHLUESSEL.length; i++) if (p >= SCHLUESSEL[i][0]) return SCHLUESSEL[i][1]; return 5; }
  function zahl(x) { x = Math.round(x * 10) / 10; return String(x).replace(".", ","); }
  function liste(a) { return a.length ? a.join(", ") : ""; }

  function standStandard() {
    var pkt = 0, max = 0, selbst = [], gesehen = [];
    T.forEach(function (t) {
      var a = S.a[t.id] || {}, beantwortet = Object.keys(a).some(function (k) { return k !== "foto" && a[k] !== "" && a[k] != null; }) || !!a.foto;
      if ((t.tag === "Zusatz" || t.hl) && !beantwortet) return;
      var ev = null; try { ev = t.chk ? evalTask(t) : null; } catch (e) {}
      if (!ev) { selbst.push(t.nr); return; }
      var viewed = typeof LH_viewed === "function" && LH_viewed(t), teile = 0, erreicht = 0;
      ev.parts.forEach(function (p) {
        if (p.kind === "strike") { teile += 1; erreicht += p.of ? p.n / p.of : 0; return; }
        teile += 1;
        if (p.kind === "kw") {
          var c = t.chk[p.key] || {}, need = c.need || p.hits.length, h = p.hits.filter(function (x) { return x[1]; }).length;
          erreicht += Math.min(1, h / need);
        } else if (p.ok) erreicht += 1;
      });
      max += teile;
      if (viewed) { gesehen.push(t.nr); return; }
      pkt += erreicht;
    });
    return { pkt: pkt, max: max, selbst: selbst, gesehen: gesehen };
  }
  function standSeite() {
    var st = pdfStats();
    return { pkt: st.right, max: st.tot, selbst: (st.unchecked || []).concat(st.open || []), gesehen: st.shown || [], wort: "nicht geprüft oder nicht bearbeitet" };
  }
  function stand() {
    if (typeof T !== "undefined" && typeof evalTask === "function") return standStandard();
    if (typeof pdfStats === "function") return standSeite();
    return null;
  }

  function kasten(d) {
    var s = stand(); if (!s || !s.max) return;
    var W = 210, M = 15, pct = Math.round(s.pkt / s.max * 100), n = note(pct);
    d.setPage(1);
    d.setFillColor(255, 244, 214); d.setDrawColor(176, 136, 20); d.setLineWidth(0.3); d.roundedRect(M, 2, W - 2 * M, 9.5, 1.5, 1.5, "FD");
    d.setFont("C", "bold"); d.setFontSize(9); d.setTextColor(74, 52, 0);
    d.text(clean("Für LMS: " + zahl(s.pkt) + " von " + zahl(s.max) + " Punkten (" + pct + " %) · Notenvorschlag " + n + " – vorläufig"), M + 2, 6);
    d.setFont("C", "normal"); d.setFontSize(7.2);
    var rest = [];
    if (s.gesehen.length) rest.push("Lösung angesehen (0 Punkte): Aufgabe " + liste(s.gesehen));
    if (s.selbst.length) rest.push((s.wort || "selbst bewerten") + ": Aufgabe " + liste(s.selbst));
    var z2 = rest.length ? rest.join(" · ") : "alle Aufgaben automatisch gewertet";
    z2 = d.splitTextToSize(clean(z2 + " · Schlüssel 88/75/62/50 %"), W - 2 * M - 4)[0];
    d.text(z2, M + 2, 9.6);
  }

  function umhuellen(name) {
    var orig = window[name]; if (typeof orig !== "function") return;
    window[name] = function () {
      var J = window.jspdf && window.jspdf.jsPDF, args = arguments, self = this;
      if (!J) return orig.apply(self, args);
      var neu = function () {
        var d = new (Function.prototype.bind.apply(J, [null].concat([].slice.call(arguments))))();
        var o = d.output; d.output = function () { try { kasten(d); } catch (e) {} d.output = o; return o.apply(d, arguments); };
        return d;
      };
      neu.prototype = J.prototype;
      window.jspdf.jsPDF = neu;
      var zurueck = function () { window.jspdf.jsPDF = J; };
      var r; try { r = orig.apply(self, args); } catch (e) { zurueck(); throw e; }
      if (r && typeof r.then === "function") return r.then(function (v) { zurueck(); return v; }, function (e) { zurueck(); throw e; });
      zurueck(); return r;
    };
  }
  umhuellen("buildPdf");
})();
