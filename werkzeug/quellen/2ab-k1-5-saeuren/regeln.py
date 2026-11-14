"""Trägt die Übungsvarianten der Rechenaufgaben (werkzeug/loesungshilfe_varianten.json) für K1.5 Säuren und Basen ein. Wiederholbar.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/2ab-k1-5-saeuren/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

VAR = [
 {"id": "a4", "vars": [{"n": "p", "min": 1, "max": 6, "step": 1}, {"n": "d", "min": 1, "max": 5, "step": 1}], "abgeleitet": {"q": "p+d"},
  "text": "Übung mit anderen Zahlen: Lösung A hat pH {p}, Lösung B hat pH {q}. Wievielmal so viele H₃O⁺-Ionen hat Lösung A?",
  "felder": [{"label": "Faktor (nur die Zahl)", "expr": "Math.pow(10, d)", "einheit": ""}]},
 {"id": "z2", "vars": [{"n": "d", "min": 0.1, "max": 0.5, "step": 0.05}],
  "text": "Übung mit anderen Zahlen: Der pH-Wert sinkt um {d}. Um wie viel Prozent steigt die Zahl der H₃O⁺-Ionen?",
  "felder": [{"label": "Zunahme in %", "expr": "(Math.pow(10, d) - 1) * 100", "einheit": "%"}]},
]
P = os.path.join(ROOT, "werkzeug/loesungshilfe_varianten.json")
d = json.load(open(P, encoding="utf-8"))
d[I.ORDNER] = VAR
out = "{\n" + ",\n".join("  %s: [\n%s\n  ]" % (json.dumps(k, ensure_ascii=False), ",\n".join("    " + json.dumps(v, ensure_ascii=False) for v in vs)) for k, vs in d.items()) + "\n}\n"
open(P, "w", encoding="utf-8").write(out)
print("Varianten eingetragen:", [v["id"] for v in VAR])
