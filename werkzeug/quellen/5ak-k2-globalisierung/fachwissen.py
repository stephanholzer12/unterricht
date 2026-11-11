"""Fachwissen für die Lehrkraft (nur für Stephan): Lehrer-Infos und Lösungsmappe K2.1 Globalisierung (5AK IWK, Buch S. 42–51).
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle). Stand 11.11.2026."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan v14, E3 = 2 Stunden (Fr 13.11. und Fr 20.11.). Buch Trauner IWK Teil II, S. 42–51 »Die Welt ohne Grenzen: Globalisierung«. Institutionen (S. 52–63) folgen als eigene Einheit ab Fr 27.11., Auswirkungen (S. 64–77) danach."),
    ("Stunde 2: ", "Zuerst der angekündigte Test (Dauer 20 min nur angenommen, Stoff und Nummer unbekannt – nichts ergänzt), danach etwa 22 min Unterricht."),
    ("Abweichungen vom Buch: ", "Keine Buchbilder oder Buchtexte auf Seiten und Folien (öffentlich). Aufgaben sind in eigenen Worten umgesetzt, Grafiken selbst gezeichnet. Kein Versuch, kein CLIL, kein Kahoot, keine Hausübung."),
    ("Lehraufgaben: ", "Die Lehraufgaben der E3 stehen im Jahresplan IWK_Jahresplan_5Jg_v14 und sind verbindlich – bitte dort gegen die Aufgaben 1–3 gegenprüfen; ich habe sie nicht neu formuliert."),
]

THEMEN = {1: "Beginn und Antriebskräfte (S. 42–47)", 2: "Digital Divide und Statement-Ampel (S. 48–51)"}


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, _ = PL.aufgaben_der(st)
        z = f"Lesen {PL.minuten(st, ['lesen'])} · Erklären {PL.minuten(st, ['erkl'])} · Aufgaben {PL.minuten(st, ['a'])} · Bespr. {PL.minuten(st, ['bespr'])} · Reserve {PL.minuten(st, ['reserve'])}"
        if PL.minuten(st, ["test"]): z = f"Test {PL.minuten(st, ['test'])} · " + z
        rows.append([f"{st['std']} · {st['datum']}", THEMEN[st["std"]], "– (kein Versuch)", PL.bereich(nrs), z, st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}

MATERIAL = {1: "Beamer mit TH-Unterricht · Tafel für Begriffe und Vermutung · keine Papiere nötig · Zeitstrahl liegt als Bild in der Theorie",
            2: "Test (bestehend) · Beamer · Platz zum Aufstellen in drei Zonen (stimmt · unklar · stimmt nicht), Zettel oder Schilder nach Wunsch",
            }


def _karten():
    out = []
    k = I.KLASSEN[0]
    for st in PL.PLAN[k]:
        t, schritte = 0, []
        for name, m, oh, art in st["phasen"]:
            schritte.append(f"Min {t}–{t + m}: {name}" + (" (ohne Handy)" if oh and art not in ("org", "reserve", "test") else "")); t += m
        schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
        ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0].split(":")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve", "org", "test")))
        out.append((f"5AK · Stunde {st['std']} · {st['datum']} · {THEMEN[st['std']]}", schritte, MATERIAL[st["std"]], ohne))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Einheit einblenden vor der ersten Stunde (Fr 13.11.): GitHub → Actions → »Einheit ein-/ausblenden« → 5ak-iwk/k2-1-globalisierung → einblenden. Die Direktlinks und QR-Codes funktionieren auch versteckt.",
    "Zölle (nur Aussage 4 der Ampel und Zusatz 5): Meldung vom 09.11.2026 (China, 24 % ausgesetzt, 10 % bleiben) vor dem 20.11. neu prüfen. Es wurde auch ein Treffen Trump–Xi am Rand des APEC-Gipfels angekündigt; Ergebnis ungeprüft.",
    "Stunde 2: Testdauer bestätigen (hier 20 min angenommen). Wird der Test länger, zuerst Ampel auf eine Aussage kürzen, dann Weißt du noch streichen.",
    "Stunde 2: Statement-Ampel vorbereiten – Zonen im Raum festlegen; Aussagen 1 und 4 (Buch S. 51) vorlesen, keine Auflösung, keine Note.",
    "Quiz-Check (6 Fragen) liegt als QR auf der Abgabe-Folie; das vollständige Quiz (16 Fragen) ist freiwillig.",
    "Medien: Es gibt keine Pflichtvideos oder Podcasts. Die Ö1-Beiträge aus dem Jahresplan (Zölle; Globalisierung um das Jahr 1000) habe ich nicht angehört und nicht eingebaut – nur freigeben, wenn du sie vorher hörst.",
]

AUF_EINEN_BLICK = [
    ["Stunde 1 · Beginn", "Kein einzelner Beginn: 1492 Kolumbus · 1844 Telegraf · 1944 IWF/Weltbank (Bretton Woods) · 1980er Technik · Internet; je nach Kriterium. 1944 − 1492 = 452 Jahre.", "Handzeichen + Tafel"],
    ["Stunde 1 · Antriebskräfte", "Sechs Kräfte (Buch S. 45–47): Informationsrevolution, Transport, Marktwirtschaft/Liberalisierung, Postfordismus/Just-in-time, transnationale Konzerne, Normen. Liberalisierung = Handelshemmnisse abbauen, Märkte öffnen.", "Handy + Tafel"],
    ["Stunde 2 · Digital Divide", "ITU 2025: 94 % (hohes) vs. 23 % (niedriges Einkommen) = 71 Prozentpunkte; Stadt 85 % vs. Land 58 % = 27; rund 2,2 Mrd. offline. Buch: rund 32 % – Quellen zählen verschieden.", "Handy"],
    ["Stunde 2 · Ampel", "Quellenkritik mit den vier Fragen an Aussagen aus Buch S. 51; keine Auflösung, keine Note.", "Bewegung im Raum"],
]

KAPITEL = [
 {"titel": "1 Wann begann die Globalisierung? (Buch S. 42–44)",
  "text": ["Es gibt keine einheitliche Definition und keine einzelne Geburtsstunde. Das Buch nennt mehrere Standpunkte: Entdeckungen (Kolumbus 1492), Handelsliberalismus und Industrialisierung, technische Neuerungen wie den Telegrafen (1844), Institutionen nach dem Krieg (IWF und Weltbank 1944, WTO 1995) und die Technik der 1980er/1990er mit dem Internet. Entscheidend ist das Kriterium, nicht die Jahreszahl.",
           "Didaktik: Die Kadetten tippen zuerst allein (»Was glaubst du?«), lesen dann, und die Seite vergleicht am Ende ihre Vermutung mit dem Buch. Keine Wertung der Vermutung."],
  "nur": ["Quellenkritik-Impuls China (Gemeinsam): Gesichert ist, dass die staatlichen Flottenfahrten unter Zheng He (1405–1433) endeten (EBSCO Research Starter, geprüft 11.11.2026). Die Überschrift »zerstörte seine Marine, weil die Herrscher Angst vor Freihandel hatten« ist eine Deutung; Quellen nennen eher Kosten und innenpolitischen Streit, unter Fachleuten diskutiert. Die Szenarien (»Wäre China weitergesegelt?«) sind ein Gedankenspiel, nicht Fakt."],
  "stolper": "Einen einzigen Beginn behaupten; das Gedankenspiel als Tatsache nehmen."},
 {"titel": "2 Sechs Antriebskräfte und Liberalisierung (Buch S. 45–47)",
  "text": ["Informationsrevolution, Innovationen im Transport (Container, Großraumflugzeuge), Marktwirtschaft und Liberalisierung, transnationale Konzerne, Normen und Standards (Buch nennt auch Postfordismus und Just-in-time). Liberalisierung = Abbau von Handelshemmnissen und Öffnung der Märkte für Güter, Dienstleistungen und Kapital; dazu gehören Deregulierung und Privatisierung.",
           "Neoliberalismus (S. 46–47): Befürworter sehen Wachstum und Effizienz, Kritiker Ungleichheit und Machtkonzentration. Die Hayek-Passage im Buch dient nur als Diskussionsgrundlage – eine Auflösung gibt es nicht."],
  "nur": ["Verbindung zu deiner PPP vom Vorjahr: Beispiele zu Konzernen und Transport lassen sich mit Bundesheer-Bezug ergänzen (Ausrüstung, Lieferketten) – ohne Behauptung zu einer konkreten Beschaffung."],
  "stolper": "Liberalisierung mit Globalisierung gleichsetzen; Antriebskräfte als Ursachenkette statt als Zusammenspiel."},
 {"titel": "3 Digitalisierung und Digital Divide (Buch S. 48)",
  "text": ["ITU »Facts and Figures 2025« (17.11.2025): rund 6 Mrd. Menschen nutzen das Internet, 2,2 Mrd. nicht. Hohes Einkommen 94 %, niedriges 23 %; Stadt 85 %, Land 58 %; Männer 77 %, Frauen 71 %. Das Buch nennt für 2025 rund 32 % ohne Internet; die ITU kommt auf etwa ein Viertel. Beide Aussagen zeigen in dieselbe Richtung, zählen aber verschieden (Jahr, Messweise, Definition von »Nutzer«).",
           "Corona wirkte als Beschleuniger (Homeoffice, Distance Learning) und machte die Ungleichheit sichtbar."],
  "nur": ["Beispielländer aus deiner PPP (Stand 2024) habe ich nicht geprüft und nicht übernommen. Wenn du sie zeigen willst, vorher in ITU DataHub nachsehen."],
  "stolper": "Eine der beiden Zahlen als »falsch« abtun; Zahlen ohne Quelle und Jahr nennen."},
 {"titel": "4 Statement-Ampel (Buch S. 51) und der Handelskrieg",
  "text": ["Buch S. 51 »Ziele erreicht?« bietet Aussagen als Diskussionsanlass. Für zwei Aussagen (1: Bereicherung für Europa; 4: Schäden des US-Handelskriegs) gilt: kein Ergebnis vorgeben. Die Kadetten prüfen mit den vier Fragen: Wer sagt das? Woher weiß er das? Was hat er davon? Was sagen andere Quellen?",
           "Zu Aussage 4 (Stand 09.11.2026): Berliner Zeitung (Anika Schlünz, nach Xinhua, Reuters, dpa): China setzt den Zusatzzoll von 24 % auf US-Waren für weitere zwei Monate aus, 10 % bleiben. US Supreme Court 20.02.2026: auf IEEPA gestützte Zölle für rechtswidrig erklärt (WKO, Seite vom 23.10.2026). Das ist keine Entwarnung, sondern ein Zwischenstand."],
  "nur": ["Moderation: neutral bleiben, alle Zonen gleich ernst nehmen, Wechsel in einem Satz begründen lassen. Parteipolitische Auflösung vermeiden; ein Treffen Trump–Xi am APEC-Rand wurde angekündigt, das Ergebnis ist ungeprüft."],
  "stolper": "Aussagen parteipolitisch auflösen; eine Zeitungsmeldung als endgültigen Stand nehmen (nur eine Quelle geprüft)."},
]

RECHNEN = ["Aufgabe 1: 1944 − 1492 = 452 Jahre.",
           "Aufgabe 3: 94 − 23 = 71 Prozentpunkte; 85 − 58 = 27 Prozentpunkte. Prozentpunkte, nicht Prozent: Unterschied zweier Prozentwerte.",
           "Zusatz 5: 799 × 1,45 = 1 158,55 → 1 159 US-Dollar Zoll; Summe 1 957,55 → 1 958 (gerundet auf ganze Dollar, weil Komma und Punkt sonst Fehler verursachen)."]

FEHLVORSTELLUNGEN = [
    ["»Die Globalisierung begann mit dem Internet.«", "Je nach Kriterium früher (1492, 1844, 1944); das Internet verstärkt sie.", "Aufgabe 1, Zeitstrahl"],
    ["»China hat seine Flotte zerstört, weil …« (als Fakt)", "Gesichert ist nur das Ende der Fahrten; Gründe sind Deutung.", "Gemeinsam-Impuls, vier Fragen"],
    ["»Liberalisierung = Globalisierung.«", "Liberalisierung ist nur eine von sechs Antriebskräften.", "Aufgabe 2"],
    ["»32 % und 2,2 Mrd. widersprechen sich.«", "Verschiedene Quellen, Jahre, Definitionen.", "Aufgabe 3 d)"],
    ["»Prozentpunkte = Prozent.«", "Differenz zweier Anteile.", "Aufgabe 3 a), b)"],
    ["»Zoll 2025 = Zoll heute.«", "Rechtslage hat sich geändert (Supreme Court 20.02.2026, China-Pause 09.11.2026).", "Zusatz 5"],
]

FRAGEN = [("Und wann hat sie denn nun wirklich begonnen?", "Es gibt keine richtige Jahreszahl. Wer 1492 nennt, meint Entdeckungen und Handel über Kontinente; wer 1944 nennt, meint Institutionen; wer die 1980er nennt, meint Technik und Tempo. Das Kriterium zählt."),
          ("Ist die Zeitungsmeldung zu den Zöllen sicher?", "Nur eine geprüfte Quelle (Berliner Zeitung, nach Agenturen). Der Stand ändert sich; vor dem 20.11. neu prüfen und im Unterricht als »Stand 09.11.2026« nennen."),
          ("Warum nennt das Buch 32 %, die ITU etwa ein Viertel?", "Andere Quelle und andere Zählweise; beide zeigen, dass ein großer Teil der Welt offline ist. Quelle und Jahr nennen."),
          ("Warum bekommen wir keine Note für die Ampel?", "Es ist eine Übung im Prüfen und Begründen; wer die Zone wechselt, begründet es in einem Satz.")]

VIDEO_NOTIZ = {"keine": "Keine Pflichtvideos. Optionale Kandidaten aus dem Jahresplan (E3): Ö1 Dimensionen »Zölle: Regulierungsinstrument oder Konfliktpotenzial für den Welthandel?« (24 min, 2025) und radioWissen »Globalisierung um das Jahr 1000«. Abspielbarkeit und Inhalt nicht geprüft – nur nach eigenem Anhören einsetzen, mit drei Hörfragen vorab."}

AUSBLICK = ("Fr 27.11.: Institutionen der Globalisierung (Buch S. 52–63: WTO, IWF, Weltbank) als eigene Einheit; danach Auswirkungen (S. 64–77). "
            "Querverweis: Der Lieferkettenfall in TÖW E6 ist damit hier nicht doppelt nötig.")

QUELLEN = [
    "Schulbuch IWK (Trauner), Teil II, S. 42–51 (Screenshots von Stephan, 11.11.2026) und seine PPP »Globalisierung – wann begann sie?« (Vorjahr). Nichts davon liegt auf den öffentlichen Seiten.",
    "ITU, Facts and Figures 2025 (17.11.2025): 94 %, 23 %, 85 %, 58 %, 77 %, 71 %, 2,2 Mrd. offline.",
    "Berliner Zeitung, 09.11.2026 (Anika Schlünz, nach Xinhua, Reuters, dpa): China setzt den Zusatzzoll von 24 % für zwei Monate aus, 10 % bleiben. Eine zweite Quelle (Xinhua, ms-aktuell) war nicht abrufbar.",
    "WKO (Seite vom 23.10.2026): Urteil des US Supreme Court vom 20.02.2026 zu IEEPA-Zöllen.",
    "EBSCO Research Starter »Zheng He's Naval Expeditions« (geprüft 11.11.2026): Flottenfahrten 1405–1433.",
    "Nicht geprüft und nicht eingebaut: Ö1/radioWissen-Beiträge aus dem Jahresplan, Beispielländer der Vorjahres-PPP (Stand 2024), Ergebnis des APEC-Treffens Trump–Xi.",
]
