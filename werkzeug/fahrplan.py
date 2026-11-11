"""Fahrplan jeder Einheit: Was passiert in Stunde 1, Stunde 2 …?

Quelle ist das Feld »fahrplan« einer Einheit in einheiten.json:
  "fahrplan": {"text": "kurzer Satz (optional)",
               "zeilen": [{"wann": "Stunde 1", "datum": "Di 3.11. (optional)", "lesen": "Einstieg + Teil 1 · …", "aufgaben": "1–4",
                           "zeit": "Aufgaben ca. 18 min (optional)", "wie": "ohne Handy: … (optional)", "abgabe": "–"}, …]}
Die Spalten »Datum« und »Zeit« erscheinen nur, wenn mindestens eine Zeile sie hat.
Zeilen, deren »wann« mit »Stunde« beginnt, zählen als Unterrichtsstunden. Andere Zeilen (»Für Schnelle«,
»Hausübung«) sind Zusatz.

build_index.py baut den Fahrplan bei jedem Lauf in theorie.html und aufgaben.html der Einheit ein
(zwischen den Markierungen <!--FAHRPLAN--> und <!--/FAHRPLAN-->) und zeigt ihn auf der Klassenseite.
Die im Jahresplan geplanten Stunden (bloecke.json, Felder »stunden« und »brutto«) werden auf der
Lehrer-Seite mit den Stunden des Fahrplans verglichen.

Getrennte Stundenpläne (z. B. 4AK und 4BK teilen sich eine Klassenseite): Jede Zeile darf zusätzlich
»klasse": "4AK" haben. Dann zeigt der Fahrplan je Klasse eine eigene Tabelle, und als Stundenzahl zählt
die Klasse mit den meisten Stunden-Zeilen. Zeilen ohne »klasse« gelten für alle. Einheiten ohne dieses
Feld bleiben genau wie bisher.

Kompakte Ansicht (Stephan, 11.11.2026, Probe an K2.1 Kräfte 1AB): »fahrplan": {"ansicht": "kompakt", …}.
Die Kadetten tippen ihre Klasse an (wird im Browser gemerkt), groß steht nur »Diese Stunde« (nächste geplante Stunde
nach Datum) mit drei Zeilen: Lesen/Tun · Im Arbeitsblatt · Abgabe, dazu die Marke (»marke«: SELBSTSTUDIUM, VERSUCH …).
Alle anderen Stunden sind zugeklappt, je eine Zeile. Keine Minuten. Einheiten ohne »ansicht« bleiben unverändert.
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
    """Anzahl der Unterrichtsstunden, die der Fahrplan vorsieht (bei getrennten Klassen: die größte Zahl)."""
    je = stunden_je_klasse(fp)
    if je:
        return max(je.values())
    return sum(1 for z in (fp or {}).get("zeilen", []) if z["wann"].lower().startswith("stunde"))


def stunden_je_klasse(fp):
    """{"4AK": 5, "4BK": 4} bei getrennten Stundenplänen, sonst None."""
    z = (fp or {}).get("zeilen", [])
    klassen = [r["klasse"] for r in z if r.get("klasse")]
    if not klassen:
        return None
    out = {}
    for k in dict.fromkeys(klassen):
        out[k] = sum(1 for r in z if r["wann"].lower().startswith("stunde") and r.get("klasse") in (k, None))
    return out


def stunden_text(fp):
    """»4AK: 5 Stunden · 4BK: 4 Stunden« bzw. »2 Stunden«."""
    je = stunden_je_klasse(fp)
    wort = lambda n: f'{n} {"Stunde" if n == 1 else "Stunden"}'
    if je:
        return " · ".join(f"{k}: {wort(n)}" for k, n in je.items())
    return wort(stunden(fp))


def zeilen_label(r):
    """Beschriftung einer Zeile: »4AK · Stunde 2« bzw. »Stunde 2«."""
    return (r["klasse"] + " · " if r.get("klasse") else "") + r["wann"]


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


KOMPAKT_CSS = """<style>
.fp-kompakt .fp-wahl { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; margin: 4px 0 10px; font-weight: 700; color: #3B4A2F; }
.fp-kompakt .fp-wahl button { font: inherit; font-size: 17px; font-weight: 700; min-height: 44px; padding: 6px 18px; border-radius: 999px;
  border: 2px solid #3B4A2F; background: #fff; color: #3B4A2F; cursor: pointer; }
.fp-kompakt .fp-wahl button[aria-pressed="true"] { background: #3B4A2F; color: #fff; }
.fp-kompakt .fp-std { border: 2px solid #7FA83A; border-radius: 12px; padding: 10px 12px; background: #F4F7EC; display: grid; gap: 6px; }
.fp-kompakt .fp-kopf { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; font-size: 18px; font-weight: 700; color: #3B4A2F; }
.fp-kompakt .fp-marke { font-size: 13px; font-weight: 700; color: #fff; background: #2E7D8C; border-radius: 999px; padding: 2px 10px; }
.fp-kompakt .fp-zeile { display: grid; grid-template-columns: 30px 1fr; gap: 6px; font-size: 17px; line-height: 1.4; }
.fp-kompakt .fp-zeile b.n { display: inline-flex; width: 26px; height: 26px; border-radius: 50%; background: #7FA83A; color: #fff; align-items: center; justify-content: center; font-size: 15px; }
.fp-kompakt details { margin-top: 10px; } .fp-kompakt summary { cursor: pointer; font-weight: 700; color: #2E7D8C; min-height: 44px; display: flex; align-items: center; }
.fp-kompakt ol.fp-liste { margin: 4px 0 0; padding-left: 0; list-style: none; display: grid; gap: 4px; }
.fp-kompakt ol.fp-liste li { font-size: 16px; padding: 6px 8px; border-radius: 8px; background: #fff; border: 1px solid #D3DCC2; }
.fp-kompakt ol.fp-liste li.fp-jetzt { border: 2px solid #7FA83A; background: #F4F7EC; font-weight: 700; }
.fp-kompakt .fp-tipp { font-size: 16px; color: #5E6652; }
</style>"""
KOMPAKT_JS = """<script>
(function () {
  var box = document.currentScript.previousElementSibling, KEY = "fahrplan-klasse";
  var btns = box.querySelectorAll(".fp-wahl button"), teile = box.querySelectorAll(".fp-kl");
  function heute() { var d = new Date(); return d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate(); }
  function zeige(k) {
    btns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.k === k)); });
    teile.forEach(function (t) {
      t.hidden = t.dataset.k !== k; if (t.hidden) return;
      var std = t.querySelectorAll(".fp-std"), li = t.querySelectorAll("ol.fp-liste li"), n = 0, h = heute();
      for (var i = 0; i < std.length; i++) { var d = +std[i].dataset.d || 0; if (d && d >= h) { n = i; break; } if (i === std.length - 1) n = d && d < h ? i : 0; }
      std.forEach(function (s, i) { s.hidden = i !== n; }); li.forEach(function (l, i) { l.classList.toggle("fp-jetzt", i === n); });
    });
    var tipp = box.querySelector(".fp-tipp"); if (tipp) tipp.hidden = !!k;
  }
  var k = ""; try { k = localStorage.getItem(KEY) || ""; } catch (e) {}
  if (!box.querySelector('.fp-kl[data-k="' + k + '"]')) k = "";
  btns.forEach(function (b) { b.addEventListener("click", function () { try { localStorage.setItem(KEY, b.dataset.k); } catch (e) {} zeige(b.dataset.k); }); });
  zeige(k);
})();
</script>"""


def _iso(datum):
    """»Do 12.11. · geplant« -> 20261112 (Schuljahr: September bis Dezember 2026, Jänner bis August 2027)."""
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.", datum or "")
    if not m:
        return ""
    t, mo = int(m.group(1)), int(m.group(2))
    return str((2026 if mo >= 9 else 2027) * 10000 + mo * 100 + t)


def html_kompakt(u, mit_marken=True):
    fp = u["fahrplan"]; z = fp["zeilen"]
    klassen = list(dict.fromkeys(r["klasse"] for r in z if r.get("klasse")))
    out = ['<section class="fahrplan fp-kompakt"><div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2>',
           f'<p class="std">{esc(stunden_text(fp))} · die Daten sind geplant, die Reihenfolge zählt.</p>',
           '<div class="fp-wahl" role="group" aria-label="Deine Klasse">Deine Klasse:'
           + "".join(f'<button type="button" data-k="{esc(k)}" aria-pressed="false">{esc(k)}</button>' for k in klassen) + "</div>",
           '<p class="fp-tipp">Tippe deine Klasse an – dann siehst du, was in dieser Stunde dran ist.</p>']
    for k in klassen:
        rows = [r for r in z if r.get("klasse") == k]
        out.append(f'<div class="fp-kl" data-k="{esc(k)}" hidden>')
        for r in rows:
            kopf = esc(r["wann"]) + (f' · {esc(r["datum"])}' if r.get("datum") else "")
            mk = f'<span class="fp-marke">{esc(r["marke"])}</span>' if r.get("marke") else ""
            ab = r.get("abgabe") or "–"
            out.append(f'<div class="fp-std" data-d="{_iso(r.get("datum"))}" hidden><div class="fp-kopf">Diese Stunde: {kopf} {mk}</div>'
                       f'<div class="fp-zeile"><b class="n">1</b><span>{esc(r["lesen"])}</span></div>'
                       f'<div class="fp-zeile"><b class="n">2</b><span>Im Arbeitsblatt: Aufgabe {esc(r.get("aufgaben") or "–")}</span></div>'
                       f'<div class="fp-zeile"><b class="n">3</b><span>Abgabe: {esc("keine" if ab == "–" else ab)}</span></div></div>')
        out.append(f'<details><summary>Alle Stunden ({len(rows)})</summary><ol class="fp-liste">'
                   + "".join(f'<li>{esc(r["wann"])}{" · " + esc(r["datum"]) if r.get("datum") else ""}{" · " + esc(r["marke"]) if r.get("marke") else ""} – {esc(r["lesen"])}</li>' for r in rows)
                   + "</ol></details></div>")
    rest = [r for r in z if not r.get("klasse")]
    if rest:
        out.append("".join(f'<p class="fp-tipp" style="margin-top:8px"><b>{esc(r["wann"])}:</b> {esc(r["lesen"])} · Aufgaben {esc(r.get("aufgaben") or "–")}</p>' for r in rest))
    if fp.get("text"):
        out.append(f'<details><summary>So läuft die ganze Einheit</summary><p>{esc(fp["text"])}</p></details>')
    out.append("</section>")
    return CSS + KOMPAKT_CSS + "".join(out) + KOMPAKT_JS


def html_fahrplan(u):
    fp = u.get("fahrplan")
    if not fp or not fp.get("zeilen"):
        return None
    if fp.get("ansicht") == "kompakt" and any(r.get("klasse") for r in fp["zeilen"]):
        return A + html_kompakt(u) + E
    z = fp["zeilen"]
    spalten = [("wann", "Wann"), ("datum", "Datum"), ("lesen", "Das machen wir"), ("aufgaben", "Aufgaben"), ("zeit", "Zeit"), ("wie", "Wie"), ("abgabe", "Abgabe")]
    spalten = [(k, t) for k, t in spalten if k in ("wann", "lesen") or any(r.get(k) for r in z)]
    n = stunden(fp)
    je = stunden_je_klasse(fp)
    kopf = '<div class="eyebrow">So gehst du vor</div><h2>Dein Fahrplan</h2>'
    if je:
        kopf += f'<p class="std">Dafür sind eingeplant: {esc(stunden_text(fp))}. Schau in die Tabelle deiner Klasse.</p>'
    elif n:
        kopf += f'<p class="std">Dafür {"ist" if n == 1 else "sind"} {n} {"Stunde" if n == 1 else "Stunden"} eingeplant.</p>'
    if fp.get("text"):
        kopf += f'<p>{esc(fp["text"])}</p>'
    th = "".join(f"<th>{t}</th>" for _, t in spalten)
    zeile = lambda r: "<tr>" + "".join(f'<td data-l="{t}">{esc(r.get(k) or "–")}</td>' for k, t in spalten) + "</tr>"
    if not je:
        tr = "".join(zeile(r) for r in z)
        return f'{A}{CSS}<section class="fahrplan">{kopf}<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></section>{E}'
    teile = []
    for k in je:
        tr = "".join(zeile(r) for r in z if r.get("klasse") == k)
        teile.append(f'<h3 class="fp-klasse">{esc(k)}</h3><div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
    alle = [r for r in z if not r.get("klasse")]
    if alle:
        tr = "".join(zeile(r) for r in alle)
        teile.append(f'<h3 class="fp-klasse">Beide Klassen</h3><div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
    css = CSS.replace("</style>", ".fahrplan h3.fp-klasse { margin: 12px 0 4px; font-size: 19px; color: #fff; background: #3B4A2F; display: inline-block; border-radius: 8px; padding: 2px 12px; }\n</style>")
    return f'{A}{css}<section class="fahrplan">{kopf}{"".join(teile)}</section>{E}'


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
