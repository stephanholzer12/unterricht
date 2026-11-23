"""Trägt die Übungsvarianten der Rechenaufgaben (werkzeug/loesungshilfe_varianten.json) für TÖW 5AB K1.9 ein. Wiederholbar.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/5ab-k1-9-global-klima/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

VAR = [
 {"id": "a1", "vars": [{"n": "tag", "min": 60, "max": 300, "step": 1}],
  "text": "Übung mit anderen Zahlen: Ein Land erreicht seinen Overshoot Day am {tag}. Tag des Jahres. Wie viele Erden bräuchte die Menschheit, wenn alle so lebten?",
  "felder": [{"label": "Anzahl Erden", "expr": "365/tag", "einheit": ""}]},
 {"id": "a3", "vars": [{"n": "p", "min": 15, "max": 30, "step": 1}, {"n": "n", "min": 5, "max": 60, "step": 5}],
  "text": "Übung mit anderen Zahlen: {p} Kadetten stellen je {n} KI-Fragen pro Tag (0,24 Wh pro Frage).",
  "felder": [{"label": "Strom pro Tag", "expr": "p*n*0.24", "einheit": "Wh"},
             {"label": "Strom pro Jahr (365 Tage)", "expr": "p*n*0.24*365/1000", "einheit": "kWh"}]},
 {"id": "a5", "vars": [{"n": "t", "min": 20000, "max": 200000, "step": 1000}],
  "text": "Übung mit anderen Zahlen: Ein Abkommen erlaubt {t} t Rindfleisch zu niedrigem Zoll. Die EU isst rund 8 000 000 t pro Jahr. Wie viel Prozent sind das?",
  "felder": [{"label": "Anteil", "expr": "t/8000000*100", "einheit": "%"}]},
]
P = os.path.join(ROOT, "werkzeug/loesungshilfe_varianten.json")
d = json.load(open(P, encoding="utf-8"))
d[I.ORDNER] = VAR
out = "{\n" + ",\n".join("  %s: [\n%s\n  ]" % (json.dumps(k, ensure_ascii=False), ",\n".join("    " + json.dumps(v, ensure_ascii=False) for v in vs)) for k, vs in d.items()) + "\n}\n"
open(P, "w", encoding="utf-8").write(out)
print("Varianten eingetragen:", [v["id"] for v in VAR])
