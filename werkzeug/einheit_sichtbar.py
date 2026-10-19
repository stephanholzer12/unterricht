#!/usr/bin/env python3
"""Einheit für EINE Klasse ein- oder ausblenden (setzt/entfernt "versteckt" in einheiten.json).
Aufruf: python3 werkzeug/einheit_sichtbar.py <ordner-oder-teil> <ausblenden|einblenden>
Beispiel: python3 werkzeug/einheit_sichtbar.py 1ak-nawi/k1-2-2-koerper ausblenden
Der Teil muss genau eine Einheit treffen. Die Seiten bleiben online (Direktlink/QR geht weiter), nur die Klassenseite zeigt sie nicht mehr."""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "einheiten.json")
if len(sys.argv) != 3 or sys.argv[2] not in ("ausblenden", "einblenden"):
    sys.exit(__doc__)
teil, aktion = sys.argv[1].strip().strip("/"), sys.argv[2]
L = json.load(open(P, encoding="utf-8"))
treffer = [e for e in L if e.get("ordner") == teil] or [e for e in L if teil in e.get("ordner", "")]
if len(treffer) != 1:
    sys.exit("Gefunden: %d Einheiten für '%s'. Ordner genauer angeben. Vorhanden:\n  %s" % (len(treffer), teil, "\n  ".join(e["ordner"] for e in L)))
e = treffer[0]
if aktion == "ausblenden": e["versteckt"] = True
else: e.pop("versteckt", None)
json.dump(L, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2); open(P, "a").write("\n")
print(e["ordner"], "->", "versteckt" if aktion == "ausblenden" else "sichtbar")
