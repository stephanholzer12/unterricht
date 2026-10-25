"""Fachwissen für die Lehrkraft (nur für Stephan): TH-Fachwissen, VS-Fachwissen und Lösungsmappe K2.1–2.3 Schwingungen und Wellen.
Stundenvorschlag und Stundenkarten werden aus plan.py erzeugt (eine Quelle für Fahrplan, PPP, Word)."""
import inhalt as I
import plan as PL

LEHRPLAN = [
    ("Einheit: ", "Jahresplan E6 Schwingungen (2 Std., Buch S. 48–53) + E7 Wellen (2 Std., S. 54–57) + E8 Elektromagnetisches Spektrum (2 Std., S. 58–59) = 6 Std. · "
                  "hier: 4AK 5 Termine, 4BK 4 Termine + optional Mi 18.11.; jede Stunde 50 min, davon ca. 3 min Klassenbuch/Anwesenheit; Test bzw. Referat je 20 min → für das Thema bleiben 4AK ca. 195 min, 4BK ca. 168 min."),
    ("K03 ", "die wichtigsten Größen zur Beschreibung von Schwingungen und Wellen benennen und dazu passende Experimente durchführen → A1–A9, K2.1-V1, K2.1-V2, K2.2-V1, K2.2-V2"),
    ("K04 ", "Überblick über die Bereiche des elektromagnetischen Spektrums; Wirkung und Bedeutung in Technik und Natur erklären → A10–A13, Teil 5"),
    ("K05 ", "mathematische Verfahren zur Lösung physikalischer Problemstellungen anwenden → A1, A3, A7, A8, A11 (Zusatz A14–A16)"),
    ("N01 · N04 · N02/N05/N07 ", "Beobachten, mit Größen beschreiben, darstellen · Untersuchungen planen und auswerten (nur eine Variable ändern) · Technik/Natur verstehen, Nutzen und Risiko beurteilen"),
    ("P7 · P8 · SDG 3 · GLV 2 · GLV 4 ", "KI-Antwort prüfen (A12), Forschungskarte (A17) · Gesundheit: UV-Schutz (A13) · Informationsresilienz: Behauptung vs. Beleg · Krisenfähigkeit: Funk, UV-Schutz im Einsatz"),
    ("Schulprofil: ", "Gleichschritt-Verbot auf Brücken, Stoßdämpfer im Gelände, Truppenfunk (UKW), Radar, Wärmebild, Sonar (Marine) · Sport: Schaukel, La-Ola, Kadetten-Welle"),
    ("Buchabdeckung: ", "Pflichtkern: Schwingungsgrößen, Fadenpendel, Dämpfung, Resonanz, Quer-/Längswelle, v = λ · f, Überlagerung, stehende Welle, Huygens, EM-Spektrum mit Schutz. "
                        "Nur als Begriff bzw. Zusatz: harmonische Schwingung, Phase (über Gleich-/Gegentakt in A16), Federpendel (A14). Bewusst vertagt: Schwebung (S. 51), lineare/Flächen-/Raumwellen (S. 55) – passt zu Akustik E9. "
                        "Für A16 vorher klären, ob die Kadetten Sinuskurven gleicher Periode zeichnen können – sonst ein vorbereitetes Achsenraster (Karopapier, 1 cm = 2 Kästchen) austeilen."),
    ("Abweichung: ", "Stunden je Klasse verschieden (Fahrplan je Klasse); Gliederung nach Teilen statt Stunden; V4.12 Federpendel/Stimmgabeln nicht durchgeführt (Federpendel nicht im Inventar; laut Stephan nur eine Stimmgabel und zwei Resonanzkästen – Mitschwingen zweier Stimmgabeln nicht möglich; K2.1-V2 ist eine Alternative, kein Ersatz), "
                     "V4.13 Wellenwanne durch Simulation ersetzt (Wellenwanne nicht im Inventar), V4.14–V4.16 nicht eingeplant (Zeit, Geräte). Kein CLIL."),
]


def _stundenvorschlag(k):
    rows = []
    for st in PL.PLAN[k]:
        nrs, zus = PL.aufgaben_der(st)
        teile = " + ".join(f"Teil {t}" for t in st["teile"])
        extra = [p[0] for p in st["phasen"] if p[3] in ("test", "ref")]
        vs = [p[0] for p in st["phasen"] if p[3].startswith("v:")]
        rows.append([f"{st['std']} · {st['datum']}", " · ".join([e.split(" inkl.")[0] for e in extra] + [teile]), " · ".join(v.split(" (inkl.")[0] + f" {m} min" for v, m in
                     [(p[0], p[1]) for p in st["phasen"] if p[3].startswith("v:")]) or "–",
                     PL.bereich(nrs) + (" · Zusatz " + PL.bereich(zus) if zus else ""),
                     f"Reserve {PL.minuten(st, ['reserve'])} · Bespr. {PL.minuten(st, ['bespr'])}", st["methode"]])
    return rows


STUNDENVORSCHLAG = {k: _stundenvorschlag(k) for k in PL.PLAN}
STUNDENVORSCHLAG["4BK"].append(["opt. · Mi 18.11.", "Vertiefung", "–", "Zusatz 14–17", "Reserve 6 · Bespr. 6", PL.ZUSATZTERMIN_4BK["methode"]])

MATERIAL = {1: "Pendel-Aufbau (Stativ mit Querstab, Schnur, 100-g-Stück), Bandmaß, Handys als Stoppuhr · Schaukel-Folie",
            2: "Schnur mit Gewicht (aus V1) · Partnerkarten am Beamer",
            3: "3 m gelbe Schnur + Büroklammer, Platz für 10 Kadetten in einer Reihe",
            4: "Beamer mit PhET »Welleninterferenz« · Hefte für Skizzen",
            5: "keine Strahlungsquelle · Mini-Whiteboards oder Heft für A12/A13"}


def _karten():
    out = []
    for k in PL.PLAN:
        for st in PL.PLAN[k]:
            schritte = [f"{name} ({m} min)" for name, m, oh, art in st["phasen"]]
            if (k, st["std"]) in PL.KNAPP: schritte.append("Wenn die Zeit knapp wird – " + PL.KNAPP[(k, st["std"])])
            mat = " · ".join(MATERIAL[t] for t in st["teile"])
            ohne = ", ".join(dict.fromkeys(p[0].split(" (")[0] for p in st["phasen"] if p[2] and p[3] not in ("reserve",)))
            out.append((f"{k} · Stunde {st['std']} · {st['datum']} · " + " + ".join(f"Teil {t}" for t in st["teile"]), schritte, mat, ohne))
    z = PL.ZUSATZTERMIN_4BK
    out.append(("4BK · optional · Mi 18.11. · Vertiefung", [f"{n} ({m} min)" for n, m, o, a in z["phasen"]], "keine Geräte", "Wiederholung, Zusatz 16 mit der Hand"))
    return out


STUNDENKARTEN = _karten()

CHECKLISTE = [
    "Bis spätestens 03.11.: Vorversuch K2.1-V1 – Stativ (#179, #141, #143, #29) über der Tischkante aufbauen, gelbe Schnur #57 am Querstab-Ende festknoten und mit Klebeband sichern (oder Universalklemme #160 testen – #140 ist für 10–25 mm und hält die Schnur kaum), 100-g-Stück aus dem Gewichtssatz #59 anbinden (hält der Knoten? hat das Stück einen Griffknopf?), je zwei Probeläufe bei 0,40 m und 0,90 m stoppen.",
    "Schnur mit zwei Klebeband-Fähnchen markieren: 0,40 m und 0,90 m vom Aufhängepunkt bis zur Mitte des Gewichts (Umstellen ca. 2 min: Gewicht stützen, Knoten lösen, nachlassen, neu verknoten – nie nur Klebeband).",
    "2–3 schwere Bücher für den Stativfuß bereitlegen; Pendel vorne am Lehrertisch, Schwingung quer zur Klasse; links und rechts in Schwingungsrichtung je ca. 1,5 m frei, die Klasse sitzt davor – Sichtlinie von hinten prüfen.",
    "K2.1-V2 einmal üben: Pendel an der Schnur (0,40 m) mit ca. 1 cm Handweg im eigenen Takt (ca. 0,8 Hz) aufschaukeln; Abbruch bei ca. 20 cm Ausschlag.",
    "K2.2-V1: 3 m Schnur abmessen, Büroklammer bereit; ausprobieren, bei welcher (lockeren) Spannung der Puls gut sichtbar ist. Platz für 10 Kadetten in einer Reihe freiräumen.",
    "Am Lehrer-PC vorab öffnen: PhET »Pendel-Labor«, »Welle an einem Seil«, »Welleninterferenz« (Deutsch, Start prüfen) und die drei Buch-Filmtipps (freigegeben, einmal anspielen: laufen sie am Schul-PC?).",
    "4AK Mi 11.11.: Referat EKG/MRT (20 min) einplanen – Inhalte werden nicht vorausgesetzt (4BK hört es nicht).",
    "Partnerkarten (Aufgabe 5) am Beamer bereit: Folie »Partnercheck-Karten« in der TH-PPP.",
    "Einheit auf der Klassenseite einblenden, wenn es losgeht (GitHub → Actions → »Einheit ein-/ausblenden« → 4ab-nawi/k2-1-wellen → einblenden). QR-Codes auf der Folie »Dein Lernpfad«.",
]

AUF_EINEN_BLICK = [
    ["Teil 1 · 4AK+4BK Std. 1", "Schwingung um eine Gleichgewichtslage; A, T, f = 1/T. Fadenpendel: T hängt von der Länge ab, nicht von der Masse (Versuch V1).", MATERIAL[1]],
    ["Teil 2 · 4AK Std. 2 · 4BK Std. 2", "Dämpfung gibt Energie an die Umgebung ab; Feder ≠ Dämpfer. Resonanz bei Anregung im Takt der Eigenfrequenz, begrenzt durch Dämpfung.", MATERIAL[2]],
    ["Teil 3 · 4AK Std. 3 · 4BK Std. 2", "Welle = weitergegebene Störung; Teilchen bleiben am Ort. Quer/längs. v = λ · f; Achse lesen: x → λ, t → T.", MATERIAL[3]],
    ["Teil 4 · 4AK Std. 4 · 4BK Std. 4", "Überlagerung: Auslenkungen mit Vorzeichen addieren; stehende Welle (Knoten λ/2); Huygens: Elementarwellen, Einhüllende, Beugung.", MATERIAL[4]],
    ["Teil 5 · 4AK Std. 5 · 4BK Std. 3", "EM-Wellen ohne Medium, c = λ · f; Spektrum Radio–Gamma; ionisierend: Röntgen, Gamma; Risiko = Art + Stärke + Dauer.", MATERIAL[5]],
]

KAPITEL = [
 {"titel": "1 Schwingungen messen, Pendel verstehen (Buch S. 48–50)",
  "text": ["**Grundidee:** Eine mechanische Schwingung braucht eine Gleichgewichtslage, eine rücktreibende Kraft (Schwerkraft-Komponente beim Pendel, Federkraft) und Trägheit. Ohne Trägheit bliebe der Körper in der Mitte stehen; ohne rücktreibende Kraft liefe er davon.",
           "**Zählen:** Ein Nulldurchgang kommt zweimal pro Periode vor (je Richtung einmal). Darum im Versuch festlegen: Start beim Durchgang links → rechts = »Null«, dann jeden weiteren Durchgang in dieselbe Richtung zählen; bei »Zehn« stoppen. Wer jeden Durchgang zählt, erhält T halb so groß – häufigster Messfehler.",
           "**Warum die Masse beim Fadenpendel herausfällt:** Rücktreibende Kraft F = m·g·sin φ und Trägheit m wachsen beide mit m – sie kürzen sich. Beim Federpendel hängt die rücktreibende Kraft nur von der Feder ab (F = −k·y), die Trägheit aber von m – darum T = 2π·√(m/k).",
           "**Energiebrücke:** Am Umkehrpunkt ist die Geschwindigkeit null (nur Lageenergie), in der Gleichgewichtslage am größten (nur Bewegungsenergie). Für die Kadetten reicht die qualitative Aussage."],
  "nur": ["Kleinwinkelnäherung sin φ ≈ φ (Bogenmaß): Bei 10° ist T um ca. 0,2 % länger, bei 30° um ca. 1,7 %, bei 60° um ca. 7 %. Im Versuch (≤ 10°) geht das völlig in der Reaktionszeit unter.",
          "Realer Pendelkörper = physikalisches Pendel: Länge bis zum Schwerpunkt, dazu ein kleiner Beitrag vom Trägheitsmoment des Körpers. Falls das 100-g-Stück ein kompakter Zylinder ist (Form im Inventar nicht dokumentiert, z. B. ca. 2,5 cm Durchmesser), ist das bei l = 0,40 m vernachlässigbar (< 0,5 %)."],
  "stolper": "»Schwerer schwingt schneller« – genau die Schaukelfrage im Einstieg. Gegenprobe im Versuch (falls Zeit): dasselbe Pendel mit 50-g- statt 100-g-Stück – gleiche Zeit.",
  "bild": "img/g_pendel.png"},
 {"titel": "2 Dämpfung, erzwungene Schwingung, Resonanz (Buch S. 51–53)",
  "text": ["**Dämpfung:** Reibung und Luftwiderstand wandeln Schwingungsenergie in innere Energie um; die Amplitude sinkt. Bei schwacher Dämpfung bleibt die Frequenz fast gleich; bei sehr starker Dämpfung schwingt das System gar nicht mehr, sondern kriecht zurück (Fahrzeug: deutlich gedämpft, aber unter diesem Grenzfall – es schwingt nur kurz nach).",
           "**Feder und Dämpfer im Fahrzeug:** Die Feder speichert Energie kurzzeitig und gibt sie zurück; der hydraulische Dämpfer drückt Öl durch enge Ventile und wandelt die Energie in Wärme um. Defekte Dämpfer → Fahrzeug schaukelt nach, Räder verlieren Bodenkontakt (Bremsweg!).",
           "**Resonanz:** Bei periodischer Anregung schwingt das System im Takt der Anregung. Liegt die Erregerfrequenz nahe der Eigenfrequenz, wird bei jedem Zyklus Energie »phasenrichtig« zugeführt – die Amplitude wächst, bis Dämpfung und Zufuhr im Gleichgewicht sind.",
           "**Brücken:** Broughton (bei Manchester) 1831: Hängebrücke brach teilweise ein (ein schlecht geschmiedeter Bolzen an der Verankerung versagte; 20 Verletzte, keine Toten), als 74 Soldaten im Gleichschritt darüber marschierten – seither »ohne Tritt« über Brücken. Millennium Bridge London 2000: seitliches Schwanken durch Fußgänger, die sich unbewusst dem Schwanken anpassten (Rückkopplung). Tacoma Narrows 1940: aeroelastisches Flattern – nicht einfach »Windstöße im Takt«."],
  "nur": ["Erzwungene gedämpfte Schwingung: Das Maximum der Auslenkungsamplitude liegt bei ω_r = √(ω₀² − 2δ²) (δ = Abklingkonstante) – bei schwacher Dämpfung praktisch bei ω₀. Darum im Kadettentext »nahe der Eigenfrequenz«.",
          "Tacoma Narrows: Billah & Scanlan, American Journal of Physics 59 (1991) 118 – zeigen, dass das Schulbuchbild »Resonanz durch Wind« zu einfach ist (Flattern = selbsterregte Schwingung).",
          "Biologie-Brücke Innenohr: Die Basilarmembran schwingt je nach Frequenz an verschiedenen Orten maximal (Wanderwelle); die äußeren Haarzellen verstärken aktiv. »Resonanzorgan« ist ein brauchbares Bild, aber nicht die ganze Wahrheit – Vertiefung in der Einheit Gehör (E10)."],
  "stolper": "»Resonanz = Zerstörung« – nein: Resonanz heißt große Amplitude; ob etwas bricht, entscheiden Dämpfung und Festigkeit. Auch erwünscht: Schaukel, Musikinstrument, Radio-Empfang.",
  "bild": "img/g3_resonanz.png"},
 {"titel": "3 Mechanische Wellen, v = λ · f (Buch S. 54–55)",
  "text": ["**Welle:** Gekoppelte Teilchen geben eine Störung weiter; transportiert wird Energie (und Information), nicht Materie. Mechanische Wellen brauchen ein Medium.",
           "**Quer/längs:** Seil (quer), Schall in Luft (längs). In Festkörpern gibt es beides (Erdbeben: P-Welle längs und schneller, S-Welle quer). Wasseroberflächenwellen sind gemischt (Kreisbahnen) – im Unterricht als Modell kennzeichnen.",
           "**Zwei Diagramme:** y(x) bei festem t (Momentaufnahme) → λ ablesen; y(t) bei festem x → T ablesen. Gleiche Sinusform, andere Achse – der häufigste Lesefehler. Brücke zum EKG-Referat (4AK): eine EKG-Kurve ist ein Zeitsignal y(t), keine Momentaufnahme einer Welle.",
           "**Grundgleichung:** In einer Periode T läuft die Welle eine Wellenlänge λ weiter → v = λ/T = λ·f. v hängt vom Medium ab (Schall in Luft ca. 343 m/s bei 20 °C; das Buch rechnet mit 334 m/s), nicht von f."],
  "nur": ["Seilwelle: v = √(F/μ) (F Spannkraft, μ Masse pro Länge). Leichte gelbe Schnur (μ geschätzt wenige g/m) bei 5 N → v ≈ 30 m/s: Puls in 0,1 s über 3 m – darum die Schnur nur locker halten bzw. die Kadetten-Welle als Hauptbeobachtung.",
          "Sonar/Echoortung: Entfernung s = v·t/2 (Hin- und Rückweg). Schall in Wasser ca. 1 480 m/s – Brücke zum Ultraschall (Akustik, E9)."],
  "stolper": "λ auf der Zeitachse ablesen (oder T auf der Ortsachse). Gegenmittel: vor jedem Diagramm laut die waagrechte Achse vorlesen lassen.",
  "bild": "img/g4_ort_zeit.png"},
 {"titel": "4 Überlagerung, stehende Wellen, Huygens (Buch S. 51, 56–57)",
  "text": ["**Superposition:** In linearen Medien addieren sich die momentanen Auslenkungen an jedem Ort. Gleiche Frequenz und Gleichtakt: Amplituden addieren sich; Gegentakt: Betrag der Differenz (3 cm und 1 cm → 4 cm bzw. 2 cm). Vollständige Auslöschung nur bei gleichen Amplituden.",
           "**Energie:** Auslenkung null an einem Ort/Zeitpunkt heißt nicht, dass Energie vernichtet ist: Bei laufenden Pulsen steckt sie im Moment der Begegnung in der Bewegung der Teilchen; bei festen Mustern ist sie räumlich umverteilt (helle/dunkle Streifen).",
           "**Stehende Welle:** zwei gegenläufige gleiche Wellen (oft Welle + Reflexion). Knoten ruhen immer, benachbarte Knoten im Abstand λ/2; Bäuche schwingen maximal. Grundlage für Saiten und Pfeifen (Akustik).",
           "**Huygens:** Jeder Punkt einer Wellenfront ist Ausgangspunkt einer Elementarwelle; die Einhüllende ist die neue Front. Erklärt Beugung (stark, wenn Öffnung ≈ λ) und – später in der Optik – Reflexion und Brechung. Huygens baute 1656 auch die erste Pendeluhr (Verbindung zu Teil 1)."],
  "nur": ["Das Huygens-Prinzip liefert ohne Zusatzannahmen (Fresnel) auch eine rückwärts laufende Welle – im Unterricht nur die vordere Hälfte zeichnen.",
          "Aktuelle Forschung (Für Schnelle, A17): Beugung/Interferenz auch bei Gravitationswellen – GW231123 (23.11.2023), mögliche Linsenwirkung, laut MPG-Meldung vom 27.08.2026 nicht eindeutig nachgewiesen. Gut, um Messung und Modell zu trennen."],
  "stolper": "Amplituden immer addieren (+2 und −2 = 4). Gegenmittel: Werte mit Vorzeichen in die Tabelle von K2.2-V2 schreiben lassen.",
  "bild": "img/g6_huygens.png"},
 {"titel": "5 Elektromagnetisches Spektrum und Strahlenschutz (Buch S. 58–59)",
  "text": ["**EM-Wellen:** gekoppelte elektrische und magnetische Felder, kein Medium nötig; im Vakuum c = 299 792 458 m/s (Rechnen mit 3,00 · 10⁸ m/s). In Materie langsamer (Glas ca. 2 · 10⁸ m/s) – darum Brechung (Optik).",
           "**Bereiche:** Radiowellen (inkl. Mikrowellen 1 mm–1 m) – Infrarot – sichtbar (ca. 380–780 nm laut Buch; Grenzen unscharf) – UV – Röntgen – Gamma. Röntgen und Gamma unterscheiden sich vor allem durch die Entstehung (Elektronenhülle bzw. Atomkern), die Energiebereiche überlappen.",
           "**Photonenenergie und Intensität:** E = h·f gilt pro Photon; Intensität = Leistung pro Fläche. Ionisierend wird es ab einigen eV pro Photon (fernes UV, Röntgen, Gamma). UVA/UVB der Sonne sind nach Strahlenschutz-Einteilung nicht-ionisierende optische Strahlung, schädigen aber trotzdem Haut, Augen und DNA (photochemisch).",
           "**Bundesheer-Bezug:** Truppenfunk im UKW-Bereich (30–88 MHz → λ ≈ 3–10 m, darum lange Antennen); Radar mit Mikrowellen (cm-Bereich); Wärmebildgeräte (IR, 8–14 µm) vs. Restlichtverstärker (verstärken schwaches sichtbares/nahes IR-Licht)."],
  "nur": ["MRT: statisches Magnetfeld (1,5–3 T), Gradientenfelder und Radiofrequenz-Pulse; keine ionisierende Strahlung, aber eigene Risiken (Metall, Implantate, Erwärmung). EKG: misst Potentialdifferenzen der Herzaktivität über die Zeit. Beides nur als Infobox – keine medizinischen Aussagen zu Einzelfällen.",
          "Radioaktivität ≠ elektromagnetische Strahlung: Radioaktive Kerne senden Alpha-, Beta-Teilchen und oft Gamma aus; Funkwellen haben mit Kernzerfall nichts zu tun."],
  "stolper": "»Höhere Frequenz = gefährlicher« pauschal – stimmt nur für die Energie je Photon. Risiko = Art + Stärke (Intensität) + Dauer + Körperteil.",
  "bild": "img/g7_spektrum.png"},
]

RECHNEN = [
    "**Pendel (V1, A2, A3):** T = 2π·√(l/g). l = 0,40 m → T = 1,269 s (10 Schwingungen 12,69 s, f = 0,788 Hz); l = 0,90 m → T = 1,903 s (19,03 s, f = 0,525 Hz); Verhältnis 1,5. l = 0,81 m → T = 1,805 s ≈ 1,81 s.",
    "**Diagramm (A1):** y = 3 cm · sin(2πt / 0,8 s): Hochpunkte bei 0,2 s, 1,0 s, 1,8 s → T = 0,8 s, f = 1,25 Hz, A = 3 cm (nicht 6 cm).",
    "**Federpendel (A14):** m = 0,200 kg, k = 20,0 N/m → T = 2π·√0,0100 s² = 0,628 s; vierfache Masse → doppelte Periodendauer.",
    "**g aus Daten (A15):** 20 Schwingungen in 32,6 s → T = 1,63 s; g = 4π²·0,640 m / (1,63 s)² = 9,51 m/s² (3 % unter 9,81). Die Daten sind bewusst so gewählt, dass »9,81« nicht als richtig erkannt wird (2-%-Toleranz der Prüfung).",
    "**Wellen (A7):** λ = 334 m/s : 440 Hz = 0,759 m; Meereswelle v = 300 m : 15 s = 20 m/s. **Funk (A11):** 50 MHz → λ = 3,00 · 10⁸ : 5,0 · 10⁷ m = 6,0 m; UKW-Radio 100 MHz → 3,00 m.",
    "**Überlagerung (A8, A16):** (+2) + (−1) = +1 cm; 3 cm und 1 cm → Gleichtakt 4 cm, Gegentakt 2 cm.",
]

FEHLVORSTELLUNGEN = [
    ["Der schwerere Pendelkörper schwingt schneller.", "Beim Fadenpendel spielt die Masse im Modell keine Rolle.", "V1 mit 50 g statt 100 g wiederholen; PhET »Pendel-Labor« (Masse verstellen)."],
    ["Am Umkehrpunkt ist das Pendel am schnellsten.", "Dort ist die Geschwindigkeit null, in der Mitte am größten.", "Pendel-Animation in Teil 1 anhalten; Hand am Umkehrpunkt."],
    ["Ein Stoßdämpfer ist einfach eine Feder.", "Die Feder speichert Energie, der Dämpfer wandelt sie in Wärme um.", "Skizze Feder + Dämpfer; nach langer Fahrt ist der Dämpfer warm."],
    ["Resonanz zerstört immer.", "Resonanz heißt große Amplitude – Dämpfung begrenzt sie.", "Demo V2: Pendel schaukelt sich auf, reißt aber nicht."],
    ["Bei einer Welle wandert das Material mit.", "Teilchen schwingen am Ort; die Störung wandert.", "Büroklammer auf der Schnur, Kadetten-Welle (V3)."],
    ["Wellen prallen voneinander ab.", "Sie überlagern sich und laufen unverändert weiter.", "Animation »Überlagerung« (Teil 4) Bild für Bild."],
    ["Alle Strahlung ist radioaktiv / Handystrahlung = Radioaktivität.", "EM-Wellen sind Felder; Radioaktivität ist Kernzerfall.", "Funkantenne vs. radioaktive Quelle begrifflich trennen (Teil 5)."],
    ["Nicht-ionisierend = harmlos.", "UV und starke Laser schaden trotzdem.", "Sonnenbrand als Alltagsbeispiel."],
]

FRAGEN = [
    ("Warum schwingt ein schwerer Kadett auf der Schaukel nicht schneller?", "Mehr Gewichtskraft, aber auch mehr Trägheit – im Modell gleicht sich das aus. Real ändern Sitzhaltung und Schwerpunkt die wirksame Länge ein wenig."),
    ("Muss ich für zehn Schwingungen elfmal den Durchgang sehen?", "Ja, wenn der erste Durchgang »Null« ist: Null plus zehn weitere Durchgänge in dieselbe Richtung."),
    ("Warum bleibt das Pendel in der Mitte nicht einfach stehen?", "Dort ist die rücktreibende Kraft null, die Geschwindigkeit aber am größten – die Trägheit trägt es weiter."),
    ("Warum wird ein Stoßdämpfer warm?", "Er wandelt Schwingungsenergie in innere Energie (Wärme) um – genau seine Aufgabe."),
    ("Kann eine kleine Kraft eine Brücke zum Schwingen bringen?", "Ja, wenn sie oft im passenden Takt kommt (Resonanz). Wie groß die Schwingung wird, hängt von Dämpfung und Bauweise ab – darum »ohne Tritt«."),
    ("Warum hört man jemanden um die Ecke, sieht ihn aber nicht?", "Schall hat Wellenlängen von cm bis m – ähnlich groß wie Türen und Ecken – und wird stark gebeugt. Licht hat nur ca. 0,5 µm Wellenlänge."),
    ("Funktioniert Funk im Weltraum?", "Ja – Funk ist eine elektromagnetische Welle und braucht kein Medium (Funk zur Raumstation)."),
    ("Ist Handystrahlung dasselbe wie Radioaktivität?", "Nein. Handys senden Radiowellen (Mikrowellen); Radioaktivität ist der Zerfall von Atomkernen."),
    ("Kann eine Wärmebildkamera durch Rauch oder Wände sehen?", "Durch Rauch oft ja – langwelliges Infrarot (8–14 µm) wird von feinem Rauch weniger gestreut als Licht. Durch Wände, Glasscheiben und dichten Nebel aber nicht."),
    ("Ist MRT eine Art Röntgen?", "Nein: MRT nutzt Magnetfelder und Radiowellen, Röntgen ionisierende Strahlung. Beide haben eigene Sicherheitsregeln."),
    ("Warum zerspringt ein Glas, wenn man laut singt?", "Resonanz: Trifft der Ton genau die Eigenfrequenz und ist er sehr laut, schaukelt sich die Schwingung auf. Im Unterricht nur als Buch-Film, kein Versuch."),
]

VIDEO_NOTIZ = {
    "resonanz_buch": "Filmtipp aus dem Buch S. 53 (Resonanz). Von Stephan zum Einbau freigegeben (25.10.2026); für Claude nicht abrufbar, Titel und Länge daher nicht bestätigt. Freiwillig, kein Glas-Versuch.",
    "stehend_buch": "Filmtipp aus dem Buch S. 56 (stehende Schallwellen). Von Stephan freigegeben (25.10.2026), für Claude nicht abrufbar; passt zu Teil 4 bzw. Ausblick Akustik.",
    "stehwelle_buch": "Animation aus dem Buch S. 56 (stehende Welle). Von Stephan freigegeben (25.10.2026), für Claude nicht abrufbar; Ersatz: eigene GIF-Animation in Teil 4.",
    "phet_pendel": "PhET Pendel-Labor (HTML5, Deutsch, läuft am Handy): Länge und Masse getrennt verstellen, Reibung aus – Ersatz für V1, falls der Aufbau scheitert. Oberfläche nicht interaktiv getestet.",
    "phet_seil": "PhET Welle an einem Seil: »Puls«, Dämpfung niedrig, Ende »lose« – zeigt den markierten Punkt. Ersatz für die Schnur. Vorher am Schul-PC starten.",
    "phet_interferenz": "PhET Welleninterferenz: Wasser, zwei Quellen, gleiche Frequenz – ruhige Linien zeigen destruktive Interferenz. Grundlage für K2.2-V2.",
}

AUSBLICK = ("Danach laut Jahresplan Block C: E9 Akustik (Schall, Tonhöhe, Lautstärke, Dopplereffekt, Ultraschall – Versuch V4.14 Schallgeschwindigkeit/Echo und V4.18 stehende Wellen passen dort), "
            "E10 Gehör (Basilarmembran als »Resonanzorgan«), E11 Optik (Brechung mit Huygens), E12 Auge. Die Begriffe Frequenz, Wellenlänge, Resonanz und Beugung werden dort direkt gebraucht.")

QUELLEN = [
    "**Grundlage:** Entwurf ChatGPT v1 (25.10.2026, »Inhaltliche Ausarbeitung für Claude«) – fachlich geprüft; Korrekturen und Ergänzungen im Prüfbericht Claude v1.",
    "**Trauner Naturwissenschaften HAK 4** S. 47–59: Inhalte, Buch-Aufgaben S. 55, 57, 59 (in eigenen Worten als A7, A9, A11), Versuch S. 53 (→ K2.1-V2), Filmtipps nawi_v50, nawi_v51, stehendeWelle. Die Buchseiten lagen ChatGPT als Fotos vor; Claude hat sie nicht selbst gesehen (Stephan: ChatGPT vertrauen).",
    "**Zusatzquellen A/B** (»Naturwissenschaften HAK IV« und Kapitel 18/19 Schwingungen/Wellen) laut ChatGPT: Ein-Variablen-Vergleich, Stoßdämpfer, Grenzen der Wasserwellen-Darstellung – übernommen in Theorie Teil 2/3 und V1.",
    "**Expedition Physik 4** (Projekt): Wellenlänge aus Ortsdiagrammen → Teil 3 (Grafik Ort/Zeit); Praxisteil V7.2 Schwingkreis geprüft, nicht übernommen (elektrischer Aufbau, Zeit).",
    "**Jahresplan v23:** E6–E8, Versuche V4.11 (übernommen, gekürzt), V4.12 (nicht durchgeführt: Federpendel fehlt; nur eine Stimmgabel und zwei Resonanzkästen vorhanden (Stephan, 25.10.) – kein Mitschwingversuch möglich; K2.1-V2 ist Alternative, kein Ersatz), V4.13 (ersetzt durch Simulation: Wellenwanne nicht nachgewiesen), V4.14–V4.16 (nicht eingeplant: Zeit bzw. Geräte); Referatsthema »Resonanzkatastrophen«, Querverbindung Basilarmembran.",
    "**Inventar (2026-09):** #10 Bandmaß 3 m, #29 Doppelmuffe, #57 gelbe Schnur, #59 Gewichtssatz, #141/#143 Stativstäbe, #179 V-Fuß, F-038 Büroklammern; #140 Stativklemme (10–25 mm) passt nicht für die dünne Schnur – Schnur festknoten oder Universalklemme #160 (0–80 mm) testen. Stimmgabeln: im Inventar #144 und »Stimmgabelpaar« #145, tatsächlich laut Stephan (25.10.2026) nur eine Stimmgabel und zwei Resonanzkästen – nicht eingeplant; passt zu Akustik E9 (Schallerzeugung, Übertragung, Hörbarkeit), nicht als Resonanzversuch.",
    "**Fachquellen:** OpenStax University Physics Vol. 1, Kap. 15.4–15.6 und 16.1/16.5 (Pendel, Dämpfung, Resonanz, Wellen, Interferenz); OpenStax College Physics 2e 27.2 (Huygens); Billah & Scanlan, Am. J. Phys. 59 (1991) 118 (Tacoma Narrows) – laut ChatGPT-Entwurf geöffnet.",
    "**Selbst geprüft (25.10.2026):** Max-Planck-Gesellschaft, »Black holes heavier than allowed?« (27.08.2026) und Live Science zur GW231123-Linsenstudie (Goyal, Villarrubia-Rojo, Zumalacárregui, ApJL 2026) → Forschungskarte A17; Dlubal-Blog zu Broughton 1831/Millennium Bridge → Teil 2; PhET-Liste (Pendel-Labor HTML5, Deutsch).",
    "**Nicht prüfbar von hier:** die drei Trauner-Filmtipps (Seite gesperrt) – von Stephan am 25.10.2026 zum Einbau freigegeben; keine zusätzlichen YouTube-Videos eingebaut, weil sie hier nicht geprüft werden konnten.",
]
