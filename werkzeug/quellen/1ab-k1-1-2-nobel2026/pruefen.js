// ---------- Prüfen: Auswertung pro Aufgabe, Versuche zählen ----------
const norm = (s) => String(s == null ? "" : s).toLowerCase().replace(/dezember/g, "12").replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss").replace(/[^a-z0-9]/g, "");
function lev(a, b) {
  let p = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) { const c = [i]; for (let j = 1; j <= b.length; j++) c[j] = Math.min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); p = c; }
  return p[b.length];
}
function sameWord(x, target) { const a = norm(x), b = norm(target); if (!a) return false; if (a === b) return true; return b.length >= 6 && lev(a, b) <= 1; }
function hasKw(x, kws) {
  const n = norm(x); if (!n) return false;
  const words = String(x).toLowerCase().split(/[^a-zäöüß0-9]+/).map(norm).filter(Boolean);
  return kws.some(k => { const nk = norm(k); return n.includes(nk) || (nk.length >= 5 && words.some(w => w.length >= 4 && lev(w, nk) <= (nk.length >= 8 ? 2 : 1))); });
}
function calcA(x) { const s = String(x).toLowerCase().replace(/[\s. ]/g, ""); return /180000000000000/.test(s) || /1,8(\*|x|·|⋅|×)?10\^?(14|¹⁴)/.test(s) || /180billionen/.test(s); }

// Alle Antworten einer Aufgabe als Liste prüfbarer Einträge
function evalItems(t) {
  const a = S.a[t.id] || {}, K = t.key || {}, out = [];
  const ans = (x) => filled(x) ? String(x).trim() : "";
  if (t.type === "gaps") t.sents.forEach((parts, si) => parts.forEach(p => {
    if (typeof p === "string") return;
    const x = ans(a["g" + p]);
    out.push({ k: "g" + p, kind: "auto", has: !!x, val: x, ok: !!x && K.acc[p].some(z => sameWord(x, z)), sel: "#" + t.id + "_g" + p,
      text: (si + 1) + ". " + parts.map(q => typeof q === "string" ? q : "[" + v(a["g" + q]) + "]").join(""), solLine: (si + 1) + ". " + K.sol[p], sol: K.sol[p] });
  }));
  if (t.type === "assign") t.rows.forEach((r, i) => t.cols.forEach((c, j) => {
    const k = "r" + i + "c" + j, x = ans(a[k]);
    out.push({ k, kind: "kw", has: !!x, val: x, ok: !!x && hasKw(x, K.kw[i][j]), sel: "#" + t.id + "_" + k, text: r + " – " + c + ": " + (x || "?"), solLine: r + " – " + c + ": " + K.sol[i][j], sol: K.sol[i][j] });
  }));
  if (t.type === "multichoose") t.items.forEach((it, i) => {
    const k = "c" + i, sel = a[k] || [], names = sel.map(o => t.opts[o]);
    out.push({ k, kind: "auto", has: sel.length > 0, val: names.join("|"), ok: sel.length > 0 && names.every(n => K.acc[i].includes(n)), row: i, text: it + " → " + (names.join(", ") || "?"), solLine: it + " → " + K.sol[i], sol: K.sol[i] });
  });
  if (t.type === "choose") t.items.forEach((it, i) => {
    const k = "c" + i, x = a[k];
    out.push({ k, kind: "auto", has: x != null, val: String(x), ok: x === K.sol[i], row: i, text: it + ": " + (x != null ? t.opts[x] : "?"), solLine: it + " → " + t.opts[K.sol[i]], sol: t.opts[K.sol[i]] });
  });
  if (t.type === "order") t.items.forEach((it, i) => {
    const k = "o" + i, x = ans(a[k]);
    out.push({ k, kind: "auto", has: !!x, val: x, ok: !!x && Number(x) === K.sol[i], sel: "#" + t.id + "_" + k, text: (x || "?") + " – " + it, solLine: it + " → Nr. " + K.sol[i], sol: "Nr. " + K.sol[i] });
  });
  if (t.type === "myth") t.items.forEach((it, i) => {
    const k = "c" + i, x = a[k], r = ans(a["r" + i]);
    out.push({ k, kind: "auto", has: x != null, val: String(x), ok: x != null && t.opts[x] === K.sol[i], row: i, text: "»" + it + "«: " + (x != null ? t.opts[x] : "?"), solLine: "»" + it + "« → " + K.sol[i] + " – " + K.why[i], sol: K.sol[i] + " – " + K.why[i] });
    out.push({ k: "r" + i, kind: "manual", has: !!r, val: r, ok: null, text: "Begründung: " + (r || "?"), solLine: "" });
  });
  if (t.type === "multi" && t.id !== "a8") t.parts.forEach(([k, lab], idx) => {
    const x = ans(a[k]);
    out.push({ k, kind: "kw", has: !!x, val: x, ok: !!x && (k === "a" ? calcA(x) : hasKw(x, K.kw[k])), sel: "#" + t.id + "_" + k, text: lab + "\n" + (x || "?"), solLine: lab + " → " + K.sol[idx], sol: K.sol[idx] });
  });
  if (t.type === "multi" && t.id === "a8") {
    const x = ans(a.t);
    out.push({ k: "t", kind: "manual", has: !!x, val: x, ok: null, text: x || "?", solLine: "Beispiel: " + K.sol });
  }
  return out;
}

const countable = (items) => items.filter(it => it.kind !== "manual");
function taskState(t) {
  const items = evalItems(t), c = S.chk[t.id] || { items: {}, shown: false }, auto = countable(items);
  let right = 0, att = 0, first = 0, answered = 0;
  auto.forEach(it => { const rec = c.items[it.k]; if (it.has) { answered++; if (it.ok) right++; } if (rec) { att = Math.max(att, rec.n); if (rec.first) first++; } });
  return { items, auto, c, right, att, first, answered, total: auto.length, shown: !!c.shown, checked: Object.keys(c.items).length > 0 };
}

function runCheck(t) {
  const c = (S.chk[t.id] = S.chk[t.id] || { items: {}, shown: false });
  evalItems(t).forEach(it => {
    if (it.kind === "manual" || !it.has) return;
    const rec = c.items[it.k];
    if (!rec) c.items[it.k] = { n: 1, first: it.ok, val: it.val };
    else if (rec.val !== it.val) { rec.n++; rec.val = it.val; }
  });
  save(); paintTask(t);
}

function nodeFor(card, it) {
  if (it.sel) return card.querySelector(it.sel);
  return card.querySelectorAll(".rows > .row")[it.row] || null;
}

function paintTask(t) {
  const card = $("#card_" + t.id); if (!card) return;
  const st = taskState(t), fb = card.querySelector(".fb"), sb = card.querySelector(".solbtn"), box = card.querySelector(".solbox"), pb = card.querySelector(".pruefbtn");
  card.querySelectorAll(".r-ok,.r-bad").forEach(n => n.classList.remove("r-ok", "r-bad"));
  let right = 0, shown = 0;
  st.auto.forEach(it => {
    const rec = st.c.items[it.k];
    if (rec && it.has && rec.val === it.val) { shown++; if (it.ok) right++; const nd = nodeFor(card, it); if (nd) nd.classList.add(it.ok ? "r-ok" : "r-bad"); }
  });
  const manualOnly = st.total === 0;
  if (pb) pb.disabled = manualOnly ? !st.items.some(i => i.has) : st.answered === 0;
  if (manualOnly) {
    fb.className = "fb info"; fb.textContent = st.shown ? "Beispiel angezeigt. Deine Lehrkraft liest deine Antwort." : (st.items.some(i => i.has) ? "Deine Lehrkraft liest deine Antwort. Du kannst jetzt ein Beispiel ansehen." : "Schreib deine Antwort – deine Lehrkraft liest sie.");
  } else if (!shown) {
    fb.className = "fb info"; fb.textContent = st.answered ? "Drück auf Prüfen." : "";
  } else {
    const all = right === st.total, rest = st.total - shown;
    fb.className = "fb " + (all ? "ok" : "bad");
    fb.textContent = (all ? "Richtig! " : right + " von " + st.total + " richtig. ") + "Versuch " + st.att + (rest > 0 && !all ? " · " + rest + " noch ungeprüft" : "") + (st.shown ? " · Lösung angezeigt" : "");
    if (!all && st.att < 2) fb.textContent += " – verbessere die roten Felder und prüfe nochmal.";
  }
  const showSolBtn = manualOnly ? (!st.shown && st.items.some(i => i.has)) : (!st.shown && st.att >= 2 && shown && right < st.total);
  if (sb) sb.hidden = !showSolBtn;
  if (box) {
    box.hidden = !st.shown;
    if (st.shown && !box.childElementCount) {
      box.append(el("strong", { text: "Lösung" }));
      st.items.forEach(it => { if (it.solLine && (manualOnly || it.kind === "manual" || !it.ok || true)) box.append(el("div", { text: it.solLine })); });
    }
  }
}

function addCheck(card, t) {
  const probe = evalItems(t), manualOnly = countable(probe).length === 0;
  const pb = el("button", { class: "btn small pruefbtn", type: "button", text: manualOnly ? "Speichern" : "Prüfen" });
  pb.hidden = manualOnly;
  const sb = el("button", { class: "btn secondary small solbtn", type: "button", text: manualOnly ? "Beispiel ansehen" : "Lösung anzeigen", hidden: "" });
  const fb = el("span", { class: "fb info", role: "status", "aria-live": "polite" });
  pb.addEventListener("click", () => runCheck(t));
  sb.addEventListener("click", () => { const c = (S.chk[t.id] = S.chk[t.id] || { items: {}, shown: false }); c.shown = true; save(); paintTask(t); });
  card.append(el("div", { class: "chk" }, pb, fb, sb), el("div", { class: "solbox", hidden: "" }));
}
function unchecked() {
  const l = T.filter(t => { const s = taskState(t); return s.total > 0 && s.answered > 0 && !s.checked; }).map(t => t.nr);
  return l.length ? " Noch nicht geprüft: Aufgabe " + l.join(", ") + "." : "";
}
