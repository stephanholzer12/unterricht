"""NAWI 3AB · K2.3a Ernährungsweisen (Buch S. 68–72) – 2 Stunden (v1).
Stunde 1: Personengruppen + Alternative Ernährungsformen · Stunde 2: Vegetarismus + Vollwerternährung, dann Quiz.
Quelle für Handy-Seiten (Lernseite, Arbeitsblatt, Quiz). Aus PPP 26-27-3AB-K2.1a-Ernaehrungsweisen-Lehrer.pptx."""
from daten import T, STAND

ORDNER = "3ab-nawi/k2-3a-ernaehrung"
BASE = "https://stephanholzer12.github.io/unterricht/"
URL = BASE + ORDNER + "/"
EYEBROW = "NAWI · 3AB · K2.3a Ernährungsweisen"
TITEL = "Ernährungsweisen: Personengruppen, Vegetarismus & Vollwerternährung"
BUCH = "Buch S. 68–72"
KEY = "26-27-3AB-K2.3a-Ernaehrung-TH-Handy-v1"
V = "v1"

GRP = {1: "Stunde 1 · Personengruppen und Ernährungsformen", 2: "Stunde 2 · Vegetarismus und Vollwerternährung", 0: "Für Schnelle und Neugierige · optional"}

LERNZIELE = ["unterschiedliche Ernährungsweisen nennen",
             "ihre Auswirkungen auf den Körper erklären",
             "Ernährungsweisen und Vorurteile darüber beurteilen"]

WICHTIGSTE = ["Personengruppen haben unterschiedlichen Bedarf: Schwangere brauchen kaum mehr Energie, Sportler mehr Flüssigkeit und Nährstoffdichte, "
              "Ältere weniger Energie, Kinder und Jugendliche Vollkorn statt Süßem.",
              "**Vegan, lakto, ovo, ovolakto, Pescetarier und Flexitarier** unterscheiden sich darin, welche tierischen Lebensmittel erlaubt sind – "
              "**ovolakto** ist die größte Gruppe unter den Vegetariern.",
              "Bei Honig und Gelatine ist Vorsicht geboten: Honig zählt für vegane Kost nicht, Gelatine (aus Knochen und Häuten) für keine vegetarische Form.",
              "Vegetarische Ernährung ist als Dauerkost geeignet, wenn sie abwechslungsreich ist – bei veganer Kost drohen Engpässe bei Eiweiß, Eisen, "
              "Kalzium und Jod, bei **Puddingvegetarismus** wird nur das Fleisch gestrichen, nicht aber Süßes.",
              "Die **Wertstufen 1–4** ordnen Lebensmittel nach dem Grad der Verarbeitung – Stufe 1+2 sollte die Hälfte der täglichen Nahrung ausmachen, "
              "Stufe 4 möglichst gar nicht."]

FACHBEGRIFFE = [["Begriff", "Bedeutung"],
                ["Ernährungsweise", "Art, wie sich ein Mensch dauerhaft ernährt"],
                ["Vegetarier", "isst kein Fleisch und keinen Fisch"],
                ["vegan", "nur pflanzliche Lebensmittel – auch kein Honig"],
                ["lakto / ovo", "lakto = + Milchprodukte · ovo = + Eier erlaubt"],
                ["ovolakto", "+ Milch und Eier – größte Gruppe der Vegetarier, als Dauerkost geeignet"],
                ["Pescetarier", "isst Fisch statt Fleisch"],
                ["Flexitarier", "isst flexibel – selten Fleisch, viel Gemüse und Obst"],
                ["Vollwerternährung", "möglichst natürliche, frische, wenig verarbeitete Lebensmittel"],
                ["Wertstufe", "Einteilung der Lebensmittel nach ihrem Wert – von 1 (sehr gut) bis 4"],
                ["Nährstoffdichte", "Menge an Nährstoffen im Verhältnis zur Energie (kcal)"],
                ["Puddingvegetarismus", "Fleisch weglassen, aber vor allem Süßes und Mehlspeisen essen"],
                ["Gelatine", "tierisches Bindemittel aus Knochen und Häuten (z. B. in Gummibärchen)"],
                ["V-Label", "gelbes Siegel mit „V“ für vegetarische bzw. vegane Produkte"]]

QUIZ = [  # (Thema, Frage, [richtig, falsch, falsch, falsch], Erklärung, Buchseite)
 ("Personengruppen", "Wie viel mehr Energie braucht eine Schwangere ungefähr pro Tag?", ["ca. 240 kcal", "das Doppelte", "ca. 1.000 kcal", "gar nicht mehr"],
  "Nur ca. 1.000 kJ (≈ 240 kcal) Mehrbedarf – etwa eine Portion Müsli mit Milch. „Für zwei essen“ ist ein Mythos.", "Buch S. 69"),
 ("Personengruppen", "Worauf sollten Sportler besonders achten?", ["auf Nährstoffdichte und ausreichend Trinken", "auf möglichst viele Energydrinks", "auf eine einzige große Mahlzeit", "auf möglichst wenig Flüssigkeit"],
  "Mehrere kleine Mahlzeiten, Wasser statt Energydrinks, und Nährstoffdichte = Nährstoffe im Verhältnis zur Energie.", "Buch S. 69"),
 ("Personengruppen", "Warum sollten ältere Menschen „Trinken ohne Durst“ üben?", ["Das Durstempfinden lässt im Alter nach", "Sie brauchen mehr Energie", "Wasser ersetzt Mahlzeiten", "Durst ist bei Älteren stärker"],
  "Mit dem Alter nehmen Muskel- und Knochenmasse ab, das Durstgefühl sinkt – Trinken muss bewusst trainiert werden.", "Buch S. 69"),
 ("Ernährungsformen", "Was lehnt veganer Kost zusätzlich zu Fleisch und Fisch ab?", ["auch Honig, Milch und Eier", "nur Fleisch", "nur Fisch", "nur Milchprodukte"],
  "Vegane Kost ist rein pflanzlich – sogar Honig wird abgelehnt.", "Buch S. 70"),
 ("Ernährungsformen", "Welche Gruppe ist unter den Vegetariern am größten?", ["ovolakto", "vegan", "Pescetarier", "Flexitarier"],
  "Ovolakto (Milch und Eier erlaubt) ist die größte Gruppe – und als Dauerkost gut geeignet.", "Buch S. 70–71"),
 ("Ernährungsformen", "Ein Pescetarier isst …", ["Fisch statt Fleisch", "weder Fisch noch Fleisch", "nur Fleisch", "nur Milchprodukte"],
  "Pescetarier (ital. pesce = Fisch) essen Fisch, aber kein Fleisch.", "Buch S. 70"),
 ("Vegetarismus", "Darf ein veganer Mensch Honig essen?", ["nein", "ja, uneingeschränkt", "nur Bio-Honig", "nur im Winter"],
  "Honig gilt als tierisches Produkt und wird bei veganer Kost abgelehnt.", "Buch S. 70"),
 ("Vegetarismus", "Warum sind Gummibärchen für keine vegetarische Form geeignet?", ["wegen der Gelatine aus Knochen und Häuten", "wegen des Zuckers", "wegen der Farbstoffe", "wegen der Verpackung"],
  "Gelatine wird aus Knochen und Häuten von Schwein oder Rind gewonnen – auch Ovolakto-Vegetarier essen sie nicht.", "Buch S. 71"),
 ("Vegetarismus", "Was bedeutet Puddingvegetarismus?", ["Fleisch weglassen, aber viel Süßes und Mehlspeisen essen", "nur Pudding essen", "kein Zucker, aber Fleisch", "vegane Süßspeisen"],
  "Wird nur das Fleisch gestrichen und vermehrt zu Süßem gegriffen, ist das minderwertiger als herkömmliche Kost.", "Buch S. 71"),
 ("Vegetarismus", "Welches Risiko besteht bei veganer Ernährung ohne Planung?", ["Mangel an Eiweiß, Eisen, Kalzium oder Jod", "zu viel Eiweiß", "zu hoher Blutzucker", "zu viel Kalzium"],
  "Bei Veganern kann die Versorgung mit diesen Stoffen gefährdet sein – für Säuglinge und Kleinkinder wird abgeraten.", "Buch S. 71"),
 ("Vollwerternährung", "Wie viel der täglichen Nahrung sollte laut Buch aus Stufe 1+2 stammen?", ["die Hälfte", "ein Zehntel", "fast nichts", "alles"],
  "Rohe und schonend verarbeitete Lebensmittel sollten die Hälfte der täglichen Nahrung abdecken.", "Buch S. 72"),
 ("Vollwerternährung", "In welche Wertstufe gehören Fertiggerichte und Vitaminpräparate?", ["Stufe 4", "Stufe 1", "Stufe 2", "Stufe 3"],
  "Übertrieben verarbeitete Lebensmittel und isolierte Präparate sind Stufe 4 – nicht empfehlenswert.", "Buch S. 72"),
 ("Vollwerternährung", "Was kritisiert das Buch an der Wertstufen-Einteilung?", ["Manche „wenig empfehlenswerte“ Lebensmittel können trotzdem sinnvoll sein (z. B. H-Milch als Kalziumquelle)", "Sie ist zu kompliziert zum Merken", "Sie gilt nur für Sportler", "Sie wurde nie wissenschaftlich geprüft"],
  "H-Milch ist Stufe 3, aber eine gute Kalziumquelle – die Einteilung ist nicht ganz unproblematisch.", "Buch S. 72"),
]
