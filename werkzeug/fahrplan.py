"""Fahrplan jeder Einheit: Was passiert in Stunde 1, Stunde 2 …?

Quelle ist das Feld »fahrplan« einer Einheit in einheiten.json:
  "fahrplan": {"text": "kurzer Satz (optional)",
               "zeilen": [{"wann": "Stunde 1", "lesen": "Einstieg + Teil 1 · …", "aufgaben": "1–4",
                           "wie": "ohne Handy: … (optional)", "abgabe": "–"}, …]}
Zeilen, deren »wann« mit »Stunde« beginnt, zählen als Unterrichtsstunden. Andere Zeilen (»Für Schnelle«,
»Hausübung«) sind Zusatz.

build_index.py baut den Fahrplan bei jedem Lauf in theorie.html und aufgaben.html der Einheit ein
(zwischen den Markierungen <!--FAHRPLAN--> und <!--/FAHRPLAN-->) und zeigt ihn auf der Klassenseite.
Die im Jahresplan geplanten Stunden (bloecke.json, Felder »stunden« und »brutto«) werden auf der
Lehrer-Seite mit den Stunden des Fahrplans verglichen.
"""
import html, os, re

esc = html.escape
A, E = "<!--FAHRPLAN-->", "<!--/FAHRPLAN-->"

CSS = """<style>
.fahrplan { background: #fff; border: 2px solid #7FA83A; border-radius: 16px; padding: 14px 16px; margin: 14px 0; min-width: 0; max-width: 100%; }
.fahrplan .eyebrow { font-size: 14px; font-weight: 700; color: #2E7D8C; }
.fahrplan h2 { font-family: Cambria, "Source Serif 4", Georgia, serif; color: #3B4A2F; margin: 2px 0 6px; font-size: 24px; }
.fahrplan p { margin: 0 0 8px; } .fahrplan .std { font-weight: 700; color: #3B4A2F; }
.fahrplan .tablewrap { overflow-x: auto; max-width: 100%; }
.fahrplan table { width: 100%; border-collapse: collapse; font-size: 15px; }
.fahrplan th, .fahrplan td { border-bottom: 1px solid #D3DCC2; padding: 6px 6px; text-align: left; vertical-align: top; }
.fahrplan th { background: #DFE5D0; color: #3B4A2F; }
@media (max-width: 600px) {
  .fahrplan thead { display: none; }
  .fahrplan tr { display: block; border-bottom: 2px solid #D3DCC2; padding: 6px 0; }
  .fahrplan td { display: block; border: 0; padding: 1px 0; }
  .fahrplan td:first-child { font-weight: 700; color: #3B4A2F; font-size: 16px; }
  .fahrplan td[data-l]:not(:first-child)::before { content: attr(data-l) ": "; color: #5E6652; font-weight: 700; }
}
</style>"""


def stunden(fp):
    """Anzahl der Unterrichtsstunden, die der Fahrplan vorsieht."""
    return sum(1 for z in (fp or {}).get("zeilen", []) if z["wann"].lower().startswith("stunde"))


def jahresplan(bloecke, ordner, kennung):
    """(tatsächlich, ursprünglich) geplante Stunden aus dem Jahresplan für »E4« oder »E4–E5«; None, wenn unbekannt."""
    nrn = [int(x) for x in re.findall(r"E(\d+)", kennung or "")]
    if len(nrn) == 2 and "–" in kennung:
        nrn = list(range(nrn[0], nrn[1] + 1))
    ist = brutto = 0
    gefunden = False
    for b in bloecke.get(ordner, []):
        for n in nrn:
            if f"E{n}" in b.get("stunden", {}):
                gefunden = True
                ist += b["stunden"][f"E{n}"]
                brutto += b.get("brutto", {}).get(f"E{n}", 0)
    return (ist, brutto) if gefunden else None


def html_fahrplan(u):
    fp = u.get("fahrplan")
    if not fp or not fp.get("zeilen"):
        return None
    z = fp["zeilen"]
    spalten = [("wann", "Wann"), ("lesen", "Das machen wir"), ("aufgaben", "Aufgaben"), ("wie", "Wie"), ("abgabe", "Abgabe")]
    spalten = [(k, t) for k, t in spalten if k in ("wann", "lesen") or any(r.get(k) for r in z)]
    n = stunden(fp)
    kopf = '<div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2>'
    if n:
        kopf += f'<p class="std">Dafür {"ist" if n == 1 else "sind"} {n} {"Stunde" if n == 1 else "Stunden"} eingeplant.</p>'
    if fp.get("text"):
        kopf += f'<p>{esc(fp["text"])}</p>'
    th = "".join(f"<th>{t}</th>" for _, t in spalten)
    tr = "".join("<tr>" + "".join(f'<td data-l="{t}">{esc(r.get(k) or "–")}</td>' for k, t in spalten) + "</tr>" for r in z)
    return f'{A}{CSS}<section class="fahrplan">{kopf}<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></section>{E}'


ANKER = {"theorie.html": '<section class="part" id="einstieg"', "aufgaben.html": '<div class="progress">'}


def einbauen(u, root):
    """Fahrplan in theorie.html und aufgaben.html der Einheit setzen (oder entfernen, wenn keiner eingetragen ist)."""
    neu = html_fahrplan(u)
    geaendert = []
    for seite, anker in ANKER.items():
        if seite not in u["seiten"]:
            continue
        pfad = os.path.join(root, u["ordner"], seite)
        s = open(pfad, encoding="utf-8").read()
        if A in s:
            i, j = s.index(A), s.index(E) + len(E)
        else:  # alter, von Hand eingebauter Fahrplan ohne Markierung
            i = s.find('<section class="fahrplan"')
            j = s.index("</section>", i) + len("</section>") if i >= 0 else -1
        if i >= 0:
            t = s[:i] + (neu or "") + s[j:]
        elif neu and anker in s:
            k = s.index(anker)
            t = s[:k] + neu + s[k:]
        else:
            continue
        if t != s:
            open(pfad, "w", encoding="utf-8").write(t)
            geaendert.append(seite)
    return geaendert
