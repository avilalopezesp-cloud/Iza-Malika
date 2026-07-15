"""
Iza Malika — Creative Project Book
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, NextPageTemplate
from PIL import Image as PILImage
import os, tempfile

# ── Brand colours ─────────────────────────────────────────────────────────────
CREAM   = colors.HexColor("#F5EDE0")
ROSE    = colors.HexColor("#C4687A")
GOLD    = colors.HexColor("#C9A84C")
GREEN   = colors.HexColor("#4A7C59")
NIGHT   = colors.HexColor("#1C1C2E")
INK     = colors.HexColor("#2A2018")
WARM    = colors.HexColor("#8a7060")
PALE    = colors.HexColor("#ede5d8")
RULE    = colors.HexColor("#d4c8b8")
WHITE   = colors.white

PAGE_W, PAGE_H = A4

OUTPUT      = os.path.join(os.path.dirname(__file__), "Iza_Malika_Creative_Project_Book.pdf")
LOGO_SRC    = os.path.join(os.path.dirname(__file__), "..", "images", "hero-spiral.webp")

def _make_logo_png():
    """Convert hero-spiral.webp to a cream-backgrounded PNG for ReportLab."""
    img = PILImage.open(LOGO_SRC).convert("RGBA")
    bg  = PILImage.new("RGBA", img.size, (245, 237, 224, 255))
    bg.paste(img, mask=img.split()[3])
    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    bg.convert("RGB").save(tmp.name, "PNG")
    return tmp.name

LOGO_PNG = _make_logo_png()

# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles():
    return {
        # Cover
        "cover_name": ParagraphStyle("cover_name",
            fontName="Times-Roman", fontSize=58, leading=60,
            textColor=CREAM, alignment=TA_LEFT),
        "cover_name2": ParagraphStyle("cover_name2",
            fontName="Times-Roman", fontSize=58, leading=52,
            textColor=ROSE, alignment=TA_LEFT),
        "cover_sub": ParagraphStyle("cover_sub",
            fontName="Times-Italic", fontSize=13, leading=18,
            textColor=colors.HexColor("#9a8070"), alignment=TA_LEFT,
            letterSpacing=2),
        "cover_label": ParagraphStyle("cover_label",
            fontName="Times-Roman", fontSize=8, leading=13,
            textColor=colors.HexColor("#ffffff"), letterSpacing=3),
        "cover_book": ParagraphStyle("cover_book",
            fontName="Times-Roman", fontSize=9, leading=14,
            textColor=GOLD, letterSpacing=4),

        # Section
        "eyebrow": ParagraphStyle("eyebrow",
            fontName="Times-Roman", fontSize=7.5, leading=11,
            textColor=ROSE, letterSpacing=4, spaceAfter=6),
        "section_title": ParagraphStyle("section_title",
            fontName="Times-Roman", fontSize=36, leading=40,
            textColor=INK, alignment=TA_LEFT, spaceAfter=18),
        "section_italic": ParagraphStyle("section_italic",
            fontName="Times-Italic", fontSize=24, leading=30,
            textColor=INK, alignment=TA_LEFT, spaceAfter=16),

        # Body
        "body": ParagraphStyle("body",
            fontName="Times-Roman", fontSize=10.5, leading=18,
            textColor=INK, spaceAfter=10),
        "body_italic": ParagraphStyle("body_italic",
            fontName="Times-Italic", fontSize=10.5, leading=18,
            textColor=INK, spaceAfter=10),
        "caption": ParagraphStyle("caption",
            fontName="Times-Italic", fontSize=8.5, leading=13,
            textColor=WARM),
        "label_sm": ParagraphStyle("label_sm",
            fontName="Times-Roman", fontSize=7.5, leading=11,
            textColor=ROSE, letterSpacing=3, spaceAfter=3),

        # Quote
        "quote": ParagraphStyle("quote",
            fontName="Times-Italic", fontSize=18, leading=26,
            textColor=INK, alignment=TA_CENTER, spaceAfter=6),
        "quote_attr": ParagraphStyle("quote_attr",
            fontName="Times-Roman", fontSize=8.5, leading=12,
            textColor=WARM, alignment=TA_CENTER),

        # ToC
        "toc_num": ParagraphStyle("toc_num",
            fontName="Times-Italic", fontSize=11, leading=22,
            textColor=ROSE),
        "toc_item": ParagraphStyle("toc_item",
            fontName="Times-Roman", fontSize=11, leading=22,
            textColor=INK),
        "toc_sub": ParagraphStyle("toc_sub",
            fontName="Times-Italic", fontSize=8.5, leading=12,
            textColor=WARM),

        # Checklist
        "check": ParagraphStyle("check",
            fontName="Times-Roman", fontSize=9.5, leading=16,
            textColor=INK, leftIndent=14),

        # Thank you page
        "ty_big": ParagraphStyle("ty_big",
            fontName="Times-Italic", fontSize=22, leading=30,
            textColor=INK, alignment=TA_CENTER),
        "ty_name": ParagraphStyle("ty_name",
            fontName="Times-Roman", fontSize=12, leading=18,
            textColor=INK, alignment=TA_CENTER, spaceAfter=2),
        "ty_role": ParagraphStyle("ty_role",
            fontName="Times-Italic", fontSize=9.5, leading=14,
            textColor=WARM, alignment=TA_CENTER),

        # Journey
        "journey_step": ParagraphStyle("journey_step",
            fontName="Times-Roman", fontSize=11, leading=16,
            textColor=INK, alignment=TA_CENTER),
        "journey_arrow": ParagraphStyle("journey_arrow",
            fontName="Times-Roman", fontSize=14, leading=18,
            textColor=RULE, alignment=TA_CENTER),
        "journey_note": ParagraphStyle("journey_note",
            fontName="Times-Italic", fontSize=8.5, leading=13,
            textColor=WARM, alignment=TA_CENTER),
    }

S = make_styles()

# ── Canvas callbacks ──────────────────────────────────────────────────────────
def cover_bg(c, doc):
    c.saveState()
    c.setFillColor(INK)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(ROSE)
    c.rect(0, 0, 5, PAGE_H, fill=1, stroke=0)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.5)
    c.line(40, 96, PAGE_W - 40, 96)
    c.restoreState()

def inner_bg(c, doc):
    c.saveState()
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(ROSE)
    c.rect(0, 0, 2.5, PAGE_H, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor("#e0d4c4"))
    c.setLineWidth(0.4)
    c.line(40, 36, PAGE_W - 40, 36)
    c.setFont("Times-Italic", 7)
    c.setFillColor(WARM)
    c.drawCentredString(PAGE_W / 2, 22, "Iza Malika  ·  Creative Project Book  ·  2026")
    c.drawRightString(PAGE_W - 40, 22, str(doc.page - 1))
    c.restoreState()

def thankyou_bg(c, doc):
    c.saveState()
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.restoreState()

# ── Helpers ───────────────────────────────────────────────────────────────────
def sp(h_mm):
    return Spacer(1, h_mm * mm)

def hr(color=None, thickness=0.4, pct="100%"):
    return HRFlowable(width=pct, thickness=thickness,
                      color=color or RULE,
                      spaceAfter=4 * mm, spaceBefore=4 * mm)

def eyebrow(text):
    return Paragraph(text.upper(), S["eyebrow"])

def color_swatch_row(name, hex_val, story_text):
    col = colors.HexColor(hex_val)
    t = Table(
        [["", Paragraph(f"<b>{name}</b><br/>{hex_val}",
            ParagraphStyle("csn", fontName="Times-Roman", fontSize=9.5,
                           textColor=INK, leading=14)),
          Paragraph(story_text, ParagraphStyle("csd", fontName="Times-Italic",
                    fontSize=9, textColor=WARM, leading=14))]],
        colWidths=[18*mm, 48*mm, 90*mm],
        rowHeights=[16*mm]
    )
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), col),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",(1,0),(-1,-1), 8),
        ("GRID",       (0,0), (-1,-1), 0.3, RULE),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[CREAM]),
    ]))
    return t

# ── Build ─────────────────────────────────────────────────────────────────────
def build():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=40*mm, rightMargin=20*mm,
        topMargin=20*mm,  bottomMargin=20*mm,
    )

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H,
                        leftPadding=46*mm, rightPadding=20*mm,
                        topPadding=0, bottomPadding=0)
    inner_frame = Frame(40*mm, 18*mm, PAGE_W - 60*mm, PAGE_H - 36*mm,
                        leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    ty_frame    = Frame(20*mm, 20*mm, PAGE_W - 40*mm, PAGE_H - 40*mm,
                        leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)

    doc.addPageTemplates([
        PageTemplate(id="cover",    frames=[cover_frame], onPage=cover_bg),
        PageTemplate(id="inner",    frames=[inner_frame], onPage=inner_bg),
        PageTemplate(id="thankyou", frames=[ty_frame],    onPage=thankyou_bg),
    ])

    story = []

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 1 — COVER
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(56))
    story.append(Paragraph("IZA", S["cover_name"]))
    story.append(Paragraph("MALIKA", S["cover_name2"]))
    story.append(sp(10))
    story.append(Paragraph("Painter  ·  Granada", S["cover_sub"]))
    story.append(sp(24))
    story.append(HRFlowable(width="55%", thickness=0.5,
                             color=colors.HexColor("#4a3828"),
                             spaceBefore=0, spaceAfter=6*mm))
    story.append(Paragraph("CREATIVE PROJECT BOOK", S["cover_book"]))
    story.append(sp(2))
    story.append(Paragraph("2026", S["cover_label"]))

    story.append(NextPageTemplate("inner"))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 2 — TABLE OF CONTENTS
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("Contents"))
    story.append(Paragraph("Creative Project Book", S["section_title"]))
    story.append(hr())
    story.append(sp(2))

    toc = [
        ("01", "The Story",               "Who is Iza, what inspires her, what she wants to transmit"),
        ("02", "Visual Identity",          "The mandala — the logo, its variants and usage"),
        ("03", "Color Language",           "Why these colors exist — then the HEX values"),
        ("04", "Typography",               "The typeface and the full hierarchy: H1 to Caption"),
        ("05", "Digital Experience",       "Buttons, cards, animations, hover states, transitions"),
        ("06", "The Journey",              "The user's path through the website — and why it was designed this way"),
        ("07", "Workshops & Experiences",  "The workshop program and its visual world"),
        ("08", "Brand in Practice",        "Desktop, mobile, and tablet — the brand living"),
        ("09", "Handoff Package",          "Everything the client receives"),
        ("10", "Thank You",               ""),
    ]

    for num, title, sub in toc:
        content = [
            Paragraph(num, S["toc_num"]),
            [Paragraph(title, S["toc_item"]),
             Paragraph(sub, S["toc_sub"])] if sub else Paragraph(title, S["toc_item"]),
        ]
        if sub:
            cell_content = Table(
                [[Paragraph(num, S["toc_num"]),
                  [Paragraph(title, S["toc_item"]),
                   Paragraph(sub, S["toc_sub"])]]],
                colWidths=[16*mm, 130*mm]
            )
        else:
            cell_content = Table(
                [[Paragraph(num, S["toc_num"]),
                  Paragraph(title, S["toc_item"])]],
                colWidths=[16*mm, 130*mm]
            )
        cell_content.setStyle(TableStyle([
            ("VALIGN",        (0,0),(-1,-1),"MIDDLE"),
            ("BOTTOMPADDING", (0,0),(-1,-1), 5),
            ("TOPPADDING",    (0,0),(-1,-1), 5),
        ]))
        story.append(cell_content)
        story.append(HRFlowable(width="100%", thickness=0.3,
                                 color=colors.HexColor("#ddd0c0"),
                                 spaceBefore=0, spaceAfter=0))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 3 — 01: THE STORY
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("01 — The Story"))
    story.append(Paragraph("The Story", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "Iza Malika is a painter based in Granada, Spain. Her work spans acrylics, "
        "watercolors, mandalas, and portraits — but what defines it is not the medium. "
        "It is the impulse. Every piece begins with a feeling that needs to leave the body "
        "and become something visible.",
        S["body"]))

    story.append(Paragraph(
        "She grew up surrounded by color, pattern, and the kind of stillness you only find "
        "in cities that have been beautiful for centuries. Granada gave her the light. "
        "Painting gave her the language.",
        S["body"]))

    story.append(sp(4))
    story.append(hr(color=ROSE, thickness=0.8))
    story.append(sp(2))

    story.append(eyebrow("What Inspires Her"))
    story.append(sp(2))
    story.append(Paragraph(
        "Nature — its textures, its silences, its cycles. "
        "The way a plant grows toward light without being told to. "
        "The geometry hidden inside a flower. "
        "The color a sky turns just before it rains.",
        S["body_italic"]))

    story.append(sp(4))
    story.append(eyebrow("What She Wants to Transmit"))
    story.append(sp(2))

    transmit = [
        ("Slowness", "In a world that accelerates, her work asks you to stop. To look. To feel something before you name it."),
        ("Presence", "Each painting is a record of a real moment. Not a concept. A presence."),
        ("Permission", "Through her workshops, she gives other people permission to create — to stop waiting until they're 'good enough'."),
        ("Connection", "Art is most powerful when it becomes shared. A painting on your wall is a conversation that never ends."),
    ]
    for title, desc in transmit:
        story.append(KeepTogether([
            Paragraph(f"<b>{title}</b>", ParagraphStyle("tt",
                fontName="Times-Bold", fontSize=10.5, leading=14,
                textColor=ROSE, spaceAfter=2)),
            Paragraph(desc, ParagraphStyle("td",
                fontName="Times-Roman", fontSize=10, leading=16,
                textColor=INK, spaceAfter=10)),
        ]))

    story.append(sp(4))
    story.append(Paragraph(
        '"For me, art is stopping time — a way to listen to nature, '
        'to magic, to the quiet voice that lives inside."',
        S["quote"]))
    story.append(Paragraph("— Iza Malika", S["quote_attr"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 4 — 02: VISUAL IDENTITY
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("02 — Visual Identity"))
    story.append(Paragraph("Visual Identity", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "The logo is the mandala painted by Iza herself — a spiral sun, radiating outward "
        "from a single center point. It lives at the heart of the website, animating on load "
        "as if it is being painted in real time. It is not a symbol designed in software. "
        "It is a painting.",
        S["body"]))

    story.append(sp(4))
    story.append(eyebrow("The Logo"))
    story.append(sp(3))

    # Mandala image centered
    logo_img = Image(LOGO_PNG, width=80*mm, height=80*mm)
    logo_table = Table([[logo_img]], colWidths=[150*mm], rowHeights=[84*mm])
    logo_table.setStyle(TableStyle([
        ("ALIGN",   (0,0),(-1,-1), "CENTER"),
        ("VALIGN",  (0,0),(-1,-1), "MIDDLE"),
        ("BACKGROUND", (0,0),(-1,-1), CREAM),
        ("BOX",     (0,0),(-1,-1), 0.4, RULE),
    ]))
    story.append(logo_table)
    story.append(sp(2))
    story.append(Paragraph(
        "Painted by Iza Malika · Acrylic · Original artwork · Used as the primary brand mark.",
        S["caption"]))

    story.append(sp(6))
    story.append(eyebrow("Logo + Name — Primary Lockup"))
    story.append(sp(2))

    # Logo + name side by side
    small_logo = Image(LOGO_PNG, width=22*mm, height=22*mm)
    lockup = Table(
        [[small_logo,
          Paragraph("Iza Malika", ParagraphStyle("lkup",
            fontName="Times-Roman", fontSize=28, leading=32,
            textColor=INK))]],
        colWidths=[28*mm, 122*mm],
        rowHeights=[26*mm]
    )
    lockup.setStyle(TableStyle([
        ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
        ("LEFTPADDING", (1,0),(1,-1), 10),
        ("BACKGROUND",  (0,0),(-1,-1), CREAM),
        ("BOX",         (0,0),(-1,-1), 0.4, RULE),
    ]))
    story.append(lockup)
    story.append(sp(2))
    story.append(Paragraph(
        "Primary lockup — mandala + name in Cormorant Garamond 300.",
        S["caption"]))

    story.append(sp(5))
    story.append(eyebrow("Logo on Dark"))
    story.append(sp(2))

    dark_logo = Image(LOGO_PNG, width=22*mm, height=22*mm)
    dark_lockup = Table(
        [[dark_logo,
          Paragraph("Iza Malika", ParagraphStyle("dlkup",
            fontName="Times-Roman", fontSize=28, leading=32,
            textColor=CREAM))]],
        colWidths=[28*mm, 122*mm],
        rowHeights=[26*mm]
    )
    dark_lockup.setStyle(TableStyle([
        ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
        ("LEFTPADDING", (1,0),(1,-1), 10),
        ("BACKGROUND",  (0,0),(-1,-1), INK),
        ("BOX",         (0,0),(-1,-1), 0.4, RULE),
    ]))
    story.append(dark_lockup)
    story.append(sp(2))
    story.append(Paragraph(
        "Dark variant — used on night background sections.",
        S["caption"]))

    story.append(sp(5))
    story.append(eyebrow("Usage"))
    story.append(sp(2))
    usage_rules = [
        "The mandala is always used at full color — never grayscale, never recolored.",
        "Minimum size: 40px on screen, 14mm in print.",
        "Clear space around the mandala: equal to one radius of the circle on all sides.",
        "Never crop, rotate, or distort the mandala.",
        "Never place the mandala on a busy photographic background without an overlay.",
        "The name 'Iza Malika' always appears in Cormorant Garamond weight 300.",
    ]
    for r in usage_rules:
        story.append(Paragraph(f"· {r}", S["check"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 5 — 03: COLOR LANGUAGE
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("03 — Color Language"))
    story.append(Paragraph("Color Language", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "These colors were not chosen from a palette library. They were pulled from "
        "the paintings themselves — from the warm glow of a canvas in afternoon light, "
        "the deep shadow of an ink brushstroke, the soft rose of a dried flower.",
        S["body"]))
    story.append(Paragraph(
        "Each color has a reason. Together they feel like a single room "
        "where you would want to spend an afternoon.",
        S["body"]))

    story.append(sp(5))

    color_stories = [
        ("#F5EDE0", "Cream",
         "This is the background of everything. Old paper, raw linen, warm light. "
         "It replaces white in every context — white feels cold here."),
        ("#2A2018", "Ink",
         "The color of charcoal and deep earth. "
         "Text, borders, shadows. It replaces black — warmer, more human."),
        ("#C4687A", "Rose",
         "Used sparingly, like the moment in a painting where color suddenly speaks. "
         "Taglines, hover states, emotional highlights."),
        ("#C9A84C", "Gold",
         "For fine details only. Dividers, active states, the progress bar that tells you "
         "where you are. Never a fill color — always a signal."),
        ("#4A7C59", "Green",
         "Nature. The color that appears in mandalas and botanical pieces. "
         "Present as a secondary accent — the forest at the edge of the frame."),
        ("#1C1C2E", "Night",
         "The deepest tone in the palette. Used for the lightbox overlay, "
         "for moments where the world outside needs to disappear."),
    ]

    for hex_val, name, story_text in color_stories:
        story.append(color_swatch_row(name, hex_val, story_text))
        story.append(sp(1))

    story.append(sp(4))
    story.append(hr())
    story.append(eyebrow("Color Rules"))
    color_rules = [
        "Cream is always the default background. Never pure white.",
        "Rose is used for one thing per layout — not three things at once.",
        "Gold lives in details: lines, borders, one-pixel accents.",
        "Night appears only in full-overlay contexts. Not in UI elements.",
        "The palette works because it is restrained. Every color earns its place.",
    ]
    for r in color_rules:
        story.append(Paragraph(f"· {r}", S["check"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 6 — 04: TYPOGRAPHY
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("04 — Typography"))
    story.append(Paragraph("Typography", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "One typeface. Cormorant Garamond. Classical, elegant, and slightly imperfect "
        "in the way that handwriting is imperfect. It looks like it belongs in a letter "
        "written by someone who cares about words.",
        S["body"]))
    story.append(Paragraph(
        "Weight 300 is the default. The brand speaks quietly — "
        "it never shouts. Italic is reserved for poetry, quotes, and the moments "
        "where language becomes feeling.",
        S["body"]))

    story.append(sp(6))
    story.append(eyebrow("Type Hierarchy"))
    story.append(sp(4))

    # H1
    story.append(Table(
        [[Paragraph("H1 — Display", ParagraphStyle("hl", fontName="Times-Roman",
            fontSize=7.5, textColor=ROSE, letterSpacing=3, leading=10)),
          Paragraph("Iza Malika", ParagraphStyle("h1s", fontName="Times-Roman",
            fontSize=36, leading=40, textColor=INK)),
          Paragraph("Cormorant Garamond 300\nclamp(3rem, 8vw, 6.5rem)",
            ParagraphStyle("hn", fontName="Times-Italic", fontSize=8,
            textColor=WARM, leading=12))]],
        colWidths=[28*mm, 90*mm, 38*mm]
    ))
    story.append(hr(color=RULE, thickness=0.3))

    # H2
    story.append(Table(
        [[Paragraph("H2 — Section", ParagraphStyle("hl2", fontName="Times-Roman",
            fontSize=7.5, textColor=ROSE, letterSpacing=3, leading=10)),
          Paragraph("Creative Experiences", ParagraphStyle("h2s", fontName="Times-Roman",
            fontSize=22, leading=28, textColor=INK)),
          Paragraph("Cormorant Garamond 300\nclamp(2.4rem, 6.5vw, 5rem)",
            ParagraphStyle("h2n", fontName="Times-Italic", fontSize=8,
            textColor=WARM, leading=12))]],
        colWidths=[28*mm, 90*mm, 38*mm]
    ))
    story.append(hr(color=RULE, thickness=0.3))

    # H3 italic
    story.append(Table(
        [[Paragraph("H3 — Sub", ParagraphStyle("hl3", fontName="Times-Roman",
            fontSize=7.5, textColor=ROSE, letterSpacing=3, leading=10)),
          Paragraph("Every painting begins with a feeling.", ParagraphStyle("h3s",
            fontName="Times-Italic", fontSize=16, leading=22, textColor=INK)),
          Paragraph("Cormorant Garamond 300 italic\nclamp(1.8rem, 4vw, 3rem)",
            ParagraphStyle("h3n", fontName="Times-Italic", fontSize=8,
            textColor=WARM, leading=12))]],
        colWidths=[28*mm, 90*mm, 38*mm]
    ))
    story.append(hr(color=RULE, thickness=0.3))

    # Body
    story.append(Table(
        [[Paragraph("Body", ParagraphStyle("hlb", fontName="Times-Roman",
            fontSize=7.5, textColor=ROSE, letterSpacing=3, leading=10)),
          Paragraph("I believe art begins with intuition. Each brushstroke is an act of listening to what already exists, waiting to become visible.", ParagraphStyle("bs",
            fontName="Times-Roman", fontSize=10.5, leading=17, textColor=INK)),
          Paragraph("Cormorant Garamond 300\nclamp(1rem, 1.8vw, 1.3rem)\nLine height 1.75",
            ParagraphStyle("bn", fontName="Times-Italic", fontSize=8,
            textColor=WARM, leading=12))]],
        colWidths=[28*mm, 90*mm, 38*mm]
    ))
    story.append(hr(color=RULE, thickness=0.3))

    # Caption
    story.append(Table(
        [[Paragraph("Caption", ParagraphStyle("hlc", fontName="Times-Roman",
            fontSize=7.5, textColor=ROSE, letterSpacing=3, leading=10)),
          Paragraph("ACRYLIC ON CANVAS  ·  50 × 40 CM  ·  2024", ParagraphStyle("cs",
            fontName="Times-Roman", fontSize=8, leading=12, textColor=WARM,
            letterSpacing=2)),
          Paragraph("Cormorant Garamond 300\n0.72rem – 0.9rem\nUppercase, tracked",
            ParagraphStyle("cn", fontName="Times-Italic", fontSize=8,
            textColor=WARM, leading=12))]],
        colWidths=[28*mm, 90*mm, 38*mm]
    ))
    story.append(hr(color=RULE, thickness=0.3))

    story.append(sp(6))
    story.append(eyebrow("Type Rules"))
    type_rules = [
        "One typeface only. Never substitute or pair with another font.",
        "Weight 300 is the default. Use 400 only for emphasis within body copy — never in headings.",
        "Italic is for poetry, quotes, and captions. Never for UI labels or navigation.",
        "Letter-spacing on headings: 0.04em – 0.12em. Labels and navigation: 0.3em – 0.5em.",
        "Never use bold (700) weight. The brand speaks at a low volume — it doesn't need to.",
        "Line height: 1.0–1.2 for display, 1.75–1.85 for body text.",
    ]
    for r in type_rules:
        story.append(Paragraph(f"· {r}", S["check"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 7 — 05: DIGITAL EXPERIENCE
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("05 — Digital Experience"))
    story.append(Paragraph("Digital Experience", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "The website is not a store. It is a space. Every interaction is designed "
        "to feel considered — never instant, never aggressive. Animations slow "
        "the pace just enough to make you feel like you arrived somewhere.",
        S["body"]))

    story.append(sp(4))

    components = [
        ("Buttons",
         "Outlined, no fill. When a button appears on scroll, its border draws itself "
         "from left to right — as if someone just underlined the word. On hover: the background "
         "fills with Ink and text turns Cream. Letter-spacing 0.38em, uppercase. "
         "The button never rushes.",
         "Example: 'Discover the Collection'"),

        ("Cards",
         "No border-radius. No shadows by default. On hover: a quiet lift (translateY -5px), "
         "a barely-visible shadow, and a bottom line that draws across the full width. "
         "Cards feel like paper on a table.",
         "Example: Workshop feature cards, Oracle cards"),

        ("Animations",
         "Everything enters from below with a fade. Nothing pops or bounces. "
         "The spring easing (cubic-bezier 0.16, 1, 0.3, 1) gives each element a "
         "sense of settling — like something being placed gently, not dropped.",
         "Scroll reveals, hero entrance, section transitions"),

        ("Hover States",
         "Subtle. Opacity shifts from 0.45 to 1 on navigation links. "
         "Colors shift, not sizes. The experience rewards attention "
         "rather than demanding it.",
         "Navigation, artwork thumbnails, gallery items"),

        ("Transitions",
         "Standard duration: 0.85s. No transition faster than 0.2s appears "
         "in a visible UI element. The pace is measured. "
         "The oracle carousel changes background color over 0.6s — "
         "the whole mood of the page shifts quietly.",
         "Carousel, language toggle, lightbox open/close"),

        ("Language Toggle",
         "A small outlined button — shows the language you can switch TO. "
         "One click changes every word on the page instantly. "
         "The choice is remembered forever in the browser.",
         "EN ↔ ES — persists via localStorage"),
    ]

    for name, desc, example in components:
        story.append(KeepTogether([
            Paragraph(name, ParagraphStyle("cname",
                fontName="Times-Bold", fontSize=11, leading=14,
                textColor=INK, spaceAfter=3)),
            Paragraph(desc, ParagraphStyle("cdesc",
                fontName="Times-Roman", fontSize=9.5, leading=15,
                textColor=INK, spaceAfter=2)),
            Paragraph(example, ParagraphStyle("cex",
                fontName="Times-Italic", fontSize=8.5, leading=13,
                textColor=ROSE, spaceAfter=8)),
            HRFlowable(width="100%", thickness=0.3, color=colors.HexColor("#e0d4c4"),
                       spaceAfter=8, spaceBefore=0),
        ]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 8 — 06: THE JOURNEY
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("06 — The Journey"))
    story.append(Paragraph("The Journey", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "The website was designed as a single continuous experience. "
        "Not a collection of pages, but a walk through a gallery — "
        "each section earning the next. The order is intentional.",
        S["body"]))

    story.append(sp(6))

    # Journey map
    journey_steps = [
        ("Hero",            "You arrive. A spiral canvas paints itself. The name appears.\nYou don't know yet where you are — but you feel something."),
        ("Meet Iza",        "A brief manifesto. A portrait. A bio.\nYou learn who made this world before you explore it."),
        ("Oracle",          "An invitation: how are you feeling today?\nYou choose an emotion. The palette of the whole page shifts."),
        ("Collection",      "The artworks appear in a carousel, themed by the emotion you chose.\nThe work speaks the language of your mood."),
        ("Workshops",       "You learn you can participate. Paint alongside Iza.\nThe brand becomes not just something to look at — but to join."),
        ("Let's Create",    "Two doors: ask about an artwork, or book a workshop.\nThe call to action arrives after the relationship has been built."),
    ]

    for i, (step, explanation) in enumerate(journey_steps):
        # Step box
        step_box = Table(
            [[Paragraph(step, ParagraphStyle("js", fontName="Times-Roman",
                fontSize=12, leading=16, textColor=INK, alignment=TA_CENTER))]],
            colWidths=[100*mm], rowHeights=[14*mm]
        )
        step_box.setStyle(TableStyle([
            ("ALIGN",      (0,0),(-1,-1), "CENTER"),
            ("VALIGN",     (0,0),(-1,-1), "MIDDLE"),
            ("BOX",        (0,0),(-1,-1), 0.5, ROSE),
            ("BACKGROUND", (0,0),(-1,-1), CREAM),
        ]))

        row = Table([[step_box,
                      Paragraph(explanation, ParagraphStyle("je",
                        fontName="Times-Italic", fontSize=9, leading=14,
                        textColor=WARM))]],
                    colWidths=[105*mm, 80*mm])
        row.setStyle(TableStyle([
            ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
            ("LEFTPADDING",  (1,0),(1,-1), 10),
            ("TOPPADDING",   (0,0),(-1,-1), 2),
            ("BOTTOMPADDING",(0,0),(-1,-1), 2),
        ]))
        story.append(row)

        if i < len(journey_steps) - 1:
            story.append(Paragraph("↓", ParagraphStyle("arr",
                fontName="Times-Roman", fontSize=16, textColor=ROSE,
                alignment=TA_LEFT, spaceAfter=0, spaceBefore=2,
                leftIndent=43*mm)))

    story.append(sp(6))
    story.append(hr())
    story.append(eyebrow("Why Built This Way"))
    story.append(Paragraph(
        "The structure reflects the way trust works. You don't ask someone to buy something "
        "the moment they walk through the door. You let them feel the space. "
        "You show them who you are. Then — when they are already moved — "
        "you offer them a way to stay.",
        S["body"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 9 — 07: WORKSHOPS & EXPERIENCES
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("07 — Workshops & Experiences"))
    story.append(Paragraph("Workshops &\nExperiences", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "The workshops are not an afterthought. They are a core part of the brand — "
        "the place where Iza's art becomes participatory. She doesn't just make things. "
        "She creates conditions for other people to make things.",
        S["body"]))

    story.append(sp(4))
    story.append(eyebrow("The Program"))
    story.append(sp(2))

    workshops = [
        ("No experience needed",
         "The first card in the workshop section says this clearly. "
         "The program is designed for people who have never held a brush — "
         "and for people who forgot they wanted to."),
        ("All materials included",
         "You arrive. Everything is ready. "
         "The act of showing up is the whole task."),
        ("Small groups. Real presence.",
         "These are not classes. They are gatherings. "
         "The group size is intentionally small so that "
         "something real can happen between people."),
    ]
    for title, desc in workshops:
        story.append(KeepTogether([
            Paragraph(f"<b>{title}</b>", ParagraphStyle("wt",
                fontName="Times-Bold", fontSize=10.5, leading=14,
                textColor=ROSE, spaceAfter=3)),
            Paragraph(desc, ParagraphStyle("wd",
                fontName="Times-Roman", fontSize=10, leading=16,
                textColor=INK, spaceAfter=10)),
        ]))

    story.append(sp(4))
    story.append(hr())
    story.append(eyebrow("Brand Role of the Workshop Section"))
    story.append(Paragraph(
        "The workshop section appears after the gallery for a reason. "
        "By the time visitors arrive here, they have already seen the work. "
        "They have been moved. Now they are being invited in.",
        S["body"]))

    story.append(sp(4))
    story.append(Paragraph(
        '"Art brings people together. I have seen it happen, over and over — '
        'strangers becoming friends because they painted in the same room."',
        S["quote"]))
    story.append(Paragraph("— Iza Malika", S["quote_attr"]))

    story.append(sp(6))
    story.append(eyebrow("Visual World of the Workshops"))
    story.append(Paragraph(
        "The workshop photography section of the website uses an editorial mosaic — "
        "5 photographs arranged asymmetrically, each one revealing itself on scroll. "
        "Not a grid. Not a slideshow. A moment from inside the room.",
        S["body"]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 10 — 08: BRAND IN PRACTICE
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("08 — Brand in Practice"))
    story.append(Paragraph("Brand in Practice", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "The brand living across screen sizes. The design adapts — "
        "but the feeling stays the same.",
        S["body"]))

    story.append(sp(4))

    mockups = [
        ("Desktop  ·  1280px+",
         "The hero fills the screen. The name appears large — Iza Malika — "
         "centered in generous whitespace. The spiral canvas animation plays behind it. "
         "Navigation sits at the top with the language toggle at the right. "
         "The oracle section shows three buttons side by side, each opening a themed carousel "
         "that spans the full viewport width.",
         [
             "Full-width carousel with visible side cards",
             "Two-column layout for About (photo + text)",
             "Workshop cards in a 3-column grid",
             "Gallery in a 4-column masonry grid",
         ]),
        ("Tablet  ·  768px – 1280px",
         "The layout compresses gracefully. Oracle buttons remain side by side. "
         "Workshop cards shift to 2 columns. The gallery becomes a 3-column grid. "
         "Typography scales fluidly via clamp() — nothing snaps or breaks.",
         [
             "Gallery grid: 4 columns → 3 columns",
             "Workshop cards: 3 → 2 columns",
             "Navigation remains horizontal",
             "Carousel side cards slightly reduced",
         ]),
        ("Mobile  ·  375px – 640px",
         "The site becomes linear and vertical. One column. The hamburger menu appears. "
         "The oracle buttons stack. The gallery drops to 2 columns. "
         "Touch swipe is enabled on the carousel. "
         "Nothing is hidden — only reorganized.",
         [
             "Hamburger menu replaces navigation",
             "Oracle buttons stack vertically",
             "Gallery: 2-column grid",
             "Workshop cards: single column",
             "Carousel: full-width, swipe-enabled",
         ]),
    ]

    for device, desc, details in mockups:
        story.append(KeepTogether([
            Paragraph(device, ParagraphStyle("dt",
                fontName="Times-Bold", fontSize=11, leading=14,
                textColor=ROSE, spaceAfter=4)),
            Paragraph(desc, ParagraphStyle("dd",
                fontName="Times-Roman", fontSize=9.5, leading=15,
                textColor=INK, spaceAfter=6)),
            *[Paragraph(f"· {d}", ParagraphStyle("di",
                fontName="Times-Italic", fontSize=9, leading=14,
                textColor=WARM, leftIndent=10, spaceAfter=2)) for d in details],
            HRFlowable(width="100%", thickness=0.3, color=colors.HexColor("#e0d4c4"),
                       spaceAfter=10, spaceBefore=6),
        ]))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 11 — 09: HANDOFF PACKAGE
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(6))
    story.append(eyebrow("09 — Handoff Package"))
    story.append(Paragraph("Handoff Package", S["section_title"]))
    story.append(hr())

    story.append(Paragraph(
        "Everything you need to own, maintain, and evolve this project. "
        "Nothing is locked. Everything is yours.",
        S["body"]))

    story.append(sp(5))

    deliverables = [
        ("Website",
         "The complete, ready-to-deploy website. Pure HTML, CSS, and vanilla JavaScript — "
         "no frameworks, no subscriptions, no dependencies. "
         "Upload to GitHub Pages and you are live.",
         ["index.html — the complete page",
          "css/ — 4 focused stylesheets",
          "js/ — 7 ES module files, one responsibility each",
          "images/ — all artwork and workshop photographs"]),

        ("Brand Assets",
         "This Creative Project Book, plus machine-readable design tokens "
         "for every value used in the codebase — colors, typography, spacing, animation timings.",
         ["Iza_Malika_Creative_Project_Book.pdf",
          "design-tokens.json — all CSS values in JSON format"]),

        ("Documentation",
         "A complete technical guide written for someone who has never seen the code. "
         "How to edit text, replace images, add artworks, change the WhatsApp number, "
         "deploy to GitHub Pages, and set up a custom domain.",
         ["README.md — full technical reference"]),

        ("Backup",
         "The full project folder should be kept in a safe place — "
         "cloud storage, an external drive, or a GitHub repository. "
         "If something is accidentally deleted, everything can be restored.",
         ["Recommended: GitHub repository (free)",
          "Also: iCloud Drive, Google Drive, or Dropbox"]),

        ("Future Support",
         "The website was built to be editable without a developer. "
         "For larger changes — new sections, new features, redesigns — "
         "reach out directly.",
         ["Sebastián Ávila · avilalopezesp@gmail.com"]),
    ]

    for title, desc, items in deliverables:
        story.append(KeepTogether([
            Paragraph(title, ParagraphStyle("ht",
                fontName="Times-Bold", fontSize=11, leading=14,
                textColor=INK, spaceAfter=3)),
            Paragraph(desc, ParagraphStyle("hd",
                fontName="Times-Roman", fontSize=9.5, leading=15,
                textColor=INK, spaceAfter=4)),
            *[Paragraph(f"· {item}", ParagraphStyle("hi",
                fontName="Times-Italic", fontSize=9, leading=14,
                textColor=WARM, leftIndent=10, spaceAfter=2)) for item in items],
            HRFlowable(width="100%", thickness=0.3, color=colors.HexColor("#e0d4c4"),
                       spaceAfter=10, spaceBefore=6),
        ]))

    # Switch to thank you template
    story.append(NextPageTemplate("thankyou"))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE 12 — 10: THANK YOU
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(sp(72))
    story.append(Paragraph(
        "Thank you for trusting me with your story.",
        S["ty_big"]))

    story.append(sp(52))
    story.append(HRFlowable(width="30%", thickness=0.5, color=GOLD,
                             spaceAfter=8*mm, spaceBefore=0))
    story.append(Paragraph("Designed & developed by", S["ty_role"]))
    story.append(sp(2))
    story.append(Paragraph("Sebastián Ávila", S["ty_name"]))
    story.append(Paragraph("Creative Designer", S["ty_role"]))

    # Build
    doc.build(story)
    print(f"✓ PDF created: {OUTPUT}")

if __name__ == "__main__":
    build()
