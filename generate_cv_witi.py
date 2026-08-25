# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Full Stack CV for WiTi Senior role (honest)."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_WiTi_FullStack.pdf"

ACCENT = colors.HexColor("#5B2C6F")
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
            "Full Stack Developer | TypeScript | NestJS | React | PostgreSQL | MongoDB",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remoto LATAM | github.com/Witch19",
            styles["contact"],
        ),
        Paragraph(
            "+593 99 252 3644 &nbsp;|&nbsp; Josytst.js@gmail.com &nbsp;|&nbsp; "
            "linkedin.com/in/joselyn-saavedra-dev",
            styles["contact"],
        ),
        Paragraph("PERFIL PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Desarrolladora Full Stack con m\u00e1s de 2 a\u00f1os de experiencia "
            "en aplicaciones web productivas con stack <b>JavaScript/TypeScript</b>. "
            "Backend con <b>Node.js</b> y <b>NestJS</b>; frontend con <b>React</b> "
            "(Hooks) y Angular. Experiencia en <b>PostgreSQL</b> y <b>MongoDB</b>, "
            "APIs REST, Git, CI/CD (Azure DevOps) y metodolog\u00edas \u00e1giles. "
            "Uso diario de herramientas de <b>IA</b> (Cursor, Copilot, ChatGPT) "
            "para acelerar delivery. Proyecto personal tipo eCommerce "
            "(tienda_bnk). Sin seniority senior ni experiencia productiva "
            "profunda en AWS (Lambda/SQS/EventBridge), Terraform/CloudFormation "
            "ni ETL; motivaci\u00f3n alta por crecer en cloud, event-driven "
            "y arquitecturas de alto tr\u00e1fico.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo full stack con <b>TypeScript</b>, <b>Node.js</b>, "
        "<b>NestJS</b>, <b>React</b> y .NET en aplicaciones corporativas "
        "en producci\u00f3n.",
        "Dise\u00f1o e integraci\u00f3n de <b>APIs REST</b>; modelado y "
        "consultas en <b>PostgreSQL</b>, SQL Server y <b>MongoDB</b>.",
        "Componentes frontend reutilizables con React (Hooks) / Angular; "
        "mantenimiento evolutivo y resoluci\u00f3n de incidencias.",
        "Git, code reviews, pipelines <b>CI/CD</b> en Azure DevOps; "
        "trabajo \u00e1gil (Scrum/Jira) con equipos multidisciplinarios.",
        "Documentaci\u00f3n t\u00e9cnica y uso de IA para acelerar "
        "desarrollo, debugging y calidad.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo frontend con Angular, TypeScript y JavaScript; "
        "integraci\u00f3n con APIs.",
        "Mantenimiento de interfaces; trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "eCommerce full stack: .NET 8, Angular, microservicios, APIs REST",
            [
                "Plataforma tipo retail/ecommerce con cat\u00e1logo, "
                "servicios e integraciones API.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, Hooks, Tailwind, REST, JWT",
            [
                "Frontends React/TS con estado de UI, autenticaci\u00f3n "
                "e integraci\u00f3n backend.",
            ],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "APIs REST, PostgreSQL, JWT, reglas de negocio",
            [
                "API con modelado relacional, autenticaci\u00f3n y "
                "documentaci\u00f3n t\u00e9cnica.",
            ],
        ),
    ]
    for title, meta, items in projects:
        story.append(Paragraph(title, styles["job_title"]))
        story.append(Paragraph(meta, styles["job_meta"]))
        for item in items:
            story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("HABILIDADES T\u00c9CNICAS", styles["section"]))
    story.append(section_rule())
    skills = [
        (
            "Backend:",
            "NestJS, Node.js, TypeScript, APIs REST; microservicios "
            "(conocimiento aplicado en proyectos)",
        ),
        (
            "Frontend:",
            "React.js (Hooks), TypeScript, Angular; estado (Context); "
            "Zustand/Redux y Next.js (aprendizaje activo)",
        ),
        ("Datos:", "PostgreSQL, MongoDB, SQL Server"),
        (
            "Cloud / IaC:",
            "Azure DevOps CI/CD; AWS (Lambda, S3, SQS, SNS, EventBridge, "
            "DynamoDB) y Terraform/CloudFormation (aprendizaje activo, "
            "sin producci\u00f3n profunda)",
        ),
        (
            "Pr\u00e1cticas:",
            "Git/GitHub, Scrum/Kanban, Jira, Clean Code, Docker (b\u00e1sico); "
            "ETL / event-driven (inter\u00e9s y aprendizaje)",
        ),
        (
            "IA:",
            "Cursor, GitHub Copilot, ChatGPT, Claude \u2014 uso diario "
            "para acelerar delivery",
        ),
    ]
    for label, value in skills:
        story.append(Paragraph("<b>" + label + "</b> " + value, styles["skill"]))

    story.append(Paragraph("EDUCACI\u00d3N", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Tecnolog\u00eda en Desarrollo de Software - Universidad UTE",
            styles["body"],
        )
    )
    story.append(
        Paragraph("Ingenier\u00eda en Mecatr\u00f3nica - Universidad UTE", styles["body"])
    )

    story.append(Paragraph("IDIOMAS", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "<b>Espa\u00f1ol:</b> Nativo &nbsp;|&nbsp; <b>Ingl\u00e9s:</b> Intermedio",
            styles["body"],
        )
    )
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<i>GitHub: https://github.com/Witch19 | Referencias disponibles a solicitud</i>",
        styles["body"],
    ))

    doc.build(story)
    print("CV generado: " + OUTPUT)


if __name__ == "__main__":
    main()
