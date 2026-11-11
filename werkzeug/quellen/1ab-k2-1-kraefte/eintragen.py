"""Trägt die Einheit K2.1 Mechanische Kräfte in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste der Lieferung).
Die Einheit wird VERSTECKT angelegt (Stephans Vorgabe) – Direktlink und QR-Code funktionieren, auf der Klassenseite erscheint sie erst nach dem Einblenden.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/1ab-k2-1-kraefte/eintragen.py [https://claude.ai/... Lösungsseite]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
V = I.V
P = I.PRAEFIX
# Teillieferung 08.11.2026 / v2 11.11.2026: nur Handy-Seiten, Unterrichts-PPP und private Lösungsseite.
DATEIEN = {"stand": I.STAND, "liste": [f"{P}-TH-Unterricht-{V}.pptx"]}
neu = {"klasse": "1AB", "fach": "NAWI", "ordner": I.ORDNER, "kapitel": "K2.1", "titel": I.TITEL,
       "block": "E Physik", "jahresplan": "E15–E17",
       "seiten": ["aufgaben.html", "theorie.html", "quiz.html"],
       "versteckt": True,
       "fahrplan": {"ansicht": "kompakt", "text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()},
       "dateien": DATEIEN}
alt = [i for i, u in enumerate(E) if u["ordner"] == I.ORDNER]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):  # von Stephan oder später gesetzte Felder behalten
        if k in u: neu[k] = u[k]
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "1AB") + 1
    E.insert(pos, neu)
for a in sys.argv[1:]:
    if a.startswith("https://claude.ai/"): neu["lehrerseite"] = a
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(PFAD, "a", encoding="utf-8") as fh: fh.write("\n")
print("eingetragen:", I.ORDNER, "· versteckt:", neu.get("versteckt"), "· Lösungsseite:", neu.get("lehrerseite", "noch keine"))
