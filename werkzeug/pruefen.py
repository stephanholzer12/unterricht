"""Automatische Kontrolle der Seiten (läuft bei jedem Push über .github/workflows/pruefen.yml, lokal: python3 werkzeug/pruefen.py).
Prüft für alle veröffentlichten Seiten (*/*/*.html, ohne werkzeug/):
 1. Kein Fremdserver für Schriften/Skripte/Bilder (link, script, img mit http-Adresse).
 2. Kein Zugangs-Token im Text (ghp_…, github_pat_…).
 3. Alle Skripte in der Seite sind syntaktisch in Ordnung (node --check).
 4. Jede Seite mit PDF-Abgabe (jsPDF) hat den Speicherstatus- und den PDF-Erinnerungs-Baustein und nutzt die gemeinsame PDF-Datei.
 5. Speicherschlüssel (const KEY = "…"): ein Schlüssel, der gegenüber dem vorigen Stand verschwunden ist, wäre eine Umbenennung –
    dann verlieren Kadetten ihre Antworten. Wird gemeldet (Fehler), außer die Commit-Nachricht enthält [schluessel-ok].
Exit-Code 1 bei Fehlern."""
import glob, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fehler = []
KEY_RE = re.compile(r'(?:const|var|let)\s+KEY\s*=\s*"([^"]+)"')
seiten = [f for f in sorted(glob.glob(os.path.join(ROOT, "*", "*", "*.html"))) if not os.path.relpath(f, ROOT).startswith("werkzeug")]

def rel(f): return os.path.relpath(f, ROOT)

for f in seiten:
    s = open(f, encoding="utf-8").read()
    if re.search(r'<(?:link|script|img)\b[^>]*\b(?:src|href)="https?://(?!github\.com)', s):
        fehler.append(f"{rel(f)}: lädt etwas von einem Fremdserver (Schriften/Skripte sollen lokal liegen)")
    if re.search(r'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}', s):
        fehler.append(f"{rel(f)}: enthält etwas, das wie ein GitHub-Token aussieht")
    if "jsPDF" in s and "speicherstatus:start" not in s:
        fehler.append(f"{rel(f)}: PDF-Seite ohne Speicherstatus (python3 werkzeug/speicherstatus_einbauen.py ausführen)")
    if "/* jsPDF 2.5.1 (MIT) */" in s:
        fehler.append(f"{rel(f)}: PDF-Programm steckt noch in der Seite (python3 werkzeug/nach_dem_bauen.py ausführen)")
    if "jsPDF" in s and "pdferinnerung:start" not in s:
        fehler.append(f"{rel(f)}: PDF-Seite ohne PDF-Erinnerung (python3 werkzeug/pdf_erinnerung_einbauen.py ausführen)")
    for i, m in enumerate(re.finditer(r"<script(?![^>]*\bsrc=)(?![^>]*type=\"(?:application/json|text/template))[^>]*>(.*?)</script>", s, re.S)):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as t:
            t.write(m.group(1)); p = t.name
        try:
            r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
            if r.returncode: fehler.append(f"{rel(f)}: Skript Nr. {i+1} hat einen Syntaxfehler: " + r.stderr.strip().splitlines()[-1][:120])
        except FileNotFoundError:
            print("Hinweis: node fehlt, Skriptprüfung übersprungen"); break
        finally:
            os.unlink(p)

# Speicherschlüssel gegenüber dem vorigen Stand
def keys_von(ref):
    out = set()
    try:
        files = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
        for n in files:
            if n.endswith(".html") and n.count("/") == 2 and not n.startswith("werkzeug/"):
                t = subprocess.run(["git", "show", f"{ref}:{n}"], cwd=ROOT, capture_output=True, text=True).stdout
                out |= set(KEY_RE.findall(t))
    except Exception:
        return None
    return out
alt = keys_von("HEAD~1")
neu = set(k for f in seiten for k in KEY_RE.findall(open(f, encoding="utf-8").read()))
msg = subprocess.run(["git", "log", "-1", "--format=%B"], cwd=ROOT, capture_output=True, text=True).stdout
if alt is not None and "[schluessel-ok]" not in msg:
    for k in sorted(alt - neu):
        fehler.append(f"Speicherschlüssel verschwunden/umbenannt: {k} (Kadetten würden ihre Antworten verlieren; beabsichtigt? dann [schluessel-ok] in die Commit-Nachricht)")

print(f"{len(seiten)} Seiten geprüft, {len(neu)} Speicherschlüssel.")
if fehler:
    print("\nFEHLER:"); [print(" -", x) for x in fehler]; sys.exit(1)
print("Alles in Ordnung.")
