"""Trägt die Einheit K1.4–1.5 Ökodesign und Ökobilanz in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste der Lieferung).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ab-k1-4-5-oeko/eintragen.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
V = I.V
P = I.PRAEFIX
ZIP_V = "v1"  # erste Lieferung 30.10.2026 (ohne Kahoot – Stephan, 30.10.2026)
DATEIEN = {"stand": "31.10.2026", "zip": f"{P}-{ZIP_V}.zip",
           "liste": [f"{P}-TH-Unterricht-{I.V_UNT}.pptx", f"{P}-TH-Lehrer-{V}.pptx", f"{P}-TH-Kadetten-{V}.pptx",
                     f"{P}-TH-AB-{V}.docx", f"{P}-TH-Loesung-{V}.docx", f"{P}-TH-Fachwissen-{V}.docx", f"{P}-Pruefbericht-Claude-{V}.md"]}
neu = {"klasse": "5AB", "fach": "TÖW", "ordner": I.ORDNER, "kapitel": I.KAP, "titel": I.KURZTITEL, "block": "A Ökologisches Wirtschaften", "jahresplan": "E3",
       "seiten": ["theorie.html", "aufgaben.html", "quiz.html"], "versteckt": True, "fahrplan": {"text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()}, "dateien": DATEIEN}
alt = [i for i, u in enumerate(E) if u["ordner"] == I.ORDNER]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):  # von Stephan oder später gesetzte Felder behalten
        if k in u: neu[k] = u[k]
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "5AB") + 1
    E.insert(pos, neu)
if len(sys.argv) > 1 and sys.argv[1].startswith("https://claude.ai/"):
    neu["lehrerseite"] = sys.argv[1]
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(PFAD, "a", encoding="utf-8").write("\n") if not open(PFAD, encoding="utf-8").read().endswith("\n") else None
print("eingetragen:", I.ORDNER, "·", PL.FAHRPLAN_TEXT[:60], "…")
