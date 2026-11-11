"""Trägt die Übungsvariante der Rechenaufgaben 1, 3 und 5 (werkzeug/loesungshilfe_varianten.json) für K2.1 Globalisierung ein. Wiederholbar.
Keine Versuchsseite, darum keine Regeln in versuche_pruefung.json. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/5ak-k2-globalisierung/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Varianten: nur die Zahlen ändern sich, der Rechenweg bleibt. Klimawerte ohne Einheit (»kg CO₂-Äq.« enthält selbst eine Zahl).
VARIANTEN = [
 {"id": "a1", "vars": [{"n": "a", "min": 1492, "max": 1844, "step": 352}, {"n": "b", "min": 1944, "max": 1995, "step": 51}],
  "text": "Übung mit anderen Zahlen: Wie viele Jahre liegen zwischen dem Jahr {a} und dem Jahr {b}?",
  "felder": [{"label": "Jahre", "expr": "b-a", "einheit": ""}]},
 {"id": "a3", "vars": [{"n": "h", "min": 80, "max": 97, "step": 3}, {"n": "n", "min": 15, "max": 40, "step": 5}],
  "text": "Übung mit anderen Zahlen: In Land A nutzen {h} Prozent der Menschen das Internet, in Land B {n} Prozent. Berechne den Unterschied in Prozentpunkten.",
  "felder": [{"label": "Unterschied in Prozentpunkten", "expr": "h-n", "einheit": ""}]},
 {"id": "a5", "vars": [{"n": "w", "min": 200, "max": 1000, "step": 200}, {"n": "z", "min": 10, "max": 50, "step": 10}],
  "text": "Übung mit anderen Zahlen: Ein Gerät hat einen Zollwert von {w} US-Dollar, der Zollsatz beträgt {z} Prozent. Berechne den Zoll und die Summe aus Zollwert plus Zoll (in US-Dollar).",
  "felder": [{"label": "Zoll in US-Dollar", "expr": "w*z/100", "einheit": ""}, {"label": "Zollwert plus Zoll in US-Dollar", "expr": "w*(1+z/100)", "einheit": ""}]},
]
# Kontrolle: mit den Originalzahlen ergeben die Formeln die Lösungen aus inhalt.py
_e = lambda expr, **v: eval(expr, {}, v)
assert _e("b-a", a=1492, b=1944) == 452 and _e("h-n", h=94, n=23) == 71 and abs(_e("w*z/100", w=799, z=145) - 1158.55) < 1e-9


def var():
    """Kompaktes Format der Datei erhalten: Einheit als eigener Block, jede Variante in einer Zeile."""
    pfad = os.path.join(ROOT, "werkzeug", "loesungshilfe_varianten.json")
    roh = open(pfad, encoding="utf-8").read()
    d = json.loads(roh)
    if I.ORDNER in d:
        d[I.ORDNER] = VARIANTEN
        teile = []
        for k, v in d.items():
            teile.append(f'  {json.dumps(k)}: [\n' + ",\n".join("    " + json.dumps(x, ensure_ascii=False) for x in v) + "\n  ]")
        open(pfad, "w", encoding="utf-8").write("{\n" + ",\n".join(teile) + "\n}\n")
    else:
        i = roh.rstrip().rfind("}")
        neu = roh[:i].rstrip() + f',\n  {json.dumps(I.ORDNER)}: [\n    ' + ",\n    ".join(json.dumps(x, ensure_ascii=False) for x in VARIANTEN) + "\n  ]\n}\n"
        json.loads(neu)
        open(pfad, "w", encoding="utf-8").write(neu)


if __name__ == "__main__":
    var(); print("loesungshilfe_varianten.json: ok")
