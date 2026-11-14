"""Trägt die Einheit K2.4/K3.2 Akustik und Gehör in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste).
Die Einheit wird VERSTECKT angelegt – Direktlink funktioniert, auf der Klassenseite erscheint sie erst nach dem Einblenden.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/4ab-k2-4-akustik/eintragen.py [https://claude.ai/... Lehrerseite]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
P = I.PRAEFIX
DATEIEN = {"stand": I.STAND, "zip": "26-27-4AB-Akustik-Gehoer-Claude-v2.zip",
           "liste": [f"{P}-Lehrer-{I.V}.html", f"{P}-Konzept-{I.V}.md", f"{P}-Pruefbericht-Claude-{I.V}.md"]}
neu = {"klasse": "4AB", "fach": "NAWI", "ordner": I.ORDNER, "kapitel": "K2.4 · K3.2", "titel": I.TITEL,
       "block": "C Akustik, Optik & Sinne", "jahresplan": "E9–E10",
       "seiten": ["aufgaben.html", "theorie.html"],
       "versteckt": True,
       "fahrplan": {"ansicht": "kompakt", "text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()},
       "dateien": DATEIEN}
alt = [i for i, u in enumerate(E) if u["ordner"] == I.ORDNER]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):
        if k in u: neu[k] = u[k]
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "4AB") + 1
    E.insert(pos, neu)
for a in sys.argv[1:]:
    if a.startswith("https://claude.ai/"): neu["lehrerseite"] = a
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(PFAD, "a", encoding="utf-8") as fh: fh.write("\n")
print("eingetragen:", I.ORDNER, "· versteckt:", neu.get("versteckt"), "· Lehrerseite:", neu.get("lehrerseite", "noch keine"))
