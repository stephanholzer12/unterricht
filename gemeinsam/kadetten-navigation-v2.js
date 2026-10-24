/* Kadettenansicht v2. Ausschließlich Navigation; keine Speicherzugriffe. */
(function () {
  'use strict';
  var suche = document.getElementById('ks-themen-suche'), offenVorSuche = new Map();
  function normal(s) { return String(s).toLowerCase().replace(/ß/g, 'ss').normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
  if (suche) {
    suche.addEventListener('input', function () {
      var teile = normal(suche.value).trim().split(/\s+/).filter(Boolean), n = 0;
      document.querySelectorAll('[data-ks-thema]').forEach(function (thema) {
        var text = normal(thema.dataset.ksThema);
        thema.hidden = !teile.every(function (t) { return text.indexOf(t) !== -1; });
        if (!thema.hidden) n++;
      });
      document.querySelectorAll('.ks-themenblock').forEach(function (block) {
        block.hidden = !block.querySelector('[data-ks-thema]:not([hidden])');
        if (teile.length && !block.hidden) { if (!offenVorSuche.has(block)) offenVorSuche.set(block, block.open); block.open = true; }
      });
      if (!teile.length) { offenVorSuche.forEach(function (offen, block) { block.open = offen; }); offenVorSuche.clear(); }
      document.getElementById('ks-themen-treffer').textContent = teile.length ? (n ? n + (n === 1 ? ' Thema gefunden' : ' Themen gefunden') : 'Kein Thema gefunden. Versuche ein kürzeres Wort.') : '';
    });
  }
  function ankerOeffnen() {
    var id; try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { return; }
    var ziel = id && document.getElementById(id);
    if (!ziel) return;
    if (ziel.matches('[data-ks-thema]') && suche && suche.value) { suche.value = ''; suche.dispatchEvent(new Event('input')); }
    var block = ziel.closest('details.ks-themenblock');
    if (block) { block.open = true; ziel.scrollIntoView(); }
  }
  window.addEventListener('hashchange', ankerOeffnen); ankerOeffnen();
  var nav = document.querySelector('.ks-topnav');
  if (nav) {
    function hoehe() { document.documentElement.style.setProperty('--ks-topnav-hoehe', (nav.getBoundingClientRect().height || 44) + 'px'); }
    hoehe(); if (typeof ResizeObserver !== 'undefined') new ResizeObserver(hoehe).observe(nav);
  }
})();
