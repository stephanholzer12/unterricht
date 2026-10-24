"""Teststoff als Handy-Seite – aus DERSELBEN Datei wie die Word-Seite (werkzeug/teststoff/daten/*.json), keine zweite Stoffliste.

Aufruf:  python3 werkzeug/teststoff/handyseite.py            baut für alle Einheiten mit »teststoff« in einheiten.json
         python3 werkzeug/teststoff/handyseite.py --entwurf <Zielordner>   Entwurf MIT offenen Stellen (nur zum Ansehen, nicht veröffentlichen)

Regel: Solange im JSON noch [[gelbe Stellen]] stehen (Stephan ergänzt), wird KEINE Seite veröffentlicht – sonst sähen die
Kadetten unfertigen Stoff. Die Seite entsteht als <ordner>/teststoff.html (neben quiz.html). Sie erscheint auf der Klassenseite,
sobald »teststoff.html« in der Seitenliste der Einheit steht (einheiten.json). Antworten: nur die Selbsteinschätzung
(sicher / fast / noch nicht), Speicher-Schlüssel 26-27-<Klasse>-<Test>-Teststoff-Check-v1; sonst wird nichts gespeichert."""
import html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
esc = html.escape


def offene(d):
    """Alle [[gelben Stellen]] in den Textwerten (nicht die JSON-Klammern verschachtelter Listen)."""
    out = []
    def lauf(x):
        if isinstance(x, str): out.extend(re.findall(r"\[\[(.*?)\]\]", x))
        elif isinstance(x, list): [lauf(i) for i in x]
        elif isinstance(x, dict): [lauf(i) for i in x.values()]
    lauf(d); return out


def md(s, entwurf=False):
    s = esc(str(s))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\[\[(.*?)\]\]", (r'<mark>\1</mark>' if entwurf else r"\1"), s)


def seite(d, ordner, entwurf=False):
    kl = ordner.split("-")[0].upper()
    nr = re.search(r"test(\d+)", ordner)
    key = f"26-27-{kl}-Test{nr.group(1) if nr else '1'}-Teststoff-Check-v1"
    m = lambda x: md(x, entwurf)
    durch = "".join(
        f'<div class="row"><span class="nr">{m(r[0])}</span><div><b>{m(r[1])}</b><div class="meta">Buch {m(r[2])}</div>'
        f'<div class="meta">{m(r[3])}</div><div class="meta">Aufgaben: {m(r[4])}</div></div></div>' for r in d["durchgenommen"])
    kann = "".join(
        f'<div class="ziel" data-z="{i}"><p>{m(r[1])}</p>' + (f'<p class="begr"><b>Begriffe:</b> {m(r[2])}</p>' if len(r) > 2 and r[2] else "")
        + '<div class="chips" role="group" aria-label="Selbstcheck">'
        + "".join(f'<button type="button" class="chip" data-z="{i}" data-v="{v}" aria-pressed="false">{v}</button>' for v in ("sicher", "fast", "noch nicht"))
        + "</div></div>" for i, r in enumerate(d["koennen"]))
    formeln = ""
    if d.get("formeln"):
        formeln = '<section class="card"><h2>Formeln</h2><table>' + "".join(f"<tr><th>{m(r[0])}</th><td>{m(r[1])}</td></tr>" for r in d["formeln"]) + "</table>" + (f'<p class="meta">{m(d["tipp"])}</p>' if d.get("tipp") else "") + "</section>"
    kein = '<section class="card"><h2>Kein Teststoff</h2><ul>' + "".join(f"<li>{m(x)}</li>" for x in d.get("kein_teststoff", [])) + "</ul></section>" if d.get("kein_teststoff") else ""
    links = "".join(f'<a class="btn" href="{esc(q["url"])}"><b>{esc(q["titel"])}</b> – {esc(q["text"])}</a>' for q in d.get("qr", []))
    warn = '<p class="warn">ENTWURF – gelbe Stellen sind noch offen. Nicht an Kadetten weitergeben.</p>' if entwurf else ""
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Teststoff {esc(kl)}</title>
<style>
:root{{--bg:#EEF3E4;--card:#fff;--ink:#1F2A1C;--olive:#3B4A2F;--green:#7FA83A;--teal:#2E7D8C;--line:#D3DCC2;--muted:#5E6652;--head:Cambria,Georgia,serif}}
@media(prefers-color-scheme:dark){{:root{{color-scheme:light}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:18px/1.45 Calibri,"Segoe UI",sans-serif}}
header{{background:var(--olive);color:#fff;padding:18px 16px}}header div{{max-width:720px;margin:0 auto}}
.eyebrow{{font-weight:700;font-size:14px;letter-spacing:.04em;opacity:.85}}h1{{font:700 28px/1.15 var(--head);margin:4px 0 0}}
main{{max-width:720px;margin:0 auto;padding:16px 16px 48px;display:grid;gap:14px}}
.card{{background:var(--card);border-radius:14px;padding:14px 16px;box-shadow:0 2px 6px rgba(31,42,28,.12)}}
h2{{font:700 22px/1.2 var(--head);color:var(--olive);margin:0 0 8px}}.meta{{color:var(--muted);font-size:15px}}
.row{{display:flex;gap:12px;padding:8px 0;border-top:1px solid var(--line)}}.row:first-of-type{{border-top:0}}
.nr{{flex:0 0 32px;height:32px;border-radius:50%;background:var(--olive);color:#fff;font-weight:700;display:grid;place-items:center}}
.ziel{{border:1px solid var(--line);border-radius:12px;padding:10px 12px;display:grid;gap:6px;margin:8px 0}}.ziel p{{margin:0}}.begr{{font-size:15px;color:var(--muted)}}
.chips{{display:flex;gap:8px;flex-wrap:wrap}}.chip{{font:inherit;font-size:16px;font-weight:700;color:var(--olive);background:#fff;border:2px solid var(--line);border-radius:999px;padding:6px 14px;min-height:44px;cursor:pointer}}
.chip[aria-pressed="true"][data-v="sicher"]{{background:#E6F0D3;border-color:var(--green)}}.chip[aria-pressed="true"][data-v="fast"]{{background:#FFF1D6;border-color:#D9772B}}.chip[aria-pressed="true"][data-v="noch nicht"]{{background:#F6E3DF;border-color:#8C3B2E}}
a.btn{{display:block;text-decoration:none;color:#fff;background:var(--teal);border-radius:10px;padding:10px 16px;margin:6px 0}}
table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;padding:6px;border-top:1px solid var(--line)}}
mark{{background:#FFE98A}}.warn{{background:#FFE98A;padding:8px 12px;border-radius:10px;font-weight:700;margin:0}}
</style></head><body>
<header><div><div class="eyebrow">{md(d["kopf"])}</div><h1>{md(d["titel"])}</h1></div></header>
<main>{warn}
<section class="card"><h2>Wann und was?</h2><p><b>Termin:</b> {m(d["termin"])}</p><p><b>Stoff:</b> {m(d["stoff"])}</p></section>
<section class="card"><h2>Das haben wir durchgenommen</h2>{durch}</section>
<section class="card"><h2>Das musst du können</h2><p class="meta">Tippe ehrlich an – das bleibt nur auf deinem Handy.</p>{kann}</section>
{formeln}{kein}
<section class="card"><h2>Üben</h2>{links}</section>
</main>
<script>(function(){{var KEY = "{key}", S = {{}};try{{S=JSON.parse(localStorage.getItem(KEY)||"{{}}")||{{}};}}catch(e){{S={{}};}}var chips=document.querySelectorAll(".chip[data-z]");function paint(){{chips.forEach(function(c){{c.setAttribute("aria-pressed",String(S[c.dataset.z]===c.dataset.v));}});}}chips.forEach(function(c){{c.addEventListener("click",function(){{S[c.dataset.z]=S[c.dataset.z]===c.dataset.v?null:c.dataset.v;paint();try{{localStorage.setItem(KEY,JSON.stringify(S));}}catch(e){{}}}});}});paint();}})();</script>
</body></html>
"""


def main():
    einh = json.load(open(os.path.join(ROOT, "werkzeug", "einheiten.json"), encoding="utf-8"))
    if "--entwurf" in sys.argv:
        ziel = sys.argv[sys.argv.index("--entwurf") + 1]
        os.makedirs(ziel, exist_ok=True)
    for e in einh:
        if not e.get("teststoff"): continue
        d = json.load(open(os.path.join(ROOT, e["teststoff"]), encoding="utf-8"))
        off = offene(d); ziel_datei = os.path.join(ROOT, e["ordner"], "teststoff.html")
        if "--entwurf" in sys.argv:
            open(os.path.join(ziel, e["ordner"].split("/")[0] + "-teststoff-entwurf.html"), "w", encoding="utf-8").write(seite(d, e["ordner"], True))
            print("Entwurf:", e["ordner"], f"({len(off)} offene Stellen)"); continue
        if off:
            if os.path.exists(ziel_datei): os.remove(ziel_datei)   # nie unfertigen Stoff veröffentlichen
            print(f"Teststoff-Handyseite {e['ordner']}: wartet auf Ergänzungen ({len(off)} gelbe Stellen)")
        else:
            open(ziel_datei, "w", encoding="utf-8").write(seite(d, e["ordner"]))
            print("Teststoff-Handyseite gebaut:", e["ordner"] + "/teststoff.html")


if __name__ == "__main__":
    main()
