"""Sichert Materialwege und Arbeitsaufträge der Kadettenansicht; nur Standardbibliothek."""
import html
import json
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlsplit

from test_lehrer_navigation import Seite

ROOT = Path(__file__).resolve().parent.parent
E = json.loads((ROOT / "werkzeug/einheiten.json").read_text(encoding="utf-8"))


class KadettenLayoutTest(unittest.TestCase):
    def test_navigationseinbau_ist_wiederholbar(self):
        import kadetten_layout as ks
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            p = root / '2ab-nawi/test/aufgaben.html'
            p.parent.mkdir(parents=True)
            p.write_text('<html><head></head><body>\n<section id="abgabe"></section><script>const KEY="behalten";</script>\n</body></html>', encoding='utf-8')
            daten = [{'ordner': '2ab-nawi/test', 'klasse': '2AB', 'fach': 'NAWI', 'seiten': ['aufgaben.html']}]
            ks.einbauen(daten, d)
            erster = p.read_bytes()
            ks.einbauen(daten, d)
            self.assertEqual(p.read_bytes(), erster)

    def test_materialwege_bleiben_in_der_klasse(self):
        for e in E:
            for datei in e["seiten"]:
                p = ROOT / e["ordner"] / datei
                if not p.exists():
                    continue
                with self.subTest(seite=str(p.relative_to(ROOT))):
                    s, parsed = p.read_text(encoding="utf-8"), Seite(p)
                    self.assertEqual(s.count('<!-- ks-navigation:start -->'), 1)
                    self.assertEqual(s.count('<!-- ks-kopf:start -->'), 1)
                    self.assertEqual(s.count('<!-- ks-ende:start -->'), 1)
                    ids = [a['id'] for a in parsed.mit(attr='id')]
                    self.assertEqual(len(ids), len(set(ids)))
                    nav = re.search(r'<!-- ks-navigation:start -->(.*?)<!-- ks-navigation:end -->', s, re.S)[1]
                    self.assertIn('href="../index.html"', nav)
                    self.assertEqual(nav.count('aria-current="page"'), 1)
                    for href in re.findall(r'href="([^"]+)"', nav):
                        u = urlsplit(html.unescape(href))
                        self.assertFalse(u.scheme or u.netloc)
                        if u.path:
                            ziel = (p.parent / u.path).resolve()
                            self.assertTrue(ziel.exists(), str(ziel))
                            self.assertEqual(ziel.relative_to(ROOT).parts[0], e['ordner'].split('/')[0])
                        else:
                            self.assertIn(u.fragment, ids)
                    for a in parsed.mit(tag='script', attr='src') + parsed.mit(tag='link', attr='href'):
                        href = a.get('src', a.get('href', ''))
                        if 'kadetten-' in href:
                            self.assertTrue((p.parent / href).exists(), href)

    def test_klassenstart_behaelt_material_und_abgaben(self):
        for gruppe in {e['ordner'].split('/')[0] for e in E}:
            p = ROOT / gruppe / 'index.html'
            s, parsed = p.read_text(encoding='utf-8'), Seite(p)
            with self.subTest(gruppe=gruppe):
                self.assertIn('Was soll ich machen?', s)
                self.assertIn('id="ks-themen-suche"', s)
                self.assertFalse(any('open' in a for a in parsed.mit(tag='details', klasse='ks-themenblock')))
                hrefs = {a['href'] for a in parsed.mit(tag='a', attr='href')}
                for e in E:
                    if not e['ordner'].startswith(gruppe + '/') or e.get('versteckt'):
                        continue
                    for seite in e['seiten']:
                        self.assertIn(e['ordner'].split('/', 1)[1] + '/' + seite, hrefs)
                ids = [a['id'] for a in parsed.mit(attr='id')]
                self.assertEqual(len(ids), len(set(ids)))

    def test_auftrag_uebernimmt_vorgaben_unveraendert(self):
        import kadetten_layout as ks
        for e in E:
            if not e.get('fahrplan'):
                continue
            u = dict(e, unter=e['ordner'].split('/', 1)[1])
            ausgabe = ks.arbeitsauftrag(u)
            for r in e['fahrplan']['zeilen']:
                self.assertIn(html.escape(r['lesen']), ausgabe)
                if not re.search(r'für schnelle|zusatz|optional', r['wann'], re.I):
                    if r.get('abgabe') and r['abgabe'] != '–':
                        self.assertIn(html.escape(r['abgabe']), ausgabe)


if __name__ == '__main__':
    unittest.main()
