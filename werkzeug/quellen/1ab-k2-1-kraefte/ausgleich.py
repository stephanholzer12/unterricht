"""Ausgleich und Referat-Brücken K2.1 Mechanische Kräfte (13.11.2026) – EINE Quelle für Lösungsseite und Unterrichts-PPP.

AUSGLEICH: Fertige Bausteine für die Klasse, die vorne liegt (z. B. 1AK ist früher fertig als 1BK), damit beide beim nächsten Thema ungefähr gleich weit sind.
Alle Bausteine sind freiwillig und ohne Note, brauchen kein Material außer Papier und Handy und stehen NICHT auf den öffentlichen Kadetten-Seiten
(Prof. HOLZER sagt sie an, die Folien dazu stehen in der PPP als ausgeblendete Folien in der Präsentation »Ausgleich«).
Alles stammt aus bereits geprüften Inhalten dieser Einheit (Fehlvorstellungen, Newton-Fragen, Kräfte-Check) – hier steht nichts Neues, was nicht schon geprüft wäre.

BRUECKEN: Zu jedem Schüler-Referat, das in eine Stunde fällt, eine Minute Verbindung zur Einheit (eine Frage an die Klasse mit Kurzantwort für Prof. HOLZER).
Stichworte werden in der Lösungsseite im Referat-Titel gesucht (Groß-/Kleinschreibung egal)."""
import fachwissen as F, gruppen_daten as GD, inhalt as I

_FV = F.FEHLVORSTELLUNGEN
AUSSAGEN = [(_FV[i][0], _FV[i][1]) for i in (0, 2, 3, 5, 6)]

BAUSTEINE = [
 {"id": "A1", "marke": "DISKUSSION", "titel": "Stimmt das? Vier Ecken", "min": 15, "material": "keines",
  "tun": ["Vier Ecken im Raum: stimmt · stimmt nicht · kommt darauf an · weiß nicht. Handys weg.",
          "Prof. HOLZER liest eine Behauptung vor – alle gehen in ihre Ecke.",
          "Aus jeder Ecke begründet eine Person in einem Satz.",
          "Auflösung: Die Klasse nennt die richtige Version, Prof. HOLZER ergänzt."],
  "ergebnis": "Nichts abzugeben. Die Behauptungen, bei denen die Klasse geteilt war, kommen in Aufgabe 8 wieder vor.",
  "hinweis": "Fünf Behauptungen à 3 Minuten. Die Behauptungen und die richtige Version stehen im Reiter »Ausgleich«.", "quelle": "Fachwissen: Häufige Fehlvorstellungen"},
 {"id": "A2", "marke": "GRUPPENARBEIT", "titel": "Erklär's in 60 Sekunden", "min": 20, "material": "Papier, Stift",
  "tun": ["Jede Gruppe wählt eine Kraftsituation: Sprintstart, Klimmzug, Schwimmen, Bremsen, Rucksack beim Marsch oder Seilziehen.",
          "8 Minuten planen: Skizze mit Kraftpfeilen und drei Sätze – Welche Kraft? Wie groß, mit Formel und Einheit? Wo ist die Gegenkraft?",
          "Jede Gruppe erklärt in 60 Sekunden an der Tafel oder am Platz.",
          "Die anderen geben ein Daumenzeichen: richtig · verständlich · mit Zahl und Einheit."],
  "ergebnis": "Nichts abzugeben. Wer will, fotografiert die Skizze und stellt sie in Teams.",
  "hinweis": "Kein Video nötig. Wer gern filmt: 60 Sekunden, keine Gesichter nötig, nur Skizze und Stimme – freiwillig, in Teams.", "quelle": "Theorie-Karten Kraft, Gewichtskraft, Reibung, Gegenkraft"},
 {"id": "A3", "marke": "PARTNERCHECK", "titel": "Kräfte-Detektive", "min": 15, "material": "ein Handy je Paar",
  "tun": ["Zu zweit einen Gegenstand oder eine Situation im Raum fotografieren (keine Personen).",
          "Alle Kräfte als Pfeile einzeichnen: Richtung, ungefähre Länge, Name der Kraft.",
          "Foto tauschen: Das andere Paar prüft – Fehlt eine Kraft? Stimmt die Richtung? Gleichgewicht oder nicht?",
          "Drei Fotos am Beamer besprechen."],
  "ergebnis": "Nichts abzugeben. Die besten Fotos dürfen in Teams stehen.",
  "hinweis": "Nur Gegenstände fotografieren, keine Mitschüler, keine Gesichter. Fotos bleiben in Teams und werden nicht weitergeschickt.", "quelle": "Stunde 1: Kraftwirkung, Richtung, resultierende Kraft"},
 {"id": "A4", "marke": "VIDEO", "titel": "Newton sehen, Newton prüfen", "min": 20, "material": "Beamer, Handys",
  "tun": ["Video 2 (F = m · a) oder Video 3 (Kraft und Gegenkraft) von Apolin ansehen – mit den zwei Beobachtungsfragen.",
          "Antworten zu zweit vergleichen und kurz in der Klasse besprechen.",
          "Kräfte-Check (Quiz) zu zweit: ein Handy, beide diskutieren, dann antippen.",
          "Zum Schluss: Welche Frage war am schwersten? Prof. HOLZER klärt sie."],
  "ergebnis": "Nichts abzugeben. Das Quiz zählt nicht für die Note.",
  "hinweis": "Länge und Inhalt der Videos vorher prüfen (von hier nicht prüfbar). Passt auch als Supplierstunde.", "quelle": "Apolin: Newtonsche Grundgesetze; Kräfte-Check"},
]

VORHANDEN = "Schon im Arbeitsblatt für Schnelle: Zusatz 9 bis 11 (ca. 26 Minuten) – dafür braucht es keine Vorbereitung."

BRUECKEN = [
 {"such": ["rückstoß", "rueckstoss", "stg", "gewehr", "waffe"], "thema": "Rückstoß",
  "frage": "Die Kugel fliegt nach vorn – was spürt die Waffe? Auf welche Körper wirken Kraft und Gegenkraft, und warum heben sie sich nicht auf?",
  "antwort": "Die Gase drücken das Geschoss nach vorn und mit gleich großer Kraft die Waffe nach hinten (Wechselwirkung, 3. Newtonsches Gesetz). Beide Kräfte wirken auf verschiedene Körper, deshalb heben sie sich nicht auf.",
  "wo": "Gruppe 7 · Aufgabe 8 · Video 3"},
 {"such": ["porsche", "gt3", "sportwagen", "auto"], "thema": "Sportwagen",
  "frage": "Was hält ein Auto in der Kurve auf der Straße – und was ändert sich bei Nässe? Warum beschleunigt ein leichter Sportwagen bei gleicher Kraft stärker?",
  "antwort": "Die Haftreibung zwischen Reifen und Straße; bei Nässe ist sie kleiner. F = m · a: Bei gleicher Kraft ergibt eine kleinere Masse eine größere Beschleunigung.",
  "wo": "Gruppe 4 (Reibung) · Gruppe 1 (Beschleunigung) · Video 2"},
 {"such": ["vulkan"], "thema": "Vulkane",
  "frage": "Welche der sieben Kraft-Themen stecken in einem Vulkan? Warum steigt Magma auf, und was hat Druck damit zu tun?",
  "antwort": "Vereinfacht: Magma ist meist leichter als das umgebende Gestein und steigt auf (Auftrieb, Gruppe 3). In der Schmelze gelöste Gase stehen unter Druck (Gruppe 6) – das treibt Ausbrüche an. Frag nach, was das Referat dazu gesagt hat, und knüpfe daran an.",
  "wo": "Gruppe 3 (Auftrieb) · Gruppe 6 (Druck)"},
 {"such": ["eurofighter", "kampfjet", "jet", "flugzeug"], "thema": "Eurofighter",
  "frage": "Wie entsteht der Schub eines Strahltriebwerks? Wie groß sind Schub und Luftwiderstand, wenn der Jet gleichmäßig geradeaus fliegt?",
  "antwort": "Das Triebwerk stößt heiße Gase nach hinten aus, die Gegenkraft schiebt den Jet nach vorn (wie beim Rückstoß). Bei gleichmäßigem Geradeausflug sind Schub und Widerstand gleich groß – die resultierende Kraft ist null.",
  "wo": "Gruppe 7 · Stunde 1 (resultierende Kraft)"},
 {"such": ["hubschrauber", "helikopter", "heli"], "thema": "Hubschrauber",
  "frage": "Der Rotor drückt Luft nach unten – was bekommt der Hubschrauber dafür? Wie groß ist diese Kraft, wenn er ruhig in der Luft steht?",
  "antwort": "Die Luft drückt mit gleich großer Kraft zurück nach oben (Kraft und Gegenkraft). Beim Schweben ist die Kraft nach oben so groß wie die Gewichtskraft – ein Kräftegleichgewicht.",
  "wo": "Gruppe 7 · Gruppe 2 (Gewichtskraft) · Video 3"},
]
BRUECKE_ALLGEMEIN = {"thema": "Referat",
                      "frage": "Welche der sieben Themen (Bewegung, Gewichtskraft, Auftrieb, Reibung, Kapillarwirkung, Druck, Kraft und Gegenkraft) steckt in diesem Referat?",
                      "antwort": "Lass zwei Kadetten ein Thema nennen und in einem Satz begründen. Eine Minute reicht.", "wo": "alle Gruppen"}

# Reihenfolge der Aufgaben für die Folien: genau diese Texte stehen in der PPP
assert [b["id"] for b in BAUSTEINE] == ["A1", "A2", "A3", "A4"]
assert all(b["min"] in (15, 20) for b in BAUSTEINE)
assert len(AUSSAGEN) == 5
