"""Trägt die Prüfregeln der Versuchsseite (werkzeug/versuche_pruefung.json) und die Übungsvariante der Rechenaufgabe 8
(werkzeug/loesungshilfe_varianten.json) für K1.4 ein. Wiederholbar. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/1ab-k1-4-erkenntnis/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

# Versuchsseite: nur die drei Pflicht-Vergleichspaare (Spalten A und B) müssen Zahlen sein; Mittelwert/Spannweite und Gegenprobe sind nicht Pflicht
VS_REGELN = {
 "flieger": {
  "beob": {f"b{r}_{c}": {"zahl": True} for r in (0, 1, 2) for c in (1, 2)},
  "erk": {"kw": ["Mittelwert / im Mittel=mittel,durchschnitt,schnitt", "Vergleich A und B=weiter,kuerzer,gleich,mehr,weniger,unterschied,ohne,mit,klammer",
                 "Streuung / Kontakt=streu,spannweite,unterschiedlich,schwank,decke,wand,kontakt,kein kontakt,keine kontakte"], "need": 2},
  "interp": {"kw": ["Einordnung=unterstuetz,stuetz,spricht dafuer,spricht dagegen,dagegen,unklar,keine entscheidung,nicht entscheid,bestaetig,widerspr",
                    "Begruendung mit Daten=mittel,wert,spannweite,ueberlapp,streu,gegenprobe,zweite,werfer,decke,einzel"], "need": 2},
  "schluss": {"kw": ["Grenze=nur drei,wenig,werfer,kraft,hand,decke,hoehe,masse,schwerpunkt,ein flieger,zufall,wind,luft,ungenau",
                     "Verbesserung=mehr,oefter,wiederhol,rampe,schleuder,gleich,zweite,anderer,messen,genauer,flieger"], "need": 2}},
}

VARIANTE = {"id": "a8", "vars": [{"n": "a1", "min": 3.0, "max": 4.9, "step": 0.1}, {"n": "a2", "min": 3.0, "max": 4.9, "step": 0.1}, {"n": "a3", "min": 3.0, "max": 4.9, "step": 0.1},
                                 {"n": "b1", "min": 3.0, "max": 4.9, "step": 0.1}, {"n": "b2", "min": 3.0, "max": 4.9, "step": 0.1}, {"n": "b3", "min": 3.0, "max": 4.9, "step": 0.1}],
            "text": "Übungsdaten: ohne Klammer {a1} m · {a2} m · {a3} m, mit Klammer {b1} m · {b2} m · {b3} m. Berechne den Mittelwert A, den Mittelwert B und die Spannweite von B.",
            "felder": [{"label": "Mittelwert A", "expr": "(a1+a2+a3)/3", "einheit": "m"}, {"label": "Mittelwert B", "expr": "(b1+b2+b3)/3", "einheit": "m"},
                       {"label": "Spannweite B", "expr": "Math.max(b1,b2,b3)-Math.min(b1,b2,b3)", "einheit": "m"}]}


def vs():
    pfad = os.path.join(ROOT, "werkzeug", "versuche_pruefung.json")
    d = json.load(open(pfad, encoding="utf-8"))
    d["einheiten"][I.ORDNER] = VS_REGELN
    open(pfad, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def var():
    """Kompaktes Format der Datei erhalten: Einheit als eigener Block, jede Variante in einer Zeile."""
    pfad = os.path.join(ROOT, "werkzeug", "loesungshilfe_varianten.json")
    roh = open(pfad, encoding="utf-8").read()
    d = json.loads(roh)
    if I.ORDNER in d:
        d[I.ORDNER] = [VARIANTE]
        teile = []
        for k, v in d.items():
            teile.append(f'  {json.dumps(k)}: [\n' + ",\n".join("    " + json.dumps(x, ensure_ascii=False) for x in v) + "\n  ]")
        open(pfad, "w", encoding="utf-8").write("{\n" + ",\n".join(teile) + "\n}\n")
    else:
        i = roh.rstrip().rfind("}")
        neu = roh[:i].rstrip() + f',\n  {json.dumps(I.ORDNER)}: [\n    ' + json.dumps(VARIANTE, ensure_ascii=False) + "\n  ]\n}\n"
        json.loads(neu)
        open(pfad, "w", encoding="utf-8").write(neu)


if __name__ == "__main__":
    vs(); var(); print("versuche_pruefung.json und loesungshilfe_varianten.json: ok")
