"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, Lehrer-Infos der PPPs und Lösungsmappe PBGW 3BK · Meilensteine.
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Word). Grundlage: ChatGPT-Auftrag 29.10.2026, von Claude nachgeprüft."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v14: E3 »Neolithische Revolution«, E4 »Hochkulturen und frühe Staatenbildung«, E5 »Antike Vorbilder« (je 2 Std., zusammen 6 Std. brutto). "
                  "Hier: 3 Stunden (Stephans Vorgabe), Mo 16.11., Mo 23.11. (zuerst 20 min Test + 4 min Organisation), Mo 30.11.2026; Annahme 50 min. Buch: Trauner PBGW 3 S. 23–44, Ergänzungsbuch S. 58–73."),
    ("K02 / K04 ", "Einfluss historischer Entwicklungen auf Individuum, Gesellschaft und Staat beschreiben · Veränderungsprozesse beschreiben, Ursachen analysieren → Aufgabe 2 (begründete Zusammenhänge, zusätzliche Bedingung, Grenze der Erklärung)"),
    ("K01 ", "historische Quellen zur kritischen Rekonstruktion und Dekonstruktion einsetzen → Aufgabe 1 (Befund – Vermutung – Grenze), Aufgabe 4 (Hammurabi: Kontext, Aussage, Herrscherperspektive), Aufgabe 6 (Augustus-Tatenbericht)"),
    ("K05 ", "grundlegende Formen der Staatenbildung nennen, vergleichen und diskutieren → Aufgabe 3 (Stadtstaat und Flächenkönigtum)"),
    ("K08 ", "zivilisatorische Leistungen den Epochen zuordnen → Aufgabe 8 (gemeinsamer Zeitstrahl, in zwei Teilen)"),
    ("K06 ", "unterschiedliche Herrschaftsformen und Führungsstrukturen beschreiben, Auswirkungen erörtern → Aufgabe 5–7 (Athen, Republik, Prinzipat)"),
    ("N01 / N02 · P3 / P4 · SDG 2 ", "Veränderungsprozesse zusammenhängend betrachten · Demokratieverständnis durch Vergleich von Beteiligung und Ausschluss · Umwelterziehung (Abhängigkeit der Landwirtschaft von Boden und Wasser) · politische Bildung (Herrschaft, Recht, Beteiligung, Kontrolle) · "
                                      "Ernährungssicherung als heutige Frage (ohne antiken Gesellschaften heutige Ziele zuzuschreiben)"),
    ("GLV: ", "Im Jahresplan E3–E5 stehen keine GLV-Codes. Als **didaktische Ergänzung** (nicht Planbestand): Wertebewusstsein und Informationsresilienz – Rechtsgleichheit, Machtkontrolle, Prüfung von Herrscheraussagen (Aufgaben 4, 6, 10)."),
    ("Schulprofil: ", "Vorratshaltung und Transport als logistische Aufgabe · Verwaltung, Zuständigkeit und Befehlsketten (ein Schaubild einer Hierarchie sagt nichts über ihre Rechtmäßigkeit) · Heer und Gefolgschaft als Faktor römischer Macht – nicht nach dem Muster »die beste Armee gewinnt immer«."),
    ("Abweichung: ", "3 statt 6 Stunden brutto (Stephans Vorgabe); Kern in Aufgaben 1–8, Rest OPTIONAL. Kein Versuch (PBGW), kein CLIL. Teststoff für den 23.11. kommt von dir – es gibt noch keine Teststoff-Seite. Trauner-Seiten S. 105–118 (Antike) lagen nicht vor: Athen und Rom stützen sich auf das Ergänzungsbuch."),
]

THEMEN = {1: "Vorrat, Metall, Schrift, frühe Staaten (S. 25–39)", 2: "Hammurabis Rechtssammlung (S. 39–40)", 3: "Athen, Rom, Prinzipat (Ergänzungsbuch S. 62–73)"}


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, _ = PL.aufgaben_der(st)
        z = f"Lesen {PL.minuten(st, ['lesen'])} · Erklären {PL.minuten(st, ['erkl'])} · Aufgaben {PL.minuten(st, ['a'])} · Bespr. {PL.minuten(st, ['bespr'])} · Reserve {PL.minuten(st, ['reserve'])}"
        if PL.minuten(st, ["test"]): z = f"Test {PL.minuten(st, ['test'])} · " + z
        rows.append([f"{st['std']} · {st['datum']}", THEMEN[st["std"]], "– (kein Versuch)", PL.bereich(nrs), z, st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "Beamer mit TH-Unterricht · Mini-Whiteboards und Stifte (1 je Paar) · Tafel für die Tabelle zu Aufgabe 3 · Papier für die Zeitstrahl-Karten (sechs Spalten, Karten 1–4)",
            2: "Test (Stoff von dir, noch offen) · TH-AB mit dem Paragrafenblatt zu Aufgabe 4 (ausdrucken, je Paar eines) · farbige Stifte zum Markieren",
            3: "Platz für eine Skala 0–10 im Raum (Seil oder Kreide) · TH-AB mit Tabelle zu Aufgabe 7 (je Paar) · Zeitstrahl-Karten 5–9"}


def _karten():
    out = []
    k = I.KLASSEN[0]
    for st in PL.PLAN[k]:
        t, schritte = 0, []
        for name, m, oh, art in st["phasen"]:
            schritte.append(f"Min {t}–{t + m}: {name}" + (" (ohne Handy)" if oh else "")); t += m
        schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
        ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org", "test")))
        out.append((f"3BK · Stunde {st['std']} · {st['datum']} · {THEMEN[st['std']]}", schritte, MATERIAL[st["std"]], ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Einheit einblenden vor der ersten Stunde (Mo 16.11.): GitHub → Actions → »Einheit ein-/ausblenden« → 3bk-pbgw/k2-5-meilensteine → einblenden. Die Direktlinks und QR-Codes funktionieren auch versteckt.",
    "TH-Unterricht einmal mit F5 durchklicken: Lösungen erscheinen erst per Klick. Regiefolien je Stunde ausgeblendet am Anfang; Start je Stunde über »Benutzerdefinierte Bildschirmpräsentation«.",
    "Test am 23.11.: Stoff und Unterlagen kommen von dir. Sobald du den Stoff nennst, baue ich Teststoff und Handy-Seite. Die Stunde ist auf 20 min Test + 4 min Organisation + 26 min Unterricht geplant.",
    "Stunde 1: Ötzi kennen die Kadetten aus der Quellenarbeit (Buch S. 30) – das Beil nur als Anlass für Befund, Vermutung, Grenze. Eigene Zeichnung auf der Folie, kein Foto.",
    "Stunde 2: Paragrafenblatt ausdrucken (TH-AB, Aufgabe 4). Hammurabi-Text ist eine **Arbeitsfassung**, kein wörtliches Zitat (Buch S. 40).",
    "Stunde 3: Aufgabe 5 und 6 beziehen sich auf das Ergänzungsbuch (S. 62–65, 70–71) – Kadetten brauchen es als Buch oder du zeigst die Seiten. Das Perikles-Gemälde (S. 65) ist von 1852.",
    "Trauner-Filmtipps der Buchseiten sind **nicht eingebaut** (von hier aus nicht prüfbar). Passen sie, sag Bescheid – dann baue ich sie als OPTIONAL ein.",
    "Abgabe: Der Plan sieht keine PDF-Abgabe vor. Soll es eine geben (z. B. am 30.11.), sag es – dann baue ich eine Abgabefolie und einen Ordner in LMS ein.",
]

AUF_EINEN_BLICK = [
    ["Stunde 1 · Vorrat bis frühe Staaten", "Landwirtschaft: Möglichkeiten und Probleme, kein Automatismus zum Staat · Ötzis Beil: Befund, Vermutung, Grenze; Metall braucht Rohstoff, Können, Austausch · Schrift als Verwaltung · Stadtstaat (Uruk) und Flächenkönigtum (Nil): ähnliche Aufgaben, verschiedene Form", "Mini-Whiteboard, Tafel, Karten"],
    ["Stunde 2 · Test, Hammurabi", "Rechtssammlung um 1750 v. Chr.: ordnet Konflikte (§ 53, 233), zeigt Ungleichheit (§ 196, 198, 199) · schriftlich ≠ gleiches Recht · Quelle königlicher Selbstdarstellung, Alltag unbekannt · nicht die erste Sammlung", "Paragrafenblatt (Papier)"],
    ["Stunde 3 · Athen, Rom, Prinzipat", "Athen: Volksversammlung der männlichen Bürger, Los und Wahl, Ausschluss von Frauen, Versklavten, Metöken · Rom: Konsuln, Senat, Tribunen, Oberschicht · Augustus: Einrichtungen bleiben, Macht (Heer, Provinzen, Befugnisse) beim Princeps · Zeitstrahl abschließen", "Skala im Raum, Tabelle"],
]

KAPITEL = [
 {"titel": "1 Landwirtschaft, Vorrat und Metall (Buch S. 25–32)",
  "text": ["**Neolithische Revolution:** Der Begriff geht auf Gordon Childe zurück und betont die Wirkung, nicht die Dauer. Landwirtschaft entstand in mehreren Regionen unabhängig (Vorderer Orient, China, Mittelamerika u. a.); Sesshaftigkeit und Nahrungsproduktion lagen nicht überall in derselben Reihenfolge. Für die Kadetten: »viele Generationen, regional verschieden«.",
           "**Gleichstellung (Buch S. 25, Tabelle »Gesellschaft«):** Die pauschale Aussage, gemeinsame Feldarbeit habe Frauen und Männer gleichgestellt, nicht übernehmen. Arbeitsteilung, Besitz und Einfluss unterschieden sich nach Region und Zeit; gemeinsame Arbeit beweist keine politische oder soziale Gleichstellung.",
           "**Metall:** Kupfer-, Bronze- und Eisenzeit sind regionale Orientierungsbegriffe. Bronze ist eine Gruppe von Kupferlegierungen (etwa 90 % Kupfer und 10 % Zinn ist ein Beispiel). Eisen wurde schon in der Antike durch Verhüttung und Schmieden verarbeitet.",
           "**Ötzi (Buch S. 30):** Die Ausrüstung erlaubt begrenzte Schlüsse. Ein Befund (Kupferklinge im Holzschaft) ist keine Deutung (»Anführer«). **Neu 2024:** Das Südtiroler Archäologiemuseum und die Universität Padua haben mehr als 50 Metallgegenstände mit Bleiisotopen und Verunreinigungen untersucht; das Beilkupfer stammt demnach aus der südlichen Toskana (Pressemeldung 1.3.2024, von mir gelesen). Das zeigt den Weg des Metalls, nicht den einer Person."],
  "nur": ["Buch S. 27–28 (Milchverträglichkeit) ist OPTIONAL: Milch wurde lange genutzt, bevor Laktasepersistenz häufig wurde (Evershed u. a. 2022, Nature) – modellgestützt, nicht als einfache Folge darstellen. Von mir nicht neu gelesen.",
          "Buch S. 31 (Grabbeigaben, drei feste Gruppen): als Hinweise auf Unterschiede lesen, nicht als gesicherte Sozialordnung (NHM Wien, Hallstatt – nur über Suchtext geprüft)."],
  "stolper": "»Revolution = über Nacht«, »Ötzi war der Chef«, »Metallzeiten gelten überall gleich«. Gegenmittel: Aufgabe 1 (Befund – Vermutung – Grenze), Grafik »Zeittafel«.",
  "bild": "img/beil.png"},
 {"titel": "2 Frühe Staaten: Stadtstaat und Flächenkönigtum (Buch S. 33–39)",
  "text": ["**Hochkultur:** gebräuchlicher Begriff für frühe städtische, sozial differenzierte Gesellschaften mit spezialisierten Einrichtungen. Er ist keine Rangstufe und keine Checkliste; nicht jedes Merkmal ist überall vorhanden. Die Tabelle S. 34 ist keine verlässliche weltweite Erstentstehungs-Chronologie.",
           "**Mesopotamien:** Stadtstaaten (z. B. Uruk) mit Umland; Austausch, Konkurrenz und Krieg; später größere Reiche. Frühe Schrift (Uruk, späte 4. Jt. v. Chr.) dokumentiert zunächst Wirtschaftsvorgänge – Mengen, Güter, Verteilung (Met Museum, nur Abstract geprüft). **Ägypten:** Königtum über ein langes Flusstal; hierarchische Ordnung; Religion hilft, Herrschaft zu begründen – braucht aber auch Verwaltung, Ressourcen und Durchsetzung.",
           "**Fluss ≠ Staat:** Wasserwirtschaft ist eine wichtige Organisationsaufgabe, aber kein zwingender Weg zur Alleinherrschaft; Handel, Konflikte, Religion und Machtbildung wirken mit.",
           "**Schrift:** entstand mehrfach, nicht geradlinig »vom Bild zur Alphabetschrift«; Hieroglyphen sind nicht bloß Bilder; Alphabetschrift ist kein Wertmaßstab."],
  "nur": ["Echnaton und »erster Monotheist« (Buch S. 36–37) ist ein strittiger Superlativ – nur als OPTIONALER Spezialfall. Buch S. 41–42 (Israeliten): biblische Erzählung, historische Rekonstruktion und heutige Ansprüche nicht gleichsetzen, nur OPTIONAL."],
  "stolper": "»Hochkultur = besser«, »großer Fluss = automatisch Zentralstaat«. Gegenmittel: Stopp-Frage 3, Aufgabe 3 d).",
  "bild": "img/karte.png"},
 {"titel": "3 Hammurabi (Buch S. 39–40)",
  "text": ["**Datierung und Gegenstand:** Hammurabi, König von Babylon im 18. Jh. v. Chr. Die Stele (um 1750 v. Chr., heute im Louvre) trägt 282 Entscheidungen; der Louvre beschreibt sie als Sammlung von Rechtsfällen (»case law«), nicht als modernes Gesetzbuch (von mir auf der Louvre-Seite gelesen). Typisch ist das Muster »Wenn …, dann …«.",
           "**Ältere Sammlungen:** u. a. Ur-Nammu (Ur) und Eshnunna sind bekannt (Bodleian-Leitfaden, nur Übersicht). Darum nicht »erstes Gesetz«.",
           "**Paragrafen der Arbeitsfassung (vereinfacht nach Buch S. 40):** § 53 Damm und Getreide · § 196 Auge des Bürgersohns → Auge · § 198 Auge eines Untergebenen → 1 Mine Silber · § 199 Auge des Knechts → halber Kaufpreis · § 233 Wand des Baumeisters. Eine Mine ist eine Gewichts- und Recheneinheit für Silber. Die Arbeitsfassung ist **sprachlich vereinfacht**; die Paragrafennummern und Aussagen wurden mit Buch S. 40 abgeglichen.",
           "**Quellenfragen:** Herrscherperspektive und Darstellung von Ordnung · was die Regeln zeigen (Konflikte, Ungleichheit, Eigentum) · was sie nicht zeigen (tatsächliche Anwendung im Alltag, Gerichtsverfahren, vollständiges Recht)."],
  "nur": ["Eine historische UN-Geschenkseite nennt die Sammlung »die älteste« – nicht übernommen, weil ältere Sammlungen dokumentiert sind."],
  "stolper": "»Hammurabi erfand das Recht«, »vor dem Gesetz alle gleich«. Gegenmittel: Aufgabe 4 c) und f), Aufgabe 10 (KI-Antwort prüfen).",
  "bild": None},
 {"titel": "4 Athen (Ergänzungsbuch S. 62–65)",
  "text": ["**Beteiligung:** In der behandelten klassischen Phase (vor allem 5. Jh. v. Chr.) entscheiden erwachsene männliche Bürger in der Volksversammlung. Frauen, Versklavte und Metöken sind ausgeschlossen. Der Rat (500) bereitet vor und wird gelost; viele Ämter (z. B. Archonten) werden gelost, die Strategen gewählt. Details der Ordnung veränderten sich – Kleisthenes um 508/507 v. Chr. ist nur ein Orientierungspunkt.",
           "**Vergleich mit Österreich:** parlamentarische Demokratie (Wahl von Vertretern, Gesetzgebung, Kontrolle der Regierung; Parlament Österreich, Seite »Parlament und Wahlen«). Auch heute sind Wahlrechte an Voraussetzungen gebunden (Staatsbürgerschaft, Wahlalter). Der Vergleich fragt nach Beteiligung, Ausschluss und Kontrolle – er setzt nicht gleich.",
           "**Quellenfrage:** Das Gemälde »Gefallenenrede des Perikles« im Ergänzungsbuch (S. 65) stammt von 1852 – eine spätere Darstellung, kein Augenzeugenbild."],
  "nur": ["Trauner S. 105–118 (Hellenen, Polis, Klassengesellschaft Athen) lagen nicht vor – nur Kapitelnavigation. Falls du die Seiten hast, schick sie; ich gleiche dann die Aussagen ab."],
  "stolper": "»In Athen durften alle abstimmen«, »alle Ämter wurden gewählt«. Gegenmittel: Aufgabe 5 b) und c), Stopp-Frage 3.",
  "bild": "img/athen.png"},
 {"titel": "5 Rom, Augustus und der Anschluss (Ergänzungsbuch S. 68–73)",
  "text": ["**Republik:** zwei Konsuln mit begrenzter Amtszeit, Senat (Gewicht einflussreicher Familien), Volksversammlungen, Volkstribunen (Einspruch). Keine moderne parlamentarische Demokratie: Vermögen, Herkunft und Verbindungen beeinflussen den Zugang; Frauen und Versklavte ausgeschlossen. Das Buchschema ist zeitgebunden – keine unveränderte Ordnung für die ganze Republik behaupten.",
           "**Augustus:** Octavian setzte sich nach Bürgerkriegen durch, 27 v. Chr. Name Augustus; Princeps (»Erster unter Gleichen«). Republikanische Einrichtungen bestehen weiter; entscheidende Machtmittel liegen bei ihm (Oberbefehl über das Heer, Statthalterschaft in wichtigen Provinzen, Befugnisse von Konsul und Volkstribun). Die Res gestae (Ergänzungsbuch S. 71, M3) sind **Selbstdarstellung**: nützlich als Beleg für das gewollte Bild, aber nicht als unabhängige Bewertung.",
           "**476 n. Chr.:** konventioneller Orientierungspunkt für das Ende Westroms; Ostrom besteht weiter. Politische, militärische und wirtschaftliche Faktoren wirken zusammen – keine pauschale Gegenwartsanalogie."],
  "nur": ["Britisches Museum (Augustus, Münze zur republikanischen Selbstdarstellung): nur als Hinweis geprüft, die Münzabbildung wurde nicht als Medium freigegeben. Heer und Gefolgschaft sind Faktoren römischer Macht, aber nicht die einzige Erklärung."],
  "stolper": "»Republik = Demokratie«, »Augustus stellte die Republik tatsächlich wieder her«, »476 endete das Römische Reich«. Gegenmittel: Aufgabe 6 und 7, Stopp-Frage 3.",
  "bild": "img/rom.png"},
]

RECHNEN = [
    "**Zeitrechnung (v. Chr.):** Von 2026 rückwärts: 1750 v. Chr. → vor ca. 3800 Jahren (2026 + 1750 = 3776) · 3300 v. Chr. (Ötzi) → vor ca. 5300 Jahren · rund 12 000 Jahre seit den Anfängen der Landwirtschaft · 27 v. Chr. → vor ca. 2050 Jahren.",
    "**Jahrhunderte:** Das 5. Jh. v. Chr. umfasst 500–401 v. Chr. (rückwärts zählen) · das 18. Jh. v. Chr. umfasst 1800–1701 v. Chr.",
    "**Mine:** Gewichts- und Recheneinheit für Silber – im Unterricht nicht umrechnen, nur als »Silbergewicht« erwähnen.",
]

FEHLVORSTELLUNGEN = [
    ["Revolution = plötzlich und überall gleich.", "Langer, regional verschiedener Wandel; mehrere Ursprünge.", "Stopp-Frage Teil 1, Aufgabe 2 c)."],
    ["Ötzi war Jäger oder Chef.", "Beruf und Rang sind aus dem Beil allein nicht ablesbar.", "Aufgabe 1 c)."],
    ["Hochkultur = bessere Menschen.", "Der Begriff beschreibt frühe städtische Gesellschaften; er wertet nicht.", "Stopp-Frage Teil 1."],
    ["Großer Fluss = automatisch Zentralstaat.", "Wasserwirtschaft ist eine Aufgabe unter mehreren Einflüssen.", "Aufgabe 3 d)."],
    ["Hammurabi schuf das erste Gesetz; alle waren gleich.", "Ältere Sammlungen; Rechtsfolgen hingen vom Stand ab.", "Aufgabe 4, Aufgabe 10."],
    ["Ein Text zeigt den ganzen Rechtsalltag.", "Er zeigt Ordnung und Darstellung; die Anwendung bleibt offen.", "Aufgabe 4 f)."],
    ["Alle Athener durften mitbestimmen; alle Ämter wurden gewählt.", "Nur erwachsene männliche Bürger; viele Ämter durch Los, Strategen durch Wahl.", "Aufgabe 5."],
    ["Republik = moderne Demokratie.", "Mehrere Ämter, aber starker Einfluss der Oberschicht.", "Aufgabe 7."],
    ["Augustus stellte die Republik wieder her.", "Einrichtungen blieben, die Macht lag beim Princeps; seine Aussage ist Quelle.", "Aufgabe 6."],
    ["476 endete das ganze Römische Reich.", "Orientierungspunkt für Westrom; Ostrom bestand weiter.", "Quiz-Frage 17."],
]

FRAGEN = [
    ("War Ötzi ein Anführer?", "Das wissen wir nicht. Das Beil zeigt Kupferverarbeitung und Austausch, belegt aber weder Beruf noch Rang. (Auch seine Ausrüstung lässt nur begrenzte Schlüsse zu.)"),
    ("Ist ein Staat eine Folge von Landwirtschaft?", "Nicht automatisch. Vorräte, Verteilung und Einfluss schaffen Möglichkeiten; Handel, Konflikte, Religion und örtliche Bedingungen wirken mit."),
    ("Warum wurde ein Auge gegen ein Auge gesetzt, aber ein Knecht nur mit Silber bezahlt?", "Die Rechtsfolge hing vom Stand ab: Der Knecht (versklavte Mensch) wurde als Eigentum behandelt, der Besitzer bekam Ausgleich. Das zeigt Ungleichheit, keine Gerechtigkeit nach heutigen Maßstäben."),
    ("War Hammurabis Sammlung wirklich das älteste Gesetz?", "Nein. Ältere Sammlungen sind bekannt (z. B. Ur-Nammu). Hammurabis Stele ist besonders gut erhalten und bekannt."),
    ("Warum durften Frauen in Athen nicht mitbestimmen?", "Das Bürgerrecht war an männliche Erwachsene gebunden. Wie das begründet wurde, ist nicht in einem Satz zu erklären; für den Unterricht reicht: Beteiligung bedeutete damals nicht gleiche Rechte für alle Einwohner."),
    ("War Athen dann überhaupt eine Demokratie?", "Für die Bürger ja – mit direkter Beteiligung. Nach heutigen Maßstäben war die Gleichberechtigung stark begrenzt. Beides stimmt."),
    ("Warum nannte sich Augustus nicht König?", "Der Königstitel war in Rom politisch belastet. Er nannte sich Princeps und ließ die Einrichtungen bestehen – die Macht lag trotzdem bei ihm. (Beleg: Aufgabe 6.)"),
    ("Was hat das mit dem Bundesheer zu tun?", "Heer und Gefolgschaft waren ein Machtfaktor des Augustus; Vorratshaltung, Transport und Verwaltung sind logistische Aufgaben. Wichtig: Antike Abgaben- und Zwangssysteme sind etwas anderes als heutige rechtsgebundene Institutionen."),
    ("Warum prüfen wir Quellen, wenn sie vom Herrscher selbst stammen?", "Weil sie zeigen, wie er gesehen werden wollte – nicht unbedingt, was geschah. Man vergleicht mit anderen Quellen und mit den tatsächlichen Machtverhältnissen."),
]

VIDEO_NOTIZ = {
    "oetzi": "Pressemeldung des Südtiroler Archäologiemuseums, 1.3.2024 (PDF, von mir gelesen): über 50 Metallobjekte, Bleiisotope und Verunreinigungen, Beilkupfer aus der südlichen Toskana. In der Theorie als Lesetipp verlinkt (Zusatzaufgabe 11). Link über Suche gefunden und geöffnet, in der Klasse noch nicht ausprobiert.",
    "buchfilme": "Trauner-Filmtipps auf den Buchseiten (z. B. S. 23): von hier aus nicht erreichbar – Ziel, Länge und Verfügbarkeit bitte selbst prüfen; dann als OPTIONAL einbauen. Kein Podcast eingeplant (Jahresplan: u. a. »Die Erfindung des Ackerbaus«, »4000 v. Chr. – Die Hochkultur der Sumerer …«): Titel gelesen, nicht abgehört, keine Links.",
}

AUSBLICK = ("Nächste Einheit laut Jahresplan: Frühe Neuzeit um 1500 (Buch S. 61 ff.): Wissen, Religion, Wirtschaft und Macht verändern sich; antike Texte und Vorbilder werden neu gedeutet – keine lückenlose Linie von Athen zur heutigen Demokratie. "
            "Anknüpfung: Quellenkritik (Aufgabe 6), Beteiligung und Kontrolle (Aufgabe 7).")

BILDER = [
    ("eigene Zeichnung (Typ des Ötzi-Beils)", "–", "selbst gezeichnet", "img/beil.png (Einstieg, Aufgabe 1)", "Befund, Vermutung, Grenze – kein Foto des Fundes"),
    ("eigene Zeichnung", "–", "selbst gezeichnet", "img/kette.png (Teil 1, Schrift)", "Verwaltung: Ernte – Lager – Liste – Verteilung"),
    ("eigene Karte, Schema", "Nil, Euphrat, Tigris", "selbst gezeichnet", "img/karte.png (Teil 1, Aufgabe 3)", "Orientierung; nicht maßstabsgerecht"),
    ("eigenes Schaubild", "Athen", "selbst gezeichnet", "img/athen.png (Teil 3, Aufgabe 5)", "nicht das Schaubild des Ergänzungsbuchs"),
    ("eigenes Schaubild", "Republik und Prinzipat", "selbst gezeichnet", "img/rom.png (Teil 3, Aufgabe 6/7)", "vereinfacht; Ordnung veränderte sich"),
    ("eigene Zeittafel", "sechs Zeitbereiche", "selbst gezeichnet", "img/zeitstrahl.png (Teil 1, Aufgabe 8)", "Bereiche nicht gleich lang"),
    ("Trauner PBGW 3 und Ergänzungsbuch (Screenshots im Paket)", "–", "nicht verwendet (nur Verweise)", "–", "keine Buchbilder auf öffentlichen Seiten und in den PPPs"),
]

QUELLEN = [
    "**Grundlage:** ChatGPT-Auftrag »26-27-3BK-Meilenst-ChatGPT-v2.md« (29.10.2026) mit Paket (Screenshots Trauner S. 23–44, Ergänzungsbuch S. 58–73, Jahresplan v14, Regelwerk, Muster) – Ablauf, Texte T1–T6, Aufgaben A1–A8 und Quizpool übernommen, sprachlich vereinfacht, nach dem Regelwerk (14. Fassung) umgebaut und nachgeprüft (Prüfbericht).",
    "**Buchzuordnung:** Hammurabi-Paragrafen (§ 53, 196, 198, 199, 233) mit Trauner S. 40 abgeglichen; Augustus M3 (Ergänzungsbuch S. 71) und Athen-Schaubild (S. 64) bestätigt. Trauner S. 105–118 lagen nicht vor.",
    "**Selbst geprüft (30.10.2026):** Südtiroler Archäologiemuseum, Pressemeldung 1.3.2024 (PDF) – Ötzis Beilkupfer, über 50 Objekte, Bleiisotope; Louvre, »The Code of Hammurabi« – Stele um 1750 v. Chr., Rechtsfälle (»case law«), 282 Entscheidungen.",
    "**Aus der Übergabe übernommen, von mir nicht neu geprüft:** Bodleian Libraries (ältere Rechtssammlungen), Universität Graz (Athen und Rom), British Museum (Augustus), NHM Wien (Hallstatt), Evershed u. a. 2022 (Nature), Parlament Österreich (Demokratie), Met Museum (Ursprünge der Schrift).",
    "**Jahresplan v14:** E3–E5 (K01, K02, K04, K05, K06, K08, N01, N02, P3, P4, SDG 2; keine GLV-Codes). Teststoff für den 23.11. liegt bei dir.",
]
