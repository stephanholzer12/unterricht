"""Trägt die Übungsvariante der Rechenaufgabe 3 (werkzeug/loesungshilfe_varianten.json) für K2 Globalisierung ein. Wiederholbar.
Keine Versuchsseite, darum keine Regeln in versuche_pruefung.json. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/5ak-k2-globalisierung/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Varianten: nur die Zahlen ändern sich, der Rechenweg bleibt. Klimawerte ohne Einheit (»kg CO₂-Äq.« enthält selbst eine Zahl).
VARIANTEN = [
 {"id": "a3", "vars": [{"n": "w", "min": 60, "max": 200, "step": 20}, {"n": "z", "min": 10, "max": 25, "step": 5}],
  "text": "Übung mit anderen Zahlen: Ein US-Importeur führt eine Uhr mit einem Zollwert von {w} US-Dollar ein. Der Zollsatz beträgt {z} Prozent. Berechne den Zoll und den Betrag aus Zollwert plus Zoll (nur die Zahlen, in US-Dollar).",
  "felder": [{"label": "Zoll in US-Dollar", "expr": "w*z/100", "einheit": ""}, {"label": "Zollwert plus Zoll in US-Dollar", "expr": "w*(1+z/100)", "einheit": ""}]},
]
# Kontrolle: mit den Originalzahlen ergeben die Formeln die Lösungen aus inhalt.py
_e = lambda expr, **v: eval(expr, {}, v)
assert _e("w*z/100", w=100, z=15) == 15 and abs(_e("w*(1+z/100)", w=100, z=15) - 115) < 1e-9


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
