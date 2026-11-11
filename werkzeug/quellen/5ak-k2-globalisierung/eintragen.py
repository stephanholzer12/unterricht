"""Trägt die Einheit K2.1 Globalisierung (5AK IWK) in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste der Lieferung).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ak-k2-globalisierung/eintragen.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
V = I.V
P = I.PRAEFIX
DATEIEN = {"stand": I.STAND, "zip": "",
           "liste": [f"{P}-TH-Unterricht-{V}.pptx"]}
neu = {"klasse": "5AK", "fach": "IWK", "ordner": I.ORDNER, "kapitel": I.KAP, "titel": I.KURZTITEL, "block": "B Globalisierung", "jahresplan": "E3 (Prozesse der Globalisierung, 2 Stunden)",
       "seiten": ["theorie.html", "aufgaben.html", "quiz.html"], "versteckt": True, "lehrerseite": "https://claude.ai/artifact/HDe46vKV98ogtwmLxKHr4v", "fahrplan": {"text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()}, "dateien": DATEIEN}
OLD = "5ak-iwk/k2-globalisierung"   # frühere Fassung (v1–v4, K2): wird ersetzt
alt = [i for i, u in enumerate(E) if u["ordner"] in (I.ORDNER, OLD)]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):  # von Stephan oder später gesetzte Felder behalten
        if k in u: neu[k] = u[k]
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "5AK") + 1  # zuletzt eingetragen = »Gerade dran«, sobald eingeblendet
    E.insert(pos, neu)
if len(sys.argv) > 1 and sys.argv[1].startswith("https://claude.ai/"):
    neu["lehrerseite"] = sys.argv[1]
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(PFAD, "a", encoding="utf-8").write("\n") if not open(PFAD, encoding="utf-8").read().endswith("\n") else None
print("eingetragen:", I.ORDNER, "·", PL.FAHRPLAN_TEXT[:60], "…")
