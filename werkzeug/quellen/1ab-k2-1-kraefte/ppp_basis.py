"""Zeichen-Bausteine für die Präsentationen der Einheit K2.1 Mechanische Kräfte (BHAK-Folienmaster).
Übernommen aus werkzeug/quellen/1ab-k1-4-erkenntnis/bauen_ppp.py (Stand 30.10.2026) und auf die hier gebrauchten Bausteine gekürzt:
Deck mit Abschnitten und Klick-Animationen, Kästen, Text, Tabellen mit gemessenen Zeilenhöhen, Pills, QR-Codes und Bilder.
Wird von unterricht_ppp.py geladen: python3 werkzeug/quellen/1ab-k2-1-kraefte/unterricht_ppp.py <Folienmaster.pptx> <Zielordner>"""
import copy, io, os, re, sys, uuid
import qrcode
from lxml import etree
from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
import inhalt as I
import theorie_daten as TD
import versuche_daten as VD
import plan as PL

MASTER, OUT = sys.argv[1], sys.argv[2]
UNIT = os.path.join(ROOT, I.ORDNER) + "/"
VER = I.V
OLIVE, INK, CARD, GREEN, ORANGE, TEAL, RUST, MUTED, WHITE, PALE = (RGBColor.from_string(x) for x in
    ["3B4A2F", "1F2A1C", "EEF3E4", "7FA83A", "D9772B", "2E7D8C", "8C3B2E", "5E6652", "FFFFFF", "F7F9F2"])
RED = RGBColor.from_string("A33A2B")
GREY = RGBColor.from_string("DCDFD6")
FONT_R = ImageFont.truetype("/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf", 100)
FONT_B = ImageFont.truetype("/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf", 100)
URL = {k: I.URL + k + ".html" for k in ("theorie", "aufgaben", "versuche", "quiz")}
X0, X1, Y0, Y1 = 0.5, 9.5, 1.12, 5.08


# ================================================================ Messen
def plain(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", t)


def lines_needed(t, size, w_in, bold=False):
    """Zeilen, die ein Text bei Schriftgröße size (pt) in einer Box der Breite w_in (Zoll) braucht (Calibri ≈ Carlito)."""
    font = FONT_B if bold else FONT_R
    maxw = (w_in - 0.22) * 72 / size * 100 * 0.97
    n = 0
    for para in plain(t).split("\n"):
        words, cur = para.split(" "), ""
        n += 1
        for wd in words:
            test = (cur + " " + wd).strip()
            if font.getlength(test) > maxw and cur:
                n += 1; cur = wd
            else:
                cur = test
    return n


def th(t, size, w_in, bold=False, ls=1.17, pad=0.1):
    return lines_needed(t, size, w_in, bold) * size * ls / 72 + pad


# ================================================================ Deck
def qr_png(url):
    q = qrcode.QRCode(border=1, box_size=10); q.add_data(url); q.make(fit=True)
    b = io.BytesIO(); q.make_image(fill_color="#1F2A1C", back_color="white").save(b, "PNG"); b.seek(0); return b


class Deck:
    def __init__(self, lehrer, fuss):
        self.lehrer = lehrer
        self.p = Presentation(MASTER)
        lst = self.p.slides._sldIdLst
        self.pill_proto = None
        for sh in self.p.slides[2].shapes:
            if sh.name == "Buchseite": self.pill_proto = copy.deepcopy(sh._element)
        for sid in list(lst):
            self.p.part.drop_rel(sid.get(qn("r:id"))); lst.remove(sid)
        self.L = {l.name: l for l in self.p.slide_layouts}
        self.sections = []
        for part in self.p.part.package.iter_parts():
            if "slideLayout" in str(part.partname) or "slideMaster" in str(part.partname):
                for t in part._element.iter(qn("a:t")):
                    if t.text and "Fach · Jahrgang · Thema" in t.text: t.text = fuss

    def section(self, name):
        self.sections.append((name, []))

    def slide(self, layout, title, hidden=False):
        s = self.p.slides.add_slide(self.L[layout])
        for ph in s.placeholders:
            if ph.placeholder_format.type == 1:
                ph.text_frame.text = title
                if layout in ("Nur Titel", "Aufgabe") and len(title) > 36:   # lange Titel kleiner, damit sie den Inhalt nicht berühren
                    for r_ in ph.text_frame.paragraphs[0].runs: r_.font.size = Pt(24 if len(title) <= 44 else 21)
        if hidden: s._element.set("show", "0")
        self.sections[-1][1].append(self.p.slides._sldIdLst[-1].get("id"))
        s._anim = []
        return s

    def save(self, path):
        for s in self.p.slides:
            if getattr(s, "_anim", None): add_clicks(s, s._anim)
        prs = self.p.part._element
        ext_lst = prs.find(qn("p:extLst"))
        if ext_lst is None: ext_lst = etree.SubElement(prs, qn("p:extLst"))
        P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
        for old in ext_lst.findall(qn("p:ext")):
            if old.get("uri") == "{521415D9-36F7-43E2-AB2F-B90AF26B5E84}": ext_lst.remove(old)
        ext = etree.SubElement(ext_lst, qn("p:ext")); ext.set("uri", "{521415D9-36F7-43E2-AB2F-B90AF26B5E84}")
        sl = etree.SubElement(ext, "{%s}sectionLst" % P14, nsmap={"p14": P14})
        for name, ids in self.sections:
            se = etree.SubElement(sl, "{%s}section" % P14); se.set("name", name); se.set("id", "{%s}" % str(uuid.uuid4()).upper())
            il = etree.SubElement(se, "{%s}sldIdLst" % P14)
            for i in ids: etree.SubElement(il, "{%s}sldId" % P14).set("id", i)
        self.p.save(path)


def add_clicks(slide, groups):
    nid = [2]
    def cid():
        nid[0] += 1; return str(nid[0])
    P = "http://schemas.openxmlformats.org/presentationml/2006/main"
    clicks = ""
    for grp in groups:
        inner = ""
        for k, sh in enumerate(grp):
            spid = sh.shape_id
            inner += (f'<p:par><p:cTn id="{cid()}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="{"clickEffect" if k == 0 else "withEffect"}">'
                      f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                      f'<p:set><p:cBhvr><p:cTn id="{cid()}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
                      f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
                      f'<p:to><p:strVal val="visible"/></p:to></p:set>'
                      f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{cid()}" dur="400"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
                      f'</p:childTnLst></p:cTn></p:par>')
        clicks += (f'<p:par><p:cTn id="{cid()}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
                   f'<p:par><p:cTn id="{cid()}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{inner}</p:childTnLst></p:cTn></p:par>'
                   f'</p:childTnLst></p:cTn></p:par>')
    xml = (f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
           f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{clicks}</p:childTnLst></p:cTn>'
           f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
           f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
           f'</p:childTnLst></p:cTn></p:par></p:tnLst>'
           f'<p:bldLst>{"".join(f"<p:bldP spid=\"{sh.shape_id}\" grpId=\"0\" animBg=\"1\"/>" for grp in groups for sh in grp)}</p:bldLst></p:timing>')
    el = etree.fromstring(xml)
    sld = slide._element
    ext = sld.find(qn("p:extLst"))
    if ext is not None: ext.addprevious(el)
    else: sld.append(el)


def box(s, x, y, w, h, fill=None, line=None, radius=True, lw=1.25):
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    if radius: shp.adjustments[0] = 0.08
    if fill is None: shp.fill.background()
    else: shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(lw)
    shp.shadow.inherit = False
    tf = shp.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.1); tf.margin_top = tf.margin_bottom = Inches(0.05)
    return shp


def runs_md(t):
    out, pos = [], 0
    for m in re.finditer(r"\*\*(.+?)\*\*", t):
        if m.start() > pos: out.append((t[pos:m.start()], {}))
        out.append((m.group(1), {"bold": True})); pos = m.end()
    if pos < len(t): out.append((t[pos:], {}))
    return out or [("", {})]


def text(target, parts, size=20, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, after=4):
    tf = target.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    first = True
    for para in parts:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.alignment = align; p.space_after = Pt(after)
        runs = para if isinstance(para, list) else runs_md(para)
        for t, o in runs:
            r = p.add_run(); r.text = t; f = r.font
            f.size = Pt(o.get("size", size)); f.bold = o.get("bold", bold); f.color.rgb = o.get("color", color)
            if o.get("italic"): f.italic = True
    return target


def tb(s, x, y, w, h, parts, **kw):
    t = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    t.text_frame.margin_left = t.text_frame.margin_right = Inches(0.05)
    return text(t, parts, **kw)


def pill(s, label, x=3.55, y=5.18, w=2.2, kind="theory"):
    el = copy.deepcopy(d.pill_proto)
    ids = [int(v) for v in s.shapes._spTree.xpath("//p:cNvPr/@id")]
    el.xpath(".//p:cNvPr")[0].set("id", str(max(ids + [1]) + 1))
    s.shapes._spTree.append(el)
    shp = s.shapes[-1]
    shp.left, shp.top, shp.width = Inches(x), Inches(y), Inches(w)
    col = {"theory": RGBColor.from_string("6E7F4E"), "book": TEAL, "versuch": RED}[kind]
    shp.fill.solid(); shp.fill.fore_color.rgb = col
    r = shp.text_frame.paragraphs[0].runs
    r[0].text = label
    for extra in r[1:]: extra.text = ""
    return shp


def kind_of(src):
    return "versuch" if src.startswith("Versuch im Buch") else ("book" if src.startswith("Buch-Aufgabe") else "theory")


def tag(s, label, color=OLIVE, x=7.6, y=0.95, w=1.9):
    t = box(s, x, y, w, 0.32, fill=color)
    text(t, [label], size=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    return t


def grid(s, x, y, colw, rows, rowh, head=True, size=16, fills=None):
    cells, yy = [], y
    for ri, row in enumerate(rows):
        xx, rc = x, []
        h = rowh[ri] if isinstance(rowh, (list, tuple)) else rowh
        for ci, val in enumerate(row):
            hd = head and ri == 0
            fill = OLIVE if hd else (fills[ri] if fills else (CARD if ri % 2 else WHITE))
            c = box(s, xx, yy, colw[ci], h, fill=fill, line=RGBColor.from_string("B9C4A6"), radius=False, lw=0.75)
            text(c, [val] if isinstance(val, str) else val, size=size, color=WHITE if hd else INK, bold=hd, anchor=MSO_ANCHOR.MIDDLE, after=0)
            rc.append(c); xx += colw[ci]
        cells.append(rc); yy += h
    return cells


def auto_grid(s, x, y, colw, rows, size=16, head=True, minh=0.36, fills=None):
    """Tabelle mit gemessenen Zeilenhöhen. Gibt (Zellen, Gesamthöhe) zurück."""
    hs = [max(minh, max(th(str(c), size, w, bold=(head and ri == 0), pad=0.1) for c, w in zip(r, colw))) for ri, r in enumerate(rows)]
    return grid(s, x, y, colw, rows, hs, head=head, size=size, fills=fills), sum(hs)


def table_h(colw, rows, size=16, head=True, minh=0.36):
    return sum(max(minh, max(th(str(c), size, w, bold=(head and ri == 0), pad=0.1) for c, w in zip(r, colw))) for ri, r in enumerate(rows))


def answer(s, x, y, w, h, title, body, lehrer, hint="Deine Antwort – am Arbeitsblatt eintragen", size=20):
    if lehrer:
        b = box(s, x, y, w, h, fill=WHITE, line=ORANGE, lw=2)
        text(b, ([[(title, {"bold": True, "color": ORANGE, "size": 16})]] if title else []) + (body if isinstance(body, list) else [body]), size=size, after=2)
        s._anim.append([b])
    else:
        b = box(s, x, y, w, h, fill=PALE, line=RGBColor.from_string("B9C4A6"), lw=1.5)
        text(b, [[(hint, {"italic": True, "color": MUTED, "size": 16})]], size=16)
    return b


def ppt_qr(s, url, x, y, size, step, label, color=OLIVE, linksize=8):
    s.shapes.add_picture(qr_png(url), Inches(x), Inches(y), Inches(size), Inches(size))
    c = box(s, x + size / 2 - 0.2, y - 0.25, 0.4, 0.4, fill=color)
    text(c, [step], size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, after=0)
    tb(s, x - 0.3, y + size + 0.02, size + 0.6, 0.32, [label], size=16, bold=True, color=color, align=PP_ALIGN.CENTER, after=0)
    tb(s, x - 0.45, y + size + 0.34, size + 0.9, 0.5, [url], size=linksize, color=MUTED, align=PP_ALIGN.CENTER, after=0)


def picture(s, path, x, y, w=None, h=None):
    from PIL import Image
    im = Image.open(path); iw, ih = im.size
    if w and h:
        k = min(w / iw, h / ih); w2, h2 = iw * k, ih * k
        return s.shapes.add_picture(path, Inches(x + (w - w2) / 2), Inches(y), Inches(w2), Inches(h2)), h2
    if w: return s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(w * ih / iw)), w * ih / iw
    return s.shapes.add_picture(path, Inches(x), Inches(y), Inches(h * iw / ih), Inches(h)), h
