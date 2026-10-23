"""Handy-Seiten NAWI 3AB · K2.3a Ernährungsweisen bauen (Theorie-Seite, Arbeitsblatt, Quiz).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/3ab-k2-3a-ernaehrung/bauen.py
Arbeitsblatt-Grundlage: 2ak-pbgw/k1-grundrechte/aufgaben.html (Engine schon mit Select-Mischung und
Zahlen-Erkennung gepatcht – Muster werkzeug/quellen/2ak-k1-grundrechte/bauen.py).
Danach: python3 werkzeug/pdf_hilfe_einbauen.py und python3 werkzeug/build_index.py"""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
from daten import T, STAND

UNIT = I.ORDNER + "/"
DST = os.path.join(ROOT, UNIT)
os.makedirs(DST, exist_ok=True)
esc = html.escape
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
CAMO, LOGO, SMILEY = b64(WZ + "/camo.png"), b64(WZ + "/logo.png"), b64(WZ + "/smiley.png")
nb = lambda s: re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
md = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(nb(s)))


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


FAHRPLAN_ROWS = [["Stunde 1", "Teil 1 · Personengruppen + Teil 2 · Alternative Ernährungsformen", "1–2", "am Handy", "–"],
                 ["Stunde 2", "Teil 2.1 · Vegetarismus + Teil 2.2 · Vollwerternährung, dann Quiz", "3–6 · Quiz", "3, 5, 6 am Handy · 4 ohne Handy (Gruppen zu viert)", "PDF in LMS"],
                 ["Für Schnelle", "Für Schnelle und Neugierige", "7", "am Handy", "freiwillig"]]
FAHRPLAN = ('<section class="fahrplan"><div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2><p class="std">Dafür sind 2 Stunden eingeplant.</p>'
            '<p>Lies die <strong>Theorie-Seite</strong> Teil für Teil, mach die passenden <strong>Aufgaben</strong> im Arbeitsblatt, teste dich mit dem <strong>Quiz</strong> '
            'und gib nach Stunde 2 das <strong>PDF</strong> ab.</p><div class="tablewrap"><table><thead><tr><th>Wann</th><th>Das machen wir</th><th>Aufgaben</th><th>Wie</th><th>Abgabe</th></tr></thead><tbody>'
            + "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in FAHRPLAN_ROWS) + "</tbody></table></div></section>")

# ================================================================ Arbeitsblatt
s = open(os.path.join(ROOT, "2ak-pbgw/k1-grundrechte/aufgaben.html"), encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (old[:80], n); s = s.replace(old, new)


TITLE = "Ernährungsweisen-Aufgaben"
rep("<title>Menschenrechte-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("PBGW · 2AK · K1 Grund- und Menschenrechte</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Menschenrechte-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Menschenrechte-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>2AK</option>', '<option value="">–</option><option>3A</option><option>3B</option>')
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Lies zuerst den passenden Teil der <a href="theorie.html">Theorie-Seite</a>, dann die Aufgaben in die <b>gelben Felder</b> – alles wird am Handy gespeichert.</li>
      <li><b>Stunde 1</b>: 1–2 · <b>Stunde 2</b>: 3–6 (Aufgabe 4 in der Gruppe zu viert) · <b>Für Schnelle</b>: 7.</li>
      <li>Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Nach Stunde 2 ganz unten <b>PDF erstellen</b> und in LMS hochladen.</li>
    </ol>""" + s[j:]
i = s.index('<section class="fahrplan">'); j = s.index("</section>", i) + 10
s = s[:i] + FAHRPLAN + s[j:]
rep("0 von 11 bearbeitet", "0 von %d bearbeitet" % len(T))
rep("Stand 18.10.2026 · v3", "Stand " + STAND + " · " + I.V)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = s[:i] + 'const KEY = "%s";\nconst KAP = "K2.3a", THEMA = "Ernaehrungsweisen";\nconst T = ' % I.KEY + json.dumps(T, ensure_ascii=False, indent=1) + ";" + s[j:]
rep('else if (t.h === 1) open.push(t.nr);', 'else if (t.h === 1 || t.h === 2) open.push(t.nr);')
rep('"Noch offen (Stunde 1): Aufgabe "', '"Noch offen (Stunde 1 und 2): Aufgabe "')
rep('"Alle Aufgaben aus Stunde 1 bearbeitet."', '"Alle Pflicht-Aufgaben 1–6 bearbeitet."')
rep('KAP + " Grund- und Menschenrechte – Aufgaben"', 'KAP + " Ernaehrungsweisen – Aufgaben"')
rep('clean("PBGW · 2AK · K1 Grund- und Menschenrechte · Schulbuch S. 46–58")', 'clean("NAWI · 3AB · K2.3a Ernaehrungsweisen · Schulbuch S. 68–72")')
rep('d.text("Menschenrechte-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
assert not re.search(r"Menschenrechte|2AK|Grundrechte", _plain), re.findall(r".{60}(?:Menschenrechte|2AK|Grundrechte).{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Ernährungsweisen-Check – Quiz</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Ernährungsweisen-Check</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Ernährungsweisen-Check am Handy</h2>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Ernährungsweisen-Check"')
qv = qv.replace('Frage 1 von 16', 'Frage 1 von %d' % len(I.QUIZ))
a, b = qv.index("const Q = ["), qv.index("];", qv.index("const Q = [")) + 2
qv = qv[:a] + "const Q = [\n" + qs + "\n];" + qv[b:]
qv = qv.replace("if (p >= 13) return", "if (p >= %d) return" % (len(I.QUIZ) - 3)).replace("if (p >= 9) return", "if (p >= %d) return" % (len(I.QUIZ) // 2 + 2))
if "[hidden]" not in qv: qv = qv.replace("<style>", "<style>\n[hidden] { display: none !important; }", 1)
for k, v_ in {"__CAMO__": CAMO, "__LOGO__": LOGO, "__SMILEY__": SMILEY, "__QR__": qr_b64(I.URL + "quiz.html")}.items(): qv = qv.replace(k, v_)
assert not re.search(r"__[A-Z]+__", qv) and "Bindung" not in qv


def wrap(src):
    te = src.index("</title>") + 8; rest = src[te:]; bs = rest.index("<header")
    return ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="robots" content="noindex">\n' + src[:te] + "\n" + rest[:bs] + "</head>\n<body>\n" + rest[bs:] + "\n</body>\n</html>\n")


open(DST + "quiz.html", "w", encoding="utf-8").write(wrap(qv) if not qv.lstrip().startswith("<!doctype") else qv)

# ================================================================ Theorie-Seite
def slide(title, body, pill=None, sid=None):
    head = f'<div class="slidehead"><h3>{esc(title)}</h3>' + (f'<span class="pill">{esc(pill)}</span>' if pill else "") + "</div>"
    return f'<article class="slide"{" id=" + chr(34) + sid + chr(34) if sid else ""}>{head}{body}</article>'


def tiles(items):
    return '<div class="tiles">' + "".join(f'<div class="tile"><h4>{esc(h)}</h4>{"".join("<p>" + md(x) + "</p>" for x in (b if isinstance(b, list) else [b]) if x)}</div>' for h, b in items) + "</div>"


def table(rows):
    h = "".join(f"<th>{esc(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join((f"<th scope=row>{md(c)}</th>" if k == 0 else f"<td>{md(c)}</td>") for k, c in enumerate(r)) + "</tr>" for r in rows[1:])
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


ul = lambda xs: '<ul class="pts">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ul>"
ol = lambda xs: '<ol class="goals">' + "".join(f"<li>{md(x)}</li>" for x in xs) + "</ol>"
merke = lambda x: f'<div class="merke">{md(x)}</div>'
hint = lambda x: f'<p class="hint">{md(x)}</p>'
stat = lambda z, t: f'<div class="stat"><b>{esc(z)}</b><span>{md(t)}</span></div>'
reveal = lambda q, a: f'<div class="stopq"><p><strong>{md(q)}</strong></p><details class="reveal"><summary>Erst überlegen – dann Lösung anzeigen</summary><p>{md(a)}</p></details></div>'
jetzt = lambda txt, href: f'<a class="jetzt" href="{href}">{esc(txt)} →</a>'

PARTS = [
 ("einstieg", "Einstieg", "Stimmt das?", [
   slide("Drei Behauptungen – stimmt, teilweise oder falsch?", tiles([("„Vegetarische Kost ist langweilig.“", "Auflösung in Aufgabe 5"),
                                                                      ("„Nur viel Fleisch bringt genug Eiweiß.“", "Auflösung in Aufgabe 5"),
                                                                      ("„Vegan ist für alle Menschen das Beste.“", "Auflösung in Aufgabe 5")])),
   slide("Das kannst du nach dieser Einheit", ol(I.LERNZIELE))]),
 ("teil1", "Teil 1 · Stunde 1 · Buch S. 69–70", "Ernährung für Personengruppen", [
   slide("Schwangere", tiles([("Mehrbedarf", "Nur ca. 1.000 kJ (≈ 240 kcal) mehr pro Tag – etwa eine Portion Müsli mit Milch. „Für zwei essen“ ist zu viel."),
                              ("Tabu und Vorsicht", "Alkohol und Zigaretten sind tabu, Koffein nur eingeschränkt, Medikamente nur nach ärztlichem Rat.")]), "Buch S. 69"),
   slide("Sportler", tiles([("Trinken", "Wasser, verdünnte Säfte oder Früchte-/Kräutertees statt Energydrinks."),
                            ("Mahlzeiten", "Mehrere kleine Mahlzeiten statt Riesenportionen."),
                            ("Nährstoffdichte", "Auf das Verhältnis von Nährstoffen zu Energie achten – nicht nur auf die kcal-Zahl.")]), "Buch S. 69"),
   slide("Ältere", tiles([("Weniger Energie", "Muskel- und Knochenmasse nehmen ab → Energiebedarf sinkt, Fett einsparen."),
                          ("Trinken ohne Durst", "Das Durstempfinden lässt nach – bewusst und regelmäßig trinken.")]), "Buch S. 69"),
   slide("Kinder und Jugendliche", tiles([("Mahlzeiten verteilen", "Energie auf mehrere Mahlzeiten verteilen, Frühstück nicht auslassen."),
                                          ("Wenig Süßes und Fett", "Viel Wasser, täglich Obst und Gemüse, Vollkorn statt Weißmehl.")]), "Buch S. 70"),
   slide("Stopp – kannst du das?", reveal("Warum ist „für zwei essen“ für Schwangere zu viel?", "Der tatsächliche Mehrbedarf liegt bei nur ca. 240 kcal pro Tag – das entspricht einer Portion Müsli, nicht einer zweiten Mahlzeit."), "Teil 1"),
   jetzt("Jetzt: Aufgabe 1", "aufgaben.html")]),
 ("teil2", "Teil 2 · Stunde 1 · Buch S. 70–71", "Alternative Ernährungsformen", [
   slide("Die Formen im Überblick", table([["Form", "Erlaubt"], ["vegan", "nur Pflanzliches – auch kein Honig"], ["lakto", "+ Milch und Milchprodukte"],
                                           ["ovo", "+ Eier"], ["ovolakto", "+ Milch und Eier – größte Gruppe, als Dauerkost geeignet"],
                                           ["Pescetarier", "Fisch statt Fleisch"], ["Flexitarier", "selten Fleisch, viel Gemüse, Obst, Fisch"]]), "Buch S. 70–71"),
   slide("Und Vollwerternährung?", merke("**Vollwerternährung** ist keine Form des Vegetarismus, sondern eine eigene Idee: Lebensmittel möglichst natürlich, frisch und wenig verarbeitet – dazu mehr in Teil 2.2."), "Buch S. 71"),
   jetzt("Jetzt: Aufgabe 2", "aufgaben.html")]),
 ("teil21", "Teil 2.1 · Stunde 2 · Buch S. 70–71", "Vegetarismus", [
   slide("Achtung bei Honig und Gelatine", tiles([("Honig", "Bei veganer Kost nicht erlaubt – auch wenn er von Pflanzen stammt."),
                                                  ("Gelatine", "Tierisches Bindemittel aus Knochen und Häuten von Schwein oder Rind – für keine vegetarische Form erlaubt (z. B. in Gummibärchen).")])
         + hint("**Diskussion:** Käse kann mit tierischem Lab hergestellt sein – streng genommen dann nicht vegetarisch."), "Buch S. 70–71"),
   slide("Warum vegetarisch?", ul(["Tiere haben ein Recht auf Leben", "Fleisch als religiöses Tabu", "Ekel vor toten Tieren", "Tierfutter fehlt den Menschen",
                                   "Umwelt: Massentierhaltung", "Gesundheit: weniger Krankheiten"])
         + stat("16 %", "der 15- bis 29-Jährigen in Österreich essen fleischlos – die Zahl hat sich in zehn Jahren verdreifacht."), "Buch S. 70"),
   slide("Bewertung des Vegetarismus", tiles([("Gesundheit", "Vegetarier haben im Schnitt normale Blutzuckerwerte, geringere Cholesterinwerte und seltener Übergewicht."),
                                              ("Vorsicht bei vegan", "Eiweiß, Eisen, Kalzium und Jod können knapp werden – für Säuglinge und Kleinkinder wird abgeraten."),
                                              ("Puddingvegetarismus", "Nur das Fleisch weglassen, aber vor allem Süßes und Mehlspeisen essen – minderwertiger als herkömmliche Kost.")]), "Buch S. 71"),
   slide("Stopp – kannst du das?", reveal("Darf ein Ovolakto-Vegetarier Gummibärchen essen?", "Nein – sie enthalten Gelatine aus Knochen und Häuten.")
         + reveal("Was ist Puddingvegetarismus?", "Fleisch weglassen, aber vor allem Süßes und Mehlspeisen essen – gilt als minderwertiger als herkömmliche Kost."), "Teil 2.1"),
   jetzt("Jetzt: Aufgaben 3–5", "aufgaben.html")]),
 ("teil22", "Teil 2.2 · Stunde 2 · Buch S. 72", "Vollwerternährung", [
   slide("Die Wertstufen", table([["Stufe", "Beispiele", "Einschätzung"],
                                  ["1 + 2", "Gemüse, Obst, Vollkorn, Nüsse", "sehr empfehlenswert – die Hälfte der täglichen Nahrung"],
                                  ["3", "H-Milch, Extrawurst, Konserven", "nur selten"],
                                  ["4", "Fertiggerichte, Pommes, Vitaminpräparate", "übertrieben verarbeitet – nicht empfehlenswert"]]), "Buch S. 72"),
   slide("Nicht ganz unproblematisch", merke("**Kritik laut Buch:** Manche als wenig empfehlenswert eingestufte Lebensmittel können trotzdem sinnvoll sein – H-Milch (Stufe 3) ist zum Beispiel eine gute Kalziumquelle."), "Buch S. 72"),
   slide("Stopp – kannst du das?", reveal("In welche Wertstufe gehören Vitamintabletten?", "Stufe 4 – ein isoliertes, übertrieben verarbeitetes Präparat."), "Teil 2.2"),
   jetzt("Jetzt: Aufgabe 6 und das Quiz", "aufgaben.html")]),
 ("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]),
]
CHECK = "".join(f'<div class="ziel"><p>{md(z)}</p><div class="chips" role="group" aria-label="Selbstcheck">' + "".join(f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht")) + "</div></div>" for k, z in enumerate(I.LERNZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                       slide("Kann ich das?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [
   slide("Verpflegung im Feld", merke("Das Bundesheer verpflegt Soldaten im Feld mit der **Einmannpackung (EPA)**.")
         + hint("Aufgabe 7: Recherchiere kcal und Zusammensetzung der EPA und vergleiche mit dem Tagesbedarf."), "OPTIONAL"),
   jetzt("Jetzt: Aufgabe 7", "aufgaben.html")]))

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1", "teil2": "Teil 2", "teil21": "Teil 2.1", "teil22": "Teil 2.2", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}
toc = "".join(f'<a href="#{p[0]}">{TOCLAB[p[0]]}</a>' for p in PARTS) + '<a href="#weiter">Aufgaben</a>'
body = "".join(f'<section class="part" id="{p[0]}"><div class="band"><div class="eyebrow">{esc(p[1])}</div><h2>{esc(p[2])}</h2></div>{"".join(p[3])}</section>' for p in PARTS)
bt = open(os.path.join(WZ, "vorlagen", "build_theorie.py"), encoding="utf-8").read()
tcss = bt[bt.index("<style>"):bt.index("</style>") + 8].replace("{{", "{").replace("}}", "}")
tcss = tcss.replace("</style>", """.merke { background: var(--olive); color: #fff; border-radius: 12px; padding: 12px 14px; }
.merke strong { color: #C9D8A8; }
ol.goals, ul.pts { margin: 0; padding-left: 24px; display: grid; gap: 6px; }
details.reveal { border: 2px solid #D9772B; border-radius: 12px; padding: 10px 14px; }
details.reveal summary { cursor: pointer; font-weight: 700; color: #D9772B; }
details.reveal p { margin: 8px 0 0; }
.stat { background: #2E7D8C; color: #fff; border-radius: 12px; padding: 12px 14px; display: grid; gap: 4px; }
.stat b { font-family: Cambria, "Source Serif 4", Georgia, serif; font-size: 28px; }
.stat strong { color: #fff; }
.stopq { display: grid; gap: 6px; }
.stopq + .stopq { margin-top: 10px; }
.ziel { border: 1px solid #D3DCC2; border-radius: 12px; padding: 10px 12px; display: grid; gap: 6px; }
.ziel p { margin: 0; }
.chips { display: flex; gap: 8px; flex-wrap: wrap; }
.chip { font: inherit; font-size: 16px; font-weight: 700; color: #3B4A2F; background: #fff; border: 2px solid #D3DCC2; border-radius: 999px; padding: 6px 14px; cursor: pointer; }
.chip[aria-pressed="true"][data-v="sicher"] { background: #E6F0D3; border-color: #7FA83A; }
.chip[aria-pressed="true"][data-v="fast"] { background: #FFF1D6; border-color: #D9772B; }
.chip[aria-pressed="true"][data-v="noch nicht"] { background: #F6E3DF; border-color: #8C3B2E; }
.chip:focus-visible { outline: 3px solid #2E7D8C; outline-offset: 2px; }
.jetzt { display: block; text-align: center; background: #7FA83A; color: #fff; font-weight: 700; font-size: 18px; text-decoration: none; border-radius: 12px; padding: 12px 16px; }
.fahrplan { background: #fff; border: 2px solid #7FA83A; border-radius: 16px; padding: 14px 16px; min-width: 0; }
.fahrplan h2 { font-family: Cambria, "Source Serif 4", Georgia, serif; color: #3B4A2F; margin: 2px 0 6px; } .fahrplan p { margin: 0 0 8px; }
.fahrplan table { width: 100%; border-collapse: collapse; font-size: 15px; } .fahrplan th, .fahrplan td { border-bottom: 1px solid #D3DCC2; padding: 5px 6px; text-align: left; vertical-align: top; }
.fahrplan .tablewrap { overflow-x: auto; max-width: 100%; }
.slide[id], .part { scroll-margin-top: 56px; }
</style>""")
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<title>Ernährungsweisen – Theorie-Seite</title>
<link rel="stylesheet" href="../../schriften/schriften.css">
{tcss}
</head>
<body>
<header class="top">
  <img class="camo" alt="" src="data:image/png;base64,{CAMO}">
  <img class="logo" alt="BHAK Wappen" src="data:image/png;base64,{LOGO}">
  <div class="top-inner">
    <div class="top-text"><div class="eyebrow">{esc(I.EYEBROW)} · {esc(I.BUCH)}</div><h1>{esc(I.TITEL)}</h1></div>
    <img class="smiley" alt="" src="data:image/png;base64,{SMILEY}">
  </div>
</header>
<nav class="toc" aria-label="Inhalt"><div>{toc}</div></nav>
<main>
{FAHRPLAN}
{body}
<section class="next" id="weiter">
  <div class="eyebrow">Weiter geht's</div>
  <h2>Jetzt bist du dran</h2>
  <div class="btns"><a class="btn" href="aufgaben.html">2 · Arbeitsblatt A1–A{len(T)}</a><a class="btn alt" href="quiz.html">3 · Ernährungsweisen-Check (Quiz)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch NAWI 3 (Trauner) S. 68–72.</p>
  <p class="hint">Stand {STAND} · {I.V}</p>
</section>
</main>
<script>
(function () {{
  var KEY = "{I.KEY}-Lernseite-Check", S = {{}};
  try {{ S = JSON.parse(localStorage.getItem(KEY) || "{{}}") || {{}}; }} catch (e) {{ S = {{}}; }}
  var chips = document.querySelectorAll(".chip[data-z]");
  function paint() {{ chips.forEach(function (c) {{ c.setAttribute("aria-pressed", String(S[c.dataset.z] === c.dataset.v)); }}); }}
  chips.forEach(function (c) {{ c.addEventListener("click", function () {{
    S[c.dataset.z] = S[c.dataset.z] === c.dataset.v ? null : c.dataset.v; paint();
    try {{ localStorage.setItem(KEY, JSON.stringify(S)); }} catch (e) {{}}
  }}); }});
  paint();
}})();
</script>
</body>
</html>
"""
open(DST + "theorie.html", "w", encoding="utf-8").write(page)

for f in ["theorie.html", "aufgaben.html", "quiz.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
