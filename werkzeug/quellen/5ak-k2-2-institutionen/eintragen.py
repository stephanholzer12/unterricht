"""Trägt die Einheit K2.2 Institutionen der Globalisierung (5AK IWK) in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste).
Die Einheit bleibt versteckt, solange sie in einheiten.json als versteckt steht – einmal eingeblendet bleibt sie sichtbar.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/5ak-k2-2-institutionen/eintragen.py [https://claude.ai/... Lehrerseite]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
P = I.PRAEFIX
DATEIEN = {"stand": I.STAND, "zip": "",
           "liste": ["GitHub: theorie.html, aufgaben.html, quiz.html (" + I.V + ")",
                     "Lösungsseite (Artifact, privat) mit Präsentation, Kalender, Gruppen, Bewertungsraster",
                     f"{P}-Gruppenfolien-Vorlage-v1.pptx"]}  # Word, Kahoot, ZIP auf Zuruf
neu = {"klasse": "5AK", "fach": "IWK", "ordner": I.ORDNER, "kapitel": I.KAP, "titel": I.KURZTITEL,
       "block": "C Akteure", "jahresplan": "E5 (Akteure der Weltwirtschaft, 2 Stunden)",
       "seiten": ["aufgaben.html", "theorie.html", "quiz.html"],
       "versteckt": True, "kapitelmenue": True,
       "fahrplan": {"ansicht": "kompakt", "text": PL.FAHRPLAN_TEXT, "zeilen": PL.fahrplan_zeilen()},
       "dateien": DATEIEN}
alt = [i for i, u in enumerate(E) if u["ordner"] == I.ORDNER]
if alt:
    u = E[alt[0]]
    for k in ("lehrerseite", "versteckt", "aktuell"):
        if k in u: neu[k] = u[k]
    if "versteckt" not in u: neu.pop("versteckt", None)   # einmal eingeblendet bleibt sichtbar
    E[alt[0]] = neu
else:
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "5AK") + 1
    E.insert(pos, neu)
for a in sys.argv[1:]:
    if a.startswith("https://claude.ai/"): neu["lehrerseite"] = a
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(PFAD, "a", encoding="utf-8") as fh: fh.write("\n")
print("eingetragen:", I.ORDNER, "· versteckt:", neu.get("versteckt"), "· Lehrerseite:", neu.get("lehrerseite", "noch keine"))
