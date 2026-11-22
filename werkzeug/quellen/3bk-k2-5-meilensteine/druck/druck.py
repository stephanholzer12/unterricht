"""Druckvorlagen für PBGW 3BK · K2.1–5.4 Meilensteine (Standard 16.11.2026: alles Auszudruckende fertig als PDF liefern).
Erzeugt zwei PDF:
  1 Paragrafenblatt Hammurabi (Stunde 2, Aufgabe 4) – A4 hoch, 1 Blatt je Paar
  2 Zeitstrahl-Karten (Stunde 1 und 3, Aufgabe 8) – A4 quer, Schilder und Karten zum Ausschneiden
Aufruf: python3 druck.py <Zielordner>"""
import io, os, subprocess, sys

sys.path.insert(0, "/home/claude/unterricht/werkzeug/quellen/3bk-k2-5-meilensteine")
import inhalt as I

ZIEL = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
PARA = [r for r in [t for t in I.T if t["nr"] == 4][0]["tab"][1:]]
KARTEN = [f[1].split("·", 1)[1].strip() if "·" in f[1] else f[1] for f in [t for t in I.T if t["nr"] == 8][0]["fields"][:9]]
BEREICHE = [t for t in I.T if t["nr"] == 8][0]["fields"][0][2]
GRUPPEN = 6   # Annahme: 6 Gruppen (steht so auf dem Blatt; im Gruppen-Generator der Lösungsseite änderbar)

BASIS = """
@page { size: %s; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "Source Sans 3", "Noto Sans", system-ui, sans-serif; color: #1F2A1C; }
.blatt { width: %s; height: %s; padding: 14mm 14mm 10mm; break-after: page; page-break-after: always; display: flex; flex-direction: column; position: relative; }
.blatt:last-child { break-after: auto; page-break-after: auto; }
.kopf { border-bottom: 3px solid #3B4A2F; padding-bottom: 5mm; margin-bottom: 6mm; display: flex; justify-content: space-between; align-items: baseline; gap: 8mm; }
.kopf .titel { font-size: 20pt; font-weight: 800; color: #3B4A2F; }
.kopf .rechts { font-size: 11pt; color: #5E6652; text-align: right; }
.fuss { position: absolute; left: 14mm; right: 14mm; bottom: 6mm; font-size: 9pt; color: #5E6652; display: flex; justify-content: space-between; }
"""


def schreibe(name, html, querformat, seiten_erwartet):
    groesse = ("A4 landscape", "297mm", "210mm") if querformat else ("A4 portrait", "210mm", "297mm")
    voll = ("<!doctype html><html lang=de><head><meta charset=utf-8><style>" + BASIS % groesse + html[0] + "</style></head><body>" + html[1] + "</body></html>")
    hp = os.path.join(ZIEL, name + ".html")
    io.open(hp, "w", encoding="utf-8").write(voll)
    pdf = os.path.join(ZIEL, name + ".pdf")
    # Chrome im Kopflos-Modus ignoriert @page size (druckt Letter) – darum über Playwright mit festem A4-Format.
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(hp))
        pg.emulate_media(media="print")
        pg.pdf(path=pdf, format="A4", landscape=querformat, print_background=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        b.close()
    assert os.path.exists(pdf)
    n = int(subprocess.run(["pdfinfo", pdf], capture_output=True).stdout.decode().split("Pages:")[1].split()[0])
    assert n == seiten_erwartet, (name, "Seiten:", n, "erwartet:", seiten_erwartet)
    print("gebaut:", os.path.basename(pdf), n, "Seite(n)", os.path.getsize(pdf) // 1024, "KB")
    return pdf


# ------------------------------------------------------------------ 1 Paragrafenblatt
css1 = """
.hinweis { font-size: 11.5pt; color: #5E6652; margin-bottom: 5mm; }
table.para { width: 100%; border-collapse: collapse; font-size: 14.5pt; line-height: 1.35; }
table.para th { background: #3B4A2F; color: #fff; font-size: 12pt; letter-spacing: .05em; text-transform: uppercase; padding: 3mm 4mm; text-align: left; }
table.para td { border: 1.5px solid #3B4A2F; padding: 4mm; vertical-align: top; }
table.para td.nr { width: 22mm; text-align: center; font-size: 20pt; font-weight: 800; color: #8C3B2E; background: #F9ECE9; }
.markier { margin-top: 6mm; border: 2.5px dashed #2E7D8C; border-radius: 4mm; padding: 4mm 5mm; font-size: 12.5pt; background: #F2F8F9; }
.markier b { color: #2E7D8C; }
.markier ol { margin: 2mm 0 0; padding-left: 6mm; } .markier li { margin: 1.5mm 0; }
"""
zeilen = "".join(f'<tr><td class="nr">§&nbsp;{p[0]}</td><td>{p[1]}</td></tr>' for p in PARA)
body1 = f"""<div class="blatt">
 <div class="kopf"><div class="titel">Hammurabis Rechtssammlung – Arbeitsfassung</div>
  <div class="rechts">PBGW 3BK · Stunde 2 · Aufgabe 4<br>Name: ______________________</div></div>
 <p class="hinweis">Sprachlich vereinfachte Arbeitsfassung nach dem Schulbuch S. 40 – kein wörtliches Zitat.
  Eine Mine ist eine Gewichts- und Recheneinheit für Silber.</p>
 <table class="para"><tr><th>§</th><th>Worum es geht</th></tr>{zeilen}</table>
 <div class="markier"><b>So arbeitest du mit dem Blatt (zu zweit):</b>
  <ol><li>Unterstreiche in jedem Paragrafen, <b>wer</b> geschädigt wird (Bürgersohn, Untergebener, Knecht).</li>
   <li>Kreise ein, <b>was</b> als Folge droht (Vergeltung oder Zahlung).</li>
   <li>Vergleiche § 196, § 198 und § 199: gleiche Verletzung – welche Folge?</li>
   <li>Trage deine Antworten danach im Arbeitsblatt am Handy ein.</li></ol></div>
 <div class="fuss"><span>26-27-3BK-K2.1–5.4 Meilensteine · Druckvorlage</span><span>1 Blatt je Paar · Stand {I.STAND}</span></div>
</div>"""

# ------------------------------------------------------------------ 2 Zeitstrahl-Karten
css2 = """
.schilder { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 1fr); gap: 6mm; flex: 1; }
.schild { border: 4px solid #3B4A2F; border-radius: 5mm; display: flex; align-items: center; justify-content: center; text-align: center;
          font-size: 26pt; font-weight: 800; color: #3B4A2F; background: #EEF3E4; padding: 4mm; line-height: 1.2; }
.karten { display: grid; grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(3, 1fr); gap: 0; flex: 1; }
.karte { border: 2px dashed #5E6652; display: flex; flex-direction: column; justify-content: center; gap: 3mm; padding: 6mm 8mm; }
.karte .nr { font-size: 15pt; font-weight: 800; color: #fff; background: #3B4A2F; border-radius: 3mm; padding: 1mm 4mm; align-self: flex-start; }
.karte .txt { font-size: 19pt; font-weight: 700; line-height: 1.25; }
.karte.leer .txt { color: #9AA68C; font-weight: 600; font-style: italic; }
.schnitt { font-size: 9pt; color: #5E6652; margin-bottom: 3mm; }
"""
schilder = "".join(f'<div class="schild">{b.replace("–", "–<br>")}</div>' for b in BEREICHE)
blatt_s = f"""<div class="blatt">
 <div class="kopf"><div class="titel">Zeitstrahl: Die sechs Zeitbereiche</div>
  <div class="rechts">PBGW 3BK · Aufgabe 8<br>Schilder für den Tisch oder die Tafel</div></div>
 <p class="schnitt">An den Linien auseinanderschneiden. Je Gruppe ein Satz (6 Schilder) – für {GRUPPEN} Gruppen {GRUPPEN}× ausdrucken.</p>
 <div class="schilder">{schilder}</div>
 <div class="fuss"><span>26-27-3BK-K2.1–5.4 Meilensteine · Druckvorlage</span><span>Blatt 1 von 3 · Stand {I.STAND}</span></div>
</div>"""


def kartenblatt(von, bis, blattnr, leer=0):
    k = "".join(f'<div class="karte"><span class="nr">Karte {i + 1}</span><span class="txt">{KARTEN[i]}</span></div>'
                for i in range(von, bis))
    k += "".join('<div class="karte leer"><span class="nr">Eigene Karte</span>'
                 '<span class="txt">Ereignis: ________________________<br>Zeitbereich: ____________________</span></div>' for _ in range(leer))
    return f"""<div class="blatt">
 <div class="kopf"><div class="titel">Zeitstrahl-Karten {von + 1}–{bis}{" und eigene Karte" if leer else ""}</div>
  <div class="rechts">PBGW 3BK · Aufgabe 8<br>Gruppe: ____________</div></div>
 <p class="schnitt">An den gestrichelten Linien auseinanderschneiden. Je Gruppe ein Satz – für {GRUPPEN} Gruppen {GRUPPEN}× ausdrucken.</p>
 <div class="karten">{k}</div>
 <div class="fuss"><span>26-27-3BK-K2.1–5.4 Meilensteine · Druckvorlage</span><span>Blatt {blattnr} von 3 · Stand {I.STAND}</span></div>
</div>"""


body2 = blatt_s + kartenblatt(0, 6, 2) + kartenblatt(6, 9, 3, leer=3)

p1 = schreibe("26-27-3BK-K2.1-5.4-Meilenst-Druck-Para-v1", (css1, body1), False, 1)
p2 = schreibe("26-27-3BK-K2.1-5.4-Meilenst-Druck-Zeit-v1", (css2, body2), True, 3)
print("fertig:", p1, p2)
