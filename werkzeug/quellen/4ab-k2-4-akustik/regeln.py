"""Trägt die Übungsvarianten der Rechenaufgaben (werkzeug/loesungshilfe_varianten.json) für K2.4 Akustik ein. Wiederholbar.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/4ab-k2-4-akustik/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

VAR = [
 {"id": "a2", "vars": [{"n": "t", "min": 2, "max": 15, "step": 1}, {"n": "te", "min": 0.4, "max": 3.0, "step": 0.1}, {"n": "f", "min": 110, "max": 1760, "step": 10}],
  "text": "Übung mit anderen Zahlen (v = 340 m/s): Der Donner kommt {t} s nach dem Blitz. Ein Echo kommt nach {te} s zurück. Ein Ton hat {f} Hz.",
  "felder": [{"label": "Entfernung des Gewitters", "expr": "340*t", "einheit": "m"},
             {"label": "Entfernung der Wand", "expr": "340*te/2", "einheit": "m"},
             {"label": "Wellenlänge des Tons", "expr": "340/f", "einheit": "m"}]},
 {"id": "a8", "vars": [{"n": "d", "min": 0.1, "max": 0.3, "step": 0.01}],
  "text": "Übung mit anderen Zahlen (v = 340 m/s): Der Umweg zum abgewandten Ohr beträgt {d} m. Wie viel später kommt der Schall dort an?",
  "felder": [{"label": "Zeitunterschied in Millisekunden", "expr": "d/340*1000", "einheit": "ms"}]},
 {"id": "z1", "vars": [{"n": "tw", "min": 0.02, "max": 0.4, "step": 0.01}, {"n": "tl", "min": 2, "max": 20, "step": 1}],
  "text": "Übung mit anderen Zahlen: Das Echolot-Signal kommt nach {tw} s zurück (Wasser 1480 m/s). Das Echo der Fledermaus kommt nach {tl} ms an (Luft 340 m/s).",
  "felder": [{"label": "Tiefe des Sees", "expr": "1480*tw/2", "einheit": "m"},
             {"label": "Entfernung des Insekts", "expr": "340*tl/1000/2", "einheit": "m"}]},
]
P = os.path.join(ROOT, "werkzeug/loesungshilfe_varianten.json")
d = json.load(open(P, encoding="utf-8"))
d[I.ORDNER] = VAR
# im Stil der Datei schreiben (eine Variante je Zeile), damit andere Einheiten im Diff unverändert bleiben
out = "{\n" + ",\n".join("  %s: [\n%s\n  ]" % (json.dumps(k, ensure_ascii=False), ",\n".join("    " + json.dumps(v, ensure_ascii=False) for v in vs)) for k, vs in d.items()) + "\n}\n"
open(P, "w", encoding="utf-8").write(out)
print("Varianten eingetragen:", [v["id"] for v in VAR])
