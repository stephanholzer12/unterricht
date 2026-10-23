"""Themenblöcke aus dem Jahresplan übernehmen → werkzeug/bloecke.json

Aufruf im Repository-Ordner:
    python3 werkzeug/bloecke_aus_jahresplan.py <Pfad zu Jahresplan_SJ_2026-27….xlsx>

Liest im Blatt »Stunden« die Spalten Klasse, Datum, Block und Geplante Einheit und schreibt pro
Klassenseite die Blöcke in der Reihenfolge, in der sie im Schuljahr drankommen, samt den
Einheiten-Nummern (E1, E2 …) des Jahresplans. build_index.py ordnet damit die Blöcke und
zeigt »Themenblock x von y«. Welche Einheit zu welchem Block gehört, steht in einheiten.json
(Feld »block«, z. B. "A Atombau & Bindung", und »jahresplan«, z. B. "E3"). Zusätzlich wird pro Einheit die
Zahl der geplanten Unterrichtsstunden gespeichert (»stunden«) – sie erscheint im Fahrplan jeder Theorie-Seite.
"""
import json, os, re, sys
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Klassenseite im Repository → Klasse im Jahresplan (bei NAWI/TÖW die A-Klasse; die B-Klasse hat dieselben Blöcke)
KLASSEN = {"1ab-nawi": "1AK", "2ab-nawi": "2AK", "3ab-nawi": "3AK", "4ab-nawi": "4AK", "5ab-toew": "5AK",
           "2ak-pbgw": "2AK PBGW", "3bk-pbgw": "3BK PBGW", "5ak-iwk": "5AK IWK"}


def name(block):
    return re.sub(r"\s*\([^)]*\)\s*$", "", block).strip()  # »C Ökologie (Mai/Juni)« → »C Ökologie«


def main(pfad):
    wb = openpyxl.load_workbook(pfad, read_only=True, data_only=True)
    ws = wb["Stunden"]
    kopf = None
    daten = {}
    for r in ws.iter_rows(values_only=True):
        if kopf is None:
            if "Block" in r and "Klasse" in r:
                kopf = {v: i for i, v in enumerate(r) if v}
            continue
        k, d, b, e = (r[kopf["Klasse"]], r[kopf["Datum"]], r[kopf["Block"]], r[kopf["Geplante Einheit"]])
        if not (k and d and b):
            continue
        b = name(str(b))
        if "/" in b or b.startswith("Reserve"):  # Übergangsstunden »A … / E …« und Reserve auslassen
            continue
        eintrag = daten.setdefault(k, {}).setdefault(b, {"ab": d, "einheiten": set(), "stunden": {}, "brutto": {}})
        eintrag["ab"] = min(eintrag["ab"], d)
        m = re.match(r"E(\d+)", str(e or ""))
        if m:
            eintrag["einheiten"].add(int(m.group(1)))
            # Unterrichtsstunden: Spalte »Anz.«. »stunden« = tatsächlich stattfindende (ohne Entfall x, Feiertag F,
            # Verschiebung v), »brutto« = ursprünglich geplante (Entfall zählt mit)
            st = str(r[kopf["Status"]] or "").strip().lower()
            n = int(r[kopf["Anz."]]) if isinstance(r[kopf["Anz."]], (int, float)) else 1
            nr = int(m.group(1))
            if st not in ("f", "v"):
                eintrag["brutto"][nr] = eintrag["brutto"].get(nr, 0) + n
            if st not in ("x", "f", "v"):
                eintrag["stunden"][nr] = eintrag["stunden"].get(nr, 0) + n
    out = {}
    for ordner, k in KLASSEN.items():
        bl = sorted(daten.get(k, {}).items(), key=lambda kv: kv[1]["ab"])
        out[ordner] = [{"block": b, "einheiten": ["E%d" % n for n in sorted(v["einheiten"])],
                        "stunden": {"E%d" % n: v["stunden"].get(n, 0) for n in sorted(v["einheiten"])},
                        "brutto": {"E%d" % n: v["brutto"].get(n, 0) for n in sorted(v["einheiten"])}} for b, v in bl]
        print(ordner, "←", k, ":", " → ".join(b for b, _ in bl))
    ziel = os.path.join(ROOT, "werkzeug", "bloecke.json")
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("geschrieben:", ziel)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
