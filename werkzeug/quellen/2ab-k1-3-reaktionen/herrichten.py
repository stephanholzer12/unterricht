"""Herrichte-Liste K1.3: alle Lehrmittel der Versuche, Stück je Versuch, höchster gleichzeitiger Bedarf, Bestand laut Inventar, Fehlmenge."""
import versuche_daten as VD

# Versuche, die gleichzeitig laufen (Stationen 1–3); alle anderen einzeln
SLOTS = [["K1.3-V1", "K1.3-V2"], ["K1.3-V3"], ["K1.3-V4", "K1.3-V5", "K1.3-V6"], ["K1.3-V7"], ["K1.3-V8"], ["K1.3-V9"]]


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
        if key in ("eisenwolle", "salz", "oel", "cuso4", "zitrone", "natron", "h2o2", "braunstein", "cuo", "kohle", "kupferblech", "eis", "kartoffel", "brause", "parafilm"):
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
    "Kupfersulfatlösung ca. 10 %": "ca. 15 g CuSO₄ · 5 H₂O in 100 ml Wasser (reicht für 5 Durchgänge à 20 ml)",
    "Zitronensäurelösung ca. 40 %": "40 g Zitronensäure in 60 ml Wasser (6 Durchgänge à 15 ml)",
    "Natron": "6 × 3 gehäufte Spatel ≈ 40 g",
    "Kochsalz": "6 Portionen à 30 g für die Kältemischung + 1 Spatel für Rost-Ansatz 4",
    "Eis": "6 × ca. 150 g zerstoßen (Kühlbox)",
    "Eisenwolle": "V1: 1–1,2 g · V2: 4 kleine Bäusche · V4: 6 × 1 g → ca. 10 g",
    "Wasserstoffperoxid 3 %": "10 ml H₂O₂ 30 % + 90 ml Wasser (Handschuhe, Brille)",
    "Brausetabletten": "9 Stück (6 Gruppen × 3 Hälften)",
    "Kartoffel": "1 rohe + 1 gekochte (10 min)",
}
