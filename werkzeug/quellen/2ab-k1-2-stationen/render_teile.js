function renderTask(t) {
  const card = el("section", { class: "card", id: "card_" + t.id });
  card.append(el("div", { class: "head" },
    el("span", { class: "nr" }, el("span", { class: "check", "aria-hidden": "true", text: "✓" }), "Aufgabe " + t.nr + " · Stunde " + t.h, t.tag ? el("span", { class: "tag zusatz", text: t.tag }) : null),
    el("span", { class: "pill theory", text: t.src })));
  card.append(el("h2", { text: t.title }));
  card.append(el("p", { class: "q", text: t.q }));
  if (t.hint) card.append(el("p", { class: "hint", text: t.hint }));
  const chips = (key, opts, multi, aria) => {
    const btns = opts.map(o => el("button", { class: "chip", type: "button", text: o, "aria-pressed": "false" }));
    const cur = () => A(t.id)[key];
    const paint = () => btns.forEach((b, oi) => b.setAttribute("aria-pressed", String(multi ? (cur() || []).includes(oi) : cur() === oi)));
    btns.forEach((b, oi) => b.addEventListener("click", () => {
      if (multi) { const a = (cur() || []).slice(); const k = a.indexOf(oi); if (k >= 0) a.splice(k, 1); else a.push(oi); A(t.id)[key] = a.sort(); }
      else A(t.id)[key] = cur() === oi ? undefined : oi;
      paint(); update(); save(); }));
    paint();
    return el("div", { class: "choose", role: "group", "aria-label": aria }, ...btns);
  };
  if (t.type === "gaps") {
    const box = el("div", { class: "rows" });
    t.sents.forEach((parts, si) => {
      const p = el("div", { class: "sent2" }); p.append((si + 1) + "  ");
      parts.forEach(part => { if (typeof part === "string") p.append(part); else p.append(input(t.id, "g" + part, { cls: "gap", aria: "Lücke " + (part + 1) })); });
      box.append(p);
    });
    card.append(box);
  }
  if (t.type === "assign") {
    const box = el("div", { class: "rows" });
    t.rows.forEach((r, i) => box.append(el("div", { class: "row" }, el("div", { class: "stoff", text: r }),
      ...t.cols.map((c, j) => labeled(t.id, "r" + i + "c" + j, c, { multi: j > 0 })))));
    card.append(box);
  }
  if (t.type === "multichoose" || t.type === "choose") {
    const box = el("div", { class: "rows" });
    t.items.forEach((it, i) => box.append(el("div", { class: "row" }, el("div", { text: it }), chips("c" + i, t.opts, t.type === "multichoose", it))));
    card.append(box);
  }
  if (t.type === "order") {
    const box = el("div", { class: "rows" });
    const nums = t.items.map((_, k) => String(k + 1));
    t.items.forEach((it, i) => box.append(el("div", { class: "row" }, el("div", { text: it }), el("div", {}, el("label", { class: "lbl", text: "Schritt Nr." }), select(t.id, "o" + i, nums, "Schritt Nr. für: " + it)))));
    card.append(box);
  }
  if (t.type === "myth") {
    const box = el("div", { class: "rows" });
    t.items.forEach((it, i) => box.append(el("div", { class: "row" }, el("div", { class: "stoff", text: "»" + it + "«" }), chips("c" + i, t.opts, false, it),
      labeled(t.id, "r" + i, "Begründung", {}))));
    card.append(box);
  }
  if (t.type === "multi") t.parts.forEach(([k, lab]) => card.append(labeled(t.id, k, lab, { multi: true })));
  addCheck(card, t);
  return card;
}
//----TEIL----
function isDone(t) {
  const a = S.a[t.id] || {};
  if (t.type === "gaps") return t.sents.every(p => p.filter(x => typeof x !== "string").every(g => filled(a["g" + g])));
  if (t.type === "assign") return t.rows.every((_, i) => t.cols.every((_, j) => filled(a["r" + i + "c" + j])));
  if (t.type === "multichoose") return t.items.every((_, i) => (a["c" + i] || []).length > 0);
  if (t.type === "choose") return t.items.every((_, i) => a["c" + i] != null);
  if (t.type === "order") return t.items.every((_, i) => filled(a["o" + i]));
  if (t.type === "myth") return t.items.every((_, i) => a["c" + i] != null && filled(a["r" + i]));
  if (t.type === "multi") return t.parts.every(([k]) => filled(a[k]));
}
//----TEIL----
function answerLines(t) {
  const a = S.a[t.id] || {}, L = [];
  if (t.type === "gaps") t.sents.forEach((parts, si) => L.push((si + 1) + ". " + parts.map(p => typeof p === "string" ? p : "[" + v(a["g" + p]) + "]").join("")));
  if (t.type === "assign") t.rows.forEach((r, i) => L.push(r + ": " + t.cols.map((c, j) => c + " " + v(a["r" + i + "c" + j])).join(" · ")));
  if (t.type === "multichoose") t.items.forEach((it, i) => L.push(it + " → " + ((a["c" + i] || []).map(k => t.opts[k]).join(", ") || "?")));
  if (t.type === "choose") t.items.forEach((it, i) => L.push(it + ": " + (a["c" + i] != null ? t.opts[a["c" + i]] : "?")));
  if (t.type === "order") t.items.forEach((it, i) => L.push(v(a["o" + i]) + " – " + it));
  if (t.type === "myth") t.items.forEach((it, i) => L.push("»" + it + "«: " + (a["c" + i] != null ? t.opts[a["c" + i]] : "?") + " – " + v(a["r" + i])));
  if (t.type === "multi") t.parts.forEach(([k, lab]) => { L.push(lab); L.push("   " + (filled(a[k]) ? a[k].trim() : none)); });
  return L;
}
