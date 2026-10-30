"""Trägt die Übungsvarianten der Rechenaufgaben 2 und 6 (werkzeug/loesungshilfe_varianten.json) für K1.4–1.5 ein. Wiederholbar.
Keine Versuchsseite, darum keine Regeln in versuche_pruefung.json. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/5ab-k1-4-5-oeko/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Varianten: nur die Zahlen ändern sich, der Rechenweg bleibt. Klimawerte ohne Einheit (»kg CO₂-Äq.« enthält selbst eine Zahl).
VARIANTEN = [
 {"id": "a2", "vars": [{"n": "hA", "min": 2.0, "max": 4.0, "step": 0.5}, {"n": "hB", "min": 5.0, "max": 8.0, "step": 0.5},
                       {"n": "pA", "min": 6, "max": 12, "step": 1}, {"n": "pB", "min": 20, "max": 40, "step": 5}],
  "text": "Übung mit anderen Zahlen: A hält 200 Nutzungen, kostet {pA} € und verursacht in der Herstellung {hA} kg CO₂-Äq.; B hält 1.000 Nutzungen, kostet {pB} €, Herstellung {hB} kg CO₂-Äq. "
          "Endbehandlung A 0,2 kg, B 0,5 kg; Reinigung je Nutzung 0,01 kg CO₂-Äq. und 0,02 €. Berechne für 1.000 Nutzungen Klimawirkung (Zahl in kg CO₂-Äq.) und Gesamtkosten (Zahl in €) von A und B.",
  "felder": [{"label": "Klimawirkung A (Zahl)", "expr": "5*(hA+0.2)+10", "einheit": ""}, {"label": "Klimawirkung B (Zahl)", "expr": "1*(hB+0.5)+10", "einheit": ""},
             {"label": "Gesamtkosten A in €", "expr": "5*pA+20", "einheit": ""}, {"label": "Gesamtkosten B in €", "expr": "pB+20", "einheit": ""}]},
 {"id": "a6", "vars": [{"n": "nb", "min": 250, "max": 500, "step": 250}, {"n": "hB", "min": 5.0, "max": 8.0, "step": 0.5}, {"n": "pB", "min": 20, "max": 40, "step": 5}],
  "text": "Übung mit anderen Zahlen: Flasche B hält nur {nb} Nutzungen, kostet {pB} € und verursacht in der Herstellung {hB} kg CO₂-Äq., am Nutzungsende 0,5 kg; Reinigung je Nutzung 0,01 kg CO₂-Äq. und 0,02 €. "
          "Berechne für 1.000 Nutzungen die Zahl der B-Flaschen, die Klimawirkung (Zahl in kg CO₂-Äq.) und die Gesamtkosten (Zahl in €).",
  "felder": [{"label": "Anzahl B-Flaschen", "expr": "1000/nb", "einheit": ""}, {"label": "Klimawirkung B (Zahl)", "expr": "1000/nb*(hB+0.5)+10", "einheit": ""},
             {"label": "Gesamtkosten B in €", "expr": "1000/nb*pB+20", "einheit": ""}]},
]
# Kontrolle: mit den Originalzahlen ergeben die Formeln die Lösungen aus inhalt.py
_e = lambda expr, **v: eval(expr.replace("Math.", ""), {}, v)
assert _e("5*(hA+0.2)+10", hA=3.0) == 26 and _e("1*(hB+0.5)+10", hB=6.0) == 16.5 and _e("5*pA+20", pA=8) == 60 and _e("pB+20", pB=30) == 50
assert _e("1000/nb*(hB+0.5)+10", nb=500, hB=6.0) == 23 and _e("1000/nb*pB+20", nb=500, pB=30) == 80


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
