/* Großzügigere Prüfung der Arbeitsblätter (»Prüfen«-Knopf): Richtige Antworten sollen nicht wegen Schreibweise, Format oder Einheit als falsch gelten.
   Wird NACH der Seiten-Prüfung eingesetzt und ersetzt nur checkField/parseNum/normU/showCheck (die Seite selbst bleibt unverändert).
   Ändert keinen Speicherschlüssel und keine gespeicherte Antwort.

   ZAHLEN (Rechenaufgaben):
     - Irgendeine Zahl in der Antwort darf die richtige sein (nicht nur die letzte): »0,4 A bei 600 Windungen = 240 A« wird erkannt.
     - Tausendertrennung (2.069 / 2 069 / 2'069), Komma oder Punkt, »m2«, »m^2«, »m²«, »qm«, µ und μ werden verstanden.
     - Gleichwertige Einheiten gelten: 2 kA/m = 2000 A/m, 1500 mT = 1,5 T, 4 cm² = 0,0004 m², Vs/m² = T, Tesla = T.
     - Fehlt die Einheit, gilt die Zahl trotzdem als richtig – mit Hinweis »Einheit nicht vergessen«. Eine FALSCHE Einheit bleibt falsch.
     - Gerundete Antworten gelten: 3 statt 3,1 und 83 statt 82,8 (Rundung auf die angeschriebene Stelle), sonst 2 % Spielraum wie bisher.
   TEXTE (Stichwörter):
     - Verneinung (nur wenn im chk-Feld »neg: true« steht): »keine Lorentzkraft«, »nicht abgelenkt« zählt nicht als Treffer. Nur für Aufgaben,
       deren richtige Antwort bejahend ist – bei Aufgaben wie »Kein Alkohol« bleibt die Verneinung aus.
     - ä/ae, ö/oe, ü/ue, ß/ss, Bindestriche (»ovo-lakto«), Tausenderpunkte werden gleichgesetzt.
     - Ein Tippfehler in einem Stichwort (ab 6 Buchstaben) wird verziehen.
     - Pro Aufgabe kann festgelegt werden, wie viele Stichwortgruppen vorkommen müssen (need) und wie viele verschiedene Wörter einer Gruppe (3. Eintrag),
       z. B. »Nenne zwei Gründe«. Korrekturen je Einheit: werkzeug/pruefregeln_korrekturen.json.
   Einbau: python3 werkzeug/pruefung_nachsicht_einbauen.py */
(function () {
  if (window.__nachsicht) return; window.__nachsicht = true;
  if (typeof checkField !== "function" || typeof S === "undefined") return;

  /* ---------- Einheiten ---------- */
  var PRE = { G: 1e9, M: 1e6, k: 1e3, h: 1e2, c: 1e-2, m: 1e-3, "µ": 1e-6, n: 1e-9 };
  var BASE = { A: [0, 0, 0, 1, 1], T: [1, 0, -2, -1, 1], V: [1, 2, -3, -1, 1], Wb: [1, 2, -2, -1, 1], N: [1, 1, -2, 0, 1], W: [1, 2, -3, 0, 1], J: [1, 2, -2, 0, 1],
    "Ω": [1, 2, -3, -2, 1], Hz: [0, 0, -1, 0, 1], m: [0, 1, 0, 0, 1], s: [0, 0, 1, 0, 1], g: [1, 0, 0, 0, 1e-3], l: [0, 3, 0, 0, 1e-3], L: [0, 3, 0, 0, 1e-3] };
  var WORT = [[/Vs/g, "V·s"], [/tesla/gi, "T"], [/ampere/gi, "A"], [/weber/gi, "Wb"], [/volt/gi, "V"], [/newton/gi, "N"], [/ohm/gi, "Ω"], [/quadratmeter|qm/gi, "m2"], [/meter/gi, "m"], [/sekunden?/gi, "s"]];
  function einheitDim(u) {
    u = String(u || "").replace(/\^\(\s*([-−]?\d)\s*\)/g, "$1").replace(/[−–]/g, "-").replace(/\/\(([^()]*)\)/g, function (_, x) { return "/" + x.split(/[·*.\s]+/).filter(Boolean).join("/"); }).replace(/[μ]/g, "µ").replace(/ω/g, "Ω").replace(/²/g, "2").replace(/³/g, "3").replace(/\^/g, "").replace(/\s+/g, "");
    WORT.forEach(function (w) { u = u.replace(w[0], w[1]); });
    if (!u) return null;
    var teile = u.split("/"), dim = [0, 0, 0, 0], f = 1;
    for (var i = 0; i < teile.length; i++) {
      var sign = i === 0 ? 1 : -1, terme = teile[i].split(/[·*.]/).filter(Boolean);
      if (!terme.length) return null;
      for (var j = 0; j < terme.length; j++) {
        var mt = /^([A-Za-zµΩ]+?)(-?\d)?$/.exec(terme[j]); if (!mt) return null;
        var name = mt[1], ex = mt[2] ? parseInt(mt[2], 10) : 1, pre = 1, b = BASE[name];
        if (!b) { var p = name.charAt(0), rest = name.slice(1); if (PRE[p] && BASE[rest]) { pre = PRE[p]; b = BASE[rest]; } else return null; }
        for (var k = 0; k < 4; k++) dim[k] += sign * ex * b[k];
        f *= Math.pow(pre * b[4], sign * ex);
      }
    }
    return { dim: dim, f: f };
  }
  /* Faktor, mit dem eine Zahl in Einheit u in die Einheit soll umgerechnet wird; null = andere Größe (falsche Einheit) */
  function faktor(u, soll) {
    var a = einheitDim(u), b = einheitDim(soll);
    if (!a || !b) return String(u).replace(/\s/g, "").toLowerCase() === String(soll).replace(/\s/g, "").toLowerCase() ? 1 : null;
    for (var i = 0; i < 4; i++) if (a.dim[i] !== b.dim[i]) return null;
    return a.f / b.f;
  }
  function parseZahlen(str) {
    var HOCH = { "⁰": 0, "¹": 1, "²": 2, "³": 3, "⁴": 4, "⁵": 5, "⁶": 6, "⁷": 7, "⁸": 8, "⁹": 9 };
    /* Typografisches Minus (− U+2212, – Halbgeviertstrich, ‒) direkt vor einer Ziffer ist ein Vorzeichen – wie »-« (25.10.2026, Stephans Okay).
       Nur am Anfang bzw. nach Leerzeichen, Klammer, = : ; , + – ein Strich als Trenner (»Antwort – 24 A«, Leerzeichen danach) oder Bereich (»10–20«) bleibt unberührt. */
    var s0 = String(str || "").replace(/(^|[\s(\[{=:;,+])[−–‒](?=\d)/g, "$1-").replace(/[⋅∙•‧]/g, "·").replace(/10([⁻⁺]?)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g, function (_, mi, z) { return "10^" + (mi === "⁻" ? "-" : "") + z.split("").map(function (c) { return HOCH[c]; }).join(""); })
      .replace(/([A-Za-zµμΩ²³])⁻([⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g, function (_, u, z) { return u + "^-" + z.split("").map(function (c) { return HOCH[c]; }).join(""); })
      /* Minuszeichen U+2212, Exponent in Klammern, Nenner in Klammern: »m−2« → »m^-2«, »m^(-2)« → »m^-2«, »N/(A·m)« → »N/A/m« */
      .replace(/([A-Za-zµμΩ²³])[−–](\d)/g, "$1^-$2").replace(/\^\(\s*[-−–]?\s*(\d)\s*\)/g, function (m, z) { return /-|−|–/.test(m) ? "^-" + z : "^" + z; })
      .replace(/([A-Za-zµμΩ²³])\s*\/\s*\(/g, "$1/(")
      .replace(/\/\(([A-Za-zµμΩ²³0-9^\-·*. ]+)\)/g, function (_, x) { return "/" + x.trim().split(/[·*.\s]+/).filter(Boolean).join("/"); })
      /* Einheit in Klammern direkt nach der Zahl: »1500 (mT)« → »1500 mT« (nur wenn der Klammerinhalt eine bekannte Einheit ist; »240 A (oder 0,24 kA)« bleibt unberührt) */
      .replace(/(\d)\s*\(\s*([A-Za-zµμΩ][A-Za-zµμΩ·²³^\-0-9\/ ]{0,16}?)\s*\)/g, function (m, d, u) { return einheitDim(u.replace(/\s+/g, "")) ? d + " " + u.replace(/\s+/g, "") : m; })
      /* Malpunkt und Schrägstrich mit Leerzeichen innerhalb einer Einheit: »A · m^-1« → »A·m^-1«, »kg / A / s²« → »kg/A/s²« */
      .replace(/([A-Za-zµμΩ²³]|\^-?\d)\s*[·*]\s*(?=[A-Za-zµμΩ])/g, "$1·")
      .replace(/([A-Za-zµμΩ²³]|\^-?\d)\s+\/\s+(?=[A-Za-zµμΩ])/g, "$1/")
      /* Einheitenkette mit Leerzeichen: »V s m^-2« → »V·s·m^-2« (nur wenn alle Teile bekannte Einheiten sind) */
      .replace(/(\d\s*)((?:[A-Za-zµμΩ]{1,2}(?:\^-?\d)?)(?:\s+[A-Za-zµμΩ]{1,2}(?:\^-?\d)?){1,3})(?![A-Za-zäöüµμΩ])/g, function (m, a, ch) { var j = ch.split(/\s+/).join("·"); return einheitDim(j) ? a + j : m; })
      /* Einheiten mit Leerzeichen: »A m^-1« → »A·m^-1«, »V s / m²« → »V·s/m²«, »A / m« → »A/m« */
      .replace(/(\d\s*[A-Za-zµμΩ]{1,2})\s+([A-Za-zµμΩ]{1,2}\s*\^\s*-?\d)/g, "$1·$2")
      .replace(/(\d\s*[A-Za-zµμΩ]{1,2})\s+([A-Za-zµμΩ]{1,2})\s*\/\s*(?=[A-Za-zµμΩ])/g, "$1·$2/")
      .replace(/(\d\s*[A-Za-zµμΩ][A-Za-zµμΩ·²³^\-0-9]{0,12})\s*\/\s*(?=[A-Za-zµμΩ])/g, "$1/")
      .replace(/(\d+(?:[.,]\d+)?)\s*[*·x×]\s*10\s*\^?\s*\(?([+-]?\d+)\)?/gi, function (_, a, e) { return String(parseFloat(a.replace(",", ".")) * Math.pow(10, parseInt(e, 10))); })
      .replace(/(\d+(?:[.,]\d+)?)\s*e\s*([+-]?\d+)(?![A-Za-zäöü])/gi, function (_, a, e) { return String(parseFloat(a.replace(",", ".")) * Math.pow(10, parseInt(e, 10))); })
      .replace(/\s+pro\s+/gi, "/").replace(/[  ]/g, " ").replace(/(\d)[ ']+(?=\d{3}(?!\d))/g, "$1");
    var re = /(-?\d+(?:[.,]\d+)*)\s*((?:[A-Za-zµμΩω°%²³]+(?:\^?-?\d)?(?:[·*]?[A-Za-zµμΩω]+[²³]?(?:\^?-?\d)?)*(?:\/[A-Za-zµμΩω]+[²³]?(?:\^?-?\d)?)*)?)/g, out = [], m;
    while ((m = re.exec(s0))) {
      var n = m[1];
      /* 2.069 = Tausenderpunkt; 0.240 und 1.500 sind aber Dezimalzahlen (führende Null) bzw. mehrdeutig → beide Lesarten prüfen */
      var tausend = /^[1-9]\d{0,2}(\.\d{3})+$/.test(n), v2 = null;
      if (tausend) { v2 = parseFloat(n); n = n.replace(/\./g, ""); } else n = n.replace(",", ".");
      var dec = (n.split(".")[1] || "").length, sig = n.replace(".", "").replace(/^0+/, "").replace(dec ? /$^/ : /0+$/, "").length;
      /* Zahl wird ausdrücklich verworfen? (»240 A ist falsch«, »nicht 240 A«, »statt 240 A«) */
      var vor = s0.slice(Math.max(0, m.index - 14), m.index).split(/[,;.!?]/).pop(), rest = s0.slice(m.index + m[0].length), nx = rest.search(/\d/);
      var nach = (nx < 0 ? rest : rest.slice(0, nx)).slice(0, 28).split(/[,;.!?]/)[0];
      /* Verwerfung vor der Zahl: Bezug nur auf den Textteil seit der vorigen Zahl (»24 A sind falsch 240 A sind richtig«: 240 ist NICHT verworfen) */
      var segV = (out.length ? s0.slice(out[out.length - 1].ende, m.index) : s0.slice(0, m.index)).split(/[,;.!?]/).pop();
      var neg = /\b(nicht|kein\w*|statt|anstatt)\s*$/i.test(vor) || /(?<!nicht\s)\bfalsch(e|er|es|en|em)\s+(\w+\s+){0,3}(wäre|ist|lautet|sind|war|wurde)?\s*$/i.test(segV) || /^\s*falsch:?\s*(wäre|ist|lautet|sind|war|wurde)?\s*$/i.test(segV) ||
        (/\bfalsch:?\s*$/i.test(segV) && !(out.length && /^\s*(ist|sind|war|wäre|wurde)\s+falsch/i.test(segV))) /* »Das ist falsch 240 A« */ ||
        /^\s*[×x*·]\s*10\b/i.test(rest) /* Potenzausdruck nicht vollständig erkannt: Mantisse allein nie werten (»240 × 10^x A«) */ ||
        (!(nx >= 0 && /^\s*falsch:?\s*(wäre|ist|lautet|sind|war|wurde)?\s*$/i.test(nach)) /* »240 A falsch sind 24 A«: »falsch« gehört zur NÄCHSTEN Zahl */ &&
          /^\s*(\S+\s+)?(ist|sind|war)?\s*(\S+\s+)?(falsch|nicht richtig|nicht korrekt|stimmt nicht)\b/i.test(nach));
      if (/\bnicht\s+(falsch|unrichtig|inkorrekt)\b/i.test(nach)) neg = false;   // »240 A sind nicht falsch« bestätigt die Zahl
      /* steht »oder« zwischen zwei Zahlen? (»240 A oder 24 A«) → keine eindeutige Antwort */
      var davor = out.length ? s0.slice(out[out.length - 1].ende, m.index) : s0.slice(0, m.index);
      var alt = /\b(oder|entweder|vielleicht|eventuell|evtl\.?)\b/i.test(davor) && !/\d/.test(davor);
      /* Gleichheitszeichen direkt zwischen zwei Zahlen (»240 A = 24 A«): Gleichung, die nur stimmt, wenn beide Seiten gleich sind. Nicht gewertet, wenn eine Seite in einer Rechnung steht (+ − · × / davor oder danach) */
      var zw = out.length ? s0.slice(out[out.length - 1].ende, m.index) : "";
      var eq = !!out.length && /^\s*=\s*$/.test(zw) && !/[+\-−·×*\/x]\s*$/i.test(s0.slice(0, out.length === 1 ? out[0].start : out[out.length - 1].start)) && !/^\s*[+\-−·×*\/^]/.test(s0.slice(m.index + m[0].length));
      out.push({ v: parseFloat(n), v2: v2, u: m[2] || "", dec: dec, sig: sig, neg: neg, alt: alt, eq: eq, start: m.index, ende: m.index + m[0].length });
    }
    return out;
  }
  var parseNum0 = parseNum;
  parseNum = function (str) { var l = parseZahlen(str); return l.length ? l[l.length - 1] : null; };
  var normU0 = normU;
  normU = function (u) { var d = String(u || "").replace(/[μ]/g, "µ"); return normU0(d.replace(/\^2/g, "²")); };

  /* Prüft eine Zahlen-Antwort. Gibt {ok, msg, note} zurück. */
  function numPruefen(text, soll, einheit) {
    var L = parseZahlen(text);
    if (!L.length || L.every(function (x) { return isNaN(x.v); })) return { ok: false, msg: "Keine Zahl gefunden." };
    var zahlOk = false, einheitFalsch = false, einheitFehlt = false;
    /* »240 A oder 24 A«: verschiedene Ergebnisse zur Auswahl = keine eindeutige Antwort */
    var gl = function (x) { var u = (x.u || "").replace(/^%$/, ""), f = einheit && u ? faktor(u, einheit) : 1; if (f === null) return null; var o = [x.v * f]; if (x.v2 != null && !isNaN(x.v2)) o.push(x.v2 * f); return o; };   // mehrere Lesarten (1.500 = 1500 oder 1,5)
    for (var k = 1; k < L.length; k++) if (L[k].alt && !L[k].neg && !L[k - 1].neg) {
      var w1 = gl(L[k - 1]), w2 = gl(L[k]), gleich = !!(w1 && w2) && w1.some(function (a) { return w2.some(function (b) { return Math.abs(a - b) <= Math.max(Math.abs(a), Math.abs(b)) * 0.005; }); });
      if (!gleich) return { ok: false, msg: "Bitte genau ein Ergebnis angeben (nicht »oder«)." };
    }
    /* Widerspruch in einer Gleichung: »240 A = 24 A«, »1,5 T = 15 mT« (beide Seiten haben vergleichbare Einheiten, aber verschiedene Werte, Abweichung über 5 %) */
    for (var e = 1; e < L.length; e++) if (L[e].eq && !L[e].neg && !L[e - 1].neg && L[e].u && L[e - 1].u) {
      var fq = faktor(L[e - 1].u, L[e].u);
      if (fq !== null) { var lw = L[e - 1].v * fq, rw = L[e].v; if (Math.abs(lw - rw) > Math.max(Math.abs(lw), Math.abs(rw)) * 0.05 + 1e-12) return { ok: false, msg: "Die beiden Seiten der Gleichung sind nicht gleich." }; }
    }
    for (var i = 0; i < L.length; i++) {
      var x = L[i]; if (x.neg) continue;
      var u = (x.u || "").replace(/^%$/, ""), f = 1, hatEinheit = !!u;
      if (einheit && hatEinheit) { f = faktor(u, einheit); }
      var lesarten = x.v2 != null && !isNaN(x.v2) ? [x.v, x.v2] : [x.v];   // 1.500 kann 1500 oder 1,5 heißen
      for (var q = 0; q < lesarten.length; q++) {
        var wert = f === null ? lesarten[q] : lesarten[q] * f;
        var rel = soll === 0 ? Math.abs(wert) <= 1e-9 : Math.abs(wert - soll) <= Math.abs(soll) * 0.02;
        /* Rundungsspielraum: eine Stelle der GESCHRIEBENEN Zahl, mit umgerechnet (1000 mT sind 1 T, nicht 1,5 T).
           Zusätzlich höchstens 5 % Abweichung: »3« für 3,1 ist gerundet, »1 T« oder »2 T« für 1,5 T nicht. */
        var halb = (0.5 * Math.pow(10, -x.dec) + 1e-9) * (f === null ? 1 : f);
        var rund = Math.abs(soll) >= 1 && wert !== 0 && Math.abs(wert - soll) <= halb && Math.abs(wert - soll) <= Math.abs(soll) * 0.05;
        if (rel || rund) {
          if (f === null) { einheitFalsch = true; zahlOk = true; }
          else if (einheit && !hatEinheit) { zahlOk = true; einheitFehlt = true; }
          else { return { ok: true }; }
        }
      }
    }
    if (zahlOk && einheitFalsch && !einheitFehlt) return { ok: false, msg: "Zahl stimmt – Einheit prüfen." };
    if (zahlOk && einheitFehlt) return { ok: true, note: "Die Zahl stimmt. Denk daran, immer die Einheit (" + einheit + ") dazuzuschreiben." };
    if (zahlOk) return { ok: false, msg: "Zahl stimmt – Einheit prüfen." };
    return { ok: false, msg: "Das Ergebnis stimmt noch nicht." };
  }
  window.numPruefen = numPruefen;

  /* ---------- Text ---------- */
  function lev(a, b) {
    var m = a.length, n = b.length, i, j, d = [];
    for (i = 0; i <= m; i++) d[i] = [i]; for (j = 1; j <= n; j++) d[0][j] = j;
    for (i = 1; i <= m; i++) for (j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    return d[m][n];
  }
  function varianten(txt) {
    var t = String(txt || "").toLowerCase().replace(/(\d)[.\s'](?=\d{3}(?!\d))/g, "$1");
    var V = [t];
    V.push(t.replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss"));
    V.push(t.replace(/ae/g, "ä").replace(/oe/g, "ö").replace(/ue/g, "ü").replace(/ss/g, "ß"));
    V.push(t.replace(/ä/g, "a").replace(/ö/g, "o").replace(/ü/g, "u").replace(/ß/g, "ss"));
    var o = V.slice(); V.forEach(function (v) { var h = v.replace(/-/g, ""); if (h !== v) o.push(h); });
    return o;
  }
  function einfach(a) { return /^[a-zäöüß ]{6,}$/.test(a); }
  function splitAlt(rx) {   // nur Striche außerhalb von Klammern trennen
    var out = [], d = 0, cur = "";
    for (var i = 0; i < rx.length; i++) { var ch = rx[i];
      if (ch === "\\") { cur += ch + (rx[i + 1] || ""); i++; continue; }
      if (ch === "(" || ch === "[") d++; if (ch === ")" || ch === "]") d--;
      if (ch === "|" && d === 0) { out.push(cur); cur = ""; } else cur += ch; }
    out.push(cur); return out;
  }
  /* Treffer zählt nur, wenn das Stichwort nicht verneint ist (»keine Lorentzkraft«, »nicht abgelenkt«, »bleibt nicht stehen«) */
  function positiv(ra, v, neg) {   // 1 = Treffer, -1 = nur verneinte Treffer, 0 = kein Treffer
    var m, verneint = false; ra.lastIndex = 0;
    while ((m = ra.exec(v))) {
      if (m[0] === "") { ra.lastIndex++; continue; }
      var vor = v.slice(Math.max(0, m.index - 34), m.index).split(/[,;.!?:]/).pop();
      var nein = /\b(nicht|kein\w*|nie|niemals)\s+(\S+\s+){0,2}\S*$/.test(vor) && !/\bnicht\s+nur\s+\S*$/.test(vor);
      /* nachgestellte Verneinung am Satzende: »stoppt nicht.«, »stoppt nie.« (nur bei Feldern mit neg: true; »Lorentzkraft nicht durch Reibung« bleibt gültig) */
      if (!nein && neg && /^\w*\s+(nicht|nie|niemals)\s*([.,;!?]|$)/.test(v.slice(m.index + m[0].length, m.index + m[0].length + 18))) nein = true;
      if (!nein || !neg) return 1; verneint = true;
    }
    return verneint ? -1 : 0;
  }
  function contraTreffer(ra, v) {   // Treffer zählt nicht, wenn davor »nicht/kein/statt/anstatt« steht
    var m; ra.lastIndex = 0;
    while ((m = ra.exec(v))) {
      if (m[0] === "") { ra.lastIndex++; continue; }
      var vor = v.slice(Math.max(0, m.index - 26), m.index).split(/[,;.!?:]/).pop();
      if (!/\b(nicht|kein\w*|nie|niemals|statt|anstatt|ohne)\s+(\S+\s+)?(\S+\s+)?$/.test(vor)) return true;
    }
    return false;
  }
  function treffer(rx, V, W, neg) {
    var re; try { re = new RegExp(rx, "i"); } catch (e) { return 0; }
    var alts = splitAlt(rx), n = 0;
    alts.forEach(function (a) {
      var gefunden = false;
      var vern = false;
      try { var ra = new RegExp(a, "gi"); V.forEach(function (v) { var r = positiv(ra, v, neg); if (r === 1) gefunden = true; else if (r === -1) vern = true; }); } catch (e) {}
      if (!gefunden && !vern && einfach(a)) gefunden = W.some(function (w) { return w.length >= a.length - 1 && lev(w.slice(0, a.length), a) <= 1; });
      if (gefunden) n++;
    });
    return n;   // Anzahl verschiedener passender Alternativen
  }

  var checkField0 = checkField;
  checkField = function (t, key, c) {
    var a = S.a[t.id] || {};
    if (c.num !== undefined) {
      var r = numPruefen(a[key], c.num, c.unit);
      return { ok: r.ok, kind: "num", msg: r.msg, note: r.note, filled: filled(a[key]) };
    }
    if (c.kw) {
      var V = varianten(a[key]), W = []; V.forEach(function (v) { v.split(/[^a-zäöüß0-9]+/).forEach(function (w) { if (w) W.push(w); }); });
      var hits = c.kw.map(function (g) { var n = treffer(g[1], V, W, c.neg); return [g[0], n >= (g[2] || 1)]; });
      /* »contra«: Muster für ausdrücklich FALSCHE Aussagen (nicht verneint, z. B. »läuft immer weiter«) – dann zählt kein Stichwort */
      if (c.contra && c.contra.some(function (rx) { try { return V.some(function (v) { return contraTreffer(new RegExp(rx, "gi"), v); }); } catch (e) { return false; } })) hits = hits.map(function (h) { return [h[0], false]; });
      var need = c.need || hits.length, n = hits.filter(function (h) { return h[1]; }).length;
      return { ok: n >= need, kind: "kw", hits: hits, filled: filled(a[key]) };
    }
    return checkField0(t, key, c);
  };

  /* Hinweis bei richtiger Zahl ohne Einheit */
  var showCheck0 = showCheck;
  showCheck = function (t) {
    showCheck0(t);
    try {
      var r = evalTask(t), fb = document.getElementById("fb_" + t.id);
      if (r && r.ok && fb) r.parts.forEach(function (p) { if (p.note) { var d = document.createElement("div"); d.textContent = "Hinweis: " + p.note; fb.appendChild(d); } });
    } catch (e) {}
  };

  /* ---------- Korrekturen einzelner Regeln (je Einheit) ---------- */
  var K = window.__CHK_KORREKTUR || {};
  Object.keys(K).forEach(function (id) {
    var t = T.filter(function (x) { return x.id === id; })[0]; if (!t || !t.chk) return;
    Object.keys(K[id]).forEach(function (key) { t.chk[key] = Object.assign({}, t.chk[key] || {}, K[id][key]); });
  });
})();
