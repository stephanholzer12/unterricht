"""PBGW 3BK · Meilensteine, Hochkulturen, frühe Staaten, Athen und Rom – 3 Stunden (v3).
Trauner PBGW 3: Kap. »Meilensteine der Entwicklungsgeschichte: Ur- und Frühgeschichte – Hochkulturen« (S. 23–44) = Buchkapitel K2.1–2.3 (3.1–3.5),
# Seitenangaben immer nur nach dem Trauner-Schulbuch (Projekt-Einstellung Stephan).
Jahresplan v14: E3, E4, E5 (je 2 Std. = 6 Std. brutto), K01, K02, K04, K05, K06, K08, N01, N02, P3, P4, SDG 2. Stephan: 3 Termine (Mo 16.11., 23.11., 30.11.2026),
am 23.11. 20 min Test (Stoff kommt von Stephan) + 4 min Organisation. Annahme 50 min je Stunde.
Grundlage: ChatGPT-Auftrag »26-27-3BK-Meilenst-ChatGPT-v2.md« (29.10.2026): Ablauf, Texte T1–T6, Aufgaben A1–A8, Quizpool – von Claude nach dem Regelwerk
(14. Fassung, 29.10.2026) umgesetzt und gegengeprüft. Trauner S. 109–115 am 01.11.2026 anhand von Buchfotos abgeglichen; S. 105–108 und 116–118 liegen nicht vor.
Eine Quelle für Handy-Seiten, Word, PPPs und Lösungsmappe.
Auswahlfelder: richtige Antwort an 1. Stelle (Anzeige gemischt), außer das 4. Element eines Feldes ist False (feste Reihenfolge)."""

STAND = "23.11.2026"
V = "v6"                       # v1/v2 = ChatGPT-Auftrag und -Paket; v3 = erste Umsetzung durch Claude
ORDNER = "3bk-pbgw/k2-5-meilensteine"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
KLASSE_URL = BASE + "3bk-pbgw/"
EYEBROW = "PBGW · 3BK · Meilensteine, Hochkulturen und antike Vorbilder"
TITEL = "Vom Vorrat zum Staat – Hochkulturen, Athen und Rom"
KURZTITEL = "Meilensteine: Vom Vorrat zum Staat – Hochkulturen, Athen, Rom"
BUCH = "Buch S. 23–44 und S. 105–118"
KEY = "26-27-3BK-K2.1-5.4-Meilenst-TH-Handy-v1"
CHECK_KEY = "26-27-3BK-K2.1-5.4-Meilenst-Lernseite-Check-v1"
PRAEFIX = "26-27-3BK-K2.1-5.4-Meilenst"
KAP = "K2.1–5.4"
TEST = "Mo 23.11.2026"
LEITFRAGE = "Wie organisieren Menschen Versorgung, Macht und Mitbestimmung, wenn Gemeinschaften größer werden?"

# Medien: (Titel, Quelle, Dauer, Link[, "sim"|"audio"]). Nur geprüfte Links sind freigegeben.
VIDEOS = {
    "oetzi": ("Südtiroler Archäologiemuseum: Kupfer von Ötzis Beil (Pressemeldung 1.3.2024, PDF)", "Südtiroler Archäologiemuseum / Universität Padua", "Lesen, ca. 3 min",
              "https://www.iceman.it/wp-content/uploads/2024/03/20240301_Pressemeldung_Archaometallurgieprojekt.pdf", "link"),
}
FREIGEGEBEN = {"oetzi"}


def zeigen(key, lehrer=False):
    return key in FREIGEGEBEN


KLASSEN = ["3BK"]
_D = {1: "Mo 16.11.", 2: "Mo 23.11.", 3: "Mo 30.11."}
DATEN = {k: dict(_D) for k in KLASSEN}
TEIL_STUNDE = {t: {k: t for k in KLASSEN} for t in (1, 2, 3)}
TEILNAME = {1: "Teil 1 · Vom Vorrat zum frühen Staat", 2: "Teil 2 · Hammurabis Rechtssammlung", 3: "Teil 3 · Athen und Rom"}
TEILBUCH = {1: "Buch S. 25–39", 2: "Buch S. 39–40", 3: "Buch S. 105–118"}

# Stundentitel: kreativ, mit Fachteil nach dem Doppelpunkt (Standard 15.11.2026)
STUNDENTITEL = {1: "Vom Korn zur Macht: Wie aus Dörfern Staaten wurden",
                2: "Auge um Auge – aber nicht für alle: Hammurabis Recht",
                3: "Losen und wählen: Athen, Rom und der Erste unter Gleichen"}


def wann(teil=None):
    if teil: return f"3BK: {_D[teil]}"
    return "3BK: " + " · ".join(_D[t] for t in (1, 2, 3))


# ======================================================================= Aufgaben
# Offene Erklärungen »man« (Lehrkraft bewertet), Stichwörter nur als Schreibhilfe. Auswahlfelder und eindeutige Zuordnungen prüft die Seite selbst.
ZB = ["10.000–8000 v. Chr.", "4000–3000 v. Chr.", "2000–1500 v. Chr.", "600–400 v. Chr.", "100 v. Chr.–100 n. Chr.", "400–500 n. Chr."]
SEL3 = ["Mesopotamischer Stadtstaat", "Ägyptisches Flächenkönigtum", "beide"]
FOLGE = ["Das Auge des Täters wird zerstört", "Eine Mine Silber wird gezahlt", "Die Hälfte des Kaufpreises wird gezahlt"]
LOS = ["Los", "Wahl"]

T = [
 # ======================================================= Teil 1 · Stunde 1
 {"id": "a1", "nr": 1, "title": "Ötzi: Was zeigt uns ein Gegenstand?", "src": "Buch S. 30", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 4,
  "q": "Ötzis Kupferbeil seht ihr am Beamer. Was steht fest, was ist nur vermutet – und was sagt das Beil nicht?",
  "hint": "Mündlich im Einstieg, am Mini-Whiteboard. Du kannst deine Stichworte danach hier eintragen. Info: Theorieteil »Metall, Können und Austausch«",
  "type": "multi",
  "fields": [["befund", "a) Befund: Das lässt sich am Beil feststellen"], ["vermutung", "b) Begründete Vermutung zum Zusammenleben"], ["grenze", "c) Das belegt das Beil allein nicht"]],
  "opt": ["befund", "vermutung", "grenze"],
  "chk": {"befund": {"kw": [["Material oder Form", r"kupfer|metall|klinge|beil|axt|material|schaft|holz|geschäftet"]], "man": True},
          "vermutung": {"kw": [["Rohstoff, Können oder Austausch", r"austausch|handel|rohstoff|können|koennen|fachwissen|spezial|herstell|werkstatt|bearbeit|brennstoff|wissen"]], "man": True},
          "grenze": {"kw": [["Beruf, Rang oder Reise", r"beruf|rang|anführer|anfuehrer|häuptling|haeuptling|reise|herkunft|jäger|jaeger|status|chef|beweis|nicht belegt|wissen wir nicht"]], "man": True}},
  "sol": [["Musterlösung", ["a) Es ist eine Klinge aus Kupfer, die in einen Holzschaft gesetzt wurde; das Material wurde gewonnen und bearbeitet.",
                          "b) Wer Kupfer verarbeitet, braucht Rohstoffe, Brennstoff und Können. Wenn der Rohstoff vor Ort fehlt, muss er durch Austausch beschafft werden – das spricht für Spezialisten und Verbindungen über Entfernungen. "
                          "Die Materialanalyse (Bleiisotope) lässt das Kupfer aus der südlichen Toskana stammen.",
                          "c) Das Beil allein belegt weder einen bestimmten Beruf noch eine Führungsrolle Ötzis noch eine Reise Ötzis selbst. Dafür bräuchte man zusätzliche Belege."]]],
  "fsol": {"befund": "Kupferklinge im Holzschaft, bearbeitet", "vermutung": "Rohstoff, Brennstoff, Können nötig – Austausch möglich", "grenze": "Beruf, Rang oder Reise Ötzis"},
  "tip": ["Metall, Können und Austausch", "theorie.html#metall"], "besprechen": True},

 {"id": "a2", "nr": 2, "title": "Landwirtschaft: Was hängt womit zusammen?", "src": "Buch S. 25–28", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 7,
  "q": "Landwirtschaft, Vorrat, Spezialisierung, Verteilung: Was hängt womit zusammen? Arbeitet zu zweit und schreibt in »kann …, weil …«.",
  "hint": "Info: Theorieteil »Vom Sammeln zum Vorrat« und »Neue Möglichkeiten, neue Probleme«",
  "type": "multi",
  "fields": [["z1", "a) Zusammenhang 1 (kann …, weil …)"], ["z2", "a) Zusammenhang 2 (kann …, weil …)"], ["z3", "a) Zusammenhang 3 (kann …, weil …)"],
             ["problem", "b) Ein neues Problem"], ["staat", "c) Warum nicht zwangsläufig ein Staat? (1–2 Sätze)"]],
  "chk": {"z1": {"kw": [["kann …, weil …", r"kann.*weil|weil"]], "man": True}, "z2": {"kw": [["kann …, weil …", r"kann.*weil|weil"]], "man": True},
          "z3": {"kw": [["kann …, weil …", r"kann.*weil|weil"]], "man": True},
          "problem": {"kw": [["Missernte, Krankheit oder Streit", r"missernte|krankheit|streit|ungleich|konflikt|schädling|schaedling|hunger|abhängig|abhaengig|diebstahl|schutz|lager|verteil"]], "man": True},
          "staat": {"kw": [["weitere Bedingungen", r"handel|konflikt|religi|bedingung|boden|klima|örtlich|oertlich|macht|nicht automatisch|nicht zwangsl|verschieden|andere|zusätzlich|zusaetzlich"]], "man": True}},
  "sol": [["Musterlösung", ["a) Landwirtschaft kann Vorräte ermöglichen, weil ein Teil der Ernte gelagert werden kann. Vorräte können Spezialisierung unterstützen, weil nicht mehr jeder ständig Nahrung beschaffen muss. "
                          "Die Kontrolle der Verteilung kann Einfluss verschaffen, weil andere von der Zuteilung abhängig sind. (Andere schlüssige Zusammenhänge, auch Rückwirkungen, zählen.)",
                          "b) z. B. Missernte, die viele gleichzeitig trifft · Schädlinge in den Vorräten · Krankheiten durch enges Zusammenleben · Streit um Land und Ernte · ungleicher Zugang zu Nahrung.",
                          "c) Wie eine Gemeinschaft diese Aufgaben löst, hängt auch von den örtlichen Bedingungen, von Handel, Konflikten, Religion und Machtverhältnissen ab. Ein Staat ist eine mögliche Antwort, kein Automatismus."],
                         ]],
  "fsol": {"z1": "kann Vorräte ermöglichen, weil …", "z2": "kann Spezialisierung unterstützen, weil …", "z3": "kann Einfluss verschaffen, weil …", "problem": "Missernte · Krankheiten · Streit · Ungleichheit",
           "staat": "Handel, Konflikte, Religion und örtliche Bedingungen wirken mit – kein Automatismus"},
  "kriterien": ["drei begründete Zusammenhänge mit »weil«", "ein neues Problem genannt", "keine Einbahnstraße: weitere Bedingungen genannt"],
  "tip": ["Neue Möglichkeiten, neue Probleme", "theorie.html#probleme"], "besprechen": True},

 {"id": "a3", "nr": 3, "title": "Zwei frühe Organisationsformen", "src": "Buch S. 33–39", "own": True, "tag": "Stunde 1", "h": 1, "zeit": 7,
  "q": "Zwei Wege, ein Gemeinwesen zu organisieren: die Stadt Uruk und das Königtum am Nil. Ordnet zu zweit zu und vergleicht.",
  "hint": "Auf Karte und Zeichnung findest du Nil, Euphrat und Tigris. Info: Theorieteil »Frühe Staaten: Stadtstaat und Flächenkönigtum«",
  "type": "multi",
  "fields": [["s1", "a) Eine Stadt mit ihrem Umland bildet einen eigenen Staat.", SEL3, False],
             ["s2", "Ein Königtum umfasst ein langes Flusstal mit vielen Siedlungen.", SEL3, False],
             ["s3", "Mehrere eigenständige Zentren stehen im Austausch, in Konkurrenz und im Krieg.", SEL3, False],
             ["s4", "Ein König steht an der Spitze einer hierarchischen Verwaltung für einen großen Raum.", SEL3, False],
             ["s5", "Abgaben, Arbeit und Vorräte müssen organisiert werden.", SEL3, False],
             ["s6", "Aufzeichnungen helfen, Mengen und Güter zu verwalten.", SEL3, False],
             ["s7", "Religiöse Vorstellungen helfen, Herrschaft zu begründen.", SEL3, False],
             ["s8", "Bewässerung und Schutz vor Wasserschäden verlangen Zusammenarbeit.", SEL3, False],
             ["gemeinsam", "b) Eine gemeinsame Organisationsaufgabe"], ["unterschied", "c) Ein Unterschied der politischen Ordnung"],
             ["fluss", "d) Warum erklärt ein großer Fluss allein keinen Staat? (1–2 Sätze)"]],
  "chk": {"s1": {"sel": SEL3[0]}, "s2": {"sel": SEL3[1]}, "s3": {"sel": SEL3[0]}, "s4": {"sel": SEL3[1]}, "s5": {"sel": SEL3[2]}, "s6": {"sel": SEL3[2]}, "s7": {"sel": SEL3[2]}, "s8": {"sel": SEL3[2]},
          "gemeinsam": {"kw": [["Versorgung, Abgaben, Verwaltung oder Wasser", r"versorg|vorrat|abgabe|verwalt|wasser|bewässer|bewaesser|aufzeichn|schrift|ernte|lager|religi"]], "man": True},
          "unterschied": {"kw": [["Raum oder Machtverteilung", r"stadt|umland|fläche|flaeche|pharao|könig|koenig|mehrere|einzeln|zentral|größer|groesser|raum|selbstständig|selbststaendig|eigen"]], "man": True},
          "fluss": {"kw": [["weitere Faktoren", r"handel|konflikt|religi|macht|bedingung|boden|ressource|verteil|nicht allein|nicht automatisch|auch|außerdem|ausserdem|zusätzlich|zusaetzlich"]], "man": True}},
  "sol": [["Musterlösung", ["a) Stadtstaat: 1, 3 · Flächenkönigtum: 2, 4 · beide: 5, 6, 7, 8",
                          "b) Versorgung und Verwaltung: Abgaben, Arbeit und Vorräte organisieren (mit Aufzeichnungen) und für das Wasser zusammenarbeiten.",
                          "c) Mesopotamien: Stadt mit Umland, mehrere zunächst eigenständige Zentren. Ägypten: ein Königtum mit Verwaltung über einen größeren, zusammenhängenden Raum am Nil.",
                          "d) Wasserwirtschaft verlangt Organisation, aber verschiedene Formen der Zusammenarbeit sind denkbar. Ob Macht entsteht, hängt auch von Handel, Konflikten, Religion, Ressourcen und örtlichen Bedingungen ab.",
                          "Sicherungssatz: Beide Gesellschaften organisierten Versorgung und Herrschaft. Die räumliche Ausdehnung und die Verteilung politischer Macht unterschieden sich."]]],
  "fsol": {"gemeinsam": "Abgaben, Arbeit und Vorräte organisieren (mit Aufzeichnungen)", "unterschied": "Stadt mit Umland ↔ Königtum über das ganze Nil-Tal", "fluss": "auch Handel, Konflikte, Religion, Ressourcen"},
  "fsol_rest": ["Sicherungssatz: Beide organisierten Versorgung und Herrschaft; Ausdehnung und Machtverteilung unterschieden sich."],
  "tab": [["Kriterium", "Stadtstaat Mesopotamien", "Flächenkönigtum Ägypten"], ["Raum und Flüsse", "Stadt mit Umland, Euphrat und Tigris", "viele Siedlungen am Nil"],
          ["Politische Organisation", "mehrere zunächst eigenständige Städte", "Königtum über einen größeren Raum"], ["Versorgung und Aufzeichnung", "Abgaben, Vorräte, Schrift", "Abgaben, Vorräte, Schrift"],
          ["Begründung von Herrschaft", "Religion, Kontrolle von Einrichtungen", "Religion, Verwaltung, Durchsetzung"]],
  "tabnote": "Die vier Kriterien (Raum · Organisation · Versorgung · Begründung) stecken in den Aussagen a).",
  "tip": ["Frühe Staaten: Stadtstaat und Flächenkönigtum", "theorie.html#staaten"], "besprechen": True},

 # ======================================================= Teil 2 · Stunde 2
 {"id": "a4", "nr": 4, "title": "Hammurabi: Ordnung, Verantwortung und Ungleichheit", "src": "Buch-Aufgabe S. 40", "own": False, "tag": "Stunde 2", "h": 2, "zeit": 9,
  "q": "Auf dem Blatt stehen fünf Paragrafen in einer Arbeitsfassung. Lest sie zu zweit und arbeitet heraus, was dieses Recht ordnet – und für wen es nicht gleich gilt.",
  "hint": "Neu formuliert nach der Buch-Aufgabe S. 40 (Nr. 1, 7, 10), auf fünf Paragrafen gekürzt (§ 53, 196, 198, 199, 233). Info: Theorieteil »Was die Regeln verraten« und »Recht ist nicht gleich Gleichheit«",
  "type": "multi",
  "fields": [["damm", "a) § 53 regelt das Problem …"],
             ["f196", "b) § 196: Opfer ist ein Bürgersohn", FOLGE, False], ["f198", "§ 198: Opfer ist ein Untergebener", FOLGE, False], ["f199", "§ 199: Opfer ist der Knecht (versklavte Mensch) eines Bürgers", FOLGE, False],
             ["entsch", "c) Das entscheidet über die Rechtsfolge", ["Der gesellschaftliche Stand des Opfers", "Die Schwere der Verletzung", "Das Geschlecht des Täters", "Der Ort der Tat"]],
             ["eigentum", "d) Beleg für den Schutz von Eigentum oder wirtschaftlichen Interessen"],
             ["gleich", "e) Schriftliches Recht ↔ Rechtsgleichheit (1–2 Sätze)"],
             ["zeigt", "f) Die Sammlung zeigt …"], ["offen", "…; ob …, können wir aus ihr allein nicht feststellen."]],
  "chk": {"damm": {"kw": [["Damm, Überschwemmung oder Getreide", r"damm|deich|feld|überschwemm|ueberschwemm|getreide|nachbar|verantwort|ersatz|instand|schaden"]], "man": True},
          "f196": {"sel": FOLGE[0]}, "f198": {"sel": FOLGE[1]}, "f199": {"sel": FOLGE[2]}, "entsch": {"sel": "Der gesellschaftliche Stand des Opfers"},
          "eigentum": {"kw": [["§ und Begründung", r"damm|getreide|§|wand|baumeister|kaufpreis|silber|ersatz|haft|eigentum|mine|feld"]], "man": True},
          "gleich": {"kw": [["Regel ≠ gleiche Rechte", r"nicht gleich|ungleich|unterschied|stand|status|rang|bürger|knecht|trotzdem|aber|obwohl|schriftlich|geschrieben"]], "man": True},
          "zeigt": {"kw": [["Aussage über Gesellschaft", r"ungleich|hierarch|status|stand|eigentum|ordnung|konflikt|haftung|könig|koenig|verantwort"]], "man": True},
          "offen": {"kw": [["Grenze der Quelle", r"anwend|alltag|tatsächlich|tatsaechlich|wirklich|jeder fall|gericht|entschied|praxis|befolgt|durchgesetzt"]], "man": True}},
  "sol": [["Musterlösung", ["a) Wer seinen Damm nicht instand hält und dadurch fremde Felder überschwemmt, muss das vernichtete Getreide ersetzen: Infrastruktur und Verantwortung gegenüber Nachbarn.",
                          "b) § 196: dem Täter wird ein Auge zerstört (Vergeltung) · § 198: eine Mine Silber · § 199: die Hälfte des Kaufpreises (der versklavte Mensch wird als Eigentum behandelt).",
                          "c) Der gesellschaftliche Stand des Opfers – bei gleicher Verletzung unterschiedliche Folgen.",
                          "d) z. B. § 53 (Getreide wird ersetzt) · § 233 (der Baumeister muss eine mangelhafte Wand auf eigene Kosten instand setzen) · § 199 (Zahlung an den Besitzer).",
                          "e) Eine schriftliche Regel macht Folgen berechenbar, sagt aber nichts darüber, ob alle gleich behandelt werden: Hier hängt die Rechtsfolge vom Stand ab.",
                          "f) Die Sammlung zeigt, welche Konflikte geordnet werden sollten und dass die Gesellschaft hierarchisch war; ob jeder Fall im Alltag genau so entschieden wurde, können wir aus ihr allein nicht feststellen.",
                          "Hinweis: »Auge um Auge« ist eine Form der Vergeltung; daneben stehen Ausgleichszahlungen. Die Sammlung ist eine Darstellung königlicher Ordnung, keine Gerichtsakte."]]],
  "fsol": {"damm": "Damm nicht instand → fremde Felder überschwemmt → Getreide ersetzen", "eigentum": "§ 53 oder § 233 (Haftung), § 199 (Zahlung an den Besitzer)",
           "gleich": "Schriftlich ≠ gleich: Folge hängt vom Stand ab", "zeigt": "… hierarchische Gesellschaft und geordnete Konflikte", "offen": "… jeder Fall im Alltag so entschieden wurde"},
  "kriterien": ["Gleiche Verletzung – ungleiche Folgen erkannt", "Eigentumsschutz mit Beleg", "Regel ≠ Gleichheit erklärt", "Grenze der Quelle genannt"],
  "tab": [["§", "Arbeitsfassung (vereinfacht)"], ["53", "Wer den Damm seines Feldes nicht instand hält und dadurch andere Felder überschwemmt, ersetzt das vernichtete Getreide."],
          ["196", "Wird einem Bürgersohn ein Auge zerstört, wird dem Täter ein Auge zerstört."], ["198", "Wird das Auge eines Untergebenen zerstört, ist eine Mine Silber zu zahlen."],
          ["199", "Wird das Auge des Knechtes eines Bürgers zerstört, ist die Hälfte seines Kaufpreises zu zahlen."],
          ["233", "Baut ein Baumeister eine Wand nicht fest genug und zeigt sie Schäden oder droht einzustürzen, muss er sie auf eigene Kosten instand setzen."]],
  "tabnote": "Sprachlich vereinfachte Arbeitsfassung nach Buch S. 40, kein wörtliches Zitat. Eine Mine ist eine Gewichts- und Recheneinheit für Silber.",
  "tip": ["Was die Regeln verraten", "theorie.html#regeln"], "besprechen": True},

 # ======================================================= Teil 3 · Stunde 3
 {"id": "a5", "nr": 5, "title": "Athen: Wer gehört zum entscheidenden Volk?", "src": "Buch S. 111 (Athen)", "own": False, "tag": "Stunde 3", "h": 3, "zeit": 7,
  "q": "Wer hat in Athen wirklich mitentschieden? Arbeitet zu zweit mit dem Schaubild und dem Theorie-Teil.",
  "hint": "Eigene Aufgabe zum Thema (Buch S. 109–111). Bilder von Athen sind meist spätere Darstellungen, keine Augenzeugenbilder. Info: Theorieteil »Athen: direkte Beteiligung mit Grenzen«",
  "type": "multi",
  "fields": [["einr", "a) Hier entscheiden Bürger unmittelbar", ["Volksversammlung", "Areopag", "Heer", "Rat der 500"]],
             ["rat", "b) Rat der 500", LOS, False], ["arch", "Archonten (hohe Beamte)", LOS, False], ["strat", "Strategen (Heerführer)", LOS, False],
             ["aus", "c) Drei Gruppen ohne politische Mitbestimmung"],
             ["at", "d) Österreich heute: Wer entscheidet, welche Kontrolle?"],
             ["urteil", "e) Dein Urteilssatz"]],
  "chk": {"einr": {"sel": "Volksversammlung"}, "rat": {"sel": "Los"}, "arch": {"sel": "Los"}, "strat": {"sel": "Wahl"},
          "aus": {"kw": [["Frauen", r"frau"], ["Versklavte", r"sklav|versklav|knecht"], ["Fremde (Metöken)", r"fremd|metök|metoek|ausländ|auslaend|zugezogen"]], "man": True},
          "at": {"kw": [["Parlament oder Wahlen", r"parlament|nationalrat|gewählt|gewaehlt|abgeordnete|wahl|vertreter|verfassung|gericht|kontroll"]], "man": True},
          "urteil": {"kw": [["Beteiligung und Grenze", r"bürger|buerger|beteilig|begrenzt|eingeschränkt|eingeschraenkt|ausgeschlossen|männer|maenner|weitreichend"]], "man": True}},
  "sol": [["Musterlösung", ["a) Volksversammlung (die berechtigten erwachsenen männlichen Bürger entscheiden selbst).",
                          "b) Rat der 500: Los · Archonten: Los · Strategen: Wahl (viele Ämter wurden gelost, die Heerführer gewählt).",
                          "c) Frauen, Versklavte, Fremde (Metöken).",
                          "d) In Österreich wählen die Wahlberechtigten Vertreter; diese wirken an der Gesetzgebung mit und kontrollieren die Regierung. Es gibt Rechtsbindung und Kontrolle. Auch heute haben nicht alle Einwohner automatisch alle Wahlrechte (z. B. Staatsbürgerschaft, Wahlalter).",
                          "e) Athen war für seine Bürger weitreichend partizipativ. Nach heutigen Maßstäben war die politische Gleichberechtigung stark begrenzt."]]],
  "fsol": {"aus": "Frauen · Versklavte · Fremde (Metöken)", "at": "gewählte Vertreter, Parlament kontrolliert, rechtliche Bindung",
           "urteil": "… weitreichend partizipativ … stark begrenzt"},
  "kriterien": ["unmittelbare Entscheidung erklärt", "Los und Wahl unterschieden", "drei ausgeschlossene Gruppen", "Vergleich nennt Vertretung und Kontrolle"],
  "tip": ["Athen: direkte Beteiligung mit Grenzen", "theorie.html#athen"], "besprechen": True},

 {"id": "a6", "nr": 6, "title": "Augustus: Aussage und Machtverteilung", "src": "Buch S. 114 (Caesar und Augustus)", "own": False, "tag": "Stunde 3", "h": 3, "zeit": 6,
  "q": "Augustus schreibt in seinem Tatenbericht: Er habe die Macht an Senat und Volk zurückgegeben, sein Vorrang beruhe nur auf seinem Ansehen. Prüft zu zweit, ob das zur wirklichen Machtverteilung passt.",
  "hint": "Arbeitsfassung des Tatenberichts (Res gestae), sprachlich vereinfacht. Info: Theorieteil »Rom: Republik und Machtkonzentration«",
  "type": "multi",
  "fields": [["name", "a) Augustus nannte sich selbst", ["Princeps – Erster unter Gleichen", "König", "Diktator auf Lebenszeit", "Gott"]],
             ["eindruck", "b) Diesen Eindruck will er erzeugen"], ["macht", "c) Machtmittel und Befugnisse bei Augustus"], ["quelle", "d) Nützlich, aber zu prüfen, weil …"]],
  "chk": {"name": {"sel": "Princeps – Erster unter Gleichen"},
          "eindruck": {"kw": [["Friedensstifter oder Wiederhersteller", r"frieden|wiederherst|republik|ordnung|bürgerkrieg|buergerkrieg|senat|volk|zurückgeg|zurueckgeg|bescheiden|rechtmäßig|rechtmaessig"]], "man": True},
          "macht": {"kw": [["Heer, Provinzen oder Ämter", r"heer|militär|militaer|oberbefehl|provinz|konsul|tribun|befugnis|senat|ehrenname|macht"]], "man": True},
          "quelle": {"kw": [["Selbstdarstellung", r"selbstdarstell|eigen|perspektive|sicht|bild|wollte|überprüf|ueberpruef|vergleich|andere quellen|nicht neutral|interesse"]], "man": True}},
  "sol": [["Musterlösung", ["a) Princeps (»Erster unter Gleichen«), nicht König.",
                          "b) Er stellt sich als Friedensstifter dar, der die Republik wiederhergestellt und die Macht zurückgegeben hat; sein Vorrang beruhe nur auf Ansehen.",
                          "c) Entscheidend sind seine militärische Macht (Oberbefehl über das Heer, Statthalterschaft in wichtigen Provinzen) und weitreichende Befugnisse: wichtige Amtsgewalten, die sonst auf mehrere Ämter verteilt waren (Konsul, Volkstribun). Der Ehrenname Augustus und der Titel Princeps stützten sein Ansehen, waren aber keine Amtsgewalt. Die republikanischen Einrichtungen bestanden weiter.",
                          "d) Der Tatenbericht ist nützlich, weil er zeigt, wie Augustus gesehen werden wollte. Er ist aber seine eigene Darstellung und keine unabhängige Gesamtbewertung; jede Behauptung muss man mit anderen Quellen und mit der tatsächlichen Machtverteilung vergleichen.",
                          "Schlusssatz: Augustus verwendet die Sprache der Republik, während die entscheidende Macht bei ihm liegt. (Nicht gleich »jede Aussage ist gelogen«: Jede Behauptung konkret prüfen.)"]]],
  "fsol": {"eindruck": "Friedensstifter, Wiederhersteller der Republik, nur Ansehen", "macht": "Heer, Provinzen, Konsul- und Tribunenbefugnisse (Ehrenname = Ansehen, keine Amtsgewalt)",
           "quelle": "Selbstdarstellung – mit anderen Quellen und der tatsächlichen Macht vergleichen"},
  "kriterien": ["Selbstbezeichnung Princeps", "gewünschter Eindruck", "mindestens zwei Machtmittel", "Quelle ist Selbstdarstellung"],
  "tip": ["Rom: Republik und Machtkonzentration", "theorie.html#rom"], "besprechen": True},

 {"id": "a7", "nr": 7, "title": "Vier Formen der Herrschaft vergleichen", "src": "Buch S. 36–38, 111–115", "own": True, "tag": "Stunde 3", "h": 3, "zeit": 5,
  "q": "Vier Ordnungen, eine Tabelle: Ägypten und die Spalte »Wo liegt die Macht?« sind schon ausgefüllt. Ergänzt den Rest und begründet zwei Ordnungen.",
  "hint": "Kein Ranking »primitiv – modern«. »Republik« allein sagt nicht, dass alle gleich mitentscheiden. Info: Theorieteile zu Ägypten, Athen und Rom",
  "type": "multi",
  "fields": [["ath_b", "a) Athen: Beteiligung und Ausschluss"], ["ath_k", "Athen: Kontrolle und Grenze"],
             ["rep_b", "Römische Republik: Beteiligung und Ausschluss"], ["rep_k", "Römische Republik: Kontrolle und Grenze"],
             ["pri_b", "Prinzipat des Augustus: Beteiligung und Ausschluss"], ["pri_k", "Prinzipat des Augustus: Kontrolle und Grenze"],
             ["wahl", "b) Zwei Ordnungen: Wie beeinflusst die Machtverteilung Beteiligung oder Kontrolle? (mit je einem Merkmal)"]],
  "chk": {"ath_b": {"kw": [["Bürger, Ausschluss", r"bürger|buerger|männer|maenner|volksversammlung|direkt|frauen|sklav|metök|metoek|fremde"]], "man": True},
          "ath_k": {"kw": [["Amtszeit, Los oder Rechenschaft", r"los|befrist|amtszeit|rechenschaft|scherben|ostrak|rat|begrenzt|bürger|buerger"]], "man": True},
          "rep_b": {"kw": [["Männer, unterschiedliches Gewicht", r"männer|maenner|bürger|buerger|senat|oberschicht|adel|vermögen|vermoegen|frauen|sklav|versammlung|gewicht|wahl"]], "man": True},
          "rep_k": {"kw": [["Befristung oder Einspruch", r"befrist|amtszeit|zwei konsul|konsuln|tribun|einspruch|veto|mehrere|senat|soziale macht|oberschicht"]], "man": True},
          "pri_b": {"kw": [["Einrichtungen bleiben, Mitbestimmung schwach", r"einrichtung|weiter|bleiben|senat|ämter|aemter|eingeschränkt|eingeschraenkt|schwach|kaum|nur noch|formal"]], "man": True},
          "pri_k": {"kw": [["begrenzte Kontrolle", r"kaum|schwach|begrenzt|nur|formal|beschränkt|beschraenkt|einrichtung|heer|princeps|augustus|eine person"]], "man": True},
          "wahl": {"kw": [["Machtverteilung und Merkmal", r"weil|dadurch|deshalb|macht|verteil|konzentr|beispiel|merkmal|los|konsul|heer|volksversammlung"]], "man": True}},
  "sol": [["Musterlösung", ["Athen: Beteiligung – direkte Beteiligung der männlichen Bürger in der Volksversammlung; Frauen, Versklavte und Fremde (Metöken) ausgeschlossen · Kontrolle – zeitlich begrenzte Ämter, Los, Rechenschaft; nur innerhalb eines begrenzten Bürgerkreises.",
                          "Römische Republik: Beteiligung – männliche Bürger mit unterschiedlichem politischem Gewicht; Oberschicht und Senat stark; Frauen und Versklavte ausgeschlossen · Kontrolle – Befristung, zwei Konsuln, Einspruch der Volkstribunen; soziale Macht begrenzt Gleichheit.",
                          "Prinzipat: Beteiligung – republikanische Einrichtungen bestehen weiter, wirksame Mitbestimmung ist eingeschränkt · Kontrolle – formale Einrichtungen begrenzen die persönliche Vorrangstellung nur schwach.",
                          "b) Beispiel: Athen – Weil die Volksversammlung entscheidet und viele Ämter gelost werden, ist die Beteiligung der Bürger groß; weil Frauen, Versklavte und Metöken fehlen, bleibt sie auf eine kleine Gruppe beschränkt. "
                          "Prinzipat – Weil Heer und wichtige Befugnisse bei einer Person liegen, bleiben Senat und Ämter formal bestehen, kontrollieren ihn aber kaum.",
                          "Nicht: »Rom war eine Republik, also entschieden alle gleichberechtigt.«"]]],
  "fsol": {"ath_b": "Bürger (Männer) direkt; Frauen, Versklavte, Metöken ausgeschlossen", "ath_k": "Ämter befristet, Los, Rechenschaft – nur im Bürgerkreis",
           "rep_b": "männliche Bürger, Oberschicht stark, Frauen und Versklavte ausgeschlossen", "rep_k": "Befristung, zwei Konsuln, Einspruch der Tribunen",
           "pri_b": "Einrichtungen bleiben, Mitbestimmung eingeschränkt", "pri_k": "formale Einrichtungen begrenzen den Princeps kaum",
           "wahl": "z. B. Athen: Volksversammlung + Los → große Beteiligung, aber nur Bürger"},
  "kriterien": ["Athen vollständig", "Republik: Oberschicht und Einspruch erkannt", "Prinzipat: Machtkonzentration erkannt", "Begründung mit konkreten Merkmalen"],
  "tab": [["Ordnung", "Wo liegt die entscheidende Macht?", "Beteiligung und Ausschluss", "Kontrolle und Grenze"],
          ["Ägyptisches Königtum", "König und hierarchische Verwaltung, religiös begründet", "breite Bevölkerung ohne Mitentscheidungsrecht", "keine moderne Machtkontrolle"],
          ["Klassisches Athen", "Volksversammlung der berechtigten Bürger, Rat und Ämter", "", ""],
          ["Römische Republik", "mehrere Ämter, Senat und Versammlungen, starker Einfluss der Oberschicht", "", ""],
          ["Prinzipat des Augustus", "entscheidende Befugnisse und militärische Macht beim Princeps", "", ""]],
  "tabnote": "Gelb auszufüllen: Spalten 3 und 4 für Athen, Republik und Prinzipat.",
  "tip": ["Athen und Rom im Vergleich", "theorie.html#vergleich"], "besprechen": True},

 {"id": "a8", "nr": 8, "title": "Gemeinsamer Zeitstrahl", "src": "Buch S. 24–40 und S. 105–118", "own": True, "tag": "Stunde 1 und 3", "h": 3, "zeit": 7,
  "q": "Neun Karten, sechs Zeitbereiche. Legt den Zeitstrahl, begründet zwei Karten und ergänzt eine eigene. Teil 1 in Stunde 1, Teil 2 in Stunde 3.",
  "hint": "Jahreszahlen sind Orientierung. Die Begründung zählt mehr als das Datum. Info: Zeittafel im Theorieteil (Zeitstrahl) und Buch S. 24",
  "type": "multi",
  "fields": [["k1", "a) 1 · Beginn landwirtschaftlicher Lebensweisen im Vorderen Orient", ZB, False], ["k2", "2 · Ötzis Kupferbeil", ZB, False], ["k3", "3 · Frühe Schrift in Mesopotamien", ZB, False],
             ["k4", "4 · Uruk wächst zu einer Stadt", ZB, False], ["k5", "5 · Hammurabis Rechtssammlung", ZB, False], ["k6", "6 · Klassische athenische Demokratie", ZB, False],
             ["k7", "7 · Beginn der römischen Republik (nach der Überlieferung)", ZB, False], ["k8", "8 · Beginn des Prinzipats des Augustus", ZB, False], ["k9", "9 · Ende Westroms als Epochenmarke", ZB, False],
             ["warum", "b) Begründung bei zwei Karten (Nummer und Grund)"], ["eigen", "c) Eigene Karte: gleichzeitig, aber nicht überall"],
             ["schluss", "d) Schlusssatz nach Teil 1 (1 Satz)"]],
  "chk": {"k1": {"sel": ZB[0]}, "k2": {"sel": ZB[1]}, "k3": {"sel": ZB[1]}, "k4": {"sel": ZB[1]}, "k5": {"sel": ZB[2]}, "k6": {"sel": ZB[3]}, "k7": {"sel": ZB[3]}, "k8": {"sel": ZB[4]}, "k9": {"sel": ZB[5]},
          "warum": {"kw": [["Karte und Grund", r"weil|da |denn|deshalb|\d"]], "man": True},
          "eigen": {"kw": [["Region und Zeit", r"region|gleichzeitig|noch|schon|während|waehrend|amerika|china|ägypten|aegypten|mitteleuropa|alpen|\d"]], "man": True},
          "schluss": {"kw": [["Organisation und Herrschaft", r"organis|herrschaft|verwalt|macht|vorrat|abgabe|staat|ordnung"]], "man": True}},
  "sol": [["Musterlösung", ["a) 1 → 10.000–8000 v. Chr. (langer, regional verschiedener Prozess) · 2 → 4000–3000 (um 3300 v. Chr., Kupferzeit im Alpenraum) · 3 → 4000–3000 (spätes 4. Jahrtausend, grobe Orientierung um 3300/3200) · "
                          "4 → 4000–3000 · 5 → 2000–1500 (um 1750 v. Chr.) · 6 → 600–400 (besonders 5. Jh. v. Chr.) · 7 → 600–400 (überliefert seit 509 v. Chr.) · 8 → 100 v. Chr.–100 n. Chr. (27 v. Chr.) · 9 → 400–500 n. Chr. (476).",
                          "b) z. B. Karte 2 und 3 liegen im selben Zeitbereich: Ötzi lebte in den Alpen, die frühe Schrift entstand in Mesopotamien – gleichzeitig, aber in verschiedenen Regionen.",
                          "c) z. B. Um 3300 v. Chr. kannte man in Mesopotamien schon Schrift, in den Alpen lebte Ötzi mit Kupferbeil und ohne Schrift. Oder: Eisen wurde in manchen Regionen schon früh genutzt, in anderen erst Jahrhunderte später.",
                          "d) Landwirtschaft, Metall, Schrift und Städte schufen Vorräte, Spezialisten und Aufzeichnungen – das verlangte Organisation und eröffnete Möglichkeiten für Herrschaft.",
                          "Hinweis: Nicht als Abfolge »Ötzi erfindet Metall, danach entsteht Schrift« darstellen."]]],
  "fsol": {"warum": "z. B. Karte 2 und 3: gleicher Zeitbereich, verschiedene Regionen", "eigen": "z. B. Schrift in Mesopotamien, Ötzi ohne Schrift in den Alpen", "schluss": "Vorräte, Städte, Schrift verlangten Organisation – und boten Herrschaft Chancen"},
  "kriterien": ["Karten richtig zugeordnet", "zwei Zuordnungen begründet", "eigene Karte zeigt Ungleichzeitigkeit", "Schlusssatz verbindet Organisation und Herrschaft"],
  "tip": ["Der gemeinsame Zeitstrahl", "theorie.html#zeitstrahl"], "besprechen": True},

 # ======================================================= Zusatz · Für Schnelle (freiwillig, keine Hausübung)
 {"id": "a9", "nr": 10, "title": "Eine eigene Lieferliste", "src": "Buch S. 34–35 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 10,
  "q": "Mit der Hand auf Papier: Erfinde Zeichen für vier Waren und schreib eine kurze Lieferliste damit. Blatt fotografieren.",
  "hint": "Kreativ, aber genau: Eine Liste ist erst brauchbar, wenn andere sie ohne Rückfrage lesen können. Info: Theorieteil »Schrift: Listen und Verwaltung«",
  "type": "sketch",
  "fields": [["raten", "a) Das musste mein Partner raten"], ["zahlen", "b) Darum braucht man Zahlzeichen"], ["heute", "c) Heute sieht eine Magazin-Liste anders aus, weil …"]],
  "chk": {"raten": {"kw": [["Zeichen oder Menge", r"zeichen|menge|zahl|ware|nicht klar|unklar|bedeutung|erraten|raten"]], "man": True},
          "zahlen": {"kw": [["Mengen und Abgaben", r"menge|abgabe|anzahl|zähl|zaehl|verwalt|kontroll|vorrat|liefer|wie viel"]], "man": True},
          "heute": {"kw": [["einheitlich oder digital", r"einheit|norm|standard|digital|computer|scanner|barcode|artikelnummer|einheitlich|datenbank|schrift|alphabet"]], "man": True}},
  "sol": [["Musterlösung", ["a) z. B. welches Zeichen für welche Ware steht und ob eine Zahl für Stück oder Krüge gilt – ohne gemeinsame Zeichenliste ist eine Liste kaum lesbar.",
                          "b) Ohne Zahlen weiß man nicht, wie viel geliefert wurde oder wie viel als Abgabe zu leisten ist; Kontrolle und Verteilung brauchen Mengen.",
                          "c) Heute gibt es einheitliche Bezeichnungen, Nummern und Datenbanken; jeder Gegenstand hat eine eindeutige Artikelnummer, und alle lesen dasselbe. (Andere sinnvolle Antworten zählen.)"]]],
  "fsol": {"raten": "Bedeutung der Zeichen, Mengen", "zahlen": "Mengen für Kontrolle und Abgaben", "heute": "einheitliche Bezeichnungen, Nummern, Datenbank"},
  "tip": ["Schrift: Listen und Verwaltung", "theorie.html#schrift"]},

 {"id": "a10", "nr": 11, "title": "Eine KI-Antwort prüfen", "src": "Buch S. 40, 64 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Eine KI hat auf »Erkläre Hammurabi und Athen« geantwortet: »Hammurabi erfand das Recht und schrieb als Erster Gesetze auf. Vor dem Gesetz waren alle Babylonier gleich. In Athen durften alle Einwohner über die Gesetze abstimmen, weil Athen die erste Demokratie der Welt war.« Prüft diese Antwort.",
  "hint": "Die KI hat dir keine fertige Lösung zu liefern – du prüfst sie. Info: Theorieteile zu Hammurabi und Athen",
  "type": "multi",
  "fields": [["fehler", "a) Drei Fehler und ihre Korrektur"], ["prompt", "b) Dein Prompt"], ["pruefen", "c) Das prüfe ich nach, und zwar hier"]],
  "chk": {"fehler": {"kw": [["älter oder nicht gleich oder nicht alle", r"älter|aelter|vorher|schon vor|nicht der erste|nicht erste|ungleich|nicht gleich|stand|status|nicht alle|bürger|buerger|männer|maenner|frauen|sklav"]], "man": True},
          "prompt": {"kw": [["Quellen und Unsicherheit", r"quelle|beleg|unsicher|belegt|wie sicher|welche quelle|nenne|gib an|unterschied|zeitraum"]], "man": True},
          "pruefen": {"kw": [["Prüfweg", r"buch|theorie|museum|lexikon|quelle|vergleich|seite|nachschlag|nachlesen|louvre|parlament|uni"]], "man": True}},
  "sol": [["Musterlösung", ["a) 1. Hammurabi war nicht der Erste: Es gibt ältere Rechtssammlungen (z. B. Ur-Nammu); seine Sammlung ist ein bedeutendes Zeugnis, kein »Erfinder des Rechts«. "
                          "2. Vor dem Gesetz waren nicht alle gleich: Die Rechtsfolgen hingen vom Stand ab (§ 196, 198, 199). "
                          "3. In Athen durften nur erwachsene männliche Bürger abstimmen – Frauen, Versklavte und Metöken nicht. (Auch »erste Demokratie der Welt« ist eine Behauptung, die man belegen müsste.)",
                          "b) z. B. »Erkläre Hammurabis Rechtssammlung und die attische Demokratie. Nenne zu jeder Aussage die Quelle und sage dazu, was in der Forschung unsicher oder umstritten ist.«",
                          "c) z. B. die Aussage über die Gleichheit: im Buch S. 40 (Paragrafen) und in einer Museumsseite nachlesen; die Athen-Aussage im Buch S. 109–111."]]],
  "fsol": {"fehler": "nicht der Erste · nicht alle gleich · nur männliche Bürger", "prompt": "… mit Quellen und Angabe, was unsicher ist", "pruefen": "z. B. Buch S. 40 und eine Museumsseite"},
  "tip": ["Recht ist nicht gleich Gleichheit", "theorie.html#regeln"]},

 {"id": "a11", "nr": 12, "title": "Woher kam das Kupfer?", "src": "Buch S. 30 · Zusatz", "own": True, "tag": "Zusatz", "h": 0, "zeit": 8,
  "q": "Ötzis Beil ist aus Kupfer. Aber woher kam das Kupfer? Lies die Pressemeldung und beantworte die drei Fragen.",
  "hint": "Recherche: Pressemeldung des Südtiroler Archäologiemuseums und der Universität Padua vom 1. März 2024 – über 50 Metallgegenstände untersucht. Link im Theorie-Teil »Metall, Können und Austausch« unter »Zum Lesen«, Suchtipp »Archäometallurgie Ötzi Kupfer Pressemeldung«. Info: Theorieteil »Metall, Können und Austausch«",
  "type": "multi",
  "fields": [["methode", "a) So bestimmt man die Herkunft"], ["herkunft", "b) Das Kupfer stammt aus"], ["reise", "c) Warum kein Beweis für eine Reise?"]],
  "chk": {"methode": {"kw": [["Isotope oder Verunreinigungen", r"isotop|blei|verunreinig|analyse|chemisch"]], "man": True},
          "herkunft": {"kw": [["südliche Toskana", r"toskana|italien"]], "man": True},
          "reise": {"kw": [["Metall wurde gehandelt", r"handel|austausch|weitergegeben|transport|metall|rohstoff|nicht ötzi|nicht oetzi|material|zwischenhändler|zwischenhaendler"]], "man": True}},
  "sol": [["Musterlösung", ["a) Man vergleicht Bleiisotope und chemische Verunreinigungen im Kupfer mit denen von Lagerstätten; das Bleiisotopenverhältnis bleibt beim Verhütten und Verarbeiten gleich.",
                          "b) Aus der südlichen Toskana (nicht aus lokaler Produktion in den Alpen).",
                          "c) Die Analyse zeigt den Weg des Metalls, nicht den Weg einer Person. Metall und Waren wurden weitergegeben und gehandelt; wer sie transportierte, sagt der Befund nicht."]]],
  "fsol": {"methode": "Bleiisotope und Verunreinigungen im Kupfer", "herkunft": "südliche Toskana", "reise": "Metall wurde gehandelt – Befund zeigt den Weg des Materials"},
  "tip": ["Metall, Können und Austausch", "theorie.html#metall"]},

 {"id": "a12", "nr": 13, "title": "Partnercheck", "src": "Buch S. 25–40", "own": True, "tag": "Zusatz", "h": 0, "zeit": 5,
  "q": "Zu zweit, ohne Handy: A nimmt vier Karten aus dem Abschnitt »Partnercheck« im Theorieteil und liest die Fragen vor. B antwortet, A vergleicht mit der Antwort auf der Karte und hakt ab. "
       "Dann tauscht ihr. Trag ein, mit wem du geübt hast und wie viele deiner vier Antworten gepasst haben.",
  "hint": "Ehrlich zählen – es geht um deine Wiederholung, nicht um Punkte.",
  "type": "multi",
  "fields": [["partner", "Partnercheck mit (Vorname)"], ["richtig", "Davon hat gepasst", ["4 von 4", "3 von 4", "2 von 4", "1 von 4", "0 von 4"], False],
             ["unsicher", "Da war ich noch unsicher (Stichwort, freiwillig)"]],
  "opt": ["unsicher"],
  "chk": {"partner": {"kw": [["Name", r"[a-zäöüß]{2,}"]], "man": True}},
  "sol": [["Hinweis", ["Kein Lösungsschlüssel – die Antworten stehen auf den Karten im Theorieteil."]]],
  "tip": ["Partnercheck", "theorie.html#partnercheck"]},
]
assert sorted(t["nr"] for t in T) == [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]   # 9 = »Ziele erreicht?«, wird unten eingefügt
for _t in T:
    for _k, _c in _t["chk"].items():
        assert _k in [f[0] for f in _t["fields"]], (_t["id"], _k)
    for _f in _t["fields"]:
        if len(_f) > 2 and _f[0] in _t["chk"] and "sel" in _t["chk"][_f[0]]:
            assert _t["chk"][_f[0]]["sel"] in _f[2], (_t["id"], _f[0])
    for _x in [_t["q"]] + [z for _a, zz in _t["sol"] for z in zz]:
        assert "√" not in _x and "≈" not in _x, (_t["id"], "Zeichen fehlt in der PDF-Schrift")

PFLICHT = [t["nr"] for t in T if t["h"] and t["tag"] != "Zusatz"]
assert PFLICHT == list(range(1, 9))
BESPRECHEN = [t["nr"] for t in T if t.get("besprechen")]

GRP = {1: "Stunde 1 · " + STUNDENTITEL[1] + " (Buch S. 25–39)",
       2: "Stunde 2 · " + STUNDENTITEL[2] + " (Buch S. 39–40) · nach dem Test",
       3: "Stunde 3 · " + STUNDENTITEL[3] + " (Buch S. 105–118)",
       0: "Zusatz · Für Schnelle und Neugierige · freiwillig, keine Hausübung"}

LERNZIELE = ["erklären, wie **Landwirtschaft und Vorräte** das Zusammenleben veränderten, und Vorteile und Probleme nennen",
             "am Beispiel **Ägyptens und Mesopotamiens** zeigen, wie frühe Staaten organisiert waren",
             "aus einem historischen Text Aussagen über **Macht und Gesellschaft** gewinnen und die Grenzen der Quelle erklären",
             "**Athen, die römische Republik und die Herrschaft des Augustus** nach Beteiligung und Kontrolle vergleichen"]

HEUTE_ZIEL = {1: "Vorrat, Spezialisierung und Streit um Verteilung erklären – und Stadtstaat und Flächenkönigtum vergleichen.",
              2: "Eine Rechtssammlung als Quelle lesen: Was zeigt sie – und was nicht?",
              3: "Athen, Republik und Prinzipat nach Beteiligung und Kontrolle vergleichen."}

WICHTIGSTE = ["**Landwirtschaft** ermöglichte Vorräte und Spezialisierung, brachte aber auch neue Probleme: Missernten, Krankheiten und Streit um die Verteilung. Der Wandel verlief regional sehr verschieden.",
              "**Stadtstaat** (Mesopotamien) und **Flächenkönigtum** (Ägypten) lösten ähnliche Aufgaben – Abgaben, Vorräte, Verwaltung, Religion – in unterschiedlicher Form. Ein großer Fluss erklärt keinen Staat allein.",
              "**Hammurabis Rechtssammlung** (um 1750 v. Chr.) ordnet Konflikte und zeigt eine ungleiche Gesellschaft. Eine schriftliche Regel ist nicht dasselbe wie gleiches Recht, und aus dem Text allein wissen wir nicht, wie jeder Fall entschieden wurde.",
              "**Athen** kannte direkte Beteiligung der Bürger – aber nur erwachsener Männer; Frauen, Versklavte und Fremde (Metöken) waren ausgeschlossen. Viele Ämter wurden gelost, die Strategen gewählt.",
              "Die **römische Republik** verteilte Macht auf mehrere Ämter, blieb aber von der Oberschicht geprägt. **Augustus** ließ die Einrichtungen bestehen, vereinte aber die entscheidende Macht in seiner Person (Prinzipat)."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Neolithische Revolution", "tiefgreifender Wandel zu Ackerbau und Viehzucht, der viele Generationen dauerte und in mehreren Regionen eigenständig ablief"],
                ["Domestikation", "wilde Pflanzen und Tiere werden durch Züchtung an das Leben mit dem Menschen angepasst"],
                ["Sesshaftigkeit", "Menschen bleiben dauerhaft an einem Ort wohnen"],
                ["Vorrat", "gelagerte Nahrung für schlechte Zeiten – muss geschützt und verteilt werden"],
                ["Spezialisierung", "bestimmte Tätigkeiten werden besonders gut und regelmäßig ausgeübt (z. B. Töpfern, Metallverarbeitung)"],
                ["Ressource", "Rohstoff oder Mittel, das man zum Leben und Wirtschaften braucht (Land, Wasser, Metall)"],
                ["Bronze", "Kupferlegierung, meist mit Zinn (Beispiel: rund 90 % Kupfer, 10 % Zinn); Rohstoffe musste man oft einhandeln"],
                ["Hochkultur", "gebräuchlicher Begriff für frühe städtische Gesellschaften mit Verwaltung und Schrift – sagt nichts über den Wert der Menschen"],
                ["Stadtstaat", "eine Stadt bildet zusammen mit ihrem Umland einen eigenen Staat"],
                ["Flächenkönigtum", "Vergleichsbegriff: Königtum über einen größeren, zusammenhängenden Raum (Ägypten am Nil)"],
                ["Hierarchie", "Ordnung, in der Menschen und Ämter unterschiedliche Stellungen und Befugnisse haben"],
                ["Legitimation", "Begründung, warum eine Herrschaft gelten soll (z. B. durch Religion oder Recht)"],
                ["Abgaben", "Teil von Ernte oder Arbeit, der an die Herrschaft geht"],
                ["Rechtssammlung", "gesammelte Regeln und Rechtsfälle – nicht dasselbe wie ein modernes Gesetzbuch"],
                ["Stele", "aufgerichteter Stein mit Inschrift"],
                ["Befund / Deutung", "Befund: was man am Objekt oder Text feststellen kann · Deutung: was man daraus (begründet) schließt"],
                ["Polis", "griechische Gemeinschaft aus Stadt und Umland, politisch selbstständig"],
                ["Metöken", "dauerhaft in Athen lebende Menschen ohne athenisches Bürgerrecht"],
                ["Volksversammlung", "Versammlung der berechtigten Bürger, in Athen oberstes Entscheidungsorgan"],
                ["Los / Wahl", "zwei Verfahren, um Ämter zu besetzen: Zufall unter den Bewerbern oder Abstimmung"],
                ["Strategen", "in Athen gewählte Heerführer"],
                ["Republik (res publica)", "lat. »öffentliche Angelegenheit«; in Rom eine Ordnung mit mehreren Ämtern und Senat, geprägt von der Oberschicht"],
                ["Konsul / Senat / Volkstribun", "zwei Spitzenbeamte mit begrenzter Amtszeit / Rat einflussreicher Familien / Vertreter der Plebejer mit Einspruchsrecht"],
                ["Prinzipat / Princeps", "Herrschaftsform des Augustus: »Erster unter Gleichen« mit entscheidender Macht bei einer Person"]]

WEISST_DU_NOCH = {
    2: [("Ein Damm bricht, mehrere Felder stehen unter Wasser. Wer sollte die Folgen tragen – und wer entscheidet darüber?", "Das ist eine Frage der Zuständigkeit: Eine Gemeinschaft braucht Regeln, wer verantwortlich ist und wer entscheidet. Genau das regelt § 53 bei Hammurabi."),
        ("Warum musste man Vorräte verwalten?", "Vorräte mussten geschützt, gelagert und verteilt werden – sonst gab es Streit und Verluste.")],
    3: [("Warum musste man Vorräte verwalten?", "Vorräte mussten geschützt, gelagert und verteilt werden; wer die Verteilung kontrolliert, gewinnt Einfluss."),
        ("Was zeigt Hammurabis Sammlung über Ungleichheit?", "Gleiche Verletzung, ungleiche Folgen: Die Rechtsfolge hängt vom Stand des Opfers ab."),
        ("Was bleibt bei dieser Quelle offen?", "Ob jeder Fall im Alltag wirklich so entschieden wurde – und wie der König gesehen werden wollte.")],
}

STOPPFRAGEN = {
    1: [("Warum führt Landwirtschaft nicht zwangsläufig zu einem Staat?", "Weil auch Handel, Konflikte, Religion und die örtlichen Bedingungen mitwirken – es gibt keinen Automatismus."),
        ("Warum zeigt Ötzis Kupferbeil nicht, dass er ein Anführer war?", "Das Beil belegt Kupferverarbeitung, aber weder Beruf noch Rang noch eine Reise Ötzis."),
        ("Stimmt der Satz »Hochkultur heißt: Diese Menschen waren besser«?", "Nein – der Begriff beschreibt frühe städtische Gesellschaften mit Verwaltung und Schrift, er bewertet keine Menschen.")],
    2: [("Welche zwei Dinge zeigen § 53 und § 233 über die Gesellschaft?", "Infrastruktur und Bauleistung waren wirtschaftlich wichtig: Wer einen Schaden verursacht, haftet dafür."),
        ("Warum sind Auge-Regeln ein Beleg für Ungleichheit?", "Dieselbe Verletzung hat je nach Stand des Opfers eine andere Folge.")],
    3: [("Was ist der Unterschied zwischen Los und Wahl?", "Beim Los entscheidet der Zufall unter den Berechtigten, bei der Wahl die Stimmen."),
        ("Warum ist Rom als Republik noch keine moderne Demokratie?", "Vermögen, Herkunft und Ausschluss (Frauen, Versklavte) prägten die Beteiligung stark; die Oberschicht hatte großen Einfluss."),
        ("Was bedeutet Prinzipat?", "Die Einrichtungen der Republik bestehen weiter, die entscheidende Macht liegt aber beim Princeps.")],
}

PARTNERKARTEN = [("Warum entsteht aus Landwirtschaft nicht automatisch ein Staat?", "Auch Handel, Konflikte, Religion und örtliche Bedingungen wirken mit."),
                 ("Was ist ein Stadtstaat?", "Eine Stadt mit ihrem Umland als eigener Staat (z. B. Uruk)."),
                 ("Wofür wurde frühe Schrift in Mesopotamien gebraucht?", "Unter anderem für Listen: Mengen, Güter, Abgaben – Verwaltung."),
                 ("Was ist ein Flächenkönigtum?", "Ein Königtum über einen größeren zusammenhängenden Raum, z. B. am Nil mit einem Pharao an der Spitze."),
                 ("Was zeigt Hammurabis Sammlung NICHT?", "Ob jeder Fall im Alltag genau so entschieden wurde."),
                 ("Wer durfte im klassischen Athen mitentscheiden?", "Erwachsene männliche Bürger – nicht Frauen, Versklavte, Metöken."),
                 ("Los oder Wahl: Wie wurden die Strategen bestimmt?", "Sie wurden gewählt. Viele andere Ämter wurden gelost."),
                 ("Was heißt Prinzipat?", "Die Einrichtungen bleiben, aber die entscheidende Macht liegt beim Princeps (Augustus).")]

STOLPERSTEINE = [("»Revolution« heißt »über Nacht«", "Die Neolithische Revolution dauerte viele Generationen und lief in mehreren Regionen eigenständig ab – nicht überall in derselben Reihenfolge von Sesshaftigkeit und Ackerbau."),
                 ("»Hochkultur« als Rangstufe", "Der Begriff beschreibt frühe städtische Gesellschaften mit Verwaltung und Schrift. Er wertet keine Menschen ab, und nicht jedes Merkmal gilt überall. Auch »Fluss = Staat« ist zu einfach."),
                 ("Hammurabi = »erstes Gesetz«, alle gleich", "Es gab ältere Rechtssammlungen. Hammurabis Sammlung ist ein Zeugnis königlicher Rechtsetzung und Selbstdarstellung, kein modernes Gesetzbuch und kein Bericht über den Rechtsalltag."),
                 ("Athen = Demokratie für alle", "Beteiligt waren nur erwachsene männliche Bürger. Frauen, Versklavte und Metöken waren ausgeschlossen. Viele Ämter wurden gelost, die Strategen gewählt. Das Perikles-Gemälde von 1852 ist eine späte Darstellung."),
                 ("Republik = Demokratie, Augustus = Republik zurück", "Rom war eine Republik mit starkem Einfluss der Oberschicht. Augustus nannte sich Princeps, vereinte aber die Macht – die Selbstaussage ist Quelle, kein Urteil. 476 ist eine Orientierungsmarke für Westrom, Ostrom bestand weiter.")]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite) – aus dem ChatGPT-Pool, Auswahlmöglichkeiten überarbeitet
 ("Landwirtschaft", "Warum spricht man von der »Neolithischen Revolution«?", ["Der Wandel veränderte das Leben tief, dauerte aber Generationen.", "Er geschah in allen Regionen im selben Jahr.", "Eine Regierung beschloss überall den Ackerbau.", "Er endete nach wenigen Jahren wieder."],
  "»Revolution« meint hier die große Wirkung, nicht einen einzelnen Tag.", "Buch S. 25–28"),
 ("Vorräte", "Welche Aussage über Vorräte ist begründet?", ["Sie ermöglichen Spezialisierung, können aber Streit auslösen.", "Sie machen alle Menschen automatisch gleich reich.", "Sie führen zwangsläufig zu einer Demokratie.", "Sie waren nur für Tiere wichtig."],
  "Möglichkeiten und neue Probleme bestehen nebeneinander.", "Buch S. 25–28"),
 ("Probleme", "Welches Problem bringt enges Zusammenleben in Dörfern mit sich?", ["Krankheiten können sich leichter ausbreiten.", "Es gibt keine Nahrung mehr.", "Niemand kann mehr Werkzeug herstellen.", "Alle müssen weiterwandern."],
  "Missernten, Krankheiten und Streit gehören zum Leben mit Vorräten dazu.", "Buch S. 25–28"),
 ("Metall", "Was zeigt Ötzis Kupferbeil über seine Zeit?", ["Man konnte Kupfer verarbeiten – dafür brauchte es Rohstoffe und Können.", "Ötzi war ein Anführer.", "Ötzi ist selbst bis in die Toskana gereist.", "Damals gab es schon überall Eisen."],
  "Aus dem Beil allein folgen weder Beruf noch Rang noch eine Reise. Die Materialanalyse zeigt, dass Kupfer aus der Toskana ausgetauscht wurde.", "Buch S. 29–32"),
 ("Stadtstaat", "Was ist ein mesopotamischer Stadtstaat?", ["Eine Stadt mit ihrem Umland und eigenen Herrschaftseinrichtungen.", "Eine Festung ohne Umland.", "Eine moderne Hauptstadt mit Parlament.", "Ein Reich aus vielen Königreichen."],
  "Die Stadt bildet zusammen mit ihrem Umland eine politische Einheit.", "Buch S. 33–39"),
 ("Flächenkönigtum", "Was passt zum ägyptischen Flächenkönigtum?", ["Ein König mit Verwaltung für ein langes Flusstal voller Siedlungen.", "Eine einzelne Stadt mit Umland bildet einen eigenen Staat.", "Eine Volksversammlung entscheidet über alles.", "Es gab keine Abgaben."],
  "Der Pharao stand an der Spitze einer hierarchischen Ordnung über einen großen Raum.", "Buch S. 36–37"),
 ("Schrift", "Wozu dienten frühe Aufzeichnungen in Mesopotamien unter anderem?", ["Zur Erfassung von Mengen, Gütern und Abgaben.", "Zum Schreiben von Romanen.", "Für allgemeine Wahlen.", "Nur für Briefe an Götter."],
  "Listen machen Entscheidungen nachvollziehbar – und geben denen Einfluss, die sie führen und kontrollieren.", "Buch S. 34–35"),
 ("Fluss", "Warum erklärt ein großer Fluss allein die Entstehung eines Staates nicht?", ["Auch Handel, Konflikte, Religion und Machtbildung wirken mit.", "Frühe Staaten lagen nie an Flüssen.", "Wasser erfordert keine Organisation.", "Flüsse waren damals ausgetrocknet."],
  "Bewässerung verlangt Organisation, aber es gibt keinen zwingenden Weg von Wasserwirtschaft zu Alleinherrschaft.", "Buch S. 33, 36, 39"),
 ("Hammurabi", "Was zeigen die unterschiedlichen Rechtsfolgen für eine Augenverletzung bei Hammurabi?", ["Die Rechtsfolge hing vom gesellschaftlichen Stand des Opfers ab.", "Alle wurden rechtlich gleich behandelt.", "Es gab keine schriftlichen Regeln.", "Nur Frauen wurden bestraft."],
  "Gleiche Art der Verletzung, unterschiedliche Folgen – das zeigt eine hierarchische Gesellschaft.", "Buch S. 40"),
 ("Quelle", "Was lässt sich aus Hammurabis Rechtssammlung allein NICHT belegen?", ["Ob jeder Fall im Alltag genau so entschieden wurde.", "Dass bestimmte Konflikte geordnet werden sollten.", "Dass Rechtsfolgen sich nach dem Stand unterschieden.", "Dass der König seine Ordnung zeigen wollte."],
  "Vorschrift und tatsächliche Anwendung sind verschiedene Quellenfragen.", "Buch S. 40"),
 ("Hammurabi", "Gilt Hammurabis Sammlung als die erste Rechtssammlung der Geschichte?", ["Nein, es gab ältere Rechtssammlungen.", "Ja, davor gab es keine Regeln.", "Ja, weil sie als Einzige aufgeschrieben wurde.", "Nein, sie ist nur eine Legende."],
  "Hammurabis Sammlung ist bedeutend, aber ältere Sammlungen (z. B. von Ur-Nammu) sind bekannt.", "Buch S. 40"),
 ("Athen", "Wer durfte im klassischen Athen in der Volksversammlung mitentscheiden?", ["Erwachsene männliche Bürger.", "Alle erwachsenen Männer, die in Athen lebten, auch Fremde.", "Alle Einwohner, auch Frauen und Versklavte.", "Nur der Adel."],
  "Große Gruppen waren ausgeschlossen; entscheidend war der Bürgerstatus.", "Buch S. 109–111"),
 ("Athen", "Welche Aussage zu den Ämtern in Athen stimmt?", ["Viele Ämter wurden gelost, die Strategen gewählt.", "Alle Ämter wurden vererbt.", "Alle Ämter wurden gewählt.", "Ein König ernannte alle Beamten."],
  "Die Auswahlverfahren unterschieden sich nach Aufgabe.", "Buch S. 109–111"),
 ("Republik", "Warum ist die römische Republik keine moderne Demokratie?", ["Vermögen, Herkunft und Ausschluss prägten die Beteiligung stark.", "Weil das Wort aus dem Lateinischen stammt.", "Weil es keine Ämter gab.", "Weil alle Einwohner abstimmen durften."],
  "Der Name »Republik« allein beschreibt die tatsächliche Beteiligung nicht.", "Buch S. 113"),
 ("Augustus", "Warum muss Augustus' eigener Tatenbericht geprüft werden?", ["Er enthält auch das Bild, das Augustus von sich vermitteln wollte.", "Alte Texte sind immer gelogen.", "Man darf Quellen nie vergleichen.", "Er ist ein neutraler Bericht Dritter."],
  "Die Quelle ist nützlich, aber sie ist seine eigene Perspektive.", "Buch S. 114–115"),
 ("Prinzipat", "Was kennzeichnet den Prinzipat des Augustus?", ["Die Einrichtungen bleiben, die entscheidende Macht liegt bei einer Person.", "Alle Römer haben gleich viel Macht.", "Es gibt keinen Senat und keine Ämter mehr.", "Der Herrscher regiert nur als Priester."],
  "Formale Einrichtungen und tatsächliche Machtverteilung müssen verglichen werden.", "Buch S. 114–115"),
 ("476", "Welche Aussage zum Jahr 476 ist angemessen?", ["Eine Orientierungsmarke für das Ende Westroms; Ostrom bestand weiter.", "An diesem Tag endete überall jede römische Lebensform.", "Damals begann die Renaissance.", "Das ganze Römische Reich war damit erledigt."],
  "Eine Epochenmarke ersetzt keine Erklärung längerer Veränderungen.", "Buch S. 115–118"),
 ("Zeitstrahl", "Ötzi lebte um 3300 v. Chr., die frühe Schrift entstand in Mesopotamien im späten 4. Jahrtausend v. Chr. Was stimmt?", ["Beides liegt ungefähr in derselben Zeit, aber in verschiedenen Regionen.", "Die Schrift entstand erst lange nach Ötzi – und überall zugleich.", "Ötzi lebte nach Hammurabi.", "Schrift gab es schon vor der Landwirtschaft."],
  "Entwicklungen verlaufen gleichzeitig, aber nicht überall gleich.", "Buch S. 24–35"),
]
for _q in QUIZ:
    assert len(_q[2]) == 4 and len(set(_q[2])) == 4, _q[1]


# ====================================================================== Kompetenzmodell (Skill bhak-kompetenzmodell, 20.11.2026)
# hd: A verstehen und wiedergeben · B anwenden und analysieren · C diskutieren, interpretieren, begründen, bewerten
# niveau 1 = + (Grundlegendes) · 2 = ++ (Vertiefung). Chip = Kompetenz, nicht mit der Marke (DEMO, GRUPPENARBEIT …) verwechseln.
ZIELE = [{"nr": 1, "hd": "A", "text": "Ich kann erklären, wie Landwirtschaft, Vorräte und Spezialisierung das Zusammenleben verändert haben – mit Vorteilen und Problemen.",
          "theorie": "vorrat", "buch": "Buch S. 25–28"},
         {"nr": 2, "hd": "A", "text": "Ich kann Stadtstaat und Flächenkönigtum vergleichen und sagen, welche Aufgaben beide lösen mussten.",
          "theorie": "staaten", "buch": "Buch S. 33–39"},
         {"nr": 3, "hd": "B", "text": "Ich kann aus Hammurabis Rechtssammlung herauslesen, was sie über Ordnung und Ungleichheit zeigt – und wo ihre Grenze liegt.",
          "theorie": "regeln", "buch": "Buch S. 39–40"},
         {"nr": 4, "hd": "C", "text": "Ich kann Athen, die römische Republik und das Prinzipat nach Beteiligung und Kontrolle vergleichen und meine Einschätzung begründen.",
          "theorie": "vergleich", "buch": "Buch S. 109–115"}]
KOMPETENZ = {"a1": ("B", 1, 1), "a2": ("C", 2, 1), "a3": ("A", 1, 2), "a4": ("B", 2, 3),
             "a5": ("A", 1, 4), "a6": ("B", 2, 4), "a7": ("C", 2, 4), "a8": ("A", 1, 2),
             "a9": ("B", 2, 2), "a10": ("C", 2, 3), "a11": ("B", 2, 1), "a12": ("A", 1, 2)}
for _t in T:
    if _t["id"] in KOMPETENZ:
        _t["hd"], _t["niveau"], _t["ziel"] = KOMPETENZ[_t["id"]]
_pf = [t for t in T if t["id"] in KOMPETENZ and t["h"] and t["tag"] != "Zusatz"]
assert sum(t["niveau"] == 1 for t in _pf) >= 2 and any(t["niveau"] == 2 for t in _pf), "Pflicht: mindestens zwei + und eine ++"
assert {t["hd"] for t in T if "hd" in t} == {"A", "B", "C"}, "A, B und C müssen vorkommen"

# ---------------------------------------------------------------- »Ziele erreicht?« (Selbsteinschätzung, keine Punkte)
_ZT = {1: "Theorie »Vom Sammeln zum Vorrat« · Buch S. 25–28", 2: "Theorie »Frühe Staaten« · Buch S. 33–39",
       3: "Theorie »Was die Regeln verraten« · Buch S. 39–40", 4: "Theorie »Athen und Rom im Vergleich« · Buch S. 109–115"}
_ZZ = ({"id": "zz", "nr": 9, "title": "Ziele erreicht? Deine Selbsteinschätzung", "src": "Meine Ziele (Theorie oben)", "own": True,
  "tag": "Selbsteinschätzung", "h": 3, "zeit": 2, "type": "multi", "vorhersage": True,
  "q": "Schätz ehrlich ein, wie gut du die vier Ziele der Einheit erreicht hast. Es gibt keine Punkte. Bei »noch nicht«: Lies den angegebenen Theorie-Teil und die Buchseite noch einmal.",
  "hint": "Ehrlich ist besser als schön – das hilft dir beim Lernen für den Test.",
  "fields": [["ziel%d" % z["nr"], "Ziel %d (%s): %s – bei »noch nicht«: %s" % (z["nr"], z["hd"], z["text"], _ZT[z["nr"]]),
              ["zur Gänze", "überwiegend", "noch nicht"], False] for z in ZIELE],
  "chk": {}, "sol": [["Hinweis", ["Selbsteinschätzung – keine richtige oder falsche Antwort."]]],
  "tip": ["Meine Ziele", "theorie.html#ziele"]})
T.insert(min(i for i, t in enumerate(T) if t["tag"] == "Zusatz"), _ZZ)   # vor den Zusatzaufgaben, damit der Stundenkasten nur einmal kommt
assert [t["nr"] for t in T] == list(range(1, 14)), "Aufgaben müssen in Reihenfolge stehen (Stephan 23.11.2026)"

# ====================================================================== Zusatztheorie für Schnelle (Standard 23.11.2026)
# Geprüfter Artikel: Spektrum, »Neolithische Revolution: Ackern, ohne satt zu werden«, 09.03.2011, Kürzel »jd«,
# zur Studie von Samuel Bowles (Santa Fe Institute), PNAS 2011, doi 10.1073/pnas.1010733108. Von Claude selbst geöffnet und geprüft (22.11.2026).
LESE_LINK = "https://www.spektrum.de/news/ackern-ohne-satt-zu-werden/1065918"
T.append({"id": "les", "nr": 14, "title": "Lesen und prüfen: Ackern, ohne satt zu werden", "src": "Spektrum, 09.03.2011 · Zusatz", "own": True,
  "tag": "Zusatz", "h": 0, "zeit": 10, "type": "multi", "hd": "C", "niveau": 2, "ziel": 1,
  "q": "Du bist mit allem fertig? Dann lies den kurzen Artikel (Link in der Theorie, Abschnitt »Noch mehr wissen«) und filtere das Wichtigste heraus.",
  "hint": "Quelle: Spektrum, »Neolithische Revolution: Ackern, ohne satt zu werden«, 09.03.2011, Kürzel »jd«, zur Studie von Samuel Bowles (PNAS 2011). "
          "Info: Theorieteil »Neue Möglichkeiten, neue Probleme«",
  "fields": [["drei", "a) Die drei wichtigsten Aussagen – in eigenen Worten, als Stichpunkte"],
             ["was", "b) Was hat Samuel Bowles berechnet?",
              ["Wie viele Kalorien eine Stunde Feldarbeit einbrachte – verglichen mit der Arbeit von Jägern und Sammlern",
               "Wie viele Menschen in der Jungsteinzeit lebten", "Wie lange Getreide gelagert werden kann", "Wie hoch die Ernteerträge heute sind"]],
             ["ergebnis", "c) Was kam dabei heraus?",
              ["Die frühen Bauern steckten vermutlich mehr Arbeit in ihren Lebensunterhalt, nicht weniger",
               "Ackerbau war von Anfang an weniger Arbeit", "Die Erträge waren sofort doppelt so hoch", "Jäger und Sammler arbeiteten mehr"]],
             ["warum", "d) Warum setzte sich der Ackerbau trotzdem durch?",
              ["Das bleibt offen – Bowles vermutet soziale Gründe: größere Gruppen konnten sich besser organisieren und waren militärisch stärker",
               "Weil Ackerbau sofort mehr Nahrung brachte", "Weil alle Jagdtiere ausgestorben waren", "Weil ein Gesetz es vorschrieb"]],
             ["kritik", "e) Quellenkritik: Der Artikel nennt als Autor nur »jd« und stützt sich auf eine Modellrechnung von 2011. Was heißt das? Zwei Punkte."],
             ["bruecke", "f) Brücke zur Stunde: Was heißt das für »Neue Möglichkeiten, neue Probleme«? (ein Satz)"]],
  "chk": {"was": {"sel": "Wie viele Kalorien eine Stunde Feldarbeit einbrachte – verglichen mit der Arbeit von Jägern und Sammlern"},
          "ergebnis": {"sel": "Die frühen Bauern steckten vermutlich mehr Arbeit in ihren Lebensunterhalt, nicht weniger"},
          "warum": {"sel": "Das bleibt offen – Bowles vermutet soziale Gründe: größere Gruppen konnten sich besser organisieren und waren militärisch stärker"},
          "drei": {"man": True, "kw": [["mehr Arbeit statt weniger", "arbeit|mühe|muehe|stunden|aufwand"],
                                       ["Mangel, kleinere Körpergröße, Abnutzung", "mangel|körpergröße|koerpergroesse|klein|abnutzung|knochen|krank"],
                                       ["Modellrechnung mit Unsicherheiten", "modell|berechn|bowles|unsicher|schätz|schaetz"]]},
          "kritik": {"man": True, "kw": [["kein Autorname und eine Modellrechnung von 2011", "autor|kürzel|kuerzel|jd|modell|unsicher|2011|alt|pnas|studie|nachprüf|nachpruef"]]},
          "bruecke": {"man": True, "kw": [["Die Vorteile waren nicht sofort da", "nicht sofort|mehr arbeit|problem|nachteil|abhängig|abhaengig|mangel|kein automatismus"]]}},
  "fsol": {"drei": "mehr Arbeit als vorher · Hinweise auf Mangelernährung · Modellrechnung, keine Messung",
           "kritik": "Autor nur als Kürzel »jd«; Modellrechnung von 2011 mit großen Unsicherheiten – zweite Quelle wäre nötig",
           "bruecke": "Die Landwirtschaft brachte nicht sofort ein besseres Leben, sondern zuerst mehr Arbeit und neue Probleme."},
  "sol": [["Musterlösung", [
    "a) z. B.: Die frühen Bauern arbeiteten mehr als Jäger und Sammler. · Knochenfunde zeigen Mangelernährung, kleinere Körpergröße und Abnutzung. · "
    "Die Zahlen stammen aus einer Modellrechnung, nicht aus Messungen an den Menschen selbst.",
    "b) Kalorien pro Arbeitsstunde Feldarbeit im Vergleich zur Arbeit von Jägern und Sammlern.",
    "c) Die frühen Bauern investierten vermutlich deutlich mehr Arbeit, auf keinen Fall weniger (unzureichende Technik, Verarbeitung und Lagerung, "
    "Schutz vor Ernteverlusten, Abhängigkeit von einer oder zwei Feldfrüchten).",
    "d) Bowles nennt es rätselhaft und vermutet soziale Gründe: In größeren, dichter zusammenlebenden Gruppen ließen sich Kinderbetreuung und "
    "Auseinandersetzungen besser organisieren; militärische Überlegenheit könnte die Ausbreitung erklären.",
    "e) Kein Autorname (nur »jd«) – die Verantwortung liegt bei der Redaktion. Die Berechnung ist ein Modell von 2011 mit großen Unsicherheiten; "
    "der Artikel sagt das selbst. Für eine Prüfung bräuchte man die Studie (PNAS) oder eine zweite Quelle.",
    "f) Die Landwirtschaft war kein sofortiger Gewinn: Erst kamen mehr Arbeit und neue Probleme – genau das steht im Theorie-Teil."]]],
  "tip": ["Neue Möglichkeiten, neue Probleme", "theorie.html#probleme"]})
assert [t["nr"] for t in T] == list(range(1, 15)), "Aufgaben müssen in Reihenfolge stehen"


# ====================================================================== ABCD-Karte (Standard 15.11.2026)
# (Frage, richtig, [drei Ablenker aus echten Fehlvorstellungen], kurze Erklärung). Anzeige mischt die Antworten.
WDN_ABCD = {
 1: [("Was ist eine Primärquelle?", "Ein Zeugnis aus der Zeit selbst, zum Beispiel ein Vertrag oder ein Fundstück",
      ["Ein Schulbuchtext über diese Zeit", "Ein Film über diese Zeit", "Eine Zusammenfassung im Internet"],
      "Primärquelle = aus der Zeit selbst. Alles, was später darüber geschrieben wurde, ist eine Darstellung."),
     ("Womit beginnt man, wenn man prüft, ob ein Schriftstück echt ist?", "Mit Material, Schrift und Machart",
      ["Mit dem Gefühl beim Lesen", "Mit der Frage, ob die Geschichte spannend ist", "Mit dem Preis, den jemand dafür zahlt"],
      "Äußere Quellenkritik: Papier, Tinte, Schrift. Bei den Hitler-Tagebüchern fiel genau das auf."),
     ("Welches Jahr ist die übliche Marke für das Ende der Antike?", "476 n. Chr.", ["1492", "1789", "800 n. Chr."],
      "476 = Ende Westroms. Eine Epochenmarke ist eine Orientierung, kein Schalter.")],
 3: [("Warum musste man Vorräte verwalten?", "Weil sie geschützt, gelagert und verteilt werden mussten",
      ["Weil Vorräte von allein verderben", "Weil es schon Geld gab", "Weil die Schrift das vorschrieb"],
      "Wer die Verteilung kontrolliert, bekommt Einfluss – daraus kann Macht entstehen."),
     ("Was zeigt Hammurabis Sammlung über die Gesellschaft?", "Gleiche Verletzung, ungleiche Folge – je nach Stand des Opfers",
      ["Alle waren vor dem Recht gleich", "Es gab keine Strafen", "Nur Könige wurden bestraft"],
      "Schriftliches Recht ordnet, macht aber nicht gleich."),
     ("Was bleibt bei dieser Quelle offen?", "Ob im Alltag wirklich jeder Fall so entschieden wurde",
      ["Wie alt der Stein ist", "Ob Hammurabi gelebt hat", "In welcher Sprache sie geschrieben ist"],
      "Eine Regel auf Stein ist nicht der Beweis für die gelebte Praxis.")],
}
VERMUTUNG_ABCD = {
 "K2.1-D1": ("Woher stammt das Kupfer von Ötzis Beil?", "Aus der südlichen Toskana",
             ["Aus den Alpen, nahe dem Fundort", "Aus Anatolien, der heutigen Türkei", "Aus dem Balkan"],
             "Eine Analyse der Bleiisotope (Südtiroler Archäologiemuseum und Universität Padua, 2024) spricht für die südliche Toskana. "
             "Das zeigt den Weg des Metalls – nicht, dass Ötzi selbst dort war."),
}

# ====================================================================== Mitarbeits-Check (Standard 15.11.2026)
# 10 Fragen, nur Pflichtstoff, kein Militärbezug. Aufbau: (id, Frage, richtig, [drei falsch], Buchseite).
# "jahre" = Zahlenfrage mit Zufallszahlen (Abstand zweier Jahre v. Chr.).
MCHECK = [
 {"thema": "Vorrat und Spezialisierung", "n": 2, "fragen": [
   ("v1", "Was wurde durch Vorräte möglich?", "Einzelne konnten sich auf andere Arbeiten spezialisieren",
    ["Alle mussten weiter täglich Nahrung suchen", "Die Bevölkerung wurde kleiner", "Niemand musste mehr arbeiten"], "S. 25–28"),
   ("v2", "Welches Problem kam mit dem Leben von Vorräten?", "Eine Missernte traf viele Menschen gleichzeitig",
    ["Es gab keine Krankheiten mehr", "Streit um Verteilung war ausgeschlossen", "Vorräte brauchten keinen Schutz"], "S. 25–28"),
   ("v3", "Was heißt »Neolithische Revolution«?", "Ein tiefgreifender Wandel, der viele Generationen dauerte",
    ["Ein Umsturz an einem einzigen Tag", "Ein Krieg um Ackerland", "Die Erfindung der Schrift"], "S. 25–26"),
   ("v4", "Was braucht man, um Kupfer zu verarbeiten?", "Rohstoff, Brennstoff und Können",
    ["Nur einen Hammer", "Nur Holz", "Eisen und Schrift"], "S. 29–32")]},
 {"thema": "Frühe Staaten und Schrift", "n": 3, "fragen": [
   ("s1", "Was ist ein Stadtstaat?", "Eine Stadt bildet mit ihrem Umland einen eigenen Staat",
    ["Ein Königtum über ein ganzes Flusstal", "Ein Dorf ohne Verwaltung", "Ein Bündnis mehrerer Länder"], "S. 33–39"),
   ("s2", "Wofür wurde die frühe Schrift in Mesopotamien gebraucht?", "Für Listen: Mengen, Güter und Abgaben",
    ["Für Romane", "Für Briefe an Verwandte", "Für Liedtexte"], "S. 34–35"),
   ("s3", "Welche Aufgabe mussten Mesopotamien und Ägypten beide lösen?", "Abgaben, Arbeit und Vorräte organisieren",
    ["Die Wahl eines Parlaments", "Die Ausgabe von Geldscheinen", "Den Bau von Eisenbahnen"], "S. 33–39"),
   ("s4", "Warum erklärt ein großer Fluss allein keinen Staat?", "Weil auch Handel, Konflikte, Religion und örtliche Bedingungen mitwirken",
    ["Weil Flüsse unwichtig waren", "Weil es damals keine Flüsse gab", "Weil Wasser keine Arbeit macht"], "S. 33–39")]},
 {"thema": "Hammurabi", "n": 2, "fragen": [
   ("h1", "Was entscheidet bei Hammurabi über die Rechtsfolge?", "Der gesellschaftliche Stand des Opfers",
    ["Das Alter des Täters", "Der Wohnort des Täters", "Der Wochentag der Tat"], "S. 39–40"),
   ("h2", "Was ist eine Rechtssammlung?", "Gesammelte Regeln und Rechtsfälle",
    ["Ein modernes Gesetzbuch mit Paragrafen für alle", "Eine Liste von Königen", "Ein Vertrag zwischen zwei Städten"], "S. 39–40"),
   ("h3", "Was zeigt § 53 (Dammbruch)?", "Wer einen Schaden verursacht, haftet dafür",
    ["Dämme waren verboten", "Wasser gehörte dem König", "Bauern durften keine Felder besitzen"], "S. 39–40")]},
 {"thema": "Athen und Rom", "n": 2, "fragen": [
   ("a1", "Wer durfte in Athen in der Volksversammlung entscheiden?", "Erwachsene männliche Bürger",
    ["Alle Einwohner der Stadt", "Nur die Strategen", "Alle, die in Athen geboren wurden"], "S. 109–111"),
   ("a2", "Wie wurden in Athen die Strategen bestimmt?", "Durch Wahl", ["Durch das Los", "Durch Erbfolge", "Durch den Rat der 500 allein"], "S. 109–111"),
   ("a3", "Was kennzeichnet den Prinzipat des Augustus?", "Die Einrichtungen bleiben, die entscheidende Macht liegt bei einer Person",
    ["Der Senat wurde abgeschafft", "Alle Römer hatten gleich viel Macht", "Es gab keine Ämter mehr"], "S. 114–115"),
   ("a4", "Warum war die römische Republik keine moderne Demokratie?", "Herkunft und Vermögen prägten die Beteiligung stark",
    ["Es gab gar keine Ämter", "Alle Bewohner durften abstimmen", "Der Kaiser bestimmte alles"], "S. 112–115")]},
 {"thema": "Zeitstrahl", "n": 1, "fragen": [
   ("z1", "Was war zuerst da?", "Die Landwirtschaft im Vorderen Orient – lange vor der Schrift",
    ["Die Schrift – erst danach die Landwirtschaft", "Beides begann gleichzeitig", "Die Städte – erst danach die Landwirtschaft"], "S. 24–40"),
   ("z2", "Was zeigt der gemeinsame Zeitstrahl?", "Die Entwicklungen liefen nicht überall gleichzeitig ab",
    ["Überall begann alles zur selben Zeit", "Jede Entwicklung dauerte genau 100 Jahre", "Die Reihenfolge ist bis heute unbekannt"], "S. 24–40")]},
]
assert sum(g["n"] for g in MCHECK) == 10
assert all(len(f[3]) == 3 or f[1] == "jahre" for g in MCHECK for f in g["fragen"])
MCHECK_KEY = "26-27-3BK-K2.1-5.4-Meilenst-check"
MCHECK_CODE = "2451"   # Startcode – im Seitencode nur als Prüfsumme; Prof. HOLZER zeigt ihn am Beamer
