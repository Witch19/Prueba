# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra cover letter PDF for Gulf Associates."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_Cover_Letter_Gulf_Associates.pdf"

TEXT = colors.HexColor("#2c2c2c")
MUTED = colors.HexColor("#555555")
ACCENT = colors.HexColor("#1A365D")


def main():
    base = getSampleStyleSheet()
    styles = {
        "header": ParagraphStyle(
            "Header", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=14, textColor=ACCENT, spaceAfter=2, leading=18,
        ),
        "meta": ParagraphStyle(
            "Meta", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=MUTED, spaceAfter=2, leading=13,
        ),
        "date": ParagraphStyle(
            "Date", parent=base["Normal"], fontName="Helvetica",
            fontSize=10, textColor=TEXT, spaceBefore=12, spaceAfter=12, leading=13,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.5, textColor=TEXT, alignment=TA_JUSTIFY,
            spaceAfter=10, leading=15,
        ),
        "sign": ParagraphStyle(
            "Sign", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.5, textColor=TEXT, spaceBefore=6, spaceAfter=2, leading=14,
        ),
    }

    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2.2 * cm, rightMargin=2.2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
    )

    story = [
        Paragraph("JOSELYN SAAVEDRA", styles["header"]),
        Paragraph("Quito, Ecuador | Fully remote", styles["meta"]),
        Paragraph(
            "+593 99 252 3644 | Josytst.js@gmail.com | "
            "linkedin.com/in/joselyn-saavedra-dev",
            styles["meta"],
        ),
        Paragraph("github.com/Witch19", styles["meta"]),
        Paragraph("Hiring Team<br/>Gulf Associates", styles["date"]),
        Paragraph(
            "Re: Application for Associate Frontend Developer",
            styles["date"],
        ),
        Paragraph("Hello,", styles["body"]),
        Paragraph(
            "I am applying for the <b>Associate Frontend Developer</b> role at "
            "Gulf Associates. I build and maintain clean, responsive interfaces "
            "with <b>HTML, CSS, and JavaScript</b> (plus TypeScript/React), with "
            "strong attention to detail when turning requirements into reliable UI.",
            styles["body"],
        ),
        Paragraph(
            "In my current remote role at Vidortec/Vigatec Chile, I collaborate "
            "with technical and non-technical stakeholders, fix bugs found in "
            "testing, document components clearly, and own delivery on deadlines. "
            "I am especially interested in making complex information easy to "
            "read on screen, so dashboards and tools actually support judgment, "
            "not just display data.",
            styles["body"],
        ),
        Paragraph(
            "I would welcome contributing to your Amsterdam client engagement "
            "and learning the commercial logic behind the interfaces we ship. "
            "I am fully available for remote work and can manage tasks "
            "independently with clear, direct communication.",
            styles["body"],
        ),
        Paragraph(
            "Selected work: "
            "https://github.com/Witch19/billing-ui &nbsp;|&nbsp; "
            "https://github.com/Witch19/pet-adoption-ui",
            styles["body"],
        ),
        Paragraph(
            "Thank you for your time. I look forward to hearing from you.",
            styles["body"],
        ),
        Paragraph("Sincerely,", styles["sign"]),
        Spacer(1, 8),
        Paragraph("<b>Joselyn Saavedra</b>", styles["sign"]),
        Paragraph("+593 99 252 3644 | Josytst.js@gmail.com", styles["meta"]),
    ]

    doc.build(story)
    print("Cover letter generated: " + OUTPUT)


if __name__ == "__main__":
    main()
