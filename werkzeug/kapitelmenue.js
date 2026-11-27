/* Kapitel-Menü statt Wischleiste auf Theorie-Seiten (Stephan, 15.11.2026).
   Baut die Leiste <nav class="toc"><div>…Links…</div></nav> beim Laden um:
   oben fest »☰ Kapitel« · aktuelles Kapitel · Knopf zum Arbeitsblatt; ein Tipp auf »Kapitel« zeigt ALLE Kapitel umbrechend.
   Ohne JavaScript bleibt die alte Leiste – nichts geht verloren. Ändert keine Antworten und keine Speicherschlüssel. */
(function () {
  var nav = document.querySelector("nav.toc");
  if (!nav || nav.classList.contains("mitmenue")) return;
  var alt = nav.querySelector("div"); if (!alt) return;
  var alle = [].slice.call(alt.querySelectorAll("a"));
  if (alle.length < 2) return;
  var ab = alle.filter(function (a) { return /aufgaben\.html|#weiter$/.test(a.getAttribute("href") || ""); }).pop();
  var kap = alle.filter(function (a) { return a !== ab && (a.getAttribute("href") || "").charAt(0) === "#"; });

  var bar = document.createElement("div"); bar.className = "tocbar";
  var btn = document.createElement("button"); btn.type = "button"; btn.className = "tocbtn"; btn.textContent = "☰ Kapitel";
  btn.setAttribute("aria-expanded", "false"); btn.setAttribute("aria-controls", "tocpanel");
  var cur = document.createElement("span"); cur.className = "toccur"; cur.setAttribute("aria-live", "polite");
  bar.append(btn, cur);
  if (ab) { var abk = document.createElement("a"); abk.className = "tocab"; abk.href = ab.getAttribute("href");
    abk.textContent = /aufgaben\.html/.test(ab.getAttribute("href")) ? "Arbeitsblatt" : ab.textContent;   /* heißt für die Kadetten überall »Arbeitsblatt« */ bar.append(abk); }
  var panel = document.createElement("div"); panel.className = "tocpanel"; panel.id = "tocpanel"; panel.hidden = true;
  kap.forEach(function (a) { panel.append(a); });
  alt.replaceWith(bar); nav.append(panel); nav.classList.add("mitmenue");

  function zu() { panel.hidden = true; btn.setAttribute("aria-expanded", "false"); btn.textContent = "☰ Kapitel"; }
  btn.addEventListener("click", function () {
    var auf = panel.hidden; panel.hidden = !auf; btn.setAttribute("aria-expanded", String(auf)); btn.textContent = auf ? "✕ Schließen" : "☰ Kapitel";
  });
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") zu(); });
  panel.addEventListener("click", function (ev) {
    var a = ev.target.closest("a"); if (!a) return; zu();
    var h = a.getAttribute("href"), z = document.getElementById(h.slice(1)); if (!z) return;
    ev.preventDefault(); try { history.replaceState(null, "", h); } catch (e) {}
    var hin = function () { window.scrollTo({ top: z.getBoundingClientRect().top + window.scrollY - nav.getBoundingClientRect().bottom - 8, behavior: "instant" }); };
    hin(); setTimeout(hin, 350); setTimeout(hin, 1000);   /* nachladende Bilder verschieben sonst das Ziel */
  });
  var ziele = kap.map(function (a) { return document.getElementById((a.getAttribute("href") || "").slice(1)); });
  function markiere() {
    var y = nav.getBoundingClientRect().bottom + 24, best = 0;
    ziele.forEach(function (z, i) { if (z && z.getBoundingClientRect().top <= y) best = i; });
    kap.forEach(function (a, i) { a.classList.toggle("aktiv", i === best); });
    cur.textContent = kap[best] ? kap[best].textContent : "";
  }
  window.addEventListener("scroll", markiere, { passive: true }); window.addEventListener("resize", markiere); markiere();

  var st = document.createElement("style");
  st.textContent =
    "nav.toc.mitmenue div.tocbar{display:flex;align-items:center;gap:8px;overflow:visible;padding:8px 12px;max-width:720px;margin:0 auto}" +
    "nav.toc .tocbtn{font:inherit;font-size:16px;font-weight:700;color:#3B4A2F;background:#fff;border:0;border-radius:999px;padding:8px 14px;min-height:40px;cursor:pointer;white-space:nowrap}" +
    "nav.toc .toccur{flex:1;min-width:0;color:#fff;font-weight:700;font-size:16px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}" +
    "nav.toc a.tocab{flex:0 0 auto;min-height:44px;display:inline-flex;align-items:center;background:#7FA83A;border-color:#7FA83A;color:#fff}" +
    "nav.toc.mitmenue div.tocpanel{display:flex;flex-wrap:wrap;gap:6px;overflow:visible;padding:2px 12px 12px;max-width:720px;margin:0 auto}" +
    "nav.toc.mitmenue div.tocpanel[hidden]{display:none}" +
    "nav.toc div.tocpanel a{font-size:16px;padding:8px 14px}" +
    "nav.toc div.tocpanel a.aktiv{background:#fff;color:#3B4A2F}";
  document.head.append(st);
})();
