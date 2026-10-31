"""Herrichte-Liste K2.1–2.3: alle Lehrmittel der Versuche, Stück je Versuch, höchster gleichzeitiger Bedarf, Bestand laut Inventar, Fehlmenge.
Alle Versuche laufen an einem gemeinsamen Aufbau (1 Ansatz); nur die Handys braucht jede Gruppe (Kadetten-Geräte, kein Inventar)."""
import versuche_daten as VD

SLOTS = [["K2.1-V1"], ["K2.1-V2"], ["K2.2-V1"], ["K2.2-V2"]]  # nie gleichzeitig


def ansaetze(v, key):
    return VD.GRUPPEN if key in VD.JE_GRUPPE else 1


def tabelle():
    per = {}
    for v in VD.VS:
        for txt, icon, key, n in v["mat"]:
            if not n: continue
            per.setdefault(key, {})
            per[key][v["nr"]] = per[key].get(v["nr"], 0) + n * ansaetze(v, key)
    rows = []
    for key, d in per.items():
        name, icon, ort, bestand = VD.LM[key]
        gesamt = max(sum(d.get(nr, 0) for nr in slot) for slot in SLOTS)
        if bestand is None or isinstance(bestand, str):
            fehlt = "–"
        else:
            fehlt = str(gesamt - bestand) if gesamt > bestand else "–"
        rows.append({"key": key, "name": name, "icon": icon, "ort": ort, "per": d, "gesamt": gesamt, "bestand": bestand, "fehlt": fehlt})
    order = list(VD.LM.keys())
    rows.sort(key=lambda r: order.index(r["key"]))
    return rows, SLOTS


MENGEN = {
    "Pendel-Aufbau (K2.1-V1, V2)": "1 Aufbau für alle 8 Gruppen; Schnur ca. 1,2 m mit Fähnchen bei 0,40 m und 0,90 m; 100-g-Stück fest angebunden",
    "Schnur (K2.2-V1)": "ca. 3 m von derselben Rolle #57 + 1 Büroklammer",
    "Handys": "2 je Gruppe als Stoppuhr (16 Stück) – reichen sie nicht, stoppt eine Gruppe mit einem Handy",
    "Beamer": "PhET »Pendel-Labor«, »Welle an einem Seil«, »Welleninterferenz« vorab im Browser öffnen",
}


# Wo steht der Versuch? (Regelwerk 9: bei jedem Versuch angeben; Vorschlag, Stephan kann ändern)
PLATZ = {
    "K2.1-V1": "Lehrertisch vorne, Pendel quer zur Klasse (von links nach rechts); links und rechts je ca. 1,5 m frei lassen; Querstab nur über die Tischkante, nicht über Sitzplätze",
    "K2.1-V2": "Lehrertisch vorne, am selben Pendel wie K2.1-V1",
    "K2.2-V1": "Freie Fläche vorne bzw. Gang im Saal (Schnur ca. 3 m locker gespannt); für die Kadetten-Welle Platz für 10 Kadetten in einer Reihe",
    "K2.2-V2": "Lehrer-PC mit Beamer (PhET), kein Aufbau am Tisch nötig",
}
# Hinweis an der jeweiligen Zeile (Schlüssel = Material-Schlüssel aus versuche_daten.LM)
HINWEIS = {
    "stativ": MENGEN["Pendel-Aufbau (K2.1-V1, V2)"],
    ("schnur", "K2.1-V1"): "ca. 1,2 m mit Fähnchen bei 0,40 m und 0,90 m, fest am Querstab",
    ("schnur", "K2.1-V2"): "dieselbe Schnur wie K2.1-V1 (Länge 0,40 m)",
    ("schnur", "K2.2-V1"): MENGEN["Schnur (K2.2-V1)"],
    "handy": MENGEN["Handys"],
    "laptop": MENGEN["Beamer"],
}
