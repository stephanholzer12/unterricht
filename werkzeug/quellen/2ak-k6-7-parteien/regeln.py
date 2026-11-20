"""Trägt die Übungsvarianten der Rechenaufgaben (werkzeug/loesungshilfe_varianten.json) für K6–7 Wahlrecht und Parteien ein. Wiederholbar.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/2ak-k6-7-parteien/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

VAR = [
 {"id": "z1", "vars": [{"n": "a", "min": 50, "max": 70, "step": 1}, {"n": "d", "min": 3, "max": 15, "step": 1}], "abgeleitet": {"b": "a-d"},
  "text": "Übung mit anderen Zahlen: Bei einer Wahl gingen {a} % der 16- bis 17-Jährigen und {b} % der 18- bis 20-Jährigen wählen. Um wie viele Prozentpunkte lagen die Jüngeren vorne?",
  "felder": [{"label": "Prozentpunkte (nur die Zahl)", "expr": "d", "einheit": ""}]},
 {"id": "z4", "vars": [{"n": "x", "min": 20, "max": 60, "step": 1}, {"n": "y", "min": 10, "max": 50, "step": 1}, {"n": "z", "min": 5, "max": 30, "step": 1}],
  "text": "Übung mit anderen Zahlen: Drei Parteien haben {x}, {y} und {z} Mandate. Wie viele haben sie zusammen? (Mehrheit ab 92)",
  "felder": [{"label": "Mandate zusammen", "expr": "x + y + z", "einheit": ""}]},
]
P = os.path.join(ROOT, "werkzeug/loesungshilfe_varianten.json")
d = json.load(open(P, encoding="utf-8"))
d[I.ORDNER] = VAR
out = "{\n" + ",\n".join("  %s: [\n%s\n  ]" % (json.dumps(k, ensure_ascii=False), ",\n".join("    " + json.dumps(v, ensure_ascii=False) for v in vs)) for k, vs in d.items()) + "\n}\n"
open(P, "w", encoding="utf-8").write(out)
print("Varianten eingetragen:", [v["id"] for v in VAR])
