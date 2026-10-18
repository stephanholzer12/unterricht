// Teststoff-Generator (eine A4-Seite) – gleiches Layout für alle Klassen und Fächer.
// Aufruf im Repository-Ordner:
//   node werkzeug/teststoff/teststoff.js werkzeug/teststoff/daten/<datei>.json [Zielordner]
// Schreibt die .docx mit dem Namen aus "datei" (Regelwerk Abschnitt 2/16) und prüft,
// ob sie auf genau eine Seite passt (wenn LibreOffice da ist).
// Textauszeichnung in der JSON:  **fett**   [[gelb markiert = Stephan ergänzt]]
// Abhängigkeiten: npm docx (vorinstalliert), Python-Paket qrcode (pip install qrcode).
"use strict";
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun, Footer,
  AlignmentType, WidthType, BorderStyle, ShadingType, VerticalAlign, LevelFormat,
  HighlightColor, PageNumber, TableLayoutType,
} = require("docx");

const HERE = __dirname;
const FONT = "Calibri";
const DUNKEL = "1F2A1C", OLIV = "3B4A2F", GRAU = "8A8F86", ROT = "C8102E";
const GRUEN = "7FA83A", HELL = "EEF3E4", KOPF = "D9D9D9", LINIE = "BFC7B3";
const CW = 10206; // A4 minus 2 × 850 Rand

// ---------- Text mit **fett** und [[gelb]] ----------
function runs(text, o = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\[\[[^\]]+\]\])/g;
  let last = 0, m;
  const mk = (t, extra = {}) => new TextRun({
    text: t, font: FONT, size: o.size || 18, color: o.color || DUNKEL,
    bold: o.bold || extra.bold, highlight: extra.gelb ? HighlightColor.YELLOW : undefined,
  });
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(mk(text.slice(last, m.index)));
    const t = m[0];
    if (t.startsWith("**")) out.push(...runs(t.slice(2, -2), { ...o, bold: true }));
    else out.push(mk(t.slice(2, -2), { gelb: true }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(mk(text.slice(last)));
  return out;
}
const P = (text, o = {}) => new Paragraph({
  alignment: o.align, keepNext: o.keepNext,
  spacing: { before: o.before || 0, after: o.after || 0 },
  numbering: o.bullet ? { reference: "punkte", level: 0 } : undefined,
  children: runs(text, o),
});

const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const kein = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const rand = (c, s) => ({ top: { style: BorderStyle.SINGLE, size: s, color: c }, bottom: { style: BorderStyle.SINGLE, size: s, color: c }, left: { style: BorderStyle.SINGLE, size: s, color: c }, right: { style: BorderStyle.SINGLE, size: s, color: c } });
const TBL_NONE = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };

function cell(children, w, o = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA }, children,
    borders: o.borders || rand(LINIE, 4),
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    verticalAlign: o.valign || VerticalAlign.CENTER,
    margins: { top: o.pad ?? 50, bottom: o.pad ?? 50, left: 90, right: 90 },
  });
}
function table(widths, rows) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths, layout: TableLayoutType.FIXED, borders: TBL_NONE,
    rows: rows.map(r => new TableRow({ cantSplit: true, children: r })),
  });
}
const ueberschrift = t => P(t, { bold: true, size: 22, color: OLIV, before: 140, after: 50, keepNext: true });

// Datentabelle: Kopfzeile grau, Zeilen abwechselnd hell
function datentabelle(widths, kopf, zeilen, center = []) {
  const rows = [kopf.map((t, i) => cell([P(t, { bold: true })], widths[i], { fill: KOPF }))];
  zeilen.forEach((z, zi) => rows.push(z.map((t, i) => cell(
    [P(String(t), { align: center.includes(i) ? AlignmentType.CENTER : undefined })],
    widths[i], { fill: zi % 2 === 1 ? HELL : undefined }))));
  return table(widths, rows);
}

function qrPng(url) {
  const f = path.join(os.tmpdir(), "qr_" + Buffer.from(url).toString("hex").slice(-40) + ".png");
  execFileSync("python3", ["-c",
    "import sys,qrcode;q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=2);" +
    "q.add_data(sys.argv[1]);q.make(fit=True);q.make_image(fill_color='#1F2A1C',back_color='white').save(sys.argv[2])",
    url, f]);
  return fs.readFileSync(f);
}

function bauen(D) {
  const ch = [];
  // Kopf: Wappen + Kopfzeile + Titel, darunter grüne Linie
  ch.push(table([800, CW - 800], [[
    cell([new Paragraph({ children: [new ImageRun({ type: "png", data: fs.readFileSync(path.join(HERE, "wappen.png")), transformation: { width: 40, height: 46 } })] })], 800, { borders: kein }),
    cell([P(D.kopf, { bold: true, size: 17, color: GRAU, after: 10 }), P(D.titel, { bold: true, size: 30, color: OLIV })], CW - 800, { borders: kein }),
  ]]));
  ch.push(new Paragraph({ spacing: { after: 80 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GRUEN, space: 1 } }, children: [] }));

  // Kasten Termin + Stoff
  ch.push(table([CW], [[cell([
    new Paragraph({ children: [...runs("Termin:  ", { bold: true, size: 20, color: OLIV }), ...runs(D.termin, { size: 20 })] }),
    new Paragraph({ children: [...runs("Stoff:  ", { bold: true, size: 20, color: OLIV }), ...runs(D.stoff, { size: 20 })] }),
  ], CW, { fill: HELL, borders: rand(GRUEN, 8), pad: 90 })]]));

  // Was wir durchgenommen haben
  ch.push(ueberschrift("Was wir durchgenommen haben"));
  ch.push(datentabelle([450, 2550, 950, 3350, 2906], ["Nr.", "Thema", "Schulbuch", "Unterlagen", "Aufgaben"], D.durchgenommen));

  // Das musst du können
  ch.push(ueberschrift("Das musst du können"));
  const kw = [450, 6606, 2700, 450];
  ch.push(datentabelle(kw, ["Nr.", "Ich kann …", "Fachbegriffe", "✓"],
    D.koennen.map(([nr, kann, begriffe]) => [nr, kann, begriffe, "☐"]), [0, 3]));

  // Formeln und Einheiten (nur wenn es Formeln gibt)
  if (D.formeln && D.formeln.length) {
    ch.push(ueberschrift("Formeln und Einheiten"));
    const n = D.formeln.length, w = Math.floor(CW / n);
    ch.push(table(Array(n).fill(w), [D.formeln.map(([f, e]) => cell([
      P(f, { bold: true, size: 20, align: AlignmentType.CENTER }),
      P("Einheit: " + e, { size: 17, color: GRAU, align: AlignmentType.CENTER }),
    ], w, { fill: HELL }))]));
    if (D.tipp) ch.push(new Paragraph({ spacing: { before: 40 }, children: [...runs("Tipp:", { bold: true, size: 17 }), ...runs(" " + D.tipp, { size: 17 })] }));
  }
  ch.push(new Paragraph({ spacing: { after: 60 }, children: [] }));

  // Kein Teststoff + QR-Codes
  const qr = D.qr || [];
  const qw = 1750, lw = CW - qr.length * qw;
  const links = [P("Kein Teststoff", { bold: true, size: 22, color: ROT, after: 40 }),
    ...D.kein_teststoff.map(t => P(t, { bullet: true, after: 20 })),
    P(D.gruss || "Viel Erfolg!", { bold: true, size: 22, color: OLIV, before: 100 })];
  ch.push(table([lw, ...qr.map(() => qw)], [[
    cell(links, lw, { borders: kein, valign: VerticalAlign.TOP }),
    ...qr.map(q => cell([
      q.url && !q.url.includes("[[")
        ? new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data: qrPng(q.url), transformation: { width: 112, height: 112 } })] })
        : table([1500], [[cell([P("[[QR-Code]]", { align: AlignmentType.CENTER, color: GRAU })], 1500, { pad: 500 })]]), // Vorlage: Platzhalter statt QR
      P(q.titel, { bold: true, color: OLIV, align: AlignmentType.CENTER }),
      P(q.text, { size: 16, color: GRAU, align: AlignmentType.CENTER }),
    ], qw, { borders: kein })),
  ]]));

  return new Document({
    creator: "Stephan Holzer", title: D.fuss,
    styles: { default: { document: { run: { font: FONT, size: 18 } } } },
    numbering: { config: [{ reference: "punkte", levels: [{ level: 0, format: LevelFormat.BULLET, text: "●", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { size: 12, color: OLIV } } }] }] },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 700, bottom: 700, left: 850, right: 850, footer: 350 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
        ...runs(D.fuss + " · Seite ", { size: 16, color: GRAU }),
        new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: GRAU }),
      ] })] }) },
      children: ch,
    }],
  });
}

async function main() {
  const [json, ziel = "."] = process.argv.slice(2);
  if (!json) { console.error("Aufruf: node teststoff.js <daten.json> [Zielordner]"); process.exit(1); }
  const D = JSON.parse(fs.readFileSync(json, "utf8"));
  const out = path.join(ziel, D.datei);
  fs.mkdirSync(ziel, { recursive: true });
  fs.writeFileSync(out, await Packer.toBuffer(bauen(D)));
  console.log("geschrieben:", out);
  const texte = [];
  (function sammeln(x) { if (typeof x === "string") texte.push(x); else if (x && typeof x === "object") Object.values(x).forEach(sammeln); })(D);
  const gelb = [...new Set(texte.flatMap(t => (t.match(/\[\[[^\]]+\]\]/g) || []).map(g => g.slice(2, -2))))];
  if (gelb.length) console.log("gelb markiert (Stephan ergänzt):", gelb.join(" | "));
  try { // Seitenprüfung: genau eine A4-Seite
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ts-"));
    execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, out], { stdio: "ignore" });
    const pdf = path.join(tmp, path.basename(out).replace(/\.docx$/, ".pdf"));
    const seiten = /Pages:\s+(\d+)/.exec(execFileSync("pdfinfo", [pdf]).toString())[1];
    console.log(seiten === "1" ? "Seitenprüfung: 1 Seite ✓" : `ACHTUNG: ${seiten} Seiten – kürzen, bis es eine Seite ist!`);
  } catch (e) { console.log("(Seitenprüfung übersprungen – LibreOffice/pdfinfo fehlt)"); }
}
main();
