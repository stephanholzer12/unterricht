"""Kadettenansicht v2: sichtbare Stundenübersicht und klare Materialwege.

Arbeitsaufträge kommen ausschließlich aus dem vorhandenen Fahrplan. Keine
Bewertungsregeln, Eingaben, Versuchs-IDs oder Speicherschlüssel ändern.
"""
import html
import os
import re

esc = html.escape
CSS_DATEI = "kadetten-layout-v2.css"
JS_DATEI = "kadetten-navigation-v2.js"
NAMEN = {"theorie.html": "Theorie", "aufgaben.html": "Arbeitsblatt", "versuche.html": "Versuche",
         "quiz.html": "Quiz", "vertiefung.html": "Vertiefung", "uebung.html": "Übung",
         "projekt.html": "Projekt", "gruppe.html": "Gruppenarbeit", "kurz.html": "Gruppe kompakt",
         "teststoff.html": "Teststoff"}
REIHE = ["theorie.html", "aufgaben.html", "versuche.html", "vertiefung.html", "uebung.html",
         "projekt.html", "gruppe.html", "kurz.html", "teststoff.html", "quiz.html"]


def ressourcen(u, klasse="ks-ressourcen"):
    beschreibung = {"theorie.html": "Lesen und nachschlagen", "aufgaben.html": "Aufgaben bearbeiten und PDF erstellen",
                    "quiz.html": "Wissen selbst prüfen", "versuche.html": "Anleitung und Protokoll",
                    "teststoff.html": "Prüfungsumfang nachlesen"}
    out, weitere = [], []
    for s in REIHE:
        if s not in u["seiten"]:
            continue
        text = NAMEN[s]
        if s not in ("theorie.html", "aufgaben.html", "quiz.html"):
            weitere.append(f'<a href="{esc(u["unter"])}/{s}">{text}</a>')
            continue
        sub = beschreibung.get(s, "Nach Arbeitsauftrag bearbeiten")
        out.append(f'<a class="ks-material" href="{esc(u["unter"])}/{s}"><strong>{text}</strong><span>{sub}</span></a>')
    return f'<div class="{klasse}">{"".join(out)}</div>' + (f'<div class="ks-weitere" aria-label="Weitere Materialien">{"".join(weitere)}</div>' if weitere else "")


def arbeitsauftrag(u):
    zeilen = (u.get("fahrplan") or {}).get("zeilen", [])
    if not zeilen:
        return '<p class="note">Beachte den Arbeitsauftrag deines Lehrers auf dem Arbeitsblatt.</p>'
    extra = lambda r: bool(re.search(r"für schnelle|zusatz|optional", r.get("wann", ""), re.I))
    pflicht, zusatz = [r for r in zeilen if not extra(r)], [r for r in zeilen if extra(r)]
    out = ['<section class="ks-auftrag" aria-label="Arbeitsauftrag"><h3>Was soll ich machen?</h3>'
           '<p class="meta">Alle Stunden und Arbeitsphasen auf einen Blick. Beginne bei der Phase, die gerade dran ist.</p>']
    if pflicht:
        out.append('<table class="ks-stundenplan"><caption class="ks-visuell-versteckt">Stundenübersicht: Arbeitsauftrag, Aufgaben und Abgabe</caption>'
                   '<thead><tr><th scope="col">Phase</th><th scope="col">Lesen und bearbeiten</th>'
                   '<th scope="col">Aufgaben</th><th scope="col">Abgabe</th></tr></thead><tbody>')
        for r in pflicht:
            out.append(f'<tr><th scope="row">{esc((r["klasse"] + " · " if r.get("klasse") else "") + r["wann"] + (" · " + r["datum"] if r.get("datum") else ""))}</th><td data-label="Lesen und bearbeiten">{esc(r["lesen"])}')
            if r.get("wie"):
                out.append(f'<p class="ks-arbeitsweise"><strong>Arbeitsweise:</strong> {esc(r["wie"])}</p>')
            abgabe = r.get("abgabe", "–")
            abgabe = "Keine Abgabe in dieser Phase angegeben" if abgabe == "–" else abgabe
            aufgaben = r.get("aufgaben", "–")
            out.append(f'</td><td data-label="Aufgaben">{esc(aufgaben)}</td><td data-label="Abgabe">{esc(abgabe)}</td></tr>')
        out.append('</tbody></table>')
    if zusatz:
        out.append('<details class="mehr ks-zusatzauftrag"><summary>Zusatz · nur nach Auftrag oder wenn Zeit bleibt</summary><div><ul>')
        for r in zusatz:
            out.append(f'<li><strong>{esc((r["klasse"] + " · " if r.get("klasse") else "") + r["wann"] + (" · " + r["datum"] if r.get("datum") else ""))}</strong>: {esc(r["lesen"])}'
                       + (f' · Aufgaben {esc(r["aufgaben"])}' if r.get("aufgaben") else "") + '</li>')
        out.append('</ul></div></details>')
    if (u.get("fahrplan") or {}).get("text"):
        out.append(f'<details class="mehr"><summary>Hinweise zum gesamten Ablauf</summary><div>{esc(u["fahrplan"]["text"])}</div></details>')
    out.append('</section>')
    return "".join(out)


def start(u, buch=""):
    ident = "jetzt-" + u["unter"]
    return (f'<section class="card ks-aktuell" aria-labelledby="{esc(ident)}"><div class="eyebrow">AKTUELLES THEMA</div>'
            f'<h2 id="{esc(ident)}">{esc(u["titel"])}</h2><p class="meta">{esc(u["kapitel"])}'
            + (f' · {esc(buch)}' if buch else "") + '</p>' + ressourcen(u) + arbeitsauftrag(u) + '</section>')


def kopf(s):
    """Nur die drei Klassenübersichten erhalten diese Gestaltung, nie die Lehrer-Seite."""
    s = s.replace('</head>', f'<link rel="stylesheet" href="../gemeinsam/{CSS_DATEI}">\n{skript()}\n</head>')
    s = s.replace('<body>', '<body class="ks-klassenseite">', 1)
    s = s.replace('>Übersicht</a>', '>Start</a>').replace('>Themen</a>', '>Alle Themen</a>')
    return s


def skript():
    return f'<script src="../gemeinsam/{JS_DATEI}" defer></script>'


def einbauen(einheiten, root):
    """Wiederholbarer Einbau in Materialseiten, ohne ihre vorhandenen Skripte umzuschreiben."""
    marker = lambda art: re.compile((r'\n' if art == 'navigation' else '') + rf'<!-- ks-{art}:start -->.*?<!-- ks-{art}:end -->\n?', re.S)
    for e in einheiten:
        gruppe = e["ordner"].split('/')[0]
        for seite in e["seiten"]:
            pfad = os.path.join(root, e["ordner"], seite)
            if not os.path.isfile(pfad):
                continue
            with open(pfad, encoding="utf-8", newline="") as f:
                alt = f.read()
            s = alt
            for art in ("kopf", "navigation", "ende"):
                s = marker(art).sub('', s)
            css = f'<!-- ks-kopf:start --><link rel="stylesheet" href="../../gemeinsam/{CSS_DATEI}"><!-- ks-kopf:end -->\n'
            s = s.replace('</head>', css + '</head>', 1)
            def body(m):
                tag = m[0]
                if not re.search(r'\bclass=', tag):
                    tag = tag[:-1] + ' class="ks-materialseite">'
                elif 'ks-materialseite' not in tag:
                    tag = re.sub(r'\bclass="', 'class="ks-materialseite ', tag, count=1)
                nav = (f'<nav class="ks-topnav" aria-label="Zur eigenen Klasse"><a href="../index.html">'
                       f'← {esc(e["fach"])} {esc(e["klasse"])} · Start</a><span>{esc(NAMEN.get(seite, seite))}</span></nav>'
                       '<nav class="ks-materialnav" aria-label="Material dieser Einheit">')
                for ziel in REIHE:
                    if ziel not in e["seiten"]:
                        continue
                    cur = ' aria-current="page"' if ziel == seite else ""
                    nav += f'<a href="{ziel}"{cur}>{esc(NAMEN[ziel])}</a>'
                if 'id="abgabe"' in s:
                    nav += '<a class="ks-zur-abgabe" href="#abgabe">Zur PDF-Abgabe</a>'
                nav += '</nav>'
                return tag + '\n<!-- ks-navigation:start -->' + nav + '<!-- ks-navigation:end -->\n'
            s = re.sub(r'<body\b[^>]*>', body, s, count=1)
            ende = (f'<!-- ks-ende:start --><nav class="ks-ende" aria-label="Zurück zur Klassenübersicht">'
                    f'<a href="../index.html">← Zurück zu {esc(e["fach"])} {esc(e["klasse"])}</a></nav>'
                    f'<script src="../../gemeinsam/{JS_DATEI}" defer></script><!-- ks-ende:end -->\n')
            s = s.replace('</body>', ende + '</body>', 1)
            if s != alt:
                with open(pfad, 'w', encoding='utf-8', newline='') as f:
                    f.write(s)

