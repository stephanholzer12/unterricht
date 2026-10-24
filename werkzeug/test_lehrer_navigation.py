"""Regression: Lehrerübersicht darf nicht in die Navigation der Kadetten gelangen.

Nach dem Bauen ausführen: python3 werkzeug/test_lehrer_navigation.py
"""
import json
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent
E = json.loads((ROOT / "werkzeug/einheiten.json").read_text(encoding="utf-8"))
GRUPPEN = {e["ordner"].split("/")[0] for e in E}
LEHRER = "lehrer-0f6eec.html"


class Seite(HTMLParser):
    def __init__(self, pfad):
        super().__init__()
        self.elemente = []
        self.feed(pfad.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        self.elemente.append((tag, dict(attrs)))

    def mit(self, tag=None, klasse=None, attr=None):
        return [a for t, a in self.elemente if (tag is None or t == tag)
                and (klasse is None or klasse in a.get("class", "").split())
                and (attr is None or attr in a)]


class NavigationTest(unittest.TestCase):
    def test_kadetten_sehen_keine_fachauswahl_oder_fremde_klasse(self):
        seiten = [ROOT / "index.html"]
        seiten += [p for g in GRUPPEN for p in (ROOT / g).rglob("*.html")]
        for seite in seiten:
            soup = Seite(seite)
            with self.subTest(seite=seite.relative_to(ROOT).as_posix()):
                self.assertFalse(soup.mit(attr="data-fach-filter"))
                self.assertNotIn("lehrer-suche", [e["id"] for e in soup.mit(attr="id")])
                for link in soup.mit(tag="a", attr="href"):
                    href = urlsplit(link["href"])
                    if href.scheme or href.netloc or not href.path:
                        continue
                    ziel = (seite.parent / unquote(href.path)).resolve()
                    try:
                        rel = ziel.relative_to(ROOT)
                    except ValueError:
                        continue
                    self.assertNotEqual(rel.as_posix(), LEHRER)
                    if rel.parts[0] in GRUPPEN:
                        self.assertEqual(rel.parts[0], seite.relative_to(ROOT).parts[0])

    def test_lehrer_links_qr_und_anker(self):
        soup = Seite(ROOT / LEHRER)
        self.assertEqual({b["data-fach-filter"] for b in soup.mit(attr="data-fach-filter")}, {e["fach"] for e in E})
        self.assertEqual({d["id"] for d in soup.mit(tag="details", klasse="kl")}, GRUPPEN)
        self.assertEqual(len(soup.mit(klasse="lehrer-zeile")), len(GRUPPEN))
        ids = [e["id"] for e in soup.mit(attr="id")]
        self.assertEqual(len(ids), len(set(ids)))
        for link in soup.mit(tag="a", attr="href"):
            href = urlsplit(link["href"])
            if href.scheme or href.netloc:
                continue
            if not href.path:
                self.assertIn(unquote(href.fragment), ids)
            else:
                self.assertTrue((ROOT / unquote(href.path)).exists(), link["href"])
        qr_urls = {b["data-url"] for b in soup.mit(klasse="qrbtn", attr="data-url")}
        for b in soup.mit(attr="data-qr-ziel"):
            self.assertIn(b["data-qr-ziel"], ids)
            self.assertTrue(any(u.endswith('/' + b["data-qr-ziel"] + '/') for u in qr_urls))


if __name__ == "__main__":
    unittest.main()
