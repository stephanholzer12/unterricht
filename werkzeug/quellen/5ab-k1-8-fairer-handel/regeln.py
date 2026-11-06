"""Trägt die Übungsvarianten der Rechenaufgabe 2 (werkzeug/loesungshilfe_varianten.json) für K1.8 ein. Wiederholbar.
Keine Versuchsseite, darum keine Regeln in versuche_pruefung.json. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/5ab-k1-8-fairer-handel/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Varianten: nur die Zahlen ändern sich, der Rechenweg bleibt. Klimawerte ohne Einheit (»kg CO₂-Äq.« enthält selbst eine Zahl).
VARIANTEN = [
 {"id": "a2", "vars": [{"n": "t", "min": 20, "max": 60, "step": 10}, {"n": "p", "min": 200, "max": 300, "step": 25}, {"n": "m", "min": 3300, "max": 3700, "step": 100}, {"n": "w", "min": 2400, "max": 3000, "step": 100}],
  "text": "Übung mit anderen Zahlen: Eine Kooperative verkauft {t} Tonnen Kakao. Mindestpreis {m} US-Dollar je Tonne, Prämie {p} US-Dollar je Tonne, Weltmarktpreis {w} US-Dollar je Tonne. "
          "Berechne die Prämie insgesamt, den Erlös zum Mindestpreis (ohne Prämie) und den Mehrerlös gegenüber dem Weltmarktpreis (alles in US-Dollar, nur die Zahl).",
  "felder": [{"label": "Prämie insgesamt in US-Dollar", "expr": "t*p", "einheit": ""}, {"label": "Erlös zum Mindestpreis in US-Dollar", "expr": "t*m", "einheit": ""},
             {"label": "Mehrerlös gegenüber dem Weltmarkt in US-Dollar", "expr": "(m-w)*t", "einheit": ""}]},
]
# Kontrolle: mit den Originalzahlen ergeben die Formeln die Lösungen aus inhalt.py
_e = lambda expr, **v: eval(expr, {}, v)
assert _e("t*p", t=40, p=275) == 11000 and _e("t*m", t=40, m=3500) == 140000 and _e("(m-w)*t", m=3500, w=3100, t=40) == 16000


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
