function pdfStats() {
  let tot = 0, right = 0, first = 0, answered = 0;
  const rows = T.map(t => {
    const s = taskState(t); tot += s.total; right += s.right; first += s.first; answered += s.answered;
    return { t, s };
  });
  return { tot, right, first, answered, rows,
    shown: rows.filter(r => r.s.shown && r.s.total > 0).map(r => r.t.nr),
    unchecked: rows.filter(r => r.s.total > 0 && r.s.answered > 0 && !r.s.checked).map(r => r.t.nr),
    open: rows.filter(r => r.s.total > 0 && r.s.answered === 0).map(r => r.t.nr) };
}
function buildPdf() {
  const { jsPDF } = window.jspdf;
  const d = new jsPDF({ unit: "mm", format: "a4" });
  d.addFileToVFS("C-R.ttf", FONT_R); d.addFont("C-R.ttf", "C", "normal");
  d.addFileToVFS("C-B.ttf", FONT_B); d.addFont("C-B.ttf", "C", "bold");
  const W = 210, M = 18, CW = W - 2 * M, BOT = 282; let y = 14;
  const olive = [59, 74, 47], teal = [46, 125, 140], muted = [94, 102, 82], ink = [31, 42, 28], rust = [140, 59, 46], theory = [110, 127, 78];
  const green = [40, 120, 52], red = [178, 48, 36], grey = [140, 146, 128], amber = [176, 118, 20];
  const newPage = () => { d.addPage(); y = 18; };
  const txt = (s, size, style, color, x = M, w = CW, lh = 1.32) => {
    d.setFont("C", style); d.setFontSize(size); d.setTextColor(...color);
    const lines = d.splitTextToSize(clean(s), w), h = size * 0.3528 * lh;
    lines.forEach(l => { if (y + h > BOT) newPage(); d.text(l, x, y + h * 0.78); y += h; });
  };
  const tick = (x, yy, c) => { d.setDrawColor(...c); d.setLineWidth(0.7); d.line(x, yy, x + 1.3, yy + 1.4); d.line(x + 1.3, yy + 1.4, x + 3.6, yy - 1.8); };
  const cross = (x, yy, c) => { d.setDrawColor(...c); d.setLineWidth(0.7); d.line(x, yy - 1.6, x + 3, yy + 1.6); d.line(x, yy + 1.6, x + 3, yy - 1.6); };
  const dash = (x, yy, c) => { d.setDrawColor(...c); d.setLineWidth(0.7); d.line(x + 0.2, yy, x + 3, yy); };
  const now = new Date(), when = now.toLocaleDateString("de-AT") + ", " + now.toLocaleTimeString("de-AT", { hour: "2-digit", minute: "2-digit" }) + " Uhr";

  // Kopf
  d.addImage(LOGO, "PNG", M, y, 11, 12.6);
  d.setFont("C", "bold"); d.setFontSize(9); d.setTextColor(...teal); d.text(clean(__EYEBROW__ + " · Schulbuch S. 11–14"), M + 15, y + 4);
  d.setFontSize(18); d.setTextColor(...olive); d.text(clean(__TITEL__), M + 15, y + 11.5);
  y += 17;
  d.setFont("C", "normal"); d.setFontSize(11); d.setTextColor(...ink);
  d.text(clean("Name: " + (S.name || "—")), M, y); d.text(clean("Klasse: " + (S.klasse || "—")), M + 80, y); d.text(clean("Abgabe: " + when), W - M, y, { align: "right" });
  y += 3; d.setDrawColor(...olive); d.setLineWidth(0.6); d.line(M, y, W - M, y); y += 6;

  // Ergebnis-Übersicht
  const st = pdfStats(), pct = st.tot ? Math.round(st.right / st.tot * 100) : 0;
  const col = pct >= 75 ? green : pct >= 50 ? amber : red;
  d.setFillColor(238, 243, 228); d.setDrawColor(211, 220, 194); d.setLineWidth(0.3); d.roundedRect(M, y, CW, 27, 2, 2, "FD");
  d.setFont("C", "bold"); d.setFontSize(17); d.setTextColor(...col); d.text(clean(st.right + " von " + st.tot + " Antworten richtig (" + pct + " %)"), M + 4, y + 8.5);
  d.setFont("C", "normal"); d.setFontSize(10.5); d.setTextColor(...ink);
  d.text(clean("Gleich beim 1. Versuch richtig: " + st.first + " von " + st.tot), M + 4, y + 15);
  d.text(clean("Lösung angezeigt bei: " + (st.shown.length ? "Aufgabe " + st.shown.join(", ") : "keiner Aufgabe")), M + 4, y + 20);
  const warn = [];
  if (st.unchecked.length) warn.push("nicht geprüft: Aufgabe " + st.unchecked.join(", "));
  if (st.open.length) warn.push("nicht bearbeitet: Aufgabe " + st.open.join(", "));
  d.setTextColor(...(warn.length ? rust : muted)); d.text(clean(warn.length ? warn.join(" · ") : "Alle Aufgaben bearbeitet und geprüft."), M + 4, y + 25);
  y += 32;

  // Tabelle
  const cx = { nr: M + 2, title: M + 11, ric: M + 106, v1: M + 126, att: M + 146 }, RH = 6.2;
  d.setFont("C", "bold"); d.setFontSize(9); d.setTextColor(...muted);
  d.text("Nr.", cx.nr, y + 4); d.text("Aufgabe", cx.title, y + 4);
  d.text("richtig", cx.ric, y + 4, { align: "center" }); d.text("1. Versuch", cx.v1, y + 4, { align: "center" }); d.text("Versuche", cx.att, y + 4, { align: "center" }); d.text("Lösung", W - M - 1, y + 4, { align: "right" });
  y += 6; d.setDrawColor(...olive); d.setLineWidth(0.4); d.line(M, y, W - M, y);
  st.rows.forEach((r, i) => {
    const { t, s } = r, base = y + 4.3;
    if (i % 2 === 0) { d.setFillColor(246, 249, 240); d.rect(M, y + 0.3, CW, RH, "F"); }
    d.setFont("C", "bold"); d.setFontSize(10.5); d.setTextColor(...olive); d.text(String(t.nr), cx.nr, base);
    d.setFont("C", "normal"); d.setTextColor(...ink); d.text(d.splitTextToSize(clean(t.title), 88)[0], cx.title, base);
    if (s.total > 0) {
      const c2 = s.right === s.total ? green : s.right === 0 ? red : amber;
      d.setFont("C", "bold"); d.setTextColor(...c2); d.text(s.right + " / " + s.total, cx.ric, base, { align: "center" });
      d.setFont("C", "normal"); d.setTextColor(...ink);
      d.text(s.checked ? s.first + " / " + s.total : "–", cx.v1, base, { align: "center" });
      d.text(s.checked ? String(s.att) : "nicht geprüft", cx.att, base, { align: "center" });
      d.setTextColor(...(s.shown ? rust : ink)); d.text(s.shown ? "angezeigt" : "nein", W - M - 1, base, { align: "right" });
    } else {
      d.setFont("C", "normal"); d.setTextColor(...muted); d.text("Freitext – Lehrkraft liest", cx.ric, base); d.setTextColor(...(s.shown ? rust : ink)); d.text(s.shown ? "Beispiel gesehen" : "–", W - M - 1, base, { align: "right" });
    }
    y += RH;
  });
  d.setDrawColor(...olive); d.setLineWidth(0.4); d.line(M, y + 0.3, W - M, y + 0.3); y += 2.5;
  d.setFont("C", "normal"); d.setFontSize(8.5); d.setTextColor(...muted);
  const note = d.splitTextToSize(clean("Freitext wird nur auf Stichwörter geprüft (Aufgabe 2 und 4); Begründungen in Aufgabe 7 und die Antwort in Aufgabe 8 beurteilt die Lehrkraft. »1. Versuch« = beim ersten Prüfen richtig. »Versuche« = häufigstes Prüfen einer Antwort in dieser Aufgabe."), CW);
  note.forEach(l => { d.text(l, M, y + 3); y += 3.6; });
  y += 3;

  // Einzelauswertung
  const rowOf = (it, rec) => {
    let info, c;
    if (it.kind === "manual") { info = it.has ? "Lehrkraft liest" : "keine Antwort"; c = it.has ? grey : rust; }
    else if (!it.has) { info = "keine Antwort"; c = rust; }
    else if (!rec) { info = "nicht geprüft"; c = grey; }
    else if (it.ok) { info = rec.n === 1 ? "richtig im 1. Versuch" : "richtig im " + rec.n + ". Versuch"; c = green; }
    else { info = rec.n + (rec.n === 1 ? " Versuch" : " Versuche") + ", falsch"; c = red; }
    return { info, c };
  };
  for (const r of st.rows) {
    const { t, s } = r;
    if (y > BOT - 40) newPage();
    y += 2;
    d.setFont("C", "bold"); d.setFontSize(9); d.setTextColor(...theory); d.text(clean(t.src + (t.tag ? " · " + t.tag : "")), W - M, y + 4, { align: "right" });
    txt("Aufgabe " + t.nr + ": " + t.title, 13, "bold", olive, M, CW - 40);
    txt(t.q, 9.5, "normal", muted);
    if (s.total > 0) {
      const c2 = s.right === s.total ? green : s.right === 0 ? red : amber;
      txt(s.right + " von " + s.total + " richtig" + (s.checked ? " · " + s.att + (s.att === 1 ? " Versuch" : " Versuche") : " · nicht geprüft") + (s.shown ? " · Lösung angezeigt" : ""), 10.5, "bold", c2);
    }
    y += 1.2;
    for (const it of s.items) {
      const rec = s.c.items[it.k], { info, c } = rowOf(it, rec), noAns = !it.has;
      const w = CW - 8 - 34; d.setFont("C", "normal"); d.setFontSize(11.5);
      const lines = d.splitTextToSize(clean(noAns && it.kind === "manual" ? it.text.replace(/\?\s*$/, "— keine Antwort —") : it.text), w), h = 11.5 * 0.3528 * 1.3;
      const wrong = it.kind !== "manual" && it.has && !it.ok && it.sol;
      const solLines = wrong ? (d.setFontSize(9.5), d.splitTextToSize(clean("Richtig: " + it.sol), CW - 8)) : [];
      const need = lines.length * h + solLines.length * 4.2;
      if (y + need > BOT) newPage();
      const my = y + h * 0.55;
      if (it.kind === "manual") dash(M + 2, my, grey); else if (!it.has) dash(M + 2, my, rust); else if (it.ok) tick(M + 1.6, my, green); else cross(M + 2, my, red);
      d.setFont("C", noAns ? "bold" : "normal"); d.setFontSize(11.5); d.setTextColor(...(noAns ? rust : ink));
      lines.forEach(l => { d.text(l, M + 8, y + h * 0.78); y += h; });
      d.setFont("C", "bold"); d.setFontSize(8.5); d.setTextColor(...c); d.text(clean(info), W - M, y - lines.length * h + h * 0.78, { align: "right" });
      if (solLines.length) { d.setFont("C", "normal"); d.setFontSize(9.5); d.setTextColor(...teal); solLines.forEach(l => { d.text(l, M + 8, y + 3); y += 4.2; }); }
    }
    y += 2.5; d.setDrawColor(211, 220, 194); d.setLineWidth(0.3); d.line(M, y, W - M, y); y += 2;
  }
  const n = d.getNumberOfPages();
  for (let p = 1; p <= n; p++) { d.setPage(p); d.setFont("C", "normal"); d.setFontSize(8); d.setTextColor(...muted); d.text(clean(__KAPTITEL__ + " · " + (S.name || "") + " · Seite " + p + " von " + n), W - M, 292, { align: "right" }); }
  return d.output("blob");
}
