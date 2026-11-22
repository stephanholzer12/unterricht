"""Trägt die Einheit K2.1–5.4 Meilensteine (3BK) in werkzeug/einheiten.json ein bzw. aktualisiert sie (Fahrplan aus plan.py, Dateiliste).
Die Einheit bleibt versteckt, solange sie in einheiten.json als versteckt steht – einmal eingeblendet bleibt sie sichtbar.
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3bk-k2-5-meilensteine/eintragen.py [https://claude.ai/... Lehrerseite]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, plan as PL

PFAD = os.path.join(ROOT, "werkzeug/einheiten.json")
E = json.load(open(PFAD, encoding="utf-8"))
P = I.PRAEFIX
DATEIEN = {"stand": I.STAND, "zip": f"{P}-v3.zip",
           "liste": ["GitHub: theorie.html, aufgaben.html, quiz.html, check.html (" + I.V + ")",
                     "Lösungsseite (Artifact, privat) mit Präsentation, Kalender, Gruppen",
                     f"{P}-TH-Unterricht-v4.pptx", f"{P}-TH-Lehrer-v3.pptx", f"{P}-TH-Kadetten-v3.pptx",
                     f"{P}-TH-AB-v3.docx", f"{P}-TH-Loesung-v3.docx", f"{P}-TH-Fachwissen-v3.docx"]}  # PPP und Word noch auf dem Stand v3/v4 (31.10.2026)
neu = {"klasse": "3BK", "fach": "PBGW", "ordner": I.ORDNER, "kapitel": I.KAP, "titel": I.KURZTITEL,
       "block": "B Meilensteine", "jahresplan": "E3–E5",
       "seiten": ["aufgaben.html", "theorie.html", "quiz.html", "check.html"],
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
    pos = max(i for i, u in enumerate(E) if u["klasse"] == "3BK") + 1
    E.insert(pos, neu)
for a in sys.argv[1:]:
    if a.startswith("https://claude.ai/"): neu["lehrerseite"] = a
json.dump(E, open(PFAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(PFAD, "a", encoding="utf-8") as fh: fh.write("\n")
print("eingetragen:", I.ORDNER, "· versteckt:", neu.get("versteckt"), "· Lehrerseite:", neu.get("lehrerseite", "noch keine"))
