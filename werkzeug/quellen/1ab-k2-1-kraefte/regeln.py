"""Trägt die Prüfregeln der Versuchsseite (werkzeug/versuche_pruefung.json) und die Übungsvarianten der Rechenaufgaben
(werkzeug/loesungshilfe_varianten.json) für K2.1 Mechanische Kräfte ein. Wiederholbar. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/1ab-k2-1-kraefte/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I


def felder(pflicht, frei):
    """pflicht: {(zeile, spalte)} als Zahl · frei: {(zeile, spalte)} darf leer bleiben oder einen Strich enthalten."""
    d = {f"b{r}_{c}": {"zahl": True} for r, c in pflicht}
    d.update({f"b{r}_{c}": {"opt": True, "strich": True, "min": 1} for r, c in frei})
    return d


_ALLE = lambda rows, cols: {(r, c) for r in rows for c in cols}

VS_REGELN = {
 "g1": {"beob": felder(_ALLE(range(3), (1, 2, 3, 4)), set()),
        "erk": {"kw": ["Werte genannt=m/s,km/h,sekund,wert,durchgang,zwischen", "Vergleich=unterschied,fast gleich,gleich,streu,schwank,abweich"], "need": 2},
        "interp": {"kw": ["Ursache=reaktion,stopp,hand,start,ziel,markier,schrittl,ungenau,ablesen",
                          "zwei Gründe=und,zweite,ausserdem,außerdem,sowie,zudem,auch"], "need": 1},
        "schluss": {"kw": ["Grenze=nur drei,mittel,verlauf,nicht,kein,ungenau,hand,zeigt nicht",
                           "Alltag=marsch,weg,zeit,gehen,sport,planung,strecke,schule"], "need": 2}},
 "g2": {"beob": felder({(0, 1), (0, 2), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1)},
                       {(0, 3), (0, 4), (3, 2), (3, 3), (3, 4)}),
        "erk": {"kw": ["Änderung der Kraft=gestiegen,groesser,größer,mehr,zugenommen,1 n,ein newton,etwa 1",
                       "Vergleich Rechnung und Anzeige=rechnung,berechnet,anzeige,gemessen,passt,stimmt,unterschied"], "need": 2},
        "interp": {"kw": ["Messgenauigkeit=teilung,skala,ablesen,rundung,genau,0,2,naeherung,näherung,9,81,zehn"], "need": 1},
        "schluss": {"kw": ["Grenze=grob,teilung,nicht genau,keine bestaetigung,keine bestätigung,nur,ungenau",
                           "kg und N=masse,kilogramm,newton,kraft,unterschied,rucksack"], "need": 2}},
 "g3": {"beob": felder(_ALLE(range(3), (1, 2, 3)), {(3, 1), (3, 2), (3, 3)}),
        "erk": {"kw": ["Anzeige steigt=steigt,groesser,größer,mehr,zunimmt,nimmt zu,hoeher,höher",
                       "mit der Tiefe=tiefe,eintauch,volumen,tiefer,cm"], "need": 2},
        "interp": {"kw": ["nicht schwerer=nicht schwerer,gleich schwer,keine masse,nicht mehr masse,wird nicht",
                          "Gegenkraft=gegenkraft,wechselwirkung,drueckt,drückt,nach unten,wasser,gefaess,gefäß"], "need": 2},
        "schluss": {"kw": ["Grenze=klein,oberflaechen,oberfläch,anhaft,durchmesser,hand,ungenau,streu,keine dichte",
                           "Schiff=schiff,hohl,form,verdraeng,verdräng,mittlere dichte,luft"], "need": 2}},
 "g4": {"beob": felder(_ALLE(range(3), (1, 2, 3)), {(3, 1), (3, 2), (3, 3)}),
        "erk": {"kw": ["welcher Wert größer=losgleiten,vor dem,groesser,größer,hoeher,höher,gleichfoermig,gleichförmig,kleiner",
                       "alle Durchgänge=immer,jedes mal,nicht immer,einmal,durchgang,alle drei"], "need": 2},
        "interp": {"kw": ["Haft- und Gleitreibung=haftreibung,haft,gleitreibung,gleit,losbrech,maximum",
                          "mehr Masse=mehr wasser,400,normalkraft,masse,groesser,größer"], "need": 1},
        "schluss": {"kw": ["Grenze=klein,unruhig,schwank,ablesen,schraeg,schräg,nicht eindeutig,ein material",
                           "Beispiel=schuh,sohle,reifen,bremse,lager,kette,oel,öl,schmier"], "need": 2}},
 "g5": {"beob": felder(_ALLE(range(6), (1,)), _ALLE(range(6), (2,))),
        "erk": {"kw": ["wie weit=mm,cm,ueber,über,gestiegen,hoch,grenze",
                       "schneller oder langsamer=langsam,schnell,am anfang,zuerst,dann,nimmt ab,bremst"], "need": 2},
        "interp": {"kw": ["Adhäsion=adhaesion,adhäsion,wand,faser,benetz,haftet",
                          "Kohäsion=kohaesion,kohäsion,zusammen,wassersaeule,wassersäule,zieht nach"], "need": 2},
        "schluss": {"kw": ["Grenze=keine poren,misst nicht,nur,papier,baum,nicht vollstaendig,nicht vollständig,ungenau",
                           "Alltag=tuch,socke,kleidung,verband,handtuch,papier,saug"], "need": 2}},
 "g6": {"beob": felder(_ALLE(range(2), (1, 2)), _ALLE(range(2), (3,))),
        "erk": {"kw": ["offen leicht=offen,leicht,gering,entweicht,geht leicht",
                       "geschlossen schwerer=zu,geschlossen,schwer,groesser,größer,widerstand,drueckt zurueck,drückt zurück"], "need": 2},
        "interp": {"kw": ["Druck steigt=druck,steigt,groesser,größer,zusammengedrueckt,zusammengedrückt,komprim",
                          "Kraft auf den Kolben=kolben,kraft,zurueck,zurück,flaeche,fläche"], "need": 2},
        "schluss": {"kw": ["Grenze=nicht gemessen,kein wert,qualitativ,keine zahl,nur beobacht,kolbenreibung,dicht",
                           "Schneeschuh=flaeche,fläche,groesser,größer,kleiner druck,verteilt,einsink,schnee"], "need": 2}},
 "g7": {"beob": felder(_ALLE(range(4), (1, 2)), set()),
        "erk": {"kw": ["Unterschied klein=gleich,fast gleich,kein unterschied,klein,0,2,eine teilung,innerhalb"], "need": 1},
        "interp": {"kw": ["dieselbe Zugkraft=dieselbe,gleiche,eine kraft,uebertragen,übertragen,messkette,nicht addier",
                          "Begründung=weil,denn,ruhig,kette,spannung,beide,wechselwirkung"], "need": 2},
        "schluss": {"kw": ["Grenze=aufloesung,auflösung,teilung,nullpunkt,skala,ungenau,zwei geraete,zwei geräte",
                           "Beispiel=abstossen,abstoßen,sprint,gehen,rueckstoss,rückstoß,rakete,schwimmen,klettern"], "need": 2}},
}

# ---------------------------------------------------------------- Übungsvarianten (zählen nicht für die Abgabe)
VARIANTEN = [
 {"id": "a1", "vars": [{"n": "s", "min": 3.0, "max": 12.0, "step": 0.5}, {"n": "t", "min": 2.0, "max": 8.0, "step": 0.5},
                       {"n": "m", "min": 1.0, "max": 5.0, "step": 0.5}, {"n": "a", "min": 1.0, "max": 6.0, "step": 0.5}],
  "text": "Übung mit anderen Zahlen: Ein Körper legt geradeaus {s} m in {t} s zurück. Eine Masse von {m} kg wird mit {a} m/s² beschleunigt.",
  "felder": [{"label": "mittlere Schnelligkeit", "expr": "s/t", "einheit": "m/s"},
             {"label": "dasselbe in km/h", "expr": "s/t*3.6", "einheit": "km/h"},
             {"label": "resultierende Kraft", "expr": "m*a", "einheit": "N"}]},
 {"id": "a3", "vars": [{"n": "m", "min": 2.0, "max": 25.0, "step": 0.5}, {"n": "F", "min": 60, "max": 600, "step": 10},
                       {"n": "A", "min": 0.01, "max": 0.5, "step": 0.01}, {"n": "s", "min": 4.0, "max": 20.0, "step": 0.5},
                       {"n": "t", "min": 2.0, "max": 10.0, "step": 0.5}],
  "text": "Übung mit anderen Zahlen: Ein Rucksack hat {m} kg Masse (g = 10 N/kg). Eine senkrechte Kraft von {F} N verteilt sich auf {A} m². Ein Körper legt geradeaus {s} m in {t} s zurück.",
  "felder": [{"label": "Gewichtskraft des Rucksacks", "expr": "m*10", "einheit": "N"},
             {"label": "mittlerer Druck", "expr": "F/A", "einheit": "Pa"},
             {"label": "mittlere Schnelligkeit", "expr": "s/t", "einheit": "m/s"}]},
 {"id": "z2", "vars": [{"n": "F", "min": 200, "max": 900, "step": 50}, {"n": "A1", "min": 0.02, "max": 0.06, "step": 0.01},
                       {"n": "A2", "min": 0.2, "max": 0.6, "step": 0.05}],
  "text": "Übung mit anderen Zahlen: Eine senkrechte Kraft von {F} N verteilt sich zuerst auf {A1} m², dann auf {A2} m².",
  "felder": [{"label": "erster Druck", "expr": "F/A1", "einheit": "Pa"},
             {"label": "zweiter Druck", "expr": "F/A2", "einheit": "Pa"}]},
]


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
    d[I.ORDNER] = VARIANTEN
    teile = []
    for k, v in d.items():
        teile.append(f"  {json.dumps(k)}: [\n" + ",\n".join("    " + json.dumps(x, ensure_ascii=False) for x in v) + "\n  ]")
    open(pfad, "w", encoding="utf-8").write("{\n" + ",\n".join(teile) + "\n}\n")


if __name__ == "__main__":
    vs(); var(); print("versuche_pruefung.json und loesungshilfe_varianten.json: ok ·", len(VS_REGELN), "Gruppen,", len(VARIANTEN), "Übungsvarianten")
