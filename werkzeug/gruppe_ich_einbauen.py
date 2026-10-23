"""Gruppen-Versuchsseiten: Feld »Ich gebe ab als (dein Nachname)« + eigener Dateiname je Gruppenmitglied.
Aufruf im Repository-Ordner: python3 werkzeug/gruppe_ich_einbauen.py   (wiederholbar: Seiten mit Feld #ich werden übersprungen)

Problem: Auf den Versuchsseiten steht im Feld »Namen der Gruppe« z. B. »Huber, Maier, Novak«. Der Dateiname nahm bisher nur den
ersten Namen – alle drei Gruppenmitglieder hatten also dieselbe Datei »K1.5a-Versuche-Huber.pdf«. Jedes Mitglied gibt seine eigene
PDF in LMS ab (damit jeder die Mitschrift hat), also muss die PDF sagen, wer sie abgibt.

Neu: Feld #ich (Pflicht vor »PDF erstellen«), Dateiname »K1.5a-Versuche-<Nachname-der-abgebenden-Person>.pdf«, Zeile »Abgabe durch: …«
im PDF-Kopf und im Kopier-Text. Das Feld liegt im selben Speicherstand S (Eigenschaft S.ich); der Schlüssel (const KEY) bleibt gleich,
alte Speicherstände ohne S.ich laden wie bisher (Standardwert leer).

Betrifft die Versuchsseiten mit »Namen der Gruppe« (1AB, 2AB, 4AB) und die Vorlage werkzeug/vorlagen/vs_body.html.
Nicht betroffen: 3AB Gruppe und 5AB Projekt (dort trägt jeder »Dein Name« ein und gibt allein ab)."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FELD = ('<div style="grid-column:1/-1"><label class="lbl" for="ich">Ich gebe diese PDF ab als (dein Nachname)</label>'
        '<input type="text" id="ich" autocomplete="family-name" placeholder="z. B. Maier">'
        '<div style="font-size:14px;color:var(--muted);margin-top:4px">Jeder aus der Gruppe gibt seine eigene PDF in LMS ab – so hat jeder die Mitschrift.</div></div>')

# (Name, Muster als Regex, Ersatz) – jedes Muster muss in einer Seite genau einmal passen
PATCHES = [
    ("Feld im Kopf",
     r'(<div><label class="lbl" for="klasse">Klasse</label><select id="klasse">.*?</select></div>)',
     lambda m: m.group(1) + FELD),
    ("Standardwert S.ich",
     r'let S = \{ name: "", klasse: "", a: \{\} \}',
     lambda m: 'let S = { name: "", ich: "", klasse: "", a: {} }'),
    ("Hinweis fehlende Angaben",
     r'(if \(!S\.name\.trim\(\)\) who\.push\("Namen der Gruppe"\);)',
     lambda m: m.group(1) + ' if (!(S.ich || "").trim()) who.push("Ich gebe ab als");'),
    ("Kopier-Text",
     r'"Gruppe: " \+ \(S\.name \|\| ""\) \+ " · Klasse: "',
     lambda m: '"Gruppe: " + (S.name || "") + " · Abgabe durch: " + (S.ich || "") + " · Klasse: "'),
    ("PDF-Kopf",
     r'(d\.text\("Datum: " \+ new Date\(\)\.toLocaleDateString\("de-AT"\), W - M, y \+ 4, \{ align: "right" \}\);)\n(\s*)(y \+= 6; d\.setDrawColor)',
     lambda m: (m.group(1) + '\n' + m.group(2) + 'y += 5; d.setFont("C", "normal"); d.setFontSize(11); d.setTextColor(...ink); '
                'd.text(clean("Abgabe durch: " + (S.ich || "—")), M, y + 4);\n' + m.group(2) + m.group(3))),
    ("Prüfung vor PDF",
     r'(if \(!S\.name\.trim\(\)\) \{ say\("err", "Bitte zuerst oben die Namen der Gruppe eintragen\."\); \$\("#name"\)\.focus\(\); return; \})',
     lambda m: m.group(1) + ' if (!(S.ich || "").trim()) { say("err", "Bitte oben eintragen, wer von euch diese PDF abgibt (dein Nachname). '
                'Jeder aus der Gruppe gibt seine eigene PDF in LMS ab."); $("#ich").focus(); return; }'),
    ("Dateiname",
     r'(const filename = "[^"]*" \+ )slug\(S\.name\)',
     lambda m: m.group(1) + 'slug(S.ich)'),
    ("Eingabe-Ereignis",
     r'(nameI\.addEventListener\("input", \(\) => \{ S\.name = nameI\.value; mark\(nameI\); update\(\); save\(\); \}\);)',
     lambda m: m.group(1) + '\nconst ichI = $("#ich"); ichI.value = S.ich || ""; mark(ichI);\n'
                            'ichI.addEventListener("input", () => { S.ich = ichI.value; mark(ichI); update(); save(); });'),
]


def anwenden(s):
    """Gibt (neuer Text, [fehlende Patches]) zurück."""
    fehlt = []
    for name, muster, ersatz in PATCHES:
        treffer = list(re.finditer(muster, s, flags=re.S))
        if len(treffer) != 1:
            fehlt.append(f"{name} ({len(treffer)}×)")
            continue
        m = treffer[0]
        s = s[:m.start()] + ersatz(m) + s[m.end():]
    return s, fehlt


def lesen(f):
    with open(f, encoding="utf-8", newline="") as fh:
        return fh.read()


ziele = [f for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "versuche.html"))) if "Namen der Gruppe" in lesen(f)]
vorlage = os.path.join(ROOT, "werkzeug", "vorlagen", "vs_body.html")
fehler = []
for f in ziele + [vorlage]:
    rel = os.path.relpath(f, ROOT)
    s = lesen(f)
    if 'id="ich"' in s:
        print("schon eingebaut:", rel); continue
    neu, fehlt = anwenden(s)
    if fehlt:
        fehler.append(f"{rel}: nicht angewendet: " + ", ".join(fehlt)); continue
    with open(f, "w", encoding="utf-8", newline="") as fh:
        fh.write(neu)
    print("Feld »Ich gebe ab als« eingebaut:", rel)
if fehler:
    print("\nFEHLER (nichts davon wurde geschrieben):"); [print(" -", x) for x in fehler]; sys.exit(1)
