"""Trägt die Einheit K1.4 Erkenntnisgewinn in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste der Lieferung).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k1-4-erkenntnis/eintragen.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
V = I.V
P = I.PRAEFIX
ZIP_V = "v1"  # Lieferung 29.10.2026 (Test: ohne TH-Kadetten, VS-Kadetten, QR-PNG, Kahoot)
DATEIEN = {"stand": "29.10.2026", "zip": f"{P}-{ZIP_V}.zip",
           "liste": [f"{P}-TH-Unterricht-{V}.pptx", f"{P}-TH-Lehrer-{V}.pptx", f"{P}-VS-Lehrer-{V}.pptx",
                     f"{P}-TH-AB-{V}.docx", f"{P}-TH-Loesung-{V}.docx", f"{P}-TH-Fachwissen-{V}.docx",
                     f"{P}-VS-AB-{V}.docx", f"{P}-VS-Loesung-{V}.docx", f"{P}-VS-Fachwissen-{V}.docx", f"{P}-Pruefbericht-Claude-{V}.md"]}
neu = {"klasse": "1AB", "fach": "NAWI", "ordner": I.ORDNER, "kapitel": "K1.4", "titel": I.TITEL, "block": "A Wissenschaft verstehen", "jahresplan": "E3",
       "seiten": ["theorie.html", "aufgaben.html", "versuche.html", "quiz.html"], "versteckt": True, "fahrplan": {"text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()}, "dateien": DATEIEN}
alt = [i for i, u in enumerate(E) if u["ordner"] == I.ORDNER]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):  # von Stephan oder später gesetzte Felder behalten
        if k in u: neu[k] = u[k]
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "1AB") + 1
    E.insert(pos, neu)
if len(sys.argv) > 1 and sys.argv[1].startswith("https://claude.ai/"):
    neu["lehrerseite"] = sys.argv[1]
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(PFAD, "a", encoding="utf-8").write("\n") if not open(PFAD, encoding="utf-8").read().endswith("\n") else None
print("eingetragen:", I.ORDNER, "·", PL.FAHRPLAN_TEXT[:60], "…")
