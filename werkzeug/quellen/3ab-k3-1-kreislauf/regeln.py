"""Trägt die Übungsvarianten der Rechenaufgaben (werkzeug/loesungshilfe_varianten.json) für K3.1 Körper unter Belastung (3AB) ein. Wiederholbar.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/3ab-k3-1-kreislauf/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

VAR = [
 {"id": "a4", "vars": [{"n": "sv", "min": 55, "max": 100, "step": 5}, {"n": "hf", "min": 55, "max": 90, "step": 1}, {"n": "sv2", "min": 100, "max": 140, "step": 5}, {"n": "hf2", "min": 120, "max": 190, "step": 5}],
  "text": "Übung mit anderen Zahlen: In Ruhe Schlagvolumen {sv} ml und Puls {hf} pro Minute. Beim Sport Schlagvolumen {sv2} ml und Puls {hf2} pro Minute.",
  "felder": [{"label": "Liter pro Minute in Ruhe", "expr": "sv*hf/1000", "einheit": "l"},
             {"label": "Liter an einem Tag in Ruhe", "expr": "sv*hf/1000*1440", "einheit": "l"},
             {"label": "Liter pro Minute beim Sport", "expr": "sv2*hf2/1000", "einheit": "l"}]},
 {"id": "z2", "vars": [{"n": "h", "min": 0.4, "max": 1.4, "step": 0.05}],
  "text": "Übung mit anderen Zahlen: Das Herz liegt {h} m über dem Boden (Blut 1000 kg/m³, g = 9,81 m/s²).",
  "felder": [{"label": "Druck p = ρ · g · h in Pa", "expr": "1000*9.81*h", "einheit": "Pa"}]},
]
P = os.path.join(ROOT, "werkzeug/loesungshilfe_varianten.json")
d = json.load(open(P, encoding="utf-8"))
d[I.ORDNER] = VAR
# im Stil der Datei schreiben (eine Variante je Zeile), damit andere Einheiten im Diff unverändert bleiben
out = "{\n" + ",\n".join("  %s: [\n%s\n  ]" % (json.dumps(k, ensure_ascii=False), ",\n".join("    " + json.dumps(v, ensure_ascii=False) for v in vs)) for k, vs in d.items()) + "\n}\n"
open(P, "w", encoding="utf-8").write(out)
print("Varianten eingetragen:", [v["id"] for v in VAR])
