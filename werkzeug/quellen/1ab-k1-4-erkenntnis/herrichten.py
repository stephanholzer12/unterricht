"""Herrichte-Liste K1.4 Erkenntnisgewinn (Mengen je Klasse – für 1AK und 1BK jeweils herrichten) – zum Abhaken (☐), EINE Quelle für VS-Fachwissen (Seite 1), VS-Lehrer-PPP (ausgeblendet) und Lösungsmappe.
Ordnung laut Regelwerk (14. Fassung): zuerst je Versuch, dann gesamt für alle Versuche; innerhalb jeder Liste zuerst Chemikalien und Verbrauchsmaterial,
dann Geräte und Lehrmittel, zuletzt was die Kadetten selbst mitbringen. Menge = Stück je Ansatz × Ansätze + Reserve.
Ansätze: 8 Gruppen (Klassengröße nicht bestätigt) für alles in VD.JE_GRUPPE, sonst 1 Ansatz für die ganze Klasse."""
import versuche_daten as VD

RESERVE = {"papier": 4, "klammer": 2}           # Ersatz für verknickte Blätter und verbogene Klammern
KADETTEN = {"handy", "bleistift"}               # bringen die Kadetten selbst mit – nur zur Erinnerung
ABSCHNITTE = [("chem", "Chemikalien und Verbrauchsmaterial"), ("geraet", "Geräte und Lehrmittel"), ("kadetten", "Bringen die Kadetten mit")]


def _abschnitt(key):
    if key in KADETTEN: return "kadetten"
    return VD.LM[key][4]


def _bestand_text(b):
    if b is None: return "nicht im Inventar"
    return str(b)


def _fehlt(gesamt, b):
    if isinstance(b, int): return str(gesamt - b) if gesamt > b else "–"
    return "–"


def zeilen(versuche):
    """Zeilen für eine Liste über die angegebenen Versuche (nie gleichzeitig → höchster Bedarf zählt)."""
    bedarf = {}
    for v in versuche:
        for txt, icon, key, n in v["mat"]:
            ans = VD.GRUPPEN if key in VD.JE_GRUPPE else 1
            menge = n * ans + RESERVE.get(key, 0)
            alt = bedarf.get(key)
            if alt is None or menge > alt["gesamt"]:
                bedarf[key] = {"key": key, "je": n, "ansaetze": ans, "reserve": RESERVE.get(key, 0), "gesamt": menge, "text": txt}
    out = []
    order = list(VD.LM)
    for key in sorted(bedarf, key=order.index):
        name, icon, ort, bestand, art = VD.LM[key]
        r = bedarf[key]
        rechnung = (f"{r['je']} × {r['ansaetze']} Gruppen" if r["ansaetze"] > 1 else f"{r['je']} für die Klasse") + (f" + {r['reserve']} Reserve" if r["reserve"] else "")
        out.append(dict(r, name=name, icon=icon, ort=ort, bestand=_bestand_text(bestand), fehlt=_fehlt(r["gesamt"], bestand),
                        abschnitt=_abschnitt(key), rechnung=rechnung))
    out.sort(key=lambda r: [a for a, _ in ABSCHNITTE].index(r["abschnitt"]))
    return out


def je_versuch():
    return [(v["nr"], v["titel"], zeilen([v])) for v in VD.VS]


def gesamt():
    return zeilen(VD.VS)


def tabelle():
    """Kompatibel mit älteren Bauskripten: (Zeilen gesamt, Slots)."""
    return gesamt(), [[v["nr"]] for v in VD.VS]


VOR_ORT = [  # was außer dem Material noch hergerichtet werden muss – ebenfalls zum Abhaken
    "Hallenprobe im Eingangsbereich gemacht (Faltung, Klammersitz, flacher Abwurf ohne Deckenkontakt, nutzbare Länge)",
    "Abwurflinie festgelegt (Bodenfuge) und Bandmaß am Rand ausgelegt, Nullpunkt an der Linie",
    "Eingangsbereich zur Stunde frei? (Durchgangsverkehr, Fluchtweg) – ggf. Schulwart informieren",
    "Papierblätter VS-AB je Gruppe ausgedruckt (8 Stück + 2 Reserve, je Klasse) – Ersatz, falls ein Protokoll-Handy streikt",
    "Faltanleitung am Beamer (Theorieteil »So baust du den Flieger«) bzw. 8 Ausdrucke",
    "Schachtel für die fertigen Flieger beschriftet (Klasse) – 1BK lagert von Mi 04.11. bis Mo 09.11.",
]

if __name__ == "__main__":
    for nr, tit, rows in je_versuch():
        print("==", nr, tit)
        for r in rows: print(" ☐", r["abschnitt"], r["name"], r["gesamt"], "(", r["rechnung"], ")", r["bestand"], r["fehlt"])
    print("== gesamt"); [print(" ☐", r["name"], r["gesamt"]) for r in gesamt()]
