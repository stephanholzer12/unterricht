"""Versuchsseite 2AB K1.2 auf den Stationenbetrieb (Stunde 3–4) umstellen.
Aufruf im Repository-Ordner: python3 werkzeug/quellen/2ab-k1-2-stationen/versuche_anpassen.py
- 4 ungefährliche Stationen A–D (je 1 Satz Material), K1.2-V4 als Lehrer-Demo, Rest ZUSATZ
- volle Versuchs-IDs K1.2-V1 … K1.2-V11, Stationsplan, Stand-Datum
Läuft auf der aktuellen versuche.html (ersetzt die Daten V und die Darstellung); mehrfach ausführbar."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
P = os.path.join(ROOT, "2ab-nawi/k1-2-bindungen/versuche.html")
STAND = "19.10.2026"
s = open(P, encoding="utf-8").read()
a = s.index("const V = ") + 10; b = s.index("];\n", a) + 1
V = {v["id"]: v for v in json.loads(s[a:b])}

for v in V.values():
    n = re.sub(r"^(K1\.2-)?V", "", v["nr"]); v["nr"] = "K1.2-V" + n
    v["kern"] = False; v.pop("station", None); v.pop("demo", None)

# ---- Station A: K1.2-V9 Wasser mit Haut (ohne Pfeffer, mit Münze)
V["haut"].update(station="A", kern=True, skizze="c10b",
    intro="Wie viel Wasser passt auf eine Münze – und kann eine Büroklammer aus Metall auf dem Wasser schwimmen?",
    sicher="Waschmittel nicht in die Augen bringen. Verschüttetes Wasser gleich aufwischen (Rutschgefahr).",
    mat=[["Petrischale + Wasser", "petrischale"], ["Münze (10 Cent)", "muenze"], ["Tropfpipette", "pipette"],
         ["Becherglas 100 mL", "becher"], ["Büroklammer", "klammer"], ["Filterpapier", "filterpapier"], ["Waschmittel", "seife"]],
    entsorgung="Wasser in den Ausguss. Petrischale, Becherglas und Münze gründlich mit Leitungswasser spülen und abtrocknen – Waschmittelreste verderben den Versuch für die nächste Gruppe.",
    schritte=["Leg die trockene Münze auf den Tisch. Tropf mit der Pipette Wasser darauf – Tropfen für Tropfen – und zähl mit, bis das Wasser überläuft. Schau dir den »Wasserberg« von der Seite an.",
              "Trockne die Münze ab. Gib in das Becherglas 1 Tropfen Waschmittel und rühr um. Wiederhole Schritt 1 mit diesem Seifenwasser.",
              "Leg die Büroklammer auf ein Stück Filterpapier und leg beides vorsichtig auf das Wasser in der Petrischale. Warte, bis das Papier sinkt.",
              "Gib einen Tropfen Waschmittel an den Rand der Petrischale und beobachte die Büroklammer."],
    beob={"titel": "Beobachtung", "kopf": ["Versuchsteil", "Anzahl Tropfen bzw. was passiert?"],
          "zeilen": [["Münze + Wasser"], ["Münze + Seifenwasser"], ["Büroklammer auf dem Wasser"], ["Büroklammer nach dem Waschmitteltropfen"]]},
    erk="Vergleiche die Tropfenzahl mit Wasser und mit Seifenwasser. Was passiert mit der Büroklammer, wenn Waschmittel dazukommt?",
    interp="Erkläre den »Wasserberg« und die schwimmende Büroklammer mit den Wasserstoffbrücken zwischen den Wassermolekülen (Schulbuch S. 26). Was macht das Waschmittel mit diesen Brücken?",
    schluss="Wasserläufer laufen über das Wasser. Was passiert mit ihnen, wenn Waschmittel (z. B. vom Abwasch im Feldlager) in ihren Teich gelangt? Was folgt daraus für den Umweltschutz?",
    buch={"s": "S. 26", "kap": "Die Bindungsarten: 5.1 Wasserstoffbrückenbindungen – Oberflächenspannung (S. 26); Tenside: S. 166"})

# ---- Station B: K1.2-V7 Der scheue Wasserstrahl (Reiben an Haaren oder Pullover)
V["wasserstrahl"].update(station="B", kern=True,
    sicher="Kein Strom im Spiel. Spritzwasser am Boden gleich aufwischen.",
    mat=[["Luftballon (aufgeblasen)", "ballon"], ["Wasserhahn", "hahn"], ["Reibetuch (Wolle) oder Pullover", "tuch"], ["Becherglas 100 mL", "becher"]],
    schritte=["Dreh den Wasserhahn so weit auf, dass ein dünner, gleichmäßiger Strahl fließt (so dünn wie eine Bleistiftmine).",
              "Halte den Luftballon nah an den Strahl, ohne ihn zu berühren.",
              "Reib den Ballon kräftig am Reibetuch, an einem Pullover oder an trockenen Haaren (etwa 20-mal).",
              "Nähere den geriebenen Ballon langsam dem Wasserstrahl. Probier auch: Fang Wasser im Becherglas auf und gieß es in dünnem Strahl aus – geht es auch so?"],
    entsorgung="Nichts zu entsorgen. Wasserhahn zudrehen, Ballon für die nächste Gruppe liegen lassen.")

# ---- Station C: K1.2-V8 Wer mischt sich mit wem? (ohne Brennspiritus und Paraffinöl)
V["mischen"].update(station="C", kern=True, skizze="c4b",
    intro="Du schüttelst Stoffe paarweise zusammen und prüfst, ob eine einheitliche Mischung entsteht oder ob sie sich wieder trennen.",
    sicher="Schutzbrille! Nichts kosten. Reagenzglas mit Parafilm verschließen und beim Schütteln den Daumen draufhalten. Waschmittel nicht in die Augen bringen.",
    mat=[["4 Reagenzgläser + Gestell", "reagenzglas"], ["Parafilm", "parafilm"], ["Tropfpipette", "pipette"], ["Spatel", "spatel"],
         ["blaues Wasser", "farbe"], ["Glycerin", "glycerin"], ["Olivenöl", "oel"], ["Kochsalz", "salz"], ["Waschmittel", "seife"]],
    entsorgung="Alle Gläser mit Öl in den Sammelbehälter »organische Reste« – NICHT in den Ausguss. Wasser mit Glycerin in den Ausguss. Reagenzgläser mit Waschmittel und Bürste reinigen und ins Gestell zum Trocknen.",
    schritte=["Füll Reagenzglas 1 und 2 je 2 cm hoch mit blauem Wasser, Reagenzglas 4 mit 2 cm Olivenöl.",
              "Gib dazu: in Glas 1 2 cm Glycerin, in Glas 2 2 cm Olivenöl, in Glas 4 eine Spatelspitze Kochsalz.",
              "Verschließ die Gläser mit Parafilm, schüttle 10 Sekunden und stell sie ins Gestell. Warte 1 Minute.",
              "Gib in Glas 2 drei Tropfen Waschmittel, verschließ es wieder, schüttle und beobachte (das ist Nr. 3)."],
    beob={"titel": "Beobachtung", "kopf": ["Nr.", "Mischung", "eine Phase oder zwei? Wie sieht es aus?"],
          "zeilen": [["1", "Wasser + Glycerin"], ["2", "Wasser + Olivenöl"], ["3", "Glas 2 + Waschmittel"], ["4", "Olivenöl + Kochsalz"]]},
    erk="Welche Stoffe mischen sich bzw. lösen sich? Teile Wasser, Glycerin, Olivenöl und Kochsalz in zwei Gruppen ein: »mag Wasser« und »mag Öl«.",
    interp="Erkläre mit polar/unpolar, warum sich Glycerin und Wasser mischen, Öl und Wasser aber nicht – und warum sich das Salz (Ionen) nicht im Öl löst. Was macht das Waschmittel?",
    schluss="Tarnschminke besteht aus Fett und Wachs. Warum geht sie mit Wasser allein kaum ab – mit Öl oder Seife aber schon?",
    buch={"s": "S. 22–23, 27", "kap": "Die Bindungsarten: 3.1 Arten von Atombindungen – polar/unpolar (S. 22–23) · 5.2 Ähnliches löst sich in Ähnlichem (S. 27); Tenside: S. 166"})

# ---- Station D: K1.2-V2 Salzkörner unter der Lupe + K1.2-V3 Spröde oder verformbar?
V["kristall"].update(station="D", kern=True, skizze="c3b", titel="Würfel im Salzstreuer",
    intro="Schau dir Kochsalz, Zucker und Alaun ganz genau an. Haben die Körner eine bestimmte Form – und was verrät sie über die Teilchen?",
    sicher="Nichts in den Mund nehmen, danach Hände waschen. Objektträger sind aus Glas – vorsichtig anfassen.",
    mat=[["Mikroskop oder Lupe", "mikroskop"], ["Lupe", "lupe"], ["3 Objektträger", "objekttraeger"], ["Spatel", "spatel"],
         ["Kochsalz", "salz"], ["Zucker", "zucker"], ["Kaliumalaun", "alaun"]],
    entsorgung="Körner vom Objektträger in den Restmüll klopfen. Objektträger kurz abspülen und abtrocknen.",
    schritte=["Leg drei Objektträger auf ein Blatt Papier und beschrifte das Papier darunter: Salz, Zucker, Alaun.",
              "Gib auf jeden Objektträger eine kleine Spatelspitze des passenden Stoffs und verteil die Körner ein wenig.",
              "Betrachte die Körner zuerst mit der Lupe, dann – wenn ein Mikroskop frei ist – mit der kleinsten Vergrößerung.",
              "Zeichne oder fotografiere jeweils ein typisches Korn. Danach geht es an diesem Tisch mit K1.2-V3 weiter."],
    beob={"titel": "Beobachtung", "kopf": ["Probe", "Form der Körner (Skizze oder Beschreibung)"], "zeilen": [["Kochsalz"], ["Zucker"], ["Kaliumalaun"]]},
    erk="Beschreibe die Form der Kochsalz-Körner. Sind große und kleine Körner gleich geformt?",
    interp="Warum haben alle Kochsalz-Körner dieselbe Würfelform – egal wie groß sie sind? Erkläre mit dem Ionengitter (Schulbuch S. 21).",
    schluss="Was kannst du aus der äußeren Form eines Kristalls über die Anordnung der Teilchen im Inneren schließen?")
V["sproede"].update(station="D", kern=True,
    intro="Ein Salzkristall und ein Stück Metall bekommen denselben Druck ab. Was hält stand – und was zerbricht? (Am selben Tisch wie K1.2-V2.)")

# ---- Lehrer-Demo in Stunde 4: K1.2-V4 Multimeter-Check (nur 1 Gerät)
V["multimeter"].update(demo=True, kern=True,
    intro="Lehrer-Demo in Stunde 4: Deine Lehrkraft prüft mit dem Multimeter, welche Stoffe den Strom leiten. Tipp zuerst: leitet oder leitet nicht? Dann schau zu und trag die Ergebnisse ein.",
    sicher="Nur mit dem Multimeter (Batterie) – niemals mit Strom aus der Steckdose! Das Gerät bedient nur die Lehrkraft.")

order = ["haut", "wasserstrahl", "mischen", "kristall", "sproede", "multimeter", "schmelz", "kaelte", "leitung", "eis", "verdunsten"]
assert set(order) == set(V), set(V) ^ set(order)
data = [V[k] for k in order]
s = s[:a] + json.dumps(data, ensure_ascii=False) + s[b:]

# ---- Darstellung: Station / Demo / Zusatz
OLD_LIST = 'const kern = V.filter(v => v.kern), zus = V.filter(v => !v.kern);\n$("#vs").append(el("div", { class: "grp", text: "Kern-Versuche" }));\nkern.forEach(v => $("#vs").append(versuch(v)));\n$("#vs").append(el("div", { class: "grp", text: "Zusatz-Versuche" }));\nzus.forEach(v => $("#vs").append(versuch(v)));'
NEW_LIST = ('/*STATIONEN*/\n["A", "B", "C", "D"].forEach(st => { $("#vs").append(el("div", { class: "grp", text: "Station " + st + (st === "D" ? " · zwei Versuche am selben Tisch" : "") }));\n'
            '  V.filter(v => v.station === st).forEach(v => $("#vs").append(versuch(v))); });\n'
            '$("#vs").append(el("div", { class: "grp", text: "Lehrer-Demo zu Beginn von Stunde 4 – mittippen und eintragen" }));\nV.filter(v => v.demo).forEach(v => $("#vs").append(versuch(v)));\n'
            '$("#vs").append(el("div", { class: "grp", text: "Zusatz-Versuche – heute nicht dran (Brenner, Hitze oder Spiritus)" }));\nV.filter(v => !v.station && !v.demo).forEach(v => $("#vs").append(versuch(v)));\n/*/STATIONEN*/')
if OLD_LIST in s: s = s.replace(OLD_LIST, NEW_LIST)
else: s = re.sub(r"/\*STATIONEN\*/.*?/\*/STATIONEN\*/", lambda m: NEW_LIST, s, flags=re.S)
assert "/*STATIONEN*/" in s

# Kopfzeile des Versuchs: Tag zeigt Station bzw. Demo
OLD_TAG = 'el("span", { class: "tag " + (v.kern ? "kern" : "zusatz"), text: v.kern ? "KERN" : "ZUSATZ" })'
NEW_TAG = 'el("span", { class: "tag " + (v.kern ? "kern" : "zusatz"), text: v.station ? "KERN · Station " + v.station : (v.demo ? "KERN · Demo" : "ZUSATZ") })'
s = s.replace(OLD_TAG, NEW_TAG)
s = s.replace('d.text(clean((v.kern ? "KERN · " : "ZUSATZ · ")', 'd.text(clean((v.station ? "KERN · Station " + v.station + " · " : (v.demo ? "KERN · Lehrer-Demo · " : "ZUSATZ · "))')

# Sicherheitskarte (heute ohne Brenner)
s = re.sub(r'<li><b>Erst arbeiten, dann tippen\.</b>[^<]*</li>',
           '<li><b>Erst arbeiten, dann tippen.</b> Beim Schütteln, Gießen und Drücken das Handy nicht in der Hand.</li>', s)

# Stationsplan nach der Namenskarte
PLAN = f'''<!--PLAN--><section class="card" id="plan">
    <div class="head"><span class="nr">Stunde 3–4</span><span class="pill theory">Stationen A–D</span></div>
    <h2>So läuft es heute</h2>
    <ul class="steps">
      <li><b>8 Gruppen à 3</b> (eine Gruppe zu viert). Ein Protokoll-Handy pro Gruppe – nur diese Seite.</li>
      <li><b>Gruppe 1–4:</b> Stunde 3 Stationen, Stunde 4 Vertiefung. <b>Gruppe 5–8:</b> umgekehrt.</li>
      <li><b>Pro Station 7 Minuten</b>, dann auf das Zeichen weiter: A → B → C → D → A.</li>
      <li><b>Start:</b> Gruppe 1/5 bei A · 2/6 bei B · 3/7 bei C · 4/8 bei D.</li>
      <li>Vor dem Wechsel: Station aufräumen, wie ihr sie vorgefunden habt.</li>
      <li><b>Wartet ihr oder seid ihr früher fertig?</b> Jeder macht am eigenen Handy die <a href="vertiefung.html">Vertiefung (Aufgaben 11–17)</a>.</li>
      <li>Zu Beginn von Stunde 4 zeigt die Lehrkraft <b>K1.2-V4 Multimeter-Check</b> – erst tippen, dann zuschauen und die Ergebnisse auch hier eintragen.</li>
    </ul>
    <p class="hint"><b>Abgabe:</b> eine Versuchs-PDF pro Gruppe (Stationen A–D + Demo) und jeder eine Vertiefungs-PDF – beides in LMS bis zur nächsten NAWI-Stunde.</p>
  </section><!--/PLAN-->'''
if "<!--PLAN-->" in s: s = re.sub(r"<!--PLAN-->.*?<!--/PLAN-->", lambda m: PLAN, s, flags=re.S)
else:
    k = s.index('<div class="progress">'); s = s[:k] + PLAN + "\n  " + s[k:]

# Stand-Datum im Fuß
FOOT = f'<!--STAND--><p class="hint" style="text-align:center;margin:18px 0 8px">NAWI · 2AB · K1.2 Versuche · Stand {STAND}</p><!--/STAND-->'
if "<!--STAND-->" in s: s = re.sub(r"<!--STAND-->.*?<!--/STAND-->", lambda m: FOOT, s, flags=re.S)
else:
    k = s.index("</main>"); s = s[:k] + "  " + FOOT + "\n" + s[k:]
open(P, "w", encoding="utf-8").write(s)
print("ok", [(v["nr"], v.get("station") or ("Demo" if v.get("demo") else "Zusatz")) for v in data])
