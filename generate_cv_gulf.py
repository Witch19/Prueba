# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for Gulf Associates Associate Frontend role."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Gulf_Associate_Frontend.pdf"

ACCENT = colors.HexColor("#1A365D")
TEXT = colors.HexColor("#2c2c2c")
MUTED = colors.HexColor("#555555")


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=20, textColor=ACCENT, spaceAfter=2, leading=24,
        ),
        "title": ParagraphStyle(
            "Title", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.5, textColor=MUTED, spaceAfter=4, leading=14,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=MUTED, spaceAfter=10, leading=13,
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=11, textColor=ACCENT, spaceBefore=8, spaceAfter=4, leading=14,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, alignment=TA_LEFT, spaceAfter=6, leading=13,
        ),
        "job_title": ParagraphStyle(
            "JobTitle", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10, textColor=TEXT, spaceBefore=4, spaceAfter=1, leading=13,
        ),
        "job_meta": ParagraphStyle(
            "JobMeta", parent=base["Normal"], fontName="Helvetica-Oblique",
            fontSize=9, textColor=MUTED, spaceAfter=3, leading=12,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, leftIndent=12, spaceAfter=2, leading=13,
        ),
        "skill": ParagraphStyle(
            "Skill", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, spaceAfter=2, leading=13,
        ),
    }


def section_rule():
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=0, spaceAfter=4)


def bullet(text, style):
    return Paragraph("\u2022 " + text, style)


def main():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.5 * cm, bottomMargin=1.5 * cm,
    )

    story = [
        Paragraph("JOSELYN SAAVEDRA", styles["name"]),
        Paragraph(
            "Associate Frontend Developer | HTML | CSS | JavaScript | "
            "Responsive UI | Documentation",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Fully remote | github.com/Witch19",
            styles["contact"],
        ),
        Paragraph(
            "+593 99 252 3644 &nbsp;|&nbsp; Josytst.js@gmail.com &nbsp;|&nbsp; "
            "linkedin.com/in/joselyn-saavedra-dev",
            styles["contact"],
        ),
        Paragraph("PROFESSIONAL SUMMARY", styles["section"]),
        section_rule(),
        Paragraph(
            "Associate-level frontend developer with 2+ years building and "
            "maintaining clean, functional user interfaces with <b>HTML</b>, "
            "<b>CSS</b>, and <b>JavaScript</b> (plus TypeScript/React). "
            "Strong attention to detail translating requirements and mockups "
            "into reliable, responsive UIs. Experience fixing bugs, writing "
            "clear component documentation, and explaining technical concepts "
            "to non-engineering stakeholders. Self-managed and deadline-driven "
            "in fully remote work. Curious about the business logic behind "
            "on-screen data and motivated to turn complex information into "
            "clear interactive interfaces that support decision-making.",
            styles["body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer (Frontend focus)",
            styles["job_title"],
        ),
        Paragraph("October 2023 - Present | Fully remote (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Build and maintain UIs with <b>HTML</b>, <b>CSS</b>, "
        "<b>JavaScript</b>, TypeScript, and React/Angular for internal "
        "and client-facing tools.",
        "Implement <b>responsive</b> designs that work across browsers "
        "and devices; improve UX based on stakeholder feedback.",
        "Turn requirements into clear interfaces; collaborate with "
        "technical and non-technical teammates.",
        "Debug issues found in testing; improve reliability and "
        "performance of frontend components.",
        "Draft <b>documentation</b> for components and flows so others "
        "can understand the underlying logic.",
        "Own tasks independently in a remote setup; meet delivery "
        "deadlines without heavy process overhead.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("June 2023 - August 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Built functional web interfaces from requirements using "
        "HTML/CSS/JavaScript and Angular; REST integration.",
        "Corrective UI maintenance; clear communication in agile teams.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("SELECTED PROJECTS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Billing UI - github.com/Witch19/billing-ui",
            "React, TypeScript, Tailwind CSS, forms & data-driven UI",
            [
                "Clear interface for structured data entry and review; "
                "focus on readability and maintainable components.",
            ],
        ),
        (
            "Pet Adoption UI - github.com/Witch19/pet-adoption-ui",
            "HTML/CSS/JS via React + TypeScript + Tailwind",
            [
                "Responsive web app built from the ground up with "
                "reusable UI and API integration.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "TypeScript frontend + APIs",
            [
                "Product-style UI demonstrating end-to-end web application "
                "structure.",
            ],
        ),
    ]
    for title, meta, items in projects:
        story.append(Paragraph(title, styles["job_title"]))
        story.append(Paragraph(meta, styles["job_meta"]))
        for item in items:
            story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("TECHNICAL SKILLS", styles["section"]))
    story.append(section_rule())
    skills = [
        (
            "Core web:",
            "HTML5, CSS3, JavaScript; CSS frameworks (Tailwind); "
            "responsive / cross-browser UI",
        ),
        (
            "Also:",
            "TypeScript, React, Angular; REST APIs; Git; basic charting / "
            "dashboard UI patterns (learning deepening)",
        ),
        (
            "Working style:",
            "Documentation, code reviews, bug fixing, remote self-management, "
            "clear communication with non-technical stakeholders",
        ),
        (
            "Mindset:",
            "Detail-oriented, logical problem-solving, curiosity about "
            "business logic behind presented data",
        ),
    ]
    for label, value in skills:
        story.append(Paragraph("<b>" + label + "</b> " + value, styles["skill"]))

    story.append(Paragraph("EDUCATION", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Technology Degree in Software Development - Universidad UTE",
            styles["body"],
        )
    )
    story.append(
        Paragraph("Mechatronics Engineering studies - Universidad UTE", styles["body"])
    )

    story.append(Paragraph("LANGUAGES", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "<b>Spanish:</b> Native &nbsp;|&nbsp; <b>English:</b> Intermediate "
            "(comfortable documenting and explaining UI logic in writing)",
            styles["body"],
        )
    )
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<i>GitHub: https://github.com/Witch19 | References available upon request</i>",
        styles["body"],
    ))

    doc.build(story)
    print("CV generated: " + OUTPUT)


if __name__ == "__main__":
    main()
