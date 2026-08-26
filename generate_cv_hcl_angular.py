# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for HCLTech Front-End Developer (Angular)."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_HCL_Angular_Frontend.pdf"

ACCENT = colors.HexColor("#0F62FE")
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
            "Front-End Developer | Angular | TypeScript | HTML/CSS | REST | Azure DevOps",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remote / virtual-first | github.com/Witch19",
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
            "Front-end developer with 2+ years building responsive web applications "
            "using <b>Angular</b>, <b>TypeScript</b>, <b>JavaScript (ES6+)</b>, "
            "<b>HTML5</b>, and <b>CSS3</b>. Experience creating reusable UI "
            "components, integrating <b>RESTful APIs</b>, and collaborating with "
            "backend and product teams in remote environments. Strong with "
            "<b>Git</b>, Agile practices, code reviews, and <b>CI/CD</b> via "
            "<b>Azure DevOps / Azure Pipelines</b>. Also proficient in React "
            "(Context API) for state patterns. Motivated to deepen Azure App "
            "Services, Azure AD / Entra ID authentication, and performance "
            "optimization within a global engineering culture.",
            styles["body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer (Front-End focus)",
            styles["job_title"],
        ),
        Paragraph("October 2023 - Present | Remote (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Develop and maintain responsive UIs with <b>Angular</b>, "
        "<b>TypeScript</b>, <b>JavaScript</b>, HTML5, and CSS3.",
        "Build reusable components; integrate frontends with <b>REST APIs</b> "
        "and corporate backend services.",
        "Collaborate with backend, DevOps, and functional teams; participate "
        "in Agile ceremonies and code reviews.",
        "Optimize UI behavior and fix cross-browser / responsiveness issues "
        "in test and production.",
        "Version control with <b>Git</b>; CI/CD pipelines in "
        "<b>Azure DevOps</b> (Azure Pipelines).",
        "Work with authentication flows (JWT) and role-aware UI behavior "
        "in enterprise applications.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("June 2023 - August 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Built web interfaces with <b>Angular</b>, TypeScript, HTML, and CSS; "
        "REST API integration.",
        "Corrective UI maintenance; Agile delivery with Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("SELECTED PROJECTS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "Angular, TypeScript, .NET APIs, responsive UI",
            [
                "Angular frontend with reusable components and REST "
                "integration in a full-stack app.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, Context/state patterns, REST, JWT",
            [
                "Modern UI work demonstrating component design and "
                "client-side state management.",
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
            "Required:",
            "Angular, JavaScript (ES6+), TypeScript, HTML5, CSS3, "
            "REST API integration, Git",
        ),
        (
            "State / UI:",
            "Angular services & reactive patterns; React Context API; "
            "Redux (learning / transferable concepts)",
        ),
        (
            "Preferred / Azure:",
            "Azure DevOps, Azure Pipelines; Azure App Service / Static Web Apps "
            "and Azure AD / Entra ID (active learning)",
        ),
        (
            "Also:",
            "CI/CD, Agile/Scrum, code reviews, performance & responsiveness; "
            "Next.js / Docker (basic / learning)",
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
            "<b>Spanish:</b> Native &nbsp;|&nbsp; <b>English:</b> Intermediate",
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
