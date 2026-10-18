"""Handy-Seiten PBGW 2AK · K1 Grund- und Menschenrechte bauen (Lernseite, Arbeitsblatt, Quiz).
Aufruf im Repository-Ordner:  python3 werkzeug/quellen/2ak-k1-grundrechte/bauen.py
Arbeitsblatt-Grundlage: 4ab-nawi/k1-5a-elektromagnet/aufgaben.html (Sofort-Feedback, Lösungen nach Abgabe, PDF).
Danach: python3 werkzeug/pdf_hilfe_einbauen.py und python3 werkzeug/build_index.py"""
import base64, html, io, json, os, re, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
WZ = os.path.join(ROOT, "werkzeug")
sys.path.insert(0, HERE)
import inhalt as I
from daten import STAND

UNIT = I.ORDNER + "/"
DST = os.path.join(ROOT, UNIT)
os.makedirs(DST, exist_ok=True)
esc = html.escape
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
CAMO, LOGO, SMILEY = b64(WZ + "/camo.png"), b64(WZ + "/logo.png"), b64(WZ + "/smiley.png")
nb = lambda s: re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
md = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(nb(s)))


def qr_b64(url):
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make()
    b = io.BytesIO(); q.make_image(fill_color="#2C3424", back_color="white").save(b, format="PNG"); return base64.b64encode(b.getvalue()).decode()


FAHRPLAN_ROWS = [["Stunde 1", "Teil 1 · Grund- und Menschenrechte", "1–3", "Aufgabe 2 zu zweit ohne Handy", "–"],
                 ["Stunde 2", "Teil 2 · Verstöße", "4–5 · Quiz", "Pro und Contra ohne Handy", "–"],
                 ["Stunde 3", "Arbeitsblatt M1–M4 (Papier) · Teil 3", "6–11", "lesen ohne Handy, dann am Handy", "PDF in LMS"],
                 ["Stunde 4", "Teil 4 · Stolz und Schande 2026", "12 · eure Fragen", "ohne Handy: Vier Ecken, Aufstellen, Diskussion", "–"],
                 ["Für Schnelle", "Für Schnelle und Neugierige", "13–16", "am Handy", "freiwillig"]]
FAHRPLAN = ('<section class="fahrplan"><div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2>'
            '<p>Lies die <strong>Lernseite</strong> Teil für Teil, mach die passenden <strong>Aufgaben</strong> im Arbeitsblatt, teste dich mit dem <strong>Quiz</strong> '
            'und gib nach Stunde 3 das <strong>PDF</strong> ab.</p><div class="tablewrap"><table><thead><tr><th>Stunde</th><th>Lesen</th><th>Aufgaben</th><th>Methode</th><th>Abgabe</th></tr></thead><tbody>'
            + "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in FAHRPLAN_ROWS) + "</tbody></table></div></section>")

# ================================================================ Arbeitsblatt
s = open(os.path.join(ROOT, "4ab-nawi/k1-5a-elektromagnet/aufgaben.html"), encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (old[:80], n); s = s.replace(old, new)


TITLE = "Menschenrechte-Aufgaben"
rep("<title>Elektromagnet-Aufgaben</title>", "<title>" + TITLE + "</title>")
rep("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor</div>", I.EYEBROW + "</div>", 2)
rep("<h1>Elektromagnet-Aufgaben</h1>", "<h1>" + TITLE + "</h1>")
rep("<h2>Elektromagnet-Aufgaben am Handy</h2>", "<h2>" + TITLE + " am Handy</h2>")
s = re.sub(r'(alt="QR-Code zum Arbeitsblatt" src="data:image/png;base64,)[A-Za-z0-9+/=]+', lambda m: m.group(1) + qr_b64(I.URL + "aufgaben.html"), s, count=1)
rep('<option value="">–</option><option>4AK</option><option>4BK</option>', '<option value="">–</option><option>2AK</option>')
i = s.index('<ol class="steps hint">'); j = s.index("</ol>", i) + 5
s = s[:i] + """<ol class="steps hint">
      <li>Lies zuerst den passenden Teil der <a href="theorie.html">Lernseite</a>, dann die Aufgaben in die <b>gelben Felder</b> – alles wird am Handy gespeichert.</li>
      <li><b>Stunde 1</b>: 1–3 · <b>Stunde 2</b>: 4–5 · <b>Stunde 3</b>: 6–11 (Arbeitsblatt M1–M4 auf Papier) · <b>Stunde 4</b>: 12 · <b>Für Schnelle</b>: 13–16.</li>
      <li>Mit <b>»Prüfen«</b> siehst du sofort, ob deine Antwort passt – die Lösung wird dabei nicht verraten.</li>
      <li>Nach Stunde 3 ganz unten <b>PDF erstellen</b> und in LMS hochladen. Deine Frage aus Aufgabe 11 besprechen wir in Stunde 4.</li>
    </ol>""" + s[j:]
i = s.index('<section class="fahrplan">'); j = s.index("</section>", i) + 10
s = s[:i] + FAHRPLAN + s[j:]
rep("0 von 20 bearbeitet", "0 von %d bearbeitet" % len(I.T))
rep('<p class="hint"><a href="theorie.html">Zurück zur Lernseite</a> · <a href="quiz.html">Zum Quiz</a></p>',
    '<p class="hint"><a href="theorie.html">Zur Lernseite</a> · <a href="quiz.html">Zum Quiz</a> · <a href="../">Klassenübersicht</a></p>')
rep("Stand 15.10.2026", "Stand " + STAND + " · " + I.V)
i = s.index("const KEY = "); j = s.index("\n];", i) + 3
s = s[:i] + 'const KEY = "%s";\nconst KAP = "K1", THEMA = "Grundrechte";\nconst T = ' % I.KEY + json.dumps(I.T, ensure_ascii=False, indent=1) + ";" + s[j:]
rep("function fieldsFor(t) {", """const MIX = {};
function mixed(opts) {
  const k = JSON.stringify(opts);
  if (!MIX[k]) { const a = opts.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } MIX[k] = a; }
  return MIX[k];
}
function fieldsFor(t) {""")
rep("f[2] ? selectField(t.id, f[0], f[2], f[1]) : textField(t.id, f[0], f[1], true, 3)",
    "f[2] ? selectField(t.id, f[0], f[3] === false ? f[2] : mixed(f[2]), f[1]) : textField(t.id, f[0], f[1], !(t.chk && t.chk[f[0]] && t.chk[f[0]].num !== undefined), 3)")
rep('else if (t.tag !== "Zusatz") open.push(t.nr);', 'else if (t.h >= 1 && t.h <= 3) open.push(t.nr);')
rep('KAP + " Elektromagnet und Elektromotor – Aufgaben"', 'KAP + " Grund- und Menschenrechte – Aufgaben"')
rep('clean("NAWI · 4AB · K1.5a Elektromagnet und Elektromotor · Schulbuch S. 29–33, 38")', 'clean("PBGW · 2AK · K1 Grund- und Menschenrechte · Schulbuch S. 46–58")')
rep('d.text("Elektromagnet-Aufgaben", M + 15, y + 11.5)', 'd.text("' + TITLE + '", M + 15, y + 11.5)')
rep('"Noch offen (Teil 1 und 2): Aufgabe "', '"Noch offen (Stunde 1–3): Aufgabe "')
rep('"Alle Pflicht-Aufgaben 1–9 bearbeitet."', '"Alle Aufgaben aus Stunde 1–3 bearbeitet."')
i = s.index("const GRP = {"); j = s.index("};", i) + 2
s = s[:i] + "const GRP = " + json.dumps({str(k): v for k, v in I.GRP.items()}, ensure_ascii=False) + ";" + s[j:]
_plain = re.sub(r"[A-Za-z0-9+/=]{200,}", "", s)
assert not re.search(r"Elektromagnet|4AB|K1\.5", _plain), re.findall(r".{60}(?:Elektromagnet|4AB|K1\.5).{20}", _plain)[:5]
open(DST + "aufgaben.html", "w", encoding="utf-8").write(s)

# ================================================================ Quiz
qs = ",\n".join("  { t: %s, q: %s, a: %s, e: %s, p: %s }" % tuple(json.dumps(x, ensure_ascii=False) for x in (t, nb(q), [nb(z) for z in a], nb(e), p)) for t, q, a, e, p in I.QUIZ)
qv = open(os.path.join(WZ, "vorlagen", "quiz_vorlage.html"), encoding="utf-8").read()
qv = qv.replace("<title>Bindungs-Check</title>", "<title>Menschenrechte-Check – Quiz</title>")
qv = qv.replace("NAWI · 2AB · K1.2 Die Bindungsarten", I.EYEBROW)
qv = qv.replace("<h1>Bindungs-Check</h1>", "<h1>Menschenrechte-Check</h1>").replace("<h2>Bindungs-Check am Handy</h2>", "<h2>Menschenrechte-Check am Handy</h2>")
qv = qv.replace('alt="QR-Code zum Bindungs-Check"', 'alt="QR-Code zum Menschenrechte-Check"')
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

# ================================================================ Lernseite
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
 ("einstieg", "Einstieg", "Worum geht es?", [
   slide("Was meinst du?", tiles([("Mythos oder Fakt?", "»Wer zum Bundesheer einrückt, gibt seine Grundrechte am Kasernentor ab.« – Auflösung in Teil 1"),
                                  ("Alltag", "Mit 16 wählen, einen Verein gründen, den Beruf frei wählen – wer garantiert dir das eigentlich?"),
                                  ("Star Trek", "Captain Picard wird gefoltert und soll fünf Lichter sehen, wo vier sind. Was bringt Folter wirklich?"),
                                  ("Paris, 1948", "10. Dezember, 3 Uhr nachts: Eleanor Roosevelt verkündet die Allgemeine Erklärung der Menschenrechte.")])),
   slide("Das kannst du nach dieser Einheit", ol(I.LERNZIELE))]),
 ("teil1", "Teil 1 · Stunde 1 · Buch S. 46–50", "Grund- und Menschenrechte", [
   slide("Grundrecht oder Menschenrecht?", tiles([("Wahlrecht", "**Grundrecht** – nur für österreichische Staatsbürger"),
                                                  ("Folterverbot", "**Menschenrecht** – gilt für jeden, auch für Kriegsgefangene")])
         + merke("**Merksatz:** Menschenrechte hat man, weil man Mensch ist – angeboren, unveräußerlich, nicht verdienbar. Viele Grundrechte sind zugleich Menschenrechte."), "Buch S. 46–47"),
   slide("Drei Arten von Grundrechten", tiles([("Liberal – Schutz VOR dem Staat", "Meinungs- und Pressefreiheit, Privatsphäre, Eigentum, Vereinsfreiheit"),
                                               ("Demokratisch – Mitbestimmung IM Staat", "aktives und passives Wahlrecht, Gleichheit vor dem Gesetz"),
                                               ("Sozial – Leistung DURCH den Staat", "soziale Sicherung, medizinische Versorgung, Altersvorsorge")])
         + hint("**Achtung:** Soziale Grundrechte stehen nicht in der österreichischen Verfassung."), "Buch S. 46"),
   slide("Wo verankert – wie geschützt?", tiles([("1867 · Staatsgrundgesetz", "Kern der österreichischen Grundrechte"),
                                                 ("1950 · EMRK", "Europäische Menschenrechtskonvention des Europarats – in Österreich seit 1958, Verfassungsrang 1964"),
                                                 ("2009 · EU-Grundrechtecharta", "gilt nur, wenn EU-Recht angewendet wird")])
         + tiles([("Bei Verletzung: Beschwerde", "beim **Verfassungsgerichtshof** in Wien – danach beim **Europäischen Gerichtshof für Menschenrechte (EGMR)** in Straßburg")]), "Buch S. 47, 50"),
   slide("Drei Generationen von Menschenrechten", tiles([("1. Freiheit", "bürgerliche und politische Rechte"), ("2. Gleichheit", "wirtschaftliche, soziale, kulturelle Rechte"),
                                                         ("3. Solidarität", "Frieden, Entwicklung, saubere Umwelt")])
         + merke("**Aktuell:** 2022 erkennt die UNO das Recht auf eine saubere, gesunde Umwelt an. 2024 gibt der EGMR den Schweizer »KlimaSeniorinnen« recht: Zu wenig Klimaschutz verletzt die EMRK."), "Buch S. 47–48", "generationen"),
   slide("Ein langer Weg – auch in Österreich", table([["Jahr", "Was geschah?"], ["1867", "Staatsgrundgesetz (Dezemberverfassung)"], ["1945", "Grundrechte von 1867 wieder in Kraft"],
                                                       ["1948", "AEMR der UNO – nicht verbindlich"], ["1964", "EMRK im Verfassungsrang"], ["1968", "Todesstrafe in Österreich ganz abgeschafft"]]), "Buch S. 50"),
   slide("Grundrechte und Bundesheer – aktuell", tiles([("Wehrpflicht", "Jeder männliche Staatsbürger ist wehrpflichtig (Art. 9a B-VG)."),
                                                        ("Gewissensfreiheit", "Wer aus Gewissensgründen keine Waffe tragen will, leistet Zivildienst."),
                                                        ("Reform 2027 (Entwurf)", "Vorgestellt am 7.10.2026: Grundwehrdienst 6 Monate + 3 Monate Übungen, Zivildienst 9 Monate.")])
         + merke("**Auflösung Mythos:** Soldaten behalten ihre Grundrechte. Einschränkungen – etwa durch Befehle oder Dienstzeiten – braucht es per Gesetz, und sie müssen verhältnismäßig sein."), "Buch S. 46–47", "bundesheer"),
   slide("Stopp – kannst du das?", reveal("Gilt das Folterverbot auch für einen Asylwerber ohne österreichischen Pass?", "Ja – das Folterverbot ist ein Menschenrecht und gilt für jeden Menschen (Art. 3 EMRK).")
         + reveal("Wohin wendest du dich, wenn der Staat deine Grundrechte verletzt?", "An den Verfassungsgerichtshof in Wien – danach an den EGMR in Straßburg."), "Teil 1"),
   jetzt("Jetzt: Aufgaben 1–3", "aufgaben.html#card_a1")]),
 ("teil2", "Teil 2 · Stunde 2 · Buch S. 51–58", "Verstöße gegen Menschenrechte – aktuell", [
   slide("Todesstrafe 2025: ein Rekordjahr", stat("2.707", "Hinrichtungen 2025 – höchster Wert seit 1981") + stat("2.159+", "im Iran – mehr als doppelt so viele wie 2024")
         + stat("356+", "in Saudi-Arabien – Gastgeber der Fußball-WM 2034") + hint("China: vermutlich Tausende – die Zahlen sind Staatsgeheimnis. Quelle: Amnesty International, Mai 2026"), "Buch S. 57", "todesstrafe"),
   slide("Todesstrafe weltweit", ul(["Österreich: seit **1968** ganz abgeschafft", "**113 Staaten** haben sie für alle Verbrechen abgeschafft", "46 % der Hinrichtungen 2025 wegen Drogendelikten",
                                    "USA: **47** Hinrichtungen – einziges Land Amerikas"])
         + merke("**Quellenkritik:** Die Karte im Buch zeigt den Stand 2022. Solche Zahlen ändern sich jedes Jahr – immer das Datum prüfen!"), "Buch S. 57–58"),
   slide("Länderfall Iran: Protest wird bestraft", ul(["Seit 28.12.2025 landesweite Proteste – Sicherheitskräfte schießen mit scharfer Munition.",
                                                      "Hunderte willkürlich festgenommen, auch Jugendliche ab 14 (Human Rights Watch, 9.1.2026).",
                                                      "2025: mindestens 2.159 Hinrichtungen, 998 davon wegen Drogendelikten.",
                                                      "Iran veröffentlicht kaum Zahlen – NGOs zählen aus Berichten: Das sind Mindestwerte."])
         + reveal("Welche Menschenrechte werden hier verletzt?", "Recht auf Leben (Art. 3 AEMR) · Verbot von Folter (Art. 5) · Schutz vor willkürlicher Haft (Art. 9) · Meinungs- und Versammlungsfreiheit (Art. 19, 20) · Kinderrechte"), "Buch S. 51, 57"),
   slide("Pressefreiheit: Österreich holt auf", tiles([("Buch (ORF 2022)", "Platz 31"), ("Rangliste 2026", "**Platz 19**")])
         + ul(["Platz 1 Norwegen – Schlusslicht Eritrea", "weltweiter Schnitt so tief wie nie in 25 Jahren", "USA fallen auf Platz 64"])
         + merke("Freie Medien decken Missstände auf – ein Teil der geistigen Landesverteidigung."), "Buch S. 52"),
   slide("Verschleppte Kinder aus der Ukraine", ul(["über 20.000 Kinder seit 2014 nach Russland gebracht – Angabe Kiews, nicht unabhängig geprüft",
                                                   "rund 2.100 Kinder zurückgeholt (Hilfsorganisation Save Ukraine, Mai 2026)",
                                                   "2023: Der Internationale Strafgerichtshof erlässt Haftbefehle gegen Putin und Lwowa-Belowa.",
                                                   "Mai 2026: EU-Sanktionen gegen 16 Personen und 7 Organisationen"])
         + merke("**Kriegsvölkerrecht:** Die Genfer Abkommen verbieten, Zivilisten zu deportieren."), "Buch S. 56", "kinder"),
   slide("Wer setzt Menschenrechte durch?", tiles([("Kein Weltpolizist", "Völkerrecht hat oft keine Strafen."),
                                                   ("»Weiche Macht«", "NGOs wie Amnesty und Reporter ohne Grenzen stellen Verstöße öffentlich an den Pranger."),
                                                   ("Druck durch Staaten", "Sanktionen, z. B. der EU"), ("Gerichte", "EGMR in Straßburg, Internationaler Strafgerichtshof in Den Haag")]), "Buch S. 51"),
   slide("Stopp – kannst du das?", reveal("Warum sind Zahlen zu Hinrichtungen immer Mindestwerte?", "Viele Staaten veröffentlichen keine Zahlen (China: Staatsgeheimnis) – NGOs zählen nur, was bekannt wird.")
         + reveal("Nenne zwei Wege, wie Menschenrechte durchgesetzt werden.", "Gerichte (EGMR, Strafgerichtshof), Sanktionen von Staaten, öffentlicher Druck durch NGOs und Medien."), "Teil 2"),
   jetzt("Jetzt: Aufgaben 4–5 und das Quiz", "aufgaben.html#card_a4")]),
 ("teil3", "Teil 3 · Stunde 3 · Arbeitsblatt M1–M4", "70 Jahre AEMR", [
   slide("Dein Material", tiles([("Arbeitsblatt auf Papier oder in LMS", "»70 Jahre Allgemeine Erklärung der Menschenrechte« (Schroedel aktuell, 2018)"),
                                 ("Was steht wo?", ["**M1** Zeitleiste: ein langer Weg", "**M2** Die AEMR – ein Meilenstein", "**M3** Die weiche Macht", "**M4** Kommentar: Stolz und Schande"])])
         + hint("Lies M1–M4 zuerst **ohne Handy** und markiere Wichtiges. Zu jedem M gibt es eine Aufgabe: M1 → 6, M2 → 7, M3 → 8, M4 → 9."), "Buch S. 47–52"),
   slide("Die AEMR in Kürze", ul(["verkündet am **10. Dezember 1948** in Paris von der UNO-Generalversammlung – 30 Artikel",
                                  "Art. 1: »Alle Menschen sind frei und gleich an Würde und Rechten geboren.«",
                                  "eine **Erklärung, kein Vertrag** – verbindlich wurden erst die EMRK (1950) und die UN-Pakte (1966)",
                                  "Österreich war 1948 noch besetzt und ist erst seit **1955** bei der UNO."]), "Buch S. 47"),
   jetzt("Jetzt: Aufgaben 6–11", "aufgaben.html#card_a6")]),
 ("teil4", "Teil 4 · Stunde 4", "Stolz und Schande – 2026", [
   slide("Stolz oder Schande – 2026?", tiles([("Stolz", ["Friedensnobelpreis 2026 für die Juristin Navi Pillay (9.10.2026)", "113 Staaten ohne Todesstrafe", "Pressefreiheit: Österreich Platz 19 (vorher 22)"]),
                                              ("Schande", ["2.707 Hinrichtungen 2025 – Höchstwert seit 1981", "Iran: mindestens 2.159", "Pressefreiheit: USA fallen auf Platz 64"])])
         + hint("M4 ist von 2018. Was hat sich geändert – und was überwiegt für dich? Quellen: Amnesty 5/2026, Reporter ohne Grenzen 4/2026"), "Aufgabe 12"),
   slide("Preise für Menschenrechte", tiles([("Friedensnobelpreis", "Navi Pillay (Südafrika): Richterin am Ruanda-Tribunal und am Internationalen Strafgerichtshof, UN-Hochkommissarin für Menschenrechte – Verleihung am 10.12. in Oslo"),
                                             ("Sacharow-Preis", "Preis des EU-Parlaments – Entscheidung am 22.10., Verleihung am 16.12. in Straßburg"),
                                             ("10. Dezember", "Tag der Menschenrechte – die AEMR wird 78.")])),
   slide("Menschenrechte im Einsatz", tiles([("Wehrpflicht", "ist keine Zwangsarbeit – Art. 4 EMRK nimmt Militär- und Zivildienst ausdrücklich aus."),
                                             ("Befehl und Gewissen", "Befehle, die gegen Strafgesetze verstoßen, dürfen nicht befolgt werden."),
                                             ("Genfer Abkommen", "schützen im Krieg Zivilisten, Verwundete und Gefangene."),
                                             ("Seit 1960", "ist das Bundesheer in UNO-Einsätzen (Kongo) – heute z. B. bei KFOR im Kosovo.")]), "Buch S. 46"),
   slide("Häufige Fragen – kurz beantwortet", reveal("Ist Asyl ein Menschenrecht?", "Ja – das Recht, Asyl zu **suchen** (Art. 14 AEMR). Ob man es bekommt, prüft der Staat nach der Genfer Flüchtlingskonvention.")
         + reveal("Gilt das Folterverbot auch für Terroristen?", "Ja – für jeden Menschen, ohne Ausnahme, auch im Krieg (Art. 5 AEMR, Art. 3 EMRK).")
         + reveal("Ist das Internet ein Menschenrecht?", "Kein eigenes Recht – aber die UNO sagt: Rechte, die offline gelten, gelten auch online (z. B. Meinungsfreiheit).")),
   jetzt("Jetzt: Aufgabe 12", "aufgaben.html#card_a12")]),
 ("begriffe", "Zum Nachschlagen", "Fachbegriffe", [slide("Fachbegriffe", table(I.FACHBEGRIFFE))]),
]
CHECK = "".join(f'<div class="ziel"><p>{md(z)}</p><div class="chips" role="group" aria-label="Selbstcheck">' + "".join(f'<button type="button" class="chip" data-z="{k}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht")) + "</div></div>" for k, z in enumerate(I.LERNZIELE))
PARTS.append(("kurz", "Zum Schluss", "Kurz & knapp", [slide("Das Wichtigste in 5 Sätzen", ol(I.WICHTIGSTE)),
                                                       slide("Kann ich das?", hint("Tippe ehrlich an – bei »noch nicht« den passenden Teil noch einmal lesen.") + CHECK)]))
PARTS.append(("schnelle", "Optional", "Für Schnelle und Neugierige", [
   slide("Wo beginnen Menschenrechte?", merke("»An den kleinen Plätzen, nahe dem eigenen Heim … Solange diese Rechte dort keine Geltung haben, sind sie auch woanders nicht von Bedeutung.« – Eleanor Roosevelt")
         + hint("Aufgabe 13: Welche »kleinen Plätze« gibt es in deinem Leben?"), "OPTIONAL"),
   slide("Die Genfer Abkommen", ul(["1949 beschlossen, fast alle Staaten der Welt sind dabei", "schützen Verwundete, Kranke, Schiffbrüchige, Kriegsgefangene und Zivilisten",
                                    "das Rote Kreuz darf helfen und Gefangene besuchen"]) + hint("Aufgabe 15: Recherche – roteskreuz.at"), "OPTIONAL"),
   jetzt("Jetzt: Aufgaben 13–16", "aufgaben.html#card_a13")]))

TOCLAB = {"einstieg": "Einstieg", "teil1": "Teil 1", "teil2": "Teil 2", "teil3": "Teil 3", "teil4": "Teil 4", "begriffe": "Begriffe", "kurz": "Kurz & knapp", "schnelle": "Für Schnelle"}
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
<title>Menschenrechte – Lernseite</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,700&display=swap">
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
  <div class="btns"><a class="btn" href="aufgaben.html">2 · Arbeitsblatt A1–A{len(I.T)}</a><a class="btn alt" href="quiz.html">3 · Menschenrechte-Check (Quiz)</a></div>
  <p class="hint">Theorie zum Nachlesen im Schulbuch PBGW 2 (Trauner) S. 46–58. Material Stunde 3: Arbeitsblatt »70 Jahre AEMR« (Schroedel aktuell, 2018) auf Papier oder in LMS. Zahlen: Amnesty International (Mai 2026), Reporter ohne Grenzen (April 2026).</p>
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

# alte Adresse k1-aemr → Weiterleitung
old = os.path.join(ROOT, "2ak-pbgw/k1-aemr")
os.makedirs(old, exist_ok=True)
open(os.path.join(old, "aufgaben.html"), "w", encoding="utf-8").write(
    '<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
    '<meta http-equiv="refresh" content="0; url=../k1-grundrechte/aufgaben.html"><title>Weiterleitung</title></head>'
    '<body><p><a href="../k1-grundrechte/aufgaben.html">Zum Arbeitsblatt K1 Grund- und Menschenrechte</a></p></body></html>\n')
for f in ["theorie.html", "aufgaben.html", "quiz.html"]:
    print(f, os.path.getsize(DST + f) // 1024, "KB")
