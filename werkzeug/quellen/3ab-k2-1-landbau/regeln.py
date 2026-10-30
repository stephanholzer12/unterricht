"""Trägt die Übungsvariante der Rechenaufgabe 5 (werkzeug/loesungshilfe_varianten.json) für K2.1 Landbau ein. Wiederholbar.
Keine Versuchsseite, darum keine Regeln in versuche_pruefung.json. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/3ab-k2-1-landbau/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Varianten: nur die Zahlen ändern sich, der Rechenweg bleibt. Klimawerte ohne Einheit (»kg CO₂-Äq.« enthält selbst eine Zahl).
VARIANTEN = [
 {"id": "a5", "vars": [{"n": "m", "min": 40, "max": 120, "step": 20}, {"n": "ek", "min": 60, "max": 90, "step": 10}, {"n": "eb", "min": 30, "max": 45, "step": 5}],
  "text": "Übung mit anderen Zahlen: Du brauchst {m} dt Weizen. Konventionell wachsen {ek} dt/ha, bio {eb} dt/ha. Berechne die Fläche in ha (nur die Zahl, auf zwei Dezimalstellen).",
  "felder": [{"label": "Fläche konventionell in ha", "expr": "m/ek", "einheit": ""}, {"label": "Fläche bio in ha", "expr": "m/eb", "einheit": ""}]},
]
# Kontrolle: mit den Originalzahlen ergeben die Formeln die Lösungen aus inhalt.py
_e = lambda expr, **v: eval(expr, {}, v)
assert _e("m/ek", m=80, ek=80) == 1 and abs(_e("m/eb", m=80, eb=36) - 2.2222) < 0.001


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
