// Kalender und Vorbereitung der Lösungsseite K2.1: Prof. HOLZER trägt Termine, Doppelstunden und Referate selbst ein (nur in diesem Browser gespeichert).
(function () {
  'use strict';
  var D = JSON.parse(document.getElementById('k-daten').textContent);
  var TKEY = 'k21-termine-v1', T = [], offen = new Set(), nextId = 1, WT = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'];
  var OPT = [1, 2, 3, 4, 5, 6].map(function (n) { return [String(n), 'Stunde ' + n]; })
    .concat([1, 2, 3, 4, 5].map(function (n) { return [n + '+' + (n + 1), 'Doppelstunde ' + n + '+' + (n + 1)]; }));

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function teile(s) { return String(s).split('+').map(Number).filter(Boolean); }
  function dat(d) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(d || ''); if (!m) return null; var x = new Date(+m[1], +m[2] - 1, +m[3], 12); return isNaN(x) ? null : x; }
  function kurz(d) { var x = dat(d); return x ? WT[x.getDay()] + ' ' + x.getDate() + '.' + (x.getMonth() + 1) + '.' : 'Datum fehlt'; }
  function heuteIso() { var n = new Date(); return n.getFullYear() + '-' + String(n.getMonth() + 1).padStart(2, '0') + '-' + String(n.getDate()).padStart(2, '0'); }
  function lade() {
    var a = null; try { a = JSON.parse(localStorage.getItem(TKEY) || 'null'); } catch (e) {}
    if (!Array.isArray(a)) a = D.term;
    T = a.map(function (x) { return { id: nextId++, k: String(x.k || D.kl[0]), d: String(x.d || ''), h: String(x.h || ''), s: String(x.s || '1'), r: String(x.r || '') }; });
  }
  function speichern() {
    try { localStorage.setItem(TKEY, JSON.stringify(T.map(function (t) { return { k: t.k, d: t.d, h: t.h, s: t.s, r: t.r }; }))); } catch (e) { if (window.warnung) window.warnung(); }
  }
  function sortiert() { return T.slice().sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : (a.k < b.k ? -1 : a.k > b.k ? 1 : 0); }); }
  function inp(type, val, ph, fn) { var i = document.createElement('input'); i.type = type; i.value = val; if (ph) i.placeholder = ph; i.addEventListener('change', function () { fn(i.value); }); return i; }
  function sel(opts, val, fn) {
    var s = document.createElement('select');
    opts.forEach(function (o) { var op = document.createElement('option'); op.value = o[0]; op.textContent = o[1]; if (o[0] === val) op.selected = true; s.append(op); });
    s.addEventListener('change', function () { fn(s.value); }); return s;
  }
  function feld(txt, c) { var l = el('label', 'fk'); l.append(el('span', 'klein', txt), c); return l; }
  function set(t, k, v) { t[k] = v; offen.add(t.id); speichern(); zeichne(); }

  function ablauf(t) {
    var rows = D['var'][t.s + (t.r.trim() ? 'R' : '')];
    if (!rows) return el('p', 'klein', 'Für diese Stundenfolge gibt es keinen fertigen Ablauf (möglich: Stunde 1 bis 6 oder Doppelstunde 1+2 bis 5+6).');
    var w = el('div', 'scroll'), tb = el('table'), t0 = 0;
    rows.forEach(function (r) {
      var tr = el('tr', r[1] === 0 ? 'weg' : (r[3] === 'referat' ? 'ref' : '')), td = el('td');
      tr.append(el('td', 'num', r[1] === 0 ? '–' : t0 + '–' + (t0 + r[1])));
      td.append(document.createTextNode(r[0]));
      if (r[2]) td.append(' ', el('span', 'chip', 'ohne Handy'));
      if (r[4]) td.append(' ', el('span', 'chip rot', r[4]));
      tr.append(td); tb.append(tr); t0 += r[1];
    });
    w.append(tb); w.append(el('p', 'klein', 'Summe ' + t0 + ' Minuten' + (t.s.indexOf('+') > 0 ? ' (Doppelstunde einschließlich 5 Minuten Pause)' : '')));
    return w;
  }
  function bruecke(t) {
    var q = t.r.toLowerCase(), b = null;
    D.bruecken.forEach(function (x) { if (!b && x.such.some(function (w) { return q.indexOf(w) >= 0; })) b = x; });
    b = b || D.allg;
    var box = el('div', 'box fach'); box.append(el('b', 'k', 'Verbindung zur Einheit · 1 Minute nach dem Referat'));
    box.append(el('p', null, b.frage));
    var p = el('p'); p.append(el('b', null, 'Kurzantwort: '), document.createTextNode(b.antwort)); box.append(p);
    box.append(el('p', 'klein', 'Passt zu: ' + b.wo));
    return box;
  }
  function karte(t, jetzt) {
    var det = el('details', 'card' + (jetzt ? ' jetzt' : '')), sm = el('summary'), tl = teile(t.s);
    if (offen.has(t.id) || (jetzt && !offen.size)) det.open = true;
    det.addEventListener('toggle', function () { if (det.open) offen.add(t.id); else offen.delete(t.id); });
    sm.append(el('span', 'nr', t.s), el('span', 'ttl', kurz(t.d) + ' · ' + t.k + (t.h ? ' · ' + t.h : '')));
    tl.forEach(function (n) { if (D.std[n]) sm.append(el('span', 'tag', D.std[n].marke)); });
    if (t.r.trim()) sm.append(el('span', 'tag zus', 'Referat: ' + t.r.trim()));
    if (jetzt) sm.append(el('span', 'tag bew', 'als Nächstes'));
    det.append(sm);
    var b = el('div', 'body'), g = el('div', 'fgrid');
    g.append(feld('Datum', inp('date', t.d, '', function (v) { set(t, 'd', v); })),
             feld('Klasse', sel(D.kl.map(function (k) { return [k, k]; }), t.k, function (v) { set(t, 'k', v); })),
             feld('Schulstunde (frei)', inp('text', t.h, 'z. B. 7.–8. Std.', function (v) { set(t, 'h', v); })),
             feld('Stunde der Einheit', sel(OPT, t.s, function (v) { set(t, 's', v); })),
             feld('Referat (Thema, leer = keines)', inp('text', t.r, 'z. B. Vulkane', function (v) { set(t, 'r', v); })));
    b.append(g);
    b.append(el('h3', null, 'Ablauf an diesem Tag' + (t.r.trim() ? ' (mit Referat)' : '')));
    b.append(ablauf(t));
    if (tl.length === 2 && D.doppel[t.s]) b.append(el('p', 'warnline', D.doppel[t.s]));
    if (t.r.trim()) {
      if (tl.length === 1 && D.kuerz[tl[0]]) { var w = el('p', 'warnline'); w.append(el('b', null, 'Das ändert sich wegen des Referats: '), document.createTextNode(D.kuerz[tl[0]])); b.append(w); }
      b.append(bruecke(t));
    }
    var br = tl.map(function (n) { return D.std[n] ? 'Stunde ' + n + ': ' + D.std[n].brauchst : ''; }).filter(Boolean);
    var vm = tl.reduce(function (s, n) { return s + (D.std[n] ? D.std[n].vorb : 0); }, 0);
    if (br.length) { var p = el('p', 'klein'); p.append(el('b', null, 'Du brauchst: '), document.createTextNode(br.join(' · ') + ' · Vorbereitung ca. ' + vm + ' min')); b.append(p); }
    var del = el('button', 'btn ghost', 'Termin löschen'); del.type = 'button';
    del.addEventListener('click', function () {
      if (del.dataset.sicher) { T = T.filter(function (x) { return x.id !== t.id; }); speichern(); zeichne(); return; }
      del.dataset.sicher = '1'; del.textContent = 'Wirklich löschen? Nochmal tippen'; setTimeout(function () { delete del.dataset.sicher; del.textContent = 'Termin löschen'; }, 4000);
    });
    b.append(del); det.append(b); return det;
  }
  function pruefen() {
    var msg = [];
    D.kl.forEach(function (k) {
      var cnt = {}, fol = [], mine = sortiert().filter(function (t) { return t.k === k; });
      mine.forEach(function (t) { teile(t.s).forEach(function (n) { cnt[n] = (cnt[n] || 0) + 1; fol.push(n); }); });
      var fehlt = [], dopp = [], i;
      for (i = 1; i <= 6; i++) { if (!cnt[i]) fehlt.push(i); else if (cnt[i] > 1) dopp.push(i); }
      var teil = [];
      if (fehlt.length) teil.push('Stunde ' + fehlt.join(', ') + ' fehlt noch');
      if (dopp.length) teil.push('Stunde ' + dopp.join(', ') + ' kommt mehrfach vor');
      for (i = 1; i < fol.length; i++) { if (fol[i] < fol[i - 1]) { teil.push('die Reihenfolge der Stunden stimmt nach dem Datum nicht'); break; } }
      if (teil.length) msg.push(k + ': ' + teil.join('; ') + '.');
    });
    if (T.some(function (t) { return !dat(t.d); })) msg.push('Mindestens ein Termin hat kein gültiges Datum.');
    return msg;
  }
  function vorsprung() {
    var ende = {}, ok = true;
    D.kl.forEach(function (k) {
      T.forEach(function (t) { if (t.k === k && teile(t.s).indexOf(6) >= 0 && dat(t.d)) { if (!ende[k] || t.d > ende[k]) ende[k] = t.d; } });
      if (!ende[k]) ok = false;
    });
    var p = document.getElementById('k-vorsprung');
    if (!ok || D.kl.length < 2) { p.hidden = true; return; }
    var a = D.kl.slice().sort(function (x, y) { return ende[x] < ende[y] ? -1 : ende[x] > ende[y] ? 1 : 0; }), tage = Math.round((dat(ende[a[1]]) - dat(ende[a[0]])) / 86400000);
    p.hidden = false;
    p.textContent = tage >= 3
      ? a[0] + ' ist am ' + kurz(ende[a[0]]) + ' mit Stunde 6 fertig, ' + a[1] + ' erst am ' + kurz(ende[a[1]]) + ' (' + tage + ' Tage später). Gib der ' + a[0] + ' vor dem nächsten Thema einen Ausgleichsbaustein (Reiter »Ausgleich«), dann sind beide ungefähr gleich weit.'
      : 'Beide Klassen sind ungefähr gleichzeitig fertig (' + a[0] + ' ' + kurz(ende[a[0]]) + ', ' + a[1] + ' ' + kurz(ende[a[1]]) + ') – ein Ausgleich ist nicht nötig.';
  }
  function vorb() {
    var cont = document.getElementById('vb-karten'); if (!cont) return;
    var heute = heuteIso(), ks = [].slice.call(cont.querySelectorAll('details.tag-karte'));
    ks.forEach(function (c) {
      var m = T.filter(function (x) { return x.k === c.dataset.k && teile(x.s).indexOf(+c.dataset.n) >= 0; }).sort(function (a, b) { return a.d < b.d ? -1 : 1; })[0];
      c._d = m && dat(m.d) ? m.d : '9999'; c.hidden = !m;
      c.querySelector('.dt').textContent = m ? ' · ' + kurz(m.d) + (m.h ? ' · ' + m.h : '') : '';
    });
    ks.sort(function (a, b) { return a._d < b._d ? -1 : a._d > b._d ? 1 : (a.dataset.k + a.dataset.n).localeCompare(b.dataset.k + b.dataset.n); });
    ks.forEach(function (c) { cont.append(c); });
    var nx = ks.filter(function (c) { return !c.hidden && c._d >= heute; })[0];
    ks.forEach(function (c) { c.open = (c === nx); });
    [].forEach.call(document.querySelectorAll('[data-vs]'), function (s) {
      var n = +s.dataset.vs, m = sortiert().filter(function (x) { return teile(x.s).indexOf(n) >= 0 && dat(x.d); })[0];
      s.textContent = s.dataset.basis + (m ? ' → ' + kurz(m.d) + ' (' + m.k + ')' : '');
    });
  }
  function zeichne() {
    var liste = document.getElementById('k-liste'), s = sortiert(), heute = heuteIso(), nx = s.filter(function (t) { return t.d >= heute; })[0];
    liste.textContent = '';
    s.forEach(function (t) { liste.append(karte(t, t === nx)); });
    if (!s.length) liste.append(el('p', 'leer', 'Noch kein Termin. Mit »+ Termin« anlegen.'));
    var w = document.getElementById('k-warn'), m = pruefen();
    w.hidden = !m.length; w.textContent = ''; if (m.length) { w.append(el('b', 'k', 'Bitte prüfen')); m.forEach(function (x) { w.append(el('p', null, x)); }); }
    vorsprung(); vorb();
  }
  document.getElementById('k-neu').addEventListener('click', function () {
    var l = sortiert(), last = l.length ? l[l.length - 1] : null, id = nextId;
    T.push({ id: nextId++, k: last ? last.k : D.kl[0], d: heuteIso(), h: '', s: '1', r: '' }); offen.add(id); speichern(); zeichne();
  });
  var rs = document.getElementById('k-reset');
  rs.addEventListener('click', function () {
    if (rs.dataset.sicher) { try { localStorage.removeItem(TKEY); } catch (e) {} offen.clear(); lade(); zeichne(); delete rs.dataset.sicher; rs.textContent = 'Standard wiederherstellen'; return; }
    rs.dataset.sicher = '1'; rs.textContent = 'Wirklich? Eigene Änderungen gehen verloren – nochmal tippen';
    setTimeout(function () { delete rs.dataset.sicher; rs.textContent = 'Standard wiederherstellen'; }, 4000);
  });
  lade(); zeichne();
})();
