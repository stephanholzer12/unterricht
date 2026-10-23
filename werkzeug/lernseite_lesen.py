"""Liest aus einer Theorie-Seite (theorie.html) die Bausteine für die Klassenübersicht:
Buchseiten, Lernziele (»Kann ich das?«), »Das Wichtigste in 5 Sätzen«, Fachbegriffe
und den Speicher-Schlüssel des Selbstchecks. Wird von build_index.py verwendet.
"""
import re
from bs4 import BeautifulSoup, NavigableString, Tag

ERLAUBT = {"strong", "b", "em", "i", "sub", "sup", "br"}


def sauber(el):
    """Inneres HTML eines Elements, nur mit einfachen Auszeichnungen (fett, kursiv, hoch/tief)."""
    def rec(n):
        if isinstance(n, NavigableString):
            return re.sub(r"[<>&]", lambda m: {"<": "&lt;", ">": "&gt;", "&": "&amp;"}[m.group(0)], str(n))
        if not isinstance(n, Tag):
            return ""
        innen = "".join(rec(c) for c in n.children)
        name = n.name.lower()
        if name == "br":
            return " "
        if name in ERLAUBT:
            name = {"b": "strong", "i": "em"}.get(name, name)
            return f"<{name}>{innen}</{name}>"
        return innen
    return re.sub(r"\s+", " ", rec(el)).strip()


def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ")).strip()


def folie(soup, titel):
    for h in soup.select(".slidehead h3"):
        if text(h).lower().startswith(titel.lower()):
            return h.find_parent("article") or h.find_parent("section")
    return None


def lesen(pfad):
    s = open(pfad, encoding="utf-8").read()
    key = re.search(r'var KEY = "([^"]+)"', s)
    soup = BeautifulSoup(s, "lxml")
    for t in soup(["script", "style"]):
        t.decompose()
    out = {"buch": "", "ziele": [], "ziele_sync": False, "kurz": [], "begriffe": [], "key": key.group(1) if key else ""}

    head = soup.find("header")
    if head:
        m = re.search(r"Buch S\. ?[\d–\-, ]+\d", text(head))
        if m:
            out["buch"] = m.group(0).replace("S.", "S.").strip()

    # Teile der Theorie-Seite (für das Inhaltsverzeichnis in der Übersicht)
    out["teile"] = []
    for sec in soup.select("section.part[id]"):
        eb = sec.select_one(".band .eyebrow")
        h2 = sec.find("h2")
        ebt = text(eb) if eb else ""
        if h2 and (re.match(r"(teil|stunde)\d", sec["id"]) or re.match(r"(Teil|Abschnitt|Stunde) ?\d", ebt)):
            seiten = re.search(r"Buch S\. ?[\d–\-, ]+\d", ebt)
            out["teile"].append({"id": sec["id"], "titel": text(h2), "buch": seiten.group(0) if seiten else ""})

    # Lernziele: bevorzugt aus »Kann ich das?« (dann passt die Nummer zum Selbstcheck der Theorie-Seite)
    k = folie(soup, "Kann ich das")
    if k and k.select(".ziel p"):
        out["ziele"] = [sauber(p) for p in k.select(".ziel p")]
        out["ziele_sync"] = bool(out["key"]) and bool(k.select("[data-z]"))
    else:
        z = folie(soup, "Das kannst du nach")
        if z:
            items = z.select("li") or z.select(".tile p")
            out["ziele"] = [sauber(i) for i in items]

    w = folie(soup, "Das Wichtigste")
    if w:
        out["kurz"] = [sauber(li) for li in w.select("li")]

    sec = soup.find(id="begriffe")
    if sec is None:
        for h2 in soup.select("section h2"):
            if "fachbegriff" in text(h2).lower():
                sec = h2.find_parent("section")
                break
    if sec is not None:
        for tr in sec.select("tbody tr"):
            zellen = tr.find_all(["th", "td"], recursive=False)
            if len(zellen) >= 2:
                b, d = text(zellen[0]), sauber(zellen[1])
                if b and d:
                    out["begriffe"].append((b, d))
        if not out["begriffe"]:  # Begriffe als Kacheln (h4 + p)
            for t in sec.select(".tile"):
                h, p = t.find(["h4", "strong"]), t.find("p")
                if h and p:
                    out["begriffe"].append((text(h), sauber(p)))
    # Ziele ohne Satzzeichen am Ende vereinheitlichen
    out["ziele"] = [z for z in out["ziele"] if z]
    return out


if __name__ == "__main__":
    import sys, glob
    for f in sys.argv[1:] or sorted(glob.glob("*/*/theorie.html")):
        d = lesen(f)
        print(f, "| Buch:", d["buch"], "| Ziele:", len(d["ziele"]), "sync" if d["ziele_sync"] else "", "| 5 Sätze:", len(d["kurz"]), "| Begriffe:", len(d["begriffe"]), "| Key:", d["key"][:30])
