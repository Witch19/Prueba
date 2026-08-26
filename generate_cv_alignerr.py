# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for Alignerr JavaScript evaluation role."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Alignerr_JavaScript.pdf"

ACCENT = colors.HexColor("#111827")
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
            "JavaScript Developer | React | Node.js | TypeScript | Code Quality & Review",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remote | Flexible hours | github.com/Witch19",
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
            "Software developer with 2+ years of hands-on <b>JavaScript</b> and "
            "<b>TypeScript</b> experience building and maintaining web and backend "
            "applications. Strong command of modern ES6+ patterns "
            "(async/await, closures, modules), <b>React</b>, <b>Node.js</b>, "
            "DOM/UI work, and REST APIs. Detail-oriented debugger who writes "
            "clear technical explanations and documentation. Experienced working "
            "independently and asynchronously in fully remote settings. Daily "
            "user of AI coding tools (Cursor, Copilot, ChatGPT) with a practical "
            "eye for what makes generated code correct, efficient, and "
            "maintainable. Motivated to evaluate AI-generated JavaScript and "
            "provide structured, actionable feedback.",
            styles["body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer",
            styles["job_title"],
        ),
        Paragraph("October 2023 - Present | Remote (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Develop and maintain production web apps with <b>JavaScript</b>, "
        "<b>TypeScript</b>, <b>React</b>, and <b>Node.js</b> (plus .NET).",
        "Write and review clean, readable code; identify bugs, edge cases, "
        "and failure points in frontend and backend flows.",
        "Implement async logic (Promises/async-await), API integrations, "
        "and DOM/UI behavior aligned with modern ES6+ practices.",
        "Document technical solutions clearly; communicate trade-offs and "
        "fixes to technical and non-technical teammates.",
        "Work independently and asynchronously in a remote setup using "
        "Git, Azure DevOps, and agile workflows.",
        "Use AI assistants daily while validating outputs for correctness "
        "and code quality before shipping.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("June 2023 - August 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Built UI features with JavaScript/TypeScript and Angular; "
        "integrated REST APIs.",
        "Performed corrective maintenance and issue analysis on web interfaces.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("SELECTED PROJECTS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI - github.com/Witch19/pet-adoption-ui",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            [
                "Modern React UI with clean component structure and "
                "backend integration.",
            ],
        ),
        (
            "Billing UI - github.com/Witch19/billing-ui",
            "React, TypeScript, forms, API-driven state",
            [
                "Frontend focused on readable logic, validation, and "
                "maintainable UI flows.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "Full stack: Angular/TypeScript + .NET APIs",
            [
                "End-to-end web solution demonstrating JS/TS frontend "
                "discipline and API consumption.",
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
            "JavaScript core:",
            "ES6+, async/await, Promises, closures, modules, DOM, "
            "error handling, debugging",
        ),
        (
            "Frameworks:",
            "React, Node.js, TypeScript; Angular; Vue (familiarity / learning)",
        ),
        (
            "Quality / writing:",
            "Code review mindset, bug hunting, edge cases, technical "
            "writing, structured feedback",
        ),
        (
            "Backend / APIs:",
            "REST APIs, JWT auth, Node.js services, SQL/NoSQL basics",
        ),
        (
            "Tools:",
            "Git/GitHub, Azure DevOps, Jira; AI pair-programming "
            "(Cursor, Copilot, ChatGPT)",
        ),
        (
            "Nice-to-have:",
            "No formal RLHF/data-labeling role yet; strong transfer from "
            "daily AI-assisted coding + QA-style debugging",
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
            "(comfortable writing technical explanations)",
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
