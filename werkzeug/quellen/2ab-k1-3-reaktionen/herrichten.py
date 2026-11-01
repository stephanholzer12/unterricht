"""Herrichte-Liste K1.3: alle Lehrmittel der Versuche, Stück je Versuch, höchster gleichzeitiger Bedarf, Bestand laut Inventar, Fehlmenge."""
import versuche_daten as VD

# Versuche, die gleichzeitig laufen (Stationen 1 und 2); V6 läuft als Demo davor
SLOTS = [["K1.3-V1", "K1.3-V2"], ["K1.3-V3"], ["K1.3-V6"], ["K1.3-V4", "K1.3-V5"], ["K1.3-V7"], ["K1.3-V8"]]


def ansaetze(v):
    return VD.GRUPPEN if v["id"] == "brause" else 1


def tabelle():
    per = {}  # key -> {nr: stück}
    for v in VD.VS:
        for txt, icon, key, n in v["mat"]:
            if not n: continue
            per.setdefault(key, {})
            per[key][v["nr"]] = per[key].get(v["nr"], 0) + n * ansaetze(v)
    rows = []
    for key, d in per.items():
        name, icon, ort, bestand = VD.LM[key]
        gesamt = max(sum(d.get(nr, 0) for nr in slot) for slot in SLOTS)
        if key in ("eisenwolle", "salz", "oel", "cuso4", "zitrone", "natron", "h2o2", "mno2", "kupferblech", "eis", "brause", "parafilm"):
            fehlt = "besorgen" if bestand is None else ""
            gesamt_txt = gesamt
        else:
            fehlt = "besorgen" if bestand is None else (str(gesamt - bestand) if gesamt > bestand else "")
            gesamt_txt = gesamt
        rows.append({"key": key, "name": name, "icon": icon, "ort": ort, "per": d, "gesamt": gesamt_txt, "bestand": bestand, "fehlt": fehlt or "–"})
    order = list(VD.LM.keys())
    rows.sort(key=lambda r: order.index(r["key"]))
    return rows, SLOTS


MENGEN = {  # Verbrauchsmaterial: was insgesamt anzusetzen ist (pro Klasse)
    "Kupfersulfatlösung": "15,0 g CuSO₄ · 5 H₂O auf 150 ml Lösung auffüllen (= 10 g pro 100 ml) → 6 Durchgänge à 20 ml + Reserve",
    "Zitronensäure-Pulver, 5,0 g je Ansatz (vorportioniert)": "6 Portionen à 5,0 g abwiegen (Vortag möglich) – nichts ansetzen, kein Verdünnen",
    "Natron": "6 Portionen à 6,0 g (abgewogen, Vortag möglich)",
    "Kochsalz": "30 g für die Demo-Kältemischung + 1 Spatel für Rost-Ansatz 4",
    "Eis": "ca. 150 g, angetaut und zerstoßen (Kühlbox) – nur für die Demo am 10.11.",
    "Eisenwolle": "V1: 1–1,2 g · V2: 4 kleine Bäusche · V4: 6 × 1 g → ca. 10 g",
    "Wasserstoffperoxid-Lösung 3 % (Viroxidin 3 %, 1000 ml)": "gekauft/bestellt, Lieferung ausstehend: bei Eingang Etikett und Konzentration (3 %) prüfen, echtes Sicherheitsdatenblatt beim Lieferanten anfordern und ablegen; Menge für V7 erst nach dem Vorversuch festlegen – nichts aus den 30-%/35-%-Vorräten verdünnen",
    "Braunstein (Mangan(IV)-oxid, MnO₂)": "nur eine kleine Menge (Inventar #80) auf ein Uhrglas, Dose gleich schließen; Staub vermeiden; Abfall in den Sammelbehälter für manganhaltige Abfälle",
    "Dosierhilfe (Messzylinder oder Pipette) für gleiche Mengen": "2 Stück, Menge nach dem Vorversuch; Vorversuch (Dauer, Sichtbarkeit, Gefäßwahl) bis spätestens Mi 11.11.",
    "Brausetabletten": "9 Stück, gleiche Sorte (nur für den Zusatz-Versuch V8)",
}
