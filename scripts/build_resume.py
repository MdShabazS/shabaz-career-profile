#!/usr/bin/env python3
"""Build the master resume as an ATS-friendly PDF and DOCX from one content source.

PDF  -> reportlab (single column, selectable text, clickable links, one page)
DOCX -> python-docx (single column, live hyperlinks)

Run: python3 scripts/build_resume.py
Outputs: resume/Mohammed_Shabaz_S_Master_Resume.pdf and .docx
Keep the content here in sync with resume/master-resume.md.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "resume")
BASENAME = "Mohammed_Shabaz_S_Master_Resume"
LINK = "#1155cc"

NAME = "MOHAMMED SHABAZ S"
TITLE = "Software Developer | Embedded Engineer"
EMAIL = "md.shabaz.2005@gmail.com"
PHONE = "7975512403"
LINKEDIN_URL = "https://www.linkedin.com/in/shabaz17/"
LINKEDIN_TXT = "linkedin.com/in/shabaz17"
GITHUB_URL = "https://github.com/MdShabazS"
GITHUB_TXT = "github.com/MdShabazS"
LOCATION = "Ballari, Karnataka, India"

SUMMARY = ("Final-year Electronics & Communication Engineering student (CGPA 8.38) working "
           "across application software and embedded firmware. Internship experience at Nokia "
           "and iHelp Robotics, with projects in Android, computer vision, and microcontrollers "
           "using C/C++, Python, and Embedded C.")

EDUCATION = [
    "Ballari Institute of Technology and Management (BITM) — Ballari, Karnataka",
    "B.E. Electronics & Communication Engineering | Final Year | Expected 2027 | CGPA 8.38",
    "Class 12: 80% | Class 10: 86.88%",
]

SKILLS = [
    ("Languages", "C, C++, Python, Java, SQL"),
    ("Software & Tools", "Android Studio, OpenCV, Firebase, Git, GitHub"),
    ("Embedded", "Embedded C, Microcontrollers"),
    ("CS Fundamentals", "Data Structures & Algorithms, DBMS, Operating Systems, Computer Networks"),
]

# (title line, meta line, [bullets])
EXPERIENCE = [
    ("Nokia Solutions and Networks India — Student Intern",
     "Bangalore | Sep 2026 – Present",
     ["Student intern contributing to engineering work; project scope is covered by company confidentiality."]),
    ("iHelp Robotics Private Limited — AI Research Intern, Deep Learning & Model Development",
     "Remote | Mar 2026 – Aug 2026 | Project: MITRA",
     ["Improved live camera-stream reliability in the MITRA assistive Android app: reduced WiFi/RTSP stream search delay, persisted the last working transport, and added refresh/stall recovery.",
      "Built a visual-freeze watchdog that reconnects when frame counters advance but the image stalls; added on-screen stream- and cloud-status panels and a guard that sends frames only when the cloud WebSocket is connected.",
      "Hardened offline voice commands (offline-preferred speech recognition with model recovery and microphone retry backoff); verified builds across devices with Gradle test/lint/assemble runs and captured logs. Backend and model work were handled by another team."]),
    ("IEEE EMBS Pune Section — Student Intern, Skin Disease Classification",
     "Remote | Jun 2026",
     ["Built a demo-level skin-disease image classifier with a 3-person team: model selection, training, evaluation, image processing, UI, and testing in Python."]),
]

# (title, stack/meta, [bullets])
PROJECTS = [
    ("VisionPay — Individual",
     "Python, MobileNetV2, TensorFlow Lite, OpenCV | github.com/MdShabazS/visionpay",
     ["Built an offline Indian-currency recognizer with spoken feedback for low-vision users: trained a MobileNetV2 model, converted it to TensorFlow Lite, and ran real-time webcam inference with text-to-speech.",
      "Collected ~400 images per denomination across 6 note classes; added confidence/margin gating, temporal smoothing, a background class, and auto-count mode; reported ~93% validation accuracy."]),
    ("Automotive Body Control Module — Individual",
     "ESP32, Embedded C | github.com/MdShabazS/Automotive-Body-Control-Module-ESP32",
     ["Built an ESP32 body-control-module prototype with an OFF/ACC/ON ignition state machine, indicators, synchronized hazard mode, and an OLED dashboard.",
      "Structured the firmware around non-blocking millis()-based scheduling with brake debouncing, GPIO abstraction, and edge-triggered serial logging."]),
    ("AEGIS — Team (lead), design stage / in progress",
     "",
     ["Leading a 3-person team designing AEGIS, an AI-assisted emergency-response platform: defined a 15-stage incident workflow where AI analyzes and recommends and a human dispatcher verifies before resources are dispatched."]),
]

LEADERSHIP = [
    "Vice-Chair, IEEE CAS Society, IEEE Student Branch BITM (previously Treasurer)",
    "Treasurer, BITM Robotics Club",
    "Google Student Ambassador, 2025",
    "Selected Participant, IEEE SPACE 2026 — B.Tech Initiative",
]

CERTS = ("Embedded Systems — Internshala Trainings (2025) | Python Programming — EISystems (2024) | "
         "Google Cloud Generative AI — SmartBridge/SmartInternz (2025) | SQL for Data Analytics with AI | "
         "Programming in C and C++ with AI")

LANGS = "English, Kannada, Hindi, Urdu"


# ---------------------------------------------------------------- PDF (reportlab)
def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
    from reportlab.lib.colors import HexColor

    path = os.path.join(OUT, BASENAME + ".pdf")
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=12 * mm, rightMargin=12 * mm,
                            topMargin=8 * mm, bottomMargin=8 * mm,
                            title="Mohammed Shabaz S — Resume", author="Mohammed Shabaz S")
    dark = HexColor("#111827")
    name_st = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15, leading=16,
                             textColor=dark, alignment=TA_LEFT, spaceAfter=1)
    title_st = ParagraphStyle("title", fontName="Helvetica", fontSize=10, leading=12,
                              textColor=dark, spaceAfter=1)
    contact_st = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.3, leading=10.5,
                                textColor=dark)
    head_st = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=9.2, leading=10.5,
                             textColor=dark, spaceBefore=3.5, spaceAfter=0.5)
    body_st = ParagraphStyle("body", fontName="Helvetica", fontSize=8.6, leading=10.5, textColor=dark)
    entry_st = ParagraphStyle("entry", fontName="Helvetica-Bold", fontSize=8.9, leading=10.6,
                              textColor=dark, spaceBefore=2)
    meta_st = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8.3, leading=10,
                             textColor=dark)
    bullet_st = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.6, leading=10.3,
                               textColor=dark, leftIndent=9, bulletIndent=0, spaceBefore=0.4)

    story = []

    def rule():
        story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#9ca3af"),
                                spaceBefore=1, spaceAfter=2))

    def section(name):
        story.append(Paragraph(name, head_st))
        rule()

    def bullets(items):
        for b in items:
            story.append(Paragraph(b, bullet_st, bulletText="•"))

    story.append(Paragraph(NAME, name_st))
    story.append(Paragraph(TITLE, title_st))
    contact = (f'{LOCATION} | {PHONE} | '
               f'<a href="mailto:{EMAIL}" color="{LINK}">{EMAIL}</a> | '
               f'<a href="{LINKEDIN_URL}" color="{LINK}">{LINKEDIN_TXT}</a> | '
               f'<a href="{GITHUB_URL}" color="{LINK}">{GITHUB_TXT}</a> | '
               f'Portfolio: available on request')
    story.append(Paragraph(contact, contact_st))

    section("SUMMARY")
    story.append(Paragraph(SUMMARY, body_st))

    section("EDUCATION")
    for i, line in enumerate(EDUCATION):
        story.append(Paragraph(("<b>%s</b>" % line) if i == 0 else line, body_st))

    section("SKILLS")
    for label, val in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {val}", body_st))

    section("EXPERIENCE")
    for title, meta, items in EXPERIENCE:
        story.append(Paragraph(title, entry_st))
        if meta:
            story.append(Paragraph(meta, meta_st))
        bullets(items)

    section("PROJECTS")
    for title, meta, items in PROJECTS:
        story.append(Paragraph(title, entry_st))
        if meta:
            story.append(Paragraph(meta, meta_st))
        bullets(items)

    section("LEADERSHIP & ACTIVITIES")
    bullets(LEADERSHIP)

    section("CERTIFICATIONS")
    story.append(Paragraph(CERTS, body_st))

    section("LANGUAGES")
    story.append(Paragraph(LANGS, body_st))

    doc.build(story)
    return path


# ---------------------------------------------------------------- DOCX (python-docx)
def _add_hyperlink(paragraph, url, text):
    from docx.oxml.shared import OxmlElement, qn
    part = paragraph.part
    r_id = part.relate_to(url,
                          "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                          is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "1155CC")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    new_run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink


def build_docx():
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    path = os.path.join(OUT, BASENAME + ".docx")
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.5)
        s.left_margin = s.right_margin = Inches(0.55)

    def spacing(p, before=0, after=2, line=1.0):
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.line_spacing = line

    def heading(text):
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(10.5)
        spacing(p, before=6, after=1)
        # bottom border
        pPr = p._p.get_or_add_pPr()
        pbdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single")
        bottom.set(qn("w:sz"), "6")
        bottom.set(qn("w:space"), "1")
        bottom.set(qn("w:color"), "9CA3AF")
        pbdr.append(bottom)
        pPr.append(pbdr)

    def bullet(text):
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(text)
        spacing(p, before=0, after=1.5)
        return p

    # header
    p = doc.add_paragraph()
    r = p.add_run(NAME)
    r.bold = True
    r.font.size = Pt(16)
    spacing(p, after=0)
    p = doc.add_paragraph()
    p.add_run(TITLE).font.size = Pt(10.5)
    spacing(p, after=1)
    p = doc.add_paragraph()
    p.add_run(f"{LOCATION} | {PHONE} | ").font.size = Pt(9)
    _add_hyperlink(p, f"mailto:{EMAIL}", EMAIL)
    p.add_run(" | ").font.size = Pt(9)
    _add_hyperlink(p, LINKEDIN_URL, LINKEDIN_TXT)
    p.add_run(" | ").font.size = Pt(9)
    _add_hyperlink(p, GITHUB_URL, GITHUB_TXT)
    p.add_run(" | Portfolio: available on request").font.size = Pt(9)
    spacing(p, after=2)

    heading("SUMMARY")
    p = doc.add_paragraph(); p.add_run(SUMMARY); spacing(p, after=2)

    heading("EDUCATION")
    for i, line in enumerate(EDUCATION):
        p = doc.add_paragraph(); run = p.add_run(line); run.bold = (i == 0); spacing(p, after=1)

    heading("SKILLS")
    for label, val in SKILLS:
        p = doc.add_paragraph(); p.add_run(f"{label}: ").bold = True; p.add_run(val); spacing(p, after=1)

    heading("EXPERIENCE")
    for title, meta, items in EXPERIENCE:
        p = doc.add_paragraph(); p.add_run(title).bold = True; spacing(p, before=3, after=0)
        if meta:
            p = doc.add_paragraph(); ri = p.add_run(meta); ri.italic = True; ri.font.size = Pt(9); spacing(p, after=1)
        for b in items:
            bullet(b)

    heading("PROJECTS")
    for title, meta, items in PROJECTS:
        p = doc.add_paragraph(); p.add_run(title).bold = True; spacing(p, before=3, after=0)
        if meta:
            p = doc.add_paragraph(); ri = p.add_run(meta); ri.italic = True; ri.font.size = Pt(9); spacing(p, after=1)
        for b in items:
            bullet(b)

    heading("LEADERSHIP & ACTIVITIES")
    for b in LEADERSHIP:
        bullet(b)

    heading("CERTIFICATIONS")
    p = doc.add_paragraph(); p.add_run(CERTS); spacing(p, after=2)

    heading("LANGUAGES")
    p = doc.add_paragraph(); p.add_run(LANGS); spacing(p, after=0)

    doc.save(path)
    return path


if __name__ == "__main__":
    pdf = build_pdf()
    docx_path = build_docx()
    print("Wrote:", os.path.relpath(pdf, ROOT))
    print("Wrote:", os.path.relpath(docx_path, ROOT))
    try:
        import fitz
        d = fitz.open(pdf)
        print(f"PDF pages: {d.page_count}")
    except Exception as e:
        print("page count check skipped:", e)
