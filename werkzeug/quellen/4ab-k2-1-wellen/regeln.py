"""Trägt die Prüfregeln der Versuchsseite (werkzeug/versuche_pruefung.json) und die Übungsvarianten der Rechenaufgaben
(werkzeug/loesungshilfe_varianten.json) für K2.1–2.3 ein. Wiederholbar. Aufruf im Repository-Ordner:
python3 werkzeug/quellen/4ab-k2-1-wellen/regeln.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I

GROESSE = "Ausschlag=klein,mittel,gross,groß,riesig,kaum,stark,wenig,schwach,hoch,maximal,winzig,fast nichts,nichts"
VS_REGELN = {
 "pendel": {
  "beob": {f"b{r}_{c}": {"zahl": True} for r in (0, 1) for c in range(1, 6)},
  "erk": {"kw": ["laenger / groesser=laeng,groess,mehr,hoeher,steigt,zunimmt,langsamer", "Periodendauer / Zeit=periode,dauer,zeit,schwingung,t ="], "need": 2},
  "interp": {"kw": ["Laenge veraendert=laenge,lang,l ", "gleich gelassen=gleich,selb,derselb,konstant,nicht veraendert,blieb", "fairer Vergleich=fair,vergleich,nur eine,eine groesse,einfluss,ursache"], "need": 2},
  "schluss": {"kw": ["kuerzer=kuerzer,kurz,verkuerz", "schneller / kleinere Periodendauer=schneller,kleiner,weniger zeit,kuerzere zeit,tickt"], "need": 2}},
 "resonanz": {
  "beob": {f"b{r}_1": {"kw": [GROESSE], "need": 1} for r in (0, 1, 2)},
  "erk": {"kw": ["eigener Takt / Rhythmus=eigen,rhythm,takt,passend,gleich,frequenz,mittler"], "need": 1},
  "interp": {"kw": ["nur eine Groesse aendern=nur,eine,gleich,fair,sonst,handweg,weg,ausholen", "Vergleich=vergleich,unterschied,wissen,ursache,liegt"], "need": 1},
  "schluss": {"kw": ["viele kleine Stoesse addieren=viele,addier,summ,aufschaukel,immer,wiederhol,takt,rhythm", "Resonanz / Eigenfrequenz=resonanz,eigenfrequenz,eigen,frequenz,mitschwing"], "need": 1}},
 "schnur": {
  "beob": {"b0_1": {"kw": ["auf und ab / bleibt am Ort=auf,ab,hoch,runter,bleibt,ort,stelle,quer"], "need": 1},
           "b0_2": {"kw": ["entlang der Schnur=entlang,ende,anderen,seite,zum,richtung,laengs,weiter"], "need": 1},
           "b1_1": {"kw": ["auf und ab=auf,ab,hoch,runter,hocke,aufsteh,steh"], "need": 1},
           "b1_2": {"kw": ["die Reihe entlang=reihe,entlang,weiter,naechst,seite,ende,nach"], "need": 1},
           "b2_1": {"kw": ["vor und zurueck=vor,zurueck,schritt,nach vorn"], "need": 1},
           "b2_2": {"kw": ["die Reihe entlang=reihe,entlang,weiter,naechst,vorn,ende,nach"], "need": 1}},
  "erk": {"kw": ["Stoerung / Energie kommt an=stoerung,puls,energie,welle,bewegung,signal", "Material bleibt am Platz=bleibt,platz,ort,stelle,nicht mit,klammer"], "need": 2},
  "interp": {"kw": ["quer / senkrecht=quer,senkrecht,auf und ab,transversal", "laengs / parallel=laengs,parallel,vor und zurueck,gleiche richtung,longitudinal"], "need": 2},
  "schluss": {"kw": ["nein, Luft reist nicht=nein,nicht,keine", "weitergegeben / Schall / Funk ohne Luft=weitergeg,teilchen,schall,druck,funk,elektromagnet,ohne luft"], "need": 2}},
 "interferenz": {
  "beob": {f"b{r}_2": {"zahl": True} for r in (0, 1, 2)},
  "erk": {"kw": ["verstaerken=verstaerk,groesser,addier,4", "abschwaechen / ausloeschen=schwaech,loesch,null,0,aufheb,kleiner"], "need": 2},
  "interp": {"kw": ["Richtung / Vorzeichen=richtung,vorzeichen,oben,unten,plus,minus,negativ,positiv", "heben sich auf=aufheb,ausloesch,gegen,abzieh,minus"], "need": 1},
  "schluss": {"kw": ["Gegenwelle / Gegenschall=gegen,entgegen,umgekehrt,ausloesch,aufheb", "nur am Ohr / an einer Stelle=ohr,stelle,ort,nur,dort,nah,ueberall,raum"], "need": 2}},
}

VARIANTEN = [
 {"id": "a1", "vars": [{"n": "A", "min": 2, "max": 6, "step": 1}, {"n": "T", "min": 0.4, "max": 2.0, "step": 0.2}, {"n": "t1", "min": 0.1, "max": 0.5, "step": 0.1}],
  "abgeleitet": {"t2": "t1+T", "A2": "2*A"},
  "text": "Ein Diagramm zeigt eine Schwingung: Vom tiefsten bis zum höchsten Punkt sind es {A2} cm, zwei benachbarte Hochpunkte liegen bei t = {t1} s und t = {t2} s. Gib A und T an und berechne f.",
  "felder": [{"label": "Amplitude A", "expr": "A", "einheit": "cm"}, {"label": "Periodendauer T", "expr": "T", "einheit": "s"}, {"label": "Frequenz f", "expr": "1/T", "einheit": "Hz"}]},
 {"id": "a3", "vars": [{"n": "l", "min": 0.25, "max": 1.5, "step": 0.05}],
  "text": "Ein ideales Fadenpendel ist l = {l} m lang (g = 9,81 m/s², kleine Auslenkung). Berechne T.",
  "felder": [{"label": "Periodendauer T", "expr": "2*Math.PI*Math.sqrt(l/9.81)", "einheit": "s"}]},
 {"id": "a7", "vars": [{"n": "f", "min": 200, "max": 1000, "step": 20}, {"n": "v", "min": 330, "max": 345, "step": 1}, {"n": "T", "min": 6, "max": 16, "step": 1}],
  "abgeleitet": {"L": "Math.round(1.56*T*T/10)*10"},
  "text": "a) Ein Ton hat f = {f} Hz, Schall ist v = {v} m/s schnell. Berechne λ. b) Eine Meereswelle hat λ = {L} m und T = {T} s. Berechne v.",
  "felder": [{"label": "a) Wellenlänge λ", "expr": "v/f", "einheit": "m"}, {"label": "b) Geschwindigkeit v", "expr": "Math.round(1.56*T*T/10)*10/T", "einheit": "m/s"}]},
 {"id": "a8", "vars": [{"n": "y1", "min": 3, "max": 6, "step": 1}, {"n": "y2", "min": -2, "max": -1, "step": 1}],
  "text": "Zwei Auslenkungen treffen sich an einem Ort: +{y1} cm und {y2} cm. Berechne die Summe.",
  "felder": [{"label": "Summe", "expr": "y1+y2", "einheit": "cm"}]},
 {"id": "a11", "vars": [{"n": "fMHz", "min": 30, "max": 88, "step": 2}],
  "text": "Ein Funkgerät sendet mit f = {fMHz} MHz. Berechne die Wellenlänge λ (c = 3,00 · 10⁸ m/s).",
  "felder": [{"label": "Wellenlänge λ", "expr": "3e8/(fMHz*1e6)", "einheit": "m"}]},
 {"id": "a14", "vars": [{"n": "m", "min": 0.1, "max": 0.5, "step": 0.05}, {"n": "k", "min": 10, "max": 50, "step": 5}],
  "text": "Ein ideales Federpendel: m = {m} kg, k = {k} N/m. Berechne T.",
  "felder": [{"label": "Periodendauer T", "expr": "2*Math.PI*Math.sqrt(m/k)", "einheit": "s"}]},
 {"id": "a15", "vars": [{"n": "l", "min": 0.4, "max": 1.0, "step": 0.05}, {"n": "n", "min": 10, "max": 20, "step": 5}, {"n": "g", "min": 9.78, "max": 9.84, "step": 0.01}],
  "abgeleitet": {"t": "Math.round(n*2*Math.PI*Math.sqrt(l/g)*10)/10"},
  "text": "Übungsdaten: Ein Fadenpendel ist l = {l} m lang, {n} volle Schwingungen dauern {t} s. Berechne T und g.",
  "felder": [{"label": "Periodendauer T", "expr": "Math.round(n*2*Math.PI*Math.sqrt(l/g)*10)/10/n", "einheit": "s"},
             {"label": "Fallbeschleunigung g", "expr": "4*Math.PI*Math.PI*l/Math.pow(Math.round(n*2*Math.PI*Math.sqrt(l/g)*10)/10/n,2)", "einheit": "m/s²"}]},
 {"id": "a16", "vars": [{"n": "A1", "min": 3, "max": 6, "step": 1}, {"n": "A2", "min": 1, "max": 2, "step": 1}],
  "text": "Zwei Schwingungen mit gleicher Frequenz haben die Amplituden {A1} cm und {A2} cm. Wie groß ist die Amplitude der Summe a) im Gleichtakt, b) im Gegentakt?",
  "felder": [{"label": "a) Gleichtakt", "expr": "A1+A2", "einheit": "cm"}, {"label": "b) Gegentakt", "expr": "A1-A2", "einheit": "cm"}]},
]


def schreiben(pfad, fn):
    d = json.load(open(pfad, encoding="utf-8"))
    fn(d)
    txt = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    open(pfad, "w", encoding="utf-8").write(txt)


def vs(d):
    d["einheiten"][I.ORDNER] = VS_REGELN


def var(d):
    d[I.ORDNER] = VARIANTEN


if __name__ == "__main__":
    # Format der Dateien beibehalten: Einrückung prüfen
    for name, fn in (("versuche_pruefung.json", vs),):  # Varianten: kompakt von Hand eingefügt (Format der Datei), siehe Prüfbericht
        pfad = os.path.join(ROOT, "werkzeug", name)
        roh = open(pfad, encoding="utf-8").read()
        schreiben(pfad, fn)
        print(name, "ok")
