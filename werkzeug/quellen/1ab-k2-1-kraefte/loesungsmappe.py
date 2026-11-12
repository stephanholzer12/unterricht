"""Private Lehrer-Seite (Lösungsmappe) K2.1 Mechanische Kräfte – als Artifact, nur für Prof. HOLZER.
NICHT ins öffentliche Repository legen und nicht auf Kadetten-Seiten verlinken.
Aus derselben Datenquelle wie Handy-Seiten und Unterrichts-PPP (inhalt, theorie_daten, versuche_daten, plan, fachwissen).
Aufruf: python3 loesungsmappe.py <TH-Unterricht.pptx> <Ordner mit Folienbildern s-NN.jpg> <Ziel.html> <Ordner mit loesungen_gruppen.py>
v2 (11.11.2026): Reiter Kalender · Vorbereitung · Besprechen · Aufgaben · Versuche · Gruppen (Zufallsgenerator) · Folien · Fachwissen.
Die Musterantworten zu den Leitfragen liegen NICHT im Repository (loesungen_gruppen.py, im Claude-Projekt gespeichert).
Die Folienbilder sind die sichtbaren Folien der TH-Unterricht (LibreOffice-Render), damit die Seite am Beamer-PC als Ersatz taugt."""
import base64, glob, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
import inhalt as I, theorie_daten as TD, versuche_daten as VD, plan as P, fachwissen as F, gruppen_daten as GD
from pptx import Presentation

PPTX, FOLDIR, ZIEL, PRIVAT = sys.argv[1:5]
sys.path.insert(0, PRIVAT)
import loesungen_gruppen as LG
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
e = lambda t: html.escape(str(t), quote=False)


def md(t):
    """**fett** und Formelzeichen: F_G wird zu F mit tiefgestelltem G."""
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(t))
    return re.sub(r"(?<![\w/])([A-Za-zρμ])_([A-Za-zäöü]{1,12}|\d{1,2})\b", r"\1<sub>\2</sub>", s)


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def ul(items, cls=""):
    return f"<ul class='{cls}'>" + "".join(f"<li>{md(x)}</li>" for x in items) + "</ul>"


def tab(head, rows, cls=""):
    h = "".join(f"<th>{e(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f"<div class='scroll'><table class='{cls}'><tr>{h}</tr>{b}</table></div>"


def slug(x):
    s = re.sub(r"<[^>]+>|[*_`]", "", str(x)).lower().translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))
    return "-".join(re.findall(r"[a-z0-9]+", s)[:5])


# ---------------------------------------------------------------- Kalender (beide Klassen in EINER Liste nach Datum)
sys.path.insert(0, os.path.join(ROOT, "werkzeug"))
import fahrplan as FP_  # noqa: E402  (nur für das Datumsformat)
BRAUCHST = {1: "Beamer, Reiter »Gruppen« (Namen eingefügt), Bücher", 2: "Bücher; Handy der Gruppe für das Foto der Materiallisten",
            3: "freigegebenes Saal-Material je Gruppe, Wannen, Tücher; Gang für Gruppe 1 frei", 4: "Teams-Kanal für die Steckbriefe",
            5: "Beamer; Material der Gruppen steht an den Plätzen", 6: "nichts – Supplierstunde möglich"}
VORB_MIN = {1: 5, 2: 3, 3: 15, 4: 3, 5: 5, 6: 0}
termine = []
for k in I.KLASSEN:
    for st in P.PLAN[k]:
        termine.append((FP_._iso(st["datum"]) + ("8" if "8. Std" in st["datum"] else "1"), k, st))
termine.sort(key=lambda x: x[0])
krow = []
for iso, k, st in termine:
    n = st["std"]
    krow.append(f"<tr data-d='{iso[:8]}'><td class='num'>{e(st['datum'])}</td><td><b>{e(k)}</b></td><td>{e(I.STUNDENNAME[n])}</td>"
                f"<td><span class='tag'>{e(P.MARKE[n])}</span></td><td>{e(BRAUCHST[n])}</td><td class='num'>{VORB_MIN[n] or '–'}{' min' if VORB_MIN[n] else ''}</td></tr>")
kal = ("<p class='warn'>Die Daten sind <b>geplant</b> – abgeleitet aus dem Stundenmuster von K1.4 (1AK Donnerstag Doppelstunde und Freitag, 1BK Montag, Mittwoch, Freitag). "
       "Bitte einmal prüfen; falsche Daten ändere ich im Fahrplan, die Seiten ziehen nach.</p>"
       "<div class='scroll'><table class='kal'><tr><th>Datum</th><th>Klasse</th><th>Stunde</th><th>Was läuft</th><th>Du brauchst</th><th>Vorbereiten</th></tr>"
       + "".join(krow) + "</table></div>"
       "<p class='klein'>Hervorgehoben: der nächste Termin. 1AK hat Stunde 3 und 4 am selben Donnerstag (Doppelstunde) – Versuch und Steckbrief hintereinander, nur einmal auf- und abbauen.</p>")
kal += "<h2>Stundenkarten (Minuten je Phase, Summe je 50)</h2>"
for std in sorted(P.STUNDE):
    t0, li = 0, []
    for name, mi, oh, a in P.STUNDE[std]:
        chip = " <span class='chip'>ohne Handy</span>" if oh and a not in ("org", "reserve", "bespr", "erkl") else ""
        li.append(f"<tr><td class='num'>{t0}–{t0 + mi}</td><td>{e(name)}{chip}</td></tr>"); t0 += mi
    kal += (f"<details class='card'><summary><span class='nr'>{std}</span><span class='ttl'>{e(I.STUNDENNAME[std])}</span>"
            f"<span class='tag'>{e(P.MARKE[std])}</span></summary>"
            f"<div class='body'><p class='q'>Ziel: {e(P.ZIEL[std])}</p><div class='scroll'><table>{''.join(li)}</table></div>"
            f"<p class='warnline'><b>Wenn es knapp wird:</b> {e(P.KUERZEN[std].replace('Wenn es knapp wird: ', ''))}</p></div></details>")
kal += "<h2>Wenn eine Stunde ausfällt</h2>" + ul(["Zuerst fällt **Stunde 4** weg: Steckbrief in den ersten 15 Minuten von Stunde 5, Präsentationen je 2 Minuten.",
                                                 "**Supplierstunde möglich: Stunde 6** – Aufgabe 8 braucht kein Material und keinen Versuch.",
                                                 "Nie zwei Stunden in eine pressen, keine Hausübung."])
kal += "<h2>Links der Kadetten-Seiten</h2><ul>" + "".join(
    f"<li><b>{lab}</b><br><span class='mono'>{I.URL}{k}.html</span></li>"
    for k, lab in (("aufgaben", "Arbeitsblatt (alles, auch Gruppenprojekt und Versuch)"), ("theorie", "Theorie zum Nachschlagen"), ("quiz", "Kräfte-Check (Quiz)"))) + "</ul>"
kal += ("<p class='warnline'><b>Die Einheit ist noch versteckt.</b> Direktlink und QR-Code gehen schon; auf der Klassenseite erscheint sie erst nach "
        "GitHub → Actions → »Einheit ein-/ausblenden« → <span class='mono'>1ab-nawi/k2-1-kraefte</span>. Die alte Versuchsseite leitet ins Arbeitsblatt weiter.</p>")

# ---------------------------------------------------------------- Vorbereitung (statt »Herrichten«): nach Tagen, abhakbar
n_haken = 0
def haken(key, text, klein=""):
    global n_haken
    n_haken += 1
    return f"<li><label><input type='checkbox' data-k='{e(key)}'> {md(text)}" + (f"<br><span class='klein'>{md(klein)}</span>" if klein else "") + "</label></li>"

VORHER = [("vh-teams", "**Teams:** je Klasse einen Kanal oder Ordner »Steckbriefe K2.1« anlegen", "spätestens vor Stunde 4"),
          ("vh-namen", "**Gruppen-Generator:** Namenslisten 1AK und 1BK einmal einfügen (Reiter »Gruppen«)", "spätestens vor Stunde 1"),
          ("vh-gang", "**Gang für Gruppe 1** ansehen: 5 m frei, kein Durchgangsverkehr", "vor Stunde 3"),
          ("vh-km", "**Kraftmesser #51, #52, #26:** Nullpunkt und Skala prüfen – nur drei Stück für bis zu vier Gruppen", "vor Stunde 2 (Freigabe)"),
          ("vh-waage", "**Waagen #128:** einschalten, Funktion prüfen; Höchstlast 620 g", "vor Stunde 3"),
          ("vh-filter", "**Filterpapier #54:** gleich breite Streifen schneiden, falls Gruppe 5 es braucht", "nach der Freigabe")]
vb = ("<p>Zum Abhaken – die Haken bleiben nur in diesem Browser. Es gibt <b>keine Chemikalien</b> in dieser Einheit: nichts ansetzen, nichts verdünnen. "
      "Weil die Gruppen ihren Versuch selbst wählen, steht das genaue Material erst nach der <b>Freigabe in Stunde 2</b> fest. "
      "Unten bei Stunde 3 steht die Saal-Grundausstattung je Thema – streiche, was keine Gruppe braucht.</p>"
      "<div class='werkzeug'><button type='button' class='btn ghost' id='h-nur' aria-pressed='false'>Nur offene zeigen</button>"
      "<span class='zaehler' id='h-zaehler'>0 von 0 abgehakt</span><div class='balken'><i id='h-balken'></i></div></div>")
vb += "<h2>Schon vorher erledigen</h2><ul class='check'>" + "".join(haken(k, t, "wann: " + w) for k, t, w in VORHER) + "</ul>"
vb += "<h2>Pro Tag</h2>"
for iso, k, st in termine:
    n = st["std"]
    if VORB_MIN[n] == 0: continue
    li = []
    if n == 1:
        li = [haken(f"t{iso}-gen", "Gruppen auslosen und am Beamer zeigen (Reiter »Gruppen«)"), haken(f"t{iso}-buch", "Schulbücher für alle")]
    elif n == 2:
        li = [haken(f"t{iso}-buch", "Schulbücher – jede Gruppe braucht ihre Seiten"),
              haken(f"t{iso}-frei", "Freigabe: Materiallisten der sieben Gruppen fotografieren", "Daraus richtest du Stunde 3 her."),
              haken(f"t{iso}-km", "Kraftmesser verteilen: welche Gruppe misst wann", "nur #51, #52, #26")]
    elif n == 3:
        li = [haken(f"t{iso}-g{g}-{a}", f"Gruppe {g} · {GD.THEMEN[g]}: {a}", f"{nr} · Bestand {best} · NAWI-Saal E21 · am Vortag möglich")
              for g in range(1, 8) for a, nr, best in GD.G[g]["saal"]]
        li += [haken(f"t{iso}-wanne", "Wannen und Putztücher für alle Gruppen mit Wasser"),
               haken(f"t{iso}-weg", "Nach der Stunde: Saal-Material zurück, Gefäße trocknen")]
    elif n == 4:
        li = [haken(f"t{iso}-teams", "Teams-Kanal offen, Schriftführungen wissen, wohin das Handout kommt")]
    elif n == 5:
        li = [haken(f"t{iso}-reihe", "Reihenfolge der Gruppen 1 bis 7 an die Tafel"), haken(f"t{iso}-mat", "Material der Gruppen an den Plätzen")]
    offen = " open" if not vb.count("<details") else ""
    vb += (f"<details class='card tag-karte' data-d='{iso[:8]}'{offen}><summary><span class='nr'>{n}</span><span class='ttl'>{e(st['datum'])} · {e(k)}</span>"
           f"<span class='tag'>{e(P.MARKE[n])}</span><span class='tag zus'>ca. {VORB_MIN[n]} min</span></summary>"
           f"<div class='body'><ul class='check'>{''.join(li)}</ul></div></details>")
vb += "<h2>Was du vor Ort noch prüfen musst</h2>" + ul([
    "Die Saal-Bestände sind aus der Inventarliste gerechnet, nicht gezählt.",
    "Freigabe: Nichts von der Liste »nicht erlaubt« (Feuer, Chemikalien, Glas von zu Hause, Steckdose, Akkus, Waffen oder Waffenteile, Druckbehälter).",
    "Gruppe 7, Idee 3 (Rollbrett) nur sitzend und nur, wenn du es selbst für sicher hältst – sonst Idee 1 oder 2.",
    "Gruppe 6, Idee 2: Die Kadetten rechnen mit einer gewählten Masse (70 kg), nicht mit der eigenen Körpermasse."])
vb += "<h2>Gefahren-Check: harmlosere Alternativen</h2>" + tab(["Geprüft", "Ergebnis"], [
    ["Chemikalien", "Keine. Wasser, Speisesalz und Lebensmittelfarbe sind die einzigen Stoffe."],
    ["Flamme, Abzug", "Nicht nötig und nicht erlaubt."],
    ["Material von zu Hause", "Nur von der Liste »erlaubt«; alles steht auf der Materialliste und wird von dir freigegeben."],
    ["Glas", "Nur Saal-Glas (z. B. Becherglas #15); von zu Hause kein Glas."],
    ["Spritze, Ballon", "Ohne Nadel; nie auf Personen richten."],
    ["Kraftmesser", "Langsam ziehen, nie gegen den Körper."]])

# ---------------------------------------------------------------- Besprechen (pro Stunde)
besp = "<p>Was du in jeder Stunde gemeinsam besprichst – mit Kurzlösung. Die Folie »Das besprechen wir« zeigt dieselben Punkte.</p>"
BESP = {1: ("Aufgabe 2", [("a) Fahrrad in der Kurve", "Die Richtung der Geschwindigkeit ändert sich – das ist Beschleunigung."),
                         ("c), d) 5 m in 4 s", "v = 1,25 m/s · mal 3,6 = 4,5 km/h"), ("e) 2 kg, 3 m/s²", "F = m · a = 6 N")]),
        2: ("Freigabe je Gruppe", [(q, "ja – sonst nachbessern lassen") for q in GD.FREIGABE_FRAGEN]),
        3: ("Probe am Platz", [("Was sieht man?", "Eine Beobachtung in einem Satz – ohne Erklärung."), ("Was ist die Erklärung?", "Mit dem Fachbegriff des Themas.")]),
        4: ("Partnercheck", [("Ist der Steckbrief ohne die Gruppe verständlich?", "Zwei Stärken, eine Sache, die noch fehlt."),
                             ("Stimmt die Formel samt Einheit?", "Siehe Kernaussagen je Gruppe unten.")]),
        5: ("Nach den Präsentationen", [("Ist Druck eine eigene Kraftart?", "Nein: p = F / A verbindet Kraft und Fläche."),
                                        ("Auftrieb beim ruhigen Schwimmen?", "So groß wie die Gewichtskraft (Gleichgewicht)."),
                                        ("Fachlicher Fehler in einem Steckbrief?", "Hier kurz richtigstellen – die Gruppe bessert das Handout in Teams aus.")]),
        6: ("Aufgabe 8 und Denkfehler", [("Drei Denkfehler", "Auftrieb im Gleichgewicht · Reibung kann antreiben · Gegenkraft wirkt auf den anderen Körper."),
                                         ("Rechenwege a, e, i, j", "60 N · 6000 Pa · 1,5 m/s · 4 m/s²")])}
for n in sorted(BESP):
    t_, xs = BESP[n]
    besp += (f"<details class='card'{' open' if n == 1 else ''}><summary><span class='nr'>{n}</span><span class='ttl'>{e(I.STUNDENNAME[n])}</span><span class='tag besp'>{e(t_)}</span></summary>"
             "<div class='body'>" + "".join(f"<p class='q'>{md(q)}</p><div class='box sol'>{md(a)}</div>" for q, a in xs) + "</div></details>")
besp += "<h2>Kernaussage je Gruppenthema</h2>" + tab(["Gruppe", "Thema", "Das muss im Steckbrief stehen"], [[str(g), GD.THEMEN[g], LG.KERN[g]] for g in range(1, 8)])
besp += "<h2>Die 5 größten Stolpersteine</h2>" + "".join(f"<div class='fehler'><b class='k'>{e(a)}</b>{md(b)}</div>" for a, b in I.STOLPERSTEINE)
besp += "<h2>So bewertest du das Projekt</h2>" + tab(["Teil", "Punkte", "Woran du es siehst"], [[a, str(b), c] for a, b, c in GD.RASTER]) + ul([
    "**Notenschlüssel Projekt (10 Punkte):** ab 8,8 Sehr gut · ab 7,5 Gut · ab 6,2 Befriedigend · ab 5 Genügend · darunter Nicht genügend.",
    "**Automatisch geprüft** werden nur Aufgabe 2 (5 Felder) und Aufgabe 8 (10 Felder). Die Projektaufgaben 3–7 stehen im PDF als »bewertet Prof. HOLZER nach dem Raster«.",
    "**Musterlösungen** sehen die Kadetten erst, wenn Aufgabe 8 ausgefüllt und ein PDF erstellt ist – die Zwischenstand-PDFs der Stunden 1–5 schalten sie nicht frei."])

# ---------------------------------------------------------------- Aufgaben
auf = []
for t in I.T:
    tags = [f"<span class='tag{' zus' if t['h'] == 0 else ''}'>{e(t['tag'])} · {t['zeit']} min</span>"]
    if t.get("besprechen"): tags.append("<span class='tag besp'>BESPRECHEN</span>")
    if t.get("projekt"): tags.append("<span class='tag bew'>du bewertest (Raster)</span>")
    if t.get("marke"): tags.append(f"<span class='tag'>{e(t['marke'])}</span>")
    if t["id"] == "v0": tags.append("<span class='tag bew'>ohne Punkte</span>")
    felder = "".join(
        f"<li>{e(f[1])}" + (f" <span class='klein'>({' · '.join(e(o) for o in f[2])})</span>" if len(f) > 2 and isinstance(f[2], (list, tuple)) else "") + "</li>"
        for f in t.get("fields", []))
    sol = "".join(f"<p>{'' if h in ('Lösung', 'Beispiel', 'Bewertung') else '<b>' + e(h) + '</b> '}{md(x)}</p>" for h, xs in t["sol"] for x in xs)
    tipps = ""
    if t.get("tipps"):
        k = t["tipps"][1]
        karte = TD.KARTEN.get(k, {}).get("titel", k)
        tipps = ("<div class='box fach'><b class='k'>Tippstufen (freiwillig, kosten keine Punkte)</b>"
                 f"<p><b>1 · Denkanstoß</b> {md(t['tipps'][0])}</p><p><b>2 · Theorie-Karte</b> {e(karte)}</p><p><b>3 · Buch</b> {md(t['tipps'][2])}</p></div>")
    auf.append(f"<details class='card' data-h='{t['h']}' data-s='{html.escape((t['title'] + ' ' + t['q']).lower(), quote=True)}'>"
               f"<summary><span class='nr'>{t['nr']}</span><span class='ttl'>{e(t['title'])}</span>{''.join(tags)}</summary>"
               f"<div class='body'><p class='q'>{md(t['q'])}</p><p class='klein'>{e(t['src'])}</p>"
               + (f"<ul class='felder'>{felder}</ul>" if felder else "")
               + f"<div class='box sol'><b class='k'>Lösung</b>{sol}</div>" + tipps
               + (f"<p class='klein'>Hinweis für Kadetten: {md(t['hint'])}</p>" if t.get("hint") else "") + "</div></details>")

filt = "".join(f"<button type='button' data-f='{h}' aria-pressed='false'>{e(I.GRP[h].split(' · ')[0])}</button>" for h in (1, 2, 3, 4, 5, 6, 0))
aufgaben = (f"<input class='search' type='search' id='suche' placeholder='Aufgaben durchsuchen' aria-label='Aufgaben durchsuchen'>"
            f"<div class='filter' id='filter'>{filt}</div>" + "".join(auf) + "<p class='leer' id='leer' hidden>Nichts gefunden.</p>"
            + "<h2>Gruppenkarten mit Musterantworten (Aufgabe 3)</h2>"
            + "".join(f"<details class='card'><summary><span class='nr'>{g}</span><span class='ttl'>{e(GD.G[g]['titel'])}</span><span class='tag'>{e(GD.G[g]['buch'])}</span></summary><div class='body'>"
                      + "".join(f"<p class='q'>{md(q)}</p><div class='box sol'>{md(a)}</div>" for q, a in zip(GD.G[g]["leit"], LG.LF[g]))
                      + f"<p class='klein'><b>Formel:</b> {md(GD.G[g]['formel'])}</p></div></details>" for g in range(1, 8))
            + "<h2>Quizfragen (Kräfte-Check) mit Lösung</h2>"
            + tab(["Thema", "Frage", "Richtig", "Erklärung", "Buch"],
                  [[q[0], q[1], q[2][0], q[3], q[4]] for q in I.QUIZ]))

# ---------------------------------------------------------------- Versuche (7 Gruppen)
vs = (f"<p><b>{e(I.VS_ID)} · Gruppenprojekt mit selbst gewähltem Versuch.</b> Es gibt <b>keine Demonstration</b> von dir in Stunde 3 – "
      "jede Gruppe macht ihren eigenen <b>Versuch</b>. Je Gruppe stehen zuerst die drei Ideen von der Gruppenkarte, darunter die erprobte Beschreibung von Idee 1 "
      "mit Beispielwerten (keine Messdaten). Gruppen, die keine Freigabe bekommen oder Material vergessen, nehmen Idee 1.</p>")
for v in VD.VS:
    bild = UNIT + "vs-img/d_" + v["skizze"] + ".png"
    kopf = (f"<div class='vsgrid'><div><p>{md(v['intro'])}</p>"
            f"<p class='klein'>{e(v['form'])} · ca. {v['zeit']} min · {e(v['wann'])} · {e(v['bindung'])}</p>"
            f"<div class='box fach'><b class='k'>Wo steht der Versuch?</b>{e(v['platz'])}</div>"
            f"<div class='fehler'><b class='k'>Sicherheit</b>{md(v['sicher'])}</div></div>"
            + (f"<img src='{b64(bild, 'image/png')}' alt='Aufbau {e(v['titel'])}'>" if os.path.exists(bild) else "") + "</div>")
    mat = tab(["Material", "Inventar / Fundort", "Stück"],
              [[m[0], VD.LM[m[2]][2], str(m[3])] for m in v["mat"]])
    schritte = "<h3>Durchführung</h3><ol>" + "".join(f"<li>{md(s)}</li>" for s in v["schritte"]) + "</ol>"
    beob = "<h3>Beispielwerte (erfunden – das Ergebnis ist offen)</h3>" + tab(
        v["beob"]["kopf"], [z + list(v["erwartet_tab"][i]) for i, z in enumerate(v["beob"]["zeilen"][:len(v["erwartet_tab"])])])
    erw = "".join(f"<div class='box fach'><b class='k'>Erwartet: {e(a)}</b>{md(b)}</div>" for a, b in v["erwartet"])
    deut = "".join(f"<div class='box sol'><b class='k'>{lab}</b><p class='q'>{md(v[k])}</p><p>{md(v[k + '_l'])}</p></div>"
                   for k, lab in (("erk", "Erkenntnis"), ("interp", "Interpretation"), ("schluss", "Schlussfolgerung")))
    rest = ("<h3>Tipps für dich</h3>" + ul(v["lehrer"]) + "<h3>Typische Pannen</h3>"
            + "".join(f"<div class='fehler'>{md(x)}</div>" for x in v["fehler"])
            + "<h3>Fachlich genau</h3>" + "".join(f"<div class='box fach'>{md(x)}</div>" for x in v["fach"])
            + f"<div class='box bew'><b class='k'>Vorher selbst ausprobieren</b>{md(v['vorversuch'])}</div>"
            + f"<p class='klein'><b>Wegräumen:</b> {e(v['entsorgung'])}</p>"
            + f"<p class='klein'>Quelle: {e(v['quelle'])} · {e(v['jp'])}</p>")
    G_ = GD.G[v["gruppe"]]
    ideen = ("<h3>Ideen von der Gruppenkarte</h3><ol>" + "".join(f"<li>{md(x)}</li>" for x in G_["ideen"]) + "</ol>"
             + "<p class='klein'><b>Im Saal:</b> " + e(" · ".join("%s %s (Bestand %d)" % m for m in G_["saal"])) + "</p>"
             + f"<p class='klein'><b>Von zu Hause:</b> {e(G_['haus'])}</p><div class='fehler'><b class='k'>Achtung</b>{e(G_['achtung'])}</div>"
             + "<h3>Idee 1 genauer (erprobte Beschreibung)</h3>")
    kopf = ideen + kopf
    vs += (f"<details class='card'><summary><span class='nr'>{v['gruppe']}</span><span class='ttl'>{e(GD.THEMEN[v['gruppe']])}: {e(v['titel'])}</span>"
           f"<span class='tag'>{e(v['buch']['s'])}</span>{'<span class=\"tag\">KERN</span>' if v.get('kern') else '<span class=\"tag zus\">ZUSATZ</span>'}</summary>"
           f"<div class='body'>{kopf}<h3>Material</h3>{mat}{schritte}{beob}{erw}{deut}{rest}</div></details>")

vs += "<h2>Material von zu Hause</h2>" + tab(["Erlaubt", "Nicht erlaubt"], [[a, b] for a, b in zip(GD.ZUHAUSE_JA + [""] * 6, GD.ZUHAUSE_NEIN)])

# ---------------------------------------------------------------- Fachwissen
fw = "<h2>Lehrplanbezug</h2><ul>" + "".join(f"<li><b>{e(a)}</b> {md(b)}</li>" for a, b in F.LEHRPLAN) + "</ul>"
fw += "<h2>Die Theorie in Kurzform</h2>"
for k, karte in TD.KARTEN.items():
    bild = UNIT + karte["bild"] if karte.get("bild") else None
    fw += (f"<details class='card'><summary><span class='nr'>{e(k[1:])}</span><span class='ttl'>{e(karte['titel'])}</span>"
           f"<span class='tag'>{e(karte['buch'])}</span></summary><div class='body'>"
           + "".join(f"<p>{md(s)}</p>" for s in karte["satz"])
           + (f"<div class='bild'><img src='{b64(bild, 'image/png')}' alt='{e(karte.get('alt', ''))}'></div>" if bild and os.path.exists(bild) else "")
           + "</div></details>")
fw += "<h2>Wo die Quellen verkürzen – und was hier steht</h2>" + tab(["Quelle", "Verkürzung", "Verwendete Fassung"], F.KORREKTUREN)
fw += "<h2>Häufige Fehlvorstellungen</h2>" + tab(["Fehlvorstellung", "Richtig ist", "So zeigst du es"], F.FEHLVORSTELLUNGEN)
fw += "<h2>Fragen, die Kadetten stellen</h2>" + "".join(f"<p><b>{e(q)}</b><br>{md(a)}</p>" for q, a in F.FRAGEN)
fw += "<h2>Rechenkontrolle</h2>" + ul(F.RECHENKONTROLLE)
fw += "<h2>Fachbegriffe</h2>" + tab(I.FACHBEGRIFFE[0], I.FACHBEGRIFFE[1:])
fw += "<h2>Videos</h2>" + tab(["Video", "Wo eingebaut", "Link"], [
    [f"Apolin: {GD.NEWTON[1]['titel']} (Trägheit)", "Theorie Teil 1 · Gruppenkarten 1 und 4 · PPP Stunde 1 (optional)", GD.NEWTON[1]["url"]],
    [f"Apolin: {GD.NEWTON[2]['titel']} (F = m · a)", "Theorie Teil 1 · Gruppenkarten 1 und 2 · PPP Stunde 1 (optional)", GD.NEWTON[2]["url"]],
    [f"Apolin: {GD.NEWTON[3]['titel']} (Kraft und Gegenkraft)", "Theorie Teil 8 · Gruppenkarte 7 · PPP Stunde 1 (optional)", GD.NEWTON[3]["url"]],
    ["Action = Reaction (Pohl, TIB AV-Portal, 1 min)", "Gruppenkarte 7 (zusätzlich)", "https://av.tib.eu/media/30463"]]) + ul([
    "Die Apolin-Links hast du ausgewählt; von hier aus war YouTube gesperrt. **Bitte einmal Länge und Inhalt prüfen** – die Beobachtungsfragen sind nach Titel und Thema formuliert.",
    "In Stunde 1 ist für die Videos keine eigene Zeit eingeplant. Die Folie zeigt die QR-Codes; einen Ausschnitt nur zeigen, wenn Zeit bleibt.",
    "Gute Wahl für die Supplierstunde (Stunde 6): Video 2 oder 3 mit den Beobachtungsfragen vor Aufgabe 8."])
fw += "<h2>Ausblick</h2><p>" + md(F.AUSBLICK) + "</p>"
fw += "<h2>Geprüfte Quellen</h2><ul>" + "".join(
    f"<li><b>{e(q[0])} – {e(q[1])}</b><br>{e(q[2])}<br><span class='mono'>{e(q[3])}</span></li>" for q in I.QUELLEN) + "</ul>"
fw += "<h2>Nicht geprüft – nicht eingebaut</h2>" + ul(I.NICHT_GEPRUEFT)

# ---------------------------------------------------------------- Folien (TH-Unterricht als Bilder)
prs = Presentation(PPTX)
titel = [next((ph.text_frame.text for ph in s.placeholders if ph.placeholder_format.type == 1), "") for s in prs.slides if s._element.get("show") != "0"]
bilder = sorted(glob.glob(os.path.join(FOLDIR, "s-*.jpg")))
assert len(bilder) == len(titel), (len(bilder), len(titel))
nr_phys = [i + 1 for i, s in enumerate(prs.slides) if s._element.get("show") != "0"]
folien_js = json.dumps([[b64(b, "image/jpeg"), t, n] for b, t, n in zip(bilder, titel, nr_phys)], ensure_ascii=False).replace("</", "<\\/")
optionen = "".join(f"<option value='{i}'>Folie {n} · {e(t)}</option>" for i, (t, n) in enumerate(zip(titel, nr_phys)))

gen = ("<p>Zufällige Einteilung in sieben Gruppen. Füge die Namen deiner Klasse einmal ein (ein Name pro Zeile, z. B. aus der Klassenliste kopiert). "
       "<b>Die Namen bleiben nur in diesem Browser</b> – sie werden nirgends hochgeladen. Mit »Behalten« bleibt die Einteilung für alle sechs Stunden gleich.</p>"
       "<div class='steuer'><label class='klein' for='g-kl'>Klasse</label><select id='g-kl'>" + "".join(f"<option>{e(k)}</option>" for k in I.KLASSEN) + "</select>"
       "<label class='klein' for='g-n'>Gruppen</label><select id='g-n'>" + "".join(f"<option{' selected' if n == 7 else ''}>{n}</option>" for n in range(4, 9)) + "</select></div>"
       "<textarea id='g-namen' rows='8' class='search' placeholder='Ein Name pro Zeile …' aria-label='Namen der Klasse, ein Name pro Zeile'></textarea>"
       "<div class='steuer'><button type='button' class='btn' id='g-los'>Auslosen</button><button type='button' class='btn ghost' id='g-halt'>Behalten</button>"
       "<button type='button' class='btn ghost' id='g-kopie'>Kopieren</button><button type='button' class='btn ghost' id='g-gross'>Groß für den Beamer</button></div>"
       "<p class='klein' id='g-info' role='status' aria-live='polite'></p><div id='g-aus' class='g-raster'></div>"
       "<div id='g-voll' hidden role='dialog' aria-modal='true' aria-label='Gruppeneinteilung groß'><button type='button' class='btn' id='g-zu'>Schließen</button><div class='g-raster gross' id='g-voll-in'></div></div>")
THEMEN_JS = json.dumps({str(k): v for k, v in GD.THEMEN.items()}, ensure_ascii=False)
STIL = open(os.path.join(HERE, "loesungsmappe_stil.css"), encoding="utf-8").read()
ZUSATZ = """
.werkzeug { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; margin: 10px 0 14px; }
.zaehler { font-weight: 700; color: var(--olive); }
.balken { flex: 1 1 140px; height: 10px; border-radius: 999px; background: #dfe4d2; overflow: hidden; }
.balken i { display: block; height: 100%; width: 0; background: var(--olive); transition: width .2s; }
.vsgrid { display: grid; grid-template-columns: 1fr; gap: 12px; align-items: start; }
.vsgrid img { width: 100%; height: auto; border-radius: 10px; background: #fff; }
@media (min-width: 760px) { .vsgrid { grid-template-columns: 1.1fr 1fr; } }
table.kal tr.jetzt td { background: var(--olive-soft); font-weight: 700; }
@media (max-width: 620px) { table.kal tr:first-child { display: none; } table.kal tr { display: block; border-bottom: 2px solid var(--line); padding: 6px 0; }
  table.kal td { display: block; border: 0; padding: 1px 8px; } table.kal td.num { width: auto; } }
.g-raster { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; margin-top: 10px; }
.g-raster .g { background: var(--surface); border: 2px solid var(--olive); border-radius: 12px; padding: 8px 10px; }
.g-raster .g b { display: block; color: var(--olive); font-family: var(--serif); }
.g-raster .g span { display: block; font-size: 13px; color: var(--teal); font-weight: 700; margin-bottom: 4px; }
#g-voll { position: fixed; inset: 0; z-index: 50; background: #fff; overflow: auto; padding: 16px; }
.g-raster.gross { grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }
.g-raster.gross .g { font-size: 24px; } .g-raster.gross .g b { font-size: 28px; } .g-raster.gross .g span { font-size: 18px; }
#g-namen { min-height: 160px; font: 16px var(--sans); }
"""
seite = f"""<title>Lösungsmappe Mechanische Kräfte 1AB</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="schriften/schriften.css">
<style>{STIL}{ZUSATZ}</style>
<div class="wrap">
<header class="lese">
  <div class="eyebrow">NAWI · 1AB (1AK, 1BK) · K2.1 Mechanische Kräfte · nur für dich</div>
  <h1>Lösungen und Fachwissen: sechs Stunden mit Gruppenprojekt</h1>
  <p class="sub">Aufgaben 1–11 (9–11 Zusatz), sieben Gruppen mit selbst gewähltem Versuch, Kalender beider Klassen, Vorbereitung nach Tagen,
     Gruppen-Generator, die Unterrichts-PPP als Folien und das Fachwissen. Buch: Trauner NAWI HAK 1, S. 44–65. Stand {e(I.STAND)} · {e(I.V)}</p>
  <p class="warn">Privat in deinem Konto – nicht an Kadetten weitergeben und nicht ins Repository legen.
     Die Kadetten sehen Musterlösungen erst nach Aufgabe 8 und dem PDF bzw. nach drei Fehlversuchen.</p>
</header>
<nav class="tabs" role="tablist" aria-label="Bereiche">
  <button role="tab" id="t-kalender" aria-selected="true">Kalender</button>
  <button role="tab" id="t-vorbereitung" aria-selected="false">Vorbereitung</button>
  <button role="tab" id="t-besprechen" aria-selected="false">Besprechen</button>
  <button role="tab" id="t-aufgaben" aria-selected="false">Aufgaben ({len(I.T)})</button>
  <button role="tab" id="t-versuche" aria-selected="false">Versuche (7 Gruppen)</button>
  <button role="tab" id="t-gruppen" aria-selected="false">Gruppen</button>
  <button role="tab" id="t-folien" aria-selected="false">Folien</button>
  <button role="tab" id="t-fachwissen" aria-selected="false">Fachwissen</button>
</nav>
<section class="panel lese" id="p-kalender">{kal}</section>
<section class="panel lese" id="p-vorbereitung" hidden>{vb}</section>
<section class="panel lese" id="p-besprechen" hidden>{besp}</section>
<section class="panel lese" id="p-aufgaben" hidden>{aufgaben}</section>
<section class="panel lese" id="p-versuche" hidden>{vs}</section>
<section class="panel lese" id="p-gruppen" hidden>{gen}</section>
<section class="panel" id="p-folien" hidden>
  <div class="steuer"><button class="btn ghost" id="f-zur" type="button">◀ zurück</button><button class="btn" id="f-vor" type="button">weiter ▶</button>
  <select id="f-wahl" aria-label="Folie wählen">{optionen}</select><button class="btn ghost" id="f-voll" type="button">Vollbild</button></div>
  <div class="buehne" id="buehne" tabindex="0"><img id="f-img" alt=""></div>
  <p class="hilfe">Die {len(titel)} sichtbaren Folien der TH-Unterricht (Lösungen sind hier schon aufgedeckt). Weiter: Tippen rechts, Pfeiltaste oder Leertaste ·
     zurück: Tippen links · Vollbild: Knopf oder Taste F. Die Foliennummer entspricht der Nummer in PowerPoint.</p>
</section>
<section class="panel lese" id="p-fachwissen" hidden>{fw}</section>
<footer class="lese">Gebaut aus werkzeug/quellen/1ab-k2-1-kraefte (eine Datenquelle für Handy-Seiten, Unterrichts-PPP und diese Mappe) · Stand {e(I.STAND)}</footer>
</div>
<script>
const F={folien_js};
const tabs=[...document.querySelectorAll('nav.tabs button')];
function zeige(id){{tabs.forEach(b=>{{const on=b.id==='t-'+id;b.setAttribute('aria-selected',on);document.getElementById('p-'+b.id.slice(2)).hidden=!on;}});try{{localStorage.setItem('k21-tab2',id)}}catch(e){{}}}}
tabs.forEach(b=>b.addEventListener('click',()=>zeige(b.id.slice(2))));
try{{const t=localStorage.getItem('k21-tab2');if(t&&document.getElementById('p-'+t))zeige(t)}}catch(e){{}}
// Herrichten: Haken merken, zählen, filtern
const PRE='k21-';
function warnung(){{const h=document.getElementById('speicherhinweis');if(h){{h.hidden=false;return;}}
  const p=document.createElement('p');p.id='speicherhinweis';p.setAttribute('role','status');p.setAttribute('aria-live','polite');
  p.style.cssText='background:#fff3cd;color:#5c4400;border:1px solid #d9b44a;padding:8px 12px;margin:8px 0;border-radius:6px';
  p.textContent='Diese Vorbereitungshaken konnten nicht gespeichert werden. Sie gelten nur für die aktuelle Sitzung.';
  const n=document.querySelector('nav.tabs');(n?n.parentNode:document.body).insertBefore(p,n?n.nextSibling:document.body.firstChild);}}
function sichern(k,v){{try{{localStorage.setItem(PRE+k,v)}}catch(e){{warnung()}}}}
try{{localStorage.setItem(PRE+'probe','1');localStorage.removeItem(PRE+'probe')}}catch(e){{warnung()}}
const haken=[...document.querySelectorAll('#p-vorbereitung input[data-k]')];
let nurOffen=false;
function stand(){{const n=haken.filter(c=>c.checked).length;
  document.getElementById('h-zaehler').textContent=n+' von '+haken.length+' abgehakt';
  document.getElementById('h-balken').style.width=(haken.length?100*n/haken.length:0)+'%';
  haken.forEach(c=>{{const li=c.closest('li');if(li)li.hidden=nurOffen&&c.checked;}});}}
haken.forEach(c=>{{try{{c.checked=localStorage.getItem(PRE+c.dataset.k)==='1'}}catch(e){{}}
  c.addEventListener('change',()=>{{sichern(c.dataset.k,c.checked?'1':'0');stand();}});}});
document.getElementById('h-nur').addEventListener('click',ev=>{{nurOffen=!nurOffen;ev.currentTarget.setAttribute('aria-pressed',nurOffen);
  ev.currentTarget.textContent=nurOffen?'Alle zeigen':'Nur offene zeigen';stand();}});
stand();
// Kalender und Vorbereitung: nächster Termin
(function(){{const d=new Date(),h=String(d.getFullYear()*10000+(d.getMonth()+1)*100+d.getDate());
  const z=[...document.querySelectorAll('table.kal tr[data-d]')];const n=z.find(r=>r.dataset.d>=h);if(n)n.classList.add('jetzt');
  const k=[...document.querySelectorAll('details.tag-karte')];const m=k.find(x=>x.dataset.d>=h);if(m){{k.forEach(x=>x.open=false);m.open=true;}}}})();
// Gruppen-Generator (Namen nur in diesem Browser)
const TH={THEMEN_JS};
const gk=document.getElementById('g-kl'),gn=document.getElementById('g-n'),ga=document.getElementById('g-namen'),gi=document.getElementById('g-info'),gaus=document.getElementById('g-aus');
let EIN=null;
function lies(k){{try{{return localStorage.getItem('k21-'+k)}}catch(e){{return null}}}}
function schreib(k,v){{try{{localStorage.setItem('k21-'+k,v);return true}}catch(e){{warnung();return false}}}}
function zeigeEin(z,ein){{z.textContent='';(ein||[]).forEach((g,i)=>{{const d=document.createElement('div');d.className='g';
  const b=document.createElement('b');b.textContent='Gruppe '+(i+1);const s=document.createElement('span');s.textContent=TH[i+1]||'';d.append(b,s);
  g.forEach(n=>{{const p=document.createElement('div');p.textContent=n;d.append(p)}});z.append(d)}});}}
function laden(){{ga.value=lies('namen-'+gk.value)||'';let e=null;try{{e=JSON.parse(lies('ein-'+gk.value)||'null')}}catch(x){{}}EIN=e;zeigeEin(gaus,EIN);
  gi.textContent=EIN?'Behaltene Einteilung für '+gk.value+'.':'Noch keine Einteilung behalten.';}}
gk.onchange=laden;ga.addEventListener('input',()=>schreib('namen-'+gk.value,ga.value));
document.getElementById('g-los').onclick=()=>{{const N=ga.value.split(/\\n/).map(x=>x.trim()).filter(Boolean);const n=+gn.value;
  if(N.length<n){{gi.textContent='Bitte mindestens '+n+' Namen eingeben.';return}}
  for(let i=N.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[N[i],N[j]]=[N[j],N[i]]}}
  EIN=Array.from({{length:n}},()=>[]);N.forEach((x,i)=>EIN[i%n].push(x));zeigeEin(gaus,EIN);gi.textContent='Neu ausgelost ('+N.length+' Kadetten) – mit »Behalten« speichern.';}};
document.getElementById('g-halt').onclick=()=>{{if(!EIN)return;if(schreib('ein-'+gk.value,JSON.stringify(EIN)))gi.textContent='Einteilung für '+gk.value+' behalten.';}};
document.getElementById('g-kopie').onclick=()=>{{if(!EIN)return;const t=EIN.map((g,i)=>'Gruppe '+(i+1)+' · '+(TH[i+1]||'')+': '+g.join(', ')).join('\\n');
  try{{navigator.clipboard.writeText(t).then(()=>gi.textContent='Kopiert.',()=>gi.textContent=t)}}catch(e){{gi.textContent=t}}}};
const gv=document.getElementById('g-voll');
document.getElementById('g-gross').onclick=()=>{{if(!EIN)return;zeigeEin(document.getElementById('g-voll-in'),EIN);gv.hidden=false;try{{gv.requestFullscreen&&gv.requestFullscreen().catch(()=>{{}})}}catch(e){{}}}};
document.getElementById('g-zu').onclick=()=>{{gv.hidden=true;try{{document.fullscreenElement&&document.exitFullscreen()}}catch(e){{}}}};
laden();
// Aufgaben: Suche und Filter
const karten=[...document.querySelectorAll('#p-aufgaben details.card')];let fil=null;
function filtern(){{const q=document.getElementById('suche').value.toLowerCase().trim();let n=0;
  karten.forEach(k=>{{const ok=(!q||k.dataset.s.includes(q))&&(fil===null||k.dataset.h===fil);k.hidden=!ok;if(ok)n++;}});document.getElementById('leer').hidden=n>0;}}
document.getElementById('suche').addEventListener('input',filtern);
document.querySelectorAll('#filter button').forEach(b=>b.addEventListener('click',()=>{{fil=(fil===b.dataset.f)?null:b.dataset.f;
  document.querySelectorAll('#filter button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.f===fil));filtern();}}));
// Folien
let i=0;const img=document.getElementById('f-img'),wahl=document.getElementById('f-wahl'),bu=document.getElementById('buehne');
function geh(n){{i=Math.max(0,Math.min(F.length-1,n));img.src=F[i][0];img.alt='Folie '+F[i][2]+': '+F[i][1];wahl.value=i;}}
document.getElementById('f-vor').onclick=()=>geh(i+1);document.getElementById('f-zur').onclick=()=>geh(i-1);wahl.onchange=()=>geh(+wahl.value);
bu.addEventListener('click',ev=>{{const r=bu.getBoundingClientRect();geh(ev.clientX-r.left<r.width/3?i-1:i+1)}});
document.getElementById('f-voll').onclick=()=>{{try{{bu.requestFullscreen&&bu.requestFullscreen().catch(()=>{{}})}}catch(e){{}}}};
document.addEventListener('keydown',ev=>{{if(document.getElementById('p-folien').hidden)return;
  const z=ev.target;if(z&&(/^(INPUT|SELECT|TEXTAREA)$/.test(z.tagName)||z.isContentEditable))return;
  if(ev.key===' '&&z&&/^(BUTTON|A)$/.test(z.tagName))return;
  if(['ArrowRight',' ','PageDown'].includes(ev.key)){{ev.preventDefault();geh(i+1)}}else if(['ArrowLeft','PageUp'].includes(ev.key)){{ev.preventDefault();geh(i-1)}}
  else if(ev.key==='f'||ev.key==='F')document.getElementById('f-voll').click();}});
geh(0);
</script>
"""
open(ZIEL, "w", encoding="utf-8").write(seite)
print("ok", ZIEL, len(seite) // 1024, "KB ·", len(titel), "Folien ·", n_haken, "Haken")
